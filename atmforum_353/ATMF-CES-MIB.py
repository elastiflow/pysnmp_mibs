# SNMP MIB module (ATMF-CES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/atmforum_353/ATMF-CES-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:04:44 2025
# On host e-ws1-mac.muc.elastiflow.net platform Darwin version 24.3.0 by user rob
# Using Python version 3.13.3 (main, Apr  8 2025, 13:54:08) [Clang 16.0.0 (clang-1600.0.26.6)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn) = mibBuilder.importSymbols(
    "RFC1212",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn")

(NotificationType,) = mibBuilder.importSymbols(
    "RFC1215",
    "NotificationType")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(DisplayString,) = mibBuilder.importSymbols(
    "SNMPv2-TC-v1",
    "DisplayString")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AtmForum_ObjectIdentity = ObjectIdentity
atmForum = _AtmForum_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353)
)
_AtmForumNetworkManagement_ObjectIdentity = ObjectIdentity
atmForumNetworkManagement = _AtmForumNetworkManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5)
)
_AtmfCESmib_ObjectIdentity = ObjectIdentity
atmfCESmib = _AtmfCESmib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 2)
)
_AtmfDS1E1CESmib_ObjectIdentity = ObjectIdentity
atmfDS1E1CESmib = _AtmfDS1E1CESmib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 1)
)
_AtmfDS1E1CESConfTable_Object = MibTable
atmfDS1E1CESConfTable = _AtmfDS1E1CESConfTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 1, 1)
)
if mibBuilder.loadTexts:
    atmfDS1E1CESConfTable.setStatus("mandatory")
_AtmfDS1E1CESConfEntry_Object = MibTableRow
atmfDS1E1CESConfEntry = _AtmfDS1E1CESConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 1, 1, 1)
)
atmfDS1E1CESConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    atmfDS1E1CESConfEntry.setStatus("mandatory")
_AtmfDS1E1CESMapATMIndex_Type = Integer32
_AtmfDS1E1CESMapATMIndex_Object = MibTableColumn
atmfDS1E1CESMapATMIndex = _AtmfDS1E1CESMapATMIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 1, 1, 1, 1),
    _AtmfDS1E1CESMapATMIndex_Type()
)
atmfDS1E1CESMapATMIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfDS1E1CESMapATMIndex.setStatus("mandatory")
_AtmfDS1E1CESMapVPI_Type = Integer32
_AtmfDS1E1CESMapVPI_Object = MibTableColumn
atmfDS1E1CESMapVPI = _AtmfDS1E1CESMapVPI_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 1, 1, 1, 2),
    _AtmfDS1E1CESMapVPI_Type()
)
atmfDS1E1CESMapVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfDS1E1CESMapVPI.setStatus("mandatory")
_AtmfDS1E1CESMapVCI_Type = Integer32
_AtmfDS1E1CESMapVCI_Object = MibTableColumn
atmfDS1E1CESMapVCI = _AtmfDS1E1CESMapVCI_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 1, 1, 1, 3),
    _AtmfDS1E1CESMapVCI_Type()
)
atmfDS1E1CESMapVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfDS1E1CESMapVCI.setStatus("mandatory")


class _AtmfDS1E1CESCBRService_Type(Integer32):
    """Custom type atmfDS1E1CESCBRService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unstructured", 1),
          ("structured", 2))
    )


_AtmfDS1E1CESCBRService_Type.__name__ = "Integer32"
_AtmfDS1E1CESCBRService_Object = MibTableColumn
atmfDS1E1CESCBRService = _AtmfDS1E1CESCBRService_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 1, 1, 1, 4),
    _AtmfDS1E1CESCBRService_Type()
)
atmfDS1E1CESCBRService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmfDS1E1CESCBRService.setStatus("mandatory")


class _AtmfDS1E1CESCBRClockMode_Type(Integer32):
    """Custom type atmfDS1E1CESCBRClockMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("synchronous", 1),
          ("srts", 2),
          ("adaptive", 3))
    )


_AtmfDS1E1CESCBRClockMode_Type.__name__ = "Integer32"
_AtmfDS1E1CESCBRClockMode_Object = MibTableColumn
atmfDS1E1CESCBRClockMode = _AtmfDS1E1CESCBRClockMode_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 1, 1, 1, 5),
    _AtmfDS1E1CESCBRClockMode_Type()
)
atmfDS1E1CESCBRClockMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmfDS1E1CESCBRClockMode.setStatus("mandatory")


class _AtmfDS1E1CESCas_Type(Integer32):
    """Custom type atmfDS1E1CESCas based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("basic", 1),
          ("e1Cas", 2),
          ("ds1SfCas", 3),
          ("ds1EsfCas", 4))
    )


_AtmfDS1E1CESCas_Type.__name__ = "Integer32"
_AtmfDS1E1CESCas_Object = MibTableColumn
atmfDS1E1CESCas = _AtmfDS1E1CESCas_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 1, 1, 1, 6),
    _AtmfDS1E1CESCas_Type()
)
atmfDS1E1CESCas.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmfDS1E1CESCas.setStatus("mandatory")


class _AtmfDS1E1CESPartialFill_Type(Integer32):
    """Custom type atmfDS1E1CESPartialFill based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 47),
    )


_AtmfDS1E1CESPartialFill_Type.__name__ = "Integer32"
_AtmfDS1E1CESPartialFill_Object = MibTableColumn
atmfDS1E1CESPartialFill = _AtmfDS1E1CESPartialFill_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 1, 1, 1, 7),
    _AtmfDS1E1CESPartialFill_Type()
)
atmfDS1E1CESPartialFill.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmfDS1E1CESPartialFill.setStatus("mandatory")


class _AtmfDS1E1CESBufMaxSize_Type(Integer32):
    """Custom type atmfDS1E1CESBufMaxSize based on Integer32"""
    defaultValue = 256

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_AtmfDS1E1CESBufMaxSize_Type.__name__ = "Integer32"
_AtmfDS1E1CESBufMaxSize_Object = MibTableColumn
atmfDS1E1CESBufMaxSize = _AtmfDS1E1CESBufMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 1, 1, 1, 8),
    _AtmfDS1E1CESBufMaxSize_Type()
)
atmfDS1E1CESBufMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmfDS1E1CESBufMaxSize.setStatus("mandatory")


class _AtmfDS1E1CESCDVRxT_Type(Integer32):
    """Custom type atmfDS1E1CESCDVRxT based on Integer32"""
    defaultValue = 100


_AtmfDS1E1CESCDVRxT_Type.__name__ = "Integer32"
_AtmfDS1E1CESCDVRxT_Object = MibTableColumn
atmfDS1E1CESCDVRxT = _AtmfDS1E1CESCDVRxT_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 1, 1, 1, 9),
    _AtmfDS1E1CESCDVRxT_Type()
)
atmfDS1E1CESCDVRxT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmfDS1E1CESCDVRxT.setStatus("mandatory")


class _AtmfDS1E1CESCellLossIntegrationPeriod_Type(Integer32):
    """Custom type atmfDS1E1CESCellLossIntegrationPeriod based on Integer32"""
    defaultValue = 2500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 65535),
    )


_AtmfDS1E1CESCellLossIntegrationPeriod_Type.__name__ = "Integer32"
_AtmfDS1E1CESCellLossIntegrationPeriod_Object = MibTableColumn
atmfDS1E1CESCellLossIntegrationPeriod = _AtmfDS1E1CESCellLossIntegrationPeriod_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 1, 1, 1, 10),
    _AtmfDS1E1CESCellLossIntegrationPeriod_Type()
)
atmfDS1E1CESCellLossIntegrationPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmfDS1E1CESCellLossIntegrationPeriod.setStatus("mandatory")
_AtmfDS1E1CESStatsTable_Object = MibTable
atmfDS1E1CESStatsTable = _AtmfDS1E1CESStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 1, 2)
)
if mibBuilder.loadTexts:
    atmfDS1E1CESStatsTable.setStatus("mandatory")
_AtmfDS1E1CESStatsEntry_Object = MibTableRow
atmfDS1E1CESStatsEntry = _AtmfDS1E1CESStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 1, 2, 1)
)
atmfDS1E1CESStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    atmfDS1E1CESStatsEntry.setStatus("mandatory")
_AtmfDS1E1CESReassCells_Type = Counter32
_AtmfDS1E1CESReassCells_Object = MibTableColumn
atmfDS1E1CESReassCells = _AtmfDS1E1CESReassCells_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 1, 2, 1, 1),
    _AtmfDS1E1CESReassCells_Type()
)
atmfDS1E1CESReassCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfDS1E1CESReassCells.setStatus("mandatory")
_AtmfDS1E1CESHdrErrors_Type = Counter32
_AtmfDS1E1CESHdrErrors_Object = MibTableColumn
atmfDS1E1CESHdrErrors = _AtmfDS1E1CESHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 1, 2, 1, 2),
    _AtmfDS1E1CESHdrErrors_Type()
)
atmfDS1E1CESHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfDS1E1CESHdrErrors.setStatus("mandatory")
_AtmfDS1E1CESPointerReframes_Type = Counter32
_AtmfDS1E1CESPointerReframes_Object = MibTableColumn
atmfDS1E1CESPointerReframes = _AtmfDS1E1CESPointerReframes_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 1, 2, 1, 3),
    _AtmfDS1E1CESPointerReframes_Type()
)
atmfDS1E1CESPointerReframes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfDS1E1CESPointerReframes.setStatus("mandatory")
_AtmfDS1E1CESLostCells_Type = Counter32
_AtmfDS1E1CESLostCells_Object = MibTableColumn
atmfDS1E1CESLostCells = _AtmfDS1E1CESLostCells_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 1, 2, 1, 4),
    _AtmfDS1E1CESLostCells_Type()
)
atmfDS1E1CESLostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfDS1E1CESLostCells.setStatus("mandatory")
_AtmfDS1E1CESBufUnderflows_Type = Counter32
_AtmfDS1E1CESBufUnderflows_Object = MibTableColumn
atmfDS1E1CESBufUnderflows = _AtmfDS1E1CESBufUnderflows_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 1, 2, 1, 5),
    _AtmfDS1E1CESBufUnderflows_Type()
)
atmfDS1E1CESBufUnderflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfDS1E1CESBufUnderflows.setStatus("mandatory")
_AtmfDS1E1CESBufOverflows_Type = Counter32
_AtmfDS1E1CESBufOverflows_Object = MibTableColumn
atmfDS1E1CESBufOverflows = _AtmfDS1E1CESBufOverflows_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 1, 2, 1, 6),
    _AtmfDS1E1CESBufOverflows_Type()
)
atmfDS1E1CESBufOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfDS1E1CESBufOverflows.setStatus("mandatory")


class _AtmfDS1E1CESCellLossStatus_Type(Integer32):
    """Custom type atmfDS1E1CESCellLossStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noLoss", 1),
          ("loss", 2),
          ("idle", 3))
    )


_AtmfDS1E1CESCellLossStatus_Type.__name__ = "Integer32"
_AtmfDS1E1CESCellLossStatus_Object = MibTableColumn
atmfDS1E1CESCellLossStatus = _AtmfDS1E1CESCellLossStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 1, 2, 1, 7),
    _AtmfDS1E1CESCellLossStatus_Type()
)
atmfDS1E1CESCellLossStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfDS1E1CESCellLossStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ATMF-CES-MIB",
    **{"atmForum": atmForum,
       "atmForumNetworkManagement": atmForumNetworkManagement,
       "atmfCESmib": atmfCESmib,
       "atmfDS1E1CESmib": atmfDS1E1CESmib,
       "atmfDS1E1CESConfTable": atmfDS1E1CESConfTable,
       "atmfDS1E1CESConfEntry": atmfDS1E1CESConfEntry,
       "atmfDS1E1CESMapATMIndex": atmfDS1E1CESMapATMIndex,
       "atmfDS1E1CESMapVPI": atmfDS1E1CESMapVPI,
       "atmfDS1E1CESMapVCI": atmfDS1E1CESMapVCI,
       "atmfDS1E1CESCBRService": atmfDS1E1CESCBRService,
       "atmfDS1E1CESCBRClockMode": atmfDS1E1CESCBRClockMode,
       "atmfDS1E1CESCas": atmfDS1E1CESCas,
       "atmfDS1E1CESPartialFill": atmfDS1E1CESPartialFill,
       "atmfDS1E1CESBufMaxSize": atmfDS1E1CESBufMaxSize,
       "atmfDS1E1CESCDVRxT": atmfDS1E1CESCDVRxT,
       "atmfDS1E1CESCellLossIntegrationPeriod": atmfDS1E1CESCellLossIntegrationPeriod,
       "atmfDS1E1CESStatsTable": atmfDS1E1CESStatsTable,
       "atmfDS1E1CESStatsEntry": atmfDS1E1CESStatsEntry,
       "atmfDS1E1CESReassCells": atmfDS1E1CESReassCells,
       "atmfDS1E1CESHdrErrors": atmfDS1E1CESHdrErrors,
       "atmfDS1E1CESPointerReframes": atmfDS1E1CESPointerReframes,
       "atmfDS1E1CESLostCells": atmfDS1E1CESLostCells,
       "atmfDS1E1CESBufUnderflows": atmfDS1E1CESBufUnderflows,
       "atmfDS1E1CESBufOverflows": atmfDS1E1CESBufOverflows,
       "atmfDS1E1CESCellLossStatus": atmfDS1E1CESCellLossStatus}
)
