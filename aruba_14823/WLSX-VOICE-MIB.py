# SNMP MIB module (WLSX-VOICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/aruba_14823/WLSX-VOICE-MIB.mib
# Produced by pysmi-1.5.11 at Wed May 21 21:48:55 2025
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

(wlsxEnterpriseMibModules,) = mibBuilder.importSymbols(
    "ARUBA-MIB",
    "wlsxEnterpriseMibModules")

(ArubaCallStates,
 ArubaEnableValue,
 ArubaVlanValidRange,
 ArubaVoiceCacBit,
 ArubaVoiceCdrDirection,
 ArubaVoipProtocol,
 ArubaVoipRegState) = mibBuilder.importSymbols(
    "ARUBA-TC",
    "ArubaCallStates",
    "ArubaEnableValue",
    "ArubaVlanValidRange",
    "ArubaVoiceCacBit",
    "ArubaVoiceCdrDirection",
    "ArubaVoipProtocol",
    "ArubaVoipRegState")

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
 iso,
 snmpModules) = mibBuilder.importSymbols(
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
    "iso",
    "snmpModules")

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 StorageType,
 TAddress,
 TDomain,
 TextualConvention,
 TestAndIncr,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TAddress",
    "TDomain",
    "TextualConvention",
    "TestAndIncr",
    "TimeInterval",
    "TruthValue")

(wlanAPBSSID,
 wlanAPMacAddress,
 wlanAPRadioNumber,
 wlanStaPhyAddress) = mibBuilder.importSymbols(
    "WLSX-WLAN-MIB",
    "wlanAPBSSID",
    "wlanAPMacAddress",
    "wlanAPRadioNumber",
    "wlanStaPhyAddress")


# MODULE-IDENTITY

wlsxVoiceMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12)
)
if mibBuilder.loadTexts:
    wlsxVoiceMIB.setRevisions(
        ("2020-08-14 17:45",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WlsxVoiceStatsGroup_ObjectIdentity = ObjectIdentity
wlsxVoiceStatsGroup = _WlsxVoiceStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1)
)
_WlsxVoiceCdrInfoGroup_ObjectIdentity = ObjectIdentity
wlsxVoiceCdrInfoGroup = _WlsxVoiceCdrInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1)
)
_WlsxVoiceCdrTotal_Type = Unsigned32
_WlsxVoiceCdrTotal_Object = MibScalar
wlsxVoiceCdrTotal = _WlsxVoiceCdrTotal_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 1),
    _WlsxVoiceCdrTotal_Type()
)
wlsxVoiceCdrTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxVoiceCdrTotal.setStatus("current")
_WlsxVoiceCdrTable_Object = MibTable
wlsxVoiceCdrTable = _WlsxVoiceCdrTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2)
)
if mibBuilder.loadTexts:
    wlsxVoiceCdrTable.setStatus("current")
_WlsxVoiceCdrEntry_Object = MibTableRow
wlsxVoiceCdrEntry = _WlsxVoiceCdrEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1)
)
wlsxVoiceCdrEntry.setIndexNames(
    (0, "WLSX-VOICE-MIB", "voiceCdrId"),
)
if mibBuilder.loadTexts:
    wlsxVoiceCdrEntry.setStatus("current")
_VoiceCdrId_Type = Unsigned32
_VoiceCdrId_Object = MibTableColumn
voiceCdrId = _VoiceCdrId_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 1),
    _VoiceCdrId_Type()
)
voiceCdrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    voiceCdrId.setStatus("current")
_VoiceCdrIp_Type = IpAddress
_VoiceCdrIp_Object = MibTableColumn
voiceCdrIp = _VoiceCdrIp_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 2),
    _VoiceCdrIp_Type()
)
voiceCdrIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCdrIp.setStatus("current")
_VoiceCdrMac_Type = MacAddress
_VoiceCdrMac_Object = MibTableColumn
voiceCdrMac = _VoiceCdrMac_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 3),
    _VoiceCdrMac_Type()
)
voiceCdrMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCdrMac.setStatus("current")
_VoiceCdrName_Type = DisplayString
_VoiceCdrName_Object = MibTableColumn
voiceCdrName = _VoiceCdrName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 4),
    _VoiceCdrName_Type()
)
voiceCdrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCdrName.setStatus("current")
_VoiceCdrDialNum_Type = DisplayString
_VoiceCdrDialNum_Object = MibTableColumn
voiceCdrDialNum = _VoiceCdrDialNum_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 5),
    _VoiceCdrDialNum_Type()
)
voiceCdrDialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCdrDialNum.setStatus("current")
_VoiceCdrDir_Type = ArubaVoiceCdrDirection
_VoiceCdrDir_Object = MibTableColumn
voiceCdrDir = _VoiceCdrDir_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 6),
    _VoiceCdrDir_Type()
)
voiceCdrDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCdrDir.setStatus("current")
_VoiceCdrOrigTime_Type = Unsigned32
_VoiceCdrOrigTime_Object = MibTableColumn
voiceCdrOrigTime = _VoiceCdrOrigTime_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 7),
    _VoiceCdrOrigTime_Type()
)
voiceCdrOrigTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCdrOrigTime.setStatus("current")
_VoiceCdrSetupTime_Type = Unsigned32
_VoiceCdrSetupTime_Object = MibTableColumn
voiceCdrSetupTime = _VoiceCdrSetupTime_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 8),
    _VoiceCdrSetupTime_Type()
)
voiceCdrSetupTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCdrSetupTime.setStatus("deprecated")
_VoiceCdrTeardownTime_Type = Unsigned32
_VoiceCdrTeardownTime_Object = MibTableColumn
voiceCdrTeardownTime = _VoiceCdrTeardownTime_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 9),
    _VoiceCdrTeardownTime_Type()
)
voiceCdrTeardownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCdrTeardownTime.setStatus("deprecated")
_VoiceCdrStatus_Type = ArubaCallStates
_VoiceCdrStatus_Object = MibTableColumn
voiceCdrStatus = _VoiceCdrStatus_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 10),
    _VoiceCdrStatus_Type()
)
voiceCdrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCdrStatus.setStatus("current")
_VoiceCdrReason_Type = DisplayString
_VoiceCdrReason_Object = MibTableColumn
voiceCdrReason = _VoiceCdrReason_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 11),
    _VoiceCdrReason_Type()
)
voiceCdrReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCdrReason.setStatus("current")
_VoiceCdrDuration_Type = Integer32
_VoiceCdrDuration_Object = MibTableColumn
voiceCdrDuration = _VoiceCdrDuration_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 12),
    _VoiceCdrDuration_Type()
)
voiceCdrDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCdrDuration.setStatus("current")
_VoiceCdrRValueA_Type = Integer32
_VoiceCdrRValueA_Object = MibTableColumn
voiceCdrRValueA = _VoiceCdrRValueA_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 13),
    _VoiceCdrRValueA_Type()
)
voiceCdrRValueA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCdrRValueA.setStatus("current")
_VoiceCdrApSwitchDelay_Type = Integer32
_VoiceCdrApSwitchDelay_Object = MibTableColumn
voiceCdrApSwitchDelay = _VoiceCdrApSwitchDelay_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 14),
    _VoiceCdrApSwitchDelay_Type()
)
voiceCdrApSwitchDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCdrApSwitchDelay.setStatus("deprecated")
_VoiceCdrCodec_Type = Integer32
_VoiceCdrCodec_Object = MibTableColumn
voiceCdrCodec = _VoiceCdrCodec_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 15),
    _VoiceCdrCodec_Type()
)
voiceCdrCodec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCdrCodec.setStatus("current")
_VoiceCdrApName_Type = DisplayString
_VoiceCdrApName_Object = MibTableColumn
voiceCdrApName = _VoiceCdrApName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 16),
    _VoiceCdrApName_Type()
)
voiceCdrApName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCdrApName.setStatus("current")
_VoiceCdrApMac_Type = MacAddress
_VoiceCdrApMac_Object = MibTableColumn
voiceCdrApMac = _VoiceCdrApMac_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 17),
    _VoiceCdrApMac_Type()
)
voiceCdrApMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCdrApMac.setStatus("current")
_VoiceCdrBssid_Type = DisplayString
_VoiceCdrBssid_Object = MibTableColumn
voiceCdrBssid = _VoiceCdrBssid_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 18),
    _VoiceCdrBssid_Type()
)
voiceCdrBssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCdrBssid.setStatus("current")
_VoiceCdrEssid_Type = DisplayString
_VoiceCdrEssid_Object = MibTableColumn
voiceCdrEssid = _VoiceCdrEssid_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 19),
    _VoiceCdrEssid_Type()
)
voiceCdrEssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCdrEssid.setStatus("current")
_VoiceCdrHandovers_Type = Integer32
_VoiceCdrHandovers_Object = MibTableColumn
voiceCdrHandovers = _VoiceCdrHandovers_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 20),
    _VoiceCdrHandovers_Type()
)
voiceCdrHandovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCdrHandovers.setStatus("current")
_VoiceCdrMOS_Type = DisplayString
_VoiceCdrMOS_Object = MibTableColumn
voiceCdrMOS = _VoiceCdrMOS_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 21),
    _VoiceCdrMOS_Type()
)
voiceCdrMOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCdrMOS.setStatus("current")
_VoiceCdrDelayA_Type = DisplayString
_VoiceCdrDelayA_Object = MibTableColumn
voiceCdrDelayA = _VoiceCdrDelayA_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 22),
    _VoiceCdrDelayA_Type()
)
voiceCdrDelayA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCdrDelayA.setStatus("current")
_VoiceCdrJitterA_Type = DisplayString
_VoiceCdrJitterA_Object = MibTableColumn
voiceCdrJitterA = _VoiceCdrJitterA_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 23),
    _VoiceCdrJitterA_Type()
)
voiceCdrJitterA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCdrJitterA.setStatus("current")
_VoiceCdrPktLossA_Type = DisplayString
_VoiceCdrPktLossA_Object = MibTableColumn
voiceCdrPktLossA = _VoiceCdrPktLossA_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 24),
    _VoiceCdrPktLossA_Type()
)
voiceCdrPktLossA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCdrPktLossA.setStatus("current")
_VoiceCdrRValueC_Type = Integer32
_VoiceCdrRValueC_Object = MibTableColumn
voiceCdrRValueC = _VoiceCdrRValueC_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 25),
    _VoiceCdrRValueC_Type()
)
voiceCdrRValueC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCdrRValueC.setStatus("current")
_VoiceCdrDelayC_Type = DisplayString
_VoiceCdrDelayC_Object = MibTableColumn
voiceCdrDelayC = _VoiceCdrDelayC_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 26),
    _VoiceCdrDelayC_Type()
)
voiceCdrDelayC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCdrDelayC.setStatus("current")
_VoiceCdrJitterC_Type = DisplayString
_VoiceCdrJitterC_Object = MibTableColumn
voiceCdrJitterC = _VoiceCdrJitterC_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 27),
    _VoiceCdrJitterC_Type()
)
voiceCdrJitterC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCdrJitterC.setStatus("current")
_VoiceCdrPktLossC_Type = DisplayString
_VoiceCdrPktLossC_Object = MibTableColumn
voiceCdrPktLossC = _VoiceCdrPktLossC_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 28),
    _VoiceCdrPktLossC_Type()
)
voiceCdrPktLossC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCdrPktLossC.setStatus("current")
_WlsxVoiceCallCtrsGroup_ObjectIdentity = ObjectIdentity
wlsxVoiceCallCtrsGroup = _WlsxVoiceCallCtrsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 2)
)
_VoiceCallCtrsTotal_Type = Unsigned32
_VoiceCallCtrsTotal_Object = MibScalar
voiceCallCtrsTotal = _VoiceCallCtrsTotal_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 2, 1),
    _VoiceCallCtrsTotal_Type()
)
voiceCallCtrsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCallCtrsTotal.setStatus("current")
_VoiceCallCtrsSuccess_Type = Unsigned32
_VoiceCallCtrsSuccess_Object = MibScalar
voiceCallCtrsSuccess = _VoiceCallCtrsSuccess_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 2, 2),
    _VoiceCallCtrsSuccess_Type()
)
voiceCallCtrsSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCallCtrsSuccess.setStatus("current")
_VoiceCallCtrsFailed_Type = Unsigned32
_VoiceCallCtrsFailed_Object = MibScalar
voiceCallCtrsFailed = _VoiceCallCtrsFailed_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 2, 3),
    _VoiceCallCtrsFailed_Type()
)
voiceCallCtrsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCallCtrsFailed.setStatus("current")
_VoiceCallCtrsRejected_Type = Unsigned32
_VoiceCallCtrsRejected_Object = MibScalar
voiceCallCtrsRejected = _VoiceCallCtrsRejected_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 2, 4),
    _VoiceCallCtrsRejected_Type()
)
voiceCallCtrsRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCallCtrsRejected.setStatus("current")
_VoiceCallCtrsAborted_Type = Unsigned32
_VoiceCallCtrsAborted_Object = MibScalar
voiceCallCtrsAborted = _VoiceCallCtrsAborted_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 2, 5),
    _VoiceCallCtrsAborted_Type()
)
voiceCallCtrsAborted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCallCtrsAborted.setStatus("current")
_VoiceCallCtrsOrig_Type = Unsigned32
_VoiceCallCtrsOrig_Object = MibScalar
voiceCallCtrsOrig = _VoiceCallCtrsOrig_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 2, 6),
    _VoiceCallCtrsOrig_Type()
)
voiceCallCtrsOrig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCallCtrsOrig.setStatus("current")
_VoiceCallCtrsRecvd_Type = Unsigned32
_VoiceCallCtrsRecvd_Object = MibScalar
voiceCallCtrsRecvd = _VoiceCallCtrsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 2, 7),
    _VoiceCallCtrsRecvd_Type()
)
voiceCallCtrsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCallCtrsRecvd.setStatus("current")
_VoiceCallCtrsActive_Type = Unsigned32
_VoiceCallCtrsActive_Object = MibScalar
voiceCallCtrsActive = _VoiceCallCtrsActive_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 2, 8),
    _VoiceCallCtrsActive_Type()
)
voiceCallCtrsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCallCtrsActive.setStatus("current")
_VoiceCallCtrsNotFnd_Type = Unsigned32
_VoiceCallCtrsNotFnd_Object = MibScalar
voiceCallCtrsNotFnd = _VoiceCallCtrsNotFnd_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 2, 9),
    _VoiceCallCtrsNotFnd_Type()
)
voiceCallCtrsNotFnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCallCtrsNotFnd.setStatus("deprecated")
_VoiceCallCtrsBusy_Type = Unsigned32
_VoiceCallCtrsBusy_Object = MibScalar
voiceCallCtrsBusy = _VoiceCallCtrsBusy_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 2, 10),
    _VoiceCallCtrsBusy_Type()
)
voiceCallCtrsBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCallCtrsBusy.setStatus("deprecated")
_VoiceCallCtrsSvc_Type = Unsigned32
_VoiceCallCtrsSvc_Object = MibScalar
voiceCallCtrsSvc = _VoiceCallCtrsSvc_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 2, 11),
    _VoiceCallCtrsSvc_Type()
)
voiceCallCtrsSvc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCallCtrsSvc.setStatus("deprecated")
_VoiceCallCtrsReqTerm_Type = Unsigned32
_VoiceCallCtrsReqTerm_Object = MibScalar
voiceCallCtrsReqTerm = _VoiceCallCtrsReqTerm_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 2, 12),
    _VoiceCallCtrsReqTerm_Type()
)
voiceCallCtrsReqTerm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCallCtrsReqTerm.setStatus("deprecated")
_VoiceCallCtrsDecline_Type = Unsigned32
_VoiceCallCtrsDecline_Object = MibScalar
voiceCallCtrsDecline = _VoiceCallCtrsDecline_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 2, 13),
    _VoiceCallCtrsDecline_Type()
)
voiceCallCtrsDecline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCallCtrsDecline.setStatus("deprecated")
_VoiceCallCtrsUnauth_Type = Unsigned32
_VoiceCallCtrsUnauth_Object = MibScalar
voiceCallCtrsUnauth = _VoiceCallCtrsUnauth_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 2, 14),
    _VoiceCallCtrsUnauth_Type()
)
voiceCallCtrsUnauth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCallCtrsUnauth.setStatus("deprecated")
_VoiceCallCtrsMisc_Type = Unsigned32
_VoiceCallCtrsMisc_Object = MibScalar
voiceCallCtrsMisc = _VoiceCallCtrsMisc_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 2, 15),
    _VoiceCallCtrsMisc_Type()
)
voiceCallCtrsMisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCallCtrsMisc.setStatus("deprecated")
_WlsxVoiceClientInfoGroup_ObjectIdentity = ObjectIdentity
wlsxVoiceClientInfoGroup = _WlsxVoiceClientInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 3)
)
_WlsxVoiceClientTotal_Type = Unsigned32
_WlsxVoiceClientTotal_Object = MibScalar
wlsxVoiceClientTotal = _WlsxVoiceClientTotal_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 3, 1),
    _WlsxVoiceClientTotal_Type()
)
wlsxVoiceClientTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxVoiceClientTotal.setStatus("current")
_WlsxVoiceClientTable_Object = MibTable
wlsxVoiceClientTable = _WlsxVoiceClientTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 3, 2)
)
if mibBuilder.loadTexts:
    wlsxVoiceClientTable.setStatus("current")
_WlsxVoiceClientEntry_Object = MibTableRow
wlsxVoiceClientEntry = _WlsxVoiceClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 3, 2, 1)
)
wlsxVoiceClientEntry.setIndexNames(
    (0, "WLSX-WLAN-MIB", "wlanStaPhyAddress"),
)
if mibBuilder.loadTexts:
    wlsxVoiceClientEntry.setStatus("current")
_VoiceClientIp_Type = IpAddress
_VoiceClientIp_Object = MibTableColumn
voiceClientIp = _VoiceClientIp_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 3, 2, 1, 1),
    _VoiceClientIp_Type()
)
voiceClientIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceClientIp.setStatus("current")
_VoiceClientProtocol_Type = DisplayString
_VoiceClientProtocol_Object = MibTableColumn
voiceClientProtocol = _VoiceClientProtocol_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 3, 2, 1, 2),
    _VoiceClientProtocol_Type()
)
voiceClientProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceClientProtocol.setStatus("current")
_VoiceClientRegState_Type = DisplayString
_VoiceClientRegState_Object = MibTableColumn
voiceClientRegState = _VoiceClientRegState_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 3, 2, 1, 3),
    _VoiceClientRegState_Type()
)
voiceClientRegState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceClientRegState.setStatus("current")
_VoiceClientContactName_Type = DisplayString
_VoiceClientContactName_Object = MibTableColumn
voiceClientContactName = _VoiceClientContactName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 3, 2, 1, 4),
    _VoiceClientContactName_Type()
)
voiceClientContactName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceClientContactName.setStatus("current")
_VoiceClientServerName_Type = DisplayString
_VoiceClientServerName_Object = MibTableColumn
voiceClientServerName = _VoiceClientServerName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 3, 2, 1, 5),
    _VoiceClientServerName_Type()
)
voiceClientServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceClientServerName.setStatus("current")
_VoiceClientEssid_Type = DisplayString
_VoiceClientEssid_Object = MibTableColumn
voiceClientEssid = _VoiceClientEssid_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 3, 2, 1, 6),
    _VoiceClientEssid_Type()
)
voiceClientEssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceClientEssid.setStatus("current")
_VoiceClientVlanId_Type = ArubaVlanValidRange
_VoiceClientVlanId_Object = MibTableColumn
voiceClientVlanId = _VoiceClientVlanId_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 3, 2, 1, 7),
    _VoiceClientVlanId_Type()
)
voiceClientVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceClientVlanId.setStatus("deprecated")
_VoiceClientTunnelId_Type = Integer32
_VoiceClientTunnelId_Object = MibTableColumn
voiceClientTunnelId = _VoiceClientTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 3, 2, 1, 8),
    _VoiceClientTunnelId_Type()
)
voiceClientTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceClientTunnelId.setStatus("deprecated")
_VoiceClientAvgDelay_Type = DisplayString
_VoiceClientAvgDelay_Object = MibTableColumn
voiceClientAvgDelay = _VoiceClientAvgDelay_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 3, 2, 1, 9),
    _VoiceClientAvgDelay_Type()
)
voiceClientAvgDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceClientAvgDelay.setStatus("current")
_VoiceClientAvgJitter_Type = DisplayString
_VoiceClientAvgJitter_Object = MibTableColumn
voiceClientAvgJitter = _VoiceClientAvgJitter_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 3, 2, 1, 10),
    _VoiceClientAvgJitter_Type()
)
voiceClientAvgJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceClientAvgJitter.setStatus("current")
_VoiceClientAvgPktLoss_Type = DisplayString
_VoiceClientAvgPktLoss_Object = MibTableColumn
voiceClientAvgPktLoss = _VoiceClientAvgPktLoss_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 3, 2, 1, 11),
    _VoiceClientAvgPktLoss_Type()
)
voiceClientAvgPktLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceClientAvgPktLoss.setStatus("current")
_VoiceClientAvgCallDuration_Type = Integer32
_VoiceClientAvgCallDuration_Object = MibTableColumn
voiceClientAvgCallDuration = _VoiceClientAvgCallDuration_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 3, 2, 1, 12),
    _VoiceClientAvgCallDuration_Type()
)
voiceClientAvgCallDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceClientAvgCallDuration.setStatus("current")
_WlsxVoiceCallCtrPerClientInfoGroup_ObjectIdentity = ObjectIdentity
wlsxVoiceCallCtrPerClientInfoGroup = _WlsxVoiceCallCtrPerClientInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 4)
)
_WlsxVoiceCallCtrPerClientTotal_Type = Unsigned32
_WlsxVoiceCallCtrPerClientTotal_Object = MibScalar
wlsxVoiceCallCtrPerClientTotal = _WlsxVoiceCallCtrPerClientTotal_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 4, 1),
    _WlsxVoiceCallCtrPerClientTotal_Type()
)
wlsxVoiceCallCtrPerClientTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxVoiceCallCtrPerClientTotal.setStatus("current")
_WlsxVoiceCallCtrPerClientTable_Object = MibTable
wlsxVoiceCallCtrPerClientTable = _WlsxVoiceCallCtrPerClientTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 4, 2)
)
if mibBuilder.loadTexts:
    wlsxVoiceCallCtrPerClientTable.setStatus("current")
_WlsxVoiceCallCtrPerClientEntry_Object = MibTableRow
wlsxVoiceCallCtrPerClientEntry = _WlsxVoiceCallCtrPerClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 4, 2, 1)
)
wlsxVoiceCallCtrPerClientEntry.setIndexNames(
    (0, "WLSX-WLAN-MIB", "wlanStaPhyAddress"),
)
if mibBuilder.loadTexts:
    wlsxVoiceCallCtrPerClientEntry.setStatus("current")
_VoiceCallCtrTotal_Type = Unsigned32
_VoiceCallCtrTotal_Object = MibTableColumn
voiceCallCtrTotal = _VoiceCallCtrTotal_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 4, 2, 1, 1),
    _VoiceCallCtrTotal_Type()
)
voiceCallCtrTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCallCtrTotal.setStatus("current")
_VoiceCallCtrSuccess_Type = Unsigned32
_VoiceCallCtrSuccess_Object = MibTableColumn
voiceCallCtrSuccess = _VoiceCallCtrSuccess_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 4, 2, 1, 2),
    _VoiceCallCtrSuccess_Type()
)
voiceCallCtrSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCallCtrSuccess.setStatus("current")
_VoiceCallCtrFailed_Type = Unsigned32
_VoiceCallCtrFailed_Object = MibTableColumn
voiceCallCtrFailed = _VoiceCallCtrFailed_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 4, 2, 1, 3),
    _VoiceCallCtrFailed_Type()
)
voiceCallCtrFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCallCtrFailed.setStatus("current")
_VoiceCallCtrRejected_Type = Unsigned32
_VoiceCallCtrRejected_Object = MibTableColumn
voiceCallCtrRejected = _VoiceCallCtrRejected_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 4, 2, 1, 4),
    _VoiceCallCtrRejected_Type()
)
voiceCallCtrRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCallCtrRejected.setStatus("current")
_VoiceCallCtrAborted_Type = Unsigned32
_VoiceCallCtrAborted_Object = MibTableColumn
voiceCallCtrAborted = _VoiceCallCtrAborted_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 4, 2, 1, 5),
    _VoiceCallCtrAborted_Type()
)
voiceCallCtrAborted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCallCtrAborted.setStatus("current")
_VoiceCallCtrOrig_Type = Unsigned32
_VoiceCallCtrOrig_Object = MibTableColumn
voiceCallCtrOrig = _VoiceCallCtrOrig_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 4, 2, 1, 6),
    _VoiceCallCtrOrig_Type()
)
voiceCallCtrOrig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCallCtrOrig.setStatus("current")
_VoiceCallCtrRecvd_Type = Unsigned32
_VoiceCallCtrRecvd_Object = MibTableColumn
voiceCallCtrRecvd = _VoiceCallCtrRecvd_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 4, 2, 1, 7),
    _VoiceCallCtrRecvd_Type()
)
voiceCallCtrRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCallCtrRecvd.setStatus("current")
_VoiceCallCtrActive_Type = Unsigned32
_VoiceCallCtrActive_Object = MibTableColumn
voiceCallCtrActive = _VoiceCallCtrActive_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 4, 2, 1, 8),
    _VoiceCallCtrActive_Type()
)
voiceCallCtrActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCallCtrActive.setStatus("current")
_WlsxVoiceClientLocationInfoGroup_ObjectIdentity = ObjectIdentity
wlsxVoiceClientLocationInfoGroup = _WlsxVoiceClientLocationInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 5)
)
_WlsxVoiceClientLocationTotal_Type = Unsigned32
_WlsxVoiceClientLocationTotal_Object = MibScalar
wlsxVoiceClientLocationTotal = _WlsxVoiceClientLocationTotal_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 5, 1),
    _WlsxVoiceClientLocationTotal_Type()
)
wlsxVoiceClientLocationTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxVoiceClientLocationTotal.setStatus("current")
_WlsxVoiceClientLocationTable_Object = MibTable
wlsxVoiceClientLocationTable = _WlsxVoiceClientLocationTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 5, 2)
)
if mibBuilder.loadTexts:
    wlsxVoiceClientLocationTable.setStatus("current")
_WlsxVoiceClientLocationEntry_Object = MibTableRow
wlsxVoiceClientLocationEntry = _WlsxVoiceClientLocationEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 5, 2, 1)
)
wlsxVoiceClientLocationEntry.setIndexNames(
    (0, "WLSX-WLAN-MIB", "wlanStaPhyAddress"),
)
if mibBuilder.loadTexts:
    wlsxVoiceClientLocationEntry.setStatus("current")
_VcLocationIp_Type = IpAddress
_VcLocationIp_Object = MibTableColumn
vcLocationIp = _VcLocationIp_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 5, 2, 1, 1),
    _VcLocationIp_Type()
)
vcLocationIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcLocationIp.setStatus("current")
_VcLocationMac_Type = MacAddress
_VcLocationMac_Object = MibTableColumn
vcLocationMac = _VcLocationMac_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 5, 2, 1, 2),
    _VcLocationMac_Type()
)
vcLocationMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcLocationMac.setStatus("current")
_VcLocationSwitchIp_Type = IpAddress
_VcLocationSwitchIp_Object = MibTableColumn
vcLocationSwitchIp = _VcLocationSwitchIp_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 5, 2, 1, 3),
    _VcLocationSwitchIp_Type()
)
vcLocationSwitchIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcLocationSwitchIp.setStatus("current")
_VcLocationApName_Type = DisplayString
_VcLocationApName_Object = MibTableColumn
vcLocationApName = _VcLocationApName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 5, 2, 1, 4),
    _VcLocationApName_Type()
)
vcLocationApName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcLocationApName.setStatus("current")
_VcLocationApMac_Type = MacAddress
_VcLocationApMac_Object = MibTableColumn
vcLocationApMac = _VcLocationApMac_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 5, 2, 1, 5),
    _VcLocationApMac_Type()
)
vcLocationApMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcLocationApMac.setStatus("current")
_VcLocationApMode_Type = Integer32
_VcLocationApMode_Object = MibTableColumn
vcLocationApMode = _VcLocationApMode_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 5, 2, 1, 6),
    _VcLocationApMode_Type()
)
vcLocationApMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcLocationApMode.setStatus("current")
_VcLocationApLoc_Type = DisplayString
_VcLocationApLoc_Object = MibTableColumn
vcLocationApLoc = _VcLocationApLoc_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 5, 2, 1, 7),
    _VcLocationApLoc_Type()
)
vcLocationApLoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcLocationApLoc.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WLSX-VOICE-MIB",
    **{"wlsxVoiceMIB": wlsxVoiceMIB,
       "wlsxVoiceStatsGroup": wlsxVoiceStatsGroup,
       "wlsxVoiceCdrInfoGroup": wlsxVoiceCdrInfoGroup,
       "wlsxVoiceCdrTotal": wlsxVoiceCdrTotal,
       "wlsxVoiceCdrTable": wlsxVoiceCdrTable,
       "wlsxVoiceCdrEntry": wlsxVoiceCdrEntry,
       "voiceCdrId": voiceCdrId,
       "voiceCdrIp": voiceCdrIp,
       "voiceCdrMac": voiceCdrMac,
       "voiceCdrName": voiceCdrName,
       "voiceCdrDialNum": voiceCdrDialNum,
       "voiceCdrDir": voiceCdrDir,
       "voiceCdrOrigTime": voiceCdrOrigTime,
       "voiceCdrSetupTime": voiceCdrSetupTime,
       "voiceCdrTeardownTime": voiceCdrTeardownTime,
       "voiceCdrStatus": voiceCdrStatus,
       "voiceCdrReason": voiceCdrReason,
       "voiceCdrDuration": voiceCdrDuration,
       "voiceCdrRValueA": voiceCdrRValueA,
       "voiceCdrApSwitchDelay": voiceCdrApSwitchDelay,
       "voiceCdrCodec": voiceCdrCodec,
       "voiceCdrApName": voiceCdrApName,
       "voiceCdrApMac": voiceCdrApMac,
       "voiceCdrBssid": voiceCdrBssid,
       "voiceCdrEssid": voiceCdrEssid,
       "voiceCdrHandovers": voiceCdrHandovers,
       "voiceCdrMOS": voiceCdrMOS,
       "voiceCdrDelayA": voiceCdrDelayA,
       "voiceCdrJitterA": voiceCdrJitterA,
       "voiceCdrPktLossA": voiceCdrPktLossA,
       "voiceCdrRValueC": voiceCdrRValueC,
       "voiceCdrDelayC": voiceCdrDelayC,
       "voiceCdrJitterC": voiceCdrJitterC,
       "voiceCdrPktLossC": voiceCdrPktLossC,
       "wlsxVoiceCallCtrsGroup": wlsxVoiceCallCtrsGroup,
       "voiceCallCtrsTotal": voiceCallCtrsTotal,
       "voiceCallCtrsSuccess": voiceCallCtrsSuccess,
       "voiceCallCtrsFailed": voiceCallCtrsFailed,
       "voiceCallCtrsRejected": voiceCallCtrsRejected,
       "voiceCallCtrsAborted": voiceCallCtrsAborted,
       "voiceCallCtrsOrig": voiceCallCtrsOrig,
       "voiceCallCtrsRecvd": voiceCallCtrsRecvd,
       "voiceCallCtrsActive": voiceCallCtrsActive,
       "voiceCallCtrsNotFnd": voiceCallCtrsNotFnd,
       "voiceCallCtrsBusy": voiceCallCtrsBusy,
       "voiceCallCtrsSvc": voiceCallCtrsSvc,
       "voiceCallCtrsReqTerm": voiceCallCtrsReqTerm,
       "voiceCallCtrsDecline": voiceCallCtrsDecline,
       "voiceCallCtrsUnauth": voiceCallCtrsUnauth,
       "voiceCallCtrsMisc": voiceCallCtrsMisc,
       "wlsxVoiceClientInfoGroup": wlsxVoiceClientInfoGroup,
       "wlsxVoiceClientTotal": wlsxVoiceClientTotal,
       "wlsxVoiceClientTable": wlsxVoiceClientTable,
       "wlsxVoiceClientEntry": wlsxVoiceClientEntry,
       "voiceClientIp": voiceClientIp,
       "voiceClientProtocol": voiceClientProtocol,
       "voiceClientRegState": voiceClientRegState,
       "voiceClientContactName": voiceClientContactName,
       "voiceClientServerName": voiceClientServerName,
       "voiceClientEssid": voiceClientEssid,
       "voiceClientVlanId": voiceClientVlanId,
       "voiceClientTunnelId": voiceClientTunnelId,
       "voiceClientAvgDelay": voiceClientAvgDelay,
       "voiceClientAvgJitter": voiceClientAvgJitter,
       "voiceClientAvgPktLoss": voiceClientAvgPktLoss,
       "voiceClientAvgCallDuration": voiceClientAvgCallDuration,
       "wlsxVoiceCallCtrPerClientInfoGroup": wlsxVoiceCallCtrPerClientInfoGroup,
       "wlsxVoiceCallCtrPerClientTotal": wlsxVoiceCallCtrPerClientTotal,
       "wlsxVoiceCallCtrPerClientTable": wlsxVoiceCallCtrPerClientTable,
       "wlsxVoiceCallCtrPerClientEntry": wlsxVoiceCallCtrPerClientEntry,
       "voiceCallCtrTotal": voiceCallCtrTotal,
       "voiceCallCtrSuccess": voiceCallCtrSuccess,
       "voiceCallCtrFailed": voiceCallCtrFailed,
       "voiceCallCtrRejected": voiceCallCtrRejected,
       "voiceCallCtrAborted": voiceCallCtrAborted,
       "voiceCallCtrOrig": voiceCallCtrOrig,
       "voiceCallCtrRecvd": voiceCallCtrRecvd,
       "voiceCallCtrActive": voiceCallCtrActive,
       "wlsxVoiceClientLocationInfoGroup": wlsxVoiceClientLocationInfoGroup,
       "wlsxVoiceClientLocationTotal": wlsxVoiceClientLocationTotal,
       "wlsxVoiceClientLocationTable": wlsxVoiceClientLocationTable,
       "wlsxVoiceClientLocationEntry": wlsxVoiceClientLocationEntry,
       "vcLocationIp": vcLocationIp,
       "vcLocationMac": vcLocationMac,
       "vcLocationSwitchIp": vcLocationSwitchIp,
       "vcLocationApName": vcLocationApName,
       "vcLocationApMac": vcLocationApMac,
       "vcLocationApMode": vcLocationApMode,
       "vcLocationApLoc": vcLocationApLoc}
)
