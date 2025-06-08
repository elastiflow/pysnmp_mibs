# SNMP MIB module (TIMETRA-ISIS-NG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-ISIS-NG-MIB.mib
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

(SNPAAddress,
 SystemID,
 isisCircIndex,
 isisISAdjEntry,
 isisISAdjIndex,
 isisISAdjState,
 isisManAreaAddrExistState,
 isisSysInstance,
 isisSysL1State,
 isisSysL2State) = mibBuilder.importSymbols(
    "ISIS-MIB",
    "SNPAAddress",
    "SystemID",
    "isisCircIndex",
    "isisISAdjEntry",
    "isisISAdjIndex",
    "isisISAdjState",
    "isisManAreaAddrExistState",
    "isisSysInstance",
    "isisSysL1State",
    "isisSysL2State")

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
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
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

(TNamedItem,
 TNamedItemOrEmpty,
 TmnxAdminState,
 TmnxEnabledDisabled,
 TmnxOperState,
 TmnxReferenceBandwidth,
 TmnxSpbFid) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TmnxAdminState",
    "TmnxEnabledDisabled",
    "TmnxOperState",
    "TmnxReferenceBandwidth",
    "TmnxSpbFid")

(TmnxInetCidrNextHopOwner,
 TmnxInetCidrNextHopType,
 vRtrID,
 vRtrIfIndex) = mibBuilder.importSymbols(
    "TIMETRA-VRTR-MIB",
    "TmnxInetCidrNextHopOwner",
    "TmnxInetCidrNextHopType",
    "vRtrID",
    "vRtrIfIndex")


# MODULE-IDENTITY

timetraIsisNgMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 88)
)
if mibBuilder.loadTexts:
    timetraIsisNgMIBModule.setRevisions(
        ("2013-04-08 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxIsisLSPBuffSize(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(490, 9190),
    )



class TmnxIsisRoutingTopology(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("native", 1),
          ("mt", 2))
    )



# MIB Managed Objects in the order of their OIDs

_TmnxIsisConformance_ObjectIdentity = ObjectIdentity
tmnxIsisConformance = _TmnxIsisConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 88)
)
_TmnxIsisCompliances_ObjectIdentity = ObjectIdentity
tmnxIsisCompliances = _TmnxIsisCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 88, 1)
)
_TmnxIsisGroups_ObjectIdentity = ObjectIdentity
tmnxIsisGroups = _TmnxIsisGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 88, 2)
)
_TmnxIsisObjs_ObjectIdentity = ObjectIdentity
tmnxIsisObjs = _TmnxIsisObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88)
)
_TmnxIsisSystemObjs_ObjectIdentity = ObjectIdentity
tmnxIsisSystemObjs = _TmnxIsisSystemObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1)
)
_TmnxIsisTable_Object = MibTable
tmnxIsisTable = _TmnxIsisTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxIsisTable.setStatus("current")
_TmnxIsisEntry_Object = MibTableRow
tmnxIsisEntry = _TmnxIsisEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1)
)
tmnxIsisEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ISIS-MIB", "isisSysInstance"),
)
if mibBuilder.loadTexts:
    tmnxIsisEntry.setStatus("current")
_TmnxIsisLastEnabledTime_Type = TimeStamp
_TmnxIsisLastEnabledTime_Object = MibTableColumn
tmnxIsisLastEnabledTime = _TmnxIsisLastEnabledTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 1),
    _TmnxIsisLastEnabledTime_Type()
)
tmnxIsisLastEnabledTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisLastEnabledTime.setStatus("current")


class _TmnxIsisAuthKey_Type(OctetString):
    """Custom type tmnxIsisAuthKey based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_TmnxIsisAuthKey_Type.__name__ = "OctetString"
_TmnxIsisAuthKey_Object = MibTableColumn
tmnxIsisAuthKey = _TmnxIsisAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 2),
    _TmnxIsisAuthKey_Type()
)
tmnxIsisAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisAuthKey.setStatus("current")


class _TmnxIsisAuthType_Type(Integer32):
    """Custom type tmnxIsisAuthType based on Integer32"""
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
        *(("none", 1),
          ("password", 2),
          ("md5", 3))
    )


_TmnxIsisAuthType_Type.__name__ = "Integer32"
_TmnxIsisAuthType_Object = MibTableColumn
tmnxIsisAuthType = _TmnxIsisAuthType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 3),
    _TmnxIsisAuthType_Type()
)
tmnxIsisAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisAuthType.setStatus("current")


class _TmnxIsisAuthCheck_Type(TruthValue):
    """Custom type tmnxIsisAuthCheck based on TruthValue"""
    defaultValue = 1


_TmnxIsisAuthCheck_Type.__name__ = "TruthValue"
_TmnxIsisAuthCheck_Object = MibTableColumn
tmnxIsisAuthCheck = _TmnxIsisAuthCheck_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 4),
    _TmnxIsisAuthCheck_Type()
)
tmnxIsisAuthCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisAuthCheck.setStatus("current")


class _TmnxIsisExportPolicy1_Type(TNamedItemOrEmpty):
    """Custom type tmnxIsisExportPolicy1 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIsisExportPolicy1_Type.__name__ = "TNamedItemOrEmpty"
_TmnxIsisExportPolicy1_Object = MibTableColumn
tmnxIsisExportPolicy1 = _TmnxIsisExportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 5),
    _TmnxIsisExportPolicy1_Type()
)
tmnxIsisExportPolicy1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisExportPolicy1.setStatus("current")


class _TmnxIsisExportPolicy2_Type(TNamedItemOrEmpty):
    """Custom type tmnxIsisExportPolicy2 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIsisExportPolicy2_Type.__name__ = "TNamedItemOrEmpty"
_TmnxIsisExportPolicy2_Object = MibTableColumn
tmnxIsisExportPolicy2 = _TmnxIsisExportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 6),
    _TmnxIsisExportPolicy2_Type()
)
tmnxIsisExportPolicy2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisExportPolicy2.setStatus("current")


class _TmnxIsisExportPolicy3_Type(TNamedItemOrEmpty):
    """Custom type tmnxIsisExportPolicy3 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIsisExportPolicy3_Type.__name__ = "TNamedItemOrEmpty"
_TmnxIsisExportPolicy3_Object = MibTableColumn
tmnxIsisExportPolicy3 = _TmnxIsisExportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 7),
    _TmnxIsisExportPolicy3_Type()
)
tmnxIsisExportPolicy3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisExportPolicy3.setStatus("current")


class _TmnxIsisExportPolicy4_Type(TNamedItemOrEmpty):
    """Custom type tmnxIsisExportPolicy4 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIsisExportPolicy4_Type.__name__ = "TNamedItemOrEmpty"
_TmnxIsisExportPolicy4_Object = MibTableColumn
tmnxIsisExportPolicy4 = _TmnxIsisExportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 8),
    _TmnxIsisExportPolicy4_Type()
)
tmnxIsisExportPolicy4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisExportPolicy4.setStatus("current")


class _TmnxIsisExportPolicy5_Type(TNamedItemOrEmpty):
    """Custom type tmnxIsisExportPolicy5 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIsisExportPolicy5_Type.__name__ = "TNamedItemOrEmpty"
_TmnxIsisExportPolicy5_Object = MibTableColumn
tmnxIsisExportPolicy5 = _TmnxIsisExportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 9),
    _TmnxIsisExportPolicy5_Type()
)
tmnxIsisExportPolicy5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisExportPolicy5.setStatus("current")


class _TmnxIsisLspLifetime_Type(Unsigned32):
    """Custom type tmnxIsisLspLifetime based on Unsigned32"""
    defaultValue = 1200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(350, 65535),
    )


_TmnxIsisLspLifetime_Type.__name__ = "Unsigned32"
_TmnxIsisLspLifetime_Object = MibTableColumn
tmnxIsisLspLifetime = _TmnxIsisLspLifetime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 10),
    _TmnxIsisLspLifetime_Type()
)
tmnxIsisLspLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLspLifetime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIsisLspLifetime.setUnits("seconds")


class _TmnxIsisOverloadTimeout_Type(Unsigned32):
    """Custom type tmnxIsisOverloadTimeout based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 1800),
    )


_TmnxIsisOverloadTimeout_Type.__name__ = "Unsigned32"
_TmnxIsisOverloadTimeout_Object = MibTableColumn
tmnxIsisOverloadTimeout = _TmnxIsisOverloadTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 11),
    _TmnxIsisOverloadTimeout_Type()
)
tmnxIsisOverloadTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisOverloadTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIsisOverloadTimeout.setUnits("seconds")
_TmnxIsisOperState_Type = TmnxOperState
_TmnxIsisOperState_Object = MibTableColumn
tmnxIsisOperState = _TmnxIsisOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 12),
    _TmnxIsisOperState_Type()
)
tmnxIsisOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisOperState.setStatus("current")


class _TmnxIsisReferenceBw_Type(TmnxReferenceBandwidth):
    """Custom type tmnxIsisReferenceBw based on TmnxReferenceBandwidth"""
    defaultValue = 0


_TmnxIsisReferenceBw_Type.__name__ = "TmnxReferenceBandwidth"
_TmnxIsisReferenceBw_Object = MibTableColumn
tmnxIsisReferenceBw = _TmnxIsisReferenceBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 13),
    _TmnxIsisReferenceBw_Type()
)
tmnxIsisReferenceBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisReferenceBw.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIsisReferenceBw.setUnits("kilobits per second")


class _TmnxIsisTrafficEng_Type(TruthValue):
    """Custom type tmnxIsisTrafficEng based on TruthValue"""
    defaultValue = 2


_TmnxIsisTrafficEng_Type.__name__ = "TruthValue"
_TmnxIsisTrafficEng_Object = MibTableColumn
tmnxIsisTrafficEng = _TmnxIsisTrafficEng_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 14),
    _TmnxIsisTrafficEng_Type()
)
tmnxIsisTrafficEng.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisTrafficEng.setStatus("current")
_TmnxIsisShortCuts_Type = TruthValue
_TmnxIsisShortCuts_Object = MibTableColumn
tmnxIsisShortCuts = _TmnxIsisShortCuts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 15),
    _TmnxIsisShortCuts_Type()
)
tmnxIsisShortCuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisShortCuts.setStatus("current")


class _TmnxIsisSpfHoldTime_Type(Integer32):
    """Custom type tmnxIsisSpfHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TmnxIsisSpfHoldTime_Type.__name__ = "Integer32"
_TmnxIsisSpfHoldTime_Object = MibTableColumn
tmnxIsisSpfHoldTime = _TmnxIsisSpfHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 16),
    _TmnxIsisSpfHoldTime_Type()
)
tmnxIsisSpfHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisSpfHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIsisSpfHoldTime.setUnits("seconds")
_TmnxIsisLastSpfRun_Type = TimeStamp
_TmnxIsisLastSpfRun_Object = MibTableColumn
tmnxIsisLastSpfRun = _TmnxIsisLastSpfRun_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 17),
    _TmnxIsisLastSpfRun_Type()
)
tmnxIsisLastSpfRun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisLastSpfRun.setStatus("current")


class _TmnxIsisGracefulRestart_Type(TruthValue):
    """Custom type tmnxIsisGracefulRestart based on TruthValue"""
    defaultValue = 2


_TmnxIsisGracefulRestart_Type.__name__ = "TruthValue"
_TmnxIsisGracefulRestart_Object = MibTableColumn
tmnxIsisGracefulRestart = _TmnxIsisGracefulRestart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 18),
    _TmnxIsisGracefulRestart_Type()
)
tmnxIsisGracefulRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisGracefulRestart.setStatus("current")


class _TmnxIsisOverloadOnBoot_Type(Integer32):
    """Custom type tmnxIsisOverloadOnBoot based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_TmnxIsisOverloadOnBoot_Type.__name__ = "Integer32"
_TmnxIsisOverloadOnBoot_Object = MibTableColumn
tmnxIsisOverloadOnBoot = _TmnxIsisOverloadOnBoot_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 19),
    _TmnxIsisOverloadOnBoot_Type()
)
tmnxIsisOverloadOnBoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisOverloadOnBoot.setStatus("current")


class _TmnxIsisOverloadOnBootTimeout_Type(Unsigned32):
    """Custom type tmnxIsisOverloadOnBootTimeout based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 1800),
    )


_TmnxIsisOverloadOnBootTimeout_Type.__name__ = "Unsigned32"
_TmnxIsisOverloadOnBootTimeout_Object = MibTableColumn
tmnxIsisOverloadOnBootTimeout = _TmnxIsisOverloadOnBootTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 20),
    _TmnxIsisOverloadOnBootTimeout_Type()
)
tmnxIsisOverloadOnBootTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisOverloadOnBootTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIsisOverloadOnBootTimeout.setUnits("seconds")


class _TmnxIsisSpfWait_Type(Unsigned32):
    """Custom type tmnxIsisSpfWait based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_TmnxIsisSpfWait_Type.__name__ = "Unsigned32"
_TmnxIsisSpfWait_Object = MibTableColumn
tmnxIsisSpfWait = _TmnxIsisSpfWait_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 21),
    _TmnxIsisSpfWait_Type()
)
tmnxIsisSpfWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisSpfWait.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIsisSpfWait.setUnits("seconds")


class _TmnxIsisSpfInitialWait_Type(Unsigned32):
    """Custom type tmnxIsisSpfInitialWait based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100000),
    )


_TmnxIsisSpfInitialWait_Type.__name__ = "Unsigned32"
_TmnxIsisSpfInitialWait_Object = MibTableColumn
tmnxIsisSpfInitialWait = _TmnxIsisSpfInitialWait_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 22),
    _TmnxIsisSpfInitialWait_Type()
)
tmnxIsisSpfInitialWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisSpfInitialWait.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIsisSpfInitialWait.setUnits("milliseconds")


class _TmnxIsisSpfSecondWait_Type(Unsigned32):
    """Custom type tmnxIsisSpfSecondWait based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_TmnxIsisSpfSecondWait_Type.__name__ = "Unsigned32"
_TmnxIsisSpfSecondWait_Object = MibTableColumn
tmnxIsisSpfSecondWait = _TmnxIsisSpfSecondWait_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 23),
    _TmnxIsisSpfSecondWait_Type()
)
tmnxIsisSpfSecondWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisSpfSecondWait.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIsisSpfSecondWait.setUnits("milliseconds")


class _TmnxIsisLspMaxWait_Type(Unsigned32):
    """Custom type tmnxIsisLspMaxWait based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_TmnxIsisLspMaxWait_Type.__name__ = "Unsigned32"
_TmnxIsisLspMaxWait_Object = MibTableColumn
tmnxIsisLspMaxWait = _TmnxIsisLspMaxWait_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 24),
    _TmnxIsisLspMaxWait_Type()
)
tmnxIsisLspMaxWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLspMaxWait.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIsisLspMaxWait.setUnits("seconds")


class _TmnxIsisLspInitialWait_Type(Unsigned32):
    """Custom type tmnxIsisLspInitialWait based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxIsisLspInitialWait_Type.__name__ = "Unsigned32"
_TmnxIsisLspInitialWait_Object = MibTableColumn
tmnxIsisLspInitialWait = _TmnxIsisLspInitialWait_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 25),
    _TmnxIsisLspInitialWait_Type()
)
tmnxIsisLspInitialWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLspInitialWait.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIsisLspInitialWait.setUnits("seconds")


class _TmnxIsisLspSecondWait_Type(Unsigned32):
    """Custom type tmnxIsisLspSecondWait based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_TmnxIsisLspSecondWait_Type.__name__ = "Unsigned32"
_TmnxIsisLspSecondWait_Object = MibTableColumn
tmnxIsisLspSecondWait = _TmnxIsisLspSecondWait_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 26),
    _TmnxIsisLspSecondWait_Type()
)
tmnxIsisLspSecondWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLspSecondWait.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIsisLspSecondWait.setUnits("seconds")


class _TmnxIsisCsnpAuthentication_Type(TruthValue):
    """Custom type tmnxIsisCsnpAuthentication based on TruthValue"""
    defaultValue = 1


_TmnxIsisCsnpAuthentication_Type.__name__ = "TruthValue"
_TmnxIsisCsnpAuthentication_Object = MibTableColumn
tmnxIsisCsnpAuthentication = _TmnxIsisCsnpAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 27),
    _TmnxIsisCsnpAuthentication_Type()
)
tmnxIsisCsnpAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisCsnpAuthentication.setStatus("current")


class _TmnxIsisHelloAuthentication_Type(TruthValue):
    """Custom type tmnxIsisHelloAuthentication based on TruthValue"""
    defaultValue = 1


_TmnxIsisHelloAuthentication_Type.__name__ = "TruthValue"
_TmnxIsisHelloAuthentication_Object = MibTableColumn
tmnxIsisHelloAuthentication = _TmnxIsisHelloAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 28),
    _TmnxIsisHelloAuthentication_Type()
)
tmnxIsisHelloAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisHelloAuthentication.setStatus("current")


class _TmnxIsisPsnpAuthentication_Type(TruthValue):
    """Custom type tmnxIsisPsnpAuthentication based on TruthValue"""
    defaultValue = 1


_TmnxIsisPsnpAuthentication_Type.__name__ = "TruthValue"
_TmnxIsisPsnpAuthentication_Object = MibTableColumn
tmnxIsisPsnpAuthentication = _TmnxIsisPsnpAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 29),
    _TmnxIsisPsnpAuthentication_Type()
)
tmnxIsisPsnpAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisPsnpAuthentication.setStatus("current")


class _TmnxIsisGRHelperMode_Type(TruthValue):
    """Custom type tmnxIsisGRHelperMode based on TruthValue"""
    defaultValue = 2


_TmnxIsisGRHelperMode_Type.__name__ = "TruthValue"
_TmnxIsisGRHelperMode_Object = MibTableColumn
tmnxIsisGRHelperMode = _TmnxIsisGRHelperMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 30),
    _TmnxIsisGRHelperMode_Type()
)
tmnxIsisGRHelperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisGRHelperMode.setStatus("current")


class _TmnxIsisEnableIPv4_Type(TruthValue):
    """Custom type tmnxIsisEnableIPv4 based on TruthValue"""
    defaultValue = 1


_TmnxIsisEnableIPv4_Type.__name__ = "TruthValue"
_TmnxIsisEnableIPv4_Object = MibTableColumn
tmnxIsisEnableIPv4 = _TmnxIsisEnableIPv4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 31),
    _TmnxIsisEnableIPv4_Type()
)
tmnxIsisEnableIPv4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisEnableIPv4.setStatus("current")


class _TmnxIsisUnicastImport_Type(TruthValue):
    """Custom type tmnxIsisUnicastImport based on TruthValue"""
    defaultValue = 1


_TmnxIsisUnicastImport_Type.__name__ = "TruthValue"
_TmnxIsisUnicastImport_Object = MibTableColumn
tmnxIsisUnicastImport = _TmnxIsisUnicastImport_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 32),
    _TmnxIsisUnicastImport_Type()
)
tmnxIsisUnicastImport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisUnicastImport.setStatus("current")


class _TmnxIsisMulticastImport_Type(TruthValue):
    """Custom type tmnxIsisMulticastImport based on TruthValue"""
    defaultValue = 2


_TmnxIsisMulticastImport_Type.__name__ = "TruthValue"
_TmnxIsisMulticastImport_Object = MibTableColumn
tmnxIsisMulticastImport = _TmnxIsisMulticastImport_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 33),
    _TmnxIsisMulticastImport_Type()
)
tmnxIsisMulticastImport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisMulticastImport.setStatus("current")


class _TmnxIsisStrictAdjacencyCheck_Type(TruthValue):
    """Custom type tmnxIsisStrictAdjacencyCheck based on TruthValue"""
    defaultValue = 2


_TmnxIsisStrictAdjacencyCheck_Type.__name__ = "TruthValue"
_TmnxIsisStrictAdjacencyCheck_Object = MibTableColumn
tmnxIsisStrictAdjacencyCheck = _TmnxIsisStrictAdjacencyCheck_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 34),
    _TmnxIsisStrictAdjacencyCheck_Type()
)
tmnxIsisStrictAdjacencyCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisStrictAdjacencyCheck.setStatus("current")


class _TmnxIsisManualSpfTrigger_Type(Integer32):
    """Custom type tmnxIsisManualSpfTrigger based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("runTotalSpf", 2))
    )


_TmnxIsisManualSpfTrigger_Type.__name__ = "Integer32"
_TmnxIsisManualSpfTrigger_Object = MibTableColumn
tmnxIsisManualSpfTrigger = _TmnxIsisManualSpfTrigger_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 35),
    _TmnxIsisManualSpfTrigger_Type()
)
tmnxIsisManualSpfTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisManualSpfTrigger.setStatus("current")


class _TmnxIsisMultiTopology_Type(TruthValue):
    """Custom type tmnxIsisMultiTopology based on TruthValue"""
    defaultValue = 2


_TmnxIsisMultiTopology_Type.__name__ = "TruthValue"
_TmnxIsisMultiTopology_Object = MibTableColumn
tmnxIsisMultiTopology = _TmnxIsisMultiTopology_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 36),
    _TmnxIsisMultiTopology_Type()
)
tmnxIsisMultiTopology.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisMultiTopology.setStatus("current")


class _TmnxIsisMultiTopoIPv6Ucast_Type(TruthValue):
    """Custom type tmnxIsisMultiTopoIPv6Ucast based on TruthValue"""
    defaultValue = 2


_TmnxIsisMultiTopoIPv6Ucast_Type.__name__ = "TruthValue"
_TmnxIsisMultiTopoIPv6Ucast_Object = MibTableColumn
tmnxIsisMultiTopoIPv6Ucast = _TmnxIsisMultiTopoIPv6Ucast_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 37),
    _TmnxIsisMultiTopoIPv6Ucast_Type()
)
tmnxIsisMultiTopoIPv6Ucast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisMultiTopoIPv6Ucast.setStatus("current")


class _TmnxIsisIPv6RoutingTopo_Type(Integer32):
    """Custom type tmnxIsisIPv6RoutingTopo based on Integer32"""
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
        *(("none", 0),
          ("native", 1),
          ("mt", 2))
    )


_TmnxIsisIPv6RoutingTopo_Type.__name__ = "Integer32"
_TmnxIsisIPv6RoutingTopo_Object = MibTableColumn
tmnxIsisIPv6RoutingTopo = _TmnxIsisIPv6RoutingTopo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 38),
    _TmnxIsisIPv6RoutingTopo_Type()
)
tmnxIsisIPv6RoutingTopo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisIPv6RoutingTopo.setStatus("current")


class _TmnxIsisSysOrigL1LSPBuffSize_Type(TmnxIsisLSPBuffSize):
    """Custom type tmnxIsisSysOrigL1LSPBuffSize based on TmnxIsisLSPBuffSize"""
    defaultValue = 1492


_TmnxIsisSysOrigL1LSPBuffSize_Type.__name__ = "TmnxIsisLSPBuffSize"
_TmnxIsisSysOrigL1LSPBuffSize_Object = MibTableColumn
tmnxIsisSysOrigL1LSPBuffSize = _TmnxIsisSysOrigL1LSPBuffSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 39),
    _TmnxIsisSysOrigL1LSPBuffSize_Type()
)
tmnxIsisSysOrigL1LSPBuffSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisSysOrigL1LSPBuffSize.setStatus("current")


class _TmnxIsisSysOrigL2LSPBuffSize_Type(TmnxIsisLSPBuffSize):
    """Custom type tmnxIsisSysOrigL2LSPBuffSize based on TmnxIsisLSPBuffSize"""
    defaultValue = 1492


_TmnxIsisSysOrigL2LSPBuffSize_Type.__name__ = "TmnxIsisLSPBuffSize"
_TmnxIsisSysOrigL2LSPBuffSize_Object = MibTableColumn
tmnxIsisSysOrigL2LSPBuffSize = _TmnxIsisSysOrigL2LSPBuffSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 40),
    _TmnxIsisSysOrigL2LSPBuffSize_Type()
)
tmnxIsisSysOrigL2LSPBuffSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisSysOrigL2LSPBuffSize.setStatus("current")


class _TmnxIsisLdpSyncAdminState_Type(TruthValue):
    """Custom type tmnxIsisLdpSyncAdminState based on TruthValue"""
    defaultValue = 1


_TmnxIsisLdpSyncAdminState_Type.__name__ = "TruthValue"
_TmnxIsisLdpSyncAdminState_Object = MibTableColumn
tmnxIsisLdpSyncAdminState = _TmnxIsisLdpSyncAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 41),
    _TmnxIsisLdpSyncAdminState_Type()
)
tmnxIsisLdpSyncAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLdpSyncAdminState.setStatus("current")


class _TmnxIsisIPv6UnicastImport_Type(TruthValue):
    """Custom type tmnxIsisIPv6UnicastImport based on TruthValue"""
    defaultValue = 1


_TmnxIsisIPv6UnicastImport_Type.__name__ = "TruthValue"
_TmnxIsisIPv6UnicastImport_Object = MibTableColumn
tmnxIsisIPv6UnicastImport = _TmnxIsisIPv6UnicastImport_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 42),
    _TmnxIsisIPv6UnicastImport_Type()
)
tmnxIsisIPv6UnicastImport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisIPv6UnicastImport.setStatus("current")


class _TmnxIsisIPv6MulticastImport_Type(TruthValue):
    """Custom type tmnxIsisIPv6MulticastImport based on TruthValue"""
    defaultValue = 2


_TmnxIsisIPv6MulticastImport_Type.__name__ = "TruthValue"
_TmnxIsisIPv6MulticastImport_Object = MibTableColumn
tmnxIsisIPv6MulticastImport = _TmnxIsisIPv6MulticastImport_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 43),
    _TmnxIsisIPv6MulticastImport_Type()
)
tmnxIsisIPv6MulticastImport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisIPv6MulticastImport.setStatus("current")


class _TmnxIsisAdvertisePassiveOnly_Type(TruthValue):
    """Custom type tmnxIsisAdvertisePassiveOnly based on TruthValue"""
    defaultValue = 2


_TmnxIsisAdvertisePassiveOnly_Type.__name__ = "TruthValue"
_TmnxIsisAdvertisePassiveOnly_Object = MibTableColumn
tmnxIsisAdvertisePassiveOnly = _TmnxIsisAdvertisePassiveOnly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 44),
    _TmnxIsisAdvertisePassiveOnly_Type()
)
tmnxIsisAdvertisePassiveOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisAdvertisePassiveOnly.setStatus("current")


class _TmnxIsisDefaultRouteTag_Type(Unsigned32):
    """Custom type tmnxIsisDefaultRouteTag based on Unsigned32"""
    defaultValue = 0


_TmnxIsisDefaultRouteTag_Type.__name__ = "Unsigned32"
_TmnxIsisDefaultRouteTag_Object = MibTableColumn
tmnxIsisDefaultRouteTag = _TmnxIsisDefaultRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 45),
    _TmnxIsisDefaultRouteTag_Type()
)
tmnxIsisDefaultRouteTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisDefaultRouteTag.setStatus("current")


class _TmnxIsisSuppressDefault_Type(TruthValue):
    """Custom type tmnxIsisSuppressDefault based on TruthValue"""
    defaultValue = 2


_TmnxIsisSuppressDefault_Type.__name__ = "TruthValue"
_TmnxIsisSuppressDefault_Object = MibTableColumn
tmnxIsisSuppressDefault = _TmnxIsisSuppressDefault_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 46),
    _TmnxIsisSuppressDefault_Type()
)
tmnxIsisSuppressDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisSuppressDefault.setStatus("current")


class _TmnxIsisLdpOverRsvp_Type(TmnxEnabledDisabled):
    """Custom type tmnxIsisLdpOverRsvp based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxIsisLdpOverRsvp_Type.__name__ = "TmnxEnabledDisabled"
_TmnxIsisLdpOverRsvp_Object = MibTableColumn
tmnxIsisLdpOverRsvp = _TmnxIsisLdpOverRsvp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 47),
    _TmnxIsisLdpOverRsvp_Type()
)
tmnxIsisLdpOverRsvp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLdpOverRsvp.setStatus("current")


class _TmnxIsisExportLimit_Type(Unsigned32):
    """Custom type tmnxIsisExportLimit based on Unsigned32"""
    defaultValue = 0


_TmnxIsisExportLimit_Type.__name__ = "Unsigned32"
_TmnxIsisExportLimit_Object = MibTableColumn
tmnxIsisExportLimit = _TmnxIsisExportLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 48),
    _TmnxIsisExportLimit_Type()
)
tmnxIsisExportLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisExportLimit.setStatus("current")


class _TmnxIsisExportLimitLogPercent_Type(Unsigned32):
    """Custom type tmnxIsisExportLimitLogPercent based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxIsisExportLimitLogPercent_Type.__name__ = "Unsigned32"
_TmnxIsisExportLimitLogPercent_Object = MibTableColumn
tmnxIsisExportLimitLogPercent = _TmnxIsisExportLimitLogPercent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 49),
    _TmnxIsisExportLimitLogPercent_Type()
)
tmnxIsisExportLimitLogPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisExportLimitLogPercent.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIsisExportLimitLogPercent.setUnits("percentage")
_TmnxIsisTotalL1ExportedRoutes_Type = Gauge32
_TmnxIsisTotalL1ExportedRoutes_Object = MibTableColumn
tmnxIsisTotalL1ExportedRoutes = _TmnxIsisTotalL1ExportedRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 50),
    _TmnxIsisTotalL1ExportedRoutes_Type()
)
tmnxIsisTotalL1ExportedRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisTotalL1ExportedRoutes.setStatus("current")
_TmnxIsisTotalL2ExportedRoutes_Type = Gauge32
_TmnxIsisTotalL2ExportedRoutes_Object = MibTableColumn
tmnxIsisTotalL2ExportedRoutes = _TmnxIsisTotalL2ExportedRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 51),
    _TmnxIsisTotalL2ExportedRoutes_Type()
)
tmnxIsisTotalL2ExportedRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisTotalL2ExportedRoutes.setStatus("current")


class _TmnxIsisRsvpShortcut_Type(TruthValue):
    """Custom type tmnxIsisRsvpShortcut based on TruthValue"""
    defaultValue = 2


_TmnxIsisRsvpShortcut_Type.__name__ = "TruthValue"
_TmnxIsisRsvpShortcut_Object = MibTableColumn
tmnxIsisRsvpShortcut = _TmnxIsisRsvpShortcut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 52),
    _TmnxIsisRsvpShortcut_Type()
)
tmnxIsisRsvpShortcut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisRsvpShortcut.setStatus("current")


class _TmnxIsisAdvertiseTunnelLink_Type(TruthValue):
    """Custom type tmnxIsisAdvertiseTunnelLink based on TruthValue"""
    defaultValue = 2


_TmnxIsisAdvertiseTunnelLink_Type.__name__ = "TruthValue"
_TmnxIsisAdvertiseTunnelLink_Object = MibTableColumn
tmnxIsisAdvertiseTunnelLink = _TmnxIsisAdvertiseTunnelLink_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 53),
    _TmnxIsisAdvertiseTunnelLink_Type()
)
tmnxIsisAdvertiseTunnelLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisAdvertiseTunnelLink.setStatus("current")


class _TmnxIsisIidTlv_Type(TmnxEnabledDisabled):
    """Custom type tmnxIsisIidTlv based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxIsisIidTlv_Type.__name__ = "TmnxEnabledDisabled"
_TmnxIsisIidTlv_Object = MibTableColumn
tmnxIsisIidTlv = _TmnxIsisIidTlv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 54),
    _TmnxIsisIidTlv_Type()
)
tmnxIsisIidTlv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisIidTlv.setStatus("current")


class _TmnxIsisL1MacAddress_Type(MacAddress):
    """Custom type tmnxIsisL1MacAddress based on MacAddress"""
    defaultHexValue = "0180C2000014"


_TmnxIsisL1MacAddress_Type.__name__ = "MacAddress"
_TmnxIsisL1MacAddress_Object = MibTableColumn
tmnxIsisL1MacAddress = _TmnxIsisL1MacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 55),
    _TmnxIsisL1MacAddress_Type()
)
tmnxIsisL1MacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisL1MacAddress.setStatus("current")


class _TmnxIsisL2MacAddress_Type(MacAddress):
    """Custom type tmnxIsisL2MacAddress based on MacAddress"""
    defaultHexValue = "0180C2000015"


_TmnxIsisL2MacAddress_Type.__name__ = "MacAddress"
_TmnxIsisL2MacAddress_Object = MibTableColumn
tmnxIsisL2MacAddress = _TmnxIsisL2MacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 56),
    _TmnxIsisL2MacAddress_Type()
)
tmnxIsisL2MacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisL2MacAddress.setStatus("current")
_TmnxIsisSysOperL1LSPBuffSize_Type = TmnxIsisLSPBuffSize
_TmnxIsisSysOperL1LSPBuffSize_Object = MibTableColumn
tmnxIsisSysOperL1LSPBuffSize = _TmnxIsisSysOperL1LSPBuffSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 57),
    _TmnxIsisSysOperL1LSPBuffSize_Type()
)
tmnxIsisSysOperL1LSPBuffSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisSysOperL1LSPBuffSize.setStatus("current")
_TmnxIsisSysOperL2LSPBuffSize_Type = TmnxIsisLSPBuffSize
_TmnxIsisSysOperL2LSPBuffSize_Object = MibTableColumn
tmnxIsisSysOperL2LSPBuffSize = _TmnxIsisSysOperL2LSPBuffSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 58),
    _TmnxIsisSysOperL2LSPBuffSize_Type()
)
tmnxIsisSysOperL2LSPBuffSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisSysOperL2LSPBuffSize.setStatus("current")


class _TmnxIsisLoopfreeAlternate_Type(TruthValue):
    """Custom type tmnxIsisLoopfreeAlternate based on TruthValue"""
    defaultValue = 2


_TmnxIsisLoopfreeAlternate_Type.__name__ = "TruthValue"
_TmnxIsisLoopfreeAlternate_Object = MibTableColumn
tmnxIsisLoopfreeAlternate = _TmnxIsisLoopfreeAlternate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 59),
    _TmnxIsisLoopfreeAlternate_Type()
)
tmnxIsisLoopfreeAlternate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLoopfreeAlternate.setStatus("current")


class _TmnxIsisIPv4McastRoutingTopo_Type(TmnxIsisRoutingTopology):
    """Custom type tmnxIsisIPv4McastRoutingTopo based on TmnxIsisRoutingTopology"""
    defaultValue = 1


_TmnxIsisIPv4McastRoutingTopo_Type.__name__ = "TmnxIsisRoutingTopology"
_TmnxIsisIPv4McastRoutingTopo_Object = MibTableColumn
tmnxIsisIPv4McastRoutingTopo = _TmnxIsisIPv4McastRoutingTopo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 60),
    _TmnxIsisIPv4McastRoutingTopo_Type()
)
tmnxIsisIPv4McastRoutingTopo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisIPv4McastRoutingTopo.setStatus("current")


class _TmnxIsisIPv6McastRoutingTopo_Type(TmnxIsisRoutingTopology):
    """Custom type tmnxIsisIPv6McastRoutingTopo based on TmnxIsisRoutingTopology"""
    defaultValue = 1


_TmnxIsisIPv6McastRoutingTopo_Type.__name__ = "TmnxIsisRoutingTopology"
_TmnxIsisIPv6McastRoutingTopo_Object = MibTableColumn
tmnxIsisIPv6McastRoutingTopo = _TmnxIsisIPv6McastRoutingTopo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 61),
    _TmnxIsisIPv6McastRoutingTopo_Type()
)
tmnxIsisIPv6McastRoutingTopo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisIPv6McastRoutingTopo.setStatus("current")


class _TmnxIsisMultiTopoIPv4Mcast_Type(TruthValue):
    """Custom type tmnxIsisMultiTopoIPv4Mcast based on TruthValue"""
    defaultValue = 2


_TmnxIsisMultiTopoIPv4Mcast_Type.__name__ = "TruthValue"
_TmnxIsisMultiTopoIPv4Mcast_Object = MibTableColumn
tmnxIsisMultiTopoIPv4Mcast = _TmnxIsisMultiTopoIPv4Mcast_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 62),
    _TmnxIsisMultiTopoIPv4Mcast_Type()
)
tmnxIsisMultiTopoIPv4Mcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisMultiTopoIPv4Mcast.setStatus("current")


class _TmnxIsisMultiTopoIPv6Mcast_Type(TruthValue):
    """Custom type tmnxIsisMultiTopoIPv6Mcast based on TruthValue"""
    defaultValue = 2


_TmnxIsisMultiTopoIPv6Mcast_Type.__name__ = "TruthValue"
_TmnxIsisMultiTopoIPv6Mcast_Object = MibTableColumn
tmnxIsisMultiTopoIPv6Mcast = _TmnxIsisMultiTopoIPv6Mcast_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 63),
    _TmnxIsisMultiTopoIPv6Mcast_Type()
)
tmnxIsisMultiTopoIPv6Mcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisMultiTopoIPv6Mcast.setStatus("current")


class _TmnxIsisOverloadMaxMetric_Type(TruthValue):
    """Custom type tmnxIsisOverloadMaxMetric based on TruthValue"""
    defaultValue = 2


_TmnxIsisOverloadMaxMetric_Type.__name__ = "TruthValue"
_TmnxIsisOverloadMaxMetric_Object = MibTableColumn
tmnxIsisOverloadMaxMetric = _TmnxIsisOverloadMaxMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 64),
    _TmnxIsisOverloadMaxMetric_Type()
)
tmnxIsisOverloadMaxMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisOverloadMaxMetric.setStatus("current")


class _TmnxIsisOverloadOnBootMaxMetric_Type(TruthValue):
    """Custom type tmnxIsisOverloadOnBootMaxMetric based on TruthValue"""
    defaultValue = 2


_TmnxIsisOverloadOnBootMaxMetric_Type.__name__ = "TruthValue"
_TmnxIsisOverloadOnBootMaxMetric_Object = MibTableColumn
tmnxIsisOverloadOnBootMaxMetric = _TmnxIsisOverloadOnBootMaxMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 65),
    _TmnxIsisOverloadOnBootMaxMetric_Type()
)
tmnxIsisOverloadOnBootMaxMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisOverloadOnBootMaxMetric.setStatus("current")


class _TmnxIsisRouterId_Type(Unsigned32):
    """Custom type tmnxIsisRouterId based on Unsigned32"""
    defaultValue = 0


_TmnxIsisRouterId_Type.__name__ = "Unsigned32"
_TmnxIsisRouterId_Object = MibTableColumn
tmnxIsisRouterId = _TmnxIsisRouterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 66),
    _TmnxIsisRouterId_Type()
)
tmnxIsisRouterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisRouterId.setStatus("current")


class _TmnxIsisAdvRtrCapability_Type(Integer32):
    """Custom type tmnxIsisAdvRtrCapability based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("area", 2),
          ("as", 3))
    )


_TmnxIsisAdvRtrCapability_Type.__name__ = "Integer32"
_TmnxIsisAdvRtrCapability_Object = MibTableColumn
tmnxIsisAdvRtrCapability = _TmnxIsisAdvRtrCapability_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 67),
    _TmnxIsisAdvRtrCapability_Type()
)
tmnxIsisAdvRtrCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisAdvRtrCapability.setStatus("current")


class _TmnxIsisHelloPadding_Type(Integer32):
    """Custom type tmnxIsisHelloPadding based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("adaptive", 1),
          ("loose", 2),
          ("strict", 3))
    )


_TmnxIsisHelloPadding_Type.__name__ = "Integer32"
_TmnxIsisHelloPadding_Object = MibTableColumn
tmnxIsisHelloPadding = _TmnxIsisHelloPadding_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 68),
    _TmnxIsisHelloPadding_Type()
)
tmnxIsisHelloPadding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisHelloPadding.setStatus("current")


class _TmnxIsisLspRefreshInterval_Type(Unsigned32):
    """Custom type tmnxIsisLspRefreshInterval based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(150, 65535),
    )


_TmnxIsisLspRefreshInterval_Type.__name__ = "Unsigned32"
_TmnxIsisLspRefreshInterval_Object = MibTableColumn
tmnxIsisLspRefreshInterval = _TmnxIsisLspRefreshInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 69),
    _TmnxIsisLspRefreshInterval_Type()
)
tmnxIsisLspRefreshInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLspRefreshInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIsisLspRefreshInterval.setUnits("seconds")
_TmnxIsisOperRouterId_Type = Unsigned32
_TmnxIsisOperRouterId_Object = MibTableColumn
tmnxIsisOperRouterId = _TmnxIsisOperRouterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 70),
    _TmnxIsisOperRouterId_Type()
)
tmnxIsisOperRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisOperRouterId.setStatus("current")


class _TmnxIsisAuthKeyChain_Type(TNamedItemOrEmpty):
    """Custom type tmnxIsisAuthKeyChain based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIsisAuthKeyChain_Type.__name__ = "TNamedItemOrEmpty"
_TmnxIsisAuthKeyChain_Object = MibTableColumn
tmnxIsisAuthKeyChain = _TmnxIsisAuthKeyChain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 71),
    _TmnxIsisAuthKeyChain_Type()
)
tmnxIsisAuthKeyChain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisAuthKeyChain.setStatus("current")


class _TmnxIsisIgnoreLspErrors_Type(TruthValue):
    """Custom type tmnxIsisIgnoreLspErrors based on TruthValue"""
    defaultValue = 2


_TmnxIsisIgnoreLspErrors_Type.__name__ = "TruthValue"
_TmnxIsisIgnoreLspErrors_Object = MibTableColumn
tmnxIsisIgnoreLspErrors = _TmnxIsisIgnoreLspErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 72),
    _TmnxIsisIgnoreLspErrors_Type()
)
tmnxIsisIgnoreLspErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisIgnoreLspErrors.setStatus("current")
_TmnxIsisLevelTable_Object = MibTable
tmnxIsisLevelTable = _TmnxIsisLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 2)
)
if mibBuilder.loadTexts:
    tmnxIsisLevelTable.setStatus("current")
_TmnxIsisLevelEntry_Object = MibTableRow
tmnxIsisLevelEntry = _TmnxIsisLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 2, 1)
)
tmnxIsisLevelEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisLevel"),
)
if mibBuilder.loadTexts:
    tmnxIsisLevelEntry.setStatus("current")


class _TmnxIsisLevel_Type(Integer32):
    """Custom type tmnxIsisLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("level1", 1),
          ("level2", 2))
    )


_TmnxIsisLevel_Type.__name__ = "Integer32"
_TmnxIsisLevel_Object = MibTableColumn
tmnxIsisLevel = _TmnxIsisLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 2, 1, 1),
    _TmnxIsisLevel_Type()
)
tmnxIsisLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisLevel.setStatus("current")


class _TmnxIsisLevelAuthKey_Type(OctetString):
    """Custom type tmnxIsisLevelAuthKey based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_TmnxIsisLevelAuthKey_Type.__name__ = "OctetString"
_TmnxIsisLevelAuthKey_Object = MibTableColumn
tmnxIsisLevelAuthKey = _TmnxIsisLevelAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 2, 1, 2),
    _TmnxIsisLevelAuthKey_Type()
)
tmnxIsisLevelAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLevelAuthKey.setStatus("current")


class _TmnxIsisLevelAuthType_Type(Integer32):
    """Custom type tmnxIsisLevelAuthType based on Integer32"""
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
        *(("none", 1),
          ("password", 2),
          ("md5", 3))
    )


_TmnxIsisLevelAuthType_Type.__name__ = "Integer32"
_TmnxIsisLevelAuthType_Object = MibTableColumn
tmnxIsisLevelAuthType = _TmnxIsisLevelAuthType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 2, 1, 3),
    _TmnxIsisLevelAuthType_Type()
)
tmnxIsisLevelAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLevelAuthType.setStatus("current")


class _TmnxIsisLevelExtPreference_Type(Unsigned32):
    """Custom type tmnxIsisLevelExtPreference based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TmnxIsisLevelExtPreference_Type.__name__ = "Unsigned32"
_TmnxIsisLevelExtPreference_Object = MibTableColumn
tmnxIsisLevelExtPreference = _TmnxIsisLevelExtPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 2, 1, 4),
    _TmnxIsisLevelExtPreference_Type()
)
tmnxIsisLevelExtPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLevelExtPreference.setStatus("current")


class _TmnxIsisLevelPreference_Type(Unsigned32):
    """Custom type tmnxIsisLevelPreference based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TmnxIsisLevelPreference_Type.__name__ = "Unsigned32"
_TmnxIsisLevelPreference_Object = MibTableColumn
tmnxIsisLevelPreference = _TmnxIsisLevelPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 2, 1, 5),
    _TmnxIsisLevelPreference_Type()
)
tmnxIsisLevelPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLevelPreference.setStatus("current")


class _TmnxIsisLevelWideMetricsOnly_Type(TruthValue):
    """Custom type tmnxIsisLevelWideMetricsOnly based on TruthValue"""
    defaultValue = 2


_TmnxIsisLevelWideMetricsOnly_Type.__name__ = "TruthValue"
_TmnxIsisLevelWideMetricsOnly_Object = MibTableColumn
tmnxIsisLevelWideMetricsOnly = _TmnxIsisLevelWideMetricsOnly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 2, 1, 6),
    _TmnxIsisLevelWideMetricsOnly_Type()
)
tmnxIsisLevelWideMetricsOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLevelWideMetricsOnly.setStatus("current")


class _TmnxIsisLevelOverloadStatus_Type(Integer32):
    """Custom type tmnxIsisLevelOverloadStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("notInOverload", 1),
          ("dynamic", 2),
          ("manual", 3),
          ("manualOnBoot", 4),
          ("singleSfm", 5))
    )


_TmnxIsisLevelOverloadStatus_Type.__name__ = "Integer32"
_TmnxIsisLevelOverloadStatus_Object = MibTableColumn
tmnxIsisLevelOverloadStatus = _TmnxIsisLevelOverloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 2, 1, 7),
    _TmnxIsisLevelOverloadStatus_Type()
)
tmnxIsisLevelOverloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisLevelOverloadStatus.setStatus("current")
_TmnxIsisLevelOverloadTimeLeft_Type = TimeInterval
_TmnxIsisLevelOverloadTimeLeft_Object = MibTableColumn
tmnxIsisLevelOverloadTimeLeft = _TmnxIsisLevelOverloadTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 2, 1, 8),
    _TmnxIsisLevelOverloadTimeLeft_Type()
)
tmnxIsisLevelOverloadTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisLevelOverloadTimeLeft.setStatus("current")
_TmnxIsisLevelNumLSPs_Type = Unsigned32
_TmnxIsisLevelNumLSPs_Object = MibTableColumn
tmnxIsisLevelNumLSPs = _TmnxIsisLevelNumLSPs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 2, 1, 9),
    _TmnxIsisLevelNumLSPs_Type()
)
tmnxIsisLevelNumLSPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisLevelNumLSPs.setStatus("current")


class _TmnxIsisLevelCsnpAuthentication_Type(TruthValue):
    """Custom type tmnxIsisLevelCsnpAuthentication based on TruthValue"""
    defaultValue = 1


_TmnxIsisLevelCsnpAuthentication_Type.__name__ = "TruthValue"
_TmnxIsisLevelCsnpAuthentication_Object = MibTableColumn
tmnxIsisLevelCsnpAuthentication = _TmnxIsisLevelCsnpAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 2, 1, 10),
    _TmnxIsisLevelCsnpAuthentication_Type()
)
tmnxIsisLevelCsnpAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLevelCsnpAuthentication.setStatus("current")


class _TmnxIsisLevelHelloAuthentication_Type(TruthValue):
    """Custom type tmnxIsisLevelHelloAuthentication based on TruthValue"""
    defaultValue = 1


_TmnxIsisLevelHelloAuthentication_Type.__name__ = "TruthValue"
_TmnxIsisLevelHelloAuthentication_Object = MibTableColumn
tmnxIsisLevelHelloAuthentication = _TmnxIsisLevelHelloAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 2, 1, 11),
    _TmnxIsisLevelHelloAuthentication_Type()
)
tmnxIsisLevelHelloAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLevelHelloAuthentication.setStatus("current")


class _TmnxIsisLevelPsnpAuthentication_Type(TruthValue):
    """Custom type tmnxIsisLevelPsnpAuthentication based on TruthValue"""
    defaultValue = 1


_TmnxIsisLevelPsnpAuthentication_Type.__name__ = "TruthValue"
_TmnxIsisLevelPsnpAuthentication_Object = MibTableColumn
tmnxIsisLevelPsnpAuthentication = _TmnxIsisLevelPsnpAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 2, 1, 12),
    _TmnxIsisLevelPsnpAuthentication_Type()
)
tmnxIsisLevelPsnpAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLevelPsnpAuthentication.setStatus("current")


class _TmnxIsisLevelDefMetric_Type(Unsigned32):
    """Custom type tmnxIsisLevelDefMetric based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_TmnxIsisLevelDefMetric_Type.__name__ = "Unsigned32"
_TmnxIsisLevelDefMetric_Object = MibTableColumn
tmnxIsisLevelDefMetric = _TmnxIsisLevelDefMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 2, 1, 13),
    _TmnxIsisLevelDefMetric_Type()
)
tmnxIsisLevelDefMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLevelDefMetric.setStatus("current")


class _TmnxIsisLevelIPv6DefMetric_Type(Unsigned32):
    """Custom type tmnxIsisLevelIPv6DefMetric based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_TmnxIsisLevelIPv6DefMetric_Type.__name__ = "Unsigned32"
_TmnxIsisLevelIPv6DefMetric_Object = MibTableColumn
tmnxIsisLevelIPv6DefMetric = _TmnxIsisLevelIPv6DefMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 2, 1, 14),
    _TmnxIsisLevelIPv6DefMetric_Type()
)
tmnxIsisLevelIPv6DefMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLevelIPv6DefMetric.setStatus("current")


class _TmnxIsisLevelLoopfreeAltExclude_Type(TruthValue):
    """Custom type tmnxIsisLevelLoopfreeAltExclude based on TruthValue"""
    defaultValue = 2


_TmnxIsisLevelLoopfreeAltExclude_Type.__name__ = "TruthValue"
_TmnxIsisLevelLoopfreeAltExclude_Object = MibTableColumn
tmnxIsisLevelLoopfreeAltExclude = _TmnxIsisLevelLoopfreeAltExclude_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 2, 1, 15),
    _TmnxIsisLevelLoopfreeAltExclude_Type()
)
tmnxIsisLevelLoopfreeAltExclude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLevelLoopfreeAltExclude.setStatus("current")
_TmnxIsisLevelSpbBridgePriority_Type = Unsigned32
_TmnxIsisLevelSpbBridgePriority_Object = MibTableColumn
tmnxIsisLevelSpbBridgePriority = _TmnxIsisLevelSpbBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 2, 1, 16),
    _TmnxIsisLevelSpbBridgePriority_Type()
)
tmnxIsisLevelSpbBridgePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisLevelSpbBridgePriority.setStatus("current")
_TmnxIsisLevelSpbForwardTreeTopo_Type = Unsigned32
_TmnxIsisLevelSpbForwardTreeTopo_Object = MibTableColumn
tmnxIsisLevelSpbForwardTreeTopo = _TmnxIsisLevelSpbForwardTreeTopo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 2, 1, 17),
    _TmnxIsisLevelSpbForwardTreeTopo_Type()
)
tmnxIsisLevelSpbForwardTreeTopo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisLevelSpbForwardTreeTopo.setStatus("current")


class _TmnxIsisLevelDefIPv4McastMetric_Type(Unsigned32):
    """Custom type tmnxIsisLevelDefIPv4McastMetric based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_TmnxIsisLevelDefIPv4McastMetric_Type.__name__ = "Unsigned32"
_TmnxIsisLevelDefIPv4McastMetric_Object = MibTableColumn
tmnxIsisLevelDefIPv4McastMetric = _TmnxIsisLevelDefIPv4McastMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 2, 1, 18),
    _TmnxIsisLevelDefIPv4McastMetric_Type()
)
tmnxIsisLevelDefIPv4McastMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLevelDefIPv4McastMetric.setStatus("current")


class _TmnxIsisLevelDefIPv6McastMetric_Type(Unsigned32):
    """Custom type tmnxIsisLevelDefIPv6McastMetric based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_TmnxIsisLevelDefIPv6McastMetric_Type.__name__ = "Unsigned32"
_TmnxIsisLevelDefIPv6McastMetric_Object = MibTableColumn
tmnxIsisLevelDefIPv6McastMetric = _TmnxIsisLevelDefIPv6McastMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 2, 1, 19),
    _TmnxIsisLevelDefIPv6McastMetric_Type()
)
tmnxIsisLevelDefIPv6McastMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLevelDefIPv6McastMetric.setStatus("current")


class _TmnxIsisLevelAdvRtrCapability_Type(TruthValue):
    """Custom type tmnxIsisLevelAdvRtrCapability based on TruthValue"""
    defaultValue = 1


_TmnxIsisLevelAdvRtrCapability_Type.__name__ = "TruthValue"
_TmnxIsisLevelAdvRtrCapability_Object = MibTableColumn
tmnxIsisLevelAdvRtrCapability = _TmnxIsisLevelAdvRtrCapability_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 2, 1, 20),
    _TmnxIsisLevelAdvRtrCapability_Type()
)
tmnxIsisLevelAdvRtrCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLevelAdvRtrCapability.setStatus("current")


class _TmnxIsisLevelAuthKeyChain_Type(TNamedItemOrEmpty):
    """Custom type tmnxIsisLevelAuthKeyChain based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIsisLevelAuthKeyChain_Type.__name__ = "TNamedItemOrEmpty"
_TmnxIsisLevelAuthKeyChain_Object = MibTableColumn
tmnxIsisLevelAuthKeyChain = _TmnxIsisLevelAuthKeyChain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 2, 1, 21),
    _TmnxIsisLevelAuthKeyChain_Type()
)
tmnxIsisLevelAuthKeyChain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLevelAuthKeyChain.setStatus("current")
_TmnxIsisStatsTable_Object = MibTable
tmnxIsisStatsTable = _TmnxIsisStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3)
)
if mibBuilder.loadTexts:
    tmnxIsisStatsTable.setStatus("current")
_TmnxIsisStatsEntry_Object = MibTableRow
tmnxIsisStatsEntry = _TmnxIsisStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1)
)
tmnxIsisStatsEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ISIS-MIB", "isisSysInstance"),
)
if mibBuilder.loadTexts:
    tmnxIsisStatsEntry.setStatus("current")
_TmnxIsisStatsSpfRuns_Type = Counter32
_TmnxIsisStatsSpfRuns_Object = MibTableColumn
tmnxIsisStatsSpfRuns = _TmnxIsisStatsSpfRuns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 1),
    _TmnxIsisStatsSpfRuns_Type()
)
tmnxIsisStatsSpfRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsSpfRuns.setStatus("current")
_TmnxIsisStatsLSPRegenerations_Type = Counter32
_TmnxIsisStatsLSPRegenerations_Object = MibTableColumn
tmnxIsisStatsLSPRegenerations = _TmnxIsisStatsLSPRegenerations_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 2),
    _TmnxIsisStatsLSPRegenerations_Type()
)
tmnxIsisStatsLSPRegenerations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsLSPRegenerations.setStatus("current")
_TmnxIsisStatsInitiatedPurges_Type = Counter32
_TmnxIsisStatsInitiatedPurges_Object = MibTableColumn
tmnxIsisStatsInitiatedPurges = _TmnxIsisStatsInitiatedPurges_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 3),
    _TmnxIsisStatsInitiatedPurges_Type()
)
tmnxIsisStatsInitiatedPurges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsInitiatedPurges.setStatus("current")
_TmnxIsisStatsLSPRecd_Type = Counter32
_TmnxIsisStatsLSPRecd_Object = MibTableColumn
tmnxIsisStatsLSPRecd = _TmnxIsisStatsLSPRecd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 4),
    _TmnxIsisStatsLSPRecd_Type()
)
tmnxIsisStatsLSPRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsLSPRecd.setStatus("current")
_TmnxIsisStatsLSPDrop_Type = Counter32
_TmnxIsisStatsLSPDrop_Object = MibTableColumn
tmnxIsisStatsLSPDrop = _TmnxIsisStatsLSPDrop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 5),
    _TmnxIsisStatsLSPDrop_Type()
)
tmnxIsisStatsLSPDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsLSPDrop.setStatus("current")
_TmnxIsisStatsLSPSent_Type = Counter32
_TmnxIsisStatsLSPSent_Object = MibTableColumn
tmnxIsisStatsLSPSent = _TmnxIsisStatsLSPSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 6),
    _TmnxIsisStatsLSPSent_Type()
)
tmnxIsisStatsLSPSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsLSPSent.setStatus("current")
_TmnxIsisStatsLSPRetrans_Type = Counter32
_TmnxIsisStatsLSPRetrans_Object = MibTableColumn
tmnxIsisStatsLSPRetrans = _TmnxIsisStatsLSPRetrans_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 7),
    _TmnxIsisStatsLSPRetrans_Type()
)
tmnxIsisStatsLSPRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsLSPRetrans.setStatus("current")
_TmnxIsisStatsIIHRecd_Type = Counter32
_TmnxIsisStatsIIHRecd_Object = MibTableColumn
tmnxIsisStatsIIHRecd = _TmnxIsisStatsIIHRecd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 8),
    _TmnxIsisStatsIIHRecd_Type()
)
tmnxIsisStatsIIHRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsIIHRecd.setStatus("current")
_TmnxIsisStatsIIHDrop_Type = Counter32
_TmnxIsisStatsIIHDrop_Object = MibTableColumn
tmnxIsisStatsIIHDrop = _TmnxIsisStatsIIHDrop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 9),
    _TmnxIsisStatsIIHDrop_Type()
)
tmnxIsisStatsIIHDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsIIHDrop.setStatus("current")
_TmnxIsisStatsIIHSent_Type = Counter32
_TmnxIsisStatsIIHSent_Object = MibTableColumn
tmnxIsisStatsIIHSent = _TmnxIsisStatsIIHSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 10),
    _TmnxIsisStatsIIHSent_Type()
)
tmnxIsisStatsIIHSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsIIHSent.setStatus("current")
_TmnxIsisStatsIIHRetrans_Type = Counter32
_TmnxIsisStatsIIHRetrans_Object = MibTableColumn
tmnxIsisStatsIIHRetrans = _TmnxIsisStatsIIHRetrans_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 11),
    _TmnxIsisStatsIIHRetrans_Type()
)
tmnxIsisStatsIIHRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsIIHRetrans.setStatus("current")
_TmnxIsisStatsCSNPRecd_Type = Counter32
_TmnxIsisStatsCSNPRecd_Object = MibTableColumn
tmnxIsisStatsCSNPRecd = _TmnxIsisStatsCSNPRecd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 12),
    _TmnxIsisStatsCSNPRecd_Type()
)
tmnxIsisStatsCSNPRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsCSNPRecd.setStatus("current")
_TmnxIsisStatsCSNPDrop_Type = Counter32
_TmnxIsisStatsCSNPDrop_Object = MibTableColumn
tmnxIsisStatsCSNPDrop = _TmnxIsisStatsCSNPDrop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 13),
    _TmnxIsisStatsCSNPDrop_Type()
)
tmnxIsisStatsCSNPDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsCSNPDrop.setStatus("current")
_TmnxIsisStatsCSNPSent_Type = Counter32
_TmnxIsisStatsCSNPSent_Object = MibTableColumn
tmnxIsisStatsCSNPSent = _TmnxIsisStatsCSNPSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 14),
    _TmnxIsisStatsCSNPSent_Type()
)
tmnxIsisStatsCSNPSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsCSNPSent.setStatus("current")
_TmnxIsisStatsCSNPRetrans_Type = Counter32
_TmnxIsisStatsCSNPRetrans_Object = MibTableColumn
tmnxIsisStatsCSNPRetrans = _TmnxIsisStatsCSNPRetrans_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 15),
    _TmnxIsisStatsCSNPRetrans_Type()
)
tmnxIsisStatsCSNPRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsCSNPRetrans.setStatus("current")
_TmnxIsisStatsPSNPRecd_Type = Counter32
_TmnxIsisStatsPSNPRecd_Object = MibTableColumn
tmnxIsisStatsPSNPRecd = _TmnxIsisStatsPSNPRecd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 16),
    _TmnxIsisStatsPSNPRecd_Type()
)
tmnxIsisStatsPSNPRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsPSNPRecd.setStatus("current")
_TmnxIsisStatsPSNPDrop_Type = Counter32
_TmnxIsisStatsPSNPDrop_Object = MibTableColumn
tmnxIsisStatsPSNPDrop = _TmnxIsisStatsPSNPDrop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 17),
    _TmnxIsisStatsPSNPDrop_Type()
)
tmnxIsisStatsPSNPDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsPSNPDrop.setStatus("current")
_TmnxIsisStatsPSNPSent_Type = Counter32
_TmnxIsisStatsPSNPSent_Object = MibTableColumn
tmnxIsisStatsPSNPSent = _TmnxIsisStatsPSNPSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 18),
    _TmnxIsisStatsPSNPSent_Type()
)
tmnxIsisStatsPSNPSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsPSNPSent.setStatus("current")
_TmnxIsisStatsPSNPRetrans_Type = Counter32
_TmnxIsisStatsPSNPRetrans_Object = MibTableColumn
tmnxIsisStatsPSNPRetrans = _TmnxIsisStatsPSNPRetrans_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 19),
    _TmnxIsisStatsPSNPRetrans_Type()
)
tmnxIsisStatsPSNPRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsPSNPRetrans.setStatus("current")
_TmnxIsisStatsUnknownRecd_Type = Counter32
_TmnxIsisStatsUnknownRecd_Object = MibTableColumn
tmnxIsisStatsUnknownRecd = _TmnxIsisStatsUnknownRecd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 20),
    _TmnxIsisStatsUnknownRecd_Type()
)
tmnxIsisStatsUnknownRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsUnknownRecd.setStatus("current")
_TmnxIsisStatsUnknownDrop_Type = Counter32
_TmnxIsisStatsUnknownDrop_Object = MibTableColumn
tmnxIsisStatsUnknownDrop = _TmnxIsisStatsUnknownDrop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 21),
    _TmnxIsisStatsUnknownDrop_Type()
)
tmnxIsisStatsUnknownDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsUnknownDrop.setStatus("current")
_TmnxIsisStatsUnknownSent_Type = Counter32
_TmnxIsisStatsUnknownSent_Object = MibTableColumn
tmnxIsisStatsUnknownSent = _TmnxIsisStatsUnknownSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 22),
    _TmnxIsisStatsUnknownSent_Type()
)
tmnxIsisStatsUnknownSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsUnknownSent.setStatus("current")
_TmnxIsisStatsUnknownRetrans_Type = Counter32
_TmnxIsisStatsUnknownRetrans_Object = MibTableColumn
tmnxIsisStatsUnknownRetrans = _TmnxIsisStatsUnknownRetrans_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 23),
    _TmnxIsisStatsUnknownRetrans_Type()
)
tmnxIsisStatsUnknownRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsUnknownRetrans.setStatus("current")
_TmnxIsisStatsCSPFRequests_Type = Counter32
_TmnxIsisStatsCSPFRequests_Object = MibTableColumn
tmnxIsisStatsCSPFRequests = _TmnxIsisStatsCSPFRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 24),
    _TmnxIsisStatsCSPFRequests_Type()
)
tmnxIsisStatsCSPFRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsCSPFRequests.setStatus("current")
_TmnxIsisStatsCSPFDroppedRequests_Type = Counter32
_TmnxIsisStatsCSPFDroppedRequests_Object = MibTableColumn
tmnxIsisStatsCSPFDroppedRequests = _TmnxIsisStatsCSPFDroppedRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 25),
    _TmnxIsisStatsCSPFDroppedRequests_Type()
)
tmnxIsisStatsCSPFDroppedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsCSPFDroppedRequests.setStatus("current")
_TmnxIsisStatsCSPFPathsFound_Type = Counter32
_TmnxIsisStatsCSPFPathsFound_Object = MibTableColumn
tmnxIsisStatsCSPFPathsFound = _TmnxIsisStatsCSPFPathsFound_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 26),
    _TmnxIsisStatsCSPFPathsFound_Type()
)
tmnxIsisStatsCSPFPathsFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsCSPFPathsFound.setStatus("current")
_TmnxIsisStatsCSPFPathsNotFound_Type = Counter32
_TmnxIsisStatsCSPFPathsNotFound_Object = MibTableColumn
tmnxIsisStatsCSPFPathsNotFound = _TmnxIsisStatsCSPFPathsNotFound_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 27),
    _TmnxIsisStatsCSPFPathsNotFound_Type()
)
tmnxIsisStatsCSPFPathsNotFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsCSPFPathsNotFound.setStatus("current")
_TmnxIsisStatsLfaRuns_Type = Counter32
_TmnxIsisStatsLfaRuns_Object = MibTableColumn
tmnxIsisStatsLfaRuns = _TmnxIsisStatsLfaRuns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 28),
    _TmnxIsisStatsLfaRuns_Type()
)
tmnxIsisStatsLfaRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsLfaRuns.setStatus("current")
_TmnxIsisStatsPartSpfRuns_Type = Counter32
_TmnxIsisStatsPartSpfRuns_Object = MibTableColumn
tmnxIsisStatsPartSpfRuns = _TmnxIsisStatsPartSpfRuns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 29),
    _TmnxIsisStatsPartSpfRuns_Type()
)
tmnxIsisStatsPartSpfRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsPartSpfRuns.setStatus("current")
_TmnxIsisStatsPartSpfTimeStamp_Type = TimeStamp
_TmnxIsisStatsPartSpfTimeStamp_Object = MibTableColumn
tmnxIsisStatsPartSpfTimeStamp = _TmnxIsisStatsPartSpfTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 30),
    _TmnxIsisStatsPartSpfTimeStamp_Type()
)
tmnxIsisStatsPartSpfTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsPartSpfTimeStamp.setStatus("current")
_TmnxIsisStatsPartLfaRuns_Type = Counter32
_TmnxIsisStatsPartLfaRuns_Object = MibTableColumn
tmnxIsisStatsPartLfaRuns = _TmnxIsisStatsPartLfaRuns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 31),
    _TmnxIsisStatsPartLfaRuns_Type()
)
tmnxIsisStatsPartLfaRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsPartLfaRuns.setStatus("current")
_TmnxIsisStatsPartLfaTimeStamp_Type = TimeStamp
_TmnxIsisStatsPartLfaTimeStamp_Object = MibTableColumn
tmnxIsisStatsPartLfaTimeStamp = _TmnxIsisStatsPartLfaTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 32),
    _TmnxIsisStatsPartLfaTimeStamp_Type()
)
tmnxIsisStatsPartLfaTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsPartLfaTimeStamp.setStatus("current")
_TmnxIsisStatsLfaTimeStamp_Type = TimeStamp
_TmnxIsisStatsLfaTimeStamp_Object = MibTableColumn
tmnxIsisStatsLfaTimeStamp = _TmnxIsisStatsLfaTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 33),
    _TmnxIsisStatsLfaTimeStamp_Type()
)
tmnxIsisStatsLfaTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsLfaTimeStamp.setStatus("current")
_TmnxIsisStatsSpfTimeStamp_Type = TimeStamp
_TmnxIsisStatsSpfTimeStamp_Object = MibTableColumn
tmnxIsisStatsSpfTimeStamp = _TmnxIsisStatsSpfTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 34),
    _TmnxIsisStatsSpfTimeStamp_Type()
)
tmnxIsisStatsSpfTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsSpfTimeStamp.setStatus("current")
_TmnxIsisHostTable_Object = MibTable
tmnxIsisHostTable = _TmnxIsisHostTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 4)
)
if mibBuilder.loadTexts:
    tmnxIsisHostTable.setStatus("current")
_TmnxIsisHostEntry_Object = MibTableRow
tmnxIsisHostEntry = _TmnxIsisHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 4, 1)
)
tmnxIsisHostEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisHostSysID"),
)
if mibBuilder.loadTexts:
    tmnxIsisHostEntry.setStatus("current")
_TmnxIsisHostSysID_Type = SystemID
_TmnxIsisHostSysID_Object = MibTableColumn
tmnxIsisHostSysID = _TmnxIsisHostSysID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 4, 1, 1),
    _TmnxIsisHostSysID_Type()
)
tmnxIsisHostSysID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisHostSysID.setStatus("current")
_TmnxIsisHostName_Type = DisplayString
_TmnxIsisHostName_Object = MibTableColumn
tmnxIsisHostName = _TmnxIsisHostName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 4, 1, 2),
    _TmnxIsisHostName_Type()
)
tmnxIsisHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisHostName.setStatus("current")
_TmnxIsisRouteTable_Object = MibTable
tmnxIsisRouteTable = _TmnxIsisRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 5)
)
if mibBuilder.loadTexts:
    tmnxIsisRouteTable.setStatus("current")
_TmnxIsisRouteEntry_Object = MibTableRow
tmnxIsisRouteEntry = _TmnxIsisRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 5, 1)
)
tmnxIsisRouteEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteMtId"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteDestType"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteDest"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisRoutePrefixLength"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteNexthopIPType"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteNexthopIP"),
)
if mibBuilder.loadTexts:
    tmnxIsisRouteEntry.setStatus("current")
_TmnxIsisRouteMtId_Type = Unsigned32
_TmnxIsisRouteMtId_Object = MibTableColumn
tmnxIsisRouteMtId = _TmnxIsisRouteMtId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 5, 1, 1),
    _TmnxIsisRouteMtId_Type()
)
tmnxIsisRouteMtId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisRouteMtId.setStatus("current")
_TmnxIsisRouteDestType_Type = InetAddressType
_TmnxIsisRouteDestType_Object = MibTableColumn
tmnxIsisRouteDestType = _TmnxIsisRouteDestType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 5, 1, 2),
    _TmnxIsisRouteDestType_Type()
)
tmnxIsisRouteDestType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisRouteDestType.setStatus("current")


class _TmnxIsisRouteDest_Type(InetAddress):
    """Custom type tmnxIsisRouteDest based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxIsisRouteDest_Type.__name__ = "InetAddress"
_TmnxIsisRouteDest_Object = MibTableColumn
tmnxIsisRouteDest = _TmnxIsisRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 5, 1, 3),
    _TmnxIsisRouteDest_Type()
)
tmnxIsisRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisRouteDest.setStatus("current")
_TmnxIsisRoutePrefixLength_Type = InetAddressPrefixLength
_TmnxIsisRoutePrefixLength_Object = MibTableColumn
tmnxIsisRoutePrefixLength = _TmnxIsisRoutePrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 5, 1, 4),
    _TmnxIsisRoutePrefixLength_Type()
)
tmnxIsisRoutePrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisRoutePrefixLength.setStatus("current")
_TmnxIsisRouteNexthopIPType_Type = InetAddressType
_TmnxIsisRouteNexthopIPType_Object = MibTableColumn
tmnxIsisRouteNexthopIPType = _TmnxIsisRouteNexthopIPType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 5, 1, 5),
    _TmnxIsisRouteNexthopIPType_Type()
)
tmnxIsisRouteNexthopIPType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisRouteNexthopIPType.setStatus("current")


class _TmnxIsisRouteNexthopIP_Type(InetAddress):
    """Custom type tmnxIsisRouteNexthopIP based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxIsisRouteNexthopIP_Type.__name__ = "InetAddress"
_TmnxIsisRouteNexthopIP_Object = MibTableColumn
tmnxIsisRouteNexthopIP = _TmnxIsisRouteNexthopIP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 5, 1, 6),
    _TmnxIsisRouteNexthopIP_Type()
)
tmnxIsisRouteNexthopIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisRouteNexthopIP.setStatus("current")


class _TmnxIsisRouteLevel_Type(Integer32):
    """Custom type tmnxIsisRouteLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("level1IS", 1),
          ("level2IS", 2))
    )


_TmnxIsisRouteLevel_Type.__name__ = "Integer32"
_TmnxIsisRouteLevel_Object = MibTableColumn
tmnxIsisRouteLevel = _TmnxIsisRouteLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 5, 1, 7),
    _TmnxIsisRouteLevel_Type()
)
tmnxIsisRouteLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisRouteLevel.setStatus("current")
_TmnxIsisRouteSpfRunNumber_Type = Counter32
_TmnxIsisRouteSpfRunNumber_Object = MibTableColumn
tmnxIsisRouteSpfRunNumber = _TmnxIsisRouteSpfRunNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 5, 1, 8),
    _TmnxIsisRouteSpfRunNumber_Type()
)
tmnxIsisRouteSpfRunNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisRouteSpfRunNumber.setStatus("current")
_TmnxIsisRouteMetric_Type = Unsigned32
_TmnxIsisRouteMetric_Object = MibTableColumn
tmnxIsisRouteMetric = _TmnxIsisRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 5, 1, 9),
    _TmnxIsisRouteMetric_Type()
)
tmnxIsisRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisRouteMetric.setStatus("current")


class _TmnxIsisRouteType_Type(Integer32):
    """Custom type tmnxIsisRouteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internal", 1),
          ("external", 2))
    )


_TmnxIsisRouteType_Type.__name__ = "Integer32"
_TmnxIsisRouteType_Object = MibTableColumn
tmnxIsisRouteType = _TmnxIsisRouteType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 5, 1, 10),
    _TmnxIsisRouteType_Type()
)
tmnxIsisRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisRouteType.setStatus("current")
_TmnxIsisRouteNHopSysID_Type = SystemID
_TmnxIsisRouteNHopSysID_Object = MibTableColumn
tmnxIsisRouteNHopSysID = _TmnxIsisRouteNHopSysID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 5, 1, 11),
    _TmnxIsisRouteNHopSysID_Type()
)
tmnxIsisRouteNHopSysID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisRouteNHopSysID.setStatus("current")
_TmnxIsisRouteTag_Type = Unsigned32
_TmnxIsisRouteTag_Object = MibTableColumn
tmnxIsisRouteTag = _TmnxIsisRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 5, 1, 12),
    _TmnxIsisRouteTag_Type()
)
tmnxIsisRouteTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisRouteTag.setStatus("current")


class _TmnxIsisRouteBkupFlags_Type(Integer32):
    """Custom type tmnxIsisRouteBkupFlags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("hasLfa", 1))
    )


_TmnxIsisRouteBkupFlags_Type.__name__ = "Integer32"
_TmnxIsisRouteBkupFlags_Object = MibTableColumn
tmnxIsisRouteBkupFlags = _TmnxIsisRouteBkupFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 5, 1, 13),
    _TmnxIsisRouteBkupFlags_Type()
)
tmnxIsisRouteBkupFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisRouteBkupFlags.setStatus("current")


class _TmnxIsisRouteBkupNextHopTy_Type(Integer32):
    """Custom type tmnxIsisRouteBkupNextHopTy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("nodeProtection", 1),
          ("linkProtection", 2))
    )


_TmnxIsisRouteBkupNextHopTy_Type.__name__ = "Integer32"
_TmnxIsisRouteBkupNextHopTy_Object = MibTableColumn
tmnxIsisRouteBkupNextHopTy = _TmnxIsisRouteBkupNextHopTy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 5, 1, 14),
    _TmnxIsisRouteBkupNextHopTy_Type()
)
tmnxIsisRouteBkupNextHopTy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisRouteBkupNextHopTy.setStatus("current")
_TmnxIsisRouteBkupNextHopType_Type = InetAddressType
_TmnxIsisRouteBkupNextHopType_Object = MibTableColumn
tmnxIsisRouteBkupNextHopType = _TmnxIsisRouteBkupNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 5, 1, 15),
    _TmnxIsisRouteBkupNextHopType_Type()
)
tmnxIsisRouteBkupNextHopType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisRouteBkupNextHopType.setStatus("current")


class _TmnxIsisRouteBkupNextHop_Type(InetAddress):
    """Custom type tmnxIsisRouteBkupNextHop based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxIsisRouteBkupNextHop_Type.__name__ = "InetAddress"
_TmnxIsisRouteBkupNextHop_Object = MibTableColumn
tmnxIsisRouteBkupNextHop = _TmnxIsisRouteBkupNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 5, 1, 16),
    _TmnxIsisRouteBkupNextHop_Type()
)
tmnxIsisRouteBkupNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisRouteBkupNextHop.setStatus("current")
_TmnxIsisRouteBkupMetric_Type = Unsigned32
_TmnxIsisRouteBkupMetric_Object = MibTableColumn
tmnxIsisRouteBkupMetric = _TmnxIsisRouteBkupMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 5, 1, 17),
    _TmnxIsisRouteBkupMetric_Type()
)
tmnxIsisRouteBkupMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisRouteBkupMetric.setStatus("current")
_TmnxIsisRouteNextHopType_Type = TmnxInetCidrNextHopType
_TmnxIsisRouteNextHopType_Object = MibTableColumn
tmnxIsisRouteNextHopType = _TmnxIsisRouteNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 5, 1, 18),
    _TmnxIsisRouteNextHopType_Type()
)
tmnxIsisRouteNextHopType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisRouteNextHopType.setStatus("current")
_TmnxIsisRouteNextHopOwner_Type = TmnxInetCidrNextHopOwner
_TmnxIsisRouteNextHopOwner_Object = MibTableColumn
tmnxIsisRouteNextHopOwner = _TmnxIsisRouteNextHopOwner_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 5, 1, 19),
    _TmnxIsisRouteNextHopOwner_Type()
)
tmnxIsisRouteNextHopOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisRouteNextHopOwner.setStatus("current")
_TmnxIsisRouteNHOwnerAuxInfo_Type = Unsigned32
_TmnxIsisRouteNHOwnerAuxInfo_Object = MibTableColumn
tmnxIsisRouteNHOwnerAuxInfo = _TmnxIsisRouteNHOwnerAuxInfo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 5, 1, 20),
    _TmnxIsisRouteNHOwnerAuxInfo_Type()
)
tmnxIsisRouteNHOwnerAuxInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisRouteNHOwnerAuxInfo.setStatus("current")
_TmnxIsisRouteBkupNHType_Type = TmnxInetCidrNextHopType
_TmnxIsisRouteBkupNHType_Object = MibTableColumn
tmnxIsisRouteBkupNHType = _TmnxIsisRouteBkupNHType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 5, 1, 21),
    _TmnxIsisRouteBkupNHType_Type()
)
tmnxIsisRouteBkupNHType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisRouteBkupNHType.setStatus("current")
_TmnxIsisRouteBkupNHOwner_Type = TmnxInetCidrNextHopOwner
_TmnxIsisRouteBkupNHOwner_Object = MibTableColumn
tmnxIsisRouteBkupNHOwner = _TmnxIsisRouteBkupNHOwner_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 5, 1, 22),
    _TmnxIsisRouteBkupNHOwner_Type()
)
tmnxIsisRouteBkupNHOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisRouteBkupNHOwner.setStatus("current")
_TmnxIsisRouteBkupNHOwnAxInfo_Type = Unsigned32
_TmnxIsisRouteBkupNHOwnAxInfo_Object = MibTableColumn
tmnxIsisRouteBkupNHOwnAxInfo = _TmnxIsisRouteBkupNHOwnAxInfo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 5, 1, 23),
    _TmnxIsisRouteBkupNHOwnAxInfo_Type()
)
tmnxIsisRouteBkupNHOwnAxInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisRouteBkupNHOwnAxInfo.setStatus("current")
_TmnxIsisPathTable_Object = MibTable
tmnxIsisPathTable = _TmnxIsisPathTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 6)
)
if mibBuilder.loadTexts:
    tmnxIsisPathTable.setStatus("current")
_TmnxIsisPathEntry_Object = MibTableRow
tmnxIsisPathEntry = _TmnxIsisPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 6, 1)
)
tmnxIsisPathEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisLevel"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisPathMtID"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisPathID"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisPathIfIndex"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisPathNHopSysID"),
)
if mibBuilder.loadTexts:
    tmnxIsisPathEntry.setStatus("current")
_TmnxIsisPathMtID_Type = Unsigned32
_TmnxIsisPathMtID_Object = MibTableColumn
tmnxIsisPathMtID = _TmnxIsisPathMtID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 6, 1, 1),
    _TmnxIsisPathMtID_Type()
)
tmnxIsisPathMtID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisPathMtID.setStatus("current")


class _TmnxIsisPathID_Type(OctetString):
    """Custom type tmnxIsisPathID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )
    fixed_length = 7


_TmnxIsisPathID_Type.__name__ = "OctetString"
_TmnxIsisPathID_Object = MibTableColumn
tmnxIsisPathID = _TmnxIsisPathID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 6, 1, 2),
    _TmnxIsisPathID_Type()
)
tmnxIsisPathID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisPathID.setStatus("current")
_TmnxIsisPathIfIndex_Type = InterfaceIndex
_TmnxIsisPathIfIndex_Object = MibTableColumn
tmnxIsisPathIfIndex = _TmnxIsisPathIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 6, 1, 3),
    _TmnxIsisPathIfIndex_Type()
)
tmnxIsisPathIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisPathIfIndex.setStatus("current")
_TmnxIsisPathNHopSysID_Type = SystemID
_TmnxIsisPathNHopSysID_Object = MibTableColumn
tmnxIsisPathNHopSysID = _TmnxIsisPathNHopSysID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 6, 1, 4),
    _TmnxIsisPathNHopSysID_Type()
)
tmnxIsisPathNHopSysID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisPathNHopSysID.setStatus("current")
_TmnxIsisPathMetric_Type = Unsigned32
_TmnxIsisPathMetric_Object = MibTableColumn
tmnxIsisPathMetric = _TmnxIsisPathMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 6, 1, 5),
    _TmnxIsisPathMetric_Type()
)
tmnxIsisPathMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisPathMetric.setStatus("current")
_TmnxIsisPathSNPA_Type = SNPAAddress
_TmnxIsisPathSNPA_Object = MibTableColumn
tmnxIsisPathSNPA = _TmnxIsisPathSNPA_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 6, 1, 6),
    _TmnxIsisPathSNPA_Type()
)
tmnxIsisPathSNPA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisPathSNPA.setStatus("current")
_TmnxIsisPathLfaIfIndex_Type = InterfaceIndex
_TmnxIsisPathLfaIfIndex_Object = MibTableColumn
tmnxIsisPathLfaIfIndex = _TmnxIsisPathLfaIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 6, 1, 7),
    _TmnxIsisPathLfaIfIndex_Type()
)
tmnxIsisPathLfaIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisPathLfaIfIndex.setStatus("current")
_TmnxIsisPathLfaNHop_Type = SystemID
_TmnxIsisPathLfaNHop_Object = MibTableColumn
tmnxIsisPathLfaNHop = _TmnxIsisPathLfaNHop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 6, 1, 8),
    _TmnxIsisPathLfaNHop_Type()
)
tmnxIsisPathLfaNHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisPathLfaNHop.setStatus("current")
_TmnxIsisPathLfaMetric_Type = Unsigned32
_TmnxIsisPathLfaMetric_Object = MibTableColumn
tmnxIsisPathLfaMetric = _TmnxIsisPathLfaMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 6, 1, 9),
    _TmnxIsisPathLfaMetric_Type()
)
tmnxIsisPathLfaMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisPathLfaMetric.setStatus("current")


class _TmnxIsisPathLfaType_Type(Integer32):
    """Custom type tmnxIsisPathLfaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("nodeLink", 1),
          ("pathLink", 2))
    )


_TmnxIsisPathLfaType_Type.__name__ = "Integer32"
_TmnxIsisPathLfaType_Object = MibTableColumn
tmnxIsisPathLfaType = _TmnxIsisPathLfaType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 6, 1, 10),
    _TmnxIsisPathLfaType_Type()
)
tmnxIsisPathLfaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisPathLfaType.setStatus("current")


class _TmnxIsisPathRouteType_Type(Integer32):
    """Custom type tmnxIsisPathRouteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("spf", 0),
          ("lfa", 1))
    )


_TmnxIsisPathRouteType_Type.__name__ = "Integer32"
_TmnxIsisPathRouteType_Object = MibTableColumn
tmnxIsisPathRouteType = _TmnxIsisPathRouteType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 6, 1, 11),
    _TmnxIsisPathRouteType_Type()
)
tmnxIsisPathRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisPathRouteType.setStatus("current")
_TmnxIsisLSPTable_Object = MibTable
tmnxIsisLSPTable = _TmnxIsisLSPTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 7)
)
if mibBuilder.loadTexts:
    tmnxIsisLSPTable.setStatus("current")
_TmnxIsisLSPEntry_Object = MibTableRow
tmnxIsisLSPEntry = _TmnxIsisLSPEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 7, 1)
)
tmnxIsisLSPEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisLevel"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisLSPId"),
)
if mibBuilder.loadTexts:
    tmnxIsisLSPEntry.setStatus("current")


class _TmnxIsisLSPId_Type(OctetString):
    """Custom type tmnxIsisLSPId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_TmnxIsisLSPId_Type.__name__ = "OctetString"
_TmnxIsisLSPId_Object = MibTableColumn
tmnxIsisLSPId = _TmnxIsisLSPId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 7, 1, 1),
    _TmnxIsisLSPId_Type()
)
tmnxIsisLSPId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisLSPId.setStatus("current")
_TmnxIsisLSPSeq_Type = Counter32
_TmnxIsisLSPSeq_Object = MibTableColumn
tmnxIsisLSPSeq = _TmnxIsisLSPSeq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 7, 1, 2),
    _TmnxIsisLSPSeq_Type()
)
tmnxIsisLSPSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisLSPSeq.setStatus("current")


class _TmnxIsisLSPChecksum_Type(Integer32):
    """Custom type tmnxIsisLSPChecksum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TmnxIsisLSPChecksum_Type.__name__ = "Integer32"
_TmnxIsisLSPChecksum_Object = MibTableColumn
tmnxIsisLSPChecksum = _TmnxIsisLSPChecksum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 7, 1, 3),
    _TmnxIsisLSPChecksum_Type()
)
tmnxIsisLSPChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisLSPChecksum.setStatus("current")


class _TmnxIsisLSPLifetimeRemain_Type(Integer32):
    """Custom type tmnxIsisLSPLifetimeRemain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TmnxIsisLSPLifetimeRemain_Type.__name__ = "Integer32"
_TmnxIsisLSPLifetimeRemain_Object = MibTableColumn
tmnxIsisLSPLifetimeRemain = _TmnxIsisLSPLifetimeRemain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 7, 1, 4),
    _TmnxIsisLSPLifetimeRemain_Type()
)
tmnxIsisLSPLifetimeRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisLSPLifetimeRemain.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIsisLSPLifetimeRemain.setUnits("seconds")
_TmnxIsisLSPVersion_Type = Integer32
_TmnxIsisLSPVersion_Object = MibTableColumn
tmnxIsisLSPVersion = _TmnxIsisLSPVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 7, 1, 5),
    _TmnxIsisLSPVersion_Type()
)
tmnxIsisLSPVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisLSPVersion.setStatus("current")
_TmnxIsisLSPPktType_Type = Integer32
_TmnxIsisLSPPktType_Object = MibTableColumn
tmnxIsisLSPPktType = _TmnxIsisLSPPktType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 7, 1, 6),
    _TmnxIsisLSPPktType_Type()
)
tmnxIsisLSPPktType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisLSPPktType.setStatus("current")
_TmnxIsisLSPPktVersion_Type = Integer32
_TmnxIsisLSPPktVersion_Object = MibTableColumn
tmnxIsisLSPPktVersion = _TmnxIsisLSPPktVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 7, 1, 7),
    _TmnxIsisLSPPktVersion_Type()
)
tmnxIsisLSPPktVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisLSPPktVersion.setStatus("current")
_TmnxIsisLSPMaxArea_Type = Integer32
_TmnxIsisLSPMaxArea_Object = MibTableColumn
tmnxIsisLSPMaxArea = _TmnxIsisLSPMaxArea_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 7, 1, 8),
    _TmnxIsisLSPMaxArea_Type()
)
tmnxIsisLSPMaxArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisLSPMaxArea.setStatus("current")
_TmnxIsisLSPSysIdLen_Type = Integer32
_TmnxIsisLSPSysIdLen_Object = MibTableColumn
tmnxIsisLSPSysIdLen = _TmnxIsisLSPSysIdLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 7, 1, 9),
    _TmnxIsisLSPSysIdLen_Type()
)
tmnxIsisLSPSysIdLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisLSPSysIdLen.setStatus("current")
_TmnxIsisLSPAttributes_Type = Integer32
_TmnxIsisLSPAttributes_Object = MibTableColumn
tmnxIsisLSPAttributes = _TmnxIsisLSPAttributes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 7, 1, 10),
    _TmnxIsisLSPAttributes_Type()
)
tmnxIsisLSPAttributes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisLSPAttributes.setStatus("current")
_TmnxIsisLSPUsedLen_Type = Integer32
_TmnxIsisLSPUsedLen_Object = MibTableColumn
tmnxIsisLSPUsedLen = _TmnxIsisLSPUsedLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 7, 1, 11),
    _TmnxIsisLSPUsedLen_Type()
)
tmnxIsisLSPUsedLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisLSPUsedLen.setStatus("current")
_TmnxIsisLSPAllocLen_Type = Integer32
_TmnxIsisLSPAllocLen_Object = MibTableColumn
tmnxIsisLSPAllocLen = _TmnxIsisLSPAllocLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 7, 1, 12),
    _TmnxIsisLSPAllocLen_Type()
)
tmnxIsisLSPAllocLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisLSPAllocLen.setStatus("current")


class _TmnxIsisLSPBuff_Type(OctetString):
    """Custom type tmnxIsisLSPBuff based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(27, 9190),
    )


_TmnxIsisLSPBuff_Type.__name__ = "OctetString"
_TmnxIsisLSPBuff_Object = MibTableColumn
tmnxIsisLSPBuff = _TmnxIsisLSPBuff_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 7, 1, 13),
    _TmnxIsisLSPBuff_Type()
)
tmnxIsisLSPBuff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisLSPBuff.setStatus("current")
_TmnxIsisLSPZeroRLT_Type = TruthValue
_TmnxIsisLSPZeroRLT_Object = MibTableColumn
tmnxIsisLSPZeroRLT = _TmnxIsisLSPZeroRLT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 7, 1, 14),
    _TmnxIsisLSPZeroRLT_Type()
)
tmnxIsisLSPZeroRLT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisLSPZeroRLT.setStatus("current")
_TmnxIsisSpfLogTable_Object = MibTable
tmnxIsisSpfLogTable = _TmnxIsisSpfLogTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 8)
)
if mibBuilder.loadTexts:
    tmnxIsisSpfLogTable.setStatus("current")
_TmnxIsisSpfLogEntry_Object = MibTableRow
tmnxIsisSpfLogEntry = _TmnxIsisSpfLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 8, 1)
)
tmnxIsisSpfLogEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisSpfLogTimeStamp"),
)
if mibBuilder.loadTexts:
    tmnxIsisSpfLogEntry.setStatus("current")
_TmnxIsisSpfLogTimeStamp_Type = TimeStamp
_TmnxIsisSpfLogTimeStamp_Object = MibTableColumn
tmnxIsisSpfLogTimeStamp = _TmnxIsisSpfLogTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 8, 1, 1),
    _TmnxIsisSpfLogTimeStamp_Type()
)
tmnxIsisSpfLogTimeStamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisSpfLogTimeStamp.setStatus("current")
_TmnxIsisSpfLogRunTime_Type = TimeTicks
_TmnxIsisSpfLogRunTime_Object = MibTableColumn
tmnxIsisSpfLogRunTime = _TmnxIsisSpfLogRunTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 8, 1, 2),
    _TmnxIsisSpfLogRunTime_Type()
)
tmnxIsisSpfLogRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisSpfLogRunTime.setStatus("current")
_TmnxIsisSpfLogL1Nodes_Type = Unsigned32
_TmnxIsisSpfLogL1Nodes_Object = MibTableColumn
tmnxIsisSpfLogL1Nodes = _TmnxIsisSpfLogL1Nodes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 8, 1, 3),
    _TmnxIsisSpfLogL1Nodes_Type()
)
tmnxIsisSpfLogL1Nodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisSpfLogL1Nodes.setStatus("current")
_TmnxIsisSpfLogL2Nodes_Type = Unsigned32
_TmnxIsisSpfLogL2Nodes_Object = MibTableColumn
tmnxIsisSpfLogL2Nodes = _TmnxIsisSpfLogL2Nodes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 8, 1, 4),
    _TmnxIsisSpfLogL2Nodes_Type()
)
tmnxIsisSpfLogL2Nodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisSpfLogL2Nodes.setStatus("current")
_TmnxIsisSpfLogEventCount_Type = Unsigned32
_TmnxIsisSpfLogEventCount_Object = MibTableColumn
tmnxIsisSpfLogEventCount = _TmnxIsisSpfLogEventCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 8, 1, 5),
    _TmnxIsisSpfLogEventCount_Type()
)
tmnxIsisSpfLogEventCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisSpfLogEventCount.setStatus("current")


class _TmnxIsisSpfLogLastTriggerLSPId_Type(OctetString):
    """Custom type tmnxIsisSpfLogLastTriggerLSPId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_TmnxIsisSpfLogLastTriggerLSPId_Type.__name__ = "OctetString"
_TmnxIsisSpfLogLastTriggerLSPId_Object = MibTableColumn
tmnxIsisSpfLogLastTriggerLSPId = _TmnxIsisSpfLogLastTriggerLSPId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 8, 1, 6),
    _TmnxIsisSpfLogLastTriggerLSPId_Type()
)
tmnxIsisSpfLogLastTriggerLSPId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisSpfLogLastTriggerLSPId.setStatus("current")


class _TmnxIsisSpfLogTriggerReason_Type(Bits):
    """Custom type tmnxIsisSpfLogTriggerReason based on Bits"""
    namedValues = NamedValues(
        *(("newAdjacency", 0),
          ("newLSP", 1),
          ("newArea", 2),
          ("reach", 3),
          ("ecmpChanged", 4),
          ("newMetric", 5),
          ("teChanged", 6),
          ("restart", 7),
          ("lspExpired", 8),
          ("lspDbChanged", 9),
          ("lspChanged", 10),
          ("newPreference", 11),
          ("newNLPID", 12),
          ("manualRun", 13),
          ("adminTagChanged", 14),
          ("tunnelChanged", 15),
          ("throttleEnd", 16),
          ("lfaChanged", 17))
    )

_TmnxIsisSpfLogTriggerReason_Type.__name__ = "Bits"
_TmnxIsisSpfLogTriggerReason_Object = MibTableColumn
tmnxIsisSpfLogTriggerReason = _TmnxIsisSpfLogTriggerReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 8, 1, 7),
    _TmnxIsisSpfLogTriggerReason_Type()
)
tmnxIsisSpfLogTriggerReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisSpfLogTriggerReason.setStatus("current")


class _TmnxIsisSpfLogType_Type(Integer32):
    """Custom type tmnxIsisSpfLogType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("regular", 0),
          ("lfa", 1),
          ("partialSpf", 2),
          ("partialLfa", 3))
    )


_TmnxIsisSpfLogType_Type.__name__ = "Integer32"
_TmnxIsisSpfLogType_Object = MibTableColumn
tmnxIsisSpfLogType = _TmnxIsisSpfLogType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 8, 1, 8),
    _TmnxIsisSpfLogType_Type()
)
tmnxIsisSpfLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisSpfLogType.setStatus("current")
_TmnxIsisSummaryTable_Object = MibTable
tmnxIsisSummaryTable = _TmnxIsisSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 9)
)
if mibBuilder.loadTexts:
    tmnxIsisSummaryTable.setStatus("current")
_TmnxIsisSummaryEntry_Object = MibTableRow
tmnxIsisSummaryEntry = _TmnxIsisSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 9, 1)
)
tmnxIsisSummaryEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisSummPrefixType"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisSummPrefix"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisSummPrefixLength"),
)
if mibBuilder.loadTexts:
    tmnxIsisSummaryEntry.setStatus("current")
_TmnxIsisSummPrefixType_Type = InetAddressType
_TmnxIsisSummPrefixType_Object = MibTableColumn
tmnxIsisSummPrefixType = _TmnxIsisSummPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 9, 1, 1),
    _TmnxIsisSummPrefixType_Type()
)
tmnxIsisSummPrefixType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisSummPrefixType.setStatus("current")


class _TmnxIsisSummPrefix_Type(InetAddress):
    """Custom type tmnxIsisSummPrefix based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxIsisSummPrefix_Type.__name__ = "InetAddress"
_TmnxIsisSummPrefix_Object = MibTableColumn
tmnxIsisSummPrefix = _TmnxIsisSummPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 9, 1, 2),
    _TmnxIsisSummPrefix_Type()
)
tmnxIsisSummPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisSummPrefix.setStatus("current")
_TmnxIsisSummPrefixLength_Type = InetAddressPrefixLength
_TmnxIsisSummPrefixLength_Object = MibTableColumn
tmnxIsisSummPrefixLength = _TmnxIsisSummPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 9, 1, 3),
    _TmnxIsisSummPrefixLength_Type()
)
tmnxIsisSummPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisSummPrefixLength.setStatus("current")
_TmnxIsisSummRowStatus_Type = RowStatus
_TmnxIsisSummRowStatus_Object = MibTableColumn
tmnxIsisSummRowStatus = _TmnxIsisSummRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 9, 1, 4),
    _TmnxIsisSummRowStatus_Type()
)
tmnxIsisSummRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisSummRowStatus.setStatus("current")


class _TmnxIsisSummLevel_Type(Integer32):
    """Custom type tmnxIsisSummLevel based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("level1", 1),
          ("level2", 2),
          ("level1L2", 3))
    )


_TmnxIsisSummLevel_Type.__name__ = "Integer32"
_TmnxIsisSummLevel_Object = MibTableColumn
tmnxIsisSummLevel = _TmnxIsisSummLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 9, 1, 5),
    _TmnxIsisSummLevel_Type()
)
tmnxIsisSummLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisSummLevel.setStatus("current")


class _TmnxIsisSummRouteTag_Type(Unsigned32):
    """Custom type tmnxIsisSummRouteTag based on Unsigned32"""
    defaultValue = 0


_TmnxIsisSummRouteTag_Type.__name__ = "Unsigned32"
_TmnxIsisSummRouteTag_Object = MibTableColumn
tmnxIsisSummRouteTag = _TmnxIsisSummRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 9, 1, 6),
    _TmnxIsisSummRouteTag_Type()
)
tmnxIsisSummRouteTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisSummRouteTag.setStatus("current")
_TmnxIsisLfaTable_Object = MibTable
tmnxIsisLfaTable = _TmnxIsisLfaTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 10)
)
if mibBuilder.loadTexts:
    tmnxIsisLfaTable.setStatus("current")
_TmnxIsisLfaEntry_Object = MibTableRow
tmnxIsisLfaEntry = _TmnxIsisLfaEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 10, 1)
)
tmnxIsisLfaEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisLevel"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisLfaFamilyCoverage"),
)
if mibBuilder.loadTexts:
    tmnxIsisLfaEntry.setStatus("current")


class _TmnxIsisLfaFamilyCoverage_Type(Integer32):
    """Custom type tmnxIsisLfaFamilyCoverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 0),
          ("ipv6", 1),
          ("ipv4Mcast", 2),
          ("ipv6Mcast", 3))
    )


_TmnxIsisLfaFamilyCoverage_Type.__name__ = "Integer32"
_TmnxIsisLfaFamilyCoverage_Object = MibTableColumn
tmnxIsisLfaFamilyCoverage = _TmnxIsisLfaFamilyCoverage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 10, 1, 1),
    _TmnxIsisLfaFamilyCoverage_Type()
)
tmnxIsisLfaFamilyCoverage.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisLfaFamilyCoverage.setStatus("current")
_TmnxIsisLfaNodesCovered_Type = Unsigned32
_TmnxIsisLfaNodesCovered_Object = MibTableColumn
tmnxIsisLfaNodesCovered = _TmnxIsisLfaNodesCovered_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 10, 1, 2),
    _TmnxIsisLfaNodesCovered_Type()
)
tmnxIsisLfaNodesCovered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisLfaNodesCovered.setStatus("current")
_TmnxIsisLfaTotalNodes_Type = Unsigned32
_TmnxIsisLfaTotalNodes_Object = MibTableColumn
tmnxIsisLfaTotalNodes = _TmnxIsisLfaTotalNodes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 10, 1, 3),
    _TmnxIsisLfaTotalNodes_Type()
)
tmnxIsisLfaTotalNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisLfaTotalNodes.setStatus("current")


class _TmnxIsisLfaNodeCoverage_Type(Unsigned32):
    """Custom type tmnxIsisLfaNodeCoverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_TmnxIsisLfaNodeCoverage_Type.__name__ = "Unsigned32"
_TmnxIsisLfaNodeCoverage_Object = MibTableColumn
tmnxIsisLfaNodeCoverage = _TmnxIsisLfaNodeCoverage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 10, 1, 4),
    _TmnxIsisLfaNodeCoverage_Type()
)
tmnxIsisLfaNodeCoverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisLfaNodeCoverage.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIsisLfaNodeCoverage.setUnits("hundredths of a percent")
_TmnxIsisLfaIPv4NodesCovered_Type = Unsigned32
_TmnxIsisLfaIPv4NodesCovered_Object = MibTableColumn
tmnxIsisLfaIPv4NodesCovered = _TmnxIsisLfaIPv4NodesCovered_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 10, 1, 5),
    _TmnxIsisLfaIPv4NodesCovered_Type()
)
tmnxIsisLfaIPv4NodesCovered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisLfaIPv4NodesCovered.setStatus("current")
_TmnxIsisLfaIPv4TotalNodes_Type = Unsigned32
_TmnxIsisLfaIPv4TotalNodes_Object = MibTableColumn
tmnxIsisLfaIPv4TotalNodes = _TmnxIsisLfaIPv4TotalNodes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 10, 1, 6),
    _TmnxIsisLfaIPv4TotalNodes_Type()
)
tmnxIsisLfaIPv4TotalNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisLfaIPv4TotalNodes.setStatus("current")


class _TmnxIsisLfaIPv4Coverage_Type(Unsigned32):
    """Custom type tmnxIsisLfaIPv4Coverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_TmnxIsisLfaIPv4Coverage_Type.__name__ = "Unsigned32"
_TmnxIsisLfaIPv4Coverage_Object = MibTableColumn
tmnxIsisLfaIPv4Coverage = _TmnxIsisLfaIPv4Coverage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 10, 1, 7),
    _TmnxIsisLfaIPv4Coverage_Type()
)
tmnxIsisLfaIPv4Coverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisLfaIPv4Coverage.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIsisLfaIPv4Coverage.setUnits("hundredths of a percent")
_TmnxIsisLfaIPv6NodesCovered_Type = Unsigned32
_TmnxIsisLfaIPv6NodesCovered_Object = MibTableColumn
tmnxIsisLfaIPv6NodesCovered = _TmnxIsisLfaIPv6NodesCovered_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 10, 1, 8),
    _TmnxIsisLfaIPv6NodesCovered_Type()
)
tmnxIsisLfaIPv6NodesCovered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisLfaIPv6NodesCovered.setStatus("current")
_TmnxIsisLfaIPv6TotalNodes_Type = Unsigned32
_TmnxIsisLfaIPv6TotalNodes_Object = MibTableColumn
tmnxIsisLfaIPv6TotalNodes = _TmnxIsisLfaIPv6TotalNodes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 10, 1, 9),
    _TmnxIsisLfaIPv6TotalNodes_Type()
)
tmnxIsisLfaIPv6TotalNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisLfaIPv6TotalNodes.setStatus("current")


class _TmnxIsisLfaIPv6Coverage_Type(Unsigned32):
    """Custom type tmnxIsisLfaIPv6Coverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_TmnxIsisLfaIPv6Coverage_Type.__name__ = "Unsigned32"
_TmnxIsisLfaIPv6Coverage_Object = MibTableColumn
tmnxIsisLfaIPv6Coverage = _TmnxIsisLfaIPv6Coverage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 10, 1, 10),
    _TmnxIsisLfaIPv6Coverage_Type()
)
tmnxIsisLfaIPv6Coverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisLfaIPv6Coverage.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIsisLfaIPv6Coverage.setUnits("hundredths of a percent")
_TmnxIsisExtTable_Object = MibTable
tmnxIsisExtTable = _TmnxIsisExtTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11)
)
if mibBuilder.loadTexts:
    tmnxIsisExtTable.setStatus("current")
_TmnxIsisExtEntry_Object = MibTableRow
tmnxIsisExtEntry = _TmnxIsisExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1)
)
if mibBuilder.loadTexts:
    tmnxIsisExtEntry.setStatus("current")
_TmnxIsisExLastChanged_Type = TimeStamp
_TmnxIsisExLastChanged_Object = MibTableColumn
tmnxIsisExLastChanged = _TmnxIsisExLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 1),
    _TmnxIsisExLastChanged_Type()
)
tmnxIsisExLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisExLastChanged.setStatus("current")


class _TmnxIsisLFAExcludePolicy1_Type(TNamedItemOrEmpty):
    """Custom type tmnxIsisLFAExcludePolicy1 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIsisLFAExcludePolicy1_Type.__name__ = "TNamedItemOrEmpty"
_TmnxIsisLFAExcludePolicy1_Object = MibTableColumn
tmnxIsisLFAExcludePolicy1 = _TmnxIsisLFAExcludePolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 2),
    _TmnxIsisLFAExcludePolicy1_Type()
)
tmnxIsisLFAExcludePolicy1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLFAExcludePolicy1.setStatus("current")


class _TmnxIsisLFAExcludePolicy2_Type(TNamedItemOrEmpty):
    """Custom type tmnxIsisLFAExcludePolicy2 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIsisLFAExcludePolicy2_Type.__name__ = "TNamedItemOrEmpty"
_TmnxIsisLFAExcludePolicy2_Object = MibTableColumn
tmnxIsisLFAExcludePolicy2 = _TmnxIsisLFAExcludePolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 3),
    _TmnxIsisLFAExcludePolicy2_Type()
)
tmnxIsisLFAExcludePolicy2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLFAExcludePolicy2.setStatus("current")


class _TmnxIsisLFAExcludePolicy3_Type(TNamedItemOrEmpty):
    """Custom type tmnxIsisLFAExcludePolicy3 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIsisLFAExcludePolicy3_Type.__name__ = "TNamedItemOrEmpty"
_TmnxIsisLFAExcludePolicy3_Object = MibTableColumn
tmnxIsisLFAExcludePolicy3 = _TmnxIsisLFAExcludePolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 4),
    _TmnxIsisLFAExcludePolicy3_Type()
)
tmnxIsisLFAExcludePolicy3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLFAExcludePolicy3.setStatus("current")


class _TmnxIsisLFAExcludePolicy4_Type(TNamedItemOrEmpty):
    """Custom type tmnxIsisLFAExcludePolicy4 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIsisLFAExcludePolicy4_Type.__name__ = "TNamedItemOrEmpty"
_TmnxIsisLFAExcludePolicy4_Object = MibTableColumn
tmnxIsisLFAExcludePolicy4 = _TmnxIsisLFAExcludePolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 5),
    _TmnxIsisLFAExcludePolicy4_Type()
)
tmnxIsisLFAExcludePolicy4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLFAExcludePolicy4.setStatus("current")


class _TmnxIsisLFAExcludePolicy5_Type(TNamedItemOrEmpty):
    """Custom type tmnxIsisLFAExcludePolicy5 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIsisLFAExcludePolicy5_Type.__name__ = "TNamedItemOrEmpty"
_TmnxIsisLFAExcludePolicy5_Object = MibTableColumn
tmnxIsisLFAExcludePolicy5 = _TmnxIsisLFAExcludePolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 6),
    _TmnxIsisLFAExcludePolicy5_Type()
)
tmnxIsisLFAExcludePolicy5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLFAExcludePolicy5.setStatus("current")
_TmnxIsisIfObjs_ObjectIdentity = ObjectIdentity
tmnxIsisIfObjs = _TmnxIsisIfObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2)
)
_TmnxIsisIfTable_Object = MibTable
tmnxIsisIfTable = _TmnxIsisIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxIsisIfTable.setStatus("current")
_TmnxIsisIfEntry_Object = MibTableRow
tmnxIsisIfEntry = _TmnxIsisIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1)
)
tmnxIsisIfEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
)
if mibBuilder.loadTexts:
    tmnxIsisIfEntry.setStatus("current")
_TmnxIsisIfRowStatus_Type = RowStatus
_TmnxIsisIfRowStatus_Object = MibTableColumn
tmnxIsisIfRowStatus = _TmnxIsisIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 1),
    _TmnxIsisIfRowStatus_Type()
)
tmnxIsisIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfRowStatus.setStatus("current")
_TmnxIsisIfLastChanged_Type = TimeStamp
_TmnxIsisIfLastChanged_Object = MibTableColumn
tmnxIsisIfLastChanged = _TmnxIsisIfLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 2),
    _TmnxIsisIfLastChanged_Type()
)
tmnxIsisIfLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisIfLastChanged.setStatus("current")


class _TmnxIsisIfAdminState_Type(TmnxAdminState):
    """Custom type tmnxIsisIfAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxIsisIfAdminState_Type.__name__ = "TmnxAdminState"
_TmnxIsisIfAdminState_Object = MibTableColumn
tmnxIsisIfAdminState = _TmnxIsisIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 3),
    _TmnxIsisIfAdminState_Type()
)
tmnxIsisIfAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfAdminState.setStatus("current")
_TmnxIsisIfOperState_Type = TmnxOperState
_TmnxIsisIfOperState_Object = MibTableColumn
tmnxIsisIfOperState = _TmnxIsisIfOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 4),
    _TmnxIsisIfOperState_Type()
)
tmnxIsisIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisIfOperState.setStatus("current")


class _TmnxIsisIfCsnpInterval_Type(Unsigned32):
    """Custom type tmnxIsisIfCsnpInterval based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmnxIsisIfCsnpInterval_Type.__name__ = "Unsigned32"
_TmnxIsisIfCsnpInterval_Object = MibTableColumn
tmnxIsisIfCsnpInterval = _TmnxIsisIfCsnpInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 5),
    _TmnxIsisIfCsnpInterval_Type()
)
tmnxIsisIfCsnpInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfCsnpInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIsisIfCsnpInterval.setUnits("seconds")


class _TmnxIsisIfHelloAuthKey_Type(OctetString):
    """Custom type tmnxIsisIfHelloAuthKey based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_TmnxIsisIfHelloAuthKey_Type.__name__ = "OctetString"
_TmnxIsisIfHelloAuthKey_Object = MibTableColumn
tmnxIsisIfHelloAuthKey = _TmnxIsisIfHelloAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 6),
    _TmnxIsisIfHelloAuthKey_Type()
)
tmnxIsisIfHelloAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfHelloAuthKey.setStatus("current")


class _TmnxIsisIfHelloAuthType_Type(Integer32):
    """Custom type tmnxIsisIfHelloAuthType based on Integer32"""
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
        *(("none", 1),
          ("password", 2),
          ("md5", 3))
    )


_TmnxIsisIfHelloAuthType_Type.__name__ = "Integer32"
_TmnxIsisIfHelloAuthType_Object = MibTableColumn
tmnxIsisIfHelloAuthType = _TmnxIsisIfHelloAuthType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 7),
    _TmnxIsisIfHelloAuthType_Type()
)
tmnxIsisIfHelloAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfHelloAuthType.setStatus("current")


class _TmnxIsisIfLspPacingInterval_Type(Unsigned32):
    """Custom type tmnxIsisIfLspPacingInterval based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TmnxIsisIfLspPacingInterval_Type.__name__ = "Unsigned32"
_TmnxIsisIfLspPacingInterval_Object = MibTableColumn
tmnxIsisIfLspPacingInterval = _TmnxIsisIfLspPacingInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 8),
    _TmnxIsisIfLspPacingInterval_Type()
)
tmnxIsisIfLspPacingInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfLspPacingInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIsisIfLspPacingInterval.setUnits("milliseconds")


class _TmnxIsisIfCircIndex_Type(Integer32):
    """Custom type tmnxIsisIfCircIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000000000),
    )


_TmnxIsisIfCircIndex_Type.__name__ = "Integer32"
_TmnxIsisIfCircIndex_Object = MibTableColumn
tmnxIsisIfCircIndex = _TmnxIsisIfCircIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 9),
    _TmnxIsisIfCircIndex_Type()
)
tmnxIsisIfCircIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisIfCircIndex.setStatus("current")


class _TmnxIsisIfRetransmitInterval_Type(Unsigned32):
    """Custom type tmnxIsisIfRetransmitInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmnxIsisIfRetransmitInterval_Type.__name__ = "Unsigned32"
_TmnxIsisIfRetransmitInterval_Object = MibTableColumn
tmnxIsisIfRetransmitInterval = _TmnxIsisIfRetransmitInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 10),
    _TmnxIsisIfRetransmitInterval_Type()
)
tmnxIsisIfRetransmitInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfRetransmitInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIsisIfRetransmitInterval.setUnits("seconds")


class _TmnxIsisIfTypeDefault_Type(TruthValue):
    """Custom type tmnxIsisIfTypeDefault based on TruthValue"""
    defaultValue = 1


_TmnxIsisIfTypeDefault_Type.__name__ = "TruthValue"
_TmnxIsisIfTypeDefault_Object = MibTableColumn
tmnxIsisIfTypeDefault = _TmnxIsisIfTypeDefault_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 11),
    _TmnxIsisIfTypeDefault_Type()
)
tmnxIsisIfTypeDefault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfTypeDefault.setStatus("current")


class _TmnxIsisIfEnableBfd_Type(TruthValue):
    """Custom type tmnxIsisIfEnableBfd based on TruthValue"""
    defaultValue = 2


_TmnxIsisIfEnableBfd_Type.__name__ = "TruthValue"
_TmnxIsisIfEnableBfd_Object = MibTableColumn
tmnxIsisIfEnableBfd = _TmnxIsisIfEnableBfd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 12),
    _TmnxIsisIfEnableBfd_Type()
)
tmnxIsisIfEnableBfd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfEnableBfd.setStatus("current")


class _TmnxIsisIfIPv6Unicast_Type(TruthValue):
    """Custom type tmnxIsisIfIPv6Unicast based on TruthValue"""
    defaultValue = 1


_TmnxIsisIfIPv6Unicast_Type.__name__ = "TruthValue"
_TmnxIsisIfIPv6Unicast_Object = MibTableColumn
tmnxIsisIfIPv6Unicast = _TmnxIsisIfIPv6Unicast_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 13),
    _TmnxIsisIfIPv6Unicast_Type()
)
tmnxIsisIfIPv6Unicast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfIPv6Unicast.setStatus("current")


class _TmnxIsisIfTeMetric_Type(Unsigned32):
    """Custom type tmnxIsisIfTeMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_TmnxIsisIfTeMetric_Type.__name__ = "Unsigned32"
_TmnxIsisIfTeMetric_Object = MibTableColumn
tmnxIsisIfTeMetric = _TmnxIsisIfTeMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 14),
    _TmnxIsisIfTeMetric_Type()
)
tmnxIsisIfTeMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisIfTeMetric.setStatus("current")
_TmnxIsisIfTeState_Type = TmnxOperState
_TmnxIsisIfTeState_Object = MibTableColumn
tmnxIsisIfTeState = _TmnxIsisIfTeState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 15),
    _TmnxIsisIfTeState_Type()
)
tmnxIsisIfTeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisIfTeState.setStatus("current")
_TmnxIsisIfAdminGroup_Type = Unsigned32
_TmnxIsisIfAdminGroup_Object = MibTableColumn
tmnxIsisIfAdminGroup = _TmnxIsisIfAdminGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 16),
    _TmnxIsisIfAdminGroup_Type()
)
tmnxIsisIfAdminGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisIfAdminGroup.setStatus("current")
_TmnxIsisIfLdpSyncState_Type = TmnxOperState
_TmnxIsisIfLdpSyncState_Object = MibTableColumn
tmnxIsisIfLdpSyncState = _TmnxIsisIfLdpSyncState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 17),
    _TmnxIsisIfLdpSyncState_Type()
)
tmnxIsisIfLdpSyncState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisIfLdpSyncState.setStatus("current")
_TmnxIsisIfLdpSyncMaxMetric_Type = TruthValue
_TmnxIsisIfLdpSyncMaxMetric_Object = MibTableColumn
tmnxIsisIfLdpSyncMaxMetric = _TmnxIsisIfLdpSyncMaxMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 18),
    _TmnxIsisIfLdpSyncMaxMetric_Type()
)
tmnxIsisIfLdpSyncMaxMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisIfLdpSyncMaxMetric.setStatus("current")


class _TmnxIsisIfLdpSyncTimerState_Type(Integer32):
    """Custom type tmnxIsisIfLdpSyncTimerState based on Integer32"""
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
        *(("waitForLdpAdj", 1),
          ("timerActive", 2),
          ("ldpExchgDone", 3),
          ("timerExpired", 4),
          ("manualExit", 5),
          ("disabled", 6))
    )


_TmnxIsisIfLdpSyncTimerState_Type.__name__ = "Integer32"
_TmnxIsisIfLdpSyncTimerState_Object = MibTableColumn
tmnxIsisIfLdpSyncTimerState = _TmnxIsisIfLdpSyncTimerState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 19),
    _TmnxIsisIfLdpSyncTimerState_Type()
)
tmnxIsisIfLdpSyncTimerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisIfLdpSyncTimerState.setStatus("current")


class _TmnxIsisIfLdpSyncTimeLeft_Type(Unsigned32):
    """Custom type tmnxIsisIfLdpSyncTimeLeft based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1800),
    )


_TmnxIsisIfLdpSyncTimeLeft_Type.__name__ = "Unsigned32"
_TmnxIsisIfLdpSyncTimeLeft_Object = MibTableColumn
tmnxIsisIfLdpSyncTimeLeft = _TmnxIsisIfLdpSyncTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 20),
    _TmnxIsisIfLdpSyncTimeLeft_Type()
)
tmnxIsisIfLdpSyncTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisIfLdpSyncTimeLeft.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIsisIfLdpSyncTimeLeft.setUnits("seconds")


class _TmnxIsisIfRouteTag_Type(Unsigned32):
    """Custom type tmnxIsisIfRouteTag based on Unsigned32"""
    defaultValue = 0


_TmnxIsisIfRouteTag_Type.__name__ = "Unsigned32"
_TmnxIsisIfRouteTag_Object = MibTableColumn
tmnxIsisIfRouteTag = _TmnxIsisIfRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 21),
    _TmnxIsisIfRouteTag_Type()
)
tmnxIsisIfRouteTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfRouteTag.setStatus("current")


class _TmnxIsisIfIPv6EnableBfd_Type(TruthValue):
    """Custom type tmnxIsisIfIPv6EnableBfd based on TruthValue"""
    defaultValue = 2


_TmnxIsisIfIPv6EnableBfd_Type.__name__ = "TruthValue"
_TmnxIsisIfIPv6EnableBfd_Object = MibTableColumn
tmnxIsisIfIPv6EnableBfd = _TmnxIsisIfIPv6EnableBfd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 22),
    _TmnxIsisIfIPv6EnableBfd_Type()
)
tmnxIsisIfIPv6EnableBfd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfIPv6EnableBfd.setStatus("current")


class _TmnxIsisIfHelloAuth_Type(TruthValue):
    """Custom type tmnxIsisIfHelloAuth based on TruthValue"""
    defaultValue = 1


_TmnxIsisIfHelloAuth_Type.__name__ = "TruthValue"
_TmnxIsisIfHelloAuth_Object = MibTableColumn
tmnxIsisIfHelloAuth = _TmnxIsisIfHelloAuth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 23),
    _TmnxIsisIfHelloAuth_Type()
)
tmnxIsisIfHelloAuth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfHelloAuth.setStatus("current")


class _TmnxIsisIfLoopfreeAltExclude_Type(TruthValue):
    """Custom type tmnxIsisIfLoopfreeAltExclude based on TruthValue"""
    defaultValue = 2


_TmnxIsisIfLoopfreeAltExclude_Type.__name__ = "TruthValue"
_TmnxIsisIfLoopfreeAltExclude_Object = MibTableColumn
tmnxIsisIfLoopfreeAltExclude = _TmnxIsisIfLoopfreeAltExclude_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 24),
    _TmnxIsisIfLoopfreeAltExclude_Type()
)
tmnxIsisIfLoopfreeAltExclude.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfLoopfreeAltExclude.setStatus("current")


class _TmnxIsisIfOperType_Type(Integer32):
    """Custom type tmnxIsisIfOperType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 1),
          ("ptToPt", 2))
    )


_TmnxIsisIfOperType_Type.__name__ = "Integer32"
_TmnxIsisIfOperType_Object = MibTableColumn
tmnxIsisIfOperType = _TmnxIsisIfOperType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 25),
    _TmnxIsisIfOperType_Type()
)
tmnxIsisIfOperType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisIfOperType.setStatus("current")


class _TmnxIsisIfIPv4Mcast_Type(TruthValue):
    """Custom type tmnxIsisIfIPv4Mcast based on TruthValue"""
    defaultValue = 1


_TmnxIsisIfIPv4Mcast_Type.__name__ = "TruthValue"
_TmnxIsisIfIPv4Mcast_Object = MibTableColumn
tmnxIsisIfIPv4Mcast = _TmnxIsisIfIPv4Mcast_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 26),
    _TmnxIsisIfIPv4Mcast_Type()
)
tmnxIsisIfIPv4Mcast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfIPv4Mcast.setStatus("current")


class _TmnxIsisIfIPv6Mcast_Type(TruthValue):
    """Custom type tmnxIsisIfIPv6Mcast based on TruthValue"""
    defaultValue = 1


_TmnxIsisIfIPv6Mcast_Type.__name__ = "TruthValue"
_TmnxIsisIfIPv6Mcast_Object = MibTableColumn
tmnxIsisIfIPv6Mcast = _TmnxIsisIfIPv6Mcast_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 27),
    _TmnxIsisIfIPv6Mcast_Type()
)
tmnxIsisIfIPv6Mcast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfIPv6Mcast.setStatus("current")


class _TmnxIsisIfBerState_Type(Integer32):
    """Custom type tmnxIsisIfBerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("sd", 1),
          ("sf", 2))
    )


_TmnxIsisIfBerState_Type.__name__ = "Integer32"
_TmnxIsisIfBerState_Object = MibTableColumn
tmnxIsisIfBerState = _TmnxIsisIfBerState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 28),
    _TmnxIsisIfBerState_Type()
)
tmnxIsisIfBerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisIfBerState.setStatus("current")


class _TmnxIsisIfIPv4IncludeBfdTlv_Type(TruthValue):
    """Custom type tmnxIsisIfIPv4IncludeBfdTlv based on TruthValue"""
    defaultValue = 2


_TmnxIsisIfIPv4IncludeBfdTlv_Type.__name__ = "TruthValue"
_TmnxIsisIfIPv4IncludeBfdTlv_Object = MibTableColumn
tmnxIsisIfIPv4IncludeBfdTlv = _TmnxIsisIfIPv4IncludeBfdTlv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 29),
    _TmnxIsisIfIPv4IncludeBfdTlv_Type()
)
tmnxIsisIfIPv4IncludeBfdTlv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfIPv4IncludeBfdTlv.setStatus("current")


class _TmnxIsisIfIPv6IncludeBfdTlv_Type(TruthValue):
    """Custom type tmnxIsisIfIPv6IncludeBfdTlv based on TruthValue"""
    defaultValue = 2


_TmnxIsisIfIPv6IncludeBfdTlv_Type.__name__ = "TruthValue"
_TmnxIsisIfIPv6IncludeBfdTlv_Object = MibTableColumn
tmnxIsisIfIPv6IncludeBfdTlv = _TmnxIsisIfIPv6IncludeBfdTlv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 30),
    _TmnxIsisIfIPv6IncludeBfdTlv_Type()
)
tmnxIsisIfIPv6IncludeBfdTlv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfIPv6IncludeBfdTlv.setStatus("current")


class _TmnxIsisIfHelloAuthKeyChain_Type(TNamedItemOrEmpty):
    """Custom type tmnxIsisIfHelloAuthKeyChain based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIsisIfHelloAuthKeyChain_Type.__name__ = "TNamedItemOrEmpty"
_TmnxIsisIfHelloAuthKeyChain_Object = MibTableColumn
tmnxIsisIfHelloAuthKeyChain = _TmnxIsisIfHelloAuthKeyChain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 31),
    _TmnxIsisIfHelloAuthKeyChain_Type()
)
tmnxIsisIfHelloAuthKeyChain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisIfHelloAuthKeyChain.setStatus("current")


class _TmnxIsisIfRouteNHTemplate_Type(TNamedItemOrEmpty):
    """Custom type tmnxIsisIfRouteNHTemplate based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIsisIfRouteNHTemplate_Type.__name__ = "TNamedItemOrEmpty"
_TmnxIsisIfRouteNHTemplate_Object = MibTableColumn
tmnxIsisIfRouteNHTemplate = _TmnxIsisIfRouteNHTemplate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 32),
    _TmnxIsisIfRouteNHTemplate_Type()
)
tmnxIsisIfRouteNHTemplate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfRouteNHTemplate.setStatus("current")
_TmnxIsisIfLevelTable_Object = MibTable
tmnxIsisIfLevelTable = _TmnxIsisIfLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 2)
)
if mibBuilder.loadTexts:
    tmnxIsisIfLevelTable.setStatus("current")
_TmnxIsisIfLevelEntry_Object = MibTableRow
tmnxIsisIfLevelEntry = _TmnxIsisIfLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 2, 1)
)
tmnxIsisIfLevelEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisIfLevel"),
)
if mibBuilder.loadTexts:
    tmnxIsisIfLevelEntry.setStatus("current")


class _TmnxIsisIfLevel_Type(Integer32):
    """Custom type tmnxIsisIfLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("level1", 1),
          ("level2", 2))
    )


_TmnxIsisIfLevel_Type.__name__ = "Integer32"
_TmnxIsisIfLevel_Object = MibTableColumn
tmnxIsisIfLevel = _TmnxIsisIfLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 2, 1, 1),
    _TmnxIsisIfLevel_Type()
)
tmnxIsisIfLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisIfLevel.setStatus("current")
_TmnxIsisIfLevelLastChangeTime_Type = TimeStamp
_TmnxIsisIfLevelLastChangeTime_Object = MibTableColumn
tmnxIsisIfLevelLastChangeTime = _TmnxIsisIfLevelLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 2, 1, 2),
    _TmnxIsisIfLevelLastChangeTime_Type()
)
tmnxIsisIfLevelLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisIfLevelLastChangeTime.setStatus("current")


class _TmnxIsisIfLevelHelloAuthKey_Type(OctetString):
    """Custom type tmnxIsisIfLevelHelloAuthKey based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_TmnxIsisIfLevelHelloAuthKey_Type.__name__ = "OctetString"
_TmnxIsisIfLevelHelloAuthKey_Object = MibTableColumn
tmnxIsisIfLevelHelloAuthKey = _TmnxIsisIfLevelHelloAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 2, 1, 3),
    _TmnxIsisIfLevelHelloAuthKey_Type()
)
tmnxIsisIfLevelHelloAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfLevelHelloAuthKey.setStatus("current")


class _TmnxIsisIfLevelHelloAuthType_Type(Integer32):
    """Custom type tmnxIsisIfLevelHelloAuthType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("useGlobal", 0),
          ("none", 1),
          ("password", 2),
          ("md5", 3))
    )


_TmnxIsisIfLevelHelloAuthType_Type.__name__ = "Integer32"
_TmnxIsisIfLevelHelloAuthType_Object = MibTableColumn
tmnxIsisIfLevelHelloAuthType = _TmnxIsisIfLevelHelloAuthType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 2, 1, 4),
    _TmnxIsisIfLevelHelloAuthType_Type()
)
tmnxIsisIfLevelHelloAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfLevelHelloAuthType.setStatus("current")


class _TmnxIsisIfLevelPassive_Type(TruthValue):
    """Custom type tmnxIsisIfLevelPassive based on TruthValue"""
    defaultValue = 2


_TmnxIsisIfLevelPassive_Type.__name__ = "TruthValue"
_TmnxIsisIfLevelPassive_Object = MibTableColumn
tmnxIsisIfLevelPassive = _TmnxIsisIfLevelPassive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 2, 1, 5),
    _TmnxIsisIfLevelPassive_Type()
)
tmnxIsisIfLevelPassive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfLevelPassive.setStatus("current")
_TmnxIsisIfLevelNumAdjacencies_Type = Unsigned32
_TmnxIsisIfLevelNumAdjacencies_Object = MibTableColumn
tmnxIsisIfLevelNumAdjacencies = _TmnxIsisIfLevelNumAdjacencies_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 2, 1, 6),
    _TmnxIsisIfLevelNumAdjacencies_Type()
)
tmnxIsisIfLevelNumAdjacencies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisIfLevelNumAdjacencies.setStatus("current")


class _TmnxIsisIfLevelISPriority_Type(Unsigned32):
    """Custom type tmnxIsisIfLevelISPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_TmnxIsisIfLevelISPriority_Type.__name__ = "Unsigned32"
_TmnxIsisIfLevelISPriority_Object = MibTableColumn
tmnxIsisIfLevelISPriority = _TmnxIsisIfLevelISPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 2, 1, 7),
    _TmnxIsisIfLevelISPriority_Type()
)
tmnxIsisIfLevelISPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfLevelISPriority.setStatus("current")


class _TmnxIsisIfLevelHelloTimer_Type(Unsigned32):
    """Custom type tmnxIsisIfLevelHelloTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20000),
    )


_TmnxIsisIfLevelHelloTimer_Type.__name__ = "Unsigned32"
_TmnxIsisIfLevelHelloTimer_Object = MibTableColumn
tmnxIsisIfLevelHelloTimer = _TmnxIsisIfLevelHelloTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 2, 1, 8),
    _TmnxIsisIfLevelHelloTimer_Type()
)
tmnxIsisIfLevelHelloTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfLevelHelloTimer.setStatus("current")


class _TmnxIsisIfLevelAdminMetric_Type(Unsigned32):
    """Custom type tmnxIsisIfLevelAdminMetric based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_TmnxIsisIfLevelAdminMetric_Type.__name__ = "Unsigned32"
_TmnxIsisIfLevelAdminMetric_Object = MibTableColumn
tmnxIsisIfLevelAdminMetric = _TmnxIsisIfLevelAdminMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 2, 1, 9),
    _TmnxIsisIfLevelAdminMetric_Type()
)
tmnxIsisIfLevelAdminMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfLevelAdminMetric.setStatus("current")


class _TmnxIsisIfLevelOperMetric_Type(Unsigned32):
    """Custom type tmnxIsisIfLevelOperMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_TmnxIsisIfLevelOperMetric_Type.__name__ = "Unsigned32"
_TmnxIsisIfLevelOperMetric_Object = MibTableColumn
tmnxIsisIfLevelOperMetric = _TmnxIsisIfLevelOperMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 2, 1, 10),
    _TmnxIsisIfLevelOperMetric_Type()
)
tmnxIsisIfLevelOperMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisIfLevelOperMetric.setStatus("current")


class _TmnxIsisIfLvlIPv6UcastAdmMet_Type(Unsigned32):
    """Custom type tmnxIsisIfLvlIPv6UcastAdmMet based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_TmnxIsisIfLvlIPv6UcastAdmMet_Type.__name__ = "Unsigned32"
_TmnxIsisIfLvlIPv6UcastAdmMet_Object = MibTableColumn
tmnxIsisIfLvlIPv6UcastAdmMet = _TmnxIsisIfLvlIPv6UcastAdmMet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 2, 1, 11),
    _TmnxIsisIfLvlIPv6UcastAdmMet_Type()
)
tmnxIsisIfLvlIPv6UcastAdmMet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfLvlIPv6UcastAdmMet.setStatus("current")


class _TmnxIsisIfLvlIPv6UcastOperMet_Type(Unsigned32):
    """Custom type tmnxIsisIfLvlIPv6UcastOperMet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_TmnxIsisIfLvlIPv6UcastOperMet_Type.__name__ = "Unsigned32"
_TmnxIsisIfLvlIPv6UcastOperMet_Object = MibTableColumn
tmnxIsisIfLvlIPv6UcastOperMet = _TmnxIsisIfLvlIPv6UcastOperMet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 2, 1, 12),
    _TmnxIsisIfLvlIPv6UcastOperMet_Type()
)
tmnxIsisIfLvlIPv6UcastOperMet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisIfLvlIPv6UcastOperMet.setStatus("current")


class _TmnxIsisIfLvlIPv4McastAdmMetric_Type(Unsigned32):
    """Custom type tmnxIsisIfLvlIPv4McastAdmMetric based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_TmnxIsisIfLvlIPv4McastAdmMetric_Type.__name__ = "Unsigned32"
_TmnxIsisIfLvlIPv4McastAdmMetric_Object = MibTableColumn
tmnxIsisIfLvlIPv4McastAdmMetric = _TmnxIsisIfLvlIPv4McastAdmMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 2, 1, 13),
    _TmnxIsisIfLvlIPv4McastAdmMetric_Type()
)
tmnxIsisIfLvlIPv4McastAdmMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfLvlIPv4McastAdmMetric.setStatus("current")


class _TmnxIsisIfLvlIPv6McastAdmMetric_Type(Unsigned32):
    """Custom type tmnxIsisIfLvlIPv6McastAdmMetric based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_TmnxIsisIfLvlIPv6McastAdmMetric_Type.__name__ = "Unsigned32"
_TmnxIsisIfLvlIPv6McastAdmMetric_Object = MibTableColumn
tmnxIsisIfLvlIPv6McastAdmMetric = _TmnxIsisIfLvlIPv6McastAdmMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 2, 1, 14),
    _TmnxIsisIfLvlIPv6McastAdmMetric_Type()
)
tmnxIsisIfLvlIPv6McastAdmMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfLvlIPv6McastAdmMetric.setStatus("current")


class _TmnxIsisIfLevelLinkGroupName_Type(TNamedItemOrEmpty):
    """Custom type tmnxIsisIfLevelLinkGroupName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIsisIfLevelLinkGroupName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxIsisIfLevelLinkGroupName_Object = MibTableColumn
tmnxIsisIfLevelLinkGroupName = _TmnxIsisIfLevelLinkGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 2, 1, 15),
    _TmnxIsisIfLevelLinkGroupName_Type()
)
tmnxIsisIfLevelLinkGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfLevelLinkGroupName.setStatus("current")


class _TmnxIsisIfLevelSdOffset_Type(Unsigned32):
    """Custom type tmnxIsisIfLevelSdOffset based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_TmnxIsisIfLevelSdOffset_Type.__name__ = "Unsigned32"
_TmnxIsisIfLevelSdOffset_Object = MibTableColumn
tmnxIsisIfLevelSdOffset = _TmnxIsisIfLevelSdOffset_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 2, 1, 16),
    _TmnxIsisIfLevelSdOffset_Type()
)
tmnxIsisIfLevelSdOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfLevelSdOffset.setStatus("current")


class _TmnxIsisIfLevelSfOffset_Type(Unsigned32):
    """Custom type tmnxIsisIfLevelSfOffset based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_TmnxIsisIfLevelSfOffset_Type.__name__ = "Unsigned32"
_TmnxIsisIfLevelSfOffset_Object = MibTableColumn
tmnxIsisIfLevelSfOffset = _TmnxIsisIfLevelSfOffset_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 2, 1, 17),
    _TmnxIsisIfLevelSfOffset_Type()
)
tmnxIsisIfLevelSfOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfLevelSfOffset.setStatus("current")


class _TmnxIsisIfLvlIPv4McastOperMetric_Type(Unsigned32):
    """Custom type tmnxIsisIfLvlIPv4McastOperMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_TmnxIsisIfLvlIPv4McastOperMetric_Type.__name__ = "Unsigned32"
_TmnxIsisIfLvlIPv4McastOperMetric_Object = MibTableColumn
tmnxIsisIfLvlIPv4McastOperMetric = _TmnxIsisIfLvlIPv4McastOperMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 2, 1, 18),
    _TmnxIsisIfLvlIPv4McastOperMetric_Type()
)
tmnxIsisIfLvlIPv4McastOperMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisIfLvlIPv4McastOperMetric.setStatus("current")


class _TmnxIsisIfLvlIPv6McastOperMetric_Type(Unsigned32):
    """Custom type tmnxIsisIfLvlIPv6McastOperMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_TmnxIsisIfLvlIPv6McastOperMetric_Type.__name__ = "Unsigned32"
_TmnxIsisIfLvlIPv6McastOperMetric_Object = MibTableColumn
tmnxIsisIfLvlIPv6McastOperMetric = _TmnxIsisIfLvlIPv6McastOperMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 2, 1, 19),
    _TmnxIsisIfLvlIPv6McastOperMetric_Type()
)
tmnxIsisIfLvlIPv6McastOperMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisIfLvlIPv6McastOperMetric.setStatus("current")


class _TmnxIsisIfLevelHelloAuthKeyChain_Type(TNamedItemOrEmpty):
    """Custom type tmnxIsisIfLevelHelloAuthKeyChain based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIsisIfLevelHelloAuthKeyChain_Type.__name__ = "TNamedItemOrEmpty"
_TmnxIsisIfLevelHelloAuthKeyChain_Object = MibTableColumn
tmnxIsisIfLevelHelloAuthKeyChain = _TmnxIsisIfLevelHelloAuthKeyChain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 2, 1, 20),
    _TmnxIsisIfLevelHelloAuthKeyChain_Type()
)
tmnxIsisIfLevelHelloAuthKeyChain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisIfLevelHelloAuthKeyChain.setStatus("current")
_TmnxIsisAdjObjs_ObjectIdentity = ObjectIdentity
tmnxIsisAdjObjs = _TmnxIsisAdjObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 3)
)
_TmnxIsisISAdjTable_Object = MibTable
tmnxIsisISAdjTable = _TmnxIsisISAdjTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 3, 1)
)
if mibBuilder.loadTexts:
    tmnxIsisISAdjTable.setStatus("current")
_TmnxIsisISAdjEntry_Object = MibTableRow
tmnxIsisISAdjEntry = _TmnxIsisISAdjEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 3, 1, 1)
)
tmnxIsisISAdjEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "ISIS-MIB", "isisCircIndex"),
    (0, "ISIS-MIB", "isisISAdjIndex"),
)
if mibBuilder.loadTexts:
    tmnxIsisISAdjEntry.setStatus("current")


class _TmnxIsisISAdjExpiresIn_Type(Integer32):
    """Custom type tmnxIsisISAdjExpiresIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmnxIsisISAdjExpiresIn_Type.__name__ = "Integer32"
_TmnxIsisISAdjExpiresIn_Object = MibTableColumn
tmnxIsisISAdjExpiresIn = _TmnxIsisISAdjExpiresIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 3, 1, 1, 1),
    _TmnxIsisISAdjExpiresIn_Type()
)
tmnxIsisISAdjExpiresIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisISAdjExpiresIn.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIsisISAdjExpiresIn.setUnits("seconds")


class _TmnxIsisISAdjCircLevel_Type(Integer32):
    """Custom type tmnxIsisISAdjCircLevel based on Integer32"""
    defaultValue = 4

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
        *(("level1", 1),
          ("level2", 2),
          ("level1L2", 3),
          ("unknown", 4))
    )


_TmnxIsisISAdjCircLevel_Type.__name__ = "Integer32"
_TmnxIsisISAdjCircLevel_Object = MibTableColumn
tmnxIsisISAdjCircLevel = _TmnxIsisISAdjCircLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 3, 1, 1, 2),
    _TmnxIsisISAdjCircLevel_Type()
)
tmnxIsisISAdjCircLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisISAdjCircLevel.setStatus("current")
_TmnxIsisISAdjNeighborIP_Type = IpAddress
_TmnxIsisISAdjNeighborIP_Object = MibTableColumn
tmnxIsisISAdjNeighborIP = _TmnxIsisISAdjNeighborIP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 3, 1, 1, 3),
    _TmnxIsisISAdjNeighborIP_Type()
)
tmnxIsisISAdjNeighborIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisISAdjNeighborIP.setStatus("current")
_TmnxIsisISAdjRestartSupport_Type = TruthValue
_TmnxIsisISAdjRestartSupport_Object = MibTableColumn
tmnxIsisISAdjRestartSupport = _TmnxIsisISAdjRestartSupport_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 3, 1, 1, 4),
    _TmnxIsisISAdjRestartSupport_Type()
)
tmnxIsisISAdjRestartSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisISAdjRestartSupport.setStatus("current")


class _TmnxIsisISAdjRestartStatus_Type(Integer32):
    """Custom type tmnxIsisISAdjRestartStatus based on Integer32"""
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
        *(("notHelping", 1),
          ("restarting", 2),
          ("restartComplete", 3),
          ("helping", 4))
    )


_TmnxIsisISAdjRestartStatus_Type.__name__ = "Integer32"
_TmnxIsisISAdjRestartStatus_Object = MibTableColumn
tmnxIsisISAdjRestartStatus = _TmnxIsisISAdjRestartStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 3, 1, 1, 5),
    _TmnxIsisISAdjRestartStatus_Type()
)
tmnxIsisISAdjRestartStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisISAdjRestartStatus.setStatus("current")
_TmnxIsisISAdjRestartSupressed_Type = TruthValue
_TmnxIsisISAdjRestartSupressed_Object = MibTableColumn
tmnxIsisISAdjRestartSupressed = _TmnxIsisISAdjRestartSupressed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 3, 1, 1, 6),
    _TmnxIsisISAdjRestartSupressed_Type()
)
tmnxIsisISAdjRestartSupressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisISAdjRestartSupressed.setStatus("current")
_TmnxIsisISAdjNumRestarts_Type = Unsigned32
_TmnxIsisISAdjNumRestarts_Object = MibTableColumn
tmnxIsisISAdjNumRestarts = _TmnxIsisISAdjNumRestarts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 3, 1, 1, 7),
    _TmnxIsisISAdjNumRestarts_Type()
)
tmnxIsisISAdjNumRestarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisISAdjNumRestarts.setStatus("current")
_TmnxIsisISAdjLastRestartTime_Type = TimeStamp
_TmnxIsisISAdjLastRestartTime_Object = MibTableColumn
tmnxIsisISAdjLastRestartTime = _TmnxIsisISAdjLastRestartTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 3, 1, 1, 8),
    _TmnxIsisISAdjLastRestartTime_Type()
)
tmnxIsisISAdjLastRestartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisISAdjLastRestartTime.setStatus("current")
_TmnxIsisISAdjNeighborIPv6Type_Type = InetAddressType
_TmnxIsisISAdjNeighborIPv6Type_Object = MibTableColumn
tmnxIsisISAdjNeighborIPv6Type = _TmnxIsisISAdjNeighborIPv6Type_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 3, 1, 1, 9),
    _TmnxIsisISAdjNeighborIPv6Type_Type()
)
tmnxIsisISAdjNeighborIPv6Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisISAdjNeighborIPv6Type.setStatus("current")


class _TmnxIsisISAdjNeighborIPv6_Type(InetAddress):
    """Custom type tmnxIsisISAdjNeighborIPv6 based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxIsisISAdjNeighborIPv6_Type.__name__ = "InetAddress"
_TmnxIsisISAdjNeighborIPv6_Object = MibTableColumn
tmnxIsisISAdjNeighborIPv6 = _TmnxIsisISAdjNeighborIPv6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 3, 1, 1, 10),
    _TmnxIsisISAdjNeighborIPv6_Type()
)
tmnxIsisISAdjNeighborIPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisISAdjNeighborIPv6.setStatus("current")
_TmnxIsisISAdjMtEnabled_Type = TruthValue
_TmnxIsisISAdjMtEnabled_Object = MibTableColumn
tmnxIsisISAdjMtEnabled = _TmnxIsisISAdjMtEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 3, 1, 1, 11),
    _TmnxIsisISAdjMtEnabled_Type()
)
tmnxIsisISAdjMtEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisISAdjMtEnabled.setStatus("current")
_TmnxIsisISAdjMtId0_Type = TruthValue
_TmnxIsisISAdjMtId0_Object = MibTableColumn
tmnxIsisISAdjMtId0 = _TmnxIsisISAdjMtId0_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 3, 1, 1, 12),
    _TmnxIsisISAdjMtId0_Type()
)
tmnxIsisISAdjMtId0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisISAdjMtId0.setStatus("current")
_TmnxIsisISAdjMtId2_Type = TruthValue
_TmnxIsisISAdjMtId2_Object = MibTableColumn
tmnxIsisISAdjMtId2 = _TmnxIsisISAdjMtId2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 3, 1, 1, 13),
    _TmnxIsisISAdjMtId2_Type()
)
tmnxIsisISAdjMtId2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisISAdjMtId2.setStatus("current")
_TmnxIsisISAdjMtId3_Type = TruthValue
_TmnxIsisISAdjMtId3_Object = MibTableColumn
tmnxIsisISAdjMtId3 = _TmnxIsisISAdjMtId3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 3, 1, 1, 14),
    _TmnxIsisISAdjMtId3_Type()
)
tmnxIsisISAdjMtId3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisISAdjMtId3.setStatus("current")
_TmnxIsisISAdjMtId4_Type = TruthValue
_TmnxIsisISAdjMtId4_Object = MibTableColumn
tmnxIsisISAdjMtId4 = _TmnxIsisISAdjMtId4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 3, 1, 1, 15),
    _TmnxIsisISAdjMtId4_Type()
)
tmnxIsisISAdjMtId4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisISAdjMtId4.setStatus("current")
_TmnxIsisNotificationObjs_ObjectIdentity = ObjectIdentity
tmnxIsisNotificationObjs = _TmnxIsisNotificationObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 4)
)
_TmnxIsisNotificationTable_Object = MibTable
tmnxIsisNotificationTable = _TmnxIsisNotificationTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 4, 1)
)
if mibBuilder.loadTexts:
    tmnxIsisNotificationTable.setStatus("current")
_TmnxIsisNotificationEntry_Object = MibTableRow
tmnxIsisNotificationEntry = _TmnxIsisNotificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 4, 1, 1)
)
tmnxIsisNotificationEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ISIS-MIB", "isisSysInstance"),
)
if mibBuilder.loadTexts:
    tmnxIsisNotificationEntry.setStatus("current")


class _TmnxIsisNotifTrapLSPID_Type(OctetString):
    """Custom type tmnxIsisNotifTrapLSPID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 8),
    )


_TmnxIsisNotifTrapLSPID_Type.__name__ = "OctetString"
_TmnxIsisNotifTrapLSPID_Object = MibTableColumn
tmnxIsisNotifTrapLSPID = _TmnxIsisNotifTrapLSPID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 4, 1, 1, 1),
    _TmnxIsisNotifTrapLSPID_Type()
)
tmnxIsisNotifTrapLSPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisNotifTrapLSPID.setStatus("current")


class _TmnxIsisNotifSystemLevel_Type(Integer32):
    """Custom type tmnxIsisNotifSystemLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("l1", 1),
          ("l2", 2),
          ("l1l2", 3))
    )


_TmnxIsisNotifSystemLevel_Type.__name__ = "Integer32"
_TmnxIsisNotifSystemLevel_Object = MibTableColumn
tmnxIsisNotifSystemLevel = _TmnxIsisNotifSystemLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 4, 1, 1, 2),
    _TmnxIsisNotifSystemLevel_Type()
)
tmnxIsisNotifSystemLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisNotifSystemLevel.setStatus("current")


class _TmnxIsisNotifPDUFragment_Type(OctetString):
    """Custom type tmnxIsisNotifPDUFragment based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TmnxIsisNotifPDUFragment_Type.__name__ = "OctetString"
_TmnxIsisNotifPDUFragment_Object = MibTableColumn
tmnxIsisNotifPDUFragment = _TmnxIsisNotifPDUFragment_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 4, 1, 1, 3),
    _TmnxIsisNotifPDUFragment_Type()
)
tmnxIsisNotifPDUFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisNotifPDUFragment.setStatus("current")


class _TmnxIsisNotifFieldLen_Type(Integer32):
    """Custom type tmnxIsisNotifFieldLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxIsisNotifFieldLen_Type.__name__ = "Integer32"
_TmnxIsisNotifFieldLen_Object = MibTableColumn
tmnxIsisNotifFieldLen = _TmnxIsisNotifFieldLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 4, 1, 1, 4),
    _TmnxIsisNotifFieldLen_Type()
)
tmnxIsisNotifFieldLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisNotifFieldLen.setStatus("current")


class _TmnxIsisNotifMaxAreaAddress_Type(Integer32):
    """Custom type tmnxIsisNotifMaxAreaAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxIsisNotifMaxAreaAddress_Type.__name__ = "Integer32"
_TmnxIsisNotifMaxAreaAddress_Object = MibTableColumn
tmnxIsisNotifMaxAreaAddress = _TmnxIsisNotifMaxAreaAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 4, 1, 1, 5),
    _TmnxIsisNotifMaxAreaAddress_Type()
)
tmnxIsisNotifMaxAreaAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisNotifMaxAreaAddress.setStatus("current")


class _TmnxIsisNotifProtocolVersion_Type(Integer32):
    """Custom type tmnxIsisNotifProtocolVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxIsisNotifProtocolVersion_Type.__name__ = "Integer32"
_TmnxIsisNotifProtocolVersion_Object = MibTableColumn
tmnxIsisNotifProtocolVersion = _TmnxIsisNotifProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 4, 1, 1, 6),
    _TmnxIsisNotifProtocolVersion_Type()
)
tmnxIsisNotifProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisNotifProtocolVersion.setStatus("current")


class _TmnxIsisNotifLSPSize_Type(Integer32):
    """Custom type tmnxIsisNotifLSPSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TmnxIsisNotifLSPSize_Type.__name__ = "Integer32"
_TmnxIsisNotifLSPSize_Object = MibTableColumn
tmnxIsisNotifLSPSize = _TmnxIsisNotifLSPSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 4, 1, 1, 7),
    _TmnxIsisNotifLSPSize_Type()
)
tmnxIsisNotifLSPSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisNotifLSPSize.setStatus("current")


class _TmnxIsisNotifOriginatingBuffSize_Type(Integer32):
    """Custom type tmnxIsisNotifOriginatingBuffSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TmnxIsisNotifOriginatingBuffSize_Type.__name__ = "Integer32"
_TmnxIsisNotifOriginatingBuffSize_Object = MibTableColumn
tmnxIsisNotifOriginatingBuffSize = _TmnxIsisNotifOriginatingBuffSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 4, 1, 1, 8),
    _TmnxIsisNotifOriginatingBuffSize_Type()
)
tmnxIsisNotifOriginatingBuffSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisNotifOriginatingBuffSize.setStatus("current")


class _TmnxIsisNotifProtocolsSupported_Type(OctetString):
    """Custom type tmnxIsisNotifProtocolsSupported based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxIsisNotifProtocolsSupported_Type.__name__ = "OctetString"
_TmnxIsisNotifProtocolsSupported_Object = MibTableColumn
tmnxIsisNotifProtocolsSupported = _TmnxIsisNotifProtocolsSupported_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 4, 1, 1, 9),
    _TmnxIsisNotifProtocolsSupported_Type()
)
tmnxIsisNotifProtocolsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisNotifProtocolsSupported.setStatus("current")


class _TmnxIsisNotifNbrSysId_Type(OctetString):
    """Custom type tmnxIsisNotifNbrSysId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_TmnxIsisNotifNbrSysId_Type.__name__ = "OctetString"
_TmnxIsisNotifNbrSysId_Object = MibTableColumn
tmnxIsisNotifNbrSysId = _TmnxIsisNotifNbrSysId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 4, 1, 1, 10),
    _TmnxIsisNotifNbrSysId_Type()
)
tmnxIsisNotifNbrSysId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxIsisNotifNbrSysId.setStatus("current")


class _TmnxIsisFailureReasonCode_Type(Integer32):
    """Custom type tmnxIsisFailureReasonCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("outOfResources", 1)
    )


_TmnxIsisFailureReasonCode_Type.__name__ = "Integer32"
_TmnxIsisFailureReasonCode_Object = MibScalar
tmnxIsisFailureReasonCode = _TmnxIsisFailureReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 4, 4),
    _TmnxIsisFailureReasonCode_Type()
)
tmnxIsisFailureReasonCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxIsisFailureReasonCode.setStatus("current")
_TmnxIsisNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxIsisNotifyPrefix = _TmnxIsisNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88)
)
_TmnxIsisNotifications_ObjectIdentity = ObjectIdentity
tmnxIsisNotifications = _TmnxIsisNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0)
)
tmnxIsisEntry.registerAugmentions(
    ("TIMETRA-ISIS-NG-MIB",
     "tmnxIsisExtEntry")
)
tmnxIsisExtEntry.setIndexNames(*tmnxIsisEntry.getIndexNames())

# Managed Objects groups

tmnxIsisGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 88, 2, 1)
)
tmnxIsisGroup.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisLastEnabledTime"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisAuthKey"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisAuthType"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisAuthCheck"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisExportPolicy1"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisExportPolicy2"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisExportPolicy3"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisExportPolicy4"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisExportPolicy5"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLspLifetime"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisOverloadTimeout"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisOperState"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisReferenceBw"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisTrafficEng"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisShortCuts"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSpfHoldTime"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLastSpfRun"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisGracefulRestart"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisOverloadOnBoot"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisOverloadOnBootTimeout"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSpfWait"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSpfInitialWait"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSpfSecondWait"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLspMaxWait"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLspInitialWait"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLspSecondWait"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisCsnpAuthentication"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisHelloAuthentication"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisPsnpAuthentication"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisGRHelperMode"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisEnableIPv4"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisUnicastImport"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisMulticastImport"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStrictAdjacencyCheck"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisManualSpfTrigger"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisMultiTopology"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisMultiTopoIPv6Ucast"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIPv6RoutingTopo"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSysOrigL1LSPBuffSize"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSysOrigL2LSPBuffSize"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLdpSyncAdminState"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIPv6UnicastImport"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIPv6MulticastImport"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisAdvertisePassiveOnly"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisDefaultRouteTag"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSuppressDefault"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLdpOverRsvp"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisExportLimit"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisExportLimitLogPercent"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisTotalL1ExportedRoutes"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisTotalL2ExportedRoutes"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRsvpShortcut"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisAdvertiseTunnelLink"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIidTlv"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisL1MacAddress"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisL2MacAddress"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSysOperL1LSPBuffSize"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSysOperL2LSPBuffSize"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLoopfreeAlternate"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIPv4McastRoutingTopo"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIPv6McastRoutingTopo"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisMultiTopoIPv4Mcast"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisMultiTopoIPv6Mcast"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisOverloadMaxMetric"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisOverloadOnBootMaxMetric"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRouterId"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisAdvRtrCapability"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisHelloPadding"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLspRefreshInterval"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIgnoreLspErrors"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLevelAuthKey"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLevelAuthType"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLevelExtPreference"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLevelPreference"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLevelWideMetricsOnly"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLevelOverloadStatus"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLevelOverloadTimeLeft"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLevelNumLSPs"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLevelCsnpAuthentication"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLevelHelloAuthentication"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLevelPsnpAuthentication"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLevelDefMetric"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLevelIPv6DefMetric"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLevelLoopfreeAltExclude"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLevelSpbBridgePriority"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLevelSpbForwardTreeTopo"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLevelDefIPv4McastMetric"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLevelDefIPv6McastMetric"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLevelAdvRtrCapability"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLevelAuthKeyChain"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsSpfRuns"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsLSPRegenerations"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsInitiatedPurges"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsLSPRecd"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsLSPDrop"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsLSPSent"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsLSPRetrans"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsIIHRecd"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsIIHDrop"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsIIHSent"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsIIHRetrans"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsCSNPRecd"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsCSNPDrop"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsCSNPSent"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsCSNPRetrans"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsPSNPRecd"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsPSNPDrop"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsPSNPSent"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsPSNPRetrans"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsUnknownRecd"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsUnknownDrop"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsUnknownSent"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsUnknownRetrans"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsCSPFRequests"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsCSPFDroppedRequests"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsCSPFPathsFound"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsCSPFPathsNotFound"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsLfaRuns"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisHostName"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteLevel"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteSpfRunNumber"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteMetric"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteType"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteNHopSysID"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteTag"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteBkupFlags"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteBkupNextHopTy"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteBkupNextHopType"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteBkupNextHop"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteBkupMetric"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteNextHopType"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteNextHopOwner"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteNHOwnerAuxInfo"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteBkupNHType"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteBkupNHOwner"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteBkupNHOwnAxInfo"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisPathMetric"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisPathSNPA"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisPathLfaIfIndex"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisPathLfaNHop"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisPathLfaMetric"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisPathLfaType"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisPathRouteType"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLSPSeq"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLSPChecksum"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLSPLifetimeRemain"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLSPVersion"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLSPPktType"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLSPPktVersion"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLSPMaxArea"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLSPSysIdLen"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLSPAttributes"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLSPUsedLen"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLSPAllocLen"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLSPBuff"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLSPZeroRLT"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSpfLogRunTime"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSpfLogL1Nodes"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSpfLogL2Nodes"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSpfLogEventCount"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSpfLogLastTriggerLSPId"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSpfLogTriggerReason"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSpfLogType"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSummRowStatus"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSummLevel"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSummRouteTag"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLfaNodesCovered"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLfaTotalNodes"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLfaNodeCoverage"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLfaIPv4NodesCovered"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLfaIPv4TotalNodes"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLfaIPv4Coverage"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLfaIPv6NodesCovered"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLfaIPv6TotalNodes"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLfaIPv6Coverage"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisOperRouterId"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisAuthKeyChain"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsPartSpfRuns"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsPartSpfTimeStamp"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsPartLfaRuns"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsPartLfaTimeStamp"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsLfaTimeStamp"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsSpfTimeStamp"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifTrapLSPID"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifSystemLevel"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifPDUFragment"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifFieldLen"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifMaxAreaAddress"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifProtocolVersion"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifLSPSize"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifOriginatingBuffSize"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifProtocolsSupported"))
)
if mibBuilder.loadTexts:
    tmnxIsisGroup.setStatus("current")

tmnxIsisIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 88, 2, 2)
)
tmnxIsisIfGroup.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfRowStatus"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfLastChanged"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfAdminState"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfOperState"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfCsnpInterval"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfHelloAuthKey"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfHelloAuthType"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfLspPacingInterval"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfCircIndex"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfRetransmitInterval"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfTypeDefault"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfEnableBfd"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfIPv6Unicast"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfTeMetric"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfTeState"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfAdminGroup"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfLdpSyncState"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfLdpSyncMaxMetric"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfLdpSyncTimerState"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfLdpSyncTimeLeft"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfRouteTag"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfIPv6EnableBfd"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfHelloAuth"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfLoopfreeAltExclude"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfOperType"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfIPv4Mcast"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfIPv6Mcast"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfBerState"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfIPv4IncludeBfdTlv"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfIPv6IncludeBfdTlv"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfHelloAuthKeyChain"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfLevelLastChangeTime"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfLevelHelloAuthKey"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfLevelHelloAuthType"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfLevelPassive"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfLevelNumAdjacencies"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfLevelISPriority"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfLevelHelloTimer"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfLevelAdminMetric"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfLevelOperMetric"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfLvlIPv6UcastAdmMet"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfLvlIPv6UcastOperMet"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfLvlIPv4McastAdmMetric"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfLvlIPv6McastAdmMetric"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfLevelLinkGroupName"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfLevelSdOffset"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfLevelSfOffset"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfLvlIPv4McastOperMetric"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfLvlIPv6McastOperMetric"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfLevelHelloAuthKeyChain"))
)
if mibBuilder.loadTexts:
    tmnxIsisIfGroup.setStatus("current")

tmnxIsisAdjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 88, 2, 3)
)
tmnxIsisAdjGroup.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisISAdjExpiresIn"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisISAdjCircLevel"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisISAdjNeighborIP"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisISAdjRestartSupport"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisISAdjRestartStatus"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisISAdjRestartSupressed"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisISAdjNumRestarts"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisISAdjLastRestartTime"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisISAdjNeighborIPv6Type"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisISAdjNeighborIPv6"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisISAdjMtEnabled"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisISAdjMtId0"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisISAdjMtId2"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisISAdjMtId3"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisISAdjMtId4"))
)
if mibBuilder.loadTexts:
    tmnxIsisAdjGroup.setStatus("current")

tmnxIsisLFAV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 88, 2, 4)
)
tmnxIsisLFAV12v0Group.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisExLastChanged"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLFAExcludePolicy1"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLFAExcludePolicy2"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLFAExcludePolicy3"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLFAExcludePolicy4"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLFAExcludePolicy5"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfRouteNHTemplate"))
)
if mibBuilder.loadTexts:
    tmnxIsisLFAV12v0Group.setStatus("current")

tmnxIsisNotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 88, 2, 100)
)
tmnxIsisNotifyObjsGroup.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifNbrSysId"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisFailureReasonCode"))
)
if mibBuilder.loadTexts:
    tmnxIsisNotifyObjsGroup.setStatus("current")


# Notification objects

tmnxIsisDatabaseOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0, 1)
)
tmnxIsisDatabaseOverload.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifSystemLevel"),
        ("ISIS-MIB", "isisSysL1State"),
        ("ISIS-MIB", "isisSysL2State"))
)
if mibBuilder.loadTexts:
    tmnxIsisDatabaseOverload.setStatus(
        "current"
    )

tmnxIsisManualAddressDrops = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0, 2)
)
tmnxIsisManualAddressDrops.setObjects(
    ("ISIS-MIB", "isisManAreaAddrExistState")
)
if mibBuilder.loadTexts:
    tmnxIsisManualAddressDrops.setStatus(
        "current"
    )

tmnxIsisCorruptedLSPDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0, 3)
)
tmnxIsisCorruptedLSPDetected.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifSystemLevel"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifTrapLSPID"))
)
if mibBuilder.loadTexts:
    tmnxIsisCorruptedLSPDetected.setStatus(
        "current"
    )

tmnxIsisMaxSeqExceedAttempt = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0, 4)
)
tmnxIsisMaxSeqExceedAttempt.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifSystemLevel"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifTrapLSPID"))
)
if mibBuilder.loadTexts:
    tmnxIsisMaxSeqExceedAttempt.setStatus(
        "current"
    )

tmnxIsisIDLenMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0, 5)
)
tmnxIsisIDLenMismatch.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifFieldLen"),
        ("TIMETRA-VRTR-MIB", "vRtrIfIndex"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifPDUFragment"))
)
if mibBuilder.loadTexts:
    tmnxIsisIDLenMismatch.setStatus(
        "current"
    )

tmnxIsisMaxAreaAddrsMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0, 6)
)
tmnxIsisMaxAreaAddrsMismatch.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifMaxAreaAddress"),
        ("TIMETRA-VRTR-MIB", "vRtrIfIndex"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifPDUFragment"))
)
if mibBuilder.loadTexts:
    tmnxIsisMaxAreaAddrsMismatch.setStatus(
        "current"
    )

tmnxIsisOwnLSPPurge = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0, 7)
)
tmnxIsisOwnLSPPurge.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrIfIndex"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifTrapLSPID"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifSystemLevel"))
)
if mibBuilder.loadTexts:
    tmnxIsisOwnLSPPurge.setStatus(
        "current"
    )

tmnxIsisSequenceNumberSkip = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0, 8)
)
tmnxIsisSequenceNumberSkip.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifTrapLSPID"),
        ("TIMETRA-VRTR-MIB", "vRtrIfIndex"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifSystemLevel"))
)
if mibBuilder.loadTexts:
    tmnxIsisSequenceNumberSkip.setStatus(
        "current"
    )

tmnxIsisAutTypeFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0, 9)
)
tmnxIsisAutTypeFail.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifSystemLevel"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifPDUFragment"),
        ("TIMETRA-VRTR-MIB", "vRtrIfIndex"))
)
if mibBuilder.loadTexts:
    tmnxIsisAutTypeFail.setStatus(
        "current"
    )

tmnxIsisAuthFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0, 10)
)
tmnxIsisAuthFail.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifSystemLevel"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifPDUFragment"),
        ("TIMETRA-VRTR-MIB", "vRtrIfIndex"))
)
if mibBuilder.loadTexts:
    tmnxIsisAuthFail.setStatus(
        "current"
    )

tmnxIsisVersionSkew = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0, 11)
)
tmnxIsisVersionSkew.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifProtocolVersion"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifSystemLevel"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifPDUFragment"),
        ("TIMETRA-VRTR-MIB", "vRtrIfIndex"))
)
if mibBuilder.loadTexts:
    tmnxIsisVersionSkew.setStatus(
        "current"
    )

tmnxIsisAreaMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0, 12)
)
tmnxIsisAreaMismatch.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifLSPSize"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifSystemLevel"),
        ("TIMETRA-VRTR-MIB", "vRtrIfIndex"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifPDUFragment"))
)
if mibBuilder.loadTexts:
    tmnxIsisAreaMismatch.setStatus(
        "current"
    )

tmnxIsisRejectedAdjacency = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0, 13)
)
tmnxIsisRejectedAdjacency.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifSystemLevel"),
        ("TIMETRA-VRTR-MIB", "vRtrIfIndex"))
)
if mibBuilder.loadTexts:
    tmnxIsisRejectedAdjacency.setStatus(
        "current"
    )

tmnxIsisLSPTooLargeToPropagate = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0, 14)
)
tmnxIsisLSPTooLargeToPropagate.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifLSPSize"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifSystemLevel"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifTrapLSPID"),
        ("TIMETRA-VRTR-MIB", "vRtrIfIndex"))
)
if mibBuilder.loadTexts:
    tmnxIsisLSPTooLargeToPropagate.setStatus(
        "current"
    )

tmnxIsisOrigLSPBufSizeMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0, 15)
)
tmnxIsisOrigLSPBufSizeMismatch.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifOriginatingBuffSize"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifSystemLevel"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifTrapLSPID"),
        ("TIMETRA-VRTR-MIB", "vRtrIfIndex"))
)
if mibBuilder.loadTexts:
    tmnxIsisOrigLSPBufSizeMismatch.setStatus(
        "current"
    )

tmnxIsisProtoSuppMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0, 16)
)
tmnxIsisProtoSuppMismatch.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifProtocolsSupported"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifSystemLevel"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifTrapLSPID"),
        ("TIMETRA-VRTR-MIB", "vRtrIfIndex"))
)
if mibBuilder.loadTexts:
    tmnxIsisProtoSuppMismatch.setStatus(
        "current"
    )

tmnxIsisAdjacencyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0, 17)
)
tmnxIsisAdjacencyChange.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifSystemLevel"),
        ("TIMETRA-VRTR-MIB", "vRtrIfIndex"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifTrapLSPID"),
        ("ISIS-MIB", "isisISAdjState"))
)
if mibBuilder.loadTexts:
    tmnxIsisAdjacencyChange.setStatus(
        "current"
    )

tmnxIsisCircIdExhausted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0, 18)
)
tmnxIsisCircIdExhausted.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrIfIndex"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifSystemLevel"))
)
if mibBuilder.loadTexts:
    tmnxIsisCircIdExhausted.setStatus(
        "current"
    )

tmnxIsisAdjRestartStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0, 19)
)
tmnxIsisAdjRestartStatusChange.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifSystemLevel"),
        ("TIMETRA-VRTR-MIB", "vRtrIfIndex"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisISAdjRestartStatus"))
)
if mibBuilder.loadTexts:
    tmnxIsisAdjRestartStatusChange.setStatus(
        "current"
    )

tmnxIsisLdpSyncTimerStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0, 20)
)
tmnxIsisLdpSyncTimerStarted.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrIfIndex"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfLdpSyncTimerState"))
)
if mibBuilder.loadTexts:
    tmnxIsisLdpSyncTimerStarted.setStatus(
        "current"
    )

tmnxIsisLdpSyncExit = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0, 21)
)
tmnxIsisLdpSyncExit.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrIfIndex"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfLdpSyncTimerState"))
)
if mibBuilder.loadTexts:
    tmnxIsisLdpSyncExit.setStatus(
        "current"
    )

tmnxIsisExportLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0, 22)
)
tmnxIsisExportLimitReached.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifSystemLevel"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisExportLimit"))
)
if mibBuilder.loadTexts:
    tmnxIsisExportLimitReached.setStatus(
        "current"
    )

tmnxIsisExportLimitWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0, 23)
)
tmnxIsisExportLimitWarning.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifSystemLevel"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisExportLimit"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisExportLimitLogPercent"))
)
if mibBuilder.loadTexts:
    tmnxIsisExportLimitWarning.setStatus(
        "current"
    )

tmnxIsisRoutesExpLmtDropped = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0, 24)
)
tmnxIsisRoutesExpLmtDropped.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifSystemLevel"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisExportLimit"))
)
if mibBuilder.loadTexts:
    tmnxIsisRoutesExpLmtDropped.setStatus(
        "current"
    )

tmnxIsisFailureDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0, 28)
)
tmnxIsisFailureDisabled.setObjects(
    ("TIMETRA-ISIS-NG-MIB", "tmnxIsisFailureReasonCode")
)
if mibBuilder.loadTexts:
    tmnxIsisFailureDisabled.setStatus(
        "current"
    )


# Notifications groups

tmnxIsisNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 88, 2, 101)
)
tmnxIsisNotifyGroup.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisDatabaseOverload"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisManualAddressDrops"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisCorruptedLSPDetected"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisMaxSeqExceedAttempt"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIDLenMismatch"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisMaxAreaAddrsMismatch"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisOwnLSPPurge"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSequenceNumberSkip"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisAutTypeFail"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisAuthFail"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisVersionSkew"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisAreaMismatch"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRejectedAdjacency"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLSPTooLargeToPropagate"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisOrigLSPBufSizeMismatch"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisProtoSuppMismatch"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisAdjacencyChange"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisCircIdExhausted"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisAdjRestartStatusChange"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLdpSyncTimerStarted"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLdpSyncExit"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisExportLimitReached"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisExportLimitWarning"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRoutesExpLmtDropped"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisFailureDisabled"))
)
if mibBuilder.loadTexts:
    tmnxIsisNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxIsisCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 88, 1, 1)
)
tmnxIsisCompliance.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisGroup"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfGroup"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisAdjGroup"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLFAV12v0Group"))
)
if mibBuilder.loadTexts:
    tmnxIsisCompliance.setStatus(
        "current"
    )

tmnxIsisNotifyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 88, 1, 2)
)
tmnxIsisNotifyCompliance.setObjects(
    ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifyGroup")
)
if mibBuilder.loadTexts:
    tmnxIsisNotifyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-ISIS-NG-MIB",
    **{"TmnxIsisLSPBuffSize": TmnxIsisLSPBuffSize,
       "TmnxIsisRoutingTopology": TmnxIsisRoutingTopology,
       "timetraIsisNgMIBModule": timetraIsisNgMIBModule,
       "tmnxIsisConformance": tmnxIsisConformance,
       "tmnxIsisCompliances": tmnxIsisCompliances,
       "tmnxIsisCompliance": tmnxIsisCompliance,
       "tmnxIsisNotifyCompliance": tmnxIsisNotifyCompliance,
       "tmnxIsisGroups": tmnxIsisGroups,
       "tmnxIsisGroup": tmnxIsisGroup,
       "tmnxIsisIfGroup": tmnxIsisIfGroup,
       "tmnxIsisAdjGroup": tmnxIsisAdjGroup,
       "tmnxIsisLFAV12v0Group": tmnxIsisLFAV12v0Group,
       "tmnxIsisNotifyObjsGroup": tmnxIsisNotifyObjsGroup,
       "tmnxIsisNotifyGroup": tmnxIsisNotifyGroup,
       "tmnxIsisObjs": tmnxIsisObjs,
       "tmnxIsisSystemObjs": tmnxIsisSystemObjs,
       "tmnxIsisTable": tmnxIsisTable,
       "tmnxIsisEntry": tmnxIsisEntry,
       "tmnxIsisLastEnabledTime": tmnxIsisLastEnabledTime,
       "tmnxIsisAuthKey": tmnxIsisAuthKey,
       "tmnxIsisAuthType": tmnxIsisAuthType,
       "tmnxIsisAuthCheck": tmnxIsisAuthCheck,
       "tmnxIsisExportPolicy1": tmnxIsisExportPolicy1,
       "tmnxIsisExportPolicy2": tmnxIsisExportPolicy2,
       "tmnxIsisExportPolicy3": tmnxIsisExportPolicy3,
       "tmnxIsisExportPolicy4": tmnxIsisExportPolicy4,
       "tmnxIsisExportPolicy5": tmnxIsisExportPolicy5,
       "tmnxIsisLspLifetime": tmnxIsisLspLifetime,
       "tmnxIsisOverloadTimeout": tmnxIsisOverloadTimeout,
       "tmnxIsisOperState": tmnxIsisOperState,
       "tmnxIsisReferenceBw": tmnxIsisReferenceBw,
       "tmnxIsisTrafficEng": tmnxIsisTrafficEng,
       "tmnxIsisShortCuts": tmnxIsisShortCuts,
       "tmnxIsisSpfHoldTime": tmnxIsisSpfHoldTime,
       "tmnxIsisLastSpfRun": tmnxIsisLastSpfRun,
       "tmnxIsisGracefulRestart": tmnxIsisGracefulRestart,
       "tmnxIsisOverloadOnBoot": tmnxIsisOverloadOnBoot,
       "tmnxIsisOverloadOnBootTimeout": tmnxIsisOverloadOnBootTimeout,
       "tmnxIsisSpfWait": tmnxIsisSpfWait,
       "tmnxIsisSpfInitialWait": tmnxIsisSpfInitialWait,
       "tmnxIsisSpfSecondWait": tmnxIsisSpfSecondWait,
       "tmnxIsisLspMaxWait": tmnxIsisLspMaxWait,
       "tmnxIsisLspInitialWait": tmnxIsisLspInitialWait,
       "tmnxIsisLspSecondWait": tmnxIsisLspSecondWait,
       "tmnxIsisCsnpAuthentication": tmnxIsisCsnpAuthentication,
       "tmnxIsisHelloAuthentication": tmnxIsisHelloAuthentication,
       "tmnxIsisPsnpAuthentication": tmnxIsisPsnpAuthentication,
       "tmnxIsisGRHelperMode": tmnxIsisGRHelperMode,
       "tmnxIsisEnableIPv4": tmnxIsisEnableIPv4,
       "tmnxIsisUnicastImport": tmnxIsisUnicastImport,
       "tmnxIsisMulticastImport": tmnxIsisMulticastImport,
       "tmnxIsisStrictAdjacencyCheck": tmnxIsisStrictAdjacencyCheck,
       "tmnxIsisManualSpfTrigger": tmnxIsisManualSpfTrigger,
       "tmnxIsisMultiTopology": tmnxIsisMultiTopology,
       "tmnxIsisMultiTopoIPv6Ucast": tmnxIsisMultiTopoIPv6Ucast,
       "tmnxIsisIPv6RoutingTopo": tmnxIsisIPv6RoutingTopo,
       "tmnxIsisSysOrigL1LSPBuffSize": tmnxIsisSysOrigL1LSPBuffSize,
       "tmnxIsisSysOrigL2LSPBuffSize": tmnxIsisSysOrigL2LSPBuffSize,
       "tmnxIsisLdpSyncAdminState": tmnxIsisLdpSyncAdminState,
       "tmnxIsisIPv6UnicastImport": tmnxIsisIPv6UnicastImport,
       "tmnxIsisIPv6MulticastImport": tmnxIsisIPv6MulticastImport,
       "tmnxIsisAdvertisePassiveOnly": tmnxIsisAdvertisePassiveOnly,
       "tmnxIsisDefaultRouteTag": tmnxIsisDefaultRouteTag,
       "tmnxIsisSuppressDefault": tmnxIsisSuppressDefault,
       "tmnxIsisLdpOverRsvp": tmnxIsisLdpOverRsvp,
       "tmnxIsisExportLimit": tmnxIsisExportLimit,
       "tmnxIsisExportLimitLogPercent": tmnxIsisExportLimitLogPercent,
       "tmnxIsisTotalL1ExportedRoutes": tmnxIsisTotalL1ExportedRoutes,
       "tmnxIsisTotalL2ExportedRoutes": tmnxIsisTotalL2ExportedRoutes,
       "tmnxIsisRsvpShortcut": tmnxIsisRsvpShortcut,
       "tmnxIsisAdvertiseTunnelLink": tmnxIsisAdvertiseTunnelLink,
       "tmnxIsisIidTlv": tmnxIsisIidTlv,
       "tmnxIsisL1MacAddress": tmnxIsisL1MacAddress,
       "tmnxIsisL2MacAddress": tmnxIsisL2MacAddress,
       "tmnxIsisSysOperL1LSPBuffSize": tmnxIsisSysOperL1LSPBuffSize,
       "tmnxIsisSysOperL2LSPBuffSize": tmnxIsisSysOperL2LSPBuffSize,
       "tmnxIsisLoopfreeAlternate": tmnxIsisLoopfreeAlternate,
       "tmnxIsisIPv4McastRoutingTopo": tmnxIsisIPv4McastRoutingTopo,
       "tmnxIsisIPv6McastRoutingTopo": tmnxIsisIPv6McastRoutingTopo,
       "tmnxIsisMultiTopoIPv4Mcast": tmnxIsisMultiTopoIPv4Mcast,
       "tmnxIsisMultiTopoIPv6Mcast": tmnxIsisMultiTopoIPv6Mcast,
       "tmnxIsisOverloadMaxMetric": tmnxIsisOverloadMaxMetric,
       "tmnxIsisOverloadOnBootMaxMetric": tmnxIsisOverloadOnBootMaxMetric,
       "tmnxIsisRouterId": tmnxIsisRouterId,
       "tmnxIsisAdvRtrCapability": tmnxIsisAdvRtrCapability,
       "tmnxIsisHelloPadding": tmnxIsisHelloPadding,
       "tmnxIsisLspRefreshInterval": tmnxIsisLspRefreshInterval,
       "tmnxIsisOperRouterId": tmnxIsisOperRouterId,
       "tmnxIsisAuthKeyChain": tmnxIsisAuthKeyChain,
       "tmnxIsisIgnoreLspErrors": tmnxIsisIgnoreLspErrors,
       "tmnxIsisLevelTable": tmnxIsisLevelTable,
       "tmnxIsisLevelEntry": tmnxIsisLevelEntry,
       "tmnxIsisLevel": tmnxIsisLevel,
       "tmnxIsisLevelAuthKey": tmnxIsisLevelAuthKey,
       "tmnxIsisLevelAuthType": tmnxIsisLevelAuthType,
       "tmnxIsisLevelExtPreference": tmnxIsisLevelExtPreference,
       "tmnxIsisLevelPreference": tmnxIsisLevelPreference,
       "tmnxIsisLevelWideMetricsOnly": tmnxIsisLevelWideMetricsOnly,
       "tmnxIsisLevelOverloadStatus": tmnxIsisLevelOverloadStatus,
       "tmnxIsisLevelOverloadTimeLeft": tmnxIsisLevelOverloadTimeLeft,
       "tmnxIsisLevelNumLSPs": tmnxIsisLevelNumLSPs,
       "tmnxIsisLevelCsnpAuthentication": tmnxIsisLevelCsnpAuthentication,
       "tmnxIsisLevelHelloAuthentication": tmnxIsisLevelHelloAuthentication,
       "tmnxIsisLevelPsnpAuthentication": tmnxIsisLevelPsnpAuthentication,
       "tmnxIsisLevelDefMetric": tmnxIsisLevelDefMetric,
       "tmnxIsisLevelIPv6DefMetric": tmnxIsisLevelIPv6DefMetric,
       "tmnxIsisLevelLoopfreeAltExclude": tmnxIsisLevelLoopfreeAltExclude,
       "tmnxIsisLevelSpbBridgePriority": tmnxIsisLevelSpbBridgePriority,
       "tmnxIsisLevelSpbForwardTreeTopo": tmnxIsisLevelSpbForwardTreeTopo,
       "tmnxIsisLevelDefIPv4McastMetric": tmnxIsisLevelDefIPv4McastMetric,
       "tmnxIsisLevelDefIPv6McastMetric": tmnxIsisLevelDefIPv6McastMetric,
       "tmnxIsisLevelAdvRtrCapability": tmnxIsisLevelAdvRtrCapability,
       "tmnxIsisLevelAuthKeyChain": tmnxIsisLevelAuthKeyChain,
       "tmnxIsisStatsTable": tmnxIsisStatsTable,
       "tmnxIsisStatsEntry": tmnxIsisStatsEntry,
       "tmnxIsisStatsSpfRuns": tmnxIsisStatsSpfRuns,
       "tmnxIsisStatsLSPRegenerations": tmnxIsisStatsLSPRegenerations,
       "tmnxIsisStatsInitiatedPurges": tmnxIsisStatsInitiatedPurges,
       "tmnxIsisStatsLSPRecd": tmnxIsisStatsLSPRecd,
       "tmnxIsisStatsLSPDrop": tmnxIsisStatsLSPDrop,
       "tmnxIsisStatsLSPSent": tmnxIsisStatsLSPSent,
       "tmnxIsisStatsLSPRetrans": tmnxIsisStatsLSPRetrans,
       "tmnxIsisStatsIIHRecd": tmnxIsisStatsIIHRecd,
       "tmnxIsisStatsIIHDrop": tmnxIsisStatsIIHDrop,
       "tmnxIsisStatsIIHSent": tmnxIsisStatsIIHSent,
       "tmnxIsisStatsIIHRetrans": tmnxIsisStatsIIHRetrans,
       "tmnxIsisStatsCSNPRecd": tmnxIsisStatsCSNPRecd,
       "tmnxIsisStatsCSNPDrop": tmnxIsisStatsCSNPDrop,
       "tmnxIsisStatsCSNPSent": tmnxIsisStatsCSNPSent,
       "tmnxIsisStatsCSNPRetrans": tmnxIsisStatsCSNPRetrans,
       "tmnxIsisStatsPSNPRecd": tmnxIsisStatsPSNPRecd,
       "tmnxIsisStatsPSNPDrop": tmnxIsisStatsPSNPDrop,
       "tmnxIsisStatsPSNPSent": tmnxIsisStatsPSNPSent,
       "tmnxIsisStatsPSNPRetrans": tmnxIsisStatsPSNPRetrans,
       "tmnxIsisStatsUnknownRecd": tmnxIsisStatsUnknownRecd,
       "tmnxIsisStatsUnknownDrop": tmnxIsisStatsUnknownDrop,
       "tmnxIsisStatsUnknownSent": tmnxIsisStatsUnknownSent,
       "tmnxIsisStatsUnknownRetrans": tmnxIsisStatsUnknownRetrans,
       "tmnxIsisStatsCSPFRequests": tmnxIsisStatsCSPFRequests,
       "tmnxIsisStatsCSPFDroppedRequests": tmnxIsisStatsCSPFDroppedRequests,
       "tmnxIsisStatsCSPFPathsFound": tmnxIsisStatsCSPFPathsFound,
       "tmnxIsisStatsCSPFPathsNotFound": tmnxIsisStatsCSPFPathsNotFound,
       "tmnxIsisStatsLfaRuns": tmnxIsisStatsLfaRuns,
       "tmnxIsisStatsPartSpfRuns": tmnxIsisStatsPartSpfRuns,
       "tmnxIsisStatsPartSpfTimeStamp": tmnxIsisStatsPartSpfTimeStamp,
       "tmnxIsisStatsPartLfaRuns": tmnxIsisStatsPartLfaRuns,
       "tmnxIsisStatsPartLfaTimeStamp": tmnxIsisStatsPartLfaTimeStamp,
       "tmnxIsisStatsLfaTimeStamp": tmnxIsisStatsLfaTimeStamp,
       "tmnxIsisStatsSpfTimeStamp": tmnxIsisStatsSpfTimeStamp,
       "tmnxIsisHostTable": tmnxIsisHostTable,
       "tmnxIsisHostEntry": tmnxIsisHostEntry,
       "tmnxIsisHostSysID": tmnxIsisHostSysID,
       "tmnxIsisHostName": tmnxIsisHostName,
       "tmnxIsisRouteTable": tmnxIsisRouteTable,
       "tmnxIsisRouteEntry": tmnxIsisRouteEntry,
       "tmnxIsisRouteMtId": tmnxIsisRouteMtId,
       "tmnxIsisRouteDestType": tmnxIsisRouteDestType,
       "tmnxIsisRouteDest": tmnxIsisRouteDest,
       "tmnxIsisRoutePrefixLength": tmnxIsisRoutePrefixLength,
       "tmnxIsisRouteNexthopIPType": tmnxIsisRouteNexthopIPType,
       "tmnxIsisRouteNexthopIP": tmnxIsisRouteNexthopIP,
       "tmnxIsisRouteLevel": tmnxIsisRouteLevel,
       "tmnxIsisRouteSpfRunNumber": tmnxIsisRouteSpfRunNumber,
       "tmnxIsisRouteMetric": tmnxIsisRouteMetric,
       "tmnxIsisRouteType": tmnxIsisRouteType,
       "tmnxIsisRouteNHopSysID": tmnxIsisRouteNHopSysID,
       "tmnxIsisRouteTag": tmnxIsisRouteTag,
       "tmnxIsisRouteBkupFlags": tmnxIsisRouteBkupFlags,
       "tmnxIsisRouteBkupNextHopTy": tmnxIsisRouteBkupNextHopTy,
       "tmnxIsisRouteBkupNextHopType": tmnxIsisRouteBkupNextHopType,
       "tmnxIsisRouteBkupNextHop": tmnxIsisRouteBkupNextHop,
       "tmnxIsisRouteBkupMetric": tmnxIsisRouteBkupMetric,
       "tmnxIsisRouteNextHopType": tmnxIsisRouteNextHopType,
       "tmnxIsisRouteNextHopOwner": tmnxIsisRouteNextHopOwner,
       "tmnxIsisRouteNHOwnerAuxInfo": tmnxIsisRouteNHOwnerAuxInfo,
       "tmnxIsisRouteBkupNHType": tmnxIsisRouteBkupNHType,
       "tmnxIsisRouteBkupNHOwner": tmnxIsisRouteBkupNHOwner,
       "tmnxIsisRouteBkupNHOwnAxInfo": tmnxIsisRouteBkupNHOwnAxInfo,
       "tmnxIsisPathTable": tmnxIsisPathTable,
       "tmnxIsisPathEntry": tmnxIsisPathEntry,
       "tmnxIsisPathMtID": tmnxIsisPathMtID,
       "tmnxIsisPathID": tmnxIsisPathID,
       "tmnxIsisPathIfIndex": tmnxIsisPathIfIndex,
       "tmnxIsisPathNHopSysID": tmnxIsisPathNHopSysID,
       "tmnxIsisPathMetric": tmnxIsisPathMetric,
       "tmnxIsisPathSNPA": tmnxIsisPathSNPA,
       "tmnxIsisPathLfaIfIndex": tmnxIsisPathLfaIfIndex,
       "tmnxIsisPathLfaNHop": tmnxIsisPathLfaNHop,
       "tmnxIsisPathLfaMetric": tmnxIsisPathLfaMetric,
       "tmnxIsisPathLfaType": tmnxIsisPathLfaType,
       "tmnxIsisPathRouteType": tmnxIsisPathRouteType,
       "tmnxIsisLSPTable": tmnxIsisLSPTable,
       "tmnxIsisLSPEntry": tmnxIsisLSPEntry,
       "tmnxIsisLSPId": tmnxIsisLSPId,
       "tmnxIsisLSPSeq": tmnxIsisLSPSeq,
       "tmnxIsisLSPChecksum": tmnxIsisLSPChecksum,
       "tmnxIsisLSPLifetimeRemain": tmnxIsisLSPLifetimeRemain,
       "tmnxIsisLSPVersion": tmnxIsisLSPVersion,
       "tmnxIsisLSPPktType": tmnxIsisLSPPktType,
       "tmnxIsisLSPPktVersion": tmnxIsisLSPPktVersion,
       "tmnxIsisLSPMaxArea": tmnxIsisLSPMaxArea,
       "tmnxIsisLSPSysIdLen": tmnxIsisLSPSysIdLen,
       "tmnxIsisLSPAttributes": tmnxIsisLSPAttributes,
       "tmnxIsisLSPUsedLen": tmnxIsisLSPUsedLen,
       "tmnxIsisLSPAllocLen": tmnxIsisLSPAllocLen,
       "tmnxIsisLSPBuff": tmnxIsisLSPBuff,
       "tmnxIsisLSPZeroRLT": tmnxIsisLSPZeroRLT,
       "tmnxIsisSpfLogTable": tmnxIsisSpfLogTable,
       "tmnxIsisSpfLogEntry": tmnxIsisSpfLogEntry,
       "tmnxIsisSpfLogTimeStamp": tmnxIsisSpfLogTimeStamp,
       "tmnxIsisSpfLogRunTime": tmnxIsisSpfLogRunTime,
       "tmnxIsisSpfLogL1Nodes": tmnxIsisSpfLogL1Nodes,
       "tmnxIsisSpfLogL2Nodes": tmnxIsisSpfLogL2Nodes,
       "tmnxIsisSpfLogEventCount": tmnxIsisSpfLogEventCount,
       "tmnxIsisSpfLogLastTriggerLSPId": tmnxIsisSpfLogLastTriggerLSPId,
       "tmnxIsisSpfLogTriggerReason": tmnxIsisSpfLogTriggerReason,
       "tmnxIsisSpfLogType": tmnxIsisSpfLogType,
       "tmnxIsisSummaryTable": tmnxIsisSummaryTable,
       "tmnxIsisSummaryEntry": tmnxIsisSummaryEntry,
       "tmnxIsisSummPrefixType": tmnxIsisSummPrefixType,
       "tmnxIsisSummPrefix": tmnxIsisSummPrefix,
       "tmnxIsisSummPrefixLength": tmnxIsisSummPrefixLength,
       "tmnxIsisSummRowStatus": tmnxIsisSummRowStatus,
       "tmnxIsisSummLevel": tmnxIsisSummLevel,
       "tmnxIsisSummRouteTag": tmnxIsisSummRouteTag,
       "tmnxIsisLfaTable": tmnxIsisLfaTable,
       "tmnxIsisLfaEntry": tmnxIsisLfaEntry,
       "tmnxIsisLfaFamilyCoverage": tmnxIsisLfaFamilyCoverage,
       "tmnxIsisLfaNodesCovered": tmnxIsisLfaNodesCovered,
       "tmnxIsisLfaTotalNodes": tmnxIsisLfaTotalNodes,
       "tmnxIsisLfaNodeCoverage": tmnxIsisLfaNodeCoverage,
       "tmnxIsisLfaIPv4NodesCovered": tmnxIsisLfaIPv4NodesCovered,
       "tmnxIsisLfaIPv4TotalNodes": tmnxIsisLfaIPv4TotalNodes,
       "tmnxIsisLfaIPv4Coverage": tmnxIsisLfaIPv4Coverage,
       "tmnxIsisLfaIPv6NodesCovered": tmnxIsisLfaIPv6NodesCovered,
       "tmnxIsisLfaIPv6TotalNodes": tmnxIsisLfaIPv6TotalNodes,
       "tmnxIsisLfaIPv6Coverage": tmnxIsisLfaIPv6Coverage,
       "tmnxIsisExtTable": tmnxIsisExtTable,
       "tmnxIsisExtEntry": tmnxIsisExtEntry,
       "tmnxIsisExLastChanged": tmnxIsisExLastChanged,
       "tmnxIsisLFAExcludePolicy1": tmnxIsisLFAExcludePolicy1,
       "tmnxIsisLFAExcludePolicy2": tmnxIsisLFAExcludePolicy2,
       "tmnxIsisLFAExcludePolicy3": tmnxIsisLFAExcludePolicy3,
       "tmnxIsisLFAExcludePolicy4": tmnxIsisLFAExcludePolicy4,
       "tmnxIsisLFAExcludePolicy5": tmnxIsisLFAExcludePolicy5,
       "tmnxIsisIfObjs": tmnxIsisIfObjs,
       "tmnxIsisIfTable": tmnxIsisIfTable,
       "tmnxIsisIfEntry": tmnxIsisIfEntry,
       "tmnxIsisIfRowStatus": tmnxIsisIfRowStatus,
       "tmnxIsisIfLastChanged": tmnxIsisIfLastChanged,
       "tmnxIsisIfAdminState": tmnxIsisIfAdminState,
       "tmnxIsisIfOperState": tmnxIsisIfOperState,
       "tmnxIsisIfCsnpInterval": tmnxIsisIfCsnpInterval,
       "tmnxIsisIfHelloAuthKey": tmnxIsisIfHelloAuthKey,
       "tmnxIsisIfHelloAuthType": tmnxIsisIfHelloAuthType,
       "tmnxIsisIfLspPacingInterval": tmnxIsisIfLspPacingInterval,
       "tmnxIsisIfCircIndex": tmnxIsisIfCircIndex,
       "tmnxIsisIfRetransmitInterval": tmnxIsisIfRetransmitInterval,
       "tmnxIsisIfTypeDefault": tmnxIsisIfTypeDefault,
       "tmnxIsisIfEnableBfd": tmnxIsisIfEnableBfd,
       "tmnxIsisIfIPv6Unicast": tmnxIsisIfIPv6Unicast,
       "tmnxIsisIfTeMetric": tmnxIsisIfTeMetric,
       "tmnxIsisIfTeState": tmnxIsisIfTeState,
       "tmnxIsisIfAdminGroup": tmnxIsisIfAdminGroup,
       "tmnxIsisIfLdpSyncState": tmnxIsisIfLdpSyncState,
       "tmnxIsisIfLdpSyncMaxMetric": tmnxIsisIfLdpSyncMaxMetric,
       "tmnxIsisIfLdpSyncTimerState": tmnxIsisIfLdpSyncTimerState,
       "tmnxIsisIfLdpSyncTimeLeft": tmnxIsisIfLdpSyncTimeLeft,
       "tmnxIsisIfRouteTag": tmnxIsisIfRouteTag,
       "tmnxIsisIfIPv6EnableBfd": tmnxIsisIfIPv6EnableBfd,
       "tmnxIsisIfHelloAuth": tmnxIsisIfHelloAuth,
       "tmnxIsisIfLoopfreeAltExclude": tmnxIsisIfLoopfreeAltExclude,
       "tmnxIsisIfOperType": tmnxIsisIfOperType,
       "tmnxIsisIfIPv4Mcast": tmnxIsisIfIPv4Mcast,
       "tmnxIsisIfIPv6Mcast": tmnxIsisIfIPv6Mcast,
       "tmnxIsisIfBerState": tmnxIsisIfBerState,
       "tmnxIsisIfIPv4IncludeBfdTlv": tmnxIsisIfIPv4IncludeBfdTlv,
       "tmnxIsisIfIPv6IncludeBfdTlv": tmnxIsisIfIPv6IncludeBfdTlv,
       "tmnxIsisIfHelloAuthKeyChain": tmnxIsisIfHelloAuthKeyChain,
       "tmnxIsisIfRouteNHTemplate": tmnxIsisIfRouteNHTemplate,
       "tmnxIsisIfLevelTable": tmnxIsisIfLevelTable,
       "tmnxIsisIfLevelEntry": tmnxIsisIfLevelEntry,
       "tmnxIsisIfLevel": tmnxIsisIfLevel,
       "tmnxIsisIfLevelLastChangeTime": tmnxIsisIfLevelLastChangeTime,
       "tmnxIsisIfLevelHelloAuthKey": tmnxIsisIfLevelHelloAuthKey,
       "tmnxIsisIfLevelHelloAuthType": tmnxIsisIfLevelHelloAuthType,
       "tmnxIsisIfLevelPassive": tmnxIsisIfLevelPassive,
       "tmnxIsisIfLevelNumAdjacencies": tmnxIsisIfLevelNumAdjacencies,
       "tmnxIsisIfLevelISPriority": tmnxIsisIfLevelISPriority,
       "tmnxIsisIfLevelHelloTimer": tmnxIsisIfLevelHelloTimer,
       "tmnxIsisIfLevelAdminMetric": tmnxIsisIfLevelAdminMetric,
       "tmnxIsisIfLevelOperMetric": tmnxIsisIfLevelOperMetric,
       "tmnxIsisIfLvlIPv6UcastAdmMet": tmnxIsisIfLvlIPv6UcastAdmMet,
       "tmnxIsisIfLvlIPv6UcastOperMet": tmnxIsisIfLvlIPv6UcastOperMet,
       "tmnxIsisIfLvlIPv4McastAdmMetric": tmnxIsisIfLvlIPv4McastAdmMetric,
       "tmnxIsisIfLvlIPv6McastAdmMetric": tmnxIsisIfLvlIPv6McastAdmMetric,
       "tmnxIsisIfLevelLinkGroupName": tmnxIsisIfLevelLinkGroupName,
       "tmnxIsisIfLevelSdOffset": tmnxIsisIfLevelSdOffset,
       "tmnxIsisIfLevelSfOffset": tmnxIsisIfLevelSfOffset,
       "tmnxIsisIfLvlIPv4McastOperMetric": tmnxIsisIfLvlIPv4McastOperMetric,
       "tmnxIsisIfLvlIPv6McastOperMetric": tmnxIsisIfLvlIPv6McastOperMetric,
       "tmnxIsisIfLevelHelloAuthKeyChain": tmnxIsisIfLevelHelloAuthKeyChain,
       "tmnxIsisAdjObjs": tmnxIsisAdjObjs,
       "tmnxIsisISAdjTable": tmnxIsisISAdjTable,
       "tmnxIsisISAdjEntry": tmnxIsisISAdjEntry,
       "tmnxIsisISAdjExpiresIn": tmnxIsisISAdjExpiresIn,
       "tmnxIsisISAdjCircLevel": tmnxIsisISAdjCircLevel,
       "tmnxIsisISAdjNeighborIP": tmnxIsisISAdjNeighborIP,
       "tmnxIsisISAdjRestartSupport": tmnxIsisISAdjRestartSupport,
       "tmnxIsisISAdjRestartStatus": tmnxIsisISAdjRestartStatus,
       "tmnxIsisISAdjRestartSupressed": tmnxIsisISAdjRestartSupressed,
       "tmnxIsisISAdjNumRestarts": tmnxIsisISAdjNumRestarts,
       "tmnxIsisISAdjLastRestartTime": tmnxIsisISAdjLastRestartTime,
       "tmnxIsisISAdjNeighborIPv6Type": tmnxIsisISAdjNeighborIPv6Type,
       "tmnxIsisISAdjNeighborIPv6": tmnxIsisISAdjNeighborIPv6,
       "tmnxIsisISAdjMtEnabled": tmnxIsisISAdjMtEnabled,
       "tmnxIsisISAdjMtId0": tmnxIsisISAdjMtId0,
       "tmnxIsisISAdjMtId2": tmnxIsisISAdjMtId2,
       "tmnxIsisISAdjMtId3": tmnxIsisISAdjMtId3,
       "tmnxIsisISAdjMtId4": tmnxIsisISAdjMtId4,
       "tmnxIsisNotificationObjs": tmnxIsisNotificationObjs,
       "tmnxIsisNotificationTable": tmnxIsisNotificationTable,
       "tmnxIsisNotificationEntry": tmnxIsisNotificationEntry,
       "tmnxIsisNotifTrapLSPID": tmnxIsisNotifTrapLSPID,
       "tmnxIsisNotifSystemLevel": tmnxIsisNotifSystemLevel,
       "tmnxIsisNotifPDUFragment": tmnxIsisNotifPDUFragment,
       "tmnxIsisNotifFieldLen": tmnxIsisNotifFieldLen,
       "tmnxIsisNotifMaxAreaAddress": tmnxIsisNotifMaxAreaAddress,
       "tmnxIsisNotifProtocolVersion": tmnxIsisNotifProtocolVersion,
       "tmnxIsisNotifLSPSize": tmnxIsisNotifLSPSize,
       "tmnxIsisNotifOriginatingBuffSize": tmnxIsisNotifOriginatingBuffSize,
       "tmnxIsisNotifProtocolsSupported": tmnxIsisNotifProtocolsSupported,
       "tmnxIsisNotifNbrSysId": tmnxIsisNotifNbrSysId,
       "tmnxIsisFailureReasonCode": tmnxIsisFailureReasonCode,
       "tmnxIsisNotifyPrefix": tmnxIsisNotifyPrefix,
       "tmnxIsisNotifications": tmnxIsisNotifications,
       "tmnxIsisDatabaseOverload": tmnxIsisDatabaseOverload,
       "tmnxIsisManualAddressDrops": tmnxIsisManualAddressDrops,
       "tmnxIsisCorruptedLSPDetected": tmnxIsisCorruptedLSPDetected,
       "tmnxIsisMaxSeqExceedAttempt": tmnxIsisMaxSeqExceedAttempt,
       "tmnxIsisIDLenMismatch": tmnxIsisIDLenMismatch,
       "tmnxIsisMaxAreaAddrsMismatch": tmnxIsisMaxAreaAddrsMismatch,
       "tmnxIsisOwnLSPPurge": tmnxIsisOwnLSPPurge,
       "tmnxIsisSequenceNumberSkip": tmnxIsisSequenceNumberSkip,
       "tmnxIsisAutTypeFail": tmnxIsisAutTypeFail,
       "tmnxIsisAuthFail": tmnxIsisAuthFail,
       "tmnxIsisVersionSkew": tmnxIsisVersionSkew,
       "tmnxIsisAreaMismatch": tmnxIsisAreaMismatch,
       "tmnxIsisRejectedAdjacency": tmnxIsisRejectedAdjacency,
       "tmnxIsisLSPTooLargeToPropagate": tmnxIsisLSPTooLargeToPropagate,
       "tmnxIsisOrigLSPBufSizeMismatch": tmnxIsisOrigLSPBufSizeMismatch,
       "tmnxIsisProtoSuppMismatch": tmnxIsisProtoSuppMismatch,
       "tmnxIsisAdjacencyChange": tmnxIsisAdjacencyChange,
       "tmnxIsisCircIdExhausted": tmnxIsisCircIdExhausted,
       "tmnxIsisAdjRestartStatusChange": tmnxIsisAdjRestartStatusChange,
       "tmnxIsisLdpSyncTimerStarted": tmnxIsisLdpSyncTimerStarted,
       "tmnxIsisLdpSyncExit": tmnxIsisLdpSyncExit,
       "tmnxIsisExportLimitReached": tmnxIsisExportLimitReached,
       "tmnxIsisExportLimitWarning": tmnxIsisExportLimitWarning,
       "tmnxIsisRoutesExpLmtDropped": tmnxIsisRoutesExpLmtDropped,
       "tmnxIsisFailureDisabled": tmnxIsisFailureDisabled}
)
