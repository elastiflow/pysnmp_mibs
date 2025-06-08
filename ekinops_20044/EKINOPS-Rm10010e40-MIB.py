# SNMP MIB module (EKINOPS-Rm10010e40-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ekinops_20044/EKINOPS-Rm10010e40-MIB.mib
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

moduleRm10010e40 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57)
)
if mibBuilder.loadTexts:
    moduleRm10010e40.setRevisions(
        ("2013-03-04 00:00",
         "2013-06-11 00:00",
         "2014-01-16 00:00",
         "2014-04-01 00:00",
         "2014-10-14 00:00",
         "2015-01-22 00:00",
         "2015-10-21 00:00",
         "2016-05-20 00:00",
         "2016-06-02 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Rm10010e40MultiRate(TextualConvention, Integer32):
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



class Rm10010e40OtxMode(TextualConvention, Integer32):
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



class Rm10010e40OtxGrid(TextualConvention, Integer32):
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



class Rm10010e40AdjustValue(TextualConvention, Integer32):
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



class Rm10010e40ClientProtocol(TextualConvention, Integer32):
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



class Rm10010e40ProtocolMode(TextualConvention, Integer32):
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



class Rm10010e40OtxChannel(TextualConvention, Integer32):
    status = "current"


class Rm10010e40OrxChannel(TextualConvention, Integer32):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Rm10010e40alarms_ObjectIdentity = ObjectIdentity
rm10010e40alarms = _Rm10010e40alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2)
)
_Rm10010e40AlmOther_ObjectIdentity = ObjectIdentity
rm10010e40AlmOther = _Rm10010e40AlmOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1)
)
_Rm10010e40AlmOtherNurg_ObjectIdentity = ObjectIdentity
rm10010e40AlmOtherNurg = _Rm10010e40AlmOtherNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 1)
)
_Rm10010e40AlmsynthAlm2_ObjectIdentity = ObjectIdentity
rm10010e40AlmsynthAlm2 = _Rm10010e40AlmsynthAlm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 1, 2)
)
_Rm10010e40AlmConfTableSave_Type = EkiOnOff
_Rm10010e40AlmConfTableSave_Object = MibScalar
rm10010e40AlmConfTableSave = _Rm10010e40AlmConfTableSave_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 1, 2, 1),
    _Rm10010e40AlmConfTableSave_Type()
)
rm10010e40AlmConfTableSave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmConfTableSave.setStatus("current")
_Rm10010e40AlmInvUpload_Type = EkiOnOff
_Rm10010e40AlmInvUpload_Object = MibScalar
rm10010e40AlmInvUpload = _Rm10010e40AlmInvUpload_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 1, 2, 2),
    _Rm10010e40AlmInvUpload_Type()
)
rm10010e40AlmInvUpload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmInvUpload.setStatus("current")
_Rm10010e40AlmConfTableLoad_Type = EkiOnOff
_Rm10010e40AlmConfTableLoad_Object = MibScalar
rm10010e40AlmConfTableLoad = _Rm10010e40AlmConfTableLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 1, 2, 3),
    _Rm10010e40AlmConfTableLoad_Type()
)
rm10010e40AlmConfTableLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmConfTableLoad.setStatus("current")
_Rm10010e40AlmCorrelatOff_Type = EkiOnOff
_Rm10010e40AlmCorrelatOff_Object = MibScalar
rm10010e40AlmCorrelatOff = _Rm10010e40AlmCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 1, 2, 4),
    _Rm10010e40AlmCorrelatOff_Type()
)
rm10010e40AlmCorrelatOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmCorrelatOff.setStatus("current")
_Rm10010e40AlmMaintenanceOn_Type = EkiOnOff
_Rm10010e40AlmMaintenanceOn_Object = MibScalar
rm10010e40AlmMaintenanceOn = _Rm10010e40AlmMaintenanceOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 1, 2, 5),
    _Rm10010e40AlmMaintenanceOn_Type()
)
rm10010e40AlmMaintenanceOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmMaintenanceOn.setStatus("current")
_Rm10010e40AlmOtherUrg_ObjectIdentity = ObjectIdentity
rm10010e40AlmOtherUrg = _Rm10010e40AlmOtherUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 2)
)
_Rm10010e40AlmmodFanFail_ObjectIdentity = ObjectIdentity
rm10010e40AlmmodFanFail = _Rm10010e40AlmmodFanFail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 2, 248)
)
_Rm10010e40AlmFanModuleAbsent_Type = EkiOnOff
_Rm10010e40AlmFanModuleAbsent_Object = MibScalar
rm10010e40AlmFanModuleAbsent = _Rm10010e40AlmFanModuleAbsent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 2, 248, 1),
    _Rm10010e40AlmFanModuleAbsent_Type()
)
rm10010e40AlmFanModuleAbsent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmFanModuleAbsent.setStatus("current")
_Rm10010e40AlmFansFail_Type = EkiOnOff
_Rm10010e40AlmFansFail_Object = MibScalar
rm10010e40AlmFansFail = _Rm10010e40AlmFansFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 2, 248, 2),
    _Rm10010e40AlmFansFail_Type()
)
rm10010e40AlmFansFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmFansFail.setStatus("current")
_Rm10010e40AlmFan1Fail_Type = EkiOnOff
_Rm10010e40AlmFan1Fail_Object = MibScalar
rm10010e40AlmFan1Fail = _Rm10010e40AlmFan1Fail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 2, 248, 4),
    _Rm10010e40AlmFan1Fail_Type()
)
rm10010e40AlmFan1Fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmFan1Fail.setStatus("current")
_Rm10010e40AlmFan2Fail_Type = EkiOnOff
_Rm10010e40AlmFan2Fail_Object = MibScalar
rm10010e40AlmFan2Fail = _Rm10010e40AlmFan2Fail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 2, 248, 5),
    _Rm10010e40AlmFan2Fail_Type()
)
rm10010e40AlmFan2Fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmFan2Fail.setStatus("current")
_Rm10010e40AlmFan3Fail_Type = EkiOnOff
_Rm10010e40AlmFan3Fail_Object = MibScalar
rm10010e40AlmFan3Fail = _Rm10010e40AlmFan3Fail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 2, 248, 6),
    _Rm10010e40AlmFan3Fail_Type()
)
rm10010e40AlmFan3Fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmFan3Fail.setStatus("current")
_Rm10010e40AlmFan4Fail_Type = EkiOnOff
_Rm10010e40AlmFan4Fail_Object = MibScalar
rm10010e40AlmFan4Fail = _Rm10010e40AlmFan4Fail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 2, 248, 7),
    _Rm10010e40AlmFan4Fail_Type()
)
rm10010e40AlmFan4Fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmFan4Fail.setStatus("current")
_Rm10010e40AlmOtherCrit_ObjectIdentity = ObjectIdentity
rm10010e40AlmOtherCrit = _Rm10010e40AlmOtherCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3)
)
_Rm10010e40AlmsynthAlm0_ObjectIdentity = ObjectIdentity
rm10010e40AlmsynthAlm0 = _Rm10010e40AlmsynthAlm0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 0)
)
_Rm10010e40AlmFailFan_Type = EkiOnOff
_Rm10010e40AlmFailFan_Object = MibScalar
rm10010e40AlmFailFan = _Rm10010e40AlmFailFan_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 0, 2),
    _Rm10010e40AlmFailFan_Type()
)
rm10010e40AlmFailFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmFailFan.setStatus("current")
_Rm10010e40AlmModGlobFail_Type = EkiOnOff
_Rm10010e40AlmModGlobFail_Object = MibScalar
rm10010e40AlmModGlobFail = _Rm10010e40AlmModGlobFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 0, 9),
    _Rm10010e40AlmModGlobFail_Type()
)
rm10010e40AlmModGlobFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmModGlobFail.setStatus("current")
_Rm10010e40AlmDefFuseA_Type = EkiOnOff
_Rm10010e40AlmDefFuseA_Object = MibScalar
rm10010e40AlmDefFuseA = _Rm10010e40AlmDefFuseA_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 0, 15),
    _Rm10010e40AlmDefFuseA_Type()
)
rm10010e40AlmDefFuseA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmDefFuseA.setStatus("current")
_Rm10010e40AlmDefFuseB_Type = EkiOnOff
_Rm10010e40AlmDefFuseB_Object = MibScalar
rm10010e40AlmDefFuseB = _Rm10010e40AlmDefFuseB_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 0, 16),
    _Rm10010e40AlmDefFuseB_Type()
)
rm10010e40AlmDefFuseB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmDefFuseB.setStatus("current")
_Rm10010e40AlmclientModuleState_ObjectIdentity = ObjectIdentity
rm10010e40AlmclientModuleState = _Rm10010e40AlmclientModuleState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 40)
)
_Rm10010e40AlmCfpInitialize_Type = EkiOnOff
_Rm10010e40AlmCfpInitialize_Object = MibScalar
rm10010e40AlmCfpInitialize = _Rm10010e40AlmCfpInitialize_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 40, 1),
    _Rm10010e40AlmCfpInitialize_Type()
)
rm10010e40AlmCfpInitialize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmCfpInitialize.setStatus("current")
_Rm10010e40AlmCfpLowPower_Type = EkiOnOff
_Rm10010e40AlmCfpLowPower_Object = MibScalar
rm10010e40AlmCfpLowPower = _Rm10010e40AlmCfpLowPower_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 40, 2),
    _Rm10010e40AlmCfpLowPower_Type()
)
rm10010e40AlmCfpLowPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmCfpLowPower.setStatus("current")
_Rm10010e40AlmCfpHighPowerUp_Type = EkiOnOff
_Rm10010e40AlmCfpHighPowerUp_Object = MibScalar
rm10010e40AlmCfpHighPowerUp = _Rm10010e40AlmCfpHighPowerUp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 40, 3),
    _Rm10010e40AlmCfpHighPowerUp_Type()
)
rm10010e40AlmCfpHighPowerUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmCfpHighPowerUp.setStatus("current")
_Rm10010e40AlmCfpTxOff_Type = EkiOnOff
_Rm10010e40AlmCfpTxOff_Object = MibScalar
rm10010e40AlmCfpTxOff = _Rm10010e40AlmCfpTxOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 40, 4),
    _Rm10010e40AlmCfpTxOff_Type()
)
rm10010e40AlmCfpTxOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmCfpTxOff.setStatus("current")
_Rm10010e40AlmCfpTxTurnOn_Type = EkiOnOff
_Rm10010e40AlmCfpTxTurnOn_Object = MibScalar
rm10010e40AlmCfpTxTurnOn = _Rm10010e40AlmCfpTxTurnOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 40, 5),
    _Rm10010e40AlmCfpTxTurnOn_Type()
)
rm10010e40AlmCfpTxTurnOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmCfpTxTurnOn.setStatus("current")
_Rm10010e40AlmCfpReady_Type = EkiOnOff
_Rm10010e40AlmCfpReady_Object = MibScalar
rm10010e40AlmCfpReady = _Rm10010e40AlmCfpReady_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 40, 6),
    _Rm10010e40AlmCfpReady_Type()
)
rm10010e40AlmCfpReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmCfpReady.setStatus("current")
_Rm10010e40AlmCfpFault_Type = EkiOnOff
_Rm10010e40AlmCfpFault_Object = MibScalar
rm10010e40AlmCfpFault = _Rm10010e40AlmCfpFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 40, 7),
    _Rm10010e40AlmCfpFault_Type()
)
rm10010e40AlmCfpFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmCfpFault.setStatus("current")
_Rm10010e40AlmCfpTxTurnOff_Type = EkiOnOff
_Rm10010e40AlmCfpTxTurnOff_Object = MibScalar
rm10010e40AlmCfpTxTurnOff = _Rm10010e40AlmCfpTxTurnOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 40, 8),
    _Rm10010e40AlmCfpTxTurnOff_Type()
)
rm10010e40AlmCfpTxTurnOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmCfpTxTurnOff.setStatus("current")
_Rm10010e40AlmCfpHighPowerDown_Type = EkiOnOff
_Rm10010e40AlmCfpHighPowerDown_Object = MibScalar
rm10010e40AlmCfpHighPowerDown = _Rm10010e40AlmCfpHighPowerDown_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 40, 9),
    _Rm10010e40AlmCfpHighPowerDown_Type()
)
rm10010e40AlmCfpHighPowerDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmCfpHighPowerDown.setStatus("current")
_Rm10010e40AlmclientModuleGeneralStatus_ObjectIdentity = ObjectIdentity
rm10010e40AlmclientModuleGeneralStatus = _Rm10010e40AlmclientModuleGeneralStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 41)
)
_Rm10010e40AlmCfpOutOfAlignment_Type = EkiOnOff
_Rm10010e40AlmCfpOutOfAlignment_Object = MibScalar
rm10010e40AlmCfpOutOfAlignment = _Rm10010e40AlmCfpOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 41, 4),
    _Rm10010e40AlmCfpOutOfAlignment_Type()
)
rm10010e40AlmCfpOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmCfpOutOfAlignment.setStatus("current")
_Rm10010e40AlmCfpRxNetworkLol_Type = EkiOnOff
_Rm10010e40AlmCfpRxNetworkLol_Object = MibScalar
rm10010e40AlmCfpRxNetworkLol = _Rm10010e40AlmCfpRxNetworkLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 41, 5),
    _Rm10010e40AlmCfpRxNetworkLol_Type()
)
rm10010e40AlmCfpRxNetworkLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmCfpRxNetworkLol.setStatus("current")
_Rm10010e40AlmCfpRxLos_Type = EkiOnOff
_Rm10010e40AlmCfpRxLos_Object = MibScalar
rm10010e40AlmCfpRxLos = _Rm10010e40AlmCfpRxLos_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 41, 6),
    _Rm10010e40AlmCfpRxLos_Type()
)
rm10010e40AlmCfpRxLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmCfpRxLos.setStatus("current")
_Rm10010e40AlmCfpTxHostLol_Type = EkiOnOff
_Rm10010e40AlmCfpTxHostLol_Object = MibScalar
rm10010e40AlmCfpTxHostLol = _Rm10010e40AlmCfpTxHostLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 41, 7),
    _Rm10010e40AlmCfpTxHostLol_Type()
)
rm10010e40AlmCfpTxHostLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmCfpTxHostLol.setStatus("current")
_Rm10010e40AlmCfpTxLosf_Type = EkiOnOff
_Rm10010e40AlmCfpTxLosf_Object = MibScalar
rm10010e40AlmCfpTxLosf = _Rm10010e40AlmCfpTxLosf_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 41, 8),
    _Rm10010e40AlmCfpTxLosf_Type()
)
rm10010e40AlmCfpTxLosf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmCfpTxLosf.setStatus("current")
_Rm10010e40AlmCfpTxCmuLol_Type = EkiOnOff
_Rm10010e40AlmCfpTxCmuLol_Object = MibScalar
rm10010e40AlmCfpTxCmuLol = _Rm10010e40AlmCfpTxCmuLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 41, 9),
    _Rm10010e40AlmCfpTxCmuLol_Type()
)
rm10010e40AlmCfpTxCmuLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmCfpTxCmuLol.setStatus("current")
_Rm10010e40AlmCfpTxJitterPllLol_Type = EkiOnOff
_Rm10010e40AlmCfpTxJitterPllLol_Object = MibScalar
rm10010e40AlmCfpTxJitterPllLol = _Rm10010e40AlmCfpTxJitterPllLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 41, 10),
    _Rm10010e40AlmCfpTxJitterPllLol_Type()
)
rm10010e40AlmCfpTxJitterPllLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmCfpTxJitterPllLol.setStatus("current")
_Rm10010e40AlmCfpLossOfRefclk_Type = EkiOnOff
_Rm10010e40AlmCfpLossOfRefclk_Object = MibScalar
rm10010e40AlmCfpLossOfRefclk = _Rm10010e40AlmCfpLossOfRefclk_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 41, 11),
    _Rm10010e40AlmCfpLossOfRefclk_Type()
)
rm10010e40AlmCfpLossOfRefclk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmCfpLossOfRefclk.setStatus("current")
_Rm10010e40AlmCfpHwInterlock_Type = EkiOnOff
_Rm10010e40AlmCfpHwInterlock_Object = MibScalar
rm10010e40AlmCfpHwInterlock = _Rm10010e40AlmCfpHwInterlock_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 41, 14),
    _Rm10010e40AlmCfpHwInterlock_Type()
)
rm10010e40AlmCfpHwInterlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmCfpHwInterlock.setStatus("current")
_Rm10010e40AlmclientGlobalAlarmSummary_ObjectIdentity = ObjectIdentity
rm10010e40AlmclientGlobalAlarmSummary = _Rm10010e40AlmclientGlobalAlarmSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 42)
)
_Rm10010e40AlmCfpSoftGlobAlarmTest_Type = EkiOnOff
_Rm10010e40AlmCfpSoftGlobAlarmTest_Object = MibScalar
rm10010e40AlmCfpSoftGlobAlarmTest = _Rm10010e40AlmCfpSoftGlobAlarmTest_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 42, 1),
    _Rm10010e40AlmCfpSoftGlobAlarmTest_Type()
)
rm10010e40AlmCfpSoftGlobAlarmTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmCfpSoftGlobAlarmTest.setStatus("current")
_Rm10010e40AlmCfpNetworkLaneAlarmWarning2_Type = EkiOnOff
_Rm10010e40AlmCfpNetworkLaneAlarmWarning2_Object = MibScalar
rm10010e40AlmCfpNetworkLaneAlarmWarning2 = _Rm10010e40AlmCfpNetworkLaneAlarmWarning2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 42, 7),
    _Rm10010e40AlmCfpNetworkLaneAlarmWarning2_Type()
)
rm10010e40AlmCfpNetworkLaneAlarmWarning2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmCfpNetworkLaneAlarmWarning2.setStatus("current")
_Rm10010e40AlmCfpModuleState_Type = EkiOnOff
_Rm10010e40AlmCfpModuleState_Object = MibScalar
rm10010e40AlmCfpModuleState = _Rm10010e40AlmCfpModuleState_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 42, 8),
    _Rm10010e40AlmCfpModuleState_Type()
)
rm10010e40AlmCfpModuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmCfpModuleState.setStatus("current")
_Rm10010e40AlmCfpModuleGeneralStatus_Type = EkiOnOff
_Rm10010e40AlmCfpModuleGeneralStatus_Object = MibScalar
rm10010e40AlmCfpModuleGeneralStatus = _Rm10010e40AlmCfpModuleGeneralStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 42, 9),
    _Rm10010e40AlmCfpModuleGeneralStatus_Type()
)
rm10010e40AlmCfpModuleGeneralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmCfpModuleGeneralStatus.setStatus("current")
_Rm10010e40AlmCfpModuleFault_Type = EkiOnOff
_Rm10010e40AlmCfpModuleFault_Object = MibScalar
rm10010e40AlmCfpModuleFault = _Rm10010e40AlmCfpModuleFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 42, 10),
    _Rm10010e40AlmCfpModuleFault_Type()
)
rm10010e40AlmCfpModuleFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmCfpModuleFault.setStatus("current")
_Rm10010e40AlmCfpModuleAlarmWarning1_Type = EkiOnOff
_Rm10010e40AlmCfpModuleAlarmWarning1_Object = MibScalar
rm10010e40AlmCfpModuleAlarmWarning1 = _Rm10010e40AlmCfpModuleAlarmWarning1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 42, 11),
    _Rm10010e40AlmCfpModuleAlarmWarning1_Type()
)
rm10010e40AlmCfpModuleAlarmWarning1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmCfpModuleAlarmWarning1.setStatus("current")
_Rm10010e40AlmCfpModuleAlarmWarning2_Type = EkiOnOff
_Rm10010e40AlmCfpModuleAlarmWarning2_Object = MibScalar
rm10010e40AlmCfpModuleAlarmWarning2 = _Rm10010e40AlmCfpModuleAlarmWarning2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 42, 12),
    _Rm10010e40AlmCfpModuleAlarmWarning2_Type()
)
rm10010e40AlmCfpModuleAlarmWarning2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmCfpModuleAlarmWarning2.setStatus("current")
_Rm10010e40AlmCfpNetworkLaneAlarmWarning1_Type = EkiOnOff
_Rm10010e40AlmCfpNetworkLaneAlarmWarning1_Object = MibScalar
rm10010e40AlmCfpNetworkLaneAlarmWarning1 = _Rm10010e40AlmCfpNetworkLaneAlarmWarning1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 42, 13),
    _Rm10010e40AlmCfpNetworkLaneAlarmWarning1_Type()
)
rm10010e40AlmCfpNetworkLaneAlarmWarning1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmCfpNetworkLaneAlarmWarning1.setStatus("current")
_Rm10010e40AlmCfpNetworkLaneFaultStatus_Type = EkiOnOff
_Rm10010e40AlmCfpNetworkLaneFaultStatus_Object = MibScalar
rm10010e40AlmCfpNetworkLaneFaultStatus = _Rm10010e40AlmCfpNetworkLaneFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 42, 14),
    _Rm10010e40AlmCfpNetworkLaneFaultStatus_Type()
)
rm10010e40AlmCfpNetworkLaneFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmCfpNetworkLaneFaultStatus.setStatus("current")
_Rm10010e40AlmCfpHostLaneFaultStatus_Type = EkiOnOff
_Rm10010e40AlmCfpHostLaneFaultStatus_Object = MibScalar
rm10010e40AlmCfpHostLaneFaultStatus = _Rm10010e40AlmCfpHostLaneFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 42, 15),
    _Rm10010e40AlmCfpHostLaneFaultStatus_Type()
)
rm10010e40AlmCfpHostLaneFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmCfpHostLaneFaultStatus.setStatus("current")
_Rm10010e40AlmCfpGlobAlarmAssertion_Type = EkiOnOff
_Rm10010e40AlmCfpGlobAlarmAssertion_Object = MibScalar
rm10010e40AlmCfpGlobAlarmAssertion = _Rm10010e40AlmCfpGlobAlarmAssertion_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 42, 16),
    _Rm10010e40AlmCfpGlobAlarmAssertion_Type()
)
rm10010e40AlmCfpGlobAlarmAssertion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmCfpGlobAlarmAssertion.setStatus("current")
_Rm10010e40AlmmsaModuleState_ObjectIdentity = ObjectIdentity
rm10010e40AlmmsaModuleState = _Rm10010e40AlmmsaModuleState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 46)
)
_Rm10010e40AlmMsaInitialize_Type = EkiOnOff
_Rm10010e40AlmMsaInitialize_Object = MibScalar
rm10010e40AlmMsaInitialize = _Rm10010e40AlmMsaInitialize_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 46, 1),
    _Rm10010e40AlmMsaInitialize_Type()
)
rm10010e40AlmMsaInitialize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmMsaInitialize.setStatus("current")
_Rm10010e40AlmMsaLowPower_Type = EkiOnOff
_Rm10010e40AlmMsaLowPower_Object = MibScalar
rm10010e40AlmMsaLowPower = _Rm10010e40AlmMsaLowPower_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 46, 2),
    _Rm10010e40AlmMsaLowPower_Type()
)
rm10010e40AlmMsaLowPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmMsaLowPower.setStatus("current")
_Rm10010e40AlmMsaHighPowerUp_Type = EkiOnOff
_Rm10010e40AlmMsaHighPowerUp_Object = MibScalar
rm10010e40AlmMsaHighPowerUp = _Rm10010e40AlmMsaHighPowerUp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 46, 3),
    _Rm10010e40AlmMsaHighPowerUp_Type()
)
rm10010e40AlmMsaHighPowerUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmMsaHighPowerUp.setStatus("current")
_Rm10010e40AlmMsaTxOff_Type = EkiOnOff
_Rm10010e40AlmMsaTxOff_Object = MibScalar
rm10010e40AlmMsaTxOff = _Rm10010e40AlmMsaTxOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 46, 4),
    _Rm10010e40AlmMsaTxOff_Type()
)
rm10010e40AlmMsaTxOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmMsaTxOff.setStatus("current")
_Rm10010e40AlmMsaTxTurnOn_Type = EkiOnOff
_Rm10010e40AlmMsaTxTurnOn_Object = MibScalar
rm10010e40AlmMsaTxTurnOn = _Rm10010e40AlmMsaTxTurnOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 46, 5),
    _Rm10010e40AlmMsaTxTurnOn_Type()
)
rm10010e40AlmMsaTxTurnOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmMsaTxTurnOn.setStatus("current")
_Rm10010e40AlmMsaReady_Type = EkiOnOff
_Rm10010e40AlmMsaReady_Object = MibScalar
rm10010e40AlmMsaReady = _Rm10010e40AlmMsaReady_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 46, 6),
    _Rm10010e40AlmMsaReady_Type()
)
rm10010e40AlmMsaReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmMsaReady.setStatus("current")
_Rm10010e40AlmMsaFault_Type = EkiOnOff
_Rm10010e40AlmMsaFault_Object = MibScalar
rm10010e40AlmMsaFault = _Rm10010e40AlmMsaFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 46, 7),
    _Rm10010e40AlmMsaFault_Type()
)
rm10010e40AlmMsaFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmMsaFault.setStatus("current")
_Rm10010e40AlmMsaTxTurnOff_Type = EkiOnOff
_Rm10010e40AlmMsaTxTurnOff_Object = MibScalar
rm10010e40AlmMsaTxTurnOff = _Rm10010e40AlmMsaTxTurnOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 46, 8),
    _Rm10010e40AlmMsaTxTurnOff_Type()
)
rm10010e40AlmMsaTxTurnOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmMsaTxTurnOff.setStatus("current")
_Rm10010e40AlmMsaHighPowerDown_Type = EkiOnOff
_Rm10010e40AlmMsaHighPowerDown_Object = MibScalar
rm10010e40AlmMsaHighPowerDown = _Rm10010e40AlmMsaHighPowerDown_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 46, 9),
    _Rm10010e40AlmMsaHighPowerDown_Type()
)
rm10010e40AlmMsaHighPowerDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmMsaHighPowerDown.setStatus("current")
_Rm10010e40AlmmsaModuleGeneralStatus_ObjectIdentity = ObjectIdentity
rm10010e40AlmmsaModuleGeneralStatus = _Rm10010e40AlmmsaModuleGeneralStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 47)
)
_Rm10010e40AlmMsaOutOfAlignment_Type = EkiOnOff
_Rm10010e40AlmMsaOutOfAlignment_Object = MibScalar
rm10010e40AlmMsaOutOfAlignment = _Rm10010e40AlmMsaOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 47, 4),
    _Rm10010e40AlmMsaOutOfAlignment_Type()
)
rm10010e40AlmMsaOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmMsaOutOfAlignment.setStatus("current")
_Rm10010e40AlmMsaRxNetworkLol_Type = EkiOnOff
_Rm10010e40AlmMsaRxNetworkLol_Object = MibScalar
rm10010e40AlmMsaRxNetworkLol = _Rm10010e40AlmMsaRxNetworkLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 47, 5),
    _Rm10010e40AlmMsaRxNetworkLol_Type()
)
rm10010e40AlmMsaRxNetworkLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmMsaRxNetworkLol.setStatus("current")
_Rm10010e40AlmMsaRxLos_Type = EkiOnOff
_Rm10010e40AlmMsaRxLos_Object = MibScalar
rm10010e40AlmMsaRxLos = _Rm10010e40AlmMsaRxLos_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 47, 6),
    _Rm10010e40AlmMsaRxLos_Type()
)
rm10010e40AlmMsaRxLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmMsaRxLos.setStatus("current")
_Rm10010e40AlmMsaTxHostLol_Type = EkiOnOff
_Rm10010e40AlmMsaTxHostLol_Object = MibScalar
rm10010e40AlmMsaTxHostLol = _Rm10010e40AlmMsaTxHostLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 47, 7),
    _Rm10010e40AlmMsaTxHostLol_Type()
)
rm10010e40AlmMsaTxHostLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmMsaTxHostLol.setStatus("current")
_Rm10010e40AlmMsaTxLosf_Type = EkiOnOff
_Rm10010e40AlmMsaTxLosf_Object = MibScalar
rm10010e40AlmMsaTxLosf = _Rm10010e40AlmMsaTxLosf_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 47, 8),
    _Rm10010e40AlmMsaTxLosf_Type()
)
rm10010e40AlmMsaTxLosf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmMsaTxLosf.setStatus("current")
_Rm10010e40AlmMsaTxCmuLol_Type = EkiOnOff
_Rm10010e40AlmMsaTxCmuLol_Object = MibScalar
rm10010e40AlmMsaTxCmuLol = _Rm10010e40AlmMsaTxCmuLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 47, 9),
    _Rm10010e40AlmMsaTxCmuLol_Type()
)
rm10010e40AlmMsaTxCmuLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmMsaTxCmuLol.setStatus("current")
_Rm10010e40AlmMsaTxJitterPllLol_Type = EkiOnOff
_Rm10010e40AlmMsaTxJitterPllLol_Object = MibScalar
rm10010e40AlmMsaTxJitterPllLol = _Rm10010e40AlmMsaTxJitterPllLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 47, 10),
    _Rm10010e40AlmMsaTxJitterPllLol_Type()
)
rm10010e40AlmMsaTxJitterPllLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmMsaTxJitterPllLol.setStatus("current")
_Rm10010e40AlmMsaLossOfRefclk_Type = EkiOnOff
_Rm10010e40AlmMsaLossOfRefclk_Object = MibScalar
rm10010e40AlmMsaLossOfRefclk = _Rm10010e40AlmMsaLossOfRefclk_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 47, 11),
    _Rm10010e40AlmMsaLossOfRefclk_Type()
)
rm10010e40AlmMsaLossOfRefclk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmMsaLossOfRefclk.setStatus("current")
_Rm10010e40AlmMsaHwInterlock_Type = EkiOnOff
_Rm10010e40AlmMsaHwInterlock_Object = MibScalar
rm10010e40AlmMsaHwInterlock = _Rm10010e40AlmMsaHwInterlock_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 47, 14),
    _Rm10010e40AlmMsaHwInterlock_Type()
)
rm10010e40AlmMsaHwInterlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmMsaHwInterlock.setStatus("current")
_Rm10010e40AlmmsaGlobalAlarmSummary_ObjectIdentity = ObjectIdentity
rm10010e40AlmmsaGlobalAlarmSummary = _Rm10010e40AlmmsaGlobalAlarmSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 48)
)
_Rm10010e40AlmMsaSoftGlobAlarmTest_Type = EkiOnOff
_Rm10010e40AlmMsaSoftGlobAlarmTest_Object = MibScalar
rm10010e40AlmMsaSoftGlobAlarmTest = _Rm10010e40AlmMsaSoftGlobAlarmTest_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 48, 1),
    _Rm10010e40AlmMsaSoftGlobAlarmTest_Type()
)
rm10010e40AlmMsaSoftGlobAlarmTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmMsaSoftGlobAlarmTest.setStatus("current")
_Rm10010e40AlmMsaNetworkHostAlarmStatus_Type = EkiOnOff
_Rm10010e40AlmMsaNetworkHostAlarmStatus_Object = MibScalar
rm10010e40AlmMsaNetworkHostAlarmStatus = _Rm10010e40AlmMsaNetworkHostAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 48, 6),
    _Rm10010e40AlmMsaNetworkHostAlarmStatus_Type()
)
rm10010e40AlmMsaNetworkHostAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmMsaNetworkHostAlarmStatus.setStatus("current")
_Rm10010e40AlmMsaNetworkLaneAlarmWarning2_Type = EkiOnOff
_Rm10010e40AlmMsaNetworkLaneAlarmWarning2_Object = MibScalar
rm10010e40AlmMsaNetworkLaneAlarmWarning2 = _Rm10010e40AlmMsaNetworkLaneAlarmWarning2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 48, 7),
    _Rm10010e40AlmMsaNetworkLaneAlarmWarning2_Type()
)
rm10010e40AlmMsaNetworkLaneAlarmWarning2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmMsaNetworkLaneAlarmWarning2.setStatus("current")
_Rm10010e40AlmMsaModuleState_Type = EkiOnOff
_Rm10010e40AlmMsaModuleState_Object = MibScalar
rm10010e40AlmMsaModuleState = _Rm10010e40AlmMsaModuleState_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 48, 8),
    _Rm10010e40AlmMsaModuleState_Type()
)
rm10010e40AlmMsaModuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmMsaModuleState.setStatus("current")
_Rm10010e40AlmMsaModuleGeneralStatus_Type = EkiOnOff
_Rm10010e40AlmMsaModuleGeneralStatus_Object = MibScalar
rm10010e40AlmMsaModuleGeneralStatus = _Rm10010e40AlmMsaModuleGeneralStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 48, 9),
    _Rm10010e40AlmMsaModuleGeneralStatus_Type()
)
rm10010e40AlmMsaModuleGeneralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmMsaModuleGeneralStatus.setStatus("current")
_Rm10010e40AlmModuleFault_Type = EkiOnOff
_Rm10010e40AlmModuleFault_Object = MibScalar
rm10010e40AlmModuleFault = _Rm10010e40AlmModuleFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 48, 10),
    _Rm10010e40AlmModuleFault_Type()
)
rm10010e40AlmModuleFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmModuleFault.setStatus("current")
_Rm10010e40AlmMsaModuleAlarmWarning1_Type = EkiOnOff
_Rm10010e40AlmMsaModuleAlarmWarning1_Object = MibScalar
rm10010e40AlmMsaModuleAlarmWarning1 = _Rm10010e40AlmMsaModuleAlarmWarning1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 48, 11),
    _Rm10010e40AlmMsaModuleAlarmWarning1_Type()
)
rm10010e40AlmMsaModuleAlarmWarning1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmMsaModuleAlarmWarning1.setStatus("current")
_Rm10010e40AlmMsaModuleAlarmWarning2_Type = EkiOnOff
_Rm10010e40AlmMsaModuleAlarmWarning2_Object = MibScalar
rm10010e40AlmMsaModuleAlarmWarning2 = _Rm10010e40AlmMsaModuleAlarmWarning2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 48, 12),
    _Rm10010e40AlmMsaModuleAlarmWarning2_Type()
)
rm10010e40AlmMsaModuleAlarmWarning2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmMsaModuleAlarmWarning2.setStatus("current")
_Rm10010e40AlmMsaNetworkLaneAlarmWarning1_Type = EkiOnOff
_Rm10010e40AlmMsaNetworkLaneAlarmWarning1_Object = MibScalar
rm10010e40AlmMsaNetworkLaneAlarmWarning1 = _Rm10010e40AlmMsaNetworkLaneAlarmWarning1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 48, 13),
    _Rm10010e40AlmMsaNetworkLaneAlarmWarning1_Type()
)
rm10010e40AlmMsaNetworkLaneAlarmWarning1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmMsaNetworkLaneAlarmWarning1.setStatus("current")
_Rm10010e40AlmMsaNetworkLaneFaultStatus_Type = EkiOnOff
_Rm10010e40AlmMsaNetworkLaneFaultStatus_Object = MibScalar
rm10010e40AlmMsaNetworkLaneFaultStatus = _Rm10010e40AlmMsaNetworkLaneFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 48, 14),
    _Rm10010e40AlmMsaNetworkLaneFaultStatus_Type()
)
rm10010e40AlmMsaNetworkLaneFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmMsaNetworkLaneFaultStatus.setStatus("current")
_Rm10010e40AlmMsaHostLaneFaultStatus_Type = EkiOnOff
_Rm10010e40AlmMsaHostLaneFaultStatus_Object = MibScalar
rm10010e40AlmMsaHostLaneFaultStatus = _Rm10010e40AlmMsaHostLaneFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 48, 15),
    _Rm10010e40AlmMsaHostLaneFaultStatus_Type()
)
rm10010e40AlmMsaHostLaneFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmMsaHostLaneFaultStatus.setStatus("current")
_Rm10010e40AlmMsaGlobAlarmAssertion_Type = EkiOnOff
_Rm10010e40AlmMsaGlobAlarmAssertion_Object = MibScalar
rm10010e40AlmMsaGlobAlarmAssertion = _Rm10010e40AlmMsaGlobAlarmAssertion_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 48, 16),
    _Rm10010e40AlmMsaGlobAlarmAssertion_Type()
)
rm10010e40AlmMsaGlobAlarmAssertion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmMsaGlobAlarmAssertion.setStatus("current")
_Rm10010e40AlmmsaNetworkTxAlignment_ObjectIdentity = ObjectIdentity
rm10010e40AlmmsaNetworkTxAlignment = _Rm10010e40AlmmsaNetworkTxAlignment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 49)
)
_Rm10010e40AlmNetTxTimingFault_Type = EkiOnOff
_Rm10010e40AlmNetTxTimingFault_Object = MibScalar
rm10010e40AlmNetTxTimingFault = _Rm10010e40AlmNetTxTimingFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 49, 12),
    _Rm10010e40AlmNetTxTimingFault_Type()
)
rm10010e40AlmNetTxTimingFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmNetTxTimingFault.setStatus("current")
_Rm10010e40AlmNetTxReferenceClockFault_Type = EkiOnOff
_Rm10010e40AlmNetTxReferenceClockFault_Object = MibScalar
rm10010e40AlmNetTxReferenceClockFault = _Rm10010e40AlmNetTxReferenceClockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 49, 13),
    _Rm10010e40AlmNetTxReferenceClockFault_Type()
)
rm10010e40AlmNetTxReferenceClockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmNetTxReferenceClockFault.setStatus("current")
_Rm10010e40AlmNetTxCmuLockFault_Type = EkiOnOff
_Rm10010e40AlmNetTxCmuLockFault_Object = MibScalar
rm10010e40AlmNetTxCmuLockFault = _Rm10010e40AlmNetTxCmuLockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 49, 14),
    _Rm10010e40AlmNetTxCmuLockFault_Type()
)
rm10010e40AlmNetTxCmuLockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmNetTxCmuLockFault.setStatus("current")
_Rm10010e40AlmNetTxOutOfAlignment_Type = EkiOnOff
_Rm10010e40AlmNetTxOutOfAlignment_Object = MibScalar
rm10010e40AlmNetTxOutOfAlignment = _Rm10010e40AlmNetTxOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 49, 15),
    _Rm10010e40AlmNetTxOutOfAlignment_Type()
)
rm10010e40AlmNetTxOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmNetTxOutOfAlignment.setStatus("current")
_Rm10010e40AlmNetTxLossOfAlignment_Type = EkiOnOff
_Rm10010e40AlmNetTxLossOfAlignment_Object = MibScalar
rm10010e40AlmNetTxLossOfAlignment = _Rm10010e40AlmNetTxLossOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 49, 16),
    _Rm10010e40AlmNetTxLossOfAlignment_Type()
)
rm10010e40AlmNetTxLossOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmNetTxLossOfAlignment.setStatus("current")
_Rm10010e40AlmmsaNetworkRxAlignment_ObjectIdentity = ObjectIdentity
rm10010e40AlmmsaNetworkRxAlignment = _Rm10010e40AlmmsaNetworkRxAlignment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 50)
)
_Rm10010e40AlmNetRxTimingFault_Type = EkiOnOff
_Rm10010e40AlmNetRxTimingFault_Object = MibScalar
rm10010e40AlmNetRxTimingFault = _Rm10010e40AlmNetRxTimingFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 50, 12),
    _Rm10010e40AlmNetRxTimingFault_Type()
)
rm10010e40AlmNetRxTimingFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmNetRxTimingFault.setStatus("current")
_Rm10010e40AlmNetRxOutOfAlignment_Type = EkiOnOff
_Rm10010e40AlmNetRxOutOfAlignment_Object = MibScalar
rm10010e40AlmNetRxOutOfAlignment = _Rm10010e40AlmNetRxOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 50, 13),
    _Rm10010e40AlmNetRxOutOfAlignment_Type()
)
rm10010e40AlmNetRxOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmNetRxOutOfAlignment.setStatus("current")
_Rm10010e40AlmNetRxLossOfAlignment_Type = EkiOnOff
_Rm10010e40AlmNetRxLossOfAlignment_Object = MibScalar
rm10010e40AlmNetRxLossOfAlignment = _Rm10010e40AlmNetRxLossOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 50, 14),
    _Rm10010e40AlmNetRxLossOfAlignment_Type()
)
rm10010e40AlmNetRxLossOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmNetRxLossOfAlignment.setStatus("current")
_Rm10010e40AlmNetRxModemLockFault_Type = EkiOnOff
_Rm10010e40AlmNetRxModemLockFault_Object = MibScalar
rm10010e40AlmNetRxModemLockFault = _Rm10010e40AlmNetRxModemLockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 50, 15),
    _Rm10010e40AlmNetRxModemLockFault_Type()
)
rm10010e40AlmNetRxModemLockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmNetRxModemLockFault.setStatus("current")
_Rm10010e40AlmNetRxModemSyncDetectFault_Type = EkiOnOff
_Rm10010e40AlmNetRxModemSyncDetectFault_Object = MibScalar
rm10010e40AlmNetRxModemSyncDetectFault = _Rm10010e40AlmNetRxModemSyncDetectFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 50, 16),
    _Rm10010e40AlmNetRxModemSyncDetectFault_Type()
)
rm10010e40AlmNetRxModemSyncDetectFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmNetRxModemSyncDetectFault.setStatus("current")
_Rm10010e40AlmmsaNetworkHostNetworkAlarmSummary_ObjectIdentity = ObjectIdentity
rm10010e40AlmmsaNetworkHostNetworkAlarmSummary = _Rm10010e40AlmmsaNetworkHostNetworkAlarmSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 51)
)
_Rm10010e40AlmNetworkTxAlignment_Type = EkiOnOff
_Rm10010e40AlmNetworkTxAlignment_Object = MibScalar
rm10010e40AlmNetworkTxAlignment = _Rm10010e40AlmNetworkTxAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 51, 11),
    _Rm10010e40AlmNetworkTxAlignment_Type()
)
rm10010e40AlmNetworkTxAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmNetworkTxAlignment.setStatus("current")
_Rm10010e40AlmNetworkRxAlignment_Type = EkiOnOff
_Rm10010e40AlmNetworkRxAlignment_Object = MibScalar
rm10010e40AlmNetworkRxAlignment = _Rm10010e40AlmNetworkRxAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 51, 12),
    _Rm10010e40AlmNetworkRxAlignment_Type()
)
rm10010e40AlmNetworkRxAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmNetworkRxAlignment.setStatus("current")
_Rm10010e40AlmNetworkRxOtn_Type = EkiOnOff
_Rm10010e40AlmNetworkRxOtn_Object = MibScalar
rm10010e40AlmNetworkRxOtn = _Rm10010e40AlmNetworkRxOtn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 51, 13),
    _Rm10010e40AlmNetworkRxOtn_Type()
)
rm10010e40AlmNetworkRxOtn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmNetworkRxOtn.setStatus("current")
_Rm10010e40AlmHostRxAlignment_Type = EkiOnOff
_Rm10010e40AlmHostRxAlignment_Object = MibScalar
rm10010e40AlmHostRxAlignment = _Rm10010e40AlmHostRxAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 51, 14),
    _Rm10010e40AlmHostRxAlignment_Type()
)
rm10010e40AlmHostRxAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmHostRxAlignment.setStatus("current")
_Rm10010e40AlmHostTxAlignment_Type = EkiOnOff
_Rm10010e40AlmHostTxAlignment_Object = MibScalar
rm10010e40AlmHostTxAlignment = _Rm10010e40AlmHostTxAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 51, 15),
    _Rm10010e40AlmHostTxAlignment_Type()
)
rm10010e40AlmHostTxAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmHostTxAlignment.setStatus("current")
_Rm10010e40AlmHostTxOtnStatus_Type = EkiOnOff
_Rm10010e40AlmHostTxOtnStatus_Object = MibScalar
rm10010e40AlmHostTxOtnStatus = _Rm10010e40AlmHostTxOtnStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 51, 16),
    _Rm10010e40AlmHostTxOtnStatus_Type()
)
rm10010e40AlmHostTxOtnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmHostTxOtnStatus.setStatus("current")
_Rm10010e40AlmmsaHostTxAlignment_ObjectIdentity = ObjectIdentity
rm10010e40AlmmsaHostTxAlignment = _Rm10010e40AlmmsaHostTxAlignment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 52)
)
_Rm10010e40AlmHostTxDeskewLockFault_Type = EkiOnOff
_Rm10010e40AlmHostTxDeskewLockFault_Object = MibScalar
rm10010e40AlmHostTxDeskewLockFault = _Rm10010e40AlmHostTxDeskewLockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 52, 13),
    _Rm10010e40AlmHostTxDeskewLockFault_Type()
)
rm10010e40AlmHostTxDeskewLockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmHostTxDeskewLockFault.setStatus("current")
_Rm10010e40AlmHostTxOutOfAlignment_Type = EkiOnOff
_Rm10010e40AlmHostTxOutOfAlignment_Object = MibScalar
rm10010e40AlmHostTxOutOfAlignment = _Rm10010e40AlmHostTxOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 52, 14),
    _Rm10010e40AlmHostTxOutOfAlignment_Type()
)
rm10010e40AlmHostTxOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmHostTxOutOfAlignment.setStatus("current")
_Rm10010e40AlmHostTxLossOfAlignment_Type = EkiOnOff
_Rm10010e40AlmHostTxLossOfAlignment_Object = MibScalar
rm10010e40AlmHostTxLossOfAlignment = _Rm10010e40AlmHostTxLossOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 52, 15),
    _Rm10010e40AlmHostTxLossOfAlignment_Type()
)
rm10010e40AlmHostTxLossOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmHostTxLossOfAlignment.setStatus("current")
_Rm10010e40AlmHostTxCdrLockFault_Type = EkiOnOff
_Rm10010e40AlmHostTxCdrLockFault_Object = MibScalar
rm10010e40AlmHostTxCdrLockFault = _Rm10010e40AlmHostTxCdrLockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 52, 16),
    _Rm10010e40AlmHostTxCdrLockFault_Type()
)
rm10010e40AlmHostTxCdrLockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmHostTxCdrLockFault.setStatus("current")
_Rm10010e40AlmmsaHostRxAlignment_ObjectIdentity = ObjectIdentity
rm10010e40AlmmsaHostRxAlignment = _Rm10010e40AlmmsaHostRxAlignment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 53)
)
_Rm10010e40AlmHostRxCmuLockFault_Type = EkiOnOff
_Rm10010e40AlmHostRxCmuLockFault_Object = MibScalar
rm10010e40AlmHostRxCmuLockFault = _Rm10010e40AlmHostRxCmuLockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 53, 14),
    _Rm10010e40AlmHostRxCmuLockFault_Type()
)
rm10010e40AlmHostRxCmuLockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmHostRxCmuLockFault.setStatus("current")
_Rm10010e40AlmHostRxOutOfAlignment_Type = EkiOnOff
_Rm10010e40AlmHostRxOutOfAlignment_Object = MibScalar
rm10010e40AlmHostRxOutOfAlignment = _Rm10010e40AlmHostRxOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 53, 15),
    _Rm10010e40AlmHostRxOutOfAlignment_Type()
)
rm10010e40AlmHostRxOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmHostRxOutOfAlignment.setStatus("current")
_Rm10010e40AlmHostRxLossOfAlignment_Type = EkiOnOff
_Rm10010e40AlmHostRxLossOfAlignment_Object = MibScalar
rm10010e40AlmHostRxLossOfAlignment = _Rm10010e40AlmHostRxLossOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 1, 3, 53, 16),
    _Rm10010e40AlmHostRxLossOfAlignment_Type()
)
rm10010e40AlmHostRxLossOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmHostRxLossOfAlignment.setStatus("current")
_Rm10010e40AlmClient_ObjectIdentity = ObjectIdentity
rm10010e40AlmClient = _Rm10010e40AlmClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2)
)
_Rm10010e40AlmClientNurg_ObjectIdentity = ObjectIdentity
rm10010e40AlmClientNurg = _Rm10010e40AlmClientNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 1)
)
_Rm10010e40AlmclientNetworkLaneAlarmWarningTable_Object = MibTable
rm10010e40AlmclientNetworkLaneAlarmWarningTable = _Rm10010e40AlmclientNetworkLaneAlarmWarningTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 1, 56)
)
if mibBuilder.loadTexts:
    rm10010e40AlmclientNetworkLaneAlarmWarningTable.setStatus("current")
_Rm10010e40AlmclientNetworkLaneAlarmWarningEntry_Object = MibTableRow
rm10010e40AlmclientNetworkLaneAlarmWarningEntry = _Rm10010e40AlmclientNetworkLaneAlarmWarningEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 1, 56, 1)
)
rm10010e40AlmclientNetworkLaneAlarmWarningEntry.setIndexNames(
    (0, "EKINOPS-Rm10010e40-MIB", "rm10010e40AlmclientNetworkLaneAlarmWarningIndex"),
)
if mibBuilder.loadTexts:
    rm10010e40AlmclientNetworkLaneAlarmWarningEntry.setStatus("current")


class _Rm10010e40AlmclientNetworkLaneAlarmWarningIndex_Type(Integer32):
    """Custom type rm10010e40AlmclientNetworkLaneAlarmWarningIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010e40AlmclientNetworkLaneAlarmWarningIndex_Type.__name__ = "Integer32"
_Rm10010e40AlmclientNetworkLaneAlarmWarningIndex_Object = MibTableColumn
rm10010e40AlmclientNetworkLaneAlarmWarningIndex = _Rm10010e40AlmclientNetworkLaneAlarmWarningIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 1, 56, 1, 1),
    _Rm10010e40AlmclientNetworkLaneAlarmWarningIndex_Type()
)
rm10010e40AlmclientNetworkLaneAlarmWarningIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmclientNetworkLaneAlarmWarningIndex.setStatus("current")
_Rm10010e40AlmClientRxPowerLowAlarmPortn_Type = EkiOnOff
_Rm10010e40AlmClientRxPowerLowAlarmPortn_Object = MibTableColumn
rm10010e40AlmClientRxPowerLowAlarmPortn = _Rm10010e40AlmClientRxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 1, 56, 1, 2),
    _Rm10010e40AlmClientRxPowerLowAlarmPortn_Type()
)
rm10010e40AlmClientRxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmClientRxPowerLowAlarmPortn.setStatus("current")
_Rm10010e40AlmClientRxPowerLowWarningPortn_Type = EkiOnOff
_Rm10010e40AlmClientRxPowerLowWarningPortn_Object = MibTableColumn
rm10010e40AlmClientRxPowerLowWarningPortn = _Rm10010e40AlmClientRxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 1, 56, 1, 3),
    _Rm10010e40AlmClientRxPowerLowWarningPortn_Type()
)
rm10010e40AlmClientRxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmClientRxPowerLowWarningPortn.setStatus("current")
_Rm10010e40AlmClientRxPowerHighWarningPortn_Type = EkiOnOff
_Rm10010e40AlmClientRxPowerHighWarningPortn_Object = MibTableColumn
rm10010e40AlmClientRxPowerHighWarningPortn = _Rm10010e40AlmClientRxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 1, 56, 1, 4),
    _Rm10010e40AlmClientRxPowerHighWarningPortn_Type()
)
rm10010e40AlmClientRxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmClientRxPowerHighWarningPortn.setStatus("current")
_Rm10010e40AlmClientRxPowerHighAlarmPortn_Type = EkiOnOff
_Rm10010e40AlmClientRxPowerHighAlarmPortn_Object = MibTableColumn
rm10010e40AlmClientRxPowerHighAlarmPortn = _Rm10010e40AlmClientRxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 1, 56, 1, 5),
    _Rm10010e40AlmClientRxPowerHighAlarmPortn_Type()
)
rm10010e40AlmClientRxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmClientRxPowerHighAlarmPortn.setStatus("current")
_Rm10010e40AlmLaserTempLowAlarmPortn_Type = EkiOnOff
_Rm10010e40AlmLaserTempLowAlarmPortn_Object = MibTableColumn
rm10010e40AlmLaserTempLowAlarmPortn = _Rm10010e40AlmLaserTempLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 1, 56, 1, 6),
    _Rm10010e40AlmLaserTempLowAlarmPortn_Type()
)
rm10010e40AlmLaserTempLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmLaserTempLowAlarmPortn.setStatus("current")
_Rm10010e40AlmClientLaserTempLowWarningPortn_Type = EkiOnOff
_Rm10010e40AlmClientLaserTempLowWarningPortn_Object = MibTableColumn
rm10010e40AlmClientLaserTempLowWarningPortn = _Rm10010e40AlmClientLaserTempLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 1, 56, 1, 7),
    _Rm10010e40AlmClientLaserTempLowWarningPortn_Type()
)
rm10010e40AlmClientLaserTempLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmClientLaserTempLowWarningPortn.setStatus("current")
_Rm10010e40AlmClientLaserTempHighWarningPortn_Type = EkiOnOff
_Rm10010e40AlmClientLaserTempHighWarningPortn_Object = MibTableColumn
rm10010e40AlmClientLaserTempHighWarningPortn = _Rm10010e40AlmClientLaserTempHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 1, 56, 1, 8),
    _Rm10010e40AlmClientLaserTempHighWarningPortn_Type()
)
rm10010e40AlmClientLaserTempHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmClientLaserTempHighWarningPortn.setStatus("current")
_Rm10010e40AlmClientLaserTempHighAlarmPortn_Type = EkiOnOff
_Rm10010e40AlmClientLaserTempHighAlarmPortn_Object = MibTableColumn
rm10010e40AlmClientLaserTempHighAlarmPortn = _Rm10010e40AlmClientLaserTempHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 1, 56, 1, 9),
    _Rm10010e40AlmClientLaserTempHighAlarmPortn_Type()
)
rm10010e40AlmClientLaserTempHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmClientLaserTempHighAlarmPortn.setStatus("current")
_Rm10010e40AlmClientTxPowerLowAlarmPortn_Type = EkiOnOff
_Rm10010e40AlmClientTxPowerLowAlarmPortn_Object = MibTableColumn
rm10010e40AlmClientTxPowerLowAlarmPortn = _Rm10010e40AlmClientTxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 1, 56, 1, 10),
    _Rm10010e40AlmClientTxPowerLowAlarmPortn_Type()
)
rm10010e40AlmClientTxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmClientTxPowerLowAlarmPortn.setStatus("current")
_Rm10010e40AlmClientTxPowerLowWarningPortn_Type = EkiOnOff
_Rm10010e40AlmClientTxPowerLowWarningPortn_Object = MibTableColumn
rm10010e40AlmClientTxPowerLowWarningPortn = _Rm10010e40AlmClientTxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 1, 56, 1, 11),
    _Rm10010e40AlmClientTxPowerLowWarningPortn_Type()
)
rm10010e40AlmClientTxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmClientTxPowerLowWarningPortn.setStatus("current")
_Rm10010e40AlmClientTxPowerHighWarningPortn_Type = EkiOnOff
_Rm10010e40AlmClientTxPowerHighWarningPortn_Object = MibTableColumn
rm10010e40AlmClientTxPowerHighWarningPortn = _Rm10010e40AlmClientTxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 1, 56, 1, 12),
    _Rm10010e40AlmClientTxPowerHighWarningPortn_Type()
)
rm10010e40AlmClientTxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmClientTxPowerHighWarningPortn.setStatus("current")
_Rm10010e40AlmClientTxPowerHighAlarmPortn_Type = EkiOnOff
_Rm10010e40AlmClientTxPowerHighAlarmPortn_Object = MibTableColumn
rm10010e40AlmClientTxPowerHighAlarmPortn = _Rm10010e40AlmClientTxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 1, 56, 1, 13),
    _Rm10010e40AlmClientTxPowerHighAlarmPortn_Type()
)
rm10010e40AlmClientTxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmClientTxPowerHighAlarmPortn.setStatus("current")
_Rm10010e40AlmClientBiasLowAlarmPortn_Type = EkiOnOff
_Rm10010e40AlmClientBiasLowAlarmPortn_Object = MibTableColumn
rm10010e40AlmClientBiasLowAlarmPortn = _Rm10010e40AlmClientBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 1, 56, 1, 14),
    _Rm10010e40AlmClientBiasLowAlarmPortn_Type()
)
rm10010e40AlmClientBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmClientBiasLowAlarmPortn.setStatus("current")
_Rm10010e40AlmClientBiasLowWarningPortn_Type = EkiOnOff
_Rm10010e40AlmClientBiasLowWarningPortn_Object = MibTableColumn
rm10010e40AlmClientBiasLowWarningPortn = _Rm10010e40AlmClientBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 1, 56, 1, 15),
    _Rm10010e40AlmClientBiasLowWarningPortn_Type()
)
rm10010e40AlmClientBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmClientBiasLowWarningPortn.setStatus("current")
_Rm10010e40AlmClientBiasHighWarningPortn_Type = EkiOnOff
_Rm10010e40AlmClientBiasHighWarningPortn_Object = MibTableColumn
rm10010e40AlmClientBiasHighWarningPortn = _Rm10010e40AlmClientBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 1, 56, 1, 16),
    _Rm10010e40AlmClientBiasHighWarningPortn_Type()
)
rm10010e40AlmClientBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmClientBiasHighWarningPortn.setStatus("current")
_Rm10010e40AlmClientBiasHighAlarmPortn_Type = EkiOnOff
_Rm10010e40AlmClientBiasHighAlarmPortn_Object = MibTableColumn
rm10010e40AlmClientBiasHighAlarmPortn = _Rm10010e40AlmClientBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 1, 56, 1, 17),
    _Rm10010e40AlmClientBiasHighAlarmPortn_Type()
)
rm10010e40AlmClientBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmClientBiasHighAlarmPortn.setStatus("current")
_Rm10010e40AlmclientSfpWarnDdmTable_Object = MibTable
rm10010e40AlmclientSfpWarnDdmTable = _Rm10010e40AlmclientSfpWarnDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 1, 232)
)
if mibBuilder.loadTexts:
    rm10010e40AlmclientSfpWarnDdmTable.setStatus("current")
_Rm10010e40AlmclientSfpWarnDdmEntry_Object = MibTableRow
rm10010e40AlmclientSfpWarnDdmEntry = _Rm10010e40AlmclientSfpWarnDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 1, 232, 1)
)
rm10010e40AlmclientSfpWarnDdmEntry.setIndexNames(
    (0, "EKINOPS-Rm10010e40-MIB", "rm10010e40AlmclientSfpWarnDdmIndex"),
)
if mibBuilder.loadTexts:
    rm10010e40AlmclientSfpWarnDdmEntry.setStatus("current")


class _Rm10010e40AlmclientSfpWarnDdmIndex_Type(Integer32):
    """Custom type rm10010e40AlmclientSfpWarnDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010e40AlmclientSfpWarnDdmIndex_Type.__name__ = "Integer32"
_Rm10010e40AlmclientSfpWarnDdmIndex_Object = MibTableColumn
rm10010e40AlmclientSfpWarnDdmIndex = _Rm10010e40AlmclientSfpWarnDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 1, 232, 1, 1),
    _Rm10010e40AlmclientSfpWarnDdmIndex_Type()
)
rm10010e40AlmclientSfpWarnDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmclientSfpWarnDdmIndex.setStatus("current")
_Rm10010e40AlmTxPwLowWngPortn_Type = EkiOnOff
_Rm10010e40AlmTxPwLowWngPortn_Object = MibTableColumn
rm10010e40AlmTxPwLowWngPortn = _Rm10010e40AlmTxPwLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 1, 232, 1, 2),
    _Rm10010e40AlmTxPwLowWngPortn_Type()
)
rm10010e40AlmTxPwLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmTxPwLowWngPortn.setStatus("current")
_Rm10010e40AlmTxPwrHighWngPortn_Type = EkiOnOff
_Rm10010e40AlmTxPwrHighWngPortn_Object = MibTableColumn
rm10010e40AlmTxPwrHighWngPortn = _Rm10010e40AlmTxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 1, 232, 1, 3),
    _Rm10010e40AlmTxPwrHighWngPortn_Type()
)
rm10010e40AlmTxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmTxPwrHighWngPortn.setStatus("current")
_Rm10010e40AlmTxBiasLowWngPortn_Type = EkiOnOff
_Rm10010e40AlmTxBiasLowWngPortn_Object = MibTableColumn
rm10010e40AlmTxBiasLowWngPortn = _Rm10010e40AlmTxBiasLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 1, 232, 1, 4),
    _Rm10010e40AlmTxBiasLowWngPortn_Type()
)
rm10010e40AlmTxBiasLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmTxBiasLowWngPortn.setStatus("current")
_Rm10010e40AlmTxBiasHighWngPortn_Type = EkiOnOff
_Rm10010e40AlmTxBiasHighWngPortn_Object = MibTableColumn
rm10010e40AlmTxBiasHighWngPortn = _Rm10010e40AlmTxBiasHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 1, 232, 1, 5),
    _Rm10010e40AlmTxBiasHighWngPortn_Type()
)
rm10010e40AlmTxBiasHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmTxBiasHighWngPortn.setStatus("current")
_Rm10010e40AlmVccLowWngPortn_Type = EkiOnOff
_Rm10010e40AlmVccLowWngPortn_Object = MibTableColumn
rm10010e40AlmVccLowWngPortn = _Rm10010e40AlmVccLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 1, 232, 1, 6),
    _Rm10010e40AlmVccLowWngPortn_Type()
)
rm10010e40AlmVccLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmVccLowWngPortn.setStatus("current")
_Rm10010e40AlmVccHighWngPortn_Type = EkiOnOff
_Rm10010e40AlmVccHighWngPortn_Object = MibTableColumn
rm10010e40AlmVccHighWngPortn = _Rm10010e40AlmVccHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 1, 232, 1, 7),
    _Rm10010e40AlmVccHighWngPortn_Type()
)
rm10010e40AlmVccHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmVccHighWngPortn.setStatus("current")
_Rm10010e40AlmTempLowWngPortn_Type = EkiOnOff
_Rm10010e40AlmTempLowWngPortn_Object = MibTableColumn
rm10010e40AlmTempLowWngPortn = _Rm10010e40AlmTempLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 1, 232, 1, 8),
    _Rm10010e40AlmTempLowWngPortn_Type()
)
rm10010e40AlmTempLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmTempLowWngPortn.setStatus("current")
_Rm10010e40AlmTempHighWngPortn_Type = EkiOnOff
_Rm10010e40AlmTempHighWngPortn_Object = MibTableColumn
rm10010e40AlmTempHighWngPortn = _Rm10010e40AlmTempHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 1, 232, 1, 9),
    _Rm10010e40AlmTempHighWngPortn_Type()
)
rm10010e40AlmTempHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmTempHighWngPortn.setStatus("current")
_Rm10010e40AlmRxPwrLowWngPortn_Type = EkiOnOff
_Rm10010e40AlmRxPwrLowWngPortn_Object = MibTableColumn
rm10010e40AlmRxPwrLowWngPortn = _Rm10010e40AlmRxPwrLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 1, 232, 1, 16),
    _Rm10010e40AlmRxPwrLowWngPortn_Type()
)
rm10010e40AlmRxPwrLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmRxPwrLowWngPortn.setStatus("current")
_Rm10010e40AlmRxPwrHighWngPortn_Type = EkiOnOff
_Rm10010e40AlmRxPwrHighWngPortn_Object = MibTableColumn
rm10010e40AlmRxPwrHighWngPortn = _Rm10010e40AlmRxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 1, 232, 1, 17),
    _Rm10010e40AlmRxPwrHighWngPortn_Type()
)
rm10010e40AlmRxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmRxPwrHighWngPortn.setStatus("current")
_Rm10010e40AlmClientUrg_ObjectIdentity = ObjectIdentity
rm10010e40AlmClientUrg = _Rm10010e40AlmClientUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 2)
)
_Rm10010e40AlmclientNetworkLaneFaultTable_Object = MibTable
rm10010e40AlmclientNetworkLaneFaultTable = _Rm10010e40AlmclientNetworkLaneFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 2, 72)
)
if mibBuilder.loadTexts:
    rm10010e40AlmclientNetworkLaneFaultTable.setStatus("current")
_Rm10010e40AlmclientNetworkLaneFaultEntry_Object = MibTableRow
rm10010e40AlmclientNetworkLaneFaultEntry = _Rm10010e40AlmclientNetworkLaneFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 2, 72, 1)
)
rm10010e40AlmclientNetworkLaneFaultEntry.setIndexNames(
    (0, "EKINOPS-Rm10010e40-MIB", "rm10010e40AlmclientNetworkLaneFaultIndex"),
)
if mibBuilder.loadTexts:
    rm10010e40AlmclientNetworkLaneFaultEntry.setStatus("current")


class _Rm10010e40AlmclientNetworkLaneFaultIndex_Type(Integer32):
    """Custom type rm10010e40AlmclientNetworkLaneFaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010e40AlmclientNetworkLaneFaultIndex_Type.__name__ = "Integer32"
_Rm10010e40AlmclientNetworkLaneFaultIndex_Object = MibTableColumn
rm10010e40AlmclientNetworkLaneFaultIndex = _Rm10010e40AlmclientNetworkLaneFaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 2, 72, 1, 1),
    _Rm10010e40AlmclientNetworkLaneFaultIndex_Type()
)
rm10010e40AlmclientNetworkLaneFaultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmclientNetworkLaneFaultIndex.setStatus("current")
_Rm10010e40AlmClientLaneRxFifoErrorPortn_Type = EkiOnOff
_Rm10010e40AlmClientLaneRxFifoErrorPortn_Object = MibTableColumn
rm10010e40AlmClientLaneRxFifoErrorPortn = _Rm10010e40AlmClientLaneRxFifoErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 2, 72, 1, 4),
    _Rm10010e40AlmClientLaneRxFifoErrorPortn_Type()
)
rm10010e40AlmClientLaneRxFifoErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmClientLaneRxFifoErrorPortn.setStatus("current")
_Rm10010e40AlmClientLaneRxLolPortn_Type = EkiOnOff
_Rm10010e40AlmClientLaneRxLolPortn_Object = MibTableColumn
rm10010e40AlmClientLaneRxLolPortn = _Rm10010e40AlmClientLaneRxLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 2, 72, 1, 5),
    _Rm10010e40AlmClientLaneRxLolPortn_Type()
)
rm10010e40AlmClientLaneRxLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmClientLaneRxLolPortn.setStatus("current")
_Rm10010e40AlmClientLaneRxLosPortn_Type = EkiOnOff
_Rm10010e40AlmClientLaneRxLosPortn_Object = MibTableColumn
rm10010e40AlmClientLaneRxLosPortn = _Rm10010e40AlmClientLaneRxLosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 2, 72, 1, 6),
    _Rm10010e40AlmClientLaneRxLosPortn_Type()
)
rm10010e40AlmClientLaneRxLosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmClientLaneRxLosPortn.setStatus("current")
_Rm10010e40AlmClientLaneTxLolPortn_Type = EkiOnOff
_Rm10010e40AlmClientLaneTxLolPortn_Object = MibTableColumn
rm10010e40AlmClientLaneTxLolPortn = _Rm10010e40AlmClientLaneTxLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 2, 72, 1, 8),
    _Rm10010e40AlmClientLaneTxLolPortn_Type()
)
rm10010e40AlmClientLaneTxLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmClientLaneTxLolPortn.setStatus("current")
_Rm10010e40AlmClientLaneTxLosfPortn_Type = EkiOnOff
_Rm10010e40AlmClientLaneTxLosfPortn_Object = MibTableColumn
rm10010e40AlmClientLaneTxLosfPortn = _Rm10010e40AlmClientLaneTxLosfPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 2, 72, 1, 9),
    _Rm10010e40AlmClientLaneTxLosfPortn_Type()
)
rm10010e40AlmClientLaneTxLosfPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmClientLaneTxLosfPortn.setStatus("current")
_Rm10010e40AlmClientLaneApdPowerSupplyPortn_Type = EkiOnOff
_Rm10010e40AlmClientLaneApdPowerSupplyPortn_Object = MibTableColumn
rm10010e40AlmClientLaneApdPowerSupplyPortn = _Rm10010e40AlmClientLaneApdPowerSupplyPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 2, 72, 1, 15),
    _Rm10010e40AlmClientLaneApdPowerSupplyPortn_Type()
)
rm10010e40AlmClientLaneApdPowerSupplyPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmClientLaneApdPowerSupplyPortn.setStatus("current")
_Rm10010e40AlmClientLaneWavelengthUnlockedPortn_Type = EkiOnOff
_Rm10010e40AlmClientLaneWavelengthUnlockedPortn_Object = MibTableColumn
rm10010e40AlmClientLaneWavelengthUnlockedPortn = _Rm10010e40AlmClientLaneWavelengthUnlockedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 2, 72, 1, 16),
    _Rm10010e40AlmClientLaneWavelengthUnlockedPortn_Type()
)
rm10010e40AlmClientLaneWavelengthUnlockedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmClientLaneWavelengthUnlockedPortn.setStatus("current")
_Rm10010e40AlmClientLaneTecFaultPortn_Type = EkiOnOff
_Rm10010e40AlmClientLaneTecFaultPortn_Object = MibTableColumn
rm10010e40AlmClientLaneTecFaultPortn = _Rm10010e40AlmClientLaneTecFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 2, 72, 1, 17),
    _Rm10010e40AlmClientLaneTecFaultPortn_Type()
)
rm10010e40AlmClientLaneTecFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmClientLaneTecFaultPortn.setStatus("current")
_Rm10010e40AlmclientHostLaneFaultTable_Object = MibTable
rm10010e40AlmclientHostLaneFaultTable = _Rm10010e40AlmclientHostLaneFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 2, 88)
)
if mibBuilder.loadTexts:
    rm10010e40AlmclientHostLaneFaultTable.setStatus("current")
_Rm10010e40AlmclientHostLaneFaultEntry_Object = MibTableRow
rm10010e40AlmclientHostLaneFaultEntry = _Rm10010e40AlmclientHostLaneFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 2, 88, 1)
)
rm10010e40AlmclientHostLaneFaultEntry.setIndexNames(
    (0, "EKINOPS-Rm10010e40-MIB", "rm10010e40AlmclientHostLaneFaultIndex"),
)
if mibBuilder.loadTexts:
    rm10010e40AlmclientHostLaneFaultEntry.setStatus("current")


class _Rm10010e40AlmclientHostLaneFaultIndex_Type(Integer32):
    """Custom type rm10010e40AlmclientHostLaneFaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010e40AlmclientHostLaneFaultIndex_Type.__name__ = "Integer32"
_Rm10010e40AlmclientHostLaneFaultIndex_Object = MibTableColumn
rm10010e40AlmclientHostLaneFaultIndex = _Rm10010e40AlmclientHostLaneFaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 2, 88, 1, 1),
    _Rm10010e40AlmclientHostLaneFaultIndex_Type()
)
rm10010e40AlmclientHostLaneFaultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmclientHostLaneFaultIndex.setStatus("current")
_Rm10010e40AlmClientLossOfSyncPortn_Type = EkiOnOff
_Rm10010e40AlmClientLossOfSyncPortn_Object = MibTableColumn
rm10010e40AlmClientLossOfSyncPortn = _Rm10010e40AlmClientLossOfSyncPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 2, 88, 1, 2),
    _Rm10010e40AlmClientLossOfSyncPortn_Type()
)
rm10010e40AlmClientLossOfSyncPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmClientLossOfSyncPortn.setStatus("current")
_Rm10010e40AlmClientInputLossOfSigPortn_Type = EkiOnOff
_Rm10010e40AlmClientInputLossOfSigPortn_Object = MibTableColumn
rm10010e40AlmClientInputLossOfSigPortn = _Rm10010e40AlmClientInputLossOfSigPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 2, 88, 1, 3),
    _Rm10010e40AlmClientInputLossOfSigPortn_Type()
)
rm10010e40AlmClientInputLossOfSigPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmClientInputLossOfSigPortn.setStatus("current")
_Rm10010e40AlmClientLanesMarkerUnlockPortn_Type = EkiOnOff
_Rm10010e40AlmClientLanesMarkerUnlockPortn_Object = MibTableColumn
rm10010e40AlmClientLanesMarkerUnlockPortn = _Rm10010e40AlmClientLanesMarkerUnlockPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 2, 88, 1, 4),
    _Rm10010e40AlmClientLanesMarkerUnlockPortn_Type()
)
rm10010e40AlmClientLanesMarkerUnlockPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmClientLanesMarkerUnlockPortn.setStatus("current")
_Rm10010e40AlmClientLanes6466UnlockPortn_Type = EkiOnOff
_Rm10010e40AlmClientLanes6466UnlockPortn_Object = MibTableColumn
rm10010e40AlmClientLanes6466UnlockPortn = _Rm10010e40AlmClientLanes6466UnlockPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 2, 88, 1, 5),
    _Rm10010e40AlmClientLanes6466UnlockPortn_Type()
)
rm10010e40AlmClientLanes6466UnlockPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmClientLanes6466UnlockPortn.setStatus("current")
_Rm10010e40AlmClientLanesNotAlignedPortn_Type = EkiOnOff
_Rm10010e40AlmClientLanesNotAlignedPortn_Object = MibTableColumn
rm10010e40AlmClientLanesNotAlignedPortn = _Rm10010e40AlmClientLanesNotAlignedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 2, 88, 1, 6),
    _Rm10010e40AlmClientLanesNotAlignedPortn_Type()
)
rm10010e40AlmClientLanesNotAlignedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmClientLanesNotAlignedPortn.setStatus("current")
_Rm10010e40AlmClientCsfDetectedPortn_Type = EkiOnOff
_Rm10010e40AlmClientCsfDetectedPortn_Object = MibTableColumn
rm10010e40AlmClientCsfDetectedPortn = _Rm10010e40AlmClientCsfDetectedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 2, 88, 1, 7),
    _Rm10010e40AlmClientCsfDetectedPortn_Type()
)
rm10010e40AlmClientCsfDetectedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmClientCsfDetectedPortn.setStatus("current")
_Rm10010e40AlmClientTxHostLolPortn_Type = EkiOnOff
_Rm10010e40AlmClientTxHostLolPortn_Object = MibTableColumn
rm10010e40AlmClientTxHostLolPortn = _Rm10010e40AlmClientTxHostLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 2, 88, 1, 10),
    _Rm10010e40AlmClientTxHostLolPortn_Type()
)
rm10010e40AlmClientTxHostLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmClientTxHostLolPortn.setStatus("current")
_Rm10010e40AlmClientLaneTxFifoErrorPortn_Type = EkiOnOff
_Rm10010e40AlmClientLaneTxFifoErrorPortn_Object = MibTableColumn
rm10010e40AlmClientLaneTxFifoErrorPortn = _Rm10010e40AlmClientLaneTxFifoErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 2, 88, 1, 11),
    _Rm10010e40AlmClientLaneTxFifoErrorPortn_Type()
)
rm10010e40AlmClientLaneTxFifoErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmClientLaneTxFifoErrorPortn.setStatus("current")
_Rm10010e40AlmclientSfpAlmDdmTable_Object = MibTable
rm10010e40AlmclientSfpAlmDdmTable = _Rm10010e40AlmclientSfpAlmDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 2, 216)
)
if mibBuilder.loadTexts:
    rm10010e40AlmclientSfpAlmDdmTable.setStatus("current")
_Rm10010e40AlmclientSfpAlmDdmEntry_Object = MibTableRow
rm10010e40AlmclientSfpAlmDdmEntry = _Rm10010e40AlmclientSfpAlmDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 2, 216, 1)
)
rm10010e40AlmclientSfpAlmDdmEntry.setIndexNames(
    (0, "EKINOPS-Rm10010e40-MIB", "rm10010e40AlmclientSfpAlmDdmIndex"),
)
if mibBuilder.loadTexts:
    rm10010e40AlmclientSfpAlmDdmEntry.setStatus("current")


class _Rm10010e40AlmclientSfpAlmDdmIndex_Type(Integer32):
    """Custom type rm10010e40AlmclientSfpAlmDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010e40AlmclientSfpAlmDdmIndex_Type.__name__ = "Integer32"
_Rm10010e40AlmclientSfpAlmDdmIndex_Object = MibTableColumn
rm10010e40AlmclientSfpAlmDdmIndex = _Rm10010e40AlmclientSfpAlmDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 2, 216, 1, 1),
    _Rm10010e40AlmclientSfpAlmDdmIndex_Type()
)
rm10010e40AlmclientSfpAlmDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmclientSfpAlmDdmIndex.setStatus("current")
_Rm10010e40AlmTxPwrLowAlaPortn_Type = EkiOnOff
_Rm10010e40AlmTxPwrLowAlaPortn_Object = MibTableColumn
rm10010e40AlmTxPwrLowAlaPortn = _Rm10010e40AlmTxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 2, 216, 1, 2),
    _Rm10010e40AlmTxPwrLowAlaPortn_Type()
)
rm10010e40AlmTxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmTxPwrLowAlaPortn.setStatus("current")
_Rm10010e40AlmTxPwrHighAlaPortn_Type = EkiOnOff
_Rm10010e40AlmTxPwrHighAlaPortn_Object = MibTableColumn
rm10010e40AlmTxPwrHighAlaPortn = _Rm10010e40AlmTxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 2, 216, 1, 3),
    _Rm10010e40AlmTxPwrHighAlaPortn_Type()
)
rm10010e40AlmTxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmTxPwrHighAlaPortn.setStatus("current")
_Rm10010e40AlmTxBiasLowAlaPortn_Type = EkiOnOff
_Rm10010e40AlmTxBiasLowAlaPortn_Object = MibTableColumn
rm10010e40AlmTxBiasLowAlaPortn = _Rm10010e40AlmTxBiasLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 2, 216, 1, 4),
    _Rm10010e40AlmTxBiasLowAlaPortn_Type()
)
rm10010e40AlmTxBiasLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmTxBiasLowAlaPortn.setStatus("current")
_Rm10010e40AlmTxBiasHighAlaPortn_Type = EkiOnOff
_Rm10010e40AlmTxBiasHighAlaPortn_Object = MibTableColumn
rm10010e40AlmTxBiasHighAlaPortn = _Rm10010e40AlmTxBiasHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 2, 216, 1, 5),
    _Rm10010e40AlmTxBiasHighAlaPortn_Type()
)
rm10010e40AlmTxBiasHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmTxBiasHighAlaPortn.setStatus("current")
_Rm10010e40AlmVccLowAlaPortn_Type = EkiOnOff
_Rm10010e40AlmVccLowAlaPortn_Object = MibTableColumn
rm10010e40AlmVccLowAlaPortn = _Rm10010e40AlmVccLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 2, 216, 1, 6),
    _Rm10010e40AlmVccLowAlaPortn_Type()
)
rm10010e40AlmVccLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmVccLowAlaPortn.setStatus("current")
_Rm10010e40AlmVccHighAlaPortn_Type = EkiOnOff
_Rm10010e40AlmVccHighAlaPortn_Object = MibTableColumn
rm10010e40AlmVccHighAlaPortn = _Rm10010e40AlmVccHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 2, 216, 1, 7),
    _Rm10010e40AlmVccHighAlaPortn_Type()
)
rm10010e40AlmVccHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmVccHighAlaPortn.setStatus("current")
_Rm10010e40AlmTempLowAlaPortn_Type = EkiOnOff
_Rm10010e40AlmTempLowAlaPortn_Object = MibTableColumn
rm10010e40AlmTempLowAlaPortn = _Rm10010e40AlmTempLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 2, 216, 1, 8),
    _Rm10010e40AlmTempLowAlaPortn_Type()
)
rm10010e40AlmTempLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmTempLowAlaPortn.setStatus("current")
_Rm10010e40AlmTempHighAlaPortn_Type = EkiOnOff
_Rm10010e40AlmTempHighAlaPortn_Object = MibTableColumn
rm10010e40AlmTempHighAlaPortn = _Rm10010e40AlmTempHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 2, 216, 1, 9),
    _Rm10010e40AlmTempHighAlaPortn_Type()
)
rm10010e40AlmTempHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmTempHighAlaPortn.setStatus("current")
_Rm10010e40AlmRxPwrLowAlaPortn_Type = EkiOnOff
_Rm10010e40AlmRxPwrLowAlaPortn_Object = MibTableColumn
rm10010e40AlmRxPwrLowAlaPortn = _Rm10010e40AlmRxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 2, 216, 1, 16),
    _Rm10010e40AlmRxPwrLowAlaPortn_Type()
)
rm10010e40AlmRxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmRxPwrLowAlaPortn.setStatus("current")
_Rm10010e40AlmRxPwrHighAlaPortn_Type = EkiOnOff
_Rm10010e40AlmRxPwrHighAlaPortn_Object = MibTableColumn
rm10010e40AlmRxPwrHighAlaPortn = _Rm10010e40AlmRxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 2, 216, 1, 17),
    _Rm10010e40AlmRxPwrHighAlaPortn_Type()
)
rm10010e40AlmRxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmRxPwrHighAlaPortn.setStatus("current")
_Rm10010e40AlmClientCrit_ObjectIdentity = ObjectIdentity
rm10010e40AlmClientCrit = _Rm10010e40AlmClientCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 3)
)
_Rm10010e40AlmsynthAlmPortTable_Object = MibTable
rm10010e40AlmsynthAlmPortTable = _Rm10010e40AlmsynthAlmPortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 3, 8)
)
if mibBuilder.loadTexts:
    rm10010e40AlmsynthAlmPortTable.setStatus("current")
_Rm10010e40AlmsynthAlmPortEntry_Object = MibTableRow
rm10010e40AlmsynthAlmPortEntry = _Rm10010e40AlmsynthAlmPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 3, 8, 1)
)
rm10010e40AlmsynthAlmPortEntry.setIndexNames(
    (0, "EKINOPS-Rm10010e40-MIB", "rm10010e40AlmsynthAlmPortIndex"),
)
if mibBuilder.loadTexts:
    rm10010e40AlmsynthAlmPortEntry.setStatus("current")


class _Rm10010e40AlmsynthAlmPortIndex_Type(Integer32):
    """Custom type rm10010e40AlmsynthAlmPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010e40AlmsynthAlmPortIndex_Type.__name__ = "Integer32"
_Rm10010e40AlmsynthAlmPortIndex_Object = MibTableColumn
rm10010e40AlmsynthAlmPortIndex = _Rm10010e40AlmsynthAlmPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 3, 8, 1, 1),
    _Rm10010e40AlmsynthAlmPortIndex_Type()
)
rm10010e40AlmsynthAlmPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmsynthAlmPortIndex.setStatus("current")
_Rm10010e40AlmSfpAbsentPortn_Type = EkiOnOff
_Rm10010e40AlmSfpAbsentPortn_Object = MibTableColumn
rm10010e40AlmSfpAbsentPortn = _Rm10010e40AlmSfpAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 3, 8, 1, 2),
    _Rm10010e40AlmSfpAbsentPortn_Type()
)
rm10010e40AlmSfpAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmSfpAbsentPortn.setStatus("current")
_Rm10010e40AlmDdmAbsentPortn_Type = EkiOnOff
_Rm10010e40AlmDdmAbsentPortn_Object = MibTableColumn
rm10010e40AlmDdmAbsentPortn = _Rm10010e40AlmDdmAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 3, 8, 1, 3),
    _Rm10010e40AlmDdmAbsentPortn_Type()
)
rm10010e40AlmDdmAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmDdmAbsentPortn.setStatus("current")
_Rm10010e40AlmHwFailAccPortn_Type = EkiOnOff
_Rm10010e40AlmHwFailAccPortn_Object = MibTableColumn
rm10010e40AlmHwFailAccPortn = _Rm10010e40AlmHwFailAccPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 3, 8, 1, 5),
    _Rm10010e40AlmHwFailAccPortn_Type()
)
rm10010e40AlmHwFailAccPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmHwFailAccPortn.setStatus("current")
_Rm10010e40AlmDwLsdPortn_Type = EkiOnOff
_Rm10010e40AlmDwLsdPortn_Object = MibTableColumn
rm10010e40AlmDwLsdPortn = _Rm10010e40AlmDwLsdPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 3, 8, 1, 6),
    _Rm10010e40AlmDwLsdPortn_Type()
)
rm10010e40AlmDwLsdPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmDwLsdPortn.setStatus("current")
_Rm10010e40AlmClientLocalOosPortn_Type = EkiOnOff
_Rm10010e40AlmClientLocalOosPortn_Object = MibTableColumn
rm10010e40AlmClientLocalOosPortn = _Rm10010e40AlmClientLocalOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 3, 8, 1, 7),
    _Rm10010e40AlmClientLocalOosPortn_Type()
)
rm10010e40AlmClientLocalOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmClientLocalOosPortn.setStatus("current")
_Rm10010e40AlmClientRemoteOosPortn_Type = EkiOnOff
_Rm10010e40AlmClientRemoteOosPortn_Object = MibTableColumn
rm10010e40AlmClientRemoteOosPortn = _Rm10010e40AlmClientRemoteOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 3, 8, 1, 8),
    _Rm10010e40AlmClientRemoteOosPortn_Type()
)
rm10010e40AlmClientRemoteOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmClientRemoteOosPortn.setStatus("current")
_Rm10010e40AlmDwCaisPortn_Type = EkiOnOff
_Rm10010e40AlmDwCaisPortn_Object = MibTableColumn
rm10010e40AlmDwCaisPortn = _Rm10010e40AlmDwCaisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 3, 8, 1, 9),
    _Rm10010e40AlmDwCaisPortn_Type()
)
rm10010e40AlmDwCaisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmDwCaisPortn.setStatus("current")
_Rm10010e40AlmSfpDdmWarningPortn_Type = EkiOnOff
_Rm10010e40AlmSfpDdmWarningPortn_Object = MibTableColumn
rm10010e40AlmSfpDdmWarningPortn = _Rm10010e40AlmSfpDdmWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 3, 8, 1, 10),
    _Rm10010e40AlmSfpDdmWarningPortn_Type()
)
rm10010e40AlmSfpDdmWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmSfpDdmWarningPortn.setStatus("current")
_Rm10010e40AlmSfpDdmAlmPortn_Type = EkiOnOff
_Rm10010e40AlmSfpDdmAlmPortn_Object = MibTableColumn
rm10010e40AlmSfpDdmAlmPortn = _Rm10010e40AlmSfpDdmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 3, 8, 1, 11),
    _Rm10010e40AlmSfpDdmAlmPortn_Type()
)
rm10010e40AlmSfpDdmAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmSfpDdmAlmPortn.setStatus("current")
_Rm10010e40AlmFailAccPortn_Type = EkiOnOff
_Rm10010e40AlmFailAccPortn_Object = MibTableColumn
rm10010e40AlmFailAccPortn = _Rm10010e40AlmFailAccPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 3, 8, 1, 13),
    _Rm10010e40AlmFailAccPortn_Type()
)
rm10010e40AlmFailAccPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmFailAccPortn.setStatus("current")
_Rm10010e40AlmUpCsfPortn_Type = EkiOnOff
_Rm10010e40AlmUpCsfPortn_Object = MibTableColumn
rm10010e40AlmUpCsfPortn = _Rm10010e40AlmUpCsfPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 2, 3, 8, 1, 17),
    _Rm10010e40AlmUpCsfPortn_Type()
)
rm10010e40AlmUpCsfPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmUpCsfPortn.setStatus("current")
_Rm10010e40AlmLine_ObjectIdentity = ObjectIdentity
rm10010e40AlmLine = _Rm10010e40AlmLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3)
)
_Rm10010e40AlmLineNurg_ObjectIdentity = ObjectIdentity
rm10010e40AlmLineNurg = _Rm10010e40AlmLineNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 1)
)
_Rm10010e40AlmlineNetworkLaneAlarmWarning1Table_Object = MibTable
rm10010e40AlmlineNetworkLaneAlarmWarning1Table = _Rm10010e40AlmlineNetworkLaneAlarmWarning1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 1, 104)
)
if mibBuilder.loadTexts:
    rm10010e40AlmlineNetworkLaneAlarmWarning1Table.setStatus("current")
_Rm10010e40AlmlineNetworkLaneAlarmWarning1Entry_Object = MibTableRow
rm10010e40AlmlineNetworkLaneAlarmWarning1Entry = _Rm10010e40AlmlineNetworkLaneAlarmWarning1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 1, 104, 1)
)
rm10010e40AlmlineNetworkLaneAlarmWarning1Entry.setIndexNames(
    (0, "EKINOPS-Rm10010e40-MIB", "rm10010e40AlmlineNetworkLaneAlarmWarning1Index"),
)
if mibBuilder.loadTexts:
    rm10010e40AlmlineNetworkLaneAlarmWarning1Entry.setStatus("current")


class _Rm10010e40AlmlineNetworkLaneAlarmWarning1Index_Type(Integer32):
    """Custom type rm10010e40AlmlineNetworkLaneAlarmWarning1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010e40AlmlineNetworkLaneAlarmWarning1Index_Type.__name__ = "Integer32"
_Rm10010e40AlmlineNetworkLaneAlarmWarning1Index_Object = MibTableColumn
rm10010e40AlmlineNetworkLaneAlarmWarning1Index = _Rm10010e40AlmlineNetworkLaneAlarmWarning1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 1, 104, 1, 1),
    _Rm10010e40AlmlineNetworkLaneAlarmWarning1Index_Type()
)
rm10010e40AlmlineNetworkLaneAlarmWarning1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmlineNetworkLaneAlarmWarning1Index.setStatus("current")
_Rm10010e40AlmLineRxPowerLowAlarmPortn_Type = EkiOnOff
_Rm10010e40AlmLineRxPowerLowAlarmPortn_Object = MibTableColumn
rm10010e40AlmLineRxPowerLowAlarmPortn = _Rm10010e40AlmLineRxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 1, 104, 1, 2),
    _Rm10010e40AlmLineRxPowerLowAlarmPortn_Type()
)
rm10010e40AlmLineRxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmLineRxPowerLowAlarmPortn.setStatus("current")
_Rm10010e40AlmLineRxPowerLowWarningPortn_Type = EkiOnOff
_Rm10010e40AlmLineRxPowerLowWarningPortn_Object = MibTableColumn
rm10010e40AlmLineRxPowerLowWarningPortn = _Rm10010e40AlmLineRxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 1, 104, 1, 3),
    _Rm10010e40AlmLineRxPowerLowWarningPortn_Type()
)
rm10010e40AlmLineRxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmLineRxPowerLowWarningPortn.setStatus("current")
_Rm10010e40AlmLineRxPowerHighWarningPortn_Type = EkiOnOff
_Rm10010e40AlmLineRxPowerHighWarningPortn_Object = MibTableColumn
rm10010e40AlmLineRxPowerHighWarningPortn = _Rm10010e40AlmLineRxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 1, 104, 1, 4),
    _Rm10010e40AlmLineRxPowerHighWarningPortn_Type()
)
rm10010e40AlmLineRxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmLineRxPowerHighWarningPortn.setStatus("current")
_Rm10010e40AlmLineRxPowerHighAlarmPortn_Type = EkiOnOff
_Rm10010e40AlmLineRxPowerHighAlarmPortn_Object = MibTableColumn
rm10010e40AlmLineRxPowerHighAlarmPortn = _Rm10010e40AlmLineRxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 1, 104, 1, 5),
    _Rm10010e40AlmLineRxPowerHighAlarmPortn_Type()
)
rm10010e40AlmLineRxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmLineRxPowerHighAlarmPortn.setStatus("current")
_Rm10010e40AlmLineLaserTempLowAlarmPortn_Type = EkiOnOff
_Rm10010e40AlmLineLaserTempLowAlarmPortn_Object = MibTableColumn
rm10010e40AlmLineLaserTempLowAlarmPortn = _Rm10010e40AlmLineLaserTempLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 1, 104, 1, 6),
    _Rm10010e40AlmLineLaserTempLowAlarmPortn_Type()
)
rm10010e40AlmLineLaserTempLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmLineLaserTempLowAlarmPortn.setStatus("current")
_Rm10010e40AlmLineLaserTempLowWarningPortn_Type = EkiOnOff
_Rm10010e40AlmLineLaserTempLowWarningPortn_Object = MibTableColumn
rm10010e40AlmLineLaserTempLowWarningPortn = _Rm10010e40AlmLineLaserTempLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 1, 104, 1, 7),
    _Rm10010e40AlmLineLaserTempLowWarningPortn_Type()
)
rm10010e40AlmLineLaserTempLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmLineLaserTempLowWarningPortn.setStatus("current")
_Rm10010e40AlmLineLaserTempHighWarningPortn_Type = EkiOnOff
_Rm10010e40AlmLineLaserTempHighWarningPortn_Object = MibTableColumn
rm10010e40AlmLineLaserTempHighWarningPortn = _Rm10010e40AlmLineLaserTempHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 1, 104, 1, 8),
    _Rm10010e40AlmLineLaserTempHighWarningPortn_Type()
)
rm10010e40AlmLineLaserTempHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmLineLaserTempHighWarningPortn.setStatus("current")
_Rm10010e40AlmLineLaserTempHighAlarmPortn_Type = EkiOnOff
_Rm10010e40AlmLineLaserTempHighAlarmPortn_Object = MibTableColumn
rm10010e40AlmLineLaserTempHighAlarmPortn = _Rm10010e40AlmLineLaserTempHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 1, 104, 1, 9),
    _Rm10010e40AlmLineLaserTempHighAlarmPortn_Type()
)
rm10010e40AlmLineLaserTempHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmLineLaserTempHighAlarmPortn.setStatus("current")
_Rm10010e40AlmLineTxPowerLowAlarmPortn_Type = EkiOnOff
_Rm10010e40AlmLineTxPowerLowAlarmPortn_Object = MibTableColumn
rm10010e40AlmLineTxPowerLowAlarmPortn = _Rm10010e40AlmLineTxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 1, 104, 1, 10),
    _Rm10010e40AlmLineTxPowerLowAlarmPortn_Type()
)
rm10010e40AlmLineTxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmLineTxPowerLowAlarmPortn.setStatus("current")
_Rm10010e40AlmLineTxPowerLowWarningPortn_Type = EkiOnOff
_Rm10010e40AlmLineTxPowerLowWarningPortn_Object = MibTableColumn
rm10010e40AlmLineTxPowerLowWarningPortn = _Rm10010e40AlmLineTxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 1, 104, 1, 11),
    _Rm10010e40AlmLineTxPowerLowWarningPortn_Type()
)
rm10010e40AlmLineTxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmLineTxPowerLowWarningPortn.setStatus("current")
_Rm10010e40AlmLineTxPowerHighWarningPortn_Type = EkiOnOff
_Rm10010e40AlmLineTxPowerHighWarningPortn_Object = MibTableColumn
rm10010e40AlmLineTxPowerHighWarningPortn = _Rm10010e40AlmLineTxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 1, 104, 1, 12),
    _Rm10010e40AlmLineTxPowerHighWarningPortn_Type()
)
rm10010e40AlmLineTxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmLineTxPowerHighWarningPortn.setStatus("current")
_Rm10010e40AlmLineTxPowerHighAlarmPortn_Type = EkiOnOff
_Rm10010e40AlmLineTxPowerHighAlarmPortn_Object = MibTableColumn
rm10010e40AlmLineTxPowerHighAlarmPortn = _Rm10010e40AlmLineTxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 1, 104, 1, 13),
    _Rm10010e40AlmLineTxPowerHighAlarmPortn_Type()
)
rm10010e40AlmLineTxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmLineTxPowerHighAlarmPortn.setStatus("current")
_Rm10010e40AlmLineBiasLowAlarmPortn_Type = EkiOnOff
_Rm10010e40AlmLineBiasLowAlarmPortn_Object = MibTableColumn
rm10010e40AlmLineBiasLowAlarmPortn = _Rm10010e40AlmLineBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 1, 104, 1, 14),
    _Rm10010e40AlmLineBiasLowAlarmPortn_Type()
)
rm10010e40AlmLineBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmLineBiasLowAlarmPortn.setStatus("current")
_Rm10010e40AlmLineBiasLowWarningPortn_Type = EkiOnOff
_Rm10010e40AlmLineBiasLowWarningPortn_Object = MibTableColumn
rm10010e40AlmLineBiasLowWarningPortn = _Rm10010e40AlmLineBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 1, 104, 1, 15),
    _Rm10010e40AlmLineBiasLowWarningPortn_Type()
)
rm10010e40AlmLineBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmLineBiasLowWarningPortn.setStatus("current")
_Rm10010e40AlmLineBiasHighWarningPortn_Type = EkiOnOff
_Rm10010e40AlmLineBiasHighWarningPortn_Object = MibTableColumn
rm10010e40AlmLineBiasHighWarningPortn = _Rm10010e40AlmLineBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 1, 104, 1, 16),
    _Rm10010e40AlmLineBiasHighWarningPortn_Type()
)
rm10010e40AlmLineBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmLineBiasHighWarningPortn.setStatus("current")
_Rm10010e40AlmLineBiasHighAlarmPortn_Type = EkiOnOff
_Rm10010e40AlmLineBiasHighAlarmPortn_Object = MibTableColumn
rm10010e40AlmLineBiasHighAlarmPortn = _Rm10010e40AlmLineBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 1, 104, 1, 17),
    _Rm10010e40AlmLineBiasHighAlarmPortn_Type()
)
rm10010e40AlmLineBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmLineBiasHighAlarmPortn.setStatus("current")
_Rm10010e40AlmlineNetworkLaneAlarmWarning2Table_Object = MibTable
rm10010e40AlmlineNetworkLaneAlarmWarning2Table = _Rm10010e40AlmlineNetworkLaneAlarmWarning2Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 1, 120)
)
if mibBuilder.loadTexts:
    rm10010e40AlmlineNetworkLaneAlarmWarning2Table.setStatus("current")
_Rm10010e40AlmlineNetworkLaneAlarmWarning2Entry_Object = MibTableRow
rm10010e40AlmlineNetworkLaneAlarmWarning2Entry = _Rm10010e40AlmlineNetworkLaneAlarmWarning2Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 1, 120, 1)
)
rm10010e40AlmlineNetworkLaneAlarmWarning2Entry.setIndexNames(
    (0, "EKINOPS-Rm10010e40-MIB", "rm10010e40AlmlineNetworkLaneAlarmWarning2Index"),
)
if mibBuilder.loadTexts:
    rm10010e40AlmlineNetworkLaneAlarmWarning2Entry.setStatus("current")


class _Rm10010e40AlmlineNetworkLaneAlarmWarning2Index_Type(Integer32):
    """Custom type rm10010e40AlmlineNetworkLaneAlarmWarning2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010e40AlmlineNetworkLaneAlarmWarning2Index_Type.__name__ = "Integer32"
_Rm10010e40AlmlineNetworkLaneAlarmWarning2Index_Object = MibTableColumn
rm10010e40AlmlineNetworkLaneAlarmWarning2Index = _Rm10010e40AlmlineNetworkLaneAlarmWarning2Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 1, 120, 1, 1),
    _Rm10010e40AlmlineNetworkLaneAlarmWarning2Index_Type()
)
rm10010e40AlmlineNetworkLaneAlarmWarning2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmlineNetworkLaneAlarmWarning2Index.setStatus("current")
_Rm10010e40AlmTxModulatorBiasLowAlarmPortn_Type = EkiOnOff
_Rm10010e40AlmTxModulatorBiasLowAlarmPortn_Object = MibTableColumn
rm10010e40AlmTxModulatorBiasLowAlarmPortn = _Rm10010e40AlmTxModulatorBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 1, 120, 1, 2),
    _Rm10010e40AlmTxModulatorBiasLowAlarmPortn_Type()
)
rm10010e40AlmTxModulatorBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmTxModulatorBiasLowAlarmPortn.setStatus("current")
_Rm10010e40AlmTxModulatorBiasLowWarningPortn_Type = EkiOnOff
_Rm10010e40AlmTxModulatorBiasLowWarningPortn_Object = MibTableColumn
rm10010e40AlmTxModulatorBiasLowWarningPortn = _Rm10010e40AlmTxModulatorBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 1, 120, 1, 3),
    _Rm10010e40AlmTxModulatorBiasLowWarningPortn_Type()
)
rm10010e40AlmTxModulatorBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmTxModulatorBiasLowWarningPortn.setStatus("current")
_Rm10010e40AlmTxModulatorBiasHighWarningPortn_Type = EkiOnOff
_Rm10010e40AlmTxModulatorBiasHighWarningPortn_Object = MibTableColumn
rm10010e40AlmTxModulatorBiasHighWarningPortn = _Rm10010e40AlmTxModulatorBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 1, 120, 1, 4),
    _Rm10010e40AlmTxModulatorBiasHighWarningPortn_Type()
)
rm10010e40AlmTxModulatorBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmTxModulatorBiasHighWarningPortn.setStatus("current")
_Rm10010e40AlmTxModulatorBiasHighAlarmPortn_Type = EkiOnOff
_Rm10010e40AlmTxModulatorBiasHighAlarmPortn_Object = MibTableColumn
rm10010e40AlmTxModulatorBiasHighAlarmPortn = _Rm10010e40AlmTxModulatorBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 1, 120, 1, 5),
    _Rm10010e40AlmTxModulatorBiasHighAlarmPortn_Type()
)
rm10010e40AlmTxModulatorBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmTxModulatorBiasHighAlarmPortn.setStatus("current")
_Rm10010e40AlmRxLaserTempLowAlarmPortn_Type = EkiOnOff
_Rm10010e40AlmRxLaserTempLowAlarmPortn_Object = MibTableColumn
rm10010e40AlmRxLaserTempLowAlarmPortn = _Rm10010e40AlmRxLaserTempLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 1, 120, 1, 6),
    _Rm10010e40AlmRxLaserTempLowAlarmPortn_Type()
)
rm10010e40AlmRxLaserTempLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmRxLaserTempLowAlarmPortn.setStatus("current")
_Rm10010e40AlmRxLaserTempLowWarningPortn_Type = EkiOnOff
_Rm10010e40AlmRxLaserTempLowWarningPortn_Object = MibTableColumn
rm10010e40AlmRxLaserTempLowWarningPortn = _Rm10010e40AlmRxLaserTempLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 1, 120, 1, 7),
    _Rm10010e40AlmRxLaserTempLowWarningPortn_Type()
)
rm10010e40AlmRxLaserTempLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmRxLaserTempLowWarningPortn.setStatus("current")
_Rm10010e40AlmRxLaserTempHighWarningPortn_Type = EkiOnOff
_Rm10010e40AlmRxLaserTempHighWarningPortn_Object = MibTableColumn
rm10010e40AlmRxLaserTempHighWarningPortn = _Rm10010e40AlmRxLaserTempHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 1, 120, 1, 8),
    _Rm10010e40AlmRxLaserTempHighWarningPortn_Type()
)
rm10010e40AlmRxLaserTempHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmRxLaserTempHighWarningPortn.setStatus("current")
_Rm10010e40AlmRxLaserTempHighAlarmPortn_Type = EkiOnOff
_Rm10010e40AlmRxLaserTempHighAlarmPortn_Object = MibTableColumn
rm10010e40AlmRxLaserTempHighAlarmPortn = _Rm10010e40AlmRxLaserTempHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 1, 120, 1, 9),
    _Rm10010e40AlmRxLaserTempHighAlarmPortn_Type()
)
rm10010e40AlmRxLaserTempHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmRxLaserTempHighAlarmPortn.setStatus("current")
_Rm10010e40AlmRxLaserOutputLowAlarmPortn_Type = EkiOnOff
_Rm10010e40AlmRxLaserOutputLowAlarmPortn_Object = MibTableColumn
rm10010e40AlmRxLaserOutputLowAlarmPortn = _Rm10010e40AlmRxLaserOutputLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 1, 120, 1, 10),
    _Rm10010e40AlmRxLaserOutputLowAlarmPortn_Type()
)
rm10010e40AlmRxLaserOutputLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmRxLaserOutputLowAlarmPortn.setStatus("current")
_Rm10010e40AlmRxLaserOutputLowWarningPortn_Type = EkiOnOff
_Rm10010e40AlmRxLaserOutputLowWarningPortn_Object = MibTableColumn
rm10010e40AlmRxLaserOutputLowWarningPortn = _Rm10010e40AlmRxLaserOutputLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 1, 120, 1, 11),
    _Rm10010e40AlmRxLaserOutputLowWarningPortn_Type()
)
rm10010e40AlmRxLaserOutputLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmRxLaserOutputLowWarningPortn.setStatus("current")
_Rm10010e40AlmRxLaserOutputHighWarningPortn_Type = EkiOnOff
_Rm10010e40AlmRxLaserOutputHighWarningPortn_Object = MibTableColumn
rm10010e40AlmRxLaserOutputHighWarningPortn = _Rm10010e40AlmRxLaserOutputHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 1, 120, 1, 12),
    _Rm10010e40AlmRxLaserOutputHighWarningPortn_Type()
)
rm10010e40AlmRxLaserOutputHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmRxLaserOutputHighWarningPortn.setStatus("current")
_Rm10010e40AlmRxLaserOutputHighAlarmPortn_Type = EkiOnOff
_Rm10010e40AlmRxLaserOutputHighAlarmPortn_Object = MibTableColumn
rm10010e40AlmRxLaserOutputHighAlarmPortn = _Rm10010e40AlmRxLaserOutputHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 1, 120, 1, 13),
    _Rm10010e40AlmRxLaserOutputHighAlarmPortn_Type()
)
rm10010e40AlmRxLaserOutputHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmRxLaserOutputHighAlarmPortn.setStatus("current")
_Rm10010e40AlmRxLaserBiasLowAlarmPortn_Type = EkiOnOff
_Rm10010e40AlmRxLaserBiasLowAlarmPortn_Object = MibTableColumn
rm10010e40AlmRxLaserBiasLowAlarmPortn = _Rm10010e40AlmRxLaserBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 1, 120, 1, 14),
    _Rm10010e40AlmRxLaserBiasLowAlarmPortn_Type()
)
rm10010e40AlmRxLaserBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmRxLaserBiasLowAlarmPortn.setStatus("current")
_Rm10010e40AlmRxLaserBiasLowWarningPortn_Type = EkiOnOff
_Rm10010e40AlmRxLaserBiasLowWarningPortn_Object = MibTableColumn
rm10010e40AlmRxLaserBiasLowWarningPortn = _Rm10010e40AlmRxLaserBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 1, 120, 1, 15),
    _Rm10010e40AlmRxLaserBiasLowWarningPortn_Type()
)
rm10010e40AlmRxLaserBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmRxLaserBiasLowWarningPortn.setStatus("current")
_Rm10010e40AlmRxLaserBiasHighWarningPortn_Type = EkiOnOff
_Rm10010e40AlmRxLaserBiasHighWarningPortn_Object = MibTableColumn
rm10010e40AlmRxLaserBiasHighWarningPortn = _Rm10010e40AlmRxLaserBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 1, 120, 1, 16),
    _Rm10010e40AlmRxLaserBiasHighWarningPortn_Type()
)
rm10010e40AlmRxLaserBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmRxLaserBiasHighWarningPortn.setStatus("current")
_Rm10010e40AlmRxLaserBiasHighAlarmPortn_Type = EkiOnOff
_Rm10010e40AlmRxLaserBiasHighAlarmPortn_Object = MibTableColumn
rm10010e40AlmRxLaserBiasHighAlarmPortn = _Rm10010e40AlmRxLaserBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 1, 120, 1, 17),
    _Rm10010e40AlmRxLaserBiasHighAlarmPortn_Type()
)
rm10010e40AlmRxLaserBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmRxLaserBiasHighAlarmPortn.setStatus("current")
_Rm10010e40AlmLineUrg_ObjectIdentity = ObjectIdentity
rm10010e40AlmLineUrg = _Rm10010e40AlmLineUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 2)
)
_Rm10010e40AlmlineNetworkLaneFaultTable_Object = MibTable
rm10010e40AlmlineNetworkLaneFaultTable = _Rm10010e40AlmlineNetworkLaneFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 2, 136)
)
if mibBuilder.loadTexts:
    rm10010e40AlmlineNetworkLaneFaultTable.setStatus("current")
_Rm10010e40AlmlineNetworkLaneFaultEntry_Object = MibTableRow
rm10010e40AlmlineNetworkLaneFaultEntry = _Rm10010e40AlmlineNetworkLaneFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 2, 136, 1)
)
rm10010e40AlmlineNetworkLaneFaultEntry.setIndexNames(
    (0, "EKINOPS-Rm10010e40-MIB", "rm10010e40AlmlineNetworkLaneFaultIndex"),
)
if mibBuilder.loadTexts:
    rm10010e40AlmlineNetworkLaneFaultEntry.setStatus("current")


class _Rm10010e40AlmlineNetworkLaneFaultIndex_Type(Integer32):
    """Custom type rm10010e40AlmlineNetworkLaneFaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010e40AlmlineNetworkLaneFaultIndex_Type.__name__ = "Integer32"
_Rm10010e40AlmlineNetworkLaneFaultIndex_Object = MibTableColumn
rm10010e40AlmlineNetworkLaneFaultIndex = _Rm10010e40AlmlineNetworkLaneFaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 2, 136, 1, 1),
    _Rm10010e40AlmlineNetworkLaneFaultIndex_Type()
)
rm10010e40AlmlineNetworkLaneFaultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmlineNetworkLaneFaultIndex.setStatus("current")
_Rm10010e40AlmLineLaneRxTecFaultPortn_Type = EkiOnOff
_Rm10010e40AlmLineLaneRxTecFaultPortn_Object = MibTableColumn
rm10010e40AlmLineLaneRxTecFaultPortn = _Rm10010e40AlmLineLaneRxTecFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 2, 136, 1, 3),
    _Rm10010e40AlmLineLaneRxTecFaultPortn_Type()
)
rm10010e40AlmLineLaneRxTecFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmLineLaneRxTecFaultPortn.setStatus("current")
_Rm10010e40AlmLineLaneRxFifoErrorPortn_Type = EkiOnOff
_Rm10010e40AlmLineLaneRxFifoErrorPortn_Object = MibTableColumn
rm10010e40AlmLineLaneRxFifoErrorPortn = _Rm10010e40AlmLineLaneRxFifoErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 2, 136, 1, 4),
    _Rm10010e40AlmLineLaneRxFifoErrorPortn_Type()
)
rm10010e40AlmLineLaneRxFifoErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmLineLaneRxFifoErrorPortn.setStatus("current")
_Rm10010e40AlmLineLaneRxLolPortn_Type = EkiOnOff
_Rm10010e40AlmLineLaneRxLolPortn_Object = MibTableColumn
rm10010e40AlmLineLaneRxLolPortn = _Rm10010e40AlmLineLaneRxLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 2, 136, 1, 5),
    _Rm10010e40AlmLineLaneRxLolPortn_Type()
)
rm10010e40AlmLineLaneRxLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmLineLaneRxLolPortn.setStatus("current")
_Rm10010e40AlmLineLaneRxLosPortn_Type = EkiOnOff
_Rm10010e40AlmLineLaneRxLosPortn_Object = MibTableColumn
rm10010e40AlmLineLaneRxLosPortn = _Rm10010e40AlmLineLaneRxLosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 2, 136, 1, 6),
    _Rm10010e40AlmLineLaneRxLosPortn_Type()
)
rm10010e40AlmLineLaneRxLosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmLineLaneRxLosPortn.setStatus("current")
_Rm10010e40AlmLineLaneTxLolPortn_Type = EkiOnOff
_Rm10010e40AlmLineLaneTxLolPortn_Object = MibTableColumn
rm10010e40AlmLineLaneTxLolPortn = _Rm10010e40AlmLineLaneTxLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 2, 136, 1, 8),
    _Rm10010e40AlmLineLaneTxLolPortn_Type()
)
rm10010e40AlmLineLaneTxLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmLineLaneTxLolPortn.setStatus("current")
_Rm10010e40AlmLineLaneTxLosfPortn_Type = EkiOnOff
_Rm10010e40AlmLineLaneTxLosfPortn_Object = MibTableColumn
rm10010e40AlmLineLaneTxLosfPortn = _Rm10010e40AlmLineLaneTxLosfPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 2, 136, 1, 9),
    _Rm10010e40AlmLineLaneTxLosfPortn_Type()
)
rm10010e40AlmLineLaneTxLosfPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmLineLaneTxLosfPortn.setStatus("current")
_Rm10010e40AlmLineLaneApdPowerSupplyPortn_Type = EkiOnOff
_Rm10010e40AlmLineLaneApdPowerSupplyPortn_Object = MibTableColumn
rm10010e40AlmLineLaneApdPowerSupplyPortn = _Rm10010e40AlmLineLaneApdPowerSupplyPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 2, 136, 1, 15),
    _Rm10010e40AlmLineLaneApdPowerSupplyPortn_Type()
)
rm10010e40AlmLineLaneApdPowerSupplyPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmLineLaneApdPowerSupplyPortn.setStatus("current")
_Rm10010e40AlmLineLaneWavelengthUnlockedPortn_Type = EkiOnOff
_Rm10010e40AlmLineLaneWavelengthUnlockedPortn_Object = MibTableColumn
rm10010e40AlmLineLaneWavelengthUnlockedPortn = _Rm10010e40AlmLineLaneWavelengthUnlockedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 2, 136, 1, 16),
    _Rm10010e40AlmLineLaneWavelengthUnlockedPortn_Type()
)
rm10010e40AlmLineLaneWavelengthUnlockedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmLineLaneWavelengthUnlockedPortn.setStatus("current")
_Rm10010e40AlmLineLaneTecFaultPortn_Type = EkiOnOff
_Rm10010e40AlmLineLaneTecFaultPortn_Object = MibTableColumn
rm10010e40AlmLineLaneTecFaultPortn = _Rm10010e40AlmLineLaneTecFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 2, 136, 1, 17),
    _Rm10010e40AlmLineLaneTecFaultPortn_Type()
)
rm10010e40AlmLineLaneTecFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmLineLaneTecFaultPortn.setStatus("current")
_Rm10010e40AlmlineHostLaneFaultTable_Object = MibTable
rm10010e40AlmlineHostLaneFaultTable = _Rm10010e40AlmlineHostLaneFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 2, 152)
)
if mibBuilder.loadTexts:
    rm10010e40AlmlineHostLaneFaultTable.setStatus("current")
_Rm10010e40AlmlineHostLaneFaultEntry_Object = MibTableRow
rm10010e40AlmlineHostLaneFaultEntry = _Rm10010e40AlmlineHostLaneFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 2, 152, 1)
)
rm10010e40AlmlineHostLaneFaultEntry.setIndexNames(
    (0, "EKINOPS-Rm10010e40-MIB", "rm10010e40AlmlineHostLaneFaultIndex"),
)
if mibBuilder.loadTexts:
    rm10010e40AlmlineHostLaneFaultEntry.setStatus("current")


class _Rm10010e40AlmlineHostLaneFaultIndex_Type(Integer32):
    """Custom type rm10010e40AlmlineHostLaneFaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010e40AlmlineHostLaneFaultIndex_Type.__name__ = "Integer32"
_Rm10010e40AlmlineHostLaneFaultIndex_Object = MibTableColumn
rm10010e40AlmlineHostLaneFaultIndex = _Rm10010e40AlmlineHostLaneFaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 2, 152, 1, 1),
    _Rm10010e40AlmlineHostLaneFaultIndex_Type()
)
rm10010e40AlmlineHostLaneFaultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmlineHostLaneFaultIndex.setStatus("current")
_Rm10010e40AlmLineInputLossOfSignalPortn_Type = EkiOnOff
_Rm10010e40AlmLineInputLossOfSignalPortn_Object = MibTableColumn
rm10010e40AlmLineInputLossOfSignalPortn = _Rm10010e40AlmLineInputLossOfSignalPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 2, 152, 1, 2),
    _Rm10010e40AlmLineInputLossOfSignalPortn_Type()
)
rm10010e40AlmLineInputLossOfSignalPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmLineInputLossOfSignalPortn.setStatus("current")
_Rm10010e40AlmLineLossOfFramePortn_Type = EkiOnOff
_Rm10010e40AlmLineLossOfFramePortn_Object = MibTableColumn
rm10010e40AlmLineLossOfFramePortn = _Rm10010e40AlmLineLossOfFramePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 2, 152, 1, 3),
    _Rm10010e40AlmLineLossOfFramePortn_Type()
)
rm10010e40AlmLineLossOfFramePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmLineLossOfFramePortn.setStatus("current")
_Rm10010e40AlmLineSmBdiInsertedPortn_Type = EkiOnOff
_Rm10010e40AlmLineSmBdiInsertedPortn_Object = MibTableColumn
rm10010e40AlmLineSmBdiInsertedPortn = _Rm10010e40AlmLineSmBdiInsertedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 2, 152, 1, 4),
    _Rm10010e40AlmLineSmBdiInsertedPortn_Type()
)
rm10010e40AlmLineSmBdiInsertedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmLineSmBdiInsertedPortn.setStatus("current")
_Rm10010e40AlmLineSmBdiDetectedPortn_Type = EkiOnOff
_Rm10010e40AlmLineSmBdiDetectedPortn_Object = MibTableColumn
rm10010e40AlmLineSmBdiDetectedPortn = _Rm10010e40AlmLineSmBdiDetectedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 2, 152, 1, 5),
    _Rm10010e40AlmLineSmBdiDetectedPortn_Type()
)
rm10010e40AlmLineSmBdiDetectedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmLineSmBdiDetectedPortn.setStatus("current")
_Rm10010e40AlmLineSmIaeInsertedPortn_Type = EkiOnOff
_Rm10010e40AlmLineSmIaeInsertedPortn_Object = MibTableColumn
rm10010e40AlmLineSmIaeInsertedPortn = _Rm10010e40AlmLineSmIaeInsertedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 2, 152, 1, 6),
    _Rm10010e40AlmLineSmIaeInsertedPortn_Type()
)
rm10010e40AlmLineSmIaeInsertedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmLineSmIaeInsertedPortn.setStatus("current")
_Rm10010e40AlmLineSmIaeDetectedPortn_Type = EkiOnOff
_Rm10010e40AlmLineSmIaeDetectedPortn_Object = MibTableColumn
rm10010e40AlmLineSmIaeDetectedPortn = _Rm10010e40AlmLineSmIaeDetectedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 2, 152, 1, 7),
    _Rm10010e40AlmLineSmIaeDetectedPortn_Type()
)
rm10010e40AlmLineSmIaeDetectedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmLineSmIaeDetectedPortn.setStatus("current")
_Rm10010e40AlmLineTxHostLolPortn_Type = EkiOnOff
_Rm10010e40AlmLineTxHostLolPortn_Object = MibTableColumn
rm10010e40AlmLineTxHostLolPortn = _Rm10010e40AlmLineTxHostLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 2, 152, 1, 10),
    _Rm10010e40AlmLineTxHostLolPortn_Type()
)
rm10010e40AlmLineTxHostLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmLineTxHostLolPortn.setStatus("current")
_Rm10010e40AlmLineLaneTxFifoErrorPortn_Type = EkiOnOff
_Rm10010e40AlmLineLaneTxFifoErrorPortn_Object = MibTableColumn
rm10010e40AlmLineLaneTxFifoErrorPortn = _Rm10010e40AlmLineLaneTxFifoErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 2, 152, 1, 11),
    _Rm10010e40AlmLineLaneTxFifoErrorPortn_Type()
)
rm10010e40AlmLineLaneTxFifoErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmLineLaneTxFifoErrorPortn.setStatus("current")
_Rm10010e40AlmlineNetworkLaneRxOtnTable_Object = MibTable
rm10010e40AlmlineNetworkLaneRxOtnTable = _Rm10010e40AlmlineNetworkLaneRxOtnTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 2, 168)
)
if mibBuilder.loadTexts:
    rm10010e40AlmlineNetworkLaneRxOtnTable.setStatus("current")
_Rm10010e40AlmlineNetworkLaneRxOtnEntry_Object = MibTableRow
rm10010e40AlmlineNetworkLaneRxOtnEntry = _Rm10010e40AlmlineNetworkLaneRxOtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 2, 168, 1)
)
rm10010e40AlmlineNetworkLaneRxOtnEntry.setIndexNames(
    (0, "EKINOPS-Rm10010e40-MIB", "rm10010e40AlmlineNetworkLaneRxOtnIndex"),
)
if mibBuilder.loadTexts:
    rm10010e40AlmlineNetworkLaneRxOtnEntry.setStatus("current")


class _Rm10010e40AlmlineNetworkLaneRxOtnIndex_Type(Integer32):
    """Custom type rm10010e40AlmlineNetworkLaneRxOtnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010e40AlmlineNetworkLaneRxOtnIndex_Type.__name__ = "Integer32"
_Rm10010e40AlmlineNetworkLaneRxOtnIndex_Object = MibTableColumn
rm10010e40AlmlineNetworkLaneRxOtnIndex = _Rm10010e40AlmlineNetworkLaneRxOtnIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 2, 168, 1, 1),
    _Rm10010e40AlmlineNetworkLaneRxOtnIndex_Type()
)
rm10010e40AlmlineNetworkLaneRxOtnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmlineNetworkLaneRxOtnIndex.setStatus("current")
_Rm10010e40AlmLineRxOtnOduAisPortn_Type = EkiOnOff
_Rm10010e40AlmLineRxOtnOduAisPortn_Object = MibTableColumn
rm10010e40AlmLineRxOtnOduAisPortn = _Rm10010e40AlmLineRxOtnOduAisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 2, 168, 1, 10),
    _Rm10010e40AlmLineRxOtnOduAisPortn_Type()
)
rm10010e40AlmLineRxOtnOduAisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmLineRxOtnOduAisPortn.setStatus("current")
_Rm10010e40AlmLineRxOtnOtuAisPortn_Type = EkiOnOff
_Rm10010e40AlmLineRxOtnOtuAisPortn_Object = MibTableColumn
rm10010e40AlmLineRxOtnOtuAisPortn = _Rm10010e40AlmLineRxOtnOtuAisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 2, 168, 1, 11),
    _Rm10010e40AlmLineRxOtnOtuAisPortn_Type()
)
rm10010e40AlmLineRxOtnOtuAisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmLineRxOtnOtuAisPortn.setStatus("current")
_Rm10010e40AlmLineRxSmBdiPortn_Type = EkiOnOff
_Rm10010e40AlmLineRxSmBdiPortn_Object = MibTableColumn
rm10010e40AlmLineRxSmBdiPortn = _Rm10010e40AlmLineRxSmBdiPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 2, 168, 1, 12),
    _Rm10010e40AlmLineRxSmBdiPortn_Type()
)
rm10010e40AlmLineRxSmBdiPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmLineRxSmBdiPortn.setStatus("current")
_Rm10010e40AlmLineRxOtnIaePortn_Type = EkiOnOff
_Rm10010e40AlmLineRxOtnIaePortn_Object = MibTableColumn
rm10010e40AlmLineRxOtnIaePortn = _Rm10010e40AlmLineRxOtnIaePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 2, 168, 1, 13),
    _Rm10010e40AlmLineRxOtnIaePortn_Type()
)
rm10010e40AlmLineRxOtnIaePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmLineRxOtnIaePortn.setStatus("current")
_Rm10010e40AlmLineRxOtnOomPortn_Type = EkiOnOff
_Rm10010e40AlmLineRxOtnOomPortn_Object = MibTableColumn
rm10010e40AlmLineRxOtnOomPortn = _Rm10010e40AlmLineRxOtnOomPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 2, 168, 1, 14),
    _Rm10010e40AlmLineRxOtnOomPortn_Type()
)
rm10010e40AlmLineRxOtnOomPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmLineRxOtnOomPortn.setStatus("current")
_Rm10010e40AlmLineRxOtnLomPortn_Type = EkiOnOff
_Rm10010e40AlmLineRxOtnLomPortn_Object = MibTableColumn
rm10010e40AlmLineRxOtnLomPortn = _Rm10010e40AlmLineRxOtnLomPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 2, 168, 1, 15),
    _Rm10010e40AlmLineRxOtnLomPortn_Type()
)
rm10010e40AlmLineRxOtnLomPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmLineRxOtnLomPortn.setStatus("current")
_Rm10010e40AlmLineRxOtnOofPortn_Type = EkiOnOff
_Rm10010e40AlmLineRxOtnOofPortn_Object = MibTableColumn
rm10010e40AlmLineRxOtnOofPortn = _Rm10010e40AlmLineRxOtnOofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 2, 168, 1, 16),
    _Rm10010e40AlmLineRxOtnOofPortn_Type()
)
rm10010e40AlmLineRxOtnOofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmLineRxOtnOofPortn.setStatus("current")
_Rm10010e40AlmLineRxOtnLofPortn_Type = EkiOnOff
_Rm10010e40AlmLineRxOtnLofPortn_Object = MibTableColumn
rm10010e40AlmLineRxOtnLofPortn = _Rm10010e40AlmLineRxOtnLofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 2, 168, 1, 17),
    _Rm10010e40AlmLineRxOtnLofPortn_Type()
)
rm10010e40AlmLineRxOtnLofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmLineRxOtnLofPortn.setStatus("current")
_Rm10010e40AlmlineHostLaneTxOtnTable_Object = MibTable
rm10010e40AlmlineHostLaneTxOtnTable = _Rm10010e40AlmlineHostLaneTxOtnTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 2, 184)
)
if mibBuilder.loadTexts:
    rm10010e40AlmlineHostLaneTxOtnTable.setStatus("current")
_Rm10010e40AlmlineHostLaneTxOtnEntry_Object = MibTableRow
rm10010e40AlmlineHostLaneTxOtnEntry = _Rm10010e40AlmlineHostLaneTxOtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 2, 184, 1)
)
rm10010e40AlmlineHostLaneTxOtnEntry.setIndexNames(
    (0, "EKINOPS-Rm10010e40-MIB", "rm10010e40AlmlineHostLaneTxOtnIndex"),
)
if mibBuilder.loadTexts:
    rm10010e40AlmlineHostLaneTxOtnEntry.setStatus("current")


class _Rm10010e40AlmlineHostLaneTxOtnIndex_Type(Integer32):
    """Custom type rm10010e40AlmlineHostLaneTxOtnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010e40AlmlineHostLaneTxOtnIndex_Type.__name__ = "Integer32"
_Rm10010e40AlmlineHostLaneTxOtnIndex_Object = MibTableColumn
rm10010e40AlmlineHostLaneTxOtnIndex = _Rm10010e40AlmlineHostLaneTxOtnIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 2, 184, 1, 1),
    _Rm10010e40AlmlineHostLaneTxOtnIndex_Type()
)
rm10010e40AlmlineHostLaneTxOtnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmlineHostLaneTxOtnIndex.setStatus("current")
_Rm10010e40AlmLineTxOtnOduAisPortn_Type = EkiOnOff
_Rm10010e40AlmLineTxOtnOduAisPortn_Object = MibTableColumn
rm10010e40AlmLineTxOtnOduAisPortn = _Rm10010e40AlmLineTxOtnOduAisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 2, 184, 1, 10),
    _Rm10010e40AlmLineTxOtnOduAisPortn_Type()
)
rm10010e40AlmLineTxOtnOduAisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmLineTxOtnOduAisPortn.setStatus("current")
_Rm10010e40AlmLineTxOtnOtuAisPortn_Type = EkiOnOff
_Rm10010e40AlmLineTxOtnOtuAisPortn_Object = MibTableColumn
rm10010e40AlmLineTxOtnOtuAisPortn = _Rm10010e40AlmLineTxOtnOtuAisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 2, 184, 1, 11),
    _Rm10010e40AlmLineTxOtnOtuAisPortn_Type()
)
rm10010e40AlmLineTxOtnOtuAisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmLineTxOtnOtuAisPortn.setStatus("current")
_Rm10010e40AlmLineTxSmBdiPortn_Type = EkiOnOff
_Rm10010e40AlmLineTxSmBdiPortn_Object = MibTableColumn
rm10010e40AlmLineTxSmBdiPortn = _Rm10010e40AlmLineTxSmBdiPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 2, 184, 1, 12),
    _Rm10010e40AlmLineTxSmBdiPortn_Type()
)
rm10010e40AlmLineTxSmBdiPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmLineTxSmBdiPortn.setStatus("current")
_Rm10010e40AlmLineTxOtnIaePortn_Type = EkiOnOff
_Rm10010e40AlmLineTxOtnIaePortn_Object = MibTableColumn
rm10010e40AlmLineTxOtnIaePortn = _Rm10010e40AlmLineTxOtnIaePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 2, 184, 1, 13),
    _Rm10010e40AlmLineTxOtnIaePortn_Type()
)
rm10010e40AlmLineTxOtnIaePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmLineTxOtnIaePortn.setStatus("current")
_Rm10010e40AlmLineTxOtnOomPortn_Type = EkiOnOff
_Rm10010e40AlmLineTxOtnOomPortn_Object = MibTableColumn
rm10010e40AlmLineTxOtnOomPortn = _Rm10010e40AlmLineTxOtnOomPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 2, 184, 1, 14),
    _Rm10010e40AlmLineTxOtnOomPortn_Type()
)
rm10010e40AlmLineTxOtnOomPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmLineTxOtnOomPortn.setStatus("current")
_Rm10010e40AlmLineTxOtnLomPortn_Type = EkiOnOff
_Rm10010e40AlmLineTxOtnLomPortn_Object = MibTableColumn
rm10010e40AlmLineTxOtnLomPortn = _Rm10010e40AlmLineTxOtnLomPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 2, 184, 1, 15),
    _Rm10010e40AlmLineTxOtnLomPortn_Type()
)
rm10010e40AlmLineTxOtnLomPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmLineTxOtnLomPortn.setStatus("current")
_Rm10010e40AlmLineTxOtnOofPortn_Type = EkiOnOff
_Rm10010e40AlmLineTxOtnOofPortn_Object = MibTableColumn
rm10010e40AlmLineTxOtnOofPortn = _Rm10010e40AlmLineTxOtnOofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 2, 184, 1, 16),
    _Rm10010e40AlmLineTxOtnOofPortn_Type()
)
rm10010e40AlmLineTxOtnOofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmLineTxOtnOofPortn.setStatus("current")
_Rm10010e40AlmLineTxOtnLofPortn_Type = EkiOnOff
_Rm10010e40AlmLineTxOtnLofPortn_Object = MibTableColumn
rm10010e40AlmLineTxOtnLofPortn = _Rm10010e40AlmLineTxOtnLofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 2, 184, 1, 17),
    _Rm10010e40AlmLineTxOtnLofPortn_Type()
)
rm10010e40AlmLineTxOtnLofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmLineTxOtnLofPortn.setStatus("current")
_Rm10010e40AlmLineCrit_ObjectIdentity = ObjectIdentity
rm10010e40AlmLineCrit = _Rm10010e40AlmLineCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 3)
)
_Rm10010e40AlmsynthAlmLineTable_Object = MibTable
rm10010e40AlmsynthAlmLineTable = _Rm10010e40AlmsynthAlmLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 3, 24)
)
if mibBuilder.loadTexts:
    rm10010e40AlmsynthAlmLineTable.setStatus("current")
_Rm10010e40AlmsynthAlmLineEntry_Object = MibTableRow
rm10010e40AlmsynthAlmLineEntry = _Rm10010e40AlmsynthAlmLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 3, 24, 1)
)
rm10010e40AlmsynthAlmLineEntry.setIndexNames(
    (0, "EKINOPS-Rm10010e40-MIB", "rm10010e40AlmsynthAlmLineIndex"),
)
if mibBuilder.loadTexts:
    rm10010e40AlmsynthAlmLineEntry.setStatus("current")


class _Rm10010e40AlmsynthAlmLineIndex_Type(Integer32):
    """Custom type rm10010e40AlmsynthAlmLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010e40AlmsynthAlmLineIndex_Type.__name__ = "Integer32"
_Rm10010e40AlmsynthAlmLineIndex_Object = MibTableColumn
rm10010e40AlmsynthAlmLineIndex = _Rm10010e40AlmsynthAlmLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 3, 24, 1, 1),
    _Rm10010e40AlmsynthAlmLineIndex_Type()
)
rm10010e40AlmsynthAlmLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmsynthAlmLineIndex.setStatus("current")
_Rm10010e40AlmXfpAbsentPortn_Type = EkiOnOff
_Rm10010e40AlmXfpAbsentPortn_Object = MibTableColumn
rm10010e40AlmXfpAbsentPortn = _Rm10010e40AlmXfpAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 3, 24, 1, 2),
    _Rm10010e40AlmXfpAbsentPortn_Type()
)
rm10010e40AlmXfpAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmXfpAbsentPortn.setStatus("current")
_Rm10010e40AlmXfpInitNotComplPortn_Type = EkiOnOff
_Rm10010e40AlmXfpInitNotComplPortn_Object = MibTableColumn
rm10010e40AlmXfpInitNotComplPortn = _Rm10010e40AlmXfpInitNotComplPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 3, 24, 1, 3),
    _Rm10010e40AlmXfpInitNotComplPortn_Type()
)
rm10010e40AlmXfpInitNotComplPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmXfpInitNotComplPortn.setStatus("current")
_Rm10010e40AlmLineHwFailPortn_Type = EkiOnOff
_Rm10010e40AlmLineHwFailPortn_Object = MibTableColumn
rm10010e40AlmLineHwFailPortn = _Rm10010e40AlmLineHwFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 3, 24, 1, 5),
    _Rm10010e40AlmLineHwFailPortn_Type()
)
rm10010e40AlmLineHwFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmLineHwFailPortn.setStatus("current")
_Rm10010e40AlmXfpTxOffPortn_Type = EkiOnOff
_Rm10010e40AlmXfpTxOffPortn_Object = MibTableColumn
rm10010e40AlmXfpTxOffPortn = _Rm10010e40AlmXfpTxOffPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 3, 24, 1, 6),
    _Rm10010e40AlmXfpTxOffPortn_Type()
)
rm10010e40AlmXfpTxOffPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmXfpTxOffPortn.setStatus("current")
_Rm10010e40AlmLineLocalOosPortn_Type = EkiOnOff
_Rm10010e40AlmLineLocalOosPortn_Object = MibTableColumn
rm10010e40AlmLineLocalOosPortn = _Rm10010e40AlmLineLocalOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 3, 24, 1, 7),
    _Rm10010e40AlmLineLocalOosPortn_Type()
)
rm10010e40AlmLineLocalOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmLineLocalOosPortn.setStatus("current")
_Rm10010e40AlmUpRdiInsPortn_Type = EkiOnOff
_Rm10010e40AlmUpRdiInsPortn_Object = MibTableColumn
rm10010e40AlmUpRdiInsPortn = _Rm10010e40AlmUpRdiInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 3, 24, 1, 9),
    _Rm10010e40AlmUpRdiInsPortn_Type()
)
rm10010e40AlmUpRdiInsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmUpRdiInsPortn.setStatus("current")
_Rm10010e40AlmLineDdmWarningPortn_Type = EkiOnOff
_Rm10010e40AlmLineDdmWarningPortn_Object = MibTableColumn
rm10010e40AlmLineDdmWarningPortn = _Rm10010e40AlmLineDdmWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 3, 24, 1, 10),
    _Rm10010e40AlmLineDdmWarningPortn_Type()
)
rm10010e40AlmLineDdmWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmLineDdmWarningPortn.setStatus("current")
_Rm10010e40AlmLineDdmAlmPortn_Type = EkiOnOff
_Rm10010e40AlmLineDdmAlmPortn_Object = MibTableColumn
rm10010e40AlmLineDdmAlmPortn = _Rm10010e40AlmLineDdmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 3, 24, 1, 11),
    _Rm10010e40AlmLineDdmAlmPortn_Type()
)
rm10010e40AlmLineDdmAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmLineDdmAlmPortn.setStatus("current")
_Rm10010e40AlmLineFailPortn_Type = EkiOnOff
_Rm10010e40AlmLineFailPortn_Object = MibTableColumn
rm10010e40AlmLineFailPortn = _Rm10010e40AlmLineFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 3, 24, 1, 13),
    _Rm10010e40AlmLineFailPortn_Type()
)
rm10010e40AlmLineFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmLineFailPortn.setStatus("current")
_Rm10010e40AlmLineActivePortn_Type = EkiOnOff
_Rm10010e40AlmLineActivePortn_Object = MibTableColumn
rm10010e40AlmLineActivePortn = _Rm10010e40AlmLineActivePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 2, 3, 3, 24, 1, 17),
    _Rm10010e40AlmLineActivePortn_Type()
)
rm10010e40AlmLineActivePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40AlmLineActivePortn.setStatus("current")
_Rm10010e40measures_ObjectIdentity = ObjectIdentity
rm10010e40measures = _Rm10010e40measures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3)
)
_Rm10010e40MesrOther_ObjectIdentity = ObjectIdentity
rm10010e40MesrOther = _Rm10010e40MesrOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 1)
)
_Rm10010e40Mesrsynth0_Type = EkiMeasureType
_Rm10010e40Mesrsynth0_Object = MibScalar
rm10010e40Mesrsynth0 = _Rm10010e40Mesrsynth0_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 1, 0),
    _Rm10010e40Mesrsynth0_Type()
)
rm10010e40Mesrsynth0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40Mesrsynth0.setStatus("deprecated")
_Rm10010e40Mesrsynth1_Type = EkiMeasureType
_Rm10010e40Mesrsynth1_Object = MibScalar
rm10010e40Mesrsynth1 = _Rm10010e40Mesrsynth1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 1, 1),
    _Rm10010e40Mesrsynth1_Type()
)
rm10010e40Mesrsynth1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40Mesrsynth1.setStatus("deprecated")


class _Rm10010e40MesrpmIntervalNumber_Type(Unsigned32):
    """Custom type rm10010e40MesrpmIntervalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010e40MesrpmIntervalNumber_Type.__name__ = "Unsigned32"
_Rm10010e40MesrpmIntervalNumber_Object = MibScalar
rm10010e40MesrpmIntervalNumber = _Rm10010e40MesrpmIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 1, 7),
    _Rm10010e40MesrpmIntervalNumber_Type()
)
rm10010e40MesrpmIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrpmIntervalNumber.setStatus("current")


class _Rm10010e40MesrlineNetTxLaserOutputPwrAverage_Type(Unsigned32):
    """Custom type rm10010e40MesrlineNetTxLaserOutputPwrAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010e40MesrlineNetTxLaserOutputPwrAverage_Type.__name__ = "Unsigned32"
_Rm10010e40MesrlineNetTxLaserOutputPwrAverage_Object = MibScalar
rm10010e40MesrlineNetTxLaserOutputPwrAverage = _Rm10010e40MesrlineNetTxLaserOutputPwrAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 1, 180),
    _Rm10010e40MesrlineNetTxLaserOutputPwrAverage_Type()
)
rm10010e40MesrlineNetTxLaserOutputPwrAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrlineNetTxLaserOutputPwrAverage.setStatus("current")


class _Rm10010e40MesrlineNetTxLaserTempAverage_Type(Unsigned32):
    """Custom type rm10010e40MesrlineNetTxLaserTempAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010e40MesrlineNetTxLaserTempAverage_Type.__name__ = "Unsigned32"
_Rm10010e40MesrlineNetTxLaserTempAverage_Object = MibScalar
rm10010e40MesrlineNetTxLaserTempAverage = _Rm10010e40MesrlineNetTxLaserTempAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 1, 181),
    _Rm10010e40MesrlineNetTxLaserTempAverage_Type()
)
rm10010e40MesrlineNetTxLaserTempAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrlineNetTxLaserTempAverage.setStatus("current")


class _Rm10010e40MesrlineNetTxBiasCurrentAverage_Type(Unsigned32):
    """Custom type rm10010e40MesrlineNetTxBiasCurrentAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010e40MesrlineNetTxBiasCurrentAverage_Type.__name__ = "Unsigned32"
_Rm10010e40MesrlineNetTxBiasCurrentAverage_Object = MibScalar
rm10010e40MesrlineNetTxBiasCurrentAverage = _Rm10010e40MesrlineNetTxBiasCurrentAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 1, 182),
    _Rm10010e40MesrlineNetTxBiasCurrentAverage_Type()
)
rm10010e40MesrlineNetTxBiasCurrentAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrlineNetTxBiasCurrentAverage.setStatus("current")


class _Rm10010e40MesrlineNetRxInputPwrAverage_Type(Unsigned32):
    """Custom type rm10010e40MesrlineNetRxInputPwrAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010e40MesrlineNetRxInputPwrAverage_Type.__name__ = "Unsigned32"
_Rm10010e40MesrlineNetRxInputPwrAverage_Object = MibScalar
rm10010e40MesrlineNetRxInputPwrAverage = _Rm10010e40MesrlineNetRxInputPwrAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 1, 183),
    _Rm10010e40MesrlineNetRxInputPwrAverage_Type()
)
rm10010e40MesrlineNetRxInputPwrAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrlineNetRxInputPwrAverage.setStatus("current")


class _Rm10010e40MesrlineResidualChromaticDispAverage_Type(Unsigned32):
    """Custom type rm10010e40MesrlineResidualChromaticDispAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010e40MesrlineResidualChromaticDispAverage_Type.__name__ = "Unsigned32"
_Rm10010e40MesrlineResidualChromaticDispAverage_Object = MibScalar
rm10010e40MesrlineResidualChromaticDispAverage = _Rm10010e40MesrlineResidualChromaticDispAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 1, 184),
    _Rm10010e40MesrlineResidualChromaticDispAverage_Type()
)
rm10010e40MesrlineResidualChromaticDispAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrlineResidualChromaticDispAverage.setStatus("current")


class _Rm10010e40MesrlineDiffGroupDelayAverage_Type(Unsigned32):
    """Custom type rm10010e40MesrlineDiffGroupDelayAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010e40MesrlineDiffGroupDelayAverage_Type.__name__ = "Unsigned32"
_Rm10010e40MesrlineDiffGroupDelayAverage_Object = MibScalar
rm10010e40MesrlineDiffGroupDelayAverage = _Rm10010e40MesrlineDiffGroupDelayAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 1, 185),
    _Rm10010e40MesrlineDiffGroupDelayAverage_Type()
)
rm10010e40MesrlineDiffGroupDelayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrlineDiffGroupDelayAverage.setStatus("current")


class _Rm10010e40MesrlineQFactorAverage_Type(Unsigned32):
    """Custom type rm10010e40MesrlineQFactorAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010e40MesrlineQFactorAverage_Type.__name__ = "Unsigned32"
_Rm10010e40MesrlineQFactorAverage_Object = MibScalar
rm10010e40MesrlineQFactorAverage = _Rm10010e40MesrlineQFactorAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 1, 186),
    _Rm10010e40MesrlineQFactorAverage_Type()
)
rm10010e40MesrlineQFactorAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrlineQFactorAverage.setStatus("current")


class _Rm10010e40MesrlineCarrierFreqOffsetAverage_Type(Unsigned32):
    """Custom type rm10010e40MesrlineCarrierFreqOffsetAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010e40MesrlineCarrierFreqOffsetAverage_Type.__name__ = "Unsigned32"
_Rm10010e40MesrlineCarrierFreqOffsetAverage_Object = MibScalar
rm10010e40MesrlineCarrierFreqOffsetAverage = _Rm10010e40MesrlineCarrierFreqOffsetAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 1, 187),
    _Rm10010e40MesrlineCarrierFreqOffsetAverage_Type()
)
rm10010e40MesrlineCarrierFreqOffsetAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrlineCarrierFreqOffsetAverage.setStatus("current")


class _Rm10010e40MesrlineOsnrAverage_Type(Unsigned32):
    """Custom type rm10010e40MesrlineOsnrAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010e40MesrlineOsnrAverage_Type.__name__ = "Unsigned32"
_Rm10010e40MesrlineOsnrAverage_Object = MibScalar
rm10010e40MesrlineOsnrAverage = _Rm10010e40MesrlineOsnrAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 1, 188),
    _Rm10010e40MesrlineOsnrAverage_Type()
)
rm10010e40MesrlineOsnrAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrlineOsnrAverage.setStatus("current")


class _Rm10010e40MesrclientNetTxTempMin_Type(Unsigned32):
    """Custom type rm10010e40MesrclientNetTxTempMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010e40MesrclientNetTxTempMin_Type.__name__ = "Unsigned32"
_Rm10010e40MesrclientNetTxTempMin_Object = MibScalar
rm10010e40MesrclientNetTxTempMin = _Rm10010e40MesrclientNetTxTempMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 1, 192),
    _Rm10010e40MesrclientNetTxTempMin_Type()
)
rm10010e40MesrclientNetTxTempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrclientNetTxTempMin.setStatus("current")


class _Rm10010e40MesrclientNetTxBiasMin_Type(Unsigned32):
    """Custom type rm10010e40MesrclientNetTxBiasMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010e40MesrclientNetTxBiasMin_Type.__name__ = "Unsigned32"
_Rm10010e40MesrclientNetTxBiasMin_Object = MibScalar
rm10010e40MesrclientNetTxBiasMin = _Rm10010e40MesrclientNetTxBiasMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 1, 193),
    _Rm10010e40MesrclientNetTxBiasMin_Type()
)
rm10010e40MesrclientNetTxBiasMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrclientNetTxBiasMin.setStatus("current")


class _Rm10010e40MesrclientNetTxPwrMin_Type(Unsigned32):
    """Custom type rm10010e40MesrclientNetTxPwrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010e40MesrclientNetTxPwrMin_Type.__name__ = "Unsigned32"
_Rm10010e40MesrclientNetTxPwrMin_Object = MibScalar
rm10010e40MesrclientNetTxPwrMin = _Rm10010e40MesrclientNetTxPwrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 1, 194),
    _Rm10010e40MesrclientNetTxPwrMin_Type()
)
rm10010e40MesrclientNetTxPwrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrclientNetTxPwrMin.setStatus("current")


class _Rm10010e40MesrclientNetRxPwrMin_Type(Unsigned32):
    """Custom type rm10010e40MesrclientNetRxPwrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010e40MesrclientNetRxPwrMin_Type.__name__ = "Unsigned32"
_Rm10010e40MesrclientNetRxPwrMin_Object = MibScalar
rm10010e40MesrclientNetRxPwrMin = _Rm10010e40MesrclientNetRxPwrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 1, 195),
    _Rm10010e40MesrclientNetRxPwrMin_Type()
)
rm10010e40MesrclientNetRxPwrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrclientNetRxPwrMin.setStatus("current")


class _Rm10010e40MesrlineNetTxLaserOutputPwrMin_Type(Unsigned32):
    """Custom type rm10010e40MesrlineNetTxLaserOutputPwrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010e40MesrlineNetTxLaserOutputPwrMin_Type.__name__ = "Unsigned32"
_Rm10010e40MesrlineNetTxLaserOutputPwrMin_Object = MibScalar
rm10010e40MesrlineNetTxLaserOutputPwrMin = _Rm10010e40MesrlineNetTxLaserOutputPwrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 1, 196),
    _Rm10010e40MesrlineNetTxLaserOutputPwrMin_Type()
)
rm10010e40MesrlineNetTxLaserOutputPwrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrlineNetTxLaserOutputPwrMin.setStatus("current")


class _Rm10010e40MesrlineNetTxLaserTempMin_Type(Unsigned32):
    """Custom type rm10010e40MesrlineNetTxLaserTempMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010e40MesrlineNetTxLaserTempMin_Type.__name__ = "Unsigned32"
_Rm10010e40MesrlineNetTxLaserTempMin_Object = MibScalar
rm10010e40MesrlineNetTxLaserTempMin = _Rm10010e40MesrlineNetTxLaserTempMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 1, 197),
    _Rm10010e40MesrlineNetTxLaserTempMin_Type()
)
rm10010e40MesrlineNetTxLaserTempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrlineNetTxLaserTempMin.setStatus("current")


class _Rm10010e40MesrlineNetTxBiasCurrentMin_Type(Unsigned32):
    """Custom type rm10010e40MesrlineNetTxBiasCurrentMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010e40MesrlineNetTxBiasCurrentMin_Type.__name__ = "Unsigned32"
_Rm10010e40MesrlineNetTxBiasCurrentMin_Object = MibScalar
rm10010e40MesrlineNetTxBiasCurrentMin = _Rm10010e40MesrlineNetTxBiasCurrentMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 1, 198),
    _Rm10010e40MesrlineNetTxBiasCurrentMin_Type()
)
rm10010e40MesrlineNetTxBiasCurrentMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrlineNetTxBiasCurrentMin.setStatus("current")


class _Rm10010e40MesrlineNetRxInputPwrMin_Type(Unsigned32):
    """Custom type rm10010e40MesrlineNetRxInputPwrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010e40MesrlineNetRxInputPwrMin_Type.__name__ = "Unsigned32"
_Rm10010e40MesrlineNetRxInputPwrMin_Object = MibScalar
rm10010e40MesrlineNetRxInputPwrMin = _Rm10010e40MesrlineNetRxInputPwrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 1, 199),
    _Rm10010e40MesrlineNetRxInputPwrMin_Type()
)
rm10010e40MesrlineNetRxInputPwrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrlineNetRxInputPwrMin.setStatus("current")


class _Rm10010e40MesrlineResidualChromaticDispMin_Type(Unsigned32):
    """Custom type rm10010e40MesrlineResidualChromaticDispMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010e40MesrlineResidualChromaticDispMin_Type.__name__ = "Unsigned32"
_Rm10010e40MesrlineResidualChromaticDispMin_Object = MibScalar
rm10010e40MesrlineResidualChromaticDispMin = _Rm10010e40MesrlineResidualChromaticDispMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 1, 200),
    _Rm10010e40MesrlineResidualChromaticDispMin_Type()
)
rm10010e40MesrlineResidualChromaticDispMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrlineResidualChromaticDispMin.setStatus("current")


class _Rm10010e40MesrlineDiffGroupDelayMin_Type(Unsigned32):
    """Custom type rm10010e40MesrlineDiffGroupDelayMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010e40MesrlineDiffGroupDelayMin_Type.__name__ = "Unsigned32"
_Rm10010e40MesrlineDiffGroupDelayMin_Object = MibScalar
rm10010e40MesrlineDiffGroupDelayMin = _Rm10010e40MesrlineDiffGroupDelayMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 1, 201),
    _Rm10010e40MesrlineDiffGroupDelayMin_Type()
)
rm10010e40MesrlineDiffGroupDelayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrlineDiffGroupDelayMin.setStatus("current")


class _Rm10010e40MesrlineQFactorMin_Type(Unsigned32):
    """Custom type rm10010e40MesrlineQFactorMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010e40MesrlineQFactorMin_Type.__name__ = "Unsigned32"
_Rm10010e40MesrlineQFactorMin_Object = MibScalar
rm10010e40MesrlineQFactorMin = _Rm10010e40MesrlineQFactorMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 1, 202),
    _Rm10010e40MesrlineQFactorMin_Type()
)
rm10010e40MesrlineQFactorMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrlineQFactorMin.setStatus("current")


class _Rm10010e40MesrlineCarrierFreqOffsetMin_Type(Unsigned32):
    """Custom type rm10010e40MesrlineCarrierFreqOffsetMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010e40MesrlineCarrierFreqOffsetMin_Type.__name__ = "Unsigned32"
_Rm10010e40MesrlineCarrierFreqOffsetMin_Object = MibScalar
rm10010e40MesrlineCarrierFreqOffsetMin = _Rm10010e40MesrlineCarrierFreqOffsetMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 1, 203),
    _Rm10010e40MesrlineCarrierFreqOffsetMin_Type()
)
rm10010e40MesrlineCarrierFreqOffsetMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrlineCarrierFreqOffsetMin.setStatus("current")


class _Rm10010e40MesrlineOsnrMin_Type(Unsigned32):
    """Custom type rm10010e40MesrlineOsnrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010e40MesrlineOsnrMin_Type.__name__ = "Unsigned32"
_Rm10010e40MesrlineOsnrMin_Object = MibScalar
rm10010e40MesrlineOsnrMin = _Rm10010e40MesrlineOsnrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 1, 204),
    _Rm10010e40MesrlineOsnrMin_Type()
)
rm10010e40MesrlineOsnrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrlineOsnrMin.setStatus("current")


class _Rm10010e40MesrclientNetTxTempMax_Type(Unsigned32):
    """Custom type rm10010e40MesrclientNetTxTempMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010e40MesrclientNetTxTempMax_Type.__name__ = "Unsigned32"
_Rm10010e40MesrclientNetTxTempMax_Object = MibScalar
rm10010e40MesrclientNetTxTempMax = _Rm10010e40MesrclientNetTxTempMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 1, 208),
    _Rm10010e40MesrclientNetTxTempMax_Type()
)
rm10010e40MesrclientNetTxTempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrclientNetTxTempMax.setStatus("current")


class _Rm10010e40MesrclientNetTxBiasMax_Type(Unsigned32):
    """Custom type rm10010e40MesrclientNetTxBiasMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010e40MesrclientNetTxBiasMax_Type.__name__ = "Unsigned32"
_Rm10010e40MesrclientNetTxBiasMax_Object = MibScalar
rm10010e40MesrclientNetTxBiasMax = _Rm10010e40MesrclientNetTxBiasMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 1, 209),
    _Rm10010e40MesrclientNetTxBiasMax_Type()
)
rm10010e40MesrclientNetTxBiasMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrclientNetTxBiasMax.setStatus("current")


class _Rm10010e40MesrclientNetTxPwrMax_Type(Unsigned32):
    """Custom type rm10010e40MesrclientNetTxPwrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010e40MesrclientNetTxPwrMax_Type.__name__ = "Unsigned32"
_Rm10010e40MesrclientNetTxPwrMax_Object = MibScalar
rm10010e40MesrclientNetTxPwrMax = _Rm10010e40MesrclientNetTxPwrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 1, 210),
    _Rm10010e40MesrclientNetTxPwrMax_Type()
)
rm10010e40MesrclientNetTxPwrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrclientNetTxPwrMax.setStatus("current")


class _Rm10010e40MesrclientNetRxPwrMax_Type(Unsigned32):
    """Custom type rm10010e40MesrclientNetRxPwrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010e40MesrclientNetRxPwrMax_Type.__name__ = "Unsigned32"
_Rm10010e40MesrclientNetRxPwrMax_Object = MibScalar
rm10010e40MesrclientNetRxPwrMax = _Rm10010e40MesrclientNetRxPwrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 1, 211),
    _Rm10010e40MesrclientNetRxPwrMax_Type()
)
rm10010e40MesrclientNetRxPwrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrclientNetRxPwrMax.setStatus("current")


class _Rm10010e40MesrlineNetTxLaserOutputPwrMax_Type(Unsigned32):
    """Custom type rm10010e40MesrlineNetTxLaserOutputPwrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010e40MesrlineNetTxLaserOutputPwrMax_Type.__name__ = "Unsigned32"
_Rm10010e40MesrlineNetTxLaserOutputPwrMax_Object = MibScalar
rm10010e40MesrlineNetTxLaserOutputPwrMax = _Rm10010e40MesrlineNetTxLaserOutputPwrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 1, 212),
    _Rm10010e40MesrlineNetTxLaserOutputPwrMax_Type()
)
rm10010e40MesrlineNetTxLaserOutputPwrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrlineNetTxLaserOutputPwrMax.setStatus("current")


class _Rm10010e40MesrlineNetTxLaserTempMax_Type(Unsigned32):
    """Custom type rm10010e40MesrlineNetTxLaserTempMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010e40MesrlineNetTxLaserTempMax_Type.__name__ = "Unsigned32"
_Rm10010e40MesrlineNetTxLaserTempMax_Object = MibScalar
rm10010e40MesrlineNetTxLaserTempMax = _Rm10010e40MesrlineNetTxLaserTempMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 1, 213),
    _Rm10010e40MesrlineNetTxLaserTempMax_Type()
)
rm10010e40MesrlineNetTxLaserTempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrlineNetTxLaserTempMax.setStatus("current")


class _Rm10010e40MesrlineNetTxBiasCurrentMax_Type(Unsigned32):
    """Custom type rm10010e40MesrlineNetTxBiasCurrentMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010e40MesrlineNetTxBiasCurrentMax_Type.__name__ = "Unsigned32"
_Rm10010e40MesrlineNetTxBiasCurrentMax_Object = MibScalar
rm10010e40MesrlineNetTxBiasCurrentMax = _Rm10010e40MesrlineNetTxBiasCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 1, 214),
    _Rm10010e40MesrlineNetTxBiasCurrentMax_Type()
)
rm10010e40MesrlineNetTxBiasCurrentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrlineNetTxBiasCurrentMax.setStatus("current")


class _Rm10010e40MesrlineNetRxInputPwrMax_Type(Unsigned32):
    """Custom type rm10010e40MesrlineNetRxInputPwrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010e40MesrlineNetRxInputPwrMax_Type.__name__ = "Unsigned32"
_Rm10010e40MesrlineNetRxInputPwrMax_Object = MibScalar
rm10010e40MesrlineNetRxInputPwrMax = _Rm10010e40MesrlineNetRxInputPwrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 1, 215),
    _Rm10010e40MesrlineNetRxInputPwrMax_Type()
)
rm10010e40MesrlineNetRxInputPwrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrlineNetRxInputPwrMax.setStatus("current")


class _Rm10010e40MesrlineResidualChromaticDispMax_Type(Unsigned32):
    """Custom type rm10010e40MesrlineResidualChromaticDispMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010e40MesrlineResidualChromaticDispMax_Type.__name__ = "Unsigned32"
_Rm10010e40MesrlineResidualChromaticDispMax_Object = MibScalar
rm10010e40MesrlineResidualChromaticDispMax = _Rm10010e40MesrlineResidualChromaticDispMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 1, 216),
    _Rm10010e40MesrlineResidualChromaticDispMax_Type()
)
rm10010e40MesrlineResidualChromaticDispMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrlineResidualChromaticDispMax.setStatus("current")


class _Rm10010e40MesrlineDiffGroupDelayMax_Type(Unsigned32):
    """Custom type rm10010e40MesrlineDiffGroupDelayMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010e40MesrlineDiffGroupDelayMax_Type.__name__ = "Unsigned32"
_Rm10010e40MesrlineDiffGroupDelayMax_Object = MibScalar
rm10010e40MesrlineDiffGroupDelayMax = _Rm10010e40MesrlineDiffGroupDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 1, 217),
    _Rm10010e40MesrlineDiffGroupDelayMax_Type()
)
rm10010e40MesrlineDiffGroupDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrlineDiffGroupDelayMax.setStatus("current")


class _Rm10010e40MesrlineQFactorMax_Type(Unsigned32):
    """Custom type rm10010e40MesrlineQFactorMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010e40MesrlineQFactorMax_Type.__name__ = "Unsigned32"
_Rm10010e40MesrlineQFactorMax_Object = MibScalar
rm10010e40MesrlineQFactorMax = _Rm10010e40MesrlineQFactorMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 1, 218),
    _Rm10010e40MesrlineQFactorMax_Type()
)
rm10010e40MesrlineQFactorMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrlineQFactorMax.setStatus("current")


class _Rm10010e40MesrlineCarrierFreqOffsetMax_Type(Unsigned32):
    """Custom type rm10010e40MesrlineCarrierFreqOffsetMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010e40MesrlineCarrierFreqOffsetMax_Type.__name__ = "Unsigned32"
_Rm10010e40MesrlineCarrierFreqOffsetMax_Object = MibScalar
rm10010e40MesrlineCarrierFreqOffsetMax = _Rm10010e40MesrlineCarrierFreqOffsetMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 1, 219),
    _Rm10010e40MesrlineCarrierFreqOffsetMax_Type()
)
rm10010e40MesrlineCarrierFreqOffsetMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrlineCarrierFreqOffsetMax.setStatus("current")


class _Rm10010e40MesrlineOsnrMax_Type(Unsigned32):
    """Custom type rm10010e40MesrlineOsnrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010e40MesrlineOsnrMax_Type.__name__ = "Unsigned32"
_Rm10010e40MesrlineOsnrMax_Object = MibScalar
rm10010e40MesrlineOsnrMax = _Rm10010e40MesrlineOsnrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 1, 220),
    _Rm10010e40MesrlineOsnrMax_Type()
)
rm10010e40MesrlineOsnrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrlineOsnrMax.setStatus("current")
_Rm10010e40MesrClient_ObjectIdentity = ObjectIdentity
rm10010e40MesrClient = _Rm10010e40MesrClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 2)
)


class _Rm10010e40MesrclientCfpTemp_Type(Unsigned32):
    """Custom type rm10010e40MesrclientCfpTemp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010e40MesrclientCfpTemp_Type.__name__ = "Unsigned32"
_Rm10010e40MesrclientCfpTemp_Object = MibScalar
rm10010e40MesrclientCfpTemp = _Rm10010e40MesrclientCfpTemp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 2, 8),
    _Rm10010e40MesrclientCfpTemp_Type()
)
rm10010e40MesrclientCfpTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrclientCfpTemp.setStatus("current")


class _Rm10010e40MesrclientCfp3v3Voltage_Type(Unsigned32):
    """Custom type rm10010e40MesrclientCfp3v3Voltage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010e40MesrclientCfp3v3Voltage_Type.__name__ = "Unsigned32"
_Rm10010e40MesrclientCfp3v3Voltage_Object = MibScalar
rm10010e40MesrclientCfp3v3Voltage = _Rm10010e40MesrclientCfp3v3Voltage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 2, 9),
    _Rm10010e40MesrclientCfp3v3Voltage_Type()
)
rm10010e40MesrclientCfp3v3Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrclientCfp3v3Voltage.setStatus("current")


class _Rm10010e40MesrclientSoaBiasCurrent_Type(Unsigned32):
    """Custom type rm10010e40MesrclientSoaBiasCurrent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010e40MesrclientSoaBiasCurrent_Type.__name__ = "Unsigned32"
_Rm10010e40MesrclientSoaBiasCurrent_Object = MibScalar
rm10010e40MesrclientSoaBiasCurrent = _Rm10010e40MesrclientSoaBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 2, 10),
    _Rm10010e40MesrclientSoaBiasCurrent_Type()
)
rm10010e40MesrclientSoaBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrclientSoaBiasCurrent.setStatus("current")
_Rm10010e40MesrclientNetTxTempTable_Object = MibTable
rm10010e40MesrclientNetTxTempTable = _Rm10010e40MesrclientNetTxTempTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 2, 16)
)
if mibBuilder.loadTexts:
    rm10010e40MesrclientNetTxTempTable.setStatus("current")
_Rm10010e40MesrclientNetTxTempEntry_Object = MibTableRow
rm10010e40MesrclientNetTxTempEntry = _Rm10010e40MesrclientNetTxTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 2, 16, 1)
)
rm10010e40MesrclientNetTxTempEntry.setIndexNames(
    (0, "EKINOPS-Rm10010e40-MIB", "rm10010e40MesrclientNetTxTempIndex"),
)
if mibBuilder.loadTexts:
    rm10010e40MesrclientNetTxTempEntry.setStatus("current")


class _Rm10010e40MesrclientNetTxTempIndex_Type(Integer32):
    """Custom type rm10010e40MesrclientNetTxTempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010e40MesrclientNetTxTempIndex_Type.__name__ = "Integer32"
_Rm10010e40MesrclientNetTxTempIndex_Object = MibTableColumn
rm10010e40MesrclientNetTxTempIndex = _Rm10010e40MesrclientNetTxTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 2, 16, 1, 1),
    _Rm10010e40MesrclientNetTxTempIndex_Type()
)
rm10010e40MesrclientNetTxTempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrclientNetTxTempIndex.setStatus("current")


class _Rm10010e40MesrclientNetTxTempPortn_Type(Integer32):
    """Custom type rm10010e40MesrclientNetTxTempPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010e40MesrclientNetTxTempPortn_Type.__name__ = "Integer32"
_Rm10010e40MesrclientNetTxTempPortn_Object = MibTableColumn
rm10010e40MesrclientNetTxTempPortn = _Rm10010e40MesrclientNetTxTempPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 2, 16, 1, 2),
    _Rm10010e40MesrclientNetTxTempPortn_Type()
)
rm10010e40MesrclientNetTxTempPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrclientNetTxTempPortn.setStatus("current")
_Rm10010e40MesrclientNetTxBiasTable_Object = MibTable
rm10010e40MesrclientNetTxBiasTable = _Rm10010e40MesrclientNetTxBiasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 2, 32)
)
if mibBuilder.loadTexts:
    rm10010e40MesrclientNetTxBiasTable.setStatus("current")
_Rm10010e40MesrclientNetTxBiasEntry_Object = MibTableRow
rm10010e40MesrclientNetTxBiasEntry = _Rm10010e40MesrclientNetTxBiasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 2, 32, 1)
)
rm10010e40MesrclientNetTxBiasEntry.setIndexNames(
    (0, "EKINOPS-Rm10010e40-MIB", "rm10010e40MesrclientNetTxBiasIndex"),
)
if mibBuilder.loadTexts:
    rm10010e40MesrclientNetTxBiasEntry.setStatus("current")


class _Rm10010e40MesrclientNetTxBiasIndex_Type(Integer32):
    """Custom type rm10010e40MesrclientNetTxBiasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010e40MesrclientNetTxBiasIndex_Type.__name__ = "Integer32"
_Rm10010e40MesrclientNetTxBiasIndex_Object = MibTableColumn
rm10010e40MesrclientNetTxBiasIndex = _Rm10010e40MesrclientNetTxBiasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 2, 32, 1, 1),
    _Rm10010e40MesrclientNetTxBiasIndex_Type()
)
rm10010e40MesrclientNetTxBiasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrclientNetTxBiasIndex.setStatus("current")


class _Rm10010e40MesrclientNetTxBiasPortn_Type(Integer32):
    """Custom type rm10010e40MesrclientNetTxBiasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010e40MesrclientNetTxBiasPortn_Type.__name__ = "Integer32"
_Rm10010e40MesrclientNetTxBiasPortn_Object = MibTableColumn
rm10010e40MesrclientNetTxBiasPortn = _Rm10010e40MesrclientNetTxBiasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 2, 32, 1, 2),
    _Rm10010e40MesrclientNetTxBiasPortn_Type()
)
rm10010e40MesrclientNetTxBiasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrclientNetTxBiasPortn.setStatus("current")
_Rm10010e40MesrclientNetTxPwrTable_Object = MibTable
rm10010e40MesrclientNetTxPwrTable = _Rm10010e40MesrclientNetTxPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 2, 48)
)
if mibBuilder.loadTexts:
    rm10010e40MesrclientNetTxPwrTable.setStatus("current")
_Rm10010e40MesrclientNetTxPwrEntry_Object = MibTableRow
rm10010e40MesrclientNetTxPwrEntry = _Rm10010e40MesrclientNetTxPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 2, 48, 1)
)
rm10010e40MesrclientNetTxPwrEntry.setIndexNames(
    (0, "EKINOPS-Rm10010e40-MIB", "rm10010e40MesrclientNetTxPwrIndex"),
)
if mibBuilder.loadTexts:
    rm10010e40MesrclientNetTxPwrEntry.setStatus("current")


class _Rm10010e40MesrclientNetTxPwrIndex_Type(Integer32):
    """Custom type rm10010e40MesrclientNetTxPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010e40MesrclientNetTxPwrIndex_Type.__name__ = "Integer32"
_Rm10010e40MesrclientNetTxPwrIndex_Object = MibTableColumn
rm10010e40MesrclientNetTxPwrIndex = _Rm10010e40MesrclientNetTxPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 2, 48, 1, 1),
    _Rm10010e40MesrclientNetTxPwrIndex_Type()
)
rm10010e40MesrclientNetTxPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrclientNetTxPwrIndex.setStatus("current")


class _Rm10010e40MesrclientNetTxPwrPortn_Type(Integer32):
    """Custom type rm10010e40MesrclientNetTxPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010e40MesrclientNetTxPwrPortn_Type.__name__ = "Integer32"
_Rm10010e40MesrclientNetTxPwrPortn_Object = MibTableColumn
rm10010e40MesrclientNetTxPwrPortn = _Rm10010e40MesrclientNetTxPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 2, 48, 1, 2),
    _Rm10010e40MesrclientNetTxPwrPortn_Type()
)
rm10010e40MesrclientNetTxPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrclientNetTxPwrPortn.setStatus("current")
_Rm10010e40MesrclientNetRxPwrTable_Object = MibTable
rm10010e40MesrclientNetRxPwrTable = _Rm10010e40MesrclientNetRxPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 2, 64)
)
if mibBuilder.loadTexts:
    rm10010e40MesrclientNetRxPwrTable.setStatus("current")
_Rm10010e40MesrclientNetRxPwrEntry_Object = MibTableRow
rm10010e40MesrclientNetRxPwrEntry = _Rm10010e40MesrclientNetRxPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 2, 64, 1)
)
rm10010e40MesrclientNetRxPwrEntry.setIndexNames(
    (0, "EKINOPS-Rm10010e40-MIB", "rm10010e40MesrclientNetRxPwrIndex"),
)
if mibBuilder.loadTexts:
    rm10010e40MesrclientNetRxPwrEntry.setStatus("current")


class _Rm10010e40MesrclientNetRxPwrIndex_Type(Integer32):
    """Custom type rm10010e40MesrclientNetRxPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010e40MesrclientNetRxPwrIndex_Type.__name__ = "Integer32"
_Rm10010e40MesrclientNetRxPwrIndex_Object = MibTableColumn
rm10010e40MesrclientNetRxPwrIndex = _Rm10010e40MesrclientNetRxPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 2, 64, 1, 1),
    _Rm10010e40MesrclientNetRxPwrIndex_Type()
)
rm10010e40MesrclientNetRxPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrclientNetRxPwrIndex.setStatus("current")


class _Rm10010e40MesrclientNetRxPwrPortn_Type(Integer32):
    """Custom type rm10010e40MesrclientNetRxPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010e40MesrclientNetRxPwrPortn_Type.__name__ = "Integer32"
_Rm10010e40MesrclientNetRxPwrPortn_Object = MibTableColumn
rm10010e40MesrclientNetRxPwrPortn = _Rm10010e40MesrclientNetRxPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 2, 64, 1, 2),
    _Rm10010e40MesrclientNetRxPwrPortn_Type()
)
rm10010e40MesrclientNetRxPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrclientNetRxPwrPortn.setStatus("current")
_Rm10010e40MesrLine_ObjectIdentity = ObjectIdentity
rm10010e40MesrLine = _Rm10010e40MesrLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 3)
)


class _Rm10010e40MesrlineMsaTemp_Type(Unsigned32):
    """Custom type rm10010e40MesrlineMsaTemp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010e40MesrlineMsaTemp_Type.__name__ = "Unsigned32"
_Rm10010e40MesrlineMsaTemp_Object = MibScalar
rm10010e40MesrlineMsaTemp = _Rm10010e40MesrlineMsaTemp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 3, 12),
    _Rm10010e40MesrlineMsaTemp_Type()
)
rm10010e40MesrlineMsaTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrlineMsaTemp.setStatus("current")


class _Rm10010e40MesrlineMsa3v3Voltage_Type(Unsigned32):
    """Custom type rm10010e40MesrlineMsa3v3Voltage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010e40MesrlineMsa3v3Voltage_Type.__name__ = "Unsigned32"
_Rm10010e40MesrlineMsa3v3Voltage_Object = MibScalar
rm10010e40MesrlineMsa3v3Voltage = _Rm10010e40MesrlineMsa3v3Voltage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 3, 13),
    _Rm10010e40MesrlineMsa3v3Voltage_Type()
)
rm10010e40MesrlineMsa3v3Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrlineMsa3v3Voltage.setStatus("current")


class _Rm10010e40MesrlineSoaBiasCurrent_Type(Unsigned32):
    """Custom type rm10010e40MesrlineSoaBiasCurrent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010e40MesrlineSoaBiasCurrent_Type.__name__ = "Unsigned32"
_Rm10010e40MesrlineSoaBiasCurrent_Object = MibScalar
rm10010e40MesrlineSoaBiasCurrent = _Rm10010e40MesrlineSoaBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 3, 14),
    _Rm10010e40MesrlineSoaBiasCurrent_Type()
)
rm10010e40MesrlineSoaBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrlineSoaBiasCurrent.setStatus("current")
_Rm10010e40MesrlineNetTxLaserOutputPwrTable_Object = MibTable
rm10010e40MesrlineNetTxLaserOutputPwrTable = _Rm10010e40MesrlineNetTxLaserOutputPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 3, 80)
)
if mibBuilder.loadTexts:
    rm10010e40MesrlineNetTxLaserOutputPwrTable.setStatus("current")
_Rm10010e40MesrlineNetTxLaserOutputPwrEntry_Object = MibTableRow
rm10010e40MesrlineNetTxLaserOutputPwrEntry = _Rm10010e40MesrlineNetTxLaserOutputPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 3, 80, 1)
)
rm10010e40MesrlineNetTxLaserOutputPwrEntry.setIndexNames(
    (0, "EKINOPS-Rm10010e40-MIB", "rm10010e40MesrlineNetTxLaserOutputPwrIndex"),
)
if mibBuilder.loadTexts:
    rm10010e40MesrlineNetTxLaserOutputPwrEntry.setStatus("current")


class _Rm10010e40MesrlineNetTxLaserOutputPwrIndex_Type(Integer32):
    """Custom type rm10010e40MesrlineNetTxLaserOutputPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010e40MesrlineNetTxLaserOutputPwrIndex_Type.__name__ = "Integer32"
_Rm10010e40MesrlineNetTxLaserOutputPwrIndex_Object = MibTableColumn
rm10010e40MesrlineNetTxLaserOutputPwrIndex = _Rm10010e40MesrlineNetTxLaserOutputPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 3, 80, 1, 1),
    _Rm10010e40MesrlineNetTxLaserOutputPwrIndex_Type()
)
rm10010e40MesrlineNetTxLaserOutputPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrlineNetTxLaserOutputPwrIndex.setStatus("current")


class _Rm10010e40MesrlineNetTxLaserOutputPwrPortn_Type(Integer32):
    """Custom type rm10010e40MesrlineNetTxLaserOutputPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010e40MesrlineNetTxLaserOutputPwrPortn_Type.__name__ = "Integer32"
_Rm10010e40MesrlineNetTxLaserOutputPwrPortn_Object = MibTableColumn
rm10010e40MesrlineNetTxLaserOutputPwrPortn = _Rm10010e40MesrlineNetTxLaserOutputPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 3, 80, 1, 2),
    _Rm10010e40MesrlineNetTxLaserOutputPwrPortn_Type()
)
rm10010e40MesrlineNetTxLaserOutputPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrlineNetTxLaserOutputPwrPortn.setStatus("current")
_Rm10010e40MesrlineNetTxLaserTempTable_Object = MibTable
rm10010e40MesrlineNetTxLaserTempTable = _Rm10010e40MesrlineNetTxLaserTempTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 3, 96)
)
if mibBuilder.loadTexts:
    rm10010e40MesrlineNetTxLaserTempTable.setStatus("current")
_Rm10010e40MesrlineNetTxLaserTempEntry_Object = MibTableRow
rm10010e40MesrlineNetTxLaserTempEntry = _Rm10010e40MesrlineNetTxLaserTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 3, 96, 1)
)
rm10010e40MesrlineNetTxLaserTempEntry.setIndexNames(
    (0, "EKINOPS-Rm10010e40-MIB", "rm10010e40MesrlineNetTxLaserTempIndex"),
)
if mibBuilder.loadTexts:
    rm10010e40MesrlineNetTxLaserTempEntry.setStatus("current")


class _Rm10010e40MesrlineNetTxLaserTempIndex_Type(Integer32):
    """Custom type rm10010e40MesrlineNetTxLaserTempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010e40MesrlineNetTxLaserTempIndex_Type.__name__ = "Integer32"
_Rm10010e40MesrlineNetTxLaserTempIndex_Object = MibTableColumn
rm10010e40MesrlineNetTxLaserTempIndex = _Rm10010e40MesrlineNetTxLaserTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 3, 96, 1, 1),
    _Rm10010e40MesrlineNetTxLaserTempIndex_Type()
)
rm10010e40MesrlineNetTxLaserTempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrlineNetTxLaserTempIndex.setStatus("current")


class _Rm10010e40MesrlineNetTxLaserTempPortn_Type(Integer32):
    """Custom type rm10010e40MesrlineNetTxLaserTempPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010e40MesrlineNetTxLaserTempPortn_Type.__name__ = "Integer32"
_Rm10010e40MesrlineNetTxLaserTempPortn_Object = MibTableColumn
rm10010e40MesrlineNetTxLaserTempPortn = _Rm10010e40MesrlineNetTxLaserTempPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 3, 96, 1, 2),
    _Rm10010e40MesrlineNetTxLaserTempPortn_Type()
)
rm10010e40MesrlineNetTxLaserTempPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrlineNetTxLaserTempPortn.setStatus("current")
_Rm10010e40MesrlineNetTxBiasCurrentTable_Object = MibTable
rm10010e40MesrlineNetTxBiasCurrentTable = _Rm10010e40MesrlineNetTxBiasCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 3, 112)
)
if mibBuilder.loadTexts:
    rm10010e40MesrlineNetTxBiasCurrentTable.setStatus("current")
_Rm10010e40MesrlineNetTxBiasCurrentEntry_Object = MibTableRow
rm10010e40MesrlineNetTxBiasCurrentEntry = _Rm10010e40MesrlineNetTxBiasCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 3, 112, 1)
)
rm10010e40MesrlineNetTxBiasCurrentEntry.setIndexNames(
    (0, "EKINOPS-Rm10010e40-MIB", "rm10010e40MesrlineNetTxBiasCurrentIndex"),
)
if mibBuilder.loadTexts:
    rm10010e40MesrlineNetTxBiasCurrentEntry.setStatus("current")


class _Rm10010e40MesrlineNetTxBiasCurrentIndex_Type(Integer32):
    """Custom type rm10010e40MesrlineNetTxBiasCurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010e40MesrlineNetTxBiasCurrentIndex_Type.__name__ = "Integer32"
_Rm10010e40MesrlineNetTxBiasCurrentIndex_Object = MibTableColumn
rm10010e40MesrlineNetTxBiasCurrentIndex = _Rm10010e40MesrlineNetTxBiasCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 3, 112, 1, 1),
    _Rm10010e40MesrlineNetTxBiasCurrentIndex_Type()
)
rm10010e40MesrlineNetTxBiasCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrlineNetTxBiasCurrentIndex.setStatus("current")


class _Rm10010e40MesrlineNetTxBiasCurrentPortn_Type(Integer32):
    """Custom type rm10010e40MesrlineNetTxBiasCurrentPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010e40MesrlineNetTxBiasCurrentPortn_Type.__name__ = "Integer32"
_Rm10010e40MesrlineNetTxBiasCurrentPortn_Object = MibTableColumn
rm10010e40MesrlineNetTxBiasCurrentPortn = _Rm10010e40MesrlineNetTxBiasCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 3, 112, 1, 2),
    _Rm10010e40MesrlineNetTxBiasCurrentPortn_Type()
)
rm10010e40MesrlineNetTxBiasCurrentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrlineNetTxBiasCurrentPortn.setStatus("current")
_Rm10010e40MesrlineNetRxInputPwrTable_Object = MibTable
rm10010e40MesrlineNetRxInputPwrTable = _Rm10010e40MesrlineNetRxInputPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 3, 128)
)
if mibBuilder.loadTexts:
    rm10010e40MesrlineNetRxInputPwrTable.setStatus("current")
_Rm10010e40MesrlineNetRxInputPwrEntry_Object = MibTableRow
rm10010e40MesrlineNetRxInputPwrEntry = _Rm10010e40MesrlineNetRxInputPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 3, 128, 1)
)
rm10010e40MesrlineNetRxInputPwrEntry.setIndexNames(
    (0, "EKINOPS-Rm10010e40-MIB", "rm10010e40MesrlineNetRxInputPwrIndex"),
)
if mibBuilder.loadTexts:
    rm10010e40MesrlineNetRxInputPwrEntry.setStatus("current")


class _Rm10010e40MesrlineNetRxInputPwrIndex_Type(Integer32):
    """Custom type rm10010e40MesrlineNetRxInputPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010e40MesrlineNetRxInputPwrIndex_Type.__name__ = "Integer32"
_Rm10010e40MesrlineNetRxInputPwrIndex_Object = MibTableColumn
rm10010e40MesrlineNetRxInputPwrIndex = _Rm10010e40MesrlineNetRxInputPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 3, 128, 1, 1),
    _Rm10010e40MesrlineNetRxInputPwrIndex_Type()
)
rm10010e40MesrlineNetRxInputPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrlineNetRxInputPwrIndex.setStatus("current")


class _Rm10010e40MesrlineNetRxInputPwrPortn_Type(Integer32):
    """Custom type rm10010e40MesrlineNetRxInputPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010e40MesrlineNetRxInputPwrPortn_Type.__name__ = "Integer32"
_Rm10010e40MesrlineNetRxInputPwrPortn_Object = MibTableColumn
rm10010e40MesrlineNetRxInputPwrPortn = _Rm10010e40MesrlineNetRxInputPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 3, 128, 1, 2),
    _Rm10010e40MesrlineNetRxInputPwrPortn_Type()
)
rm10010e40MesrlineNetRxInputPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrlineNetRxInputPwrPortn.setStatus("current")
_Rm10010e40MesrlineResidualChromaticDispTable_Object = MibTable
rm10010e40MesrlineResidualChromaticDispTable = _Rm10010e40MesrlineResidualChromaticDispTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 3, 144)
)
if mibBuilder.loadTexts:
    rm10010e40MesrlineResidualChromaticDispTable.setStatus("current")
_Rm10010e40MesrlineResidualChromaticDispEntry_Object = MibTableRow
rm10010e40MesrlineResidualChromaticDispEntry = _Rm10010e40MesrlineResidualChromaticDispEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 3, 144, 1)
)
rm10010e40MesrlineResidualChromaticDispEntry.setIndexNames(
    (0, "EKINOPS-Rm10010e40-MIB", "rm10010e40MesrlineResidualChromaticDispIndex"),
)
if mibBuilder.loadTexts:
    rm10010e40MesrlineResidualChromaticDispEntry.setStatus("current")


class _Rm10010e40MesrlineResidualChromaticDispIndex_Type(Integer32):
    """Custom type rm10010e40MesrlineResidualChromaticDispIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010e40MesrlineResidualChromaticDispIndex_Type.__name__ = "Integer32"
_Rm10010e40MesrlineResidualChromaticDispIndex_Object = MibTableColumn
rm10010e40MesrlineResidualChromaticDispIndex = _Rm10010e40MesrlineResidualChromaticDispIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 3, 144, 1, 1),
    _Rm10010e40MesrlineResidualChromaticDispIndex_Type()
)
rm10010e40MesrlineResidualChromaticDispIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrlineResidualChromaticDispIndex.setStatus("current")


class _Rm10010e40MesrlineResidualChromaticDispPortn_Type(Integer32):
    """Custom type rm10010e40MesrlineResidualChromaticDispPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010e40MesrlineResidualChromaticDispPortn_Type.__name__ = "Integer32"
_Rm10010e40MesrlineResidualChromaticDispPortn_Object = MibTableColumn
rm10010e40MesrlineResidualChromaticDispPortn = _Rm10010e40MesrlineResidualChromaticDispPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 3, 144, 1, 2),
    _Rm10010e40MesrlineResidualChromaticDispPortn_Type()
)
rm10010e40MesrlineResidualChromaticDispPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrlineResidualChromaticDispPortn.setStatus("current")
_Rm10010e40MesrlineDiffGroupDelayTable_Object = MibTable
rm10010e40MesrlineDiffGroupDelayTable = _Rm10010e40MesrlineDiffGroupDelayTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 3, 148)
)
if mibBuilder.loadTexts:
    rm10010e40MesrlineDiffGroupDelayTable.setStatus("current")
_Rm10010e40MesrlineDiffGroupDelayEntry_Object = MibTableRow
rm10010e40MesrlineDiffGroupDelayEntry = _Rm10010e40MesrlineDiffGroupDelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 3, 148, 1)
)
rm10010e40MesrlineDiffGroupDelayEntry.setIndexNames(
    (0, "EKINOPS-Rm10010e40-MIB", "rm10010e40MesrlineDiffGroupDelayIndex"),
)
if mibBuilder.loadTexts:
    rm10010e40MesrlineDiffGroupDelayEntry.setStatus("current")


class _Rm10010e40MesrlineDiffGroupDelayIndex_Type(Integer32):
    """Custom type rm10010e40MesrlineDiffGroupDelayIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010e40MesrlineDiffGroupDelayIndex_Type.__name__ = "Integer32"
_Rm10010e40MesrlineDiffGroupDelayIndex_Object = MibTableColumn
rm10010e40MesrlineDiffGroupDelayIndex = _Rm10010e40MesrlineDiffGroupDelayIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 3, 148, 1, 1),
    _Rm10010e40MesrlineDiffGroupDelayIndex_Type()
)
rm10010e40MesrlineDiffGroupDelayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrlineDiffGroupDelayIndex.setStatus("current")


class _Rm10010e40MesrlineDiffGroupDelayPortn_Type(Integer32):
    """Custom type rm10010e40MesrlineDiffGroupDelayPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010e40MesrlineDiffGroupDelayPortn_Type.__name__ = "Integer32"
_Rm10010e40MesrlineDiffGroupDelayPortn_Object = MibTableColumn
rm10010e40MesrlineDiffGroupDelayPortn = _Rm10010e40MesrlineDiffGroupDelayPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 3, 148, 1, 2),
    _Rm10010e40MesrlineDiffGroupDelayPortn_Type()
)
rm10010e40MesrlineDiffGroupDelayPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrlineDiffGroupDelayPortn.setStatus("current")
_Rm10010e40MesrlineQFactorTable_Object = MibTable
rm10010e40MesrlineQFactorTable = _Rm10010e40MesrlineQFactorTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 3, 152)
)
if mibBuilder.loadTexts:
    rm10010e40MesrlineQFactorTable.setStatus("current")
_Rm10010e40MesrlineQFactorEntry_Object = MibTableRow
rm10010e40MesrlineQFactorEntry = _Rm10010e40MesrlineQFactorEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 3, 152, 1)
)
rm10010e40MesrlineQFactorEntry.setIndexNames(
    (0, "EKINOPS-Rm10010e40-MIB", "rm10010e40MesrlineQFactorIndex"),
)
if mibBuilder.loadTexts:
    rm10010e40MesrlineQFactorEntry.setStatus("current")


class _Rm10010e40MesrlineQFactorIndex_Type(Integer32):
    """Custom type rm10010e40MesrlineQFactorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010e40MesrlineQFactorIndex_Type.__name__ = "Integer32"
_Rm10010e40MesrlineQFactorIndex_Object = MibTableColumn
rm10010e40MesrlineQFactorIndex = _Rm10010e40MesrlineQFactorIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 3, 152, 1, 1),
    _Rm10010e40MesrlineQFactorIndex_Type()
)
rm10010e40MesrlineQFactorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrlineQFactorIndex.setStatus("current")


class _Rm10010e40MesrlineQFactorPortn_Type(Integer32):
    """Custom type rm10010e40MesrlineQFactorPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010e40MesrlineQFactorPortn_Type.__name__ = "Integer32"
_Rm10010e40MesrlineQFactorPortn_Object = MibTableColumn
rm10010e40MesrlineQFactorPortn = _Rm10010e40MesrlineQFactorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 3, 152, 1, 2),
    _Rm10010e40MesrlineQFactorPortn_Type()
)
rm10010e40MesrlineQFactorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrlineQFactorPortn.setStatus("current")
_Rm10010e40MesrlineCarrierFreqOffsetTable_Object = MibTable
rm10010e40MesrlineCarrierFreqOffsetTable = _Rm10010e40MesrlineCarrierFreqOffsetTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 3, 156)
)
if mibBuilder.loadTexts:
    rm10010e40MesrlineCarrierFreqOffsetTable.setStatus("current")
_Rm10010e40MesrlineCarrierFreqOffsetEntry_Object = MibTableRow
rm10010e40MesrlineCarrierFreqOffsetEntry = _Rm10010e40MesrlineCarrierFreqOffsetEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 3, 156, 1)
)
rm10010e40MesrlineCarrierFreqOffsetEntry.setIndexNames(
    (0, "EKINOPS-Rm10010e40-MIB", "rm10010e40MesrlineCarrierFreqOffsetIndex"),
)
if mibBuilder.loadTexts:
    rm10010e40MesrlineCarrierFreqOffsetEntry.setStatus("current")


class _Rm10010e40MesrlineCarrierFreqOffsetIndex_Type(Integer32):
    """Custom type rm10010e40MesrlineCarrierFreqOffsetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010e40MesrlineCarrierFreqOffsetIndex_Type.__name__ = "Integer32"
_Rm10010e40MesrlineCarrierFreqOffsetIndex_Object = MibTableColumn
rm10010e40MesrlineCarrierFreqOffsetIndex = _Rm10010e40MesrlineCarrierFreqOffsetIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 3, 156, 1, 1),
    _Rm10010e40MesrlineCarrierFreqOffsetIndex_Type()
)
rm10010e40MesrlineCarrierFreqOffsetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrlineCarrierFreqOffsetIndex.setStatus("current")


class _Rm10010e40MesrlineCarrierFreqOffsetPortn_Type(Integer32):
    """Custom type rm10010e40MesrlineCarrierFreqOffsetPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010e40MesrlineCarrierFreqOffsetPortn_Type.__name__ = "Integer32"
_Rm10010e40MesrlineCarrierFreqOffsetPortn_Object = MibTableColumn
rm10010e40MesrlineCarrierFreqOffsetPortn = _Rm10010e40MesrlineCarrierFreqOffsetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 3, 156, 1, 2),
    _Rm10010e40MesrlineCarrierFreqOffsetPortn_Type()
)
rm10010e40MesrlineCarrierFreqOffsetPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrlineCarrierFreqOffsetPortn.setStatus("current")
_Rm10010e40MesrlineOsnrTable_Object = MibTable
rm10010e40MesrlineOsnrTable = _Rm10010e40MesrlineOsnrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 3, 160)
)
if mibBuilder.loadTexts:
    rm10010e40MesrlineOsnrTable.setStatus("current")
_Rm10010e40MesrlineOsnrEntry_Object = MibTableRow
rm10010e40MesrlineOsnrEntry = _Rm10010e40MesrlineOsnrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 3, 160, 1)
)
rm10010e40MesrlineOsnrEntry.setIndexNames(
    (0, "EKINOPS-Rm10010e40-MIB", "rm10010e40MesrlineOsnrIndex"),
)
if mibBuilder.loadTexts:
    rm10010e40MesrlineOsnrEntry.setStatus("current")


class _Rm10010e40MesrlineOsnrIndex_Type(Integer32):
    """Custom type rm10010e40MesrlineOsnrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010e40MesrlineOsnrIndex_Type.__name__ = "Integer32"
_Rm10010e40MesrlineOsnrIndex_Object = MibTableColumn
rm10010e40MesrlineOsnrIndex = _Rm10010e40MesrlineOsnrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 3, 160, 1, 1),
    _Rm10010e40MesrlineOsnrIndex_Type()
)
rm10010e40MesrlineOsnrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrlineOsnrIndex.setStatus("current")


class _Rm10010e40MesrlineOsnrPortn_Type(Integer32):
    """Custom type rm10010e40MesrlineOsnrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010e40MesrlineOsnrPortn_Type.__name__ = "Integer32"
_Rm10010e40MesrlineOsnrPortn_Object = MibTableColumn
rm10010e40MesrlineOsnrPortn = _Rm10010e40MesrlineOsnrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 3, 3, 160, 1, 2),
    _Rm10010e40MesrlineOsnrPortn_Type()
)
rm10010e40MesrlineOsnrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MesrlineOsnrPortn.setStatus("current")
_Rm10010e40counters_ObjectIdentity = ObjectIdentity
rm10010e40counters = _Rm10010e40counters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4)
)
_Rm10010e40CntOther_ObjectIdentity = ObjectIdentity
rm10010e40CntOther = _Rm10010e40CntOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4, 1)
)
_Rm10010e40CntClient_ObjectIdentity = ObjectIdentity
rm10010e40CntClient = _Rm10010e40CntClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4, 2)
)
_Rm10010e40CntclientInputErrorCounterLaneOneTable_Object = MibTable
rm10010e40CntclientInputErrorCounterLaneOneTable = _Rm10010e40CntclientInputErrorCounterLaneOneTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4, 2, 16)
)
if mibBuilder.loadTexts:
    rm10010e40CntclientInputErrorCounterLaneOneTable.setStatus("current")
_Rm10010e40CntclientInputErrorCounterLaneOneEntry_Object = MibTableRow
rm10010e40CntclientInputErrorCounterLaneOneEntry = _Rm10010e40CntclientInputErrorCounterLaneOneEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4, 2, 16, 1)
)
rm10010e40CntclientInputErrorCounterLaneOneEntry.setIndexNames(
    (0, "EKINOPS-Rm10010e40-MIB", "rm10010e40CntclientInputErrorCounterLaneOneIndex"),
)
if mibBuilder.loadTexts:
    rm10010e40CntclientInputErrorCounterLaneOneEntry.setStatus("current")


class _Rm10010e40CntclientInputErrorCounterLaneOneIndex_Type(Integer32):
    """Custom type rm10010e40CntclientInputErrorCounterLaneOneIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010e40CntclientInputErrorCounterLaneOneIndex_Type.__name__ = "Integer32"
_Rm10010e40CntclientInputErrorCounterLaneOneIndex_Object = MibTableColumn
rm10010e40CntclientInputErrorCounterLaneOneIndex = _Rm10010e40CntclientInputErrorCounterLaneOneIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4, 2, 16, 1, 1),
    _Rm10010e40CntclientInputErrorCounterLaneOneIndex_Type()
)
rm10010e40CntclientInputErrorCounterLaneOneIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CntclientInputErrorCounterLaneOneIndex.setStatus("current")
_Rm10010e40CntclientInputErrorCounterLaneOneValuePortn_Type = Counter32
_Rm10010e40CntclientInputErrorCounterLaneOneValuePortn_Object = MibTableColumn
rm10010e40CntclientInputErrorCounterLaneOneValuePortn = _Rm10010e40CntclientInputErrorCounterLaneOneValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4, 2, 16, 1, 2),
    _Rm10010e40CntclientInputErrorCounterLaneOneValuePortn_Type()
)
rm10010e40CntclientInputErrorCounterLaneOneValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CntclientInputErrorCounterLaneOneValuePortn.setStatus("current")
_Rm10010e40CntclientInputErrorCounterLaneOneErrorPortn_Type = EkiOnOff
_Rm10010e40CntclientInputErrorCounterLaneOneErrorPortn_Object = MibTableColumn
rm10010e40CntclientInputErrorCounterLaneOneErrorPortn = _Rm10010e40CntclientInputErrorCounterLaneOneErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4, 2, 16, 1, 3),
    _Rm10010e40CntclientInputErrorCounterLaneOneErrorPortn_Type()
)
rm10010e40CntclientInputErrorCounterLaneOneErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CntclientInputErrorCounterLaneOneErrorPortn.setStatus("current")
_Rm10010e40CntclientInputErrorCounterLaneOneOverloadPortn_Type = EkiOnOff
_Rm10010e40CntclientInputErrorCounterLaneOneOverloadPortn_Object = MibTableColumn
rm10010e40CntclientInputErrorCounterLaneOneOverloadPortn = _Rm10010e40CntclientInputErrorCounterLaneOneOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4, 2, 16, 1, 4),
    _Rm10010e40CntclientInputErrorCounterLaneOneOverloadPortn_Type()
)
rm10010e40CntclientInputErrorCounterLaneOneOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CntclientInputErrorCounterLaneOneOverloadPortn.setStatus("current")
_Rm10010e40CntclientInputErrorCounterLaneTwoTable_Object = MibTable
rm10010e40CntclientInputErrorCounterLaneTwoTable = _Rm10010e40CntclientInputErrorCounterLaneTwoTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4, 2, 32)
)
if mibBuilder.loadTexts:
    rm10010e40CntclientInputErrorCounterLaneTwoTable.setStatus("current")
_Rm10010e40CntclientInputErrorCounterLaneTwoEntry_Object = MibTableRow
rm10010e40CntclientInputErrorCounterLaneTwoEntry = _Rm10010e40CntclientInputErrorCounterLaneTwoEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4, 2, 32, 1)
)
rm10010e40CntclientInputErrorCounterLaneTwoEntry.setIndexNames(
    (0, "EKINOPS-Rm10010e40-MIB", "rm10010e40CntclientInputErrorCounterLaneTwoIndex"),
)
if mibBuilder.loadTexts:
    rm10010e40CntclientInputErrorCounterLaneTwoEntry.setStatus("current")


class _Rm10010e40CntclientInputErrorCounterLaneTwoIndex_Type(Integer32):
    """Custom type rm10010e40CntclientInputErrorCounterLaneTwoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010e40CntclientInputErrorCounterLaneTwoIndex_Type.__name__ = "Integer32"
_Rm10010e40CntclientInputErrorCounterLaneTwoIndex_Object = MibTableColumn
rm10010e40CntclientInputErrorCounterLaneTwoIndex = _Rm10010e40CntclientInputErrorCounterLaneTwoIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4, 2, 32, 1, 1),
    _Rm10010e40CntclientInputErrorCounterLaneTwoIndex_Type()
)
rm10010e40CntclientInputErrorCounterLaneTwoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CntclientInputErrorCounterLaneTwoIndex.setStatus("current")
_Rm10010e40CntclientInputErrorCounterLaneTwoValuePortn_Type = Counter32
_Rm10010e40CntclientInputErrorCounterLaneTwoValuePortn_Object = MibTableColumn
rm10010e40CntclientInputErrorCounterLaneTwoValuePortn = _Rm10010e40CntclientInputErrorCounterLaneTwoValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4, 2, 32, 1, 2),
    _Rm10010e40CntclientInputErrorCounterLaneTwoValuePortn_Type()
)
rm10010e40CntclientInputErrorCounterLaneTwoValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CntclientInputErrorCounterLaneTwoValuePortn.setStatus("current")
_Rm10010e40CntclientInputErrorCounterLaneTwoErrorPortn_Type = EkiOnOff
_Rm10010e40CntclientInputErrorCounterLaneTwoErrorPortn_Object = MibTableColumn
rm10010e40CntclientInputErrorCounterLaneTwoErrorPortn = _Rm10010e40CntclientInputErrorCounterLaneTwoErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4, 2, 32, 1, 3),
    _Rm10010e40CntclientInputErrorCounterLaneTwoErrorPortn_Type()
)
rm10010e40CntclientInputErrorCounterLaneTwoErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CntclientInputErrorCounterLaneTwoErrorPortn.setStatus("current")
_Rm10010e40CntclientInputErrorCounterLaneTwoOverloadPortn_Type = EkiOnOff
_Rm10010e40CntclientInputErrorCounterLaneTwoOverloadPortn_Object = MibTableColumn
rm10010e40CntclientInputErrorCounterLaneTwoOverloadPortn = _Rm10010e40CntclientInputErrorCounterLaneTwoOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4, 2, 32, 1, 4),
    _Rm10010e40CntclientInputErrorCounterLaneTwoOverloadPortn_Type()
)
rm10010e40CntclientInputErrorCounterLaneTwoOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CntclientInputErrorCounterLaneTwoOverloadPortn.setStatus("current")
_Rm10010e40CntclientInputErrorCounterTable_Object = MibTable
rm10010e40CntclientInputErrorCounterTable = _Rm10010e40CntclientInputErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4, 2, 80)
)
if mibBuilder.loadTexts:
    rm10010e40CntclientInputErrorCounterTable.setStatus("current")
_Rm10010e40CntclientInputErrorCounterEntry_Object = MibTableRow
rm10010e40CntclientInputErrorCounterEntry = _Rm10010e40CntclientInputErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4, 2, 80, 1)
)
rm10010e40CntclientInputErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Rm10010e40-MIB", "rm10010e40CntclientInputErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    rm10010e40CntclientInputErrorCounterEntry.setStatus("current")


class _Rm10010e40CntclientInputErrorCounterIndex_Type(Integer32):
    """Custom type rm10010e40CntclientInputErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010e40CntclientInputErrorCounterIndex_Type.__name__ = "Integer32"
_Rm10010e40CntclientInputErrorCounterIndex_Object = MibTableColumn
rm10010e40CntclientInputErrorCounterIndex = _Rm10010e40CntclientInputErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4, 2, 80, 1, 1),
    _Rm10010e40CntclientInputErrorCounterIndex_Type()
)
rm10010e40CntclientInputErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CntclientInputErrorCounterIndex.setStatus("current")
_Rm10010e40CntclientInputErrorCounterValuePortn_Type = Counter32
_Rm10010e40CntclientInputErrorCounterValuePortn_Object = MibTableColumn
rm10010e40CntclientInputErrorCounterValuePortn = _Rm10010e40CntclientInputErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4, 2, 80, 1, 2),
    _Rm10010e40CntclientInputErrorCounterValuePortn_Type()
)
rm10010e40CntclientInputErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CntclientInputErrorCounterValuePortn.setStatus("current")
_Rm10010e40CntclientInputErrorCounterErrorPortn_Type = EkiOnOff
_Rm10010e40CntclientInputErrorCounterErrorPortn_Object = MibTableColumn
rm10010e40CntclientInputErrorCounterErrorPortn = _Rm10010e40CntclientInputErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4, 2, 80, 1, 3),
    _Rm10010e40CntclientInputErrorCounterErrorPortn_Type()
)
rm10010e40CntclientInputErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CntclientInputErrorCounterErrorPortn.setStatus("current")
_Rm10010e40CntclientInputErrorCounterOverloadPortn_Type = EkiOnOff
_Rm10010e40CntclientInputErrorCounterOverloadPortn_Object = MibTableColumn
rm10010e40CntclientInputErrorCounterOverloadPortn = _Rm10010e40CntclientInputErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4, 2, 80, 1, 4),
    _Rm10010e40CntclientInputErrorCounterOverloadPortn_Type()
)
rm10010e40CntclientInputErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CntclientInputErrorCounterOverloadPortn.setStatus("current")
_Rm10010e40CntclientCbipCounterTable_Object = MibTable
rm10010e40CntclientCbipCounterTable = _Rm10010e40CntclientCbipCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4, 2, 96)
)
if mibBuilder.loadTexts:
    rm10010e40CntclientCbipCounterTable.setStatus("current")
_Rm10010e40CntclientCbipCounterEntry_Object = MibTableRow
rm10010e40CntclientCbipCounterEntry = _Rm10010e40CntclientCbipCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4, 2, 96, 1)
)
rm10010e40CntclientCbipCounterEntry.setIndexNames(
    (0, "EKINOPS-Rm10010e40-MIB", "rm10010e40CntclientCbipCounterIndex"),
)
if mibBuilder.loadTexts:
    rm10010e40CntclientCbipCounterEntry.setStatus("current")


class _Rm10010e40CntclientCbipCounterIndex_Type(Integer32):
    """Custom type rm10010e40CntclientCbipCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010e40CntclientCbipCounterIndex_Type.__name__ = "Integer32"
_Rm10010e40CntclientCbipCounterIndex_Object = MibTableColumn
rm10010e40CntclientCbipCounterIndex = _Rm10010e40CntclientCbipCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4, 2, 96, 1, 1),
    _Rm10010e40CntclientCbipCounterIndex_Type()
)
rm10010e40CntclientCbipCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CntclientCbipCounterIndex.setStatus("current")
_Rm10010e40CntclientCbipCounterValuePortn_Type = Counter32
_Rm10010e40CntclientCbipCounterValuePortn_Object = MibTableColumn
rm10010e40CntclientCbipCounterValuePortn = _Rm10010e40CntclientCbipCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4, 2, 96, 1, 2),
    _Rm10010e40CntclientCbipCounterValuePortn_Type()
)
rm10010e40CntclientCbipCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CntclientCbipCounterValuePortn.setStatus("current")
_Rm10010e40CntclientCbipCounterErrorPortn_Type = EkiOnOff
_Rm10010e40CntclientCbipCounterErrorPortn_Object = MibTableColumn
rm10010e40CntclientCbipCounterErrorPortn = _Rm10010e40CntclientCbipCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4, 2, 96, 1, 3),
    _Rm10010e40CntclientCbipCounterErrorPortn_Type()
)
rm10010e40CntclientCbipCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CntclientCbipCounterErrorPortn.setStatus("current")
_Rm10010e40CntclientCbipCounterOverloadPortn_Type = EkiOnOff
_Rm10010e40CntclientCbipCounterOverloadPortn_Object = MibTableColumn
rm10010e40CntclientCbipCounterOverloadPortn = _Rm10010e40CntclientCbipCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4, 2, 96, 1, 4),
    _Rm10010e40CntclientCbipCounterOverloadPortn_Type()
)
rm10010e40CntclientCbipCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CntclientCbipCounterOverloadPortn.setStatus("current")
_Rm10010e40CntLine_ObjectIdentity = ObjectIdentity
rm10010e40CntLine = _Rm10010e40CntLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4, 3)
)
_Rm10010e40CntlocalLineSmBip8ErrorCounterTable_Object = MibTable
rm10010e40CntlocalLineSmBip8ErrorCounterTable = _Rm10010e40CntlocalLineSmBip8ErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4, 3, 192)
)
if mibBuilder.loadTexts:
    rm10010e40CntlocalLineSmBip8ErrorCounterTable.setStatus("current")
_Rm10010e40CntlocalLineSmBip8ErrorCounterEntry_Object = MibTableRow
rm10010e40CntlocalLineSmBip8ErrorCounterEntry = _Rm10010e40CntlocalLineSmBip8ErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4, 3, 192, 1)
)
rm10010e40CntlocalLineSmBip8ErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Rm10010e40-MIB", "rm10010e40CntlocalLineSmBip8ErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    rm10010e40CntlocalLineSmBip8ErrorCounterEntry.setStatus("current")


class _Rm10010e40CntlocalLineSmBip8ErrorCounterIndex_Type(Integer32):
    """Custom type rm10010e40CntlocalLineSmBip8ErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010e40CntlocalLineSmBip8ErrorCounterIndex_Type.__name__ = "Integer32"
_Rm10010e40CntlocalLineSmBip8ErrorCounterIndex_Object = MibTableColumn
rm10010e40CntlocalLineSmBip8ErrorCounterIndex = _Rm10010e40CntlocalLineSmBip8ErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4, 3, 192, 1, 1),
    _Rm10010e40CntlocalLineSmBip8ErrorCounterIndex_Type()
)
rm10010e40CntlocalLineSmBip8ErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CntlocalLineSmBip8ErrorCounterIndex.setStatus("current")
_Rm10010e40CntlocalLineSmBip8ErrorCounterValuePortn_Type = Counter64
_Rm10010e40CntlocalLineSmBip8ErrorCounterValuePortn_Object = MibTableColumn
rm10010e40CntlocalLineSmBip8ErrorCounterValuePortn = _Rm10010e40CntlocalLineSmBip8ErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4, 3, 192, 1, 2),
    _Rm10010e40CntlocalLineSmBip8ErrorCounterValuePortn_Type()
)
rm10010e40CntlocalLineSmBip8ErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CntlocalLineSmBip8ErrorCounterValuePortn.setStatus("current")
_Rm10010e40CntlocalLineSmBip8ErrorCounterErrorPortn_Type = EkiOnOff
_Rm10010e40CntlocalLineSmBip8ErrorCounterErrorPortn_Object = MibTableColumn
rm10010e40CntlocalLineSmBip8ErrorCounterErrorPortn = _Rm10010e40CntlocalLineSmBip8ErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4, 3, 192, 1, 3),
    _Rm10010e40CntlocalLineSmBip8ErrorCounterErrorPortn_Type()
)
rm10010e40CntlocalLineSmBip8ErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CntlocalLineSmBip8ErrorCounterErrorPortn.setStatus("current")
_Rm10010e40CntlocalLineSmBip8ErrorCounterOverloadPortn_Type = EkiOnOff
_Rm10010e40CntlocalLineSmBip8ErrorCounterOverloadPortn_Object = MibTableColumn
rm10010e40CntlocalLineSmBip8ErrorCounterOverloadPortn = _Rm10010e40CntlocalLineSmBip8ErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4, 3, 192, 1, 4),
    _Rm10010e40CntlocalLineSmBip8ErrorCounterOverloadPortn_Type()
)
rm10010e40CntlocalLineSmBip8ErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CntlocalLineSmBip8ErrorCounterOverloadPortn.setStatus("current")
_Rm10010e40CntlocalLineFecCorrectedErrorsCounterTable_Object = MibTable
rm10010e40CntlocalLineFecCorrectedErrorsCounterTable = _Rm10010e40CntlocalLineFecCorrectedErrorsCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4, 3, 193)
)
if mibBuilder.loadTexts:
    rm10010e40CntlocalLineFecCorrectedErrorsCounterTable.setStatus("current")
_Rm10010e40CntlocalLineFecCorrectedErrorsCounterEntry_Object = MibTableRow
rm10010e40CntlocalLineFecCorrectedErrorsCounterEntry = _Rm10010e40CntlocalLineFecCorrectedErrorsCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4, 3, 193, 1)
)
rm10010e40CntlocalLineFecCorrectedErrorsCounterEntry.setIndexNames(
    (0, "EKINOPS-Rm10010e40-MIB", "rm10010e40CntlocalLineFecCorrectedErrorsCounterIndex"),
)
if mibBuilder.loadTexts:
    rm10010e40CntlocalLineFecCorrectedErrorsCounterEntry.setStatus("current")


class _Rm10010e40CntlocalLineFecCorrectedErrorsCounterIndex_Type(Integer32):
    """Custom type rm10010e40CntlocalLineFecCorrectedErrorsCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010e40CntlocalLineFecCorrectedErrorsCounterIndex_Type.__name__ = "Integer32"
_Rm10010e40CntlocalLineFecCorrectedErrorsCounterIndex_Object = MibTableColumn
rm10010e40CntlocalLineFecCorrectedErrorsCounterIndex = _Rm10010e40CntlocalLineFecCorrectedErrorsCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4, 3, 193, 1, 1),
    _Rm10010e40CntlocalLineFecCorrectedErrorsCounterIndex_Type()
)
rm10010e40CntlocalLineFecCorrectedErrorsCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CntlocalLineFecCorrectedErrorsCounterIndex.setStatus("current")
_Rm10010e40CntlocalLineFecCorrectedErrorsCounterValuePortn_Type = Counter64
_Rm10010e40CntlocalLineFecCorrectedErrorsCounterValuePortn_Object = MibTableColumn
rm10010e40CntlocalLineFecCorrectedErrorsCounterValuePortn = _Rm10010e40CntlocalLineFecCorrectedErrorsCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4, 3, 193, 1, 2),
    _Rm10010e40CntlocalLineFecCorrectedErrorsCounterValuePortn_Type()
)
rm10010e40CntlocalLineFecCorrectedErrorsCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CntlocalLineFecCorrectedErrorsCounterValuePortn.setStatus("current")
_Rm10010e40CntlocalLineFecCorrectedErrorsCounterErrorPortn_Type = EkiOnOff
_Rm10010e40CntlocalLineFecCorrectedErrorsCounterErrorPortn_Object = MibTableColumn
rm10010e40CntlocalLineFecCorrectedErrorsCounterErrorPortn = _Rm10010e40CntlocalLineFecCorrectedErrorsCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4, 3, 193, 1, 3),
    _Rm10010e40CntlocalLineFecCorrectedErrorsCounterErrorPortn_Type()
)
rm10010e40CntlocalLineFecCorrectedErrorsCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CntlocalLineFecCorrectedErrorsCounterErrorPortn.setStatus("current")
_Rm10010e40CntlocalLineFecCorrectedErrorsCounterOverloadPortn_Type = EkiOnOff
_Rm10010e40CntlocalLineFecCorrectedErrorsCounterOverloadPortn_Object = MibTableColumn
rm10010e40CntlocalLineFecCorrectedErrorsCounterOverloadPortn = _Rm10010e40CntlocalLineFecCorrectedErrorsCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4, 3, 193, 1, 4),
    _Rm10010e40CntlocalLineFecCorrectedErrorsCounterOverloadPortn_Type()
)
rm10010e40CntlocalLineFecCorrectedErrorsCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CntlocalLineFecCorrectedErrorsCounterOverloadPortn.setStatus("current")
_Rm10010e40CntremoteLineSmBip8ErrorCounterTable_Object = MibTable
rm10010e40CntremoteLineSmBip8ErrorCounterTable = _Rm10010e40CntremoteLineSmBip8ErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4, 3, 194)
)
if mibBuilder.loadTexts:
    rm10010e40CntremoteLineSmBip8ErrorCounterTable.setStatus("current")
_Rm10010e40CntremoteLineSmBip8ErrorCounterEntry_Object = MibTableRow
rm10010e40CntremoteLineSmBip8ErrorCounterEntry = _Rm10010e40CntremoteLineSmBip8ErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4, 3, 194, 1)
)
rm10010e40CntremoteLineSmBip8ErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Rm10010e40-MIB", "rm10010e40CntremoteLineSmBip8ErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    rm10010e40CntremoteLineSmBip8ErrorCounterEntry.setStatus("current")


class _Rm10010e40CntremoteLineSmBip8ErrorCounterIndex_Type(Integer32):
    """Custom type rm10010e40CntremoteLineSmBip8ErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010e40CntremoteLineSmBip8ErrorCounterIndex_Type.__name__ = "Integer32"
_Rm10010e40CntremoteLineSmBip8ErrorCounterIndex_Object = MibTableColumn
rm10010e40CntremoteLineSmBip8ErrorCounterIndex = _Rm10010e40CntremoteLineSmBip8ErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4, 3, 194, 1, 1),
    _Rm10010e40CntremoteLineSmBip8ErrorCounterIndex_Type()
)
rm10010e40CntremoteLineSmBip8ErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CntremoteLineSmBip8ErrorCounterIndex.setStatus("current")
_Rm10010e40CntremoteLineSmBip8ErrorCounterValuePortn_Type = Counter64
_Rm10010e40CntremoteLineSmBip8ErrorCounterValuePortn_Object = MibTableColumn
rm10010e40CntremoteLineSmBip8ErrorCounterValuePortn = _Rm10010e40CntremoteLineSmBip8ErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4, 3, 194, 1, 2),
    _Rm10010e40CntremoteLineSmBip8ErrorCounterValuePortn_Type()
)
rm10010e40CntremoteLineSmBip8ErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CntremoteLineSmBip8ErrorCounterValuePortn.setStatus("current")
_Rm10010e40CntremoteLineSmBip8ErrorCounterErrorPortn_Type = EkiOnOff
_Rm10010e40CntremoteLineSmBip8ErrorCounterErrorPortn_Object = MibTableColumn
rm10010e40CntremoteLineSmBip8ErrorCounterErrorPortn = _Rm10010e40CntremoteLineSmBip8ErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4, 3, 194, 1, 3),
    _Rm10010e40CntremoteLineSmBip8ErrorCounterErrorPortn_Type()
)
rm10010e40CntremoteLineSmBip8ErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CntremoteLineSmBip8ErrorCounterErrorPortn.setStatus("current")
_Rm10010e40CntremoteLineSmBip8ErrorCounterOverloadPortn_Type = EkiOnOff
_Rm10010e40CntremoteLineSmBip8ErrorCounterOverloadPortn_Object = MibTableColumn
rm10010e40CntremoteLineSmBip8ErrorCounterOverloadPortn = _Rm10010e40CntremoteLineSmBip8ErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4, 3, 194, 1, 4),
    _Rm10010e40CntremoteLineSmBip8ErrorCounterOverloadPortn_Type()
)
rm10010e40CntremoteLineSmBip8ErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CntremoteLineSmBip8ErrorCounterOverloadPortn.setStatus("current")
_Rm10010e40CntlineDfrmTimCntTable_Object = MibTable
rm10010e40CntlineDfrmTimCntTable = _Rm10010e40CntlineDfrmTimCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4, 3, 195)
)
if mibBuilder.loadTexts:
    rm10010e40CntlineDfrmTimCntTable.setStatus("current")
_Rm10010e40CntlineDfrmTimCntEntry_Object = MibTableRow
rm10010e40CntlineDfrmTimCntEntry = _Rm10010e40CntlineDfrmTimCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4, 3, 195, 1)
)
rm10010e40CntlineDfrmTimCntEntry.setIndexNames(
    (0, "EKINOPS-Rm10010e40-MIB", "rm10010e40CntlineDfrmTimCntIndex"),
)
if mibBuilder.loadTexts:
    rm10010e40CntlineDfrmTimCntEntry.setStatus("current")


class _Rm10010e40CntlineDfrmTimCntIndex_Type(Integer32):
    """Custom type rm10010e40CntlineDfrmTimCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010e40CntlineDfrmTimCntIndex_Type.__name__ = "Integer32"
_Rm10010e40CntlineDfrmTimCntIndex_Object = MibTableColumn
rm10010e40CntlineDfrmTimCntIndex = _Rm10010e40CntlineDfrmTimCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4, 3, 195, 1, 1),
    _Rm10010e40CntlineDfrmTimCntIndex_Type()
)
rm10010e40CntlineDfrmTimCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CntlineDfrmTimCntIndex.setStatus("current")
_Rm10010e40CntlineDfrmTimCntValuePortn_Type = Counter64
_Rm10010e40CntlineDfrmTimCntValuePortn_Object = MibTableColumn
rm10010e40CntlineDfrmTimCntValuePortn = _Rm10010e40CntlineDfrmTimCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4, 3, 195, 1, 2),
    _Rm10010e40CntlineDfrmTimCntValuePortn_Type()
)
rm10010e40CntlineDfrmTimCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CntlineDfrmTimCntValuePortn.setStatus("current")
_Rm10010e40CntlineDfrmTimCntErrorPortn_Type = EkiOnOff
_Rm10010e40CntlineDfrmTimCntErrorPortn_Object = MibTableColumn
rm10010e40CntlineDfrmTimCntErrorPortn = _Rm10010e40CntlineDfrmTimCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4, 3, 195, 1, 3),
    _Rm10010e40CntlineDfrmTimCntErrorPortn_Type()
)
rm10010e40CntlineDfrmTimCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CntlineDfrmTimCntErrorPortn.setStatus("current")
_Rm10010e40CntlineDfrmTimCntOverloadPortn_Type = EkiOnOff
_Rm10010e40CntlineDfrmTimCntOverloadPortn_Object = MibTableColumn
rm10010e40CntlineDfrmTimCntOverloadPortn = _Rm10010e40CntlineDfrmTimCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4, 3, 195, 1, 4),
    _Rm10010e40CntlineDfrmTimCntOverloadPortn_Type()
)
rm10010e40CntlineDfrmTimCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CntlineDfrmTimCntOverloadPortn.setStatus("current")
_Rm10010e40CntlocalLineTrscvFecCorrectedErrorCounterTable_Object = MibTable
rm10010e40CntlocalLineTrscvFecCorrectedErrorCounterTable = _Rm10010e40CntlocalLineTrscvFecCorrectedErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4, 3, 196)
)
if mibBuilder.loadTexts:
    rm10010e40CntlocalLineTrscvFecCorrectedErrorCounterTable.setStatus("current")
_Rm10010e40CntlocalLineTrscvFecCorrectedErrorCounterEntry_Object = MibTableRow
rm10010e40CntlocalLineTrscvFecCorrectedErrorCounterEntry = _Rm10010e40CntlocalLineTrscvFecCorrectedErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4, 3, 196, 1)
)
rm10010e40CntlocalLineTrscvFecCorrectedErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Rm10010e40-MIB", "rm10010e40CntlocalLineTrscvFecCorrectedErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    rm10010e40CntlocalLineTrscvFecCorrectedErrorCounterEntry.setStatus("current")


class _Rm10010e40CntlocalLineTrscvFecCorrectedErrorCounterIndex_Type(Integer32):
    """Custom type rm10010e40CntlocalLineTrscvFecCorrectedErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010e40CntlocalLineTrscvFecCorrectedErrorCounterIndex_Type.__name__ = "Integer32"
_Rm10010e40CntlocalLineTrscvFecCorrectedErrorCounterIndex_Object = MibTableColumn
rm10010e40CntlocalLineTrscvFecCorrectedErrorCounterIndex = _Rm10010e40CntlocalLineTrscvFecCorrectedErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4, 3, 196, 1, 1),
    _Rm10010e40CntlocalLineTrscvFecCorrectedErrorCounterIndex_Type()
)
rm10010e40CntlocalLineTrscvFecCorrectedErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CntlocalLineTrscvFecCorrectedErrorCounterIndex.setStatus("current")
_Rm10010e40CntlocalLineTrscvFecCorrectedErrorCounterValuePortn_Type = Counter64
_Rm10010e40CntlocalLineTrscvFecCorrectedErrorCounterValuePortn_Object = MibTableColumn
rm10010e40CntlocalLineTrscvFecCorrectedErrorCounterValuePortn = _Rm10010e40CntlocalLineTrscvFecCorrectedErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4, 3, 196, 1, 2),
    _Rm10010e40CntlocalLineTrscvFecCorrectedErrorCounterValuePortn_Type()
)
rm10010e40CntlocalLineTrscvFecCorrectedErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CntlocalLineTrscvFecCorrectedErrorCounterValuePortn.setStatus("current")
_Rm10010e40CntlocalLineTrscvFecCorrectedErrorCounterErrorPortn_Type = EkiOnOff
_Rm10010e40CntlocalLineTrscvFecCorrectedErrorCounterErrorPortn_Object = MibTableColumn
rm10010e40CntlocalLineTrscvFecCorrectedErrorCounterErrorPortn = _Rm10010e40CntlocalLineTrscvFecCorrectedErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4, 3, 196, 1, 3),
    _Rm10010e40CntlocalLineTrscvFecCorrectedErrorCounterErrorPortn_Type()
)
rm10010e40CntlocalLineTrscvFecCorrectedErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CntlocalLineTrscvFecCorrectedErrorCounterErrorPortn.setStatus("current")
_Rm10010e40CntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn_Type = EkiOnOff
_Rm10010e40CntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn_Object = MibTableColumn
rm10010e40CntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn = _Rm10010e40CntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4, 3, 196, 1, 4),
    _Rm10010e40CntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn_Type()
)
rm10010e40CntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn.setStatus("current")
_Rm10010e40CntlocalLineTrscvFecUncorrectedErrorCounterTable_Object = MibTable
rm10010e40CntlocalLineTrscvFecUncorrectedErrorCounterTable = _Rm10010e40CntlocalLineTrscvFecUncorrectedErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4, 3, 197)
)
if mibBuilder.loadTexts:
    rm10010e40CntlocalLineTrscvFecUncorrectedErrorCounterTable.setStatus("current")
_Rm10010e40CntlocalLineTrscvFecUncorrectedErrorCounterEntry_Object = MibTableRow
rm10010e40CntlocalLineTrscvFecUncorrectedErrorCounterEntry = _Rm10010e40CntlocalLineTrscvFecUncorrectedErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4, 3, 197, 1)
)
rm10010e40CntlocalLineTrscvFecUncorrectedErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Rm10010e40-MIB", "rm10010e40CntlocalLineTrscvFecUncorrectedErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    rm10010e40CntlocalLineTrscvFecUncorrectedErrorCounterEntry.setStatus("current")


class _Rm10010e40CntlocalLineTrscvFecUncorrectedErrorCounterIndex_Type(Integer32):
    """Custom type rm10010e40CntlocalLineTrscvFecUncorrectedErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010e40CntlocalLineTrscvFecUncorrectedErrorCounterIndex_Type.__name__ = "Integer32"
_Rm10010e40CntlocalLineTrscvFecUncorrectedErrorCounterIndex_Object = MibTableColumn
rm10010e40CntlocalLineTrscvFecUncorrectedErrorCounterIndex = _Rm10010e40CntlocalLineTrscvFecUncorrectedErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4, 3, 197, 1, 1),
    _Rm10010e40CntlocalLineTrscvFecUncorrectedErrorCounterIndex_Type()
)
rm10010e40CntlocalLineTrscvFecUncorrectedErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CntlocalLineTrscvFecUncorrectedErrorCounterIndex.setStatus("current")
_Rm10010e40CntlocalLineTrscvFecUncorrectedErrorCounterValuePortn_Type = Counter64
_Rm10010e40CntlocalLineTrscvFecUncorrectedErrorCounterValuePortn_Object = MibTableColumn
rm10010e40CntlocalLineTrscvFecUncorrectedErrorCounterValuePortn = _Rm10010e40CntlocalLineTrscvFecUncorrectedErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4, 3, 197, 1, 2),
    _Rm10010e40CntlocalLineTrscvFecUncorrectedErrorCounterValuePortn_Type()
)
rm10010e40CntlocalLineTrscvFecUncorrectedErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CntlocalLineTrscvFecUncorrectedErrorCounterValuePortn.setStatus("current")
_Rm10010e40CntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn_Type = EkiOnOff
_Rm10010e40CntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn_Object = MibTableColumn
rm10010e40CntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn = _Rm10010e40CntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4, 3, 197, 1, 3),
    _Rm10010e40CntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn_Type()
)
rm10010e40CntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn.setStatus("current")
_Rm10010e40CntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn_Type = EkiOnOff
_Rm10010e40CntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn_Object = MibTableColumn
rm10010e40CntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn = _Rm10010e40CntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 4, 3, 197, 1, 4),
    _Rm10010e40CntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn_Type()
)
rm10010e40CntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn.setStatus("current")
_Rm10010e40controlsWrite_ObjectIdentity = ObjectIdentity
rm10010e40controlsWrite = _Rm10010e40controlsWrite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6)
)
_Rm10010e40CtrlOther_ObjectIdentity = ObjectIdentity
rm10010e40CtrlOther = _Rm10010e40CtrlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 1)
)
_Rm10010e40CtrlconfMgnt1_ObjectIdentity = ObjectIdentity
rm10010e40CtrlconfMgnt1 = _Rm10010e40CtrlconfMgnt1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 1, 1)
)
_Rm10010e40CtrlConf1Load1_Type = EkiOnOff
_Rm10010e40CtrlConf1Load1_Object = MibScalar
rm10010e40CtrlConf1Load1 = _Rm10010e40CtrlConf1Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 1, 1, 1),
    _Rm10010e40CtrlConf1Load1_Type()
)
rm10010e40CtrlConf1Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010e40CtrlConf1Load1.setStatus("current")
_Rm10010e40CtrlConf2Load1_Type = EkiOnOff
_Rm10010e40CtrlConf2Load1_Object = MibScalar
rm10010e40CtrlConf2Load1 = _Rm10010e40CtrlConf2Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 1, 1, 2),
    _Rm10010e40CtrlConf2Load1_Type()
)
rm10010e40CtrlConf2Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010e40CtrlConf2Load1.setStatus("current")
_Rm10010e40CtrlConf2Flash1_Type = EkiOnOff
_Rm10010e40CtrlConf2Flash1_Object = MibScalar
rm10010e40CtrlConf2Flash1 = _Rm10010e40CtrlConf2Flash1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 1, 1, 10),
    _Rm10010e40CtrlConf2Flash1_Type()
)
rm10010e40CtrlConf2Flash1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010e40CtrlConf2Flash1.setStatus("current")
_Rm10010e40CtrlConf2Clear1_Type = EkiOnOff
_Rm10010e40CtrlConf2Clear1_Object = MibScalar
rm10010e40CtrlConf2Clear1 = _Rm10010e40CtrlConf2Clear1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 1, 1, 14),
    _Rm10010e40CtrlConf2Clear1_Type()
)
rm10010e40CtrlConf2Clear1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010e40CtrlConf2Clear1.setStatus("current")
_Rm10010e40Ctrlsynth4_ObjectIdentity = ObjectIdentity
rm10010e40Ctrlsynth4 = _Rm10010e40Ctrlsynth4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 1, 4)
)
_Rm10010e40CtrlCorrelatOn_Type = EkiOnOff
_Rm10010e40CtrlCorrelatOn_Object = MibScalar
rm10010e40CtrlCorrelatOn = _Rm10010e40CtrlCorrelatOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 1, 4, 1),
    _Rm10010e40CtrlCorrelatOn_Type()
)
rm10010e40CtrlCorrelatOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010e40CtrlCorrelatOn.setStatus("current")
_Rm10010e40CtrlCorrelatOff_Type = EkiOnOff
_Rm10010e40CtrlCorrelatOff_Object = MibScalar
rm10010e40CtrlCorrelatOff = _Rm10010e40CtrlCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 1, 4, 2),
    _Rm10010e40CtrlCorrelatOff_Type()
)
rm10010e40CtrlCorrelatOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010e40CtrlCorrelatOff.setStatus("current")
_Rm10010e40CtrlswMgnt_ObjectIdentity = ObjectIdentity
rm10010e40CtrlswMgnt = _Rm10010e40CtrlswMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 1, 5)
)
_Rm10010e40CtrlColdReset_Type = EkiOnOff
_Rm10010e40CtrlColdReset_Object = MibScalar
rm10010e40CtrlColdReset = _Rm10010e40CtrlColdReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 1, 5, 2),
    _Rm10010e40CtrlColdReset_Type()
)
rm10010e40CtrlColdReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010e40CtrlColdReset.setStatus("current")
_Rm10010e40CtrlWarmReset_Type = EkiOnOff
_Rm10010e40CtrlWarmReset_Object = MibScalar
rm10010e40CtrlWarmReset = _Rm10010e40CtrlWarmReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 1, 5, 3),
    _Rm10010e40CtrlWarmReset_Type()
)
rm10010e40CtrlWarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010e40CtrlWarmReset.setStatus("current")
_Rm10010e40CtrlLoadSwBank1_Type = EkiOnOff
_Rm10010e40CtrlLoadSwBank1_Object = MibScalar
rm10010e40CtrlLoadSwBank1 = _Rm10010e40CtrlLoadSwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 1, 5, 5),
    _Rm10010e40CtrlLoadSwBank1_Type()
)
rm10010e40CtrlLoadSwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010e40CtrlLoadSwBank1.setStatus("current")
_Rm10010e40CtrlLoadSwBank2_Type = EkiOnOff
_Rm10010e40CtrlLoadSwBank2_Object = MibScalar
rm10010e40CtrlLoadSwBank2 = _Rm10010e40CtrlLoadSwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 1, 5, 6),
    _Rm10010e40CtrlLoadSwBank2_Type()
)
rm10010e40CtrlLoadSwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010e40CtrlLoadSwBank2.setStatus("current")
_Rm10010e40CtrlgwMgnt_ObjectIdentity = ObjectIdentity
rm10010e40CtrlgwMgnt = _Rm10010e40CtrlgwMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 1, 6)
)
_Rm10010e40CtrlCurrentGwReset_Type = EkiOnOff
_Rm10010e40CtrlCurrentGwReset_Object = MibScalar
rm10010e40CtrlCurrentGwReset = _Rm10010e40CtrlCurrentGwReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 1, 6, 1),
    _Rm10010e40CtrlCurrentGwReset_Type()
)
rm10010e40CtrlCurrentGwReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010e40CtrlCurrentGwReset.setStatus("current")
_Rm10010e40CtrlLoadGwBank1_Type = EkiOnOff
_Rm10010e40CtrlLoadGwBank1_Object = MibScalar
rm10010e40CtrlLoadGwBank1 = _Rm10010e40CtrlLoadGwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 1, 6, 5),
    _Rm10010e40CtrlLoadGwBank1_Type()
)
rm10010e40CtrlLoadGwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010e40CtrlLoadGwBank1.setStatus("current")
_Rm10010e40CtrlLoadGwBank2_Type = EkiOnOff
_Rm10010e40CtrlLoadGwBank2_Object = MibScalar
rm10010e40CtrlLoadGwBank2 = _Rm10010e40CtrlLoadGwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 1, 6, 6),
    _Rm10010e40CtrlLoadGwBank2_Type()
)
rm10010e40CtrlLoadGwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010e40CtrlLoadGwBank2.setStatus("current")
_Rm10010e40CtrlLoadGwBank3_Type = EkiOnOff
_Rm10010e40CtrlLoadGwBank3_Object = MibScalar
rm10010e40CtrlLoadGwBank3 = _Rm10010e40CtrlLoadGwBank3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 1, 6, 7),
    _Rm10010e40CtrlLoadGwBank3_Type()
)
rm10010e40CtrlLoadGwBank3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010e40CtrlLoadGwBank3.setStatus("current")
_Rm10010e40CtrlLoadGwBank4_Type = EkiOnOff
_Rm10010e40CtrlLoadGwBank4_Object = MibScalar
rm10010e40CtrlLoadGwBank4 = _Rm10010e40CtrlLoadGwBank4_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 1, 6, 8),
    _Rm10010e40CtrlLoadGwBank4_Type()
)
rm10010e40CtrlLoadGwBank4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010e40CtrlLoadGwBank4.setStatus("current")
_Rm10010e40CtrlledTest_ObjectIdentity = ObjectIdentity
rm10010e40CtrlledTest = _Rm10010e40CtrlledTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 1, 192)
)
_Rm10010e40CtrlGreenLed_Type = EkiOnOff
_Rm10010e40CtrlGreenLed_Object = MibScalar
rm10010e40CtrlGreenLed = _Rm10010e40CtrlGreenLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 1, 192, 1),
    _Rm10010e40CtrlGreenLed_Type()
)
rm10010e40CtrlGreenLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010e40CtrlGreenLed.setStatus("current")
_Rm10010e40CtrlRedLed_Type = EkiOnOff
_Rm10010e40CtrlRedLed_Object = MibScalar
rm10010e40CtrlRedLed = _Rm10010e40CtrlRedLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 1, 192, 2),
    _Rm10010e40CtrlRedLed_Type()
)
rm10010e40CtrlRedLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010e40CtrlRedLed.setStatus("current")
_Rm10010e40CtrlLedOff_Type = EkiOnOff
_Rm10010e40CtrlLedOff_Object = MibScalar
rm10010e40CtrlLedOff = _Rm10010e40CtrlLedOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 1, 192, 3),
    _Rm10010e40CtrlLedOff_Type()
)
rm10010e40CtrlLedOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010e40CtrlLedOff.setStatus("current")
_Rm10010e40CtrlinitSwitchMarvell_ObjectIdentity = ObjectIdentity
rm10010e40CtrlinitSwitchMarvell = _Rm10010e40CtrlinitSwitchMarvell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 1, 201)
)
_Rm10010e40CtrlInitSwitchMarvell_Type = EkiOnOff
_Rm10010e40CtrlInitSwitchMarvell_Object = MibScalar
rm10010e40CtrlInitSwitchMarvell = _Rm10010e40CtrlInitSwitchMarvell_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 1, 201, 1),
    _Rm10010e40CtrlInitSwitchMarvell_Type()
)
rm10010e40CtrlInitSwitchMarvell.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010e40CtrlInitSwitchMarvell.setStatus("current")
_Rm10010e40CtrlresetCount_ObjectIdentity = ObjectIdentity
rm10010e40CtrlresetCount = _Rm10010e40CtrlresetCount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 1, 259)
)
_Rm10010e40CtrlResetcount_Type = EkiOnOff
_Rm10010e40CtrlResetcount_Object = MibScalar
rm10010e40CtrlResetcount = _Rm10010e40CtrlResetcount_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 1, 259, 1),
    _Rm10010e40CtrlResetcount_Type()
)
rm10010e40CtrlResetcount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010e40CtrlResetcount.setStatus("current")
_Rm10010e40CtrlresetRmon_ObjectIdentity = ObjectIdentity
rm10010e40CtrlresetRmon = _Rm10010e40CtrlresetRmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 1, 260)
)
_Rm10010e40CtrlResetrmon_Type = EkiOnOff
_Rm10010e40CtrlResetrmon_Object = MibScalar
rm10010e40CtrlResetrmon = _Rm10010e40CtrlResetrmon_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 1, 260, 1),
    _Rm10010e40CtrlResetrmon_Type()
)
rm10010e40CtrlResetrmon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010e40CtrlResetrmon.setStatus("current")
_Rm10010e40CtrlresetMeasurements_ObjectIdentity = ObjectIdentity
rm10010e40CtrlresetMeasurements = _Rm10010e40CtrlresetMeasurements_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 1, 261)
)
_Rm10010e40CtrlResetmeasurements_Type = EkiOnOff
_Rm10010e40CtrlResetmeasurements_Object = MibScalar
rm10010e40CtrlResetmeasurements = _Rm10010e40CtrlResetmeasurements_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 1, 261, 1),
    _Rm10010e40CtrlResetmeasurements_Type()
)
rm10010e40CtrlResetmeasurements.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010e40CtrlResetmeasurements.setStatus("current")
_Rm10010e40CtrlClient_ObjectIdentity = ObjectIdentity
rm10010e40CtrlClient = _Rm10010e40CtrlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 2)
)
_Rm10010e40CtrlaccessLoopTable_Object = MibTable
rm10010e40CtrlaccessLoopTable = _Rm10010e40CtrlaccessLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 2, 16)
)
if mibBuilder.loadTexts:
    rm10010e40CtrlaccessLoopTable.setStatus("current")
_Rm10010e40CtrlaccessLoopEntry_Object = MibTableRow
rm10010e40CtrlaccessLoopEntry = _Rm10010e40CtrlaccessLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 2, 16, 1)
)
rm10010e40CtrlaccessLoopEntry.setIndexNames(
    (0, "EKINOPS-Rm10010e40-MIB", "rm10010e40CtrlaccessLoopIndex"),
)
if mibBuilder.loadTexts:
    rm10010e40CtrlaccessLoopEntry.setStatus("current")


class _Rm10010e40CtrlaccessLoopIndex_Type(Integer32):
    """Custom type rm10010e40CtrlaccessLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010e40CtrlaccessLoopIndex_Type.__name__ = "Integer32"
_Rm10010e40CtrlaccessLoopIndex_Object = MibTableColumn
rm10010e40CtrlaccessLoopIndex = _Rm10010e40CtrlaccessLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 2, 16, 1, 1),
    _Rm10010e40CtrlaccessLoopIndex_Type()
)
rm10010e40CtrlaccessLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CtrlaccessLoopIndex.setStatus("current")
_Rm10010e40CtrlaccessLoopPortn_Type = EkiState
_Rm10010e40CtrlaccessLoopPortn_Object = MibTableColumn
rm10010e40CtrlaccessLoopPortn = _Rm10010e40CtrlaccessLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 2, 16, 1, 2),
    _Rm10010e40CtrlaccessLoopPortn_Type()
)
rm10010e40CtrlaccessLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010e40CtrlaccessLoopPortn.setStatus("current")
_Rm10010e40CtrlclientLoopToLineTable_Object = MibTable
rm10010e40CtrlclientLoopToLineTable = _Rm10010e40CtrlclientLoopToLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 2, 17)
)
if mibBuilder.loadTexts:
    rm10010e40CtrlclientLoopToLineTable.setStatus("current")
_Rm10010e40CtrlclientLoopToLineEntry_Object = MibTableRow
rm10010e40CtrlclientLoopToLineEntry = _Rm10010e40CtrlclientLoopToLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 2, 17, 1)
)
rm10010e40CtrlclientLoopToLineEntry.setIndexNames(
    (0, "EKINOPS-Rm10010e40-MIB", "rm10010e40CtrlclientLoopToLineIndex"),
)
if mibBuilder.loadTexts:
    rm10010e40CtrlclientLoopToLineEntry.setStatus("current")


class _Rm10010e40CtrlclientLoopToLineIndex_Type(Integer32):
    """Custom type rm10010e40CtrlclientLoopToLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010e40CtrlclientLoopToLineIndex_Type.__name__ = "Integer32"
_Rm10010e40CtrlclientLoopToLineIndex_Object = MibTableColumn
rm10010e40CtrlclientLoopToLineIndex = _Rm10010e40CtrlclientLoopToLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 2, 17, 1, 1),
    _Rm10010e40CtrlclientLoopToLineIndex_Type()
)
rm10010e40CtrlclientLoopToLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CtrlclientLoopToLineIndex.setStatus("current")
_Rm10010e40CtrlclientLoopToLinePortn_Type = EkiState
_Rm10010e40CtrlclientLoopToLinePortn_Object = MibTableColumn
rm10010e40CtrlclientLoopToLinePortn = _Rm10010e40CtrlclientLoopToLinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 2, 17, 1, 2),
    _Rm10010e40CtrlclientLoopToLinePortn_Type()
)
rm10010e40CtrlclientLoopToLinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010e40CtrlclientLoopToLinePortn.setStatus("current")
_Rm10010e40CtrlcsfUpInsTable_Object = MibTable
rm10010e40CtrlcsfUpInsTable = _Rm10010e40CtrlcsfUpInsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 2, 21)
)
if mibBuilder.loadTexts:
    rm10010e40CtrlcsfUpInsTable.setStatus("current")
_Rm10010e40CtrlcsfUpInsEntry_Object = MibTableRow
rm10010e40CtrlcsfUpInsEntry = _Rm10010e40CtrlcsfUpInsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 2, 21, 1)
)
rm10010e40CtrlcsfUpInsEntry.setIndexNames(
    (0, "EKINOPS-Rm10010e40-MIB", "rm10010e40CtrlcsfUpInsIndex"),
)
if mibBuilder.loadTexts:
    rm10010e40CtrlcsfUpInsEntry.setStatus("current")


class _Rm10010e40CtrlcsfUpInsIndex_Type(Integer32):
    """Custom type rm10010e40CtrlcsfUpInsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010e40CtrlcsfUpInsIndex_Type.__name__ = "Integer32"
_Rm10010e40CtrlcsfUpInsIndex_Object = MibTableColumn
rm10010e40CtrlcsfUpInsIndex = _Rm10010e40CtrlcsfUpInsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 2, 21, 1, 1),
    _Rm10010e40CtrlcsfUpInsIndex_Type()
)
rm10010e40CtrlcsfUpInsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CtrlcsfUpInsIndex.setStatus("current")
_Rm10010e40CtrlcsfUpInsPortn_Type = EkiState
_Rm10010e40CtrlcsfUpInsPortn_Object = MibTableColumn
rm10010e40CtrlcsfUpInsPortn = _Rm10010e40CtrlcsfUpInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 2, 21, 1, 2),
    _Rm10010e40CtrlcsfUpInsPortn_Type()
)
rm10010e40CtrlcsfUpInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010e40CtrlcsfUpInsPortn.setStatus("current")
_Rm10010e40CtrlcaisDwInsTable_Object = MibTable
rm10010e40CtrlcaisDwInsTable = _Rm10010e40CtrlcaisDwInsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 2, 22)
)
if mibBuilder.loadTexts:
    rm10010e40CtrlcaisDwInsTable.setStatus("current")
_Rm10010e40CtrlcaisDwInsEntry_Object = MibTableRow
rm10010e40CtrlcaisDwInsEntry = _Rm10010e40CtrlcaisDwInsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 2, 22, 1)
)
rm10010e40CtrlcaisDwInsEntry.setIndexNames(
    (0, "EKINOPS-Rm10010e40-MIB", "rm10010e40CtrlcaisDwInsIndex"),
)
if mibBuilder.loadTexts:
    rm10010e40CtrlcaisDwInsEntry.setStatus("current")


class _Rm10010e40CtrlcaisDwInsIndex_Type(Integer32):
    """Custom type rm10010e40CtrlcaisDwInsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010e40CtrlcaisDwInsIndex_Type.__name__ = "Integer32"
_Rm10010e40CtrlcaisDwInsIndex_Object = MibTableColumn
rm10010e40CtrlcaisDwInsIndex = _Rm10010e40CtrlcaisDwInsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 2, 22, 1, 1),
    _Rm10010e40CtrlcaisDwInsIndex_Type()
)
rm10010e40CtrlcaisDwInsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CtrlcaisDwInsIndex.setStatus("current")
_Rm10010e40CtrlcaisDwInsPortn_Type = EkiState
_Rm10010e40CtrlcaisDwInsPortn_Object = MibTableColumn
rm10010e40CtrlcaisDwInsPortn = _Rm10010e40CtrlcaisDwInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 2, 22, 1, 2),
    _Rm10010e40CtrlcaisDwInsPortn_Type()
)
rm10010e40CtrlcaisDwInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010e40CtrlcaisDwInsPortn.setStatus("current")
_Rm10010e40CtrlLine_ObjectIdentity = ObjectIdentity
rm10010e40CtrlLine = _Rm10010e40CtrlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 3)
)
_Rm10010e40CtrlcommAccessLoopTable_Object = MibTable
rm10010e40CtrlcommAccessLoopTable = _Rm10010e40CtrlcommAccessLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 3, 64)
)
if mibBuilder.loadTexts:
    rm10010e40CtrlcommAccessLoopTable.setStatus("current")
_Rm10010e40CtrlcommAccessLoopEntry_Object = MibTableRow
rm10010e40CtrlcommAccessLoopEntry = _Rm10010e40CtrlcommAccessLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 3, 64, 1)
)
rm10010e40CtrlcommAccessLoopEntry.setIndexNames(
    (0, "EKINOPS-Rm10010e40-MIB", "rm10010e40CtrlcommAccessLoopIndex"),
)
if mibBuilder.loadTexts:
    rm10010e40CtrlcommAccessLoopEntry.setStatus("current")


class _Rm10010e40CtrlcommAccessLoopIndex_Type(Integer32):
    """Custom type rm10010e40CtrlcommAccessLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010e40CtrlcommAccessLoopIndex_Type.__name__ = "Integer32"
_Rm10010e40CtrlcommAccessLoopIndex_Object = MibTableColumn
rm10010e40CtrlcommAccessLoopIndex = _Rm10010e40CtrlcommAccessLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 3, 64, 1, 1),
    _Rm10010e40CtrlcommAccessLoopIndex_Type()
)
rm10010e40CtrlcommAccessLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CtrlcommAccessLoopIndex.setStatus("current")
_Rm10010e40CtrlcommAccessLoopPortn_Type = EkiState
_Rm10010e40CtrlcommAccessLoopPortn_Object = MibTableColumn
rm10010e40CtrlcommAccessLoopPortn = _Rm10010e40CtrlcommAccessLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 3, 64, 1, 2),
    _Rm10010e40CtrlcommAccessLoopPortn_Type()
)
rm10010e40CtrlcommAccessLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010e40CtrlcommAccessLoopPortn.setStatus("current")
_Rm10010e40CtrllineLoopTable_Object = MibTable
rm10010e40CtrllineLoopTable = _Rm10010e40CtrllineLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 3, 66)
)
if mibBuilder.loadTexts:
    rm10010e40CtrllineLoopTable.setStatus("current")
_Rm10010e40CtrllineLoopEntry_Object = MibTableRow
rm10010e40CtrllineLoopEntry = _Rm10010e40CtrllineLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 3, 66, 1)
)
rm10010e40CtrllineLoopEntry.setIndexNames(
    (0, "EKINOPS-Rm10010e40-MIB", "rm10010e40CtrllineLoopIndex"),
)
if mibBuilder.loadTexts:
    rm10010e40CtrllineLoopEntry.setStatus("current")


class _Rm10010e40CtrllineLoopIndex_Type(Integer32):
    """Custom type rm10010e40CtrllineLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010e40CtrllineLoopIndex_Type.__name__ = "Integer32"
_Rm10010e40CtrllineLoopIndex_Object = MibTableColumn
rm10010e40CtrllineLoopIndex = _Rm10010e40CtrllineLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 3, 66, 1, 1),
    _Rm10010e40CtrllineLoopIndex_Type()
)
rm10010e40CtrllineLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CtrllineLoopIndex.setStatus("current")
_Rm10010e40CtrllineLoopPortn_Type = EkiState
_Rm10010e40CtrllineLoopPortn_Object = MibTableColumn
rm10010e40CtrllineLoopPortn = _Rm10010e40CtrllineLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 3, 66, 1, 2),
    _Rm10010e40CtrllineLoopPortn_Type()
)
rm10010e40CtrllineLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010e40CtrllineLoopPortn.setStatus("current")
_Rm10010e40CtrlfecDisableTable_Object = MibTable
rm10010e40CtrlfecDisableTable = _Rm10010e40CtrlfecDisableTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 3, 69)
)
if mibBuilder.loadTexts:
    rm10010e40CtrlfecDisableTable.setStatus("current")
_Rm10010e40CtrlfecDisableEntry_Object = MibTableRow
rm10010e40CtrlfecDisableEntry = _Rm10010e40CtrlfecDisableEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 3, 69, 1)
)
rm10010e40CtrlfecDisableEntry.setIndexNames(
    (0, "EKINOPS-Rm10010e40-MIB", "rm10010e40CtrlfecDisableIndex"),
)
if mibBuilder.loadTexts:
    rm10010e40CtrlfecDisableEntry.setStatus("current")


class _Rm10010e40CtrlfecDisableIndex_Type(Integer32):
    """Custom type rm10010e40CtrlfecDisableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010e40CtrlfecDisableIndex_Type.__name__ = "Integer32"
_Rm10010e40CtrlfecDisableIndex_Object = MibTableColumn
rm10010e40CtrlfecDisableIndex = _Rm10010e40CtrlfecDisableIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 3, 69, 1, 1),
    _Rm10010e40CtrlfecDisableIndex_Type()
)
rm10010e40CtrlfecDisableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CtrlfecDisableIndex.setStatus("current")
_Rm10010e40CtrlfecDisablePortn_Type = EkiState
_Rm10010e40CtrlfecDisablePortn_Object = MibTableColumn
rm10010e40CtrlfecDisablePortn = _Rm10010e40CtrlfecDisablePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 3, 69, 1, 2),
    _Rm10010e40CtrlfecDisablePortn_Type()
)
rm10010e40CtrlfecDisablePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010e40CtrlfecDisablePortn.setStatus("current")
_Rm10010e40CtrlmsaLineLoopTable_Object = MibTable
rm10010e40CtrlmsaLineLoopTable = _Rm10010e40CtrlmsaLineLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 3, 209)
)
if mibBuilder.loadTexts:
    rm10010e40CtrlmsaLineLoopTable.setStatus("current")
_Rm10010e40CtrlmsaLineLoopEntry_Object = MibTableRow
rm10010e40CtrlmsaLineLoopEntry = _Rm10010e40CtrlmsaLineLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 3, 209, 1)
)
rm10010e40CtrlmsaLineLoopEntry.setIndexNames(
    (0, "EKINOPS-Rm10010e40-MIB", "rm10010e40CtrlmsaLineLoopIndex"),
)
if mibBuilder.loadTexts:
    rm10010e40CtrlmsaLineLoopEntry.setStatus("current")


class _Rm10010e40CtrlmsaLineLoopIndex_Type(Integer32):
    """Custom type rm10010e40CtrlmsaLineLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010e40CtrlmsaLineLoopIndex_Type.__name__ = "Integer32"
_Rm10010e40CtrlmsaLineLoopIndex_Object = MibTableColumn
rm10010e40CtrlmsaLineLoopIndex = _Rm10010e40CtrlmsaLineLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 3, 209, 1, 1),
    _Rm10010e40CtrlmsaLineLoopIndex_Type()
)
rm10010e40CtrlmsaLineLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CtrlmsaLineLoopIndex.setStatus("current")
_Rm10010e40CtrlmsaLineLoopPortn_Type = EkiState
_Rm10010e40CtrlmsaLineLoopPortn_Object = MibTableColumn
rm10010e40CtrlmsaLineLoopPortn = _Rm10010e40CtrlmsaLineLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 3, 209, 1, 2),
    _Rm10010e40CtrlmsaLineLoopPortn_Type()
)
rm10010e40CtrlmsaLineLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010e40CtrlmsaLineLoopPortn.setStatus("current")
_Rm10010e40CtrlmsaTxResetTable_Object = MibTable
rm10010e40CtrlmsaTxResetTable = _Rm10010e40CtrlmsaTxResetTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 3, 210)
)
if mibBuilder.loadTexts:
    rm10010e40CtrlmsaTxResetTable.setStatus("current")
_Rm10010e40CtrlmsaTxResetEntry_Object = MibTableRow
rm10010e40CtrlmsaTxResetEntry = _Rm10010e40CtrlmsaTxResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 3, 210, 1)
)
rm10010e40CtrlmsaTxResetEntry.setIndexNames(
    (0, "EKINOPS-Rm10010e40-MIB", "rm10010e40CtrlmsaTxResetIndex"),
)
if mibBuilder.loadTexts:
    rm10010e40CtrlmsaTxResetEntry.setStatus("current")


class _Rm10010e40CtrlmsaTxResetIndex_Type(Integer32):
    """Custom type rm10010e40CtrlmsaTxResetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010e40CtrlmsaTxResetIndex_Type.__name__ = "Integer32"
_Rm10010e40CtrlmsaTxResetIndex_Object = MibTableColumn
rm10010e40CtrlmsaTxResetIndex = _Rm10010e40CtrlmsaTxResetIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 3, 210, 1, 1),
    _Rm10010e40CtrlmsaTxResetIndex_Type()
)
rm10010e40CtrlmsaTxResetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CtrlmsaTxResetIndex.setStatus("current")
_Rm10010e40CtrlmsaTxResetPortn_Type = EkiState
_Rm10010e40CtrlmsaTxResetPortn_Object = MibTableColumn
rm10010e40CtrlmsaTxResetPortn = _Rm10010e40CtrlmsaTxResetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 3, 210, 1, 2),
    _Rm10010e40CtrlmsaTxResetPortn_Type()
)
rm10010e40CtrlmsaTxResetPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010e40CtrlmsaTxResetPortn.setStatus("current")
_Rm10010e40CtrlmsaRxResetTable_Object = MibTable
rm10010e40CtrlmsaRxResetTable = _Rm10010e40CtrlmsaRxResetTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 3, 211)
)
if mibBuilder.loadTexts:
    rm10010e40CtrlmsaRxResetTable.setStatus("current")
_Rm10010e40CtrlmsaRxResetEntry_Object = MibTableRow
rm10010e40CtrlmsaRxResetEntry = _Rm10010e40CtrlmsaRxResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 3, 211, 1)
)
rm10010e40CtrlmsaRxResetEntry.setIndexNames(
    (0, "EKINOPS-Rm10010e40-MIB", "rm10010e40CtrlmsaRxResetIndex"),
)
if mibBuilder.loadTexts:
    rm10010e40CtrlmsaRxResetEntry.setStatus("current")


class _Rm10010e40CtrlmsaRxResetIndex_Type(Integer32):
    """Custom type rm10010e40CtrlmsaRxResetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010e40CtrlmsaRxResetIndex_Type.__name__ = "Integer32"
_Rm10010e40CtrlmsaRxResetIndex_Object = MibTableColumn
rm10010e40CtrlmsaRxResetIndex = _Rm10010e40CtrlmsaRxResetIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 3, 211, 1, 1),
    _Rm10010e40CtrlmsaRxResetIndex_Type()
)
rm10010e40CtrlmsaRxResetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CtrlmsaRxResetIndex.setStatus("current")
_Rm10010e40CtrlmsaRxResetPortn_Type = EkiState
_Rm10010e40CtrlmsaRxResetPortn_Object = MibTableColumn
rm10010e40CtrlmsaRxResetPortn = _Rm10010e40CtrlmsaRxResetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 3, 211, 1, 2),
    _Rm10010e40CtrlmsaRxResetPortn_Type()
)
rm10010e40CtrlmsaRxResetPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010e40CtrlmsaRxResetPortn.setStatus("current")
_Rm10010e40CtrlmsaShutdownTable_Object = MibTable
rm10010e40CtrlmsaShutdownTable = _Rm10010e40CtrlmsaShutdownTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 3, 212)
)
if mibBuilder.loadTexts:
    rm10010e40CtrlmsaShutdownTable.setStatus("current")
_Rm10010e40CtrlmsaShutdownEntry_Object = MibTableRow
rm10010e40CtrlmsaShutdownEntry = _Rm10010e40CtrlmsaShutdownEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 3, 212, 1)
)
rm10010e40CtrlmsaShutdownEntry.setIndexNames(
    (0, "EKINOPS-Rm10010e40-MIB", "rm10010e40CtrlmsaShutdownIndex"),
)
if mibBuilder.loadTexts:
    rm10010e40CtrlmsaShutdownEntry.setStatus("current")


class _Rm10010e40CtrlmsaShutdownIndex_Type(Integer32):
    """Custom type rm10010e40CtrlmsaShutdownIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010e40CtrlmsaShutdownIndex_Type.__name__ = "Integer32"
_Rm10010e40CtrlmsaShutdownIndex_Object = MibTableColumn
rm10010e40CtrlmsaShutdownIndex = _Rm10010e40CtrlmsaShutdownIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 3, 212, 1, 1),
    _Rm10010e40CtrlmsaShutdownIndex_Type()
)
rm10010e40CtrlmsaShutdownIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CtrlmsaShutdownIndex.setStatus("current")
_Rm10010e40CtrlmsaShutdownPortn_Type = EkiState
_Rm10010e40CtrlmsaShutdownPortn_Object = MibTableColumn
rm10010e40CtrlmsaShutdownPortn = _Rm10010e40CtrlmsaShutdownPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 6, 3, 212, 1, 2),
    _Rm10010e40CtrlmsaShutdownPortn_Type()
)
rm10010e40CtrlmsaShutdownPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010e40CtrlmsaShutdownPortn.setStatus("current")
_Rm10010e40ri_ObjectIdentity = ObjectIdentity
rm10010e40ri = _Rm10010e40ri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 7)
)
_Rm10010e40riTable_ObjectIdentity = ObjectIdentity
rm10010e40riTable = _Rm10010e40riTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 7, 1)
)
_Rm10010e40RinvSfpTable_Object = MibTable
rm10010e40RinvSfpTable = _Rm10010e40RinvSfpTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 7, 1, 1)
)
if mibBuilder.loadTexts:
    rm10010e40RinvSfpTable.setStatus("current")
_Rm10010e40RinvSfpEntry_Object = MibTableRow
rm10010e40RinvSfpEntry = _Rm10010e40RinvSfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 7, 1, 1, 1)
)
rm10010e40RinvSfpEntry.setIndexNames(
    (0, "EKINOPS-Rm10010e40-MIB", "rm10010e40RinvSfpIndex"),
)
if mibBuilder.loadTexts:
    rm10010e40RinvSfpEntry.setStatus("current")


class _Rm10010e40RinvSfpIndex_Type(Integer32):
    """Custom type rm10010e40RinvSfpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Rm10010e40RinvSfpIndex_Type.__name__ = "Integer32"
_Rm10010e40RinvSfpIndex_Object = MibTableColumn
rm10010e40RinvSfpIndex = _Rm10010e40RinvSfpIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 7, 1, 1, 1, 1),
    _Rm10010e40RinvSfpIndex_Type()
)
rm10010e40RinvSfpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40RinvSfpIndex.setStatus("current")
_Rm10010e40Rinvsfp_Type = DisplayString
_Rm10010e40Rinvsfp_Object = MibTableColumn
rm10010e40Rinvsfp = _Rm10010e40Rinvsfp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 7, 1, 1, 1, 2),
    _Rm10010e40Rinvsfp_Type()
)
rm10010e40Rinvsfp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40Rinvsfp.setStatus("current")
_Rm10010e40RinvLineTable_Object = MibTable
rm10010e40RinvLineTable = _Rm10010e40RinvLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 7, 1, 2)
)
if mibBuilder.loadTexts:
    rm10010e40RinvLineTable.setStatus("current")
_Rm10010e40RinvLineEntry_Object = MibTableRow
rm10010e40RinvLineEntry = _Rm10010e40RinvLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 7, 1, 2, 1)
)
rm10010e40RinvLineEntry.setIndexNames(
    (0, "EKINOPS-Rm10010e40-MIB", "rm10010e40RinvLineIndex"),
)
if mibBuilder.loadTexts:
    rm10010e40RinvLineEntry.setStatus("current")


class _Rm10010e40RinvLineIndex_Type(Integer32):
    """Custom type rm10010e40RinvLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Rm10010e40RinvLineIndex_Type.__name__ = "Integer32"
_Rm10010e40RinvLineIndex_Object = MibTableColumn
rm10010e40RinvLineIndex = _Rm10010e40RinvLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 7, 1, 2, 1, 1),
    _Rm10010e40RinvLineIndex_Type()
)
rm10010e40RinvLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40RinvLineIndex.setStatus("current")
_Rm10010e40RinvxfpLine_Type = DisplayString
_Rm10010e40RinvxfpLine_Object = MibTableColumn
rm10010e40RinvxfpLine = _Rm10010e40RinvxfpLine_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 7, 1, 2, 1, 2),
    _Rm10010e40RinvxfpLine_Type()
)
rm10010e40RinvxfpLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40RinvxfpLine.setStatus("current")
_Rm10010e40RinvReloadInventory_Type = EkiOnOff
_Rm10010e40RinvReloadInventory_Object = MibScalar
rm10010e40RinvReloadInventory = _Rm10010e40RinvReloadInventory_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 7, 2),
    _Rm10010e40RinvReloadInventory_Type()
)
rm10010e40RinvReloadInventory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010e40RinvReloadInventory.setStatus("current")
_Rm10010e40RinvHwPlatform_Type = DisplayString
_Rm10010e40RinvHwPlatform_Object = MibScalar
rm10010e40RinvHwPlatform = _Rm10010e40RinvHwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 7, 3),
    _Rm10010e40RinvHwPlatform_Type()
)
rm10010e40RinvHwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40RinvHwPlatform.setStatus("current")
_Rm10010e40RinvModulePlatform_Type = DisplayString
_Rm10010e40RinvModulePlatform_Object = MibScalar
rm10010e40RinvModulePlatform = _Rm10010e40RinvModulePlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 7, 4),
    _Rm10010e40RinvModulePlatform_Type()
)
rm10010e40RinvModulePlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40RinvModulePlatform.setStatus("current")
_Rm10010e40RinvSwPlatform_Type = DisplayString
_Rm10010e40RinvSwPlatform_Object = MibScalar
rm10010e40RinvSwPlatform = _Rm10010e40RinvSwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 7, 5),
    _Rm10010e40RinvSwPlatform_Type()
)
rm10010e40RinvSwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40RinvSwPlatform.setStatus("current")
_Rm10010e40RinvGwPlatform_Type = DisplayString
_Rm10010e40RinvGwPlatform_Object = MibScalar
rm10010e40RinvGwPlatform = _Rm10010e40RinvGwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 7, 6),
    _Rm10010e40RinvGwPlatform_Type()
)
rm10010e40RinvGwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40RinvGwPlatform.setStatus("current")
_Rm10010e40download_ObjectIdentity = ObjectIdentity
rm10010e40download = _Rm10010e40download_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 8)
)
_Rm10010e40DwlOther_ObjectIdentity = ObjectIdentity
rm10010e40DwlOther = _Rm10010e40DwlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 8, 1)
)
_Rm10010e40DwlrestartProcess_ObjectIdentity = ObjectIdentity
rm10010e40DwlrestartProcess = _Rm10010e40DwlrestartProcess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 8, 1, 0)
)
_Rm10010e40DwlWarmRestartProcessed_Type = EkiOnOff
_Rm10010e40DwlWarmRestartProcessed_Object = MibScalar
rm10010e40DwlWarmRestartProcessed = _Rm10010e40DwlWarmRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 8, 1, 0, 1),
    _Rm10010e40DwlWarmRestartProcessed_Type()
)
rm10010e40DwlWarmRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40DwlWarmRestartProcessed.setStatus("current")
_Rm10010e40DwlColdRestartProcessed_Type = EkiOnOff
_Rm10010e40DwlColdRestartProcessed_Object = MibScalar
rm10010e40DwlColdRestartProcessed = _Rm10010e40DwlColdRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 8, 1, 0, 2),
    _Rm10010e40DwlColdRestartProcessed_Type()
)
rm10010e40DwlColdRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40DwlColdRestartProcessed.setStatus("current")
_Rm10010e40DwlswBanksUsed_ObjectIdentity = ObjectIdentity
rm10010e40DwlswBanksUsed = _Rm10010e40DwlswBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 8, 1, 1)
)
_Rm10010e40DwlSwBank1Used_Type = EkiOnOff
_Rm10010e40DwlSwBank1Used_Object = MibScalar
rm10010e40DwlSwBank1Used = _Rm10010e40DwlSwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 8, 1, 1, 1),
    _Rm10010e40DwlSwBank1Used_Type()
)
rm10010e40DwlSwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40DwlSwBank1Used.setStatus("current")
_Rm10010e40DwlSwBank2Used_Type = EkiOnOff
_Rm10010e40DwlSwBank2Used_Object = MibScalar
rm10010e40DwlSwBank2Used = _Rm10010e40DwlSwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 8, 1, 1, 2),
    _Rm10010e40DwlSwBank2Used_Type()
)
rm10010e40DwlSwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40DwlSwBank2Used.setStatus("current")
_Rm10010e40DwlSwBank1Notempty_Type = EkiOnOff
_Rm10010e40DwlSwBank1Notempty_Object = MibScalar
rm10010e40DwlSwBank1Notempty = _Rm10010e40DwlSwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 8, 1, 1, 5),
    _Rm10010e40DwlSwBank1Notempty_Type()
)
rm10010e40DwlSwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40DwlSwBank1Notempty.setStatus("current")
_Rm10010e40DwlSwBank2Notempty_Type = EkiOnOff
_Rm10010e40DwlSwBank2Notempty_Object = MibScalar
rm10010e40DwlSwBank2Notempty = _Rm10010e40DwlSwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 8, 1, 1, 6),
    _Rm10010e40DwlSwBank2Notempty_Type()
)
rm10010e40DwlSwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40DwlSwBank2Notempty.setStatus("current")
_Rm10010e40DwlgwBanksUsed_ObjectIdentity = ObjectIdentity
rm10010e40DwlgwBanksUsed = _Rm10010e40DwlgwBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 8, 1, 2)
)
_Rm10010e40DwlGwBank1Used_Type = EkiOnOff
_Rm10010e40DwlGwBank1Used_Object = MibScalar
rm10010e40DwlGwBank1Used = _Rm10010e40DwlGwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 8, 1, 2, 1),
    _Rm10010e40DwlGwBank1Used_Type()
)
rm10010e40DwlGwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40DwlGwBank1Used.setStatus("current")
_Rm10010e40DwlGwBank2Used_Type = EkiOnOff
_Rm10010e40DwlGwBank2Used_Object = MibScalar
rm10010e40DwlGwBank2Used = _Rm10010e40DwlGwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 8, 1, 2, 2),
    _Rm10010e40DwlGwBank2Used_Type()
)
rm10010e40DwlGwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40DwlGwBank2Used.setStatus("current")
_Rm10010e40DwlGwBank3Used_Type = EkiOnOff
_Rm10010e40DwlGwBank3Used_Object = MibScalar
rm10010e40DwlGwBank3Used = _Rm10010e40DwlGwBank3Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 8, 1, 2, 3),
    _Rm10010e40DwlGwBank3Used_Type()
)
rm10010e40DwlGwBank3Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40DwlGwBank3Used.setStatus("current")
_Rm10010e40DwlGwBank4Used_Type = EkiOnOff
_Rm10010e40DwlGwBank4Used_Object = MibScalar
rm10010e40DwlGwBank4Used = _Rm10010e40DwlGwBank4Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 8, 1, 2, 4),
    _Rm10010e40DwlGwBank4Used_Type()
)
rm10010e40DwlGwBank4Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40DwlGwBank4Used.setStatus("current")
_Rm10010e40DwlGwBank1Notempty_Type = EkiOnOff
_Rm10010e40DwlGwBank1Notempty_Object = MibScalar
rm10010e40DwlGwBank1Notempty = _Rm10010e40DwlGwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 8, 1, 2, 5),
    _Rm10010e40DwlGwBank1Notempty_Type()
)
rm10010e40DwlGwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40DwlGwBank1Notempty.setStatus("current")
_Rm10010e40DwlGwBank2Notempty_Type = EkiOnOff
_Rm10010e40DwlGwBank2Notempty_Object = MibScalar
rm10010e40DwlGwBank2Notempty = _Rm10010e40DwlGwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 8, 1, 2, 6),
    _Rm10010e40DwlGwBank2Notempty_Type()
)
rm10010e40DwlGwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40DwlGwBank2Notempty.setStatus("current")
_Rm10010e40DwlGwBank3Notempty_Type = EkiOnOff
_Rm10010e40DwlGwBank3Notempty_Object = MibScalar
rm10010e40DwlGwBank3Notempty = _Rm10010e40DwlGwBank3Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 8, 1, 2, 7),
    _Rm10010e40DwlGwBank3Notempty_Type()
)
rm10010e40DwlGwBank3Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40DwlGwBank3Notempty.setStatus("current")
_Rm10010e40DwlGwBank4Notempty_Type = EkiOnOff
_Rm10010e40DwlGwBank4Notempty_Object = MibScalar
rm10010e40DwlGwBank4Notempty = _Rm10010e40DwlGwBank4Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 8, 1, 2, 8),
    _Rm10010e40DwlGwBank4Notempty_Type()
)
rm10010e40DwlGwBank4Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40DwlGwBank4Notempty.setStatus("current")
_Rm10010e40DwlClient_ObjectIdentity = ObjectIdentity
rm10010e40DwlClient = _Rm10010e40DwlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 8, 2)
)
_Rm10010e40DwlLine_ObjectIdentity = ObjectIdentity
rm10010e40DwlLine = _Rm10010e40DwlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 8, 3)
)
_Rm10010e40Config_ObjectIdentity = ObjectIdentity
rm10010e40Config = _Rm10010e40Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 9)
)
_Rm10010e40CfgAccessCAisCsf_ObjectIdentity = ObjectIdentity
rm10010e40CfgAccessCAisCsf = _Rm10010e40CfgAccessCAisCsf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 9, 1)
)
_Rm10010e40CfgClientcaiscsfTable_Object = MibTable
rm10010e40CfgClientcaiscsfTable = _Rm10010e40CfgClientcaiscsfTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 9, 1, 1)
)
if mibBuilder.loadTexts:
    rm10010e40CfgClientcaiscsfTable.setStatus("current")
_Rm10010e40CfgClientcaiscsfEntry_Object = MibTableRow
rm10010e40CfgClientcaiscsfEntry = _Rm10010e40CfgClientcaiscsfEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 9, 1, 1, 1)
)
rm10010e40CfgClientcaiscsfEntry.setIndexNames(
    (0, "EKINOPS-Rm10010e40-MIB", "rm10010e40CfgClientcaiscsfIndex"),
)
if mibBuilder.loadTexts:
    rm10010e40CfgClientcaiscsfEntry.setStatus("current")


class _Rm10010e40CfgClientcaiscsfIndex_Type(Integer32):
    """Custom type rm10010e40CfgClientcaiscsfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010e40CfgClientcaiscsfIndex_Type.__name__ = "Integer32"
_Rm10010e40CfgClientcaiscsfIndex_Object = MibTableColumn
rm10010e40CfgClientcaiscsfIndex = _Rm10010e40CfgClientcaiscsfIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 9, 1, 1, 1, 1),
    _Rm10010e40CfgClientcaiscsfIndex_Type()
)
rm10010e40CfgClientcaiscsfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CfgClientcaiscsfIndex.setStatus("current")


class _Rm10010e40CfgReservePortn_Type(Unsigned32):
    """Custom type rm10010e40CfgReservePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010e40CfgReservePortn_Type.__name__ = "Unsigned32"
_Rm10010e40CfgReservePortn_Object = MibTableColumn
rm10010e40CfgReservePortn = _Rm10010e40CfgReservePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 9, 1, 1, 1, 3),
    _Rm10010e40CfgReservePortn_Type()
)
rm10010e40CfgReservePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010e40CfgReservePortn.setStatus("current")
_Rm10010e40CfgStartup_ObjectIdentity = ObjectIdentity
rm10010e40CfgStartup = _Rm10010e40CfgStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 9, 2)
)
_Rm10010e40CfgClientStartupTable_Object = MibTable
rm10010e40CfgClientStartupTable = _Rm10010e40CfgClientStartupTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 9, 2, 1)
)
if mibBuilder.loadTexts:
    rm10010e40CfgClientStartupTable.setStatus("current")
_Rm10010e40CfgClientStartupEntry_Object = MibTableRow
rm10010e40CfgClientStartupEntry = _Rm10010e40CfgClientStartupEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 9, 2, 1, 1)
)
rm10010e40CfgClientStartupEntry.setIndexNames(
    (0, "EKINOPS-Rm10010e40-MIB", "rm10010e40CfgClientStartupIndex"),
)
if mibBuilder.loadTexts:
    rm10010e40CfgClientStartupEntry.setStatus("current")


class _Rm10010e40CfgClientStartupIndex_Type(Integer32):
    """Custom type rm10010e40CfgClientStartupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010e40CfgClientStartupIndex_Type.__name__ = "Integer32"
_Rm10010e40CfgClientStartupIndex_Object = MibTableColumn
rm10010e40CfgClientStartupIndex = _Rm10010e40CfgClientStartupIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 9, 2, 1, 1, 1),
    _Rm10010e40CfgClientStartupIndex_Type()
)
rm10010e40CfgClientStartupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CfgClientStartupIndex.setStatus("current")


class _Rm10010e40CfgSystConfPortPortn_Type(Unsigned32):
    """Custom type rm10010e40CfgSystConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010e40CfgSystConfPortPortn_Type.__name__ = "Unsigned32"
_Rm10010e40CfgSystConfPortPortn_Object = MibTableColumn
rm10010e40CfgSystConfPortPortn = _Rm10010e40CfgSystConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 9, 2, 1, 1, 3),
    _Rm10010e40CfgSystConfPortPortn_Type()
)
rm10010e40CfgSystConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010e40CfgSystConfPortPortn.setStatus("current")


class _Rm10010e40CfgNetConfPortPortn_Type(Unsigned32):
    """Custom type rm10010e40CfgNetConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010e40CfgNetConfPortPortn_Type.__name__ = "Unsigned32"
_Rm10010e40CfgNetConfPortPortn_Object = MibTableColumn
rm10010e40CfgNetConfPortPortn = _Rm10010e40CfgNetConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 9, 2, 1, 1, 4),
    _Rm10010e40CfgNetConfPortPortn_Type()
)
rm10010e40CfgNetConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010e40CfgNetConfPortPortn.setStatus("current")


class _Rm10010e40CfgOptionsPortPortn_Type(Unsigned32):
    """Custom type rm10010e40CfgOptionsPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010e40CfgOptionsPortPortn_Type.__name__ = "Unsigned32"
_Rm10010e40CfgOptionsPortPortn_Object = MibTableColumn
rm10010e40CfgOptionsPortPortn = _Rm10010e40CfgOptionsPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 9, 2, 1, 1, 14),
    _Rm10010e40CfgOptionsPortPortn_Type()
)
rm10010e40CfgOptionsPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010e40CfgOptionsPortPortn.setStatus("current")
_Rm10010e40CfgLineStartupTable_Object = MibTable
rm10010e40CfgLineStartupTable = _Rm10010e40CfgLineStartupTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 9, 2, 2)
)
if mibBuilder.loadTexts:
    rm10010e40CfgLineStartupTable.setStatus("current")
_Rm10010e40CfgLineStartupEntry_Object = MibTableRow
rm10010e40CfgLineStartupEntry = _Rm10010e40CfgLineStartupEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 9, 2, 2, 1)
)
rm10010e40CfgLineStartupEntry.setIndexNames(
    (0, "EKINOPS-Rm10010e40-MIB", "rm10010e40CfgLineStartupIndex"),
)
if mibBuilder.loadTexts:
    rm10010e40CfgLineStartupEntry.setStatus("current")


class _Rm10010e40CfgLineStartupIndex_Type(Integer32):
    """Custom type rm10010e40CfgLineStartupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010e40CfgLineStartupIndex_Type.__name__ = "Integer32"
_Rm10010e40CfgLineStartupIndex_Object = MibTableColumn
rm10010e40CfgLineStartupIndex = _Rm10010e40CfgLineStartupIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 9, 2, 2, 1, 1),
    _Rm10010e40CfgLineStartupIndex_Type()
)
rm10010e40CfgLineStartupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CfgLineStartupIndex.setStatus("current")


class _Rm10010e40CfgSystConfLinePortn_Type(Unsigned32):
    """Custom type rm10010e40CfgSystConfLinePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010e40CfgSystConfLinePortn_Type.__name__ = "Unsigned32"
_Rm10010e40CfgSystConfLinePortn_Object = MibTableColumn
rm10010e40CfgSystConfLinePortn = _Rm10010e40CfgSystConfLinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 9, 2, 2, 1, 3),
    _Rm10010e40CfgSystConfLinePortn_Type()
)
rm10010e40CfgSystConfLinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010e40CfgSystConfLinePortn.setStatus("current")


class _Rm10010e40CfgOptionsLinePortn_Type(Unsigned32):
    """Custom type rm10010e40CfgOptionsLinePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010e40CfgOptionsLinePortn_Type.__name__ = "Unsigned32"
_Rm10010e40CfgOptionsLinePortn_Object = MibTableColumn
rm10010e40CfgOptionsLinePortn = _Rm10010e40CfgOptionsLinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 9, 2, 2, 1, 14),
    _Rm10010e40CfgOptionsLinePortn_Type()
)
rm10010e40CfgOptionsLinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010e40CfgOptionsLinePortn.setStatus("current")
_Rm10010e40CfgXfpTable_Object = MibTable
rm10010e40CfgXfpTable = _Rm10010e40CfgXfpTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 9, 2, 3)
)
if mibBuilder.loadTexts:
    rm10010e40CfgXfpTable.setStatus("current")
_Rm10010e40CfgXfpEntry_Object = MibTableRow
rm10010e40CfgXfpEntry = _Rm10010e40CfgXfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 9, 2, 3, 1)
)
rm10010e40CfgXfpEntry.setIndexNames(
    (0, "EKINOPS-Rm10010e40-MIB", "rm10010e40CfgXfpIndex"),
)
if mibBuilder.loadTexts:
    rm10010e40CfgXfpEntry.setStatus("current")


class _Rm10010e40CfgXfpIndex_Type(Integer32):
    """Custom type rm10010e40CfgXfpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010e40CfgXfpIndex_Type.__name__ = "Integer32"
_Rm10010e40CfgXfpIndex_Object = MibTableColumn
rm10010e40CfgXfpIndex = _Rm10010e40CfgXfpIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 9, 2, 3, 1, 1),
    _Rm10010e40CfgXfpIndex_Type()
)
rm10010e40CfgXfpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CfgXfpIndex.setStatus("current")


class _Rm10010e40CfgSystConfMsaLinePortn_Type(Unsigned32):
    """Custom type rm10010e40CfgSystConfMsaLinePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010e40CfgSystConfMsaLinePortn_Type.__name__ = "Unsigned32"
_Rm10010e40CfgSystConfMsaLinePortn_Object = MibTableColumn
rm10010e40CfgSystConfMsaLinePortn = _Rm10010e40CfgSystConfMsaLinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 9, 2, 3, 1, 3),
    _Rm10010e40CfgSystConfMsaLinePortn_Type()
)
rm10010e40CfgSystConfMsaLinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010e40CfgSystConfMsaLinePortn.setStatus("current")
_Rm10010e40CfgLabels_ObjectIdentity = ObjectIdentity
rm10010e40CfgLabels = _Rm10010e40CfgLabels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 9, 3)
)
_Rm10010e40CfgLabelclientTable_Object = MibTable
rm10010e40CfgLabelclientTable = _Rm10010e40CfgLabelclientTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 9, 3, 1)
)
if mibBuilder.loadTexts:
    rm10010e40CfgLabelclientTable.setStatus("current")
_Rm10010e40CfgLabelclientEntry_Object = MibTableRow
rm10010e40CfgLabelclientEntry = _Rm10010e40CfgLabelclientEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 9, 3, 1, 1)
)
rm10010e40CfgLabelclientEntry.setIndexNames(
    (0, "EKINOPS-Rm10010e40-MIB", "rm10010e40CfgLabelclientIndex"),
)
if mibBuilder.loadTexts:
    rm10010e40CfgLabelclientEntry.setStatus("current")


class _Rm10010e40CfgLabelclientIndex_Type(Integer32):
    """Custom type rm10010e40CfgLabelclientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010e40CfgLabelclientIndex_Type.__name__ = "Integer32"
_Rm10010e40CfgLabelclientIndex_Object = MibTableColumn
rm10010e40CfgLabelclientIndex = _Rm10010e40CfgLabelclientIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 9, 3, 1, 1, 1),
    _Rm10010e40CfgLabelclientIndex_Type()
)
rm10010e40CfgLabelclientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CfgLabelclientIndex.setStatus("current")


class _Rm10010e40CfgLabelclientPortn_Type(DisplayString):
    """Custom type rm10010e40CfgLabelclientPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Rm10010e40CfgLabelclientPortn_Type.__name__ = "DisplayString"
_Rm10010e40CfgLabelclientPortn_Object = MibTableColumn
rm10010e40CfgLabelclientPortn = _Rm10010e40CfgLabelclientPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 9, 3, 1, 1, 3),
    _Rm10010e40CfgLabelclientPortn_Type()
)
rm10010e40CfgLabelclientPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010e40CfgLabelclientPortn.setStatus("current")
_Rm10010e40CfgLabellineTable_Object = MibTable
rm10010e40CfgLabellineTable = _Rm10010e40CfgLabellineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 9, 3, 2)
)
if mibBuilder.loadTexts:
    rm10010e40CfgLabellineTable.setStatus("current")
_Rm10010e40CfgLabellineEntry_Object = MibTableRow
rm10010e40CfgLabellineEntry = _Rm10010e40CfgLabellineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 9, 3, 2, 1)
)
rm10010e40CfgLabellineEntry.setIndexNames(
    (0, "EKINOPS-Rm10010e40-MIB", "rm10010e40CfgLabellineIndex"),
)
if mibBuilder.loadTexts:
    rm10010e40CfgLabellineEntry.setStatus("current")


class _Rm10010e40CfgLabellineIndex_Type(Integer32):
    """Custom type rm10010e40CfgLabellineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010e40CfgLabellineIndex_Type.__name__ = "Integer32"
_Rm10010e40CfgLabellineIndex_Object = MibTableColumn
rm10010e40CfgLabellineIndex = _Rm10010e40CfgLabellineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 9, 3, 2, 1, 1),
    _Rm10010e40CfgLabellineIndex_Type()
)
rm10010e40CfgLabellineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CfgLabellineIndex.setStatus("current")


class _Rm10010e40CfgLabellinePortn_Type(DisplayString):
    """Custom type rm10010e40CfgLabellinePortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Rm10010e40CfgLabellinePortn_Type.__name__ = "DisplayString"
_Rm10010e40CfgLabellinePortn_Object = MibTableColumn
rm10010e40CfgLabellinePortn = _Rm10010e40CfgLabellinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 9, 3, 2, 1, 3),
    _Rm10010e40CfgLabellinePortn_Type()
)
rm10010e40CfgLabellinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010e40CfgLabellinePortn.setStatus("current")
_Rm10010e40CfgStartuptlh_ObjectIdentity = ObjectIdentity
rm10010e40CfgStartuptlh = _Rm10010e40CfgStartuptlh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 9, 4)
)
_Rm10010e40CfgOtxtlhTable_Object = MibTable
rm10010e40CfgOtxtlhTable = _Rm10010e40CfgOtxtlhTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 9, 4, 1)
)
if mibBuilder.loadTexts:
    rm10010e40CfgOtxtlhTable.setStatus("current")
_Rm10010e40CfgOtxtlhEntry_Object = MibTableRow
rm10010e40CfgOtxtlhEntry = _Rm10010e40CfgOtxtlhEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 9, 4, 1, 1)
)
rm10010e40CfgOtxtlhEntry.setIndexNames(
    (0, "EKINOPS-Rm10010e40-MIB", "rm10010e40CfgOtxtlhIndex"),
)
if mibBuilder.loadTexts:
    rm10010e40CfgOtxtlhEntry.setStatus("current")


class _Rm10010e40CfgOtxtlhIndex_Type(Integer32):
    """Custom type rm10010e40CfgOtxtlhIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010e40CfgOtxtlhIndex_Type.__name__ = "Integer32"
_Rm10010e40CfgOtxtlhIndex_Object = MibTableColumn
rm10010e40CfgOtxtlhIndex = _Rm10010e40CfgOtxtlhIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 9, 4, 1, 1, 1),
    _Rm10010e40CfgOtxtlhIndex_Type()
)
rm10010e40CfgOtxtlhIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CfgOtxtlhIndex.setStatus("current")


class _Rm10010e40CfgLinePwrLaserPortn_Type(Unsigned32):
    """Custom type rm10010e40CfgLinePwrLaserPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010e40CfgLinePwrLaserPortn_Type.__name__ = "Unsigned32"
_Rm10010e40CfgLinePwrLaserPortn_Object = MibTableColumn
rm10010e40CfgLinePwrLaserPortn = _Rm10010e40CfgLinePwrLaserPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 9, 4, 1, 1, 6),
    _Rm10010e40CfgLinePwrLaserPortn_Type()
)
rm10010e40CfgLinePwrLaserPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010e40CfgLinePwrLaserPortn.setStatus("current")


class _Rm10010e40CfgLineFCurrentPortn_Type(Unsigned32):
    """Custom type rm10010e40CfgLineFCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010e40CfgLineFCurrentPortn_Type.__name__ = "Unsigned32"
_Rm10010e40CfgLineFCurrentPortn_Object = MibTableColumn
rm10010e40CfgLineFCurrentPortn = _Rm10010e40CfgLineFCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 9, 4, 1, 1, 7),
    _Rm10010e40CfgLineFCurrentPortn_Type()
)
rm10010e40CfgLineFCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010e40CfgLineFCurrentPortn.setStatus("current")


class _Rm10010e40CfgLineGridCurrentPortn_Type(Unsigned32):
    """Custom type rm10010e40CfgLineGridCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010e40CfgLineGridCurrentPortn_Type.__name__ = "Unsigned32"
_Rm10010e40CfgLineGridCurrentPortn_Object = MibTableColumn
rm10010e40CfgLineGridCurrentPortn = _Rm10010e40CfgLineGridCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 9, 4, 1, 1, 8),
    _Rm10010e40CfgLineGridCurrentPortn_Type()
)
rm10010e40CfgLineGridCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010e40CfgLineGridCurrentPortn.setStatus("current")


class _Rm10010e40CfgFPortn_Type(Unsigned32):
    """Custom type rm10010e40CfgFPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010e40CfgFPortn_Type.__name__ = "Unsigned32"
_Rm10010e40CfgFPortn_Object = MibTableColumn
rm10010e40CfgFPortn = _Rm10010e40CfgFPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 9, 4, 1, 1, 9),
    _Rm10010e40CfgFPortn_Type()
)
rm10010e40CfgFPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010e40CfgFPortn.setStatus("current")


class _Rm10010e40CfgRxLineFCurrentPortn_Type(Unsigned32):
    """Custom type rm10010e40CfgRxLineFCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010e40CfgRxLineFCurrentPortn_Type.__name__ = "Unsigned32"
_Rm10010e40CfgRxLineFCurrentPortn_Object = MibTableColumn
rm10010e40CfgRxLineFCurrentPortn = _Rm10010e40CfgRxLineFCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 9, 4, 1, 1, 10),
    _Rm10010e40CfgRxLineFCurrentPortn_Type()
)
rm10010e40CfgRxLineFCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010e40CfgRxLineFCurrentPortn.setStatus("current")
_Rm10010e40CfgOther_ObjectIdentity = ObjectIdentity
rm10010e40CfgOther = _Rm10010e40CfgOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 9, 5)
)
_Rm10010e40tablemoduleOther_ObjectIdentity = ObjectIdentity
rm10010e40tablemoduleOther = _Rm10010e40tablemoduleOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 9, 5, 1)
)


class _Rm10010e40Cfgmode_Type(Unsigned32):
    """Custom type rm10010e40Cfgmode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010e40Cfgmode_Type.__name__ = "Unsigned32"
_Rm10010e40Cfgmode_Object = MibScalar
rm10010e40Cfgmode = _Rm10010e40Cfgmode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 9, 5, 1, 2),
    _Rm10010e40Cfgmode_Type()
)
rm10010e40Cfgmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010e40Cfgmode.setStatus("current")


class _Rm10010e40CfgfanLowSpeedThreshold_Type(Unsigned32):
    """Custom type rm10010e40CfgfanLowSpeedThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010e40CfgfanLowSpeedThreshold_Type.__name__ = "Unsigned32"
_Rm10010e40CfgfanLowSpeedThreshold_Object = MibScalar
rm10010e40CfgfanLowSpeedThreshold = _Rm10010e40CfgfanLowSpeedThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 9, 5, 1, 3),
    _Rm10010e40CfgfanLowSpeedThreshold_Type()
)
rm10010e40CfgfanLowSpeedThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010e40CfgfanLowSpeedThreshold.setStatus("current")


class _Rm10010e40CfgfanHighSpeedThreshold_Type(Unsigned32):
    """Custom type rm10010e40CfgfanHighSpeedThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010e40CfgfanHighSpeedThreshold_Type.__name__ = "Unsigned32"
_Rm10010e40CfgfanHighSpeedThreshold_Object = MibScalar
rm10010e40CfgfanHighSpeedThreshold = _Rm10010e40CfgfanHighSpeedThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 9, 5, 1, 4),
    _Rm10010e40CfgfanHighSpeedThreshold_Type()
)
rm10010e40CfgfanHighSpeedThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010e40CfgfanHighSpeedThreshold.setStatus("current")
_Rm10010e40CfgStartuptablefive_ObjectIdentity = ObjectIdentity
rm10010e40CfgStartuptablefive = _Rm10010e40CfgStartuptablefive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 9, 6)
)
_Rm10010e40CfgOtxtlhcapabilitiesTable_Object = MibTable
rm10010e40CfgOtxtlhcapabilitiesTable = _Rm10010e40CfgOtxtlhcapabilitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 9, 6, 1)
)
if mibBuilder.loadTexts:
    rm10010e40CfgOtxtlhcapabilitiesTable.setStatus("current")
_Rm10010e40CfgOtxtlhcapabilitiesEntry_Object = MibTableRow
rm10010e40CfgOtxtlhcapabilitiesEntry = _Rm10010e40CfgOtxtlhcapabilitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 9, 6, 1, 1)
)
rm10010e40CfgOtxtlhcapabilitiesEntry.setIndexNames(
    (0, "EKINOPS-Rm10010e40-MIB", "rm10010e40CfgOtxtlhcapabilitiesIndex"),
)
if mibBuilder.loadTexts:
    rm10010e40CfgOtxtlhcapabilitiesEntry.setStatus("current")


class _Rm10010e40CfgOtxtlhcapabilitiesIndex_Type(Integer32):
    """Custom type rm10010e40CfgOtxtlhcapabilitiesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010e40CfgOtxtlhcapabilitiesIndex_Type.__name__ = "Integer32"
_Rm10010e40CfgOtxtlhcapabilitiesIndex_Object = MibTableColumn
rm10010e40CfgOtxtlhcapabilitiesIndex = _Rm10010e40CfgOtxtlhcapabilitiesIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 9, 6, 1, 1, 1),
    _Rm10010e40CfgOtxtlhcapabilitiesIndex_Type()
)
rm10010e40CfgOtxtlhcapabilitiesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CfgOtxtlhcapabilitiesIndex.setStatus("current")


class _Rm10010e40CfgComponentTypePortn_Type(Unsigned32):
    """Custom type rm10010e40CfgComponentTypePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010e40CfgComponentTypePortn_Type.__name__ = "Unsigned32"
_Rm10010e40CfgComponentTypePortn_Object = MibTableColumn
rm10010e40CfgComponentTypePortn = _Rm10010e40CfgComponentTypePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 9, 6, 1, 1, 3),
    _Rm10010e40CfgComponentTypePortn_Type()
)
rm10010e40CfgComponentTypePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CfgComponentTypePortn.setStatus("current")


class _Rm10010e40CfgMiscellaneousPortn_Type(Unsigned32):
    """Custom type rm10010e40CfgMiscellaneousPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010e40CfgMiscellaneousPortn_Type.__name__ = "Unsigned32"
_Rm10010e40CfgMiscellaneousPortn_Object = MibTableColumn
rm10010e40CfgMiscellaneousPortn = _Rm10010e40CfgMiscellaneousPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 9, 6, 1, 1, 4),
    _Rm10010e40CfgMiscellaneousPortn_Type()
)
rm10010e40CfgMiscellaneousPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CfgMiscellaneousPortn.setStatus("current")


class _Rm10010e40CfgFirstChannelPortn_Type(Unsigned32):
    """Custom type rm10010e40CfgFirstChannelPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010e40CfgFirstChannelPortn_Type.__name__ = "Unsigned32"
_Rm10010e40CfgFirstChannelPortn_Object = MibTableColumn
rm10010e40CfgFirstChannelPortn = _Rm10010e40CfgFirstChannelPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 9, 6, 1, 1, 5),
    _Rm10010e40CfgFirstChannelPortn_Type()
)
rm10010e40CfgFirstChannelPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CfgFirstChannelPortn.setStatus("current")


class _Rm10010e40CfgLastChannelPortn_Type(Unsigned32):
    """Custom type rm10010e40CfgLastChannelPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010e40CfgLastChannelPortn_Type.__name__ = "Unsigned32"
_Rm10010e40CfgLastChannelPortn_Object = MibTableColumn
rm10010e40CfgLastChannelPortn = _Rm10010e40CfgLastChannelPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 9, 6, 1, 1, 6),
    _Rm10010e40CfgLastChannelPortn_Type()
)
rm10010e40CfgLastChannelPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CfgLastChannelPortn.setStatus("current")


class _Rm10010e40CfgGridPortn_Type(Unsigned32):
    """Custom type rm10010e40CfgGridPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010e40CfgGridPortn_Type.__name__ = "Unsigned32"
_Rm10010e40CfgGridPortn_Object = MibTableColumn
rm10010e40CfgGridPortn = _Rm10010e40CfgGridPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 9, 6, 1, 1, 7),
    _Rm10010e40CfgGridPortn_Type()
)
rm10010e40CfgGridPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40CfgGridPortn.setStatus("current")
_Rm10010e40CfgWriteConfiguration_Type = EkiOnOff
_Rm10010e40CfgWriteConfiguration_Object = MibScalar
rm10010e40CfgWriteConfiguration = _Rm10010e40CfgWriteConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 9, 257),
    _Rm10010e40CfgWriteConfiguration_Type()
)
rm10010e40CfgWriteConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010e40CfgWriteConfiguration.setStatus("current")
_Rm10010e40traps_ObjectIdentity = ObjectIdentity
rm10010e40traps = _Rm10010e40traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 10)
)


class _Rm10010e40trapPortNumber_Type(Integer32):
    """Custom type rm10010e40trapPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Rm10010e40trapPortNumber_Type.__name__ = "Integer32"
_Rm10010e40trapPortNumber_Object = MibScalar
rm10010e40trapPortNumber = _Rm10010e40trapPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 10, 2),
    _Rm10010e40trapPortNumber_Type()
)
rm10010e40trapPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40trapPortNumber.setStatus("current")


class _Rm10010e40trapLineNumber_Type(Integer32):
    """Custom type rm10010e40trapLineNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Rm10010e40trapLineNumber_Type.__name__ = "Integer32"
_Rm10010e40trapLineNumber_Object = MibScalar
rm10010e40trapLineNumber = _Rm10010e40trapLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 10, 3),
    _Rm10010e40trapLineNumber_Type()
)
rm10010e40trapLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40trapLineNumber.setStatus("current")


class _Rm10010e40trapBoardNumber_Type(Integer32):
    """Custom type rm10010e40trapBoardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Rm10010e40trapBoardNumber_Type.__name__ = "Integer32"
_Rm10010e40trapBoardNumber_Object = MibScalar
rm10010e40trapBoardNumber = _Rm10010e40trapBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 10, 4),
    _Rm10010e40trapBoardNumber_Type()
)
rm10010e40trapBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40trapBoardNumber.setStatus("current")
_Rm10010e40Monitoring_ObjectIdentity = ObjectIdentity
rm10010e40Monitoring = _Rm10010e40Monitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 11)
)
_Rm10010e40MonOther_ObjectIdentity = ObjectIdentity
rm10010e40MonOther = _Rm10010e40MonOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 11, 1)
)
_Rm10010e40MonRmon_ObjectIdentity = ObjectIdentity
rm10010e40MonRmon = _Rm10010e40MonRmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 11, 1, 3)
)
_Rm10010e40MonClient_ObjectIdentity = ObjectIdentity
rm10010e40MonClient = _Rm10010e40MonClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 11, 2)
)
_Rm10010e40MonClientRmonCounter_ObjectIdentity = ObjectIdentity
rm10010e40MonClientRmonCounter = _Rm10010e40MonClientRmonCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 57, 11, 2, 4)
)
_Rm10010e40MonupRmonBytesCounterClientInputTable_Object = MibTable
rm10010e40MonupRmonBytesCounterClientInputTable = _Rm10010e40MonupRmonBytesCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 11, 2, 4, 16)
)
if mibBuilder.loadTexts:
    rm10010e40MonupRmonBytesCounterClientInputTable.setStatus("current")
_Rm10010e40MonupRmonBytesCounterClientInputEntry_Object = MibTableRow
rm10010e40MonupRmonBytesCounterClientInputEntry = _Rm10010e40MonupRmonBytesCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 11, 2, 4, 16, 1)
)
rm10010e40MonupRmonBytesCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Rm10010e40-MIB", "rm10010e40MonupRmonBytesCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    rm10010e40MonupRmonBytesCounterClientInputEntry.setStatus("current")


class _Rm10010e40MonupRmonBytesCounterClientInputIndex_Type(Integer32):
    """Custom type rm10010e40MonupRmonBytesCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010e40MonupRmonBytesCounterClientInputIndex_Type.__name__ = "Integer32"
_Rm10010e40MonupRmonBytesCounterClientInputIndex_Object = MibTableColumn
rm10010e40MonupRmonBytesCounterClientInputIndex = _Rm10010e40MonupRmonBytesCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 11, 2, 4, 16, 1, 1),
    _Rm10010e40MonupRmonBytesCounterClientInputIndex_Type()
)
rm10010e40MonupRmonBytesCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MonupRmonBytesCounterClientInputIndex.setStatus("current")
_Rm10010e40MonupRmonBytesCounterClientInputValuePortn_Type = Counter64
_Rm10010e40MonupRmonBytesCounterClientInputValuePortn_Object = MibTableColumn
rm10010e40MonupRmonBytesCounterClientInputValuePortn = _Rm10010e40MonupRmonBytesCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 11, 2, 4, 16, 1, 2),
    _Rm10010e40MonupRmonBytesCounterClientInputValuePortn_Type()
)
rm10010e40MonupRmonBytesCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MonupRmonBytesCounterClientInputValuePortn.setStatus("current")
_Rm10010e40MonupRmonBytesCounterClientInputErrorPortn_Type = EkiOnOff
_Rm10010e40MonupRmonBytesCounterClientInputErrorPortn_Object = MibTableColumn
rm10010e40MonupRmonBytesCounterClientInputErrorPortn = _Rm10010e40MonupRmonBytesCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 11, 2, 4, 16, 1, 3),
    _Rm10010e40MonupRmonBytesCounterClientInputErrorPortn_Type()
)
rm10010e40MonupRmonBytesCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MonupRmonBytesCounterClientInputErrorPortn.setStatus("current")
_Rm10010e40MonupRmonBytesCounterClientInputOverloadPortn_Type = EkiOnOff
_Rm10010e40MonupRmonBytesCounterClientInputOverloadPortn_Object = MibTableColumn
rm10010e40MonupRmonBytesCounterClientInputOverloadPortn = _Rm10010e40MonupRmonBytesCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 11, 2, 4, 16, 1, 4),
    _Rm10010e40MonupRmonBytesCounterClientInputOverloadPortn_Type()
)
rm10010e40MonupRmonBytesCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MonupRmonBytesCounterClientInputOverloadPortn.setStatus("current")
_Rm10010e40MonupRmonCrcErrorsCounterClientInputTable_Object = MibTable
rm10010e40MonupRmonCrcErrorsCounterClientInputTable = _Rm10010e40MonupRmonCrcErrorsCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 11, 2, 4, 32)
)
if mibBuilder.loadTexts:
    rm10010e40MonupRmonCrcErrorsCounterClientInputTable.setStatus("current")
_Rm10010e40MonupRmonCrcErrorsCounterClientInputEntry_Object = MibTableRow
rm10010e40MonupRmonCrcErrorsCounterClientInputEntry = _Rm10010e40MonupRmonCrcErrorsCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 11, 2, 4, 32, 1)
)
rm10010e40MonupRmonCrcErrorsCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Rm10010e40-MIB", "rm10010e40MonupRmonCrcErrorsCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    rm10010e40MonupRmonCrcErrorsCounterClientInputEntry.setStatus("current")


class _Rm10010e40MonupRmonCrcErrorsCounterClientInputIndex_Type(Integer32):
    """Custom type rm10010e40MonupRmonCrcErrorsCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010e40MonupRmonCrcErrorsCounterClientInputIndex_Type.__name__ = "Integer32"
_Rm10010e40MonupRmonCrcErrorsCounterClientInputIndex_Object = MibTableColumn
rm10010e40MonupRmonCrcErrorsCounterClientInputIndex = _Rm10010e40MonupRmonCrcErrorsCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 11, 2, 4, 32, 1, 1),
    _Rm10010e40MonupRmonCrcErrorsCounterClientInputIndex_Type()
)
rm10010e40MonupRmonCrcErrorsCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MonupRmonCrcErrorsCounterClientInputIndex.setStatus("current")
_Rm10010e40MonupRmonCrcErrorsCounterClientInputValuePortn_Type = Counter64
_Rm10010e40MonupRmonCrcErrorsCounterClientInputValuePortn_Object = MibTableColumn
rm10010e40MonupRmonCrcErrorsCounterClientInputValuePortn = _Rm10010e40MonupRmonCrcErrorsCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 11, 2, 4, 32, 1, 2),
    _Rm10010e40MonupRmonCrcErrorsCounterClientInputValuePortn_Type()
)
rm10010e40MonupRmonCrcErrorsCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MonupRmonCrcErrorsCounterClientInputValuePortn.setStatus("current")
_Rm10010e40MonupRmonCrcErrorsCounterClientInputErrorPortn_Type = EkiOnOff
_Rm10010e40MonupRmonCrcErrorsCounterClientInputErrorPortn_Object = MibTableColumn
rm10010e40MonupRmonCrcErrorsCounterClientInputErrorPortn = _Rm10010e40MonupRmonCrcErrorsCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 11, 2, 4, 32, 1, 3),
    _Rm10010e40MonupRmonCrcErrorsCounterClientInputErrorPortn_Type()
)
rm10010e40MonupRmonCrcErrorsCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MonupRmonCrcErrorsCounterClientInputErrorPortn.setStatus("current")
_Rm10010e40MonupRmonCrcErrorsCounterClientInputOverloadPortn_Type = EkiOnOff
_Rm10010e40MonupRmonCrcErrorsCounterClientInputOverloadPortn_Object = MibTableColumn
rm10010e40MonupRmonCrcErrorsCounterClientInputOverloadPortn = _Rm10010e40MonupRmonCrcErrorsCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 11, 2, 4, 32, 1, 4),
    _Rm10010e40MonupRmonCrcErrorsCounterClientInputOverloadPortn_Type()
)
rm10010e40MonupRmonCrcErrorsCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MonupRmonCrcErrorsCounterClientInputOverloadPortn.setStatus("current")
_Rm10010e40MonupRmonPacketsCounterClientInputTable_Object = MibTable
rm10010e40MonupRmonPacketsCounterClientInputTable = _Rm10010e40MonupRmonPacketsCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 11, 2, 4, 48)
)
if mibBuilder.loadTexts:
    rm10010e40MonupRmonPacketsCounterClientInputTable.setStatus("current")
_Rm10010e40MonupRmonPacketsCounterClientInputEntry_Object = MibTableRow
rm10010e40MonupRmonPacketsCounterClientInputEntry = _Rm10010e40MonupRmonPacketsCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 11, 2, 4, 48, 1)
)
rm10010e40MonupRmonPacketsCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Rm10010e40-MIB", "rm10010e40MonupRmonPacketsCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    rm10010e40MonupRmonPacketsCounterClientInputEntry.setStatus("current")


class _Rm10010e40MonupRmonPacketsCounterClientInputIndex_Type(Integer32):
    """Custom type rm10010e40MonupRmonPacketsCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010e40MonupRmonPacketsCounterClientInputIndex_Type.__name__ = "Integer32"
_Rm10010e40MonupRmonPacketsCounterClientInputIndex_Object = MibTableColumn
rm10010e40MonupRmonPacketsCounterClientInputIndex = _Rm10010e40MonupRmonPacketsCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 11, 2, 4, 48, 1, 1),
    _Rm10010e40MonupRmonPacketsCounterClientInputIndex_Type()
)
rm10010e40MonupRmonPacketsCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MonupRmonPacketsCounterClientInputIndex.setStatus("current")
_Rm10010e40MonupRmonPacketsCounterClientInputValuePortn_Type = Counter64
_Rm10010e40MonupRmonPacketsCounterClientInputValuePortn_Object = MibTableColumn
rm10010e40MonupRmonPacketsCounterClientInputValuePortn = _Rm10010e40MonupRmonPacketsCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 11, 2, 4, 48, 1, 2),
    _Rm10010e40MonupRmonPacketsCounterClientInputValuePortn_Type()
)
rm10010e40MonupRmonPacketsCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MonupRmonPacketsCounterClientInputValuePortn.setStatus("current")
_Rm10010e40MonupRmonPacketsCounterClientInputErrorPortn_Type = EkiOnOff
_Rm10010e40MonupRmonPacketsCounterClientInputErrorPortn_Object = MibTableColumn
rm10010e40MonupRmonPacketsCounterClientInputErrorPortn = _Rm10010e40MonupRmonPacketsCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 11, 2, 4, 48, 1, 3),
    _Rm10010e40MonupRmonPacketsCounterClientInputErrorPortn_Type()
)
rm10010e40MonupRmonPacketsCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MonupRmonPacketsCounterClientInputErrorPortn.setStatus("current")
_Rm10010e40MonupRmonPacketsCounterClientInputOverloadPortn_Type = EkiOnOff
_Rm10010e40MonupRmonPacketsCounterClientInputOverloadPortn_Object = MibTableColumn
rm10010e40MonupRmonPacketsCounterClientInputOverloadPortn = _Rm10010e40MonupRmonPacketsCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 11, 2, 4, 48, 1, 4),
    _Rm10010e40MonupRmonPacketsCounterClientInputOverloadPortn_Type()
)
rm10010e40MonupRmonPacketsCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MonupRmonPacketsCounterClientInputOverloadPortn.setStatus("current")
_Rm10010e40MonupRmonBroadcastCounterClientInputTable_Object = MibTable
rm10010e40MonupRmonBroadcastCounterClientInputTable = _Rm10010e40MonupRmonBroadcastCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 11, 2, 4, 64)
)
if mibBuilder.loadTexts:
    rm10010e40MonupRmonBroadcastCounterClientInputTable.setStatus("current")
_Rm10010e40MonupRmonBroadcastCounterClientInputEntry_Object = MibTableRow
rm10010e40MonupRmonBroadcastCounterClientInputEntry = _Rm10010e40MonupRmonBroadcastCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 11, 2, 4, 64, 1)
)
rm10010e40MonupRmonBroadcastCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Rm10010e40-MIB", "rm10010e40MonupRmonBroadcastCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    rm10010e40MonupRmonBroadcastCounterClientInputEntry.setStatus("current")


class _Rm10010e40MonupRmonBroadcastCounterClientInputIndex_Type(Integer32):
    """Custom type rm10010e40MonupRmonBroadcastCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010e40MonupRmonBroadcastCounterClientInputIndex_Type.__name__ = "Integer32"
_Rm10010e40MonupRmonBroadcastCounterClientInputIndex_Object = MibTableColumn
rm10010e40MonupRmonBroadcastCounterClientInputIndex = _Rm10010e40MonupRmonBroadcastCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 11, 2, 4, 64, 1, 1),
    _Rm10010e40MonupRmonBroadcastCounterClientInputIndex_Type()
)
rm10010e40MonupRmonBroadcastCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MonupRmonBroadcastCounterClientInputIndex.setStatus("current")
_Rm10010e40MonupRmonBroadcastCounterClientInputValuePortn_Type = Counter64
_Rm10010e40MonupRmonBroadcastCounterClientInputValuePortn_Object = MibTableColumn
rm10010e40MonupRmonBroadcastCounterClientInputValuePortn = _Rm10010e40MonupRmonBroadcastCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 11, 2, 4, 64, 1, 2),
    _Rm10010e40MonupRmonBroadcastCounterClientInputValuePortn_Type()
)
rm10010e40MonupRmonBroadcastCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MonupRmonBroadcastCounterClientInputValuePortn.setStatus("current")
_Rm10010e40MonupRmonBroadcastCounterClientInputErrorPortn_Type = EkiOnOff
_Rm10010e40MonupRmonBroadcastCounterClientInputErrorPortn_Object = MibTableColumn
rm10010e40MonupRmonBroadcastCounterClientInputErrorPortn = _Rm10010e40MonupRmonBroadcastCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 11, 2, 4, 64, 1, 3),
    _Rm10010e40MonupRmonBroadcastCounterClientInputErrorPortn_Type()
)
rm10010e40MonupRmonBroadcastCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MonupRmonBroadcastCounterClientInputErrorPortn.setStatus("current")
_Rm10010e40MonupRmonBroadcastCounterClientInputOverloadPortn_Type = EkiOnOff
_Rm10010e40MonupRmonBroadcastCounterClientInputOverloadPortn_Object = MibTableColumn
rm10010e40MonupRmonBroadcastCounterClientInputOverloadPortn = _Rm10010e40MonupRmonBroadcastCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 11, 2, 4, 64, 1, 4),
    _Rm10010e40MonupRmonBroadcastCounterClientInputOverloadPortn_Type()
)
rm10010e40MonupRmonBroadcastCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MonupRmonBroadcastCounterClientInputOverloadPortn.setStatus("current")
_Rm10010e40MonupRmonMulticastCounterClientInputTable_Object = MibTable
rm10010e40MonupRmonMulticastCounterClientInputTable = _Rm10010e40MonupRmonMulticastCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 11, 2, 4, 80)
)
if mibBuilder.loadTexts:
    rm10010e40MonupRmonMulticastCounterClientInputTable.setStatus("current")
_Rm10010e40MonupRmonMulticastCounterClientInputEntry_Object = MibTableRow
rm10010e40MonupRmonMulticastCounterClientInputEntry = _Rm10010e40MonupRmonMulticastCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 11, 2, 4, 80, 1)
)
rm10010e40MonupRmonMulticastCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Rm10010e40-MIB", "rm10010e40MonupRmonMulticastCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    rm10010e40MonupRmonMulticastCounterClientInputEntry.setStatus("current")


class _Rm10010e40MonupRmonMulticastCounterClientInputIndex_Type(Integer32):
    """Custom type rm10010e40MonupRmonMulticastCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010e40MonupRmonMulticastCounterClientInputIndex_Type.__name__ = "Integer32"
_Rm10010e40MonupRmonMulticastCounterClientInputIndex_Object = MibTableColumn
rm10010e40MonupRmonMulticastCounterClientInputIndex = _Rm10010e40MonupRmonMulticastCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 11, 2, 4, 80, 1, 1),
    _Rm10010e40MonupRmonMulticastCounterClientInputIndex_Type()
)
rm10010e40MonupRmonMulticastCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MonupRmonMulticastCounterClientInputIndex.setStatus("current")
_Rm10010e40MonupRmonMulticastCounterClientInputValuePortn_Type = Counter64
_Rm10010e40MonupRmonMulticastCounterClientInputValuePortn_Object = MibTableColumn
rm10010e40MonupRmonMulticastCounterClientInputValuePortn = _Rm10010e40MonupRmonMulticastCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 11, 2, 4, 80, 1, 2),
    _Rm10010e40MonupRmonMulticastCounterClientInputValuePortn_Type()
)
rm10010e40MonupRmonMulticastCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MonupRmonMulticastCounterClientInputValuePortn.setStatus("current")
_Rm10010e40MonupRmonMulticastCounterClientInputErrorPortn_Type = EkiOnOff
_Rm10010e40MonupRmonMulticastCounterClientInputErrorPortn_Object = MibTableColumn
rm10010e40MonupRmonMulticastCounterClientInputErrorPortn = _Rm10010e40MonupRmonMulticastCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 11, 2, 4, 80, 1, 3),
    _Rm10010e40MonupRmonMulticastCounterClientInputErrorPortn_Type()
)
rm10010e40MonupRmonMulticastCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MonupRmonMulticastCounterClientInputErrorPortn.setStatus("current")
_Rm10010e40MonupRmonMulticastCounterClientInputOverloadPortn_Type = EkiOnOff
_Rm10010e40MonupRmonMulticastCounterClientInputOverloadPortn_Object = MibTableColumn
rm10010e40MonupRmonMulticastCounterClientInputOverloadPortn = _Rm10010e40MonupRmonMulticastCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 11, 2, 4, 80, 1, 4),
    _Rm10010e40MonupRmonMulticastCounterClientInputOverloadPortn_Type()
)
rm10010e40MonupRmonMulticastCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MonupRmonMulticastCounterClientInputOverloadPortn.setStatus("current")
_Rm10010e40MonupRmonPauseFrameCounterClientInputTable_Object = MibTable
rm10010e40MonupRmonPauseFrameCounterClientInputTable = _Rm10010e40MonupRmonPauseFrameCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 11, 2, 4, 96)
)
if mibBuilder.loadTexts:
    rm10010e40MonupRmonPauseFrameCounterClientInputTable.setStatus("current")
_Rm10010e40MonupRmonPauseFrameCounterClientInputEntry_Object = MibTableRow
rm10010e40MonupRmonPauseFrameCounterClientInputEntry = _Rm10010e40MonupRmonPauseFrameCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 11, 2, 4, 96, 1)
)
rm10010e40MonupRmonPauseFrameCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Rm10010e40-MIB", "rm10010e40MonupRmonPauseFrameCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    rm10010e40MonupRmonPauseFrameCounterClientInputEntry.setStatus("current")


class _Rm10010e40MonupRmonPauseFrameCounterClientInputIndex_Type(Integer32):
    """Custom type rm10010e40MonupRmonPauseFrameCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010e40MonupRmonPauseFrameCounterClientInputIndex_Type.__name__ = "Integer32"
_Rm10010e40MonupRmonPauseFrameCounterClientInputIndex_Object = MibTableColumn
rm10010e40MonupRmonPauseFrameCounterClientInputIndex = _Rm10010e40MonupRmonPauseFrameCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 11, 2, 4, 96, 1, 1),
    _Rm10010e40MonupRmonPauseFrameCounterClientInputIndex_Type()
)
rm10010e40MonupRmonPauseFrameCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MonupRmonPauseFrameCounterClientInputIndex.setStatus("current")
_Rm10010e40MonupRmonPauseFrameCounterClientInputValuePortn_Type = Counter64
_Rm10010e40MonupRmonPauseFrameCounterClientInputValuePortn_Object = MibTableColumn
rm10010e40MonupRmonPauseFrameCounterClientInputValuePortn = _Rm10010e40MonupRmonPauseFrameCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 11, 2, 4, 96, 1, 2),
    _Rm10010e40MonupRmonPauseFrameCounterClientInputValuePortn_Type()
)
rm10010e40MonupRmonPauseFrameCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MonupRmonPauseFrameCounterClientInputValuePortn.setStatus("current")
_Rm10010e40MonupRmonPauseFrameCounterClientInputErrorPortn_Type = EkiOnOff
_Rm10010e40MonupRmonPauseFrameCounterClientInputErrorPortn_Object = MibTableColumn
rm10010e40MonupRmonPauseFrameCounterClientInputErrorPortn = _Rm10010e40MonupRmonPauseFrameCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 11, 2, 4, 96, 1, 3),
    _Rm10010e40MonupRmonPauseFrameCounterClientInputErrorPortn_Type()
)
rm10010e40MonupRmonPauseFrameCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MonupRmonPauseFrameCounterClientInputErrorPortn.setStatus("current")
_Rm10010e40MonupRmonPauseFrameCounterClientInputOverloadPortn_Type = EkiOnOff
_Rm10010e40MonupRmonPauseFrameCounterClientInputOverloadPortn_Object = MibTableColumn
rm10010e40MonupRmonPauseFrameCounterClientInputOverloadPortn = _Rm10010e40MonupRmonPauseFrameCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 57, 11, 2, 4, 96, 1, 4),
    _Rm10010e40MonupRmonPauseFrameCounterClientInputOverloadPortn_Type()
)
rm10010e40MonupRmonPauseFrameCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010e40MonupRmonPauseFrameCounterClientInputOverloadPortn.setStatus("current")

# Managed Objects groups


# Notification objects

rm10010e40LineTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 57, 10, 30)
)
rm10010e40LineTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Rm10010e40-MIB", "rm10010e40AlmLineDdmWarningPortn"),
        ("EKINOPS-Rm10010e40-MIB", "rm10010e40trapLineNumber"),
        ("EKINOPS-Rm10010e40-MIB", "rm10010e40trapBoardNumber"))
)
if mibBuilder.loadTexts:
    rm10010e40LineTrapNotUrgentGoesOn.setStatus(
        "current"
    )

rm10010e40LineTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 57, 10, 31)
)
rm10010e40LineTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Rm10010e40-MIB", "rm10010e40AlmLineDdmWarningPortn"),
        ("EKINOPS-Rm10010e40-MIB", "rm10010e40trapLineNumber"),
        ("EKINOPS-Rm10010e40-MIB", "rm10010e40trapBoardNumber"))
)
if mibBuilder.loadTexts:
    rm10010e40LineTrapNotUrgentGoesOff.setStatus(
        "current"
    )

rm10010e40LineTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 57, 10, 32)
)
rm10010e40LineTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Rm10010e40-MIB", "rm10010e40AlmLineDdmAlmPortn"),
        ("EKINOPS-Rm10010e40-MIB", "rm10010e40trapLineNumber"),
        ("EKINOPS-Rm10010e40-MIB", "rm10010e40trapBoardNumber"))
)
if mibBuilder.loadTexts:
    rm10010e40LineTrapUrgentGoesOn.setStatus(
        "current"
    )

rm10010e40LineTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 57, 10, 33)
)
rm10010e40LineTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Rm10010e40-MIB", "rm10010e40AlmLineDdmAlmPortn"),
        ("EKINOPS-Rm10010e40-MIB", "rm10010e40trapLineNumber"),
        ("EKINOPS-Rm10010e40-MIB", "rm10010e40trapBoardNumber"))
)
if mibBuilder.loadTexts:
    rm10010e40LineTrapUrgentGoesOff.setStatus(
        "current"
    )

rm10010e40LineTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 57, 10, 34)
)
rm10010e40LineTrapCritGoesOn.setObjects(
      *(("EKINOPS-Rm10010e40-MIB", "rm10010e40AlmLineFailPortn"),
        ("EKINOPS-Rm10010e40-MIB", "rm10010e40AlmLineHwFailPortn"),
        ("EKINOPS-Rm10010e40-MIB", "rm10010e40trapLineNumber"),
        ("EKINOPS-Rm10010e40-MIB", "rm10010e40trapBoardNumber"))
)
if mibBuilder.loadTexts:
    rm10010e40LineTrapCritGoesOn.setStatus(
        "current"
    )

rm10010e40LineTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 57, 10, 35)
)
rm10010e40LineTrapCritGoesOff.setObjects(
      *(("EKINOPS-Rm10010e40-MIB", "rm10010e40AlmLineFailPortn"),
        ("EKINOPS-Rm10010e40-MIB", "rm10010e40AlmLineHwFailPortn"),
        ("EKINOPS-Rm10010e40-MIB", "rm10010e40trapLineNumber"),
        ("EKINOPS-Rm10010e40-MIB", "rm10010e40trapBoardNumber"))
)
if mibBuilder.loadTexts:
    rm10010e40LineTrapCritGoesOff.setStatus(
        "current"
    )

rm10010e40ClientTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 57, 10, 40)
)
rm10010e40ClientTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Rm10010e40-MIB", "rm10010e40AlmSfpDdmWarningPortn"),
        ("EKINOPS-Rm10010e40-MIB", "rm10010e40trapPortNumber"),
        ("EKINOPS-Rm10010e40-MIB", "rm10010e40trapBoardNumber"))
)
if mibBuilder.loadTexts:
    rm10010e40ClientTrapNotUrgentGoesOn.setStatus(
        "current"
    )

rm10010e40ClientTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 57, 10, 41)
)
rm10010e40ClientTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Rm10010e40-MIB", "rm10010e40AlmSfpDdmWarningPortn"),
        ("EKINOPS-Rm10010e40-MIB", "rm10010e40trapPortNumber"),
        ("EKINOPS-Rm10010e40-MIB", "rm10010e40trapBoardNumber"))
)
if mibBuilder.loadTexts:
    rm10010e40ClientTrapNotUrgentGoesOff.setStatus(
        "current"
    )

rm10010e40ClientTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 57, 10, 42)
)
rm10010e40ClientTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Rm10010e40-MIB", "rm10010e40AlmSfpDdmAlmPortn"),
        ("EKINOPS-Rm10010e40-MIB", "rm10010e40trapPortNumber"),
        ("EKINOPS-Rm10010e40-MIB", "rm10010e40trapBoardNumber"))
)
if mibBuilder.loadTexts:
    rm10010e40ClientTrapUrgentGoesOn.setStatus(
        "current"
    )

rm10010e40ClientTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 57, 10, 43)
)
rm10010e40ClientTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Rm10010e40-MIB", "rm10010e40AlmSfpDdmAlmPortn"),
        ("EKINOPS-Rm10010e40-MIB", "rm10010e40trapPortNumber"),
        ("EKINOPS-Rm10010e40-MIB", "rm10010e40trapBoardNumber"))
)
if mibBuilder.loadTexts:
    rm10010e40ClientTrapUrgentGoesOff.setStatus(
        "current"
    )

rm10010e40ClientTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 57, 10, 44)
)
rm10010e40ClientTrapCritGoesOn.setObjects(
      *(("EKINOPS-Rm10010e40-MIB", "rm10010e40AlmFailAccPortn"),
        ("EKINOPS-Rm10010e40-MIB", "rm10010e40AlmHwFailAccPortn"),
        ("EKINOPS-Rm10010e40-MIB", "rm10010e40trapPortNumber"),
        ("EKINOPS-Rm10010e40-MIB", "rm10010e40trapBoardNumber"))
)
if mibBuilder.loadTexts:
    rm10010e40ClientTrapCritGoesOn.setStatus(
        "current"
    )

rm10010e40ClientTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 57, 10, 45)
)
rm10010e40ClientTrapCritGoesOff.setObjects(
      *(("EKINOPS-Rm10010e40-MIB", "rm10010e40AlmFailAccPortn"),
        ("EKINOPS-Rm10010e40-MIB", "rm10010e40AlmHwFailAccPortn"),
        ("EKINOPS-Rm10010e40-MIB", "rm10010e40trapPortNumber"),
        ("EKINOPS-Rm10010e40-MIB", "rm10010e40trapBoardNumber"))
)
if mibBuilder.loadTexts:
    rm10010e40ClientTrapCritGoesOff.setStatus(
        "current"
    )

rm10010e40PowerTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 57, 10, 50)
)
rm10010e40PowerTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Rm10010e40-MIB", "rm10010e40AlmDefFuseB"),
        ("EKINOPS-Rm10010e40-MIB", "rm10010e40AlmDefFuseA"),
        ("EKINOPS-Rm10010e40-MIB", "rm10010e40trapBoardNumber"))
)
if mibBuilder.loadTexts:
    rm10010e40PowerTrapUrgentGoesOn.setStatus(
        "current"
    )

rm10010e40PowerTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 57, 10, 51)
)
rm10010e40PowerTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Rm10010e40-MIB", "rm10010e40AlmDefFuseB"),
        ("EKINOPS-Rm10010e40-MIB", "rm10010e40AlmDefFuseA"),
        ("EKINOPS-Rm10010e40-MIB", "rm10010e40trapBoardNumber"))
)
if mibBuilder.loadTexts:
    rm10010e40PowerTrapUrgentGoesOff.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EKINOPS-Rm10010e40-MIB",
    **{"Rm10010e40MultiRate": Rm10010e40MultiRate,
       "Rm10010e40OtxMode": Rm10010e40OtxMode,
       "Rm10010e40OtxGrid": Rm10010e40OtxGrid,
       "Rm10010e40AdjustValue": Rm10010e40AdjustValue,
       "Rm10010e40ClientProtocol": Rm10010e40ClientProtocol,
       "Rm10010e40ProtocolMode": Rm10010e40ProtocolMode,
       "Rm10010e40OtxChannel": Rm10010e40OtxChannel,
       "Rm10010e40OrxChannel": Rm10010e40OrxChannel,
       "moduleRm10010e40": moduleRm10010e40,
       "rm10010e40alarms": rm10010e40alarms,
       "rm10010e40AlmOther": rm10010e40AlmOther,
       "rm10010e40AlmOtherNurg": rm10010e40AlmOtherNurg,
       "rm10010e40AlmsynthAlm2": rm10010e40AlmsynthAlm2,
       "rm10010e40AlmConfTableSave": rm10010e40AlmConfTableSave,
       "rm10010e40AlmInvUpload": rm10010e40AlmInvUpload,
       "rm10010e40AlmConfTableLoad": rm10010e40AlmConfTableLoad,
       "rm10010e40AlmCorrelatOff": rm10010e40AlmCorrelatOff,
       "rm10010e40AlmMaintenanceOn": rm10010e40AlmMaintenanceOn,
       "rm10010e40AlmOtherUrg": rm10010e40AlmOtherUrg,
       "rm10010e40AlmmodFanFail": rm10010e40AlmmodFanFail,
       "rm10010e40AlmFanModuleAbsent": rm10010e40AlmFanModuleAbsent,
       "rm10010e40AlmFansFail": rm10010e40AlmFansFail,
       "rm10010e40AlmFan1Fail": rm10010e40AlmFan1Fail,
       "rm10010e40AlmFan2Fail": rm10010e40AlmFan2Fail,
       "rm10010e40AlmFan3Fail": rm10010e40AlmFan3Fail,
       "rm10010e40AlmFan4Fail": rm10010e40AlmFan4Fail,
       "rm10010e40AlmOtherCrit": rm10010e40AlmOtherCrit,
       "rm10010e40AlmsynthAlm0": rm10010e40AlmsynthAlm0,
       "rm10010e40AlmFailFan": rm10010e40AlmFailFan,
       "rm10010e40AlmModGlobFail": rm10010e40AlmModGlobFail,
       "rm10010e40AlmDefFuseA": rm10010e40AlmDefFuseA,
       "rm10010e40AlmDefFuseB": rm10010e40AlmDefFuseB,
       "rm10010e40AlmclientModuleState": rm10010e40AlmclientModuleState,
       "rm10010e40AlmCfpInitialize": rm10010e40AlmCfpInitialize,
       "rm10010e40AlmCfpLowPower": rm10010e40AlmCfpLowPower,
       "rm10010e40AlmCfpHighPowerUp": rm10010e40AlmCfpHighPowerUp,
       "rm10010e40AlmCfpTxOff": rm10010e40AlmCfpTxOff,
       "rm10010e40AlmCfpTxTurnOn": rm10010e40AlmCfpTxTurnOn,
       "rm10010e40AlmCfpReady": rm10010e40AlmCfpReady,
       "rm10010e40AlmCfpFault": rm10010e40AlmCfpFault,
       "rm10010e40AlmCfpTxTurnOff": rm10010e40AlmCfpTxTurnOff,
       "rm10010e40AlmCfpHighPowerDown": rm10010e40AlmCfpHighPowerDown,
       "rm10010e40AlmclientModuleGeneralStatus": rm10010e40AlmclientModuleGeneralStatus,
       "rm10010e40AlmCfpOutOfAlignment": rm10010e40AlmCfpOutOfAlignment,
       "rm10010e40AlmCfpRxNetworkLol": rm10010e40AlmCfpRxNetworkLol,
       "rm10010e40AlmCfpRxLos": rm10010e40AlmCfpRxLos,
       "rm10010e40AlmCfpTxHostLol": rm10010e40AlmCfpTxHostLol,
       "rm10010e40AlmCfpTxLosf": rm10010e40AlmCfpTxLosf,
       "rm10010e40AlmCfpTxCmuLol": rm10010e40AlmCfpTxCmuLol,
       "rm10010e40AlmCfpTxJitterPllLol": rm10010e40AlmCfpTxJitterPllLol,
       "rm10010e40AlmCfpLossOfRefclk": rm10010e40AlmCfpLossOfRefclk,
       "rm10010e40AlmCfpHwInterlock": rm10010e40AlmCfpHwInterlock,
       "rm10010e40AlmclientGlobalAlarmSummary": rm10010e40AlmclientGlobalAlarmSummary,
       "rm10010e40AlmCfpSoftGlobAlarmTest": rm10010e40AlmCfpSoftGlobAlarmTest,
       "rm10010e40AlmCfpNetworkLaneAlarmWarning2": rm10010e40AlmCfpNetworkLaneAlarmWarning2,
       "rm10010e40AlmCfpModuleState": rm10010e40AlmCfpModuleState,
       "rm10010e40AlmCfpModuleGeneralStatus": rm10010e40AlmCfpModuleGeneralStatus,
       "rm10010e40AlmCfpModuleFault": rm10010e40AlmCfpModuleFault,
       "rm10010e40AlmCfpModuleAlarmWarning1": rm10010e40AlmCfpModuleAlarmWarning1,
       "rm10010e40AlmCfpModuleAlarmWarning2": rm10010e40AlmCfpModuleAlarmWarning2,
       "rm10010e40AlmCfpNetworkLaneAlarmWarning1": rm10010e40AlmCfpNetworkLaneAlarmWarning1,
       "rm10010e40AlmCfpNetworkLaneFaultStatus": rm10010e40AlmCfpNetworkLaneFaultStatus,
       "rm10010e40AlmCfpHostLaneFaultStatus": rm10010e40AlmCfpHostLaneFaultStatus,
       "rm10010e40AlmCfpGlobAlarmAssertion": rm10010e40AlmCfpGlobAlarmAssertion,
       "rm10010e40AlmmsaModuleState": rm10010e40AlmmsaModuleState,
       "rm10010e40AlmMsaInitialize": rm10010e40AlmMsaInitialize,
       "rm10010e40AlmMsaLowPower": rm10010e40AlmMsaLowPower,
       "rm10010e40AlmMsaHighPowerUp": rm10010e40AlmMsaHighPowerUp,
       "rm10010e40AlmMsaTxOff": rm10010e40AlmMsaTxOff,
       "rm10010e40AlmMsaTxTurnOn": rm10010e40AlmMsaTxTurnOn,
       "rm10010e40AlmMsaReady": rm10010e40AlmMsaReady,
       "rm10010e40AlmMsaFault": rm10010e40AlmMsaFault,
       "rm10010e40AlmMsaTxTurnOff": rm10010e40AlmMsaTxTurnOff,
       "rm10010e40AlmMsaHighPowerDown": rm10010e40AlmMsaHighPowerDown,
       "rm10010e40AlmmsaModuleGeneralStatus": rm10010e40AlmmsaModuleGeneralStatus,
       "rm10010e40AlmMsaOutOfAlignment": rm10010e40AlmMsaOutOfAlignment,
       "rm10010e40AlmMsaRxNetworkLol": rm10010e40AlmMsaRxNetworkLol,
       "rm10010e40AlmMsaRxLos": rm10010e40AlmMsaRxLos,
       "rm10010e40AlmMsaTxHostLol": rm10010e40AlmMsaTxHostLol,
       "rm10010e40AlmMsaTxLosf": rm10010e40AlmMsaTxLosf,
       "rm10010e40AlmMsaTxCmuLol": rm10010e40AlmMsaTxCmuLol,
       "rm10010e40AlmMsaTxJitterPllLol": rm10010e40AlmMsaTxJitterPllLol,
       "rm10010e40AlmMsaLossOfRefclk": rm10010e40AlmMsaLossOfRefclk,
       "rm10010e40AlmMsaHwInterlock": rm10010e40AlmMsaHwInterlock,
       "rm10010e40AlmmsaGlobalAlarmSummary": rm10010e40AlmmsaGlobalAlarmSummary,
       "rm10010e40AlmMsaSoftGlobAlarmTest": rm10010e40AlmMsaSoftGlobAlarmTest,
       "rm10010e40AlmMsaNetworkHostAlarmStatus": rm10010e40AlmMsaNetworkHostAlarmStatus,
       "rm10010e40AlmMsaNetworkLaneAlarmWarning2": rm10010e40AlmMsaNetworkLaneAlarmWarning2,
       "rm10010e40AlmMsaModuleState": rm10010e40AlmMsaModuleState,
       "rm10010e40AlmMsaModuleGeneralStatus": rm10010e40AlmMsaModuleGeneralStatus,
       "rm10010e40AlmModuleFault": rm10010e40AlmModuleFault,
       "rm10010e40AlmMsaModuleAlarmWarning1": rm10010e40AlmMsaModuleAlarmWarning1,
       "rm10010e40AlmMsaModuleAlarmWarning2": rm10010e40AlmMsaModuleAlarmWarning2,
       "rm10010e40AlmMsaNetworkLaneAlarmWarning1": rm10010e40AlmMsaNetworkLaneAlarmWarning1,
       "rm10010e40AlmMsaNetworkLaneFaultStatus": rm10010e40AlmMsaNetworkLaneFaultStatus,
       "rm10010e40AlmMsaHostLaneFaultStatus": rm10010e40AlmMsaHostLaneFaultStatus,
       "rm10010e40AlmMsaGlobAlarmAssertion": rm10010e40AlmMsaGlobAlarmAssertion,
       "rm10010e40AlmmsaNetworkTxAlignment": rm10010e40AlmmsaNetworkTxAlignment,
       "rm10010e40AlmNetTxTimingFault": rm10010e40AlmNetTxTimingFault,
       "rm10010e40AlmNetTxReferenceClockFault": rm10010e40AlmNetTxReferenceClockFault,
       "rm10010e40AlmNetTxCmuLockFault": rm10010e40AlmNetTxCmuLockFault,
       "rm10010e40AlmNetTxOutOfAlignment": rm10010e40AlmNetTxOutOfAlignment,
       "rm10010e40AlmNetTxLossOfAlignment": rm10010e40AlmNetTxLossOfAlignment,
       "rm10010e40AlmmsaNetworkRxAlignment": rm10010e40AlmmsaNetworkRxAlignment,
       "rm10010e40AlmNetRxTimingFault": rm10010e40AlmNetRxTimingFault,
       "rm10010e40AlmNetRxOutOfAlignment": rm10010e40AlmNetRxOutOfAlignment,
       "rm10010e40AlmNetRxLossOfAlignment": rm10010e40AlmNetRxLossOfAlignment,
       "rm10010e40AlmNetRxModemLockFault": rm10010e40AlmNetRxModemLockFault,
       "rm10010e40AlmNetRxModemSyncDetectFault": rm10010e40AlmNetRxModemSyncDetectFault,
       "rm10010e40AlmmsaNetworkHostNetworkAlarmSummary": rm10010e40AlmmsaNetworkHostNetworkAlarmSummary,
       "rm10010e40AlmNetworkTxAlignment": rm10010e40AlmNetworkTxAlignment,
       "rm10010e40AlmNetworkRxAlignment": rm10010e40AlmNetworkRxAlignment,
       "rm10010e40AlmNetworkRxOtn": rm10010e40AlmNetworkRxOtn,
       "rm10010e40AlmHostRxAlignment": rm10010e40AlmHostRxAlignment,
       "rm10010e40AlmHostTxAlignment": rm10010e40AlmHostTxAlignment,
       "rm10010e40AlmHostTxOtnStatus": rm10010e40AlmHostTxOtnStatus,
       "rm10010e40AlmmsaHostTxAlignment": rm10010e40AlmmsaHostTxAlignment,
       "rm10010e40AlmHostTxDeskewLockFault": rm10010e40AlmHostTxDeskewLockFault,
       "rm10010e40AlmHostTxOutOfAlignment": rm10010e40AlmHostTxOutOfAlignment,
       "rm10010e40AlmHostTxLossOfAlignment": rm10010e40AlmHostTxLossOfAlignment,
       "rm10010e40AlmHostTxCdrLockFault": rm10010e40AlmHostTxCdrLockFault,
       "rm10010e40AlmmsaHostRxAlignment": rm10010e40AlmmsaHostRxAlignment,
       "rm10010e40AlmHostRxCmuLockFault": rm10010e40AlmHostRxCmuLockFault,
       "rm10010e40AlmHostRxOutOfAlignment": rm10010e40AlmHostRxOutOfAlignment,
       "rm10010e40AlmHostRxLossOfAlignment": rm10010e40AlmHostRxLossOfAlignment,
       "rm10010e40AlmClient": rm10010e40AlmClient,
       "rm10010e40AlmClientNurg": rm10010e40AlmClientNurg,
       "rm10010e40AlmclientNetworkLaneAlarmWarningTable": rm10010e40AlmclientNetworkLaneAlarmWarningTable,
       "rm10010e40AlmclientNetworkLaneAlarmWarningEntry": rm10010e40AlmclientNetworkLaneAlarmWarningEntry,
       "rm10010e40AlmclientNetworkLaneAlarmWarningIndex": rm10010e40AlmclientNetworkLaneAlarmWarningIndex,
       "rm10010e40AlmClientRxPowerLowAlarmPortn": rm10010e40AlmClientRxPowerLowAlarmPortn,
       "rm10010e40AlmClientRxPowerLowWarningPortn": rm10010e40AlmClientRxPowerLowWarningPortn,
       "rm10010e40AlmClientRxPowerHighWarningPortn": rm10010e40AlmClientRxPowerHighWarningPortn,
       "rm10010e40AlmClientRxPowerHighAlarmPortn": rm10010e40AlmClientRxPowerHighAlarmPortn,
       "rm10010e40AlmLaserTempLowAlarmPortn": rm10010e40AlmLaserTempLowAlarmPortn,
       "rm10010e40AlmClientLaserTempLowWarningPortn": rm10010e40AlmClientLaserTempLowWarningPortn,
       "rm10010e40AlmClientLaserTempHighWarningPortn": rm10010e40AlmClientLaserTempHighWarningPortn,
       "rm10010e40AlmClientLaserTempHighAlarmPortn": rm10010e40AlmClientLaserTempHighAlarmPortn,
       "rm10010e40AlmClientTxPowerLowAlarmPortn": rm10010e40AlmClientTxPowerLowAlarmPortn,
       "rm10010e40AlmClientTxPowerLowWarningPortn": rm10010e40AlmClientTxPowerLowWarningPortn,
       "rm10010e40AlmClientTxPowerHighWarningPortn": rm10010e40AlmClientTxPowerHighWarningPortn,
       "rm10010e40AlmClientTxPowerHighAlarmPortn": rm10010e40AlmClientTxPowerHighAlarmPortn,
       "rm10010e40AlmClientBiasLowAlarmPortn": rm10010e40AlmClientBiasLowAlarmPortn,
       "rm10010e40AlmClientBiasLowWarningPortn": rm10010e40AlmClientBiasLowWarningPortn,
       "rm10010e40AlmClientBiasHighWarningPortn": rm10010e40AlmClientBiasHighWarningPortn,
       "rm10010e40AlmClientBiasHighAlarmPortn": rm10010e40AlmClientBiasHighAlarmPortn,
       "rm10010e40AlmclientSfpWarnDdmTable": rm10010e40AlmclientSfpWarnDdmTable,
       "rm10010e40AlmclientSfpWarnDdmEntry": rm10010e40AlmclientSfpWarnDdmEntry,
       "rm10010e40AlmclientSfpWarnDdmIndex": rm10010e40AlmclientSfpWarnDdmIndex,
       "rm10010e40AlmTxPwLowWngPortn": rm10010e40AlmTxPwLowWngPortn,
       "rm10010e40AlmTxPwrHighWngPortn": rm10010e40AlmTxPwrHighWngPortn,
       "rm10010e40AlmTxBiasLowWngPortn": rm10010e40AlmTxBiasLowWngPortn,
       "rm10010e40AlmTxBiasHighWngPortn": rm10010e40AlmTxBiasHighWngPortn,
       "rm10010e40AlmVccLowWngPortn": rm10010e40AlmVccLowWngPortn,
       "rm10010e40AlmVccHighWngPortn": rm10010e40AlmVccHighWngPortn,
       "rm10010e40AlmTempLowWngPortn": rm10010e40AlmTempLowWngPortn,
       "rm10010e40AlmTempHighWngPortn": rm10010e40AlmTempHighWngPortn,
       "rm10010e40AlmRxPwrLowWngPortn": rm10010e40AlmRxPwrLowWngPortn,
       "rm10010e40AlmRxPwrHighWngPortn": rm10010e40AlmRxPwrHighWngPortn,
       "rm10010e40AlmClientUrg": rm10010e40AlmClientUrg,
       "rm10010e40AlmclientNetworkLaneFaultTable": rm10010e40AlmclientNetworkLaneFaultTable,
       "rm10010e40AlmclientNetworkLaneFaultEntry": rm10010e40AlmclientNetworkLaneFaultEntry,
       "rm10010e40AlmclientNetworkLaneFaultIndex": rm10010e40AlmclientNetworkLaneFaultIndex,
       "rm10010e40AlmClientLaneRxFifoErrorPortn": rm10010e40AlmClientLaneRxFifoErrorPortn,
       "rm10010e40AlmClientLaneRxLolPortn": rm10010e40AlmClientLaneRxLolPortn,
       "rm10010e40AlmClientLaneRxLosPortn": rm10010e40AlmClientLaneRxLosPortn,
       "rm10010e40AlmClientLaneTxLolPortn": rm10010e40AlmClientLaneTxLolPortn,
       "rm10010e40AlmClientLaneTxLosfPortn": rm10010e40AlmClientLaneTxLosfPortn,
       "rm10010e40AlmClientLaneApdPowerSupplyPortn": rm10010e40AlmClientLaneApdPowerSupplyPortn,
       "rm10010e40AlmClientLaneWavelengthUnlockedPortn": rm10010e40AlmClientLaneWavelengthUnlockedPortn,
       "rm10010e40AlmClientLaneTecFaultPortn": rm10010e40AlmClientLaneTecFaultPortn,
       "rm10010e40AlmclientHostLaneFaultTable": rm10010e40AlmclientHostLaneFaultTable,
       "rm10010e40AlmclientHostLaneFaultEntry": rm10010e40AlmclientHostLaneFaultEntry,
       "rm10010e40AlmclientHostLaneFaultIndex": rm10010e40AlmclientHostLaneFaultIndex,
       "rm10010e40AlmClientLossOfSyncPortn": rm10010e40AlmClientLossOfSyncPortn,
       "rm10010e40AlmClientInputLossOfSigPortn": rm10010e40AlmClientInputLossOfSigPortn,
       "rm10010e40AlmClientLanesMarkerUnlockPortn": rm10010e40AlmClientLanesMarkerUnlockPortn,
       "rm10010e40AlmClientLanes6466UnlockPortn": rm10010e40AlmClientLanes6466UnlockPortn,
       "rm10010e40AlmClientLanesNotAlignedPortn": rm10010e40AlmClientLanesNotAlignedPortn,
       "rm10010e40AlmClientCsfDetectedPortn": rm10010e40AlmClientCsfDetectedPortn,
       "rm10010e40AlmClientTxHostLolPortn": rm10010e40AlmClientTxHostLolPortn,
       "rm10010e40AlmClientLaneTxFifoErrorPortn": rm10010e40AlmClientLaneTxFifoErrorPortn,
       "rm10010e40AlmclientSfpAlmDdmTable": rm10010e40AlmclientSfpAlmDdmTable,
       "rm10010e40AlmclientSfpAlmDdmEntry": rm10010e40AlmclientSfpAlmDdmEntry,
       "rm10010e40AlmclientSfpAlmDdmIndex": rm10010e40AlmclientSfpAlmDdmIndex,
       "rm10010e40AlmTxPwrLowAlaPortn": rm10010e40AlmTxPwrLowAlaPortn,
       "rm10010e40AlmTxPwrHighAlaPortn": rm10010e40AlmTxPwrHighAlaPortn,
       "rm10010e40AlmTxBiasLowAlaPortn": rm10010e40AlmTxBiasLowAlaPortn,
       "rm10010e40AlmTxBiasHighAlaPortn": rm10010e40AlmTxBiasHighAlaPortn,
       "rm10010e40AlmVccLowAlaPortn": rm10010e40AlmVccLowAlaPortn,
       "rm10010e40AlmVccHighAlaPortn": rm10010e40AlmVccHighAlaPortn,
       "rm10010e40AlmTempLowAlaPortn": rm10010e40AlmTempLowAlaPortn,
       "rm10010e40AlmTempHighAlaPortn": rm10010e40AlmTempHighAlaPortn,
       "rm10010e40AlmRxPwrLowAlaPortn": rm10010e40AlmRxPwrLowAlaPortn,
       "rm10010e40AlmRxPwrHighAlaPortn": rm10010e40AlmRxPwrHighAlaPortn,
       "rm10010e40AlmClientCrit": rm10010e40AlmClientCrit,
       "rm10010e40AlmsynthAlmPortTable": rm10010e40AlmsynthAlmPortTable,
       "rm10010e40AlmsynthAlmPortEntry": rm10010e40AlmsynthAlmPortEntry,
       "rm10010e40AlmsynthAlmPortIndex": rm10010e40AlmsynthAlmPortIndex,
       "rm10010e40AlmSfpAbsentPortn": rm10010e40AlmSfpAbsentPortn,
       "rm10010e40AlmDdmAbsentPortn": rm10010e40AlmDdmAbsentPortn,
       "rm10010e40AlmHwFailAccPortn": rm10010e40AlmHwFailAccPortn,
       "rm10010e40AlmDwLsdPortn": rm10010e40AlmDwLsdPortn,
       "rm10010e40AlmClientLocalOosPortn": rm10010e40AlmClientLocalOosPortn,
       "rm10010e40AlmClientRemoteOosPortn": rm10010e40AlmClientRemoteOosPortn,
       "rm10010e40AlmDwCaisPortn": rm10010e40AlmDwCaisPortn,
       "rm10010e40AlmSfpDdmWarningPortn": rm10010e40AlmSfpDdmWarningPortn,
       "rm10010e40AlmSfpDdmAlmPortn": rm10010e40AlmSfpDdmAlmPortn,
       "rm10010e40AlmFailAccPortn": rm10010e40AlmFailAccPortn,
       "rm10010e40AlmUpCsfPortn": rm10010e40AlmUpCsfPortn,
       "rm10010e40AlmLine": rm10010e40AlmLine,
       "rm10010e40AlmLineNurg": rm10010e40AlmLineNurg,
       "rm10010e40AlmlineNetworkLaneAlarmWarning1Table": rm10010e40AlmlineNetworkLaneAlarmWarning1Table,
       "rm10010e40AlmlineNetworkLaneAlarmWarning1Entry": rm10010e40AlmlineNetworkLaneAlarmWarning1Entry,
       "rm10010e40AlmlineNetworkLaneAlarmWarning1Index": rm10010e40AlmlineNetworkLaneAlarmWarning1Index,
       "rm10010e40AlmLineRxPowerLowAlarmPortn": rm10010e40AlmLineRxPowerLowAlarmPortn,
       "rm10010e40AlmLineRxPowerLowWarningPortn": rm10010e40AlmLineRxPowerLowWarningPortn,
       "rm10010e40AlmLineRxPowerHighWarningPortn": rm10010e40AlmLineRxPowerHighWarningPortn,
       "rm10010e40AlmLineRxPowerHighAlarmPortn": rm10010e40AlmLineRxPowerHighAlarmPortn,
       "rm10010e40AlmLineLaserTempLowAlarmPortn": rm10010e40AlmLineLaserTempLowAlarmPortn,
       "rm10010e40AlmLineLaserTempLowWarningPortn": rm10010e40AlmLineLaserTempLowWarningPortn,
       "rm10010e40AlmLineLaserTempHighWarningPortn": rm10010e40AlmLineLaserTempHighWarningPortn,
       "rm10010e40AlmLineLaserTempHighAlarmPortn": rm10010e40AlmLineLaserTempHighAlarmPortn,
       "rm10010e40AlmLineTxPowerLowAlarmPortn": rm10010e40AlmLineTxPowerLowAlarmPortn,
       "rm10010e40AlmLineTxPowerLowWarningPortn": rm10010e40AlmLineTxPowerLowWarningPortn,
       "rm10010e40AlmLineTxPowerHighWarningPortn": rm10010e40AlmLineTxPowerHighWarningPortn,
       "rm10010e40AlmLineTxPowerHighAlarmPortn": rm10010e40AlmLineTxPowerHighAlarmPortn,
       "rm10010e40AlmLineBiasLowAlarmPortn": rm10010e40AlmLineBiasLowAlarmPortn,
       "rm10010e40AlmLineBiasLowWarningPortn": rm10010e40AlmLineBiasLowWarningPortn,
       "rm10010e40AlmLineBiasHighWarningPortn": rm10010e40AlmLineBiasHighWarningPortn,
       "rm10010e40AlmLineBiasHighAlarmPortn": rm10010e40AlmLineBiasHighAlarmPortn,
       "rm10010e40AlmlineNetworkLaneAlarmWarning2Table": rm10010e40AlmlineNetworkLaneAlarmWarning2Table,
       "rm10010e40AlmlineNetworkLaneAlarmWarning2Entry": rm10010e40AlmlineNetworkLaneAlarmWarning2Entry,
       "rm10010e40AlmlineNetworkLaneAlarmWarning2Index": rm10010e40AlmlineNetworkLaneAlarmWarning2Index,
       "rm10010e40AlmTxModulatorBiasLowAlarmPortn": rm10010e40AlmTxModulatorBiasLowAlarmPortn,
       "rm10010e40AlmTxModulatorBiasLowWarningPortn": rm10010e40AlmTxModulatorBiasLowWarningPortn,
       "rm10010e40AlmTxModulatorBiasHighWarningPortn": rm10010e40AlmTxModulatorBiasHighWarningPortn,
       "rm10010e40AlmTxModulatorBiasHighAlarmPortn": rm10010e40AlmTxModulatorBiasHighAlarmPortn,
       "rm10010e40AlmRxLaserTempLowAlarmPortn": rm10010e40AlmRxLaserTempLowAlarmPortn,
       "rm10010e40AlmRxLaserTempLowWarningPortn": rm10010e40AlmRxLaserTempLowWarningPortn,
       "rm10010e40AlmRxLaserTempHighWarningPortn": rm10010e40AlmRxLaserTempHighWarningPortn,
       "rm10010e40AlmRxLaserTempHighAlarmPortn": rm10010e40AlmRxLaserTempHighAlarmPortn,
       "rm10010e40AlmRxLaserOutputLowAlarmPortn": rm10010e40AlmRxLaserOutputLowAlarmPortn,
       "rm10010e40AlmRxLaserOutputLowWarningPortn": rm10010e40AlmRxLaserOutputLowWarningPortn,
       "rm10010e40AlmRxLaserOutputHighWarningPortn": rm10010e40AlmRxLaserOutputHighWarningPortn,
       "rm10010e40AlmRxLaserOutputHighAlarmPortn": rm10010e40AlmRxLaserOutputHighAlarmPortn,
       "rm10010e40AlmRxLaserBiasLowAlarmPortn": rm10010e40AlmRxLaserBiasLowAlarmPortn,
       "rm10010e40AlmRxLaserBiasLowWarningPortn": rm10010e40AlmRxLaserBiasLowWarningPortn,
       "rm10010e40AlmRxLaserBiasHighWarningPortn": rm10010e40AlmRxLaserBiasHighWarningPortn,
       "rm10010e40AlmRxLaserBiasHighAlarmPortn": rm10010e40AlmRxLaserBiasHighAlarmPortn,
       "rm10010e40AlmLineUrg": rm10010e40AlmLineUrg,
       "rm10010e40AlmlineNetworkLaneFaultTable": rm10010e40AlmlineNetworkLaneFaultTable,
       "rm10010e40AlmlineNetworkLaneFaultEntry": rm10010e40AlmlineNetworkLaneFaultEntry,
       "rm10010e40AlmlineNetworkLaneFaultIndex": rm10010e40AlmlineNetworkLaneFaultIndex,
       "rm10010e40AlmLineLaneRxTecFaultPortn": rm10010e40AlmLineLaneRxTecFaultPortn,
       "rm10010e40AlmLineLaneRxFifoErrorPortn": rm10010e40AlmLineLaneRxFifoErrorPortn,
       "rm10010e40AlmLineLaneRxLolPortn": rm10010e40AlmLineLaneRxLolPortn,
       "rm10010e40AlmLineLaneRxLosPortn": rm10010e40AlmLineLaneRxLosPortn,
       "rm10010e40AlmLineLaneTxLolPortn": rm10010e40AlmLineLaneTxLolPortn,
       "rm10010e40AlmLineLaneTxLosfPortn": rm10010e40AlmLineLaneTxLosfPortn,
       "rm10010e40AlmLineLaneApdPowerSupplyPortn": rm10010e40AlmLineLaneApdPowerSupplyPortn,
       "rm10010e40AlmLineLaneWavelengthUnlockedPortn": rm10010e40AlmLineLaneWavelengthUnlockedPortn,
       "rm10010e40AlmLineLaneTecFaultPortn": rm10010e40AlmLineLaneTecFaultPortn,
       "rm10010e40AlmlineHostLaneFaultTable": rm10010e40AlmlineHostLaneFaultTable,
       "rm10010e40AlmlineHostLaneFaultEntry": rm10010e40AlmlineHostLaneFaultEntry,
       "rm10010e40AlmlineHostLaneFaultIndex": rm10010e40AlmlineHostLaneFaultIndex,
       "rm10010e40AlmLineInputLossOfSignalPortn": rm10010e40AlmLineInputLossOfSignalPortn,
       "rm10010e40AlmLineLossOfFramePortn": rm10010e40AlmLineLossOfFramePortn,
       "rm10010e40AlmLineSmBdiInsertedPortn": rm10010e40AlmLineSmBdiInsertedPortn,
       "rm10010e40AlmLineSmBdiDetectedPortn": rm10010e40AlmLineSmBdiDetectedPortn,
       "rm10010e40AlmLineSmIaeInsertedPortn": rm10010e40AlmLineSmIaeInsertedPortn,
       "rm10010e40AlmLineSmIaeDetectedPortn": rm10010e40AlmLineSmIaeDetectedPortn,
       "rm10010e40AlmLineTxHostLolPortn": rm10010e40AlmLineTxHostLolPortn,
       "rm10010e40AlmLineLaneTxFifoErrorPortn": rm10010e40AlmLineLaneTxFifoErrorPortn,
       "rm10010e40AlmlineNetworkLaneRxOtnTable": rm10010e40AlmlineNetworkLaneRxOtnTable,
       "rm10010e40AlmlineNetworkLaneRxOtnEntry": rm10010e40AlmlineNetworkLaneRxOtnEntry,
       "rm10010e40AlmlineNetworkLaneRxOtnIndex": rm10010e40AlmlineNetworkLaneRxOtnIndex,
       "rm10010e40AlmLineRxOtnOduAisPortn": rm10010e40AlmLineRxOtnOduAisPortn,
       "rm10010e40AlmLineRxOtnOtuAisPortn": rm10010e40AlmLineRxOtnOtuAisPortn,
       "rm10010e40AlmLineRxSmBdiPortn": rm10010e40AlmLineRxSmBdiPortn,
       "rm10010e40AlmLineRxOtnIaePortn": rm10010e40AlmLineRxOtnIaePortn,
       "rm10010e40AlmLineRxOtnOomPortn": rm10010e40AlmLineRxOtnOomPortn,
       "rm10010e40AlmLineRxOtnLomPortn": rm10010e40AlmLineRxOtnLomPortn,
       "rm10010e40AlmLineRxOtnOofPortn": rm10010e40AlmLineRxOtnOofPortn,
       "rm10010e40AlmLineRxOtnLofPortn": rm10010e40AlmLineRxOtnLofPortn,
       "rm10010e40AlmlineHostLaneTxOtnTable": rm10010e40AlmlineHostLaneTxOtnTable,
       "rm10010e40AlmlineHostLaneTxOtnEntry": rm10010e40AlmlineHostLaneTxOtnEntry,
       "rm10010e40AlmlineHostLaneTxOtnIndex": rm10010e40AlmlineHostLaneTxOtnIndex,
       "rm10010e40AlmLineTxOtnOduAisPortn": rm10010e40AlmLineTxOtnOduAisPortn,
       "rm10010e40AlmLineTxOtnOtuAisPortn": rm10010e40AlmLineTxOtnOtuAisPortn,
       "rm10010e40AlmLineTxSmBdiPortn": rm10010e40AlmLineTxSmBdiPortn,
       "rm10010e40AlmLineTxOtnIaePortn": rm10010e40AlmLineTxOtnIaePortn,
       "rm10010e40AlmLineTxOtnOomPortn": rm10010e40AlmLineTxOtnOomPortn,
       "rm10010e40AlmLineTxOtnLomPortn": rm10010e40AlmLineTxOtnLomPortn,
       "rm10010e40AlmLineTxOtnOofPortn": rm10010e40AlmLineTxOtnOofPortn,
       "rm10010e40AlmLineTxOtnLofPortn": rm10010e40AlmLineTxOtnLofPortn,
       "rm10010e40AlmLineCrit": rm10010e40AlmLineCrit,
       "rm10010e40AlmsynthAlmLineTable": rm10010e40AlmsynthAlmLineTable,
       "rm10010e40AlmsynthAlmLineEntry": rm10010e40AlmsynthAlmLineEntry,
       "rm10010e40AlmsynthAlmLineIndex": rm10010e40AlmsynthAlmLineIndex,
       "rm10010e40AlmXfpAbsentPortn": rm10010e40AlmXfpAbsentPortn,
       "rm10010e40AlmXfpInitNotComplPortn": rm10010e40AlmXfpInitNotComplPortn,
       "rm10010e40AlmLineHwFailPortn": rm10010e40AlmLineHwFailPortn,
       "rm10010e40AlmXfpTxOffPortn": rm10010e40AlmXfpTxOffPortn,
       "rm10010e40AlmLineLocalOosPortn": rm10010e40AlmLineLocalOosPortn,
       "rm10010e40AlmUpRdiInsPortn": rm10010e40AlmUpRdiInsPortn,
       "rm10010e40AlmLineDdmWarningPortn": rm10010e40AlmLineDdmWarningPortn,
       "rm10010e40AlmLineDdmAlmPortn": rm10010e40AlmLineDdmAlmPortn,
       "rm10010e40AlmLineFailPortn": rm10010e40AlmLineFailPortn,
       "rm10010e40AlmLineActivePortn": rm10010e40AlmLineActivePortn,
       "rm10010e40measures": rm10010e40measures,
       "rm10010e40MesrOther": rm10010e40MesrOther,
       "rm10010e40Mesrsynth0": rm10010e40Mesrsynth0,
       "rm10010e40Mesrsynth1": rm10010e40Mesrsynth1,
       "rm10010e40MesrpmIntervalNumber": rm10010e40MesrpmIntervalNumber,
       "rm10010e40MesrlineNetTxLaserOutputPwrAverage": rm10010e40MesrlineNetTxLaserOutputPwrAverage,
       "rm10010e40MesrlineNetTxLaserTempAverage": rm10010e40MesrlineNetTxLaserTempAverage,
       "rm10010e40MesrlineNetTxBiasCurrentAverage": rm10010e40MesrlineNetTxBiasCurrentAverage,
       "rm10010e40MesrlineNetRxInputPwrAverage": rm10010e40MesrlineNetRxInputPwrAverage,
       "rm10010e40MesrlineResidualChromaticDispAverage": rm10010e40MesrlineResidualChromaticDispAverage,
       "rm10010e40MesrlineDiffGroupDelayAverage": rm10010e40MesrlineDiffGroupDelayAverage,
       "rm10010e40MesrlineQFactorAverage": rm10010e40MesrlineQFactorAverage,
       "rm10010e40MesrlineCarrierFreqOffsetAverage": rm10010e40MesrlineCarrierFreqOffsetAverage,
       "rm10010e40MesrlineOsnrAverage": rm10010e40MesrlineOsnrAverage,
       "rm10010e40MesrclientNetTxTempMin": rm10010e40MesrclientNetTxTempMin,
       "rm10010e40MesrclientNetTxBiasMin": rm10010e40MesrclientNetTxBiasMin,
       "rm10010e40MesrclientNetTxPwrMin": rm10010e40MesrclientNetTxPwrMin,
       "rm10010e40MesrclientNetRxPwrMin": rm10010e40MesrclientNetRxPwrMin,
       "rm10010e40MesrlineNetTxLaserOutputPwrMin": rm10010e40MesrlineNetTxLaserOutputPwrMin,
       "rm10010e40MesrlineNetTxLaserTempMin": rm10010e40MesrlineNetTxLaserTempMin,
       "rm10010e40MesrlineNetTxBiasCurrentMin": rm10010e40MesrlineNetTxBiasCurrentMin,
       "rm10010e40MesrlineNetRxInputPwrMin": rm10010e40MesrlineNetRxInputPwrMin,
       "rm10010e40MesrlineResidualChromaticDispMin": rm10010e40MesrlineResidualChromaticDispMin,
       "rm10010e40MesrlineDiffGroupDelayMin": rm10010e40MesrlineDiffGroupDelayMin,
       "rm10010e40MesrlineQFactorMin": rm10010e40MesrlineQFactorMin,
       "rm10010e40MesrlineCarrierFreqOffsetMin": rm10010e40MesrlineCarrierFreqOffsetMin,
       "rm10010e40MesrlineOsnrMin": rm10010e40MesrlineOsnrMin,
       "rm10010e40MesrclientNetTxTempMax": rm10010e40MesrclientNetTxTempMax,
       "rm10010e40MesrclientNetTxBiasMax": rm10010e40MesrclientNetTxBiasMax,
       "rm10010e40MesrclientNetTxPwrMax": rm10010e40MesrclientNetTxPwrMax,
       "rm10010e40MesrclientNetRxPwrMax": rm10010e40MesrclientNetRxPwrMax,
       "rm10010e40MesrlineNetTxLaserOutputPwrMax": rm10010e40MesrlineNetTxLaserOutputPwrMax,
       "rm10010e40MesrlineNetTxLaserTempMax": rm10010e40MesrlineNetTxLaserTempMax,
       "rm10010e40MesrlineNetTxBiasCurrentMax": rm10010e40MesrlineNetTxBiasCurrentMax,
       "rm10010e40MesrlineNetRxInputPwrMax": rm10010e40MesrlineNetRxInputPwrMax,
       "rm10010e40MesrlineResidualChromaticDispMax": rm10010e40MesrlineResidualChromaticDispMax,
       "rm10010e40MesrlineDiffGroupDelayMax": rm10010e40MesrlineDiffGroupDelayMax,
       "rm10010e40MesrlineQFactorMax": rm10010e40MesrlineQFactorMax,
       "rm10010e40MesrlineCarrierFreqOffsetMax": rm10010e40MesrlineCarrierFreqOffsetMax,
       "rm10010e40MesrlineOsnrMax": rm10010e40MesrlineOsnrMax,
       "rm10010e40MesrClient": rm10010e40MesrClient,
       "rm10010e40MesrclientCfpTemp": rm10010e40MesrclientCfpTemp,
       "rm10010e40MesrclientCfp3v3Voltage": rm10010e40MesrclientCfp3v3Voltage,
       "rm10010e40MesrclientSoaBiasCurrent": rm10010e40MesrclientSoaBiasCurrent,
       "rm10010e40MesrclientNetTxTempTable": rm10010e40MesrclientNetTxTempTable,
       "rm10010e40MesrclientNetTxTempEntry": rm10010e40MesrclientNetTxTempEntry,
       "rm10010e40MesrclientNetTxTempIndex": rm10010e40MesrclientNetTxTempIndex,
       "rm10010e40MesrclientNetTxTempPortn": rm10010e40MesrclientNetTxTempPortn,
       "rm10010e40MesrclientNetTxBiasTable": rm10010e40MesrclientNetTxBiasTable,
       "rm10010e40MesrclientNetTxBiasEntry": rm10010e40MesrclientNetTxBiasEntry,
       "rm10010e40MesrclientNetTxBiasIndex": rm10010e40MesrclientNetTxBiasIndex,
       "rm10010e40MesrclientNetTxBiasPortn": rm10010e40MesrclientNetTxBiasPortn,
       "rm10010e40MesrclientNetTxPwrTable": rm10010e40MesrclientNetTxPwrTable,
       "rm10010e40MesrclientNetTxPwrEntry": rm10010e40MesrclientNetTxPwrEntry,
       "rm10010e40MesrclientNetTxPwrIndex": rm10010e40MesrclientNetTxPwrIndex,
       "rm10010e40MesrclientNetTxPwrPortn": rm10010e40MesrclientNetTxPwrPortn,
       "rm10010e40MesrclientNetRxPwrTable": rm10010e40MesrclientNetRxPwrTable,
       "rm10010e40MesrclientNetRxPwrEntry": rm10010e40MesrclientNetRxPwrEntry,
       "rm10010e40MesrclientNetRxPwrIndex": rm10010e40MesrclientNetRxPwrIndex,
       "rm10010e40MesrclientNetRxPwrPortn": rm10010e40MesrclientNetRxPwrPortn,
       "rm10010e40MesrLine": rm10010e40MesrLine,
       "rm10010e40MesrlineMsaTemp": rm10010e40MesrlineMsaTemp,
       "rm10010e40MesrlineMsa3v3Voltage": rm10010e40MesrlineMsa3v3Voltage,
       "rm10010e40MesrlineSoaBiasCurrent": rm10010e40MesrlineSoaBiasCurrent,
       "rm10010e40MesrlineNetTxLaserOutputPwrTable": rm10010e40MesrlineNetTxLaserOutputPwrTable,
       "rm10010e40MesrlineNetTxLaserOutputPwrEntry": rm10010e40MesrlineNetTxLaserOutputPwrEntry,
       "rm10010e40MesrlineNetTxLaserOutputPwrIndex": rm10010e40MesrlineNetTxLaserOutputPwrIndex,
       "rm10010e40MesrlineNetTxLaserOutputPwrPortn": rm10010e40MesrlineNetTxLaserOutputPwrPortn,
       "rm10010e40MesrlineNetTxLaserTempTable": rm10010e40MesrlineNetTxLaserTempTable,
       "rm10010e40MesrlineNetTxLaserTempEntry": rm10010e40MesrlineNetTxLaserTempEntry,
       "rm10010e40MesrlineNetTxLaserTempIndex": rm10010e40MesrlineNetTxLaserTempIndex,
       "rm10010e40MesrlineNetTxLaserTempPortn": rm10010e40MesrlineNetTxLaserTempPortn,
       "rm10010e40MesrlineNetTxBiasCurrentTable": rm10010e40MesrlineNetTxBiasCurrentTable,
       "rm10010e40MesrlineNetTxBiasCurrentEntry": rm10010e40MesrlineNetTxBiasCurrentEntry,
       "rm10010e40MesrlineNetTxBiasCurrentIndex": rm10010e40MesrlineNetTxBiasCurrentIndex,
       "rm10010e40MesrlineNetTxBiasCurrentPortn": rm10010e40MesrlineNetTxBiasCurrentPortn,
       "rm10010e40MesrlineNetRxInputPwrTable": rm10010e40MesrlineNetRxInputPwrTable,
       "rm10010e40MesrlineNetRxInputPwrEntry": rm10010e40MesrlineNetRxInputPwrEntry,
       "rm10010e40MesrlineNetRxInputPwrIndex": rm10010e40MesrlineNetRxInputPwrIndex,
       "rm10010e40MesrlineNetRxInputPwrPortn": rm10010e40MesrlineNetRxInputPwrPortn,
       "rm10010e40MesrlineResidualChromaticDispTable": rm10010e40MesrlineResidualChromaticDispTable,
       "rm10010e40MesrlineResidualChromaticDispEntry": rm10010e40MesrlineResidualChromaticDispEntry,
       "rm10010e40MesrlineResidualChromaticDispIndex": rm10010e40MesrlineResidualChromaticDispIndex,
       "rm10010e40MesrlineResidualChromaticDispPortn": rm10010e40MesrlineResidualChromaticDispPortn,
       "rm10010e40MesrlineDiffGroupDelayTable": rm10010e40MesrlineDiffGroupDelayTable,
       "rm10010e40MesrlineDiffGroupDelayEntry": rm10010e40MesrlineDiffGroupDelayEntry,
       "rm10010e40MesrlineDiffGroupDelayIndex": rm10010e40MesrlineDiffGroupDelayIndex,
       "rm10010e40MesrlineDiffGroupDelayPortn": rm10010e40MesrlineDiffGroupDelayPortn,
       "rm10010e40MesrlineQFactorTable": rm10010e40MesrlineQFactorTable,
       "rm10010e40MesrlineQFactorEntry": rm10010e40MesrlineQFactorEntry,
       "rm10010e40MesrlineQFactorIndex": rm10010e40MesrlineQFactorIndex,
       "rm10010e40MesrlineQFactorPortn": rm10010e40MesrlineQFactorPortn,
       "rm10010e40MesrlineCarrierFreqOffsetTable": rm10010e40MesrlineCarrierFreqOffsetTable,
       "rm10010e40MesrlineCarrierFreqOffsetEntry": rm10010e40MesrlineCarrierFreqOffsetEntry,
       "rm10010e40MesrlineCarrierFreqOffsetIndex": rm10010e40MesrlineCarrierFreqOffsetIndex,
       "rm10010e40MesrlineCarrierFreqOffsetPortn": rm10010e40MesrlineCarrierFreqOffsetPortn,
       "rm10010e40MesrlineOsnrTable": rm10010e40MesrlineOsnrTable,
       "rm10010e40MesrlineOsnrEntry": rm10010e40MesrlineOsnrEntry,
       "rm10010e40MesrlineOsnrIndex": rm10010e40MesrlineOsnrIndex,
       "rm10010e40MesrlineOsnrPortn": rm10010e40MesrlineOsnrPortn,
       "rm10010e40counters": rm10010e40counters,
       "rm10010e40CntOther": rm10010e40CntOther,
       "rm10010e40CntClient": rm10010e40CntClient,
       "rm10010e40CntclientInputErrorCounterLaneOneTable": rm10010e40CntclientInputErrorCounterLaneOneTable,
       "rm10010e40CntclientInputErrorCounterLaneOneEntry": rm10010e40CntclientInputErrorCounterLaneOneEntry,
       "rm10010e40CntclientInputErrorCounterLaneOneIndex": rm10010e40CntclientInputErrorCounterLaneOneIndex,
       "rm10010e40CntclientInputErrorCounterLaneOneValuePortn": rm10010e40CntclientInputErrorCounterLaneOneValuePortn,
       "rm10010e40CntclientInputErrorCounterLaneOneErrorPortn": rm10010e40CntclientInputErrorCounterLaneOneErrorPortn,
       "rm10010e40CntclientInputErrorCounterLaneOneOverloadPortn": rm10010e40CntclientInputErrorCounterLaneOneOverloadPortn,
       "rm10010e40CntclientInputErrorCounterLaneTwoTable": rm10010e40CntclientInputErrorCounterLaneTwoTable,
       "rm10010e40CntclientInputErrorCounterLaneTwoEntry": rm10010e40CntclientInputErrorCounterLaneTwoEntry,
       "rm10010e40CntclientInputErrorCounterLaneTwoIndex": rm10010e40CntclientInputErrorCounterLaneTwoIndex,
       "rm10010e40CntclientInputErrorCounterLaneTwoValuePortn": rm10010e40CntclientInputErrorCounterLaneTwoValuePortn,
       "rm10010e40CntclientInputErrorCounterLaneTwoErrorPortn": rm10010e40CntclientInputErrorCounterLaneTwoErrorPortn,
       "rm10010e40CntclientInputErrorCounterLaneTwoOverloadPortn": rm10010e40CntclientInputErrorCounterLaneTwoOverloadPortn,
       "rm10010e40CntclientInputErrorCounterTable": rm10010e40CntclientInputErrorCounterTable,
       "rm10010e40CntclientInputErrorCounterEntry": rm10010e40CntclientInputErrorCounterEntry,
       "rm10010e40CntclientInputErrorCounterIndex": rm10010e40CntclientInputErrorCounterIndex,
       "rm10010e40CntclientInputErrorCounterValuePortn": rm10010e40CntclientInputErrorCounterValuePortn,
       "rm10010e40CntclientInputErrorCounterErrorPortn": rm10010e40CntclientInputErrorCounterErrorPortn,
       "rm10010e40CntclientInputErrorCounterOverloadPortn": rm10010e40CntclientInputErrorCounterOverloadPortn,
       "rm10010e40CntclientCbipCounterTable": rm10010e40CntclientCbipCounterTable,
       "rm10010e40CntclientCbipCounterEntry": rm10010e40CntclientCbipCounterEntry,
       "rm10010e40CntclientCbipCounterIndex": rm10010e40CntclientCbipCounterIndex,
       "rm10010e40CntclientCbipCounterValuePortn": rm10010e40CntclientCbipCounterValuePortn,
       "rm10010e40CntclientCbipCounterErrorPortn": rm10010e40CntclientCbipCounterErrorPortn,
       "rm10010e40CntclientCbipCounterOverloadPortn": rm10010e40CntclientCbipCounterOverloadPortn,
       "rm10010e40CntLine": rm10010e40CntLine,
       "rm10010e40CntlocalLineSmBip8ErrorCounterTable": rm10010e40CntlocalLineSmBip8ErrorCounterTable,
       "rm10010e40CntlocalLineSmBip8ErrorCounterEntry": rm10010e40CntlocalLineSmBip8ErrorCounterEntry,
       "rm10010e40CntlocalLineSmBip8ErrorCounterIndex": rm10010e40CntlocalLineSmBip8ErrorCounterIndex,
       "rm10010e40CntlocalLineSmBip8ErrorCounterValuePortn": rm10010e40CntlocalLineSmBip8ErrorCounterValuePortn,
       "rm10010e40CntlocalLineSmBip8ErrorCounterErrorPortn": rm10010e40CntlocalLineSmBip8ErrorCounterErrorPortn,
       "rm10010e40CntlocalLineSmBip8ErrorCounterOverloadPortn": rm10010e40CntlocalLineSmBip8ErrorCounterOverloadPortn,
       "rm10010e40CntlocalLineFecCorrectedErrorsCounterTable": rm10010e40CntlocalLineFecCorrectedErrorsCounterTable,
       "rm10010e40CntlocalLineFecCorrectedErrorsCounterEntry": rm10010e40CntlocalLineFecCorrectedErrorsCounterEntry,
       "rm10010e40CntlocalLineFecCorrectedErrorsCounterIndex": rm10010e40CntlocalLineFecCorrectedErrorsCounterIndex,
       "rm10010e40CntlocalLineFecCorrectedErrorsCounterValuePortn": rm10010e40CntlocalLineFecCorrectedErrorsCounterValuePortn,
       "rm10010e40CntlocalLineFecCorrectedErrorsCounterErrorPortn": rm10010e40CntlocalLineFecCorrectedErrorsCounterErrorPortn,
       "rm10010e40CntlocalLineFecCorrectedErrorsCounterOverloadPortn": rm10010e40CntlocalLineFecCorrectedErrorsCounterOverloadPortn,
       "rm10010e40CntremoteLineSmBip8ErrorCounterTable": rm10010e40CntremoteLineSmBip8ErrorCounterTable,
       "rm10010e40CntremoteLineSmBip8ErrorCounterEntry": rm10010e40CntremoteLineSmBip8ErrorCounterEntry,
       "rm10010e40CntremoteLineSmBip8ErrorCounterIndex": rm10010e40CntremoteLineSmBip8ErrorCounterIndex,
       "rm10010e40CntremoteLineSmBip8ErrorCounterValuePortn": rm10010e40CntremoteLineSmBip8ErrorCounterValuePortn,
       "rm10010e40CntremoteLineSmBip8ErrorCounterErrorPortn": rm10010e40CntremoteLineSmBip8ErrorCounterErrorPortn,
       "rm10010e40CntremoteLineSmBip8ErrorCounterOverloadPortn": rm10010e40CntremoteLineSmBip8ErrorCounterOverloadPortn,
       "rm10010e40CntlineDfrmTimCntTable": rm10010e40CntlineDfrmTimCntTable,
       "rm10010e40CntlineDfrmTimCntEntry": rm10010e40CntlineDfrmTimCntEntry,
       "rm10010e40CntlineDfrmTimCntIndex": rm10010e40CntlineDfrmTimCntIndex,
       "rm10010e40CntlineDfrmTimCntValuePortn": rm10010e40CntlineDfrmTimCntValuePortn,
       "rm10010e40CntlineDfrmTimCntErrorPortn": rm10010e40CntlineDfrmTimCntErrorPortn,
       "rm10010e40CntlineDfrmTimCntOverloadPortn": rm10010e40CntlineDfrmTimCntOverloadPortn,
       "rm10010e40CntlocalLineTrscvFecCorrectedErrorCounterTable": rm10010e40CntlocalLineTrscvFecCorrectedErrorCounterTable,
       "rm10010e40CntlocalLineTrscvFecCorrectedErrorCounterEntry": rm10010e40CntlocalLineTrscvFecCorrectedErrorCounterEntry,
       "rm10010e40CntlocalLineTrscvFecCorrectedErrorCounterIndex": rm10010e40CntlocalLineTrscvFecCorrectedErrorCounterIndex,
       "rm10010e40CntlocalLineTrscvFecCorrectedErrorCounterValuePortn": rm10010e40CntlocalLineTrscvFecCorrectedErrorCounterValuePortn,
       "rm10010e40CntlocalLineTrscvFecCorrectedErrorCounterErrorPortn": rm10010e40CntlocalLineTrscvFecCorrectedErrorCounterErrorPortn,
       "rm10010e40CntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn": rm10010e40CntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn,
       "rm10010e40CntlocalLineTrscvFecUncorrectedErrorCounterTable": rm10010e40CntlocalLineTrscvFecUncorrectedErrorCounterTable,
       "rm10010e40CntlocalLineTrscvFecUncorrectedErrorCounterEntry": rm10010e40CntlocalLineTrscvFecUncorrectedErrorCounterEntry,
       "rm10010e40CntlocalLineTrscvFecUncorrectedErrorCounterIndex": rm10010e40CntlocalLineTrscvFecUncorrectedErrorCounterIndex,
       "rm10010e40CntlocalLineTrscvFecUncorrectedErrorCounterValuePortn": rm10010e40CntlocalLineTrscvFecUncorrectedErrorCounterValuePortn,
       "rm10010e40CntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn": rm10010e40CntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn,
       "rm10010e40CntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn": rm10010e40CntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn,
       "rm10010e40controlsWrite": rm10010e40controlsWrite,
       "rm10010e40CtrlOther": rm10010e40CtrlOther,
       "rm10010e40CtrlconfMgnt1": rm10010e40CtrlconfMgnt1,
       "rm10010e40CtrlConf1Load1": rm10010e40CtrlConf1Load1,
       "rm10010e40CtrlConf2Load1": rm10010e40CtrlConf2Load1,
       "rm10010e40CtrlConf2Flash1": rm10010e40CtrlConf2Flash1,
       "rm10010e40CtrlConf2Clear1": rm10010e40CtrlConf2Clear1,
       "rm10010e40Ctrlsynth4": rm10010e40Ctrlsynth4,
       "rm10010e40CtrlCorrelatOn": rm10010e40CtrlCorrelatOn,
       "rm10010e40CtrlCorrelatOff": rm10010e40CtrlCorrelatOff,
       "rm10010e40CtrlswMgnt": rm10010e40CtrlswMgnt,
       "rm10010e40CtrlColdReset": rm10010e40CtrlColdReset,
       "rm10010e40CtrlWarmReset": rm10010e40CtrlWarmReset,
       "rm10010e40CtrlLoadSwBank1": rm10010e40CtrlLoadSwBank1,
       "rm10010e40CtrlLoadSwBank2": rm10010e40CtrlLoadSwBank2,
       "rm10010e40CtrlgwMgnt": rm10010e40CtrlgwMgnt,
       "rm10010e40CtrlCurrentGwReset": rm10010e40CtrlCurrentGwReset,
       "rm10010e40CtrlLoadGwBank1": rm10010e40CtrlLoadGwBank1,
       "rm10010e40CtrlLoadGwBank2": rm10010e40CtrlLoadGwBank2,
       "rm10010e40CtrlLoadGwBank3": rm10010e40CtrlLoadGwBank3,
       "rm10010e40CtrlLoadGwBank4": rm10010e40CtrlLoadGwBank4,
       "rm10010e40CtrlledTest": rm10010e40CtrlledTest,
       "rm10010e40CtrlGreenLed": rm10010e40CtrlGreenLed,
       "rm10010e40CtrlRedLed": rm10010e40CtrlRedLed,
       "rm10010e40CtrlLedOff": rm10010e40CtrlLedOff,
       "rm10010e40CtrlinitSwitchMarvell": rm10010e40CtrlinitSwitchMarvell,
       "rm10010e40CtrlInitSwitchMarvell": rm10010e40CtrlInitSwitchMarvell,
       "rm10010e40CtrlresetCount": rm10010e40CtrlresetCount,
       "rm10010e40CtrlResetcount": rm10010e40CtrlResetcount,
       "rm10010e40CtrlresetRmon": rm10010e40CtrlresetRmon,
       "rm10010e40CtrlResetrmon": rm10010e40CtrlResetrmon,
       "rm10010e40CtrlresetMeasurements": rm10010e40CtrlresetMeasurements,
       "rm10010e40CtrlResetmeasurements": rm10010e40CtrlResetmeasurements,
       "rm10010e40CtrlClient": rm10010e40CtrlClient,
       "rm10010e40CtrlaccessLoopTable": rm10010e40CtrlaccessLoopTable,
       "rm10010e40CtrlaccessLoopEntry": rm10010e40CtrlaccessLoopEntry,
       "rm10010e40CtrlaccessLoopIndex": rm10010e40CtrlaccessLoopIndex,
       "rm10010e40CtrlaccessLoopPortn": rm10010e40CtrlaccessLoopPortn,
       "rm10010e40CtrlclientLoopToLineTable": rm10010e40CtrlclientLoopToLineTable,
       "rm10010e40CtrlclientLoopToLineEntry": rm10010e40CtrlclientLoopToLineEntry,
       "rm10010e40CtrlclientLoopToLineIndex": rm10010e40CtrlclientLoopToLineIndex,
       "rm10010e40CtrlclientLoopToLinePortn": rm10010e40CtrlclientLoopToLinePortn,
       "rm10010e40CtrlcsfUpInsTable": rm10010e40CtrlcsfUpInsTable,
       "rm10010e40CtrlcsfUpInsEntry": rm10010e40CtrlcsfUpInsEntry,
       "rm10010e40CtrlcsfUpInsIndex": rm10010e40CtrlcsfUpInsIndex,
       "rm10010e40CtrlcsfUpInsPortn": rm10010e40CtrlcsfUpInsPortn,
       "rm10010e40CtrlcaisDwInsTable": rm10010e40CtrlcaisDwInsTable,
       "rm10010e40CtrlcaisDwInsEntry": rm10010e40CtrlcaisDwInsEntry,
       "rm10010e40CtrlcaisDwInsIndex": rm10010e40CtrlcaisDwInsIndex,
       "rm10010e40CtrlcaisDwInsPortn": rm10010e40CtrlcaisDwInsPortn,
       "rm10010e40CtrlLine": rm10010e40CtrlLine,
       "rm10010e40CtrlcommAccessLoopTable": rm10010e40CtrlcommAccessLoopTable,
       "rm10010e40CtrlcommAccessLoopEntry": rm10010e40CtrlcommAccessLoopEntry,
       "rm10010e40CtrlcommAccessLoopIndex": rm10010e40CtrlcommAccessLoopIndex,
       "rm10010e40CtrlcommAccessLoopPortn": rm10010e40CtrlcommAccessLoopPortn,
       "rm10010e40CtrllineLoopTable": rm10010e40CtrllineLoopTable,
       "rm10010e40CtrllineLoopEntry": rm10010e40CtrllineLoopEntry,
       "rm10010e40CtrllineLoopIndex": rm10010e40CtrllineLoopIndex,
       "rm10010e40CtrllineLoopPortn": rm10010e40CtrllineLoopPortn,
       "rm10010e40CtrlfecDisableTable": rm10010e40CtrlfecDisableTable,
       "rm10010e40CtrlfecDisableEntry": rm10010e40CtrlfecDisableEntry,
       "rm10010e40CtrlfecDisableIndex": rm10010e40CtrlfecDisableIndex,
       "rm10010e40CtrlfecDisablePortn": rm10010e40CtrlfecDisablePortn,
       "rm10010e40CtrlmsaLineLoopTable": rm10010e40CtrlmsaLineLoopTable,
       "rm10010e40CtrlmsaLineLoopEntry": rm10010e40CtrlmsaLineLoopEntry,
       "rm10010e40CtrlmsaLineLoopIndex": rm10010e40CtrlmsaLineLoopIndex,
       "rm10010e40CtrlmsaLineLoopPortn": rm10010e40CtrlmsaLineLoopPortn,
       "rm10010e40CtrlmsaTxResetTable": rm10010e40CtrlmsaTxResetTable,
       "rm10010e40CtrlmsaTxResetEntry": rm10010e40CtrlmsaTxResetEntry,
       "rm10010e40CtrlmsaTxResetIndex": rm10010e40CtrlmsaTxResetIndex,
       "rm10010e40CtrlmsaTxResetPortn": rm10010e40CtrlmsaTxResetPortn,
       "rm10010e40CtrlmsaRxResetTable": rm10010e40CtrlmsaRxResetTable,
       "rm10010e40CtrlmsaRxResetEntry": rm10010e40CtrlmsaRxResetEntry,
       "rm10010e40CtrlmsaRxResetIndex": rm10010e40CtrlmsaRxResetIndex,
       "rm10010e40CtrlmsaRxResetPortn": rm10010e40CtrlmsaRxResetPortn,
       "rm10010e40CtrlmsaShutdownTable": rm10010e40CtrlmsaShutdownTable,
       "rm10010e40CtrlmsaShutdownEntry": rm10010e40CtrlmsaShutdownEntry,
       "rm10010e40CtrlmsaShutdownIndex": rm10010e40CtrlmsaShutdownIndex,
       "rm10010e40CtrlmsaShutdownPortn": rm10010e40CtrlmsaShutdownPortn,
       "rm10010e40ri": rm10010e40ri,
       "rm10010e40riTable": rm10010e40riTable,
       "rm10010e40RinvSfpTable": rm10010e40RinvSfpTable,
       "rm10010e40RinvSfpEntry": rm10010e40RinvSfpEntry,
       "rm10010e40RinvSfpIndex": rm10010e40RinvSfpIndex,
       "rm10010e40Rinvsfp": rm10010e40Rinvsfp,
       "rm10010e40RinvLineTable": rm10010e40RinvLineTable,
       "rm10010e40RinvLineEntry": rm10010e40RinvLineEntry,
       "rm10010e40RinvLineIndex": rm10010e40RinvLineIndex,
       "rm10010e40RinvxfpLine": rm10010e40RinvxfpLine,
       "rm10010e40RinvReloadInventory": rm10010e40RinvReloadInventory,
       "rm10010e40RinvHwPlatform": rm10010e40RinvHwPlatform,
       "rm10010e40RinvModulePlatform": rm10010e40RinvModulePlatform,
       "rm10010e40RinvSwPlatform": rm10010e40RinvSwPlatform,
       "rm10010e40RinvGwPlatform": rm10010e40RinvGwPlatform,
       "rm10010e40download": rm10010e40download,
       "rm10010e40DwlOther": rm10010e40DwlOther,
       "rm10010e40DwlrestartProcess": rm10010e40DwlrestartProcess,
       "rm10010e40DwlWarmRestartProcessed": rm10010e40DwlWarmRestartProcessed,
       "rm10010e40DwlColdRestartProcessed": rm10010e40DwlColdRestartProcessed,
       "rm10010e40DwlswBanksUsed": rm10010e40DwlswBanksUsed,
       "rm10010e40DwlSwBank1Used": rm10010e40DwlSwBank1Used,
       "rm10010e40DwlSwBank2Used": rm10010e40DwlSwBank2Used,
       "rm10010e40DwlSwBank1Notempty": rm10010e40DwlSwBank1Notempty,
       "rm10010e40DwlSwBank2Notempty": rm10010e40DwlSwBank2Notempty,
       "rm10010e40DwlgwBanksUsed": rm10010e40DwlgwBanksUsed,
       "rm10010e40DwlGwBank1Used": rm10010e40DwlGwBank1Used,
       "rm10010e40DwlGwBank2Used": rm10010e40DwlGwBank2Used,
       "rm10010e40DwlGwBank3Used": rm10010e40DwlGwBank3Used,
       "rm10010e40DwlGwBank4Used": rm10010e40DwlGwBank4Used,
       "rm10010e40DwlGwBank1Notempty": rm10010e40DwlGwBank1Notempty,
       "rm10010e40DwlGwBank2Notempty": rm10010e40DwlGwBank2Notempty,
       "rm10010e40DwlGwBank3Notempty": rm10010e40DwlGwBank3Notempty,
       "rm10010e40DwlGwBank4Notempty": rm10010e40DwlGwBank4Notempty,
       "rm10010e40DwlClient": rm10010e40DwlClient,
       "rm10010e40DwlLine": rm10010e40DwlLine,
       "rm10010e40Config": rm10010e40Config,
       "rm10010e40CfgAccessCAisCsf": rm10010e40CfgAccessCAisCsf,
       "rm10010e40CfgClientcaiscsfTable": rm10010e40CfgClientcaiscsfTable,
       "rm10010e40CfgClientcaiscsfEntry": rm10010e40CfgClientcaiscsfEntry,
       "rm10010e40CfgClientcaiscsfIndex": rm10010e40CfgClientcaiscsfIndex,
       "rm10010e40CfgReservePortn": rm10010e40CfgReservePortn,
       "rm10010e40CfgStartup": rm10010e40CfgStartup,
       "rm10010e40CfgClientStartupTable": rm10010e40CfgClientStartupTable,
       "rm10010e40CfgClientStartupEntry": rm10010e40CfgClientStartupEntry,
       "rm10010e40CfgClientStartupIndex": rm10010e40CfgClientStartupIndex,
       "rm10010e40CfgSystConfPortPortn": rm10010e40CfgSystConfPortPortn,
       "rm10010e40CfgNetConfPortPortn": rm10010e40CfgNetConfPortPortn,
       "rm10010e40CfgOptionsPortPortn": rm10010e40CfgOptionsPortPortn,
       "rm10010e40CfgLineStartupTable": rm10010e40CfgLineStartupTable,
       "rm10010e40CfgLineStartupEntry": rm10010e40CfgLineStartupEntry,
       "rm10010e40CfgLineStartupIndex": rm10010e40CfgLineStartupIndex,
       "rm10010e40CfgSystConfLinePortn": rm10010e40CfgSystConfLinePortn,
       "rm10010e40CfgOptionsLinePortn": rm10010e40CfgOptionsLinePortn,
       "rm10010e40CfgXfpTable": rm10010e40CfgXfpTable,
       "rm10010e40CfgXfpEntry": rm10010e40CfgXfpEntry,
       "rm10010e40CfgXfpIndex": rm10010e40CfgXfpIndex,
       "rm10010e40CfgSystConfMsaLinePortn": rm10010e40CfgSystConfMsaLinePortn,
       "rm10010e40CfgLabels": rm10010e40CfgLabels,
       "rm10010e40CfgLabelclientTable": rm10010e40CfgLabelclientTable,
       "rm10010e40CfgLabelclientEntry": rm10010e40CfgLabelclientEntry,
       "rm10010e40CfgLabelclientIndex": rm10010e40CfgLabelclientIndex,
       "rm10010e40CfgLabelclientPortn": rm10010e40CfgLabelclientPortn,
       "rm10010e40CfgLabellineTable": rm10010e40CfgLabellineTable,
       "rm10010e40CfgLabellineEntry": rm10010e40CfgLabellineEntry,
       "rm10010e40CfgLabellineIndex": rm10010e40CfgLabellineIndex,
       "rm10010e40CfgLabellinePortn": rm10010e40CfgLabellinePortn,
       "rm10010e40CfgStartuptlh": rm10010e40CfgStartuptlh,
       "rm10010e40CfgOtxtlhTable": rm10010e40CfgOtxtlhTable,
       "rm10010e40CfgOtxtlhEntry": rm10010e40CfgOtxtlhEntry,
       "rm10010e40CfgOtxtlhIndex": rm10010e40CfgOtxtlhIndex,
       "rm10010e40CfgLinePwrLaserPortn": rm10010e40CfgLinePwrLaserPortn,
       "rm10010e40CfgLineFCurrentPortn": rm10010e40CfgLineFCurrentPortn,
       "rm10010e40CfgLineGridCurrentPortn": rm10010e40CfgLineGridCurrentPortn,
       "rm10010e40CfgFPortn": rm10010e40CfgFPortn,
       "rm10010e40CfgRxLineFCurrentPortn": rm10010e40CfgRxLineFCurrentPortn,
       "rm10010e40CfgOther": rm10010e40CfgOther,
       "rm10010e40tablemoduleOther": rm10010e40tablemoduleOther,
       "rm10010e40Cfgmode": rm10010e40Cfgmode,
       "rm10010e40CfgfanLowSpeedThreshold": rm10010e40CfgfanLowSpeedThreshold,
       "rm10010e40CfgfanHighSpeedThreshold": rm10010e40CfgfanHighSpeedThreshold,
       "rm10010e40CfgStartuptablefive": rm10010e40CfgStartuptablefive,
       "rm10010e40CfgOtxtlhcapabilitiesTable": rm10010e40CfgOtxtlhcapabilitiesTable,
       "rm10010e40CfgOtxtlhcapabilitiesEntry": rm10010e40CfgOtxtlhcapabilitiesEntry,
       "rm10010e40CfgOtxtlhcapabilitiesIndex": rm10010e40CfgOtxtlhcapabilitiesIndex,
       "rm10010e40CfgComponentTypePortn": rm10010e40CfgComponentTypePortn,
       "rm10010e40CfgMiscellaneousPortn": rm10010e40CfgMiscellaneousPortn,
       "rm10010e40CfgFirstChannelPortn": rm10010e40CfgFirstChannelPortn,
       "rm10010e40CfgLastChannelPortn": rm10010e40CfgLastChannelPortn,
       "rm10010e40CfgGridPortn": rm10010e40CfgGridPortn,
       "rm10010e40CfgWriteConfiguration": rm10010e40CfgWriteConfiguration,
       "rm10010e40traps": rm10010e40traps,
       "rm10010e40trapPortNumber": rm10010e40trapPortNumber,
       "rm10010e40trapLineNumber": rm10010e40trapLineNumber,
       "rm10010e40trapBoardNumber": rm10010e40trapBoardNumber,
       "rm10010e40LineTrapNotUrgentGoesOn": rm10010e40LineTrapNotUrgentGoesOn,
       "rm10010e40LineTrapNotUrgentGoesOff": rm10010e40LineTrapNotUrgentGoesOff,
       "rm10010e40LineTrapUrgentGoesOn": rm10010e40LineTrapUrgentGoesOn,
       "rm10010e40LineTrapUrgentGoesOff": rm10010e40LineTrapUrgentGoesOff,
       "rm10010e40LineTrapCritGoesOn": rm10010e40LineTrapCritGoesOn,
       "rm10010e40LineTrapCritGoesOff": rm10010e40LineTrapCritGoesOff,
       "rm10010e40ClientTrapNotUrgentGoesOn": rm10010e40ClientTrapNotUrgentGoesOn,
       "rm10010e40ClientTrapNotUrgentGoesOff": rm10010e40ClientTrapNotUrgentGoesOff,
       "rm10010e40ClientTrapUrgentGoesOn": rm10010e40ClientTrapUrgentGoesOn,
       "rm10010e40ClientTrapUrgentGoesOff": rm10010e40ClientTrapUrgentGoesOff,
       "rm10010e40ClientTrapCritGoesOn": rm10010e40ClientTrapCritGoesOn,
       "rm10010e40ClientTrapCritGoesOff": rm10010e40ClientTrapCritGoesOff,
       "rm10010e40PowerTrapUrgentGoesOn": rm10010e40PowerTrapUrgentGoesOn,
       "rm10010e40PowerTrapUrgentGoesOff": rm10010e40PowerTrapUrgentGoesOff,
       "rm10010e40Monitoring": rm10010e40Monitoring,
       "rm10010e40MonOther": rm10010e40MonOther,
       "rm10010e40MonRmon": rm10010e40MonRmon,
       "rm10010e40MonClient": rm10010e40MonClient,
       "rm10010e40MonClientRmonCounter": rm10010e40MonClientRmonCounter,
       "rm10010e40MonupRmonBytesCounterClientInputTable": rm10010e40MonupRmonBytesCounterClientInputTable,
       "rm10010e40MonupRmonBytesCounterClientInputEntry": rm10010e40MonupRmonBytesCounterClientInputEntry,
       "rm10010e40MonupRmonBytesCounterClientInputIndex": rm10010e40MonupRmonBytesCounterClientInputIndex,
       "rm10010e40MonupRmonBytesCounterClientInputValuePortn": rm10010e40MonupRmonBytesCounterClientInputValuePortn,
       "rm10010e40MonupRmonBytesCounterClientInputErrorPortn": rm10010e40MonupRmonBytesCounterClientInputErrorPortn,
       "rm10010e40MonupRmonBytesCounterClientInputOverloadPortn": rm10010e40MonupRmonBytesCounterClientInputOverloadPortn,
       "rm10010e40MonupRmonCrcErrorsCounterClientInputTable": rm10010e40MonupRmonCrcErrorsCounterClientInputTable,
       "rm10010e40MonupRmonCrcErrorsCounterClientInputEntry": rm10010e40MonupRmonCrcErrorsCounterClientInputEntry,
       "rm10010e40MonupRmonCrcErrorsCounterClientInputIndex": rm10010e40MonupRmonCrcErrorsCounterClientInputIndex,
       "rm10010e40MonupRmonCrcErrorsCounterClientInputValuePortn": rm10010e40MonupRmonCrcErrorsCounterClientInputValuePortn,
       "rm10010e40MonupRmonCrcErrorsCounterClientInputErrorPortn": rm10010e40MonupRmonCrcErrorsCounterClientInputErrorPortn,
       "rm10010e40MonupRmonCrcErrorsCounterClientInputOverloadPortn": rm10010e40MonupRmonCrcErrorsCounterClientInputOverloadPortn,
       "rm10010e40MonupRmonPacketsCounterClientInputTable": rm10010e40MonupRmonPacketsCounterClientInputTable,
       "rm10010e40MonupRmonPacketsCounterClientInputEntry": rm10010e40MonupRmonPacketsCounterClientInputEntry,
       "rm10010e40MonupRmonPacketsCounterClientInputIndex": rm10010e40MonupRmonPacketsCounterClientInputIndex,
       "rm10010e40MonupRmonPacketsCounterClientInputValuePortn": rm10010e40MonupRmonPacketsCounterClientInputValuePortn,
       "rm10010e40MonupRmonPacketsCounterClientInputErrorPortn": rm10010e40MonupRmonPacketsCounterClientInputErrorPortn,
       "rm10010e40MonupRmonPacketsCounterClientInputOverloadPortn": rm10010e40MonupRmonPacketsCounterClientInputOverloadPortn,
       "rm10010e40MonupRmonBroadcastCounterClientInputTable": rm10010e40MonupRmonBroadcastCounterClientInputTable,
       "rm10010e40MonupRmonBroadcastCounterClientInputEntry": rm10010e40MonupRmonBroadcastCounterClientInputEntry,
       "rm10010e40MonupRmonBroadcastCounterClientInputIndex": rm10010e40MonupRmonBroadcastCounterClientInputIndex,
       "rm10010e40MonupRmonBroadcastCounterClientInputValuePortn": rm10010e40MonupRmonBroadcastCounterClientInputValuePortn,
       "rm10010e40MonupRmonBroadcastCounterClientInputErrorPortn": rm10010e40MonupRmonBroadcastCounterClientInputErrorPortn,
       "rm10010e40MonupRmonBroadcastCounterClientInputOverloadPortn": rm10010e40MonupRmonBroadcastCounterClientInputOverloadPortn,
       "rm10010e40MonupRmonMulticastCounterClientInputTable": rm10010e40MonupRmonMulticastCounterClientInputTable,
       "rm10010e40MonupRmonMulticastCounterClientInputEntry": rm10010e40MonupRmonMulticastCounterClientInputEntry,
       "rm10010e40MonupRmonMulticastCounterClientInputIndex": rm10010e40MonupRmonMulticastCounterClientInputIndex,
       "rm10010e40MonupRmonMulticastCounterClientInputValuePortn": rm10010e40MonupRmonMulticastCounterClientInputValuePortn,
       "rm10010e40MonupRmonMulticastCounterClientInputErrorPortn": rm10010e40MonupRmonMulticastCounterClientInputErrorPortn,
       "rm10010e40MonupRmonMulticastCounterClientInputOverloadPortn": rm10010e40MonupRmonMulticastCounterClientInputOverloadPortn,
       "rm10010e40MonupRmonPauseFrameCounterClientInputTable": rm10010e40MonupRmonPauseFrameCounterClientInputTable,
       "rm10010e40MonupRmonPauseFrameCounterClientInputEntry": rm10010e40MonupRmonPauseFrameCounterClientInputEntry,
       "rm10010e40MonupRmonPauseFrameCounterClientInputIndex": rm10010e40MonupRmonPauseFrameCounterClientInputIndex,
       "rm10010e40MonupRmonPauseFrameCounterClientInputValuePortn": rm10010e40MonupRmonPauseFrameCounterClientInputValuePortn,
       "rm10010e40MonupRmonPauseFrameCounterClientInputErrorPortn": rm10010e40MonupRmonPauseFrameCounterClientInputErrorPortn,
       "rm10010e40MonupRmonPauseFrameCounterClientInputOverloadPortn": rm10010e40MonupRmonPauseFrameCounterClientInputOverloadPortn}
)
