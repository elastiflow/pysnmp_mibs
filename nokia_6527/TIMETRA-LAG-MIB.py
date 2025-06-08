# SNMP MIB module (TIMETRA-LAG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-LAG-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:44:24 2025
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(tmnxPortLagId,
 tmnxPortPortID) = mibBuilder.importSymbols(
    "TIMETRA-PORT-MIB",
    "tmnxPortLagId",
    "tmnxPortPortID")

(TItemDescription,
 TItemLongDescription,
 TNamedItemOrEmpty,
 TQosIngressPolicyID,
 TmnxActionType,
 TmnxEnabledDisabled,
 TmnxLagPerLinkHashClass,
 TmnxLagPerLinkHashClassOrNone,
 TmnxLinkMapProfileId,
 TmnxPortID) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TItemDescription",
    "TItemLongDescription",
    "TNamedItemOrEmpty",
    "TQosIngressPolicyID",
    "TmnxActionType",
    "TmnxEnabledDisabled",
    "TmnxLagPerLinkHashClass",
    "TmnxLagPerLinkHashClassOrNone",
    "TmnxLinkMapProfileId",
    "TmnxPortID")


# MODULE-IDENTITY

timetraLagMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 15)
)
if mibBuilder.loadTexts:
    timetraLagMIBModule.setRevisions(
        ("2014-01-01 00:00",
         "2012-04-11 00:00",
         "2012-04-06 00:00",
         "2011-02-01 00:00",
         "2009-02-28 00:00",
         "2008-07-01 00:00",
         "2008-01-01 00:00",
         "2007-01-01 00:00",
         "2006-03-15 00:00",
         "2005-08-31 00:00",
         "2005-01-24 00:00",
         "2004-01-15 00:00",
         "2003-08-15 00:00",
         "2003-01-20 00:00",
         "2001-02-09 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class LAGInterfaceNumber(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
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

_TmnxLagConformance_ObjectIdentity = ObjectIdentity
tmnxLagConformance = _TmnxLagConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15)
)
_TmnxLagCompliances_ObjectIdentity = ObjectIdentity
tmnxLagCompliances = _TmnxLagCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 1)
)
_TmnxLagGroups_ObjectIdentity = ObjectIdentity
tmnxLagGroups = _TmnxLagGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 2)
)
_TmnxLagDCCompliances_ObjectIdentity = ObjectIdentity
tmnxLagDCCompliances = _TmnxLagDCCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 3)
)
_TmnxLagDCGroups_ObjectIdentity = ObjectIdentity
tmnxLagDCGroups = _TmnxLagDCGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 4)
)
_TLagObjects_ObjectIdentity = ObjectIdentity
tLagObjects = _TLagObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15)
)
_TLagConfigTable_Object = MibTable
tLagConfigTable = _TLagConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 2)
)
if mibBuilder.loadTexts:
    tLagConfigTable.setStatus("current")
_TLagConfigEntry_Object = MibTableRow
tLagConfigEntry = _TLagConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 2, 1)
)
tLagConfigEntry.setIndexNames(
    (0, "TIMETRA-LAG-MIB", "tLagIndex"),
)
if mibBuilder.loadTexts:
    tLagConfigEntry.setStatus("current")
_TLagIndex_Type = LAGInterfaceNumber
_TLagIndex_Object = MibTableColumn
tLagIndex = _TLagIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 2, 1, 1),
    _TLagIndex_Type()
)
tLagIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tLagIndex.setStatus("current")
_TLagRowStatus_Type = RowStatus
_TLagRowStatus_Object = MibTableColumn
tLagRowStatus = _TLagRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 2, 1, 2),
    _TLagRowStatus_Type()
)
tLagRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLagRowStatus.setStatus("current")


class _TLagPortThreshold_Type(Integer32):
    """Custom type tLagPortThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_TLagPortThreshold_Type.__name__ = "Integer32"
_TLagPortThreshold_Object = MibTableColumn
tLagPortThreshold = _TLagPortThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 2, 1, 3),
    _TLagPortThreshold_Type()
)
tLagPortThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLagPortThreshold.setStatus("current")


class _TLagPortThresholdAction_Type(Integer32):
    """Custom type tLagPortThresholdAction based on Integer32"""
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


_TLagPortThresholdAction_Type.__name__ = "Integer32"
_TLagPortThresholdAction_Object = MibTableColumn
tLagPortThresholdAction = _TLagPortThresholdAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 2, 1, 4),
    _TLagPortThresholdAction_Type()
)
tLagPortThresholdAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLagPortThresholdAction.setStatus("current")


class _TLagEnableMarkerGenerator_Type(TruthValue):
    """Custom type tLagEnableMarkerGenerator based on TruthValue"""
    defaultValue = 2


_TLagEnableMarkerGenerator_Type.__name__ = "TruthValue"
_TLagEnableMarkerGenerator_Object = MibTableColumn
tLagEnableMarkerGenerator = _TLagEnableMarkerGenerator_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 2, 1, 5),
    _TLagEnableMarkerGenerator_Type()
)
tLagEnableMarkerGenerator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLagEnableMarkerGenerator.setStatus("current")


class _TLagEnableLACP_Type(TruthValue):
    """Custom type tLagEnableLACP based on TruthValue"""
    defaultValue = 2


_TLagEnableLACP_Type.__name__ = "TruthValue"
_TLagEnableLACP_Object = MibTableColumn
tLagEnableLACP = _TLagEnableLACP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 2, 1, 6),
    _TLagEnableLACP_Type()
)
tLagEnableLACP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLagEnableLACP.setStatus("current")


class _TLagDescription_Type(TItemLongDescription):
    """Custom type tLagDescription based on TItemLongDescription"""
    defaultHexValue = ""


_TLagDescription_Type.__name__ = "TItemLongDescription"
_TLagDescription_Object = MibTableColumn
tLagDescription = _TLagDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 2, 1, 7),
    _TLagDescription_Type()
)
tLagDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLagDescription.setStatus("current")


class _TLagDynamicCosting_Type(TruthValue):
    """Custom type tLagDynamicCosting based on TruthValue"""
    defaultValue = 2


_TLagDynamicCosting_Type.__name__ = "TruthValue"
_TLagDynamicCosting_Object = MibTableColumn
tLagDynamicCosting = _TLagDynamicCosting_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 2, 1, 8),
    _TLagDynamicCosting_Type()
)
tLagDynamicCosting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLagDynamicCosting.setStatus("current")


class _TLagLACPMode_Type(Integer32):
    """Custom type tLagLACPMode based on Integer32"""
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


_TLagLACPMode_Type.__name__ = "Integer32"
_TLagLACPMode_Object = MibTableColumn
tLagLACPMode = _TLagLACPMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 2, 1, 9),
    _TLagLACPMode_Type()
)
tLagLACPMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLagLACPMode.setStatus("current")


class _TLagLACPAdminKeyAutogen_Type(TruthValue):
    """Custom type tLagLACPAdminKeyAutogen based on TruthValue"""
    defaultValue = 1


_TLagLACPAdminKeyAutogen_Type.__name__ = "TruthValue"
_TLagLACPAdminKeyAutogen_Object = MibTableColumn
tLagLACPAdminKeyAutogen = _TLagLACPAdminKeyAutogen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 2, 1, 10),
    _TLagLACPAdminKeyAutogen_Type()
)
tLagLACPAdminKeyAutogen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLagLACPAdminKeyAutogen.setStatus("current")


class _TLagLACPTransmitInterval_Type(Integer32):
    """Custom type tLagLACPTransmitInterval based on Integer32"""
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


_TLagLACPTransmitInterval_Type.__name__ = "Integer32"
_TLagLACPTransmitInterval_Object = MibTableColumn
tLagLACPTransmitInterval = _TLagLACPTransmitInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 2, 1, 11),
    _TLagLACPTransmitInterval_Type()
)
tLagLACPTransmitInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLagLACPTransmitInterval.setStatus("current")


class _TLagAccessAdaptQos_Type(Integer32):
    """Custom type tLagAccessAdaptQos based on Integer32"""
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
        *(("link", 1),
          ("distribute", 2),
          ("portFair", 3))
    )


_TLagAccessAdaptQos_Type.__name__ = "Integer32"
_TLagAccessAdaptQos_Object = MibTableColumn
tLagAccessAdaptQos = _TLagAccessAdaptQos_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 2, 1, 12),
    _TLagAccessAdaptQos_Type()
)
tLagAccessAdaptQos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLagAccessAdaptQos.setStatus("current")


class _TLagLACPXmitStdby_Type(TruthValue):
    """Custom type tLagLACPXmitStdby based on TruthValue"""
    defaultValue = 1


_TLagLACPXmitStdby_Type.__name__ = "TruthValue"
_TLagLACPXmitStdby_Object = MibTableColumn
tLagLACPXmitStdby = _TLagLACPXmitStdby_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 2, 1, 13),
    _TLagLACPXmitStdby_Type()
)
tLagLACPXmitStdby.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLagLACPXmitStdby.setStatus("current")


class _TLagLACPSelCrit_Type(Integer32):
    """Custom type tLagLACPSelCrit based on Integer32"""
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
        *(("highestCount", 1),
          ("highestWeight", 2),
          ("bestPort", 3))
    )


_TLagLACPSelCrit_Type.__name__ = "Integer32"
_TLagLACPSelCrit_Object = MibTableColumn
tLagLACPSelCrit = _TLagLACPSelCrit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 2, 1, 14),
    _TLagLACPSelCrit_Type()
)
tLagLACPSelCrit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLagLACPSelCrit.setStatus("current")


class _TLagLACPSelCritSlaveToPartner_Type(TruthValue):
    """Custom type tLagLACPSelCritSlaveToPartner based on TruthValue"""
    defaultValue = 2


_TLagLACPSelCritSlaveToPartner_Type.__name__ = "TruthValue"
_TLagLACPSelCritSlaveToPartner_Object = MibTableColumn
tLagLACPSelCritSlaveToPartner = _TLagLACPSelCritSlaveToPartner_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 2, 1, 15),
    _TLagLACPSelCritSlaveToPartner_Type()
)
tLagLACPSelCritSlaveToPartner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLagLACPSelCritSlaveToPartner.setStatus("current")
_TLagLACPNbrOfSubGroups_Type = Unsigned32
_TLagLACPNbrOfSubGroups_Object = MibTableColumn
tLagLACPNbrOfSubGroups = _TLagLACPNbrOfSubGroups_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 2, 1, 16),
    _TLagLACPNbrOfSubGroups_Type()
)
tLagLACPNbrOfSubGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLagLACPNbrOfSubGroups.setStatus("current")


class _TLagholdTimeDown_Type(Unsigned32):
    """Custom type tLagholdTimeDown based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_TLagholdTimeDown_Type.__name__ = "Unsigned32"
_TLagholdTimeDown_Object = MibTableColumn
tLagholdTimeDown = _TLagholdTimeDown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 2, 1, 17),
    _TLagholdTimeDown_Type()
)
tLagholdTimeDown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLagholdTimeDown.setStatus("current")
if mibBuilder.loadTexts:
    tLagholdTimeDown.setUnits("100s of milliseconds")


class _TLagPortType_Type(Integer32):
    """Custom type tLagPortType based on Integer32"""
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
        *(("standard", 1),
          ("hsmda", 2),
          ("hsmdaV2", 3))
    )


_TLagPortType_Type.__name__ = "Integer32"
_TLagPortType_Object = MibTableColumn
tLagPortType = _TLagPortType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 2, 1, 18),
    _TLagPortType_Type()
)
tLagPortType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLagPortType.setStatus("current")


class _TLagPerFpIngQueuing_Type(TruthValue):
    """Custom type tLagPerFpIngQueuing based on TruthValue"""
    defaultValue = 2


_TLagPerFpIngQueuing_Type.__name__ = "TruthValue"
_TLagPerFpIngQueuing_Object = MibTableColumn
tLagPerFpIngQueuing = _TLagPerFpIngQueuing_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 2, 1, 19),
    _TLagPerFpIngQueuing_Type()
)
tLagPerFpIngQueuing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLagPerFpIngQueuing.setStatus("current")


class _TLagSystemId_Type(MacAddress):
    """Custom type tLagSystemId based on MacAddress"""
    defaultHexValue = "000000000000"


_TLagSystemId_Type.__name__ = "MacAddress"
_TLagSystemId_Object = MibTableColumn
tLagSystemId = _TLagSystemId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 2, 1, 20),
    _TLagSystemId_Type()
)
tLagSystemId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLagSystemId.setStatus("current")


class _TLagSystemPriority_Type(Integer32):
    """Custom type tLagSystemPriority based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )


_TLagSystemPriority_Type.__name__ = "Integer32"
_TLagSystemPriority_Object = MibTableColumn
tLagSystemPriority = _TLagSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 2, 1, 21),
    _TLagSystemPriority_Type()
)
tLagSystemPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLagSystemPriority.setStatus("current")


class _TLagStandbySignaling_Type(Integer32):
    """Custom type tLagStandbySignaling based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lacp", 1),
          ("powerOff", 2))
    )


_TLagStandbySignaling_Type.__name__ = "Integer32"
_TLagStandbySignaling_Object = MibTableColumn
tLagStandbySignaling = _TLagStandbySignaling_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 2, 1, 22),
    _TLagStandbySignaling_Type()
)
tLagStandbySignaling.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLagStandbySignaling.setStatus("current")


class _TLagPerLinkHash_Type(TruthValue):
    """Custom type tLagPerLinkHash based on TruthValue"""
    defaultValue = 2


_TLagPerLinkHash_Type.__name__ = "TruthValue"
_TLagPerLinkHash_Object = MibTableColumn
tLagPerLinkHash = _TLagPerLinkHash_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 2, 1, 23),
    _TLagPerLinkHash_Type()
)
tLagPerLinkHash.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLagPerLinkHash.setStatus("current")


class _TLagPerFpEgrQueuing_Type(TruthValue):
    """Custom type tLagPerFpEgrQueuing based on TruthValue"""
    defaultValue = 2


_TLagPerFpEgrQueuing_Type.__name__ = "TruthValue"
_TLagPerFpEgrQueuing_Object = MibTableColumn
tLagPerFpEgrQueuing = _TLagPerFpEgrQueuing_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 2, 1, 24),
    _TLagPerFpEgrQueuing_Type()
)
tLagPerFpEgrQueuing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLagPerFpEgrQueuing.setStatus("current")


class _TLagIncludeEgrHashCfg_Type(TruthValue):
    """Custom type tLagIncludeEgrHashCfg based on TruthValue"""
    defaultValue = 2


_TLagIncludeEgrHashCfg_Type.__name__ = "TruthValue"
_TLagIncludeEgrHashCfg_Object = MibTableColumn
tLagIncludeEgrHashCfg = _TLagIncludeEgrHashCfg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 2, 1, 25),
    _TLagIncludeEgrHashCfg_Type()
)
tLagIncludeEgrHashCfg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLagIncludeEgrHashCfg.setStatus("current")


class _TLagPerFpSapInstance_Type(TruthValue):
    """Custom type tLagPerFpSapInstance based on TruthValue"""
    defaultValue = 2


_TLagPerFpSapInstance_Type.__name__ = "TruthValue"
_TLagPerFpSapInstance_Object = MibTableColumn
tLagPerFpSapInstance = _TLagPerFpSapInstance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 2, 1, 26),
    _TLagPerFpSapInstance_Type()
)
tLagPerFpSapInstance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLagPerFpSapInstance.setStatus("current")


class _TLagLacpHoldTime_Type(Unsigned32):
    """Custom type tLagLacpHoldTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_TLagLacpHoldTime_Type.__name__ = "Unsigned32"
_TLagLacpHoldTime_Object = MibTableColumn
tLagLacpHoldTime = _TLagLacpHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 2, 1, 27),
    _TLagLacpHoldTime_Type()
)
tLagLacpHoldTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLagLacpHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    tLagLacpHoldTime.setUnits("100s of milliseconds")


class _TLagPerLinkHashWeighted_Type(TruthValue):
    """Custom type tLagPerLinkHashWeighted based on TruthValue"""
    defaultValue = 2


_TLagPerLinkHashWeighted_Type.__name__ = "TruthValue"
_TLagPerLinkHashWeighted_Object = MibTableColumn
tLagPerLinkHashWeighted = _TLagPerLinkHashWeighted_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 2, 1, 29),
    _TLagPerLinkHashWeighted_Type()
)
tLagPerLinkHashWeighted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLagPerLinkHashWeighted.setStatus("current")


class _TLagPerLinkHashWeightedRebalance_Type(TruthValue):
    """Custom type tLagPerLinkHashWeightedRebalance based on TruthValue"""
    defaultValue = 2


_TLagPerLinkHashWeightedRebalance_Type.__name__ = "TruthValue"
_TLagPerLinkHashWeightedRebalance_Object = MibTableColumn
tLagPerLinkHashWeightedRebalance = _TLagPerLinkHashWeightedRebalance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 2, 1, 30),
    _TLagPerLinkHashWeightedRebalance_Type()
)
tLagPerLinkHashWeightedRebalance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLagPerLinkHashWeightedRebalance.setStatus("current")


class _TLagPortWeightSpeed_Type(Unsigned32):
    """Custom type tLagPortWeightSpeed based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(10, 10),
    )


_TLagPortWeightSpeed_Type.__name__ = "Unsigned32"
_TLagPortWeightSpeed_Object = MibTableColumn
tLagPortWeightSpeed = _TLagPortWeightSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 2, 1, 31),
    _TLagPortWeightSpeed_Type()
)
tLagPortWeightSpeed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLagPortWeightSpeed.setStatus("current")
if mibBuilder.loadTexts:
    tLagPortWeightSpeed.setUnits("gbps")


class _TLagWeightThreshold_Type(Integer32):
    """Custom type tLagWeightThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_TLagWeightThreshold_Type.__name__ = "Integer32"
_TLagWeightThreshold_Object = MibTableColumn
tLagWeightThreshold = _TLagWeightThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 2, 1, 33),
    _TLagWeightThreshold_Type()
)
tLagWeightThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLagWeightThreshold.setStatus("current")


class _TLagWeightThresholdAction_Type(Integer32):
    """Custom type tLagWeightThresholdAction based on Integer32"""
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


_TLagWeightThresholdAction_Type.__name__ = "Integer32"
_TLagWeightThresholdAction_Object = MibTableColumn
tLagWeightThresholdAction = _TLagWeightThresholdAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 2, 1, 34),
    _TLagWeightThresholdAction_Type()
)
tLagWeightThresholdAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLagWeightThresholdAction.setStatus("current")
_TLagOperationTable_Object = MibTable
tLagOperationTable = _TLagOperationTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 3)
)
if mibBuilder.loadTexts:
    tLagOperationTable.setStatus("current")
_TLagOperationEntry_Object = MibTableRow
tLagOperationEntry = _TLagOperationEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 3, 1)
)
if mibBuilder.loadTexts:
    tLagOperationEntry.setStatus("current")
_TLagIfIndex_Type = InterfaceIndexOrZero
_TLagIfIndex_Object = MibTableColumn
tLagIfIndex = _TLagIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 3, 1, 1),
    _TLagIfIndex_Type()
)
tLagIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLagIfIndex.setStatus("current")
_TLagConfigLastChange_Type = TimeStamp
_TLagConfigLastChange_Object = MibTableColumn
tLagConfigLastChange = _TLagConfigLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 3, 1, 2),
    _TLagConfigLastChange_Type()
)
tLagConfigLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLagConfigLastChange.setStatus("current")
_TLagPortThresholdFalling_Type = Counter32
_TLagPortThresholdFalling_Object = MibTableColumn
tLagPortThresholdFalling = _TLagPortThresholdFalling_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 3, 1, 3),
    _TLagPortThresholdFalling_Type()
)
tLagPortThresholdFalling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLagPortThresholdFalling.setStatus("current")
_TLagPortThresholdRising_Type = Counter32
_TLagPortThresholdRising_Object = MibTableColumn
tLagPortThresholdRising = _TLagPortThresholdRising_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 3, 1, 4),
    _TLagPortThresholdRising_Type()
)
tLagPortThresholdRising.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLagPortThresholdRising.setStatus("current")
_TLagLACPPrimaryPort_Type = TmnxPortID
_TLagLACPPrimaryPort_Object = MibTableColumn
tLagLACPPrimaryPort = _TLagLACPPrimaryPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 3, 1, 5),
    _TLagLACPPrimaryPort_Type()
)
tLagLACPPrimaryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLagLACPPrimaryPort.setStatus("obsolete")


class _TLagPortReasonDownFlags_Type(Bits):
    """Custom type tLagPortReasonDownFlags based on Bits"""
    namedValues = NamedValues(
        *(("unknown", 0),
          ("linklossFwd", 1))
    )

_TLagPortReasonDownFlags_Type.__name__ = "Bits"
_TLagPortReasonDownFlags_Object = MibTableColumn
tLagPortReasonDownFlags = _TLagPortReasonDownFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 3, 1, 6),
    _TLagPortReasonDownFlags_Type()
)
tLagPortReasonDownFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLagPortReasonDownFlags.setStatus("obsolete")
_TLagSelectedSubGroup_Type = Integer32
_TLagSelectedSubGroup_Object = MibTableColumn
tLagSelectedSubGroup = _TLagSelectedSubGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 3, 1, 7),
    _TLagSelectedSubGroup_Type()
)
tLagSelectedSubGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLagSelectedSubGroup.setStatus("current")
_TLagCandidateSubGroup_Type = Integer32
_TLagCandidateSubGroup_Object = MibTableColumn
tLagCandidateSubGroup = _TLagCandidateSubGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 3, 1, 8),
    _TLagCandidateSubGroup_Type()
)
tLagCandidateSubGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLagCandidateSubGroup.setStatus("current")
_TLagRemainingHoldTime_Type = Unsigned32
_TLagRemainingHoldTime_Object = MibTableColumn
tLagRemainingHoldTime = _TLagRemainingHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 3, 1, 9),
    _TLagRemainingHoldTime_Type()
)
tLagRemainingHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLagRemainingHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    tLagRemainingHoldTime.setUnits("100s of milliseconds")
_TLagPortWeightUp_Type = Gauge32
_TLagPortWeightUp_Object = MibTableColumn
tLagPortWeightUp = _TLagPortWeightUp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 3, 1, 10),
    _TLagPortWeightUp_Type()
)
tLagPortWeightUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLagPortWeightUp.setStatus("current")
_TLagNotificationObjects_ObjectIdentity = ObjectIdentity
tLagNotificationObjects = _TLagNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 4)
)


class _TLagNotifyPortAddFailReason_Type(Integer32):
    """Custom type tLagNotifyPortAddFailReason based on Integer32"""
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
        *(("unknown", 0),
          ("adminkey-mismatch", 1),
          ("sysid-mismatch", 2),
          ("lacp-passive-both-ends", 3),
          ("link-down", 4))
    )


_TLagNotifyPortAddFailReason_Type.__name__ = "Integer32"
_TLagNotifyPortAddFailReason_Object = MibScalar
tLagNotifyPortAddFailReason = _TLagNotifyPortAddFailReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 4, 1),
    _TLagNotifyPortAddFailReason_Type()
)
tLagNotifyPortAddFailReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tLagNotifyPortAddFailReason.setStatus("current")
_TLagNotifySubGroupSelected_Type = DisplayString
_TLagNotifySubGroupSelected_Object = MibScalar
tLagNotifySubGroupSelected = _TLagNotifySubGroupSelected_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 4, 2),
    _TLagNotifySubGroupSelected_Type()
)
tLagNotifySubGroupSelected.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tLagNotifySubGroupSelected.setStatus("current")
_TLagNotifyAdditionalInfo_Type = DisplayString
_TLagNotifyAdditionalInfo_Object = MibScalar
tLagNotifyAdditionalInfo = _TLagNotifyAdditionalInfo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 4, 3),
    _TLagNotifyAdditionalInfo_Type()
)
tLagNotifyAdditionalInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tLagNotifyAdditionalInfo.setStatus("current")


class _TLagNotifyStateChangedReason_Type(Integer32):
    """Custom type tLagNotifyStateChangedReason based on Integer32"""
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
        *(("partner-oper-state-changed", 1),
          ("lacp-expired", 2),
          ("lacp-rx-state-machine", 3),
          ("efm-oam-state-changed", 4),
          ("dot1ag-state-changed", 5),
          ("bfd-state-changed", 6))
    )


_TLagNotifyStateChangedReason_Type.__name__ = "Integer32"
_TLagNotifyStateChangedReason_Object = MibScalar
tLagNotifyStateChangedReason = _TLagNotifyStateChangedReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 4, 4),
    _TLagNotifyStateChangedReason_Type()
)
tLagNotifyStateChangedReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tLagNotifyStateChangedReason.setStatus("current")
_TLagMemberTable_Object = MibTable
tLagMemberTable = _TLagMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 5)
)
if mibBuilder.loadTexts:
    tLagMemberTable.setStatus("current")
_TLagMemberEntry_Object = MibTableRow
tLagMemberEntry = _TLagMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 5, 1)
)
tLagMemberEntry.setIndexNames(
    (0, "TIMETRA-LAG-MIB", "tLagIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    tLagMemberEntry.setStatus("current")
_TLagMemberPortName_Type = TNamedItemOrEmpty
_TLagMemberPortName_Object = MibTableColumn
tLagMemberPortName = _TLagMemberPortName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 5, 1, 1),
    _TLagMemberPortName_Type()
)
tLagMemberPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLagMemberPortName.setStatus("current")
_TLagMemberPortIsPrimary_Type = TruthValue
_TLagMemberPortIsPrimary_Object = MibTableColumn
tLagMemberPortIsPrimary = _TLagMemberPortIsPrimary_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 5, 1, 2),
    _TLagMemberPortIsPrimary_Type()
)
tLagMemberPortIsPrimary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLagMemberPortIsPrimary.setStatus("current")
_TLagPortTable_Object = MibTable
tLagPortTable = _TLagPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 6)
)
if mibBuilder.loadTexts:
    tLagPortTable.setStatus("current")
_TLagPortEntry_Object = MibTableRow
tLagPortEntry = _TLagPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 6, 1)
)
if mibBuilder.loadTexts:
    tLagPortEntry.setStatus("current")


class _TLagPortSubgroup_Type(LAGSubgroup):
    """Custom type tLagPortSubgroup based on LAGSubgroup"""
    defaultValue = 1


_TLagPortSubgroup_Type.__name__ = "LAGSubgroup"
_TLagPortSubgroup_Object = MibTableColumn
tLagPortSubgroup = _TLagPortSubgroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 6, 1, 1),
    _TLagPortSubgroup_Type()
)
tLagPortSubgroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tLagPortSubgroup.setStatus("current")


class _TLagPortActiveStdby_Type(Integer32):
    """Custom type tLagPortActiveStdby based on Integer32"""
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


_TLagPortActiveStdby_Type.__name__ = "Integer32"
_TLagPortActiveStdby_Object = MibTableColumn
tLagPortActiveStdby = _TLagPortActiveStdby_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 6, 1, 2),
    _TLagPortActiveStdby_Type()
)
tLagPortActiveStdby.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLagPortActiveStdby.setStatus("current")
_TLagLinkMapProfileTableLastChgd_Type = TimeStamp
_TLagLinkMapProfileTableLastChgd_Object = MibScalar
tLagLinkMapProfileTableLastChgd = _TLagLinkMapProfileTableLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 7),
    _TLagLinkMapProfileTableLastChgd_Type()
)
tLagLinkMapProfileTableLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLagLinkMapProfileTableLastChgd.setStatus("current")
_TLagLinkMapProfileTable_Object = MibTable
tLagLinkMapProfileTable = _TLagLinkMapProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 8)
)
if mibBuilder.loadTexts:
    tLagLinkMapProfileTable.setStatus("current")
_TLagLinkMapProfileEntry_Object = MibTableRow
tLagLinkMapProfileEntry = _TLagLinkMapProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 8, 1)
)
tLagLinkMapProfileEntry.setIndexNames(
    (0, "TIMETRA-LAG-MIB", "tLagIndex"),
    (0, "TIMETRA-LAG-MIB", "tLagLinkMapProfileId"),
)
if mibBuilder.loadTexts:
    tLagLinkMapProfileEntry.setStatus("current")
_TLagLinkMapProfileId_Type = TmnxLinkMapProfileId
_TLagLinkMapProfileId_Object = MibTableColumn
tLagLinkMapProfileId = _TLagLinkMapProfileId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 8, 1, 1),
    _TLagLinkMapProfileId_Type()
)
tLagLinkMapProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tLagLinkMapProfileId.setStatus("current")
_TLagLinkMapProfileRowStatus_Type = RowStatus
_TLagLinkMapProfileRowStatus_Object = MibTableColumn
tLagLinkMapProfileRowStatus = _TLagLinkMapProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 8, 1, 2),
    _TLagLinkMapProfileRowStatus_Type()
)
tLagLinkMapProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLagLinkMapProfileRowStatus.setStatus("current")
_TLagLinkMapProfileLastChanged_Type = TimeStamp
_TLagLinkMapProfileLastChanged_Object = MibTableColumn
tLagLinkMapProfileLastChanged = _TLagLinkMapProfileLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 8, 1, 3),
    _TLagLinkMapProfileLastChanged_Type()
)
tLagLinkMapProfileLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLagLinkMapProfileLastChanged.setStatus("current")


class _TLagLinkMapProfileDescription_Type(TItemDescription):
    """Custom type tLagLinkMapProfileDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TLagLinkMapProfileDescription_Type.__name__ = "TItemDescription"
_TLagLinkMapProfileDescription_Object = MibTableColumn
tLagLinkMapProfileDescription = _TLagLinkMapProfileDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 8, 1, 4),
    _TLagLinkMapProfileDescription_Type()
)
tLagLinkMapProfileDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLagLinkMapProfileDescription.setStatus("current")


class _TLagLinkMapProfileFailureMode_Type(Integer32):
    """Custom type tLagLinkMapProfileFailureMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("perLinkHash", 1),
          ("discard", 2))
    )


_TLagLinkMapProfileFailureMode_Type.__name__ = "Integer32"
_TLagLinkMapProfileFailureMode_Object = MibTableColumn
tLagLinkMapProfileFailureMode = _TLagLinkMapProfileFailureMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 8, 1, 5),
    _TLagLinkMapProfileFailureMode_Type()
)
tLagLinkMapProfileFailureMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLagLinkMapProfileFailureMode.setStatus("current")
_TLagLinkMapProfileActiveLink_Type = TmnxPortID
_TLagLinkMapProfileActiveLink_Object = MibTableColumn
tLagLinkMapProfileActiveLink = _TLagLinkMapProfileActiveLink_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 8, 1, 6),
    _TLagLinkMapProfileActiveLink_Type()
)
tLagLinkMapProfileActiveLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLagLinkMapProfileActiveLink.setStatus("current")
_TLagLinkMapProfPortTableLastChgd_Type = TimeStamp
_TLagLinkMapProfPortTableLastChgd_Object = MibScalar
tLagLinkMapProfPortTableLastChgd = _TLagLinkMapProfPortTableLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 9),
    _TLagLinkMapProfPortTableLastChgd_Type()
)
tLagLinkMapProfPortTableLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLagLinkMapProfPortTableLastChgd.setStatus("current")
_TLagLinkMapProfPortTable_Object = MibTable
tLagLinkMapProfPortTable = _TLagLinkMapProfPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 10)
)
if mibBuilder.loadTexts:
    tLagLinkMapProfPortTable.setStatus("current")
_TLagLinkMapProfPortEntry_Object = MibTableRow
tLagLinkMapProfPortEntry = _TLagLinkMapProfPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 10, 1)
)
tLagLinkMapProfPortEntry.setIndexNames(
    (0, "TIMETRA-LAG-MIB", "tLagIndex"),
    (0, "TIMETRA-LAG-MIB", "tLagLinkMapProfileId"),
    (0, "TIMETRA-LAG-MIB", "tLagLinkMapProfPortId"),
)
if mibBuilder.loadTexts:
    tLagLinkMapProfPortEntry.setStatus("current")
_TLagLinkMapProfPortId_Type = TmnxPortID
_TLagLinkMapProfPortId_Object = MibTableColumn
tLagLinkMapProfPortId = _TLagLinkMapProfPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 10, 1, 1),
    _TLagLinkMapProfPortId_Type()
)
tLagLinkMapProfPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tLagLinkMapProfPortId.setStatus("current")
_TLagLinkMapProfPortRowStatus_Type = RowStatus
_TLagLinkMapProfPortRowStatus_Object = MibTableColumn
tLagLinkMapProfPortRowStatus = _TLagLinkMapProfPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 10, 1, 2),
    _TLagLinkMapProfPortRowStatus_Type()
)
tLagLinkMapProfPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLagLinkMapProfPortRowStatus.setStatus("current")
_TLagLinkMapProfPortLastChanged_Type = TimeStamp
_TLagLinkMapProfPortLastChanged_Object = MibTableColumn
tLagLinkMapProfPortLastChanged = _TLagLinkMapProfPortLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 10, 1, 3),
    _TLagLinkMapProfPortLastChanged_Type()
)
tLagLinkMapProfPortLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLagLinkMapProfPortLastChanged.setStatus("current")


class _TLagLinkMapProfPortType_Type(Integer32):
    """Custom type tLagLinkMapProfPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_TLagLinkMapProfPortType_Type.__name__ = "Integer32"
_TLagLinkMapProfPortType_Object = MibTableColumn
tLagLinkMapProfPortType = _TLagLinkMapProfPortType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 10, 1, 4),
    _TLagLinkMapProfPortType_Type()
)
tLagLinkMapProfPortType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLagLinkMapProfPortType.setStatus("current")
_TLagPerLinkHashWtPortClassTable_Object = MibTable
tLagPerLinkHashWtPortClassTable = _TLagPerLinkHashWtPortClassTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 11)
)
if mibBuilder.loadTexts:
    tLagPerLinkHashWtPortClassTable.setStatus("current")
_TLagPerLinkHashWtPortClassEntry_Object = MibTableRow
tLagPerLinkHashWtPortClassEntry = _TLagPerLinkHashWtPortClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 11, 1)
)
tLagPerLinkHashWtPortClassEntry.setIndexNames(
    (0, "TIMETRA-LAG-MIB", "tLagIndex"),
    (0, "TIMETRA-LAG-MIB", "tLagPerLinkHashWtPort"),
    (0, "TIMETRA-LAG-MIB", "tLagPerLinkHashWtPortClassId"),
)
if mibBuilder.loadTexts:
    tLagPerLinkHashWtPortClassEntry.setStatus("current")
_TLagPerLinkHashWtPort_Type = TmnxPortID
_TLagPerLinkHashWtPort_Object = MibTableColumn
tLagPerLinkHashWtPort = _TLagPerLinkHashWtPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 11, 1, 1),
    _TLagPerLinkHashWtPort_Type()
)
tLagPerLinkHashWtPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLagPerLinkHashWtPort.setStatus("current")
_TLagPerLinkHashWtPortClassId_Type = TmnxLagPerLinkHashClass
_TLagPerLinkHashWtPortClassId_Object = MibTableColumn
tLagPerLinkHashWtPortClassId = _TLagPerLinkHashWtPortClassId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 11, 1, 2),
    _TLagPerLinkHashWtPortClassId_Type()
)
tLagPerLinkHashWtPortClassId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLagPerLinkHashWtPortClassId.setStatus("current")
_TLagPerLinkHashWtPortClassUsers_Type = Integer32
_TLagPerLinkHashWtPortClassUsers_Object = MibTableColumn
tLagPerLinkHashWtPortClassUsers = _TLagPerLinkHashWtPortClassUsers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 11, 1, 3),
    _TLagPerLinkHashWtPortClassUsers_Type()
)
tLagPerLinkHashWtPortClassUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLagPerLinkHashWtPortClassUsers.setStatus("current")
_TLagPerLinkHashWtPortClassAggWt_Type = Integer32
_TLagPerLinkHashWtPortClassAggWt_Object = MibTableColumn
tLagPerLinkHashWtPortClassAggWt = _TLagPerLinkHashWtPortClassAggWt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 11, 1, 4),
    _TLagPerLinkHashWtPortClassAggWt_Type()
)
tLagPerLinkHashWtPortClassAggWt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLagPerLinkHashWtPortClassAggWt.setStatus("current")
_TmnxLagActionTable_Object = MibTable
tmnxLagActionTable = _TmnxLagActionTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 12)
)
if mibBuilder.loadTexts:
    tmnxLagActionTable.setStatus("current")
_TmnxLagActionEntry_Object = MibTableRow
tmnxLagActionEntry = _TmnxLagActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 12, 1)
)
tmnxLagActionEntry.setIndexNames(
    (0, "TIMETRA-LAG-MIB", "tLagIndex"),
)
if mibBuilder.loadTexts:
    tmnxLagActionEntry.setStatus("current")


class _TmnxLagActionType_Type(Integer32):
    """Custom type tmnxLagActionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("loadBalance", 1))
    )


_TmnxLagActionType_Type.__name__ = "Integer32"
_TmnxLagActionType_Object = MibTableColumn
tmnxLagActionType = _TmnxLagActionType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 12, 1, 1),
    _TmnxLagActionType_Type()
)
tmnxLagActionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxLagActionType.setStatus("current")


class _TmnxLagAction_Type(TmnxActionType):
    """Custom type tmnxLagAction based on TmnxActionType"""
    defaultValue = 2


_TmnxLagAction_Type.__name__ = "TmnxActionType"
_TmnxLagAction_Object = MibTableColumn
tmnxLagAction = _TmnxLagAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 12, 1, 2),
    _TmnxLagAction_Type()
)
tmnxLagAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxLagAction.setStatus("current")


class _TmnxLagActionClassId_Type(TmnxLagPerLinkHashClassOrNone):
    """Custom type tmnxLagActionClassId based on TmnxLagPerLinkHashClassOrNone"""
    defaultValue = 0


_TmnxLagActionClassId_Type.__name__ = "TmnxLagPerLinkHashClassOrNone"
_TmnxLagActionClassId_Object = MibTableColumn
tmnxLagActionClassId = _TmnxLagActionClassId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 12, 1, 3),
    _TmnxLagActionClassId_Type()
)
tmnxLagActionClassId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxLagActionClassId.setStatus("current")
_TLagBfdObs_ObjectIdentity = ObjectIdentity
tLagBfdObs = _TLagBfdObs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 50)
)
_TmnxLagBfdFamTableLastChgd_Type = TimeStamp
_TmnxLagBfdFamTableLastChgd_Object = MibScalar
tmnxLagBfdFamTableLastChgd = _TmnxLagBfdFamTableLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 50, 1),
    _TmnxLagBfdFamTableLastChgd_Type()
)
tmnxLagBfdFamTableLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLagBfdFamTableLastChgd.setStatus("current")
_TmnxLagBfdFamTable_Object = MibTable
tmnxLagBfdFamTable = _TmnxLagBfdFamTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 50, 2)
)
if mibBuilder.loadTexts:
    tmnxLagBfdFamTable.setStatus("current")
_TmnxLagBfdFamEntry_Object = MibTableRow
tmnxLagBfdFamEntry = _TmnxLagBfdFamEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 50, 2, 1)
)
tmnxLagBfdFamEntry.setIndexNames(
    (0, "TIMETRA-LAG-MIB", "tLagIndex"),
    (0, "TIMETRA-LAG-MIB", "tmnxLagBfdFamAddressType"),
)
if mibBuilder.loadTexts:
    tmnxLagBfdFamEntry.setStatus("current")
_TmnxLagBfdFamAddressType_Type = InetAddressType
_TmnxLagBfdFamAddressType_Object = MibTableColumn
tmnxLagBfdFamAddressType = _TmnxLagBfdFamAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 50, 2, 1, 1),
    _TmnxLagBfdFamAddressType_Type()
)
tmnxLagBfdFamAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxLagBfdFamAddressType.setStatus("current")
_TmnxLagBfdFamLastCh_Type = TimeStamp
_TmnxLagBfdFamLastCh_Object = MibTableColumn
tmnxLagBfdFamLastCh = _TmnxLagBfdFamLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 50, 2, 1, 2),
    _TmnxLagBfdFamLastCh_Type()
)
tmnxLagBfdFamLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLagBfdFamLastCh.setStatus("current")


class _TmnxLagBfdFamAdminState_Type(TmnxEnabledDisabled):
    """Custom type tmnxLagBfdFamAdminState based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxLagBfdFamAdminState_Type.__name__ = "TmnxEnabledDisabled"
_TmnxLagBfdFamAdminState_Object = MibTableColumn
tmnxLagBfdFamAdminState = _TmnxLagBfdFamAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 50, 2, 1, 3),
    _TmnxLagBfdFamAdminState_Type()
)
tmnxLagBfdFamAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLagBfdFamAdminState.setStatus("current")


class _TmnxLagBfdFamAddrType_Type(InetAddressType):
    """Custom type tmnxLagBfdFamAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxLagBfdFamAddrType_Type.__name__ = "InetAddressType"
_TmnxLagBfdFamAddrType_Object = MibTableColumn
tmnxLagBfdFamAddrType = _TmnxLagBfdFamAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 50, 2, 1, 4),
    _TmnxLagBfdFamAddrType_Type()
)
tmnxLagBfdFamAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLagBfdFamAddrType.setStatus("current")


class _TmnxLagBfdFamAddr_Type(InetAddress):
    """Custom type tmnxLagBfdFamAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxLagBfdFamAddr_Type.__name__ = "InetAddress"
_TmnxLagBfdFamAddr_Object = MibTableColumn
tmnxLagBfdFamAddr = _TmnxLagBfdFamAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 50, 2, 1, 5),
    _TmnxLagBfdFamAddr_Type()
)
tmnxLagBfdFamAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLagBfdFamAddr.setStatus("current")


class _TmnxLagBfdFamRemAddrType_Type(InetAddressType):
    """Custom type tmnxLagBfdFamRemAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxLagBfdFamRemAddrType_Type.__name__ = "InetAddressType"
_TmnxLagBfdFamRemAddrType_Object = MibTableColumn
tmnxLagBfdFamRemAddrType = _TmnxLagBfdFamRemAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 50, 2, 1, 6),
    _TmnxLagBfdFamRemAddrType_Type()
)
tmnxLagBfdFamRemAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLagBfdFamRemAddrType.setStatus("current")


class _TmnxLagBfdFamRemAddr_Type(InetAddress):
    """Custom type tmnxLagBfdFamRemAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxLagBfdFamRemAddr_Type.__name__ = "InetAddress"
_TmnxLagBfdFamRemAddr_Object = MibTableColumn
tmnxLagBfdFamRemAddr = _TmnxLagBfdFamRemAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 50, 2, 1, 7),
    _TmnxLagBfdFamRemAddr_Type()
)
tmnxLagBfdFamRemAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLagBfdFamRemAddr.setStatus("current")


class _TmnxLagBfdFamTransmitInterval_Type(Unsigned32):
    """Custom type tmnxLagBfdFamTransmitInterval based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100000),
    )


_TmnxLagBfdFamTransmitInterval_Type.__name__ = "Unsigned32"
_TmnxLagBfdFamTransmitInterval_Object = MibTableColumn
tmnxLagBfdFamTransmitInterval = _TmnxLagBfdFamTransmitInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 50, 2, 1, 8),
    _TmnxLagBfdFamTransmitInterval_Type()
)
tmnxLagBfdFamTransmitInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLagBfdFamTransmitInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxLagBfdFamTransmitInterval.setUnits("milliseconds")


class _TmnxLagBfdFamReceiveInterval_Type(Unsigned32):
    """Custom type tmnxLagBfdFamReceiveInterval based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100000),
    )


_TmnxLagBfdFamReceiveInterval_Type.__name__ = "Unsigned32"
_TmnxLagBfdFamReceiveInterval_Object = MibTableColumn
tmnxLagBfdFamReceiveInterval = _TmnxLagBfdFamReceiveInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 50, 2, 1, 9),
    _TmnxLagBfdFamReceiveInterval_Type()
)
tmnxLagBfdFamReceiveInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLagBfdFamReceiveInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxLagBfdFamReceiveInterval.setUnits("milliseconds")


class _TmnxLagBfdFamMultiplier_Type(Unsigned32):
    """Custom type tmnxLagBfdFamMultiplier based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 20),
    )


_TmnxLagBfdFamMultiplier_Type.__name__ = "Unsigned32"
_TmnxLagBfdFamMultiplier_Object = MibTableColumn
tmnxLagBfdFamMultiplier = _TmnxLagBfdFamMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 50, 2, 1, 10),
    _TmnxLagBfdFamMultiplier_Type()
)
tmnxLagBfdFamMultiplier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLagBfdFamMultiplier.setStatus("current")


class _TmnxLagBfdFamMaxSetupTime_Type(Integer32):
    """Custom type tmnxLagBfdFamMaxSetupTime based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 60000),
    )


_TmnxLagBfdFamMaxSetupTime_Type.__name__ = "Integer32"
_TmnxLagBfdFamMaxSetupTime_Object = MibTableColumn
tmnxLagBfdFamMaxSetupTime = _TmnxLagBfdFamMaxSetupTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 50, 2, 1, 11),
    _TmnxLagBfdFamMaxSetupTime_Type()
)
tmnxLagBfdFamMaxSetupTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLagBfdFamMaxSetupTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxLagBfdFamMaxSetupTime.setUnits("milli-seconds")


class _TmnxLagBfdFamMaxAdminDownTime_Type(Integer32):
    """Custom type tmnxLagBfdFamMaxAdminDownTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 3600),
    )


_TmnxLagBfdFamMaxAdminDownTime_Type.__name__ = "Integer32"
_TmnxLagBfdFamMaxAdminDownTime_Object = MibTableColumn
tmnxLagBfdFamMaxAdminDownTime = _TmnxLagBfdFamMaxAdminDownTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 50, 2, 1, 12),
    _TmnxLagBfdFamMaxAdminDownTime_Type()
)
tmnxLagBfdFamMaxAdminDownTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLagBfdFamMaxAdminDownTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxLagBfdFamMaxAdminDownTime.setUnits("seconds")


class _TmnxLagBfdFamBfdOnDistributing_Type(TruthValue):
    """Custom type tmnxLagBfdFamBfdOnDistributing based on TruthValue"""
    defaultValue = 2


_TmnxLagBfdFamBfdOnDistributing_Type.__name__ = "TruthValue"
_TmnxLagBfdFamBfdOnDistributing_Object = MibTableColumn
tmnxLagBfdFamBfdOnDistributing = _TmnxLagBfdFamBfdOnDistributing_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 50, 2, 1, 13),
    _TmnxLagBfdFamBfdOnDistributing_Type()
)
tmnxLagBfdFamBfdOnDistributing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLagBfdFamBfdOnDistributing.setStatus("current")
_TmnxLagBfdMemTable_Object = MibTable
tmnxLagBfdMemTable = _TmnxLagBfdMemTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 50, 3)
)
if mibBuilder.loadTexts:
    tmnxLagBfdMemTable.setStatus("current")
_TmnxLagBfdMemEntry_Object = MibTableRow
tmnxLagBfdMemEntry = _TmnxLagBfdMemEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 50, 3, 1)
)
if mibBuilder.loadTexts:
    tmnxLagBfdMemEntry.setStatus("current")


class _TmnxLagBfdMemState_Type(Integer32):
    """Custom type tmnxLagBfdMemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("failed", 1),
          ("failedFwd", 2),
          ("waiting", 3),
          ("waitingFwd", 4),
          ("up", 5),
          ("down", 6))
    )


_TmnxLagBfdMemState_Type.__name__ = "Integer32"
_TmnxLagBfdMemState_Object = MibTableColumn
tmnxLagBfdMemState = _TmnxLagBfdMemState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 50, 3, 1, 1),
    _TmnxLagBfdMemState_Type()
)
tmnxLagBfdMemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLagBfdMemState.setStatus("current")
_TmnxLagBfdMemSetupTimeLeft_Type = Unsigned32
_TmnxLagBfdMemSetupTimeLeft_Object = MibTableColumn
tmnxLagBfdMemSetupTimeLeft = _TmnxLagBfdMemSetupTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 50, 3, 1, 2),
    _TmnxLagBfdMemSetupTimeLeft_Type()
)
tmnxLagBfdMemSetupTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLagBfdMemSetupTimeLeft.setStatus("current")
if mibBuilder.loadTexts:
    tmnxLagBfdMemSetupTimeLeft.setUnits("milli-seconds")
_TmnxLagBfdMemAdminDownLeft_Type = Unsigned32
_TmnxLagBfdMemAdminDownLeft_Object = MibTableColumn
tmnxLagBfdMemAdminDownLeft = _TmnxLagBfdMemAdminDownLeft_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 50, 3, 1, 3),
    _TmnxLagBfdMemAdminDownLeft_Type()
)
tmnxLagBfdMemAdminDownLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLagBfdMemAdminDownLeft.setStatus("current")
if mibBuilder.loadTexts:
    tmnxLagBfdMemAdminDownLeft.setUnits("seconds")
_TLagNotifyPrefix_ObjectIdentity = ObjectIdentity
tLagNotifyPrefix = _TLagNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 15)
)
_TLagNotifications_ObjectIdentity = ObjectIdentity
tLagNotifications = _TLagNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 15, 0)
)
tLagConfigEntry.registerAugmentions(
    ("TIMETRA-LAG-MIB",
     "tLagOperationEntry")
)
tLagOperationEntry.setIndexNames(*tLagConfigEntry.getIndexNames())
dot3adAggPortEntry.registerAugmentions(
    ("TIMETRA-LAG-MIB",
     "tLagPortEntry")
)
tLagPortEntry.setIndexNames(*dot3adAggPortEntry.getIndexNames())
tLagMemberEntry.registerAugmentions(
    ("TIMETRA-LAG-MIB",
     "tmnxLagBfdMemEntry")
)
tmnxLagBfdMemEntry.setIndexNames(*tLagMemberEntry.getIndexNames())

# Managed Objects groups

tmnxLagNotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 2, 2)
)
tmnxLagNotifyObjsGroup.setObjects(
    ("TIMETRA-LAG-MIB", "tLagNotifyPortAddFailReason")
)
if mibBuilder.loadTexts:
    tmnxLagNotifyObjsGroup.setStatus("obsolete")

tmnxLagInstanceV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 2, 5)
)
tmnxLagInstanceV4v0Group.setObjects(
      *(("TIMETRA-LAG-MIB", "tLagRowStatus"),
        ("TIMETRA-LAG-MIB", "tLagPortThreshold"),
        ("TIMETRA-LAG-MIB", "tLagPortThresholdAction"),
        ("TIMETRA-LAG-MIB", "tLagEnableMarkerGenerator"),
        ("TIMETRA-LAG-MIB", "tLagEnableLACP"),
        ("TIMETRA-LAG-MIB", "tLagDescription"),
        ("TIMETRA-LAG-MIB", "tLagDynamicCosting"),
        ("TIMETRA-LAG-MIB", "tLagLACPMode"),
        ("TIMETRA-LAG-MIB", "tLagLACPAdminKeyAutogen"),
        ("TIMETRA-LAG-MIB", "tLagLACPTransmitInterval"),
        ("TIMETRA-LAG-MIB", "tLagAccessAdaptQos"),
        ("TIMETRA-LAG-MIB", "tLagLACPXmitStdby"),
        ("TIMETRA-LAG-MIB", "tLagLACPSelCrit"),
        ("TIMETRA-LAG-MIB", "tLagLACPSelCritSlaveToPartner"),
        ("TIMETRA-LAG-MIB", "tLagLACPNbrOfSubGroups"),
        ("TIMETRA-LAG-MIB", "tLagholdTimeDown"),
        ("TIMETRA-LAG-MIB", "tLagIfIndex"),
        ("TIMETRA-LAG-MIB", "tLagConfigLastChange"),
        ("TIMETRA-LAG-MIB", "tLagPortThresholdFalling"),
        ("TIMETRA-LAG-MIB", "tLagPortThresholdRising"),
        ("TIMETRA-LAG-MIB", "tLagMemberPortName"),
        ("TIMETRA-LAG-MIB", "tLagMemberPortIsPrimary"),
        ("TIMETRA-LAG-MIB", "tLagPortSubgroup"),
        ("TIMETRA-LAG-MIB", "tLagPortActiveStdby"))
)
if mibBuilder.loadTexts:
    tmnxLagInstanceV4v0Group.setStatus("obsolete")

tmnxObsoletedObjectsV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 2, 6)
)
tmnxObsoletedObjectsV4v0Group.setObjects(
    ("TIMETRA-LAG-MIB", "tLagLACPPrimaryPort")
)
if mibBuilder.loadTexts:
    tmnxObsoletedObjectsV4v0Group.setStatus("current")

tmnxLagInstanceV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 2, 7)
)
tmnxLagInstanceV5v0Group.setObjects(
      *(("TIMETRA-LAG-MIB", "tLagRowStatus"),
        ("TIMETRA-LAG-MIB", "tLagPortThreshold"),
        ("TIMETRA-LAG-MIB", "tLagPortThresholdAction"),
        ("TIMETRA-LAG-MIB", "tLagEnableMarkerGenerator"),
        ("TIMETRA-LAG-MIB", "tLagEnableLACP"),
        ("TIMETRA-LAG-MIB", "tLagDescription"),
        ("TIMETRA-LAG-MIB", "tLagDynamicCosting"),
        ("TIMETRA-LAG-MIB", "tLagLACPMode"),
        ("TIMETRA-LAG-MIB", "tLagLACPAdminKeyAutogen"),
        ("TIMETRA-LAG-MIB", "tLagLACPTransmitInterval"),
        ("TIMETRA-LAG-MIB", "tLagAccessAdaptQos"),
        ("TIMETRA-LAG-MIB", "tLagLACPXmitStdby"),
        ("TIMETRA-LAG-MIB", "tLagLACPSelCrit"),
        ("TIMETRA-LAG-MIB", "tLagLACPSelCritSlaveToPartner"),
        ("TIMETRA-LAG-MIB", "tLagLACPNbrOfSubGroups"),
        ("TIMETRA-LAG-MIB", "tLagholdTimeDown"),
        ("TIMETRA-LAG-MIB", "tLagIfIndex"),
        ("TIMETRA-LAG-MIB", "tLagConfigLastChange"),
        ("TIMETRA-LAG-MIB", "tLagPortThresholdFalling"),
        ("TIMETRA-LAG-MIB", "tLagPortThresholdRising"),
        ("TIMETRA-LAG-MIB", "tLagMemberPortName"),
        ("TIMETRA-LAG-MIB", "tLagMemberPortIsPrimary"),
        ("TIMETRA-LAG-MIB", "tLagPortSubgroup"),
        ("TIMETRA-LAG-MIB", "tLagPortActiveStdby"))
)
if mibBuilder.loadTexts:
    tmnxLagInstanceV5v0Group.setStatus("obsolete")

tmnxLagNotifyObjsV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 2, 9)
)
tmnxLagNotifyObjsV5v0Group.setObjects(
      *(("TIMETRA-LAG-MIB", "tLagNotifyPortAddFailReason"),
        ("TIMETRA-LAG-MIB", "tLagNotifySubGroupSelected"))
)
if mibBuilder.loadTexts:
    tmnxLagNotifyObjsV5v0Group.setStatus("obsolete")

tmnxLagHsmdaV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 2, 10)
)
tmnxLagHsmdaV6v0Group.setObjects(
    ("TIMETRA-LAG-MIB", "tLagPortType")
)
if mibBuilder.loadTexts:
    tmnxLagHsmdaV6v0Group.setStatus("current")

tmnxLagInstanceV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 2, 11)
)
tmnxLagInstanceV6v0Group.setObjects(
      *(("TIMETRA-LAG-MIB", "tLagRowStatus"),
        ("TIMETRA-LAG-MIB", "tLagPortThreshold"),
        ("TIMETRA-LAG-MIB", "tLagPortThresholdAction"),
        ("TIMETRA-LAG-MIB", "tLagEnableMarkerGenerator"),
        ("TIMETRA-LAG-MIB", "tLagEnableLACP"),
        ("TIMETRA-LAG-MIB", "tLagDescription"),
        ("TIMETRA-LAG-MIB", "tLagDynamicCosting"),
        ("TIMETRA-LAG-MIB", "tLagLACPMode"),
        ("TIMETRA-LAG-MIB", "tLagLACPAdminKeyAutogen"),
        ("TIMETRA-LAG-MIB", "tLagLACPTransmitInterval"),
        ("TIMETRA-LAG-MIB", "tLagAccessAdaptQos"),
        ("TIMETRA-LAG-MIB", "tLagLACPXmitStdby"),
        ("TIMETRA-LAG-MIB", "tLagLACPSelCrit"),
        ("TIMETRA-LAG-MIB", "tLagLACPSelCritSlaveToPartner"),
        ("TIMETRA-LAG-MIB", "tLagLACPNbrOfSubGroups"),
        ("TIMETRA-LAG-MIB", "tLagholdTimeDown"),
        ("TIMETRA-LAG-MIB", "tLagIfIndex"),
        ("TIMETRA-LAG-MIB", "tLagConfigLastChange"),
        ("TIMETRA-LAG-MIB", "tLagPortThresholdFalling"),
        ("TIMETRA-LAG-MIB", "tLagPortThresholdRising"),
        ("TIMETRA-LAG-MIB", "tLagMemberPortName"),
        ("TIMETRA-LAG-MIB", "tLagMemberPortIsPrimary"),
        ("TIMETRA-LAG-MIB", "tLagPortSubgroup"),
        ("TIMETRA-LAG-MIB", "tLagPortActiveStdby"),
        ("TIMETRA-LAG-MIB", "tLagPortReasonDownFlags"))
)
if mibBuilder.loadTexts:
    tmnxLagInstanceV6v0Group.setStatus("obsolete")

tmnxLagV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 2, 13)
)
tmnxLagV7v0Group.setObjects(
    ("TIMETRA-LAG-MIB", "tLagPerFpIngQueuing")
)
if mibBuilder.loadTexts:
    tmnxLagV7v0Group.setStatus("obsolete")

tmnxObsoletedObjectsV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 2, 14)
)
tmnxObsoletedObjectsV7v0Group.setObjects(
    ("TIMETRA-LAG-MIB", "tLagPortReasonDownFlags")
)
if mibBuilder.loadTexts:
    tmnxObsoletedObjectsV7v0Group.setStatus("current")

tmnxLagInstanceV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 2, 15)
)
tmnxLagInstanceV7v0Group.setObjects(
      *(("TIMETRA-LAG-MIB", "tLagRowStatus"),
        ("TIMETRA-LAG-MIB", "tLagPortThreshold"),
        ("TIMETRA-LAG-MIB", "tLagPortThresholdAction"),
        ("TIMETRA-LAG-MIB", "tLagEnableMarkerGenerator"),
        ("TIMETRA-LAG-MIB", "tLagEnableLACP"),
        ("TIMETRA-LAG-MIB", "tLagDescription"),
        ("TIMETRA-LAG-MIB", "tLagDynamicCosting"),
        ("TIMETRA-LAG-MIB", "tLagLACPMode"),
        ("TIMETRA-LAG-MIB", "tLagLACPAdminKeyAutogen"),
        ("TIMETRA-LAG-MIB", "tLagLACPTransmitInterval"),
        ("TIMETRA-LAG-MIB", "tLagAccessAdaptQos"),
        ("TIMETRA-LAG-MIB", "tLagLACPXmitStdby"),
        ("TIMETRA-LAG-MIB", "tLagLACPSelCrit"),
        ("TIMETRA-LAG-MIB", "tLagLACPSelCritSlaveToPartner"),
        ("TIMETRA-LAG-MIB", "tLagLACPNbrOfSubGroups"),
        ("TIMETRA-LAG-MIB", "tLagholdTimeDown"),
        ("TIMETRA-LAG-MIB", "tLagIfIndex"),
        ("TIMETRA-LAG-MIB", "tLagConfigLastChange"),
        ("TIMETRA-LAG-MIB", "tLagPortThresholdFalling"),
        ("TIMETRA-LAG-MIB", "tLagPortThresholdRising"),
        ("TIMETRA-LAG-MIB", "tLagMemberPortName"),
        ("TIMETRA-LAG-MIB", "tLagMemberPortIsPrimary"),
        ("TIMETRA-LAG-MIB", "tLagPortSubgroup"),
        ("TIMETRA-LAG-MIB", "tLagPortActiveStdby"))
)
if mibBuilder.loadTexts:
    tmnxLagInstanceV7v0Group.setStatus("current")

tmnxLagV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 2, 16)
)
tmnxLagV8v0Group.setObjects(
      *(("TIMETRA-LAG-MIB", "tLagPerFpIngQueuing"),
        ("TIMETRA-LAG-MIB", "tLagSystemId"),
        ("TIMETRA-LAG-MIB", "tLagSystemPriority"))
)
if mibBuilder.loadTexts:
    tmnxLagV8v0Group.setStatus("current")

tmnxLagInstanceV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 2, 17)
)
tmnxLagInstanceV9v0Group.setObjects(
    ("TIMETRA-LAG-MIB", "tLagStandbySignaling")
)
if mibBuilder.loadTexts:
    tmnxLagInstanceV9v0Group.setStatus("current")

tmnxLagNotifyObjsV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 2, 18)
)
tmnxLagNotifyObjsV10v0Group.setObjects(
      *(("TIMETRA-LAG-MIB", "tLagNotifyPortAddFailReason"),
        ("TIMETRA-LAG-MIB", "tLagNotifySubGroupSelected"),
        ("TIMETRA-LAG-MIB", "tLagNotifyAdditionalInfo"),
        ("TIMETRA-LAG-MIB", "tLagNotifyStateChangedReason"))
)
if mibBuilder.loadTexts:
    tmnxLagNotifyObjsV10v0Group.setStatus("current")

tmnxLagV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 2, 20)
)
tmnxLagV11v0Group.setObjects(
      *(("TIMETRA-LAG-MIB", "tLagLinkMapProfPortTableLastChgd"),
        ("TIMETRA-LAG-MIB", "tLagLinkMapProfPortRowStatus"),
        ("TIMETRA-LAG-MIB", "tLagLinkMapProfPortLastChanged"),
        ("TIMETRA-LAG-MIB", "tLagLinkMapProfPortType"),
        ("TIMETRA-LAG-MIB", "tLagLinkMapProfileDescription"),
        ("TIMETRA-LAG-MIB", "tLagLinkMapProfileFailureMode"),
        ("TIMETRA-LAG-MIB", "tLagLinkMapProfileLastChanged"),
        ("TIMETRA-LAG-MIB", "tLagLinkMapProfileActiveLink"),
        ("TIMETRA-LAG-MIB", "tLagLinkMapProfileRowStatus"),
        ("TIMETRA-LAG-MIB", "tLagLinkMapProfileTableLastChgd"),
        ("TIMETRA-LAG-MIB", "tLagPerLinkHash"),
        ("TIMETRA-LAG-MIB", "tLagPerFpEgrQueuing"),
        ("TIMETRA-LAG-MIB", "tLagIncludeEgrHashCfg"))
)
if mibBuilder.loadTexts:
    tmnxLagV11v0Group.setStatus("current")

tmnxLagBfdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 2, 21)
)
tmnxLagBfdGroup.setObjects(
      *(("TIMETRA-LAG-MIB", "tmnxLagBfdFamTableLastChgd"),
        ("TIMETRA-LAG-MIB", "tmnxLagBfdFamLastCh"),
        ("TIMETRA-LAG-MIB", "tmnxLagBfdFamAdminState"),
        ("TIMETRA-LAG-MIB", "tmnxLagBfdFamAddrType"),
        ("TIMETRA-LAG-MIB", "tmnxLagBfdFamAddr"),
        ("TIMETRA-LAG-MIB", "tmnxLagBfdFamRemAddrType"),
        ("TIMETRA-LAG-MIB", "tmnxLagBfdFamRemAddr"),
        ("TIMETRA-LAG-MIB", "tmnxLagBfdFamTransmitInterval"),
        ("TIMETRA-LAG-MIB", "tmnxLagBfdFamReceiveInterval"),
        ("TIMETRA-LAG-MIB", "tmnxLagBfdFamMultiplier"),
        ("TIMETRA-LAG-MIB", "tmnxLagBfdFamMaxSetupTime"),
        ("TIMETRA-LAG-MIB", "tmnxLagBfdFamMaxAdminDownTime"),
        ("TIMETRA-LAG-MIB", "tmnxLagBfdFamBfdOnDistributing"),
        ("TIMETRA-LAG-MIB", "tmnxLagBfdMemState"),
        ("TIMETRA-LAG-MIB", "tmnxLagBfdMemSetupTimeLeft"),
        ("TIMETRA-LAG-MIB", "tmnxLagBfdMemAdminDownLeft"))
)
if mibBuilder.loadTexts:
    tmnxLagBfdGroup.setStatus("current")

tmnxLagPerFpSapV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 2, 23)
)
tmnxLagPerFpSapV12v0Group.setObjects(
    ("TIMETRA-LAG-MIB", "tLagPerFpSapInstance")
)
if mibBuilder.loadTexts:
    tmnxLagPerFpSapV12v0Group.setStatus("current")

tmnxLagSelectionHoldV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 2, 24)
)
tmnxLagSelectionHoldV12v0Group.setObjects(
      *(("TIMETRA-LAG-MIB", "tLagLacpHoldTime"),
        ("TIMETRA-LAG-MIB", "tLagSelectedSubGroup"),
        ("TIMETRA-LAG-MIB", "tLagCandidateSubGroup"),
        ("TIMETRA-LAG-MIB", "tLagRemainingHoldTime"))
)
if mibBuilder.loadTexts:
    tmnxLagSelectionHoldV12v0Group.setStatus("current")

tmnxLagPerLinkHashV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 2, 25)
)
tmnxLagPerLinkHashV12v0Group.setObjects(
      *(("TIMETRA-LAG-MIB", "tLagPerLinkHashWeighted"),
        ("TIMETRA-LAG-MIB", "tLagPerLinkHashWeightedRebalance"),
        ("TIMETRA-LAG-MIB", "tLagPerLinkHashWtPort"),
        ("TIMETRA-LAG-MIB", "tLagPerLinkHashWtPortClassId"),
        ("TIMETRA-LAG-MIB", "tLagPerLinkHashWtPortClassUsers"),
        ("TIMETRA-LAG-MIB", "tLagPerLinkHashWtPortClassAggWt"),
        ("TIMETRA-LAG-MIB", "tmnxLagActionType"),
        ("TIMETRA-LAG-MIB", "tmnxLagAction"),
        ("TIMETRA-LAG-MIB", "tmnxLagActionClassId"))
)
if mibBuilder.loadTexts:
    tmnxLagPerLinkHashV12v0Group.setStatus("current")

tmnxLagMixed10g100gV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 2, 26)
)
tmnxLagMixed10g100gV12v0Group.setObjects(
      *(("TIMETRA-LAG-MIB", "tLagPortWeightSpeed"),
        ("TIMETRA-LAG-MIB", "tLagWeightThreshold"),
        ("TIMETRA-LAG-MIB", "tLagWeightThresholdAction"),
        ("TIMETRA-LAG-MIB", "tLagPortWeightUp"))
)
if mibBuilder.loadTexts:
    tmnxLagMixed10g100gV12v0Group.setStatus("current")


# Notification objects

tLagDynamicCostOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 15, 0, 1)
)
tLagDynamicCostOn.setObjects(
    ("TIMETRA-LAG-MIB", "tLagPortThreshold")
)
if mibBuilder.loadTexts:
    tLagDynamicCostOn.setStatus(
        "current"
    )

tLagDynamicCostOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 15, 0, 2)
)
tLagDynamicCostOff.setObjects(
    ("TIMETRA-LAG-MIB", "tLagPortThreshold")
)
if mibBuilder.loadTexts:
    tLagDynamicCostOff.setStatus(
        "current"
    )

tLagPortAddFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 15, 0, 3)
)
tLagPortAddFailed.setObjects(
      *(("TIMETRA-LAG-MIB", "tLagRowStatus"),
        ("TIMETRA-PORT-MIB", "tmnxPortLagId"),
        ("TIMETRA-LAG-MIB", "tLagNotifyPortAddFailReason"))
)
if mibBuilder.loadTexts:
    tLagPortAddFailed.setStatus(
        "current"
    )

tLagSubGroupSelected = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 15, 0, 4)
)
tLagSubGroupSelected.setObjects(
    ("TIMETRA-LAG-MIB", "tLagNotifySubGroupSelected")
)
if mibBuilder.loadTexts:
    tLagSubGroupSelected.setStatus(
        "current"
    )

tLagPortAddFailureCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 15, 0, 5)
)
tLagPortAddFailureCleared.setObjects(
      *(("TIMETRA-LAG-MIB", "tLagRowStatus"),
        ("TIMETRA-PORT-MIB", "tmnxPortLagId"),
        ("TIMETRA-LAG-MIB", "tLagNotifyPortAddFailReason"))
)
if mibBuilder.loadTexts:
    tLagPortAddFailureCleared.setStatus(
        "current"
    )

tLagStateEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 15, 0, 6)
)
tLagStateEvent.setObjects(
      *(("TIMETRA-LAG-MIB", "tLagRowStatus"),
        ("TIMETRA-LAG-MIB", "tLagNotifyAdditionalInfo"))
)
if mibBuilder.loadTexts:
    tLagStateEvent.setStatus(
        "current"
    )

tLagMemberStateEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 15, 0, 7)
)
tLagMemberStateEvent.setObjects(
      *(("TIMETRA-LAG-MIB", "tLagRowStatus"),
        ("TIMETRA-PORT-MIB", "tmnxPortLagId"),
        ("TIMETRA-LAG-MIB", "tLagNotifyAdditionalInfo"),
        ("TIMETRA-LAG-MIB", "tLagNotifyStateChangedReason"))
)
if mibBuilder.loadTexts:
    tLagMemberStateEvent.setStatus(
        "current"
    )

tmnxLagBfdMemStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 15, 0, 8)
)
tmnxLagBfdMemStateChanged.setObjects(
      *(("TIMETRA-LAG-MIB", "tmnxLagBfdMemState"),
        ("TIMETRA-LAG-MIB", "tLagNotifyAdditionalInfo"))
)
if mibBuilder.loadTexts:
    tmnxLagBfdMemStateChanged.setStatus(
        "current"
    )


# Notifications groups

tmnxLagNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 2, 3)
)
tmnxLagNotificationsGroup.setObjects(
      *(("TIMETRA-LAG-MIB", "tLagDynamicCostOn"),
        ("TIMETRA-LAG-MIB", "tLagDynamicCostOff"),
        ("TIMETRA-LAG-MIB", "tLagPortAddFailed"))
)
if mibBuilder.loadTexts:
    tmnxLagNotificationsGroup.setStatus(
        "obsolete"
    )

tmnxLagV5v0NotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 2, 8)
)
tmnxLagV5v0NotifGroup.setObjects(
      *(("TIMETRA-LAG-MIB", "tLagDynamicCostOn"),
        ("TIMETRA-LAG-MIB", "tLagDynamicCostOff"),
        ("TIMETRA-LAG-MIB", "tLagPortAddFailed"),
        ("TIMETRA-LAG-MIB", "tLagSubGroupSelected"))
)
if mibBuilder.loadTexts:
    tmnxLagV5v0NotifGroup.setStatus(
        "obsolete"
    )

tmnxLagV6v0NotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 2, 12)
)
tmnxLagV6v0NotifGroup.setObjects(
      *(("TIMETRA-LAG-MIB", "tLagDynamicCostOn"),
        ("TIMETRA-LAG-MIB", "tLagDynamicCostOff"),
        ("TIMETRA-LAG-MIB", "tLagPortAddFailed"),
        ("TIMETRA-LAG-MIB", "tLagSubGroupSelected"),
        ("TIMETRA-LAG-MIB", "tLagPortAddFailureCleared"))
)
if mibBuilder.loadTexts:
    tmnxLagV6v0NotifGroup.setStatus(
        "current"
    )

tmnxLagV10v0NotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 2, 19)
)
tmnxLagV10v0NotifGroup.setObjects(
      *(("TIMETRA-LAG-MIB", "tLagStateEvent"),
        ("TIMETRA-LAG-MIB", "tLagMemberStateEvent"))
)
if mibBuilder.loadTexts:
    tmnxLagV10v0NotifGroup.setStatus(
        "current"
    )

tmnxLagBfdNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 2, 22)
)
tmnxLagBfdNotifGroup.setObjects(
    ("TIMETRA-LAG-MIB", "tmnxLagBfdMemStateChanged")
)
if mibBuilder.loadTexts:
    tmnxLagBfdNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxLagV4v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 1, 3)
)
tmnxLagV4v0Compliance.setObjects(
      *(("TIMETRA-LAG-MIB", "tmnxLagInstanceV4v0Group"),
        ("TIMETRA-LAG-MIB", "tmnxLagNotifyObjsGroup"),
        ("TIMETRA-LAG-MIB", "tmnxLagNotificationsGroup"))
)
if mibBuilder.loadTexts:
    tmnxLagV4v0Compliance.setStatus(
        "obsolete"
    )

tmnxLagV5v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 1, 4)
)
tmnxLagV5v0Compliance.setObjects(
      *(("TIMETRA-LAG-MIB", "tmnxLagInstanceV5v0Group"),
        ("TIMETRA-LAG-MIB", "tmnxLagV5v0NotifGroup"))
)
if mibBuilder.loadTexts:
    tmnxLagV5v0Compliance.setStatus(
        "obsolete"
    )

tmnxLagV6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 1, 5)
)
tmnxLagV6v0Compliance.setObjects(
      *(("TIMETRA-LAG-MIB", "tmnxLagInstanceV6v0Group"),
        ("TIMETRA-LAG-MIB", "tmnxLagV6v0NotifGroup"))
)
if mibBuilder.loadTexts:
    tmnxLagV6v0Compliance.setStatus(
        "obsolete"
    )

tmnxLagV6v1Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 1, 6)
)
tmnxLagV6v1Compliance.setObjects(
      *(("TIMETRA-LAG-MIB", "tmnxLagInstanceV6v0Group"),
        ("TIMETRA-LAG-MIB", "tmnxLagV6v0NotifGroup"),
        ("TIMETRA-LAG-MIB", "tmnxLagHsmdaV6v0Group"))
)
if mibBuilder.loadTexts:
    tmnxLagV6v1Compliance.setStatus(
        "obsolete"
    )

tmnxLagV7v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 1, 7)
)
tmnxLagV7v0Compliance.setObjects(
      *(("TIMETRA-LAG-MIB", "tmnxLagInstanceV7v0Group"),
        ("TIMETRA-LAG-MIB", "tmnxLagV6v0NotifGroup"),
        ("TIMETRA-LAG-MIB", "tmnxLagHsmdaV6v0Group"),
        ("TIMETRA-LAG-MIB", "tmnxLagV7v0Group"))
)
if mibBuilder.loadTexts:
    tmnxLagV7v0Compliance.setStatus(
        "obsolete"
    )

tmnxLagV8v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 1, 8)
)
tmnxLagV8v0Compliance.setObjects(
      *(("TIMETRA-LAG-MIB", "tmnxLagInstanceV7v0Group"),
        ("TIMETRA-LAG-MIB", "tmnxLagV6v0NotifGroup"),
        ("TIMETRA-LAG-MIB", "tmnxLagHsmdaV6v0Group"),
        ("TIMETRA-LAG-MIB", "tmnxLagV8v0Group"))
)
if mibBuilder.loadTexts:
    tmnxLagV8v0Compliance.setStatus(
        "obsolete"
    )

tmnxLagV9v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 1, 9)
)
tmnxLagV9v0Compliance.setObjects(
      *(("TIMETRA-LAG-MIB", "tmnxLagInstanceV7v0Group"),
        ("TIMETRA-LAG-MIB", "tmnxLagInstanceV9v0Group"),
        ("TIMETRA-LAG-MIB", "tmnxLagV6v0NotifGroup"),
        ("TIMETRA-LAG-MIB", "tmnxLagHsmdaV6v0Group"),
        ("TIMETRA-LAG-MIB", "tmnxLagV8v0Group"))
)
if mibBuilder.loadTexts:
    tmnxLagV9v0Compliance.setStatus(
        "obsolete"
    )

tmnxLagV10v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 1, 10)
)
tmnxLagV10v0Compliance.setObjects(
      *(("TIMETRA-LAG-MIB", "tmnxLagInstanceV7v0Group"),
        ("TIMETRA-LAG-MIB", "tmnxLagInstanceV9v0Group"),
        ("TIMETRA-LAG-MIB", "tmnxLagV6v0NotifGroup"),
        ("TIMETRA-LAG-MIB", "tmnxLagV10v0NotifGroup"),
        ("TIMETRA-LAG-MIB", "tmnxLagHsmdaV6v0Group"),
        ("TIMETRA-LAG-MIB", "tmnxLagV8v0Group"))
)
if mibBuilder.loadTexts:
    tmnxLagV10v0Compliance.setStatus(
        "obsolete"
    )

tmnxLagV11v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 1, 11)
)
tmnxLagV11v0Compliance.setObjects(
      *(("TIMETRA-LAG-MIB", "tmnxLagInstanceV7v0Group"),
        ("TIMETRA-LAG-MIB", "tmnxLagInstanceV9v0Group"),
        ("TIMETRA-LAG-MIB", "tmnxLagV6v0NotifGroup"),
        ("TIMETRA-LAG-MIB", "tmnxLagV10v0NotifGroup"),
        ("TIMETRA-LAG-MIB", "tmnxLagHsmdaV6v0Group"),
        ("TIMETRA-LAG-MIB", "tmnxLagV11v0Group"),
        ("TIMETRA-LAG-MIB", "tmnxLagV8v0Group"),
        ("TIMETRA-LAG-MIB", "tmnxLagBfdGroup"),
        ("TIMETRA-LAG-MIB", "tmnxLagBfdNotifGroup"))
)
if mibBuilder.loadTexts:
    tmnxLagV11v0Compliance.setStatus(
        "obsolete"
    )

tmnxLagV12v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 1, 12)
)
tmnxLagV12v0Compliance.setObjects(
      *(("TIMETRA-LAG-MIB", "tmnxLagInstanceV7v0Group"),
        ("TIMETRA-LAG-MIB", "tmnxLagInstanceV9v0Group"),
        ("TIMETRA-LAG-MIB", "tmnxLagV6v0NotifGroup"),
        ("TIMETRA-LAG-MIB", "tmnxLagV10v0NotifGroup"),
        ("TIMETRA-LAG-MIB", "tmnxLagHsmdaV6v0Group"),
        ("TIMETRA-LAG-MIB", "tmnxLagV11v0Group"),
        ("TIMETRA-LAG-MIB", "tmnxLagV8v0Group"),
        ("TIMETRA-LAG-MIB", "tmnxLagBfdGroup"),
        ("TIMETRA-LAG-MIB", "tmnxLagBfdNotifGroup"),
        ("TIMETRA-LAG-MIB", "tmnxLagPerFpSapV12v0Group"),
        ("TIMETRA-LAG-MIB", "tmnxLagSelectionHoldV12v0Group"),
        ("TIMETRA-LAG-MIB", "tmnxLagPerLinkHashV12v0Group"),
        ("TIMETRA-LAG-MIB", "tmnxLagMixed10g100gV12v0Group"))
)
if mibBuilder.loadTexts:
    tmnxLagV12v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-LAG-MIB",
    **{"LAGInterfaceNumber": LAGInterfaceNumber,
       "LAGSubgroup": LAGSubgroup,
       "timetraLagMIBModule": timetraLagMIBModule,
       "tmnxLagConformance": tmnxLagConformance,
       "tmnxLagCompliances": tmnxLagCompliances,
       "tmnxLagV4v0Compliance": tmnxLagV4v0Compliance,
       "tmnxLagV5v0Compliance": tmnxLagV5v0Compliance,
       "tmnxLagV6v0Compliance": tmnxLagV6v0Compliance,
       "tmnxLagV6v1Compliance": tmnxLagV6v1Compliance,
       "tmnxLagV7v0Compliance": tmnxLagV7v0Compliance,
       "tmnxLagV8v0Compliance": tmnxLagV8v0Compliance,
       "tmnxLagV9v0Compliance": tmnxLagV9v0Compliance,
       "tmnxLagV10v0Compliance": tmnxLagV10v0Compliance,
       "tmnxLagV11v0Compliance": tmnxLagV11v0Compliance,
       "tmnxLagV12v0Compliance": tmnxLagV12v0Compliance,
       "tmnxLagGroups": tmnxLagGroups,
       "tmnxLagNotifyObjsGroup": tmnxLagNotifyObjsGroup,
       "tmnxLagNotificationsGroup": tmnxLagNotificationsGroup,
       "tmnxLagInstanceV4v0Group": tmnxLagInstanceV4v0Group,
       "tmnxObsoletedObjectsV4v0Group": tmnxObsoletedObjectsV4v0Group,
       "tmnxLagInstanceV5v0Group": tmnxLagInstanceV5v0Group,
       "tmnxLagV5v0NotifGroup": tmnxLagV5v0NotifGroup,
       "tmnxLagNotifyObjsV5v0Group": tmnxLagNotifyObjsV5v0Group,
       "tmnxLagHsmdaV6v0Group": tmnxLagHsmdaV6v0Group,
       "tmnxLagInstanceV6v0Group": tmnxLagInstanceV6v0Group,
       "tmnxLagV6v0NotifGroup": tmnxLagV6v0NotifGroup,
       "tmnxLagV7v0Group": tmnxLagV7v0Group,
       "tmnxObsoletedObjectsV7v0Group": tmnxObsoletedObjectsV7v0Group,
       "tmnxLagInstanceV7v0Group": tmnxLagInstanceV7v0Group,
       "tmnxLagV8v0Group": tmnxLagV8v0Group,
       "tmnxLagInstanceV9v0Group": tmnxLagInstanceV9v0Group,
       "tmnxLagNotifyObjsV10v0Group": tmnxLagNotifyObjsV10v0Group,
       "tmnxLagV10v0NotifGroup": tmnxLagV10v0NotifGroup,
       "tmnxLagV11v0Group": tmnxLagV11v0Group,
       "tmnxLagBfdGroup": tmnxLagBfdGroup,
       "tmnxLagBfdNotifGroup": tmnxLagBfdNotifGroup,
       "tmnxLagPerFpSapV12v0Group": tmnxLagPerFpSapV12v0Group,
       "tmnxLagSelectionHoldV12v0Group": tmnxLagSelectionHoldV12v0Group,
       "tmnxLagPerLinkHashV12v0Group": tmnxLagPerLinkHashV12v0Group,
       "tmnxLagMixed10g100gV12v0Group": tmnxLagMixed10g100gV12v0Group,
       "tmnxLagDCCompliances": tmnxLagDCCompliances,
       "tmnxLagDCGroups": tmnxLagDCGroups,
       "tLagObjects": tLagObjects,
       "tLagConfigTable": tLagConfigTable,
       "tLagConfigEntry": tLagConfigEntry,
       "tLagIndex": tLagIndex,
       "tLagRowStatus": tLagRowStatus,
       "tLagPortThreshold": tLagPortThreshold,
       "tLagPortThresholdAction": tLagPortThresholdAction,
       "tLagEnableMarkerGenerator": tLagEnableMarkerGenerator,
       "tLagEnableLACP": tLagEnableLACP,
       "tLagDescription": tLagDescription,
       "tLagDynamicCosting": tLagDynamicCosting,
       "tLagLACPMode": tLagLACPMode,
       "tLagLACPAdminKeyAutogen": tLagLACPAdminKeyAutogen,
       "tLagLACPTransmitInterval": tLagLACPTransmitInterval,
       "tLagAccessAdaptQos": tLagAccessAdaptQos,
       "tLagLACPXmitStdby": tLagLACPXmitStdby,
       "tLagLACPSelCrit": tLagLACPSelCrit,
       "tLagLACPSelCritSlaveToPartner": tLagLACPSelCritSlaveToPartner,
       "tLagLACPNbrOfSubGroups": tLagLACPNbrOfSubGroups,
       "tLagholdTimeDown": tLagholdTimeDown,
       "tLagPortType": tLagPortType,
       "tLagPerFpIngQueuing": tLagPerFpIngQueuing,
       "tLagSystemId": tLagSystemId,
       "tLagSystemPriority": tLagSystemPriority,
       "tLagStandbySignaling": tLagStandbySignaling,
       "tLagPerLinkHash": tLagPerLinkHash,
       "tLagPerFpEgrQueuing": tLagPerFpEgrQueuing,
       "tLagIncludeEgrHashCfg": tLagIncludeEgrHashCfg,
       "tLagPerFpSapInstance": tLagPerFpSapInstance,
       "tLagLacpHoldTime": tLagLacpHoldTime,
       "tLagPerLinkHashWeighted": tLagPerLinkHashWeighted,
       "tLagPerLinkHashWeightedRebalance": tLagPerLinkHashWeightedRebalance,
       "tLagPortWeightSpeed": tLagPortWeightSpeed,
       "tLagWeightThreshold": tLagWeightThreshold,
       "tLagWeightThresholdAction": tLagWeightThresholdAction,
       "tLagOperationTable": tLagOperationTable,
       "tLagOperationEntry": tLagOperationEntry,
       "tLagIfIndex": tLagIfIndex,
       "tLagConfigLastChange": tLagConfigLastChange,
       "tLagPortThresholdFalling": tLagPortThresholdFalling,
       "tLagPortThresholdRising": tLagPortThresholdRising,
       "tLagLACPPrimaryPort": tLagLACPPrimaryPort,
       "tLagPortReasonDownFlags": tLagPortReasonDownFlags,
       "tLagSelectedSubGroup": tLagSelectedSubGroup,
       "tLagCandidateSubGroup": tLagCandidateSubGroup,
       "tLagRemainingHoldTime": tLagRemainingHoldTime,
       "tLagPortWeightUp": tLagPortWeightUp,
       "tLagNotificationObjects": tLagNotificationObjects,
       "tLagNotifyPortAddFailReason": tLagNotifyPortAddFailReason,
       "tLagNotifySubGroupSelected": tLagNotifySubGroupSelected,
       "tLagNotifyAdditionalInfo": tLagNotifyAdditionalInfo,
       "tLagNotifyStateChangedReason": tLagNotifyStateChangedReason,
       "tLagMemberTable": tLagMemberTable,
       "tLagMemberEntry": tLagMemberEntry,
       "tLagMemberPortName": tLagMemberPortName,
       "tLagMemberPortIsPrimary": tLagMemberPortIsPrimary,
       "tLagPortTable": tLagPortTable,
       "tLagPortEntry": tLagPortEntry,
       "tLagPortSubgroup": tLagPortSubgroup,
       "tLagPortActiveStdby": tLagPortActiveStdby,
       "tLagLinkMapProfileTableLastChgd": tLagLinkMapProfileTableLastChgd,
       "tLagLinkMapProfileTable": tLagLinkMapProfileTable,
       "tLagLinkMapProfileEntry": tLagLinkMapProfileEntry,
       "tLagLinkMapProfileId": tLagLinkMapProfileId,
       "tLagLinkMapProfileRowStatus": tLagLinkMapProfileRowStatus,
       "tLagLinkMapProfileLastChanged": tLagLinkMapProfileLastChanged,
       "tLagLinkMapProfileDescription": tLagLinkMapProfileDescription,
       "tLagLinkMapProfileFailureMode": tLagLinkMapProfileFailureMode,
       "tLagLinkMapProfileActiveLink": tLagLinkMapProfileActiveLink,
       "tLagLinkMapProfPortTableLastChgd": tLagLinkMapProfPortTableLastChgd,
       "tLagLinkMapProfPortTable": tLagLinkMapProfPortTable,
       "tLagLinkMapProfPortEntry": tLagLinkMapProfPortEntry,
       "tLagLinkMapProfPortId": tLagLinkMapProfPortId,
       "tLagLinkMapProfPortRowStatus": tLagLinkMapProfPortRowStatus,
       "tLagLinkMapProfPortLastChanged": tLagLinkMapProfPortLastChanged,
       "tLagLinkMapProfPortType": tLagLinkMapProfPortType,
       "tLagPerLinkHashWtPortClassTable": tLagPerLinkHashWtPortClassTable,
       "tLagPerLinkHashWtPortClassEntry": tLagPerLinkHashWtPortClassEntry,
       "tLagPerLinkHashWtPort": tLagPerLinkHashWtPort,
       "tLagPerLinkHashWtPortClassId": tLagPerLinkHashWtPortClassId,
       "tLagPerLinkHashWtPortClassUsers": tLagPerLinkHashWtPortClassUsers,
       "tLagPerLinkHashWtPortClassAggWt": tLagPerLinkHashWtPortClassAggWt,
       "tmnxLagActionTable": tmnxLagActionTable,
       "tmnxLagActionEntry": tmnxLagActionEntry,
       "tmnxLagActionType": tmnxLagActionType,
       "tmnxLagAction": tmnxLagAction,
       "tmnxLagActionClassId": tmnxLagActionClassId,
       "tLagBfdObs": tLagBfdObs,
       "tmnxLagBfdFamTableLastChgd": tmnxLagBfdFamTableLastChgd,
       "tmnxLagBfdFamTable": tmnxLagBfdFamTable,
       "tmnxLagBfdFamEntry": tmnxLagBfdFamEntry,
       "tmnxLagBfdFamAddressType": tmnxLagBfdFamAddressType,
       "tmnxLagBfdFamLastCh": tmnxLagBfdFamLastCh,
       "tmnxLagBfdFamAdminState": tmnxLagBfdFamAdminState,
       "tmnxLagBfdFamAddrType": tmnxLagBfdFamAddrType,
       "tmnxLagBfdFamAddr": tmnxLagBfdFamAddr,
       "tmnxLagBfdFamRemAddrType": tmnxLagBfdFamRemAddrType,
       "tmnxLagBfdFamRemAddr": tmnxLagBfdFamRemAddr,
       "tmnxLagBfdFamTransmitInterval": tmnxLagBfdFamTransmitInterval,
       "tmnxLagBfdFamReceiveInterval": tmnxLagBfdFamReceiveInterval,
       "tmnxLagBfdFamMultiplier": tmnxLagBfdFamMultiplier,
       "tmnxLagBfdFamMaxSetupTime": tmnxLagBfdFamMaxSetupTime,
       "tmnxLagBfdFamMaxAdminDownTime": tmnxLagBfdFamMaxAdminDownTime,
       "tmnxLagBfdFamBfdOnDistributing": tmnxLagBfdFamBfdOnDistributing,
       "tmnxLagBfdMemTable": tmnxLagBfdMemTable,
       "tmnxLagBfdMemEntry": tmnxLagBfdMemEntry,
       "tmnxLagBfdMemState": tmnxLagBfdMemState,
       "tmnxLagBfdMemSetupTimeLeft": tmnxLagBfdMemSetupTimeLeft,
       "tmnxLagBfdMemAdminDownLeft": tmnxLagBfdMemAdminDownLeft,
       "tLagNotifyPrefix": tLagNotifyPrefix,
       "tLagNotifications": tLagNotifications,
       "tLagDynamicCostOn": tLagDynamicCostOn,
       "tLagDynamicCostOff": tLagDynamicCostOff,
       "tLagPortAddFailed": tLagPortAddFailed,
       "tLagSubGroupSelected": tLagSubGroupSelected,
       "tLagPortAddFailureCleared": tLagPortAddFailureCleared,
       "tLagStateEvent": tLagStateEvent,
       "tLagMemberStateEvent": tLagMemberStateEvent,
       "tmnxLagBfdMemStateChanged": tmnxLagBfdMemStateChanged}
)
