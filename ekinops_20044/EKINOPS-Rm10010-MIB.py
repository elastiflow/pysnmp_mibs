# SNMP MIB module (EKINOPS-Rm10010-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ekinops_20044/EKINOPS-Rm10010-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 12:01:49 2025
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

(EkiApiState,
 EkiMeasureType,
 EkiMode,
 EkiOnOff,
 EkiProtocol,
 EkiState,
 EkiSynchroMode,
 ekinops) = mibBuilder.importSymbols(
    "EKINOPS-MIB",
    "EkiApiState",
    "EkiMeasureType",
    "EkiMode",
    "EkiOnOff",
    "EkiProtocol",
    "EkiState",
    "EkiSynchroMode",
    "ekinops")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

moduleRm10010 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53)
)
if mibBuilder.loadTexts:
    moduleRm10010.setRevisions(
        ("2011-11-09 00:00",
         "2011-11-09 00:00",
         "2012-06-18 00:00",
         "2012-06-29 00:00",
         "2012-07-04 00:00",
         "2012-07-10 00:00",
         "2012-07-24 00:00",
         "2012-08-29 00:00",
         "2012-11-13 00:00",
         "2013-09-05 00:00",
         "2014-01-16 00:00",
         "2014-04-01 00:00",
         "2014-10-14 00:00",
         "2015-01-21 00:00",
         "2015-06-26 00:00",
         "2015-10-12 00:00",
         "2015-10-12 00:00",
         "2015-10-20 00:00",
         "2016-04-29 00:00",
         "2016-05-20 00:00",
         "2016-06-02 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Rm10010MultiRate(TextualConvention, Integer32):
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
        *(("rate100Mhz", 0),
          ("rate250Mhz", 1),
          ("rate500Mhz", 2),
          ("rate1Ghz", 3))
    )



class Rm10010OtxMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("otx80mode", 1),
          ("otx60mode", 2),
          ("otxadjustmode", 4))
    )



class Rm10010OtxGrid(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(50,
              100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("otxgrid50", 50),
          ("otxgrid100", 100),
          ("otxgrid200", 200))
    )



class Rm10010AdjustValue(TextualConvention, Integer32):
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("otxadjustvalue0", 0),
          ("otxadjustvalue1", 1),
          ("otxadjustvalue2", 2),
          ("otxadjustvalue3", 3),
          ("otxadjustvalue4", 4),
          ("otxadjustvalue5", 5),
          ("otxadjustvalue6", 6),
          ("otxadjustvalue7", 7),
          ("otxadjustvalue8", 8),
          ("otxadjustvalue9", 9),
          ("otxadjustvalue10", 10))
    )



class Rm10010ClientProtocol(TextualConvention, Integer32):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("protocolclientvalue0", 0),
          ("protocolclientvalue1", 1),
          ("protocolclientvalue2", 2),
          ("protocolclientvalue3", 3),
          ("protocolclientvalue4", 4),
          ("protocolclientvalue5", 5),
          ("protocolclientvalue6", 6),
          ("protocolclientvalue7", 7),
          ("protocolclientvalue8", 8))
    )



class Rm10010ProtocolMode(TextualConvention, Integer32):
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
        *(("protocolmodevalue0", 0),
          ("protocolmodevalue1", 1),
          ("protocolmodevalue2", 2),
          ("protocolmodevalue3", 3))
    )



class Rm10010OtxChannel(TextualConvention, Integer32):
    status = "current"


class Rm10010OrxChannel(TextualConvention, Integer32):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Rm10010alarms_ObjectIdentity = ObjectIdentity
rm10010alarms = _Rm10010alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2)
)
_Rm10010AlmOther_ObjectIdentity = ObjectIdentity
rm10010AlmOther = _Rm10010AlmOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1)
)
_Rm10010AlmOtherNurg_ObjectIdentity = ObjectIdentity
rm10010AlmOtherNurg = _Rm10010AlmOtherNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 1)
)
_Rm10010AlmsynthAlm2_ObjectIdentity = ObjectIdentity
rm10010AlmsynthAlm2 = _Rm10010AlmsynthAlm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 1, 2)
)
_Rm10010AlmConfTableSave_Type = EkiOnOff
_Rm10010AlmConfTableSave_Object = MibScalar
rm10010AlmConfTableSave = _Rm10010AlmConfTableSave_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 1, 2, 1),
    _Rm10010AlmConfTableSave_Type()
)
rm10010AlmConfTableSave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmConfTableSave.setStatus("current")
_Rm10010AlmInvUpload_Type = EkiOnOff
_Rm10010AlmInvUpload_Object = MibScalar
rm10010AlmInvUpload = _Rm10010AlmInvUpload_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 1, 2, 2),
    _Rm10010AlmInvUpload_Type()
)
rm10010AlmInvUpload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmInvUpload.setStatus("current")
_Rm10010AlmConfTableLoad_Type = EkiOnOff
_Rm10010AlmConfTableLoad_Object = MibScalar
rm10010AlmConfTableLoad = _Rm10010AlmConfTableLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 1, 2, 3),
    _Rm10010AlmConfTableLoad_Type()
)
rm10010AlmConfTableLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmConfTableLoad.setStatus("current")
_Rm10010AlmCorrelatOff_Type = EkiOnOff
_Rm10010AlmCorrelatOff_Object = MibScalar
rm10010AlmCorrelatOff = _Rm10010AlmCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 1, 2, 4),
    _Rm10010AlmCorrelatOff_Type()
)
rm10010AlmCorrelatOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmCorrelatOff.setStatus("current")
_Rm10010AlmMaintenanceOn_Type = EkiOnOff
_Rm10010AlmMaintenanceOn_Object = MibScalar
rm10010AlmMaintenanceOn = _Rm10010AlmMaintenanceOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 1, 2, 5),
    _Rm10010AlmMaintenanceOn_Type()
)
rm10010AlmMaintenanceOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmMaintenanceOn.setStatus("current")
_Rm10010AlmOtherUrg_ObjectIdentity = ObjectIdentity
rm10010AlmOtherUrg = _Rm10010AlmOtherUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 2)
)
_Rm10010AlmmodFanFail_ObjectIdentity = ObjectIdentity
rm10010AlmmodFanFail = _Rm10010AlmmodFanFail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 2, 248)
)
_Rm10010AlmFanModuleAbsent_Type = EkiOnOff
_Rm10010AlmFanModuleAbsent_Object = MibScalar
rm10010AlmFanModuleAbsent = _Rm10010AlmFanModuleAbsent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 2, 248, 1),
    _Rm10010AlmFanModuleAbsent_Type()
)
rm10010AlmFanModuleAbsent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmFanModuleAbsent.setStatus("current")
_Rm10010AlmFansFail_Type = EkiOnOff
_Rm10010AlmFansFail_Object = MibScalar
rm10010AlmFansFail = _Rm10010AlmFansFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 2, 248, 2),
    _Rm10010AlmFansFail_Type()
)
rm10010AlmFansFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmFansFail.setStatus("current")
_Rm10010AlmFan1Fail_Type = EkiOnOff
_Rm10010AlmFan1Fail_Object = MibScalar
rm10010AlmFan1Fail = _Rm10010AlmFan1Fail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 2, 248, 4),
    _Rm10010AlmFan1Fail_Type()
)
rm10010AlmFan1Fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmFan1Fail.setStatus("current")
_Rm10010AlmFan2Fail_Type = EkiOnOff
_Rm10010AlmFan2Fail_Object = MibScalar
rm10010AlmFan2Fail = _Rm10010AlmFan2Fail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 2, 248, 5),
    _Rm10010AlmFan2Fail_Type()
)
rm10010AlmFan2Fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmFan2Fail.setStatus("current")
_Rm10010AlmFan3Fail_Type = EkiOnOff
_Rm10010AlmFan3Fail_Object = MibScalar
rm10010AlmFan3Fail = _Rm10010AlmFan3Fail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 2, 248, 6),
    _Rm10010AlmFan3Fail_Type()
)
rm10010AlmFan3Fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmFan3Fail.setStatus("current")
_Rm10010AlmFan4Fail_Type = EkiOnOff
_Rm10010AlmFan4Fail_Object = MibScalar
rm10010AlmFan4Fail = _Rm10010AlmFan4Fail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 2, 248, 7),
    _Rm10010AlmFan4Fail_Type()
)
rm10010AlmFan4Fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmFan4Fail.setStatus("current")
_Rm10010AlmOtherCrit_ObjectIdentity = ObjectIdentity
rm10010AlmOtherCrit = _Rm10010AlmOtherCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3)
)
_Rm10010AlmsynthAlm0_ObjectIdentity = ObjectIdentity
rm10010AlmsynthAlm0 = _Rm10010AlmsynthAlm0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 0)
)
_Rm10010AlmFailFan_Type = EkiOnOff
_Rm10010AlmFailFan_Object = MibScalar
rm10010AlmFailFan = _Rm10010AlmFailFan_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 0, 2),
    _Rm10010AlmFailFan_Type()
)
rm10010AlmFailFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmFailFan.setStatus("current")
_Rm10010AlmModGlobFail_Type = EkiOnOff
_Rm10010AlmModGlobFail_Object = MibScalar
rm10010AlmModGlobFail = _Rm10010AlmModGlobFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 0, 9),
    _Rm10010AlmModGlobFail_Type()
)
rm10010AlmModGlobFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmModGlobFail.setStatus("current")
_Rm10010AlmDefFuseA_Type = EkiOnOff
_Rm10010AlmDefFuseA_Object = MibScalar
rm10010AlmDefFuseA = _Rm10010AlmDefFuseA_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 0, 15),
    _Rm10010AlmDefFuseA_Type()
)
rm10010AlmDefFuseA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmDefFuseA.setStatus("current")
_Rm10010AlmDefFuseB_Type = EkiOnOff
_Rm10010AlmDefFuseB_Object = MibScalar
rm10010AlmDefFuseB = _Rm10010AlmDefFuseB_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 0, 16),
    _Rm10010AlmDefFuseB_Type()
)
rm10010AlmDefFuseB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmDefFuseB.setStatus("current")
_Rm10010AlmclientModuleState_ObjectIdentity = ObjectIdentity
rm10010AlmclientModuleState = _Rm10010AlmclientModuleState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 40)
)
_Rm10010AlmCfpInitialize_Type = EkiOnOff
_Rm10010AlmCfpInitialize_Object = MibScalar
rm10010AlmCfpInitialize = _Rm10010AlmCfpInitialize_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 40, 1),
    _Rm10010AlmCfpInitialize_Type()
)
rm10010AlmCfpInitialize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmCfpInitialize.setStatus("current")
_Rm10010AlmCfpLowPower_Type = EkiOnOff
_Rm10010AlmCfpLowPower_Object = MibScalar
rm10010AlmCfpLowPower = _Rm10010AlmCfpLowPower_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 40, 2),
    _Rm10010AlmCfpLowPower_Type()
)
rm10010AlmCfpLowPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmCfpLowPower.setStatus("current")
_Rm10010AlmCfpHighPowerUp_Type = EkiOnOff
_Rm10010AlmCfpHighPowerUp_Object = MibScalar
rm10010AlmCfpHighPowerUp = _Rm10010AlmCfpHighPowerUp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 40, 3),
    _Rm10010AlmCfpHighPowerUp_Type()
)
rm10010AlmCfpHighPowerUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmCfpHighPowerUp.setStatus("current")
_Rm10010AlmCfpTxOff_Type = EkiOnOff
_Rm10010AlmCfpTxOff_Object = MibScalar
rm10010AlmCfpTxOff = _Rm10010AlmCfpTxOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 40, 4),
    _Rm10010AlmCfpTxOff_Type()
)
rm10010AlmCfpTxOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmCfpTxOff.setStatus("current")
_Rm10010AlmCfpTxTurnOn_Type = EkiOnOff
_Rm10010AlmCfpTxTurnOn_Object = MibScalar
rm10010AlmCfpTxTurnOn = _Rm10010AlmCfpTxTurnOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 40, 5),
    _Rm10010AlmCfpTxTurnOn_Type()
)
rm10010AlmCfpTxTurnOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmCfpTxTurnOn.setStatus("current")
_Rm10010AlmCfpReady_Type = EkiOnOff
_Rm10010AlmCfpReady_Object = MibScalar
rm10010AlmCfpReady = _Rm10010AlmCfpReady_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 40, 6),
    _Rm10010AlmCfpReady_Type()
)
rm10010AlmCfpReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmCfpReady.setStatus("current")
_Rm10010AlmCfpFault_Type = EkiOnOff
_Rm10010AlmCfpFault_Object = MibScalar
rm10010AlmCfpFault = _Rm10010AlmCfpFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 40, 7),
    _Rm10010AlmCfpFault_Type()
)
rm10010AlmCfpFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmCfpFault.setStatus("current")
_Rm10010AlmCfpTxTurnOff_Type = EkiOnOff
_Rm10010AlmCfpTxTurnOff_Object = MibScalar
rm10010AlmCfpTxTurnOff = _Rm10010AlmCfpTxTurnOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 40, 8),
    _Rm10010AlmCfpTxTurnOff_Type()
)
rm10010AlmCfpTxTurnOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmCfpTxTurnOff.setStatus("current")
_Rm10010AlmCfpHighPowerDown_Type = EkiOnOff
_Rm10010AlmCfpHighPowerDown_Object = MibScalar
rm10010AlmCfpHighPowerDown = _Rm10010AlmCfpHighPowerDown_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 40, 9),
    _Rm10010AlmCfpHighPowerDown_Type()
)
rm10010AlmCfpHighPowerDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmCfpHighPowerDown.setStatus("current")
_Rm10010AlmclientModuleGeneralStatus_ObjectIdentity = ObjectIdentity
rm10010AlmclientModuleGeneralStatus = _Rm10010AlmclientModuleGeneralStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 41)
)
_Rm10010AlmCfpOutOfAlignment_Type = EkiOnOff
_Rm10010AlmCfpOutOfAlignment_Object = MibScalar
rm10010AlmCfpOutOfAlignment = _Rm10010AlmCfpOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 41, 4),
    _Rm10010AlmCfpOutOfAlignment_Type()
)
rm10010AlmCfpOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmCfpOutOfAlignment.setStatus("current")
_Rm10010AlmCfpRxNetworkLol_Type = EkiOnOff
_Rm10010AlmCfpRxNetworkLol_Object = MibScalar
rm10010AlmCfpRxNetworkLol = _Rm10010AlmCfpRxNetworkLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 41, 5),
    _Rm10010AlmCfpRxNetworkLol_Type()
)
rm10010AlmCfpRxNetworkLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmCfpRxNetworkLol.setStatus("current")
_Rm10010AlmCfpRxLos_Type = EkiOnOff
_Rm10010AlmCfpRxLos_Object = MibScalar
rm10010AlmCfpRxLos = _Rm10010AlmCfpRxLos_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 41, 6),
    _Rm10010AlmCfpRxLos_Type()
)
rm10010AlmCfpRxLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmCfpRxLos.setStatus("current")
_Rm10010AlmCfpTxHostLol_Type = EkiOnOff
_Rm10010AlmCfpTxHostLol_Object = MibScalar
rm10010AlmCfpTxHostLol = _Rm10010AlmCfpTxHostLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 41, 7),
    _Rm10010AlmCfpTxHostLol_Type()
)
rm10010AlmCfpTxHostLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmCfpTxHostLol.setStatus("current")
_Rm10010AlmCfpTxLosf_Type = EkiOnOff
_Rm10010AlmCfpTxLosf_Object = MibScalar
rm10010AlmCfpTxLosf = _Rm10010AlmCfpTxLosf_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 41, 8),
    _Rm10010AlmCfpTxLosf_Type()
)
rm10010AlmCfpTxLosf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmCfpTxLosf.setStatus("current")
_Rm10010AlmCfpTxCmuLol_Type = EkiOnOff
_Rm10010AlmCfpTxCmuLol_Object = MibScalar
rm10010AlmCfpTxCmuLol = _Rm10010AlmCfpTxCmuLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 41, 9),
    _Rm10010AlmCfpTxCmuLol_Type()
)
rm10010AlmCfpTxCmuLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmCfpTxCmuLol.setStatus("current")
_Rm10010AlmCfpTxJitterPllLol_Type = EkiOnOff
_Rm10010AlmCfpTxJitterPllLol_Object = MibScalar
rm10010AlmCfpTxJitterPllLol = _Rm10010AlmCfpTxJitterPllLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 41, 10),
    _Rm10010AlmCfpTxJitterPllLol_Type()
)
rm10010AlmCfpTxJitterPllLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmCfpTxJitterPllLol.setStatus("current")
_Rm10010AlmCfpLossOfRefclk_Type = EkiOnOff
_Rm10010AlmCfpLossOfRefclk_Object = MibScalar
rm10010AlmCfpLossOfRefclk = _Rm10010AlmCfpLossOfRefclk_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 41, 11),
    _Rm10010AlmCfpLossOfRefclk_Type()
)
rm10010AlmCfpLossOfRefclk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmCfpLossOfRefclk.setStatus("current")
_Rm10010AlmCfpHwInterlock_Type = EkiOnOff
_Rm10010AlmCfpHwInterlock_Object = MibScalar
rm10010AlmCfpHwInterlock = _Rm10010AlmCfpHwInterlock_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 41, 14),
    _Rm10010AlmCfpHwInterlock_Type()
)
rm10010AlmCfpHwInterlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmCfpHwInterlock.setStatus("current")
_Rm10010AlmclientGlobalAlarmSummary_ObjectIdentity = ObjectIdentity
rm10010AlmclientGlobalAlarmSummary = _Rm10010AlmclientGlobalAlarmSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 42)
)
_Rm10010AlmCfpSoftGlobAlarmTest_Type = EkiOnOff
_Rm10010AlmCfpSoftGlobAlarmTest_Object = MibScalar
rm10010AlmCfpSoftGlobAlarmTest = _Rm10010AlmCfpSoftGlobAlarmTest_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 42, 1),
    _Rm10010AlmCfpSoftGlobAlarmTest_Type()
)
rm10010AlmCfpSoftGlobAlarmTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmCfpSoftGlobAlarmTest.setStatus("current")
_Rm10010AlmCfpNetworkLaneAlarmWarning2_Type = EkiOnOff
_Rm10010AlmCfpNetworkLaneAlarmWarning2_Object = MibScalar
rm10010AlmCfpNetworkLaneAlarmWarning2 = _Rm10010AlmCfpNetworkLaneAlarmWarning2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 42, 7),
    _Rm10010AlmCfpNetworkLaneAlarmWarning2_Type()
)
rm10010AlmCfpNetworkLaneAlarmWarning2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmCfpNetworkLaneAlarmWarning2.setStatus("current")
_Rm10010AlmCfpModuleState_Type = EkiOnOff
_Rm10010AlmCfpModuleState_Object = MibScalar
rm10010AlmCfpModuleState = _Rm10010AlmCfpModuleState_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 42, 8),
    _Rm10010AlmCfpModuleState_Type()
)
rm10010AlmCfpModuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmCfpModuleState.setStatus("current")
_Rm10010AlmCfpModuleGeneralStatus_Type = EkiOnOff
_Rm10010AlmCfpModuleGeneralStatus_Object = MibScalar
rm10010AlmCfpModuleGeneralStatus = _Rm10010AlmCfpModuleGeneralStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 42, 9),
    _Rm10010AlmCfpModuleGeneralStatus_Type()
)
rm10010AlmCfpModuleGeneralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmCfpModuleGeneralStatus.setStatus("current")
_Rm10010AlmCfpModuleFault_Type = EkiOnOff
_Rm10010AlmCfpModuleFault_Object = MibScalar
rm10010AlmCfpModuleFault = _Rm10010AlmCfpModuleFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 42, 10),
    _Rm10010AlmCfpModuleFault_Type()
)
rm10010AlmCfpModuleFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmCfpModuleFault.setStatus("current")
_Rm10010AlmCfpModuleAlarmWarning1_Type = EkiOnOff
_Rm10010AlmCfpModuleAlarmWarning1_Object = MibScalar
rm10010AlmCfpModuleAlarmWarning1 = _Rm10010AlmCfpModuleAlarmWarning1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 42, 11),
    _Rm10010AlmCfpModuleAlarmWarning1_Type()
)
rm10010AlmCfpModuleAlarmWarning1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmCfpModuleAlarmWarning1.setStatus("current")
_Rm10010AlmCfpModuleAlarmWarning2_Type = EkiOnOff
_Rm10010AlmCfpModuleAlarmWarning2_Object = MibScalar
rm10010AlmCfpModuleAlarmWarning2 = _Rm10010AlmCfpModuleAlarmWarning2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 42, 12),
    _Rm10010AlmCfpModuleAlarmWarning2_Type()
)
rm10010AlmCfpModuleAlarmWarning2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmCfpModuleAlarmWarning2.setStatus("current")
_Rm10010AlmCfpNetworkLaneAlarmWarning1_Type = EkiOnOff
_Rm10010AlmCfpNetworkLaneAlarmWarning1_Object = MibScalar
rm10010AlmCfpNetworkLaneAlarmWarning1 = _Rm10010AlmCfpNetworkLaneAlarmWarning1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 42, 13),
    _Rm10010AlmCfpNetworkLaneAlarmWarning1_Type()
)
rm10010AlmCfpNetworkLaneAlarmWarning1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmCfpNetworkLaneAlarmWarning1.setStatus("current")
_Rm10010AlmCfpNetworkLaneFaultStatus_Type = EkiOnOff
_Rm10010AlmCfpNetworkLaneFaultStatus_Object = MibScalar
rm10010AlmCfpNetworkLaneFaultStatus = _Rm10010AlmCfpNetworkLaneFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 42, 14),
    _Rm10010AlmCfpNetworkLaneFaultStatus_Type()
)
rm10010AlmCfpNetworkLaneFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmCfpNetworkLaneFaultStatus.setStatus("current")
_Rm10010AlmCfpHostLaneFaultStatus_Type = EkiOnOff
_Rm10010AlmCfpHostLaneFaultStatus_Object = MibScalar
rm10010AlmCfpHostLaneFaultStatus = _Rm10010AlmCfpHostLaneFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 42, 15),
    _Rm10010AlmCfpHostLaneFaultStatus_Type()
)
rm10010AlmCfpHostLaneFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmCfpHostLaneFaultStatus.setStatus("current")
_Rm10010AlmCfpGlobAlarmAssertion_Type = EkiOnOff
_Rm10010AlmCfpGlobAlarmAssertion_Object = MibScalar
rm10010AlmCfpGlobAlarmAssertion = _Rm10010AlmCfpGlobAlarmAssertion_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 42, 16),
    _Rm10010AlmCfpGlobAlarmAssertion_Type()
)
rm10010AlmCfpGlobAlarmAssertion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmCfpGlobAlarmAssertion.setStatus("current")
_Rm10010AlmmsaModuleState_ObjectIdentity = ObjectIdentity
rm10010AlmmsaModuleState = _Rm10010AlmmsaModuleState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 46)
)
_Rm10010AlmMsaInitialize_Type = EkiOnOff
_Rm10010AlmMsaInitialize_Object = MibScalar
rm10010AlmMsaInitialize = _Rm10010AlmMsaInitialize_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 46, 1),
    _Rm10010AlmMsaInitialize_Type()
)
rm10010AlmMsaInitialize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmMsaInitialize.setStatus("current")
_Rm10010AlmMsaLowPower_Type = EkiOnOff
_Rm10010AlmMsaLowPower_Object = MibScalar
rm10010AlmMsaLowPower = _Rm10010AlmMsaLowPower_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 46, 2),
    _Rm10010AlmMsaLowPower_Type()
)
rm10010AlmMsaLowPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmMsaLowPower.setStatus("current")
_Rm10010AlmMsaHighPowerUp_Type = EkiOnOff
_Rm10010AlmMsaHighPowerUp_Object = MibScalar
rm10010AlmMsaHighPowerUp = _Rm10010AlmMsaHighPowerUp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 46, 3),
    _Rm10010AlmMsaHighPowerUp_Type()
)
rm10010AlmMsaHighPowerUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmMsaHighPowerUp.setStatus("current")
_Rm10010AlmMsaTxOff_Type = EkiOnOff
_Rm10010AlmMsaTxOff_Object = MibScalar
rm10010AlmMsaTxOff = _Rm10010AlmMsaTxOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 46, 4),
    _Rm10010AlmMsaTxOff_Type()
)
rm10010AlmMsaTxOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmMsaTxOff.setStatus("current")
_Rm10010AlmMsaTxTurnOn_Type = EkiOnOff
_Rm10010AlmMsaTxTurnOn_Object = MibScalar
rm10010AlmMsaTxTurnOn = _Rm10010AlmMsaTxTurnOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 46, 5),
    _Rm10010AlmMsaTxTurnOn_Type()
)
rm10010AlmMsaTxTurnOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmMsaTxTurnOn.setStatus("current")
_Rm10010AlmMsaReady_Type = EkiOnOff
_Rm10010AlmMsaReady_Object = MibScalar
rm10010AlmMsaReady = _Rm10010AlmMsaReady_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 46, 6),
    _Rm10010AlmMsaReady_Type()
)
rm10010AlmMsaReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmMsaReady.setStatus("current")
_Rm10010AlmMsaFault_Type = EkiOnOff
_Rm10010AlmMsaFault_Object = MibScalar
rm10010AlmMsaFault = _Rm10010AlmMsaFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 46, 7),
    _Rm10010AlmMsaFault_Type()
)
rm10010AlmMsaFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmMsaFault.setStatus("current")
_Rm10010AlmMsaTxTurnOff_Type = EkiOnOff
_Rm10010AlmMsaTxTurnOff_Object = MibScalar
rm10010AlmMsaTxTurnOff = _Rm10010AlmMsaTxTurnOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 46, 8),
    _Rm10010AlmMsaTxTurnOff_Type()
)
rm10010AlmMsaTxTurnOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmMsaTxTurnOff.setStatus("current")
_Rm10010AlmMsaHighPowerDown_Type = EkiOnOff
_Rm10010AlmMsaHighPowerDown_Object = MibScalar
rm10010AlmMsaHighPowerDown = _Rm10010AlmMsaHighPowerDown_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 46, 9),
    _Rm10010AlmMsaHighPowerDown_Type()
)
rm10010AlmMsaHighPowerDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmMsaHighPowerDown.setStatus("current")
_Rm10010AlmmsaModuleGeneralStatus_ObjectIdentity = ObjectIdentity
rm10010AlmmsaModuleGeneralStatus = _Rm10010AlmmsaModuleGeneralStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 47)
)
_Rm10010AlmMsaOutOfAlignment_Type = EkiOnOff
_Rm10010AlmMsaOutOfAlignment_Object = MibScalar
rm10010AlmMsaOutOfAlignment = _Rm10010AlmMsaOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 47, 4),
    _Rm10010AlmMsaOutOfAlignment_Type()
)
rm10010AlmMsaOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmMsaOutOfAlignment.setStatus("current")
_Rm10010AlmMsaRxNetworkLol_Type = EkiOnOff
_Rm10010AlmMsaRxNetworkLol_Object = MibScalar
rm10010AlmMsaRxNetworkLol = _Rm10010AlmMsaRxNetworkLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 47, 5),
    _Rm10010AlmMsaRxNetworkLol_Type()
)
rm10010AlmMsaRxNetworkLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmMsaRxNetworkLol.setStatus("current")
_Rm10010AlmMsaRxLos_Type = EkiOnOff
_Rm10010AlmMsaRxLos_Object = MibScalar
rm10010AlmMsaRxLos = _Rm10010AlmMsaRxLos_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 47, 6),
    _Rm10010AlmMsaRxLos_Type()
)
rm10010AlmMsaRxLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmMsaRxLos.setStatus("current")
_Rm10010AlmMsaTxHostLol_Type = EkiOnOff
_Rm10010AlmMsaTxHostLol_Object = MibScalar
rm10010AlmMsaTxHostLol = _Rm10010AlmMsaTxHostLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 47, 7),
    _Rm10010AlmMsaTxHostLol_Type()
)
rm10010AlmMsaTxHostLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmMsaTxHostLol.setStatus("current")
_Rm10010AlmMsaTxLosf_Type = EkiOnOff
_Rm10010AlmMsaTxLosf_Object = MibScalar
rm10010AlmMsaTxLosf = _Rm10010AlmMsaTxLosf_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 47, 8),
    _Rm10010AlmMsaTxLosf_Type()
)
rm10010AlmMsaTxLosf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmMsaTxLosf.setStatus("current")
_Rm10010AlmMsaTxCmuLol_Type = EkiOnOff
_Rm10010AlmMsaTxCmuLol_Object = MibScalar
rm10010AlmMsaTxCmuLol = _Rm10010AlmMsaTxCmuLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 47, 9),
    _Rm10010AlmMsaTxCmuLol_Type()
)
rm10010AlmMsaTxCmuLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmMsaTxCmuLol.setStatus("current")
_Rm10010AlmMsaTxJitterPllLol_Type = EkiOnOff
_Rm10010AlmMsaTxJitterPllLol_Object = MibScalar
rm10010AlmMsaTxJitterPllLol = _Rm10010AlmMsaTxJitterPllLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 47, 10),
    _Rm10010AlmMsaTxJitterPllLol_Type()
)
rm10010AlmMsaTxJitterPllLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmMsaTxJitterPllLol.setStatus("current")
_Rm10010AlmMsaLossOfRefclk_Type = EkiOnOff
_Rm10010AlmMsaLossOfRefclk_Object = MibScalar
rm10010AlmMsaLossOfRefclk = _Rm10010AlmMsaLossOfRefclk_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 47, 11),
    _Rm10010AlmMsaLossOfRefclk_Type()
)
rm10010AlmMsaLossOfRefclk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmMsaLossOfRefclk.setStatus("current")
_Rm10010AlmMsaHwInterlock_Type = EkiOnOff
_Rm10010AlmMsaHwInterlock_Object = MibScalar
rm10010AlmMsaHwInterlock = _Rm10010AlmMsaHwInterlock_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 47, 14),
    _Rm10010AlmMsaHwInterlock_Type()
)
rm10010AlmMsaHwInterlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmMsaHwInterlock.setStatus("current")
_Rm10010AlmmsaGlobalAlarmSummary_ObjectIdentity = ObjectIdentity
rm10010AlmmsaGlobalAlarmSummary = _Rm10010AlmmsaGlobalAlarmSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 48)
)
_Rm10010AlmMsaSoftGlobAlarmTest_Type = EkiOnOff
_Rm10010AlmMsaSoftGlobAlarmTest_Object = MibScalar
rm10010AlmMsaSoftGlobAlarmTest = _Rm10010AlmMsaSoftGlobAlarmTest_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 48, 1),
    _Rm10010AlmMsaSoftGlobAlarmTest_Type()
)
rm10010AlmMsaSoftGlobAlarmTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmMsaSoftGlobAlarmTest.setStatus("current")
_Rm10010AlmMsaNetworkHostAlarmStatus_Type = EkiOnOff
_Rm10010AlmMsaNetworkHostAlarmStatus_Object = MibScalar
rm10010AlmMsaNetworkHostAlarmStatus = _Rm10010AlmMsaNetworkHostAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 48, 6),
    _Rm10010AlmMsaNetworkHostAlarmStatus_Type()
)
rm10010AlmMsaNetworkHostAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmMsaNetworkHostAlarmStatus.setStatus("current")
_Rm10010AlmMsaNetworkLaneAlarmWarning2_Type = EkiOnOff
_Rm10010AlmMsaNetworkLaneAlarmWarning2_Object = MibScalar
rm10010AlmMsaNetworkLaneAlarmWarning2 = _Rm10010AlmMsaNetworkLaneAlarmWarning2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 48, 7),
    _Rm10010AlmMsaNetworkLaneAlarmWarning2_Type()
)
rm10010AlmMsaNetworkLaneAlarmWarning2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmMsaNetworkLaneAlarmWarning2.setStatus("current")
_Rm10010AlmMsaModuleState_Type = EkiOnOff
_Rm10010AlmMsaModuleState_Object = MibScalar
rm10010AlmMsaModuleState = _Rm10010AlmMsaModuleState_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 48, 8),
    _Rm10010AlmMsaModuleState_Type()
)
rm10010AlmMsaModuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmMsaModuleState.setStatus("current")
_Rm10010AlmMsaModuleGeneralStatus_Type = EkiOnOff
_Rm10010AlmMsaModuleGeneralStatus_Object = MibScalar
rm10010AlmMsaModuleGeneralStatus = _Rm10010AlmMsaModuleGeneralStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 48, 9),
    _Rm10010AlmMsaModuleGeneralStatus_Type()
)
rm10010AlmMsaModuleGeneralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmMsaModuleGeneralStatus.setStatus("current")
_Rm10010AlmModuleFault_Type = EkiOnOff
_Rm10010AlmModuleFault_Object = MibScalar
rm10010AlmModuleFault = _Rm10010AlmModuleFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 48, 10),
    _Rm10010AlmModuleFault_Type()
)
rm10010AlmModuleFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmModuleFault.setStatus("current")
_Rm10010AlmMsaModuleAlarmWarning1_Type = EkiOnOff
_Rm10010AlmMsaModuleAlarmWarning1_Object = MibScalar
rm10010AlmMsaModuleAlarmWarning1 = _Rm10010AlmMsaModuleAlarmWarning1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 48, 11),
    _Rm10010AlmMsaModuleAlarmWarning1_Type()
)
rm10010AlmMsaModuleAlarmWarning1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmMsaModuleAlarmWarning1.setStatus("current")
_Rm10010AlmMsaModuleAlarmWarning2_Type = EkiOnOff
_Rm10010AlmMsaModuleAlarmWarning2_Object = MibScalar
rm10010AlmMsaModuleAlarmWarning2 = _Rm10010AlmMsaModuleAlarmWarning2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 48, 12),
    _Rm10010AlmMsaModuleAlarmWarning2_Type()
)
rm10010AlmMsaModuleAlarmWarning2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmMsaModuleAlarmWarning2.setStatus("current")
_Rm10010AlmMsaNetworkLaneAlarmWarning1_Type = EkiOnOff
_Rm10010AlmMsaNetworkLaneAlarmWarning1_Object = MibScalar
rm10010AlmMsaNetworkLaneAlarmWarning1 = _Rm10010AlmMsaNetworkLaneAlarmWarning1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 48, 13),
    _Rm10010AlmMsaNetworkLaneAlarmWarning1_Type()
)
rm10010AlmMsaNetworkLaneAlarmWarning1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmMsaNetworkLaneAlarmWarning1.setStatus("current")
_Rm10010AlmMsaNetworkLaneFaultStatus_Type = EkiOnOff
_Rm10010AlmMsaNetworkLaneFaultStatus_Object = MibScalar
rm10010AlmMsaNetworkLaneFaultStatus = _Rm10010AlmMsaNetworkLaneFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 48, 14),
    _Rm10010AlmMsaNetworkLaneFaultStatus_Type()
)
rm10010AlmMsaNetworkLaneFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmMsaNetworkLaneFaultStatus.setStatus("current")
_Rm10010AlmMsaHostLaneFaultStatus_Type = EkiOnOff
_Rm10010AlmMsaHostLaneFaultStatus_Object = MibScalar
rm10010AlmMsaHostLaneFaultStatus = _Rm10010AlmMsaHostLaneFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 48, 15),
    _Rm10010AlmMsaHostLaneFaultStatus_Type()
)
rm10010AlmMsaHostLaneFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmMsaHostLaneFaultStatus.setStatus("current")
_Rm10010AlmMsaGlobAlarmAssertion_Type = EkiOnOff
_Rm10010AlmMsaGlobAlarmAssertion_Object = MibScalar
rm10010AlmMsaGlobAlarmAssertion = _Rm10010AlmMsaGlobAlarmAssertion_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 48, 16),
    _Rm10010AlmMsaGlobAlarmAssertion_Type()
)
rm10010AlmMsaGlobAlarmAssertion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmMsaGlobAlarmAssertion.setStatus("current")
_Rm10010AlmmsaNetworkTxAlignment_ObjectIdentity = ObjectIdentity
rm10010AlmmsaNetworkTxAlignment = _Rm10010AlmmsaNetworkTxAlignment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 49)
)
_Rm10010AlmNetTxTimingFault_Type = EkiOnOff
_Rm10010AlmNetTxTimingFault_Object = MibScalar
rm10010AlmNetTxTimingFault = _Rm10010AlmNetTxTimingFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 49, 12),
    _Rm10010AlmNetTxTimingFault_Type()
)
rm10010AlmNetTxTimingFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmNetTxTimingFault.setStatus("current")
_Rm10010AlmNetTxReferenceClockFault_Type = EkiOnOff
_Rm10010AlmNetTxReferenceClockFault_Object = MibScalar
rm10010AlmNetTxReferenceClockFault = _Rm10010AlmNetTxReferenceClockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 49, 13),
    _Rm10010AlmNetTxReferenceClockFault_Type()
)
rm10010AlmNetTxReferenceClockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmNetTxReferenceClockFault.setStatus("current")
_Rm10010AlmNetTxCmuLockFault_Type = EkiOnOff
_Rm10010AlmNetTxCmuLockFault_Object = MibScalar
rm10010AlmNetTxCmuLockFault = _Rm10010AlmNetTxCmuLockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 49, 14),
    _Rm10010AlmNetTxCmuLockFault_Type()
)
rm10010AlmNetTxCmuLockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmNetTxCmuLockFault.setStatus("current")
_Rm10010AlmNetTxOutOfAlignment_Type = EkiOnOff
_Rm10010AlmNetTxOutOfAlignment_Object = MibScalar
rm10010AlmNetTxOutOfAlignment = _Rm10010AlmNetTxOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 49, 15),
    _Rm10010AlmNetTxOutOfAlignment_Type()
)
rm10010AlmNetTxOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmNetTxOutOfAlignment.setStatus("current")
_Rm10010AlmNetTxLossOfAlignment_Type = EkiOnOff
_Rm10010AlmNetTxLossOfAlignment_Object = MibScalar
rm10010AlmNetTxLossOfAlignment = _Rm10010AlmNetTxLossOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 49, 16),
    _Rm10010AlmNetTxLossOfAlignment_Type()
)
rm10010AlmNetTxLossOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmNetTxLossOfAlignment.setStatus("current")
_Rm10010AlmmsaNetworkRxAlignment_ObjectIdentity = ObjectIdentity
rm10010AlmmsaNetworkRxAlignment = _Rm10010AlmmsaNetworkRxAlignment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 50)
)
_Rm10010AlmNetRxTimingFault_Type = EkiOnOff
_Rm10010AlmNetRxTimingFault_Object = MibScalar
rm10010AlmNetRxTimingFault = _Rm10010AlmNetRxTimingFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 50, 12),
    _Rm10010AlmNetRxTimingFault_Type()
)
rm10010AlmNetRxTimingFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmNetRxTimingFault.setStatus("current")
_Rm10010AlmNetRxOutOfAlignment_Type = EkiOnOff
_Rm10010AlmNetRxOutOfAlignment_Object = MibScalar
rm10010AlmNetRxOutOfAlignment = _Rm10010AlmNetRxOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 50, 13),
    _Rm10010AlmNetRxOutOfAlignment_Type()
)
rm10010AlmNetRxOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmNetRxOutOfAlignment.setStatus("current")
_Rm10010AlmNetRxLossOfAlignment_Type = EkiOnOff
_Rm10010AlmNetRxLossOfAlignment_Object = MibScalar
rm10010AlmNetRxLossOfAlignment = _Rm10010AlmNetRxLossOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 50, 14),
    _Rm10010AlmNetRxLossOfAlignment_Type()
)
rm10010AlmNetRxLossOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmNetRxLossOfAlignment.setStatus("current")
_Rm10010AlmNetRxModemLockFault_Type = EkiOnOff
_Rm10010AlmNetRxModemLockFault_Object = MibScalar
rm10010AlmNetRxModemLockFault = _Rm10010AlmNetRxModemLockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 50, 15),
    _Rm10010AlmNetRxModemLockFault_Type()
)
rm10010AlmNetRxModemLockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmNetRxModemLockFault.setStatus("current")
_Rm10010AlmNetRxModemSyncDetectFault_Type = EkiOnOff
_Rm10010AlmNetRxModemSyncDetectFault_Object = MibScalar
rm10010AlmNetRxModemSyncDetectFault = _Rm10010AlmNetRxModemSyncDetectFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 50, 16),
    _Rm10010AlmNetRxModemSyncDetectFault_Type()
)
rm10010AlmNetRxModemSyncDetectFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmNetRxModemSyncDetectFault.setStatus("current")
_Rm10010AlmmsaNetworkHostNetworkAlarmSummary_ObjectIdentity = ObjectIdentity
rm10010AlmmsaNetworkHostNetworkAlarmSummary = _Rm10010AlmmsaNetworkHostNetworkAlarmSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 51)
)
_Rm10010AlmNetworkTxAlignment_Type = EkiOnOff
_Rm10010AlmNetworkTxAlignment_Object = MibScalar
rm10010AlmNetworkTxAlignment = _Rm10010AlmNetworkTxAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 51, 11),
    _Rm10010AlmNetworkTxAlignment_Type()
)
rm10010AlmNetworkTxAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmNetworkTxAlignment.setStatus("current")
_Rm10010AlmNetworkRxAlignment_Type = EkiOnOff
_Rm10010AlmNetworkRxAlignment_Object = MibScalar
rm10010AlmNetworkRxAlignment = _Rm10010AlmNetworkRxAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 51, 12),
    _Rm10010AlmNetworkRxAlignment_Type()
)
rm10010AlmNetworkRxAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmNetworkRxAlignment.setStatus("current")
_Rm10010AlmNetworkRxOtn_Type = EkiOnOff
_Rm10010AlmNetworkRxOtn_Object = MibScalar
rm10010AlmNetworkRxOtn = _Rm10010AlmNetworkRxOtn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 51, 13),
    _Rm10010AlmNetworkRxOtn_Type()
)
rm10010AlmNetworkRxOtn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmNetworkRxOtn.setStatus("current")
_Rm10010AlmHostRxAlignment_Type = EkiOnOff
_Rm10010AlmHostRxAlignment_Object = MibScalar
rm10010AlmHostRxAlignment = _Rm10010AlmHostRxAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 51, 14),
    _Rm10010AlmHostRxAlignment_Type()
)
rm10010AlmHostRxAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmHostRxAlignment.setStatus("current")
_Rm10010AlmHostTxAlignment_Type = EkiOnOff
_Rm10010AlmHostTxAlignment_Object = MibScalar
rm10010AlmHostTxAlignment = _Rm10010AlmHostTxAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 51, 15),
    _Rm10010AlmHostTxAlignment_Type()
)
rm10010AlmHostTxAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmHostTxAlignment.setStatus("current")
_Rm10010AlmHostTxOtnStatus_Type = EkiOnOff
_Rm10010AlmHostTxOtnStatus_Object = MibScalar
rm10010AlmHostTxOtnStatus = _Rm10010AlmHostTxOtnStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 51, 16),
    _Rm10010AlmHostTxOtnStatus_Type()
)
rm10010AlmHostTxOtnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmHostTxOtnStatus.setStatus("current")
_Rm10010AlmmsaHostTxAlignment_ObjectIdentity = ObjectIdentity
rm10010AlmmsaHostTxAlignment = _Rm10010AlmmsaHostTxAlignment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 52)
)
_Rm10010AlmHostTxDeskewLockFault_Type = EkiOnOff
_Rm10010AlmHostTxDeskewLockFault_Object = MibScalar
rm10010AlmHostTxDeskewLockFault = _Rm10010AlmHostTxDeskewLockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 52, 13),
    _Rm10010AlmHostTxDeskewLockFault_Type()
)
rm10010AlmHostTxDeskewLockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmHostTxDeskewLockFault.setStatus("current")
_Rm10010AlmHostTxOutOfAlignment_Type = EkiOnOff
_Rm10010AlmHostTxOutOfAlignment_Object = MibScalar
rm10010AlmHostTxOutOfAlignment = _Rm10010AlmHostTxOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 52, 14),
    _Rm10010AlmHostTxOutOfAlignment_Type()
)
rm10010AlmHostTxOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmHostTxOutOfAlignment.setStatus("current")
_Rm10010AlmHostTxLossOfAlignment_Type = EkiOnOff
_Rm10010AlmHostTxLossOfAlignment_Object = MibScalar
rm10010AlmHostTxLossOfAlignment = _Rm10010AlmHostTxLossOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 52, 15),
    _Rm10010AlmHostTxLossOfAlignment_Type()
)
rm10010AlmHostTxLossOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmHostTxLossOfAlignment.setStatus("current")
_Rm10010AlmHostTxCdrLockFault_Type = EkiOnOff
_Rm10010AlmHostTxCdrLockFault_Object = MibScalar
rm10010AlmHostTxCdrLockFault = _Rm10010AlmHostTxCdrLockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 52, 16),
    _Rm10010AlmHostTxCdrLockFault_Type()
)
rm10010AlmHostTxCdrLockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmHostTxCdrLockFault.setStatus("current")
_Rm10010AlmmsaHostRxAlignment_ObjectIdentity = ObjectIdentity
rm10010AlmmsaHostRxAlignment = _Rm10010AlmmsaHostRxAlignment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 53)
)
_Rm10010AlmHostRxCmuLockFault_Type = EkiOnOff
_Rm10010AlmHostRxCmuLockFault_Object = MibScalar
rm10010AlmHostRxCmuLockFault = _Rm10010AlmHostRxCmuLockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 53, 14),
    _Rm10010AlmHostRxCmuLockFault_Type()
)
rm10010AlmHostRxCmuLockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmHostRxCmuLockFault.setStatus("current")
_Rm10010AlmHostRxOutOfAlignment_Type = EkiOnOff
_Rm10010AlmHostRxOutOfAlignment_Object = MibScalar
rm10010AlmHostRxOutOfAlignment = _Rm10010AlmHostRxOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 53, 15),
    _Rm10010AlmHostRxOutOfAlignment_Type()
)
rm10010AlmHostRxOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmHostRxOutOfAlignment.setStatus("current")
_Rm10010AlmHostRxLossOfAlignment_Type = EkiOnOff
_Rm10010AlmHostRxLossOfAlignment_Object = MibScalar
rm10010AlmHostRxLossOfAlignment = _Rm10010AlmHostRxLossOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 1, 3, 53, 16),
    _Rm10010AlmHostRxLossOfAlignment_Type()
)
rm10010AlmHostRxLossOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmHostRxLossOfAlignment.setStatus("current")
_Rm10010AlmClient_ObjectIdentity = ObjectIdentity
rm10010AlmClient = _Rm10010AlmClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2)
)
_Rm10010AlmClientNurg_ObjectIdentity = ObjectIdentity
rm10010AlmClientNurg = _Rm10010AlmClientNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 1)
)
_Rm10010AlmclientNetworkLaneAlarmWarningTable_Object = MibTable
rm10010AlmclientNetworkLaneAlarmWarningTable = _Rm10010AlmclientNetworkLaneAlarmWarningTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 1, 56)
)
if mibBuilder.loadTexts:
    rm10010AlmclientNetworkLaneAlarmWarningTable.setStatus("current")
_Rm10010AlmclientNetworkLaneAlarmWarningEntry_Object = MibTableRow
rm10010AlmclientNetworkLaneAlarmWarningEntry = _Rm10010AlmclientNetworkLaneAlarmWarningEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 1, 56, 1)
)
rm10010AlmclientNetworkLaneAlarmWarningEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010AlmclientNetworkLaneAlarmWarningIndex"),
)
if mibBuilder.loadTexts:
    rm10010AlmclientNetworkLaneAlarmWarningEntry.setStatus("current")


class _Rm10010AlmclientNetworkLaneAlarmWarningIndex_Type(Integer32):
    """Custom type rm10010AlmclientNetworkLaneAlarmWarningIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010AlmclientNetworkLaneAlarmWarningIndex_Type.__name__ = "Integer32"
_Rm10010AlmclientNetworkLaneAlarmWarningIndex_Object = MibTableColumn
rm10010AlmclientNetworkLaneAlarmWarningIndex = _Rm10010AlmclientNetworkLaneAlarmWarningIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 1, 56, 1, 1),
    _Rm10010AlmclientNetworkLaneAlarmWarningIndex_Type()
)
rm10010AlmclientNetworkLaneAlarmWarningIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmclientNetworkLaneAlarmWarningIndex.setStatus("current")
_Rm10010AlmClientRxPowerLowAlarmPortn_Type = EkiOnOff
_Rm10010AlmClientRxPowerLowAlarmPortn_Object = MibTableColumn
rm10010AlmClientRxPowerLowAlarmPortn = _Rm10010AlmClientRxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 1, 56, 1, 2),
    _Rm10010AlmClientRxPowerLowAlarmPortn_Type()
)
rm10010AlmClientRxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmClientRxPowerLowAlarmPortn.setStatus("current")
_Rm10010AlmClientRxPowerLowWarningPortn_Type = EkiOnOff
_Rm10010AlmClientRxPowerLowWarningPortn_Object = MibTableColumn
rm10010AlmClientRxPowerLowWarningPortn = _Rm10010AlmClientRxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 1, 56, 1, 3),
    _Rm10010AlmClientRxPowerLowWarningPortn_Type()
)
rm10010AlmClientRxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmClientRxPowerLowWarningPortn.setStatus("current")
_Rm10010AlmClientRxPowerHighWarningPortn_Type = EkiOnOff
_Rm10010AlmClientRxPowerHighWarningPortn_Object = MibTableColumn
rm10010AlmClientRxPowerHighWarningPortn = _Rm10010AlmClientRxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 1, 56, 1, 4),
    _Rm10010AlmClientRxPowerHighWarningPortn_Type()
)
rm10010AlmClientRxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmClientRxPowerHighWarningPortn.setStatus("current")
_Rm10010AlmClientRxPowerHighAlarmPortn_Type = EkiOnOff
_Rm10010AlmClientRxPowerHighAlarmPortn_Object = MibTableColumn
rm10010AlmClientRxPowerHighAlarmPortn = _Rm10010AlmClientRxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 1, 56, 1, 5),
    _Rm10010AlmClientRxPowerHighAlarmPortn_Type()
)
rm10010AlmClientRxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmClientRxPowerHighAlarmPortn.setStatus("current")
_Rm10010AlmLaserTempLowAlarmPortn_Type = EkiOnOff
_Rm10010AlmLaserTempLowAlarmPortn_Object = MibTableColumn
rm10010AlmLaserTempLowAlarmPortn = _Rm10010AlmLaserTempLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 1, 56, 1, 6),
    _Rm10010AlmLaserTempLowAlarmPortn_Type()
)
rm10010AlmLaserTempLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmLaserTempLowAlarmPortn.setStatus("current")
_Rm10010AlmClientLaserTempLowWarningPortn_Type = EkiOnOff
_Rm10010AlmClientLaserTempLowWarningPortn_Object = MibTableColumn
rm10010AlmClientLaserTempLowWarningPortn = _Rm10010AlmClientLaserTempLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 1, 56, 1, 7),
    _Rm10010AlmClientLaserTempLowWarningPortn_Type()
)
rm10010AlmClientLaserTempLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmClientLaserTempLowWarningPortn.setStatus("current")
_Rm10010AlmClientLaserTempHighWarningPortn_Type = EkiOnOff
_Rm10010AlmClientLaserTempHighWarningPortn_Object = MibTableColumn
rm10010AlmClientLaserTempHighWarningPortn = _Rm10010AlmClientLaserTempHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 1, 56, 1, 8),
    _Rm10010AlmClientLaserTempHighWarningPortn_Type()
)
rm10010AlmClientLaserTempHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmClientLaserTempHighWarningPortn.setStatus("current")
_Rm10010AlmClientLaserTempHighAlarmPortn_Type = EkiOnOff
_Rm10010AlmClientLaserTempHighAlarmPortn_Object = MibTableColumn
rm10010AlmClientLaserTempHighAlarmPortn = _Rm10010AlmClientLaserTempHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 1, 56, 1, 9),
    _Rm10010AlmClientLaserTempHighAlarmPortn_Type()
)
rm10010AlmClientLaserTempHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmClientLaserTempHighAlarmPortn.setStatus("current")
_Rm10010AlmClientTxPowerLowAlarmPortn_Type = EkiOnOff
_Rm10010AlmClientTxPowerLowAlarmPortn_Object = MibTableColumn
rm10010AlmClientTxPowerLowAlarmPortn = _Rm10010AlmClientTxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 1, 56, 1, 10),
    _Rm10010AlmClientTxPowerLowAlarmPortn_Type()
)
rm10010AlmClientTxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmClientTxPowerLowAlarmPortn.setStatus("current")
_Rm10010AlmClientTxPowerLowWarningPortn_Type = EkiOnOff
_Rm10010AlmClientTxPowerLowWarningPortn_Object = MibTableColumn
rm10010AlmClientTxPowerLowWarningPortn = _Rm10010AlmClientTxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 1, 56, 1, 11),
    _Rm10010AlmClientTxPowerLowWarningPortn_Type()
)
rm10010AlmClientTxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmClientTxPowerLowWarningPortn.setStatus("current")
_Rm10010AlmClientTxPowerHighWarningPortn_Type = EkiOnOff
_Rm10010AlmClientTxPowerHighWarningPortn_Object = MibTableColumn
rm10010AlmClientTxPowerHighWarningPortn = _Rm10010AlmClientTxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 1, 56, 1, 12),
    _Rm10010AlmClientTxPowerHighWarningPortn_Type()
)
rm10010AlmClientTxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmClientTxPowerHighWarningPortn.setStatus("current")
_Rm10010AlmClientTxPowerHighAlarmPortn_Type = EkiOnOff
_Rm10010AlmClientTxPowerHighAlarmPortn_Object = MibTableColumn
rm10010AlmClientTxPowerHighAlarmPortn = _Rm10010AlmClientTxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 1, 56, 1, 13),
    _Rm10010AlmClientTxPowerHighAlarmPortn_Type()
)
rm10010AlmClientTxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmClientTxPowerHighAlarmPortn.setStatus("current")
_Rm10010AlmClientBiasLowAlarmPortn_Type = EkiOnOff
_Rm10010AlmClientBiasLowAlarmPortn_Object = MibTableColumn
rm10010AlmClientBiasLowAlarmPortn = _Rm10010AlmClientBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 1, 56, 1, 14),
    _Rm10010AlmClientBiasLowAlarmPortn_Type()
)
rm10010AlmClientBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmClientBiasLowAlarmPortn.setStatus("current")
_Rm10010AlmClientBiasLowWarningPortn_Type = EkiOnOff
_Rm10010AlmClientBiasLowWarningPortn_Object = MibTableColumn
rm10010AlmClientBiasLowWarningPortn = _Rm10010AlmClientBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 1, 56, 1, 15),
    _Rm10010AlmClientBiasLowWarningPortn_Type()
)
rm10010AlmClientBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmClientBiasLowWarningPortn.setStatus("current")
_Rm10010AlmClientBiasHighWarningPortn_Type = EkiOnOff
_Rm10010AlmClientBiasHighWarningPortn_Object = MibTableColumn
rm10010AlmClientBiasHighWarningPortn = _Rm10010AlmClientBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 1, 56, 1, 16),
    _Rm10010AlmClientBiasHighWarningPortn_Type()
)
rm10010AlmClientBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmClientBiasHighWarningPortn.setStatus("current")
_Rm10010AlmClientBiasHighAlarmPortn_Type = EkiOnOff
_Rm10010AlmClientBiasHighAlarmPortn_Object = MibTableColumn
rm10010AlmClientBiasHighAlarmPortn = _Rm10010AlmClientBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 1, 56, 1, 17),
    _Rm10010AlmClientBiasHighAlarmPortn_Type()
)
rm10010AlmClientBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmClientBiasHighAlarmPortn.setStatus("current")
_Rm10010AlmclientSfpWarnDdmTable_Object = MibTable
rm10010AlmclientSfpWarnDdmTable = _Rm10010AlmclientSfpWarnDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 1, 232)
)
if mibBuilder.loadTexts:
    rm10010AlmclientSfpWarnDdmTable.setStatus("current")
_Rm10010AlmclientSfpWarnDdmEntry_Object = MibTableRow
rm10010AlmclientSfpWarnDdmEntry = _Rm10010AlmclientSfpWarnDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 1, 232, 1)
)
rm10010AlmclientSfpWarnDdmEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010AlmclientSfpWarnDdmIndex"),
)
if mibBuilder.loadTexts:
    rm10010AlmclientSfpWarnDdmEntry.setStatus("current")


class _Rm10010AlmclientSfpWarnDdmIndex_Type(Integer32):
    """Custom type rm10010AlmclientSfpWarnDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010AlmclientSfpWarnDdmIndex_Type.__name__ = "Integer32"
_Rm10010AlmclientSfpWarnDdmIndex_Object = MibTableColumn
rm10010AlmclientSfpWarnDdmIndex = _Rm10010AlmclientSfpWarnDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 1, 232, 1, 1),
    _Rm10010AlmclientSfpWarnDdmIndex_Type()
)
rm10010AlmclientSfpWarnDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmclientSfpWarnDdmIndex.setStatus("current")
_Rm10010AlmTxPwLowWngPortn_Type = EkiOnOff
_Rm10010AlmTxPwLowWngPortn_Object = MibTableColumn
rm10010AlmTxPwLowWngPortn = _Rm10010AlmTxPwLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 1, 232, 1, 2),
    _Rm10010AlmTxPwLowWngPortn_Type()
)
rm10010AlmTxPwLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmTxPwLowWngPortn.setStatus("current")
_Rm10010AlmTxPwrHighWngPortn_Type = EkiOnOff
_Rm10010AlmTxPwrHighWngPortn_Object = MibTableColumn
rm10010AlmTxPwrHighWngPortn = _Rm10010AlmTxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 1, 232, 1, 3),
    _Rm10010AlmTxPwrHighWngPortn_Type()
)
rm10010AlmTxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmTxPwrHighWngPortn.setStatus("current")
_Rm10010AlmTxBiasLowWngPortn_Type = EkiOnOff
_Rm10010AlmTxBiasLowWngPortn_Object = MibTableColumn
rm10010AlmTxBiasLowWngPortn = _Rm10010AlmTxBiasLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 1, 232, 1, 4),
    _Rm10010AlmTxBiasLowWngPortn_Type()
)
rm10010AlmTxBiasLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmTxBiasLowWngPortn.setStatus("current")
_Rm10010AlmTxBiasHighWngPortn_Type = EkiOnOff
_Rm10010AlmTxBiasHighWngPortn_Object = MibTableColumn
rm10010AlmTxBiasHighWngPortn = _Rm10010AlmTxBiasHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 1, 232, 1, 5),
    _Rm10010AlmTxBiasHighWngPortn_Type()
)
rm10010AlmTxBiasHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmTxBiasHighWngPortn.setStatus("current")
_Rm10010AlmVccLowWngPortn_Type = EkiOnOff
_Rm10010AlmVccLowWngPortn_Object = MibTableColumn
rm10010AlmVccLowWngPortn = _Rm10010AlmVccLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 1, 232, 1, 6),
    _Rm10010AlmVccLowWngPortn_Type()
)
rm10010AlmVccLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmVccLowWngPortn.setStatus("current")
_Rm10010AlmVccHighWngPortn_Type = EkiOnOff
_Rm10010AlmVccHighWngPortn_Object = MibTableColumn
rm10010AlmVccHighWngPortn = _Rm10010AlmVccHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 1, 232, 1, 7),
    _Rm10010AlmVccHighWngPortn_Type()
)
rm10010AlmVccHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmVccHighWngPortn.setStatus("current")
_Rm10010AlmTempLowWngPortn_Type = EkiOnOff
_Rm10010AlmTempLowWngPortn_Object = MibTableColumn
rm10010AlmTempLowWngPortn = _Rm10010AlmTempLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 1, 232, 1, 8),
    _Rm10010AlmTempLowWngPortn_Type()
)
rm10010AlmTempLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmTempLowWngPortn.setStatus("current")
_Rm10010AlmTempHighWngPortn_Type = EkiOnOff
_Rm10010AlmTempHighWngPortn_Object = MibTableColumn
rm10010AlmTempHighWngPortn = _Rm10010AlmTempHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 1, 232, 1, 9),
    _Rm10010AlmTempHighWngPortn_Type()
)
rm10010AlmTempHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmTempHighWngPortn.setStatus("current")
_Rm10010AlmRxPwrLowWngPortn_Type = EkiOnOff
_Rm10010AlmRxPwrLowWngPortn_Object = MibTableColumn
rm10010AlmRxPwrLowWngPortn = _Rm10010AlmRxPwrLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 1, 232, 1, 16),
    _Rm10010AlmRxPwrLowWngPortn_Type()
)
rm10010AlmRxPwrLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmRxPwrLowWngPortn.setStatus("current")
_Rm10010AlmRxPwrHighWngPortn_Type = EkiOnOff
_Rm10010AlmRxPwrHighWngPortn_Object = MibTableColumn
rm10010AlmRxPwrHighWngPortn = _Rm10010AlmRxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 1, 232, 1, 17),
    _Rm10010AlmRxPwrHighWngPortn_Type()
)
rm10010AlmRxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmRxPwrHighWngPortn.setStatus("current")
_Rm10010AlmClientUrg_ObjectIdentity = ObjectIdentity
rm10010AlmClientUrg = _Rm10010AlmClientUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 2)
)
_Rm10010AlmclientNetworkLaneFaultTable_Object = MibTable
rm10010AlmclientNetworkLaneFaultTable = _Rm10010AlmclientNetworkLaneFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 2, 72)
)
if mibBuilder.loadTexts:
    rm10010AlmclientNetworkLaneFaultTable.setStatus("current")
_Rm10010AlmclientNetworkLaneFaultEntry_Object = MibTableRow
rm10010AlmclientNetworkLaneFaultEntry = _Rm10010AlmclientNetworkLaneFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 2, 72, 1)
)
rm10010AlmclientNetworkLaneFaultEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010AlmclientNetworkLaneFaultIndex"),
)
if mibBuilder.loadTexts:
    rm10010AlmclientNetworkLaneFaultEntry.setStatus("current")


class _Rm10010AlmclientNetworkLaneFaultIndex_Type(Integer32):
    """Custom type rm10010AlmclientNetworkLaneFaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010AlmclientNetworkLaneFaultIndex_Type.__name__ = "Integer32"
_Rm10010AlmclientNetworkLaneFaultIndex_Object = MibTableColumn
rm10010AlmclientNetworkLaneFaultIndex = _Rm10010AlmclientNetworkLaneFaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 2, 72, 1, 1),
    _Rm10010AlmclientNetworkLaneFaultIndex_Type()
)
rm10010AlmclientNetworkLaneFaultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmclientNetworkLaneFaultIndex.setStatus("current")
_Rm10010AlmClientLaneRxFifoErrorPortn_Type = EkiOnOff
_Rm10010AlmClientLaneRxFifoErrorPortn_Object = MibTableColumn
rm10010AlmClientLaneRxFifoErrorPortn = _Rm10010AlmClientLaneRxFifoErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 2, 72, 1, 4),
    _Rm10010AlmClientLaneRxFifoErrorPortn_Type()
)
rm10010AlmClientLaneRxFifoErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmClientLaneRxFifoErrorPortn.setStatus("current")
_Rm10010AlmClientLaneRxLolPortn_Type = EkiOnOff
_Rm10010AlmClientLaneRxLolPortn_Object = MibTableColumn
rm10010AlmClientLaneRxLolPortn = _Rm10010AlmClientLaneRxLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 2, 72, 1, 5),
    _Rm10010AlmClientLaneRxLolPortn_Type()
)
rm10010AlmClientLaneRxLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmClientLaneRxLolPortn.setStatus("current")
_Rm10010AlmClientLaneRxLosPortn_Type = EkiOnOff
_Rm10010AlmClientLaneRxLosPortn_Object = MibTableColumn
rm10010AlmClientLaneRxLosPortn = _Rm10010AlmClientLaneRxLosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 2, 72, 1, 6),
    _Rm10010AlmClientLaneRxLosPortn_Type()
)
rm10010AlmClientLaneRxLosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmClientLaneRxLosPortn.setStatus("current")
_Rm10010AlmClientLaneTxLolPortn_Type = EkiOnOff
_Rm10010AlmClientLaneTxLolPortn_Object = MibTableColumn
rm10010AlmClientLaneTxLolPortn = _Rm10010AlmClientLaneTxLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 2, 72, 1, 8),
    _Rm10010AlmClientLaneTxLolPortn_Type()
)
rm10010AlmClientLaneTxLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmClientLaneTxLolPortn.setStatus("current")
_Rm10010AlmClientLaneTxLosfPortn_Type = EkiOnOff
_Rm10010AlmClientLaneTxLosfPortn_Object = MibTableColumn
rm10010AlmClientLaneTxLosfPortn = _Rm10010AlmClientLaneTxLosfPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 2, 72, 1, 9),
    _Rm10010AlmClientLaneTxLosfPortn_Type()
)
rm10010AlmClientLaneTxLosfPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmClientLaneTxLosfPortn.setStatus("current")
_Rm10010AlmClientLaneApdPowerSupplyPortn_Type = EkiOnOff
_Rm10010AlmClientLaneApdPowerSupplyPortn_Object = MibTableColumn
rm10010AlmClientLaneApdPowerSupplyPortn = _Rm10010AlmClientLaneApdPowerSupplyPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 2, 72, 1, 15),
    _Rm10010AlmClientLaneApdPowerSupplyPortn_Type()
)
rm10010AlmClientLaneApdPowerSupplyPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmClientLaneApdPowerSupplyPortn.setStatus("current")
_Rm10010AlmClientLaneWavelengthUnlockedPortn_Type = EkiOnOff
_Rm10010AlmClientLaneWavelengthUnlockedPortn_Object = MibTableColumn
rm10010AlmClientLaneWavelengthUnlockedPortn = _Rm10010AlmClientLaneWavelengthUnlockedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 2, 72, 1, 16),
    _Rm10010AlmClientLaneWavelengthUnlockedPortn_Type()
)
rm10010AlmClientLaneWavelengthUnlockedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmClientLaneWavelengthUnlockedPortn.setStatus("current")
_Rm10010AlmClientLaneTecFaultPortn_Type = EkiOnOff
_Rm10010AlmClientLaneTecFaultPortn_Object = MibTableColumn
rm10010AlmClientLaneTecFaultPortn = _Rm10010AlmClientLaneTecFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 2, 72, 1, 17),
    _Rm10010AlmClientLaneTecFaultPortn_Type()
)
rm10010AlmClientLaneTecFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmClientLaneTecFaultPortn.setStatus("current")
_Rm10010AlmclientHostLaneFaultTable_Object = MibTable
rm10010AlmclientHostLaneFaultTable = _Rm10010AlmclientHostLaneFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 2, 88)
)
if mibBuilder.loadTexts:
    rm10010AlmclientHostLaneFaultTable.setStatus("current")
_Rm10010AlmclientHostLaneFaultEntry_Object = MibTableRow
rm10010AlmclientHostLaneFaultEntry = _Rm10010AlmclientHostLaneFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 2, 88, 1)
)
rm10010AlmclientHostLaneFaultEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010AlmclientHostLaneFaultIndex"),
)
if mibBuilder.loadTexts:
    rm10010AlmclientHostLaneFaultEntry.setStatus("current")


class _Rm10010AlmclientHostLaneFaultIndex_Type(Integer32):
    """Custom type rm10010AlmclientHostLaneFaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010AlmclientHostLaneFaultIndex_Type.__name__ = "Integer32"
_Rm10010AlmclientHostLaneFaultIndex_Object = MibTableColumn
rm10010AlmclientHostLaneFaultIndex = _Rm10010AlmclientHostLaneFaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 2, 88, 1, 1),
    _Rm10010AlmclientHostLaneFaultIndex_Type()
)
rm10010AlmclientHostLaneFaultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmclientHostLaneFaultIndex.setStatus("current")
_Rm10010AlmClientLossOfSyncPortn_Type = EkiOnOff
_Rm10010AlmClientLossOfSyncPortn_Object = MibTableColumn
rm10010AlmClientLossOfSyncPortn = _Rm10010AlmClientLossOfSyncPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 2, 88, 1, 2),
    _Rm10010AlmClientLossOfSyncPortn_Type()
)
rm10010AlmClientLossOfSyncPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmClientLossOfSyncPortn.setStatus("current")
_Rm10010AlmClientInputLossOfSigPortn_Type = EkiOnOff
_Rm10010AlmClientInputLossOfSigPortn_Object = MibTableColumn
rm10010AlmClientInputLossOfSigPortn = _Rm10010AlmClientInputLossOfSigPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 2, 88, 1, 3),
    _Rm10010AlmClientInputLossOfSigPortn_Type()
)
rm10010AlmClientInputLossOfSigPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmClientInputLossOfSigPortn.setStatus("current")
_Rm10010AlmClientLanesMarkerUnlockPortn_Type = EkiOnOff
_Rm10010AlmClientLanesMarkerUnlockPortn_Object = MibTableColumn
rm10010AlmClientLanesMarkerUnlockPortn = _Rm10010AlmClientLanesMarkerUnlockPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 2, 88, 1, 4),
    _Rm10010AlmClientLanesMarkerUnlockPortn_Type()
)
rm10010AlmClientLanesMarkerUnlockPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmClientLanesMarkerUnlockPortn.setStatus("current")
_Rm10010AlmClientLanes6466UnlockPortn_Type = EkiOnOff
_Rm10010AlmClientLanes6466UnlockPortn_Object = MibTableColumn
rm10010AlmClientLanes6466UnlockPortn = _Rm10010AlmClientLanes6466UnlockPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 2, 88, 1, 5),
    _Rm10010AlmClientLanes6466UnlockPortn_Type()
)
rm10010AlmClientLanes6466UnlockPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmClientLanes6466UnlockPortn.setStatus("current")
_Rm10010AlmClientLanesNotAlignedPortn_Type = EkiOnOff
_Rm10010AlmClientLanesNotAlignedPortn_Object = MibTableColumn
rm10010AlmClientLanesNotAlignedPortn = _Rm10010AlmClientLanesNotAlignedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 2, 88, 1, 6),
    _Rm10010AlmClientLanesNotAlignedPortn_Type()
)
rm10010AlmClientLanesNotAlignedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmClientLanesNotAlignedPortn.setStatus("current")
_Rm10010AlmClientCsfDetectedPortn_Type = EkiOnOff
_Rm10010AlmClientCsfDetectedPortn_Object = MibTableColumn
rm10010AlmClientCsfDetectedPortn = _Rm10010AlmClientCsfDetectedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 2, 88, 1, 7),
    _Rm10010AlmClientCsfDetectedPortn_Type()
)
rm10010AlmClientCsfDetectedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmClientCsfDetectedPortn.setStatus("current")
_Rm10010AlmClientTxHostLolPortn_Type = EkiOnOff
_Rm10010AlmClientTxHostLolPortn_Object = MibTableColumn
rm10010AlmClientTxHostLolPortn = _Rm10010AlmClientTxHostLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 2, 88, 1, 10),
    _Rm10010AlmClientTxHostLolPortn_Type()
)
rm10010AlmClientTxHostLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmClientTxHostLolPortn.setStatus("current")
_Rm10010AlmClientLaneTxFifoErrorPortn_Type = EkiOnOff
_Rm10010AlmClientLaneTxFifoErrorPortn_Object = MibTableColumn
rm10010AlmClientLaneTxFifoErrorPortn = _Rm10010AlmClientLaneTxFifoErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 2, 88, 1, 11),
    _Rm10010AlmClientLaneTxFifoErrorPortn_Type()
)
rm10010AlmClientLaneTxFifoErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmClientLaneTxFifoErrorPortn.setStatus("current")
_Rm10010AlmclientSfpAlmDdmTable_Object = MibTable
rm10010AlmclientSfpAlmDdmTable = _Rm10010AlmclientSfpAlmDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 2, 216)
)
if mibBuilder.loadTexts:
    rm10010AlmclientSfpAlmDdmTable.setStatus("current")
_Rm10010AlmclientSfpAlmDdmEntry_Object = MibTableRow
rm10010AlmclientSfpAlmDdmEntry = _Rm10010AlmclientSfpAlmDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 2, 216, 1)
)
rm10010AlmclientSfpAlmDdmEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010AlmclientSfpAlmDdmIndex"),
)
if mibBuilder.loadTexts:
    rm10010AlmclientSfpAlmDdmEntry.setStatus("current")


class _Rm10010AlmclientSfpAlmDdmIndex_Type(Integer32):
    """Custom type rm10010AlmclientSfpAlmDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010AlmclientSfpAlmDdmIndex_Type.__name__ = "Integer32"
_Rm10010AlmclientSfpAlmDdmIndex_Object = MibTableColumn
rm10010AlmclientSfpAlmDdmIndex = _Rm10010AlmclientSfpAlmDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 2, 216, 1, 1),
    _Rm10010AlmclientSfpAlmDdmIndex_Type()
)
rm10010AlmclientSfpAlmDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmclientSfpAlmDdmIndex.setStatus("current")
_Rm10010AlmTxPwrLowAlaPortn_Type = EkiOnOff
_Rm10010AlmTxPwrLowAlaPortn_Object = MibTableColumn
rm10010AlmTxPwrLowAlaPortn = _Rm10010AlmTxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 2, 216, 1, 2),
    _Rm10010AlmTxPwrLowAlaPortn_Type()
)
rm10010AlmTxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmTxPwrLowAlaPortn.setStatus("current")
_Rm10010AlmTxPwrHighAlaPortn_Type = EkiOnOff
_Rm10010AlmTxPwrHighAlaPortn_Object = MibTableColumn
rm10010AlmTxPwrHighAlaPortn = _Rm10010AlmTxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 2, 216, 1, 3),
    _Rm10010AlmTxPwrHighAlaPortn_Type()
)
rm10010AlmTxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmTxPwrHighAlaPortn.setStatus("current")
_Rm10010AlmTxBiasLowAlaPortn_Type = EkiOnOff
_Rm10010AlmTxBiasLowAlaPortn_Object = MibTableColumn
rm10010AlmTxBiasLowAlaPortn = _Rm10010AlmTxBiasLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 2, 216, 1, 4),
    _Rm10010AlmTxBiasLowAlaPortn_Type()
)
rm10010AlmTxBiasLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmTxBiasLowAlaPortn.setStatus("current")
_Rm10010AlmTxBiasHighAlaPortn_Type = EkiOnOff
_Rm10010AlmTxBiasHighAlaPortn_Object = MibTableColumn
rm10010AlmTxBiasHighAlaPortn = _Rm10010AlmTxBiasHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 2, 216, 1, 5),
    _Rm10010AlmTxBiasHighAlaPortn_Type()
)
rm10010AlmTxBiasHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmTxBiasHighAlaPortn.setStatus("current")
_Rm10010AlmVccLowAlaPortn_Type = EkiOnOff
_Rm10010AlmVccLowAlaPortn_Object = MibTableColumn
rm10010AlmVccLowAlaPortn = _Rm10010AlmVccLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 2, 216, 1, 6),
    _Rm10010AlmVccLowAlaPortn_Type()
)
rm10010AlmVccLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmVccLowAlaPortn.setStatus("current")
_Rm10010AlmVccHighAlaPortn_Type = EkiOnOff
_Rm10010AlmVccHighAlaPortn_Object = MibTableColumn
rm10010AlmVccHighAlaPortn = _Rm10010AlmVccHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 2, 216, 1, 7),
    _Rm10010AlmVccHighAlaPortn_Type()
)
rm10010AlmVccHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmVccHighAlaPortn.setStatus("current")
_Rm10010AlmTempLowAlaPortn_Type = EkiOnOff
_Rm10010AlmTempLowAlaPortn_Object = MibTableColumn
rm10010AlmTempLowAlaPortn = _Rm10010AlmTempLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 2, 216, 1, 8),
    _Rm10010AlmTempLowAlaPortn_Type()
)
rm10010AlmTempLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmTempLowAlaPortn.setStatus("current")
_Rm10010AlmTempHighAlaPortn_Type = EkiOnOff
_Rm10010AlmTempHighAlaPortn_Object = MibTableColumn
rm10010AlmTempHighAlaPortn = _Rm10010AlmTempHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 2, 216, 1, 9),
    _Rm10010AlmTempHighAlaPortn_Type()
)
rm10010AlmTempHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmTempHighAlaPortn.setStatus("current")
_Rm10010AlmRxPwrLowAlaPortn_Type = EkiOnOff
_Rm10010AlmRxPwrLowAlaPortn_Object = MibTableColumn
rm10010AlmRxPwrLowAlaPortn = _Rm10010AlmRxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 2, 216, 1, 16),
    _Rm10010AlmRxPwrLowAlaPortn_Type()
)
rm10010AlmRxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmRxPwrLowAlaPortn.setStatus("current")
_Rm10010AlmRxPwrHighAlaPortn_Type = EkiOnOff
_Rm10010AlmRxPwrHighAlaPortn_Object = MibTableColumn
rm10010AlmRxPwrHighAlaPortn = _Rm10010AlmRxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 2, 216, 1, 17),
    _Rm10010AlmRxPwrHighAlaPortn_Type()
)
rm10010AlmRxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmRxPwrHighAlaPortn.setStatus("current")
_Rm10010AlmClientCrit_ObjectIdentity = ObjectIdentity
rm10010AlmClientCrit = _Rm10010AlmClientCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 3)
)
_Rm10010AlmsynthAlmPortTable_Object = MibTable
rm10010AlmsynthAlmPortTable = _Rm10010AlmsynthAlmPortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 3, 8)
)
if mibBuilder.loadTexts:
    rm10010AlmsynthAlmPortTable.setStatus("current")
_Rm10010AlmsynthAlmPortEntry_Object = MibTableRow
rm10010AlmsynthAlmPortEntry = _Rm10010AlmsynthAlmPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 3, 8, 1)
)
rm10010AlmsynthAlmPortEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010AlmsynthAlmPortIndex"),
)
if mibBuilder.loadTexts:
    rm10010AlmsynthAlmPortEntry.setStatus("current")


class _Rm10010AlmsynthAlmPortIndex_Type(Integer32):
    """Custom type rm10010AlmsynthAlmPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010AlmsynthAlmPortIndex_Type.__name__ = "Integer32"
_Rm10010AlmsynthAlmPortIndex_Object = MibTableColumn
rm10010AlmsynthAlmPortIndex = _Rm10010AlmsynthAlmPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 3, 8, 1, 1),
    _Rm10010AlmsynthAlmPortIndex_Type()
)
rm10010AlmsynthAlmPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmsynthAlmPortIndex.setStatus("current")
_Rm10010AlmSfpAbsentPortn_Type = EkiOnOff
_Rm10010AlmSfpAbsentPortn_Object = MibTableColumn
rm10010AlmSfpAbsentPortn = _Rm10010AlmSfpAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 3, 8, 1, 2),
    _Rm10010AlmSfpAbsentPortn_Type()
)
rm10010AlmSfpAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmSfpAbsentPortn.setStatus("current")
_Rm10010AlmDdmAbsentPortn_Type = EkiOnOff
_Rm10010AlmDdmAbsentPortn_Object = MibTableColumn
rm10010AlmDdmAbsentPortn = _Rm10010AlmDdmAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 3, 8, 1, 3),
    _Rm10010AlmDdmAbsentPortn_Type()
)
rm10010AlmDdmAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmDdmAbsentPortn.setStatus("current")
_Rm10010AlmHwFailAccPortn_Type = EkiOnOff
_Rm10010AlmHwFailAccPortn_Object = MibTableColumn
rm10010AlmHwFailAccPortn = _Rm10010AlmHwFailAccPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 3, 8, 1, 5),
    _Rm10010AlmHwFailAccPortn_Type()
)
rm10010AlmHwFailAccPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmHwFailAccPortn.setStatus("current")
_Rm10010AlmDwLsdPortn_Type = EkiOnOff
_Rm10010AlmDwLsdPortn_Object = MibTableColumn
rm10010AlmDwLsdPortn = _Rm10010AlmDwLsdPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 3, 8, 1, 6),
    _Rm10010AlmDwLsdPortn_Type()
)
rm10010AlmDwLsdPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmDwLsdPortn.setStatus("current")
_Rm10010AlmClientLocalOosPortn_Type = EkiOnOff
_Rm10010AlmClientLocalOosPortn_Object = MibTableColumn
rm10010AlmClientLocalOosPortn = _Rm10010AlmClientLocalOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 3, 8, 1, 7),
    _Rm10010AlmClientLocalOosPortn_Type()
)
rm10010AlmClientLocalOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmClientLocalOosPortn.setStatus("current")
_Rm10010AlmClientRemoteOosPortn_Type = EkiOnOff
_Rm10010AlmClientRemoteOosPortn_Object = MibTableColumn
rm10010AlmClientRemoteOosPortn = _Rm10010AlmClientRemoteOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 3, 8, 1, 8),
    _Rm10010AlmClientRemoteOosPortn_Type()
)
rm10010AlmClientRemoteOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmClientRemoteOosPortn.setStatus("current")
_Rm10010AlmDwCaisPortn_Type = EkiOnOff
_Rm10010AlmDwCaisPortn_Object = MibTableColumn
rm10010AlmDwCaisPortn = _Rm10010AlmDwCaisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 3, 8, 1, 9),
    _Rm10010AlmDwCaisPortn_Type()
)
rm10010AlmDwCaisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmDwCaisPortn.setStatus("current")
_Rm10010AlmSfpDdmWarningPortn_Type = EkiOnOff
_Rm10010AlmSfpDdmWarningPortn_Object = MibTableColumn
rm10010AlmSfpDdmWarningPortn = _Rm10010AlmSfpDdmWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 3, 8, 1, 10),
    _Rm10010AlmSfpDdmWarningPortn_Type()
)
rm10010AlmSfpDdmWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmSfpDdmWarningPortn.setStatus("current")
_Rm10010AlmSfpDdmAlmPortn_Type = EkiOnOff
_Rm10010AlmSfpDdmAlmPortn_Object = MibTableColumn
rm10010AlmSfpDdmAlmPortn = _Rm10010AlmSfpDdmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 3, 8, 1, 11),
    _Rm10010AlmSfpDdmAlmPortn_Type()
)
rm10010AlmSfpDdmAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmSfpDdmAlmPortn.setStatus("current")
_Rm10010AlmFailAccPortn_Type = EkiOnOff
_Rm10010AlmFailAccPortn_Object = MibTableColumn
rm10010AlmFailAccPortn = _Rm10010AlmFailAccPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 3, 8, 1, 13),
    _Rm10010AlmFailAccPortn_Type()
)
rm10010AlmFailAccPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmFailAccPortn.setStatus("current")
_Rm10010AlmUpCsfPortn_Type = EkiOnOff
_Rm10010AlmUpCsfPortn_Object = MibTableColumn
rm10010AlmUpCsfPortn = _Rm10010AlmUpCsfPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 2, 3, 8, 1, 17),
    _Rm10010AlmUpCsfPortn_Type()
)
rm10010AlmUpCsfPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmUpCsfPortn.setStatus("current")
_Rm10010AlmLine_ObjectIdentity = ObjectIdentity
rm10010AlmLine = _Rm10010AlmLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3)
)
_Rm10010AlmLineNurg_ObjectIdentity = ObjectIdentity
rm10010AlmLineNurg = _Rm10010AlmLineNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 1)
)
_Rm10010AlmlineNetworkLaneAlarmWarning1Table_Object = MibTable
rm10010AlmlineNetworkLaneAlarmWarning1Table = _Rm10010AlmlineNetworkLaneAlarmWarning1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 1, 104)
)
if mibBuilder.loadTexts:
    rm10010AlmlineNetworkLaneAlarmWarning1Table.setStatus("current")
_Rm10010AlmlineNetworkLaneAlarmWarning1Entry_Object = MibTableRow
rm10010AlmlineNetworkLaneAlarmWarning1Entry = _Rm10010AlmlineNetworkLaneAlarmWarning1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 1, 104, 1)
)
rm10010AlmlineNetworkLaneAlarmWarning1Entry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010AlmlineNetworkLaneAlarmWarning1Index"),
)
if mibBuilder.loadTexts:
    rm10010AlmlineNetworkLaneAlarmWarning1Entry.setStatus("current")


class _Rm10010AlmlineNetworkLaneAlarmWarning1Index_Type(Integer32):
    """Custom type rm10010AlmlineNetworkLaneAlarmWarning1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010AlmlineNetworkLaneAlarmWarning1Index_Type.__name__ = "Integer32"
_Rm10010AlmlineNetworkLaneAlarmWarning1Index_Object = MibTableColumn
rm10010AlmlineNetworkLaneAlarmWarning1Index = _Rm10010AlmlineNetworkLaneAlarmWarning1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 1, 104, 1, 1),
    _Rm10010AlmlineNetworkLaneAlarmWarning1Index_Type()
)
rm10010AlmlineNetworkLaneAlarmWarning1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmlineNetworkLaneAlarmWarning1Index.setStatus("current")
_Rm10010AlmLineRxPowerLowAlarmPortn_Type = EkiOnOff
_Rm10010AlmLineRxPowerLowAlarmPortn_Object = MibTableColumn
rm10010AlmLineRxPowerLowAlarmPortn = _Rm10010AlmLineRxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 1, 104, 1, 2),
    _Rm10010AlmLineRxPowerLowAlarmPortn_Type()
)
rm10010AlmLineRxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmLineRxPowerLowAlarmPortn.setStatus("current")
_Rm10010AlmLineRxPowerLowWarningPortn_Type = EkiOnOff
_Rm10010AlmLineRxPowerLowWarningPortn_Object = MibTableColumn
rm10010AlmLineRxPowerLowWarningPortn = _Rm10010AlmLineRxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 1, 104, 1, 3),
    _Rm10010AlmLineRxPowerLowWarningPortn_Type()
)
rm10010AlmLineRxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmLineRxPowerLowWarningPortn.setStatus("current")
_Rm10010AlmLineRxPowerHighWarningPortn_Type = EkiOnOff
_Rm10010AlmLineRxPowerHighWarningPortn_Object = MibTableColumn
rm10010AlmLineRxPowerHighWarningPortn = _Rm10010AlmLineRxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 1, 104, 1, 4),
    _Rm10010AlmLineRxPowerHighWarningPortn_Type()
)
rm10010AlmLineRxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmLineRxPowerHighWarningPortn.setStatus("current")
_Rm10010AlmLineRxPowerHighAlarmPortn_Type = EkiOnOff
_Rm10010AlmLineRxPowerHighAlarmPortn_Object = MibTableColumn
rm10010AlmLineRxPowerHighAlarmPortn = _Rm10010AlmLineRxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 1, 104, 1, 5),
    _Rm10010AlmLineRxPowerHighAlarmPortn_Type()
)
rm10010AlmLineRxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmLineRxPowerHighAlarmPortn.setStatus("current")
_Rm10010AlmLineLaserTempLowAlarmPortn_Type = EkiOnOff
_Rm10010AlmLineLaserTempLowAlarmPortn_Object = MibTableColumn
rm10010AlmLineLaserTempLowAlarmPortn = _Rm10010AlmLineLaserTempLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 1, 104, 1, 6),
    _Rm10010AlmLineLaserTempLowAlarmPortn_Type()
)
rm10010AlmLineLaserTempLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmLineLaserTempLowAlarmPortn.setStatus("current")
_Rm10010AlmLineLaserTempLowWarningPortn_Type = EkiOnOff
_Rm10010AlmLineLaserTempLowWarningPortn_Object = MibTableColumn
rm10010AlmLineLaserTempLowWarningPortn = _Rm10010AlmLineLaserTempLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 1, 104, 1, 7),
    _Rm10010AlmLineLaserTempLowWarningPortn_Type()
)
rm10010AlmLineLaserTempLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmLineLaserTempLowWarningPortn.setStatus("current")
_Rm10010AlmLineLaserTempHighWarningPortn_Type = EkiOnOff
_Rm10010AlmLineLaserTempHighWarningPortn_Object = MibTableColumn
rm10010AlmLineLaserTempHighWarningPortn = _Rm10010AlmLineLaserTempHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 1, 104, 1, 8),
    _Rm10010AlmLineLaserTempHighWarningPortn_Type()
)
rm10010AlmLineLaserTempHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmLineLaserTempHighWarningPortn.setStatus("current")
_Rm10010AlmLineLaserTempHighAlarmPortn_Type = EkiOnOff
_Rm10010AlmLineLaserTempHighAlarmPortn_Object = MibTableColumn
rm10010AlmLineLaserTempHighAlarmPortn = _Rm10010AlmLineLaserTempHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 1, 104, 1, 9),
    _Rm10010AlmLineLaserTempHighAlarmPortn_Type()
)
rm10010AlmLineLaserTempHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmLineLaserTempHighAlarmPortn.setStatus("current")
_Rm10010AlmLineTxPowerLowAlarmPortn_Type = EkiOnOff
_Rm10010AlmLineTxPowerLowAlarmPortn_Object = MibTableColumn
rm10010AlmLineTxPowerLowAlarmPortn = _Rm10010AlmLineTxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 1, 104, 1, 10),
    _Rm10010AlmLineTxPowerLowAlarmPortn_Type()
)
rm10010AlmLineTxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmLineTxPowerLowAlarmPortn.setStatus("current")
_Rm10010AlmLineTxPowerLowWarningPortn_Type = EkiOnOff
_Rm10010AlmLineTxPowerLowWarningPortn_Object = MibTableColumn
rm10010AlmLineTxPowerLowWarningPortn = _Rm10010AlmLineTxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 1, 104, 1, 11),
    _Rm10010AlmLineTxPowerLowWarningPortn_Type()
)
rm10010AlmLineTxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmLineTxPowerLowWarningPortn.setStatus("current")
_Rm10010AlmLineTxPowerHighWarningPortn_Type = EkiOnOff
_Rm10010AlmLineTxPowerHighWarningPortn_Object = MibTableColumn
rm10010AlmLineTxPowerHighWarningPortn = _Rm10010AlmLineTxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 1, 104, 1, 12),
    _Rm10010AlmLineTxPowerHighWarningPortn_Type()
)
rm10010AlmLineTxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmLineTxPowerHighWarningPortn.setStatus("current")
_Rm10010AlmLineTxPowerHighAlarmPortn_Type = EkiOnOff
_Rm10010AlmLineTxPowerHighAlarmPortn_Object = MibTableColumn
rm10010AlmLineTxPowerHighAlarmPortn = _Rm10010AlmLineTxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 1, 104, 1, 13),
    _Rm10010AlmLineTxPowerHighAlarmPortn_Type()
)
rm10010AlmLineTxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmLineTxPowerHighAlarmPortn.setStatus("current")
_Rm10010AlmLineBiasLowAlarmPortn_Type = EkiOnOff
_Rm10010AlmLineBiasLowAlarmPortn_Object = MibTableColumn
rm10010AlmLineBiasLowAlarmPortn = _Rm10010AlmLineBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 1, 104, 1, 14),
    _Rm10010AlmLineBiasLowAlarmPortn_Type()
)
rm10010AlmLineBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmLineBiasLowAlarmPortn.setStatus("current")
_Rm10010AlmLineBiasLowWarningPortn_Type = EkiOnOff
_Rm10010AlmLineBiasLowWarningPortn_Object = MibTableColumn
rm10010AlmLineBiasLowWarningPortn = _Rm10010AlmLineBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 1, 104, 1, 15),
    _Rm10010AlmLineBiasLowWarningPortn_Type()
)
rm10010AlmLineBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmLineBiasLowWarningPortn.setStatus("current")
_Rm10010AlmLineBiasHighWarningPortn_Type = EkiOnOff
_Rm10010AlmLineBiasHighWarningPortn_Object = MibTableColumn
rm10010AlmLineBiasHighWarningPortn = _Rm10010AlmLineBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 1, 104, 1, 16),
    _Rm10010AlmLineBiasHighWarningPortn_Type()
)
rm10010AlmLineBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmLineBiasHighWarningPortn.setStatus("current")
_Rm10010AlmLineBiasHighAlarmPortn_Type = EkiOnOff
_Rm10010AlmLineBiasHighAlarmPortn_Object = MibTableColumn
rm10010AlmLineBiasHighAlarmPortn = _Rm10010AlmLineBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 1, 104, 1, 17),
    _Rm10010AlmLineBiasHighAlarmPortn_Type()
)
rm10010AlmLineBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmLineBiasHighAlarmPortn.setStatus("current")
_Rm10010AlmlineNetworkLaneAlarmWarning2Table_Object = MibTable
rm10010AlmlineNetworkLaneAlarmWarning2Table = _Rm10010AlmlineNetworkLaneAlarmWarning2Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 1, 120)
)
if mibBuilder.loadTexts:
    rm10010AlmlineNetworkLaneAlarmWarning2Table.setStatus("current")
_Rm10010AlmlineNetworkLaneAlarmWarning2Entry_Object = MibTableRow
rm10010AlmlineNetworkLaneAlarmWarning2Entry = _Rm10010AlmlineNetworkLaneAlarmWarning2Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 1, 120, 1)
)
rm10010AlmlineNetworkLaneAlarmWarning2Entry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010AlmlineNetworkLaneAlarmWarning2Index"),
)
if mibBuilder.loadTexts:
    rm10010AlmlineNetworkLaneAlarmWarning2Entry.setStatus("current")


class _Rm10010AlmlineNetworkLaneAlarmWarning2Index_Type(Integer32):
    """Custom type rm10010AlmlineNetworkLaneAlarmWarning2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010AlmlineNetworkLaneAlarmWarning2Index_Type.__name__ = "Integer32"
_Rm10010AlmlineNetworkLaneAlarmWarning2Index_Object = MibTableColumn
rm10010AlmlineNetworkLaneAlarmWarning2Index = _Rm10010AlmlineNetworkLaneAlarmWarning2Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 1, 120, 1, 1),
    _Rm10010AlmlineNetworkLaneAlarmWarning2Index_Type()
)
rm10010AlmlineNetworkLaneAlarmWarning2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmlineNetworkLaneAlarmWarning2Index.setStatus("current")
_Rm10010AlmTxModulatorBiasLowAlarmPortn_Type = EkiOnOff
_Rm10010AlmTxModulatorBiasLowAlarmPortn_Object = MibTableColumn
rm10010AlmTxModulatorBiasLowAlarmPortn = _Rm10010AlmTxModulatorBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 1, 120, 1, 2),
    _Rm10010AlmTxModulatorBiasLowAlarmPortn_Type()
)
rm10010AlmTxModulatorBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmTxModulatorBiasLowAlarmPortn.setStatus("current")
_Rm10010AlmTxModulatorBiasLowWarningPortn_Type = EkiOnOff
_Rm10010AlmTxModulatorBiasLowWarningPortn_Object = MibTableColumn
rm10010AlmTxModulatorBiasLowWarningPortn = _Rm10010AlmTxModulatorBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 1, 120, 1, 3),
    _Rm10010AlmTxModulatorBiasLowWarningPortn_Type()
)
rm10010AlmTxModulatorBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmTxModulatorBiasLowWarningPortn.setStatus("current")
_Rm10010AlmTxModulatorBiasHighWarningPortn_Type = EkiOnOff
_Rm10010AlmTxModulatorBiasHighWarningPortn_Object = MibTableColumn
rm10010AlmTxModulatorBiasHighWarningPortn = _Rm10010AlmTxModulatorBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 1, 120, 1, 4),
    _Rm10010AlmTxModulatorBiasHighWarningPortn_Type()
)
rm10010AlmTxModulatorBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmTxModulatorBiasHighWarningPortn.setStatus("current")
_Rm10010AlmTxModulatorBiasHighAlarmPortn_Type = EkiOnOff
_Rm10010AlmTxModulatorBiasHighAlarmPortn_Object = MibTableColumn
rm10010AlmTxModulatorBiasHighAlarmPortn = _Rm10010AlmTxModulatorBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 1, 120, 1, 5),
    _Rm10010AlmTxModulatorBiasHighAlarmPortn_Type()
)
rm10010AlmTxModulatorBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmTxModulatorBiasHighAlarmPortn.setStatus("current")
_Rm10010AlmRxLaserTempLowAlarmPortn_Type = EkiOnOff
_Rm10010AlmRxLaserTempLowAlarmPortn_Object = MibTableColumn
rm10010AlmRxLaserTempLowAlarmPortn = _Rm10010AlmRxLaserTempLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 1, 120, 1, 6),
    _Rm10010AlmRxLaserTempLowAlarmPortn_Type()
)
rm10010AlmRxLaserTempLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmRxLaserTempLowAlarmPortn.setStatus("current")
_Rm10010AlmRxLaserTempLowWarningPortn_Type = EkiOnOff
_Rm10010AlmRxLaserTempLowWarningPortn_Object = MibTableColumn
rm10010AlmRxLaserTempLowWarningPortn = _Rm10010AlmRxLaserTempLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 1, 120, 1, 7),
    _Rm10010AlmRxLaserTempLowWarningPortn_Type()
)
rm10010AlmRxLaserTempLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmRxLaserTempLowWarningPortn.setStatus("current")
_Rm10010AlmRxLaserTempHighWarningPortn_Type = EkiOnOff
_Rm10010AlmRxLaserTempHighWarningPortn_Object = MibTableColumn
rm10010AlmRxLaserTempHighWarningPortn = _Rm10010AlmRxLaserTempHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 1, 120, 1, 8),
    _Rm10010AlmRxLaserTempHighWarningPortn_Type()
)
rm10010AlmRxLaserTempHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmRxLaserTempHighWarningPortn.setStatus("current")
_Rm10010AlmRxLaserTempHighAlarmPortn_Type = EkiOnOff
_Rm10010AlmRxLaserTempHighAlarmPortn_Object = MibTableColumn
rm10010AlmRxLaserTempHighAlarmPortn = _Rm10010AlmRxLaserTempHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 1, 120, 1, 9),
    _Rm10010AlmRxLaserTempHighAlarmPortn_Type()
)
rm10010AlmRxLaserTempHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmRxLaserTempHighAlarmPortn.setStatus("current")
_Rm10010AlmRxLaserOutputLowAlarmPortn_Type = EkiOnOff
_Rm10010AlmRxLaserOutputLowAlarmPortn_Object = MibTableColumn
rm10010AlmRxLaserOutputLowAlarmPortn = _Rm10010AlmRxLaserOutputLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 1, 120, 1, 10),
    _Rm10010AlmRxLaserOutputLowAlarmPortn_Type()
)
rm10010AlmRxLaserOutputLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmRxLaserOutputLowAlarmPortn.setStatus("current")
_Rm10010AlmRxLaserOutputLowWarningPortn_Type = EkiOnOff
_Rm10010AlmRxLaserOutputLowWarningPortn_Object = MibTableColumn
rm10010AlmRxLaserOutputLowWarningPortn = _Rm10010AlmRxLaserOutputLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 1, 120, 1, 11),
    _Rm10010AlmRxLaserOutputLowWarningPortn_Type()
)
rm10010AlmRxLaserOutputLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmRxLaserOutputLowWarningPortn.setStatus("current")
_Rm10010AlmRxLaserOutputHighWarningPortn_Type = EkiOnOff
_Rm10010AlmRxLaserOutputHighWarningPortn_Object = MibTableColumn
rm10010AlmRxLaserOutputHighWarningPortn = _Rm10010AlmRxLaserOutputHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 1, 120, 1, 12),
    _Rm10010AlmRxLaserOutputHighWarningPortn_Type()
)
rm10010AlmRxLaserOutputHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmRxLaserOutputHighWarningPortn.setStatus("current")
_Rm10010AlmRxLaserOutputHighAlarmPortn_Type = EkiOnOff
_Rm10010AlmRxLaserOutputHighAlarmPortn_Object = MibTableColumn
rm10010AlmRxLaserOutputHighAlarmPortn = _Rm10010AlmRxLaserOutputHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 1, 120, 1, 13),
    _Rm10010AlmRxLaserOutputHighAlarmPortn_Type()
)
rm10010AlmRxLaserOutputHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmRxLaserOutputHighAlarmPortn.setStatus("current")
_Rm10010AlmRxLaserBiasLowAlarmPortn_Type = EkiOnOff
_Rm10010AlmRxLaserBiasLowAlarmPortn_Object = MibTableColumn
rm10010AlmRxLaserBiasLowAlarmPortn = _Rm10010AlmRxLaserBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 1, 120, 1, 14),
    _Rm10010AlmRxLaserBiasLowAlarmPortn_Type()
)
rm10010AlmRxLaserBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmRxLaserBiasLowAlarmPortn.setStatus("current")
_Rm10010AlmRxLaserBiasLowWarningPortn_Type = EkiOnOff
_Rm10010AlmRxLaserBiasLowWarningPortn_Object = MibTableColumn
rm10010AlmRxLaserBiasLowWarningPortn = _Rm10010AlmRxLaserBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 1, 120, 1, 15),
    _Rm10010AlmRxLaserBiasLowWarningPortn_Type()
)
rm10010AlmRxLaserBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmRxLaserBiasLowWarningPortn.setStatus("current")
_Rm10010AlmRxLaserBiasHighWarningPortn_Type = EkiOnOff
_Rm10010AlmRxLaserBiasHighWarningPortn_Object = MibTableColumn
rm10010AlmRxLaserBiasHighWarningPortn = _Rm10010AlmRxLaserBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 1, 120, 1, 16),
    _Rm10010AlmRxLaserBiasHighWarningPortn_Type()
)
rm10010AlmRxLaserBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmRxLaserBiasHighWarningPortn.setStatus("current")
_Rm10010AlmRxLaserBiasHighAlarmPortn_Type = EkiOnOff
_Rm10010AlmRxLaserBiasHighAlarmPortn_Object = MibTableColumn
rm10010AlmRxLaserBiasHighAlarmPortn = _Rm10010AlmRxLaserBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 1, 120, 1, 17),
    _Rm10010AlmRxLaserBiasHighAlarmPortn_Type()
)
rm10010AlmRxLaserBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmRxLaserBiasHighAlarmPortn.setStatus("current")
_Rm10010AlmLineUrg_ObjectIdentity = ObjectIdentity
rm10010AlmLineUrg = _Rm10010AlmLineUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 2)
)
_Rm10010AlmlineNetworkLaneFaultTable_Object = MibTable
rm10010AlmlineNetworkLaneFaultTable = _Rm10010AlmlineNetworkLaneFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 2, 136)
)
if mibBuilder.loadTexts:
    rm10010AlmlineNetworkLaneFaultTable.setStatus("current")
_Rm10010AlmlineNetworkLaneFaultEntry_Object = MibTableRow
rm10010AlmlineNetworkLaneFaultEntry = _Rm10010AlmlineNetworkLaneFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 2, 136, 1)
)
rm10010AlmlineNetworkLaneFaultEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010AlmlineNetworkLaneFaultIndex"),
)
if mibBuilder.loadTexts:
    rm10010AlmlineNetworkLaneFaultEntry.setStatus("current")


class _Rm10010AlmlineNetworkLaneFaultIndex_Type(Integer32):
    """Custom type rm10010AlmlineNetworkLaneFaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010AlmlineNetworkLaneFaultIndex_Type.__name__ = "Integer32"
_Rm10010AlmlineNetworkLaneFaultIndex_Object = MibTableColumn
rm10010AlmlineNetworkLaneFaultIndex = _Rm10010AlmlineNetworkLaneFaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 2, 136, 1, 1),
    _Rm10010AlmlineNetworkLaneFaultIndex_Type()
)
rm10010AlmlineNetworkLaneFaultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmlineNetworkLaneFaultIndex.setStatus("current")
_Rm10010AlmLineLaneRxTecFaultPortn_Type = EkiOnOff
_Rm10010AlmLineLaneRxTecFaultPortn_Object = MibTableColumn
rm10010AlmLineLaneRxTecFaultPortn = _Rm10010AlmLineLaneRxTecFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 2, 136, 1, 3),
    _Rm10010AlmLineLaneRxTecFaultPortn_Type()
)
rm10010AlmLineLaneRxTecFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmLineLaneRxTecFaultPortn.setStatus("current")
_Rm10010AlmLineLaneRxFifoErrorPortn_Type = EkiOnOff
_Rm10010AlmLineLaneRxFifoErrorPortn_Object = MibTableColumn
rm10010AlmLineLaneRxFifoErrorPortn = _Rm10010AlmLineLaneRxFifoErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 2, 136, 1, 4),
    _Rm10010AlmLineLaneRxFifoErrorPortn_Type()
)
rm10010AlmLineLaneRxFifoErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmLineLaneRxFifoErrorPortn.setStatus("current")
_Rm10010AlmLineLaneRxLolPortn_Type = EkiOnOff
_Rm10010AlmLineLaneRxLolPortn_Object = MibTableColumn
rm10010AlmLineLaneRxLolPortn = _Rm10010AlmLineLaneRxLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 2, 136, 1, 5),
    _Rm10010AlmLineLaneRxLolPortn_Type()
)
rm10010AlmLineLaneRxLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmLineLaneRxLolPortn.setStatus("current")
_Rm10010AlmLineLaneRxLosPortn_Type = EkiOnOff
_Rm10010AlmLineLaneRxLosPortn_Object = MibTableColumn
rm10010AlmLineLaneRxLosPortn = _Rm10010AlmLineLaneRxLosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 2, 136, 1, 6),
    _Rm10010AlmLineLaneRxLosPortn_Type()
)
rm10010AlmLineLaneRxLosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmLineLaneRxLosPortn.setStatus("current")
_Rm10010AlmLineLaneTxLolPortn_Type = EkiOnOff
_Rm10010AlmLineLaneTxLolPortn_Object = MibTableColumn
rm10010AlmLineLaneTxLolPortn = _Rm10010AlmLineLaneTxLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 2, 136, 1, 8),
    _Rm10010AlmLineLaneTxLolPortn_Type()
)
rm10010AlmLineLaneTxLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmLineLaneTxLolPortn.setStatus("current")
_Rm10010AlmLineLaneTxLosfPortn_Type = EkiOnOff
_Rm10010AlmLineLaneTxLosfPortn_Object = MibTableColumn
rm10010AlmLineLaneTxLosfPortn = _Rm10010AlmLineLaneTxLosfPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 2, 136, 1, 9),
    _Rm10010AlmLineLaneTxLosfPortn_Type()
)
rm10010AlmLineLaneTxLosfPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmLineLaneTxLosfPortn.setStatus("current")
_Rm10010AlmLineLaneApdPowerSupplyPortn_Type = EkiOnOff
_Rm10010AlmLineLaneApdPowerSupplyPortn_Object = MibTableColumn
rm10010AlmLineLaneApdPowerSupplyPortn = _Rm10010AlmLineLaneApdPowerSupplyPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 2, 136, 1, 15),
    _Rm10010AlmLineLaneApdPowerSupplyPortn_Type()
)
rm10010AlmLineLaneApdPowerSupplyPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmLineLaneApdPowerSupplyPortn.setStatus("current")
_Rm10010AlmLineLaneWavelengthUnlockedPortn_Type = EkiOnOff
_Rm10010AlmLineLaneWavelengthUnlockedPortn_Object = MibTableColumn
rm10010AlmLineLaneWavelengthUnlockedPortn = _Rm10010AlmLineLaneWavelengthUnlockedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 2, 136, 1, 16),
    _Rm10010AlmLineLaneWavelengthUnlockedPortn_Type()
)
rm10010AlmLineLaneWavelengthUnlockedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmLineLaneWavelengthUnlockedPortn.setStatus("current")
_Rm10010AlmLineLaneTecFaultPortn_Type = EkiOnOff
_Rm10010AlmLineLaneTecFaultPortn_Object = MibTableColumn
rm10010AlmLineLaneTecFaultPortn = _Rm10010AlmLineLaneTecFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 2, 136, 1, 17),
    _Rm10010AlmLineLaneTecFaultPortn_Type()
)
rm10010AlmLineLaneTecFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmLineLaneTecFaultPortn.setStatus("current")
_Rm10010AlmlineHostLaneFaultTable_Object = MibTable
rm10010AlmlineHostLaneFaultTable = _Rm10010AlmlineHostLaneFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 2, 152)
)
if mibBuilder.loadTexts:
    rm10010AlmlineHostLaneFaultTable.setStatus("current")
_Rm10010AlmlineHostLaneFaultEntry_Object = MibTableRow
rm10010AlmlineHostLaneFaultEntry = _Rm10010AlmlineHostLaneFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 2, 152, 1)
)
rm10010AlmlineHostLaneFaultEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010AlmlineHostLaneFaultIndex"),
)
if mibBuilder.loadTexts:
    rm10010AlmlineHostLaneFaultEntry.setStatus("current")


class _Rm10010AlmlineHostLaneFaultIndex_Type(Integer32):
    """Custom type rm10010AlmlineHostLaneFaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010AlmlineHostLaneFaultIndex_Type.__name__ = "Integer32"
_Rm10010AlmlineHostLaneFaultIndex_Object = MibTableColumn
rm10010AlmlineHostLaneFaultIndex = _Rm10010AlmlineHostLaneFaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 2, 152, 1, 1),
    _Rm10010AlmlineHostLaneFaultIndex_Type()
)
rm10010AlmlineHostLaneFaultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmlineHostLaneFaultIndex.setStatus("current")
_Rm10010AlmLineInputLossOfSignalPortn_Type = EkiOnOff
_Rm10010AlmLineInputLossOfSignalPortn_Object = MibTableColumn
rm10010AlmLineInputLossOfSignalPortn = _Rm10010AlmLineInputLossOfSignalPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 2, 152, 1, 2),
    _Rm10010AlmLineInputLossOfSignalPortn_Type()
)
rm10010AlmLineInputLossOfSignalPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmLineInputLossOfSignalPortn.setStatus("current")
_Rm10010AlmLineLossOfFramePortn_Type = EkiOnOff
_Rm10010AlmLineLossOfFramePortn_Object = MibTableColumn
rm10010AlmLineLossOfFramePortn = _Rm10010AlmLineLossOfFramePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 2, 152, 1, 3),
    _Rm10010AlmLineLossOfFramePortn_Type()
)
rm10010AlmLineLossOfFramePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmLineLossOfFramePortn.setStatus("current")
_Rm10010AlmLineSmBdiInsertedPortn_Type = EkiOnOff
_Rm10010AlmLineSmBdiInsertedPortn_Object = MibTableColumn
rm10010AlmLineSmBdiInsertedPortn = _Rm10010AlmLineSmBdiInsertedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 2, 152, 1, 4),
    _Rm10010AlmLineSmBdiInsertedPortn_Type()
)
rm10010AlmLineSmBdiInsertedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmLineSmBdiInsertedPortn.setStatus("current")
_Rm10010AlmLineSmBdiDetectedPortn_Type = EkiOnOff
_Rm10010AlmLineSmBdiDetectedPortn_Object = MibTableColumn
rm10010AlmLineSmBdiDetectedPortn = _Rm10010AlmLineSmBdiDetectedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 2, 152, 1, 5),
    _Rm10010AlmLineSmBdiDetectedPortn_Type()
)
rm10010AlmLineSmBdiDetectedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmLineSmBdiDetectedPortn.setStatus("current")
_Rm10010AlmLineSmIaeInsertedPortn_Type = EkiOnOff
_Rm10010AlmLineSmIaeInsertedPortn_Object = MibTableColumn
rm10010AlmLineSmIaeInsertedPortn = _Rm10010AlmLineSmIaeInsertedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 2, 152, 1, 6),
    _Rm10010AlmLineSmIaeInsertedPortn_Type()
)
rm10010AlmLineSmIaeInsertedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmLineSmIaeInsertedPortn.setStatus("current")
_Rm10010AlmLineSmIaeDetectedPortn_Type = EkiOnOff
_Rm10010AlmLineSmIaeDetectedPortn_Object = MibTableColumn
rm10010AlmLineSmIaeDetectedPortn = _Rm10010AlmLineSmIaeDetectedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 2, 152, 1, 7),
    _Rm10010AlmLineSmIaeDetectedPortn_Type()
)
rm10010AlmLineSmIaeDetectedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmLineSmIaeDetectedPortn.setStatus("current")
_Rm10010AlmLineTxHostLolPortn_Type = EkiOnOff
_Rm10010AlmLineTxHostLolPortn_Object = MibTableColumn
rm10010AlmLineTxHostLolPortn = _Rm10010AlmLineTxHostLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 2, 152, 1, 10),
    _Rm10010AlmLineTxHostLolPortn_Type()
)
rm10010AlmLineTxHostLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmLineTxHostLolPortn.setStatus("current")
_Rm10010AlmLineLaneTxFifoErrorPortn_Type = EkiOnOff
_Rm10010AlmLineLaneTxFifoErrorPortn_Object = MibTableColumn
rm10010AlmLineLaneTxFifoErrorPortn = _Rm10010AlmLineLaneTxFifoErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 2, 152, 1, 11),
    _Rm10010AlmLineLaneTxFifoErrorPortn_Type()
)
rm10010AlmLineLaneTxFifoErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmLineLaneTxFifoErrorPortn.setStatus("current")
_Rm10010AlmlineNetworkLaneRxOtnTable_Object = MibTable
rm10010AlmlineNetworkLaneRxOtnTable = _Rm10010AlmlineNetworkLaneRxOtnTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 2, 168)
)
if mibBuilder.loadTexts:
    rm10010AlmlineNetworkLaneRxOtnTable.setStatus("current")
_Rm10010AlmlineNetworkLaneRxOtnEntry_Object = MibTableRow
rm10010AlmlineNetworkLaneRxOtnEntry = _Rm10010AlmlineNetworkLaneRxOtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 2, 168, 1)
)
rm10010AlmlineNetworkLaneRxOtnEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010AlmlineNetworkLaneRxOtnIndex"),
)
if mibBuilder.loadTexts:
    rm10010AlmlineNetworkLaneRxOtnEntry.setStatus("current")


class _Rm10010AlmlineNetworkLaneRxOtnIndex_Type(Integer32):
    """Custom type rm10010AlmlineNetworkLaneRxOtnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010AlmlineNetworkLaneRxOtnIndex_Type.__name__ = "Integer32"
_Rm10010AlmlineNetworkLaneRxOtnIndex_Object = MibTableColumn
rm10010AlmlineNetworkLaneRxOtnIndex = _Rm10010AlmlineNetworkLaneRxOtnIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 2, 168, 1, 1),
    _Rm10010AlmlineNetworkLaneRxOtnIndex_Type()
)
rm10010AlmlineNetworkLaneRxOtnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmlineNetworkLaneRxOtnIndex.setStatus("current")
_Rm10010AlmLineRxOtnOduAisPortn_Type = EkiOnOff
_Rm10010AlmLineRxOtnOduAisPortn_Object = MibTableColumn
rm10010AlmLineRxOtnOduAisPortn = _Rm10010AlmLineRxOtnOduAisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 2, 168, 1, 10),
    _Rm10010AlmLineRxOtnOduAisPortn_Type()
)
rm10010AlmLineRxOtnOduAisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmLineRxOtnOduAisPortn.setStatus("current")
_Rm10010AlmLineRxOtnOtuAisPortn_Type = EkiOnOff
_Rm10010AlmLineRxOtnOtuAisPortn_Object = MibTableColumn
rm10010AlmLineRxOtnOtuAisPortn = _Rm10010AlmLineRxOtnOtuAisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 2, 168, 1, 11),
    _Rm10010AlmLineRxOtnOtuAisPortn_Type()
)
rm10010AlmLineRxOtnOtuAisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmLineRxOtnOtuAisPortn.setStatus("current")
_Rm10010AlmLineRxSmBdiPortn_Type = EkiOnOff
_Rm10010AlmLineRxSmBdiPortn_Object = MibTableColumn
rm10010AlmLineRxSmBdiPortn = _Rm10010AlmLineRxSmBdiPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 2, 168, 1, 12),
    _Rm10010AlmLineRxSmBdiPortn_Type()
)
rm10010AlmLineRxSmBdiPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmLineRxSmBdiPortn.setStatus("current")
_Rm10010AlmLineRxOtnIaePortn_Type = EkiOnOff
_Rm10010AlmLineRxOtnIaePortn_Object = MibTableColumn
rm10010AlmLineRxOtnIaePortn = _Rm10010AlmLineRxOtnIaePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 2, 168, 1, 13),
    _Rm10010AlmLineRxOtnIaePortn_Type()
)
rm10010AlmLineRxOtnIaePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmLineRxOtnIaePortn.setStatus("current")
_Rm10010AlmLineRxOtnOomPortn_Type = EkiOnOff
_Rm10010AlmLineRxOtnOomPortn_Object = MibTableColumn
rm10010AlmLineRxOtnOomPortn = _Rm10010AlmLineRxOtnOomPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 2, 168, 1, 14),
    _Rm10010AlmLineRxOtnOomPortn_Type()
)
rm10010AlmLineRxOtnOomPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmLineRxOtnOomPortn.setStatus("current")
_Rm10010AlmLineRxOtnLomPortn_Type = EkiOnOff
_Rm10010AlmLineRxOtnLomPortn_Object = MibTableColumn
rm10010AlmLineRxOtnLomPortn = _Rm10010AlmLineRxOtnLomPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 2, 168, 1, 15),
    _Rm10010AlmLineRxOtnLomPortn_Type()
)
rm10010AlmLineRxOtnLomPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmLineRxOtnLomPortn.setStatus("current")
_Rm10010AlmLineRxOtnOofPortn_Type = EkiOnOff
_Rm10010AlmLineRxOtnOofPortn_Object = MibTableColumn
rm10010AlmLineRxOtnOofPortn = _Rm10010AlmLineRxOtnOofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 2, 168, 1, 16),
    _Rm10010AlmLineRxOtnOofPortn_Type()
)
rm10010AlmLineRxOtnOofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmLineRxOtnOofPortn.setStatus("current")
_Rm10010AlmLineRxOtnLofPortn_Type = EkiOnOff
_Rm10010AlmLineRxOtnLofPortn_Object = MibTableColumn
rm10010AlmLineRxOtnLofPortn = _Rm10010AlmLineRxOtnLofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 2, 168, 1, 17),
    _Rm10010AlmLineRxOtnLofPortn_Type()
)
rm10010AlmLineRxOtnLofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmLineRxOtnLofPortn.setStatus("current")
_Rm10010AlmlineHostLaneTxOtnTable_Object = MibTable
rm10010AlmlineHostLaneTxOtnTable = _Rm10010AlmlineHostLaneTxOtnTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 2, 184)
)
if mibBuilder.loadTexts:
    rm10010AlmlineHostLaneTxOtnTable.setStatus("current")
_Rm10010AlmlineHostLaneTxOtnEntry_Object = MibTableRow
rm10010AlmlineHostLaneTxOtnEntry = _Rm10010AlmlineHostLaneTxOtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 2, 184, 1)
)
rm10010AlmlineHostLaneTxOtnEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010AlmlineHostLaneTxOtnIndex"),
)
if mibBuilder.loadTexts:
    rm10010AlmlineHostLaneTxOtnEntry.setStatus("current")


class _Rm10010AlmlineHostLaneTxOtnIndex_Type(Integer32):
    """Custom type rm10010AlmlineHostLaneTxOtnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010AlmlineHostLaneTxOtnIndex_Type.__name__ = "Integer32"
_Rm10010AlmlineHostLaneTxOtnIndex_Object = MibTableColumn
rm10010AlmlineHostLaneTxOtnIndex = _Rm10010AlmlineHostLaneTxOtnIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 2, 184, 1, 1),
    _Rm10010AlmlineHostLaneTxOtnIndex_Type()
)
rm10010AlmlineHostLaneTxOtnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmlineHostLaneTxOtnIndex.setStatus("current")
_Rm10010AlmLineTxOtnOduAisPortn_Type = EkiOnOff
_Rm10010AlmLineTxOtnOduAisPortn_Object = MibTableColumn
rm10010AlmLineTxOtnOduAisPortn = _Rm10010AlmLineTxOtnOduAisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 2, 184, 1, 10),
    _Rm10010AlmLineTxOtnOduAisPortn_Type()
)
rm10010AlmLineTxOtnOduAisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmLineTxOtnOduAisPortn.setStatus("current")
_Rm10010AlmLineTxOtnOtuAisPortn_Type = EkiOnOff
_Rm10010AlmLineTxOtnOtuAisPortn_Object = MibTableColumn
rm10010AlmLineTxOtnOtuAisPortn = _Rm10010AlmLineTxOtnOtuAisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 2, 184, 1, 11),
    _Rm10010AlmLineTxOtnOtuAisPortn_Type()
)
rm10010AlmLineTxOtnOtuAisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmLineTxOtnOtuAisPortn.setStatus("current")
_Rm10010AlmLineTxSmBdiPortn_Type = EkiOnOff
_Rm10010AlmLineTxSmBdiPortn_Object = MibTableColumn
rm10010AlmLineTxSmBdiPortn = _Rm10010AlmLineTxSmBdiPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 2, 184, 1, 12),
    _Rm10010AlmLineTxSmBdiPortn_Type()
)
rm10010AlmLineTxSmBdiPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmLineTxSmBdiPortn.setStatus("current")
_Rm10010AlmLineTxOtnIaePortn_Type = EkiOnOff
_Rm10010AlmLineTxOtnIaePortn_Object = MibTableColumn
rm10010AlmLineTxOtnIaePortn = _Rm10010AlmLineTxOtnIaePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 2, 184, 1, 13),
    _Rm10010AlmLineTxOtnIaePortn_Type()
)
rm10010AlmLineTxOtnIaePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmLineTxOtnIaePortn.setStatus("current")
_Rm10010AlmLineTxOtnOomPortn_Type = EkiOnOff
_Rm10010AlmLineTxOtnOomPortn_Object = MibTableColumn
rm10010AlmLineTxOtnOomPortn = _Rm10010AlmLineTxOtnOomPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 2, 184, 1, 14),
    _Rm10010AlmLineTxOtnOomPortn_Type()
)
rm10010AlmLineTxOtnOomPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmLineTxOtnOomPortn.setStatus("current")
_Rm10010AlmLineTxOtnLomPortn_Type = EkiOnOff
_Rm10010AlmLineTxOtnLomPortn_Object = MibTableColumn
rm10010AlmLineTxOtnLomPortn = _Rm10010AlmLineTxOtnLomPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 2, 184, 1, 15),
    _Rm10010AlmLineTxOtnLomPortn_Type()
)
rm10010AlmLineTxOtnLomPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmLineTxOtnLomPortn.setStatus("current")
_Rm10010AlmLineTxOtnOofPortn_Type = EkiOnOff
_Rm10010AlmLineTxOtnOofPortn_Object = MibTableColumn
rm10010AlmLineTxOtnOofPortn = _Rm10010AlmLineTxOtnOofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 2, 184, 1, 16),
    _Rm10010AlmLineTxOtnOofPortn_Type()
)
rm10010AlmLineTxOtnOofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmLineTxOtnOofPortn.setStatus("current")
_Rm10010AlmLineTxOtnLofPortn_Type = EkiOnOff
_Rm10010AlmLineTxOtnLofPortn_Object = MibTableColumn
rm10010AlmLineTxOtnLofPortn = _Rm10010AlmLineTxOtnLofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 2, 184, 1, 17),
    _Rm10010AlmLineTxOtnLofPortn_Type()
)
rm10010AlmLineTxOtnLofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmLineTxOtnLofPortn.setStatus("current")
_Rm10010AlmLineCrit_ObjectIdentity = ObjectIdentity
rm10010AlmLineCrit = _Rm10010AlmLineCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 3)
)
_Rm10010AlmsynthAlmLineTable_Object = MibTable
rm10010AlmsynthAlmLineTable = _Rm10010AlmsynthAlmLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 3, 24)
)
if mibBuilder.loadTexts:
    rm10010AlmsynthAlmLineTable.setStatus("current")
_Rm10010AlmsynthAlmLineEntry_Object = MibTableRow
rm10010AlmsynthAlmLineEntry = _Rm10010AlmsynthAlmLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 3, 24, 1)
)
rm10010AlmsynthAlmLineEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010AlmsynthAlmLineIndex"),
)
if mibBuilder.loadTexts:
    rm10010AlmsynthAlmLineEntry.setStatus("current")


class _Rm10010AlmsynthAlmLineIndex_Type(Integer32):
    """Custom type rm10010AlmsynthAlmLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010AlmsynthAlmLineIndex_Type.__name__ = "Integer32"
_Rm10010AlmsynthAlmLineIndex_Object = MibTableColumn
rm10010AlmsynthAlmLineIndex = _Rm10010AlmsynthAlmLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 3, 24, 1, 1),
    _Rm10010AlmsynthAlmLineIndex_Type()
)
rm10010AlmsynthAlmLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmsynthAlmLineIndex.setStatus("current")
_Rm10010AlmXfpAbsentPortn_Type = EkiOnOff
_Rm10010AlmXfpAbsentPortn_Object = MibTableColumn
rm10010AlmXfpAbsentPortn = _Rm10010AlmXfpAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 3, 24, 1, 2),
    _Rm10010AlmXfpAbsentPortn_Type()
)
rm10010AlmXfpAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmXfpAbsentPortn.setStatus("current")
_Rm10010AlmXfpInitNotComplPortn_Type = EkiOnOff
_Rm10010AlmXfpInitNotComplPortn_Object = MibTableColumn
rm10010AlmXfpInitNotComplPortn = _Rm10010AlmXfpInitNotComplPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 3, 24, 1, 3),
    _Rm10010AlmXfpInitNotComplPortn_Type()
)
rm10010AlmXfpInitNotComplPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmXfpInitNotComplPortn.setStatus("current")
_Rm10010AlmLineHwFailPortn_Type = EkiOnOff
_Rm10010AlmLineHwFailPortn_Object = MibTableColumn
rm10010AlmLineHwFailPortn = _Rm10010AlmLineHwFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 3, 24, 1, 5),
    _Rm10010AlmLineHwFailPortn_Type()
)
rm10010AlmLineHwFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmLineHwFailPortn.setStatus("current")
_Rm10010AlmXfpTxOffPortn_Type = EkiOnOff
_Rm10010AlmXfpTxOffPortn_Object = MibTableColumn
rm10010AlmXfpTxOffPortn = _Rm10010AlmXfpTxOffPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 3, 24, 1, 6),
    _Rm10010AlmXfpTxOffPortn_Type()
)
rm10010AlmXfpTxOffPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmXfpTxOffPortn.setStatus("current")
_Rm10010AlmLineLocalOosPortn_Type = EkiOnOff
_Rm10010AlmLineLocalOosPortn_Object = MibTableColumn
rm10010AlmLineLocalOosPortn = _Rm10010AlmLineLocalOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 3, 24, 1, 7),
    _Rm10010AlmLineLocalOosPortn_Type()
)
rm10010AlmLineLocalOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmLineLocalOosPortn.setStatus("current")
_Rm10010AlmUpRdiInsPortn_Type = EkiOnOff
_Rm10010AlmUpRdiInsPortn_Object = MibTableColumn
rm10010AlmUpRdiInsPortn = _Rm10010AlmUpRdiInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 3, 24, 1, 9),
    _Rm10010AlmUpRdiInsPortn_Type()
)
rm10010AlmUpRdiInsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmUpRdiInsPortn.setStatus("current")
_Rm10010AlmLineDdmWarningPortn_Type = EkiOnOff
_Rm10010AlmLineDdmWarningPortn_Object = MibTableColumn
rm10010AlmLineDdmWarningPortn = _Rm10010AlmLineDdmWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 3, 24, 1, 10),
    _Rm10010AlmLineDdmWarningPortn_Type()
)
rm10010AlmLineDdmWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmLineDdmWarningPortn.setStatus("current")
_Rm10010AlmLineDdmAlmPortn_Type = EkiOnOff
_Rm10010AlmLineDdmAlmPortn_Object = MibTableColumn
rm10010AlmLineDdmAlmPortn = _Rm10010AlmLineDdmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 3, 24, 1, 11),
    _Rm10010AlmLineDdmAlmPortn_Type()
)
rm10010AlmLineDdmAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmLineDdmAlmPortn.setStatus("current")
_Rm10010AlmLineFailPortn_Type = EkiOnOff
_Rm10010AlmLineFailPortn_Object = MibTableColumn
rm10010AlmLineFailPortn = _Rm10010AlmLineFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 3, 24, 1, 13),
    _Rm10010AlmLineFailPortn_Type()
)
rm10010AlmLineFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmLineFailPortn.setStatus("current")
_Rm10010AlmLineActivePortn_Type = EkiOnOff
_Rm10010AlmLineActivePortn_Object = MibTableColumn
rm10010AlmLineActivePortn = _Rm10010AlmLineActivePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 2, 3, 3, 24, 1, 17),
    _Rm10010AlmLineActivePortn_Type()
)
rm10010AlmLineActivePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010AlmLineActivePortn.setStatus("current")
_Rm10010measures_ObjectIdentity = ObjectIdentity
rm10010measures = _Rm10010measures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3)
)
_Rm10010MesrOther_ObjectIdentity = ObjectIdentity
rm10010MesrOther = _Rm10010MesrOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 1)
)
_Rm10010Mesrsynth0_Type = EkiMeasureType
_Rm10010Mesrsynth0_Object = MibScalar
rm10010Mesrsynth0 = _Rm10010Mesrsynth0_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 1, 0),
    _Rm10010Mesrsynth0_Type()
)
rm10010Mesrsynth0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010Mesrsynth0.setStatus("deprecated")
_Rm10010Mesrsynth1_Type = EkiMeasureType
_Rm10010Mesrsynth1_Object = MibScalar
rm10010Mesrsynth1 = _Rm10010Mesrsynth1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 1, 1),
    _Rm10010Mesrsynth1_Type()
)
rm10010Mesrsynth1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010Mesrsynth1.setStatus("deprecated")


class _Rm10010MesrpmIntervalNumber_Type(Unsigned32):
    """Custom type rm10010MesrpmIntervalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010MesrpmIntervalNumber_Type.__name__ = "Unsigned32"
_Rm10010MesrpmIntervalNumber_Object = MibScalar
rm10010MesrpmIntervalNumber = _Rm10010MesrpmIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 1, 7),
    _Rm10010MesrpmIntervalNumber_Type()
)
rm10010MesrpmIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrpmIntervalNumber.setStatus("current")


class _Rm10010MesrlineNetTxLaserOutputPwrAverage_Type(Unsigned32):
    """Custom type rm10010MesrlineNetTxLaserOutputPwrAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010MesrlineNetTxLaserOutputPwrAverage_Type.__name__ = "Unsigned32"
_Rm10010MesrlineNetTxLaserOutputPwrAverage_Object = MibScalar
rm10010MesrlineNetTxLaserOutputPwrAverage = _Rm10010MesrlineNetTxLaserOutputPwrAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 1, 180),
    _Rm10010MesrlineNetTxLaserOutputPwrAverage_Type()
)
rm10010MesrlineNetTxLaserOutputPwrAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrlineNetTxLaserOutputPwrAverage.setStatus("current")


class _Rm10010MesrlineNetTxLaserTempAverage_Type(Unsigned32):
    """Custom type rm10010MesrlineNetTxLaserTempAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010MesrlineNetTxLaserTempAverage_Type.__name__ = "Unsigned32"
_Rm10010MesrlineNetTxLaserTempAverage_Object = MibScalar
rm10010MesrlineNetTxLaserTempAverage = _Rm10010MesrlineNetTxLaserTempAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 1, 181),
    _Rm10010MesrlineNetTxLaserTempAverage_Type()
)
rm10010MesrlineNetTxLaserTempAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrlineNetTxLaserTempAverage.setStatus("current")


class _Rm10010MesrlineNetTxBiasCurrentAverage_Type(Unsigned32):
    """Custom type rm10010MesrlineNetTxBiasCurrentAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010MesrlineNetTxBiasCurrentAverage_Type.__name__ = "Unsigned32"
_Rm10010MesrlineNetTxBiasCurrentAverage_Object = MibScalar
rm10010MesrlineNetTxBiasCurrentAverage = _Rm10010MesrlineNetTxBiasCurrentAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 1, 182),
    _Rm10010MesrlineNetTxBiasCurrentAverage_Type()
)
rm10010MesrlineNetTxBiasCurrentAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrlineNetTxBiasCurrentAverage.setStatus("current")


class _Rm10010MesrlineNetRxInputPwrAverage_Type(Unsigned32):
    """Custom type rm10010MesrlineNetRxInputPwrAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010MesrlineNetRxInputPwrAverage_Type.__name__ = "Unsigned32"
_Rm10010MesrlineNetRxInputPwrAverage_Object = MibScalar
rm10010MesrlineNetRxInputPwrAverage = _Rm10010MesrlineNetRxInputPwrAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 1, 183),
    _Rm10010MesrlineNetRxInputPwrAverage_Type()
)
rm10010MesrlineNetRxInputPwrAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrlineNetRxInputPwrAverage.setStatus("current")


class _Rm10010MesrlineResidualChromaticDispAverage_Type(Unsigned32):
    """Custom type rm10010MesrlineResidualChromaticDispAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010MesrlineResidualChromaticDispAverage_Type.__name__ = "Unsigned32"
_Rm10010MesrlineResidualChromaticDispAverage_Object = MibScalar
rm10010MesrlineResidualChromaticDispAverage = _Rm10010MesrlineResidualChromaticDispAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 1, 184),
    _Rm10010MesrlineResidualChromaticDispAverage_Type()
)
rm10010MesrlineResidualChromaticDispAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrlineResidualChromaticDispAverage.setStatus("current")


class _Rm10010MesrlineDiffGroupDelayAverage_Type(Unsigned32):
    """Custom type rm10010MesrlineDiffGroupDelayAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010MesrlineDiffGroupDelayAverage_Type.__name__ = "Unsigned32"
_Rm10010MesrlineDiffGroupDelayAverage_Object = MibScalar
rm10010MesrlineDiffGroupDelayAverage = _Rm10010MesrlineDiffGroupDelayAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 1, 185),
    _Rm10010MesrlineDiffGroupDelayAverage_Type()
)
rm10010MesrlineDiffGroupDelayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrlineDiffGroupDelayAverage.setStatus("current")


class _Rm10010MesrlineQFactorAverage_Type(Unsigned32):
    """Custom type rm10010MesrlineQFactorAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010MesrlineQFactorAverage_Type.__name__ = "Unsigned32"
_Rm10010MesrlineQFactorAverage_Object = MibScalar
rm10010MesrlineQFactorAverage = _Rm10010MesrlineQFactorAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 1, 186),
    _Rm10010MesrlineQFactorAverage_Type()
)
rm10010MesrlineQFactorAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrlineQFactorAverage.setStatus("current")


class _Rm10010MesrlineCarrierFreqOffsetAverage_Type(Unsigned32):
    """Custom type rm10010MesrlineCarrierFreqOffsetAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010MesrlineCarrierFreqOffsetAverage_Type.__name__ = "Unsigned32"
_Rm10010MesrlineCarrierFreqOffsetAverage_Object = MibScalar
rm10010MesrlineCarrierFreqOffsetAverage = _Rm10010MesrlineCarrierFreqOffsetAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 1, 187),
    _Rm10010MesrlineCarrierFreqOffsetAverage_Type()
)
rm10010MesrlineCarrierFreqOffsetAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrlineCarrierFreqOffsetAverage.setStatus("current")


class _Rm10010MesrlineOsnrAverage_Type(Unsigned32):
    """Custom type rm10010MesrlineOsnrAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010MesrlineOsnrAverage_Type.__name__ = "Unsigned32"
_Rm10010MesrlineOsnrAverage_Object = MibScalar
rm10010MesrlineOsnrAverage = _Rm10010MesrlineOsnrAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 1, 188),
    _Rm10010MesrlineOsnrAverage_Type()
)
rm10010MesrlineOsnrAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrlineOsnrAverage.setStatus("current")


class _Rm10010MesrclientNetTxTempMin_Type(Unsigned32):
    """Custom type rm10010MesrclientNetTxTempMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010MesrclientNetTxTempMin_Type.__name__ = "Unsigned32"
_Rm10010MesrclientNetTxTempMin_Object = MibScalar
rm10010MesrclientNetTxTempMin = _Rm10010MesrclientNetTxTempMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 1, 192),
    _Rm10010MesrclientNetTxTempMin_Type()
)
rm10010MesrclientNetTxTempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrclientNetTxTempMin.setStatus("current")


class _Rm10010MesrclientNetTxBiasMin_Type(Unsigned32):
    """Custom type rm10010MesrclientNetTxBiasMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010MesrclientNetTxBiasMin_Type.__name__ = "Unsigned32"
_Rm10010MesrclientNetTxBiasMin_Object = MibScalar
rm10010MesrclientNetTxBiasMin = _Rm10010MesrclientNetTxBiasMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 1, 193),
    _Rm10010MesrclientNetTxBiasMin_Type()
)
rm10010MesrclientNetTxBiasMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrclientNetTxBiasMin.setStatus("current")


class _Rm10010MesrclientNetTxPwrMin_Type(Unsigned32):
    """Custom type rm10010MesrclientNetTxPwrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010MesrclientNetTxPwrMin_Type.__name__ = "Unsigned32"
_Rm10010MesrclientNetTxPwrMin_Object = MibScalar
rm10010MesrclientNetTxPwrMin = _Rm10010MesrclientNetTxPwrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 1, 194),
    _Rm10010MesrclientNetTxPwrMin_Type()
)
rm10010MesrclientNetTxPwrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrclientNetTxPwrMin.setStatus("current")


class _Rm10010MesrclientNetRxPwrMin_Type(Unsigned32):
    """Custom type rm10010MesrclientNetRxPwrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010MesrclientNetRxPwrMin_Type.__name__ = "Unsigned32"
_Rm10010MesrclientNetRxPwrMin_Object = MibScalar
rm10010MesrclientNetRxPwrMin = _Rm10010MesrclientNetRxPwrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 1, 195),
    _Rm10010MesrclientNetRxPwrMin_Type()
)
rm10010MesrclientNetRxPwrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrclientNetRxPwrMin.setStatus("current")


class _Rm10010MesrlineNetTxLaserOutputPwrMin_Type(Unsigned32):
    """Custom type rm10010MesrlineNetTxLaserOutputPwrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010MesrlineNetTxLaserOutputPwrMin_Type.__name__ = "Unsigned32"
_Rm10010MesrlineNetTxLaserOutputPwrMin_Object = MibScalar
rm10010MesrlineNetTxLaserOutputPwrMin = _Rm10010MesrlineNetTxLaserOutputPwrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 1, 196),
    _Rm10010MesrlineNetTxLaserOutputPwrMin_Type()
)
rm10010MesrlineNetTxLaserOutputPwrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrlineNetTxLaserOutputPwrMin.setStatus("current")


class _Rm10010MesrlineNetTxLaserTempMin_Type(Unsigned32):
    """Custom type rm10010MesrlineNetTxLaserTempMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010MesrlineNetTxLaserTempMin_Type.__name__ = "Unsigned32"
_Rm10010MesrlineNetTxLaserTempMin_Object = MibScalar
rm10010MesrlineNetTxLaserTempMin = _Rm10010MesrlineNetTxLaserTempMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 1, 197),
    _Rm10010MesrlineNetTxLaserTempMin_Type()
)
rm10010MesrlineNetTxLaserTempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrlineNetTxLaserTempMin.setStatus("current")


class _Rm10010MesrlineNetTxBiasCurrentMin_Type(Unsigned32):
    """Custom type rm10010MesrlineNetTxBiasCurrentMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010MesrlineNetTxBiasCurrentMin_Type.__name__ = "Unsigned32"
_Rm10010MesrlineNetTxBiasCurrentMin_Object = MibScalar
rm10010MesrlineNetTxBiasCurrentMin = _Rm10010MesrlineNetTxBiasCurrentMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 1, 198),
    _Rm10010MesrlineNetTxBiasCurrentMin_Type()
)
rm10010MesrlineNetTxBiasCurrentMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrlineNetTxBiasCurrentMin.setStatus("current")


class _Rm10010MesrlineNetRxInputPwrMin_Type(Unsigned32):
    """Custom type rm10010MesrlineNetRxInputPwrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010MesrlineNetRxInputPwrMin_Type.__name__ = "Unsigned32"
_Rm10010MesrlineNetRxInputPwrMin_Object = MibScalar
rm10010MesrlineNetRxInputPwrMin = _Rm10010MesrlineNetRxInputPwrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 1, 199),
    _Rm10010MesrlineNetRxInputPwrMin_Type()
)
rm10010MesrlineNetRxInputPwrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrlineNetRxInputPwrMin.setStatus("current")


class _Rm10010MesrlineResidualChromaticDispMin_Type(Unsigned32):
    """Custom type rm10010MesrlineResidualChromaticDispMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010MesrlineResidualChromaticDispMin_Type.__name__ = "Unsigned32"
_Rm10010MesrlineResidualChromaticDispMin_Object = MibScalar
rm10010MesrlineResidualChromaticDispMin = _Rm10010MesrlineResidualChromaticDispMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 1, 200),
    _Rm10010MesrlineResidualChromaticDispMin_Type()
)
rm10010MesrlineResidualChromaticDispMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrlineResidualChromaticDispMin.setStatus("current")


class _Rm10010MesrlineDiffGroupDelayMin_Type(Unsigned32):
    """Custom type rm10010MesrlineDiffGroupDelayMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010MesrlineDiffGroupDelayMin_Type.__name__ = "Unsigned32"
_Rm10010MesrlineDiffGroupDelayMin_Object = MibScalar
rm10010MesrlineDiffGroupDelayMin = _Rm10010MesrlineDiffGroupDelayMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 1, 201),
    _Rm10010MesrlineDiffGroupDelayMin_Type()
)
rm10010MesrlineDiffGroupDelayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrlineDiffGroupDelayMin.setStatus("current")


class _Rm10010MesrlineQFactorMin_Type(Unsigned32):
    """Custom type rm10010MesrlineQFactorMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010MesrlineQFactorMin_Type.__name__ = "Unsigned32"
_Rm10010MesrlineQFactorMin_Object = MibScalar
rm10010MesrlineQFactorMin = _Rm10010MesrlineQFactorMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 1, 202),
    _Rm10010MesrlineQFactorMin_Type()
)
rm10010MesrlineQFactorMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrlineQFactorMin.setStatus("current")


class _Rm10010MesrlineCarrierFreqOffsetMin_Type(Unsigned32):
    """Custom type rm10010MesrlineCarrierFreqOffsetMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010MesrlineCarrierFreqOffsetMin_Type.__name__ = "Unsigned32"
_Rm10010MesrlineCarrierFreqOffsetMin_Object = MibScalar
rm10010MesrlineCarrierFreqOffsetMin = _Rm10010MesrlineCarrierFreqOffsetMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 1, 203),
    _Rm10010MesrlineCarrierFreqOffsetMin_Type()
)
rm10010MesrlineCarrierFreqOffsetMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrlineCarrierFreqOffsetMin.setStatus("current")


class _Rm10010MesrlineOsnrMin_Type(Unsigned32):
    """Custom type rm10010MesrlineOsnrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010MesrlineOsnrMin_Type.__name__ = "Unsigned32"
_Rm10010MesrlineOsnrMin_Object = MibScalar
rm10010MesrlineOsnrMin = _Rm10010MesrlineOsnrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 1, 204),
    _Rm10010MesrlineOsnrMin_Type()
)
rm10010MesrlineOsnrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrlineOsnrMin.setStatus("current")


class _Rm10010MesrclientNetTxTempMax_Type(Unsigned32):
    """Custom type rm10010MesrclientNetTxTempMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010MesrclientNetTxTempMax_Type.__name__ = "Unsigned32"
_Rm10010MesrclientNetTxTempMax_Object = MibScalar
rm10010MesrclientNetTxTempMax = _Rm10010MesrclientNetTxTempMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 1, 208),
    _Rm10010MesrclientNetTxTempMax_Type()
)
rm10010MesrclientNetTxTempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrclientNetTxTempMax.setStatus("current")


class _Rm10010MesrclientNetTxBiasMax_Type(Unsigned32):
    """Custom type rm10010MesrclientNetTxBiasMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010MesrclientNetTxBiasMax_Type.__name__ = "Unsigned32"
_Rm10010MesrclientNetTxBiasMax_Object = MibScalar
rm10010MesrclientNetTxBiasMax = _Rm10010MesrclientNetTxBiasMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 1, 209),
    _Rm10010MesrclientNetTxBiasMax_Type()
)
rm10010MesrclientNetTxBiasMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrclientNetTxBiasMax.setStatus("current")


class _Rm10010MesrclientNetTxPwrMax_Type(Unsigned32):
    """Custom type rm10010MesrclientNetTxPwrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010MesrclientNetTxPwrMax_Type.__name__ = "Unsigned32"
_Rm10010MesrclientNetTxPwrMax_Object = MibScalar
rm10010MesrclientNetTxPwrMax = _Rm10010MesrclientNetTxPwrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 1, 210),
    _Rm10010MesrclientNetTxPwrMax_Type()
)
rm10010MesrclientNetTxPwrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrclientNetTxPwrMax.setStatus("current")


class _Rm10010MesrclientNetRxPwrMax_Type(Unsigned32):
    """Custom type rm10010MesrclientNetRxPwrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010MesrclientNetRxPwrMax_Type.__name__ = "Unsigned32"
_Rm10010MesrclientNetRxPwrMax_Object = MibScalar
rm10010MesrclientNetRxPwrMax = _Rm10010MesrclientNetRxPwrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 1, 211),
    _Rm10010MesrclientNetRxPwrMax_Type()
)
rm10010MesrclientNetRxPwrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrclientNetRxPwrMax.setStatus("current")


class _Rm10010MesrlineNetTxLaserOutputPwrMax_Type(Unsigned32):
    """Custom type rm10010MesrlineNetTxLaserOutputPwrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010MesrlineNetTxLaserOutputPwrMax_Type.__name__ = "Unsigned32"
_Rm10010MesrlineNetTxLaserOutputPwrMax_Object = MibScalar
rm10010MesrlineNetTxLaserOutputPwrMax = _Rm10010MesrlineNetTxLaserOutputPwrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 1, 212),
    _Rm10010MesrlineNetTxLaserOutputPwrMax_Type()
)
rm10010MesrlineNetTxLaserOutputPwrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrlineNetTxLaserOutputPwrMax.setStatus("current")


class _Rm10010MesrlineNetTxLaserTempMax_Type(Unsigned32):
    """Custom type rm10010MesrlineNetTxLaserTempMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010MesrlineNetTxLaserTempMax_Type.__name__ = "Unsigned32"
_Rm10010MesrlineNetTxLaserTempMax_Object = MibScalar
rm10010MesrlineNetTxLaserTempMax = _Rm10010MesrlineNetTxLaserTempMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 1, 213),
    _Rm10010MesrlineNetTxLaserTempMax_Type()
)
rm10010MesrlineNetTxLaserTempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrlineNetTxLaserTempMax.setStatus("current")


class _Rm10010MesrlineNetTxBiasCurrentMax_Type(Unsigned32):
    """Custom type rm10010MesrlineNetTxBiasCurrentMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010MesrlineNetTxBiasCurrentMax_Type.__name__ = "Unsigned32"
_Rm10010MesrlineNetTxBiasCurrentMax_Object = MibScalar
rm10010MesrlineNetTxBiasCurrentMax = _Rm10010MesrlineNetTxBiasCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 1, 214),
    _Rm10010MesrlineNetTxBiasCurrentMax_Type()
)
rm10010MesrlineNetTxBiasCurrentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrlineNetTxBiasCurrentMax.setStatus("current")


class _Rm10010MesrlineNetRxInputPwrMax_Type(Unsigned32):
    """Custom type rm10010MesrlineNetRxInputPwrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010MesrlineNetRxInputPwrMax_Type.__name__ = "Unsigned32"
_Rm10010MesrlineNetRxInputPwrMax_Object = MibScalar
rm10010MesrlineNetRxInputPwrMax = _Rm10010MesrlineNetRxInputPwrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 1, 215),
    _Rm10010MesrlineNetRxInputPwrMax_Type()
)
rm10010MesrlineNetRxInputPwrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrlineNetRxInputPwrMax.setStatus("current")


class _Rm10010MesrlineResidualChromaticDispMax_Type(Unsigned32):
    """Custom type rm10010MesrlineResidualChromaticDispMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010MesrlineResidualChromaticDispMax_Type.__name__ = "Unsigned32"
_Rm10010MesrlineResidualChromaticDispMax_Object = MibScalar
rm10010MesrlineResidualChromaticDispMax = _Rm10010MesrlineResidualChromaticDispMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 1, 216),
    _Rm10010MesrlineResidualChromaticDispMax_Type()
)
rm10010MesrlineResidualChromaticDispMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrlineResidualChromaticDispMax.setStatus("current")


class _Rm10010MesrlineDiffGroupDelayMax_Type(Unsigned32):
    """Custom type rm10010MesrlineDiffGroupDelayMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010MesrlineDiffGroupDelayMax_Type.__name__ = "Unsigned32"
_Rm10010MesrlineDiffGroupDelayMax_Object = MibScalar
rm10010MesrlineDiffGroupDelayMax = _Rm10010MesrlineDiffGroupDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 1, 217),
    _Rm10010MesrlineDiffGroupDelayMax_Type()
)
rm10010MesrlineDiffGroupDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrlineDiffGroupDelayMax.setStatus("current")


class _Rm10010MesrlineQFactorMax_Type(Unsigned32):
    """Custom type rm10010MesrlineQFactorMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010MesrlineQFactorMax_Type.__name__ = "Unsigned32"
_Rm10010MesrlineQFactorMax_Object = MibScalar
rm10010MesrlineQFactorMax = _Rm10010MesrlineQFactorMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 1, 218),
    _Rm10010MesrlineQFactorMax_Type()
)
rm10010MesrlineQFactorMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrlineQFactorMax.setStatus("current")


class _Rm10010MesrlineCarrierFreqOffsetMax_Type(Unsigned32):
    """Custom type rm10010MesrlineCarrierFreqOffsetMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010MesrlineCarrierFreqOffsetMax_Type.__name__ = "Unsigned32"
_Rm10010MesrlineCarrierFreqOffsetMax_Object = MibScalar
rm10010MesrlineCarrierFreqOffsetMax = _Rm10010MesrlineCarrierFreqOffsetMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 1, 219),
    _Rm10010MesrlineCarrierFreqOffsetMax_Type()
)
rm10010MesrlineCarrierFreqOffsetMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrlineCarrierFreqOffsetMax.setStatus("current")


class _Rm10010MesrlineOsnrMax_Type(Unsigned32):
    """Custom type rm10010MesrlineOsnrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010MesrlineOsnrMax_Type.__name__ = "Unsigned32"
_Rm10010MesrlineOsnrMax_Object = MibScalar
rm10010MesrlineOsnrMax = _Rm10010MesrlineOsnrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 1, 220),
    _Rm10010MesrlineOsnrMax_Type()
)
rm10010MesrlineOsnrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrlineOsnrMax.setStatus("current")
_Rm10010MesrClient_ObjectIdentity = ObjectIdentity
rm10010MesrClient = _Rm10010MesrClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 2)
)


class _Rm10010MesrclientCfpTemp_Type(Unsigned32):
    """Custom type rm10010MesrclientCfpTemp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010MesrclientCfpTemp_Type.__name__ = "Unsigned32"
_Rm10010MesrclientCfpTemp_Object = MibScalar
rm10010MesrclientCfpTemp = _Rm10010MesrclientCfpTemp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 2, 8),
    _Rm10010MesrclientCfpTemp_Type()
)
rm10010MesrclientCfpTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrclientCfpTemp.setStatus("current")


class _Rm10010MesrclientCfp3v3Voltage_Type(Unsigned32):
    """Custom type rm10010MesrclientCfp3v3Voltage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010MesrclientCfp3v3Voltage_Type.__name__ = "Unsigned32"
_Rm10010MesrclientCfp3v3Voltage_Object = MibScalar
rm10010MesrclientCfp3v3Voltage = _Rm10010MesrclientCfp3v3Voltage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 2, 9),
    _Rm10010MesrclientCfp3v3Voltage_Type()
)
rm10010MesrclientCfp3v3Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrclientCfp3v3Voltage.setStatus("current")


class _Rm10010MesrclientSoaBiasCurrent_Type(Unsigned32):
    """Custom type rm10010MesrclientSoaBiasCurrent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010MesrclientSoaBiasCurrent_Type.__name__ = "Unsigned32"
_Rm10010MesrclientSoaBiasCurrent_Object = MibScalar
rm10010MesrclientSoaBiasCurrent = _Rm10010MesrclientSoaBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 2, 10),
    _Rm10010MesrclientSoaBiasCurrent_Type()
)
rm10010MesrclientSoaBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrclientSoaBiasCurrent.setStatus("current")
_Rm10010MesrclientNetTxTempTable_Object = MibTable
rm10010MesrclientNetTxTempTable = _Rm10010MesrclientNetTxTempTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 2, 16)
)
if mibBuilder.loadTexts:
    rm10010MesrclientNetTxTempTable.setStatus("current")
_Rm10010MesrclientNetTxTempEntry_Object = MibTableRow
rm10010MesrclientNetTxTempEntry = _Rm10010MesrclientNetTxTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 2, 16, 1)
)
rm10010MesrclientNetTxTempEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010MesrclientNetTxTempIndex"),
)
if mibBuilder.loadTexts:
    rm10010MesrclientNetTxTempEntry.setStatus("current")


class _Rm10010MesrclientNetTxTempIndex_Type(Integer32):
    """Custom type rm10010MesrclientNetTxTempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010MesrclientNetTxTempIndex_Type.__name__ = "Integer32"
_Rm10010MesrclientNetTxTempIndex_Object = MibTableColumn
rm10010MesrclientNetTxTempIndex = _Rm10010MesrclientNetTxTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 2, 16, 1, 1),
    _Rm10010MesrclientNetTxTempIndex_Type()
)
rm10010MesrclientNetTxTempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrclientNetTxTempIndex.setStatus("current")


class _Rm10010MesrclientNetTxTempPortn_Type(Integer32):
    """Custom type rm10010MesrclientNetTxTempPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010MesrclientNetTxTempPortn_Type.__name__ = "Integer32"
_Rm10010MesrclientNetTxTempPortn_Object = MibTableColumn
rm10010MesrclientNetTxTempPortn = _Rm10010MesrclientNetTxTempPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 2, 16, 1, 2),
    _Rm10010MesrclientNetTxTempPortn_Type()
)
rm10010MesrclientNetTxTempPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrclientNetTxTempPortn.setStatus("current")
_Rm10010MesrclientNetTxBiasTable_Object = MibTable
rm10010MesrclientNetTxBiasTable = _Rm10010MesrclientNetTxBiasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 2, 32)
)
if mibBuilder.loadTexts:
    rm10010MesrclientNetTxBiasTable.setStatus("current")
_Rm10010MesrclientNetTxBiasEntry_Object = MibTableRow
rm10010MesrclientNetTxBiasEntry = _Rm10010MesrclientNetTxBiasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 2, 32, 1)
)
rm10010MesrclientNetTxBiasEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010MesrclientNetTxBiasIndex"),
)
if mibBuilder.loadTexts:
    rm10010MesrclientNetTxBiasEntry.setStatus("current")


class _Rm10010MesrclientNetTxBiasIndex_Type(Integer32):
    """Custom type rm10010MesrclientNetTxBiasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010MesrclientNetTxBiasIndex_Type.__name__ = "Integer32"
_Rm10010MesrclientNetTxBiasIndex_Object = MibTableColumn
rm10010MesrclientNetTxBiasIndex = _Rm10010MesrclientNetTxBiasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 2, 32, 1, 1),
    _Rm10010MesrclientNetTxBiasIndex_Type()
)
rm10010MesrclientNetTxBiasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrclientNetTxBiasIndex.setStatus("current")


class _Rm10010MesrclientNetTxBiasPortn_Type(Integer32):
    """Custom type rm10010MesrclientNetTxBiasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010MesrclientNetTxBiasPortn_Type.__name__ = "Integer32"
_Rm10010MesrclientNetTxBiasPortn_Object = MibTableColumn
rm10010MesrclientNetTxBiasPortn = _Rm10010MesrclientNetTxBiasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 2, 32, 1, 2),
    _Rm10010MesrclientNetTxBiasPortn_Type()
)
rm10010MesrclientNetTxBiasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrclientNetTxBiasPortn.setStatus("current")
_Rm10010MesrclientNetTxPwrTable_Object = MibTable
rm10010MesrclientNetTxPwrTable = _Rm10010MesrclientNetTxPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 2, 48)
)
if mibBuilder.loadTexts:
    rm10010MesrclientNetTxPwrTable.setStatus("current")
_Rm10010MesrclientNetTxPwrEntry_Object = MibTableRow
rm10010MesrclientNetTxPwrEntry = _Rm10010MesrclientNetTxPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 2, 48, 1)
)
rm10010MesrclientNetTxPwrEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010MesrclientNetTxPwrIndex"),
)
if mibBuilder.loadTexts:
    rm10010MesrclientNetTxPwrEntry.setStatus("current")


class _Rm10010MesrclientNetTxPwrIndex_Type(Integer32):
    """Custom type rm10010MesrclientNetTxPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010MesrclientNetTxPwrIndex_Type.__name__ = "Integer32"
_Rm10010MesrclientNetTxPwrIndex_Object = MibTableColumn
rm10010MesrclientNetTxPwrIndex = _Rm10010MesrclientNetTxPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 2, 48, 1, 1),
    _Rm10010MesrclientNetTxPwrIndex_Type()
)
rm10010MesrclientNetTxPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrclientNetTxPwrIndex.setStatus("current")


class _Rm10010MesrclientNetTxPwrPortn_Type(Integer32):
    """Custom type rm10010MesrclientNetTxPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010MesrclientNetTxPwrPortn_Type.__name__ = "Integer32"
_Rm10010MesrclientNetTxPwrPortn_Object = MibTableColumn
rm10010MesrclientNetTxPwrPortn = _Rm10010MesrclientNetTxPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 2, 48, 1, 2),
    _Rm10010MesrclientNetTxPwrPortn_Type()
)
rm10010MesrclientNetTxPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrclientNetTxPwrPortn.setStatus("current")
_Rm10010MesrclientNetRxPwrTable_Object = MibTable
rm10010MesrclientNetRxPwrTable = _Rm10010MesrclientNetRxPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 2, 64)
)
if mibBuilder.loadTexts:
    rm10010MesrclientNetRxPwrTable.setStatus("current")
_Rm10010MesrclientNetRxPwrEntry_Object = MibTableRow
rm10010MesrclientNetRxPwrEntry = _Rm10010MesrclientNetRxPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 2, 64, 1)
)
rm10010MesrclientNetRxPwrEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010MesrclientNetRxPwrIndex"),
)
if mibBuilder.loadTexts:
    rm10010MesrclientNetRxPwrEntry.setStatus("current")


class _Rm10010MesrclientNetRxPwrIndex_Type(Integer32):
    """Custom type rm10010MesrclientNetRxPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010MesrclientNetRxPwrIndex_Type.__name__ = "Integer32"
_Rm10010MesrclientNetRxPwrIndex_Object = MibTableColumn
rm10010MesrclientNetRxPwrIndex = _Rm10010MesrclientNetRxPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 2, 64, 1, 1),
    _Rm10010MesrclientNetRxPwrIndex_Type()
)
rm10010MesrclientNetRxPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrclientNetRxPwrIndex.setStatus("current")


class _Rm10010MesrclientNetRxPwrPortn_Type(Integer32):
    """Custom type rm10010MesrclientNetRxPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010MesrclientNetRxPwrPortn_Type.__name__ = "Integer32"
_Rm10010MesrclientNetRxPwrPortn_Object = MibTableColumn
rm10010MesrclientNetRxPwrPortn = _Rm10010MesrclientNetRxPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 2, 64, 1, 2),
    _Rm10010MesrclientNetRxPwrPortn_Type()
)
rm10010MesrclientNetRxPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrclientNetRxPwrPortn.setStatus("current")
_Rm10010MesrLine_ObjectIdentity = ObjectIdentity
rm10010MesrLine = _Rm10010MesrLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 3)
)


class _Rm10010MesrlineMsaTemp_Type(Unsigned32):
    """Custom type rm10010MesrlineMsaTemp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010MesrlineMsaTemp_Type.__name__ = "Unsigned32"
_Rm10010MesrlineMsaTemp_Object = MibScalar
rm10010MesrlineMsaTemp = _Rm10010MesrlineMsaTemp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 3, 12),
    _Rm10010MesrlineMsaTemp_Type()
)
rm10010MesrlineMsaTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrlineMsaTemp.setStatus("current")


class _Rm10010MesrlineMsa3v3Voltage_Type(Unsigned32):
    """Custom type rm10010MesrlineMsa3v3Voltage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010MesrlineMsa3v3Voltage_Type.__name__ = "Unsigned32"
_Rm10010MesrlineMsa3v3Voltage_Object = MibScalar
rm10010MesrlineMsa3v3Voltage = _Rm10010MesrlineMsa3v3Voltage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 3, 13),
    _Rm10010MesrlineMsa3v3Voltage_Type()
)
rm10010MesrlineMsa3v3Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrlineMsa3v3Voltage.setStatus("current")


class _Rm10010MesrlineSoaBiasCurrent_Type(Unsigned32):
    """Custom type rm10010MesrlineSoaBiasCurrent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010MesrlineSoaBiasCurrent_Type.__name__ = "Unsigned32"
_Rm10010MesrlineSoaBiasCurrent_Object = MibScalar
rm10010MesrlineSoaBiasCurrent = _Rm10010MesrlineSoaBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 3, 14),
    _Rm10010MesrlineSoaBiasCurrent_Type()
)
rm10010MesrlineSoaBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrlineSoaBiasCurrent.setStatus("current")
_Rm10010MesrlineNetTxLaserOutputPwrTable_Object = MibTable
rm10010MesrlineNetTxLaserOutputPwrTable = _Rm10010MesrlineNetTxLaserOutputPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 3, 80)
)
if mibBuilder.loadTexts:
    rm10010MesrlineNetTxLaserOutputPwrTable.setStatus("current")
_Rm10010MesrlineNetTxLaserOutputPwrEntry_Object = MibTableRow
rm10010MesrlineNetTxLaserOutputPwrEntry = _Rm10010MesrlineNetTxLaserOutputPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 3, 80, 1)
)
rm10010MesrlineNetTxLaserOutputPwrEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010MesrlineNetTxLaserOutputPwrIndex"),
)
if mibBuilder.loadTexts:
    rm10010MesrlineNetTxLaserOutputPwrEntry.setStatus("current")


class _Rm10010MesrlineNetTxLaserOutputPwrIndex_Type(Integer32):
    """Custom type rm10010MesrlineNetTxLaserOutputPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010MesrlineNetTxLaserOutputPwrIndex_Type.__name__ = "Integer32"
_Rm10010MesrlineNetTxLaserOutputPwrIndex_Object = MibTableColumn
rm10010MesrlineNetTxLaserOutputPwrIndex = _Rm10010MesrlineNetTxLaserOutputPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 3, 80, 1, 1),
    _Rm10010MesrlineNetTxLaserOutputPwrIndex_Type()
)
rm10010MesrlineNetTxLaserOutputPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrlineNetTxLaserOutputPwrIndex.setStatus("current")


class _Rm10010MesrlineNetTxLaserOutputPwrPortn_Type(Integer32):
    """Custom type rm10010MesrlineNetTxLaserOutputPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010MesrlineNetTxLaserOutputPwrPortn_Type.__name__ = "Integer32"
_Rm10010MesrlineNetTxLaserOutputPwrPortn_Object = MibTableColumn
rm10010MesrlineNetTxLaserOutputPwrPortn = _Rm10010MesrlineNetTxLaserOutputPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 3, 80, 1, 2),
    _Rm10010MesrlineNetTxLaserOutputPwrPortn_Type()
)
rm10010MesrlineNetTxLaserOutputPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrlineNetTxLaserOutputPwrPortn.setStatus("current")
_Rm10010MesrlineNetTxLaserTempTable_Object = MibTable
rm10010MesrlineNetTxLaserTempTable = _Rm10010MesrlineNetTxLaserTempTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 3, 96)
)
if mibBuilder.loadTexts:
    rm10010MesrlineNetTxLaserTempTable.setStatus("current")
_Rm10010MesrlineNetTxLaserTempEntry_Object = MibTableRow
rm10010MesrlineNetTxLaserTempEntry = _Rm10010MesrlineNetTxLaserTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 3, 96, 1)
)
rm10010MesrlineNetTxLaserTempEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010MesrlineNetTxLaserTempIndex"),
)
if mibBuilder.loadTexts:
    rm10010MesrlineNetTxLaserTempEntry.setStatus("current")


class _Rm10010MesrlineNetTxLaserTempIndex_Type(Integer32):
    """Custom type rm10010MesrlineNetTxLaserTempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010MesrlineNetTxLaserTempIndex_Type.__name__ = "Integer32"
_Rm10010MesrlineNetTxLaserTempIndex_Object = MibTableColumn
rm10010MesrlineNetTxLaserTempIndex = _Rm10010MesrlineNetTxLaserTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 3, 96, 1, 1),
    _Rm10010MesrlineNetTxLaserTempIndex_Type()
)
rm10010MesrlineNetTxLaserTempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrlineNetTxLaserTempIndex.setStatus("current")


class _Rm10010MesrlineNetTxLaserTempPortn_Type(Integer32):
    """Custom type rm10010MesrlineNetTxLaserTempPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010MesrlineNetTxLaserTempPortn_Type.__name__ = "Integer32"
_Rm10010MesrlineNetTxLaserTempPortn_Object = MibTableColumn
rm10010MesrlineNetTxLaserTempPortn = _Rm10010MesrlineNetTxLaserTempPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 3, 96, 1, 2),
    _Rm10010MesrlineNetTxLaserTempPortn_Type()
)
rm10010MesrlineNetTxLaserTempPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrlineNetTxLaserTempPortn.setStatus("current")
_Rm10010MesrlineNetTxBiasCurrentTable_Object = MibTable
rm10010MesrlineNetTxBiasCurrentTable = _Rm10010MesrlineNetTxBiasCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 3, 112)
)
if mibBuilder.loadTexts:
    rm10010MesrlineNetTxBiasCurrentTable.setStatus("current")
_Rm10010MesrlineNetTxBiasCurrentEntry_Object = MibTableRow
rm10010MesrlineNetTxBiasCurrentEntry = _Rm10010MesrlineNetTxBiasCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 3, 112, 1)
)
rm10010MesrlineNetTxBiasCurrentEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010MesrlineNetTxBiasCurrentIndex"),
)
if mibBuilder.loadTexts:
    rm10010MesrlineNetTxBiasCurrentEntry.setStatus("current")


class _Rm10010MesrlineNetTxBiasCurrentIndex_Type(Integer32):
    """Custom type rm10010MesrlineNetTxBiasCurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010MesrlineNetTxBiasCurrentIndex_Type.__name__ = "Integer32"
_Rm10010MesrlineNetTxBiasCurrentIndex_Object = MibTableColumn
rm10010MesrlineNetTxBiasCurrentIndex = _Rm10010MesrlineNetTxBiasCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 3, 112, 1, 1),
    _Rm10010MesrlineNetTxBiasCurrentIndex_Type()
)
rm10010MesrlineNetTxBiasCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrlineNetTxBiasCurrentIndex.setStatus("current")


class _Rm10010MesrlineNetTxBiasCurrentPortn_Type(Integer32):
    """Custom type rm10010MesrlineNetTxBiasCurrentPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010MesrlineNetTxBiasCurrentPortn_Type.__name__ = "Integer32"
_Rm10010MesrlineNetTxBiasCurrentPortn_Object = MibTableColumn
rm10010MesrlineNetTxBiasCurrentPortn = _Rm10010MesrlineNetTxBiasCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 3, 112, 1, 2),
    _Rm10010MesrlineNetTxBiasCurrentPortn_Type()
)
rm10010MesrlineNetTxBiasCurrentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrlineNetTxBiasCurrentPortn.setStatus("current")
_Rm10010MesrlineNetRxInputPwrTable_Object = MibTable
rm10010MesrlineNetRxInputPwrTable = _Rm10010MesrlineNetRxInputPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 3, 128)
)
if mibBuilder.loadTexts:
    rm10010MesrlineNetRxInputPwrTable.setStatus("current")
_Rm10010MesrlineNetRxInputPwrEntry_Object = MibTableRow
rm10010MesrlineNetRxInputPwrEntry = _Rm10010MesrlineNetRxInputPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 3, 128, 1)
)
rm10010MesrlineNetRxInputPwrEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010MesrlineNetRxInputPwrIndex"),
)
if mibBuilder.loadTexts:
    rm10010MesrlineNetRxInputPwrEntry.setStatus("current")


class _Rm10010MesrlineNetRxInputPwrIndex_Type(Integer32):
    """Custom type rm10010MesrlineNetRxInputPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010MesrlineNetRxInputPwrIndex_Type.__name__ = "Integer32"
_Rm10010MesrlineNetRxInputPwrIndex_Object = MibTableColumn
rm10010MesrlineNetRxInputPwrIndex = _Rm10010MesrlineNetRxInputPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 3, 128, 1, 1),
    _Rm10010MesrlineNetRxInputPwrIndex_Type()
)
rm10010MesrlineNetRxInputPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrlineNetRxInputPwrIndex.setStatus("current")


class _Rm10010MesrlineNetRxInputPwrPortn_Type(Integer32):
    """Custom type rm10010MesrlineNetRxInputPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010MesrlineNetRxInputPwrPortn_Type.__name__ = "Integer32"
_Rm10010MesrlineNetRxInputPwrPortn_Object = MibTableColumn
rm10010MesrlineNetRxInputPwrPortn = _Rm10010MesrlineNetRxInputPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 3, 128, 1, 2),
    _Rm10010MesrlineNetRxInputPwrPortn_Type()
)
rm10010MesrlineNetRxInputPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrlineNetRxInputPwrPortn.setStatus("current")
_Rm10010MesrlineResidualChromaticDispTable_Object = MibTable
rm10010MesrlineResidualChromaticDispTable = _Rm10010MesrlineResidualChromaticDispTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 3, 144)
)
if mibBuilder.loadTexts:
    rm10010MesrlineResidualChromaticDispTable.setStatus("current")
_Rm10010MesrlineResidualChromaticDispEntry_Object = MibTableRow
rm10010MesrlineResidualChromaticDispEntry = _Rm10010MesrlineResidualChromaticDispEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 3, 144, 1)
)
rm10010MesrlineResidualChromaticDispEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010MesrlineResidualChromaticDispIndex"),
)
if mibBuilder.loadTexts:
    rm10010MesrlineResidualChromaticDispEntry.setStatus("current")


class _Rm10010MesrlineResidualChromaticDispIndex_Type(Integer32):
    """Custom type rm10010MesrlineResidualChromaticDispIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010MesrlineResidualChromaticDispIndex_Type.__name__ = "Integer32"
_Rm10010MesrlineResidualChromaticDispIndex_Object = MibTableColumn
rm10010MesrlineResidualChromaticDispIndex = _Rm10010MesrlineResidualChromaticDispIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 3, 144, 1, 1),
    _Rm10010MesrlineResidualChromaticDispIndex_Type()
)
rm10010MesrlineResidualChromaticDispIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrlineResidualChromaticDispIndex.setStatus("current")


class _Rm10010MesrlineResidualChromaticDispPortn_Type(Integer32):
    """Custom type rm10010MesrlineResidualChromaticDispPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010MesrlineResidualChromaticDispPortn_Type.__name__ = "Integer32"
_Rm10010MesrlineResidualChromaticDispPortn_Object = MibTableColumn
rm10010MesrlineResidualChromaticDispPortn = _Rm10010MesrlineResidualChromaticDispPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 3, 144, 1, 2),
    _Rm10010MesrlineResidualChromaticDispPortn_Type()
)
rm10010MesrlineResidualChromaticDispPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrlineResidualChromaticDispPortn.setStatus("current")
_Rm10010MesrlineDiffGroupDelayTable_Object = MibTable
rm10010MesrlineDiffGroupDelayTable = _Rm10010MesrlineDiffGroupDelayTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 3, 148)
)
if mibBuilder.loadTexts:
    rm10010MesrlineDiffGroupDelayTable.setStatus("current")
_Rm10010MesrlineDiffGroupDelayEntry_Object = MibTableRow
rm10010MesrlineDiffGroupDelayEntry = _Rm10010MesrlineDiffGroupDelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 3, 148, 1)
)
rm10010MesrlineDiffGroupDelayEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010MesrlineDiffGroupDelayIndex"),
)
if mibBuilder.loadTexts:
    rm10010MesrlineDiffGroupDelayEntry.setStatus("current")


class _Rm10010MesrlineDiffGroupDelayIndex_Type(Integer32):
    """Custom type rm10010MesrlineDiffGroupDelayIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010MesrlineDiffGroupDelayIndex_Type.__name__ = "Integer32"
_Rm10010MesrlineDiffGroupDelayIndex_Object = MibTableColumn
rm10010MesrlineDiffGroupDelayIndex = _Rm10010MesrlineDiffGroupDelayIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 3, 148, 1, 1),
    _Rm10010MesrlineDiffGroupDelayIndex_Type()
)
rm10010MesrlineDiffGroupDelayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrlineDiffGroupDelayIndex.setStatus("current")


class _Rm10010MesrlineDiffGroupDelayPortn_Type(Integer32):
    """Custom type rm10010MesrlineDiffGroupDelayPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010MesrlineDiffGroupDelayPortn_Type.__name__ = "Integer32"
_Rm10010MesrlineDiffGroupDelayPortn_Object = MibTableColumn
rm10010MesrlineDiffGroupDelayPortn = _Rm10010MesrlineDiffGroupDelayPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 3, 148, 1, 2),
    _Rm10010MesrlineDiffGroupDelayPortn_Type()
)
rm10010MesrlineDiffGroupDelayPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrlineDiffGroupDelayPortn.setStatus("current")
_Rm10010MesrlineQFactorTable_Object = MibTable
rm10010MesrlineQFactorTable = _Rm10010MesrlineQFactorTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 3, 152)
)
if mibBuilder.loadTexts:
    rm10010MesrlineQFactorTable.setStatus("current")
_Rm10010MesrlineQFactorEntry_Object = MibTableRow
rm10010MesrlineQFactorEntry = _Rm10010MesrlineQFactorEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 3, 152, 1)
)
rm10010MesrlineQFactorEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010MesrlineQFactorIndex"),
)
if mibBuilder.loadTexts:
    rm10010MesrlineQFactorEntry.setStatus("current")


class _Rm10010MesrlineQFactorIndex_Type(Integer32):
    """Custom type rm10010MesrlineQFactorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010MesrlineQFactorIndex_Type.__name__ = "Integer32"
_Rm10010MesrlineQFactorIndex_Object = MibTableColumn
rm10010MesrlineQFactorIndex = _Rm10010MesrlineQFactorIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 3, 152, 1, 1),
    _Rm10010MesrlineQFactorIndex_Type()
)
rm10010MesrlineQFactorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrlineQFactorIndex.setStatus("current")


class _Rm10010MesrlineQFactorPortn_Type(Integer32):
    """Custom type rm10010MesrlineQFactorPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010MesrlineQFactorPortn_Type.__name__ = "Integer32"
_Rm10010MesrlineQFactorPortn_Object = MibTableColumn
rm10010MesrlineQFactorPortn = _Rm10010MesrlineQFactorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 3, 152, 1, 2),
    _Rm10010MesrlineQFactorPortn_Type()
)
rm10010MesrlineQFactorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrlineQFactorPortn.setStatus("current")
_Rm10010MesrlineCarrierFreqOffsetTable_Object = MibTable
rm10010MesrlineCarrierFreqOffsetTable = _Rm10010MesrlineCarrierFreqOffsetTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 3, 156)
)
if mibBuilder.loadTexts:
    rm10010MesrlineCarrierFreqOffsetTable.setStatus("current")
_Rm10010MesrlineCarrierFreqOffsetEntry_Object = MibTableRow
rm10010MesrlineCarrierFreqOffsetEntry = _Rm10010MesrlineCarrierFreqOffsetEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 3, 156, 1)
)
rm10010MesrlineCarrierFreqOffsetEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010MesrlineCarrierFreqOffsetIndex"),
)
if mibBuilder.loadTexts:
    rm10010MesrlineCarrierFreqOffsetEntry.setStatus("current")


class _Rm10010MesrlineCarrierFreqOffsetIndex_Type(Integer32):
    """Custom type rm10010MesrlineCarrierFreqOffsetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010MesrlineCarrierFreqOffsetIndex_Type.__name__ = "Integer32"
_Rm10010MesrlineCarrierFreqOffsetIndex_Object = MibTableColumn
rm10010MesrlineCarrierFreqOffsetIndex = _Rm10010MesrlineCarrierFreqOffsetIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 3, 156, 1, 1),
    _Rm10010MesrlineCarrierFreqOffsetIndex_Type()
)
rm10010MesrlineCarrierFreqOffsetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrlineCarrierFreqOffsetIndex.setStatus("current")


class _Rm10010MesrlineCarrierFreqOffsetPortn_Type(Integer32):
    """Custom type rm10010MesrlineCarrierFreqOffsetPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010MesrlineCarrierFreqOffsetPortn_Type.__name__ = "Integer32"
_Rm10010MesrlineCarrierFreqOffsetPortn_Object = MibTableColumn
rm10010MesrlineCarrierFreqOffsetPortn = _Rm10010MesrlineCarrierFreqOffsetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 3, 156, 1, 2),
    _Rm10010MesrlineCarrierFreqOffsetPortn_Type()
)
rm10010MesrlineCarrierFreqOffsetPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrlineCarrierFreqOffsetPortn.setStatus("current")
_Rm10010MesrlineOsnrTable_Object = MibTable
rm10010MesrlineOsnrTable = _Rm10010MesrlineOsnrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 3, 160)
)
if mibBuilder.loadTexts:
    rm10010MesrlineOsnrTable.setStatus("current")
_Rm10010MesrlineOsnrEntry_Object = MibTableRow
rm10010MesrlineOsnrEntry = _Rm10010MesrlineOsnrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 3, 160, 1)
)
rm10010MesrlineOsnrEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010MesrlineOsnrIndex"),
)
if mibBuilder.loadTexts:
    rm10010MesrlineOsnrEntry.setStatus("current")


class _Rm10010MesrlineOsnrIndex_Type(Integer32):
    """Custom type rm10010MesrlineOsnrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010MesrlineOsnrIndex_Type.__name__ = "Integer32"
_Rm10010MesrlineOsnrIndex_Object = MibTableColumn
rm10010MesrlineOsnrIndex = _Rm10010MesrlineOsnrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 3, 160, 1, 1),
    _Rm10010MesrlineOsnrIndex_Type()
)
rm10010MesrlineOsnrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrlineOsnrIndex.setStatus("current")


class _Rm10010MesrlineOsnrPortn_Type(Integer32):
    """Custom type rm10010MesrlineOsnrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010MesrlineOsnrPortn_Type.__name__ = "Integer32"
_Rm10010MesrlineOsnrPortn_Object = MibTableColumn
rm10010MesrlineOsnrPortn = _Rm10010MesrlineOsnrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 3, 3, 160, 1, 2),
    _Rm10010MesrlineOsnrPortn_Type()
)
rm10010MesrlineOsnrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MesrlineOsnrPortn.setStatus("current")
_Rm10010counters_ObjectIdentity = ObjectIdentity
rm10010counters = _Rm10010counters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4)
)
_Rm10010CntOther_ObjectIdentity = ObjectIdentity
rm10010CntOther = _Rm10010CntOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4, 1)
)
_Rm10010CntClient_ObjectIdentity = ObjectIdentity
rm10010CntClient = _Rm10010CntClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4, 2)
)
_Rm10010CntclientInputErrorCounterLaneOneTable_Object = MibTable
rm10010CntclientInputErrorCounterLaneOneTable = _Rm10010CntclientInputErrorCounterLaneOneTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4, 2, 16)
)
if mibBuilder.loadTexts:
    rm10010CntclientInputErrorCounterLaneOneTable.setStatus("current")
_Rm10010CntclientInputErrorCounterLaneOneEntry_Object = MibTableRow
rm10010CntclientInputErrorCounterLaneOneEntry = _Rm10010CntclientInputErrorCounterLaneOneEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4, 2, 16, 1)
)
rm10010CntclientInputErrorCounterLaneOneEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010CntclientInputErrorCounterLaneOneIndex"),
)
if mibBuilder.loadTexts:
    rm10010CntclientInputErrorCounterLaneOneEntry.setStatus("current")


class _Rm10010CntclientInputErrorCounterLaneOneIndex_Type(Integer32):
    """Custom type rm10010CntclientInputErrorCounterLaneOneIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010CntclientInputErrorCounterLaneOneIndex_Type.__name__ = "Integer32"
_Rm10010CntclientInputErrorCounterLaneOneIndex_Object = MibTableColumn
rm10010CntclientInputErrorCounterLaneOneIndex = _Rm10010CntclientInputErrorCounterLaneOneIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4, 2, 16, 1, 1),
    _Rm10010CntclientInputErrorCounterLaneOneIndex_Type()
)
rm10010CntclientInputErrorCounterLaneOneIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CntclientInputErrorCounterLaneOneIndex.setStatus("current")
_Rm10010CntclientInputErrorCounterLaneOneValuePortn_Type = Counter32
_Rm10010CntclientInputErrorCounterLaneOneValuePortn_Object = MibTableColumn
rm10010CntclientInputErrorCounterLaneOneValuePortn = _Rm10010CntclientInputErrorCounterLaneOneValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4, 2, 16, 1, 2),
    _Rm10010CntclientInputErrorCounterLaneOneValuePortn_Type()
)
rm10010CntclientInputErrorCounterLaneOneValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CntclientInputErrorCounterLaneOneValuePortn.setStatus("current")
_Rm10010CntclientInputErrorCounterLaneOneErrorPortn_Type = EkiOnOff
_Rm10010CntclientInputErrorCounterLaneOneErrorPortn_Object = MibTableColumn
rm10010CntclientInputErrorCounterLaneOneErrorPortn = _Rm10010CntclientInputErrorCounterLaneOneErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4, 2, 16, 1, 3),
    _Rm10010CntclientInputErrorCounterLaneOneErrorPortn_Type()
)
rm10010CntclientInputErrorCounterLaneOneErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CntclientInputErrorCounterLaneOneErrorPortn.setStatus("current")
_Rm10010CntclientInputErrorCounterLaneOneOverloadPortn_Type = EkiOnOff
_Rm10010CntclientInputErrorCounterLaneOneOverloadPortn_Object = MibTableColumn
rm10010CntclientInputErrorCounterLaneOneOverloadPortn = _Rm10010CntclientInputErrorCounterLaneOneOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4, 2, 16, 1, 4),
    _Rm10010CntclientInputErrorCounterLaneOneOverloadPortn_Type()
)
rm10010CntclientInputErrorCounterLaneOneOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CntclientInputErrorCounterLaneOneOverloadPortn.setStatus("current")
_Rm10010CntclientInputErrorCounterLaneTwoTable_Object = MibTable
rm10010CntclientInputErrorCounterLaneTwoTable = _Rm10010CntclientInputErrorCounterLaneTwoTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4, 2, 32)
)
if mibBuilder.loadTexts:
    rm10010CntclientInputErrorCounterLaneTwoTable.setStatus("current")
_Rm10010CntclientInputErrorCounterLaneTwoEntry_Object = MibTableRow
rm10010CntclientInputErrorCounterLaneTwoEntry = _Rm10010CntclientInputErrorCounterLaneTwoEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4, 2, 32, 1)
)
rm10010CntclientInputErrorCounterLaneTwoEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010CntclientInputErrorCounterLaneTwoIndex"),
)
if mibBuilder.loadTexts:
    rm10010CntclientInputErrorCounterLaneTwoEntry.setStatus("current")


class _Rm10010CntclientInputErrorCounterLaneTwoIndex_Type(Integer32):
    """Custom type rm10010CntclientInputErrorCounterLaneTwoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010CntclientInputErrorCounterLaneTwoIndex_Type.__name__ = "Integer32"
_Rm10010CntclientInputErrorCounterLaneTwoIndex_Object = MibTableColumn
rm10010CntclientInputErrorCounterLaneTwoIndex = _Rm10010CntclientInputErrorCounterLaneTwoIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4, 2, 32, 1, 1),
    _Rm10010CntclientInputErrorCounterLaneTwoIndex_Type()
)
rm10010CntclientInputErrorCounterLaneTwoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CntclientInputErrorCounterLaneTwoIndex.setStatus("current")
_Rm10010CntclientInputErrorCounterLaneTwoValuePortn_Type = Counter32
_Rm10010CntclientInputErrorCounterLaneTwoValuePortn_Object = MibTableColumn
rm10010CntclientInputErrorCounterLaneTwoValuePortn = _Rm10010CntclientInputErrorCounterLaneTwoValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4, 2, 32, 1, 2),
    _Rm10010CntclientInputErrorCounterLaneTwoValuePortn_Type()
)
rm10010CntclientInputErrorCounterLaneTwoValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CntclientInputErrorCounterLaneTwoValuePortn.setStatus("current")
_Rm10010CntclientInputErrorCounterLaneTwoErrorPortn_Type = EkiOnOff
_Rm10010CntclientInputErrorCounterLaneTwoErrorPortn_Object = MibTableColumn
rm10010CntclientInputErrorCounterLaneTwoErrorPortn = _Rm10010CntclientInputErrorCounterLaneTwoErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4, 2, 32, 1, 3),
    _Rm10010CntclientInputErrorCounterLaneTwoErrorPortn_Type()
)
rm10010CntclientInputErrorCounterLaneTwoErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CntclientInputErrorCounterLaneTwoErrorPortn.setStatus("current")
_Rm10010CntclientInputErrorCounterLaneTwoOverloadPortn_Type = EkiOnOff
_Rm10010CntclientInputErrorCounterLaneTwoOverloadPortn_Object = MibTableColumn
rm10010CntclientInputErrorCounterLaneTwoOverloadPortn = _Rm10010CntclientInputErrorCounterLaneTwoOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4, 2, 32, 1, 4),
    _Rm10010CntclientInputErrorCounterLaneTwoOverloadPortn_Type()
)
rm10010CntclientInputErrorCounterLaneTwoOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CntclientInputErrorCounterLaneTwoOverloadPortn.setStatus("current")
_Rm10010CntclientInputErrorCounterTable_Object = MibTable
rm10010CntclientInputErrorCounterTable = _Rm10010CntclientInputErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4, 2, 80)
)
if mibBuilder.loadTexts:
    rm10010CntclientInputErrorCounterTable.setStatus("current")
_Rm10010CntclientInputErrorCounterEntry_Object = MibTableRow
rm10010CntclientInputErrorCounterEntry = _Rm10010CntclientInputErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4, 2, 80, 1)
)
rm10010CntclientInputErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010CntclientInputErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    rm10010CntclientInputErrorCounterEntry.setStatus("current")


class _Rm10010CntclientInputErrorCounterIndex_Type(Integer32):
    """Custom type rm10010CntclientInputErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010CntclientInputErrorCounterIndex_Type.__name__ = "Integer32"
_Rm10010CntclientInputErrorCounterIndex_Object = MibTableColumn
rm10010CntclientInputErrorCounterIndex = _Rm10010CntclientInputErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4, 2, 80, 1, 1),
    _Rm10010CntclientInputErrorCounterIndex_Type()
)
rm10010CntclientInputErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CntclientInputErrorCounterIndex.setStatus("current")
_Rm10010CntclientInputErrorCounterValuePortn_Type = Counter32
_Rm10010CntclientInputErrorCounterValuePortn_Object = MibTableColumn
rm10010CntclientInputErrorCounterValuePortn = _Rm10010CntclientInputErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4, 2, 80, 1, 2),
    _Rm10010CntclientInputErrorCounterValuePortn_Type()
)
rm10010CntclientInputErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CntclientInputErrorCounterValuePortn.setStatus("current")
_Rm10010CntclientInputErrorCounterErrorPortn_Type = EkiOnOff
_Rm10010CntclientInputErrorCounterErrorPortn_Object = MibTableColumn
rm10010CntclientInputErrorCounterErrorPortn = _Rm10010CntclientInputErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4, 2, 80, 1, 3),
    _Rm10010CntclientInputErrorCounterErrorPortn_Type()
)
rm10010CntclientInputErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CntclientInputErrorCounterErrorPortn.setStatus("current")
_Rm10010CntclientInputErrorCounterOverloadPortn_Type = EkiOnOff
_Rm10010CntclientInputErrorCounterOverloadPortn_Object = MibTableColumn
rm10010CntclientInputErrorCounterOverloadPortn = _Rm10010CntclientInputErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4, 2, 80, 1, 4),
    _Rm10010CntclientInputErrorCounterOverloadPortn_Type()
)
rm10010CntclientInputErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CntclientInputErrorCounterOverloadPortn.setStatus("current")
_Rm10010CntclientCbipCounterTable_Object = MibTable
rm10010CntclientCbipCounterTable = _Rm10010CntclientCbipCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4, 2, 96)
)
if mibBuilder.loadTexts:
    rm10010CntclientCbipCounterTable.setStatus("current")
_Rm10010CntclientCbipCounterEntry_Object = MibTableRow
rm10010CntclientCbipCounterEntry = _Rm10010CntclientCbipCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4, 2, 96, 1)
)
rm10010CntclientCbipCounterEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010CntclientCbipCounterIndex"),
)
if mibBuilder.loadTexts:
    rm10010CntclientCbipCounterEntry.setStatus("current")


class _Rm10010CntclientCbipCounterIndex_Type(Integer32):
    """Custom type rm10010CntclientCbipCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010CntclientCbipCounterIndex_Type.__name__ = "Integer32"
_Rm10010CntclientCbipCounterIndex_Object = MibTableColumn
rm10010CntclientCbipCounterIndex = _Rm10010CntclientCbipCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4, 2, 96, 1, 1),
    _Rm10010CntclientCbipCounterIndex_Type()
)
rm10010CntclientCbipCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CntclientCbipCounterIndex.setStatus("current")
_Rm10010CntclientCbipCounterValuePortn_Type = Counter32
_Rm10010CntclientCbipCounterValuePortn_Object = MibTableColumn
rm10010CntclientCbipCounterValuePortn = _Rm10010CntclientCbipCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4, 2, 96, 1, 2),
    _Rm10010CntclientCbipCounterValuePortn_Type()
)
rm10010CntclientCbipCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CntclientCbipCounterValuePortn.setStatus("current")
_Rm10010CntclientCbipCounterErrorPortn_Type = EkiOnOff
_Rm10010CntclientCbipCounterErrorPortn_Object = MibTableColumn
rm10010CntclientCbipCounterErrorPortn = _Rm10010CntclientCbipCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4, 2, 96, 1, 3),
    _Rm10010CntclientCbipCounterErrorPortn_Type()
)
rm10010CntclientCbipCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CntclientCbipCounterErrorPortn.setStatus("current")
_Rm10010CntclientCbipCounterOverloadPortn_Type = EkiOnOff
_Rm10010CntclientCbipCounterOverloadPortn_Object = MibTableColumn
rm10010CntclientCbipCounterOverloadPortn = _Rm10010CntclientCbipCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4, 2, 96, 1, 4),
    _Rm10010CntclientCbipCounterOverloadPortn_Type()
)
rm10010CntclientCbipCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CntclientCbipCounterOverloadPortn.setStatus("current")
_Rm10010CntLine_ObjectIdentity = ObjectIdentity
rm10010CntLine = _Rm10010CntLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4, 3)
)
_Rm10010CntlocalLineSmBip8ErrorCounterTable_Object = MibTable
rm10010CntlocalLineSmBip8ErrorCounterTable = _Rm10010CntlocalLineSmBip8ErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4, 3, 192)
)
if mibBuilder.loadTexts:
    rm10010CntlocalLineSmBip8ErrorCounterTable.setStatus("current")
_Rm10010CntlocalLineSmBip8ErrorCounterEntry_Object = MibTableRow
rm10010CntlocalLineSmBip8ErrorCounterEntry = _Rm10010CntlocalLineSmBip8ErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4, 3, 192, 1)
)
rm10010CntlocalLineSmBip8ErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010CntlocalLineSmBip8ErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    rm10010CntlocalLineSmBip8ErrorCounterEntry.setStatus("current")


class _Rm10010CntlocalLineSmBip8ErrorCounterIndex_Type(Integer32):
    """Custom type rm10010CntlocalLineSmBip8ErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010CntlocalLineSmBip8ErrorCounterIndex_Type.__name__ = "Integer32"
_Rm10010CntlocalLineSmBip8ErrorCounterIndex_Object = MibTableColumn
rm10010CntlocalLineSmBip8ErrorCounterIndex = _Rm10010CntlocalLineSmBip8ErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4, 3, 192, 1, 1),
    _Rm10010CntlocalLineSmBip8ErrorCounterIndex_Type()
)
rm10010CntlocalLineSmBip8ErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CntlocalLineSmBip8ErrorCounterIndex.setStatus("current")
_Rm10010CntlocalLineSmBip8ErrorCounterValuePortn_Type = Counter64
_Rm10010CntlocalLineSmBip8ErrorCounterValuePortn_Object = MibTableColumn
rm10010CntlocalLineSmBip8ErrorCounterValuePortn = _Rm10010CntlocalLineSmBip8ErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4, 3, 192, 1, 2),
    _Rm10010CntlocalLineSmBip8ErrorCounterValuePortn_Type()
)
rm10010CntlocalLineSmBip8ErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CntlocalLineSmBip8ErrorCounterValuePortn.setStatus("current")
_Rm10010CntlocalLineSmBip8ErrorCounterErrorPortn_Type = EkiOnOff
_Rm10010CntlocalLineSmBip8ErrorCounterErrorPortn_Object = MibTableColumn
rm10010CntlocalLineSmBip8ErrorCounterErrorPortn = _Rm10010CntlocalLineSmBip8ErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4, 3, 192, 1, 3),
    _Rm10010CntlocalLineSmBip8ErrorCounterErrorPortn_Type()
)
rm10010CntlocalLineSmBip8ErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CntlocalLineSmBip8ErrorCounterErrorPortn.setStatus("current")
_Rm10010CntlocalLineSmBip8ErrorCounterOverloadPortn_Type = EkiOnOff
_Rm10010CntlocalLineSmBip8ErrorCounterOverloadPortn_Object = MibTableColumn
rm10010CntlocalLineSmBip8ErrorCounterOverloadPortn = _Rm10010CntlocalLineSmBip8ErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4, 3, 192, 1, 4),
    _Rm10010CntlocalLineSmBip8ErrorCounterOverloadPortn_Type()
)
rm10010CntlocalLineSmBip8ErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CntlocalLineSmBip8ErrorCounterOverloadPortn.setStatus("current")
_Rm10010CntlocalLineFecCorrectedErrorsCounterTable_Object = MibTable
rm10010CntlocalLineFecCorrectedErrorsCounterTable = _Rm10010CntlocalLineFecCorrectedErrorsCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4, 3, 193)
)
if mibBuilder.loadTexts:
    rm10010CntlocalLineFecCorrectedErrorsCounterTable.setStatus("current")
_Rm10010CntlocalLineFecCorrectedErrorsCounterEntry_Object = MibTableRow
rm10010CntlocalLineFecCorrectedErrorsCounterEntry = _Rm10010CntlocalLineFecCorrectedErrorsCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4, 3, 193, 1)
)
rm10010CntlocalLineFecCorrectedErrorsCounterEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010CntlocalLineFecCorrectedErrorsCounterIndex"),
)
if mibBuilder.loadTexts:
    rm10010CntlocalLineFecCorrectedErrorsCounterEntry.setStatus("current")


class _Rm10010CntlocalLineFecCorrectedErrorsCounterIndex_Type(Integer32):
    """Custom type rm10010CntlocalLineFecCorrectedErrorsCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010CntlocalLineFecCorrectedErrorsCounterIndex_Type.__name__ = "Integer32"
_Rm10010CntlocalLineFecCorrectedErrorsCounterIndex_Object = MibTableColumn
rm10010CntlocalLineFecCorrectedErrorsCounterIndex = _Rm10010CntlocalLineFecCorrectedErrorsCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4, 3, 193, 1, 1),
    _Rm10010CntlocalLineFecCorrectedErrorsCounterIndex_Type()
)
rm10010CntlocalLineFecCorrectedErrorsCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CntlocalLineFecCorrectedErrorsCounterIndex.setStatus("current")
_Rm10010CntlocalLineFecCorrectedErrorsCounterValuePortn_Type = Counter64
_Rm10010CntlocalLineFecCorrectedErrorsCounterValuePortn_Object = MibTableColumn
rm10010CntlocalLineFecCorrectedErrorsCounterValuePortn = _Rm10010CntlocalLineFecCorrectedErrorsCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4, 3, 193, 1, 2),
    _Rm10010CntlocalLineFecCorrectedErrorsCounterValuePortn_Type()
)
rm10010CntlocalLineFecCorrectedErrorsCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CntlocalLineFecCorrectedErrorsCounterValuePortn.setStatus("current")
_Rm10010CntlocalLineFecCorrectedErrorsCounterErrorPortn_Type = EkiOnOff
_Rm10010CntlocalLineFecCorrectedErrorsCounterErrorPortn_Object = MibTableColumn
rm10010CntlocalLineFecCorrectedErrorsCounterErrorPortn = _Rm10010CntlocalLineFecCorrectedErrorsCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4, 3, 193, 1, 3),
    _Rm10010CntlocalLineFecCorrectedErrorsCounterErrorPortn_Type()
)
rm10010CntlocalLineFecCorrectedErrorsCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CntlocalLineFecCorrectedErrorsCounterErrorPortn.setStatus("current")
_Rm10010CntlocalLineFecCorrectedErrorsCounterOverloadPortn_Type = EkiOnOff
_Rm10010CntlocalLineFecCorrectedErrorsCounterOverloadPortn_Object = MibTableColumn
rm10010CntlocalLineFecCorrectedErrorsCounterOverloadPortn = _Rm10010CntlocalLineFecCorrectedErrorsCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4, 3, 193, 1, 4),
    _Rm10010CntlocalLineFecCorrectedErrorsCounterOverloadPortn_Type()
)
rm10010CntlocalLineFecCorrectedErrorsCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CntlocalLineFecCorrectedErrorsCounterOverloadPortn.setStatus("current")
_Rm10010CntremoteLineSmBip8ErrorCounterTable_Object = MibTable
rm10010CntremoteLineSmBip8ErrorCounterTable = _Rm10010CntremoteLineSmBip8ErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4, 3, 194)
)
if mibBuilder.loadTexts:
    rm10010CntremoteLineSmBip8ErrorCounterTable.setStatus("current")
_Rm10010CntremoteLineSmBip8ErrorCounterEntry_Object = MibTableRow
rm10010CntremoteLineSmBip8ErrorCounterEntry = _Rm10010CntremoteLineSmBip8ErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4, 3, 194, 1)
)
rm10010CntremoteLineSmBip8ErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010CntremoteLineSmBip8ErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    rm10010CntremoteLineSmBip8ErrorCounterEntry.setStatus("current")


class _Rm10010CntremoteLineSmBip8ErrorCounterIndex_Type(Integer32):
    """Custom type rm10010CntremoteLineSmBip8ErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010CntremoteLineSmBip8ErrorCounterIndex_Type.__name__ = "Integer32"
_Rm10010CntremoteLineSmBip8ErrorCounterIndex_Object = MibTableColumn
rm10010CntremoteLineSmBip8ErrorCounterIndex = _Rm10010CntremoteLineSmBip8ErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4, 3, 194, 1, 1),
    _Rm10010CntremoteLineSmBip8ErrorCounterIndex_Type()
)
rm10010CntremoteLineSmBip8ErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CntremoteLineSmBip8ErrorCounterIndex.setStatus("current")
_Rm10010CntremoteLineSmBip8ErrorCounterValuePortn_Type = Counter64
_Rm10010CntremoteLineSmBip8ErrorCounterValuePortn_Object = MibTableColumn
rm10010CntremoteLineSmBip8ErrorCounterValuePortn = _Rm10010CntremoteLineSmBip8ErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4, 3, 194, 1, 2),
    _Rm10010CntremoteLineSmBip8ErrorCounterValuePortn_Type()
)
rm10010CntremoteLineSmBip8ErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CntremoteLineSmBip8ErrorCounterValuePortn.setStatus("current")
_Rm10010CntremoteLineSmBip8ErrorCounterErrorPortn_Type = EkiOnOff
_Rm10010CntremoteLineSmBip8ErrorCounterErrorPortn_Object = MibTableColumn
rm10010CntremoteLineSmBip8ErrorCounterErrorPortn = _Rm10010CntremoteLineSmBip8ErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4, 3, 194, 1, 3),
    _Rm10010CntremoteLineSmBip8ErrorCounterErrorPortn_Type()
)
rm10010CntremoteLineSmBip8ErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CntremoteLineSmBip8ErrorCounterErrorPortn.setStatus("current")
_Rm10010CntremoteLineSmBip8ErrorCounterOverloadPortn_Type = EkiOnOff
_Rm10010CntremoteLineSmBip8ErrorCounterOverloadPortn_Object = MibTableColumn
rm10010CntremoteLineSmBip8ErrorCounterOverloadPortn = _Rm10010CntremoteLineSmBip8ErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4, 3, 194, 1, 4),
    _Rm10010CntremoteLineSmBip8ErrorCounterOverloadPortn_Type()
)
rm10010CntremoteLineSmBip8ErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CntremoteLineSmBip8ErrorCounterOverloadPortn.setStatus("current")
_Rm10010CntlineDfrmTimCntTable_Object = MibTable
rm10010CntlineDfrmTimCntTable = _Rm10010CntlineDfrmTimCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4, 3, 195)
)
if mibBuilder.loadTexts:
    rm10010CntlineDfrmTimCntTable.setStatus("current")
_Rm10010CntlineDfrmTimCntEntry_Object = MibTableRow
rm10010CntlineDfrmTimCntEntry = _Rm10010CntlineDfrmTimCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4, 3, 195, 1)
)
rm10010CntlineDfrmTimCntEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010CntlineDfrmTimCntIndex"),
)
if mibBuilder.loadTexts:
    rm10010CntlineDfrmTimCntEntry.setStatus("current")


class _Rm10010CntlineDfrmTimCntIndex_Type(Integer32):
    """Custom type rm10010CntlineDfrmTimCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010CntlineDfrmTimCntIndex_Type.__name__ = "Integer32"
_Rm10010CntlineDfrmTimCntIndex_Object = MibTableColumn
rm10010CntlineDfrmTimCntIndex = _Rm10010CntlineDfrmTimCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4, 3, 195, 1, 1),
    _Rm10010CntlineDfrmTimCntIndex_Type()
)
rm10010CntlineDfrmTimCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CntlineDfrmTimCntIndex.setStatus("current")
_Rm10010CntlineDfrmTimCntValuePortn_Type = Counter64
_Rm10010CntlineDfrmTimCntValuePortn_Object = MibTableColumn
rm10010CntlineDfrmTimCntValuePortn = _Rm10010CntlineDfrmTimCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4, 3, 195, 1, 2),
    _Rm10010CntlineDfrmTimCntValuePortn_Type()
)
rm10010CntlineDfrmTimCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CntlineDfrmTimCntValuePortn.setStatus("current")
_Rm10010CntlineDfrmTimCntErrorPortn_Type = EkiOnOff
_Rm10010CntlineDfrmTimCntErrorPortn_Object = MibTableColumn
rm10010CntlineDfrmTimCntErrorPortn = _Rm10010CntlineDfrmTimCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4, 3, 195, 1, 3),
    _Rm10010CntlineDfrmTimCntErrorPortn_Type()
)
rm10010CntlineDfrmTimCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CntlineDfrmTimCntErrorPortn.setStatus("current")
_Rm10010CntlineDfrmTimCntOverloadPortn_Type = EkiOnOff
_Rm10010CntlineDfrmTimCntOverloadPortn_Object = MibTableColumn
rm10010CntlineDfrmTimCntOverloadPortn = _Rm10010CntlineDfrmTimCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4, 3, 195, 1, 4),
    _Rm10010CntlineDfrmTimCntOverloadPortn_Type()
)
rm10010CntlineDfrmTimCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CntlineDfrmTimCntOverloadPortn.setStatus("current")
_Rm10010CntlocalLineTrscvFecCorrectedErrorCounterTable_Object = MibTable
rm10010CntlocalLineTrscvFecCorrectedErrorCounterTable = _Rm10010CntlocalLineTrscvFecCorrectedErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4, 3, 196)
)
if mibBuilder.loadTexts:
    rm10010CntlocalLineTrscvFecCorrectedErrorCounterTable.setStatus("current")
_Rm10010CntlocalLineTrscvFecCorrectedErrorCounterEntry_Object = MibTableRow
rm10010CntlocalLineTrscvFecCorrectedErrorCounterEntry = _Rm10010CntlocalLineTrscvFecCorrectedErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4, 3, 196, 1)
)
rm10010CntlocalLineTrscvFecCorrectedErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010CntlocalLineTrscvFecCorrectedErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    rm10010CntlocalLineTrscvFecCorrectedErrorCounterEntry.setStatus("current")


class _Rm10010CntlocalLineTrscvFecCorrectedErrorCounterIndex_Type(Integer32):
    """Custom type rm10010CntlocalLineTrscvFecCorrectedErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010CntlocalLineTrscvFecCorrectedErrorCounterIndex_Type.__name__ = "Integer32"
_Rm10010CntlocalLineTrscvFecCorrectedErrorCounterIndex_Object = MibTableColumn
rm10010CntlocalLineTrscvFecCorrectedErrorCounterIndex = _Rm10010CntlocalLineTrscvFecCorrectedErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4, 3, 196, 1, 1),
    _Rm10010CntlocalLineTrscvFecCorrectedErrorCounterIndex_Type()
)
rm10010CntlocalLineTrscvFecCorrectedErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CntlocalLineTrscvFecCorrectedErrorCounterIndex.setStatus("current")
_Rm10010CntlocalLineTrscvFecCorrectedErrorCounterValuePortn_Type = Counter64
_Rm10010CntlocalLineTrscvFecCorrectedErrorCounterValuePortn_Object = MibTableColumn
rm10010CntlocalLineTrscvFecCorrectedErrorCounterValuePortn = _Rm10010CntlocalLineTrscvFecCorrectedErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4, 3, 196, 1, 2),
    _Rm10010CntlocalLineTrscvFecCorrectedErrorCounterValuePortn_Type()
)
rm10010CntlocalLineTrscvFecCorrectedErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CntlocalLineTrscvFecCorrectedErrorCounterValuePortn.setStatus("current")
_Rm10010CntlocalLineTrscvFecCorrectedErrorCounterErrorPortn_Type = EkiOnOff
_Rm10010CntlocalLineTrscvFecCorrectedErrorCounterErrorPortn_Object = MibTableColumn
rm10010CntlocalLineTrscvFecCorrectedErrorCounterErrorPortn = _Rm10010CntlocalLineTrscvFecCorrectedErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4, 3, 196, 1, 3),
    _Rm10010CntlocalLineTrscvFecCorrectedErrorCounterErrorPortn_Type()
)
rm10010CntlocalLineTrscvFecCorrectedErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CntlocalLineTrscvFecCorrectedErrorCounterErrorPortn.setStatus("current")
_Rm10010CntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn_Type = EkiOnOff
_Rm10010CntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn_Object = MibTableColumn
rm10010CntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn = _Rm10010CntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4, 3, 196, 1, 4),
    _Rm10010CntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn_Type()
)
rm10010CntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn.setStatus("current")
_Rm10010CntlocalLineTrscvFecUncorrectedErrorCounterTable_Object = MibTable
rm10010CntlocalLineTrscvFecUncorrectedErrorCounterTable = _Rm10010CntlocalLineTrscvFecUncorrectedErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4, 3, 197)
)
if mibBuilder.loadTexts:
    rm10010CntlocalLineTrscvFecUncorrectedErrorCounterTable.setStatus("current")
_Rm10010CntlocalLineTrscvFecUncorrectedErrorCounterEntry_Object = MibTableRow
rm10010CntlocalLineTrscvFecUncorrectedErrorCounterEntry = _Rm10010CntlocalLineTrscvFecUncorrectedErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4, 3, 197, 1)
)
rm10010CntlocalLineTrscvFecUncorrectedErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010CntlocalLineTrscvFecUncorrectedErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    rm10010CntlocalLineTrscvFecUncorrectedErrorCounterEntry.setStatus("current")


class _Rm10010CntlocalLineTrscvFecUncorrectedErrorCounterIndex_Type(Integer32):
    """Custom type rm10010CntlocalLineTrscvFecUncorrectedErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010CntlocalLineTrscvFecUncorrectedErrorCounterIndex_Type.__name__ = "Integer32"
_Rm10010CntlocalLineTrscvFecUncorrectedErrorCounterIndex_Object = MibTableColumn
rm10010CntlocalLineTrscvFecUncorrectedErrorCounterIndex = _Rm10010CntlocalLineTrscvFecUncorrectedErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4, 3, 197, 1, 1),
    _Rm10010CntlocalLineTrscvFecUncorrectedErrorCounterIndex_Type()
)
rm10010CntlocalLineTrscvFecUncorrectedErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CntlocalLineTrscvFecUncorrectedErrorCounterIndex.setStatus("current")
_Rm10010CntlocalLineTrscvFecUncorrectedErrorCounterValuePortn_Type = Counter64
_Rm10010CntlocalLineTrscvFecUncorrectedErrorCounterValuePortn_Object = MibTableColumn
rm10010CntlocalLineTrscvFecUncorrectedErrorCounterValuePortn = _Rm10010CntlocalLineTrscvFecUncorrectedErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4, 3, 197, 1, 2),
    _Rm10010CntlocalLineTrscvFecUncorrectedErrorCounterValuePortn_Type()
)
rm10010CntlocalLineTrscvFecUncorrectedErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CntlocalLineTrscvFecUncorrectedErrorCounterValuePortn.setStatus("current")
_Rm10010CntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn_Type = EkiOnOff
_Rm10010CntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn_Object = MibTableColumn
rm10010CntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn = _Rm10010CntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4, 3, 197, 1, 3),
    _Rm10010CntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn_Type()
)
rm10010CntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn.setStatus("current")
_Rm10010CntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn_Type = EkiOnOff
_Rm10010CntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn_Object = MibTableColumn
rm10010CntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn = _Rm10010CntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 4, 3, 197, 1, 4),
    _Rm10010CntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn_Type()
)
rm10010CntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn.setStatus("current")
_Rm10010controlsWrite_ObjectIdentity = ObjectIdentity
rm10010controlsWrite = _Rm10010controlsWrite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6)
)
_Rm10010CtrlOther_ObjectIdentity = ObjectIdentity
rm10010CtrlOther = _Rm10010CtrlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 1)
)
_Rm10010CtrlconfMgnt1_ObjectIdentity = ObjectIdentity
rm10010CtrlconfMgnt1 = _Rm10010CtrlconfMgnt1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 1, 1)
)
_Rm10010CtrlConf1Load1_Type = EkiOnOff
_Rm10010CtrlConf1Load1_Object = MibScalar
rm10010CtrlConf1Load1 = _Rm10010CtrlConf1Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 1, 1, 1),
    _Rm10010CtrlConf1Load1_Type()
)
rm10010CtrlConf1Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010CtrlConf1Load1.setStatus("current")
_Rm10010CtrlConf2Load1_Type = EkiOnOff
_Rm10010CtrlConf2Load1_Object = MibScalar
rm10010CtrlConf2Load1 = _Rm10010CtrlConf2Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 1, 1, 2),
    _Rm10010CtrlConf2Load1_Type()
)
rm10010CtrlConf2Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010CtrlConf2Load1.setStatus("current")
_Rm10010CtrlConf2Flash1_Type = EkiOnOff
_Rm10010CtrlConf2Flash1_Object = MibScalar
rm10010CtrlConf2Flash1 = _Rm10010CtrlConf2Flash1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 1, 1, 10),
    _Rm10010CtrlConf2Flash1_Type()
)
rm10010CtrlConf2Flash1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010CtrlConf2Flash1.setStatus("current")
_Rm10010CtrlConf2Clear1_Type = EkiOnOff
_Rm10010CtrlConf2Clear1_Object = MibScalar
rm10010CtrlConf2Clear1 = _Rm10010CtrlConf2Clear1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 1, 1, 14),
    _Rm10010CtrlConf2Clear1_Type()
)
rm10010CtrlConf2Clear1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010CtrlConf2Clear1.setStatus("current")
_Rm10010Ctrlsynth4_ObjectIdentity = ObjectIdentity
rm10010Ctrlsynth4 = _Rm10010Ctrlsynth4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 1, 4)
)
_Rm10010CtrlCorrelatOn_Type = EkiOnOff
_Rm10010CtrlCorrelatOn_Object = MibScalar
rm10010CtrlCorrelatOn = _Rm10010CtrlCorrelatOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 1, 4, 1),
    _Rm10010CtrlCorrelatOn_Type()
)
rm10010CtrlCorrelatOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010CtrlCorrelatOn.setStatus("current")
_Rm10010CtrlCorrelatOff_Type = EkiOnOff
_Rm10010CtrlCorrelatOff_Object = MibScalar
rm10010CtrlCorrelatOff = _Rm10010CtrlCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 1, 4, 2),
    _Rm10010CtrlCorrelatOff_Type()
)
rm10010CtrlCorrelatOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010CtrlCorrelatOff.setStatus("current")
_Rm10010CtrlswMgnt_ObjectIdentity = ObjectIdentity
rm10010CtrlswMgnt = _Rm10010CtrlswMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 1, 5)
)
_Rm10010CtrlColdReset_Type = EkiOnOff
_Rm10010CtrlColdReset_Object = MibScalar
rm10010CtrlColdReset = _Rm10010CtrlColdReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 1, 5, 2),
    _Rm10010CtrlColdReset_Type()
)
rm10010CtrlColdReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010CtrlColdReset.setStatus("current")
_Rm10010CtrlWarmReset_Type = EkiOnOff
_Rm10010CtrlWarmReset_Object = MibScalar
rm10010CtrlWarmReset = _Rm10010CtrlWarmReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 1, 5, 3),
    _Rm10010CtrlWarmReset_Type()
)
rm10010CtrlWarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010CtrlWarmReset.setStatus("current")
_Rm10010CtrlLoadSwBank1_Type = EkiOnOff
_Rm10010CtrlLoadSwBank1_Object = MibScalar
rm10010CtrlLoadSwBank1 = _Rm10010CtrlLoadSwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 1, 5, 5),
    _Rm10010CtrlLoadSwBank1_Type()
)
rm10010CtrlLoadSwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010CtrlLoadSwBank1.setStatus("current")
_Rm10010CtrlLoadSwBank2_Type = EkiOnOff
_Rm10010CtrlLoadSwBank2_Object = MibScalar
rm10010CtrlLoadSwBank2 = _Rm10010CtrlLoadSwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 1, 5, 6),
    _Rm10010CtrlLoadSwBank2_Type()
)
rm10010CtrlLoadSwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010CtrlLoadSwBank2.setStatus("current")
_Rm10010CtrlgwMgnt_ObjectIdentity = ObjectIdentity
rm10010CtrlgwMgnt = _Rm10010CtrlgwMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 1, 6)
)
_Rm10010CtrlCurrentGwReset_Type = EkiOnOff
_Rm10010CtrlCurrentGwReset_Object = MibScalar
rm10010CtrlCurrentGwReset = _Rm10010CtrlCurrentGwReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 1, 6, 1),
    _Rm10010CtrlCurrentGwReset_Type()
)
rm10010CtrlCurrentGwReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010CtrlCurrentGwReset.setStatus("current")
_Rm10010CtrlLoadGwBank1_Type = EkiOnOff
_Rm10010CtrlLoadGwBank1_Object = MibScalar
rm10010CtrlLoadGwBank1 = _Rm10010CtrlLoadGwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 1, 6, 5),
    _Rm10010CtrlLoadGwBank1_Type()
)
rm10010CtrlLoadGwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010CtrlLoadGwBank1.setStatus("current")
_Rm10010CtrlLoadGwBank2_Type = EkiOnOff
_Rm10010CtrlLoadGwBank2_Object = MibScalar
rm10010CtrlLoadGwBank2 = _Rm10010CtrlLoadGwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 1, 6, 6),
    _Rm10010CtrlLoadGwBank2_Type()
)
rm10010CtrlLoadGwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010CtrlLoadGwBank2.setStatus("current")
_Rm10010CtrlLoadGwBank3_Type = EkiOnOff
_Rm10010CtrlLoadGwBank3_Object = MibScalar
rm10010CtrlLoadGwBank3 = _Rm10010CtrlLoadGwBank3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 1, 6, 7),
    _Rm10010CtrlLoadGwBank3_Type()
)
rm10010CtrlLoadGwBank3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010CtrlLoadGwBank3.setStatus("current")
_Rm10010CtrlLoadGwBank4_Type = EkiOnOff
_Rm10010CtrlLoadGwBank4_Object = MibScalar
rm10010CtrlLoadGwBank4 = _Rm10010CtrlLoadGwBank4_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 1, 6, 8),
    _Rm10010CtrlLoadGwBank4_Type()
)
rm10010CtrlLoadGwBank4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010CtrlLoadGwBank4.setStatus("current")
_Rm10010CtrlledTest_ObjectIdentity = ObjectIdentity
rm10010CtrlledTest = _Rm10010CtrlledTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 1, 192)
)
_Rm10010CtrlGreenLed_Type = EkiOnOff
_Rm10010CtrlGreenLed_Object = MibScalar
rm10010CtrlGreenLed = _Rm10010CtrlGreenLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 1, 192, 1),
    _Rm10010CtrlGreenLed_Type()
)
rm10010CtrlGreenLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010CtrlGreenLed.setStatus("current")
_Rm10010CtrlRedLed_Type = EkiOnOff
_Rm10010CtrlRedLed_Object = MibScalar
rm10010CtrlRedLed = _Rm10010CtrlRedLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 1, 192, 2),
    _Rm10010CtrlRedLed_Type()
)
rm10010CtrlRedLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010CtrlRedLed.setStatus("current")
_Rm10010CtrlLedOff_Type = EkiOnOff
_Rm10010CtrlLedOff_Object = MibScalar
rm10010CtrlLedOff = _Rm10010CtrlLedOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 1, 192, 3),
    _Rm10010CtrlLedOff_Type()
)
rm10010CtrlLedOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010CtrlLedOff.setStatus("current")
_Rm10010CtrlinitSwitchMarvell_ObjectIdentity = ObjectIdentity
rm10010CtrlinitSwitchMarvell = _Rm10010CtrlinitSwitchMarvell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 1, 201)
)
_Rm10010CtrlInitSwitchMarvell_Type = EkiOnOff
_Rm10010CtrlInitSwitchMarvell_Object = MibScalar
rm10010CtrlInitSwitchMarvell = _Rm10010CtrlInitSwitchMarvell_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 1, 201, 1),
    _Rm10010CtrlInitSwitchMarvell_Type()
)
rm10010CtrlInitSwitchMarvell.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010CtrlInitSwitchMarvell.setStatus("current")
_Rm10010CtrlresetCount_ObjectIdentity = ObjectIdentity
rm10010CtrlresetCount = _Rm10010CtrlresetCount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 1, 259)
)
_Rm10010CtrlResetcount_Type = EkiOnOff
_Rm10010CtrlResetcount_Object = MibScalar
rm10010CtrlResetcount = _Rm10010CtrlResetcount_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 1, 259, 1),
    _Rm10010CtrlResetcount_Type()
)
rm10010CtrlResetcount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010CtrlResetcount.setStatus("current")
_Rm10010CtrlresetRmon_ObjectIdentity = ObjectIdentity
rm10010CtrlresetRmon = _Rm10010CtrlresetRmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 1, 260)
)
_Rm10010CtrlResetrmon_Type = EkiOnOff
_Rm10010CtrlResetrmon_Object = MibScalar
rm10010CtrlResetrmon = _Rm10010CtrlResetrmon_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 1, 260, 1),
    _Rm10010CtrlResetrmon_Type()
)
rm10010CtrlResetrmon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010CtrlResetrmon.setStatus("current")
_Rm10010CtrlresetMeasurements_ObjectIdentity = ObjectIdentity
rm10010CtrlresetMeasurements = _Rm10010CtrlresetMeasurements_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 1, 261)
)
_Rm10010CtrlResetmeasurements_Type = EkiOnOff
_Rm10010CtrlResetmeasurements_Object = MibScalar
rm10010CtrlResetmeasurements = _Rm10010CtrlResetmeasurements_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 1, 261, 1),
    _Rm10010CtrlResetmeasurements_Type()
)
rm10010CtrlResetmeasurements.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010CtrlResetmeasurements.setStatus("current")
_Rm10010CtrlClient_ObjectIdentity = ObjectIdentity
rm10010CtrlClient = _Rm10010CtrlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 2)
)
_Rm10010CtrlaccessLoopTable_Object = MibTable
rm10010CtrlaccessLoopTable = _Rm10010CtrlaccessLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 2, 16)
)
if mibBuilder.loadTexts:
    rm10010CtrlaccessLoopTable.setStatus("current")
_Rm10010CtrlaccessLoopEntry_Object = MibTableRow
rm10010CtrlaccessLoopEntry = _Rm10010CtrlaccessLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 2, 16, 1)
)
rm10010CtrlaccessLoopEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010CtrlaccessLoopIndex"),
)
if mibBuilder.loadTexts:
    rm10010CtrlaccessLoopEntry.setStatus("current")


class _Rm10010CtrlaccessLoopIndex_Type(Integer32):
    """Custom type rm10010CtrlaccessLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010CtrlaccessLoopIndex_Type.__name__ = "Integer32"
_Rm10010CtrlaccessLoopIndex_Object = MibTableColumn
rm10010CtrlaccessLoopIndex = _Rm10010CtrlaccessLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 2, 16, 1, 1),
    _Rm10010CtrlaccessLoopIndex_Type()
)
rm10010CtrlaccessLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CtrlaccessLoopIndex.setStatus("current")
_Rm10010CtrlaccessLoopPortn_Type = EkiState
_Rm10010CtrlaccessLoopPortn_Object = MibTableColumn
rm10010CtrlaccessLoopPortn = _Rm10010CtrlaccessLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 2, 16, 1, 2),
    _Rm10010CtrlaccessLoopPortn_Type()
)
rm10010CtrlaccessLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010CtrlaccessLoopPortn.setStatus("current")
_Rm10010CtrlclientLoopToLineTable_Object = MibTable
rm10010CtrlclientLoopToLineTable = _Rm10010CtrlclientLoopToLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 2, 17)
)
if mibBuilder.loadTexts:
    rm10010CtrlclientLoopToLineTable.setStatus("current")
_Rm10010CtrlclientLoopToLineEntry_Object = MibTableRow
rm10010CtrlclientLoopToLineEntry = _Rm10010CtrlclientLoopToLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 2, 17, 1)
)
rm10010CtrlclientLoopToLineEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010CtrlclientLoopToLineIndex"),
)
if mibBuilder.loadTexts:
    rm10010CtrlclientLoopToLineEntry.setStatus("current")


class _Rm10010CtrlclientLoopToLineIndex_Type(Integer32):
    """Custom type rm10010CtrlclientLoopToLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010CtrlclientLoopToLineIndex_Type.__name__ = "Integer32"
_Rm10010CtrlclientLoopToLineIndex_Object = MibTableColumn
rm10010CtrlclientLoopToLineIndex = _Rm10010CtrlclientLoopToLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 2, 17, 1, 1),
    _Rm10010CtrlclientLoopToLineIndex_Type()
)
rm10010CtrlclientLoopToLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CtrlclientLoopToLineIndex.setStatus("current")
_Rm10010CtrlclientLoopToLinePortn_Type = EkiState
_Rm10010CtrlclientLoopToLinePortn_Object = MibTableColumn
rm10010CtrlclientLoopToLinePortn = _Rm10010CtrlclientLoopToLinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 2, 17, 1, 2),
    _Rm10010CtrlclientLoopToLinePortn_Type()
)
rm10010CtrlclientLoopToLinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010CtrlclientLoopToLinePortn.setStatus("current")
_Rm10010CtrlcsfUpInsTable_Object = MibTable
rm10010CtrlcsfUpInsTable = _Rm10010CtrlcsfUpInsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 2, 21)
)
if mibBuilder.loadTexts:
    rm10010CtrlcsfUpInsTable.setStatus("current")
_Rm10010CtrlcsfUpInsEntry_Object = MibTableRow
rm10010CtrlcsfUpInsEntry = _Rm10010CtrlcsfUpInsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 2, 21, 1)
)
rm10010CtrlcsfUpInsEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010CtrlcsfUpInsIndex"),
)
if mibBuilder.loadTexts:
    rm10010CtrlcsfUpInsEntry.setStatus("current")


class _Rm10010CtrlcsfUpInsIndex_Type(Integer32):
    """Custom type rm10010CtrlcsfUpInsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010CtrlcsfUpInsIndex_Type.__name__ = "Integer32"
_Rm10010CtrlcsfUpInsIndex_Object = MibTableColumn
rm10010CtrlcsfUpInsIndex = _Rm10010CtrlcsfUpInsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 2, 21, 1, 1),
    _Rm10010CtrlcsfUpInsIndex_Type()
)
rm10010CtrlcsfUpInsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CtrlcsfUpInsIndex.setStatus("current")
_Rm10010CtrlcsfUpInsPortn_Type = EkiState
_Rm10010CtrlcsfUpInsPortn_Object = MibTableColumn
rm10010CtrlcsfUpInsPortn = _Rm10010CtrlcsfUpInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 2, 21, 1, 2),
    _Rm10010CtrlcsfUpInsPortn_Type()
)
rm10010CtrlcsfUpInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010CtrlcsfUpInsPortn.setStatus("current")
_Rm10010CtrlcaisDwInsTable_Object = MibTable
rm10010CtrlcaisDwInsTable = _Rm10010CtrlcaisDwInsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 2, 22)
)
if mibBuilder.loadTexts:
    rm10010CtrlcaisDwInsTable.setStatus("current")
_Rm10010CtrlcaisDwInsEntry_Object = MibTableRow
rm10010CtrlcaisDwInsEntry = _Rm10010CtrlcaisDwInsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 2, 22, 1)
)
rm10010CtrlcaisDwInsEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010CtrlcaisDwInsIndex"),
)
if mibBuilder.loadTexts:
    rm10010CtrlcaisDwInsEntry.setStatus("current")


class _Rm10010CtrlcaisDwInsIndex_Type(Integer32):
    """Custom type rm10010CtrlcaisDwInsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010CtrlcaisDwInsIndex_Type.__name__ = "Integer32"
_Rm10010CtrlcaisDwInsIndex_Object = MibTableColumn
rm10010CtrlcaisDwInsIndex = _Rm10010CtrlcaisDwInsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 2, 22, 1, 1),
    _Rm10010CtrlcaisDwInsIndex_Type()
)
rm10010CtrlcaisDwInsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CtrlcaisDwInsIndex.setStatus("current")
_Rm10010CtrlcaisDwInsPortn_Type = EkiState
_Rm10010CtrlcaisDwInsPortn_Object = MibTableColumn
rm10010CtrlcaisDwInsPortn = _Rm10010CtrlcaisDwInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 2, 22, 1, 2),
    _Rm10010CtrlcaisDwInsPortn_Type()
)
rm10010CtrlcaisDwInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010CtrlcaisDwInsPortn.setStatus("current")
_Rm10010CtrlclientResetAllCountTable_Object = MibTable
rm10010CtrlclientResetAllCountTable = _Rm10010CtrlclientResetAllCountTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 2, 262)
)
if mibBuilder.loadTexts:
    rm10010CtrlclientResetAllCountTable.setStatus("current")
_Rm10010CtrlclientResetAllCountEntry_Object = MibTableRow
rm10010CtrlclientResetAllCountEntry = _Rm10010CtrlclientResetAllCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 2, 262, 1)
)
rm10010CtrlclientResetAllCountEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010CtrlclientResetAllCountIndex"),
)
if mibBuilder.loadTexts:
    rm10010CtrlclientResetAllCountEntry.setStatus("current")


class _Rm10010CtrlclientResetAllCountIndex_Type(Integer32):
    """Custom type rm10010CtrlclientResetAllCountIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010CtrlclientResetAllCountIndex_Type.__name__ = "Integer32"
_Rm10010CtrlclientResetAllCountIndex_Object = MibTableColumn
rm10010CtrlclientResetAllCountIndex = _Rm10010CtrlclientResetAllCountIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 2, 262, 1, 1),
    _Rm10010CtrlclientResetAllCountIndex_Type()
)
rm10010CtrlclientResetAllCountIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CtrlclientResetAllCountIndex.setStatus("current")
_Rm10010CtrlclientResetAllCountsPortn_Type = EkiState
_Rm10010CtrlclientResetAllCountsPortn_Object = MibTableColumn
rm10010CtrlclientResetAllCountsPortn = _Rm10010CtrlclientResetAllCountsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 2, 262, 1, 2),
    _Rm10010CtrlclientResetAllCountsPortn_Type()
)
rm10010CtrlclientResetAllCountsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010CtrlclientResetAllCountsPortn.setStatus("current")
_Rm10010CtrlLine_ObjectIdentity = ObjectIdentity
rm10010CtrlLine = _Rm10010CtrlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 3)
)
_Rm10010CtrlcommAccessLoopTable_Object = MibTable
rm10010CtrlcommAccessLoopTable = _Rm10010CtrlcommAccessLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 3, 64)
)
if mibBuilder.loadTexts:
    rm10010CtrlcommAccessLoopTable.setStatus("current")
_Rm10010CtrlcommAccessLoopEntry_Object = MibTableRow
rm10010CtrlcommAccessLoopEntry = _Rm10010CtrlcommAccessLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 3, 64, 1)
)
rm10010CtrlcommAccessLoopEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010CtrlcommAccessLoopIndex"),
)
if mibBuilder.loadTexts:
    rm10010CtrlcommAccessLoopEntry.setStatus("current")


class _Rm10010CtrlcommAccessLoopIndex_Type(Integer32):
    """Custom type rm10010CtrlcommAccessLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010CtrlcommAccessLoopIndex_Type.__name__ = "Integer32"
_Rm10010CtrlcommAccessLoopIndex_Object = MibTableColumn
rm10010CtrlcommAccessLoopIndex = _Rm10010CtrlcommAccessLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 3, 64, 1, 1),
    _Rm10010CtrlcommAccessLoopIndex_Type()
)
rm10010CtrlcommAccessLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CtrlcommAccessLoopIndex.setStatus("current")
_Rm10010CtrlcommAccessLoopPortn_Type = EkiState
_Rm10010CtrlcommAccessLoopPortn_Object = MibTableColumn
rm10010CtrlcommAccessLoopPortn = _Rm10010CtrlcommAccessLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 3, 64, 1, 2),
    _Rm10010CtrlcommAccessLoopPortn_Type()
)
rm10010CtrlcommAccessLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010CtrlcommAccessLoopPortn.setStatus("current")
_Rm10010CtrllineLoopTable_Object = MibTable
rm10010CtrllineLoopTable = _Rm10010CtrllineLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 3, 66)
)
if mibBuilder.loadTexts:
    rm10010CtrllineLoopTable.setStatus("current")
_Rm10010CtrllineLoopEntry_Object = MibTableRow
rm10010CtrllineLoopEntry = _Rm10010CtrllineLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 3, 66, 1)
)
rm10010CtrllineLoopEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010CtrllineLoopIndex"),
)
if mibBuilder.loadTexts:
    rm10010CtrllineLoopEntry.setStatus("current")


class _Rm10010CtrllineLoopIndex_Type(Integer32):
    """Custom type rm10010CtrllineLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010CtrllineLoopIndex_Type.__name__ = "Integer32"
_Rm10010CtrllineLoopIndex_Object = MibTableColumn
rm10010CtrllineLoopIndex = _Rm10010CtrllineLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 3, 66, 1, 1),
    _Rm10010CtrllineLoopIndex_Type()
)
rm10010CtrllineLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CtrllineLoopIndex.setStatus("current")
_Rm10010CtrllineLoopPortn_Type = EkiState
_Rm10010CtrllineLoopPortn_Object = MibTableColumn
rm10010CtrllineLoopPortn = _Rm10010CtrllineLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 3, 66, 1, 2),
    _Rm10010CtrllineLoopPortn_Type()
)
rm10010CtrllineLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010CtrllineLoopPortn.setStatus("current")
_Rm10010CtrlfecDisableTable_Object = MibTable
rm10010CtrlfecDisableTable = _Rm10010CtrlfecDisableTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 3, 69)
)
if mibBuilder.loadTexts:
    rm10010CtrlfecDisableTable.setStatus("current")
_Rm10010CtrlfecDisableEntry_Object = MibTableRow
rm10010CtrlfecDisableEntry = _Rm10010CtrlfecDisableEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 3, 69, 1)
)
rm10010CtrlfecDisableEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010CtrlfecDisableIndex"),
)
if mibBuilder.loadTexts:
    rm10010CtrlfecDisableEntry.setStatus("current")


class _Rm10010CtrlfecDisableIndex_Type(Integer32):
    """Custom type rm10010CtrlfecDisableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010CtrlfecDisableIndex_Type.__name__ = "Integer32"
_Rm10010CtrlfecDisableIndex_Object = MibTableColumn
rm10010CtrlfecDisableIndex = _Rm10010CtrlfecDisableIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 3, 69, 1, 1),
    _Rm10010CtrlfecDisableIndex_Type()
)
rm10010CtrlfecDisableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CtrlfecDisableIndex.setStatus("current")
_Rm10010CtrlfecDisablePortn_Type = EkiState
_Rm10010CtrlfecDisablePortn_Object = MibTableColumn
rm10010CtrlfecDisablePortn = _Rm10010CtrlfecDisablePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 3, 69, 1, 2),
    _Rm10010CtrlfecDisablePortn_Type()
)
rm10010CtrlfecDisablePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010CtrlfecDisablePortn.setStatus("current")
_Rm10010CtrlmsaLineLoopTable_Object = MibTable
rm10010CtrlmsaLineLoopTable = _Rm10010CtrlmsaLineLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 3, 209)
)
if mibBuilder.loadTexts:
    rm10010CtrlmsaLineLoopTable.setStatus("current")
_Rm10010CtrlmsaLineLoopEntry_Object = MibTableRow
rm10010CtrlmsaLineLoopEntry = _Rm10010CtrlmsaLineLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 3, 209, 1)
)
rm10010CtrlmsaLineLoopEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010CtrlmsaLineLoopIndex"),
)
if mibBuilder.loadTexts:
    rm10010CtrlmsaLineLoopEntry.setStatus("current")


class _Rm10010CtrlmsaLineLoopIndex_Type(Integer32):
    """Custom type rm10010CtrlmsaLineLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010CtrlmsaLineLoopIndex_Type.__name__ = "Integer32"
_Rm10010CtrlmsaLineLoopIndex_Object = MibTableColumn
rm10010CtrlmsaLineLoopIndex = _Rm10010CtrlmsaLineLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 3, 209, 1, 1),
    _Rm10010CtrlmsaLineLoopIndex_Type()
)
rm10010CtrlmsaLineLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CtrlmsaLineLoopIndex.setStatus("current")
_Rm10010CtrlmsaLineLoopPortn_Type = EkiState
_Rm10010CtrlmsaLineLoopPortn_Object = MibTableColumn
rm10010CtrlmsaLineLoopPortn = _Rm10010CtrlmsaLineLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 3, 209, 1, 2),
    _Rm10010CtrlmsaLineLoopPortn_Type()
)
rm10010CtrlmsaLineLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010CtrlmsaLineLoopPortn.setStatus("current")
_Rm10010CtrlmsaTxResetTable_Object = MibTable
rm10010CtrlmsaTxResetTable = _Rm10010CtrlmsaTxResetTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 3, 210)
)
if mibBuilder.loadTexts:
    rm10010CtrlmsaTxResetTable.setStatus("current")
_Rm10010CtrlmsaTxResetEntry_Object = MibTableRow
rm10010CtrlmsaTxResetEntry = _Rm10010CtrlmsaTxResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 3, 210, 1)
)
rm10010CtrlmsaTxResetEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010CtrlmsaTxResetIndex"),
)
if mibBuilder.loadTexts:
    rm10010CtrlmsaTxResetEntry.setStatus("current")


class _Rm10010CtrlmsaTxResetIndex_Type(Integer32):
    """Custom type rm10010CtrlmsaTxResetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010CtrlmsaTxResetIndex_Type.__name__ = "Integer32"
_Rm10010CtrlmsaTxResetIndex_Object = MibTableColumn
rm10010CtrlmsaTxResetIndex = _Rm10010CtrlmsaTxResetIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 3, 210, 1, 1),
    _Rm10010CtrlmsaTxResetIndex_Type()
)
rm10010CtrlmsaTxResetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CtrlmsaTxResetIndex.setStatus("current")
_Rm10010CtrlmsaTxResetPortn_Type = EkiState
_Rm10010CtrlmsaTxResetPortn_Object = MibTableColumn
rm10010CtrlmsaTxResetPortn = _Rm10010CtrlmsaTxResetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 3, 210, 1, 2),
    _Rm10010CtrlmsaTxResetPortn_Type()
)
rm10010CtrlmsaTxResetPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010CtrlmsaTxResetPortn.setStatus("current")
_Rm10010CtrlmsaRxResetTable_Object = MibTable
rm10010CtrlmsaRxResetTable = _Rm10010CtrlmsaRxResetTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 3, 211)
)
if mibBuilder.loadTexts:
    rm10010CtrlmsaRxResetTable.setStatus("current")
_Rm10010CtrlmsaRxResetEntry_Object = MibTableRow
rm10010CtrlmsaRxResetEntry = _Rm10010CtrlmsaRxResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 3, 211, 1)
)
rm10010CtrlmsaRxResetEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010CtrlmsaRxResetIndex"),
)
if mibBuilder.loadTexts:
    rm10010CtrlmsaRxResetEntry.setStatus("current")


class _Rm10010CtrlmsaRxResetIndex_Type(Integer32):
    """Custom type rm10010CtrlmsaRxResetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010CtrlmsaRxResetIndex_Type.__name__ = "Integer32"
_Rm10010CtrlmsaRxResetIndex_Object = MibTableColumn
rm10010CtrlmsaRxResetIndex = _Rm10010CtrlmsaRxResetIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 3, 211, 1, 1),
    _Rm10010CtrlmsaRxResetIndex_Type()
)
rm10010CtrlmsaRxResetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CtrlmsaRxResetIndex.setStatus("current")
_Rm10010CtrlmsaRxResetPortn_Type = EkiState
_Rm10010CtrlmsaRxResetPortn_Object = MibTableColumn
rm10010CtrlmsaRxResetPortn = _Rm10010CtrlmsaRxResetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 3, 211, 1, 2),
    _Rm10010CtrlmsaRxResetPortn_Type()
)
rm10010CtrlmsaRxResetPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010CtrlmsaRxResetPortn.setStatus("current")
_Rm10010CtrlmsaShutdownTable_Object = MibTable
rm10010CtrlmsaShutdownTable = _Rm10010CtrlmsaShutdownTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 3, 212)
)
if mibBuilder.loadTexts:
    rm10010CtrlmsaShutdownTable.setStatus("current")
_Rm10010CtrlmsaShutdownEntry_Object = MibTableRow
rm10010CtrlmsaShutdownEntry = _Rm10010CtrlmsaShutdownEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 3, 212, 1)
)
rm10010CtrlmsaShutdownEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010CtrlmsaShutdownIndex"),
)
if mibBuilder.loadTexts:
    rm10010CtrlmsaShutdownEntry.setStatus("current")


class _Rm10010CtrlmsaShutdownIndex_Type(Integer32):
    """Custom type rm10010CtrlmsaShutdownIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010CtrlmsaShutdownIndex_Type.__name__ = "Integer32"
_Rm10010CtrlmsaShutdownIndex_Object = MibTableColumn
rm10010CtrlmsaShutdownIndex = _Rm10010CtrlmsaShutdownIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 3, 212, 1, 1),
    _Rm10010CtrlmsaShutdownIndex_Type()
)
rm10010CtrlmsaShutdownIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CtrlmsaShutdownIndex.setStatus("current")
_Rm10010CtrlmsaShutdownPortn_Type = EkiState
_Rm10010CtrlmsaShutdownPortn_Object = MibTableColumn
rm10010CtrlmsaShutdownPortn = _Rm10010CtrlmsaShutdownPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 3, 212, 1, 2),
    _Rm10010CtrlmsaShutdownPortn_Type()
)
rm10010CtrlmsaShutdownPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010CtrlmsaShutdownPortn.setStatus("current")
_Rm10010CtrllineResetAllCountTable_Object = MibTable
rm10010CtrllineResetAllCountTable = _Rm10010CtrllineResetAllCountTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 3, 263)
)
if mibBuilder.loadTexts:
    rm10010CtrllineResetAllCountTable.setStatus("current")
_Rm10010CtrllineResetAllCountEntry_Object = MibTableRow
rm10010CtrllineResetAllCountEntry = _Rm10010CtrllineResetAllCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 3, 263, 1)
)
rm10010CtrllineResetAllCountEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010CtrllineResetAllCountIndex"),
)
if mibBuilder.loadTexts:
    rm10010CtrllineResetAllCountEntry.setStatus("current")


class _Rm10010CtrllineResetAllCountIndex_Type(Integer32):
    """Custom type rm10010CtrllineResetAllCountIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010CtrllineResetAllCountIndex_Type.__name__ = "Integer32"
_Rm10010CtrllineResetAllCountIndex_Object = MibTableColumn
rm10010CtrllineResetAllCountIndex = _Rm10010CtrllineResetAllCountIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 3, 263, 1, 1),
    _Rm10010CtrllineResetAllCountIndex_Type()
)
rm10010CtrllineResetAllCountIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CtrllineResetAllCountIndex.setStatus("current")
_Rm10010CtrllineResetAllCountsPortn_Type = EkiState
_Rm10010CtrllineResetAllCountsPortn_Object = MibTableColumn
rm10010CtrllineResetAllCountsPortn = _Rm10010CtrllineResetAllCountsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 6, 3, 263, 1, 2),
    _Rm10010CtrllineResetAllCountsPortn_Type()
)
rm10010CtrllineResetAllCountsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010CtrllineResetAllCountsPortn.setStatus("current")
_Rm10010ri_ObjectIdentity = ObjectIdentity
rm10010ri = _Rm10010ri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 7)
)
_Rm10010riTable_ObjectIdentity = ObjectIdentity
rm10010riTable = _Rm10010riTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 7, 1)
)
_Rm10010RinvSfpTable_Object = MibTable
rm10010RinvSfpTable = _Rm10010RinvSfpTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 7, 1, 1)
)
if mibBuilder.loadTexts:
    rm10010RinvSfpTable.setStatus("current")
_Rm10010RinvSfpEntry_Object = MibTableRow
rm10010RinvSfpEntry = _Rm10010RinvSfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 7, 1, 1, 1)
)
rm10010RinvSfpEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010RinvSfpIndex"),
)
if mibBuilder.loadTexts:
    rm10010RinvSfpEntry.setStatus("current")


class _Rm10010RinvSfpIndex_Type(Integer32):
    """Custom type rm10010RinvSfpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Rm10010RinvSfpIndex_Type.__name__ = "Integer32"
_Rm10010RinvSfpIndex_Object = MibTableColumn
rm10010RinvSfpIndex = _Rm10010RinvSfpIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 7, 1, 1, 1, 1),
    _Rm10010RinvSfpIndex_Type()
)
rm10010RinvSfpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010RinvSfpIndex.setStatus("current")
_Rm10010Rinvsfp_Type = DisplayString
_Rm10010Rinvsfp_Object = MibTableColumn
rm10010Rinvsfp = _Rm10010Rinvsfp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 7, 1, 1, 1, 2),
    _Rm10010Rinvsfp_Type()
)
rm10010Rinvsfp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010Rinvsfp.setStatus("current")
_Rm10010RinvLineTable_Object = MibTable
rm10010RinvLineTable = _Rm10010RinvLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 7, 1, 2)
)
if mibBuilder.loadTexts:
    rm10010RinvLineTable.setStatus("current")
_Rm10010RinvLineEntry_Object = MibTableRow
rm10010RinvLineEntry = _Rm10010RinvLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 7, 1, 2, 1)
)
rm10010RinvLineEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010RinvLineIndex"),
)
if mibBuilder.loadTexts:
    rm10010RinvLineEntry.setStatus("current")


class _Rm10010RinvLineIndex_Type(Integer32):
    """Custom type rm10010RinvLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Rm10010RinvLineIndex_Type.__name__ = "Integer32"
_Rm10010RinvLineIndex_Object = MibTableColumn
rm10010RinvLineIndex = _Rm10010RinvLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 7, 1, 2, 1, 1),
    _Rm10010RinvLineIndex_Type()
)
rm10010RinvLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010RinvLineIndex.setStatus("current")
_Rm10010RinvxfpLine_Type = DisplayString
_Rm10010RinvxfpLine_Object = MibTableColumn
rm10010RinvxfpLine = _Rm10010RinvxfpLine_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 7, 1, 2, 1, 2),
    _Rm10010RinvxfpLine_Type()
)
rm10010RinvxfpLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010RinvxfpLine.setStatus("current")
_Rm10010RinvReloadInventory_Type = EkiOnOff
_Rm10010RinvReloadInventory_Object = MibScalar
rm10010RinvReloadInventory = _Rm10010RinvReloadInventory_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 7, 2),
    _Rm10010RinvReloadInventory_Type()
)
rm10010RinvReloadInventory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010RinvReloadInventory.setStatus("current")
_Rm10010RinvHwPlatform_Type = DisplayString
_Rm10010RinvHwPlatform_Object = MibScalar
rm10010RinvHwPlatform = _Rm10010RinvHwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 7, 3),
    _Rm10010RinvHwPlatform_Type()
)
rm10010RinvHwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010RinvHwPlatform.setStatus("current")
_Rm10010RinvModulePlatform_Type = DisplayString
_Rm10010RinvModulePlatform_Object = MibScalar
rm10010RinvModulePlatform = _Rm10010RinvModulePlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 7, 4),
    _Rm10010RinvModulePlatform_Type()
)
rm10010RinvModulePlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010RinvModulePlatform.setStatus("current")
_Rm10010RinvSwPlatform_Type = DisplayString
_Rm10010RinvSwPlatform_Object = MibScalar
rm10010RinvSwPlatform = _Rm10010RinvSwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 7, 5),
    _Rm10010RinvSwPlatform_Type()
)
rm10010RinvSwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010RinvSwPlatform.setStatus("current")
_Rm10010RinvGwPlatform_Type = DisplayString
_Rm10010RinvGwPlatform_Object = MibScalar
rm10010RinvGwPlatform = _Rm10010RinvGwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 7, 6),
    _Rm10010RinvGwPlatform_Type()
)
rm10010RinvGwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010RinvGwPlatform.setStatus("current")
_Rm10010download_ObjectIdentity = ObjectIdentity
rm10010download = _Rm10010download_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 8)
)
_Rm10010DwlOther_ObjectIdentity = ObjectIdentity
rm10010DwlOther = _Rm10010DwlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 8, 1)
)
_Rm10010DwlrestartProcess_ObjectIdentity = ObjectIdentity
rm10010DwlrestartProcess = _Rm10010DwlrestartProcess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 8, 1, 0)
)
_Rm10010DwlWarmRestartProcessed_Type = EkiOnOff
_Rm10010DwlWarmRestartProcessed_Object = MibScalar
rm10010DwlWarmRestartProcessed = _Rm10010DwlWarmRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 8, 1, 0, 1),
    _Rm10010DwlWarmRestartProcessed_Type()
)
rm10010DwlWarmRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010DwlWarmRestartProcessed.setStatus("current")
_Rm10010DwlColdRestartProcessed_Type = EkiOnOff
_Rm10010DwlColdRestartProcessed_Object = MibScalar
rm10010DwlColdRestartProcessed = _Rm10010DwlColdRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 8, 1, 0, 2),
    _Rm10010DwlColdRestartProcessed_Type()
)
rm10010DwlColdRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010DwlColdRestartProcessed.setStatus("current")
_Rm10010DwlswBanksUsed_ObjectIdentity = ObjectIdentity
rm10010DwlswBanksUsed = _Rm10010DwlswBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 8, 1, 1)
)
_Rm10010DwlSwBank1Used_Type = EkiOnOff
_Rm10010DwlSwBank1Used_Object = MibScalar
rm10010DwlSwBank1Used = _Rm10010DwlSwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 8, 1, 1, 1),
    _Rm10010DwlSwBank1Used_Type()
)
rm10010DwlSwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010DwlSwBank1Used.setStatus("current")
_Rm10010DwlSwBank2Used_Type = EkiOnOff
_Rm10010DwlSwBank2Used_Object = MibScalar
rm10010DwlSwBank2Used = _Rm10010DwlSwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 8, 1, 1, 2),
    _Rm10010DwlSwBank2Used_Type()
)
rm10010DwlSwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010DwlSwBank2Used.setStatus("current")
_Rm10010DwlSwBank1Notempty_Type = EkiOnOff
_Rm10010DwlSwBank1Notempty_Object = MibScalar
rm10010DwlSwBank1Notempty = _Rm10010DwlSwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 8, 1, 1, 5),
    _Rm10010DwlSwBank1Notempty_Type()
)
rm10010DwlSwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010DwlSwBank1Notempty.setStatus("current")
_Rm10010DwlSwBank2Notempty_Type = EkiOnOff
_Rm10010DwlSwBank2Notempty_Object = MibScalar
rm10010DwlSwBank2Notempty = _Rm10010DwlSwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 8, 1, 1, 6),
    _Rm10010DwlSwBank2Notempty_Type()
)
rm10010DwlSwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010DwlSwBank2Notempty.setStatus("current")
_Rm10010DwlgwBanksUsed_ObjectIdentity = ObjectIdentity
rm10010DwlgwBanksUsed = _Rm10010DwlgwBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 8, 1, 2)
)
_Rm10010DwlGwBank1Used_Type = EkiOnOff
_Rm10010DwlGwBank1Used_Object = MibScalar
rm10010DwlGwBank1Used = _Rm10010DwlGwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 8, 1, 2, 1),
    _Rm10010DwlGwBank1Used_Type()
)
rm10010DwlGwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010DwlGwBank1Used.setStatus("current")
_Rm10010DwlGwBank2Used_Type = EkiOnOff
_Rm10010DwlGwBank2Used_Object = MibScalar
rm10010DwlGwBank2Used = _Rm10010DwlGwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 8, 1, 2, 2),
    _Rm10010DwlGwBank2Used_Type()
)
rm10010DwlGwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010DwlGwBank2Used.setStatus("current")
_Rm10010DwlGwBank3Used_Type = EkiOnOff
_Rm10010DwlGwBank3Used_Object = MibScalar
rm10010DwlGwBank3Used = _Rm10010DwlGwBank3Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 8, 1, 2, 3),
    _Rm10010DwlGwBank3Used_Type()
)
rm10010DwlGwBank3Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010DwlGwBank3Used.setStatus("current")
_Rm10010DwlGwBank4Used_Type = EkiOnOff
_Rm10010DwlGwBank4Used_Object = MibScalar
rm10010DwlGwBank4Used = _Rm10010DwlGwBank4Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 8, 1, 2, 4),
    _Rm10010DwlGwBank4Used_Type()
)
rm10010DwlGwBank4Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010DwlGwBank4Used.setStatus("current")
_Rm10010DwlGwBank1Notempty_Type = EkiOnOff
_Rm10010DwlGwBank1Notempty_Object = MibScalar
rm10010DwlGwBank1Notempty = _Rm10010DwlGwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 8, 1, 2, 5),
    _Rm10010DwlGwBank1Notempty_Type()
)
rm10010DwlGwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010DwlGwBank1Notempty.setStatus("current")
_Rm10010DwlGwBank2Notempty_Type = EkiOnOff
_Rm10010DwlGwBank2Notempty_Object = MibScalar
rm10010DwlGwBank2Notempty = _Rm10010DwlGwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 8, 1, 2, 6),
    _Rm10010DwlGwBank2Notempty_Type()
)
rm10010DwlGwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010DwlGwBank2Notempty.setStatus("current")
_Rm10010DwlGwBank3Notempty_Type = EkiOnOff
_Rm10010DwlGwBank3Notempty_Object = MibScalar
rm10010DwlGwBank3Notempty = _Rm10010DwlGwBank3Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 8, 1, 2, 7),
    _Rm10010DwlGwBank3Notempty_Type()
)
rm10010DwlGwBank3Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010DwlGwBank3Notempty.setStatus("current")
_Rm10010DwlGwBank4Notempty_Type = EkiOnOff
_Rm10010DwlGwBank4Notempty_Object = MibScalar
rm10010DwlGwBank4Notempty = _Rm10010DwlGwBank4Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 8, 1, 2, 8),
    _Rm10010DwlGwBank4Notempty_Type()
)
rm10010DwlGwBank4Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010DwlGwBank4Notempty.setStatus("current")
_Rm10010DwlClient_ObjectIdentity = ObjectIdentity
rm10010DwlClient = _Rm10010DwlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 8, 2)
)
_Rm10010DwlLine_ObjectIdentity = ObjectIdentity
rm10010DwlLine = _Rm10010DwlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 8, 3)
)
_Rm10010Config_ObjectIdentity = ObjectIdentity
rm10010Config = _Rm10010Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 9)
)
_Rm10010CfgAccessCAisCsf_ObjectIdentity = ObjectIdentity
rm10010CfgAccessCAisCsf = _Rm10010CfgAccessCAisCsf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 9, 1)
)
_Rm10010CfgClientcaiscsfTable_Object = MibTable
rm10010CfgClientcaiscsfTable = _Rm10010CfgClientcaiscsfTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 9, 1, 1)
)
if mibBuilder.loadTexts:
    rm10010CfgClientcaiscsfTable.setStatus("current")
_Rm10010CfgClientcaiscsfEntry_Object = MibTableRow
rm10010CfgClientcaiscsfEntry = _Rm10010CfgClientcaiscsfEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 9, 1, 1, 1)
)
rm10010CfgClientcaiscsfEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010CfgClientcaiscsfIndex"),
)
if mibBuilder.loadTexts:
    rm10010CfgClientcaiscsfEntry.setStatus("current")


class _Rm10010CfgClientcaiscsfIndex_Type(Integer32):
    """Custom type rm10010CfgClientcaiscsfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010CfgClientcaiscsfIndex_Type.__name__ = "Integer32"
_Rm10010CfgClientcaiscsfIndex_Object = MibTableColumn
rm10010CfgClientcaiscsfIndex = _Rm10010CfgClientcaiscsfIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 9, 1, 1, 1, 1),
    _Rm10010CfgClientcaiscsfIndex_Type()
)
rm10010CfgClientcaiscsfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CfgClientcaiscsfIndex.setStatus("current")


class _Rm10010CfgReservePortn_Type(Unsigned32):
    """Custom type rm10010CfgReservePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010CfgReservePortn_Type.__name__ = "Unsigned32"
_Rm10010CfgReservePortn_Object = MibTableColumn
rm10010CfgReservePortn = _Rm10010CfgReservePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 9, 1, 1, 1, 3),
    _Rm10010CfgReservePortn_Type()
)
rm10010CfgReservePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010CfgReservePortn.setStatus("current")
_Rm10010CfgStartup_ObjectIdentity = ObjectIdentity
rm10010CfgStartup = _Rm10010CfgStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 9, 2)
)
_Rm10010CfgClientStartupTable_Object = MibTable
rm10010CfgClientStartupTable = _Rm10010CfgClientStartupTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 9, 2, 1)
)
if mibBuilder.loadTexts:
    rm10010CfgClientStartupTable.setStatus("current")
_Rm10010CfgClientStartupEntry_Object = MibTableRow
rm10010CfgClientStartupEntry = _Rm10010CfgClientStartupEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 9, 2, 1, 1)
)
rm10010CfgClientStartupEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010CfgClientStartupIndex"),
)
if mibBuilder.loadTexts:
    rm10010CfgClientStartupEntry.setStatus("current")


class _Rm10010CfgClientStartupIndex_Type(Integer32):
    """Custom type rm10010CfgClientStartupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010CfgClientStartupIndex_Type.__name__ = "Integer32"
_Rm10010CfgClientStartupIndex_Object = MibTableColumn
rm10010CfgClientStartupIndex = _Rm10010CfgClientStartupIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 9, 2, 1, 1, 1),
    _Rm10010CfgClientStartupIndex_Type()
)
rm10010CfgClientStartupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CfgClientStartupIndex.setStatus("current")


class _Rm10010CfgSystConfPortPortn_Type(Unsigned32):
    """Custom type rm10010CfgSystConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010CfgSystConfPortPortn_Type.__name__ = "Unsigned32"
_Rm10010CfgSystConfPortPortn_Object = MibTableColumn
rm10010CfgSystConfPortPortn = _Rm10010CfgSystConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 9, 2, 1, 1, 3),
    _Rm10010CfgSystConfPortPortn_Type()
)
rm10010CfgSystConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010CfgSystConfPortPortn.setStatus("current")


class _Rm10010CfgNetConfPortPortn_Type(Unsigned32):
    """Custom type rm10010CfgNetConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010CfgNetConfPortPortn_Type.__name__ = "Unsigned32"
_Rm10010CfgNetConfPortPortn_Object = MibTableColumn
rm10010CfgNetConfPortPortn = _Rm10010CfgNetConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 9, 2, 1, 1, 4),
    _Rm10010CfgNetConfPortPortn_Type()
)
rm10010CfgNetConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010CfgNetConfPortPortn.setStatus("current")


class _Rm10010CfgOptionsPortPortn_Type(Unsigned32):
    """Custom type rm10010CfgOptionsPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010CfgOptionsPortPortn_Type.__name__ = "Unsigned32"
_Rm10010CfgOptionsPortPortn_Object = MibTableColumn
rm10010CfgOptionsPortPortn = _Rm10010CfgOptionsPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 9, 2, 1, 1, 14),
    _Rm10010CfgOptionsPortPortn_Type()
)
rm10010CfgOptionsPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010CfgOptionsPortPortn.setStatus("current")
_Rm10010CfgLineStartupTable_Object = MibTable
rm10010CfgLineStartupTable = _Rm10010CfgLineStartupTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 9, 2, 2)
)
if mibBuilder.loadTexts:
    rm10010CfgLineStartupTable.setStatus("current")
_Rm10010CfgLineStartupEntry_Object = MibTableRow
rm10010CfgLineStartupEntry = _Rm10010CfgLineStartupEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 9, 2, 2, 1)
)
rm10010CfgLineStartupEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010CfgLineStartupIndex"),
)
if mibBuilder.loadTexts:
    rm10010CfgLineStartupEntry.setStatus("current")


class _Rm10010CfgLineStartupIndex_Type(Integer32):
    """Custom type rm10010CfgLineStartupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010CfgLineStartupIndex_Type.__name__ = "Integer32"
_Rm10010CfgLineStartupIndex_Object = MibTableColumn
rm10010CfgLineStartupIndex = _Rm10010CfgLineStartupIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 9, 2, 2, 1, 1),
    _Rm10010CfgLineStartupIndex_Type()
)
rm10010CfgLineStartupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CfgLineStartupIndex.setStatus("current")


class _Rm10010CfgSystConfLinePortn_Type(Unsigned32):
    """Custom type rm10010CfgSystConfLinePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010CfgSystConfLinePortn_Type.__name__ = "Unsigned32"
_Rm10010CfgSystConfLinePortn_Object = MibTableColumn
rm10010CfgSystConfLinePortn = _Rm10010CfgSystConfLinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 9, 2, 2, 1, 3),
    _Rm10010CfgSystConfLinePortn_Type()
)
rm10010CfgSystConfLinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010CfgSystConfLinePortn.setStatus("current")


class _Rm10010CfgOptionsLinePortn_Type(Unsigned32):
    """Custom type rm10010CfgOptionsLinePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010CfgOptionsLinePortn_Type.__name__ = "Unsigned32"
_Rm10010CfgOptionsLinePortn_Object = MibTableColumn
rm10010CfgOptionsLinePortn = _Rm10010CfgOptionsLinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 9, 2, 2, 1, 14),
    _Rm10010CfgOptionsLinePortn_Type()
)
rm10010CfgOptionsLinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010CfgOptionsLinePortn.setStatus("current")
_Rm10010CfgXfpTable_Object = MibTable
rm10010CfgXfpTable = _Rm10010CfgXfpTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 9, 2, 3)
)
if mibBuilder.loadTexts:
    rm10010CfgXfpTable.setStatus("current")
_Rm10010CfgXfpEntry_Object = MibTableRow
rm10010CfgXfpEntry = _Rm10010CfgXfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 9, 2, 3, 1)
)
rm10010CfgXfpEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010CfgXfpIndex"),
)
if mibBuilder.loadTexts:
    rm10010CfgXfpEntry.setStatus("current")


class _Rm10010CfgXfpIndex_Type(Integer32):
    """Custom type rm10010CfgXfpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010CfgXfpIndex_Type.__name__ = "Integer32"
_Rm10010CfgXfpIndex_Object = MibTableColumn
rm10010CfgXfpIndex = _Rm10010CfgXfpIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 9, 2, 3, 1, 1),
    _Rm10010CfgXfpIndex_Type()
)
rm10010CfgXfpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CfgXfpIndex.setStatus("current")


class _Rm10010CfgSystConfMsaLinePortn_Type(Unsigned32):
    """Custom type rm10010CfgSystConfMsaLinePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010CfgSystConfMsaLinePortn_Type.__name__ = "Unsigned32"
_Rm10010CfgSystConfMsaLinePortn_Object = MibTableColumn
rm10010CfgSystConfMsaLinePortn = _Rm10010CfgSystConfMsaLinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 9, 2, 3, 1, 3),
    _Rm10010CfgSystConfMsaLinePortn_Type()
)
rm10010CfgSystConfMsaLinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010CfgSystConfMsaLinePortn.setStatus("current")
_Rm10010CfgLabels_ObjectIdentity = ObjectIdentity
rm10010CfgLabels = _Rm10010CfgLabels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 9, 3)
)
_Rm10010CfgLabelclientTable_Object = MibTable
rm10010CfgLabelclientTable = _Rm10010CfgLabelclientTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 9, 3, 1)
)
if mibBuilder.loadTexts:
    rm10010CfgLabelclientTable.setStatus("current")
_Rm10010CfgLabelclientEntry_Object = MibTableRow
rm10010CfgLabelclientEntry = _Rm10010CfgLabelclientEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 9, 3, 1, 1)
)
rm10010CfgLabelclientEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010CfgLabelclientIndex"),
)
if mibBuilder.loadTexts:
    rm10010CfgLabelclientEntry.setStatus("current")


class _Rm10010CfgLabelclientIndex_Type(Integer32):
    """Custom type rm10010CfgLabelclientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010CfgLabelclientIndex_Type.__name__ = "Integer32"
_Rm10010CfgLabelclientIndex_Object = MibTableColumn
rm10010CfgLabelclientIndex = _Rm10010CfgLabelclientIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 9, 3, 1, 1, 1),
    _Rm10010CfgLabelclientIndex_Type()
)
rm10010CfgLabelclientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CfgLabelclientIndex.setStatus("current")


class _Rm10010CfgLabelclientPortn_Type(DisplayString):
    """Custom type rm10010CfgLabelclientPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Rm10010CfgLabelclientPortn_Type.__name__ = "DisplayString"
_Rm10010CfgLabelclientPortn_Object = MibTableColumn
rm10010CfgLabelclientPortn = _Rm10010CfgLabelclientPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 9, 3, 1, 1, 3),
    _Rm10010CfgLabelclientPortn_Type()
)
rm10010CfgLabelclientPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010CfgLabelclientPortn.setStatus("current")
_Rm10010CfgLabellineTable_Object = MibTable
rm10010CfgLabellineTable = _Rm10010CfgLabellineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 9, 3, 2)
)
if mibBuilder.loadTexts:
    rm10010CfgLabellineTable.setStatus("current")
_Rm10010CfgLabellineEntry_Object = MibTableRow
rm10010CfgLabellineEntry = _Rm10010CfgLabellineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 9, 3, 2, 1)
)
rm10010CfgLabellineEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010CfgLabellineIndex"),
)
if mibBuilder.loadTexts:
    rm10010CfgLabellineEntry.setStatus("current")


class _Rm10010CfgLabellineIndex_Type(Integer32):
    """Custom type rm10010CfgLabellineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010CfgLabellineIndex_Type.__name__ = "Integer32"
_Rm10010CfgLabellineIndex_Object = MibTableColumn
rm10010CfgLabellineIndex = _Rm10010CfgLabellineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 9, 3, 2, 1, 1),
    _Rm10010CfgLabellineIndex_Type()
)
rm10010CfgLabellineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CfgLabellineIndex.setStatus("current")


class _Rm10010CfgLabellinePortn_Type(DisplayString):
    """Custom type rm10010CfgLabellinePortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Rm10010CfgLabellinePortn_Type.__name__ = "DisplayString"
_Rm10010CfgLabellinePortn_Object = MibTableColumn
rm10010CfgLabellinePortn = _Rm10010CfgLabellinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 9, 3, 2, 1, 3),
    _Rm10010CfgLabellinePortn_Type()
)
rm10010CfgLabellinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010CfgLabellinePortn.setStatus("current")
_Rm10010CfgStartuptlh_ObjectIdentity = ObjectIdentity
rm10010CfgStartuptlh = _Rm10010CfgStartuptlh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 9, 4)
)
_Rm10010CfgOtxtlhTable_Object = MibTable
rm10010CfgOtxtlhTable = _Rm10010CfgOtxtlhTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 9, 4, 1)
)
if mibBuilder.loadTexts:
    rm10010CfgOtxtlhTable.setStatus("current")
_Rm10010CfgOtxtlhEntry_Object = MibTableRow
rm10010CfgOtxtlhEntry = _Rm10010CfgOtxtlhEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 9, 4, 1, 1)
)
rm10010CfgOtxtlhEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010CfgOtxtlhIndex"),
)
if mibBuilder.loadTexts:
    rm10010CfgOtxtlhEntry.setStatus("current")


class _Rm10010CfgOtxtlhIndex_Type(Integer32):
    """Custom type rm10010CfgOtxtlhIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010CfgOtxtlhIndex_Type.__name__ = "Integer32"
_Rm10010CfgOtxtlhIndex_Object = MibTableColumn
rm10010CfgOtxtlhIndex = _Rm10010CfgOtxtlhIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 9, 4, 1, 1, 1),
    _Rm10010CfgOtxtlhIndex_Type()
)
rm10010CfgOtxtlhIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CfgOtxtlhIndex.setStatus("current")


class _Rm10010CfgLinePwrLaserPortn_Type(Unsigned32):
    """Custom type rm10010CfgLinePwrLaserPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010CfgLinePwrLaserPortn_Type.__name__ = "Unsigned32"
_Rm10010CfgLinePwrLaserPortn_Object = MibTableColumn
rm10010CfgLinePwrLaserPortn = _Rm10010CfgLinePwrLaserPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 9, 4, 1, 1, 6),
    _Rm10010CfgLinePwrLaserPortn_Type()
)
rm10010CfgLinePwrLaserPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010CfgLinePwrLaserPortn.setStatus("current")


class _Rm10010CfgLineFCurrentPortn_Type(Unsigned32):
    """Custom type rm10010CfgLineFCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010CfgLineFCurrentPortn_Type.__name__ = "Unsigned32"
_Rm10010CfgLineFCurrentPortn_Object = MibTableColumn
rm10010CfgLineFCurrentPortn = _Rm10010CfgLineFCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 9, 4, 1, 1, 7),
    _Rm10010CfgLineFCurrentPortn_Type()
)
rm10010CfgLineFCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010CfgLineFCurrentPortn.setStatus("current")


class _Rm10010CfgLineGridCurrentPortn_Type(Unsigned32):
    """Custom type rm10010CfgLineGridCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010CfgLineGridCurrentPortn_Type.__name__ = "Unsigned32"
_Rm10010CfgLineGridCurrentPortn_Object = MibTableColumn
rm10010CfgLineGridCurrentPortn = _Rm10010CfgLineGridCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 9, 4, 1, 1, 8),
    _Rm10010CfgLineGridCurrentPortn_Type()
)
rm10010CfgLineGridCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010CfgLineGridCurrentPortn.setStatus("current")


class _Rm10010CfgFPortn_Type(Unsigned32):
    """Custom type rm10010CfgFPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010CfgFPortn_Type.__name__ = "Unsigned32"
_Rm10010CfgFPortn_Object = MibTableColumn
rm10010CfgFPortn = _Rm10010CfgFPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 9, 4, 1, 1, 9),
    _Rm10010CfgFPortn_Type()
)
rm10010CfgFPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010CfgFPortn.setStatus("current")


class _Rm10010CfgRxLineFCurrentPortn_Type(Unsigned32):
    """Custom type rm10010CfgRxLineFCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010CfgRxLineFCurrentPortn_Type.__name__ = "Unsigned32"
_Rm10010CfgRxLineFCurrentPortn_Object = MibTableColumn
rm10010CfgRxLineFCurrentPortn = _Rm10010CfgRxLineFCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 9, 4, 1, 1, 10),
    _Rm10010CfgRxLineFCurrentPortn_Type()
)
rm10010CfgRxLineFCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010CfgRxLineFCurrentPortn.setStatus("current")
_Rm10010CfgOther_ObjectIdentity = ObjectIdentity
rm10010CfgOther = _Rm10010CfgOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 9, 5)
)
_Rm10010tablemoduleOther_ObjectIdentity = ObjectIdentity
rm10010tablemoduleOther = _Rm10010tablemoduleOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 9, 5, 1)
)


class _Rm10010Cfgmode_Type(Unsigned32):
    """Custom type rm10010Cfgmode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010Cfgmode_Type.__name__ = "Unsigned32"
_Rm10010Cfgmode_Object = MibScalar
rm10010Cfgmode = _Rm10010Cfgmode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 9, 5, 1, 2),
    _Rm10010Cfgmode_Type()
)
rm10010Cfgmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010Cfgmode.setStatus("current")


class _Rm10010CfgfanLowSpeedThreshold_Type(Unsigned32):
    """Custom type rm10010CfgfanLowSpeedThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010CfgfanLowSpeedThreshold_Type.__name__ = "Unsigned32"
_Rm10010CfgfanLowSpeedThreshold_Object = MibScalar
rm10010CfgfanLowSpeedThreshold = _Rm10010CfgfanLowSpeedThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 9, 5, 1, 3),
    _Rm10010CfgfanLowSpeedThreshold_Type()
)
rm10010CfgfanLowSpeedThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010CfgfanLowSpeedThreshold.setStatus("current")


class _Rm10010CfgfanHighSpeedThreshold_Type(Unsigned32):
    """Custom type rm10010CfgfanHighSpeedThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010CfgfanHighSpeedThreshold_Type.__name__ = "Unsigned32"
_Rm10010CfgfanHighSpeedThreshold_Object = MibScalar
rm10010CfgfanHighSpeedThreshold = _Rm10010CfgfanHighSpeedThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 9, 5, 1, 4),
    _Rm10010CfgfanHighSpeedThreshold_Type()
)
rm10010CfgfanHighSpeedThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010CfgfanHighSpeedThreshold.setStatus("current")
_Rm10010CfgStartuptablefive_ObjectIdentity = ObjectIdentity
rm10010CfgStartuptablefive = _Rm10010CfgStartuptablefive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 9, 6)
)
_Rm10010CfgOtxtlhcapabilitiesTable_Object = MibTable
rm10010CfgOtxtlhcapabilitiesTable = _Rm10010CfgOtxtlhcapabilitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 9, 6, 1)
)
if mibBuilder.loadTexts:
    rm10010CfgOtxtlhcapabilitiesTable.setStatus("current")
_Rm10010CfgOtxtlhcapabilitiesEntry_Object = MibTableRow
rm10010CfgOtxtlhcapabilitiesEntry = _Rm10010CfgOtxtlhcapabilitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 9, 6, 1, 1)
)
rm10010CfgOtxtlhcapabilitiesEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010CfgOtxtlhcapabilitiesIndex"),
)
if mibBuilder.loadTexts:
    rm10010CfgOtxtlhcapabilitiesEntry.setStatus("current")


class _Rm10010CfgOtxtlhcapabilitiesIndex_Type(Integer32):
    """Custom type rm10010CfgOtxtlhcapabilitiesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010CfgOtxtlhcapabilitiesIndex_Type.__name__ = "Integer32"
_Rm10010CfgOtxtlhcapabilitiesIndex_Object = MibTableColumn
rm10010CfgOtxtlhcapabilitiesIndex = _Rm10010CfgOtxtlhcapabilitiesIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 9, 6, 1, 1, 1),
    _Rm10010CfgOtxtlhcapabilitiesIndex_Type()
)
rm10010CfgOtxtlhcapabilitiesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CfgOtxtlhcapabilitiesIndex.setStatus("current")


class _Rm10010CfgComponentTypePortn_Type(Unsigned32):
    """Custom type rm10010CfgComponentTypePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010CfgComponentTypePortn_Type.__name__ = "Unsigned32"
_Rm10010CfgComponentTypePortn_Object = MibTableColumn
rm10010CfgComponentTypePortn = _Rm10010CfgComponentTypePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 9, 6, 1, 1, 3),
    _Rm10010CfgComponentTypePortn_Type()
)
rm10010CfgComponentTypePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CfgComponentTypePortn.setStatus("current")


class _Rm10010CfgMiscellaneousPortn_Type(Unsigned32):
    """Custom type rm10010CfgMiscellaneousPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010CfgMiscellaneousPortn_Type.__name__ = "Unsigned32"
_Rm10010CfgMiscellaneousPortn_Object = MibTableColumn
rm10010CfgMiscellaneousPortn = _Rm10010CfgMiscellaneousPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 9, 6, 1, 1, 4),
    _Rm10010CfgMiscellaneousPortn_Type()
)
rm10010CfgMiscellaneousPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CfgMiscellaneousPortn.setStatus("current")


class _Rm10010CfgFirstChannelPortn_Type(Unsigned32):
    """Custom type rm10010CfgFirstChannelPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010CfgFirstChannelPortn_Type.__name__ = "Unsigned32"
_Rm10010CfgFirstChannelPortn_Object = MibTableColumn
rm10010CfgFirstChannelPortn = _Rm10010CfgFirstChannelPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 9, 6, 1, 1, 5),
    _Rm10010CfgFirstChannelPortn_Type()
)
rm10010CfgFirstChannelPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CfgFirstChannelPortn.setStatus("current")


class _Rm10010CfgLastChannelPortn_Type(Unsigned32):
    """Custom type rm10010CfgLastChannelPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010CfgLastChannelPortn_Type.__name__ = "Unsigned32"
_Rm10010CfgLastChannelPortn_Object = MibTableColumn
rm10010CfgLastChannelPortn = _Rm10010CfgLastChannelPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 9, 6, 1, 1, 6),
    _Rm10010CfgLastChannelPortn_Type()
)
rm10010CfgLastChannelPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CfgLastChannelPortn.setStatus("current")


class _Rm10010CfgGridPortn_Type(Unsigned32):
    """Custom type rm10010CfgGridPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010CfgGridPortn_Type.__name__ = "Unsigned32"
_Rm10010CfgGridPortn_Object = MibTableColumn
rm10010CfgGridPortn = _Rm10010CfgGridPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 9, 6, 1, 1, 7),
    _Rm10010CfgGridPortn_Type()
)
rm10010CfgGridPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010CfgGridPortn.setStatus("current")
_Rm10010CfgWriteConfiguration_Type = EkiOnOff
_Rm10010CfgWriteConfiguration_Object = MibScalar
rm10010CfgWriteConfiguration = _Rm10010CfgWriteConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 9, 257),
    _Rm10010CfgWriteConfiguration_Type()
)
rm10010CfgWriteConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010CfgWriteConfiguration.setStatus("current")
_Rm10010traps_ObjectIdentity = ObjectIdentity
rm10010traps = _Rm10010traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 10)
)


class _Rm10010trapPortNumber_Type(Integer32):
    """Custom type rm10010trapPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Rm10010trapPortNumber_Type.__name__ = "Integer32"
_Rm10010trapPortNumber_Object = MibScalar
rm10010trapPortNumber = _Rm10010trapPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 10, 2),
    _Rm10010trapPortNumber_Type()
)
rm10010trapPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010trapPortNumber.setStatus("current")


class _Rm10010trapLineNumber_Type(Integer32):
    """Custom type rm10010trapLineNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Rm10010trapLineNumber_Type.__name__ = "Integer32"
_Rm10010trapLineNumber_Object = MibScalar
rm10010trapLineNumber = _Rm10010trapLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 10, 3),
    _Rm10010trapLineNumber_Type()
)
rm10010trapLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010trapLineNumber.setStatus("current")


class _Rm10010trapBoardNumber_Type(Integer32):
    """Custom type rm10010trapBoardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Rm10010trapBoardNumber_Type.__name__ = "Integer32"
_Rm10010trapBoardNumber_Object = MibScalar
rm10010trapBoardNumber = _Rm10010trapBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 10, 4),
    _Rm10010trapBoardNumber_Type()
)
rm10010trapBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010trapBoardNumber.setStatus("current")
_Rm10010Monitoring_ObjectIdentity = ObjectIdentity
rm10010Monitoring = _Rm10010Monitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11)
)
_Rm10010MonOther_ObjectIdentity = ObjectIdentity
rm10010MonOther = _Rm10010MonOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 1)
)
_Rm10010MonRmon_ObjectIdentity = ObjectIdentity
rm10010MonRmon = _Rm10010MonRmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 1, 3)
)
_Rm10010MonClient_ObjectIdentity = ObjectIdentity
rm10010MonClient = _Rm10010MonClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2)
)
_Rm10010MonClientRmonCounter_ObjectIdentity = ObjectIdentity
rm10010MonClientRmonCounter = _Rm10010MonClientRmonCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4)
)
_Rm10010MonupRmonBytesCounterClientInputTable_Object = MibTable
rm10010MonupRmonBytesCounterClientInputTable = _Rm10010MonupRmonBytesCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 16)
)
if mibBuilder.loadTexts:
    rm10010MonupRmonBytesCounterClientInputTable.setStatus("current")
_Rm10010MonupRmonBytesCounterClientInputEntry_Object = MibTableRow
rm10010MonupRmonBytesCounterClientInputEntry = _Rm10010MonupRmonBytesCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 16, 1)
)
rm10010MonupRmonBytesCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010MonupRmonBytesCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    rm10010MonupRmonBytesCounterClientInputEntry.setStatus("current")


class _Rm10010MonupRmonBytesCounterClientInputIndex_Type(Integer32):
    """Custom type rm10010MonupRmonBytesCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010MonupRmonBytesCounterClientInputIndex_Type.__name__ = "Integer32"
_Rm10010MonupRmonBytesCounterClientInputIndex_Object = MibTableColumn
rm10010MonupRmonBytesCounterClientInputIndex = _Rm10010MonupRmonBytesCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 16, 1, 1),
    _Rm10010MonupRmonBytesCounterClientInputIndex_Type()
)
rm10010MonupRmonBytesCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MonupRmonBytesCounterClientInputIndex.setStatus("current")
_Rm10010MonupRmonBytesCounterClientInputValuePortn_Type = Counter64
_Rm10010MonupRmonBytesCounterClientInputValuePortn_Object = MibTableColumn
rm10010MonupRmonBytesCounterClientInputValuePortn = _Rm10010MonupRmonBytesCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 16, 1, 2),
    _Rm10010MonupRmonBytesCounterClientInputValuePortn_Type()
)
rm10010MonupRmonBytesCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MonupRmonBytesCounterClientInputValuePortn.setStatus("current")
_Rm10010MonupRmonBytesCounterClientInputErrorPortn_Type = EkiOnOff
_Rm10010MonupRmonBytesCounterClientInputErrorPortn_Object = MibTableColumn
rm10010MonupRmonBytesCounterClientInputErrorPortn = _Rm10010MonupRmonBytesCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 16, 1, 3),
    _Rm10010MonupRmonBytesCounterClientInputErrorPortn_Type()
)
rm10010MonupRmonBytesCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MonupRmonBytesCounterClientInputErrorPortn.setStatus("current")
_Rm10010MonupRmonBytesCounterClientInputOverloadPortn_Type = EkiOnOff
_Rm10010MonupRmonBytesCounterClientInputOverloadPortn_Object = MibTableColumn
rm10010MonupRmonBytesCounterClientInputOverloadPortn = _Rm10010MonupRmonBytesCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 16, 1, 4),
    _Rm10010MonupRmonBytesCounterClientInputOverloadPortn_Type()
)
rm10010MonupRmonBytesCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MonupRmonBytesCounterClientInputOverloadPortn.setStatus("current")
_Rm10010MonupRmonCrcErrorsCounterClientInputTable_Object = MibTable
rm10010MonupRmonCrcErrorsCounterClientInputTable = _Rm10010MonupRmonCrcErrorsCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 32)
)
if mibBuilder.loadTexts:
    rm10010MonupRmonCrcErrorsCounterClientInputTable.setStatus("current")
_Rm10010MonupRmonCrcErrorsCounterClientInputEntry_Object = MibTableRow
rm10010MonupRmonCrcErrorsCounterClientInputEntry = _Rm10010MonupRmonCrcErrorsCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 32, 1)
)
rm10010MonupRmonCrcErrorsCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010MonupRmonCrcErrorsCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    rm10010MonupRmonCrcErrorsCounterClientInputEntry.setStatus("current")


class _Rm10010MonupRmonCrcErrorsCounterClientInputIndex_Type(Integer32):
    """Custom type rm10010MonupRmonCrcErrorsCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010MonupRmonCrcErrorsCounterClientInputIndex_Type.__name__ = "Integer32"
_Rm10010MonupRmonCrcErrorsCounterClientInputIndex_Object = MibTableColumn
rm10010MonupRmonCrcErrorsCounterClientInputIndex = _Rm10010MonupRmonCrcErrorsCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 32, 1, 1),
    _Rm10010MonupRmonCrcErrorsCounterClientInputIndex_Type()
)
rm10010MonupRmonCrcErrorsCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MonupRmonCrcErrorsCounterClientInputIndex.setStatus("current")
_Rm10010MonupRmonCrcErrorsCounterClientInputValuePortn_Type = Counter64
_Rm10010MonupRmonCrcErrorsCounterClientInputValuePortn_Object = MibTableColumn
rm10010MonupRmonCrcErrorsCounterClientInputValuePortn = _Rm10010MonupRmonCrcErrorsCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 32, 1, 2),
    _Rm10010MonupRmonCrcErrorsCounterClientInputValuePortn_Type()
)
rm10010MonupRmonCrcErrorsCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MonupRmonCrcErrorsCounterClientInputValuePortn.setStatus("current")
_Rm10010MonupRmonCrcErrorsCounterClientInputErrorPortn_Type = EkiOnOff
_Rm10010MonupRmonCrcErrorsCounterClientInputErrorPortn_Object = MibTableColumn
rm10010MonupRmonCrcErrorsCounterClientInputErrorPortn = _Rm10010MonupRmonCrcErrorsCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 32, 1, 3),
    _Rm10010MonupRmonCrcErrorsCounterClientInputErrorPortn_Type()
)
rm10010MonupRmonCrcErrorsCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MonupRmonCrcErrorsCounterClientInputErrorPortn.setStatus("current")
_Rm10010MonupRmonCrcErrorsCounterClientInputOverloadPortn_Type = EkiOnOff
_Rm10010MonupRmonCrcErrorsCounterClientInputOverloadPortn_Object = MibTableColumn
rm10010MonupRmonCrcErrorsCounterClientInputOverloadPortn = _Rm10010MonupRmonCrcErrorsCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 32, 1, 4),
    _Rm10010MonupRmonCrcErrorsCounterClientInputOverloadPortn_Type()
)
rm10010MonupRmonCrcErrorsCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MonupRmonCrcErrorsCounterClientInputOverloadPortn.setStatus("current")
_Rm10010MonupRmonPacketsCounterClientInputTable_Object = MibTable
rm10010MonupRmonPacketsCounterClientInputTable = _Rm10010MonupRmonPacketsCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 48)
)
if mibBuilder.loadTexts:
    rm10010MonupRmonPacketsCounterClientInputTable.setStatus("current")
_Rm10010MonupRmonPacketsCounterClientInputEntry_Object = MibTableRow
rm10010MonupRmonPacketsCounterClientInputEntry = _Rm10010MonupRmonPacketsCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 48, 1)
)
rm10010MonupRmonPacketsCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010MonupRmonPacketsCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    rm10010MonupRmonPacketsCounterClientInputEntry.setStatus("current")


class _Rm10010MonupRmonPacketsCounterClientInputIndex_Type(Integer32):
    """Custom type rm10010MonupRmonPacketsCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010MonupRmonPacketsCounterClientInputIndex_Type.__name__ = "Integer32"
_Rm10010MonupRmonPacketsCounterClientInputIndex_Object = MibTableColumn
rm10010MonupRmonPacketsCounterClientInputIndex = _Rm10010MonupRmonPacketsCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 48, 1, 1),
    _Rm10010MonupRmonPacketsCounterClientInputIndex_Type()
)
rm10010MonupRmonPacketsCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MonupRmonPacketsCounterClientInputIndex.setStatus("current")
_Rm10010MonupRmonPacketsCounterClientInputValuePortn_Type = Counter64
_Rm10010MonupRmonPacketsCounterClientInputValuePortn_Object = MibTableColumn
rm10010MonupRmonPacketsCounterClientInputValuePortn = _Rm10010MonupRmonPacketsCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 48, 1, 2),
    _Rm10010MonupRmonPacketsCounterClientInputValuePortn_Type()
)
rm10010MonupRmonPacketsCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MonupRmonPacketsCounterClientInputValuePortn.setStatus("current")
_Rm10010MonupRmonPacketsCounterClientInputErrorPortn_Type = EkiOnOff
_Rm10010MonupRmonPacketsCounterClientInputErrorPortn_Object = MibTableColumn
rm10010MonupRmonPacketsCounterClientInputErrorPortn = _Rm10010MonupRmonPacketsCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 48, 1, 3),
    _Rm10010MonupRmonPacketsCounterClientInputErrorPortn_Type()
)
rm10010MonupRmonPacketsCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MonupRmonPacketsCounterClientInputErrorPortn.setStatus("current")
_Rm10010MonupRmonPacketsCounterClientInputOverloadPortn_Type = EkiOnOff
_Rm10010MonupRmonPacketsCounterClientInputOverloadPortn_Object = MibTableColumn
rm10010MonupRmonPacketsCounterClientInputOverloadPortn = _Rm10010MonupRmonPacketsCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 48, 1, 4),
    _Rm10010MonupRmonPacketsCounterClientInputOverloadPortn_Type()
)
rm10010MonupRmonPacketsCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MonupRmonPacketsCounterClientInputOverloadPortn.setStatus("current")
_Rm10010MonupRmonBroadcastCounterClientInputTable_Object = MibTable
rm10010MonupRmonBroadcastCounterClientInputTable = _Rm10010MonupRmonBroadcastCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 64)
)
if mibBuilder.loadTexts:
    rm10010MonupRmonBroadcastCounterClientInputTable.setStatus("current")
_Rm10010MonupRmonBroadcastCounterClientInputEntry_Object = MibTableRow
rm10010MonupRmonBroadcastCounterClientInputEntry = _Rm10010MonupRmonBroadcastCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 64, 1)
)
rm10010MonupRmonBroadcastCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010MonupRmonBroadcastCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    rm10010MonupRmonBroadcastCounterClientInputEntry.setStatus("current")


class _Rm10010MonupRmonBroadcastCounterClientInputIndex_Type(Integer32):
    """Custom type rm10010MonupRmonBroadcastCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010MonupRmonBroadcastCounterClientInputIndex_Type.__name__ = "Integer32"
_Rm10010MonupRmonBroadcastCounterClientInputIndex_Object = MibTableColumn
rm10010MonupRmonBroadcastCounterClientInputIndex = _Rm10010MonupRmonBroadcastCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 64, 1, 1),
    _Rm10010MonupRmonBroadcastCounterClientInputIndex_Type()
)
rm10010MonupRmonBroadcastCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MonupRmonBroadcastCounterClientInputIndex.setStatus("current")
_Rm10010MonupRmonBroadcastCounterClientInputValuePortn_Type = Counter64
_Rm10010MonupRmonBroadcastCounterClientInputValuePortn_Object = MibTableColumn
rm10010MonupRmonBroadcastCounterClientInputValuePortn = _Rm10010MonupRmonBroadcastCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 64, 1, 2),
    _Rm10010MonupRmonBroadcastCounterClientInputValuePortn_Type()
)
rm10010MonupRmonBroadcastCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MonupRmonBroadcastCounterClientInputValuePortn.setStatus("current")
_Rm10010MonupRmonBroadcastCounterClientInputErrorPortn_Type = EkiOnOff
_Rm10010MonupRmonBroadcastCounterClientInputErrorPortn_Object = MibTableColumn
rm10010MonupRmonBroadcastCounterClientInputErrorPortn = _Rm10010MonupRmonBroadcastCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 64, 1, 3),
    _Rm10010MonupRmonBroadcastCounterClientInputErrorPortn_Type()
)
rm10010MonupRmonBroadcastCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MonupRmonBroadcastCounterClientInputErrorPortn.setStatus("current")
_Rm10010MonupRmonBroadcastCounterClientInputOverloadPortn_Type = EkiOnOff
_Rm10010MonupRmonBroadcastCounterClientInputOverloadPortn_Object = MibTableColumn
rm10010MonupRmonBroadcastCounterClientInputOverloadPortn = _Rm10010MonupRmonBroadcastCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 64, 1, 4),
    _Rm10010MonupRmonBroadcastCounterClientInputOverloadPortn_Type()
)
rm10010MonupRmonBroadcastCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MonupRmonBroadcastCounterClientInputOverloadPortn.setStatus("current")
_Rm10010MonupRmonMulticastCounterClientInputTable_Object = MibTable
rm10010MonupRmonMulticastCounterClientInputTable = _Rm10010MonupRmonMulticastCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 80)
)
if mibBuilder.loadTexts:
    rm10010MonupRmonMulticastCounterClientInputTable.setStatus("current")
_Rm10010MonupRmonMulticastCounterClientInputEntry_Object = MibTableRow
rm10010MonupRmonMulticastCounterClientInputEntry = _Rm10010MonupRmonMulticastCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 80, 1)
)
rm10010MonupRmonMulticastCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010MonupRmonMulticastCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    rm10010MonupRmonMulticastCounterClientInputEntry.setStatus("current")


class _Rm10010MonupRmonMulticastCounterClientInputIndex_Type(Integer32):
    """Custom type rm10010MonupRmonMulticastCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010MonupRmonMulticastCounterClientInputIndex_Type.__name__ = "Integer32"
_Rm10010MonupRmonMulticastCounterClientInputIndex_Object = MibTableColumn
rm10010MonupRmonMulticastCounterClientInputIndex = _Rm10010MonupRmonMulticastCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 80, 1, 1),
    _Rm10010MonupRmonMulticastCounterClientInputIndex_Type()
)
rm10010MonupRmonMulticastCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MonupRmonMulticastCounterClientInputIndex.setStatus("current")
_Rm10010MonupRmonMulticastCounterClientInputValuePortn_Type = Counter64
_Rm10010MonupRmonMulticastCounterClientInputValuePortn_Object = MibTableColumn
rm10010MonupRmonMulticastCounterClientInputValuePortn = _Rm10010MonupRmonMulticastCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 80, 1, 2),
    _Rm10010MonupRmonMulticastCounterClientInputValuePortn_Type()
)
rm10010MonupRmonMulticastCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MonupRmonMulticastCounterClientInputValuePortn.setStatus("current")
_Rm10010MonupRmonMulticastCounterClientInputErrorPortn_Type = EkiOnOff
_Rm10010MonupRmonMulticastCounterClientInputErrorPortn_Object = MibTableColumn
rm10010MonupRmonMulticastCounterClientInputErrorPortn = _Rm10010MonupRmonMulticastCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 80, 1, 3),
    _Rm10010MonupRmonMulticastCounterClientInputErrorPortn_Type()
)
rm10010MonupRmonMulticastCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MonupRmonMulticastCounterClientInputErrorPortn.setStatus("current")
_Rm10010MonupRmonMulticastCounterClientInputOverloadPortn_Type = EkiOnOff
_Rm10010MonupRmonMulticastCounterClientInputOverloadPortn_Object = MibTableColumn
rm10010MonupRmonMulticastCounterClientInputOverloadPortn = _Rm10010MonupRmonMulticastCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 80, 1, 4),
    _Rm10010MonupRmonMulticastCounterClientInputOverloadPortn_Type()
)
rm10010MonupRmonMulticastCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MonupRmonMulticastCounterClientInputOverloadPortn.setStatus("current")
_Rm10010MonupRmonPauseFrameCounterClientInputTable_Object = MibTable
rm10010MonupRmonPauseFrameCounterClientInputTable = _Rm10010MonupRmonPauseFrameCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 96)
)
if mibBuilder.loadTexts:
    rm10010MonupRmonPauseFrameCounterClientInputTable.setStatus("current")
_Rm10010MonupRmonPauseFrameCounterClientInputEntry_Object = MibTableRow
rm10010MonupRmonPauseFrameCounterClientInputEntry = _Rm10010MonupRmonPauseFrameCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 96, 1)
)
rm10010MonupRmonPauseFrameCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010MonupRmonPauseFrameCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    rm10010MonupRmonPauseFrameCounterClientInputEntry.setStatus("current")


class _Rm10010MonupRmonPauseFrameCounterClientInputIndex_Type(Integer32):
    """Custom type rm10010MonupRmonPauseFrameCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010MonupRmonPauseFrameCounterClientInputIndex_Type.__name__ = "Integer32"
_Rm10010MonupRmonPauseFrameCounterClientInputIndex_Object = MibTableColumn
rm10010MonupRmonPauseFrameCounterClientInputIndex = _Rm10010MonupRmonPauseFrameCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 96, 1, 1),
    _Rm10010MonupRmonPauseFrameCounterClientInputIndex_Type()
)
rm10010MonupRmonPauseFrameCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MonupRmonPauseFrameCounterClientInputIndex.setStatus("current")
_Rm10010MonupRmonPauseFrameCounterClientInputValuePortn_Type = Counter64
_Rm10010MonupRmonPauseFrameCounterClientInputValuePortn_Object = MibTableColumn
rm10010MonupRmonPauseFrameCounterClientInputValuePortn = _Rm10010MonupRmonPauseFrameCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 96, 1, 2),
    _Rm10010MonupRmonPauseFrameCounterClientInputValuePortn_Type()
)
rm10010MonupRmonPauseFrameCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MonupRmonPauseFrameCounterClientInputValuePortn.setStatus("current")
_Rm10010MonupRmonPauseFrameCounterClientInputErrorPortn_Type = EkiOnOff
_Rm10010MonupRmonPauseFrameCounterClientInputErrorPortn_Object = MibTableColumn
rm10010MonupRmonPauseFrameCounterClientInputErrorPortn = _Rm10010MonupRmonPauseFrameCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 96, 1, 3),
    _Rm10010MonupRmonPauseFrameCounterClientInputErrorPortn_Type()
)
rm10010MonupRmonPauseFrameCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MonupRmonPauseFrameCounterClientInputErrorPortn.setStatus("current")
_Rm10010MonupRmonPauseFrameCounterClientInputOverloadPortn_Type = EkiOnOff
_Rm10010MonupRmonPauseFrameCounterClientInputOverloadPortn_Object = MibTableColumn
rm10010MonupRmonPauseFrameCounterClientInputOverloadPortn = _Rm10010MonupRmonPauseFrameCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 96, 1, 4),
    _Rm10010MonupRmonPauseFrameCounterClientInputOverloadPortn_Type()
)
rm10010MonupRmonPauseFrameCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MonupRmonPauseFrameCounterClientInputOverloadPortn.setStatus("current")
_Rm10010MonupRmonUnicastCounterClientInputTable_Object = MibTable
rm10010MonupRmonUnicastCounterClientInputTable = _Rm10010MonupRmonUnicastCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 160)
)
if mibBuilder.loadTexts:
    rm10010MonupRmonUnicastCounterClientInputTable.setStatus("current")
_Rm10010MonupRmonUnicastCounterClientInputEntry_Object = MibTableRow
rm10010MonupRmonUnicastCounterClientInputEntry = _Rm10010MonupRmonUnicastCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 160, 1)
)
rm10010MonupRmonUnicastCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010MonupRmonUnicastCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    rm10010MonupRmonUnicastCounterClientInputEntry.setStatus("current")


class _Rm10010MonupRmonUnicastCounterClientInputIndex_Type(Integer32):
    """Custom type rm10010MonupRmonUnicastCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010MonupRmonUnicastCounterClientInputIndex_Type.__name__ = "Integer32"
_Rm10010MonupRmonUnicastCounterClientInputIndex_Object = MibTableColumn
rm10010MonupRmonUnicastCounterClientInputIndex = _Rm10010MonupRmonUnicastCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 160, 1, 1),
    _Rm10010MonupRmonUnicastCounterClientInputIndex_Type()
)
rm10010MonupRmonUnicastCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MonupRmonUnicastCounterClientInputIndex.setStatus("current")
_Rm10010MonupRmonUnicastCounterClientInputValuePortn_Type = Counter64
_Rm10010MonupRmonUnicastCounterClientInputValuePortn_Object = MibTableColumn
rm10010MonupRmonUnicastCounterClientInputValuePortn = _Rm10010MonupRmonUnicastCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 160, 1, 2),
    _Rm10010MonupRmonUnicastCounterClientInputValuePortn_Type()
)
rm10010MonupRmonUnicastCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MonupRmonUnicastCounterClientInputValuePortn.setStatus("current")
_Rm10010MonupRmonUnicastCounterClientInputErrorPortn_Type = EkiOnOff
_Rm10010MonupRmonUnicastCounterClientInputErrorPortn_Object = MibTableColumn
rm10010MonupRmonUnicastCounterClientInputErrorPortn = _Rm10010MonupRmonUnicastCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 160, 1, 3),
    _Rm10010MonupRmonUnicastCounterClientInputErrorPortn_Type()
)
rm10010MonupRmonUnicastCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MonupRmonUnicastCounterClientInputErrorPortn.setStatus("current")
_Rm10010MonupRmonUnicastCounterClientInputOverloadPortn_Type = EkiOnOff
_Rm10010MonupRmonUnicastCounterClientInputOverloadPortn_Object = MibTableColumn
rm10010MonupRmonUnicastCounterClientInputOverloadPortn = _Rm10010MonupRmonUnicastCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 160, 1, 4),
    _Rm10010MonupRmonUnicastCounterClientInputOverloadPortn_Type()
)
rm10010MonupRmonUnicastCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MonupRmonUnicastCounterClientInputOverloadPortn.setStatus("current")
_Rm10010MonupRmonNonunicastCounterClientInputTable_Object = MibTable
rm10010MonupRmonNonunicastCounterClientInputTable = _Rm10010MonupRmonNonunicastCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 176)
)
if mibBuilder.loadTexts:
    rm10010MonupRmonNonunicastCounterClientInputTable.setStatus("current")
_Rm10010MonupRmonNonunicastCounterClientInputEntry_Object = MibTableRow
rm10010MonupRmonNonunicastCounterClientInputEntry = _Rm10010MonupRmonNonunicastCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 176, 1)
)
rm10010MonupRmonNonunicastCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010MonupRmonNonunicastCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    rm10010MonupRmonNonunicastCounterClientInputEntry.setStatus("current")


class _Rm10010MonupRmonNonunicastCounterClientInputIndex_Type(Integer32):
    """Custom type rm10010MonupRmonNonunicastCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010MonupRmonNonunicastCounterClientInputIndex_Type.__name__ = "Integer32"
_Rm10010MonupRmonNonunicastCounterClientInputIndex_Object = MibTableColumn
rm10010MonupRmonNonunicastCounterClientInputIndex = _Rm10010MonupRmonNonunicastCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 176, 1, 1),
    _Rm10010MonupRmonNonunicastCounterClientInputIndex_Type()
)
rm10010MonupRmonNonunicastCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MonupRmonNonunicastCounterClientInputIndex.setStatus("current")
_Rm10010MonupRmonNonunicastCounterClientInputValuePortn_Type = Counter64
_Rm10010MonupRmonNonunicastCounterClientInputValuePortn_Object = MibTableColumn
rm10010MonupRmonNonunicastCounterClientInputValuePortn = _Rm10010MonupRmonNonunicastCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 176, 1, 2),
    _Rm10010MonupRmonNonunicastCounterClientInputValuePortn_Type()
)
rm10010MonupRmonNonunicastCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MonupRmonNonunicastCounterClientInputValuePortn.setStatus("current")
_Rm10010MonupRmonNonunicastCounterClientInputErrorPortn_Type = EkiOnOff
_Rm10010MonupRmonNonunicastCounterClientInputErrorPortn_Object = MibTableColumn
rm10010MonupRmonNonunicastCounterClientInputErrorPortn = _Rm10010MonupRmonNonunicastCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 176, 1, 3),
    _Rm10010MonupRmonNonunicastCounterClientInputErrorPortn_Type()
)
rm10010MonupRmonNonunicastCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MonupRmonNonunicastCounterClientInputErrorPortn.setStatus("current")
_Rm10010MonupRmonNonunicastCounterClientInputOverloadPortn_Type = EkiOnOff
_Rm10010MonupRmonNonunicastCounterClientInputOverloadPortn_Object = MibTableColumn
rm10010MonupRmonNonunicastCounterClientInputOverloadPortn = _Rm10010MonupRmonNonunicastCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 176, 1, 4),
    _Rm10010MonupRmonNonunicastCounterClientInputOverloadPortn_Type()
)
rm10010MonupRmonNonunicastCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MonupRmonNonunicastCounterClientInputOverloadPortn.setStatus("current")
_Rm10010MondownRmonBytesCounterClientOutputTable_Object = MibTable
rm10010MondownRmonBytesCounterClientOutputTable = _Rm10010MondownRmonBytesCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 208)
)
if mibBuilder.loadTexts:
    rm10010MondownRmonBytesCounterClientOutputTable.setStatus("current")
_Rm10010MondownRmonBytesCounterClientOutputEntry_Object = MibTableRow
rm10010MondownRmonBytesCounterClientOutputEntry = _Rm10010MondownRmonBytesCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 208, 1)
)
rm10010MondownRmonBytesCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010MondownRmonBytesCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    rm10010MondownRmonBytesCounterClientOutputEntry.setStatus("current")


class _Rm10010MondownRmonBytesCounterClientOutputIndex_Type(Integer32):
    """Custom type rm10010MondownRmonBytesCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010MondownRmonBytesCounterClientOutputIndex_Type.__name__ = "Integer32"
_Rm10010MondownRmonBytesCounterClientOutputIndex_Object = MibTableColumn
rm10010MondownRmonBytesCounterClientOutputIndex = _Rm10010MondownRmonBytesCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 208, 1, 1),
    _Rm10010MondownRmonBytesCounterClientOutputIndex_Type()
)
rm10010MondownRmonBytesCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MondownRmonBytesCounterClientOutputIndex.setStatus("current")
_Rm10010MondownRmonBytesCounterClientOutputValuePortn_Type = Counter64
_Rm10010MondownRmonBytesCounterClientOutputValuePortn_Object = MibTableColumn
rm10010MondownRmonBytesCounterClientOutputValuePortn = _Rm10010MondownRmonBytesCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 208, 1, 2),
    _Rm10010MondownRmonBytesCounterClientOutputValuePortn_Type()
)
rm10010MondownRmonBytesCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MondownRmonBytesCounterClientOutputValuePortn.setStatus("current")
_Rm10010MondownRmonBytesCounterClientOutputErrorPortn_Type = EkiOnOff
_Rm10010MondownRmonBytesCounterClientOutputErrorPortn_Object = MibTableColumn
rm10010MondownRmonBytesCounterClientOutputErrorPortn = _Rm10010MondownRmonBytesCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 208, 1, 3),
    _Rm10010MondownRmonBytesCounterClientOutputErrorPortn_Type()
)
rm10010MondownRmonBytesCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MondownRmonBytesCounterClientOutputErrorPortn.setStatus("current")
_Rm10010MondownRmonBytesCounterClientOutputOverloadPortn_Type = EkiOnOff
_Rm10010MondownRmonBytesCounterClientOutputOverloadPortn_Object = MibTableColumn
rm10010MondownRmonBytesCounterClientOutputOverloadPortn = _Rm10010MondownRmonBytesCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 208, 1, 4),
    _Rm10010MondownRmonBytesCounterClientOutputOverloadPortn_Type()
)
rm10010MondownRmonBytesCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MondownRmonBytesCounterClientOutputOverloadPortn.setStatus("current")
_Rm10010MondownRmonCrcErrorsCounterClientOutputTable_Object = MibTable
rm10010MondownRmonCrcErrorsCounterClientOutputTable = _Rm10010MondownRmonCrcErrorsCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 224)
)
if mibBuilder.loadTexts:
    rm10010MondownRmonCrcErrorsCounterClientOutputTable.setStatus("current")
_Rm10010MondownRmonCrcErrorsCounterClientOutputEntry_Object = MibTableRow
rm10010MondownRmonCrcErrorsCounterClientOutputEntry = _Rm10010MondownRmonCrcErrorsCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 224, 1)
)
rm10010MondownRmonCrcErrorsCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010MondownRmonCrcErrorsCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    rm10010MondownRmonCrcErrorsCounterClientOutputEntry.setStatus("current")


class _Rm10010MondownRmonCrcErrorsCounterClientOutputIndex_Type(Integer32):
    """Custom type rm10010MondownRmonCrcErrorsCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010MondownRmonCrcErrorsCounterClientOutputIndex_Type.__name__ = "Integer32"
_Rm10010MondownRmonCrcErrorsCounterClientOutputIndex_Object = MibTableColumn
rm10010MondownRmonCrcErrorsCounterClientOutputIndex = _Rm10010MondownRmonCrcErrorsCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 224, 1, 1),
    _Rm10010MondownRmonCrcErrorsCounterClientOutputIndex_Type()
)
rm10010MondownRmonCrcErrorsCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MondownRmonCrcErrorsCounterClientOutputIndex.setStatus("current")
_Rm10010MondownRmonCrcErrorsCounterClientOutputValuePortn_Type = Counter64
_Rm10010MondownRmonCrcErrorsCounterClientOutputValuePortn_Object = MibTableColumn
rm10010MondownRmonCrcErrorsCounterClientOutputValuePortn = _Rm10010MondownRmonCrcErrorsCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 224, 1, 2),
    _Rm10010MondownRmonCrcErrorsCounterClientOutputValuePortn_Type()
)
rm10010MondownRmonCrcErrorsCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MondownRmonCrcErrorsCounterClientOutputValuePortn.setStatus("current")
_Rm10010MondownRmonCrcErrorsCounterClientOutputErrorPortn_Type = EkiOnOff
_Rm10010MondownRmonCrcErrorsCounterClientOutputErrorPortn_Object = MibTableColumn
rm10010MondownRmonCrcErrorsCounterClientOutputErrorPortn = _Rm10010MondownRmonCrcErrorsCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 224, 1, 3),
    _Rm10010MondownRmonCrcErrorsCounterClientOutputErrorPortn_Type()
)
rm10010MondownRmonCrcErrorsCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MondownRmonCrcErrorsCounterClientOutputErrorPortn.setStatus("current")
_Rm10010MondownRmonCrcErrorsCounterClientOutputOverloadPortn_Type = EkiOnOff
_Rm10010MondownRmonCrcErrorsCounterClientOutputOverloadPortn_Object = MibTableColumn
rm10010MondownRmonCrcErrorsCounterClientOutputOverloadPortn = _Rm10010MondownRmonCrcErrorsCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 224, 1, 4),
    _Rm10010MondownRmonCrcErrorsCounterClientOutputOverloadPortn_Type()
)
rm10010MondownRmonCrcErrorsCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MondownRmonCrcErrorsCounterClientOutputOverloadPortn.setStatus("current")
_Rm10010MondownRmonPacketsCounterClientOutputTable_Object = MibTable
rm10010MondownRmonPacketsCounterClientOutputTable = _Rm10010MondownRmonPacketsCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 240)
)
if mibBuilder.loadTexts:
    rm10010MondownRmonPacketsCounterClientOutputTable.setStatus("current")
_Rm10010MondownRmonPacketsCounterClientOutputEntry_Object = MibTableRow
rm10010MondownRmonPacketsCounterClientOutputEntry = _Rm10010MondownRmonPacketsCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 240, 1)
)
rm10010MondownRmonPacketsCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010MondownRmonPacketsCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    rm10010MondownRmonPacketsCounterClientOutputEntry.setStatus("current")


class _Rm10010MondownRmonPacketsCounterClientOutputIndex_Type(Integer32):
    """Custom type rm10010MondownRmonPacketsCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010MondownRmonPacketsCounterClientOutputIndex_Type.__name__ = "Integer32"
_Rm10010MondownRmonPacketsCounterClientOutputIndex_Object = MibTableColumn
rm10010MondownRmonPacketsCounterClientOutputIndex = _Rm10010MondownRmonPacketsCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 240, 1, 1),
    _Rm10010MondownRmonPacketsCounterClientOutputIndex_Type()
)
rm10010MondownRmonPacketsCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MondownRmonPacketsCounterClientOutputIndex.setStatus("current")
_Rm10010MondownRmonPacketsCounterClientOutputValuePortn_Type = Counter64
_Rm10010MondownRmonPacketsCounterClientOutputValuePortn_Object = MibTableColumn
rm10010MondownRmonPacketsCounterClientOutputValuePortn = _Rm10010MondownRmonPacketsCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 240, 1, 2),
    _Rm10010MondownRmonPacketsCounterClientOutputValuePortn_Type()
)
rm10010MondownRmonPacketsCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MondownRmonPacketsCounterClientOutputValuePortn.setStatus("current")
_Rm10010MondownRmonPacketsCounterClientOutputErrorPortn_Type = EkiOnOff
_Rm10010MondownRmonPacketsCounterClientOutputErrorPortn_Object = MibTableColumn
rm10010MondownRmonPacketsCounterClientOutputErrorPortn = _Rm10010MondownRmonPacketsCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 240, 1, 3),
    _Rm10010MondownRmonPacketsCounterClientOutputErrorPortn_Type()
)
rm10010MondownRmonPacketsCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MondownRmonPacketsCounterClientOutputErrorPortn.setStatus("current")
_Rm10010MondownRmonPacketsCounterClientOutputOverloadPortn_Type = EkiOnOff
_Rm10010MondownRmonPacketsCounterClientOutputOverloadPortn_Object = MibTableColumn
rm10010MondownRmonPacketsCounterClientOutputOverloadPortn = _Rm10010MondownRmonPacketsCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 240, 1, 4),
    _Rm10010MondownRmonPacketsCounterClientOutputOverloadPortn_Type()
)
rm10010MondownRmonPacketsCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MondownRmonPacketsCounterClientOutputOverloadPortn.setStatus("current")
_Rm10010MondownRmonBroadcastCounterClientOutputTable_Object = MibTable
rm10010MondownRmonBroadcastCounterClientOutputTable = _Rm10010MondownRmonBroadcastCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 256)
)
if mibBuilder.loadTexts:
    rm10010MondownRmonBroadcastCounterClientOutputTable.setStatus("current")
_Rm10010MondownRmonBroadcastCounterClientOutputEntry_Object = MibTableRow
rm10010MondownRmonBroadcastCounterClientOutputEntry = _Rm10010MondownRmonBroadcastCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 256, 1)
)
rm10010MondownRmonBroadcastCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010MondownRmonBroadcastCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    rm10010MondownRmonBroadcastCounterClientOutputEntry.setStatus("current")


class _Rm10010MondownRmonBroadcastCounterClientOutputIndex_Type(Integer32):
    """Custom type rm10010MondownRmonBroadcastCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010MondownRmonBroadcastCounterClientOutputIndex_Type.__name__ = "Integer32"
_Rm10010MondownRmonBroadcastCounterClientOutputIndex_Object = MibTableColumn
rm10010MondownRmonBroadcastCounterClientOutputIndex = _Rm10010MondownRmonBroadcastCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 256, 1, 1),
    _Rm10010MondownRmonBroadcastCounterClientOutputIndex_Type()
)
rm10010MondownRmonBroadcastCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MondownRmonBroadcastCounterClientOutputIndex.setStatus("current")
_Rm10010MondownRmonBroadcastCounterClientOutputValuePortn_Type = Counter64
_Rm10010MondownRmonBroadcastCounterClientOutputValuePortn_Object = MibTableColumn
rm10010MondownRmonBroadcastCounterClientOutputValuePortn = _Rm10010MondownRmonBroadcastCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 256, 1, 2),
    _Rm10010MondownRmonBroadcastCounterClientOutputValuePortn_Type()
)
rm10010MondownRmonBroadcastCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MondownRmonBroadcastCounterClientOutputValuePortn.setStatus("current")
_Rm10010MondownRmonBroadcastCounterClientOutputErrorPortn_Type = EkiOnOff
_Rm10010MondownRmonBroadcastCounterClientOutputErrorPortn_Object = MibTableColumn
rm10010MondownRmonBroadcastCounterClientOutputErrorPortn = _Rm10010MondownRmonBroadcastCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 256, 1, 3),
    _Rm10010MondownRmonBroadcastCounterClientOutputErrorPortn_Type()
)
rm10010MondownRmonBroadcastCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MondownRmonBroadcastCounterClientOutputErrorPortn.setStatus("current")
_Rm10010MondownRmonBroadcastCounterClientOutputOverloadPortn_Type = EkiOnOff
_Rm10010MondownRmonBroadcastCounterClientOutputOverloadPortn_Object = MibTableColumn
rm10010MondownRmonBroadcastCounterClientOutputOverloadPortn = _Rm10010MondownRmonBroadcastCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 256, 1, 4),
    _Rm10010MondownRmonBroadcastCounterClientOutputOverloadPortn_Type()
)
rm10010MondownRmonBroadcastCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MondownRmonBroadcastCounterClientOutputOverloadPortn.setStatus("current")
_Rm10010MondownRmonMulticastCounterClientOutputTable_Object = MibTable
rm10010MondownRmonMulticastCounterClientOutputTable = _Rm10010MondownRmonMulticastCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 272)
)
if mibBuilder.loadTexts:
    rm10010MondownRmonMulticastCounterClientOutputTable.setStatus("current")
_Rm10010MondownRmonMulticastCounterClientOutputEntry_Object = MibTableRow
rm10010MondownRmonMulticastCounterClientOutputEntry = _Rm10010MondownRmonMulticastCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 272, 1)
)
rm10010MondownRmonMulticastCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010MondownRmonMulticastCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    rm10010MondownRmonMulticastCounterClientOutputEntry.setStatus("current")


class _Rm10010MondownRmonMulticastCounterClientOutputIndex_Type(Integer32):
    """Custom type rm10010MondownRmonMulticastCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010MondownRmonMulticastCounterClientOutputIndex_Type.__name__ = "Integer32"
_Rm10010MondownRmonMulticastCounterClientOutputIndex_Object = MibTableColumn
rm10010MondownRmonMulticastCounterClientOutputIndex = _Rm10010MondownRmonMulticastCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 272, 1, 1),
    _Rm10010MondownRmonMulticastCounterClientOutputIndex_Type()
)
rm10010MondownRmonMulticastCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MondownRmonMulticastCounterClientOutputIndex.setStatus("current")
_Rm10010MondownRmonMulticastCounterClientOutputValuePortn_Type = Counter64
_Rm10010MondownRmonMulticastCounterClientOutputValuePortn_Object = MibTableColumn
rm10010MondownRmonMulticastCounterClientOutputValuePortn = _Rm10010MondownRmonMulticastCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 272, 1, 2),
    _Rm10010MondownRmonMulticastCounterClientOutputValuePortn_Type()
)
rm10010MondownRmonMulticastCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MondownRmonMulticastCounterClientOutputValuePortn.setStatus("current")
_Rm10010MondownRmonMulticastCounterClientOutputErrorPortn_Type = EkiOnOff
_Rm10010MondownRmonMulticastCounterClientOutputErrorPortn_Object = MibTableColumn
rm10010MondownRmonMulticastCounterClientOutputErrorPortn = _Rm10010MondownRmonMulticastCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 272, 1, 3),
    _Rm10010MondownRmonMulticastCounterClientOutputErrorPortn_Type()
)
rm10010MondownRmonMulticastCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MondownRmonMulticastCounterClientOutputErrorPortn.setStatus("current")
_Rm10010MondownRmonMulticastCounterClientOutputOverloadPortn_Type = EkiOnOff
_Rm10010MondownRmonMulticastCounterClientOutputOverloadPortn_Object = MibTableColumn
rm10010MondownRmonMulticastCounterClientOutputOverloadPortn = _Rm10010MondownRmonMulticastCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 272, 1, 4),
    _Rm10010MondownRmonMulticastCounterClientOutputOverloadPortn_Type()
)
rm10010MondownRmonMulticastCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MondownRmonMulticastCounterClientOutputOverloadPortn.setStatus("current")
_Rm10010MondownRmonPauseFrameCounterClientOutputTable_Object = MibTable
rm10010MondownRmonPauseFrameCounterClientOutputTable = _Rm10010MondownRmonPauseFrameCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 288)
)
if mibBuilder.loadTexts:
    rm10010MondownRmonPauseFrameCounterClientOutputTable.setStatus("current")
_Rm10010MondownRmonPauseFrameCounterClientOutputEntry_Object = MibTableRow
rm10010MondownRmonPauseFrameCounterClientOutputEntry = _Rm10010MondownRmonPauseFrameCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 288, 1)
)
rm10010MondownRmonPauseFrameCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010MondownRmonPauseFrameCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    rm10010MondownRmonPauseFrameCounterClientOutputEntry.setStatus("current")


class _Rm10010MondownRmonPauseFrameCounterClientOutputIndex_Type(Integer32):
    """Custom type rm10010MondownRmonPauseFrameCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010MondownRmonPauseFrameCounterClientOutputIndex_Type.__name__ = "Integer32"
_Rm10010MondownRmonPauseFrameCounterClientOutputIndex_Object = MibTableColumn
rm10010MondownRmonPauseFrameCounterClientOutputIndex = _Rm10010MondownRmonPauseFrameCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 288, 1, 1),
    _Rm10010MondownRmonPauseFrameCounterClientOutputIndex_Type()
)
rm10010MondownRmonPauseFrameCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MondownRmonPauseFrameCounterClientOutputIndex.setStatus("current")
_Rm10010MondownRmonPauseFrameCounterClientOutputValuePortn_Type = Counter64
_Rm10010MondownRmonPauseFrameCounterClientOutputValuePortn_Object = MibTableColumn
rm10010MondownRmonPauseFrameCounterClientOutputValuePortn = _Rm10010MondownRmonPauseFrameCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 288, 1, 2),
    _Rm10010MondownRmonPauseFrameCounterClientOutputValuePortn_Type()
)
rm10010MondownRmonPauseFrameCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MondownRmonPauseFrameCounterClientOutputValuePortn.setStatus("current")
_Rm10010MondownRmonPauseFrameCounterClientOutputErrorPortn_Type = EkiOnOff
_Rm10010MondownRmonPauseFrameCounterClientOutputErrorPortn_Object = MibTableColumn
rm10010MondownRmonPauseFrameCounterClientOutputErrorPortn = _Rm10010MondownRmonPauseFrameCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 288, 1, 3),
    _Rm10010MondownRmonPauseFrameCounterClientOutputErrorPortn_Type()
)
rm10010MondownRmonPauseFrameCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MondownRmonPauseFrameCounterClientOutputErrorPortn.setStatus("current")
_Rm10010MondownRmonPauseFrameCounterClientOutputOverloadPortn_Type = EkiOnOff
_Rm10010MondownRmonPauseFrameCounterClientOutputOverloadPortn_Object = MibTableColumn
rm10010MondownRmonPauseFrameCounterClientOutputOverloadPortn = _Rm10010MondownRmonPauseFrameCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 288, 1, 4),
    _Rm10010MondownRmonPauseFrameCounterClientOutputOverloadPortn_Type()
)
rm10010MondownRmonPauseFrameCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MondownRmonPauseFrameCounterClientOutputOverloadPortn.setStatus("current")
_Rm10010MondownRmonUnicastCounterClientOutputTable_Object = MibTable
rm10010MondownRmonUnicastCounterClientOutputTable = _Rm10010MondownRmonUnicastCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 352)
)
if mibBuilder.loadTexts:
    rm10010MondownRmonUnicastCounterClientOutputTable.setStatus("current")
_Rm10010MondownRmonUnicastCounterClientOutputEntry_Object = MibTableRow
rm10010MondownRmonUnicastCounterClientOutputEntry = _Rm10010MondownRmonUnicastCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 352, 1)
)
rm10010MondownRmonUnicastCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010MondownRmonUnicastCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    rm10010MondownRmonUnicastCounterClientOutputEntry.setStatus("current")


class _Rm10010MondownRmonUnicastCounterClientOutputIndex_Type(Integer32):
    """Custom type rm10010MondownRmonUnicastCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010MondownRmonUnicastCounterClientOutputIndex_Type.__name__ = "Integer32"
_Rm10010MondownRmonUnicastCounterClientOutputIndex_Object = MibTableColumn
rm10010MondownRmonUnicastCounterClientOutputIndex = _Rm10010MondownRmonUnicastCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 352, 1, 1),
    _Rm10010MondownRmonUnicastCounterClientOutputIndex_Type()
)
rm10010MondownRmonUnicastCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MondownRmonUnicastCounterClientOutputIndex.setStatus("current")
_Rm10010MondownRmonUnicastCounterClientOutputValuePortn_Type = Counter64
_Rm10010MondownRmonUnicastCounterClientOutputValuePortn_Object = MibTableColumn
rm10010MondownRmonUnicastCounterClientOutputValuePortn = _Rm10010MondownRmonUnicastCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 352, 1, 2),
    _Rm10010MondownRmonUnicastCounterClientOutputValuePortn_Type()
)
rm10010MondownRmonUnicastCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MondownRmonUnicastCounterClientOutputValuePortn.setStatus("current")
_Rm10010MondownRmonUnicastCounterClientOutputErrorPortn_Type = EkiOnOff
_Rm10010MondownRmonUnicastCounterClientOutputErrorPortn_Object = MibTableColumn
rm10010MondownRmonUnicastCounterClientOutputErrorPortn = _Rm10010MondownRmonUnicastCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 352, 1, 3),
    _Rm10010MondownRmonUnicastCounterClientOutputErrorPortn_Type()
)
rm10010MondownRmonUnicastCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MondownRmonUnicastCounterClientOutputErrorPortn.setStatus("current")
_Rm10010MondownRmonUnicastCounterClientOutputOverloadPortn_Type = EkiOnOff
_Rm10010MondownRmonUnicastCounterClientOutputOverloadPortn_Object = MibTableColumn
rm10010MondownRmonUnicastCounterClientOutputOverloadPortn = _Rm10010MondownRmonUnicastCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 352, 1, 4),
    _Rm10010MondownRmonUnicastCounterClientOutputOverloadPortn_Type()
)
rm10010MondownRmonUnicastCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MondownRmonUnicastCounterClientOutputOverloadPortn.setStatus("current")
_Rm10010MondownRmonNonunicastCounterClientOutputTable_Object = MibTable
rm10010MondownRmonNonunicastCounterClientOutputTable = _Rm10010MondownRmonNonunicastCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 368)
)
if mibBuilder.loadTexts:
    rm10010MondownRmonNonunicastCounterClientOutputTable.setStatus("current")
_Rm10010MondownRmonNonunicastCounterClientOutputEntry_Object = MibTableRow
rm10010MondownRmonNonunicastCounterClientOutputEntry = _Rm10010MondownRmonNonunicastCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 368, 1)
)
rm10010MondownRmonNonunicastCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010MondownRmonNonunicastCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    rm10010MondownRmonNonunicastCounterClientOutputEntry.setStatus("current")


class _Rm10010MondownRmonNonunicastCounterClientOutputIndex_Type(Integer32):
    """Custom type rm10010MondownRmonNonunicastCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010MondownRmonNonunicastCounterClientOutputIndex_Type.__name__ = "Integer32"
_Rm10010MondownRmonNonunicastCounterClientOutputIndex_Object = MibTableColumn
rm10010MondownRmonNonunicastCounterClientOutputIndex = _Rm10010MondownRmonNonunicastCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 368, 1, 1),
    _Rm10010MondownRmonNonunicastCounterClientOutputIndex_Type()
)
rm10010MondownRmonNonunicastCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MondownRmonNonunicastCounterClientOutputIndex.setStatus("current")
_Rm10010MondownRmonNonunicastCounterClientOutputValuePortn_Type = Counter64
_Rm10010MondownRmonNonunicastCounterClientOutputValuePortn_Object = MibTableColumn
rm10010MondownRmonNonunicastCounterClientOutputValuePortn = _Rm10010MondownRmonNonunicastCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 368, 1, 2),
    _Rm10010MondownRmonNonunicastCounterClientOutputValuePortn_Type()
)
rm10010MondownRmonNonunicastCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MondownRmonNonunicastCounterClientOutputValuePortn.setStatus("current")
_Rm10010MondownRmonNonunicastCounterClientOutputErrorPortn_Type = EkiOnOff
_Rm10010MondownRmonNonunicastCounterClientOutputErrorPortn_Object = MibTableColumn
rm10010MondownRmonNonunicastCounterClientOutputErrorPortn = _Rm10010MondownRmonNonunicastCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 368, 1, 3),
    _Rm10010MondownRmonNonunicastCounterClientOutputErrorPortn_Type()
)
rm10010MondownRmonNonunicastCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MondownRmonNonunicastCounterClientOutputErrorPortn.setStatus("current")
_Rm10010MondownRmonNonunicastCounterClientOutputOverloadPortn_Type = EkiOnOff
_Rm10010MondownRmonNonunicastCounterClientOutputOverloadPortn_Object = MibTableColumn
rm10010MondownRmonNonunicastCounterClientOutputOverloadPortn = _Rm10010MondownRmonNonunicastCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 2, 4, 368, 1, 4),
    _Rm10010MondownRmonNonunicastCounterClientOutputOverloadPortn_Type()
)
rm10010MondownRmonNonunicastCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010MondownRmonNonunicastCounterClientOutputOverloadPortn.setStatus("current")
_Rm10010MonPerfOther_ObjectIdentity = ObjectIdentity
rm10010MonPerfOther = _Rm10010MonPerfOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 5)
)
_Rm10010MonPerfSync_ObjectIdentity = ObjectIdentity
rm10010MonPerfSync = _Rm10010MonPerfSync_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 5, 1)
)
_Rm10010PerfEnable_Type = EkiOnOff
_Rm10010PerfEnable_Object = MibScalar
rm10010PerfEnable = _Rm10010PerfEnable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 5, 1, 257),
    _Rm10010PerfEnable_Type()
)
rm10010PerfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010PerfEnable.setStatus("current")
_Rm10010Perf15minSync_Type = EkiOnOff
_Rm10010Perf15minSync_Object = MibScalar
rm10010Perf15minSync = _Rm10010Perf15minSync_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 5, 1, 259),
    _Rm10010Perf15minSync_Type()
)
rm10010Perf15minSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010Perf15minSync.setStatus("current")
_Rm10010Perf24hSync_Type = EkiOnOff
_Rm10010Perf24hSync_Object = MibScalar
rm10010Perf24hSync = _Rm10010Perf24hSync_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 5, 1, 260),
    _Rm10010Perf24hSync_Type()
)
rm10010Perf24hSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010Perf24hSync.setStatus("current")
_Rm10010MonPerfTimeStamp_ObjectIdentity = ObjectIdentity
rm10010MonPerfTimeStamp = _Rm10010MonPerfTimeStamp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 5, 2)
)
_Rm10010Perf15MinShort_Type = EkiOnOff
_Rm10010Perf15MinShort_Object = MibScalar
rm10010Perf15MinShort = _Rm10010Perf15MinShort_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 5, 2, 1),
    _Rm10010Perf15MinShort_Type()
)
rm10010Perf15MinShort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010Perf15MinShort.setStatus("current")
_Rm10010Perf15MinLong_Type = EkiOnOff
_Rm10010Perf15MinLong_Object = MibScalar
rm10010Perf15MinLong = _Rm10010Perf15MinLong_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 5, 2, 2),
    _Rm10010Perf15MinLong_Type()
)
rm10010Perf15MinLong.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010Perf15MinLong.setStatus("current")
_Rm10010Perf24HoursShort_Type = Counter32
_Rm10010Perf24HoursShort_Object = MibScalar
rm10010Perf24HoursShort = _Rm10010Perf24HoursShort_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 5, 2, 5),
    _Rm10010Perf24HoursShort_Type()
)
rm10010Perf24HoursShort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010Perf24HoursShort.setStatus("current")
_Rm10010Perf24HoursLong_Type = Counter32
_Rm10010Perf24HoursLong_Object = MibScalar
rm10010Perf24HoursLong = _Rm10010Perf24HoursLong_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 5, 2, 6),
    _Rm10010Perf24HoursLong_Type()
)
rm10010Perf24HoursLong.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010Perf24HoursLong.setStatus("current")
_Rm10010PerfCurrent15MinElapsedTime_Type = Counter32
_Rm10010PerfCurrent15MinElapsedTime_Object = MibScalar
rm10010PerfCurrent15MinElapsedTime = _Rm10010PerfCurrent15MinElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 5, 2, 7),
    _Rm10010PerfCurrent15MinElapsedTime_Type()
)
rm10010PerfCurrent15MinElapsedTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010PerfCurrent15MinElapsedTime.setStatus("current")
_Rm10010PerfCurrent24HoursElapsedTime_Type = Counter32
_Rm10010PerfCurrent24HoursElapsedTime_Object = MibScalar
rm10010PerfCurrent24HoursElapsedTime = _Rm10010PerfCurrent24HoursElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 5, 2, 8),
    _Rm10010PerfCurrent24HoursElapsedTime_Type()
)
rm10010PerfCurrent24HoursElapsedTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010PerfCurrent24HoursElapsedTime.setStatus("current")
_Rm10010MonPerfClient_ObjectIdentity = ObjectIdentity
rm10010MonPerfClient = _Rm10010MonPerfClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6)
)
_Rm10010PerfTelecomInputClientCurrent15StatTable_Object = MibTable
rm10010PerfTelecomInputClientCurrent15StatTable = _Rm10010PerfTelecomInputClientCurrent15StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 16)
)
if mibBuilder.loadTexts:
    rm10010PerfTelecomInputClientCurrent15StatTable.setStatus("current")
_Rm10010PerfTelecomInputClientCurrent15StatEntry_Object = MibTableRow
rm10010PerfTelecomInputClientCurrent15StatEntry = _Rm10010PerfTelecomInputClientCurrent15StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 16, 1)
)
rm10010PerfTelecomInputClientCurrent15StatEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010PerfTelecomInputClientCurrent15StatIndex"),
)
if mibBuilder.loadTexts:
    rm10010PerfTelecomInputClientCurrent15StatEntry.setStatus("current")


class _Rm10010PerfTelecomInputClientCurrent15StatIndex_Type(Integer32):
    """Custom type rm10010PerfTelecomInputClientCurrent15StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010PerfTelecomInputClientCurrent15StatIndex_Type.__name__ = "Integer32"
_Rm10010PerfTelecomInputClientCurrent15StatIndex_Object = MibTableColumn
rm10010PerfTelecomInputClientCurrent15StatIndex = _Rm10010PerfTelecomInputClientCurrent15StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 16, 1, 1),
    _Rm10010PerfTelecomInputClientCurrent15StatIndex_Type()
)
rm10010PerfTelecomInputClientCurrent15StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomInputClientCurrent15StatIndex.setStatus("current")
_Rm10010PerfTelecomInputClientCurrent15StatInvCvPortn_Type = EkiOnOff
_Rm10010PerfTelecomInputClientCurrent15StatInvCvPortn_Object = MibTableColumn
rm10010PerfTelecomInputClientCurrent15StatInvCvPortn = _Rm10010PerfTelecomInputClientCurrent15StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 16, 1, 2),
    _Rm10010PerfTelecomInputClientCurrent15StatInvCvPortn_Type()
)
rm10010PerfTelecomInputClientCurrent15StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomInputClientCurrent15StatInvCvPortn.setStatus("current")
_Rm10010PerfTelecomInputClientCurrent15StatCvValuePortn_Type = Unsigned32
_Rm10010PerfTelecomInputClientCurrent15StatCvValuePortn_Object = MibTableColumn
rm10010PerfTelecomInputClientCurrent15StatCvValuePortn = _Rm10010PerfTelecomInputClientCurrent15StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 16, 1, 3),
    _Rm10010PerfTelecomInputClientCurrent15StatCvValuePortn_Type()
)
rm10010PerfTelecomInputClientCurrent15StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomInputClientCurrent15StatCvValuePortn.setStatus("current")
_Rm10010PerfTelecomInputClientCurrent15StatInvEsPortn_Type = EkiOnOff
_Rm10010PerfTelecomInputClientCurrent15StatInvEsPortn_Object = MibTableColumn
rm10010PerfTelecomInputClientCurrent15StatInvEsPortn = _Rm10010PerfTelecomInputClientCurrent15StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 16, 1, 4),
    _Rm10010PerfTelecomInputClientCurrent15StatInvEsPortn_Type()
)
rm10010PerfTelecomInputClientCurrent15StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomInputClientCurrent15StatInvEsPortn.setStatus("current")
_Rm10010PerfTelecomInputClientCurrent15StatEsValuePortn_Type = Unsigned32
_Rm10010PerfTelecomInputClientCurrent15StatEsValuePortn_Object = MibTableColumn
rm10010PerfTelecomInputClientCurrent15StatEsValuePortn = _Rm10010PerfTelecomInputClientCurrent15StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 16, 1, 5),
    _Rm10010PerfTelecomInputClientCurrent15StatEsValuePortn_Type()
)
rm10010PerfTelecomInputClientCurrent15StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomInputClientCurrent15StatEsValuePortn.setStatus("current")
_Rm10010PerfTelecomInputClientCurrent15StatInvSesPortn_Type = EkiOnOff
_Rm10010PerfTelecomInputClientCurrent15StatInvSesPortn_Object = MibTableColumn
rm10010PerfTelecomInputClientCurrent15StatInvSesPortn = _Rm10010PerfTelecomInputClientCurrent15StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 16, 1, 6),
    _Rm10010PerfTelecomInputClientCurrent15StatInvSesPortn_Type()
)
rm10010PerfTelecomInputClientCurrent15StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomInputClientCurrent15StatInvSesPortn.setStatus("current")
_Rm10010PerfTelecomInputClientCurrent15StatSesValuePortn_Type = Unsigned32
_Rm10010PerfTelecomInputClientCurrent15StatSesValuePortn_Object = MibTableColumn
rm10010PerfTelecomInputClientCurrent15StatSesValuePortn = _Rm10010PerfTelecomInputClientCurrent15StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 16, 1, 7),
    _Rm10010PerfTelecomInputClientCurrent15StatSesValuePortn_Type()
)
rm10010PerfTelecomInputClientCurrent15StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomInputClientCurrent15StatSesValuePortn.setStatus("current")
_Rm10010PerfTelecomInputClientCurrent15StatInvSefsPortn_Type = EkiOnOff
_Rm10010PerfTelecomInputClientCurrent15StatInvSefsPortn_Object = MibTableColumn
rm10010PerfTelecomInputClientCurrent15StatInvSefsPortn = _Rm10010PerfTelecomInputClientCurrent15StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 16, 1, 8),
    _Rm10010PerfTelecomInputClientCurrent15StatInvSefsPortn_Type()
)
rm10010PerfTelecomInputClientCurrent15StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomInputClientCurrent15StatInvSefsPortn.setStatus("current")
_Rm10010PerfTelecomInputClientCurrent15StatSefsValuePortn_Type = Unsigned32
_Rm10010PerfTelecomInputClientCurrent15StatSefsValuePortn_Object = MibTableColumn
rm10010PerfTelecomInputClientCurrent15StatSefsValuePortn = _Rm10010PerfTelecomInputClientCurrent15StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 16, 1, 9),
    _Rm10010PerfTelecomInputClientCurrent15StatSefsValuePortn_Type()
)
rm10010PerfTelecomInputClientCurrent15StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomInputClientCurrent15StatSefsValuePortn.setStatus("current")
_Rm10010PerfTelecomInputClientCurrent15StatInvUasPortn_Type = EkiOnOff
_Rm10010PerfTelecomInputClientCurrent15StatInvUasPortn_Object = MibTableColumn
rm10010PerfTelecomInputClientCurrent15StatInvUasPortn = _Rm10010PerfTelecomInputClientCurrent15StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 16, 1, 10),
    _Rm10010PerfTelecomInputClientCurrent15StatInvUasPortn_Type()
)
rm10010PerfTelecomInputClientCurrent15StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomInputClientCurrent15StatInvUasPortn.setStatus("current")
_Rm10010PerfTelecomInputClientCurrent15StatUasValuePortn_Type = Unsigned32
_Rm10010PerfTelecomInputClientCurrent15StatUasValuePortn_Object = MibTableColumn
rm10010PerfTelecomInputClientCurrent15StatUasValuePortn = _Rm10010PerfTelecomInputClientCurrent15StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 16, 1, 11),
    _Rm10010PerfTelecomInputClientCurrent15StatUasValuePortn_Type()
)
rm10010PerfTelecomInputClientCurrent15StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomInputClientCurrent15StatUasValuePortn.setStatus("current")
_Rm10010PerfTelecomInputClientPast15StatHistoryPort1Table_Object = MibTable
rm10010PerfTelecomInputClientPast15StatHistoryPort1Table = _Rm10010PerfTelecomInputClientPast15StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 32)
)
if mibBuilder.loadTexts:
    rm10010PerfTelecomInputClientPast15StatHistoryPort1Table.setStatus("current")
_Rm10010PerfTelecomInputClientPast15StatHistoryPort1Entry_Object = MibTableRow
rm10010PerfTelecomInputClientPast15StatHistoryPort1Entry = _Rm10010PerfTelecomInputClientPast15StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 32, 1)
)
rm10010PerfTelecomInputClientPast15StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010PerfTelecomInputClientPast15StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    rm10010PerfTelecomInputClientPast15StatHistoryPort1Entry.setStatus("current")


class _Rm10010PerfTelecomInputClientPast15StatHistoryPort1Index_Type(Integer32):
    """Custom type rm10010PerfTelecomInputClientPast15StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010PerfTelecomInputClientPast15StatHistoryPort1Index_Type.__name__ = "Integer32"
_Rm10010PerfTelecomInputClientPast15StatHistoryPort1Index_Object = MibTableColumn
rm10010PerfTelecomInputClientPast15StatHistoryPort1Index = _Rm10010PerfTelecomInputClientPast15StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 32, 1, 1),
    _Rm10010PerfTelecomInputClientPast15StatHistoryPort1Index_Type()
)
rm10010PerfTelecomInputClientPast15StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomInputClientPast15StatHistoryPort1Index.setStatus("current")
_Rm10010PerfTelecomInputClientPast15StatHistoryInvCvPort1_Type = EkiOnOff
_Rm10010PerfTelecomInputClientPast15StatHistoryInvCvPort1_Object = MibTableColumn
rm10010PerfTelecomInputClientPast15StatHistoryInvCvPort1 = _Rm10010PerfTelecomInputClientPast15StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 32, 1, 2),
    _Rm10010PerfTelecomInputClientPast15StatHistoryInvCvPort1_Type()
)
rm10010PerfTelecomInputClientPast15StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomInputClientPast15StatHistoryInvCvPort1.setStatus("current")
_Rm10010PerfTelecomInputClientPast15StatHistoryCvValuePort1_Type = Unsigned32
_Rm10010PerfTelecomInputClientPast15StatHistoryCvValuePort1_Object = MibTableColumn
rm10010PerfTelecomInputClientPast15StatHistoryCvValuePort1 = _Rm10010PerfTelecomInputClientPast15StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 32, 1, 3),
    _Rm10010PerfTelecomInputClientPast15StatHistoryCvValuePort1_Type()
)
rm10010PerfTelecomInputClientPast15StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomInputClientPast15StatHistoryCvValuePort1.setStatus("current")
_Rm10010PerfTelecomInputClientPast15StatHistoryInvEsPort1_Type = EkiOnOff
_Rm10010PerfTelecomInputClientPast15StatHistoryInvEsPort1_Object = MibTableColumn
rm10010PerfTelecomInputClientPast15StatHistoryInvEsPort1 = _Rm10010PerfTelecomInputClientPast15StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 32, 1, 4),
    _Rm10010PerfTelecomInputClientPast15StatHistoryInvEsPort1_Type()
)
rm10010PerfTelecomInputClientPast15StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomInputClientPast15StatHistoryInvEsPort1.setStatus("current")
_Rm10010PerfTelecomInputClientPast15StatHistoryEsValuePort1_Type = Unsigned32
_Rm10010PerfTelecomInputClientPast15StatHistoryEsValuePort1_Object = MibTableColumn
rm10010PerfTelecomInputClientPast15StatHistoryEsValuePort1 = _Rm10010PerfTelecomInputClientPast15StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 32, 1, 5),
    _Rm10010PerfTelecomInputClientPast15StatHistoryEsValuePort1_Type()
)
rm10010PerfTelecomInputClientPast15StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomInputClientPast15StatHistoryEsValuePort1.setStatus("current")
_Rm10010PerfTelecomInputClientPast15StatHistoryInvSesPort1_Type = EkiOnOff
_Rm10010PerfTelecomInputClientPast15StatHistoryInvSesPort1_Object = MibTableColumn
rm10010PerfTelecomInputClientPast15StatHistoryInvSesPort1 = _Rm10010PerfTelecomInputClientPast15StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 32, 1, 6),
    _Rm10010PerfTelecomInputClientPast15StatHistoryInvSesPort1_Type()
)
rm10010PerfTelecomInputClientPast15StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomInputClientPast15StatHistoryInvSesPort1.setStatus("current")
_Rm10010PerfTelecomInputClientPast15StatHistorySesValuePort1_Type = Unsigned32
_Rm10010PerfTelecomInputClientPast15StatHistorySesValuePort1_Object = MibTableColumn
rm10010PerfTelecomInputClientPast15StatHistorySesValuePort1 = _Rm10010PerfTelecomInputClientPast15StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 32, 1, 7),
    _Rm10010PerfTelecomInputClientPast15StatHistorySesValuePort1_Type()
)
rm10010PerfTelecomInputClientPast15StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomInputClientPast15StatHistorySesValuePort1.setStatus("current")
_Rm10010PerfTelecomInputClientPast15StatHistoryInvSefsPort1_Type = EkiOnOff
_Rm10010PerfTelecomInputClientPast15StatHistoryInvSefsPort1_Object = MibTableColumn
rm10010PerfTelecomInputClientPast15StatHistoryInvSefsPort1 = _Rm10010PerfTelecomInputClientPast15StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 32, 1, 8),
    _Rm10010PerfTelecomInputClientPast15StatHistoryInvSefsPort1_Type()
)
rm10010PerfTelecomInputClientPast15StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomInputClientPast15StatHistoryInvSefsPort1.setStatus("current")
_Rm10010PerfTelecomInputClientPast15StatHistorySefsValuePort1_Type = Unsigned32
_Rm10010PerfTelecomInputClientPast15StatHistorySefsValuePort1_Object = MibTableColumn
rm10010PerfTelecomInputClientPast15StatHistorySefsValuePort1 = _Rm10010PerfTelecomInputClientPast15StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 32, 1, 9),
    _Rm10010PerfTelecomInputClientPast15StatHistorySefsValuePort1_Type()
)
rm10010PerfTelecomInputClientPast15StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomInputClientPast15StatHistorySefsValuePort1.setStatus("current")
_Rm10010PerfTelecomInputClientPast15StatHistoryInvUasPort1_Type = EkiOnOff
_Rm10010PerfTelecomInputClientPast15StatHistoryInvUasPort1_Object = MibTableColumn
rm10010PerfTelecomInputClientPast15StatHistoryInvUasPort1 = _Rm10010PerfTelecomInputClientPast15StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 32, 1, 10),
    _Rm10010PerfTelecomInputClientPast15StatHistoryInvUasPort1_Type()
)
rm10010PerfTelecomInputClientPast15StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomInputClientPast15StatHistoryInvUasPort1.setStatus("current")
_Rm10010PerfTelecomInputClientPast15StatHistoryUasValuePort1_Type = Unsigned32
_Rm10010PerfTelecomInputClientPast15StatHistoryUasValuePort1_Object = MibTableColumn
rm10010PerfTelecomInputClientPast15StatHistoryUasValuePort1 = _Rm10010PerfTelecomInputClientPast15StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 32, 1, 11),
    _Rm10010PerfTelecomInputClientPast15StatHistoryUasValuePort1_Type()
)
rm10010PerfTelecomInputClientPast15StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomInputClientPast15StatHistoryUasValuePort1.setStatus("current")
_Rm10010PerfTelecomInputClientCurrent24StatTable_Object = MibTable
rm10010PerfTelecomInputClientCurrent24StatTable = _Rm10010PerfTelecomInputClientCurrent24StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 48)
)
if mibBuilder.loadTexts:
    rm10010PerfTelecomInputClientCurrent24StatTable.setStatus("current")
_Rm10010PerfTelecomInputClientCurrent24StatEntry_Object = MibTableRow
rm10010PerfTelecomInputClientCurrent24StatEntry = _Rm10010PerfTelecomInputClientCurrent24StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 48, 1)
)
rm10010PerfTelecomInputClientCurrent24StatEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010PerfTelecomInputClientCurrent24StatIndex"),
)
if mibBuilder.loadTexts:
    rm10010PerfTelecomInputClientCurrent24StatEntry.setStatus("current")


class _Rm10010PerfTelecomInputClientCurrent24StatIndex_Type(Integer32):
    """Custom type rm10010PerfTelecomInputClientCurrent24StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010PerfTelecomInputClientCurrent24StatIndex_Type.__name__ = "Integer32"
_Rm10010PerfTelecomInputClientCurrent24StatIndex_Object = MibTableColumn
rm10010PerfTelecomInputClientCurrent24StatIndex = _Rm10010PerfTelecomInputClientCurrent24StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 48, 1, 1),
    _Rm10010PerfTelecomInputClientCurrent24StatIndex_Type()
)
rm10010PerfTelecomInputClientCurrent24StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomInputClientCurrent24StatIndex.setStatus("current")
_Rm10010PerfTelecomInputClientCurrent24StatInvCvPortn_Type = EkiOnOff
_Rm10010PerfTelecomInputClientCurrent24StatInvCvPortn_Object = MibTableColumn
rm10010PerfTelecomInputClientCurrent24StatInvCvPortn = _Rm10010PerfTelecomInputClientCurrent24StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 48, 1, 2),
    _Rm10010PerfTelecomInputClientCurrent24StatInvCvPortn_Type()
)
rm10010PerfTelecomInputClientCurrent24StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomInputClientCurrent24StatInvCvPortn.setStatus("current")
_Rm10010PerfTelecomInputClientCurrent24StatCvValuePortn_Type = Unsigned32
_Rm10010PerfTelecomInputClientCurrent24StatCvValuePortn_Object = MibTableColumn
rm10010PerfTelecomInputClientCurrent24StatCvValuePortn = _Rm10010PerfTelecomInputClientCurrent24StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 48, 1, 3),
    _Rm10010PerfTelecomInputClientCurrent24StatCvValuePortn_Type()
)
rm10010PerfTelecomInputClientCurrent24StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomInputClientCurrent24StatCvValuePortn.setStatus("current")
_Rm10010PerfTelecomInputClientCurrent24StatInvEsPortn_Type = EkiOnOff
_Rm10010PerfTelecomInputClientCurrent24StatInvEsPortn_Object = MibTableColumn
rm10010PerfTelecomInputClientCurrent24StatInvEsPortn = _Rm10010PerfTelecomInputClientCurrent24StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 48, 1, 4),
    _Rm10010PerfTelecomInputClientCurrent24StatInvEsPortn_Type()
)
rm10010PerfTelecomInputClientCurrent24StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomInputClientCurrent24StatInvEsPortn.setStatus("current")
_Rm10010PerfTelecomInputClientCurrent24StatEsValuePortn_Type = Unsigned32
_Rm10010PerfTelecomInputClientCurrent24StatEsValuePortn_Object = MibTableColumn
rm10010PerfTelecomInputClientCurrent24StatEsValuePortn = _Rm10010PerfTelecomInputClientCurrent24StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 48, 1, 5),
    _Rm10010PerfTelecomInputClientCurrent24StatEsValuePortn_Type()
)
rm10010PerfTelecomInputClientCurrent24StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomInputClientCurrent24StatEsValuePortn.setStatus("current")
_Rm10010PerfTelecomInputClientCurrent24StatInvSesPortn_Type = EkiOnOff
_Rm10010PerfTelecomInputClientCurrent24StatInvSesPortn_Object = MibTableColumn
rm10010PerfTelecomInputClientCurrent24StatInvSesPortn = _Rm10010PerfTelecomInputClientCurrent24StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 48, 1, 6),
    _Rm10010PerfTelecomInputClientCurrent24StatInvSesPortn_Type()
)
rm10010PerfTelecomInputClientCurrent24StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomInputClientCurrent24StatInvSesPortn.setStatus("current")
_Rm10010PerfTelecomInputClientCurrent24StatSesValuePortn_Type = Unsigned32
_Rm10010PerfTelecomInputClientCurrent24StatSesValuePortn_Object = MibTableColumn
rm10010PerfTelecomInputClientCurrent24StatSesValuePortn = _Rm10010PerfTelecomInputClientCurrent24StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 48, 1, 7),
    _Rm10010PerfTelecomInputClientCurrent24StatSesValuePortn_Type()
)
rm10010PerfTelecomInputClientCurrent24StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomInputClientCurrent24StatSesValuePortn.setStatus("current")
_Rm10010PerfTelecomInputClientCurrent24StatInvSefsPortn_Type = EkiOnOff
_Rm10010PerfTelecomInputClientCurrent24StatInvSefsPortn_Object = MibTableColumn
rm10010PerfTelecomInputClientCurrent24StatInvSefsPortn = _Rm10010PerfTelecomInputClientCurrent24StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 48, 1, 8),
    _Rm10010PerfTelecomInputClientCurrent24StatInvSefsPortn_Type()
)
rm10010PerfTelecomInputClientCurrent24StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomInputClientCurrent24StatInvSefsPortn.setStatus("current")
_Rm10010PerfTelecomInputClientCurrent24StatSefsValuePortn_Type = Unsigned32
_Rm10010PerfTelecomInputClientCurrent24StatSefsValuePortn_Object = MibTableColumn
rm10010PerfTelecomInputClientCurrent24StatSefsValuePortn = _Rm10010PerfTelecomInputClientCurrent24StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 48, 1, 9),
    _Rm10010PerfTelecomInputClientCurrent24StatSefsValuePortn_Type()
)
rm10010PerfTelecomInputClientCurrent24StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomInputClientCurrent24StatSefsValuePortn.setStatus("current")
_Rm10010PerfTelecomInputClientCurrent24StatInvUasPortn_Type = EkiOnOff
_Rm10010PerfTelecomInputClientCurrent24StatInvUasPortn_Object = MibTableColumn
rm10010PerfTelecomInputClientCurrent24StatInvUasPortn = _Rm10010PerfTelecomInputClientCurrent24StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 48, 1, 10),
    _Rm10010PerfTelecomInputClientCurrent24StatInvUasPortn_Type()
)
rm10010PerfTelecomInputClientCurrent24StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomInputClientCurrent24StatInvUasPortn.setStatus("current")
_Rm10010PerfTelecomInputClientCurrent24StatUasValuePortn_Type = Unsigned32
_Rm10010PerfTelecomInputClientCurrent24StatUasValuePortn_Object = MibTableColumn
rm10010PerfTelecomInputClientCurrent24StatUasValuePortn = _Rm10010PerfTelecomInputClientCurrent24StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 48, 1, 11),
    _Rm10010PerfTelecomInputClientCurrent24StatUasValuePortn_Type()
)
rm10010PerfTelecomInputClientCurrent24StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomInputClientCurrent24StatUasValuePortn.setStatus("current")
_Rm10010PerfTelecomInputClientPast24StatHistoryPort1Table_Object = MibTable
rm10010PerfTelecomInputClientPast24StatHistoryPort1Table = _Rm10010PerfTelecomInputClientPast24StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 64)
)
if mibBuilder.loadTexts:
    rm10010PerfTelecomInputClientPast24StatHistoryPort1Table.setStatus("current")
_Rm10010PerfTelecomInputClientPast24StatHistoryPort1Entry_Object = MibTableRow
rm10010PerfTelecomInputClientPast24StatHistoryPort1Entry = _Rm10010PerfTelecomInputClientPast24StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 64, 1)
)
rm10010PerfTelecomInputClientPast24StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010PerfTelecomInputClientPast24StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    rm10010PerfTelecomInputClientPast24StatHistoryPort1Entry.setStatus("current")


class _Rm10010PerfTelecomInputClientPast24StatHistoryPort1Index_Type(Integer32):
    """Custom type rm10010PerfTelecomInputClientPast24StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010PerfTelecomInputClientPast24StatHistoryPort1Index_Type.__name__ = "Integer32"
_Rm10010PerfTelecomInputClientPast24StatHistoryPort1Index_Object = MibTableColumn
rm10010PerfTelecomInputClientPast24StatHistoryPort1Index = _Rm10010PerfTelecomInputClientPast24StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 64, 1, 1),
    _Rm10010PerfTelecomInputClientPast24StatHistoryPort1Index_Type()
)
rm10010PerfTelecomInputClientPast24StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomInputClientPast24StatHistoryPort1Index.setStatus("current")
_Rm10010PerfTelecomInputClientPast24StatHistoryInvCvPort1_Type = EkiOnOff
_Rm10010PerfTelecomInputClientPast24StatHistoryInvCvPort1_Object = MibTableColumn
rm10010PerfTelecomInputClientPast24StatHistoryInvCvPort1 = _Rm10010PerfTelecomInputClientPast24StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 64, 1, 2),
    _Rm10010PerfTelecomInputClientPast24StatHistoryInvCvPort1_Type()
)
rm10010PerfTelecomInputClientPast24StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomInputClientPast24StatHistoryInvCvPort1.setStatus("current")
_Rm10010PerfTelecomInputClientPast24StatHistoryCvValuePort1_Type = Unsigned32
_Rm10010PerfTelecomInputClientPast24StatHistoryCvValuePort1_Object = MibTableColumn
rm10010PerfTelecomInputClientPast24StatHistoryCvValuePort1 = _Rm10010PerfTelecomInputClientPast24StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 64, 1, 3),
    _Rm10010PerfTelecomInputClientPast24StatHistoryCvValuePort1_Type()
)
rm10010PerfTelecomInputClientPast24StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomInputClientPast24StatHistoryCvValuePort1.setStatus("current")
_Rm10010PerfTelecomInputClientPast24StatHistoryInvEsPort1_Type = EkiOnOff
_Rm10010PerfTelecomInputClientPast24StatHistoryInvEsPort1_Object = MibTableColumn
rm10010PerfTelecomInputClientPast24StatHistoryInvEsPort1 = _Rm10010PerfTelecomInputClientPast24StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 64, 1, 4),
    _Rm10010PerfTelecomInputClientPast24StatHistoryInvEsPort1_Type()
)
rm10010PerfTelecomInputClientPast24StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomInputClientPast24StatHistoryInvEsPort1.setStatus("current")
_Rm10010PerfTelecomInputClientPast24StatHistoryEsValuePort1_Type = Unsigned32
_Rm10010PerfTelecomInputClientPast24StatHistoryEsValuePort1_Object = MibTableColumn
rm10010PerfTelecomInputClientPast24StatHistoryEsValuePort1 = _Rm10010PerfTelecomInputClientPast24StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 64, 1, 5),
    _Rm10010PerfTelecomInputClientPast24StatHistoryEsValuePort1_Type()
)
rm10010PerfTelecomInputClientPast24StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomInputClientPast24StatHistoryEsValuePort1.setStatus("current")
_Rm10010PerfTelecomInputClientPast24StatHistoryInvSesPort1_Type = EkiOnOff
_Rm10010PerfTelecomInputClientPast24StatHistoryInvSesPort1_Object = MibTableColumn
rm10010PerfTelecomInputClientPast24StatHistoryInvSesPort1 = _Rm10010PerfTelecomInputClientPast24StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 64, 1, 6),
    _Rm10010PerfTelecomInputClientPast24StatHistoryInvSesPort1_Type()
)
rm10010PerfTelecomInputClientPast24StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomInputClientPast24StatHistoryInvSesPort1.setStatus("current")
_Rm10010PerfTelecomInputClientPast24StatHistorySesValuePort1_Type = Unsigned32
_Rm10010PerfTelecomInputClientPast24StatHistorySesValuePort1_Object = MibTableColumn
rm10010PerfTelecomInputClientPast24StatHistorySesValuePort1 = _Rm10010PerfTelecomInputClientPast24StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 64, 1, 7),
    _Rm10010PerfTelecomInputClientPast24StatHistorySesValuePort1_Type()
)
rm10010PerfTelecomInputClientPast24StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomInputClientPast24StatHistorySesValuePort1.setStatus("current")
_Rm10010PerfTelecomInputClientPast24StatHistoryInvSefsPort1_Type = EkiOnOff
_Rm10010PerfTelecomInputClientPast24StatHistoryInvSefsPort1_Object = MibTableColumn
rm10010PerfTelecomInputClientPast24StatHistoryInvSefsPort1 = _Rm10010PerfTelecomInputClientPast24StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 64, 1, 8),
    _Rm10010PerfTelecomInputClientPast24StatHistoryInvSefsPort1_Type()
)
rm10010PerfTelecomInputClientPast24StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomInputClientPast24StatHistoryInvSefsPort1.setStatus("current")
_Rm10010PerfTelecomInputClientPast24StatHistorySefsValuePort1_Type = Unsigned32
_Rm10010PerfTelecomInputClientPast24StatHistorySefsValuePort1_Object = MibTableColumn
rm10010PerfTelecomInputClientPast24StatHistorySefsValuePort1 = _Rm10010PerfTelecomInputClientPast24StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 64, 1, 9),
    _Rm10010PerfTelecomInputClientPast24StatHistorySefsValuePort1_Type()
)
rm10010PerfTelecomInputClientPast24StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomInputClientPast24StatHistorySefsValuePort1.setStatus("current")
_Rm10010PerfTelecomInputClientPast24StatHistoryInvUasPort1_Type = EkiOnOff
_Rm10010PerfTelecomInputClientPast24StatHistoryInvUasPort1_Object = MibTableColumn
rm10010PerfTelecomInputClientPast24StatHistoryInvUasPort1 = _Rm10010PerfTelecomInputClientPast24StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 64, 1, 10),
    _Rm10010PerfTelecomInputClientPast24StatHistoryInvUasPort1_Type()
)
rm10010PerfTelecomInputClientPast24StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomInputClientPast24StatHistoryInvUasPort1.setStatus("current")
_Rm10010PerfTelecomInputClientPast24StatHistoryUasValuePort1_Type = Unsigned32
_Rm10010PerfTelecomInputClientPast24StatHistoryUasValuePort1_Object = MibTableColumn
rm10010PerfTelecomInputClientPast24StatHistoryUasValuePort1 = _Rm10010PerfTelecomInputClientPast24StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 64, 1, 11),
    _Rm10010PerfTelecomInputClientPast24StatHistoryUasValuePort1_Type()
)
rm10010PerfTelecomInputClientPast24StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomInputClientPast24StatHistoryUasValuePort1.setStatus("current")
_Rm10010PerfTelecomOutputClientCurrent15StatTable_Object = MibTable
rm10010PerfTelecomOutputClientCurrent15StatTable = _Rm10010PerfTelecomOutputClientCurrent15StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 80)
)
if mibBuilder.loadTexts:
    rm10010PerfTelecomOutputClientCurrent15StatTable.setStatus("current")
_Rm10010PerfTelecomOutputClientCurrent15StatEntry_Object = MibTableRow
rm10010PerfTelecomOutputClientCurrent15StatEntry = _Rm10010PerfTelecomOutputClientCurrent15StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 80, 1)
)
rm10010PerfTelecomOutputClientCurrent15StatEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010PerfTelecomOutputClientCurrent15StatIndex"),
)
if mibBuilder.loadTexts:
    rm10010PerfTelecomOutputClientCurrent15StatEntry.setStatus("current")


class _Rm10010PerfTelecomOutputClientCurrent15StatIndex_Type(Integer32):
    """Custom type rm10010PerfTelecomOutputClientCurrent15StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010PerfTelecomOutputClientCurrent15StatIndex_Type.__name__ = "Integer32"
_Rm10010PerfTelecomOutputClientCurrent15StatIndex_Object = MibTableColumn
rm10010PerfTelecomOutputClientCurrent15StatIndex = _Rm10010PerfTelecomOutputClientCurrent15StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 80, 1, 1),
    _Rm10010PerfTelecomOutputClientCurrent15StatIndex_Type()
)
rm10010PerfTelecomOutputClientCurrent15StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomOutputClientCurrent15StatIndex.setStatus("current")
_Rm10010PerfTelecomOutputClientCurrent15StatInvCvPortn_Type = EkiOnOff
_Rm10010PerfTelecomOutputClientCurrent15StatInvCvPortn_Object = MibTableColumn
rm10010PerfTelecomOutputClientCurrent15StatInvCvPortn = _Rm10010PerfTelecomOutputClientCurrent15StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 80, 1, 2),
    _Rm10010PerfTelecomOutputClientCurrent15StatInvCvPortn_Type()
)
rm10010PerfTelecomOutputClientCurrent15StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomOutputClientCurrent15StatInvCvPortn.setStatus("current")
_Rm10010PerfTelecomOutputClientCurrent15StatCvValuePortn_Type = Unsigned32
_Rm10010PerfTelecomOutputClientCurrent15StatCvValuePortn_Object = MibTableColumn
rm10010PerfTelecomOutputClientCurrent15StatCvValuePortn = _Rm10010PerfTelecomOutputClientCurrent15StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 80, 1, 3),
    _Rm10010PerfTelecomOutputClientCurrent15StatCvValuePortn_Type()
)
rm10010PerfTelecomOutputClientCurrent15StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomOutputClientCurrent15StatCvValuePortn.setStatus("current")
_Rm10010PerfTelecomOutputClientCurrent15StatInvEsPortn_Type = EkiOnOff
_Rm10010PerfTelecomOutputClientCurrent15StatInvEsPortn_Object = MibTableColumn
rm10010PerfTelecomOutputClientCurrent15StatInvEsPortn = _Rm10010PerfTelecomOutputClientCurrent15StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 80, 1, 4),
    _Rm10010PerfTelecomOutputClientCurrent15StatInvEsPortn_Type()
)
rm10010PerfTelecomOutputClientCurrent15StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomOutputClientCurrent15StatInvEsPortn.setStatus("current")
_Rm10010PerfTelecomOutputClientCurrent15StatEsValuePortn_Type = Unsigned32
_Rm10010PerfTelecomOutputClientCurrent15StatEsValuePortn_Object = MibTableColumn
rm10010PerfTelecomOutputClientCurrent15StatEsValuePortn = _Rm10010PerfTelecomOutputClientCurrent15StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 80, 1, 5),
    _Rm10010PerfTelecomOutputClientCurrent15StatEsValuePortn_Type()
)
rm10010PerfTelecomOutputClientCurrent15StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomOutputClientCurrent15StatEsValuePortn.setStatus("current")
_Rm10010PerfTelecomOutputClientCurrent15StatInvSesPortn_Type = EkiOnOff
_Rm10010PerfTelecomOutputClientCurrent15StatInvSesPortn_Object = MibTableColumn
rm10010PerfTelecomOutputClientCurrent15StatInvSesPortn = _Rm10010PerfTelecomOutputClientCurrent15StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 80, 1, 6),
    _Rm10010PerfTelecomOutputClientCurrent15StatInvSesPortn_Type()
)
rm10010PerfTelecomOutputClientCurrent15StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomOutputClientCurrent15StatInvSesPortn.setStatus("current")
_Rm10010PerfTelecomOutputClientCurrent15StatSesValuePortn_Type = Unsigned32
_Rm10010PerfTelecomOutputClientCurrent15StatSesValuePortn_Object = MibTableColumn
rm10010PerfTelecomOutputClientCurrent15StatSesValuePortn = _Rm10010PerfTelecomOutputClientCurrent15StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 80, 1, 7),
    _Rm10010PerfTelecomOutputClientCurrent15StatSesValuePortn_Type()
)
rm10010PerfTelecomOutputClientCurrent15StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomOutputClientCurrent15StatSesValuePortn.setStatus("current")
_Rm10010PerfTelecomOutputClientCurrent15StatInvSefsPortn_Type = EkiOnOff
_Rm10010PerfTelecomOutputClientCurrent15StatInvSefsPortn_Object = MibTableColumn
rm10010PerfTelecomOutputClientCurrent15StatInvSefsPortn = _Rm10010PerfTelecomOutputClientCurrent15StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 80, 1, 8),
    _Rm10010PerfTelecomOutputClientCurrent15StatInvSefsPortn_Type()
)
rm10010PerfTelecomOutputClientCurrent15StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomOutputClientCurrent15StatInvSefsPortn.setStatus("current")
_Rm10010PerfTelecomOutputClientCurrent15StatSefsValuePortn_Type = Unsigned32
_Rm10010PerfTelecomOutputClientCurrent15StatSefsValuePortn_Object = MibTableColumn
rm10010PerfTelecomOutputClientCurrent15StatSefsValuePortn = _Rm10010PerfTelecomOutputClientCurrent15StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 80, 1, 9),
    _Rm10010PerfTelecomOutputClientCurrent15StatSefsValuePortn_Type()
)
rm10010PerfTelecomOutputClientCurrent15StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomOutputClientCurrent15StatSefsValuePortn.setStatus("current")
_Rm10010PerfTelecomOutputClientCurrent15StatInvUasPortn_Type = EkiOnOff
_Rm10010PerfTelecomOutputClientCurrent15StatInvUasPortn_Object = MibTableColumn
rm10010PerfTelecomOutputClientCurrent15StatInvUasPortn = _Rm10010PerfTelecomOutputClientCurrent15StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 80, 1, 10),
    _Rm10010PerfTelecomOutputClientCurrent15StatInvUasPortn_Type()
)
rm10010PerfTelecomOutputClientCurrent15StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomOutputClientCurrent15StatInvUasPortn.setStatus("current")
_Rm10010PerfTelecomOutputClientCurrent15StatUasValuePortn_Type = Unsigned32
_Rm10010PerfTelecomOutputClientCurrent15StatUasValuePortn_Object = MibTableColumn
rm10010PerfTelecomOutputClientCurrent15StatUasValuePortn = _Rm10010PerfTelecomOutputClientCurrent15StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 80, 1, 11),
    _Rm10010PerfTelecomOutputClientCurrent15StatUasValuePortn_Type()
)
rm10010PerfTelecomOutputClientCurrent15StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomOutputClientCurrent15StatUasValuePortn.setStatus("current")
_Rm10010PerfTelecomOutputClientPast15StatHistoryPort1Table_Object = MibTable
rm10010PerfTelecomOutputClientPast15StatHistoryPort1Table = _Rm10010PerfTelecomOutputClientPast15StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 96)
)
if mibBuilder.loadTexts:
    rm10010PerfTelecomOutputClientPast15StatHistoryPort1Table.setStatus("current")
_Rm10010PerfTelecomOutputClientPast15StatHistoryPort1Entry_Object = MibTableRow
rm10010PerfTelecomOutputClientPast15StatHistoryPort1Entry = _Rm10010PerfTelecomOutputClientPast15StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 96, 1)
)
rm10010PerfTelecomOutputClientPast15StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010PerfTelecomOutputClientPast15StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    rm10010PerfTelecomOutputClientPast15StatHistoryPort1Entry.setStatus("current")


class _Rm10010PerfTelecomOutputClientPast15StatHistoryPort1Index_Type(Integer32):
    """Custom type rm10010PerfTelecomOutputClientPast15StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010PerfTelecomOutputClientPast15StatHistoryPort1Index_Type.__name__ = "Integer32"
_Rm10010PerfTelecomOutputClientPast15StatHistoryPort1Index_Object = MibTableColumn
rm10010PerfTelecomOutputClientPast15StatHistoryPort1Index = _Rm10010PerfTelecomOutputClientPast15StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 96, 1, 1),
    _Rm10010PerfTelecomOutputClientPast15StatHistoryPort1Index_Type()
)
rm10010PerfTelecomOutputClientPast15StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomOutputClientPast15StatHistoryPort1Index.setStatus("current")
_Rm10010PerfTelecomOutputClientPast15StatHistoryInvCvPort1_Type = EkiOnOff
_Rm10010PerfTelecomOutputClientPast15StatHistoryInvCvPort1_Object = MibTableColumn
rm10010PerfTelecomOutputClientPast15StatHistoryInvCvPort1 = _Rm10010PerfTelecomOutputClientPast15StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 96, 1, 2),
    _Rm10010PerfTelecomOutputClientPast15StatHistoryInvCvPort1_Type()
)
rm10010PerfTelecomOutputClientPast15StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomOutputClientPast15StatHistoryInvCvPort1.setStatus("current")
_Rm10010PerfTelecomOutputClientPast15StatHistoryCvValuePort1_Type = Unsigned32
_Rm10010PerfTelecomOutputClientPast15StatHistoryCvValuePort1_Object = MibTableColumn
rm10010PerfTelecomOutputClientPast15StatHistoryCvValuePort1 = _Rm10010PerfTelecomOutputClientPast15StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 96, 1, 3),
    _Rm10010PerfTelecomOutputClientPast15StatHistoryCvValuePort1_Type()
)
rm10010PerfTelecomOutputClientPast15StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomOutputClientPast15StatHistoryCvValuePort1.setStatus("current")
_Rm10010PerfTelecomOutputClientPast15StatHistoryInvEsPort1_Type = EkiOnOff
_Rm10010PerfTelecomOutputClientPast15StatHistoryInvEsPort1_Object = MibTableColumn
rm10010PerfTelecomOutputClientPast15StatHistoryInvEsPort1 = _Rm10010PerfTelecomOutputClientPast15StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 96, 1, 4),
    _Rm10010PerfTelecomOutputClientPast15StatHistoryInvEsPort1_Type()
)
rm10010PerfTelecomOutputClientPast15StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomOutputClientPast15StatHistoryInvEsPort1.setStatus("current")
_Rm10010PerfTelecomOutputClientPast15StatHistoryEsValuePort1_Type = Unsigned32
_Rm10010PerfTelecomOutputClientPast15StatHistoryEsValuePort1_Object = MibTableColumn
rm10010PerfTelecomOutputClientPast15StatHistoryEsValuePort1 = _Rm10010PerfTelecomOutputClientPast15StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 96, 1, 5),
    _Rm10010PerfTelecomOutputClientPast15StatHistoryEsValuePort1_Type()
)
rm10010PerfTelecomOutputClientPast15StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomOutputClientPast15StatHistoryEsValuePort1.setStatus("current")
_Rm10010PerfTelecomOutputClientPast15StatHistoryInvSesPort1_Type = EkiOnOff
_Rm10010PerfTelecomOutputClientPast15StatHistoryInvSesPort1_Object = MibTableColumn
rm10010PerfTelecomOutputClientPast15StatHistoryInvSesPort1 = _Rm10010PerfTelecomOutputClientPast15StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 96, 1, 6),
    _Rm10010PerfTelecomOutputClientPast15StatHistoryInvSesPort1_Type()
)
rm10010PerfTelecomOutputClientPast15StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomOutputClientPast15StatHistoryInvSesPort1.setStatus("current")
_Rm10010PerfTelecomOutputClientPast15StatHistorySesValuePort1_Type = Unsigned32
_Rm10010PerfTelecomOutputClientPast15StatHistorySesValuePort1_Object = MibTableColumn
rm10010PerfTelecomOutputClientPast15StatHistorySesValuePort1 = _Rm10010PerfTelecomOutputClientPast15StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 96, 1, 7),
    _Rm10010PerfTelecomOutputClientPast15StatHistorySesValuePort1_Type()
)
rm10010PerfTelecomOutputClientPast15StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomOutputClientPast15StatHistorySesValuePort1.setStatus("current")
_Rm10010PerfTelecomOutputClientPast15StatHistoryInvSefsPort1_Type = EkiOnOff
_Rm10010PerfTelecomOutputClientPast15StatHistoryInvSefsPort1_Object = MibTableColumn
rm10010PerfTelecomOutputClientPast15StatHistoryInvSefsPort1 = _Rm10010PerfTelecomOutputClientPast15StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 96, 1, 8),
    _Rm10010PerfTelecomOutputClientPast15StatHistoryInvSefsPort1_Type()
)
rm10010PerfTelecomOutputClientPast15StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomOutputClientPast15StatHistoryInvSefsPort1.setStatus("current")
_Rm10010PerfTelecomOutputClientPast15StatHistorySefsValuePort1_Type = Unsigned32
_Rm10010PerfTelecomOutputClientPast15StatHistorySefsValuePort1_Object = MibTableColumn
rm10010PerfTelecomOutputClientPast15StatHistorySefsValuePort1 = _Rm10010PerfTelecomOutputClientPast15StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 96, 1, 9),
    _Rm10010PerfTelecomOutputClientPast15StatHistorySefsValuePort1_Type()
)
rm10010PerfTelecomOutputClientPast15StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomOutputClientPast15StatHistorySefsValuePort1.setStatus("current")
_Rm10010PerfTelecomOutputClientPast15StatHistoryInvUasPort1_Type = EkiOnOff
_Rm10010PerfTelecomOutputClientPast15StatHistoryInvUasPort1_Object = MibTableColumn
rm10010PerfTelecomOutputClientPast15StatHistoryInvUasPort1 = _Rm10010PerfTelecomOutputClientPast15StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 96, 1, 10),
    _Rm10010PerfTelecomOutputClientPast15StatHistoryInvUasPort1_Type()
)
rm10010PerfTelecomOutputClientPast15StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomOutputClientPast15StatHistoryInvUasPort1.setStatus("current")
_Rm10010PerfTelecomOutputClientPast15StatHistoryUasValuePort1_Type = Unsigned32
_Rm10010PerfTelecomOutputClientPast15StatHistoryUasValuePort1_Object = MibTableColumn
rm10010PerfTelecomOutputClientPast15StatHistoryUasValuePort1 = _Rm10010PerfTelecomOutputClientPast15StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 96, 1, 11),
    _Rm10010PerfTelecomOutputClientPast15StatHistoryUasValuePort1_Type()
)
rm10010PerfTelecomOutputClientPast15StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomOutputClientPast15StatHistoryUasValuePort1.setStatus("current")
_Rm10010PerfTelecomOutputClientCurrent24StatTable_Object = MibTable
rm10010PerfTelecomOutputClientCurrent24StatTable = _Rm10010PerfTelecomOutputClientCurrent24StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 112)
)
if mibBuilder.loadTexts:
    rm10010PerfTelecomOutputClientCurrent24StatTable.setStatus("current")
_Rm10010PerfTelecomOutputClientCurrent24StatEntry_Object = MibTableRow
rm10010PerfTelecomOutputClientCurrent24StatEntry = _Rm10010PerfTelecomOutputClientCurrent24StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 112, 1)
)
rm10010PerfTelecomOutputClientCurrent24StatEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010PerfTelecomOutputClientCurrent24StatIndex"),
)
if mibBuilder.loadTexts:
    rm10010PerfTelecomOutputClientCurrent24StatEntry.setStatus("current")


class _Rm10010PerfTelecomOutputClientCurrent24StatIndex_Type(Integer32):
    """Custom type rm10010PerfTelecomOutputClientCurrent24StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010PerfTelecomOutputClientCurrent24StatIndex_Type.__name__ = "Integer32"
_Rm10010PerfTelecomOutputClientCurrent24StatIndex_Object = MibTableColumn
rm10010PerfTelecomOutputClientCurrent24StatIndex = _Rm10010PerfTelecomOutputClientCurrent24StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 112, 1, 1),
    _Rm10010PerfTelecomOutputClientCurrent24StatIndex_Type()
)
rm10010PerfTelecomOutputClientCurrent24StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomOutputClientCurrent24StatIndex.setStatus("current")
_Rm10010PerfTelecomOutputClientCurrent24StatInvCvPortn_Type = EkiOnOff
_Rm10010PerfTelecomOutputClientCurrent24StatInvCvPortn_Object = MibTableColumn
rm10010PerfTelecomOutputClientCurrent24StatInvCvPortn = _Rm10010PerfTelecomOutputClientCurrent24StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 112, 1, 2),
    _Rm10010PerfTelecomOutputClientCurrent24StatInvCvPortn_Type()
)
rm10010PerfTelecomOutputClientCurrent24StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomOutputClientCurrent24StatInvCvPortn.setStatus("current")
_Rm10010PerfTelecomOutputClientCurrent24StatCvValuePortn_Type = Unsigned32
_Rm10010PerfTelecomOutputClientCurrent24StatCvValuePortn_Object = MibTableColumn
rm10010PerfTelecomOutputClientCurrent24StatCvValuePortn = _Rm10010PerfTelecomOutputClientCurrent24StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 112, 1, 3),
    _Rm10010PerfTelecomOutputClientCurrent24StatCvValuePortn_Type()
)
rm10010PerfTelecomOutputClientCurrent24StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomOutputClientCurrent24StatCvValuePortn.setStatus("current")
_Rm10010PerfTelecomOutputClientCurrent24StatInvEsPortn_Type = EkiOnOff
_Rm10010PerfTelecomOutputClientCurrent24StatInvEsPortn_Object = MibTableColumn
rm10010PerfTelecomOutputClientCurrent24StatInvEsPortn = _Rm10010PerfTelecomOutputClientCurrent24StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 112, 1, 4),
    _Rm10010PerfTelecomOutputClientCurrent24StatInvEsPortn_Type()
)
rm10010PerfTelecomOutputClientCurrent24StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomOutputClientCurrent24StatInvEsPortn.setStatus("current")
_Rm10010PerfTelecomOutputClientCurrent24StatEsValuePortn_Type = Unsigned32
_Rm10010PerfTelecomOutputClientCurrent24StatEsValuePortn_Object = MibTableColumn
rm10010PerfTelecomOutputClientCurrent24StatEsValuePortn = _Rm10010PerfTelecomOutputClientCurrent24StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 112, 1, 5),
    _Rm10010PerfTelecomOutputClientCurrent24StatEsValuePortn_Type()
)
rm10010PerfTelecomOutputClientCurrent24StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomOutputClientCurrent24StatEsValuePortn.setStatus("current")
_Rm10010PerfTelecomOutputClientCurrent24StatInvSesPortn_Type = EkiOnOff
_Rm10010PerfTelecomOutputClientCurrent24StatInvSesPortn_Object = MibTableColumn
rm10010PerfTelecomOutputClientCurrent24StatInvSesPortn = _Rm10010PerfTelecomOutputClientCurrent24StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 112, 1, 6),
    _Rm10010PerfTelecomOutputClientCurrent24StatInvSesPortn_Type()
)
rm10010PerfTelecomOutputClientCurrent24StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomOutputClientCurrent24StatInvSesPortn.setStatus("current")
_Rm10010PerfTelecomOutputClientCurrent24StatSesValuePortn_Type = Unsigned32
_Rm10010PerfTelecomOutputClientCurrent24StatSesValuePortn_Object = MibTableColumn
rm10010PerfTelecomOutputClientCurrent24StatSesValuePortn = _Rm10010PerfTelecomOutputClientCurrent24StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 112, 1, 7),
    _Rm10010PerfTelecomOutputClientCurrent24StatSesValuePortn_Type()
)
rm10010PerfTelecomOutputClientCurrent24StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomOutputClientCurrent24StatSesValuePortn.setStatus("current")
_Rm10010PerfTelecomOutputClientCurrent24StatInvSefsPortn_Type = EkiOnOff
_Rm10010PerfTelecomOutputClientCurrent24StatInvSefsPortn_Object = MibTableColumn
rm10010PerfTelecomOutputClientCurrent24StatInvSefsPortn = _Rm10010PerfTelecomOutputClientCurrent24StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 112, 1, 8),
    _Rm10010PerfTelecomOutputClientCurrent24StatInvSefsPortn_Type()
)
rm10010PerfTelecomOutputClientCurrent24StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomOutputClientCurrent24StatInvSefsPortn.setStatus("current")
_Rm10010PerfTelecomOutputClientCurrent24StatSefsValuePortn_Type = Unsigned32
_Rm10010PerfTelecomOutputClientCurrent24StatSefsValuePortn_Object = MibTableColumn
rm10010PerfTelecomOutputClientCurrent24StatSefsValuePortn = _Rm10010PerfTelecomOutputClientCurrent24StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 112, 1, 9),
    _Rm10010PerfTelecomOutputClientCurrent24StatSefsValuePortn_Type()
)
rm10010PerfTelecomOutputClientCurrent24StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomOutputClientCurrent24StatSefsValuePortn.setStatus("current")
_Rm10010PerfTelecomOutputClientCurrent24StatInvUasPortn_Type = EkiOnOff
_Rm10010PerfTelecomOutputClientCurrent24StatInvUasPortn_Object = MibTableColumn
rm10010PerfTelecomOutputClientCurrent24StatInvUasPortn = _Rm10010PerfTelecomOutputClientCurrent24StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 112, 1, 10),
    _Rm10010PerfTelecomOutputClientCurrent24StatInvUasPortn_Type()
)
rm10010PerfTelecomOutputClientCurrent24StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomOutputClientCurrent24StatInvUasPortn.setStatus("current")
_Rm10010PerfTelecomOutputClientCurrent24StatUasValuePortn_Type = Unsigned32
_Rm10010PerfTelecomOutputClientCurrent24StatUasValuePortn_Object = MibTableColumn
rm10010PerfTelecomOutputClientCurrent24StatUasValuePortn = _Rm10010PerfTelecomOutputClientCurrent24StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 112, 1, 11),
    _Rm10010PerfTelecomOutputClientCurrent24StatUasValuePortn_Type()
)
rm10010PerfTelecomOutputClientCurrent24StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomOutputClientCurrent24StatUasValuePortn.setStatus("current")
_Rm10010PerfTelecomOutputClientPast24StatHistoryPort1Table_Object = MibTable
rm10010PerfTelecomOutputClientPast24StatHistoryPort1Table = _Rm10010PerfTelecomOutputClientPast24StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 128)
)
if mibBuilder.loadTexts:
    rm10010PerfTelecomOutputClientPast24StatHistoryPort1Table.setStatus("current")
_Rm10010PerfTelecomOutputClientPast24StatHistoryPort1Entry_Object = MibTableRow
rm10010PerfTelecomOutputClientPast24StatHistoryPort1Entry = _Rm10010PerfTelecomOutputClientPast24StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 128, 1)
)
rm10010PerfTelecomOutputClientPast24StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010PerfTelecomOutputClientPast24StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    rm10010PerfTelecomOutputClientPast24StatHistoryPort1Entry.setStatus("current")


class _Rm10010PerfTelecomOutputClientPast24StatHistoryPort1Index_Type(Integer32):
    """Custom type rm10010PerfTelecomOutputClientPast24StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010PerfTelecomOutputClientPast24StatHistoryPort1Index_Type.__name__ = "Integer32"
_Rm10010PerfTelecomOutputClientPast24StatHistoryPort1Index_Object = MibTableColumn
rm10010PerfTelecomOutputClientPast24StatHistoryPort1Index = _Rm10010PerfTelecomOutputClientPast24StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 128, 1, 1),
    _Rm10010PerfTelecomOutputClientPast24StatHistoryPort1Index_Type()
)
rm10010PerfTelecomOutputClientPast24StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomOutputClientPast24StatHistoryPort1Index.setStatus("current")
_Rm10010PerfTelecomOutputClientPast24StatHistoryInvCvPort1_Type = EkiOnOff
_Rm10010PerfTelecomOutputClientPast24StatHistoryInvCvPort1_Object = MibTableColumn
rm10010PerfTelecomOutputClientPast24StatHistoryInvCvPort1 = _Rm10010PerfTelecomOutputClientPast24StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 128, 1, 2),
    _Rm10010PerfTelecomOutputClientPast24StatHistoryInvCvPort1_Type()
)
rm10010PerfTelecomOutputClientPast24StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomOutputClientPast24StatHistoryInvCvPort1.setStatus("current")
_Rm10010PerfTelecomOutputClientPast24StatHistoryCvValuePort1_Type = Unsigned32
_Rm10010PerfTelecomOutputClientPast24StatHistoryCvValuePort1_Object = MibTableColumn
rm10010PerfTelecomOutputClientPast24StatHistoryCvValuePort1 = _Rm10010PerfTelecomOutputClientPast24StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 128, 1, 3),
    _Rm10010PerfTelecomOutputClientPast24StatHistoryCvValuePort1_Type()
)
rm10010PerfTelecomOutputClientPast24StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomOutputClientPast24StatHistoryCvValuePort1.setStatus("current")
_Rm10010PerfTelecomOutputClientPast24StatHistoryInvEsPort1_Type = EkiOnOff
_Rm10010PerfTelecomOutputClientPast24StatHistoryInvEsPort1_Object = MibTableColumn
rm10010PerfTelecomOutputClientPast24StatHistoryInvEsPort1 = _Rm10010PerfTelecomOutputClientPast24StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 128, 1, 4),
    _Rm10010PerfTelecomOutputClientPast24StatHistoryInvEsPort1_Type()
)
rm10010PerfTelecomOutputClientPast24StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomOutputClientPast24StatHistoryInvEsPort1.setStatus("current")
_Rm10010PerfTelecomOutputClientPast24StatHistoryEsValuePort1_Type = Unsigned32
_Rm10010PerfTelecomOutputClientPast24StatHistoryEsValuePort1_Object = MibTableColumn
rm10010PerfTelecomOutputClientPast24StatHistoryEsValuePort1 = _Rm10010PerfTelecomOutputClientPast24StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 128, 1, 5),
    _Rm10010PerfTelecomOutputClientPast24StatHistoryEsValuePort1_Type()
)
rm10010PerfTelecomOutputClientPast24StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomOutputClientPast24StatHistoryEsValuePort1.setStatus("current")
_Rm10010PerfTelecomOutputClientPast24StatHistoryInvSesPort1_Type = EkiOnOff
_Rm10010PerfTelecomOutputClientPast24StatHistoryInvSesPort1_Object = MibTableColumn
rm10010PerfTelecomOutputClientPast24StatHistoryInvSesPort1 = _Rm10010PerfTelecomOutputClientPast24StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 128, 1, 6),
    _Rm10010PerfTelecomOutputClientPast24StatHistoryInvSesPort1_Type()
)
rm10010PerfTelecomOutputClientPast24StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomOutputClientPast24StatHistoryInvSesPort1.setStatus("current")
_Rm10010PerfTelecomOutputClientPast24StatHistorySesValuePort1_Type = Unsigned32
_Rm10010PerfTelecomOutputClientPast24StatHistorySesValuePort1_Object = MibTableColumn
rm10010PerfTelecomOutputClientPast24StatHistorySesValuePort1 = _Rm10010PerfTelecomOutputClientPast24StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 128, 1, 7),
    _Rm10010PerfTelecomOutputClientPast24StatHistorySesValuePort1_Type()
)
rm10010PerfTelecomOutputClientPast24StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomOutputClientPast24StatHistorySesValuePort1.setStatus("current")
_Rm10010PerfTelecomOutputClientPast24StatHistoryInvSefsPort1_Type = EkiOnOff
_Rm10010PerfTelecomOutputClientPast24StatHistoryInvSefsPort1_Object = MibTableColumn
rm10010PerfTelecomOutputClientPast24StatHistoryInvSefsPort1 = _Rm10010PerfTelecomOutputClientPast24StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 128, 1, 8),
    _Rm10010PerfTelecomOutputClientPast24StatHistoryInvSefsPort1_Type()
)
rm10010PerfTelecomOutputClientPast24StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomOutputClientPast24StatHistoryInvSefsPort1.setStatus("current")
_Rm10010PerfTelecomOutputClientPast24StatHistorySefsValuePort1_Type = Unsigned32
_Rm10010PerfTelecomOutputClientPast24StatHistorySefsValuePort1_Object = MibTableColumn
rm10010PerfTelecomOutputClientPast24StatHistorySefsValuePort1 = _Rm10010PerfTelecomOutputClientPast24StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 128, 1, 9),
    _Rm10010PerfTelecomOutputClientPast24StatHistorySefsValuePort1_Type()
)
rm10010PerfTelecomOutputClientPast24StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomOutputClientPast24StatHistorySefsValuePort1.setStatus("current")
_Rm10010PerfTelecomOutputClientPast24StatHistoryInvUasPort1_Type = EkiOnOff
_Rm10010PerfTelecomOutputClientPast24StatHistoryInvUasPort1_Object = MibTableColumn
rm10010PerfTelecomOutputClientPast24StatHistoryInvUasPort1 = _Rm10010PerfTelecomOutputClientPast24StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 128, 1, 10),
    _Rm10010PerfTelecomOutputClientPast24StatHistoryInvUasPort1_Type()
)
rm10010PerfTelecomOutputClientPast24StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomOutputClientPast24StatHistoryInvUasPort1.setStatus("current")
_Rm10010PerfTelecomOutputClientPast24StatHistoryUasValuePort1_Type = Unsigned32
_Rm10010PerfTelecomOutputClientPast24StatHistoryUasValuePort1_Object = MibTableColumn
rm10010PerfTelecomOutputClientPast24StatHistoryUasValuePort1 = _Rm10010PerfTelecomOutputClientPast24StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 128, 1, 11),
    _Rm10010PerfTelecomOutputClientPast24StatHistoryUasValuePort1_Type()
)
rm10010PerfTelecomOutputClientPast24StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomOutputClientPast24StatHistoryUasValuePort1.setStatus("current")
_Rm10010PerfDatacomClientCurrent15StatTable_Object = MibTable
rm10010PerfDatacomClientCurrent15StatTable = _Rm10010PerfDatacomClientCurrent15StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 432)
)
if mibBuilder.loadTexts:
    rm10010PerfDatacomClientCurrent15StatTable.setStatus("current")
_Rm10010PerfDatacomClientCurrent15StatEntry_Object = MibTableRow
rm10010PerfDatacomClientCurrent15StatEntry = _Rm10010PerfDatacomClientCurrent15StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 432, 1)
)
rm10010PerfDatacomClientCurrent15StatEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010PerfDatacomClientCurrent15StatIndex"),
)
if mibBuilder.loadTexts:
    rm10010PerfDatacomClientCurrent15StatEntry.setStatus("current")


class _Rm10010PerfDatacomClientCurrent15StatIndex_Type(Integer32):
    """Custom type rm10010PerfDatacomClientCurrent15StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010PerfDatacomClientCurrent15StatIndex_Type.__name__ = "Integer32"
_Rm10010PerfDatacomClientCurrent15StatIndex_Object = MibTableColumn
rm10010PerfDatacomClientCurrent15StatIndex = _Rm10010PerfDatacomClientCurrent15StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 432, 1, 1),
    _Rm10010PerfDatacomClientCurrent15StatIndex_Type()
)
rm10010PerfDatacomClientCurrent15StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfDatacomClientCurrent15StatIndex.setStatus("current")
_Rm10010perfdatacomclientCurrent15StatInCrcCountInvPortn_Type = EkiOnOff
_Rm10010perfdatacomclientCurrent15StatInCrcCountInvPortn_Object = MibTableColumn
rm10010perfdatacomclientCurrent15StatInCrcCountInvPortn = _Rm10010perfdatacomclientCurrent15StatInCrcCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 432, 1, 4),
    _Rm10010perfdatacomclientCurrent15StatInCrcCountInvPortn_Type()
)
rm10010perfdatacomclientCurrent15StatInCrcCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientCurrent15StatInCrcCountInvPortn.setStatus("current")
_Rm10010perfdatacomclientCurrent15StatInCrcCountPortn_Type = Counter64
_Rm10010perfdatacomclientCurrent15StatInCrcCountPortn_Object = MibTableColumn
rm10010perfdatacomclientCurrent15StatInCrcCountPortn = _Rm10010perfdatacomclientCurrent15StatInCrcCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 432, 1, 5),
    _Rm10010perfdatacomclientCurrent15StatInCrcCountPortn_Type()
)
rm10010perfdatacomclientCurrent15StatInCrcCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientCurrent15StatInCrcCountPortn.setStatus("current")
_Rm10010perfdatacomclientCurrent15StatInPacketCountInvPortn_Type = EkiOnOff
_Rm10010perfdatacomclientCurrent15StatInPacketCountInvPortn_Object = MibTableColumn
rm10010perfdatacomclientCurrent15StatInPacketCountInvPortn = _Rm10010perfdatacomclientCurrent15StatInPacketCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 432, 1, 6),
    _Rm10010perfdatacomclientCurrent15StatInPacketCountInvPortn_Type()
)
rm10010perfdatacomclientCurrent15StatInPacketCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientCurrent15StatInPacketCountInvPortn.setStatus("current")
_Rm10010perfdatacomclientCurrent15StatInPacketCountPortn_Type = Counter64
_Rm10010perfdatacomclientCurrent15StatInPacketCountPortn_Object = MibTableColumn
rm10010perfdatacomclientCurrent15StatInPacketCountPortn = _Rm10010perfdatacomclientCurrent15StatInPacketCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 432, 1, 7),
    _Rm10010perfdatacomclientCurrent15StatInPacketCountPortn_Type()
)
rm10010perfdatacomclientCurrent15StatInPacketCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientCurrent15StatInPacketCountPortn.setStatus("current")
_Rm10010perfdatacomclientCurrent15StatOutCrcCountInvPortn_Type = EkiOnOff
_Rm10010perfdatacomclientCurrent15StatOutCrcCountInvPortn_Object = MibTableColumn
rm10010perfdatacomclientCurrent15StatOutCrcCountInvPortn = _Rm10010perfdatacomclientCurrent15StatOutCrcCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 432, 1, 28),
    _Rm10010perfdatacomclientCurrent15StatOutCrcCountInvPortn_Type()
)
rm10010perfdatacomclientCurrent15StatOutCrcCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientCurrent15StatOutCrcCountInvPortn.setStatus("current")
_Rm10010perfdatacomclientCurrent15StatOutCrcCountPortn_Type = Counter64
_Rm10010perfdatacomclientCurrent15StatOutCrcCountPortn_Object = MibTableColumn
rm10010perfdatacomclientCurrent15StatOutCrcCountPortn = _Rm10010perfdatacomclientCurrent15StatOutCrcCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 432, 1, 29),
    _Rm10010perfdatacomclientCurrent15StatOutCrcCountPortn_Type()
)
rm10010perfdatacomclientCurrent15StatOutCrcCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientCurrent15StatOutCrcCountPortn.setStatus("current")
_Rm10010perfdatacomclientCurrent15StatOutPacketCountInvPortn_Type = EkiOnOff
_Rm10010perfdatacomclientCurrent15StatOutPacketCountInvPortn_Object = MibTableColumn
rm10010perfdatacomclientCurrent15StatOutPacketCountInvPortn = _Rm10010perfdatacomclientCurrent15StatOutPacketCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 432, 1, 30),
    _Rm10010perfdatacomclientCurrent15StatOutPacketCountInvPortn_Type()
)
rm10010perfdatacomclientCurrent15StatOutPacketCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientCurrent15StatOutPacketCountInvPortn.setStatus("current")
_Rm10010perfdatacomclientCurrent15StatOutPacketCountPortn_Type = Counter64
_Rm10010perfdatacomclientCurrent15StatOutPacketCountPortn_Object = MibTableColumn
rm10010perfdatacomclientCurrent15StatOutPacketCountPortn = _Rm10010perfdatacomclientCurrent15StatOutPacketCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 432, 1, 31),
    _Rm10010perfdatacomclientCurrent15StatOutPacketCountPortn_Type()
)
rm10010perfdatacomclientCurrent15StatOutPacketCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientCurrent15StatOutPacketCountPortn.setStatus("current")
_Rm10010PerfDatacomClientPast15StatHistoryPort1Table_Object = MibTable
rm10010PerfDatacomClientPast15StatHistoryPort1Table = _Rm10010PerfDatacomClientPast15StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 448)
)
if mibBuilder.loadTexts:
    rm10010PerfDatacomClientPast15StatHistoryPort1Table.setStatus("current")
_Rm10010PerfDatacomClientPast15StatHistoryPort1Entry_Object = MibTableRow
rm10010PerfDatacomClientPast15StatHistoryPort1Entry = _Rm10010PerfDatacomClientPast15StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 448, 1)
)
rm10010PerfDatacomClientPast15StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010PerfDatacomClientPast15StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    rm10010PerfDatacomClientPast15StatHistoryPort1Entry.setStatus("current")


class _Rm10010PerfDatacomClientPast15StatHistoryPort1Index_Type(Integer32):
    """Custom type rm10010PerfDatacomClientPast15StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010PerfDatacomClientPast15StatHistoryPort1Index_Type.__name__ = "Integer32"
_Rm10010PerfDatacomClientPast15StatHistoryPort1Index_Object = MibTableColumn
rm10010PerfDatacomClientPast15StatHistoryPort1Index = _Rm10010PerfDatacomClientPast15StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 448, 1, 1),
    _Rm10010PerfDatacomClientPast15StatHistoryPort1Index_Type()
)
rm10010PerfDatacomClientPast15StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfDatacomClientPast15StatHistoryPort1Index.setStatus("current")
_Rm10010perfdatacomclientPast15StatInCrcCountInvPort1_Type = EkiOnOff
_Rm10010perfdatacomclientPast15StatInCrcCountInvPort1_Object = MibTableColumn
rm10010perfdatacomclientPast15StatInCrcCountInvPort1 = _Rm10010perfdatacomclientPast15StatInCrcCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 448, 1, 4),
    _Rm10010perfdatacomclientPast15StatInCrcCountInvPort1_Type()
)
rm10010perfdatacomclientPast15StatInCrcCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientPast15StatInCrcCountInvPort1.setStatus("current")
_Rm10010perfdatacomclientPast15StatInCrcCountPort1_Type = Counter64
_Rm10010perfdatacomclientPast15StatInCrcCountPort1_Object = MibTableColumn
rm10010perfdatacomclientPast15StatInCrcCountPort1 = _Rm10010perfdatacomclientPast15StatInCrcCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 448, 1, 5),
    _Rm10010perfdatacomclientPast15StatInCrcCountPort1_Type()
)
rm10010perfdatacomclientPast15StatInCrcCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientPast15StatInCrcCountPort1.setStatus("current")
_Rm10010perfdatacomclientPast15StatInPacketCountInvPort1_Type = EkiOnOff
_Rm10010perfdatacomclientPast15StatInPacketCountInvPort1_Object = MibTableColumn
rm10010perfdatacomclientPast15StatInPacketCountInvPort1 = _Rm10010perfdatacomclientPast15StatInPacketCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 448, 1, 6),
    _Rm10010perfdatacomclientPast15StatInPacketCountInvPort1_Type()
)
rm10010perfdatacomclientPast15StatInPacketCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientPast15StatInPacketCountInvPort1.setStatus("current")
_Rm10010perfdatacomclientPast15StatInPacketCountPort1_Type = Counter64
_Rm10010perfdatacomclientPast15StatInPacketCountPort1_Object = MibTableColumn
rm10010perfdatacomclientPast15StatInPacketCountPort1 = _Rm10010perfdatacomclientPast15StatInPacketCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 448, 1, 7),
    _Rm10010perfdatacomclientPast15StatInPacketCountPort1_Type()
)
rm10010perfdatacomclientPast15StatInPacketCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientPast15StatInPacketCountPort1.setStatus("current")
_Rm10010perfdatacomclientPast15StatOutCrcCountInvPort1_Type = EkiOnOff
_Rm10010perfdatacomclientPast15StatOutCrcCountInvPort1_Object = MibTableColumn
rm10010perfdatacomclientPast15StatOutCrcCountInvPort1 = _Rm10010perfdatacomclientPast15StatOutCrcCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 448, 1, 28),
    _Rm10010perfdatacomclientPast15StatOutCrcCountInvPort1_Type()
)
rm10010perfdatacomclientPast15StatOutCrcCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientPast15StatOutCrcCountInvPort1.setStatus("current")
_Rm10010perfdatacomclientPast15StatOutCrcCountPort1_Type = Counter64
_Rm10010perfdatacomclientPast15StatOutCrcCountPort1_Object = MibTableColumn
rm10010perfdatacomclientPast15StatOutCrcCountPort1 = _Rm10010perfdatacomclientPast15StatOutCrcCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 448, 1, 29),
    _Rm10010perfdatacomclientPast15StatOutCrcCountPort1_Type()
)
rm10010perfdatacomclientPast15StatOutCrcCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientPast15StatOutCrcCountPort1.setStatus("current")
_Rm10010perfdatacomclientPast15StatOutPacketCountInvPort1_Type = EkiOnOff
_Rm10010perfdatacomclientPast15StatOutPacketCountInvPort1_Object = MibTableColumn
rm10010perfdatacomclientPast15StatOutPacketCountInvPort1 = _Rm10010perfdatacomclientPast15StatOutPacketCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 448, 1, 30),
    _Rm10010perfdatacomclientPast15StatOutPacketCountInvPort1_Type()
)
rm10010perfdatacomclientPast15StatOutPacketCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientPast15StatOutPacketCountInvPort1.setStatus("current")
_Rm10010perfdatacomclientPast15StatOutPacketCountPort1_Type = Counter64
_Rm10010perfdatacomclientPast15StatOutPacketCountPort1_Object = MibTableColumn
rm10010perfdatacomclientPast15StatOutPacketCountPort1 = _Rm10010perfdatacomclientPast15StatOutPacketCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 448, 1, 31),
    _Rm10010perfdatacomclientPast15StatOutPacketCountPort1_Type()
)
rm10010perfdatacomclientPast15StatOutPacketCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientPast15StatOutPacketCountPort1.setStatus("current")
_Rm10010PerfDatacomClientCurrent24StatTable_Object = MibTable
rm10010PerfDatacomClientCurrent24StatTable = _Rm10010PerfDatacomClientCurrent24StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 464)
)
if mibBuilder.loadTexts:
    rm10010PerfDatacomClientCurrent24StatTable.setStatus("current")
_Rm10010PerfDatacomClientCurrent24StatEntry_Object = MibTableRow
rm10010PerfDatacomClientCurrent24StatEntry = _Rm10010PerfDatacomClientCurrent24StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 464, 1)
)
rm10010PerfDatacomClientCurrent24StatEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010PerfDatacomClientCurrent24StatIndex"),
)
if mibBuilder.loadTexts:
    rm10010PerfDatacomClientCurrent24StatEntry.setStatus("current")


class _Rm10010PerfDatacomClientCurrent24StatIndex_Type(Integer32):
    """Custom type rm10010PerfDatacomClientCurrent24StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010PerfDatacomClientCurrent24StatIndex_Type.__name__ = "Integer32"
_Rm10010PerfDatacomClientCurrent24StatIndex_Object = MibTableColumn
rm10010PerfDatacomClientCurrent24StatIndex = _Rm10010PerfDatacomClientCurrent24StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 464, 1, 1),
    _Rm10010PerfDatacomClientCurrent24StatIndex_Type()
)
rm10010PerfDatacomClientCurrent24StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfDatacomClientCurrent24StatIndex.setStatus("current")
_Rm10010perfdatacomclientCurrent24StatInCrcCountInvPortn_Type = EkiOnOff
_Rm10010perfdatacomclientCurrent24StatInCrcCountInvPortn_Object = MibTableColumn
rm10010perfdatacomclientCurrent24StatInCrcCountInvPortn = _Rm10010perfdatacomclientCurrent24StatInCrcCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 464, 1, 4),
    _Rm10010perfdatacomclientCurrent24StatInCrcCountInvPortn_Type()
)
rm10010perfdatacomclientCurrent24StatInCrcCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientCurrent24StatInCrcCountInvPortn.setStatus("current")
_Rm10010perfdatacomclientCurrent24StatInCrcCountPortn_Type = Counter64
_Rm10010perfdatacomclientCurrent24StatInCrcCountPortn_Object = MibTableColumn
rm10010perfdatacomclientCurrent24StatInCrcCountPortn = _Rm10010perfdatacomclientCurrent24StatInCrcCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 464, 1, 5),
    _Rm10010perfdatacomclientCurrent24StatInCrcCountPortn_Type()
)
rm10010perfdatacomclientCurrent24StatInCrcCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientCurrent24StatInCrcCountPortn.setStatus("current")
_Rm10010perfdatacomclientCurrent24StatInPacketCountInvPortn_Type = EkiOnOff
_Rm10010perfdatacomclientCurrent24StatInPacketCountInvPortn_Object = MibTableColumn
rm10010perfdatacomclientCurrent24StatInPacketCountInvPortn = _Rm10010perfdatacomclientCurrent24StatInPacketCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 464, 1, 6),
    _Rm10010perfdatacomclientCurrent24StatInPacketCountInvPortn_Type()
)
rm10010perfdatacomclientCurrent24StatInPacketCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientCurrent24StatInPacketCountInvPortn.setStatus("current")
_Rm10010perfdatacomclientCurrent24StatInPacketCountPortn_Type = Counter64
_Rm10010perfdatacomclientCurrent24StatInPacketCountPortn_Object = MibTableColumn
rm10010perfdatacomclientCurrent24StatInPacketCountPortn = _Rm10010perfdatacomclientCurrent24StatInPacketCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 464, 1, 7),
    _Rm10010perfdatacomclientCurrent24StatInPacketCountPortn_Type()
)
rm10010perfdatacomclientCurrent24StatInPacketCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientCurrent24StatInPacketCountPortn.setStatus("current")
_Rm10010perfdatacomclientCurrent24StatOutCrcCountInvPortn_Type = EkiOnOff
_Rm10010perfdatacomclientCurrent24StatOutCrcCountInvPortn_Object = MibTableColumn
rm10010perfdatacomclientCurrent24StatOutCrcCountInvPortn = _Rm10010perfdatacomclientCurrent24StatOutCrcCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 464, 1, 28),
    _Rm10010perfdatacomclientCurrent24StatOutCrcCountInvPortn_Type()
)
rm10010perfdatacomclientCurrent24StatOutCrcCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientCurrent24StatOutCrcCountInvPortn.setStatus("current")
_Rm10010perfdatacomclientCurrent24StatOutCrcCountPortn_Type = Counter64
_Rm10010perfdatacomclientCurrent24StatOutCrcCountPortn_Object = MibTableColumn
rm10010perfdatacomclientCurrent24StatOutCrcCountPortn = _Rm10010perfdatacomclientCurrent24StatOutCrcCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 464, 1, 29),
    _Rm10010perfdatacomclientCurrent24StatOutCrcCountPortn_Type()
)
rm10010perfdatacomclientCurrent24StatOutCrcCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientCurrent24StatOutCrcCountPortn.setStatus("current")
_Rm10010perfdatacomclientCurrent24StatOutPacketCountInvPortn_Type = EkiOnOff
_Rm10010perfdatacomclientCurrent24StatOutPacketCountInvPortn_Object = MibTableColumn
rm10010perfdatacomclientCurrent24StatOutPacketCountInvPortn = _Rm10010perfdatacomclientCurrent24StatOutPacketCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 464, 1, 30),
    _Rm10010perfdatacomclientCurrent24StatOutPacketCountInvPortn_Type()
)
rm10010perfdatacomclientCurrent24StatOutPacketCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientCurrent24StatOutPacketCountInvPortn.setStatus("current")
_Rm10010perfdatacomclientCurrent24StatOutPacketCountPortn_Type = Counter64
_Rm10010perfdatacomclientCurrent24StatOutPacketCountPortn_Object = MibTableColumn
rm10010perfdatacomclientCurrent24StatOutPacketCountPortn = _Rm10010perfdatacomclientCurrent24StatOutPacketCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 464, 1, 31),
    _Rm10010perfdatacomclientCurrent24StatOutPacketCountPortn_Type()
)
rm10010perfdatacomclientCurrent24StatOutPacketCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientCurrent24StatOutPacketCountPortn.setStatus("current")
_Rm10010PerfDatacomClientPast24StatHistoryPort1Table_Object = MibTable
rm10010PerfDatacomClientPast24StatHistoryPort1Table = _Rm10010PerfDatacomClientPast24StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 480)
)
if mibBuilder.loadTexts:
    rm10010PerfDatacomClientPast24StatHistoryPort1Table.setStatus("current")
_Rm10010PerfDatacomClientPast24StatHistoryPort1Entry_Object = MibTableRow
rm10010PerfDatacomClientPast24StatHistoryPort1Entry = _Rm10010PerfDatacomClientPast24StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 480, 1)
)
rm10010PerfDatacomClientPast24StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010PerfDatacomClientPast24StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    rm10010PerfDatacomClientPast24StatHistoryPort1Entry.setStatus("current")


class _Rm10010PerfDatacomClientPast24StatHistoryPort1Index_Type(Integer32):
    """Custom type rm10010PerfDatacomClientPast24StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010PerfDatacomClientPast24StatHistoryPort1Index_Type.__name__ = "Integer32"
_Rm10010PerfDatacomClientPast24StatHistoryPort1Index_Object = MibTableColumn
rm10010PerfDatacomClientPast24StatHistoryPort1Index = _Rm10010PerfDatacomClientPast24StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 480, 1, 1),
    _Rm10010PerfDatacomClientPast24StatHistoryPort1Index_Type()
)
rm10010PerfDatacomClientPast24StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfDatacomClientPast24StatHistoryPort1Index.setStatus("current")
_Rm10010perfdatacomclientPast24StatInCrcCountInvPort1_Type = EkiOnOff
_Rm10010perfdatacomclientPast24StatInCrcCountInvPort1_Object = MibTableColumn
rm10010perfdatacomclientPast24StatInCrcCountInvPort1 = _Rm10010perfdatacomclientPast24StatInCrcCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 480, 1, 4),
    _Rm10010perfdatacomclientPast24StatInCrcCountInvPort1_Type()
)
rm10010perfdatacomclientPast24StatInCrcCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientPast24StatInCrcCountInvPort1.setStatus("current")
_Rm10010perfdatacomclientPast24StatInCrcCountPort1_Type = Counter64
_Rm10010perfdatacomclientPast24StatInCrcCountPort1_Object = MibTableColumn
rm10010perfdatacomclientPast24StatInCrcCountPort1 = _Rm10010perfdatacomclientPast24StatInCrcCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 480, 1, 5),
    _Rm10010perfdatacomclientPast24StatInCrcCountPort1_Type()
)
rm10010perfdatacomclientPast24StatInCrcCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientPast24StatInCrcCountPort1.setStatus("current")
_Rm10010perfdatacomclientPast24StatInPacketCountInvPort1_Type = EkiOnOff
_Rm10010perfdatacomclientPast24StatInPacketCountInvPort1_Object = MibTableColumn
rm10010perfdatacomclientPast24StatInPacketCountInvPort1 = _Rm10010perfdatacomclientPast24StatInPacketCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 480, 1, 6),
    _Rm10010perfdatacomclientPast24StatInPacketCountInvPort1_Type()
)
rm10010perfdatacomclientPast24StatInPacketCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientPast24StatInPacketCountInvPort1.setStatus("current")
_Rm10010perfdatacomclientPast24StatInPacketCountPort1_Type = Counter64
_Rm10010perfdatacomclientPast24StatInPacketCountPort1_Object = MibTableColumn
rm10010perfdatacomclientPast24StatInPacketCountPort1 = _Rm10010perfdatacomclientPast24StatInPacketCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 480, 1, 7),
    _Rm10010perfdatacomclientPast24StatInPacketCountPort1_Type()
)
rm10010perfdatacomclientPast24StatInPacketCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientPast24StatInPacketCountPort1.setStatus("current")
_Rm10010perfdatacomclientPast24StatOutCrcCountInvPort1_Type = EkiOnOff
_Rm10010perfdatacomclientPast24StatOutCrcCountInvPort1_Object = MibTableColumn
rm10010perfdatacomclientPast24StatOutCrcCountInvPort1 = _Rm10010perfdatacomclientPast24StatOutCrcCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 480, 1, 28),
    _Rm10010perfdatacomclientPast24StatOutCrcCountInvPort1_Type()
)
rm10010perfdatacomclientPast24StatOutCrcCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientPast24StatOutCrcCountInvPort1.setStatus("current")
_Rm10010perfdatacomclientPast24StatOutCrcCountPort1_Type = Counter64
_Rm10010perfdatacomclientPast24StatOutCrcCountPort1_Object = MibTableColumn
rm10010perfdatacomclientPast24StatOutCrcCountPort1 = _Rm10010perfdatacomclientPast24StatOutCrcCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 480, 1, 29),
    _Rm10010perfdatacomclientPast24StatOutCrcCountPort1_Type()
)
rm10010perfdatacomclientPast24StatOutCrcCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientPast24StatOutCrcCountPort1.setStatus("current")
_Rm10010perfdatacomclientPast24StatOutPacketCountInvPort1_Type = EkiOnOff
_Rm10010perfdatacomclientPast24StatOutPacketCountInvPort1_Object = MibTableColumn
rm10010perfdatacomclientPast24StatOutPacketCountInvPort1 = _Rm10010perfdatacomclientPast24StatOutPacketCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 480, 1, 30),
    _Rm10010perfdatacomclientPast24StatOutPacketCountInvPort1_Type()
)
rm10010perfdatacomclientPast24StatOutPacketCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientPast24StatOutPacketCountInvPort1.setStatus("current")
_Rm10010perfdatacomclientPast24StatOutPacketCountPort1_Type = Counter64
_Rm10010perfdatacomclientPast24StatOutPacketCountPort1_Object = MibTableColumn
rm10010perfdatacomclientPast24StatOutPacketCountPort1 = _Rm10010perfdatacomclientPast24StatOutPacketCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 6, 480, 1, 31),
    _Rm10010perfdatacomclientPast24StatOutPacketCountPort1_Type()
)
rm10010perfdatacomclientPast24StatOutPacketCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientPast24StatOutPacketCountPort1.setStatus("current")
_Rm10010MonPerfLine_ObjectIdentity = ObjectIdentity
rm10010MonPerfLine = _Rm10010MonPerfLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7)
)
_Rm10010PerfTelecomLinePostFecCurrent15StatTable_Object = MibTable
rm10010PerfTelecomLinePostFecCurrent15StatTable = _Rm10010PerfTelecomLinePostFecCurrent15StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 192)
)
if mibBuilder.loadTexts:
    rm10010PerfTelecomLinePostFecCurrent15StatTable.setStatus("current")
_Rm10010PerfTelecomLinePostFecCurrent15StatEntry_Object = MibTableRow
rm10010PerfTelecomLinePostFecCurrent15StatEntry = _Rm10010PerfTelecomLinePostFecCurrent15StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 192, 1)
)
rm10010PerfTelecomLinePostFecCurrent15StatEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010PerfTelecomLinePostFecCurrent15StatIndex"),
)
if mibBuilder.loadTexts:
    rm10010PerfTelecomLinePostFecCurrent15StatEntry.setStatus("current")


class _Rm10010PerfTelecomLinePostFecCurrent15StatIndex_Type(Integer32):
    """Custom type rm10010PerfTelecomLinePostFecCurrent15StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010PerfTelecomLinePostFecCurrent15StatIndex_Type.__name__ = "Integer32"
_Rm10010PerfTelecomLinePostFecCurrent15StatIndex_Object = MibTableColumn
rm10010PerfTelecomLinePostFecCurrent15StatIndex = _Rm10010PerfTelecomLinePostFecCurrent15StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 192, 1, 1),
    _Rm10010PerfTelecomLinePostFecCurrent15StatIndex_Type()
)
rm10010PerfTelecomLinePostFecCurrent15StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomLinePostFecCurrent15StatIndex.setStatus("current")
_Rm10010PerfTelecomLinePostFecCurrent15StatInvCvPortn_Type = EkiOnOff
_Rm10010PerfTelecomLinePostFecCurrent15StatInvCvPortn_Object = MibTableColumn
rm10010PerfTelecomLinePostFecCurrent15StatInvCvPortn = _Rm10010PerfTelecomLinePostFecCurrent15StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 192, 1, 2),
    _Rm10010PerfTelecomLinePostFecCurrent15StatInvCvPortn_Type()
)
rm10010PerfTelecomLinePostFecCurrent15StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomLinePostFecCurrent15StatInvCvPortn.setStatus("current")
_Rm10010PerfTelecomLinePostFecCurrent15StatCvValuePortn_Type = Unsigned32
_Rm10010PerfTelecomLinePostFecCurrent15StatCvValuePortn_Object = MibTableColumn
rm10010PerfTelecomLinePostFecCurrent15StatCvValuePortn = _Rm10010PerfTelecomLinePostFecCurrent15StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 192, 1, 3),
    _Rm10010PerfTelecomLinePostFecCurrent15StatCvValuePortn_Type()
)
rm10010PerfTelecomLinePostFecCurrent15StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomLinePostFecCurrent15StatCvValuePortn.setStatus("current")
_Rm10010PerfTelecomLinePostFecCurrent15StatInvEsPortn_Type = EkiOnOff
_Rm10010PerfTelecomLinePostFecCurrent15StatInvEsPortn_Object = MibTableColumn
rm10010PerfTelecomLinePostFecCurrent15StatInvEsPortn = _Rm10010PerfTelecomLinePostFecCurrent15StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 192, 1, 4),
    _Rm10010PerfTelecomLinePostFecCurrent15StatInvEsPortn_Type()
)
rm10010PerfTelecomLinePostFecCurrent15StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomLinePostFecCurrent15StatInvEsPortn.setStatus("current")
_Rm10010PerfTelecomLinePostFecCurrent15StatEsValuePortn_Type = Unsigned32
_Rm10010PerfTelecomLinePostFecCurrent15StatEsValuePortn_Object = MibTableColumn
rm10010PerfTelecomLinePostFecCurrent15StatEsValuePortn = _Rm10010PerfTelecomLinePostFecCurrent15StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 192, 1, 5),
    _Rm10010PerfTelecomLinePostFecCurrent15StatEsValuePortn_Type()
)
rm10010PerfTelecomLinePostFecCurrent15StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomLinePostFecCurrent15StatEsValuePortn.setStatus("current")
_Rm10010PerfTelecomLinePostFecCurrent15StatInvSesPortn_Type = EkiOnOff
_Rm10010PerfTelecomLinePostFecCurrent15StatInvSesPortn_Object = MibTableColumn
rm10010PerfTelecomLinePostFecCurrent15StatInvSesPortn = _Rm10010PerfTelecomLinePostFecCurrent15StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 192, 1, 6),
    _Rm10010PerfTelecomLinePostFecCurrent15StatInvSesPortn_Type()
)
rm10010PerfTelecomLinePostFecCurrent15StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomLinePostFecCurrent15StatInvSesPortn.setStatus("current")
_Rm10010PerfTelecomLinePostFecCurrent15StatSesValuePortn_Type = Unsigned32
_Rm10010PerfTelecomLinePostFecCurrent15StatSesValuePortn_Object = MibTableColumn
rm10010PerfTelecomLinePostFecCurrent15StatSesValuePortn = _Rm10010PerfTelecomLinePostFecCurrent15StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 192, 1, 7),
    _Rm10010PerfTelecomLinePostFecCurrent15StatSesValuePortn_Type()
)
rm10010PerfTelecomLinePostFecCurrent15StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomLinePostFecCurrent15StatSesValuePortn.setStatus("current")
_Rm10010PerfTelecomLinePostFecCurrent15StatInvSefsPortn_Type = EkiOnOff
_Rm10010PerfTelecomLinePostFecCurrent15StatInvSefsPortn_Object = MibTableColumn
rm10010PerfTelecomLinePostFecCurrent15StatInvSefsPortn = _Rm10010PerfTelecomLinePostFecCurrent15StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 192, 1, 8),
    _Rm10010PerfTelecomLinePostFecCurrent15StatInvSefsPortn_Type()
)
rm10010PerfTelecomLinePostFecCurrent15StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomLinePostFecCurrent15StatInvSefsPortn.setStatus("current")
_Rm10010PerfTelecomLinePostFecCurrent15StatSefsValuePortn_Type = Unsigned32
_Rm10010PerfTelecomLinePostFecCurrent15StatSefsValuePortn_Object = MibTableColumn
rm10010PerfTelecomLinePostFecCurrent15StatSefsValuePortn = _Rm10010PerfTelecomLinePostFecCurrent15StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 192, 1, 9),
    _Rm10010PerfTelecomLinePostFecCurrent15StatSefsValuePortn_Type()
)
rm10010PerfTelecomLinePostFecCurrent15StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomLinePostFecCurrent15StatSefsValuePortn.setStatus("current")
_Rm10010PerfTelecomLinePostFecCurrent15StatInvUasPortn_Type = EkiOnOff
_Rm10010PerfTelecomLinePostFecCurrent15StatInvUasPortn_Object = MibTableColumn
rm10010PerfTelecomLinePostFecCurrent15StatInvUasPortn = _Rm10010PerfTelecomLinePostFecCurrent15StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 192, 1, 10),
    _Rm10010PerfTelecomLinePostFecCurrent15StatInvUasPortn_Type()
)
rm10010PerfTelecomLinePostFecCurrent15StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomLinePostFecCurrent15StatInvUasPortn.setStatus("current")
_Rm10010PerfTelecomLinePostFecCurrent15StatUasValuePortn_Type = Unsigned32
_Rm10010PerfTelecomLinePostFecCurrent15StatUasValuePortn_Object = MibTableColumn
rm10010PerfTelecomLinePostFecCurrent15StatUasValuePortn = _Rm10010PerfTelecomLinePostFecCurrent15StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 192, 1, 11),
    _Rm10010PerfTelecomLinePostFecCurrent15StatUasValuePortn_Type()
)
rm10010PerfTelecomLinePostFecCurrent15StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomLinePostFecCurrent15StatUasValuePortn.setStatus("current")
_Rm10010PerfTelecomLinePostFecPast15StatHistoryPort1Table_Object = MibTable
rm10010PerfTelecomLinePostFecPast15StatHistoryPort1Table = _Rm10010PerfTelecomLinePostFecPast15StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 193)
)
if mibBuilder.loadTexts:
    rm10010PerfTelecomLinePostFecPast15StatHistoryPort1Table.setStatus("current")
_Rm10010PerfTelecomLinePostFecPast15StatHistoryPort1Entry_Object = MibTableRow
rm10010PerfTelecomLinePostFecPast15StatHistoryPort1Entry = _Rm10010PerfTelecomLinePostFecPast15StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 193, 1)
)
rm10010PerfTelecomLinePostFecPast15StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010PerfTelecomLinePostFecPast15StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    rm10010PerfTelecomLinePostFecPast15StatHistoryPort1Entry.setStatus("current")


class _Rm10010PerfTelecomLinePostFecPast15StatHistoryPort1Index_Type(Integer32):
    """Custom type rm10010PerfTelecomLinePostFecPast15StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010PerfTelecomLinePostFecPast15StatHistoryPort1Index_Type.__name__ = "Integer32"
_Rm10010PerfTelecomLinePostFecPast15StatHistoryPort1Index_Object = MibTableColumn
rm10010PerfTelecomLinePostFecPast15StatHistoryPort1Index = _Rm10010PerfTelecomLinePostFecPast15StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 193, 1, 1),
    _Rm10010PerfTelecomLinePostFecPast15StatHistoryPort1Index_Type()
)
rm10010PerfTelecomLinePostFecPast15StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomLinePostFecPast15StatHistoryPort1Index.setStatus("current")
_Rm10010PerfTelecomLinePostFecPast15StatHistoryInvCvPort1_Type = EkiOnOff
_Rm10010PerfTelecomLinePostFecPast15StatHistoryInvCvPort1_Object = MibTableColumn
rm10010PerfTelecomLinePostFecPast15StatHistoryInvCvPort1 = _Rm10010PerfTelecomLinePostFecPast15StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 193, 1, 2),
    _Rm10010PerfTelecomLinePostFecPast15StatHistoryInvCvPort1_Type()
)
rm10010PerfTelecomLinePostFecPast15StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomLinePostFecPast15StatHistoryInvCvPort1.setStatus("current")
_Rm10010PerfTelecomLinePostFecPast15StatHistoryCvValuePort1_Type = Unsigned32
_Rm10010PerfTelecomLinePostFecPast15StatHistoryCvValuePort1_Object = MibTableColumn
rm10010PerfTelecomLinePostFecPast15StatHistoryCvValuePort1 = _Rm10010PerfTelecomLinePostFecPast15StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 193, 1, 3),
    _Rm10010PerfTelecomLinePostFecPast15StatHistoryCvValuePort1_Type()
)
rm10010PerfTelecomLinePostFecPast15StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomLinePostFecPast15StatHistoryCvValuePort1.setStatus("current")
_Rm10010PerfTelecomLinePostFecPast15StatHistoryInvEsPort1_Type = EkiOnOff
_Rm10010PerfTelecomLinePostFecPast15StatHistoryInvEsPort1_Object = MibTableColumn
rm10010PerfTelecomLinePostFecPast15StatHistoryInvEsPort1 = _Rm10010PerfTelecomLinePostFecPast15StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 193, 1, 4),
    _Rm10010PerfTelecomLinePostFecPast15StatHistoryInvEsPort1_Type()
)
rm10010PerfTelecomLinePostFecPast15StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomLinePostFecPast15StatHistoryInvEsPort1.setStatus("current")
_Rm10010PerfTelecomLinePostFecPast15StatHistoryEsValuePort1_Type = Unsigned32
_Rm10010PerfTelecomLinePostFecPast15StatHistoryEsValuePort1_Object = MibTableColumn
rm10010PerfTelecomLinePostFecPast15StatHistoryEsValuePort1 = _Rm10010PerfTelecomLinePostFecPast15StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 193, 1, 5),
    _Rm10010PerfTelecomLinePostFecPast15StatHistoryEsValuePort1_Type()
)
rm10010PerfTelecomLinePostFecPast15StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomLinePostFecPast15StatHistoryEsValuePort1.setStatus("current")
_Rm10010PerfTelecomLinePostFecPast15StatHistoryInvSesPort1_Type = EkiOnOff
_Rm10010PerfTelecomLinePostFecPast15StatHistoryInvSesPort1_Object = MibTableColumn
rm10010PerfTelecomLinePostFecPast15StatHistoryInvSesPort1 = _Rm10010PerfTelecomLinePostFecPast15StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 193, 1, 6),
    _Rm10010PerfTelecomLinePostFecPast15StatHistoryInvSesPort1_Type()
)
rm10010PerfTelecomLinePostFecPast15StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomLinePostFecPast15StatHistoryInvSesPort1.setStatus("current")
_Rm10010PerfTelecomLinePostFecPast15StatHistorySesValuePort1_Type = Unsigned32
_Rm10010PerfTelecomLinePostFecPast15StatHistorySesValuePort1_Object = MibTableColumn
rm10010PerfTelecomLinePostFecPast15StatHistorySesValuePort1 = _Rm10010PerfTelecomLinePostFecPast15StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 193, 1, 7),
    _Rm10010PerfTelecomLinePostFecPast15StatHistorySesValuePort1_Type()
)
rm10010PerfTelecomLinePostFecPast15StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomLinePostFecPast15StatHistorySesValuePort1.setStatus("current")
_Rm10010PerfTelecomLinePostFecPast15StatHistoryInvSefsPort1_Type = EkiOnOff
_Rm10010PerfTelecomLinePostFecPast15StatHistoryInvSefsPort1_Object = MibTableColumn
rm10010PerfTelecomLinePostFecPast15StatHistoryInvSefsPort1 = _Rm10010PerfTelecomLinePostFecPast15StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 193, 1, 8),
    _Rm10010PerfTelecomLinePostFecPast15StatHistoryInvSefsPort1_Type()
)
rm10010PerfTelecomLinePostFecPast15StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomLinePostFecPast15StatHistoryInvSefsPort1.setStatus("current")
_Rm10010PerfTelecomLinePostFecPast15StatHistorySefsValuePort1_Type = Unsigned32
_Rm10010PerfTelecomLinePostFecPast15StatHistorySefsValuePort1_Object = MibTableColumn
rm10010PerfTelecomLinePostFecPast15StatHistorySefsValuePort1 = _Rm10010PerfTelecomLinePostFecPast15StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 193, 1, 9),
    _Rm10010PerfTelecomLinePostFecPast15StatHistorySefsValuePort1_Type()
)
rm10010PerfTelecomLinePostFecPast15StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomLinePostFecPast15StatHistorySefsValuePort1.setStatus("current")
_Rm10010PerfTelecomLinePostFecPast15StatHistoryInvUasPort1_Type = EkiOnOff
_Rm10010PerfTelecomLinePostFecPast15StatHistoryInvUasPort1_Object = MibTableColumn
rm10010PerfTelecomLinePostFecPast15StatHistoryInvUasPort1 = _Rm10010PerfTelecomLinePostFecPast15StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 193, 1, 10),
    _Rm10010PerfTelecomLinePostFecPast15StatHistoryInvUasPort1_Type()
)
rm10010PerfTelecomLinePostFecPast15StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomLinePostFecPast15StatHistoryInvUasPort1.setStatus("current")
_Rm10010PerfTelecomLinePostFecPast15StatHistoryUasValuePort1_Type = Unsigned32
_Rm10010PerfTelecomLinePostFecPast15StatHistoryUasValuePort1_Object = MibTableColumn
rm10010PerfTelecomLinePostFecPast15StatHistoryUasValuePort1 = _Rm10010PerfTelecomLinePostFecPast15StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 193, 1, 11),
    _Rm10010PerfTelecomLinePostFecPast15StatHistoryUasValuePort1_Type()
)
rm10010PerfTelecomLinePostFecPast15StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomLinePostFecPast15StatHistoryUasValuePort1.setStatus("current")
_Rm10010PerfTelecomLinePostFecCurrent24StatTable_Object = MibTable
rm10010PerfTelecomLinePostFecCurrent24StatTable = _Rm10010PerfTelecomLinePostFecCurrent24StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 194)
)
if mibBuilder.loadTexts:
    rm10010PerfTelecomLinePostFecCurrent24StatTable.setStatus("current")
_Rm10010PerfTelecomLinePostFecCurrent24StatEntry_Object = MibTableRow
rm10010PerfTelecomLinePostFecCurrent24StatEntry = _Rm10010PerfTelecomLinePostFecCurrent24StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 194, 1)
)
rm10010PerfTelecomLinePostFecCurrent24StatEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010PerfTelecomLinePostFecCurrent24StatIndex"),
)
if mibBuilder.loadTexts:
    rm10010PerfTelecomLinePostFecCurrent24StatEntry.setStatus("current")


class _Rm10010PerfTelecomLinePostFecCurrent24StatIndex_Type(Integer32):
    """Custom type rm10010PerfTelecomLinePostFecCurrent24StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010PerfTelecomLinePostFecCurrent24StatIndex_Type.__name__ = "Integer32"
_Rm10010PerfTelecomLinePostFecCurrent24StatIndex_Object = MibTableColumn
rm10010PerfTelecomLinePostFecCurrent24StatIndex = _Rm10010PerfTelecomLinePostFecCurrent24StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 194, 1, 1),
    _Rm10010PerfTelecomLinePostFecCurrent24StatIndex_Type()
)
rm10010PerfTelecomLinePostFecCurrent24StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomLinePostFecCurrent24StatIndex.setStatus("current")
_Rm10010PerfTelecomLinePostFecCurrent24StatInvCvPortn_Type = EkiOnOff
_Rm10010PerfTelecomLinePostFecCurrent24StatInvCvPortn_Object = MibTableColumn
rm10010PerfTelecomLinePostFecCurrent24StatInvCvPortn = _Rm10010PerfTelecomLinePostFecCurrent24StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 194, 1, 2),
    _Rm10010PerfTelecomLinePostFecCurrent24StatInvCvPortn_Type()
)
rm10010PerfTelecomLinePostFecCurrent24StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomLinePostFecCurrent24StatInvCvPortn.setStatus("current")
_Rm10010PerfTelecomLinePostFecCurrent24StatCvValuePortn_Type = Unsigned32
_Rm10010PerfTelecomLinePostFecCurrent24StatCvValuePortn_Object = MibTableColumn
rm10010PerfTelecomLinePostFecCurrent24StatCvValuePortn = _Rm10010PerfTelecomLinePostFecCurrent24StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 194, 1, 3),
    _Rm10010PerfTelecomLinePostFecCurrent24StatCvValuePortn_Type()
)
rm10010PerfTelecomLinePostFecCurrent24StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomLinePostFecCurrent24StatCvValuePortn.setStatus("current")
_Rm10010PerfTelecomLinePostFecCurrent24StatInvEsPortn_Type = EkiOnOff
_Rm10010PerfTelecomLinePostFecCurrent24StatInvEsPortn_Object = MibTableColumn
rm10010PerfTelecomLinePostFecCurrent24StatInvEsPortn = _Rm10010PerfTelecomLinePostFecCurrent24StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 194, 1, 4),
    _Rm10010PerfTelecomLinePostFecCurrent24StatInvEsPortn_Type()
)
rm10010PerfTelecomLinePostFecCurrent24StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomLinePostFecCurrent24StatInvEsPortn.setStatus("current")
_Rm10010PerfTelecomLinePostFecCurrent24StatEsValuePortn_Type = Unsigned32
_Rm10010PerfTelecomLinePostFecCurrent24StatEsValuePortn_Object = MibTableColumn
rm10010PerfTelecomLinePostFecCurrent24StatEsValuePortn = _Rm10010PerfTelecomLinePostFecCurrent24StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 194, 1, 5),
    _Rm10010PerfTelecomLinePostFecCurrent24StatEsValuePortn_Type()
)
rm10010PerfTelecomLinePostFecCurrent24StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomLinePostFecCurrent24StatEsValuePortn.setStatus("current")
_Rm10010PerfTelecomLinePostFecCurrent24StatInvSesPortn_Type = EkiOnOff
_Rm10010PerfTelecomLinePostFecCurrent24StatInvSesPortn_Object = MibTableColumn
rm10010PerfTelecomLinePostFecCurrent24StatInvSesPortn = _Rm10010PerfTelecomLinePostFecCurrent24StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 194, 1, 6),
    _Rm10010PerfTelecomLinePostFecCurrent24StatInvSesPortn_Type()
)
rm10010PerfTelecomLinePostFecCurrent24StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomLinePostFecCurrent24StatInvSesPortn.setStatus("current")
_Rm10010PerfTelecomLinePostFecCurrent24StatSesValuePortn_Type = Unsigned32
_Rm10010PerfTelecomLinePostFecCurrent24StatSesValuePortn_Object = MibTableColumn
rm10010PerfTelecomLinePostFecCurrent24StatSesValuePortn = _Rm10010PerfTelecomLinePostFecCurrent24StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 194, 1, 7),
    _Rm10010PerfTelecomLinePostFecCurrent24StatSesValuePortn_Type()
)
rm10010PerfTelecomLinePostFecCurrent24StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomLinePostFecCurrent24StatSesValuePortn.setStatus("current")
_Rm10010PerfTelecomLinePostFecCurrent24StatInvSefsPortn_Type = EkiOnOff
_Rm10010PerfTelecomLinePostFecCurrent24StatInvSefsPortn_Object = MibTableColumn
rm10010PerfTelecomLinePostFecCurrent24StatInvSefsPortn = _Rm10010PerfTelecomLinePostFecCurrent24StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 194, 1, 8),
    _Rm10010PerfTelecomLinePostFecCurrent24StatInvSefsPortn_Type()
)
rm10010PerfTelecomLinePostFecCurrent24StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomLinePostFecCurrent24StatInvSefsPortn.setStatus("current")
_Rm10010PerfTelecomLinePostFecCurrent24StatSefsValuePortn_Type = Unsigned32
_Rm10010PerfTelecomLinePostFecCurrent24StatSefsValuePortn_Object = MibTableColumn
rm10010PerfTelecomLinePostFecCurrent24StatSefsValuePortn = _Rm10010PerfTelecomLinePostFecCurrent24StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 194, 1, 9),
    _Rm10010PerfTelecomLinePostFecCurrent24StatSefsValuePortn_Type()
)
rm10010PerfTelecomLinePostFecCurrent24StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomLinePostFecCurrent24StatSefsValuePortn.setStatus("current")
_Rm10010PerfTelecomLinePostFecCurrent24StatInvUasPortn_Type = EkiOnOff
_Rm10010PerfTelecomLinePostFecCurrent24StatInvUasPortn_Object = MibTableColumn
rm10010PerfTelecomLinePostFecCurrent24StatInvUasPortn = _Rm10010PerfTelecomLinePostFecCurrent24StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 194, 1, 10),
    _Rm10010PerfTelecomLinePostFecCurrent24StatInvUasPortn_Type()
)
rm10010PerfTelecomLinePostFecCurrent24StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomLinePostFecCurrent24StatInvUasPortn.setStatus("current")
_Rm10010PerfTelecomLinePostFecCurrent24StatUasValuePortn_Type = Unsigned32
_Rm10010PerfTelecomLinePostFecCurrent24StatUasValuePortn_Object = MibTableColumn
rm10010PerfTelecomLinePostFecCurrent24StatUasValuePortn = _Rm10010PerfTelecomLinePostFecCurrent24StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 194, 1, 11),
    _Rm10010PerfTelecomLinePostFecCurrent24StatUasValuePortn_Type()
)
rm10010PerfTelecomLinePostFecCurrent24StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomLinePostFecCurrent24StatUasValuePortn.setStatus("current")
_Rm10010PerfTelecomLinePostFecPast24StatHistoryPort1Table_Object = MibTable
rm10010PerfTelecomLinePostFecPast24StatHistoryPort1Table = _Rm10010PerfTelecomLinePostFecPast24StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 195)
)
if mibBuilder.loadTexts:
    rm10010PerfTelecomLinePostFecPast24StatHistoryPort1Table.setStatus("current")
_Rm10010PerfTelecomLinePostFecPast24StatHistoryPort1Entry_Object = MibTableRow
rm10010PerfTelecomLinePostFecPast24StatHistoryPort1Entry = _Rm10010PerfTelecomLinePostFecPast24StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 195, 1)
)
rm10010PerfTelecomLinePostFecPast24StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010PerfTelecomLinePostFecPast24StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    rm10010PerfTelecomLinePostFecPast24StatHistoryPort1Entry.setStatus("current")


class _Rm10010PerfTelecomLinePostFecPast24StatHistoryPort1Index_Type(Integer32):
    """Custom type rm10010PerfTelecomLinePostFecPast24StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010PerfTelecomLinePostFecPast24StatHistoryPort1Index_Type.__name__ = "Integer32"
_Rm10010PerfTelecomLinePostFecPast24StatHistoryPort1Index_Object = MibTableColumn
rm10010PerfTelecomLinePostFecPast24StatHistoryPort1Index = _Rm10010PerfTelecomLinePostFecPast24StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 195, 1, 1),
    _Rm10010PerfTelecomLinePostFecPast24StatHistoryPort1Index_Type()
)
rm10010PerfTelecomLinePostFecPast24StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomLinePostFecPast24StatHistoryPort1Index.setStatus("current")
_Rm10010PerfTelecomLinePostFecPast24StatHistoryInvCvPort1_Type = EkiOnOff
_Rm10010PerfTelecomLinePostFecPast24StatHistoryInvCvPort1_Object = MibTableColumn
rm10010PerfTelecomLinePostFecPast24StatHistoryInvCvPort1 = _Rm10010PerfTelecomLinePostFecPast24StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 195, 1, 2),
    _Rm10010PerfTelecomLinePostFecPast24StatHistoryInvCvPort1_Type()
)
rm10010PerfTelecomLinePostFecPast24StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomLinePostFecPast24StatHistoryInvCvPort1.setStatus("current")
_Rm10010PerfTelecomLinePostFecPast24StatHistoryCvValuePort1_Type = Unsigned32
_Rm10010PerfTelecomLinePostFecPast24StatHistoryCvValuePort1_Object = MibTableColumn
rm10010PerfTelecomLinePostFecPast24StatHistoryCvValuePort1 = _Rm10010PerfTelecomLinePostFecPast24StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 195, 1, 3),
    _Rm10010PerfTelecomLinePostFecPast24StatHistoryCvValuePort1_Type()
)
rm10010PerfTelecomLinePostFecPast24StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomLinePostFecPast24StatHistoryCvValuePort1.setStatus("current")
_Rm10010PerfTelecomLinePostFecPast24StatHistoryInvEsPort1_Type = EkiOnOff
_Rm10010PerfTelecomLinePostFecPast24StatHistoryInvEsPort1_Object = MibTableColumn
rm10010PerfTelecomLinePostFecPast24StatHistoryInvEsPort1 = _Rm10010PerfTelecomLinePostFecPast24StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 195, 1, 4),
    _Rm10010PerfTelecomLinePostFecPast24StatHistoryInvEsPort1_Type()
)
rm10010PerfTelecomLinePostFecPast24StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomLinePostFecPast24StatHistoryInvEsPort1.setStatus("current")
_Rm10010PerfTelecomLinePostFecPast24StatHistoryEsValuePort1_Type = Unsigned32
_Rm10010PerfTelecomLinePostFecPast24StatHistoryEsValuePort1_Object = MibTableColumn
rm10010PerfTelecomLinePostFecPast24StatHistoryEsValuePort1 = _Rm10010PerfTelecomLinePostFecPast24StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 195, 1, 5),
    _Rm10010PerfTelecomLinePostFecPast24StatHistoryEsValuePort1_Type()
)
rm10010PerfTelecomLinePostFecPast24StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomLinePostFecPast24StatHistoryEsValuePort1.setStatus("current")
_Rm10010PerfTelecomLinePostFecPast24StatHistoryInvSesPort1_Type = EkiOnOff
_Rm10010PerfTelecomLinePostFecPast24StatHistoryInvSesPort1_Object = MibTableColumn
rm10010PerfTelecomLinePostFecPast24StatHistoryInvSesPort1 = _Rm10010PerfTelecomLinePostFecPast24StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 195, 1, 6),
    _Rm10010PerfTelecomLinePostFecPast24StatHistoryInvSesPort1_Type()
)
rm10010PerfTelecomLinePostFecPast24StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomLinePostFecPast24StatHistoryInvSesPort1.setStatus("current")
_Rm10010PerfTelecomLinePostFecPast24StatHistorySesValuePort1_Type = Unsigned32
_Rm10010PerfTelecomLinePostFecPast24StatHistorySesValuePort1_Object = MibTableColumn
rm10010PerfTelecomLinePostFecPast24StatHistorySesValuePort1 = _Rm10010PerfTelecomLinePostFecPast24StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 195, 1, 7),
    _Rm10010PerfTelecomLinePostFecPast24StatHistorySesValuePort1_Type()
)
rm10010PerfTelecomLinePostFecPast24StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomLinePostFecPast24StatHistorySesValuePort1.setStatus("current")
_Rm10010PerfTelecomLinePostFecPast24StatHistoryInvSefsPort1_Type = EkiOnOff
_Rm10010PerfTelecomLinePostFecPast24StatHistoryInvSefsPort1_Object = MibTableColumn
rm10010PerfTelecomLinePostFecPast24StatHistoryInvSefsPort1 = _Rm10010PerfTelecomLinePostFecPast24StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 195, 1, 8),
    _Rm10010PerfTelecomLinePostFecPast24StatHistoryInvSefsPort1_Type()
)
rm10010PerfTelecomLinePostFecPast24StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomLinePostFecPast24StatHistoryInvSefsPort1.setStatus("current")
_Rm10010PerfTelecomLinePostFecPast24StatHistorySefsValuePort1_Type = Unsigned32
_Rm10010PerfTelecomLinePostFecPast24StatHistorySefsValuePort1_Object = MibTableColumn
rm10010PerfTelecomLinePostFecPast24StatHistorySefsValuePort1 = _Rm10010PerfTelecomLinePostFecPast24StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 195, 1, 9),
    _Rm10010PerfTelecomLinePostFecPast24StatHistorySefsValuePort1_Type()
)
rm10010PerfTelecomLinePostFecPast24StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomLinePostFecPast24StatHistorySefsValuePort1.setStatus("current")
_Rm10010PerfTelecomLinePostFecPast24StatHistoryInvUasPort1_Type = EkiOnOff
_Rm10010PerfTelecomLinePostFecPast24StatHistoryInvUasPort1_Object = MibTableColumn
rm10010PerfTelecomLinePostFecPast24StatHistoryInvUasPort1 = _Rm10010PerfTelecomLinePostFecPast24StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 195, 1, 10),
    _Rm10010PerfTelecomLinePostFecPast24StatHistoryInvUasPort1_Type()
)
rm10010PerfTelecomLinePostFecPast24StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomLinePostFecPast24StatHistoryInvUasPort1.setStatus("current")
_Rm10010PerfTelecomLinePostFecPast24StatHistoryUasValuePort1_Type = Unsigned32
_Rm10010PerfTelecomLinePostFecPast24StatHistoryUasValuePort1_Object = MibTableColumn
rm10010PerfTelecomLinePostFecPast24StatHistoryUasValuePort1 = _Rm10010PerfTelecomLinePostFecPast24StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 195, 1, 11),
    _Rm10010PerfTelecomLinePostFecPast24StatHistoryUasValuePort1_Type()
)
rm10010PerfTelecomLinePostFecPast24StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomLinePostFecPast24StatHistoryUasValuePort1.setStatus("current")
_Rm10010PerfTelecomBerLinePreFecCurrent15StatTable_Object = MibTable
rm10010PerfTelecomBerLinePreFecCurrent15StatTable = _Rm10010PerfTelecomBerLinePreFecCurrent15StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 208)
)
if mibBuilder.loadTexts:
    rm10010PerfTelecomBerLinePreFecCurrent15StatTable.setStatus("current")
_Rm10010PerfTelecomBerLinePreFecCurrent15StatEntry_Object = MibTableRow
rm10010PerfTelecomBerLinePreFecCurrent15StatEntry = _Rm10010PerfTelecomBerLinePreFecCurrent15StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 208, 1)
)
rm10010PerfTelecomBerLinePreFecCurrent15StatEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010PerfTelecomBerLinePreFecCurrent15StatIndex"),
)
if mibBuilder.loadTexts:
    rm10010PerfTelecomBerLinePreFecCurrent15StatEntry.setStatus("current")


class _Rm10010PerfTelecomBerLinePreFecCurrent15StatIndex_Type(Integer32):
    """Custom type rm10010PerfTelecomBerLinePreFecCurrent15StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010PerfTelecomBerLinePreFecCurrent15StatIndex_Type.__name__ = "Integer32"
_Rm10010PerfTelecomBerLinePreFecCurrent15StatIndex_Object = MibTableColumn
rm10010PerfTelecomBerLinePreFecCurrent15StatIndex = _Rm10010PerfTelecomBerLinePreFecCurrent15StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 208, 1, 1),
    _Rm10010PerfTelecomBerLinePreFecCurrent15StatIndex_Type()
)
rm10010PerfTelecomBerLinePreFecCurrent15StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomBerLinePreFecCurrent15StatIndex.setStatus("current")
_Rm10010PerfTelecomBerLinePreFecCurrent15StatInvBerPortn_Type = EkiOnOff
_Rm10010PerfTelecomBerLinePreFecCurrent15StatInvBerPortn_Object = MibTableColumn
rm10010PerfTelecomBerLinePreFecCurrent15StatInvBerPortn = _Rm10010PerfTelecomBerLinePreFecCurrent15StatInvBerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 208, 1, 2),
    _Rm10010PerfTelecomBerLinePreFecCurrent15StatInvBerPortn_Type()
)
rm10010PerfTelecomBerLinePreFecCurrent15StatInvBerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomBerLinePreFecCurrent15StatInvBerPortn.setStatus("current")
_Rm10010PerfTelecomBerLinePreFecCurrent15StatBerValuePortn_Type = Unsigned32
_Rm10010PerfTelecomBerLinePreFecCurrent15StatBerValuePortn_Object = MibTableColumn
rm10010PerfTelecomBerLinePreFecCurrent15StatBerValuePortn = _Rm10010PerfTelecomBerLinePreFecCurrent15StatBerValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 208, 1, 3),
    _Rm10010PerfTelecomBerLinePreFecCurrent15StatBerValuePortn_Type()
)
rm10010PerfTelecomBerLinePreFecCurrent15StatBerValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomBerLinePreFecCurrent15StatBerValuePortn.setStatus("current")
_Rm10010PerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn_Type = EkiOnOff
_Rm10010PerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn_Object = MibTableColumn
rm10010PerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn = _Rm10010PerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 208, 1, 4),
    _Rm10010PerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn_Type()
)
rm10010PerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn.setStatus("current")
_Rm10010PerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn_Type = Unsigned32
_Rm10010PerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn_Object = MibTableColumn
rm10010PerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn = _Rm10010PerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 208, 1, 5),
    _Rm10010PerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn_Type()
)
rm10010PerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn.setStatus("current")
_Rm10010PerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn_Type = EkiOnOff
_Rm10010PerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn_Object = MibTableColumn
rm10010PerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn = _Rm10010PerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 208, 1, 6),
    _Rm10010PerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn_Type()
)
rm10010PerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn.setStatus("current")
_Rm10010PerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn_Type = Unsigned32
_Rm10010PerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn_Object = MibTableColumn
rm10010PerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn = _Rm10010PerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 208, 1, 7),
    _Rm10010PerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn_Type()
)
rm10010PerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn.setStatus("current")
_Rm10010PerfTelecomBerLinePreFecPast15StatHistoryPort1Table_Object = MibTable
rm10010PerfTelecomBerLinePreFecPast15StatHistoryPort1Table = _Rm10010PerfTelecomBerLinePreFecPast15StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 209)
)
if mibBuilder.loadTexts:
    rm10010PerfTelecomBerLinePreFecPast15StatHistoryPort1Table.setStatus("current")
_Rm10010PerfTelecomBerLinePreFecPast15StatHistoryPort1Entry_Object = MibTableRow
rm10010PerfTelecomBerLinePreFecPast15StatHistoryPort1Entry = _Rm10010PerfTelecomBerLinePreFecPast15StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 209, 1)
)
rm10010PerfTelecomBerLinePreFecPast15StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010PerfTelecomBerLinePreFecPast15StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    rm10010PerfTelecomBerLinePreFecPast15StatHistoryPort1Entry.setStatus("current")


class _Rm10010PerfTelecomBerLinePreFecPast15StatHistoryPort1Index_Type(Integer32):
    """Custom type rm10010PerfTelecomBerLinePreFecPast15StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010PerfTelecomBerLinePreFecPast15StatHistoryPort1Index_Type.__name__ = "Integer32"
_Rm10010PerfTelecomBerLinePreFecPast15StatHistoryPort1Index_Object = MibTableColumn
rm10010PerfTelecomBerLinePreFecPast15StatHistoryPort1Index = _Rm10010PerfTelecomBerLinePreFecPast15StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 209, 1, 1),
    _Rm10010PerfTelecomBerLinePreFecPast15StatHistoryPort1Index_Type()
)
rm10010PerfTelecomBerLinePreFecPast15StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomBerLinePreFecPast15StatHistoryPort1Index.setStatus("current")
_Rm10010PerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1_Type = EkiOnOff
_Rm10010PerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1_Object = MibTableColumn
rm10010PerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1 = _Rm10010PerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 209, 1, 2),
    _Rm10010PerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1_Type()
)
rm10010PerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1.setStatus("current")
_Rm10010PerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1_Type = Unsigned32
_Rm10010PerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1_Object = MibTableColumn
rm10010PerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1 = _Rm10010PerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 209, 1, 3),
    _Rm10010PerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1_Type()
)
rm10010PerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1.setStatus("current")
_Rm10010PerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1_Type = EkiOnOff
_Rm10010PerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1_Object = MibTableColumn
rm10010PerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1 = _Rm10010PerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 209, 1, 4),
    _Rm10010PerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1_Type()
)
rm10010PerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1.setStatus("current")
_Rm10010PerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1_Type = Unsigned32
_Rm10010PerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1_Object = MibTableColumn
rm10010PerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1 = _Rm10010PerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 209, 1, 5),
    _Rm10010PerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1_Type()
)
rm10010PerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1.setStatus("current")
_Rm10010PerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1_Type = EkiOnOff
_Rm10010PerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1_Object = MibTableColumn
rm10010PerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1 = _Rm10010PerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 209, 1, 6),
    _Rm10010PerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1_Type()
)
rm10010PerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1.setStatus("current")
_Rm10010PerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1_Type = Unsigned32
_Rm10010PerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1_Object = MibTableColumn
rm10010PerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1 = _Rm10010PerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 209, 1, 7),
    _Rm10010PerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1_Type()
)
rm10010PerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1.setStatus("current")
_Rm10010PerfTelecomBerLinePreFecCurrent24StatTable_Object = MibTable
rm10010PerfTelecomBerLinePreFecCurrent24StatTable = _Rm10010PerfTelecomBerLinePreFecCurrent24StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 210)
)
if mibBuilder.loadTexts:
    rm10010PerfTelecomBerLinePreFecCurrent24StatTable.setStatus("current")
_Rm10010PerfTelecomBerLinePreFecCurrent24StatEntry_Object = MibTableRow
rm10010PerfTelecomBerLinePreFecCurrent24StatEntry = _Rm10010PerfTelecomBerLinePreFecCurrent24StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 210, 1)
)
rm10010PerfTelecomBerLinePreFecCurrent24StatEntry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010PerfTelecomBerLinePreFecCurrent24StatIndex"),
)
if mibBuilder.loadTexts:
    rm10010PerfTelecomBerLinePreFecCurrent24StatEntry.setStatus("current")


class _Rm10010PerfTelecomBerLinePreFecCurrent24StatIndex_Type(Integer32):
    """Custom type rm10010PerfTelecomBerLinePreFecCurrent24StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010PerfTelecomBerLinePreFecCurrent24StatIndex_Type.__name__ = "Integer32"
_Rm10010PerfTelecomBerLinePreFecCurrent24StatIndex_Object = MibTableColumn
rm10010PerfTelecomBerLinePreFecCurrent24StatIndex = _Rm10010PerfTelecomBerLinePreFecCurrent24StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 210, 1, 1),
    _Rm10010PerfTelecomBerLinePreFecCurrent24StatIndex_Type()
)
rm10010PerfTelecomBerLinePreFecCurrent24StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomBerLinePreFecCurrent24StatIndex.setStatus("current")
_Rm10010PerfTelecomBerLinePreFecCurrent24StatInvBerPortn_Type = EkiOnOff
_Rm10010PerfTelecomBerLinePreFecCurrent24StatInvBerPortn_Object = MibTableColumn
rm10010PerfTelecomBerLinePreFecCurrent24StatInvBerPortn = _Rm10010PerfTelecomBerLinePreFecCurrent24StatInvBerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 210, 1, 2),
    _Rm10010PerfTelecomBerLinePreFecCurrent24StatInvBerPortn_Type()
)
rm10010PerfTelecomBerLinePreFecCurrent24StatInvBerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomBerLinePreFecCurrent24StatInvBerPortn.setStatus("current")
_Rm10010PerfTelecomBerLinePreFecCurrent24StatBerValuePortn_Type = Unsigned32
_Rm10010PerfTelecomBerLinePreFecCurrent24StatBerValuePortn_Object = MibTableColumn
rm10010PerfTelecomBerLinePreFecCurrent24StatBerValuePortn = _Rm10010PerfTelecomBerLinePreFecCurrent24StatBerValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 210, 1, 3),
    _Rm10010PerfTelecomBerLinePreFecCurrent24StatBerValuePortn_Type()
)
rm10010PerfTelecomBerLinePreFecCurrent24StatBerValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomBerLinePreFecCurrent24StatBerValuePortn.setStatus("current")
_Rm10010PerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn_Type = EkiOnOff
_Rm10010PerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn_Object = MibTableColumn
rm10010PerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn = _Rm10010PerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 210, 1, 4),
    _Rm10010PerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn_Type()
)
rm10010PerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn.setStatus("current")
_Rm10010PerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn_Type = Unsigned32
_Rm10010PerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn_Object = MibTableColumn
rm10010PerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn = _Rm10010PerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 210, 1, 5),
    _Rm10010PerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn_Type()
)
rm10010PerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn.setStatus("current")
_Rm10010PerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn_Type = EkiOnOff
_Rm10010PerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn_Object = MibTableColumn
rm10010PerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn = _Rm10010PerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 210, 1, 6),
    _Rm10010PerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn_Type()
)
rm10010PerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn.setStatus("current")
_Rm10010PerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn_Type = Unsigned32
_Rm10010PerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn_Object = MibTableColumn
rm10010PerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn = _Rm10010PerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 210, 1, 7),
    _Rm10010PerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn_Type()
)
rm10010PerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn.setStatus("current")
_Rm10010PerfTelecomBerLinePreFecPast24StatHistoryPort1Table_Object = MibTable
rm10010PerfTelecomBerLinePreFecPast24StatHistoryPort1Table = _Rm10010PerfTelecomBerLinePreFecPast24StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 211)
)
if mibBuilder.loadTexts:
    rm10010PerfTelecomBerLinePreFecPast24StatHistoryPort1Table.setStatus("current")
_Rm10010PerfTelecomBerLinePreFecPast24StatHistoryPort1Entry_Object = MibTableRow
rm10010PerfTelecomBerLinePreFecPast24StatHistoryPort1Entry = _Rm10010PerfTelecomBerLinePreFecPast24StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 211, 1)
)
rm10010PerfTelecomBerLinePreFecPast24StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Rm10010-MIB", "rm10010PerfTelecomBerLinePreFecPast24StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    rm10010PerfTelecomBerLinePreFecPast24StatHistoryPort1Entry.setStatus("current")


class _Rm10010PerfTelecomBerLinePreFecPast24StatHistoryPort1Index_Type(Integer32):
    """Custom type rm10010PerfTelecomBerLinePreFecPast24StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010PerfTelecomBerLinePreFecPast24StatHistoryPort1Index_Type.__name__ = "Integer32"
_Rm10010PerfTelecomBerLinePreFecPast24StatHistoryPort1Index_Object = MibTableColumn
rm10010PerfTelecomBerLinePreFecPast24StatHistoryPort1Index = _Rm10010PerfTelecomBerLinePreFecPast24StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 211, 1, 1),
    _Rm10010PerfTelecomBerLinePreFecPast24StatHistoryPort1Index_Type()
)
rm10010PerfTelecomBerLinePreFecPast24StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomBerLinePreFecPast24StatHistoryPort1Index.setStatus("current")
_Rm10010PerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1_Type = EkiOnOff
_Rm10010PerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1_Object = MibTableColumn
rm10010PerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1 = _Rm10010PerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 211, 1, 2),
    _Rm10010PerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1_Type()
)
rm10010PerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1.setStatus("current")
_Rm10010PerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1_Type = Unsigned32
_Rm10010PerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1_Object = MibTableColumn
rm10010PerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1 = _Rm10010PerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 211, 1, 3),
    _Rm10010PerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1_Type()
)
rm10010PerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1.setStatus("current")
_Rm10010PerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1_Type = EkiOnOff
_Rm10010PerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1_Object = MibTableColumn
rm10010PerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1 = _Rm10010PerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 211, 1, 4),
    _Rm10010PerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1_Type()
)
rm10010PerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1.setStatus("current")
_Rm10010PerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1_Type = Unsigned32
_Rm10010PerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1_Object = MibTableColumn
rm10010PerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1 = _Rm10010PerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 211, 1, 5),
    _Rm10010PerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1_Type()
)
rm10010PerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1.setStatus("current")
_Rm10010PerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1_Type = EkiOnOff
_Rm10010PerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1_Object = MibTableColumn
rm10010PerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1 = _Rm10010PerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 211, 1, 6),
    _Rm10010PerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1_Type()
)
rm10010PerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1.setStatus("current")
_Rm10010PerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1_Type = Unsigned32
_Rm10010PerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1_Object = MibTableColumn
rm10010PerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1 = _Rm10010PerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 53, 11, 7, 211, 1, 7),
    _Rm10010PerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1_Type()
)
rm10010PerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010PerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1.setStatus("current")

# Managed Objects groups


# Notification objects

rm10010LineTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 53, 10, 30)
)
rm10010LineTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Rm10010-MIB", "rm10010AlmLineDdmWarningPortn"),
        ("EKINOPS-Rm10010-MIB", "rm10010trapLineNumber"),
        ("EKINOPS-Rm10010-MIB", "rm10010trapBoardNumber"))
)
if mibBuilder.loadTexts:
    rm10010LineTrapNotUrgentGoesOn.setStatus(
        "current"
    )

rm10010LineTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 53, 10, 31)
)
rm10010LineTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Rm10010-MIB", "rm10010AlmLineDdmWarningPortn"),
        ("EKINOPS-Rm10010-MIB", "rm10010trapLineNumber"),
        ("EKINOPS-Rm10010-MIB", "rm10010trapBoardNumber"))
)
if mibBuilder.loadTexts:
    rm10010LineTrapNotUrgentGoesOff.setStatus(
        "current"
    )

rm10010LineTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 53, 10, 32)
)
rm10010LineTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Rm10010-MIB", "rm10010AlmLineDdmAlmPortn"),
        ("EKINOPS-Rm10010-MIB", "rm10010trapLineNumber"),
        ("EKINOPS-Rm10010-MIB", "rm10010trapBoardNumber"))
)
if mibBuilder.loadTexts:
    rm10010LineTrapUrgentGoesOn.setStatus(
        "current"
    )

rm10010LineTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 53, 10, 33)
)
rm10010LineTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Rm10010-MIB", "rm10010AlmLineDdmAlmPortn"),
        ("EKINOPS-Rm10010-MIB", "rm10010trapLineNumber"),
        ("EKINOPS-Rm10010-MIB", "rm10010trapBoardNumber"))
)
if mibBuilder.loadTexts:
    rm10010LineTrapUrgentGoesOff.setStatus(
        "current"
    )

rm10010LineTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 53, 10, 34)
)
rm10010LineTrapCritGoesOn.setObjects(
      *(("EKINOPS-Rm10010-MIB", "rm10010AlmLineFailPortn"),
        ("EKINOPS-Rm10010-MIB", "rm10010AlmLineHwFailPortn"),
        ("EKINOPS-Rm10010-MIB", "rm10010trapLineNumber"),
        ("EKINOPS-Rm10010-MIB", "rm10010trapBoardNumber"))
)
if mibBuilder.loadTexts:
    rm10010LineTrapCritGoesOn.setStatus(
        "current"
    )

rm10010LineTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 53, 10, 35)
)
rm10010LineTrapCritGoesOff.setObjects(
      *(("EKINOPS-Rm10010-MIB", "rm10010AlmLineFailPortn"),
        ("EKINOPS-Rm10010-MIB", "rm10010AlmLineHwFailPortn"),
        ("EKINOPS-Rm10010-MIB", "rm10010trapLineNumber"),
        ("EKINOPS-Rm10010-MIB", "rm10010trapBoardNumber"))
)
if mibBuilder.loadTexts:
    rm10010LineTrapCritGoesOff.setStatus(
        "current"
    )

rm10010ClientTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 53, 10, 40)
)
rm10010ClientTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Rm10010-MIB", "rm10010AlmSfpDdmWarningPortn"),
        ("EKINOPS-Rm10010-MIB", "rm10010trapPortNumber"),
        ("EKINOPS-Rm10010-MIB", "rm10010trapBoardNumber"))
)
if mibBuilder.loadTexts:
    rm10010ClientTrapNotUrgentGoesOn.setStatus(
        "current"
    )

rm10010ClientTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 53, 10, 41)
)
rm10010ClientTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Rm10010-MIB", "rm10010AlmSfpDdmWarningPortn"),
        ("EKINOPS-Rm10010-MIB", "rm10010trapPortNumber"),
        ("EKINOPS-Rm10010-MIB", "rm10010trapBoardNumber"))
)
if mibBuilder.loadTexts:
    rm10010ClientTrapNotUrgentGoesOff.setStatus(
        "current"
    )

rm10010ClientTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 53, 10, 42)
)
rm10010ClientTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Rm10010-MIB", "rm10010AlmSfpDdmAlmPortn"),
        ("EKINOPS-Rm10010-MIB", "rm10010trapPortNumber"),
        ("EKINOPS-Rm10010-MIB", "rm10010trapBoardNumber"))
)
if mibBuilder.loadTexts:
    rm10010ClientTrapUrgentGoesOn.setStatus(
        "current"
    )

rm10010ClientTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 53, 10, 43)
)
rm10010ClientTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Rm10010-MIB", "rm10010AlmSfpDdmAlmPortn"),
        ("EKINOPS-Rm10010-MIB", "rm10010trapPortNumber"),
        ("EKINOPS-Rm10010-MIB", "rm10010trapBoardNumber"))
)
if mibBuilder.loadTexts:
    rm10010ClientTrapUrgentGoesOff.setStatus(
        "current"
    )

rm10010ClientTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 53, 10, 44)
)
rm10010ClientTrapCritGoesOn.setObjects(
      *(("EKINOPS-Rm10010-MIB", "rm10010AlmFailAccPortn"),
        ("EKINOPS-Rm10010-MIB", "rm10010AlmHwFailAccPortn"),
        ("EKINOPS-Rm10010-MIB", "rm10010trapPortNumber"),
        ("EKINOPS-Rm10010-MIB", "rm10010trapBoardNumber"))
)
if mibBuilder.loadTexts:
    rm10010ClientTrapCritGoesOn.setStatus(
        "current"
    )

rm10010ClientTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 53, 10, 45)
)
rm10010ClientTrapCritGoesOff.setObjects(
      *(("EKINOPS-Rm10010-MIB", "rm10010AlmFailAccPortn"),
        ("EKINOPS-Rm10010-MIB", "rm10010AlmHwFailAccPortn"),
        ("EKINOPS-Rm10010-MIB", "rm10010trapPortNumber"),
        ("EKINOPS-Rm10010-MIB", "rm10010trapBoardNumber"))
)
if mibBuilder.loadTexts:
    rm10010ClientTrapCritGoesOff.setStatus(
        "current"
    )

rm10010PowerTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 53, 10, 50)
)
rm10010PowerTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Rm10010-MIB", "rm10010AlmDefFuseB"),
        ("EKINOPS-Rm10010-MIB", "rm10010AlmDefFuseA"),
        ("EKINOPS-Rm10010-MIB", "rm10010trapBoardNumber"))
)
if mibBuilder.loadTexts:
    rm10010PowerTrapUrgentGoesOn.setStatus(
        "current"
    )

rm10010PowerTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 53, 10, 51)
)
rm10010PowerTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Rm10010-MIB", "rm10010AlmDefFuseB"),
        ("EKINOPS-Rm10010-MIB", "rm10010AlmDefFuseA"),
        ("EKINOPS-Rm10010-MIB", "rm10010trapBoardNumber"))
)
if mibBuilder.loadTexts:
    rm10010PowerTrapUrgentGoesOff.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EKINOPS-Rm10010-MIB",
    **{"Rm10010MultiRate": Rm10010MultiRate,
       "Rm10010OtxMode": Rm10010OtxMode,
       "Rm10010OtxGrid": Rm10010OtxGrid,
       "Rm10010AdjustValue": Rm10010AdjustValue,
       "Rm10010ClientProtocol": Rm10010ClientProtocol,
       "Rm10010ProtocolMode": Rm10010ProtocolMode,
       "Rm10010OtxChannel": Rm10010OtxChannel,
       "Rm10010OrxChannel": Rm10010OrxChannel,
       "moduleRm10010": moduleRm10010,
       "rm10010alarms": rm10010alarms,
       "rm10010AlmOther": rm10010AlmOther,
       "rm10010AlmOtherNurg": rm10010AlmOtherNurg,
       "rm10010AlmsynthAlm2": rm10010AlmsynthAlm2,
       "rm10010AlmConfTableSave": rm10010AlmConfTableSave,
       "rm10010AlmInvUpload": rm10010AlmInvUpload,
       "rm10010AlmConfTableLoad": rm10010AlmConfTableLoad,
       "rm10010AlmCorrelatOff": rm10010AlmCorrelatOff,
       "rm10010AlmMaintenanceOn": rm10010AlmMaintenanceOn,
       "rm10010AlmOtherUrg": rm10010AlmOtherUrg,
       "rm10010AlmmodFanFail": rm10010AlmmodFanFail,
       "rm10010AlmFanModuleAbsent": rm10010AlmFanModuleAbsent,
       "rm10010AlmFansFail": rm10010AlmFansFail,
       "rm10010AlmFan1Fail": rm10010AlmFan1Fail,
       "rm10010AlmFan2Fail": rm10010AlmFan2Fail,
       "rm10010AlmFan3Fail": rm10010AlmFan3Fail,
       "rm10010AlmFan4Fail": rm10010AlmFan4Fail,
       "rm10010AlmOtherCrit": rm10010AlmOtherCrit,
       "rm10010AlmsynthAlm0": rm10010AlmsynthAlm0,
       "rm10010AlmFailFan": rm10010AlmFailFan,
       "rm10010AlmModGlobFail": rm10010AlmModGlobFail,
       "rm10010AlmDefFuseA": rm10010AlmDefFuseA,
       "rm10010AlmDefFuseB": rm10010AlmDefFuseB,
       "rm10010AlmclientModuleState": rm10010AlmclientModuleState,
       "rm10010AlmCfpInitialize": rm10010AlmCfpInitialize,
       "rm10010AlmCfpLowPower": rm10010AlmCfpLowPower,
       "rm10010AlmCfpHighPowerUp": rm10010AlmCfpHighPowerUp,
       "rm10010AlmCfpTxOff": rm10010AlmCfpTxOff,
       "rm10010AlmCfpTxTurnOn": rm10010AlmCfpTxTurnOn,
       "rm10010AlmCfpReady": rm10010AlmCfpReady,
       "rm10010AlmCfpFault": rm10010AlmCfpFault,
       "rm10010AlmCfpTxTurnOff": rm10010AlmCfpTxTurnOff,
       "rm10010AlmCfpHighPowerDown": rm10010AlmCfpHighPowerDown,
       "rm10010AlmclientModuleGeneralStatus": rm10010AlmclientModuleGeneralStatus,
       "rm10010AlmCfpOutOfAlignment": rm10010AlmCfpOutOfAlignment,
       "rm10010AlmCfpRxNetworkLol": rm10010AlmCfpRxNetworkLol,
       "rm10010AlmCfpRxLos": rm10010AlmCfpRxLos,
       "rm10010AlmCfpTxHostLol": rm10010AlmCfpTxHostLol,
       "rm10010AlmCfpTxLosf": rm10010AlmCfpTxLosf,
       "rm10010AlmCfpTxCmuLol": rm10010AlmCfpTxCmuLol,
       "rm10010AlmCfpTxJitterPllLol": rm10010AlmCfpTxJitterPllLol,
       "rm10010AlmCfpLossOfRefclk": rm10010AlmCfpLossOfRefclk,
       "rm10010AlmCfpHwInterlock": rm10010AlmCfpHwInterlock,
       "rm10010AlmclientGlobalAlarmSummary": rm10010AlmclientGlobalAlarmSummary,
       "rm10010AlmCfpSoftGlobAlarmTest": rm10010AlmCfpSoftGlobAlarmTest,
       "rm10010AlmCfpNetworkLaneAlarmWarning2": rm10010AlmCfpNetworkLaneAlarmWarning2,
       "rm10010AlmCfpModuleState": rm10010AlmCfpModuleState,
       "rm10010AlmCfpModuleGeneralStatus": rm10010AlmCfpModuleGeneralStatus,
       "rm10010AlmCfpModuleFault": rm10010AlmCfpModuleFault,
       "rm10010AlmCfpModuleAlarmWarning1": rm10010AlmCfpModuleAlarmWarning1,
       "rm10010AlmCfpModuleAlarmWarning2": rm10010AlmCfpModuleAlarmWarning2,
       "rm10010AlmCfpNetworkLaneAlarmWarning1": rm10010AlmCfpNetworkLaneAlarmWarning1,
       "rm10010AlmCfpNetworkLaneFaultStatus": rm10010AlmCfpNetworkLaneFaultStatus,
       "rm10010AlmCfpHostLaneFaultStatus": rm10010AlmCfpHostLaneFaultStatus,
       "rm10010AlmCfpGlobAlarmAssertion": rm10010AlmCfpGlobAlarmAssertion,
       "rm10010AlmmsaModuleState": rm10010AlmmsaModuleState,
       "rm10010AlmMsaInitialize": rm10010AlmMsaInitialize,
       "rm10010AlmMsaLowPower": rm10010AlmMsaLowPower,
       "rm10010AlmMsaHighPowerUp": rm10010AlmMsaHighPowerUp,
       "rm10010AlmMsaTxOff": rm10010AlmMsaTxOff,
       "rm10010AlmMsaTxTurnOn": rm10010AlmMsaTxTurnOn,
       "rm10010AlmMsaReady": rm10010AlmMsaReady,
       "rm10010AlmMsaFault": rm10010AlmMsaFault,
       "rm10010AlmMsaTxTurnOff": rm10010AlmMsaTxTurnOff,
       "rm10010AlmMsaHighPowerDown": rm10010AlmMsaHighPowerDown,
       "rm10010AlmmsaModuleGeneralStatus": rm10010AlmmsaModuleGeneralStatus,
       "rm10010AlmMsaOutOfAlignment": rm10010AlmMsaOutOfAlignment,
       "rm10010AlmMsaRxNetworkLol": rm10010AlmMsaRxNetworkLol,
       "rm10010AlmMsaRxLos": rm10010AlmMsaRxLos,
       "rm10010AlmMsaTxHostLol": rm10010AlmMsaTxHostLol,
       "rm10010AlmMsaTxLosf": rm10010AlmMsaTxLosf,
       "rm10010AlmMsaTxCmuLol": rm10010AlmMsaTxCmuLol,
       "rm10010AlmMsaTxJitterPllLol": rm10010AlmMsaTxJitterPllLol,
       "rm10010AlmMsaLossOfRefclk": rm10010AlmMsaLossOfRefclk,
       "rm10010AlmMsaHwInterlock": rm10010AlmMsaHwInterlock,
       "rm10010AlmmsaGlobalAlarmSummary": rm10010AlmmsaGlobalAlarmSummary,
       "rm10010AlmMsaSoftGlobAlarmTest": rm10010AlmMsaSoftGlobAlarmTest,
       "rm10010AlmMsaNetworkHostAlarmStatus": rm10010AlmMsaNetworkHostAlarmStatus,
       "rm10010AlmMsaNetworkLaneAlarmWarning2": rm10010AlmMsaNetworkLaneAlarmWarning2,
       "rm10010AlmMsaModuleState": rm10010AlmMsaModuleState,
       "rm10010AlmMsaModuleGeneralStatus": rm10010AlmMsaModuleGeneralStatus,
       "rm10010AlmModuleFault": rm10010AlmModuleFault,
       "rm10010AlmMsaModuleAlarmWarning1": rm10010AlmMsaModuleAlarmWarning1,
       "rm10010AlmMsaModuleAlarmWarning2": rm10010AlmMsaModuleAlarmWarning2,
       "rm10010AlmMsaNetworkLaneAlarmWarning1": rm10010AlmMsaNetworkLaneAlarmWarning1,
       "rm10010AlmMsaNetworkLaneFaultStatus": rm10010AlmMsaNetworkLaneFaultStatus,
       "rm10010AlmMsaHostLaneFaultStatus": rm10010AlmMsaHostLaneFaultStatus,
       "rm10010AlmMsaGlobAlarmAssertion": rm10010AlmMsaGlobAlarmAssertion,
       "rm10010AlmmsaNetworkTxAlignment": rm10010AlmmsaNetworkTxAlignment,
       "rm10010AlmNetTxTimingFault": rm10010AlmNetTxTimingFault,
       "rm10010AlmNetTxReferenceClockFault": rm10010AlmNetTxReferenceClockFault,
       "rm10010AlmNetTxCmuLockFault": rm10010AlmNetTxCmuLockFault,
       "rm10010AlmNetTxOutOfAlignment": rm10010AlmNetTxOutOfAlignment,
       "rm10010AlmNetTxLossOfAlignment": rm10010AlmNetTxLossOfAlignment,
       "rm10010AlmmsaNetworkRxAlignment": rm10010AlmmsaNetworkRxAlignment,
       "rm10010AlmNetRxTimingFault": rm10010AlmNetRxTimingFault,
       "rm10010AlmNetRxOutOfAlignment": rm10010AlmNetRxOutOfAlignment,
       "rm10010AlmNetRxLossOfAlignment": rm10010AlmNetRxLossOfAlignment,
       "rm10010AlmNetRxModemLockFault": rm10010AlmNetRxModemLockFault,
       "rm10010AlmNetRxModemSyncDetectFault": rm10010AlmNetRxModemSyncDetectFault,
       "rm10010AlmmsaNetworkHostNetworkAlarmSummary": rm10010AlmmsaNetworkHostNetworkAlarmSummary,
       "rm10010AlmNetworkTxAlignment": rm10010AlmNetworkTxAlignment,
       "rm10010AlmNetworkRxAlignment": rm10010AlmNetworkRxAlignment,
       "rm10010AlmNetworkRxOtn": rm10010AlmNetworkRxOtn,
       "rm10010AlmHostRxAlignment": rm10010AlmHostRxAlignment,
       "rm10010AlmHostTxAlignment": rm10010AlmHostTxAlignment,
       "rm10010AlmHostTxOtnStatus": rm10010AlmHostTxOtnStatus,
       "rm10010AlmmsaHostTxAlignment": rm10010AlmmsaHostTxAlignment,
       "rm10010AlmHostTxDeskewLockFault": rm10010AlmHostTxDeskewLockFault,
       "rm10010AlmHostTxOutOfAlignment": rm10010AlmHostTxOutOfAlignment,
       "rm10010AlmHostTxLossOfAlignment": rm10010AlmHostTxLossOfAlignment,
       "rm10010AlmHostTxCdrLockFault": rm10010AlmHostTxCdrLockFault,
       "rm10010AlmmsaHostRxAlignment": rm10010AlmmsaHostRxAlignment,
       "rm10010AlmHostRxCmuLockFault": rm10010AlmHostRxCmuLockFault,
       "rm10010AlmHostRxOutOfAlignment": rm10010AlmHostRxOutOfAlignment,
       "rm10010AlmHostRxLossOfAlignment": rm10010AlmHostRxLossOfAlignment,
       "rm10010AlmClient": rm10010AlmClient,
       "rm10010AlmClientNurg": rm10010AlmClientNurg,
       "rm10010AlmclientNetworkLaneAlarmWarningTable": rm10010AlmclientNetworkLaneAlarmWarningTable,
       "rm10010AlmclientNetworkLaneAlarmWarningEntry": rm10010AlmclientNetworkLaneAlarmWarningEntry,
       "rm10010AlmclientNetworkLaneAlarmWarningIndex": rm10010AlmclientNetworkLaneAlarmWarningIndex,
       "rm10010AlmClientRxPowerLowAlarmPortn": rm10010AlmClientRxPowerLowAlarmPortn,
       "rm10010AlmClientRxPowerLowWarningPortn": rm10010AlmClientRxPowerLowWarningPortn,
       "rm10010AlmClientRxPowerHighWarningPortn": rm10010AlmClientRxPowerHighWarningPortn,
       "rm10010AlmClientRxPowerHighAlarmPortn": rm10010AlmClientRxPowerHighAlarmPortn,
       "rm10010AlmLaserTempLowAlarmPortn": rm10010AlmLaserTempLowAlarmPortn,
       "rm10010AlmClientLaserTempLowWarningPortn": rm10010AlmClientLaserTempLowWarningPortn,
       "rm10010AlmClientLaserTempHighWarningPortn": rm10010AlmClientLaserTempHighWarningPortn,
       "rm10010AlmClientLaserTempHighAlarmPortn": rm10010AlmClientLaserTempHighAlarmPortn,
       "rm10010AlmClientTxPowerLowAlarmPortn": rm10010AlmClientTxPowerLowAlarmPortn,
       "rm10010AlmClientTxPowerLowWarningPortn": rm10010AlmClientTxPowerLowWarningPortn,
       "rm10010AlmClientTxPowerHighWarningPortn": rm10010AlmClientTxPowerHighWarningPortn,
       "rm10010AlmClientTxPowerHighAlarmPortn": rm10010AlmClientTxPowerHighAlarmPortn,
       "rm10010AlmClientBiasLowAlarmPortn": rm10010AlmClientBiasLowAlarmPortn,
       "rm10010AlmClientBiasLowWarningPortn": rm10010AlmClientBiasLowWarningPortn,
       "rm10010AlmClientBiasHighWarningPortn": rm10010AlmClientBiasHighWarningPortn,
       "rm10010AlmClientBiasHighAlarmPortn": rm10010AlmClientBiasHighAlarmPortn,
       "rm10010AlmclientSfpWarnDdmTable": rm10010AlmclientSfpWarnDdmTable,
       "rm10010AlmclientSfpWarnDdmEntry": rm10010AlmclientSfpWarnDdmEntry,
       "rm10010AlmclientSfpWarnDdmIndex": rm10010AlmclientSfpWarnDdmIndex,
       "rm10010AlmTxPwLowWngPortn": rm10010AlmTxPwLowWngPortn,
       "rm10010AlmTxPwrHighWngPortn": rm10010AlmTxPwrHighWngPortn,
       "rm10010AlmTxBiasLowWngPortn": rm10010AlmTxBiasLowWngPortn,
       "rm10010AlmTxBiasHighWngPortn": rm10010AlmTxBiasHighWngPortn,
       "rm10010AlmVccLowWngPortn": rm10010AlmVccLowWngPortn,
       "rm10010AlmVccHighWngPortn": rm10010AlmVccHighWngPortn,
       "rm10010AlmTempLowWngPortn": rm10010AlmTempLowWngPortn,
       "rm10010AlmTempHighWngPortn": rm10010AlmTempHighWngPortn,
       "rm10010AlmRxPwrLowWngPortn": rm10010AlmRxPwrLowWngPortn,
       "rm10010AlmRxPwrHighWngPortn": rm10010AlmRxPwrHighWngPortn,
       "rm10010AlmClientUrg": rm10010AlmClientUrg,
       "rm10010AlmclientNetworkLaneFaultTable": rm10010AlmclientNetworkLaneFaultTable,
       "rm10010AlmclientNetworkLaneFaultEntry": rm10010AlmclientNetworkLaneFaultEntry,
       "rm10010AlmclientNetworkLaneFaultIndex": rm10010AlmclientNetworkLaneFaultIndex,
       "rm10010AlmClientLaneRxFifoErrorPortn": rm10010AlmClientLaneRxFifoErrorPortn,
       "rm10010AlmClientLaneRxLolPortn": rm10010AlmClientLaneRxLolPortn,
       "rm10010AlmClientLaneRxLosPortn": rm10010AlmClientLaneRxLosPortn,
       "rm10010AlmClientLaneTxLolPortn": rm10010AlmClientLaneTxLolPortn,
       "rm10010AlmClientLaneTxLosfPortn": rm10010AlmClientLaneTxLosfPortn,
       "rm10010AlmClientLaneApdPowerSupplyPortn": rm10010AlmClientLaneApdPowerSupplyPortn,
       "rm10010AlmClientLaneWavelengthUnlockedPortn": rm10010AlmClientLaneWavelengthUnlockedPortn,
       "rm10010AlmClientLaneTecFaultPortn": rm10010AlmClientLaneTecFaultPortn,
       "rm10010AlmclientHostLaneFaultTable": rm10010AlmclientHostLaneFaultTable,
       "rm10010AlmclientHostLaneFaultEntry": rm10010AlmclientHostLaneFaultEntry,
       "rm10010AlmclientHostLaneFaultIndex": rm10010AlmclientHostLaneFaultIndex,
       "rm10010AlmClientLossOfSyncPortn": rm10010AlmClientLossOfSyncPortn,
       "rm10010AlmClientInputLossOfSigPortn": rm10010AlmClientInputLossOfSigPortn,
       "rm10010AlmClientLanesMarkerUnlockPortn": rm10010AlmClientLanesMarkerUnlockPortn,
       "rm10010AlmClientLanes6466UnlockPortn": rm10010AlmClientLanes6466UnlockPortn,
       "rm10010AlmClientLanesNotAlignedPortn": rm10010AlmClientLanesNotAlignedPortn,
       "rm10010AlmClientCsfDetectedPortn": rm10010AlmClientCsfDetectedPortn,
       "rm10010AlmClientTxHostLolPortn": rm10010AlmClientTxHostLolPortn,
       "rm10010AlmClientLaneTxFifoErrorPortn": rm10010AlmClientLaneTxFifoErrorPortn,
       "rm10010AlmclientSfpAlmDdmTable": rm10010AlmclientSfpAlmDdmTable,
       "rm10010AlmclientSfpAlmDdmEntry": rm10010AlmclientSfpAlmDdmEntry,
       "rm10010AlmclientSfpAlmDdmIndex": rm10010AlmclientSfpAlmDdmIndex,
       "rm10010AlmTxPwrLowAlaPortn": rm10010AlmTxPwrLowAlaPortn,
       "rm10010AlmTxPwrHighAlaPortn": rm10010AlmTxPwrHighAlaPortn,
       "rm10010AlmTxBiasLowAlaPortn": rm10010AlmTxBiasLowAlaPortn,
       "rm10010AlmTxBiasHighAlaPortn": rm10010AlmTxBiasHighAlaPortn,
       "rm10010AlmVccLowAlaPortn": rm10010AlmVccLowAlaPortn,
       "rm10010AlmVccHighAlaPortn": rm10010AlmVccHighAlaPortn,
       "rm10010AlmTempLowAlaPortn": rm10010AlmTempLowAlaPortn,
       "rm10010AlmTempHighAlaPortn": rm10010AlmTempHighAlaPortn,
       "rm10010AlmRxPwrLowAlaPortn": rm10010AlmRxPwrLowAlaPortn,
       "rm10010AlmRxPwrHighAlaPortn": rm10010AlmRxPwrHighAlaPortn,
       "rm10010AlmClientCrit": rm10010AlmClientCrit,
       "rm10010AlmsynthAlmPortTable": rm10010AlmsynthAlmPortTable,
       "rm10010AlmsynthAlmPortEntry": rm10010AlmsynthAlmPortEntry,
       "rm10010AlmsynthAlmPortIndex": rm10010AlmsynthAlmPortIndex,
       "rm10010AlmSfpAbsentPortn": rm10010AlmSfpAbsentPortn,
       "rm10010AlmDdmAbsentPortn": rm10010AlmDdmAbsentPortn,
       "rm10010AlmHwFailAccPortn": rm10010AlmHwFailAccPortn,
       "rm10010AlmDwLsdPortn": rm10010AlmDwLsdPortn,
       "rm10010AlmClientLocalOosPortn": rm10010AlmClientLocalOosPortn,
       "rm10010AlmClientRemoteOosPortn": rm10010AlmClientRemoteOosPortn,
       "rm10010AlmDwCaisPortn": rm10010AlmDwCaisPortn,
       "rm10010AlmSfpDdmWarningPortn": rm10010AlmSfpDdmWarningPortn,
       "rm10010AlmSfpDdmAlmPortn": rm10010AlmSfpDdmAlmPortn,
       "rm10010AlmFailAccPortn": rm10010AlmFailAccPortn,
       "rm10010AlmUpCsfPortn": rm10010AlmUpCsfPortn,
       "rm10010AlmLine": rm10010AlmLine,
       "rm10010AlmLineNurg": rm10010AlmLineNurg,
       "rm10010AlmlineNetworkLaneAlarmWarning1Table": rm10010AlmlineNetworkLaneAlarmWarning1Table,
       "rm10010AlmlineNetworkLaneAlarmWarning1Entry": rm10010AlmlineNetworkLaneAlarmWarning1Entry,
       "rm10010AlmlineNetworkLaneAlarmWarning1Index": rm10010AlmlineNetworkLaneAlarmWarning1Index,
       "rm10010AlmLineRxPowerLowAlarmPortn": rm10010AlmLineRxPowerLowAlarmPortn,
       "rm10010AlmLineRxPowerLowWarningPortn": rm10010AlmLineRxPowerLowWarningPortn,
       "rm10010AlmLineRxPowerHighWarningPortn": rm10010AlmLineRxPowerHighWarningPortn,
       "rm10010AlmLineRxPowerHighAlarmPortn": rm10010AlmLineRxPowerHighAlarmPortn,
       "rm10010AlmLineLaserTempLowAlarmPortn": rm10010AlmLineLaserTempLowAlarmPortn,
       "rm10010AlmLineLaserTempLowWarningPortn": rm10010AlmLineLaserTempLowWarningPortn,
       "rm10010AlmLineLaserTempHighWarningPortn": rm10010AlmLineLaserTempHighWarningPortn,
       "rm10010AlmLineLaserTempHighAlarmPortn": rm10010AlmLineLaserTempHighAlarmPortn,
       "rm10010AlmLineTxPowerLowAlarmPortn": rm10010AlmLineTxPowerLowAlarmPortn,
       "rm10010AlmLineTxPowerLowWarningPortn": rm10010AlmLineTxPowerLowWarningPortn,
       "rm10010AlmLineTxPowerHighWarningPortn": rm10010AlmLineTxPowerHighWarningPortn,
       "rm10010AlmLineTxPowerHighAlarmPortn": rm10010AlmLineTxPowerHighAlarmPortn,
       "rm10010AlmLineBiasLowAlarmPortn": rm10010AlmLineBiasLowAlarmPortn,
       "rm10010AlmLineBiasLowWarningPortn": rm10010AlmLineBiasLowWarningPortn,
       "rm10010AlmLineBiasHighWarningPortn": rm10010AlmLineBiasHighWarningPortn,
       "rm10010AlmLineBiasHighAlarmPortn": rm10010AlmLineBiasHighAlarmPortn,
       "rm10010AlmlineNetworkLaneAlarmWarning2Table": rm10010AlmlineNetworkLaneAlarmWarning2Table,
       "rm10010AlmlineNetworkLaneAlarmWarning2Entry": rm10010AlmlineNetworkLaneAlarmWarning2Entry,
       "rm10010AlmlineNetworkLaneAlarmWarning2Index": rm10010AlmlineNetworkLaneAlarmWarning2Index,
       "rm10010AlmTxModulatorBiasLowAlarmPortn": rm10010AlmTxModulatorBiasLowAlarmPortn,
       "rm10010AlmTxModulatorBiasLowWarningPortn": rm10010AlmTxModulatorBiasLowWarningPortn,
       "rm10010AlmTxModulatorBiasHighWarningPortn": rm10010AlmTxModulatorBiasHighWarningPortn,
       "rm10010AlmTxModulatorBiasHighAlarmPortn": rm10010AlmTxModulatorBiasHighAlarmPortn,
       "rm10010AlmRxLaserTempLowAlarmPortn": rm10010AlmRxLaserTempLowAlarmPortn,
       "rm10010AlmRxLaserTempLowWarningPortn": rm10010AlmRxLaserTempLowWarningPortn,
       "rm10010AlmRxLaserTempHighWarningPortn": rm10010AlmRxLaserTempHighWarningPortn,
       "rm10010AlmRxLaserTempHighAlarmPortn": rm10010AlmRxLaserTempHighAlarmPortn,
       "rm10010AlmRxLaserOutputLowAlarmPortn": rm10010AlmRxLaserOutputLowAlarmPortn,
       "rm10010AlmRxLaserOutputLowWarningPortn": rm10010AlmRxLaserOutputLowWarningPortn,
       "rm10010AlmRxLaserOutputHighWarningPortn": rm10010AlmRxLaserOutputHighWarningPortn,
       "rm10010AlmRxLaserOutputHighAlarmPortn": rm10010AlmRxLaserOutputHighAlarmPortn,
       "rm10010AlmRxLaserBiasLowAlarmPortn": rm10010AlmRxLaserBiasLowAlarmPortn,
       "rm10010AlmRxLaserBiasLowWarningPortn": rm10010AlmRxLaserBiasLowWarningPortn,
       "rm10010AlmRxLaserBiasHighWarningPortn": rm10010AlmRxLaserBiasHighWarningPortn,
       "rm10010AlmRxLaserBiasHighAlarmPortn": rm10010AlmRxLaserBiasHighAlarmPortn,
       "rm10010AlmLineUrg": rm10010AlmLineUrg,
       "rm10010AlmlineNetworkLaneFaultTable": rm10010AlmlineNetworkLaneFaultTable,
       "rm10010AlmlineNetworkLaneFaultEntry": rm10010AlmlineNetworkLaneFaultEntry,
       "rm10010AlmlineNetworkLaneFaultIndex": rm10010AlmlineNetworkLaneFaultIndex,
       "rm10010AlmLineLaneRxTecFaultPortn": rm10010AlmLineLaneRxTecFaultPortn,
       "rm10010AlmLineLaneRxFifoErrorPortn": rm10010AlmLineLaneRxFifoErrorPortn,
       "rm10010AlmLineLaneRxLolPortn": rm10010AlmLineLaneRxLolPortn,
       "rm10010AlmLineLaneRxLosPortn": rm10010AlmLineLaneRxLosPortn,
       "rm10010AlmLineLaneTxLolPortn": rm10010AlmLineLaneTxLolPortn,
       "rm10010AlmLineLaneTxLosfPortn": rm10010AlmLineLaneTxLosfPortn,
       "rm10010AlmLineLaneApdPowerSupplyPortn": rm10010AlmLineLaneApdPowerSupplyPortn,
       "rm10010AlmLineLaneWavelengthUnlockedPortn": rm10010AlmLineLaneWavelengthUnlockedPortn,
       "rm10010AlmLineLaneTecFaultPortn": rm10010AlmLineLaneTecFaultPortn,
       "rm10010AlmlineHostLaneFaultTable": rm10010AlmlineHostLaneFaultTable,
       "rm10010AlmlineHostLaneFaultEntry": rm10010AlmlineHostLaneFaultEntry,
       "rm10010AlmlineHostLaneFaultIndex": rm10010AlmlineHostLaneFaultIndex,
       "rm10010AlmLineInputLossOfSignalPortn": rm10010AlmLineInputLossOfSignalPortn,
       "rm10010AlmLineLossOfFramePortn": rm10010AlmLineLossOfFramePortn,
       "rm10010AlmLineSmBdiInsertedPortn": rm10010AlmLineSmBdiInsertedPortn,
       "rm10010AlmLineSmBdiDetectedPortn": rm10010AlmLineSmBdiDetectedPortn,
       "rm10010AlmLineSmIaeInsertedPortn": rm10010AlmLineSmIaeInsertedPortn,
       "rm10010AlmLineSmIaeDetectedPortn": rm10010AlmLineSmIaeDetectedPortn,
       "rm10010AlmLineTxHostLolPortn": rm10010AlmLineTxHostLolPortn,
       "rm10010AlmLineLaneTxFifoErrorPortn": rm10010AlmLineLaneTxFifoErrorPortn,
       "rm10010AlmlineNetworkLaneRxOtnTable": rm10010AlmlineNetworkLaneRxOtnTable,
       "rm10010AlmlineNetworkLaneRxOtnEntry": rm10010AlmlineNetworkLaneRxOtnEntry,
       "rm10010AlmlineNetworkLaneRxOtnIndex": rm10010AlmlineNetworkLaneRxOtnIndex,
       "rm10010AlmLineRxOtnOduAisPortn": rm10010AlmLineRxOtnOduAisPortn,
       "rm10010AlmLineRxOtnOtuAisPortn": rm10010AlmLineRxOtnOtuAisPortn,
       "rm10010AlmLineRxSmBdiPortn": rm10010AlmLineRxSmBdiPortn,
       "rm10010AlmLineRxOtnIaePortn": rm10010AlmLineRxOtnIaePortn,
       "rm10010AlmLineRxOtnOomPortn": rm10010AlmLineRxOtnOomPortn,
       "rm10010AlmLineRxOtnLomPortn": rm10010AlmLineRxOtnLomPortn,
       "rm10010AlmLineRxOtnOofPortn": rm10010AlmLineRxOtnOofPortn,
       "rm10010AlmLineRxOtnLofPortn": rm10010AlmLineRxOtnLofPortn,
       "rm10010AlmlineHostLaneTxOtnTable": rm10010AlmlineHostLaneTxOtnTable,
       "rm10010AlmlineHostLaneTxOtnEntry": rm10010AlmlineHostLaneTxOtnEntry,
       "rm10010AlmlineHostLaneTxOtnIndex": rm10010AlmlineHostLaneTxOtnIndex,
       "rm10010AlmLineTxOtnOduAisPortn": rm10010AlmLineTxOtnOduAisPortn,
       "rm10010AlmLineTxOtnOtuAisPortn": rm10010AlmLineTxOtnOtuAisPortn,
       "rm10010AlmLineTxSmBdiPortn": rm10010AlmLineTxSmBdiPortn,
       "rm10010AlmLineTxOtnIaePortn": rm10010AlmLineTxOtnIaePortn,
       "rm10010AlmLineTxOtnOomPortn": rm10010AlmLineTxOtnOomPortn,
       "rm10010AlmLineTxOtnLomPortn": rm10010AlmLineTxOtnLomPortn,
       "rm10010AlmLineTxOtnOofPortn": rm10010AlmLineTxOtnOofPortn,
       "rm10010AlmLineTxOtnLofPortn": rm10010AlmLineTxOtnLofPortn,
       "rm10010AlmLineCrit": rm10010AlmLineCrit,
       "rm10010AlmsynthAlmLineTable": rm10010AlmsynthAlmLineTable,
       "rm10010AlmsynthAlmLineEntry": rm10010AlmsynthAlmLineEntry,
       "rm10010AlmsynthAlmLineIndex": rm10010AlmsynthAlmLineIndex,
       "rm10010AlmXfpAbsentPortn": rm10010AlmXfpAbsentPortn,
       "rm10010AlmXfpInitNotComplPortn": rm10010AlmXfpInitNotComplPortn,
       "rm10010AlmLineHwFailPortn": rm10010AlmLineHwFailPortn,
       "rm10010AlmXfpTxOffPortn": rm10010AlmXfpTxOffPortn,
       "rm10010AlmLineLocalOosPortn": rm10010AlmLineLocalOosPortn,
       "rm10010AlmUpRdiInsPortn": rm10010AlmUpRdiInsPortn,
       "rm10010AlmLineDdmWarningPortn": rm10010AlmLineDdmWarningPortn,
       "rm10010AlmLineDdmAlmPortn": rm10010AlmLineDdmAlmPortn,
       "rm10010AlmLineFailPortn": rm10010AlmLineFailPortn,
       "rm10010AlmLineActivePortn": rm10010AlmLineActivePortn,
       "rm10010measures": rm10010measures,
       "rm10010MesrOther": rm10010MesrOther,
       "rm10010Mesrsynth0": rm10010Mesrsynth0,
       "rm10010Mesrsynth1": rm10010Mesrsynth1,
       "rm10010MesrpmIntervalNumber": rm10010MesrpmIntervalNumber,
       "rm10010MesrlineNetTxLaserOutputPwrAverage": rm10010MesrlineNetTxLaserOutputPwrAverage,
       "rm10010MesrlineNetTxLaserTempAverage": rm10010MesrlineNetTxLaserTempAverage,
       "rm10010MesrlineNetTxBiasCurrentAverage": rm10010MesrlineNetTxBiasCurrentAverage,
       "rm10010MesrlineNetRxInputPwrAverage": rm10010MesrlineNetRxInputPwrAverage,
       "rm10010MesrlineResidualChromaticDispAverage": rm10010MesrlineResidualChromaticDispAverage,
       "rm10010MesrlineDiffGroupDelayAverage": rm10010MesrlineDiffGroupDelayAverage,
       "rm10010MesrlineQFactorAverage": rm10010MesrlineQFactorAverage,
       "rm10010MesrlineCarrierFreqOffsetAverage": rm10010MesrlineCarrierFreqOffsetAverage,
       "rm10010MesrlineOsnrAverage": rm10010MesrlineOsnrAverage,
       "rm10010MesrclientNetTxTempMin": rm10010MesrclientNetTxTempMin,
       "rm10010MesrclientNetTxBiasMin": rm10010MesrclientNetTxBiasMin,
       "rm10010MesrclientNetTxPwrMin": rm10010MesrclientNetTxPwrMin,
       "rm10010MesrclientNetRxPwrMin": rm10010MesrclientNetRxPwrMin,
       "rm10010MesrlineNetTxLaserOutputPwrMin": rm10010MesrlineNetTxLaserOutputPwrMin,
       "rm10010MesrlineNetTxLaserTempMin": rm10010MesrlineNetTxLaserTempMin,
       "rm10010MesrlineNetTxBiasCurrentMin": rm10010MesrlineNetTxBiasCurrentMin,
       "rm10010MesrlineNetRxInputPwrMin": rm10010MesrlineNetRxInputPwrMin,
       "rm10010MesrlineResidualChromaticDispMin": rm10010MesrlineResidualChromaticDispMin,
       "rm10010MesrlineDiffGroupDelayMin": rm10010MesrlineDiffGroupDelayMin,
       "rm10010MesrlineQFactorMin": rm10010MesrlineQFactorMin,
       "rm10010MesrlineCarrierFreqOffsetMin": rm10010MesrlineCarrierFreqOffsetMin,
       "rm10010MesrlineOsnrMin": rm10010MesrlineOsnrMin,
       "rm10010MesrclientNetTxTempMax": rm10010MesrclientNetTxTempMax,
       "rm10010MesrclientNetTxBiasMax": rm10010MesrclientNetTxBiasMax,
       "rm10010MesrclientNetTxPwrMax": rm10010MesrclientNetTxPwrMax,
       "rm10010MesrclientNetRxPwrMax": rm10010MesrclientNetRxPwrMax,
       "rm10010MesrlineNetTxLaserOutputPwrMax": rm10010MesrlineNetTxLaserOutputPwrMax,
       "rm10010MesrlineNetTxLaserTempMax": rm10010MesrlineNetTxLaserTempMax,
       "rm10010MesrlineNetTxBiasCurrentMax": rm10010MesrlineNetTxBiasCurrentMax,
       "rm10010MesrlineNetRxInputPwrMax": rm10010MesrlineNetRxInputPwrMax,
       "rm10010MesrlineResidualChromaticDispMax": rm10010MesrlineResidualChromaticDispMax,
       "rm10010MesrlineDiffGroupDelayMax": rm10010MesrlineDiffGroupDelayMax,
       "rm10010MesrlineQFactorMax": rm10010MesrlineQFactorMax,
       "rm10010MesrlineCarrierFreqOffsetMax": rm10010MesrlineCarrierFreqOffsetMax,
       "rm10010MesrlineOsnrMax": rm10010MesrlineOsnrMax,
       "rm10010MesrClient": rm10010MesrClient,
       "rm10010MesrclientCfpTemp": rm10010MesrclientCfpTemp,
       "rm10010MesrclientCfp3v3Voltage": rm10010MesrclientCfp3v3Voltage,
       "rm10010MesrclientSoaBiasCurrent": rm10010MesrclientSoaBiasCurrent,
       "rm10010MesrclientNetTxTempTable": rm10010MesrclientNetTxTempTable,
       "rm10010MesrclientNetTxTempEntry": rm10010MesrclientNetTxTempEntry,
       "rm10010MesrclientNetTxTempIndex": rm10010MesrclientNetTxTempIndex,
       "rm10010MesrclientNetTxTempPortn": rm10010MesrclientNetTxTempPortn,
       "rm10010MesrclientNetTxBiasTable": rm10010MesrclientNetTxBiasTable,
       "rm10010MesrclientNetTxBiasEntry": rm10010MesrclientNetTxBiasEntry,
       "rm10010MesrclientNetTxBiasIndex": rm10010MesrclientNetTxBiasIndex,
       "rm10010MesrclientNetTxBiasPortn": rm10010MesrclientNetTxBiasPortn,
       "rm10010MesrclientNetTxPwrTable": rm10010MesrclientNetTxPwrTable,
       "rm10010MesrclientNetTxPwrEntry": rm10010MesrclientNetTxPwrEntry,
       "rm10010MesrclientNetTxPwrIndex": rm10010MesrclientNetTxPwrIndex,
       "rm10010MesrclientNetTxPwrPortn": rm10010MesrclientNetTxPwrPortn,
       "rm10010MesrclientNetRxPwrTable": rm10010MesrclientNetRxPwrTable,
       "rm10010MesrclientNetRxPwrEntry": rm10010MesrclientNetRxPwrEntry,
       "rm10010MesrclientNetRxPwrIndex": rm10010MesrclientNetRxPwrIndex,
       "rm10010MesrclientNetRxPwrPortn": rm10010MesrclientNetRxPwrPortn,
       "rm10010MesrLine": rm10010MesrLine,
       "rm10010MesrlineMsaTemp": rm10010MesrlineMsaTemp,
       "rm10010MesrlineMsa3v3Voltage": rm10010MesrlineMsa3v3Voltage,
       "rm10010MesrlineSoaBiasCurrent": rm10010MesrlineSoaBiasCurrent,
       "rm10010MesrlineNetTxLaserOutputPwrTable": rm10010MesrlineNetTxLaserOutputPwrTable,
       "rm10010MesrlineNetTxLaserOutputPwrEntry": rm10010MesrlineNetTxLaserOutputPwrEntry,
       "rm10010MesrlineNetTxLaserOutputPwrIndex": rm10010MesrlineNetTxLaserOutputPwrIndex,
       "rm10010MesrlineNetTxLaserOutputPwrPortn": rm10010MesrlineNetTxLaserOutputPwrPortn,
       "rm10010MesrlineNetTxLaserTempTable": rm10010MesrlineNetTxLaserTempTable,
       "rm10010MesrlineNetTxLaserTempEntry": rm10010MesrlineNetTxLaserTempEntry,
       "rm10010MesrlineNetTxLaserTempIndex": rm10010MesrlineNetTxLaserTempIndex,
       "rm10010MesrlineNetTxLaserTempPortn": rm10010MesrlineNetTxLaserTempPortn,
       "rm10010MesrlineNetTxBiasCurrentTable": rm10010MesrlineNetTxBiasCurrentTable,
       "rm10010MesrlineNetTxBiasCurrentEntry": rm10010MesrlineNetTxBiasCurrentEntry,
       "rm10010MesrlineNetTxBiasCurrentIndex": rm10010MesrlineNetTxBiasCurrentIndex,
       "rm10010MesrlineNetTxBiasCurrentPortn": rm10010MesrlineNetTxBiasCurrentPortn,
       "rm10010MesrlineNetRxInputPwrTable": rm10010MesrlineNetRxInputPwrTable,
       "rm10010MesrlineNetRxInputPwrEntry": rm10010MesrlineNetRxInputPwrEntry,
       "rm10010MesrlineNetRxInputPwrIndex": rm10010MesrlineNetRxInputPwrIndex,
       "rm10010MesrlineNetRxInputPwrPortn": rm10010MesrlineNetRxInputPwrPortn,
       "rm10010MesrlineResidualChromaticDispTable": rm10010MesrlineResidualChromaticDispTable,
       "rm10010MesrlineResidualChromaticDispEntry": rm10010MesrlineResidualChromaticDispEntry,
       "rm10010MesrlineResidualChromaticDispIndex": rm10010MesrlineResidualChromaticDispIndex,
       "rm10010MesrlineResidualChromaticDispPortn": rm10010MesrlineResidualChromaticDispPortn,
       "rm10010MesrlineDiffGroupDelayTable": rm10010MesrlineDiffGroupDelayTable,
       "rm10010MesrlineDiffGroupDelayEntry": rm10010MesrlineDiffGroupDelayEntry,
       "rm10010MesrlineDiffGroupDelayIndex": rm10010MesrlineDiffGroupDelayIndex,
       "rm10010MesrlineDiffGroupDelayPortn": rm10010MesrlineDiffGroupDelayPortn,
       "rm10010MesrlineQFactorTable": rm10010MesrlineQFactorTable,
       "rm10010MesrlineQFactorEntry": rm10010MesrlineQFactorEntry,
       "rm10010MesrlineQFactorIndex": rm10010MesrlineQFactorIndex,
       "rm10010MesrlineQFactorPortn": rm10010MesrlineQFactorPortn,
       "rm10010MesrlineCarrierFreqOffsetTable": rm10010MesrlineCarrierFreqOffsetTable,
       "rm10010MesrlineCarrierFreqOffsetEntry": rm10010MesrlineCarrierFreqOffsetEntry,
       "rm10010MesrlineCarrierFreqOffsetIndex": rm10010MesrlineCarrierFreqOffsetIndex,
       "rm10010MesrlineCarrierFreqOffsetPortn": rm10010MesrlineCarrierFreqOffsetPortn,
       "rm10010MesrlineOsnrTable": rm10010MesrlineOsnrTable,
       "rm10010MesrlineOsnrEntry": rm10010MesrlineOsnrEntry,
       "rm10010MesrlineOsnrIndex": rm10010MesrlineOsnrIndex,
       "rm10010MesrlineOsnrPortn": rm10010MesrlineOsnrPortn,
       "rm10010counters": rm10010counters,
       "rm10010CntOther": rm10010CntOther,
       "rm10010CntClient": rm10010CntClient,
       "rm10010CntclientInputErrorCounterLaneOneTable": rm10010CntclientInputErrorCounterLaneOneTable,
       "rm10010CntclientInputErrorCounterLaneOneEntry": rm10010CntclientInputErrorCounterLaneOneEntry,
       "rm10010CntclientInputErrorCounterLaneOneIndex": rm10010CntclientInputErrorCounterLaneOneIndex,
       "rm10010CntclientInputErrorCounterLaneOneValuePortn": rm10010CntclientInputErrorCounterLaneOneValuePortn,
       "rm10010CntclientInputErrorCounterLaneOneErrorPortn": rm10010CntclientInputErrorCounterLaneOneErrorPortn,
       "rm10010CntclientInputErrorCounterLaneOneOverloadPortn": rm10010CntclientInputErrorCounterLaneOneOverloadPortn,
       "rm10010CntclientInputErrorCounterLaneTwoTable": rm10010CntclientInputErrorCounterLaneTwoTable,
       "rm10010CntclientInputErrorCounterLaneTwoEntry": rm10010CntclientInputErrorCounterLaneTwoEntry,
       "rm10010CntclientInputErrorCounterLaneTwoIndex": rm10010CntclientInputErrorCounterLaneTwoIndex,
       "rm10010CntclientInputErrorCounterLaneTwoValuePortn": rm10010CntclientInputErrorCounterLaneTwoValuePortn,
       "rm10010CntclientInputErrorCounterLaneTwoErrorPortn": rm10010CntclientInputErrorCounterLaneTwoErrorPortn,
       "rm10010CntclientInputErrorCounterLaneTwoOverloadPortn": rm10010CntclientInputErrorCounterLaneTwoOverloadPortn,
       "rm10010CntclientInputErrorCounterTable": rm10010CntclientInputErrorCounterTable,
       "rm10010CntclientInputErrorCounterEntry": rm10010CntclientInputErrorCounterEntry,
       "rm10010CntclientInputErrorCounterIndex": rm10010CntclientInputErrorCounterIndex,
       "rm10010CntclientInputErrorCounterValuePortn": rm10010CntclientInputErrorCounterValuePortn,
       "rm10010CntclientInputErrorCounterErrorPortn": rm10010CntclientInputErrorCounterErrorPortn,
       "rm10010CntclientInputErrorCounterOverloadPortn": rm10010CntclientInputErrorCounterOverloadPortn,
       "rm10010CntclientCbipCounterTable": rm10010CntclientCbipCounterTable,
       "rm10010CntclientCbipCounterEntry": rm10010CntclientCbipCounterEntry,
       "rm10010CntclientCbipCounterIndex": rm10010CntclientCbipCounterIndex,
       "rm10010CntclientCbipCounterValuePortn": rm10010CntclientCbipCounterValuePortn,
       "rm10010CntclientCbipCounterErrorPortn": rm10010CntclientCbipCounterErrorPortn,
       "rm10010CntclientCbipCounterOverloadPortn": rm10010CntclientCbipCounterOverloadPortn,
       "rm10010CntLine": rm10010CntLine,
       "rm10010CntlocalLineSmBip8ErrorCounterTable": rm10010CntlocalLineSmBip8ErrorCounterTable,
       "rm10010CntlocalLineSmBip8ErrorCounterEntry": rm10010CntlocalLineSmBip8ErrorCounterEntry,
       "rm10010CntlocalLineSmBip8ErrorCounterIndex": rm10010CntlocalLineSmBip8ErrorCounterIndex,
       "rm10010CntlocalLineSmBip8ErrorCounterValuePortn": rm10010CntlocalLineSmBip8ErrorCounterValuePortn,
       "rm10010CntlocalLineSmBip8ErrorCounterErrorPortn": rm10010CntlocalLineSmBip8ErrorCounterErrorPortn,
       "rm10010CntlocalLineSmBip8ErrorCounterOverloadPortn": rm10010CntlocalLineSmBip8ErrorCounterOverloadPortn,
       "rm10010CntlocalLineFecCorrectedErrorsCounterTable": rm10010CntlocalLineFecCorrectedErrorsCounterTable,
       "rm10010CntlocalLineFecCorrectedErrorsCounterEntry": rm10010CntlocalLineFecCorrectedErrorsCounterEntry,
       "rm10010CntlocalLineFecCorrectedErrorsCounterIndex": rm10010CntlocalLineFecCorrectedErrorsCounterIndex,
       "rm10010CntlocalLineFecCorrectedErrorsCounterValuePortn": rm10010CntlocalLineFecCorrectedErrorsCounterValuePortn,
       "rm10010CntlocalLineFecCorrectedErrorsCounterErrorPortn": rm10010CntlocalLineFecCorrectedErrorsCounterErrorPortn,
       "rm10010CntlocalLineFecCorrectedErrorsCounterOverloadPortn": rm10010CntlocalLineFecCorrectedErrorsCounterOverloadPortn,
       "rm10010CntremoteLineSmBip8ErrorCounterTable": rm10010CntremoteLineSmBip8ErrorCounterTable,
       "rm10010CntremoteLineSmBip8ErrorCounterEntry": rm10010CntremoteLineSmBip8ErrorCounterEntry,
       "rm10010CntremoteLineSmBip8ErrorCounterIndex": rm10010CntremoteLineSmBip8ErrorCounterIndex,
       "rm10010CntremoteLineSmBip8ErrorCounterValuePortn": rm10010CntremoteLineSmBip8ErrorCounterValuePortn,
       "rm10010CntremoteLineSmBip8ErrorCounterErrorPortn": rm10010CntremoteLineSmBip8ErrorCounterErrorPortn,
       "rm10010CntremoteLineSmBip8ErrorCounterOverloadPortn": rm10010CntremoteLineSmBip8ErrorCounterOverloadPortn,
       "rm10010CntlineDfrmTimCntTable": rm10010CntlineDfrmTimCntTable,
       "rm10010CntlineDfrmTimCntEntry": rm10010CntlineDfrmTimCntEntry,
       "rm10010CntlineDfrmTimCntIndex": rm10010CntlineDfrmTimCntIndex,
       "rm10010CntlineDfrmTimCntValuePortn": rm10010CntlineDfrmTimCntValuePortn,
       "rm10010CntlineDfrmTimCntErrorPortn": rm10010CntlineDfrmTimCntErrorPortn,
       "rm10010CntlineDfrmTimCntOverloadPortn": rm10010CntlineDfrmTimCntOverloadPortn,
       "rm10010CntlocalLineTrscvFecCorrectedErrorCounterTable": rm10010CntlocalLineTrscvFecCorrectedErrorCounterTable,
       "rm10010CntlocalLineTrscvFecCorrectedErrorCounterEntry": rm10010CntlocalLineTrscvFecCorrectedErrorCounterEntry,
       "rm10010CntlocalLineTrscvFecCorrectedErrorCounterIndex": rm10010CntlocalLineTrscvFecCorrectedErrorCounterIndex,
       "rm10010CntlocalLineTrscvFecCorrectedErrorCounterValuePortn": rm10010CntlocalLineTrscvFecCorrectedErrorCounterValuePortn,
       "rm10010CntlocalLineTrscvFecCorrectedErrorCounterErrorPortn": rm10010CntlocalLineTrscvFecCorrectedErrorCounterErrorPortn,
       "rm10010CntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn": rm10010CntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn,
       "rm10010CntlocalLineTrscvFecUncorrectedErrorCounterTable": rm10010CntlocalLineTrscvFecUncorrectedErrorCounterTable,
       "rm10010CntlocalLineTrscvFecUncorrectedErrorCounterEntry": rm10010CntlocalLineTrscvFecUncorrectedErrorCounterEntry,
       "rm10010CntlocalLineTrscvFecUncorrectedErrorCounterIndex": rm10010CntlocalLineTrscvFecUncorrectedErrorCounterIndex,
       "rm10010CntlocalLineTrscvFecUncorrectedErrorCounterValuePortn": rm10010CntlocalLineTrscvFecUncorrectedErrorCounterValuePortn,
       "rm10010CntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn": rm10010CntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn,
       "rm10010CntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn": rm10010CntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn,
       "rm10010controlsWrite": rm10010controlsWrite,
       "rm10010CtrlOther": rm10010CtrlOther,
       "rm10010CtrlconfMgnt1": rm10010CtrlconfMgnt1,
       "rm10010CtrlConf1Load1": rm10010CtrlConf1Load1,
       "rm10010CtrlConf2Load1": rm10010CtrlConf2Load1,
       "rm10010CtrlConf2Flash1": rm10010CtrlConf2Flash1,
       "rm10010CtrlConf2Clear1": rm10010CtrlConf2Clear1,
       "rm10010Ctrlsynth4": rm10010Ctrlsynth4,
       "rm10010CtrlCorrelatOn": rm10010CtrlCorrelatOn,
       "rm10010CtrlCorrelatOff": rm10010CtrlCorrelatOff,
       "rm10010CtrlswMgnt": rm10010CtrlswMgnt,
       "rm10010CtrlColdReset": rm10010CtrlColdReset,
       "rm10010CtrlWarmReset": rm10010CtrlWarmReset,
       "rm10010CtrlLoadSwBank1": rm10010CtrlLoadSwBank1,
       "rm10010CtrlLoadSwBank2": rm10010CtrlLoadSwBank2,
       "rm10010CtrlgwMgnt": rm10010CtrlgwMgnt,
       "rm10010CtrlCurrentGwReset": rm10010CtrlCurrentGwReset,
       "rm10010CtrlLoadGwBank1": rm10010CtrlLoadGwBank1,
       "rm10010CtrlLoadGwBank2": rm10010CtrlLoadGwBank2,
       "rm10010CtrlLoadGwBank3": rm10010CtrlLoadGwBank3,
       "rm10010CtrlLoadGwBank4": rm10010CtrlLoadGwBank4,
       "rm10010CtrlledTest": rm10010CtrlledTest,
       "rm10010CtrlGreenLed": rm10010CtrlGreenLed,
       "rm10010CtrlRedLed": rm10010CtrlRedLed,
       "rm10010CtrlLedOff": rm10010CtrlLedOff,
       "rm10010CtrlinitSwitchMarvell": rm10010CtrlinitSwitchMarvell,
       "rm10010CtrlInitSwitchMarvell": rm10010CtrlInitSwitchMarvell,
       "rm10010CtrlresetCount": rm10010CtrlresetCount,
       "rm10010CtrlResetcount": rm10010CtrlResetcount,
       "rm10010CtrlresetRmon": rm10010CtrlresetRmon,
       "rm10010CtrlResetrmon": rm10010CtrlResetrmon,
       "rm10010CtrlresetMeasurements": rm10010CtrlresetMeasurements,
       "rm10010CtrlResetmeasurements": rm10010CtrlResetmeasurements,
       "rm10010CtrlClient": rm10010CtrlClient,
       "rm10010CtrlaccessLoopTable": rm10010CtrlaccessLoopTable,
       "rm10010CtrlaccessLoopEntry": rm10010CtrlaccessLoopEntry,
       "rm10010CtrlaccessLoopIndex": rm10010CtrlaccessLoopIndex,
       "rm10010CtrlaccessLoopPortn": rm10010CtrlaccessLoopPortn,
       "rm10010CtrlclientLoopToLineTable": rm10010CtrlclientLoopToLineTable,
       "rm10010CtrlclientLoopToLineEntry": rm10010CtrlclientLoopToLineEntry,
       "rm10010CtrlclientLoopToLineIndex": rm10010CtrlclientLoopToLineIndex,
       "rm10010CtrlclientLoopToLinePortn": rm10010CtrlclientLoopToLinePortn,
       "rm10010CtrlcsfUpInsTable": rm10010CtrlcsfUpInsTable,
       "rm10010CtrlcsfUpInsEntry": rm10010CtrlcsfUpInsEntry,
       "rm10010CtrlcsfUpInsIndex": rm10010CtrlcsfUpInsIndex,
       "rm10010CtrlcsfUpInsPortn": rm10010CtrlcsfUpInsPortn,
       "rm10010CtrlcaisDwInsTable": rm10010CtrlcaisDwInsTable,
       "rm10010CtrlcaisDwInsEntry": rm10010CtrlcaisDwInsEntry,
       "rm10010CtrlcaisDwInsIndex": rm10010CtrlcaisDwInsIndex,
       "rm10010CtrlcaisDwInsPortn": rm10010CtrlcaisDwInsPortn,
       "rm10010CtrlclientResetAllCountTable": rm10010CtrlclientResetAllCountTable,
       "rm10010CtrlclientResetAllCountEntry": rm10010CtrlclientResetAllCountEntry,
       "rm10010CtrlclientResetAllCountIndex": rm10010CtrlclientResetAllCountIndex,
       "rm10010CtrlclientResetAllCountsPortn": rm10010CtrlclientResetAllCountsPortn,
       "rm10010CtrlLine": rm10010CtrlLine,
       "rm10010CtrlcommAccessLoopTable": rm10010CtrlcommAccessLoopTable,
       "rm10010CtrlcommAccessLoopEntry": rm10010CtrlcommAccessLoopEntry,
       "rm10010CtrlcommAccessLoopIndex": rm10010CtrlcommAccessLoopIndex,
       "rm10010CtrlcommAccessLoopPortn": rm10010CtrlcommAccessLoopPortn,
       "rm10010CtrllineLoopTable": rm10010CtrllineLoopTable,
       "rm10010CtrllineLoopEntry": rm10010CtrllineLoopEntry,
       "rm10010CtrllineLoopIndex": rm10010CtrllineLoopIndex,
       "rm10010CtrllineLoopPortn": rm10010CtrllineLoopPortn,
       "rm10010CtrlfecDisableTable": rm10010CtrlfecDisableTable,
       "rm10010CtrlfecDisableEntry": rm10010CtrlfecDisableEntry,
       "rm10010CtrlfecDisableIndex": rm10010CtrlfecDisableIndex,
       "rm10010CtrlfecDisablePortn": rm10010CtrlfecDisablePortn,
       "rm10010CtrlmsaLineLoopTable": rm10010CtrlmsaLineLoopTable,
       "rm10010CtrlmsaLineLoopEntry": rm10010CtrlmsaLineLoopEntry,
       "rm10010CtrlmsaLineLoopIndex": rm10010CtrlmsaLineLoopIndex,
       "rm10010CtrlmsaLineLoopPortn": rm10010CtrlmsaLineLoopPortn,
       "rm10010CtrlmsaTxResetTable": rm10010CtrlmsaTxResetTable,
       "rm10010CtrlmsaTxResetEntry": rm10010CtrlmsaTxResetEntry,
       "rm10010CtrlmsaTxResetIndex": rm10010CtrlmsaTxResetIndex,
       "rm10010CtrlmsaTxResetPortn": rm10010CtrlmsaTxResetPortn,
       "rm10010CtrlmsaRxResetTable": rm10010CtrlmsaRxResetTable,
       "rm10010CtrlmsaRxResetEntry": rm10010CtrlmsaRxResetEntry,
       "rm10010CtrlmsaRxResetIndex": rm10010CtrlmsaRxResetIndex,
       "rm10010CtrlmsaRxResetPortn": rm10010CtrlmsaRxResetPortn,
       "rm10010CtrlmsaShutdownTable": rm10010CtrlmsaShutdownTable,
       "rm10010CtrlmsaShutdownEntry": rm10010CtrlmsaShutdownEntry,
       "rm10010CtrlmsaShutdownIndex": rm10010CtrlmsaShutdownIndex,
       "rm10010CtrlmsaShutdownPortn": rm10010CtrlmsaShutdownPortn,
       "rm10010CtrllineResetAllCountTable": rm10010CtrllineResetAllCountTable,
       "rm10010CtrllineResetAllCountEntry": rm10010CtrllineResetAllCountEntry,
       "rm10010CtrllineResetAllCountIndex": rm10010CtrllineResetAllCountIndex,
       "rm10010CtrllineResetAllCountsPortn": rm10010CtrllineResetAllCountsPortn,
       "rm10010ri": rm10010ri,
       "rm10010riTable": rm10010riTable,
       "rm10010RinvSfpTable": rm10010RinvSfpTable,
       "rm10010RinvSfpEntry": rm10010RinvSfpEntry,
       "rm10010RinvSfpIndex": rm10010RinvSfpIndex,
       "rm10010Rinvsfp": rm10010Rinvsfp,
       "rm10010RinvLineTable": rm10010RinvLineTable,
       "rm10010RinvLineEntry": rm10010RinvLineEntry,
       "rm10010RinvLineIndex": rm10010RinvLineIndex,
       "rm10010RinvxfpLine": rm10010RinvxfpLine,
       "rm10010RinvReloadInventory": rm10010RinvReloadInventory,
       "rm10010RinvHwPlatform": rm10010RinvHwPlatform,
       "rm10010RinvModulePlatform": rm10010RinvModulePlatform,
       "rm10010RinvSwPlatform": rm10010RinvSwPlatform,
       "rm10010RinvGwPlatform": rm10010RinvGwPlatform,
       "rm10010download": rm10010download,
       "rm10010DwlOther": rm10010DwlOther,
       "rm10010DwlrestartProcess": rm10010DwlrestartProcess,
       "rm10010DwlWarmRestartProcessed": rm10010DwlWarmRestartProcessed,
       "rm10010DwlColdRestartProcessed": rm10010DwlColdRestartProcessed,
       "rm10010DwlswBanksUsed": rm10010DwlswBanksUsed,
       "rm10010DwlSwBank1Used": rm10010DwlSwBank1Used,
       "rm10010DwlSwBank2Used": rm10010DwlSwBank2Used,
       "rm10010DwlSwBank1Notempty": rm10010DwlSwBank1Notempty,
       "rm10010DwlSwBank2Notempty": rm10010DwlSwBank2Notempty,
       "rm10010DwlgwBanksUsed": rm10010DwlgwBanksUsed,
       "rm10010DwlGwBank1Used": rm10010DwlGwBank1Used,
       "rm10010DwlGwBank2Used": rm10010DwlGwBank2Used,
       "rm10010DwlGwBank3Used": rm10010DwlGwBank3Used,
       "rm10010DwlGwBank4Used": rm10010DwlGwBank4Used,
       "rm10010DwlGwBank1Notempty": rm10010DwlGwBank1Notempty,
       "rm10010DwlGwBank2Notempty": rm10010DwlGwBank2Notempty,
       "rm10010DwlGwBank3Notempty": rm10010DwlGwBank3Notempty,
       "rm10010DwlGwBank4Notempty": rm10010DwlGwBank4Notempty,
       "rm10010DwlClient": rm10010DwlClient,
       "rm10010DwlLine": rm10010DwlLine,
       "rm10010Config": rm10010Config,
       "rm10010CfgAccessCAisCsf": rm10010CfgAccessCAisCsf,
       "rm10010CfgClientcaiscsfTable": rm10010CfgClientcaiscsfTable,
       "rm10010CfgClientcaiscsfEntry": rm10010CfgClientcaiscsfEntry,
       "rm10010CfgClientcaiscsfIndex": rm10010CfgClientcaiscsfIndex,
       "rm10010CfgReservePortn": rm10010CfgReservePortn,
       "rm10010CfgStartup": rm10010CfgStartup,
       "rm10010CfgClientStartupTable": rm10010CfgClientStartupTable,
       "rm10010CfgClientStartupEntry": rm10010CfgClientStartupEntry,
       "rm10010CfgClientStartupIndex": rm10010CfgClientStartupIndex,
       "rm10010CfgSystConfPortPortn": rm10010CfgSystConfPortPortn,
       "rm10010CfgNetConfPortPortn": rm10010CfgNetConfPortPortn,
       "rm10010CfgOptionsPortPortn": rm10010CfgOptionsPortPortn,
       "rm10010CfgLineStartupTable": rm10010CfgLineStartupTable,
       "rm10010CfgLineStartupEntry": rm10010CfgLineStartupEntry,
       "rm10010CfgLineStartupIndex": rm10010CfgLineStartupIndex,
       "rm10010CfgSystConfLinePortn": rm10010CfgSystConfLinePortn,
       "rm10010CfgOptionsLinePortn": rm10010CfgOptionsLinePortn,
       "rm10010CfgXfpTable": rm10010CfgXfpTable,
       "rm10010CfgXfpEntry": rm10010CfgXfpEntry,
       "rm10010CfgXfpIndex": rm10010CfgXfpIndex,
       "rm10010CfgSystConfMsaLinePortn": rm10010CfgSystConfMsaLinePortn,
       "rm10010CfgLabels": rm10010CfgLabels,
       "rm10010CfgLabelclientTable": rm10010CfgLabelclientTable,
       "rm10010CfgLabelclientEntry": rm10010CfgLabelclientEntry,
       "rm10010CfgLabelclientIndex": rm10010CfgLabelclientIndex,
       "rm10010CfgLabelclientPortn": rm10010CfgLabelclientPortn,
       "rm10010CfgLabellineTable": rm10010CfgLabellineTable,
       "rm10010CfgLabellineEntry": rm10010CfgLabellineEntry,
       "rm10010CfgLabellineIndex": rm10010CfgLabellineIndex,
       "rm10010CfgLabellinePortn": rm10010CfgLabellinePortn,
       "rm10010CfgStartuptlh": rm10010CfgStartuptlh,
       "rm10010CfgOtxtlhTable": rm10010CfgOtxtlhTable,
       "rm10010CfgOtxtlhEntry": rm10010CfgOtxtlhEntry,
       "rm10010CfgOtxtlhIndex": rm10010CfgOtxtlhIndex,
       "rm10010CfgLinePwrLaserPortn": rm10010CfgLinePwrLaserPortn,
       "rm10010CfgLineFCurrentPortn": rm10010CfgLineFCurrentPortn,
       "rm10010CfgLineGridCurrentPortn": rm10010CfgLineGridCurrentPortn,
       "rm10010CfgFPortn": rm10010CfgFPortn,
       "rm10010CfgRxLineFCurrentPortn": rm10010CfgRxLineFCurrentPortn,
       "rm10010CfgOther": rm10010CfgOther,
       "rm10010tablemoduleOther": rm10010tablemoduleOther,
       "rm10010Cfgmode": rm10010Cfgmode,
       "rm10010CfgfanLowSpeedThreshold": rm10010CfgfanLowSpeedThreshold,
       "rm10010CfgfanHighSpeedThreshold": rm10010CfgfanHighSpeedThreshold,
       "rm10010CfgStartuptablefive": rm10010CfgStartuptablefive,
       "rm10010CfgOtxtlhcapabilitiesTable": rm10010CfgOtxtlhcapabilitiesTable,
       "rm10010CfgOtxtlhcapabilitiesEntry": rm10010CfgOtxtlhcapabilitiesEntry,
       "rm10010CfgOtxtlhcapabilitiesIndex": rm10010CfgOtxtlhcapabilitiesIndex,
       "rm10010CfgComponentTypePortn": rm10010CfgComponentTypePortn,
       "rm10010CfgMiscellaneousPortn": rm10010CfgMiscellaneousPortn,
       "rm10010CfgFirstChannelPortn": rm10010CfgFirstChannelPortn,
       "rm10010CfgLastChannelPortn": rm10010CfgLastChannelPortn,
       "rm10010CfgGridPortn": rm10010CfgGridPortn,
       "rm10010CfgWriteConfiguration": rm10010CfgWriteConfiguration,
       "rm10010traps": rm10010traps,
       "rm10010trapPortNumber": rm10010trapPortNumber,
       "rm10010trapLineNumber": rm10010trapLineNumber,
       "rm10010trapBoardNumber": rm10010trapBoardNumber,
       "rm10010LineTrapNotUrgentGoesOn": rm10010LineTrapNotUrgentGoesOn,
       "rm10010LineTrapNotUrgentGoesOff": rm10010LineTrapNotUrgentGoesOff,
       "rm10010LineTrapUrgentGoesOn": rm10010LineTrapUrgentGoesOn,
       "rm10010LineTrapUrgentGoesOff": rm10010LineTrapUrgentGoesOff,
       "rm10010LineTrapCritGoesOn": rm10010LineTrapCritGoesOn,
       "rm10010LineTrapCritGoesOff": rm10010LineTrapCritGoesOff,
       "rm10010ClientTrapNotUrgentGoesOn": rm10010ClientTrapNotUrgentGoesOn,
       "rm10010ClientTrapNotUrgentGoesOff": rm10010ClientTrapNotUrgentGoesOff,
       "rm10010ClientTrapUrgentGoesOn": rm10010ClientTrapUrgentGoesOn,
       "rm10010ClientTrapUrgentGoesOff": rm10010ClientTrapUrgentGoesOff,
       "rm10010ClientTrapCritGoesOn": rm10010ClientTrapCritGoesOn,
       "rm10010ClientTrapCritGoesOff": rm10010ClientTrapCritGoesOff,
       "rm10010PowerTrapUrgentGoesOn": rm10010PowerTrapUrgentGoesOn,
       "rm10010PowerTrapUrgentGoesOff": rm10010PowerTrapUrgentGoesOff,
       "rm10010Monitoring": rm10010Monitoring,
       "rm10010MonOther": rm10010MonOther,
       "rm10010MonRmon": rm10010MonRmon,
       "rm10010MonClient": rm10010MonClient,
       "rm10010MonClientRmonCounter": rm10010MonClientRmonCounter,
       "rm10010MonupRmonBytesCounterClientInputTable": rm10010MonupRmonBytesCounterClientInputTable,
       "rm10010MonupRmonBytesCounterClientInputEntry": rm10010MonupRmonBytesCounterClientInputEntry,
       "rm10010MonupRmonBytesCounterClientInputIndex": rm10010MonupRmonBytesCounterClientInputIndex,
       "rm10010MonupRmonBytesCounterClientInputValuePortn": rm10010MonupRmonBytesCounterClientInputValuePortn,
       "rm10010MonupRmonBytesCounterClientInputErrorPortn": rm10010MonupRmonBytesCounterClientInputErrorPortn,
       "rm10010MonupRmonBytesCounterClientInputOverloadPortn": rm10010MonupRmonBytesCounterClientInputOverloadPortn,
       "rm10010MonupRmonCrcErrorsCounterClientInputTable": rm10010MonupRmonCrcErrorsCounterClientInputTable,
       "rm10010MonupRmonCrcErrorsCounterClientInputEntry": rm10010MonupRmonCrcErrorsCounterClientInputEntry,
       "rm10010MonupRmonCrcErrorsCounterClientInputIndex": rm10010MonupRmonCrcErrorsCounterClientInputIndex,
       "rm10010MonupRmonCrcErrorsCounterClientInputValuePortn": rm10010MonupRmonCrcErrorsCounterClientInputValuePortn,
       "rm10010MonupRmonCrcErrorsCounterClientInputErrorPortn": rm10010MonupRmonCrcErrorsCounterClientInputErrorPortn,
       "rm10010MonupRmonCrcErrorsCounterClientInputOverloadPortn": rm10010MonupRmonCrcErrorsCounterClientInputOverloadPortn,
       "rm10010MonupRmonPacketsCounterClientInputTable": rm10010MonupRmonPacketsCounterClientInputTable,
       "rm10010MonupRmonPacketsCounterClientInputEntry": rm10010MonupRmonPacketsCounterClientInputEntry,
       "rm10010MonupRmonPacketsCounterClientInputIndex": rm10010MonupRmonPacketsCounterClientInputIndex,
       "rm10010MonupRmonPacketsCounterClientInputValuePortn": rm10010MonupRmonPacketsCounterClientInputValuePortn,
       "rm10010MonupRmonPacketsCounterClientInputErrorPortn": rm10010MonupRmonPacketsCounterClientInputErrorPortn,
       "rm10010MonupRmonPacketsCounterClientInputOverloadPortn": rm10010MonupRmonPacketsCounterClientInputOverloadPortn,
       "rm10010MonupRmonBroadcastCounterClientInputTable": rm10010MonupRmonBroadcastCounterClientInputTable,
       "rm10010MonupRmonBroadcastCounterClientInputEntry": rm10010MonupRmonBroadcastCounterClientInputEntry,
       "rm10010MonupRmonBroadcastCounterClientInputIndex": rm10010MonupRmonBroadcastCounterClientInputIndex,
       "rm10010MonupRmonBroadcastCounterClientInputValuePortn": rm10010MonupRmonBroadcastCounterClientInputValuePortn,
       "rm10010MonupRmonBroadcastCounterClientInputErrorPortn": rm10010MonupRmonBroadcastCounterClientInputErrorPortn,
       "rm10010MonupRmonBroadcastCounterClientInputOverloadPortn": rm10010MonupRmonBroadcastCounterClientInputOverloadPortn,
       "rm10010MonupRmonMulticastCounterClientInputTable": rm10010MonupRmonMulticastCounterClientInputTable,
       "rm10010MonupRmonMulticastCounterClientInputEntry": rm10010MonupRmonMulticastCounterClientInputEntry,
       "rm10010MonupRmonMulticastCounterClientInputIndex": rm10010MonupRmonMulticastCounterClientInputIndex,
       "rm10010MonupRmonMulticastCounterClientInputValuePortn": rm10010MonupRmonMulticastCounterClientInputValuePortn,
       "rm10010MonupRmonMulticastCounterClientInputErrorPortn": rm10010MonupRmonMulticastCounterClientInputErrorPortn,
       "rm10010MonupRmonMulticastCounterClientInputOverloadPortn": rm10010MonupRmonMulticastCounterClientInputOverloadPortn,
       "rm10010MonupRmonPauseFrameCounterClientInputTable": rm10010MonupRmonPauseFrameCounterClientInputTable,
       "rm10010MonupRmonPauseFrameCounterClientInputEntry": rm10010MonupRmonPauseFrameCounterClientInputEntry,
       "rm10010MonupRmonPauseFrameCounterClientInputIndex": rm10010MonupRmonPauseFrameCounterClientInputIndex,
       "rm10010MonupRmonPauseFrameCounterClientInputValuePortn": rm10010MonupRmonPauseFrameCounterClientInputValuePortn,
       "rm10010MonupRmonPauseFrameCounterClientInputErrorPortn": rm10010MonupRmonPauseFrameCounterClientInputErrorPortn,
       "rm10010MonupRmonPauseFrameCounterClientInputOverloadPortn": rm10010MonupRmonPauseFrameCounterClientInputOverloadPortn,
       "rm10010MonupRmonUnicastCounterClientInputTable": rm10010MonupRmonUnicastCounterClientInputTable,
       "rm10010MonupRmonUnicastCounterClientInputEntry": rm10010MonupRmonUnicastCounterClientInputEntry,
       "rm10010MonupRmonUnicastCounterClientInputIndex": rm10010MonupRmonUnicastCounterClientInputIndex,
       "rm10010MonupRmonUnicastCounterClientInputValuePortn": rm10010MonupRmonUnicastCounterClientInputValuePortn,
       "rm10010MonupRmonUnicastCounterClientInputErrorPortn": rm10010MonupRmonUnicastCounterClientInputErrorPortn,
       "rm10010MonupRmonUnicastCounterClientInputOverloadPortn": rm10010MonupRmonUnicastCounterClientInputOverloadPortn,
       "rm10010MonupRmonNonunicastCounterClientInputTable": rm10010MonupRmonNonunicastCounterClientInputTable,
       "rm10010MonupRmonNonunicastCounterClientInputEntry": rm10010MonupRmonNonunicastCounterClientInputEntry,
       "rm10010MonupRmonNonunicastCounterClientInputIndex": rm10010MonupRmonNonunicastCounterClientInputIndex,
       "rm10010MonupRmonNonunicastCounterClientInputValuePortn": rm10010MonupRmonNonunicastCounterClientInputValuePortn,
       "rm10010MonupRmonNonunicastCounterClientInputErrorPortn": rm10010MonupRmonNonunicastCounterClientInputErrorPortn,
       "rm10010MonupRmonNonunicastCounterClientInputOverloadPortn": rm10010MonupRmonNonunicastCounterClientInputOverloadPortn,
       "rm10010MondownRmonBytesCounterClientOutputTable": rm10010MondownRmonBytesCounterClientOutputTable,
       "rm10010MondownRmonBytesCounterClientOutputEntry": rm10010MondownRmonBytesCounterClientOutputEntry,
       "rm10010MondownRmonBytesCounterClientOutputIndex": rm10010MondownRmonBytesCounterClientOutputIndex,
       "rm10010MondownRmonBytesCounterClientOutputValuePortn": rm10010MondownRmonBytesCounterClientOutputValuePortn,
       "rm10010MondownRmonBytesCounterClientOutputErrorPortn": rm10010MondownRmonBytesCounterClientOutputErrorPortn,
       "rm10010MondownRmonBytesCounterClientOutputOverloadPortn": rm10010MondownRmonBytesCounterClientOutputOverloadPortn,
       "rm10010MondownRmonCrcErrorsCounterClientOutputTable": rm10010MondownRmonCrcErrorsCounterClientOutputTable,
       "rm10010MondownRmonCrcErrorsCounterClientOutputEntry": rm10010MondownRmonCrcErrorsCounterClientOutputEntry,
       "rm10010MondownRmonCrcErrorsCounterClientOutputIndex": rm10010MondownRmonCrcErrorsCounterClientOutputIndex,
       "rm10010MondownRmonCrcErrorsCounterClientOutputValuePortn": rm10010MondownRmonCrcErrorsCounterClientOutputValuePortn,
       "rm10010MondownRmonCrcErrorsCounterClientOutputErrorPortn": rm10010MondownRmonCrcErrorsCounterClientOutputErrorPortn,
       "rm10010MondownRmonCrcErrorsCounterClientOutputOverloadPortn": rm10010MondownRmonCrcErrorsCounterClientOutputOverloadPortn,
       "rm10010MondownRmonPacketsCounterClientOutputTable": rm10010MondownRmonPacketsCounterClientOutputTable,
       "rm10010MondownRmonPacketsCounterClientOutputEntry": rm10010MondownRmonPacketsCounterClientOutputEntry,
       "rm10010MondownRmonPacketsCounterClientOutputIndex": rm10010MondownRmonPacketsCounterClientOutputIndex,
       "rm10010MondownRmonPacketsCounterClientOutputValuePortn": rm10010MondownRmonPacketsCounterClientOutputValuePortn,
       "rm10010MondownRmonPacketsCounterClientOutputErrorPortn": rm10010MondownRmonPacketsCounterClientOutputErrorPortn,
       "rm10010MondownRmonPacketsCounterClientOutputOverloadPortn": rm10010MondownRmonPacketsCounterClientOutputOverloadPortn,
       "rm10010MondownRmonBroadcastCounterClientOutputTable": rm10010MondownRmonBroadcastCounterClientOutputTable,
       "rm10010MondownRmonBroadcastCounterClientOutputEntry": rm10010MondownRmonBroadcastCounterClientOutputEntry,
       "rm10010MondownRmonBroadcastCounterClientOutputIndex": rm10010MondownRmonBroadcastCounterClientOutputIndex,
       "rm10010MondownRmonBroadcastCounterClientOutputValuePortn": rm10010MondownRmonBroadcastCounterClientOutputValuePortn,
       "rm10010MondownRmonBroadcastCounterClientOutputErrorPortn": rm10010MondownRmonBroadcastCounterClientOutputErrorPortn,
       "rm10010MondownRmonBroadcastCounterClientOutputOverloadPortn": rm10010MondownRmonBroadcastCounterClientOutputOverloadPortn,
       "rm10010MondownRmonMulticastCounterClientOutputTable": rm10010MondownRmonMulticastCounterClientOutputTable,
       "rm10010MondownRmonMulticastCounterClientOutputEntry": rm10010MondownRmonMulticastCounterClientOutputEntry,
       "rm10010MondownRmonMulticastCounterClientOutputIndex": rm10010MondownRmonMulticastCounterClientOutputIndex,
       "rm10010MondownRmonMulticastCounterClientOutputValuePortn": rm10010MondownRmonMulticastCounterClientOutputValuePortn,
       "rm10010MondownRmonMulticastCounterClientOutputErrorPortn": rm10010MondownRmonMulticastCounterClientOutputErrorPortn,
       "rm10010MondownRmonMulticastCounterClientOutputOverloadPortn": rm10010MondownRmonMulticastCounterClientOutputOverloadPortn,
       "rm10010MondownRmonPauseFrameCounterClientOutputTable": rm10010MondownRmonPauseFrameCounterClientOutputTable,
       "rm10010MondownRmonPauseFrameCounterClientOutputEntry": rm10010MondownRmonPauseFrameCounterClientOutputEntry,
       "rm10010MondownRmonPauseFrameCounterClientOutputIndex": rm10010MondownRmonPauseFrameCounterClientOutputIndex,
       "rm10010MondownRmonPauseFrameCounterClientOutputValuePortn": rm10010MondownRmonPauseFrameCounterClientOutputValuePortn,
       "rm10010MondownRmonPauseFrameCounterClientOutputErrorPortn": rm10010MondownRmonPauseFrameCounterClientOutputErrorPortn,
       "rm10010MondownRmonPauseFrameCounterClientOutputOverloadPortn": rm10010MondownRmonPauseFrameCounterClientOutputOverloadPortn,
       "rm10010MondownRmonUnicastCounterClientOutputTable": rm10010MondownRmonUnicastCounterClientOutputTable,
       "rm10010MondownRmonUnicastCounterClientOutputEntry": rm10010MondownRmonUnicastCounterClientOutputEntry,
       "rm10010MondownRmonUnicastCounterClientOutputIndex": rm10010MondownRmonUnicastCounterClientOutputIndex,
       "rm10010MondownRmonUnicastCounterClientOutputValuePortn": rm10010MondownRmonUnicastCounterClientOutputValuePortn,
       "rm10010MondownRmonUnicastCounterClientOutputErrorPortn": rm10010MondownRmonUnicastCounterClientOutputErrorPortn,
       "rm10010MondownRmonUnicastCounterClientOutputOverloadPortn": rm10010MondownRmonUnicastCounterClientOutputOverloadPortn,
       "rm10010MondownRmonNonunicastCounterClientOutputTable": rm10010MondownRmonNonunicastCounterClientOutputTable,
       "rm10010MondownRmonNonunicastCounterClientOutputEntry": rm10010MondownRmonNonunicastCounterClientOutputEntry,
       "rm10010MondownRmonNonunicastCounterClientOutputIndex": rm10010MondownRmonNonunicastCounterClientOutputIndex,
       "rm10010MondownRmonNonunicastCounterClientOutputValuePortn": rm10010MondownRmonNonunicastCounterClientOutputValuePortn,
       "rm10010MondownRmonNonunicastCounterClientOutputErrorPortn": rm10010MondownRmonNonunicastCounterClientOutputErrorPortn,
       "rm10010MondownRmonNonunicastCounterClientOutputOverloadPortn": rm10010MondownRmonNonunicastCounterClientOutputOverloadPortn,
       "rm10010MonPerfOther": rm10010MonPerfOther,
       "rm10010MonPerfSync": rm10010MonPerfSync,
       "rm10010PerfEnable": rm10010PerfEnable,
       "rm10010Perf15minSync": rm10010Perf15minSync,
       "rm10010Perf24hSync": rm10010Perf24hSync,
       "rm10010MonPerfTimeStamp": rm10010MonPerfTimeStamp,
       "rm10010Perf15MinShort": rm10010Perf15MinShort,
       "rm10010Perf15MinLong": rm10010Perf15MinLong,
       "rm10010Perf24HoursShort": rm10010Perf24HoursShort,
       "rm10010Perf24HoursLong": rm10010Perf24HoursLong,
       "rm10010PerfCurrent15MinElapsedTime": rm10010PerfCurrent15MinElapsedTime,
       "rm10010PerfCurrent24HoursElapsedTime": rm10010PerfCurrent24HoursElapsedTime,
       "rm10010MonPerfClient": rm10010MonPerfClient,
       "rm10010PerfTelecomInputClientCurrent15StatTable": rm10010PerfTelecomInputClientCurrent15StatTable,
       "rm10010PerfTelecomInputClientCurrent15StatEntry": rm10010PerfTelecomInputClientCurrent15StatEntry,
       "rm10010PerfTelecomInputClientCurrent15StatIndex": rm10010PerfTelecomInputClientCurrent15StatIndex,
       "rm10010PerfTelecomInputClientCurrent15StatInvCvPortn": rm10010PerfTelecomInputClientCurrent15StatInvCvPortn,
       "rm10010PerfTelecomInputClientCurrent15StatCvValuePortn": rm10010PerfTelecomInputClientCurrent15StatCvValuePortn,
       "rm10010PerfTelecomInputClientCurrent15StatInvEsPortn": rm10010PerfTelecomInputClientCurrent15StatInvEsPortn,
       "rm10010PerfTelecomInputClientCurrent15StatEsValuePortn": rm10010PerfTelecomInputClientCurrent15StatEsValuePortn,
       "rm10010PerfTelecomInputClientCurrent15StatInvSesPortn": rm10010PerfTelecomInputClientCurrent15StatInvSesPortn,
       "rm10010PerfTelecomInputClientCurrent15StatSesValuePortn": rm10010PerfTelecomInputClientCurrent15StatSesValuePortn,
       "rm10010PerfTelecomInputClientCurrent15StatInvSefsPortn": rm10010PerfTelecomInputClientCurrent15StatInvSefsPortn,
       "rm10010PerfTelecomInputClientCurrent15StatSefsValuePortn": rm10010PerfTelecomInputClientCurrent15StatSefsValuePortn,
       "rm10010PerfTelecomInputClientCurrent15StatInvUasPortn": rm10010PerfTelecomInputClientCurrent15StatInvUasPortn,
       "rm10010PerfTelecomInputClientCurrent15StatUasValuePortn": rm10010PerfTelecomInputClientCurrent15StatUasValuePortn,
       "rm10010PerfTelecomInputClientPast15StatHistoryPort1Table": rm10010PerfTelecomInputClientPast15StatHistoryPort1Table,
       "rm10010PerfTelecomInputClientPast15StatHistoryPort1Entry": rm10010PerfTelecomInputClientPast15StatHistoryPort1Entry,
       "rm10010PerfTelecomInputClientPast15StatHistoryPort1Index": rm10010PerfTelecomInputClientPast15StatHistoryPort1Index,
       "rm10010PerfTelecomInputClientPast15StatHistoryInvCvPort1": rm10010PerfTelecomInputClientPast15StatHistoryInvCvPort1,
       "rm10010PerfTelecomInputClientPast15StatHistoryCvValuePort1": rm10010PerfTelecomInputClientPast15StatHistoryCvValuePort1,
       "rm10010PerfTelecomInputClientPast15StatHistoryInvEsPort1": rm10010PerfTelecomInputClientPast15StatHistoryInvEsPort1,
       "rm10010PerfTelecomInputClientPast15StatHistoryEsValuePort1": rm10010PerfTelecomInputClientPast15StatHistoryEsValuePort1,
       "rm10010PerfTelecomInputClientPast15StatHistoryInvSesPort1": rm10010PerfTelecomInputClientPast15StatHistoryInvSesPort1,
       "rm10010PerfTelecomInputClientPast15StatHistorySesValuePort1": rm10010PerfTelecomInputClientPast15StatHistorySesValuePort1,
       "rm10010PerfTelecomInputClientPast15StatHistoryInvSefsPort1": rm10010PerfTelecomInputClientPast15StatHistoryInvSefsPort1,
       "rm10010PerfTelecomInputClientPast15StatHistorySefsValuePort1": rm10010PerfTelecomInputClientPast15StatHistorySefsValuePort1,
       "rm10010PerfTelecomInputClientPast15StatHistoryInvUasPort1": rm10010PerfTelecomInputClientPast15StatHistoryInvUasPort1,
       "rm10010PerfTelecomInputClientPast15StatHistoryUasValuePort1": rm10010PerfTelecomInputClientPast15StatHistoryUasValuePort1,
       "rm10010PerfTelecomInputClientCurrent24StatTable": rm10010PerfTelecomInputClientCurrent24StatTable,
       "rm10010PerfTelecomInputClientCurrent24StatEntry": rm10010PerfTelecomInputClientCurrent24StatEntry,
       "rm10010PerfTelecomInputClientCurrent24StatIndex": rm10010PerfTelecomInputClientCurrent24StatIndex,
       "rm10010PerfTelecomInputClientCurrent24StatInvCvPortn": rm10010PerfTelecomInputClientCurrent24StatInvCvPortn,
       "rm10010PerfTelecomInputClientCurrent24StatCvValuePortn": rm10010PerfTelecomInputClientCurrent24StatCvValuePortn,
       "rm10010PerfTelecomInputClientCurrent24StatInvEsPortn": rm10010PerfTelecomInputClientCurrent24StatInvEsPortn,
       "rm10010PerfTelecomInputClientCurrent24StatEsValuePortn": rm10010PerfTelecomInputClientCurrent24StatEsValuePortn,
       "rm10010PerfTelecomInputClientCurrent24StatInvSesPortn": rm10010PerfTelecomInputClientCurrent24StatInvSesPortn,
       "rm10010PerfTelecomInputClientCurrent24StatSesValuePortn": rm10010PerfTelecomInputClientCurrent24StatSesValuePortn,
       "rm10010PerfTelecomInputClientCurrent24StatInvSefsPortn": rm10010PerfTelecomInputClientCurrent24StatInvSefsPortn,
       "rm10010PerfTelecomInputClientCurrent24StatSefsValuePortn": rm10010PerfTelecomInputClientCurrent24StatSefsValuePortn,
       "rm10010PerfTelecomInputClientCurrent24StatInvUasPortn": rm10010PerfTelecomInputClientCurrent24StatInvUasPortn,
       "rm10010PerfTelecomInputClientCurrent24StatUasValuePortn": rm10010PerfTelecomInputClientCurrent24StatUasValuePortn,
       "rm10010PerfTelecomInputClientPast24StatHistoryPort1Table": rm10010PerfTelecomInputClientPast24StatHistoryPort1Table,
       "rm10010PerfTelecomInputClientPast24StatHistoryPort1Entry": rm10010PerfTelecomInputClientPast24StatHistoryPort1Entry,
       "rm10010PerfTelecomInputClientPast24StatHistoryPort1Index": rm10010PerfTelecomInputClientPast24StatHistoryPort1Index,
       "rm10010PerfTelecomInputClientPast24StatHistoryInvCvPort1": rm10010PerfTelecomInputClientPast24StatHistoryInvCvPort1,
       "rm10010PerfTelecomInputClientPast24StatHistoryCvValuePort1": rm10010PerfTelecomInputClientPast24StatHistoryCvValuePort1,
       "rm10010PerfTelecomInputClientPast24StatHistoryInvEsPort1": rm10010PerfTelecomInputClientPast24StatHistoryInvEsPort1,
       "rm10010PerfTelecomInputClientPast24StatHistoryEsValuePort1": rm10010PerfTelecomInputClientPast24StatHistoryEsValuePort1,
       "rm10010PerfTelecomInputClientPast24StatHistoryInvSesPort1": rm10010PerfTelecomInputClientPast24StatHistoryInvSesPort1,
       "rm10010PerfTelecomInputClientPast24StatHistorySesValuePort1": rm10010PerfTelecomInputClientPast24StatHistorySesValuePort1,
       "rm10010PerfTelecomInputClientPast24StatHistoryInvSefsPort1": rm10010PerfTelecomInputClientPast24StatHistoryInvSefsPort1,
       "rm10010PerfTelecomInputClientPast24StatHistorySefsValuePort1": rm10010PerfTelecomInputClientPast24StatHistorySefsValuePort1,
       "rm10010PerfTelecomInputClientPast24StatHistoryInvUasPort1": rm10010PerfTelecomInputClientPast24StatHistoryInvUasPort1,
       "rm10010PerfTelecomInputClientPast24StatHistoryUasValuePort1": rm10010PerfTelecomInputClientPast24StatHistoryUasValuePort1,
       "rm10010PerfTelecomOutputClientCurrent15StatTable": rm10010PerfTelecomOutputClientCurrent15StatTable,
       "rm10010PerfTelecomOutputClientCurrent15StatEntry": rm10010PerfTelecomOutputClientCurrent15StatEntry,
       "rm10010PerfTelecomOutputClientCurrent15StatIndex": rm10010PerfTelecomOutputClientCurrent15StatIndex,
       "rm10010PerfTelecomOutputClientCurrent15StatInvCvPortn": rm10010PerfTelecomOutputClientCurrent15StatInvCvPortn,
       "rm10010PerfTelecomOutputClientCurrent15StatCvValuePortn": rm10010PerfTelecomOutputClientCurrent15StatCvValuePortn,
       "rm10010PerfTelecomOutputClientCurrent15StatInvEsPortn": rm10010PerfTelecomOutputClientCurrent15StatInvEsPortn,
       "rm10010PerfTelecomOutputClientCurrent15StatEsValuePortn": rm10010PerfTelecomOutputClientCurrent15StatEsValuePortn,
       "rm10010PerfTelecomOutputClientCurrent15StatInvSesPortn": rm10010PerfTelecomOutputClientCurrent15StatInvSesPortn,
       "rm10010PerfTelecomOutputClientCurrent15StatSesValuePortn": rm10010PerfTelecomOutputClientCurrent15StatSesValuePortn,
       "rm10010PerfTelecomOutputClientCurrent15StatInvSefsPortn": rm10010PerfTelecomOutputClientCurrent15StatInvSefsPortn,
       "rm10010PerfTelecomOutputClientCurrent15StatSefsValuePortn": rm10010PerfTelecomOutputClientCurrent15StatSefsValuePortn,
       "rm10010PerfTelecomOutputClientCurrent15StatInvUasPortn": rm10010PerfTelecomOutputClientCurrent15StatInvUasPortn,
       "rm10010PerfTelecomOutputClientCurrent15StatUasValuePortn": rm10010PerfTelecomOutputClientCurrent15StatUasValuePortn,
       "rm10010PerfTelecomOutputClientPast15StatHistoryPort1Table": rm10010PerfTelecomOutputClientPast15StatHistoryPort1Table,
       "rm10010PerfTelecomOutputClientPast15StatHistoryPort1Entry": rm10010PerfTelecomOutputClientPast15StatHistoryPort1Entry,
       "rm10010PerfTelecomOutputClientPast15StatHistoryPort1Index": rm10010PerfTelecomOutputClientPast15StatHistoryPort1Index,
       "rm10010PerfTelecomOutputClientPast15StatHistoryInvCvPort1": rm10010PerfTelecomOutputClientPast15StatHistoryInvCvPort1,
       "rm10010PerfTelecomOutputClientPast15StatHistoryCvValuePort1": rm10010PerfTelecomOutputClientPast15StatHistoryCvValuePort1,
       "rm10010PerfTelecomOutputClientPast15StatHistoryInvEsPort1": rm10010PerfTelecomOutputClientPast15StatHistoryInvEsPort1,
       "rm10010PerfTelecomOutputClientPast15StatHistoryEsValuePort1": rm10010PerfTelecomOutputClientPast15StatHistoryEsValuePort1,
       "rm10010PerfTelecomOutputClientPast15StatHistoryInvSesPort1": rm10010PerfTelecomOutputClientPast15StatHistoryInvSesPort1,
       "rm10010PerfTelecomOutputClientPast15StatHistorySesValuePort1": rm10010PerfTelecomOutputClientPast15StatHistorySesValuePort1,
       "rm10010PerfTelecomOutputClientPast15StatHistoryInvSefsPort1": rm10010PerfTelecomOutputClientPast15StatHistoryInvSefsPort1,
       "rm10010PerfTelecomOutputClientPast15StatHistorySefsValuePort1": rm10010PerfTelecomOutputClientPast15StatHistorySefsValuePort1,
       "rm10010PerfTelecomOutputClientPast15StatHistoryInvUasPort1": rm10010PerfTelecomOutputClientPast15StatHistoryInvUasPort1,
       "rm10010PerfTelecomOutputClientPast15StatHistoryUasValuePort1": rm10010PerfTelecomOutputClientPast15StatHistoryUasValuePort1,
       "rm10010PerfTelecomOutputClientCurrent24StatTable": rm10010PerfTelecomOutputClientCurrent24StatTable,
       "rm10010PerfTelecomOutputClientCurrent24StatEntry": rm10010PerfTelecomOutputClientCurrent24StatEntry,
       "rm10010PerfTelecomOutputClientCurrent24StatIndex": rm10010PerfTelecomOutputClientCurrent24StatIndex,
       "rm10010PerfTelecomOutputClientCurrent24StatInvCvPortn": rm10010PerfTelecomOutputClientCurrent24StatInvCvPortn,
       "rm10010PerfTelecomOutputClientCurrent24StatCvValuePortn": rm10010PerfTelecomOutputClientCurrent24StatCvValuePortn,
       "rm10010PerfTelecomOutputClientCurrent24StatInvEsPortn": rm10010PerfTelecomOutputClientCurrent24StatInvEsPortn,
       "rm10010PerfTelecomOutputClientCurrent24StatEsValuePortn": rm10010PerfTelecomOutputClientCurrent24StatEsValuePortn,
       "rm10010PerfTelecomOutputClientCurrent24StatInvSesPortn": rm10010PerfTelecomOutputClientCurrent24StatInvSesPortn,
       "rm10010PerfTelecomOutputClientCurrent24StatSesValuePortn": rm10010PerfTelecomOutputClientCurrent24StatSesValuePortn,
       "rm10010PerfTelecomOutputClientCurrent24StatInvSefsPortn": rm10010PerfTelecomOutputClientCurrent24StatInvSefsPortn,
       "rm10010PerfTelecomOutputClientCurrent24StatSefsValuePortn": rm10010PerfTelecomOutputClientCurrent24StatSefsValuePortn,
       "rm10010PerfTelecomOutputClientCurrent24StatInvUasPortn": rm10010PerfTelecomOutputClientCurrent24StatInvUasPortn,
       "rm10010PerfTelecomOutputClientCurrent24StatUasValuePortn": rm10010PerfTelecomOutputClientCurrent24StatUasValuePortn,
       "rm10010PerfTelecomOutputClientPast24StatHistoryPort1Table": rm10010PerfTelecomOutputClientPast24StatHistoryPort1Table,
       "rm10010PerfTelecomOutputClientPast24StatHistoryPort1Entry": rm10010PerfTelecomOutputClientPast24StatHistoryPort1Entry,
       "rm10010PerfTelecomOutputClientPast24StatHistoryPort1Index": rm10010PerfTelecomOutputClientPast24StatHistoryPort1Index,
       "rm10010PerfTelecomOutputClientPast24StatHistoryInvCvPort1": rm10010PerfTelecomOutputClientPast24StatHistoryInvCvPort1,
       "rm10010PerfTelecomOutputClientPast24StatHistoryCvValuePort1": rm10010PerfTelecomOutputClientPast24StatHistoryCvValuePort1,
       "rm10010PerfTelecomOutputClientPast24StatHistoryInvEsPort1": rm10010PerfTelecomOutputClientPast24StatHistoryInvEsPort1,
       "rm10010PerfTelecomOutputClientPast24StatHistoryEsValuePort1": rm10010PerfTelecomOutputClientPast24StatHistoryEsValuePort1,
       "rm10010PerfTelecomOutputClientPast24StatHistoryInvSesPort1": rm10010PerfTelecomOutputClientPast24StatHistoryInvSesPort1,
       "rm10010PerfTelecomOutputClientPast24StatHistorySesValuePort1": rm10010PerfTelecomOutputClientPast24StatHistorySesValuePort1,
       "rm10010PerfTelecomOutputClientPast24StatHistoryInvSefsPort1": rm10010PerfTelecomOutputClientPast24StatHistoryInvSefsPort1,
       "rm10010PerfTelecomOutputClientPast24StatHistorySefsValuePort1": rm10010PerfTelecomOutputClientPast24StatHistorySefsValuePort1,
       "rm10010PerfTelecomOutputClientPast24StatHistoryInvUasPort1": rm10010PerfTelecomOutputClientPast24StatHistoryInvUasPort1,
       "rm10010PerfTelecomOutputClientPast24StatHistoryUasValuePort1": rm10010PerfTelecomOutputClientPast24StatHistoryUasValuePort1,
       "rm10010PerfDatacomClientCurrent15StatTable": rm10010PerfDatacomClientCurrent15StatTable,
       "rm10010PerfDatacomClientCurrent15StatEntry": rm10010PerfDatacomClientCurrent15StatEntry,
       "rm10010PerfDatacomClientCurrent15StatIndex": rm10010PerfDatacomClientCurrent15StatIndex,
       "rm10010perfdatacomclientCurrent15StatInCrcCountInvPortn": rm10010perfdatacomclientCurrent15StatInCrcCountInvPortn,
       "rm10010perfdatacomclientCurrent15StatInCrcCountPortn": rm10010perfdatacomclientCurrent15StatInCrcCountPortn,
       "rm10010perfdatacomclientCurrent15StatInPacketCountInvPortn": rm10010perfdatacomclientCurrent15StatInPacketCountInvPortn,
       "rm10010perfdatacomclientCurrent15StatInPacketCountPortn": rm10010perfdatacomclientCurrent15StatInPacketCountPortn,
       "rm10010perfdatacomclientCurrent15StatOutCrcCountInvPortn": rm10010perfdatacomclientCurrent15StatOutCrcCountInvPortn,
       "rm10010perfdatacomclientCurrent15StatOutCrcCountPortn": rm10010perfdatacomclientCurrent15StatOutCrcCountPortn,
       "rm10010perfdatacomclientCurrent15StatOutPacketCountInvPortn": rm10010perfdatacomclientCurrent15StatOutPacketCountInvPortn,
       "rm10010perfdatacomclientCurrent15StatOutPacketCountPortn": rm10010perfdatacomclientCurrent15StatOutPacketCountPortn,
       "rm10010PerfDatacomClientPast15StatHistoryPort1Table": rm10010PerfDatacomClientPast15StatHistoryPort1Table,
       "rm10010PerfDatacomClientPast15StatHistoryPort1Entry": rm10010PerfDatacomClientPast15StatHistoryPort1Entry,
       "rm10010PerfDatacomClientPast15StatHistoryPort1Index": rm10010PerfDatacomClientPast15StatHistoryPort1Index,
       "rm10010perfdatacomclientPast15StatInCrcCountInvPort1": rm10010perfdatacomclientPast15StatInCrcCountInvPort1,
       "rm10010perfdatacomclientPast15StatInCrcCountPort1": rm10010perfdatacomclientPast15StatInCrcCountPort1,
       "rm10010perfdatacomclientPast15StatInPacketCountInvPort1": rm10010perfdatacomclientPast15StatInPacketCountInvPort1,
       "rm10010perfdatacomclientPast15StatInPacketCountPort1": rm10010perfdatacomclientPast15StatInPacketCountPort1,
       "rm10010perfdatacomclientPast15StatOutCrcCountInvPort1": rm10010perfdatacomclientPast15StatOutCrcCountInvPort1,
       "rm10010perfdatacomclientPast15StatOutCrcCountPort1": rm10010perfdatacomclientPast15StatOutCrcCountPort1,
       "rm10010perfdatacomclientPast15StatOutPacketCountInvPort1": rm10010perfdatacomclientPast15StatOutPacketCountInvPort1,
       "rm10010perfdatacomclientPast15StatOutPacketCountPort1": rm10010perfdatacomclientPast15StatOutPacketCountPort1,
       "rm10010PerfDatacomClientCurrent24StatTable": rm10010PerfDatacomClientCurrent24StatTable,
       "rm10010PerfDatacomClientCurrent24StatEntry": rm10010PerfDatacomClientCurrent24StatEntry,
       "rm10010PerfDatacomClientCurrent24StatIndex": rm10010PerfDatacomClientCurrent24StatIndex,
       "rm10010perfdatacomclientCurrent24StatInCrcCountInvPortn": rm10010perfdatacomclientCurrent24StatInCrcCountInvPortn,
       "rm10010perfdatacomclientCurrent24StatInCrcCountPortn": rm10010perfdatacomclientCurrent24StatInCrcCountPortn,
       "rm10010perfdatacomclientCurrent24StatInPacketCountInvPortn": rm10010perfdatacomclientCurrent24StatInPacketCountInvPortn,
       "rm10010perfdatacomclientCurrent24StatInPacketCountPortn": rm10010perfdatacomclientCurrent24StatInPacketCountPortn,
       "rm10010perfdatacomclientCurrent24StatOutCrcCountInvPortn": rm10010perfdatacomclientCurrent24StatOutCrcCountInvPortn,
       "rm10010perfdatacomclientCurrent24StatOutCrcCountPortn": rm10010perfdatacomclientCurrent24StatOutCrcCountPortn,
       "rm10010perfdatacomclientCurrent24StatOutPacketCountInvPortn": rm10010perfdatacomclientCurrent24StatOutPacketCountInvPortn,
       "rm10010perfdatacomclientCurrent24StatOutPacketCountPortn": rm10010perfdatacomclientCurrent24StatOutPacketCountPortn,
       "rm10010PerfDatacomClientPast24StatHistoryPort1Table": rm10010PerfDatacomClientPast24StatHistoryPort1Table,
       "rm10010PerfDatacomClientPast24StatHistoryPort1Entry": rm10010PerfDatacomClientPast24StatHistoryPort1Entry,
       "rm10010PerfDatacomClientPast24StatHistoryPort1Index": rm10010PerfDatacomClientPast24StatHistoryPort1Index,
       "rm10010perfdatacomclientPast24StatInCrcCountInvPort1": rm10010perfdatacomclientPast24StatInCrcCountInvPort1,
       "rm10010perfdatacomclientPast24StatInCrcCountPort1": rm10010perfdatacomclientPast24StatInCrcCountPort1,
       "rm10010perfdatacomclientPast24StatInPacketCountInvPort1": rm10010perfdatacomclientPast24StatInPacketCountInvPort1,
       "rm10010perfdatacomclientPast24StatInPacketCountPort1": rm10010perfdatacomclientPast24StatInPacketCountPort1,
       "rm10010perfdatacomclientPast24StatOutCrcCountInvPort1": rm10010perfdatacomclientPast24StatOutCrcCountInvPort1,
       "rm10010perfdatacomclientPast24StatOutCrcCountPort1": rm10010perfdatacomclientPast24StatOutCrcCountPort1,
       "rm10010perfdatacomclientPast24StatOutPacketCountInvPort1": rm10010perfdatacomclientPast24StatOutPacketCountInvPort1,
       "rm10010perfdatacomclientPast24StatOutPacketCountPort1": rm10010perfdatacomclientPast24StatOutPacketCountPort1,
       "rm10010MonPerfLine": rm10010MonPerfLine,
       "rm10010PerfTelecomLinePostFecCurrent15StatTable": rm10010PerfTelecomLinePostFecCurrent15StatTable,
       "rm10010PerfTelecomLinePostFecCurrent15StatEntry": rm10010PerfTelecomLinePostFecCurrent15StatEntry,
       "rm10010PerfTelecomLinePostFecCurrent15StatIndex": rm10010PerfTelecomLinePostFecCurrent15StatIndex,
       "rm10010PerfTelecomLinePostFecCurrent15StatInvCvPortn": rm10010PerfTelecomLinePostFecCurrent15StatInvCvPortn,
       "rm10010PerfTelecomLinePostFecCurrent15StatCvValuePortn": rm10010PerfTelecomLinePostFecCurrent15StatCvValuePortn,
       "rm10010PerfTelecomLinePostFecCurrent15StatInvEsPortn": rm10010PerfTelecomLinePostFecCurrent15StatInvEsPortn,
       "rm10010PerfTelecomLinePostFecCurrent15StatEsValuePortn": rm10010PerfTelecomLinePostFecCurrent15StatEsValuePortn,
       "rm10010PerfTelecomLinePostFecCurrent15StatInvSesPortn": rm10010PerfTelecomLinePostFecCurrent15StatInvSesPortn,
       "rm10010PerfTelecomLinePostFecCurrent15StatSesValuePortn": rm10010PerfTelecomLinePostFecCurrent15StatSesValuePortn,
       "rm10010PerfTelecomLinePostFecCurrent15StatInvSefsPortn": rm10010PerfTelecomLinePostFecCurrent15StatInvSefsPortn,
       "rm10010PerfTelecomLinePostFecCurrent15StatSefsValuePortn": rm10010PerfTelecomLinePostFecCurrent15StatSefsValuePortn,
       "rm10010PerfTelecomLinePostFecCurrent15StatInvUasPortn": rm10010PerfTelecomLinePostFecCurrent15StatInvUasPortn,
       "rm10010PerfTelecomLinePostFecCurrent15StatUasValuePortn": rm10010PerfTelecomLinePostFecCurrent15StatUasValuePortn,
       "rm10010PerfTelecomLinePostFecPast15StatHistoryPort1Table": rm10010PerfTelecomLinePostFecPast15StatHistoryPort1Table,
       "rm10010PerfTelecomLinePostFecPast15StatHistoryPort1Entry": rm10010PerfTelecomLinePostFecPast15StatHistoryPort1Entry,
       "rm10010PerfTelecomLinePostFecPast15StatHistoryPort1Index": rm10010PerfTelecomLinePostFecPast15StatHistoryPort1Index,
       "rm10010PerfTelecomLinePostFecPast15StatHistoryInvCvPort1": rm10010PerfTelecomLinePostFecPast15StatHistoryInvCvPort1,
       "rm10010PerfTelecomLinePostFecPast15StatHistoryCvValuePort1": rm10010PerfTelecomLinePostFecPast15StatHistoryCvValuePort1,
       "rm10010PerfTelecomLinePostFecPast15StatHistoryInvEsPort1": rm10010PerfTelecomLinePostFecPast15StatHistoryInvEsPort1,
       "rm10010PerfTelecomLinePostFecPast15StatHistoryEsValuePort1": rm10010PerfTelecomLinePostFecPast15StatHistoryEsValuePort1,
       "rm10010PerfTelecomLinePostFecPast15StatHistoryInvSesPort1": rm10010PerfTelecomLinePostFecPast15StatHistoryInvSesPort1,
       "rm10010PerfTelecomLinePostFecPast15StatHistorySesValuePort1": rm10010PerfTelecomLinePostFecPast15StatHistorySesValuePort1,
       "rm10010PerfTelecomLinePostFecPast15StatHistoryInvSefsPort1": rm10010PerfTelecomLinePostFecPast15StatHistoryInvSefsPort1,
       "rm10010PerfTelecomLinePostFecPast15StatHistorySefsValuePort1": rm10010PerfTelecomLinePostFecPast15StatHistorySefsValuePort1,
       "rm10010PerfTelecomLinePostFecPast15StatHistoryInvUasPort1": rm10010PerfTelecomLinePostFecPast15StatHistoryInvUasPort1,
       "rm10010PerfTelecomLinePostFecPast15StatHistoryUasValuePort1": rm10010PerfTelecomLinePostFecPast15StatHistoryUasValuePort1,
       "rm10010PerfTelecomLinePostFecCurrent24StatTable": rm10010PerfTelecomLinePostFecCurrent24StatTable,
       "rm10010PerfTelecomLinePostFecCurrent24StatEntry": rm10010PerfTelecomLinePostFecCurrent24StatEntry,
       "rm10010PerfTelecomLinePostFecCurrent24StatIndex": rm10010PerfTelecomLinePostFecCurrent24StatIndex,
       "rm10010PerfTelecomLinePostFecCurrent24StatInvCvPortn": rm10010PerfTelecomLinePostFecCurrent24StatInvCvPortn,
       "rm10010PerfTelecomLinePostFecCurrent24StatCvValuePortn": rm10010PerfTelecomLinePostFecCurrent24StatCvValuePortn,
       "rm10010PerfTelecomLinePostFecCurrent24StatInvEsPortn": rm10010PerfTelecomLinePostFecCurrent24StatInvEsPortn,
       "rm10010PerfTelecomLinePostFecCurrent24StatEsValuePortn": rm10010PerfTelecomLinePostFecCurrent24StatEsValuePortn,
       "rm10010PerfTelecomLinePostFecCurrent24StatInvSesPortn": rm10010PerfTelecomLinePostFecCurrent24StatInvSesPortn,
       "rm10010PerfTelecomLinePostFecCurrent24StatSesValuePortn": rm10010PerfTelecomLinePostFecCurrent24StatSesValuePortn,
       "rm10010PerfTelecomLinePostFecCurrent24StatInvSefsPortn": rm10010PerfTelecomLinePostFecCurrent24StatInvSefsPortn,
       "rm10010PerfTelecomLinePostFecCurrent24StatSefsValuePortn": rm10010PerfTelecomLinePostFecCurrent24StatSefsValuePortn,
       "rm10010PerfTelecomLinePostFecCurrent24StatInvUasPortn": rm10010PerfTelecomLinePostFecCurrent24StatInvUasPortn,
       "rm10010PerfTelecomLinePostFecCurrent24StatUasValuePortn": rm10010PerfTelecomLinePostFecCurrent24StatUasValuePortn,
       "rm10010PerfTelecomLinePostFecPast24StatHistoryPort1Table": rm10010PerfTelecomLinePostFecPast24StatHistoryPort1Table,
       "rm10010PerfTelecomLinePostFecPast24StatHistoryPort1Entry": rm10010PerfTelecomLinePostFecPast24StatHistoryPort1Entry,
       "rm10010PerfTelecomLinePostFecPast24StatHistoryPort1Index": rm10010PerfTelecomLinePostFecPast24StatHistoryPort1Index,
       "rm10010PerfTelecomLinePostFecPast24StatHistoryInvCvPort1": rm10010PerfTelecomLinePostFecPast24StatHistoryInvCvPort1,
       "rm10010PerfTelecomLinePostFecPast24StatHistoryCvValuePort1": rm10010PerfTelecomLinePostFecPast24StatHistoryCvValuePort1,
       "rm10010PerfTelecomLinePostFecPast24StatHistoryInvEsPort1": rm10010PerfTelecomLinePostFecPast24StatHistoryInvEsPort1,
       "rm10010PerfTelecomLinePostFecPast24StatHistoryEsValuePort1": rm10010PerfTelecomLinePostFecPast24StatHistoryEsValuePort1,
       "rm10010PerfTelecomLinePostFecPast24StatHistoryInvSesPort1": rm10010PerfTelecomLinePostFecPast24StatHistoryInvSesPort1,
       "rm10010PerfTelecomLinePostFecPast24StatHistorySesValuePort1": rm10010PerfTelecomLinePostFecPast24StatHistorySesValuePort1,
       "rm10010PerfTelecomLinePostFecPast24StatHistoryInvSefsPort1": rm10010PerfTelecomLinePostFecPast24StatHistoryInvSefsPort1,
       "rm10010PerfTelecomLinePostFecPast24StatHistorySefsValuePort1": rm10010PerfTelecomLinePostFecPast24StatHistorySefsValuePort1,
       "rm10010PerfTelecomLinePostFecPast24StatHistoryInvUasPort1": rm10010PerfTelecomLinePostFecPast24StatHistoryInvUasPort1,
       "rm10010PerfTelecomLinePostFecPast24StatHistoryUasValuePort1": rm10010PerfTelecomLinePostFecPast24StatHistoryUasValuePort1,
       "rm10010PerfTelecomBerLinePreFecCurrent15StatTable": rm10010PerfTelecomBerLinePreFecCurrent15StatTable,
       "rm10010PerfTelecomBerLinePreFecCurrent15StatEntry": rm10010PerfTelecomBerLinePreFecCurrent15StatEntry,
       "rm10010PerfTelecomBerLinePreFecCurrent15StatIndex": rm10010PerfTelecomBerLinePreFecCurrent15StatIndex,
       "rm10010PerfTelecomBerLinePreFecCurrent15StatInvBerPortn": rm10010PerfTelecomBerLinePreFecCurrent15StatInvBerPortn,
       "rm10010PerfTelecomBerLinePreFecCurrent15StatBerValuePortn": rm10010PerfTelecomBerLinePreFecCurrent15StatBerValuePortn,
       "rm10010PerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn": rm10010PerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn,
       "rm10010PerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn": rm10010PerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn,
       "rm10010PerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn": rm10010PerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn,
       "rm10010PerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn": rm10010PerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn,
       "rm10010PerfTelecomBerLinePreFecPast15StatHistoryPort1Table": rm10010PerfTelecomBerLinePreFecPast15StatHistoryPort1Table,
       "rm10010PerfTelecomBerLinePreFecPast15StatHistoryPort1Entry": rm10010PerfTelecomBerLinePreFecPast15StatHistoryPort1Entry,
       "rm10010PerfTelecomBerLinePreFecPast15StatHistoryPort1Index": rm10010PerfTelecomBerLinePreFecPast15StatHistoryPort1Index,
       "rm10010PerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1": rm10010PerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1,
       "rm10010PerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1": rm10010PerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1,
       "rm10010PerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1": rm10010PerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1,
       "rm10010PerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1": rm10010PerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1,
       "rm10010PerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1": rm10010PerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1,
       "rm10010PerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1": rm10010PerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1,
       "rm10010PerfTelecomBerLinePreFecCurrent24StatTable": rm10010PerfTelecomBerLinePreFecCurrent24StatTable,
       "rm10010PerfTelecomBerLinePreFecCurrent24StatEntry": rm10010PerfTelecomBerLinePreFecCurrent24StatEntry,
       "rm10010PerfTelecomBerLinePreFecCurrent24StatIndex": rm10010PerfTelecomBerLinePreFecCurrent24StatIndex,
       "rm10010PerfTelecomBerLinePreFecCurrent24StatInvBerPortn": rm10010PerfTelecomBerLinePreFecCurrent24StatInvBerPortn,
       "rm10010PerfTelecomBerLinePreFecCurrent24StatBerValuePortn": rm10010PerfTelecomBerLinePreFecCurrent24StatBerValuePortn,
       "rm10010PerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn": rm10010PerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn,
       "rm10010PerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn": rm10010PerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn,
       "rm10010PerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn": rm10010PerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn,
       "rm10010PerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn": rm10010PerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn,
       "rm10010PerfTelecomBerLinePreFecPast24StatHistoryPort1Table": rm10010PerfTelecomBerLinePreFecPast24StatHistoryPort1Table,
       "rm10010PerfTelecomBerLinePreFecPast24StatHistoryPort1Entry": rm10010PerfTelecomBerLinePreFecPast24StatHistoryPort1Entry,
       "rm10010PerfTelecomBerLinePreFecPast24StatHistoryPort1Index": rm10010PerfTelecomBerLinePreFecPast24StatHistoryPort1Index,
       "rm10010PerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1": rm10010PerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1,
       "rm10010PerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1": rm10010PerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1,
       "rm10010PerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1": rm10010PerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1,
       "rm10010PerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1": rm10010PerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1,
       "rm10010PerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1": rm10010PerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1,
       "rm10010PerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1": rm10010PerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1}
)
