# SNMP MIB module (TIMETRA-ISIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-ISIS-MIB.mib
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
 isisISAdjEntry,
 isisISAdjState,
 isisManAreaAddrExistState,
 isisSysInstance,
 isisSysL1State,
 isisSysL2State) = mibBuilder.importSymbols(
    "ISIS-MIB",
    "SNPAAddress",
    "SystemID",
    "isisISAdjEntry",
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

timetraIsisMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 10)
)
if mibBuilder.loadTexts:
    timetraIsisMIBModule.setRevisions(
        ("2014-01-01 00:00",
         "2011-02-01 00:00",
         "2009-02-28 00:00",
         "2008-07-01 00:00",
         "2008-01-01 00:00",
         "2007-01-01 00:00",
         "2006-03-15 00:00",
         "2005-08-31 00:00",
         "2005-01-24 00:00",
         "2004-06-02 00:00",
         "2004-01-15 00:00",
         "2003-08-15 00:00",
         "2003-01-20 00:00",
         "2001-09-21 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxLSPBuffSize(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(490, 9190),
    )



class IsisRoutingTopology(TextualConvention, Integer32):
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

_VRtrIsisMIBConformance_ObjectIdentity = ObjectIdentity
vRtrIsisMIBConformance = _VRtrIsisMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 10)
)
_VRtrIsisMIBConformances_ObjectIdentity = ObjectIdentity
vRtrIsisMIBConformances = _VRtrIsisMIBConformances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 10, 1)
)
_VRtrIsisMIBGroups_ObjectIdentity = ObjectIdentity
vRtrIsisMIBGroups = _VRtrIsisMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 10, 2)
)
_VRtrIsisMIBDCConformances_ObjectIdentity = ObjectIdentity
vRtrIsisMIBDCConformances = _VRtrIsisMIBDCConformances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 10, 3)
)
_VRtrIsisDCMIBGroups_ObjectIdentity = ObjectIdentity
vRtrIsisDCMIBGroups = _VRtrIsisDCMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 10, 4)
)
_VRtrIsisObjs_ObjectIdentity = ObjectIdentity
vRtrIsisObjs = _VRtrIsisObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10)
)
_VRtrIsisSystemObjs_ObjectIdentity = ObjectIdentity
vRtrIsisSystemObjs = _VRtrIsisSystemObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1)
)
_VRtrIsisTable_Object = MibTable
vRtrIsisTable = _VRtrIsisTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1)
)
if mibBuilder.loadTexts:
    vRtrIsisTable.setStatus("deprecated")
_VRtrIsisEntry_Object = MibTableRow
vRtrIsisEntry = _VRtrIsisEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1)
)
vRtrIsisEntry.setIndexNames(
    (0, "ISIS-MIB", "isisSysInstance"),
)
if mibBuilder.loadTexts:
    vRtrIsisEntry.setStatus("deprecated")
_VRtrIsisLastEnabledTime_Type = TimeStamp
_VRtrIsisLastEnabledTime_Object = MibTableColumn
vRtrIsisLastEnabledTime = _VRtrIsisLastEnabledTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 1),
    _VRtrIsisLastEnabledTime_Type()
)
vRtrIsisLastEnabledTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLastEnabledTime.setStatus("deprecated")


class _VRtrIsisAuthKey_Type(OctetString):
    """Custom type vRtrIsisAuthKey based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_VRtrIsisAuthKey_Type.__name__ = "OctetString"
_VRtrIsisAuthKey_Object = MibTableColumn
vRtrIsisAuthKey = _VRtrIsisAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 2),
    _VRtrIsisAuthKey_Type()
)
vRtrIsisAuthKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisAuthKey.setStatus("deprecated")


class _VRtrIsisAuthType_Type(Integer32):
    """Custom type vRtrIsisAuthType based on Integer32"""
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


_VRtrIsisAuthType_Type.__name__ = "Integer32"
_VRtrIsisAuthType_Object = MibTableColumn
vRtrIsisAuthType = _VRtrIsisAuthType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 3),
    _VRtrIsisAuthType_Type()
)
vRtrIsisAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisAuthType.setStatus("deprecated")


class _VRtrIsisAuthCheck_Type(TruthValue):
    """Custom type vRtrIsisAuthCheck based on TruthValue"""
    defaultValue = 1


_VRtrIsisAuthCheck_Type.__name__ = "TruthValue"
_VRtrIsisAuthCheck_Object = MibTableColumn
vRtrIsisAuthCheck = _VRtrIsisAuthCheck_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 4),
    _VRtrIsisAuthCheck_Type()
)
vRtrIsisAuthCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisAuthCheck.setStatus("deprecated")


class _VRtrIsisExportPolicy1_Type(TNamedItemOrEmpty):
    """Custom type vRtrIsisExportPolicy1 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrIsisExportPolicy1_Type.__name__ = "TNamedItemOrEmpty"
_VRtrIsisExportPolicy1_Object = MibTableColumn
vRtrIsisExportPolicy1 = _VRtrIsisExportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 5),
    _VRtrIsisExportPolicy1_Type()
)
vRtrIsisExportPolicy1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisExportPolicy1.setStatus("deprecated")


class _VRtrIsisExportPolicy2_Type(TNamedItemOrEmpty):
    """Custom type vRtrIsisExportPolicy2 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrIsisExportPolicy2_Type.__name__ = "TNamedItemOrEmpty"
_VRtrIsisExportPolicy2_Object = MibTableColumn
vRtrIsisExportPolicy2 = _VRtrIsisExportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 6),
    _VRtrIsisExportPolicy2_Type()
)
vRtrIsisExportPolicy2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisExportPolicy2.setStatus("deprecated")


class _VRtrIsisExportPolicy3_Type(TNamedItemOrEmpty):
    """Custom type vRtrIsisExportPolicy3 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrIsisExportPolicy3_Type.__name__ = "TNamedItemOrEmpty"
_VRtrIsisExportPolicy3_Object = MibTableColumn
vRtrIsisExportPolicy3 = _VRtrIsisExportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 7),
    _VRtrIsisExportPolicy3_Type()
)
vRtrIsisExportPolicy3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisExportPolicy3.setStatus("deprecated")


class _VRtrIsisExportPolicy4_Type(TNamedItemOrEmpty):
    """Custom type vRtrIsisExportPolicy4 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrIsisExportPolicy4_Type.__name__ = "TNamedItemOrEmpty"
_VRtrIsisExportPolicy4_Object = MibTableColumn
vRtrIsisExportPolicy4 = _VRtrIsisExportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 8),
    _VRtrIsisExportPolicy4_Type()
)
vRtrIsisExportPolicy4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisExportPolicy4.setStatus("deprecated")


class _VRtrIsisExportPolicy5_Type(TNamedItemOrEmpty):
    """Custom type vRtrIsisExportPolicy5 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrIsisExportPolicy5_Type.__name__ = "TNamedItemOrEmpty"
_VRtrIsisExportPolicy5_Object = MibTableColumn
vRtrIsisExportPolicy5 = _VRtrIsisExportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 9),
    _VRtrIsisExportPolicy5_Type()
)
vRtrIsisExportPolicy5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisExportPolicy5.setStatus("deprecated")


class _VRtrIsisLspLifetime_Type(Unsigned32):
    """Custom type vRtrIsisLspLifetime based on Unsigned32"""
    defaultValue = 1200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(350, 65535),
    )


_VRtrIsisLspLifetime_Type.__name__ = "Unsigned32"
_VRtrIsisLspLifetime_Object = MibTableColumn
vRtrIsisLspLifetime = _VRtrIsisLspLifetime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 10),
    _VRtrIsisLspLifetime_Type()
)
vRtrIsisLspLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLspLifetime.setStatus("deprecated")
if mibBuilder.loadTexts:
    vRtrIsisLspLifetime.setUnits("seconds")


class _VRtrIsisOverloadTimeout_Type(Unsigned32):
    """Custom type vRtrIsisOverloadTimeout based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 1800),
    )


_VRtrIsisOverloadTimeout_Type.__name__ = "Unsigned32"
_VRtrIsisOverloadTimeout_Object = MibTableColumn
vRtrIsisOverloadTimeout = _VRtrIsisOverloadTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 11),
    _VRtrIsisOverloadTimeout_Type()
)
vRtrIsisOverloadTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisOverloadTimeout.setStatus("deprecated")
if mibBuilder.loadTexts:
    vRtrIsisOverloadTimeout.setUnits("seconds")
_VRtrIsisOperState_Type = TmnxOperState
_VRtrIsisOperState_Object = MibTableColumn
vRtrIsisOperState = _VRtrIsisOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 12),
    _VRtrIsisOperState_Type()
)
vRtrIsisOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisOperState.setStatus("deprecated")


class _VRtrIsisReferenceBw_Type(TmnxReferenceBandwidth):
    """Custom type vRtrIsisReferenceBw based on TmnxReferenceBandwidth"""
    defaultValue = 0


_VRtrIsisReferenceBw_Type.__name__ = "TmnxReferenceBandwidth"
_VRtrIsisReferenceBw_Object = MibTableColumn
vRtrIsisReferenceBw = _VRtrIsisReferenceBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 13),
    _VRtrIsisReferenceBw_Type()
)
vRtrIsisReferenceBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisReferenceBw.setStatus("deprecated")
if mibBuilder.loadTexts:
    vRtrIsisReferenceBw.setUnits("kilobits per second")


class _VRtrIsisTrafficEng_Type(TruthValue):
    """Custom type vRtrIsisTrafficEng based on TruthValue"""
    defaultValue = 1


_VRtrIsisTrafficEng_Type.__name__ = "TruthValue"
_VRtrIsisTrafficEng_Object = MibTableColumn
vRtrIsisTrafficEng = _VRtrIsisTrafficEng_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 14),
    _VRtrIsisTrafficEng_Type()
)
vRtrIsisTrafficEng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisTrafficEng.setStatus("deprecated")


class _VRtrIsisShortCuts_Type(TruthValue):
    """Custom type vRtrIsisShortCuts based on TruthValue"""
    defaultValue = 2


_VRtrIsisShortCuts_Type.__name__ = "TruthValue"
_VRtrIsisShortCuts_Object = MibTableColumn
vRtrIsisShortCuts = _VRtrIsisShortCuts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 15),
    _VRtrIsisShortCuts_Type()
)
vRtrIsisShortCuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisShortCuts.setStatus("deprecated")


class _VRtrIsisSpfHoldTime_Type(Integer32):
    """Custom type vRtrIsisSpfHoldTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VRtrIsisSpfHoldTime_Type.__name__ = "Integer32"
_VRtrIsisSpfHoldTime_Object = MibTableColumn
vRtrIsisSpfHoldTime = _VRtrIsisSpfHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 16),
    _VRtrIsisSpfHoldTime_Type()
)
vRtrIsisSpfHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisSpfHoldTime.setStatus("deprecated")
if mibBuilder.loadTexts:
    vRtrIsisSpfHoldTime.setUnits("seconds")
_VRtrIsisLastSpfRun_Type = TimeStamp
_VRtrIsisLastSpfRun_Object = MibTableColumn
vRtrIsisLastSpfRun = _VRtrIsisLastSpfRun_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 17),
    _VRtrIsisLastSpfRun_Type()
)
vRtrIsisLastSpfRun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLastSpfRun.setStatus("deprecated")


class _VRtrIsisGracefulRestart_Type(TruthValue):
    """Custom type vRtrIsisGracefulRestart based on TruthValue"""
    defaultValue = 2


_VRtrIsisGracefulRestart_Type.__name__ = "TruthValue"
_VRtrIsisGracefulRestart_Object = MibTableColumn
vRtrIsisGracefulRestart = _VRtrIsisGracefulRestart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 18),
    _VRtrIsisGracefulRestart_Type()
)
vRtrIsisGracefulRestart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisGracefulRestart.setStatus("deprecated")


class _VRtrIsisOverloadOnBoot_Type(Integer32):
    """Custom type vRtrIsisOverloadOnBoot based on Integer32"""
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
        *(("disabled", 1),
          ("enabled", 2),
          ("enabledWaitForBgp", 3))
    )


_VRtrIsisOverloadOnBoot_Type.__name__ = "Integer32"
_VRtrIsisOverloadOnBoot_Object = MibTableColumn
vRtrIsisOverloadOnBoot = _VRtrIsisOverloadOnBoot_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 19),
    _VRtrIsisOverloadOnBoot_Type()
)
vRtrIsisOverloadOnBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisOverloadOnBoot.setStatus("deprecated")


class _VRtrIsisOverloadOnBootTimeout_Type(Unsigned32):
    """Custom type vRtrIsisOverloadOnBootTimeout based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 1800),
    )


_VRtrIsisOverloadOnBootTimeout_Type.__name__ = "Unsigned32"
_VRtrIsisOverloadOnBootTimeout_Object = MibTableColumn
vRtrIsisOverloadOnBootTimeout = _VRtrIsisOverloadOnBootTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 20),
    _VRtrIsisOverloadOnBootTimeout_Type()
)
vRtrIsisOverloadOnBootTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisOverloadOnBootTimeout.setStatus("deprecated")
if mibBuilder.loadTexts:
    vRtrIsisOverloadOnBootTimeout.setUnits("seconds")


class _VRtrIsisSpfWait_Type(Unsigned32):
    """Custom type vRtrIsisSpfWait based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_VRtrIsisSpfWait_Type.__name__ = "Unsigned32"
_VRtrIsisSpfWait_Object = MibTableColumn
vRtrIsisSpfWait = _VRtrIsisSpfWait_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 21),
    _VRtrIsisSpfWait_Type()
)
vRtrIsisSpfWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisSpfWait.setStatus("deprecated")
if mibBuilder.loadTexts:
    vRtrIsisSpfWait.setUnits("seconds")


class _VRtrIsisSpfInitialWait_Type(Unsigned32):
    """Custom type vRtrIsisSpfInitialWait based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100000),
    )


_VRtrIsisSpfInitialWait_Type.__name__ = "Unsigned32"
_VRtrIsisSpfInitialWait_Object = MibTableColumn
vRtrIsisSpfInitialWait = _VRtrIsisSpfInitialWait_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 22),
    _VRtrIsisSpfInitialWait_Type()
)
vRtrIsisSpfInitialWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisSpfInitialWait.setStatus("deprecated")
if mibBuilder.loadTexts:
    vRtrIsisSpfInitialWait.setUnits("milliseconds")


class _VRtrIsisSpfSecondWait_Type(Unsigned32):
    """Custom type vRtrIsisSpfSecondWait based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_VRtrIsisSpfSecondWait_Type.__name__ = "Unsigned32"
_VRtrIsisSpfSecondWait_Object = MibTableColumn
vRtrIsisSpfSecondWait = _VRtrIsisSpfSecondWait_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 23),
    _VRtrIsisSpfSecondWait_Type()
)
vRtrIsisSpfSecondWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisSpfSecondWait.setStatus("deprecated")
if mibBuilder.loadTexts:
    vRtrIsisSpfSecondWait.setUnits("milliseconds")


class _VRtrIsisLspMaxWait_Type(Unsigned32):
    """Custom type vRtrIsisLspMaxWait based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_VRtrIsisLspMaxWait_Type.__name__ = "Unsigned32"
_VRtrIsisLspMaxWait_Object = MibTableColumn
vRtrIsisLspMaxWait = _VRtrIsisLspMaxWait_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 24),
    _VRtrIsisLspMaxWait_Type()
)
vRtrIsisLspMaxWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLspMaxWait.setStatus("deprecated")
if mibBuilder.loadTexts:
    vRtrIsisLspMaxWait.setUnits("seconds")


class _VRtrIsisLspInitialWait_Type(Unsigned32):
    """Custom type vRtrIsisLspInitialWait based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VRtrIsisLspInitialWait_Type.__name__ = "Unsigned32"
_VRtrIsisLspInitialWait_Object = MibTableColumn
vRtrIsisLspInitialWait = _VRtrIsisLspInitialWait_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 25),
    _VRtrIsisLspInitialWait_Type()
)
vRtrIsisLspInitialWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLspInitialWait.setStatus("deprecated")
if mibBuilder.loadTexts:
    vRtrIsisLspInitialWait.setUnits("seconds")


class _VRtrIsisLspSecondWait_Type(Unsigned32):
    """Custom type vRtrIsisLspSecondWait based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_VRtrIsisLspSecondWait_Type.__name__ = "Unsigned32"
_VRtrIsisLspSecondWait_Object = MibTableColumn
vRtrIsisLspSecondWait = _VRtrIsisLspSecondWait_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 26),
    _VRtrIsisLspSecondWait_Type()
)
vRtrIsisLspSecondWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLspSecondWait.setStatus("deprecated")
if mibBuilder.loadTexts:
    vRtrIsisLspSecondWait.setUnits("seconds")


class _VRtrIsisCsnpAuthentication_Type(TruthValue):
    """Custom type vRtrIsisCsnpAuthentication based on TruthValue"""
    defaultValue = 1


_VRtrIsisCsnpAuthentication_Type.__name__ = "TruthValue"
_VRtrIsisCsnpAuthentication_Object = MibTableColumn
vRtrIsisCsnpAuthentication = _VRtrIsisCsnpAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 27),
    _VRtrIsisCsnpAuthentication_Type()
)
vRtrIsisCsnpAuthentication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisCsnpAuthentication.setStatus("deprecated")


class _VRtrIsisHelloAuthentication_Type(TruthValue):
    """Custom type vRtrIsisHelloAuthentication based on TruthValue"""
    defaultValue = 1


_VRtrIsisHelloAuthentication_Type.__name__ = "TruthValue"
_VRtrIsisHelloAuthentication_Object = MibTableColumn
vRtrIsisHelloAuthentication = _VRtrIsisHelloAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 28),
    _VRtrIsisHelloAuthentication_Type()
)
vRtrIsisHelloAuthentication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisHelloAuthentication.setStatus("deprecated")


class _VRtrIsisPsnpAuthentication_Type(TruthValue):
    """Custom type vRtrIsisPsnpAuthentication based on TruthValue"""
    defaultValue = 1


_VRtrIsisPsnpAuthentication_Type.__name__ = "TruthValue"
_VRtrIsisPsnpAuthentication_Object = MibTableColumn
vRtrIsisPsnpAuthentication = _VRtrIsisPsnpAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 29),
    _VRtrIsisPsnpAuthentication_Type()
)
vRtrIsisPsnpAuthentication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisPsnpAuthentication.setStatus("deprecated")


class _VRtrIsisGRRestartDuration_Type(Unsigned32):
    """Custom type vRtrIsisGRRestartDuration based on Unsigned32"""
    defaultValue = 180

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_VRtrIsisGRRestartDuration_Type.__name__ = "Unsigned32"
_VRtrIsisGRRestartDuration_Object = MibTableColumn
vRtrIsisGRRestartDuration = _VRtrIsisGRRestartDuration_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 30),
    _VRtrIsisGRRestartDuration_Type()
)
vRtrIsisGRRestartDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisGRRestartDuration.setStatus("deprecated")
if mibBuilder.loadTexts:
    vRtrIsisGRRestartDuration.setUnits("seconds")


class _VRtrIsisGRHelperMode_Type(TruthValue):
    """Custom type vRtrIsisGRHelperMode based on TruthValue"""
    defaultValue = 2


_VRtrIsisGRHelperMode_Type.__name__ = "TruthValue"
_VRtrIsisGRHelperMode_Object = MibTableColumn
vRtrIsisGRHelperMode = _VRtrIsisGRHelperMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 31),
    _VRtrIsisGRHelperMode_Type()
)
vRtrIsisGRHelperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisGRHelperMode.setStatus("deprecated")


class _VRtrIsisEnableIPv6_Type(TruthValue):
    """Custom type vRtrIsisEnableIPv6 based on TruthValue"""
    defaultValue = 2


_VRtrIsisEnableIPv6_Type.__name__ = "TruthValue"
_VRtrIsisEnableIPv6_Object = MibTableColumn
vRtrIsisEnableIPv6 = _VRtrIsisEnableIPv6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 32),
    _VRtrIsisEnableIPv6_Type()
)
vRtrIsisEnableIPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisEnableIPv6.setStatus("obsolete")


class _VRtrIsisEnableIPv4_Type(TruthValue):
    """Custom type vRtrIsisEnableIPv4 based on TruthValue"""
    defaultValue = 1


_VRtrIsisEnableIPv4_Type.__name__ = "TruthValue"
_VRtrIsisEnableIPv4_Object = MibTableColumn
vRtrIsisEnableIPv4 = _VRtrIsisEnableIPv4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 33),
    _VRtrIsisEnableIPv4_Type()
)
vRtrIsisEnableIPv4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisEnableIPv4.setStatus("deprecated")


class _VRtrIsisUnicastImport_Type(TruthValue):
    """Custom type vRtrIsisUnicastImport based on TruthValue"""
    defaultValue = 1


_VRtrIsisUnicastImport_Type.__name__ = "TruthValue"
_VRtrIsisUnicastImport_Object = MibTableColumn
vRtrIsisUnicastImport = _VRtrIsisUnicastImport_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 34),
    _VRtrIsisUnicastImport_Type()
)
vRtrIsisUnicastImport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisUnicastImport.setStatus("deprecated")


class _VRtrIsisMulticastImport_Type(TruthValue):
    """Custom type vRtrIsisMulticastImport based on TruthValue"""
    defaultValue = 2


_VRtrIsisMulticastImport_Type.__name__ = "TruthValue"
_VRtrIsisMulticastImport_Object = MibTableColumn
vRtrIsisMulticastImport = _VRtrIsisMulticastImport_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 35),
    _VRtrIsisMulticastImport_Type()
)
vRtrIsisMulticastImport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisMulticastImport.setStatus("deprecated")


class _VRtrIsisStrictAdjacencyCheck_Type(TruthValue):
    """Custom type vRtrIsisStrictAdjacencyCheck based on TruthValue"""
    defaultValue = 2


_VRtrIsisStrictAdjacencyCheck_Type.__name__ = "TruthValue"
_VRtrIsisStrictAdjacencyCheck_Object = MibTableColumn
vRtrIsisStrictAdjacencyCheck = _VRtrIsisStrictAdjacencyCheck_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 36),
    _VRtrIsisStrictAdjacencyCheck_Type()
)
vRtrIsisStrictAdjacencyCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisStrictAdjacencyCheck.setStatus("deprecated")


class _VRtrIsisManualSpfTrigger_Type(Integer32):
    """Custom type vRtrIsisManualSpfTrigger based on Integer32"""
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


_VRtrIsisManualSpfTrigger_Type.__name__ = "Integer32"
_VRtrIsisManualSpfTrigger_Object = MibTableColumn
vRtrIsisManualSpfTrigger = _VRtrIsisManualSpfTrigger_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 37),
    _VRtrIsisManualSpfTrigger_Type()
)
vRtrIsisManualSpfTrigger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisManualSpfTrigger.setStatus("deprecated")


class _VRtrIsisMultiTopology_Type(TruthValue):
    """Custom type vRtrIsisMultiTopology based on TruthValue"""
    defaultValue = 2


_VRtrIsisMultiTopology_Type.__name__ = "TruthValue"
_VRtrIsisMultiTopology_Object = MibTableColumn
vRtrIsisMultiTopology = _VRtrIsisMultiTopology_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 38),
    _VRtrIsisMultiTopology_Type()
)
vRtrIsisMultiTopology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisMultiTopology.setStatus("deprecated")


class _VRtrIsisMultiTopoIPv6Ucast_Type(TruthValue):
    """Custom type vRtrIsisMultiTopoIPv6Ucast based on TruthValue"""
    defaultValue = 2


_VRtrIsisMultiTopoIPv6Ucast_Type.__name__ = "TruthValue"
_VRtrIsisMultiTopoIPv6Ucast_Object = MibTableColumn
vRtrIsisMultiTopoIPv6Ucast = _VRtrIsisMultiTopoIPv6Ucast_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 39),
    _VRtrIsisMultiTopoIPv6Ucast_Type()
)
vRtrIsisMultiTopoIPv6Ucast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisMultiTopoIPv6Ucast.setStatus("deprecated")


class _VRtrIsisIPv6RoutingTopo_Type(Integer32):
    """Custom type vRtrIsisIPv6RoutingTopo based on Integer32"""
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


_VRtrIsisIPv6RoutingTopo_Type.__name__ = "Integer32"
_VRtrIsisIPv6RoutingTopo_Object = MibTableColumn
vRtrIsisIPv6RoutingTopo = _VRtrIsisIPv6RoutingTopo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 40),
    _VRtrIsisIPv6RoutingTopo_Type()
)
vRtrIsisIPv6RoutingTopo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIPv6RoutingTopo.setStatus("deprecated")


class _VRtrIsisSysOrigL1LSPBuffSize_Type(TmnxLSPBuffSize):
    """Custom type vRtrIsisSysOrigL1LSPBuffSize based on TmnxLSPBuffSize"""
    defaultValue = 1492


_VRtrIsisSysOrigL1LSPBuffSize_Type.__name__ = "TmnxLSPBuffSize"
_VRtrIsisSysOrigL1LSPBuffSize_Object = MibTableColumn
vRtrIsisSysOrigL1LSPBuffSize = _VRtrIsisSysOrigL1LSPBuffSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 41),
    _VRtrIsisSysOrigL1LSPBuffSize_Type()
)
vRtrIsisSysOrigL1LSPBuffSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisSysOrigL1LSPBuffSize.setStatus("deprecated")


class _VRtrIsisSysOrigL2LSPBuffSize_Type(TmnxLSPBuffSize):
    """Custom type vRtrIsisSysOrigL2LSPBuffSize based on TmnxLSPBuffSize"""
    defaultValue = 1492


_VRtrIsisSysOrigL2LSPBuffSize_Type.__name__ = "TmnxLSPBuffSize"
_VRtrIsisSysOrigL2LSPBuffSize_Object = MibTableColumn
vRtrIsisSysOrigL2LSPBuffSize = _VRtrIsisSysOrigL2LSPBuffSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 42),
    _VRtrIsisSysOrigL2LSPBuffSize_Type()
)
vRtrIsisSysOrigL2LSPBuffSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisSysOrigL2LSPBuffSize.setStatus("deprecated")


class _VRtrIsisLdpSyncAdminState_Type(TruthValue):
    """Custom type vRtrIsisLdpSyncAdminState based on TruthValue"""
    defaultValue = 1


_VRtrIsisLdpSyncAdminState_Type.__name__ = "TruthValue"
_VRtrIsisLdpSyncAdminState_Object = MibTableColumn
vRtrIsisLdpSyncAdminState = _VRtrIsisLdpSyncAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 43),
    _VRtrIsisLdpSyncAdminState_Type()
)
vRtrIsisLdpSyncAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLdpSyncAdminState.setStatus("deprecated")


class _VRtrIsisIPv6UnicastImport_Type(TruthValue):
    """Custom type vRtrIsisIPv6UnicastImport based on TruthValue"""
    defaultValue = 1


_VRtrIsisIPv6UnicastImport_Type.__name__ = "TruthValue"
_VRtrIsisIPv6UnicastImport_Object = MibTableColumn
vRtrIsisIPv6UnicastImport = _VRtrIsisIPv6UnicastImport_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 44),
    _VRtrIsisIPv6UnicastImport_Type()
)
vRtrIsisIPv6UnicastImport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIPv6UnicastImport.setStatus("deprecated")


class _VRtrIsisIPv6MulticastImport_Type(TruthValue):
    """Custom type vRtrIsisIPv6MulticastImport based on TruthValue"""
    defaultValue = 2


_VRtrIsisIPv6MulticastImport_Type.__name__ = "TruthValue"
_VRtrIsisIPv6MulticastImport_Object = MibTableColumn
vRtrIsisIPv6MulticastImport = _VRtrIsisIPv6MulticastImport_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 45),
    _VRtrIsisIPv6MulticastImport_Type()
)
vRtrIsisIPv6MulticastImport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIPv6MulticastImport.setStatus("deprecated")


class _VRtrIsisAdvertisePassiveOnly_Type(TruthValue):
    """Custom type vRtrIsisAdvertisePassiveOnly based on TruthValue"""
    defaultValue = 2


_VRtrIsisAdvertisePassiveOnly_Type.__name__ = "TruthValue"
_VRtrIsisAdvertisePassiveOnly_Object = MibTableColumn
vRtrIsisAdvertisePassiveOnly = _VRtrIsisAdvertisePassiveOnly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 46),
    _VRtrIsisAdvertisePassiveOnly_Type()
)
vRtrIsisAdvertisePassiveOnly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisAdvertisePassiveOnly.setStatus("deprecated")


class _VRtrIsisDefaultRouteTag_Type(Unsigned32):
    """Custom type vRtrIsisDefaultRouteTag based on Unsigned32"""
    defaultValue = 0


_VRtrIsisDefaultRouteTag_Type.__name__ = "Unsigned32"
_VRtrIsisDefaultRouteTag_Object = MibTableColumn
vRtrIsisDefaultRouteTag = _VRtrIsisDefaultRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 47),
    _VRtrIsisDefaultRouteTag_Type()
)
vRtrIsisDefaultRouteTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisDefaultRouteTag.setStatus("deprecated")


class _VRtrIsisSuppressDefault_Type(TruthValue):
    """Custom type vRtrIsisSuppressDefault based on TruthValue"""
    defaultValue = 2


_VRtrIsisSuppressDefault_Type.__name__ = "TruthValue"
_VRtrIsisSuppressDefault_Object = MibTableColumn
vRtrIsisSuppressDefault = _VRtrIsisSuppressDefault_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 48),
    _VRtrIsisSuppressDefault_Type()
)
vRtrIsisSuppressDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisSuppressDefault.setStatus("deprecated")


class _VRtrIsisLdpOverRsvp_Type(TmnxEnabledDisabled):
    """Custom type vRtrIsisLdpOverRsvp based on TmnxEnabledDisabled"""
    defaultValue = 2


_VRtrIsisLdpOverRsvp_Type.__name__ = "TmnxEnabledDisabled"
_VRtrIsisLdpOverRsvp_Object = MibTableColumn
vRtrIsisLdpOverRsvp = _VRtrIsisLdpOverRsvp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 49),
    _VRtrIsisLdpOverRsvp_Type()
)
vRtrIsisLdpOverRsvp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLdpOverRsvp.setStatus("deprecated")


class _VRtrIsisExportLimit_Type(Unsigned32):
    """Custom type vRtrIsisExportLimit based on Unsigned32"""
    defaultValue = 0


_VRtrIsisExportLimit_Type.__name__ = "Unsigned32"
_VRtrIsisExportLimit_Object = MibTableColumn
vRtrIsisExportLimit = _VRtrIsisExportLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 50),
    _VRtrIsisExportLimit_Type()
)
vRtrIsisExportLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisExportLimit.setStatus("deprecated")


class _VRtrIsisExportLimitLogPercent_Type(Unsigned32):
    """Custom type vRtrIsisExportLimitLogPercent based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VRtrIsisExportLimitLogPercent_Type.__name__ = "Unsigned32"
_VRtrIsisExportLimitLogPercent_Object = MibTableColumn
vRtrIsisExportLimitLogPercent = _VRtrIsisExportLimitLogPercent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 51),
    _VRtrIsisExportLimitLogPercent_Type()
)
vRtrIsisExportLimitLogPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisExportLimitLogPercent.setStatus("deprecated")
if mibBuilder.loadTexts:
    vRtrIsisExportLimitLogPercent.setUnits("percentage")
_VRtrIsisTotalL1ExportedRoutes_Type = Gauge32
_VRtrIsisTotalL1ExportedRoutes_Object = MibTableColumn
vRtrIsisTotalL1ExportedRoutes = _VRtrIsisTotalL1ExportedRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 52),
    _VRtrIsisTotalL1ExportedRoutes_Type()
)
vRtrIsisTotalL1ExportedRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisTotalL1ExportedRoutes.setStatus("deprecated")
_VRtrIsisTotalL2ExportedRoutes_Type = Gauge32
_VRtrIsisTotalL2ExportedRoutes_Object = MibTableColumn
vRtrIsisTotalL2ExportedRoutes = _VRtrIsisTotalL2ExportedRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 53),
    _VRtrIsisTotalL2ExportedRoutes_Type()
)
vRtrIsisTotalL2ExportedRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisTotalL2ExportedRoutes.setStatus("deprecated")


class _VRtrIsisRsvpShortcut_Type(TruthValue):
    """Custom type vRtrIsisRsvpShortcut based on TruthValue"""
    defaultValue = 2


_VRtrIsisRsvpShortcut_Type.__name__ = "TruthValue"
_VRtrIsisRsvpShortcut_Object = MibTableColumn
vRtrIsisRsvpShortcut = _VRtrIsisRsvpShortcut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 54),
    _VRtrIsisRsvpShortcut_Type()
)
vRtrIsisRsvpShortcut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisRsvpShortcut.setStatus("deprecated")


class _VRtrIsisAdvertiseTunnelLink_Type(TruthValue):
    """Custom type vRtrIsisAdvertiseTunnelLink based on TruthValue"""
    defaultValue = 2


_VRtrIsisAdvertiseTunnelLink_Type.__name__ = "TruthValue"
_VRtrIsisAdvertiseTunnelLink_Object = MibTableColumn
vRtrIsisAdvertiseTunnelLink = _VRtrIsisAdvertiseTunnelLink_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 55),
    _VRtrIsisAdvertiseTunnelLink_Type()
)
vRtrIsisAdvertiseTunnelLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisAdvertiseTunnelLink.setStatus("deprecated")


class _VRtrIsisIidTlv_Type(TmnxEnabledDisabled):
    """Custom type vRtrIsisIidTlv based on TmnxEnabledDisabled"""
    defaultValue = 2


_VRtrIsisIidTlv_Type.__name__ = "TmnxEnabledDisabled"
_VRtrIsisIidTlv_Object = MibTableColumn
vRtrIsisIidTlv = _VRtrIsisIidTlv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 56),
    _VRtrIsisIidTlv_Type()
)
vRtrIsisIidTlv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIidTlv.setStatus("deprecated")


class _VRtrIsisL1MacAddress_Type(MacAddress):
    """Custom type vRtrIsisL1MacAddress based on MacAddress"""
    defaultHexValue = "0180C2000014"


_VRtrIsisL1MacAddress_Type.__name__ = "MacAddress"
_VRtrIsisL1MacAddress_Object = MibTableColumn
vRtrIsisL1MacAddress = _VRtrIsisL1MacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 57),
    _VRtrIsisL1MacAddress_Type()
)
vRtrIsisL1MacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisL1MacAddress.setStatus("deprecated")


class _VRtrIsisL2MacAddress_Type(MacAddress):
    """Custom type vRtrIsisL2MacAddress based on MacAddress"""
    defaultHexValue = "0180C2000015"


_VRtrIsisL2MacAddress_Type.__name__ = "MacAddress"
_VRtrIsisL2MacAddress_Object = MibTableColumn
vRtrIsisL2MacAddress = _VRtrIsisL2MacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 58),
    _VRtrIsisL2MacAddress_Type()
)
vRtrIsisL2MacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisL2MacAddress.setStatus("deprecated")
_VRtrIsisSysOperL1LSPBuffSize_Type = TmnxLSPBuffSize
_VRtrIsisSysOperL1LSPBuffSize_Object = MibTableColumn
vRtrIsisSysOperL1LSPBuffSize = _VRtrIsisSysOperL1LSPBuffSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 59),
    _VRtrIsisSysOperL1LSPBuffSize_Type()
)
vRtrIsisSysOperL1LSPBuffSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisSysOperL1LSPBuffSize.setStatus("deprecated")
_VRtrIsisSysOperL2LSPBuffSize_Type = TmnxLSPBuffSize
_VRtrIsisSysOperL2LSPBuffSize_Object = MibTableColumn
vRtrIsisSysOperL2LSPBuffSize = _VRtrIsisSysOperL2LSPBuffSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 60),
    _VRtrIsisSysOperL2LSPBuffSize_Type()
)
vRtrIsisSysOperL2LSPBuffSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisSysOperL2LSPBuffSize.setStatus("deprecated")


class _VRtrIsisLoopfreeAlternate_Type(TruthValue):
    """Custom type vRtrIsisLoopfreeAlternate based on TruthValue"""
    defaultValue = 2


_VRtrIsisLoopfreeAlternate_Type.__name__ = "TruthValue"
_VRtrIsisLoopfreeAlternate_Object = MibTableColumn
vRtrIsisLoopfreeAlternate = _VRtrIsisLoopfreeAlternate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 61),
    _VRtrIsisLoopfreeAlternate_Type()
)
vRtrIsisLoopfreeAlternate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLoopfreeAlternate.setStatus("deprecated")


class _VRtrIsisIPv4McastRoutingTopo_Type(IsisRoutingTopology):
    """Custom type vRtrIsisIPv4McastRoutingTopo based on IsisRoutingTopology"""
    defaultValue = 1


_VRtrIsisIPv4McastRoutingTopo_Type.__name__ = "IsisRoutingTopology"
_VRtrIsisIPv4McastRoutingTopo_Object = MibTableColumn
vRtrIsisIPv4McastRoutingTopo = _VRtrIsisIPv4McastRoutingTopo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 62),
    _VRtrIsisIPv4McastRoutingTopo_Type()
)
vRtrIsisIPv4McastRoutingTopo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIPv4McastRoutingTopo.setStatus("deprecated")


class _VRtrIsisIPv6McastRoutingTopo_Type(IsisRoutingTopology):
    """Custom type vRtrIsisIPv6McastRoutingTopo based on IsisRoutingTopology"""
    defaultValue = 1


_VRtrIsisIPv6McastRoutingTopo_Type.__name__ = "IsisRoutingTopology"
_VRtrIsisIPv6McastRoutingTopo_Object = MibTableColumn
vRtrIsisIPv6McastRoutingTopo = _VRtrIsisIPv6McastRoutingTopo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 63),
    _VRtrIsisIPv6McastRoutingTopo_Type()
)
vRtrIsisIPv6McastRoutingTopo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIPv6McastRoutingTopo.setStatus("deprecated")


class _VRtrIsisMultiTopoIPv4Mcast_Type(TruthValue):
    """Custom type vRtrIsisMultiTopoIPv4Mcast based on TruthValue"""
    defaultValue = 2


_VRtrIsisMultiTopoIPv4Mcast_Type.__name__ = "TruthValue"
_VRtrIsisMultiTopoIPv4Mcast_Object = MibTableColumn
vRtrIsisMultiTopoIPv4Mcast = _VRtrIsisMultiTopoIPv4Mcast_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 64),
    _VRtrIsisMultiTopoIPv4Mcast_Type()
)
vRtrIsisMultiTopoIPv4Mcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisMultiTopoIPv4Mcast.setStatus("deprecated")


class _VRtrIsisMultiTopoIPv6Mcast_Type(TruthValue):
    """Custom type vRtrIsisMultiTopoIPv6Mcast based on TruthValue"""
    defaultValue = 2


_VRtrIsisMultiTopoIPv6Mcast_Type.__name__ = "TruthValue"
_VRtrIsisMultiTopoIPv6Mcast_Object = MibTableColumn
vRtrIsisMultiTopoIPv6Mcast = _VRtrIsisMultiTopoIPv6Mcast_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 65),
    _VRtrIsisMultiTopoIPv6Mcast_Type()
)
vRtrIsisMultiTopoIPv6Mcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisMultiTopoIPv6Mcast.setStatus("deprecated")


class _VRtrIsisOverloadMaxMetric_Type(TruthValue):
    """Custom type vRtrIsisOverloadMaxMetric based on TruthValue"""
    defaultValue = 2


_VRtrIsisOverloadMaxMetric_Type.__name__ = "TruthValue"
_VRtrIsisOverloadMaxMetric_Object = MibTableColumn
vRtrIsisOverloadMaxMetric = _VRtrIsisOverloadMaxMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 66),
    _VRtrIsisOverloadMaxMetric_Type()
)
vRtrIsisOverloadMaxMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisOverloadMaxMetric.setStatus("deprecated")


class _VRtrIsisOverloadOnBootMaxMetric_Type(TruthValue):
    """Custom type vRtrIsisOverloadOnBootMaxMetric based on TruthValue"""
    defaultValue = 2


_VRtrIsisOverloadOnBootMaxMetric_Type.__name__ = "TruthValue"
_VRtrIsisOverloadOnBootMaxMetric_Object = MibTableColumn
vRtrIsisOverloadOnBootMaxMetric = _VRtrIsisOverloadOnBootMaxMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 67),
    _VRtrIsisOverloadOnBootMaxMetric_Type()
)
vRtrIsisOverloadOnBootMaxMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisOverloadOnBootMaxMetric.setStatus("deprecated")


class _VRtrIsisRouterId_Type(Unsigned32):
    """Custom type vRtrIsisRouterId based on Unsigned32"""
    defaultValue = 0


_VRtrIsisRouterId_Type.__name__ = "Unsigned32"
_VRtrIsisRouterId_Object = MibTableColumn
vRtrIsisRouterId = _VRtrIsisRouterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 68),
    _VRtrIsisRouterId_Type()
)
vRtrIsisRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisRouterId.setStatus("deprecated")


class _VRtrIsisAdvRtrCapability_Type(Integer32):
    """Custom type vRtrIsisAdvRtrCapability based on Integer32"""
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


_VRtrIsisAdvRtrCapability_Type.__name__ = "Integer32"
_VRtrIsisAdvRtrCapability_Object = MibTableColumn
vRtrIsisAdvRtrCapability = _VRtrIsisAdvRtrCapability_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 69),
    _VRtrIsisAdvRtrCapability_Type()
)
vRtrIsisAdvRtrCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisAdvRtrCapability.setStatus("deprecated")


class _VRtrIsisHelloPadding_Type(Integer32):
    """Custom type vRtrIsisHelloPadding based on Integer32"""
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


_VRtrIsisHelloPadding_Type.__name__ = "Integer32"
_VRtrIsisHelloPadding_Object = MibTableColumn
vRtrIsisHelloPadding = _VRtrIsisHelloPadding_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 70),
    _VRtrIsisHelloPadding_Type()
)
vRtrIsisHelloPadding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisHelloPadding.setStatus("deprecated")
_VRtrIsisOperRouterId_Type = Unsigned32
_VRtrIsisOperRouterId_Object = MibTableColumn
vRtrIsisOperRouterId = _VRtrIsisOperRouterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 71),
    _VRtrIsisOperRouterId_Type()
)
vRtrIsisOperRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisOperRouterId.setStatus("deprecated")


class _VRtrIsisIgnoreLspErrors_Type(TruthValue):
    """Custom type vRtrIsisIgnoreLspErrors based on TruthValue"""
    defaultValue = 2


_VRtrIsisIgnoreLspErrors_Type.__name__ = "TruthValue"
_VRtrIsisIgnoreLspErrors_Object = MibTableColumn
vRtrIsisIgnoreLspErrors = _VRtrIsisIgnoreLspErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 1, 1, 72),
    _VRtrIsisIgnoreLspErrors_Type()
)
vRtrIsisIgnoreLspErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIgnoreLspErrors.setStatus("deprecated")
_VRtrIsisLevelTable_Object = MibTable
vRtrIsisLevelTable = _VRtrIsisLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 2)
)
if mibBuilder.loadTexts:
    vRtrIsisLevelTable.setStatus("deprecated")
_VRtrIsisLevelEntry_Object = MibTableRow
vRtrIsisLevelEntry = _VRtrIsisLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 2, 1)
)
vRtrIsisLevelEntry.setIndexNames(
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "TIMETRA-ISIS-MIB", "vRtrIsisLevel"),
)
if mibBuilder.loadTexts:
    vRtrIsisLevelEntry.setStatus("deprecated")


class _VRtrIsisLevel_Type(Integer32):
    """Custom type vRtrIsisLevel based on Integer32"""
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


_VRtrIsisLevel_Type.__name__ = "Integer32"
_VRtrIsisLevel_Object = MibTableColumn
vRtrIsisLevel = _VRtrIsisLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 2, 1, 1),
    _VRtrIsisLevel_Type()
)
vRtrIsisLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIsisLevel.setStatus("deprecated")


class _VRtrIsisLevelAuthKey_Type(OctetString):
    """Custom type vRtrIsisLevelAuthKey based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_VRtrIsisLevelAuthKey_Type.__name__ = "OctetString"
_VRtrIsisLevelAuthKey_Object = MibTableColumn
vRtrIsisLevelAuthKey = _VRtrIsisLevelAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 2, 1, 2),
    _VRtrIsisLevelAuthKey_Type()
)
vRtrIsisLevelAuthKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLevelAuthKey.setStatus("deprecated")


class _VRtrIsisLevelAuthType_Type(Integer32):
    """Custom type vRtrIsisLevelAuthType based on Integer32"""
    defaultValue = 1

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


_VRtrIsisLevelAuthType_Type.__name__ = "Integer32"
_VRtrIsisLevelAuthType_Object = MibTableColumn
vRtrIsisLevelAuthType = _VRtrIsisLevelAuthType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 2, 1, 3),
    _VRtrIsisLevelAuthType_Type()
)
vRtrIsisLevelAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLevelAuthType.setStatus("deprecated")


class _VRtrIsisLevelExtPreference_Type(Unsigned32):
    """Custom type vRtrIsisLevelExtPreference based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VRtrIsisLevelExtPreference_Type.__name__ = "Unsigned32"
_VRtrIsisLevelExtPreference_Object = MibTableColumn
vRtrIsisLevelExtPreference = _VRtrIsisLevelExtPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 2, 1, 4),
    _VRtrIsisLevelExtPreference_Type()
)
vRtrIsisLevelExtPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLevelExtPreference.setStatus("deprecated")


class _VRtrIsisLevelPreference_Type(Unsigned32):
    """Custom type vRtrIsisLevelPreference based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VRtrIsisLevelPreference_Type.__name__ = "Unsigned32"
_VRtrIsisLevelPreference_Object = MibTableColumn
vRtrIsisLevelPreference = _VRtrIsisLevelPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 2, 1, 5),
    _VRtrIsisLevelPreference_Type()
)
vRtrIsisLevelPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLevelPreference.setStatus("deprecated")


class _VRtrIsisLevelWideMetricsOnly_Type(TruthValue):
    """Custom type vRtrIsisLevelWideMetricsOnly based on TruthValue"""
    defaultValue = 2


_VRtrIsisLevelWideMetricsOnly_Type.__name__ = "TruthValue"
_VRtrIsisLevelWideMetricsOnly_Object = MibTableColumn
vRtrIsisLevelWideMetricsOnly = _VRtrIsisLevelWideMetricsOnly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 2, 1, 6),
    _VRtrIsisLevelWideMetricsOnly_Type()
)
vRtrIsisLevelWideMetricsOnly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLevelWideMetricsOnly.setStatus("deprecated")


class _VRtrIsisLevelOverloadStatus_Type(Integer32):
    """Custom type vRtrIsisLevelOverloadStatus based on Integer32"""
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


_VRtrIsisLevelOverloadStatus_Type.__name__ = "Integer32"
_VRtrIsisLevelOverloadStatus_Object = MibTableColumn
vRtrIsisLevelOverloadStatus = _VRtrIsisLevelOverloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 2, 1, 7),
    _VRtrIsisLevelOverloadStatus_Type()
)
vRtrIsisLevelOverloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLevelOverloadStatus.setStatus("deprecated")
_VRtrIsisLevelOverloadTimeLeft_Type = TimeInterval
_VRtrIsisLevelOverloadTimeLeft_Object = MibTableColumn
vRtrIsisLevelOverloadTimeLeft = _VRtrIsisLevelOverloadTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 2, 1, 8),
    _VRtrIsisLevelOverloadTimeLeft_Type()
)
vRtrIsisLevelOverloadTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLevelOverloadTimeLeft.setStatus("deprecated")
_VRtrIsisLevelNumLSPs_Type = Unsigned32
_VRtrIsisLevelNumLSPs_Object = MibTableColumn
vRtrIsisLevelNumLSPs = _VRtrIsisLevelNumLSPs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 2, 1, 9),
    _VRtrIsisLevelNumLSPs_Type()
)
vRtrIsisLevelNumLSPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLevelNumLSPs.setStatus("deprecated")


class _VRtrIsisLevelCsnpAuthentication_Type(TruthValue):
    """Custom type vRtrIsisLevelCsnpAuthentication based on TruthValue"""
    defaultValue = 1


_VRtrIsisLevelCsnpAuthentication_Type.__name__ = "TruthValue"
_VRtrIsisLevelCsnpAuthentication_Object = MibTableColumn
vRtrIsisLevelCsnpAuthentication = _VRtrIsisLevelCsnpAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 2, 1, 10),
    _VRtrIsisLevelCsnpAuthentication_Type()
)
vRtrIsisLevelCsnpAuthentication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLevelCsnpAuthentication.setStatus("deprecated")


class _VRtrIsisLevelHelloAuthentication_Type(TruthValue):
    """Custom type vRtrIsisLevelHelloAuthentication based on TruthValue"""
    defaultValue = 1


_VRtrIsisLevelHelloAuthentication_Type.__name__ = "TruthValue"
_VRtrIsisLevelHelloAuthentication_Object = MibTableColumn
vRtrIsisLevelHelloAuthentication = _VRtrIsisLevelHelloAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 2, 1, 11),
    _VRtrIsisLevelHelloAuthentication_Type()
)
vRtrIsisLevelHelloAuthentication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLevelHelloAuthentication.setStatus("deprecated")


class _VRtrIsisLevelPsnpAuthentication_Type(TruthValue):
    """Custom type vRtrIsisLevelPsnpAuthentication based on TruthValue"""
    defaultValue = 1


_VRtrIsisLevelPsnpAuthentication_Type.__name__ = "TruthValue"
_VRtrIsisLevelPsnpAuthentication_Object = MibTableColumn
vRtrIsisLevelPsnpAuthentication = _VRtrIsisLevelPsnpAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 2, 1, 12),
    _VRtrIsisLevelPsnpAuthentication_Type()
)
vRtrIsisLevelPsnpAuthentication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLevelPsnpAuthentication.setStatus("deprecated")


class _VRtrIsisLevelDefMetric_Type(Unsigned32):
    """Custom type vRtrIsisLevelDefMetric based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_VRtrIsisLevelDefMetric_Type.__name__ = "Unsigned32"
_VRtrIsisLevelDefMetric_Object = MibTableColumn
vRtrIsisLevelDefMetric = _VRtrIsisLevelDefMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 2, 1, 13),
    _VRtrIsisLevelDefMetric_Type()
)
vRtrIsisLevelDefMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLevelDefMetric.setStatus("deprecated")


class _VRtrIsisLevelIPv6DefMetric_Type(Unsigned32):
    """Custom type vRtrIsisLevelIPv6DefMetric based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_VRtrIsisLevelIPv6DefMetric_Type.__name__ = "Unsigned32"
_VRtrIsisLevelIPv6DefMetric_Object = MibTableColumn
vRtrIsisLevelIPv6DefMetric = _VRtrIsisLevelIPv6DefMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 2, 1, 14),
    _VRtrIsisLevelIPv6DefMetric_Type()
)
vRtrIsisLevelIPv6DefMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLevelIPv6DefMetric.setStatus("deprecated")


class _VRtrIsisLevelLoopfreeAltExclude_Type(TruthValue):
    """Custom type vRtrIsisLevelLoopfreeAltExclude based on TruthValue"""
    defaultValue = 2


_VRtrIsisLevelLoopfreeAltExclude_Type.__name__ = "TruthValue"
_VRtrIsisLevelLoopfreeAltExclude_Object = MibTableColumn
vRtrIsisLevelLoopfreeAltExclude = _VRtrIsisLevelLoopfreeAltExclude_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 2, 1, 15),
    _VRtrIsisLevelLoopfreeAltExclude_Type()
)
vRtrIsisLevelLoopfreeAltExclude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLevelLoopfreeAltExclude.setStatus("deprecated")


class _VRtrIsisLevelDefIPv4McastMetric_Type(Unsigned32):
    """Custom type vRtrIsisLevelDefIPv4McastMetric based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_VRtrIsisLevelDefIPv4McastMetric_Type.__name__ = "Unsigned32"
_VRtrIsisLevelDefIPv4McastMetric_Object = MibTableColumn
vRtrIsisLevelDefIPv4McastMetric = _VRtrIsisLevelDefIPv4McastMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 2, 1, 16),
    _VRtrIsisLevelDefIPv4McastMetric_Type()
)
vRtrIsisLevelDefIPv4McastMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLevelDefIPv4McastMetric.setStatus("deprecated")


class _VRtrIsisLevelDefIPv6McastMetric_Type(Unsigned32):
    """Custom type vRtrIsisLevelDefIPv6McastMetric based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_VRtrIsisLevelDefIPv6McastMetric_Type.__name__ = "Unsigned32"
_VRtrIsisLevelDefIPv6McastMetric_Object = MibTableColumn
vRtrIsisLevelDefIPv6McastMetric = _VRtrIsisLevelDefIPv6McastMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 2, 1, 17),
    _VRtrIsisLevelDefIPv6McastMetric_Type()
)
vRtrIsisLevelDefIPv6McastMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLevelDefIPv6McastMetric.setStatus("deprecated")


class _VRtrIsisLevelAdvRtrCapability_Type(TruthValue):
    """Custom type vRtrIsisLevelAdvRtrCapability based on TruthValue"""
    defaultValue = 1


_VRtrIsisLevelAdvRtrCapability_Type.__name__ = "TruthValue"
_VRtrIsisLevelAdvRtrCapability_Object = MibTableColumn
vRtrIsisLevelAdvRtrCapability = _VRtrIsisLevelAdvRtrCapability_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 2, 1, 18),
    _VRtrIsisLevelAdvRtrCapability_Type()
)
vRtrIsisLevelAdvRtrCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLevelAdvRtrCapability.setStatus("deprecated")
_VRtrIsisStatsTable_Object = MibTable
vRtrIsisStatsTable = _VRtrIsisStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 3)
)
if mibBuilder.loadTexts:
    vRtrIsisStatsTable.setStatus("deprecated")
_VRtrIsisStatsEntry_Object = MibTableRow
vRtrIsisStatsEntry = _VRtrIsisStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 3, 1)
)
vRtrIsisStatsEntry.setIndexNames(
    (0, "ISIS-MIB", "isisSysInstance"),
)
if mibBuilder.loadTexts:
    vRtrIsisStatsEntry.setStatus("deprecated")
_VRtrIsisSpfRuns_Type = Counter32
_VRtrIsisSpfRuns_Object = MibTableColumn
vRtrIsisSpfRuns = _VRtrIsisSpfRuns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 3, 1, 1),
    _VRtrIsisSpfRuns_Type()
)
vRtrIsisSpfRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisSpfRuns.setStatus("deprecated")
_VRtrIsisLSPRegenerations_Type = Counter32
_VRtrIsisLSPRegenerations_Object = MibTableColumn
vRtrIsisLSPRegenerations = _VRtrIsisLSPRegenerations_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 3, 1, 2),
    _VRtrIsisLSPRegenerations_Type()
)
vRtrIsisLSPRegenerations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLSPRegenerations.setStatus("deprecated")
_VRtrIsisInitiatedPurges_Type = Counter32
_VRtrIsisInitiatedPurges_Object = MibTableColumn
vRtrIsisInitiatedPurges = _VRtrIsisInitiatedPurges_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 3, 1, 3),
    _VRtrIsisInitiatedPurges_Type()
)
vRtrIsisInitiatedPurges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisInitiatedPurges.setStatus("deprecated")
_VRtrIsisLSPRecd_Type = Counter32
_VRtrIsisLSPRecd_Object = MibTableColumn
vRtrIsisLSPRecd = _VRtrIsisLSPRecd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 3, 1, 4),
    _VRtrIsisLSPRecd_Type()
)
vRtrIsisLSPRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLSPRecd.setStatus("deprecated")
_VRtrIsisLSPDrop_Type = Counter32
_VRtrIsisLSPDrop_Object = MibTableColumn
vRtrIsisLSPDrop = _VRtrIsisLSPDrop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 3, 1, 5),
    _VRtrIsisLSPDrop_Type()
)
vRtrIsisLSPDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLSPDrop.setStatus("deprecated")
_VRtrIsisLSPSent_Type = Counter32
_VRtrIsisLSPSent_Object = MibTableColumn
vRtrIsisLSPSent = _VRtrIsisLSPSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 3, 1, 6),
    _VRtrIsisLSPSent_Type()
)
vRtrIsisLSPSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLSPSent.setStatus("deprecated")
_VRtrIsisLSPRetrans_Type = Counter32
_VRtrIsisLSPRetrans_Object = MibTableColumn
vRtrIsisLSPRetrans = _VRtrIsisLSPRetrans_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 3, 1, 7),
    _VRtrIsisLSPRetrans_Type()
)
vRtrIsisLSPRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLSPRetrans.setStatus("deprecated")
_VRtrIsisIIHRecd_Type = Counter32
_VRtrIsisIIHRecd_Object = MibTableColumn
vRtrIsisIIHRecd = _VRtrIsisIIHRecd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 3, 1, 8),
    _VRtrIsisIIHRecd_Type()
)
vRtrIsisIIHRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIIHRecd.setStatus("deprecated")
_VRtrIsisIIHDrop_Type = Counter32
_VRtrIsisIIHDrop_Object = MibTableColumn
vRtrIsisIIHDrop = _VRtrIsisIIHDrop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 3, 1, 9),
    _VRtrIsisIIHDrop_Type()
)
vRtrIsisIIHDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIIHDrop.setStatus("deprecated")
_VRtrIsisIIHSent_Type = Counter32
_VRtrIsisIIHSent_Object = MibTableColumn
vRtrIsisIIHSent = _VRtrIsisIIHSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 3, 1, 10),
    _VRtrIsisIIHSent_Type()
)
vRtrIsisIIHSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIIHSent.setStatus("deprecated")
_VRtrIsisIIHRetrans_Type = Counter32
_VRtrIsisIIHRetrans_Object = MibTableColumn
vRtrIsisIIHRetrans = _VRtrIsisIIHRetrans_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 3, 1, 11),
    _VRtrIsisIIHRetrans_Type()
)
vRtrIsisIIHRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIIHRetrans.setStatus("deprecated")
_VRtrIsisCSNPRecd_Type = Counter32
_VRtrIsisCSNPRecd_Object = MibTableColumn
vRtrIsisCSNPRecd = _VRtrIsisCSNPRecd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 3, 1, 12),
    _VRtrIsisCSNPRecd_Type()
)
vRtrIsisCSNPRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisCSNPRecd.setStatus("deprecated")
_VRtrIsisCSNPDrop_Type = Counter32
_VRtrIsisCSNPDrop_Object = MibTableColumn
vRtrIsisCSNPDrop = _VRtrIsisCSNPDrop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 3, 1, 13),
    _VRtrIsisCSNPDrop_Type()
)
vRtrIsisCSNPDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisCSNPDrop.setStatus("deprecated")
_VRtrIsisCSNPSent_Type = Counter32
_VRtrIsisCSNPSent_Object = MibTableColumn
vRtrIsisCSNPSent = _VRtrIsisCSNPSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 3, 1, 14),
    _VRtrIsisCSNPSent_Type()
)
vRtrIsisCSNPSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisCSNPSent.setStatus("deprecated")
_VRtrIsisCSNPRetrans_Type = Counter32
_VRtrIsisCSNPRetrans_Object = MibTableColumn
vRtrIsisCSNPRetrans = _VRtrIsisCSNPRetrans_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 3, 1, 15),
    _VRtrIsisCSNPRetrans_Type()
)
vRtrIsisCSNPRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisCSNPRetrans.setStatus("deprecated")
_VRtrIsisPSNPRecd_Type = Counter32
_VRtrIsisPSNPRecd_Object = MibTableColumn
vRtrIsisPSNPRecd = _VRtrIsisPSNPRecd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 3, 1, 16),
    _VRtrIsisPSNPRecd_Type()
)
vRtrIsisPSNPRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisPSNPRecd.setStatus("deprecated")
_VRtrIsisPSNPDrop_Type = Counter32
_VRtrIsisPSNPDrop_Object = MibTableColumn
vRtrIsisPSNPDrop = _VRtrIsisPSNPDrop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 3, 1, 17),
    _VRtrIsisPSNPDrop_Type()
)
vRtrIsisPSNPDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisPSNPDrop.setStatus("deprecated")
_VRtrIsisPSNPSent_Type = Counter32
_VRtrIsisPSNPSent_Object = MibTableColumn
vRtrIsisPSNPSent = _VRtrIsisPSNPSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 3, 1, 18),
    _VRtrIsisPSNPSent_Type()
)
vRtrIsisPSNPSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisPSNPSent.setStatus("deprecated")
_VRtrIsisPSNPRetrans_Type = Counter32
_VRtrIsisPSNPRetrans_Object = MibTableColumn
vRtrIsisPSNPRetrans = _VRtrIsisPSNPRetrans_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 3, 1, 19),
    _VRtrIsisPSNPRetrans_Type()
)
vRtrIsisPSNPRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisPSNPRetrans.setStatus("deprecated")
_VRtrIsisUnknownRecd_Type = Counter32
_VRtrIsisUnknownRecd_Object = MibTableColumn
vRtrIsisUnknownRecd = _VRtrIsisUnknownRecd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 3, 1, 20),
    _VRtrIsisUnknownRecd_Type()
)
vRtrIsisUnknownRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisUnknownRecd.setStatus("deprecated")
_VRtrIsisUnknownDrop_Type = Counter32
_VRtrIsisUnknownDrop_Object = MibTableColumn
vRtrIsisUnknownDrop = _VRtrIsisUnknownDrop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 3, 1, 21),
    _VRtrIsisUnknownDrop_Type()
)
vRtrIsisUnknownDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisUnknownDrop.setStatus("deprecated")
_VRtrIsisUnknownSent_Type = Counter32
_VRtrIsisUnknownSent_Object = MibTableColumn
vRtrIsisUnknownSent = _VRtrIsisUnknownSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 3, 1, 22),
    _VRtrIsisUnknownSent_Type()
)
vRtrIsisUnknownSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisUnknownSent.setStatus("deprecated")
_VRtrIsisUnknownRetrans_Type = Counter32
_VRtrIsisUnknownRetrans_Object = MibTableColumn
vRtrIsisUnknownRetrans = _VRtrIsisUnknownRetrans_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 3, 1, 23),
    _VRtrIsisUnknownRetrans_Type()
)
vRtrIsisUnknownRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisUnknownRetrans.setStatus("deprecated")
_VRtrIsisCSPFRequests_Type = Counter32
_VRtrIsisCSPFRequests_Object = MibTableColumn
vRtrIsisCSPFRequests = _VRtrIsisCSPFRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 3, 1, 24),
    _VRtrIsisCSPFRequests_Type()
)
vRtrIsisCSPFRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisCSPFRequests.setStatus("deprecated")
_VRtrIsisCSPFDroppedRequests_Type = Counter32
_VRtrIsisCSPFDroppedRequests_Object = MibTableColumn
vRtrIsisCSPFDroppedRequests = _VRtrIsisCSPFDroppedRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 3, 1, 25),
    _VRtrIsisCSPFDroppedRequests_Type()
)
vRtrIsisCSPFDroppedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisCSPFDroppedRequests.setStatus("deprecated")
_VRtrIsisCSPFPathsFound_Type = Counter32
_VRtrIsisCSPFPathsFound_Object = MibTableColumn
vRtrIsisCSPFPathsFound = _VRtrIsisCSPFPathsFound_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 3, 1, 26),
    _VRtrIsisCSPFPathsFound_Type()
)
vRtrIsisCSPFPathsFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisCSPFPathsFound.setStatus("deprecated")
_VRtrIsisCSPFPathsNotFound_Type = Counter32
_VRtrIsisCSPFPathsNotFound_Object = MibTableColumn
vRtrIsisCSPFPathsNotFound = _VRtrIsisCSPFPathsNotFound_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 3, 1, 27),
    _VRtrIsisCSPFPathsNotFound_Type()
)
vRtrIsisCSPFPathsNotFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisCSPFPathsNotFound.setStatus("deprecated")
_VRtrIsisLfaRuns_Type = Counter32
_VRtrIsisLfaRuns_Object = MibTableColumn
vRtrIsisLfaRuns = _VRtrIsisLfaRuns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 3, 1, 28),
    _VRtrIsisLfaRuns_Type()
)
vRtrIsisLfaRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLfaRuns.setStatus("deprecated")
_VRtrIsisHostnameTable_Object = MibTable
vRtrIsisHostnameTable = _VRtrIsisHostnameTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 4)
)
if mibBuilder.loadTexts:
    vRtrIsisHostnameTable.setStatus("deprecated")
_VRtrIsisHostnameEntry_Object = MibTableRow
vRtrIsisHostnameEntry = _VRtrIsisHostnameEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 4, 1)
)
vRtrIsisHostnameEntry.setIndexNames(
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "TIMETRA-ISIS-MIB", "vRtrIsisSysID"),
)
if mibBuilder.loadTexts:
    vRtrIsisHostnameEntry.setStatus("deprecated")
_VRtrIsisSysID_Type = SystemID
_VRtrIsisSysID_Object = MibTableColumn
vRtrIsisSysID = _VRtrIsisSysID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 4, 1, 1),
    _VRtrIsisSysID_Type()
)
vRtrIsisSysID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIsisSysID.setStatus("deprecated")
_VRtrIsisHostname_Type = DisplayString
_VRtrIsisHostname_Object = MibTableColumn
vRtrIsisHostname = _VRtrIsisHostname_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 4, 1, 2),
    _VRtrIsisHostname_Type()
)
vRtrIsisHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisHostname.setStatus("deprecated")
_VRtrIsisRouteTable_Object = MibTable
vRtrIsisRouteTable = _VRtrIsisRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 5)
)
if mibBuilder.loadTexts:
    vRtrIsisRouteTable.setStatus("deprecated")
_VRtrIsisRouteEntry_Object = MibTableRow
vRtrIsisRouteEntry = _VRtrIsisRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 5, 1)
)
vRtrIsisRouteEntry.setIndexNames(
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "TIMETRA-ISIS-MIB", "vRtrIsisRouteDest"),
    (0, "TIMETRA-ISIS-MIB", "vRtrIsisRouteMask"),
    (0, "TIMETRA-ISIS-MIB", "vRtrIsisRouteNexthopIP"),
)
if mibBuilder.loadTexts:
    vRtrIsisRouteEntry.setStatus("deprecated")
_VRtrIsisRouteDest_Type = IpAddress
_VRtrIsisRouteDest_Object = MibTableColumn
vRtrIsisRouteDest = _VRtrIsisRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 5, 1, 1),
    _VRtrIsisRouteDest_Type()
)
vRtrIsisRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIsisRouteDest.setStatus("deprecated")
_VRtrIsisRouteMask_Type = IpAddress
_VRtrIsisRouteMask_Object = MibTableColumn
vRtrIsisRouteMask = _VRtrIsisRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 5, 1, 2),
    _VRtrIsisRouteMask_Type()
)
vRtrIsisRouteMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIsisRouteMask.setStatus("deprecated")
_VRtrIsisRouteNexthopIP_Type = IpAddress
_VRtrIsisRouteNexthopIP_Object = MibTableColumn
vRtrIsisRouteNexthopIP = _VRtrIsisRouteNexthopIP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 5, 1, 3),
    _VRtrIsisRouteNexthopIP_Type()
)
vRtrIsisRouteNexthopIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIsisRouteNexthopIP.setStatus("deprecated")


class _VRtrIsisRouteLevel_Type(Integer32):
    """Custom type vRtrIsisRouteLevel based on Integer32"""
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


_VRtrIsisRouteLevel_Type.__name__ = "Integer32"
_VRtrIsisRouteLevel_Object = MibTableColumn
vRtrIsisRouteLevel = _VRtrIsisRouteLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 5, 1, 4),
    _VRtrIsisRouteLevel_Type()
)
vRtrIsisRouteLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisRouteLevel.setStatus("deprecated")
_VRtrIsisRouteSpfVersion_Type = Counter32
_VRtrIsisRouteSpfVersion_Object = MibTableColumn
vRtrIsisRouteSpfVersion = _VRtrIsisRouteSpfVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 5, 1, 5),
    _VRtrIsisRouteSpfVersion_Type()
)
vRtrIsisRouteSpfVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisRouteSpfVersion.setStatus("deprecated")
_VRtrIsisRouteMetric_Type = Unsigned32
_VRtrIsisRouteMetric_Object = MibTableColumn
vRtrIsisRouteMetric = _VRtrIsisRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 5, 1, 6),
    _VRtrIsisRouteMetric_Type()
)
vRtrIsisRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisRouteMetric.setStatus("deprecated")


class _VRtrIsisRouteType_Type(Integer32):
    """Custom type vRtrIsisRouteType based on Integer32"""
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


_VRtrIsisRouteType_Type.__name__ = "Integer32"
_VRtrIsisRouteType_Object = MibTableColumn
vRtrIsisRouteType = _VRtrIsisRouteType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 5, 1, 7),
    _VRtrIsisRouteType_Type()
)
vRtrIsisRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisRouteType.setStatus("deprecated")
_VRtrIsisRouteNHopSysID_Type = SystemID
_VRtrIsisRouteNHopSysID_Object = MibTableColumn
vRtrIsisRouteNHopSysID = _VRtrIsisRouteNHopSysID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 5, 1, 8),
    _VRtrIsisRouteNHopSysID_Type()
)
vRtrIsisRouteNHopSysID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisRouteNHopSysID.setStatus("deprecated")
_VRtrIsisPathTable_Object = MibTable
vRtrIsisPathTable = _VRtrIsisPathTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 6)
)
if mibBuilder.loadTexts:
    vRtrIsisPathTable.setStatus("deprecated")
_VRtrIsisPathEntry_Object = MibTableRow
vRtrIsisPathEntry = _VRtrIsisPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 6, 1)
)
vRtrIsisPathEntry.setIndexNames(
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "TIMETRA-ISIS-MIB", "vRtrIsisLevel"),
    (0, "TIMETRA-ISIS-MIB", "vRtrIsisPathID"),
    (0, "TIMETRA-ISIS-MIB", "vRtrIsisPathIfIndex"),
    (0, "TIMETRA-ISIS-MIB", "vRtrIsisPathNHopSysID"),
)
if mibBuilder.loadTexts:
    vRtrIsisPathEntry.setStatus("deprecated")


class _VRtrIsisPathID_Type(OctetString):
    """Custom type vRtrIsisPathID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_VRtrIsisPathID_Type.__name__ = "OctetString"
_VRtrIsisPathID_Object = MibTableColumn
vRtrIsisPathID = _VRtrIsisPathID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 6, 1, 1),
    _VRtrIsisPathID_Type()
)
vRtrIsisPathID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIsisPathID.setStatus("deprecated")
_VRtrIsisPathIfIndex_Type = InterfaceIndex
_VRtrIsisPathIfIndex_Object = MibTableColumn
vRtrIsisPathIfIndex = _VRtrIsisPathIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 6, 1, 2),
    _VRtrIsisPathIfIndex_Type()
)
vRtrIsisPathIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIsisPathIfIndex.setStatus("deprecated")
_VRtrIsisPathNHopSysID_Type = SystemID
_VRtrIsisPathNHopSysID_Object = MibTableColumn
vRtrIsisPathNHopSysID = _VRtrIsisPathNHopSysID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 6, 1, 3),
    _VRtrIsisPathNHopSysID_Type()
)
vRtrIsisPathNHopSysID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIsisPathNHopSysID.setStatus("deprecated")
_VRtrIsisPathMetric_Type = Unsigned32
_VRtrIsisPathMetric_Object = MibTableColumn
vRtrIsisPathMetric = _VRtrIsisPathMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 6, 1, 4),
    _VRtrIsisPathMetric_Type()
)
vRtrIsisPathMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisPathMetric.setStatus("deprecated")
_VRtrIsisPathSNPA_Type = SNPAAddress
_VRtrIsisPathSNPA_Object = MibTableColumn
vRtrIsisPathSNPA = _VRtrIsisPathSNPA_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 6, 1, 5),
    _VRtrIsisPathSNPA_Type()
)
vRtrIsisPathSNPA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisPathSNPA.setStatus("deprecated")
_VRtrIsisPathLfaIfIndex_Type = InterfaceIndex
_VRtrIsisPathLfaIfIndex_Object = MibTableColumn
vRtrIsisPathLfaIfIndex = _VRtrIsisPathLfaIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 6, 1, 6),
    _VRtrIsisPathLfaIfIndex_Type()
)
vRtrIsisPathLfaIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisPathLfaIfIndex.setStatus("deprecated")
_VRtrIsisPathLfaNHop_Type = SystemID
_VRtrIsisPathLfaNHop_Object = MibTableColumn
vRtrIsisPathLfaNHop = _VRtrIsisPathLfaNHop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 6, 1, 7),
    _VRtrIsisPathLfaNHop_Type()
)
vRtrIsisPathLfaNHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisPathLfaNHop.setStatus("deprecated")
_VRtrIsisPathLfaMetric_Type = Unsigned32
_VRtrIsisPathLfaMetric_Object = MibTableColumn
vRtrIsisPathLfaMetric = _VRtrIsisPathLfaMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 6, 1, 8),
    _VRtrIsisPathLfaMetric_Type()
)
vRtrIsisPathLfaMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisPathLfaMetric.setStatus("deprecated")


class _VRtrIsisPathLfaType_Type(Integer32):
    """Custom type vRtrIsisPathLfaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noProtection", 0),
          ("nodeProtection", 1),
          ("linkProtection", 2))
    )


_VRtrIsisPathLfaType_Type.__name__ = "Integer32"
_VRtrIsisPathLfaType_Object = MibTableColumn
vRtrIsisPathLfaType = _VRtrIsisPathLfaType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 6, 1, 9),
    _VRtrIsisPathLfaType_Type()
)
vRtrIsisPathLfaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisPathLfaType.setStatus("deprecated")


class _VRtrIsisPathRouteType_Type(Integer32):
    """Custom type vRtrIsisPathRouteType based on Integer32"""
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


_VRtrIsisPathRouteType_Type.__name__ = "Integer32"
_VRtrIsisPathRouteType_Object = MibTableColumn
vRtrIsisPathRouteType = _VRtrIsisPathRouteType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 6, 1, 10),
    _VRtrIsisPathRouteType_Type()
)
vRtrIsisPathRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisPathRouteType.setStatus("deprecated")
_VRtrIsisLSPTable_Object = MibTable
vRtrIsisLSPTable = _VRtrIsisLSPTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 7)
)
if mibBuilder.loadTexts:
    vRtrIsisLSPTable.setStatus("deprecated")
_VRtrIsisLSPEntry_Object = MibTableRow
vRtrIsisLSPEntry = _VRtrIsisLSPEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 7, 1)
)
vRtrIsisLSPEntry.setIndexNames(
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "TIMETRA-ISIS-MIB", "vRtrIsisLevel"),
    (0, "TIMETRA-ISIS-MIB", "vRtrIsisLSPId"),
)
if mibBuilder.loadTexts:
    vRtrIsisLSPEntry.setStatus("deprecated")


class _VRtrIsisLSPId_Type(OctetString):
    """Custom type vRtrIsisLSPId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_VRtrIsisLSPId_Type.__name__ = "OctetString"
_VRtrIsisLSPId_Object = MibTableColumn
vRtrIsisLSPId = _VRtrIsisLSPId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 7, 1, 1),
    _VRtrIsisLSPId_Type()
)
vRtrIsisLSPId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIsisLSPId.setStatus("deprecated")
_VRtrIsisLSPSeq_Type = Counter32
_VRtrIsisLSPSeq_Object = MibTableColumn
vRtrIsisLSPSeq = _VRtrIsisLSPSeq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 7, 1, 2),
    _VRtrIsisLSPSeq_Type()
)
vRtrIsisLSPSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLSPSeq.setStatus("deprecated")


class _VRtrIsisLSPChecksum_Type(Integer32):
    """Custom type vRtrIsisLSPChecksum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VRtrIsisLSPChecksum_Type.__name__ = "Integer32"
_VRtrIsisLSPChecksum_Object = MibTableColumn
vRtrIsisLSPChecksum = _VRtrIsisLSPChecksum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 7, 1, 3),
    _VRtrIsisLSPChecksum_Type()
)
vRtrIsisLSPChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLSPChecksum.setStatus("deprecated")


class _VRtrIsisLSPLifetimeRemain_Type(Integer32):
    """Custom type vRtrIsisLSPLifetimeRemain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VRtrIsisLSPLifetimeRemain_Type.__name__ = "Integer32"
_VRtrIsisLSPLifetimeRemain_Object = MibTableColumn
vRtrIsisLSPLifetimeRemain = _VRtrIsisLSPLifetimeRemain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 7, 1, 4),
    _VRtrIsisLSPLifetimeRemain_Type()
)
vRtrIsisLSPLifetimeRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLSPLifetimeRemain.setStatus("deprecated")
if mibBuilder.loadTexts:
    vRtrIsisLSPLifetimeRemain.setUnits("seconds")
_VRtrIsisLSPVersion_Type = Integer32
_VRtrIsisLSPVersion_Object = MibTableColumn
vRtrIsisLSPVersion = _VRtrIsisLSPVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 7, 1, 5),
    _VRtrIsisLSPVersion_Type()
)
vRtrIsisLSPVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLSPVersion.setStatus("deprecated")
_VRtrIsisLSPPktType_Type = Integer32
_VRtrIsisLSPPktType_Object = MibTableColumn
vRtrIsisLSPPktType = _VRtrIsisLSPPktType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 7, 1, 6),
    _VRtrIsisLSPPktType_Type()
)
vRtrIsisLSPPktType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLSPPktType.setStatus("deprecated")
_VRtrIsisLSPPktVersion_Type = Integer32
_VRtrIsisLSPPktVersion_Object = MibTableColumn
vRtrIsisLSPPktVersion = _VRtrIsisLSPPktVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 7, 1, 7),
    _VRtrIsisLSPPktVersion_Type()
)
vRtrIsisLSPPktVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLSPPktVersion.setStatus("deprecated")
_VRtrIsisLSPMaxArea_Type = Integer32
_VRtrIsisLSPMaxArea_Object = MibTableColumn
vRtrIsisLSPMaxArea = _VRtrIsisLSPMaxArea_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 7, 1, 8),
    _VRtrIsisLSPMaxArea_Type()
)
vRtrIsisLSPMaxArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLSPMaxArea.setStatus("deprecated")
_VRtrIsisLSPSysIdLen_Type = Integer32
_VRtrIsisLSPSysIdLen_Object = MibTableColumn
vRtrIsisLSPSysIdLen = _VRtrIsisLSPSysIdLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 7, 1, 9),
    _VRtrIsisLSPSysIdLen_Type()
)
vRtrIsisLSPSysIdLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLSPSysIdLen.setStatus("deprecated")
_VRtrIsisLSPAttributes_Type = Integer32
_VRtrIsisLSPAttributes_Object = MibTableColumn
vRtrIsisLSPAttributes = _VRtrIsisLSPAttributes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 7, 1, 10),
    _VRtrIsisLSPAttributes_Type()
)
vRtrIsisLSPAttributes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLSPAttributes.setStatus("deprecated")
_VRtrIsisLSPUsedLen_Type = Integer32
_VRtrIsisLSPUsedLen_Object = MibTableColumn
vRtrIsisLSPUsedLen = _VRtrIsisLSPUsedLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 7, 1, 11),
    _VRtrIsisLSPUsedLen_Type()
)
vRtrIsisLSPUsedLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLSPUsedLen.setStatus("deprecated")
_VRtrIsisLSPAllocLen_Type = Integer32
_VRtrIsisLSPAllocLen_Object = MibTableColumn
vRtrIsisLSPAllocLen = _VRtrIsisLSPAllocLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 7, 1, 12),
    _VRtrIsisLSPAllocLen_Type()
)
vRtrIsisLSPAllocLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLSPAllocLen.setStatus("deprecated")


class _VRtrIsisLSPBuff_Type(OctetString):
    """Custom type vRtrIsisLSPBuff based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(27, 9190),
    )


_VRtrIsisLSPBuff_Type.__name__ = "OctetString"
_VRtrIsisLSPBuff_Object = MibTableColumn
vRtrIsisLSPBuff = _VRtrIsisLSPBuff_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 7, 1, 13),
    _VRtrIsisLSPBuff_Type()
)
vRtrIsisLSPBuff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLSPBuff.setStatus("deprecated")
_VRtrIsisLSPZeroRLT_Type = TruthValue
_VRtrIsisLSPZeroRLT_Object = MibTableColumn
vRtrIsisLSPZeroRLT = _VRtrIsisLSPZeroRLT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 7, 1, 14),
    _VRtrIsisLSPZeroRLT_Type()
)
vRtrIsisLSPZeroRLT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLSPZeroRLT.setStatus("deprecated")
_VRtrIsisSpfLogTable_Object = MibTable
vRtrIsisSpfLogTable = _VRtrIsisSpfLogTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 8)
)
if mibBuilder.loadTexts:
    vRtrIsisSpfLogTable.setStatus("deprecated")
_VRtrIsisSpfLogEntry_Object = MibTableRow
vRtrIsisSpfLogEntry = _VRtrIsisSpfLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 8, 1)
)
vRtrIsisSpfLogEntry.setIndexNames(
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "TIMETRA-ISIS-MIB", "vRtrIsisSpfTimeStamp"),
)
if mibBuilder.loadTexts:
    vRtrIsisSpfLogEntry.setStatus("deprecated")
_VRtrIsisSpfTimeStamp_Type = TimeStamp
_VRtrIsisSpfTimeStamp_Object = MibTableColumn
vRtrIsisSpfTimeStamp = _VRtrIsisSpfTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 8, 1, 1),
    _VRtrIsisSpfTimeStamp_Type()
)
vRtrIsisSpfTimeStamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIsisSpfTimeStamp.setStatus("deprecated")
_VRtrIsisSpfRunTime_Type = TimeTicks
_VRtrIsisSpfRunTime_Object = MibTableColumn
vRtrIsisSpfRunTime = _VRtrIsisSpfRunTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 8, 1, 2),
    _VRtrIsisSpfRunTime_Type()
)
vRtrIsisSpfRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisSpfRunTime.setStatus("deprecated")
_VRtrIsisSpfL1Nodes_Type = Unsigned32
_VRtrIsisSpfL1Nodes_Object = MibTableColumn
vRtrIsisSpfL1Nodes = _VRtrIsisSpfL1Nodes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 8, 1, 3),
    _VRtrIsisSpfL1Nodes_Type()
)
vRtrIsisSpfL1Nodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisSpfL1Nodes.setStatus("deprecated")
_VRtrIsisSpfL2Nodes_Type = Unsigned32
_VRtrIsisSpfL2Nodes_Object = MibTableColumn
vRtrIsisSpfL2Nodes = _VRtrIsisSpfL2Nodes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 8, 1, 4),
    _VRtrIsisSpfL2Nodes_Type()
)
vRtrIsisSpfL2Nodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisSpfL2Nodes.setStatus("deprecated")
_VRtrIsisSpfEventCount_Type = Unsigned32
_VRtrIsisSpfEventCount_Object = MibTableColumn
vRtrIsisSpfEventCount = _VRtrIsisSpfEventCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 8, 1, 5),
    _VRtrIsisSpfEventCount_Type()
)
vRtrIsisSpfEventCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisSpfEventCount.setStatus("deprecated")


class _VRtrIsisSpfLastTriggerLSPId_Type(OctetString):
    """Custom type vRtrIsisSpfLastTriggerLSPId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_VRtrIsisSpfLastTriggerLSPId_Type.__name__ = "OctetString"
_VRtrIsisSpfLastTriggerLSPId_Object = MibTableColumn
vRtrIsisSpfLastTriggerLSPId = _VRtrIsisSpfLastTriggerLSPId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 8, 1, 6),
    _VRtrIsisSpfLastTriggerLSPId_Type()
)
vRtrIsisSpfLastTriggerLSPId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisSpfLastTriggerLSPId.setStatus("deprecated")


class _VRtrIsisSpfTriggerReason_Type(Bits):
    """Custom type vRtrIsisSpfTriggerReason based on Bits"""
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

_VRtrIsisSpfTriggerReason_Type.__name__ = "Bits"
_VRtrIsisSpfTriggerReason_Object = MibTableColumn
vRtrIsisSpfTriggerReason = _VRtrIsisSpfTriggerReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 8, 1, 7),
    _VRtrIsisSpfTriggerReason_Type()
)
vRtrIsisSpfTriggerReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisSpfTriggerReason.setStatus("deprecated")


class _VRtrIsisSpfType_Type(Integer32):
    """Custom type vRtrIsisSpfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("regular", 0),
          ("lfa", 1))
    )


_VRtrIsisSpfType_Type.__name__ = "Integer32"
_VRtrIsisSpfType_Object = MibTableColumn
vRtrIsisSpfType = _VRtrIsisSpfType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 8, 1, 8),
    _VRtrIsisSpfType_Type()
)
vRtrIsisSpfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisSpfType.setStatus("deprecated")
_VRtrIsisSummaryTable_Object = MibTable
vRtrIsisSummaryTable = _VRtrIsisSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 9)
)
if mibBuilder.loadTexts:
    vRtrIsisSummaryTable.setStatus("deprecated")
_VRtrIsisSummaryEntry_Object = MibTableRow
vRtrIsisSummaryEntry = _VRtrIsisSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 9, 1)
)
vRtrIsisSummaryEntry.setIndexNames(
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "TIMETRA-ISIS-MIB", "vRtrIsisSummPrefix"),
    (0, "TIMETRA-ISIS-MIB", "vRtrIsisSummMask"),
)
if mibBuilder.loadTexts:
    vRtrIsisSummaryEntry.setStatus("deprecated")
_VRtrIsisSummPrefix_Type = IpAddress
_VRtrIsisSummPrefix_Object = MibTableColumn
vRtrIsisSummPrefix = _VRtrIsisSummPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 9, 1, 1),
    _VRtrIsisSummPrefix_Type()
)
vRtrIsisSummPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIsisSummPrefix.setStatus("deprecated")
_VRtrIsisSummMask_Type = IpAddress
_VRtrIsisSummMask_Object = MibTableColumn
vRtrIsisSummMask = _VRtrIsisSummMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 9, 1, 2),
    _VRtrIsisSummMask_Type()
)
vRtrIsisSummMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIsisSummMask.setStatus("deprecated")
_VRtrIsisSummRowStatus_Type = RowStatus
_VRtrIsisSummRowStatus_Object = MibTableColumn
vRtrIsisSummRowStatus = _VRtrIsisSummRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 9, 1, 3),
    _VRtrIsisSummRowStatus_Type()
)
vRtrIsisSummRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisSummRowStatus.setStatus("deprecated")


class _VRtrIsisSummLevel_Type(Integer32):
    """Custom type vRtrIsisSummLevel based on Integer32"""
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


_VRtrIsisSummLevel_Type.__name__ = "Integer32"
_VRtrIsisSummLevel_Object = MibTableColumn
vRtrIsisSummLevel = _VRtrIsisSummLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 9, 1, 4),
    _VRtrIsisSummLevel_Type()
)
vRtrIsisSummLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisSummLevel.setStatus("deprecated")
_VRtrIsisInetRouteTable_Object = MibTable
vRtrIsisInetRouteTable = _VRtrIsisInetRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 10)
)
if mibBuilder.loadTexts:
    vRtrIsisInetRouteTable.setStatus("deprecated")
_VRtrIsisInetRouteEntry_Object = MibTableRow
vRtrIsisInetRouteEntry = _VRtrIsisInetRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 10, 1)
)
vRtrIsisInetRouteEntry.setIndexNames(
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "TIMETRA-ISIS-MIB", "vRtrIsisInetRouteDestType"),
    (0, "TIMETRA-ISIS-MIB", "vRtrIsisInetRouteDest"),
    (0, "TIMETRA-ISIS-MIB", "vRtrIsisInetRoutePrefixLength"),
    (0, "TIMETRA-ISIS-MIB", "vRtrIsisInetRouteNexthopIPType"),
    (0, "TIMETRA-ISIS-MIB", "vRtrIsisInetRouteNexthopIP"),
)
if mibBuilder.loadTexts:
    vRtrIsisInetRouteEntry.setStatus("deprecated")
_VRtrIsisInetRouteDestType_Type = InetAddressType
_VRtrIsisInetRouteDestType_Object = MibTableColumn
vRtrIsisInetRouteDestType = _VRtrIsisInetRouteDestType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 10, 1, 1),
    _VRtrIsisInetRouteDestType_Type()
)
vRtrIsisInetRouteDestType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIsisInetRouteDestType.setStatus("deprecated")


class _VRtrIsisInetRouteDest_Type(InetAddress):
    """Custom type vRtrIsisInetRouteDest based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_VRtrIsisInetRouteDest_Type.__name__ = "InetAddress"
_VRtrIsisInetRouteDest_Object = MibTableColumn
vRtrIsisInetRouteDest = _VRtrIsisInetRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 10, 1, 2),
    _VRtrIsisInetRouteDest_Type()
)
vRtrIsisInetRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIsisInetRouteDest.setStatus("deprecated")
_VRtrIsisInetRoutePrefixLength_Type = InetAddressPrefixLength
_VRtrIsisInetRoutePrefixLength_Object = MibTableColumn
vRtrIsisInetRoutePrefixLength = _VRtrIsisInetRoutePrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 10, 1, 3),
    _VRtrIsisInetRoutePrefixLength_Type()
)
vRtrIsisInetRoutePrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIsisInetRoutePrefixLength.setStatus("deprecated")
_VRtrIsisInetRouteNexthopIPType_Type = InetAddressType
_VRtrIsisInetRouteNexthopIPType_Object = MibTableColumn
vRtrIsisInetRouteNexthopIPType = _VRtrIsisInetRouteNexthopIPType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 10, 1, 4),
    _VRtrIsisInetRouteNexthopIPType_Type()
)
vRtrIsisInetRouteNexthopIPType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIsisInetRouteNexthopIPType.setStatus("deprecated")


class _VRtrIsisInetRouteNexthopIP_Type(InetAddress):
    """Custom type vRtrIsisInetRouteNexthopIP based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_VRtrIsisInetRouteNexthopIP_Type.__name__ = "InetAddress"
_VRtrIsisInetRouteNexthopIP_Object = MibTableColumn
vRtrIsisInetRouteNexthopIP = _VRtrIsisInetRouteNexthopIP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 10, 1, 5),
    _VRtrIsisInetRouteNexthopIP_Type()
)
vRtrIsisInetRouteNexthopIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIsisInetRouteNexthopIP.setStatus("deprecated")


class _VRtrIsisInetRouteLevel_Type(Integer32):
    """Custom type vRtrIsisInetRouteLevel based on Integer32"""
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


_VRtrIsisInetRouteLevel_Type.__name__ = "Integer32"
_VRtrIsisInetRouteLevel_Object = MibTableColumn
vRtrIsisInetRouteLevel = _VRtrIsisInetRouteLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 10, 1, 6),
    _VRtrIsisInetRouteLevel_Type()
)
vRtrIsisInetRouteLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisInetRouteLevel.setStatus("deprecated")
_VRtrIsisInetRouteSpfRunNumber_Type = Counter32
_VRtrIsisInetRouteSpfRunNumber_Object = MibTableColumn
vRtrIsisInetRouteSpfRunNumber = _VRtrIsisInetRouteSpfRunNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 10, 1, 7),
    _VRtrIsisInetRouteSpfRunNumber_Type()
)
vRtrIsisInetRouteSpfRunNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisInetRouteSpfRunNumber.setStatus("deprecated")
_VRtrIsisInetRouteMetric_Type = Unsigned32
_VRtrIsisInetRouteMetric_Object = MibTableColumn
vRtrIsisInetRouteMetric = _VRtrIsisInetRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 10, 1, 8),
    _VRtrIsisInetRouteMetric_Type()
)
vRtrIsisInetRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisInetRouteMetric.setStatus("deprecated")


class _VRtrIsisInetRouteType_Type(Integer32):
    """Custom type vRtrIsisInetRouteType based on Integer32"""
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


_VRtrIsisInetRouteType_Type.__name__ = "Integer32"
_VRtrIsisInetRouteType_Object = MibTableColumn
vRtrIsisInetRouteType = _VRtrIsisInetRouteType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 10, 1, 9),
    _VRtrIsisInetRouteType_Type()
)
vRtrIsisInetRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisInetRouteType.setStatus("deprecated")
_VRtrIsisInetRouteNHopSysID_Type = SystemID
_VRtrIsisInetRouteNHopSysID_Object = MibTableColumn
vRtrIsisInetRouteNHopSysID = _VRtrIsisInetRouteNHopSysID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 10, 1, 10),
    _VRtrIsisInetRouteNHopSysID_Type()
)
vRtrIsisInetRouteNHopSysID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisInetRouteNHopSysID.setStatus("deprecated")
_VRtrIsisInetSummaryTable_Object = MibTable
vRtrIsisInetSummaryTable = _VRtrIsisInetSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 11)
)
if mibBuilder.loadTexts:
    vRtrIsisInetSummaryTable.setStatus("deprecated")
_VRtrIsisInetSummaryEntry_Object = MibTableRow
vRtrIsisInetSummaryEntry = _VRtrIsisInetSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 11, 1)
)
vRtrIsisInetSummaryEntry.setIndexNames(
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "TIMETRA-ISIS-MIB", "vRtrIsisInetSummPrefixType"),
    (0, "TIMETRA-ISIS-MIB", "vRtrIsisInetSummPrefix"),
    (0, "TIMETRA-ISIS-MIB", "vRtrIsisInetSummPrefixLength"),
)
if mibBuilder.loadTexts:
    vRtrIsisInetSummaryEntry.setStatus("deprecated")
_VRtrIsisInetSummPrefixType_Type = InetAddressType
_VRtrIsisInetSummPrefixType_Object = MibTableColumn
vRtrIsisInetSummPrefixType = _VRtrIsisInetSummPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 11, 1, 1),
    _VRtrIsisInetSummPrefixType_Type()
)
vRtrIsisInetSummPrefixType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIsisInetSummPrefixType.setStatus("deprecated")


class _VRtrIsisInetSummPrefix_Type(InetAddress):
    """Custom type vRtrIsisInetSummPrefix based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_VRtrIsisInetSummPrefix_Type.__name__ = "InetAddress"
_VRtrIsisInetSummPrefix_Object = MibTableColumn
vRtrIsisInetSummPrefix = _VRtrIsisInetSummPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 11, 1, 2),
    _VRtrIsisInetSummPrefix_Type()
)
vRtrIsisInetSummPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIsisInetSummPrefix.setStatus("deprecated")
_VRtrIsisInetSummPrefixLength_Type = InetAddressPrefixLength
_VRtrIsisInetSummPrefixLength_Object = MibTableColumn
vRtrIsisInetSummPrefixLength = _VRtrIsisInetSummPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 11, 1, 3),
    _VRtrIsisInetSummPrefixLength_Type()
)
vRtrIsisInetSummPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIsisInetSummPrefixLength.setStatus("deprecated")
_VRtrIsisInetSummRowStatus_Type = RowStatus
_VRtrIsisInetSummRowStatus_Object = MibTableColumn
vRtrIsisInetSummRowStatus = _VRtrIsisInetSummRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 11, 1, 4),
    _VRtrIsisInetSummRowStatus_Type()
)
vRtrIsisInetSummRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisInetSummRowStatus.setStatus("deprecated")


class _VRtrIsisInetSummLevel_Type(Integer32):
    """Custom type vRtrIsisInetSummLevel based on Integer32"""
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


_VRtrIsisInetSummLevel_Type.__name__ = "Integer32"
_VRtrIsisInetSummLevel_Object = MibTableColumn
vRtrIsisInetSummLevel = _VRtrIsisInetSummLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 11, 1, 5),
    _VRtrIsisInetSummLevel_Type()
)
vRtrIsisInetSummLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisInetSummLevel.setStatus("deprecated")


class _VRtrIsisInetSummRouteTag_Type(Unsigned32):
    """Custom type vRtrIsisInetSummRouteTag based on Unsigned32"""
    defaultValue = 0


_VRtrIsisInetSummRouteTag_Type.__name__ = "Unsigned32"
_VRtrIsisInetSummRouteTag_Object = MibTableColumn
vRtrIsisInetSummRouteTag = _VRtrIsisInetSummRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 11, 1, 6),
    _VRtrIsisInetSummRouteTag_Type()
)
vRtrIsisInetSummRouteTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisInetSummRouteTag.setStatus("deprecated")
_VRtrIsisInetMtRouteTable_Object = MibTable
vRtrIsisInetMtRouteTable = _VRtrIsisInetMtRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 12)
)
if mibBuilder.loadTexts:
    vRtrIsisInetMtRouteTable.setStatus("deprecated")
_VRtrIsisInetMtRouteEntry_Object = MibTableRow
vRtrIsisInetMtRouteEntry = _VRtrIsisInetMtRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 12, 1)
)
vRtrIsisInetMtRouteEntry.setIndexNames(
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "TIMETRA-ISIS-MIB", "vRtrIsisInetMtRouteMtId"),
    (0, "TIMETRA-ISIS-MIB", "vRtrIsisInetMtRouteDestType"),
    (0, "TIMETRA-ISIS-MIB", "vRtrIsisInetMtRouteDest"),
    (0, "TIMETRA-ISIS-MIB", "vRtrIsisInetMtRoutePrefixLength"),
    (0, "TIMETRA-ISIS-MIB", "vRtrIsisInetMtRouteNexthopIPType"),
    (0, "TIMETRA-ISIS-MIB", "vRtrIsisInetMtRouteNexthopIP"),
)
if mibBuilder.loadTexts:
    vRtrIsisInetMtRouteEntry.setStatus("deprecated")
_VRtrIsisInetMtRouteMtId_Type = Unsigned32
_VRtrIsisInetMtRouteMtId_Object = MibTableColumn
vRtrIsisInetMtRouteMtId = _VRtrIsisInetMtRouteMtId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 12, 1, 1),
    _VRtrIsisInetMtRouteMtId_Type()
)
vRtrIsisInetMtRouteMtId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIsisInetMtRouteMtId.setStatus("deprecated")
_VRtrIsisInetMtRouteDestType_Type = InetAddressType
_VRtrIsisInetMtRouteDestType_Object = MibTableColumn
vRtrIsisInetMtRouteDestType = _VRtrIsisInetMtRouteDestType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 12, 1, 2),
    _VRtrIsisInetMtRouteDestType_Type()
)
vRtrIsisInetMtRouteDestType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIsisInetMtRouteDestType.setStatus("deprecated")


class _VRtrIsisInetMtRouteDest_Type(InetAddress):
    """Custom type vRtrIsisInetMtRouteDest based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_VRtrIsisInetMtRouteDest_Type.__name__ = "InetAddress"
_VRtrIsisInetMtRouteDest_Object = MibTableColumn
vRtrIsisInetMtRouteDest = _VRtrIsisInetMtRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 12, 1, 3),
    _VRtrIsisInetMtRouteDest_Type()
)
vRtrIsisInetMtRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIsisInetMtRouteDest.setStatus("deprecated")
_VRtrIsisInetMtRoutePrefixLength_Type = InetAddressPrefixLength
_VRtrIsisInetMtRoutePrefixLength_Object = MibTableColumn
vRtrIsisInetMtRoutePrefixLength = _VRtrIsisInetMtRoutePrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 12, 1, 4),
    _VRtrIsisInetMtRoutePrefixLength_Type()
)
vRtrIsisInetMtRoutePrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIsisInetMtRoutePrefixLength.setStatus("deprecated")
_VRtrIsisInetMtRouteNexthopIPType_Type = InetAddressType
_VRtrIsisInetMtRouteNexthopIPType_Object = MibTableColumn
vRtrIsisInetMtRouteNexthopIPType = _VRtrIsisInetMtRouteNexthopIPType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 12, 1, 5),
    _VRtrIsisInetMtRouteNexthopIPType_Type()
)
vRtrIsisInetMtRouteNexthopIPType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIsisInetMtRouteNexthopIPType.setStatus("deprecated")


class _VRtrIsisInetMtRouteNexthopIP_Type(InetAddress):
    """Custom type vRtrIsisInetMtRouteNexthopIP based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_VRtrIsisInetMtRouteNexthopIP_Type.__name__ = "InetAddress"
_VRtrIsisInetMtRouteNexthopIP_Object = MibTableColumn
vRtrIsisInetMtRouteNexthopIP = _VRtrIsisInetMtRouteNexthopIP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 12, 1, 6),
    _VRtrIsisInetMtRouteNexthopIP_Type()
)
vRtrIsisInetMtRouteNexthopIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIsisInetMtRouteNexthopIP.setStatus("deprecated")


class _VRtrIsisInetMtRouteLevel_Type(Integer32):
    """Custom type vRtrIsisInetMtRouteLevel based on Integer32"""
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


_VRtrIsisInetMtRouteLevel_Type.__name__ = "Integer32"
_VRtrIsisInetMtRouteLevel_Object = MibTableColumn
vRtrIsisInetMtRouteLevel = _VRtrIsisInetMtRouteLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 12, 1, 7),
    _VRtrIsisInetMtRouteLevel_Type()
)
vRtrIsisInetMtRouteLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisInetMtRouteLevel.setStatus("deprecated")
_VRtrIsisInetMtRouteSpfRunNumber_Type = Counter32
_VRtrIsisInetMtRouteSpfRunNumber_Object = MibTableColumn
vRtrIsisInetMtRouteSpfRunNumber = _VRtrIsisInetMtRouteSpfRunNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 12, 1, 8),
    _VRtrIsisInetMtRouteSpfRunNumber_Type()
)
vRtrIsisInetMtRouteSpfRunNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisInetMtRouteSpfRunNumber.setStatus("deprecated")
_VRtrIsisInetMtRouteMetric_Type = Unsigned32
_VRtrIsisInetMtRouteMetric_Object = MibTableColumn
vRtrIsisInetMtRouteMetric = _VRtrIsisInetMtRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 12, 1, 9),
    _VRtrIsisInetMtRouteMetric_Type()
)
vRtrIsisInetMtRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisInetMtRouteMetric.setStatus("deprecated")


class _VRtrIsisInetMtRouteType_Type(Integer32):
    """Custom type vRtrIsisInetMtRouteType based on Integer32"""
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


_VRtrIsisInetMtRouteType_Type.__name__ = "Integer32"
_VRtrIsisInetMtRouteType_Object = MibTableColumn
vRtrIsisInetMtRouteType = _VRtrIsisInetMtRouteType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 12, 1, 10),
    _VRtrIsisInetMtRouteType_Type()
)
vRtrIsisInetMtRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisInetMtRouteType.setStatus("deprecated")
_VRtrIsisInetMtRouteNHopSysID_Type = SystemID
_VRtrIsisInetMtRouteNHopSysID_Object = MibTableColumn
vRtrIsisInetMtRouteNHopSysID = _VRtrIsisInetMtRouteNHopSysID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 12, 1, 11),
    _VRtrIsisInetMtRouteNHopSysID_Type()
)
vRtrIsisInetMtRouteNHopSysID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisInetMtRouteNHopSysID.setStatus("deprecated")


class _VRtrIsisInetMtRouteTag_Type(Unsigned32):
    """Custom type vRtrIsisInetMtRouteTag based on Unsigned32"""
    defaultValue = 0


_VRtrIsisInetMtRouteTag_Type.__name__ = "Unsigned32"
_VRtrIsisInetMtRouteTag_Object = MibTableColumn
vRtrIsisInetMtRouteTag = _VRtrIsisInetMtRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 12, 1, 12),
    _VRtrIsisInetMtRouteTag_Type()
)
vRtrIsisInetMtRouteTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisInetMtRouteTag.setStatus("deprecated")


class _VRtrIsisInetMtRouteBkupFlags_Type(Integer32):
    """Custom type vRtrIsisInetMtRouteBkupFlags based on Integer32"""
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


_VRtrIsisInetMtRouteBkupFlags_Type.__name__ = "Integer32"
_VRtrIsisInetMtRouteBkupFlags_Object = MibTableColumn
vRtrIsisInetMtRouteBkupFlags = _VRtrIsisInetMtRouteBkupFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 12, 1, 13),
    _VRtrIsisInetMtRouteBkupFlags_Type()
)
vRtrIsisInetMtRouteBkupFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisInetMtRouteBkupFlags.setStatus("deprecated")


class _VRtrIsisInetMtRouteBkupNextHopTy_Type(Integer32):
    """Custom type vRtrIsisInetMtRouteBkupNextHopTy based on Integer32"""
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


_VRtrIsisInetMtRouteBkupNextHopTy_Type.__name__ = "Integer32"
_VRtrIsisInetMtRouteBkupNextHopTy_Object = MibTableColumn
vRtrIsisInetMtRouteBkupNextHopTy = _VRtrIsisInetMtRouteBkupNextHopTy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 12, 1, 14),
    _VRtrIsisInetMtRouteBkupNextHopTy_Type()
)
vRtrIsisInetMtRouteBkupNextHopTy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisInetMtRouteBkupNextHopTy.setStatus("deprecated")
_VRtrIsisInetMtRouteBkupNextHop_Type = InetAddress
_VRtrIsisInetMtRouteBkupNextHop_Object = MibTableColumn
vRtrIsisInetMtRouteBkupNextHop = _VRtrIsisInetMtRouteBkupNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 12, 1, 15),
    _VRtrIsisInetMtRouteBkupNextHop_Type()
)
vRtrIsisInetMtRouteBkupNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisInetMtRouteBkupNextHop.setStatus("deprecated")
_VRtrIsisInetMtRouteBkupMetric_Type = Unsigned32
_VRtrIsisInetMtRouteBkupMetric_Object = MibTableColumn
vRtrIsisInetMtRouteBkupMetric = _VRtrIsisInetMtRouteBkupMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 12, 1, 16),
    _VRtrIsisInetMtRouteBkupMetric_Type()
)
vRtrIsisInetMtRouteBkupMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisInetMtRouteBkupMetric.setStatus("deprecated")
_VRtrIsisRouteNextHopType_Type = TmnxInetCidrNextHopType
_VRtrIsisRouteNextHopType_Object = MibTableColumn
vRtrIsisRouteNextHopType = _VRtrIsisRouteNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 12, 1, 17),
    _VRtrIsisRouteNextHopType_Type()
)
vRtrIsisRouteNextHopType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisRouteNextHopType.setStatus("deprecated")
_VRtrIsisNextHopOwner_Type = TmnxInetCidrNextHopOwner
_VRtrIsisNextHopOwner_Object = MibTableColumn
vRtrIsisNextHopOwner = _VRtrIsisNextHopOwner_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 12, 1, 18),
    _VRtrIsisNextHopOwner_Type()
)
vRtrIsisNextHopOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisNextHopOwner.setStatus("deprecated")
_VRtrIsisRouteNHOwnerAuxInfo_Type = Unsigned32
_VRtrIsisRouteNHOwnerAuxInfo_Object = MibTableColumn
vRtrIsisRouteNHOwnerAuxInfo = _VRtrIsisRouteNHOwnerAuxInfo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 12, 1, 19),
    _VRtrIsisRouteNHOwnerAuxInfo_Type()
)
vRtrIsisRouteNHOwnerAuxInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisRouteNHOwnerAuxInfo.setStatus("deprecated")
_VRtrIsisRouteBkupNHType_Type = TmnxInetCidrNextHopType
_VRtrIsisRouteBkupNHType_Object = MibTableColumn
vRtrIsisRouteBkupNHType = _VRtrIsisRouteBkupNHType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 12, 1, 20),
    _VRtrIsisRouteBkupNHType_Type()
)
vRtrIsisRouteBkupNHType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisRouteBkupNHType.setStatus("deprecated")
_VRtrIsisRouteBkupNHOwner_Type = TmnxInetCidrNextHopOwner
_VRtrIsisRouteBkupNHOwner_Object = MibTableColumn
vRtrIsisRouteBkupNHOwner = _VRtrIsisRouteBkupNHOwner_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 12, 1, 21),
    _VRtrIsisRouteBkupNHOwner_Type()
)
vRtrIsisRouteBkupNHOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisRouteBkupNHOwner.setStatus("deprecated")
_VRtrIsisRouteBkupNHOwnAxInfo_Type = Unsigned32
_VRtrIsisRouteBkupNHOwnAxInfo_Object = MibTableColumn
vRtrIsisRouteBkupNHOwnAxInfo = _VRtrIsisRouteBkupNHOwnAxInfo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 12, 1, 22),
    _VRtrIsisRouteBkupNHOwnAxInfo_Type()
)
vRtrIsisRouteBkupNHOwnAxInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisRouteBkupNHOwnAxInfo.setStatus("deprecated")
_VRtrIsisMtPathTable_Object = MibTable
vRtrIsisMtPathTable = _VRtrIsisMtPathTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 13)
)
if mibBuilder.loadTexts:
    vRtrIsisMtPathTable.setStatus("deprecated")
_VRtrIsisMtPathEntry_Object = MibTableRow
vRtrIsisMtPathEntry = _VRtrIsisMtPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 13, 1)
)
vRtrIsisMtPathEntry.setIndexNames(
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "TIMETRA-ISIS-MIB", "vRtrIsisLevel"),
    (0, "TIMETRA-ISIS-MIB", "vRtrIsisMtPathMtID"),
    (0, "TIMETRA-ISIS-MIB", "vRtrIsisMtPathID"),
    (0, "TIMETRA-ISIS-MIB", "vRtrIsisMtPathIfIndex"),
    (0, "TIMETRA-ISIS-MIB", "vRtrIsisMtPathNHopSysID"),
)
if mibBuilder.loadTexts:
    vRtrIsisMtPathEntry.setStatus("deprecated")
_VRtrIsisMtPathMtID_Type = Unsigned32
_VRtrIsisMtPathMtID_Object = MibTableColumn
vRtrIsisMtPathMtID = _VRtrIsisMtPathMtID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 13, 1, 1),
    _VRtrIsisMtPathMtID_Type()
)
vRtrIsisMtPathMtID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIsisMtPathMtID.setStatus("deprecated")


class _VRtrIsisMtPathID_Type(OctetString):
    """Custom type vRtrIsisMtPathID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )
    fixed_length = 7


_VRtrIsisMtPathID_Type.__name__ = "OctetString"
_VRtrIsisMtPathID_Object = MibTableColumn
vRtrIsisMtPathID = _VRtrIsisMtPathID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 13, 1, 2),
    _VRtrIsisMtPathID_Type()
)
vRtrIsisMtPathID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIsisMtPathID.setStatus("deprecated")
_VRtrIsisMtPathIfIndex_Type = InterfaceIndex
_VRtrIsisMtPathIfIndex_Object = MibTableColumn
vRtrIsisMtPathIfIndex = _VRtrIsisMtPathIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 13, 1, 3),
    _VRtrIsisMtPathIfIndex_Type()
)
vRtrIsisMtPathIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIsisMtPathIfIndex.setStatus("deprecated")
_VRtrIsisMtPathNHopSysID_Type = SystemID
_VRtrIsisMtPathNHopSysID_Object = MibTableColumn
vRtrIsisMtPathNHopSysID = _VRtrIsisMtPathNHopSysID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 13, 1, 4),
    _VRtrIsisMtPathNHopSysID_Type()
)
vRtrIsisMtPathNHopSysID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIsisMtPathNHopSysID.setStatus("deprecated")
_VRtrIsisMtPathMetric_Type = Unsigned32
_VRtrIsisMtPathMetric_Object = MibTableColumn
vRtrIsisMtPathMetric = _VRtrIsisMtPathMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 13, 1, 5),
    _VRtrIsisMtPathMetric_Type()
)
vRtrIsisMtPathMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisMtPathMetric.setStatus("deprecated")
_VRtrIsisMtPathSNPA_Type = SNPAAddress
_VRtrIsisMtPathSNPA_Object = MibTableColumn
vRtrIsisMtPathSNPA = _VRtrIsisMtPathSNPA_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 13, 1, 6),
    _VRtrIsisMtPathSNPA_Type()
)
vRtrIsisMtPathSNPA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisMtPathSNPA.setStatus("deprecated")
_VRtrIsisMtPathLfaIfIndex_Type = InterfaceIndex
_VRtrIsisMtPathLfaIfIndex_Object = MibTableColumn
vRtrIsisMtPathLfaIfIndex = _VRtrIsisMtPathLfaIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 13, 1, 7),
    _VRtrIsisMtPathLfaIfIndex_Type()
)
vRtrIsisMtPathLfaIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisMtPathLfaIfIndex.setStatus("deprecated")
_VRtrIsisMtPathLfaNHop_Type = SystemID
_VRtrIsisMtPathLfaNHop_Object = MibTableColumn
vRtrIsisMtPathLfaNHop = _VRtrIsisMtPathLfaNHop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 13, 1, 8),
    _VRtrIsisMtPathLfaNHop_Type()
)
vRtrIsisMtPathLfaNHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisMtPathLfaNHop.setStatus("deprecated")
_VRtrIsisMtPathLfaMetric_Type = Unsigned32
_VRtrIsisMtPathLfaMetric_Object = MibTableColumn
vRtrIsisMtPathLfaMetric = _VRtrIsisMtPathLfaMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 13, 1, 9),
    _VRtrIsisMtPathLfaMetric_Type()
)
vRtrIsisMtPathLfaMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisMtPathLfaMetric.setStatus("deprecated")


class _VRtrIsisMtPathLfaType_Type(Integer32):
    """Custom type vRtrIsisMtPathLfaType based on Integer32"""
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


_VRtrIsisMtPathLfaType_Type.__name__ = "Integer32"
_VRtrIsisMtPathLfaType_Object = MibTableColumn
vRtrIsisMtPathLfaType = _VRtrIsisMtPathLfaType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 13, 1, 10),
    _VRtrIsisMtPathLfaType_Type()
)
vRtrIsisMtPathLfaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisMtPathLfaType.setStatus("deprecated")


class _VRtrIsisMtPathRouteType_Type(Integer32):
    """Custom type vRtrIsisMtPathRouteType based on Integer32"""
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


_VRtrIsisMtPathRouteType_Type.__name__ = "Integer32"
_VRtrIsisMtPathRouteType_Object = MibTableColumn
vRtrIsisMtPathRouteType = _VRtrIsisMtPathRouteType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 13, 1, 11),
    _VRtrIsisMtPathRouteType_Type()
)
vRtrIsisMtPathRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisMtPathRouteType.setStatus("deprecated")
_VRtrIsisLfaTable_Object = MibTable
vRtrIsisLfaTable = _VRtrIsisLfaTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 14)
)
if mibBuilder.loadTexts:
    vRtrIsisLfaTable.setStatus("deprecated")
_VRtrIsisLfaEntry_Object = MibTableRow
vRtrIsisLfaEntry = _VRtrIsisLfaEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 14, 1)
)
vRtrIsisLfaEntry.setIndexNames(
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "TIMETRA-ISIS-MIB", "vRtrIsisLevel"),
    (0, "TIMETRA-ISIS-MIB", "vRtrIsisLfaFamilyCoverage"),
)
if mibBuilder.loadTexts:
    vRtrIsisLfaEntry.setStatus("deprecated")


class _VRtrIsisLfaFamilyCoverage_Type(Integer32):
    """Custom type vRtrIsisLfaFamilyCoverage based on Integer32"""
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


_VRtrIsisLfaFamilyCoverage_Type.__name__ = "Integer32"
_VRtrIsisLfaFamilyCoverage_Object = MibTableColumn
vRtrIsisLfaFamilyCoverage = _VRtrIsisLfaFamilyCoverage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 14, 1, 1),
    _VRtrIsisLfaFamilyCoverage_Type()
)
vRtrIsisLfaFamilyCoverage.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIsisLfaFamilyCoverage.setStatus("deprecated")
_VRtrIsisLfaNodesCovered_Type = Unsigned32
_VRtrIsisLfaNodesCovered_Object = MibTableColumn
vRtrIsisLfaNodesCovered = _VRtrIsisLfaNodesCovered_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 14, 1, 2),
    _VRtrIsisLfaNodesCovered_Type()
)
vRtrIsisLfaNodesCovered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLfaNodesCovered.setStatus("deprecated")
_VRtrIsisLfaTotalNodes_Type = Unsigned32
_VRtrIsisLfaTotalNodes_Object = MibTableColumn
vRtrIsisLfaTotalNodes = _VRtrIsisLfaTotalNodes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 14, 1, 3),
    _VRtrIsisLfaTotalNodes_Type()
)
vRtrIsisLfaTotalNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLfaTotalNodes.setStatus("deprecated")


class _VRtrIsisLfaNodeCoverage_Type(Unsigned32):
    """Custom type vRtrIsisLfaNodeCoverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_VRtrIsisLfaNodeCoverage_Type.__name__ = "Unsigned32"
_VRtrIsisLfaNodeCoverage_Object = MibTableColumn
vRtrIsisLfaNodeCoverage = _VRtrIsisLfaNodeCoverage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 14, 1, 4),
    _VRtrIsisLfaNodeCoverage_Type()
)
vRtrIsisLfaNodeCoverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLfaNodeCoverage.setStatus("deprecated")
if mibBuilder.loadTexts:
    vRtrIsisLfaNodeCoverage.setUnits("hundredths of a percent")
_VRtrIsisLfaIpv4NodesCovered_Type = Unsigned32
_VRtrIsisLfaIpv4NodesCovered_Object = MibTableColumn
vRtrIsisLfaIpv4NodesCovered = _VRtrIsisLfaIpv4NodesCovered_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 14, 1, 5),
    _VRtrIsisLfaIpv4NodesCovered_Type()
)
vRtrIsisLfaIpv4NodesCovered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLfaIpv4NodesCovered.setStatus("deprecated")
_VRtrIsisLfaIpv4TotalNodes_Type = Unsigned32
_VRtrIsisLfaIpv4TotalNodes_Object = MibTableColumn
vRtrIsisLfaIpv4TotalNodes = _VRtrIsisLfaIpv4TotalNodes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 14, 1, 6),
    _VRtrIsisLfaIpv4TotalNodes_Type()
)
vRtrIsisLfaIpv4TotalNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLfaIpv4TotalNodes.setStatus("deprecated")


class _VRtrIsisLfaIpv4Coverage_Type(Unsigned32):
    """Custom type vRtrIsisLfaIpv4Coverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_VRtrIsisLfaIpv4Coverage_Type.__name__ = "Unsigned32"
_VRtrIsisLfaIpv4Coverage_Object = MibTableColumn
vRtrIsisLfaIpv4Coverage = _VRtrIsisLfaIpv4Coverage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 14, 1, 7),
    _VRtrIsisLfaIpv4Coverage_Type()
)
vRtrIsisLfaIpv4Coverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLfaIpv4Coverage.setStatus("deprecated")
if mibBuilder.loadTexts:
    vRtrIsisLfaIpv4Coverage.setUnits("hundredths of a percent")
_VRtrIsisLfaIpv6NodesCovered_Type = Unsigned32
_VRtrIsisLfaIpv6NodesCovered_Object = MibTableColumn
vRtrIsisLfaIpv6NodesCovered = _VRtrIsisLfaIpv6NodesCovered_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 14, 1, 8),
    _VRtrIsisLfaIpv6NodesCovered_Type()
)
vRtrIsisLfaIpv6NodesCovered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLfaIpv6NodesCovered.setStatus("deprecated")
_VRtrIsisLfaIpv6TotalNodes_Type = Unsigned32
_VRtrIsisLfaIpv6TotalNodes_Object = MibTableColumn
vRtrIsisLfaIpv6TotalNodes = _VRtrIsisLfaIpv6TotalNodes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 14, 1, 9),
    _VRtrIsisLfaIpv6TotalNodes_Type()
)
vRtrIsisLfaIpv6TotalNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLfaIpv6TotalNodes.setStatus("deprecated")


class _VRtrIsisLfaIpv6Coverage_Type(Unsigned32):
    """Custom type vRtrIsisLfaIpv6Coverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_VRtrIsisLfaIpv6Coverage_Type.__name__ = "Unsigned32"
_VRtrIsisLfaIpv6Coverage_Object = MibTableColumn
vRtrIsisLfaIpv6Coverage = _VRtrIsisLfaIpv6Coverage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 14, 1, 10),
    _VRtrIsisLfaIpv6Coverage_Type()
)
vRtrIsisLfaIpv6Coverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLfaIpv6Coverage.setStatus("deprecated")
if mibBuilder.loadTexts:
    vRtrIsisLfaIpv6Coverage.setUnits("hundredths of a percent")
_VRtrSpbEctFidTableLastChanged_Type = TimeStamp
_VRtrSpbEctFidTableLastChanged_Object = MibScalar
vRtrSpbEctFidTableLastChanged = _VRtrSpbEctFidTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 15),
    _VRtrSpbEctFidTableLastChanged_Type()
)
vRtrSpbEctFidTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSpbEctFidTableLastChanged.setStatus("current")
_VRtrSpbEctFidTable_Object = MibTable
vRtrSpbEctFidTable = _VRtrSpbEctFidTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 16)
)
if mibBuilder.loadTexts:
    vRtrSpbEctFidTable.setStatus("current")
_VRtrSpbEctFidEntry_Object = MibTableRow
vRtrSpbEctFidEntry = _VRtrSpbEctFidEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 16, 1)
)
vRtrSpbEctFidEntry.setIndexNames(
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "TIMETRA-ISIS-MIB", "vRtrIsisLevel"),
    (0, "TIMETRA-ISIS-MIB", "vRtrSpbEctFid"),
)
if mibBuilder.loadTexts:
    vRtrSpbEctFidEntry.setStatus("current")
_VRtrSpbEctFid_Type = TmnxSpbFid
_VRtrSpbEctFid_Object = MibTableColumn
vRtrSpbEctFid = _VRtrSpbEctFid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 16, 1, 1),
    _VRtrSpbEctFid_Type()
)
vRtrSpbEctFid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrSpbEctFid.setStatus("current")
_VRtrSpbEctFidLastChanged_Type = TimeStamp
_VRtrSpbEctFidLastChanged_Object = MibTableColumn
vRtrSpbEctFidLastChanged = _VRtrSpbEctFidLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 16, 1, 2),
    _VRtrSpbEctFidLastChanged_Type()
)
vRtrSpbEctFidLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSpbEctFidLastChanged.setStatus("current")


class _VRtrSpbEctFidAlgorithm_Type(Integer32):
    """Custom type vRtrSpbEctFidAlgorithm based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("lowPathId", 0),
          ("highPathId", 1))
    )


_VRtrSpbEctFidAlgorithm_Type.__name__ = "Integer32"
_VRtrSpbEctFidAlgorithm_Object = MibTableColumn
vRtrSpbEctFidAlgorithm = _VRtrSpbEctFidAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 16, 1, 3),
    _VRtrSpbEctFidAlgorithm_Type()
)
vRtrSpbEctFidAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrSpbEctFidAlgorithm.setStatus("current")
_VRtrSpbPathTable_Object = MibTable
vRtrSpbPathTable = _VRtrSpbPathTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 17)
)
if mibBuilder.loadTexts:
    vRtrSpbPathTable.setStatus("current")
_VRtrSpbPathEntry_Object = MibTableRow
vRtrSpbPathEntry = _VRtrSpbPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 17, 1)
)
vRtrSpbPathEntry.setIndexNames(
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "TIMETRA-ISIS-MIB", "vRtrIsisLevel"),
    (0, "TIMETRA-ISIS-MIB", "vRtrSpbPathFwdTree"),
    (0, "TIMETRA-ISIS-MIB", "vRtrSpbEctFidAlgorithm"),
    (0, "TIMETRA-ISIS-MIB", "vRtrIsisPathID"),
)
if mibBuilder.loadTexts:
    vRtrSpbPathEntry.setStatus("current")


class _VRtrSpbPathFwdTree_Type(Integer32):
    """Custom type vRtrSpbPathFwdTree based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unicast", 1),
          ("multicast", 2))
    )


_VRtrSpbPathFwdTree_Type.__name__ = "Integer32"
_VRtrSpbPathFwdTree_Object = MibTableColumn
vRtrSpbPathFwdTree = _VRtrSpbPathFwdTree_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 17, 1, 1),
    _VRtrSpbPathFwdTree_Type()
)
vRtrSpbPathFwdTree.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrSpbPathFwdTree.setStatus("current")
_VRtrSpbPathIfIndex_Type = InterfaceIndex
_VRtrSpbPathIfIndex_Object = MibTableColumn
vRtrSpbPathIfIndex = _VRtrSpbPathIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 17, 1, 2),
    _VRtrSpbPathIfIndex_Type()
)
vRtrSpbPathIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSpbPathIfIndex.setStatus("current")
_VRtrSpbPathNHopSysID_Type = SystemID
_VRtrSpbPathNHopSysID_Object = MibTableColumn
vRtrSpbPathNHopSysID = _VRtrSpbPathNHopSysID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 17, 1, 3),
    _VRtrSpbPathNHopSysID_Type()
)
vRtrSpbPathNHopSysID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSpbPathNHopSysID.setStatus("current")
_VRtrSpbPathMetric_Type = Unsigned32
_VRtrSpbPathMetric_Object = MibTableColumn
vRtrSpbPathMetric = _VRtrSpbPathMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 17, 1, 4),
    _VRtrSpbPathMetric_Type()
)
vRtrSpbPathMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSpbPathMetric.setStatus("current")
_VRtrSpbPathSNPA_Type = SNPAAddress
_VRtrSpbPathSNPA_Object = MibTableColumn
vRtrSpbPathSNPA = _VRtrSpbPathSNPA_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 17, 1, 5),
    _VRtrSpbPathSNPA_Type()
)
vRtrSpbPathSNPA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSpbPathSNPA.setStatus("current")
_VRtrSpbRouteMacTable_Object = MibTable
vRtrSpbRouteMacTable = _VRtrSpbRouteMacTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 18)
)
if mibBuilder.loadTexts:
    vRtrSpbRouteMacTable.setStatus("current")
_VRtrSpbRouteMacEntry_Object = MibTableRow
vRtrSpbRouteMacEntry = _VRtrSpbRouteMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 18, 1)
)
vRtrSpbRouteMacEntry.setIndexNames(
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "TIMETRA-ISIS-MIB", "vRtrSpbPathFwdTree"),
    (0, "TIMETRA-ISIS-MIB", "vRtrSpbEctFid"),
    (0, "TIMETRA-ISIS-MIB", "vRtrSpbRouteMacDestMac"),
)
if mibBuilder.loadTexts:
    vRtrSpbRouteMacEntry.setStatus("current")
_VRtrSpbRouteMacDestMac_Type = MacAddress
_VRtrSpbRouteMacDestMac_Object = MibTableColumn
vRtrSpbRouteMacDestMac = _VRtrSpbRouteMacDestMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 18, 1, 1),
    _VRtrSpbRouteMacDestMac_Type()
)
vRtrSpbRouteMacDestMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrSpbRouteMacDestMac.setStatus("current")
_VRtrSpbRouteMacIfIndex_Type = InterfaceIndex
_VRtrSpbRouteMacIfIndex_Object = MibTableColumn
vRtrSpbRouteMacIfIndex = _VRtrSpbRouteMacIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 18, 1, 2),
    _VRtrSpbRouteMacIfIndex_Type()
)
vRtrSpbRouteMacIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSpbRouteMacIfIndex.setStatus("current")
_VRtrSpbRouteMacSpfRunNumber_Type = Counter32
_VRtrSpbRouteMacSpfRunNumber_Object = MibTableColumn
vRtrSpbRouteMacSpfRunNumber = _VRtrSpbRouteMacSpfRunNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 18, 1, 3),
    _VRtrSpbRouteMacSpfRunNumber_Type()
)
vRtrSpbRouteMacSpfRunNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSpbRouteMacSpfRunNumber.setStatus("current")
_VRtrSpbRouteMacMetric_Type = Unsigned32
_VRtrSpbRouteMacMetric_Object = MibTableColumn
vRtrSpbRouteMacMetric = _VRtrSpbRouteMacMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 18, 1, 4),
    _VRtrSpbRouteMacMetric_Type()
)
vRtrSpbRouteMacMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSpbRouteMacMetric.setStatus("current")
_VRtrSpbRouteMacNHopSysID_Type = SystemID
_VRtrSpbRouteMacNHopSysID_Object = MibTableColumn
vRtrSpbRouteMacNHopSysID = _VRtrSpbRouteMacNHopSysID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 18, 1, 5),
    _VRtrSpbRouteMacNHopSysID_Type()
)
vRtrSpbRouteMacNHopSysID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSpbRouteMacNHopSysID.setStatus("current")


class _VRtrSpbRouteMacMetricType_Type(Integer32):
    """Custom type vRtrSpbRouteMacMetricType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("exact", 0),
          ("lowerBound", 1))
    )


_VRtrSpbRouteMacMetricType_Type.__name__ = "Integer32"
_VRtrSpbRouteMacMetricType_Object = MibTableColumn
vRtrSpbRouteMacMetricType = _VRtrSpbRouteMacMetricType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 18, 1, 6),
    _VRtrSpbRouteMacMetricType_Type()
)
vRtrSpbRouteMacMetricType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSpbRouteMacMetricType.setStatus("current")
_VRtrSpbRouteIsidTable_Object = MibTable
vRtrSpbRouteIsidTable = _VRtrSpbRouteIsidTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 19)
)
if mibBuilder.loadTexts:
    vRtrSpbRouteIsidTable.setStatus("current")
_VRtrSpbRouteIsidEntry_Object = MibTableRow
vRtrSpbRouteIsidEntry = _VRtrSpbRouteIsidEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 19, 1)
)
vRtrSpbRouteIsidEntry.setIndexNames(
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "TIMETRA-ISIS-MIB", "vRtrSpbEctFid"),
    (0, "TIMETRA-ISIS-MIB", "vRtrSpbRouteIsidDestIsid"),
    (0, "TIMETRA-ISIS-MIB", "vRtrSpbRouteIsidIfIndex"),
)
if mibBuilder.loadTexts:
    vRtrSpbRouteIsidEntry.setStatus("current")
_VRtrSpbRouteIsidDestIsid_Type = Unsigned32
_VRtrSpbRouteIsidDestIsid_Object = MibTableColumn
vRtrSpbRouteIsidDestIsid = _VRtrSpbRouteIsidDestIsid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 19, 1, 1),
    _VRtrSpbRouteIsidDestIsid_Type()
)
vRtrSpbRouteIsidDestIsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrSpbRouteIsidDestIsid.setStatus("current")
_VRtrSpbRouteIsidIfIndex_Type = InterfaceIndex
_VRtrSpbRouteIsidIfIndex_Object = MibTableColumn
vRtrSpbRouteIsidIfIndex = _VRtrSpbRouteIsidIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 19, 1, 2),
    _VRtrSpbRouteIsidIfIndex_Type()
)
vRtrSpbRouteIsidIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrSpbRouteIsidIfIndex.setStatus("current")
_VRtrSpbRouteIsidSpfRunNumber_Type = Counter32
_VRtrSpbRouteIsidSpfRunNumber_Object = MibTableColumn
vRtrSpbRouteIsidSpfRunNumber = _VRtrSpbRouteIsidSpfRunNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 19, 1, 3),
    _VRtrSpbRouteIsidSpfRunNumber_Type()
)
vRtrSpbRouteIsidSpfRunNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSpbRouteIsidSpfRunNumber.setStatus("current")
_VRtrSpbRouteIsidNHopSysID_Type = SystemID
_VRtrSpbRouteIsidNHopSysID_Object = MibTableColumn
vRtrSpbRouteIsidNHopSysID = _VRtrSpbRouteIsidNHopSysID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 19, 1, 4),
    _VRtrSpbRouteIsidNHopSysID_Type()
)
vRtrSpbRouteIsidNHopSysID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSpbRouteIsidNHopSysID.setStatus("current")
_VRtrSpbRouteIsidInMfib_Type = TruthValue
_VRtrSpbRouteIsidInMfib_Object = MibTableColumn
vRtrSpbRouteIsidInMfib = _VRtrSpbRouteIsidInMfib_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 19, 1, 5),
    _VRtrSpbRouteIsidInMfib_Type()
)
vRtrSpbRouteIsidInMfib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSpbRouteIsidInMfib.setStatus("current")
_VRtrSpbEctFidRangeTable_Object = MibTable
vRtrSpbEctFidRangeTable = _VRtrSpbEctFidRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 20)
)
if mibBuilder.loadTexts:
    vRtrSpbEctFidRangeTable.setStatus("current")
_VRtrSpbEctFidRangeEntry_Object = MibTableRow
vRtrSpbEctFidRangeEntry = _VRtrSpbEctFidRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 20, 1)
)
vRtrSpbEctFidRangeEntry.setIndexNames(
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "TIMETRA-ISIS-MIB", "vRtrIsisLevel"),
    (0, "TIMETRA-ISIS-MIB", "vRtrSpbEctFid"),
)
if mibBuilder.loadTexts:
    vRtrSpbEctFidRangeEntry.setStatus("current")
_VRtrSpbEctFidRangeEnd_Type = TmnxSpbFid
_VRtrSpbEctFidRangeEnd_Object = MibTableColumn
vRtrSpbEctFidRangeEnd = _VRtrSpbEctFidRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 20, 1, 1),
    _VRtrSpbEctFidRangeEnd_Type()
)
vRtrSpbEctFidRangeEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSpbEctFidRangeEnd.setStatus("current")


class _VRtrSpbEctFidRangeAlgorithm_Type(Integer32):
    """Custom type vRtrSpbEctFidRangeAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("lowPathId", 0),
          ("highPathId", 1))
    )


_VRtrSpbEctFidRangeAlgorithm_Type.__name__ = "Integer32"
_VRtrSpbEctFidRangeAlgorithm_Object = MibTableColumn
vRtrSpbEctFidRangeAlgorithm = _VRtrSpbEctFidRangeAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 20, 1, 2),
    _VRtrSpbEctFidRangeAlgorithm_Type()
)
vRtrSpbEctFidRangeAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSpbEctFidRangeAlgorithm.setStatus("current")
_VRtrIsisLgTableLastChanged_Type = TimeStamp
_VRtrIsisLgTableLastChanged_Object = MibScalar
vRtrIsisLgTableLastChanged = _VRtrIsisLgTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 21),
    _VRtrIsisLgTableLastChanged_Type()
)
vRtrIsisLgTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLgTableLastChanged.setStatus("current")
_VRtrIsisLgTable_Object = MibTable
vRtrIsisLgTable = _VRtrIsisLgTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 22)
)
if mibBuilder.loadTexts:
    vRtrIsisLgTable.setStatus("current")
_VRtrIsisLgEntry_Object = MibTableRow
vRtrIsisLgEntry = _VRtrIsisLgEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 22, 1)
)
vRtrIsisLgEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "TIMETRA-ISIS-MIB", "vRtrIsisLgName"),
)
if mibBuilder.loadTexts:
    vRtrIsisLgEntry.setStatus("current")
_VRtrIsisLgName_Type = TNamedItem
_VRtrIsisLgName_Object = MibTableColumn
vRtrIsisLgName = _VRtrIsisLgName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 22, 1, 1),
    _VRtrIsisLgName_Type()
)
vRtrIsisLgName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIsisLgName.setStatus("current")
_VRtrIsisLgRowStatus_Type = RowStatus
_VRtrIsisLgRowStatus_Object = MibTableColumn
vRtrIsisLgRowStatus = _VRtrIsisLgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 22, 1, 2),
    _VRtrIsisLgRowStatus_Type()
)
vRtrIsisLgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIsisLgRowStatus.setStatus("current")
_VRtrIsisLgDescription_Type = DisplayString
_VRtrIsisLgDescription_Object = MibTableColumn
vRtrIsisLgDescription = _VRtrIsisLgDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 22, 1, 3),
    _VRtrIsisLgDescription_Type()
)
vRtrIsisLgDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIsisLgDescription.setStatus("current")
_VRtrIsisLgRowLastChanged_Type = TimeStamp
_VRtrIsisLgRowLastChanged_Object = MibTableColumn
vRtrIsisLgRowLastChanged = _VRtrIsisLgRowLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 22, 1, 4),
    _VRtrIsisLgRowLastChanged_Type()
)
vRtrIsisLgRowLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLgRowLastChanged.setStatus("current")
_VRtrIsisLgLevelTableLastChanged_Type = TimeStamp
_VRtrIsisLgLevelTableLastChanged_Object = MibScalar
vRtrIsisLgLevelTableLastChanged = _VRtrIsisLgLevelTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 23),
    _VRtrIsisLgLevelTableLastChanged_Type()
)
vRtrIsisLgLevelTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLgLevelTableLastChanged.setStatus("current")
_VRtrIsisLgLevelTable_Object = MibTable
vRtrIsisLgLevelTable = _VRtrIsisLgLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 24)
)
if mibBuilder.loadTexts:
    vRtrIsisLgLevelTable.setStatus("current")
_VRtrIsisLgLevelEntry_Object = MibTableRow
vRtrIsisLgLevelEntry = _VRtrIsisLgLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 24, 1)
)
vRtrIsisLgLevelEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "TIMETRA-ISIS-MIB", "vRtrIsisLgName"),
    (0, "TIMETRA-ISIS-MIB", "vRtrIsisLgLevelLvl"),
)
if mibBuilder.loadTexts:
    vRtrIsisLgLevelEntry.setStatus("current")


class _VRtrIsisLgLevelLvl_Type(Integer32):
    """Custom type vRtrIsisLgLevelLvl based on Integer32"""
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


_VRtrIsisLgLevelLvl_Type.__name__ = "Integer32"
_VRtrIsisLgLevelLvl_Object = MibTableColumn
vRtrIsisLgLevelLvl = _VRtrIsisLgLevelLvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 24, 1, 1),
    _VRtrIsisLgLevelLvl_Type()
)
vRtrIsisLgLevelLvl.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIsisLgLevelLvl.setStatus("current")


class _VRtrIsisLgLevelOperMembers_Type(Unsigned32):
    """Custom type vRtrIsisLgLevelOperMembers based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_VRtrIsisLgLevelOperMembers_Type.__name__ = "Unsigned32"
_VRtrIsisLgLevelOperMembers_Object = MibTableColumn
vRtrIsisLgLevelOperMembers = _VRtrIsisLgLevelOperMembers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 24, 1, 2),
    _VRtrIsisLgLevelOperMembers_Type()
)
vRtrIsisLgLevelOperMembers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrIsisLgLevelOperMembers.setStatus("current")


class _VRtrIsisLgLevelRevertMembers_Type(Unsigned32):
    """Custom type vRtrIsisLgLevelRevertMembers based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_VRtrIsisLgLevelRevertMembers_Type.__name__ = "Unsigned32"
_VRtrIsisLgLevelRevertMembers_Object = MibTableColumn
vRtrIsisLgLevelRevertMembers = _VRtrIsisLgLevelRevertMembers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 24, 1, 3),
    _VRtrIsisLgLevelRevertMembers_Type()
)
vRtrIsisLgLevelRevertMembers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrIsisLgLevelRevertMembers.setStatus("current")


class _VRtrIsisLgLevelIPv4UcastMetric_Type(Unsigned32):
    """Custom type vRtrIsisLgLevelIPv4UcastMetric based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_VRtrIsisLgLevelIPv4UcastMetric_Type.__name__ = "Unsigned32"
_VRtrIsisLgLevelIPv4UcastMetric_Object = MibTableColumn
vRtrIsisLgLevelIPv4UcastMetric = _VRtrIsisLgLevelIPv4UcastMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 24, 1, 4),
    _VRtrIsisLgLevelIPv4UcastMetric_Type()
)
vRtrIsisLgLevelIPv4UcastMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrIsisLgLevelIPv4UcastMetric.setStatus("current")


class _VRtrIsisLgLevelIPv6UcastMetric_Type(Unsigned32):
    """Custom type vRtrIsisLgLevelIPv6UcastMetric based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_VRtrIsisLgLevelIPv6UcastMetric_Type.__name__ = "Unsigned32"
_VRtrIsisLgLevelIPv6UcastMetric_Object = MibTableColumn
vRtrIsisLgLevelIPv6UcastMetric = _VRtrIsisLgLevelIPv6UcastMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 24, 1, 5),
    _VRtrIsisLgLevelIPv6UcastMetric_Type()
)
vRtrIsisLgLevelIPv6UcastMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrIsisLgLevelIPv6UcastMetric.setStatus("current")


class _VRtrIsisLgLevelIPv4McastMetric_Type(Unsigned32):
    """Custom type vRtrIsisLgLevelIPv4McastMetric based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_VRtrIsisLgLevelIPv4McastMetric_Type.__name__ = "Unsigned32"
_VRtrIsisLgLevelIPv4McastMetric_Object = MibTableColumn
vRtrIsisLgLevelIPv4McastMetric = _VRtrIsisLgLevelIPv4McastMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 24, 1, 6),
    _VRtrIsisLgLevelIPv4McastMetric_Type()
)
vRtrIsisLgLevelIPv4McastMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrIsisLgLevelIPv4McastMetric.setStatus("current")


class _VRtrIsisLgLevelIPv6McastMetric_Type(Unsigned32):
    """Custom type vRtrIsisLgLevelIPv6McastMetric based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_VRtrIsisLgLevelIPv6McastMetric_Type.__name__ = "Unsigned32"
_VRtrIsisLgLevelIPv6McastMetric_Object = MibTableColumn
vRtrIsisLgLevelIPv6McastMetric = _VRtrIsisLgLevelIPv6McastMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 24, 1, 7),
    _VRtrIsisLgLevelIPv6McastMetric_Type()
)
vRtrIsisLgLevelIPv6McastMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrIsisLgLevelIPv6McastMetric.setStatus("current")
_VRtrIsisLgLevelLastChanged_Type = TimeStamp
_VRtrIsisLgLevelLastChanged_Object = MibTableColumn
vRtrIsisLgLevelLastChanged = _VRtrIsisLgLevelLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 24, 1, 8),
    _VRtrIsisLgLevelLastChanged_Type()
)
vRtrIsisLgLevelLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLgLevelLastChanged.setStatus("current")
_VRtrIsisLgLevelOperTable_Object = MibTable
vRtrIsisLgLevelOperTable = _VRtrIsisLgLevelOperTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 25)
)
if mibBuilder.loadTexts:
    vRtrIsisLgLevelOperTable.setStatus("current")
_VRtrIsisLgLevelOperEntry_Object = MibTableRow
vRtrIsisLgLevelOperEntry = _VRtrIsisLgLevelOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 25, 1)
)
vRtrIsisLgLevelOperEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "TIMETRA-ISIS-MIB", "vRtrIsisLgName"),
    (0, "TIMETRA-ISIS-MIB", "vRtrIsisLgLevelLvl"),
)
if mibBuilder.loadTexts:
    vRtrIsisLgLevelOperEntry.setStatus("current")
_VRtrIsisLgLevelOpOperMembers_Type = Unsigned32
_VRtrIsisLgLevelOpOperMembers_Object = MibTableColumn
vRtrIsisLgLevelOpOperMembers = _VRtrIsisLgLevelOpOperMembers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 25, 1, 1),
    _VRtrIsisLgLevelOpOperMembers_Type()
)
vRtrIsisLgLevelOpOperMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLgLevelOpOperMembers.setStatus("current")
_VRtrIsisLgLevelOperRevertMembers_Type = Unsigned32
_VRtrIsisLgLevelOperRevertMembers_Object = MibTableColumn
vRtrIsisLgLevelOperRevertMembers = _VRtrIsisLgLevelOperRevertMembers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 25, 1, 2),
    _VRtrIsisLgLevelOperRevertMembers_Type()
)
vRtrIsisLgLevelOperRevertMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLgLevelOperRevertMembers.setStatus("current")
_VRtrIsisLgLevelOperMembersCount_Type = Unsigned32
_VRtrIsisLgLevelOperMembersCount_Object = MibTableColumn
vRtrIsisLgLevelOperMembersCount = _VRtrIsisLgLevelOperMembersCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 25, 1, 3),
    _VRtrIsisLgLevelOperMembersCount_Type()
)
vRtrIsisLgLevelOperMembersCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLgLevelOperMembersCount.setStatus("current")
_VRtrIsisLgLevelOperActiveMembers_Type = Unsigned32
_VRtrIsisLgLevelOperActiveMembers_Object = MibTableColumn
vRtrIsisLgLevelOperActiveMembers = _VRtrIsisLgLevelOperActiveMembers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 25, 1, 4),
    _VRtrIsisLgLevelOperActiveMembers_Type()
)
vRtrIsisLgLevelOperActiveMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLgLevelOperActiveMembers.setStatus("current")


class _VRtrIsisLgLevelOperState_Type(Integer32):
    """Custom type vRtrIsisLgLevelOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("offsetApplied", 2))
    )


_VRtrIsisLgLevelOperState_Type.__name__ = "Integer32"
_VRtrIsisLgLevelOperState_Object = MibTableColumn
vRtrIsisLgLevelOperState = _VRtrIsisLgLevelOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 25, 1, 5),
    _VRtrIsisLgLevelOperState_Type()
)
vRtrIsisLgLevelOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLgLevelOperState.setStatus("current")
_VRtrIsisLgLevelMembersOperTable_Object = MibTable
vRtrIsisLgLevelMembersOperTable = _VRtrIsisLgLevelMembersOperTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 27)
)
if mibBuilder.loadTexts:
    vRtrIsisLgLevelMembersOperTable.setStatus("current")
_VRtrIsisLgLevelMembersOperEntry_Object = MibTableRow
vRtrIsisLgLevelMembersOperEntry = _VRtrIsisLgLevelMembersOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 27, 1)
)
vRtrIsisLgLevelMembersOperEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "TIMETRA-ISIS-MIB", "vRtrIsisLgName"),
    (0, "TIMETRA-ISIS-MIB", "vRtrIsisLgLevelLvl"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
)
if mibBuilder.loadTexts:
    vRtrIsisLgLevelMembersOperEntry.setStatus("current")


class _VRtrIsisLgLevelMembersOperState_Type(Integer32):
    """Custom type vRtrIsisLgLevelMembersOperState based on Integer32"""
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
          ("bitErrorRate", 3))
    )


_VRtrIsisLgLevelMembersOperState_Type.__name__ = "Integer32"
_VRtrIsisLgLevelMembersOperState_Object = MibTableColumn
vRtrIsisLgLevelMembersOperState = _VRtrIsisLgLevelMembersOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 1, 27, 1, 1),
    _VRtrIsisLgLevelMembersOperState_Type()
)
vRtrIsisLgLevelMembersOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLgLevelMembersOperState.setStatus("current")
_VRtrIsisIfObjs_ObjectIdentity = ObjectIdentity
vRtrIsisIfObjs = _VRtrIsisIfObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 2)
)
_VRtrIsisIfTable_Object = MibTable
vRtrIsisIfTable = _VRtrIsisIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 2, 1)
)
if mibBuilder.loadTexts:
    vRtrIsisIfTable.setStatus("deprecated")
_VRtrIsisIfEntry_Object = MibTableRow
vRtrIsisIfEntry = _VRtrIsisIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 2, 1, 1)
)
vRtrIsisIfEntry.setIndexNames(
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
)
if mibBuilder.loadTexts:
    vRtrIsisIfEntry.setStatus("deprecated")
_VRtrIsisIfRowStatus_Type = RowStatus
_VRtrIsisIfRowStatus_Object = MibTableColumn
vRtrIsisIfRowStatus = _VRtrIsisIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 2, 1, 1, 1),
    _VRtrIsisIfRowStatus_Type()
)
vRtrIsisIfRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIfRowStatus.setStatus("deprecated")
_VRtrIsisIfLastChangeTime_Type = TimeStamp
_VRtrIsisIfLastChangeTime_Object = MibTableColumn
vRtrIsisIfLastChangeTime = _VRtrIsisIfLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 2, 1, 1, 2),
    _VRtrIsisIfLastChangeTime_Type()
)
vRtrIsisIfLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIfLastChangeTime.setStatus("deprecated")


class _VRtrIsisIfAdminState_Type(TmnxAdminState):
    """Custom type vRtrIsisIfAdminState based on TmnxAdminState"""
    defaultValue = 3


_VRtrIsisIfAdminState_Type.__name__ = "TmnxAdminState"
_VRtrIsisIfAdminState_Object = MibTableColumn
vRtrIsisIfAdminState = _VRtrIsisIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 2, 1, 1, 3),
    _VRtrIsisIfAdminState_Type()
)
vRtrIsisIfAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIfAdminState.setStatus("deprecated")
_VRtrIsisIfOperState_Type = TmnxOperState
_VRtrIsisIfOperState_Object = MibTableColumn
vRtrIsisIfOperState = _VRtrIsisIfOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 2, 1, 1, 4),
    _VRtrIsisIfOperState_Type()
)
vRtrIsisIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIfOperState.setStatus("deprecated")


class _VRtrIsisIfCsnpInterval_Type(Unsigned32):
    """Custom type vRtrIsisIfCsnpInterval based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VRtrIsisIfCsnpInterval_Type.__name__ = "Unsigned32"
_VRtrIsisIfCsnpInterval_Object = MibTableColumn
vRtrIsisIfCsnpInterval = _VRtrIsisIfCsnpInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 2, 1, 1, 5),
    _VRtrIsisIfCsnpInterval_Type()
)
vRtrIsisIfCsnpInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIfCsnpInterval.setStatus("deprecated")
if mibBuilder.loadTexts:
    vRtrIsisIfCsnpInterval.setUnits("seconds")


class _VRtrIsisIfHelloAuthKey_Type(OctetString):
    """Custom type vRtrIsisIfHelloAuthKey based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_VRtrIsisIfHelloAuthKey_Type.__name__ = "OctetString"
_VRtrIsisIfHelloAuthKey_Object = MibTableColumn
vRtrIsisIfHelloAuthKey = _VRtrIsisIfHelloAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 2, 1, 1, 6),
    _VRtrIsisIfHelloAuthKey_Type()
)
vRtrIsisIfHelloAuthKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIfHelloAuthKey.setStatus("deprecated")


class _VRtrIsisIfHelloAuthType_Type(Integer32):
    """Custom type vRtrIsisIfHelloAuthType based on Integer32"""
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


_VRtrIsisIfHelloAuthType_Type.__name__ = "Integer32"
_VRtrIsisIfHelloAuthType_Object = MibTableColumn
vRtrIsisIfHelloAuthType = _VRtrIsisIfHelloAuthType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 2, 1, 1, 7),
    _VRtrIsisIfHelloAuthType_Type()
)
vRtrIsisIfHelloAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIfHelloAuthType.setStatus("deprecated")


class _VRtrIsisIfLspPacingInterval_Type(Unsigned32):
    """Custom type vRtrIsisIfLspPacingInterval based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VRtrIsisIfLspPacingInterval_Type.__name__ = "Unsigned32"
_VRtrIsisIfLspPacingInterval_Object = MibTableColumn
vRtrIsisIfLspPacingInterval = _VRtrIsisIfLspPacingInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 2, 1, 1, 8),
    _VRtrIsisIfLspPacingInterval_Type()
)
vRtrIsisIfLspPacingInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIfLspPacingInterval.setStatus("deprecated")
if mibBuilder.loadTexts:
    vRtrIsisIfLspPacingInterval.setUnits("milliseconds")


class _VRtrIsisIfCircIndex_Type(Integer32):
    """Custom type vRtrIsisIfCircIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000000000),
    )


_VRtrIsisIfCircIndex_Type.__name__ = "Integer32"
_VRtrIsisIfCircIndex_Object = MibTableColumn
vRtrIsisIfCircIndex = _VRtrIsisIfCircIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 2, 1, 1, 9),
    _VRtrIsisIfCircIndex_Type()
)
vRtrIsisIfCircIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIfCircIndex.setStatus("deprecated")


class _VRtrIsisIfRetransmitInterval_Type(Unsigned32):
    """Custom type vRtrIsisIfRetransmitInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VRtrIsisIfRetransmitInterval_Type.__name__ = "Unsigned32"
_VRtrIsisIfRetransmitInterval_Object = MibTableColumn
vRtrIsisIfRetransmitInterval = _VRtrIsisIfRetransmitInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 2, 1, 1, 10),
    _VRtrIsisIfRetransmitInterval_Type()
)
vRtrIsisIfRetransmitInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIfRetransmitInterval.setStatus("deprecated")
if mibBuilder.loadTexts:
    vRtrIsisIfRetransmitInterval.setUnits("seconds")


class _VRtrIsisIfTypeDefault_Type(TruthValue):
    """Custom type vRtrIsisIfTypeDefault based on TruthValue"""
    defaultValue = 1


_VRtrIsisIfTypeDefault_Type.__name__ = "TruthValue"
_VRtrIsisIfTypeDefault_Object = MibTableColumn
vRtrIsisIfTypeDefault = _VRtrIsisIfTypeDefault_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 2, 1, 1, 11),
    _VRtrIsisIfTypeDefault_Type()
)
vRtrIsisIfTypeDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIfTypeDefault.setStatus("deprecated")


class _VRtrIsisIfEnableBfd_Type(TruthValue):
    """Custom type vRtrIsisIfEnableBfd based on TruthValue"""
    defaultValue = 2


_VRtrIsisIfEnableBfd_Type.__name__ = "TruthValue"
_VRtrIsisIfEnableBfd_Object = MibTableColumn
vRtrIsisIfEnableBfd = _VRtrIsisIfEnableBfd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 2, 1, 1, 12),
    _VRtrIsisIfEnableBfd_Type()
)
vRtrIsisIfEnableBfd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIfEnableBfd.setStatus("deprecated")


class _VRtrIsisIfIPv6Unicast_Type(TruthValue):
    """Custom type vRtrIsisIfIPv6Unicast based on TruthValue"""
    defaultValue = 1


_VRtrIsisIfIPv6Unicast_Type.__name__ = "TruthValue"
_VRtrIsisIfIPv6Unicast_Object = MibTableColumn
vRtrIsisIfIPv6Unicast = _VRtrIsisIfIPv6Unicast_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 2, 1, 1, 13),
    _VRtrIsisIfIPv6Unicast_Type()
)
vRtrIsisIfIPv6Unicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIfIPv6Unicast.setStatus("deprecated")


class _VRtrIsisIfTeMetric_Type(Unsigned32):
    """Custom type vRtrIsisIfTeMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_VRtrIsisIfTeMetric_Type.__name__ = "Unsigned32"
_VRtrIsisIfTeMetric_Object = MibTableColumn
vRtrIsisIfTeMetric = _VRtrIsisIfTeMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 2, 1, 1, 14),
    _VRtrIsisIfTeMetric_Type()
)
vRtrIsisIfTeMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIfTeMetric.setStatus("deprecated")
_VRtrIsisIfTeState_Type = TmnxOperState
_VRtrIsisIfTeState_Object = MibTableColumn
vRtrIsisIfTeState = _VRtrIsisIfTeState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 2, 1, 1, 15),
    _VRtrIsisIfTeState_Type()
)
vRtrIsisIfTeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIfTeState.setStatus("deprecated")
_VRtrIsisIfAdminGroup_Type = Unsigned32
_VRtrIsisIfAdminGroup_Object = MibTableColumn
vRtrIsisIfAdminGroup = _VRtrIsisIfAdminGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 2, 1, 1, 16),
    _VRtrIsisIfAdminGroup_Type()
)
vRtrIsisIfAdminGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIfAdminGroup.setStatus("deprecated")
_VRtrIsisIfLdpSyncState_Type = TmnxOperState
_VRtrIsisIfLdpSyncState_Object = MibTableColumn
vRtrIsisIfLdpSyncState = _VRtrIsisIfLdpSyncState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 2, 1, 1, 17),
    _VRtrIsisIfLdpSyncState_Type()
)
vRtrIsisIfLdpSyncState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIfLdpSyncState.setStatus("deprecated")
_VRtrIsisIfLdpSyncMaxMetric_Type = TruthValue
_VRtrIsisIfLdpSyncMaxMetric_Object = MibTableColumn
vRtrIsisIfLdpSyncMaxMetric = _VRtrIsisIfLdpSyncMaxMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 2, 1, 1, 18),
    _VRtrIsisIfLdpSyncMaxMetric_Type()
)
vRtrIsisIfLdpSyncMaxMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIfLdpSyncMaxMetric.setStatus("deprecated")


class _VRtrIsisIfLdpSyncTimerState_Type(Integer32):
    """Custom type vRtrIsisIfLdpSyncTimerState based on Integer32"""
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


_VRtrIsisIfLdpSyncTimerState_Type.__name__ = "Integer32"
_VRtrIsisIfLdpSyncTimerState_Object = MibTableColumn
vRtrIsisIfLdpSyncTimerState = _VRtrIsisIfLdpSyncTimerState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 2, 1, 1, 19),
    _VRtrIsisIfLdpSyncTimerState_Type()
)
vRtrIsisIfLdpSyncTimerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIfLdpSyncTimerState.setStatus("deprecated")


class _VRtrIsisIfLdpSyncTimeLeft_Type(Unsigned32):
    """Custom type vRtrIsisIfLdpSyncTimeLeft based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1800),
    )


_VRtrIsisIfLdpSyncTimeLeft_Type.__name__ = "Unsigned32"
_VRtrIsisIfLdpSyncTimeLeft_Object = MibTableColumn
vRtrIsisIfLdpSyncTimeLeft = _VRtrIsisIfLdpSyncTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 2, 1, 1, 20),
    _VRtrIsisIfLdpSyncTimeLeft_Type()
)
vRtrIsisIfLdpSyncTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIfLdpSyncTimeLeft.setStatus("deprecated")
if mibBuilder.loadTexts:
    vRtrIsisIfLdpSyncTimeLeft.setUnits("seconds")


class _VRtrIsisIfRouteTag_Type(Unsigned32):
    """Custom type vRtrIsisIfRouteTag based on Unsigned32"""
    defaultValue = 0


_VRtrIsisIfRouteTag_Type.__name__ = "Unsigned32"
_VRtrIsisIfRouteTag_Object = MibTableColumn
vRtrIsisIfRouteTag = _VRtrIsisIfRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 2, 1, 1, 21),
    _VRtrIsisIfRouteTag_Type()
)
vRtrIsisIfRouteTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIfRouteTag.setStatus("deprecated")


class _VRtrIsisIfIpv6EnableBfd_Type(TruthValue):
    """Custom type vRtrIsisIfIpv6EnableBfd based on TruthValue"""
    defaultValue = 2


_VRtrIsisIfIpv6EnableBfd_Type.__name__ = "TruthValue"
_VRtrIsisIfIpv6EnableBfd_Object = MibTableColumn
vRtrIsisIfIpv6EnableBfd = _VRtrIsisIfIpv6EnableBfd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 2, 1, 1, 22),
    _VRtrIsisIfIpv6EnableBfd_Type()
)
vRtrIsisIfIpv6EnableBfd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIfIpv6EnableBfd.setStatus("deprecated")


class _VRtrIsisIfHelloAuthentication_Type(TruthValue):
    """Custom type vRtrIsisIfHelloAuthentication based on TruthValue"""
    defaultValue = 1


_VRtrIsisIfHelloAuthentication_Type.__name__ = "TruthValue"
_VRtrIsisIfHelloAuthentication_Object = MibTableColumn
vRtrIsisIfHelloAuthentication = _VRtrIsisIfHelloAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 2, 1, 1, 23),
    _VRtrIsisIfHelloAuthentication_Type()
)
vRtrIsisIfHelloAuthentication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIfHelloAuthentication.setStatus("deprecated")


class _VRtrIsisIfLoopfreeAltExclude_Type(TruthValue):
    """Custom type vRtrIsisIfLoopfreeAltExclude based on TruthValue"""
    defaultValue = 2


_VRtrIsisIfLoopfreeAltExclude_Type.__name__ = "TruthValue"
_VRtrIsisIfLoopfreeAltExclude_Object = MibTableColumn
vRtrIsisIfLoopfreeAltExclude = _VRtrIsisIfLoopfreeAltExclude_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 2, 1, 1, 24),
    _VRtrIsisIfLoopfreeAltExclude_Type()
)
vRtrIsisIfLoopfreeAltExclude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIfLoopfreeAltExclude.setStatus("deprecated")


class _VRtrIsisIfOperType_Type(Integer32):
    """Custom type vRtrIsisIfOperType based on Integer32"""
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


_VRtrIsisIfOperType_Type.__name__ = "Integer32"
_VRtrIsisIfOperType_Object = MibTableColumn
vRtrIsisIfOperType = _VRtrIsisIfOperType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 2, 1, 1, 25),
    _VRtrIsisIfOperType_Type()
)
vRtrIsisIfOperType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIfOperType.setStatus("deprecated")


class _VRtrIsisIfIPv4Mcast_Type(TruthValue):
    """Custom type vRtrIsisIfIPv4Mcast based on TruthValue"""
    defaultValue = 1


_VRtrIsisIfIPv4Mcast_Type.__name__ = "TruthValue"
_VRtrIsisIfIPv4Mcast_Object = MibTableColumn
vRtrIsisIfIPv4Mcast = _VRtrIsisIfIPv4Mcast_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 2, 1, 1, 26),
    _VRtrIsisIfIPv4Mcast_Type()
)
vRtrIsisIfIPv4Mcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIfIPv4Mcast.setStatus("deprecated")


class _VRtrIsisIfIPv6Mcast_Type(TruthValue):
    """Custom type vRtrIsisIfIPv6Mcast based on TruthValue"""
    defaultValue = 1


_VRtrIsisIfIPv6Mcast_Type.__name__ = "TruthValue"
_VRtrIsisIfIPv6Mcast_Object = MibTableColumn
vRtrIsisIfIPv6Mcast = _VRtrIsisIfIPv6Mcast_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 2, 1, 1, 27),
    _VRtrIsisIfIPv6Mcast_Type()
)
vRtrIsisIfIPv6Mcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIfIPv6Mcast.setStatus("deprecated")


class _VRtrIsisIfBerState_Type(Integer32):
    """Custom type vRtrIsisIfBerState based on Integer32"""
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


_VRtrIsisIfBerState_Type.__name__ = "Integer32"
_VRtrIsisIfBerState_Object = MibTableColumn
vRtrIsisIfBerState = _VRtrIsisIfBerState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 2, 1, 1, 28),
    _VRtrIsisIfBerState_Type()
)
vRtrIsisIfBerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIfBerState.setStatus("deprecated")
_VRtrIsisIfLevelTable_Object = MibTable
vRtrIsisIfLevelTable = _VRtrIsisIfLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 2, 2)
)
if mibBuilder.loadTexts:
    vRtrIsisIfLevelTable.setStatus("deprecated")
_VRtrIsisIfLevelEntry_Object = MibTableRow
vRtrIsisIfLevelEntry = _VRtrIsisIfLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 2, 2, 1)
)
vRtrIsisIfLevelEntry.setIndexNames(
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
    (0, "TIMETRA-ISIS-MIB", "vRtrIsisIfLevel"),
)
if mibBuilder.loadTexts:
    vRtrIsisIfLevelEntry.setStatus("deprecated")


class _VRtrIsisIfLevel_Type(Integer32):
    """Custom type vRtrIsisIfLevel based on Integer32"""
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


_VRtrIsisIfLevel_Type.__name__ = "Integer32"
_VRtrIsisIfLevel_Object = MibTableColumn
vRtrIsisIfLevel = _VRtrIsisIfLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 2, 2, 1, 1),
    _VRtrIsisIfLevel_Type()
)
vRtrIsisIfLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIsisIfLevel.setStatus("deprecated")
_VRtrIsisIfLevelLastChangeTime_Type = TimeStamp
_VRtrIsisIfLevelLastChangeTime_Object = MibTableColumn
vRtrIsisIfLevelLastChangeTime = _VRtrIsisIfLevelLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 2, 2, 1, 2),
    _VRtrIsisIfLevelLastChangeTime_Type()
)
vRtrIsisIfLevelLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIfLevelLastChangeTime.setStatus("deprecated")


class _VRtrIsisIfLevelHelloAuthKey_Type(OctetString):
    """Custom type vRtrIsisIfLevelHelloAuthKey based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_VRtrIsisIfLevelHelloAuthKey_Type.__name__ = "OctetString"
_VRtrIsisIfLevelHelloAuthKey_Object = MibTableColumn
vRtrIsisIfLevelHelloAuthKey = _VRtrIsisIfLevelHelloAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 2, 2, 1, 3),
    _VRtrIsisIfLevelHelloAuthKey_Type()
)
vRtrIsisIfLevelHelloAuthKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIfLevelHelloAuthKey.setStatus("deprecated")


class _VRtrIsisIfLevelHelloAuthType_Type(Integer32):
    """Custom type vRtrIsisIfLevelHelloAuthType based on Integer32"""
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


_VRtrIsisIfLevelHelloAuthType_Type.__name__ = "Integer32"
_VRtrIsisIfLevelHelloAuthType_Object = MibTableColumn
vRtrIsisIfLevelHelloAuthType = _VRtrIsisIfLevelHelloAuthType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 2, 2, 1, 4),
    _VRtrIsisIfLevelHelloAuthType_Type()
)
vRtrIsisIfLevelHelloAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIfLevelHelloAuthType.setStatus("deprecated")


class _VRtrIsisIfLevelPassive_Type(TruthValue):
    """Custom type vRtrIsisIfLevelPassive based on TruthValue"""
    defaultValue = 2


_VRtrIsisIfLevelPassive_Type.__name__ = "TruthValue"
_VRtrIsisIfLevelPassive_Object = MibTableColumn
vRtrIsisIfLevelPassive = _VRtrIsisIfLevelPassive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 2, 2, 1, 5),
    _VRtrIsisIfLevelPassive_Type()
)
vRtrIsisIfLevelPassive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIfLevelPassive.setStatus("deprecated")


class _VRtrIsisIfLevelTeMetric_Type(Unsigned32):
    """Custom type vRtrIsisIfLevelTeMetric based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4261412864),
    )


_VRtrIsisIfLevelTeMetric_Type.__name__ = "Unsigned32"
_VRtrIsisIfLevelTeMetric_Object = MibTableColumn
vRtrIsisIfLevelTeMetric = _VRtrIsisIfLevelTeMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 2, 2, 1, 6),
    _VRtrIsisIfLevelTeMetric_Type()
)
vRtrIsisIfLevelTeMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIfLevelTeMetric.setStatus("deprecated")
_VRtrIsisIfLevelNumAdjacencies_Type = Unsigned32
_VRtrIsisIfLevelNumAdjacencies_Object = MibTableColumn
vRtrIsisIfLevelNumAdjacencies = _VRtrIsisIfLevelNumAdjacencies_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 2, 2, 1, 7),
    _VRtrIsisIfLevelNumAdjacencies_Type()
)
vRtrIsisIfLevelNumAdjacencies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIfLevelNumAdjacencies.setStatus("deprecated")


class _VRtrIsisIfLevelISPriority_Type(Unsigned32):
    """Custom type vRtrIsisIfLevelISPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_VRtrIsisIfLevelISPriority_Type.__name__ = "Unsigned32"
_VRtrIsisIfLevelISPriority_Object = MibTableColumn
vRtrIsisIfLevelISPriority = _VRtrIsisIfLevelISPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 2, 2, 1, 8),
    _VRtrIsisIfLevelISPriority_Type()
)
vRtrIsisIfLevelISPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIfLevelISPriority.setStatus("deprecated")


class _VRtrIsisIfLevelHelloTimer_Type(Unsigned32):
    """Custom type vRtrIsisIfLevelHelloTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20000),
    )


_VRtrIsisIfLevelHelloTimer_Type.__name__ = "Unsigned32"
_VRtrIsisIfLevelHelloTimer_Object = MibTableColumn
vRtrIsisIfLevelHelloTimer = _VRtrIsisIfLevelHelloTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 2, 2, 1, 9),
    _VRtrIsisIfLevelHelloTimer_Type()
)
vRtrIsisIfLevelHelloTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIfLevelHelloTimer.setStatus("deprecated")


class _VRtrIsisIfLevelAdminMetric_Type(Unsigned32):
    """Custom type vRtrIsisIfLevelAdminMetric based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_VRtrIsisIfLevelAdminMetric_Type.__name__ = "Unsigned32"
_VRtrIsisIfLevelAdminMetric_Object = MibTableColumn
vRtrIsisIfLevelAdminMetric = _VRtrIsisIfLevelAdminMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 2, 2, 1, 10),
    _VRtrIsisIfLevelAdminMetric_Type()
)
vRtrIsisIfLevelAdminMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIfLevelAdminMetric.setStatus("deprecated")


class _VRtrIsisIfLevelOperMetric_Type(Unsigned32):
    """Custom type vRtrIsisIfLevelOperMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_VRtrIsisIfLevelOperMetric_Type.__name__ = "Unsigned32"
_VRtrIsisIfLevelOperMetric_Object = MibTableColumn
vRtrIsisIfLevelOperMetric = _VRtrIsisIfLevelOperMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 2, 2, 1, 11),
    _VRtrIsisIfLevelOperMetric_Type()
)
vRtrIsisIfLevelOperMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIfLevelOperMetric.setStatus("deprecated")


class _VRtrIsisIfLvlIPv6UcastAdmMet_Type(Unsigned32):
    """Custom type vRtrIsisIfLvlIPv6UcastAdmMet based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_VRtrIsisIfLvlIPv6UcastAdmMet_Type.__name__ = "Unsigned32"
_VRtrIsisIfLvlIPv6UcastAdmMet_Object = MibTableColumn
vRtrIsisIfLvlIPv6UcastAdmMet = _VRtrIsisIfLvlIPv6UcastAdmMet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 2, 2, 1, 12),
    _VRtrIsisIfLvlIPv6UcastAdmMet_Type()
)
vRtrIsisIfLvlIPv6UcastAdmMet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIfLvlIPv6UcastAdmMet.setStatus("deprecated")


class _VRtrIsisIfLvlIPv6UcastOperMet_Type(Unsigned32):
    """Custom type vRtrIsisIfLvlIPv6UcastOperMet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_VRtrIsisIfLvlIPv6UcastOperMet_Type.__name__ = "Unsigned32"
_VRtrIsisIfLvlIPv6UcastOperMet_Object = MibTableColumn
vRtrIsisIfLvlIPv6UcastOperMet = _VRtrIsisIfLvlIPv6UcastOperMet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 2, 2, 1, 13),
    _VRtrIsisIfLvlIPv6UcastOperMet_Type()
)
vRtrIsisIfLvlIPv6UcastOperMet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIfLvlIPv6UcastOperMet.setStatus("deprecated")


class _VRtrIsisIfLvlIPv4McastAdmMetric_Type(Unsigned32):
    """Custom type vRtrIsisIfLvlIPv4McastAdmMetric based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_VRtrIsisIfLvlIPv4McastAdmMetric_Type.__name__ = "Unsigned32"
_VRtrIsisIfLvlIPv4McastAdmMetric_Object = MibTableColumn
vRtrIsisIfLvlIPv4McastAdmMetric = _VRtrIsisIfLvlIPv4McastAdmMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 2, 2, 1, 14),
    _VRtrIsisIfLvlIPv4McastAdmMetric_Type()
)
vRtrIsisIfLvlIPv4McastAdmMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIfLvlIPv4McastAdmMetric.setStatus("deprecated")


class _VRtrIsisIfLvlIPv6McastAdmMetric_Type(Unsigned32):
    """Custom type vRtrIsisIfLvlIPv6McastAdmMetric based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_VRtrIsisIfLvlIPv6McastAdmMetric_Type.__name__ = "Unsigned32"
_VRtrIsisIfLvlIPv6McastAdmMetric_Object = MibTableColumn
vRtrIsisIfLvlIPv6McastAdmMetric = _VRtrIsisIfLvlIPv6McastAdmMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 2, 2, 1, 15),
    _VRtrIsisIfLvlIPv6McastAdmMetric_Type()
)
vRtrIsisIfLvlIPv6McastAdmMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIfLvlIPv6McastAdmMetric.setStatus("deprecated")


class _VRtrIsisIfLevelLinkGroupName_Type(TNamedItemOrEmpty):
    """Custom type vRtrIsisIfLevelLinkGroupName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrIsisIfLevelLinkGroupName_Type.__name__ = "TNamedItemOrEmpty"
_VRtrIsisIfLevelLinkGroupName_Object = MibTableColumn
vRtrIsisIfLevelLinkGroupName = _VRtrIsisIfLevelLinkGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 2, 2, 1, 16),
    _VRtrIsisIfLevelLinkGroupName_Type()
)
vRtrIsisIfLevelLinkGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIfLevelLinkGroupName.setStatus("deprecated")


class _VRtrIsisIfLevelSdOffset_Type(Unsigned32):
    """Custom type vRtrIsisIfLevelSdOffset based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_VRtrIsisIfLevelSdOffset_Type.__name__ = "Unsigned32"
_VRtrIsisIfLevelSdOffset_Object = MibTableColumn
vRtrIsisIfLevelSdOffset = _VRtrIsisIfLevelSdOffset_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 2, 2, 1, 17),
    _VRtrIsisIfLevelSdOffset_Type()
)
vRtrIsisIfLevelSdOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIfLevelSdOffset.setStatus("deprecated")


class _VRtrIsisIfLevelSfOffset_Type(Unsigned32):
    """Custom type vRtrIsisIfLevelSfOffset based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_VRtrIsisIfLevelSfOffset_Type.__name__ = "Unsigned32"
_VRtrIsisIfLevelSfOffset_Object = MibTableColumn
vRtrIsisIfLevelSfOffset = _VRtrIsisIfLevelSfOffset_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 2, 2, 1, 18),
    _VRtrIsisIfLevelSfOffset_Type()
)
vRtrIsisIfLevelSfOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIfLevelSfOffset.setStatus("deprecated")


class _VRtrIsisIfLvlIPv4McastOperMetric_Type(Unsigned32):
    """Custom type vRtrIsisIfLvlIPv4McastOperMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_VRtrIsisIfLvlIPv4McastOperMetric_Type.__name__ = "Unsigned32"
_VRtrIsisIfLvlIPv4McastOperMetric_Object = MibTableColumn
vRtrIsisIfLvlIPv4McastOperMetric = _VRtrIsisIfLvlIPv4McastOperMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 2, 2, 1, 19),
    _VRtrIsisIfLvlIPv4McastOperMetric_Type()
)
vRtrIsisIfLvlIPv4McastOperMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIfLvlIPv4McastOperMetric.setStatus("deprecated")


class _VRtrIsisIfLvlIPv6McastOperMetric_Type(Unsigned32):
    """Custom type vRtrIsisIfLvlIPv6McastOperMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_VRtrIsisIfLvlIPv6McastOperMetric_Type.__name__ = "Unsigned32"
_VRtrIsisIfLvlIPv6McastOperMetric_Object = MibTableColumn
vRtrIsisIfLvlIPv6McastOperMetric = _VRtrIsisIfLvlIPv6McastOperMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 2, 2, 1, 20),
    _VRtrIsisIfLvlIPv6McastOperMetric_Type()
)
vRtrIsisIfLvlIPv6McastOperMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIfLvlIPv6McastOperMetric.setStatus("deprecated")
_VRtrIsisAdjObjs_ObjectIdentity = ObjectIdentity
vRtrIsisAdjObjs = _VRtrIsisAdjObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 3)
)
_VRtrIsisISAdjTable_Object = MibTable
vRtrIsisISAdjTable = _VRtrIsisISAdjTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 3, 1)
)
if mibBuilder.loadTexts:
    vRtrIsisISAdjTable.setStatus("deprecated")
_VRtrIsisISAdjEntry_Object = MibTableRow
vRtrIsisISAdjEntry = _VRtrIsisISAdjEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 3, 1, 1)
)
if mibBuilder.loadTexts:
    vRtrIsisISAdjEntry.setStatus("deprecated")


class _VRtrIsisISAdjExpiresIn_Type(Integer32):
    """Custom type vRtrIsisISAdjExpiresIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VRtrIsisISAdjExpiresIn_Type.__name__ = "Integer32"
_VRtrIsisISAdjExpiresIn_Object = MibTableColumn
vRtrIsisISAdjExpiresIn = _VRtrIsisISAdjExpiresIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 3, 1, 1, 1),
    _VRtrIsisISAdjExpiresIn_Type()
)
vRtrIsisISAdjExpiresIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisISAdjExpiresIn.setStatus("deprecated")
if mibBuilder.loadTexts:
    vRtrIsisISAdjExpiresIn.setUnits("seconds")


class _VRtrIsisISAdjCircLevel_Type(Integer32):
    """Custom type vRtrIsisISAdjCircLevel based on Integer32"""
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


_VRtrIsisISAdjCircLevel_Type.__name__ = "Integer32"
_VRtrIsisISAdjCircLevel_Object = MibTableColumn
vRtrIsisISAdjCircLevel = _VRtrIsisISAdjCircLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 3, 1, 1, 2),
    _VRtrIsisISAdjCircLevel_Type()
)
vRtrIsisISAdjCircLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisISAdjCircLevel.setStatus("deprecated")
_VRtrIsisISAdjNeighborIP_Type = IpAddress
_VRtrIsisISAdjNeighborIP_Object = MibTableColumn
vRtrIsisISAdjNeighborIP = _VRtrIsisISAdjNeighborIP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 3, 1, 1, 3),
    _VRtrIsisISAdjNeighborIP_Type()
)
vRtrIsisISAdjNeighborIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisISAdjNeighborIP.setStatus("deprecated")
_VRtrIsisISAdjRestartSupport_Type = TruthValue
_VRtrIsisISAdjRestartSupport_Object = MibTableColumn
vRtrIsisISAdjRestartSupport = _VRtrIsisISAdjRestartSupport_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 3, 1, 1, 4),
    _VRtrIsisISAdjRestartSupport_Type()
)
vRtrIsisISAdjRestartSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisISAdjRestartSupport.setStatus("deprecated")


class _VRtrIsisISAdjRestartStatus_Type(Integer32):
    """Custom type vRtrIsisISAdjRestartStatus based on Integer32"""
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
          ("restart-complete", 3),
          ("helping", 4))
    )


_VRtrIsisISAdjRestartStatus_Type.__name__ = "Integer32"
_VRtrIsisISAdjRestartStatus_Object = MibTableColumn
vRtrIsisISAdjRestartStatus = _VRtrIsisISAdjRestartStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 3, 1, 1, 5),
    _VRtrIsisISAdjRestartStatus_Type()
)
vRtrIsisISAdjRestartStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisISAdjRestartStatus.setStatus("deprecated")
_VRtrIsisISAdjRestartSupressed_Type = TruthValue
_VRtrIsisISAdjRestartSupressed_Object = MibTableColumn
vRtrIsisISAdjRestartSupressed = _VRtrIsisISAdjRestartSupressed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 3, 1, 1, 6),
    _VRtrIsisISAdjRestartSupressed_Type()
)
vRtrIsisISAdjRestartSupressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisISAdjRestartSupressed.setStatus("deprecated")
_VRtrIsisISAdjNumRestarts_Type = Unsigned32
_VRtrIsisISAdjNumRestarts_Object = MibTableColumn
vRtrIsisISAdjNumRestarts = _VRtrIsisISAdjNumRestarts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 3, 1, 1, 7),
    _VRtrIsisISAdjNumRestarts_Type()
)
vRtrIsisISAdjNumRestarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisISAdjNumRestarts.setStatus("deprecated")
_VRtrIsisISAdjLastRestartTime_Type = TimeStamp
_VRtrIsisISAdjLastRestartTime_Object = MibTableColumn
vRtrIsisISAdjLastRestartTime = _VRtrIsisISAdjLastRestartTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 3, 1, 1, 8),
    _VRtrIsisISAdjLastRestartTime_Type()
)
vRtrIsisISAdjLastRestartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisISAdjLastRestartTime.setStatus("deprecated")
_VRtrIsisISAdjNeighborIPv6Type_Type = InetAddressType
_VRtrIsisISAdjNeighborIPv6Type_Object = MibTableColumn
vRtrIsisISAdjNeighborIPv6Type = _VRtrIsisISAdjNeighborIPv6Type_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 3, 1, 1, 9),
    _VRtrIsisISAdjNeighborIPv6Type_Type()
)
vRtrIsisISAdjNeighborIPv6Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisISAdjNeighborIPv6Type.setStatus("deprecated")


class _VRtrIsisISAdjNeighborIpv6_Type(InetAddress):
    """Custom type vRtrIsisISAdjNeighborIpv6 based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_VRtrIsisISAdjNeighborIpv6_Type.__name__ = "InetAddress"
_VRtrIsisISAdjNeighborIpv6_Object = MibTableColumn
vRtrIsisISAdjNeighborIpv6 = _VRtrIsisISAdjNeighborIpv6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 3, 1, 1, 10),
    _VRtrIsisISAdjNeighborIpv6_Type()
)
vRtrIsisISAdjNeighborIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisISAdjNeighborIpv6.setStatus("deprecated")
_VRtrIsisISAdjMtEnabled_Type = TruthValue
_VRtrIsisISAdjMtEnabled_Object = MibTableColumn
vRtrIsisISAdjMtEnabled = _VRtrIsisISAdjMtEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 3, 1, 1, 11),
    _VRtrIsisISAdjMtEnabled_Type()
)
vRtrIsisISAdjMtEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisISAdjMtEnabled.setStatus("deprecated")
_VRtrIsisISAdjMtId0_Type = TruthValue
_VRtrIsisISAdjMtId0_Object = MibTableColumn
vRtrIsisISAdjMtId0 = _VRtrIsisISAdjMtId0_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 3, 1, 1, 12),
    _VRtrIsisISAdjMtId0_Type()
)
vRtrIsisISAdjMtId0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisISAdjMtId0.setStatus("deprecated")
_VRtrIsisISAdjMtId2_Type = TruthValue
_VRtrIsisISAdjMtId2_Object = MibTableColumn
vRtrIsisISAdjMtId2 = _VRtrIsisISAdjMtId2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 3, 1, 1, 13),
    _VRtrIsisISAdjMtId2_Type()
)
vRtrIsisISAdjMtId2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisISAdjMtId2.setStatus("deprecated")
_VRtrIsisISAdjMtId3_Type = TruthValue
_VRtrIsisISAdjMtId3_Object = MibTableColumn
vRtrIsisISAdjMtId3 = _VRtrIsisISAdjMtId3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 3, 1, 1, 14),
    _VRtrIsisISAdjMtId3_Type()
)
vRtrIsisISAdjMtId3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisISAdjMtId3.setStatus("deprecated")
_VRtrIsisISAdjMtId4_Type = TruthValue
_VRtrIsisISAdjMtId4_Object = MibTableColumn
vRtrIsisISAdjMtId4 = _VRtrIsisISAdjMtId4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 3, 1, 1, 15),
    _VRtrIsisISAdjMtId4_Type()
)
vRtrIsisISAdjMtId4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisISAdjMtId4.setStatus("deprecated")
_VRtrIsisNotificationObjs_ObjectIdentity = ObjectIdentity
vRtrIsisNotificationObjs = _VRtrIsisNotificationObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 4)
)
_VRtrIsisNotificationTable_Object = MibTable
vRtrIsisNotificationTable = _VRtrIsisNotificationTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 4, 1)
)
if mibBuilder.loadTexts:
    vRtrIsisNotificationTable.setStatus("current")
_VRtrIsisNotificationEntry_Object = MibTableRow
vRtrIsisNotificationEntry = _VRtrIsisNotificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 4, 1, 1)
)
vRtrIsisNotificationEntry.setIndexNames(
    (0, "ISIS-MIB", "isisSysInstance"),
)
if mibBuilder.loadTexts:
    vRtrIsisNotificationEntry.setStatus("current")


class _VRtrIsisTrapLSPID_Type(OctetString):
    """Custom type vRtrIsisTrapLSPID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 8),
    )


_VRtrIsisTrapLSPID_Type.__name__ = "OctetString"
_VRtrIsisTrapLSPID_Object = MibTableColumn
vRtrIsisTrapLSPID = _VRtrIsisTrapLSPID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 4, 1, 1, 1),
    _VRtrIsisTrapLSPID_Type()
)
vRtrIsisTrapLSPID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrIsisTrapLSPID.setStatus("current")


class _VRtrIsisSystemLevel_Type(Integer32):
    """Custom type vRtrIsisSystemLevel based on Integer32"""
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


_VRtrIsisSystemLevel_Type.__name__ = "Integer32"
_VRtrIsisSystemLevel_Object = MibTableColumn
vRtrIsisSystemLevel = _VRtrIsisSystemLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 4, 1, 1, 2),
    _VRtrIsisSystemLevel_Type()
)
vRtrIsisSystemLevel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrIsisSystemLevel.setStatus("current")


class _VRtrIsisPDUFragment_Type(OctetString):
    """Custom type vRtrIsisPDUFragment based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_VRtrIsisPDUFragment_Type.__name__ = "OctetString"
_VRtrIsisPDUFragment_Object = MibTableColumn
vRtrIsisPDUFragment = _VRtrIsisPDUFragment_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 4, 1, 1, 3),
    _VRtrIsisPDUFragment_Type()
)
vRtrIsisPDUFragment.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrIsisPDUFragment.setStatus("current")


class _VRtrIsisFieldLen_Type(Integer32):
    """Custom type vRtrIsisFieldLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VRtrIsisFieldLen_Type.__name__ = "Integer32"
_VRtrIsisFieldLen_Object = MibTableColumn
vRtrIsisFieldLen = _VRtrIsisFieldLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 4, 1, 1, 4),
    _VRtrIsisFieldLen_Type()
)
vRtrIsisFieldLen.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrIsisFieldLen.setStatus("current")


class _VRtrIsisMaxAreaAddress_Type(Integer32):
    """Custom type vRtrIsisMaxAreaAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VRtrIsisMaxAreaAddress_Type.__name__ = "Integer32"
_VRtrIsisMaxAreaAddress_Object = MibTableColumn
vRtrIsisMaxAreaAddress = _VRtrIsisMaxAreaAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 4, 1, 1, 5),
    _VRtrIsisMaxAreaAddress_Type()
)
vRtrIsisMaxAreaAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrIsisMaxAreaAddress.setStatus("current")


class _VRtrIsisProtocolVersion_Type(Integer32):
    """Custom type vRtrIsisProtocolVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VRtrIsisProtocolVersion_Type.__name__ = "Integer32"
_VRtrIsisProtocolVersion_Object = MibTableColumn
vRtrIsisProtocolVersion = _VRtrIsisProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 4, 1, 1, 6),
    _VRtrIsisProtocolVersion_Type()
)
vRtrIsisProtocolVersion.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrIsisProtocolVersion.setStatus("current")


class _VRtrIsisLSPSize_Type(Integer32):
    """Custom type vRtrIsisLSPSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VRtrIsisLSPSize_Type.__name__ = "Integer32"
_VRtrIsisLSPSize_Object = MibTableColumn
vRtrIsisLSPSize = _VRtrIsisLSPSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 4, 1, 1, 7),
    _VRtrIsisLSPSize_Type()
)
vRtrIsisLSPSize.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrIsisLSPSize.setStatus("current")


class _VRtrIsisOriginatingBufferSize_Type(Integer32):
    """Custom type vRtrIsisOriginatingBufferSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VRtrIsisOriginatingBufferSize_Type.__name__ = "Integer32"
_VRtrIsisOriginatingBufferSize_Object = MibTableColumn
vRtrIsisOriginatingBufferSize = _VRtrIsisOriginatingBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 4, 1, 1, 8),
    _VRtrIsisOriginatingBufferSize_Type()
)
vRtrIsisOriginatingBufferSize.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrIsisOriginatingBufferSize.setStatus("current")


class _VRtrIsisProtocolsSupported_Type(OctetString):
    """Custom type vRtrIsisProtocolsSupported based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VRtrIsisProtocolsSupported_Type.__name__ = "OctetString"
_VRtrIsisProtocolsSupported_Object = MibTableColumn
vRtrIsisProtocolsSupported = _VRtrIsisProtocolsSupported_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 4, 1, 1, 9),
    _VRtrIsisProtocolsSupported_Type()
)
vRtrIsisProtocolsSupported.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrIsisProtocolsSupported.setStatus("current")


class _VRtrIsisNbrSysId_Type(OctetString):
    """Custom type vRtrIsisNbrSysId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_VRtrIsisNbrSysId_Type.__name__ = "OctetString"
_VRtrIsisNbrSysId_Object = MibTableColumn
vRtrIsisNbrSysId = _VRtrIsisNbrSysId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 4, 1, 1, 10),
    _VRtrIsisNbrSysId_Type()
)
vRtrIsisNbrSysId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrIsisNbrSysId.setStatus("current")
_VRtrSpbEctFidStart_Type = TmnxSpbFid
_VRtrSpbEctFidStart_Object = MibScalar
vRtrSpbEctFidStart = _VRtrSpbEctFidStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 4, 2),
    _VRtrSpbEctFidStart_Type()
)
vRtrSpbEctFidStart.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrSpbEctFidStart.setStatus("current")
_VRtrSpbEctFidEnd_Type = TmnxSpbFid
_VRtrSpbEctFidEnd_Object = MibScalar
vRtrSpbEctFidEnd = _VRtrSpbEctFidEnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 4, 3),
    _VRtrSpbEctFidEnd_Type()
)
vRtrSpbEctFidEnd.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrSpbEctFidEnd.setStatus("current")


class _VRtrIsisFailureReasonCode_Type(Integer32):
    """Custom type vRtrIsisFailureReasonCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("outOfResources", 1)
    )


_VRtrIsisFailureReasonCode_Type.__name__ = "Integer32"
_VRtrIsisFailureReasonCode_Object = MibScalar
vRtrIsisFailureReasonCode = _VRtrIsisFailureReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 10, 4, 4),
    _VRtrIsisFailureReasonCode_Type()
)
vRtrIsisFailureReasonCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrIsisFailureReasonCode.setStatus("obsolete")
_VRtrIsisNotifyPrefix_ObjectIdentity = ObjectIdentity
vRtrIsisNotifyPrefix = _VRtrIsisNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 10)
)
_VRtrIsisNotifications_ObjectIdentity = ObjectIdentity
vRtrIsisNotifications = _VRtrIsisNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 10, 0)
)
isisISAdjEntry.registerAugmentions(
    ("TIMETRA-ISIS-MIB",
     "vRtrIsisISAdjEntry")
)
vRtrIsisISAdjEntry.setIndexNames(*isisISAdjEntry.getIndexNames())

# Managed Objects groups

vRtrIsisHostGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 10, 2, 2)
)
vRtrIsisHostGroup.setObjects(
    ("TIMETRA-ISIS-MIB", "vRtrIsisHostname")
)
if mibBuilder.loadTexts:
    vRtrIsisHostGroup.setStatus("deprecated")

vRtrIsisPathGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 10, 2, 4)
)
vRtrIsisPathGroup.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisPathMetric"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisPathSNPA"))
)
if mibBuilder.loadTexts:
    vRtrIsisPathGroup.setStatus("obsolete")

vRtrIsisLSPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 10, 2, 5)
)
vRtrIsisLSPGroup.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisLSPSeq"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLSPChecksum"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLSPLifetimeRemain"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLSPVersion"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLSPPktType"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLSPPktVersion"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLSPMaxArea"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLSPSysIdLen"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLSPAttributes"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLSPUsedLen"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLSPAllocLen"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLSPBuff"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLSPZeroRLT"))
)
if mibBuilder.loadTexts:
    vRtrIsisLSPGroup.setStatus("deprecated")

vRtrIsisNotificationObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 10, 2, 8)
)
vRtrIsisNotificationObjGroup.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisTrapLSPID"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSystemLevel"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisPDUFragment"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisFieldLen"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisMaxAreaAddress"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisProtocolVersion"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLSPSize"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisOriginatingBufferSize"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisProtocolsSupported"))
)
if mibBuilder.loadTexts:
    vRtrIsisNotificationObjGroup.setStatus("current")

vRtrIsisSpfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 10, 2, 10)
)
vRtrIsisSpfGroup.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisSpfRunTime"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSpfL1Nodes"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSpfL2Nodes"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSpfEventCount"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSpfLastTriggerLSPId"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSpfTriggerReason"))
)
if mibBuilder.loadTexts:
    vRtrIsisSpfGroup.setStatus("deprecated")

vRtrIsisV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 10, 2, 16)
)
vRtrIsisV4v0Group.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisLastEnabledTime"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisAuthKey"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisAuthType"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisAuthCheck"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisExportPolicy1"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisExportPolicy2"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisExportPolicy3"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisExportPolicy4"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisExportPolicy5"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLspLifetime"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisOverloadTimeout"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisOperState"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisReferenceBw"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisTrafficEng"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisShortCuts"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSpfHoldTime"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLastSpfRun"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisGracefulRestart"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisOverloadOnBoot"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisOverloadOnBootTimeout"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSpfWait"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSpfInitialWait"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSpfSecondWait"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLspMaxWait"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLspInitialWait"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLspSecondWait"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisCsnpAuthentication"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisHelloAuthentication"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisPsnpAuthentication"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisGRRestartDuration"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisGRHelperMode"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisEnableIPv6"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisEnableIPv4"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisUnicastImport"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisMulticastImport"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisStrictAdjacencyCheck"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLevelAuthKey"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLevelAuthType"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLevelExtPreference"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLevelPreference"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLevelWideMetricsOnly"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLevelOverloadStatus"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLevelOverloadTimeLeft"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLevelNumLSPs"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLevelCsnpAuthentication"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLevelHelloAuthentication"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLevelPsnpAuthentication"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSpfRuns"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLSPRegenerations"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisInitiatedPurges"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLSPRecd"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLSPDrop"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLSPSent"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLSPRetrans"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIIHRecd"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIIHDrop"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIIHSent"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIIHRetrans"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisCSNPRecd"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisCSNPDrop"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisCSNPSent"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisCSNPRetrans"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisPSNPRecd"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisPSNPDrop"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisPSNPSent"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisPSNPRetrans"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisUnknownRecd"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisUnknownDrop"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisUnknownSent"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisUnknownRetrans"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisCSPFRequests"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisCSPFDroppedRequests"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisCSPFPathsFound"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisCSPFPathsNotFound"))
)
if mibBuilder.loadTexts:
    vRtrIsisV4v0Group.setStatus("obsolete")

vRtrIsisRouteV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 10, 2, 17)
)
vRtrIsisRouteV4v0Group.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisRouteLevel"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisRouteSpfVersion"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisRouteMetric"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisRouteType"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisRouteNHopSysID"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisInetRouteLevel"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisInetRouteSpfRunNumber"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisInetRouteMetric"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisInetRouteType"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisInetRouteNHopSysID"))
)
if mibBuilder.loadTexts:
    vRtrIsisRouteV4v0Group.setStatus("obsolete")

vRtrIsisSummaryV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 10, 2, 18)
)
vRtrIsisSummaryV4v0Group.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisSummRowStatus"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSummLevel"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisInetSummRowStatus"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisInetSummLevel"))
)
if mibBuilder.loadTexts:
    vRtrIsisSummaryV4v0Group.setStatus("deprecated")

vRtrIsisAdjV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 10, 2, 19)
)
vRtrIsisAdjV4v0Group.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisISAdjExpiresIn"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisISAdjCircLevel"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisISAdjNeighborIP"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisISAdjRestartSupport"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisISAdjRestartStatus"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisISAdjRestartSupressed"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisISAdjNumRestarts"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisISAdjLastRestartTime"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisISAdjNeighborIPv6Type"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisISAdjNeighborIpv6"))
)
if mibBuilder.loadTexts:
    vRtrIsisAdjV4v0Group.setStatus("obsolete")

vRtrIsisIfV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 10, 2, 20)
)
vRtrIsisIfV4v0Group.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisIfRowStatus"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLastChangeTime"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfAdminState"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfOperState"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfCsnpInterval"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfHelloAuthKey"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfHelloAuthType"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLspPacingInterval"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfCircIndex"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfRetransmitInterval"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfTypeDefault"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfEnableBfd"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLevelLastChangeTime"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLevelHelloAuthKey"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLevelHelloAuthType"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLevelPassive"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLevelTeMetric"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLevelNumAdjacencies"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLevelISPriority"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLevelHelloTimer"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLevelAdminMetric"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLevelOperMetric"))
)
if mibBuilder.loadTexts:
    vRtrIsisIfV4v0Group.setStatus("obsolete")

vRtrIsisV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 10, 2, 21)
)
vRtrIsisV5v0Group.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisLastEnabledTime"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisAuthKey"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisAuthType"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisAuthCheck"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisExportPolicy1"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisExportPolicy2"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisExportPolicy3"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisExportPolicy4"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisExportPolicy5"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLspLifetime"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisOverloadTimeout"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisOperState"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisReferenceBw"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisTrafficEng"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisShortCuts"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSpfHoldTime"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLastSpfRun"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisGracefulRestart"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisOverloadOnBoot"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisOverloadOnBootTimeout"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSpfWait"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSpfInitialWait"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSpfSecondWait"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLspMaxWait"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLspInitialWait"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLspSecondWait"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisCsnpAuthentication"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisHelloAuthentication"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisPsnpAuthentication"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisGRRestartDuration"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisGRHelperMode"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisEnableIPv4"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisUnicastImport"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisMulticastImport"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisStrictAdjacencyCheck"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisManualSpfTrigger"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisMultiTopology"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIPv6RoutingTopo"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisMultiTopoIPv6Ucast"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLevelAuthKey"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLevelAuthType"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLevelExtPreference"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLevelPreference"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLevelWideMetricsOnly"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLevelOverloadStatus"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLevelOverloadTimeLeft"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLevelNumLSPs"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLevelCsnpAuthentication"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLevelHelloAuthentication"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLevelPsnpAuthentication"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSpfRuns"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLSPRegenerations"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisInitiatedPurges"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLSPRecd"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLSPDrop"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLSPSent"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLSPRetrans"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIIHRecd"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIIHDrop"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIIHSent"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIIHRetrans"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisCSNPRecd"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisCSNPDrop"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisCSNPSent"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisCSNPRetrans"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisPSNPRecd"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisPSNPDrop"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisPSNPSent"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisPSNPRetrans"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisUnknownRecd"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisUnknownDrop"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisUnknownSent"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisUnknownRetrans"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisCSPFRequests"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisCSPFDroppedRequests"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisCSPFPathsFound"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisCSPFPathsNotFound"))
)
if mibBuilder.loadTexts:
    vRtrIsisV5v0Group.setStatus("deprecated")

vRtrIsisIfV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 10, 2, 22)
)
vRtrIsisIfV5v0Group.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisIfRowStatus"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLastChangeTime"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfAdminState"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfOperState"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfCsnpInterval"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfHelloAuthKey"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfHelloAuthType"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLspPacingInterval"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfCircIndex"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfRetransmitInterval"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfTypeDefault"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfEnableBfd"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfIPv6Unicast"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLevelLastChangeTime"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLevelHelloAuthKey"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLevelHelloAuthType"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLevelPassive"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLevelTeMetric"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLevelNumAdjacencies"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLevelISPriority"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLevelHelloTimer"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLevelAdminMetric"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLevelOperMetric"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLvlIPv6UcastAdmMet"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLvlIPv6UcastOperMet"))
)
if mibBuilder.loadTexts:
    vRtrIsisIfV5v0Group.setStatus("deprecated")

vRtrIsisRouteV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 10, 2, 23)
)
vRtrIsisRouteV5v0Group.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisRouteLevel"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisRouteSpfVersion"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisRouteMetric"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisRouteType"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisRouteNHopSysID"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisInetRouteLevel"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisInetRouteSpfRunNumber"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisInetRouteMetric"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisInetRouteType"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisInetRouteNHopSysID"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisInetMtRouteLevel"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisInetMtRouteSpfRunNumber"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisInetMtRouteMetric"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisInetMtRouteType"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisInetMtRouteNHopSysID"))
)
if mibBuilder.loadTexts:
    vRtrIsisRouteV5v0Group.setStatus("deprecated")

vRtrIsisPathV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 10, 2, 24)
)
vRtrIsisPathV5v0Group.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisPathMetric"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisPathSNPA"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisMtPathMetric"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisMtPathSNPA"))
)
if mibBuilder.loadTexts:
    vRtrIsisPathV5v0Group.setStatus("deprecated")

vRtrIsisObsoleteV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 10, 2, 25)
)
vRtrIsisObsoleteV5v0Group.setObjects(
    ("TIMETRA-ISIS-MIB", "vRtrIsisEnableIPv6")
)
if mibBuilder.loadTexts:
    vRtrIsisObsoleteV5v0Group.setStatus("current")

vRtrIsisAdjV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 10, 2, 26)
)
vRtrIsisAdjV5v0Group.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisISAdjExpiresIn"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisISAdjCircLevel"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisISAdjNeighborIP"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisISAdjRestartSupport"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisISAdjRestartStatus"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisISAdjRestartSupressed"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisISAdjNumRestarts"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisISAdjLastRestartTime"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisISAdjNeighborIPv6Type"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisISAdjNeighborIpv6"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisISAdjMtEnabled"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisISAdjMtId0"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisISAdjMtId2"))
)
if mibBuilder.loadTexts:
    vRtrIsisAdjV5v0Group.setStatus("deprecated")

vRtrIsisLspMtuV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 10, 2, 27)
)
vRtrIsisLspMtuV6v0Group.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisSysOrigL1LSPBuffSize"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSysOrigL2LSPBuffSize"))
)
if mibBuilder.loadTexts:
    vRtrIsisLspMtuV6v0Group.setStatus("deprecated")

vRtrIsisIfV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 10, 2, 28)
)
vRtrIsisIfV6v0Group.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisIfTeMetric"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfTeState"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfAdminGroup"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLdpSyncState"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLdpSyncMaxMetric"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLdpSyncTimerState"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLdpSyncTimeLeft"))
)
if mibBuilder.loadTexts:
    vRtrIsisIfV6v0Group.setStatus("deprecated")

vRtrIsisV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 10, 2, 29)
)
vRtrIsisV6v0Group.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisLdpSyncAdminState"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIPv6UnicastImport"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIPv6MulticastImport"))
)
if mibBuilder.loadTexts:
    vRtrIsisV6v0Group.setStatus("deprecated")

vRtrIsisV6v1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 10, 2, 31)
)
vRtrIsisV6v1Group.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisAdvertisePassiveOnly"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisDefaultRouteTag"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSuppressDefault"))
)
if mibBuilder.loadTexts:
    vRtrIsisV6v1Group.setStatus("deprecated")

vRtrIsisIfV6v1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 10, 2, 32)
)
vRtrIsisIfV6v1Group.setObjects(
    ("TIMETRA-ISIS-MIB", "vRtrIsisIfRouteTag")
)
if mibBuilder.loadTexts:
    vRtrIsisIfV6v1Group.setStatus("deprecated")

vRtrIsisSummaryV6v1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 10, 2, 33)
)
vRtrIsisSummaryV6v1Group.setObjects(
    ("TIMETRA-ISIS-MIB", "vRtrIsisInetSummRouteTag")
)
if mibBuilder.loadTexts:
    vRtrIsisSummaryV6v1Group.setStatus("deprecated")

vRtrIsisRouteV6v1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 10, 2, 34)
)
vRtrIsisRouteV6v1Group.setObjects(
    ("TIMETRA-ISIS-MIB", "vRtrIsisInetMtRouteTag")
)
if mibBuilder.loadTexts:
    vRtrIsisRouteV6v1Group.setStatus("deprecated")

vRtrIsisV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 10, 2, 35)
)
vRtrIsisV7v0Group.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisLdpOverRsvp"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisExportLimit"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisExportLimitLogPercent"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisTotalL1ExportedRoutes"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisTotalL2ExportedRoutes"))
)
if mibBuilder.loadTexts:
    vRtrIsisV7v0Group.setStatus("deprecated")

vRtrIsisV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 10, 2, 37)
)
vRtrIsisV8v0Group.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisRsvpShortcut"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisAdvertiseTunnelLink"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIidTlv"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisL1MacAddress"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisL2MacAddress"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLevelDefMetric"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLevelIPv6DefMetric"))
)
if mibBuilder.loadTexts:
    vRtrIsisV8v0Group.setStatus("deprecated")

vRtrIsisV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 10, 2, 38)
)
vRtrIsisV9v0Group.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisSysOperL1LSPBuffSize"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSysOperL2LSPBuffSize"))
)
if mibBuilder.loadTexts:
    vRtrIsisV9v0Group.setStatus("deprecated")

vRtrIsisIfV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 10, 2, 39)
)
vRtrIsisIfV9v0Group.setObjects(
    ("TIMETRA-ISIS-MIB", "vRtrIsisIfIpv6EnableBfd")
)
if mibBuilder.loadTexts:
    vRtrIsisIfV9v0Group.setStatus("deprecated")

vRtrIsisV9v0R4Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 10, 2, 40)
)
vRtrIsisV9v0R4Group.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisLoopfreeAlternate"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfHelloAuthentication"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLfaRuns"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisPathLfaIfIndex"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisPathLfaNHop"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisPathLfaMetric"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisPathLfaType"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisPathRouteType"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLfaNodesCovered"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLfaTotalNodes"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLfaNodeCoverage"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLfaIpv4NodesCovered"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLfaIpv4TotalNodes"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLfaIpv4Coverage"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLfaIpv6NodesCovered"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLfaIpv6TotalNodes"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLfaIpv6Coverage"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisMtPathLfaIfIndex"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisMtPathLfaNHop"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisMtPathLfaMetric"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisMtPathLfaType"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisMtPathRouteType"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisInetMtRouteBkupFlags"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisInetMtRouteBkupNextHopTy"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisInetMtRouteBkupNextHop"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisInetMtRouteBkupMetric"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSpfType"))
)
if mibBuilder.loadTexts:
    vRtrIsisV9v0R4Group.setStatus("deprecated")

vRtrSpbEctFidGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 10, 2, 41)
)
vRtrSpbEctFidGroup.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrSpbRouteIsidNHopSysID"),
        ("TIMETRA-ISIS-MIB", "vRtrSpbRouteIsidSpfRunNumber"),
        ("TIMETRA-ISIS-MIB", "vRtrSpbRouteIsidInMfib"),
        ("TIMETRA-ISIS-MIB", "vRtrSpbRouteMacMetric"),
        ("TIMETRA-ISIS-MIB", "vRtrSpbRouteMacMetricType"),
        ("TIMETRA-ISIS-MIB", "vRtrSpbRouteMacNHopSysID"),
        ("TIMETRA-ISIS-MIB", "vRtrSpbRouteMacSpfRunNumber"),
        ("TIMETRA-ISIS-MIB", "vRtrSpbRouteMacIfIndex"),
        ("TIMETRA-ISIS-MIB", "vRtrSpbPathIfIndex"),
        ("TIMETRA-ISIS-MIB", "vRtrSpbPathNHopSysID"),
        ("TIMETRA-ISIS-MIB", "vRtrSpbPathMetric"),
        ("TIMETRA-ISIS-MIB", "vRtrSpbPathSNPA"),
        ("TIMETRA-ISIS-MIB", "vRtrSpbEctFidRangeEnd"),
        ("TIMETRA-ISIS-MIB", "vRtrSpbEctFidRangeAlgorithm"),
        ("TIMETRA-ISIS-MIB", "vRtrSpbEctFidLastChanged"),
        ("TIMETRA-ISIS-MIB", "vRtrSpbEctFidAlgorithm"),
        ("TIMETRA-ISIS-MIB", "vRtrSpbEctFidTableLastChanged"))
)
if mibBuilder.loadTexts:
    vRtrSpbEctFidGroup.setStatus("current")

vRtrIsisV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 10, 2, 42)
)
vRtrIsisV10v0Group.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisLevelLoopfreeAltExclude"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLoopfreeAltExclude"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisRouteNextHopType"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisNextHopOwner"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisRouteNHOwnerAuxInfo"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisRouteBkupNHType"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisRouteBkupNHOwner"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisRouteBkupNHOwnAxInfo"))
)
if mibBuilder.loadTexts:
    vRtrIsisV10v0Group.setStatus("deprecated")

vRtrIsisNotifyObjsV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 10, 2, 43)
)
vRtrIsisNotifyObjsV10v0Group.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrSpbEctFidStart"),
        ("TIMETRA-ISIS-MIB", "vRtrSpbEctFidEnd"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisNbrSysId"))
)
if mibBuilder.loadTexts:
    vRtrIsisNotifyObjsV10v0Group.setStatus("current")

vRtrIsisV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 10, 2, 45)
)
vRtrIsisV11v0Group.setObjects(
    ("TIMETRA-ISIS-MIB", "vRtrIsisIfOperType")
)
if mibBuilder.loadTexts:
    vRtrIsisV11v0Group.setStatus("deprecated")

vRtrIsisV11R4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 10, 2, 46)
)
vRtrIsisV11R4v0Group.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisIPv4McastRoutingTopo"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIPv6McastRoutingTopo"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLevelDefIPv4McastMetric"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLevelDefIPv6McastMetric"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfIPv4Mcast"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfIPv6Mcast"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLvlIPv4McastAdmMetric"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLvlIPv6McastAdmMetric"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisMultiTopoIPv4Mcast"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisMultiTopoIPv6Mcast"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisISAdjMtId3"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisISAdjMtId4"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLvlIPv4McastOperMetric"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLvlIPv6McastOperMetric"))
)
if mibBuilder.loadTexts:
    vRtrIsisV11R4v0Group.setStatus("deprecated")

vRtrIsisOvrMaxMetricGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 10, 2, 47)
)
vRtrIsisOvrMaxMetricGroup.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisOverloadMaxMetric"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisOverloadOnBootMaxMetric"))
)
if mibBuilder.loadTexts:
    vRtrIsisOvrMaxMetricGroup.setStatus("deprecated")

vRtrIsisLgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 10, 2, 48)
)
vRtrIsisLgGroup.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisLgRowStatus"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLgRowLastChanged"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLgTableLastChanged"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLgLevelOperMembers"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLgLevelRevertMembers"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLgLevelIPv4UcastMetric"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLgLevelIPv6UcastMetric"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLgLevelIPv4McastMetric"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLgLevelIPv6McastMetric"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLgLevelTableLastChanged"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLgLevelLastChanged"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLevelLinkGroupName"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLgLevelOpOperMembers"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLgLevelOperRevertMembers"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLgLevelOperMembersCount"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLgLevelOperActiveMembers"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLgLevelOperState"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfBerState"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLevelSdOffset"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLevelSfOffset"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLgLevelMembersOperState"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLgDescription"))
)
if mibBuilder.loadTexts:
    vRtrIsisLgGroup.setStatus("deprecated")

vRtrIsisRouterIdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 10, 2, 49)
)
vRtrIsisRouterIdGroup.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisRouterId"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisOperRouterId"))
)
if mibBuilder.loadTexts:
    vRtrIsisRouterIdGroup.setStatus("deprecated")

vRtrIsisHelloPaddingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 10, 2, 50)
)
vRtrIsisHelloPaddingGroup.setObjects(
    ("TIMETRA-ISIS-MIB", "vRtrIsisHelloPadding")
)
if mibBuilder.loadTexts:
    vRtrIsisHelloPaddingGroup.setStatus("deprecated")

vRtrIsisLspGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 10, 2, 51)
)
vRtrIsisLspGroup.setObjects(
    ("TIMETRA-ISIS-MIB", "vRtrIsisIgnoreLspErrors")
)
if mibBuilder.loadTexts:
    vRtrIsisLspGroup.setStatus("deprecated")

vRtrIsisObsoleteNotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 10, 2, 53)
)
vRtrIsisObsoleteNotifyObjsGroup.setObjects(
    ("TIMETRA-ISIS-MIB", "vRtrIsisFailureReasonCode")
)
if mibBuilder.loadTexts:
    vRtrIsisObsoleteNotifyObjsGroup.setStatus("current")

vRtrIsisAdvRtrCapaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 10, 2, 55)
)
vRtrIsisAdvRtrCapaGroup.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisAdvRtrCapability"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLevelAdvRtrCapability"))
)
if mibBuilder.loadTexts:
    vRtrIsisAdvRtrCapaGroup.setStatus("deprecated")

vRtrIsisObsoletedV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 10, 2, 56)
)
vRtrIsisObsoletedV12v0Group.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisLastEnabledTime"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisAuthKey"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisAuthType"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisAuthCheck"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisExportPolicy1"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisExportPolicy2"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisExportPolicy3"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisExportPolicy4"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisExportPolicy5"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLspLifetime"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisOverloadTimeout"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisOperState"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisReferenceBw"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisTrafficEng"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisShortCuts"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSpfHoldTime"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLastSpfRun"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisGracefulRestart"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisOverloadOnBoot"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisOverloadOnBootTimeout"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSpfWait"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSpfInitialWait"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSpfSecondWait"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLspMaxWait"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLspInitialWait"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLspSecondWait"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisCsnpAuthentication"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisHelloAuthentication"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisPsnpAuthentication"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisGRRestartDuration"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisGRHelperMode"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisEnableIPv6"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisEnableIPv4"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisUnicastImport"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisMulticastImport"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisStrictAdjacencyCheck"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisManualSpfTrigger"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisMultiTopology"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisMultiTopoIPv6Ucast"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIPv6RoutingTopo"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSysOrigL1LSPBuffSize"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSysOrigL2LSPBuffSize"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLdpSyncAdminState"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIPv6UnicastImport"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIPv6MulticastImport"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisAdvertisePassiveOnly"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisDefaultRouteTag"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSuppressDefault"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLdpOverRsvp"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisExportLimit"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisExportLimitLogPercent"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisTotalL1ExportedRoutes"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisTotalL2ExportedRoutes"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisRsvpShortcut"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisAdvertiseTunnelLink"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIidTlv"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisL1MacAddress"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisL2MacAddress"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSysOperL1LSPBuffSize"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSysOperL2LSPBuffSize"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLoopfreeAlternate"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIPv4McastRoutingTopo"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIPv6McastRoutingTopo"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisMultiTopoIPv4Mcast"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisMultiTopoIPv6Mcast"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisOverloadMaxMetric"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisOverloadOnBootMaxMetric"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisRouterId"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisAdvRtrCapability"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisHelloPadding"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisOperRouterId"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIgnoreLspErrors"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLevelAuthKey"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLevelAuthType"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLevelExtPreference"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLevelPreference"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLevelWideMetricsOnly"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLevelOverloadStatus"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLevelOverloadTimeLeft"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLevelNumLSPs"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLevelCsnpAuthentication"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLevelHelloAuthentication"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLevelPsnpAuthentication"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLevelDefMetric"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLevelIPv6DefMetric"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLevelLoopfreeAltExclude"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLevelDefIPv4McastMetric"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLevelDefIPv6McastMetric"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLevelAdvRtrCapability"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSpfRuns"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLSPRegenerations"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisInitiatedPurges"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLSPRecd"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLSPDrop"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLSPSent"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLSPRetrans"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIIHRecd"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIIHDrop"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIIHSent"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIIHRetrans"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisCSNPRecd"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisCSNPDrop"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisCSNPSent"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisCSNPRetrans"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisPSNPRecd"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisPSNPDrop"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisPSNPSent"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisPSNPRetrans"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisUnknownRecd"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisUnknownDrop"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisUnknownSent"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisUnknownRetrans"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisCSPFRequests"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisCSPFDroppedRequests"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisCSPFPathsFound"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisCSPFPathsNotFound"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLfaRuns"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisHostname"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisRouteLevel"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisRouteSpfVersion"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisRouteMetric"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisRouteType"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisRouteNHopSysID"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisPathMetric"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisPathSNPA"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisPathLfaIfIndex"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisPathLfaNHop"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisPathLfaMetric"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisPathLfaType"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisPathRouteType"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLSPSeq"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLSPChecksum"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLSPLifetimeRemain"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLSPVersion"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLSPPktType"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLSPPktVersion"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLSPMaxArea"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLSPSysIdLen"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLSPAttributes"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLSPUsedLen"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLSPAllocLen"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLSPBuff"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLSPZeroRLT"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSpfRunTime"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSpfL1Nodes"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSpfL2Nodes"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSpfEventCount"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSpfLastTriggerLSPId"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSpfTriggerReason"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSpfType"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSummRowStatus"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSummLevel"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisInetRouteLevel"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisInetRouteSpfRunNumber"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisInetRouteMetric"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisInetRouteType"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisInetRouteNHopSysID"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisInetSummRowStatus"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisInetSummLevel"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisInetSummRouteTag"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisInetMtRouteLevel"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisInetMtRouteSpfRunNumber"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisInetMtRouteMetric"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisInetMtRouteType"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisInetMtRouteNHopSysID"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisInetMtRouteTag"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisInetMtRouteBkupFlags"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisInetMtRouteBkupNextHopTy"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisInetMtRouteBkupNextHop"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisInetMtRouteBkupMetric"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisRouteNextHopType"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisNextHopOwner"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisRouteNHOwnerAuxInfo"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisRouteBkupNHType"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisRouteBkupNHOwner"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisRouteBkupNHOwnAxInfo"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisMtPathMetric"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisMtPathSNPA"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisMtPathLfaIfIndex"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisMtPathLfaNHop"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisMtPathLfaMetric"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisMtPathLfaType"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisMtPathRouteType"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLfaNodesCovered"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLfaTotalNodes"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLfaNodeCoverage"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLfaIpv4NodesCovered"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLfaIpv4TotalNodes"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLfaIpv4Coverage"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLfaIpv6NodesCovered"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLfaIpv6TotalNodes"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLfaIpv6Coverage"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfRowStatus"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLastChangeTime"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfAdminState"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfOperState"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfCsnpInterval"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfHelloAuthKey"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfHelloAuthType"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLspPacingInterval"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfCircIndex"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfRetransmitInterval"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfTypeDefault"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfEnableBfd"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfIPv6Unicast"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfTeMetric"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfTeState"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfAdminGroup"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLdpSyncState"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLdpSyncMaxMetric"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLdpSyncTimerState"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLdpSyncTimeLeft"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfRouteTag"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfIpv6EnableBfd"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfHelloAuthentication"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLoopfreeAltExclude"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfOperType"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfIPv4Mcast"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfIPv6Mcast"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfBerState"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLevelLastChangeTime"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLevelHelloAuthKey"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLevelHelloAuthType"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLevelPassive"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLevelTeMetric"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLevelNumAdjacencies"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLevelISPriority"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLevelHelloTimer"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLevelAdminMetric"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLevelOperMetric"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLvlIPv6UcastAdmMet"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLvlIPv6UcastOperMet"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLvlIPv4McastAdmMetric"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLvlIPv6McastAdmMetric"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLevelLinkGroupName"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLevelSdOffset"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLevelSfOffset"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLvlIPv4McastOperMetric"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLvlIPv6McastOperMetric"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisISAdjExpiresIn"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisISAdjCircLevel"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisISAdjNeighborIP"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisISAdjRestartSupport"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisISAdjRestartStatus"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisISAdjRestartSupressed"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisISAdjNumRestarts"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisISAdjLastRestartTime"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisISAdjNeighborIPv6Type"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisISAdjNeighborIpv6"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisISAdjMtEnabled"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisISAdjMtId0"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisISAdjMtId2"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisISAdjMtId3"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisISAdjMtId4"))
)
if mibBuilder.loadTexts:
    vRtrIsisObsoletedV12v0Group.setStatus("current")

vRtrIsisLgV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 10, 2, 57)
)
vRtrIsisLgV12v0Group.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisLgRowStatus"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLgRowLastChanged"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLgTableLastChanged"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLgLevelOperMembers"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLgLevelRevertMembers"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLgLevelIPv4UcastMetric"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLgLevelIPv6UcastMetric"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLgLevelIPv4McastMetric"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLgLevelIPv6McastMetric"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLgLevelTableLastChanged"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLgLevelLastChanged"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLgLevelOpOperMembers"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLgLevelOperRevertMembers"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLgLevelOperMembersCount"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLgLevelOperActiveMembers"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLgLevelOperState"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLgLevelMembersOperState"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLgDescription"))
)
if mibBuilder.loadTexts:
    vRtrIsisLgV12v0Group.setStatus("current")


# Notification objects

vRtrIsisDatabaseOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 10, 0, 1)
)
vRtrIsisDatabaseOverload.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisSystemLevel"),
        ("ISIS-MIB", "isisSysL1State"),
        ("ISIS-MIB", "isisSysL2State"))
)
if mibBuilder.loadTexts:
    vRtrIsisDatabaseOverload.setStatus(
        "current"
    )

vRtrIsisManualAddressDrops = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 10, 0, 2)
)
vRtrIsisManualAddressDrops.setObjects(
    ("ISIS-MIB", "isisManAreaAddrExistState")
)
if mibBuilder.loadTexts:
    vRtrIsisManualAddressDrops.setStatus(
        "current"
    )

vRtrIsisCorruptedLSPDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 10, 0, 3)
)
vRtrIsisCorruptedLSPDetected.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisSystemLevel"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisTrapLSPID"))
)
if mibBuilder.loadTexts:
    vRtrIsisCorruptedLSPDetected.setStatus(
        "current"
    )

vRtrIsisMaxSeqExceedAttempt = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 10, 0, 4)
)
vRtrIsisMaxSeqExceedAttempt.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisSystemLevel"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisTrapLSPID"))
)
if mibBuilder.loadTexts:
    vRtrIsisMaxSeqExceedAttempt.setStatus(
        "current"
    )

vRtrIsisIDLenMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 10, 0, 5)
)
vRtrIsisIDLenMismatch.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisFieldLen"),
        ("TIMETRA-VRTR-MIB", "vRtrIfIndex"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisPDUFragment"))
)
if mibBuilder.loadTexts:
    vRtrIsisIDLenMismatch.setStatus(
        "current"
    )

vRtrIsisMaxAreaAddrsMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 10, 0, 6)
)
vRtrIsisMaxAreaAddrsMismatch.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisMaxAreaAddress"),
        ("TIMETRA-VRTR-MIB", "vRtrIfIndex"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisPDUFragment"))
)
if mibBuilder.loadTexts:
    vRtrIsisMaxAreaAddrsMismatch.setStatus(
        "current"
    )

vRtrIsisOwnLSPPurge = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 10, 0, 7)
)
vRtrIsisOwnLSPPurge.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrIfIndex"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisTrapLSPID"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSystemLevel"))
)
if mibBuilder.loadTexts:
    vRtrIsisOwnLSPPurge.setStatus(
        "current"
    )

vRtrIsisSequenceNumberSkip = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 10, 0, 8)
)
vRtrIsisSequenceNumberSkip.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisTrapLSPID"),
        ("TIMETRA-VRTR-MIB", "vRtrIfIndex"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSystemLevel"))
)
if mibBuilder.loadTexts:
    vRtrIsisSequenceNumberSkip.setStatus(
        "current"
    )

vRtrIsisAutTypeFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 10, 0, 9)
)
vRtrIsisAutTypeFail.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisSystemLevel"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisPDUFragment"),
        ("TIMETRA-VRTR-MIB", "vRtrIfIndex"))
)
if mibBuilder.loadTexts:
    vRtrIsisAutTypeFail.setStatus(
        "current"
    )

vRtrIsisAuthFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 10, 0, 10)
)
vRtrIsisAuthFail.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisSystemLevel"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisPDUFragment"),
        ("TIMETRA-VRTR-MIB", "vRtrIfIndex"))
)
if mibBuilder.loadTexts:
    vRtrIsisAuthFail.setStatus(
        "current"
    )

vRtrIsisVersionSkew = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 10, 0, 11)
)
vRtrIsisVersionSkew.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisProtocolVersion"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSystemLevel"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisPDUFragment"),
        ("TIMETRA-VRTR-MIB", "vRtrIfIndex"))
)
if mibBuilder.loadTexts:
    vRtrIsisVersionSkew.setStatus(
        "current"
    )

vRtrIsisAreaMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 10, 0, 12)
)
vRtrIsisAreaMismatch.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisLSPSize"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSystemLevel"),
        ("TIMETRA-VRTR-MIB", "vRtrIfIndex"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisPDUFragment"))
)
if mibBuilder.loadTexts:
    vRtrIsisAreaMismatch.setStatus(
        "current"
    )

vRtrIsisRejectedAdjacency = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 10, 0, 13)
)
vRtrIsisRejectedAdjacency.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisSystemLevel"),
        ("TIMETRA-VRTR-MIB", "vRtrIfIndex"))
)
if mibBuilder.loadTexts:
    vRtrIsisRejectedAdjacency.setStatus(
        "current"
    )

vRtrIsisLSPTooLargeToPropagate = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 10, 0, 14)
)
vRtrIsisLSPTooLargeToPropagate.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisLSPSize"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSystemLevel"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisTrapLSPID"),
        ("TIMETRA-VRTR-MIB", "vRtrIfIndex"))
)
if mibBuilder.loadTexts:
    vRtrIsisLSPTooLargeToPropagate.setStatus(
        "current"
    )

vRtrIsisOrigLSPBufSizeMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 10, 0, 15)
)
vRtrIsisOrigLSPBufSizeMismatch.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisOriginatingBufferSize"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSystemLevel"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisTrapLSPID"),
        ("TIMETRA-VRTR-MIB", "vRtrIfIndex"))
)
if mibBuilder.loadTexts:
    vRtrIsisOrigLSPBufSizeMismatch.setStatus(
        "current"
    )

vRtrIsisProtoSuppMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 10, 0, 16)
)
vRtrIsisProtoSuppMismatch.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisProtocolsSupported"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSystemLevel"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisTrapLSPID"),
        ("TIMETRA-VRTR-MIB", "vRtrIfIndex"))
)
if mibBuilder.loadTexts:
    vRtrIsisProtoSuppMismatch.setStatus(
        "current"
    )

vRtrIsisAdjacencyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 10, 0, 17)
)
vRtrIsisAdjacencyChange.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisSystemLevel"),
        ("TIMETRA-VRTR-MIB", "vRtrIfIndex"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisTrapLSPID"),
        ("ISIS-MIB", "isisISAdjState"))
)
if mibBuilder.loadTexts:
    vRtrIsisAdjacencyChange.setStatus(
        "current"
    )

vRtrIsisCircIdExhausted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 10, 0, 18)
)
vRtrIsisCircIdExhausted.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrIfIndex"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSystemLevel"))
)
if mibBuilder.loadTexts:
    vRtrIsisCircIdExhausted.setStatus(
        "current"
    )

vRtrIsisAdjRestartStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 10, 0, 19)
)
vRtrIsisAdjRestartStatusChange.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisSystemLevel"),
        ("TIMETRA-VRTR-MIB", "vRtrIfIndex"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisISAdjRestartStatus"))
)
if mibBuilder.loadTexts:
    vRtrIsisAdjRestartStatusChange.setStatus(
        "current"
    )

vRtrIsisLdpSyncTimerStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 10, 0, 20)
)
vRtrIsisLdpSyncTimerStarted.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrIfIndex"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLdpSyncTimerState"))
)
if mibBuilder.loadTexts:
    vRtrIsisLdpSyncTimerStarted.setStatus(
        "current"
    )

vRtrIsisLdpSyncExit = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 10, 0, 21)
)
vRtrIsisLdpSyncExit.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrIfIndex"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfLdpSyncTimerState"))
)
if mibBuilder.loadTexts:
    vRtrIsisLdpSyncExit.setStatus(
        "current"
    )

vRtrIsisExportLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 10, 0, 22)
)
vRtrIsisExportLimitReached.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisSystemLevel"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisExportLimit"))
)
if mibBuilder.loadTexts:
    vRtrIsisExportLimitReached.setStatus(
        "current"
    )

vRtrIsisExportLimitWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 10, 0, 23)
)
vRtrIsisExportLimitWarning.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisSystemLevel"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisExportLimit"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisExportLimitLogPercent"))
)
if mibBuilder.loadTexts:
    vRtrIsisExportLimitWarning.setStatus(
        "current"
    )

vRtrIsisRoutesExpLmtDropped = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 10, 0, 24)
)
vRtrIsisRoutesExpLmtDropped.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisSystemLevel"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisExportLimit"))
)
if mibBuilder.loadTexts:
    vRtrIsisRoutesExpLmtDropped.setStatus(
        "current"
    )

vRtrIsisSpbNbrMultAdjExists = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 10, 0, 25)
)
vRtrIsisSpbNbrMultAdjExists.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisSystemLevel"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisNbrSysId"))
)
if mibBuilder.loadTexts:
    vRtrIsisSpbNbrMultAdjExists.setStatus(
        "current"
    )

vRtrIsisSpbNbrMultAdjExistsClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 10, 0, 26)
)
vRtrIsisSpbNbrMultAdjExistsClear.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisSystemLevel"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisNbrSysId"))
)
if mibBuilder.loadTexts:
    vRtrIsisSpbNbrMultAdjExistsClear.setStatus(
        "current"
    )

vRtrSpbEctFidCfgChg = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 10, 0, 27)
)
vRtrSpbEctFidCfgChg.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrSpbEctFidStart"),
        ("TIMETRA-ISIS-MIB", "vRtrSpbEctFidEnd"),
        ("TIMETRA-ISIS-MIB", "vRtrSpbEctFidAlgorithm"))
)
if mibBuilder.loadTexts:
    vRtrSpbEctFidCfgChg.setStatus(
        "current"
    )

vRtrIsisFailureDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 10, 0, 28)
)
vRtrIsisFailureDisabled.setObjects(
    ("TIMETRA-ISIS-MIB", "vRtrIsisFailureReasonCode")
)
if mibBuilder.loadTexts:
    vRtrIsisFailureDisabled.setStatus(
        "obsolete"
    )


# Notifications groups

vRtrIsisNotificationV3v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 10, 2, 15)
)
vRtrIsisNotificationV3v0Group.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisDatabaseOverload"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisManualAddressDrops"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisCorruptedLSPDetected"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisMaxSeqExceedAttempt"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIDLenMismatch"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisMaxAreaAddrsMismatch"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisOwnLSPPurge"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSequenceNumberSkip"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisAutTypeFail"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisAuthFail"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisVersionSkew"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisAreaMismatch"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisRejectedAdjacency"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLSPTooLargeToPropagate"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisOrigLSPBufSizeMismatch"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisProtoSuppMismatch"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisAdjacencyChange"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisCircIdExhausted"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisAdjRestartStatusChange"))
)
if mibBuilder.loadTexts:
    vRtrIsisNotificationV3v0Group.setStatus(
        "current"
    )

vRtrIsisNotificationV6v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 10, 2, 30)
)
vRtrIsisNotificationV6v0Group.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisLdpSyncTimerStarted"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLdpSyncExit"))
)
if mibBuilder.loadTexts:
    vRtrIsisNotificationV6v0Group.setStatus(
        "current"
    )

vRtrIsisNotificationV7v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 10, 2, 36)
)
vRtrIsisNotificationV7v0Group.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisExportLimitReached"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisExportLimitWarning"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisRoutesExpLmtDropped"))
)
if mibBuilder.loadTexts:
    vRtrIsisNotificationV7v0Group.setStatus(
        "current"
    )

vRtrIsisNotifyV10v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 10, 2, 44)
)
vRtrIsisNotifyV10v0Group.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrSpbEctFidCfgChg"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSpbNbrMultAdjExists"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSpbNbrMultAdjExistsClear"))
)
if mibBuilder.loadTexts:
    vRtrIsisNotifyV10v0Group.setStatus(
        "current"
    )

vRtrIsisObsoleteNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 10, 2, 54)
)
vRtrIsisObsoleteNotifyGroup.setObjects(
    ("TIMETRA-ISIS-MIB", "vRtrIsisFailureDisabled")
)
if mibBuilder.loadTexts:
    vRtrIsisObsoleteNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

vRtrIsisMIBV4v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 10, 1, 4)
)
vRtrIsisMIBV4v0Compliance.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisV4v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisHostGroup"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisRouteV4v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLSPGroup"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfV4v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisAdjV4v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisNotificationV3v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSpfGroup"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisPathGroup"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSummaryV4v0Group"))
)
if mibBuilder.loadTexts:
    vRtrIsisMIBV4v0Compliance.setStatus(
        "obsolete"
    )

vRtrIsisMIBV5v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 10, 1, 5)
)
vRtrIsisMIBV5v0Compliance.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisV5v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisHostGroup"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisRouteV5v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLSPGroup"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfV5v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisAdjV5v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisNotificationV3v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSpfGroup"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisPathV5v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSummaryV4v0Group"))
)
if mibBuilder.loadTexts:
    vRtrIsisMIBV5v0Compliance.setStatus(
        "obsolete"
    )

vRtrIsisMIBV6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 10, 1, 6)
)
vRtrIsisMIBV6v0Compliance.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisV5v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisHostGroup"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisRouteV5v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLSPGroup"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfV5v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisAdjV5v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisNotificationV3v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSpfGroup"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisPathV5v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSummaryV4v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfV6v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisV6v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisNotificationV6v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLspMtuV6v0Group"))
)
if mibBuilder.loadTexts:
    vRtrIsisMIBV6v0Compliance.setStatus(
        "obsolete"
    )

vRtrIsisMIBV6v1Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 10, 1, 7)
)
vRtrIsisMIBV6v1Compliance.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisV5v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisHostGroup"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisRouteV5v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLSPGroup"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfV5v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisAdjV5v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisNotificationV3v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSpfGroup"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisPathV5v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSummaryV4v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfV6v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisV6v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisNotificationV6v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLspMtuV6v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisV6v1Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfV6v1Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSummaryV6v1Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisRouteV6v1Group"))
)
if mibBuilder.loadTexts:
    vRtrIsisMIBV6v1Compliance.setStatus(
        "obsolete"
    )

vRtrIsisMIBV7v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 10, 1, 8)
)
vRtrIsisMIBV7v0Compliance.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisV5v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisHostGroup"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisRouteV5v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLSPGroup"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfV5v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisAdjV5v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisNotificationV3v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSpfGroup"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisPathV5v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSummaryV4v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfV6v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisV6v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisNotificationV6v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLspMtuV6v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisV6v1Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfV6v1Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSummaryV6v1Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisRouteV6v1Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisV7v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisNotificationV7v0Group"))
)
if mibBuilder.loadTexts:
    vRtrIsisMIBV7v0Compliance.setStatus(
        "obsolete"
    )

vRtrIsisMIBV8v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 10, 1, 9)
)
vRtrIsisMIBV8v0Compliance.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisV5v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisHostGroup"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisRouteV5v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLSPGroup"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfV5v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisAdjV5v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisNotificationV3v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSpfGroup"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisPathV5v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSummaryV4v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfV6v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisV6v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisNotificationV6v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLspMtuV6v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisV6v1Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfV6v1Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSummaryV6v1Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisRouteV6v1Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisV7v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisNotificationV7v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisV8v0Group"))
)
if mibBuilder.loadTexts:
    vRtrIsisMIBV8v0Compliance.setStatus(
        "obsolete"
    )

vRtrIsisMIBV9v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 10, 1, 10)
)
vRtrIsisMIBV9v0Compliance.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisV5v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisHostGroup"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisRouteV5v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLSPGroup"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfV5v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisAdjV5v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisNotificationV3v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSpfGroup"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisPathV5v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSummaryV4v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfV6v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisV6v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisNotificationV6v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLspMtuV6v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisV6v1Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfV6v1Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSummaryV6v1Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisRouteV6v1Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisV7v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisNotificationV7v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisV8v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisV9v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfV9v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisV9v0R4Group"))
)
if mibBuilder.loadTexts:
    vRtrIsisMIBV9v0Compliance.setStatus(
        "obsolete"
    )

vRtrIsisMIBV10v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 10, 1, 11)
)
vRtrIsisMIBV10v0Compliance.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisV5v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisHostGroup"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisRouteV5v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLSPGroup"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfV5v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisAdjV5v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisNotificationV3v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSpfGroup"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisPathV5v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSummaryV4v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfV6v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisV6v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisNotificationV6v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLspMtuV6v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisV6v1Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfV6v1Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSummaryV6v1Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisRouteV6v1Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisV7v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisNotificationV7v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisV8v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisV9v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfV9v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisV9v0R4Group"),
        ("TIMETRA-ISIS-MIB", "vRtrSpbEctFidGroup"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisNotifyObjsV10v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisNotifyV10v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisV10v0Group"))
)
if mibBuilder.loadTexts:
    vRtrIsisMIBV10v0Compliance.setStatus(
        "obsolete"
    )

vRtrIsisMIBV11v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 10, 1, 12)
)
vRtrIsisMIBV11v0Compliance.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisV5v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisHostGroup"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisRouteV5v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLSPGroup"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfV5v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisAdjV5v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisNotificationV3v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSpfGroup"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisPathV5v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSummaryV4v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfV6v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisV6v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisNotificationV6v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLspMtuV6v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisV6v1Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfV6v1Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisSummaryV6v1Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisRouteV6v1Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisV7v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisNotificationV7v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisV8v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisV9v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisIfV9v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisV9v0R4Group"),
        ("TIMETRA-ISIS-MIB", "vRtrSpbEctFidGroup"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisNotifyObjsV10v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisNotifyV10v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisV10v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisV11v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisV11R4v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisOvrMaxMetricGroup"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLgGroup"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisRouterIdGroup"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLspGroup"))
)
if mibBuilder.loadTexts:
    vRtrIsisMIBV11v0Compliance.setStatus(
        "obsolete"
    )

vRtrIsisMIBV12v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 10, 1, 13)
)
vRtrIsisMIBV12v0Compliance.setObjects(
      *(("TIMETRA-ISIS-MIB", "vRtrIsisNotificationV3v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisNotificationV6v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisNotificationV7v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrSpbEctFidGroup"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisNotifyObjsV10v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisNotifyV10v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisLgV12v0Group"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisObsoletedV12v0Group"))
)
if mibBuilder.loadTexts:
    vRtrIsisMIBV12v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-ISIS-MIB",
    **{"TmnxLSPBuffSize": TmnxLSPBuffSize,
       "IsisRoutingTopology": IsisRoutingTopology,
       "timetraIsisMIBModule": timetraIsisMIBModule,
       "vRtrIsisMIBConformance": vRtrIsisMIBConformance,
       "vRtrIsisMIBConformances": vRtrIsisMIBConformances,
       "vRtrIsisMIBV4v0Compliance": vRtrIsisMIBV4v0Compliance,
       "vRtrIsisMIBV5v0Compliance": vRtrIsisMIBV5v0Compliance,
       "vRtrIsisMIBV6v0Compliance": vRtrIsisMIBV6v0Compliance,
       "vRtrIsisMIBV6v1Compliance": vRtrIsisMIBV6v1Compliance,
       "vRtrIsisMIBV7v0Compliance": vRtrIsisMIBV7v0Compliance,
       "vRtrIsisMIBV8v0Compliance": vRtrIsisMIBV8v0Compliance,
       "vRtrIsisMIBV9v0Compliance": vRtrIsisMIBV9v0Compliance,
       "vRtrIsisMIBV10v0Compliance": vRtrIsisMIBV10v0Compliance,
       "vRtrIsisMIBV11v0Compliance": vRtrIsisMIBV11v0Compliance,
       "vRtrIsisMIBV12v0Compliance": vRtrIsisMIBV12v0Compliance,
       "vRtrIsisMIBGroups": vRtrIsisMIBGroups,
       "vRtrIsisHostGroup": vRtrIsisHostGroup,
       "vRtrIsisPathGroup": vRtrIsisPathGroup,
       "vRtrIsisLSPGroup": vRtrIsisLSPGroup,
       "vRtrIsisNotificationObjGroup": vRtrIsisNotificationObjGroup,
       "vRtrIsisSpfGroup": vRtrIsisSpfGroup,
       "vRtrIsisNotificationV3v0Group": vRtrIsisNotificationV3v0Group,
       "vRtrIsisV4v0Group": vRtrIsisV4v0Group,
       "vRtrIsisRouteV4v0Group": vRtrIsisRouteV4v0Group,
       "vRtrIsisSummaryV4v0Group": vRtrIsisSummaryV4v0Group,
       "vRtrIsisAdjV4v0Group": vRtrIsisAdjV4v0Group,
       "vRtrIsisIfV4v0Group": vRtrIsisIfV4v0Group,
       "vRtrIsisV5v0Group": vRtrIsisV5v0Group,
       "vRtrIsisIfV5v0Group": vRtrIsisIfV5v0Group,
       "vRtrIsisRouteV5v0Group": vRtrIsisRouteV5v0Group,
       "vRtrIsisPathV5v0Group": vRtrIsisPathV5v0Group,
       "vRtrIsisObsoleteV5v0Group": vRtrIsisObsoleteV5v0Group,
       "vRtrIsisAdjV5v0Group": vRtrIsisAdjV5v0Group,
       "vRtrIsisLspMtuV6v0Group": vRtrIsisLspMtuV6v0Group,
       "vRtrIsisIfV6v0Group": vRtrIsisIfV6v0Group,
       "vRtrIsisV6v0Group": vRtrIsisV6v0Group,
       "vRtrIsisNotificationV6v0Group": vRtrIsisNotificationV6v0Group,
       "vRtrIsisV6v1Group": vRtrIsisV6v1Group,
       "vRtrIsisIfV6v1Group": vRtrIsisIfV6v1Group,
       "vRtrIsisSummaryV6v1Group": vRtrIsisSummaryV6v1Group,
       "vRtrIsisRouteV6v1Group": vRtrIsisRouteV6v1Group,
       "vRtrIsisV7v0Group": vRtrIsisV7v0Group,
       "vRtrIsisNotificationV7v0Group": vRtrIsisNotificationV7v0Group,
       "vRtrIsisV8v0Group": vRtrIsisV8v0Group,
       "vRtrIsisV9v0Group": vRtrIsisV9v0Group,
       "vRtrIsisIfV9v0Group": vRtrIsisIfV9v0Group,
       "vRtrIsisV9v0R4Group": vRtrIsisV9v0R4Group,
       "vRtrSpbEctFidGroup": vRtrSpbEctFidGroup,
       "vRtrIsisV10v0Group": vRtrIsisV10v0Group,
       "vRtrIsisNotifyObjsV10v0Group": vRtrIsisNotifyObjsV10v0Group,
       "vRtrIsisNotifyV10v0Group": vRtrIsisNotifyV10v0Group,
       "vRtrIsisV11v0Group": vRtrIsisV11v0Group,
       "vRtrIsisV11R4v0Group": vRtrIsisV11R4v0Group,
       "vRtrIsisOvrMaxMetricGroup": vRtrIsisOvrMaxMetricGroup,
       "vRtrIsisLgGroup": vRtrIsisLgGroup,
       "vRtrIsisRouterIdGroup": vRtrIsisRouterIdGroup,
       "vRtrIsisHelloPaddingGroup": vRtrIsisHelloPaddingGroup,
       "vRtrIsisLspGroup": vRtrIsisLspGroup,
       "vRtrIsisObsoleteNotifyObjsGroup": vRtrIsisObsoleteNotifyObjsGroup,
       "vRtrIsisObsoleteNotifyGroup": vRtrIsisObsoleteNotifyGroup,
       "vRtrIsisAdvRtrCapaGroup": vRtrIsisAdvRtrCapaGroup,
       "vRtrIsisObsoletedV12v0Group": vRtrIsisObsoletedV12v0Group,
       "vRtrIsisLgV12v0Group": vRtrIsisLgV12v0Group,
       "vRtrIsisMIBDCConformances": vRtrIsisMIBDCConformances,
       "vRtrIsisDCMIBGroups": vRtrIsisDCMIBGroups,
       "vRtrIsisObjs": vRtrIsisObjs,
       "vRtrIsisSystemObjs": vRtrIsisSystemObjs,
       "vRtrIsisTable": vRtrIsisTable,
       "vRtrIsisEntry": vRtrIsisEntry,
       "vRtrIsisLastEnabledTime": vRtrIsisLastEnabledTime,
       "vRtrIsisAuthKey": vRtrIsisAuthKey,
       "vRtrIsisAuthType": vRtrIsisAuthType,
       "vRtrIsisAuthCheck": vRtrIsisAuthCheck,
       "vRtrIsisExportPolicy1": vRtrIsisExportPolicy1,
       "vRtrIsisExportPolicy2": vRtrIsisExportPolicy2,
       "vRtrIsisExportPolicy3": vRtrIsisExportPolicy3,
       "vRtrIsisExportPolicy4": vRtrIsisExportPolicy4,
       "vRtrIsisExportPolicy5": vRtrIsisExportPolicy5,
       "vRtrIsisLspLifetime": vRtrIsisLspLifetime,
       "vRtrIsisOverloadTimeout": vRtrIsisOverloadTimeout,
       "vRtrIsisOperState": vRtrIsisOperState,
       "vRtrIsisReferenceBw": vRtrIsisReferenceBw,
       "vRtrIsisTrafficEng": vRtrIsisTrafficEng,
       "vRtrIsisShortCuts": vRtrIsisShortCuts,
       "vRtrIsisSpfHoldTime": vRtrIsisSpfHoldTime,
       "vRtrIsisLastSpfRun": vRtrIsisLastSpfRun,
       "vRtrIsisGracefulRestart": vRtrIsisGracefulRestart,
       "vRtrIsisOverloadOnBoot": vRtrIsisOverloadOnBoot,
       "vRtrIsisOverloadOnBootTimeout": vRtrIsisOverloadOnBootTimeout,
       "vRtrIsisSpfWait": vRtrIsisSpfWait,
       "vRtrIsisSpfInitialWait": vRtrIsisSpfInitialWait,
       "vRtrIsisSpfSecondWait": vRtrIsisSpfSecondWait,
       "vRtrIsisLspMaxWait": vRtrIsisLspMaxWait,
       "vRtrIsisLspInitialWait": vRtrIsisLspInitialWait,
       "vRtrIsisLspSecondWait": vRtrIsisLspSecondWait,
       "vRtrIsisCsnpAuthentication": vRtrIsisCsnpAuthentication,
       "vRtrIsisHelloAuthentication": vRtrIsisHelloAuthentication,
       "vRtrIsisPsnpAuthentication": vRtrIsisPsnpAuthentication,
       "vRtrIsisGRRestartDuration": vRtrIsisGRRestartDuration,
       "vRtrIsisGRHelperMode": vRtrIsisGRHelperMode,
       "vRtrIsisEnableIPv6": vRtrIsisEnableIPv6,
       "vRtrIsisEnableIPv4": vRtrIsisEnableIPv4,
       "vRtrIsisUnicastImport": vRtrIsisUnicastImport,
       "vRtrIsisMulticastImport": vRtrIsisMulticastImport,
       "vRtrIsisStrictAdjacencyCheck": vRtrIsisStrictAdjacencyCheck,
       "vRtrIsisManualSpfTrigger": vRtrIsisManualSpfTrigger,
       "vRtrIsisMultiTopology": vRtrIsisMultiTopology,
       "vRtrIsisMultiTopoIPv6Ucast": vRtrIsisMultiTopoIPv6Ucast,
       "vRtrIsisIPv6RoutingTopo": vRtrIsisIPv6RoutingTopo,
       "vRtrIsisSysOrigL1LSPBuffSize": vRtrIsisSysOrigL1LSPBuffSize,
       "vRtrIsisSysOrigL2LSPBuffSize": vRtrIsisSysOrigL2LSPBuffSize,
       "vRtrIsisLdpSyncAdminState": vRtrIsisLdpSyncAdminState,
       "vRtrIsisIPv6UnicastImport": vRtrIsisIPv6UnicastImport,
       "vRtrIsisIPv6MulticastImport": vRtrIsisIPv6MulticastImport,
       "vRtrIsisAdvertisePassiveOnly": vRtrIsisAdvertisePassiveOnly,
       "vRtrIsisDefaultRouteTag": vRtrIsisDefaultRouteTag,
       "vRtrIsisSuppressDefault": vRtrIsisSuppressDefault,
       "vRtrIsisLdpOverRsvp": vRtrIsisLdpOverRsvp,
       "vRtrIsisExportLimit": vRtrIsisExportLimit,
       "vRtrIsisExportLimitLogPercent": vRtrIsisExportLimitLogPercent,
       "vRtrIsisTotalL1ExportedRoutes": vRtrIsisTotalL1ExportedRoutes,
       "vRtrIsisTotalL2ExportedRoutes": vRtrIsisTotalL2ExportedRoutes,
       "vRtrIsisRsvpShortcut": vRtrIsisRsvpShortcut,
       "vRtrIsisAdvertiseTunnelLink": vRtrIsisAdvertiseTunnelLink,
       "vRtrIsisIidTlv": vRtrIsisIidTlv,
       "vRtrIsisL1MacAddress": vRtrIsisL1MacAddress,
       "vRtrIsisL2MacAddress": vRtrIsisL2MacAddress,
       "vRtrIsisSysOperL1LSPBuffSize": vRtrIsisSysOperL1LSPBuffSize,
       "vRtrIsisSysOperL2LSPBuffSize": vRtrIsisSysOperL2LSPBuffSize,
       "vRtrIsisLoopfreeAlternate": vRtrIsisLoopfreeAlternate,
       "vRtrIsisIPv4McastRoutingTopo": vRtrIsisIPv4McastRoutingTopo,
       "vRtrIsisIPv6McastRoutingTopo": vRtrIsisIPv6McastRoutingTopo,
       "vRtrIsisMultiTopoIPv4Mcast": vRtrIsisMultiTopoIPv4Mcast,
       "vRtrIsisMultiTopoIPv6Mcast": vRtrIsisMultiTopoIPv6Mcast,
       "vRtrIsisOverloadMaxMetric": vRtrIsisOverloadMaxMetric,
       "vRtrIsisOverloadOnBootMaxMetric": vRtrIsisOverloadOnBootMaxMetric,
       "vRtrIsisRouterId": vRtrIsisRouterId,
       "vRtrIsisAdvRtrCapability": vRtrIsisAdvRtrCapability,
       "vRtrIsisHelloPadding": vRtrIsisHelloPadding,
       "vRtrIsisOperRouterId": vRtrIsisOperRouterId,
       "vRtrIsisIgnoreLspErrors": vRtrIsisIgnoreLspErrors,
       "vRtrIsisLevelTable": vRtrIsisLevelTable,
       "vRtrIsisLevelEntry": vRtrIsisLevelEntry,
       "vRtrIsisLevel": vRtrIsisLevel,
       "vRtrIsisLevelAuthKey": vRtrIsisLevelAuthKey,
       "vRtrIsisLevelAuthType": vRtrIsisLevelAuthType,
       "vRtrIsisLevelExtPreference": vRtrIsisLevelExtPreference,
       "vRtrIsisLevelPreference": vRtrIsisLevelPreference,
       "vRtrIsisLevelWideMetricsOnly": vRtrIsisLevelWideMetricsOnly,
       "vRtrIsisLevelOverloadStatus": vRtrIsisLevelOverloadStatus,
       "vRtrIsisLevelOverloadTimeLeft": vRtrIsisLevelOverloadTimeLeft,
       "vRtrIsisLevelNumLSPs": vRtrIsisLevelNumLSPs,
       "vRtrIsisLevelCsnpAuthentication": vRtrIsisLevelCsnpAuthentication,
       "vRtrIsisLevelHelloAuthentication": vRtrIsisLevelHelloAuthentication,
       "vRtrIsisLevelPsnpAuthentication": vRtrIsisLevelPsnpAuthentication,
       "vRtrIsisLevelDefMetric": vRtrIsisLevelDefMetric,
       "vRtrIsisLevelIPv6DefMetric": vRtrIsisLevelIPv6DefMetric,
       "vRtrIsisLevelLoopfreeAltExclude": vRtrIsisLevelLoopfreeAltExclude,
       "vRtrIsisLevelDefIPv4McastMetric": vRtrIsisLevelDefIPv4McastMetric,
       "vRtrIsisLevelDefIPv6McastMetric": vRtrIsisLevelDefIPv6McastMetric,
       "vRtrIsisLevelAdvRtrCapability": vRtrIsisLevelAdvRtrCapability,
       "vRtrIsisStatsTable": vRtrIsisStatsTable,
       "vRtrIsisStatsEntry": vRtrIsisStatsEntry,
       "vRtrIsisSpfRuns": vRtrIsisSpfRuns,
       "vRtrIsisLSPRegenerations": vRtrIsisLSPRegenerations,
       "vRtrIsisInitiatedPurges": vRtrIsisInitiatedPurges,
       "vRtrIsisLSPRecd": vRtrIsisLSPRecd,
       "vRtrIsisLSPDrop": vRtrIsisLSPDrop,
       "vRtrIsisLSPSent": vRtrIsisLSPSent,
       "vRtrIsisLSPRetrans": vRtrIsisLSPRetrans,
       "vRtrIsisIIHRecd": vRtrIsisIIHRecd,
       "vRtrIsisIIHDrop": vRtrIsisIIHDrop,
       "vRtrIsisIIHSent": vRtrIsisIIHSent,
       "vRtrIsisIIHRetrans": vRtrIsisIIHRetrans,
       "vRtrIsisCSNPRecd": vRtrIsisCSNPRecd,
       "vRtrIsisCSNPDrop": vRtrIsisCSNPDrop,
       "vRtrIsisCSNPSent": vRtrIsisCSNPSent,
       "vRtrIsisCSNPRetrans": vRtrIsisCSNPRetrans,
       "vRtrIsisPSNPRecd": vRtrIsisPSNPRecd,
       "vRtrIsisPSNPDrop": vRtrIsisPSNPDrop,
       "vRtrIsisPSNPSent": vRtrIsisPSNPSent,
       "vRtrIsisPSNPRetrans": vRtrIsisPSNPRetrans,
       "vRtrIsisUnknownRecd": vRtrIsisUnknownRecd,
       "vRtrIsisUnknownDrop": vRtrIsisUnknownDrop,
       "vRtrIsisUnknownSent": vRtrIsisUnknownSent,
       "vRtrIsisUnknownRetrans": vRtrIsisUnknownRetrans,
       "vRtrIsisCSPFRequests": vRtrIsisCSPFRequests,
       "vRtrIsisCSPFDroppedRequests": vRtrIsisCSPFDroppedRequests,
       "vRtrIsisCSPFPathsFound": vRtrIsisCSPFPathsFound,
       "vRtrIsisCSPFPathsNotFound": vRtrIsisCSPFPathsNotFound,
       "vRtrIsisLfaRuns": vRtrIsisLfaRuns,
       "vRtrIsisHostnameTable": vRtrIsisHostnameTable,
       "vRtrIsisHostnameEntry": vRtrIsisHostnameEntry,
       "vRtrIsisSysID": vRtrIsisSysID,
       "vRtrIsisHostname": vRtrIsisHostname,
       "vRtrIsisRouteTable": vRtrIsisRouteTable,
       "vRtrIsisRouteEntry": vRtrIsisRouteEntry,
       "vRtrIsisRouteDest": vRtrIsisRouteDest,
       "vRtrIsisRouteMask": vRtrIsisRouteMask,
       "vRtrIsisRouteNexthopIP": vRtrIsisRouteNexthopIP,
       "vRtrIsisRouteLevel": vRtrIsisRouteLevel,
       "vRtrIsisRouteSpfVersion": vRtrIsisRouteSpfVersion,
       "vRtrIsisRouteMetric": vRtrIsisRouteMetric,
       "vRtrIsisRouteType": vRtrIsisRouteType,
       "vRtrIsisRouteNHopSysID": vRtrIsisRouteNHopSysID,
       "vRtrIsisPathTable": vRtrIsisPathTable,
       "vRtrIsisPathEntry": vRtrIsisPathEntry,
       "vRtrIsisPathID": vRtrIsisPathID,
       "vRtrIsisPathIfIndex": vRtrIsisPathIfIndex,
       "vRtrIsisPathNHopSysID": vRtrIsisPathNHopSysID,
       "vRtrIsisPathMetric": vRtrIsisPathMetric,
       "vRtrIsisPathSNPA": vRtrIsisPathSNPA,
       "vRtrIsisPathLfaIfIndex": vRtrIsisPathLfaIfIndex,
       "vRtrIsisPathLfaNHop": vRtrIsisPathLfaNHop,
       "vRtrIsisPathLfaMetric": vRtrIsisPathLfaMetric,
       "vRtrIsisPathLfaType": vRtrIsisPathLfaType,
       "vRtrIsisPathRouteType": vRtrIsisPathRouteType,
       "vRtrIsisLSPTable": vRtrIsisLSPTable,
       "vRtrIsisLSPEntry": vRtrIsisLSPEntry,
       "vRtrIsisLSPId": vRtrIsisLSPId,
       "vRtrIsisLSPSeq": vRtrIsisLSPSeq,
       "vRtrIsisLSPChecksum": vRtrIsisLSPChecksum,
       "vRtrIsisLSPLifetimeRemain": vRtrIsisLSPLifetimeRemain,
       "vRtrIsisLSPVersion": vRtrIsisLSPVersion,
       "vRtrIsisLSPPktType": vRtrIsisLSPPktType,
       "vRtrIsisLSPPktVersion": vRtrIsisLSPPktVersion,
       "vRtrIsisLSPMaxArea": vRtrIsisLSPMaxArea,
       "vRtrIsisLSPSysIdLen": vRtrIsisLSPSysIdLen,
       "vRtrIsisLSPAttributes": vRtrIsisLSPAttributes,
       "vRtrIsisLSPUsedLen": vRtrIsisLSPUsedLen,
       "vRtrIsisLSPAllocLen": vRtrIsisLSPAllocLen,
       "vRtrIsisLSPBuff": vRtrIsisLSPBuff,
       "vRtrIsisLSPZeroRLT": vRtrIsisLSPZeroRLT,
       "vRtrIsisSpfLogTable": vRtrIsisSpfLogTable,
       "vRtrIsisSpfLogEntry": vRtrIsisSpfLogEntry,
       "vRtrIsisSpfTimeStamp": vRtrIsisSpfTimeStamp,
       "vRtrIsisSpfRunTime": vRtrIsisSpfRunTime,
       "vRtrIsisSpfL1Nodes": vRtrIsisSpfL1Nodes,
       "vRtrIsisSpfL2Nodes": vRtrIsisSpfL2Nodes,
       "vRtrIsisSpfEventCount": vRtrIsisSpfEventCount,
       "vRtrIsisSpfLastTriggerLSPId": vRtrIsisSpfLastTriggerLSPId,
       "vRtrIsisSpfTriggerReason": vRtrIsisSpfTriggerReason,
       "vRtrIsisSpfType": vRtrIsisSpfType,
       "vRtrIsisSummaryTable": vRtrIsisSummaryTable,
       "vRtrIsisSummaryEntry": vRtrIsisSummaryEntry,
       "vRtrIsisSummPrefix": vRtrIsisSummPrefix,
       "vRtrIsisSummMask": vRtrIsisSummMask,
       "vRtrIsisSummRowStatus": vRtrIsisSummRowStatus,
       "vRtrIsisSummLevel": vRtrIsisSummLevel,
       "vRtrIsisInetRouteTable": vRtrIsisInetRouteTable,
       "vRtrIsisInetRouteEntry": vRtrIsisInetRouteEntry,
       "vRtrIsisInetRouteDestType": vRtrIsisInetRouteDestType,
       "vRtrIsisInetRouteDest": vRtrIsisInetRouteDest,
       "vRtrIsisInetRoutePrefixLength": vRtrIsisInetRoutePrefixLength,
       "vRtrIsisInetRouteNexthopIPType": vRtrIsisInetRouteNexthopIPType,
       "vRtrIsisInetRouteNexthopIP": vRtrIsisInetRouteNexthopIP,
       "vRtrIsisInetRouteLevel": vRtrIsisInetRouteLevel,
       "vRtrIsisInetRouteSpfRunNumber": vRtrIsisInetRouteSpfRunNumber,
       "vRtrIsisInetRouteMetric": vRtrIsisInetRouteMetric,
       "vRtrIsisInetRouteType": vRtrIsisInetRouteType,
       "vRtrIsisInetRouteNHopSysID": vRtrIsisInetRouteNHopSysID,
       "vRtrIsisInetSummaryTable": vRtrIsisInetSummaryTable,
       "vRtrIsisInetSummaryEntry": vRtrIsisInetSummaryEntry,
       "vRtrIsisInetSummPrefixType": vRtrIsisInetSummPrefixType,
       "vRtrIsisInetSummPrefix": vRtrIsisInetSummPrefix,
       "vRtrIsisInetSummPrefixLength": vRtrIsisInetSummPrefixLength,
       "vRtrIsisInetSummRowStatus": vRtrIsisInetSummRowStatus,
       "vRtrIsisInetSummLevel": vRtrIsisInetSummLevel,
       "vRtrIsisInetSummRouteTag": vRtrIsisInetSummRouteTag,
       "vRtrIsisInetMtRouteTable": vRtrIsisInetMtRouteTable,
       "vRtrIsisInetMtRouteEntry": vRtrIsisInetMtRouteEntry,
       "vRtrIsisInetMtRouteMtId": vRtrIsisInetMtRouteMtId,
       "vRtrIsisInetMtRouteDestType": vRtrIsisInetMtRouteDestType,
       "vRtrIsisInetMtRouteDest": vRtrIsisInetMtRouteDest,
       "vRtrIsisInetMtRoutePrefixLength": vRtrIsisInetMtRoutePrefixLength,
       "vRtrIsisInetMtRouteNexthopIPType": vRtrIsisInetMtRouteNexthopIPType,
       "vRtrIsisInetMtRouteNexthopIP": vRtrIsisInetMtRouteNexthopIP,
       "vRtrIsisInetMtRouteLevel": vRtrIsisInetMtRouteLevel,
       "vRtrIsisInetMtRouteSpfRunNumber": vRtrIsisInetMtRouteSpfRunNumber,
       "vRtrIsisInetMtRouteMetric": vRtrIsisInetMtRouteMetric,
       "vRtrIsisInetMtRouteType": vRtrIsisInetMtRouteType,
       "vRtrIsisInetMtRouteNHopSysID": vRtrIsisInetMtRouteNHopSysID,
       "vRtrIsisInetMtRouteTag": vRtrIsisInetMtRouteTag,
       "vRtrIsisInetMtRouteBkupFlags": vRtrIsisInetMtRouteBkupFlags,
       "vRtrIsisInetMtRouteBkupNextHopTy": vRtrIsisInetMtRouteBkupNextHopTy,
       "vRtrIsisInetMtRouteBkupNextHop": vRtrIsisInetMtRouteBkupNextHop,
       "vRtrIsisInetMtRouteBkupMetric": vRtrIsisInetMtRouteBkupMetric,
       "vRtrIsisRouteNextHopType": vRtrIsisRouteNextHopType,
       "vRtrIsisNextHopOwner": vRtrIsisNextHopOwner,
       "vRtrIsisRouteNHOwnerAuxInfo": vRtrIsisRouteNHOwnerAuxInfo,
       "vRtrIsisRouteBkupNHType": vRtrIsisRouteBkupNHType,
       "vRtrIsisRouteBkupNHOwner": vRtrIsisRouteBkupNHOwner,
       "vRtrIsisRouteBkupNHOwnAxInfo": vRtrIsisRouteBkupNHOwnAxInfo,
       "vRtrIsisMtPathTable": vRtrIsisMtPathTable,
       "vRtrIsisMtPathEntry": vRtrIsisMtPathEntry,
       "vRtrIsisMtPathMtID": vRtrIsisMtPathMtID,
       "vRtrIsisMtPathID": vRtrIsisMtPathID,
       "vRtrIsisMtPathIfIndex": vRtrIsisMtPathIfIndex,
       "vRtrIsisMtPathNHopSysID": vRtrIsisMtPathNHopSysID,
       "vRtrIsisMtPathMetric": vRtrIsisMtPathMetric,
       "vRtrIsisMtPathSNPA": vRtrIsisMtPathSNPA,
       "vRtrIsisMtPathLfaIfIndex": vRtrIsisMtPathLfaIfIndex,
       "vRtrIsisMtPathLfaNHop": vRtrIsisMtPathLfaNHop,
       "vRtrIsisMtPathLfaMetric": vRtrIsisMtPathLfaMetric,
       "vRtrIsisMtPathLfaType": vRtrIsisMtPathLfaType,
       "vRtrIsisMtPathRouteType": vRtrIsisMtPathRouteType,
       "vRtrIsisLfaTable": vRtrIsisLfaTable,
       "vRtrIsisLfaEntry": vRtrIsisLfaEntry,
       "vRtrIsisLfaFamilyCoverage": vRtrIsisLfaFamilyCoverage,
       "vRtrIsisLfaNodesCovered": vRtrIsisLfaNodesCovered,
       "vRtrIsisLfaTotalNodes": vRtrIsisLfaTotalNodes,
       "vRtrIsisLfaNodeCoverage": vRtrIsisLfaNodeCoverage,
       "vRtrIsisLfaIpv4NodesCovered": vRtrIsisLfaIpv4NodesCovered,
       "vRtrIsisLfaIpv4TotalNodes": vRtrIsisLfaIpv4TotalNodes,
       "vRtrIsisLfaIpv4Coverage": vRtrIsisLfaIpv4Coverage,
       "vRtrIsisLfaIpv6NodesCovered": vRtrIsisLfaIpv6NodesCovered,
       "vRtrIsisLfaIpv6TotalNodes": vRtrIsisLfaIpv6TotalNodes,
       "vRtrIsisLfaIpv6Coverage": vRtrIsisLfaIpv6Coverage,
       "vRtrSpbEctFidTableLastChanged": vRtrSpbEctFidTableLastChanged,
       "vRtrSpbEctFidTable": vRtrSpbEctFidTable,
       "vRtrSpbEctFidEntry": vRtrSpbEctFidEntry,
       "vRtrSpbEctFid": vRtrSpbEctFid,
       "vRtrSpbEctFidLastChanged": vRtrSpbEctFidLastChanged,
       "vRtrSpbEctFidAlgorithm": vRtrSpbEctFidAlgorithm,
       "vRtrSpbPathTable": vRtrSpbPathTable,
       "vRtrSpbPathEntry": vRtrSpbPathEntry,
       "vRtrSpbPathFwdTree": vRtrSpbPathFwdTree,
       "vRtrSpbPathIfIndex": vRtrSpbPathIfIndex,
       "vRtrSpbPathNHopSysID": vRtrSpbPathNHopSysID,
       "vRtrSpbPathMetric": vRtrSpbPathMetric,
       "vRtrSpbPathSNPA": vRtrSpbPathSNPA,
       "vRtrSpbRouteMacTable": vRtrSpbRouteMacTable,
       "vRtrSpbRouteMacEntry": vRtrSpbRouteMacEntry,
       "vRtrSpbRouteMacDestMac": vRtrSpbRouteMacDestMac,
       "vRtrSpbRouteMacIfIndex": vRtrSpbRouteMacIfIndex,
       "vRtrSpbRouteMacSpfRunNumber": vRtrSpbRouteMacSpfRunNumber,
       "vRtrSpbRouteMacMetric": vRtrSpbRouteMacMetric,
       "vRtrSpbRouteMacNHopSysID": vRtrSpbRouteMacNHopSysID,
       "vRtrSpbRouteMacMetricType": vRtrSpbRouteMacMetricType,
       "vRtrSpbRouteIsidTable": vRtrSpbRouteIsidTable,
       "vRtrSpbRouteIsidEntry": vRtrSpbRouteIsidEntry,
       "vRtrSpbRouteIsidDestIsid": vRtrSpbRouteIsidDestIsid,
       "vRtrSpbRouteIsidIfIndex": vRtrSpbRouteIsidIfIndex,
       "vRtrSpbRouteIsidSpfRunNumber": vRtrSpbRouteIsidSpfRunNumber,
       "vRtrSpbRouteIsidNHopSysID": vRtrSpbRouteIsidNHopSysID,
       "vRtrSpbRouteIsidInMfib": vRtrSpbRouteIsidInMfib,
       "vRtrSpbEctFidRangeTable": vRtrSpbEctFidRangeTable,
       "vRtrSpbEctFidRangeEntry": vRtrSpbEctFidRangeEntry,
       "vRtrSpbEctFidRangeEnd": vRtrSpbEctFidRangeEnd,
       "vRtrSpbEctFidRangeAlgorithm": vRtrSpbEctFidRangeAlgorithm,
       "vRtrIsisLgTableLastChanged": vRtrIsisLgTableLastChanged,
       "vRtrIsisLgTable": vRtrIsisLgTable,
       "vRtrIsisLgEntry": vRtrIsisLgEntry,
       "vRtrIsisLgName": vRtrIsisLgName,
       "vRtrIsisLgRowStatus": vRtrIsisLgRowStatus,
       "vRtrIsisLgDescription": vRtrIsisLgDescription,
       "vRtrIsisLgRowLastChanged": vRtrIsisLgRowLastChanged,
       "vRtrIsisLgLevelTableLastChanged": vRtrIsisLgLevelTableLastChanged,
       "vRtrIsisLgLevelTable": vRtrIsisLgLevelTable,
       "vRtrIsisLgLevelEntry": vRtrIsisLgLevelEntry,
       "vRtrIsisLgLevelLvl": vRtrIsisLgLevelLvl,
       "vRtrIsisLgLevelOperMembers": vRtrIsisLgLevelOperMembers,
       "vRtrIsisLgLevelRevertMembers": vRtrIsisLgLevelRevertMembers,
       "vRtrIsisLgLevelIPv4UcastMetric": vRtrIsisLgLevelIPv4UcastMetric,
       "vRtrIsisLgLevelIPv6UcastMetric": vRtrIsisLgLevelIPv6UcastMetric,
       "vRtrIsisLgLevelIPv4McastMetric": vRtrIsisLgLevelIPv4McastMetric,
       "vRtrIsisLgLevelIPv6McastMetric": vRtrIsisLgLevelIPv6McastMetric,
       "vRtrIsisLgLevelLastChanged": vRtrIsisLgLevelLastChanged,
       "vRtrIsisLgLevelOperTable": vRtrIsisLgLevelOperTable,
       "vRtrIsisLgLevelOperEntry": vRtrIsisLgLevelOperEntry,
       "vRtrIsisLgLevelOpOperMembers": vRtrIsisLgLevelOpOperMembers,
       "vRtrIsisLgLevelOperRevertMembers": vRtrIsisLgLevelOperRevertMembers,
       "vRtrIsisLgLevelOperMembersCount": vRtrIsisLgLevelOperMembersCount,
       "vRtrIsisLgLevelOperActiveMembers": vRtrIsisLgLevelOperActiveMembers,
       "vRtrIsisLgLevelOperState": vRtrIsisLgLevelOperState,
       "vRtrIsisLgLevelMembersOperTable": vRtrIsisLgLevelMembersOperTable,
       "vRtrIsisLgLevelMembersOperEntry": vRtrIsisLgLevelMembersOperEntry,
       "vRtrIsisLgLevelMembersOperState": vRtrIsisLgLevelMembersOperState,
       "vRtrIsisIfObjs": vRtrIsisIfObjs,
       "vRtrIsisIfTable": vRtrIsisIfTable,
       "vRtrIsisIfEntry": vRtrIsisIfEntry,
       "vRtrIsisIfRowStatus": vRtrIsisIfRowStatus,
       "vRtrIsisIfLastChangeTime": vRtrIsisIfLastChangeTime,
       "vRtrIsisIfAdminState": vRtrIsisIfAdminState,
       "vRtrIsisIfOperState": vRtrIsisIfOperState,
       "vRtrIsisIfCsnpInterval": vRtrIsisIfCsnpInterval,
       "vRtrIsisIfHelloAuthKey": vRtrIsisIfHelloAuthKey,
       "vRtrIsisIfHelloAuthType": vRtrIsisIfHelloAuthType,
       "vRtrIsisIfLspPacingInterval": vRtrIsisIfLspPacingInterval,
       "vRtrIsisIfCircIndex": vRtrIsisIfCircIndex,
       "vRtrIsisIfRetransmitInterval": vRtrIsisIfRetransmitInterval,
       "vRtrIsisIfTypeDefault": vRtrIsisIfTypeDefault,
       "vRtrIsisIfEnableBfd": vRtrIsisIfEnableBfd,
       "vRtrIsisIfIPv6Unicast": vRtrIsisIfIPv6Unicast,
       "vRtrIsisIfTeMetric": vRtrIsisIfTeMetric,
       "vRtrIsisIfTeState": vRtrIsisIfTeState,
       "vRtrIsisIfAdminGroup": vRtrIsisIfAdminGroup,
       "vRtrIsisIfLdpSyncState": vRtrIsisIfLdpSyncState,
       "vRtrIsisIfLdpSyncMaxMetric": vRtrIsisIfLdpSyncMaxMetric,
       "vRtrIsisIfLdpSyncTimerState": vRtrIsisIfLdpSyncTimerState,
       "vRtrIsisIfLdpSyncTimeLeft": vRtrIsisIfLdpSyncTimeLeft,
       "vRtrIsisIfRouteTag": vRtrIsisIfRouteTag,
       "vRtrIsisIfIpv6EnableBfd": vRtrIsisIfIpv6EnableBfd,
       "vRtrIsisIfHelloAuthentication": vRtrIsisIfHelloAuthentication,
       "vRtrIsisIfLoopfreeAltExclude": vRtrIsisIfLoopfreeAltExclude,
       "vRtrIsisIfOperType": vRtrIsisIfOperType,
       "vRtrIsisIfIPv4Mcast": vRtrIsisIfIPv4Mcast,
       "vRtrIsisIfIPv6Mcast": vRtrIsisIfIPv6Mcast,
       "vRtrIsisIfBerState": vRtrIsisIfBerState,
       "vRtrIsisIfLevelTable": vRtrIsisIfLevelTable,
       "vRtrIsisIfLevelEntry": vRtrIsisIfLevelEntry,
       "vRtrIsisIfLevel": vRtrIsisIfLevel,
       "vRtrIsisIfLevelLastChangeTime": vRtrIsisIfLevelLastChangeTime,
       "vRtrIsisIfLevelHelloAuthKey": vRtrIsisIfLevelHelloAuthKey,
       "vRtrIsisIfLevelHelloAuthType": vRtrIsisIfLevelHelloAuthType,
       "vRtrIsisIfLevelPassive": vRtrIsisIfLevelPassive,
       "vRtrIsisIfLevelTeMetric": vRtrIsisIfLevelTeMetric,
       "vRtrIsisIfLevelNumAdjacencies": vRtrIsisIfLevelNumAdjacencies,
       "vRtrIsisIfLevelISPriority": vRtrIsisIfLevelISPriority,
       "vRtrIsisIfLevelHelloTimer": vRtrIsisIfLevelHelloTimer,
       "vRtrIsisIfLevelAdminMetric": vRtrIsisIfLevelAdminMetric,
       "vRtrIsisIfLevelOperMetric": vRtrIsisIfLevelOperMetric,
       "vRtrIsisIfLvlIPv6UcastAdmMet": vRtrIsisIfLvlIPv6UcastAdmMet,
       "vRtrIsisIfLvlIPv6UcastOperMet": vRtrIsisIfLvlIPv6UcastOperMet,
       "vRtrIsisIfLvlIPv4McastAdmMetric": vRtrIsisIfLvlIPv4McastAdmMetric,
       "vRtrIsisIfLvlIPv6McastAdmMetric": vRtrIsisIfLvlIPv6McastAdmMetric,
       "vRtrIsisIfLevelLinkGroupName": vRtrIsisIfLevelLinkGroupName,
       "vRtrIsisIfLevelSdOffset": vRtrIsisIfLevelSdOffset,
       "vRtrIsisIfLevelSfOffset": vRtrIsisIfLevelSfOffset,
       "vRtrIsisIfLvlIPv4McastOperMetric": vRtrIsisIfLvlIPv4McastOperMetric,
       "vRtrIsisIfLvlIPv6McastOperMetric": vRtrIsisIfLvlIPv6McastOperMetric,
       "vRtrIsisAdjObjs": vRtrIsisAdjObjs,
       "vRtrIsisISAdjTable": vRtrIsisISAdjTable,
       "vRtrIsisISAdjEntry": vRtrIsisISAdjEntry,
       "vRtrIsisISAdjExpiresIn": vRtrIsisISAdjExpiresIn,
       "vRtrIsisISAdjCircLevel": vRtrIsisISAdjCircLevel,
       "vRtrIsisISAdjNeighborIP": vRtrIsisISAdjNeighborIP,
       "vRtrIsisISAdjRestartSupport": vRtrIsisISAdjRestartSupport,
       "vRtrIsisISAdjRestartStatus": vRtrIsisISAdjRestartStatus,
       "vRtrIsisISAdjRestartSupressed": vRtrIsisISAdjRestartSupressed,
       "vRtrIsisISAdjNumRestarts": vRtrIsisISAdjNumRestarts,
       "vRtrIsisISAdjLastRestartTime": vRtrIsisISAdjLastRestartTime,
       "vRtrIsisISAdjNeighborIPv6Type": vRtrIsisISAdjNeighborIPv6Type,
       "vRtrIsisISAdjNeighborIpv6": vRtrIsisISAdjNeighborIpv6,
       "vRtrIsisISAdjMtEnabled": vRtrIsisISAdjMtEnabled,
       "vRtrIsisISAdjMtId0": vRtrIsisISAdjMtId0,
       "vRtrIsisISAdjMtId2": vRtrIsisISAdjMtId2,
       "vRtrIsisISAdjMtId3": vRtrIsisISAdjMtId3,
       "vRtrIsisISAdjMtId4": vRtrIsisISAdjMtId4,
       "vRtrIsisNotificationObjs": vRtrIsisNotificationObjs,
       "vRtrIsisNotificationTable": vRtrIsisNotificationTable,
       "vRtrIsisNotificationEntry": vRtrIsisNotificationEntry,
       "vRtrIsisTrapLSPID": vRtrIsisTrapLSPID,
       "vRtrIsisSystemLevel": vRtrIsisSystemLevel,
       "vRtrIsisPDUFragment": vRtrIsisPDUFragment,
       "vRtrIsisFieldLen": vRtrIsisFieldLen,
       "vRtrIsisMaxAreaAddress": vRtrIsisMaxAreaAddress,
       "vRtrIsisProtocolVersion": vRtrIsisProtocolVersion,
       "vRtrIsisLSPSize": vRtrIsisLSPSize,
       "vRtrIsisOriginatingBufferSize": vRtrIsisOriginatingBufferSize,
       "vRtrIsisProtocolsSupported": vRtrIsisProtocolsSupported,
       "vRtrIsisNbrSysId": vRtrIsisNbrSysId,
       "vRtrSpbEctFidStart": vRtrSpbEctFidStart,
       "vRtrSpbEctFidEnd": vRtrSpbEctFidEnd,
       "vRtrIsisFailureReasonCode": vRtrIsisFailureReasonCode,
       "vRtrIsisNotifyPrefix": vRtrIsisNotifyPrefix,
       "vRtrIsisNotifications": vRtrIsisNotifications,
       "vRtrIsisDatabaseOverload": vRtrIsisDatabaseOverload,
       "vRtrIsisManualAddressDrops": vRtrIsisManualAddressDrops,
       "vRtrIsisCorruptedLSPDetected": vRtrIsisCorruptedLSPDetected,
       "vRtrIsisMaxSeqExceedAttempt": vRtrIsisMaxSeqExceedAttempt,
       "vRtrIsisIDLenMismatch": vRtrIsisIDLenMismatch,
       "vRtrIsisMaxAreaAddrsMismatch": vRtrIsisMaxAreaAddrsMismatch,
       "vRtrIsisOwnLSPPurge": vRtrIsisOwnLSPPurge,
       "vRtrIsisSequenceNumberSkip": vRtrIsisSequenceNumberSkip,
       "vRtrIsisAutTypeFail": vRtrIsisAutTypeFail,
       "vRtrIsisAuthFail": vRtrIsisAuthFail,
       "vRtrIsisVersionSkew": vRtrIsisVersionSkew,
       "vRtrIsisAreaMismatch": vRtrIsisAreaMismatch,
       "vRtrIsisRejectedAdjacency": vRtrIsisRejectedAdjacency,
       "vRtrIsisLSPTooLargeToPropagate": vRtrIsisLSPTooLargeToPropagate,
       "vRtrIsisOrigLSPBufSizeMismatch": vRtrIsisOrigLSPBufSizeMismatch,
       "vRtrIsisProtoSuppMismatch": vRtrIsisProtoSuppMismatch,
       "vRtrIsisAdjacencyChange": vRtrIsisAdjacencyChange,
       "vRtrIsisCircIdExhausted": vRtrIsisCircIdExhausted,
       "vRtrIsisAdjRestartStatusChange": vRtrIsisAdjRestartStatusChange,
       "vRtrIsisLdpSyncTimerStarted": vRtrIsisLdpSyncTimerStarted,
       "vRtrIsisLdpSyncExit": vRtrIsisLdpSyncExit,
       "vRtrIsisExportLimitReached": vRtrIsisExportLimitReached,
       "vRtrIsisExportLimitWarning": vRtrIsisExportLimitWarning,
       "vRtrIsisRoutesExpLmtDropped": vRtrIsisRoutesExpLmtDropped,
       "vRtrIsisSpbNbrMultAdjExists": vRtrIsisSpbNbrMultAdjExists,
       "vRtrIsisSpbNbrMultAdjExistsClear": vRtrIsisSpbNbrMultAdjExistsClear,
       "vRtrSpbEctFidCfgChg": vRtrSpbEctFidCfgChg,
       "vRtrIsisFailureDisabled": vRtrIsisFailureDisabled}
)
