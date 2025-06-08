# SNMP MIB module (EKINOPS-Rm10010ar-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ekinops_20044/EKINOPS-Rm10010ar-MIB.mib
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

moduleRm10010ar = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67)
)
if mibBuilder.loadTexts:
    moduleRm10010ar.setRevisions(
        ("2014-08-25 00:00",
         "2014-10-14 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Rm10010arMultiRate(TextualConvention, Integer32):
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



class Rm10010arOtxMode(TextualConvention, Integer32):
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



class Rm10010arOtxGrid(TextualConvention, Integer32):
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



class Rm10010arAdjustValue(TextualConvention, Integer32):
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



class Rm10010arClientProtocol(TextualConvention, Integer32):
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



class Rm10010arProtocolMode(TextualConvention, Integer32):
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



class Rm10010arOtxChannel(TextualConvention, Integer32):
    status = "current"


class Rm10010arOrxChannel(TextualConvention, Integer32):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Rm10010aralarms_ObjectIdentity = ObjectIdentity
rm10010aralarms = _Rm10010aralarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2)
)
_Rm10010arAlmOther_ObjectIdentity = ObjectIdentity
rm10010arAlmOther = _Rm10010arAlmOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1)
)
_Rm10010arAlmOtherNurg_ObjectIdentity = ObjectIdentity
rm10010arAlmOtherNurg = _Rm10010arAlmOtherNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 1)
)
_Rm10010arAlmsynthAlm2_ObjectIdentity = ObjectIdentity
rm10010arAlmsynthAlm2 = _Rm10010arAlmsynthAlm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 1, 2)
)
_Rm10010arAlmConfTableSave_Type = EkiOnOff
_Rm10010arAlmConfTableSave_Object = MibScalar
rm10010arAlmConfTableSave = _Rm10010arAlmConfTableSave_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 1, 2, 1),
    _Rm10010arAlmConfTableSave_Type()
)
rm10010arAlmConfTableSave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmConfTableSave.setStatus("current")
_Rm10010arAlmInvUpload_Type = EkiOnOff
_Rm10010arAlmInvUpload_Object = MibScalar
rm10010arAlmInvUpload = _Rm10010arAlmInvUpload_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 1, 2, 2),
    _Rm10010arAlmInvUpload_Type()
)
rm10010arAlmInvUpload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmInvUpload.setStatus("current")
_Rm10010arAlmConfTableLoad_Type = EkiOnOff
_Rm10010arAlmConfTableLoad_Object = MibScalar
rm10010arAlmConfTableLoad = _Rm10010arAlmConfTableLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 1, 2, 3),
    _Rm10010arAlmConfTableLoad_Type()
)
rm10010arAlmConfTableLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmConfTableLoad.setStatus("current")
_Rm10010arAlmCorrelatOff_Type = EkiOnOff
_Rm10010arAlmCorrelatOff_Object = MibScalar
rm10010arAlmCorrelatOff = _Rm10010arAlmCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 1, 2, 4),
    _Rm10010arAlmCorrelatOff_Type()
)
rm10010arAlmCorrelatOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmCorrelatOff.setStatus("current")
_Rm10010arAlmMaintenanceOn_Type = EkiOnOff
_Rm10010arAlmMaintenanceOn_Object = MibScalar
rm10010arAlmMaintenanceOn = _Rm10010arAlmMaintenanceOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 1, 2, 5),
    _Rm10010arAlmMaintenanceOn_Type()
)
rm10010arAlmMaintenanceOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmMaintenanceOn.setStatus("current")
_Rm10010arAlmOtherUrg_ObjectIdentity = ObjectIdentity
rm10010arAlmOtherUrg = _Rm10010arAlmOtherUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 2)
)
_Rm10010arAlmmodFanFail_ObjectIdentity = ObjectIdentity
rm10010arAlmmodFanFail = _Rm10010arAlmmodFanFail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 2, 248)
)
_Rm10010arAlmFanModuleAbsent_Type = EkiOnOff
_Rm10010arAlmFanModuleAbsent_Object = MibScalar
rm10010arAlmFanModuleAbsent = _Rm10010arAlmFanModuleAbsent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 2, 248, 1),
    _Rm10010arAlmFanModuleAbsent_Type()
)
rm10010arAlmFanModuleAbsent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmFanModuleAbsent.setStatus("current")
_Rm10010arAlmFansFail_Type = EkiOnOff
_Rm10010arAlmFansFail_Object = MibScalar
rm10010arAlmFansFail = _Rm10010arAlmFansFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 2, 248, 2),
    _Rm10010arAlmFansFail_Type()
)
rm10010arAlmFansFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmFansFail.setStatus("current")
_Rm10010arAlmFan1Fail_Type = EkiOnOff
_Rm10010arAlmFan1Fail_Object = MibScalar
rm10010arAlmFan1Fail = _Rm10010arAlmFan1Fail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 2, 248, 4),
    _Rm10010arAlmFan1Fail_Type()
)
rm10010arAlmFan1Fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmFan1Fail.setStatus("current")
_Rm10010arAlmFan2Fail_Type = EkiOnOff
_Rm10010arAlmFan2Fail_Object = MibScalar
rm10010arAlmFan2Fail = _Rm10010arAlmFan2Fail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 2, 248, 5),
    _Rm10010arAlmFan2Fail_Type()
)
rm10010arAlmFan2Fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmFan2Fail.setStatus("current")
_Rm10010arAlmFan3Fail_Type = EkiOnOff
_Rm10010arAlmFan3Fail_Object = MibScalar
rm10010arAlmFan3Fail = _Rm10010arAlmFan3Fail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 2, 248, 6),
    _Rm10010arAlmFan3Fail_Type()
)
rm10010arAlmFan3Fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmFan3Fail.setStatus("current")
_Rm10010arAlmFan4Fail_Type = EkiOnOff
_Rm10010arAlmFan4Fail_Object = MibScalar
rm10010arAlmFan4Fail = _Rm10010arAlmFan4Fail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 2, 248, 7),
    _Rm10010arAlmFan4Fail_Type()
)
rm10010arAlmFan4Fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmFan4Fail.setStatus("current")
_Rm10010arAlmOtherCrit_ObjectIdentity = ObjectIdentity
rm10010arAlmOtherCrit = _Rm10010arAlmOtherCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3)
)
_Rm10010arAlmsynthAlm0_ObjectIdentity = ObjectIdentity
rm10010arAlmsynthAlm0 = _Rm10010arAlmsynthAlm0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 0)
)
_Rm10010arAlmFailFan_Type = EkiOnOff
_Rm10010arAlmFailFan_Object = MibScalar
rm10010arAlmFailFan = _Rm10010arAlmFailFan_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 0, 2),
    _Rm10010arAlmFailFan_Type()
)
rm10010arAlmFailFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmFailFan.setStatus("current")
_Rm10010arAlmModGlobFail_Type = EkiOnOff
_Rm10010arAlmModGlobFail_Object = MibScalar
rm10010arAlmModGlobFail = _Rm10010arAlmModGlobFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 0, 9),
    _Rm10010arAlmModGlobFail_Type()
)
rm10010arAlmModGlobFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmModGlobFail.setStatus("current")
_Rm10010arAlmDefFuseA_Type = EkiOnOff
_Rm10010arAlmDefFuseA_Object = MibScalar
rm10010arAlmDefFuseA = _Rm10010arAlmDefFuseA_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 0, 15),
    _Rm10010arAlmDefFuseA_Type()
)
rm10010arAlmDefFuseA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmDefFuseA.setStatus("current")
_Rm10010arAlmDefFuseB_Type = EkiOnOff
_Rm10010arAlmDefFuseB_Object = MibScalar
rm10010arAlmDefFuseB = _Rm10010arAlmDefFuseB_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 0, 16),
    _Rm10010arAlmDefFuseB_Type()
)
rm10010arAlmDefFuseB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmDefFuseB.setStatus("current")
_Rm10010arAlmclientModuleState_ObjectIdentity = ObjectIdentity
rm10010arAlmclientModuleState = _Rm10010arAlmclientModuleState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 40)
)
_Rm10010arAlmCfpInitialize_Type = EkiOnOff
_Rm10010arAlmCfpInitialize_Object = MibScalar
rm10010arAlmCfpInitialize = _Rm10010arAlmCfpInitialize_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 40, 1),
    _Rm10010arAlmCfpInitialize_Type()
)
rm10010arAlmCfpInitialize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmCfpInitialize.setStatus("current")
_Rm10010arAlmCfpLowPower_Type = EkiOnOff
_Rm10010arAlmCfpLowPower_Object = MibScalar
rm10010arAlmCfpLowPower = _Rm10010arAlmCfpLowPower_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 40, 2),
    _Rm10010arAlmCfpLowPower_Type()
)
rm10010arAlmCfpLowPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmCfpLowPower.setStatus("current")
_Rm10010arAlmCfpHighPowerUp_Type = EkiOnOff
_Rm10010arAlmCfpHighPowerUp_Object = MibScalar
rm10010arAlmCfpHighPowerUp = _Rm10010arAlmCfpHighPowerUp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 40, 3),
    _Rm10010arAlmCfpHighPowerUp_Type()
)
rm10010arAlmCfpHighPowerUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmCfpHighPowerUp.setStatus("current")
_Rm10010arAlmCfpTxOff_Type = EkiOnOff
_Rm10010arAlmCfpTxOff_Object = MibScalar
rm10010arAlmCfpTxOff = _Rm10010arAlmCfpTxOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 40, 4),
    _Rm10010arAlmCfpTxOff_Type()
)
rm10010arAlmCfpTxOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmCfpTxOff.setStatus("current")
_Rm10010arAlmCfpTxTurnOn_Type = EkiOnOff
_Rm10010arAlmCfpTxTurnOn_Object = MibScalar
rm10010arAlmCfpTxTurnOn = _Rm10010arAlmCfpTxTurnOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 40, 5),
    _Rm10010arAlmCfpTxTurnOn_Type()
)
rm10010arAlmCfpTxTurnOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmCfpTxTurnOn.setStatus("current")
_Rm10010arAlmCfpReady_Type = EkiOnOff
_Rm10010arAlmCfpReady_Object = MibScalar
rm10010arAlmCfpReady = _Rm10010arAlmCfpReady_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 40, 6),
    _Rm10010arAlmCfpReady_Type()
)
rm10010arAlmCfpReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmCfpReady.setStatus("current")
_Rm10010arAlmCfpFault_Type = EkiOnOff
_Rm10010arAlmCfpFault_Object = MibScalar
rm10010arAlmCfpFault = _Rm10010arAlmCfpFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 40, 7),
    _Rm10010arAlmCfpFault_Type()
)
rm10010arAlmCfpFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmCfpFault.setStatus("current")
_Rm10010arAlmCfpTxTurnOff_Type = EkiOnOff
_Rm10010arAlmCfpTxTurnOff_Object = MibScalar
rm10010arAlmCfpTxTurnOff = _Rm10010arAlmCfpTxTurnOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 40, 8),
    _Rm10010arAlmCfpTxTurnOff_Type()
)
rm10010arAlmCfpTxTurnOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmCfpTxTurnOff.setStatus("current")
_Rm10010arAlmCfpHighPowerDown_Type = EkiOnOff
_Rm10010arAlmCfpHighPowerDown_Object = MibScalar
rm10010arAlmCfpHighPowerDown = _Rm10010arAlmCfpHighPowerDown_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 40, 9),
    _Rm10010arAlmCfpHighPowerDown_Type()
)
rm10010arAlmCfpHighPowerDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmCfpHighPowerDown.setStatus("current")
_Rm10010arAlmclientModuleGeneralStatus_ObjectIdentity = ObjectIdentity
rm10010arAlmclientModuleGeneralStatus = _Rm10010arAlmclientModuleGeneralStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 41)
)
_Rm10010arAlmCfpOutOfAlignment_Type = EkiOnOff
_Rm10010arAlmCfpOutOfAlignment_Object = MibScalar
rm10010arAlmCfpOutOfAlignment = _Rm10010arAlmCfpOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 41, 4),
    _Rm10010arAlmCfpOutOfAlignment_Type()
)
rm10010arAlmCfpOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmCfpOutOfAlignment.setStatus("current")
_Rm10010arAlmCfpRxNetworkLol_Type = EkiOnOff
_Rm10010arAlmCfpRxNetworkLol_Object = MibScalar
rm10010arAlmCfpRxNetworkLol = _Rm10010arAlmCfpRxNetworkLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 41, 5),
    _Rm10010arAlmCfpRxNetworkLol_Type()
)
rm10010arAlmCfpRxNetworkLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmCfpRxNetworkLol.setStatus("current")
_Rm10010arAlmCfpRxLos_Type = EkiOnOff
_Rm10010arAlmCfpRxLos_Object = MibScalar
rm10010arAlmCfpRxLos = _Rm10010arAlmCfpRxLos_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 41, 6),
    _Rm10010arAlmCfpRxLos_Type()
)
rm10010arAlmCfpRxLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmCfpRxLos.setStatus("current")
_Rm10010arAlmCfpTxHostLol_Type = EkiOnOff
_Rm10010arAlmCfpTxHostLol_Object = MibScalar
rm10010arAlmCfpTxHostLol = _Rm10010arAlmCfpTxHostLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 41, 7),
    _Rm10010arAlmCfpTxHostLol_Type()
)
rm10010arAlmCfpTxHostLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmCfpTxHostLol.setStatus("current")
_Rm10010arAlmCfpTxLosf_Type = EkiOnOff
_Rm10010arAlmCfpTxLosf_Object = MibScalar
rm10010arAlmCfpTxLosf = _Rm10010arAlmCfpTxLosf_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 41, 8),
    _Rm10010arAlmCfpTxLosf_Type()
)
rm10010arAlmCfpTxLosf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmCfpTxLosf.setStatus("current")
_Rm10010arAlmCfpTxCmuLol_Type = EkiOnOff
_Rm10010arAlmCfpTxCmuLol_Object = MibScalar
rm10010arAlmCfpTxCmuLol = _Rm10010arAlmCfpTxCmuLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 41, 9),
    _Rm10010arAlmCfpTxCmuLol_Type()
)
rm10010arAlmCfpTxCmuLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmCfpTxCmuLol.setStatus("current")
_Rm10010arAlmCfpTxJitterPllLol_Type = EkiOnOff
_Rm10010arAlmCfpTxJitterPllLol_Object = MibScalar
rm10010arAlmCfpTxJitterPllLol = _Rm10010arAlmCfpTxJitterPllLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 41, 10),
    _Rm10010arAlmCfpTxJitterPllLol_Type()
)
rm10010arAlmCfpTxJitterPllLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmCfpTxJitterPllLol.setStatus("current")
_Rm10010arAlmCfpLossOfRefclk_Type = EkiOnOff
_Rm10010arAlmCfpLossOfRefclk_Object = MibScalar
rm10010arAlmCfpLossOfRefclk = _Rm10010arAlmCfpLossOfRefclk_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 41, 11),
    _Rm10010arAlmCfpLossOfRefclk_Type()
)
rm10010arAlmCfpLossOfRefclk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmCfpLossOfRefclk.setStatus("current")
_Rm10010arAlmCfpHwInterlock_Type = EkiOnOff
_Rm10010arAlmCfpHwInterlock_Object = MibScalar
rm10010arAlmCfpHwInterlock = _Rm10010arAlmCfpHwInterlock_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 41, 14),
    _Rm10010arAlmCfpHwInterlock_Type()
)
rm10010arAlmCfpHwInterlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmCfpHwInterlock.setStatus("current")
_Rm10010arAlmclientGlobalAlarmSummary_ObjectIdentity = ObjectIdentity
rm10010arAlmclientGlobalAlarmSummary = _Rm10010arAlmclientGlobalAlarmSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 42)
)
_Rm10010arAlmCfpSoftGlobAlarmTest_Type = EkiOnOff
_Rm10010arAlmCfpSoftGlobAlarmTest_Object = MibScalar
rm10010arAlmCfpSoftGlobAlarmTest = _Rm10010arAlmCfpSoftGlobAlarmTest_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 42, 1),
    _Rm10010arAlmCfpSoftGlobAlarmTest_Type()
)
rm10010arAlmCfpSoftGlobAlarmTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmCfpSoftGlobAlarmTest.setStatus("current")
_Rm10010arAlmCfpNetworkLaneAlarmWarning2_Type = EkiOnOff
_Rm10010arAlmCfpNetworkLaneAlarmWarning2_Object = MibScalar
rm10010arAlmCfpNetworkLaneAlarmWarning2 = _Rm10010arAlmCfpNetworkLaneAlarmWarning2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 42, 7),
    _Rm10010arAlmCfpNetworkLaneAlarmWarning2_Type()
)
rm10010arAlmCfpNetworkLaneAlarmWarning2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmCfpNetworkLaneAlarmWarning2.setStatus("current")
_Rm10010arAlmCfpModuleState_Type = EkiOnOff
_Rm10010arAlmCfpModuleState_Object = MibScalar
rm10010arAlmCfpModuleState = _Rm10010arAlmCfpModuleState_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 42, 8),
    _Rm10010arAlmCfpModuleState_Type()
)
rm10010arAlmCfpModuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmCfpModuleState.setStatus("current")
_Rm10010arAlmCfpModuleGeneralStatus_Type = EkiOnOff
_Rm10010arAlmCfpModuleGeneralStatus_Object = MibScalar
rm10010arAlmCfpModuleGeneralStatus = _Rm10010arAlmCfpModuleGeneralStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 42, 9),
    _Rm10010arAlmCfpModuleGeneralStatus_Type()
)
rm10010arAlmCfpModuleGeneralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmCfpModuleGeneralStatus.setStatus("current")
_Rm10010arAlmCfpModuleFault_Type = EkiOnOff
_Rm10010arAlmCfpModuleFault_Object = MibScalar
rm10010arAlmCfpModuleFault = _Rm10010arAlmCfpModuleFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 42, 10),
    _Rm10010arAlmCfpModuleFault_Type()
)
rm10010arAlmCfpModuleFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmCfpModuleFault.setStatus("current")
_Rm10010arAlmCfpModuleAlarmWarning1_Type = EkiOnOff
_Rm10010arAlmCfpModuleAlarmWarning1_Object = MibScalar
rm10010arAlmCfpModuleAlarmWarning1 = _Rm10010arAlmCfpModuleAlarmWarning1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 42, 11),
    _Rm10010arAlmCfpModuleAlarmWarning1_Type()
)
rm10010arAlmCfpModuleAlarmWarning1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmCfpModuleAlarmWarning1.setStatus("current")
_Rm10010arAlmCfpModuleAlarmWarning2_Type = EkiOnOff
_Rm10010arAlmCfpModuleAlarmWarning2_Object = MibScalar
rm10010arAlmCfpModuleAlarmWarning2 = _Rm10010arAlmCfpModuleAlarmWarning2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 42, 12),
    _Rm10010arAlmCfpModuleAlarmWarning2_Type()
)
rm10010arAlmCfpModuleAlarmWarning2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmCfpModuleAlarmWarning2.setStatus("current")
_Rm10010arAlmCfpNetworkLaneAlarmWarning1_Type = EkiOnOff
_Rm10010arAlmCfpNetworkLaneAlarmWarning1_Object = MibScalar
rm10010arAlmCfpNetworkLaneAlarmWarning1 = _Rm10010arAlmCfpNetworkLaneAlarmWarning1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 42, 13),
    _Rm10010arAlmCfpNetworkLaneAlarmWarning1_Type()
)
rm10010arAlmCfpNetworkLaneAlarmWarning1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmCfpNetworkLaneAlarmWarning1.setStatus("current")
_Rm10010arAlmCfpNetworkLaneFaultStatus_Type = EkiOnOff
_Rm10010arAlmCfpNetworkLaneFaultStatus_Object = MibScalar
rm10010arAlmCfpNetworkLaneFaultStatus = _Rm10010arAlmCfpNetworkLaneFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 42, 14),
    _Rm10010arAlmCfpNetworkLaneFaultStatus_Type()
)
rm10010arAlmCfpNetworkLaneFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmCfpNetworkLaneFaultStatus.setStatus("current")
_Rm10010arAlmCfpHostLaneFaultStatus_Type = EkiOnOff
_Rm10010arAlmCfpHostLaneFaultStatus_Object = MibScalar
rm10010arAlmCfpHostLaneFaultStatus = _Rm10010arAlmCfpHostLaneFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 42, 15),
    _Rm10010arAlmCfpHostLaneFaultStatus_Type()
)
rm10010arAlmCfpHostLaneFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmCfpHostLaneFaultStatus.setStatus("current")
_Rm10010arAlmCfpGlobAlarmAssertion_Type = EkiOnOff
_Rm10010arAlmCfpGlobAlarmAssertion_Object = MibScalar
rm10010arAlmCfpGlobAlarmAssertion = _Rm10010arAlmCfpGlobAlarmAssertion_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 42, 16),
    _Rm10010arAlmCfpGlobAlarmAssertion_Type()
)
rm10010arAlmCfpGlobAlarmAssertion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmCfpGlobAlarmAssertion.setStatus("current")
_Rm10010arAlmmsaModuleState_ObjectIdentity = ObjectIdentity
rm10010arAlmmsaModuleState = _Rm10010arAlmmsaModuleState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 46)
)
_Rm10010arAlmMsaInitialize_Type = EkiOnOff
_Rm10010arAlmMsaInitialize_Object = MibScalar
rm10010arAlmMsaInitialize = _Rm10010arAlmMsaInitialize_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 46, 1),
    _Rm10010arAlmMsaInitialize_Type()
)
rm10010arAlmMsaInitialize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmMsaInitialize.setStatus("current")
_Rm10010arAlmMsaLowPower_Type = EkiOnOff
_Rm10010arAlmMsaLowPower_Object = MibScalar
rm10010arAlmMsaLowPower = _Rm10010arAlmMsaLowPower_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 46, 2),
    _Rm10010arAlmMsaLowPower_Type()
)
rm10010arAlmMsaLowPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmMsaLowPower.setStatus("current")
_Rm10010arAlmMsaHighPowerUp_Type = EkiOnOff
_Rm10010arAlmMsaHighPowerUp_Object = MibScalar
rm10010arAlmMsaHighPowerUp = _Rm10010arAlmMsaHighPowerUp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 46, 3),
    _Rm10010arAlmMsaHighPowerUp_Type()
)
rm10010arAlmMsaHighPowerUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmMsaHighPowerUp.setStatus("current")
_Rm10010arAlmMsaTxOff_Type = EkiOnOff
_Rm10010arAlmMsaTxOff_Object = MibScalar
rm10010arAlmMsaTxOff = _Rm10010arAlmMsaTxOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 46, 4),
    _Rm10010arAlmMsaTxOff_Type()
)
rm10010arAlmMsaTxOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmMsaTxOff.setStatus("current")
_Rm10010arAlmMsaTxTurnOn_Type = EkiOnOff
_Rm10010arAlmMsaTxTurnOn_Object = MibScalar
rm10010arAlmMsaTxTurnOn = _Rm10010arAlmMsaTxTurnOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 46, 5),
    _Rm10010arAlmMsaTxTurnOn_Type()
)
rm10010arAlmMsaTxTurnOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmMsaTxTurnOn.setStatus("current")
_Rm10010arAlmMsaReady_Type = EkiOnOff
_Rm10010arAlmMsaReady_Object = MibScalar
rm10010arAlmMsaReady = _Rm10010arAlmMsaReady_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 46, 6),
    _Rm10010arAlmMsaReady_Type()
)
rm10010arAlmMsaReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmMsaReady.setStatus("current")
_Rm10010arAlmMsaFault_Type = EkiOnOff
_Rm10010arAlmMsaFault_Object = MibScalar
rm10010arAlmMsaFault = _Rm10010arAlmMsaFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 46, 7),
    _Rm10010arAlmMsaFault_Type()
)
rm10010arAlmMsaFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmMsaFault.setStatus("current")
_Rm10010arAlmMsaTxTurnOff_Type = EkiOnOff
_Rm10010arAlmMsaTxTurnOff_Object = MibScalar
rm10010arAlmMsaTxTurnOff = _Rm10010arAlmMsaTxTurnOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 46, 8),
    _Rm10010arAlmMsaTxTurnOff_Type()
)
rm10010arAlmMsaTxTurnOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmMsaTxTurnOff.setStatus("current")
_Rm10010arAlmMsaHighPowerDown_Type = EkiOnOff
_Rm10010arAlmMsaHighPowerDown_Object = MibScalar
rm10010arAlmMsaHighPowerDown = _Rm10010arAlmMsaHighPowerDown_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 46, 9),
    _Rm10010arAlmMsaHighPowerDown_Type()
)
rm10010arAlmMsaHighPowerDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmMsaHighPowerDown.setStatus("current")
_Rm10010arAlmmsaModuleGeneralStatus_ObjectIdentity = ObjectIdentity
rm10010arAlmmsaModuleGeneralStatus = _Rm10010arAlmmsaModuleGeneralStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 47)
)
_Rm10010arAlmMsaOutOfAlignment_Type = EkiOnOff
_Rm10010arAlmMsaOutOfAlignment_Object = MibScalar
rm10010arAlmMsaOutOfAlignment = _Rm10010arAlmMsaOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 47, 4),
    _Rm10010arAlmMsaOutOfAlignment_Type()
)
rm10010arAlmMsaOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmMsaOutOfAlignment.setStatus("current")
_Rm10010arAlmMsaRxNetworkLol_Type = EkiOnOff
_Rm10010arAlmMsaRxNetworkLol_Object = MibScalar
rm10010arAlmMsaRxNetworkLol = _Rm10010arAlmMsaRxNetworkLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 47, 5),
    _Rm10010arAlmMsaRxNetworkLol_Type()
)
rm10010arAlmMsaRxNetworkLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmMsaRxNetworkLol.setStatus("current")
_Rm10010arAlmMsaRxLos_Type = EkiOnOff
_Rm10010arAlmMsaRxLos_Object = MibScalar
rm10010arAlmMsaRxLos = _Rm10010arAlmMsaRxLos_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 47, 6),
    _Rm10010arAlmMsaRxLos_Type()
)
rm10010arAlmMsaRxLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmMsaRxLos.setStatus("current")
_Rm10010arAlmMsaTxHostLol_Type = EkiOnOff
_Rm10010arAlmMsaTxHostLol_Object = MibScalar
rm10010arAlmMsaTxHostLol = _Rm10010arAlmMsaTxHostLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 47, 7),
    _Rm10010arAlmMsaTxHostLol_Type()
)
rm10010arAlmMsaTxHostLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmMsaTxHostLol.setStatus("current")
_Rm10010arAlmMsaTxLosf_Type = EkiOnOff
_Rm10010arAlmMsaTxLosf_Object = MibScalar
rm10010arAlmMsaTxLosf = _Rm10010arAlmMsaTxLosf_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 47, 8),
    _Rm10010arAlmMsaTxLosf_Type()
)
rm10010arAlmMsaTxLosf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmMsaTxLosf.setStatus("current")
_Rm10010arAlmMsaTxCmuLol_Type = EkiOnOff
_Rm10010arAlmMsaTxCmuLol_Object = MibScalar
rm10010arAlmMsaTxCmuLol = _Rm10010arAlmMsaTxCmuLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 47, 9),
    _Rm10010arAlmMsaTxCmuLol_Type()
)
rm10010arAlmMsaTxCmuLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmMsaTxCmuLol.setStatus("current")
_Rm10010arAlmMsaTxJitterPllLol_Type = EkiOnOff
_Rm10010arAlmMsaTxJitterPllLol_Object = MibScalar
rm10010arAlmMsaTxJitterPllLol = _Rm10010arAlmMsaTxJitterPllLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 47, 10),
    _Rm10010arAlmMsaTxJitterPllLol_Type()
)
rm10010arAlmMsaTxJitterPllLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmMsaTxJitterPllLol.setStatus("current")
_Rm10010arAlmMsaLossOfRefclk_Type = EkiOnOff
_Rm10010arAlmMsaLossOfRefclk_Object = MibScalar
rm10010arAlmMsaLossOfRefclk = _Rm10010arAlmMsaLossOfRefclk_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 47, 11),
    _Rm10010arAlmMsaLossOfRefclk_Type()
)
rm10010arAlmMsaLossOfRefclk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmMsaLossOfRefclk.setStatus("current")
_Rm10010arAlmMsaHwInterlock_Type = EkiOnOff
_Rm10010arAlmMsaHwInterlock_Object = MibScalar
rm10010arAlmMsaHwInterlock = _Rm10010arAlmMsaHwInterlock_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 47, 14),
    _Rm10010arAlmMsaHwInterlock_Type()
)
rm10010arAlmMsaHwInterlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmMsaHwInterlock.setStatus("current")
_Rm10010arAlmmsaGlobalAlarmSummary_ObjectIdentity = ObjectIdentity
rm10010arAlmmsaGlobalAlarmSummary = _Rm10010arAlmmsaGlobalAlarmSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 48)
)
_Rm10010arAlmMsaSoftGlobAlarmTest_Type = EkiOnOff
_Rm10010arAlmMsaSoftGlobAlarmTest_Object = MibScalar
rm10010arAlmMsaSoftGlobAlarmTest = _Rm10010arAlmMsaSoftGlobAlarmTest_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 48, 1),
    _Rm10010arAlmMsaSoftGlobAlarmTest_Type()
)
rm10010arAlmMsaSoftGlobAlarmTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmMsaSoftGlobAlarmTest.setStatus("current")
_Rm10010arAlmMsaNetworkHostAlarmStatus_Type = EkiOnOff
_Rm10010arAlmMsaNetworkHostAlarmStatus_Object = MibScalar
rm10010arAlmMsaNetworkHostAlarmStatus = _Rm10010arAlmMsaNetworkHostAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 48, 6),
    _Rm10010arAlmMsaNetworkHostAlarmStatus_Type()
)
rm10010arAlmMsaNetworkHostAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmMsaNetworkHostAlarmStatus.setStatus("current")
_Rm10010arAlmMsaNetworkLaneAlarmWarning2_Type = EkiOnOff
_Rm10010arAlmMsaNetworkLaneAlarmWarning2_Object = MibScalar
rm10010arAlmMsaNetworkLaneAlarmWarning2 = _Rm10010arAlmMsaNetworkLaneAlarmWarning2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 48, 7),
    _Rm10010arAlmMsaNetworkLaneAlarmWarning2_Type()
)
rm10010arAlmMsaNetworkLaneAlarmWarning2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmMsaNetworkLaneAlarmWarning2.setStatus("current")
_Rm10010arAlmMsaModuleState_Type = EkiOnOff
_Rm10010arAlmMsaModuleState_Object = MibScalar
rm10010arAlmMsaModuleState = _Rm10010arAlmMsaModuleState_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 48, 8),
    _Rm10010arAlmMsaModuleState_Type()
)
rm10010arAlmMsaModuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmMsaModuleState.setStatus("current")
_Rm10010arAlmMsaModuleGeneralStatus_Type = EkiOnOff
_Rm10010arAlmMsaModuleGeneralStatus_Object = MibScalar
rm10010arAlmMsaModuleGeneralStatus = _Rm10010arAlmMsaModuleGeneralStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 48, 9),
    _Rm10010arAlmMsaModuleGeneralStatus_Type()
)
rm10010arAlmMsaModuleGeneralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmMsaModuleGeneralStatus.setStatus("current")
_Rm10010arAlmModuleFault_Type = EkiOnOff
_Rm10010arAlmModuleFault_Object = MibScalar
rm10010arAlmModuleFault = _Rm10010arAlmModuleFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 48, 10),
    _Rm10010arAlmModuleFault_Type()
)
rm10010arAlmModuleFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmModuleFault.setStatus("current")
_Rm10010arAlmMsaModuleAlarmWarning1_Type = EkiOnOff
_Rm10010arAlmMsaModuleAlarmWarning1_Object = MibScalar
rm10010arAlmMsaModuleAlarmWarning1 = _Rm10010arAlmMsaModuleAlarmWarning1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 48, 11),
    _Rm10010arAlmMsaModuleAlarmWarning1_Type()
)
rm10010arAlmMsaModuleAlarmWarning1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmMsaModuleAlarmWarning1.setStatus("current")
_Rm10010arAlmMsaModuleAlarmWarning2_Type = EkiOnOff
_Rm10010arAlmMsaModuleAlarmWarning2_Object = MibScalar
rm10010arAlmMsaModuleAlarmWarning2 = _Rm10010arAlmMsaModuleAlarmWarning2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 48, 12),
    _Rm10010arAlmMsaModuleAlarmWarning2_Type()
)
rm10010arAlmMsaModuleAlarmWarning2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmMsaModuleAlarmWarning2.setStatus("current")
_Rm10010arAlmMsaNetworkLaneAlarmWarning1_Type = EkiOnOff
_Rm10010arAlmMsaNetworkLaneAlarmWarning1_Object = MibScalar
rm10010arAlmMsaNetworkLaneAlarmWarning1 = _Rm10010arAlmMsaNetworkLaneAlarmWarning1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 48, 13),
    _Rm10010arAlmMsaNetworkLaneAlarmWarning1_Type()
)
rm10010arAlmMsaNetworkLaneAlarmWarning1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmMsaNetworkLaneAlarmWarning1.setStatus("current")
_Rm10010arAlmMsaNetworkLaneFaultStatus_Type = EkiOnOff
_Rm10010arAlmMsaNetworkLaneFaultStatus_Object = MibScalar
rm10010arAlmMsaNetworkLaneFaultStatus = _Rm10010arAlmMsaNetworkLaneFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 48, 14),
    _Rm10010arAlmMsaNetworkLaneFaultStatus_Type()
)
rm10010arAlmMsaNetworkLaneFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmMsaNetworkLaneFaultStatus.setStatus("current")
_Rm10010arAlmMsaHostLaneFaultStatus_Type = EkiOnOff
_Rm10010arAlmMsaHostLaneFaultStatus_Object = MibScalar
rm10010arAlmMsaHostLaneFaultStatus = _Rm10010arAlmMsaHostLaneFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 48, 15),
    _Rm10010arAlmMsaHostLaneFaultStatus_Type()
)
rm10010arAlmMsaHostLaneFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmMsaHostLaneFaultStatus.setStatus("current")
_Rm10010arAlmMsaGlobAlarmAssertion_Type = EkiOnOff
_Rm10010arAlmMsaGlobAlarmAssertion_Object = MibScalar
rm10010arAlmMsaGlobAlarmAssertion = _Rm10010arAlmMsaGlobAlarmAssertion_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 48, 16),
    _Rm10010arAlmMsaGlobAlarmAssertion_Type()
)
rm10010arAlmMsaGlobAlarmAssertion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmMsaGlobAlarmAssertion.setStatus("current")
_Rm10010arAlmmsaNetworkTxAlignment_ObjectIdentity = ObjectIdentity
rm10010arAlmmsaNetworkTxAlignment = _Rm10010arAlmmsaNetworkTxAlignment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 49)
)
_Rm10010arAlmNetTxTimingFault_Type = EkiOnOff
_Rm10010arAlmNetTxTimingFault_Object = MibScalar
rm10010arAlmNetTxTimingFault = _Rm10010arAlmNetTxTimingFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 49, 12),
    _Rm10010arAlmNetTxTimingFault_Type()
)
rm10010arAlmNetTxTimingFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmNetTxTimingFault.setStatus("current")
_Rm10010arAlmNetTxReferenceClockFault_Type = EkiOnOff
_Rm10010arAlmNetTxReferenceClockFault_Object = MibScalar
rm10010arAlmNetTxReferenceClockFault = _Rm10010arAlmNetTxReferenceClockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 49, 13),
    _Rm10010arAlmNetTxReferenceClockFault_Type()
)
rm10010arAlmNetTxReferenceClockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmNetTxReferenceClockFault.setStatus("current")
_Rm10010arAlmNetTxCmuLockFault_Type = EkiOnOff
_Rm10010arAlmNetTxCmuLockFault_Object = MibScalar
rm10010arAlmNetTxCmuLockFault = _Rm10010arAlmNetTxCmuLockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 49, 14),
    _Rm10010arAlmNetTxCmuLockFault_Type()
)
rm10010arAlmNetTxCmuLockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmNetTxCmuLockFault.setStatus("current")
_Rm10010arAlmNetTxOutOfAlignment_Type = EkiOnOff
_Rm10010arAlmNetTxOutOfAlignment_Object = MibScalar
rm10010arAlmNetTxOutOfAlignment = _Rm10010arAlmNetTxOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 49, 15),
    _Rm10010arAlmNetTxOutOfAlignment_Type()
)
rm10010arAlmNetTxOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmNetTxOutOfAlignment.setStatus("current")
_Rm10010arAlmNetTxLossOfAlignment_Type = EkiOnOff
_Rm10010arAlmNetTxLossOfAlignment_Object = MibScalar
rm10010arAlmNetTxLossOfAlignment = _Rm10010arAlmNetTxLossOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 49, 16),
    _Rm10010arAlmNetTxLossOfAlignment_Type()
)
rm10010arAlmNetTxLossOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmNetTxLossOfAlignment.setStatus("current")
_Rm10010arAlmmsaNetworkRxAlignment_ObjectIdentity = ObjectIdentity
rm10010arAlmmsaNetworkRxAlignment = _Rm10010arAlmmsaNetworkRxAlignment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 50)
)
_Rm10010arAlmNetRxTimingFault_Type = EkiOnOff
_Rm10010arAlmNetRxTimingFault_Object = MibScalar
rm10010arAlmNetRxTimingFault = _Rm10010arAlmNetRxTimingFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 50, 12),
    _Rm10010arAlmNetRxTimingFault_Type()
)
rm10010arAlmNetRxTimingFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmNetRxTimingFault.setStatus("current")
_Rm10010arAlmNetRxOutOfAlignment_Type = EkiOnOff
_Rm10010arAlmNetRxOutOfAlignment_Object = MibScalar
rm10010arAlmNetRxOutOfAlignment = _Rm10010arAlmNetRxOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 50, 13),
    _Rm10010arAlmNetRxOutOfAlignment_Type()
)
rm10010arAlmNetRxOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmNetRxOutOfAlignment.setStatus("current")
_Rm10010arAlmNetRxLossOfAlignment_Type = EkiOnOff
_Rm10010arAlmNetRxLossOfAlignment_Object = MibScalar
rm10010arAlmNetRxLossOfAlignment = _Rm10010arAlmNetRxLossOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 50, 14),
    _Rm10010arAlmNetRxLossOfAlignment_Type()
)
rm10010arAlmNetRxLossOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmNetRxLossOfAlignment.setStatus("current")
_Rm10010arAlmNetRxModemLockFault_Type = EkiOnOff
_Rm10010arAlmNetRxModemLockFault_Object = MibScalar
rm10010arAlmNetRxModemLockFault = _Rm10010arAlmNetRxModemLockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 50, 15),
    _Rm10010arAlmNetRxModemLockFault_Type()
)
rm10010arAlmNetRxModemLockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmNetRxModemLockFault.setStatus("current")
_Rm10010arAlmNetRxModemSyncDetectFault_Type = EkiOnOff
_Rm10010arAlmNetRxModemSyncDetectFault_Object = MibScalar
rm10010arAlmNetRxModemSyncDetectFault = _Rm10010arAlmNetRxModemSyncDetectFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 50, 16),
    _Rm10010arAlmNetRxModemSyncDetectFault_Type()
)
rm10010arAlmNetRxModemSyncDetectFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmNetRxModemSyncDetectFault.setStatus("current")
_Rm10010arAlmmsaNetworkHostNetworkAlarmSummary_ObjectIdentity = ObjectIdentity
rm10010arAlmmsaNetworkHostNetworkAlarmSummary = _Rm10010arAlmmsaNetworkHostNetworkAlarmSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 51)
)
_Rm10010arAlmNetworkTxAlignment_Type = EkiOnOff
_Rm10010arAlmNetworkTxAlignment_Object = MibScalar
rm10010arAlmNetworkTxAlignment = _Rm10010arAlmNetworkTxAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 51, 11),
    _Rm10010arAlmNetworkTxAlignment_Type()
)
rm10010arAlmNetworkTxAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmNetworkTxAlignment.setStatus("current")
_Rm10010arAlmNetworkRxAlignment_Type = EkiOnOff
_Rm10010arAlmNetworkRxAlignment_Object = MibScalar
rm10010arAlmNetworkRxAlignment = _Rm10010arAlmNetworkRxAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 51, 12),
    _Rm10010arAlmNetworkRxAlignment_Type()
)
rm10010arAlmNetworkRxAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmNetworkRxAlignment.setStatus("current")
_Rm10010arAlmNetworkRxOtn_Type = EkiOnOff
_Rm10010arAlmNetworkRxOtn_Object = MibScalar
rm10010arAlmNetworkRxOtn = _Rm10010arAlmNetworkRxOtn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 51, 13),
    _Rm10010arAlmNetworkRxOtn_Type()
)
rm10010arAlmNetworkRxOtn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmNetworkRxOtn.setStatus("current")
_Rm10010arAlmHostRxAlignment_Type = EkiOnOff
_Rm10010arAlmHostRxAlignment_Object = MibScalar
rm10010arAlmHostRxAlignment = _Rm10010arAlmHostRxAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 51, 14),
    _Rm10010arAlmHostRxAlignment_Type()
)
rm10010arAlmHostRxAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmHostRxAlignment.setStatus("current")
_Rm10010arAlmHostTxAlignment_Type = EkiOnOff
_Rm10010arAlmHostTxAlignment_Object = MibScalar
rm10010arAlmHostTxAlignment = _Rm10010arAlmHostTxAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 51, 15),
    _Rm10010arAlmHostTxAlignment_Type()
)
rm10010arAlmHostTxAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmHostTxAlignment.setStatus("current")
_Rm10010arAlmHostTxOtnStatus_Type = EkiOnOff
_Rm10010arAlmHostTxOtnStatus_Object = MibScalar
rm10010arAlmHostTxOtnStatus = _Rm10010arAlmHostTxOtnStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 51, 16),
    _Rm10010arAlmHostTxOtnStatus_Type()
)
rm10010arAlmHostTxOtnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmHostTxOtnStatus.setStatus("current")
_Rm10010arAlmmsaHostTxAlignment_ObjectIdentity = ObjectIdentity
rm10010arAlmmsaHostTxAlignment = _Rm10010arAlmmsaHostTxAlignment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 52)
)
_Rm10010arAlmHostTxDeskewLockFault_Type = EkiOnOff
_Rm10010arAlmHostTxDeskewLockFault_Object = MibScalar
rm10010arAlmHostTxDeskewLockFault = _Rm10010arAlmHostTxDeskewLockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 52, 13),
    _Rm10010arAlmHostTxDeskewLockFault_Type()
)
rm10010arAlmHostTxDeskewLockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmHostTxDeskewLockFault.setStatus("current")
_Rm10010arAlmHostTxOutOfAlignment_Type = EkiOnOff
_Rm10010arAlmHostTxOutOfAlignment_Object = MibScalar
rm10010arAlmHostTxOutOfAlignment = _Rm10010arAlmHostTxOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 52, 14),
    _Rm10010arAlmHostTxOutOfAlignment_Type()
)
rm10010arAlmHostTxOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmHostTxOutOfAlignment.setStatus("current")
_Rm10010arAlmHostTxLossOfAlignment_Type = EkiOnOff
_Rm10010arAlmHostTxLossOfAlignment_Object = MibScalar
rm10010arAlmHostTxLossOfAlignment = _Rm10010arAlmHostTxLossOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 52, 15),
    _Rm10010arAlmHostTxLossOfAlignment_Type()
)
rm10010arAlmHostTxLossOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmHostTxLossOfAlignment.setStatus("current")
_Rm10010arAlmHostTxCdrLockFault_Type = EkiOnOff
_Rm10010arAlmHostTxCdrLockFault_Object = MibScalar
rm10010arAlmHostTxCdrLockFault = _Rm10010arAlmHostTxCdrLockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 52, 16),
    _Rm10010arAlmHostTxCdrLockFault_Type()
)
rm10010arAlmHostTxCdrLockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmHostTxCdrLockFault.setStatus("current")
_Rm10010arAlmmsaHostRxAlignment_ObjectIdentity = ObjectIdentity
rm10010arAlmmsaHostRxAlignment = _Rm10010arAlmmsaHostRxAlignment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 53)
)
_Rm10010arAlmHostRxCmuLockFault_Type = EkiOnOff
_Rm10010arAlmHostRxCmuLockFault_Object = MibScalar
rm10010arAlmHostRxCmuLockFault = _Rm10010arAlmHostRxCmuLockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 53, 14),
    _Rm10010arAlmHostRxCmuLockFault_Type()
)
rm10010arAlmHostRxCmuLockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmHostRxCmuLockFault.setStatus("current")
_Rm10010arAlmHostRxOutOfAlignment_Type = EkiOnOff
_Rm10010arAlmHostRxOutOfAlignment_Object = MibScalar
rm10010arAlmHostRxOutOfAlignment = _Rm10010arAlmHostRxOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 53, 15),
    _Rm10010arAlmHostRxOutOfAlignment_Type()
)
rm10010arAlmHostRxOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmHostRxOutOfAlignment.setStatus("current")
_Rm10010arAlmHostRxLossOfAlignment_Type = EkiOnOff
_Rm10010arAlmHostRxLossOfAlignment_Object = MibScalar
rm10010arAlmHostRxLossOfAlignment = _Rm10010arAlmHostRxLossOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 1, 3, 53, 16),
    _Rm10010arAlmHostRxLossOfAlignment_Type()
)
rm10010arAlmHostRxLossOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmHostRxLossOfAlignment.setStatus("current")
_Rm10010arAlmClient_ObjectIdentity = ObjectIdentity
rm10010arAlmClient = _Rm10010arAlmClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2)
)
_Rm10010arAlmClientNurg_ObjectIdentity = ObjectIdentity
rm10010arAlmClientNurg = _Rm10010arAlmClientNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 1)
)
_Rm10010arAlmclientNetworkLaneAlarmWarningTable_Object = MibTable
rm10010arAlmclientNetworkLaneAlarmWarningTable = _Rm10010arAlmclientNetworkLaneAlarmWarningTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 1, 56)
)
if mibBuilder.loadTexts:
    rm10010arAlmclientNetworkLaneAlarmWarningTable.setStatus("current")
_Rm10010arAlmclientNetworkLaneAlarmWarningEntry_Object = MibTableRow
rm10010arAlmclientNetworkLaneAlarmWarningEntry = _Rm10010arAlmclientNetworkLaneAlarmWarningEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 1, 56, 1)
)
rm10010arAlmclientNetworkLaneAlarmWarningEntry.setIndexNames(
    (0, "EKINOPS-Rm10010ar-MIB", "rm10010arAlmclientNetworkLaneAlarmWarningIndex"),
)
if mibBuilder.loadTexts:
    rm10010arAlmclientNetworkLaneAlarmWarningEntry.setStatus("current")


class _Rm10010arAlmclientNetworkLaneAlarmWarningIndex_Type(Integer32):
    """Custom type rm10010arAlmclientNetworkLaneAlarmWarningIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010arAlmclientNetworkLaneAlarmWarningIndex_Type.__name__ = "Integer32"
_Rm10010arAlmclientNetworkLaneAlarmWarningIndex_Object = MibTableColumn
rm10010arAlmclientNetworkLaneAlarmWarningIndex = _Rm10010arAlmclientNetworkLaneAlarmWarningIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 1, 56, 1, 1),
    _Rm10010arAlmclientNetworkLaneAlarmWarningIndex_Type()
)
rm10010arAlmclientNetworkLaneAlarmWarningIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmclientNetworkLaneAlarmWarningIndex.setStatus("current")
_Rm10010arAlmClientRxPowerLowAlarmPortn_Type = EkiOnOff
_Rm10010arAlmClientRxPowerLowAlarmPortn_Object = MibTableColumn
rm10010arAlmClientRxPowerLowAlarmPortn = _Rm10010arAlmClientRxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 1, 56, 1, 2),
    _Rm10010arAlmClientRxPowerLowAlarmPortn_Type()
)
rm10010arAlmClientRxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmClientRxPowerLowAlarmPortn.setStatus("current")
_Rm10010arAlmClientRxPowerLowWarningPortn_Type = EkiOnOff
_Rm10010arAlmClientRxPowerLowWarningPortn_Object = MibTableColumn
rm10010arAlmClientRxPowerLowWarningPortn = _Rm10010arAlmClientRxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 1, 56, 1, 3),
    _Rm10010arAlmClientRxPowerLowWarningPortn_Type()
)
rm10010arAlmClientRxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmClientRxPowerLowWarningPortn.setStatus("current")
_Rm10010arAlmClientRxPowerHighWarningPortn_Type = EkiOnOff
_Rm10010arAlmClientRxPowerHighWarningPortn_Object = MibTableColumn
rm10010arAlmClientRxPowerHighWarningPortn = _Rm10010arAlmClientRxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 1, 56, 1, 4),
    _Rm10010arAlmClientRxPowerHighWarningPortn_Type()
)
rm10010arAlmClientRxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmClientRxPowerHighWarningPortn.setStatus("current")
_Rm10010arAlmClientRxPowerHighAlarmPortn_Type = EkiOnOff
_Rm10010arAlmClientRxPowerHighAlarmPortn_Object = MibTableColumn
rm10010arAlmClientRxPowerHighAlarmPortn = _Rm10010arAlmClientRxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 1, 56, 1, 5),
    _Rm10010arAlmClientRxPowerHighAlarmPortn_Type()
)
rm10010arAlmClientRxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmClientRxPowerHighAlarmPortn.setStatus("current")
_Rm10010arAlmLaserTempLowAlarmPortn_Type = EkiOnOff
_Rm10010arAlmLaserTempLowAlarmPortn_Object = MibTableColumn
rm10010arAlmLaserTempLowAlarmPortn = _Rm10010arAlmLaserTempLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 1, 56, 1, 6),
    _Rm10010arAlmLaserTempLowAlarmPortn_Type()
)
rm10010arAlmLaserTempLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmLaserTempLowAlarmPortn.setStatus("current")
_Rm10010arAlmClientLaserTempLowWarningPortn_Type = EkiOnOff
_Rm10010arAlmClientLaserTempLowWarningPortn_Object = MibTableColumn
rm10010arAlmClientLaserTempLowWarningPortn = _Rm10010arAlmClientLaserTempLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 1, 56, 1, 7),
    _Rm10010arAlmClientLaserTempLowWarningPortn_Type()
)
rm10010arAlmClientLaserTempLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmClientLaserTempLowWarningPortn.setStatus("current")
_Rm10010arAlmClientLaserTempHighWarningPortn_Type = EkiOnOff
_Rm10010arAlmClientLaserTempHighWarningPortn_Object = MibTableColumn
rm10010arAlmClientLaserTempHighWarningPortn = _Rm10010arAlmClientLaserTempHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 1, 56, 1, 8),
    _Rm10010arAlmClientLaserTempHighWarningPortn_Type()
)
rm10010arAlmClientLaserTempHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmClientLaserTempHighWarningPortn.setStatus("current")
_Rm10010arAlmClientLaserTempHighAlarmPortn_Type = EkiOnOff
_Rm10010arAlmClientLaserTempHighAlarmPortn_Object = MibTableColumn
rm10010arAlmClientLaserTempHighAlarmPortn = _Rm10010arAlmClientLaserTempHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 1, 56, 1, 9),
    _Rm10010arAlmClientLaserTempHighAlarmPortn_Type()
)
rm10010arAlmClientLaserTempHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmClientLaserTempHighAlarmPortn.setStatus("current")
_Rm10010arAlmClientTxPowerLowAlarmPortn_Type = EkiOnOff
_Rm10010arAlmClientTxPowerLowAlarmPortn_Object = MibTableColumn
rm10010arAlmClientTxPowerLowAlarmPortn = _Rm10010arAlmClientTxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 1, 56, 1, 10),
    _Rm10010arAlmClientTxPowerLowAlarmPortn_Type()
)
rm10010arAlmClientTxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmClientTxPowerLowAlarmPortn.setStatus("current")
_Rm10010arAlmClientTxPowerLowWarningPortn_Type = EkiOnOff
_Rm10010arAlmClientTxPowerLowWarningPortn_Object = MibTableColumn
rm10010arAlmClientTxPowerLowWarningPortn = _Rm10010arAlmClientTxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 1, 56, 1, 11),
    _Rm10010arAlmClientTxPowerLowWarningPortn_Type()
)
rm10010arAlmClientTxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmClientTxPowerLowWarningPortn.setStatus("current")
_Rm10010arAlmClientTxPowerHighWarningPortn_Type = EkiOnOff
_Rm10010arAlmClientTxPowerHighWarningPortn_Object = MibTableColumn
rm10010arAlmClientTxPowerHighWarningPortn = _Rm10010arAlmClientTxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 1, 56, 1, 12),
    _Rm10010arAlmClientTxPowerHighWarningPortn_Type()
)
rm10010arAlmClientTxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmClientTxPowerHighWarningPortn.setStatus("current")
_Rm10010arAlmClientTxPowerHighAlarmPortn_Type = EkiOnOff
_Rm10010arAlmClientTxPowerHighAlarmPortn_Object = MibTableColumn
rm10010arAlmClientTxPowerHighAlarmPortn = _Rm10010arAlmClientTxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 1, 56, 1, 13),
    _Rm10010arAlmClientTxPowerHighAlarmPortn_Type()
)
rm10010arAlmClientTxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmClientTxPowerHighAlarmPortn.setStatus("current")
_Rm10010arAlmClientBiasLowAlarmPortn_Type = EkiOnOff
_Rm10010arAlmClientBiasLowAlarmPortn_Object = MibTableColumn
rm10010arAlmClientBiasLowAlarmPortn = _Rm10010arAlmClientBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 1, 56, 1, 14),
    _Rm10010arAlmClientBiasLowAlarmPortn_Type()
)
rm10010arAlmClientBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmClientBiasLowAlarmPortn.setStatus("current")
_Rm10010arAlmClientBiasLowWarningPortn_Type = EkiOnOff
_Rm10010arAlmClientBiasLowWarningPortn_Object = MibTableColumn
rm10010arAlmClientBiasLowWarningPortn = _Rm10010arAlmClientBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 1, 56, 1, 15),
    _Rm10010arAlmClientBiasLowWarningPortn_Type()
)
rm10010arAlmClientBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmClientBiasLowWarningPortn.setStatus("current")
_Rm10010arAlmClientBiasHighWarningPortn_Type = EkiOnOff
_Rm10010arAlmClientBiasHighWarningPortn_Object = MibTableColumn
rm10010arAlmClientBiasHighWarningPortn = _Rm10010arAlmClientBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 1, 56, 1, 16),
    _Rm10010arAlmClientBiasHighWarningPortn_Type()
)
rm10010arAlmClientBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmClientBiasHighWarningPortn.setStatus("current")
_Rm10010arAlmClientBiasHighAlarmPortn_Type = EkiOnOff
_Rm10010arAlmClientBiasHighAlarmPortn_Object = MibTableColumn
rm10010arAlmClientBiasHighAlarmPortn = _Rm10010arAlmClientBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 1, 56, 1, 17),
    _Rm10010arAlmClientBiasHighAlarmPortn_Type()
)
rm10010arAlmClientBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmClientBiasHighAlarmPortn.setStatus("current")
_Rm10010arAlmclientSfpWarnDdmTable_Object = MibTable
rm10010arAlmclientSfpWarnDdmTable = _Rm10010arAlmclientSfpWarnDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 1, 232)
)
if mibBuilder.loadTexts:
    rm10010arAlmclientSfpWarnDdmTable.setStatus("current")
_Rm10010arAlmclientSfpWarnDdmEntry_Object = MibTableRow
rm10010arAlmclientSfpWarnDdmEntry = _Rm10010arAlmclientSfpWarnDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 1, 232, 1)
)
rm10010arAlmclientSfpWarnDdmEntry.setIndexNames(
    (0, "EKINOPS-Rm10010ar-MIB", "rm10010arAlmclientSfpWarnDdmIndex"),
)
if mibBuilder.loadTexts:
    rm10010arAlmclientSfpWarnDdmEntry.setStatus("current")


class _Rm10010arAlmclientSfpWarnDdmIndex_Type(Integer32):
    """Custom type rm10010arAlmclientSfpWarnDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010arAlmclientSfpWarnDdmIndex_Type.__name__ = "Integer32"
_Rm10010arAlmclientSfpWarnDdmIndex_Object = MibTableColumn
rm10010arAlmclientSfpWarnDdmIndex = _Rm10010arAlmclientSfpWarnDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 1, 232, 1, 1),
    _Rm10010arAlmclientSfpWarnDdmIndex_Type()
)
rm10010arAlmclientSfpWarnDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmclientSfpWarnDdmIndex.setStatus("current")
_Rm10010arAlmTxPwLowWngPortn_Type = EkiOnOff
_Rm10010arAlmTxPwLowWngPortn_Object = MibTableColumn
rm10010arAlmTxPwLowWngPortn = _Rm10010arAlmTxPwLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 1, 232, 1, 2),
    _Rm10010arAlmTxPwLowWngPortn_Type()
)
rm10010arAlmTxPwLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmTxPwLowWngPortn.setStatus("current")
_Rm10010arAlmTxPwrHighWngPortn_Type = EkiOnOff
_Rm10010arAlmTxPwrHighWngPortn_Object = MibTableColumn
rm10010arAlmTxPwrHighWngPortn = _Rm10010arAlmTxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 1, 232, 1, 3),
    _Rm10010arAlmTxPwrHighWngPortn_Type()
)
rm10010arAlmTxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmTxPwrHighWngPortn.setStatus("current")
_Rm10010arAlmTxBiasLowWngPortn_Type = EkiOnOff
_Rm10010arAlmTxBiasLowWngPortn_Object = MibTableColumn
rm10010arAlmTxBiasLowWngPortn = _Rm10010arAlmTxBiasLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 1, 232, 1, 4),
    _Rm10010arAlmTxBiasLowWngPortn_Type()
)
rm10010arAlmTxBiasLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmTxBiasLowWngPortn.setStatus("current")
_Rm10010arAlmTxBiasHighWngPortn_Type = EkiOnOff
_Rm10010arAlmTxBiasHighWngPortn_Object = MibTableColumn
rm10010arAlmTxBiasHighWngPortn = _Rm10010arAlmTxBiasHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 1, 232, 1, 5),
    _Rm10010arAlmTxBiasHighWngPortn_Type()
)
rm10010arAlmTxBiasHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmTxBiasHighWngPortn.setStatus("current")
_Rm10010arAlmVccLowWngPortn_Type = EkiOnOff
_Rm10010arAlmVccLowWngPortn_Object = MibTableColumn
rm10010arAlmVccLowWngPortn = _Rm10010arAlmVccLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 1, 232, 1, 6),
    _Rm10010arAlmVccLowWngPortn_Type()
)
rm10010arAlmVccLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmVccLowWngPortn.setStatus("current")
_Rm10010arAlmVccHighWngPortn_Type = EkiOnOff
_Rm10010arAlmVccHighWngPortn_Object = MibTableColumn
rm10010arAlmVccHighWngPortn = _Rm10010arAlmVccHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 1, 232, 1, 7),
    _Rm10010arAlmVccHighWngPortn_Type()
)
rm10010arAlmVccHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmVccHighWngPortn.setStatus("current")
_Rm10010arAlmTempLowWngPortn_Type = EkiOnOff
_Rm10010arAlmTempLowWngPortn_Object = MibTableColumn
rm10010arAlmTempLowWngPortn = _Rm10010arAlmTempLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 1, 232, 1, 8),
    _Rm10010arAlmTempLowWngPortn_Type()
)
rm10010arAlmTempLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmTempLowWngPortn.setStatus("current")
_Rm10010arAlmTempHighWngPortn_Type = EkiOnOff
_Rm10010arAlmTempHighWngPortn_Object = MibTableColumn
rm10010arAlmTempHighWngPortn = _Rm10010arAlmTempHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 1, 232, 1, 9),
    _Rm10010arAlmTempHighWngPortn_Type()
)
rm10010arAlmTempHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmTempHighWngPortn.setStatus("current")
_Rm10010arAlmRxPwrLowWngPortn_Type = EkiOnOff
_Rm10010arAlmRxPwrLowWngPortn_Object = MibTableColumn
rm10010arAlmRxPwrLowWngPortn = _Rm10010arAlmRxPwrLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 1, 232, 1, 16),
    _Rm10010arAlmRxPwrLowWngPortn_Type()
)
rm10010arAlmRxPwrLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmRxPwrLowWngPortn.setStatus("current")
_Rm10010arAlmRxPwrHighWngPortn_Type = EkiOnOff
_Rm10010arAlmRxPwrHighWngPortn_Object = MibTableColumn
rm10010arAlmRxPwrHighWngPortn = _Rm10010arAlmRxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 1, 232, 1, 17),
    _Rm10010arAlmRxPwrHighWngPortn_Type()
)
rm10010arAlmRxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmRxPwrHighWngPortn.setStatus("current")
_Rm10010arAlmClientUrg_ObjectIdentity = ObjectIdentity
rm10010arAlmClientUrg = _Rm10010arAlmClientUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 2)
)
_Rm10010arAlmclientNetworkLaneFaultTable_Object = MibTable
rm10010arAlmclientNetworkLaneFaultTable = _Rm10010arAlmclientNetworkLaneFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 2, 72)
)
if mibBuilder.loadTexts:
    rm10010arAlmclientNetworkLaneFaultTable.setStatus("current")
_Rm10010arAlmclientNetworkLaneFaultEntry_Object = MibTableRow
rm10010arAlmclientNetworkLaneFaultEntry = _Rm10010arAlmclientNetworkLaneFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 2, 72, 1)
)
rm10010arAlmclientNetworkLaneFaultEntry.setIndexNames(
    (0, "EKINOPS-Rm10010ar-MIB", "rm10010arAlmclientNetworkLaneFaultIndex"),
)
if mibBuilder.loadTexts:
    rm10010arAlmclientNetworkLaneFaultEntry.setStatus("current")


class _Rm10010arAlmclientNetworkLaneFaultIndex_Type(Integer32):
    """Custom type rm10010arAlmclientNetworkLaneFaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010arAlmclientNetworkLaneFaultIndex_Type.__name__ = "Integer32"
_Rm10010arAlmclientNetworkLaneFaultIndex_Object = MibTableColumn
rm10010arAlmclientNetworkLaneFaultIndex = _Rm10010arAlmclientNetworkLaneFaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 2, 72, 1, 1),
    _Rm10010arAlmclientNetworkLaneFaultIndex_Type()
)
rm10010arAlmclientNetworkLaneFaultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmclientNetworkLaneFaultIndex.setStatus("current")
_Rm10010arAlmClientLaneRxFifoErrorPortn_Type = EkiOnOff
_Rm10010arAlmClientLaneRxFifoErrorPortn_Object = MibTableColumn
rm10010arAlmClientLaneRxFifoErrorPortn = _Rm10010arAlmClientLaneRxFifoErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 2, 72, 1, 4),
    _Rm10010arAlmClientLaneRxFifoErrorPortn_Type()
)
rm10010arAlmClientLaneRxFifoErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmClientLaneRxFifoErrorPortn.setStatus("current")
_Rm10010arAlmClientLaneRxLolPortn_Type = EkiOnOff
_Rm10010arAlmClientLaneRxLolPortn_Object = MibTableColumn
rm10010arAlmClientLaneRxLolPortn = _Rm10010arAlmClientLaneRxLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 2, 72, 1, 5),
    _Rm10010arAlmClientLaneRxLolPortn_Type()
)
rm10010arAlmClientLaneRxLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmClientLaneRxLolPortn.setStatus("current")
_Rm10010arAlmClientLaneRxLosPortn_Type = EkiOnOff
_Rm10010arAlmClientLaneRxLosPortn_Object = MibTableColumn
rm10010arAlmClientLaneRxLosPortn = _Rm10010arAlmClientLaneRxLosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 2, 72, 1, 6),
    _Rm10010arAlmClientLaneRxLosPortn_Type()
)
rm10010arAlmClientLaneRxLosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmClientLaneRxLosPortn.setStatus("current")
_Rm10010arAlmClientLaneTxLolPortn_Type = EkiOnOff
_Rm10010arAlmClientLaneTxLolPortn_Object = MibTableColumn
rm10010arAlmClientLaneTxLolPortn = _Rm10010arAlmClientLaneTxLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 2, 72, 1, 8),
    _Rm10010arAlmClientLaneTxLolPortn_Type()
)
rm10010arAlmClientLaneTxLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmClientLaneTxLolPortn.setStatus("current")
_Rm10010arAlmClientLaneTxLosfPortn_Type = EkiOnOff
_Rm10010arAlmClientLaneTxLosfPortn_Object = MibTableColumn
rm10010arAlmClientLaneTxLosfPortn = _Rm10010arAlmClientLaneTxLosfPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 2, 72, 1, 9),
    _Rm10010arAlmClientLaneTxLosfPortn_Type()
)
rm10010arAlmClientLaneTxLosfPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmClientLaneTxLosfPortn.setStatus("current")
_Rm10010arAlmClientLaneApdPowerSupplyPortn_Type = EkiOnOff
_Rm10010arAlmClientLaneApdPowerSupplyPortn_Object = MibTableColumn
rm10010arAlmClientLaneApdPowerSupplyPortn = _Rm10010arAlmClientLaneApdPowerSupplyPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 2, 72, 1, 15),
    _Rm10010arAlmClientLaneApdPowerSupplyPortn_Type()
)
rm10010arAlmClientLaneApdPowerSupplyPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmClientLaneApdPowerSupplyPortn.setStatus("current")
_Rm10010arAlmClientLaneWavelengthUnlockedPortn_Type = EkiOnOff
_Rm10010arAlmClientLaneWavelengthUnlockedPortn_Object = MibTableColumn
rm10010arAlmClientLaneWavelengthUnlockedPortn = _Rm10010arAlmClientLaneWavelengthUnlockedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 2, 72, 1, 16),
    _Rm10010arAlmClientLaneWavelengthUnlockedPortn_Type()
)
rm10010arAlmClientLaneWavelengthUnlockedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmClientLaneWavelengthUnlockedPortn.setStatus("current")
_Rm10010arAlmClientLaneTecFaultPortn_Type = EkiOnOff
_Rm10010arAlmClientLaneTecFaultPortn_Object = MibTableColumn
rm10010arAlmClientLaneTecFaultPortn = _Rm10010arAlmClientLaneTecFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 2, 72, 1, 17),
    _Rm10010arAlmClientLaneTecFaultPortn_Type()
)
rm10010arAlmClientLaneTecFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmClientLaneTecFaultPortn.setStatus("current")
_Rm10010arAlmclientHostLaneFaultTable_Object = MibTable
rm10010arAlmclientHostLaneFaultTable = _Rm10010arAlmclientHostLaneFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 2, 88)
)
if mibBuilder.loadTexts:
    rm10010arAlmclientHostLaneFaultTable.setStatus("current")
_Rm10010arAlmclientHostLaneFaultEntry_Object = MibTableRow
rm10010arAlmclientHostLaneFaultEntry = _Rm10010arAlmclientHostLaneFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 2, 88, 1)
)
rm10010arAlmclientHostLaneFaultEntry.setIndexNames(
    (0, "EKINOPS-Rm10010ar-MIB", "rm10010arAlmclientHostLaneFaultIndex"),
)
if mibBuilder.loadTexts:
    rm10010arAlmclientHostLaneFaultEntry.setStatus("current")


class _Rm10010arAlmclientHostLaneFaultIndex_Type(Integer32):
    """Custom type rm10010arAlmclientHostLaneFaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010arAlmclientHostLaneFaultIndex_Type.__name__ = "Integer32"
_Rm10010arAlmclientHostLaneFaultIndex_Object = MibTableColumn
rm10010arAlmclientHostLaneFaultIndex = _Rm10010arAlmclientHostLaneFaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 2, 88, 1, 1),
    _Rm10010arAlmclientHostLaneFaultIndex_Type()
)
rm10010arAlmclientHostLaneFaultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmclientHostLaneFaultIndex.setStatus("current")
_Rm10010arAlmClientLossOfSyncPortn_Type = EkiOnOff
_Rm10010arAlmClientLossOfSyncPortn_Object = MibTableColumn
rm10010arAlmClientLossOfSyncPortn = _Rm10010arAlmClientLossOfSyncPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 2, 88, 1, 2),
    _Rm10010arAlmClientLossOfSyncPortn_Type()
)
rm10010arAlmClientLossOfSyncPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmClientLossOfSyncPortn.setStatus("current")
_Rm10010arAlmClientInputLossOfSigPortn_Type = EkiOnOff
_Rm10010arAlmClientInputLossOfSigPortn_Object = MibTableColumn
rm10010arAlmClientInputLossOfSigPortn = _Rm10010arAlmClientInputLossOfSigPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 2, 88, 1, 3),
    _Rm10010arAlmClientInputLossOfSigPortn_Type()
)
rm10010arAlmClientInputLossOfSigPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmClientInputLossOfSigPortn.setStatus("current")
_Rm10010arAlmClientLanesMarkerUnlockPortn_Type = EkiOnOff
_Rm10010arAlmClientLanesMarkerUnlockPortn_Object = MibTableColumn
rm10010arAlmClientLanesMarkerUnlockPortn = _Rm10010arAlmClientLanesMarkerUnlockPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 2, 88, 1, 4),
    _Rm10010arAlmClientLanesMarkerUnlockPortn_Type()
)
rm10010arAlmClientLanesMarkerUnlockPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmClientLanesMarkerUnlockPortn.setStatus("current")
_Rm10010arAlmClientLanes6466UnlockPortn_Type = EkiOnOff
_Rm10010arAlmClientLanes6466UnlockPortn_Object = MibTableColumn
rm10010arAlmClientLanes6466UnlockPortn = _Rm10010arAlmClientLanes6466UnlockPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 2, 88, 1, 5),
    _Rm10010arAlmClientLanes6466UnlockPortn_Type()
)
rm10010arAlmClientLanes6466UnlockPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmClientLanes6466UnlockPortn.setStatus("current")
_Rm10010arAlmClientLanesNotAlignedPortn_Type = EkiOnOff
_Rm10010arAlmClientLanesNotAlignedPortn_Object = MibTableColumn
rm10010arAlmClientLanesNotAlignedPortn = _Rm10010arAlmClientLanesNotAlignedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 2, 88, 1, 6),
    _Rm10010arAlmClientLanesNotAlignedPortn_Type()
)
rm10010arAlmClientLanesNotAlignedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmClientLanesNotAlignedPortn.setStatus("current")
_Rm10010arAlmClientCsfDetectedPortn_Type = EkiOnOff
_Rm10010arAlmClientCsfDetectedPortn_Object = MibTableColumn
rm10010arAlmClientCsfDetectedPortn = _Rm10010arAlmClientCsfDetectedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 2, 88, 1, 7),
    _Rm10010arAlmClientCsfDetectedPortn_Type()
)
rm10010arAlmClientCsfDetectedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmClientCsfDetectedPortn.setStatus("current")
_Rm10010arAlmClientTxHostLolPortn_Type = EkiOnOff
_Rm10010arAlmClientTxHostLolPortn_Object = MibTableColumn
rm10010arAlmClientTxHostLolPortn = _Rm10010arAlmClientTxHostLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 2, 88, 1, 10),
    _Rm10010arAlmClientTxHostLolPortn_Type()
)
rm10010arAlmClientTxHostLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmClientTxHostLolPortn.setStatus("current")
_Rm10010arAlmClientLaneTxFifoErrorPortn_Type = EkiOnOff
_Rm10010arAlmClientLaneTxFifoErrorPortn_Object = MibTableColumn
rm10010arAlmClientLaneTxFifoErrorPortn = _Rm10010arAlmClientLaneTxFifoErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 2, 88, 1, 11),
    _Rm10010arAlmClientLaneTxFifoErrorPortn_Type()
)
rm10010arAlmClientLaneTxFifoErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmClientLaneTxFifoErrorPortn.setStatus("current")
_Rm10010arAlmclientSfpAlmDdmTable_Object = MibTable
rm10010arAlmclientSfpAlmDdmTable = _Rm10010arAlmclientSfpAlmDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 2, 216)
)
if mibBuilder.loadTexts:
    rm10010arAlmclientSfpAlmDdmTable.setStatus("current")
_Rm10010arAlmclientSfpAlmDdmEntry_Object = MibTableRow
rm10010arAlmclientSfpAlmDdmEntry = _Rm10010arAlmclientSfpAlmDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 2, 216, 1)
)
rm10010arAlmclientSfpAlmDdmEntry.setIndexNames(
    (0, "EKINOPS-Rm10010ar-MIB", "rm10010arAlmclientSfpAlmDdmIndex"),
)
if mibBuilder.loadTexts:
    rm10010arAlmclientSfpAlmDdmEntry.setStatus("current")


class _Rm10010arAlmclientSfpAlmDdmIndex_Type(Integer32):
    """Custom type rm10010arAlmclientSfpAlmDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010arAlmclientSfpAlmDdmIndex_Type.__name__ = "Integer32"
_Rm10010arAlmclientSfpAlmDdmIndex_Object = MibTableColumn
rm10010arAlmclientSfpAlmDdmIndex = _Rm10010arAlmclientSfpAlmDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 2, 216, 1, 1),
    _Rm10010arAlmclientSfpAlmDdmIndex_Type()
)
rm10010arAlmclientSfpAlmDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmclientSfpAlmDdmIndex.setStatus("current")
_Rm10010arAlmTxPwrLowAlaPortn_Type = EkiOnOff
_Rm10010arAlmTxPwrLowAlaPortn_Object = MibTableColumn
rm10010arAlmTxPwrLowAlaPortn = _Rm10010arAlmTxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 2, 216, 1, 2),
    _Rm10010arAlmTxPwrLowAlaPortn_Type()
)
rm10010arAlmTxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmTxPwrLowAlaPortn.setStatus("current")
_Rm10010arAlmTxPwrHighAlaPortn_Type = EkiOnOff
_Rm10010arAlmTxPwrHighAlaPortn_Object = MibTableColumn
rm10010arAlmTxPwrHighAlaPortn = _Rm10010arAlmTxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 2, 216, 1, 3),
    _Rm10010arAlmTxPwrHighAlaPortn_Type()
)
rm10010arAlmTxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmTxPwrHighAlaPortn.setStatus("current")
_Rm10010arAlmTxBiasLowAlaPortn_Type = EkiOnOff
_Rm10010arAlmTxBiasLowAlaPortn_Object = MibTableColumn
rm10010arAlmTxBiasLowAlaPortn = _Rm10010arAlmTxBiasLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 2, 216, 1, 4),
    _Rm10010arAlmTxBiasLowAlaPortn_Type()
)
rm10010arAlmTxBiasLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmTxBiasLowAlaPortn.setStatus("current")
_Rm10010arAlmTxBiasHighAlaPortn_Type = EkiOnOff
_Rm10010arAlmTxBiasHighAlaPortn_Object = MibTableColumn
rm10010arAlmTxBiasHighAlaPortn = _Rm10010arAlmTxBiasHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 2, 216, 1, 5),
    _Rm10010arAlmTxBiasHighAlaPortn_Type()
)
rm10010arAlmTxBiasHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmTxBiasHighAlaPortn.setStatus("current")
_Rm10010arAlmVccLowAlaPortn_Type = EkiOnOff
_Rm10010arAlmVccLowAlaPortn_Object = MibTableColumn
rm10010arAlmVccLowAlaPortn = _Rm10010arAlmVccLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 2, 216, 1, 6),
    _Rm10010arAlmVccLowAlaPortn_Type()
)
rm10010arAlmVccLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmVccLowAlaPortn.setStatus("current")
_Rm10010arAlmVccHighAlaPortn_Type = EkiOnOff
_Rm10010arAlmVccHighAlaPortn_Object = MibTableColumn
rm10010arAlmVccHighAlaPortn = _Rm10010arAlmVccHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 2, 216, 1, 7),
    _Rm10010arAlmVccHighAlaPortn_Type()
)
rm10010arAlmVccHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmVccHighAlaPortn.setStatus("current")
_Rm10010arAlmTempLowAlaPortn_Type = EkiOnOff
_Rm10010arAlmTempLowAlaPortn_Object = MibTableColumn
rm10010arAlmTempLowAlaPortn = _Rm10010arAlmTempLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 2, 216, 1, 8),
    _Rm10010arAlmTempLowAlaPortn_Type()
)
rm10010arAlmTempLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmTempLowAlaPortn.setStatus("current")
_Rm10010arAlmTempHighAlaPortn_Type = EkiOnOff
_Rm10010arAlmTempHighAlaPortn_Object = MibTableColumn
rm10010arAlmTempHighAlaPortn = _Rm10010arAlmTempHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 2, 216, 1, 9),
    _Rm10010arAlmTempHighAlaPortn_Type()
)
rm10010arAlmTempHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmTempHighAlaPortn.setStatus("current")
_Rm10010arAlmRxPwrLowAlaPortn_Type = EkiOnOff
_Rm10010arAlmRxPwrLowAlaPortn_Object = MibTableColumn
rm10010arAlmRxPwrLowAlaPortn = _Rm10010arAlmRxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 2, 216, 1, 16),
    _Rm10010arAlmRxPwrLowAlaPortn_Type()
)
rm10010arAlmRxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmRxPwrLowAlaPortn.setStatus("current")
_Rm10010arAlmRxPwrHighAlaPortn_Type = EkiOnOff
_Rm10010arAlmRxPwrHighAlaPortn_Object = MibTableColumn
rm10010arAlmRxPwrHighAlaPortn = _Rm10010arAlmRxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 2, 216, 1, 17),
    _Rm10010arAlmRxPwrHighAlaPortn_Type()
)
rm10010arAlmRxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmRxPwrHighAlaPortn.setStatus("current")
_Rm10010arAlmClientCrit_ObjectIdentity = ObjectIdentity
rm10010arAlmClientCrit = _Rm10010arAlmClientCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 3)
)
_Rm10010arAlmsynthAlmPortTable_Object = MibTable
rm10010arAlmsynthAlmPortTable = _Rm10010arAlmsynthAlmPortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 3, 8)
)
if mibBuilder.loadTexts:
    rm10010arAlmsynthAlmPortTable.setStatus("current")
_Rm10010arAlmsynthAlmPortEntry_Object = MibTableRow
rm10010arAlmsynthAlmPortEntry = _Rm10010arAlmsynthAlmPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 3, 8, 1)
)
rm10010arAlmsynthAlmPortEntry.setIndexNames(
    (0, "EKINOPS-Rm10010ar-MIB", "rm10010arAlmsynthAlmPortIndex"),
)
if mibBuilder.loadTexts:
    rm10010arAlmsynthAlmPortEntry.setStatus("current")


class _Rm10010arAlmsynthAlmPortIndex_Type(Integer32):
    """Custom type rm10010arAlmsynthAlmPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010arAlmsynthAlmPortIndex_Type.__name__ = "Integer32"
_Rm10010arAlmsynthAlmPortIndex_Object = MibTableColumn
rm10010arAlmsynthAlmPortIndex = _Rm10010arAlmsynthAlmPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 3, 8, 1, 1),
    _Rm10010arAlmsynthAlmPortIndex_Type()
)
rm10010arAlmsynthAlmPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmsynthAlmPortIndex.setStatus("current")
_Rm10010arAlmSfpAbsentPortn_Type = EkiOnOff
_Rm10010arAlmSfpAbsentPortn_Object = MibTableColumn
rm10010arAlmSfpAbsentPortn = _Rm10010arAlmSfpAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 3, 8, 1, 2),
    _Rm10010arAlmSfpAbsentPortn_Type()
)
rm10010arAlmSfpAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmSfpAbsentPortn.setStatus("current")
_Rm10010arAlmDdmAbsentPortn_Type = EkiOnOff
_Rm10010arAlmDdmAbsentPortn_Object = MibTableColumn
rm10010arAlmDdmAbsentPortn = _Rm10010arAlmDdmAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 3, 8, 1, 3),
    _Rm10010arAlmDdmAbsentPortn_Type()
)
rm10010arAlmDdmAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmDdmAbsentPortn.setStatus("current")
_Rm10010arAlmHwFailAccPortn_Type = EkiOnOff
_Rm10010arAlmHwFailAccPortn_Object = MibTableColumn
rm10010arAlmHwFailAccPortn = _Rm10010arAlmHwFailAccPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 3, 8, 1, 5),
    _Rm10010arAlmHwFailAccPortn_Type()
)
rm10010arAlmHwFailAccPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmHwFailAccPortn.setStatus("current")
_Rm10010arAlmDwLsdPortn_Type = EkiOnOff
_Rm10010arAlmDwLsdPortn_Object = MibTableColumn
rm10010arAlmDwLsdPortn = _Rm10010arAlmDwLsdPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 3, 8, 1, 6),
    _Rm10010arAlmDwLsdPortn_Type()
)
rm10010arAlmDwLsdPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmDwLsdPortn.setStatus("current")
_Rm10010arAlmClientLocalOosPortn_Type = EkiOnOff
_Rm10010arAlmClientLocalOosPortn_Object = MibTableColumn
rm10010arAlmClientLocalOosPortn = _Rm10010arAlmClientLocalOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 3, 8, 1, 7),
    _Rm10010arAlmClientLocalOosPortn_Type()
)
rm10010arAlmClientLocalOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmClientLocalOosPortn.setStatus("current")
_Rm10010arAlmClientRemoteOosPortn_Type = EkiOnOff
_Rm10010arAlmClientRemoteOosPortn_Object = MibTableColumn
rm10010arAlmClientRemoteOosPortn = _Rm10010arAlmClientRemoteOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 3, 8, 1, 8),
    _Rm10010arAlmClientRemoteOosPortn_Type()
)
rm10010arAlmClientRemoteOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmClientRemoteOosPortn.setStatus("current")
_Rm10010arAlmDwCaisPortn_Type = EkiOnOff
_Rm10010arAlmDwCaisPortn_Object = MibTableColumn
rm10010arAlmDwCaisPortn = _Rm10010arAlmDwCaisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 3, 8, 1, 9),
    _Rm10010arAlmDwCaisPortn_Type()
)
rm10010arAlmDwCaisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmDwCaisPortn.setStatus("current")
_Rm10010arAlmSfpDdmWarningPortn_Type = EkiOnOff
_Rm10010arAlmSfpDdmWarningPortn_Object = MibTableColumn
rm10010arAlmSfpDdmWarningPortn = _Rm10010arAlmSfpDdmWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 3, 8, 1, 10),
    _Rm10010arAlmSfpDdmWarningPortn_Type()
)
rm10010arAlmSfpDdmWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmSfpDdmWarningPortn.setStatus("current")
_Rm10010arAlmSfpDdmAlmPortn_Type = EkiOnOff
_Rm10010arAlmSfpDdmAlmPortn_Object = MibTableColumn
rm10010arAlmSfpDdmAlmPortn = _Rm10010arAlmSfpDdmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 3, 8, 1, 11),
    _Rm10010arAlmSfpDdmAlmPortn_Type()
)
rm10010arAlmSfpDdmAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmSfpDdmAlmPortn.setStatus("current")
_Rm10010arAlmFailAccPortn_Type = EkiOnOff
_Rm10010arAlmFailAccPortn_Object = MibTableColumn
rm10010arAlmFailAccPortn = _Rm10010arAlmFailAccPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 3, 8, 1, 13),
    _Rm10010arAlmFailAccPortn_Type()
)
rm10010arAlmFailAccPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmFailAccPortn.setStatus("current")
_Rm10010arAlmUpCsfPortn_Type = EkiOnOff
_Rm10010arAlmUpCsfPortn_Object = MibTableColumn
rm10010arAlmUpCsfPortn = _Rm10010arAlmUpCsfPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 2, 3, 8, 1, 17),
    _Rm10010arAlmUpCsfPortn_Type()
)
rm10010arAlmUpCsfPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmUpCsfPortn.setStatus("current")
_Rm10010arAlmLine_ObjectIdentity = ObjectIdentity
rm10010arAlmLine = _Rm10010arAlmLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3)
)
_Rm10010arAlmLineNurg_ObjectIdentity = ObjectIdentity
rm10010arAlmLineNurg = _Rm10010arAlmLineNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 1)
)
_Rm10010arAlmlineNetworkLaneAlarmWarning1Table_Object = MibTable
rm10010arAlmlineNetworkLaneAlarmWarning1Table = _Rm10010arAlmlineNetworkLaneAlarmWarning1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 1, 104)
)
if mibBuilder.loadTexts:
    rm10010arAlmlineNetworkLaneAlarmWarning1Table.setStatus("current")
_Rm10010arAlmlineNetworkLaneAlarmWarning1Entry_Object = MibTableRow
rm10010arAlmlineNetworkLaneAlarmWarning1Entry = _Rm10010arAlmlineNetworkLaneAlarmWarning1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 1, 104, 1)
)
rm10010arAlmlineNetworkLaneAlarmWarning1Entry.setIndexNames(
    (0, "EKINOPS-Rm10010ar-MIB", "rm10010arAlmlineNetworkLaneAlarmWarning1Index"),
)
if mibBuilder.loadTexts:
    rm10010arAlmlineNetworkLaneAlarmWarning1Entry.setStatus("current")


class _Rm10010arAlmlineNetworkLaneAlarmWarning1Index_Type(Integer32):
    """Custom type rm10010arAlmlineNetworkLaneAlarmWarning1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010arAlmlineNetworkLaneAlarmWarning1Index_Type.__name__ = "Integer32"
_Rm10010arAlmlineNetworkLaneAlarmWarning1Index_Object = MibTableColumn
rm10010arAlmlineNetworkLaneAlarmWarning1Index = _Rm10010arAlmlineNetworkLaneAlarmWarning1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 1, 104, 1, 1),
    _Rm10010arAlmlineNetworkLaneAlarmWarning1Index_Type()
)
rm10010arAlmlineNetworkLaneAlarmWarning1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmlineNetworkLaneAlarmWarning1Index.setStatus("current")
_Rm10010arAlmLineRxPowerLowAlarmPortn_Type = EkiOnOff
_Rm10010arAlmLineRxPowerLowAlarmPortn_Object = MibTableColumn
rm10010arAlmLineRxPowerLowAlarmPortn = _Rm10010arAlmLineRxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 1, 104, 1, 2),
    _Rm10010arAlmLineRxPowerLowAlarmPortn_Type()
)
rm10010arAlmLineRxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmLineRxPowerLowAlarmPortn.setStatus("current")
_Rm10010arAlmLineRxPowerLowWarningPortn_Type = EkiOnOff
_Rm10010arAlmLineRxPowerLowWarningPortn_Object = MibTableColumn
rm10010arAlmLineRxPowerLowWarningPortn = _Rm10010arAlmLineRxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 1, 104, 1, 3),
    _Rm10010arAlmLineRxPowerLowWarningPortn_Type()
)
rm10010arAlmLineRxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmLineRxPowerLowWarningPortn.setStatus("current")
_Rm10010arAlmLineRxPowerHighWarningPortn_Type = EkiOnOff
_Rm10010arAlmLineRxPowerHighWarningPortn_Object = MibTableColumn
rm10010arAlmLineRxPowerHighWarningPortn = _Rm10010arAlmLineRxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 1, 104, 1, 4),
    _Rm10010arAlmLineRxPowerHighWarningPortn_Type()
)
rm10010arAlmLineRxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmLineRxPowerHighWarningPortn.setStatus("current")
_Rm10010arAlmLineRxPowerHighAlarmPortn_Type = EkiOnOff
_Rm10010arAlmLineRxPowerHighAlarmPortn_Object = MibTableColumn
rm10010arAlmLineRxPowerHighAlarmPortn = _Rm10010arAlmLineRxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 1, 104, 1, 5),
    _Rm10010arAlmLineRxPowerHighAlarmPortn_Type()
)
rm10010arAlmLineRxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmLineRxPowerHighAlarmPortn.setStatus("current")
_Rm10010arAlmLineLaserTempLowAlarmPortn_Type = EkiOnOff
_Rm10010arAlmLineLaserTempLowAlarmPortn_Object = MibTableColumn
rm10010arAlmLineLaserTempLowAlarmPortn = _Rm10010arAlmLineLaserTempLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 1, 104, 1, 6),
    _Rm10010arAlmLineLaserTempLowAlarmPortn_Type()
)
rm10010arAlmLineLaserTempLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmLineLaserTempLowAlarmPortn.setStatus("current")
_Rm10010arAlmLineLaserTempLowWarningPortn_Type = EkiOnOff
_Rm10010arAlmLineLaserTempLowWarningPortn_Object = MibTableColumn
rm10010arAlmLineLaserTempLowWarningPortn = _Rm10010arAlmLineLaserTempLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 1, 104, 1, 7),
    _Rm10010arAlmLineLaserTempLowWarningPortn_Type()
)
rm10010arAlmLineLaserTempLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmLineLaserTempLowWarningPortn.setStatus("current")
_Rm10010arAlmLineLaserTempHighWarningPortn_Type = EkiOnOff
_Rm10010arAlmLineLaserTempHighWarningPortn_Object = MibTableColumn
rm10010arAlmLineLaserTempHighWarningPortn = _Rm10010arAlmLineLaserTempHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 1, 104, 1, 8),
    _Rm10010arAlmLineLaserTempHighWarningPortn_Type()
)
rm10010arAlmLineLaserTempHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmLineLaserTempHighWarningPortn.setStatus("current")
_Rm10010arAlmLineLaserTempHighAlarmPortn_Type = EkiOnOff
_Rm10010arAlmLineLaserTempHighAlarmPortn_Object = MibTableColumn
rm10010arAlmLineLaserTempHighAlarmPortn = _Rm10010arAlmLineLaserTempHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 1, 104, 1, 9),
    _Rm10010arAlmLineLaserTempHighAlarmPortn_Type()
)
rm10010arAlmLineLaserTempHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmLineLaserTempHighAlarmPortn.setStatus("current")
_Rm10010arAlmLineTxPowerLowAlarmPortn_Type = EkiOnOff
_Rm10010arAlmLineTxPowerLowAlarmPortn_Object = MibTableColumn
rm10010arAlmLineTxPowerLowAlarmPortn = _Rm10010arAlmLineTxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 1, 104, 1, 10),
    _Rm10010arAlmLineTxPowerLowAlarmPortn_Type()
)
rm10010arAlmLineTxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmLineTxPowerLowAlarmPortn.setStatus("current")
_Rm10010arAlmLineTxPowerLowWarningPortn_Type = EkiOnOff
_Rm10010arAlmLineTxPowerLowWarningPortn_Object = MibTableColumn
rm10010arAlmLineTxPowerLowWarningPortn = _Rm10010arAlmLineTxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 1, 104, 1, 11),
    _Rm10010arAlmLineTxPowerLowWarningPortn_Type()
)
rm10010arAlmLineTxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmLineTxPowerLowWarningPortn.setStatus("current")
_Rm10010arAlmLineTxPowerHighWarningPortn_Type = EkiOnOff
_Rm10010arAlmLineTxPowerHighWarningPortn_Object = MibTableColumn
rm10010arAlmLineTxPowerHighWarningPortn = _Rm10010arAlmLineTxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 1, 104, 1, 12),
    _Rm10010arAlmLineTxPowerHighWarningPortn_Type()
)
rm10010arAlmLineTxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmLineTxPowerHighWarningPortn.setStatus("current")
_Rm10010arAlmLineTxPowerHighAlarmPortn_Type = EkiOnOff
_Rm10010arAlmLineTxPowerHighAlarmPortn_Object = MibTableColumn
rm10010arAlmLineTxPowerHighAlarmPortn = _Rm10010arAlmLineTxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 1, 104, 1, 13),
    _Rm10010arAlmLineTxPowerHighAlarmPortn_Type()
)
rm10010arAlmLineTxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmLineTxPowerHighAlarmPortn.setStatus("current")
_Rm10010arAlmLineBiasLowAlarmPortn_Type = EkiOnOff
_Rm10010arAlmLineBiasLowAlarmPortn_Object = MibTableColumn
rm10010arAlmLineBiasLowAlarmPortn = _Rm10010arAlmLineBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 1, 104, 1, 14),
    _Rm10010arAlmLineBiasLowAlarmPortn_Type()
)
rm10010arAlmLineBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmLineBiasLowAlarmPortn.setStatus("current")
_Rm10010arAlmLineBiasLowWarningPortn_Type = EkiOnOff
_Rm10010arAlmLineBiasLowWarningPortn_Object = MibTableColumn
rm10010arAlmLineBiasLowWarningPortn = _Rm10010arAlmLineBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 1, 104, 1, 15),
    _Rm10010arAlmLineBiasLowWarningPortn_Type()
)
rm10010arAlmLineBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmLineBiasLowWarningPortn.setStatus("current")
_Rm10010arAlmLineBiasHighWarningPortn_Type = EkiOnOff
_Rm10010arAlmLineBiasHighWarningPortn_Object = MibTableColumn
rm10010arAlmLineBiasHighWarningPortn = _Rm10010arAlmLineBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 1, 104, 1, 16),
    _Rm10010arAlmLineBiasHighWarningPortn_Type()
)
rm10010arAlmLineBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmLineBiasHighWarningPortn.setStatus("current")
_Rm10010arAlmLineBiasHighAlarmPortn_Type = EkiOnOff
_Rm10010arAlmLineBiasHighAlarmPortn_Object = MibTableColumn
rm10010arAlmLineBiasHighAlarmPortn = _Rm10010arAlmLineBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 1, 104, 1, 17),
    _Rm10010arAlmLineBiasHighAlarmPortn_Type()
)
rm10010arAlmLineBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmLineBiasHighAlarmPortn.setStatus("current")
_Rm10010arAlmlineNetworkLaneAlarmWarning2Table_Object = MibTable
rm10010arAlmlineNetworkLaneAlarmWarning2Table = _Rm10010arAlmlineNetworkLaneAlarmWarning2Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 1, 120)
)
if mibBuilder.loadTexts:
    rm10010arAlmlineNetworkLaneAlarmWarning2Table.setStatus("current")
_Rm10010arAlmlineNetworkLaneAlarmWarning2Entry_Object = MibTableRow
rm10010arAlmlineNetworkLaneAlarmWarning2Entry = _Rm10010arAlmlineNetworkLaneAlarmWarning2Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 1, 120, 1)
)
rm10010arAlmlineNetworkLaneAlarmWarning2Entry.setIndexNames(
    (0, "EKINOPS-Rm10010ar-MIB", "rm10010arAlmlineNetworkLaneAlarmWarning2Index"),
)
if mibBuilder.loadTexts:
    rm10010arAlmlineNetworkLaneAlarmWarning2Entry.setStatus("current")


class _Rm10010arAlmlineNetworkLaneAlarmWarning2Index_Type(Integer32):
    """Custom type rm10010arAlmlineNetworkLaneAlarmWarning2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010arAlmlineNetworkLaneAlarmWarning2Index_Type.__name__ = "Integer32"
_Rm10010arAlmlineNetworkLaneAlarmWarning2Index_Object = MibTableColumn
rm10010arAlmlineNetworkLaneAlarmWarning2Index = _Rm10010arAlmlineNetworkLaneAlarmWarning2Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 1, 120, 1, 1),
    _Rm10010arAlmlineNetworkLaneAlarmWarning2Index_Type()
)
rm10010arAlmlineNetworkLaneAlarmWarning2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmlineNetworkLaneAlarmWarning2Index.setStatus("current")
_Rm10010arAlmTxModulatorBiasLowAlarmPortn_Type = EkiOnOff
_Rm10010arAlmTxModulatorBiasLowAlarmPortn_Object = MibTableColumn
rm10010arAlmTxModulatorBiasLowAlarmPortn = _Rm10010arAlmTxModulatorBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 1, 120, 1, 2),
    _Rm10010arAlmTxModulatorBiasLowAlarmPortn_Type()
)
rm10010arAlmTxModulatorBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmTxModulatorBiasLowAlarmPortn.setStatus("current")
_Rm10010arAlmTxModulatorBiasLowWarningPortn_Type = EkiOnOff
_Rm10010arAlmTxModulatorBiasLowWarningPortn_Object = MibTableColumn
rm10010arAlmTxModulatorBiasLowWarningPortn = _Rm10010arAlmTxModulatorBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 1, 120, 1, 3),
    _Rm10010arAlmTxModulatorBiasLowWarningPortn_Type()
)
rm10010arAlmTxModulatorBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmTxModulatorBiasLowWarningPortn.setStatus("current")
_Rm10010arAlmTxModulatorBiasHighWarningPortn_Type = EkiOnOff
_Rm10010arAlmTxModulatorBiasHighWarningPortn_Object = MibTableColumn
rm10010arAlmTxModulatorBiasHighWarningPortn = _Rm10010arAlmTxModulatorBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 1, 120, 1, 4),
    _Rm10010arAlmTxModulatorBiasHighWarningPortn_Type()
)
rm10010arAlmTxModulatorBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmTxModulatorBiasHighWarningPortn.setStatus("current")
_Rm10010arAlmTxModulatorBiasHighAlarmPortn_Type = EkiOnOff
_Rm10010arAlmTxModulatorBiasHighAlarmPortn_Object = MibTableColumn
rm10010arAlmTxModulatorBiasHighAlarmPortn = _Rm10010arAlmTxModulatorBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 1, 120, 1, 5),
    _Rm10010arAlmTxModulatorBiasHighAlarmPortn_Type()
)
rm10010arAlmTxModulatorBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmTxModulatorBiasHighAlarmPortn.setStatus("current")
_Rm10010arAlmRxLaserTempLowAlarmPortn_Type = EkiOnOff
_Rm10010arAlmRxLaserTempLowAlarmPortn_Object = MibTableColumn
rm10010arAlmRxLaserTempLowAlarmPortn = _Rm10010arAlmRxLaserTempLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 1, 120, 1, 6),
    _Rm10010arAlmRxLaserTempLowAlarmPortn_Type()
)
rm10010arAlmRxLaserTempLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmRxLaserTempLowAlarmPortn.setStatus("current")
_Rm10010arAlmRxLaserTempLowWarningPortn_Type = EkiOnOff
_Rm10010arAlmRxLaserTempLowWarningPortn_Object = MibTableColumn
rm10010arAlmRxLaserTempLowWarningPortn = _Rm10010arAlmRxLaserTempLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 1, 120, 1, 7),
    _Rm10010arAlmRxLaserTempLowWarningPortn_Type()
)
rm10010arAlmRxLaserTempLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmRxLaserTempLowWarningPortn.setStatus("current")
_Rm10010arAlmRxLaserTempHighWarningPortn_Type = EkiOnOff
_Rm10010arAlmRxLaserTempHighWarningPortn_Object = MibTableColumn
rm10010arAlmRxLaserTempHighWarningPortn = _Rm10010arAlmRxLaserTempHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 1, 120, 1, 8),
    _Rm10010arAlmRxLaserTempHighWarningPortn_Type()
)
rm10010arAlmRxLaserTempHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmRxLaserTempHighWarningPortn.setStatus("current")
_Rm10010arAlmRxLaserTempHighAlarmPortn_Type = EkiOnOff
_Rm10010arAlmRxLaserTempHighAlarmPortn_Object = MibTableColumn
rm10010arAlmRxLaserTempHighAlarmPortn = _Rm10010arAlmRxLaserTempHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 1, 120, 1, 9),
    _Rm10010arAlmRxLaserTempHighAlarmPortn_Type()
)
rm10010arAlmRxLaserTempHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmRxLaserTempHighAlarmPortn.setStatus("current")
_Rm10010arAlmRxLaserOutputLowAlarmPortn_Type = EkiOnOff
_Rm10010arAlmRxLaserOutputLowAlarmPortn_Object = MibTableColumn
rm10010arAlmRxLaserOutputLowAlarmPortn = _Rm10010arAlmRxLaserOutputLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 1, 120, 1, 10),
    _Rm10010arAlmRxLaserOutputLowAlarmPortn_Type()
)
rm10010arAlmRxLaserOutputLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmRxLaserOutputLowAlarmPortn.setStatus("current")
_Rm10010arAlmRxLaserOutputLowWarningPortn_Type = EkiOnOff
_Rm10010arAlmRxLaserOutputLowWarningPortn_Object = MibTableColumn
rm10010arAlmRxLaserOutputLowWarningPortn = _Rm10010arAlmRxLaserOutputLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 1, 120, 1, 11),
    _Rm10010arAlmRxLaserOutputLowWarningPortn_Type()
)
rm10010arAlmRxLaserOutputLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmRxLaserOutputLowWarningPortn.setStatus("current")
_Rm10010arAlmRxLaserOutputHighWarningPortn_Type = EkiOnOff
_Rm10010arAlmRxLaserOutputHighWarningPortn_Object = MibTableColumn
rm10010arAlmRxLaserOutputHighWarningPortn = _Rm10010arAlmRxLaserOutputHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 1, 120, 1, 12),
    _Rm10010arAlmRxLaserOutputHighWarningPortn_Type()
)
rm10010arAlmRxLaserOutputHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmRxLaserOutputHighWarningPortn.setStatus("current")
_Rm10010arAlmRxLaserOutputHighAlarmPortn_Type = EkiOnOff
_Rm10010arAlmRxLaserOutputHighAlarmPortn_Object = MibTableColumn
rm10010arAlmRxLaserOutputHighAlarmPortn = _Rm10010arAlmRxLaserOutputHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 1, 120, 1, 13),
    _Rm10010arAlmRxLaserOutputHighAlarmPortn_Type()
)
rm10010arAlmRxLaserOutputHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmRxLaserOutputHighAlarmPortn.setStatus("current")
_Rm10010arAlmRxLaserBiasLowAlarmPortn_Type = EkiOnOff
_Rm10010arAlmRxLaserBiasLowAlarmPortn_Object = MibTableColumn
rm10010arAlmRxLaserBiasLowAlarmPortn = _Rm10010arAlmRxLaserBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 1, 120, 1, 14),
    _Rm10010arAlmRxLaserBiasLowAlarmPortn_Type()
)
rm10010arAlmRxLaserBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmRxLaserBiasLowAlarmPortn.setStatus("current")
_Rm10010arAlmRxLaserBiasLowWarningPortn_Type = EkiOnOff
_Rm10010arAlmRxLaserBiasLowWarningPortn_Object = MibTableColumn
rm10010arAlmRxLaserBiasLowWarningPortn = _Rm10010arAlmRxLaserBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 1, 120, 1, 15),
    _Rm10010arAlmRxLaserBiasLowWarningPortn_Type()
)
rm10010arAlmRxLaserBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmRxLaserBiasLowWarningPortn.setStatus("current")
_Rm10010arAlmRxLaserBiasHighWarningPortn_Type = EkiOnOff
_Rm10010arAlmRxLaserBiasHighWarningPortn_Object = MibTableColumn
rm10010arAlmRxLaserBiasHighWarningPortn = _Rm10010arAlmRxLaserBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 1, 120, 1, 16),
    _Rm10010arAlmRxLaserBiasHighWarningPortn_Type()
)
rm10010arAlmRxLaserBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmRxLaserBiasHighWarningPortn.setStatus("current")
_Rm10010arAlmRxLaserBiasHighAlarmPortn_Type = EkiOnOff
_Rm10010arAlmRxLaserBiasHighAlarmPortn_Object = MibTableColumn
rm10010arAlmRxLaserBiasHighAlarmPortn = _Rm10010arAlmRxLaserBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 1, 120, 1, 17),
    _Rm10010arAlmRxLaserBiasHighAlarmPortn_Type()
)
rm10010arAlmRxLaserBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmRxLaserBiasHighAlarmPortn.setStatus("current")
_Rm10010arAlmLineUrg_ObjectIdentity = ObjectIdentity
rm10010arAlmLineUrg = _Rm10010arAlmLineUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 2)
)
_Rm10010arAlmlineNetworkLaneFaultTable_Object = MibTable
rm10010arAlmlineNetworkLaneFaultTable = _Rm10010arAlmlineNetworkLaneFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 2, 136)
)
if mibBuilder.loadTexts:
    rm10010arAlmlineNetworkLaneFaultTable.setStatus("current")
_Rm10010arAlmlineNetworkLaneFaultEntry_Object = MibTableRow
rm10010arAlmlineNetworkLaneFaultEntry = _Rm10010arAlmlineNetworkLaneFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 2, 136, 1)
)
rm10010arAlmlineNetworkLaneFaultEntry.setIndexNames(
    (0, "EKINOPS-Rm10010ar-MIB", "rm10010arAlmlineNetworkLaneFaultIndex"),
)
if mibBuilder.loadTexts:
    rm10010arAlmlineNetworkLaneFaultEntry.setStatus("current")


class _Rm10010arAlmlineNetworkLaneFaultIndex_Type(Integer32):
    """Custom type rm10010arAlmlineNetworkLaneFaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010arAlmlineNetworkLaneFaultIndex_Type.__name__ = "Integer32"
_Rm10010arAlmlineNetworkLaneFaultIndex_Object = MibTableColumn
rm10010arAlmlineNetworkLaneFaultIndex = _Rm10010arAlmlineNetworkLaneFaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 2, 136, 1, 1),
    _Rm10010arAlmlineNetworkLaneFaultIndex_Type()
)
rm10010arAlmlineNetworkLaneFaultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmlineNetworkLaneFaultIndex.setStatus("current")
_Rm10010arAlmLineLaneRxTecFaultPortn_Type = EkiOnOff
_Rm10010arAlmLineLaneRxTecFaultPortn_Object = MibTableColumn
rm10010arAlmLineLaneRxTecFaultPortn = _Rm10010arAlmLineLaneRxTecFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 2, 136, 1, 3),
    _Rm10010arAlmLineLaneRxTecFaultPortn_Type()
)
rm10010arAlmLineLaneRxTecFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmLineLaneRxTecFaultPortn.setStatus("current")
_Rm10010arAlmLineLaneRxFifoErrorPortn_Type = EkiOnOff
_Rm10010arAlmLineLaneRxFifoErrorPortn_Object = MibTableColumn
rm10010arAlmLineLaneRxFifoErrorPortn = _Rm10010arAlmLineLaneRxFifoErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 2, 136, 1, 4),
    _Rm10010arAlmLineLaneRxFifoErrorPortn_Type()
)
rm10010arAlmLineLaneRxFifoErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmLineLaneRxFifoErrorPortn.setStatus("current")
_Rm10010arAlmLineLaneRxLolPortn_Type = EkiOnOff
_Rm10010arAlmLineLaneRxLolPortn_Object = MibTableColumn
rm10010arAlmLineLaneRxLolPortn = _Rm10010arAlmLineLaneRxLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 2, 136, 1, 5),
    _Rm10010arAlmLineLaneRxLolPortn_Type()
)
rm10010arAlmLineLaneRxLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmLineLaneRxLolPortn.setStatus("current")
_Rm10010arAlmLineLaneRxLosPortn_Type = EkiOnOff
_Rm10010arAlmLineLaneRxLosPortn_Object = MibTableColumn
rm10010arAlmLineLaneRxLosPortn = _Rm10010arAlmLineLaneRxLosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 2, 136, 1, 6),
    _Rm10010arAlmLineLaneRxLosPortn_Type()
)
rm10010arAlmLineLaneRxLosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmLineLaneRxLosPortn.setStatus("current")
_Rm10010arAlmLineLaneTxLolPortn_Type = EkiOnOff
_Rm10010arAlmLineLaneTxLolPortn_Object = MibTableColumn
rm10010arAlmLineLaneTxLolPortn = _Rm10010arAlmLineLaneTxLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 2, 136, 1, 8),
    _Rm10010arAlmLineLaneTxLolPortn_Type()
)
rm10010arAlmLineLaneTxLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmLineLaneTxLolPortn.setStatus("current")
_Rm10010arAlmLineLaneTxLosfPortn_Type = EkiOnOff
_Rm10010arAlmLineLaneTxLosfPortn_Object = MibTableColumn
rm10010arAlmLineLaneTxLosfPortn = _Rm10010arAlmLineLaneTxLosfPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 2, 136, 1, 9),
    _Rm10010arAlmLineLaneTxLosfPortn_Type()
)
rm10010arAlmLineLaneTxLosfPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmLineLaneTxLosfPortn.setStatus("current")
_Rm10010arAlmLineLaneApdPowerSupplyPortn_Type = EkiOnOff
_Rm10010arAlmLineLaneApdPowerSupplyPortn_Object = MibTableColumn
rm10010arAlmLineLaneApdPowerSupplyPortn = _Rm10010arAlmLineLaneApdPowerSupplyPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 2, 136, 1, 15),
    _Rm10010arAlmLineLaneApdPowerSupplyPortn_Type()
)
rm10010arAlmLineLaneApdPowerSupplyPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmLineLaneApdPowerSupplyPortn.setStatus("current")
_Rm10010arAlmLineLaneWavelengthUnlockedPortn_Type = EkiOnOff
_Rm10010arAlmLineLaneWavelengthUnlockedPortn_Object = MibTableColumn
rm10010arAlmLineLaneWavelengthUnlockedPortn = _Rm10010arAlmLineLaneWavelengthUnlockedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 2, 136, 1, 16),
    _Rm10010arAlmLineLaneWavelengthUnlockedPortn_Type()
)
rm10010arAlmLineLaneWavelengthUnlockedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmLineLaneWavelengthUnlockedPortn.setStatus("current")
_Rm10010arAlmLineLaneTecFaultPortn_Type = EkiOnOff
_Rm10010arAlmLineLaneTecFaultPortn_Object = MibTableColumn
rm10010arAlmLineLaneTecFaultPortn = _Rm10010arAlmLineLaneTecFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 2, 136, 1, 17),
    _Rm10010arAlmLineLaneTecFaultPortn_Type()
)
rm10010arAlmLineLaneTecFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmLineLaneTecFaultPortn.setStatus("current")
_Rm10010arAlmlineHostLaneFaultTable_Object = MibTable
rm10010arAlmlineHostLaneFaultTable = _Rm10010arAlmlineHostLaneFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 2, 152)
)
if mibBuilder.loadTexts:
    rm10010arAlmlineHostLaneFaultTable.setStatus("current")
_Rm10010arAlmlineHostLaneFaultEntry_Object = MibTableRow
rm10010arAlmlineHostLaneFaultEntry = _Rm10010arAlmlineHostLaneFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 2, 152, 1)
)
rm10010arAlmlineHostLaneFaultEntry.setIndexNames(
    (0, "EKINOPS-Rm10010ar-MIB", "rm10010arAlmlineHostLaneFaultIndex"),
)
if mibBuilder.loadTexts:
    rm10010arAlmlineHostLaneFaultEntry.setStatus("current")


class _Rm10010arAlmlineHostLaneFaultIndex_Type(Integer32):
    """Custom type rm10010arAlmlineHostLaneFaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010arAlmlineHostLaneFaultIndex_Type.__name__ = "Integer32"
_Rm10010arAlmlineHostLaneFaultIndex_Object = MibTableColumn
rm10010arAlmlineHostLaneFaultIndex = _Rm10010arAlmlineHostLaneFaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 2, 152, 1, 1),
    _Rm10010arAlmlineHostLaneFaultIndex_Type()
)
rm10010arAlmlineHostLaneFaultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmlineHostLaneFaultIndex.setStatus("current")
_Rm10010arAlmLineInputLossOfSignalPortn_Type = EkiOnOff
_Rm10010arAlmLineInputLossOfSignalPortn_Object = MibTableColumn
rm10010arAlmLineInputLossOfSignalPortn = _Rm10010arAlmLineInputLossOfSignalPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 2, 152, 1, 2),
    _Rm10010arAlmLineInputLossOfSignalPortn_Type()
)
rm10010arAlmLineInputLossOfSignalPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmLineInputLossOfSignalPortn.setStatus("current")
_Rm10010arAlmLineLossOfFramePortn_Type = EkiOnOff
_Rm10010arAlmLineLossOfFramePortn_Object = MibTableColumn
rm10010arAlmLineLossOfFramePortn = _Rm10010arAlmLineLossOfFramePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 2, 152, 1, 3),
    _Rm10010arAlmLineLossOfFramePortn_Type()
)
rm10010arAlmLineLossOfFramePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmLineLossOfFramePortn.setStatus("current")
_Rm10010arAlmLineSmBdiInsertedPortn_Type = EkiOnOff
_Rm10010arAlmLineSmBdiInsertedPortn_Object = MibTableColumn
rm10010arAlmLineSmBdiInsertedPortn = _Rm10010arAlmLineSmBdiInsertedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 2, 152, 1, 4),
    _Rm10010arAlmLineSmBdiInsertedPortn_Type()
)
rm10010arAlmLineSmBdiInsertedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmLineSmBdiInsertedPortn.setStatus("current")
_Rm10010arAlmLineSmBdiDetectedPortn_Type = EkiOnOff
_Rm10010arAlmLineSmBdiDetectedPortn_Object = MibTableColumn
rm10010arAlmLineSmBdiDetectedPortn = _Rm10010arAlmLineSmBdiDetectedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 2, 152, 1, 5),
    _Rm10010arAlmLineSmBdiDetectedPortn_Type()
)
rm10010arAlmLineSmBdiDetectedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmLineSmBdiDetectedPortn.setStatus("current")
_Rm10010arAlmLineSmIaeInsertedPortn_Type = EkiOnOff
_Rm10010arAlmLineSmIaeInsertedPortn_Object = MibTableColumn
rm10010arAlmLineSmIaeInsertedPortn = _Rm10010arAlmLineSmIaeInsertedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 2, 152, 1, 6),
    _Rm10010arAlmLineSmIaeInsertedPortn_Type()
)
rm10010arAlmLineSmIaeInsertedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmLineSmIaeInsertedPortn.setStatus("current")
_Rm10010arAlmLineSmIaeDetectedPortn_Type = EkiOnOff
_Rm10010arAlmLineSmIaeDetectedPortn_Object = MibTableColumn
rm10010arAlmLineSmIaeDetectedPortn = _Rm10010arAlmLineSmIaeDetectedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 2, 152, 1, 7),
    _Rm10010arAlmLineSmIaeDetectedPortn_Type()
)
rm10010arAlmLineSmIaeDetectedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmLineSmIaeDetectedPortn.setStatus("current")
_Rm10010arAlmLineTxHostLolPortn_Type = EkiOnOff
_Rm10010arAlmLineTxHostLolPortn_Object = MibTableColumn
rm10010arAlmLineTxHostLolPortn = _Rm10010arAlmLineTxHostLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 2, 152, 1, 10),
    _Rm10010arAlmLineTxHostLolPortn_Type()
)
rm10010arAlmLineTxHostLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmLineTxHostLolPortn.setStatus("current")
_Rm10010arAlmLineLaneTxFifoErrorPortn_Type = EkiOnOff
_Rm10010arAlmLineLaneTxFifoErrorPortn_Object = MibTableColumn
rm10010arAlmLineLaneTxFifoErrorPortn = _Rm10010arAlmLineLaneTxFifoErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 2, 152, 1, 11),
    _Rm10010arAlmLineLaneTxFifoErrorPortn_Type()
)
rm10010arAlmLineLaneTxFifoErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmLineLaneTxFifoErrorPortn.setStatus("current")
_Rm10010arAlmlineNetworkLaneRxOtnTable_Object = MibTable
rm10010arAlmlineNetworkLaneRxOtnTable = _Rm10010arAlmlineNetworkLaneRxOtnTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 2, 168)
)
if mibBuilder.loadTexts:
    rm10010arAlmlineNetworkLaneRxOtnTable.setStatus("current")
_Rm10010arAlmlineNetworkLaneRxOtnEntry_Object = MibTableRow
rm10010arAlmlineNetworkLaneRxOtnEntry = _Rm10010arAlmlineNetworkLaneRxOtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 2, 168, 1)
)
rm10010arAlmlineNetworkLaneRxOtnEntry.setIndexNames(
    (0, "EKINOPS-Rm10010ar-MIB", "rm10010arAlmlineNetworkLaneRxOtnIndex"),
)
if mibBuilder.loadTexts:
    rm10010arAlmlineNetworkLaneRxOtnEntry.setStatus("current")


class _Rm10010arAlmlineNetworkLaneRxOtnIndex_Type(Integer32):
    """Custom type rm10010arAlmlineNetworkLaneRxOtnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010arAlmlineNetworkLaneRxOtnIndex_Type.__name__ = "Integer32"
_Rm10010arAlmlineNetworkLaneRxOtnIndex_Object = MibTableColumn
rm10010arAlmlineNetworkLaneRxOtnIndex = _Rm10010arAlmlineNetworkLaneRxOtnIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 2, 168, 1, 1),
    _Rm10010arAlmlineNetworkLaneRxOtnIndex_Type()
)
rm10010arAlmlineNetworkLaneRxOtnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmlineNetworkLaneRxOtnIndex.setStatus("current")
_Rm10010arAlmLineRxOtnOduAisPortn_Type = EkiOnOff
_Rm10010arAlmLineRxOtnOduAisPortn_Object = MibTableColumn
rm10010arAlmLineRxOtnOduAisPortn = _Rm10010arAlmLineRxOtnOduAisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 2, 168, 1, 10),
    _Rm10010arAlmLineRxOtnOduAisPortn_Type()
)
rm10010arAlmLineRxOtnOduAisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmLineRxOtnOduAisPortn.setStatus("current")
_Rm10010arAlmLineRxOtnOtuAisPortn_Type = EkiOnOff
_Rm10010arAlmLineRxOtnOtuAisPortn_Object = MibTableColumn
rm10010arAlmLineRxOtnOtuAisPortn = _Rm10010arAlmLineRxOtnOtuAisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 2, 168, 1, 11),
    _Rm10010arAlmLineRxOtnOtuAisPortn_Type()
)
rm10010arAlmLineRxOtnOtuAisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmLineRxOtnOtuAisPortn.setStatus("current")
_Rm10010arAlmLineRxSmBdiPortn_Type = EkiOnOff
_Rm10010arAlmLineRxSmBdiPortn_Object = MibTableColumn
rm10010arAlmLineRxSmBdiPortn = _Rm10010arAlmLineRxSmBdiPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 2, 168, 1, 12),
    _Rm10010arAlmLineRxSmBdiPortn_Type()
)
rm10010arAlmLineRxSmBdiPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmLineRxSmBdiPortn.setStatus("current")
_Rm10010arAlmLineRxOtnIaePortn_Type = EkiOnOff
_Rm10010arAlmLineRxOtnIaePortn_Object = MibTableColumn
rm10010arAlmLineRxOtnIaePortn = _Rm10010arAlmLineRxOtnIaePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 2, 168, 1, 13),
    _Rm10010arAlmLineRxOtnIaePortn_Type()
)
rm10010arAlmLineRxOtnIaePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmLineRxOtnIaePortn.setStatus("current")
_Rm10010arAlmLineRxOtnOomPortn_Type = EkiOnOff
_Rm10010arAlmLineRxOtnOomPortn_Object = MibTableColumn
rm10010arAlmLineRxOtnOomPortn = _Rm10010arAlmLineRxOtnOomPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 2, 168, 1, 14),
    _Rm10010arAlmLineRxOtnOomPortn_Type()
)
rm10010arAlmLineRxOtnOomPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmLineRxOtnOomPortn.setStatus("current")
_Rm10010arAlmLineRxOtnLomPortn_Type = EkiOnOff
_Rm10010arAlmLineRxOtnLomPortn_Object = MibTableColumn
rm10010arAlmLineRxOtnLomPortn = _Rm10010arAlmLineRxOtnLomPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 2, 168, 1, 15),
    _Rm10010arAlmLineRxOtnLomPortn_Type()
)
rm10010arAlmLineRxOtnLomPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmLineRxOtnLomPortn.setStatus("current")
_Rm10010arAlmLineRxOtnOofPortn_Type = EkiOnOff
_Rm10010arAlmLineRxOtnOofPortn_Object = MibTableColumn
rm10010arAlmLineRxOtnOofPortn = _Rm10010arAlmLineRxOtnOofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 2, 168, 1, 16),
    _Rm10010arAlmLineRxOtnOofPortn_Type()
)
rm10010arAlmLineRxOtnOofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmLineRxOtnOofPortn.setStatus("current")
_Rm10010arAlmLineRxOtnLofPortn_Type = EkiOnOff
_Rm10010arAlmLineRxOtnLofPortn_Object = MibTableColumn
rm10010arAlmLineRxOtnLofPortn = _Rm10010arAlmLineRxOtnLofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 2, 168, 1, 17),
    _Rm10010arAlmLineRxOtnLofPortn_Type()
)
rm10010arAlmLineRxOtnLofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmLineRxOtnLofPortn.setStatus("current")
_Rm10010arAlmlineHostLaneTxOtnTable_Object = MibTable
rm10010arAlmlineHostLaneTxOtnTable = _Rm10010arAlmlineHostLaneTxOtnTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 2, 184)
)
if mibBuilder.loadTexts:
    rm10010arAlmlineHostLaneTxOtnTable.setStatus("current")
_Rm10010arAlmlineHostLaneTxOtnEntry_Object = MibTableRow
rm10010arAlmlineHostLaneTxOtnEntry = _Rm10010arAlmlineHostLaneTxOtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 2, 184, 1)
)
rm10010arAlmlineHostLaneTxOtnEntry.setIndexNames(
    (0, "EKINOPS-Rm10010ar-MIB", "rm10010arAlmlineHostLaneTxOtnIndex"),
)
if mibBuilder.loadTexts:
    rm10010arAlmlineHostLaneTxOtnEntry.setStatus("current")


class _Rm10010arAlmlineHostLaneTxOtnIndex_Type(Integer32):
    """Custom type rm10010arAlmlineHostLaneTxOtnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010arAlmlineHostLaneTxOtnIndex_Type.__name__ = "Integer32"
_Rm10010arAlmlineHostLaneTxOtnIndex_Object = MibTableColumn
rm10010arAlmlineHostLaneTxOtnIndex = _Rm10010arAlmlineHostLaneTxOtnIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 2, 184, 1, 1),
    _Rm10010arAlmlineHostLaneTxOtnIndex_Type()
)
rm10010arAlmlineHostLaneTxOtnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmlineHostLaneTxOtnIndex.setStatus("current")
_Rm10010arAlmLineTxOtnOduAisPortn_Type = EkiOnOff
_Rm10010arAlmLineTxOtnOduAisPortn_Object = MibTableColumn
rm10010arAlmLineTxOtnOduAisPortn = _Rm10010arAlmLineTxOtnOduAisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 2, 184, 1, 10),
    _Rm10010arAlmLineTxOtnOduAisPortn_Type()
)
rm10010arAlmLineTxOtnOduAisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmLineTxOtnOduAisPortn.setStatus("current")
_Rm10010arAlmLineTxOtnOtuAisPortn_Type = EkiOnOff
_Rm10010arAlmLineTxOtnOtuAisPortn_Object = MibTableColumn
rm10010arAlmLineTxOtnOtuAisPortn = _Rm10010arAlmLineTxOtnOtuAisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 2, 184, 1, 11),
    _Rm10010arAlmLineTxOtnOtuAisPortn_Type()
)
rm10010arAlmLineTxOtnOtuAisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmLineTxOtnOtuAisPortn.setStatus("current")
_Rm10010arAlmLineTxSmBdiPortn_Type = EkiOnOff
_Rm10010arAlmLineTxSmBdiPortn_Object = MibTableColumn
rm10010arAlmLineTxSmBdiPortn = _Rm10010arAlmLineTxSmBdiPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 2, 184, 1, 12),
    _Rm10010arAlmLineTxSmBdiPortn_Type()
)
rm10010arAlmLineTxSmBdiPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmLineTxSmBdiPortn.setStatus("current")
_Rm10010arAlmLineTxOtnIaePortn_Type = EkiOnOff
_Rm10010arAlmLineTxOtnIaePortn_Object = MibTableColumn
rm10010arAlmLineTxOtnIaePortn = _Rm10010arAlmLineTxOtnIaePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 2, 184, 1, 13),
    _Rm10010arAlmLineTxOtnIaePortn_Type()
)
rm10010arAlmLineTxOtnIaePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmLineTxOtnIaePortn.setStatus("current")
_Rm10010arAlmLineTxOtnOomPortn_Type = EkiOnOff
_Rm10010arAlmLineTxOtnOomPortn_Object = MibTableColumn
rm10010arAlmLineTxOtnOomPortn = _Rm10010arAlmLineTxOtnOomPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 2, 184, 1, 14),
    _Rm10010arAlmLineTxOtnOomPortn_Type()
)
rm10010arAlmLineTxOtnOomPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmLineTxOtnOomPortn.setStatus("current")
_Rm10010arAlmLineTxOtnLomPortn_Type = EkiOnOff
_Rm10010arAlmLineTxOtnLomPortn_Object = MibTableColumn
rm10010arAlmLineTxOtnLomPortn = _Rm10010arAlmLineTxOtnLomPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 2, 184, 1, 15),
    _Rm10010arAlmLineTxOtnLomPortn_Type()
)
rm10010arAlmLineTxOtnLomPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmLineTxOtnLomPortn.setStatus("current")
_Rm10010arAlmLineTxOtnOofPortn_Type = EkiOnOff
_Rm10010arAlmLineTxOtnOofPortn_Object = MibTableColumn
rm10010arAlmLineTxOtnOofPortn = _Rm10010arAlmLineTxOtnOofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 2, 184, 1, 16),
    _Rm10010arAlmLineTxOtnOofPortn_Type()
)
rm10010arAlmLineTxOtnOofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmLineTxOtnOofPortn.setStatus("current")
_Rm10010arAlmLineTxOtnLofPortn_Type = EkiOnOff
_Rm10010arAlmLineTxOtnLofPortn_Object = MibTableColumn
rm10010arAlmLineTxOtnLofPortn = _Rm10010arAlmLineTxOtnLofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 2, 184, 1, 17),
    _Rm10010arAlmLineTxOtnLofPortn_Type()
)
rm10010arAlmLineTxOtnLofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmLineTxOtnLofPortn.setStatus("current")
_Rm10010arAlmLineCrit_ObjectIdentity = ObjectIdentity
rm10010arAlmLineCrit = _Rm10010arAlmLineCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 3)
)
_Rm10010arAlmsynthAlmLineTable_Object = MibTable
rm10010arAlmsynthAlmLineTable = _Rm10010arAlmsynthAlmLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 3, 24)
)
if mibBuilder.loadTexts:
    rm10010arAlmsynthAlmLineTable.setStatus("current")
_Rm10010arAlmsynthAlmLineEntry_Object = MibTableRow
rm10010arAlmsynthAlmLineEntry = _Rm10010arAlmsynthAlmLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 3, 24, 1)
)
rm10010arAlmsynthAlmLineEntry.setIndexNames(
    (0, "EKINOPS-Rm10010ar-MIB", "rm10010arAlmsynthAlmLineIndex"),
)
if mibBuilder.loadTexts:
    rm10010arAlmsynthAlmLineEntry.setStatus("current")


class _Rm10010arAlmsynthAlmLineIndex_Type(Integer32):
    """Custom type rm10010arAlmsynthAlmLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010arAlmsynthAlmLineIndex_Type.__name__ = "Integer32"
_Rm10010arAlmsynthAlmLineIndex_Object = MibTableColumn
rm10010arAlmsynthAlmLineIndex = _Rm10010arAlmsynthAlmLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 3, 24, 1, 1),
    _Rm10010arAlmsynthAlmLineIndex_Type()
)
rm10010arAlmsynthAlmLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmsynthAlmLineIndex.setStatus("current")
_Rm10010arAlmXfpAbsentPortn_Type = EkiOnOff
_Rm10010arAlmXfpAbsentPortn_Object = MibTableColumn
rm10010arAlmXfpAbsentPortn = _Rm10010arAlmXfpAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 3, 24, 1, 2),
    _Rm10010arAlmXfpAbsentPortn_Type()
)
rm10010arAlmXfpAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmXfpAbsentPortn.setStatus("current")
_Rm10010arAlmXfpInitNotComplPortn_Type = EkiOnOff
_Rm10010arAlmXfpInitNotComplPortn_Object = MibTableColumn
rm10010arAlmXfpInitNotComplPortn = _Rm10010arAlmXfpInitNotComplPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 3, 24, 1, 3),
    _Rm10010arAlmXfpInitNotComplPortn_Type()
)
rm10010arAlmXfpInitNotComplPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmXfpInitNotComplPortn.setStatus("current")
_Rm10010arAlmLineHwFailPortn_Type = EkiOnOff
_Rm10010arAlmLineHwFailPortn_Object = MibTableColumn
rm10010arAlmLineHwFailPortn = _Rm10010arAlmLineHwFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 3, 24, 1, 5),
    _Rm10010arAlmLineHwFailPortn_Type()
)
rm10010arAlmLineHwFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmLineHwFailPortn.setStatus("current")
_Rm10010arAlmXfpTxOffPortn_Type = EkiOnOff
_Rm10010arAlmXfpTxOffPortn_Object = MibTableColumn
rm10010arAlmXfpTxOffPortn = _Rm10010arAlmXfpTxOffPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 3, 24, 1, 6),
    _Rm10010arAlmXfpTxOffPortn_Type()
)
rm10010arAlmXfpTxOffPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmXfpTxOffPortn.setStatus("current")
_Rm10010arAlmLineLocalOosPortn_Type = EkiOnOff
_Rm10010arAlmLineLocalOosPortn_Object = MibTableColumn
rm10010arAlmLineLocalOosPortn = _Rm10010arAlmLineLocalOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 3, 24, 1, 7),
    _Rm10010arAlmLineLocalOosPortn_Type()
)
rm10010arAlmLineLocalOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmLineLocalOosPortn.setStatus("current")
_Rm10010arAlmUpRdiInsPortn_Type = EkiOnOff
_Rm10010arAlmUpRdiInsPortn_Object = MibTableColumn
rm10010arAlmUpRdiInsPortn = _Rm10010arAlmUpRdiInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 3, 24, 1, 9),
    _Rm10010arAlmUpRdiInsPortn_Type()
)
rm10010arAlmUpRdiInsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmUpRdiInsPortn.setStatus("current")
_Rm10010arAlmLineDdmWarningPortn_Type = EkiOnOff
_Rm10010arAlmLineDdmWarningPortn_Object = MibTableColumn
rm10010arAlmLineDdmWarningPortn = _Rm10010arAlmLineDdmWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 3, 24, 1, 10),
    _Rm10010arAlmLineDdmWarningPortn_Type()
)
rm10010arAlmLineDdmWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmLineDdmWarningPortn.setStatus("current")
_Rm10010arAlmLineDdmAlmPortn_Type = EkiOnOff
_Rm10010arAlmLineDdmAlmPortn_Object = MibTableColumn
rm10010arAlmLineDdmAlmPortn = _Rm10010arAlmLineDdmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 3, 24, 1, 11),
    _Rm10010arAlmLineDdmAlmPortn_Type()
)
rm10010arAlmLineDdmAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmLineDdmAlmPortn.setStatus("current")
_Rm10010arAlmLineFailPortn_Type = EkiOnOff
_Rm10010arAlmLineFailPortn_Object = MibTableColumn
rm10010arAlmLineFailPortn = _Rm10010arAlmLineFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 3, 24, 1, 13),
    _Rm10010arAlmLineFailPortn_Type()
)
rm10010arAlmLineFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmLineFailPortn.setStatus("current")
_Rm10010arAlmLineActivePortn_Type = EkiOnOff
_Rm10010arAlmLineActivePortn_Object = MibTableColumn
rm10010arAlmLineActivePortn = _Rm10010arAlmLineActivePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 2, 3, 3, 24, 1, 17),
    _Rm10010arAlmLineActivePortn_Type()
)
rm10010arAlmLineActivePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arAlmLineActivePortn.setStatus("current")
_Rm10010armeasures_ObjectIdentity = ObjectIdentity
rm10010armeasures = _Rm10010armeasures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3)
)
_Rm10010arMesrOther_ObjectIdentity = ObjectIdentity
rm10010arMesrOther = _Rm10010arMesrOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 1)
)
_Rm10010arMesrsynth0_Type = EkiMeasureType
_Rm10010arMesrsynth0_Object = MibScalar
rm10010arMesrsynth0 = _Rm10010arMesrsynth0_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 1, 0),
    _Rm10010arMesrsynth0_Type()
)
rm10010arMesrsynth0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrsynth0.setStatus("deprecated")
_Rm10010arMesrsynth1_Type = EkiMeasureType
_Rm10010arMesrsynth1_Object = MibScalar
rm10010arMesrsynth1 = _Rm10010arMesrsynth1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 1, 1),
    _Rm10010arMesrsynth1_Type()
)
rm10010arMesrsynth1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrsynth1.setStatus("deprecated")


class _Rm10010arMesrpmIntervalNumber_Type(Unsigned32):
    """Custom type rm10010arMesrpmIntervalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010arMesrpmIntervalNumber_Type.__name__ = "Unsigned32"
_Rm10010arMesrpmIntervalNumber_Object = MibScalar
rm10010arMesrpmIntervalNumber = _Rm10010arMesrpmIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 1, 7),
    _Rm10010arMesrpmIntervalNumber_Type()
)
rm10010arMesrpmIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrpmIntervalNumber.setStatus("current")


class _Rm10010arMesrlineNetTxLaserOutputPwrAverage_Type(Unsigned32):
    """Custom type rm10010arMesrlineNetTxLaserOutputPwrAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010arMesrlineNetTxLaserOutputPwrAverage_Type.__name__ = "Unsigned32"
_Rm10010arMesrlineNetTxLaserOutputPwrAverage_Object = MibScalar
rm10010arMesrlineNetTxLaserOutputPwrAverage = _Rm10010arMesrlineNetTxLaserOutputPwrAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 1, 180),
    _Rm10010arMesrlineNetTxLaserOutputPwrAverage_Type()
)
rm10010arMesrlineNetTxLaserOutputPwrAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrlineNetTxLaserOutputPwrAverage.setStatus("current")


class _Rm10010arMesrlineNetTxLaserTempAverage_Type(Unsigned32):
    """Custom type rm10010arMesrlineNetTxLaserTempAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010arMesrlineNetTxLaserTempAverage_Type.__name__ = "Unsigned32"
_Rm10010arMesrlineNetTxLaserTempAverage_Object = MibScalar
rm10010arMesrlineNetTxLaserTempAverage = _Rm10010arMesrlineNetTxLaserTempAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 1, 181),
    _Rm10010arMesrlineNetTxLaserTempAverage_Type()
)
rm10010arMesrlineNetTxLaserTempAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrlineNetTxLaserTempAverage.setStatus("current")


class _Rm10010arMesrlineNetTxBiasCurrentAverage_Type(Unsigned32):
    """Custom type rm10010arMesrlineNetTxBiasCurrentAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010arMesrlineNetTxBiasCurrentAverage_Type.__name__ = "Unsigned32"
_Rm10010arMesrlineNetTxBiasCurrentAverage_Object = MibScalar
rm10010arMesrlineNetTxBiasCurrentAverage = _Rm10010arMesrlineNetTxBiasCurrentAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 1, 182),
    _Rm10010arMesrlineNetTxBiasCurrentAverage_Type()
)
rm10010arMesrlineNetTxBiasCurrentAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrlineNetTxBiasCurrentAverage.setStatus("current")


class _Rm10010arMesrlineNetRxInputPwrAverage_Type(Unsigned32):
    """Custom type rm10010arMesrlineNetRxInputPwrAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010arMesrlineNetRxInputPwrAverage_Type.__name__ = "Unsigned32"
_Rm10010arMesrlineNetRxInputPwrAverage_Object = MibScalar
rm10010arMesrlineNetRxInputPwrAverage = _Rm10010arMesrlineNetRxInputPwrAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 1, 183),
    _Rm10010arMesrlineNetRxInputPwrAverage_Type()
)
rm10010arMesrlineNetRxInputPwrAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrlineNetRxInputPwrAverage.setStatus("current")


class _Rm10010arMesrlineResidualChromaticDispAverage_Type(Unsigned32):
    """Custom type rm10010arMesrlineResidualChromaticDispAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010arMesrlineResidualChromaticDispAverage_Type.__name__ = "Unsigned32"
_Rm10010arMesrlineResidualChromaticDispAverage_Object = MibScalar
rm10010arMesrlineResidualChromaticDispAverage = _Rm10010arMesrlineResidualChromaticDispAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 1, 184),
    _Rm10010arMesrlineResidualChromaticDispAverage_Type()
)
rm10010arMesrlineResidualChromaticDispAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrlineResidualChromaticDispAverage.setStatus("current")


class _Rm10010arMesrlineDiffGroupDelayAverage_Type(Unsigned32):
    """Custom type rm10010arMesrlineDiffGroupDelayAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010arMesrlineDiffGroupDelayAverage_Type.__name__ = "Unsigned32"
_Rm10010arMesrlineDiffGroupDelayAverage_Object = MibScalar
rm10010arMesrlineDiffGroupDelayAverage = _Rm10010arMesrlineDiffGroupDelayAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 1, 185),
    _Rm10010arMesrlineDiffGroupDelayAverage_Type()
)
rm10010arMesrlineDiffGroupDelayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrlineDiffGroupDelayAverage.setStatus("current")


class _Rm10010arMesrlineQFactorAverage_Type(Unsigned32):
    """Custom type rm10010arMesrlineQFactorAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010arMesrlineQFactorAverage_Type.__name__ = "Unsigned32"
_Rm10010arMesrlineQFactorAverage_Object = MibScalar
rm10010arMesrlineQFactorAverage = _Rm10010arMesrlineQFactorAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 1, 186),
    _Rm10010arMesrlineQFactorAverage_Type()
)
rm10010arMesrlineQFactorAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrlineQFactorAverage.setStatus("current")


class _Rm10010arMesrlineCarrierFreqOffsetAverage_Type(Unsigned32):
    """Custom type rm10010arMesrlineCarrierFreqOffsetAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010arMesrlineCarrierFreqOffsetAverage_Type.__name__ = "Unsigned32"
_Rm10010arMesrlineCarrierFreqOffsetAverage_Object = MibScalar
rm10010arMesrlineCarrierFreqOffsetAverage = _Rm10010arMesrlineCarrierFreqOffsetAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 1, 187),
    _Rm10010arMesrlineCarrierFreqOffsetAverage_Type()
)
rm10010arMesrlineCarrierFreqOffsetAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrlineCarrierFreqOffsetAverage.setStatus("current")


class _Rm10010arMesrlineOsnrAverage_Type(Unsigned32):
    """Custom type rm10010arMesrlineOsnrAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010arMesrlineOsnrAverage_Type.__name__ = "Unsigned32"
_Rm10010arMesrlineOsnrAverage_Object = MibScalar
rm10010arMesrlineOsnrAverage = _Rm10010arMesrlineOsnrAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 1, 188),
    _Rm10010arMesrlineOsnrAverage_Type()
)
rm10010arMesrlineOsnrAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrlineOsnrAverage.setStatus("current")


class _Rm10010arMesrclientNetTxTempMin_Type(Unsigned32):
    """Custom type rm10010arMesrclientNetTxTempMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010arMesrclientNetTxTempMin_Type.__name__ = "Unsigned32"
_Rm10010arMesrclientNetTxTempMin_Object = MibScalar
rm10010arMesrclientNetTxTempMin = _Rm10010arMesrclientNetTxTempMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 1, 192),
    _Rm10010arMesrclientNetTxTempMin_Type()
)
rm10010arMesrclientNetTxTempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrclientNetTxTempMin.setStatus("current")


class _Rm10010arMesrclientNetTxBiasMin_Type(Unsigned32):
    """Custom type rm10010arMesrclientNetTxBiasMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010arMesrclientNetTxBiasMin_Type.__name__ = "Unsigned32"
_Rm10010arMesrclientNetTxBiasMin_Object = MibScalar
rm10010arMesrclientNetTxBiasMin = _Rm10010arMesrclientNetTxBiasMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 1, 193),
    _Rm10010arMesrclientNetTxBiasMin_Type()
)
rm10010arMesrclientNetTxBiasMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrclientNetTxBiasMin.setStatus("current")


class _Rm10010arMesrclientNetTxPwrMin_Type(Unsigned32):
    """Custom type rm10010arMesrclientNetTxPwrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010arMesrclientNetTxPwrMin_Type.__name__ = "Unsigned32"
_Rm10010arMesrclientNetTxPwrMin_Object = MibScalar
rm10010arMesrclientNetTxPwrMin = _Rm10010arMesrclientNetTxPwrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 1, 194),
    _Rm10010arMesrclientNetTxPwrMin_Type()
)
rm10010arMesrclientNetTxPwrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrclientNetTxPwrMin.setStatus("current")


class _Rm10010arMesrclientNetRxPwrMin_Type(Unsigned32):
    """Custom type rm10010arMesrclientNetRxPwrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010arMesrclientNetRxPwrMin_Type.__name__ = "Unsigned32"
_Rm10010arMesrclientNetRxPwrMin_Object = MibScalar
rm10010arMesrclientNetRxPwrMin = _Rm10010arMesrclientNetRxPwrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 1, 195),
    _Rm10010arMesrclientNetRxPwrMin_Type()
)
rm10010arMesrclientNetRxPwrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrclientNetRxPwrMin.setStatus("current")


class _Rm10010arMesrlineNetTxLaserOutputPwrMin_Type(Unsigned32):
    """Custom type rm10010arMesrlineNetTxLaserOutputPwrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010arMesrlineNetTxLaserOutputPwrMin_Type.__name__ = "Unsigned32"
_Rm10010arMesrlineNetTxLaserOutputPwrMin_Object = MibScalar
rm10010arMesrlineNetTxLaserOutputPwrMin = _Rm10010arMesrlineNetTxLaserOutputPwrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 1, 196),
    _Rm10010arMesrlineNetTxLaserOutputPwrMin_Type()
)
rm10010arMesrlineNetTxLaserOutputPwrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrlineNetTxLaserOutputPwrMin.setStatus("current")


class _Rm10010arMesrlineNetTxLaserTempMin_Type(Unsigned32):
    """Custom type rm10010arMesrlineNetTxLaserTempMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010arMesrlineNetTxLaserTempMin_Type.__name__ = "Unsigned32"
_Rm10010arMesrlineNetTxLaserTempMin_Object = MibScalar
rm10010arMesrlineNetTxLaserTempMin = _Rm10010arMesrlineNetTxLaserTempMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 1, 197),
    _Rm10010arMesrlineNetTxLaserTempMin_Type()
)
rm10010arMesrlineNetTxLaserTempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrlineNetTxLaserTempMin.setStatus("current")


class _Rm10010arMesrlineNetTxBiasCurrentMin_Type(Unsigned32):
    """Custom type rm10010arMesrlineNetTxBiasCurrentMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010arMesrlineNetTxBiasCurrentMin_Type.__name__ = "Unsigned32"
_Rm10010arMesrlineNetTxBiasCurrentMin_Object = MibScalar
rm10010arMesrlineNetTxBiasCurrentMin = _Rm10010arMesrlineNetTxBiasCurrentMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 1, 198),
    _Rm10010arMesrlineNetTxBiasCurrentMin_Type()
)
rm10010arMesrlineNetTxBiasCurrentMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrlineNetTxBiasCurrentMin.setStatus("current")


class _Rm10010arMesrlineNetRxInputPwrMin_Type(Unsigned32):
    """Custom type rm10010arMesrlineNetRxInputPwrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010arMesrlineNetRxInputPwrMin_Type.__name__ = "Unsigned32"
_Rm10010arMesrlineNetRxInputPwrMin_Object = MibScalar
rm10010arMesrlineNetRxInputPwrMin = _Rm10010arMesrlineNetRxInputPwrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 1, 199),
    _Rm10010arMesrlineNetRxInputPwrMin_Type()
)
rm10010arMesrlineNetRxInputPwrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrlineNetRxInputPwrMin.setStatus("current")


class _Rm10010arMesrlineResidualChromaticDispMin_Type(Unsigned32):
    """Custom type rm10010arMesrlineResidualChromaticDispMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010arMesrlineResidualChromaticDispMin_Type.__name__ = "Unsigned32"
_Rm10010arMesrlineResidualChromaticDispMin_Object = MibScalar
rm10010arMesrlineResidualChromaticDispMin = _Rm10010arMesrlineResidualChromaticDispMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 1, 200),
    _Rm10010arMesrlineResidualChromaticDispMin_Type()
)
rm10010arMesrlineResidualChromaticDispMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrlineResidualChromaticDispMin.setStatus("current")


class _Rm10010arMesrlineDiffGroupDelayMin_Type(Unsigned32):
    """Custom type rm10010arMesrlineDiffGroupDelayMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010arMesrlineDiffGroupDelayMin_Type.__name__ = "Unsigned32"
_Rm10010arMesrlineDiffGroupDelayMin_Object = MibScalar
rm10010arMesrlineDiffGroupDelayMin = _Rm10010arMesrlineDiffGroupDelayMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 1, 201),
    _Rm10010arMesrlineDiffGroupDelayMin_Type()
)
rm10010arMesrlineDiffGroupDelayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrlineDiffGroupDelayMin.setStatus("current")


class _Rm10010arMesrlineQFactorMin_Type(Unsigned32):
    """Custom type rm10010arMesrlineQFactorMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010arMesrlineQFactorMin_Type.__name__ = "Unsigned32"
_Rm10010arMesrlineQFactorMin_Object = MibScalar
rm10010arMesrlineQFactorMin = _Rm10010arMesrlineQFactorMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 1, 202),
    _Rm10010arMesrlineQFactorMin_Type()
)
rm10010arMesrlineQFactorMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrlineQFactorMin.setStatus("current")


class _Rm10010arMesrlineCarrierFreqOffsetMin_Type(Unsigned32):
    """Custom type rm10010arMesrlineCarrierFreqOffsetMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010arMesrlineCarrierFreqOffsetMin_Type.__name__ = "Unsigned32"
_Rm10010arMesrlineCarrierFreqOffsetMin_Object = MibScalar
rm10010arMesrlineCarrierFreqOffsetMin = _Rm10010arMesrlineCarrierFreqOffsetMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 1, 203),
    _Rm10010arMesrlineCarrierFreqOffsetMin_Type()
)
rm10010arMesrlineCarrierFreqOffsetMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrlineCarrierFreqOffsetMin.setStatus("current")


class _Rm10010arMesrlineOsnrMin_Type(Unsigned32):
    """Custom type rm10010arMesrlineOsnrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010arMesrlineOsnrMin_Type.__name__ = "Unsigned32"
_Rm10010arMesrlineOsnrMin_Object = MibScalar
rm10010arMesrlineOsnrMin = _Rm10010arMesrlineOsnrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 1, 204),
    _Rm10010arMesrlineOsnrMin_Type()
)
rm10010arMesrlineOsnrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrlineOsnrMin.setStatus("current")


class _Rm10010arMesrclientNetTxTempMax_Type(Unsigned32):
    """Custom type rm10010arMesrclientNetTxTempMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010arMesrclientNetTxTempMax_Type.__name__ = "Unsigned32"
_Rm10010arMesrclientNetTxTempMax_Object = MibScalar
rm10010arMesrclientNetTxTempMax = _Rm10010arMesrclientNetTxTempMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 1, 208),
    _Rm10010arMesrclientNetTxTempMax_Type()
)
rm10010arMesrclientNetTxTempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrclientNetTxTempMax.setStatus("current")


class _Rm10010arMesrclientNetTxBiasMax_Type(Unsigned32):
    """Custom type rm10010arMesrclientNetTxBiasMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010arMesrclientNetTxBiasMax_Type.__name__ = "Unsigned32"
_Rm10010arMesrclientNetTxBiasMax_Object = MibScalar
rm10010arMesrclientNetTxBiasMax = _Rm10010arMesrclientNetTxBiasMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 1, 209),
    _Rm10010arMesrclientNetTxBiasMax_Type()
)
rm10010arMesrclientNetTxBiasMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrclientNetTxBiasMax.setStatus("current")


class _Rm10010arMesrclientNetTxPwrMax_Type(Unsigned32):
    """Custom type rm10010arMesrclientNetTxPwrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010arMesrclientNetTxPwrMax_Type.__name__ = "Unsigned32"
_Rm10010arMesrclientNetTxPwrMax_Object = MibScalar
rm10010arMesrclientNetTxPwrMax = _Rm10010arMesrclientNetTxPwrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 1, 210),
    _Rm10010arMesrclientNetTxPwrMax_Type()
)
rm10010arMesrclientNetTxPwrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrclientNetTxPwrMax.setStatus("current")


class _Rm10010arMesrclientNetRxPwrMax_Type(Unsigned32):
    """Custom type rm10010arMesrclientNetRxPwrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010arMesrclientNetRxPwrMax_Type.__name__ = "Unsigned32"
_Rm10010arMesrclientNetRxPwrMax_Object = MibScalar
rm10010arMesrclientNetRxPwrMax = _Rm10010arMesrclientNetRxPwrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 1, 211),
    _Rm10010arMesrclientNetRxPwrMax_Type()
)
rm10010arMesrclientNetRxPwrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrclientNetRxPwrMax.setStatus("current")


class _Rm10010arMesrlineNetTxLaserOutputPwrMax_Type(Unsigned32):
    """Custom type rm10010arMesrlineNetTxLaserOutputPwrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010arMesrlineNetTxLaserOutputPwrMax_Type.__name__ = "Unsigned32"
_Rm10010arMesrlineNetTxLaserOutputPwrMax_Object = MibScalar
rm10010arMesrlineNetTxLaserOutputPwrMax = _Rm10010arMesrlineNetTxLaserOutputPwrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 1, 212),
    _Rm10010arMesrlineNetTxLaserOutputPwrMax_Type()
)
rm10010arMesrlineNetTxLaserOutputPwrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrlineNetTxLaserOutputPwrMax.setStatus("current")


class _Rm10010arMesrlineNetTxLaserTempMax_Type(Unsigned32):
    """Custom type rm10010arMesrlineNetTxLaserTempMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010arMesrlineNetTxLaserTempMax_Type.__name__ = "Unsigned32"
_Rm10010arMesrlineNetTxLaserTempMax_Object = MibScalar
rm10010arMesrlineNetTxLaserTempMax = _Rm10010arMesrlineNetTxLaserTempMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 1, 213),
    _Rm10010arMesrlineNetTxLaserTempMax_Type()
)
rm10010arMesrlineNetTxLaserTempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrlineNetTxLaserTempMax.setStatus("current")


class _Rm10010arMesrlineNetTxBiasCurrentMax_Type(Unsigned32):
    """Custom type rm10010arMesrlineNetTxBiasCurrentMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010arMesrlineNetTxBiasCurrentMax_Type.__name__ = "Unsigned32"
_Rm10010arMesrlineNetTxBiasCurrentMax_Object = MibScalar
rm10010arMesrlineNetTxBiasCurrentMax = _Rm10010arMesrlineNetTxBiasCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 1, 214),
    _Rm10010arMesrlineNetTxBiasCurrentMax_Type()
)
rm10010arMesrlineNetTxBiasCurrentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrlineNetTxBiasCurrentMax.setStatus("current")


class _Rm10010arMesrlineNetRxInputPwrMax_Type(Unsigned32):
    """Custom type rm10010arMesrlineNetRxInputPwrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010arMesrlineNetRxInputPwrMax_Type.__name__ = "Unsigned32"
_Rm10010arMesrlineNetRxInputPwrMax_Object = MibScalar
rm10010arMesrlineNetRxInputPwrMax = _Rm10010arMesrlineNetRxInputPwrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 1, 215),
    _Rm10010arMesrlineNetRxInputPwrMax_Type()
)
rm10010arMesrlineNetRxInputPwrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrlineNetRxInputPwrMax.setStatus("current")


class _Rm10010arMesrlineResidualChromaticDispMax_Type(Unsigned32):
    """Custom type rm10010arMesrlineResidualChromaticDispMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010arMesrlineResidualChromaticDispMax_Type.__name__ = "Unsigned32"
_Rm10010arMesrlineResidualChromaticDispMax_Object = MibScalar
rm10010arMesrlineResidualChromaticDispMax = _Rm10010arMesrlineResidualChromaticDispMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 1, 216),
    _Rm10010arMesrlineResidualChromaticDispMax_Type()
)
rm10010arMesrlineResidualChromaticDispMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrlineResidualChromaticDispMax.setStatus("current")


class _Rm10010arMesrlineDiffGroupDelayMax_Type(Unsigned32):
    """Custom type rm10010arMesrlineDiffGroupDelayMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010arMesrlineDiffGroupDelayMax_Type.__name__ = "Unsigned32"
_Rm10010arMesrlineDiffGroupDelayMax_Object = MibScalar
rm10010arMesrlineDiffGroupDelayMax = _Rm10010arMesrlineDiffGroupDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 1, 217),
    _Rm10010arMesrlineDiffGroupDelayMax_Type()
)
rm10010arMesrlineDiffGroupDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrlineDiffGroupDelayMax.setStatus("current")


class _Rm10010arMesrlineQFactorMax_Type(Unsigned32):
    """Custom type rm10010arMesrlineQFactorMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010arMesrlineQFactorMax_Type.__name__ = "Unsigned32"
_Rm10010arMesrlineQFactorMax_Object = MibScalar
rm10010arMesrlineQFactorMax = _Rm10010arMesrlineQFactorMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 1, 218),
    _Rm10010arMesrlineQFactorMax_Type()
)
rm10010arMesrlineQFactorMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrlineQFactorMax.setStatus("current")


class _Rm10010arMesrlineCarrierFreqOffsetMax_Type(Unsigned32):
    """Custom type rm10010arMesrlineCarrierFreqOffsetMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010arMesrlineCarrierFreqOffsetMax_Type.__name__ = "Unsigned32"
_Rm10010arMesrlineCarrierFreqOffsetMax_Object = MibScalar
rm10010arMesrlineCarrierFreqOffsetMax = _Rm10010arMesrlineCarrierFreqOffsetMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 1, 219),
    _Rm10010arMesrlineCarrierFreqOffsetMax_Type()
)
rm10010arMesrlineCarrierFreqOffsetMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrlineCarrierFreqOffsetMax.setStatus("current")


class _Rm10010arMesrlineOsnrMax_Type(Unsigned32):
    """Custom type rm10010arMesrlineOsnrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010arMesrlineOsnrMax_Type.__name__ = "Unsigned32"
_Rm10010arMesrlineOsnrMax_Object = MibScalar
rm10010arMesrlineOsnrMax = _Rm10010arMesrlineOsnrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 1, 220),
    _Rm10010arMesrlineOsnrMax_Type()
)
rm10010arMesrlineOsnrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrlineOsnrMax.setStatus("current")
_Rm10010arMesrClient_ObjectIdentity = ObjectIdentity
rm10010arMesrClient = _Rm10010arMesrClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 2)
)


class _Rm10010arMesrclientCfpTemp_Type(Unsigned32):
    """Custom type rm10010arMesrclientCfpTemp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010arMesrclientCfpTemp_Type.__name__ = "Unsigned32"
_Rm10010arMesrclientCfpTemp_Object = MibScalar
rm10010arMesrclientCfpTemp = _Rm10010arMesrclientCfpTemp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 2, 8),
    _Rm10010arMesrclientCfpTemp_Type()
)
rm10010arMesrclientCfpTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrclientCfpTemp.setStatus("current")


class _Rm10010arMesrclientCfp3v3Voltage_Type(Unsigned32):
    """Custom type rm10010arMesrclientCfp3v3Voltage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010arMesrclientCfp3v3Voltage_Type.__name__ = "Unsigned32"
_Rm10010arMesrclientCfp3v3Voltage_Object = MibScalar
rm10010arMesrclientCfp3v3Voltage = _Rm10010arMesrclientCfp3v3Voltage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 2, 9),
    _Rm10010arMesrclientCfp3v3Voltage_Type()
)
rm10010arMesrclientCfp3v3Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrclientCfp3v3Voltage.setStatus("current")


class _Rm10010arMesrclientSoaBiasCurrent_Type(Unsigned32):
    """Custom type rm10010arMesrclientSoaBiasCurrent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010arMesrclientSoaBiasCurrent_Type.__name__ = "Unsigned32"
_Rm10010arMesrclientSoaBiasCurrent_Object = MibScalar
rm10010arMesrclientSoaBiasCurrent = _Rm10010arMesrclientSoaBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 2, 10),
    _Rm10010arMesrclientSoaBiasCurrent_Type()
)
rm10010arMesrclientSoaBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrclientSoaBiasCurrent.setStatus("current")
_Rm10010arMesrclientNetTxTempTable_Object = MibTable
rm10010arMesrclientNetTxTempTable = _Rm10010arMesrclientNetTxTempTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 2, 16)
)
if mibBuilder.loadTexts:
    rm10010arMesrclientNetTxTempTable.setStatus("current")
_Rm10010arMesrclientNetTxTempEntry_Object = MibTableRow
rm10010arMesrclientNetTxTempEntry = _Rm10010arMesrclientNetTxTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 2, 16, 1)
)
rm10010arMesrclientNetTxTempEntry.setIndexNames(
    (0, "EKINOPS-Rm10010ar-MIB", "rm10010arMesrclientNetTxTempIndex"),
)
if mibBuilder.loadTexts:
    rm10010arMesrclientNetTxTempEntry.setStatus("current")


class _Rm10010arMesrclientNetTxTempIndex_Type(Integer32):
    """Custom type rm10010arMesrclientNetTxTempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010arMesrclientNetTxTempIndex_Type.__name__ = "Integer32"
_Rm10010arMesrclientNetTxTempIndex_Object = MibTableColumn
rm10010arMesrclientNetTxTempIndex = _Rm10010arMesrclientNetTxTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 2, 16, 1, 1),
    _Rm10010arMesrclientNetTxTempIndex_Type()
)
rm10010arMesrclientNetTxTempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrclientNetTxTempIndex.setStatus("current")


class _Rm10010arMesrclientNetTxTempPortn_Type(Integer32):
    """Custom type rm10010arMesrclientNetTxTempPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010arMesrclientNetTxTempPortn_Type.__name__ = "Integer32"
_Rm10010arMesrclientNetTxTempPortn_Object = MibTableColumn
rm10010arMesrclientNetTxTempPortn = _Rm10010arMesrclientNetTxTempPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 2, 16, 1, 2),
    _Rm10010arMesrclientNetTxTempPortn_Type()
)
rm10010arMesrclientNetTxTempPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrclientNetTxTempPortn.setStatus("current")
_Rm10010arMesrclientNetTxBiasTable_Object = MibTable
rm10010arMesrclientNetTxBiasTable = _Rm10010arMesrclientNetTxBiasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 2, 32)
)
if mibBuilder.loadTexts:
    rm10010arMesrclientNetTxBiasTable.setStatus("current")
_Rm10010arMesrclientNetTxBiasEntry_Object = MibTableRow
rm10010arMesrclientNetTxBiasEntry = _Rm10010arMesrclientNetTxBiasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 2, 32, 1)
)
rm10010arMesrclientNetTxBiasEntry.setIndexNames(
    (0, "EKINOPS-Rm10010ar-MIB", "rm10010arMesrclientNetTxBiasIndex"),
)
if mibBuilder.loadTexts:
    rm10010arMesrclientNetTxBiasEntry.setStatus("current")


class _Rm10010arMesrclientNetTxBiasIndex_Type(Integer32):
    """Custom type rm10010arMesrclientNetTxBiasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010arMesrclientNetTxBiasIndex_Type.__name__ = "Integer32"
_Rm10010arMesrclientNetTxBiasIndex_Object = MibTableColumn
rm10010arMesrclientNetTxBiasIndex = _Rm10010arMesrclientNetTxBiasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 2, 32, 1, 1),
    _Rm10010arMesrclientNetTxBiasIndex_Type()
)
rm10010arMesrclientNetTxBiasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrclientNetTxBiasIndex.setStatus("current")


class _Rm10010arMesrclientNetTxBiasPortn_Type(Integer32):
    """Custom type rm10010arMesrclientNetTxBiasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010arMesrclientNetTxBiasPortn_Type.__name__ = "Integer32"
_Rm10010arMesrclientNetTxBiasPortn_Object = MibTableColumn
rm10010arMesrclientNetTxBiasPortn = _Rm10010arMesrclientNetTxBiasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 2, 32, 1, 2),
    _Rm10010arMesrclientNetTxBiasPortn_Type()
)
rm10010arMesrclientNetTxBiasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrclientNetTxBiasPortn.setStatus("current")
_Rm10010arMesrclientNetTxPwrTable_Object = MibTable
rm10010arMesrclientNetTxPwrTable = _Rm10010arMesrclientNetTxPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 2, 48)
)
if mibBuilder.loadTexts:
    rm10010arMesrclientNetTxPwrTable.setStatus("current")
_Rm10010arMesrclientNetTxPwrEntry_Object = MibTableRow
rm10010arMesrclientNetTxPwrEntry = _Rm10010arMesrclientNetTxPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 2, 48, 1)
)
rm10010arMesrclientNetTxPwrEntry.setIndexNames(
    (0, "EKINOPS-Rm10010ar-MIB", "rm10010arMesrclientNetTxPwrIndex"),
)
if mibBuilder.loadTexts:
    rm10010arMesrclientNetTxPwrEntry.setStatus("current")


class _Rm10010arMesrclientNetTxPwrIndex_Type(Integer32):
    """Custom type rm10010arMesrclientNetTxPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010arMesrclientNetTxPwrIndex_Type.__name__ = "Integer32"
_Rm10010arMesrclientNetTxPwrIndex_Object = MibTableColumn
rm10010arMesrclientNetTxPwrIndex = _Rm10010arMesrclientNetTxPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 2, 48, 1, 1),
    _Rm10010arMesrclientNetTxPwrIndex_Type()
)
rm10010arMesrclientNetTxPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrclientNetTxPwrIndex.setStatus("current")


class _Rm10010arMesrclientNetTxPwrPortn_Type(Integer32):
    """Custom type rm10010arMesrclientNetTxPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010arMesrclientNetTxPwrPortn_Type.__name__ = "Integer32"
_Rm10010arMesrclientNetTxPwrPortn_Object = MibTableColumn
rm10010arMesrclientNetTxPwrPortn = _Rm10010arMesrclientNetTxPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 2, 48, 1, 2),
    _Rm10010arMesrclientNetTxPwrPortn_Type()
)
rm10010arMesrclientNetTxPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrclientNetTxPwrPortn.setStatus("current")
_Rm10010arMesrclientNetRxPwrTable_Object = MibTable
rm10010arMesrclientNetRxPwrTable = _Rm10010arMesrclientNetRxPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 2, 64)
)
if mibBuilder.loadTexts:
    rm10010arMesrclientNetRxPwrTable.setStatus("current")
_Rm10010arMesrclientNetRxPwrEntry_Object = MibTableRow
rm10010arMesrclientNetRxPwrEntry = _Rm10010arMesrclientNetRxPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 2, 64, 1)
)
rm10010arMesrclientNetRxPwrEntry.setIndexNames(
    (0, "EKINOPS-Rm10010ar-MIB", "rm10010arMesrclientNetRxPwrIndex"),
)
if mibBuilder.loadTexts:
    rm10010arMesrclientNetRxPwrEntry.setStatus("current")


class _Rm10010arMesrclientNetRxPwrIndex_Type(Integer32):
    """Custom type rm10010arMesrclientNetRxPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010arMesrclientNetRxPwrIndex_Type.__name__ = "Integer32"
_Rm10010arMesrclientNetRxPwrIndex_Object = MibTableColumn
rm10010arMesrclientNetRxPwrIndex = _Rm10010arMesrclientNetRxPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 2, 64, 1, 1),
    _Rm10010arMesrclientNetRxPwrIndex_Type()
)
rm10010arMesrclientNetRxPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrclientNetRxPwrIndex.setStatus("current")


class _Rm10010arMesrclientNetRxPwrPortn_Type(Integer32):
    """Custom type rm10010arMesrclientNetRxPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010arMesrclientNetRxPwrPortn_Type.__name__ = "Integer32"
_Rm10010arMesrclientNetRxPwrPortn_Object = MibTableColumn
rm10010arMesrclientNetRxPwrPortn = _Rm10010arMesrclientNetRxPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 2, 64, 1, 2),
    _Rm10010arMesrclientNetRxPwrPortn_Type()
)
rm10010arMesrclientNetRxPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrclientNetRxPwrPortn.setStatus("current")
_Rm10010arMesrLine_ObjectIdentity = ObjectIdentity
rm10010arMesrLine = _Rm10010arMesrLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 3)
)


class _Rm10010arMesrlineMsaTemp_Type(Unsigned32):
    """Custom type rm10010arMesrlineMsaTemp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010arMesrlineMsaTemp_Type.__name__ = "Unsigned32"
_Rm10010arMesrlineMsaTemp_Object = MibScalar
rm10010arMesrlineMsaTemp = _Rm10010arMesrlineMsaTemp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 3, 12),
    _Rm10010arMesrlineMsaTemp_Type()
)
rm10010arMesrlineMsaTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrlineMsaTemp.setStatus("current")


class _Rm10010arMesrlineMsa3v3Voltage_Type(Unsigned32):
    """Custom type rm10010arMesrlineMsa3v3Voltage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010arMesrlineMsa3v3Voltage_Type.__name__ = "Unsigned32"
_Rm10010arMesrlineMsa3v3Voltage_Object = MibScalar
rm10010arMesrlineMsa3v3Voltage = _Rm10010arMesrlineMsa3v3Voltage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 3, 13),
    _Rm10010arMesrlineMsa3v3Voltage_Type()
)
rm10010arMesrlineMsa3v3Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrlineMsa3v3Voltage.setStatus("current")


class _Rm10010arMesrlineSoaBiasCurrent_Type(Unsigned32):
    """Custom type rm10010arMesrlineSoaBiasCurrent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010arMesrlineSoaBiasCurrent_Type.__name__ = "Unsigned32"
_Rm10010arMesrlineSoaBiasCurrent_Object = MibScalar
rm10010arMesrlineSoaBiasCurrent = _Rm10010arMesrlineSoaBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 3, 14),
    _Rm10010arMesrlineSoaBiasCurrent_Type()
)
rm10010arMesrlineSoaBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrlineSoaBiasCurrent.setStatus("current")
_Rm10010arMesrlineNetTxLaserOutputPwrTable_Object = MibTable
rm10010arMesrlineNetTxLaserOutputPwrTable = _Rm10010arMesrlineNetTxLaserOutputPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 3, 80)
)
if mibBuilder.loadTexts:
    rm10010arMesrlineNetTxLaserOutputPwrTable.setStatus("current")
_Rm10010arMesrlineNetTxLaserOutputPwrEntry_Object = MibTableRow
rm10010arMesrlineNetTxLaserOutputPwrEntry = _Rm10010arMesrlineNetTxLaserOutputPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 3, 80, 1)
)
rm10010arMesrlineNetTxLaserOutputPwrEntry.setIndexNames(
    (0, "EKINOPS-Rm10010ar-MIB", "rm10010arMesrlineNetTxLaserOutputPwrIndex"),
)
if mibBuilder.loadTexts:
    rm10010arMesrlineNetTxLaserOutputPwrEntry.setStatus("current")


class _Rm10010arMesrlineNetTxLaserOutputPwrIndex_Type(Integer32):
    """Custom type rm10010arMesrlineNetTxLaserOutputPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010arMesrlineNetTxLaserOutputPwrIndex_Type.__name__ = "Integer32"
_Rm10010arMesrlineNetTxLaserOutputPwrIndex_Object = MibTableColumn
rm10010arMesrlineNetTxLaserOutputPwrIndex = _Rm10010arMesrlineNetTxLaserOutputPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 3, 80, 1, 1),
    _Rm10010arMesrlineNetTxLaserOutputPwrIndex_Type()
)
rm10010arMesrlineNetTxLaserOutputPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrlineNetTxLaserOutputPwrIndex.setStatus("current")


class _Rm10010arMesrlineNetTxLaserOutputPwrPortn_Type(Integer32):
    """Custom type rm10010arMesrlineNetTxLaserOutputPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010arMesrlineNetTxLaserOutputPwrPortn_Type.__name__ = "Integer32"
_Rm10010arMesrlineNetTxLaserOutputPwrPortn_Object = MibTableColumn
rm10010arMesrlineNetTxLaserOutputPwrPortn = _Rm10010arMesrlineNetTxLaserOutputPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 3, 80, 1, 2),
    _Rm10010arMesrlineNetTxLaserOutputPwrPortn_Type()
)
rm10010arMesrlineNetTxLaserOutputPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrlineNetTxLaserOutputPwrPortn.setStatus("current")
_Rm10010arMesrlineNetTxLaserTempTable_Object = MibTable
rm10010arMesrlineNetTxLaserTempTable = _Rm10010arMesrlineNetTxLaserTempTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 3, 96)
)
if mibBuilder.loadTexts:
    rm10010arMesrlineNetTxLaserTempTable.setStatus("current")
_Rm10010arMesrlineNetTxLaserTempEntry_Object = MibTableRow
rm10010arMesrlineNetTxLaserTempEntry = _Rm10010arMesrlineNetTxLaserTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 3, 96, 1)
)
rm10010arMesrlineNetTxLaserTempEntry.setIndexNames(
    (0, "EKINOPS-Rm10010ar-MIB", "rm10010arMesrlineNetTxLaserTempIndex"),
)
if mibBuilder.loadTexts:
    rm10010arMesrlineNetTxLaserTempEntry.setStatus("current")


class _Rm10010arMesrlineNetTxLaserTempIndex_Type(Integer32):
    """Custom type rm10010arMesrlineNetTxLaserTempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010arMesrlineNetTxLaserTempIndex_Type.__name__ = "Integer32"
_Rm10010arMesrlineNetTxLaserTempIndex_Object = MibTableColumn
rm10010arMesrlineNetTxLaserTempIndex = _Rm10010arMesrlineNetTxLaserTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 3, 96, 1, 1),
    _Rm10010arMesrlineNetTxLaserTempIndex_Type()
)
rm10010arMesrlineNetTxLaserTempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrlineNetTxLaserTempIndex.setStatus("current")


class _Rm10010arMesrlineNetTxLaserTempPortn_Type(Integer32):
    """Custom type rm10010arMesrlineNetTxLaserTempPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010arMesrlineNetTxLaserTempPortn_Type.__name__ = "Integer32"
_Rm10010arMesrlineNetTxLaserTempPortn_Object = MibTableColumn
rm10010arMesrlineNetTxLaserTempPortn = _Rm10010arMesrlineNetTxLaserTempPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 3, 96, 1, 2),
    _Rm10010arMesrlineNetTxLaserTempPortn_Type()
)
rm10010arMesrlineNetTxLaserTempPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrlineNetTxLaserTempPortn.setStatus("current")
_Rm10010arMesrlineNetTxBiasCurrentTable_Object = MibTable
rm10010arMesrlineNetTxBiasCurrentTable = _Rm10010arMesrlineNetTxBiasCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 3, 112)
)
if mibBuilder.loadTexts:
    rm10010arMesrlineNetTxBiasCurrentTable.setStatus("current")
_Rm10010arMesrlineNetTxBiasCurrentEntry_Object = MibTableRow
rm10010arMesrlineNetTxBiasCurrentEntry = _Rm10010arMesrlineNetTxBiasCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 3, 112, 1)
)
rm10010arMesrlineNetTxBiasCurrentEntry.setIndexNames(
    (0, "EKINOPS-Rm10010ar-MIB", "rm10010arMesrlineNetTxBiasCurrentIndex"),
)
if mibBuilder.loadTexts:
    rm10010arMesrlineNetTxBiasCurrentEntry.setStatus("current")


class _Rm10010arMesrlineNetTxBiasCurrentIndex_Type(Integer32):
    """Custom type rm10010arMesrlineNetTxBiasCurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010arMesrlineNetTxBiasCurrentIndex_Type.__name__ = "Integer32"
_Rm10010arMesrlineNetTxBiasCurrentIndex_Object = MibTableColumn
rm10010arMesrlineNetTxBiasCurrentIndex = _Rm10010arMesrlineNetTxBiasCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 3, 112, 1, 1),
    _Rm10010arMesrlineNetTxBiasCurrentIndex_Type()
)
rm10010arMesrlineNetTxBiasCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrlineNetTxBiasCurrentIndex.setStatus("current")


class _Rm10010arMesrlineNetTxBiasCurrentPortn_Type(Integer32):
    """Custom type rm10010arMesrlineNetTxBiasCurrentPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010arMesrlineNetTxBiasCurrentPortn_Type.__name__ = "Integer32"
_Rm10010arMesrlineNetTxBiasCurrentPortn_Object = MibTableColumn
rm10010arMesrlineNetTxBiasCurrentPortn = _Rm10010arMesrlineNetTxBiasCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 3, 112, 1, 2),
    _Rm10010arMesrlineNetTxBiasCurrentPortn_Type()
)
rm10010arMesrlineNetTxBiasCurrentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrlineNetTxBiasCurrentPortn.setStatus("current")
_Rm10010arMesrlineNetRxInputPwrTable_Object = MibTable
rm10010arMesrlineNetRxInputPwrTable = _Rm10010arMesrlineNetRxInputPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 3, 128)
)
if mibBuilder.loadTexts:
    rm10010arMesrlineNetRxInputPwrTable.setStatus("current")
_Rm10010arMesrlineNetRxInputPwrEntry_Object = MibTableRow
rm10010arMesrlineNetRxInputPwrEntry = _Rm10010arMesrlineNetRxInputPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 3, 128, 1)
)
rm10010arMesrlineNetRxInputPwrEntry.setIndexNames(
    (0, "EKINOPS-Rm10010ar-MIB", "rm10010arMesrlineNetRxInputPwrIndex"),
)
if mibBuilder.loadTexts:
    rm10010arMesrlineNetRxInputPwrEntry.setStatus("current")


class _Rm10010arMesrlineNetRxInputPwrIndex_Type(Integer32):
    """Custom type rm10010arMesrlineNetRxInputPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010arMesrlineNetRxInputPwrIndex_Type.__name__ = "Integer32"
_Rm10010arMesrlineNetRxInputPwrIndex_Object = MibTableColumn
rm10010arMesrlineNetRxInputPwrIndex = _Rm10010arMesrlineNetRxInputPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 3, 128, 1, 1),
    _Rm10010arMesrlineNetRxInputPwrIndex_Type()
)
rm10010arMesrlineNetRxInputPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrlineNetRxInputPwrIndex.setStatus("current")


class _Rm10010arMesrlineNetRxInputPwrPortn_Type(Integer32):
    """Custom type rm10010arMesrlineNetRxInputPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010arMesrlineNetRxInputPwrPortn_Type.__name__ = "Integer32"
_Rm10010arMesrlineNetRxInputPwrPortn_Object = MibTableColumn
rm10010arMesrlineNetRxInputPwrPortn = _Rm10010arMesrlineNetRxInputPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 3, 128, 1, 2),
    _Rm10010arMesrlineNetRxInputPwrPortn_Type()
)
rm10010arMesrlineNetRxInputPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrlineNetRxInputPwrPortn.setStatus("current")
_Rm10010arMesrlineResidualChromaticDispTable_Object = MibTable
rm10010arMesrlineResidualChromaticDispTable = _Rm10010arMesrlineResidualChromaticDispTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 3, 144)
)
if mibBuilder.loadTexts:
    rm10010arMesrlineResidualChromaticDispTable.setStatus("current")
_Rm10010arMesrlineResidualChromaticDispEntry_Object = MibTableRow
rm10010arMesrlineResidualChromaticDispEntry = _Rm10010arMesrlineResidualChromaticDispEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 3, 144, 1)
)
rm10010arMesrlineResidualChromaticDispEntry.setIndexNames(
    (0, "EKINOPS-Rm10010ar-MIB", "rm10010arMesrlineResidualChromaticDispIndex"),
)
if mibBuilder.loadTexts:
    rm10010arMesrlineResidualChromaticDispEntry.setStatus("current")


class _Rm10010arMesrlineResidualChromaticDispIndex_Type(Integer32):
    """Custom type rm10010arMesrlineResidualChromaticDispIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010arMesrlineResidualChromaticDispIndex_Type.__name__ = "Integer32"
_Rm10010arMesrlineResidualChromaticDispIndex_Object = MibTableColumn
rm10010arMesrlineResidualChromaticDispIndex = _Rm10010arMesrlineResidualChromaticDispIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 3, 144, 1, 1),
    _Rm10010arMesrlineResidualChromaticDispIndex_Type()
)
rm10010arMesrlineResidualChromaticDispIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrlineResidualChromaticDispIndex.setStatus("current")


class _Rm10010arMesrlineResidualChromaticDispPortn_Type(Integer32):
    """Custom type rm10010arMesrlineResidualChromaticDispPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010arMesrlineResidualChromaticDispPortn_Type.__name__ = "Integer32"
_Rm10010arMesrlineResidualChromaticDispPortn_Object = MibTableColumn
rm10010arMesrlineResidualChromaticDispPortn = _Rm10010arMesrlineResidualChromaticDispPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 3, 144, 1, 2),
    _Rm10010arMesrlineResidualChromaticDispPortn_Type()
)
rm10010arMesrlineResidualChromaticDispPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrlineResidualChromaticDispPortn.setStatus("current")
_Rm10010arMesrlineDiffGroupDelayTable_Object = MibTable
rm10010arMesrlineDiffGroupDelayTable = _Rm10010arMesrlineDiffGroupDelayTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 3, 148)
)
if mibBuilder.loadTexts:
    rm10010arMesrlineDiffGroupDelayTable.setStatus("current")
_Rm10010arMesrlineDiffGroupDelayEntry_Object = MibTableRow
rm10010arMesrlineDiffGroupDelayEntry = _Rm10010arMesrlineDiffGroupDelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 3, 148, 1)
)
rm10010arMesrlineDiffGroupDelayEntry.setIndexNames(
    (0, "EKINOPS-Rm10010ar-MIB", "rm10010arMesrlineDiffGroupDelayIndex"),
)
if mibBuilder.loadTexts:
    rm10010arMesrlineDiffGroupDelayEntry.setStatus("current")


class _Rm10010arMesrlineDiffGroupDelayIndex_Type(Integer32):
    """Custom type rm10010arMesrlineDiffGroupDelayIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010arMesrlineDiffGroupDelayIndex_Type.__name__ = "Integer32"
_Rm10010arMesrlineDiffGroupDelayIndex_Object = MibTableColumn
rm10010arMesrlineDiffGroupDelayIndex = _Rm10010arMesrlineDiffGroupDelayIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 3, 148, 1, 1),
    _Rm10010arMesrlineDiffGroupDelayIndex_Type()
)
rm10010arMesrlineDiffGroupDelayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrlineDiffGroupDelayIndex.setStatus("current")


class _Rm10010arMesrlineDiffGroupDelayPortn_Type(Integer32):
    """Custom type rm10010arMesrlineDiffGroupDelayPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010arMesrlineDiffGroupDelayPortn_Type.__name__ = "Integer32"
_Rm10010arMesrlineDiffGroupDelayPortn_Object = MibTableColumn
rm10010arMesrlineDiffGroupDelayPortn = _Rm10010arMesrlineDiffGroupDelayPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 3, 148, 1, 2),
    _Rm10010arMesrlineDiffGroupDelayPortn_Type()
)
rm10010arMesrlineDiffGroupDelayPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrlineDiffGroupDelayPortn.setStatus("current")
_Rm10010arMesrlineQFactorTable_Object = MibTable
rm10010arMesrlineQFactorTable = _Rm10010arMesrlineQFactorTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 3, 152)
)
if mibBuilder.loadTexts:
    rm10010arMesrlineQFactorTable.setStatus("current")
_Rm10010arMesrlineQFactorEntry_Object = MibTableRow
rm10010arMesrlineQFactorEntry = _Rm10010arMesrlineQFactorEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 3, 152, 1)
)
rm10010arMesrlineQFactorEntry.setIndexNames(
    (0, "EKINOPS-Rm10010ar-MIB", "rm10010arMesrlineQFactorIndex"),
)
if mibBuilder.loadTexts:
    rm10010arMesrlineQFactorEntry.setStatus("current")


class _Rm10010arMesrlineQFactorIndex_Type(Integer32):
    """Custom type rm10010arMesrlineQFactorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010arMesrlineQFactorIndex_Type.__name__ = "Integer32"
_Rm10010arMesrlineQFactorIndex_Object = MibTableColumn
rm10010arMesrlineQFactorIndex = _Rm10010arMesrlineQFactorIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 3, 152, 1, 1),
    _Rm10010arMesrlineQFactorIndex_Type()
)
rm10010arMesrlineQFactorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrlineQFactorIndex.setStatus("current")


class _Rm10010arMesrlineQFactorPortn_Type(Integer32):
    """Custom type rm10010arMesrlineQFactorPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010arMesrlineQFactorPortn_Type.__name__ = "Integer32"
_Rm10010arMesrlineQFactorPortn_Object = MibTableColumn
rm10010arMesrlineQFactorPortn = _Rm10010arMesrlineQFactorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 3, 152, 1, 2),
    _Rm10010arMesrlineQFactorPortn_Type()
)
rm10010arMesrlineQFactorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrlineQFactorPortn.setStatus("current")
_Rm10010arMesrlineCarrierFreqOffsetTable_Object = MibTable
rm10010arMesrlineCarrierFreqOffsetTable = _Rm10010arMesrlineCarrierFreqOffsetTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 3, 156)
)
if mibBuilder.loadTexts:
    rm10010arMesrlineCarrierFreqOffsetTable.setStatus("current")
_Rm10010arMesrlineCarrierFreqOffsetEntry_Object = MibTableRow
rm10010arMesrlineCarrierFreqOffsetEntry = _Rm10010arMesrlineCarrierFreqOffsetEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 3, 156, 1)
)
rm10010arMesrlineCarrierFreqOffsetEntry.setIndexNames(
    (0, "EKINOPS-Rm10010ar-MIB", "rm10010arMesrlineCarrierFreqOffsetIndex"),
)
if mibBuilder.loadTexts:
    rm10010arMesrlineCarrierFreqOffsetEntry.setStatus("current")


class _Rm10010arMesrlineCarrierFreqOffsetIndex_Type(Integer32):
    """Custom type rm10010arMesrlineCarrierFreqOffsetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010arMesrlineCarrierFreqOffsetIndex_Type.__name__ = "Integer32"
_Rm10010arMesrlineCarrierFreqOffsetIndex_Object = MibTableColumn
rm10010arMesrlineCarrierFreqOffsetIndex = _Rm10010arMesrlineCarrierFreqOffsetIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 3, 156, 1, 1),
    _Rm10010arMesrlineCarrierFreqOffsetIndex_Type()
)
rm10010arMesrlineCarrierFreqOffsetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrlineCarrierFreqOffsetIndex.setStatus("current")


class _Rm10010arMesrlineCarrierFreqOffsetPortn_Type(Integer32):
    """Custom type rm10010arMesrlineCarrierFreqOffsetPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010arMesrlineCarrierFreqOffsetPortn_Type.__name__ = "Integer32"
_Rm10010arMesrlineCarrierFreqOffsetPortn_Object = MibTableColumn
rm10010arMesrlineCarrierFreqOffsetPortn = _Rm10010arMesrlineCarrierFreqOffsetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 3, 156, 1, 2),
    _Rm10010arMesrlineCarrierFreqOffsetPortn_Type()
)
rm10010arMesrlineCarrierFreqOffsetPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrlineCarrierFreqOffsetPortn.setStatus("current")
_Rm10010arMesrlineOsnrTable_Object = MibTable
rm10010arMesrlineOsnrTable = _Rm10010arMesrlineOsnrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 3, 160)
)
if mibBuilder.loadTexts:
    rm10010arMesrlineOsnrTable.setStatus("current")
_Rm10010arMesrlineOsnrEntry_Object = MibTableRow
rm10010arMesrlineOsnrEntry = _Rm10010arMesrlineOsnrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 3, 160, 1)
)
rm10010arMesrlineOsnrEntry.setIndexNames(
    (0, "EKINOPS-Rm10010ar-MIB", "rm10010arMesrlineOsnrIndex"),
)
if mibBuilder.loadTexts:
    rm10010arMesrlineOsnrEntry.setStatus("current")


class _Rm10010arMesrlineOsnrIndex_Type(Integer32):
    """Custom type rm10010arMesrlineOsnrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010arMesrlineOsnrIndex_Type.__name__ = "Integer32"
_Rm10010arMesrlineOsnrIndex_Object = MibTableColumn
rm10010arMesrlineOsnrIndex = _Rm10010arMesrlineOsnrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 3, 160, 1, 1),
    _Rm10010arMesrlineOsnrIndex_Type()
)
rm10010arMesrlineOsnrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrlineOsnrIndex.setStatus("current")


class _Rm10010arMesrlineOsnrPortn_Type(Integer32):
    """Custom type rm10010arMesrlineOsnrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010arMesrlineOsnrPortn_Type.__name__ = "Integer32"
_Rm10010arMesrlineOsnrPortn_Object = MibTableColumn
rm10010arMesrlineOsnrPortn = _Rm10010arMesrlineOsnrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 3, 3, 160, 1, 2),
    _Rm10010arMesrlineOsnrPortn_Type()
)
rm10010arMesrlineOsnrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMesrlineOsnrPortn.setStatus("current")
_Rm10010arcounters_ObjectIdentity = ObjectIdentity
rm10010arcounters = _Rm10010arcounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4)
)
_Rm10010arCntOther_ObjectIdentity = ObjectIdentity
rm10010arCntOther = _Rm10010arCntOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4, 1)
)
_Rm10010arCntClient_ObjectIdentity = ObjectIdentity
rm10010arCntClient = _Rm10010arCntClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4, 2)
)
_Rm10010arCntclientInputErrorCounterLaneOneTable_Object = MibTable
rm10010arCntclientInputErrorCounterLaneOneTable = _Rm10010arCntclientInputErrorCounterLaneOneTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4, 2, 16)
)
if mibBuilder.loadTexts:
    rm10010arCntclientInputErrorCounterLaneOneTable.setStatus("current")
_Rm10010arCntclientInputErrorCounterLaneOneEntry_Object = MibTableRow
rm10010arCntclientInputErrorCounterLaneOneEntry = _Rm10010arCntclientInputErrorCounterLaneOneEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4, 2, 16, 1)
)
rm10010arCntclientInputErrorCounterLaneOneEntry.setIndexNames(
    (0, "EKINOPS-Rm10010ar-MIB", "rm10010arCntclientInputErrorCounterLaneOneIndex"),
)
if mibBuilder.loadTexts:
    rm10010arCntclientInputErrorCounterLaneOneEntry.setStatus("current")


class _Rm10010arCntclientInputErrorCounterLaneOneIndex_Type(Integer32):
    """Custom type rm10010arCntclientInputErrorCounterLaneOneIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010arCntclientInputErrorCounterLaneOneIndex_Type.__name__ = "Integer32"
_Rm10010arCntclientInputErrorCounterLaneOneIndex_Object = MibTableColumn
rm10010arCntclientInputErrorCounterLaneOneIndex = _Rm10010arCntclientInputErrorCounterLaneOneIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4, 2, 16, 1, 1),
    _Rm10010arCntclientInputErrorCounterLaneOneIndex_Type()
)
rm10010arCntclientInputErrorCounterLaneOneIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arCntclientInputErrorCounterLaneOneIndex.setStatus("current")
_Rm10010arCntclientInputErrorCounterLaneOneValuePortn_Type = Counter32
_Rm10010arCntclientInputErrorCounterLaneOneValuePortn_Object = MibTableColumn
rm10010arCntclientInputErrorCounterLaneOneValuePortn = _Rm10010arCntclientInputErrorCounterLaneOneValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4, 2, 16, 1, 2),
    _Rm10010arCntclientInputErrorCounterLaneOneValuePortn_Type()
)
rm10010arCntclientInputErrorCounterLaneOneValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arCntclientInputErrorCounterLaneOneValuePortn.setStatus("current")
_Rm10010arCntclientInputErrorCounterLaneOneErrorPortn_Type = EkiOnOff
_Rm10010arCntclientInputErrorCounterLaneOneErrorPortn_Object = MibTableColumn
rm10010arCntclientInputErrorCounterLaneOneErrorPortn = _Rm10010arCntclientInputErrorCounterLaneOneErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4, 2, 16, 1, 3),
    _Rm10010arCntclientInputErrorCounterLaneOneErrorPortn_Type()
)
rm10010arCntclientInputErrorCounterLaneOneErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arCntclientInputErrorCounterLaneOneErrorPortn.setStatus("current")
_Rm10010arCntclientInputErrorCounterLaneOneOverloadPortn_Type = EkiOnOff
_Rm10010arCntclientInputErrorCounterLaneOneOverloadPortn_Object = MibTableColumn
rm10010arCntclientInputErrorCounterLaneOneOverloadPortn = _Rm10010arCntclientInputErrorCounterLaneOneOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4, 2, 16, 1, 4),
    _Rm10010arCntclientInputErrorCounterLaneOneOverloadPortn_Type()
)
rm10010arCntclientInputErrorCounterLaneOneOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arCntclientInputErrorCounterLaneOneOverloadPortn.setStatus("current")
_Rm10010arCntclientInputErrorCounterLaneTwoTable_Object = MibTable
rm10010arCntclientInputErrorCounterLaneTwoTable = _Rm10010arCntclientInputErrorCounterLaneTwoTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4, 2, 32)
)
if mibBuilder.loadTexts:
    rm10010arCntclientInputErrorCounterLaneTwoTable.setStatus("current")
_Rm10010arCntclientInputErrorCounterLaneTwoEntry_Object = MibTableRow
rm10010arCntclientInputErrorCounterLaneTwoEntry = _Rm10010arCntclientInputErrorCounterLaneTwoEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4, 2, 32, 1)
)
rm10010arCntclientInputErrorCounterLaneTwoEntry.setIndexNames(
    (0, "EKINOPS-Rm10010ar-MIB", "rm10010arCntclientInputErrorCounterLaneTwoIndex"),
)
if mibBuilder.loadTexts:
    rm10010arCntclientInputErrorCounterLaneTwoEntry.setStatus("current")


class _Rm10010arCntclientInputErrorCounterLaneTwoIndex_Type(Integer32):
    """Custom type rm10010arCntclientInputErrorCounterLaneTwoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010arCntclientInputErrorCounterLaneTwoIndex_Type.__name__ = "Integer32"
_Rm10010arCntclientInputErrorCounterLaneTwoIndex_Object = MibTableColumn
rm10010arCntclientInputErrorCounterLaneTwoIndex = _Rm10010arCntclientInputErrorCounterLaneTwoIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4, 2, 32, 1, 1),
    _Rm10010arCntclientInputErrorCounterLaneTwoIndex_Type()
)
rm10010arCntclientInputErrorCounterLaneTwoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arCntclientInputErrorCounterLaneTwoIndex.setStatus("current")
_Rm10010arCntclientInputErrorCounterLaneTwoValuePortn_Type = Counter32
_Rm10010arCntclientInputErrorCounterLaneTwoValuePortn_Object = MibTableColumn
rm10010arCntclientInputErrorCounterLaneTwoValuePortn = _Rm10010arCntclientInputErrorCounterLaneTwoValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4, 2, 32, 1, 2),
    _Rm10010arCntclientInputErrorCounterLaneTwoValuePortn_Type()
)
rm10010arCntclientInputErrorCounterLaneTwoValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arCntclientInputErrorCounterLaneTwoValuePortn.setStatus("current")
_Rm10010arCntclientInputErrorCounterLaneTwoErrorPortn_Type = EkiOnOff
_Rm10010arCntclientInputErrorCounterLaneTwoErrorPortn_Object = MibTableColumn
rm10010arCntclientInputErrorCounterLaneTwoErrorPortn = _Rm10010arCntclientInputErrorCounterLaneTwoErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4, 2, 32, 1, 3),
    _Rm10010arCntclientInputErrorCounterLaneTwoErrorPortn_Type()
)
rm10010arCntclientInputErrorCounterLaneTwoErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arCntclientInputErrorCounterLaneTwoErrorPortn.setStatus("current")
_Rm10010arCntclientInputErrorCounterLaneTwoOverloadPortn_Type = EkiOnOff
_Rm10010arCntclientInputErrorCounterLaneTwoOverloadPortn_Object = MibTableColumn
rm10010arCntclientInputErrorCounterLaneTwoOverloadPortn = _Rm10010arCntclientInputErrorCounterLaneTwoOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4, 2, 32, 1, 4),
    _Rm10010arCntclientInputErrorCounterLaneTwoOverloadPortn_Type()
)
rm10010arCntclientInputErrorCounterLaneTwoOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arCntclientInputErrorCounterLaneTwoOverloadPortn.setStatus("current")
_Rm10010arCntclientInputErrorCounterTable_Object = MibTable
rm10010arCntclientInputErrorCounterTable = _Rm10010arCntclientInputErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4, 2, 80)
)
if mibBuilder.loadTexts:
    rm10010arCntclientInputErrorCounterTable.setStatus("current")
_Rm10010arCntclientInputErrorCounterEntry_Object = MibTableRow
rm10010arCntclientInputErrorCounterEntry = _Rm10010arCntclientInputErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4, 2, 80, 1)
)
rm10010arCntclientInputErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Rm10010ar-MIB", "rm10010arCntclientInputErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    rm10010arCntclientInputErrorCounterEntry.setStatus("current")


class _Rm10010arCntclientInputErrorCounterIndex_Type(Integer32):
    """Custom type rm10010arCntclientInputErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010arCntclientInputErrorCounterIndex_Type.__name__ = "Integer32"
_Rm10010arCntclientInputErrorCounterIndex_Object = MibTableColumn
rm10010arCntclientInputErrorCounterIndex = _Rm10010arCntclientInputErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4, 2, 80, 1, 1),
    _Rm10010arCntclientInputErrorCounterIndex_Type()
)
rm10010arCntclientInputErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arCntclientInputErrorCounterIndex.setStatus("current")
_Rm10010arCntclientInputErrorCounterValuePortn_Type = Counter32
_Rm10010arCntclientInputErrorCounterValuePortn_Object = MibTableColumn
rm10010arCntclientInputErrorCounterValuePortn = _Rm10010arCntclientInputErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4, 2, 80, 1, 2),
    _Rm10010arCntclientInputErrorCounterValuePortn_Type()
)
rm10010arCntclientInputErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arCntclientInputErrorCounterValuePortn.setStatus("current")
_Rm10010arCntclientInputErrorCounterErrorPortn_Type = EkiOnOff
_Rm10010arCntclientInputErrorCounterErrorPortn_Object = MibTableColumn
rm10010arCntclientInputErrorCounterErrorPortn = _Rm10010arCntclientInputErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4, 2, 80, 1, 3),
    _Rm10010arCntclientInputErrorCounterErrorPortn_Type()
)
rm10010arCntclientInputErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arCntclientInputErrorCounterErrorPortn.setStatus("current")
_Rm10010arCntclientInputErrorCounterOverloadPortn_Type = EkiOnOff
_Rm10010arCntclientInputErrorCounterOverloadPortn_Object = MibTableColumn
rm10010arCntclientInputErrorCounterOverloadPortn = _Rm10010arCntclientInputErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4, 2, 80, 1, 4),
    _Rm10010arCntclientInputErrorCounterOverloadPortn_Type()
)
rm10010arCntclientInputErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arCntclientInputErrorCounterOverloadPortn.setStatus("current")
_Rm10010arCntclientCbipCounterTable_Object = MibTable
rm10010arCntclientCbipCounterTable = _Rm10010arCntclientCbipCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4, 2, 96)
)
if mibBuilder.loadTexts:
    rm10010arCntclientCbipCounterTable.setStatus("current")
_Rm10010arCntclientCbipCounterEntry_Object = MibTableRow
rm10010arCntclientCbipCounterEntry = _Rm10010arCntclientCbipCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4, 2, 96, 1)
)
rm10010arCntclientCbipCounterEntry.setIndexNames(
    (0, "EKINOPS-Rm10010ar-MIB", "rm10010arCntclientCbipCounterIndex"),
)
if mibBuilder.loadTexts:
    rm10010arCntclientCbipCounterEntry.setStatus("current")


class _Rm10010arCntclientCbipCounterIndex_Type(Integer32):
    """Custom type rm10010arCntclientCbipCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010arCntclientCbipCounterIndex_Type.__name__ = "Integer32"
_Rm10010arCntclientCbipCounterIndex_Object = MibTableColumn
rm10010arCntclientCbipCounterIndex = _Rm10010arCntclientCbipCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4, 2, 96, 1, 1),
    _Rm10010arCntclientCbipCounterIndex_Type()
)
rm10010arCntclientCbipCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arCntclientCbipCounterIndex.setStatus("current")
_Rm10010arCntclientCbipCounterValuePortn_Type = Counter32
_Rm10010arCntclientCbipCounterValuePortn_Object = MibTableColumn
rm10010arCntclientCbipCounterValuePortn = _Rm10010arCntclientCbipCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4, 2, 96, 1, 2),
    _Rm10010arCntclientCbipCounterValuePortn_Type()
)
rm10010arCntclientCbipCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arCntclientCbipCounterValuePortn.setStatus("current")
_Rm10010arCntclientCbipCounterErrorPortn_Type = EkiOnOff
_Rm10010arCntclientCbipCounterErrorPortn_Object = MibTableColumn
rm10010arCntclientCbipCounterErrorPortn = _Rm10010arCntclientCbipCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4, 2, 96, 1, 3),
    _Rm10010arCntclientCbipCounterErrorPortn_Type()
)
rm10010arCntclientCbipCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arCntclientCbipCounterErrorPortn.setStatus("current")
_Rm10010arCntclientCbipCounterOverloadPortn_Type = EkiOnOff
_Rm10010arCntclientCbipCounterOverloadPortn_Object = MibTableColumn
rm10010arCntclientCbipCounterOverloadPortn = _Rm10010arCntclientCbipCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4, 2, 96, 1, 4),
    _Rm10010arCntclientCbipCounterOverloadPortn_Type()
)
rm10010arCntclientCbipCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arCntclientCbipCounterOverloadPortn.setStatus("current")
_Rm10010arCntLine_ObjectIdentity = ObjectIdentity
rm10010arCntLine = _Rm10010arCntLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4, 3)
)
_Rm10010arCntlocalLineSmBip8ErrorCounterTable_Object = MibTable
rm10010arCntlocalLineSmBip8ErrorCounterTable = _Rm10010arCntlocalLineSmBip8ErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4, 3, 192)
)
if mibBuilder.loadTexts:
    rm10010arCntlocalLineSmBip8ErrorCounterTable.setStatus("current")
_Rm10010arCntlocalLineSmBip8ErrorCounterEntry_Object = MibTableRow
rm10010arCntlocalLineSmBip8ErrorCounterEntry = _Rm10010arCntlocalLineSmBip8ErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4, 3, 192, 1)
)
rm10010arCntlocalLineSmBip8ErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Rm10010ar-MIB", "rm10010arCntlocalLineSmBip8ErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    rm10010arCntlocalLineSmBip8ErrorCounterEntry.setStatus("current")


class _Rm10010arCntlocalLineSmBip8ErrorCounterIndex_Type(Integer32):
    """Custom type rm10010arCntlocalLineSmBip8ErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010arCntlocalLineSmBip8ErrorCounterIndex_Type.__name__ = "Integer32"
_Rm10010arCntlocalLineSmBip8ErrorCounterIndex_Object = MibTableColumn
rm10010arCntlocalLineSmBip8ErrorCounterIndex = _Rm10010arCntlocalLineSmBip8ErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4, 3, 192, 1, 1),
    _Rm10010arCntlocalLineSmBip8ErrorCounterIndex_Type()
)
rm10010arCntlocalLineSmBip8ErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arCntlocalLineSmBip8ErrorCounterIndex.setStatus("current")
_Rm10010arCntlocalLineSmBip8ErrorCounterValuePortn_Type = Counter64
_Rm10010arCntlocalLineSmBip8ErrorCounterValuePortn_Object = MibTableColumn
rm10010arCntlocalLineSmBip8ErrorCounterValuePortn = _Rm10010arCntlocalLineSmBip8ErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4, 3, 192, 1, 2),
    _Rm10010arCntlocalLineSmBip8ErrorCounterValuePortn_Type()
)
rm10010arCntlocalLineSmBip8ErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arCntlocalLineSmBip8ErrorCounterValuePortn.setStatus("current")
_Rm10010arCntlocalLineSmBip8ErrorCounterErrorPortn_Type = EkiOnOff
_Rm10010arCntlocalLineSmBip8ErrorCounterErrorPortn_Object = MibTableColumn
rm10010arCntlocalLineSmBip8ErrorCounterErrorPortn = _Rm10010arCntlocalLineSmBip8ErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4, 3, 192, 1, 3),
    _Rm10010arCntlocalLineSmBip8ErrorCounterErrorPortn_Type()
)
rm10010arCntlocalLineSmBip8ErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arCntlocalLineSmBip8ErrorCounterErrorPortn.setStatus("current")
_Rm10010arCntlocalLineSmBip8ErrorCounterOverloadPortn_Type = EkiOnOff
_Rm10010arCntlocalLineSmBip8ErrorCounterOverloadPortn_Object = MibTableColumn
rm10010arCntlocalLineSmBip8ErrorCounterOverloadPortn = _Rm10010arCntlocalLineSmBip8ErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4, 3, 192, 1, 4),
    _Rm10010arCntlocalLineSmBip8ErrorCounterOverloadPortn_Type()
)
rm10010arCntlocalLineSmBip8ErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arCntlocalLineSmBip8ErrorCounterOverloadPortn.setStatus("current")
_Rm10010arCntlocalLineFecCorrectedErrorsCounterTable_Object = MibTable
rm10010arCntlocalLineFecCorrectedErrorsCounterTable = _Rm10010arCntlocalLineFecCorrectedErrorsCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4, 3, 193)
)
if mibBuilder.loadTexts:
    rm10010arCntlocalLineFecCorrectedErrorsCounterTable.setStatus("current")
_Rm10010arCntlocalLineFecCorrectedErrorsCounterEntry_Object = MibTableRow
rm10010arCntlocalLineFecCorrectedErrorsCounterEntry = _Rm10010arCntlocalLineFecCorrectedErrorsCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4, 3, 193, 1)
)
rm10010arCntlocalLineFecCorrectedErrorsCounterEntry.setIndexNames(
    (0, "EKINOPS-Rm10010ar-MIB", "rm10010arCntlocalLineFecCorrectedErrorsCounterIndex"),
)
if mibBuilder.loadTexts:
    rm10010arCntlocalLineFecCorrectedErrorsCounterEntry.setStatus("current")


class _Rm10010arCntlocalLineFecCorrectedErrorsCounterIndex_Type(Integer32):
    """Custom type rm10010arCntlocalLineFecCorrectedErrorsCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010arCntlocalLineFecCorrectedErrorsCounterIndex_Type.__name__ = "Integer32"
_Rm10010arCntlocalLineFecCorrectedErrorsCounterIndex_Object = MibTableColumn
rm10010arCntlocalLineFecCorrectedErrorsCounterIndex = _Rm10010arCntlocalLineFecCorrectedErrorsCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4, 3, 193, 1, 1),
    _Rm10010arCntlocalLineFecCorrectedErrorsCounterIndex_Type()
)
rm10010arCntlocalLineFecCorrectedErrorsCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arCntlocalLineFecCorrectedErrorsCounterIndex.setStatus("current")
_Rm10010arCntlocalLineFecCorrectedErrorsCounterValuePortn_Type = Counter64
_Rm10010arCntlocalLineFecCorrectedErrorsCounterValuePortn_Object = MibTableColumn
rm10010arCntlocalLineFecCorrectedErrorsCounterValuePortn = _Rm10010arCntlocalLineFecCorrectedErrorsCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4, 3, 193, 1, 2),
    _Rm10010arCntlocalLineFecCorrectedErrorsCounterValuePortn_Type()
)
rm10010arCntlocalLineFecCorrectedErrorsCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arCntlocalLineFecCorrectedErrorsCounterValuePortn.setStatus("current")
_Rm10010arCntlocalLineFecCorrectedErrorsCounterErrorPortn_Type = EkiOnOff
_Rm10010arCntlocalLineFecCorrectedErrorsCounterErrorPortn_Object = MibTableColumn
rm10010arCntlocalLineFecCorrectedErrorsCounterErrorPortn = _Rm10010arCntlocalLineFecCorrectedErrorsCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4, 3, 193, 1, 3),
    _Rm10010arCntlocalLineFecCorrectedErrorsCounterErrorPortn_Type()
)
rm10010arCntlocalLineFecCorrectedErrorsCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arCntlocalLineFecCorrectedErrorsCounterErrorPortn.setStatus("current")
_Rm10010arCntlocalLineFecCorrectedErrorsCounterOverloadPortn_Type = EkiOnOff
_Rm10010arCntlocalLineFecCorrectedErrorsCounterOverloadPortn_Object = MibTableColumn
rm10010arCntlocalLineFecCorrectedErrorsCounterOverloadPortn = _Rm10010arCntlocalLineFecCorrectedErrorsCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4, 3, 193, 1, 4),
    _Rm10010arCntlocalLineFecCorrectedErrorsCounterOverloadPortn_Type()
)
rm10010arCntlocalLineFecCorrectedErrorsCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arCntlocalLineFecCorrectedErrorsCounterOverloadPortn.setStatus("current")
_Rm10010arCntremoteLineSmBip8ErrorCounterTable_Object = MibTable
rm10010arCntremoteLineSmBip8ErrorCounterTable = _Rm10010arCntremoteLineSmBip8ErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4, 3, 194)
)
if mibBuilder.loadTexts:
    rm10010arCntremoteLineSmBip8ErrorCounterTable.setStatus("current")
_Rm10010arCntremoteLineSmBip8ErrorCounterEntry_Object = MibTableRow
rm10010arCntremoteLineSmBip8ErrorCounterEntry = _Rm10010arCntremoteLineSmBip8ErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4, 3, 194, 1)
)
rm10010arCntremoteLineSmBip8ErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Rm10010ar-MIB", "rm10010arCntremoteLineSmBip8ErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    rm10010arCntremoteLineSmBip8ErrorCounterEntry.setStatus("current")


class _Rm10010arCntremoteLineSmBip8ErrorCounterIndex_Type(Integer32):
    """Custom type rm10010arCntremoteLineSmBip8ErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010arCntremoteLineSmBip8ErrorCounterIndex_Type.__name__ = "Integer32"
_Rm10010arCntremoteLineSmBip8ErrorCounterIndex_Object = MibTableColumn
rm10010arCntremoteLineSmBip8ErrorCounterIndex = _Rm10010arCntremoteLineSmBip8ErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4, 3, 194, 1, 1),
    _Rm10010arCntremoteLineSmBip8ErrorCounterIndex_Type()
)
rm10010arCntremoteLineSmBip8ErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arCntremoteLineSmBip8ErrorCounterIndex.setStatus("current")
_Rm10010arCntremoteLineSmBip8ErrorCounterValuePortn_Type = Counter64
_Rm10010arCntremoteLineSmBip8ErrorCounterValuePortn_Object = MibTableColumn
rm10010arCntremoteLineSmBip8ErrorCounterValuePortn = _Rm10010arCntremoteLineSmBip8ErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4, 3, 194, 1, 2),
    _Rm10010arCntremoteLineSmBip8ErrorCounterValuePortn_Type()
)
rm10010arCntremoteLineSmBip8ErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arCntremoteLineSmBip8ErrorCounterValuePortn.setStatus("current")
_Rm10010arCntremoteLineSmBip8ErrorCounterErrorPortn_Type = EkiOnOff
_Rm10010arCntremoteLineSmBip8ErrorCounterErrorPortn_Object = MibTableColumn
rm10010arCntremoteLineSmBip8ErrorCounterErrorPortn = _Rm10010arCntremoteLineSmBip8ErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4, 3, 194, 1, 3),
    _Rm10010arCntremoteLineSmBip8ErrorCounterErrorPortn_Type()
)
rm10010arCntremoteLineSmBip8ErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arCntremoteLineSmBip8ErrorCounterErrorPortn.setStatus("current")
_Rm10010arCntremoteLineSmBip8ErrorCounterOverloadPortn_Type = EkiOnOff
_Rm10010arCntremoteLineSmBip8ErrorCounterOverloadPortn_Object = MibTableColumn
rm10010arCntremoteLineSmBip8ErrorCounterOverloadPortn = _Rm10010arCntremoteLineSmBip8ErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4, 3, 194, 1, 4),
    _Rm10010arCntremoteLineSmBip8ErrorCounterOverloadPortn_Type()
)
rm10010arCntremoteLineSmBip8ErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arCntremoteLineSmBip8ErrorCounterOverloadPortn.setStatus("current")
_Rm10010arCntlineDfrmTimCntTable_Object = MibTable
rm10010arCntlineDfrmTimCntTable = _Rm10010arCntlineDfrmTimCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4, 3, 195)
)
if mibBuilder.loadTexts:
    rm10010arCntlineDfrmTimCntTable.setStatus("current")
_Rm10010arCntlineDfrmTimCntEntry_Object = MibTableRow
rm10010arCntlineDfrmTimCntEntry = _Rm10010arCntlineDfrmTimCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4, 3, 195, 1)
)
rm10010arCntlineDfrmTimCntEntry.setIndexNames(
    (0, "EKINOPS-Rm10010ar-MIB", "rm10010arCntlineDfrmTimCntIndex"),
)
if mibBuilder.loadTexts:
    rm10010arCntlineDfrmTimCntEntry.setStatus("current")


class _Rm10010arCntlineDfrmTimCntIndex_Type(Integer32):
    """Custom type rm10010arCntlineDfrmTimCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010arCntlineDfrmTimCntIndex_Type.__name__ = "Integer32"
_Rm10010arCntlineDfrmTimCntIndex_Object = MibTableColumn
rm10010arCntlineDfrmTimCntIndex = _Rm10010arCntlineDfrmTimCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4, 3, 195, 1, 1),
    _Rm10010arCntlineDfrmTimCntIndex_Type()
)
rm10010arCntlineDfrmTimCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arCntlineDfrmTimCntIndex.setStatus("current")
_Rm10010arCntlineDfrmTimCntValuePortn_Type = Counter64
_Rm10010arCntlineDfrmTimCntValuePortn_Object = MibTableColumn
rm10010arCntlineDfrmTimCntValuePortn = _Rm10010arCntlineDfrmTimCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4, 3, 195, 1, 2),
    _Rm10010arCntlineDfrmTimCntValuePortn_Type()
)
rm10010arCntlineDfrmTimCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arCntlineDfrmTimCntValuePortn.setStatus("current")
_Rm10010arCntlineDfrmTimCntErrorPortn_Type = EkiOnOff
_Rm10010arCntlineDfrmTimCntErrorPortn_Object = MibTableColumn
rm10010arCntlineDfrmTimCntErrorPortn = _Rm10010arCntlineDfrmTimCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4, 3, 195, 1, 3),
    _Rm10010arCntlineDfrmTimCntErrorPortn_Type()
)
rm10010arCntlineDfrmTimCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arCntlineDfrmTimCntErrorPortn.setStatus("current")
_Rm10010arCntlineDfrmTimCntOverloadPortn_Type = EkiOnOff
_Rm10010arCntlineDfrmTimCntOverloadPortn_Object = MibTableColumn
rm10010arCntlineDfrmTimCntOverloadPortn = _Rm10010arCntlineDfrmTimCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4, 3, 195, 1, 4),
    _Rm10010arCntlineDfrmTimCntOverloadPortn_Type()
)
rm10010arCntlineDfrmTimCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arCntlineDfrmTimCntOverloadPortn.setStatus("current")
_Rm10010arCntlocalLineTrscvFecCorrectedErrorCounterTable_Object = MibTable
rm10010arCntlocalLineTrscvFecCorrectedErrorCounterTable = _Rm10010arCntlocalLineTrscvFecCorrectedErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4, 3, 196)
)
if mibBuilder.loadTexts:
    rm10010arCntlocalLineTrscvFecCorrectedErrorCounterTable.setStatus("current")
_Rm10010arCntlocalLineTrscvFecCorrectedErrorCounterEntry_Object = MibTableRow
rm10010arCntlocalLineTrscvFecCorrectedErrorCounterEntry = _Rm10010arCntlocalLineTrscvFecCorrectedErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4, 3, 196, 1)
)
rm10010arCntlocalLineTrscvFecCorrectedErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Rm10010ar-MIB", "rm10010arCntlocalLineTrscvFecCorrectedErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    rm10010arCntlocalLineTrscvFecCorrectedErrorCounterEntry.setStatus("current")


class _Rm10010arCntlocalLineTrscvFecCorrectedErrorCounterIndex_Type(Integer32):
    """Custom type rm10010arCntlocalLineTrscvFecCorrectedErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010arCntlocalLineTrscvFecCorrectedErrorCounterIndex_Type.__name__ = "Integer32"
_Rm10010arCntlocalLineTrscvFecCorrectedErrorCounterIndex_Object = MibTableColumn
rm10010arCntlocalLineTrscvFecCorrectedErrorCounterIndex = _Rm10010arCntlocalLineTrscvFecCorrectedErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4, 3, 196, 1, 1),
    _Rm10010arCntlocalLineTrscvFecCorrectedErrorCounterIndex_Type()
)
rm10010arCntlocalLineTrscvFecCorrectedErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arCntlocalLineTrscvFecCorrectedErrorCounterIndex.setStatus("current")
_Rm10010arCntlocalLineTrscvFecCorrectedErrorCounterValuePortn_Type = Counter64
_Rm10010arCntlocalLineTrscvFecCorrectedErrorCounterValuePortn_Object = MibTableColumn
rm10010arCntlocalLineTrscvFecCorrectedErrorCounterValuePortn = _Rm10010arCntlocalLineTrscvFecCorrectedErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4, 3, 196, 1, 2),
    _Rm10010arCntlocalLineTrscvFecCorrectedErrorCounterValuePortn_Type()
)
rm10010arCntlocalLineTrscvFecCorrectedErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arCntlocalLineTrscvFecCorrectedErrorCounterValuePortn.setStatus("current")
_Rm10010arCntlocalLineTrscvFecCorrectedErrorCounterErrorPortn_Type = EkiOnOff
_Rm10010arCntlocalLineTrscvFecCorrectedErrorCounterErrorPortn_Object = MibTableColumn
rm10010arCntlocalLineTrscvFecCorrectedErrorCounterErrorPortn = _Rm10010arCntlocalLineTrscvFecCorrectedErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4, 3, 196, 1, 3),
    _Rm10010arCntlocalLineTrscvFecCorrectedErrorCounterErrorPortn_Type()
)
rm10010arCntlocalLineTrscvFecCorrectedErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arCntlocalLineTrscvFecCorrectedErrorCounterErrorPortn.setStatus("current")
_Rm10010arCntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn_Type = EkiOnOff
_Rm10010arCntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn_Object = MibTableColumn
rm10010arCntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn = _Rm10010arCntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4, 3, 196, 1, 4),
    _Rm10010arCntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn_Type()
)
rm10010arCntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arCntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn.setStatus("current")
_Rm10010arCntlocalLineTrscvFecUncorrectedErrorCounterTable_Object = MibTable
rm10010arCntlocalLineTrscvFecUncorrectedErrorCounterTable = _Rm10010arCntlocalLineTrscvFecUncorrectedErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4, 3, 197)
)
if mibBuilder.loadTexts:
    rm10010arCntlocalLineTrscvFecUncorrectedErrorCounterTable.setStatus("current")
_Rm10010arCntlocalLineTrscvFecUncorrectedErrorCounterEntry_Object = MibTableRow
rm10010arCntlocalLineTrscvFecUncorrectedErrorCounterEntry = _Rm10010arCntlocalLineTrscvFecUncorrectedErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4, 3, 197, 1)
)
rm10010arCntlocalLineTrscvFecUncorrectedErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Rm10010ar-MIB", "rm10010arCntlocalLineTrscvFecUncorrectedErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    rm10010arCntlocalLineTrscvFecUncorrectedErrorCounterEntry.setStatus("current")


class _Rm10010arCntlocalLineTrscvFecUncorrectedErrorCounterIndex_Type(Integer32):
    """Custom type rm10010arCntlocalLineTrscvFecUncorrectedErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010arCntlocalLineTrscvFecUncorrectedErrorCounterIndex_Type.__name__ = "Integer32"
_Rm10010arCntlocalLineTrscvFecUncorrectedErrorCounterIndex_Object = MibTableColumn
rm10010arCntlocalLineTrscvFecUncorrectedErrorCounterIndex = _Rm10010arCntlocalLineTrscvFecUncorrectedErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4, 3, 197, 1, 1),
    _Rm10010arCntlocalLineTrscvFecUncorrectedErrorCounterIndex_Type()
)
rm10010arCntlocalLineTrscvFecUncorrectedErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arCntlocalLineTrscvFecUncorrectedErrorCounterIndex.setStatus("current")
_Rm10010arCntlocalLineTrscvFecUncorrectedErrorCounterValuePortn_Type = Counter64
_Rm10010arCntlocalLineTrscvFecUncorrectedErrorCounterValuePortn_Object = MibTableColumn
rm10010arCntlocalLineTrscvFecUncorrectedErrorCounterValuePortn = _Rm10010arCntlocalLineTrscvFecUncorrectedErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4, 3, 197, 1, 2),
    _Rm10010arCntlocalLineTrscvFecUncorrectedErrorCounterValuePortn_Type()
)
rm10010arCntlocalLineTrscvFecUncorrectedErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arCntlocalLineTrscvFecUncorrectedErrorCounterValuePortn.setStatus("current")
_Rm10010arCntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn_Type = EkiOnOff
_Rm10010arCntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn_Object = MibTableColumn
rm10010arCntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn = _Rm10010arCntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4, 3, 197, 1, 3),
    _Rm10010arCntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn_Type()
)
rm10010arCntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arCntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn.setStatus("current")
_Rm10010arCntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn_Type = EkiOnOff
_Rm10010arCntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn_Object = MibTableColumn
rm10010arCntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn = _Rm10010arCntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 4, 3, 197, 1, 4),
    _Rm10010arCntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn_Type()
)
rm10010arCntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arCntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn.setStatus("current")
_Rm10010arcontrolsWrite_ObjectIdentity = ObjectIdentity
rm10010arcontrolsWrite = _Rm10010arcontrolsWrite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6)
)
_Rm10010arCtrlOther_ObjectIdentity = ObjectIdentity
rm10010arCtrlOther = _Rm10010arCtrlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 1)
)
_Rm10010arCtrlconfMgnt1_ObjectIdentity = ObjectIdentity
rm10010arCtrlconfMgnt1 = _Rm10010arCtrlconfMgnt1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 1, 1)
)
_Rm10010arCtrlConf1Load1_Type = EkiOnOff
_Rm10010arCtrlConf1Load1_Object = MibScalar
rm10010arCtrlConf1Load1 = _Rm10010arCtrlConf1Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 1, 1, 1),
    _Rm10010arCtrlConf1Load1_Type()
)
rm10010arCtrlConf1Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010arCtrlConf1Load1.setStatus("current")
_Rm10010arCtrlConf2Load1_Type = EkiOnOff
_Rm10010arCtrlConf2Load1_Object = MibScalar
rm10010arCtrlConf2Load1 = _Rm10010arCtrlConf2Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 1, 1, 2),
    _Rm10010arCtrlConf2Load1_Type()
)
rm10010arCtrlConf2Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010arCtrlConf2Load1.setStatus("current")
_Rm10010arCtrlConf2Flash1_Type = EkiOnOff
_Rm10010arCtrlConf2Flash1_Object = MibScalar
rm10010arCtrlConf2Flash1 = _Rm10010arCtrlConf2Flash1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 1, 1, 10),
    _Rm10010arCtrlConf2Flash1_Type()
)
rm10010arCtrlConf2Flash1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010arCtrlConf2Flash1.setStatus("current")
_Rm10010arCtrlConf2Clear1_Type = EkiOnOff
_Rm10010arCtrlConf2Clear1_Object = MibScalar
rm10010arCtrlConf2Clear1 = _Rm10010arCtrlConf2Clear1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 1, 1, 14),
    _Rm10010arCtrlConf2Clear1_Type()
)
rm10010arCtrlConf2Clear1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010arCtrlConf2Clear1.setStatus("current")
_Rm10010arCtrlsynth4_ObjectIdentity = ObjectIdentity
rm10010arCtrlsynth4 = _Rm10010arCtrlsynth4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 1, 4)
)
_Rm10010arCtrlCorrelatOn_Type = EkiOnOff
_Rm10010arCtrlCorrelatOn_Object = MibScalar
rm10010arCtrlCorrelatOn = _Rm10010arCtrlCorrelatOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 1, 4, 1),
    _Rm10010arCtrlCorrelatOn_Type()
)
rm10010arCtrlCorrelatOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010arCtrlCorrelatOn.setStatus("current")
_Rm10010arCtrlCorrelatOff_Type = EkiOnOff
_Rm10010arCtrlCorrelatOff_Object = MibScalar
rm10010arCtrlCorrelatOff = _Rm10010arCtrlCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 1, 4, 2),
    _Rm10010arCtrlCorrelatOff_Type()
)
rm10010arCtrlCorrelatOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010arCtrlCorrelatOff.setStatus("current")
_Rm10010arCtrlswMgnt_ObjectIdentity = ObjectIdentity
rm10010arCtrlswMgnt = _Rm10010arCtrlswMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 1, 5)
)
_Rm10010arCtrlColdReset_Type = EkiOnOff
_Rm10010arCtrlColdReset_Object = MibScalar
rm10010arCtrlColdReset = _Rm10010arCtrlColdReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 1, 5, 2),
    _Rm10010arCtrlColdReset_Type()
)
rm10010arCtrlColdReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010arCtrlColdReset.setStatus("current")
_Rm10010arCtrlWarmReset_Type = EkiOnOff
_Rm10010arCtrlWarmReset_Object = MibScalar
rm10010arCtrlWarmReset = _Rm10010arCtrlWarmReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 1, 5, 3),
    _Rm10010arCtrlWarmReset_Type()
)
rm10010arCtrlWarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010arCtrlWarmReset.setStatus("current")
_Rm10010arCtrlLoadSwBank1_Type = EkiOnOff
_Rm10010arCtrlLoadSwBank1_Object = MibScalar
rm10010arCtrlLoadSwBank1 = _Rm10010arCtrlLoadSwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 1, 5, 5),
    _Rm10010arCtrlLoadSwBank1_Type()
)
rm10010arCtrlLoadSwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010arCtrlLoadSwBank1.setStatus("current")
_Rm10010arCtrlLoadSwBank2_Type = EkiOnOff
_Rm10010arCtrlLoadSwBank2_Object = MibScalar
rm10010arCtrlLoadSwBank2 = _Rm10010arCtrlLoadSwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 1, 5, 6),
    _Rm10010arCtrlLoadSwBank2_Type()
)
rm10010arCtrlLoadSwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010arCtrlLoadSwBank2.setStatus("current")
_Rm10010arCtrlgwMgnt_ObjectIdentity = ObjectIdentity
rm10010arCtrlgwMgnt = _Rm10010arCtrlgwMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 1, 6)
)
_Rm10010arCtrlCurrentGwReset_Type = EkiOnOff
_Rm10010arCtrlCurrentGwReset_Object = MibScalar
rm10010arCtrlCurrentGwReset = _Rm10010arCtrlCurrentGwReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 1, 6, 1),
    _Rm10010arCtrlCurrentGwReset_Type()
)
rm10010arCtrlCurrentGwReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010arCtrlCurrentGwReset.setStatus("current")
_Rm10010arCtrlLoadGwBank1_Type = EkiOnOff
_Rm10010arCtrlLoadGwBank1_Object = MibScalar
rm10010arCtrlLoadGwBank1 = _Rm10010arCtrlLoadGwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 1, 6, 5),
    _Rm10010arCtrlLoadGwBank1_Type()
)
rm10010arCtrlLoadGwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010arCtrlLoadGwBank1.setStatus("current")
_Rm10010arCtrlLoadGwBank2_Type = EkiOnOff
_Rm10010arCtrlLoadGwBank2_Object = MibScalar
rm10010arCtrlLoadGwBank2 = _Rm10010arCtrlLoadGwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 1, 6, 6),
    _Rm10010arCtrlLoadGwBank2_Type()
)
rm10010arCtrlLoadGwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010arCtrlLoadGwBank2.setStatus("current")
_Rm10010arCtrlLoadGwBank3_Type = EkiOnOff
_Rm10010arCtrlLoadGwBank3_Object = MibScalar
rm10010arCtrlLoadGwBank3 = _Rm10010arCtrlLoadGwBank3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 1, 6, 7),
    _Rm10010arCtrlLoadGwBank3_Type()
)
rm10010arCtrlLoadGwBank3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010arCtrlLoadGwBank3.setStatus("current")
_Rm10010arCtrlLoadGwBank4_Type = EkiOnOff
_Rm10010arCtrlLoadGwBank4_Object = MibScalar
rm10010arCtrlLoadGwBank4 = _Rm10010arCtrlLoadGwBank4_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 1, 6, 8),
    _Rm10010arCtrlLoadGwBank4_Type()
)
rm10010arCtrlLoadGwBank4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010arCtrlLoadGwBank4.setStatus("current")
_Rm10010arCtrlledTest_ObjectIdentity = ObjectIdentity
rm10010arCtrlledTest = _Rm10010arCtrlledTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 1, 192)
)
_Rm10010arCtrlGreenLed_Type = EkiOnOff
_Rm10010arCtrlGreenLed_Object = MibScalar
rm10010arCtrlGreenLed = _Rm10010arCtrlGreenLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 1, 192, 1),
    _Rm10010arCtrlGreenLed_Type()
)
rm10010arCtrlGreenLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010arCtrlGreenLed.setStatus("current")
_Rm10010arCtrlRedLed_Type = EkiOnOff
_Rm10010arCtrlRedLed_Object = MibScalar
rm10010arCtrlRedLed = _Rm10010arCtrlRedLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 1, 192, 2),
    _Rm10010arCtrlRedLed_Type()
)
rm10010arCtrlRedLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010arCtrlRedLed.setStatus("current")
_Rm10010arCtrlLedOff_Type = EkiOnOff
_Rm10010arCtrlLedOff_Object = MibScalar
rm10010arCtrlLedOff = _Rm10010arCtrlLedOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 1, 192, 3),
    _Rm10010arCtrlLedOff_Type()
)
rm10010arCtrlLedOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010arCtrlLedOff.setStatus("current")
_Rm10010arCtrlinitSwitchMarvell_ObjectIdentity = ObjectIdentity
rm10010arCtrlinitSwitchMarvell = _Rm10010arCtrlinitSwitchMarvell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 1, 201)
)
_Rm10010arCtrlInitSwitchMarvell_Type = EkiOnOff
_Rm10010arCtrlInitSwitchMarvell_Object = MibScalar
rm10010arCtrlInitSwitchMarvell = _Rm10010arCtrlInitSwitchMarvell_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 1, 201, 1),
    _Rm10010arCtrlInitSwitchMarvell_Type()
)
rm10010arCtrlInitSwitchMarvell.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010arCtrlInitSwitchMarvell.setStatus("current")
_Rm10010arCtrlresetCount_ObjectIdentity = ObjectIdentity
rm10010arCtrlresetCount = _Rm10010arCtrlresetCount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 1, 259)
)
_Rm10010arCtrlResetcount_Type = EkiOnOff
_Rm10010arCtrlResetcount_Object = MibScalar
rm10010arCtrlResetcount = _Rm10010arCtrlResetcount_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 1, 259, 1),
    _Rm10010arCtrlResetcount_Type()
)
rm10010arCtrlResetcount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010arCtrlResetcount.setStatus("current")
_Rm10010arCtrlresetRmon_ObjectIdentity = ObjectIdentity
rm10010arCtrlresetRmon = _Rm10010arCtrlresetRmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 1, 260)
)
_Rm10010arCtrlResetrmon_Type = EkiOnOff
_Rm10010arCtrlResetrmon_Object = MibScalar
rm10010arCtrlResetrmon = _Rm10010arCtrlResetrmon_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 1, 260, 1),
    _Rm10010arCtrlResetrmon_Type()
)
rm10010arCtrlResetrmon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010arCtrlResetrmon.setStatus("current")
_Rm10010arCtrlresetMeasurements_ObjectIdentity = ObjectIdentity
rm10010arCtrlresetMeasurements = _Rm10010arCtrlresetMeasurements_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 1, 261)
)
_Rm10010arCtrlResetmeasurements_Type = EkiOnOff
_Rm10010arCtrlResetmeasurements_Object = MibScalar
rm10010arCtrlResetmeasurements = _Rm10010arCtrlResetmeasurements_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 1, 261, 1),
    _Rm10010arCtrlResetmeasurements_Type()
)
rm10010arCtrlResetmeasurements.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010arCtrlResetmeasurements.setStatus("current")
_Rm10010arCtrlClient_ObjectIdentity = ObjectIdentity
rm10010arCtrlClient = _Rm10010arCtrlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 2)
)
_Rm10010arCtrlaccessLoopTable_Object = MibTable
rm10010arCtrlaccessLoopTable = _Rm10010arCtrlaccessLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 2, 16)
)
if mibBuilder.loadTexts:
    rm10010arCtrlaccessLoopTable.setStatus("current")
_Rm10010arCtrlaccessLoopEntry_Object = MibTableRow
rm10010arCtrlaccessLoopEntry = _Rm10010arCtrlaccessLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 2, 16, 1)
)
rm10010arCtrlaccessLoopEntry.setIndexNames(
    (0, "EKINOPS-Rm10010ar-MIB", "rm10010arCtrlaccessLoopIndex"),
)
if mibBuilder.loadTexts:
    rm10010arCtrlaccessLoopEntry.setStatus("current")


class _Rm10010arCtrlaccessLoopIndex_Type(Integer32):
    """Custom type rm10010arCtrlaccessLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010arCtrlaccessLoopIndex_Type.__name__ = "Integer32"
_Rm10010arCtrlaccessLoopIndex_Object = MibTableColumn
rm10010arCtrlaccessLoopIndex = _Rm10010arCtrlaccessLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 2, 16, 1, 1),
    _Rm10010arCtrlaccessLoopIndex_Type()
)
rm10010arCtrlaccessLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arCtrlaccessLoopIndex.setStatus("current")
_Rm10010arCtrlaccessLoopPortn_Type = EkiState
_Rm10010arCtrlaccessLoopPortn_Object = MibTableColumn
rm10010arCtrlaccessLoopPortn = _Rm10010arCtrlaccessLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 2, 16, 1, 2),
    _Rm10010arCtrlaccessLoopPortn_Type()
)
rm10010arCtrlaccessLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010arCtrlaccessLoopPortn.setStatus("current")
_Rm10010arCtrlclientLoopToLineTable_Object = MibTable
rm10010arCtrlclientLoopToLineTable = _Rm10010arCtrlclientLoopToLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 2, 17)
)
if mibBuilder.loadTexts:
    rm10010arCtrlclientLoopToLineTable.setStatus("current")
_Rm10010arCtrlclientLoopToLineEntry_Object = MibTableRow
rm10010arCtrlclientLoopToLineEntry = _Rm10010arCtrlclientLoopToLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 2, 17, 1)
)
rm10010arCtrlclientLoopToLineEntry.setIndexNames(
    (0, "EKINOPS-Rm10010ar-MIB", "rm10010arCtrlclientLoopToLineIndex"),
)
if mibBuilder.loadTexts:
    rm10010arCtrlclientLoopToLineEntry.setStatus("current")


class _Rm10010arCtrlclientLoopToLineIndex_Type(Integer32):
    """Custom type rm10010arCtrlclientLoopToLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010arCtrlclientLoopToLineIndex_Type.__name__ = "Integer32"
_Rm10010arCtrlclientLoopToLineIndex_Object = MibTableColumn
rm10010arCtrlclientLoopToLineIndex = _Rm10010arCtrlclientLoopToLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 2, 17, 1, 1),
    _Rm10010arCtrlclientLoopToLineIndex_Type()
)
rm10010arCtrlclientLoopToLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arCtrlclientLoopToLineIndex.setStatus("current")
_Rm10010arCtrlclientLoopToLinePortn_Type = EkiState
_Rm10010arCtrlclientLoopToLinePortn_Object = MibTableColumn
rm10010arCtrlclientLoopToLinePortn = _Rm10010arCtrlclientLoopToLinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 2, 17, 1, 2),
    _Rm10010arCtrlclientLoopToLinePortn_Type()
)
rm10010arCtrlclientLoopToLinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010arCtrlclientLoopToLinePortn.setStatus("current")
_Rm10010arCtrlcsfUpInsTable_Object = MibTable
rm10010arCtrlcsfUpInsTable = _Rm10010arCtrlcsfUpInsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 2, 21)
)
if mibBuilder.loadTexts:
    rm10010arCtrlcsfUpInsTable.setStatus("current")
_Rm10010arCtrlcsfUpInsEntry_Object = MibTableRow
rm10010arCtrlcsfUpInsEntry = _Rm10010arCtrlcsfUpInsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 2, 21, 1)
)
rm10010arCtrlcsfUpInsEntry.setIndexNames(
    (0, "EKINOPS-Rm10010ar-MIB", "rm10010arCtrlcsfUpInsIndex"),
)
if mibBuilder.loadTexts:
    rm10010arCtrlcsfUpInsEntry.setStatus("current")


class _Rm10010arCtrlcsfUpInsIndex_Type(Integer32):
    """Custom type rm10010arCtrlcsfUpInsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010arCtrlcsfUpInsIndex_Type.__name__ = "Integer32"
_Rm10010arCtrlcsfUpInsIndex_Object = MibTableColumn
rm10010arCtrlcsfUpInsIndex = _Rm10010arCtrlcsfUpInsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 2, 21, 1, 1),
    _Rm10010arCtrlcsfUpInsIndex_Type()
)
rm10010arCtrlcsfUpInsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arCtrlcsfUpInsIndex.setStatus("current")
_Rm10010arCtrlcsfUpInsPortn_Type = EkiState
_Rm10010arCtrlcsfUpInsPortn_Object = MibTableColumn
rm10010arCtrlcsfUpInsPortn = _Rm10010arCtrlcsfUpInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 2, 21, 1, 2),
    _Rm10010arCtrlcsfUpInsPortn_Type()
)
rm10010arCtrlcsfUpInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010arCtrlcsfUpInsPortn.setStatus("current")
_Rm10010arCtrlcaisDwInsTable_Object = MibTable
rm10010arCtrlcaisDwInsTable = _Rm10010arCtrlcaisDwInsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 2, 22)
)
if mibBuilder.loadTexts:
    rm10010arCtrlcaisDwInsTable.setStatus("current")
_Rm10010arCtrlcaisDwInsEntry_Object = MibTableRow
rm10010arCtrlcaisDwInsEntry = _Rm10010arCtrlcaisDwInsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 2, 22, 1)
)
rm10010arCtrlcaisDwInsEntry.setIndexNames(
    (0, "EKINOPS-Rm10010ar-MIB", "rm10010arCtrlcaisDwInsIndex"),
)
if mibBuilder.loadTexts:
    rm10010arCtrlcaisDwInsEntry.setStatus("current")


class _Rm10010arCtrlcaisDwInsIndex_Type(Integer32):
    """Custom type rm10010arCtrlcaisDwInsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010arCtrlcaisDwInsIndex_Type.__name__ = "Integer32"
_Rm10010arCtrlcaisDwInsIndex_Object = MibTableColumn
rm10010arCtrlcaisDwInsIndex = _Rm10010arCtrlcaisDwInsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 2, 22, 1, 1),
    _Rm10010arCtrlcaisDwInsIndex_Type()
)
rm10010arCtrlcaisDwInsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arCtrlcaisDwInsIndex.setStatus("current")
_Rm10010arCtrlcaisDwInsPortn_Type = EkiState
_Rm10010arCtrlcaisDwInsPortn_Object = MibTableColumn
rm10010arCtrlcaisDwInsPortn = _Rm10010arCtrlcaisDwInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 2, 22, 1, 2),
    _Rm10010arCtrlcaisDwInsPortn_Type()
)
rm10010arCtrlcaisDwInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010arCtrlcaisDwInsPortn.setStatus("current")
_Rm10010arCtrlLine_ObjectIdentity = ObjectIdentity
rm10010arCtrlLine = _Rm10010arCtrlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 3)
)
_Rm10010arCtrlcommAccessLoopTable_Object = MibTable
rm10010arCtrlcommAccessLoopTable = _Rm10010arCtrlcommAccessLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 3, 64)
)
if mibBuilder.loadTexts:
    rm10010arCtrlcommAccessLoopTable.setStatus("current")
_Rm10010arCtrlcommAccessLoopEntry_Object = MibTableRow
rm10010arCtrlcommAccessLoopEntry = _Rm10010arCtrlcommAccessLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 3, 64, 1)
)
rm10010arCtrlcommAccessLoopEntry.setIndexNames(
    (0, "EKINOPS-Rm10010ar-MIB", "rm10010arCtrlcommAccessLoopIndex"),
)
if mibBuilder.loadTexts:
    rm10010arCtrlcommAccessLoopEntry.setStatus("current")


class _Rm10010arCtrlcommAccessLoopIndex_Type(Integer32):
    """Custom type rm10010arCtrlcommAccessLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010arCtrlcommAccessLoopIndex_Type.__name__ = "Integer32"
_Rm10010arCtrlcommAccessLoopIndex_Object = MibTableColumn
rm10010arCtrlcommAccessLoopIndex = _Rm10010arCtrlcommAccessLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 3, 64, 1, 1),
    _Rm10010arCtrlcommAccessLoopIndex_Type()
)
rm10010arCtrlcommAccessLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arCtrlcommAccessLoopIndex.setStatus("current")
_Rm10010arCtrlcommAccessLoopPortn_Type = EkiState
_Rm10010arCtrlcommAccessLoopPortn_Object = MibTableColumn
rm10010arCtrlcommAccessLoopPortn = _Rm10010arCtrlcommAccessLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 3, 64, 1, 2),
    _Rm10010arCtrlcommAccessLoopPortn_Type()
)
rm10010arCtrlcommAccessLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010arCtrlcommAccessLoopPortn.setStatus("current")
_Rm10010arCtrllineLoopTable_Object = MibTable
rm10010arCtrllineLoopTable = _Rm10010arCtrllineLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 3, 66)
)
if mibBuilder.loadTexts:
    rm10010arCtrllineLoopTable.setStatus("current")
_Rm10010arCtrllineLoopEntry_Object = MibTableRow
rm10010arCtrllineLoopEntry = _Rm10010arCtrllineLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 3, 66, 1)
)
rm10010arCtrllineLoopEntry.setIndexNames(
    (0, "EKINOPS-Rm10010ar-MIB", "rm10010arCtrllineLoopIndex"),
)
if mibBuilder.loadTexts:
    rm10010arCtrllineLoopEntry.setStatus("current")


class _Rm10010arCtrllineLoopIndex_Type(Integer32):
    """Custom type rm10010arCtrllineLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010arCtrllineLoopIndex_Type.__name__ = "Integer32"
_Rm10010arCtrllineLoopIndex_Object = MibTableColumn
rm10010arCtrllineLoopIndex = _Rm10010arCtrllineLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 3, 66, 1, 1),
    _Rm10010arCtrllineLoopIndex_Type()
)
rm10010arCtrllineLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arCtrllineLoopIndex.setStatus("current")
_Rm10010arCtrllineLoopPortn_Type = EkiState
_Rm10010arCtrllineLoopPortn_Object = MibTableColumn
rm10010arCtrllineLoopPortn = _Rm10010arCtrllineLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 3, 66, 1, 2),
    _Rm10010arCtrllineLoopPortn_Type()
)
rm10010arCtrllineLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010arCtrllineLoopPortn.setStatus("current")
_Rm10010arCtrlfecDisableTable_Object = MibTable
rm10010arCtrlfecDisableTable = _Rm10010arCtrlfecDisableTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 3, 69)
)
if mibBuilder.loadTexts:
    rm10010arCtrlfecDisableTable.setStatus("current")
_Rm10010arCtrlfecDisableEntry_Object = MibTableRow
rm10010arCtrlfecDisableEntry = _Rm10010arCtrlfecDisableEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 3, 69, 1)
)
rm10010arCtrlfecDisableEntry.setIndexNames(
    (0, "EKINOPS-Rm10010ar-MIB", "rm10010arCtrlfecDisableIndex"),
)
if mibBuilder.loadTexts:
    rm10010arCtrlfecDisableEntry.setStatus("current")


class _Rm10010arCtrlfecDisableIndex_Type(Integer32):
    """Custom type rm10010arCtrlfecDisableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010arCtrlfecDisableIndex_Type.__name__ = "Integer32"
_Rm10010arCtrlfecDisableIndex_Object = MibTableColumn
rm10010arCtrlfecDisableIndex = _Rm10010arCtrlfecDisableIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 3, 69, 1, 1),
    _Rm10010arCtrlfecDisableIndex_Type()
)
rm10010arCtrlfecDisableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arCtrlfecDisableIndex.setStatus("current")
_Rm10010arCtrlfecDisablePortn_Type = EkiState
_Rm10010arCtrlfecDisablePortn_Object = MibTableColumn
rm10010arCtrlfecDisablePortn = _Rm10010arCtrlfecDisablePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 3, 69, 1, 2),
    _Rm10010arCtrlfecDisablePortn_Type()
)
rm10010arCtrlfecDisablePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010arCtrlfecDisablePortn.setStatus("current")
_Rm10010arCtrlmsaLineLoopTable_Object = MibTable
rm10010arCtrlmsaLineLoopTable = _Rm10010arCtrlmsaLineLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 3, 209)
)
if mibBuilder.loadTexts:
    rm10010arCtrlmsaLineLoopTable.setStatus("current")
_Rm10010arCtrlmsaLineLoopEntry_Object = MibTableRow
rm10010arCtrlmsaLineLoopEntry = _Rm10010arCtrlmsaLineLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 3, 209, 1)
)
rm10010arCtrlmsaLineLoopEntry.setIndexNames(
    (0, "EKINOPS-Rm10010ar-MIB", "rm10010arCtrlmsaLineLoopIndex"),
)
if mibBuilder.loadTexts:
    rm10010arCtrlmsaLineLoopEntry.setStatus("current")


class _Rm10010arCtrlmsaLineLoopIndex_Type(Integer32):
    """Custom type rm10010arCtrlmsaLineLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010arCtrlmsaLineLoopIndex_Type.__name__ = "Integer32"
_Rm10010arCtrlmsaLineLoopIndex_Object = MibTableColumn
rm10010arCtrlmsaLineLoopIndex = _Rm10010arCtrlmsaLineLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 3, 209, 1, 1),
    _Rm10010arCtrlmsaLineLoopIndex_Type()
)
rm10010arCtrlmsaLineLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arCtrlmsaLineLoopIndex.setStatus("current")
_Rm10010arCtrlmsaLineLoopPortn_Type = EkiState
_Rm10010arCtrlmsaLineLoopPortn_Object = MibTableColumn
rm10010arCtrlmsaLineLoopPortn = _Rm10010arCtrlmsaLineLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 3, 209, 1, 2),
    _Rm10010arCtrlmsaLineLoopPortn_Type()
)
rm10010arCtrlmsaLineLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010arCtrlmsaLineLoopPortn.setStatus("current")
_Rm10010arCtrlmsaTxResetTable_Object = MibTable
rm10010arCtrlmsaTxResetTable = _Rm10010arCtrlmsaTxResetTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 3, 210)
)
if mibBuilder.loadTexts:
    rm10010arCtrlmsaTxResetTable.setStatus("current")
_Rm10010arCtrlmsaTxResetEntry_Object = MibTableRow
rm10010arCtrlmsaTxResetEntry = _Rm10010arCtrlmsaTxResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 3, 210, 1)
)
rm10010arCtrlmsaTxResetEntry.setIndexNames(
    (0, "EKINOPS-Rm10010ar-MIB", "rm10010arCtrlmsaTxResetIndex"),
)
if mibBuilder.loadTexts:
    rm10010arCtrlmsaTxResetEntry.setStatus("current")


class _Rm10010arCtrlmsaTxResetIndex_Type(Integer32):
    """Custom type rm10010arCtrlmsaTxResetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010arCtrlmsaTxResetIndex_Type.__name__ = "Integer32"
_Rm10010arCtrlmsaTxResetIndex_Object = MibTableColumn
rm10010arCtrlmsaTxResetIndex = _Rm10010arCtrlmsaTxResetIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 3, 210, 1, 1),
    _Rm10010arCtrlmsaTxResetIndex_Type()
)
rm10010arCtrlmsaTxResetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arCtrlmsaTxResetIndex.setStatus("current")
_Rm10010arCtrlmsaTxResetPortn_Type = EkiState
_Rm10010arCtrlmsaTxResetPortn_Object = MibTableColumn
rm10010arCtrlmsaTxResetPortn = _Rm10010arCtrlmsaTxResetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 3, 210, 1, 2),
    _Rm10010arCtrlmsaTxResetPortn_Type()
)
rm10010arCtrlmsaTxResetPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010arCtrlmsaTxResetPortn.setStatus("current")
_Rm10010arCtrlmsaRxResetTable_Object = MibTable
rm10010arCtrlmsaRxResetTable = _Rm10010arCtrlmsaRxResetTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 3, 211)
)
if mibBuilder.loadTexts:
    rm10010arCtrlmsaRxResetTable.setStatus("current")
_Rm10010arCtrlmsaRxResetEntry_Object = MibTableRow
rm10010arCtrlmsaRxResetEntry = _Rm10010arCtrlmsaRxResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 3, 211, 1)
)
rm10010arCtrlmsaRxResetEntry.setIndexNames(
    (0, "EKINOPS-Rm10010ar-MIB", "rm10010arCtrlmsaRxResetIndex"),
)
if mibBuilder.loadTexts:
    rm10010arCtrlmsaRxResetEntry.setStatus("current")


class _Rm10010arCtrlmsaRxResetIndex_Type(Integer32):
    """Custom type rm10010arCtrlmsaRxResetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010arCtrlmsaRxResetIndex_Type.__name__ = "Integer32"
_Rm10010arCtrlmsaRxResetIndex_Object = MibTableColumn
rm10010arCtrlmsaRxResetIndex = _Rm10010arCtrlmsaRxResetIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 3, 211, 1, 1),
    _Rm10010arCtrlmsaRxResetIndex_Type()
)
rm10010arCtrlmsaRxResetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arCtrlmsaRxResetIndex.setStatus("current")
_Rm10010arCtrlmsaRxResetPortn_Type = EkiState
_Rm10010arCtrlmsaRxResetPortn_Object = MibTableColumn
rm10010arCtrlmsaRxResetPortn = _Rm10010arCtrlmsaRxResetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 3, 211, 1, 2),
    _Rm10010arCtrlmsaRxResetPortn_Type()
)
rm10010arCtrlmsaRxResetPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010arCtrlmsaRxResetPortn.setStatus("current")
_Rm10010arCtrlmsaShutdownTable_Object = MibTable
rm10010arCtrlmsaShutdownTable = _Rm10010arCtrlmsaShutdownTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 3, 212)
)
if mibBuilder.loadTexts:
    rm10010arCtrlmsaShutdownTable.setStatus("current")
_Rm10010arCtrlmsaShutdownEntry_Object = MibTableRow
rm10010arCtrlmsaShutdownEntry = _Rm10010arCtrlmsaShutdownEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 3, 212, 1)
)
rm10010arCtrlmsaShutdownEntry.setIndexNames(
    (0, "EKINOPS-Rm10010ar-MIB", "rm10010arCtrlmsaShutdownIndex"),
)
if mibBuilder.loadTexts:
    rm10010arCtrlmsaShutdownEntry.setStatus("current")


class _Rm10010arCtrlmsaShutdownIndex_Type(Integer32):
    """Custom type rm10010arCtrlmsaShutdownIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010arCtrlmsaShutdownIndex_Type.__name__ = "Integer32"
_Rm10010arCtrlmsaShutdownIndex_Object = MibTableColumn
rm10010arCtrlmsaShutdownIndex = _Rm10010arCtrlmsaShutdownIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 3, 212, 1, 1),
    _Rm10010arCtrlmsaShutdownIndex_Type()
)
rm10010arCtrlmsaShutdownIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arCtrlmsaShutdownIndex.setStatus("current")
_Rm10010arCtrlmsaShutdownPortn_Type = EkiState
_Rm10010arCtrlmsaShutdownPortn_Object = MibTableColumn
rm10010arCtrlmsaShutdownPortn = _Rm10010arCtrlmsaShutdownPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 6, 3, 212, 1, 2),
    _Rm10010arCtrlmsaShutdownPortn_Type()
)
rm10010arCtrlmsaShutdownPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010arCtrlmsaShutdownPortn.setStatus("current")
_Rm10010arri_ObjectIdentity = ObjectIdentity
rm10010arri = _Rm10010arri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 7)
)
_Rm10010arriTable_ObjectIdentity = ObjectIdentity
rm10010arriTable = _Rm10010arriTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 7, 1)
)
_Rm10010arRinvSfpTable_Object = MibTable
rm10010arRinvSfpTable = _Rm10010arRinvSfpTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 7, 1, 1)
)
if mibBuilder.loadTexts:
    rm10010arRinvSfpTable.setStatus("current")
_Rm10010arRinvSfpEntry_Object = MibTableRow
rm10010arRinvSfpEntry = _Rm10010arRinvSfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 7, 1, 1, 1)
)
rm10010arRinvSfpEntry.setIndexNames(
    (0, "EKINOPS-Rm10010ar-MIB", "rm10010arRinvSfpIndex"),
)
if mibBuilder.loadTexts:
    rm10010arRinvSfpEntry.setStatus("current")


class _Rm10010arRinvSfpIndex_Type(Integer32):
    """Custom type rm10010arRinvSfpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Rm10010arRinvSfpIndex_Type.__name__ = "Integer32"
_Rm10010arRinvSfpIndex_Object = MibTableColumn
rm10010arRinvSfpIndex = _Rm10010arRinvSfpIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 7, 1, 1, 1, 1),
    _Rm10010arRinvSfpIndex_Type()
)
rm10010arRinvSfpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arRinvSfpIndex.setStatus("current")
_Rm10010arRinvsfp_Type = DisplayString
_Rm10010arRinvsfp_Object = MibTableColumn
rm10010arRinvsfp = _Rm10010arRinvsfp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 7, 1, 1, 1, 2),
    _Rm10010arRinvsfp_Type()
)
rm10010arRinvsfp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arRinvsfp.setStatus("current")
_Rm10010arRinvLineTable_Object = MibTable
rm10010arRinvLineTable = _Rm10010arRinvLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 7, 1, 2)
)
if mibBuilder.loadTexts:
    rm10010arRinvLineTable.setStatus("current")
_Rm10010arRinvLineEntry_Object = MibTableRow
rm10010arRinvLineEntry = _Rm10010arRinvLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 7, 1, 2, 1)
)
rm10010arRinvLineEntry.setIndexNames(
    (0, "EKINOPS-Rm10010ar-MIB", "rm10010arRinvLineIndex"),
)
if mibBuilder.loadTexts:
    rm10010arRinvLineEntry.setStatus("current")


class _Rm10010arRinvLineIndex_Type(Integer32):
    """Custom type rm10010arRinvLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Rm10010arRinvLineIndex_Type.__name__ = "Integer32"
_Rm10010arRinvLineIndex_Object = MibTableColumn
rm10010arRinvLineIndex = _Rm10010arRinvLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 7, 1, 2, 1, 1),
    _Rm10010arRinvLineIndex_Type()
)
rm10010arRinvLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arRinvLineIndex.setStatus("current")
_Rm10010arRinvxfpLine_Type = DisplayString
_Rm10010arRinvxfpLine_Object = MibTableColumn
rm10010arRinvxfpLine = _Rm10010arRinvxfpLine_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 7, 1, 2, 1, 2),
    _Rm10010arRinvxfpLine_Type()
)
rm10010arRinvxfpLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arRinvxfpLine.setStatus("current")
_Rm10010arRinvReloadInventory_Type = EkiOnOff
_Rm10010arRinvReloadInventory_Object = MibScalar
rm10010arRinvReloadInventory = _Rm10010arRinvReloadInventory_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 7, 2),
    _Rm10010arRinvReloadInventory_Type()
)
rm10010arRinvReloadInventory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010arRinvReloadInventory.setStatus("current")
_Rm10010arRinvHwPlatform_Type = DisplayString
_Rm10010arRinvHwPlatform_Object = MibScalar
rm10010arRinvHwPlatform = _Rm10010arRinvHwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 7, 3),
    _Rm10010arRinvHwPlatform_Type()
)
rm10010arRinvHwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arRinvHwPlatform.setStatus("current")
_Rm10010arRinvModulePlatform_Type = DisplayString
_Rm10010arRinvModulePlatform_Object = MibScalar
rm10010arRinvModulePlatform = _Rm10010arRinvModulePlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 7, 4),
    _Rm10010arRinvModulePlatform_Type()
)
rm10010arRinvModulePlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arRinvModulePlatform.setStatus("current")
_Rm10010arRinvSwPlatform_Type = DisplayString
_Rm10010arRinvSwPlatform_Object = MibScalar
rm10010arRinvSwPlatform = _Rm10010arRinvSwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 7, 5),
    _Rm10010arRinvSwPlatform_Type()
)
rm10010arRinvSwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arRinvSwPlatform.setStatus("current")
_Rm10010arRinvGwPlatform_Type = DisplayString
_Rm10010arRinvGwPlatform_Object = MibScalar
rm10010arRinvGwPlatform = _Rm10010arRinvGwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 7, 6),
    _Rm10010arRinvGwPlatform_Type()
)
rm10010arRinvGwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arRinvGwPlatform.setStatus("current")
_Rm10010ardownload_ObjectIdentity = ObjectIdentity
rm10010ardownload = _Rm10010ardownload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 8)
)
_Rm10010arDwlOther_ObjectIdentity = ObjectIdentity
rm10010arDwlOther = _Rm10010arDwlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 8, 1)
)
_Rm10010arDwlrestartProcess_ObjectIdentity = ObjectIdentity
rm10010arDwlrestartProcess = _Rm10010arDwlrestartProcess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 8, 1, 0)
)
_Rm10010arDwlWarmRestartProcessed_Type = EkiOnOff
_Rm10010arDwlWarmRestartProcessed_Object = MibScalar
rm10010arDwlWarmRestartProcessed = _Rm10010arDwlWarmRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 8, 1, 0, 1),
    _Rm10010arDwlWarmRestartProcessed_Type()
)
rm10010arDwlWarmRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arDwlWarmRestartProcessed.setStatus("current")
_Rm10010arDwlColdRestartProcessed_Type = EkiOnOff
_Rm10010arDwlColdRestartProcessed_Object = MibScalar
rm10010arDwlColdRestartProcessed = _Rm10010arDwlColdRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 8, 1, 0, 2),
    _Rm10010arDwlColdRestartProcessed_Type()
)
rm10010arDwlColdRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arDwlColdRestartProcessed.setStatus("current")
_Rm10010arDwlswBanksUsed_ObjectIdentity = ObjectIdentity
rm10010arDwlswBanksUsed = _Rm10010arDwlswBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 8, 1, 1)
)
_Rm10010arDwlSwBank1Used_Type = EkiOnOff
_Rm10010arDwlSwBank1Used_Object = MibScalar
rm10010arDwlSwBank1Used = _Rm10010arDwlSwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 8, 1, 1, 1),
    _Rm10010arDwlSwBank1Used_Type()
)
rm10010arDwlSwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arDwlSwBank1Used.setStatus("current")
_Rm10010arDwlSwBank2Used_Type = EkiOnOff
_Rm10010arDwlSwBank2Used_Object = MibScalar
rm10010arDwlSwBank2Used = _Rm10010arDwlSwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 8, 1, 1, 2),
    _Rm10010arDwlSwBank2Used_Type()
)
rm10010arDwlSwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arDwlSwBank2Used.setStatus("current")
_Rm10010arDwlSwBank1Notempty_Type = EkiOnOff
_Rm10010arDwlSwBank1Notempty_Object = MibScalar
rm10010arDwlSwBank1Notempty = _Rm10010arDwlSwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 8, 1, 1, 5),
    _Rm10010arDwlSwBank1Notempty_Type()
)
rm10010arDwlSwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arDwlSwBank1Notempty.setStatus("current")
_Rm10010arDwlSwBank2Notempty_Type = EkiOnOff
_Rm10010arDwlSwBank2Notempty_Object = MibScalar
rm10010arDwlSwBank2Notempty = _Rm10010arDwlSwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 8, 1, 1, 6),
    _Rm10010arDwlSwBank2Notempty_Type()
)
rm10010arDwlSwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arDwlSwBank2Notempty.setStatus("current")
_Rm10010arDwlgwBanksUsed_ObjectIdentity = ObjectIdentity
rm10010arDwlgwBanksUsed = _Rm10010arDwlgwBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 8, 1, 2)
)
_Rm10010arDwlGwBank1Used_Type = EkiOnOff
_Rm10010arDwlGwBank1Used_Object = MibScalar
rm10010arDwlGwBank1Used = _Rm10010arDwlGwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 8, 1, 2, 1),
    _Rm10010arDwlGwBank1Used_Type()
)
rm10010arDwlGwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arDwlGwBank1Used.setStatus("current")
_Rm10010arDwlGwBank2Used_Type = EkiOnOff
_Rm10010arDwlGwBank2Used_Object = MibScalar
rm10010arDwlGwBank2Used = _Rm10010arDwlGwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 8, 1, 2, 2),
    _Rm10010arDwlGwBank2Used_Type()
)
rm10010arDwlGwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arDwlGwBank2Used.setStatus("current")
_Rm10010arDwlGwBank3Used_Type = EkiOnOff
_Rm10010arDwlGwBank3Used_Object = MibScalar
rm10010arDwlGwBank3Used = _Rm10010arDwlGwBank3Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 8, 1, 2, 3),
    _Rm10010arDwlGwBank3Used_Type()
)
rm10010arDwlGwBank3Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arDwlGwBank3Used.setStatus("current")
_Rm10010arDwlGwBank4Used_Type = EkiOnOff
_Rm10010arDwlGwBank4Used_Object = MibScalar
rm10010arDwlGwBank4Used = _Rm10010arDwlGwBank4Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 8, 1, 2, 4),
    _Rm10010arDwlGwBank4Used_Type()
)
rm10010arDwlGwBank4Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arDwlGwBank4Used.setStatus("current")
_Rm10010arDwlGwBank1Notempty_Type = EkiOnOff
_Rm10010arDwlGwBank1Notempty_Object = MibScalar
rm10010arDwlGwBank1Notempty = _Rm10010arDwlGwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 8, 1, 2, 5),
    _Rm10010arDwlGwBank1Notempty_Type()
)
rm10010arDwlGwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arDwlGwBank1Notempty.setStatus("current")
_Rm10010arDwlGwBank2Notempty_Type = EkiOnOff
_Rm10010arDwlGwBank2Notempty_Object = MibScalar
rm10010arDwlGwBank2Notempty = _Rm10010arDwlGwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 8, 1, 2, 6),
    _Rm10010arDwlGwBank2Notempty_Type()
)
rm10010arDwlGwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arDwlGwBank2Notempty.setStatus("current")
_Rm10010arDwlGwBank3Notempty_Type = EkiOnOff
_Rm10010arDwlGwBank3Notempty_Object = MibScalar
rm10010arDwlGwBank3Notempty = _Rm10010arDwlGwBank3Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 8, 1, 2, 7),
    _Rm10010arDwlGwBank3Notempty_Type()
)
rm10010arDwlGwBank3Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arDwlGwBank3Notempty.setStatus("current")
_Rm10010arDwlGwBank4Notempty_Type = EkiOnOff
_Rm10010arDwlGwBank4Notempty_Object = MibScalar
rm10010arDwlGwBank4Notempty = _Rm10010arDwlGwBank4Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 8, 1, 2, 8),
    _Rm10010arDwlGwBank4Notempty_Type()
)
rm10010arDwlGwBank4Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arDwlGwBank4Notempty.setStatus("current")
_Rm10010arDwlClient_ObjectIdentity = ObjectIdentity
rm10010arDwlClient = _Rm10010arDwlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 8, 2)
)
_Rm10010arDwlLine_ObjectIdentity = ObjectIdentity
rm10010arDwlLine = _Rm10010arDwlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 8, 3)
)
_Rm10010arConfig_ObjectIdentity = ObjectIdentity
rm10010arConfig = _Rm10010arConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 9)
)
_Rm10010arCfgAccessCAisCsf_ObjectIdentity = ObjectIdentity
rm10010arCfgAccessCAisCsf = _Rm10010arCfgAccessCAisCsf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 9, 1)
)
_Rm10010arCfgClientcaiscsfTable_Object = MibTable
rm10010arCfgClientcaiscsfTable = _Rm10010arCfgClientcaiscsfTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 9, 1, 1)
)
if mibBuilder.loadTexts:
    rm10010arCfgClientcaiscsfTable.setStatus("current")
_Rm10010arCfgClientcaiscsfEntry_Object = MibTableRow
rm10010arCfgClientcaiscsfEntry = _Rm10010arCfgClientcaiscsfEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 9, 1, 1, 1)
)
rm10010arCfgClientcaiscsfEntry.setIndexNames(
    (0, "EKINOPS-Rm10010ar-MIB", "rm10010arCfgClientcaiscsfIndex"),
)
if mibBuilder.loadTexts:
    rm10010arCfgClientcaiscsfEntry.setStatus("current")


class _Rm10010arCfgClientcaiscsfIndex_Type(Integer32):
    """Custom type rm10010arCfgClientcaiscsfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010arCfgClientcaiscsfIndex_Type.__name__ = "Integer32"
_Rm10010arCfgClientcaiscsfIndex_Object = MibTableColumn
rm10010arCfgClientcaiscsfIndex = _Rm10010arCfgClientcaiscsfIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 9, 1, 1, 1, 1),
    _Rm10010arCfgClientcaiscsfIndex_Type()
)
rm10010arCfgClientcaiscsfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arCfgClientcaiscsfIndex.setStatus("current")


class _Rm10010arCfgReservePortn_Type(Unsigned32):
    """Custom type rm10010arCfgReservePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010arCfgReservePortn_Type.__name__ = "Unsigned32"
_Rm10010arCfgReservePortn_Object = MibTableColumn
rm10010arCfgReservePortn = _Rm10010arCfgReservePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 9, 1, 1, 1, 3),
    _Rm10010arCfgReservePortn_Type()
)
rm10010arCfgReservePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010arCfgReservePortn.setStatus("current")
_Rm10010arCfgStartup_ObjectIdentity = ObjectIdentity
rm10010arCfgStartup = _Rm10010arCfgStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 9, 2)
)
_Rm10010arCfgClientStartupTable_Object = MibTable
rm10010arCfgClientStartupTable = _Rm10010arCfgClientStartupTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 9, 2, 1)
)
if mibBuilder.loadTexts:
    rm10010arCfgClientStartupTable.setStatus("current")
_Rm10010arCfgClientStartupEntry_Object = MibTableRow
rm10010arCfgClientStartupEntry = _Rm10010arCfgClientStartupEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 9, 2, 1, 1)
)
rm10010arCfgClientStartupEntry.setIndexNames(
    (0, "EKINOPS-Rm10010ar-MIB", "rm10010arCfgClientStartupIndex"),
)
if mibBuilder.loadTexts:
    rm10010arCfgClientStartupEntry.setStatus("current")


class _Rm10010arCfgClientStartupIndex_Type(Integer32):
    """Custom type rm10010arCfgClientStartupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010arCfgClientStartupIndex_Type.__name__ = "Integer32"
_Rm10010arCfgClientStartupIndex_Object = MibTableColumn
rm10010arCfgClientStartupIndex = _Rm10010arCfgClientStartupIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 9, 2, 1, 1, 1),
    _Rm10010arCfgClientStartupIndex_Type()
)
rm10010arCfgClientStartupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arCfgClientStartupIndex.setStatus("current")


class _Rm10010arCfgSystConfPortPortn_Type(Unsigned32):
    """Custom type rm10010arCfgSystConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010arCfgSystConfPortPortn_Type.__name__ = "Unsigned32"
_Rm10010arCfgSystConfPortPortn_Object = MibTableColumn
rm10010arCfgSystConfPortPortn = _Rm10010arCfgSystConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 9, 2, 1, 1, 3),
    _Rm10010arCfgSystConfPortPortn_Type()
)
rm10010arCfgSystConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010arCfgSystConfPortPortn.setStatus("current")


class _Rm10010arCfgNetConfPortPortn_Type(Unsigned32):
    """Custom type rm10010arCfgNetConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010arCfgNetConfPortPortn_Type.__name__ = "Unsigned32"
_Rm10010arCfgNetConfPortPortn_Object = MibTableColumn
rm10010arCfgNetConfPortPortn = _Rm10010arCfgNetConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 9, 2, 1, 1, 4),
    _Rm10010arCfgNetConfPortPortn_Type()
)
rm10010arCfgNetConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010arCfgNetConfPortPortn.setStatus("current")


class _Rm10010arCfgOptionsPortPortn_Type(Unsigned32):
    """Custom type rm10010arCfgOptionsPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010arCfgOptionsPortPortn_Type.__name__ = "Unsigned32"
_Rm10010arCfgOptionsPortPortn_Object = MibTableColumn
rm10010arCfgOptionsPortPortn = _Rm10010arCfgOptionsPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 9, 2, 1, 1, 14),
    _Rm10010arCfgOptionsPortPortn_Type()
)
rm10010arCfgOptionsPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010arCfgOptionsPortPortn.setStatus("current")
_Rm10010arCfgLineStartupTable_Object = MibTable
rm10010arCfgLineStartupTable = _Rm10010arCfgLineStartupTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 9, 2, 2)
)
if mibBuilder.loadTexts:
    rm10010arCfgLineStartupTable.setStatus("current")
_Rm10010arCfgLineStartupEntry_Object = MibTableRow
rm10010arCfgLineStartupEntry = _Rm10010arCfgLineStartupEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 9, 2, 2, 1)
)
rm10010arCfgLineStartupEntry.setIndexNames(
    (0, "EKINOPS-Rm10010ar-MIB", "rm10010arCfgLineStartupIndex"),
)
if mibBuilder.loadTexts:
    rm10010arCfgLineStartupEntry.setStatus("current")


class _Rm10010arCfgLineStartupIndex_Type(Integer32):
    """Custom type rm10010arCfgLineStartupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010arCfgLineStartupIndex_Type.__name__ = "Integer32"
_Rm10010arCfgLineStartupIndex_Object = MibTableColumn
rm10010arCfgLineStartupIndex = _Rm10010arCfgLineStartupIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 9, 2, 2, 1, 1),
    _Rm10010arCfgLineStartupIndex_Type()
)
rm10010arCfgLineStartupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arCfgLineStartupIndex.setStatus("current")


class _Rm10010arCfgSystConfLinePortn_Type(Unsigned32):
    """Custom type rm10010arCfgSystConfLinePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010arCfgSystConfLinePortn_Type.__name__ = "Unsigned32"
_Rm10010arCfgSystConfLinePortn_Object = MibTableColumn
rm10010arCfgSystConfLinePortn = _Rm10010arCfgSystConfLinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 9, 2, 2, 1, 3),
    _Rm10010arCfgSystConfLinePortn_Type()
)
rm10010arCfgSystConfLinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010arCfgSystConfLinePortn.setStatus("current")


class _Rm10010arCfgOptionsLinePortn_Type(Unsigned32):
    """Custom type rm10010arCfgOptionsLinePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010arCfgOptionsLinePortn_Type.__name__ = "Unsigned32"
_Rm10010arCfgOptionsLinePortn_Object = MibTableColumn
rm10010arCfgOptionsLinePortn = _Rm10010arCfgOptionsLinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 9, 2, 2, 1, 14),
    _Rm10010arCfgOptionsLinePortn_Type()
)
rm10010arCfgOptionsLinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010arCfgOptionsLinePortn.setStatus("current")
_Rm10010arCfgXfpTable_Object = MibTable
rm10010arCfgXfpTable = _Rm10010arCfgXfpTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 9, 2, 3)
)
if mibBuilder.loadTexts:
    rm10010arCfgXfpTable.setStatus("current")
_Rm10010arCfgXfpEntry_Object = MibTableRow
rm10010arCfgXfpEntry = _Rm10010arCfgXfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 9, 2, 3, 1)
)
rm10010arCfgXfpEntry.setIndexNames(
    (0, "EKINOPS-Rm10010ar-MIB", "rm10010arCfgXfpIndex"),
)
if mibBuilder.loadTexts:
    rm10010arCfgXfpEntry.setStatus("current")


class _Rm10010arCfgXfpIndex_Type(Integer32):
    """Custom type rm10010arCfgXfpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010arCfgXfpIndex_Type.__name__ = "Integer32"
_Rm10010arCfgXfpIndex_Object = MibTableColumn
rm10010arCfgXfpIndex = _Rm10010arCfgXfpIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 9, 2, 3, 1, 1),
    _Rm10010arCfgXfpIndex_Type()
)
rm10010arCfgXfpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arCfgXfpIndex.setStatus("current")


class _Rm10010arCfgSystConfMsaLinePortn_Type(Unsigned32):
    """Custom type rm10010arCfgSystConfMsaLinePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010arCfgSystConfMsaLinePortn_Type.__name__ = "Unsigned32"
_Rm10010arCfgSystConfMsaLinePortn_Object = MibTableColumn
rm10010arCfgSystConfMsaLinePortn = _Rm10010arCfgSystConfMsaLinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 9, 2, 3, 1, 3),
    _Rm10010arCfgSystConfMsaLinePortn_Type()
)
rm10010arCfgSystConfMsaLinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010arCfgSystConfMsaLinePortn.setStatus("current")
_Rm10010arCfgLabels_ObjectIdentity = ObjectIdentity
rm10010arCfgLabels = _Rm10010arCfgLabels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 9, 3)
)
_Rm10010arCfgLabelclientTable_Object = MibTable
rm10010arCfgLabelclientTable = _Rm10010arCfgLabelclientTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 9, 3, 1)
)
if mibBuilder.loadTexts:
    rm10010arCfgLabelclientTable.setStatus("current")
_Rm10010arCfgLabelclientEntry_Object = MibTableRow
rm10010arCfgLabelclientEntry = _Rm10010arCfgLabelclientEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 9, 3, 1, 1)
)
rm10010arCfgLabelclientEntry.setIndexNames(
    (0, "EKINOPS-Rm10010ar-MIB", "rm10010arCfgLabelclientIndex"),
)
if mibBuilder.loadTexts:
    rm10010arCfgLabelclientEntry.setStatus("current")


class _Rm10010arCfgLabelclientIndex_Type(Integer32):
    """Custom type rm10010arCfgLabelclientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010arCfgLabelclientIndex_Type.__name__ = "Integer32"
_Rm10010arCfgLabelclientIndex_Object = MibTableColumn
rm10010arCfgLabelclientIndex = _Rm10010arCfgLabelclientIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 9, 3, 1, 1, 1),
    _Rm10010arCfgLabelclientIndex_Type()
)
rm10010arCfgLabelclientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arCfgLabelclientIndex.setStatus("current")


class _Rm10010arCfgLabelclientPortn_Type(DisplayString):
    """Custom type rm10010arCfgLabelclientPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Rm10010arCfgLabelclientPortn_Type.__name__ = "DisplayString"
_Rm10010arCfgLabelclientPortn_Object = MibTableColumn
rm10010arCfgLabelclientPortn = _Rm10010arCfgLabelclientPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 9, 3, 1, 1, 3),
    _Rm10010arCfgLabelclientPortn_Type()
)
rm10010arCfgLabelclientPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010arCfgLabelclientPortn.setStatus("current")
_Rm10010arCfgLabellineTable_Object = MibTable
rm10010arCfgLabellineTable = _Rm10010arCfgLabellineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 9, 3, 2)
)
if mibBuilder.loadTexts:
    rm10010arCfgLabellineTable.setStatus("current")
_Rm10010arCfgLabellineEntry_Object = MibTableRow
rm10010arCfgLabellineEntry = _Rm10010arCfgLabellineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 9, 3, 2, 1)
)
rm10010arCfgLabellineEntry.setIndexNames(
    (0, "EKINOPS-Rm10010ar-MIB", "rm10010arCfgLabellineIndex"),
)
if mibBuilder.loadTexts:
    rm10010arCfgLabellineEntry.setStatus("current")


class _Rm10010arCfgLabellineIndex_Type(Integer32):
    """Custom type rm10010arCfgLabellineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010arCfgLabellineIndex_Type.__name__ = "Integer32"
_Rm10010arCfgLabellineIndex_Object = MibTableColumn
rm10010arCfgLabellineIndex = _Rm10010arCfgLabellineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 9, 3, 2, 1, 1),
    _Rm10010arCfgLabellineIndex_Type()
)
rm10010arCfgLabellineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arCfgLabellineIndex.setStatus("current")


class _Rm10010arCfgLabellinePortn_Type(DisplayString):
    """Custom type rm10010arCfgLabellinePortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Rm10010arCfgLabellinePortn_Type.__name__ = "DisplayString"
_Rm10010arCfgLabellinePortn_Object = MibTableColumn
rm10010arCfgLabellinePortn = _Rm10010arCfgLabellinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 9, 3, 2, 1, 3),
    _Rm10010arCfgLabellinePortn_Type()
)
rm10010arCfgLabellinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010arCfgLabellinePortn.setStatus("current")
_Rm10010arCfgStartuptlh_ObjectIdentity = ObjectIdentity
rm10010arCfgStartuptlh = _Rm10010arCfgStartuptlh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 9, 4)
)
_Rm10010arCfgOtxtlhTable_Object = MibTable
rm10010arCfgOtxtlhTable = _Rm10010arCfgOtxtlhTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 9, 4, 1)
)
if mibBuilder.loadTexts:
    rm10010arCfgOtxtlhTable.setStatus("current")
_Rm10010arCfgOtxtlhEntry_Object = MibTableRow
rm10010arCfgOtxtlhEntry = _Rm10010arCfgOtxtlhEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 9, 4, 1, 1)
)
rm10010arCfgOtxtlhEntry.setIndexNames(
    (0, "EKINOPS-Rm10010ar-MIB", "rm10010arCfgOtxtlhIndex"),
)
if mibBuilder.loadTexts:
    rm10010arCfgOtxtlhEntry.setStatus("current")


class _Rm10010arCfgOtxtlhIndex_Type(Integer32):
    """Custom type rm10010arCfgOtxtlhIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010arCfgOtxtlhIndex_Type.__name__ = "Integer32"
_Rm10010arCfgOtxtlhIndex_Object = MibTableColumn
rm10010arCfgOtxtlhIndex = _Rm10010arCfgOtxtlhIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 9, 4, 1, 1, 1),
    _Rm10010arCfgOtxtlhIndex_Type()
)
rm10010arCfgOtxtlhIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arCfgOtxtlhIndex.setStatus("current")


class _Rm10010arCfgLinePwrLaserPortn_Type(Unsigned32):
    """Custom type rm10010arCfgLinePwrLaserPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010arCfgLinePwrLaserPortn_Type.__name__ = "Unsigned32"
_Rm10010arCfgLinePwrLaserPortn_Object = MibTableColumn
rm10010arCfgLinePwrLaserPortn = _Rm10010arCfgLinePwrLaserPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 9, 4, 1, 1, 6),
    _Rm10010arCfgLinePwrLaserPortn_Type()
)
rm10010arCfgLinePwrLaserPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010arCfgLinePwrLaserPortn.setStatus("current")


class _Rm10010arCfgLineFCurrentPortn_Type(Unsigned32):
    """Custom type rm10010arCfgLineFCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010arCfgLineFCurrentPortn_Type.__name__ = "Unsigned32"
_Rm10010arCfgLineFCurrentPortn_Object = MibTableColumn
rm10010arCfgLineFCurrentPortn = _Rm10010arCfgLineFCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 9, 4, 1, 1, 7),
    _Rm10010arCfgLineFCurrentPortn_Type()
)
rm10010arCfgLineFCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010arCfgLineFCurrentPortn.setStatus("current")


class _Rm10010arCfgLineGridCurrentPortn_Type(Unsigned32):
    """Custom type rm10010arCfgLineGridCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010arCfgLineGridCurrentPortn_Type.__name__ = "Unsigned32"
_Rm10010arCfgLineGridCurrentPortn_Object = MibTableColumn
rm10010arCfgLineGridCurrentPortn = _Rm10010arCfgLineGridCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 9, 4, 1, 1, 8),
    _Rm10010arCfgLineGridCurrentPortn_Type()
)
rm10010arCfgLineGridCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010arCfgLineGridCurrentPortn.setStatus("current")


class _Rm10010arCfgRxLineFCurrentPortn_Type(Unsigned32):
    """Custom type rm10010arCfgRxLineFCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010arCfgRxLineFCurrentPortn_Type.__name__ = "Unsigned32"
_Rm10010arCfgRxLineFCurrentPortn_Object = MibTableColumn
rm10010arCfgRxLineFCurrentPortn = _Rm10010arCfgRxLineFCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 9, 4, 1, 1, 10),
    _Rm10010arCfgRxLineFCurrentPortn_Type()
)
rm10010arCfgRxLineFCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010arCfgRxLineFCurrentPortn.setStatus("current")
_Rm10010arCfgOther_ObjectIdentity = ObjectIdentity
rm10010arCfgOther = _Rm10010arCfgOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 9, 5)
)
_Rm10010artablemoduleOther_ObjectIdentity = ObjectIdentity
rm10010artablemoduleOther = _Rm10010artablemoduleOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 9, 5, 1)
)


class _Rm10010arCfgmode_Type(Unsigned32):
    """Custom type rm10010arCfgmode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010arCfgmode_Type.__name__ = "Unsigned32"
_Rm10010arCfgmode_Object = MibScalar
rm10010arCfgmode = _Rm10010arCfgmode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 9, 5, 1, 2),
    _Rm10010arCfgmode_Type()
)
rm10010arCfgmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010arCfgmode.setStatus("current")


class _Rm10010arCfgfanLowSpeedThreshold_Type(Unsigned32):
    """Custom type rm10010arCfgfanLowSpeedThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010arCfgfanLowSpeedThreshold_Type.__name__ = "Unsigned32"
_Rm10010arCfgfanLowSpeedThreshold_Object = MibScalar
rm10010arCfgfanLowSpeedThreshold = _Rm10010arCfgfanLowSpeedThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 9, 5, 1, 3),
    _Rm10010arCfgfanLowSpeedThreshold_Type()
)
rm10010arCfgfanLowSpeedThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010arCfgfanLowSpeedThreshold.setStatus("current")


class _Rm10010arCfgfanHighSpeedThreshold_Type(Unsigned32):
    """Custom type rm10010arCfgfanHighSpeedThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010arCfgfanHighSpeedThreshold_Type.__name__ = "Unsigned32"
_Rm10010arCfgfanHighSpeedThreshold_Object = MibScalar
rm10010arCfgfanHighSpeedThreshold = _Rm10010arCfgfanHighSpeedThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 9, 5, 1, 4),
    _Rm10010arCfgfanHighSpeedThreshold_Type()
)
rm10010arCfgfanHighSpeedThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010arCfgfanHighSpeedThreshold.setStatus("current")
_Rm10010arCfgWriteConfiguration_Type = EkiOnOff
_Rm10010arCfgWriteConfiguration_Object = MibScalar
rm10010arCfgWriteConfiguration = _Rm10010arCfgWriteConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 9, 257),
    _Rm10010arCfgWriteConfiguration_Type()
)
rm10010arCfgWriteConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010arCfgWriteConfiguration.setStatus("current")
_Rm10010artraps_ObjectIdentity = ObjectIdentity
rm10010artraps = _Rm10010artraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 10)
)


class _Rm10010artrapPortNumber_Type(Integer32):
    """Custom type rm10010artrapPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Rm10010artrapPortNumber_Type.__name__ = "Integer32"
_Rm10010artrapPortNumber_Object = MibScalar
rm10010artrapPortNumber = _Rm10010artrapPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 10, 2),
    _Rm10010artrapPortNumber_Type()
)
rm10010artrapPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010artrapPortNumber.setStatus("current")


class _Rm10010artrapLineNumber_Type(Integer32):
    """Custom type rm10010artrapLineNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Rm10010artrapLineNumber_Type.__name__ = "Integer32"
_Rm10010artrapLineNumber_Object = MibScalar
rm10010artrapLineNumber = _Rm10010artrapLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 10, 3),
    _Rm10010artrapLineNumber_Type()
)
rm10010artrapLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010artrapLineNumber.setStatus("current")


class _Rm10010artrapBoardNumber_Type(Integer32):
    """Custom type rm10010artrapBoardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Rm10010artrapBoardNumber_Type.__name__ = "Integer32"
_Rm10010artrapBoardNumber_Object = MibScalar
rm10010artrapBoardNumber = _Rm10010artrapBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 10, 4),
    _Rm10010artrapBoardNumber_Type()
)
rm10010artrapBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010artrapBoardNumber.setStatus("current")
_Rm10010arMonitoring_ObjectIdentity = ObjectIdentity
rm10010arMonitoring = _Rm10010arMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 11)
)
_Rm10010arMonOther_ObjectIdentity = ObjectIdentity
rm10010arMonOther = _Rm10010arMonOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 11, 1)
)
_Rm10010arMonRmon_ObjectIdentity = ObjectIdentity
rm10010arMonRmon = _Rm10010arMonRmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 11, 1, 3)
)
_Rm10010arMonClient_ObjectIdentity = ObjectIdentity
rm10010arMonClient = _Rm10010arMonClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 11, 2)
)
_Rm10010arMonClientRmonCounter_ObjectIdentity = ObjectIdentity
rm10010arMonClientRmonCounter = _Rm10010arMonClientRmonCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 67, 11, 2, 4)
)
_Rm10010arMonupRmonBytesCounterClientInputTable_Object = MibTable
rm10010arMonupRmonBytesCounterClientInputTable = _Rm10010arMonupRmonBytesCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 11, 2, 4, 16)
)
if mibBuilder.loadTexts:
    rm10010arMonupRmonBytesCounterClientInputTable.setStatus("current")
_Rm10010arMonupRmonBytesCounterClientInputEntry_Object = MibTableRow
rm10010arMonupRmonBytesCounterClientInputEntry = _Rm10010arMonupRmonBytesCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 11, 2, 4, 16, 1)
)
rm10010arMonupRmonBytesCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Rm10010ar-MIB", "rm10010arMonupRmonBytesCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    rm10010arMonupRmonBytesCounterClientInputEntry.setStatus("current")


class _Rm10010arMonupRmonBytesCounterClientInputIndex_Type(Integer32):
    """Custom type rm10010arMonupRmonBytesCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010arMonupRmonBytesCounterClientInputIndex_Type.__name__ = "Integer32"
_Rm10010arMonupRmonBytesCounterClientInputIndex_Object = MibTableColumn
rm10010arMonupRmonBytesCounterClientInputIndex = _Rm10010arMonupRmonBytesCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 11, 2, 4, 16, 1, 1),
    _Rm10010arMonupRmonBytesCounterClientInputIndex_Type()
)
rm10010arMonupRmonBytesCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMonupRmonBytesCounterClientInputIndex.setStatus("current")
_Rm10010arMonupRmonBytesCounterClientInputValuePortn_Type = Counter64
_Rm10010arMonupRmonBytesCounterClientInputValuePortn_Object = MibTableColumn
rm10010arMonupRmonBytesCounterClientInputValuePortn = _Rm10010arMonupRmonBytesCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 11, 2, 4, 16, 1, 2),
    _Rm10010arMonupRmonBytesCounterClientInputValuePortn_Type()
)
rm10010arMonupRmonBytesCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMonupRmonBytesCounterClientInputValuePortn.setStatus("current")
_Rm10010arMonupRmonBytesCounterClientInputErrorPortn_Type = EkiOnOff
_Rm10010arMonupRmonBytesCounterClientInputErrorPortn_Object = MibTableColumn
rm10010arMonupRmonBytesCounterClientInputErrorPortn = _Rm10010arMonupRmonBytesCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 11, 2, 4, 16, 1, 3),
    _Rm10010arMonupRmonBytesCounterClientInputErrorPortn_Type()
)
rm10010arMonupRmonBytesCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMonupRmonBytesCounterClientInputErrorPortn.setStatus("current")
_Rm10010arMonupRmonBytesCounterClientInputOverloadPortn_Type = EkiOnOff
_Rm10010arMonupRmonBytesCounterClientInputOverloadPortn_Object = MibTableColumn
rm10010arMonupRmonBytesCounterClientInputOverloadPortn = _Rm10010arMonupRmonBytesCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 11, 2, 4, 16, 1, 4),
    _Rm10010arMonupRmonBytesCounterClientInputOverloadPortn_Type()
)
rm10010arMonupRmonBytesCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMonupRmonBytesCounterClientInputOverloadPortn.setStatus("current")
_Rm10010arMonupRmonCrcErrorsCounterClientInputTable_Object = MibTable
rm10010arMonupRmonCrcErrorsCounterClientInputTable = _Rm10010arMonupRmonCrcErrorsCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 11, 2, 4, 32)
)
if mibBuilder.loadTexts:
    rm10010arMonupRmonCrcErrorsCounterClientInputTable.setStatus("current")
_Rm10010arMonupRmonCrcErrorsCounterClientInputEntry_Object = MibTableRow
rm10010arMonupRmonCrcErrorsCounterClientInputEntry = _Rm10010arMonupRmonCrcErrorsCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 11, 2, 4, 32, 1)
)
rm10010arMonupRmonCrcErrorsCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Rm10010ar-MIB", "rm10010arMonupRmonCrcErrorsCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    rm10010arMonupRmonCrcErrorsCounterClientInputEntry.setStatus("current")


class _Rm10010arMonupRmonCrcErrorsCounterClientInputIndex_Type(Integer32):
    """Custom type rm10010arMonupRmonCrcErrorsCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010arMonupRmonCrcErrorsCounterClientInputIndex_Type.__name__ = "Integer32"
_Rm10010arMonupRmonCrcErrorsCounterClientInputIndex_Object = MibTableColumn
rm10010arMonupRmonCrcErrorsCounterClientInputIndex = _Rm10010arMonupRmonCrcErrorsCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 11, 2, 4, 32, 1, 1),
    _Rm10010arMonupRmonCrcErrorsCounterClientInputIndex_Type()
)
rm10010arMonupRmonCrcErrorsCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMonupRmonCrcErrorsCounterClientInputIndex.setStatus("current")
_Rm10010arMonupRmonCrcErrorsCounterClientInputValuePortn_Type = Counter64
_Rm10010arMonupRmonCrcErrorsCounterClientInputValuePortn_Object = MibTableColumn
rm10010arMonupRmonCrcErrorsCounterClientInputValuePortn = _Rm10010arMonupRmonCrcErrorsCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 11, 2, 4, 32, 1, 2),
    _Rm10010arMonupRmonCrcErrorsCounterClientInputValuePortn_Type()
)
rm10010arMonupRmonCrcErrorsCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMonupRmonCrcErrorsCounterClientInputValuePortn.setStatus("current")
_Rm10010arMonupRmonCrcErrorsCounterClientInputErrorPortn_Type = EkiOnOff
_Rm10010arMonupRmonCrcErrorsCounterClientInputErrorPortn_Object = MibTableColumn
rm10010arMonupRmonCrcErrorsCounterClientInputErrorPortn = _Rm10010arMonupRmonCrcErrorsCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 11, 2, 4, 32, 1, 3),
    _Rm10010arMonupRmonCrcErrorsCounterClientInputErrorPortn_Type()
)
rm10010arMonupRmonCrcErrorsCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMonupRmonCrcErrorsCounterClientInputErrorPortn.setStatus("current")
_Rm10010arMonupRmonCrcErrorsCounterClientInputOverloadPortn_Type = EkiOnOff
_Rm10010arMonupRmonCrcErrorsCounterClientInputOverloadPortn_Object = MibTableColumn
rm10010arMonupRmonCrcErrorsCounterClientInputOverloadPortn = _Rm10010arMonupRmonCrcErrorsCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 11, 2, 4, 32, 1, 4),
    _Rm10010arMonupRmonCrcErrorsCounterClientInputOverloadPortn_Type()
)
rm10010arMonupRmonCrcErrorsCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMonupRmonCrcErrorsCounterClientInputOverloadPortn.setStatus("current")
_Rm10010arMonupRmonPacketsCounterClientInputTable_Object = MibTable
rm10010arMonupRmonPacketsCounterClientInputTable = _Rm10010arMonupRmonPacketsCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 11, 2, 4, 48)
)
if mibBuilder.loadTexts:
    rm10010arMonupRmonPacketsCounterClientInputTable.setStatus("current")
_Rm10010arMonupRmonPacketsCounterClientInputEntry_Object = MibTableRow
rm10010arMonupRmonPacketsCounterClientInputEntry = _Rm10010arMonupRmonPacketsCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 11, 2, 4, 48, 1)
)
rm10010arMonupRmonPacketsCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Rm10010ar-MIB", "rm10010arMonupRmonPacketsCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    rm10010arMonupRmonPacketsCounterClientInputEntry.setStatus("current")


class _Rm10010arMonupRmonPacketsCounterClientInputIndex_Type(Integer32):
    """Custom type rm10010arMonupRmonPacketsCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010arMonupRmonPacketsCounterClientInputIndex_Type.__name__ = "Integer32"
_Rm10010arMonupRmonPacketsCounterClientInputIndex_Object = MibTableColumn
rm10010arMonupRmonPacketsCounterClientInputIndex = _Rm10010arMonupRmonPacketsCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 11, 2, 4, 48, 1, 1),
    _Rm10010arMonupRmonPacketsCounterClientInputIndex_Type()
)
rm10010arMonupRmonPacketsCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMonupRmonPacketsCounterClientInputIndex.setStatus("current")
_Rm10010arMonupRmonPacketsCounterClientInputValuePortn_Type = Counter64
_Rm10010arMonupRmonPacketsCounterClientInputValuePortn_Object = MibTableColumn
rm10010arMonupRmonPacketsCounterClientInputValuePortn = _Rm10010arMonupRmonPacketsCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 11, 2, 4, 48, 1, 2),
    _Rm10010arMonupRmonPacketsCounterClientInputValuePortn_Type()
)
rm10010arMonupRmonPacketsCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMonupRmonPacketsCounterClientInputValuePortn.setStatus("current")
_Rm10010arMonupRmonPacketsCounterClientInputErrorPortn_Type = EkiOnOff
_Rm10010arMonupRmonPacketsCounterClientInputErrorPortn_Object = MibTableColumn
rm10010arMonupRmonPacketsCounterClientInputErrorPortn = _Rm10010arMonupRmonPacketsCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 11, 2, 4, 48, 1, 3),
    _Rm10010arMonupRmonPacketsCounterClientInputErrorPortn_Type()
)
rm10010arMonupRmonPacketsCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMonupRmonPacketsCounterClientInputErrorPortn.setStatus("current")
_Rm10010arMonupRmonPacketsCounterClientInputOverloadPortn_Type = EkiOnOff
_Rm10010arMonupRmonPacketsCounterClientInputOverloadPortn_Object = MibTableColumn
rm10010arMonupRmonPacketsCounterClientInputOverloadPortn = _Rm10010arMonupRmonPacketsCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 11, 2, 4, 48, 1, 4),
    _Rm10010arMonupRmonPacketsCounterClientInputOverloadPortn_Type()
)
rm10010arMonupRmonPacketsCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMonupRmonPacketsCounterClientInputOverloadPortn.setStatus("current")
_Rm10010arMonupRmonBroadcastCounterClientInputTable_Object = MibTable
rm10010arMonupRmonBroadcastCounterClientInputTable = _Rm10010arMonupRmonBroadcastCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 11, 2, 4, 64)
)
if mibBuilder.loadTexts:
    rm10010arMonupRmonBroadcastCounterClientInputTable.setStatus("current")
_Rm10010arMonupRmonBroadcastCounterClientInputEntry_Object = MibTableRow
rm10010arMonupRmonBroadcastCounterClientInputEntry = _Rm10010arMonupRmonBroadcastCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 11, 2, 4, 64, 1)
)
rm10010arMonupRmonBroadcastCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Rm10010ar-MIB", "rm10010arMonupRmonBroadcastCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    rm10010arMonupRmonBroadcastCounterClientInputEntry.setStatus("current")


class _Rm10010arMonupRmonBroadcastCounterClientInputIndex_Type(Integer32):
    """Custom type rm10010arMonupRmonBroadcastCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010arMonupRmonBroadcastCounterClientInputIndex_Type.__name__ = "Integer32"
_Rm10010arMonupRmonBroadcastCounterClientInputIndex_Object = MibTableColumn
rm10010arMonupRmonBroadcastCounterClientInputIndex = _Rm10010arMonupRmonBroadcastCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 11, 2, 4, 64, 1, 1),
    _Rm10010arMonupRmonBroadcastCounterClientInputIndex_Type()
)
rm10010arMonupRmonBroadcastCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMonupRmonBroadcastCounterClientInputIndex.setStatus("current")
_Rm10010arMonupRmonBroadcastCounterClientInputValuePortn_Type = Counter64
_Rm10010arMonupRmonBroadcastCounterClientInputValuePortn_Object = MibTableColumn
rm10010arMonupRmonBroadcastCounterClientInputValuePortn = _Rm10010arMonupRmonBroadcastCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 11, 2, 4, 64, 1, 2),
    _Rm10010arMonupRmonBroadcastCounterClientInputValuePortn_Type()
)
rm10010arMonupRmonBroadcastCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMonupRmonBroadcastCounterClientInputValuePortn.setStatus("current")
_Rm10010arMonupRmonBroadcastCounterClientInputErrorPortn_Type = EkiOnOff
_Rm10010arMonupRmonBroadcastCounterClientInputErrorPortn_Object = MibTableColumn
rm10010arMonupRmonBroadcastCounterClientInputErrorPortn = _Rm10010arMonupRmonBroadcastCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 11, 2, 4, 64, 1, 3),
    _Rm10010arMonupRmonBroadcastCounterClientInputErrorPortn_Type()
)
rm10010arMonupRmonBroadcastCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMonupRmonBroadcastCounterClientInputErrorPortn.setStatus("current")
_Rm10010arMonupRmonBroadcastCounterClientInputOverloadPortn_Type = EkiOnOff
_Rm10010arMonupRmonBroadcastCounterClientInputOverloadPortn_Object = MibTableColumn
rm10010arMonupRmonBroadcastCounterClientInputOverloadPortn = _Rm10010arMonupRmonBroadcastCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 11, 2, 4, 64, 1, 4),
    _Rm10010arMonupRmonBroadcastCounterClientInputOverloadPortn_Type()
)
rm10010arMonupRmonBroadcastCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMonupRmonBroadcastCounterClientInputOverloadPortn.setStatus("current")
_Rm10010arMonupRmonMulticastCounterClientInputTable_Object = MibTable
rm10010arMonupRmonMulticastCounterClientInputTable = _Rm10010arMonupRmonMulticastCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 11, 2, 4, 80)
)
if mibBuilder.loadTexts:
    rm10010arMonupRmonMulticastCounterClientInputTable.setStatus("current")
_Rm10010arMonupRmonMulticastCounterClientInputEntry_Object = MibTableRow
rm10010arMonupRmonMulticastCounterClientInputEntry = _Rm10010arMonupRmonMulticastCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 11, 2, 4, 80, 1)
)
rm10010arMonupRmonMulticastCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Rm10010ar-MIB", "rm10010arMonupRmonMulticastCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    rm10010arMonupRmonMulticastCounterClientInputEntry.setStatus("current")


class _Rm10010arMonupRmonMulticastCounterClientInputIndex_Type(Integer32):
    """Custom type rm10010arMonupRmonMulticastCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010arMonupRmonMulticastCounterClientInputIndex_Type.__name__ = "Integer32"
_Rm10010arMonupRmonMulticastCounterClientInputIndex_Object = MibTableColumn
rm10010arMonupRmonMulticastCounterClientInputIndex = _Rm10010arMonupRmonMulticastCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 11, 2, 4, 80, 1, 1),
    _Rm10010arMonupRmonMulticastCounterClientInputIndex_Type()
)
rm10010arMonupRmonMulticastCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMonupRmonMulticastCounterClientInputIndex.setStatus("current")
_Rm10010arMonupRmonMulticastCounterClientInputValuePortn_Type = Counter64
_Rm10010arMonupRmonMulticastCounterClientInputValuePortn_Object = MibTableColumn
rm10010arMonupRmonMulticastCounterClientInputValuePortn = _Rm10010arMonupRmonMulticastCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 11, 2, 4, 80, 1, 2),
    _Rm10010arMonupRmonMulticastCounterClientInputValuePortn_Type()
)
rm10010arMonupRmonMulticastCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMonupRmonMulticastCounterClientInputValuePortn.setStatus("current")
_Rm10010arMonupRmonMulticastCounterClientInputErrorPortn_Type = EkiOnOff
_Rm10010arMonupRmonMulticastCounterClientInputErrorPortn_Object = MibTableColumn
rm10010arMonupRmonMulticastCounterClientInputErrorPortn = _Rm10010arMonupRmonMulticastCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 11, 2, 4, 80, 1, 3),
    _Rm10010arMonupRmonMulticastCounterClientInputErrorPortn_Type()
)
rm10010arMonupRmonMulticastCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMonupRmonMulticastCounterClientInputErrorPortn.setStatus("current")
_Rm10010arMonupRmonMulticastCounterClientInputOverloadPortn_Type = EkiOnOff
_Rm10010arMonupRmonMulticastCounterClientInputOverloadPortn_Object = MibTableColumn
rm10010arMonupRmonMulticastCounterClientInputOverloadPortn = _Rm10010arMonupRmonMulticastCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 11, 2, 4, 80, 1, 4),
    _Rm10010arMonupRmonMulticastCounterClientInputOverloadPortn_Type()
)
rm10010arMonupRmonMulticastCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMonupRmonMulticastCounterClientInputOverloadPortn.setStatus("current")
_Rm10010arMonupRmonPauseFrameCounterClientInputTable_Object = MibTable
rm10010arMonupRmonPauseFrameCounterClientInputTable = _Rm10010arMonupRmonPauseFrameCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 11, 2, 4, 96)
)
if mibBuilder.loadTexts:
    rm10010arMonupRmonPauseFrameCounterClientInputTable.setStatus("current")
_Rm10010arMonupRmonPauseFrameCounterClientInputEntry_Object = MibTableRow
rm10010arMonupRmonPauseFrameCounterClientInputEntry = _Rm10010arMonupRmonPauseFrameCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 11, 2, 4, 96, 1)
)
rm10010arMonupRmonPauseFrameCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Rm10010ar-MIB", "rm10010arMonupRmonPauseFrameCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    rm10010arMonupRmonPauseFrameCounterClientInputEntry.setStatus("current")


class _Rm10010arMonupRmonPauseFrameCounterClientInputIndex_Type(Integer32):
    """Custom type rm10010arMonupRmonPauseFrameCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010arMonupRmonPauseFrameCounterClientInputIndex_Type.__name__ = "Integer32"
_Rm10010arMonupRmonPauseFrameCounterClientInputIndex_Object = MibTableColumn
rm10010arMonupRmonPauseFrameCounterClientInputIndex = _Rm10010arMonupRmonPauseFrameCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 11, 2, 4, 96, 1, 1),
    _Rm10010arMonupRmonPauseFrameCounterClientInputIndex_Type()
)
rm10010arMonupRmonPauseFrameCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMonupRmonPauseFrameCounterClientInputIndex.setStatus("current")
_Rm10010arMonupRmonPauseFrameCounterClientInputValuePortn_Type = Counter64
_Rm10010arMonupRmonPauseFrameCounterClientInputValuePortn_Object = MibTableColumn
rm10010arMonupRmonPauseFrameCounterClientInputValuePortn = _Rm10010arMonupRmonPauseFrameCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 11, 2, 4, 96, 1, 2),
    _Rm10010arMonupRmonPauseFrameCounterClientInputValuePortn_Type()
)
rm10010arMonupRmonPauseFrameCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMonupRmonPauseFrameCounterClientInputValuePortn.setStatus("current")
_Rm10010arMonupRmonPauseFrameCounterClientInputErrorPortn_Type = EkiOnOff
_Rm10010arMonupRmonPauseFrameCounterClientInputErrorPortn_Object = MibTableColumn
rm10010arMonupRmonPauseFrameCounterClientInputErrorPortn = _Rm10010arMonupRmonPauseFrameCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 11, 2, 4, 96, 1, 3),
    _Rm10010arMonupRmonPauseFrameCounterClientInputErrorPortn_Type()
)
rm10010arMonupRmonPauseFrameCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMonupRmonPauseFrameCounterClientInputErrorPortn.setStatus("current")
_Rm10010arMonupRmonPauseFrameCounterClientInputOverloadPortn_Type = EkiOnOff
_Rm10010arMonupRmonPauseFrameCounterClientInputOverloadPortn_Object = MibTableColumn
rm10010arMonupRmonPauseFrameCounterClientInputOverloadPortn = _Rm10010arMonupRmonPauseFrameCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 67, 11, 2, 4, 96, 1, 4),
    _Rm10010arMonupRmonPauseFrameCounterClientInputOverloadPortn_Type()
)
rm10010arMonupRmonPauseFrameCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010arMonupRmonPauseFrameCounterClientInputOverloadPortn.setStatus("current")

# Managed Objects groups


# Notification objects

rm10010arLineTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 67, 10, 30)
)
rm10010arLineTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Rm10010ar-MIB", "rm10010arAlmLineDdmWarningPortn"),
        ("EKINOPS-Rm10010ar-MIB", "rm10010artrapLineNumber"),
        ("EKINOPS-Rm10010ar-MIB", "rm10010artrapBoardNumber"))
)
if mibBuilder.loadTexts:
    rm10010arLineTrapNotUrgentGoesOn.setStatus(
        "current"
    )

rm10010arLineTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 67, 10, 31)
)
rm10010arLineTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Rm10010ar-MIB", "rm10010arAlmLineDdmWarningPortn"),
        ("EKINOPS-Rm10010ar-MIB", "rm10010artrapLineNumber"),
        ("EKINOPS-Rm10010ar-MIB", "rm10010artrapBoardNumber"))
)
if mibBuilder.loadTexts:
    rm10010arLineTrapNotUrgentGoesOff.setStatus(
        "current"
    )

rm10010arLineTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 67, 10, 32)
)
rm10010arLineTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Rm10010ar-MIB", "rm10010arAlmLineDdmAlmPortn"),
        ("EKINOPS-Rm10010ar-MIB", "rm10010artrapLineNumber"),
        ("EKINOPS-Rm10010ar-MIB", "rm10010artrapBoardNumber"))
)
if mibBuilder.loadTexts:
    rm10010arLineTrapUrgentGoesOn.setStatus(
        "current"
    )

rm10010arLineTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 67, 10, 33)
)
rm10010arLineTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Rm10010ar-MIB", "rm10010arAlmLineDdmAlmPortn"),
        ("EKINOPS-Rm10010ar-MIB", "rm10010artrapLineNumber"),
        ("EKINOPS-Rm10010ar-MIB", "rm10010artrapBoardNumber"))
)
if mibBuilder.loadTexts:
    rm10010arLineTrapUrgentGoesOff.setStatus(
        "current"
    )

rm10010arLineTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 67, 10, 34)
)
rm10010arLineTrapCritGoesOn.setObjects(
      *(("EKINOPS-Rm10010ar-MIB", "rm10010arAlmLineFailPortn"),
        ("EKINOPS-Rm10010ar-MIB", "rm10010arAlmLineHwFailPortn"),
        ("EKINOPS-Rm10010ar-MIB", "rm10010artrapLineNumber"),
        ("EKINOPS-Rm10010ar-MIB", "rm10010artrapBoardNumber"))
)
if mibBuilder.loadTexts:
    rm10010arLineTrapCritGoesOn.setStatus(
        "current"
    )

rm10010arLineTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 67, 10, 35)
)
rm10010arLineTrapCritGoesOff.setObjects(
      *(("EKINOPS-Rm10010ar-MIB", "rm10010arAlmLineFailPortn"),
        ("EKINOPS-Rm10010ar-MIB", "rm10010arAlmLineHwFailPortn"),
        ("EKINOPS-Rm10010ar-MIB", "rm10010artrapLineNumber"),
        ("EKINOPS-Rm10010ar-MIB", "rm10010artrapBoardNumber"))
)
if mibBuilder.loadTexts:
    rm10010arLineTrapCritGoesOff.setStatus(
        "current"
    )

rm10010arClientTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 67, 10, 40)
)
rm10010arClientTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Rm10010ar-MIB", "rm10010arAlmSfpDdmWarningPortn"),
        ("EKINOPS-Rm10010ar-MIB", "rm10010artrapPortNumber"),
        ("EKINOPS-Rm10010ar-MIB", "rm10010artrapBoardNumber"))
)
if mibBuilder.loadTexts:
    rm10010arClientTrapNotUrgentGoesOn.setStatus(
        "current"
    )

rm10010arClientTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 67, 10, 41)
)
rm10010arClientTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Rm10010ar-MIB", "rm10010arAlmSfpDdmWarningPortn"),
        ("EKINOPS-Rm10010ar-MIB", "rm10010artrapPortNumber"),
        ("EKINOPS-Rm10010ar-MIB", "rm10010artrapBoardNumber"))
)
if mibBuilder.loadTexts:
    rm10010arClientTrapNotUrgentGoesOff.setStatus(
        "current"
    )

rm10010arClientTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 67, 10, 42)
)
rm10010arClientTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Rm10010ar-MIB", "rm10010arAlmSfpDdmAlmPortn"),
        ("EKINOPS-Rm10010ar-MIB", "rm10010artrapPortNumber"),
        ("EKINOPS-Rm10010ar-MIB", "rm10010artrapBoardNumber"))
)
if mibBuilder.loadTexts:
    rm10010arClientTrapUrgentGoesOn.setStatus(
        "current"
    )

rm10010arClientTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 67, 10, 43)
)
rm10010arClientTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Rm10010ar-MIB", "rm10010arAlmSfpDdmAlmPortn"),
        ("EKINOPS-Rm10010ar-MIB", "rm10010artrapPortNumber"),
        ("EKINOPS-Rm10010ar-MIB", "rm10010artrapBoardNumber"))
)
if mibBuilder.loadTexts:
    rm10010arClientTrapUrgentGoesOff.setStatus(
        "current"
    )

rm10010arClientTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 67, 10, 44)
)
rm10010arClientTrapCritGoesOn.setObjects(
      *(("EKINOPS-Rm10010ar-MIB", "rm10010arAlmFailAccPortn"),
        ("EKINOPS-Rm10010ar-MIB", "rm10010arAlmHwFailAccPortn"),
        ("EKINOPS-Rm10010ar-MIB", "rm10010artrapPortNumber"),
        ("EKINOPS-Rm10010ar-MIB", "rm10010artrapBoardNumber"))
)
if mibBuilder.loadTexts:
    rm10010arClientTrapCritGoesOn.setStatus(
        "current"
    )

rm10010arClientTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 67, 10, 45)
)
rm10010arClientTrapCritGoesOff.setObjects(
      *(("EKINOPS-Rm10010ar-MIB", "rm10010arAlmFailAccPortn"),
        ("EKINOPS-Rm10010ar-MIB", "rm10010arAlmHwFailAccPortn"),
        ("EKINOPS-Rm10010ar-MIB", "rm10010artrapPortNumber"),
        ("EKINOPS-Rm10010ar-MIB", "rm10010artrapBoardNumber"))
)
if mibBuilder.loadTexts:
    rm10010arClientTrapCritGoesOff.setStatus(
        "current"
    )

rm10010arPowerTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 67, 10, 50)
)
rm10010arPowerTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Rm10010ar-MIB", "rm10010arAlmDefFuseB"),
        ("EKINOPS-Rm10010ar-MIB", "rm10010arAlmDefFuseA"),
        ("EKINOPS-Rm10010ar-MIB", "rm10010artrapBoardNumber"))
)
if mibBuilder.loadTexts:
    rm10010arPowerTrapUrgentGoesOn.setStatus(
        "current"
    )

rm10010arPowerTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 67, 10, 51)
)
rm10010arPowerTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Rm10010ar-MIB", "rm10010arAlmDefFuseB"),
        ("EKINOPS-Rm10010ar-MIB", "rm10010arAlmDefFuseA"),
        ("EKINOPS-Rm10010ar-MIB", "rm10010artrapBoardNumber"))
)
if mibBuilder.loadTexts:
    rm10010arPowerTrapUrgentGoesOff.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EKINOPS-Rm10010ar-MIB",
    **{"Rm10010arMultiRate": Rm10010arMultiRate,
       "Rm10010arOtxMode": Rm10010arOtxMode,
       "Rm10010arOtxGrid": Rm10010arOtxGrid,
       "Rm10010arAdjustValue": Rm10010arAdjustValue,
       "Rm10010arClientProtocol": Rm10010arClientProtocol,
       "Rm10010arProtocolMode": Rm10010arProtocolMode,
       "Rm10010arOtxChannel": Rm10010arOtxChannel,
       "Rm10010arOrxChannel": Rm10010arOrxChannel,
       "moduleRm10010ar": moduleRm10010ar,
       "rm10010aralarms": rm10010aralarms,
       "rm10010arAlmOther": rm10010arAlmOther,
       "rm10010arAlmOtherNurg": rm10010arAlmOtherNurg,
       "rm10010arAlmsynthAlm2": rm10010arAlmsynthAlm2,
       "rm10010arAlmConfTableSave": rm10010arAlmConfTableSave,
       "rm10010arAlmInvUpload": rm10010arAlmInvUpload,
       "rm10010arAlmConfTableLoad": rm10010arAlmConfTableLoad,
       "rm10010arAlmCorrelatOff": rm10010arAlmCorrelatOff,
       "rm10010arAlmMaintenanceOn": rm10010arAlmMaintenanceOn,
       "rm10010arAlmOtherUrg": rm10010arAlmOtherUrg,
       "rm10010arAlmmodFanFail": rm10010arAlmmodFanFail,
       "rm10010arAlmFanModuleAbsent": rm10010arAlmFanModuleAbsent,
       "rm10010arAlmFansFail": rm10010arAlmFansFail,
       "rm10010arAlmFan1Fail": rm10010arAlmFan1Fail,
       "rm10010arAlmFan2Fail": rm10010arAlmFan2Fail,
       "rm10010arAlmFan3Fail": rm10010arAlmFan3Fail,
       "rm10010arAlmFan4Fail": rm10010arAlmFan4Fail,
       "rm10010arAlmOtherCrit": rm10010arAlmOtherCrit,
       "rm10010arAlmsynthAlm0": rm10010arAlmsynthAlm0,
       "rm10010arAlmFailFan": rm10010arAlmFailFan,
       "rm10010arAlmModGlobFail": rm10010arAlmModGlobFail,
       "rm10010arAlmDefFuseA": rm10010arAlmDefFuseA,
       "rm10010arAlmDefFuseB": rm10010arAlmDefFuseB,
       "rm10010arAlmclientModuleState": rm10010arAlmclientModuleState,
       "rm10010arAlmCfpInitialize": rm10010arAlmCfpInitialize,
       "rm10010arAlmCfpLowPower": rm10010arAlmCfpLowPower,
       "rm10010arAlmCfpHighPowerUp": rm10010arAlmCfpHighPowerUp,
       "rm10010arAlmCfpTxOff": rm10010arAlmCfpTxOff,
       "rm10010arAlmCfpTxTurnOn": rm10010arAlmCfpTxTurnOn,
       "rm10010arAlmCfpReady": rm10010arAlmCfpReady,
       "rm10010arAlmCfpFault": rm10010arAlmCfpFault,
       "rm10010arAlmCfpTxTurnOff": rm10010arAlmCfpTxTurnOff,
       "rm10010arAlmCfpHighPowerDown": rm10010arAlmCfpHighPowerDown,
       "rm10010arAlmclientModuleGeneralStatus": rm10010arAlmclientModuleGeneralStatus,
       "rm10010arAlmCfpOutOfAlignment": rm10010arAlmCfpOutOfAlignment,
       "rm10010arAlmCfpRxNetworkLol": rm10010arAlmCfpRxNetworkLol,
       "rm10010arAlmCfpRxLos": rm10010arAlmCfpRxLos,
       "rm10010arAlmCfpTxHostLol": rm10010arAlmCfpTxHostLol,
       "rm10010arAlmCfpTxLosf": rm10010arAlmCfpTxLosf,
       "rm10010arAlmCfpTxCmuLol": rm10010arAlmCfpTxCmuLol,
       "rm10010arAlmCfpTxJitterPllLol": rm10010arAlmCfpTxJitterPllLol,
       "rm10010arAlmCfpLossOfRefclk": rm10010arAlmCfpLossOfRefclk,
       "rm10010arAlmCfpHwInterlock": rm10010arAlmCfpHwInterlock,
       "rm10010arAlmclientGlobalAlarmSummary": rm10010arAlmclientGlobalAlarmSummary,
       "rm10010arAlmCfpSoftGlobAlarmTest": rm10010arAlmCfpSoftGlobAlarmTest,
       "rm10010arAlmCfpNetworkLaneAlarmWarning2": rm10010arAlmCfpNetworkLaneAlarmWarning2,
       "rm10010arAlmCfpModuleState": rm10010arAlmCfpModuleState,
       "rm10010arAlmCfpModuleGeneralStatus": rm10010arAlmCfpModuleGeneralStatus,
       "rm10010arAlmCfpModuleFault": rm10010arAlmCfpModuleFault,
       "rm10010arAlmCfpModuleAlarmWarning1": rm10010arAlmCfpModuleAlarmWarning1,
       "rm10010arAlmCfpModuleAlarmWarning2": rm10010arAlmCfpModuleAlarmWarning2,
       "rm10010arAlmCfpNetworkLaneAlarmWarning1": rm10010arAlmCfpNetworkLaneAlarmWarning1,
       "rm10010arAlmCfpNetworkLaneFaultStatus": rm10010arAlmCfpNetworkLaneFaultStatus,
       "rm10010arAlmCfpHostLaneFaultStatus": rm10010arAlmCfpHostLaneFaultStatus,
       "rm10010arAlmCfpGlobAlarmAssertion": rm10010arAlmCfpGlobAlarmAssertion,
       "rm10010arAlmmsaModuleState": rm10010arAlmmsaModuleState,
       "rm10010arAlmMsaInitialize": rm10010arAlmMsaInitialize,
       "rm10010arAlmMsaLowPower": rm10010arAlmMsaLowPower,
       "rm10010arAlmMsaHighPowerUp": rm10010arAlmMsaHighPowerUp,
       "rm10010arAlmMsaTxOff": rm10010arAlmMsaTxOff,
       "rm10010arAlmMsaTxTurnOn": rm10010arAlmMsaTxTurnOn,
       "rm10010arAlmMsaReady": rm10010arAlmMsaReady,
       "rm10010arAlmMsaFault": rm10010arAlmMsaFault,
       "rm10010arAlmMsaTxTurnOff": rm10010arAlmMsaTxTurnOff,
       "rm10010arAlmMsaHighPowerDown": rm10010arAlmMsaHighPowerDown,
       "rm10010arAlmmsaModuleGeneralStatus": rm10010arAlmmsaModuleGeneralStatus,
       "rm10010arAlmMsaOutOfAlignment": rm10010arAlmMsaOutOfAlignment,
       "rm10010arAlmMsaRxNetworkLol": rm10010arAlmMsaRxNetworkLol,
       "rm10010arAlmMsaRxLos": rm10010arAlmMsaRxLos,
       "rm10010arAlmMsaTxHostLol": rm10010arAlmMsaTxHostLol,
       "rm10010arAlmMsaTxLosf": rm10010arAlmMsaTxLosf,
       "rm10010arAlmMsaTxCmuLol": rm10010arAlmMsaTxCmuLol,
       "rm10010arAlmMsaTxJitterPllLol": rm10010arAlmMsaTxJitterPllLol,
       "rm10010arAlmMsaLossOfRefclk": rm10010arAlmMsaLossOfRefclk,
       "rm10010arAlmMsaHwInterlock": rm10010arAlmMsaHwInterlock,
       "rm10010arAlmmsaGlobalAlarmSummary": rm10010arAlmmsaGlobalAlarmSummary,
       "rm10010arAlmMsaSoftGlobAlarmTest": rm10010arAlmMsaSoftGlobAlarmTest,
       "rm10010arAlmMsaNetworkHostAlarmStatus": rm10010arAlmMsaNetworkHostAlarmStatus,
       "rm10010arAlmMsaNetworkLaneAlarmWarning2": rm10010arAlmMsaNetworkLaneAlarmWarning2,
       "rm10010arAlmMsaModuleState": rm10010arAlmMsaModuleState,
       "rm10010arAlmMsaModuleGeneralStatus": rm10010arAlmMsaModuleGeneralStatus,
       "rm10010arAlmModuleFault": rm10010arAlmModuleFault,
       "rm10010arAlmMsaModuleAlarmWarning1": rm10010arAlmMsaModuleAlarmWarning1,
       "rm10010arAlmMsaModuleAlarmWarning2": rm10010arAlmMsaModuleAlarmWarning2,
       "rm10010arAlmMsaNetworkLaneAlarmWarning1": rm10010arAlmMsaNetworkLaneAlarmWarning1,
       "rm10010arAlmMsaNetworkLaneFaultStatus": rm10010arAlmMsaNetworkLaneFaultStatus,
       "rm10010arAlmMsaHostLaneFaultStatus": rm10010arAlmMsaHostLaneFaultStatus,
       "rm10010arAlmMsaGlobAlarmAssertion": rm10010arAlmMsaGlobAlarmAssertion,
       "rm10010arAlmmsaNetworkTxAlignment": rm10010arAlmmsaNetworkTxAlignment,
       "rm10010arAlmNetTxTimingFault": rm10010arAlmNetTxTimingFault,
       "rm10010arAlmNetTxReferenceClockFault": rm10010arAlmNetTxReferenceClockFault,
       "rm10010arAlmNetTxCmuLockFault": rm10010arAlmNetTxCmuLockFault,
       "rm10010arAlmNetTxOutOfAlignment": rm10010arAlmNetTxOutOfAlignment,
       "rm10010arAlmNetTxLossOfAlignment": rm10010arAlmNetTxLossOfAlignment,
       "rm10010arAlmmsaNetworkRxAlignment": rm10010arAlmmsaNetworkRxAlignment,
       "rm10010arAlmNetRxTimingFault": rm10010arAlmNetRxTimingFault,
       "rm10010arAlmNetRxOutOfAlignment": rm10010arAlmNetRxOutOfAlignment,
       "rm10010arAlmNetRxLossOfAlignment": rm10010arAlmNetRxLossOfAlignment,
       "rm10010arAlmNetRxModemLockFault": rm10010arAlmNetRxModemLockFault,
       "rm10010arAlmNetRxModemSyncDetectFault": rm10010arAlmNetRxModemSyncDetectFault,
       "rm10010arAlmmsaNetworkHostNetworkAlarmSummary": rm10010arAlmmsaNetworkHostNetworkAlarmSummary,
       "rm10010arAlmNetworkTxAlignment": rm10010arAlmNetworkTxAlignment,
       "rm10010arAlmNetworkRxAlignment": rm10010arAlmNetworkRxAlignment,
       "rm10010arAlmNetworkRxOtn": rm10010arAlmNetworkRxOtn,
       "rm10010arAlmHostRxAlignment": rm10010arAlmHostRxAlignment,
       "rm10010arAlmHostTxAlignment": rm10010arAlmHostTxAlignment,
       "rm10010arAlmHostTxOtnStatus": rm10010arAlmHostTxOtnStatus,
       "rm10010arAlmmsaHostTxAlignment": rm10010arAlmmsaHostTxAlignment,
       "rm10010arAlmHostTxDeskewLockFault": rm10010arAlmHostTxDeskewLockFault,
       "rm10010arAlmHostTxOutOfAlignment": rm10010arAlmHostTxOutOfAlignment,
       "rm10010arAlmHostTxLossOfAlignment": rm10010arAlmHostTxLossOfAlignment,
       "rm10010arAlmHostTxCdrLockFault": rm10010arAlmHostTxCdrLockFault,
       "rm10010arAlmmsaHostRxAlignment": rm10010arAlmmsaHostRxAlignment,
       "rm10010arAlmHostRxCmuLockFault": rm10010arAlmHostRxCmuLockFault,
       "rm10010arAlmHostRxOutOfAlignment": rm10010arAlmHostRxOutOfAlignment,
       "rm10010arAlmHostRxLossOfAlignment": rm10010arAlmHostRxLossOfAlignment,
       "rm10010arAlmClient": rm10010arAlmClient,
       "rm10010arAlmClientNurg": rm10010arAlmClientNurg,
       "rm10010arAlmclientNetworkLaneAlarmWarningTable": rm10010arAlmclientNetworkLaneAlarmWarningTable,
       "rm10010arAlmclientNetworkLaneAlarmWarningEntry": rm10010arAlmclientNetworkLaneAlarmWarningEntry,
       "rm10010arAlmclientNetworkLaneAlarmWarningIndex": rm10010arAlmclientNetworkLaneAlarmWarningIndex,
       "rm10010arAlmClientRxPowerLowAlarmPortn": rm10010arAlmClientRxPowerLowAlarmPortn,
       "rm10010arAlmClientRxPowerLowWarningPortn": rm10010arAlmClientRxPowerLowWarningPortn,
       "rm10010arAlmClientRxPowerHighWarningPortn": rm10010arAlmClientRxPowerHighWarningPortn,
       "rm10010arAlmClientRxPowerHighAlarmPortn": rm10010arAlmClientRxPowerHighAlarmPortn,
       "rm10010arAlmLaserTempLowAlarmPortn": rm10010arAlmLaserTempLowAlarmPortn,
       "rm10010arAlmClientLaserTempLowWarningPortn": rm10010arAlmClientLaserTempLowWarningPortn,
       "rm10010arAlmClientLaserTempHighWarningPortn": rm10010arAlmClientLaserTempHighWarningPortn,
       "rm10010arAlmClientLaserTempHighAlarmPortn": rm10010arAlmClientLaserTempHighAlarmPortn,
       "rm10010arAlmClientTxPowerLowAlarmPortn": rm10010arAlmClientTxPowerLowAlarmPortn,
       "rm10010arAlmClientTxPowerLowWarningPortn": rm10010arAlmClientTxPowerLowWarningPortn,
       "rm10010arAlmClientTxPowerHighWarningPortn": rm10010arAlmClientTxPowerHighWarningPortn,
       "rm10010arAlmClientTxPowerHighAlarmPortn": rm10010arAlmClientTxPowerHighAlarmPortn,
       "rm10010arAlmClientBiasLowAlarmPortn": rm10010arAlmClientBiasLowAlarmPortn,
       "rm10010arAlmClientBiasLowWarningPortn": rm10010arAlmClientBiasLowWarningPortn,
       "rm10010arAlmClientBiasHighWarningPortn": rm10010arAlmClientBiasHighWarningPortn,
       "rm10010arAlmClientBiasHighAlarmPortn": rm10010arAlmClientBiasHighAlarmPortn,
       "rm10010arAlmclientSfpWarnDdmTable": rm10010arAlmclientSfpWarnDdmTable,
       "rm10010arAlmclientSfpWarnDdmEntry": rm10010arAlmclientSfpWarnDdmEntry,
       "rm10010arAlmclientSfpWarnDdmIndex": rm10010arAlmclientSfpWarnDdmIndex,
       "rm10010arAlmTxPwLowWngPortn": rm10010arAlmTxPwLowWngPortn,
       "rm10010arAlmTxPwrHighWngPortn": rm10010arAlmTxPwrHighWngPortn,
       "rm10010arAlmTxBiasLowWngPortn": rm10010arAlmTxBiasLowWngPortn,
       "rm10010arAlmTxBiasHighWngPortn": rm10010arAlmTxBiasHighWngPortn,
       "rm10010arAlmVccLowWngPortn": rm10010arAlmVccLowWngPortn,
       "rm10010arAlmVccHighWngPortn": rm10010arAlmVccHighWngPortn,
       "rm10010arAlmTempLowWngPortn": rm10010arAlmTempLowWngPortn,
       "rm10010arAlmTempHighWngPortn": rm10010arAlmTempHighWngPortn,
       "rm10010arAlmRxPwrLowWngPortn": rm10010arAlmRxPwrLowWngPortn,
       "rm10010arAlmRxPwrHighWngPortn": rm10010arAlmRxPwrHighWngPortn,
       "rm10010arAlmClientUrg": rm10010arAlmClientUrg,
       "rm10010arAlmclientNetworkLaneFaultTable": rm10010arAlmclientNetworkLaneFaultTable,
       "rm10010arAlmclientNetworkLaneFaultEntry": rm10010arAlmclientNetworkLaneFaultEntry,
       "rm10010arAlmclientNetworkLaneFaultIndex": rm10010arAlmclientNetworkLaneFaultIndex,
       "rm10010arAlmClientLaneRxFifoErrorPortn": rm10010arAlmClientLaneRxFifoErrorPortn,
       "rm10010arAlmClientLaneRxLolPortn": rm10010arAlmClientLaneRxLolPortn,
       "rm10010arAlmClientLaneRxLosPortn": rm10010arAlmClientLaneRxLosPortn,
       "rm10010arAlmClientLaneTxLolPortn": rm10010arAlmClientLaneTxLolPortn,
       "rm10010arAlmClientLaneTxLosfPortn": rm10010arAlmClientLaneTxLosfPortn,
       "rm10010arAlmClientLaneApdPowerSupplyPortn": rm10010arAlmClientLaneApdPowerSupplyPortn,
       "rm10010arAlmClientLaneWavelengthUnlockedPortn": rm10010arAlmClientLaneWavelengthUnlockedPortn,
       "rm10010arAlmClientLaneTecFaultPortn": rm10010arAlmClientLaneTecFaultPortn,
       "rm10010arAlmclientHostLaneFaultTable": rm10010arAlmclientHostLaneFaultTable,
       "rm10010arAlmclientHostLaneFaultEntry": rm10010arAlmclientHostLaneFaultEntry,
       "rm10010arAlmclientHostLaneFaultIndex": rm10010arAlmclientHostLaneFaultIndex,
       "rm10010arAlmClientLossOfSyncPortn": rm10010arAlmClientLossOfSyncPortn,
       "rm10010arAlmClientInputLossOfSigPortn": rm10010arAlmClientInputLossOfSigPortn,
       "rm10010arAlmClientLanesMarkerUnlockPortn": rm10010arAlmClientLanesMarkerUnlockPortn,
       "rm10010arAlmClientLanes6466UnlockPortn": rm10010arAlmClientLanes6466UnlockPortn,
       "rm10010arAlmClientLanesNotAlignedPortn": rm10010arAlmClientLanesNotAlignedPortn,
       "rm10010arAlmClientCsfDetectedPortn": rm10010arAlmClientCsfDetectedPortn,
       "rm10010arAlmClientTxHostLolPortn": rm10010arAlmClientTxHostLolPortn,
       "rm10010arAlmClientLaneTxFifoErrorPortn": rm10010arAlmClientLaneTxFifoErrorPortn,
       "rm10010arAlmclientSfpAlmDdmTable": rm10010arAlmclientSfpAlmDdmTable,
       "rm10010arAlmclientSfpAlmDdmEntry": rm10010arAlmclientSfpAlmDdmEntry,
       "rm10010arAlmclientSfpAlmDdmIndex": rm10010arAlmclientSfpAlmDdmIndex,
       "rm10010arAlmTxPwrLowAlaPortn": rm10010arAlmTxPwrLowAlaPortn,
       "rm10010arAlmTxPwrHighAlaPortn": rm10010arAlmTxPwrHighAlaPortn,
       "rm10010arAlmTxBiasLowAlaPortn": rm10010arAlmTxBiasLowAlaPortn,
       "rm10010arAlmTxBiasHighAlaPortn": rm10010arAlmTxBiasHighAlaPortn,
       "rm10010arAlmVccLowAlaPortn": rm10010arAlmVccLowAlaPortn,
       "rm10010arAlmVccHighAlaPortn": rm10010arAlmVccHighAlaPortn,
       "rm10010arAlmTempLowAlaPortn": rm10010arAlmTempLowAlaPortn,
       "rm10010arAlmTempHighAlaPortn": rm10010arAlmTempHighAlaPortn,
       "rm10010arAlmRxPwrLowAlaPortn": rm10010arAlmRxPwrLowAlaPortn,
       "rm10010arAlmRxPwrHighAlaPortn": rm10010arAlmRxPwrHighAlaPortn,
       "rm10010arAlmClientCrit": rm10010arAlmClientCrit,
       "rm10010arAlmsynthAlmPortTable": rm10010arAlmsynthAlmPortTable,
       "rm10010arAlmsynthAlmPortEntry": rm10010arAlmsynthAlmPortEntry,
       "rm10010arAlmsynthAlmPortIndex": rm10010arAlmsynthAlmPortIndex,
       "rm10010arAlmSfpAbsentPortn": rm10010arAlmSfpAbsentPortn,
       "rm10010arAlmDdmAbsentPortn": rm10010arAlmDdmAbsentPortn,
       "rm10010arAlmHwFailAccPortn": rm10010arAlmHwFailAccPortn,
       "rm10010arAlmDwLsdPortn": rm10010arAlmDwLsdPortn,
       "rm10010arAlmClientLocalOosPortn": rm10010arAlmClientLocalOosPortn,
       "rm10010arAlmClientRemoteOosPortn": rm10010arAlmClientRemoteOosPortn,
       "rm10010arAlmDwCaisPortn": rm10010arAlmDwCaisPortn,
       "rm10010arAlmSfpDdmWarningPortn": rm10010arAlmSfpDdmWarningPortn,
       "rm10010arAlmSfpDdmAlmPortn": rm10010arAlmSfpDdmAlmPortn,
       "rm10010arAlmFailAccPortn": rm10010arAlmFailAccPortn,
       "rm10010arAlmUpCsfPortn": rm10010arAlmUpCsfPortn,
       "rm10010arAlmLine": rm10010arAlmLine,
       "rm10010arAlmLineNurg": rm10010arAlmLineNurg,
       "rm10010arAlmlineNetworkLaneAlarmWarning1Table": rm10010arAlmlineNetworkLaneAlarmWarning1Table,
       "rm10010arAlmlineNetworkLaneAlarmWarning1Entry": rm10010arAlmlineNetworkLaneAlarmWarning1Entry,
       "rm10010arAlmlineNetworkLaneAlarmWarning1Index": rm10010arAlmlineNetworkLaneAlarmWarning1Index,
       "rm10010arAlmLineRxPowerLowAlarmPortn": rm10010arAlmLineRxPowerLowAlarmPortn,
       "rm10010arAlmLineRxPowerLowWarningPortn": rm10010arAlmLineRxPowerLowWarningPortn,
       "rm10010arAlmLineRxPowerHighWarningPortn": rm10010arAlmLineRxPowerHighWarningPortn,
       "rm10010arAlmLineRxPowerHighAlarmPortn": rm10010arAlmLineRxPowerHighAlarmPortn,
       "rm10010arAlmLineLaserTempLowAlarmPortn": rm10010arAlmLineLaserTempLowAlarmPortn,
       "rm10010arAlmLineLaserTempLowWarningPortn": rm10010arAlmLineLaserTempLowWarningPortn,
       "rm10010arAlmLineLaserTempHighWarningPortn": rm10010arAlmLineLaserTempHighWarningPortn,
       "rm10010arAlmLineLaserTempHighAlarmPortn": rm10010arAlmLineLaserTempHighAlarmPortn,
       "rm10010arAlmLineTxPowerLowAlarmPortn": rm10010arAlmLineTxPowerLowAlarmPortn,
       "rm10010arAlmLineTxPowerLowWarningPortn": rm10010arAlmLineTxPowerLowWarningPortn,
       "rm10010arAlmLineTxPowerHighWarningPortn": rm10010arAlmLineTxPowerHighWarningPortn,
       "rm10010arAlmLineTxPowerHighAlarmPortn": rm10010arAlmLineTxPowerHighAlarmPortn,
       "rm10010arAlmLineBiasLowAlarmPortn": rm10010arAlmLineBiasLowAlarmPortn,
       "rm10010arAlmLineBiasLowWarningPortn": rm10010arAlmLineBiasLowWarningPortn,
       "rm10010arAlmLineBiasHighWarningPortn": rm10010arAlmLineBiasHighWarningPortn,
       "rm10010arAlmLineBiasHighAlarmPortn": rm10010arAlmLineBiasHighAlarmPortn,
       "rm10010arAlmlineNetworkLaneAlarmWarning2Table": rm10010arAlmlineNetworkLaneAlarmWarning2Table,
       "rm10010arAlmlineNetworkLaneAlarmWarning2Entry": rm10010arAlmlineNetworkLaneAlarmWarning2Entry,
       "rm10010arAlmlineNetworkLaneAlarmWarning2Index": rm10010arAlmlineNetworkLaneAlarmWarning2Index,
       "rm10010arAlmTxModulatorBiasLowAlarmPortn": rm10010arAlmTxModulatorBiasLowAlarmPortn,
       "rm10010arAlmTxModulatorBiasLowWarningPortn": rm10010arAlmTxModulatorBiasLowWarningPortn,
       "rm10010arAlmTxModulatorBiasHighWarningPortn": rm10010arAlmTxModulatorBiasHighWarningPortn,
       "rm10010arAlmTxModulatorBiasHighAlarmPortn": rm10010arAlmTxModulatorBiasHighAlarmPortn,
       "rm10010arAlmRxLaserTempLowAlarmPortn": rm10010arAlmRxLaserTempLowAlarmPortn,
       "rm10010arAlmRxLaserTempLowWarningPortn": rm10010arAlmRxLaserTempLowWarningPortn,
       "rm10010arAlmRxLaserTempHighWarningPortn": rm10010arAlmRxLaserTempHighWarningPortn,
       "rm10010arAlmRxLaserTempHighAlarmPortn": rm10010arAlmRxLaserTempHighAlarmPortn,
       "rm10010arAlmRxLaserOutputLowAlarmPortn": rm10010arAlmRxLaserOutputLowAlarmPortn,
       "rm10010arAlmRxLaserOutputLowWarningPortn": rm10010arAlmRxLaserOutputLowWarningPortn,
       "rm10010arAlmRxLaserOutputHighWarningPortn": rm10010arAlmRxLaserOutputHighWarningPortn,
       "rm10010arAlmRxLaserOutputHighAlarmPortn": rm10010arAlmRxLaserOutputHighAlarmPortn,
       "rm10010arAlmRxLaserBiasLowAlarmPortn": rm10010arAlmRxLaserBiasLowAlarmPortn,
       "rm10010arAlmRxLaserBiasLowWarningPortn": rm10010arAlmRxLaserBiasLowWarningPortn,
       "rm10010arAlmRxLaserBiasHighWarningPortn": rm10010arAlmRxLaserBiasHighWarningPortn,
       "rm10010arAlmRxLaserBiasHighAlarmPortn": rm10010arAlmRxLaserBiasHighAlarmPortn,
       "rm10010arAlmLineUrg": rm10010arAlmLineUrg,
       "rm10010arAlmlineNetworkLaneFaultTable": rm10010arAlmlineNetworkLaneFaultTable,
       "rm10010arAlmlineNetworkLaneFaultEntry": rm10010arAlmlineNetworkLaneFaultEntry,
       "rm10010arAlmlineNetworkLaneFaultIndex": rm10010arAlmlineNetworkLaneFaultIndex,
       "rm10010arAlmLineLaneRxTecFaultPortn": rm10010arAlmLineLaneRxTecFaultPortn,
       "rm10010arAlmLineLaneRxFifoErrorPortn": rm10010arAlmLineLaneRxFifoErrorPortn,
       "rm10010arAlmLineLaneRxLolPortn": rm10010arAlmLineLaneRxLolPortn,
       "rm10010arAlmLineLaneRxLosPortn": rm10010arAlmLineLaneRxLosPortn,
       "rm10010arAlmLineLaneTxLolPortn": rm10010arAlmLineLaneTxLolPortn,
       "rm10010arAlmLineLaneTxLosfPortn": rm10010arAlmLineLaneTxLosfPortn,
       "rm10010arAlmLineLaneApdPowerSupplyPortn": rm10010arAlmLineLaneApdPowerSupplyPortn,
       "rm10010arAlmLineLaneWavelengthUnlockedPortn": rm10010arAlmLineLaneWavelengthUnlockedPortn,
       "rm10010arAlmLineLaneTecFaultPortn": rm10010arAlmLineLaneTecFaultPortn,
       "rm10010arAlmlineHostLaneFaultTable": rm10010arAlmlineHostLaneFaultTable,
       "rm10010arAlmlineHostLaneFaultEntry": rm10010arAlmlineHostLaneFaultEntry,
       "rm10010arAlmlineHostLaneFaultIndex": rm10010arAlmlineHostLaneFaultIndex,
       "rm10010arAlmLineInputLossOfSignalPortn": rm10010arAlmLineInputLossOfSignalPortn,
       "rm10010arAlmLineLossOfFramePortn": rm10010arAlmLineLossOfFramePortn,
       "rm10010arAlmLineSmBdiInsertedPortn": rm10010arAlmLineSmBdiInsertedPortn,
       "rm10010arAlmLineSmBdiDetectedPortn": rm10010arAlmLineSmBdiDetectedPortn,
       "rm10010arAlmLineSmIaeInsertedPortn": rm10010arAlmLineSmIaeInsertedPortn,
       "rm10010arAlmLineSmIaeDetectedPortn": rm10010arAlmLineSmIaeDetectedPortn,
       "rm10010arAlmLineTxHostLolPortn": rm10010arAlmLineTxHostLolPortn,
       "rm10010arAlmLineLaneTxFifoErrorPortn": rm10010arAlmLineLaneTxFifoErrorPortn,
       "rm10010arAlmlineNetworkLaneRxOtnTable": rm10010arAlmlineNetworkLaneRxOtnTable,
       "rm10010arAlmlineNetworkLaneRxOtnEntry": rm10010arAlmlineNetworkLaneRxOtnEntry,
       "rm10010arAlmlineNetworkLaneRxOtnIndex": rm10010arAlmlineNetworkLaneRxOtnIndex,
       "rm10010arAlmLineRxOtnOduAisPortn": rm10010arAlmLineRxOtnOduAisPortn,
       "rm10010arAlmLineRxOtnOtuAisPortn": rm10010arAlmLineRxOtnOtuAisPortn,
       "rm10010arAlmLineRxSmBdiPortn": rm10010arAlmLineRxSmBdiPortn,
       "rm10010arAlmLineRxOtnIaePortn": rm10010arAlmLineRxOtnIaePortn,
       "rm10010arAlmLineRxOtnOomPortn": rm10010arAlmLineRxOtnOomPortn,
       "rm10010arAlmLineRxOtnLomPortn": rm10010arAlmLineRxOtnLomPortn,
       "rm10010arAlmLineRxOtnOofPortn": rm10010arAlmLineRxOtnOofPortn,
       "rm10010arAlmLineRxOtnLofPortn": rm10010arAlmLineRxOtnLofPortn,
       "rm10010arAlmlineHostLaneTxOtnTable": rm10010arAlmlineHostLaneTxOtnTable,
       "rm10010arAlmlineHostLaneTxOtnEntry": rm10010arAlmlineHostLaneTxOtnEntry,
       "rm10010arAlmlineHostLaneTxOtnIndex": rm10010arAlmlineHostLaneTxOtnIndex,
       "rm10010arAlmLineTxOtnOduAisPortn": rm10010arAlmLineTxOtnOduAisPortn,
       "rm10010arAlmLineTxOtnOtuAisPortn": rm10010arAlmLineTxOtnOtuAisPortn,
       "rm10010arAlmLineTxSmBdiPortn": rm10010arAlmLineTxSmBdiPortn,
       "rm10010arAlmLineTxOtnIaePortn": rm10010arAlmLineTxOtnIaePortn,
       "rm10010arAlmLineTxOtnOomPortn": rm10010arAlmLineTxOtnOomPortn,
       "rm10010arAlmLineTxOtnLomPortn": rm10010arAlmLineTxOtnLomPortn,
       "rm10010arAlmLineTxOtnOofPortn": rm10010arAlmLineTxOtnOofPortn,
       "rm10010arAlmLineTxOtnLofPortn": rm10010arAlmLineTxOtnLofPortn,
       "rm10010arAlmLineCrit": rm10010arAlmLineCrit,
       "rm10010arAlmsynthAlmLineTable": rm10010arAlmsynthAlmLineTable,
       "rm10010arAlmsynthAlmLineEntry": rm10010arAlmsynthAlmLineEntry,
       "rm10010arAlmsynthAlmLineIndex": rm10010arAlmsynthAlmLineIndex,
       "rm10010arAlmXfpAbsentPortn": rm10010arAlmXfpAbsentPortn,
       "rm10010arAlmXfpInitNotComplPortn": rm10010arAlmXfpInitNotComplPortn,
       "rm10010arAlmLineHwFailPortn": rm10010arAlmLineHwFailPortn,
       "rm10010arAlmXfpTxOffPortn": rm10010arAlmXfpTxOffPortn,
       "rm10010arAlmLineLocalOosPortn": rm10010arAlmLineLocalOosPortn,
       "rm10010arAlmUpRdiInsPortn": rm10010arAlmUpRdiInsPortn,
       "rm10010arAlmLineDdmWarningPortn": rm10010arAlmLineDdmWarningPortn,
       "rm10010arAlmLineDdmAlmPortn": rm10010arAlmLineDdmAlmPortn,
       "rm10010arAlmLineFailPortn": rm10010arAlmLineFailPortn,
       "rm10010arAlmLineActivePortn": rm10010arAlmLineActivePortn,
       "rm10010armeasures": rm10010armeasures,
       "rm10010arMesrOther": rm10010arMesrOther,
       "rm10010arMesrsynth0": rm10010arMesrsynth0,
       "rm10010arMesrsynth1": rm10010arMesrsynth1,
       "rm10010arMesrpmIntervalNumber": rm10010arMesrpmIntervalNumber,
       "rm10010arMesrlineNetTxLaserOutputPwrAverage": rm10010arMesrlineNetTxLaserOutputPwrAverage,
       "rm10010arMesrlineNetTxLaserTempAverage": rm10010arMesrlineNetTxLaserTempAverage,
       "rm10010arMesrlineNetTxBiasCurrentAverage": rm10010arMesrlineNetTxBiasCurrentAverage,
       "rm10010arMesrlineNetRxInputPwrAverage": rm10010arMesrlineNetRxInputPwrAverage,
       "rm10010arMesrlineResidualChromaticDispAverage": rm10010arMesrlineResidualChromaticDispAverage,
       "rm10010arMesrlineDiffGroupDelayAverage": rm10010arMesrlineDiffGroupDelayAverage,
       "rm10010arMesrlineQFactorAverage": rm10010arMesrlineQFactorAverage,
       "rm10010arMesrlineCarrierFreqOffsetAverage": rm10010arMesrlineCarrierFreqOffsetAverage,
       "rm10010arMesrlineOsnrAverage": rm10010arMesrlineOsnrAverage,
       "rm10010arMesrclientNetTxTempMin": rm10010arMesrclientNetTxTempMin,
       "rm10010arMesrclientNetTxBiasMin": rm10010arMesrclientNetTxBiasMin,
       "rm10010arMesrclientNetTxPwrMin": rm10010arMesrclientNetTxPwrMin,
       "rm10010arMesrclientNetRxPwrMin": rm10010arMesrclientNetRxPwrMin,
       "rm10010arMesrlineNetTxLaserOutputPwrMin": rm10010arMesrlineNetTxLaserOutputPwrMin,
       "rm10010arMesrlineNetTxLaserTempMin": rm10010arMesrlineNetTxLaserTempMin,
       "rm10010arMesrlineNetTxBiasCurrentMin": rm10010arMesrlineNetTxBiasCurrentMin,
       "rm10010arMesrlineNetRxInputPwrMin": rm10010arMesrlineNetRxInputPwrMin,
       "rm10010arMesrlineResidualChromaticDispMin": rm10010arMesrlineResidualChromaticDispMin,
       "rm10010arMesrlineDiffGroupDelayMin": rm10010arMesrlineDiffGroupDelayMin,
       "rm10010arMesrlineQFactorMin": rm10010arMesrlineQFactorMin,
       "rm10010arMesrlineCarrierFreqOffsetMin": rm10010arMesrlineCarrierFreqOffsetMin,
       "rm10010arMesrlineOsnrMin": rm10010arMesrlineOsnrMin,
       "rm10010arMesrclientNetTxTempMax": rm10010arMesrclientNetTxTempMax,
       "rm10010arMesrclientNetTxBiasMax": rm10010arMesrclientNetTxBiasMax,
       "rm10010arMesrclientNetTxPwrMax": rm10010arMesrclientNetTxPwrMax,
       "rm10010arMesrclientNetRxPwrMax": rm10010arMesrclientNetRxPwrMax,
       "rm10010arMesrlineNetTxLaserOutputPwrMax": rm10010arMesrlineNetTxLaserOutputPwrMax,
       "rm10010arMesrlineNetTxLaserTempMax": rm10010arMesrlineNetTxLaserTempMax,
       "rm10010arMesrlineNetTxBiasCurrentMax": rm10010arMesrlineNetTxBiasCurrentMax,
       "rm10010arMesrlineNetRxInputPwrMax": rm10010arMesrlineNetRxInputPwrMax,
       "rm10010arMesrlineResidualChromaticDispMax": rm10010arMesrlineResidualChromaticDispMax,
       "rm10010arMesrlineDiffGroupDelayMax": rm10010arMesrlineDiffGroupDelayMax,
       "rm10010arMesrlineQFactorMax": rm10010arMesrlineQFactorMax,
       "rm10010arMesrlineCarrierFreqOffsetMax": rm10010arMesrlineCarrierFreqOffsetMax,
       "rm10010arMesrlineOsnrMax": rm10010arMesrlineOsnrMax,
       "rm10010arMesrClient": rm10010arMesrClient,
       "rm10010arMesrclientCfpTemp": rm10010arMesrclientCfpTemp,
       "rm10010arMesrclientCfp3v3Voltage": rm10010arMesrclientCfp3v3Voltage,
       "rm10010arMesrclientSoaBiasCurrent": rm10010arMesrclientSoaBiasCurrent,
       "rm10010arMesrclientNetTxTempTable": rm10010arMesrclientNetTxTempTable,
       "rm10010arMesrclientNetTxTempEntry": rm10010arMesrclientNetTxTempEntry,
       "rm10010arMesrclientNetTxTempIndex": rm10010arMesrclientNetTxTempIndex,
       "rm10010arMesrclientNetTxTempPortn": rm10010arMesrclientNetTxTempPortn,
       "rm10010arMesrclientNetTxBiasTable": rm10010arMesrclientNetTxBiasTable,
       "rm10010arMesrclientNetTxBiasEntry": rm10010arMesrclientNetTxBiasEntry,
       "rm10010arMesrclientNetTxBiasIndex": rm10010arMesrclientNetTxBiasIndex,
       "rm10010arMesrclientNetTxBiasPortn": rm10010arMesrclientNetTxBiasPortn,
       "rm10010arMesrclientNetTxPwrTable": rm10010arMesrclientNetTxPwrTable,
       "rm10010arMesrclientNetTxPwrEntry": rm10010arMesrclientNetTxPwrEntry,
       "rm10010arMesrclientNetTxPwrIndex": rm10010arMesrclientNetTxPwrIndex,
       "rm10010arMesrclientNetTxPwrPortn": rm10010arMesrclientNetTxPwrPortn,
       "rm10010arMesrclientNetRxPwrTable": rm10010arMesrclientNetRxPwrTable,
       "rm10010arMesrclientNetRxPwrEntry": rm10010arMesrclientNetRxPwrEntry,
       "rm10010arMesrclientNetRxPwrIndex": rm10010arMesrclientNetRxPwrIndex,
       "rm10010arMesrclientNetRxPwrPortn": rm10010arMesrclientNetRxPwrPortn,
       "rm10010arMesrLine": rm10010arMesrLine,
       "rm10010arMesrlineMsaTemp": rm10010arMesrlineMsaTemp,
       "rm10010arMesrlineMsa3v3Voltage": rm10010arMesrlineMsa3v3Voltage,
       "rm10010arMesrlineSoaBiasCurrent": rm10010arMesrlineSoaBiasCurrent,
       "rm10010arMesrlineNetTxLaserOutputPwrTable": rm10010arMesrlineNetTxLaserOutputPwrTable,
       "rm10010arMesrlineNetTxLaserOutputPwrEntry": rm10010arMesrlineNetTxLaserOutputPwrEntry,
       "rm10010arMesrlineNetTxLaserOutputPwrIndex": rm10010arMesrlineNetTxLaserOutputPwrIndex,
       "rm10010arMesrlineNetTxLaserOutputPwrPortn": rm10010arMesrlineNetTxLaserOutputPwrPortn,
       "rm10010arMesrlineNetTxLaserTempTable": rm10010arMesrlineNetTxLaserTempTable,
       "rm10010arMesrlineNetTxLaserTempEntry": rm10010arMesrlineNetTxLaserTempEntry,
       "rm10010arMesrlineNetTxLaserTempIndex": rm10010arMesrlineNetTxLaserTempIndex,
       "rm10010arMesrlineNetTxLaserTempPortn": rm10010arMesrlineNetTxLaserTempPortn,
       "rm10010arMesrlineNetTxBiasCurrentTable": rm10010arMesrlineNetTxBiasCurrentTable,
       "rm10010arMesrlineNetTxBiasCurrentEntry": rm10010arMesrlineNetTxBiasCurrentEntry,
       "rm10010arMesrlineNetTxBiasCurrentIndex": rm10010arMesrlineNetTxBiasCurrentIndex,
       "rm10010arMesrlineNetTxBiasCurrentPortn": rm10010arMesrlineNetTxBiasCurrentPortn,
       "rm10010arMesrlineNetRxInputPwrTable": rm10010arMesrlineNetRxInputPwrTable,
       "rm10010arMesrlineNetRxInputPwrEntry": rm10010arMesrlineNetRxInputPwrEntry,
       "rm10010arMesrlineNetRxInputPwrIndex": rm10010arMesrlineNetRxInputPwrIndex,
       "rm10010arMesrlineNetRxInputPwrPortn": rm10010arMesrlineNetRxInputPwrPortn,
       "rm10010arMesrlineResidualChromaticDispTable": rm10010arMesrlineResidualChromaticDispTable,
       "rm10010arMesrlineResidualChromaticDispEntry": rm10010arMesrlineResidualChromaticDispEntry,
       "rm10010arMesrlineResidualChromaticDispIndex": rm10010arMesrlineResidualChromaticDispIndex,
       "rm10010arMesrlineResidualChromaticDispPortn": rm10010arMesrlineResidualChromaticDispPortn,
       "rm10010arMesrlineDiffGroupDelayTable": rm10010arMesrlineDiffGroupDelayTable,
       "rm10010arMesrlineDiffGroupDelayEntry": rm10010arMesrlineDiffGroupDelayEntry,
       "rm10010arMesrlineDiffGroupDelayIndex": rm10010arMesrlineDiffGroupDelayIndex,
       "rm10010arMesrlineDiffGroupDelayPortn": rm10010arMesrlineDiffGroupDelayPortn,
       "rm10010arMesrlineQFactorTable": rm10010arMesrlineQFactorTable,
       "rm10010arMesrlineQFactorEntry": rm10010arMesrlineQFactorEntry,
       "rm10010arMesrlineQFactorIndex": rm10010arMesrlineQFactorIndex,
       "rm10010arMesrlineQFactorPortn": rm10010arMesrlineQFactorPortn,
       "rm10010arMesrlineCarrierFreqOffsetTable": rm10010arMesrlineCarrierFreqOffsetTable,
       "rm10010arMesrlineCarrierFreqOffsetEntry": rm10010arMesrlineCarrierFreqOffsetEntry,
       "rm10010arMesrlineCarrierFreqOffsetIndex": rm10010arMesrlineCarrierFreqOffsetIndex,
       "rm10010arMesrlineCarrierFreqOffsetPortn": rm10010arMesrlineCarrierFreqOffsetPortn,
       "rm10010arMesrlineOsnrTable": rm10010arMesrlineOsnrTable,
       "rm10010arMesrlineOsnrEntry": rm10010arMesrlineOsnrEntry,
       "rm10010arMesrlineOsnrIndex": rm10010arMesrlineOsnrIndex,
       "rm10010arMesrlineOsnrPortn": rm10010arMesrlineOsnrPortn,
       "rm10010arcounters": rm10010arcounters,
       "rm10010arCntOther": rm10010arCntOther,
       "rm10010arCntClient": rm10010arCntClient,
       "rm10010arCntclientInputErrorCounterLaneOneTable": rm10010arCntclientInputErrorCounterLaneOneTable,
       "rm10010arCntclientInputErrorCounterLaneOneEntry": rm10010arCntclientInputErrorCounterLaneOneEntry,
       "rm10010arCntclientInputErrorCounterLaneOneIndex": rm10010arCntclientInputErrorCounterLaneOneIndex,
       "rm10010arCntclientInputErrorCounterLaneOneValuePortn": rm10010arCntclientInputErrorCounterLaneOneValuePortn,
       "rm10010arCntclientInputErrorCounterLaneOneErrorPortn": rm10010arCntclientInputErrorCounterLaneOneErrorPortn,
       "rm10010arCntclientInputErrorCounterLaneOneOverloadPortn": rm10010arCntclientInputErrorCounterLaneOneOverloadPortn,
       "rm10010arCntclientInputErrorCounterLaneTwoTable": rm10010arCntclientInputErrorCounterLaneTwoTable,
       "rm10010arCntclientInputErrorCounterLaneTwoEntry": rm10010arCntclientInputErrorCounterLaneTwoEntry,
       "rm10010arCntclientInputErrorCounterLaneTwoIndex": rm10010arCntclientInputErrorCounterLaneTwoIndex,
       "rm10010arCntclientInputErrorCounterLaneTwoValuePortn": rm10010arCntclientInputErrorCounterLaneTwoValuePortn,
       "rm10010arCntclientInputErrorCounterLaneTwoErrorPortn": rm10010arCntclientInputErrorCounterLaneTwoErrorPortn,
       "rm10010arCntclientInputErrorCounterLaneTwoOverloadPortn": rm10010arCntclientInputErrorCounterLaneTwoOverloadPortn,
       "rm10010arCntclientInputErrorCounterTable": rm10010arCntclientInputErrorCounterTable,
       "rm10010arCntclientInputErrorCounterEntry": rm10010arCntclientInputErrorCounterEntry,
       "rm10010arCntclientInputErrorCounterIndex": rm10010arCntclientInputErrorCounterIndex,
       "rm10010arCntclientInputErrorCounterValuePortn": rm10010arCntclientInputErrorCounterValuePortn,
       "rm10010arCntclientInputErrorCounterErrorPortn": rm10010arCntclientInputErrorCounterErrorPortn,
       "rm10010arCntclientInputErrorCounterOverloadPortn": rm10010arCntclientInputErrorCounterOverloadPortn,
       "rm10010arCntclientCbipCounterTable": rm10010arCntclientCbipCounterTable,
       "rm10010arCntclientCbipCounterEntry": rm10010arCntclientCbipCounterEntry,
       "rm10010arCntclientCbipCounterIndex": rm10010arCntclientCbipCounterIndex,
       "rm10010arCntclientCbipCounterValuePortn": rm10010arCntclientCbipCounterValuePortn,
       "rm10010arCntclientCbipCounterErrorPortn": rm10010arCntclientCbipCounterErrorPortn,
       "rm10010arCntclientCbipCounterOverloadPortn": rm10010arCntclientCbipCounterOverloadPortn,
       "rm10010arCntLine": rm10010arCntLine,
       "rm10010arCntlocalLineSmBip8ErrorCounterTable": rm10010arCntlocalLineSmBip8ErrorCounterTable,
       "rm10010arCntlocalLineSmBip8ErrorCounterEntry": rm10010arCntlocalLineSmBip8ErrorCounterEntry,
       "rm10010arCntlocalLineSmBip8ErrorCounterIndex": rm10010arCntlocalLineSmBip8ErrorCounterIndex,
       "rm10010arCntlocalLineSmBip8ErrorCounterValuePortn": rm10010arCntlocalLineSmBip8ErrorCounterValuePortn,
       "rm10010arCntlocalLineSmBip8ErrorCounterErrorPortn": rm10010arCntlocalLineSmBip8ErrorCounterErrorPortn,
       "rm10010arCntlocalLineSmBip8ErrorCounterOverloadPortn": rm10010arCntlocalLineSmBip8ErrorCounterOverloadPortn,
       "rm10010arCntlocalLineFecCorrectedErrorsCounterTable": rm10010arCntlocalLineFecCorrectedErrorsCounterTable,
       "rm10010arCntlocalLineFecCorrectedErrorsCounterEntry": rm10010arCntlocalLineFecCorrectedErrorsCounterEntry,
       "rm10010arCntlocalLineFecCorrectedErrorsCounterIndex": rm10010arCntlocalLineFecCorrectedErrorsCounterIndex,
       "rm10010arCntlocalLineFecCorrectedErrorsCounterValuePortn": rm10010arCntlocalLineFecCorrectedErrorsCounterValuePortn,
       "rm10010arCntlocalLineFecCorrectedErrorsCounterErrorPortn": rm10010arCntlocalLineFecCorrectedErrorsCounterErrorPortn,
       "rm10010arCntlocalLineFecCorrectedErrorsCounterOverloadPortn": rm10010arCntlocalLineFecCorrectedErrorsCounterOverloadPortn,
       "rm10010arCntremoteLineSmBip8ErrorCounterTable": rm10010arCntremoteLineSmBip8ErrorCounterTable,
       "rm10010arCntremoteLineSmBip8ErrorCounterEntry": rm10010arCntremoteLineSmBip8ErrorCounterEntry,
       "rm10010arCntremoteLineSmBip8ErrorCounterIndex": rm10010arCntremoteLineSmBip8ErrorCounterIndex,
       "rm10010arCntremoteLineSmBip8ErrorCounterValuePortn": rm10010arCntremoteLineSmBip8ErrorCounterValuePortn,
       "rm10010arCntremoteLineSmBip8ErrorCounterErrorPortn": rm10010arCntremoteLineSmBip8ErrorCounterErrorPortn,
       "rm10010arCntremoteLineSmBip8ErrorCounterOverloadPortn": rm10010arCntremoteLineSmBip8ErrorCounterOverloadPortn,
       "rm10010arCntlineDfrmTimCntTable": rm10010arCntlineDfrmTimCntTable,
       "rm10010arCntlineDfrmTimCntEntry": rm10010arCntlineDfrmTimCntEntry,
       "rm10010arCntlineDfrmTimCntIndex": rm10010arCntlineDfrmTimCntIndex,
       "rm10010arCntlineDfrmTimCntValuePortn": rm10010arCntlineDfrmTimCntValuePortn,
       "rm10010arCntlineDfrmTimCntErrorPortn": rm10010arCntlineDfrmTimCntErrorPortn,
       "rm10010arCntlineDfrmTimCntOverloadPortn": rm10010arCntlineDfrmTimCntOverloadPortn,
       "rm10010arCntlocalLineTrscvFecCorrectedErrorCounterTable": rm10010arCntlocalLineTrscvFecCorrectedErrorCounterTable,
       "rm10010arCntlocalLineTrscvFecCorrectedErrorCounterEntry": rm10010arCntlocalLineTrscvFecCorrectedErrorCounterEntry,
       "rm10010arCntlocalLineTrscvFecCorrectedErrorCounterIndex": rm10010arCntlocalLineTrscvFecCorrectedErrorCounterIndex,
       "rm10010arCntlocalLineTrscvFecCorrectedErrorCounterValuePortn": rm10010arCntlocalLineTrscvFecCorrectedErrorCounterValuePortn,
       "rm10010arCntlocalLineTrscvFecCorrectedErrorCounterErrorPortn": rm10010arCntlocalLineTrscvFecCorrectedErrorCounterErrorPortn,
       "rm10010arCntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn": rm10010arCntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn,
       "rm10010arCntlocalLineTrscvFecUncorrectedErrorCounterTable": rm10010arCntlocalLineTrscvFecUncorrectedErrorCounterTable,
       "rm10010arCntlocalLineTrscvFecUncorrectedErrorCounterEntry": rm10010arCntlocalLineTrscvFecUncorrectedErrorCounterEntry,
       "rm10010arCntlocalLineTrscvFecUncorrectedErrorCounterIndex": rm10010arCntlocalLineTrscvFecUncorrectedErrorCounterIndex,
       "rm10010arCntlocalLineTrscvFecUncorrectedErrorCounterValuePortn": rm10010arCntlocalLineTrscvFecUncorrectedErrorCounterValuePortn,
       "rm10010arCntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn": rm10010arCntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn,
       "rm10010arCntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn": rm10010arCntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn,
       "rm10010arcontrolsWrite": rm10010arcontrolsWrite,
       "rm10010arCtrlOther": rm10010arCtrlOther,
       "rm10010arCtrlconfMgnt1": rm10010arCtrlconfMgnt1,
       "rm10010arCtrlConf1Load1": rm10010arCtrlConf1Load1,
       "rm10010arCtrlConf2Load1": rm10010arCtrlConf2Load1,
       "rm10010arCtrlConf2Flash1": rm10010arCtrlConf2Flash1,
       "rm10010arCtrlConf2Clear1": rm10010arCtrlConf2Clear1,
       "rm10010arCtrlsynth4": rm10010arCtrlsynth4,
       "rm10010arCtrlCorrelatOn": rm10010arCtrlCorrelatOn,
       "rm10010arCtrlCorrelatOff": rm10010arCtrlCorrelatOff,
       "rm10010arCtrlswMgnt": rm10010arCtrlswMgnt,
       "rm10010arCtrlColdReset": rm10010arCtrlColdReset,
       "rm10010arCtrlWarmReset": rm10010arCtrlWarmReset,
       "rm10010arCtrlLoadSwBank1": rm10010arCtrlLoadSwBank1,
       "rm10010arCtrlLoadSwBank2": rm10010arCtrlLoadSwBank2,
       "rm10010arCtrlgwMgnt": rm10010arCtrlgwMgnt,
       "rm10010arCtrlCurrentGwReset": rm10010arCtrlCurrentGwReset,
       "rm10010arCtrlLoadGwBank1": rm10010arCtrlLoadGwBank1,
       "rm10010arCtrlLoadGwBank2": rm10010arCtrlLoadGwBank2,
       "rm10010arCtrlLoadGwBank3": rm10010arCtrlLoadGwBank3,
       "rm10010arCtrlLoadGwBank4": rm10010arCtrlLoadGwBank4,
       "rm10010arCtrlledTest": rm10010arCtrlledTest,
       "rm10010arCtrlGreenLed": rm10010arCtrlGreenLed,
       "rm10010arCtrlRedLed": rm10010arCtrlRedLed,
       "rm10010arCtrlLedOff": rm10010arCtrlLedOff,
       "rm10010arCtrlinitSwitchMarvell": rm10010arCtrlinitSwitchMarvell,
       "rm10010arCtrlInitSwitchMarvell": rm10010arCtrlInitSwitchMarvell,
       "rm10010arCtrlresetCount": rm10010arCtrlresetCount,
       "rm10010arCtrlResetcount": rm10010arCtrlResetcount,
       "rm10010arCtrlresetRmon": rm10010arCtrlresetRmon,
       "rm10010arCtrlResetrmon": rm10010arCtrlResetrmon,
       "rm10010arCtrlresetMeasurements": rm10010arCtrlresetMeasurements,
       "rm10010arCtrlResetmeasurements": rm10010arCtrlResetmeasurements,
       "rm10010arCtrlClient": rm10010arCtrlClient,
       "rm10010arCtrlaccessLoopTable": rm10010arCtrlaccessLoopTable,
       "rm10010arCtrlaccessLoopEntry": rm10010arCtrlaccessLoopEntry,
       "rm10010arCtrlaccessLoopIndex": rm10010arCtrlaccessLoopIndex,
       "rm10010arCtrlaccessLoopPortn": rm10010arCtrlaccessLoopPortn,
       "rm10010arCtrlclientLoopToLineTable": rm10010arCtrlclientLoopToLineTable,
       "rm10010arCtrlclientLoopToLineEntry": rm10010arCtrlclientLoopToLineEntry,
       "rm10010arCtrlclientLoopToLineIndex": rm10010arCtrlclientLoopToLineIndex,
       "rm10010arCtrlclientLoopToLinePortn": rm10010arCtrlclientLoopToLinePortn,
       "rm10010arCtrlcsfUpInsTable": rm10010arCtrlcsfUpInsTable,
       "rm10010arCtrlcsfUpInsEntry": rm10010arCtrlcsfUpInsEntry,
       "rm10010arCtrlcsfUpInsIndex": rm10010arCtrlcsfUpInsIndex,
       "rm10010arCtrlcsfUpInsPortn": rm10010arCtrlcsfUpInsPortn,
       "rm10010arCtrlcaisDwInsTable": rm10010arCtrlcaisDwInsTable,
       "rm10010arCtrlcaisDwInsEntry": rm10010arCtrlcaisDwInsEntry,
       "rm10010arCtrlcaisDwInsIndex": rm10010arCtrlcaisDwInsIndex,
       "rm10010arCtrlcaisDwInsPortn": rm10010arCtrlcaisDwInsPortn,
       "rm10010arCtrlLine": rm10010arCtrlLine,
       "rm10010arCtrlcommAccessLoopTable": rm10010arCtrlcommAccessLoopTable,
       "rm10010arCtrlcommAccessLoopEntry": rm10010arCtrlcommAccessLoopEntry,
       "rm10010arCtrlcommAccessLoopIndex": rm10010arCtrlcommAccessLoopIndex,
       "rm10010arCtrlcommAccessLoopPortn": rm10010arCtrlcommAccessLoopPortn,
       "rm10010arCtrllineLoopTable": rm10010arCtrllineLoopTable,
       "rm10010arCtrllineLoopEntry": rm10010arCtrllineLoopEntry,
       "rm10010arCtrllineLoopIndex": rm10010arCtrllineLoopIndex,
       "rm10010arCtrllineLoopPortn": rm10010arCtrllineLoopPortn,
       "rm10010arCtrlfecDisableTable": rm10010arCtrlfecDisableTable,
       "rm10010arCtrlfecDisableEntry": rm10010arCtrlfecDisableEntry,
       "rm10010arCtrlfecDisableIndex": rm10010arCtrlfecDisableIndex,
       "rm10010arCtrlfecDisablePortn": rm10010arCtrlfecDisablePortn,
       "rm10010arCtrlmsaLineLoopTable": rm10010arCtrlmsaLineLoopTable,
       "rm10010arCtrlmsaLineLoopEntry": rm10010arCtrlmsaLineLoopEntry,
       "rm10010arCtrlmsaLineLoopIndex": rm10010arCtrlmsaLineLoopIndex,
       "rm10010arCtrlmsaLineLoopPortn": rm10010arCtrlmsaLineLoopPortn,
       "rm10010arCtrlmsaTxResetTable": rm10010arCtrlmsaTxResetTable,
       "rm10010arCtrlmsaTxResetEntry": rm10010arCtrlmsaTxResetEntry,
       "rm10010arCtrlmsaTxResetIndex": rm10010arCtrlmsaTxResetIndex,
       "rm10010arCtrlmsaTxResetPortn": rm10010arCtrlmsaTxResetPortn,
       "rm10010arCtrlmsaRxResetTable": rm10010arCtrlmsaRxResetTable,
       "rm10010arCtrlmsaRxResetEntry": rm10010arCtrlmsaRxResetEntry,
       "rm10010arCtrlmsaRxResetIndex": rm10010arCtrlmsaRxResetIndex,
       "rm10010arCtrlmsaRxResetPortn": rm10010arCtrlmsaRxResetPortn,
       "rm10010arCtrlmsaShutdownTable": rm10010arCtrlmsaShutdownTable,
       "rm10010arCtrlmsaShutdownEntry": rm10010arCtrlmsaShutdownEntry,
       "rm10010arCtrlmsaShutdownIndex": rm10010arCtrlmsaShutdownIndex,
       "rm10010arCtrlmsaShutdownPortn": rm10010arCtrlmsaShutdownPortn,
       "rm10010arri": rm10010arri,
       "rm10010arriTable": rm10010arriTable,
       "rm10010arRinvSfpTable": rm10010arRinvSfpTable,
       "rm10010arRinvSfpEntry": rm10010arRinvSfpEntry,
       "rm10010arRinvSfpIndex": rm10010arRinvSfpIndex,
       "rm10010arRinvsfp": rm10010arRinvsfp,
       "rm10010arRinvLineTable": rm10010arRinvLineTable,
       "rm10010arRinvLineEntry": rm10010arRinvLineEntry,
       "rm10010arRinvLineIndex": rm10010arRinvLineIndex,
       "rm10010arRinvxfpLine": rm10010arRinvxfpLine,
       "rm10010arRinvReloadInventory": rm10010arRinvReloadInventory,
       "rm10010arRinvHwPlatform": rm10010arRinvHwPlatform,
       "rm10010arRinvModulePlatform": rm10010arRinvModulePlatform,
       "rm10010arRinvSwPlatform": rm10010arRinvSwPlatform,
       "rm10010arRinvGwPlatform": rm10010arRinvGwPlatform,
       "rm10010ardownload": rm10010ardownload,
       "rm10010arDwlOther": rm10010arDwlOther,
       "rm10010arDwlrestartProcess": rm10010arDwlrestartProcess,
       "rm10010arDwlWarmRestartProcessed": rm10010arDwlWarmRestartProcessed,
       "rm10010arDwlColdRestartProcessed": rm10010arDwlColdRestartProcessed,
       "rm10010arDwlswBanksUsed": rm10010arDwlswBanksUsed,
       "rm10010arDwlSwBank1Used": rm10010arDwlSwBank1Used,
       "rm10010arDwlSwBank2Used": rm10010arDwlSwBank2Used,
       "rm10010arDwlSwBank1Notempty": rm10010arDwlSwBank1Notempty,
       "rm10010arDwlSwBank2Notempty": rm10010arDwlSwBank2Notempty,
       "rm10010arDwlgwBanksUsed": rm10010arDwlgwBanksUsed,
       "rm10010arDwlGwBank1Used": rm10010arDwlGwBank1Used,
       "rm10010arDwlGwBank2Used": rm10010arDwlGwBank2Used,
       "rm10010arDwlGwBank3Used": rm10010arDwlGwBank3Used,
       "rm10010arDwlGwBank4Used": rm10010arDwlGwBank4Used,
       "rm10010arDwlGwBank1Notempty": rm10010arDwlGwBank1Notempty,
       "rm10010arDwlGwBank2Notempty": rm10010arDwlGwBank2Notempty,
       "rm10010arDwlGwBank3Notempty": rm10010arDwlGwBank3Notempty,
       "rm10010arDwlGwBank4Notempty": rm10010arDwlGwBank4Notempty,
       "rm10010arDwlClient": rm10010arDwlClient,
       "rm10010arDwlLine": rm10010arDwlLine,
       "rm10010arConfig": rm10010arConfig,
       "rm10010arCfgAccessCAisCsf": rm10010arCfgAccessCAisCsf,
       "rm10010arCfgClientcaiscsfTable": rm10010arCfgClientcaiscsfTable,
       "rm10010arCfgClientcaiscsfEntry": rm10010arCfgClientcaiscsfEntry,
       "rm10010arCfgClientcaiscsfIndex": rm10010arCfgClientcaiscsfIndex,
       "rm10010arCfgReservePortn": rm10010arCfgReservePortn,
       "rm10010arCfgStartup": rm10010arCfgStartup,
       "rm10010arCfgClientStartupTable": rm10010arCfgClientStartupTable,
       "rm10010arCfgClientStartupEntry": rm10010arCfgClientStartupEntry,
       "rm10010arCfgClientStartupIndex": rm10010arCfgClientStartupIndex,
       "rm10010arCfgSystConfPortPortn": rm10010arCfgSystConfPortPortn,
       "rm10010arCfgNetConfPortPortn": rm10010arCfgNetConfPortPortn,
       "rm10010arCfgOptionsPortPortn": rm10010arCfgOptionsPortPortn,
       "rm10010arCfgLineStartupTable": rm10010arCfgLineStartupTable,
       "rm10010arCfgLineStartupEntry": rm10010arCfgLineStartupEntry,
       "rm10010arCfgLineStartupIndex": rm10010arCfgLineStartupIndex,
       "rm10010arCfgSystConfLinePortn": rm10010arCfgSystConfLinePortn,
       "rm10010arCfgOptionsLinePortn": rm10010arCfgOptionsLinePortn,
       "rm10010arCfgXfpTable": rm10010arCfgXfpTable,
       "rm10010arCfgXfpEntry": rm10010arCfgXfpEntry,
       "rm10010arCfgXfpIndex": rm10010arCfgXfpIndex,
       "rm10010arCfgSystConfMsaLinePortn": rm10010arCfgSystConfMsaLinePortn,
       "rm10010arCfgLabels": rm10010arCfgLabels,
       "rm10010arCfgLabelclientTable": rm10010arCfgLabelclientTable,
       "rm10010arCfgLabelclientEntry": rm10010arCfgLabelclientEntry,
       "rm10010arCfgLabelclientIndex": rm10010arCfgLabelclientIndex,
       "rm10010arCfgLabelclientPortn": rm10010arCfgLabelclientPortn,
       "rm10010arCfgLabellineTable": rm10010arCfgLabellineTable,
       "rm10010arCfgLabellineEntry": rm10010arCfgLabellineEntry,
       "rm10010arCfgLabellineIndex": rm10010arCfgLabellineIndex,
       "rm10010arCfgLabellinePortn": rm10010arCfgLabellinePortn,
       "rm10010arCfgStartuptlh": rm10010arCfgStartuptlh,
       "rm10010arCfgOtxtlhTable": rm10010arCfgOtxtlhTable,
       "rm10010arCfgOtxtlhEntry": rm10010arCfgOtxtlhEntry,
       "rm10010arCfgOtxtlhIndex": rm10010arCfgOtxtlhIndex,
       "rm10010arCfgLinePwrLaserPortn": rm10010arCfgLinePwrLaserPortn,
       "rm10010arCfgLineFCurrentPortn": rm10010arCfgLineFCurrentPortn,
       "rm10010arCfgLineGridCurrentPortn": rm10010arCfgLineGridCurrentPortn,
       "rm10010arCfgRxLineFCurrentPortn": rm10010arCfgRxLineFCurrentPortn,
       "rm10010arCfgOther": rm10010arCfgOther,
       "rm10010artablemoduleOther": rm10010artablemoduleOther,
       "rm10010arCfgmode": rm10010arCfgmode,
       "rm10010arCfgfanLowSpeedThreshold": rm10010arCfgfanLowSpeedThreshold,
       "rm10010arCfgfanHighSpeedThreshold": rm10010arCfgfanHighSpeedThreshold,
       "rm10010arCfgWriteConfiguration": rm10010arCfgWriteConfiguration,
       "rm10010artraps": rm10010artraps,
       "rm10010artrapPortNumber": rm10010artrapPortNumber,
       "rm10010artrapLineNumber": rm10010artrapLineNumber,
       "rm10010artrapBoardNumber": rm10010artrapBoardNumber,
       "rm10010arLineTrapNotUrgentGoesOn": rm10010arLineTrapNotUrgentGoesOn,
       "rm10010arLineTrapNotUrgentGoesOff": rm10010arLineTrapNotUrgentGoesOff,
       "rm10010arLineTrapUrgentGoesOn": rm10010arLineTrapUrgentGoesOn,
       "rm10010arLineTrapUrgentGoesOff": rm10010arLineTrapUrgentGoesOff,
       "rm10010arLineTrapCritGoesOn": rm10010arLineTrapCritGoesOn,
       "rm10010arLineTrapCritGoesOff": rm10010arLineTrapCritGoesOff,
       "rm10010arClientTrapNotUrgentGoesOn": rm10010arClientTrapNotUrgentGoesOn,
       "rm10010arClientTrapNotUrgentGoesOff": rm10010arClientTrapNotUrgentGoesOff,
       "rm10010arClientTrapUrgentGoesOn": rm10010arClientTrapUrgentGoesOn,
       "rm10010arClientTrapUrgentGoesOff": rm10010arClientTrapUrgentGoesOff,
       "rm10010arClientTrapCritGoesOn": rm10010arClientTrapCritGoesOn,
       "rm10010arClientTrapCritGoesOff": rm10010arClientTrapCritGoesOff,
       "rm10010arPowerTrapUrgentGoesOn": rm10010arPowerTrapUrgentGoesOn,
       "rm10010arPowerTrapUrgentGoesOff": rm10010arPowerTrapUrgentGoesOff,
       "rm10010arMonitoring": rm10010arMonitoring,
       "rm10010arMonOther": rm10010arMonOther,
       "rm10010arMonRmon": rm10010arMonRmon,
       "rm10010arMonClient": rm10010arMonClient,
       "rm10010arMonClientRmonCounter": rm10010arMonClientRmonCounter,
       "rm10010arMonupRmonBytesCounterClientInputTable": rm10010arMonupRmonBytesCounterClientInputTable,
       "rm10010arMonupRmonBytesCounterClientInputEntry": rm10010arMonupRmonBytesCounterClientInputEntry,
       "rm10010arMonupRmonBytesCounterClientInputIndex": rm10010arMonupRmonBytesCounterClientInputIndex,
       "rm10010arMonupRmonBytesCounterClientInputValuePortn": rm10010arMonupRmonBytesCounterClientInputValuePortn,
       "rm10010arMonupRmonBytesCounterClientInputErrorPortn": rm10010arMonupRmonBytesCounterClientInputErrorPortn,
       "rm10010arMonupRmonBytesCounterClientInputOverloadPortn": rm10010arMonupRmonBytesCounterClientInputOverloadPortn,
       "rm10010arMonupRmonCrcErrorsCounterClientInputTable": rm10010arMonupRmonCrcErrorsCounterClientInputTable,
       "rm10010arMonupRmonCrcErrorsCounterClientInputEntry": rm10010arMonupRmonCrcErrorsCounterClientInputEntry,
       "rm10010arMonupRmonCrcErrorsCounterClientInputIndex": rm10010arMonupRmonCrcErrorsCounterClientInputIndex,
       "rm10010arMonupRmonCrcErrorsCounterClientInputValuePortn": rm10010arMonupRmonCrcErrorsCounterClientInputValuePortn,
       "rm10010arMonupRmonCrcErrorsCounterClientInputErrorPortn": rm10010arMonupRmonCrcErrorsCounterClientInputErrorPortn,
       "rm10010arMonupRmonCrcErrorsCounterClientInputOverloadPortn": rm10010arMonupRmonCrcErrorsCounterClientInputOverloadPortn,
       "rm10010arMonupRmonPacketsCounterClientInputTable": rm10010arMonupRmonPacketsCounterClientInputTable,
       "rm10010arMonupRmonPacketsCounterClientInputEntry": rm10010arMonupRmonPacketsCounterClientInputEntry,
       "rm10010arMonupRmonPacketsCounterClientInputIndex": rm10010arMonupRmonPacketsCounterClientInputIndex,
       "rm10010arMonupRmonPacketsCounterClientInputValuePortn": rm10010arMonupRmonPacketsCounterClientInputValuePortn,
       "rm10010arMonupRmonPacketsCounterClientInputErrorPortn": rm10010arMonupRmonPacketsCounterClientInputErrorPortn,
       "rm10010arMonupRmonPacketsCounterClientInputOverloadPortn": rm10010arMonupRmonPacketsCounterClientInputOverloadPortn,
       "rm10010arMonupRmonBroadcastCounterClientInputTable": rm10010arMonupRmonBroadcastCounterClientInputTable,
       "rm10010arMonupRmonBroadcastCounterClientInputEntry": rm10010arMonupRmonBroadcastCounterClientInputEntry,
       "rm10010arMonupRmonBroadcastCounterClientInputIndex": rm10010arMonupRmonBroadcastCounterClientInputIndex,
       "rm10010arMonupRmonBroadcastCounterClientInputValuePortn": rm10010arMonupRmonBroadcastCounterClientInputValuePortn,
       "rm10010arMonupRmonBroadcastCounterClientInputErrorPortn": rm10010arMonupRmonBroadcastCounterClientInputErrorPortn,
       "rm10010arMonupRmonBroadcastCounterClientInputOverloadPortn": rm10010arMonupRmonBroadcastCounterClientInputOverloadPortn,
       "rm10010arMonupRmonMulticastCounterClientInputTable": rm10010arMonupRmonMulticastCounterClientInputTable,
       "rm10010arMonupRmonMulticastCounterClientInputEntry": rm10010arMonupRmonMulticastCounterClientInputEntry,
       "rm10010arMonupRmonMulticastCounterClientInputIndex": rm10010arMonupRmonMulticastCounterClientInputIndex,
       "rm10010arMonupRmonMulticastCounterClientInputValuePortn": rm10010arMonupRmonMulticastCounterClientInputValuePortn,
       "rm10010arMonupRmonMulticastCounterClientInputErrorPortn": rm10010arMonupRmonMulticastCounterClientInputErrorPortn,
       "rm10010arMonupRmonMulticastCounterClientInputOverloadPortn": rm10010arMonupRmonMulticastCounterClientInputOverloadPortn,
       "rm10010arMonupRmonPauseFrameCounterClientInputTable": rm10010arMonupRmonPauseFrameCounterClientInputTable,
       "rm10010arMonupRmonPauseFrameCounterClientInputEntry": rm10010arMonupRmonPauseFrameCounterClientInputEntry,
       "rm10010arMonupRmonPauseFrameCounterClientInputIndex": rm10010arMonupRmonPauseFrameCounterClientInputIndex,
       "rm10010arMonupRmonPauseFrameCounterClientInputValuePortn": rm10010arMonupRmonPauseFrameCounterClientInputValuePortn,
       "rm10010arMonupRmonPauseFrameCounterClientInputErrorPortn": rm10010arMonupRmonPauseFrameCounterClientInputErrorPortn,
       "rm10010arMonupRmonPauseFrameCounterClientInputOverloadPortn": rm10010arMonupRmonPauseFrameCounterClientInputOverloadPortn}
)
