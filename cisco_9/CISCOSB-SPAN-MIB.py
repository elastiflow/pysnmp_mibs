# SNMP MIB module (CISCOSB-SPAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCOSB-SPAN-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:12:47 2025
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

(rndNotifications,
 switch001) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "rndNotifications",
    "switch001")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlSpan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219)
)
if mibBuilder.loadTexts:
    rlSpan.setRevisions(
        ("2015-03-25 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class SpanDestinationPortType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("monitor-only", 1),
          ("network", 2))
    )



class SpanSourceType(TextualConvention, Integer32):
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
        *(("port", 1),
          ("vlan", 2),
          ("flow", 3),
          ("remote-vlan", 4))
    )



class SpanSourceDirection(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rx", 1),
          ("tx", 2),
          ("both", 3))
    )



# MIB Managed Objects in the order of their OIDs

_RlSpanMibVersion_Type = Integer32
_RlSpanMibVersion_Object = MibScalar
rlSpanMibVersion = _RlSpanMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219, 1),
    _RlSpanMibVersion_Type()
)
rlSpanMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSpanMibVersion.setStatus("current")
_RlSpanDestinationTable_Object = MibTable
rlSpanDestinationTable = _RlSpanDestinationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219, 2)
)
if mibBuilder.loadTexts:
    rlSpanDestinationTable.setStatus("current")
_RlSpanDestinationEntry_Object = MibTableRow
rlSpanDestinationEntry = _RlSpanDestinationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219, 2, 1)
)
rlSpanDestinationEntry.setIndexNames(
    (0, "CISCOSB-SPAN-MIB", "rlSpanDestinationSessionId"),
)
if mibBuilder.loadTexts:
    rlSpanDestinationEntry.setStatus("current")
_RlSpanDestinationSessionId_Type = Integer32
_RlSpanDestinationSessionId_Object = MibTableColumn
rlSpanDestinationSessionId = _RlSpanDestinationSessionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219, 2, 1, 1),
    _RlSpanDestinationSessionId_Type()
)
rlSpanDestinationSessionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlSpanDestinationSessionId.setStatus("current")
_RlSpanDestinationIfIndex_Type = InterfaceIndex
_RlSpanDestinationIfIndex_Object = MibTableColumn
rlSpanDestinationIfIndex = _RlSpanDestinationIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219, 2, 1, 2),
    _RlSpanDestinationIfIndex_Type()
)
rlSpanDestinationIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSpanDestinationIfIndex.setStatus("current")
_RlSpanDestinationIsReflector_Type = TruthValue
_RlSpanDestinationIsReflector_Object = MibTableColumn
rlSpanDestinationIsReflector = _RlSpanDestinationIsReflector_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219, 2, 1, 3),
    _RlSpanDestinationIsReflector_Type()
)
rlSpanDestinationIsReflector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSpanDestinationIsReflector.setStatus("current")
_RlSpanDestinationPortType_Type = SpanDestinationPortType
_RlSpanDestinationPortType_Object = MibTableColumn
rlSpanDestinationPortType = _RlSpanDestinationPortType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219, 2, 1, 4),
    _RlSpanDestinationPortType_Type()
)
rlSpanDestinationPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSpanDestinationPortType.setStatus("current")
_RlSpanDestinationRowStatus_Type = RowStatus
_RlSpanDestinationRowStatus_Object = MibTableColumn
rlSpanDestinationRowStatus = _RlSpanDestinationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219, 2, 1, 5),
    _RlSpanDestinationRowStatus_Type()
)
rlSpanDestinationRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSpanDestinationRowStatus.setStatus("current")
_RlSpanSourceTable_Object = MibTable
rlSpanSourceTable = _RlSpanSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219, 3)
)
if mibBuilder.loadTexts:
    rlSpanSourceTable.setStatus("current")
_RlSpanSourceEntry_Object = MibTableRow
rlSpanSourceEntry = _RlSpanSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219, 3, 1)
)
rlSpanSourceEntry.setIndexNames(
    (0, "CISCOSB-SPAN-MIB", "rlSpanSourceSessionId"),
    (0, "CISCOSB-SPAN-MIB", "rlSpanSourceType"),
    (0, "CISCOSB-SPAN-MIB", "rlSpanSourceIndex"),
)
if mibBuilder.loadTexts:
    rlSpanSourceEntry.setStatus("current")
_RlSpanSourceSessionId_Type = Integer32
_RlSpanSourceSessionId_Object = MibTableColumn
rlSpanSourceSessionId = _RlSpanSourceSessionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219, 3, 1, 1),
    _RlSpanSourceSessionId_Type()
)
rlSpanSourceSessionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlSpanSourceSessionId.setStatus("current")
_RlSpanSourceType_Type = SpanSourceType
_RlSpanSourceType_Object = MibTableColumn
rlSpanSourceType = _RlSpanSourceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219, 3, 1, 2),
    _RlSpanSourceType_Type()
)
rlSpanSourceType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlSpanSourceType.setStatus("current")
_RlSpanSourceIndex_Type = Integer32
_RlSpanSourceIndex_Object = MibTableColumn
rlSpanSourceIndex = _RlSpanSourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219, 3, 1, 3),
    _RlSpanSourceIndex_Type()
)
rlSpanSourceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlSpanSourceIndex.setStatus("current")
_RlSpanSourceDirection_Type = SpanSourceDirection
_RlSpanSourceDirection_Object = MibTableColumn
rlSpanSourceDirection = _RlSpanSourceDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219, 3, 1, 4),
    _RlSpanSourceDirection_Type()
)
rlSpanSourceDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSpanSourceDirection.setStatus("current")
_RlSpanSourceRowStatus_Type = RowStatus
_RlSpanSourceRowStatus_Object = MibTableColumn
rlSpanSourceRowStatus = _RlSpanSourceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219, 3, 1, 5),
    _RlSpanSourceRowStatus_Type()
)
rlSpanSourceRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSpanSourceRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-SPAN-MIB",
    **{"SpanDestinationPortType": SpanDestinationPortType,
       "SpanSourceType": SpanSourceType,
       "SpanSourceDirection": SpanSourceDirection,
       "rlSpan": rlSpan,
       "rlSpanMibVersion": rlSpanMibVersion,
       "rlSpanDestinationTable": rlSpanDestinationTable,
       "rlSpanDestinationEntry": rlSpanDestinationEntry,
       "rlSpanDestinationSessionId": rlSpanDestinationSessionId,
       "rlSpanDestinationIfIndex": rlSpanDestinationIfIndex,
       "rlSpanDestinationIsReflector": rlSpanDestinationIsReflector,
       "rlSpanDestinationPortType": rlSpanDestinationPortType,
       "rlSpanDestinationRowStatus": rlSpanDestinationRowStatus,
       "rlSpanSourceTable": rlSpanSourceTable,
       "rlSpanSourceEntry": rlSpanSourceEntry,
       "rlSpanSourceSessionId": rlSpanSourceSessionId,
       "rlSpanSourceType": rlSpanSourceType,
       "rlSpanSourceIndex": rlSpanSourceIndex,
       "rlSpanSourceDirection": rlSpanSourceDirection,
       "rlSpanSourceRowStatus": rlSpanSourceRowStatus}
)
