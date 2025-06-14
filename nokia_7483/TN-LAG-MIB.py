# SNMP MIB module (TN-LAG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_7483/TN-LAG-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 18:08:43 2025
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

(dot3adAggPortEntry,) = mibBuilder.importSymbols(
    "IEEE8023-LAG-MIB",
    "dot3adAggPortEntry")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(tnPortLagId,
 tnPortPortID) = mibBuilder.importSymbols(
    "TN-PORT-MIB",
    "tnPortLagId",
    "tnPortPortID")

(TItemLongDescription,
 TNamedItemOrEmpty) = mibBuilder.importSymbols(
    "TN-TC-MIB",
    "TItemLongDescription",
    "TNamedItemOrEmpty")

(tnSRMIBModules,
 tnSRNotifyPrefix,
 tnSRObjs) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnSRMIBModules",
    "tnSRNotifyPrefix",
    "tnSRObjs")

(tnSysSwitchId,) = mibBuilder.importSymbols(
    "TROPIC-SYSTEM-MIB",
    "tnSysSwitchId")


# MODULE-IDENTITY

tnLagMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 5, 1, 3, 15)
)
if mibBuilder.loadTexts:
    tnLagMIBModule.setRevisions(
        ("1912-12-13 00:00",
         "1912-12-05 00:00",
         "1912-04-27 00:00",
         "1912-02-21 00:00",
         "1909-02-28 00:00",
         "1908-07-01 00:00",
         "1908-01-01 00:00",
         "1907-01-01 00:00",
         "1906-03-15 00:00",
         "1905-08-31 00:00",
         "1905-01-24 00:00",
         "1904-01-15 00:00",
         "1903-08-15 00:00",
         "1903-01-20 00:00",
         "1901-02-09 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class LAGInterfaceNumber(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )



class LAGSubgroup(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 8),
    )



# MIB Managed Objects in the order of their OIDs

_TnLagObjects_ObjectIdentity = ObjectIdentity
tnLagObjects = _TnLagObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 15)
)
_TnLagConfigTable_Object = MibTable
tnLagConfigTable = _TnLagConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 15, 2)
)
if mibBuilder.loadTexts:
    tnLagConfigTable.setStatus("current")
_TnLagConfigEntry_Object = MibTableRow
tnLagConfigEntry = _TnLagConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 15, 2, 1)
)
tnLagConfigEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-LAG-MIB", "tnLagIndex"),
)
if mibBuilder.loadTexts:
    tnLagConfigEntry.setStatus("current")
_TnLagIndex_Type = LAGInterfaceNumber
_TnLagIndex_Object = MibTableColumn
tnLagIndex = _TnLagIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 15, 2, 1, 1),
    _TnLagIndex_Type()
)
tnLagIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnLagIndex.setStatus("current")
_TnLagRowStatus_Type = RowStatus
_TnLagRowStatus_Object = MibTableColumn
tnLagRowStatus = _TnLagRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 15, 2, 1, 2),
    _TnLagRowStatus_Type()
)
tnLagRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnLagRowStatus.setStatus("current")


class _TnLagPortThreshold_Type(Integer32):
    """Custom type tnLagPortThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnLagPortThreshold_Type.__name__ = "Integer32"
_TnLagPortThreshold_Object = MibTableColumn
tnLagPortThreshold = _TnLagPortThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 15, 2, 1, 3),
    _TnLagPortThreshold_Type()
)
tnLagPortThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnLagPortThreshold.setStatus("current")


class _TnLagPortThresholdAction_Type(Integer32):
    """Custom type tnLagPortThresholdAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("dynamicCost", 2))
    )


_TnLagPortThresholdAction_Type.__name__ = "Integer32"
_TnLagPortThresholdAction_Object = MibTableColumn
tnLagPortThresholdAction = _TnLagPortThresholdAction_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 15, 2, 1, 4),
    _TnLagPortThresholdAction_Type()
)
tnLagPortThresholdAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnLagPortThresholdAction.setStatus("current")


class _TnLagEnableMarkerGenerator_Type(TruthValue):
    """Custom type tnLagEnableMarkerGenerator based on TruthValue"""
    defaultValue = 2


_TnLagEnableMarkerGenerator_Type.__name__ = "TruthValue"
_TnLagEnableMarkerGenerator_Object = MibTableColumn
tnLagEnableMarkerGenerator = _TnLagEnableMarkerGenerator_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 15, 2, 1, 5),
    _TnLagEnableMarkerGenerator_Type()
)
tnLagEnableMarkerGenerator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnLagEnableMarkerGenerator.setStatus("current")


class _TnLagEnableLACP_Type(TruthValue):
    """Custom type tnLagEnableLACP based on TruthValue"""
    defaultValue = 2


_TnLagEnableLACP_Type.__name__ = "TruthValue"
_TnLagEnableLACP_Object = MibTableColumn
tnLagEnableLACP = _TnLagEnableLACP_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 15, 2, 1, 6),
    _TnLagEnableLACP_Type()
)
tnLagEnableLACP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnLagEnableLACP.setStatus("current")


class _TnLagDescription_Type(TItemLongDescription):
    """Custom type tnLagDescription based on TItemLongDescription"""
    defaultHexValue = ""


_TnLagDescription_Type.__name__ = "TItemLongDescription"
_TnLagDescription_Object = MibTableColumn
tnLagDescription = _TnLagDescription_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 15, 2, 1, 7),
    _TnLagDescription_Type()
)
tnLagDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnLagDescription.setStatus("current")


class _TnLagDynamicCosting_Type(TruthValue):
    """Custom type tnLagDynamicCosting based on TruthValue"""
    defaultValue = 2


_TnLagDynamicCosting_Type.__name__ = "TruthValue"
_TnLagDynamicCosting_Object = MibTableColumn
tnLagDynamicCosting = _TnLagDynamicCosting_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 15, 2, 1, 8),
    _TnLagDynamicCosting_Type()
)
tnLagDynamicCosting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnLagDynamicCosting.setStatus("current")


class _TnLagLACPMode_Type(Integer32):
    """Custom type tnLagLACPMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("passive", 1),
          ("active", 2))
    )


_TnLagLACPMode_Type.__name__ = "Integer32"
_TnLagLACPMode_Object = MibTableColumn
tnLagLACPMode = _TnLagLACPMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 15, 2, 1, 9),
    _TnLagLACPMode_Type()
)
tnLagLACPMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnLagLACPMode.setStatus("current")


class _TnLagLACPAdminKeyAutogen_Type(TruthValue):
    """Custom type tnLagLACPAdminKeyAutogen based on TruthValue"""
    defaultValue = 1


_TnLagLACPAdminKeyAutogen_Type.__name__ = "TruthValue"
_TnLagLACPAdminKeyAutogen_Object = MibTableColumn
tnLagLACPAdminKeyAutogen = _TnLagLACPAdminKeyAutogen_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 15, 2, 1, 10),
    _TnLagLACPAdminKeyAutogen_Type()
)
tnLagLACPAdminKeyAutogen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLagLACPAdminKeyAutogen.setStatus("current")


class _TnLagLACPTransmitInterval_Type(Integer32):
    """Custom type tnLagLACPTransmitInterval based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("slow", 1),
          ("fast", 2))
    )


_TnLagLACPTransmitInterval_Type.__name__ = "Integer32"
_TnLagLACPTransmitInterval_Object = MibTableColumn
tnLagLACPTransmitInterval = _TnLagLACPTransmitInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 15, 2, 1, 11),
    _TnLagLACPTransmitInterval_Type()
)
tnLagLACPTransmitInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnLagLACPTransmitInterval.setStatus("current")


class _TnLagAccessAdaptQos_Type(Integer32):
    """Custom type tnLagAccessAdaptQos based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("link", 1),
          ("distribute", 2))
    )


_TnLagAccessAdaptQos_Type.__name__ = "Integer32"
_TnLagAccessAdaptQos_Object = MibTableColumn
tnLagAccessAdaptQos = _TnLagAccessAdaptQos_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 15, 2, 1, 12),
    _TnLagAccessAdaptQos_Type()
)
tnLagAccessAdaptQos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnLagAccessAdaptQos.setStatus("current")


class _TnLagLACPXmitStdby_Type(TruthValue):
    """Custom type tnLagLACPXmitStdby based on TruthValue"""
    defaultValue = 1


_TnLagLACPXmitStdby_Type.__name__ = "TruthValue"
_TnLagLACPXmitStdby_Object = MibTableColumn
tnLagLACPXmitStdby = _TnLagLACPXmitStdby_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 15, 2, 1, 13),
    _TnLagLACPXmitStdby_Type()
)
tnLagLACPXmitStdby.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnLagLACPXmitStdby.setStatus("current")


class _TnLagLACPSelCrit_Type(Integer32):
    """Custom type tnLagLACPSelCrit based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("highest-count", 1),
          ("highest-weight", 2))
    )


_TnLagLACPSelCrit_Type.__name__ = "Integer32"
_TnLagLACPSelCrit_Object = MibTableColumn
tnLagLACPSelCrit = _TnLagLACPSelCrit_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 15, 2, 1, 14),
    _TnLagLACPSelCrit_Type()
)
tnLagLACPSelCrit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnLagLACPSelCrit.setStatus("current")


class _TnLagLACPSelCritSlaveToPartner_Type(TruthValue):
    """Custom type tnLagLACPSelCritSlaveToPartner based on TruthValue"""
    defaultValue = 2


_TnLagLACPSelCritSlaveToPartner_Type.__name__ = "TruthValue"
_TnLagLACPSelCritSlaveToPartner_Object = MibTableColumn
tnLagLACPSelCritSlaveToPartner = _TnLagLACPSelCritSlaveToPartner_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 15, 2, 1, 15),
    _TnLagLACPSelCritSlaveToPartner_Type()
)
tnLagLACPSelCritSlaveToPartner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnLagLACPSelCritSlaveToPartner.setStatus("current")
_TnLagLACPNbrOfSubGroups_Type = Unsigned32
_TnLagLACPNbrOfSubGroups_Object = MibTableColumn
tnLagLACPNbrOfSubGroups = _TnLagLACPNbrOfSubGroups_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 15, 2, 1, 16),
    _TnLagLACPNbrOfSubGroups_Type()
)
tnLagLACPNbrOfSubGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLagLACPNbrOfSubGroups.setStatus("current")


class _TnLagholdTimeDown_Type(Unsigned32):
    """Custom type tnLagholdTimeDown based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_TnLagholdTimeDown_Type.__name__ = "Unsigned32"
_TnLagholdTimeDown_Object = MibTableColumn
tnLagholdTimeDown = _TnLagholdTimeDown_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 15, 2, 1, 17),
    _TnLagholdTimeDown_Type()
)
tnLagholdTimeDown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnLagholdTimeDown.setStatus("current")
if mibBuilder.loadTexts:
    tnLagholdTimeDown.setUnits("100s of milliseconds")


class _TnLagPortType_Type(Integer32):
    """Custom type tnLagPortType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("standard", 1),
          ("hsmda", 2))
    )


_TnLagPortType_Type.__name__ = "Integer32"
_TnLagPortType_Object = MibTableColumn
tnLagPortType = _TnLagPortType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 15, 2, 1, 18),
    _TnLagPortType_Type()
)
tnLagPortType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnLagPortType.setStatus("current")


class _TnLagPerFpIngQueuing_Type(TruthValue):
    """Custom type tnLagPerFpIngQueuing based on TruthValue"""
    defaultValue = 2


_TnLagPerFpIngQueuing_Type.__name__ = "TruthValue"
_TnLagPerFpIngQueuing_Object = MibTableColumn
tnLagPerFpIngQueuing = _TnLagPerFpIngQueuing_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 15, 2, 1, 19),
    _TnLagPerFpIngQueuing_Type()
)
tnLagPerFpIngQueuing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnLagPerFpIngQueuing.setStatus("current")
_TnLagOperationTable_Object = MibTable
tnLagOperationTable = _TnLagOperationTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 15, 3)
)
if mibBuilder.loadTexts:
    tnLagOperationTable.setStatus("current")
_TnLagOperationEntry_Object = MibTableRow
tnLagOperationEntry = _TnLagOperationEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 15, 3, 1)
)
if mibBuilder.loadTexts:
    tnLagOperationEntry.setStatus("current")
_TnLagIfIndex_Type = InterfaceIndexOrZero
_TnLagIfIndex_Object = MibTableColumn
tnLagIfIndex = _TnLagIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 15, 3, 1, 1),
    _TnLagIfIndex_Type()
)
tnLagIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLagIfIndex.setStatus("current")
_TnLagConfigLastChange_Type = TimeStamp
_TnLagConfigLastChange_Object = MibTableColumn
tnLagConfigLastChange = _TnLagConfigLastChange_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 15, 3, 1, 2),
    _TnLagConfigLastChange_Type()
)
tnLagConfigLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLagConfigLastChange.setStatus("current")
_TnLagPortThresholdFalling_Type = Counter32
_TnLagPortThresholdFalling_Object = MibTableColumn
tnLagPortThresholdFalling = _TnLagPortThresholdFalling_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 15, 3, 1, 3),
    _TnLagPortThresholdFalling_Type()
)
tnLagPortThresholdFalling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLagPortThresholdFalling.setStatus("current")
_TnLagPortThresholdRising_Type = Counter32
_TnLagPortThresholdRising_Object = MibTableColumn
tnLagPortThresholdRising = _TnLagPortThresholdRising_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 15, 3, 1, 4),
    _TnLagPortThresholdRising_Type()
)
tnLagPortThresholdRising.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLagPortThresholdRising.setStatus("current")
_TnLagScalar1_Type = Unsigned32
_TnLagScalar1_Object = MibScalar
tnLagScalar1 = _TnLagScalar1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 15, 4),
    _TnLagScalar1_Type()
)
tnLagScalar1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLagScalar1.setStatus("current")
_TnLagMemberTable_Object = MibTable
tnLagMemberTable = _TnLagMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 15, 5)
)
if mibBuilder.loadTexts:
    tnLagMemberTable.setStatus("current")
_TnLagMemberEntry_Object = MibTableRow
tnLagMemberEntry = _TnLagMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 15, 5, 1)
)
tnLagMemberEntry.setIndexNames(
    (0, "TN-LAG-MIB", "tnLagIndex"),
    (0, "TN-PORT-MIB", "tnPortPortID"),
)
if mibBuilder.loadTexts:
    tnLagMemberEntry.setStatus("current")
_TnLagMemberPortName_Type = TNamedItemOrEmpty
_TnLagMemberPortName_Object = MibTableColumn
tnLagMemberPortName = _TnLagMemberPortName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 15, 5, 1, 1),
    _TnLagMemberPortName_Type()
)
tnLagMemberPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLagMemberPortName.setStatus("current")
_TnLagMemberPortIsPrimary_Type = TruthValue
_TnLagMemberPortIsPrimary_Object = MibTableColumn
tnLagMemberPortIsPrimary = _TnLagMemberPortIsPrimary_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 15, 5, 1, 2),
    _TnLagMemberPortIsPrimary_Type()
)
tnLagMemberPortIsPrimary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLagMemberPortIsPrimary.setStatus("current")
_TnLagPortTable_Object = MibTable
tnLagPortTable = _TnLagPortTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 15, 6)
)
if mibBuilder.loadTexts:
    tnLagPortTable.setStatus("current")
_TnLagPortEntry_Object = MibTableRow
tnLagPortEntry = _TnLagPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 15, 6, 1)
)
if mibBuilder.loadTexts:
    tnLagPortEntry.setStatus("current")


class _TnLagPortSubgroup_Type(LAGSubgroup):
    """Custom type tnLagPortSubgroup based on LAGSubgroup"""
    defaultValue = 1


_TnLagPortSubgroup_Type.__name__ = "LAGSubgroup"
_TnLagPortSubgroup_Object = MibTableColumn
tnLagPortSubgroup = _TnLagPortSubgroup_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 15, 6, 1, 1),
    _TnLagPortSubgroup_Type()
)
tnLagPortSubgroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLagPortSubgroup.setStatus("current")


class _TnLagPortActiveStdby_Type(Integer32):
    """Custom type tnLagPortActiveStdby based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("stand-by", 2))
    )


_TnLagPortActiveStdby_Type.__name__ = "Integer32"
_TnLagPortActiveStdby_Object = MibTableColumn
tnLagPortActiveStdby = _TnLagPortActiveStdby_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 15, 6, 1, 2),
    _TnLagPortActiveStdby_Type()
)
tnLagPortActiveStdby.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLagPortActiveStdby.setStatus("current")
_TnLagConfigXTable_Object = MibTable
tnLagConfigXTable = _TnLagConfigXTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 15, 7)
)
if mibBuilder.loadTexts:
    tnLagConfigXTable.setStatus("current")
_TnLagConfigXEntry_Object = MibTableRow
tnLagConfigXEntry = _TnLagConfigXEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 15, 7, 1)
)
if mibBuilder.loadTexts:
    tnLagConfigXEntry.setStatus("current")
_TnLagConfigXIngressAvailBandwidth_Type = Unsigned32
_TnLagConfigXIngressAvailBandwidth_Object = MibTableColumn
tnLagConfigXIngressAvailBandwidth = _TnLagConfigXIngressAvailBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 15, 7, 1, 1),
    _TnLagConfigXIngressAvailBandwidth_Type()
)
tnLagConfigXIngressAvailBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLagConfigXIngressAvailBandwidth.setStatus("current")
_TnLagConfigXEgressAvailBandwidth_Type = Unsigned32
_TnLagConfigXEgressAvailBandwidth_Object = MibTableColumn
tnLagConfigXEgressAvailBandwidth = _TnLagConfigXEgressAvailBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 15, 7, 1, 2),
    _TnLagConfigXEgressAvailBandwidth_Type()
)
tnLagConfigXEgressAvailBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLagConfigXEgressAvailBandwidth.setStatus("current")


class _TnLagConfigXMaxPortSize_Type(Integer32):
    """Custom type tnLagConfigXMaxPortSize based on Integer32"""
    defaultValue = 4


_TnLagConfigXMaxPortSize_Type.__name__ = "Integer32"
_TnLagConfigXMaxPortSize_Object = MibTableColumn
tnLagConfigXMaxPortSize = _TnLagConfigXMaxPortSize_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 15, 7, 1, 3),
    _TnLagConfigXMaxPortSize_Type()
)
tnLagConfigXMaxPortSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnLagConfigXMaxPortSize.setStatus("current")
_TnLagConfigXNumSelectedPorts_Type = Unsigned32
_TnLagConfigXNumSelectedPorts_Object = MibTableColumn
tnLagConfigXNumSelectedPorts = _TnLagConfigXNumSelectedPorts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 15, 7, 1, 4),
    _TnLagConfigXNumSelectedPorts_Type()
)
tnLagConfigXNumSelectedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLagConfigXNumSelectedPorts.setStatus("current")
_TnLagConfigXNumAttachedPorts_Type = Unsigned32
_TnLagConfigXNumAttachedPorts_Object = MibTableColumn
tnLagConfigXNumAttachedPorts = _TnLagConfigXNumAttachedPorts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 15, 7, 1, 5),
    _TnLagConfigXNumAttachedPorts_Type()
)
tnLagConfigXNumAttachedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLagConfigXNumAttachedPorts.setStatus("current")
_TnLagConfigXPrimaryPort_Type = InterfaceIndex
_TnLagConfigXPrimaryPort_Object = MibTableColumn
tnLagConfigXPrimaryPort = _TnLagConfigXPrimaryPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 15, 7, 1, 6),
    _TnLagConfigXPrimaryPort_Type()
)
tnLagConfigXPrimaryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLagConfigXPrimaryPort.setStatus("current")


class _TnLagAdminState_Type(Integer32):
    """Custom type tnLagAdminState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_TnLagAdminState_Type.__name__ = "Integer32"
_TnLagAdminState_Object = MibTableColumn
tnLagAdminState = _TnLagAdminState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 15, 7, 1, 7),
    _TnLagAdminState_Type()
)
tnLagAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLagAdminState.setStatus("current")


class _TnLagLPTConsequenceAction_Type(Integer32):
    """Custom type tnLagLPTConsequenceAction based on Integer32"""
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
        *(("noAction", 1),
          ("oneShutDown", 2),
          ("allShutDown", 3))
    )


_TnLagLPTConsequenceAction_Type.__name__ = "Integer32"
_TnLagLPTConsequenceAction_Object = MibTableColumn
tnLagLPTConsequenceAction = _TnLagLPTConsequenceAction_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 15, 7, 1, 8),
    _TnLagLPTConsequenceAction_Type()
)
tnLagLPTConsequenceAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnLagLPTConsequenceAction.setStatus("current")


class _TnLagLosProp_Type(Integer32):
    """Custom type tnLagLosProp based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("laserOn", 1),
          ("laserOff", 2))
    )


_TnLagLosProp_Type.__name__ = "Integer32"
_TnLagLosProp_Object = MibTableColumn
tnLagLosProp = _TnLagLosProp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 15, 7, 1, 9),
    _TnLagLosProp_Type()
)
tnLagLosProp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnLagLosProp.setStatus("current")


class _TnLagTPID_Type(Integer32):
    """Custom type tnLagTPID based on Integer32"""
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
        *(("qinqtpid1", 1),
          ("qinqtpid2", 2),
          ("qinqtpid3", 3),
          ("qinqtpid4", 4))
    )


_TnLagTPID_Type.__name__ = "Integer32"
_TnLagTPID_Object = MibTableColumn
tnLagTPID = _TnLagTPID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 15, 7, 1, 10),
    _TnLagTPID_Type()
)
tnLagTPID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnLagTPID.setStatus("current")


class _TnLagMtu_Type(Integer32):
    """Custom type tnLagMtu based on Integer32"""
    defaultValue = 9600


_TnLagMtu_Type.__name__ = "Integer32"
_TnLagMtu_Object = MibTableColumn
tnLagMtu = _TnLagMtu_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 15, 7, 1, 11),
    _TnLagMtu_Type()
)
tnLagMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnLagMtu.setStatus("current")
_TnLagSpeed_Type = Gauge32
_TnLagSpeed_Object = MibTableColumn
tnLagSpeed = _TnLagSpeed_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 15, 7, 1, 12),
    _TnLagSpeed_Type()
)
tnLagSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLagSpeed.setStatus("current")
_TnLagCommandTable_Object = MibTable
tnLagCommandTable = _TnLagCommandTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 15, 20)
)
if mibBuilder.loadTexts:
    tnLagCommandTable.setStatus("current")
_TnLagCommandEntry_Object = MibTableRow
tnLagCommandEntry = _TnLagCommandEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 15, 20, 1)
)
tnLagCommandEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-LAG-MIB", "tnLagIndex"),
    (0, "TN-LAG-MIB", "tnLagSubgroup"),
)
if mibBuilder.loadTexts:
    tnLagCommandEntry.setStatus("current")


class _TnLagSubgroup_Type(LAGSubgroup):
    """Custom type tnLagSubgroup based on LAGSubgroup"""
    defaultValue = 1


_TnLagSubgroup_Type.__name__ = "LAGSubgroup"
_TnLagSubgroup_Object = MibTableColumn
tnLagSubgroup = _TnLagSubgroup_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 15, 20, 1, 1),
    _TnLagSubgroup_Type()
)
tnLagSubgroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnLagSubgroup.setStatus("current")


class _TnLagCommand_Type(Integer32):
    """Custom type tnLagCommand based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noCmd", 0),
          ("clearForce", 1),
          ("force", 2))
    )


_TnLagCommand_Type.__name__ = "Integer32"
_TnLagCommand_Object = MibTableColumn
tnLagCommand = _TnLagCommand_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 15, 20, 1, 2),
    _TnLagCommand_Type()
)
tnLagCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLagCommand.setStatus("current")


class _TnLagCommandActiveStdby_Type(Integer32):
    """Custom type tnLagCommandActiveStdby based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 2))
    )


_TnLagCommandActiveStdby_Type.__name__ = "Integer32"
_TnLagCommandActiveStdby_Object = MibTableColumn
tnLagCommandActiveStdby = _TnLagCommandActiveStdby_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 15, 20, 1, 3),
    _TnLagCommandActiveStdby_Type()
)
tnLagCommandActiveStdby.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLagCommandActiveStdby.setStatus("current")


class _TnLagCommandAllMc_Type(TruthValue):
    """Custom type tnLagCommandAllMc based on TruthValue"""
    defaultValue = 2


_TnLagCommandAllMc_Type.__name__ = "TruthValue"
_TnLagCommandAllMc_Object = MibTableColumn
tnLagCommandAllMc = _TnLagCommandAllMc_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 15, 20, 1, 4),
    _TnLagCommandAllMc_Type()
)
tnLagCommandAllMc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLagCommandAllMc.setStatus("current")


class _TnLagCommandMcPeerIpType_Type(InetAddressType):
    """Custom type tnLagCommandMcPeerIpType based on InetAddressType"""
    defaultValue = 1


_TnLagCommandMcPeerIpType_Type.__name__ = "InetAddressType"
_TnLagCommandMcPeerIpType_Object = MibTableColumn
tnLagCommandMcPeerIpType = _TnLagCommandMcPeerIpType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 15, 20, 1, 5),
    _TnLagCommandMcPeerIpType_Type()
)
tnLagCommandMcPeerIpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLagCommandMcPeerIpType.setStatus("current")


class _TnLagCommandMcPeerIpAddr_Type(InetAddress):
    """Custom type tnLagCommandMcPeerIpAddr based on InetAddress"""
    defaultValue = OctetString("")

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TnLagCommandMcPeerIpAddr_Type.__name__ = "InetAddress"
_TnLagCommandMcPeerIpAddr_Object = MibTableColumn
tnLagCommandMcPeerIpAddr = _TnLagCommandMcPeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 15, 20, 1, 6),
    _TnLagCommandMcPeerIpAddr_Type()
)
tnLagCommandMcPeerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLagCommandMcPeerIpAddr.setStatus("current")
_TnLagScalar2_Type = Unsigned32
_TnLagScalar2_Object = MibScalar
tnLagScalar2 = _TnLagScalar2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 15, 101),
    _TnLagScalar2_Type()
)
tnLagScalar2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLagScalar2.setStatus("current")
_TnLagScalar3_Type = Unsigned32
_TnLagScalar3_Object = MibScalar
tnLagScalar3 = _TnLagScalar3_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 15, 102),
    _TnLagScalar3_Type()
)
tnLagScalar3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLagScalar3.setStatus("current")
_TnLagNotifyPrefix_ObjectIdentity = ObjectIdentity
tnLagNotifyPrefix = _TnLagNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 15)
)
_TnLagNotifications_ObjectIdentity = ObjectIdentity
tnLagNotifications = _TnLagNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 15, 0)
)
tnLagConfigEntry.registerAugmentions(
    ("TN-LAG-MIB",
     "tnLagOperationEntry")
)
tnLagOperationEntry.setIndexNames(*tnLagConfigEntry.getIndexNames())
dot3adAggPortEntry.registerAugmentions(
    ("TN-LAG-MIB",
     "tnLagPortEntry")
)
tnLagPortEntry.setIndexNames(*dot3adAggPortEntry.getIndexNames())
tnLagConfigEntry.registerAugmentions(
    ("TN-LAG-MIB",
     "tnLagConfigXEntry")
)
tnLagConfigXEntry.setIndexNames(*tnLagConfigEntry.getIndexNames())

# Managed Objects groups


# Notification objects

tnLagDynamicCostOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 15, 0, 1)
)
tnLagDynamicCostOn.setObjects(
    ("TN-LAG-MIB", "tnLagPortThreshold")
)
if mibBuilder.loadTexts:
    tnLagDynamicCostOn.setStatus(
        "current"
    )

tnLagDynamicCostOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 15, 0, 2)
)
tnLagDynamicCostOff.setObjects(
    ("TN-LAG-MIB", "tnLagPortThreshold")
)
if mibBuilder.loadTexts:
    tnLagDynamicCostOff.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-LAG-MIB",
    **{"LAGInterfaceNumber": LAGInterfaceNumber,
       "LAGSubgroup": LAGSubgroup,
       "tnLagMIBModule": tnLagMIBModule,
       "tnLagObjects": tnLagObjects,
       "tnLagConfigTable": tnLagConfigTable,
       "tnLagConfigEntry": tnLagConfigEntry,
       "tnLagIndex": tnLagIndex,
       "tnLagRowStatus": tnLagRowStatus,
       "tnLagPortThreshold": tnLagPortThreshold,
       "tnLagPortThresholdAction": tnLagPortThresholdAction,
       "tnLagEnableMarkerGenerator": tnLagEnableMarkerGenerator,
       "tnLagEnableLACP": tnLagEnableLACP,
       "tnLagDescription": tnLagDescription,
       "tnLagDynamicCosting": tnLagDynamicCosting,
       "tnLagLACPMode": tnLagLACPMode,
       "tnLagLACPAdminKeyAutogen": tnLagLACPAdminKeyAutogen,
       "tnLagLACPTransmitInterval": tnLagLACPTransmitInterval,
       "tnLagAccessAdaptQos": tnLagAccessAdaptQos,
       "tnLagLACPXmitStdby": tnLagLACPXmitStdby,
       "tnLagLACPSelCrit": tnLagLACPSelCrit,
       "tnLagLACPSelCritSlaveToPartner": tnLagLACPSelCritSlaveToPartner,
       "tnLagLACPNbrOfSubGroups": tnLagLACPNbrOfSubGroups,
       "tnLagholdTimeDown": tnLagholdTimeDown,
       "tnLagPortType": tnLagPortType,
       "tnLagPerFpIngQueuing": tnLagPerFpIngQueuing,
       "tnLagOperationTable": tnLagOperationTable,
       "tnLagOperationEntry": tnLagOperationEntry,
       "tnLagIfIndex": tnLagIfIndex,
       "tnLagConfigLastChange": tnLagConfigLastChange,
       "tnLagPortThresholdFalling": tnLagPortThresholdFalling,
       "tnLagPortThresholdRising": tnLagPortThresholdRising,
       "tnLagScalar1": tnLagScalar1,
       "tnLagMemberTable": tnLagMemberTable,
       "tnLagMemberEntry": tnLagMemberEntry,
       "tnLagMemberPortName": tnLagMemberPortName,
       "tnLagMemberPortIsPrimary": tnLagMemberPortIsPrimary,
       "tnLagPortTable": tnLagPortTable,
       "tnLagPortEntry": tnLagPortEntry,
       "tnLagPortSubgroup": tnLagPortSubgroup,
       "tnLagPortActiveStdby": tnLagPortActiveStdby,
       "tnLagConfigXTable": tnLagConfigXTable,
       "tnLagConfigXEntry": tnLagConfigXEntry,
       "tnLagConfigXIngressAvailBandwidth": tnLagConfigXIngressAvailBandwidth,
       "tnLagConfigXEgressAvailBandwidth": tnLagConfigXEgressAvailBandwidth,
       "tnLagConfigXMaxPortSize": tnLagConfigXMaxPortSize,
       "tnLagConfigXNumSelectedPorts": tnLagConfigXNumSelectedPorts,
       "tnLagConfigXNumAttachedPorts": tnLagConfigXNumAttachedPorts,
       "tnLagConfigXPrimaryPort": tnLagConfigXPrimaryPort,
       "tnLagAdminState": tnLagAdminState,
       "tnLagLPTConsequenceAction": tnLagLPTConsequenceAction,
       "tnLagLosProp": tnLagLosProp,
       "tnLagTPID": tnLagTPID,
       "tnLagMtu": tnLagMtu,
       "tnLagSpeed": tnLagSpeed,
       "tnLagCommandTable": tnLagCommandTable,
       "tnLagCommandEntry": tnLagCommandEntry,
       "tnLagSubgroup": tnLagSubgroup,
       "tnLagCommand": tnLagCommand,
       "tnLagCommandActiveStdby": tnLagCommandActiveStdby,
       "tnLagCommandAllMc": tnLagCommandAllMc,
       "tnLagCommandMcPeerIpType": tnLagCommandMcPeerIpType,
       "tnLagCommandMcPeerIpAddr": tnLagCommandMcPeerIpAddr,
       "tnLagScalar2": tnLagScalar2,
       "tnLagScalar3": tnLagScalar3,
       "tnLagNotifyPrefix": tnLagNotifyPrefix,
       "tnLagNotifications": tnLagNotifications,
       "tnLagDynamicCostOn": tnLagDynamicCostOn,
       "tnLagDynamicCostOff": tnLagDynamicCostOff}
)
