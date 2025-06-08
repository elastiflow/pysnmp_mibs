# SNMP MIB module (CEM-CN1000-SUBTENDING-001) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ciena_6352/CEM-CN1000-SUBTENDING-001.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:49:20 2025
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

(catena,) = mibBuilder.importSymbols(
    "CEM-SMI",
    "catena")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
    "iso")

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

cn1000SubtendingModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 16)
)
if mibBuilder.loadTexts:
    cn1000SubtendingModule.setRevisions(
        ("2002-02-20 13:23",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Cn1000SubtendingConnectionStatusType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("configSucceeded", 1),
          ("configPending", 2),
          ("configFailed", 3),
          ("deleteInProgress", 4),
          ("deleteFailed", 5),
          ("configInProgress", 6))
    )



class Cn1000SubtendingMediaEndPointType(TextualConvention, Integer32):
    status = "current"
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
        *(("cnTP", 1),
          ("cnWP", 2),
          ("cnDS3", 3),
          ("cnOC12", 4))
    )



class Cn1000SubtendingMediaEndpointStatusType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("configSucceeded", 1),
          ("configPending", 2),
          ("configFailed", 3),
          ("deleteInProgress", 4),
          ("deleteFailed", 5),
          ("configInProgress", 6))
    )



class Cn1000SubtendingMediaWanConnectionStatusType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("configSucceeded", 1),
          ("configPending", 2),
          ("configFailed", 3),
          ("deleteInProgress", 4),
          ("deleteFailed", 5),
          ("configInProgress", 6))
    )



# MIB Managed Objects in the order of their OIDs

_Cn1000StandaloneSubtendingT1ConnectionTable_Object = MibTable
cn1000StandaloneSubtendingT1ConnectionTable = _Cn1000StandaloneSubtendingT1ConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 16, 1)
)
if mibBuilder.loadTexts:
    cn1000StandaloneSubtendingT1ConnectionTable.setStatus("current")
_Cn1000StandaloneSubtendingT1ConnectionEntry_Object = MibTableRow
cn1000StandaloneSubtendingT1ConnectionEntry = _Cn1000StandaloneSubtendingT1ConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 16, 1, 1)
)
cn1000StandaloneSubtendingT1ConnectionEntry.setIndexNames(
    (0, "CEM-CN1000-SUBTENDING-001", "cn1000STT1CardT1ifIndex"),
    (0, "CEM-CN1000-SUBTENDING-001", "cn1000STWANCardT1ifIndex"),
)
if mibBuilder.loadTexts:
    cn1000StandaloneSubtendingT1ConnectionEntry.setStatus("current")
_Cn1000STWANCardT1ifIndex_Type = InterfaceIndex
_Cn1000STWANCardT1ifIndex_Object = MibTableColumn
cn1000STWANCardT1ifIndex = _Cn1000STWANCardT1ifIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 16, 1, 1, 1),
    _Cn1000STWANCardT1ifIndex_Type()
)
cn1000STWANCardT1ifIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cn1000STWANCardT1ifIndex.setStatus("current")
_Cn1000STT1CardT1ifIndex_Type = InterfaceIndex
_Cn1000STT1CardT1ifIndex_Object = MibTableColumn
cn1000STT1CardT1ifIndex = _Cn1000STT1CardT1ifIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 16, 1, 1, 2),
    _Cn1000STT1CardT1ifIndex_Type()
)
cn1000STT1CardT1ifIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cn1000STT1CardT1ifIndex.setStatus("current")
_Cn1000SubtendingT1ConnectionStatus_Type = Cn1000SubtendingConnectionStatusType
_Cn1000SubtendingT1ConnectionStatus_Object = MibTableColumn
cn1000SubtendingT1ConnectionStatus = _Cn1000SubtendingT1ConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 16, 1, 1, 3),
    _Cn1000SubtendingT1ConnectionStatus_Type()
)
cn1000SubtendingT1ConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000SubtendingT1ConnectionStatus.setStatus("current")
_Cn1000SubtendingT1ConnectionRowStatus_Type = RowStatus
_Cn1000SubtendingT1ConnectionRowStatus_Object = MibTableColumn
cn1000SubtendingT1ConnectionRowStatus = _Cn1000SubtendingT1ConnectionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 16, 1, 1, 4),
    _Cn1000SubtendingT1ConnectionRowStatus_Type()
)
cn1000SubtendingT1ConnectionRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cn1000SubtendingT1ConnectionRowStatus.setStatus("current")
_Cn1000SubtendingMediaEndpointTable_Object = MibTable
cn1000SubtendingMediaEndpointTable = _Cn1000SubtendingMediaEndpointTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 16, 2)
)
if mibBuilder.loadTexts:
    cn1000SubtendingMediaEndpointTable.setStatus("current")
_Cn1000SubtendingMediaEndpointEntry_Object = MibTableRow
cn1000SubtendingMediaEndpointEntry = _Cn1000SubtendingMediaEndpointEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 16, 2, 1)
)
cn1000SubtendingMediaEndpointEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CEM-CN1000-SUBTENDING-001", "cn1000SubtendingMediaEndpointVpi"),
    (0, "CEM-CN1000-SUBTENDING-001", "cn1000SubtendingMediaEndpointVci"),
)
if mibBuilder.loadTexts:
    cn1000SubtendingMediaEndpointEntry.setStatus("current")


class _Cn1000SubtendingMediaEndpointVpi_Type(Integer32):
    """Custom type cn1000SubtendingMediaEndpointVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_Cn1000SubtendingMediaEndpointVpi_Type.__name__ = "Integer32"
_Cn1000SubtendingMediaEndpointVpi_Object = MibTableColumn
cn1000SubtendingMediaEndpointVpi = _Cn1000SubtendingMediaEndpointVpi_Object(
    (1, 3, 6, 1, 4, 1, 6352, 16, 2, 1, 1),
    _Cn1000SubtendingMediaEndpointVpi_Type()
)
cn1000SubtendingMediaEndpointVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000SubtendingMediaEndpointVpi.setStatus("current")


class _Cn1000SubtendingMediaEndpointVci_Type(Integer32):
    """Custom type cn1000SubtendingMediaEndpointVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_Cn1000SubtendingMediaEndpointVci_Type.__name__ = "Integer32"
_Cn1000SubtendingMediaEndpointVci_Object = MibTableColumn
cn1000SubtendingMediaEndpointVci = _Cn1000SubtendingMediaEndpointVci_Object(
    (1, 3, 6, 1, 4, 1, 6352, 16, 2, 1, 2),
    _Cn1000SubtendingMediaEndpointVci_Type()
)
cn1000SubtendingMediaEndpointVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000SubtendingMediaEndpointVci.setStatus("current")
_Cn1000SubtendingMediaEndpointRemoteEndpointType_Type = Cn1000SubtendingMediaEndPointType
_Cn1000SubtendingMediaEndpointRemoteEndpointType_Object = MibTableColumn
cn1000SubtendingMediaEndpointRemoteEndpointType = _Cn1000SubtendingMediaEndpointRemoteEndpointType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 16, 2, 1, 3),
    _Cn1000SubtendingMediaEndpointRemoteEndpointType_Type()
)
cn1000SubtendingMediaEndpointRemoteEndpointType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000SubtendingMediaEndpointRemoteEndpointType.setStatus("current")
_Cn1000SubtendingMediaEndpointStatus_Type = Cn1000SubtendingMediaEndpointStatusType
_Cn1000SubtendingMediaEndpointStatus_Object = MibTableColumn
cn1000SubtendingMediaEndpointStatus = _Cn1000SubtendingMediaEndpointStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 16, 2, 1, 5),
    _Cn1000SubtendingMediaEndpointStatus_Type()
)
cn1000SubtendingMediaEndpointStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000SubtendingMediaEndpointStatus.setStatus("current")
_Cn1000SubtendingMediaEndpointRowStatus_Type = RowStatus
_Cn1000SubtendingMediaEndpointRowStatus_Object = MibTableColumn
cn1000SubtendingMediaEndpointRowStatus = _Cn1000SubtendingMediaEndpointRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 16, 2, 1, 6),
    _Cn1000SubtendingMediaEndpointRowStatus_Type()
)
cn1000SubtendingMediaEndpointRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000SubtendingMediaEndpointRowStatus.setStatus("current")
_Cn1000SubtendingMediaWanConnectionTable_Object = MibTable
cn1000SubtendingMediaWanConnectionTable = _Cn1000SubtendingMediaWanConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 16, 3)
)
if mibBuilder.loadTexts:
    cn1000SubtendingMediaWanConnectionTable.setStatus("current")
_Cn1000SubtendingMediaWanConnectionEntry_Object = MibTableRow
cn1000SubtendingMediaWanConnectionEntry = _Cn1000SubtendingMediaWanConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 16, 3, 1)
)
cn1000SubtendingMediaWanConnectionEntry.setIndexNames(
    (0, "CEM-CN1000-SUBTENDING-001", "cn1000SubtendingMediaConnectionWanIfIndex"),
    (0, "CEM-CN1000-SUBTENDING-001", "cn1000SubtendingMediaConnectionWanVpi"),
    (0, "CEM-CN1000-SUBTENDING-001", "cn1000SubtendingMediaConnectionWanVci"),
    (0, "CEM-CN1000-SUBTENDING-001", "cn1000SubtendingMediaWanConnectionIfIndex"),
)
if mibBuilder.loadTexts:
    cn1000SubtendingMediaWanConnectionEntry.setStatus("current")
_Cn1000SubtendingMediaConnectionWanIfIndex_Type = InterfaceIndex
_Cn1000SubtendingMediaConnectionWanIfIndex_Object = MibTableColumn
cn1000SubtendingMediaConnectionWanIfIndex = _Cn1000SubtendingMediaConnectionWanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 16, 3, 1, 1),
    _Cn1000SubtendingMediaConnectionWanIfIndex_Type()
)
cn1000SubtendingMediaConnectionWanIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000SubtendingMediaConnectionWanIfIndex.setStatus("current")


class _Cn1000SubtendingMediaConnectionWanVpi_Type(Integer32):
    """Custom type cn1000SubtendingMediaConnectionWanVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Cn1000SubtendingMediaConnectionWanVpi_Type.__name__ = "Integer32"
_Cn1000SubtendingMediaConnectionWanVpi_Object = MibTableColumn
cn1000SubtendingMediaConnectionWanVpi = _Cn1000SubtendingMediaConnectionWanVpi_Object(
    (1, 3, 6, 1, 4, 1, 6352, 16, 3, 1, 2),
    _Cn1000SubtendingMediaConnectionWanVpi_Type()
)
cn1000SubtendingMediaConnectionWanVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000SubtendingMediaConnectionWanVpi.setStatus("current")


class _Cn1000SubtendingMediaConnectionWanVci_Type(Integer32):
    """Custom type cn1000SubtendingMediaConnectionWanVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_Cn1000SubtendingMediaConnectionWanVci_Type.__name__ = "Integer32"
_Cn1000SubtendingMediaConnectionWanVci_Object = MibTableColumn
cn1000SubtendingMediaConnectionWanVci = _Cn1000SubtendingMediaConnectionWanVci_Object(
    (1, 3, 6, 1, 4, 1, 6352, 16, 3, 1, 3),
    _Cn1000SubtendingMediaConnectionWanVci_Type()
)
cn1000SubtendingMediaConnectionWanVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000SubtendingMediaConnectionWanVci.setStatus("current")
_Cn1000SubtendingMediaWanConnectionIfIndex_Type = InterfaceIndex
_Cn1000SubtendingMediaWanConnectionIfIndex_Object = MibTableColumn
cn1000SubtendingMediaWanConnectionIfIndex = _Cn1000SubtendingMediaWanConnectionIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 16, 3, 1, 4),
    _Cn1000SubtendingMediaWanConnectionIfIndex_Type()
)
cn1000SubtendingMediaWanConnectionIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000SubtendingMediaWanConnectionIfIndex.setStatus("current")


class _Cn1000SubtendingMediaWanConnectionInternalVpi_Type(Integer32):
    """Custom type cn1000SubtendingMediaWanConnectionInternalVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Cn1000SubtendingMediaWanConnectionInternalVpi_Type.__name__ = "Integer32"
_Cn1000SubtendingMediaWanConnectionInternalVpi_Object = MibTableColumn
cn1000SubtendingMediaWanConnectionInternalVpi = _Cn1000SubtendingMediaWanConnectionInternalVpi_Object(
    (1, 3, 6, 1, 4, 1, 6352, 16, 3, 1, 5),
    _Cn1000SubtendingMediaWanConnectionInternalVpi_Type()
)
cn1000SubtendingMediaWanConnectionInternalVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000SubtendingMediaWanConnectionInternalVpi.setStatus("current")


class _Cn1000SubtendingMediaWanConnectionInternalVci_Type(Integer32):
    """Custom type cn1000SubtendingMediaWanConnectionInternalVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_Cn1000SubtendingMediaWanConnectionInternalVci_Type.__name__ = "Integer32"
_Cn1000SubtendingMediaWanConnectionInternalVci_Object = MibTableColumn
cn1000SubtendingMediaWanConnectionInternalVci = _Cn1000SubtendingMediaWanConnectionInternalVci_Object(
    (1, 3, 6, 1, 4, 1, 6352, 16, 3, 1, 6),
    _Cn1000SubtendingMediaWanConnectionInternalVci_Type()
)
cn1000SubtendingMediaWanConnectionInternalVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000SubtendingMediaWanConnectionInternalVci.setStatus("current")
_Cn1000SubtendingMediaWanConnectionEndpointType_Type = Cn1000SubtendingMediaEndPointType
_Cn1000SubtendingMediaWanConnectionEndpointType_Object = MibTableColumn
cn1000SubtendingMediaWanConnectionEndpointType = _Cn1000SubtendingMediaWanConnectionEndpointType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 16, 3, 1, 7),
    _Cn1000SubtendingMediaWanConnectionEndpointType_Type()
)
cn1000SubtendingMediaWanConnectionEndpointType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000SubtendingMediaWanConnectionEndpointType.setStatus("current")
_Cn1000SubtendingMediaWanConnectionStatus_Type = Cn1000SubtendingMediaWanConnectionStatusType
_Cn1000SubtendingMediaWanConnectionStatus_Object = MibTableColumn
cn1000SubtendingMediaWanConnectionStatus = _Cn1000SubtendingMediaWanConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 16, 3, 1, 8),
    _Cn1000SubtendingMediaWanConnectionStatus_Type()
)
cn1000SubtendingMediaWanConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000SubtendingMediaWanConnectionStatus.setStatus("current")


class _Cn1000SubtendingMediaWanConnectionInternalOffset_Type(Integer32):
    """Custom type cn1000SubtendingMediaWanConnectionInternalOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_Cn1000SubtendingMediaWanConnectionInternalOffset_Type.__name__ = "Integer32"
_Cn1000SubtendingMediaWanConnectionInternalOffset_Object = MibTableColumn
cn1000SubtendingMediaWanConnectionInternalOffset = _Cn1000SubtendingMediaWanConnectionInternalOffset_Object(
    (1, 3, 6, 1, 4, 1, 6352, 16, 3, 1, 9),
    _Cn1000SubtendingMediaWanConnectionInternalOffset_Type()
)
cn1000SubtendingMediaWanConnectionInternalOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000SubtendingMediaWanConnectionInternalOffset.setStatus("current")


class _Cn1000SubtendingMediaWanConnectionCdvt_Type(Integer32):
    """Custom type cn1000SubtendingMediaWanConnectionCdvt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 32),
    )


_Cn1000SubtendingMediaWanConnectionCdvt_Type.__name__ = "Integer32"
_Cn1000SubtendingMediaWanConnectionCdvt_Object = MibTableColumn
cn1000SubtendingMediaWanConnectionCdvt = _Cn1000SubtendingMediaWanConnectionCdvt_Object(
    (1, 3, 6, 1, 4, 1, 6352, 16, 3, 1, 10),
    _Cn1000SubtendingMediaWanConnectionCdvt_Type()
)
cn1000SubtendingMediaWanConnectionCdvt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cn1000SubtendingMediaWanConnectionCdvt.setStatus("current")
_Cn1000SubtendingMediaWanConnectionRowStatus_Type = RowStatus
_Cn1000SubtendingMediaWanConnectionRowStatus_Object = MibTableColumn
cn1000SubtendingMediaWanConnectionRowStatus = _Cn1000SubtendingMediaWanConnectionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 16, 3, 1, 11),
    _Cn1000SubtendingMediaWanConnectionRowStatus_Type()
)
cn1000SubtendingMediaWanConnectionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000SubtendingMediaWanConnectionRowStatus.setStatus("current")


class _Cn1000SubtendingMediaWanConnectionDSPvcTag_Type(OctetString):
    """Custom type cn1000SubtendingMediaWanConnectionDSPvcTag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Cn1000SubtendingMediaWanConnectionDSPvcTag_Type.__name__ = "OctetString"
_Cn1000SubtendingMediaWanConnectionDSPvcTag_Object = MibTableColumn
cn1000SubtendingMediaWanConnectionDSPvcTag = _Cn1000SubtendingMediaWanConnectionDSPvcTag_Object(
    (1, 3, 6, 1, 4, 1, 6352, 16, 3, 1, 12),
    _Cn1000SubtendingMediaWanConnectionDSPvcTag_Type()
)
cn1000SubtendingMediaWanConnectionDSPvcTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000SubtendingMediaWanConnectionDSPvcTag.setStatus("current")


class _Cn1000SubtendingMediaWanConnectionUSPvcTag_Type(OctetString):
    """Custom type cn1000SubtendingMediaWanConnectionUSPvcTag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Cn1000SubtendingMediaWanConnectionUSPvcTag_Type.__name__ = "OctetString"
_Cn1000SubtendingMediaWanConnectionUSPvcTag_Object = MibTableColumn
cn1000SubtendingMediaWanConnectionUSPvcTag = _Cn1000SubtendingMediaWanConnectionUSPvcTag_Object(
    (1, 3, 6, 1, 4, 1, 6352, 16, 3, 1, 13),
    _Cn1000SubtendingMediaWanConnectionUSPvcTag_Type()
)
cn1000SubtendingMediaWanConnectionUSPvcTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000SubtendingMediaWanConnectionUSPvcTag.setStatus("current")
_Cn1000ModuleConformance_ObjectIdentity = ObjectIdentity
cn1000ModuleConformance = _Cn1000ModuleConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 16, 4)
)
_Cn1000SubtendingMediaWanConnectionCurrentStatsTable_Object = MibTable
cn1000SubtendingMediaWanConnectionCurrentStatsTable = _Cn1000SubtendingMediaWanConnectionCurrentStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 16, 5)
)
if mibBuilder.loadTexts:
    cn1000SubtendingMediaWanConnectionCurrentStatsTable.setStatus("current")
_Cn1000SubtendingMediaWanConnectionCurrentStatsEntry_Object = MibTableRow
cn1000SubtendingMediaWanConnectionCurrentStatsEntry = _Cn1000SubtendingMediaWanConnectionCurrentStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 16, 5, 1)
)
cn1000SubtendingMediaWanConnectionCurrentStatsEntry.setIndexNames(
    (0, "CEM-CN1000-SUBTENDING-001", "cn1000SubtendingMediaConnectionWanCurrentStatsIfIndex"),
    (0, "CEM-CN1000-SUBTENDING-001", "cn1000SubtendingMediaConnectionWanCurrentStatsVpi"),
    (0, "CEM-CN1000-SUBTENDING-001", "cn1000SubtendingMediaConnectionWanCurrentStatsVci"),
    (0, "CEM-CN1000-SUBTENDING-001", "cn1000SubtendingMediaWanConnectionCurrentStatsIfIndex"),
    (0, "CEM-CN1000-SUBTENDING-001", "cn1000SubtendingMediaWanConnectionCurrentStatsOffset"),
)
if mibBuilder.loadTexts:
    cn1000SubtendingMediaWanConnectionCurrentStatsEntry.setStatus("current")
_Cn1000SubtendingMediaConnectionWanCurrentStatsIfIndex_Type = InterfaceIndex
_Cn1000SubtendingMediaConnectionWanCurrentStatsIfIndex_Object = MibTableColumn
cn1000SubtendingMediaConnectionWanCurrentStatsIfIndex = _Cn1000SubtendingMediaConnectionWanCurrentStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 16, 5, 1, 1),
    _Cn1000SubtendingMediaConnectionWanCurrentStatsIfIndex_Type()
)
cn1000SubtendingMediaConnectionWanCurrentStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000SubtendingMediaConnectionWanCurrentStatsIfIndex.setStatus("current")


class _Cn1000SubtendingMediaConnectionWanCurrentStatsVpi_Type(Integer32):
    """Custom type cn1000SubtendingMediaConnectionWanCurrentStatsVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cn1000SubtendingMediaConnectionWanCurrentStatsVpi_Type.__name__ = "Integer32"
_Cn1000SubtendingMediaConnectionWanCurrentStatsVpi_Object = MibTableColumn
cn1000SubtendingMediaConnectionWanCurrentStatsVpi = _Cn1000SubtendingMediaConnectionWanCurrentStatsVpi_Object(
    (1, 3, 6, 1, 4, 1, 6352, 16, 5, 1, 2),
    _Cn1000SubtendingMediaConnectionWanCurrentStatsVpi_Type()
)
cn1000SubtendingMediaConnectionWanCurrentStatsVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000SubtendingMediaConnectionWanCurrentStatsVpi.setStatus("current")


class _Cn1000SubtendingMediaConnectionWanCurrentStatsVci_Type(Integer32):
    """Custom type cn1000SubtendingMediaConnectionWanCurrentStatsVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cn1000SubtendingMediaConnectionWanCurrentStatsVci_Type.__name__ = "Integer32"
_Cn1000SubtendingMediaConnectionWanCurrentStatsVci_Object = MibTableColumn
cn1000SubtendingMediaConnectionWanCurrentStatsVci = _Cn1000SubtendingMediaConnectionWanCurrentStatsVci_Object(
    (1, 3, 6, 1, 4, 1, 6352, 16, 5, 1, 3),
    _Cn1000SubtendingMediaConnectionWanCurrentStatsVci_Type()
)
cn1000SubtendingMediaConnectionWanCurrentStatsVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000SubtendingMediaConnectionWanCurrentStatsVci.setStatus("current")
_Cn1000SubtendingMediaWanConnectionCurrentStatsIfIndex_Type = InterfaceIndex
_Cn1000SubtendingMediaWanConnectionCurrentStatsIfIndex_Object = MibTableColumn
cn1000SubtendingMediaWanConnectionCurrentStatsIfIndex = _Cn1000SubtendingMediaWanConnectionCurrentStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 16, 5, 1, 4),
    _Cn1000SubtendingMediaWanConnectionCurrentStatsIfIndex_Type()
)
cn1000SubtendingMediaWanConnectionCurrentStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000SubtendingMediaWanConnectionCurrentStatsIfIndex.setStatus("current")


class _Cn1000SubtendingMediaWanConnectionCurrentStatsOffset_Type(Integer32):
    """Custom type cn1000SubtendingMediaWanConnectionCurrentStatsOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cn1000SubtendingMediaWanConnectionCurrentStatsOffset_Type.__name__ = "Integer32"
_Cn1000SubtendingMediaWanConnectionCurrentStatsOffset_Object = MibTableColumn
cn1000SubtendingMediaWanConnectionCurrentStatsOffset = _Cn1000SubtendingMediaWanConnectionCurrentStatsOffset_Object(
    (1, 3, 6, 1, 4, 1, 6352, 16, 5, 1, 5),
    _Cn1000SubtendingMediaWanConnectionCurrentStatsOffset_Type()
)
cn1000SubtendingMediaWanConnectionCurrentStatsOffset.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000SubtendingMediaWanConnectionCurrentStatsOffset.setStatus("current")


class _Cn1000SubtendingMediaWanConnectionCurrentStatsUnderFlows_Type(Integer32):
    """Custom type cn1000SubtendingMediaWanConnectionCurrentStatsUnderFlows based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cn1000SubtendingMediaWanConnectionCurrentStatsUnderFlows_Type.__name__ = "Integer32"
_Cn1000SubtendingMediaWanConnectionCurrentStatsUnderFlows_Object = MibTableColumn
cn1000SubtendingMediaWanConnectionCurrentStatsUnderFlows = _Cn1000SubtendingMediaWanConnectionCurrentStatsUnderFlows_Object(
    (1, 3, 6, 1, 4, 1, 6352, 16, 5, 1, 6),
    _Cn1000SubtendingMediaWanConnectionCurrentStatsUnderFlows_Type()
)
cn1000SubtendingMediaWanConnectionCurrentStatsUnderFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000SubtendingMediaWanConnectionCurrentStatsUnderFlows.setStatus("current")


class _Cn1000SubtendingMediaWanConnectionCurrentStatsOverFlows_Type(Integer32):
    """Custom type cn1000SubtendingMediaWanConnectionCurrentStatsOverFlows based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cn1000SubtendingMediaWanConnectionCurrentStatsOverFlows_Type.__name__ = "Integer32"
_Cn1000SubtendingMediaWanConnectionCurrentStatsOverFlows_Object = MibTableColumn
cn1000SubtendingMediaWanConnectionCurrentStatsOverFlows = _Cn1000SubtendingMediaWanConnectionCurrentStatsOverFlows_Object(
    (1, 3, 6, 1, 4, 1, 6352, 16, 5, 1, 7),
    _Cn1000SubtendingMediaWanConnectionCurrentStatsOverFlows_Type()
)
cn1000SubtendingMediaWanConnectionCurrentStatsOverFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000SubtendingMediaWanConnectionCurrentStatsOverFlows.setStatus("current")


class _Cn1000SubtendingMediaWanConnectionCurrentStatsCellDrop_Type(Integer32):
    """Custom type cn1000SubtendingMediaWanConnectionCurrentStatsCellDrop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cn1000SubtendingMediaWanConnectionCurrentStatsCellDrop_Type.__name__ = "Integer32"
_Cn1000SubtendingMediaWanConnectionCurrentStatsCellDrop_Object = MibTableColumn
cn1000SubtendingMediaWanConnectionCurrentStatsCellDrop = _Cn1000SubtendingMediaWanConnectionCurrentStatsCellDrop_Object(
    (1, 3, 6, 1, 4, 1, 6352, 16, 5, 1, 8),
    _Cn1000SubtendingMediaWanConnectionCurrentStatsCellDrop_Type()
)
cn1000SubtendingMediaWanConnectionCurrentStatsCellDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000SubtendingMediaWanConnectionCurrentStatsCellDrop.setStatus("current")


class _Cn1000SubtendingMediaWanConnectionCurrentStatsMisInsertedCell_Type(Integer32):
    """Custom type cn1000SubtendingMediaWanConnectionCurrentStatsMisInsertedCell based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cn1000SubtendingMediaWanConnectionCurrentStatsMisInsertedCell_Type.__name__ = "Integer32"
_Cn1000SubtendingMediaWanConnectionCurrentStatsMisInsertedCell_Object = MibTableColumn
cn1000SubtendingMediaWanConnectionCurrentStatsMisInsertedCell = _Cn1000SubtendingMediaWanConnectionCurrentStatsMisInsertedCell_Object(
    (1, 3, 6, 1, 4, 1, 6352, 16, 5, 1, 9),
    _Cn1000SubtendingMediaWanConnectionCurrentStatsMisInsertedCell_Type()
)
cn1000SubtendingMediaWanConnectionCurrentStatsMisInsertedCell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000SubtendingMediaWanConnectionCurrentStatsMisInsertedCell.setStatus("current")


class _Cn1000SubtendingMediaWanConnectionCurrentStatsSequenceErrors_Type(Integer32):
    """Custom type cn1000SubtendingMediaWanConnectionCurrentStatsSequenceErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cn1000SubtendingMediaWanConnectionCurrentStatsSequenceErrors_Type.__name__ = "Integer32"
_Cn1000SubtendingMediaWanConnectionCurrentStatsSequenceErrors_Object = MibTableColumn
cn1000SubtendingMediaWanConnectionCurrentStatsSequenceErrors = _Cn1000SubtendingMediaWanConnectionCurrentStatsSequenceErrors_Object(
    (1, 3, 6, 1, 4, 1, 6352, 16, 5, 1, 10),
    _Cn1000SubtendingMediaWanConnectionCurrentStatsSequenceErrors_Type()
)
cn1000SubtendingMediaWanConnectionCurrentStatsSequenceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000SubtendingMediaWanConnectionCurrentStatsSequenceErrors.setStatus("current")


class _Cn1000SubtendingMediaWanConnectionCurrentStatsPointerReframes_Type(Integer32):
    """Custom type cn1000SubtendingMediaWanConnectionCurrentStatsPointerReframes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cn1000SubtendingMediaWanConnectionCurrentStatsPointerReframes_Type.__name__ = "Integer32"
_Cn1000SubtendingMediaWanConnectionCurrentStatsPointerReframes_Object = MibTableColumn
cn1000SubtendingMediaWanConnectionCurrentStatsPointerReframes = _Cn1000SubtendingMediaWanConnectionCurrentStatsPointerReframes_Object(
    (1, 3, 6, 1, 4, 1, 6352, 16, 5, 1, 11),
    _Cn1000SubtendingMediaWanConnectionCurrentStatsPointerReframes_Type()
)
cn1000SubtendingMediaWanConnectionCurrentStatsPointerReframes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000SubtendingMediaWanConnectionCurrentStatsPointerReframes.setStatus("current")


class _Cn1000SubtendingMediaWanConnectionCurrentStatsHeaderErrors_Type(Integer32):
    """Custom type cn1000SubtendingMediaWanConnectionCurrentStatsHeaderErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cn1000SubtendingMediaWanConnectionCurrentStatsHeaderErrors_Type.__name__ = "Integer32"
_Cn1000SubtendingMediaWanConnectionCurrentStatsHeaderErrors_Object = MibTableColumn
cn1000SubtendingMediaWanConnectionCurrentStatsHeaderErrors = _Cn1000SubtendingMediaWanConnectionCurrentStatsHeaderErrors_Object(
    (1, 3, 6, 1, 4, 1, 6352, 16, 5, 1, 12),
    _Cn1000SubtendingMediaWanConnectionCurrentStatsHeaderErrors_Type()
)
cn1000SubtendingMediaWanConnectionCurrentStatsHeaderErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000SubtendingMediaWanConnectionCurrentStatsHeaderErrors.setStatus("current")


class _Cn1000SubtendingMediaWanConnectionCurrentStatsPtrPtyErrors_Type(Integer32):
    """Custom type cn1000SubtendingMediaWanConnectionCurrentStatsPtrPtyErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cn1000SubtendingMediaWanConnectionCurrentStatsPtrPtyErrors_Type.__name__ = "Integer32"
_Cn1000SubtendingMediaWanConnectionCurrentStatsPtrPtyErrors_Object = MibTableColumn
cn1000SubtendingMediaWanConnectionCurrentStatsPtrPtyErrors = _Cn1000SubtendingMediaWanConnectionCurrentStatsPtrPtyErrors_Object(
    (1, 3, 6, 1, 4, 1, 6352, 16, 5, 1, 13),
    _Cn1000SubtendingMediaWanConnectionCurrentStatsPtrPtyErrors_Type()
)
cn1000SubtendingMediaWanConnectionCurrentStatsPtrPtyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000SubtendingMediaWanConnectionCurrentStatsPtrPtyErrors.setStatus("current")


class _Cn1000SubtendingMediaWanConnectionCurrentStatsRxCells_Type(Integer32):
    """Custom type cn1000SubtendingMediaWanConnectionCurrentStatsRxCells based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cn1000SubtendingMediaWanConnectionCurrentStatsRxCells_Type.__name__ = "Integer32"
_Cn1000SubtendingMediaWanConnectionCurrentStatsRxCells_Object = MibTableColumn
cn1000SubtendingMediaWanConnectionCurrentStatsRxCells = _Cn1000SubtendingMediaWanConnectionCurrentStatsRxCells_Object(
    (1, 3, 6, 1, 4, 1, 6352, 16, 5, 1, 14),
    _Cn1000SubtendingMediaWanConnectionCurrentStatsRxCells_Type()
)
cn1000SubtendingMediaWanConnectionCurrentStatsRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000SubtendingMediaWanConnectionCurrentStatsRxCells.setStatus("current")


class _Cn1000SubtendingMediaWanConnectionCurrentStatsTxCells_Type(Integer32):
    """Custom type cn1000SubtendingMediaWanConnectionCurrentStatsTxCells based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cn1000SubtendingMediaWanConnectionCurrentStatsTxCells_Type.__name__ = "Integer32"
_Cn1000SubtendingMediaWanConnectionCurrentStatsTxCells_Object = MibTableColumn
cn1000SubtendingMediaWanConnectionCurrentStatsTxCells = _Cn1000SubtendingMediaWanConnectionCurrentStatsTxCells_Object(
    (1, 3, 6, 1, 4, 1, 6352, 16, 5, 1, 15),
    _Cn1000SubtendingMediaWanConnectionCurrentStatsTxCells_Type()
)
cn1000SubtendingMediaWanConnectionCurrentStatsTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000SubtendingMediaWanConnectionCurrentStatsTxCells.setStatus("current")

# Managed Objects groups

cn100010ObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6352, 16, 4, 1)
)
cn100010ObjectsGroup.setObjects(
      *(("CEM-CN1000-SUBTENDING-001", "cn1000SubtendingT1ConnectionRowStatus"),
        ("CEM-CN1000-SUBTENDING-001", "cn1000SubtendingT1ConnectionStatus"),
        ("CEM-CN1000-SUBTENDING-001", "cn1000STWANCardT1ifIndex"),
        ("CEM-CN1000-SUBTENDING-001", "cn1000STT1CardT1ifIndex"),
        ("CEM-CN1000-SUBTENDING-001", "cn1000SubtendingMediaEndpointVpi"),
        ("CEM-CN1000-SUBTENDING-001", "cn1000SubtendingMediaEndpointVci"),
        ("CEM-CN1000-SUBTENDING-001", "cn1000SubtendingMediaEndpointRemoteEndpointType"),
        ("CEM-CN1000-SUBTENDING-001", "cn1000SubtendingMediaEndpointRowStatus"),
        ("CEM-CN1000-SUBTENDING-001", "cn1000SubtendingMediaWanConnectionIfIndex"),
        ("CEM-CN1000-SUBTENDING-001", "cn1000SubtendingMediaEndpointStatus"),
        ("CEM-CN1000-SUBTENDING-001", "cn1000SubtendingMediaWanConnectionStatus"),
        ("CEM-CN1000-SUBTENDING-001", "cn1000SubtendingMediaWanConnectionInternalVpi"),
        ("CEM-CN1000-SUBTENDING-001", "cn1000SubtendingMediaWanConnectionEndpointType"),
        ("CEM-CN1000-SUBTENDING-001", "cn1000SubtendingMediaWanConnectionInternalOffset"),
        ("CEM-CN1000-SUBTENDING-001", "cn1000SubtendingMediaConnectionWanVci"),
        ("CEM-CN1000-SUBTENDING-001", "cn1000SubtendingMediaConnectionWanVpi"),
        ("CEM-CN1000-SUBTENDING-001", "cn1000SubtendingMediaConnectionWanIfIndex"),
        ("CEM-CN1000-SUBTENDING-001", "cn1000SubtendingMediaWanConnectionRowStatus"),
        ("CEM-CN1000-SUBTENDING-001", "cn1000SubtendingMediaWanConnectionInternalVci"))
)
if mibBuilder.loadTexts:
    cn100010ObjectsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CEM-CN1000-SUBTENDING-001",
    **{"Cn1000SubtendingConnectionStatusType": Cn1000SubtendingConnectionStatusType,
       "Cn1000SubtendingMediaEndPointType": Cn1000SubtendingMediaEndPointType,
       "Cn1000SubtendingMediaEndpointStatusType": Cn1000SubtendingMediaEndpointStatusType,
       "Cn1000SubtendingMediaWanConnectionStatusType": Cn1000SubtendingMediaWanConnectionStatusType,
       "cn1000SubtendingModule": cn1000SubtendingModule,
       "cn1000StandaloneSubtendingT1ConnectionTable": cn1000StandaloneSubtendingT1ConnectionTable,
       "cn1000StandaloneSubtendingT1ConnectionEntry": cn1000StandaloneSubtendingT1ConnectionEntry,
       "cn1000STWANCardT1ifIndex": cn1000STWANCardT1ifIndex,
       "cn1000STT1CardT1ifIndex": cn1000STT1CardT1ifIndex,
       "cn1000SubtendingT1ConnectionStatus": cn1000SubtendingT1ConnectionStatus,
       "cn1000SubtendingT1ConnectionRowStatus": cn1000SubtendingT1ConnectionRowStatus,
       "cn1000SubtendingMediaEndpointTable": cn1000SubtendingMediaEndpointTable,
       "cn1000SubtendingMediaEndpointEntry": cn1000SubtendingMediaEndpointEntry,
       "cn1000SubtendingMediaEndpointVpi": cn1000SubtendingMediaEndpointVpi,
       "cn1000SubtendingMediaEndpointVci": cn1000SubtendingMediaEndpointVci,
       "cn1000SubtendingMediaEndpointRemoteEndpointType": cn1000SubtendingMediaEndpointRemoteEndpointType,
       "cn1000SubtendingMediaEndpointStatus": cn1000SubtendingMediaEndpointStatus,
       "cn1000SubtendingMediaEndpointRowStatus": cn1000SubtendingMediaEndpointRowStatus,
       "cn1000SubtendingMediaWanConnectionTable": cn1000SubtendingMediaWanConnectionTable,
       "cn1000SubtendingMediaWanConnectionEntry": cn1000SubtendingMediaWanConnectionEntry,
       "cn1000SubtendingMediaConnectionWanIfIndex": cn1000SubtendingMediaConnectionWanIfIndex,
       "cn1000SubtendingMediaConnectionWanVpi": cn1000SubtendingMediaConnectionWanVpi,
       "cn1000SubtendingMediaConnectionWanVci": cn1000SubtendingMediaConnectionWanVci,
       "cn1000SubtendingMediaWanConnectionIfIndex": cn1000SubtendingMediaWanConnectionIfIndex,
       "cn1000SubtendingMediaWanConnectionInternalVpi": cn1000SubtendingMediaWanConnectionInternalVpi,
       "cn1000SubtendingMediaWanConnectionInternalVci": cn1000SubtendingMediaWanConnectionInternalVci,
       "cn1000SubtendingMediaWanConnectionEndpointType": cn1000SubtendingMediaWanConnectionEndpointType,
       "cn1000SubtendingMediaWanConnectionStatus": cn1000SubtendingMediaWanConnectionStatus,
       "cn1000SubtendingMediaWanConnectionInternalOffset": cn1000SubtendingMediaWanConnectionInternalOffset,
       "cn1000SubtendingMediaWanConnectionCdvt": cn1000SubtendingMediaWanConnectionCdvt,
       "cn1000SubtendingMediaWanConnectionRowStatus": cn1000SubtendingMediaWanConnectionRowStatus,
       "cn1000SubtendingMediaWanConnectionDSPvcTag": cn1000SubtendingMediaWanConnectionDSPvcTag,
       "cn1000SubtendingMediaWanConnectionUSPvcTag": cn1000SubtendingMediaWanConnectionUSPvcTag,
       "cn1000ModuleConformance": cn1000ModuleConformance,
       "cn100010ObjectsGroup": cn100010ObjectsGroup,
       "cn1000SubtendingMediaWanConnectionCurrentStatsTable": cn1000SubtendingMediaWanConnectionCurrentStatsTable,
       "cn1000SubtendingMediaWanConnectionCurrentStatsEntry": cn1000SubtendingMediaWanConnectionCurrentStatsEntry,
       "cn1000SubtendingMediaConnectionWanCurrentStatsIfIndex": cn1000SubtendingMediaConnectionWanCurrentStatsIfIndex,
       "cn1000SubtendingMediaConnectionWanCurrentStatsVpi": cn1000SubtendingMediaConnectionWanCurrentStatsVpi,
       "cn1000SubtendingMediaConnectionWanCurrentStatsVci": cn1000SubtendingMediaConnectionWanCurrentStatsVci,
       "cn1000SubtendingMediaWanConnectionCurrentStatsIfIndex": cn1000SubtendingMediaWanConnectionCurrentStatsIfIndex,
       "cn1000SubtendingMediaWanConnectionCurrentStatsOffset": cn1000SubtendingMediaWanConnectionCurrentStatsOffset,
       "cn1000SubtendingMediaWanConnectionCurrentStatsUnderFlows": cn1000SubtendingMediaWanConnectionCurrentStatsUnderFlows,
       "cn1000SubtendingMediaWanConnectionCurrentStatsOverFlows": cn1000SubtendingMediaWanConnectionCurrentStatsOverFlows,
       "cn1000SubtendingMediaWanConnectionCurrentStatsCellDrop": cn1000SubtendingMediaWanConnectionCurrentStatsCellDrop,
       "cn1000SubtendingMediaWanConnectionCurrentStatsMisInsertedCell": cn1000SubtendingMediaWanConnectionCurrentStatsMisInsertedCell,
       "cn1000SubtendingMediaWanConnectionCurrentStatsSequenceErrors": cn1000SubtendingMediaWanConnectionCurrentStatsSequenceErrors,
       "cn1000SubtendingMediaWanConnectionCurrentStatsPointerReframes": cn1000SubtendingMediaWanConnectionCurrentStatsPointerReframes,
       "cn1000SubtendingMediaWanConnectionCurrentStatsHeaderErrors": cn1000SubtendingMediaWanConnectionCurrentStatsHeaderErrors,
       "cn1000SubtendingMediaWanConnectionCurrentStatsPtrPtyErrors": cn1000SubtendingMediaWanConnectionCurrentStatsPtrPtyErrors,
       "cn1000SubtendingMediaWanConnectionCurrentStatsRxCells": cn1000SubtendingMediaWanConnectionCurrentStatsRxCells,
       "cn1000SubtendingMediaWanConnectionCurrentStatsTxCells": cn1000SubtendingMediaWanConnectionCurrentStatsTxCells}
)
