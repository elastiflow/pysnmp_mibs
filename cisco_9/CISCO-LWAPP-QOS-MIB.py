# SNMP MIB module (CISCO-LWAPP-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-LWAPP-QOS-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:55:05 2025
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

(cLApDot11IfEntry,
 cLApDot11IfSlotId,
 cLApDot11IfType,
 cLApName,
 cLApSysMacAddress) = mibBuilder.importSymbols(
    "CISCO-LWAPP-AP-MIB",
    "cLApDot11IfEntry",
    "cLApDot11IfSlotId",
    "cLApDot11IfType",
    "cLApName",
    "cLApSysMacAddress")

(cldcClientMacAddress,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-DOT11-CLIENT-MIB",
    "cldcClientMacAddress")

(cLAPGroupName,
 cLWlanConfigEntry,
 cLWlanIndex,
 cLWlanProfileName) = mibBuilder.importSymbols(
    "CISCO-LWAPP-WLAN-MIB",
    "cLAPGroupName",
    "cLWlanConfigEntry",
    "cLWlanIndex",
    "cLWlanProfileName")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(TimeIntervalSec,
 Unsigned64) = mibBuilder.importSymbols(
    "CISCO-TC",
    "TimeIntervalSec",
    "Unsigned64")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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


# MODULE-IDENTITY

ciscoLwappQosMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 524)
)
if mibBuilder.loadTexts:
    ciscoLwappQosMIB.setRevisions(
        ("2018-04-24 00:00",
         "2017-05-12 00:00",
         "2007-01-07 00:00",
         "2006-04-13 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CiscoLwappDot11aPhyRates(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              9,
              12,
              18,
              24,
              36,
              48,
              54,
              65,
              72,
              130,
              135,
              144,
              150,
              270,
              300)
        )
    )
    namedValues = NamedValues(
        *(("six", 6),
          ("nine", 9),
          ("twelve", 12),
          ("eighteen", 18),
          ("twentyfour", 24),
          ("thirtysix", 36),
          ("fortyeight", 48),
          ("fiftyfour", 54),
          ("sixtyfive", 65),
          ("seventyTwoPointTwo", 72),
          ("oneThirty", 130),
          ("oneThirtyfive", 135),
          ("oneFortyFourPointFour", 144),
          ("oneFifty", 150),
          ("twoSeventy", 270),
          ("threeHundred", 300))
    )



class CiscoLwappDot11bPhyRates(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              6,
              9,
              11,
              12,
              18,
              24,
              36,
              48,
              54,
              65,
              72,
              130,
              135,
              144,
              150,
              270,
              300)
        )
    )
    namedValues = NamedValues(
        *(("one", 1),
          ("two", 2),
          ("fivepointfive", 5),
          ("six", 6),
          ("nine", 9),
          ("eleven", 11),
          ("twelve", 12),
          ("eighteen", 18),
          ("twentyfour", 24),
          ("thirtysix", 36),
          ("fortyeight", 48),
          ("fiftyfour", 54),
          ("sixtyfive", 65),
          ("seventyTwoPointTwo", 72),
          ("oneThirty", 130),
          ("oneThirtyfive", 135),
          ("oneFortyFourPointFour", 144),
          ("oneFifty", 150),
          ("twoSeventy", 270),
          ("threeHundred", 300))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoLwappQosMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappQosMIBNotifs = _CiscoLwappQosMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 0)
)
_CiscoLwappQosMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappQosMIBObjects = _CiscoLwappQosMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1)
)
_CLQd11aCACConfig_ObjectIdentity = ObjectIdentity
cLQd11aCACConfig = _CLQd11aCACConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 1)
)


class _CLQd11aVoiceAdmCtrlSupport_Type(TruthValue):
    """Custom type cLQd11aVoiceAdmCtrlSupport based on TruthValue"""
    defaultValue = 1


_CLQd11aVoiceAdmCtrlSupport_Type.__name__ = "TruthValue"
_CLQd11aVoiceAdmCtrlSupport_Object = MibScalar
cLQd11aVoiceAdmCtrlSupport = _CLQd11aVoiceAdmCtrlSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 1, 1),
    _CLQd11aVoiceAdmCtrlSupport_Type()
)
cLQd11aVoiceAdmCtrlSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11aVoiceAdmCtrlSupport.setStatus("current")


class _CLQd11aVoiceMaxAdmBandwidth_Type(Unsigned32):
    """Custom type cLQd11aVoiceMaxAdmBandwidth based on Unsigned32"""
    defaultValue = 75

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CLQd11aVoiceMaxAdmBandwidth_Type.__name__ = "Unsigned32"
_CLQd11aVoiceMaxAdmBandwidth_Object = MibScalar
cLQd11aVoiceMaxAdmBandwidth = _CLQd11aVoiceMaxAdmBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 1, 2),
    _CLQd11aVoiceMaxAdmBandwidth_Type()
)
cLQd11aVoiceMaxAdmBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11aVoiceMaxAdmBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    cLQd11aVoiceMaxAdmBandwidth.setUnits("Percent")


class _CLQd11aVoiceMaxRoamBandwidth_Type(Unsigned32):
    """Custom type cLQd11aVoiceMaxRoamBandwidth based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CLQd11aVoiceMaxRoamBandwidth_Type.__name__ = "Unsigned32"
_CLQd11aVoiceMaxRoamBandwidth_Object = MibScalar
cLQd11aVoiceMaxRoamBandwidth = _CLQd11aVoiceMaxRoamBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 1, 3),
    _CLQd11aVoiceMaxRoamBandwidth_Type()
)
cLQd11aVoiceMaxRoamBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11aVoiceMaxRoamBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    cLQd11aVoiceMaxRoamBandwidth.setUnits("Percent")


class _CLQd11aVideoAdmCtrlSupport_Type(TruthValue):
    """Custom type cLQd11aVideoAdmCtrlSupport based on TruthValue"""
    defaultValue = 2


_CLQd11aVideoAdmCtrlSupport_Type.__name__ = "TruthValue"
_CLQd11aVideoAdmCtrlSupport_Object = MibScalar
cLQd11aVideoAdmCtrlSupport = _CLQd11aVideoAdmCtrlSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 1, 4),
    _CLQd11aVideoAdmCtrlSupport_Type()
)
cLQd11aVideoAdmCtrlSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11aVideoAdmCtrlSupport.setStatus("current")


class _CLQd11aVideoMaxAdmBandwidth_Type(Unsigned32):
    """Custom type cLQd11aVideoMaxAdmBandwidth based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CLQd11aVideoMaxAdmBandwidth_Type.__name__ = "Unsigned32"
_CLQd11aVideoMaxAdmBandwidth_Object = MibScalar
cLQd11aVideoMaxAdmBandwidth = _CLQd11aVideoMaxAdmBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 1, 5),
    _CLQd11aVideoMaxAdmBandwidth_Type()
)
cLQd11aVideoMaxAdmBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11aVideoMaxAdmBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    cLQd11aVideoMaxAdmBandwidth.setUnits("Percent")


class _CLQd11aVideoMaxRoamBandwidth_Type(Unsigned32):
    """Custom type cLQd11aVideoMaxRoamBandwidth based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CLQd11aVideoMaxRoamBandwidth_Type.__name__ = "Unsigned32"
_CLQd11aVideoMaxRoamBandwidth_Object = MibScalar
cLQd11aVideoMaxRoamBandwidth = _CLQd11aVideoMaxRoamBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 1, 6),
    _CLQd11aVideoMaxRoamBandwidth_Type()
)
cLQd11aVideoMaxRoamBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11aVideoMaxRoamBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    cLQd11aVideoMaxRoamBandwidth.setUnits("Percent")


class _CLQd11aGprProbeInterval_Type(Unsigned32):
    """Custom type cLQd11aGprProbeInterval based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100),
    )


_CLQd11aGprProbeInterval_Type.__name__ = "Unsigned32"
_CLQd11aGprProbeInterval_Object = MibScalar
cLQd11aGprProbeInterval = _CLQd11aGprProbeInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 1, 7),
    _CLQd11aGprProbeInterval_Type()
)
cLQd11aGprProbeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11aGprProbeInterval.setStatus("current")
if mibBuilder.loadTexts:
    cLQd11aGprProbeInterval.setUnits("TU")


class _CLQd11aVoiceCtrl_Type(Integer32):
    """Custom type cLQd11aVoiceCtrl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loadBased", 1),
          ("static", 2))
    )


_CLQd11aVoiceCtrl_Type.__name__ = "Integer32"
_CLQd11aVoiceCtrl_Object = MibScalar
cLQd11aVoiceCtrl = _CLQd11aVoiceCtrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 1, 8),
    _CLQd11aVoiceCtrl_Type()
)
cLQd11aVoiceCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11aVoiceCtrl.setStatus("current")
_CLQd11aExpeditedBw_Type = TruthValue
_CLQd11aExpeditedBw_Object = MibScalar
cLQd11aExpeditedBw = _CLQd11aExpeditedBw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 1, 9),
    _CLQd11aExpeditedBw_Type()
)
cLQd11aExpeditedBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11aExpeditedBw.setStatus("current")


class _CLQd11aEdcaProfile_Type(Integer32):
    """Custom type cLQd11aEdcaProfile based on Integer32"""
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
        *(("wmmDefault", 1),
          ("svpVoice", 2),
          ("optimizedVoice", 3),
          ("optimizedVideoVoice", 4),
          ("customVoice", 5),
          ("fastlane", 6))
    )


_CLQd11aEdcaProfile_Type.__name__ = "Integer32"
_CLQd11aEdcaProfile_Object = MibScalar
cLQd11aEdcaProfile = _CLQd11aEdcaProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 1, 10),
    _CLQd11aEdcaProfile_Type()
)
cLQd11aEdcaProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11aEdcaProfile.setStatus("current")


class _CLQd11aMacOptimization_Type(TruthValue):
    """Custom type cLQd11aMacOptimization based on TruthValue"""
    defaultValue = 2


_CLQd11aMacOptimization_Type.__name__ = "TruthValue"
_CLQd11aMacOptimization_Object = MibScalar
cLQd11aMacOptimization = _CLQd11aMacOptimization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 1, 11),
    _CLQd11aMacOptimization_Type()
)
cLQd11aMacOptimization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11aMacOptimization.setStatus("current")
_CLQd11aMaxCallLimit_Type = Unsigned32
_CLQd11aMaxCallLimit_Object = MibScalar
cLQd11aMaxCallLimit = _CLQd11aMaxCallLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 1, 12),
    _CLQd11aMaxCallLimit_Type()
)
cLQd11aMaxCallLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11aMaxCallLimit.setStatus("deprecated")


class _CLQd11aMcastDirectEnable_Type(TruthValue):
    """Custom type cLQd11aMcastDirectEnable based on TruthValue"""
    defaultValue = 1


_CLQd11aMcastDirectEnable_Type.__name__ = "TruthValue"
_CLQd11aMcastDirectEnable_Object = MibScalar
cLQd11aMcastDirectEnable = _CLQd11aMcastDirectEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 1, 13),
    _CLQd11aMcastDirectEnable_Type()
)
cLQd11aMcastDirectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11aMcastDirectEnable.setStatus("current")


class _CLQd11aBestEffortAdmission_Type(TruthValue):
    """Custom type cLQd11aBestEffortAdmission based on TruthValue"""
    defaultValue = 2


_CLQd11aBestEffortAdmission_Type.__name__ = "TruthValue"
_CLQd11aBestEffortAdmission_Object = MibScalar
cLQd11aBestEffortAdmission = _CLQd11aBestEffortAdmission_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 1, 14),
    _CLQd11aBestEffortAdmission_Type()
)
cLQd11aBestEffortAdmission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11aBestEffortAdmission.setStatus("current")


class _CLQd11aRedirectBestEffort_Type(TruthValue):
    """Custom type cLQd11aRedirectBestEffort based on TruthValue"""
    defaultValue = 1


_CLQd11aRedirectBestEffort_Type.__name__ = "TruthValue"
_CLQd11aRedirectBestEffort_Object = MibScalar
cLQd11aRedirectBestEffort = _CLQd11aRedirectBestEffort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 1, 15),
    _CLQd11aRedirectBestEffort_Type()
)
cLQd11aRedirectBestEffort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11aRedirectBestEffort.setStatus("current")


class _CLQd11aRadioMaxStreams_Type(Integer32):
    """Custom type cLQd11aRadioMaxStreams based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_CLQd11aRadioMaxStreams_Type.__name__ = "Integer32"
_CLQd11aRadioMaxStreams_Object = MibScalar
cLQd11aRadioMaxStreams = _CLQd11aRadioMaxStreams_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 1, 16),
    _CLQd11aRadioMaxStreams_Type()
)
cLQd11aRadioMaxStreams.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11aRadioMaxStreams.setStatus("current")


class _CLQd11aMaxVideoATPercent_Type(Integer32):
    """Custom type cLQd11aMaxVideoATPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 85),
    )


_CLQd11aMaxVideoATPercent_Type.__name__ = "Integer32"
_CLQd11aMaxVideoATPercent_Object = MibScalar
cLQd11aMaxVideoATPercent = _CLQd11aMaxVideoATPercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 1, 17),
    _CLQd11aMaxVideoATPercent_Type()
)
cLQd11aMaxVideoATPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11aMaxVideoATPercent.setStatus("current")
if mibBuilder.loadTexts:
    cLQd11aMaxVideoATPercent.setUnits("Percent")


class _CLQd11aMaxVoiceATPercent_Type(Integer32):
    """Custom type cLQd11aMaxVoiceATPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 85),
    )


_CLQd11aMaxVoiceATPercent_Type.__name__ = "Integer32"
_CLQd11aMaxVoiceATPercent_Object = MibScalar
cLQd11aMaxVoiceATPercent = _CLQd11aMaxVoiceATPercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 1, 18),
    _CLQd11aMaxVoiceATPercent_Type()
)
cLQd11aMaxVoiceATPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11aMaxVoiceATPercent.setStatus("current")
if mibBuilder.loadTexts:
    cLQd11aMaxVoiceATPercent.setUnits("Percent")


class _CLQd11aMaxMediaATPercent_Type(Integer32):
    """Custom type cLQd11aMaxMediaATPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CLQd11aMaxMediaATPercent_Type.__name__ = "Integer32"
_CLQd11aMaxMediaATPercent_Object = MibScalar
cLQd11aMaxMediaATPercent = _CLQd11aMaxMediaATPercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 1, 19),
    _CLQd11aMaxMediaATPercent_Type()
)
cLQd11aMaxMediaATPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11aMaxMediaATPercent.setStatus("current")
if mibBuilder.loadTexts:
    cLQd11aMaxMediaATPercent.setUnits("Percent")
_CLQd11aMinPhyRate_Type = CiscoLwappDot11aPhyRates
_CLQd11aMinPhyRate_Object = MibScalar
cLQd11aMinPhyRate = _CLQd11aMinPhyRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 1, 20),
    _CLQd11aMinPhyRate_Type()
)
cLQd11aMinPhyRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11aMinPhyRate.setStatus("current")
if mibBuilder.loadTexts:
    cLQd11aMinPhyRate.setUnits("Mbps")


class _CLQd11aClientMaxStreams_Type(Integer32):
    """Custom type cLQd11aClientMaxStreams based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_CLQd11aClientMaxStreams_Type.__name__ = "Integer32"
_CLQd11aClientMaxStreams_Object = MibScalar
cLQd11aClientMaxStreams = _CLQd11aClientMaxStreams_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 1, 21),
    _CLQd11aClientMaxStreams_Type()
)
cLQd11aClientMaxStreams.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11aClientMaxStreams.setStatus("current")


class _CLQd11aSipCacSupportEnable_Type(TruthValue):
    """Custom type cLQd11aSipCacSupportEnable based on TruthValue"""
    defaultValue = 2


_CLQd11aSipCacSupportEnable_Type.__name__ = "TruthValue"
_CLQd11aSipCacSupportEnable_Object = MibScalar
cLQd11aSipCacSupportEnable = _CLQd11aSipCacSupportEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 1, 22),
    _CLQd11aSipCacSupportEnable_Type()
)
cLQd11aSipCacSupportEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11aSipCacSupportEnable.setStatus("current")


class _CLQd11aMaxRetryPercent_Type(Integer32):
    """Custom type cLQd11aMaxRetryPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CLQd11aMaxRetryPercent_Type.__name__ = "Integer32"
_CLQd11aMaxRetryPercent_Object = MibScalar
cLQd11aMaxRetryPercent = _CLQd11aMaxRetryPercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 1, 23),
    _CLQd11aMaxRetryPercent_Type()
)
cLQd11aMaxRetryPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11aMaxRetryPercent.setStatus("current")
if mibBuilder.loadTexts:
    cLQd11aMaxRetryPercent.setUnits("Percent")


class _CLQd11aVideoCtrl_Type(Integer32):
    """Custom type cLQd11aVideoCtrl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loadBased", 1),
          ("static", 2))
    )


_CLQd11aVideoCtrl_Type.__name__ = "Integer32"
_CLQd11aVideoCtrl_Object = MibScalar
cLQd11aVideoCtrl = _CLQd11aVideoCtrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 1, 24),
    _CLQd11aVideoCtrl_Type()
)
cLQd11aVideoCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11aVideoCtrl.setStatus("current")


class _CLQd11aSipCacVideoEnable_Type(TruthValue):
    """Custom type cLQd11aSipCacVideoEnable based on TruthValue"""
    defaultValue = 2


_CLQd11aSipCacVideoEnable_Type.__name__ = "TruthValue"
_CLQd11aSipCacVideoEnable_Object = MibScalar
cLQd11aSipCacVideoEnable = _CLQd11aSipCacVideoEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 1, 25),
    _CLQd11aSipCacVideoEnable_Type()
)
cLQd11aSipCacVideoEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11aSipCacVideoEnable.setStatus("current")
_CLQd11bCACConfig_ObjectIdentity = ObjectIdentity
cLQd11bCACConfig = _CLQd11bCACConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 2)
)


class _CLQd11bVoiceAdmCtrlSupport_Type(TruthValue):
    """Custom type cLQd11bVoiceAdmCtrlSupport based on TruthValue"""
    defaultValue = 1


_CLQd11bVoiceAdmCtrlSupport_Type.__name__ = "TruthValue"
_CLQd11bVoiceAdmCtrlSupport_Object = MibScalar
cLQd11bVoiceAdmCtrlSupport = _CLQd11bVoiceAdmCtrlSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 2, 1),
    _CLQd11bVoiceAdmCtrlSupport_Type()
)
cLQd11bVoiceAdmCtrlSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11bVoiceAdmCtrlSupport.setStatus("current")


class _CLQd11bVoiceMaxAdmBandwidth_Type(Unsigned32):
    """Custom type cLQd11bVoiceMaxAdmBandwidth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CLQd11bVoiceMaxAdmBandwidth_Type.__name__ = "Unsigned32"
_CLQd11bVoiceMaxAdmBandwidth_Object = MibScalar
cLQd11bVoiceMaxAdmBandwidth = _CLQd11bVoiceMaxAdmBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 2, 2),
    _CLQd11bVoiceMaxAdmBandwidth_Type()
)
cLQd11bVoiceMaxAdmBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11bVoiceMaxAdmBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    cLQd11bVoiceMaxAdmBandwidth.setUnits("Percent")


class _CLQd11bVoiceMaxRoamBandwidth_Type(Unsigned32):
    """Custom type cLQd11bVoiceMaxRoamBandwidth based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CLQd11bVoiceMaxRoamBandwidth_Type.__name__ = "Unsigned32"
_CLQd11bVoiceMaxRoamBandwidth_Object = MibScalar
cLQd11bVoiceMaxRoamBandwidth = _CLQd11bVoiceMaxRoamBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 2, 3),
    _CLQd11bVoiceMaxRoamBandwidth_Type()
)
cLQd11bVoiceMaxRoamBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11bVoiceMaxRoamBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    cLQd11bVoiceMaxRoamBandwidth.setUnits("Percent")


class _CLQd11bVideoAdmCtrlSupport_Type(TruthValue):
    """Custom type cLQd11bVideoAdmCtrlSupport based on TruthValue"""
    defaultValue = 1


_CLQd11bVideoAdmCtrlSupport_Type.__name__ = "TruthValue"
_CLQd11bVideoAdmCtrlSupport_Object = MibScalar
cLQd11bVideoAdmCtrlSupport = _CLQd11bVideoAdmCtrlSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 2, 4),
    _CLQd11bVideoAdmCtrlSupport_Type()
)
cLQd11bVideoAdmCtrlSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11bVideoAdmCtrlSupport.setStatus("current")


class _CLQd11bVideoMaxAdmBandwidth_Type(Unsigned32):
    """Custom type cLQd11bVideoMaxAdmBandwidth based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CLQd11bVideoMaxAdmBandwidth_Type.__name__ = "Unsigned32"
_CLQd11bVideoMaxAdmBandwidth_Object = MibScalar
cLQd11bVideoMaxAdmBandwidth = _CLQd11bVideoMaxAdmBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 2, 5),
    _CLQd11bVideoMaxAdmBandwidth_Type()
)
cLQd11bVideoMaxAdmBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11bVideoMaxAdmBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    cLQd11bVideoMaxAdmBandwidth.setUnits("Percent")


class _CLQd11bVideoMaxRoamBandwidth_Type(Unsigned32):
    """Custom type cLQd11bVideoMaxRoamBandwidth based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CLQd11bVideoMaxRoamBandwidth_Type.__name__ = "Unsigned32"
_CLQd11bVideoMaxRoamBandwidth_Object = MibScalar
cLQd11bVideoMaxRoamBandwidth = _CLQd11bVideoMaxRoamBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 2, 6),
    _CLQd11bVideoMaxRoamBandwidth_Type()
)
cLQd11bVideoMaxRoamBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11bVideoMaxRoamBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    cLQd11bVideoMaxRoamBandwidth.setUnits("Percent")


class _CLQd11bGprProbeInterval_Type(Unsigned32):
    """Custom type cLQd11bGprProbeInterval based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100),
    )


_CLQd11bGprProbeInterval_Type.__name__ = "Unsigned32"
_CLQd11bGprProbeInterval_Object = MibScalar
cLQd11bGprProbeInterval = _CLQd11bGprProbeInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 2, 7),
    _CLQd11bGprProbeInterval_Type()
)
cLQd11bGprProbeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11bGprProbeInterval.setStatus("current")
if mibBuilder.loadTexts:
    cLQd11bGprProbeInterval.setUnits("TU")


class _CLQd11bVoiceCtrl_Type(Integer32):
    """Custom type cLQd11bVoiceCtrl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loadBased", 1),
          ("static", 2))
    )


_CLQd11bVoiceCtrl_Type.__name__ = "Integer32"
_CLQd11bVoiceCtrl_Object = MibScalar
cLQd11bVoiceCtrl = _CLQd11bVoiceCtrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 2, 8),
    _CLQd11bVoiceCtrl_Type()
)
cLQd11bVoiceCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11bVoiceCtrl.setStatus("current")
_CLQd11bExpeditedBw_Type = TruthValue
_CLQd11bExpeditedBw_Object = MibScalar
cLQd11bExpeditedBw = _CLQd11bExpeditedBw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 2, 9),
    _CLQd11bExpeditedBw_Type()
)
cLQd11bExpeditedBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11bExpeditedBw.setStatus("current")


class _CLQd11bEdcaProfile_Type(Integer32):
    """Custom type cLQd11bEdcaProfile based on Integer32"""
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
        *(("wmmDefault", 1),
          ("svpVoice", 2),
          ("optimizedVoice", 3),
          ("optimizedVideoVoice", 4),
          ("customVoice", 5),
          ("fastlane", 6))
    )


_CLQd11bEdcaProfile_Type.__name__ = "Integer32"
_CLQd11bEdcaProfile_Object = MibScalar
cLQd11bEdcaProfile = _CLQd11bEdcaProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 2, 10),
    _CLQd11bEdcaProfile_Type()
)
cLQd11bEdcaProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11bEdcaProfile.setStatus("current")
_CLQd11bMacOptimization_Type = TruthValue
_CLQd11bMacOptimization_Object = MibScalar
cLQd11bMacOptimization = _CLQd11bMacOptimization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 2, 11),
    _CLQd11bMacOptimization_Type()
)
cLQd11bMacOptimization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11bMacOptimization.setStatus("current")
_CLQd11bMaxCallLimit_Type = Unsigned32
_CLQd11bMaxCallLimit_Object = MibScalar
cLQd11bMaxCallLimit = _CLQd11bMaxCallLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 2, 12),
    _CLQd11bMaxCallLimit_Type()
)
cLQd11bMaxCallLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11bMaxCallLimit.setStatus("current")


class _CLQd11bMcastDirectEnable_Type(TruthValue):
    """Custom type cLQd11bMcastDirectEnable based on TruthValue"""
    defaultValue = 1


_CLQd11bMcastDirectEnable_Type.__name__ = "TruthValue"
_CLQd11bMcastDirectEnable_Object = MibScalar
cLQd11bMcastDirectEnable = _CLQd11bMcastDirectEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 2, 13),
    _CLQd11bMcastDirectEnable_Type()
)
cLQd11bMcastDirectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11bMcastDirectEnable.setStatus("current")


class _CLQd11bBestEffortAdmission_Type(TruthValue):
    """Custom type cLQd11bBestEffortAdmission based on TruthValue"""
    defaultValue = 2


_CLQd11bBestEffortAdmission_Type.__name__ = "TruthValue"
_CLQd11bBestEffortAdmission_Object = MibScalar
cLQd11bBestEffortAdmission = _CLQd11bBestEffortAdmission_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 2, 14),
    _CLQd11bBestEffortAdmission_Type()
)
cLQd11bBestEffortAdmission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11bBestEffortAdmission.setStatus("current")


class _CLQd11bRedirectBestEffort_Type(TruthValue):
    """Custom type cLQd11bRedirectBestEffort based on TruthValue"""
    defaultValue = 1


_CLQd11bRedirectBestEffort_Type.__name__ = "TruthValue"
_CLQd11bRedirectBestEffort_Object = MibScalar
cLQd11bRedirectBestEffort = _CLQd11bRedirectBestEffort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 2, 15),
    _CLQd11bRedirectBestEffort_Type()
)
cLQd11bRedirectBestEffort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11bRedirectBestEffort.setStatus("current")


class _CLQd11bRadioMaxStreams_Type(Integer32):
    """Custom type cLQd11bRadioMaxStreams based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_CLQd11bRadioMaxStreams_Type.__name__ = "Integer32"
_CLQd11bRadioMaxStreams_Object = MibScalar
cLQd11bRadioMaxStreams = _CLQd11bRadioMaxStreams_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 2, 16),
    _CLQd11bRadioMaxStreams_Type()
)
cLQd11bRadioMaxStreams.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11bRadioMaxStreams.setStatus("current")


class _CLQd11bMaxVideoATPercent_Type(Integer32):
    """Custom type cLQd11bMaxVideoATPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 85),
    )


_CLQd11bMaxVideoATPercent_Type.__name__ = "Integer32"
_CLQd11bMaxVideoATPercent_Object = MibScalar
cLQd11bMaxVideoATPercent = _CLQd11bMaxVideoATPercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 2, 17),
    _CLQd11bMaxVideoATPercent_Type()
)
cLQd11bMaxVideoATPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11bMaxVideoATPercent.setStatus("current")
if mibBuilder.loadTexts:
    cLQd11bMaxVideoATPercent.setUnits("Percent")


class _CLQd11bMaxVoiceATPercent_Type(Integer32):
    """Custom type cLQd11bMaxVoiceATPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 85),
    )


_CLQd11bMaxVoiceATPercent_Type.__name__ = "Integer32"
_CLQd11bMaxVoiceATPercent_Object = MibScalar
cLQd11bMaxVoiceATPercent = _CLQd11bMaxVoiceATPercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 2, 18),
    _CLQd11bMaxVoiceATPercent_Type()
)
cLQd11bMaxVoiceATPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11bMaxVoiceATPercent.setStatus("current")
if mibBuilder.loadTexts:
    cLQd11bMaxVoiceATPercent.setUnits("Percent")


class _CLQd11bMaxMediaATPercent_Type(Integer32):
    """Custom type cLQd11bMaxMediaATPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CLQd11bMaxMediaATPercent_Type.__name__ = "Integer32"
_CLQd11bMaxMediaATPercent_Object = MibScalar
cLQd11bMaxMediaATPercent = _CLQd11bMaxMediaATPercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 2, 19),
    _CLQd11bMaxMediaATPercent_Type()
)
cLQd11bMaxMediaATPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11bMaxMediaATPercent.setStatus("current")
if mibBuilder.loadTexts:
    cLQd11bMaxMediaATPercent.setUnits("Percent")


class _CLQd11bMinPhyRate_Type(CiscoLwappDot11bPhyRates):
    """Custom type cLQd11bMinPhyRate based on CiscoLwappDot11bPhyRates"""
    defaultValue = 1


_CLQd11bMinPhyRate_Type.__name__ = "CiscoLwappDot11bPhyRates"
_CLQd11bMinPhyRate_Object = MibScalar
cLQd11bMinPhyRate = _CLQd11bMinPhyRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 2, 20),
    _CLQd11bMinPhyRate_Type()
)
cLQd11bMinPhyRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11bMinPhyRate.setStatus("current")
if mibBuilder.loadTexts:
    cLQd11bMinPhyRate.setUnits("Mbps")


class _CLQd11bClientMaxStreams_Type(Integer32):
    """Custom type cLQd11bClientMaxStreams based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CLQd11bClientMaxStreams_Type.__name__ = "Integer32"
_CLQd11bClientMaxStreams_Object = MibScalar
cLQd11bClientMaxStreams = _CLQd11bClientMaxStreams_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 2, 21),
    _CLQd11bClientMaxStreams_Type()
)
cLQd11bClientMaxStreams.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11bClientMaxStreams.setStatus("current")


class _CLQd11bSipCacSupportEnable_Type(TruthValue):
    """Custom type cLQd11bSipCacSupportEnable based on TruthValue"""
    defaultValue = 2


_CLQd11bSipCacSupportEnable_Type.__name__ = "TruthValue"
_CLQd11bSipCacSupportEnable_Object = MibScalar
cLQd11bSipCacSupportEnable = _CLQd11bSipCacSupportEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 2, 22),
    _CLQd11bSipCacSupportEnable_Type()
)
cLQd11bSipCacSupportEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11bSipCacSupportEnable.setStatus("current")


class _CLQd11bMaxRetryPercent_Type(Integer32):
    """Custom type cLQd11bMaxRetryPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CLQd11bMaxRetryPercent_Type.__name__ = "Integer32"
_CLQd11bMaxRetryPercent_Object = MibScalar
cLQd11bMaxRetryPercent = _CLQd11bMaxRetryPercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 2, 23),
    _CLQd11bMaxRetryPercent_Type()
)
cLQd11bMaxRetryPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11bMaxRetryPercent.setStatus("current")
if mibBuilder.loadTexts:
    cLQd11bMaxRetryPercent.setUnits("Percent")


class _CLQd11bVideoCtrl_Type(Integer32):
    """Custom type cLQd11bVideoCtrl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loadBased", 1),
          ("static", 2))
    )


_CLQd11bVideoCtrl_Type.__name__ = "Integer32"
_CLQd11bVideoCtrl_Object = MibScalar
cLQd11bVideoCtrl = _CLQd11bVideoCtrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 2, 24),
    _CLQd11bVideoCtrl_Type()
)
cLQd11bVideoCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11bVideoCtrl.setStatus("current")


class _CLQd11bSipCacVideoEnable_Type(TruthValue):
    """Custom type cLQd11bSipCacVideoEnable based on TruthValue"""
    defaultValue = 2


_CLQd11bSipCacVideoEnable_Type.__name__ = "TruthValue"
_CLQd11bSipCacVideoEnable_Object = MibScalar
cLQd11bSipCacVideoEnable = _CLQd11bSipCacVideoEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 2, 25),
    _CLQd11bSipCacVideoEnable_Type()
)
cLQd11bSipCacVideoEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11bSipCacVideoEnable.setStatus("current")
_CLQd11GprConfig_ObjectIdentity = ObjectIdentity
cLQd11GprConfig = _CLQd11GprConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 3)
)
_CLQd11GprTable_Object = MibTable
cLQd11GprTable = _CLQd11GprTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cLQd11GprTable.setStatus("current")
_CLQd11GprEntry_Object = MibTableRow
cLQd11GprEntry = _CLQd11GprEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 3, 1, 1)
)
cLQd11GprEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"),
)
if mibBuilder.loadTexts:
    cLQd11GprEntry.setStatus("current")


class _CLQd11GprSupport_Type(TruthValue):
    """Custom type cLQd11GprSupport based on TruthValue"""
    defaultValue = 2


_CLQd11GprSupport_Type.__name__ = "TruthValue"
_CLQd11GprSupport_Object = MibTableColumn
cLQd11GprSupport = _CLQd11GprSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 3, 1, 1, 1),
    _CLQd11GprSupport_Type()
)
cLQd11GprSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11GprSupport.setStatus("current")
_CLQd11CACStats_ObjectIdentity = ObjectIdentity
cLQd11CACStats = _CLQd11CACStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4)
)
_CLQd11CACStatsTable_Object = MibTable
cLQd11CACStatsTable = _CLQd11CACStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cLQd11CACStatsTable.setStatus("current")
_CLQd11CACStatsEntry_Object = MibTableRow
cLQd11CACStatsEntry = _CLQd11CACStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1)
)
cLQd11CACStatsEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"),
)
if mibBuilder.loadTexts:
    cLQd11CACStatsEntry.setStatus("current")


class _CLQd11CacVoiceBwInUse_Type(Gauge32):
    """Custom type cLQd11CacVoiceBwInUse based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CLQd11CacVoiceBwInUse_Type.__name__ = "Gauge32"
_CLQd11CacVoiceBwInUse_Object = MibTableColumn
cLQd11CacVoiceBwInUse = _CLQd11CacVoiceBwInUse_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 1),
    _CLQd11CacVoiceBwInUse_Type()
)
cLQd11CacVoiceBwInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11CacVoiceBwInUse.setStatus("current")
if mibBuilder.loadTexts:
    cLQd11CacVoiceBwInUse.setUnits("Percent")


class _CLQd11CacVideoBwInUse_Type(Gauge32):
    """Custom type cLQd11CacVideoBwInUse based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CLQd11CacVideoBwInUse_Type.__name__ = "Gauge32"
_CLQd11CacVideoBwInUse_Object = MibTableColumn
cLQd11CacVideoBwInUse = _CLQd11CacVideoBwInUse_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 2),
    _CLQd11CacVideoBwInUse_Type()
)
cLQd11CacVideoBwInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11CacVideoBwInUse.setStatus("current")
if mibBuilder.loadTexts:
    cLQd11CacVideoBwInUse.setUnits("Percent")
_CLQd11CacVoiceCallsInProgress_Type = Gauge32
_CLQd11CacVoiceCallsInProgress_Object = MibTableColumn
cLQd11CacVoiceCallsInProgress = _CLQd11CacVoiceCallsInProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 3),
    _CLQd11CacVoiceCallsInProgress_Type()
)
cLQd11CacVoiceCallsInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11CacVoiceCallsInProgress.setStatus("current")
_CLQd11CacRoamVoiceCallsInProg_Type = Gauge32
_CLQd11CacRoamVoiceCallsInProg_Object = MibTableColumn
cLQd11CacRoamVoiceCallsInProg = _CLQd11CacRoamVoiceCallsInProg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 4),
    _CLQd11CacRoamVoiceCallsInProg_Type()
)
cLQd11CacRoamVoiceCallsInProg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11CacRoamVoiceCallsInProg.setStatus("current")
_CLQd11CacTotalVoiceCallsAP_Type = Counter32
_CLQd11CacTotalVoiceCallsAP_Object = MibTableColumn
cLQd11CacTotalVoiceCallsAP = _CLQd11CacTotalVoiceCallsAP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 5),
    _CLQd11CacTotalVoiceCallsAP_Type()
)
cLQd11CacTotalVoiceCallsAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11CacTotalVoiceCallsAP.setStatus("current")
_CLQd11CacTotalRoamCallsAP_Type = Counter32
_CLQd11CacTotalRoamCallsAP_Object = MibTableColumn
cLQd11CacTotalRoamCallsAP = _CLQd11CacTotalRoamCallsAP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 6),
    _CLQd11CacTotalRoamCallsAP_Type()
)
cLQd11CacTotalRoamCallsAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11CacTotalRoamCallsAP.setStatus("current")
_CLQd11CacVoiceCallsRejectedAP_Type = Counter32
_CLQd11CacVoiceCallsRejectedAP_Object = MibTableColumn
cLQd11CacVoiceCallsRejectedAP = _CLQd11CacVoiceCallsRejectedAP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 7),
    _CLQd11CacVoiceCallsRejectedAP_Type()
)
cLQd11CacVoiceCallsRejectedAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11CacVoiceCallsRejectedAP.setStatus("current")
_CLQd11CacRoamCallsRejectedAP_Type = Counter32
_CLQd11CacRoamCallsRejectedAP_Object = MibTableColumn
cLQd11CacRoamCallsRejectedAP = _CLQd11CacRoamCallsRejectedAP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 8),
    _CLQd11CacRoamCallsRejectedAP_Type()
)
cLQd11CacRoamCallsRejectedAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11CacRoamCallsRejectedAP.setStatus("current")
_CLQd11CacRejCallsInsufBw_Type = Counter32
_CLQd11CacRejCallsInsufBw_Object = MibTableColumn
cLQd11CacRejCallsInsufBw = _CLQd11CacRejCallsInsufBw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 9),
    _CLQd11CacRejCallsInsufBw_Type()
)
cLQd11CacRejCallsInsufBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11CacRejCallsInsufBw.setStatus("current")
_CLQd11CacRejCallsBadParams_Type = Counter32
_CLQd11CacRejCallsBadParams_Object = MibTableColumn
cLQd11CacRejCallsBadParams = _CLQd11CacRejCallsBadParams_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 10),
    _CLQd11CacRejCallsBadParams_Type()
)
cLQd11CacRejCallsBadParams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11CacRejCallsBadParams.setStatus("current")
_CLQd11CacRejCallsPhyRate_Type = Counter32
_CLQd11CacRejCallsPhyRate_Object = MibTableColumn
cLQd11CacRejCallsPhyRate = _CLQd11CacRejCallsPhyRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 11),
    _CLQd11CacRejCallsPhyRate_Type()
)
cLQd11CacRejCallsPhyRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11CacRejCallsPhyRate.setStatus("current")
_CLQd11CacRejCallsQosPolicy_Type = Counter32
_CLQd11CacRejCallsQosPolicy_Object = MibTableColumn
cLQd11CacRejCallsQosPolicy = _CLQd11CacRejCallsQosPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 12),
    _CLQd11CacRejCallsQosPolicy_Type()
)
cLQd11CacRejCallsQosPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11CacRejCallsQosPolicy.setStatus("current")
_CLQd11SipCacNonRoamCallsInProgress_Type = Gauge32
_CLQd11SipCacNonRoamCallsInProgress_Object = MibTableColumn
cLQd11SipCacNonRoamCallsInProgress = _CLQd11SipCacNonRoamCallsInProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 13),
    _CLQd11SipCacNonRoamCallsInProgress_Type()
)
cLQd11SipCacNonRoamCallsInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11SipCacNonRoamCallsInProgress.setStatus("current")
_CLQd11SipCacRoamCallsInProg_Type = Gauge32
_CLQd11SipCacRoamCallsInProg_Object = MibTableColumn
cLQd11SipCacRoamCallsInProg = _CLQd11SipCacRoamCallsInProg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 14),
    _CLQd11SipCacRoamCallsInProg_Type()
)
cLQd11SipCacRoamCallsInProg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11SipCacRoamCallsInProg.setStatus("current")
_CLQd11SipCacTotalNonRoamCallsAP_Type = Counter32
_CLQd11SipCacTotalNonRoamCallsAP_Object = MibTableColumn
cLQd11SipCacTotalNonRoamCallsAP = _CLQd11SipCacTotalNonRoamCallsAP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 15),
    _CLQd11SipCacTotalNonRoamCallsAP_Type()
)
cLQd11SipCacTotalNonRoamCallsAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11SipCacTotalNonRoamCallsAP.setStatus("current")
_CLQd11SipCacTotalRoamCallsAP_Type = Counter32
_CLQd11SipCacTotalRoamCallsAP_Object = MibTableColumn
cLQd11SipCacTotalRoamCallsAP = _CLQd11SipCacTotalRoamCallsAP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 16),
    _CLQd11SipCacTotalRoamCallsAP_Type()
)
cLQd11SipCacTotalRoamCallsAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11SipCacTotalRoamCallsAP.setStatus("current")
_CLQd11SipCacNonRoamCallsRejectedInSuffBw_Type = Counter32
_CLQd11SipCacNonRoamCallsRejectedInSuffBw_Object = MibTableColumn
cLQd11SipCacNonRoamCallsRejectedInSuffBw = _CLQd11SipCacNonRoamCallsRejectedInSuffBw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 17),
    _CLQd11SipCacNonRoamCallsRejectedInSuffBw_Type()
)
cLQd11SipCacNonRoamCallsRejectedInSuffBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11SipCacNonRoamCallsRejectedInSuffBw.setStatus("current")
_CLQd11SipCacRoamCallsRejectedInSuffBw_Type = Counter32
_CLQd11SipCacRoamCallsRejectedInSuffBw_Object = MibTableColumn
cLQd11SipCacRoamCallsRejectedInSuffBw = _CLQd11SipCacRoamCallsRejectedInSuffBw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 18),
    _CLQd11SipCacRoamCallsRejectedInSuffBw_Type()
)
cLQd11SipCacRoamCallsRejectedInSuffBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11SipCacRoamCallsRejectedInSuffBw.setStatus("current")
_CLQd11SipCacNonRoamCallsRejectedMaxLimit_Type = Counter32
_CLQd11SipCacNonRoamCallsRejectedMaxLimit_Object = MibTableColumn
cLQd11SipCacNonRoamCallsRejectedMaxLimit = _CLQd11SipCacNonRoamCallsRejectedMaxLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 19),
    _CLQd11SipCacNonRoamCallsRejectedMaxLimit_Type()
)
cLQd11SipCacNonRoamCallsRejectedMaxLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11SipCacNonRoamCallsRejectedMaxLimit.setStatus("current")
_CLQd11SipCacRoamCallsRejectedMaxLimit_Type = Counter32
_CLQd11SipCacRoamCallsRejectedMaxLimit_Object = MibTableColumn
cLQd11SipCacRoamCallsRejectedMaxLimit = _CLQd11SipCacRoamCallsRejectedMaxLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 20),
    _CLQd11SipCacRoamCallsRejectedMaxLimit_Type()
)
cLQd11SipCacRoamCallsRejectedMaxLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11SipCacRoamCallsRejectedMaxLimit.setStatus("current")
_CLQd11SipCacRejCallsQosPolicy_Type = Counter32
_CLQd11SipCacRejCallsQosPolicy_Object = MibTableColumn
cLQd11SipCacRejCallsQosPolicy = _CLQd11SipCacRejCallsQosPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 21),
    _CLQd11SipCacRejCallsQosPolicy_Type()
)
cLQd11SipCacRejCallsQosPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11SipCacRejCallsQosPolicy.setStatus("deprecated")
_CLQd11SipCacPreferredCallsReceived_Type = Counter32
_CLQd11SipCacPreferredCallsReceived_Object = MibTableColumn
cLQd11SipCacPreferredCallsReceived = _CLQd11SipCacPreferredCallsReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 22),
    _CLQd11SipCacPreferredCallsReceived_Type()
)
cLQd11SipCacPreferredCallsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11SipCacPreferredCallsReceived.setStatus("current")
_CLQd11SipCacPreferredCallsAccepted_Type = Counter32
_CLQd11SipCacPreferredCallsAccepted_Object = MibTableColumn
cLQd11SipCacPreferredCallsAccepted = _CLQd11SipCacPreferredCallsAccepted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 23),
    _CLQd11SipCacPreferredCallsAccepted_Type()
)
cLQd11SipCacPreferredCallsAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11SipCacPreferredCallsAccepted.setStatus("current")
_CLQd11KtsCacNonRoamCallsInProgress_Type = Gauge32
_CLQd11KtsCacNonRoamCallsInProgress_Object = MibTableColumn
cLQd11KtsCacNonRoamCallsInProgress = _CLQd11KtsCacNonRoamCallsInProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 24),
    _CLQd11KtsCacNonRoamCallsInProgress_Type()
)
cLQd11KtsCacNonRoamCallsInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11KtsCacNonRoamCallsInProgress.setStatus("current")
_CLQd11KtsCacRoamCallsInProg_Type = Gauge32
_CLQd11KtsCacRoamCallsInProg_Object = MibTableColumn
cLQd11KtsCacRoamCallsInProg = _CLQd11KtsCacRoamCallsInProg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 25),
    _CLQd11KtsCacRoamCallsInProg_Type()
)
cLQd11KtsCacRoamCallsInProg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11KtsCacRoamCallsInProg.setStatus("current")
_CLQd11KtsCacTotalNonRoamCallsAP_Type = Counter32
_CLQd11KtsCacTotalNonRoamCallsAP_Object = MibTableColumn
cLQd11KtsCacTotalNonRoamCallsAP = _CLQd11KtsCacTotalNonRoamCallsAP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 26),
    _CLQd11KtsCacTotalNonRoamCallsAP_Type()
)
cLQd11KtsCacTotalNonRoamCallsAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11KtsCacTotalNonRoamCallsAP.setStatus("current")
_CLQd11KtsCacTotalRoamCallsAP_Type = Counter32
_CLQd11KtsCacTotalRoamCallsAP_Object = MibTableColumn
cLQd11KtsCacTotalRoamCallsAP = _CLQd11KtsCacTotalRoamCallsAP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 27),
    _CLQd11KtsCacTotalRoamCallsAP_Type()
)
cLQd11KtsCacTotalRoamCallsAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11KtsCacTotalRoamCallsAP.setStatus("current")
_CLQd11KtsCacNonRoamCallsRejectedInSuffBw_Type = Counter32
_CLQd11KtsCacNonRoamCallsRejectedInSuffBw_Object = MibTableColumn
cLQd11KtsCacNonRoamCallsRejectedInSuffBw = _CLQd11KtsCacNonRoamCallsRejectedInSuffBw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 28),
    _CLQd11KtsCacNonRoamCallsRejectedInSuffBw_Type()
)
cLQd11KtsCacNonRoamCallsRejectedInSuffBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11KtsCacNonRoamCallsRejectedInSuffBw.setStatus("current")
_CLQd11KtsCacRoamCallsRejectedInSuffBw_Type = Counter32
_CLQd11KtsCacRoamCallsRejectedInSuffBw_Object = MibTableColumn
cLQd11KtsCacRoamCallsRejectedInSuffBw = _CLQd11KtsCacRoamCallsRejectedInSuffBw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 29),
    _CLQd11KtsCacRoamCallsRejectedInSuffBw_Type()
)
cLQd11KtsCacRoamCallsRejectedInSuffBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11KtsCacRoamCallsRejectedInSuffBw.setStatus("current")


class _CLQd11CacVideoRoamBwInUse_Type(Gauge32):
    """Custom type cLQd11CacVideoRoamBwInUse based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CLQd11CacVideoRoamBwInUse_Type.__name__ = "Gauge32"
_CLQd11CacVideoRoamBwInUse_Object = MibTableColumn
cLQd11CacVideoRoamBwInUse = _CLQd11CacVideoRoamBwInUse_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 30),
    _CLQd11CacVideoRoamBwInUse_Type()
)
cLQd11CacVideoRoamBwInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11CacVideoRoamBwInUse.setStatus("current")
if mibBuilder.loadTexts:
    cLQd11CacVideoRoamBwInUse.setUnits("Percent")


class _CLQd11CacVideoTotalBwInUse_Type(Gauge32):
    """Custom type cLQd11CacVideoTotalBwInUse based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CLQd11CacVideoTotalBwInUse_Type.__name__ = "Gauge32"
_CLQd11CacVideoTotalBwInUse_Object = MibTableColumn
cLQd11CacVideoTotalBwInUse = _CLQd11CacVideoTotalBwInUse_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 31),
    _CLQd11CacVideoTotalBwInUse_Type()
)
cLQd11CacVideoTotalBwInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11CacVideoTotalBwInUse.setStatus("current")
if mibBuilder.loadTexts:
    cLQd11CacVideoTotalBwInUse.setUnits("Percent")
_CLQd11CacVideoCallsInProgress_Type = Gauge32
_CLQd11CacVideoCallsInProgress_Object = MibTableColumn
cLQd11CacVideoCallsInProgress = _CLQd11CacVideoCallsInProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 32),
    _CLQd11CacVideoCallsInProgress_Type()
)
cLQd11CacVideoCallsInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11CacVideoCallsInProgress.setStatus("current")
_CLQd11CacVideoRoamCallsInProg_Type = Gauge32
_CLQd11CacVideoRoamCallsInProg_Object = MibTableColumn
cLQd11CacVideoRoamCallsInProg = _CLQd11CacVideoRoamCallsInProg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 33),
    _CLQd11CacVideoRoamCallsInProg_Type()
)
cLQd11CacVideoRoamCallsInProg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11CacVideoRoamCallsInProg.setStatus("current")
_CLQd11CacVideoTotalCallsAP_Type = Counter32
_CLQd11CacVideoTotalCallsAP_Object = MibTableColumn
cLQd11CacVideoTotalCallsAP = _CLQd11CacVideoTotalCallsAP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 34),
    _CLQd11CacVideoTotalCallsAP_Type()
)
cLQd11CacVideoTotalCallsAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11CacVideoTotalCallsAP.setStatus("current")
_CLQd11CacVideoTotalRoamCallsAP_Type = Counter32
_CLQd11CacVideoTotalRoamCallsAP_Object = MibTableColumn
cLQd11CacVideoTotalRoamCallsAP = _CLQd11CacVideoTotalRoamCallsAP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 35),
    _CLQd11CacVideoTotalRoamCallsAP_Type()
)
cLQd11CacVideoTotalRoamCallsAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11CacVideoTotalRoamCallsAP.setStatus("current")
_CLQd11CacVideoCallsRejectedAP_Type = Counter32
_CLQd11CacVideoCallsRejectedAP_Object = MibTableColumn
cLQd11CacVideoCallsRejectedAP = _CLQd11CacVideoCallsRejectedAP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 36),
    _CLQd11CacVideoCallsRejectedAP_Type()
)
cLQd11CacVideoCallsRejectedAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11CacVideoCallsRejectedAP.setStatus("current")
_CLQd11CacVideoRoamCallsRejectedAP_Type = Counter32
_CLQd11CacVideoRoamCallsRejectedAP_Object = MibTableColumn
cLQd11CacVideoRoamCallsRejectedAP = _CLQd11CacVideoRoamCallsRejectedAP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 37),
    _CLQd11CacVideoRoamCallsRejectedAP_Type()
)
cLQd11CacVideoRoamCallsRejectedAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11CacVideoRoamCallsRejectedAP.setStatus("current")
_CLQd11CacVideoRejCallsInsufBw_Type = Counter32
_CLQd11CacVideoRejCallsInsufBw_Object = MibTableColumn
cLQd11CacVideoRejCallsInsufBw = _CLQd11CacVideoRejCallsInsufBw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 38),
    _CLQd11CacVideoRejCallsInsufBw_Type()
)
cLQd11CacVideoRejCallsInsufBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11CacVideoRejCallsInsufBw.setStatus("current")
_CLQd11CacVideoRejCallsBadParams_Type = Counter32
_CLQd11CacVideoRejCallsBadParams_Object = MibTableColumn
cLQd11CacVideoRejCallsBadParams = _CLQd11CacVideoRejCallsBadParams_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 39),
    _CLQd11CacVideoRejCallsBadParams_Type()
)
cLQd11CacVideoRejCallsBadParams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11CacVideoRejCallsBadParams.setStatus("current")
_CLQd11CacVideoRejCallsPhyRate_Type = Counter32
_CLQd11CacVideoRejCallsPhyRate_Object = MibTableColumn
cLQd11CacVideoRejCallsPhyRate = _CLQd11CacVideoRejCallsPhyRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 40),
    _CLQd11CacVideoRejCallsPhyRate_Type()
)
cLQd11CacVideoRejCallsPhyRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11CacVideoRejCallsPhyRate.setStatus("current")
_CLQd11CacVideoRejCallsQosPolicy_Type = Counter32
_CLQd11CacVideoRejCallsQosPolicy_Object = MibTableColumn
cLQd11CacVideoRejCallsQosPolicy = _CLQd11CacVideoRejCallsQosPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 41),
    _CLQd11CacVideoRejCallsQosPolicy_Type()
)
cLQd11CacVideoRejCallsQosPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11CacVideoRejCallsQosPolicy.setStatus("current")
_CLQd11SipCacVideoCallsInProgress_Type = Gauge32
_CLQd11SipCacVideoCallsInProgress_Object = MibTableColumn
cLQd11SipCacVideoCallsInProgress = _CLQd11SipCacVideoCallsInProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 42),
    _CLQd11SipCacVideoCallsInProgress_Type()
)
cLQd11SipCacVideoCallsInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11SipCacVideoCallsInProgress.setStatus("current")
_CLQd11SipCacVideoRoamCallsInProg_Type = Gauge32
_CLQd11SipCacVideoRoamCallsInProg_Object = MibTableColumn
cLQd11SipCacVideoRoamCallsInProg = _CLQd11SipCacVideoRoamCallsInProg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 43),
    _CLQd11SipCacVideoRoamCallsInProg_Type()
)
cLQd11SipCacVideoRoamCallsInProg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11SipCacVideoRoamCallsInProg.setStatus("current")
_CLQd11SipCacVideoTotalCallsAP_Type = Counter32
_CLQd11SipCacVideoTotalCallsAP_Object = MibTableColumn
cLQd11SipCacVideoTotalCallsAP = _CLQd11SipCacVideoTotalCallsAP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 44),
    _CLQd11SipCacVideoTotalCallsAP_Type()
)
cLQd11SipCacVideoTotalCallsAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11SipCacVideoTotalCallsAP.setStatus("current")
_CLQd11SipCacVideoTotalRoamCallsAP_Type = Counter32
_CLQd11SipCacVideoTotalRoamCallsAP_Object = MibTableColumn
cLQd11SipCacVideoTotalRoamCallsAP = _CLQd11SipCacVideoTotalRoamCallsAP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 45),
    _CLQd11SipCacVideoTotalRoamCallsAP_Type()
)
cLQd11SipCacVideoTotalRoamCallsAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11SipCacVideoTotalRoamCallsAP.setStatus("current")
_CLQd11SipCacVideoCallsRejectedInSuffBw_Type = Counter32
_CLQd11SipCacVideoCallsRejectedInSuffBw_Object = MibTableColumn
cLQd11SipCacVideoCallsRejectedInSuffBw = _CLQd11SipCacVideoCallsRejectedInSuffBw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 46),
    _CLQd11SipCacVideoCallsRejectedInSuffBw_Type()
)
cLQd11SipCacVideoCallsRejectedInSuffBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11SipCacVideoCallsRejectedInSuffBw.setStatus("current")
_CLQd11SipCacVideoRoamCallsRejectedInSuffBw_Type = Counter32
_CLQd11SipCacVideoRoamCallsRejectedInSuffBw_Object = MibTableColumn
cLQd11SipCacVideoRoamCallsRejectedInSuffBw = _CLQd11SipCacVideoRoamCallsRejectedInSuffBw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 47),
    _CLQd11SipCacVideoRoamCallsRejectedInSuffBw_Type()
)
cLQd11SipCacVideoRoamCallsRejectedInSuffBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11SipCacVideoRoamCallsRejectedInSuffBw.setStatus("current")
_CLQEntConfConfig_ObjectIdentity = ObjectIdentity
cLQEntConfConfig = _CLQEntConfConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 5)
)
_CLQd11VoiceStats_ObjectIdentity = ObjectIdentity
cLQd11VoiceStats = _CLQd11VoiceStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 6)
)
_CLQd11VoiceStatsTable_Object = MibTable
cLQd11VoiceStatsTable = _CLQd11VoiceStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 6, 1)
)
if mibBuilder.loadTexts:
    cLQd11VoiceStatsTable.setStatus("current")
_CLQd11VoiceStatsEntry_Object = MibTableRow
cLQd11VoiceStatsEntry = _CLQd11VoiceStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 6, 1, 1)
)
cLQd11VoiceStatsEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"),
)
if mibBuilder.loadTexts:
    cLQd11VoiceStatsEntry.setStatus("current")
_CLQd11VoiceCallCounts_Type = Counter32
_CLQd11VoiceCallCounts_Object = MibTableColumn
cLQd11VoiceCallCounts = _CLQd11VoiceCallCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 6, 1, 1, 1),
    _CLQd11VoiceCallCounts_Type()
)
cLQd11VoiceCallCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11VoiceCallCounts.setStatus("current")
if mibBuilder.loadTexts:
    cLQd11VoiceCallCounts.setUnits("calls")
_CLQd11CacVoiceCallTimePeriod_Type = TimeIntervalSec
_CLQd11CacVoiceCallTimePeriod_Object = MibTableColumn
cLQd11CacVoiceCallTimePeriod = _CLQd11CacVoiceCallTimePeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 6, 1, 1, 2),
    _CLQd11CacVoiceCallTimePeriod_Type()
)
cLQd11CacVoiceCallTimePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11CacVoiceCallTimePeriod.setStatus("current")
if mibBuilder.loadTexts:
    cLQd11CacVoiceCallTimePeriod.setUnits("seconds")
_CLQVoiceWlanConfig_ObjectIdentity = ObjectIdentity
cLQVoiceWlanConfig = _CLQVoiceWlanConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 7)
)
_CLQVoiceWlanConfigTable_Object = MibTable
cLQVoiceWlanConfigTable = _CLQVoiceWlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 7, 1)
)
if mibBuilder.loadTexts:
    cLQVoiceWlanConfigTable.setStatus("current")
_CLQVoiceWlanConfigEntry_Object = MibTableRow
cLQVoiceWlanConfigEntry = _CLQVoiceWlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 7, 1, 1)
)
cLQVoiceWlanConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"),
)
if mibBuilder.loadTexts:
    cLQVoiceWlanConfigEntry.setStatus("current")


class _CLQVoiceWlanConfigDetectVoipCallFailure_Type(TruthValue):
    """Custom type cLQVoiceWlanConfigDetectVoipCallFailure based on TruthValue"""
    defaultValue = 2


_CLQVoiceWlanConfigDetectVoipCallFailure_Type.__name__ = "TruthValue"
_CLQVoiceWlanConfigDetectVoipCallFailure_Object = MibTableColumn
cLQVoiceWlanConfigDetectVoipCallFailure = _CLQVoiceWlanConfigDetectVoipCallFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 7, 1, 1, 1),
    _CLQVoiceWlanConfigDetectVoipCallFailure_Type()
)
cLQVoiceWlanConfigDetectVoipCallFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQVoiceWlanConfigDetectVoipCallFailure.setStatus("current")
_CLQVoiceClient_ObjectIdentity = ObjectIdentity
cLQVoiceClient = _CLQVoiceClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 8)
)
_CLQVoiceClientTable_Object = MibTable
cLQVoiceClientTable = _CLQVoiceClientTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 8, 1)
)
if mibBuilder.loadTexts:
    cLQVoiceClientTable.setStatus("current")
_CLQVoiceClientEntry_Object = MibTableRow
cLQVoiceClientEntry = _CLQVoiceClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 8, 1, 1)
)
cLQVoiceClientEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
)
if mibBuilder.loadTexts:
    cLQVoiceClientEntry.setStatus("current")
_CLQVoiceClientCallingNumber_Type = SnmpAdminString
_CLQVoiceClientCallingNumber_Object = MibTableColumn
cLQVoiceClientCallingNumber = _CLQVoiceClientCallingNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 8, 1, 1, 1),
    _CLQVoiceClientCallingNumber_Type()
)
cLQVoiceClientCallingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQVoiceClientCallingNumber.setStatus("current")
_CLQVoiceClientLastCalledNumber_Type = SnmpAdminString
_CLQVoiceClientLastCalledNumber_Object = MibTableColumn
cLQVoiceClientLastCalledNumber = _CLQVoiceClientLastCalledNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 8, 1, 1, 2),
    _CLQVoiceClientLastCalledNumber_Type()
)
cLQVoiceClientLastCalledNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQVoiceClientLastCalledNumber.setStatus("current")


class _CLQVoiceClientLastCallFailureReasonCode_Type(Integer32):
    """Custom type cLQVoiceClientLastCallFailureReasonCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              400,
              401,
              402,
              403,
              404,
              405,
              406,
              407,
              408,
              409,
              410,
              411,
              413,
              414,
              415,
              420,
              480,
              481,
              482,
              483,
              484,
              485,
              486,
              500,
              501,
              502,
              503,
              504,
              505,
              600,
              603,
              604,
              606)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("normalFailure", 2),
          ("roamFailure", 3),
          ("maxLimitExceeded", 4),
          ("sipPrefCallNoBw", 5),
          ("badRequest", 400),
          ("unauthorized", 401),
          ("paymentRequired", 402),
          ("forbidden", 403),
          ("notFound", 404),
          ("methodNotallowed", 405),
          ("notAcceptable", 406),
          ("proxyAuthenticationRequired", 407),
          ("requestTimeout", 408),
          ("conflict", 409),
          ("gone", 410),
          ("lengthRequired", 411),
          ("requestEntityTooLarge", 413),
          ("requestURITooLarge", 414),
          ("unsupportedMdediaType", 415),
          ("badExtension", 420),
          ("temporarilyNotAvailable", 480),
          ("callLegDoesNotExist", 481),
          ("loopDetected", 482),
          ("tooManyHops", 483),
          ("addressIncomplete", 484),
          ("ambiguous", 485),
          ("busy", 486),
          ("internalServerError", 500),
          ("notImplemented", 501),
          ("badGateway", 502),
          ("serviceUnavailable", 503),
          ("serverTimeout", 504),
          ("versionNotSupported", 505),
          ("busyEverywhere", 600),
          ("decline", 603),
          ("doesNotExistAnywhere", 604),
          ("sessionNotAcceptable", 606))
    )


_CLQVoiceClientLastCallFailureReasonCode_Type.__name__ = "Integer32"
_CLQVoiceClientLastCallFailureReasonCode_Object = MibTableColumn
cLQVoiceClientLastCallFailureReasonCode = _CLQVoiceClientLastCallFailureReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 8, 1, 1, 3),
    _CLQVoiceClientLastCallFailureReasonCode_Type()
)
cLQVoiceClientLastCallFailureReasonCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQVoiceClientLastCallFailureReasonCode.setStatus("current")
_CLQd11SipCacConfig_ObjectIdentity = ObjectIdentity
cLQd11SipCacConfig = _CLQd11SipCacConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 9)
)
_CLQd11SipCacConfigTable_Object = MibTable
cLQd11SipCacConfigTable = _CLQd11SipCacConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 9, 1)
)
if mibBuilder.loadTexts:
    cLQd11SipCacConfigTable.setStatus("current")
_CLQd11SipCacConfigEntry_Object = MibTableRow
cLQd11SipCacConfigEntry = _CLQd11SipCacConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 9, 1, 1)
)
cLQd11SipCacConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApDot11IfType"),
)
if mibBuilder.loadTexts:
    cLQd11SipCacConfigEntry.setStatus("current")


class _CLQd11SipCacConfigCodecType_Type(Integer32):
    """Custom type cLQd11SipCacConfigCodecType based on Integer32"""
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
        *(("userDefined", 1),
          ("g711", 2),
          ("g729", 3))
    )


_CLQd11SipCacConfigCodecType_Type.__name__ = "Integer32"
_CLQd11SipCacConfigCodecType_Object = MibTableColumn
cLQd11SipCacConfigCodecType = _CLQd11SipCacConfigCodecType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 9, 1, 1, 1),
    _CLQd11SipCacConfigCodecType_Type()
)
cLQd11SipCacConfigCodecType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11SipCacConfigCodecType.setStatus("current")
_CLQd11SipCacConfigBw_Type = Unsigned32
_CLQd11SipCacConfigBw_Object = MibTableColumn
cLQd11SipCacConfigBw = _CLQd11SipCacConfigBw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 9, 1, 1, 2),
    _CLQd11SipCacConfigBw_Type()
)
cLQd11SipCacConfigBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11SipCacConfigBw.setStatus("current")
if mibBuilder.loadTexts:
    cLQd11SipCacConfigBw.setUnits("kbps")
_CLQd11SipCacConfigVoiceSampleSize_Type = Unsigned32
_CLQd11SipCacConfigVoiceSampleSize_Object = MibTableColumn
cLQd11SipCacConfigVoiceSampleSize = _CLQd11SipCacConfigVoiceSampleSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 9, 1, 1, 3),
    _CLQd11SipCacConfigVoiceSampleSize_Type()
)
cLQd11SipCacConfigVoiceSampleSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11SipCacConfigVoiceSampleSize.setStatus("current")
if mibBuilder.loadTexts:
    cLQd11SipCacConfigVoiceSampleSize.setUnits("milliseconds")
_CLQd11SipCacMaxPossibleVoiceCalls_Type = Unsigned32
_CLQd11SipCacMaxPossibleVoiceCalls_Object = MibTableColumn
cLQd11SipCacMaxPossibleVoiceCalls = _CLQd11SipCacMaxPossibleVoiceCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 9, 1, 1, 4),
    _CLQd11SipCacMaxPossibleVoiceCalls_Type()
)
cLQd11SipCacMaxPossibleVoiceCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11SipCacMaxPossibleVoiceCalls.setStatus("current")
_CLQd11SipCacMaxPossibleReservedRoamingCalls_Type = Unsigned32
_CLQd11SipCacMaxPossibleReservedRoamingCalls_Object = MibTableColumn
cLQd11SipCacMaxPossibleReservedRoamingCalls = _CLQd11SipCacMaxPossibleReservedRoamingCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 9, 1, 1, 5),
    _CLQd11SipCacMaxPossibleReservedRoamingCalls_Type()
)
cLQd11SipCacMaxPossibleReservedRoamingCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11SipCacMaxPossibleReservedRoamingCalls.setStatus("current")
_CLQConfigObjects_ObjectIdentity = ObjectIdentity
cLQConfigObjects = _CLQConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 10)
)
_CiscoLwappVoipCallFailureNotifEnabled_Type = TruthValue
_CiscoLwappVoipCallFailureNotifEnabled_Object = MibScalar
ciscoLwappVoipCallFailureNotifEnabled = _CiscoLwappVoipCallFailureNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 10, 1),
    _CiscoLwappVoipCallFailureNotifEnabled_Type()
)
ciscoLwappVoipCallFailureNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoLwappVoipCallFailureNotifEnabled.setStatus("current")
_CiscoLwappKtsVoipCallFailureNotifEnabled_Type = TruthValue
_CiscoLwappKtsVoipCallFailureNotifEnabled_Object = MibScalar
ciscoLwappKtsVoipCallFailureNotifEnabled = _CiscoLwappKtsVoipCallFailureNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 10, 2),
    _CiscoLwappKtsVoipCallFailureNotifEnabled_Type()
)
ciscoLwappKtsVoipCallFailureNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoLwappKtsVoipCallFailureNotifEnabled.setStatus("current")
_CLQMediaClient_ObjectIdentity = ObjectIdentity
cLQMediaClient = _CLQMediaClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 11)
)
_CLQMediaClientTable_Object = MibTable
cLQMediaClientTable = _CLQMediaClientTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 11, 1)
)
if mibBuilder.loadTexts:
    cLQMediaClientTable.setStatus("current")
_CLQMediaClientEntry_Object = MibTableRow
cLQMediaClientEntry = _CLQMediaClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 11, 1, 1)
)
cLQMediaClientEntry.setIndexNames(
    (0, "CISCO-LWAPP-QOS-MIB", "cLQMStreamName"),
    (0, "CISCO-LWAPP-QOS-MIB", "cLQVMediaClientDestIpAddrType"),
    (0, "CISCO-LWAPP-QOS-MIB", "cLQVMediaClientDestIpAddr"),
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
)
if mibBuilder.loadTexts:
    cLQMediaClientEntry.setStatus("current")
_CLQVMediaClientDestIpAddrType_Type = InetAddressType
_CLQVMediaClientDestIpAddrType_Object = MibTableColumn
cLQVMediaClientDestIpAddrType = _CLQVMediaClientDestIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 11, 1, 1, 1),
    _CLQVMediaClientDestIpAddrType_Type()
)
cLQVMediaClientDestIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLQVMediaClientDestIpAddrType.setStatus("current")
_CLQVMediaClientDestIpAddr_Type = InetAddress
_CLQVMediaClientDestIpAddr_Object = MibTableColumn
cLQVMediaClientDestIpAddr = _CLQVMediaClientDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 11, 1, 1, 2),
    _CLQVMediaClientDestIpAddr_Type()
)
cLQVMediaClientDestIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLQVMediaClientDestIpAddr.setStatus("current")
_CLQVMediaClientSrcIpAddrType_Type = InetAddressType
_CLQVMediaClientSrcIpAddrType_Object = MibTableColumn
cLQVMediaClientSrcIpAddrType = _CLQVMediaClientSrcIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 11, 1, 1, 3),
    _CLQVMediaClientSrcIpAddrType_Type()
)
cLQVMediaClientSrcIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQVMediaClientSrcIpAddrType.setStatus("current")
_CLQVMediaClientSrcIpAddr_Type = InetAddress
_CLQVMediaClientSrcIpAddr_Object = MibTableColumn
cLQVMediaClientSrcIpAddr = _CLQVMediaClientSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 11, 1, 1, 4),
    _CLQVMediaClientSrcIpAddr_Type()
)
cLQVMediaClientSrcIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQVMediaClientSrcIpAddr.setStatus("current")
_CLQVMediaClientApMacAddress_Type = MacAddress
_CLQVMediaClientApMacAddress_Object = MibTableColumn
cLQVMediaClientApMacAddress = _CLQVMediaClientApMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 11, 1, 1, 5),
    _CLQVMediaClientApMacAddress_Type()
)
cLQVMediaClientApMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQVMediaClientApMacAddress.setStatus("current")
_CLQVMediaClientWlanIndex_Type = Unsigned32
_CLQVMediaClientWlanIndex_Object = MibTableColumn
cLQVMediaClientWlanIndex = _CLQVMediaClientWlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 11, 1, 1, 6),
    _CLQVMediaClientWlanIndex_Type()
)
cLQVMediaClientWlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQVMediaClientWlanIndex.setStatus("current")


class _CLQVMediaClientRadioType_Type(Integer32):
    """Custom type cLQVMediaClientRadioType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("radio80211bg", 1),
          ("radio80211a", 2))
    )


_CLQVMediaClientRadioType_Type.__name__ = "Integer32"
_CLQVMediaClientRadioType_Object = MibTableColumn
cLQVMediaClientRadioType = _CLQVMediaClientRadioType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 11, 1, 1, 7),
    _CLQVMediaClientRadioType_Type()
)
cLQVMediaClientRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQVMediaClientRadioType.setStatus("current")


class _CLQVMediaClientQos_Type(Integer32):
    """Custom type cLQVMediaClientQos based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("besteffort", 1),
          ("background", 2),
          ("undefined", 3),
          ("excellenteffort", 4),
          ("ctrlload", 5),
          ("video", 6),
          ("voice", 7),
          ("network", 8))
    )


_CLQVMediaClientQos_Type.__name__ = "Integer32"
_CLQVMediaClientQos_Object = MibTableColumn
cLQVMediaClientQos = _CLQVMediaClientQos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 11, 1, 1, 8),
    _CLQVMediaClientQos_Type()
)
cLQVMediaClientQos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQVMediaClientQos.setStatus("current")


class _CLQVMediaClientDecision_Type(Integer32):
    """Custom type cLQVMediaClientDecision based on Integer32"""
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
        *(("deny", 1),
          ("admit", 2),
          ("badClientDeny", 3),
          ("badClientDemote", 4))
    )


_CLQVMediaClientDecision_Type.__name__ = "Integer32"
_CLQVMediaClientDecision_Object = MibTableColumn
cLQVMediaClientDecision = _CLQVMediaClientDecision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 11, 1, 1, 9),
    _CLQVMediaClientDecision_Type()
)
cLQVMediaClientDecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQVMediaClientDecision.setStatus("current")
_CLQMediaClientHistoryTable_Object = MibTable
cLQMediaClientHistoryTable = _CLQMediaClientHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 11, 2)
)
if mibBuilder.loadTexts:
    cLQMediaClientHistoryTable.setStatus("current")
_CLQMediaClientHistoryEntry_Object = MibTableRow
cLQMediaClientHistoryEntry = _CLQMediaClientHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 11, 2, 1)
)
cLQMediaClientHistoryEntry.setIndexNames(
    (0, "CISCO-LWAPP-QOS-MIB", "cLQVMediaClientHistTimeStamp"),
)
if mibBuilder.loadTexts:
    cLQMediaClientHistoryEntry.setStatus("current")
_CLQVMediaClientHistTimeStamp_Type = TimeStamp
_CLQVMediaClientHistTimeStamp_Object = MibTableColumn
cLQVMediaClientHistTimeStamp = _CLQVMediaClientHistTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 11, 2, 1, 1),
    _CLQVMediaClientHistTimeStamp_Type()
)
cLQVMediaClientHistTimeStamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLQVMediaClientHistTimeStamp.setStatus("current")
_CLQVMediaClientHistClientMacAddress_Type = MacAddress
_CLQVMediaClientHistClientMacAddress_Object = MibTableColumn
cLQVMediaClientHistClientMacAddress = _CLQVMediaClientHistClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 11, 2, 1, 2),
    _CLQVMediaClientHistClientMacAddress_Type()
)
cLQVMediaClientHistClientMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQVMediaClientHistClientMacAddress.setStatus("current")
_CLQVMediaClientHistApMacAddress_Type = MacAddress
_CLQVMediaClientHistApMacAddress_Object = MibTableColumn
cLQVMediaClientHistApMacAddress = _CLQVMediaClientHistApMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 11, 2, 1, 3),
    _CLQVMediaClientHistApMacAddress_Type()
)
cLQVMediaClientHistApMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQVMediaClientHistApMacAddress.setStatus("current")
_CLQVMediaClientHistSlotId_Type = Unsigned32
_CLQVMediaClientHistSlotId_Object = MibTableColumn
cLQVMediaClientHistSlotId = _CLQVMediaClientHistSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 11, 2, 1, 4),
    _CLQVMediaClientHistSlotId_Type()
)
cLQVMediaClientHistSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQVMediaClientHistSlotId.setStatus("current")
_CLQVMediaClientHistSrcIpAddr_Type = IpAddress
_CLQVMediaClientHistSrcIpAddr_Object = MibTableColumn
cLQVMediaClientHistSrcIpAddr = _CLQVMediaClientHistSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 11, 2, 1, 5),
    _CLQVMediaClientHistSrcIpAddr_Type()
)
cLQVMediaClientHistSrcIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQVMediaClientHistSrcIpAddr.setStatus("deprecated")
_CLQVMediaClientHistDestIpAddr_Type = IpAddress
_CLQVMediaClientHistDestIpAddr_Object = MibTableColumn
cLQVMediaClientHistDestIpAddr = _CLQVMediaClientHistDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 11, 2, 1, 6),
    _CLQVMediaClientHistDestIpAddr_Type()
)
cLQVMediaClientHistDestIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQVMediaClientHistDestIpAddr.setStatus("deprecated")


class _CLQVMediaClientHistDecision_Type(Integer32):
    """Custom type cLQVMediaClientHistDecision based on Integer32"""
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
        *(("deny", 1),
          ("admit", 2),
          ("badClientDeny", 3),
          ("badClientDemote", 4))
    )


_CLQVMediaClientHistDecision_Type.__name__ = "Integer32"
_CLQVMediaClientHistDecision_Object = MibTableColumn
cLQVMediaClientHistDecision = _CLQVMediaClientHistDecision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 11, 2, 1, 7),
    _CLQVMediaClientHistDecision_Type()
)
cLQVMediaClientHistDecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQVMediaClientHistDecision.setStatus("current")


class _CLQVMediaClientHistLastFailureReasonCode_Type(Integer32):
    """Custom type cLQVMediaClientHistLastFailureReasonCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("enoughBw", 1),
          ("notEnoughBw", 2),
          ("bwViolation", 3),
          ("radioOverSubscribe", 4),
          ("badClientLink", 5),
          ("policyNotAllowed", 6),
          ("otherErrors", 7),
          ("clientDemote", 8),
          ("clientTimeout", 9),
          ("clientLeave", 10))
    )


_CLQVMediaClientHistLastFailureReasonCode_Type.__name__ = "Integer32"
_CLQVMediaClientHistLastFailureReasonCode_Object = MibTableColumn
cLQVMediaClientHistLastFailureReasonCode = _CLQVMediaClientHistLastFailureReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 11, 2, 1, 8),
    _CLQVMediaClientHistLastFailureReasonCode_Type()
)
cLQVMediaClientHistLastFailureReasonCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQVMediaClientHistLastFailureReasonCode.setStatus("current")


class _CLQVMediaClientHistWlanIndex_Type(Unsigned32):
    """Custom type cLQVMediaClientHistWlanIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 517),
    )


_CLQVMediaClientHistWlanIndex_Type.__name__ = "Unsigned32"
_CLQVMediaClientHistWlanIndex_Object = MibTableColumn
cLQVMediaClientHistWlanIndex = _CLQVMediaClientHistWlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 11, 2, 1, 9),
    _CLQVMediaClientHistWlanIndex_Type()
)
cLQVMediaClientHistWlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQVMediaClientHistWlanIndex.setStatus("current")


class _CLQVMediaClientHistRadioType_Type(Integer32):
    """Custom type cLQVMediaClientHistRadioType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("radio80211bg", 1),
          ("radio80211a", 2))
    )


_CLQVMediaClientHistRadioType_Type.__name__ = "Integer32"
_CLQVMediaClientHistRadioType_Object = MibTableColumn
cLQVMediaClientHistRadioType = _CLQVMediaClientHistRadioType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 11, 2, 1, 10),
    _CLQVMediaClientHistRadioType_Type()
)
cLQVMediaClientHistRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQVMediaClientHistRadioType.setStatus("current")


class _CLQVMediaClientHistQos_Type(Integer32):
    """Custom type cLQVMediaClientHistQos based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("besteffort", 1),
          ("background", 2),
          ("undefined", 3),
          ("excellenteffort", 4),
          ("ctrlload", 5),
          ("video", 6),
          ("voice", 7),
          ("network", 8))
    )


_CLQVMediaClientHistQos_Type.__name__ = "Integer32"
_CLQVMediaClientHistQos_Object = MibTableColumn
cLQVMediaClientHistQos = _CLQVMediaClientHistQos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 11, 2, 1, 11),
    _CLQVMediaClientHistQos_Type()
)
cLQVMediaClientHistQos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQVMediaClientHistQos.setStatus("current")
_CLQVMediaClientHistCfgBw_Type = Unsigned32
_CLQVMediaClientHistCfgBw_Object = MibTableColumn
cLQVMediaClientHistCfgBw = _CLQVMediaClientHistCfgBw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 11, 2, 1, 12),
    _CLQVMediaClientHistCfgBw_Type()
)
cLQVMediaClientHistCfgBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQVMediaClientHistCfgBw.setStatus("current")
_CLQVMediaClientHistCurrentRate_Type = Unsigned32
_CLQVMediaClientHistCurrentRate_Object = MibTableColumn
cLQVMediaClientHistCurrentRate = _CLQVMediaClientHistCurrentRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 11, 2, 1, 13),
    _CLQVMediaClientHistCurrentRate_Type()
)
cLQVMediaClientHistCurrentRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQVMediaClientHistCurrentRate.setStatus("current")
_CLQVMediaClientHistVideoPktSize_Type = Unsigned32
_CLQVMediaClientHistVideoPktSize_Object = MibTableColumn
cLQVMediaClientHistVideoPktSize = _CLQVMediaClientHistVideoPktSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 11, 2, 1, 14),
    _CLQVMediaClientHistVideoPktSize_Type()
)
cLQVMediaClientHistVideoPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQVMediaClientHistVideoPktSize.setStatus("current")
_CLQVMediaClientHistVideoUtil_Type = Unsigned32
_CLQVMediaClientHistVideoUtil_Object = MibTableColumn
cLQVMediaClientHistVideoUtil = _CLQVMediaClientHistVideoUtil_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 11, 2, 1, 15),
    _CLQVMediaClientHistVideoUtil_Type()
)
cLQVMediaClientHistVideoUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQVMediaClientHistVideoUtil.setStatus("current")
_CLQVMediaClientHistVoiceUtil_Type = Unsigned32
_CLQVMediaClientHistVoiceUtil_Object = MibTableColumn
cLQVMediaClientHistVoiceUtil = _CLQVMediaClientHistVoiceUtil_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 11, 2, 1, 16),
    _CLQVMediaClientHistVoiceUtil_Type()
)
cLQVMediaClientHistVoiceUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQVMediaClientHistVoiceUtil.setStatus("current")
_CLQVMediaClientHistChannelUtil_Type = Unsigned32
_CLQVMediaClientHistChannelUtil_Object = MibTableColumn
cLQVMediaClientHistChannelUtil = _CLQVMediaClientHistChannelUtil_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 11, 2, 1, 17),
    _CLQVMediaClientHistChannelUtil_Type()
)
cLQVMediaClientHistChannelUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQVMediaClientHistChannelUtil.setStatus("current")
_CLQVMediaClientHistQueueUtil_Type = Unsigned32
_CLQVMediaClientHistQueueUtil_Object = MibTableColumn
cLQVMediaClientHistQueueUtil = _CLQVMediaClientHistQueueUtil_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 11, 2, 1, 18),
    _CLQVMediaClientHistQueueUtil_Type()
)
cLQVMediaClientHistQueueUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQVMediaClientHistQueueUtil.setStatus("current")
_CLQVMediaClientHistVideoPps_Type = Unsigned32
_CLQVMediaClientHistVideoPps_Object = MibTableColumn
cLQVMediaClientHistVideoPps = _CLQVMediaClientHistVideoPps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 11, 2, 1, 19),
    _CLQVMediaClientHistVideoPps_Type()
)
cLQVMediaClientHistVideoPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQVMediaClientHistVideoPps.setStatus("current")
_CLQVMediaClientHistVideoDelay_Type = Unsigned32
_CLQVMediaClientHistVideoDelay_Object = MibTableColumn
cLQVMediaClientHistVideoDelay = _CLQVMediaClientHistVideoDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 11, 2, 1, 20),
    _CLQVMediaClientHistVideoDelay_Type()
)
cLQVMediaClientHistVideoDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQVMediaClientHistVideoDelay.setStatus("current")
_CLQVMediaClientHistPktLossDiscard_Type = Unsigned32
_CLQVMediaClientHistPktLossDiscard_Object = MibTableColumn
cLQVMediaClientHistPktLossDiscard = _CLQVMediaClientHistPktLossDiscard_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 11, 2, 1, 21),
    _CLQVMediaClientHistPktLossDiscard_Type()
)
cLQVMediaClientHistPktLossDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQVMediaClientHistPktLossDiscard.setStatus("current")
_CLQVMediaClientHistPktLossFail_Type = Unsigned32
_CLQVMediaClientHistPktLossFail_Object = MibTableColumn
cLQVMediaClientHistPktLossFail = _CLQVMediaClientHistPktLossFail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 11, 2, 1, 22),
    _CLQVMediaClientHistPktLossFail_Type()
)
cLQVMediaClientHistPktLossFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQVMediaClientHistPktLossFail.setStatus("current")
_CLQVMediaClientHistNumVideoStreams_Type = Unsigned32
_CLQVMediaClientHistNumVideoStreams_Object = MibTableColumn
cLQVMediaClientHistNumVideoStreams = _CLQVMediaClientHistNumVideoStreams_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 11, 2, 1, 23),
    _CLQVMediaClientHistNumVideoStreams_Type()
)
cLQVMediaClientHistNumVideoStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQVMediaClientHistNumVideoStreams.setStatus("current")


class _CLQVMediaClientHistCacEnable_Type(Integer32):
    """Custom type cLQVMediaClientHistCacEnable based on Integer32"""
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
        *(("video", 1),
          ("voice", 2),
          ("videoAndVoice", 3),
          ("none", 4))
    )


_CLQVMediaClientHistCacEnable_Type.__name__ = "Integer32"
_CLQVMediaClientHistCacEnable_Object = MibTableColumn
cLQVMediaClientHistCacEnable = _CLQVMediaClientHistCacEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 11, 2, 1, 24),
    _CLQVMediaClientHistCacEnable_Type()
)
cLQVMediaClientHistCacEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQVMediaClientHistCacEnable.setStatus("current")
_CLQVMediaClientHistStreamName_Type = SnmpAdminString
_CLQVMediaClientHistStreamName_Object = MibTableColumn
cLQVMediaClientHistStreamName = _CLQVMediaClientHistStreamName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 11, 2, 1, 25),
    _CLQVMediaClientHistStreamName_Type()
)
cLQVMediaClientHistStreamName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQVMediaClientHistStreamName.setStatus("current")
_CLQVMediaClientHistSrcInetAddrType_Type = InetAddressType
_CLQVMediaClientHistSrcInetAddrType_Object = MibTableColumn
cLQVMediaClientHistSrcInetAddrType = _CLQVMediaClientHistSrcInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 11, 2, 1, 26),
    _CLQVMediaClientHistSrcInetAddrType_Type()
)
cLQVMediaClientHistSrcInetAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQVMediaClientHistSrcInetAddrType.setStatus("current")
_CLQVMediaClientHistSrcInetAddr_Type = InetAddress
_CLQVMediaClientHistSrcInetAddr_Object = MibTableColumn
cLQVMediaClientHistSrcInetAddr = _CLQVMediaClientHistSrcInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 11, 2, 1, 27),
    _CLQVMediaClientHistSrcInetAddr_Type()
)
cLQVMediaClientHistSrcInetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQVMediaClientHistSrcInetAddr.setStatus("current")
_CLQVMediaClientHistDestInetAddrType_Type = InetAddressType
_CLQVMediaClientHistDestInetAddrType_Object = MibTableColumn
cLQVMediaClientHistDestInetAddrType = _CLQVMediaClientHistDestInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 11, 2, 1, 28),
    _CLQVMediaClientHistDestInetAddrType_Type()
)
cLQVMediaClientHistDestInetAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQVMediaClientHistDestInetAddrType.setStatus("current")
_CLQVMediaClientHistDestInetAddr_Type = InetAddress
_CLQVMediaClientHistDestInetAddr_Object = MibTableColumn
cLQVMediaClientHistDestInetAddr = _CLQVMediaClientHistDestInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 11, 2, 1, 29),
    _CLQVMediaClientHistDestInetAddr_Type()
)
cLQVMediaClientHistDestInetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQVMediaClientHistDestInetAddr.setStatus("current")
_CLQMediaMulticastClientTable_Object = MibTable
cLQMediaMulticastClientTable = _CLQMediaMulticastClientTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 11, 3)
)
if mibBuilder.loadTexts:
    cLQMediaMulticastClientTable.setStatus("current")
_CLQMediaMulticastClientEntry_Object = MibTableRow
cLQMediaMulticastClientEntry = _CLQMediaMulticastClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 11, 3, 1)
)
cLQMediaMulticastClientEntry.setIndexNames(
    (0, "CISCO-LWAPP-QOS-MIB", "cLQMStreamName"),
    (0, "CISCO-LWAPP-QOS-MIB", "cLQVMediaClientMCGrpIpAddrType"),
    (0, "CISCO-LWAPP-QOS-MIB", "cLQVMediaClientMCGrpIpAddr"),
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
)
if mibBuilder.loadTexts:
    cLQMediaMulticastClientEntry.setStatus("current")
_CLQVMediaClientMCGrpIpAddrType_Type = InetAddressType
_CLQVMediaClientMCGrpIpAddrType_Object = MibTableColumn
cLQVMediaClientMCGrpIpAddrType = _CLQVMediaClientMCGrpIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 11, 3, 1, 1),
    _CLQVMediaClientMCGrpIpAddrType_Type()
)
cLQVMediaClientMCGrpIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLQVMediaClientMCGrpIpAddrType.setStatus("current")
_CLQVMediaClientMCGrpIpAddr_Type = InetAddress
_CLQVMediaClientMCGrpIpAddr_Object = MibTableColumn
cLQVMediaClientMCGrpIpAddr = _CLQVMediaClientMCGrpIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 11, 3, 1, 2),
    _CLQVMediaClientMCGrpIpAddr_Type()
)
cLQVMediaClientMCGrpIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLQVMediaClientMCGrpIpAddr.setStatus("current")
_CLQVMediaClientVlanId_Type = Unsigned32
_CLQVMediaClientVlanId_Object = MibTableColumn
cLQVMediaClientVlanId = _CLQVMediaClientVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 11, 3, 1, 3),
    _CLQVMediaClientVlanId_Type()
)
cLQVMediaClientVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQVMediaClientVlanId.setStatus("current")
_CLQVMediaMCClientApName_Type = SnmpAdminString
_CLQVMediaMCClientApName_Object = MibTableColumn
cLQVMediaMCClientApName = _CLQVMediaMCClientApName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 11, 3, 1, 4),
    _CLQVMediaMCClientApName_Type()
)
cLQVMediaMCClientApName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQVMediaMCClientApName.setStatus("current")
_CLQVMediaClientMCUCStatus_Type = SnmpAdminString
_CLQVMediaClientMCUCStatus_Object = MibTableColumn
cLQVMediaClientMCUCStatus = _CLQVMediaClientMCUCStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 11, 3, 1, 5),
    _CLQVMediaClientMCUCStatus_Type()
)
cLQVMediaClientMCUCStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQVMediaClientMCUCStatus.setStatus("current")
_CLQMediaStreamConfig_ObjectIdentity = ObjectIdentity
cLQMediaStreamConfig = _CLQMediaStreamConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 12)
)
_CLQMStreamTable_Object = MibTable
cLQMStreamTable = _CLQMStreamTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 12, 1)
)
if mibBuilder.loadTexts:
    cLQMStreamTable.setStatus("current")
_CLQMStreamEntry_Object = MibTableRow
cLQMStreamEntry = _CLQMStreamEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 12, 1, 1)
)
cLQMStreamEntry.setIndexNames(
    (0, "CISCO-LWAPP-QOS-MIB", "cLQMStreamName"),
)
if mibBuilder.loadTexts:
    cLQMStreamEntry.setStatus("current")
_CLQMStreamName_Type = SnmpAdminString
_CLQMStreamName_Object = MibTableColumn
cLQMStreamName = _CLQMStreamName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 12, 1, 1, 1),
    _CLQMStreamName_Type()
)
cLQMStreamName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLQMStreamName.setStatus("current")
_CLQMStreamRowStatus_Type = RowStatus
_CLQMStreamRowStatus_Object = MibTableColumn
cLQMStreamRowStatus = _CLQMStreamRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 12, 1, 1, 2),
    _CLQMStreamRowStatus_Type()
)
cLQMStreamRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLQMStreamRowStatus.setStatus("current")
_CLQMStreamDestIPStartAddr_Type = IpAddress
_CLQMStreamDestIPStartAddr_Object = MibTableColumn
cLQMStreamDestIPStartAddr = _CLQMStreamDestIPStartAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 12, 1, 1, 3),
    _CLQMStreamDestIPStartAddr_Type()
)
cLQMStreamDestIPStartAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLQMStreamDestIPStartAddr.setStatus("deprecated")
_CLQMStreamDestIPEndAddr_Type = IpAddress
_CLQMStreamDestIPEndAddr_Object = MibTableColumn
cLQMStreamDestIPEndAddr = _CLQMStreamDestIPEndAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 12, 1, 1, 4),
    _CLQMStreamDestIPEndAddr_Type()
)
cLQMStreamDestIPEndAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLQMStreamDestIPEndAddr.setStatus("deprecated")


class _CLQMStreamstate_Type(TruthValue):
    """Custom type cLQMStreamstate based on TruthValue"""
    defaultValue = 2


_CLQMStreamstate_Type.__name__ = "TruthValue"
_CLQMStreamstate_Object = MibTableColumn
cLQMStreamstate = _CLQMStreamstate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 12, 1, 1, 5),
    _CLQMStreamstate_Type()
)
cLQMStreamstate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLQMStreamstate.setStatus("current")


class _CLQMStreamRrcExpBw_Type(Unsigned32):
    """Custom type cLQMStreamRrcExpBw based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 35000),
    )


_CLQMStreamRrcExpBw_Type.__name__ = "Unsigned32"
_CLQMStreamRrcExpBw_Object = MibTableColumn
cLQMStreamRrcExpBw = _CLQMStreamRrcExpBw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 12, 1, 1, 6),
    _CLQMStreamRrcExpBw_Type()
)
cLQMStreamRrcExpBw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLQMStreamRrcExpBw.setStatus("current")


class _CLQMStreamRrcAvgPkt_Type(Unsigned32):
    """Custom type cLQMStreamRrcAvgPkt based on Unsigned32"""
    defaultValue = 1200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1500),
    )


_CLQMStreamRrcAvgPkt_Type.__name__ = "Unsigned32"
_CLQMStreamRrcAvgPkt_Object = MibTableColumn
cLQMStreamRrcAvgPkt = _CLQMStreamRrcAvgPkt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 12, 1, 1, 7),
    _CLQMStreamRrcAvgPkt_Type()
)
cLQMStreamRrcAvgPkt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLQMStreamRrcAvgPkt.setStatus("current")


class _CLQMStreamReRrc_Type(TruthValue):
    """Custom type cLQMStreamReRrc based on TruthValue"""
    defaultValue = 1


_CLQMStreamReRrc_Type.__name__ = "TruthValue"
_CLQMStreamReRrc_Object = MibTableColumn
cLQMStreamReRrc = _CLQMStreamReRrc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 12, 1, 1, 8),
    _CLQMStreamReRrc_Type()
)
cLQMStreamReRrc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLQMStreamReRrc.setStatus("current")


class _CLQMStreamRrcQos_Type(Integer32):
    """Custom type cLQMStreamRrcQos based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("besteffort", 1),
          ("background", 2),
          ("undefined", 3),
          ("excellenteffort", 4),
          ("ctrlload", 5),
          ("video", 6),
          ("voice", 7),
          ("network", 8))
    )


_CLQMStreamRrcQos_Type.__name__ = "Integer32"
_CLQMStreamRrcQos_Object = MibTableColumn
cLQMStreamRrcQos = _CLQMStreamRrcQos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 12, 1, 1, 9),
    _CLQMStreamRrcQos_Type()
)
cLQMStreamRrcQos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLQMStreamRrcQos.setStatus("current")


class _CLQMStreamRrcType_Type(Integer32):
    """Custom type cLQMStreamRrcType based on Integer32"""
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
        *(("mc2uc", 1),
          ("m-only", 2),
          ("unicast", 3),
          ("disabled", 4))
    )


_CLQMStreamRrcType_Type.__name__ = "Integer32"
_CLQMStreamRrcType_Object = MibTableColumn
cLQMStreamRrcType = _CLQMStreamRrcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 12, 1, 1, 10),
    _CLQMStreamRrcType_Type()
)
cLQMStreamRrcType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLQMStreamRrcType.setStatus("current")


class _CLQMStreamRrcPriority_Type(Integer32):
    """Custom type cLQMStreamRrcPriority based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CLQMStreamRrcPriority_Type.__name__ = "Integer32"
_CLQMStreamRrcPriority_Object = MibTableColumn
cLQMStreamRrcPriority = _CLQMStreamRrcPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 12, 1, 1, 11),
    _CLQMStreamRrcPriority_Type()
)
cLQMStreamRrcPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLQMStreamRrcPriority.setStatus("current")


class _CLQMStreamRrcViolation_Type(Integer32):
    """Custom type cLQMStreamRrcViolation based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fallback", 1),
          ("drop", 2))
    )


_CLQMStreamRrcViolation_Type.__name__ = "Integer32"
_CLQMStreamRrcViolation_Object = MibTableColumn
cLQMStreamRrcViolation = _CLQMStreamRrcViolation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 12, 1, 1, 12),
    _CLQMStreamRrcViolation_Type()
)
cLQMStreamRrcViolation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLQMStreamRrcViolation.setStatus("current")


class _CLQMStreamRrcPolicy_Type(TruthValue):
    """Custom type cLQMStreamRrcPolicy based on TruthValue"""
    defaultValue = 2


_CLQMStreamRrcPolicy_Type.__name__ = "TruthValue"
_CLQMStreamRrcPolicy_Object = MibTableColumn
cLQMStreamRrcPolicy = _CLQMStreamRrcPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 12, 1, 1, 13),
    _CLQMStreamRrcPolicy_Type()
)
cLQMStreamRrcPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLQMStreamRrcPolicy.setStatus("current")
_CLQMStreamDestStartInetAddrType_Type = InetAddressType
_CLQMStreamDestStartInetAddrType_Object = MibTableColumn
cLQMStreamDestStartInetAddrType = _CLQMStreamDestStartInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 12, 1, 1, 14),
    _CLQMStreamDestStartInetAddrType_Type()
)
cLQMStreamDestStartInetAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLQMStreamDestStartInetAddrType.setStatus("current")
_CLQMStreamDestStartInetAddr_Type = InetAddress
_CLQMStreamDestStartInetAddr_Object = MibTableColumn
cLQMStreamDestStartInetAddr = _CLQMStreamDestStartInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 12, 1, 1, 15),
    _CLQMStreamDestStartInetAddr_Type()
)
cLQMStreamDestStartInetAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLQMStreamDestStartInetAddr.setStatus("current")
_CLQMStreamDestEndInetAddrType_Type = InetAddressType
_CLQMStreamDestEndInetAddrType_Object = MibTableColumn
cLQMStreamDestEndInetAddrType = _CLQMStreamDestEndInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 12, 1, 1, 16),
    _CLQMStreamDestEndInetAddrType_Type()
)
cLQMStreamDestEndInetAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLQMStreamDestEndInetAddrType.setStatus("current")
_CLQMStreamDestEndInetAddr_Type = InetAddress
_CLQMStreamDestEndInetAddr_Object = MibTableColumn
cLQMStreamDestEndInetAddr = _CLQMStreamDestEndInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 12, 1, 1, 17),
    _CLQMStreamDestEndInetAddr_Type()
)
cLQMStreamDestEndInetAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLQMStreamDestEndInetAddr.setStatus("current")
_CLQMStreamSdpConfig_ObjectIdentity = ObjectIdentity
cLQMStreamSdpConfig = _CLQMStreamSdpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 12, 2)
)


class _CLQMStreamSdpUrl_Type(OctetString):
    """Custom type cLQMStreamSdpUrl based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CLQMStreamSdpUrl_Type.__name__ = "OctetString"
_CLQMStreamSdpUrl_Object = MibScalar
cLQMStreamSdpUrl = _CLQMStreamSdpUrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 12, 2, 1),
    _CLQMStreamSdpUrl_Type()
)
cLQMStreamSdpUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQMStreamSdpUrl.setStatus("current")


class _CLQMStreamSdpEmail_Type(OctetString):
    """Custom type cLQMStreamSdpEmail based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CLQMStreamSdpEmail_Type.__name__ = "OctetString"
_CLQMStreamSdpEmail_Object = MibScalar
cLQMStreamSdpEmail = _CLQMStreamSdpEmail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 12, 2, 2),
    _CLQMStreamSdpEmail_Type()
)
cLQMStreamSdpEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQMStreamSdpEmail.setStatus("current")


class _CLQMStreamSdpPhone_Type(OctetString):
    """Custom type cLQMStreamSdpPhone based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_CLQMStreamSdpPhone_Type.__name__ = "OctetString"
_CLQMStreamSdpPhone_Object = MibScalar
cLQMStreamSdpPhone = _CLQMStreamSdpPhone_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 12, 2, 3),
    _CLQMStreamSdpPhone_Type()
)
cLQMStreamSdpPhone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQMStreamSdpPhone.setStatus("current")


class _CLQMStreamSdpNote_Type(OctetString):
    """Custom type cLQMStreamSdpNote based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CLQMStreamSdpNote_Type.__name__ = "OctetString"
_CLQMStreamSdpNote_Object = MibScalar
cLQMStreamSdpNote = _CLQMStreamSdpNote_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 12, 2, 4),
    _CLQMStreamSdpNote_Type()
)
cLQMStreamSdpNote.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQMStreamSdpNote.setStatus("current")
_CLQMStreamSdpStatus_Type = TruthValue
_CLQMStreamSdpStatus_Object = MibScalar
cLQMStreamSdpStatus = _CLQMStreamSdpStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 12, 2, 5),
    _CLQMStreamSdpStatus_Type()
)
cLQMStreamSdpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQMStreamSdpStatus.setStatus("current")
_CLQMStreamRrcGlobal_ObjectIdentity = ObjectIdentity
cLQMStreamRrcGlobal = _CLQMStreamRrcGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 12, 3)
)


class _CLQMStreamRrcGlobalState_Type(TruthValue):
    """Custom type cLQMStreamRrcGlobalState based on TruthValue"""
    defaultValue = 2


_CLQMStreamRrcGlobalState_Type.__name__ = "TruthValue"
_CLQMStreamRrcGlobalState_Object = MibScalar
cLQMStreamRrcGlobalState = _CLQMStreamRrcGlobalState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 12, 3, 1),
    _CLQMStreamRrcGlobalState_Type()
)
cLQMStreamRrcGlobalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQMStreamRrcGlobalState.setStatus("current")
_CLQPreferredCallConfig_ObjectIdentity = ObjectIdentity
cLQPreferredCallConfig = _CLQPreferredCallConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 13)
)
_CLQPreferredCallTable_Object = MibTable
cLQPreferredCallTable = _CLQPreferredCallTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 13, 1)
)
if mibBuilder.loadTexts:
    cLQPreferredCallTable.setStatus("current")
_CLQPreferredCallEntry_Object = MibTableRow
cLQPreferredCallEntry = _CLQPreferredCallEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 13, 1, 1)
)
cLQPreferredCallEntry.setIndexNames(
    (0, "CISCO-LWAPP-QOS-MIB", "cLQPreferredCallIndex"),
)
if mibBuilder.loadTexts:
    cLQPreferredCallEntry.setStatus("current")


class _CLQPreferredCallIndex_Type(Unsigned32):
    """Custom type cLQPreferredCallIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_CLQPreferredCallIndex_Type.__name__ = "Unsigned32"
_CLQPreferredCallIndex_Object = MibTableColumn
cLQPreferredCallIndex = _CLQPreferredCallIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 13, 1, 1, 1),
    _CLQPreferredCallIndex_Type()
)
cLQPreferredCallIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLQPreferredCallIndex.setStatus("current")


class _CLQPreferredCallNumber_Type(SnmpAdminString):
    """Custom type cLQPreferredCallNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLQPreferredCallNumber_Type.__name__ = "SnmpAdminString"
_CLQPreferredCallNumber_Object = MibTableColumn
cLQPreferredCallNumber = _CLQPreferredCallNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 13, 1, 1, 2),
    _CLQPreferredCallNumber_Type()
)
cLQPreferredCallNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLQPreferredCallNumber.setStatus("current")
_CLQPreferredCallRowStatus_Type = RowStatus
_CLQPreferredCallRowStatus_Object = MibTableColumn
cLQPreferredCallRowStatus = _CLQPreferredCallRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 13, 1, 1, 3),
    _CLQPreferredCallRowStatus_Type()
)
cLQPreferredCallRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLQPreferredCallRowStatus.setStatus("current")
_CLQoSProfileConfig_ObjectIdentity = ObjectIdentity
cLQoSProfileConfig = _CLQoSProfileConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 14)
)
_CLQoSProfileTable_Object = MibTable
cLQoSProfileTable = _CLQoSProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 14, 1)
)
if mibBuilder.loadTexts:
    cLQoSProfileTable.setStatus("current")
_CLQoSProfileEntry_Object = MibTableRow
cLQoSProfileEntry = _CLQoSProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 14, 1, 1)
)
cLQoSProfileEntry.setIndexNames(
    (0, "CISCO-LWAPP-QOS-MIB", "cLQoSProfileName"),
)
if mibBuilder.loadTexts:
    cLQoSProfileEntry.setStatus("current")
_CLQoSProfileName_Type = SnmpAdminString
_CLQoSProfileName_Object = MibTableColumn
cLQoSProfileName = _CLQoSProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 14, 1, 1, 1),
    _CLQoSProfileName_Type()
)
cLQoSProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLQoSProfileName.setStatus("current")


class _CLQoSMaximumPriority_Type(Integer32):
    """Custom type cLQoSMaximumPriority based on Integer32"""
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
        *(("besteffort", 1),
          ("background", 2),
          ("video", 3),
          ("voice", 4))
    )


_CLQoSMaximumPriority_Type.__name__ = "Integer32"
_CLQoSMaximumPriority_Object = MibTableColumn
cLQoSMaximumPriority = _CLQoSMaximumPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 14, 1, 1, 2),
    _CLQoSMaximumPriority_Type()
)
cLQoSMaximumPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQoSMaximumPriority.setStatus("current")


class _CLQoSUnicastDefPriority_Type(Integer32):
    """Custom type cLQoSUnicastDefPriority based on Integer32"""
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
        *(("besteffort", 1),
          ("background", 2),
          ("video", 3),
          ("voice", 4))
    )


_CLQoSUnicastDefPriority_Type.__name__ = "Integer32"
_CLQoSUnicastDefPriority_Object = MibTableColumn
cLQoSUnicastDefPriority = _CLQoSUnicastDefPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 14, 1, 1, 3),
    _CLQoSUnicastDefPriority_Type()
)
cLQoSUnicastDefPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQoSUnicastDefPriority.setStatus("current")


class _CLQoSMulticastDefPriority_Type(Integer32):
    """Custom type cLQoSMulticastDefPriority based on Integer32"""
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
        *(("besteffort", 1),
          ("background", 2),
          ("video", 3),
          ("voice", 4))
    )


_CLQoSMulticastDefPriority_Type.__name__ = "Integer32"
_CLQoSMulticastDefPriority_Object = MibTableColumn
cLQoSMulticastDefPriority = _CLQoSMulticastDefPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 14, 1, 1, 4),
    _CLQoSMulticastDefPriority_Type()
)
cLQoSMulticastDefPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQoSMulticastDefPriority.setStatus("current")
_CLQoSClientDSAverageDataRate_Type = Unsigned32
_CLQoSClientDSAverageDataRate_Object = MibTableColumn
cLQoSClientDSAverageDataRate = _CLQoSClientDSAverageDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 14, 1, 1, 5),
    _CLQoSClientDSAverageDataRate_Type()
)
cLQoSClientDSAverageDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQoSClientDSAverageDataRate.setStatus("current")
_CLQoSClientUSAverageDataRate_Type = Unsigned32
_CLQoSClientUSAverageDataRate_Object = MibTableColumn
cLQoSClientUSAverageDataRate = _CLQoSClientUSAverageDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 14, 1, 1, 6),
    _CLQoSClientUSAverageDataRate_Type()
)
cLQoSClientUSAverageDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQoSClientUSAverageDataRate.setStatus("current")
_CLQoSClientDSBurstDataRate_Type = Unsigned32
_CLQoSClientDSBurstDataRate_Object = MibTableColumn
cLQoSClientDSBurstDataRate = _CLQoSClientDSBurstDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 14, 1, 1, 7),
    _CLQoSClientDSBurstDataRate_Type()
)
cLQoSClientDSBurstDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQoSClientDSBurstDataRate.setStatus("current")
_CLQoSClientUSBurstDataRate_Type = Unsigned32
_CLQoSClientUSBurstDataRate_Object = MibTableColumn
cLQoSClientUSBurstDataRate = _CLQoSClientUSBurstDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 14, 1, 1, 8),
    _CLQoSClientUSBurstDataRate_Type()
)
cLQoSClientUSBurstDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQoSClientUSBurstDataRate.setStatus("current")
_CLQoSClientDSAvgRealTimeDataRate_Type = Unsigned32
_CLQoSClientDSAvgRealTimeDataRate_Object = MibTableColumn
cLQoSClientDSAvgRealTimeDataRate = _CLQoSClientDSAvgRealTimeDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 14, 1, 1, 9),
    _CLQoSClientDSAvgRealTimeDataRate_Type()
)
cLQoSClientDSAvgRealTimeDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQoSClientDSAvgRealTimeDataRate.setStatus("current")
_CLQoSClientUSAvgRealTimeDataRate_Type = Unsigned32
_CLQoSClientUSAvgRealTimeDataRate_Object = MibTableColumn
cLQoSClientUSAvgRealTimeDataRate = _CLQoSClientUSAvgRealTimeDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 14, 1, 1, 10),
    _CLQoSClientUSAvgRealTimeDataRate_Type()
)
cLQoSClientUSAvgRealTimeDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQoSClientUSAvgRealTimeDataRate.setStatus("current")
_CLQoSClientDSBurstRealTimeDataRate_Type = Unsigned32
_CLQoSClientDSBurstRealTimeDataRate_Object = MibTableColumn
cLQoSClientDSBurstRealTimeDataRate = _CLQoSClientDSBurstRealTimeDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 14, 1, 1, 11),
    _CLQoSClientDSBurstRealTimeDataRate_Type()
)
cLQoSClientDSBurstRealTimeDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQoSClientDSBurstRealTimeDataRate.setStatus("current")
_CLQoSClientUSBurstRealTimeDataRate_Type = Unsigned32
_CLQoSClientUSBurstRealTimeDataRate_Object = MibTableColumn
cLQoSClientUSBurstRealTimeDataRate = _CLQoSClientUSBurstRealTimeDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 14, 1, 1, 12),
    _CLQoSClientUSBurstRealTimeDataRate_Type()
)
cLQoSClientUSBurstRealTimeDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQoSClientUSBurstRealTimeDataRate.setStatus("current")
_CLQoSSsidDSAverageDataRate_Type = Unsigned32
_CLQoSSsidDSAverageDataRate_Object = MibTableColumn
cLQoSSsidDSAverageDataRate = _CLQoSSsidDSAverageDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 14, 1, 1, 13),
    _CLQoSSsidDSAverageDataRate_Type()
)
cLQoSSsidDSAverageDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQoSSsidDSAverageDataRate.setStatus("current")
_CLQoSSsidUSAverageDataRate_Type = Unsigned32
_CLQoSSsidUSAverageDataRate_Object = MibTableColumn
cLQoSSsidUSAverageDataRate = _CLQoSSsidUSAverageDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 14, 1, 1, 14),
    _CLQoSSsidUSAverageDataRate_Type()
)
cLQoSSsidUSAverageDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQoSSsidUSAverageDataRate.setStatus("current")
_CLQoSSsidDSBurstDataRate_Type = Unsigned32
_CLQoSSsidDSBurstDataRate_Object = MibTableColumn
cLQoSSsidDSBurstDataRate = _CLQoSSsidDSBurstDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 14, 1, 1, 15),
    _CLQoSSsidDSBurstDataRate_Type()
)
cLQoSSsidDSBurstDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQoSSsidDSBurstDataRate.setStatus("current")
_CLQoSSsidUSBurstDataRate_Type = Unsigned32
_CLQoSSsidUSBurstDataRate_Object = MibTableColumn
cLQoSSsidUSBurstDataRate = _CLQoSSsidUSBurstDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 14, 1, 1, 16),
    _CLQoSSsidUSBurstDataRate_Type()
)
cLQoSSsidUSBurstDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQoSSsidUSBurstDataRate.setStatus("current")
_CLQoSSsidDSAvgRealTimeDataRate_Type = Unsigned32
_CLQoSSsidDSAvgRealTimeDataRate_Object = MibTableColumn
cLQoSSsidDSAvgRealTimeDataRate = _CLQoSSsidDSAvgRealTimeDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 14, 1, 1, 17),
    _CLQoSSsidDSAvgRealTimeDataRate_Type()
)
cLQoSSsidDSAvgRealTimeDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQoSSsidDSAvgRealTimeDataRate.setStatus("current")
_CLQoSSsidUSAvgRealTimeDataRate_Type = Unsigned32
_CLQoSSsidUSAvgRealTimeDataRate_Object = MibTableColumn
cLQoSSsidUSAvgRealTimeDataRate = _CLQoSSsidUSAvgRealTimeDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 14, 1, 1, 18),
    _CLQoSSsidUSAvgRealTimeDataRate_Type()
)
cLQoSSsidUSAvgRealTimeDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQoSSsidUSAvgRealTimeDataRate.setStatus("current")
_CLQoSSsidDSBurstRealTimeDataRate_Type = Unsigned32
_CLQoSSsidDSBurstRealTimeDataRate_Object = MibTableColumn
cLQoSSsidDSBurstRealTimeDataRate = _CLQoSSsidDSBurstRealTimeDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 14, 1, 1, 19),
    _CLQoSSsidDSBurstRealTimeDataRate_Type()
)
cLQoSSsidDSBurstRealTimeDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQoSSsidDSBurstRealTimeDataRate.setStatus("current")
_CLQoSSsidUSBurstRealTimeDataRate_Type = Unsigned32
_CLQoSSsidUSBurstRealTimeDataRate_Object = MibTableColumn
cLQoSSsidUSBurstRealTimeDataRate = _CLQoSSsidUSBurstRealTimeDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 14, 1, 1, 20),
    _CLQoSSsidUSBurstRealTimeDataRate_Type()
)
cLQoSSsidUSBurstRealTimeDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQoSSsidUSBurstRealTimeDataRate.setStatus("current")
_CLQoSWlanDSAverageDataRate_Type = Unsigned32
_CLQoSWlanDSAverageDataRate_Object = MibTableColumn
cLQoSWlanDSAverageDataRate = _CLQoSWlanDSAverageDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 14, 1, 1, 21),
    _CLQoSWlanDSAverageDataRate_Type()
)
cLQoSWlanDSAverageDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQoSWlanDSAverageDataRate.setStatus("current")
if mibBuilder.loadTexts:
    cLQoSWlanDSAverageDataRate.setUnits("kbytes")
_CLQoSWlanUSAverageDataRate_Type = Unsigned32
_CLQoSWlanUSAverageDataRate_Object = MibTableColumn
cLQoSWlanUSAverageDataRate = _CLQoSWlanUSAverageDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 14, 1, 1, 22),
    _CLQoSWlanUSAverageDataRate_Type()
)
cLQoSWlanUSAverageDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQoSWlanUSAverageDataRate.setStatus("current")
if mibBuilder.loadTexts:
    cLQoSWlanUSAverageDataRate.setUnits("kbytes")
_CLQoSWlanDSBurstDataRate_Type = Unsigned32
_CLQoSWlanDSBurstDataRate_Object = MibTableColumn
cLQoSWlanDSBurstDataRate = _CLQoSWlanDSBurstDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 14, 1, 1, 23),
    _CLQoSWlanDSBurstDataRate_Type()
)
cLQoSWlanDSBurstDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQoSWlanDSBurstDataRate.setStatus("current")
if mibBuilder.loadTexts:
    cLQoSWlanDSBurstDataRate.setUnits("kbytes")
_CLQoSWlanUSBurstDataRate_Type = Unsigned32
_CLQoSWlanUSBurstDataRate_Object = MibTableColumn
cLQoSWlanUSBurstDataRate = _CLQoSWlanUSBurstDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 14, 1, 1, 24),
    _CLQoSWlanUSBurstDataRate_Type()
)
cLQoSWlanUSBurstDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQoSWlanUSBurstDataRate.setStatus("current")
if mibBuilder.loadTexts:
    cLQoSWlanUSBurstDataRate.setUnits("kbytes")
_CLQoSWlanDSAvgRealTimeDataRate_Type = Unsigned32
_CLQoSWlanDSAvgRealTimeDataRate_Object = MibTableColumn
cLQoSWlanDSAvgRealTimeDataRate = _CLQoSWlanDSAvgRealTimeDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 14, 1, 1, 25),
    _CLQoSWlanDSAvgRealTimeDataRate_Type()
)
cLQoSWlanDSAvgRealTimeDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQoSWlanDSAvgRealTimeDataRate.setStatus("current")
if mibBuilder.loadTexts:
    cLQoSWlanDSAvgRealTimeDataRate.setUnits("kbytes")
_CLQoSWlanUSAvgRealTimeDataRate_Type = Unsigned32
_CLQoSWlanUSAvgRealTimeDataRate_Object = MibTableColumn
cLQoSWlanUSAvgRealTimeDataRate = _CLQoSWlanUSAvgRealTimeDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 14, 1, 1, 26),
    _CLQoSWlanUSAvgRealTimeDataRate_Type()
)
cLQoSWlanUSAvgRealTimeDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQoSWlanUSAvgRealTimeDataRate.setStatus("current")
if mibBuilder.loadTexts:
    cLQoSWlanUSAvgRealTimeDataRate.setUnits("kbytes")
_CLQoSWlanDSBurstRealTimeDataRate_Type = Unsigned32
_CLQoSWlanDSBurstRealTimeDataRate_Object = MibTableColumn
cLQoSWlanDSBurstRealTimeDataRate = _CLQoSWlanDSBurstRealTimeDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 14, 1, 1, 27),
    _CLQoSWlanDSBurstRealTimeDataRate_Type()
)
cLQoSWlanDSBurstRealTimeDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQoSWlanDSBurstRealTimeDataRate.setStatus("current")
if mibBuilder.loadTexts:
    cLQoSWlanDSBurstRealTimeDataRate.setUnits("kbytes")
_CLQoSWlanUSBurstRealTimeDataRate_Type = Unsigned32
_CLQoSWlanUSBurstRealTimeDataRate_Object = MibTableColumn
cLQoSWlanUSBurstRealTimeDataRate = _CLQoSWlanUSBurstRealTimeDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 14, 1, 1, 28),
    _CLQoSWlanUSBurstRealTimeDataRate_Type()
)
cLQoSWlanUSBurstRealTimeDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQoSWlanUSBurstRealTimeDataRate.setStatus("current")
if mibBuilder.loadTexts:
    cLQoSWlanUSBurstRealTimeDataRate.setUnits("kbytes")
_CLQoSSipSnoopingConfig_ObjectIdentity = ObjectIdentity
cLQoSSipSnoopingConfig = _CLQoSSipSnoopingConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 15)
)
_CLQoSSipSnoopingPortRangeStart_Type = InetPortNumber
_CLQoSSipSnoopingPortRangeStart_Object = MibScalar
cLQoSSipSnoopingPortRangeStart = _CLQoSSipSnoopingPortRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 15, 1),
    _CLQoSSipSnoopingPortRangeStart_Type()
)
cLQoSSipSnoopingPortRangeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQoSSipSnoopingPortRangeStart.setStatus("current")
_CLQoSSipSnoopingPortRangeEnd_Type = InetPortNumber
_CLQoSSipSnoopingPortRangeEnd_Object = MibScalar
cLQoSSipSnoopingPortRangeEnd = _CLQoSSipSnoopingPortRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 15, 2),
    _CLQoSSipSnoopingPortRangeEnd_Type()
)
cLQoSSipSnoopingPortRangeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQoSSipSnoopingPortRangeEnd.setStatus("current")
_CLQoSAirTimeFairness_ObjectIdentity = ObjectIdentity
cLQoSAirTimeFairness = _CLQoSAirTimeFairness_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 16)
)
_CLQoSGlobalAirTimeFairnessTable_Object = MibTable
cLQoSGlobalAirTimeFairnessTable = _CLQoSGlobalAirTimeFairnessTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 16, 1)
)
if mibBuilder.loadTexts:
    cLQoSGlobalAirTimeFairnessTable.setStatus("current")
_CLQoSGlobalAirTimeFairnessEntry_Object = MibTableRow
cLQoSGlobalAirTimeFairnessEntry = _CLQoSGlobalAirTimeFairnessEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 16, 1, 1)
)
cLQoSGlobalAirTimeFairnessEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApDot11IfType"),
)
if mibBuilder.loadTexts:
    cLQoSGlobalAirTimeFairnessEntry.setStatus("current")


class _CLGlobalAirTimeFairnessMode_Type(Integer32):
    """Custom type cLGlobalAirTimeFairnessMode based on Integer32"""
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
          ("ssid", 2),
          ("monitor", 3))
    )


_CLGlobalAirTimeFairnessMode_Type.__name__ = "Integer32"
_CLGlobalAirTimeFairnessMode_Object = MibTableColumn
cLGlobalAirTimeFairnessMode = _CLGlobalAirTimeFairnessMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 16, 1, 1, 1),
    _CLGlobalAirTimeFairnessMode_Type()
)
cLGlobalAirTimeFairnessMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLGlobalAirTimeFairnessMode.setStatus("current")
_CLGlobalAirTimeFairnessOptimizationPolicy_Type = TruthValue
_CLGlobalAirTimeFairnessOptimizationPolicy_Object = MibTableColumn
cLGlobalAirTimeFairnessOptimizationPolicy = _CLGlobalAirTimeFairnessOptimizationPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 16, 1, 1, 2),
    _CLGlobalAirTimeFairnessOptimizationPolicy_Type()
)
cLGlobalAirTimeFairnessOptimizationPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLGlobalAirTimeFairnessOptimizationPolicy.setStatus("current")
_CLQoSAirTimeFairnessTable_Object = MibTable
cLQoSAirTimeFairnessTable = _CLQoSAirTimeFairnessTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 16, 2)
)
if mibBuilder.loadTexts:
    cLQoSAirTimeFairnessTable.setStatus("current")
_CLQoSAirTimeFairnessEntry_Object = MibTableRow
cLQoSAirTimeFairnessEntry = _CLQoSAirTimeFairnessEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 16, 2, 1)
)
cLQoSAirTimeFairnessEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"),
)
if mibBuilder.loadTexts:
    cLQoSAirTimeFairnessEntry.setStatus("current")


class _CLApAirTimeFairnessMode_Type(Integer32):
    """Custom type cLApAirTimeFairnessMode based on Integer32"""
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
          ("ssid", 2),
          ("monitor", 3))
    )


_CLApAirTimeFairnessMode_Type.__name__ = "Integer32"
_CLApAirTimeFairnessMode_Object = MibTableColumn
cLApAirTimeFairnessMode = _CLApAirTimeFairnessMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 16, 2, 1, 1),
    _CLApAirTimeFairnessMode_Type()
)
cLApAirTimeFairnessMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApAirTimeFairnessMode.setStatus("current")
_CLApAirTimeFairnessOptimizationPolicy_Type = TruthValue
_CLApAirTimeFairnessOptimizationPolicy_Object = MibTableColumn
cLApAirTimeFairnessOptimizationPolicy = _CLApAirTimeFairnessOptimizationPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 16, 2, 1, 2),
    _CLApAirTimeFairnessOptimizationPolicy_Type()
)
cLApAirTimeFairnessOptimizationPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApAirTimeFairnessOptimizationPolicy.setStatus("current")
_CLQoSAirTimeFairnessWlanStatisticsTable_Object = MibTable
cLQoSAirTimeFairnessWlanStatisticsTable = _CLQoSAirTimeFairnessWlanStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 16, 3)
)
if mibBuilder.loadTexts:
    cLQoSAirTimeFairnessWlanStatisticsTable.setStatus("current")
_CLQoSAirTimeFairnessWlanStatisticsEntry_Object = MibTableRow
cLQoSAirTimeFairnessWlanStatisticsEntry = _CLQoSAirTimeFairnessWlanStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 16, 3, 1)
)
cLQoSAirTimeFairnessWlanStatisticsEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"),
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanProfileName"),
)
if mibBuilder.loadTexts:
    cLQoSAirTimeFairnessWlanStatisticsEntry.setStatus("current")


class _CLApAirTimeFairnessWlanAirtimeUsedInstantaneous_Type(TimeInterval):
    """Custom type cLApAirTimeFairnessWlanAirtimeUsedInstantaneous based on TimeInterval"""
    defaultValue = 0


_CLApAirTimeFairnessWlanAirtimeUsedInstantaneous_Type.__name__ = "TimeInterval"
_CLApAirTimeFairnessWlanAirtimeUsedInstantaneous_Object = MibTableColumn
cLApAirTimeFairnessWlanAirtimeUsedInstantaneous = _CLApAirTimeFairnessWlanAirtimeUsedInstantaneous_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 16, 3, 1, 1),
    _CLApAirTimeFairnessWlanAirtimeUsedInstantaneous_Type()
)
cLApAirTimeFairnessWlanAirtimeUsedInstantaneous.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApAirTimeFairnessWlanAirtimeUsedInstantaneous.setStatus("current")
if mibBuilder.loadTexts:
    cLApAirTimeFairnessWlanAirtimeUsedInstantaneous.setUnits("Microseconds")


class _CLApAirTimeFairnessWlanAirtimeUsedCumulative_Type(Unsigned64):
    """Custom type cLApAirTimeFairnessWlanAirtimeUsedCumulative based on Unsigned64"""
    defaultValue = 0


_CLApAirTimeFairnessWlanAirtimeUsedCumulative_Type.__name__ = "Unsigned64"
_CLApAirTimeFairnessWlanAirtimeUsedCumulative_Object = MibTableColumn
cLApAirTimeFairnessWlanAirtimeUsedCumulative = _CLApAirTimeFairnessWlanAirtimeUsedCumulative_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 16, 3, 1, 2),
    _CLApAirTimeFairnessWlanAirtimeUsedCumulative_Type()
)
cLApAirTimeFairnessWlanAirtimeUsedCumulative.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApAirTimeFairnessWlanAirtimeUsedCumulative.setStatus("current")
if mibBuilder.loadTexts:
    cLApAirTimeFairnessWlanAirtimeUsedCumulative.setUnits("Microseconds")


class _CLApAirTimeFairnessWlanBytesSentInstantaneous_Type(Unsigned32):
    """Custom type cLApAirTimeFairnessWlanBytesSentInstantaneous based on Unsigned32"""
    defaultValue = 0


_CLApAirTimeFairnessWlanBytesSentInstantaneous_Type.__name__ = "Unsigned32"
_CLApAirTimeFairnessWlanBytesSentInstantaneous_Object = MibTableColumn
cLApAirTimeFairnessWlanBytesSentInstantaneous = _CLApAirTimeFairnessWlanBytesSentInstantaneous_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 16, 3, 1, 3),
    _CLApAirTimeFairnessWlanBytesSentInstantaneous_Type()
)
cLApAirTimeFairnessWlanBytesSentInstantaneous.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApAirTimeFairnessWlanBytesSentInstantaneous.setStatus("current")
if mibBuilder.loadTexts:
    cLApAirTimeFairnessWlanBytesSentInstantaneous.setUnits("bytes")


class _CLApAirTimeFairnessWlanBytesSentCumulative_Type(Unsigned64):
    """Custom type cLApAirTimeFairnessWlanBytesSentCumulative based on Unsigned64"""
    defaultValue = 0


_CLApAirTimeFairnessWlanBytesSentCumulative_Type.__name__ = "Unsigned64"
_CLApAirTimeFairnessWlanBytesSentCumulative_Object = MibTableColumn
cLApAirTimeFairnessWlanBytesSentCumulative = _CLApAirTimeFairnessWlanBytesSentCumulative_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 16, 3, 1, 4),
    _CLApAirTimeFairnessWlanBytesSentCumulative_Type()
)
cLApAirTimeFairnessWlanBytesSentCumulative.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApAirTimeFairnessWlanBytesSentCumulative.setStatus("current")
if mibBuilder.loadTexts:
    cLApAirTimeFairnessWlanBytesSentCumulative.setUnits("bytes")


class _CLApAirTimeFairnessWlanBytesDroppedInstantaneous_Type(Unsigned32):
    """Custom type cLApAirTimeFairnessWlanBytesDroppedInstantaneous based on Unsigned32"""
    defaultValue = 0


_CLApAirTimeFairnessWlanBytesDroppedInstantaneous_Type.__name__ = "Unsigned32"
_CLApAirTimeFairnessWlanBytesDroppedInstantaneous_Object = MibTableColumn
cLApAirTimeFairnessWlanBytesDroppedInstantaneous = _CLApAirTimeFairnessWlanBytesDroppedInstantaneous_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 16, 3, 1, 5),
    _CLApAirTimeFairnessWlanBytesDroppedInstantaneous_Type()
)
cLApAirTimeFairnessWlanBytesDroppedInstantaneous.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApAirTimeFairnessWlanBytesDroppedInstantaneous.setStatus("current")
if mibBuilder.loadTexts:
    cLApAirTimeFairnessWlanBytesDroppedInstantaneous.setUnits("bytes")


class _CLApAirTimeFairnessWlanBytesDroppedCumulative_Type(Unsigned64):
    """Custom type cLApAirTimeFairnessWlanBytesDroppedCumulative based on Unsigned64"""
    defaultValue = 0


_CLApAirTimeFairnessWlanBytesDroppedCumulative_Type.__name__ = "Unsigned64"
_CLApAirTimeFairnessWlanBytesDroppedCumulative_Object = MibTableColumn
cLApAirTimeFairnessWlanBytesDroppedCumulative = _CLApAirTimeFairnessWlanBytesDroppedCumulative_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 16, 3, 1, 6),
    _CLApAirTimeFairnessWlanBytesDroppedCumulative_Type()
)
cLApAirTimeFairnessWlanBytesDroppedCumulative.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApAirTimeFairnessWlanBytesDroppedCumulative.setStatus("current")
if mibBuilder.loadTexts:
    cLApAirTimeFairnessWlanBytesDroppedCumulative.setUnits("bytes")


class _CLApAirTimeFairnessWlanFramesSentInstantaneous_Type(Unsigned32):
    """Custom type cLApAirTimeFairnessWlanFramesSentInstantaneous based on Unsigned32"""
    defaultValue = 0


_CLApAirTimeFairnessWlanFramesSentInstantaneous_Type.__name__ = "Unsigned32"
_CLApAirTimeFairnessWlanFramesSentInstantaneous_Object = MibTableColumn
cLApAirTimeFairnessWlanFramesSentInstantaneous = _CLApAirTimeFairnessWlanFramesSentInstantaneous_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 16, 3, 1, 7),
    _CLApAirTimeFairnessWlanFramesSentInstantaneous_Type()
)
cLApAirTimeFairnessWlanFramesSentInstantaneous.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApAirTimeFairnessWlanFramesSentInstantaneous.setStatus("current")
if mibBuilder.loadTexts:
    cLApAirTimeFairnessWlanFramesSentInstantaneous.setUnits("pkts")


class _CLApAirTimeFairnessWlanFramesSentCumulative_Type(Unsigned64):
    """Custom type cLApAirTimeFairnessWlanFramesSentCumulative based on Unsigned64"""
    defaultValue = 0


_CLApAirTimeFairnessWlanFramesSentCumulative_Type.__name__ = "Unsigned64"
_CLApAirTimeFairnessWlanFramesSentCumulative_Object = MibTableColumn
cLApAirTimeFairnessWlanFramesSentCumulative = _CLApAirTimeFairnessWlanFramesSentCumulative_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 16, 3, 1, 8),
    _CLApAirTimeFairnessWlanFramesSentCumulative_Type()
)
cLApAirTimeFairnessWlanFramesSentCumulative.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApAirTimeFairnessWlanFramesSentCumulative.setStatus("current")
if mibBuilder.loadTexts:
    cLApAirTimeFairnessWlanFramesSentCumulative.setUnits("pkts")


class _CLApAirTimeFairnessWlanFramesDroppedInstantaneous_Type(Unsigned32):
    """Custom type cLApAirTimeFairnessWlanFramesDroppedInstantaneous based on Unsigned32"""
    defaultValue = 0


_CLApAirTimeFairnessWlanFramesDroppedInstantaneous_Type.__name__ = "Unsigned32"
_CLApAirTimeFairnessWlanFramesDroppedInstantaneous_Object = MibTableColumn
cLApAirTimeFairnessWlanFramesDroppedInstantaneous = _CLApAirTimeFairnessWlanFramesDroppedInstantaneous_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 16, 3, 1, 9),
    _CLApAirTimeFairnessWlanFramesDroppedInstantaneous_Type()
)
cLApAirTimeFairnessWlanFramesDroppedInstantaneous.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApAirTimeFairnessWlanFramesDroppedInstantaneous.setStatus("current")
if mibBuilder.loadTexts:
    cLApAirTimeFairnessWlanFramesDroppedInstantaneous.setUnits("pkts")


class _CLApAirTimeFairnessWlanFramesDroppedCumulative_Type(Unsigned64):
    """Custom type cLApAirTimeFairnessWlanFramesDroppedCumulative based on Unsigned64"""
    defaultValue = 0


_CLApAirTimeFairnessWlanFramesDroppedCumulative_Type.__name__ = "Unsigned64"
_CLApAirTimeFairnessWlanFramesDroppedCumulative_Object = MibTableColumn
cLApAirTimeFairnessWlanFramesDroppedCumulative = _CLApAirTimeFairnessWlanFramesDroppedCumulative_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 16, 3, 1, 10),
    _CLApAirTimeFairnessWlanFramesDroppedCumulative_Type()
)
cLApAirTimeFairnessWlanFramesDroppedCumulative.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApAirTimeFairnessWlanFramesDroppedCumulative.setStatus("current")
if mibBuilder.loadTexts:
    cLApAirTimeFairnessWlanFramesDroppedCumulative.setUnits("pkts")
_CLQoSAirTimeFairnessStatisticsTable_Object = MibTable
cLQoSAirTimeFairnessStatisticsTable = _CLQoSAirTimeFairnessStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 16, 4)
)
if mibBuilder.loadTexts:
    cLQoSAirTimeFairnessStatisticsTable.setStatus("current")
_CLQoSAirTimeFairnessStatisticsEntry_Object = MibTableRow
cLQoSAirTimeFairnessStatisticsEntry = _CLQoSAirTimeFairnessStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 16, 4, 1)
)
cLQoSAirTimeFairnessStatisticsEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"),
)
if mibBuilder.loadTexts:
    cLQoSAirTimeFairnessStatisticsEntry.setStatus("current")


class _CLApAirTimeFairnessTotalAirtimeUsedInstantaneous_Type(TimeInterval):
    """Custom type cLApAirTimeFairnessTotalAirtimeUsedInstantaneous based on TimeInterval"""
    defaultValue = 0


_CLApAirTimeFairnessTotalAirtimeUsedInstantaneous_Type.__name__ = "TimeInterval"
_CLApAirTimeFairnessTotalAirtimeUsedInstantaneous_Object = MibTableColumn
cLApAirTimeFairnessTotalAirtimeUsedInstantaneous = _CLApAirTimeFairnessTotalAirtimeUsedInstantaneous_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 16, 4, 1, 1),
    _CLApAirTimeFairnessTotalAirtimeUsedInstantaneous_Type()
)
cLApAirTimeFairnessTotalAirtimeUsedInstantaneous.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApAirTimeFairnessTotalAirtimeUsedInstantaneous.setStatus("current")
if mibBuilder.loadTexts:
    cLApAirTimeFairnessTotalAirtimeUsedInstantaneous.setUnits("Microseconds")


class _CLApAirTimeFairnessTotalAirtimeUsedCumulative_Type(Unsigned64):
    """Custom type cLApAirTimeFairnessTotalAirtimeUsedCumulative based on Unsigned64"""
    defaultValue = 0


_CLApAirTimeFairnessTotalAirtimeUsedCumulative_Type.__name__ = "Unsigned64"
_CLApAirTimeFairnessTotalAirtimeUsedCumulative_Object = MibTableColumn
cLApAirTimeFairnessTotalAirtimeUsedCumulative = _CLApAirTimeFairnessTotalAirtimeUsedCumulative_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 16, 4, 1, 2),
    _CLApAirTimeFairnessTotalAirtimeUsedCumulative_Type()
)
cLApAirTimeFairnessTotalAirtimeUsedCumulative.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApAirTimeFairnessTotalAirtimeUsedCumulative.setStatus("current")
if mibBuilder.loadTexts:
    cLApAirTimeFairnessTotalAirtimeUsedCumulative.setUnits("Microseconds")


class _CLApAirTimeFairnessRadioUptime_Type(TimeInterval):
    """Custom type cLApAirTimeFairnessRadioUptime based on TimeInterval"""
    defaultValue = 0


_CLApAirTimeFairnessRadioUptime_Type.__name__ = "TimeInterval"
_CLApAirTimeFairnessRadioUptime_Object = MibTableColumn
cLApAirTimeFairnessRadioUptime = _CLApAirTimeFairnessRadioUptime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 16, 4, 1, 3),
    _CLApAirTimeFairnessRadioUptime_Type()
)
cLApAirTimeFairnessRadioUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApAirTimeFairnessRadioUptime.setStatus("current")
if mibBuilder.loadTexts:
    cLApAirTimeFairnessRadioUptime.setUnits("seconds")


class _CLApAirTimeFairnessRadioUptimeCumulative_Type(TimeInterval):
    """Custom type cLApAirTimeFairnessRadioUptimeCumulative based on TimeInterval"""
    defaultValue = 0


_CLApAirTimeFairnessRadioUptimeCumulative_Type.__name__ = "TimeInterval"
_CLApAirTimeFairnessRadioUptimeCumulative_Object = MibTableColumn
cLApAirTimeFairnessRadioUptimeCumulative = _CLApAirTimeFairnessRadioUptimeCumulative_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 16, 4, 1, 4),
    _CLApAirTimeFairnessRadioUptimeCumulative_Type()
)
cLApAirTimeFairnessRadioUptimeCumulative.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApAirTimeFairnessRadioUptimeCumulative.setStatus("current")
if mibBuilder.loadTexts:
    cLApAirTimeFairnessRadioUptimeCumulative.setUnits("seconds")
_CLAPGroupAirTimeFairnessTable_Object = MibTable
cLAPGroupAirTimeFairnessTable = _CLAPGroupAirTimeFairnessTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 16, 5)
)
if mibBuilder.loadTexts:
    cLAPGroupAirTimeFairnessTable.setStatus("current")
_CLAPGroupAirTimeFairnessEntry_Object = MibTableRow
cLAPGroupAirTimeFairnessEntry = _CLAPGroupAirTimeFairnessEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 16, 5, 1)
)
cLAPGroupAirTimeFairnessEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApDot11IfType"),
    (0, "CISCO-LWAPP-WLAN-MIB", "cLAPGroupName"),
)
if mibBuilder.loadTexts:
    cLAPGroupAirTimeFairnessEntry.setStatus("current")


class _CLAPGroupAirTimeFairnessMode_Type(Integer32):
    """Custom type cLAPGroupAirTimeFairnessMode based on Integer32"""
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
          ("ssid", 2),
          ("monitor", 3))
    )


_CLAPGroupAirTimeFairnessMode_Type.__name__ = "Integer32"
_CLAPGroupAirTimeFairnessMode_Object = MibTableColumn
cLAPGroupAirTimeFairnessMode = _CLAPGroupAirTimeFairnessMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 16, 5, 1, 1),
    _CLAPGroupAirTimeFairnessMode_Type()
)
cLAPGroupAirTimeFairnessMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLAPGroupAirTimeFairnessMode.setStatus("current")
_CLAPGroupAirTimeFairnessOptimizationPolicy_Type = TruthValue
_CLAPGroupAirTimeFairnessOptimizationPolicy_Object = MibTableColumn
cLAPGroupAirTimeFairnessOptimizationPolicy = _CLAPGroupAirTimeFairnessOptimizationPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 16, 5, 1, 2),
    _CLAPGroupAirTimeFairnessOptimizationPolicy_Type()
)
cLAPGroupAirTimeFairnessOptimizationPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLAPGroupAirTimeFairnessOptimizationPolicy.setStatus("current")
_CLQosAirTimeFairnessPolicyConfigTable_Object = MibTable
cLQosAirTimeFairnessPolicyConfigTable = _CLQosAirTimeFairnessPolicyConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 16, 6)
)
if mibBuilder.loadTexts:
    cLQosAirTimeFairnessPolicyConfigTable.setStatus("current")
_CLQosAirTimeFairnessPolicyConfigEntry_Object = MibTableRow
cLQosAirTimeFairnessPolicyConfigEntry = _CLQosAirTimeFairnessPolicyConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 16, 6, 1)
)
cLQosAirTimeFairnessPolicyConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-QOS-MIB", "cLAirTimeFairnessPolicyId"),
)
if mibBuilder.loadTexts:
    cLQosAirTimeFairnessPolicyConfigEntry.setStatus("current")


class _CLAirTimeFairnessPolicyId_Type(Integer32):
    """Custom type cLAirTimeFairnessPolicyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 511),
    )


_CLAirTimeFairnessPolicyId_Type.__name__ = "Integer32"
_CLAirTimeFairnessPolicyId_Object = MibTableColumn
cLAirTimeFairnessPolicyId = _CLAirTimeFairnessPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 16, 6, 1, 1),
    _CLAirTimeFairnessPolicyId_Type()
)
cLAirTimeFairnessPolicyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLAirTimeFairnessPolicyId.setStatus("current")
_CLAirTimeFairnessPolicyRowStatus_Type = RowStatus
_CLAirTimeFairnessPolicyRowStatus_Object = MibTableColumn
cLAirTimeFairnessPolicyRowStatus = _CLAirTimeFairnessPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 16, 6, 1, 2),
    _CLAirTimeFairnessPolicyRowStatus_Type()
)
cLAirTimeFairnessPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLAirTimeFairnessPolicyRowStatus.setStatus("current")


class _CLAirTimeFairnessPolicyName_Type(SnmpAdminString):
    """Custom type cLAirTimeFairnessPolicyName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CLAirTimeFairnessPolicyName_Type.__name__ = "SnmpAdminString"
_CLAirTimeFairnessPolicyName_Object = MibTableColumn
cLAirTimeFairnessPolicyName = _CLAirTimeFairnessPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 16, 6, 1, 3),
    _CLAirTimeFairnessPolicyName_Type()
)
cLAirTimeFairnessPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLAirTimeFairnessPolicyName.setStatus("current")
_CLAirTimeFairnessPolicyWeight_Type = Unsigned32
_CLAirTimeFairnessPolicyWeight_Object = MibTableColumn
cLAirTimeFairnessPolicyWeight = _CLAirTimeFairnessPolicyWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 16, 6, 1, 4),
    _CLAirTimeFairnessPolicyWeight_Type()
)
cLAirTimeFairnessPolicyWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLAirTimeFairnessPolicyWeight.setStatus("current")


class _CLAirTimeFairnessPolicyclientfairsharing_Type(Integer32):
    """Custom type cLAirTimeFairnessPolicyclientfairsharing based on Integer32"""
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


_CLAirTimeFairnessPolicyclientfairsharing_Type.__name__ = "Integer32"
_CLAirTimeFairnessPolicyclientfairsharing_Object = MibTableColumn
cLAirTimeFairnessPolicyclientfairsharing = _CLAirTimeFairnessPolicyclientfairsharing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 16, 6, 1, 5),
    _CLAirTimeFairnessPolicyclientfairsharing_Type()
)
cLAirTimeFairnessPolicyclientfairsharing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLAirTimeFairnessPolicyclientfairsharing.setStatus("current")
_CLApAirTimeFairnessPolicyOverrideTable_Object = MibTable
cLApAirTimeFairnessPolicyOverrideTable = _CLApAirTimeFairnessPolicyOverrideTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 16, 7)
)
if mibBuilder.loadTexts:
    cLApAirTimeFairnessPolicyOverrideTable.setStatus("current")
_CLApAirTimeFairnessPolicyOverrideEntry_Object = MibTableRow
cLApAirTimeFairnessPolicyOverrideEntry = _CLApAirTimeFairnessPolicyOverrideEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 16, 7, 1)
)
cLApAirTimeFairnessPolicyOverrideEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"),
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanProfileName"),
)
if mibBuilder.loadTexts:
    cLApAirTimeFairnessPolicyOverrideEntry.setStatus("current")
_CLApAirTimeFairnessPolicyOverride_Type = TruthValue
_CLApAirTimeFairnessPolicyOverride_Object = MibTableColumn
cLApAirTimeFairnessPolicyOverride = _CLApAirTimeFairnessPolicyOverride_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 16, 7, 1, 1),
    _CLApAirTimeFairnessPolicyOverride_Type()
)
cLApAirTimeFairnessPolicyOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApAirTimeFairnessPolicyOverride.setStatus("current")


class _CLApAirTimeFairnessOverridePolicyName_Type(SnmpAdminString):
    """Custom type cLApAirTimeFairnessOverridePolicyName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CLApAirTimeFairnessOverridePolicyName_Type.__name__ = "SnmpAdminString"
_CLApAirTimeFairnessOverridePolicyName_Object = MibTableColumn
cLApAirTimeFairnessOverridePolicyName = _CLApAirTimeFairnessOverridePolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 16, 7, 1, 2),
    _CLApAirTimeFairnessOverridePolicyName_Type()
)
cLApAirTimeFairnessOverridePolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApAirTimeFairnessOverridePolicyName.setStatus("current")
_CLAPGroupsAirTimeFairnessPolicyOverrideTable_Object = MibTable
cLAPGroupsAirTimeFairnessPolicyOverrideTable = _CLAPGroupsAirTimeFairnessPolicyOverrideTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 16, 8)
)
if mibBuilder.loadTexts:
    cLAPGroupsAirTimeFairnessPolicyOverrideTable.setStatus("current")
_CLAPGroupsAirTimeFairnessPolicyOverrideEntry_Object = MibTableRow
cLAPGroupsAirTimeFairnessPolicyOverrideEntry = _CLAPGroupsAirTimeFairnessPolicyOverrideEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 16, 8, 1)
)
cLAPGroupsAirTimeFairnessPolicyOverrideEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApDot11IfType"),
    (0, "CISCO-LWAPP-WLAN-MIB", "cLAPGroupName"),
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanProfileName"),
)
if mibBuilder.loadTexts:
    cLAPGroupsAirTimeFairnessPolicyOverrideEntry.setStatus("current")


class _CLAPGroupAirTimeFairnessPolicyNameOverrideEnabled_Type(TruthValue):
    """Custom type cLAPGroupAirTimeFairnessPolicyNameOverrideEnabled based on TruthValue"""
    defaultValue = 2


_CLAPGroupAirTimeFairnessPolicyNameOverrideEnabled_Type.__name__ = "TruthValue"
_CLAPGroupAirTimeFairnessPolicyNameOverrideEnabled_Object = MibTableColumn
cLAPGroupAirTimeFairnessPolicyNameOverrideEnabled = _CLAPGroupAirTimeFairnessPolicyNameOverrideEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 16, 8, 1, 1),
    _CLAPGroupAirTimeFairnessPolicyNameOverrideEnabled_Type()
)
cLAPGroupAirTimeFairnessPolicyNameOverrideEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLAPGroupAirTimeFairnessPolicyNameOverrideEnabled.setStatus("current")


class _CLAPGroupAirTimeFairnessOverridePolicyName_Type(SnmpAdminString):
    """Custom type cLAPGroupAirTimeFairnessOverridePolicyName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CLAPGroupAirTimeFairnessOverridePolicyName_Type.__name__ = "SnmpAdminString"
_CLAPGroupAirTimeFairnessOverridePolicyName_Object = MibTableColumn
cLAPGroupAirTimeFairnessOverridePolicyName = _CLAPGroupAirTimeFairnessOverridePolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 16, 8, 1, 2),
    _CLAPGroupAirTimeFairnessOverridePolicyName_Type()
)
cLAPGroupAirTimeFairnessOverridePolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLAPGroupAirTimeFairnessOverridePolicyName.setStatus("current")
_CLQoSAirTimeFairnessClientStatisticsTable_Object = MibTable
cLQoSAirTimeFairnessClientStatisticsTable = _CLQoSAirTimeFairnessClientStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 16, 9)
)
if mibBuilder.loadTexts:
    cLQoSAirTimeFairnessClientStatisticsTable.setStatus("current")
_CLQoSAirTimeFairnessClientStatisticsEntry_Object = MibTableRow
cLQoSAirTimeFairnessClientStatisticsEntry = _CLQoSAirTimeFairnessClientStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 16, 9, 1)
)
cLQoSAirTimeFairnessClientStatisticsEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"),
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanProfileName"),
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
)
if mibBuilder.loadTexts:
    cLQoSAirTimeFairnessClientStatisticsEntry.setStatus("current")


class _CLApAirTimeFairnessClientAirtimeUsedInstantaneous_Type(TimeInterval):
    """Custom type cLApAirTimeFairnessClientAirtimeUsedInstantaneous based on TimeInterval"""
    defaultValue = 0


_CLApAirTimeFairnessClientAirtimeUsedInstantaneous_Type.__name__ = "TimeInterval"
_CLApAirTimeFairnessClientAirtimeUsedInstantaneous_Object = MibTableColumn
cLApAirTimeFairnessClientAirtimeUsedInstantaneous = _CLApAirTimeFairnessClientAirtimeUsedInstantaneous_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 16, 9, 1, 1),
    _CLApAirTimeFairnessClientAirtimeUsedInstantaneous_Type()
)
cLApAirTimeFairnessClientAirtimeUsedInstantaneous.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApAirTimeFairnessClientAirtimeUsedInstantaneous.setStatus("current")
if mibBuilder.loadTexts:
    cLApAirTimeFairnessClientAirtimeUsedInstantaneous.setUnits("Microseconds")


class _CLApAirTimeFairnessClientAirtimeUsedCumulative_Type(Unsigned32):
    """Custom type cLApAirTimeFairnessClientAirtimeUsedCumulative based on Unsigned32"""
    defaultValue = 0


_CLApAirTimeFairnessClientAirtimeUsedCumulative_Type.__name__ = "Unsigned32"
_CLApAirTimeFairnessClientAirtimeUsedCumulative_Object = MibTableColumn
cLApAirTimeFairnessClientAirtimeUsedCumulative = _CLApAirTimeFairnessClientAirtimeUsedCumulative_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 16, 9, 1, 2),
    _CLApAirTimeFairnessClientAirtimeUsedCumulative_Type()
)
cLApAirTimeFairnessClientAirtimeUsedCumulative.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApAirTimeFairnessClientAirtimeUsedCumulative.setStatus("current")
if mibBuilder.loadTexts:
    cLApAirTimeFairnessClientAirtimeUsedCumulative.setUnits("Microseconds")


class _CLApAirTimeFairnessClientFramesSent_Type(Unsigned32):
    """Custom type cLApAirTimeFairnessClientFramesSent based on Unsigned32"""
    defaultValue = 0


_CLApAirTimeFairnessClientFramesSent_Type.__name__ = "Unsigned32"
_CLApAirTimeFairnessClientFramesSent_Object = MibTableColumn
cLApAirTimeFairnessClientFramesSent = _CLApAirTimeFairnessClientFramesSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 16, 9, 1, 3),
    _CLApAirTimeFairnessClientFramesSent_Type()
)
cLApAirTimeFairnessClientFramesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApAirTimeFairnessClientFramesSent.setStatus("current")
if mibBuilder.loadTexts:
    cLApAirTimeFairnessClientFramesSent.setUnits("bytes")


class _CLApAirTimeFairnessClientFramesDropped_Type(Unsigned32):
    """Custom type cLApAirTimeFairnessClientFramesDropped based on Unsigned32"""
    defaultValue = 0


_CLApAirTimeFairnessClientFramesDropped_Type.__name__ = "Unsigned32"
_CLApAirTimeFairnessClientFramesDropped_Object = MibTableColumn
cLApAirTimeFairnessClientFramesDropped = _CLApAirTimeFairnessClientFramesDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 16, 9, 1, 4),
    _CLApAirTimeFairnessClientFramesDropped_Type()
)
cLApAirTimeFairnessClientFramesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApAirTimeFairnessClientFramesDropped.setStatus("current")
if mibBuilder.loadTexts:
    cLApAirTimeFairnessClientFramesDropped.setUnits("bytes")


class _CLApAirTimeFairnessClientUsage_Type(Integer32):
    """Custom type cLApAirTimeFairnessClientUsage based on Integer32"""
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
        *(("none", 1),
          ("lowusage", 2),
          ("regusage", 3),
          ("overusage", 4))
    )


_CLApAirTimeFairnessClientUsage_Type.__name__ = "Integer32"
_CLApAirTimeFairnessClientUsage_Object = MibTableColumn
cLApAirTimeFairnessClientUsage = _CLApAirTimeFairnessClientUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 16, 9, 1, 5),
    _CLApAirTimeFairnessClientUsage_Type()
)
cLApAirTimeFairnessClientUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApAirTimeFairnessClientUsage.setStatus("current")
_CLQoSMapConfig_ObjectIdentity = ObjectIdentity
cLQoSMapConfig = _CLQoSMapConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 17)
)
_CLQosMapStatus_Type = TruthValue
_CLQosMapStatus_Object = MibScalar
cLQosMapStatus = _CLQosMapStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 17, 1),
    _CLQosMapStatus_Type()
)
cLQosMapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQosMapStatus.setStatus("current")
_CLQoSMapUpRangesTable_Object = MibTable
cLQoSMapUpRangesTable = _CLQoSMapUpRangesTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 17, 2)
)
if mibBuilder.loadTexts:
    cLQoSMapUpRangesTable.setStatus("deprecated")
_CLQoSUpTableEntry_Object = MibTableRow
cLQoSUpTableEntry = _CLQoSUpTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 17, 2, 1)
)
cLQoSUpTableEntry.setIndexNames(
    (0, "CISCO-LWAPP-QOS-MIB", "cLQoSUpTableIndex"),
)
if mibBuilder.loadTexts:
    cLQoSUpTableEntry.setStatus("deprecated")
_CLQoSUpTableIndex_Type = Unsigned32
_CLQoSUpTableIndex_Object = MibTableColumn
cLQoSUpTableIndex = _CLQoSUpTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 17, 2, 1, 1),
    _CLQoSUpTableIndex_Type()
)
cLQoSUpTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLQoSUpTableIndex.setStatus("deprecated")
_CLQoSMapUp_Type = Unsigned32
_CLQoSMapUp_Object = MibTableColumn
cLQoSMapUp = _CLQoSMapUp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 17, 2, 1, 2),
    _CLQoSMapUp_Type()
)
cLQoSMapUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQoSMapUp.setStatus("deprecated")
_CLQoSMapDscpDefault_Type = Unsigned32
_CLQoSMapDscpDefault_Object = MibTableColumn
cLQoSMapDscpDefault = _CLQoSMapDscpDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 17, 2, 1, 3),
    _CLQoSMapDscpDefault_Type()
)
cLQoSMapDscpDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQoSMapDscpDefault.setStatus("deprecated")
_CLQoSMapDscpLow_Type = Unsigned32
_CLQoSMapDscpLow_Object = MibTableColumn
cLQoSMapDscpLow = _CLQoSMapDscpLow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 17, 2, 1, 4),
    _CLQoSMapDscpLow_Type()
)
cLQoSMapDscpLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQoSMapDscpLow.setStatus("deprecated")
_CLQoSMapDscpHigh_Type = Unsigned32
_CLQoSMapDscpHigh_Object = MibTableColumn
cLQoSMapDscpHigh = _CLQoSMapDscpHigh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 17, 2, 1, 5),
    _CLQoSMapDscpHigh_Type()
)
cLQoSMapDscpHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQoSMapDscpHigh.setStatus("deprecated")
_CLQoSMapUpExceptionsTable_Object = MibTable
cLQoSMapUpExceptionsTable = _CLQoSMapUpExceptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 17, 3)
)
if mibBuilder.loadTexts:
    cLQoSMapUpExceptionsTable.setStatus("deprecated")
_CLQoSUpExceptionsTableEntry_Object = MibTableRow
cLQoSUpExceptionsTableEntry = _CLQoSUpExceptionsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 17, 3, 1)
)
cLQoSUpExceptionsTableEntry.setIndexNames(
    (0, "CISCO-LWAPP-QOS-MIB", "cLQoSMapExceptionNumber"),
)
if mibBuilder.loadTexts:
    cLQoSUpExceptionsTableEntry.setStatus("deprecated")
_CLQoSMapExceptionNumber_Type = Unsigned32
_CLQoSMapExceptionNumber_Object = MibTableColumn
cLQoSMapExceptionNumber = _CLQoSMapExceptionNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 17, 3, 1, 1),
    _CLQoSMapExceptionNumber_Type()
)
cLQoSMapExceptionNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLQoSMapExceptionNumber.setStatus("deprecated")
_CLQoSMapExceptionUp_Type = Unsigned32
_CLQoSMapExceptionUp_Object = MibTableColumn
cLQoSMapExceptionUp = _CLQoSMapExceptionUp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 17, 3, 1, 2),
    _CLQoSMapExceptionUp_Type()
)
cLQoSMapExceptionUp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLQoSMapExceptionUp.setStatus("deprecated")
_CLQoSMapExceptionDscp_Type = Unsigned32
_CLQoSMapExceptionDscp_Object = MibTableColumn
cLQoSMapExceptionDscp = _CLQoSMapExceptionDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 17, 3, 1, 3),
    _CLQoSMapExceptionDscp_Type()
)
cLQoSMapExceptionDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLQoSMapExceptionDscp.setStatus("deprecated")
_CLQosMapExceptionsRowStatus_Type = RowStatus
_CLQosMapExceptionsRowStatus_Object = MibTableColumn
cLQosMapExceptionsRowStatus = _CLQosMapExceptionsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 17, 3, 1, 4),
    _CLQosMapExceptionsRowStatus_Type()
)
cLQosMapExceptionsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLQosMapExceptionsRowStatus.setStatus("deprecated")
_CLQosCopyClientDscpStatus_Type = TruthValue
_CLQosCopyClientDscpStatus_Object = MibScalar
cLQosCopyClientDscpStatus = _CLQosCopyClientDscpStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 17, 4),
    _CLQosCopyClientDscpStatus_Type()
)
cLQosCopyClientDscpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQosCopyClientDscpStatus.setStatus("current")


class _CLQosMapExceptionsClearAll_Type(Integer32):
    """Custom type cLQosMapExceptionsClearAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear-all", 1),
          ("no-operation", 2))
    )


_CLQosMapExceptionsClearAll_Type.__name__ = "Integer32"
_CLQosMapExceptionsClearAll_Object = MibScalar
cLQosMapExceptionsClearAll = _CLQosMapExceptionsClearAll_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 17, 5),
    _CLQosMapExceptionsClearAll_Type()
)
cLQosMapExceptionsClearAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQosMapExceptionsClearAll.setStatus("current")


class _CLQosMapDefault_Type(Integer32):
    """Custom type cLQosMapDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("no-operation", 2))
    )


_CLQosMapDefault_Type.__name__ = "Integer32"
_CLQosMapDefault_Object = MibScalar
cLQosMapDefault = _CLQosMapDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 17, 6),
    _CLQosMapDefault_Type()
)
cLQosMapDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQosMapDefault.setStatus("current")
_CLQoSFastlaneConfig_ObjectIdentity = ObjectIdentity
cLQoSFastlaneConfig = _CLQoSFastlaneConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 18)
)


class _CLQosFastlaneDisable_Type(Integer32):
    """Custom type cLQosFastlaneDisable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("no-operation", 2))
    )


_CLQosFastlaneDisable_Type.__name__ = "Integer32"
_CLQosFastlaneDisable_Object = MibScalar
cLQosFastlaneDisable = _CLQosFastlaneDisable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 18, 1),
    _CLQosFastlaneDisable_Type()
)
cLQosFastlaneDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQosFastlaneDisable.setStatus("current")
_CiscoLwappQosMIBTableObjects_ObjectIdentity = ObjectIdentity
ciscoLwappQosMIBTableObjects = _CiscoLwappQosMIBTableObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 19)
)
_CLQoSMapDownstreamDscpTable_Object = MibTable
cLQoSMapDownstreamDscpTable = _CLQoSMapDownstreamDscpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 19, 1)
)
if mibBuilder.loadTexts:
    cLQoSMapDownstreamDscpTable.setStatus("current")
_CLQoSMapDownstreamDscpEntry_Object = MibTableRow
cLQoSMapDownstreamDscpEntry = _CLQoSMapDownstreamDscpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 19, 1, 1)
)
cLQoSMapDownstreamDscpEntry.setIndexNames(
    (0, "CISCO-LWAPP-QOS-MIB", "cLQoSMapDownstreamDscpIndex"),
)
if mibBuilder.loadTexts:
    cLQoSMapDownstreamDscpEntry.setStatus("current")
_CLQoSMapDownstreamDscpIndex_Type = Unsigned32
_CLQoSMapDownstreamDscpIndex_Object = MibTableColumn
cLQoSMapDownstreamDscpIndex = _CLQoSMapDownstreamDscpIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 19, 1, 1, 1),
    _CLQoSMapDownstreamDscpIndex_Type()
)
cLQoSMapDownstreamDscpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLQoSMapDownstreamDscpIndex.setStatus("current")
_CLQoSMapDownstreamDscpLow_Type = Unsigned32
_CLQoSMapDownstreamDscpLow_Object = MibTableColumn
cLQoSMapDownstreamDscpLow = _CLQoSMapDownstreamDscpLow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 19, 1, 1, 2),
    _CLQoSMapDownstreamDscpLow_Type()
)
cLQoSMapDownstreamDscpLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQoSMapDownstreamDscpLow.setStatus("current")
_CLQoSMapDownstreamDscpHigh_Type = Unsigned32
_CLQoSMapDownstreamDscpHigh_Object = MibTableColumn
cLQoSMapDownstreamDscpHigh = _CLQoSMapDownstreamDscpHigh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 19, 1, 1, 3),
    _CLQoSMapDownstreamDscpHigh_Type()
)
cLQoSMapDownstreamDscpHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQoSMapDownstreamDscpHigh.setStatus("current")
_CLQoSMapDownstreamUp_Type = Unsigned32
_CLQoSMapDownstreamUp_Object = MibTableColumn
cLQoSMapDownstreamUp = _CLQoSMapDownstreamUp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 19, 1, 1, 4),
    _CLQoSMapDownstreamUp_Type()
)
cLQoSMapDownstreamUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQoSMapDownstreamUp.setStatus("current")
_CLQoSMapDownstreamUpExceptionsTable_Object = MibTable
cLQoSMapDownstreamUpExceptionsTable = _CLQoSMapDownstreamUpExceptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 19, 2)
)
if mibBuilder.loadTexts:
    cLQoSMapDownstreamUpExceptionsTable.setStatus("current")
_CLQoSDownstreamUpExceptionsTableEntry_Object = MibTableRow
cLQoSDownstreamUpExceptionsTableEntry = _CLQoSDownstreamUpExceptionsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 19, 2, 1)
)
cLQoSDownstreamUpExceptionsTableEntry.setIndexNames(
    (0, "CISCO-LWAPP-QOS-MIB", "cLQoSMapDownstreamExceptionNumber"),
)
if mibBuilder.loadTexts:
    cLQoSDownstreamUpExceptionsTableEntry.setStatus("current")
_CLQoSMapDownstreamExceptionNumber_Type = Unsigned32
_CLQoSMapDownstreamExceptionNumber_Object = MibTableColumn
cLQoSMapDownstreamExceptionNumber = _CLQoSMapDownstreamExceptionNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 19, 2, 1, 1),
    _CLQoSMapDownstreamExceptionNumber_Type()
)
cLQoSMapDownstreamExceptionNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLQoSMapDownstreamExceptionNumber.setStatus("current")
_CLQoSMapDownstreamExceptionDscp_Type = Unsigned32
_CLQoSMapDownstreamExceptionDscp_Object = MibTableColumn
cLQoSMapDownstreamExceptionDscp = _CLQoSMapDownstreamExceptionDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 19, 2, 1, 2),
    _CLQoSMapDownstreamExceptionDscp_Type()
)
cLQoSMapDownstreamExceptionDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLQoSMapDownstreamExceptionDscp.setStatus("current")
_CLQoSMapDownstreamExceptionUp_Type = Unsigned32
_CLQoSMapDownstreamExceptionUp_Object = MibTableColumn
cLQoSMapDownstreamExceptionUp = _CLQoSMapDownstreamExceptionUp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 19, 2, 1, 3),
    _CLQoSMapDownstreamExceptionUp_Type()
)
cLQoSMapDownstreamExceptionUp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLQoSMapDownstreamExceptionUp.setStatus("current")
_CLQosMapDownstreamExceptionsRowStatus_Type = RowStatus
_CLQosMapDownstreamExceptionsRowStatus_Object = MibTableColumn
cLQosMapDownstreamExceptionsRowStatus = _CLQosMapDownstreamExceptionsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 19, 2, 1, 4),
    _CLQosMapDownstreamExceptionsRowStatus_Type()
)
cLQosMapDownstreamExceptionsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLQosMapDownstreamExceptionsRowStatus.setStatus("current")
_CLQoSMapUpstreamUpDscpTable_Object = MibTable
cLQoSMapUpstreamUpDscpTable = _CLQoSMapUpstreamUpDscpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 19, 3)
)
if mibBuilder.loadTexts:
    cLQoSMapUpstreamUpDscpTable.setStatus("current")
_CLQoSMapUpstreamUpDscpEntry_Object = MibTableRow
cLQoSMapUpstreamUpDscpEntry = _CLQoSMapUpstreamUpDscpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 19, 3, 1)
)
cLQoSMapUpstreamUpDscpEntry.setIndexNames(
    (0, "CISCO-LWAPP-QOS-MIB", "cLQoSMapUpstreamDscpIndex"),
)
if mibBuilder.loadTexts:
    cLQoSMapUpstreamUpDscpEntry.setStatus("current")
_CLQoSMapUpstreamDscpIndex_Type = Unsigned32
_CLQoSMapUpstreamDscpIndex_Object = MibTableColumn
cLQoSMapUpstreamDscpIndex = _CLQoSMapUpstreamDscpIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 19, 3, 1, 1),
    _CLQoSMapUpstreamDscpIndex_Type()
)
cLQoSMapUpstreamDscpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLQoSMapUpstreamDscpIndex.setStatus("current")
_CLQoSMapUpstreamUp_Type = Unsigned32
_CLQoSMapUpstreamUp_Object = MibTableColumn
cLQoSMapUpstreamUp = _CLQoSMapUpstreamUp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 19, 3, 1, 2),
    _CLQoSMapUpstreamUp_Type()
)
cLQoSMapUpstreamUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQoSMapUpstreamUp.setStatus("current")
_CLQoSMapUpstreamDscp_Type = Unsigned32
_CLQoSMapUpstreamDscp_Object = MibTableColumn
cLQoSMapUpstreamDscp = _CLQoSMapUpstreamDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 19, 3, 1, 3),
    _CLQoSMapUpstreamDscp_Type()
)
cLQoSMapUpstreamDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQoSMapUpstreamDscp.setStatus("current")
_CiscoLwappQosMIBGlobalObjects_ObjectIdentity = ObjectIdentity
ciscoLwappQosMIBGlobalObjects = _CiscoLwappQosMIBGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 20)
)


class _CLQosUpstreamCopyClientDscpStatus_Type(TruthValue):
    """Custom type cLQosUpstreamCopyClientDscpStatus based on TruthValue"""
    defaultValue = 2


_CLQosUpstreamCopyClientDscpStatus_Type.__name__ = "TruthValue"
_CLQosUpstreamCopyClientDscpStatus_Object = MibScalar
cLQosUpstreamCopyClientDscpStatus = _CLQosUpstreamCopyClientDscpStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 20, 1),
    _CLQosUpstreamCopyClientDscpStatus_Type()
)
cLQosUpstreamCopyClientDscpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQosUpstreamCopyClientDscpStatus.setStatus("current")
_CiscoLwappQosMIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappQosMIBConform = _CiscoLwappQosMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 2)
)
_CiscoLwappQosMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappQosMIBCompliances = _CiscoLwappQosMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 2, 1)
)
_CiscoLwappQosMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLwappQosMIBGroups = _CiscoLwappQosMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 2, 2)
)

# Managed Objects groups

ciscoLwappQosDot11aConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 2, 2, 1)
)
ciscoLwappQosDot11aConfigGroup.setObjects(
      *(("CISCO-LWAPP-QOS-MIB", "cLQd11aVoiceAdmCtrlSupport"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11aVoiceMaxAdmBandwidth"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11aVoiceMaxRoamBandwidth"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11aVideoAdmCtrlSupport"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11aVideoMaxAdmBandwidth"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11aVideoMaxRoamBandwidth"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11aGprProbeInterval"))
)
if mibBuilder.loadTexts:
    ciscoLwappQosDot11aConfigGroup.setStatus("current")

ciscoLwappQosDot11bConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 2, 2, 2)
)
ciscoLwappQosDot11bConfigGroup.setObjects(
      *(("CISCO-LWAPP-QOS-MIB", "cLQd11bVoiceAdmCtrlSupport"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11bVoiceMaxAdmBandwidth"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11bVoiceMaxRoamBandwidth"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11bVideoAdmCtrlSupport"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11bVideoMaxAdmBandwidth"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11bVideoMaxRoamBandwidth"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11bGprProbeInterval"))
)
if mibBuilder.loadTexts:
    ciscoLwappQosDot11bConfigGroup.setStatus("current")

ciscoLwappQosDot11WlanConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 2, 2, 3)
)
ciscoLwappQosDot11WlanConfigGroup.setObjects(
    ("CISCO-LWAPP-QOS-MIB", "cLQd11GprSupport")
)
if mibBuilder.loadTexts:
    ciscoLwappQosDot11WlanConfigGroup.setStatus("current")

ciscoLwappQosDot11CacStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 2, 2, 4)
)
ciscoLwappQosDot11CacStatsGroup.setObjects(
      *(("CISCO-LWAPP-QOS-MIB", "cLQd11CacVoiceBwInUse"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11CacVideoBwInUse"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11CacVoiceCallsInProgress"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11CacRoamVoiceCallsInProg"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11CacTotalVoiceCallsAP"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11CacTotalRoamCallsAP"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11CacVoiceCallsRejectedAP"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11CacRoamCallsRejectedAP"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11CacRejCallsInsufBw"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11CacRejCallsBadParams"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11CacRejCallsPhyRate"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11CacRejCallsQosPolicy"))
)
if mibBuilder.loadTexts:
    ciscoLwappQosDot11CacStatsGroup.setStatus("current")

ciscoLwappQosDot11aConfigGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 2, 2, 5)
)
ciscoLwappQosDot11aConfigGroupSup1.setObjects(
      *(("CISCO-LWAPP-QOS-MIB", "cLQd11aVoiceCtrl"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11aExpeditedBw"))
)
if mibBuilder.loadTexts:
    ciscoLwappQosDot11aConfigGroupSup1.setStatus("current")

ciscoLwappQosDot11bConfigGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 2, 2, 6)
)
ciscoLwappQosDot11bConfigGroupSup1.setObjects(
      *(("CISCO-LWAPP-QOS-MIB", "cLQd11bVoiceCtrl"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11bExpeditedBw"))
)
if mibBuilder.loadTexts:
    ciscoLwappQosDot11bConfigGroupSup1.setStatus("current")

ciscoLwappQosDot11aConfigGroupSup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 2, 2, 7)
)
ciscoLwappQosDot11aConfigGroupSup2.setObjects(
      *(("CISCO-LWAPP-QOS-MIB", "cLQd11aEdcaProfile"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11aMacOptimization"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11aMaxCallLimit"))
)
if mibBuilder.loadTexts:
    ciscoLwappQosDot11aConfigGroupSup2.setStatus("current")

ciscoLwappQosDot11bConfigGroupSup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 2, 2, 8)
)
ciscoLwappQosDot11bConfigGroupSup2.setObjects(
      *(("CISCO-LWAPP-QOS-MIB", "cLQd11bEdcaProfile"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11bMacOptimization"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11bMaxCallLimit"))
)
if mibBuilder.loadTexts:
    ciscoLwappQosDot11bConfigGroupSup2.setStatus("current")

ciscoLwappQosDot11SipCacStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 2, 2, 9)
)
ciscoLwappQosDot11SipCacStatsGroup.setObjects(
      *(("CISCO-LWAPP-QOS-MIB", "cLQd11SipCacNonRoamCallsInProgress"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11SipCacRoamCallsInProg"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11SipCacTotalNonRoamCallsAP"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11SipCacTotalRoamCallsAP"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11SipCacNonRoamCallsRejectedInSuffBw"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11SipCacRoamCallsRejectedInSuffBw"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11SipCacNonRoamCallsRejectedMaxLimit"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11SipCacRoamCallsRejectedMaxLimit"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11SipCacRejCallsQosPolicy"))
)
if mibBuilder.loadTexts:
    ciscoLwappQosDot11SipCacStatsGroup.setStatus("current")

ciscoLwappQosDot11SipConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 2, 2, 10)
)
ciscoLwappQosDot11SipConfigGroup.setObjects(
      *(("CISCO-LWAPP-QOS-MIB", "cLQd11SipCacConfigCodecType"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11SipCacConfigBw"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11SipCacConfigVoiceSampleSize"))
)
if mibBuilder.loadTexts:
    ciscoLwappQosDot11SipConfigGroup.setStatus("current")

ciscoLwappQosDot11VoiceStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 2, 2, 11)
)
ciscoLwappQosDot11VoiceStatsGroup.setObjects(
      *(("CISCO-LWAPP-QOS-MIB", "cLQd11VoiceCallCounts"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11CacVoiceCallTimePeriod"))
)
if mibBuilder.loadTexts:
    ciscoLwappQosDot11VoiceStatsGroup.setStatus("current")

ciscoLwappQosDot11VoiceConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 2, 2, 12)
)
ciscoLwappQosDot11VoiceConfigGroup.setObjects(
      *(("CISCO-LWAPP-QOS-MIB", "cLQVoiceWlanConfigDetectVoipCallFailure"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVoiceClientCallingNumber"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVoiceClientLastCalledNumber"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVoiceClientLastCallFailureReasonCode"))
)
if mibBuilder.loadTexts:
    ciscoLwappQosDot11VoiceConfigGroup.setStatus("current")

ciscoLwappQosConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 2, 2, 14)
)
ciscoLwappQosConfigGroup.setObjects(
    ("CISCO-LWAPP-QOS-MIB", "ciscoLwappVoipCallFailureNotifEnabled")
)
if mibBuilder.loadTexts:
    ciscoLwappQosConfigGroup.setStatus("current")

ciscoLwappQosConfigGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 2, 2, 16)
)
ciscoLwappQosConfigGroupSup1.setObjects(
    ("CISCO-LWAPP-QOS-MIB", "ciscoLwappKtsVoipCallFailureNotifEnabled")
)
if mibBuilder.loadTexts:
    ciscoLwappQosConfigGroupSup1.setStatus("current")

cLQoSProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 2, 2, 17)
)
cLQoSProfileGroup.setObjects(
      *(("CISCO-LWAPP-QOS-MIB", "cLQoSMaximumPriority"),
        ("CISCO-LWAPP-QOS-MIB", "cLQoSUnicastDefPriority"),
        ("CISCO-LWAPP-QOS-MIB", "cLQoSMulticastDefPriority"),
        ("CISCO-LWAPP-QOS-MIB", "cLQoSClientDSAverageDataRate"),
        ("CISCO-LWAPP-QOS-MIB", "cLQoSClientUSAverageDataRate"),
        ("CISCO-LWAPP-QOS-MIB", "cLQoSClientDSBurstDataRate"),
        ("CISCO-LWAPP-QOS-MIB", "cLQoSClientUSBurstDataRate"),
        ("CISCO-LWAPP-QOS-MIB", "cLQoSClientDSAvgRealTimeDataRate"),
        ("CISCO-LWAPP-QOS-MIB", "cLQoSClientUSAvgRealTimeDataRate"),
        ("CISCO-LWAPP-QOS-MIB", "cLQoSClientDSBurstRealTimeDataRate"),
        ("CISCO-LWAPP-QOS-MIB", "cLQoSClientUSBurstRealTimeDataRate"),
        ("CISCO-LWAPP-QOS-MIB", "cLQoSSsidDSAverageDataRate"),
        ("CISCO-LWAPP-QOS-MIB", "cLQoSSsidUSAverageDataRate"),
        ("CISCO-LWAPP-QOS-MIB", "cLQoSSsidDSBurstDataRate"),
        ("CISCO-LWAPP-QOS-MIB", "cLQoSSsidUSBurstDataRate"),
        ("CISCO-LWAPP-QOS-MIB", "cLQoSSsidDSAvgRealTimeDataRate"),
        ("CISCO-LWAPP-QOS-MIB", "cLQoSSsidUSAvgRealTimeDataRate"),
        ("CISCO-LWAPP-QOS-MIB", "cLQoSSsidDSBurstRealTimeDataRate"),
        ("CISCO-LWAPP-QOS-MIB", "cLQoSSsidUSBurstRealTimeDataRate"),
        ("CISCO-LWAPP-QOS-MIB", "cLQoSWlanDSAverageDataRate"),
        ("CISCO-LWAPP-QOS-MIB", "cLQoSWlanUSAverageDataRate"),
        ("CISCO-LWAPP-QOS-MIB", "cLQoSWlanDSBurstDataRate"),
        ("CISCO-LWAPP-QOS-MIB", "cLQoSWlanUSBurstDataRate"),
        ("CISCO-LWAPP-QOS-MIB", "cLQoSWlanDSAvgRealTimeDataRate"),
        ("CISCO-LWAPP-QOS-MIB", "cLQoSWlanUSAvgRealTimeDataRate"),
        ("CISCO-LWAPP-QOS-MIB", "cLQoSWlanDSBurstRealTimeDataRate"),
        ("CISCO-LWAPP-QOS-MIB", "cLQoSWlanUSBurstRealTimeDataRate"))
)
if mibBuilder.loadTexts:
    cLQoSProfileGroup.setStatus("current")


# Notification objects

ciscoLwappVoipCallFailureNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 0, 1)
)
ciscoLwappVoipCallFailureNotif.setObjects(
      *(("CISCO-LWAPP-QOS-MIB", "cLQVoiceClientLastCallFailureReasonCode"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVoiceClientCallingNumber"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVoiceClientLastCalledNumber"),
        ("CISCO-LWAPP-AP-MIB", "cLApName"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfType"))
)
if mibBuilder.loadTexts:
    ciscoLwappVoipCallFailureNotif.setStatus(
        "current"
    )

ciscoLwappMediaMCStreamFailureNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 0, 2)
)
ciscoLwappMediaMCStreamFailureNotif.setObjects(
      *(("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVMediaClientSrcIpAddr"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVMediaClientSrcIpAddrType"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVMediaClientDestIpAddr"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVMediaClientDestIpAddrType"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVMediaClientHistLastFailureReasonCode"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVMediaClientHistTimeStamp"),
        ("CISCO-LWAPP-QOS-MIB", "cLQMStreamName"),
        ("CISCO-LWAPP-AP-MIB", "cLApName"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfType"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVMediaClientHistCfgBw"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVMediaClientHistCurrentRate"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVMediaClientHistVideoPktSize"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVMediaClientHistVideoUtil"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVMediaClientHistVoiceUtil"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVMediaClientHistChannelUtil"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVMediaClientHistQueueUtil"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVMediaClientHistVideoPps"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVMediaClientHistVideoDelay"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVMediaClientHistPktLossDiscard"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVMediaClientHistPktLossFail"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVMediaClientHistNumVideoStreams"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVMediaClientHistCacEnable"))
)
if mibBuilder.loadTexts:
    ciscoLwappMediaMCStreamFailureNotif.setStatus(
        "current"
    )

ciscoLwappMediaMCStreamAdmitNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 0, 3)
)
ciscoLwappMediaMCStreamAdmitNotif.setObjects(
      *(("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVMediaClientSrcIpAddr"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVMediaClientSrcIpAddrType"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVMediaClientDestIpAddr"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVMediaClientDestIpAddrType"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVMediaClientHistLastFailureReasonCode"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVMediaClientHistTimeStamp"),
        ("CISCO-LWAPP-QOS-MIB", "cLQMStreamName"),
        ("CISCO-LWAPP-AP-MIB", "cLApName"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfType"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVMediaClientHistCfgBw"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVMediaClientHistCurrentRate"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVMediaClientHistVideoPktSize"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVMediaClientHistVideoUtil"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVMediaClientHistVoiceUtil"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVMediaClientHistChannelUtil"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVMediaClientHistQueueUtil"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVMediaClientHistVideoPps"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVMediaClientHistVideoDelay"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVMediaClientHistPktLossDiscard"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVMediaClientHistPktLossFail"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVMediaClientHistNumVideoStreams"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVMediaClientHistCacEnable"))
)
if mibBuilder.loadTexts:
    ciscoLwappMediaMCStreamAdmitNotif.setStatus(
        "current"
    )

ciscoLwappMediaMCStreamDelistNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 0, 4)
)
ciscoLwappMediaMCStreamDelistNotif.setObjects(
      *(("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVMediaClientSrcIpAddr"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVMediaClientSrcIpAddrType"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVMediaClientDestIpAddr"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVMediaClientDestIpAddrType"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVMediaClientHistLastFailureReasonCode"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVMediaClientHistTimeStamp"),
        ("CISCO-LWAPP-QOS-MIB", "cLQMStreamName"),
        ("CISCO-LWAPP-AP-MIB", "cLApName"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfType"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVMediaClientHistCfgBw"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVMediaClientHistCurrentRate"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVMediaClientHistVideoPktSize"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVMediaClientHistVideoUtil"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVMediaClientHistVoiceUtil"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVMediaClientHistChannelUtil"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVMediaClientHistQueueUtil"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVMediaClientHistVideoPps"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVMediaClientHistVideoDelay"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVMediaClientHistPktLossDiscard"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVMediaClientHistPktLossFail"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVMediaClientHistNumVideoStreams"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVMediaClientHistCacEnable"))
)
if mibBuilder.loadTexts:
    ciscoLwappMediaMCStreamDelistNotif.setStatus(
        "current"
    )

ciscoLwappKtsVoipCallFailureNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 0, 5)
)
ciscoLwappKtsVoipCallFailureNotif.setObjects(
      *(("CISCO-LWAPP-QOS-MIB", "cLQVoiceClientLastCallFailureReasonCode"),
        ("CISCO-LWAPP-AP-MIB", "cLApName"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfType"))
)
if mibBuilder.loadTexts:
    ciscoLwappKtsVoipCallFailureNotif.setStatus(
        "current"
    )


# Notifications groups

ciscoLwappQosDot11VoiceNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 2, 2, 13)
)
ciscoLwappQosDot11VoiceNotifGroup.setObjects(
    ("CISCO-LWAPP-QOS-MIB", "ciscoLwappVoipCallFailureNotif")
)
if mibBuilder.loadTexts:
    ciscoLwappQosDot11VoiceNotifGroup.setStatus(
        "current"
    )

ciscoLwappQosDot11VoiceNotifGroupSup1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 2, 2, 15)
)
ciscoLwappQosDot11VoiceNotifGroupSup1.setObjects(
    ("CISCO-LWAPP-QOS-MIB", "ciscoLwappKtsVoipCallFailureNotif")
)
if mibBuilder.loadTexts:
    ciscoLwappQosDot11VoiceNotifGroupSup1.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoLwappQosMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 2, 1, 1)
)
ciscoLwappQosMIBCompliance.setObjects(
      *(("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11aConfigGroup"),
        ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11bConfigGroup"),
        ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11WlanConfigGroup"),
        ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11CacStatsGroup"))
)
if mibBuilder.loadTexts:
    ciscoLwappQosMIBCompliance.setStatus(
        "deprecated"
    )

ciscoLwappQosMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 2, 1, 2)
)
ciscoLwappQosMIBComplianceRev1.setObjects(
      *(("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11aConfigGroup"),
        ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11bConfigGroup"),
        ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11WlanConfigGroup"),
        ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11CacStatsGroup"),
        ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11aConfigGroupSup1"),
        ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11bConfigGroupSup1"))
)
if mibBuilder.loadTexts:
    ciscoLwappQosMIBComplianceRev1.setStatus(
        "deprecated"
    )

ciscoLwappQosMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 2, 1, 3)
)
ciscoLwappQosMIBComplianceRev2.setObjects(
      *(("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11aConfigGroup"),
        ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11bConfigGroup"),
        ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11WlanConfigGroup"),
        ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11CacStatsGroup"),
        ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11aConfigGroupSup1"),
        ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11bConfigGroupSup1"),
        ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11aConfigGroupSup2"),
        ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11bConfigGroupSup2"),
        ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11SipCacStatsGroup"),
        ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11SipConfigGroup"),
        ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11VoiceStatsGroup"),
        ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11VoiceConfigGroup"),
        ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11VoiceNotifGroup"),
        ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosConfigGroup"))
)
if mibBuilder.loadTexts:
    ciscoLwappQosMIBComplianceRev2.setStatus(
        "deprecated"
    )

ciscoLwappQosMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 2, 1, 4)
)
ciscoLwappQosMIBComplianceRev3.setObjects(
      *(("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11aConfigGroup"),
        ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11bConfigGroup"),
        ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11WlanConfigGroup"),
        ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11CacStatsGroup"),
        ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11aConfigGroupSup1"),
        ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11bConfigGroupSup1"),
        ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11aConfigGroupSup2"),
        ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11bConfigGroupSup2"),
        ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11SipCacStatsGroup"),
        ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11SipConfigGroup"),
        ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11VoiceStatsGroup"),
        ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11VoiceConfigGroup"),
        ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11VoiceNotifGroup"),
        ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosConfigGroup"),
        ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11VoiceNotifGroupSup1"),
        ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosConfigGroupSup1"))
)
if mibBuilder.loadTexts:
    ciscoLwappQosMIBComplianceRev3.setStatus(
        "deprecated"
    )

ciscoLwappQosMIBComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 2, 1, 5)
)
ciscoLwappQosMIBComplianceRev4.setObjects(
      *(("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11aConfigGroup"),
        ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11bConfigGroup"),
        ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11WlanConfigGroup"),
        ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11CacStatsGroup"),
        ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11aConfigGroupSup1"),
        ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11bConfigGroupSup1"),
        ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11aConfigGroupSup2"),
        ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11bConfigGroupSup2"),
        ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11SipCacStatsGroup"),
        ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11SipConfigGroup"),
        ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11VoiceStatsGroup"),
        ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11VoiceConfigGroup"),
        ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11VoiceNotifGroup"),
        ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosConfigGroup"),
        ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11VoiceNotifGroupSup1"),
        ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosConfigGroupSup1"),
        ("CISCO-LWAPP-QOS-MIB", "cLQoSProfileGroup"))
)
if mibBuilder.loadTexts:
    ciscoLwappQosMIBComplianceRev4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-QOS-MIB",
    **{"CiscoLwappDot11aPhyRates": CiscoLwappDot11aPhyRates,
       "CiscoLwappDot11bPhyRates": CiscoLwappDot11bPhyRates,
       "ciscoLwappQosMIB": ciscoLwappQosMIB,
       "ciscoLwappQosMIBNotifs": ciscoLwappQosMIBNotifs,
       "ciscoLwappVoipCallFailureNotif": ciscoLwappVoipCallFailureNotif,
       "ciscoLwappMediaMCStreamFailureNotif": ciscoLwappMediaMCStreamFailureNotif,
       "ciscoLwappMediaMCStreamAdmitNotif": ciscoLwappMediaMCStreamAdmitNotif,
       "ciscoLwappMediaMCStreamDelistNotif": ciscoLwappMediaMCStreamDelistNotif,
       "ciscoLwappKtsVoipCallFailureNotif": ciscoLwappKtsVoipCallFailureNotif,
       "ciscoLwappQosMIBObjects": ciscoLwappQosMIBObjects,
       "cLQd11aCACConfig": cLQd11aCACConfig,
       "cLQd11aVoiceAdmCtrlSupport": cLQd11aVoiceAdmCtrlSupport,
       "cLQd11aVoiceMaxAdmBandwidth": cLQd11aVoiceMaxAdmBandwidth,
       "cLQd11aVoiceMaxRoamBandwidth": cLQd11aVoiceMaxRoamBandwidth,
       "cLQd11aVideoAdmCtrlSupport": cLQd11aVideoAdmCtrlSupport,
       "cLQd11aVideoMaxAdmBandwidth": cLQd11aVideoMaxAdmBandwidth,
       "cLQd11aVideoMaxRoamBandwidth": cLQd11aVideoMaxRoamBandwidth,
       "cLQd11aGprProbeInterval": cLQd11aGprProbeInterval,
       "cLQd11aVoiceCtrl": cLQd11aVoiceCtrl,
       "cLQd11aExpeditedBw": cLQd11aExpeditedBw,
       "cLQd11aEdcaProfile": cLQd11aEdcaProfile,
       "cLQd11aMacOptimization": cLQd11aMacOptimization,
       "cLQd11aMaxCallLimit": cLQd11aMaxCallLimit,
       "cLQd11aMcastDirectEnable": cLQd11aMcastDirectEnable,
       "cLQd11aBestEffortAdmission": cLQd11aBestEffortAdmission,
       "cLQd11aRedirectBestEffort": cLQd11aRedirectBestEffort,
       "cLQd11aRadioMaxStreams": cLQd11aRadioMaxStreams,
       "cLQd11aMaxVideoATPercent": cLQd11aMaxVideoATPercent,
       "cLQd11aMaxVoiceATPercent": cLQd11aMaxVoiceATPercent,
       "cLQd11aMaxMediaATPercent": cLQd11aMaxMediaATPercent,
       "cLQd11aMinPhyRate": cLQd11aMinPhyRate,
       "cLQd11aClientMaxStreams": cLQd11aClientMaxStreams,
       "cLQd11aSipCacSupportEnable": cLQd11aSipCacSupportEnable,
       "cLQd11aMaxRetryPercent": cLQd11aMaxRetryPercent,
       "cLQd11aVideoCtrl": cLQd11aVideoCtrl,
       "cLQd11aSipCacVideoEnable": cLQd11aSipCacVideoEnable,
       "cLQd11bCACConfig": cLQd11bCACConfig,
       "cLQd11bVoiceAdmCtrlSupport": cLQd11bVoiceAdmCtrlSupport,
       "cLQd11bVoiceMaxAdmBandwidth": cLQd11bVoiceMaxAdmBandwidth,
       "cLQd11bVoiceMaxRoamBandwidth": cLQd11bVoiceMaxRoamBandwidth,
       "cLQd11bVideoAdmCtrlSupport": cLQd11bVideoAdmCtrlSupport,
       "cLQd11bVideoMaxAdmBandwidth": cLQd11bVideoMaxAdmBandwidth,
       "cLQd11bVideoMaxRoamBandwidth": cLQd11bVideoMaxRoamBandwidth,
       "cLQd11bGprProbeInterval": cLQd11bGprProbeInterval,
       "cLQd11bVoiceCtrl": cLQd11bVoiceCtrl,
       "cLQd11bExpeditedBw": cLQd11bExpeditedBw,
       "cLQd11bEdcaProfile": cLQd11bEdcaProfile,
       "cLQd11bMacOptimization": cLQd11bMacOptimization,
       "cLQd11bMaxCallLimit": cLQd11bMaxCallLimit,
       "cLQd11bMcastDirectEnable": cLQd11bMcastDirectEnable,
       "cLQd11bBestEffortAdmission": cLQd11bBestEffortAdmission,
       "cLQd11bRedirectBestEffort": cLQd11bRedirectBestEffort,
       "cLQd11bRadioMaxStreams": cLQd11bRadioMaxStreams,
       "cLQd11bMaxVideoATPercent": cLQd11bMaxVideoATPercent,
       "cLQd11bMaxVoiceATPercent": cLQd11bMaxVoiceATPercent,
       "cLQd11bMaxMediaATPercent": cLQd11bMaxMediaATPercent,
       "cLQd11bMinPhyRate": cLQd11bMinPhyRate,
       "cLQd11bClientMaxStreams": cLQd11bClientMaxStreams,
       "cLQd11bSipCacSupportEnable": cLQd11bSipCacSupportEnable,
       "cLQd11bMaxRetryPercent": cLQd11bMaxRetryPercent,
       "cLQd11bVideoCtrl": cLQd11bVideoCtrl,
       "cLQd11bSipCacVideoEnable": cLQd11bSipCacVideoEnable,
       "cLQd11GprConfig": cLQd11GprConfig,
       "cLQd11GprTable": cLQd11GprTable,
       "cLQd11GprEntry": cLQd11GprEntry,
       "cLQd11GprSupport": cLQd11GprSupport,
       "cLQd11CACStats": cLQd11CACStats,
       "cLQd11CACStatsTable": cLQd11CACStatsTable,
       "cLQd11CACStatsEntry": cLQd11CACStatsEntry,
       "cLQd11CacVoiceBwInUse": cLQd11CacVoiceBwInUse,
       "cLQd11CacVideoBwInUse": cLQd11CacVideoBwInUse,
       "cLQd11CacVoiceCallsInProgress": cLQd11CacVoiceCallsInProgress,
       "cLQd11CacRoamVoiceCallsInProg": cLQd11CacRoamVoiceCallsInProg,
       "cLQd11CacTotalVoiceCallsAP": cLQd11CacTotalVoiceCallsAP,
       "cLQd11CacTotalRoamCallsAP": cLQd11CacTotalRoamCallsAP,
       "cLQd11CacVoiceCallsRejectedAP": cLQd11CacVoiceCallsRejectedAP,
       "cLQd11CacRoamCallsRejectedAP": cLQd11CacRoamCallsRejectedAP,
       "cLQd11CacRejCallsInsufBw": cLQd11CacRejCallsInsufBw,
       "cLQd11CacRejCallsBadParams": cLQd11CacRejCallsBadParams,
       "cLQd11CacRejCallsPhyRate": cLQd11CacRejCallsPhyRate,
       "cLQd11CacRejCallsQosPolicy": cLQd11CacRejCallsQosPolicy,
       "cLQd11SipCacNonRoamCallsInProgress": cLQd11SipCacNonRoamCallsInProgress,
       "cLQd11SipCacRoamCallsInProg": cLQd11SipCacRoamCallsInProg,
       "cLQd11SipCacTotalNonRoamCallsAP": cLQd11SipCacTotalNonRoamCallsAP,
       "cLQd11SipCacTotalRoamCallsAP": cLQd11SipCacTotalRoamCallsAP,
       "cLQd11SipCacNonRoamCallsRejectedInSuffBw": cLQd11SipCacNonRoamCallsRejectedInSuffBw,
       "cLQd11SipCacRoamCallsRejectedInSuffBw": cLQd11SipCacRoamCallsRejectedInSuffBw,
       "cLQd11SipCacNonRoamCallsRejectedMaxLimit": cLQd11SipCacNonRoamCallsRejectedMaxLimit,
       "cLQd11SipCacRoamCallsRejectedMaxLimit": cLQd11SipCacRoamCallsRejectedMaxLimit,
       "cLQd11SipCacRejCallsQosPolicy": cLQd11SipCacRejCallsQosPolicy,
       "cLQd11SipCacPreferredCallsReceived": cLQd11SipCacPreferredCallsReceived,
       "cLQd11SipCacPreferredCallsAccepted": cLQd11SipCacPreferredCallsAccepted,
       "cLQd11KtsCacNonRoamCallsInProgress": cLQd11KtsCacNonRoamCallsInProgress,
       "cLQd11KtsCacRoamCallsInProg": cLQd11KtsCacRoamCallsInProg,
       "cLQd11KtsCacTotalNonRoamCallsAP": cLQd11KtsCacTotalNonRoamCallsAP,
       "cLQd11KtsCacTotalRoamCallsAP": cLQd11KtsCacTotalRoamCallsAP,
       "cLQd11KtsCacNonRoamCallsRejectedInSuffBw": cLQd11KtsCacNonRoamCallsRejectedInSuffBw,
       "cLQd11KtsCacRoamCallsRejectedInSuffBw": cLQd11KtsCacRoamCallsRejectedInSuffBw,
       "cLQd11CacVideoRoamBwInUse": cLQd11CacVideoRoamBwInUse,
       "cLQd11CacVideoTotalBwInUse": cLQd11CacVideoTotalBwInUse,
       "cLQd11CacVideoCallsInProgress": cLQd11CacVideoCallsInProgress,
       "cLQd11CacVideoRoamCallsInProg": cLQd11CacVideoRoamCallsInProg,
       "cLQd11CacVideoTotalCallsAP": cLQd11CacVideoTotalCallsAP,
       "cLQd11CacVideoTotalRoamCallsAP": cLQd11CacVideoTotalRoamCallsAP,
       "cLQd11CacVideoCallsRejectedAP": cLQd11CacVideoCallsRejectedAP,
       "cLQd11CacVideoRoamCallsRejectedAP": cLQd11CacVideoRoamCallsRejectedAP,
       "cLQd11CacVideoRejCallsInsufBw": cLQd11CacVideoRejCallsInsufBw,
       "cLQd11CacVideoRejCallsBadParams": cLQd11CacVideoRejCallsBadParams,
       "cLQd11CacVideoRejCallsPhyRate": cLQd11CacVideoRejCallsPhyRate,
       "cLQd11CacVideoRejCallsQosPolicy": cLQd11CacVideoRejCallsQosPolicy,
       "cLQd11SipCacVideoCallsInProgress": cLQd11SipCacVideoCallsInProgress,
       "cLQd11SipCacVideoRoamCallsInProg": cLQd11SipCacVideoRoamCallsInProg,
       "cLQd11SipCacVideoTotalCallsAP": cLQd11SipCacVideoTotalCallsAP,
       "cLQd11SipCacVideoTotalRoamCallsAP": cLQd11SipCacVideoTotalRoamCallsAP,
       "cLQd11SipCacVideoCallsRejectedInSuffBw": cLQd11SipCacVideoCallsRejectedInSuffBw,
       "cLQd11SipCacVideoRoamCallsRejectedInSuffBw": cLQd11SipCacVideoRoamCallsRejectedInSuffBw,
       "cLQEntConfConfig": cLQEntConfConfig,
       "cLQd11VoiceStats": cLQd11VoiceStats,
       "cLQd11VoiceStatsTable": cLQd11VoiceStatsTable,
       "cLQd11VoiceStatsEntry": cLQd11VoiceStatsEntry,
       "cLQd11VoiceCallCounts": cLQd11VoiceCallCounts,
       "cLQd11CacVoiceCallTimePeriod": cLQd11CacVoiceCallTimePeriod,
       "cLQVoiceWlanConfig": cLQVoiceWlanConfig,
       "cLQVoiceWlanConfigTable": cLQVoiceWlanConfigTable,
       "cLQVoiceWlanConfigEntry": cLQVoiceWlanConfigEntry,
       "cLQVoiceWlanConfigDetectVoipCallFailure": cLQVoiceWlanConfigDetectVoipCallFailure,
       "cLQVoiceClient": cLQVoiceClient,
       "cLQVoiceClientTable": cLQVoiceClientTable,
       "cLQVoiceClientEntry": cLQVoiceClientEntry,
       "cLQVoiceClientCallingNumber": cLQVoiceClientCallingNumber,
       "cLQVoiceClientLastCalledNumber": cLQVoiceClientLastCalledNumber,
       "cLQVoiceClientLastCallFailureReasonCode": cLQVoiceClientLastCallFailureReasonCode,
       "cLQd11SipCacConfig": cLQd11SipCacConfig,
       "cLQd11SipCacConfigTable": cLQd11SipCacConfigTable,
       "cLQd11SipCacConfigEntry": cLQd11SipCacConfigEntry,
       "cLQd11SipCacConfigCodecType": cLQd11SipCacConfigCodecType,
       "cLQd11SipCacConfigBw": cLQd11SipCacConfigBw,
       "cLQd11SipCacConfigVoiceSampleSize": cLQd11SipCacConfigVoiceSampleSize,
       "cLQd11SipCacMaxPossibleVoiceCalls": cLQd11SipCacMaxPossibleVoiceCalls,
       "cLQd11SipCacMaxPossibleReservedRoamingCalls": cLQd11SipCacMaxPossibleReservedRoamingCalls,
       "cLQConfigObjects": cLQConfigObjects,
       "ciscoLwappVoipCallFailureNotifEnabled": ciscoLwappVoipCallFailureNotifEnabled,
       "ciscoLwappKtsVoipCallFailureNotifEnabled": ciscoLwappKtsVoipCallFailureNotifEnabled,
       "cLQMediaClient": cLQMediaClient,
       "cLQMediaClientTable": cLQMediaClientTable,
       "cLQMediaClientEntry": cLQMediaClientEntry,
       "cLQVMediaClientDestIpAddrType": cLQVMediaClientDestIpAddrType,
       "cLQVMediaClientDestIpAddr": cLQVMediaClientDestIpAddr,
       "cLQVMediaClientSrcIpAddrType": cLQVMediaClientSrcIpAddrType,
       "cLQVMediaClientSrcIpAddr": cLQVMediaClientSrcIpAddr,
       "cLQVMediaClientApMacAddress": cLQVMediaClientApMacAddress,
       "cLQVMediaClientWlanIndex": cLQVMediaClientWlanIndex,
       "cLQVMediaClientRadioType": cLQVMediaClientRadioType,
       "cLQVMediaClientQos": cLQVMediaClientQos,
       "cLQVMediaClientDecision": cLQVMediaClientDecision,
       "cLQMediaClientHistoryTable": cLQMediaClientHistoryTable,
       "cLQMediaClientHistoryEntry": cLQMediaClientHistoryEntry,
       "cLQVMediaClientHistTimeStamp": cLQVMediaClientHistTimeStamp,
       "cLQVMediaClientHistClientMacAddress": cLQVMediaClientHistClientMacAddress,
       "cLQVMediaClientHistApMacAddress": cLQVMediaClientHistApMacAddress,
       "cLQVMediaClientHistSlotId": cLQVMediaClientHistSlotId,
       "cLQVMediaClientHistSrcIpAddr": cLQVMediaClientHistSrcIpAddr,
       "cLQVMediaClientHistDestIpAddr": cLQVMediaClientHistDestIpAddr,
       "cLQVMediaClientHistDecision": cLQVMediaClientHistDecision,
       "cLQVMediaClientHistLastFailureReasonCode": cLQVMediaClientHistLastFailureReasonCode,
       "cLQVMediaClientHistWlanIndex": cLQVMediaClientHistWlanIndex,
       "cLQVMediaClientHistRadioType": cLQVMediaClientHistRadioType,
       "cLQVMediaClientHistQos": cLQVMediaClientHistQos,
       "cLQVMediaClientHistCfgBw": cLQVMediaClientHistCfgBw,
       "cLQVMediaClientHistCurrentRate": cLQVMediaClientHistCurrentRate,
       "cLQVMediaClientHistVideoPktSize": cLQVMediaClientHistVideoPktSize,
       "cLQVMediaClientHistVideoUtil": cLQVMediaClientHistVideoUtil,
       "cLQVMediaClientHistVoiceUtil": cLQVMediaClientHistVoiceUtil,
       "cLQVMediaClientHistChannelUtil": cLQVMediaClientHistChannelUtil,
       "cLQVMediaClientHistQueueUtil": cLQVMediaClientHistQueueUtil,
       "cLQVMediaClientHistVideoPps": cLQVMediaClientHistVideoPps,
       "cLQVMediaClientHistVideoDelay": cLQVMediaClientHistVideoDelay,
       "cLQVMediaClientHistPktLossDiscard": cLQVMediaClientHistPktLossDiscard,
       "cLQVMediaClientHistPktLossFail": cLQVMediaClientHistPktLossFail,
       "cLQVMediaClientHistNumVideoStreams": cLQVMediaClientHistNumVideoStreams,
       "cLQVMediaClientHistCacEnable": cLQVMediaClientHistCacEnable,
       "cLQVMediaClientHistStreamName": cLQVMediaClientHistStreamName,
       "cLQVMediaClientHistSrcInetAddrType": cLQVMediaClientHistSrcInetAddrType,
       "cLQVMediaClientHistSrcInetAddr": cLQVMediaClientHistSrcInetAddr,
       "cLQVMediaClientHistDestInetAddrType": cLQVMediaClientHistDestInetAddrType,
       "cLQVMediaClientHistDestInetAddr": cLQVMediaClientHistDestInetAddr,
       "cLQMediaMulticastClientTable": cLQMediaMulticastClientTable,
       "cLQMediaMulticastClientEntry": cLQMediaMulticastClientEntry,
       "cLQVMediaClientMCGrpIpAddrType": cLQVMediaClientMCGrpIpAddrType,
       "cLQVMediaClientMCGrpIpAddr": cLQVMediaClientMCGrpIpAddr,
       "cLQVMediaClientVlanId": cLQVMediaClientVlanId,
       "cLQVMediaMCClientApName": cLQVMediaMCClientApName,
       "cLQVMediaClientMCUCStatus": cLQVMediaClientMCUCStatus,
       "cLQMediaStreamConfig": cLQMediaStreamConfig,
       "cLQMStreamTable": cLQMStreamTable,
       "cLQMStreamEntry": cLQMStreamEntry,
       "cLQMStreamName": cLQMStreamName,
       "cLQMStreamRowStatus": cLQMStreamRowStatus,
       "cLQMStreamDestIPStartAddr": cLQMStreamDestIPStartAddr,
       "cLQMStreamDestIPEndAddr": cLQMStreamDestIPEndAddr,
       "cLQMStreamstate": cLQMStreamstate,
       "cLQMStreamRrcExpBw": cLQMStreamRrcExpBw,
       "cLQMStreamRrcAvgPkt": cLQMStreamRrcAvgPkt,
       "cLQMStreamReRrc": cLQMStreamReRrc,
       "cLQMStreamRrcQos": cLQMStreamRrcQos,
       "cLQMStreamRrcType": cLQMStreamRrcType,
       "cLQMStreamRrcPriority": cLQMStreamRrcPriority,
       "cLQMStreamRrcViolation": cLQMStreamRrcViolation,
       "cLQMStreamRrcPolicy": cLQMStreamRrcPolicy,
       "cLQMStreamDestStartInetAddrType": cLQMStreamDestStartInetAddrType,
       "cLQMStreamDestStartInetAddr": cLQMStreamDestStartInetAddr,
       "cLQMStreamDestEndInetAddrType": cLQMStreamDestEndInetAddrType,
       "cLQMStreamDestEndInetAddr": cLQMStreamDestEndInetAddr,
       "cLQMStreamSdpConfig": cLQMStreamSdpConfig,
       "cLQMStreamSdpUrl": cLQMStreamSdpUrl,
       "cLQMStreamSdpEmail": cLQMStreamSdpEmail,
       "cLQMStreamSdpPhone": cLQMStreamSdpPhone,
       "cLQMStreamSdpNote": cLQMStreamSdpNote,
       "cLQMStreamSdpStatus": cLQMStreamSdpStatus,
       "cLQMStreamRrcGlobal": cLQMStreamRrcGlobal,
       "cLQMStreamRrcGlobalState": cLQMStreamRrcGlobalState,
       "cLQPreferredCallConfig": cLQPreferredCallConfig,
       "cLQPreferredCallTable": cLQPreferredCallTable,
       "cLQPreferredCallEntry": cLQPreferredCallEntry,
       "cLQPreferredCallIndex": cLQPreferredCallIndex,
       "cLQPreferredCallNumber": cLQPreferredCallNumber,
       "cLQPreferredCallRowStatus": cLQPreferredCallRowStatus,
       "cLQoSProfileConfig": cLQoSProfileConfig,
       "cLQoSProfileTable": cLQoSProfileTable,
       "cLQoSProfileEntry": cLQoSProfileEntry,
       "cLQoSProfileName": cLQoSProfileName,
       "cLQoSMaximumPriority": cLQoSMaximumPriority,
       "cLQoSUnicastDefPriority": cLQoSUnicastDefPriority,
       "cLQoSMulticastDefPriority": cLQoSMulticastDefPriority,
       "cLQoSClientDSAverageDataRate": cLQoSClientDSAverageDataRate,
       "cLQoSClientUSAverageDataRate": cLQoSClientUSAverageDataRate,
       "cLQoSClientDSBurstDataRate": cLQoSClientDSBurstDataRate,
       "cLQoSClientUSBurstDataRate": cLQoSClientUSBurstDataRate,
       "cLQoSClientDSAvgRealTimeDataRate": cLQoSClientDSAvgRealTimeDataRate,
       "cLQoSClientUSAvgRealTimeDataRate": cLQoSClientUSAvgRealTimeDataRate,
       "cLQoSClientDSBurstRealTimeDataRate": cLQoSClientDSBurstRealTimeDataRate,
       "cLQoSClientUSBurstRealTimeDataRate": cLQoSClientUSBurstRealTimeDataRate,
       "cLQoSSsidDSAverageDataRate": cLQoSSsidDSAverageDataRate,
       "cLQoSSsidUSAverageDataRate": cLQoSSsidUSAverageDataRate,
       "cLQoSSsidDSBurstDataRate": cLQoSSsidDSBurstDataRate,
       "cLQoSSsidUSBurstDataRate": cLQoSSsidUSBurstDataRate,
       "cLQoSSsidDSAvgRealTimeDataRate": cLQoSSsidDSAvgRealTimeDataRate,
       "cLQoSSsidUSAvgRealTimeDataRate": cLQoSSsidUSAvgRealTimeDataRate,
       "cLQoSSsidDSBurstRealTimeDataRate": cLQoSSsidDSBurstRealTimeDataRate,
       "cLQoSSsidUSBurstRealTimeDataRate": cLQoSSsidUSBurstRealTimeDataRate,
       "cLQoSWlanDSAverageDataRate": cLQoSWlanDSAverageDataRate,
       "cLQoSWlanUSAverageDataRate": cLQoSWlanUSAverageDataRate,
       "cLQoSWlanDSBurstDataRate": cLQoSWlanDSBurstDataRate,
       "cLQoSWlanUSBurstDataRate": cLQoSWlanUSBurstDataRate,
       "cLQoSWlanDSAvgRealTimeDataRate": cLQoSWlanDSAvgRealTimeDataRate,
       "cLQoSWlanUSAvgRealTimeDataRate": cLQoSWlanUSAvgRealTimeDataRate,
       "cLQoSWlanDSBurstRealTimeDataRate": cLQoSWlanDSBurstRealTimeDataRate,
       "cLQoSWlanUSBurstRealTimeDataRate": cLQoSWlanUSBurstRealTimeDataRate,
       "cLQoSSipSnoopingConfig": cLQoSSipSnoopingConfig,
       "cLQoSSipSnoopingPortRangeStart": cLQoSSipSnoopingPortRangeStart,
       "cLQoSSipSnoopingPortRangeEnd": cLQoSSipSnoopingPortRangeEnd,
       "cLQoSAirTimeFairness": cLQoSAirTimeFairness,
       "cLQoSGlobalAirTimeFairnessTable": cLQoSGlobalAirTimeFairnessTable,
       "cLQoSGlobalAirTimeFairnessEntry": cLQoSGlobalAirTimeFairnessEntry,
       "cLGlobalAirTimeFairnessMode": cLGlobalAirTimeFairnessMode,
       "cLGlobalAirTimeFairnessOptimizationPolicy": cLGlobalAirTimeFairnessOptimizationPolicy,
       "cLQoSAirTimeFairnessTable": cLQoSAirTimeFairnessTable,
       "cLQoSAirTimeFairnessEntry": cLQoSAirTimeFairnessEntry,
       "cLApAirTimeFairnessMode": cLApAirTimeFairnessMode,
       "cLApAirTimeFairnessOptimizationPolicy": cLApAirTimeFairnessOptimizationPolicy,
       "cLQoSAirTimeFairnessWlanStatisticsTable": cLQoSAirTimeFairnessWlanStatisticsTable,
       "cLQoSAirTimeFairnessWlanStatisticsEntry": cLQoSAirTimeFairnessWlanStatisticsEntry,
       "cLApAirTimeFairnessWlanAirtimeUsedInstantaneous": cLApAirTimeFairnessWlanAirtimeUsedInstantaneous,
       "cLApAirTimeFairnessWlanAirtimeUsedCumulative": cLApAirTimeFairnessWlanAirtimeUsedCumulative,
       "cLApAirTimeFairnessWlanBytesSentInstantaneous": cLApAirTimeFairnessWlanBytesSentInstantaneous,
       "cLApAirTimeFairnessWlanBytesSentCumulative": cLApAirTimeFairnessWlanBytesSentCumulative,
       "cLApAirTimeFairnessWlanBytesDroppedInstantaneous": cLApAirTimeFairnessWlanBytesDroppedInstantaneous,
       "cLApAirTimeFairnessWlanBytesDroppedCumulative": cLApAirTimeFairnessWlanBytesDroppedCumulative,
       "cLApAirTimeFairnessWlanFramesSentInstantaneous": cLApAirTimeFairnessWlanFramesSentInstantaneous,
       "cLApAirTimeFairnessWlanFramesSentCumulative": cLApAirTimeFairnessWlanFramesSentCumulative,
       "cLApAirTimeFairnessWlanFramesDroppedInstantaneous": cLApAirTimeFairnessWlanFramesDroppedInstantaneous,
       "cLApAirTimeFairnessWlanFramesDroppedCumulative": cLApAirTimeFairnessWlanFramesDroppedCumulative,
       "cLQoSAirTimeFairnessStatisticsTable": cLQoSAirTimeFairnessStatisticsTable,
       "cLQoSAirTimeFairnessStatisticsEntry": cLQoSAirTimeFairnessStatisticsEntry,
       "cLApAirTimeFairnessTotalAirtimeUsedInstantaneous": cLApAirTimeFairnessTotalAirtimeUsedInstantaneous,
       "cLApAirTimeFairnessTotalAirtimeUsedCumulative": cLApAirTimeFairnessTotalAirtimeUsedCumulative,
       "cLApAirTimeFairnessRadioUptime": cLApAirTimeFairnessRadioUptime,
       "cLApAirTimeFairnessRadioUptimeCumulative": cLApAirTimeFairnessRadioUptimeCumulative,
       "cLAPGroupAirTimeFairnessTable": cLAPGroupAirTimeFairnessTable,
       "cLAPGroupAirTimeFairnessEntry": cLAPGroupAirTimeFairnessEntry,
       "cLAPGroupAirTimeFairnessMode": cLAPGroupAirTimeFairnessMode,
       "cLAPGroupAirTimeFairnessOptimizationPolicy": cLAPGroupAirTimeFairnessOptimizationPolicy,
       "cLQosAirTimeFairnessPolicyConfigTable": cLQosAirTimeFairnessPolicyConfigTable,
       "cLQosAirTimeFairnessPolicyConfigEntry": cLQosAirTimeFairnessPolicyConfigEntry,
       "cLAirTimeFairnessPolicyId": cLAirTimeFairnessPolicyId,
       "cLAirTimeFairnessPolicyRowStatus": cLAirTimeFairnessPolicyRowStatus,
       "cLAirTimeFairnessPolicyName": cLAirTimeFairnessPolicyName,
       "cLAirTimeFairnessPolicyWeight": cLAirTimeFairnessPolicyWeight,
       "cLAirTimeFairnessPolicyclientfairsharing": cLAirTimeFairnessPolicyclientfairsharing,
       "cLApAirTimeFairnessPolicyOverrideTable": cLApAirTimeFairnessPolicyOverrideTable,
       "cLApAirTimeFairnessPolicyOverrideEntry": cLApAirTimeFairnessPolicyOverrideEntry,
       "cLApAirTimeFairnessPolicyOverride": cLApAirTimeFairnessPolicyOverride,
       "cLApAirTimeFairnessOverridePolicyName": cLApAirTimeFairnessOverridePolicyName,
       "cLAPGroupsAirTimeFairnessPolicyOverrideTable": cLAPGroupsAirTimeFairnessPolicyOverrideTable,
       "cLAPGroupsAirTimeFairnessPolicyOverrideEntry": cLAPGroupsAirTimeFairnessPolicyOverrideEntry,
       "cLAPGroupAirTimeFairnessPolicyNameOverrideEnabled": cLAPGroupAirTimeFairnessPolicyNameOverrideEnabled,
       "cLAPGroupAirTimeFairnessOverridePolicyName": cLAPGroupAirTimeFairnessOverridePolicyName,
       "cLQoSAirTimeFairnessClientStatisticsTable": cLQoSAirTimeFairnessClientStatisticsTable,
       "cLQoSAirTimeFairnessClientStatisticsEntry": cLQoSAirTimeFairnessClientStatisticsEntry,
       "cLApAirTimeFairnessClientAirtimeUsedInstantaneous": cLApAirTimeFairnessClientAirtimeUsedInstantaneous,
       "cLApAirTimeFairnessClientAirtimeUsedCumulative": cLApAirTimeFairnessClientAirtimeUsedCumulative,
       "cLApAirTimeFairnessClientFramesSent": cLApAirTimeFairnessClientFramesSent,
       "cLApAirTimeFairnessClientFramesDropped": cLApAirTimeFairnessClientFramesDropped,
       "cLApAirTimeFairnessClientUsage": cLApAirTimeFairnessClientUsage,
       "cLQoSMapConfig": cLQoSMapConfig,
       "cLQosMapStatus": cLQosMapStatus,
       "cLQoSMapUpRangesTable": cLQoSMapUpRangesTable,
       "cLQoSUpTableEntry": cLQoSUpTableEntry,
       "cLQoSUpTableIndex": cLQoSUpTableIndex,
       "cLQoSMapUp": cLQoSMapUp,
       "cLQoSMapDscpDefault": cLQoSMapDscpDefault,
       "cLQoSMapDscpLow": cLQoSMapDscpLow,
       "cLQoSMapDscpHigh": cLQoSMapDscpHigh,
       "cLQoSMapUpExceptionsTable": cLQoSMapUpExceptionsTable,
       "cLQoSUpExceptionsTableEntry": cLQoSUpExceptionsTableEntry,
       "cLQoSMapExceptionNumber": cLQoSMapExceptionNumber,
       "cLQoSMapExceptionUp": cLQoSMapExceptionUp,
       "cLQoSMapExceptionDscp": cLQoSMapExceptionDscp,
       "cLQosMapExceptionsRowStatus": cLQosMapExceptionsRowStatus,
       "cLQosCopyClientDscpStatus": cLQosCopyClientDscpStatus,
       "cLQosMapExceptionsClearAll": cLQosMapExceptionsClearAll,
       "cLQosMapDefault": cLQosMapDefault,
       "cLQoSFastlaneConfig": cLQoSFastlaneConfig,
       "cLQosFastlaneDisable": cLQosFastlaneDisable,
       "ciscoLwappQosMIBTableObjects": ciscoLwappQosMIBTableObjects,
       "cLQoSMapDownstreamDscpTable": cLQoSMapDownstreamDscpTable,
       "cLQoSMapDownstreamDscpEntry": cLQoSMapDownstreamDscpEntry,
       "cLQoSMapDownstreamDscpIndex": cLQoSMapDownstreamDscpIndex,
       "cLQoSMapDownstreamDscpLow": cLQoSMapDownstreamDscpLow,
       "cLQoSMapDownstreamDscpHigh": cLQoSMapDownstreamDscpHigh,
       "cLQoSMapDownstreamUp": cLQoSMapDownstreamUp,
       "cLQoSMapDownstreamUpExceptionsTable": cLQoSMapDownstreamUpExceptionsTable,
       "cLQoSDownstreamUpExceptionsTableEntry": cLQoSDownstreamUpExceptionsTableEntry,
       "cLQoSMapDownstreamExceptionNumber": cLQoSMapDownstreamExceptionNumber,
       "cLQoSMapDownstreamExceptionDscp": cLQoSMapDownstreamExceptionDscp,
       "cLQoSMapDownstreamExceptionUp": cLQoSMapDownstreamExceptionUp,
       "cLQosMapDownstreamExceptionsRowStatus": cLQosMapDownstreamExceptionsRowStatus,
       "cLQoSMapUpstreamUpDscpTable": cLQoSMapUpstreamUpDscpTable,
       "cLQoSMapUpstreamUpDscpEntry": cLQoSMapUpstreamUpDscpEntry,
       "cLQoSMapUpstreamDscpIndex": cLQoSMapUpstreamDscpIndex,
       "cLQoSMapUpstreamUp": cLQoSMapUpstreamUp,
       "cLQoSMapUpstreamDscp": cLQoSMapUpstreamDscp,
       "ciscoLwappQosMIBGlobalObjects": ciscoLwappQosMIBGlobalObjects,
       "cLQosUpstreamCopyClientDscpStatus": cLQosUpstreamCopyClientDscpStatus,
       "ciscoLwappQosMIBConform": ciscoLwappQosMIBConform,
       "ciscoLwappQosMIBCompliances": ciscoLwappQosMIBCompliances,
       "ciscoLwappQosMIBCompliance": ciscoLwappQosMIBCompliance,
       "ciscoLwappQosMIBComplianceRev1": ciscoLwappQosMIBComplianceRev1,
       "ciscoLwappQosMIBComplianceRev2": ciscoLwappQosMIBComplianceRev2,
       "ciscoLwappQosMIBComplianceRev3": ciscoLwappQosMIBComplianceRev3,
       "ciscoLwappQosMIBComplianceRev4": ciscoLwappQosMIBComplianceRev4,
       "ciscoLwappQosMIBGroups": ciscoLwappQosMIBGroups,
       "ciscoLwappQosDot11aConfigGroup": ciscoLwappQosDot11aConfigGroup,
       "ciscoLwappQosDot11bConfigGroup": ciscoLwappQosDot11bConfigGroup,
       "ciscoLwappQosDot11WlanConfigGroup": ciscoLwappQosDot11WlanConfigGroup,
       "ciscoLwappQosDot11CacStatsGroup": ciscoLwappQosDot11CacStatsGroup,
       "ciscoLwappQosDot11aConfigGroupSup1": ciscoLwappQosDot11aConfigGroupSup1,
       "ciscoLwappQosDot11bConfigGroupSup1": ciscoLwappQosDot11bConfigGroupSup1,
       "ciscoLwappQosDot11aConfigGroupSup2": ciscoLwappQosDot11aConfigGroupSup2,
       "ciscoLwappQosDot11bConfigGroupSup2": ciscoLwappQosDot11bConfigGroupSup2,
       "ciscoLwappQosDot11SipCacStatsGroup": ciscoLwappQosDot11SipCacStatsGroup,
       "ciscoLwappQosDot11SipConfigGroup": ciscoLwappQosDot11SipConfigGroup,
       "ciscoLwappQosDot11VoiceStatsGroup": ciscoLwappQosDot11VoiceStatsGroup,
       "ciscoLwappQosDot11VoiceConfigGroup": ciscoLwappQosDot11VoiceConfigGroup,
       "ciscoLwappQosDot11VoiceNotifGroup": ciscoLwappQosDot11VoiceNotifGroup,
       "ciscoLwappQosConfigGroup": ciscoLwappQosConfigGroup,
       "ciscoLwappQosDot11VoiceNotifGroupSup1": ciscoLwappQosDot11VoiceNotifGroupSup1,
       "ciscoLwappQosConfigGroupSup1": ciscoLwappQosConfigGroupSup1,
       "cLQoSProfileGroup": cLQoSProfileGroup}
)
