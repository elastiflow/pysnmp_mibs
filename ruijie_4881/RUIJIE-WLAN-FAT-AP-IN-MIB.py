# SNMP MIB module (RUIJIE-WLAN-FAT-AP-IN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-WLAN-FAT-AP-IN-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 10:59:00 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ruijieApgWlanId,) = mibBuilder.importSymbols(
    "RUIJIE-AC-MGMT-MIB",
    "ruijieApgWlanId")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ruijieStandardmibmodule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82)
)
if mibBuilder.loadTexts:
    ruijieStandardmibmodule.setRevisions(
        ("2010-02-28 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieStandardTraps_ObjectIdentity = ObjectIdentity
ruijieStandardTraps = _RuijieStandardTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 0)
)
_RuijieConfigInfoObjects_ObjectIdentity = ObjectIdentity
ruijieConfigInfoObjects = _RuijieConfigInfoObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 1)
)
_RuijieSysInfoConfig_ObjectIdentity = ObjectIdentity
ruijieSysInfoConfig = _RuijieSysInfoConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 1, 1)
)
_RuijieDomain_Type = DisplayString
_RuijieDomain_Object = MibScalar
ruijieDomain = _RuijieDomain_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 1, 1, 1),
    _RuijieDomain_Type()
)
ruijieDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDomain.setStatus("current")
_RuijieLayer2Isolate_Type = Integer32
_RuijieLayer2Isolate_Object = MibScalar
ruijieLayer2Isolate = _RuijieLayer2Isolate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 1, 1, 2),
    _RuijieLayer2Isolate_Type()
)
ruijieLayer2Isolate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieLayer2Isolate.setStatus("current")
_RuijieDosAttackProtect_Type = Integer32
_RuijieDosAttackProtect_Object = MibScalar
ruijieDosAttackProtect = _RuijieDosAttackProtect_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 1, 1, 3),
    _RuijieDosAttackProtect_Type()
)
ruijieDosAttackProtect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDosAttackProtect.setStatus("current")
_RuijieVlanConfigTable_Object = MibTable
ruijieVlanConfigTable = _RuijieVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 1, 1, 4)
)
if mibBuilder.loadTexts:
    ruijieVlanConfigTable.setStatus("current")
_RuijieVlanConfigEntry_Object = MibTableRow
ruijieVlanConfigEntry = _RuijieVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 1, 1, 4, 1)
)
ruijieVlanConfigEntry.setIndexNames(
    (0, "RUIJIE-WLAN-FAT-AP-IN-MIB", "ruijieWlanId"),
)
if mibBuilder.loadTexts:
    ruijieVlanConfigEntry.setStatus("current")
_RuijieVlanId_Type = Integer32
_RuijieVlanId_Object = MibTableColumn
ruijieVlanId = _RuijieVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 1, 1, 4, 1, 1),
    _RuijieVlanId_Type()
)
ruijieVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieVlanId.setStatus("current")
_RuijieSSID_Type = DisplayString
_RuijieSSID_Object = MibTableColumn
ruijieSSID = _RuijieSSID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 1, 1, 4, 1, 2),
    _RuijieSSID_Type()
)
ruijieSSID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieSSID.setStatus("current")
_RuijieRadioInfoConfig_ObjectIdentity = ObjectIdentity
ruijieRadioInfoConfig = _RuijieRadioInfoConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 1, 2)
)
_RuijieRadioConfigTable_Object = MibTable
ruijieRadioConfigTable = _RuijieRadioConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ruijieRadioConfigTable.setStatus("current")
_RuijieRadioConfigEntry_Object = MibTableRow
ruijieRadioConfigEntry = _RuijieRadioConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 1, 2, 1, 1)
)
ruijieRadioConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ruijieRadioConfigEntry.setStatus("current")
_RuijieSSIDNum_Type = Integer32
_RuijieSSIDNum_Object = MibTableColumn
ruijieSSIDNum = _RuijieSSIDNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 1, 2, 1, 1, 1),
    _RuijieSSIDNum_Type()
)
ruijieSSIDNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSSIDNum.setStatus("current")
_RuijieRadioSecurityMch_Type = Integer32
_RuijieRadioSecurityMch_Object = MibTableColumn
ruijieRadioSecurityMch = _RuijieRadioSecurityMch_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 1, 2, 1, 1, 2),
    _RuijieRadioSecurityMch_Type()
)
ruijieRadioSecurityMch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRadioSecurityMch.setStatus("current")
_RuijieRadioSecurityParam_Type = DisplayString
_RuijieRadioSecurityParam_Object = MibTableColumn
ruijieRadioSecurityParam = _RuijieRadioSecurityParam_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 1, 2, 1, 1, 3),
    _RuijieRadioSecurityParam_Type()
)
ruijieRadioSecurityParam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRadioSecurityParam.setStatus("current")
_RuijieRadioQos_Type = Integer32
_RuijieRadioQos_Object = MibTableColumn
ruijieRadioQos = _RuijieRadioQos_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 1, 2, 1, 1, 4),
    _RuijieRadioQos_Type()
)
ruijieRadioQos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRadioQos.setStatus("current")
_RuijieRtsCtsThreshold_Type = Integer32
_RuijieRtsCtsThreshold_Object = MibTableColumn
ruijieRtsCtsThreshold = _RuijieRtsCtsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 1, 2, 1, 1, 5),
    _RuijieRtsCtsThreshold_Type()
)
ruijieRtsCtsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRtsCtsThreshold.setStatus("current")
_RuijieMaxUserPermit_Type = Integer32
_RuijieMaxUserPermit_Object = MibTableColumn
ruijieMaxUserPermit = _RuijieMaxUserPermit_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 1, 2, 1, 1, 6),
    _RuijieMaxUserPermit_Type()
)
ruijieMaxUserPermit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieMaxUserPermit.setStatus("current")
_RuijieUserNumOnLine_Type = Integer32
_RuijieUserNumOnLine_Object = MibTableColumn
ruijieUserNumOnLine = _RuijieUserNumOnLine_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 1, 2, 1, 1, 7),
    _RuijieUserNumOnLine_Type()
)
ruijieUserNumOnLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieUserNumOnLine.setStatus("current")
_RuijieAirInterfaceType_Type = Integer32
_RuijieAirInterfaceType_Object = MibTableColumn
ruijieAirInterfaceType = _RuijieAirInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 1, 2, 1, 1, 8),
    _RuijieAirInterfaceType_Type()
)
ruijieAirInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAirInterfaceType.setStatus("current")
_RuijieChannelMode_Type = Integer32
_RuijieChannelMode_Object = MibTableColumn
ruijieChannelMode = _RuijieChannelMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 1, 2, 1, 1, 9),
    _RuijieChannelMode_Type()
)
ruijieChannelMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieChannelMode.setStatus("current")
_RuijieCurrentChannel_Type = Integer32
_RuijieCurrentChannel_Object = MibTableColumn
ruijieCurrentChannel = _RuijieCurrentChannel_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 1, 2, 1, 1, 10),
    _RuijieCurrentChannel_Type()
)
ruijieCurrentChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieCurrentChannel.setStatus("current")
_RuijieSNR_Type = Integer32
_RuijieSNR_Object = MibTableColumn
ruijieSNR = _RuijieSNR_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 1, 2, 1, 1, 11),
    _RuijieSNR_Type()
)
ruijieSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSNR.setStatus("current")
_RuijieHoppingTimes_Type = Integer32
_RuijieHoppingTimes_Object = MibTableColumn
ruijieHoppingTimes = _RuijieHoppingTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 1, 2, 1, 1, 12),
    _RuijieHoppingTimes_Type()
)
ruijieHoppingTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieHoppingTimes.setStatus("current")
_RuijieHopDetectItvTime_Type = Integer32
_RuijieHopDetectItvTime_Object = MibTableColumn
ruijieHopDetectItvTime = _RuijieHopDetectItvTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 1, 2, 1, 1, 13),
    _RuijieHopDetectItvTime_Type()
)
ruijieHopDetectItvTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieHopDetectItvTime.setStatus("current")
_RuijiePowerMgr_Type = Integer32
_RuijiePowerMgr_Object = MibTableColumn
ruijiePowerMgr = _RuijiePowerMgr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 1, 2, 1, 1, 14),
    _RuijiePowerMgr_Type()
)
ruijiePowerMgr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiePowerMgr.setStatus("current")
_RuijieTxPower_Type = Integer32
_RuijieTxPower_Object = MibTableColumn
ruijieTxPower = _RuijieTxPower_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 1, 2, 1, 1, 15),
    _RuijieTxPower_Type()
)
ruijieTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieTxPower.setStatus("current")
_RuijieWapiConfig_ObjectIdentity = ObjectIdentity
ruijieWapiConfig = _RuijieWapiConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 1, 3)
)
_RuijieWapiConfigTable_Object = MibTable
ruijieWapiConfigTable = _RuijieWapiConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ruijieWapiConfigTable.setStatus("current")
_RuijieWapiConfigEntry_Object = MibTableRow
ruijieWapiConfigEntry = _RuijieWapiConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 1, 3, 1, 1)
)
ruijieWapiConfigEntry.setIndexNames(
    (0, "RUIJIE-WLAN-FAT-AP-IN-MIB", "ruijieWlanId"),
)
if mibBuilder.loadTexts:
    ruijieWapiConfigEntry.setStatus("current")
_RuijieWlanId_Type = Integer32
_RuijieWlanId_Object = MibTableColumn
ruijieWlanId = _RuijieWlanId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 1, 3, 1, 1, 1),
    _RuijieWlanId_Type()
)
ruijieWlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWlanId.setStatus("current")
_RuijieTrustASCfg_Type = Integer32
_RuijieTrustASCfg_Object = MibTableColumn
ruijieTrustASCfg = _RuijieTrustASCfg_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 1, 3, 1, 1, 2),
    _RuijieTrustASCfg_Type()
)
ruijieTrustASCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieTrustASCfg.setStatus("current")
_RuijieCertType_Type = Integer32
_RuijieCertType_Object = MibTableColumn
ruijieCertType = _RuijieCertType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 1, 3, 1, 1, 3),
    _RuijieCertType_Type()
)
ruijieCertType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCertType.setStatus("current")
_RuijieCertState_Type = Integer32
_RuijieCertState_Object = MibTableColumn
ruijieCertState = _RuijieCertState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 1, 3, 1, 1, 4),
    _RuijieCertState_Type()
)
ruijieCertState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCertState.setStatus("current")
_RuijieCertSetup_Type = Integer32
_RuijieCertSetup_Object = MibTableColumn
ruijieCertSetup = _RuijieCertSetup_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 1, 3, 1, 1, 5),
    _RuijieCertSetup_Type()
)
ruijieCertSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieCertSetup.setStatus("current")
_RuijieAdminInfoConfig_ObjectIdentity = ObjectIdentity
ruijieAdminInfoConfig = _RuijieAdminInfoConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 1, 4)
)


class _RuijieAdminName_Type(DisplayString):
    """Custom type ruijieAdminName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieAdminName_Type.__name__ = "DisplayString"
_RuijieAdminName_Object = MibScalar
ruijieAdminName = _RuijieAdminName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 1, 4, 1),
    _RuijieAdminName_Type()
)
ruijieAdminName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAdminName.setStatus("current")


class _RuijieAdminPwd_Type(DisplayString):
    """Custom type ruijieAdminPwd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieAdminPwd_Type.__name__ = "DisplayString"
_RuijieAdminPwd_Object = MibScalar
ruijieAdminPwd = _RuijieAdminPwd_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 1, 4, 2),
    _RuijieAdminPwd_Type()
)
ruijieAdminPwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAdminPwd.setStatus("current")
_RuijiePollTimeConfig_ObjectIdentity = ObjectIdentity
ruijiePollTimeConfig = _RuijiePollTimeConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 1, 5)
)
_RuijiePollTimeOfLast_Type = TimeTicks
_RuijiePollTimeOfLast_Object = MibScalar
ruijiePollTimeOfLast = _RuijiePollTimeOfLast_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 1, 5, 1),
    _RuijiePollTimeOfLast_Type()
)
ruijiePollTimeOfLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePollTimeOfLast.setStatus("current")
_RuijiePerformanceStatObjects_ObjectIdentity = ObjectIdentity
ruijiePerformanceStatObjects = _RuijiePerformanceStatObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2)
)
_RuijieAirIfServiceStat_ObjectIdentity = ObjectIdentity
ruijieAirIfServiceStat = _RuijieAirIfServiceStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 1)
)
_RuijieUplinkTotalDataFrameNum_Type = Integer32
_RuijieUplinkTotalDataFrameNum_Object = MibScalar
ruijieUplinkTotalDataFrameNum = _RuijieUplinkTotalDataFrameNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 1, 1),
    _RuijieUplinkTotalDataFrameNum_Type()
)
ruijieUplinkTotalDataFrameNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieUplinkTotalDataFrameNum.setStatus("current")
_RuijieDownlinkTotalDataFrameNum_Type = Integer32
_RuijieDownlinkTotalDataFrameNum_Object = MibScalar
ruijieDownlinkTotalDataFrameNum = _RuijieDownlinkTotalDataFrameNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 1, 2),
    _RuijieDownlinkTotalDataFrameNum_Type()
)
ruijieDownlinkTotalDataFrameNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDownlinkTotalDataFrameNum.setStatus("current")
_RuijieDownlinkTotalLostDataFrameNum_Type = Integer32
_RuijieDownlinkTotalLostDataFrameNum_Object = MibScalar
ruijieDownlinkTotalLostDataFrameNum = _RuijieDownlinkTotalLostDataFrameNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 1, 3),
    _RuijieDownlinkTotalLostDataFrameNum_Type()
)
ruijieDownlinkTotalLostDataFrameNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDownlinkTotalLostDataFrameNum.setStatus("current")
_RuijieTotalSignalFrameNum_Type = Integer32
_RuijieTotalSignalFrameNum_Object = MibScalar
ruijieTotalSignalFrameNum = _RuijieTotalSignalFrameNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 1, 4),
    _RuijieTotalSignalFrameNum_Type()
)
ruijieTotalSignalFrameNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieTotalSignalFrameNum.setStatus("current")
_RuijieCorrectPkgByteRxByMAC_Type = Integer32
_RuijieCorrectPkgByteRxByMAC_Object = MibScalar
ruijieCorrectPkgByteRxByMAC = _RuijieCorrectPkgByteRxByMAC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 1, 5),
    _RuijieCorrectPkgByteRxByMAC_Type()
)
ruijieCorrectPkgByteRxByMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCorrectPkgByteRxByMAC.setStatus("current")
_RuijiePkgByteTxByMAC_Type = Integer32
_RuijiePkgByteTxByMAC_Object = MibScalar
ruijiePkgByteTxByMAC = _RuijiePkgByteTxByMAC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 1, 6),
    _RuijiePkgByteTxByMAC_Type()
)
ruijiePkgByteTxByMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePkgByteTxByMAC.setStatus("current")
_RuijieUplinkPortFlow_Type = Integer32
_RuijieUplinkPortFlow_Object = MibScalar
ruijieUplinkPortFlow = _RuijieUplinkPortFlow_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 1, 7),
    _RuijieUplinkPortFlow_Type()
)
ruijieUplinkPortFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieUplinkPortFlow.setStatus("current")
_RuijieDownlinkPortFlow_Type = Integer32
_RuijieDownlinkPortFlow_Object = MibScalar
ruijieDownlinkPortFlow = _RuijieDownlinkPortFlow_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 1, 8),
    _RuijieDownlinkPortFlow_Type()
)
ruijieDownlinkPortFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDownlinkPortFlow.setStatus("current")
_RuijieTermServiceStat_ObjectIdentity = ObjectIdentity
ruijieTermServiceStat = _RuijieTermServiceStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 2)
)
_RuijieTotalUserNum_Type = Integer32
_RuijieTotalUserNum_Object = MibScalar
ruijieTotalUserNum = _RuijieTotalUserNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 2, 1),
    _RuijieTotalUserNum_Type()
)
ruijieTotalUserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieTotalUserNum.setStatus("current")
_RuijieUserAccumulateTime_Type = Integer32
_RuijieUserAccumulateTime_Object = MibScalar
ruijieUserAccumulateTime = _RuijieUserAccumulateTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 2, 2),
    _RuijieUserAccumulateTime_Type()
)
ruijieUserAccumulateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieUserAccumulateTime.setStatus("current")
_RuijieTermServiceStatSSIDTable_Object = MibTable
ruijieTermServiceStatSSIDTable = _RuijieTermServiceStatSSIDTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 2, 34)
)
if mibBuilder.loadTexts:
    ruijieTermServiceStatSSIDTable.setStatus("current")
_RuijieTermServiceStatSSIDEntry_Object = MibTableRow
ruijieTermServiceStatSSIDEntry = _RuijieTermServiceStatSSIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 2, 34, 1)
)
ruijieTermServiceStatSSIDEntry.setIndexNames(
    (0, "RUIJIE-WLAN-FAT-AP-IN-MIB", "ruijieWlanId"),
)
if mibBuilder.loadTexts:
    ruijieTermServiceStatSSIDEntry.setStatus("current")
_RuijieCorrectPkgByteRxByMACBySSID_Type = Integer32
_RuijieCorrectPkgByteRxByMACBySSID_Object = MibTableColumn
ruijieCorrectPkgByteRxByMACBySSID = _RuijieCorrectPkgByteRxByMACBySSID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 2, 34, 1, 1),
    _RuijieCorrectPkgByteRxByMACBySSID_Type()
)
ruijieCorrectPkgByteRxByMACBySSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCorrectPkgByteRxByMACBySSID.setStatus("current")
_RuijiePkgByteTxByMACBySSID_Type = Integer32
_RuijiePkgByteTxByMACBySSID_Object = MibTableColumn
ruijiePkgByteTxByMACBySSID = _RuijiePkgByteTxByMACBySSID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 2, 34, 1, 2),
    _RuijiePkgByteTxByMACBySSID_Type()
)
ruijiePkgByteTxByMACBySSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePkgByteTxByMACBySSID.setStatus("current")
_RuijieAirIfResUsageRatio_Type = Integer32
_RuijieAirIfResUsageRatio_Object = MibTableColumn
ruijieAirIfResUsageRatio = _RuijieAirIfResUsageRatio_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 2, 34, 1, 3),
    _RuijieAirIfResUsageRatio_Type()
)
ruijieAirIfResUsageRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAirIfResUsageRatio.setStatus("current")
_RuijieTotalAssociationUserNum_Type = Integer32
_RuijieTotalAssociationUserNum_Object = MibTableColumn
ruijieTotalAssociationUserNum = _RuijieTotalAssociationUserNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 2, 34, 1, 4),
    _RuijieTotalAssociationUserNum_Type()
)
ruijieTotalAssociationUserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieTotalAssociationUserNum.setStatus("current")
_RuijieOnlineUserNum_Type = Integer32
_RuijieOnlineUserNum_Object = MibTableColumn
ruijieOnlineUserNum = _RuijieOnlineUserNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 2, 34, 1, 5),
    _RuijieOnlineUserNum_Type()
)
ruijieOnlineUserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOnlineUserNum.setStatus("current")
_RuijieUserReqAccessTimes_Type = Integer32
_RuijieUserReqAccessTimes_Object = MibTableColumn
ruijieUserReqAccessTimes = _RuijieUserReqAccessTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 2, 34, 1, 6),
    _RuijieUserReqAccessTimes_Type()
)
ruijieUserReqAccessTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieUserReqAccessTimes.setStatus("current")
_RuijieResponseReqAccessTimes_Type = Integer32
_RuijieResponseReqAccessTimes_Object = MibTableColumn
ruijieResponseReqAccessTimes = _RuijieResponseReqAccessTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 2, 34, 1, 7),
    _RuijieResponseReqAccessTimes_Type()
)
ruijieResponseReqAccessTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieResponseReqAccessTimes.setStatus("current")
_RuijieSuccessAccessTimes_Type = Integer32
_RuijieSuccessAccessTimes_Object = MibTableColumn
ruijieSuccessAccessTimes = _RuijieSuccessAccessTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 2, 34, 1, 8),
    _RuijieSuccessAccessTimes_Type()
)
ruijieSuccessAccessTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSuccessAccessTimes.setStatus("current")
_RuijieIneffiLinkVerifyFailTime_Type = Integer32
_RuijieIneffiLinkVerifyFailTime_Object = MibTableColumn
ruijieIneffiLinkVerifyFailTime = _RuijieIneffiLinkVerifyFailTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 2, 34, 1, 9),
    _RuijieIneffiLinkVerifyFailTime_Type()
)
ruijieIneffiLinkVerifyFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIneffiLinkVerifyFailTime.setStatus("current")
_RuijieTimeoutLinkVerifyFailTime_Type = Integer32
_RuijieTimeoutLinkVerifyFailTime_Object = MibTableColumn
ruijieTimeoutLinkVerifyFailTime = _RuijieTimeoutLinkVerifyFailTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 2, 34, 1, 10),
    _RuijieTimeoutLinkVerifyFailTime_Type()
)
ruijieTimeoutLinkVerifyFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieTimeoutLinkVerifyFailTime.setStatus("current")
_RuijieInefficiencyLinkVerifyFailTime_Type = Integer32
_RuijieInefficiencyLinkVerifyFailTime_Object = MibTableColumn
ruijieInefficiencyLinkVerifyFailTime = _RuijieInefficiencyLinkVerifyFailTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 2, 34, 1, 11),
    _RuijieInefficiencyLinkVerifyFailTime_Type()
)
ruijieInefficiencyLinkVerifyFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieInefficiencyLinkVerifyFailTime.setStatus("current")
_RuijieOtherReasonLinkVerifyFailTime_Type = Integer32
_RuijieOtherReasonLinkVerifyFailTime_Object = MibTableColumn
ruijieOtherReasonLinkVerifyFailTime = _RuijieOtherReasonLinkVerifyFailTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 2, 34, 1, 12),
    _RuijieOtherReasonLinkVerifyFailTime_Type()
)
ruijieOtherReasonLinkVerifyFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOtherReasonLinkVerifyFailTime.setStatus("current")
_RuijieIneffiAssociationFailTime_Type = Integer32
_RuijieIneffiAssociationFailTime_Object = MibTableColumn
ruijieIneffiAssociationFailTime = _RuijieIneffiAssociationFailTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 2, 34, 1, 13),
    _RuijieIneffiAssociationFailTime_Type()
)
ruijieIneffiAssociationFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIneffiAssociationFailTime.setStatus("current")
_RuijieTimeoutAssociationFailTime_Type = Integer32
_RuijieTimeoutAssociationFailTime_Object = MibTableColumn
ruijieTimeoutAssociationFailTime = _RuijieTimeoutAssociationFailTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 2, 34, 1, 14),
    _RuijieTimeoutAssociationFailTime_Type()
)
ruijieTimeoutAssociationFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieTimeoutAssociationFailTime.setStatus("current")
_RuijieInefficiencyAssociationFailTime_Type = Integer32
_RuijieInefficiencyAssociationFailTime_Object = MibTableColumn
ruijieInefficiencyAssociationFailTime = _RuijieInefficiencyAssociationFailTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 2, 34, 1, 15),
    _RuijieInefficiencyAssociationFailTime_Type()
)
ruijieInefficiencyAssociationFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieInefficiencyAssociationFailTime.setStatus("current")
_RuijieOtherReasonAssociationFailTime_Type = Integer32
_RuijieOtherReasonAssociationFailTime_Object = MibTableColumn
ruijieOtherReasonAssociationFailTime = _RuijieOtherReasonAssociationFailTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 2, 34, 1, 16),
    _RuijieOtherReasonAssociationFailTime_Type()
)
ruijieOtherReasonAssociationFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOtherReasonAssociationFailTime.setStatus("current")
_RuijieTotalReassociationAtmptTimes_Type = Integer32
_RuijieTotalReassociationAtmptTimes_Object = MibTableColumn
ruijieTotalReassociationAtmptTimes = _RuijieTotalReassociationAtmptTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 2, 34, 1, 17),
    _RuijieTotalReassociationAtmptTimes_Type()
)
ruijieTotalReassociationAtmptTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieTotalReassociationAtmptTimes.setStatus("current")
_RuijieTotalReassociationSuccessTimes_Type = Integer32
_RuijieTotalReassociationSuccessTimes_Object = MibTableColumn
ruijieTotalReassociationSuccessTimes = _RuijieTotalReassociationSuccessTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 2, 34, 1, 18),
    _RuijieTotalReassociationSuccessTimes_Type()
)
ruijieTotalReassociationSuccessTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieTotalReassociationSuccessTimes.setStatus("current")
_RuijieIneffiReassociationFailTime_Type = Integer32
_RuijieIneffiReassociationFailTime_Object = MibTableColumn
ruijieIneffiReassociationFailTime = _RuijieIneffiReassociationFailTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 2, 34, 1, 19),
    _RuijieIneffiReassociationFailTime_Type()
)
ruijieIneffiReassociationFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIneffiReassociationFailTime.setStatus("current")
_RuijieTimeoutReassociationFailTime_Type = Integer32
_RuijieTimeoutReassociationFailTime_Object = MibTableColumn
ruijieTimeoutReassociationFailTime = _RuijieTimeoutReassociationFailTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 2, 34, 1, 20),
    _RuijieTimeoutReassociationFailTime_Type()
)
ruijieTimeoutReassociationFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieTimeoutReassociationFailTime.setStatus("current")
_RuijieInefficiencyReassociationFailTime_Type = Integer32
_RuijieInefficiencyReassociationFailTime_Object = MibTableColumn
ruijieInefficiencyReassociationFailTime = _RuijieInefficiencyReassociationFailTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 2, 34, 1, 21),
    _RuijieInefficiencyReassociationFailTime_Type()
)
ruijieInefficiencyReassociationFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieInefficiencyReassociationFailTime.setStatus("current")
_RuijieOtherReasonReassociationFailTime_Type = Integer32
_RuijieOtherReasonReassociationFailTime_Object = MibTableColumn
ruijieOtherReasonReassociationFailTime = _RuijieOtherReasonReassociationFailTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 2, 34, 1, 22),
    _RuijieOtherReasonReassociationFailTime_Type()
)
ruijieOtherReasonReassociationFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOtherReasonReassociationFailTime.setStatus("current")
_RuijieTotalIdentificationAtmptTimes_Type = Integer32
_RuijieTotalIdentificationAtmptTimes_Object = MibTableColumn
ruijieTotalIdentificationAtmptTimes = _RuijieTotalIdentificationAtmptTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 2, 34, 1, 23),
    _RuijieTotalIdentificationAtmptTimes_Type()
)
ruijieTotalIdentificationAtmptTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieTotalIdentificationAtmptTimes.setStatus("current")
_RuijieTotalIdentificationSuccessTimes_Type = Integer32
_RuijieTotalIdentificationSuccessTimes_Object = MibTableColumn
ruijieTotalIdentificationSuccessTimes = _RuijieTotalIdentificationSuccessTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 2, 34, 1, 24),
    _RuijieTotalIdentificationSuccessTimes_Type()
)
ruijieTotalIdentificationSuccessTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieTotalIdentificationSuccessTimes.setStatus("current")
_RuijiePwdErrorIdentifyFailTime_Type = Integer32
_RuijiePwdErrorIdentifyFailTime_Object = MibTableColumn
ruijiePwdErrorIdentifyFailTime = _RuijiePwdErrorIdentifyFailTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 2, 34, 1, 25),
    _RuijiePwdErrorIdentifyFailTime_Type()
)
ruijiePwdErrorIdentifyFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePwdErrorIdentifyFailTime.setStatus("current")
_RuijieIneffiIdentificationFailTime_Type = Integer32
_RuijieIneffiIdentificationFailTime_Object = MibTableColumn
ruijieIneffiIdentificationFailTime = _RuijieIneffiIdentificationFailTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 2, 34, 1, 26),
    _RuijieIneffiIdentificationFailTime_Type()
)
ruijieIneffiIdentificationFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIneffiIdentificationFailTime.setStatus("current")
_RuijieTimeoutIdentificationFailTime_Type = Integer32
_RuijieTimeoutIdentificationFailTime_Object = MibTableColumn
ruijieTimeoutIdentificationFailTime = _RuijieTimeoutIdentificationFailTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 2, 34, 1, 27),
    _RuijieTimeoutIdentificationFailTime_Type()
)
ruijieTimeoutIdentificationFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieTimeoutIdentificationFailTime.setStatus("current")
_RuijieInefficiencyIdentificationFailTime_Type = Integer32
_RuijieInefficiencyIdentificationFailTime_Object = MibTableColumn
ruijieInefficiencyIdentificationFailTime = _RuijieInefficiencyIdentificationFailTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 2, 34, 1, 28),
    _RuijieInefficiencyIdentificationFailTime_Type()
)
ruijieInefficiencyIdentificationFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieInefficiencyIdentificationFailTime.setStatus("current")
_RuijieOtherReasonIdentificationFailTime_Type = Integer32
_RuijieOtherReasonIdentificationFailTime_Object = MibTableColumn
ruijieOtherReasonIdentificationFailTime = _RuijieOtherReasonIdentificationFailTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 2, 34, 1, 29),
    _RuijieOtherReasonIdentificationFailTime_Type()
)
ruijieOtherReasonIdentificationFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOtherReasonIdentificationFailTime.setStatus("current")
_RuijieTotalRemoveLinkVerifyFailTimes_Type = Integer32
_RuijieTotalRemoveLinkVerifyFailTimes_Object = MibTableColumn
ruijieTotalRemoveLinkVerifyFailTimes = _RuijieTotalRemoveLinkVerifyFailTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 2, 34, 1, 30),
    _RuijieTotalRemoveLinkVerifyFailTimes_Type()
)
ruijieTotalRemoveLinkVerifyFailTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieTotalRemoveLinkVerifyFailTimes.setStatus("current")
_RuijieLeaveAPCoverageRemoveLinkVerifyFailTimes_Type = Integer32
_RuijieLeaveAPCoverageRemoveLinkVerifyFailTimes_Object = MibTableColumn
ruijieLeaveAPCoverageRemoveLinkVerifyFailTimes = _RuijieLeaveAPCoverageRemoveLinkVerifyFailTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 2, 34, 1, 31),
    _RuijieLeaveAPCoverageRemoveLinkVerifyFailTimes_Type()
)
ruijieLeaveAPCoverageRemoveLinkVerifyFailTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieLeaveAPCoverageRemoveLinkVerifyFailTimes.setStatus("current")
_RuijieInefficiencyRemoveLinkVerifyFailTime_Type = Integer32
_RuijieInefficiencyRemoveLinkVerifyFailTime_Object = MibTableColumn
ruijieInefficiencyRemoveLinkVerifyFailTime = _RuijieInefficiencyRemoveLinkVerifyFailTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 2, 34, 1, 32),
    _RuijieInefficiencyRemoveLinkVerifyFailTime_Type()
)
ruijieInefficiencyRemoveLinkVerifyFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieInefficiencyRemoveLinkVerifyFailTime.setStatus("current")
_RuijieLinkVerifyFailRemoveLinkVerifyFailTime_Type = Integer32
_RuijieLinkVerifyFailRemoveLinkVerifyFailTime_Object = MibTableColumn
ruijieLinkVerifyFailRemoveLinkVerifyFailTime = _RuijieLinkVerifyFailRemoveLinkVerifyFailTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 2, 34, 1, 33),
    _RuijieLinkVerifyFailRemoveLinkVerifyFailTime_Type()
)
ruijieLinkVerifyFailRemoveLinkVerifyFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieLinkVerifyFailRemoveLinkVerifyFailTime.setStatus("current")
_RuijieOtherReasonRemoveLinkVerifyFailTime_Type = Integer32
_RuijieOtherReasonRemoveLinkVerifyFailTime_Object = MibTableColumn
ruijieOtherReasonRemoveLinkVerifyFailTime = _RuijieOtherReasonRemoveLinkVerifyFailTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 2, 34, 1, 34),
    _RuijieOtherReasonRemoveLinkVerifyFailTime_Type()
)
ruijieOtherReasonRemoveLinkVerifyFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOtherReasonRemoveLinkVerifyFailTime.setStatus("current")
_RuijieTotalRemoveLinkAssociationTimes_Type = Integer32
_RuijieTotalRemoveLinkAssociationTimes_Object = MibTableColumn
ruijieTotalRemoveLinkAssociationTimes = _RuijieTotalRemoveLinkAssociationTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 2, 34, 1, 35),
    _RuijieTotalRemoveLinkAssociationTimes_Type()
)
ruijieTotalRemoveLinkAssociationTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieTotalRemoveLinkAssociationTimes.setStatus("current")
_RuijieLeaveAPCoverageRemoveAssociationFailTimes_Type = Integer32
_RuijieLeaveAPCoverageRemoveAssociationFailTimes_Object = MibTableColumn
ruijieLeaveAPCoverageRemoveAssociationFailTimes = _RuijieLeaveAPCoverageRemoveAssociationFailTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 2, 34, 1, 36),
    _RuijieLeaveAPCoverageRemoveAssociationFailTimes_Type()
)
ruijieLeaveAPCoverageRemoveAssociationFailTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieLeaveAPCoverageRemoveAssociationFailTimes.setStatus("current")
_RuijieInefficiencyRemoveAssociationFailTime_Type = Integer32
_RuijieInefficiencyRemoveAssociationFailTime_Object = MibTableColumn
ruijieInefficiencyRemoveAssociationFailTime = _RuijieInefficiencyRemoveAssociationFailTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 2, 34, 1, 37),
    _RuijieInefficiencyRemoveAssociationFailTime_Type()
)
ruijieInefficiencyRemoveAssociationFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieInefficiencyRemoveAssociationFailTime.setStatus("current")
_RuijieAssociationFailRemoveAssociationFailTime_Type = Integer32
_RuijieAssociationFailRemoveAssociationFailTime_Object = MibTableColumn
ruijieAssociationFailRemoveAssociationFailTime = _RuijieAssociationFailRemoveAssociationFailTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 2, 34, 1, 38),
    _RuijieAssociationFailRemoveAssociationFailTime_Type()
)
ruijieAssociationFailRemoveAssociationFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAssociationFailRemoveAssociationFailTime.setStatus("current")
_RuijieOtherReasonRemoveAssociationFailTime_Type = Integer32
_RuijieOtherReasonRemoveAssociationFailTime_Object = MibTableColumn
ruijieOtherReasonRemoveAssociationFailTime = _RuijieOtherReasonRemoveAssociationFailTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 2, 34, 1, 39),
    _RuijieOtherReasonRemoveAssociationFailTime_Type()
)
ruijieOtherReasonRemoveAssociationFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOtherReasonRemoveAssociationFailTime.setStatus("current")
_RuijieUserMacAddrTable_Object = MibTable
ruijieUserMacAddrTable = _RuijieUserMacAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 2, 35)
)
if mibBuilder.loadTexts:
    ruijieUserMacAddrTable.setStatus("current")
_RuijieUserMacAddrEntry_Object = MibTableRow
ruijieUserMacAddrEntry = _RuijieUserMacAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 2, 35, 1)
)
ruijieUserMacAddrEntry.setIndexNames(
    (0, "RUIJIE-WLAN-FAT-AP-IN-MIB", "ruijieWlanId"),
    (0, "RUIJIE-WLAN-FAT-AP-IN-MIB", "ruijieTerminalIndex"),
)
if mibBuilder.loadTexts:
    ruijieUserMacAddrEntry.setStatus("current")
_RuijieTerminalIndex_Type = Integer32
_RuijieTerminalIndex_Object = MibTableColumn
ruijieTerminalIndex = _RuijieTerminalIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 2, 35, 1, 1),
    _RuijieTerminalIndex_Type()
)
ruijieTerminalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieTerminalIndex.setStatus("current")
_RuijieUserMacAdddr_Type = MacAddress
_RuijieUserMacAdddr_Object = MibTableColumn
ruijieUserMacAdddr = _RuijieUserMacAdddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 2, 35, 1, 2),
    _RuijieUserMacAdddr_Type()
)
ruijieUserMacAdddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieUserMacAdddr.setStatus("current")
_RuijieTermServiceStatTable_Object = MibTable
ruijieTermServiceStatTable = _RuijieTermServiceStatTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 2, 36)
)
if mibBuilder.loadTexts:
    ruijieTermServiceStatTable.setStatus("current")
_RuijieTermServiceStatEntry_Object = MibTableRow
ruijieTermServiceStatEntry = _RuijieTermServiceStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 2, 36, 1)
)
ruijieTermServiceStatEntry.setIndexNames(
    (0, "RUIJIE-WLAN-FAT-AP-IN-MIB", "ruijieTerminalIndex"),
)
if mibBuilder.loadTexts:
    ruijieTermServiceStatEntry.setStatus("current")
_RuijieTotalReTxFramNum_Type = Integer32
_RuijieTotalReTxFramNum_Object = MibTableColumn
ruijieTotalReTxFramNum = _RuijieTotalReTxFramNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 2, 36, 1, 1),
    _RuijieTotalReTxFramNum_Type()
)
ruijieTotalReTxFramNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieTotalReTxFramNum.setStatus("current")
_RuijieUserOnLineTime_Type = Integer32
_RuijieUserOnLineTime_Object = MibTableColumn
ruijieUserOnLineTime = _RuijieUserOnLineTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 2, 36, 1, 2),
    _RuijieUserOnLineTime_Type()
)
ruijieUserOnLineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieUserOnLineTime.setStatus("current")
_RuijieRevDataFrameNum_Type = Integer32
_RuijieRevDataFrameNum_Object = MibTableColumn
ruijieRevDataFrameNum = _RuijieRevDataFrameNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 2, 36, 1, 3),
    _RuijieRevDataFrameNum_Type()
)
ruijieRevDataFrameNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRevDataFrameNum.setStatus("current")
_RuijieRevErrorDataFrameNum_Type = Integer32
_RuijieRevErrorDataFrameNum_Object = MibTableColumn
ruijieRevErrorDataFrameNum = _RuijieRevErrorDataFrameNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 2, 36, 1, 4),
    _RuijieRevErrorDataFrameNum_Type()
)
ruijieRevErrorDataFrameNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRevErrorDataFrameNum.setStatus("current")
_RuijieSendDataFrameNum_Type = Integer32
_RuijieSendDataFrameNum_Object = MibTableColumn
ruijieSendDataFrameNum = _RuijieSendDataFrameNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 2, 36, 1, 5),
    _RuijieSendDataFrameNum_Type()
)
ruijieSendDataFrameNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSendDataFrameNum.setStatus("current")
_RuijieSendSuccessDataFrameNum_Type = Integer32
_RuijieSendSuccessDataFrameNum_Object = MibTableColumn
ruijieSendSuccessDataFrameNum = _RuijieSendSuccessDataFrameNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 2, 36, 1, 6),
    _RuijieSendSuccessDataFrameNum_Type()
)
ruijieSendSuccessDataFrameNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSendSuccessDataFrameNum.setStatus("current")
_RuijieSendReTxDataFrameNum_Type = Integer32
_RuijieSendReTxDataFrameNum_Object = MibTableColumn
ruijieSendReTxDataFrameNum = _RuijieSendReTxDataFrameNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 2, 36, 1, 7),
    _RuijieSendReTxDataFrameNum_Type()
)
ruijieSendReTxDataFrameNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSendReTxDataFrameNum.setStatus("current")
_RuijieAvgSendRate_Type = Integer32
_RuijieAvgSendRate_Object = MibTableColumn
ruijieAvgSendRate = _RuijieAvgSendRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 2, 36, 1, 8),
    _RuijieAvgSendRate_Type()
)
ruijieAvgSendRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAvgSendRate.setStatus("current")
_RuijieAvgReceiveRate_Type = Integer32
_RuijieAvgReceiveRate_Object = MibTableColumn
ruijieAvgReceiveRate = _RuijieAvgReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 2, 36, 1, 9),
    _RuijieAvgReceiveRate_Type()
)
ruijieAvgReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAvgReceiveRate.setStatus("current")
_RuijieTotalDataThroughput_Type = Integer32
_RuijieTotalDataThroughput_Object = MibTableColumn
ruijieTotalDataThroughput = _RuijieTotalDataThroughput_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 2, 36, 1, 10),
    _RuijieTotalDataThroughput_Type()
)
ruijieTotalDataThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieTotalDataThroughput.setStatus("current")
_RuijieSignalStrength_Type = Integer32
_RuijieSignalStrength_Object = MibTableColumn
ruijieSignalStrength = _RuijieSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 2, 36, 1, 11),
    _RuijieSignalStrength_Type()
)
ruijieSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSignalStrength.setStatus("current")
_RuijieNoise_Type = Integer32
_RuijieNoise_Object = MibTableColumn
ruijieNoise = _RuijieNoise_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 2, 2, 36, 1, 12),
    _RuijieNoise_Type()
)
ruijieNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieNoise.setStatus("current")

# Managed Objects groups


# Notification objects

ruijieRadioPortTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 82, 0, 1)
)
if mibBuilder.loadTexts:
    ruijieRadioPortTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-WLAN-FAT-AP-IN-MIB",
    **{"ruijieStandardmibmodule": ruijieStandardmibmodule,
       "ruijieStandardTraps": ruijieStandardTraps,
       "ruijieRadioPortTrap": ruijieRadioPortTrap,
       "ruijieConfigInfoObjects": ruijieConfigInfoObjects,
       "ruijieSysInfoConfig": ruijieSysInfoConfig,
       "ruijieDomain": ruijieDomain,
       "ruijieLayer2Isolate": ruijieLayer2Isolate,
       "ruijieDosAttackProtect": ruijieDosAttackProtect,
       "ruijieVlanConfigTable": ruijieVlanConfigTable,
       "ruijieVlanConfigEntry": ruijieVlanConfigEntry,
       "ruijieVlanId": ruijieVlanId,
       "ruijieSSID": ruijieSSID,
       "ruijieRadioInfoConfig": ruijieRadioInfoConfig,
       "ruijieRadioConfigTable": ruijieRadioConfigTable,
       "ruijieRadioConfigEntry": ruijieRadioConfigEntry,
       "ruijieSSIDNum": ruijieSSIDNum,
       "ruijieRadioSecurityMch": ruijieRadioSecurityMch,
       "ruijieRadioSecurityParam": ruijieRadioSecurityParam,
       "ruijieRadioQos": ruijieRadioQos,
       "ruijieRtsCtsThreshold": ruijieRtsCtsThreshold,
       "ruijieMaxUserPermit": ruijieMaxUserPermit,
       "ruijieUserNumOnLine": ruijieUserNumOnLine,
       "ruijieAirInterfaceType": ruijieAirInterfaceType,
       "ruijieChannelMode": ruijieChannelMode,
       "ruijieCurrentChannel": ruijieCurrentChannel,
       "ruijieSNR": ruijieSNR,
       "ruijieHoppingTimes": ruijieHoppingTimes,
       "ruijieHopDetectItvTime": ruijieHopDetectItvTime,
       "ruijiePowerMgr": ruijiePowerMgr,
       "ruijieTxPower": ruijieTxPower,
       "ruijieWapiConfig": ruijieWapiConfig,
       "ruijieWapiConfigTable": ruijieWapiConfigTable,
       "ruijieWapiConfigEntry": ruijieWapiConfigEntry,
       "ruijieWlanId": ruijieWlanId,
       "ruijieTrustASCfg": ruijieTrustASCfg,
       "ruijieCertType": ruijieCertType,
       "ruijieCertState": ruijieCertState,
       "ruijieCertSetup": ruijieCertSetup,
       "ruijieAdminInfoConfig": ruijieAdminInfoConfig,
       "ruijieAdminName": ruijieAdminName,
       "ruijieAdminPwd": ruijieAdminPwd,
       "ruijiePollTimeConfig": ruijiePollTimeConfig,
       "ruijiePollTimeOfLast": ruijiePollTimeOfLast,
       "ruijiePerformanceStatObjects": ruijiePerformanceStatObjects,
       "ruijieAirIfServiceStat": ruijieAirIfServiceStat,
       "ruijieUplinkTotalDataFrameNum": ruijieUplinkTotalDataFrameNum,
       "ruijieDownlinkTotalDataFrameNum": ruijieDownlinkTotalDataFrameNum,
       "ruijieDownlinkTotalLostDataFrameNum": ruijieDownlinkTotalLostDataFrameNum,
       "ruijieTotalSignalFrameNum": ruijieTotalSignalFrameNum,
       "ruijieCorrectPkgByteRxByMAC": ruijieCorrectPkgByteRxByMAC,
       "ruijiePkgByteTxByMAC": ruijiePkgByteTxByMAC,
       "ruijieUplinkPortFlow": ruijieUplinkPortFlow,
       "ruijieDownlinkPortFlow": ruijieDownlinkPortFlow,
       "ruijieTermServiceStat": ruijieTermServiceStat,
       "ruijieTotalUserNum": ruijieTotalUserNum,
       "ruijieUserAccumulateTime": ruijieUserAccumulateTime,
       "ruijieTermServiceStatSSIDTable": ruijieTermServiceStatSSIDTable,
       "ruijieTermServiceStatSSIDEntry": ruijieTermServiceStatSSIDEntry,
       "ruijieCorrectPkgByteRxByMACBySSID": ruijieCorrectPkgByteRxByMACBySSID,
       "ruijiePkgByteTxByMACBySSID": ruijiePkgByteTxByMACBySSID,
       "ruijieAirIfResUsageRatio": ruijieAirIfResUsageRatio,
       "ruijieTotalAssociationUserNum": ruijieTotalAssociationUserNum,
       "ruijieOnlineUserNum": ruijieOnlineUserNum,
       "ruijieUserReqAccessTimes": ruijieUserReqAccessTimes,
       "ruijieResponseReqAccessTimes": ruijieResponseReqAccessTimes,
       "ruijieSuccessAccessTimes": ruijieSuccessAccessTimes,
       "ruijieIneffiLinkVerifyFailTime": ruijieIneffiLinkVerifyFailTime,
       "ruijieTimeoutLinkVerifyFailTime": ruijieTimeoutLinkVerifyFailTime,
       "ruijieInefficiencyLinkVerifyFailTime": ruijieInefficiencyLinkVerifyFailTime,
       "ruijieOtherReasonLinkVerifyFailTime": ruijieOtherReasonLinkVerifyFailTime,
       "ruijieIneffiAssociationFailTime": ruijieIneffiAssociationFailTime,
       "ruijieTimeoutAssociationFailTime": ruijieTimeoutAssociationFailTime,
       "ruijieInefficiencyAssociationFailTime": ruijieInefficiencyAssociationFailTime,
       "ruijieOtherReasonAssociationFailTime": ruijieOtherReasonAssociationFailTime,
       "ruijieTotalReassociationAtmptTimes": ruijieTotalReassociationAtmptTimes,
       "ruijieTotalReassociationSuccessTimes": ruijieTotalReassociationSuccessTimes,
       "ruijieIneffiReassociationFailTime": ruijieIneffiReassociationFailTime,
       "ruijieTimeoutReassociationFailTime": ruijieTimeoutReassociationFailTime,
       "ruijieInefficiencyReassociationFailTime": ruijieInefficiencyReassociationFailTime,
       "ruijieOtherReasonReassociationFailTime": ruijieOtherReasonReassociationFailTime,
       "ruijieTotalIdentificationAtmptTimes": ruijieTotalIdentificationAtmptTimes,
       "ruijieTotalIdentificationSuccessTimes": ruijieTotalIdentificationSuccessTimes,
       "ruijiePwdErrorIdentifyFailTime": ruijiePwdErrorIdentifyFailTime,
       "ruijieIneffiIdentificationFailTime": ruijieIneffiIdentificationFailTime,
       "ruijieTimeoutIdentificationFailTime": ruijieTimeoutIdentificationFailTime,
       "ruijieInefficiencyIdentificationFailTime": ruijieInefficiencyIdentificationFailTime,
       "ruijieOtherReasonIdentificationFailTime": ruijieOtherReasonIdentificationFailTime,
       "ruijieTotalRemoveLinkVerifyFailTimes": ruijieTotalRemoveLinkVerifyFailTimes,
       "ruijieLeaveAPCoverageRemoveLinkVerifyFailTimes": ruijieLeaveAPCoverageRemoveLinkVerifyFailTimes,
       "ruijieInefficiencyRemoveLinkVerifyFailTime": ruijieInefficiencyRemoveLinkVerifyFailTime,
       "ruijieLinkVerifyFailRemoveLinkVerifyFailTime": ruijieLinkVerifyFailRemoveLinkVerifyFailTime,
       "ruijieOtherReasonRemoveLinkVerifyFailTime": ruijieOtherReasonRemoveLinkVerifyFailTime,
       "ruijieTotalRemoveLinkAssociationTimes": ruijieTotalRemoveLinkAssociationTimes,
       "ruijieLeaveAPCoverageRemoveAssociationFailTimes": ruijieLeaveAPCoverageRemoveAssociationFailTimes,
       "ruijieInefficiencyRemoveAssociationFailTime": ruijieInefficiencyRemoveAssociationFailTime,
       "ruijieAssociationFailRemoveAssociationFailTime": ruijieAssociationFailRemoveAssociationFailTime,
       "ruijieOtherReasonRemoveAssociationFailTime": ruijieOtherReasonRemoveAssociationFailTime,
       "ruijieUserMacAddrTable": ruijieUserMacAddrTable,
       "ruijieUserMacAddrEntry": ruijieUserMacAddrEntry,
       "ruijieTerminalIndex": ruijieTerminalIndex,
       "ruijieUserMacAdddr": ruijieUserMacAdddr,
       "ruijieTermServiceStatTable": ruijieTermServiceStatTable,
       "ruijieTermServiceStatEntry": ruijieTermServiceStatEntry,
       "ruijieTotalReTxFramNum": ruijieTotalReTxFramNum,
       "ruijieUserOnLineTime": ruijieUserOnLineTime,
       "ruijieRevDataFrameNum": ruijieRevDataFrameNum,
       "ruijieRevErrorDataFrameNum": ruijieRevErrorDataFrameNum,
       "ruijieSendDataFrameNum": ruijieSendDataFrameNum,
       "ruijieSendSuccessDataFrameNum": ruijieSendSuccessDataFrameNum,
       "ruijieSendReTxDataFrameNum": ruijieSendReTxDataFrameNum,
       "ruijieAvgSendRate": ruijieAvgSendRate,
       "ruijieAvgReceiveRate": ruijieAvgReceiveRate,
       "ruijieTotalDataThroughput": ruijieTotalDataThroughput,
       "ruijieSignalStrength": ruijieSignalStrength,
       "ruijieNoise": ruijieNoise}
)
