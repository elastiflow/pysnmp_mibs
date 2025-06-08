# SNMP MIB module (RUIJIE-DVMRPINTEROPERABILITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-DVMRP-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:04:21 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

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

ruijieDvmrpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 29)
)
if mibBuilder.loadTexts:
    ruijieDvmrpMIB.setRevisions(
        ("2003-01-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieDvmrpMIBObjects_ObjectIdentity = ObjectIdentity
ruijieDvmrpMIBObjects = _RuijieDvmrpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 29, 1)
)
_RuijieDvmrpGroup_ObjectIdentity = ObjectIdentity
ruijieDvmrpGroup = _RuijieDvmrpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 29, 1, 1)
)


class _RuijieDvmrpRouteLimit_Type(Unsigned32):
    """Custom type ruijieDvmrpRouteLimit based on Unsigned32"""
    defaultValue = 7000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RuijieDvmrpRouteLimit_Type.__name__ = "Unsigned32"
_RuijieDvmrpRouteLimit_Object = MibScalar
ruijieDvmrpRouteLimit = _RuijieDvmrpRouteLimit_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 29, 1, 1, 1),
    _RuijieDvmrpRouteLimit_Type()
)
ruijieDvmrpRouteLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDvmrpRouteLimit.setStatus("current")


class _RuijieDvmrpRoutehogNotification_Type(Unsigned32):
    """Custom type ruijieDvmrpRoutehogNotification based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RuijieDvmrpRoutehogNotification_Type.__name__ = "Unsigned32"
_RuijieDvmrpRoutehogNotification_Object = MibScalar
ruijieDvmrpRoutehogNotification = _RuijieDvmrpRoutehogNotification_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 29, 1, 1, 2),
    _RuijieDvmrpRoutehogNotification_Type()
)
ruijieDvmrpRoutehogNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDvmrpRoutehogNotification.setStatus("current")
_RuijieDvmrpInterfaceTable_Object = MibTable
ruijieDvmrpInterfaceTable = _RuijieDvmrpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 29, 1, 2)
)
if mibBuilder.loadTexts:
    ruijieDvmrpInterfaceTable.setStatus("current")
_RuijieDvmrpInterfaceEntry_Object = MibTableRow
ruijieDvmrpInterfaceEntry = _RuijieDvmrpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 29, 1, 2, 1)
)
ruijieDvmrpInterfaceEntry.setIndexNames(
    (0, "RUIJIE-DVMRPINTEROPERABILITY-MIB", "ruijieDvmrpInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    ruijieDvmrpInterfaceEntry.setStatus("current")
_RuijieDvmrpInterfaceIfIndex_Type = InterfaceIndex
_RuijieDvmrpInterfaceIfIndex_Object = MibTableColumn
ruijieDvmrpInterfaceIfIndex = _RuijieDvmrpInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 29, 1, 2, 1, 1),
    _RuijieDvmrpInterfaceIfIndex_Type()
)
ruijieDvmrpInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieDvmrpInterfaceIfIndex.setStatus("current")


class _RuijieDvmrpInterfaceDefaultInformation_Type(Integer32):
    """Custom type ruijieDvmrpInterfaceDefaultInformation based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("originate", 1),
          ("only", 2))
    )


_RuijieDvmrpInterfaceDefaultInformation_Type.__name__ = "Integer32"
_RuijieDvmrpInterfaceDefaultInformation_Object = MibTableColumn
ruijieDvmrpInterfaceDefaultInformation = _RuijieDvmrpInterfaceDefaultInformation_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 29, 1, 2, 1, 2),
    _RuijieDvmrpInterfaceDefaultInformation_Type()
)
ruijieDvmrpInterfaceDefaultInformation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDvmrpInterfaceDefaultInformation.setStatus("current")


class _RuijieDvmrpInterfaceUnicastRoutingStatus_Type(EnabledStatus):
    """Custom type ruijieDvmrpInterfaceUnicastRoutingStatus based on EnabledStatus"""
    defaultValue = 2


_RuijieDvmrpInterfaceUnicastRoutingStatus_Type.__name__ = "EnabledStatus"
_RuijieDvmrpInterfaceUnicastRoutingStatus_Object = MibTableColumn
ruijieDvmrpInterfaceUnicastRoutingStatus = _RuijieDvmrpInterfaceUnicastRoutingStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 29, 1, 2, 1, 3),
    _RuijieDvmrpInterfaceUnicastRoutingStatus_Type()
)
ruijieDvmrpInterfaceUnicastRoutingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDvmrpInterfaceUnicastRoutingStatus.setStatus("current")


class _RuijieDvmrpInterfaceRejectNonPrunersStatus_Type(EnabledStatus):
    """Custom type ruijieDvmrpInterfaceRejectNonPrunersStatus based on EnabledStatus"""
    defaultValue = 2


_RuijieDvmrpInterfaceRejectNonPrunersStatus_Type.__name__ = "EnabledStatus"
_RuijieDvmrpInterfaceRejectNonPrunersStatus_Object = MibTableColumn
ruijieDvmrpInterfaceRejectNonPrunersStatus = _RuijieDvmrpInterfaceRejectNonPrunersStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 29, 1, 2, 1, 4),
    _RuijieDvmrpInterfaceRejectNonPrunersStatus_Type()
)
ruijieDvmrpInterfaceRejectNonPrunersStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDvmrpInterfaceRejectNonPrunersStatus.setStatus("current")


class _RuijieDvmrpInterfaceAutoSummaryStatus_Type(EnabledStatus):
    """Custom type ruijieDvmrpInterfaceAutoSummaryStatus based on EnabledStatus"""
    defaultValue = 1


_RuijieDvmrpInterfaceAutoSummaryStatus_Type.__name__ = "EnabledStatus"
_RuijieDvmrpInterfaceAutoSummaryStatus_Object = MibTableColumn
ruijieDvmrpInterfaceAutoSummaryStatus = _RuijieDvmrpInterfaceAutoSummaryStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 29, 1, 2, 1, 5),
    _RuijieDvmrpInterfaceAutoSummaryStatus_Type()
)
ruijieDvmrpInterfaceAutoSummaryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDvmrpInterfaceAutoSummaryStatus.setStatus("current")
_RuijieDvmrpInterfaceRtsRec_Type = Integer32
_RuijieDvmrpInterfaceRtsRec_Object = MibTableColumn
ruijieDvmrpInterfaceRtsRec = _RuijieDvmrpInterfaceRtsRec_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 29, 1, 2, 1, 6),
    _RuijieDvmrpInterfaceRtsRec_Type()
)
ruijieDvmrpInterfaceRtsRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDvmrpInterfaceRtsRec.setStatus("current")
_RuijieDvmrpInterfacePoisonReverseRtsRec_Type = Integer32
_RuijieDvmrpInterfacePoisonReverseRtsRec_Object = MibTableColumn
ruijieDvmrpInterfacePoisonReverseRtsRec = _RuijieDvmrpInterfacePoisonReverseRtsRec_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 29, 1, 2, 1, 7),
    _RuijieDvmrpInterfacePoisonReverseRtsRec_Type()
)
ruijieDvmrpInterfacePoisonReverseRtsRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDvmrpInterfacePoisonReverseRtsRec.setStatus("current")
_RuijieDvmrpInterfaceUniRtAdvertised_Type = Integer32
_RuijieDvmrpInterfaceUniRtAdvertised_Object = MibTableColumn
ruijieDvmrpInterfaceUniRtAdvertised = _RuijieDvmrpInterfaceUniRtAdvertised_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 29, 1, 2, 1, 8),
    _RuijieDvmrpInterfaceUniRtAdvertised_Type()
)
ruijieDvmrpInterfaceUniRtAdvertised.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDvmrpInterfaceUniRtAdvertised.setStatus("current")
_RuijieDvmrpInterfaceDvmrpRtAdvertised_Type = Integer32
_RuijieDvmrpInterfaceDvmrpRtAdvertised_Object = MibTableColumn
ruijieDvmrpInterfaceDvmrpRtAdvertised = _RuijieDvmrpInterfaceDvmrpRtAdvertised_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 29, 1, 2, 1, 9),
    _RuijieDvmrpInterfaceDvmrpRtAdvertised_Type()
)
ruijieDvmrpInterfaceDvmrpRtAdvertised.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDvmrpInterfaceDvmrpRtAdvertised.setStatus("current")
_RuijieDvmrpMetricOffsetTable_Object = MibTable
ruijieDvmrpMetricOffsetTable = _RuijieDvmrpMetricOffsetTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 29, 1, 3)
)
if mibBuilder.loadTexts:
    ruijieDvmrpMetricOffsetTable.setStatus("current")
_RuijieDvmrpMetricOffsetEntry_Object = MibTableRow
ruijieDvmrpMetricOffsetEntry = _RuijieDvmrpMetricOffsetEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 29, 1, 3, 1)
)
ruijieDvmrpMetricOffsetEntry.setIndexNames(
    (0, "RUIJIE-DVMRPINTEROPERABILITY-MIB", "ruijieDvmrpMetricOffsetIfIndex"),
    (0, "RUIJIE-DVMRPINTEROPERABILITY-MIB", "ruijieDvmrpMetricOffsetInOrOut"),
)
if mibBuilder.loadTexts:
    ruijieDvmrpMetricOffsetEntry.setStatus("current")
_RuijieDvmrpMetricOffsetIfIndex_Type = InterfaceIndex
_RuijieDvmrpMetricOffsetIfIndex_Object = MibTableColumn
ruijieDvmrpMetricOffsetIfIndex = _RuijieDvmrpMetricOffsetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 29, 1, 3, 1, 1),
    _RuijieDvmrpMetricOffsetIfIndex_Type()
)
ruijieDvmrpMetricOffsetIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieDvmrpMetricOffsetIfIndex.setStatus("current")


class _RuijieDvmrpMetricOffsetInOrOut_Type(Integer32):
    """Custom type ruijieDvmrpMetricOffsetInOrOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2))
    )


_RuijieDvmrpMetricOffsetInOrOut_Type.__name__ = "Integer32"
_RuijieDvmrpMetricOffsetInOrOut_Object = MibTableColumn
ruijieDvmrpMetricOffsetInOrOut = _RuijieDvmrpMetricOffsetInOrOut_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 29, 1, 3, 1, 2),
    _RuijieDvmrpMetricOffsetInOrOut_Type()
)
ruijieDvmrpMetricOffsetInOrOut.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieDvmrpMetricOffsetInOrOut.setStatus("current")


class _RuijieDvmrpMetricOffsetIncrement_Type(Integer32):
    """Custom type ruijieDvmrpMetricOffsetIncrement based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_RuijieDvmrpMetricOffsetIncrement_Type.__name__ = "Integer32"
_RuijieDvmrpMetricOffsetIncrement_Object = MibTableColumn
ruijieDvmrpMetricOffsetIncrement = _RuijieDvmrpMetricOffsetIncrement_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 29, 1, 3, 1, 3),
    _RuijieDvmrpMetricOffsetIncrement_Type()
)
ruijieDvmrpMetricOffsetIncrement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDvmrpMetricOffsetIncrement.setStatus("current")
_RuijieDvmrpSummaryTable_Object = MibTable
ruijieDvmrpSummaryTable = _RuijieDvmrpSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 29, 1, 4)
)
if mibBuilder.loadTexts:
    ruijieDvmrpSummaryTable.setStatus("current")
_RuijieDvmrpSummaryEntry_Object = MibTableRow
ruijieDvmrpSummaryEntry = _RuijieDvmrpSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 29, 1, 4, 1)
)
ruijieDvmrpSummaryEntry.setIndexNames(
    (0, "RUIJIE-DVMRPINTEROPERABILITY-MIB", "ruijieDvmrpIfIndex"),
    (0, "RUIJIE-DVMRPINTEROPERABILITY-MIB", "ruijieDvmrpSummaryAddress"),
    (0, "RUIJIE-DVMRPINTEROPERABILITY-MIB", "ruijieDvmrpSummaryMask"),
)
if mibBuilder.loadTexts:
    ruijieDvmrpSummaryEntry.setStatus("current")
_RuijieDvmrpIfIndex_Type = InterfaceIndex
_RuijieDvmrpIfIndex_Object = MibTableColumn
ruijieDvmrpIfIndex = _RuijieDvmrpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 29, 1, 4, 1, 1),
    _RuijieDvmrpIfIndex_Type()
)
ruijieDvmrpIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieDvmrpIfIndex.setStatus("current")
_RuijieDvmrpSummaryAddress_Type = IpAddress
_RuijieDvmrpSummaryAddress_Object = MibTableColumn
ruijieDvmrpSummaryAddress = _RuijieDvmrpSummaryAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 29, 1, 4, 1, 2),
    _RuijieDvmrpSummaryAddress_Type()
)
ruijieDvmrpSummaryAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieDvmrpSummaryAddress.setStatus("current")
_RuijieDvmrpSummaryMask_Type = IpAddress
_RuijieDvmrpSummaryMask_Object = MibTableColumn
ruijieDvmrpSummaryMask = _RuijieDvmrpSummaryMask_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 29, 1, 4, 1, 3),
    _RuijieDvmrpSummaryMask_Type()
)
ruijieDvmrpSummaryMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieDvmrpSummaryMask.setStatus("current")


class _RuijieDvmrpSummaryMetric_Type(Integer32):
    """Custom type ruijieDvmrpSummaryMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_RuijieDvmrpSummaryMetric_Type.__name__ = "Integer32"
_RuijieDvmrpSummaryMetric_Object = MibTableColumn
ruijieDvmrpSummaryMetric = _RuijieDvmrpSummaryMetric_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 29, 1, 4, 1, 4),
    _RuijieDvmrpSummaryMetric_Type()
)
ruijieDvmrpSummaryMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieDvmrpSummaryMetric.setStatus("current")
_RuijieDvmrpSummaryStatus_Type = RowStatus
_RuijieDvmrpSummaryStatus_Object = MibTableColumn
ruijieDvmrpSummaryStatus = _RuijieDvmrpSummaryStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 29, 1, 4, 1, 5),
    _RuijieDvmrpSummaryStatus_Type()
)
ruijieDvmrpSummaryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieDvmrpSummaryStatus.setStatus("current")
_RuijieDvmrpMetricTable_Object = MibTable
ruijieDvmrpMetricTable = _RuijieDvmrpMetricTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 29, 1, 5)
)
if mibBuilder.loadTexts:
    ruijieDvmrpMetricTable.setStatus("current")
_RuijieDvmrpMetricEntry_Object = MibTableRow
ruijieDvmrpMetricEntry = _RuijieDvmrpMetricEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 29, 1, 5, 1)
)
ruijieDvmrpMetricEntry.setIndexNames(
    (0, "RUIJIE-DVMRPINTEROPERABILITY-MIB", "ruijieDvmrpMetricIfIndex"),
    (0, "RUIJIE-DVMRPINTEROPERABILITY-MIB", "ruijieDvmrpMetric"),
    (0, "RUIJIE-DVMRPINTEROPERABILITY-MIB", "ruijieDvmrpMetricProtocolId"),
)
if mibBuilder.loadTexts:
    ruijieDvmrpMetricEntry.setStatus("current")
_RuijieDvmrpMetricIfIndex_Type = InterfaceIndex
_RuijieDvmrpMetricIfIndex_Object = MibTableColumn
ruijieDvmrpMetricIfIndex = _RuijieDvmrpMetricIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 29, 1, 5, 1, 1),
    _RuijieDvmrpMetricIfIndex_Type()
)
ruijieDvmrpMetricIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieDvmrpMetricIfIndex.setStatus("current")


class _RuijieDvmrpMetric_Type(Integer32):
    """Custom type ruijieDvmrpMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_RuijieDvmrpMetric_Type.__name__ = "Integer32"
_RuijieDvmrpMetric_Object = MibTableColumn
ruijieDvmrpMetric = _RuijieDvmrpMetric_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 29, 1, 5, 1, 2),
    _RuijieDvmrpMetric_Type()
)
ruijieDvmrpMetric.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieDvmrpMetric.setStatus("current")
_RuijieDvmrpMetricListAclName_Type = DisplayString
_RuijieDvmrpMetricListAclName_Object = MibTableColumn
ruijieDvmrpMetricListAclName = _RuijieDvmrpMetricListAclName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 29, 1, 5, 1, 3),
    _RuijieDvmrpMetricListAclName_Type()
)
ruijieDvmrpMetricListAclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieDvmrpMetricListAclName.setStatus("current")


class _RuijieDvmrpMetricProtocolId_Type(Integer32):
    """Custom type ruijieDvmrpMetricProtocolId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("ospf", 1),
          ("rip", 2),
          ("static", 3),
          ("dvmrp", 4))
    )


_RuijieDvmrpMetricProtocolId_Type.__name__ = "Integer32"
_RuijieDvmrpMetricProtocolId_Object = MibTableColumn
ruijieDvmrpMetricProtocolId = _RuijieDvmrpMetricProtocolId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 29, 1, 5, 1, 4),
    _RuijieDvmrpMetricProtocolId_Type()
)
ruijieDvmrpMetricProtocolId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieDvmrpMetricProtocolId.setStatus("current")
_RuijieDvmrpMetricStatus_Type = RowStatus
_RuijieDvmrpMetricStatus_Object = MibTableColumn
ruijieDvmrpMetricStatus = _RuijieDvmrpMetricStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 29, 1, 5, 1, 5),
    _RuijieDvmrpMetricStatus_Type()
)
ruijieDvmrpMetricStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieDvmrpMetricStatus.setStatus("current")
_RuijieDvmrpRouteTable_Object = MibTable
ruijieDvmrpRouteTable = _RuijieDvmrpRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 29, 1, 6)
)
if mibBuilder.loadTexts:
    ruijieDvmrpRouteTable.setStatus("current")
_RuijieDvmrpRouteEntry_Object = MibTableRow
ruijieDvmrpRouteEntry = _RuijieDvmrpRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 29, 1, 6, 1)
)
ruijieDvmrpRouteEntry.setIndexNames(
    (0, "RUIJIE-DVMRPINTEROPERABILITY-MIB", "ruijieDvmrpRouteIpAddress"),
    (0, "RUIJIE-DVMRPINTEROPERABILITY-MIB", "ruijieDvmrpRouteInterface"),
)
if mibBuilder.loadTexts:
    ruijieDvmrpRouteEntry.setStatus("current")
_RuijieDvmrpRouteIpAddress_Type = IpAddress
_RuijieDvmrpRouteIpAddress_Object = MibTableColumn
ruijieDvmrpRouteIpAddress = _RuijieDvmrpRouteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 29, 1, 6, 1, 1),
    _RuijieDvmrpRouteIpAddress_Type()
)
ruijieDvmrpRouteIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieDvmrpRouteIpAddress.setStatus("current")
_RuijieDvmrpRouteInterface_Type = InterfaceIndex
_RuijieDvmrpRouteInterface_Object = MibTableColumn
ruijieDvmrpRouteInterface = _RuijieDvmrpRouteInterface_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 29, 1, 6, 1, 2),
    _RuijieDvmrpRouteInterface_Type()
)
ruijieDvmrpRouteInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieDvmrpRouteInterface.setStatus("current")
_RuijieDvmrpRouteDistance_Type = Integer32
_RuijieDvmrpRouteDistance_Object = MibTableColumn
ruijieDvmrpRouteDistance = _RuijieDvmrpRouteDistance_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 29, 1, 6, 1, 3),
    _RuijieDvmrpRouteDistance_Type()
)
ruijieDvmrpRouteDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDvmrpRouteDistance.setStatus("current")
_RuijieDvmrpRouteMetric_Type = Integer32
_RuijieDvmrpRouteMetric_Object = MibTableColumn
ruijieDvmrpRouteMetric = _RuijieDvmrpRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 29, 1, 6, 1, 4),
    _RuijieDvmrpRouteMetric_Type()
)
ruijieDvmrpRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDvmrpRouteMetric.setStatus("current")
_RuijieDvmrpRouteUptime_Type = TimeTicks
_RuijieDvmrpRouteUptime_Object = MibTableColumn
ruijieDvmrpRouteUptime = _RuijieDvmrpRouteUptime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 29, 1, 6, 1, 5),
    _RuijieDvmrpRouteUptime_Type()
)
ruijieDvmrpRouteUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDvmrpRouteUptime.setStatus("current")
_RuijieDvmrpRouteExpires_Type = TimeTicks
_RuijieDvmrpRouteExpires_Object = MibTableColumn
ruijieDvmrpRouteExpires = _RuijieDvmrpRouteExpires_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 29, 1, 6, 1, 6),
    _RuijieDvmrpRouteExpires_Type()
)
ruijieDvmrpRouteExpires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDvmrpRouteExpires.setStatus("current")
_RuijieDvmrpRouteNextHopAddress_Type = IpAddress
_RuijieDvmrpRouteNextHopAddress_Object = MibTableColumn
ruijieDvmrpRouteNextHopAddress = _RuijieDvmrpRouteNextHopAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 29, 1, 6, 1, 7),
    _RuijieDvmrpRouteNextHopAddress_Type()
)
ruijieDvmrpRouteNextHopAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDvmrpRouteNextHopAddress.setStatus("current")
_RuijieDvmrpRouteNextHopInterface_Type = InterfaceIndex
_RuijieDvmrpRouteNextHopInterface_Object = MibTableColumn
ruijieDvmrpRouteNextHopInterface = _RuijieDvmrpRouteNextHopInterface_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 29, 1, 6, 1, 8),
    _RuijieDvmrpRouteNextHopInterface_Type()
)
ruijieDvmrpRouteNextHopInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDvmrpRouteNextHopInterface.setStatus("current")
_RuijieDvmrpRouteStatus_Type = EnabledStatus
_RuijieDvmrpRouteStatus_Object = MibTableColumn
ruijieDvmrpRouteStatus = _RuijieDvmrpRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 29, 1, 6, 1, 9),
    _RuijieDvmrpRouteStatus_Type()
)
ruijieDvmrpRouteStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDvmrpRouteStatus.setStatus("current")
_RuijieDvmrpTraps_ObjectIdentity = ObjectIdentity
ruijieDvmrpTraps = _RuijieDvmrpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 29, 1, 7)
)
_RuijieDvmrpMIBConformance_ObjectIdentity = ObjectIdentity
ruijieDvmrpMIBConformance = _RuijieDvmrpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 29, 2)
)
_RuijieDvmrpMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieDvmrpMIBCompliances = _RuijieDvmrpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 29, 2, 1)
)
_RuijieDvmrpMIBGroups_ObjectIdentity = ObjectIdentity
ruijieDvmrpMIBGroups = _RuijieDvmrpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 29, 2, 2)
)

# Managed Objects groups

ruijieDvmrpBaseMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 29, 2, 2, 1)
)
ruijieDvmrpBaseMIBGroup.setObjects(
      *(("RUIJIE-DVMRPINTEROPERABILITY-MIB", "ruijieDvmrpRouteLimit"),
        ("RUIJIE-DVMRPINTEROPERABILITY-MIB", "ruijieDvmrpRoutehogNotification"))
)
if mibBuilder.loadTexts:
    ruijieDvmrpBaseMIBGroup.setStatus("current")

ruijieDvmrpInterfaceMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 29, 2, 2, 2)
)
ruijieDvmrpInterfaceMIBGroup.setObjects(
      *(("RUIJIE-DVMRPINTEROPERABILITY-MIB", "ruijieDvmrpInterfaceDefaultInformation"),
        ("RUIJIE-DVMRPINTEROPERABILITY-MIB", "ruijieDvmrpInterfaceUnicastRoutingStatus"),
        ("RUIJIE-DVMRPINTEROPERABILITY-MIB", "ruijieDvmrpInterfaceRejectNonPrunersStatus"),
        ("RUIJIE-DVMRPINTEROPERABILITY-MIB", "ruijieDvmrpInterfaceAutoSummaryStatus"),
        ("RUIJIE-DVMRPINTEROPERABILITY-MIB", "ruijieDvmrpInterfaceRtsRec"),
        ("RUIJIE-DVMRPINTEROPERABILITY-MIB", "ruijieDvmrpInterfacePoisonReverseRtsRec"),
        ("RUIJIE-DVMRPINTEROPERABILITY-MIB", "ruijieDvmrpInterfaceUniRtAdvertised"),
        ("RUIJIE-DVMRPINTEROPERABILITY-MIB", "ruijieDvmrpInterfaceDvmrpRtAdvertised"))
)
if mibBuilder.loadTexts:
    ruijieDvmrpInterfaceMIBGroup.setStatus("current")

ruijieDvmrpMetricOffsetMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 29, 2, 2, 3)
)
ruijieDvmrpMetricOffsetMIBGroup.setObjects(
    ("RUIJIE-DVMRPINTEROPERABILITY-MIB", "ruijieDvmrpMetricOffsetIncrement")
)
if mibBuilder.loadTexts:
    ruijieDvmrpMetricOffsetMIBGroup.setStatus("current")

ruijieDvmrpSummaryMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 29, 2, 2, 4)
)
ruijieDvmrpSummaryMIBGroup.setObjects(
      *(("RUIJIE-DVMRPINTEROPERABILITY-MIB", "ruijieDvmrpSummaryMetric"),
        ("RUIJIE-DVMRPINTEROPERABILITY-MIB", "ruijieDvmrpSummaryStatus"))
)
if mibBuilder.loadTexts:
    ruijieDvmrpSummaryMIBGroup.setStatus("current")

ruijieDvmrpMetricMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 29, 2, 2, 5)
)
ruijieDvmrpMetricMIBGroup.setObjects(
      *(("RUIJIE-DVMRPINTEROPERABILITY-MIB", "ruijieDvmrpMetricListAclName"),
        ("RUIJIE-DVMRPINTEROPERABILITY-MIB", "ruijieDvmrpMetricStatus"))
)
if mibBuilder.loadTexts:
    ruijieDvmrpMetricMIBGroup.setStatus("current")

ruijieDvmrpRouteMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 29, 2, 2, 6)
)
ruijieDvmrpRouteMIBGroup.setObjects(
      *(("RUIJIE-DVMRPINTEROPERABILITY-MIB", "ruijieDvmrpRouteDistance"),
        ("RUIJIE-DVMRPINTEROPERABILITY-MIB", "ruijieDvmrpRouteMetric"),
        ("RUIJIE-DVMRPINTEROPERABILITY-MIB", "ruijieDvmrpRouteUptime"),
        ("RUIJIE-DVMRPINTEROPERABILITY-MIB", "ruijieDvmrpRouteExpires"),
        ("RUIJIE-DVMRPINTEROPERABILITY-MIB", "ruijieDvmrpRouteNextHopAddress"),
        ("RUIJIE-DVMRPINTEROPERABILITY-MIB", "ruijieDvmrpRouteNextHopInterface"),
        ("RUIJIE-DVMRPINTEROPERABILITY-MIB", "ruijieDvmrpRouteStatus"))
)
if mibBuilder.loadTexts:
    ruijieDvmrpRouteMIBGroup.setStatus("current")


# Notification objects

ruijieDvmrpRouteInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 29, 1, 7, 1)
)
if mibBuilder.loadTexts:
    ruijieDvmrpRouteInformation.setStatus(
        "current"
    )


# Notifications groups

ruijieDvmrpRouteTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 29, 2, 2, 7)
)
ruijieDvmrpRouteTrapGroup.setObjects(
    ("RUIJIE-DVMRPINTEROPERABILITY-MIB", "ruijieDvmrpRouteInformation")
)
if mibBuilder.loadTexts:
    ruijieDvmrpRouteTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ruijieDvmrpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 29, 2, 1, 1)
)
ruijieDvmrpMIBCompliance.setObjects(
      *(("RUIJIE-DVMRPINTEROPERABILITY-MIB", "ruijieDvmrpBaseMIBGroup"),
        ("RUIJIE-DVMRPINTEROPERABILITY-MIB", "ruijieDvmrpInterfaceMIBGroup"),
        ("RUIJIE-DVMRPINTEROPERABILITY-MIB", "ruijieDvmrpMetricOffsetMIBGroup"),
        ("RUIJIE-DVMRPINTEROPERABILITY-MIB", "ruijieDvmrpSummaryMIBGroup"),
        ("RUIJIE-DVMRPINTEROPERABILITY-MIB", "ruijieDvmrpMetricMIBGroup"),
        ("RUIJIE-DVMRPINTEROPERABILITY-MIB", "ruijieDvmrpRouteMIBGroup"),
        ("RUIJIE-DVMRPINTEROPERABILITY-MIB", "ruijieDvmrpRouteTrapGroup"))
)
if mibBuilder.loadTexts:
    ruijieDvmrpMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-DVMRPINTEROPERABILITY-MIB",
    **{"ruijieDvmrpMIB": ruijieDvmrpMIB,
       "ruijieDvmrpMIBObjects": ruijieDvmrpMIBObjects,
       "ruijieDvmrpGroup": ruijieDvmrpGroup,
       "ruijieDvmrpRouteLimit": ruijieDvmrpRouteLimit,
       "ruijieDvmrpRoutehogNotification": ruijieDvmrpRoutehogNotification,
       "ruijieDvmrpInterfaceTable": ruijieDvmrpInterfaceTable,
       "ruijieDvmrpInterfaceEntry": ruijieDvmrpInterfaceEntry,
       "ruijieDvmrpInterfaceIfIndex": ruijieDvmrpInterfaceIfIndex,
       "ruijieDvmrpInterfaceDefaultInformation": ruijieDvmrpInterfaceDefaultInformation,
       "ruijieDvmrpInterfaceUnicastRoutingStatus": ruijieDvmrpInterfaceUnicastRoutingStatus,
       "ruijieDvmrpInterfaceRejectNonPrunersStatus": ruijieDvmrpInterfaceRejectNonPrunersStatus,
       "ruijieDvmrpInterfaceAutoSummaryStatus": ruijieDvmrpInterfaceAutoSummaryStatus,
       "ruijieDvmrpInterfaceRtsRec": ruijieDvmrpInterfaceRtsRec,
       "ruijieDvmrpInterfacePoisonReverseRtsRec": ruijieDvmrpInterfacePoisonReverseRtsRec,
       "ruijieDvmrpInterfaceUniRtAdvertised": ruijieDvmrpInterfaceUniRtAdvertised,
       "ruijieDvmrpInterfaceDvmrpRtAdvertised": ruijieDvmrpInterfaceDvmrpRtAdvertised,
       "ruijieDvmrpMetricOffsetTable": ruijieDvmrpMetricOffsetTable,
       "ruijieDvmrpMetricOffsetEntry": ruijieDvmrpMetricOffsetEntry,
       "ruijieDvmrpMetricOffsetIfIndex": ruijieDvmrpMetricOffsetIfIndex,
       "ruijieDvmrpMetricOffsetInOrOut": ruijieDvmrpMetricOffsetInOrOut,
       "ruijieDvmrpMetricOffsetIncrement": ruijieDvmrpMetricOffsetIncrement,
       "ruijieDvmrpSummaryTable": ruijieDvmrpSummaryTable,
       "ruijieDvmrpSummaryEntry": ruijieDvmrpSummaryEntry,
       "ruijieDvmrpIfIndex": ruijieDvmrpIfIndex,
       "ruijieDvmrpSummaryAddress": ruijieDvmrpSummaryAddress,
       "ruijieDvmrpSummaryMask": ruijieDvmrpSummaryMask,
       "ruijieDvmrpSummaryMetric": ruijieDvmrpSummaryMetric,
       "ruijieDvmrpSummaryStatus": ruijieDvmrpSummaryStatus,
       "ruijieDvmrpMetricTable": ruijieDvmrpMetricTable,
       "ruijieDvmrpMetricEntry": ruijieDvmrpMetricEntry,
       "ruijieDvmrpMetricIfIndex": ruijieDvmrpMetricIfIndex,
       "ruijieDvmrpMetric": ruijieDvmrpMetric,
       "ruijieDvmrpMetricListAclName": ruijieDvmrpMetricListAclName,
       "ruijieDvmrpMetricProtocolId": ruijieDvmrpMetricProtocolId,
       "ruijieDvmrpMetricStatus": ruijieDvmrpMetricStatus,
       "ruijieDvmrpRouteTable": ruijieDvmrpRouteTable,
       "ruijieDvmrpRouteEntry": ruijieDvmrpRouteEntry,
       "ruijieDvmrpRouteIpAddress": ruijieDvmrpRouteIpAddress,
       "ruijieDvmrpRouteInterface": ruijieDvmrpRouteInterface,
       "ruijieDvmrpRouteDistance": ruijieDvmrpRouteDistance,
       "ruijieDvmrpRouteMetric": ruijieDvmrpRouteMetric,
       "ruijieDvmrpRouteUptime": ruijieDvmrpRouteUptime,
       "ruijieDvmrpRouteExpires": ruijieDvmrpRouteExpires,
       "ruijieDvmrpRouteNextHopAddress": ruijieDvmrpRouteNextHopAddress,
       "ruijieDvmrpRouteNextHopInterface": ruijieDvmrpRouteNextHopInterface,
       "ruijieDvmrpRouteStatus": ruijieDvmrpRouteStatus,
       "ruijieDvmrpTraps": ruijieDvmrpTraps,
       "ruijieDvmrpRouteInformation": ruijieDvmrpRouteInformation,
       "ruijieDvmrpMIBConformance": ruijieDvmrpMIBConformance,
       "ruijieDvmrpMIBCompliances": ruijieDvmrpMIBCompliances,
       "ruijieDvmrpMIBCompliance": ruijieDvmrpMIBCompliance,
       "ruijieDvmrpMIBGroups": ruijieDvmrpMIBGroups,
       "ruijieDvmrpBaseMIBGroup": ruijieDvmrpBaseMIBGroup,
       "ruijieDvmrpInterfaceMIBGroup": ruijieDvmrpInterfaceMIBGroup,
       "ruijieDvmrpMetricOffsetMIBGroup": ruijieDvmrpMetricOffsetMIBGroup,
       "ruijieDvmrpSummaryMIBGroup": ruijieDvmrpSummaryMIBGroup,
       "ruijieDvmrpMetricMIBGroup": ruijieDvmrpMetricMIBGroup,
       "ruijieDvmrpRouteMIBGroup": ruijieDvmrpRouteMIBGroup,
       "ruijieDvmrpRouteTrapGroup": ruijieDvmrpRouteTrapGroup}
)
