# SNMP MIB module (KHOMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/khomp_32624/KHOMP-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 10:59:33 2025
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


# MODULE-IDENTITY

khomp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 32624)
)
if mibBuilder.loadTexts:
    khomp.setRevisions(
        ("2019-03-04 14:21",
         "2018-05-10 08:49",
         "2016-05-27 19:29",
         "2015-10-20 14:53",
         "2015-05-21 03:30",
         "2015-02-04 17:01",
         "2014-12-29 10:48",
         "2014-12-03 11:09",
         "2014-12-01 14:12",
         "2014-11-17 15:00",
         "2014-10-09 15:45",
         "2013-09-25 21:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class KhompSignaling(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("ksigInactive", 0),
          ("ksigR2Digital", 1),
          ("ksigContinuousEM", 2),
          ("ksigPulsedEM", 3),
          ("ksigUserR2Digital", 4),
          ("ksigAnalog", 5),
          ("ksigOpenCAS", 6),
          ("ksigOpenR2", 7),
          ("ksigSIP", 8),
          ("ksigOpenCCS", 9),
          ("ksigPRIEndPoint", 10),
          ("ksigAnalogTerminal", 11),
          ("ksigPRINetwork", 12),
          ("ksigPRIPassive", 13),
          ("ksigLineSide", 14),
          ("ksigCASEL7", 15),
          ("ksigGSM", 16),
          ("ksigE1LC", 17),
          ("ksigISUP", 18),
          ("ksigISUPPassive", 19),
          ("ksigInterconnection", 20))
    )



class KhompOperStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )



class KhompBoolean(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )



class KhompDeviceIndex(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 98),
    )



class KhompDeviceSerial(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(99, 16777215),
    )



class KhompUnsigned16(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class KhompDeviceType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("kdtE1", 0),
          ("kdtFXO", 1),
          ("kdtConf", 2),
          ("kdtPR", 3),
          ("kdtE1GW", 4),
          ("kdtFXOVoIP", 5),
          ("kdtE1IP", 6),
          ("kdtE1Spx", 7),
          ("kdtGWIP", 8),
          ("kdtFXS", 9),
          ("kdtFXSSpx", 10),
          ("kdtGSM", 11),
          ("kdtGSMSpx", 12),
          ("kdtE1AdHoc", 13),
          ("kdtGSMUSB", 14),
          ("kdtGSMUSBSpx", 15),
          ("kdtE1FXSSpx", 16),
          ("kdtVoIP", 17),
          ("kdtEBSE1", 18),
          ("kdtEBSFXO", 19),
          ("kdtEBSFXS", 20),
          ("kdtEBSGSM", 21),
          ("kdtEBSMod", 22),
          ("kdtEBSFXOHI", 23),
          ("kdtEBSE1HI", 24))
    )



class KhompDeviceChannelGroup(TextualConvention, Integer32):
    status = "current"
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
        *(("kdtE1", 0),
          ("kdtT1", 1),
          ("kdtFXO", 2),
          ("kdtFXS", 3),
          ("kdtGSM", 4))
    )



class KhompDeviceLinkIndex(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )



class KhompDeviceLinkAlarm(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("kesSignalLost", 0),
          ("kesNetworkAlarm", 1),
          ("kesFrameSyncLost", 2),
          ("kesMultiframeSyncLost", 3),
          ("kesRemoteAlarm", 4),
          ("kesHighErrorRate", 5),
          ("kesUnknownAlarm", 6),
          ("kesE1Error", 7))
    )


class KhompDeviceChannelIndex(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"


class KhompDeviceChannelCallStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("kcsFree", 0),
          ("kcsIncoming", 1),
          ("kcsOutgoing", 2),
          ("kcsFail", 4))
    )



class KhompDeviceChannelAudioStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ktoneSilence", 0),
          ("ktoneCallProgr", 1),
          ("ktoneInterception", 2),
          ("ktoneFax", 3),
          ("ktoneVoice", 4),
          ("ktoneCustom", 5))
    )



class KhompDeviceChannelFeatures(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("kcfDtmfSuppression", 0),
          ("kcfCallProgress", 1),
          ("kcfPulseDetection", 2),
          ("kcfAudioNotification", 3),
          ("kcfEchoCanceller", 4),
          ("kcfAutoGainControl", 5),
          ("kcfObsolete1", 6),
          ("kcfHighImpEvents", 7),
          ("kcfCallAnswerInfo", 8),
          ("kcfHMPToneDetection", 9),
          ("kcfPlayerAGC", 10),
          ("kcfHMPAnalytics", 11))
    )


class KhompDeviceE1ChannelStatus(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("kecsBusy", 0),
          ("kecsOutgoing", 1),
          ("kecsIncoming", 2),
          ("kecsLocked", 3),
          ("kecsOutgoingLock", 4),
          ("kecsLocalFail", 5),
          ("kecsIncomingLock", 6),
          ("kecsRemoteLock", 7))
    )


class KhompDeviceFxoChannelStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("kfcsDisabled", 0),
          ("kfcsEnabled", 1))
    )



class KhompDeviceFxsChannelStatus(TextualConvention, Integer32):
    status = "current"
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
        *(("kfxsOnHook", 0),
          ("kfxsOffHook", 1),
          ("kfxsRinging", 2),
          ("kfxsFail", 3))
    )



class KhompDeviceGsmChannelStatus(TextualConvention, Integer32):
    status = "current"
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
        *(("kgsmIdle", 0),
          ("kgsmCallInProgress", 1),
          ("kgsmSMSInProgress", 2),
          ("kgsmModemError", 3),
          ("kgsmSIMCardError", 4),
          ("kgsmNetworkError", 5),
          ("kgsmNotReady", 6))
    )



class KhompDeviceGsmChannelRegistryStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("kgrsNotRegistered", 0),
          ("kgrsRegistered", 1),
          ("kgrsSearching", 2),
          ("kgrsDenied", 3),
          ("kgrsUnknown", 4),
          ("kgrsRoaming", 5),
          ("kgrsInitializing", 255))
    )



class KhompDeviceGsmChannelEnabledFeatures(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("kgcfMultiparty", 0),
          ("kgcfCallForward", 1))
    )


class KhompDeviceGsmChannelCallWaitingState(TextualConvention, Integer32):
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
        *(("kgcwsDisabled", 0),
          ("kgcwsEnabled", 1),
          ("kgcwsUnknown", 2))
    )



class KhompDeviceGsmCallIndex(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )



class KhompDeviceGsmCallStatus(TextualConvention, Integer32):
    status = "current"
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
        *(("kgcstActive", 0),
          ("kgcstHeld", 1),
          ("kgcstDialing", 2),
          ("kgcstAlerting", 3),
          ("kgcstIncoming", 4),
          ("kgcstWaiting", 5),
          ("kgcstReleased", 6))
    )



class KhompDeviceGsmCallMode(TextualConvention, Integer32):
    status = "current"
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
        *(("kgcmVoice", 0),
          ("kgcmData", 1),
          ("kgcmFax", 2),
          ("kgcmUnknown", 3))
    )



class KhompDeviceGsmCallFlags(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("kgcflMultiparty", 0),
          ("kgcflInternationalNumber", 1),
          ("kgcflMobileTerminatedCall", 2))
    )


class KhompDeviceSipChannelStatus(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("kipcsOutgoingLock", 4),
          ("kipcsIncomingLock", 6))
    )


class KhompR2Country(TextualConvention, Integer32):
    status = "current"
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
        *(("brasil", 0),
          ("mexico", 1),
          ("argentina", 2),
          ("chile", 3),
          ("uruguai", 4),
          ("venezuela", 5),
          ("colombia", 6))
    )



class KhompLinkOperatingMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("t1", 0),
          ("e1", 1))
    )



class KhompLicenseSerial(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(99, 16777215),
    )



class KhompLicenseResourceType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("kLicVoipChannels", 0),
          ("kLicFaxChannels", 1),
          ("kLicIsupCircuits", 2),
          ("kLicG729Channels", 3),
          ("kLicGatewayEnable", 4),
          ("kLicGatewayLinks", 5),
          ("kLicGatewayGSMChannels", 6),
          ("kLicPlayChannels", 7),
          ("kLicRecordChannels", 8),
          ("kLicEnableHmpAnalytics", 9),
          ("kLicEnableHmpAnalyticsTrunk0", 10),
          ("kLicEnableHmpAnalyticsTrunk1", 11),
          ("kLicEnableHmpAnalyticsTrunk2", 12),
          ("kLicEnableHmpAnalyticsTrunk3", 13),
          ("kLicVoipRecordingChannels", 14),
          ("kLicGatewayAnalytics", 15),
          ("kLicGatewayVoipCalls", 16),
          ("kLicGatewayAnalyticsVoipCalls", 17),
          ("kLicInterconnectionChannels", 18),
          ("kLicMTP2Links", 19),
          ("kLicGatewaySimultaneousCalls", 20))
    )



# MIB Managed Objects in the order of their OIDs

_Legacy_ObjectIdentity = ObjectIdentity
legacy = _Legacy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32624, 1)
)
_K3l_ObjectIdentity = ObjectIdentity
k3l = _K3l_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32624, 2)
)
_K3lMIBObjects_ObjectIdentity = ObjectIdentity
k3lMIBObjects = _K3lMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1)
)
_K3lVersion_ObjectIdentity = ObjectIdentity
k3lVersion = _K3lVersion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 1)
)
_K3lVersionMajor_Type = Unsigned32
_K3lVersionMajor_Object = MibScalar
k3lVersionMajor = _K3lVersionMajor_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 1, 1),
    _K3lVersionMajor_Type()
)
k3lVersionMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lVersionMajor.setStatus("current")
_K3lVersionMinor_Type = Unsigned32
_K3lVersionMinor_Object = MibScalar
k3lVersionMinor = _K3lVersionMinor_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 1, 2),
    _K3lVersionMinor_Type()
)
k3lVersionMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lVersionMinor.setStatus("current")
_K3lVersionBuild_Type = Unsigned32
_K3lVersionBuild_Object = MibScalar
k3lVersionBuild = _K3lVersionBuild_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 1, 3),
    _K3lVersionBuild_Type()
)
k3lVersionBuild.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lVersionBuild.setStatus("current")
_K3lVersionRevision_Type = Unsigned32
_K3lVersionRevision_Object = MibScalar
k3lVersionRevision = _K3lVersionRevision_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 1, 4),
    _K3lVersionRevision_Type()
)
k3lVersionRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lVersionRevision.setStatus("current")
_K3lVersionString_Type = DisplayString
_K3lVersionString_Object = MibScalar
k3lVersionString = _K3lVersionString_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 1, 5),
    _K3lVersionString_Type()
)
k3lVersionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lVersionString.setStatus("current")
_K3lDevice_ObjectIdentity = ObjectIdentity
k3lDevice = _K3lDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2)
)
_K3lDeviceCount_Type = Gauge32
_K3lDeviceCount_Object = MibScalar
k3lDeviceCount = _K3lDeviceCount_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 1),
    _K3lDeviceCount_Type()
)
k3lDeviceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceCount.setStatus("current")
_K3lDeviceTable_Object = MibTable
k3lDeviceTable = _K3lDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    k3lDeviceTable.setStatus("current")
_K3lDeviceEntry_Object = MibTableRow
k3lDeviceEntry = _K3lDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 2, 1)
)
k3lDeviceEntry.setIndexNames(
    (0, "KHOMP-MIB", "k3lDeviceSerial"),
)
if mibBuilder.loadTexts:
    k3lDeviceEntry.setStatus("current")
_K3lDeviceSerial_Type = KhompDeviceSerial
_K3lDeviceSerial_Object = MibTableColumn
k3lDeviceSerial = _K3lDeviceSerial_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 2, 1, 1),
    _K3lDeviceSerial_Type()
)
k3lDeviceSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceSerial.setStatus("current")
_K3lDeviceIndex_Type = KhompDeviceIndex
_K3lDeviceIndex_Object = MibTableColumn
k3lDeviceIndex = _K3lDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 2, 1, 2),
    _K3lDeviceIndex_Type()
)
k3lDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceIndex.setStatus("current")
_K3lDeviceDescr_Type = DisplayString
_K3lDeviceDescr_Object = MibTableColumn
k3lDeviceDescr = _K3lDeviceDescr_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 2, 1, 3),
    _K3lDeviceDescr_Type()
)
k3lDeviceDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceDescr.setStatus("current")
_K3lDeviceOperStatus_Type = KhompOperStatus
_K3lDeviceOperStatus_Object = MibTableColumn
k3lDeviceOperStatus = _K3lDeviceOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 2, 1, 4),
    _K3lDeviceOperStatus_Type()
)
k3lDeviceOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceOperStatus.setStatus("current")
_K3lDeviceType_Type = KhompDeviceType
_K3lDeviceType_Object = MibTableColumn
k3lDeviceType = _K3lDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 2, 1, 5),
    _K3lDeviceType_Type()
)
k3lDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceType.setStatus("current")
_K3lDeviceModel_Type = Unsigned32
_K3lDeviceModel_Object = MibTableColumn
k3lDeviceModel = _K3lDeviceModel_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 2, 1, 6),
    _K3lDeviceModel_Type()
)
k3lDeviceModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceModel.setStatus("current")
_K3lDeviceLinkCount_Type = Unsigned32
_K3lDeviceLinkCount_Object = MibTableColumn
k3lDeviceLinkCount = _K3lDeviceLinkCount_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 2, 1, 7),
    _K3lDeviceLinkCount_Type()
)
k3lDeviceLinkCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceLinkCount.setStatus("current")
_K3lDeviceChannelCount_Type = Unsigned32
_K3lDeviceChannelCount_Object = MibTableColumn
k3lDeviceChannelCount = _K3lDeviceChannelCount_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 2, 1, 8),
    _K3lDeviceChannelCount_Type()
)
k3lDeviceChannelCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceChannelCount.setStatus("current")
_K3lDeviceChannelCountEnabled_Type = Gauge32
_K3lDeviceChannelCountEnabled_Object = MibTableColumn
k3lDeviceChannelCountEnabled = _K3lDeviceChannelCountEnabled_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 2, 1, 9),
    _K3lDeviceChannelCountEnabled_Type()
)
k3lDeviceChannelCountEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceChannelCountEnabled.setStatus("current")
_K3lDeviceChannelCountIdle_Type = Gauge32
_K3lDeviceChannelCountIdle_Object = MibTableColumn
k3lDeviceChannelCountIdle = _K3lDeviceChannelCountIdle_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 2, 1, 10),
    _K3lDeviceChannelCountIdle_Type()
)
k3lDeviceChannelCountIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceChannelCountIdle.setStatus("current")
_K3lDeviceChannelCountFail_Type = Gauge32
_K3lDeviceChannelCountFail_Object = MibTableColumn
k3lDeviceChannelCountFail = _K3lDeviceChannelCountFail_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 2, 1, 11),
    _K3lDeviceChannelCountFail_Type()
)
k3lDeviceChannelCountFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceChannelCountFail.setStatus("current")
_K3lDeviceChannelCountBusy_Type = Gauge32
_K3lDeviceChannelCountBusy_Object = MibTableColumn
k3lDeviceChannelCountBusy = _K3lDeviceChannelCountBusy_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 2, 1, 12),
    _K3lDeviceChannelCountBusy_Type()
)
k3lDeviceChannelCountBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceChannelCountBusy.setStatus("current")
_K3lDeviceReset_Type = KhompBoolean
_K3lDeviceReset_Object = MibTableColumn
k3lDeviceReset = _K3lDeviceReset_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 2, 1, 13),
    _K3lDeviceReset_Type()
)
k3lDeviceReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    k3lDeviceReset.setStatus("current")
_K3lDeviceChannelGroupCount_Type = Unsigned32
_K3lDeviceChannelGroupCount_Object = MibTableColumn
k3lDeviceChannelGroupCount = _K3lDeviceChannelGroupCount_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 2, 1, 14),
    _K3lDeviceChannelGroupCount_Type()
)
k3lDeviceChannelGroupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceChannelGroupCount.setStatus("current")
_K3lDeviceStatsIncoming_Type = Counter32
_K3lDeviceStatsIncoming_Object = MibTableColumn
k3lDeviceStatsIncoming = _K3lDeviceStatsIncoming_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 2, 1, 15),
    _K3lDeviceStatsIncoming_Type()
)
k3lDeviceStatsIncoming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceStatsIncoming.setStatus("current")
_K3lDeviceStatsOutgoing_Type = Counter32
_K3lDeviceStatsOutgoing_Object = MibTableColumn
k3lDeviceStatsOutgoing = _K3lDeviceStatsOutgoing_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 2, 1, 16),
    _K3lDeviceStatsOutgoing_Type()
)
k3lDeviceStatsOutgoing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceStatsOutgoing.setStatus("current")
_K3lDeviceOutgoingCompleted_Type = Counter32
_K3lDeviceOutgoingCompleted_Object = MibTableColumn
k3lDeviceOutgoingCompleted = _K3lDeviceOutgoingCompleted_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 2, 1, 17),
    _K3lDeviceOutgoingCompleted_Type()
)
k3lDeviceOutgoingCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceOutgoingCompleted.setStatus("current")
_K3lDeviceOutgoingError_Type = Counter32
_K3lDeviceOutgoingError_Object = MibTableColumn
k3lDeviceOutgoingError = _K3lDeviceOutgoingError_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 2, 1, 18),
    _K3lDeviceOutgoingError_Type()
)
k3lDeviceOutgoingError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceOutgoingError.setStatus("current")
_K3lDeviceRemoteDisconnect_Type = Counter32
_K3lDeviceRemoteDisconnect_Object = MibTableColumn
k3lDeviceRemoteDisconnect = _K3lDeviceRemoteDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 2, 1, 19),
    _K3lDeviceRemoteDisconnect_Type()
)
k3lDeviceRemoteDisconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceRemoteDisconnect.setStatus("current")
_K3lDeviceLocalDisconnect_Type = Counter32
_K3lDeviceLocalDisconnect_Object = MibTableColumn
k3lDeviceLocalDisconnect = _K3lDeviceLocalDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 2, 1, 20),
    _K3lDeviceLocalDisconnect_Type()
)
k3lDeviceLocalDisconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceLocalDisconnect.setStatus("current")
_K3lDeviceCallFailBusy_Type = Counter32
_K3lDeviceCallFailBusy_Object = MibTableColumn
k3lDeviceCallFailBusy = _K3lDeviceCallFailBusy_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 2, 1, 21),
    _K3lDeviceCallFailBusy_Type()
)
k3lDeviceCallFailBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceCallFailBusy.setStatus("current")
_K3lDeviceCallFailNoAnswer_Type = Counter32
_K3lDeviceCallFailNoAnswer_Object = MibTableColumn
k3lDeviceCallFailNoAnswer = _K3lDeviceCallFailNoAnswer_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 2, 1, 22),
    _K3lDeviceCallFailNoAnswer_Type()
)
k3lDeviceCallFailNoAnswer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceCallFailNoAnswer.setStatus("current")
_K3lDeviceCallFailRejected_Type = Counter32
_K3lDeviceCallFailRejected_Object = MibTableColumn
k3lDeviceCallFailRejected = _K3lDeviceCallFailRejected_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 2, 1, 23),
    _K3lDeviceCallFailRejected_Type()
)
k3lDeviceCallFailRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceCallFailRejected.setStatus("current")
_K3lDeviceCallFailChangedNumber_Type = Counter32
_K3lDeviceCallFailChangedNumber_Object = MibTableColumn
k3lDeviceCallFailChangedNumber = _K3lDeviceCallFailChangedNumber_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 2, 1, 24),
    _K3lDeviceCallFailChangedNumber_Type()
)
k3lDeviceCallFailChangedNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceCallFailChangedNumber.setStatus("current")
_K3lDeviceCallFailInvalidNumber_Type = Counter32
_K3lDeviceCallFailInvalidNumber_Object = MibTableColumn
k3lDeviceCallFailInvalidNumber = _K3lDeviceCallFailInvalidNumber_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 2, 1, 25),
    _K3lDeviceCallFailInvalidNumber_Type()
)
k3lDeviceCallFailInvalidNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceCallFailInvalidNumber.setStatus("current")
_K3lDeviceCallFailOutOfService_Type = Counter32
_K3lDeviceCallFailOutOfService_Object = MibTableColumn
k3lDeviceCallFailOutOfService = _K3lDeviceCallFailOutOfService_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 2, 1, 26),
    _K3lDeviceCallFailOutOfService_Type()
)
k3lDeviceCallFailOutOfService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceCallFailOutOfService.setStatus("current")
_K3lDeviceCallFailCongestion_Type = Counter32
_K3lDeviceCallFailCongestion_Object = MibTableColumn
k3lDeviceCallFailCongestion = _K3lDeviceCallFailCongestion_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 2, 1, 27),
    _K3lDeviceCallFailCongestion_Type()
)
k3lDeviceCallFailCongestion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceCallFailCongestion.setStatus("current")
_K3lDeviceCallFailNetworkFailure_Type = Counter32
_K3lDeviceCallFailNetworkFailure_Object = MibTableColumn
k3lDeviceCallFailNetworkFailure = _K3lDeviceCallFailNetworkFailure_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 2, 1, 28),
    _K3lDeviceCallFailNetworkFailure_Type()
)
k3lDeviceCallFailNetworkFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceCallFailNetworkFailure.setStatus("current")
_K3lDeviceCallFailOther_Type = Counter32
_K3lDeviceCallFailOther_Object = MibTableColumn
k3lDeviceCallFailOther = _K3lDeviceCallFailOther_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 2, 1, 29),
    _K3lDeviceCallFailOther_Type()
)
k3lDeviceCallFailOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceCallFailOther.setStatus("current")
_K3lDeviceEbsIP_Type = DisplayString
_K3lDeviceEbsIP_Object = MibTableColumn
k3lDeviceEbsIP = _K3lDeviceEbsIP_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 2, 1, 30),
    _K3lDeviceEbsIP_Type()
)
k3lDeviceEbsIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceEbsIP.setStatus("current")
_K3lDeviceLinkTable_Object = MibTable
k3lDeviceLinkTable = _K3lDeviceLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 3)
)
if mibBuilder.loadTexts:
    k3lDeviceLinkTable.setStatus("current")
_K3lDeviceLinkEntry_Object = MibTableRow
k3lDeviceLinkEntry = _K3lDeviceLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 3, 1)
)
k3lDeviceLinkEntry.setIndexNames(
    (0, "KHOMP-MIB", "k3lDeviceSerial"),
    (0, "KHOMP-MIB", "k3lDeviceLinkIndex"),
)
if mibBuilder.loadTexts:
    k3lDeviceLinkEntry.setStatus("current")
_K3lDeviceLinkIndex_Type = KhompDeviceLinkIndex
_K3lDeviceLinkIndex_Object = MibTableColumn
k3lDeviceLinkIndex = _K3lDeviceLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 3, 1, 1),
    _K3lDeviceLinkIndex_Type()
)
k3lDeviceLinkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    k3lDeviceLinkIndex.setStatus("current")
_K3lDeviceLinkOperStatus_Type = KhompOperStatus
_K3lDeviceLinkOperStatus_Object = MibTableColumn
k3lDeviceLinkOperStatus = _K3lDeviceLinkOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 3, 1, 2),
    _K3lDeviceLinkOperStatus_Type()
)
k3lDeviceLinkOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceLinkOperStatus.setStatus("current")
_K3lDeviceLinkDescr_Type = DisplayString
_K3lDeviceLinkDescr_Object = MibTableColumn
k3lDeviceLinkDescr = _K3lDeviceLinkDescr_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 3, 1, 3),
    _K3lDeviceLinkDescr_Type()
)
k3lDeviceLinkDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceLinkDescr.setStatus("current")
_K3lDeviceLinkSignaling_Type = KhompSignaling
_K3lDeviceLinkSignaling_Object = MibTableColumn
k3lDeviceLinkSignaling = _K3lDeviceLinkSignaling_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 3, 1, 4),
    _K3lDeviceLinkSignaling_Type()
)
k3lDeviceLinkSignaling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceLinkSignaling.setStatus("current")
_K3lDeviceLinkAlarm_Type = KhompDeviceLinkAlarm
_K3lDeviceLinkAlarm_Object = MibTableColumn
k3lDeviceLinkAlarm = _K3lDeviceLinkAlarm_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 3, 1, 5),
    _K3lDeviceLinkAlarm_Type()
)
k3lDeviceLinkAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceLinkAlarm.setStatus("current")
_K3lDeviceLinkErrorCountChangesToLock_Type = KhompUnsigned16
_K3lDeviceLinkErrorCountChangesToLock_Object = MibTableColumn
k3lDeviceLinkErrorCountChangesToLock = _K3lDeviceLinkErrorCountChangesToLock_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 3, 1, 6),
    _K3lDeviceLinkErrorCountChangesToLock_Type()
)
k3lDeviceLinkErrorCountChangesToLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceLinkErrorCountChangesToLock.setStatus("current")
_K3lDeviceLinkErrorCountLostOfSignal_Type = KhompUnsigned16
_K3lDeviceLinkErrorCountLostOfSignal_Object = MibTableColumn
k3lDeviceLinkErrorCountLostOfSignal = _K3lDeviceLinkErrorCountLostOfSignal_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 3, 1, 7),
    _K3lDeviceLinkErrorCountLostOfSignal_Type()
)
k3lDeviceLinkErrorCountLostOfSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceLinkErrorCountLostOfSignal.setStatus("current")
_K3lDeviceLinkErrorCountAlarmNotification_Type = KhompUnsigned16
_K3lDeviceLinkErrorCountAlarmNotification_Object = MibTableColumn
k3lDeviceLinkErrorCountAlarmNotification = _K3lDeviceLinkErrorCountAlarmNotification_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 3, 1, 8),
    _K3lDeviceLinkErrorCountAlarmNotification_Type()
)
k3lDeviceLinkErrorCountAlarmNotification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceLinkErrorCountAlarmNotification.setStatus("current")
_K3lDeviceLinkErrorCountLostOfFrame_Type = KhompUnsigned16
_K3lDeviceLinkErrorCountLostOfFrame_Object = MibTableColumn
k3lDeviceLinkErrorCountLostOfFrame = _K3lDeviceLinkErrorCountLostOfFrame_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 3, 1, 9),
    _K3lDeviceLinkErrorCountLostOfFrame_Type()
)
k3lDeviceLinkErrorCountLostOfFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceLinkErrorCountLostOfFrame.setStatus("current")
_K3lDeviceLinkErrorCountLostOfMultiframe_Type = KhompUnsigned16
_K3lDeviceLinkErrorCountLostOfMultiframe_Object = MibTableColumn
k3lDeviceLinkErrorCountLostOfMultiframe = _K3lDeviceLinkErrorCountLostOfMultiframe_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 3, 1, 10),
    _K3lDeviceLinkErrorCountLostOfMultiframe_Type()
)
k3lDeviceLinkErrorCountLostOfMultiframe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceLinkErrorCountLostOfMultiframe.setStatus("current")
_K3lDeviceLinkErrorCountRemoteAlarm_Type = KhompUnsigned16
_K3lDeviceLinkErrorCountRemoteAlarm_Object = MibTableColumn
k3lDeviceLinkErrorCountRemoteAlarm = _K3lDeviceLinkErrorCountRemoteAlarm_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 3, 1, 11),
    _K3lDeviceLinkErrorCountRemoteAlarm_Type()
)
k3lDeviceLinkErrorCountRemoteAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceLinkErrorCountRemoteAlarm.setStatus("current")
_K3lDeviceLinkErrorCountSlipAlarm_Type = KhompUnsigned16
_K3lDeviceLinkErrorCountSlipAlarm_Object = MibTableColumn
k3lDeviceLinkErrorCountSlipAlarm = _K3lDeviceLinkErrorCountSlipAlarm_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 3, 1, 12),
    _K3lDeviceLinkErrorCountSlipAlarm_Type()
)
k3lDeviceLinkErrorCountSlipAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceLinkErrorCountSlipAlarm.setStatus("current")
_K3lDeviceLinkErrorCountPRBS_Type = KhompUnsigned16
_K3lDeviceLinkErrorCountPRBS_Object = MibTableColumn
k3lDeviceLinkErrorCountPRBS = _K3lDeviceLinkErrorCountPRBS_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 3, 1, 13),
    _K3lDeviceLinkErrorCountPRBS_Type()
)
k3lDeviceLinkErrorCountPRBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceLinkErrorCountPRBS.setStatus("current")
_K3lDeviceLinkErrorCountWrongEBits_Type = KhompUnsigned16
_K3lDeviceLinkErrorCountWrongEBits_Object = MibTableColumn
k3lDeviceLinkErrorCountWrongEBits = _K3lDeviceLinkErrorCountWrongEBits_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 3, 1, 14),
    _K3lDeviceLinkErrorCountWrongEBits_Type()
)
k3lDeviceLinkErrorCountWrongEBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceLinkErrorCountWrongEBits.setStatus("current")
_K3lDeviceLinkErrorCountJitterVariation_Type = KhompUnsigned16
_K3lDeviceLinkErrorCountJitterVariation_Object = MibTableColumn
k3lDeviceLinkErrorCountJitterVariation = _K3lDeviceLinkErrorCountJitterVariation_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 3, 1, 15),
    _K3lDeviceLinkErrorCountJitterVariation_Type()
)
k3lDeviceLinkErrorCountJitterVariation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceLinkErrorCountJitterVariation.setStatus("current")
_K3lDeviceLinkErrorCountFramesWithoutSync_Type = KhompUnsigned16
_K3lDeviceLinkErrorCountFramesWithoutSync_Object = MibTableColumn
k3lDeviceLinkErrorCountFramesWithoutSync = _K3lDeviceLinkErrorCountFramesWithoutSync_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 3, 1, 16),
    _K3lDeviceLinkErrorCountFramesWithoutSync_Type()
)
k3lDeviceLinkErrorCountFramesWithoutSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceLinkErrorCountFramesWithoutSync.setStatus("current")
_K3lDeviceLinkErrorCountMultiframeSignal_Type = KhompUnsigned16
_K3lDeviceLinkErrorCountMultiframeSignal_Object = MibTableColumn
k3lDeviceLinkErrorCountMultiframeSignal = _K3lDeviceLinkErrorCountMultiframeSignal_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 3, 1, 17),
    _K3lDeviceLinkErrorCountMultiframeSignal_Type()
)
k3lDeviceLinkErrorCountMultiframeSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceLinkErrorCountMultiframeSignal.setStatus("current")
_K3lDeviceLinkErrorCountFrameError_Type = KhompUnsigned16
_K3lDeviceLinkErrorCountFrameError_Object = MibTableColumn
k3lDeviceLinkErrorCountFrameError = _K3lDeviceLinkErrorCountFrameError_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 3, 1, 18),
    _K3lDeviceLinkErrorCountFrameError_Type()
)
k3lDeviceLinkErrorCountFrameError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceLinkErrorCountFrameError.setStatus("current")
_K3lDeviceLinkErrorCountBipolarViolation_Type = KhompUnsigned16
_K3lDeviceLinkErrorCountBipolarViolation_Object = MibTableColumn
k3lDeviceLinkErrorCountBipolarViolation = _K3lDeviceLinkErrorCountBipolarViolation_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 3, 1, 19),
    _K3lDeviceLinkErrorCountBipolarViolation_Type()
)
k3lDeviceLinkErrorCountBipolarViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceLinkErrorCountBipolarViolation.setStatus("current")
_K3lDeviceLinkErrorCountCRC4_Type = KhompUnsigned16
_K3lDeviceLinkErrorCountCRC4_Object = MibTableColumn
k3lDeviceLinkErrorCountCRC4 = _K3lDeviceLinkErrorCountCRC4_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 3, 1, 20),
    _K3lDeviceLinkErrorCountCRC4_Type()
)
k3lDeviceLinkErrorCountCRC4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceLinkErrorCountCRC4.setStatus("current")
_K3lDeviceLinkReset_Type = KhompBoolean
_K3lDeviceLinkReset_Object = MibTableColumn
k3lDeviceLinkReset = _K3lDeviceLinkReset_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 3, 1, 21),
    _K3lDeviceLinkReset_Type()
)
k3lDeviceLinkReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    k3lDeviceLinkReset.setStatus("current")
_K3lDeviceLinkResetErrorCount_Type = KhompBoolean
_K3lDeviceLinkResetErrorCount_Object = MibTableColumn
k3lDeviceLinkResetErrorCount = _K3lDeviceLinkResetErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 3, 1, 22),
    _K3lDeviceLinkResetErrorCount_Type()
)
k3lDeviceLinkResetErrorCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    k3lDeviceLinkResetErrorCount.setStatus("current")
_K3lDeviceLinkBlock_Type = KhompBoolean
_K3lDeviceLinkBlock_Object = MibTableColumn
k3lDeviceLinkBlock = _K3lDeviceLinkBlock_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 3, 1, 23),
    _K3lDeviceLinkBlock_Type()
)
k3lDeviceLinkBlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    k3lDeviceLinkBlock.setStatus("current")
_K3lDeviceLinkChannelCount_Type = Unsigned32
_K3lDeviceLinkChannelCount_Object = MibTableColumn
k3lDeviceLinkChannelCount = _K3lDeviceLinkChannelCount_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 3, 1, 24),
    _K3lDeviceLinkChannelCount_Type()
)
k3lDeviceLinkChannelCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceLinkChannelCount.setStatus("current")
_K3lDeviceLinkChannelCountEnabled_Type = Gauge32
_K3lDeviceLinkChannelCountEnabled_Object = MibTableColumn
k3lDeviceLinkChannelCountEnabled = _K3lDeviceLinkChannelCountEnabled_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 3, 1, 25),
    _K3lDeviceLinkChannelCountEnabled_Type()
)
k3lDeviceLinkChannelCountEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceLinkChannelCountEnabled.setStatus("current")
_K3lDeviceLinkChannelCountIdle_Type = Gauge32
_K3lDeviceLinkChannelCountIdle_Object = MibTableColumn
k3lDeviceLinkChannelCountIdle = _K3lDeviceLinkChannelCountIdle_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 3, 1, 26),
    _K3lDeviceLinkChannelCountIdle_Type()
)
k3lDeviceLinkChannelCountIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceLinkChannelCountIdle.setStatus("current")
_K3lDeviceLinkChannelCountFail_Type = Gauge32
_K3lDeviceLinkChannelCountFail_Object = MibTableColumn
k3lDeviceLinkChannelCountFail = _K3lDeviceLinkChannelCountFail_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 3, 1, 27),
    _K3lDeviceLinkChannelCountFail_Type()
)
k3lDeviceLinkChannelCountFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceLinkChannelCountFail.setStatus("current")
_K3lDeviceLinkChannelCountBusy_Type = Gauge32
_K3lDeviceLinkChannelCountBusy_Object = MibTableColumn
k3lDeviceLinkChannelCountBusy = _K3lDeviceLinkChannelCountBusy_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 3, 1, 28),
    _K3lDeviceLinkChannelCountBusy_Type()
)
k3lDeviceLinkChannelCountBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceLinkChannelCountBusy.setStatus("current")
_K3lDeviceLinkReceivingClock_Type = KhompBoolean
_K3lDeviceLinkReceivingClock_Object = MibTableColumn
k3lDeviceLinkReceivingClock = _K3lDeviceLinkReceivingClock_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 3, 1, 29),
    _K3lDeviceLinkReceivingClock_Type()
)
k3lDeviceLinkReceivingClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceLinkReceivingClock.setStatus("current")
_K3lDeviceLinkStatsIncoming_Type = Counter32
_K3lDeviceLinkStatsIncoming_Object = MibTableColumn
k3lDeviceLinkStatsIncoming = _K3lDeviceLinkStatsIncoming_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 3, 1, 30),
    _K3lDeviceLinkStatsIncoming_Type()
)
k3lDeviceLinkStatsIncoming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceLinkStatsIncoming.setStatus("current")
_K3lDeviceLinkStatsOutgoing_Type = Counter32
_K3lDeviceLinkStatsOutgoing_Object = MibTableColumn
k3lDeviceLinkStatsOutgoing = _K3lDeviceLinkStatsOutgoing_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 3, 1, 31),
    _K3lDeviceLinkStatsOutgoing_Type()
)
k3lDeviceLinkStatsOutgoing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceLinkStatsOutgoing.setStatus("current")
_K3lDeviceLinkOutgoingCompleted_Type = Counter32
_K3lDeviceLinkOutgoingCompleted_Object = MibTableColumn
k3lDeviceLinkOutgoingCompleted = _K3lDeviceLinkOutgoingCompleted_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 3, 1, 32),
    _K3lDeviceLinkOutgoingCompleted_Type()
)
k3lDeviceLinkOutgoingCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceLinkOutgoingCompleted.setStatus("current")
_K3lDeviceLinkOutgoingError_Type = Counter32
_K3lDeviceLinkOutgoingError_Object = MibTableColumn
k3lDeviceLinkOutgoingError = _K3lDeviceLinkOutgoingError_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 3, 1, 33),
    _K3lDeviceLinkOutgoingError_Type()
)
k3lDeviceLinkOutgoingError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceLinkOutgoingError.setStatus("current")
_K3lDeviceLinkRemoteDisconnect_Type = Counter32
_K3lDeviceLinkRemoteDisconnect_Object = MibTableColumn
k3lDeviceLinkRemoteDisconnect = _K3lDeviceLinkRemoteDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 3, 1, 34),
    _K3lDeviceLinkRemoteDisconnect_Type()
)
k3lDeviceLinkRemoteDisconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceLinkRemoteDisconnect.setStatus("current")
_K3lDeviceLinkLocalDisconnect_Type = Counter32
_K3lDeviceLinkLocalDisconnect_Object = MibTableColumn
k3lDeviceLinkLocalDisconnect = _K3lDeviceLinkLocalDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 3, 1, 35),
    _K3lDeviceLinkLocalDisconnect_Type()
)
k3lDeviceLinkLocalDisconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceLinkLocalDisconnect.setStatus("current")
_K3lDeviceLinkCallFailBusy_Type = Counter32
_K3lDeviceLinkCallFailBusy_Object = MibTableColumn
k3lDeviceLinkCallFailBusy = _K3lDeviceLinkCallFailBusy_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 3, 1, 36),
    _K3lDeviceLinkCallFailBusy_Type()
)
k3lDeviceLinkCallFailBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceLinkCallFailBusy.setStatus("current")
_K3lDeviceLinkCallFailNoAnswer_Type = Counter32
_K3lDeviceLinkCallFailNoAnswer_Object = MibTableColumn
k3lDeviceLinkCallFailNoAnswer = _K3lDeviceLinkCallFailNoAnswer_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 3, 1, 37),
    _K3lDeviceLinkCallFailNoAnswer_Type()
)
k3lDeviceLinkCallFailNoAnswer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceLinkCallFailNoAnswer.setStatus("current")
_K3lDeviceLinkCallFailRejected_Type = Counter32
_K3lDeviceLinkCallFailRejected_Object = MibTableColumn
k3lDeviceLinkCallFailRejected = _K3lDeviceLinkCallFailRejected_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 3, 1, 38),
    _K3lDeviceLinkCallFailRejected_Type()
)
k3lDeviceLinkCallFailRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceLinkCallFailRejected.setStatus("current")
_K3lDeviceLinkCallFailChangedNumber_Type = Counter32
_K3lDeviceLinkCallFailChangedNumber_Object = MibTableColumn
k3lDeviceLinkCallFailChangedNumber = _K3lDeviceLinkCallFailChangedNumber_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 3, 1, 39),
    _K3lDeviceLinkCallFailChangedNumber_Type()
)
k3lDeviceLinkCallFailChangedNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceLinkCallFailChangedNumber.setStatus("current")
_K3lDeviceLinkCallFailInvalidNumber_Type = Counter32
_K3lDeviceLinkCallFailInvalidNumber_Object = MibTableColumn
k3lDeviceLinkCallFailInvalidNumber = _K3lDeviceLinkCallFailInvalidNumber_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 3, 1, 40),
    _K3lDeviceLinkCallFailInvalidNumber_Type()
)
k3lDeviceLinkCallFailInvalidNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceLinkCallFailInvalidNumber.setStatus("current")
_K3lDeviceLinkCallFailOutOfService_Type = Counter32
_K3lDeviceLinkCallFailOutOfService_Object = MibTableColumn
k3lDeviceLinkCallFailOutOfService = _K3lDeviceLinkCallFailOutOfService_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 3, 1, 41),
    _K3lDeviceLinkCallFailOutOfService_Type()
)
k3lDeviceLinkCallFailOutOfService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceLinkCallFailOutOfService.setStatus("current")
_K3lDeviceLinkCallFailCongestion_Type = Counter32
_K3lDeviceLinkCallFailCongestion_Object = MibTableColumn
k3lDeviceLinkCallFailCongestion = _K3lDeviceLinkCallFailCongestion_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 3, 1, 42),
    _K3lDeviceLinkCallFailCongestion_Type()
)
k3lDeviceLinkCallFailCongestion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceLinkCallFailCongestion.setStatus("current")
_K3lDeviceLinkCallFailNetworkFailure_Type = Counter32
_K3lDeviceLinkCallFailNetworkFailure_Object = MibTableColumn
k3lDeviceLinkCallFailNetworkFailure = _K3lDeviceLinkCallFailNetworkFailure_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 3, 1, 43),
    _K3lDeviceLinkCallFailNetworkFailure_Type()
)
k3lDeviceLinkCallFailNetworkFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceLinkCallFailNetworkFailure.setStatus("current")
_K3lDeviceLinkCallFailOther_Type = Counter32
_K3lDeviceLinkCallFailOther_Object = MibTableColumn
k3lDeviceLinkCallFailOther = _K3lDeviceLinkCallFailOther_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 3, 1, 44),
    _K3lDeviceLinkCallFailOther_Type()
)
k3lDeviceLinkCallFailOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceLinkCallFailOther.setStatus("current")
_K3lDeviceLinkOperatingMode_Type = KhompLinkOperatingMode
_K3lDeviceLinkOperatingMode_Object = MibTableColumn
k3lDeviceLinkOperatingMode = _K3lDeviceLinkOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 3, 1, 45),
    _K3lDeviceLinkOperatingMode_Type()
)
k3lDeviceLinkOperatingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceLinkOperatingMode.setStatus("current")
_K3lDeviceHILinkTable_Object = MibTable
k3lDeviceHILinkTable = _K3lDeviceHILinkTable_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 4)
)
if mibBuilder.loadTexts:
    k3lDeviceHILinkTable.setStatus("current")
_K3lDeviceHILinkEntry_Object = MibTableRow
k3lDeviceHILinkEntry = _K3lDeviceHILinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 4, 1)
)
k3lDeviceHILinkEntry.setIndexNames(
    (0, "KHOMP-MIB", "k3lDeviceSerial"),
    (0, "KHOMP-MIB", "k3lDeviceHILinkIndex"),
)
if mibBuilder.loadTexts:
    k3lDeviceHILinkEntry.setStatus("current")
_K3lDeviceHILinkIndex_Type = KhompDeviceLinkIndex
_K3lDeviceHILinkIndex_Object = MibTableColumn
k3lDeviceHILinkIndex = _K3lDeviceHILinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 4, 1, 1),
    _K3lDeviceHILinkIndex_Type()
)
k3lDeviceHILinkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    k3lDeviceHILinkIndex.setStatus("current")
_K3lDeviceHILinkOperStatus_Type = KhompOperStatus
_K3lDeviceHILinkOperStatus_Object = MibTableColumn
k3lDeviceHILinkOperStatus = _K3lDeviceHILinkOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 4, 1, 2),
    _K3lDeviceHILinkOperStatus_Type()
)
k3lDeviceHILinkOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceHILinkOperStatus.setStatus("current")
_K3lDeviceHILinkAlarm_Type = KhompDeviceLinkAlarm
_K3lDeviceHILinkAlarm_Object = MibTableColumn
k3lDeviceHILinkAlarm = _K3lDeviceHILinkAlarm_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 4, 1, 3),
    _K3lDeviceHILinkAlarm_Type()
)
k3lDeviceHILinkAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceHILinkAlarm.setStatus("current")
_K3lDeviceChannelTable_Object = MibTable
k3lDeviceChannelTable = _K3lDeviceChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 5)
)
if mibBuilder.loadTexts:
    k3lDeviceChannelTable.setStatus("current")
_K3lDeviceChannelEntry_Object = MibTableRow
k3lDeviceChannelEntry = _K3lDeviceChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 5, 1)
)
k3lDeviceChannelEntry.setIndexNames(
    (0, "KHOMP-MIB", "k3lDeviceSerial"),
    (0, "KHOMP-MIB", "k3lDeviceChannelIndex"),
)
if mibBuilder.loadTexts:
    k3lDeviceChannelEntry.setStatus("current")
_K3lDeviceChannelIndex_Type = KhompDeviceChannelIndex
_K3lDeviceChannelIndex_Object = MibTableColumn
k3lDeviceChannelIndex = _K3lDeviceChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 5, 1, 1),
    _K3lDeviceChannelIndex_Type()
)
k3lDeviceChannelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    k3lDeviceChannelIndex.setStatus("current")
_K3lDeviceChannelSignaling_Type = KhompSignaling
_K3lDeviceChannelSignaling_Object = MibTableColumn
k3lDeviceChannelSignaling = _K3lDeviceChannelSignaling_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 5, 1, 2),
    _K3lDeviceChannelSignaling_Type()
)
k3lDeviceChannelSignaling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceChannelSignaling.setStatus("current")
_K3lDeviceChannelCallStatus_Type = KhompDeviceChannelCallStatus
_K3lDeviceChannelCallStatus_Object = MibTableColumn
k3lDeviceChannelCallStatus = _K3lDeviceChannelCallStatus_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 5, 1, 3),
    _K3lDeviceChannelCallStatus_Type()
)
k3lDeviceChannelCallStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceChannelCallStatus.setStatus("current")
_K3lDeviceChannelAudioStatus_Type = KhompDeviceChannelAudioStatus
_K3lDeviceChannelAudioStatus_Object = MibTableColumn
k3lDeviceChannelAudioStatus = _K3lDeviceChannelAudioStatus_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 5, 1, 4),
    _K3lDeviceChannelAudioStatus_Type()
)
k3lDeviceChannelAudioStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceChannelAudioStatus.setStatus("current")
_K3lDeviceChannelEnabledFeatures_Type = KhompDeviceChannelFeatures
_K3lDeviceChannelEnabledFeatures_Object = MibTableColumn
k3lDeviceChannelEnabledFeatures = _K3lDeviceChannelEnabledFeatures_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 5, 1, 5),
    _K3lDeviceChannelEnabledFeatures_Type()
)
k3lDeviceChannelEnabledFeatures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceChannelEnabledFeatures.setStatus("current")
_K3lDeviceChannelStatsIncoming_Type = Counter32
_K3lDeviceChannelStatsIncoming_Object = MibTableColumn
k3lDeviceChannelStatsIncoming = _K3lDeviceChannelStatsIncoming_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 5, 1, 6),
    _K3lDeviceChannelStatsIncoming_Type()
)
k3lDeviceChannelStatsIncoming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceChannelStatsIncoming.setStatus("current")
_K3lDeviceChannelStatsOutgoing_Type = Counter32
_K3lDeviceChannelStatsOutgoing_Object = MibTableColumn
k3lDeviceChannelStatsOutgoing = _K3lDeviceChannelStatsOutgoing_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 5, 1, 7),
    _K3lDeviceChannelStatsOutgoing_Type()
)
k3lDeviceChannelStatsOutgoing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceChannelStatsOutgoing.setStatus("current")
_K3lDeviceChannelStatsOutgoingCompleted_Type = Counter32
_K3lDeviceChannelStatsOutgoingCompleted_Object = MibTableColumn
k3lDeviceChannelStatsOutgoingCompleted = _K3lDeviceChannelStatsOutgoingCompleted_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 5, 1, 8),
    _K3lDeviceChannelStatsOutgoingCompleted_Type()
)
k3lDeviceChannelStatsOutgoingCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceChannelStatsOutgoingCompleted.setStatus("current")
_K3lDeviceChannelStatsOutgoingError_Type = Counter32
_K3lDeviceChannelStatsOutgoingError_Object = MibTableColumn
k3lDeviceChannelStatsOutgoingError = _K3lDeviceChannelStatsOutgoingError_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 5, 1, 9),
    _K3lDeviceChannelStatsOutgoingError_Type()
)
k3lDeviceChannelStatsOutgoingError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceChannelStatsOutgoingError.setStatus("current")
_K3lDeviceChannelStatsRemoteDisconnect_Type = Counter32
_K3lDeviceChannelStatsRemoteDisconnect_Object = MibTableColumn
k3lDeviceChannelStatsRemoteDisconnect = _K3lDeviceChannelStatsRemoteDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 5, 1, 10),
    _K3lDeviceChannelStatsRemoteDisconnect_Type()
)
k3lDeviceChannelStatsRemoteDisconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceChannelStatsRemoteDisconnect.setStatus("current")
_K3lDeviceChannelStatsLocalDisconnect_Type = Counter32
_K3lDeviceChannelStatsLocalDisconnect_Object = MibTableColumn
k3lDeviceChannelStatsLocalDisconnect = _K3lDeviceChannelStatsLocalDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 5, 1, 11),
    _K3lDeviceChannelStatsLocalDisconnect_Type()
)
k3lDeviceChannelStatsLocalDisconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceChannelStatsLocalDisconnect.setStatus("current")
_K3lDeviceChannelStatsCallFailBusy_Type = Counter32
_K3lDeviceChannelStatsCallFailBusy_Object = MibTableColumn
k3lDeviceChannelStatsCallFailBusy = _K3lDeviceChannelStatsCallFailBusy_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 5, 1, 12),
    _K3lDeviceChannelStatsCallFailBusy_Type()
)
k3lDeviceChannelStatsCallFailBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceChannelStatsCallFailBusy.setStatus("current")
_K3lDeviceChannelStatsCallFailNoAnswer_Type = Counter32
_K3lDeviceChannelStatsCallFailNoAnswer_Object = MibTableColumn
k3lDeviceChannelStatsCallFailNoAnswer = _K3lDeviceChannelStatsCallFailNoAnswer_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 5, 1, 13),
    _K3lDeviceChannelStatsCallFailNoAnswer_Type()
)
k3lDeviceChannelStatsCallFailNoAnswer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceChannelStatsCallFailNoAnswer.setStatus("current")
_K3lDeviceChannelStatsCallFailRejected_Type = Counter32
_K3lDeviceChannelStatsCallFailRejected_Object = MibTableColumn
k3lDeviceChannelStatsCallFailRejected = _K3lDeviceChannelStatsCallFailRejected_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 5, 1, 14),
    _K3lDeviceChannelStatsCallFailRejected_Type()
)
k3lDeviceChannelStatsCallFailRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceChannelStatsCallFailRejected.setStatus("current")
_K3lDeviceChannelStatsCallFailChangedNumber_Type = Counter32
_K3lDeviceChannelStatsCallFailChangedNumber_Object = MibTableColumn
k3lDeviceChannelStatsCallFailChangedNumber = _K3lDeviceChannelStatsCallFailChangedNumber_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 5, 1, 15),
    _K3lDeviceChannelStatsCallFailChangedNumber_Type()
)
k3lDeviceChannelStatsCallFailChangedNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceChannelStatsCallFailChangedNumber.setStatus("current")
_K3lDeviceChannelStatsCallFailInvalidNumber_Type = Counter32
_K3lDeviceChannelStatsCallFailInvalidNumber_Object = MibTableColumn
k3lDeviceChannelStatsCallFailInvalidNumber = _K3lDeviceChannelStatsCallFailInvalidNumber_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 5, 1, 16),
    _K3lDeviceChannelStatsCallFailInvalidNumber_Type()
)
k3lDeviceChannelStatsCallFailInvalidNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceChannelStatsCallFailInvalidNumber.setStatus("current")
_K3lDeviceChannelStatsCallFailOutOfService_Type = Counter32
_K3lDeviceChannelStatsCallFailOutOfService_Object = MibTableColumn
k3lDeviceChannelStatsCallFailOutOfService = _K3lDeviceChannelStatsCallFailOutOfService_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 5, 1, 17),
    _K3lDeviceChannelStatsCallFailOutOfService_Type()
)
k3lDeviceChannelStatsCallFailOutOfService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceChannelStatsCallFailOutOfService.setStatus("current")
_K3lDeviceChannelStatsCallFailCongestion_Type = Counter32
_K3lDeviceChannelStatsCallFailCongestion_Object = MibTableColumn
k3lDeviceChannelStatsCallFailCongestion = _K3lDeviceChannelStatsCallFailCongestion_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 5, 1, 18),
    _K3lDeviceChannelStatsCallFailCongestion_Type()
)
k3lDeviceChannelStatsCallFailCongestion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceChannelStatsCallFailCongestion.setStatus("current")
_K3lDeviceChannelStatsCallFailNetworkFailure_Type = Counter32
_K3lDeviceChannelStatsCallFailNetworkFailure_Object = MibTableColumn
k3lDeviceChannelStatsCallFailNetworkFailure = _K3lDeviceChannelStatsCallFailNetworkFailure_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 5, 1, 19),
    _K3lDeviceChannelStatsCallFailNetworkFailure_Type()
)
k3lDeviceChannelStatsCallFailNetworkFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceChannelStatsCallFailNetworkFailure.setStatus("current")
_K3lDeviceChannelStatsCallFailOther_Type = Counter32
_K3lDeviceChannelStatsCallFailOther_Object = MibTableColumn
k3lDeviceChannelStatsCallFailOther = _K3lDeviceChannelStatsCallFailOther_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 5, 1, 20),
    _K3lDeviceChannelStatsCallFailOther_Type()
)
k3lDeviceChannelStatsCallFailOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceChannelStatsCallFailOther.setStatus("current")
_K3lDeviceChannelDestinationAddress_Type = DisplayString
_K3lDeviceChannelDestinationAddress_Object = MibTableColumn
k3lDeviceChannelDestinationAddress = _K3lDeviceChannelDestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 5, 1, 21),
    _K3lDeviceChannelDestinationAddress_Type()
)
k3lDeviceChannelDestinationAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceChannelDestinationAddress.setStatus("current")
_K3lDeviceChannelCallDuration_Type = Gauge32
_K3lDeviceChannelCallDuration_Object = MibTableColumn
k3lDeviceChannelCallDuration = _K3lDeviceChannelCallDuration_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 5, 1, 22),
    _K3lDeviceChannelCallDuration_Type()
)
k3lDeviceChannelCallDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceChannelCallDuration.setStatus("current")
_K3lDeviceChannelRecording_Type = KhompBoolean
_K3lDeviceChannelRecording_Object = MibTableColumn
k3lDeviceChannelRecording = _K3lDeviceChannelRecording_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 5, 1, 23),
    _K3lDeviceChannelRecording_Type()
)
k3lDeviceChannelRecording.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceChannelRecording.setStatus("current")
_K3lDeviceChannelAverageCallTime_Type = Gauge32
_K3lDeviceChannelAverageCallTime_Object = MibTableColumn
k3lDeviceChannelAverageCallTime = _K3lDeviceChannelAverageCallTime_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 5, 1, 24),
    _K3lDeviceChannelAverageCallTime_Type()
)
k3lDeviceChannelAverageCallTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceChannelAverageCallTime.setStatus("current")
_K3lDeviceChannelOriginAddress_Type = DisplayString
_K3lDeviceChannelOriginAddress_Object = MibTableColumn
k3lDeviceChannelOriginAddress = _K3lDeviceChannelOriginAddress_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 5, 1, 25),
    _K3lDeviceChannelOriginAddress_Type()
)
k3lDeviceChannelOriginAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceChannelOriginAddress.setStatus("current")
_K3lDeviceChannelCadenceStatus_Type = KhompBoolean
_K3lDeviceChannelCadenceStatus_Object = MibTableColumn
k3lDeviceChannelCadenceStatus = _K3lDeviceChannelCadenceStatus_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 5, 1, 26),
    _K3lDeviceChannelCadenceStatus_Type()
)
k3lDeviceChannelCadenceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceChannelCadenceStatus.setStatus("current")
_K3lDeviceExtended_ObjectIdentity = ObjectIdentity
k3lDeviceExtended = _K3lDeviceExtended_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6)
)
_K3lDeviceExtendedE1_ObjectIdentity = ObjectIdentity
k3lDeviceExtendedE1 = _K3lDeviceExtendedE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 1)
)
_K3lDeviceE1ChannelCount_Type = Unsigned32
_K3lDeviceE1ChannelCount_Object = MibScalar
k3lDeviceE1ChannelCount = _K3lDeviceE1ChannelCount_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 1, 1),
    _K3lDeviceE1ChannelCount_Type()
)
k3lDeviceE1ChannelCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceE1ChannelCount.setStatus("current")
_K3lDeviceE1ChannelTable_Object = MibTable
k3lDeviceE1ChannelTable = _K3lDeviceE1ChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 1, 2)
)
if mibBuilder.loadTexts:
    k3lDeviceE1ChannelTable.setStatus("current")
_K3lDeviceE1ChannelEntry_Object = MibTableRow
k3lDeviceE1ChannelEntry = _K3lDeviceE1ChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 1, 2, 1)
)
k3lDeviceE1ChannelEntry.setIndexNames(
    (0, "KHOMP-MIB", "k3lDeviceSerial"),
    (0, "KHOMP-MIB", "k3lDeviceChannelIndex"),
)
if mibBuilder.loadTexts:
    k3lDeviceE1ChannelEntry.setStatus("current")
_K3lDeviceE1ChannelIndex_Type = KhompDeviceChannelIndex
_K3lDeviceE1ChannelIndex_Object = MibTableColumn
k3lDeviceE1ChannelIndex = _K3lDeviceE1ChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 1, 2, 1, 1),
    _K3lDeviceE1ChannelIndex_Type()
)
k3lDeviceE1ChannelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    k3lDeviceE1ChannelIndex.setStatus("current")
_K3lDeviceE1ChannelStatus_Type = KhompDeviceE1ChannelStatus
_K3lDeviceE1ChannelStatus_Object = MibTableColumn
k3lDeviceE1ChannelStatus = _K3lDeviceE1ChannelStatus_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 1, 2, 1, 2),
    _K3lDeviceE1ChannelStatus_Type()
)
k3lDeviceE1ChannelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceE1ChannelStatus.setStatus("current")
_K3lDeviceExtendedFxo_ObjectIdentity = ObjectIdentity
k3lDeviceExtendedFxo = _K3lDeviceExtendedFxo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 2)
)
_K3lDeviceFxoChannelCount_Type = Unsigned32
_K3lDeviceFxoChannelCount_Object = MibScalar
k3lDeviceFxoChannelCount = _K3lDeviceFxoChannelCount_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 2, 1),
    _K3lDeviceFxoChannelCount_Type()
)
k3lDeviceFxoChannelCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceFxoChannelCount.setStatus("current")
_K3lDeviceFxoChannelTable_Object = MibTable
k3lDeviceFxoChannelTable = _K3lDeviceFxoChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 2, 2)
)
if mibBuilder.loadTexts:
    k3lDeviceFxoChannelTable.setStatus("current")
_K3lDeviceFxoChannelEntry_Object = MibTableRow
k3lDeviceFxoChannelEntry = _K3lDeviceFxoChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 2, 2, 1)
)
k3lDeviceFxoChannelEntry.setIndexNames(
    (0, "KHOMP-MIB", "k3lDeviceSerial"),
    (0, "KHOMP-MIB", "k3lDeviceChannelIndex"),
)
if mibBuilder.loadTexts:
    k3lDeviceFxoChannelEntry.setStatus("current")
_K3lDeviceFxoChannelIndex_Type = KhompDeviceChannelIndex
_K3lDeviceFxoChannelIndex_Object = MibTableColumn
k3lDeviceFxoChannelIndex = _K3lDeviceFxoChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 2, 2, 1, 1),
    _K3lDeviceFxoChannelIndex_Type()
)
k3lDeviceFxoChannelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    k3lDeviceFxoChannelIndex.setStatus("current")
_K3lDeviceFxoChannelStatus_Type = KhompDeviceFxoChannelStatus
_K3lDeviceFxoChannelStatus_Object = MibTableColumn
k3lDeviceFxoChannelStatus = _K3lDeviceFxoChannelStatus_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 2, 2, 1, 2),
    _K3lDeviceFxoChannelStatus_Type()
)
k3lDeviceFxoChannelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceFxoChannelStatus.setStatus("current")
_K3lDeviceExtendedFxs_ObjectIdentity = ObjectIdentity
k3lDeviceExtendedFxs = _K3lDeviceExtendedFxs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 3)
)
_K3lDeviceFxsChannelCount_Type = Unsigned32
_K3lDeviceFxsChannelCount_Object = MibScalar
k3lDeviceFxsChannelCount = _K3lDeviceFxsChannelCount_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 3, 1),
    _K3lDeviceFxsChannelCount_Type()
)
k3lDeviceFxsChannelCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceFxsChannelCount.setStatus("current")
_K3lDeviceFxsChannelTable_Object = MibTable
k3lDeviceFxsChannelTable = _K3lDeviceFxsChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 3, 2)
)
if mibBuilder.loadTexts:
    k3lDeviceFxsChannelTable.setStatus("current")
_K3lDeviceFxsChannelEntry_Object = MibTableRow
k3lDeviceFxsChannelEntry = _K3lDeviceFxsChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 3, 2, 1)
)
k3lDeviceFxsChannelEntry.setIndexNames(
    (0, "KHOMP-MIB", "k3lDeviceSerial"),
    (0, "KHOMP-MIB", "k3lDeviceChannelIndex"),
)
if mibBuilder.loadTexts:
    k3lDeviceFxsChannelEntry.setStatus("current")
_K3lDeviceFxsChannelIndex_Type = KhompDeviceChannelIndex
_K3lDeviceFxsChannelIndex_Object = MibTableColumn
k3lDeviceFxsChannelIndex = _K3lDeviceFxsChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 3, 2, 1, 1),
    _K3lDeviceFxsChannelIndex_Type()
)
k3lDeviceFxsChannelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    k3lDeviceFxsChannelIndex.setStatus("current")
_K3lDeviceFxsChannelStatus_Type = KhompDeviceFxsChannelStatus
_K3lDeviceFxsChannelStatus_Object = MibTableColumn
k3lDeviceFxsChannelStatus = _K3lDeviceFxsChannelStatus_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 3, 2, 1, 2),
    _K3lDeviceFxsChannelStatus_Type()
)
k3lDeviceFxsChannelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceFxsChannelStatus.setStatus("current")
_K3lDeviceExtendedGsm_ObjectIdentity = ObjectIdentity
k3lDeviceExtendedGsm = _K3lDeviceExtendedGsm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 4)
)
_K3lDeviceGsmChannelCount_Type = Unsigned32
_K3lDeviceGsmChannelCount_Object = MibScalar
k3lDeviceGsmChannelCount = _K3lDeviceGsmChannelCount_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 4, 1),
    _K3lDeviceGsmChannelCount_Type()
)
k3lDeviceGsmChannelCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceGsmChannelCount.setStatus("current")
_K3lDeviceGsmChannelTable_Object = MibTable
k3lDeviceGsmChannelTable = _K3lDeviceGsmChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 4, 2)
)
if mibBuilder.loadTexts:
    k3lDeviceGsmChannelTable.setStatus("current")
_K3lDeviceGsmChannelEntry_Object = MibTableRow
k3lDeviceGsmChannelEntry = _K3lDeviceGsmChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 4, 2, 1)
)
k3lDeviceGsmChannelEntry.setIndexNames(
    (0, "KHOMP-MIB", "k3lDeviceSerial"),
    (0, "KHOMP-MIB", "k3lDeviceChannelIndex"),
)
if mibBuilder.loadTexts:
    k3lDeviceGsmChannelEntry.setStatus("current")
_K3lDeviceGsmChannelIndex_Type = KhompDeviceChannelIndex
_K3lDeviceGsmChannelIndex_Object = MibTableColumn
k3lDeviceGsmChannelIndex = _K3lDeviceGsmChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 4, 2, 1, 1),
    _K3lDeviceGsmChannelIndex_Type()
)
k3lDeviceGsmChannelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    k3lDeviceGsmChannelIndex.setStatus("current")
_K3lDeviceGsmChannelStatus_Type = KhompDeviceGsmChannelStatus
_K3lDeviceGsmChannelStatus_Object = MibTableColumn
k3lDeviceGsmChannelStatus = _K3lDeviceGsmChannelStatus_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 4, 2, 1, 2),
    _K3lDeviceGsmChannelStatus_Type()
)
k3lDeviceGsmChannelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceGsmChannelStatus.setStatus("current")
_K3lDeviceGsmChannelSignalStrength_Type = Gauge32
_K3lDeviceGsmChannelSignalStrength_Object = MibTableColumn
k3lDeviceGsmChannelSignalStrength = _K3lDeviceGsmChannelSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 4, 2, 1, 3),
    _K3lDeviceGsmChannelSignalStrength_Type()
)
k3lDeviceGsmChannelSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceGsmChannelSignalStrength.setStatus("current")
_K3lDeviceGsmChannelErrorRate_Type = Gauge32
_K3lDeviceGsmChannelErrorRate_Object = MibTableColumn
k3lDeviceGsmChannelErrorRate = _K3lDeviceGsmChannelErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 4, 2, 1, 4),
    _K3lDeviceGsmChannelErrorRate_Type()
)
k3lDeviceGsmChannelErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceGsmChannelErrorRate.setStatus("current")
_K3lDeviceGsmChannelRegistryStatus_Type = KhompDeviceGsmChannelRegistryStatus
_K3lDeviceGsmChannelRegistryStatus_Object = MibTableColumn
k3lDeviceGsmChannelRegistryStatus = _K3lDeviceGsmChannelRegistryStatus_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 4, 2, 1, 5),
    _K3lDeviceGsmChannelRegistryStatus_Type()
)
k3lDeviceGsmChannelRegistryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceGsmChannelRegistryStatus.setStatus("current")
_K3lDeviceGsmChannelOperName_Type = DisplayString
_K3lDeviceGsmChannelOperName_Object = MibTableColumn
k3lDeviceGsmChannelOperName = _K3lDeviceGsmChannelOperName_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 4, 2, 1, 6),
    _K3lDeviceGsmChannelOperName_Type()
)
k3lDeviceGsmChannelOperName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceGsmChannelOperName.setStatus("current")
_K3lDeviceGsmChannelUnreadSmsMessages_Type = Gauge32
_K3lDeviceGsmChannelUnreadSmsMessages_Object = MibTableColumn
k3lDeviceGsmChannelUnreadSmsMessages = _K3lDeviceGsmChannelUnreadSmsMessages_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 4, 2, 1, 7),
    _K3lDeviceGsmChannelUnreadSmsMessages_Type()
)
k3lDeviceGsmChannelUnreadSmsMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceGsmChannelUnreadSmsMessages.setStatus("current")
_K3lDeviceGsmChannelEnabledFeatures_Type = KhompDeviceGsmChannelEnabledFeatures
_K3lDeviceGsmChannelEnabledFeatures_Object = MibTableColumn
k3lDeviceGsmChannelEnabledFeatures = _K3lDeviceGsmChannelEnabledFeatures_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 4, 2, 1, 8),
    _K3lDeviceGsmChannelEnabledFeatures_Type()
)
k3lDeviceGsmChannelEnabledFeatures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceGsmChannelEnabledFeatures.setStatus("current")
_K3lDeviceGsmChannelImei_Type = DisplayString
_K3lDeviceGsmChannelImei_Object = MibTableColumn
k3lDeviceGsmChannelImei = _K3lDeviceGsmChannelImei_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 4, 2, 1, 9),
    _K3lDeviceGsmChannelImei_Type()
)
k3lDeviceGsmChannelImei.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceGsmChannelImei.setStatus("current")
_K3lDeviceGsmChannelSim_Type = Unsigned32
_K3lDeviceGsmChannelSim_Object = MibTableColumn
k3lDeviceGsmChannelSim = _K3lDeviceGsmChannelSim_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 4, 2, 1, 10),
    _K3lDeviceGsmChannelSim_Type()
)
k3lDeviceGsmChannelSim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceGsmChannelSim.setStatus("current")
_K3lDeviceGsmChannelImsi_Type = DisplayString
_K3lDeviceGsmChannelImsi_Object = MibTableColumn
k3lDeviceGsmChannelImsi = _K3lDeviceGsmChannelImsi_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 4, 2, 1, 11),
    _K3lDeviceGsmChannelImsi_Type()
)
k3lDeviceGsmChannelImsi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceGsmChannelImsi.setStatus("current")
_K3lDeviceGsmChannelIccid_Type = DisplayString
_K3lDeviceGsmChannelIccid_Object = MibTableColumn
k3lDeviceGsmChannelIccid = _K3lDeviceGsmChannelIccid_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 4, 2, 1, 12),
    _K3lDeviceGsmChannelIccid_Type()
)
k3lDeviceGsmChannelIccid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceGsmChannelIccid.setStatus("current")
_K3lDeviceGsmChannelMsisdn_Type = DisplayString
_K3lDeviceGsmChannelMsisdn_Object = MibTableColumn
k3lDeviceGsmChannelMsisdn = _K3lDeviceGsmChannelMsisdn_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 4, 2, 1, 13),
    _K3lDeviceGsmChannelMsisdn_Type()
)
k3lDeviceGsmChannelMsisdn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceGsmChannelMsisdn.setStatus("current")
_K3lDeviceGsmChannelCallWaiting_Type = KhompDeviceGsmChannelCallWaitingState
_K3lDeviceGsmChannelCallWaiting_Object = MibTableColumn
k3lDeviceGsmChannelCallWaiting = _K3lDeviceGsmChannelCallWaiting_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 4, 2, 1, 14),
    _K3lDeviceGsmChannelCallWaiting_Type()
)
k3lDeviceGsmChannelCallWaiting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceGsmChannelCallWaiting.setStatus("current")
_K3lDeviceGsmChannelSimCardCount_Type = Gauge32
_K3lDeviceGsmChannelSimCardCount_Object = MibTableColumn
k3lDeviceGsmChannelSimCardCount = _K3lDeviceGsmChannelSimCardCount_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 4, 2, 1, 15),
    _K3lDeviceGsmChannelSimCardCount_Type()
)
k3lDeviceGsmChannelSimCardCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceGsmChannelSimCardCount.setStatus("current")
_K3lDeviceGsmCallTable_Object = MibTable
k3lDeviceGsmCallTable = _K3lDeviceGsmCallTable_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 4, 3)
)
if mibBuilder.loadTexts:
    k3lDeviceGsmCallTable.setStatus("current")
_K3lDeviceGsmCallEntry_Object = MibTableRow
k3lDeviceGsmCallEntry = _K3lDeviceGsmCallEntry_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 4, 3, 1)
)
k3lDeviceGsmCallEntry.setIndexNames(
    (0, "KHOMP-MIB", "k3lDeviceSerial"),
    (0, "KHOMP-MIB", "k3lDeviceChannelIndex"),
    (0, "KHOMP-MIB", "k3lDeviceGsmCallIndex"),
)
if mibBuilder.loadTexts:
    k3lDeviceGsmCallEntry.setStatus("current")
_K3lDeviceGsmCallIndex_Type = KhompDeviceGsmCallIndex
_K3lDeviceGsmCallIndex_Object = MibTableColumn
k3lDeviceGsmCallIndex = _K3lDeviceGsmCallIndex_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 4, 3, 1, 1),
    _K3lDeviceGsmCallIndex_Type()
)
k3lDeviceGsmCallIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    k3lDeviceGsmCallIndex.setStatus("current")
_K3lDeviceGsmCallStatus_Type = KhompDeviceGsmCallStatus
_K3lDeviceGsmCallStatus_Object = MibTableColumn
k3lDeviceGsmCallStatus = _K3lDeviceGsmCallStatus_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 4, 3, 1, 2),
    _K3lDeviceGsmCallStatus_Type()
)
k3lDeviceGsmCallStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceGsmCallStatus.setStatus("current")
_K3lDeviceGsmCallMode_Type = KhompDeviceGsmCallMode
_K3lDeviceGsmCallMode_Object = MibTableColumn
k3lDeviceGsmCallMode = _K3lDeviceGsmCallMode_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 4, 3, 1, 3),
    _K3lDeviceGsmCallMode_Type()
)
k3lDeviceGsmCallMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceGsmCallMode.setStatus("current")
_K3lDeviceGsmCallNumber_Type = DisplayString
_K3lDeviceGsmCallNumber_Object = MibTableColumn
k3lDeviceGsmCallNumber = _K3lDeviceGsmCallNumber_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 4, 3, 1, 4),
    _K3lDeviceGsmCallNumber_Type()
)
k3lDeviceGsmCallNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceGsmCallNumber.setStatus("current")
_K3lDeviceGsmCallFlags_Type = KhompDeviceGsmCallFlags
_K3lDeviceGsmCallFlags_Object = MibTableColumn
k3lDeviceGsmCallFlags = _K3lDeviceGsmCallFlags_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 4, 3, 1, 5),
    _K3lDeviceGsmCallFlags_Type()
)
k3lDeviceGsmCallFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceGsmCallFlags.setStatus("current")
_K3lDeviceExtendedVoip_ObjectIdentity = ObjectIdentity
k3lDeviceExtendedVoip = _K3lDeviceExtendedVoip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 5)
)
_K3lDeviceSipChannelCount_Type = Unsigned32
_K3lDeviceSipChannelCount_Object = MibScalar
k3lDeviceSipChannelCount = _K3lDeviceSipChannelCount_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 5, 1),
    _K3lDeviceSipChannelCount_Type()
)
k3lDeviceSipChannelCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceSipChannelCount.setStatus("current")
_K3lDeviceSipChannelTable_Object = MibTable
k3lDeviceSipChannelTable = _K3lDeviceSipChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 5, 2)
)
if mibBuilder.loadTexts:
    k3lDeviceSipChannelTable.setStatus("current")
_K3lDeviceSipChannelEntry_Object = MibTableRow
k3lDeviceSipChannelEntry = _K3lDeviceSipChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 5, 2, 1)
)
k3lDeviceSipChannelEntry.setIndexNames(
    (0, "KHOMP-MIB", "k3lDeviceChannelIndex"),
)
if mibBuilder.loadTexts:
    k3lDeviceSipChannelEntry.setStatus("current")
_K3lDeviceSipChannelIndex_Type = KhompDeviceChannelIndex
_K3lDeviceSipChannelIndex_Object = MibTableColumn
k3lDeviceSipChannelIndex = _K3lDeviceSipChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 5, 2, 1, 1),
    _K3lDeviceSipChannelIndex_Type()
)
k3lDeviceSipChannelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    k3lDeviceSipChannelIndex.setStatus("current")
_K3lDeviceSipChannelStatus_Type = KhompDeviceSipChannelStatus
_K3lDeviceSipChannelStatus_Object = MibTableColumn
k3lDeviceSipChannelStatus = _K3lDeviceSipChannelStatus_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 5, 2, 1, 2),
    _K3lDeviceSipChannelStatus_Type()
)
k3lDeviceSipChannelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceSipChannelStatus.setStatus("current")
_K3lDeviceVoipProfileLocalAddress_Type = DisplayString
_K3lDeviceVoipProfileLocalAddress_Object = MibTableColumn
k3lDeviceVoipProfileLocalAddress = _K3lDeviceVoipProfileLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 5, 2, 1, 3),
    _K3lDeviceVoipProfileLocalAddress_Type()
)
k3lDeviceVoipProfileLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceVoipProfileLocalAddress.setStatus("current")
_K3lDeviceVoipProfileLocalPort_Type = Gauge32
_K3lDeviceVoipProfileLocalPort_Object = MibTableColumn
k3lDeviceVoipProfileLocalPort = _K3lDeviceVoipProfileLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 5, 2, 1, 4),
    _K3lDeviceVoipProfileLocalPort_Type()
)
k3lDeviceVoipProfileLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceVoipProfileLocalPort.setStatus("current")
_K3lDeviceVoipProfileTransportType_Type = DisplayString
_K3lDeviceVoipProfileTransportType_Object = MibTableColumn
k3lDeviceVoipProfileTransportType = _K3lDeviceVoipProfileTransportType_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 5, 2, 1, 5),
    _K3lDeviceVoipProfileTransportType_Type()
)
k3lDeviceVoipProfileTransportType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceVoipProfileTransportType.setStatus("current")
_K3lDeviceVoipProfileRTPAddress_Type = DisplayString
_K3lDeviceVoipProfileRTPAddress_Object = MibTableColumn
k3lDeviceVoipProfileRTPAddress = _K3lDeviceVoipProfileRTPAddress_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 5, 2, 1, 6),
    _K3lDeviceVoipProfileRTPAddress_Type()
)
k3lDeviceVoipProfileRTPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceVoipProfileRTPAddress.setStatus("current")
_K3lDeviceVoipProfileUser_Type = DisplayString
_K3lDeviceVoipProfileUser_Object = MibTableColumn
k3lDeviceVoipProfileUser = _K3lDeviceVoipProfileUser_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 5, 2, 1, 7),
    _K3lDeviceVoipProfileUser_Type()
)
k3lDeviceVoipProfileUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceVoipProfileUser.setStatus("current")
_K3lDeviceVoipProfileAuthorizationUser_Type = DisplayString
_K3lDeviceVoipProfileAuthorizationUser_Object = MibTableColumn
k3lDeviceVoipProfileAuthorizationUser = _K3lDeviceVoipProfileAuthorizationUser_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 5, 2, 1, 8),
    _K3lDeviceVoipProfileAuthorizationUser_Type()
)
k3lDeviceVoipProfileAuthorizationUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceVoipProfileAuthorizationUser.setStatus("current")
_K3lDeviceVoipProfileRealm_Type = DisplayString
_K3lDeviceVoipProfileRealm_Object = MibTableColumn
k3lDeviceVoipProfileRealm = _K3lDeviceVoipProfileRealm_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 5, 2, 1, 9),
    _K3lDeviceVoipProfileRealm_Type()
)
k3lDeviceVoipProfileRealm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceVoipProfileRealm.setStatus("current")
_K3lDeviceVoipProfileDomain_Type = DisplayString
_K3lDeviceVoipProfileDomain_Object = MibTableColumn
k3lDeviceVoipProfileDomain = _K3lDeviceVoipProfileDomain_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 5, 2, 1, 10),
    _K3lDeviceVoipProfileDomain_Type()
)
k3lDeviceVoipProfileDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceVoipProfileDomain.setStatus("current")
_K3lDeviceVoipProfileDomainPort_Type = Gauge32
_K3lDeviceVoipProfileDomainPort_Object = MibTableColumn
k3lDeviceVoipProfileDomainPort = _K3lDeviceVoipProfileDomainPort_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 5, 2, 1, 11),
    _K3lDeviceVoipProfileDomainPort_Type()
)
k3lDeviceVoipProfileDomainPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceVoipProfileDomainPort.setStatus("current")
_K3lDeviceVoipProfileProxy_Type = DisplayString
_K3lDeviceVoipProfileProxy_Object = MibTableColumn
k3lDeviceVoipProfileProxy = _K3lDeviceVoipProfileProxy_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 5, 2, 1, 12),
    _K3lDeviceVoipProfileProxy_Type()
)
k3lDeviceVoipProfileProxy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceVoipProfileProxy.setStatus("current")
_K3lDeviceVoipProfileProxyPort_Type = Gauge32
_K3lDeviceVoipProfileProxyPort_Object = MibTableColumn
k3lDeviceVoipProfileProxyPort = _K3lDeviceVoipProfileProxyPort_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 5, 2, 1, 13),
    _K3lDeviceVoipProfileProxyPort_Type()
)
k3lDeviceVoipProfileProxyPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceVoipProfileProxyPort.setStatus("current")
_K3lDeviceVoipProfileRegistered_Type = DisplayString
_K3lDeviceVoipProfileRegistered_Object = MibTableColumn
k3lDeviceVoipProfileRegistered = _K3lDeviceVoipProfileRegistered_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 5, 2, 1, 14),
    _K3lDeviceVoipProfileRegistered_Type()
)
k3lDeviceVoipProfileRegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceVoipProfileRegistered.setStatus("current")
_K3lDeviceVoipChannelTransactionCount_Type = Gauge32
_K3lDeviceVoipChannelTransactionCount_Object = MibTableColumn
k3lDeviceVoipChannelTransactionCount = _K3lDeviceVoipChannelTransactionCount_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 5, 2, 1, 15),
    _K3lDeviceVoipChannelTransactionCount_Type()
)
k3lDeviceVoipChannelTransactionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceVoipChannelTransactionCount.setStatus("current")
_K3lDeviceVoipChannelClientTransactionCount_Type = Gauge32
_K3lDeviceVoipChannelClientTransactionCount_Object = MibTableColumn
k3lDeviceVoipChannelClientTransactionCount = _K3lDeviceVoipChannelClientTransactionCount_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 5, 2, 1, 16),
    _K3lDeviceVoipChannelClientTransactionCount_Type()
)
k3lDeviceVoipChannelClientTransactionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceVoipChannelClientTransactionCount.setStatus("current")
_K3lDeviceVoipChannelServerTransactionCount_Type = Gauge32
_K3lDeviceVoipChannelServerTransactionCount_Object = MibTableColumn
k3lDeviceVoipChannelServerTransactionCount = _K3lDeviceVoipChannelServerTransactionCount_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 5, 2, 1, 17),
    _K3lDeviceVoipChannelServerTransactionCount_Type()
)
k3lDeviceVoipChannelServerTransactionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceVoipChannelServerTransactionCount.setStatus("current")
_K3lDeviceVoipChannelClientTransactionFailureCount_Type = Gauge32
_K3lDeviceVoipChannelClientTransactionFailureCount_Object = MibTableColumn
k3lDeviceVoipChannelClientTransactionFailureCount = _K3lDeviceVoipChannelClientTransactionFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 5, 2, 1, 18),
    _K3lDeviceVoipChannelClientTransactionFailureCount_Type()
)
k3lDeviceVoipChannelClientTransactionFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceVoipChannelClientTransactionFailureCount.setStatus("current")
_K3lDeviceVoipChannelServerTransactionFailureCount_Type = Gauge32
_K3lDeviceVoipChannelServerTransactionFailureCount_Object = MibTableColumn
k3lDeviceVoipChannelServerTransactionFailureCount = _K3lDeviceVoipChannelServerTransactionFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 5, 2, 1, 19),
    _K3lDeviceVoipChannelServerTransactionFailureCount_Type()
)
k3lDeviceVoipChannelServerTransactionFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceVoipChannelServerTransactionFailureCount.setStatus("current")
_K3lDeviceVoipChannelClientTransactionFailure4xxCount_Type = Gauge32
_K3lDeviceVoipChannelClientTransactionFailure4xxCount_Object = MibTableColumn
k3lDeviceVoipChannelClientTransactionFailure4xxCount = _K3lDeviceVoipChannelClientTransactionFailure4xxCount_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 5, 2, 1, 20),
    _K3lDeviceVoipChannelClientTransactionFailure4xxCount_Type()
)
k3lDeviceVoipChannelClientTransactionFailure4xxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceVoipChannelClientTransactionFailure4xxCount.setStatus("current")
_K3lDeviceVoipChannelServerTransactionFailure4xxCount_Type = Gauge32
_K3lDeviceVoipChannelServerTransactionFailure4xxCount_Object = MibTableColumn
k3lDeviceVoipChannelServerTransactionFailure4xxCount = _K3lDeviceVoipChannelServerTransactionFailure4xxCount_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 5, 2, 1, 21),
    _K3lDeviceVoipChannelServerTransactionFailure4xxCount_Type()
)
k3lDeviceVoipChannelServerTransactionFailure4xxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceVoipChannelServerTransactionFailure4xxCount.setStatus("current")
_K3lDeviceVoipChannelClientTransactionFailure5xxCount_Type = Gauge32
_K3lDeviceVoipChannelClientTransactionFailure5xxCount_Object = MibTableColumn
k3lDeviceVoipChannelClientTransactionFailure5xxCount = _K3lDeviceVoipChannelClientTransactionFailure5xxCount_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 5, 2, 1, 22),
    _K3lDeviceVoipChannelClientTransactionFailure5xxCount_Type()
)
k3lDeviceVoipChannelClientTransactionFailure5xxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceVoipChannelClientTransactionFailure5xxCount.setStatus("current")
_K3lDeviceVoipChannelServerTransactionFailure5xxCount_Type = Gauge32
_K3lDeviceVoipChannelServerTransactionFailure5xxCount_Object = MibTableColumn
k3lDeviceVoipChannelServerTransactionFailure5xxCount = _K3lDeviceVoipChannelServerTransactionFailure5xxCount_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 5, 2, 1, 23),
    _K3lDeviceVoipChannelServerTransactionFailure5xxCount_Type()
)
k3lDeviceVoipChannelServerTransactionFailure5xxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceVoipChannelServerTransactionFailure5xxCount.setStatus("current")
_K3lDeviceVoipChannelClientTransactionFailure6xxCount_Type = Gauge32
_K3lDeviceVoipChannelClientTransactionFailure6xxCount_Object = MibTableColumn
k3lDeviceVoipChannelClientTransactionFailure6xxCount = _K3lDeviceVoipChannelClientTransactionFailure6xxCount_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 5, 2, 1, 24),
    _K3lDeviceVoipChannelClientTransactionFailure6xxCount_Type()
)
k3lDeviceVoipChannelClientTransactionFailure6xxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceVoipChannelClientTransactionFailure6xxCount.setStatus("current")
_K3lDeviceVoipChannelServerTransactionFailure6xxCount_Type = Gauge32
_K3lDeviceVoipChannelServerTransactionFailure6xxCount_Object = MibTableColumn
k3lDeviceVoipChannelServerTransactionFailure6xxCount = _K3lDeviceVoipChannelServerTransactionFailure6xxCount_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 5, 2, 1, 25),
    _K3lDeviceVoipChannelServerTransactionFailure6xxCount_Type()
)
k3lDeviceVoipChannelServerTransactionFailure6xxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceVoipChannelServerTransactionFailure6xxCount.setStatus("current")
_K3lDeviceVoipRTPStatusTransmitLastSequenceNumber_Type = Gauge32
_K3lDeviceVoipRTPStatusTransmitLastSequenceNumber_Object = MibTableColumn
k3lDeviceVoipRTPStatusTransmitLastSequenceNumber = _K3lDeviceVoipRTPStatusTransmitLastSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 5, 2, 1, 26),
    _K3lDeviceVoipRTPStatusTransmitLastSequenceNumber_Type()
)
k3lDeviceVoipRTPStatusTransmitLastSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceVoipRTPStatusTransmitLastSequenceNumber.setStatus("current")
_K3lDeviceVoipRTPStatusTransmitPacketCount_Type = Gauge32
_K3lDeviceVoipRTPStatusTransmitPacketCount_Object = MibTableColumn
k3lDeviceVoipRTPStatusTransmitPacketCount = _K3lDeviceVoipRTPStatusTransmitPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 5, 2, 1, 27),
    _K3lDeviceVoipRTPStatusTransmitPacketCount_Type()
)
k3lDeviceVoipRTPStatusTransmitPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceVoipRTPStatusTransmitPacketCount.setStatus("current")
_K3lDeviceVoipRTPStatusTransmitOctetCount_Type = Gauge32
_K3lDeviceVoipRTPStatusTransmitOctetCount_Object = MibTableColumn
k3lDeviceVoipRTPStatusTransmitOctetCount = _K3lDeviceVoipRTPStatusTransmitOctetCount_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 5, 2, 1, 28),
    _K3lDeviceVoipRTPStatusTransmitOctetCount_Type()
)
k3lDeviceVoipRTPStatusTransmitOctetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceVoipRTPStatusTransmitOctetCount.setStatus("current")
_K3lDeviceVoipRTPStatusTransmitPacketLost_Type = Gauge32
_K3lDeviceVoipRTPStatusTransmitPacketLost_Object = MibTableColumn
k3lDeviceVoipRTPStatusTransmitPacketLost = _K3lDeviceVoipRTPStatusTransmitPacketLost_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 5, 2, 1, 29),
    _K3lDeviceVoipRTPStatusTransmitPacketLost_Type()
)
k3lDeviceVoipRTPStatusTransmitPacketLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceVoipRTPStatusTransmitPacketLost.setStatus("current")
_K3lDeviceVoipRTPStatusReceiveInitialSequenceNumber_Type = Gauge32
_K3lDeviceVoipRTPStatusReceiveInitialSequenceNumber_Object = MibTableColumn
k3lDeviceVoipRTPStatusReceiveInitialSequenceNumber = _K3lDeviceVoipRTPStatusReceiveInitialSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 5, 2, 1, 30),
    _K3lDeviceVoipRTPStatusReceiveInitialSequenceNumber_Type()
)
k3lDeviceVoipRTPStatusReceiveInitialSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceVoipRTPStatusReceiveInitialSequenceNumber.setStatus("current")
_K3lDeviceVoipRTPStatusReceiveLastSequenceNumber_Type = Gauge32
_K3lDeviceVoipRTPStatusReceiveLastSequenceNumber_Object = MibTableColumn
k3lDeviceVoipRTPStatusReceiveLastSequenceNumber = _K3lDeviceVoipRTPStatusReceiveLastSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 5, 2, 1, 31),
    _K3lDeviceVoipRTPStatusReceiveLastSequenceNumber_Type()
)
k3lDeviceVoipRTPStatusReceiveLastSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceVoipRTPStatusReceiveLastSequenceNumber.setStatus("current")
_K3lDeviceVoipRTPStatusReceivePacketCount_Type = Gauge32
_K3lDeviceVoipRTPStatusReceivePacketCount_Object = MibTableColumn
k3lDeviceVoipRTPStatusReceivePacketCount = _K3lDeviceVoipRTPStatusReceivePacketCount_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 5, 2, 1, 32),
    _K3lDeviceVoipRTPStatusReceivePacketCount_Type()
)
k3lDeviceVoipRTPStatusReceivePacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceVoipRTPStatusReceivePacketCount.setStatus("current")
_K3lDeviceVoipRTPStatusReceiveDroppedCount_Type = Gauge32
_K3lDeviceVoipRTPStatusReceiveDroppedCount_Object = MibTableColumn
k3lDeviceVoipRTPStatusReceiveDroppedCount = _K3lDeviceVoipRTPStatusReceiveDroppedCount_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 5, 2, 1, 33),
    _K3lDeviceVoipRTPStatusReceiveDroppedCount_Type()
)
k3lDeviceVoipRTPStatusReceiveDroppedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceVoipRTPStatusReceiveDroppedCount.setStatus("current")
_K3lDeviceVoipRTPStatusReceiveLastDroppedCount_Type = Gauge32
_K3lDeviceVoipRTPStatusReceiveLastDroppedCount_Object = MibTableColumn
k3lDeviceVoipRTPStatusReceiveLastDroppedCount = _K3lDeviceVoipRTPStatusReceiveLastDroppedCount_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 6, 5, 2, 1, 34),
    _K3lDeviceVoipRTPStatusReceiveLastDroppedCount_Type()
)
k3lDeviceVoipRTPStatusReceiveLastDroppedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceVoipRTPStatusReceiveLastDroppedCount.setStatus("current")
_K3lDeviceChannelGroupChannel_ObjectIdentity = ObjectIdentity
k3lDeviceChannelGroupChannel = _K3lDeviceChannelGroupChannel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 7)
)
_K3lDeviceChannelGroupTable_Object = MibTable
k3lDeviceChannelGroupTable = _K3lDeviceChannelGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 7, 1)
)
if mibBuilder.loadTexts:
    k3lDeviceChannelGroupTable.setStatus("current")
_K3lDeviceChannelGroupEntry_Object = MibTableRow
k3lDeviceChannelGroupEntry = _K3lDeviceChannelGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 7, 1, 1)
)
k3lDeviceChannelGroupEntry.setIndexNames(
    (0, "KHOMP-MIB", "k3lDeviceSerial"),
    (0, "KHOMP-MIB", "k3lDeviceChannelGroupIndex"),
)
if mibBuilder.loadTexts:
    k3lDeviceChannelGroupEntry.setStatus("current")
_K3lDeviceChannelGroupIndex_Type = KhompDeviceIndex
_K3lDeviceChannelGroupIndex_Object = MibTableColumn
k3lDeviceChannelGroupIndex = _K3lDeviceChannelGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 7, 1, 1, 1),
    _K3lDeviceChannelGroupIndex_Type()
)
k3lDeviceChannelGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    k3lDeviceChannelGroupIndex.setStatus("current")
_K3lDeviceChannelGroupType_Type = Unsigned32
_K3lDeviceChannelGroupType_Object = MibTableColumn
k3lDeviceChannelGroupType = _K3lDeviceChannelGroupType_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 7, 1, 1, 2),
    _K3lDeviceChannelGroupType_Type()
)
k3lDeviceChannelGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceChannelGroupType.setStatus("current")
_K3lDeviceChannelGroupFirstChannel_Type = Unsigned32
_K3lDeviceChannelGroupFirstChannel_Object = MibTableColumn
k3lDeviceChannelGroupFirstChannel = _K3lDeviceChannelGroupFirstChannel_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 7, 1, 1, 3),
    _K3lDeviceChannelGroupFirstChannel_Type()
)
k3lDeviceChannelGroupFirstChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceChannelGroupFirstChannel.setStatus("current")
_K3lDeviceChannelGroupChannelCount_Type = Gauge32
_K3lDeviceChannelGroupChannelCount_Object = MibTableColumn
k3lDeviceChannelGroupChannelCount = _K3lDeviceChannelGroupChannelCount_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 7, 1, 1, 4),
    _K3lDeviceChannelGroupChannelCount_Type()
)
k3lDeviceChannelGroupChannelCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceChannelGroupChannelCount.setStatus("current")
_K3lDeviceChannelGroupChannelIdle_Type = Gauge32
_K3lDeviceChannelGroupChannelIdle_Object = MibTableColumn
k3lDeviceChannelGroupChannelIdle = _K3lDeviceChannelGroupChannelIdle_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 7, 1, 1, 5),
    _K3lDeviceChannelGroupChannelIdle_Type()
)
k3lDeviceChannelGroupChannelIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceChannelGroupChannelIdle.setStatus("current")
_K3lDeviceChannelGroupChannelFail_Type = Gauge32
_K3lDeviceChannelGroupChannelFail_Object = MibTableColumn
k3lDeviceChannelGroupChannelFail = _K3lDeviceChannelGroupChannelFail_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 7, 1, 1, 6),
    _K3lDeviceChannelGroupChannelFail_Type()
)
k3lDeviceChannelGroupChannelFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceChannelGroupChannelFail.setStatus("current")
_K3lDeviceChannelGroupChannelBusy_Type = Gauge32
_K3lDeviceChannelGroupChannelBusy_Object = MibTableColumn
k3lDeviceChannelGroupChannelBusy = _K3lDeviceChannelGroupChannelBusy_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 2, 7, 1, 1, 7),
    _K3lDeviceChannelGroupChannelBusy_Type()
)
k3lDeviceChannelGroupChannelBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lDeviceChannelGroupChannelBusy.setStatus("current")
_K3lConsolidated_ObjectIdentity = ObjectIdentity
k3lConsolidated = _K3lConsolidated_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 3)
)
_K3lConsolidatedDevices_ObjectIdentity = ObjectIdentity
k3lConsolidatedDevices = _K3lConsolidatedDevices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 3, 1)
)
_K3lConsolidatedDevicesChannelCount_Type = Gauge32
_K3lConsolidatedDevicesChannelCount_Object = MibScalar
k3lConsolidatedDevicesChannelCount = _K3lConsolidatedDevicesChannelCount_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 3, 1, 1),
    _K3lConsolidatedDevicesChannelCount_Type()
)
k3lConsolidatedDevicesChannelCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lConsolidatedDevicesChannelCount.setStatus("current")
_K3lConsolidatedDevicesChannelCountEnabled_Type = Gauge32
_K3lConsolidatedDevicesChannelCountEnabled_Object = MibScalar
k3lConsolidatedDevicesChannelCountEnabled = _K3lConsolidatedDevicesChannelCountEnabled_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 3, 1, 2),
    _K3lConsolidatedDevicesChannelCountEnabled_Type()
)
k3lConsolidatedDevicesChannelCountEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lConsolidatedDevicesChannelCountEnabled.setStatus("current")
_K3lConsolidatedDevicesChannelCountIdle_Type = Gauge32
_K3lConsolidatedDevicesChannelCountIdle_Object = MibScalar
k3lConsolidatedDevicesChannelCountIdle = _K3lConsolidatedDevicesChannelCountIdle_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 3, 1, 3),
    _K3lConsolidatedDevicesChannelCountIdle_Type()
)
k3lConsolidatedDevicesChannelCountIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lConsolidatedDevicesChannelCountIdle.setStatus("current")
_K3lConsolidatedDevicesChannelCountFail_Type = Gauge32
_K3lConsolidatedDevicesChannelCountFail_Object = MibScalar
k3lConsolidatedDevicesChannelCountFail = _K3lConsolidatedDevicesChannelCountFail_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 3, 1, 4),
    _K3lConsolidatedDevicesChannelCountFail_Type()
)
k3lConsolidatedDevicesChannelCountFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lConsolidatedDevicesChannelCountFail.setStatus("current")
_K3lConsolidatedDevicesChannelCountBusy_Type = Gauge32
_K3lConsolidatedDevicesChannelCountBusy_Object = MibScalar
k3lConsolidatedDevicesChannelCountBusy = _K3lConsolidatedDevicesChannelCountBusy_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 3, 1, 5),
    _K3lConsolidatedDevicesChannelCountBusy_Type()
)
k3lConsolidatedDevicesChannelCountBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lConsolidatedDevicesChannelCountBusy.setStatus("current")
_K3lConfiguration_ObjectIdentity = ObjectIdentity
k3lConfiguration = _K3lConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 4)
)
_K3lConfigurationR2Country_Type = KhompR2Country
_K3lConfigurationR2Country_Object = MibScalar
k3lConfigurationR2Country = _K3lConfigurationR2Country_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 4, 1),
    _K3lConfigurationR2Country_Type()
)
k3lConfigurationR2Country.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lConfigurationR2Country.setStatus("current")
_K3lLicense_ObjectIdentity = ObjectIdentity
k3lLicense = _K3lLicense_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 5)
)
_K3lLicenseCount_Type = Gauge32
_K3lLicenseCount_Object = MibScalar
k3lLicenseCount = _K3lLicenseCount_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 5, 1),
    _K3lLicenseCount_Type()
)
k3lLicenseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lLicenseCount.setStatus("current")
_K3lLicenseTable_Object = MibTable
k3lLicenseTable = _K3lLicenseTable_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 5, 2)
)
if mibBuilder.loadTexts:
    k3lLicenseTable.setStatus("current")
_K3lLicenseEntry_Object = MibTableRow
k3lLicenseEntry = _K3lLicenseEntry_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 5, 2, 1)
)
k3lLicenseEntry.setIndexNames(
    (0, "KHOMP-MIB", "k3lLicenseID"),
)
if mibBuilder.loadTexts:
    k3lLicenseEntry.setStatus("current")
_K3lLicenseIndex_Type = Unsigned32
_K3lLicenseIndex_Object = MibTableColumn
k3lLicenseIndex = _K3lLicenseIndex_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 5, 2, 1, 1),
    _K3lLicenseIndex_Type()
)
k3lLicenseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lLicenseIndex.setStatus("current")
_K3lLicenseID_Type = KhompLicenseSerial
_K3lLicenseID_Object = MibTableColumn
k3lLicenseID = _K3lLicenseID_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 5, 2, 1, 2),
    _K3lLicenseID_Type()
)
k3lLicenseID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lLicenseID.setStatus("current")
_K3lLicenseHardwareType_Type = DisplayString
_K3lLicenseHardwareType_Object = MibTableColumn
k3lLicenseHardwareType = _K3lLicenseHardwareType_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 5, 2, 1, 3),
    _K3lLicenseHardwareType_Type()
)
k3lLicenseHardwareType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lLicenseHardwareType.setStatus("current")
_K3lLicenseSerial_Type = KhompLicenseSerial
_K3lLicenseSerial_Object = MibTableColumn
k3lLicenseSerial = _K3lLicenseSerial_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 5, 2, 1, 4),
    _K3lLicenseSerial_Type()
)
k3lLicenseSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lLicenseSerial.setStatus("current")
_K3lLicenseHardwareInfo_Type = DisplayString
_K3lLicenseHardwareInfo_Object = MibTableColumn
k3lLicenseHardwareInfo = _K3lLicenseHardwareInfo_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 5, 2, 1, 5),
    _K3lLicenseHardwareInfo_Type()
)
k3lLicenseHardwareInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lLicenseHardwareInfo.setStatus("current")
_K3lLicenseIssueDate_Type = DisplayString
_K3lLicenseIssueDate_Object = MibTableColumn
k3lLicenseIssueDate = _K3lLicenseIssueDate_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 5, 2, 1, 6),
    _K3lLicenseIssueDate_Type()
)
k3lLicenseIssueDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lLicenseIssueDate.setStatus("current")
_K3lLicenseExpirationDate_Type = DisplayString
_K3lLicenseExpirationDate_Object = MibTableColumn
k3lLicenseExpirationDate = _K3lLicenseExpirationDate_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 5, 2, 1, 7),
    _K3lLicenseExpirationDate_Type()
)
k3lLicenseExpirationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lLicenseExpirationDate.setStatus("current")
_K3lLicenseCustomerInfo_Type = DisplayString
_K3lLicenseCustomerInfo_Object = MibTableColumn
k3lLicenseCustomerInfo = _K3lLicenseCustomerInfo_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 5, 2, 1, 8),
    _K3lLicenseCustomerInfo_Type()
)
k3lLicenseCustomerInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lLicenseCustomerInfo.setStatus("current")
_K3lLicenseIssuer_Type = DisplayString
_K3lLicenseIssuer_Object = MibTableColumn
k3lLicenseIssuer = _K3lLicenseIssuer_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 5, 2, 1, 9),
    _K3lLicenseIssuer_Type()
)
k3lLicenseIssuer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lLicenseIssuer.setStatus("current")
_K3lLicenseNumResourceTypes_Type = Gauge32
_K3lLicenseNumResourceTypes_Object = MibTableColumn
k3lLicenseNumResourceTypes = _K3lLicenseNumResourceTypes_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 5, 2, 1, 10),
    _K3lLicenseNumResourceTypes_Type()
)
k3lLicenseNumResourceTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lLicenseNumResourceTypes.setStatus("current")
_K3lLicenseDescr_Type = DisplayString
_K3lLicenseDescr_Object = MibTableColumn
k3lLicenseDescr = _K3lLicenseDescr_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 5, 2, 1, 11),
    _K3lLicenseDescr_Type()
)
k3lLicenseDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lLicenseDescr.setStatus("current")
_K3lLicenseResourceRequiredTable_Object = MibTable
k3lLicenseResourceRequiredTable = _K3lLicenseResourceRequiredTable_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 5, 3)
)
if mibBuilder.loadTexts:
    k3lLicenseResourceRequiredTable.setStatus("current")
_K3lLicenseResourceRequiredEntry_Object = MibTableRow
k3lLicenseResourceRequiredEntry = _K3lLicenseResourceRequiredEntry_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 5, 3, 1)
)
k3lLicenseResourceRequiredEntry.setIndexNames(
    (0, "KHOMP-MIB", "k3lLicenseID"),
    (0, "KHOMP-MIB", "k3lLicenseResourceType"),
)
if mibBuilder.loadTexts:
    k3lLicenseResourceRequiredEntry.setStatus("current")
_K3lLicenseResourceRequiredIndex_Type = Unsigned32
_K3lLicenseResourceRequiredIndex_Object = MibTableColumn
k3lLicenseResourceRequiredIndex = _K3lLicenseResourceRequiredIndex_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 5, 3, 1, 1),
    _K3lLicenseResourceRequiredIndex_Type()
)
k3lLicenseResourceRequiredIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    k3lLicenseResourceRequiredIndex.setStatus("current")
_K3lLicenseResourceRequiredType_Type = KhompLicenseResourceType
_K3lLicenseResourceRequiredType_Object = MibTableColumn
k3lLicenseResourceRequiredType = _K3lLicenseResourceRequiredType_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 5, 3, 1, 2),
    _K3lLicenseResourceRequiredType_Type()
)
k3lLicenseResourceRequiredType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lLicenseResourceRequiredType.setStatus("current")
_K3lLicenseResourceRequired_Type = Gauge32
_K3lLicenseResourceRequired_Object = MibTableColumn
k3lLicenseResourceRequired = _K3lLicenseResourceRequired_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 5, 3, 1, 3),
    _K3lLicenseResourceRequired_Type()
)
k3lLicenseResourceRequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lLicenseResourceRequired.setStatus("current")
_K3lLicenseResource_ObjectIdentity = ObjectIdentity
k3lLicenseResource = _K3lLicenseResource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 5, 4)
)
_K3lLicenseResourceCount_Type = Gauge32
_K3lLicenseResourceCount_Object = MibScalar
k3lLicenseResourceCount = _K3lLicenseResourceCount_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 5, 4, 1),
    _K3lLicenseResourceCount_Type()
)
k3lLicenseResourceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lLicenseResourceCount.setStatus("current")
_K3lLicenseResourceTable_Object = MibTable
k3lLicenseResourceTable = _K3lLicenseResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 5, 4, 2)
)
if mibBuilder.loadTexts:
    k3lLicenseResourceTable.setStatus("current")
_K3lLicenseResourceEntry_Object = MibTableRow
k3lLicenseResourceEntry = _K3lLicenseResourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 5, 4, 2, 1)
)
k3lLicenseResourceEntry.setIndexNames(
    (0, "KHOMP-MIB", "k3lLicenseResourceType"),
)
if mibBuilder.loadTexts:
    k3lLicenseResourceEntry.setStatus("current")
_K3lLicenseResourceIndex_Type = Unsigned32
_K3lLicenseResourceIndex_Object = MibTableColumn
k3lLicenseResourceIndex = _K3lLicenseResourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 5, 4, 2, 1, 1),
    _K3lLicenseResourceIndex_Type()
)
k3lLicenseResourceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    k3lLicenseResourceIndex.setStatus("current")
_K3lLicenseResourceType_Type = KhompLicenseResourceType
_K3lLicenseResourceType_Object = MibTableColumn
k3lLicenseResourceType = _K3lLicenseResourceType_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 5, 4, 2, 1, 2),
    _K3lLicenseResourceType_Type()
)
k3lLicenseResourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lLicenseResourceType.setStatus("current")
_K3lLicenseResourceName_Type = DisplayString
_K3lLicenseResourceName_Object = MibTableColumn
k3lLicenseResourceName = _K3lLicenseResourceName_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 5, 4, 2, 1, 3),
    _K3lLicenseResourceName_Type()
)
k3lLicenseResourceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lLicenseResourceName.setStatus("current")
_K3lLicenseResourcesTotal_Type = Gauge32
_K3lLicenseResourcesTotal_Object = MibTableColumn
k3lLicenseResourcesTotal = _K3lLicenseResourcesTotal_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 5, 4, 2, 1, 4),
    _K3lLicenseResourcesTotal_Type()
)
k3lLicenseResourcesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lLicenseResourcesTotal.setStatus("current")
_K3lLicenseResourcesTotalActive_Type = Gauge32
_K3lLicenseResourcesTotalActive_Object = MibTableColumn
k3lLicenseResourcesTotalActive = _K3lLicenseResourcesTotalActive_Object(
    (1, 3, 6, 1, 4, 1, 32624, 2, 1, 5, 4, 2, 1, 5),
    _K3lLicenseResourcesTotalActive_Type()
)
k3lLicenseResourcesTotalActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    k3lLicenseResourcesTotalActive.setStatus("current")
_K3lMIBConformance_ObjectIdentity = ObjectIdentity
k3lMIBConformance = _K3lMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32624, 2, 2)
)
_K3lMIBCompliances_ObjectIdentity = ObjectIdentity
k3lMIBCompliances = _K3lMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32624, 2, 2, 1)
)
_K3lMIBGroups_ObjectIdentity = ObjectIdentity
k3lMIBGroups = _K3lMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32624, 2, 2, 2)
)
_K3lDeviceGroups_ObjectIdentity = ObjectIdentity
k3lDeviceGroups = _K3lDeviceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32624, 2, 2, 2, 2)
)
_K3lDeviceLinkGroups_ObjectIdentity = ObjectIdentity
k3lDeviceLinkGroups = _K3lDeviceLinkGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32624, 2, 2, 2, 3)
)
_K3lDeviceChannelGroups_ObjectIdentity = ObjectIdentity
k3lDeviceChannelGroups = _K3lDeviceChannelGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32624, 2, 2, 2, 4)
)
_K3lDeviceCallInfoGroups_ObjectIdentity = ObjectIdentity
k3lDeviceCallInfoGroups = _K3lDeviceCallInfoGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32624, 2, 2, 2, 5)
)
_K3lConsolidatedGroups_ObjectIdentity = ObjectIdentity
k3lConsolidatedGroups = _K3lConsolidatedGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32624, 2, 2, 2, 6)
)
_K3lLicenseGroups_ObjectIdentity = ObjectIdentity
k3lLicenseGroups = _K3lLicenseGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32624, 2, 2, 2, 8)
)
_App_ObjectIdentity = ObjectIdentity
app = _App_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32624, 3)
)

# Managed Objects groups

k3lRootGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 32624, 2, 2, 2, 1)
)
k3lRootGroup.setObjects(
      *(("KHOMP-MIB", "k3lVersionMajor"),
        ("KHOMP-MIB", "k3lVersionMinor"),
        ("KHOMP-MIB", "k3lVersionBuild"),
        ("KHOMP-MIB", "k3lVersionRevision"),
        ("KHOMP-MIB", "k3lVersionString"),
        ("KHOMP-MIB", "k3lDeviceCount"))
)
if mibBuilder.loadTexts:
    k3lRootGroup.setStatus("current")

k3lDeviceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 32624, 2, 2, 2, 2, 1)
)
k3lDeviceGroup.setObjects(
      *(("KHOMP-MIB", "k3lDeviceSerial"),
        ("KHOMP-MIB", "k3lDeviceIndex"),
        ("KHOMP-MIB", "k3lDeviceDescr"),
        ("KHOMP-MIB", "k3lDeviceModel"),
        ("KHOMP-MIB", "k3lDeviceOperStatus"),
        ("KHOMP-MIB", "k3lDeviceType"),
        ("KHOMP-MIB", "k3lDeviceLinkCount"),
        ("KHOMP-MIB", "k3lDeviceChannelCount"),
        ("KHOMP-MIB", "k3lDeviceChannelCountEnabled"),
        ("KHOMP-MIB", "k3lDeviceChannelCountIdle"),
        ("KHOMP-MIB", "k3lDeviceChannelCountFail"),
        ("KHOMP-MIB", "k3lDeviceChannelCountBusy"),
        ("KHOMP-MIB", "k3lDeviceReset"),
        ("KHOMP-MIB", "k3lDeviceChannelGroupCount"),
        ("KHOMP-MIB", "k3lDeviceStatsIncoming"),
        ("KHOMP-MIB", "k3lDeviceStatsOutgoing"),
        ("KHOMP-MIB", "k3lDeviceOutgoingCompleted"),
        ("KHOMP-MIB", "k3lDeviceOutgoingError"),
        ("KHOMP-MIB", "k3lDeviceRemoteDisconnect"),
        ("KHOMP-MIB", "k3lDeviceLocalDisconnect"),
        ("KHOMP-MIB", "k3lDeviceCallFailBusy"),
        ("KHOMP-MIB", "k3lDeviceCallFailNoAnswer"),
        ("KHOMP-MIB", "k3lDeviceCallFailRejected"),
        ("KHOMP-MIB", "k3lDeviceCallFailChangedNumber"),
        ("KHOMP-MIB", "k3lDeviceCallFailInvalidNumber"),
        ("KHOMP-MIB", "k3lDeviceCallFailOutOfService"),
        ("KHOMP-MIB", "k3lDeviceCallFailCongestion"),
        ("KHOMP-MIB", "k3lDeviceCallFailNetworkFailure"),
        ("KHOMP-MIB", "k3lDeviceCallFailOther"),
        ("KHOMP-MIB", "k3lDeviceEbsIP"))
)
if mibBuilder.loadTexts:
    k3lDeviceGroup.setStatus("current")

k3lDeviceLinkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 32624, 2, 2, 2, 3, 1)
)
k3lDeviceLinkGroup.setObjects(
      *(("KHOMP-MIB", "k3lDeviceLinkOperStatus"),
        ("KHOMP-MIB", "k3lDeviceLinkSignaling"),
        ("KHOMP-MIB", "k3lDeviceLinkDescr"),
        ("KHOMP-MIB", "k3lDeviceLinkAlarm"),
        ("KHOMP-MIB", "k3lDeviceLinkErrorCountChangesToLock"),
        ("KHOMP-MIB", "k3lDeviceLinkErrorCountLostOfSignal"),
        ("KHOMP-MIB", "k3lDeviceLinkErrorCountAlarmNotification"),
        ("KHOMP-MIB", "k3lDeviceLinkErrorCountLostOfFrame"),
        ("KHOMP-MIB", "k3lDeviceLinkErrorCountLostOfMultiframe"),
        ("KHOMP-MIB", "k3lDeviceLinkErrorCountRemoteAlarm"),
        ("KHOMP-MIB", "k3lDeviceLinkErrorCountSlipAlarm"),
        ("KHOMP-MIB", "k3lDeviceLinkErrorCountPRBS"),
        ("KHOMP-MIB", "k3lDeviceLinkErrorCountWrongEBits"),
        ("KHOMP-MIB", "k3lDeviceLinkErrorCountJitterVariation"),
        ("KHOMP-MIB", "k3lDeviceLinkErrorCountFramesWithoutSync"),
        ("KHOMP-MIB", "k3lDeviceLinkErrorCountMultiframeSignal"),
        ("KHOMP-MIB", "k3lDeviceLinkErrorCountFrameError"),
        ("KHOMP-MIB", "k3lDeviceLinkErrorCountBipolarViolation"),
        ("KHOMP-MIB", "k3lDeviceLinkErrorCountCRC4"),
        ("KHOMP-MIB", "k3lDeviceLinkReset"),
        ("KHOMP-MIB", "k3lDeviceLinkResetErrorCount"),
        ("KHOMP-MIB", "k3lDeviceLinkBlock"),
        ("KHOMP-MIB", "k3lDeviceLinkChannelCount"),
        ("KHOMP-MIB", "k3lDeviceLinkChannelCountEnabled"),
        ("KHOMP-MIB", "k3lDeviceLinkChannelCountIdle"),
        ("KHOMP-MIB", "k3lDeviceLinkChannelCountFail"),
        ("KHOMP-MIB", "k3lDeviceLinkChannelCountBusy"),
        ("KHOMP-MIB", "k3lDeviceLinkReceivingClock"),
        ("KHOMP-MIB", "k3lDeviceLinkStatsIncoming"),
        ("KHOMP-MIB", "k3lDeviceLinkStatsOutgoing"),
        ("KHOMP-MIB", "k3lDeviceLinkOutgoingCompleted"),
        ("KHOMP-MIB", "k3lDeviceLinkOutgoingError"),
        ("KHOMP-MIB", "k3lDeviceLinkRemoteDisconnect"),
        ("KHOMP-MIB", "k3lDeviceLinkLocalDisconnect"),
        ("KHOMP-MIB", "k3lDeviceLinkCallFailBusy"),
        ("KHOMP-MIB", "k3lDeviceLinkCallFailNoAnswer"),
        ("KHOMP-MIB", "k3lDeviceLinkCallFailRejected"),
        ("KHOMP-MIB", "k3lDeviceLinkCallFailChangedNumber"),
        ("KHOMP-MIB", "k3lDeviceLinkCallFailInvalidNumber"),
        ("KHOMP-MIB", "k3lDeviceLinkCallFailOutOfService"),
        ("KHOMP-MIB", "k3lDeviceLinkCallFailCongestion"),
        ("KHOMP-MIB", "k3lDeviceLinkCallFailNetworkFailure"),
        ("KHOMP-MIB", "k3lDeviceLinkCallFailOther"),
        ("KHOMP-MIB", "k3lDeviceLinkOperatingMode"))
)
if mibBuilder.loadTexts:
    k3lDeviceLinkGroup.setStatus("current")

k3lDeviceHILinkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 32624, 2, 2, 2, 3, 2)
)
k3lDeviceHILinkGroup.setObjects(
      *(("KHOMP-MIB", "k3lDeviceHILinkOperStatus"),
        ("KHOMP-MIB", "k3lDeviceHILinkAlarm"))
)
if mibBuilder.loadTexts:
    k3lDeviceHILinkGroup.setStatus("current")

k3lDeviceChannelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 32624, 2, 2, 2, 4, 1)
)
k3lDeviceChannelGroup.setObjects(
      *(("KHOMP-MIB", "k3lDeviceChannelSignaling"),
        ("KHOMP-MIB", "k3lDeviceChannelCallStatus"),
        ("KHOMP-MIB", "k3lDeviceChannelAudioStatus"),
        ("KHOMP-MIB", "k3lDeviceChannelEnabledFeatures"),
        ("KHOMP-MIB", "k3lDeviceChannelStatsIncoming"),
        ("KHOMP-MIB", "k3lDeviceChannelStatsOutgoing"),
        ("KHOMP-MIB", "k3lDeviceChannelStatsOutgoingCompleted"),
        ("KHOMP-MIB", "k3lDeviceChannelStatsOutgoingError"),
        ("KHOMP-MIB", "k3lDeviceChannelStatsRemoteDisconnect"),
        ("KHOMP-MIB", "k3lDeviceChannelStatsLocalDisconnect"),
        ("KHOMP-MIB", "k3lDeviceChannelStatsCallFailBusy"),
        ("KHOMP-MIB", "k3lDeviceChannelStatsCallFailNoAnswer"),
        ("KHOMP-MIB", "k3lDeviceChannelStatsCallFailRejected"),
        ("KHOMP-MIB", "k3lDeviceChannelStatsCallFailChangedNumber"),
        ("KHOMP-MIB", "k3lDeviceChannelStatsCallFailInvalidNumber"),
        ("KHOMP-MIB", "k3lDeviceChannelStatsCallFailOutOfService"),
        ("KHOMP-MIB", "k3lDeviceChannelStatsCallFailCongestion"),
        ("KHOMP-MIB", "k3lDeviceChannelStatsCallFailNetworkFailure"),
        ("KHOMP-MIB", "k3lDeviceChannelStatsCallFailOther"),
        ("KHOMP-MIB", "k3lDeviceChannelDestinationAddress"),
        ("KHOMP-MIB", "k3lDeviceChannelCallDuration"),
        ("KHOMP-MIB", "k3lDeviceChannelRecording"),
        ("KHOMP-MIB", "k3lDeviceChannelAverageCallTime"),
        ("KHOMP-MIB", "k3lDeviceChannelOriginAddress"),
        ("KHOMP-MIB", "k3lDeviceChannelCadenceStatus"))
)
if mibBuilder.loadTexts:
    k3lDeviceChannelGroup.setStatus("current")

k3lDeviceE1ChannelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 32624, 2, 2, 2, 4, 2)
)
k3lDeviceE1ChannelGroup.setObjects(
      *(("KHOMP-MIB", "k3lDeviceE1ChannelCount"),
        ("KHOMP-MIB", "k3lDeviceE1ChannelStatus"))
)
if mibBuilder.loadTexts:
    k3lDeviceE1ChannelGroup.setStatus("current")

k3lDeviceFxoChannelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 32624, 2, 2, 2, 4, 3)
)
k3lDeviceFxoChannelGroup.setObjects(
      *(("KHOMP-MIB", "k3lDeviceFxoChannelCount"),
        ("KHOMP-MIB", "k3lDeviceFxoChannelStatus"))
)
if mibBuilder.loadTexts:
    k3lDeviceFxoChannelGroup.setStatus("current")

k3lDeviceFxsChannelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 32624, 2, 2, 2, 4, 4)
)
k3lDeviceFxsChannelGroup.setObjects(
      *(("KHOMP-MIB", "k3lDeviceFxsChannelCount"),
        ("KHOMP-MIB", "k3lDeviceFxsChannelStatus"))
)
if mibBuilder.loadTexts:
    k3lDeviceFxsChannelGroup.setStatus("current")

k3lDeviceGsmChannelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 32624, 2, 2, 2, 4, 5)
)
k3lDeviceGsmChannelGroup.setObjects(
      *(("KHOMP-MIB", "k3lDeviceGsmChannelCount"),
        ("KHOMP-MIB", "k3lDeviceGsmChannelStatus"),
        ("KHOMP-MIB", "k3lDeviceGsmChannelSignalStrength"),
        ("KHOMP-MIB", "k3lDeviceGsmChannelErrorRate"),
        ("KHOMP-MIB", "k3lDeviceGsmChannelRegistryStatus"),
        ("KHOMP-MIB", "k3lDeviceGsmChannelOperName"),
        ("KHOMP-MIB", "k3lDeviceGsmChannelUnreadSmsMessages"),
        ("KHOMP-MIB", "k3lDeviceGsmChannelEnabledFeatures"),
        ("KHOMP-MIB", "k3lDeviceGsmChannelImei"),
        ("KHOMP-MIB", "k3lDeviceGsmChannelSim"),
        ("KHOMP-MIB", "k3lDeviceGsmChannelImsi"),
        ("KHOMP-MIB", "k3lDeviceGsmChannelIccid"),
        ("KHOMP-MIB", "k3lDeviceGsmChannelMsisdn"),
        ("KHOMP-MIB", "k3lDeviceGsmChannelCallWaiting"),
        ("KHOMP-MIB", "k3lDeviceGsmChannelSimCardCount"))
)
if mibBuilder.loadTexts:
    k3lDeviceGsmChannelGroup.setStatus("current")

k3lDeviceSipChannelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 32624, 2, 2, 2, 4, 6)
)
k3lDeviceSipChannelGroup.setObjects(
      *(("KHOMP-MIB", "k3lDeviceSipChannelCount"),
        ("KHOMP-MIB", "k3lDeviceSipChannelStatus"),
        ("KHOMP-MIB", "k3lDeviceVoipProfileLocalAddress"),
        ("KHOMP-MIB", "k3lDeviceVoipProfileLocalPort"),
        ("KHOMP-MIB", "k3lDeviceVoipProfileTransportType"),
        ("KHOMP-MIB", "k3lDeviceVoipProfileRTPAddress"),
        ("KHOMP-MIB", "k3lDeviceVoipProfileUser"),
        ("KHOMP-MIB", "k3lDeviceVoipProfileAuthorizationUser"),
        ("KHOMP-MIB", "k3lDeviceVoipProfileRealm"),
        ("KHOMP-MIB", "k3lDeviceVoipProfileDomain"),
        ("KHOMP-MIB", "k3lDeviceVoipProfileDomainPort"),
        ("KHOMP-MIB", "k3lDeviceVoipProfileProxy"),
        ("KHOMP-MIB", "k3lDeviceVoipProfileProxyPort"),
        ("KHOMP-MIB", "k3lDeviceVoipProfileRegistered"),
        ("KHOMP-MIB", "k3lDeviceVoipChannelTransactionCount"),
        ("KHOMP-MIB", "k3lDeviceVoipChannelClientTransactionCount"),
        ("KHOMP-MIB", "k3lDeviceVoipChannelServerTransactionCount"),
        ("KHOMP-MIB", "k3lDeviceVoipChannelClientTransactionFailureCount"),
        ("KHOMP-MIB", "k3lDeviceVoipChannelServerTransactionFailureCount"),
        ("KHOMP-MIB", "k3lDeviceVoipChannelClientTransactionFailure4xxCount"),
        ("KHOMP-MIB", "k3lDeviceVoipChannelServerTransactionFailure4xxCount"),
        ("KHOMP-MIB", "k3lDeviceVoipChannelClientTransactionFailure5xxCount"),
        ("KHOMP-MIB", "k3lDeviceVoipChannelServerTransactionFailure5xxCount"),
        ("KHOMP-MIB", "k3lDeviceVoipChannelClientTransactionFailure6xxCount"),
        ("KHOMP-MIB", "k3lDeviceVoipChannelServerTransactionFailure6xxCount"),
        ("KHOMP-MIB", "k3lDeviceVoipRTPStatusTransmitLastSequenceNumber"),
        ("KHOMP-MIB", "k3lDeviceVoipRTPStatusTransmitPacketCount"),
        ("KHOMP-MIB", "k3lDeviceVoipRTPStatusTransmitOctetCount"),
        ("KHOMP-MIB", "k3lDeviceVoipRTPStatusTransmitPacketLost"),
        ("KHOMP-MIB", "k3lDeviceVoipRTPStatusReceiveInitialSequenceNumber"),
        ("KHOMP-MIB", "k3lDeviceVoipRTPStatusReceiveLastSequenceNumber"),
        ("KHOMP-MIB", "k3lDeviceVoipRTPStatusReceivePacketCount"),
        ("KHOMP-MIB", "k3lDeviceVoipRTPStatusReceiveDroppedCount"),
        ("KHOMP-MIB", "k3lDeviceVoipRTPStatusReceiveLastDroppedCount"))
)
if mibBuilder.loadTexts:
    k3lDeviceSipChannelGroup.setStatus("current")

k3lDeviceChannelGroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 32624, 2, 2, 2, 4, 7)
)
k3lDeviceChannelGroupGroup.setObjects(
      *(("KHOMP-MIB", "k3lDeviceChannelGroupType"),
        ("KHOMP-MIB", "k3lDeviceChannelGroupFirstChannel"),
        ("KHOMP-MIB", "k3lDeviceChannelGroupChannelCount"),
        ("KHOMP-MIB", "k3lDeviceChannelGroupChannelIdle"),
        ("KHOMP-MIB", "k3lDeviceChannelGroupChannelFail"),
        ("KHOMP-MIB", "k3lDeviceChannelGroupChannelBusy"))
)
if mibBuilder.loadTexts:
    k3lDeviceChannelGroupGroup.setStatus("current")

k3lDeviceGsmCallGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 32624, 2, 2, 2, 5, 1)
)
k3lDeviceGsmCallGroup.setObjects(
      *(("KHOMP-MIB", "k3lDeviceGsmCallStatus"),
        ("KHOMP-MIB", "k3lDeviceGsmCallMode"),
        ("KHOMP-MIB", "k3lDeviceGsmCallNumber"),
        ("KHOMP-MIB", "k3lDeviceGsmCallFlags"))
)
if mibBuilder.loadTexts:
    k3lDeviceGsmCallGroup.setStatus("current")

k3lConsolidatedDevicesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 32624, 2, 2, 2, 6, 1)
)
k3lConsolidatedDevicesGroup.setObjects(
      *(("KHOMP-MIB", "k3lConsolidatedDevicesChannelCount"),
        ("KHOMP-MIB", "k3lConsolidatedDevicesChannelCountEnabled"),
        ("KHOMP-MIB", "k3lConsolidatedDevicesChannelCountIdle"),
        ("KHOMP-MIB", "k3lConsolidatedDevicesChannelCountFail"),
        ("KHOMP-MIB", "k3lConsolidatedDevicesChannelCountBusy"))
)
if mibBuilder.loadTexts:
    k3lConsolidatedDevicesGroup.setStatus("current")

k3lConfigurationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 32624, 2, 2, 2, 7)
)
k3lConfigurationGroup.setObjects(
    ("KHOMP-MIB", "k3lConfigurationR2Country")
)
if mibBuilder.loadTexts:
    k3lConfigurationGroup.setStatus("current")

k3lLicenseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 32624, 2, 2, 2, 8, 1)
)
k3lLicenseGroup.setObjects(
      *(("KHOMP-MIB", "k3lLicenseCount"),
        ("KHOMP-MIB", "k3lLicenseIndex"),
        ("KHOMP-MIB", "k3lLicenseID"),
        ("KHOMP-MIB", "k3lLicenseHardwareType"),
        ("KHOMP-MIB", "k3lLicenseSerial"),
        ("KHOMP-MIB", "k3lLicenseHardwareInfo"),
        ("KHOMP-MIB", "k3lLicenseIssueDate"),
        ("KHOMP-MIB", "k3lLicenseExpirationDate"),
        ("KHOMP-MIB", "k3lLicenseCustomerInfo"),
        ("KHOMP-MIB", "k3lLicenseIssuer"),
        ("KHOMP-MIB", "k3lLicenseNumResourceTypes"),
        ("KHOMP-MIB", "k3lLicenseDescr"))
)
if mibBuilder.loadTexts:
    k3lLicenseGroup.setStatus("current")

k3lLicenseResourceRequiredGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 32624, 2, 2, 2, 8, 2)
)
k3lLicenseResourceRequiredGroup.setObjects(
      *(("KHOMP-MIB", "k3lLicenseResourceRequiredType"),
        ("KHOMP-MIB", "k3lLicenseResourceRequired"))
)
if mibBuilder.loadTexts:
    k3lLicenseResourceRequiredGroup.setStatus("current")

k3lLicenseResourceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 32624, 2, 2, 2, 8, 3)
)
k3lLicenseResourceGroup.setObjects(
      *(("KHOMP-MIB", "k3lLicenseResourceCount"),
        ("KHOMP-MIB", "k3lLicenseResourceType"),
        ("KHOMP-MIB", "k3lLicenseResourceName"),
        ("KHOMP-MIB", "k3lLicenseResourcesTotal"),
        ("KHOMP-MIB", "k3lLicenseResourcesTotalActive"))
)
if mibBuilder.loadTexts:
    k3lLicenseResourceGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

k3lFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 32624, 2, 2, 1, 1)
)
k3lFullCompliance.setObjects(
      *(("KHOMP-MIB", "k3lRootGroup"),
        ("KHOMP-MIB", "k3lDeviceGroup"),
        ("KHOMP-MIB", "k3lDeviceLinkGroup"),
        ("KHOMP-MIB", "k3lDeviceHILinkGroup"),
        ("KHOMP-MIB", "k3lDeviceChannelGroup"),
        ("KHOMP-MIB", "k3lDeviceE1ChannelGroup"),
        ("KHOMP-MIB", "k3lDeviceFxoChannelGroup"),
        ("KHOMP-MIB", "k3lDeviceFxsChannelGroup"),
        ("KHOMP-MIB", "k3lDeviceGsmChannelGroup"),
        ("KHOMP-MIB", "k3lDeviceSipChannelGroup"),
        ("KHOMP-MIB", "k3lDeviceGsmCallGroup"),
        ("KHOMP-MIB", "k3lConsolidatedDevicesGroup"),
        ("KHOMP-MIB", "k3lDeviceChannelGroupGroup"),
        ("KHOMP-MIB", "k3lConfigurationGroup"),
        ("KHOMP-MIB", "k3lLicenseGroup"),
        ("KHOMP-MIB", "k3lLicenseResourceRequiredGroup"),
        ("KHOMP-MIB", "k3lLicenseResourceGroup"))
)
if mibBuilder.loadTexts:
    k3lFullCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "KHOMP-MIB",
    **{"KhompSignaling": KhompSignaling,
       "KhompOperStatus": KhompOperStatus,
       "KhompBoolean": KhompBoolean,
       "KhompDeviceIndex": KhompDeviceIndex,
       "KhompDeviceSerial": KhompDeviceSerial,
       "KhompUnsigned16": KhompUnsigned16,
       "KhompDeviceType": KhompDeviceType,
       "KhompDeviceChannelGroup": KhompDeviceChannelGroup,
       "KhompDeviceLinkIndex": KhompDeviceLinkIndex,
       "KhompDeviceLinkAlarm": KhompDeviceLinkAlarm,
       "KhompDeviceChannelIndex": KhompDeviceChannelIndex,
       "KhompDeviceChannelCallStatus": KhompDeviceChannelCallStatus,
       "KhompDeviceChannelAudioStatus": KhompDeviceChannelAudioStatus,
       "KhompDeviceChannelFeatures": KhompDeviceChannelFeatures,
       "KhompDeviceE1ChannelStatus": KhompDeviceE1ChannelStatus,
       "KhompDeviceFxoChannelStatus": KhompDeviceFxoChannelStatus,
       "KhompDeviceFxsChannelStatus": KhompDeviceFxsChannelStatus,
       "KhompDeviceGsmChannelStatus": KhompDeviceGsmChannelStatus,
       "KhompDeviceGsmChannelRegistryStatus": KhompDeviceGsmChannelRegistryStatus,
       "KhompDeviceGsmChannelEnabledFeatures": KhompDeviceGsmChannelEnabledFeatures,
       "KhompDeviceGsmChannelCallWaitingState": KhompDeviceGsmChannelCallWaitingState,
       "KhompDeviceGsmCallIndex": KhompDeviceGsmCallIndex,
       "KhompDeviceGsmCallStatus": KhompDeviceGsmCallStatus,
       "KhompDeviceGsmCallMode": KhompDeviceGsmCallMode,
       "KhompDeviceGsmCallFlags": KhompDeviceGsmCallFlags,
       "KhompDeviceSipChannelStatus": KhompDeviceSipChannelStatus,
       "KhompR2Country": KhompR2Country,
       "KhompLinkOperatingMode": KhompLinkOperatingMode,
       "KhompLicenseSerial": KhompLicenseSerial,
       "KhompLicenseResourceType": KhompLicenseResourceType,
       "khomp": khomp,
       "legacy": legacy,
       "k3l": k3l,
       "k3lMIBObjects": k3lMIBObjects,
       "k3lVersion": k3lVersion,
       "k3lVersionMajor": k3lVersionMajor,
       "k3lVersionMinor": k3lVersionMinor,
       "k3lVersionBuild": k3lVersionBuild,
       "k3lVersionRevision": k3lVersionRevision,
       "k3lVersionString": k3lVersionString,
       "k3lDevice": k3lDevice,
       "k3lDeviceCount": k3lDeviceCount,
       "k3lDeviceTable": k3lDeviceTable,
       "k3lDeviceEntry": k3lDeviceEntry,
       "k3lDeviceSerial": k3lDeviceSerial,
       "k3lDeviceIndex": k3lDeviceIndex,
       "k3lDeviceDescr": k3lDeviceDescr,
       "k3lDeviceOperStatus": k3lDeviceOperStatus,
       "k3lDeviceType": k3lDeviceType,
       "k3lDeviceModel": k3lDeviceModel,
       "k3lDeviceLinkCount": k3lDeviceLinkCount,
       "k3lDeviceChannelCount": k3lDeviceChannelCount,
       "k3lDeviceChannelCountEnabled": k3lDeviceChannelCountEnabled,
       "k3lDeviceChannelCountIdle": k3lDeviceChannelCountIdle,
       "k3lDeviceChannelCountFail": k3lDeviceChannelCountFail,
       "k3lDeviceChannelCountBusy": k3lDeviceChannelCountBusy,
       "k3lDeviceReset": k3lDeviceReset,
       "k3lDeviceChannelGroupCount": k3lDeviceChannelGroupCount,
       "k3lDeviceStatsIncoming": k3lDeviceStatsIncoming,
       "k3lDeviceStatsOutgoing": k3lDeviceStatsOutgoing,
       "k3lDeviceOutgoingCompleted": k3lDeviceOutgoingCompleted,
       "k3lDeviceOutgoingError": k3lDeviceOutgoingError,
       "k3lDeviceRemoteDisconnect": k3lDeviceRemoteDisconnect,
       "k3lDeviceLocalDisconnect": k3lDeviceLocalDisconnect,
       "k3lDeviceCallFailBusy": k3lDeviceCallFailBusy,
       "k3lDeviceCallFailNoAnswer": k3lDeviceCallFailNoAnswer,
       "k3lDeviceCallFailRejected": k3lDeviceCallFailRejected,
       "k3lDeviceCallFailChangedNumber": k3lDeviceCallFailChangedNumber,
       "k3lDeviceCallFailInvalidNumber": k3lDeviceCallFailInvalidNumber,
       "k3lDeviceCallFailOutOfService": k3lDeviceCallFailOutOfService,
       "k3lDeviceCallFailCongestion": k3lDeviceCallFailCongestion,
       "k3lDeviceCallFailNetworkFailure": k3lDeviceCallFailNetworkFailure,
       "k3lDeviceCallFailOther": k3lDeviceCallFailOther,
       "k3lDeviceEbsIP": k3lDeviceEbsIP,
       "k3lDeviceLinkTable": k3lDeviceLinkTable,
       "k3lDeviceLinkEntry": k3lDeviceLinkEntry,
       "k3lDeviceLinkIndex": k3lDeviceLinkIndex,
       "k3lDeviceLinkOperStatus": k3lDeviceLinkOperStatus,
       "k3lDeviceLinkDescr": k3lDeviceLinkDescr,
       "k3lDeviceLinkSignaling": k3lDeviceLinkSignaling,
       "k3lDeviceLinkAlarm": k3lDeviceLinkAlarm,
       "k3lDeviceLinkErrorCountChangesToLock": k3lDeviceLinkErrorCountChangesToLock,
       "k3lDeviceLinkErrorCountLostOfSignal": k3lDeviceLinkErrorCountLostOfSignal,
       "k3lDeviceLinkErrorCountAlarmNotification": k3lDeviceLinkErrorCountAlarmNotification,
       "k3lDeviceLinkErrorCountLostOfFrame": k3lDeviceLinkErrorCountLostOfFrame,
       "k3lDeviceLinkErrorCountLostOfMultiframe": k3lDeviceLinkErrorCountLostOfMultiframe,
       "k3lDeviceLinkErrorCountRemoteAlarm": k3lDeviceLinkErrorCountRemoteAlarm,
       "k3lDeviceLinkErrorCountSlipAlarm": k3lDeviceLinkErrorCountSlipAlarm,
       "k3lDeviceLinkErrorCountPRBS": k3lDeviceLinkErrorCountPRBS,
       "k3lDeviceLinkErrorCountWrongEBits": k3lDeviceLinkErrorCountWrongEBits,
       "k3lDeviceLinkErrorCountJitterVariation": k3lDeviceLinkErrorCountJitterVariation,
       "k3lDeviceLinkErrorCountFramesWithoutSync": k3lDeviceLinkErrorCountFramesWithoutSync,
       "k3lDeviceLinkErrorCountMultiframeSignal": k3lDeviceLinkErrorCountMultiframeSignal,
       "k3lDeviceLinkErrorCountFrameError": k3lDeviceLinkErrorCountFrameError,
       "k3lDeviceLinkErrorCountBipolarViolation": k3lDeviceLinkErrorCountBipolarViolation,
       "k3lDeviceLinkErrorCountCRC4": k3lDeviceLinkErrorCountCRC4,
       "k3lDeviceLinkReset": k3lDeviceLinkReset,
       "k3lDeviceLinkResetErrorCount": k3lDeviceLinkResetErrorCount,
       "k3lDeviceLinkBlock": k3lDeviceLinkBlock,
       "k3lDeviceLinkChannelCount": k3lDeviceLinkChannelCount,
       "k3lDeviceLinkChannelCountEnabled": k3lDeviceLinkChannelCountEnabled,
       "k3lDeviceLinkChannelCountIdle": k3lDeviceLinkChannelCountIdle,
       "k3lDeviceLinkChannelCountFail": k3lDeviceLinkChannelCountFail,
       "k3lDeviceLinkChannelCountBusy": k3lDeviceLinkChannelCountBusy,
       "k3lDeviceLinkReceivingClock": k3lDeviceLinkReceivingClock,
       "k3lDeviceLinkStatsIncoming": k3lDeviceLinkStatsIncoming,
       "k3lDeviceLinkStatsOutgoing": k3lDeviceLinkStatsOutgoing,
       "k3lDeviceLinkOutgoingCompleted": k3lDeviceLinkOutgoingCompleted,
       "k3lDeviceLinkOutgoingError": k3lDeviceLinkOutgoingError,
       "k3lDeviceLinkRemoteDisconnect": k3lDeviceLinkRemoteDisconnect,
       "k3lDeviceLinkLocalDisconnect": k3lDeviceLinkLocalDisconnect,
       "k3lDeviceLinkCallFailBusy": k3lDeviceLinkCallFailBusy,
       "k3lDeviceLinkCallFailNoAnswer": k3lDeviceLinkCallFailNoAnswer,
       "k3lDeviceLinkCallFailRejected": k3lDeviceLinkCallFailRejected,
       "k3lDeviceLinkCallFailChangedNumber": k3lDeviceLinkCallFailChangedNumber,
       "k3lDeviceLinkCallFailInvalidNumber": k3lDeviceLinkCallFailInvalidNumber,
       "k3lDeviceLinkCallFailOutOfService": k3lDeviceLinkCallFailOutOfService,
       "k3lDeviceLinkCallFailCongestion": k3lDeviceLinkCallFailCongestion,
       "k3lDeviceLinkCallFailNetworkFailure": k3lDeviceLinkCallFailNetworkFailure,
       "k3lDeviceLinkCallFailOther": k3lDeviceLinkCallFailOther,
       "k3lDeviceLinkOperatingMode": k3lDeviceLinkOperatingMode,
       "k3lDeviceHILinkTable": k3lDeviceHILinkTable,
       "k3lDeviceHILinkEntry": k3lDeviceHILinkEntry,
       "k3lDeviceHILinkIndex": k3lDeviceHILinkIndex,
       "k3lDeviceHILinkOperStatus": k3lDeviceHILinkOperStatus,
       "k3lDeviceHILinkAlarm": k3lDeviceHILinkAlarm,
       "k3lDeviceChannelTable": k3lDeviceChannelTable,
       "k3lDeviceChannelEntry": k3lDeviceChannelEntry,
       "k3lDeviceChannelIndex": k3lDeviceChannelIndex,
       "k3lDeviceChannelSignaling": k3lDeviceChannelSignaling,
       "k3lDeviceChannelCallStatus": k3lDeviceChannelCallStatus,
       "k3lDeviceChannelAudioStatus": k3lDeviceChannelAudioStatus,
       "k3lDeviceChannelEnabledFeatures": k3lDeviceChannelEnabledFeatures,
       "k3lDeviceChannelStatsIncoming": k3lDeviceChannelStatsIncoming,
       "k3lDeviceChannelStatsOutgoing": k3lDeviceChannelStatsOutgoing,
       "k3lDeviceChannelStatsOutgoingCompleted": k3lDeviceChannelStatsOutgoingCompleted,
       "k3lDeviceChannelStatsOutgoingError": k3lDeviceChannelStatsOutgoingError,
       "k3lDeviceChannelStatsRemoteDisconnect": k3lDeviceChannelStatsRemoteDisconnect,
       "k3lDeviceChannelStatsLocalDisconnect": k3lDeviceChannelStatsLocalDisconnect,
       "k3lDeviceChannelStatsCallFailBusy": k3lDeviceChannelStatsCallFailBusy,
       "k3lDeviceChannelStatsCallFailNoAnswer": k3lDeviceChannelStatsCallFailNoAnswer,
       "k3lDeviceChannelStatsCallFailRejected": k3lDeviceChannelStatsCallFailRejected,
       "k3lDeviceChannelStatsCallFailChangedNumber": k3lDeviceChannelStatsCallFailChangedNumber,
       "k3lDeviceChannelStatsCallFailInvalidNumber": k3lDeviceChannelStatsCallFailInvalidNumber,
       "k3lDeviceChannelStatsCallFailOutOfService": k3lDeviceChannelStatsCallFailOutOfService,
       "k3lDeviceChannelStatsCallFailCongestion": k3lDeviceChannelStatsCallFailCongestion,
       "k3lDeviceChannelStatsCallFailNetworkFailure": k3lDeviceChannelStatsCallFailNetworkFailure,
       "k3lDeviceChannelStatsCallFailOther": k3lDeviceChannelStatsCallFailOther,
       "k3lDeviceChannelDestinationAddress": k3lDeviceChannelDestinationAddress,
       "k3lDeviceChannelCallDuration": k3lDeviceChannelCallDuration,
       "k3lDeviceChannelRecording": k3lDeviceChannelRecording,
       "k3lDeviceChannelAverageCallTime": k3lDeviceChannelAverageCallTime,
       "k3lDeviceChannelOriginAddress": k3lDeviceChannelOriginAddress,
       "k3lDeviceChannelCadenceStatus": k3lDeviceChannelCadenceStatus,
       "k3lDeviceExtended": k3lDeviceExtended,
       "k3lDeviceExtendedE1": k3lDeviceExtendedE1,
       "k3lDeviceE1ChannelCount": k3lDeviceE1ChannelCount,
       "k3lDeviceE1ChannelTable": k3lDeviceE1ChannelTable,
       "k3lDeviceE1ChannelEntry": k3lDeviceE1ChannelEntry,
       "k3lDeviceE1ChannelIndex": k3lDeviceE1ChannelIndex,
       "k3lDeviceE1ChannelStatus": k3lDeviceE1ChannelStatus,
       "k3lDeviceExtendedFxo": k3lDeviceExtendedFxo,
       "k3lDeviceFxoChannelCount": k3lDeviceFxoChannelCount,
       "k3lDeviceFxoChannelTable": k3lDeviceFxoChannelTable,
       "k3lDeviceFxoChannelEntry": k3lDeviceFxoChannelEntry,
       "k3lDeviceFxoChannelIndex": k3lDeviceFxoChannelIndex,
       "k3lDeviceFxoChannelStatus": k3lDeviceFxoChannelStatus,
       "k3lDeviceExtendedFxs": k3lDeviceExtendedFxs,
       "k3lDeviceFxsChannelCount": k3lDeviceFxsChannelCount,
       "k3lDeviceFxsChannelTable": k3lDeviceFxsChannelTable,
       "k3lDeviceFxsChannelEntry": k3lDeviceFxsChannelEntry,
       "k3lDeviceFxsChannelIndex": k3lDeviceFxsChannelIndex,
       "k3lDeviceFxsChannelStatus": k3lDeviceFxsChannelStatus,
       "k3lDeviceExtendedGsm": k3lDeviceExtendedGsm,
       "k3lDeviceGsmChannelCount": k3lDeviceGsmChannelCount,
       "k3lDeviceGsmChannelTable": k3lDeviceGsmChannelTable,
       "k3lDeviceGsmChannelEntry": k3lDeviceGsmChannelEntry,
       "k3lDeviceGsmChannelIndex": k3lDeviceGsmChannelIndex,
       "k3lDeviceGsmChannelStatus": k3lDeviceGsmChannelStatus,
       "k3lDeviceGsmChannelSignalStrength": k3lDeviceGsmChannelSignalStrength,
       "k3lDeviceGsmChannelErrorRate": k3lDeviceGsmChannelErrorRate,
       "k3lDeviceGsmChannelRegistryStatus": k3lDeviceGsmChannelRegistryStatus,
       "k3lDeviceGsmChannelOperName": k3lDeviceGsmChannelOperName,
       "k3lDeviceGsmChannelUnreadSmsMessages": k3lDeviceGsmChannelUnreadSmsMessages,
       "k3lDeviceGsmChannelEnabledFeatures": k3lDeviceGsmChannelEnabledFeatures,
       "k3lDeviceGsmChannelImei": k3lDeviceGsmChannelImei,
       "k3lDeviceGsmChannelSim": k3lDeviceGsmChannelSim,
       "k3lDeviceGsmChannelImsi": k3lDeviceGsmChannelImsi,
       "k3lDeviceGsmChannelIccid": k3lDeviceGsmChannelIccid,
       "k3lDeviceGsmChannelMsisdn": k3lDeviceGsmChannelMsisdn,
       "k3lDeviceGsmChannelCallWaiting": k3lDeviceGsmChannelCallWaiting,
       "k3lDeviceGsmChannelSimCardCount": k3lDeviceGsmChannelSimCardCount,
       "k3lDeviceGsmCallTable": k3lDeviceGsmCallTable,
       "k3lDeviceGsmCallEntry": k3lDeviceGsmCallEntry,
       "k3lDeviceGsmCallIndex": k3lDeviceGsmCallIndex,
       "k3lDeviceGsmCallStatus": k3lDeviceGsmCallStatus,
       "k3lDeviceGsmCallMode": k3lDeviceGsmCallMode,
       "k3lDeviceGsmCallNumber": k3lDeviceGsmCallNumber,
       "k3lDeviceGsmCallFlags": k3lDeviceGsmCallFlags,
       "k3lDeviceExtendedVoip": k3lDeviceExtendedVoip,
       "k3lDeviceSipChannelCount": k3lDeviceSipChannelCount,
       "k3lDeviceSipChannelTable": k3lDeviceSipChannelTable,
       "k3lDeviceSipChannelEntry": k3lDeviceSipChannelEntry,
       "k3lDeviceSipChannelIndex": k3lDeviceSipChannelIndex,
       "k3lDeviceSipChannelStatus": k3lDeviceSipChannelStatus,
       "k3lDeviceVoipProfileLocalAddress": k3lDeviceVoipProfileLocalAddress,
       "k3lDeviceVoipProfileLocalPort": k3lDeviceVoipProfileLocalPort,
       "k3lDeviceVoipProfileTransportType": k3lDeviceVoipProfileTransportType,
       "k3lDeviceVoipProfileRTPAddress": k3lDeviceVoipProfileRTPAddress,
       "k3lDeviceVoipProfileUser": k3lDeviceVoipProfileUser,
       "k3lDeviceVoipProfileAuthorizationUser": k3lDeviceVoipProfileAuthorizationUser,
       "k3lDeviceVoipProfileRealm": k3lDeviceVoipProfileRealm,
       "k3lDeviceVoipProfileDomain": k3lDeviceVoipProfileDomain,
       "k3lDeviceVoipProfileDomainPort": k3lDeviceVoipProfileDomainPort,
       "k3lDeviceVoipProfileProxy": k3lDeviceVoipProfileProxy,
       "k3lDeviceVoipProfileProxyPort": k3lDeviceVoipProfileProxyPort,
       "k3lDeviceVoipProfileRegistered": k3lDeviceVoipProfileRegistered,
       "k3lDeviceVoipChannelTransactionCount": k3lDeviceVoipChannelTransactionCount,
       "k3lDeviceVoipChannelClientTransactionCount": k3lDeviceVoipChannelClientTransactionCount,
       "k3lDeviceVoipChannelServerTransactionCount": k3lDeviceVoipChannelServerTransactionCount,
       "k3lDeviceVoipChannelClientTransactionFailureCount": k3lDeviceVoipChannelClientTransactionFailureCount,
       "k3lDeviceVoipChannelServerTransactionFailureCount": k3lDeviceVoipChannelServerTransactionFailureCount,
       "k3lDeviceVoipChannelClientTransactionFailure4xxCount": k3lDeviceVoipChannelClientTransactionFailure4xxCount,
       "k3lDeviceVoipChannelServerTransactionFailure4xxCount": k3lDeviceVoipChannelServerTransactionFailure4xxCount,
       "k3lDeviceVoipChannelClientTransactionFailure5xxCount": k3lDeviceVoipChannelClientTransactionFailure5xxCount,
       "k3lDeviceVoipChannelServerTransactionFailure5xxCount": k3lDeviceVoipChannelServerTransactionFailure5xxCount,
       "k3lDeviceVoipChannelClientTransactionFailure6xxCount": k3lDeviceVoipChannelClientTransactionFailure6xxCount,
       "k3lDeviceVoipChannelServerTransactionFailure6xxCount": k3lDeviceVoipChannelServerTransactionFailure6xxCount,
       "k3lDeviceVoipRTPStatusTransmitLastSequenceNumber": k3lDeviceVoipRTPStatusTransmitLastSequenceNumber,
       "k3lDeviceVoipRTPStatusTransmitPacketCount": k3lDeviceVoipRTPStatusTransmitPacketCount,
       "k3lDeviceVoipRTPStatusTransmitOctetCount": k3lDeviceVoipRTPStatusTransmitOctetCount,
       "k3lDeviceVoipRTPStatusTransmitPacketLost": k3lDeviceVoipRTPStatusTransmitPacketLost,
       "k3lDeviceVoipRTPStatusReceiveInitialSequenceNumber": k3lDeviceVoipRTPStatusReceiveInitialSequenceNumber,
       "k3lDeviceVoipRTPStatusReceiveLastSequenceNumber": k3lDeviceVoipRTPStatusReceiveLastSequenceNumber,
       "k3lDeviceVoipRTPStatusReceivePacketCount": k3lDeviceVoipRTPStatusReceivePacketCount,
       "k3lDeviceVoipRTPStatusReceiveDroppedCount": k3lDeviceVoipRTPStatusReceiveDroppedCount,
       "k3lDeviceVoipRTPStatusReceiveLastDroppedCount": k3lDeviceVoipRTPStatusReceiveLastDroppedCount,
       "k3lDeviceChannelGroupChannel": k3lDeviceChannelGroupChannel,
       "k3lDeviceChannelGroupTable": k3lDeviceChannelGroupTable,
       "k3lDeviceChannelGroupEntry": k3lDeviceChannelGroupEntry,
       "k3lDeviceChannelGroupIndex": k3lDeviceChannelGroupIndex,
       "k3lDeviceChannelGroupType": k3lDeviceChannelGroupType,
       "k3lDeviceChannelGroupFirstChannel": k3lDeviceChannelGroupFirstChannel,
       "k3lDeviceChannelGroupChannelCount": k3lDeviceChannelGroupChannelCount,
       "k3lDeviceChannelGroupChannelIdle": k3lDeviceChannelGroupChannelIdle,
       "k3lDeviceChannelGroupChannelFail": k3lDeviceChannelGroupChannelFail,
       "k3lDeviceChannelGroupChannelBusy": k3lDeviceChannelGroupChannelBusy,
       "k3lConsolidated": k3lConsolidated,
       "k3lConsolidatedDevices": k3lConsolidatedDevices,
       "k3lConsolidatedDevicesChannelCount": k3lConsolidatedDevicesChannelCount,
       "k3lConsolidatedDevicesChannelCountEnabled": k3lConsolidatedDevicesChannelCountEnabled,
       "k3lConsolidatedDevicesChannelCountIdle": k3lConsolidatedDevicesChannelCountIdle,
       "k3lConsolidatedDevicesChannelCountFail": k3lConsolidatedDevicesChannelCountFail,
       "k3lConsolidatedDevicesChannelCountBusy": k3lConsolidatedDevicesChannelCountBusy,
       "k3lConfiguration": k3lConfiguration,
       "k3lConfigurationR2Country": k3lConfigurationR2Country,
       "k3lLicense": k3lLicense,
       "k3lLicenseCount": k3lLicenseCount,
       "k3lLicenseTable": k3lLicenseTable,
       "k3lLicenseEntry": k3lLicenseEntry,
       "k3lLicenseIndex": k3lLicenseIndex,
       "k3lLicenseID": k3lLicenseID,
       "k3lLicenseHardwareType": k3lLicenseHardwareType,
       "k3lLicenseSerial": k3lLicenseSerial,
       "k3lLicenseHardwareInfo": k3lLicenseHardwareInfo,
       "k3lLicenseIssueDate": k3lLicenseIssueDate,
       "k3lLicenseExpirationDate": k3lLicenseExpirationDate,
       "k3lLicenseCustomerInfo": k3lLicenseCustomerInfo,
       "k3lLicenseIssuer": k3lLicenseIssuer,
       "k3lLicenseNumResourceTypes": k3lLicenseNumResourceTypes,
       "k3lLicenseDescr": k3lLicenseDescr,
       "k3lLicenseResourceRequiredTable": k3lLicenseResourceRequiredTable,
       "k3lLicenseResourceRequiredEntry": k3lLicenseResourceRequiredEntry,
       "k3lLicenseResourceRequiredIndex": k3lLicenseResourceRequiredIndex,
       "k3lLicenseResourceRequiredType": k3lLicenseResourceRequiredType,
       "k3lLicenseResourceRequired": k3lLicenseResourceRequired,
       "k3lLicenseResource": k3lLicenseResource,
       "k3lLicenseResourceCount": k3lLicenseResourceCount,
       "k3lLicenseResourceTable": k3lLicenseResourceTable,
       "k3lLicenseResourceEntry": k3lLicenseResourceEntry,
       "k3lLicenseResourceIndex": k3lLicenseResourceIndex,
       "k3lLicenseResourceType": k3lLicenseResourceType,
       "k3lLicenseResourceName": k3lLicenseResourceName,
       "k3lLicenseResourcesTotal": k3lLicenseResourcesTotal,
       "k3lLicenseResourcesTotalActive": k3lLicenseResourcesTotalActive,
       "k3lMIBConformance": k3lMIBConformance,
       "k3lMIBCompliances": k3lMIBCompliances,
       "k3lFullCompliance": k3lFullCompliance,
       "k3lMIBGroups": k3lMIBGroups,
       "k3lRootGroup": k3lRootGroup,
       "k3lDeviceGroups": k3lDeviceGroups,
       "k3lDeviceGroup": k3lDeviceGroup,
       "k3lDeviceLinkGroups": k3lDeviceLinkGroups,
       "k3lDeviceLinkGroup": k3lDeviceLinkGroup,
       "k3lDeviceHILinkGroup": k3lDeviceHILinkGroup,
       "k3lDeviceChannelGroups": k3lDeviceChannelGroups,
       "k3lDeviceChannelGroup": k3lDeviceChannelGroup,
       "k3lDeviceE1ChannelGroup": k3lDeviceE1ChannelGroup,
       "k3lDeviceFxoChannelGroup": k3lDeviceFxoChannelGroup,
       "k3lDeviceFxsChannelGroup": k3lDeviceFxsChannelGroup,
       "k3lDeviceGsmChannelGroup": k3lDeviceGsmChannelGroup,
       "k3lDeviceSipChannelGroup": k3lDeviceSipChannelGroup,
       "k3lDeviceChannelGroupGroup": k3lDeviceChannelGroupGroup,
       "k3lDeviceCallInfoGroups": k3lDeviceCallInfoGroups,
       "k3lDeviceGsmCallGroup": k3lDeviceGsmCallGroup,
       "k3lConsolidatedGroups": k3lConsolidatedGroups,
       "k3lConsolidatedDevicesGroup": k3lConsolidatedDevicesGroup,
       "k3lConfigurationGroup": k3lConfigurationGroup,
       "k3lLicenseGroups": k3lLicenseGroups,
       "k3lLicenseGroup": k3lLicenseGroup,
       "k3lLicenseResourceRequiredGroup": k3lLicenseResourceRequiredGroup,
       "k3lLicenseResourceGroup": k3lLicenseResourceGroup,
       "app": app}
)
