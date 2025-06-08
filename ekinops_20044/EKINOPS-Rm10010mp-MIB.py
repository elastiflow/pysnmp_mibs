# SNMP MIB module (EKINOPS-Rm10010mp-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ekinops_20044/EKINOPS-Rm10010mp-MIB.mib
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

moduleRm10010mp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54)
)
if mibBuilder.loadTexts:
    moduleRm10010mp.setRevisions(
        ("2011-11-09 00:00",
         "2011-11-09 00:00",
         "2012-06-18 00:00",
         "2012-06-29 00:00",
         "2012-07-04 00:00",
         "2012-07-10 00:00",
         "2012-07-24 00:00",
         "2012-08-28 00:00",
         "2012-08-29 00:00",
         "2012-09-03 00:00",
         "2012-11-06 00:00",
         "2014-01-16 00:00",
         "2014-04-01 00:00",
         "2014-10-14 00:00",
         "2015-01-21 00:00",
         "2015-10-21 00:00",
         "2016-05-20 00:00",
         "2016-06-02 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Rm10010mpMultiRate(TextualConvention, Integer32):
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



class Rm10010mpOtxMode(TextualConvention, Integer32):
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



class Rm10010mpOtxGrid(TextualConvention, Integer32):
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



class Rm10010mpAdjustValue(TextualConvention, Integer32):
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



class Rm10010mpClientProtocol(TextualConvention, Integer32):
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



class Rm10010mpProtocolMode(TextualConvention, Integer32):
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



class Rm10010mpOtxChannel(TextualConvention, Integer32):
    status = "current"


class Rm10010mpOrxChannel(TextualConvention, Integer32):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Rm10010mpalarms_ObjectIdentity = ObjectIdentity
rm10010mpalarms = _Rm10010mpalarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2)
)
_Rm10010mpAlmOther_ObjectIdentity = ObjectIdentity
rm10010mpAlmOther = _Rm10010mpAlmOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1)
)
_Rm10010mpAlmOtherNurg_ObjectIdentity = ObjectIdentity
rm10010mpAlmOtherNurg = _Rm10010mpAlmOtherNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 1)
)
_Rm10010mpAlmsynthAlm2_ObjectIdentity = ObjectIdentity
rm10010mpAlmsynthAlm2 = _Rm10010mpAlmsynthAlm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 1, 2)
)
_Rm10010mpAlmConfTableSave_Type = EkiOnOff
_Rm10010mpAlmConfTableSave_Object = MibScalar
rm10010mpAlmConfTableSave = _Rm10010mpAlmConfTableSave_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 1, 2, 1),
    _Rm10010mpAlmConfTableSave_Type()
)
rm10010mpAlmConfTableSave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmConfTableSave.setStatus("current")
_Rm10010mpAlmInvUpload_Type = EkiOnOff
_Rm10010mpAlmInvUpload_Object = MibScalar
rm10010mpAlmInvUpload = _Rm10010mpAlmInvUpload_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 1, 2, 2),
    _Rm10010mpAlmInvUpload_Type()
)
rm10010mpAlmInvUpload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmInvUpload.setStatus("current")
_Rm10010mpAlmConfTableLoad_Type = EkiOnOff
_Rm10010mpAlmConfTableLoad_Object = MibScalar
rm10010mpAlmConfTableLoad = _Rm10010mpAlmConfTableLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 1, 2, 3),
    _Rm10010mpAlmConfTableLoad_Type()
)
rm10010mpAlmConfTableLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmConfTableLoad.setStatus("current")
_Rm10010mpAlmCorrelatOff_Type = EkiOnOff
_Rm10010mpAlmCorrelatOff_Object = MibScalar
rm10010mpAlmCorrelatOff = _Rm10010mpAlmCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 1, 2, 4),
    _Rm10010mpAlmCorrelatOff_Type()
)
rm10010mpAlmCorrelatOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmCorrelatOff.setStatus("current")
_Rm10010mpAlmMaintenanceOn_Type = EkiOnOff
_Rm10010mpAlmMaintenanceOn_Object = MibScalar
rm10010mpAlmMaintenanceOn = _Rm10010mpAlmMaintenanceOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 1, 2, 5),
    _Rm10010mpAlmMaintenanceOn_Type()
)
rm10010mpAlmMaintenanceOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmMaintenanceOn.setStatus("current")
_Rm10010mpAlmOtherUrg_ObjectIdentity = ObjectIdentity
rm10010mpAlmOtherUrg = _Rm10010mpAlmOtherUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 2)
)
_Rm10010mpAlmmodFanFail_ObjectIdentity = ObjectIdentity
rm10010mpAlmmodFanFail = _Rm10010mpAlmmodFanFail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 2, 248)
)
_Rm10010mpAlmFanModuleAbsent_Type = EkiOnOff
_Rm10010mpAlmFanModuleAbsent_Object = MibScalar
rm10010mpAlmFanModuleAbsent = _Rm10010mpAlmFanModuleAbsent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 2, 248, 1),
    _Rm10010mpAlmFanModuleAbsent_Type()
)
rm10010mpAlmFanModuleAbsent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmFanModuleAbsent.setStatus("current")
_Rm10010mpAlmFansFail_Type = EkiOnOff
_Rm10010mpAlmFansFail_Object = MibScalar
rm10010mpAlmFansFail = _Rm10010mpAlmFansFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 2, 248, 2),
    _Rm10010mpAlmFansFail_Type()
)
rm10010mpAlmFansFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmFansFail.setStatus("current")
_Rm10010mpAlmFan1Fail_Type = EkiOnOff
_Rm10010mpAlmFan1Fail_Object = MibScalar
rm10010mpAlmFan1Fail = _Rm10010mpAlmFan1Fail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 2, 248, 4),
    _Rm10010mpAlmFan1Fail_Type()
)
rm10010mpAlmFan1Fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmFan1Fail.setStatus("current")
_Rm10010mpAlmFan2Fail_Type = EkiOnOff
_Rm10010mpAlmFan2Fail_Object = MibScalar
rm10010mpAlmFan2Fail = _Rm10010mpAlmFan2Fail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 2, 248, 5),
    _Rm10010mpAlmFan2Fail_Type()
)
rm10010mpAlmFan2Fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmFan2Fail.setStatus("current")
_Rm10010mpAlmFan3Fail_Type = EkiOnOff
_Rm10010mpAlmFan3Fail_Object = MibScalar
rm10010mpAlmFan3Fail = _Rm10010mpAlmFan3Fail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 2, 248, 6),
    _Rm10010mpAlmFan3Fail_Type()
)
rm10010mpAlmFan3Fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmFan3Fail.setStatus("current")
_Rm10010mpAlmFan4Fail_Type = EkiOnOff
_Rm10010mpAlmFan4Fail_Object = MibScalar
rm10010mpAlmFan4Fail = _Rm10010mpAlmFan4Fail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 2, 248, 7),
    _Rm10010mpAlmFan4Fail_Type()
)
rm10010mpAlmFan4Fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmFan4Fail.setStatus("current")
_Rm10010mpAlmOtherCrit_ObjectIdentity = ObjectIdentity
rm10010mpAlmOtherCrit = _Rm10010mpAlmOtherCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3)
)
_Rm10010mpAlmsynthAlm0_ObjectIdentity = ObjectIdentity
rm10010mpAlmsynthAlm0 = _Rm10010mpAlmsynthAlm0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 0)
)
_Rm10010mpAlmFailFan_Type = EkiOnOff
_Rm10010mpAlmFailFan_Object = MibScalar
rm10010mpAlmFailFan = _Rm10010mpAlmFailFan_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 0, 2),
    _Rm10010mpAlmFailFan_Type()
)
rm10010mpAlmFailFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmFailFan.setStatus("current")
_Rm10010mpAlmModGlobFail_Type = EkiOnOff
_Rm10010mpAlmModGlobFail_Object = MibScalar
rm10010mpAlmModGlobFail = _Rm10010mpAlmModGlobFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 0, 9),
    _Rm10010mpAlmModGlobFail_Type()
)
rm10010mpAlmModGlobFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmModGlobFail.setStatus("current")
_Rm10010mpAlmDefFuseA_Type = EkiOnOff
_Rm10010mpAlmDefFuseA_Object = MibScalar
rm10010mpAlmDefFuseA = _Rm10010mpAlmDefFuseA_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 0, 15),
    _Rm10010mpAlmDefFuseA_Type()
)
rm10010mpAlmDefFuseA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmDefFuseA.setStatus("current")
_Rm10010mpAlmDefFuseB_Type = EkiOnOff
_Rm10010mpAlmDefFuseB_Object = MibScalar
rm10010mpAlmDefFuseB = _Rm10010mpAlmDefFuseB_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 0, 16),
    _Rm10010mpAlmDefFuseB_Type()
)
rm10010mpAlmDefFuseB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmDefFuseB.setStatus("current")
_Rm10010mpAlmclientModuleState_ObjectIdentity = ObjectIdentity
rm10010mpAlmclientModuleState = _Rm10010mpAlmclientModuleState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 40)
)
_Rm10010mpAlmCfpInitialize_Type = EkiOnOff
_Rm10010mpAlmCfpInitialize_Object = MibScalar
rm10010mpAlmCfpInitialize = _Rm10010mpAlmCfpInitialize_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 40, 1),
    _Rm10010mpAlmCfpInitialize_Type()
)
rm10010mpAlmCfpInitialize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmCfpInitialize.setStatus("current")
_Rm10010mpAlmCfpLowPower_Type = EkiOnOff
_Rm10010mpAlmCfpLowPower_Object = MibScalar
rm10010mpAlmCfpLowPower = _Rm10010mpAlmCfpLowPower_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 40, 2),
    _Rm10010mpAlmCfpLowPower_Type()
)
rm10010mpAlmCfpLowPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmCfpLowPower.setStatus("current")
_Rm10010mpAlmCfpHighPowerUp_Type = EkiOnOff
_Rm10010mpAlmCfpHighPowerUp_Object = MibScalar
rm10010mpAlmCfpHighPowerUp = _Rm10010mpAlmCfpHighPowerUp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 40, 3),
    _Rm10010mpAlmCfpHighPowerUp_Type()
)
rm10010mpAlmCfpHighPowerUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmCfpHighPowerUp.setStatus("current")
_Rm10010mpAlmCfpTxOff_Type = EkiOnOff
_Rm10010mpAlmCfpTxOff_Object = MibScalar
rm10010mpAlmCfpTxOff = _Rm10010mpAlmCfpTxOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 40, 4),
    _Rm10010mpAlmCfpTxOff_Type()
)
rm10010mpAlmCfpTxOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmCfpTxOff.setStatus("current")
_Rm10010mpAlmCfpTxTurnOn_Type = EkiOnOff
_Rm10010mpAlmCfpTxTurnOn_Object = MibScalar
rm10010mpAlmCfpTxTurnOn = _Rm10010mpAlmCfpTxTurnOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 40, 5),
    _Rm10010mpAlmCfpTxTurnOn_Type()
)
rm10010mpAlmCfpTxTurnOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmCfpTxTurnOn.setStatus("current")
_Rm10010mpAlmCfpReady_Type = EkiOnOff
_Rm10010mpAlmCfpReady_Object = MibScalar
rm10010mpAlmCfpReady = _Rm10010mpAlmCfpReady_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 40, 6),
    _Rm10010mpAlmCfpReady_Type()
)
rm10010mpAlmCfpReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmCfpReady.setStatus("current")
_Rm10010mpAlmCfpFault_Type = EkiOnOff
_Rm10010mpAlmCfpFault_Object = MibScalar
rm10010mpAlmCfpFault = _Rm10010mpAlmCfpFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 40, 7),
    _Rm10010mpAlmCfpFault_Type()
)
rm10010mpAlmCfpFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmCfpFault.setStatus("current")
_Rm10010mpAlmCfpTxTurnOff_Type = EkiOnOff
_Rm10010mpAlmCfpTxTurnOff_Object = MibScalar
rm10010mpAlmCfpTxTurnOff = _Rm10010mpAlmCfpTxTurnOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 40, 8),
    _Rm10010mpAlmCfpTxTurnOff_Type()
)
rm10010mpAlmCfpTxTurnOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmCfpTxTurnOff.setStatus("current")
_Rm10010mpAlmCfpHighPowerDown_Type = EkiOnOff
_Rm10010mpAlmCfpHighPowerDown_Object = MibScalar
rm10010mpAlmCfpHighPowerDown = _Rm10010mpAlmCfpHighPowerDown_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 40, 9),
    _Rm10010mpAlmCfpHighPowerDown_Type()
)
rm10010mpAlmCfpHighPowerDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmCfpHighPowerDown.setStatus("current")
_Rm10010mpAlmclientModuleGeneralStatus_ObjectIdentity = ObjectIdentity
rm10010mpAlmclientModuleGeneralStatus = _Rm10010mpAlmclientModuleGeneralStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 41)
)
_Rm10010mpAlmCfpOutOfAlignment_Type = EkiOnOff
_Rm10010mpAlmCfpOutOfAlignment_Object = MibScalar
rm10010mpAlmCfpOutOfAlignment = _Rm10010mpAlmCfpOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 41, 4),
    _Rm10010mpAlmCfpOutOfAlignment_Type()
)
rm10010mpAlmCfpOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmCfpOutOfAlignment.setStatus("current")
_Rm10010mpAlmCfpRxNetworkLol_Type = EkiOnOff
_Rm10010mpAlmCfpRxNetworkLol_Object = MibScalar
rm10010mpAlmCfpRxNetworkLol = _Rm10010mpAlmCfpRxNetworkLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 41, 5),
    _Rm10010mpAlmCfpRxNetworkLol_Type()
)
rm10010mpAlmCfpRxNetworkLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmCfpRxNetworkLol.setStatus("current")
_Rm10010mpAlmCfpRxLos_Type = EkiOnOff
_Rm10010mpAlmCfpRxLos_Object = MibScalar
rm10010mpAlmCfpRxLos = _Rm10010mpAlmCfpRxLos_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 41, 6),
    _Rm10010mpAlmCfpRxLos_Type()
)
rm10010mpAlmCfpRxLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmCfpRxLos.setStatus("current")
_Rm10010mpAlmCfpTxHostLol_Type = EkiOnOff
_Rm10010mpAlmCfpTxHostLol_Object = MibScalar
rm10010mpAlmCfpTxHostLol = _Rm10010mpAlmCfpTxHostLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 41, 7),
    _Rm10010mpAlmCfpTxHostLol_Type()
)
rm10010mpAlmCfpTxHostLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmCfpTxHostLol.setStatus("current")
_Rm10010mpAlmCfpTxLosf_Type = EkiOnOff
_Rm10010mpAlmCfpTxLosf_Object = MibScalar
rm10010mpAlmCfpTxLosf = _Rm10010mpAlmCfpTxLosf_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 41, 8),
    _Rm10010mpAlmCfpTxLosf_Type()
)
rm10010mpAlmCfpTxLosf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmCfpTxLosf.setStatus("current")
_Rm10010mpAlmCfpTxCmuLol_Type = EkiOnOff
_Rm10010mpAlmCfpTxCmuLol_Object = MibScalar
rm10010mpAlmCfpTxCmuLol = _Rm10010mpAlmCfpTxCmuLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 41, 9),
    _Rm10010mpAlmCfpTxCmuLol_Type()
)
rm10010mpAlmCfpTxCmuLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmCfpTxCmuLol.setStatus("current")
_Rm10010mpAlmCfpTxJitterPllLol_Type = EkiOnOff
_Rm10010mpAlmCfpTxJitterPllLol_Object = MibScalar
rm10010mpAlmCfpTxJitterPllLol = _Rm10010mpAlmCfpTxJitterPllLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 41, 10),
    _Rm10010mpAlmCfpTxJitterPllLol_Type()
)
rm10010mpAlmCfpTxJitterPllLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmCfpTxJitterPllLol.setStatus("current")
_Rm10010mpAlmCfpLossOfRefclk_Type = EkiOnOff
_Rm10010mpAlmCfpLossOfRefclk_Object = MibScalar
rm10010mpAlmCfpLossOfRefclk = _Rm10010mpAlmCfpLossOfRefclk_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 41, 11),
    _Rm10010mpAlmCfpLossOfRefclk_Type()
)
rm10010mpAlmCfpLossOfRefclk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmCfpLossOfRefclk.setStatus("current")
_Rm10010mpAlmCfpHwInterlock_Type = EkiOnOff
_Rm10010mpAlmCfpHwInterlock_Object = MibScalar
rm10010mpAlmCfpHwInterlock = _Rm10010mpAlmCfpHwInterlock_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 41, 14),
    _Rm10010mpAlmCfpHwInterlock_Type()
)
rm10010mpAlmCfpHwInterlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmCfpHwInterlock.setStatus("current")
_Rm10010mpAlmclientGlobalAlarmSummary_ObjectIdentity = ObjectIdentity
rm10010mpAlmclientGlobalAlarmSummary = _Rm10010mpAlmclientGlobalAlarmSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 42)
)
_Rm10010mpAlmCfpSoftGlobAlarmTest_Type = EkiOnOff
_Rm10010mpAlmCfpSoftGlobAlarmTest_Object = MibScalar
rm10010mpAlmCfpSoftGlobAlarmTest = _Rm10010mpAlmCfpSoftGlobAlarmTest_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 42, 1),
    _Rm10010mpAlmCfpSoftGlobAlarmTest_Type()
)
rm10010mpAlmCfpSoftGlobAlarmTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmCfpSoftGlobAlarmTest.setStatus("current")
_Rm10010mpAlmCfpNetworkLaneAlarmWarning2_Type = EkiOnOff
_Rm10010mpAlmCfpNetworkLaneAlarmWarning2_Object = MibScalar
rm10010mpAlmCfpNetworkLaneAlarmWarning2 = _Rm10010mpAlmCfpNetworkLaneAlarmWarning2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 42, 7),
    _Rm10010mpAlmCfpNetworkLaneAlarmWarning2_Type()
)
rm10010mpAlmCfpNetworkLaneAlarmWarning2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmCfpNetworkLaneAlarmWarning2.setStatus("current")
_Rm10010mpAlmCfpModuleState_Type = EkiOnOff
_Rm10010mpAlmCfpModuleState_Object = MibScalar
rm10010mpAlmCfpModuleState = _Rm10010mpAlmCfpModuleState_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 42, 8),
    _Rm10010mpAlmCfpModuleState_Type()
)
rm10010mpAlmCfpModuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmCfpModuleState.setStatus("current")
_Rm10010mpAlmCfpModuleGeneralStatus_Type = EkiOnOff
_Rm10010mpAlmCfpModuleGeneralStatus_Object = MibScalar
rm10010mpAlmCfpModuleGeneralStatus = _Rm10010mpAlmCfpModuleGeneralStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 42, 9),
    _Rm10010mpAlmCfpModuleGeneralStatus_Type()
)
rm10010mpAlmCfpModuleGeneralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmCfpModuleGeneralStatus.setStatus("current")
_Rm10010mpAlmCfpModuleFault_Type = EkiOnOff
_Rm10010mpAlmCfpModuleFault_Object = MibScalar
rm10010mpAlmCfpModuleFault = _Rm10010mpAlmCfpModuleFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 42, 10),
    _Rm10010mpAlmCfpModuleFault_Type()
)
rm10010mpAlmCfpModuleFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmCfpModuleFault.setStatus("current")
_Rm10010mpAlmCfpModuleAlarmWarning1_Type = EkiOnOff
_Rm10010mpAlmCfpModuleAlarmWarning1_Object = MibScalar
rm10010mpAlmCfpModuleAlarmWarning1 = _Rm10010mpAlmCfpModuleAlarmWarning1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 42, 11),
    _Rm10010mpAlmCfpModuleAlarmWarning1_Type()
)
rm10010mpAlmCfpModuleAlarmWarning1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmCfpModuleAlarmWarning1.setStatus("current")
_Rm10010mpAlmCfpModuleAlarmWarning2_Type = EkiOnOff
_Rm10010mpAlmCfpModuleAlarmWarning2_Object = MibScalar
rm10010mpAlmCfpModuleAlarmWarning2 = _Rm10010mpAlmCfpModuleAlarmWarning2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 42, 12),
    _Rm10010mpAlmCfpModuleAlarmWarning2_Type()
)
rm10010mpAlmCfpModuleAlarmWarning2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmCfpModuleAlarmWarning2.setStatus("current")
_Rm10010mpAlmCfpNetworkLaneAlarmWarning1_Type = EkiOnOff
_Rm10010mpAlmCfpNetworkLaneAlarmWarning1_Object = MibScalar
rm10010mpAlmCfpNetworkLaneAlarmWarning1 = _Rm10010mpAlmCfpNetworkLaneAlarmWarning1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 42, 13),
    _Rm10010mpAlmCfpNetworkLaneAlarmWarning1_Type()
)
rm10010mpAlmCfpNetworkLaneAlarmWarning1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmCfpNetworkLaneAlarmWarning1.setStatus("current")
_Rm10010mpAlmCfpNetworkLaneFaultStatus_Type = EkiOnOff
_Rm10010mpAlmCfpNetworkLaneFaultStatus_Object = MibScalar
rm10010mpAlmCfpNetworkLaneFaultStatus = _Rm10010mpAlmCfpNetworkLaneFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 42, 14),
    _Rm10010mpAlmCfpNetworkLaneFaultStatus_Type()
)
rm10010mpAlmCfpNetworkLaneFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmCfpNetworkLaneFaultStatus.setStatus("current")
_Rm10010mpAlmCfpHostLaneFaultStatus_Type = EkiOnOff
_Rm10010mpAlmCfpHostLaneFaultStatus_Object = MibScalar
rm10010mpAlmCfpHostLaneFaultStatus = _Rm10010mpAlmCfpHostLaneFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 42, 15),
    _Rm10010mpAlmCfpHostLaneFaultStatus_Type()
)
rm10010mpAlmCfpHostLaneFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmCfpHostLaneFaultStatus.setStatus("current")
_Rm10010mpAlmCfpGlobAlarmAssertion_Type = EkiOnOff
_Rm10010mpAlmCfpGlobAlarmAssertion_Object = MibScalar
rm10010mpAlmCfpGlobAlarmAssertion = _Rm10010mpAlmCfpGlobAlarmAssertion_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 42, 16),
    _Rm10010mpAlmCfpGlobAlarmAssertion_Type()
)
rm10010mpAlmCfpGlobAlarmAssertion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmCfpGlobAlarmAssertion.setStatus("current")
_Rm10010mpAlmmsaModuleState_ObjectIdentity = ObjectIdentity
rm10010mpAlmmsaModuleState = _Rm10010mpAlmmsaModuleState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 46)
)
_Rm10010mpAlmMsaInitialize_Type = EkiOnOff
_Rm10010mpAlmMsaInitialize_Object = MibScalar
rm10010mpAlmMsaInitialize = _Rm10010mpAlmMsaInitialize_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 46, 1),
    _Rm10010mpAlmMsaInitialize_Type()
)
rm10010mpAlmMsaInitialize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmMsaInitialize.setStatus("current")
_Rm10010mpAlmMsaLowPower_Type = EkiOnOff
_Rm10010mpAlmMsaLowPower_Object = MibScalar
rm10010mpAlmMsaLowPower = _Rm10010mpAlmMsaLowPower_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 46, 2),
    _Rm10010mpAlmMsaLowPower_Type()
)
rm10010mpAlmMsaLowPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmMsaLowPower.setStatus("current")
_Rm10010mpAlmMsaHighPowerUp_Type = EkiOnOff
_Rm10010mpAlmMsaHighPowerUp_Object = MibScalar
rm10010mpAlmMsaHighPowerUp = _Rm10010mpAlmMsaHighPowerUp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 46, 3),
    _Rm10010mpAlmMsaHighPowerUp_Type()
)
rm10010mpAlmMsaHighPowerUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmMsaHighPowerUp.setStatus("current")
_Rm10010mpAlmMsaTxOff_Type = EkiOnOff
_Rm10010mpAlmMsaTxOff_Object = MibScalar
rm10010mpAlmMsaTxOff = _Rm10010mpAlmMsaTxOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 46, 4),
    _Rm10010mpAlmMsaTxOff_Type()
)
rm10010mpAlmMsaTxOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmMsaTxOff.setStatus("current")
_Rm10010mpAlmMsaTxTurnOn_Type = EkiOnOff
_Rm10010mpAlmMsaTxTurnOn_Object = MibScalar
rm10010mpAlmMsaTxTurnOn = _Rm10010mpAlmMsaTxTurnOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 46, 5),
    _Rm10010mpAlmMsaTxTurnOn_Type()
)
rm10010mpAlmMsaTxTurnOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmMsaTxTurnOn.setStatus("current")
_Rm10010mpAlmMsaReady_Type = EkiOnOff
_Rm10010mpAlmMsaReady_Object = MibScalar
rm10010mpAlmMsaReady = _Rm10010mpAlmMsaReady_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 46, 6),
    _Rm10010mpAlmMsaReady_Type()
)
rm10010mpAlmMsaReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmMsaReady.setStatus("current")
_Rm10010mpAlmMsaFault_Type = EkiOnOff
_Rm10010mpAlmMsaFault_Object = MibScalar
rm10010mpAlmMsaFault = _Rm10010mpAlmMsaFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 46, 7),
    _Rm10010mpAlmMsaFault_Type()
)
rm10010mpAlmMsaFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmMsaFault.setStatus("current")
_Rm10010mpAlmMsaTxTurnOff_Type = EkiOnOff
_Rm10010mpAlmMsaTxTurnOff_Object = MibScalar
rm10010mpAlmMsaTxTurnOff = _Rm10010mpAlmMsaTxTurnOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 46, 8),
    _Rm10010mpAlmMsaTxTurnOff_Type()
)
rm10010mpAlmMsaTxTurnOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmMsaTxTurnOff.setStatus("current")
_Rm10010mpAlmMsaHighPowerDown_Type = EkiOnOff
_Rm10010mpAlmMsaHighPowerDown_Object = MibScalar
rm10010mpAlmMsaHighPowerDown = _Rm10010mpAlmMsaHighPowerDown_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 46, 9),
    _Rm10010mpAlmMsaHighPowerDown_Type()
)
rm10010mpAlmMsaHighPowerDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmMsaHighPowerDown.setStatus("current")
_Rm10010mpAlmmsaModuleGeneralStatus_ObjectIdentity = ObjectIdentity
rm10010mpAlmmsaModuleGeneralStatus = _Rm10010mpAlmmsaModuleGeneralStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 47)
)
_Rm10010mpAlmMsaOutOfAlignment_Type = EkiOnOff
_Rm10010mpAlmMsaOutOfAlignment_Object = MibScalar
rm10010mpAlmMsaOutOfAlignment = _Rm10010mpAlmMsaOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 47, 4),
    _Rm10010mpAlmMsaOutOfAlignment_Type()
)
rm10010mpAlmMsaOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmMsaOutOfAlignment.setStatus("current")
_Rm10010mpAlmMsaRxNetworkLol_Type = EkiOnOff
_Rm10010mpAlmMsaRxNetworkLol_Object = MibScalar
rm10010mpAlmMsaRxNetworkLol = _Rm10010mpAlmMsaRxNetworkLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 47, 5),
    _Rm10010mpAlmMsaRxNetworkLol_Type()
)
rm10010mpAlmMsaRxNetworkLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmMsaRxNetworkLol.setStatus("current")
_Rm10010mpAlmMsaRxLos_Type = EkiOnOff
_Rm10010mpAlmMsaRxLos_Object = MibScalar
rm10010mpAlmMsaRxLos = _Rm10010mpAlmMsaRxLos_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 47, 6),
    _Rm10010mpAlmMsaRxLos_Type()
)
rm10010mpAlmMsaRxLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmMsaRxLos.setStatus("current")
_Rm10010mpAlmMsaTxHostLol_Type = EkiOnOff
_Rm10010mpAlmMsaTxHostLol_Object = MibScalar
rm10010mpAlmMsaTxHostLol = _Rm10010mpAlmMsaTxHostLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 47, 7),
    _Rm10010mpAlmMsaTxHostLol_Type()
)
rm10010mpAlmMsaTxHostLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmMsaTxHostLol.setStatus("current")
_Rm10010mpAlmMsaTxLosf_Type = EkiOnOff
_Rm10010mpAlmMsaTxLosf_Object = MibScalar
rm10010mpAlmMsaTxLosf = _Rm10010mpAlmMsaTxLosf_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 47, 8),
    _Rm10010mpAlmMsaTxLosf_Type()
)
rm10010mpAlmMsaTxLosf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmMsaTxLosf.setStatus("current")
_Rm10010mpAlmMsaTxCmuLol_Type = EkiOnOff
_Rm10010mpAlmMsaTxCmuLol_Object = MibScalar
rm10010mpAlmMsaTxCmuLol = _Rm10010mpAlmMsaTxCmuLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 47, 9),
    _Rm10010mpAlmMsaTxCmuLol_Type()
)
rm10010mpAlmMsaTxCmuLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmMsaTxCmuLol.setStatus("current")
_Rm10010mpAlmMsaTxJitterPllLol_Type = EkiOnOff
_Rm10010mpAlmMsaTxJitterPllLol_Object = MibScalar
rm10010mpAlmMsaTxJitterPllLol = _Rm10010mpAlmMsaTxJitterPllLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 47, 10),
    _Rm10010mpAlmMsaTxJitterPllLol_Type()
)
rm10010mpAlmMsaTxJitterPllLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmMsaTxJitterPllLol.setStatus("current")
_Rm10010mpAlmMsaLossOfRefclk_Type = EkiOnOff
_Rm10010mpAlmMsaLossOfRefclk_Object = MibScalar
rm10010mpAlmMsaLossOfRefclk = _Rm10010mpAlmMsaLossOfRefclk_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 47, 11),
    _Rm10010mpAlmMsaLossOfRefclk_Type()
)
rm10010mpAlmMsaLossOfRefclk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmMsaLossOfRefclk.setStatus("current")
_Rm10010mpAlmMsaHwInterlock_Type = EkiOnOff
_Rm10010mpAlmMsaHwInterlock_Object = MibScalar
rm10010mpAlmMsaHwInterlock = _Rm10010mpAlmMsaHwInterlock_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 47, 14),
    _Rm10010mpAlmMsaHwInterlock_Type()
)
rm10010mpAlmMsaHwInterlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmMsaHwInterlock.setStatus("current")
_Rm10010mpAlmmsaGlobalAlarmSummary_ObjectIdentity = ObjectIdentity
rm10010mpAlmmsaGlobalAlarmSummary = _Rm10010mpAlmmsaGlobalAlarmSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 48)
)
_Rm10010mpAlmMsaSoftGlobAlarmTest_Type = EkiOnOff
_Rm10010mpAlmMsaSoftGlobAlarmTest_Object = MibScalar
rm10010mpAlmMsaSoftGlobAlarmTest = _Rm10010mpAlmMsaSoftGlobAlarmTest_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 48, 1),
    _Rm10010mpAlmMsaSoftGlobAlarmTest_Type()
)
rm10010mpAlmMsaSoftGlobAlarmTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmMsaSoftGlobAlarmTest.setStatus("current")
_Rm10010mpAlmMsaNetworkHostAlarmStatus_Type = EkiOnOff
_Rm10010mpAlmMsaNetworkHostAlarmStatus_Object = MibScalar
rm10010mpAlmMsaNetworkHostAlarmStatus = _Rm10010mpAlmMsaNetworkHostAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 48, 6),
    _Rm10010mpAlmMsaNetworkHostAlarmStatus_Type()
)
rm10010mpAlmMsaNetworkHostAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmMsaNetworkHostAlarmStatus.setStatus("current")
_Rm10010mpAlmMsaNetworkLaneAlarmWarning2_Type = EkiOnOff
_Rm10010mpAlmMsaNetworkLaneAlarmWarning2_Object = MibScalar
rm10010mpAlmMsaNetworkLaneAlarmWarning2 = _Rm10010mpAlmMsaNetworkLaneAlarmWarning2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 48, 7),
    _Rm10010mpAlmMsaNetworkLaneAlarmWarning2_Type()
)
rm10010mpAlmMsaNetworkLaneAlarmWarning2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmMsaNetworkLaneAlarmWarning2.setStatus("current")
_Rm10010mpAlmMsaModuleState_Type = EkiOnOff
_Rm10010mpAlmMsaModuleState_Object = MibScalar
rm10010mpAlmMsaModuleState = _Rm10010mpAlmMsaModuleState_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 48, 8),
    _Rm10010mpAlmMsaModuleState_Type()
)
rm10010mpAlmMsaModuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmMsaModuleState.setStatus("current")
_Rm10010mpAlmMsaModuleGeneralStatus_Type = EkiOnOff
_Rm10010mpAlmMsaModuleGeneralStatus_Object = MibScalar
rm10010mpAlmMsaModuleGeneralStatus = _Rm10010mpAlmMsaModuleGeneralStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 48, 9),
    _Rm10010mpAlmMsaModuleGeneralStatus_Type()
)
rm10010mpAlmMsaModuleGeneralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmMsaModuleGeneralStatus.setStatus("current")
_Rm10010mpAlmModuleFault_Type = EkiOnOff
_Rm10010mpAlmModuleFault_Object = MibScalar
rm10010mpAlmModuleFault = _Rm10010mpAlmModuleFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 48, 10),
    _Rm10010mpAlmModuleFault_Type()
)
rm10010mpAlmModuleFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmModuleFault.setStatus("current")
_Rm10010mpAlmMsaModuleAlarmWarning1_Type = EkiOnOff
_Rm10010mpAlmMsaModuleAlarmWarning1_Object = MibScalar
rm10010mpAlmMsaModuleAlarmWarning1 = _Rm10010mpAlmMsaModuleAlarmWarning1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 48, 11),
    _Rm10010mpAlmMsaModuleAlarmWarning1_Type()
)
rm10010mpAlmMsaModuleAlarmWarning1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmMsaModuleAlarmWarning1.setStatus("current")
_Rm10010mpAlmMsaModuleAlarmWarning2_Type = EkiOnOff
_Rm10010mpAlmMsaModuleAlarmWarning2_Object = MibScalar
rm10010mpAlmMsaModuleAlarmWarning2 = _Rm10010mpAlmMsaModuleAlarmWarning2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 48, 12),
    _Rm10010mpAlmMsaModuleAlarmWarning2_Type()
)
rm10010mpAlmMsaModuleAlarmWarning2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmMsaModuleAlarmWarning2.setStatus("current")
_Rm10010mpAlmMsaNetworkLaneAlarmWarning1_Type = EkiOnOff
_Rm10010mpAlmMsaNetworkLaneAlarmWarning1_Object = MibScalar
rm10010mpAlmMsaNetworkLaneAlarmWarning1 = _Rm10010mpAlmMsaNetworkLaneAlarmWarning1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 48, 13),
    _Rm10010mpAlmMsaNetworkLaneAlarmWarning1_Type()
)
rm10010mpAlmMsaNetworkLaneAlarmWarning1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmMsaNetworkLaneAlarmWarning1.setStatus("current")
_Rm10010mpAlmMsaNetworkLaneFaultStatus_Type = EkiOnOff
_Rm10010mpAlmMsaNetworkLaneFaultStatus_Object = MibScalar
rm10010mpAlmMsaNetworkLaneFaultStatus = _Rm10010mpAlmMsaNetworkLaneFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 48, 14),
    _Rm10010mpAlmMsaNetworkLaneFaultStatus_Type()
)
rm10010mpAlmMsaNetworkLaneFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmMsaNetworkLaneFaultStatus.setStatus("current")
_Rm10010mpAlmMsaHostLaneFaultStatus_Type = EkiOnOff
_Rm10010mpAlmMsaHostLaneFaultStatus_Object = MibScalar
rm10010mpAlmMsaHostLaneFaultStatus = _Rm10010mpAlmMsaHostLaneFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 48, 15),
    _Rm10010mpAlmMsaHostLaneFaultStatus_Type()
)
rm10010mpAlmMsaHostLaneFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmMsaHostLaneFaultStatus.setStatus("current")
_Rm10010mpAlmMsaGlobAlarmAssertion_Type = EkiOnOff
_Rm10010mpAlmMsaGlobAlarmAssertion_Object = MibScalar
rm10010mpAlmMsaGlobAlarmAssertion = _Rm10010mpAlmMsaGlobAlarmAssertion_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 48, 16),
    _Rm10010mpAlmMsaGlobAlarmAssertion_Type()
)
rm10010mpAlmMsaGlobAlarmAssertion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmMsaGlobAlarmAssertion.setStatus("current")
_Rm10010mpAlmmsaNetworkTxAlignment_ObjectIdentity = ObjectIdentity
rm10010mpAlmmsaNetworkTxAlignment = _Rm10010mpAlmmsaNetworkTxAlignment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 49)
)
_Rm10010mpAlmNetTxTimingFault_Type = EkiOnOff
_Rm10010mpAlmNetTxTimingFault_Object = MibScalar
rm10010mpAlmNetTxTimingFault = _Rm10010mpAlmNetTxTimingFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 49, 12),
    _Rm10010mpAlmNetTxTimingFault_Type()
)
rm10010mpAlmNetTxTimingFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmNetTxTimingFault.setStatus("current")
_Rm10010mpAlmNetTxReferenceClockFault_Type = EkiOnOff
_Rm10010mpAlmNetTxReferenceClockFault_Object = MibScalar
rm10010mpAlmNetTxReferenceClockFault = _Rm10010mpAlmNetTxReferenceClockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 49, 13),
    _Rm10010mpAlmNetTxReferenceClockFault_Type()
)
rm10010mpAlmNetTxReferenceClockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmNetTxReferenceClockFault.setStatus("current")
_Rm10010mpAlmNetTxCmuLockFault_Type = EkiOnOff
_Rm10010mpAlmNetTxCmuLockFault_Object = MibScalar
rm10010mpAlmNetTxCmuLockFault = _Rm10010mpAlmNetTxCmuLockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 49, 14),
    _Rm10010mpAlmNetTxCmuLockFault_Type()
)
rm10010mpAlmNetTxCmuLockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmNetTxCmuLockFault.setStatus("current")
_Rm10010mpAlmNetTxOutOfAlignment_Type = EkiOnOff
_Rm10010mpAlmNetTxOutOfAlignment_Object = MibScalar
rm10010mpAlmNetTxOutOfAlignment = _Rm10010mpAlmNetTxOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 49, 15),
    _Rm10010mpAlmNetTxOutOfAlignment_Type()
)
rm10010mpAlmNetTxOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmNetTxOutOfAlignment.setStatus("current")
_Rm10010mpAlmNetTxLossOfAlignment_Type = EkiOnOff
_Rm10010mpAlmNetTxLossOfAlignment_Object = MibScalar
rm10010mpAlmNetTxLossOfAlignment = _Rm10010mpAlmNetTxLossOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 49, 16),
    _Rm10010mpAlmNetTxLossOfAlignment_Type()
)
rm10010mpAlmNetTxLossOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmNetTxLossOfAlignment.setStatus("current")
_Rm10010mpAlmmsaNetworkRxAlignment_ObjectIdentity = ObjectIdentity
rm10010mpAlmmsaNetworkRxAlignment = _Rm10010mpAlmmsaNetworkRxAlignment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 50)
)
_Rm10010mpAlmNetRxTimingFault_Type = EkiOnOff
_Rm10010mpAlmNetRxTimingFault_Object = MibScalar
rm10010mpAlmNetRxTimingFault = _Rm10010mpAlmNetRxTimingFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 50, 12),
    _Rm10010mpAlmNetRxTimingFault_Type()
)
rm10010mpAlmNetRxTimingFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmNetRxTimingFault.setStatus("current")
_Rm10010mpAlmNetRxOutOfAlignment_Type = EkiOnOff
_Rm10010mpAlmNetRxOutOfAlignment_Object = MibScalar
rm10010mpAlmNetRxOutOfAlignment = _Rm10010mpAlmNetRxOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 50, 13),
    _Rm10010mpAlmNetRxOutOfAlignment_Type()
)
rm10010mpAlmNetRxOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmNetRxOutOfAlignment.setStatus("current")
_Rm10010mpAlmNetRxLossOfAlignment_Type = EkiOnOff
_Rm10010mpAlmNetRxLossOfAlignment_Object = MibScalar
rm10010mpAlmNetRxLossOfAlignment = _Rm10010mpAlmNetRxLossOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 50, 14),
    _Rm10010mpAlmNetRxLossOfAlignment_Type()
)
rm10010mpAlmNetRxLossOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmNetRxLossOfAlignment.setStatus("current")
_Rm10010mpAlmNetRxModemLockFault_Type = EkiOnOff
_Rm10010mpAlmNetRxModemLockFault_Object = MibScalar
rm10010mpAlmNetRxModemLockFault = _Rm10010mpAlmNetRxModemLockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 50, 15),
    _Rm10010mpAlmNetRxModemLockFault_Type()
)
rm10010mpAlmNetRxModemLockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmNetRxModemLockFault.setStatus("current")
_Rm10010mpAlmNetRxModemSyncDetectFault_Type = EkiOnOff
_Rm10010mpAlmNetRxModemSyncDetectFault_Object = MibScalar
rm10010mpAlmNetRxModemSyncDetectFault = _Rm10010mpAlmNetRxModemSyncDetectFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 50, 16),
    _Rm10010mpAlmNetRxModemSyncDetectFault_Type()
)
rm10010mpAlmNetRxModemSyncDetectFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmNetRxModemSyncDetectFault.setStatus("current")
_Rm10010mpAlmmsaNetworkHostNetworkAlarmSummary_ObjectIdentity = ObjectIdentity
rm10010mpAlmmsaNetworkHostNetworkAlarmSummary = _Rm10010mpAlmmsaNetworkHostNetworkAlarmSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 51)
)
_Rm10010mpAlmNetworkTxAlignment_Type = EkiOnOff
_Rm10010mpAlmNetworkTxAlignment_Object = MibScalar
rm10010mpAlmNetworkTxAlignment = _Rm10010mpAlmNetworkTxAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 51, 11),
    _Rm10010mpAlmNetworkTxAlignment_Type()
)
rm10010mpAlmNetworkTxAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmNetworkTxAlignment.setStatus("current")
_Rm10010mpAlmNetworkRxAlignment_Type = EkiOnOff
_Rm10010mpAlmNetworkRxAlignment_Object = MibScalar
rm10010mpAlmNetworkRxAlignment = _Rm10010mpAlmNetworkRxAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 51, 12),
    _Rm10010mpAlmNetworkRxAlignment_Type()
)
rm10010mpAlmNetworkRxAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmNetworkRxAlignment.setStatus("current")
_Rm10010mpAlmNetworkRxOtn_Type = EkiOnOff
_Rm10010mpAlmNetworkRxOtn_Object = MibScalar
rm10010mpAlmNetworkRxOtn = _Rm10010mpAlmNetworkRxOtn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 51, 13),
    _Rm10010mpAlmNetworkRxOtn_Type()
)
rm10010mpAlmNetworkRxOtn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmNetworkRxOtn.setStatus("current")
_Rm10010mpAlmHostRxAlignment_Type = EkiOnOff
_Rm10010mpAlmHostRxAlignment_Object = MibScalar
rm10010mpAlmHostRxAlignment = _Rm10010mpAlmHostRxAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 51, 14),
    _Rm10010mpAlmHostRxAlignment_Type()
)
rm10010mpAlmHostRxAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmHostRxAlignment.setStatus("current")
_Rm10010mpAlmHostTxAlignment_Type = EkiOnOff
_Rm10010mpAlmHostTxAlignment_Object = MibScalar
rm10010mpAlmHostTxAlignment = _Rm10010mpAlmHostTxAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 51, 15),
    _Rm10010mpAlmHostTxAlignment_Type()
)
rm10010mpAlmHostTxAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmHostTxAlignment.setStatus("current")
_Rm10010mpAlmHostTxOtnStatus_Type = EkiOnOff
_Rm10010mpAlmHostTxOtnStatus_Object = MibScalar
rm10010mpAlmHostTxOtnStatus = _Rm10010mpAlmHostTxOtnStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 51, 16),
    _Rm10010mpAlmHostTxOtnStatus_Type()
)
rm10010mpAlmHostTxOtnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmHostTxOtnStatus.setStatus("current")
_Rm10010mpAlmmsaHostTxAlignment_ObjectIdentity = ObjectIdentity
rm10010mpAlmmsaHostTxAlignment = _Rm10010mpAlmmsaHostTxAlignment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 52)
)
_Rm10010mpAlmHostTxDeskewLockFault_Type = EkiOnOff
_Rm10010mpAlmHostTxDeskewLockFault_Object = MibScalar
rm10010mpAlmHostTxDeskewLockFault = _Rm10010mpAlmHostTxDeskewLockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 52, 13),
    _Rm10010mpAlmHostTxDeskewLockFault_Type()
)
rm10010mpAlmHostTxDeskewLockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmHostTxDeskewLockFault.setStatus("current")
_Rm10010mpAlmHostTxOutOfAlignment_Type = EkiOnOff
_Rm10010mpAlmHostTxOutOfAlignment_Object = MibScalar
rm10010mpAlmHostTxOutOfAlignment = _Rm10010mpAlmHostTxOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 52, 14),
    _Rm10010mpAlmHostTxOutOfAlignment_Type()
)
rm10010mpAlmHostTxOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmHostTxOutOfAlignment.setStatus("current")
_Rm10010mpAlmHostTxLossOfAlignment_Type = EkiOnOff
_Rm10010mpAlmHostTxLossOfAlignment_Object = MibScalar
rm10010mpAlmHostTxLossOfAlignment = _Rm10010mpAlmHostTxLossOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 52, 15),
    _Rm10010mpAlmHostTxLossOfAlignment_Type()
)
rm10010mpAlmHostTxLossOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmHostTxLossOfAlignment.setStatus("current")
_Rm10010mpAlmHostTxCdrLockFault_Type = EkiOnOff
_Rm10010mpAlmHostTxCdrLockFault_Object = MibScalar
rm10010mpAlmHostTxCdrLockFault = _Rm10010mpAlmHostTxCdrLockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 52, 16),
    _Rm10010mpAlmHostTxCdrLockFault_Type()
)
rm10010mpAlmHostTxCdrLockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmHostTxCdrLockFault.setStatus("current")
_Rm10010mpAlmmsaHostRxAlignment_ObjectIdentity = ObjectIdentity
rm10010mpAlmmsaHostRxAlignment = _Rm10010mpAlmmsaHostRxAlignment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 53)
)
_Rm10010mpAlmHostRxCmuLockFault_Type = EkiOnOff
_Rm10010mpAlmHostRxCmuLockFault_Object = MibScalar
rm10010mpAlmHostRxCmuLockFault = _Rm10010mpAlmHostRxCmuLockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 53, 14),
    _Rm10010mpAlmHostRxCmuLockFault_Type()
)
rm10010mpAlmHostRxCmuLockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmHostRxCmuLockFault.setStatus("current")
_Rm10010mpAlmHostRxOutOfAlignment_Type = EkiOnOff
_Rm10010mpAlmHostRxOutOfAlignment_Object = MibScalar
rm10010mpAlmHostRxOutOfAlignment = _Rm10010mpAlmHostRxOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 53, 15),
    _Rm10010mpAlmHostRxOutOfAlignment_Type()
)
rm10010mpAlmHostRxOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmHostRxOutOfAlignment.setStatus("current")
_Rm10010mpAlmHostRxLossOfAlignment_Type = EkiOnOff
_Rm10010mpAlmHostRxLossOfAlignment_Object = MibScalar
rm10010mpAlmHostRxLossOfAlignment = _Rm10010mpAlmHostRxLossOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 1, 3, 53, 16),
    _Rm10010mpAlmHostRxLossOfAlignment_Type()
)
rm10010mpAlmHostRxLossOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmHostRxLossOfAlignment.setStatus("current")
_Rm10010mpAlmClient_ObjectIdentity = ObjectIdentity
rm10010mpAlmClient = _Rm10010mpAlmClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2)
)
_Rm10010mpAlmClientNurg_ObjectIdentity = ObjectIdentity
rm10010mpAlmClientNurg = _Rm10010mpAlmClientNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 1)
)
_Rm10010mpAlmclientNetworkLaneAlarmWarningTable_Object = MibTable
rm10010mpAlmclientNetworkLaneAlarmWarningTable = _Rm10010mpAlmclientNetworkLaneAlarmWarningTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 1, 56)
)
if mibBuilder.loadTexts:
    rm10010mpAlmclientNetworkLaneAlarmWarningTable.setStatus("current")
_Rm10010mpAlmclientNetworkLaneAlarmWarningEntry_Object = MibTableRow
rm10010mpAlmclientNetworkLaneAlarmWarningEntry = _Rm10010mpAlmclientNetworkLaneAlarmWarningEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 1, 56, 1)
)
rm10010mpAlmclientNetworkLaneAlarmWarningEntry.setIndexNames(
    (0, "EKINOPS-Rm10010mp-MIB", "rm10010mpAlmclientNetworkLaneAlarmWarningIndex"),
)
if mibBuilder.loadTexts:
    rm10010mpAlmclientNetworkLaneAlarmWarningEntry.setStatus("current")


class _Rm10010mpAlmclientNetworkLaneAlarmWarningIndex_Type(Integer32):
    """Custom type rm10010mpAlmclientNetworkLaneAlarmWarningIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010mpAlmclientNetworkLaneAlarmWarningIndex_Type.__name__ = "Integer32"
_Rm10010mpAlmclientNetworkLaneAlarmWarningIndex_Object = MibTableColumn
rm10010mpAlmclientNetworkLaneAlarmWarningIndex = _Rm10010mpAlmclientNetworkLaneAlarmWarningIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 1, 56, 1, 1),
    _Rm10010mpAlmclientNetworkLaneAlarmWarningIndex_Type()
)
rm10010mpAlmclientNetworkLaneAlarmWarningIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmclientNetworkLaneAlarmWarningIndex.setStatus("current")
_Rm10010mpAlmClientRxPowerLowAlarmPortn_Type = EkiOnOff
_Rm10010mpAlmClientRxPowerLowAlarmPortn_Object = MibTableColumn
rm10010mpAlmClientRxPowerLowAlarmPortn = _Rm10010mpAlmClientRxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 1, 56, 1, 2),
    _Rm10010mpAlmClientRxPowerLowAlarmPortn_Type()
)
rm10010mpAlmClientRxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmClientRxPowerLowAlarmPortn.setStatus("current")
_Rm10010mpAlmClientRxPowerLowWarningPortn_Type = EkiOnOff
_Rm10010mpAlmClientRxPowerLowWarningPortn_Object = MibTableColumn
rm10010mpAlmClientRxPowerLowWarningPortn = _Rm10010mpAlmClientRxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 1, 56, 1, 3),
    _Rm10010mpAlmClientRxPowerLowWarningPortn_Type()
)
rm10010mpAlmClientRxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmClientRxPowerLowWarningPortn.setStatus("current")
_Rm10010mpAlmClientRxPowerHighWarningPortn_Type = EkiOnOff
_Rm10010mpAlmClientRxPowerHighWarningPortn_Object = MibTableColumn
rm10010mpAlmClientRxPowerHighWarningPortn = _Rm10010mpAlmClientRxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 1, 56, 1, 4),
    _Rm10010mpAlmClientRxPowerHighWarningPortn_Type()
)
rm10010mpAlmClientRxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmClientRxPowerHighWarningPortn.setStatus("current")
_Rm10010mpAlmClientRxPowerHighAlarmPortn_Type = EkiOnOff
_Rm10010mpAlmClientRxPowerHighAlarmPortn_Object = MibTableColumn
rm10010mpAlmClientRxPowerHighAlarmPortn = _Rm10010mpAlmClientRxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 1, 56, 1, 5),
    _Rm10010mpAlmClientRxPowerHighAlarmPortn_Type()
)
rm10010mpAlmClientRxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmClientRxPowerHighAlarmPortn.setStatus("current")
_Rm10010mpAlmLaserTempLowAlarmPortn_Type = EkiOnOff
_Rm10010mpAlmLaserTempLowAlarmPortn_Object = MibTableColumn
rm10010mpAlmLaserTempLowAlarmPortn = _Rm10010mpAlmLaserTempLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 1, 56, 1, 6),
    _Rm10010mpAlmLaserTempLowAlarmPortn_Type()
)
rm10010mpAlmLaserTempLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmLaserTempLowAlarmPortn.setStatus("current")
_Rm10010mpAlmClientLaserTempLowWarningPortn_Type = EkiOnOff
_Rm10010mpAlmClientLaserTempLowWarningPortn_Object = MibTableColumn
rm10010mpAlmClientLaserTempLowWarningPortn = _Rm10010mpAlmClientLaserTempLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 1, 56, 1, 7),
    _Rm10010mpAlmClientLaserTempLowWarningPortn_Type()
)
rm10010mpAlmClientLaserTempLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmClientLaserTempLowWarningPortn.setStatus("current")
_Rm10010mpAlmClientLaserTempHighWarningPortn_Type = EkiOnOff
_Rm10010mpAlmClientLaserTempHighWarningPortn_Object = MibTableColumn
rm10010mpAlmClientLaserTempHighWarningPortn = _Rm10010mpAlmClientLaserTempHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 1, 56, 1, 8),
    _Rm10010mpAlmClientLaserTempHighWarningPortn_Type()
)
rm10010mpAlmClientLaserTempHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmClientLaserTempHighWarningPortn.setStatus("current")
_Rm10010mpAlmClientLaserTempHighAlarmPortn_Type = EkiOnOff
_Rm10010mpAlmClientLaserTempHighAlarmPortn_Object = MibTableColumn
rm10010mpAlmClientLaserTempHighAlarmPortn = _Rm10010mpAlmClientLaserTempHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 1, 56, 1, 9),
    _Rm10010mpAlmClientLaserTempHighAlarmPortn_Type()
)
rm10010mpAlmClientLaserTempHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmClientLaserTempHighAlarmPortn.setStatus("current")
_Rm10010mpAlmClientTxPowerLowAlarmPortn_Type = EkiOnOff
_Rm10010mpAlmClientTxPowerLowAlarmPortn_Object = MibTableColumn
rm10010mpAlmClientTxPowerLowAlarmPortn = _Rm10010mpAlmClientTxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 1, 56, 1, 10),
    _Rm10010mpAlmClientTxPowerLowAlarmPortn_Type()
)
rm10010mpAlmClientTxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmClientTxPowerLowAlarmPortn.setStatus("current")
_Rm10010mpAlmClientTxPowerLowWarningPortn_Type = EkiOnOff
_Rm10010mpAlmClientTxPowerLowWarningPortn_Object = MibTableColumn
rm10010mpAlmClientTxPowerLowWarningPortn = _Rm10010mpAlmClientTxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 1, 56, 1, 11),
    _Rm10010mpAlmClientTxPowerLowWarningPortn_Type()
)
rm10010mpAlmClientTxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmClientTxPowerLowWarningPortn.setStatus("current")
_Rm10010mpAlmClientTxPowerHighWarningPortn_Type = EkiOnOff
_Rm10010mpAlmClientTxPowerHighWarningPortn_Object = MibTableColumn
rm10010mpAlmClientTxPowerHighWarningPortn = _Rm10010mpAlmClientTxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 1, 56, 1, 12),
    _Rm10010mpAlmClientTxPowerHighWarningPortn_Type()
)
rm10010mpAlmClientTxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmClientTxPowerHighWarningPortn.setStatus("current")
_Rm10010mpAlmClientTxPowerHighAlarmPortn_Type = EkiOnOff
_Rm10010mpAlmClientTxPowerHighAlarmPortn_Object = MibTableColumn
rm10010mpAlmClientTxPowerHighAlarmPortn = _Rm10010mpAlmClientTxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 1, 56, 1, 13),
    _Rm10010mpAlmClientTxPowerHighAlarmPortn_Type()
)
rm10010mpAlmClientTxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmClientTxPowerHighAlarmPortn.setStatus("current")
_Rm10010mpAlmClientBiasLowAlarmPortn_Type = EkiOnOff
_Rm10010mpAlmClientBiasLowAlarmPortn_Object = MibTableColumn
rm10010mpAlmClientBiasLowAlarmPortn = _Rm10010mpAlmClientBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 1, 56, 1, 14),
    _Rm10010mpAlmClientBiasLowAlarmPortn_Type()
)
rm10010mpAlmClientBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmClientBiasLowAlarmPortn.setStatus("current")
_Rm10010mpAlmClientBiasLowWarningPortn_Type = EkiOnOff
_Rm10010mpAlmClientBiasLowWarningPortn_Object = MibTableColumn
rm10010mpAlmClientBiasLowWarningPortn = _Rm10010mpAlmClientBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 1, 56, 1, 15),
    _Rm10010mpAlmClientBiasLowWarningPortn_Type()
)
rm10010mpAlmClientBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmClientBiasLowWarningPortn.setStatus("current")
_Rm10010mpAlmClientBiasHighWarningPortn_Type = EkiOnOff
_Rm10010mpAlmClientBiasHighWarningPortn_Object = MibTableColumn
rm10010mpAlmClientBiasHighWarningPortn = _Rm10010mpAlmClientBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 1, 56, 1, 16),
    _Rm10010mpAlmClientBiasHighWarningPortn_Type()
)
rm10010mpAlmClientBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmClientBiasHighWarningPortn.setStatus("current")
_Rm10010mpAlmClientBiasHighAlarmPortn_Type = EkiOnOff
_Rm10010mpAlmClientBiasHighAlarmPortn_Object = MibTableColumn
rm10010mpAlmClientBiasHighAlarmPortn = _Rm10010mpAlmClientBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 1, 56, 1, 17),
    _Rm10010mpAlmClientBiasHighAlarmPortn_Type()
)
rm10010mpAlmClientBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmClientBiasHighAlarmPortn.setStatus("current")
_Rm10010mpAlmclientSfpWarnDdmTable_Object = MibTable
rm10010mpAlmclientSfpWarnDdmTable = _Rm10010mpAlmclientSfpWarnDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 1, 232)
)
if mibBuilder.loadTexts:
    rm10010mpAlmclientSfpWarnDdmTable.setStatus("current")
_Rm10010mpAlmclientSfpWarnDdmEntry_Object = MibTableRow
rm10010mpAlmclientSfpWarnDdmEntry = _Rm10010mpAlmclientSfpWarnDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 1, 232, 1)
)
rm10010mpAlmclientSfpWarnDdmEntry.setIndexNames(
    (0, "EKINOPS-Rm10010mp-MIB", "rm10010mpAlmclientSfpWarnDdmIndex"),
)
if mibBuilder.loadTexts:
    rm10010mpAlmclientSfpWarnDdmEntry.setStatus("current")


class _Rm10010mpAlmclientSfpWarnDdmIndex_Type(Integer32):
    """Custom type rm10010mpAlmclientSfpWarnDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010mpAlmclientSfpWarnDdmIndex_Type.__name__ = "Integer32"
_Rm10010mpAlmclientSfpWarnDdmIndex_Object = MibTableColumn
rm10010mpAlmclientSfpWarnDdmIndex = _Rm10010mpAlmclientSfpWarnDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 1, 232, 1, 1),
    _Rm10010mpAlmclientSfpWarnDdmIndex_Type()
)
rm10010mpAlmclientSfpWarnDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmclientSfpWarnDdmIndex.setStatus("current")
_Rm10010mpAlmTxPwLowWngPortn_Type = EkiOnOff
_Rm10010mpAlmTxPwLowWngPortn_Object = MibTableColumn
rm10010mpAlmTxPwLowWngPortn = _Rm10010mpAlmTxPwLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 1, 232, 1, 2),
    _Rm10010mpAlmTxPwLowWngPortn_Type()
)
rm10010mpAlmTxPwLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmTxPwLowWngPortn.setStatus("current")
_Rm10010mpAlmTxPwrHighWngPortn_Type = EkiOnOff
_Rm10010mpAlmTxPwrHighWngPortn_Object = MibTableColumn
rm10010mpAlmTxPwrHighWngPortn = _Rm10010mpAlmTxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 1, 232, 1, 3),
    _Rm10010mpAlmTxPwrHighWngPortn_Type()
)
rm10010mpAlmTxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmTxPwrHighWngPortn.setStatus("current")
_Rm10010mpAlmTxBiasLowWngPortn_Type = EkiOnOff
_Rm10010mpAlmTxBiasLowWngPortn_Object = MibTableColumn
rm10010mpAlmTxBiasLowWngPortn = _Rm10010mpAlmTxBiasLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 1, 232, 1, 4),
    _Rm10010mpAlmTxBiasLowWngPortn_Type()
)
rm10010mpAlmTxBiasLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmTxBiasLowWngPortn.setStatus("current")
_Rm10010mpAlmTxBiasHighWngPortn_Type = EkiOnOff
_Rm10010mpAlmTxBiasHighWngPortn_Object = MibTableColumn
rm10010mpAlmTxBiasHighWngPortn = _Rm10010mpAlmTxBiasHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 1, 232, 1, 5),
    _Rm10010mpAlmTxBiasHighWngPortn_Type()
)
rm10010mpAlmTxBiasHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmTxBiasHighWngPortn.setStatus("current")
_Rm10010mpAlmVccLowWngPortn_Type = EkiOnOff
_Rm10010mpAlmVccLowWngPortn_Object = MibTableColumn
rm10010mpAlmVccLowWngPortn = _Rm10010mpAlmVccLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 1, 232, 1, 6),
    _Rm10010mpAlmVccLowWngPortn_Type()
)
rm10010mpAlmVccLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmVccLowWngPortn.setStatus("current")
_Rm10010mpAlmVccHighWngPortn_Type = EkiOnOff
_Rm10010mpAlmVccHighWngPortn_Object = MibTableColumn
rm10010mpAlmVccHighWngPortn = _Rm10010mpAlmVccHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 1, 232, 1, 7),
    _Rm10010mpAlmVccHighWngPortn_Type()
)
rm10010mpAlmVccHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmVccHighWngPortn.setStatus("current")
_Rm10010mpAlmTempLowWngPortn_Type = EkiOnOff
_Rm10010mpAlmTempLowWngPortn_Object = MibTableColumn
rm10010mpAlmTempLowWngPortn = _Rm10010mpAlmTempLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 1, 232, 1, 8),
    _Rm10010mpAlmTempLowWngPortn_Type()
)
rm10010mpAlmTempLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmTempLowWngPortn.setStatus("current")
_Rm10010mpAlmTempHighWngPortn_Type = EkiOnOff
_Rm10010mpAlmTempHighWngPortn_Object = MibTableColumn
rm10010mpAlmTempHighWngPortn = _Rm10010mpAlmTempHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 1, 232, 1, 9),
    _Rm10010mpAlmTempHighWngPortn_Type()
)
rm10010mpAlmTempHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmTempHighWngPortn.setStatus("current")
_Rm10010mpAlmRxPwrLowWngPortn_Type = EkiOnOff
_Rm10010mpAlmRxPwrLowWngPortn_Object = MibTableColumn
rm10010mpAlmRxPwrLowWngPortn = _Rm10010mpAlmRxPwrLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 1, 232, 1, 16),
    _Rm10010mpAlmRxPwrLowWngPortn_Type()
)
rm10010mpAlmRxPwrLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmRxPwrLowWngPortn.setStatus("current")
_Rm10010mpAlmRxPwrHighWngPortn_Type = EkiOnOff
_Rm10010mpAlmRxPwrHighWngPortn_Object = MibTableColumn
rm10010mpAlmRxPwrHighWngPortn = _Rm10010mpAlmRxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 1, 232, 1, 17),
    _Rm10010mpAlmRxPwrHighWngPortn_Type()
)
rm10010mpAlmRxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmRxPwrHighWngPortn.setStatus("current")
_Rm10010mpAlmClientUrg_ObjectIdentity = ObjectIdentity
rm10010mpAlmClientUrg = _Rm10010mpAlmClientUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 2)
)
_Rm10010mpAlmclientNetworkLaneFaultTable_Object = MibTable
rm10010mpAlmclientNetworkLaneFaultTable = _Rm10010mpAlmclientNetworkLaneFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 2, 72)
)
if mibBuilder.loadTexts:
    rm10010mpAlmclientNetworkLaneFaultTable.setStatus("current")
_Rm10010mpAlmclientNetworkLaneFaultEntry_Object = MibTableRow
rm10010mpAlmclientNetworkLaneFaultEntry = _Rm10010mpAlmclientNetworkLaneFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 2, 72, 1)
)
rm10010mpAlmclientNetworkLaneFaultEntry.setIndexNames(
    (0, "EKINOPS-Rm10010mp-MIB", "rm10010mpAlmclientNetworkLaneFaultIndex"),
)
if mibBuilder.loadTexts:
    rm10010mpAlmclientNetworkLaneFaultEntry.setStatus("current")


class _Rm10010mpAlmclientNetworkLaneFaultIndex_Type(Integer32):
    """Custom type rm10010mpAlmclientNetworkLaneFaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010mpAlmclientNetworkLaneFaultIndex_Type.__name__ = "Integer32"
_Rm10010mpAlmclientNetworkLaneFaultIndex_Object = MibTableColumn
rm10010mpAlmclientNetworkLaneFaultIndex = _Rm10010mpAlmclientNetworkLaneFaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 2, 72, 1, 1),
    _Rm10010mpAlmclientNetworkLaneFaultIndex_Type()
)
rm10010mpAlmclientNetworkLaneFaultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmclientNetworkLaneFaultIndex.setStatus("current")
_Rm10010mpAlmClientLaneRxFifoErrorPortn_Type = EkiOnOff
_Rm10010mpAlmClientLaneRxFifoErrorPortn_Object = MibTableColumn
rm10010mpAlmClientLaneRxFifoErrorPortn = _Rm10010mpAlmClientLaneRxFifoErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 2, 72, 1, 4),
    _Rm10010mpAlmClientLaneRxFifoErrorPortn_Type()
)
rm10010mpAlmClientLaneRxFifoErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmClientLaneRxFifoErrorPortn.setStatus("current")
_Rm10010mpAlmClientLaneRxLolPortn_Type = EkiOnOff
_Rm10010mpAlmClientLaneRxLolPortn_Object = MibTableColumn
rm10010mpAlmClientLaneRxLolPortn = _Rm10010mpAlmClientLaneRxLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 2, 72, 1, 5),
    _Rm10010mpAlmClientLaneRxLolPortn_Type()
)
rm10010mpAlmClientLaneRxLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmClientLaneRxLolPortn.setStatus("current")
_Rm10010mpAlmClientLaneRxLosPortn_Type = EkiOnOff
_Rm10010mpAlmClientLaneRxLosPortn_Object = MibTableColumn
rm10010mpAlmClientLaneRxLosPortn = _Rm10010mpAlmClientLaneRxLosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 2, 72, 1, 6),
    _Rm10010mpAlmClientLaneRxLosPortn_Type()
)
rm10010mpAlmClientLaneRxLosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmClientLaneRxLosPortn.setStatus("current")
_Rm10010mpAlmClientLaneTxLolPortn_Type = EkiOnOff
_Rm10010mpAlmClientLaneTxLolPortn_Object = MibTableColumn
rm10010mpAlmClientLaneTxLolPortn = _Rm10010mpAlmClientLaneTxLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 2, 72, 1, 8),
    _Rm10010mpAlmClientLaneTxLolPortn_Type()
)
rm10010mpAlmClientLaneTxLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmClientLaneTxLolPortn.setStatus("current")
_Rm10010mpAlmClientLaneTxLosfPortn_Type = EkiOnOff
_Rm10010mpAlmClientLaneTxLosfPortn_Object = MibTableColumn
rm10010mpAlmClientLaneTxLosfPortn = _Rm10010mpAlmClientLaneTxLosfPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 2, 72, 1, 9),
    _Rm10010mpAlmClientLaneTxLosfPortn_Type()
)
rm10010mpAlmClientLaneTxLosfPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmClientLaneTxLosfPortn.setStatus("current")
_Rm10010mpAlmClientLaneApdPowerSupplyPortn_Type = EkiOnOff
_Rm10010mpAlmClientLaneApdPowerSupplyPortn_Object = MibTableColumn
rm10010mpAlmClientLaneApdPowerSupplyPortn = _Rm10010mpAlmClientLaneApdPowerSupplyPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 2, 72, 1, 15),
    _Rm10010mpAlmClientLaneApdPowerSupplyPortn_Type()
)
rm10010mpAlmClientLaneApdPowerSupplyPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmClientLaneApdPowerSupplyPortn.setStatus("current")
_Rm10010mpAlmClientLaneWavelengthUnlockedPortn_Type = EkiOnOff
_Rm10010mpAlmClientLaneWavelengthUnlockedPortn_Object = MibTableColumn
rm10010mpAlmClientLaneWavelengthUnlockedPortn = _Rm10010mpAlmClientLaneWavelengthUnlockedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 2, 72, 1, 16),
    _Rm10010mpAlmClientLaneWavelengthUnlockedPortn_Type()
)
rm10010mpAlmClientLaneWavelengthUnlockedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmClientLaneWavelengthUnlockedPortn.setStatus("current")
_Rm10010mpAlmClientLaneTecFaultPortn_Type = EkiOnOff
_Rm10010mpAlmClientLaneTecFaultPortn_Object = MibTableColumn
rm10010mpAlmClientLaneTecFaultPortn = _Rm10010mpAlmClientLaneTecFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 2, 72, 1, 17),
    _Rm10010mpAlmClientLaneTecFaultPortn_Type()
)
rm10010mpAlmClientLaneTecFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmClientLaneTecFaultPortn.setStatus("current")
_Rm10010mpAlmclientHostLaneFaultTable_Object = MibTable
rm10010mpAlmclientHostLaneFaultTable = _Rm10010mpAlmclientHostLaneFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 2, 88)
)
if mibBuilder.loadTexts:
    rm10010mpAlmclientHostLaneFaultTable.setStatus("current")
_Rm10010mpAlmclientHostLaneFaultEntry_Object = MibTableRow
rm10010mpAlmclientHostLaneFaultEntry = _Rm10010mpAlmclientHostLaneFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 2, 88, 1)
)
rm10010mpAlmclientHostLaneFaultEntry.setIndexNames(
    (0, "EKINOPS-Rm10010mp-MIB", "rm10010mpAlmclientHostLaneFaultIndex"),
)
if mibBuilder.loadTexts:
    rm10010mpAlmclientHostLaneFaultEntry.setStatus("current")


class _Rm10010mpAlmclientHostLaneFaultIndex_Type(Integer32):
    """Custom type rm10010mpAlmclientHostLaneFaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010mpAlmclientHostLaneFaultIndex_Type.__name__ = "Integer32"
_Rm10010mpAlmclientHostLaneFaultIndex_Object = MibTableColumn
rm10010mpAlmclientHostLaneFaultIndex = _Rm10010mpAlmclientHostLaneFaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 2, 88, 1, 1),
    _Rm10010mpAlmclientHostLaneFaultIndex_Type()
)
rm10010mpAlmclientHostLaneFaultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmclientHostLaneFaultIndex.setStatus("current")
_Rm10010mpAlmClientLossOfSyncPortn_Type = EkiOnOff
_Rm10010mpAlmClientLossOfSyncPortn_Object = MibTableColumn
rm10010mpAlmClientLossOfSyncPortn = _Rm10010mpAlmClientLossOfSyncPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 2, 88, 1, 2),
    _Rm10010mpAlmClientLossOfSyncPortn_Type()
)
rm10010mpAlmClientLossOfSyncPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmClientLossOfSyncPortn.setStatus("current")
_Rm10010mpAlmClientInputLossOfSigPortn_Type = EkiOnOff
_Rm10010mpAlmClientInputLossOfSigPortn_Object = MibTableColumn
rm10010mpAlmClientInputLossOfSigPortn = _Rm10010mpAlmClientInputLossOfSigPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 2, 88, 1, 3),
    _Rm10010mpAlmClientInputLossOfSigPortn_Type()
)
rm10010mpAlmClientInputLossOfSigPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmClientInputLossOfSigPortn.setStatus("current")
_Rm10010mpAlmClientLanesMarkerUnlockPortn_Type = EkiOnOff
_Rm10010mpAlmClientLanesMarkerUnlockPortn_Object = MibTableColumn
rm10010mpAlmClientLanesMarkerUnlockPortn = _Rm10010mpAlmClientLanesMarkerUnlockPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 2, 88, 1, 4),
    _Rm10010mpAlmClientLanesMarkerUnlockPortn_Type()
)
rm10010mpAlmClientLanesMarkerUnlockPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmClientLanesMarkerUnlockPortn.setStatus("current")
_Rm10010mpAlmClientLanes6466UnlockPortn_Type = EkiOnOff
_Rm10010mpAlmClientLanes6466UnlockPortn_Object = MibTableColumn
rm10010mpAlmClientLanes6466UnlockPortn = _Rm10010mpAlmClientLanes6466UnlockPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 2, 88, 1, 5),
    _Rm10010mpAlmClientLanes6466UnlockPortn_Type()
)
rm10010mpAlmClientLanes6466UnlockPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmClientLanes6466UnlockPortn.setStatus("current")
_Rm10010mpAlmClientLanesNotAlignedPortn_Type = EkiOnOff
_Rm10010mpAlmClientLanesNotAlignedPortn_Object = MibTableColumn
rm10010mpAlmClientLanesNotAlignedPortn = _Rm10010mpAlmClientLanesNotAlignedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 2, 88, 1, 6),
    _Rm10010mpAlmClientLanesNotAlignedPortn_Type()
)
rm10010mpAlmClientLanesNotAlignedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmClientLanesNotAlignedPortn.setStatus("current")
_Rm10010mpAlmClientCsfDetectedPortn_Type = EkiOnOff
_Rm10010mpAlmClientCsfDetectedPortn_Object = MibTableColumn
rm10010mpAlmClientCsfDetectedPortn = _Rm10010mpAlmClientCsfDetectedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 2, 88, 1, 7),
    _Rm10010mpAlmClientCsfDetectedPortn_Type()
)
rm10010mpAlmClientCsfDetectedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmClientCsfDetectedPortn.setStatus("current")
_Rm10010mpAlmClientTxHostLolPortn_Type = EkiOnOff
_Rm10010mpAlmClientTxHostLolPortn_Object = MibTableColumn
rm10010mpAlmClientTxHostLolPortn = _Rm10010mpAlmClientTxHostLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 2, 88, 1, 10),
    _Rm10010mpAlmClientTxHostLolPortn_Type()
)
rm10010mpAlmClientTxHostLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmClientTxHostLolPortn.setStatus("current")
_Rm10010mpAlmClientLaneTxFifoErrorPortn_Type = EkiOnOff
_Rm10010mpAlmClientLaneTxFifoErrorPortn_Object = MibTableColumn
rm10010mpAlmClientLaneTxFifoErrorPortn = _Rm10010mpAlmClientLaneTxFifoErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 2, 88, 1, 11),
    _Rm10010mpAlmClientLaneTxFifoErrorPortn_Type()
)
rm10010mpAlmClientLaneTxFifoErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmClientLaneTxFifoErrorPortn.setStatus("current")
_Rm10010mpAlmclientSfpAlmDdmTable_Object = MibTable
rm10010mpAlmclientSfpAlmDdmTable = _Rm10010mpAlmclientSfpAlmDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 2, 216)
)
if mibBuilder.loadTexts:
    rm10010mpAlmclientSfpAlmDdmTable.setStatus("current")
_Rm10010mpAlmclientSfpAlmDdmEntry_Object = MibTableRow
rm10010mpAlmclientSfpAlmDdmEntry = _Rm10010mpAlmclientSfpAlmDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 2, 216, 1)
)
rm10010mpAlmclientSfpAlmDdmEntry.setIndexNames(
    (0, "EKINOPS-Rm10010mp-MIB", "rm10010mpAlmclientSfpAlmDdmIndex"),
)
if mibBuilder.loadTexts:
    rm10010mpAlmclientSfpAlmDdmEntry.setStatus("current")


class _Rm10010mpAlmclientSfpAlmDdmIndex_Type(Integer32):
    """Custom type rm10010mpAlmclientSfpAlmDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010mpAlmclientSfpAlmDdmIndex_Type.__name__ = "Integer32"
_Rm10010mpAlmclientSfpAlmDdmIndex_Object = MibTableColumn
rm10010mpAlmclientSfpAlmDdmIndex = _Rm10010mpAlmclientSfpAlmDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 2, 216, 1, 1),
    _Rm10010mpAlmclientSfpAlmDdmIndex_Type()
)
rm10010mpAlmclientSfpAlmDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmclientSfpAlmDdmIndex.setStatus("current")
_Rm10010mpAlmTxPwrLowAlaPortn_Type = EkiOnOff
_Rm10010mpAlmTxPwrLowAlaPortn_Object = MibTableColumn
rm10010mpAlmTxPwrLowAlaPortn = _Rm10010mpAlmTxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 2, 216, 1, 2),
    _Rm10010mpAlmTxPwrLowAlaPortn_Type()
)
rm10010mpAlmTxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmTxPwrLowAlaPortn.setStatus("current")
_Rm10010mpAlmTxPwrHighAlaPortn_Type = EkiOnOff
_Rm10010mpAlmTxPwrHighAlaPortn_Object = MibTableColumn
rm10010mpAlmTxPwrHighAlaPortn = _Rm10010mpAlmTxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 2, 216, 1, 3),
    _Rm10010mpAlmTxPwrHighAlaPortn_Type()
)
rm10010mpAlmTxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmTxPwrHighAlaPortn.setStatus("current")
_Rm10010mpAlmTxBiasLowAlaPortn_Type = EkiOnOff
_Rm10010mpAlmTxBiasLowAlaPortn_Object = MibTableColumn
rm10010mpAlmTxBiasLowAlaPortn = _Rm10010mpAlmTxBiasLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 2, 216, 1, 4),
    _Rm10010mpAlmTxBiasLowAlaPortn_Type()
)
rm10010mpAlmTxBiasLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmTxBiasLowAlaPortn.setStatus("current")
_Rm10010mpAlmTxBiasHighAlaPortn_Type = EkiOnOff
_Rm10010mpAlmTxBiasHighAlaPortn_Object = MibTableColumn
rm10010mpAlmTxBiasHighAlaPortn = _Rm10010mpAlmTxBiasHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 2, 216, 1, 5),
    _Rm10010mpAlmTxBiasHighAlaPortn_Type()
)
rm10010mpAlmTxBiasHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmTxBiasHighAlaPortn.setStatus("current")
_Rm10010mpAlmVccLowAlaPortn_Type = EkiOnOff
_Rm10010mpAlmVccLowAlaPortn_Object = MibTableColumn
rm10010mpAlmVccLowAlaPortn = _Rm10010mpAlmVccLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 2, 216, 1, 6),
    _Rm10010mpAlmVccLowAlaPortn_Type()
)
rm10010mpAlmVccLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmVccLowAlaPortn.setStatus("current")
_Rm10010mpAlmVccHighAlaPortn_Type = EkiOnOff
_Rm10010mpAlmVccHighAlaPortn_Object = MibTableColumn
rm10010mpAlmVccHighAlaPortn = _Rm10010mpAlmVccHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 2, 216, 1, 7),
    _Rm10010mpAlmVccHighAlaPortn_Type()
)
rm10010mpAlmVccHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmVccHighAlaPortn.setStatus("current")
_Rm10010mpAlmTempLowAlaPortn_Type = EkiOnOff
_Rm10010mpAlmTempLowAlaPortn_Object = MibTableColumn
rm10010mpAlmTempLowAlaPortn = _Rm10010mpAlmTempLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 2, 216, 1, 8),
    _Rm10010mpAlmTempLowAlaPortn_Type()
)
rm10010mpAlmTempLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmTempLowAlaPortn.setStatus("current")
_Rm10010mpAlmTempHighAlaPortn_Type = EkiOnOff
_Rm10010mpAlmTempHighAlaPortn_Object = MibTableColumn
rm10010mpAlmTempHighAlaPortn = _Rm10010mpAlmTempHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 2, 216, 1, 9),
    _Rm10010mpAlmTempHighAlaPortn_Type()
)
rm10010mpAlmTempHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmTempHighAlaPortn.setStatus("current")
_Rm10010mpAlmRxPwrLowAlaPortn_Type = EkiOnOff
_Rm10010mpAlmRxPwrLowAlaPortn_Object = MibTableColumn
rm10010mpAlmRxPwrLowAlaPortn = _Rm10010mpAlmRxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 2, 216, 1, 16),
    _Rm10010mpAlmRxPwrLowAlaPortn_Type()
)
rm10010mpAlmRxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmRxPwrLowAlaPortn.setStatus("current")
_Rm10010mpAlmRxPwrHighAlaPortn_Type = EkiOnOff
_Rm10010mpAlmRxPwrHighAlaPortn_Object = MibTableColumn
rm10010mpAlmRxPwrHighAlaPortn = _Rm10010mpAlmRxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 2, 216, 1, 17),
    _Rm10010mpAlmRxPwrHighAlaPortn_Type()
)
rm10010mpAlmRxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmRxPwrHighAlaPortn.setStatus("current")
_Rm10010mpAlmClientCrit_ObjectIdentity = ObjectIdentity
rm10010mpAlmClientCrit = _Rm10010mpAlmClientCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 3)
)
_Rm10010mpAlmsynthAlmPortTable_Object = MibTable
rm10010mpAlmsynthAlmPortTable = _Rm10010mpAlmsynthAlmPortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 3, 8)
)
if mibBuilder.loadTexts:
    rm10010mpAlmsynthAlmPortTable.setStatus("current")
_Rm10010mpAlmsynthAlmPortEntry_Object = MibTableRow
rm10010mpAlmsynthAlmPortEntry = _Rm10010mpAlmsynthAlmPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 3, 8, 1)
)
rm10010mpAlmsynthAlmPortEntry.setIndexNames(
    (0, "EKINOPS-Rm10010mp-MIB", "rm10010mpAlmsynthAlmPortIndex"),
)
if mibBuilder.loadTexts:
    rm10010mpAlmsynthAlmPortEntry.setStatus("current")


class _Rm10010mpAlmsynthAlmPortIndex_Type(Integer32):
    """Custom type rm10010mpAlmsynthAlmPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010mpAlmsynthAlmPortIndex_Type.__name__ = "Integer32"
_Rm10010mpAlmsynthAlmPortIndex_Object = MibTableColumn
rm10010mpAlmsynthAlmPortIndex = _Rm10010mpAlmsynthAlmPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 3, 8, 1, 1),
    _Rm10010mpAlmsynthAlmPortIndex_Type()
)
rm10010mpAlmsynthAlmPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmsynthAlmPortIndex.setStatus("current")
_Rm10010mpAlmSfpAbsentPortn_Type = EkiOnOff
_Rm10010mpAlmSfpAbsentPortn_Object = MibTableColumn
rm10010mpAlmSfpAbsentPortn = _Rm10010mpAlmSfpAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 3, 8, 1, 2),
    _Rm10010mpAlmSfpAbsentPortn_Type()
)
rm10010mpAlmSfpAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmSfpAbsentPortn.setStatus("current")
_Rm10010mpAlmDdmAbsentPortn_Type = EkiOnOff
_Rm10010mpAlmDdmAbsentPortn_Object = MibTableColumn
rm10010mpAlmDdmAbsentPortn = _Rm10010mpAlmDdmAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 3, 8, 1, 3),
    _Rm10010mpAlmDdmAbsentPortn_Type()
)
rm10010mpAlmDdmAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmDdmAbsentPortn.setStatus("current")
_Rm10010mpAlmHwFailAccPortn_Type = EkiOnOff
_Rm10010mpAlmHwFailAccPortn_Object = MibTableColumn
rm10010mpAlmHwFailAccPortn = _Rm10010mpAlmHwFailAccPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 3, 8, 1, 5),
    _Rm10010mpAlmHwFailAccPortn_Type()
)
rm10010mpAlmHwFailAccPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmHwFailAccPortn.setStatus("current")
_Rm10010mpAlmDwLsdPortn_Type = EkiOnOff
_Rm10010mpAlmDwLsdPortn_Object = MibTableColumn
rm10010mpAlmDwLsdPortn = _Rm10010mpAlmDwLsdPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 3, 8, 1, 6),
    _Rm10010mpAlmDwLsdPortn_Type()
)
rm10010mpAlmDwLsdPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmDwLsdPortn.setStatus("current")
_Rm10010mpAlmClientLocalOosPortn_Type = EkiOnOff
_Rm10010mpAlmClientLocalOosPortn_Object = MibTableColumn
rm10010mpAlmClientLocalOosPortn = _Rm10010mpAlmClientLocalOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 3, 8, 1, 7),
    _Rm10010mpAlmClientLocalOosPortn_Type()
)
rm10010mpAlmClientLocalOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmClientLocalOosPortn.setStatus("current")
_Rm10010mpAlmClientRemoteOosPortn_Type = EkiOnOff
_Rm10010mpAlmClientRemoteOosPortn_Object = MibTableColumn
rm10010mpAlmClientRemoteOosPortn = _Rm10010mpAlmClientRemoteOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 3, 8, 1, 8),
    _Rm10010mpAlmClientRemoteOosPortn_Type()
)
rm10010mpAlmClientRemoteOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmClientRemoteOosPortn.setStatus("current")
_Rm10010mpAlmDwCaisPortn_Type = EkiOnOff
_Rm10010mpAlmDwCaisPortn_Object = MibTableColumn
rm10010mpAlmDwCaisPortn = _Rm10010mpAlmDwCaisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 3, 8, 1, 9),
    _Rm10010mpAlmDwCaisPortn_Type()
)
rm10010mpAlmDwCaisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmDwCaisPortn.setStatus("current")
_Rm10010mpAlmSfpDdmWarningPortn_Type = EkiOnOff
_Rm10010mpAlmSfpDdmWarningPortn_Object = MibTableColumn
rm10010mpAlmSfpDdmWarningPortn = _Rm10010mpAlmSfpDdmWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 3, 8, 1, 10),
    _Rm10010mpAlmSfpDdmWarningPortn_Type()
)
rm10010mpAlmSfpDdmWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmSfpDdmWarningPortn.setStatus("current")
_Rm10010mpAlmSfpDdmAlmPortn_Type = EkiOnOff
_Rm10010mpAlmSfpDdmAlmPortn_Object = MibTableColumn
rm10010mpAlmSfpDdmAlmPortn = _Rm10010mpAlmSfpDdmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 3, 8, 1, 11),
    _Rm10010mpAlmSfpDdmAlmPortn_Type()
)
rm10010mpAlmSfpDdmAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmSfpDdmAlmPortn.setStatus("current")
_Rm10010mpAlmFailAccPortn_Type = EkiOnOff
_Rm10010mpAlmFailAccPortn_Object = MibTableColumn
rm10010mpAlmFailAccPortn = _Rm10010mpAlmFailAccPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 3, 8, 1, 13),
    _Rm10010mpAlmFailAccPortn_Type()
)
rm10010mpAlmFailAccPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmFailAccPortn.setStatus("current")
_Rm10010mpAlmUpCsfPortn_Type = EkiOnOff
_Rm10010mpAlmUpCsfPortn_Object = MibTableColumn
rm10010mpAlmUpCsfPortn = _Rm10010mpAlmUpCsfPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 2, 3, 8, 1, 17),
    _Rm10010mpAlmUpCsfPortn_Type()
)
rm10010mpAlmUpCsfPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmUpCsfPortn.setStatus("current")
_Rm10010mpAlmLine_ObjectIdentity = ObjectIdentity
rm10010mpAlmLine = _Rm10010mpAlmLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3)
)
_Rm10010mpAlmLineNurg_ObjectIdentity = ObjectIdentity
rm10010mpAlmLineNurg = _Rm10010mpAlmLineNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 1)
)
_Rm10010mpAlmlineNetworkLaneAlarmWarning1Table_Object = MibTable
rm10010mpAlmlineNetworkLaneAlarmWarning1Table = _Rm10010mpAlmlineNetworkLaneAlarmWarning1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 1, 104)
)
if mibBuilder.loadTexts:
    rm10010mpAlmlineNetworkLaneAlarmWarning1Table.setStatus("current")
_Rm10010mpAlmlineNetworkLaneAlarmWarning1Entry_Object = MibTableRow
rm10010mpAlmlineNetworkLaneAlarmWarning1Entry = _Rm10010mpAlmlineNetworkLaneAlarmWarning1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 1, 104, 1)
)
rm10010mpAlmlineNetworkLaneAlarmWarning1Entry.setIndexNames(
    (0, "EKINOPS-Rm10010mp-MIB", "rm10010mpAlmlineNetworkLaneAlarmWarning1Index"),
)
if mibBuilder.loadTexts:
    rm10010mpAlmlineNetworkLaneAlarmWarning1Entry.setStatus("current")


class _Rm10010mpAlmlineNetworkLaneAlarmWarning1Index_Type(Integer32):
    """Custom type rm10010mpAlmlineNetworkLaneAlarmWarning1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010mpAlmlineNetworkLaneAlarmWarning1Index_Type.__name__ = "Integer32"
_Rm10010mpAlmlineNetworkLaneAlarmWarning1Index_Object = MibTableColumn
rm10010mpAlmlineNetworkLaneAlarmWarning1Index = _Rm10010mpAlmlineNetworkLaneAlarmWarning1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 1, 104, 1, 1),
    _Rm10010mpAlmlineNetworkLaneAlarmWarning1Index_Type()
)
rm10010mpAlmlineNetworkLaneAlarmWarning1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmlineNetworkLaneAlarmWarning1Index.setStatus("current")
_Rm10010mpAlmLineRxPowerLowAlarmPortn_Type = EkiOnOff
_Rm10010mpAlmLineRxPowerLowAlarmPortn_Object = MibTableColumn
rm10010mpAlmLineRxPowerLowAlarmPortn = _Rm10010mpAlmLineRxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 1, 104, 1, 2),
    _Rm10010mpAlmLineRxPowerLowAlarmPortn_Type()
)
rm10010mpAlmLineRxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmLineRxPowerLowAlarmPortn.setStatus("current")
_Rm10010mpAlmLineRxPowerLowWarningPortn_Type = EkiOnOff
_Rm10010mpAlmLineRxPowerLowWarningPortn_Object = MibTableColumn
rm10010mpAlmLineRxPowerLowWarningPortn = _Rm10010mpAlmLineRxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 1, 104, 1, 3),
    _Rm10010mpAlmLineRxPowerLowWarningPortn_Type()
)
rm10010mpAlmLineRxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmLineRxPowerLowWarningPortn.setStatus("current")
_Rm10010mpAlmLineRxPowerHighWarningPortn_Type = EkiOnOff
_Rm10010mpAlmLineRxPowerHighWarningPortn_Object = MibTableColumn
rm10010mpAlmLineRxPowerHighWarningPortn = _Rm10010mpAlmLineRxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 1, 104, 1, 4),
    _Rm10010mpAlmLineRxPowerHighWarningPortn_Type()
)
rm10010mpAlmLineRxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmLineRxPowerHighWarningPortn.setStatus("current")
_Rm10010mpAlmLineRxPowerHighAlarmPortn_Type = EkiOnOff
_Rm10010mpAlmLineRxPowerHighAlarmPortn_Object = MibTableColumn
rm10010mpAlmLineRxPowerHighAlarmPortn = _Rm10010mpAlmLineRxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 1, 104, 1, 5),
    _Rm10010mpAlmLineRxPowerHighAlarmPortn_Type()
)
rm10010mpAlmLineRxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmLineRxPowerHighAlarmPortn.setStatus("current")
_Rm10010mpAlmLineLaserTempLowAlarmPortn_Type = EkiOnOff
_Rm10010mpAlmLineLaserTempLowAlarmPortn_Object = MibTableColumn
rm10010mpAlmLineLaserTempLowAlarmPortn = _Rm10010mpAlmLineLaserTempLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 1, 104, 1, 6),
    _Rm10010mpAlmLineLaserTempLowAlarmPortn_Type()
)
rm10010mpAlmLineLaserTempLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmLineLaserTempLowAlarmPortn.setStatus("current")
_Rm10010mpAlmLineLaserTempLowWarningPortn_Type = EkiOnOff
_Rm10010mpAlmLineLaserTempLowWarningPortn_Object = MibTableColumn
rm10010mpAlmLineLaserTempLowWarningPortn = _Rm10010mpAlmLineLaserTempLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 1, 104, 1, 7),
    _Rm10010mpAlmLineLaserTempLowWarningPortn_Type()
)
rm10010mpAlmLineLaserTempLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmLineLaserTempLowWarningPortn.setStatus("current")
_Rm10010mpAlmLineLaserTempHighWarningPortn_Type = EkiOnOff
_Rm10010mpAlmLineLaserTempHighWarningPortn_Object = MibTableColumn
rm10010mpAlmLineLaserTempHighWarningPortn = _Rm10010mpAlmLineLaserTempHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 1, 104, 1, 8),
    _Rm10010mpAlmLineLaserTempHighWarningPortn_Type()
)
rm10010mpAlmLineLaserTempHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmLineLaserTempHighWarningPortn.setStatus("current")
_Rm10010mpAlmLineLaserTempHighAlarmPortn_Type = EkiOnOff
_Rm10010mpAlmLineLaserTempHighAlarmPortn_Object = MibTableColumn
rm10010mpAlmLineLaserTempHighAlarmPortn = _Rm10010mpAlmLineLaserTempHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 1, 104, 1, 9),
    _Rm10010mpAlmLineLaserTempHighAlarmPortn_Type()
)
rm10010mpAlmLineLaserTempHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmLineLaserTempHighAlarmPortn.setStatus("current")
_Rm10010mpAlmLineTxPowerLowAlarmPortn_Type = EkiOnOff
_Rm10010mpAlmLineTxPowerLowAlarmPortn_Object = MibTableColumn
rm10010mpAlmLineTxPowerLowAlarmPortn = _Rm10010mpAlmLineTxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 1, 104, 1, 10),
    _Rm10010mpAlmLineTxPowerLowAlarmPortn_Type()
)
rm10010mpAlmLineTxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmLineTxPowerLowAlarmPortn.setStatus("current")
_Rm10010mpAlmLineTxPowerLowWarningPortn_Type = EkiOnOff
_Rm10010mpAlmLineTxPowerLowWarningPortn_Object = MibTableColumn
rm10010mpAlmLineTxPowerLowWarningPortn = _Rm10010mpAlmLineTxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 1, 104, 1, 11),
    _Rm10010mpAlmLineTxPowerLowWarningPortn_Type()
)
rm10010mpAlmLineTxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmLineTxPowerLowWarningPortn.setStatus("current")
_Rm10010mpAlmLineTxPowerHighWarningPortn_Type = EkiOnOff
_Rm10010mpAlmLineTxPowerHighWarningPortn_Object = MibTableColumn
rm10010mpAlmLineTxPowerHighWarningPortn = _Rm10010mpAlmLineTxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 1, 104, 1, 12),
    _Rm10010mpAlmLineTxPowerHighWarningPortn_Type()
)
rm10010mpAlmLineTxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmLineTxPowerHighWarningPortn.setStatus("current")
_Rm10010mpAlmLineTxPowerHighAlarmPortn_Type = EkiOnOff
_Rm10010mpAlmLineTxPowerHighAlarmPortn_Object = MibTableColumn
rm10010mpAlmLineTxPowerHighAlarmPortn = _Rm10010mpAlmLineTxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 1, 104, 1, 13),
    _Rm10010mpAlmLineTxPowerHighAlarmPortn_Type()
)
rm10010mpAlmLineTxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmLineTxPowerHighAlarmPortn.setStatus("current")
_Rm10010mpAlmLineBiasLowAlarmPortn_Type = EkiOnOff
_Rm10010mpAlmLineBiasLowAlarmPortn_Object = MibTableColumn
rm10010mpAlmLineBiasLowAlarmPortn = _Rm10010mpAlmLineBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 1, 104, 1, 14),
    _Rm10010mpAlmLineBiasLowAlarmPortn_Type()
)
rm10010mpAlmLineBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmLineBiasLowAlarmPortn.setStatus("current")
_Rm10010mpAlmLineBiasLowWarningPortn_Type = EkiOnOff
_Rm10010mpAlmLineBiasLowWarningPortn_Object = MibTableColumn
rm10010mpAlmLineBiasLowWarningPortn = _Rm10010mpAlmLineBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 1, 104, 1, 15),
    _Rm10010mpAlmLineBiasLowWarningPortn_Type()
)
rm10010mpAlmLineBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmLineBiasLowWarningPortn.setStatus("current")
_Rm10010mpAlmLineBiasHighWarningPortn_Type = EkiOnOff
_Rm10010mpAlmLineBiasHighWarningPortn_Object = MibTableColumn
rm10010mpAlmLineBiasHighWarningPortn = _Rm10010mpAlmLineBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 1, 104, 1, 16),
    _Rm10010mpAlmLineBiasHighWarningPortn_Type()
)
rm10010mpAlmLineBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmLineBiasHighWarningPortn.setStatus("current")
_Rm10010mpAlmLineBiasHighAlarmPortn_Type = EkiOnOff
_Rm10010mpAlmLineBiasHighAlarmPortn_Object = MibTableColumn
rm10010mpAlmLineBiasHighAlarmPortn = _Rm10010mpAlmLineBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 1, 104, 1, 17),
    _Rm10010mpAlmLineBiasHighAlarmPortn_Type()
)
rm10010mpAlmLineBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmLineBiasHighAlarmPortn.setStatus("current")
_Rm10010mpAlmlineNetworkLaneAlarmWarning2Table_Object = MibTable
rm10010mpAlmlineNetworkLaneAlarmWarning2Table = _Rm10010mpAlmlineNetworkLaneAlarmWarning2Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 1, 120)
)
if mibBuilder.loadTexts:
    rm10010mpAlmlineNetworkLaneAlarmWarning2Table.setStatus("current")
_Rm10010mpAlmlineNetworkLaneAlarmWarning2Entry_Object = MibTableRow
rm10010mpAlmlineNetworkLaneAlarmWarning2Entry = _Rm10010mpAlmlineNetworkLaneAlarmWarning2Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 1, 120, 1)
)
rm10010mpAlmlineNetworkLaneAlarmWarning2Entry.setIndexNames(
    (0, "EKINOPS-Rm10010mp-MIB", "rm10010mpAlmlineNetworkLaneAlarmWarning2Index"),
)
if mibBuilder.loadTexts:
    rm10010mpAlmlineNetworkLaneAlarmWarning2Entry.setStatus("current")


class _Rm10010mpAlmlineNetworkLaneAlarmWarning2Index_Type(Integer32):
    """Custom type rm10010mpAlmlineNetworkLaneAlarmWarning2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010mpAlmlineNetworkLaneAlarmWarning2Index_Type.__name__ = "Integer32"
_Rm10010mpAlmlineNetworkLaneAlarmWarning2Index_Object = MibTableColumn
rm10010mpAlmlineNetworkLaneAlarmWarning2Index = _Rm10010mpAlmlineNetworkLaneAlarmWarning2Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 1, 120, 1, 1),
    _Rm10010mpAlmlineNetworkLaneAlarmWarning2Index_Type()
)
rm10010mpAlmlineNetworkLaneAlarmWarning2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmlineNetworkLaneAlarmWarning2Index.setStatus("current")
_Rm10010mpAlmTxModulatorBiasLowAlarmPortn_Type = EkiOnOff
_Rm10010mpAlmTxModulatorBiasLowAlarmPortn_Object = MibTableColumn
rm10010mpAlmTxModulatorBiasLowAlarmPortn = _Rm10010mpAlmTxModulatorBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 1, 120, 1, 2),
    _Rm10010mpAlmTxModulatorBiasLowAlarmPortn_Type()
)
rm10010mpAlmTxModulatorBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmTxModulatorBiasLowAlarmPortn.setStatus("current")
_Rm10010mpAlmTxModulatorBiasLowWarningPortn_Type = EkiOnOff
_Rm10010mpAlmTxModulatorBiasLowWarningPortn_Object = MibTableColumn
rm10010mpAlmTxModulatorBiasLowWarningPortn = _Rm10010mpAlmTxModulatorBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 1, 120, 1, 3),
    _Rm10010mpAlmTxModulatorBiasLowWarningPortn_Type()
)
rm10010mpAlmTxModulatorBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmTxModulatorBiasLowWarningPortn.setStatus("current")
_Rm10010mpAlmTxModulatorBiasHighWarningPortn_Type = EkiOnOff
_Rm10010mpAlmTxModulatorBiasHighWarningPortn_Object = MibTableColumn
rm10010mpAlmTxModulatorBiasHighWarningPortn = _Rm10010mpAlmTxModulatorBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 1, 120, 1, 4),
    _Rm10010mpAlmTxModulatorBiasHighWarningPortn_Type()
)
rm10010mpAlmTxModulatorBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmTxModulatorBiasHighWarningPortn.setStatus("current")
_Rm10010mpAlmTxModulatorBiasHighAlarmPortn_Type = EkiOnOff
_Rm10010mpAlmTxModulatorBiasHighAlarmPortn_Object = MibTableColumn
rm10010mpAlmTxModulatorBiasHighAlarmPortn = _Rm10010mpAlmTxModulatorBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 1, 120, 1, 5),
    _Rm10010mpAlmTxModulatorBiasHighAlarmPortn_Type()
)
rm10010mpAlmTxModulatorBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmTxModulatorBiasHighAlarmPortn.setStatus("current")
_Rm10010mpAlmRxLaserTempLowAlarmPortn_Type = EkiOnOff
_Rm10010mpAlmRxLaserTempLowAlarmPortn_Object = MibTableColumn
rm10010mpAlmRxLaserTempLowAlarmPortn = _Rm10010mpAlmRxLaserTempLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 1, 120, 1, 6),
    _Rm10010mpAlmRxLaserTempLowAlarmPortn_Type()
)
rm10010mpAlmRxLaserTempLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmRxLaserTempLowAlarmPortn.setStatus("current")
_Rm10010mpAlmRxLaserTempLowWarningPortn_Type = EkiOnOff
_Rm10010mpAlmRxLaserTempLowWarningPortn_Object = MibTableColumn
rm10010mpAlmRxLaserTempLowWarningPortn = _Rm10010mpAlmRxLaserTempLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 1, 120, 1, 7),
    _Rm10010mpAlmRxLaserTempLowWarningPortn_Type()
)
rm10010mpAlmRxLaserTempLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmRxLaserTempLowWarningPortn.setStatus("current")
_Rm10010mpAlmRxLaserTempHighWarningPortn_Type = EkiOnOff
_Rm10010mpAlmRxLaserTempHighWarningPortn_Object = MibTableColumn
rm10010mpAlmRxLaserTempHighWarningPortn = _Rm10010mpAlmRxLaserTempHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 1, 120, 1, 8),
    _Rm10010mpAlmRxLaserTempHighWarningPortn_Type()
)
rm10010mpAlmRxLaserTempHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmRxLaserTempHighWarningPortn.setStatus("current")
_Rm10010mpAlmRxLaserTempHighAlarmPortn_Type = EkiOnOff
_Rm10010mpAlmRxLaserTempHighAlarmPortn_Object = MibTableColumn
rm10010mpAlmRxLaserTempHighAlarmPortn = _Rm10010mpAlmRxLaserTempHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 1, 120, 1, 9),
    _Rm10010mpAlmRxLaserTempHighAlarmPortn_Type()
)
rm10010mpAlmRxLaserTempHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmRxLaserTempHighAlarmPortn.setStatus("current")
_Rm10010mpAlmRxLaserOutputLowAlarmPortn_Type = EkiOnOff
_Rm10010mpAlmRxLaserOutputLowAlarmPortn_Object = MibTableColumn
rm10010mpAlmRxLaserOutputLowAlarmPortn = _Rm10010mpAlmRxLaserOutputLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 1, 120, 1, 10),
    _Rm10010mpAlmRxLaserOutputLowAlarmPortn_Type()
)
rm10010mpAlmRxLaserOutputLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmRxLaserOutputLowAlarmPortn.setStatus("current")
_Rm10010mpAlmRxLaserOutputLowWarningPortn_Type = EkiOnOff
_Rm10010mpAlmRxLaserOutputLowWarningPortn_Object = MibTableColumn
rm10010mpAlmRxLaserOutputLowWarningPortn = _Rm10010mpAlmRxLaserOutputLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 1, 120, 1, 11),
    _Rm10010mpAlmRxLaserOutputLowWarningPortn_Type()
)
rm10010mpAlmRxLaserOutputLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmRxLaserOutputLowWarningPortn.setStatus("current")
_Rm10010mpAlmRxLaserOutputHighWarningPortn_Type = EkiOnOff
_Rm10010mpAlmRxLaserOutputHighWarningPortn_Object = MibTableColumn
rm10010mpAlmRxLaserOutputHighWarningPortn = _Rm10010mpAlmRxLaserOutputHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 1, 120, 1, 12),
    _Rm10010mpAlmRxLaserOutputHighWarningPortn_Type()
)
rm10010mpAlmRxLaserOutputHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmRxLaserOutputHighWarningPortn.setStatus("current")
_Rm10010mpAlmRxLaserOutputHighAlarmPortn_Type = EkiOnOff
_Rm10010mpAlmRxLaserOutputHighAlarmPortn_Object = MibTableColumn
rm10010mpAlmRxLaserOutputHighAlarmPortn = _Rm10010mpAlmRxLaserOutputHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 1, 120, 1, 13),
    _Rm10010mpAlmRxLaserOutputHighAlarmPortn_Type()
)
rm10010mpAlmRxLaserOutputHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmRxLaserOutputHighAlarmPortn.setStatus("current")
_Rm10010mpAlmRxLaserBiasLowAlarmPortn_Type = EkiOnOff
_Rm10010mpAlmRxLaserBiasLowAlarmPortn_Object = MibTableColumn
rm10010mpAlmRxLaserBiasLowAlarmPortn = _Rm10010mpAlmRxLaserBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 1, 120, 1, 14),
    _Rm10010mpAlmRxLaserBiasLowAlarmPortn_Type()
)
rm10010mpAlmRxLaserBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmRxLaserBiasLowAlarmPortn.setStatus("current")
_Rm10010mpAlmRxLaserBiasLowWarningPortn_Type = EkiOnOff
_Rm10010mpAlmRxLaserBiasLowWarningPortn_Object = MibTableColumn
rm10010mpAlmRxLaserBiasLowWarningPortn = _Rm10010mpAlmRxLaserBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 1, 120, 1, 15),
    _Rm10010mpAlmRxLaserBiasLowWarningPortn_Type()
)
rm10010mpAlmRxLaserBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmRxLaserBiasLowWarningPortn.setStatus("current")
_Rm10010mpAlmRxLaserBiasHighWarningPortn_Type = EkiOnOff
_Rm10010mpAlmRxLaserBiasHighWarningPortn_Object = MibTableColumn
rm10010mpAlmRxLaserBiasHighWarningPortn = _Rm10010mpAlmRxLaserBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 1, 120, 1, 16),
    _Rm10010mpAlmRxLaserBiasHighWarningPortn_Type()
)
rm10010mpAlmRxLaserBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmRxLaserBiasHighWarningPortn.setStatus("current")
_Rm10010mpAlmRxLaserBiasHighAlarmPortn_Type = EkiOnOff
_Rm10010mpAlmRxLaserBiasHighAlarmPortn_Object = MibTableColumn
rm10010mpAlmRxLaserBiasHighAlarmPortn = _Rm10010mpAlmRxLaserBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 1, 120, 1, 17),
    _Rm10010mpAlmRxLaserBiasHighAlarmPortn_Type()
)
rm10010mpAlmRxLaserBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmRxLaserBiasHighAlarmPortn.setStatus("current")
_Rm10010mpAlmLineUrg_ObjectIdentity = ObjectIdentity
rm10010mpAlmLineUrg = _Rm10010mpAlmLineUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 2)
)
_Rm10010mpAlmlineNetworkLaneFaultTable_Object = MibTable
rm10010mpAlmlineNetworkLaneFaultTable = _Rm10010mpAlmlineNetworkLaneFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 2, 136)
)
if mibBuilder.loadTexts:
    rm10010mpAlmlineNetworkLaneFaultTable.setStatus("current")
_Rm10010mpAlmlineNetworkLaneFaultEntry_Object = MibTableRow
rm10010mpAlmlineNetworkLaneFaultEntry = _Rm10010mpAlmlineNetworkLaneFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 2, 136, 1)
)
rm10010mpAlmlineNetworkLaneFaultEntry.setIndexNames(
    (0, "EKINOPS-Rm10010mp-MIB", "rm10010mpAlmlineNetworkLaneFaultIndex"),
)
if mibBuilder.loadTexts:
    rm10010mpAlmlineNetworkLaneFaultEntry.setStatus("current")


class _Rm10010mpAlmlineNetworkLaneFaultIndex_Type(Integer32):
    """Custom type rm10010mpAlmlineNetworkLaneFaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010mpAlmlineNetworkLaneFaultIndex_Type.__name__ = "Integer32"
_Rm10010mpAlmlineNetworkLaneFaultIndex_Object = MibTableColumn
rm10010mpAlmlineNetworkLaneFaultIndex = _Rm10010mpAlmlineNetworkLaneFaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 2, 136, 1, 1),
    _Rm10010mpAlmlineNetworkLaneFaultIndex_Type()
)
rm10010mpAlmlineNetworkLaneFaultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmlineNetworkLaneFaultIndex.setStatus("current")
_Rm10010mpAlmLineLaneRxTecFaultPortn_Type = EkiOnOff
_Rm10010mpAlmLineLaneRxTecFaultPortn_Object = MibTableColumn
rm10010mpAlmLineLaneRxTecFaultPortn = _Rm10010mpAlmLineLaneRxTecFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 2, 136, 1, 3),
    _Rm10010mpAlmLineLaneRxTecFaultPortn_Type()
)
rm10010mpAlmLineLaneRxTecFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmLineLaneRxTecFaultPortn.setStatus("current")
_Rm10010mpAlmLineLaneRxFifoErrorPortn_Type = EkiOnOff
_Rm10010mpAlmLineLaneRxFifoErrorPortn_Object = MibTableColumn
rm10010mpAlmLineLaneRxFifoErrorPortn = _Rm10010mpAlmLineLaneRxFifoErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 2, 136, 1, 4),
    _Rm10010mpAlmLineLaneRxFifoErrorPortn_Type()
)
rm10010mpAlmLineLaneRxFifoErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmLineLaneRxFifoErrorPortn.setStatus("current")
_Rm10010mpAlmLineLaneRxLolPortn_Type = EkiOnOff
_Rm10010mpAlmLineLaneRxLolPortn_Object = MibTableColumn
rm10010mpAlmLineLaneRxLolPortn = _Rm10010mpAlmLineLaneRxLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 2, 136, 1, 5),
    _Rm10010mpAlmLineLaneRxLolPortn_Type()
)
rm10010mpAlmLineLaneRxLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmLineLaneRxLolPortn.setStatus("current")
_Rm10010mpAlmLineLaneRxLosPortn_Type = EkiOnOff
_Rm10010mpAlmLineLaneRxLosPortn_Object = MibTableColumn
rm10010mpAlmLineLaneRxLosPortn = _Rm10010mpAlmLineLaneRxLosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 2, 136, 1, 6),
    _Rm10010mpAlmLineLaneRxLosPortn_Type()
)
rm10010mpAlmLineLaneRxLosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmLineLaneRxLosPortn.setStatus("current")
_Rm10010mpAlmLineLaneTxLolPortn_Type = EkiOnOff
_Rm10010mpAlmLineLaneTxLolPortn_Object = MibTableColumn
rm10010mpAlmLineLaneTxLolPortn = _Rm10010mpAlmLineLaneTxLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 2, 136, 1, 8),
    _Rm10010mpAlmLineLaneTxLolPortn_Type()
)
rm10010mpAlmLineLaneTxLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmLineLaneTxLolPortn.setStatus("current")
_Rm10010mpAlmLineLaneTxLosfPortn_Type = EkiOnOff
_Rm10010mpAlmLineLaneTxLosfPortn_Object = MibTableColumn
rm10010mpAlmLineLaneTxLosfPortn = _Rm10010mpAlmLineLaneTxLosfPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 2, 136, 1, 9),
    _Rm10010mpAlmLineLaneTxLosfPortn_Type()
)
rm10010mpAlmLineLaneTxLosfPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmLineLaneTxLosfPortn.setStatus("current")
_Rm10010mpAlmLineLaneApdPowerSupplyPortn_Type = EkiOnOff
_Rm10010mpAlmLineLaneApdPowerSupplyPortn_Object = MibTableColumn
rm10010mpAlmLineLaneApdPowerSupplyPortn = _Rm10010mpAlmLineLaneApdPowerSupplyPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 2, 136, 1, 15),
    _Rm10010mpAlmLineLaneApdPowerSupplyPortn_Type()
)
rm10010mpAlmLineLaneApdPowerSupplyPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmLineLaneApdPowerSupplyPortn.setStatus("current")
_Rm10010mpAlmLineLaneWavelengthUnlockedPortn_Type = EkiOnOff
_Rm10010mpAlmLineLaneWavelengthUnlockedPortn_Object = MibTableColumn
rm10010mpAlmLineLaneWavelengthUnlockedPortn = _Rm10010mpAlmLineLaneWavelengthUnlockedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 2, 136, 1, 16),
    _Rm10010mpAlmLineLaneWavelengthUnlockedPortn_Type()
)
rm10010mpAlmLineLaneWavelengthUnlockedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmLineLaneWavelengthUnlockedPortn.setStatus("current")
_Rm10010mpAlmLineLaneTecFaultPortn_Type = EkiOnOff
_Rm10010mpAlmLineLaneTecFaultPortn_Object = MibTableColumn
rm10010mpAlmLineLaneTecFaultPortn = _Rm10010mpAlmLineLaneTecFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 2, 136, 1, 17),
    _Rm10010mpAlmLineLaneTecFaultPortn_Type()
)
rm10010mpAlmLineLaneTecFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmLineLaneTecFaultPortn.setStatus("current")
_Rm10010mpAlmlineHostLaneFaultTable_Object = MibTable
rm10010mpAlmlineHostLaneFaultTable = _Rm10010mpAlmlineHostLaneFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 2, 152)
)
if mibBuilder.loadTexts:
    rm10010mpAlmlineHostLaneFaultTable.setStatus("current")
_Rm10010mpAlmlineHostLaneFaultEntry_Object = MibTableRow
rm10010mpAlmlineHostLaneFaultEntry = _Rm10010mpAlmlineHostLaneFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 2, 152, 1)
)
rm10010mpAlmlineHostLaneFaultEntry.setIndexNames(
    (0, "EKINOPS-Rm10010mp-MIB", "rm10010mpAlmlineHostLaneFaultIndex"),
)
if mibBuilder.loadTexts:
    rm10010mpAlmlineHostLaneFaultEntry.setStatus("current")


class _Rm10010mpAlmlineHostLaneFaultIndex_Type(Integer32):
    """Custom type rm10010mpAlmlineHostLaneFaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010mpAlmlineHostLaneFaultIndex_Type.__name__ = "Integer32"
_Rm10010mpAlmlineHostLaneFaultIndex_Object = MibTableColumn
rm10010mpAlmlineHostLaneFaultIndex = _Rm10010mpAlmlineHostLaneFaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 2, 152, 1, 1),
    _Rm10010mpAlmlineHostLaneFaultIndex_Type()
)
rm10010mpAlmlineHostLaneFaultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmlineHostLaneFaultIndex.setStatus("current")
_Rm10010mpAlmLineInputLossOfSignalPortn_Type = EkiOnOff
_Rm10010mpAlmLineInputLossOfSignalPortn_Object = MibTableColumn
rm10010mpAlmLineInputLossOfSignalPortn = _Rm10010mpAlmLineInputLossOfSignalPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 2, 152, 1, 2),
    _Rm10010mpAlmLineInputLossOfSignalPortn_Type()
)
rm10010mpAlmLineInputLossOfSignalPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmLineInputLossOfSignalPortn.setStatus("current")
_Rm10010mpAlmLineLossOfFramePortn_Type = EkiOnOff
_Rm10010mpAlmLineLossOfFramePortn_Object = MibTableColumn
rm10010mpAlmLineLossOfFramePortn = _Rm10010mpAlmLineLossOfFramePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 2, 152, 1, 3),
    _Rm10010mpAlmLineLossOfFramePortn_Type()
)
rm10010mpAlmLineLossOfFramePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmLineLossOfFramePortn.setStatus("current")
_Rm10010mpAlmLineSmBdiInsertedPortn_Type = EkiOnOff
_Rm10010mpAlmLineSmBdiInsertedPortn_Object = MibTableColumn
rm10010mpAlmLineSmBdiInsertedPortn = _Rm10010mpAlmLineSmBdiInsertedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 2, 152, 1, 4),
    _Rm10010mpAlmLineSmBdiInsertedPortn_Type()
)
rm10010mpAlmLineSmBdiInsertedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmLineSmBdiInsertedPortn.setStatus("current")
_Rm10010mpAlmLineSmBdiDetectedPortn_Type = EkiOnOff
_Rm10010mpAlmLineSmBdiDetectedPortn_Object = MibTableColumn
rm10010mpAlmLineSmBdiDetectedPortn = _Rm10010mpAlmLineSmBdiDetectedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 2, 152, 1, 5),
    _Rm10010mpAlmLineSmBdiDetectedPortn_Type()
)
rm10010mpAlmLineSmBdiDetectedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmLineSmBdiDetectedPortn.setStatus("current")
_Rm10010mpAlmLineSmIaeInsertedPortn_Type = EkiOnOff
_Rm10010mpAlmLineSmIaeInsertedPortn_Object = MibTableColumn
rm10010mpAlmLineSmIaeInsertedPortn = _Rm10010mpAlmLineSmIaeInsertedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 2, 152, 1, 6),
    _Rm10010mpAlmLineSmIaeInsertedPortn_Type()
)
rm10010mpAlmLineSmIaeInsertedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmLineSmIaeInsertedPortn.setStatus("current")
_Rm10010mpAlmLineSmIaeDetectedPortn_Type = EkiOnOff
_Rm10010mpAlmLineSmIaeDetectedPortn_Object = MibTableColumn
rm10010mpAlmLineSmIaeDetectedPortn = _Rm10010mpAlmLineSmIaeDetectedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 2, 152, 1, 7),
    _Rm10010mpAlmLineSmIaeDetectedPortn_Type()
)
rm10010mpAlmLineSmIaeDetectedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmLineSmIaeDetectedPortn.setStatus("current")
_Rm10010mpAlmLineTxHostLolPortn_Type = EkiOnOff
_Rm10010mpAlmLineTxHostLolPortn_Object = MibTableColumn
rm10010mpAlmLineTxHostLolPortn = _Rm10010mpAlmLineTxHostLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 2, 152, 1, 10),
    _Rm10010mpAlmLineTxHostLolPortn_Type()
)
rm10010mpAlmLineTxHostLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmLineTxHostLolPortn.setStatus("current")
_Rm10010mpAlmLineLaneTxFifoErrorPortn_Type = EkiOnOff
_Rm10010mpAlmLineLaneTxFifoErrorPortn_Object = MibTableColumn
rm10010mpAlmLineLaneTxFifoErrorPortn = _Rm10010mpAlmLineLaneTxFifoErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 2, 152, 1, 11),
    _Rm10010mpAlmLineLaneTxFifoErrorPortn_Type()
)
rm10010mpAlmLineLaneTxFifoErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmLineLaneTxFifoErrorPortn.setStatus("current")
_Rm10010mpAlmlineNetworkLaneRxOtnTable_Object = MibTable
rm10010mpAlmlineNetworkLaneRxOtnTable = _Rm10010mpAlmlineNetworkLaneRxOtnTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 2, 168)
)
if mibBuilder.loadTexts:
    rm10010mpAlmlineNetworkLaneRxOtnTable.setStatus("current")
_Rm10010mpAlmlineNetworkLaneRxOtnEntry_Object = MibTableRow
rm10010mpAlmlineNetworkLaneRxOtnEntry = _Rm10010mpAlmlineNetworkLaneRxOtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 2, 168, 1)
)
rm10010mpAlmlineNetworkLaneRxOtnEntry.setIndexNames(
    (0, "EKINOPS-Rm10010mp-MIB", "rm10010mpAlmlineNetworkLaneRxOtnIndex"),
)
if mibBuilder.loadTexts:
    rm10010mpAlmlineNetworkLaneRxOtnEntry.setStatus("current")


class _Rm10010mpAlmlineNetworkLaneRxOtnIndex_Type(Integer32):
    """Custom type rm10010mpAlmlineNetworkLaneRxOtnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010mpAlmlineNetworkLaneRxOtnIndex_Type.__name__ = "Integer32"
_Rm10010mpAlmlineNetworkLaneRxOtnIndex_Object = MibTableColumn
rm10010mpAlmlineNetworkLaneRxOtnIndex = _Rm10010mpAlmlineNetworkLaneRxOtnIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 2, 168, 1, 1),
    _Rm10010mpAlmlineNetworkLaneRxOtnIndex_Type()
)
rm10010mpAlmlineNetworkLaneRxOtnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmlineNetworkLaneRxOtnIndex.setStatus("current")
_Rm10010mpAlmLineRxOtnOduAisPortn_Type = EkiOnOff
_Rm10010mpAlmLineRxOtnOduAisPortn_Object = MibTableColumn
rm10010mpAlmLineRxOtnOduAisPortn = _Rm10010mpAlmLineRxOtnOduAisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 2, 168, 1, 10),
    _Rm10010mpAlmLineRxOtnOduAisPortn_Type()
)
rm10010mpAlmLineRxOtnOduAisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmLineRxOtnOduAisPortn.setStatus("current")
_Rm10010mpAlmLineRxOtnOtuAisPortn_Type = EkiOnOff
_Rm10010mpAlmLineRxOtnOtuAisPortn_Object = MibTableColumn
rm10010mpAlmLineRxOtnOtuAisPortn = _Rm10010mpAlmLineRxOtnOtuAisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 2, 168, 1, 11),
    _Rm10010mpAlmLineRxOtnOtuAisPortn_Type()
)
rm10010mpAlmLineRxOtnOtuAisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmLineRxOtnOtuAisPortn.setStatus("current")
_Rm10010mpAlmLineRxSmBdiPortn_Type = EkiOnOff
_Rm10010mpAlmLineRxSmBdiPortn_Object = MibTableColumn
rm10010mpAlmLineRxSmBdiPortn = _Rm10010mpAlmLineRxSmBdiPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 2, 168, 1, 12),
    _Rm10010mpAlmLineRxSmBdiPortn_Type()
)
rm10010mpAlmLineRxSmBdiPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmLineRxSmBdiPortn.setStatus("current")
_Rm10010mpAlmLineRxOtnIaePortn_Type = EkiOnOff
_Rm10010mpAlmLineRxOtnIaePortn_Object = MibTableColumn
rm10010mpAlmLineRxOtnIaePortn = _Rm10010mpAlmLineRxOtnIaePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 2, 168, 1, 13),
    _Rm10010mpAlmLineRxOtnIaePortn_Type()
)
rm10010mpAlmLineRxOtnIaePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmLineRxOtnIaePortn.setStatus("current")
_Rm10010mpAlmLineRxOtnOomPortn_Type = EkiOnOff
_Rm10010mpAlmLineRxOtnOomPortn_Object = MibTableColumn
rm10010mpAlmLineRxOtnOomPortn = _Rm10010mpAlmLineRxOtnOomPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 2, 168, 1, 14),
    _Rm10010mpAlmLineRxOtnOomPortn_Type()
)
rm10010mpAlmLineRxOtnOomPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmLineRxOtnOomPortn.setStatus("current")
_Rm10010mpAlmLineRxOtnLomPortn_Type = EkiOnOff
_Rm10010mpAlmLineRxOtnLomPortn_Object = MibTableColumn
rm10010mpAlmLineRxOtnLomPortn = _Rm10010mpAlmLineRxOtnLomPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 2, 168, 1, 15),
    _Rm10010mpAlmLineRxOtnLomPortn_Type()
)
rm10010mpAlmLineRxOtnLomPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmLineRxOtnLomPortn.setStatus("current")
_Rm10010mpAlmLineRxOtnOofPortn_Type = EkiOnOff
_Rm10010mpAlmLineRxOtnOofPortn_Object = MibTableColumn
rm10010mpAlmLineRxOtnOofPortn = _Rm10010mpAlmLineRxOtnOofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 2, 168, 1, 16),
    _Rm10010mpAlmLineRxOtnOofPortn_Type()
)
rm10010mpAlmLineRxOtnOofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmLineRxOtnOofPortn.setStatus("current")
_Rm10010mpAlmLineRxOtnLofPortn_Type = EkiOnOff
_Rm10010mpAlmLineRxOtnLofPortn_Object = MibTableColumn
rm10010mpAlmLineRxOtnLofPortn = _Rm10010mpAlmLineRxOtnLofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 2, 168, 1, 17),
    _Rm10010mpAlmLineRxOtnLofPortn_Type()
)
rm10010mpAlmLineRxOtnLofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmLineRxOtnLofPortn.setStatus("current")
_Rm10010mpAlmlineHostLaneTxOtnTable_Object = MibTable
rm10010mpAlmlineHostLaneTxOtnTable = _Rm10010mpAlmlineHostLaneTxOtnTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 2, 184)
)
if mibBuilder.loadTexts:
    rm10010mpAlmlineHostLaneTxOtnTable.setStatus("current")
_Rm10010mpAlmlineHostLaneTxOtnEntry_Object = MibTableRow
rm10010mpAlmlineHostLaneTxOtnEntry = _Rm10010mpAlmlineHostLaneTxOtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 2, 184, 1)
)
rm10010mpAlmlineHostLaneTxOtnEntry.setIndexNames(
    (0, "EKINOPS-Rm10010mp-MIB", "rm10010mpAlmlineHostLaneTxOtnIndex"),
)
if mibBuilder.loadTexts:
    rm10010mpAlmlineHostLaneTxOtnEntry.setStatus("current")


class _Rm10010mpAlmlineHostLaneTxOtnIndex_Type(Integer32):
    """Custom type rm10010mpAlmlineHostLaneTxOtnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010mpAlmlineHostLaneTxOtnIndex_Type.__name__ = "Integer32"
_Rm10010mpAlmlineHostLaneTxOtnIndex_Object = MibTableColumn
rm10010mpAlmlineHostLaneTxOtnIndex = _Rm10010mpAlmlineHostLaneTxOtnIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 2, 184, 1, 1),
    _Rm10010mpAlmlineHostLaneTxOtnIndex_Type()
)
rm10010mpAlmlineHostLaneTxOtnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmlineHostLaneTxOtnIndex.setStatus("current")
_Rm10010mpAlmLineTxOtnOduAisPortn_Type = EkiOnOff
_Rm10010mpAlmLineTxOtnOduAisPortn_Object = MibTableColumn
rm10010mpAlmLineTxOtnOduAisPortn = _Rm10010mpAlmLineTxOtnOduAisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 2, 184, 1, 10),
    _Rm10010mpAlmLineTxOtnOduAisPortn_Type()
)
rm10010mpAlmLineTxOtnOduAisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmLineTxOtnOduAisPortn.setStatus("current")
_Rm10010mpAlmLineTxOtnOtuAisPortn_Type = EkiOnOff
_Rm10010mpAlmLineTxOtnOtuAisPortn_Object = MibTableColumn
rm10010mpAlmLineTxOtnOtuAisPortn = _Rm10010mpAlmLineTxOtnOtuAisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 2, 184, 1, 11),
    _Rm10010mpAlmLineTxOtnOtuAisPortn_Type()
)
rm10010mpAlmLineTxOtnOtuAisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmLineTxOtnOtuAisPortn.setStatus("current")
_Rm10010mpAlmLineTxSmBdiPortn_Type = EkiOnOff
_Rm10010mpAlmLineTxSmBdiPortn_Object = MibTableColumn
rm10010mpAlmLineTxSmBdiPortn = _Rm10010mpAlmLineTxSmBdiPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 2, 184, 1, 12),
    _Rm10010mpAlmLineTxSmBdiPortn_Type()
)
rm10010mpAlmLineTxSmBdiPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmLineTxSmBdiPortn.setStatus("current")
_Rm10010mpAlmLineTxOtnIaePortn_Type = EkiOnOff
_Rm10010mpAlmLineTxOtnIaePortn_Object = MibTableColumn
rm10010mpAlmLineTxOtnIaePortn = _Rm10010mpAlmLineTxOtnIaePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 2, 184, 1, 13),
    _Rm10010mpAlmLineTxOtnIaePortn_Type()
)
rm10010mpAlmLineTxOtnIaePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmLineTxOtnIaePortn.setStatus("current")
_Rm10010mpAlmLineTxOtnOomPortn_Type = EkiOnOff
_Rm10010mpAlmLineTxOtnOomPortn_Object = MibTableColumn
rm10010mpAlmLineTxOtnOomPortn = _Rm10010mpAlmLineTxOtnOomPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 2, 184, 1, 14),
    _Rm10010mpAlmLineTxOtnOomPortn_Type()
)
rm10010mpAlmLineTxOtnOomPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmLineTxOtnOomPortn.setStatus("current")
_Rm10010mpAlmLineTxOtnLomPortn_Type = EkiOnOff
_Rm10010mpAlmLineTxOtnLomPortn_Object = MibTableColumn
rm10010mpAlmLineTxOtnLomPortn = _Rm10010mpAlmLineTxOtnLomPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 2, 184, 1, 15),
    _Rm10010mpAlmLineTxOtnLomPortn_Type()
)
rm10010mpAlmLineTxOtnLomPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmLineTxOtnLomPortn.setStatus("current")
_Rm10010mpAlmLineTxOtnOofPortn_Type = EkiOnOff
_Rm10010mpAlmLineTxOtnOofPortn_Object = MibTableColumn
rm10010mpAlmLineTxOtnOofPortn = _Rm10010mpAlmLineTxOtnOofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 2, 184, 1, 16),
    _Rm10010mpAlmLineTxOtnOofPortn_Type()
)
rm10010mpAlmLineTxOtnOofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmLineTxOtnOofPortn.setStatus("current")
_Rm10010mpAlmLineTxOtnLofPortn_Type = EkiOnOff
_Rm10010mpAlmLineTxOtnLofPortn_Object = MibTableColumn
rm10010mpAlmLineTxOtnLofPortn = _Rm10010mpAlmLineTxOtnLofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 2, 184, 1, 17),
    _Rm10010mpAlmLineTxOtnLofPortn_Type()
)
rm10010mpAlmLineTxOtnLofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmLineTxOtnLofPortn.setStatus("current")
_Rm10010mpAlmLineCrit_ObjectIdentity = ObjectIdentity
rm10010mpAlmLineCrit = _Rm10010mpAlmLineCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 3)
)
_Rm10010mpAlmsynthAlmLineTable_Object = MibTable
rm10010mpAlmsynthAlmLineTable = _Rm10010mpAlmsynthAlmLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 3, 24)
)
if mibBuilder.loadTexts:
    rm10010mpAlmsynthAlmLineTable.setStatus("current")
_Rm10010mpAlmsynthAlmLineEntry_Object = MibTableRow
rm10010mpAlmsynthAlmLineEntry = _Rm10010mpAlmsynthAlmLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 3, 24, 1)
)
rm10010mpAlmsynthAlmLineEntry.setIndexNames(
    (0, "EKINOPS-Rm10010mp-MIB", "rm10010mpAlmsynthAlmLineIndex"),
)
if mibBuilder.loadTexts:
    rm10010mpAlmsynthAlmLineEntry.setStatus("current")


class _Rm10010mpAlmsynthAlmLineIndex_Type(Integer32):
    """Custom type rm10010mpAlmsynthAlmLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010mpAlmsynthAlmLineIndex_Type.__name__ = "Integer32"
_Rm10010mpAlmsynthAlmLineIndex_Object = MibTableColumn
rm10010mpAlmsynthAlmLineIndex = _Rm10010mpAlmsynthAlmLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 3, 24, 1, 1),
    _Rm10010mpAlmsynthAlmLineIndex_Type()
)
rm10010mpAlmsynthAlmLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmsynthAlmLineIndex.setStatus("current")
_Rm10010mpAlmXfpAbsentPortn_Type = EkiOnOff
_Rm10010mpAlmXfpAbsentPortn_Object = MibTableColumn
rm10010mpAlmXfpAbsentPortn = _Rm10010mpAlmXfpAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 3, 24, 1, 2),
    _Rm10010mpAlmXfpAbsentPortn_Type()
)
rm10010mpAlmXfpAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmXfpAbsentPortn.setStatus("current")
_Rm10010mpAlmXfpInitNotComplPortn_Type = EkiOnOff
_Rm10010mpAlmXfpInitNotComplPortn_Object = MibTableColumn
rm10010mpAlmXfpInitNotComplPortn = _Rm10010mpAlmXfpInitNotComplPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 3, 24, 1, 3),
    _Rm10010mpAlmXfpInitNotComplPortn_Type()
)
rm10010mpAlmXfpInitNotComplPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmXfpInitNotComplPortn.setStatus("current")
_Rm10010mpAlmLineHwFailPortn_Type = EkiOnOff
_Rm10010mpAlmLineHwFailPortn_Object = MibTableColumn
rm10010mpAlmLineHwFailPortn = _Rm10010mpAlmLineHwFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 3, 24, 1, 5),
    _Rm10010mpAlmLineHwFailPortn_Type()
)
rm10010mpAlmLineHwFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmLineHwFailPortn.setStatus("current")
_Rm10010mpAlmXfpTxOffPortn_Type = EkiOnOff
_Rm10010mpAlmXfpTxOffPortn_Object = MibTableColumn
rm10010mpAlmXfpTxOffPortn = _Rm10010mpAlmXfpTxOffPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 3, 24, 1, 6),
    _Rm10010mpAlmXfpTxOffPortn_Type()
)
rm10010mpAlmXfpTxOffPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmXfpTxOffPortn.setStatus("current")
_Rm10010mpAlmLineLocalOosPortn_Type = EkiOnOff
_Rm10010mpAlmLineLocalOosPortn_Object = MibTableColumn
rm10010mpAlmLineLocalOosPortn = _Rm10010mpAlmLineLocalOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 3, 24, 1, 7),
    _Rm10010mpAlmLineLocalOosPortn_Type()
)
rm10010mpAlmLineLocalOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmLineLocalOosPortn.setStatus("current")
_Rm10010mpAlmUpRdiInsPortn_Type = EkiOnOff
_Rm10010mpAlmUpRdiInsPortn_Object = MibTableColumn
rm10010mpAlmUpRdiInsPortn = _Rm10010mpAlmUpRdiInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 3, 24, 1, 9),
    _Rm10010mpAlmUpRdiInsPortn_Type()
)
rm10010mpAlmUpRdiInsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmUpRdiInsPortn.setStatus("current")
_Rm10010mpAlmLineDdmWarningPortn_Type = EkiOnOff
_Rm10010mpAlmLineDdmWarningPortn_Object = MibTableColumn
rm10010mpAlmLineDdmWarningPortn = _Rm10010mpAlmLineDdmWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 3, 24, 1, 10),
    _Rm10010mpAlmLineDdmWarningPortn_Type()
)
rm10010mpAlmLineDdmWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmLineDdmWarningPortn.setStatus("current")
_Rm10010mpAlmLineDdmAlmPortn_Type = EkiOnOff
_Rm10010mpAlmLineDdmAlmPortn_Object = MibTableColumn
rm10010mpAlmLineDdmAlmPortn = _Rm10010mpAlmLineDdmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 3, 24, 1, 11),
    _Rm10010mpAlmLineDdmAlmPortn_Type()
)
rm10010mpAlmLineDdmAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmLineDdmAlmPortn.setStatus("current")
_Rm10010mpAlmLineFailPortn_Type = EkiOnOff
_Rm10010mpAlmLineFailPortn_Object = MibTableColumn
rm10010mpAlmLineFailPortn = _Rm10010mpAlmLineFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 3, 24, 1, 13),
    _Rm10010mpAlmLineFailPortn_Type()
)
rm10010mpAlmLineFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmLineFailPortn.setStatus("current")
_Rm10010mpAlmLineActivePortn_Type = EkiOnOff
_Rm10010mpAlmLineActivePortn_Object = MibTableColumn
rm10010mpAlmLineActivePortn = _Rm10010mpAlmLineActivePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 2, 3, 3, 24, 1, 17),
    _Rm10010mpAlmLineActivePortn_Type()
)
rm10010mpAlmLineActivePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpAlmLineActivePortn.setStatus("current")
_Rm10010mpmeasures_ObjectIdentity = ObjectIdentity
rm10010mpmeasures = _Rm10010mpmeasures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3)
)
_Rm10010mpMesrOther_ObjectIdentity = ObjectIdentity
rm10010mpMesrOther = _Rm10010mpMesrOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 1)
)
_Rm10010mpMesrsynth0_Type = EkiMeasureType
_Rm10010mpMesrsynth0_Object = MibScalar
rm10010mpMesrsynth0 = _Rm10010mpMesrsynth0_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 1, 0),
    _Rm10010mpMesrsynth0_Type()
)
rm10010mpMesrsynth0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrsynth0.setStatus("deprecated")
_Rm10010mpMesrsynth1_Type = EkiMeasureType
_Rm10010mpMesrsynth1_Object = MibScalar
rm10010mpMesrsynth1 = _Rm10010mpMesrsynth1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 1, 1),
    _Rm10010mpMesrsynth1_Type()
)
rm10010mpMesrsynth1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrsynth1.setStatus("deprecated")


class _Rm10010mpMesrpmIntervalNumber_Type(Unsigned32):
    """Custom type rm10010mpMesrpmIntervalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010mpMesrpmIntervalNumber_Type.__name__ = "Unsigned32"
_Rm10010mpMesrpmIntervalNumber_Object = MibScalar
rm10010mpMesrpmIntervalNumber = _Rm10010mpMesrpmIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 1, 7),
    _Rm10010mpMesrpmIntervalNumber_Type()
)
rm10010mpMesrpmIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrpmIntervalNumber.setStatus("current")


class _Rm10010mpMesrlineNetTxLaserOutputPwrAverage_Type(Unsigned32):
    """Custom type rm10010mpMesrlineNetTxLaserOutputPwrAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010mpMesrlineNetTxLaserOutputPwrAverage_Type.__name__ = "Unsigned32"
_Rm10010mpMesrlineNetTxLaserOutputPwrAverage_Object = MibScalar
rm10010mpMesrlineNetTxLaserOutputPwrAverage = _Rm10010mpMesrlineNetTxLaserOutputPwrAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 1, 180),
    _Rm10010mpMesrlineNetTxLaserOutputPwrAverage_Type()
)
rm10010mpMesrlineNetTxLaserOutputPwrAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrlineNetTxLaserOutputPwrAverage.setStatus("current")


class _Rm10010mpMesrlineNetTxLaserTempAverage_Type(Unsigned32):
    """Custom type rm10010mpMesrlineNetTxLaserTempAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010mpMesrlineNetTxLaserTempAverage_Type.__name__ = "Unsigned32"
_Rm10010mpMesrlineNetTxLaserTempAverage_Object = MibScalar
rm10010mpMesrlineNetTxLaserTempAverage = _Rm10010mpMesrlineNetTxLaserTempAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 1, 181),
    _Rm10010mpMesrlineNetTxLaserTempAverage_Type()
)
rm10010mpMesrlineNetTxLaserTempAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrlineNetTxLaserTempAverage.setStatus("current")


class _Rm10010mpMesrlineNetTxBiasCurrentAverage_Type(Unsigned32):
    """Custom type rm10010mpMesrlineNetTxBiasCurrentAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010mpMesrlineNetTxBiasCurrentAverage_Type.__name__ = "Unsigned32"
_Rm10010mpMesrlineNetTxBiasCurrentAverage_Object = MibScalar
rm10010mpMesrlineNetTxBiasCurrentAverage = _Rm10010mpMesrlineNetTxBiasCurrentAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 1, 182),
    _Rm10010mpMesrlineNetTxBiasCurrentAverage_Type()
)
rm10010mpMesrlineNetTxBiasCurrentAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrlineNetTxBiasCurrentAverage.setStatus("current")


class _Rm10010mpMesrlineNetRxInputPwrAverage_Type(Unsigned32):
    """Custom type rm10010mpMesrlineNetRxInputPwrAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010mpMesrlineNetRxInputPwrAverage_Type.__name__ = "Unsigned32"
_Rm10010mpMesrlineNetRxInputPwrAverage_Object = MibScalar
rm10010mpMesrlineNetRxInputPwrAverage = _Rm10010mpMesrlineNetRxInputPwrAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 1, 183),
    _Rm10010mpMesrlineNetRxInputPwrAverage_Type()
)
rm10010mpMesrlineNetRxInputPwrAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrlineNetRxInputPwrAverage.setStatus("current")


class _Rm10010mpMesrlineResidualChromaticDispAverage_Type(Unsigned32):
    """Custom type rm10010mpMesrlineResidualChromaticDispAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010mpMesrlineResidualChromaticDispAverage_Type.__name__ = "Unsigned32"
_Rm10010mpMesrlineResidualChromaticDispAverage_Object = MibScalar
rm10010mpMesrlineResidualChromaticDispAverage = _Rm10010mpMesrlineResidualChromaticDispAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 1, 184),
    _Rm10010mpMesrlineResidualChromaticDispAverage_Type()
)
rm10010mpMesrlineResidualChromaticDispAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrlineResidualChromaticDispAverage.setStatus("current")


class _Rm10010mpMesrlineDiffGroupDelayAverage_Type(Unsigned32):
    """Custom type rm10010mpMesrlineDiffGroupDelayAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010mpMesrlineDiffGroupDelayAverage_Type.__name__ = "Unsigned32"
_Rm10010mpMesrlineDiffGroupDelayAverage_Object = MibScalar
rm10010mpMesrlineDiffGroupDelayAverage = _Rm10010mpMesrlineDiffGroupDelayAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 1, 185),
    _Rm10010mpMesrlineDiffGroupDelayAverage_Type()
)
rm10010mpMesrlineDiffGroupDelayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrlineDiffGroupDelayAverage.setStatus("current")


class _Rm10010mpMesrlineQFactorAverage_Type(Unsigned32):
    """Custom type rm10010mpMesrlineQFactorAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010mpMesrlineQFactorAverage_Type.__name__ = "Unsigned32"
_Rm10010mpMesrlineQFactorAverage_Object = MibScalar
rm10010mpMesrlineQFactorAverage = _Rm10010mpMesrlineQFactorAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 1, 186),
    _Rm10010mpMesrlineQFactorAverage_Type()
)
rm10010mpMesrlineQFactorAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrlineQFactorAverage.setStatus("current")


class _Rm10010mpMesrlineCarrierFreqOffsetAverage_Type(Unsigned32):
    """Custom type rm10010mpMesrlineCarrierFreqOffsetAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010mpMesrlineCarrierFreqOffsetAverage_Type.__name__ = "Unsigned32"
_Rm10010mpMesrlineCarrierFreqOffsetAverage_Object = MibScalar
rm10010mpMesrlineCarrierFreqOffsetAverage = _Rm10010mpMesrlineCarrierFreqOffsetAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 1, 187),
    _Rm10010mpMesrlineCarrierFreqOffsetAverage_Type()
)
rm10010mpMesrlineCarrierFreqOffsetAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrlineCarrierFreqOffsetAverage.setStatus("current")


class _Rm10010mpMesrlineOsnrAverage_Type(Unsigned32):
    """Custom type rm10010mpMesrlineOsnrAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010mpMesrlineOsnrAverage_Type.__name__ = "Unsigned32"
_Rm10010mpMesrlineOsnrAverage_Object = MibScalar
rm10010mpMesrlineOsnrAverage = _Rm10010mpMesrlineOsnrAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 1, 188),
    _Rm10010mpMesrlineOsnrAverage_Type()
)
rm10010mpMesrlineOsnrAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrlineOsnrAverage.setStatus("current")


class _Rm10010mpMesrclientNetTxTempMin_Type(Unsigned32):
    """Custom type rm10010mpMesrclientNetTxTempMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010mpMesrclientNetTxTempMin_Type.__name__ = "Unsigned32"
_Rm10010mpMesrclientNetTxTempMin_Object = MibScalar
rm10010mpMesrclientNetTxTempMin = _Rm10010mpMesrclientNetTxTempMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 1, 192),
    _Rm10010mpMesrclientNetTxTempMin_Type()
)
rm10010mpMesrclientNetTxTempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrclientNetTxTempMin.setStatus("current")


class _Rm10010mpMesrclientNetTxBiasMin_Type(Unsigned32):
    """Custom type rm10010mpMesrclientNetTxBiasMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010mpMesrclientNetTxBiasMin_Type.__name__ = "Unsigned32"
_Rm10010mpMesrclientNetTxBiasMin_Object = MibScalar
rm10010mpMesrclientNetTxBiasMin = _Rm10010mpMesrclientNetTxBiasMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 1, 193),
    _Rm10010mpMesrclientNetTxBiasMin_Type()
)
rm10010mpMesrclientNetTxBiasMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrclientNetTxBiasMin.setStatus("current")


class _Rm10010mpMesrclientNetTxPwrMin_Type(Unsigned32):
    """Custom type rm10010mpMesrclientNetTxPwrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010mpMesrclientNetTxPwrMin_Type.__name__ = "Unsigned32"
_Rm10010mpMesrclientNetTxPwrMin_Object = MibScalar
rm10010mpMesrclientNetTxPwrMin = _Rm10010mpMesrclientNetTxPwrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 1, 194),
    _Rm10010mpMesrclientNetTxPwrMin_Type()
)
rm10010mpMesrclientNetTxPwrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrclientNetTxPwrMin.setStatus("current")


class _Rm10010mpMesrclientNetRxPwrMin_Type(Unsigned32):
    """Custom type rm10010mpMesrclientNetRxPwrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010mpMesrclientNetRxPwrMin_Type.__name__ = "Unsigned32"
_Rm10010mpMesrclientNetRxPwrMin_Object = MibScalar
rm10010mpMesrclientNetRxPwrMin = _Rm10010mpMesrclientNetRxPwrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 1, 195),
    _Rm10010mpMesrclientNetRxPwrMin_Type()
)
rm10010mpMesrclientNetRxPwrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrclientNetRxPwrMin.setStatus("current")


class _Rm10010mpMesrlineNetTxLaserOutputPwrMin_Type(Unsigned32):
    """Custom type rm10010mpMesrlineNetTxLaserOutputPwrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010mpMesrlineNetTxLaserOutputPwrMin_Type.__name__ = "Unsigned32"
_Rm10010mpMesrlineNetTxLaserOutputPwrMin_Object = MibScalar
rm10010mpMesrlineNetTxLaserOutputPwrMin = _Rm10010mpMesrlineNetTxLaserOutputPwrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 1, 196),
    _Rm10010mpMesrlineNetTxLaserOutputPwrMin_Type()
)
rm10010mpMesrlineNetTxLaserOutputPwrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrlineNetTxLaserOutputPwrMin.setStatus("current")


class _Rm10010mpMesrlineNetTxLaserTempMin_Type(Unsigned32):
    """Custom type rm10010mpMesrlineNetTxLaserTempMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010mpMesrlineNetTxLaserTempMin_Type.__name__ = "Unsigned32"
_Rm10010mpMesrlineNetTxLaserTempMin_Object = MibScalar
rm10010mpMesrlineNetTxLaserTempMin = _Rm10010mpMesrlineNetTxLaserTempMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 1, 197),
    _Rm10010mpMesrlineNetTxLaserTempMin_Type()
)
rm10010mpMesrlineNetTxLaserTempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrlineNetTxLaserTempMin.setStatus("current")


class _Rm10010mpMesrlineNetTxBiasCurrentMin_Type(Unsigned32):
    """Custom type rm10010mpMesrlineNetTxBiasCurrentMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010mpMesrlineNetTxBiasCurrentMin_Type.__name__ = "Unsigned32"
_Rm10010mpMesrlineNetTxBiasCurrentMin_Object = MibScalar
rm10010mpMesrlineNetTxBiasCurrentMin = _Rm10010mpMesrlineNetTxBiasCurrentMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 1, 198),
    _Rm10010mpMesrlineNetTxBiasCurrentMin_Type()
)
rm10010mpMesrlineNetTxBiasCurrentMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrlineNetTxBiasCurrentMin.setStatus("current")


class _Rm10010mpMesrlineNetRxInputPwrMin_Type(Unsigned32):
    """Custom type rm10010mpMesrlineNetRxInputPwrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010mpMesrlineNetRxInputPwrMin_Type.__name__ = "Unsigned32"
_Rm10010mpMesrlineNetRxInputPwrMin_Object = MibScalar
rm10010mpMesrlineNetRxInputPwrMin = _Rm10010mpMesrlineNetRxInputPwrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 1, 199),
    _Rm10010mpMesrlineNetRxInputPwrMin_Type()
)
rm10010mpMesrlineNetRxInputPwrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrlineNetRxInputPwrMin.setStatus("current")


class _Rm10010mpMesrlineResidualChromaticDispMin_Type(Unsigned32):
    """Custom type rm10010mpMesrlineResidualChromaticDispMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010mpMesrlineResidualChromaticDispMin_Type.__name__ = "Unsigned32"
_Rm10010mpMesrlineResidualChromaticDispMin_Object = MibScalar
rm10010mpMesrlineResidualChromaticDispMin = _Rm10010mpMesrlineResidualChromaticDispMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 1, 200),
    _Rm10010mpMesrlineResidualChromaticDispMin_Type()
)
rm10010mpMesrlineResidualChromaticDispMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrlineResidualChromaticDispMin.setStatus("current")


class _Rm10010mpMesrlineDiffGroupDelayMin_Type(Unsigned32):
    """Custom type rm10010mpMesrlineDiffGroupDelayMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010mpMesrlineDiffGroupDelayMin_Type.__name__ = "Unsigned32"
_Rm10010mpMesrlineDiffGroupDelayMin_Object = MibScalar
rm10010mpMesrlineDiffGroupDelayMin = _Rm10010mpMesrlineDiffGroupDelayMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 1, 201),
    _Rm10010mpMesrlineDiffGroupDelayMin_Type()
)
rm10010mpMesrlineDiffGroupDelayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrlineDiffGroupDelayMin.setStatus("current")


class _Rm10010mpMesrlineQFactorMin_Type(Unsigned32):
    """Custom type rm10010mpMesrlineQFactorMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010mpMesrlineQFactorMin_Type.__name__ = "Unsigned32"
_Rm10010mpMesrlineQFactorMin_Object = MibScalar
rm10010mpMesrlineQFactorMin = _Rm10010mpMesrlineQFactorMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 1, 202),
    _Rm10010mpMesrlineQFactorMin_Type()
)
rm10010mpMesrlineQFactorMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrlineQFactorMin.setStatus("current")


class _Rm10010mpMesrlineCarrierFreqOffsetMin_Type(Unsigned32):
    """Custom type rm10010mpMesrlineCarrierFreqOffsetMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010mpMesrlineCarrierFreqOffsetMin_Type.__name__ = "Unsigned32"
_Rm10010mpMesrlineCarrierFreqOffsetMin_Object = MibScalar
rm10010mpMesrlineCarrierFreqOffsetMin = _Rm10010mpMesrlineCarrierFreqOffsetMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 1, 203),
    _Rm10010mpMesrlineCarrierFreqOffsetMin_Type()
)
rm10010mpMesrlineCarrierFreqOffsetMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrlineCarrierFreqOffsetMin.setStatus("current")


class _Rm10010mpMesrlineOsnrMin_Type(Unsigned32):
    """Custom type rm10010mpMesrlineOsnrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010mpMesrlineOsnrMin_Type.__name__ = "Unsigned32"
_Rm10010mpMesrlineOsnrMin_Object = MibScalar
rm10010mpMesrlineOsnrMin = _Rm10010mpMesrlineOsnrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 1, 204),
    _Rm10010mpMesrlineOsnrMin_Type()
)
rm10010mpMesrlineOsnrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrlineOsnrMin.setStatus("current")


class _Rm10010mpMesrclientNetTxTempMax_Type(Unsigned32):
    """Custom type rm10010mpMesrclientNetTxTempMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010mpMesrclientNetTxTempMax_Type.__name__ = "Unsigned32"
_Rm10010mpMesrclientNetTxTempMax_Object = MibScalar
rm10010mpMesrclientNetTxTempMax = _Rm10010mpMesrclientNetTxTempMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 1, 208),
    _Rm10010mpMesrclientNetTxTempMax_Type()
)
rm10010mpMesrclientNetTxTempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrclientNetTxTempMax.setStatus("current")


class _Rm10010mpMesrclientNetTxBiasMax_Type(Unsigned32):
    """Custom type rm10010mpMesrclientNetTxBiasMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010mpMesrclientNetTxBiasMax_Type.__name__ = "Unsigned32"
_Rm10010mpMesrclientNetTxBiasMax_Object = MibScalar
rm10010mpMesrclientNetTxBiasMax = _Rm10010mpMesrclientNetTxBiasMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 1, 209),
    _Rm10010mpMesrclientNetTxBiasMax_Type()
)
rm10010mpMesrclientNetTxBiasMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrclientNetTxBiasMax.setStatus("current")


class _Rm10010mpMesrclientNetTxPwrMax_Type(Unsigned32):
    """Custom type rm10010mpMesrclientNetTxPwrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010mpMesrclientNetTxPwrMax_Type.__name__ = "Unsigned32"
_Rm10010mpMesrclientNetTxPwrMax_Object = MibScalar
rm10010mpMesrclientNetTxPwrMax = _Rm10010mpMesrclientNetTxPwrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 1, 210),
    _Rm10010mpMesrclientNetTxPwrMax_Type()
)
rm10010mpMesrclientNetTxPwrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrclientNetTxPwrMax.setStatus("current")


class _Rm10010mpMesrclientNetRxPwrMax_Type(Unsigned32):
    """Custom type rm10010mpMesrclientNetRxPwrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010mpMesrclientNetRxPwrMax_Type.__name__ = "Unsigned32"
_Rm10010mpMesrclientNetRxPwrMax_Object = MibScalar
rm10010mpMesrclientNetRxPwrMax = _Rm10010mpMesrclientNetRxPwrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 1, 211),
    _Rm10010mpMesrclientNetRxPwrMax_Type()
)
rm10010mpMesrclientNetRxPwrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrclientNetRxPwrMax.setStatus("current")


class _Rm10010mpMesrlineNetTxLaserOutputPwrMax_Type(Unsigned32):
    """Custom type rm10010mpMesrlineNetTxLaserOutputPwrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010mpMesrlineNetTxLaserOutputPwrMax_Type.__name__ = "Unsigned32"
_Rm10010mpMesrlineNetTxLaserOutputPwrMax_Object = MibScalar
rm10010mpMesrlineNetTxLaserOutputPwrMax = _Rm10010mpMesrlineNetTxLaserOutputPwrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 1, 212),
    _Rm10010mpMesrlineNetTxLaserOutputPwrMax_Type()
)
rm10010mpMesrlineNetTxLaserOutputPwrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrlineNetTxLaserOutputPwrMax.setStatus("current")


class _Rm10010mpMesrlineNetTxLaserTempMax_Type(Unsigned32):
    """Custom type rm10010mpMesrlineNetTxLaserTempMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010mpMesrlineNetTxLaserTempMax_Type.__name__ = "Unsigned32"
_Rm10010mpMesrlineNetTxLaserTempMax_Object = MibScalar
rm10010mpMesrlineNetTxLaserTempMax = _Rm10010mpMesrlineNetTxLaserTempMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 1, 213),
    _Rm10010mpMesrlineNetTxLaserTempMax_Type()
)
rm10010mpMesrlineNetTxLaserTempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrlineNetTxLaserTempMax.setStatus("current")


class _Rm10010mpMesrlineNetTxBiasCurrentMax_Type(Unsigned32):
    """Custom type rm10010mpMesrlineNetTxBiasCurrentMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010mpMesrlineNetTxBiasCurrentMax_Type.__name__ = "Unsigned32"
_Rm10010mpMesrlineNetTxBiasCurrentMax_Object = MibScalar
rm10010mpMesrlineNetTxBiasCurrentMax = _Rm10010mpMesrlineNetTxBiasCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 1, 214),
    _Rm10010mpMesrlineNetTxBiasCurrentMax_Type()
)
rm10010mpMesrlineNetTxBiasCurrentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrlineNetTxBiasCurrentMax.setStatus("current")


class _Rm10010mpMesrlineNetRxInputPwrMax_Type(Unsigned32):
    """Custom type rm10010mpMesrlineNetRxInputPwrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010mpMesrlineNetRxInputPwrMax_Type.__name__ = "Unsigned32"
_Rm10010mpMesrlineNetRxInputPwrMax_Object = MibScalar
rm10010mpMesrlineNetRxInputPwrMax = _Rm10010mpMesrlineNetRxInputPwrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 1, 215),
    _Rm10010mpMesrlineNetRxInputPwrMax_Type()
)
rm10010mpMesrlineNetRxInputPwrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrlineNetRxInputPwrMax.setStatus("current")


class _Rm10010mpMesrlineResidualChromaticDispMax_Type(Unsigned32):
    """Custom type rm10010mpMesrlineResidualChromaticDispMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010mpMesrlineResidualChromaticDispMax_Type.__name__ = "Unsigned32"
_Rm10010mpMesrlineResidualChromaticDispMax_Object = MibScalar
rm10010mpMesrlineResidualChromaticDispMax = _Rm10010mpMesrlineResidualChromaticDispMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 1, 216),
    _Rm10010mpMesrlineResidualChromaticDispMax_Type()
)
rm10010mpMesrlineResidualChromaticDispMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrlineResidualChromaticDispMax.setStatus("current")


class _Rm10010mpMesrlineDiffGroupDelayMax_Type(Unsigned32):
    """Custom type rm10010mpMesrlineDiffGroupDelayMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010mpMesrlineDiffGroupDelayMax_Type.__name__ = "Unsigned32"
_Rm10010mpMesrlineDiffGroupDelayMax_Object = MibScalar
rm10010mpMesrlineDiffGroupDelayMax = _Rm10010mpMesrlineDiffGroupDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 1, 217),
    _Rm10010mpMesrlineDiffGroupDelayMax_Type()
)
rm10010mpMesrlineDiffGroupDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrlineDiffGroupDelayMax.setStatus("current")


class _Rm10010mpMesrlineQFactorMax_Type(Unsigned32):
    """Custom type rm10010mpMesrlineQFactorMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010mpMesrlineQFactorMax_Type.__name__ = "Unsigned32"
_Rm10010mpMesrlineQFactorMax_Object = MibScalar
rm10010mpMesrlineQFactorMax = _Rm10010mpMesrlineQFactorMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 1, 218),
    _Rm10010mpMesrlineQFactorMax_Type()
)
rm10010mpMesrlineQFactorMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrlineQFactorMax.setStatus("current")


class _Rm10010mpMesrlineCarrierFreqOffsetMax_Type(Unsigned32):
    """Custom type rm10010mpMesrlineCarrierFreqOffsetMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010mpMesrlineCarrierFreqOffsetMax_Type.__name__ = "Unsigned32"
_Rm10010mpMesrlineCarrierFreqOffsetMax_Object = MibScalar
rm10010mpMesrlineCarrierFreqOffsetMax = _Rm10010mpMesrlineCarrierFreqOffsetMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 1, 219),
    _Rm10010mpMesrlineCarrierFreqOffsetMax_Type()
)
rm10010mpMesrlineCarrierFreqOffsetMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrlineCarrierFreqOffsetMax.setStatus("current")


class _Rm10010mpMesrlineOsnrMax_Type(Unsigned32):
    """Custom type rm10010mpMesrlineOsnrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010mpMesrlineOsnrMax_Type.__name__ = "Unsigned32"
_Rm10010mpMesrlineOsnrMax_Object = MibScalar
rm10010mpMesrlineOsnrMax = _Rm10010mpMesrlineOsnrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 1, 220),
    _Rm10010mpMesrlineOsnrMax_Type()
)
rm10010mpMesrlineOsnrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrlineOsnrMax.setStatus("current")
_Rm10010mpMesrClient_ObjectIdentity = ObjectIdentity
rm10010mpMesrClient = _Rm10010mpMesrClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 2)
)


class _Rm10010mpMesrclientCfpTemp_Type(Unsigned32):
    """Custom type rm10010mpMesrclientCfpTemp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010mpMesrclientCfpTemp_Type.__name__ = "Unsigned32"
_Rm10010mpMesrclientCfpTemp_Object = MibScalar
rm10010mpMesrclientCfpTemp = _Rm10010mpMesrclientCfpTemp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 2, 8),
    _Rm10010mpMesrclientCfpTemp_Type()
)
rm10010mpMesrclientCfpTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrclientCfpTemp.setStatus("current")


class _Rm10010mpMesrclientCfp3v3Voltage_Type(Unsigned32):
    """Custom type rm10010mpMesrclientCfp3v3Voltage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010mpMesrclientCfp3v3Voltage_Type.__name__ = "Unsigned32"
_Rm10010mpMesrclientCfp3v3Voltage_Object = MibScalar
rm10010mpMesrclientCfp3v3Voltage = _Rm10010mpMesrclientCfp3v3Voltage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 2, 9),
    _Rm10010mpMesrclientCfp3v3Voltage_Type()
)
rm10010mpMesrclientCfp3v3Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrclientCfp3v3Voltage.setStatus("current")


class _Rm10010mpMesrclientSoaBiasCurrent_Type(Unsigned32):
    """Custom type rm10010mpMesrclientSoaBiasCurrent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010mpMesrclientSoaBiasCurrent_Type.__name__ = "Unsigned32"
_Rm10010mpMesrclientSoaBiasCurrent_Object = MibScalar
rm10010mpMesrclientSoaBiasCurrent = _Rm10010mpMesrclientSoaBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 2, 10),
    _Rm10010mpMesrclientSoaBiasCurrent_Type()
)
rm10010mpMesrclientSoaBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrclientSoaBiasCurrent.setStatus("current")
_Rm10010mpMesrclientNetTxTempTable_Object = MibTable
rm10010mpMesrclientNetTxTempTable = _Rm10010mpMesrclientNetTxTempTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 2, 16)
)
if mibBuilder.loadTexts:
    rm10010mpMesrclientNetTxTempTable.setStatus("current")
_Rm10010mpMesrclientNetTxTempEntry_Object = MibTableRow
rm10010mpMesrclientNetTxTempEntry = _Rm10010mpMesrclientNetTxTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 2, 16, 1)
)
rm10010mpMesrclientNetTxTempEntry.setIndexNames(
    (0, "EKINOPS-Rm10010mp-MIB", "rm10010mpMesrclientNetTxTempIndex"),
)
if mibBuilder.loadTexts:
    rm10010mpMesrclientNetTxTempEntry.setStatus("current")


class _Rm10010mpMesrclientNetTxTempIndex_Type(Integer32):
    """Custom type rm10010mpMesrclientNetTxTempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010mpMesrclientNetTxTempIndex_Type.__name__ = "Integer32"
_Rm10010mpMesrclientNetTxTempIndex_Object = MibTableColumn
rm10010mpMesrclientNetTxTempIndex = _Rm10010mpMesrclientNetTxTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 2, 16, 1, 1),
    _Rm10010mpMesrclientNetTxTempIndex_Type()
)
rm10010mpMesrclientNetTxTempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrclientNetTxTempIndex.setStatus("current")


class _Rm10010mpMesrclientNetTxTempPortn_Type(Integer32):
    """Custom type rm10010mpMesrclientNetTxTempPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010mpMesrclientNetTxTempPortn_Type.__name__ = "Integer32"
_Rm10010mpMesrclientNetTxTempPortn_Object = MibTableColumn
rm10010mpMesrclientNetTxTempPortn = _Rm10010mpMesrclientNetTxTempPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 2, 16, 1, 2),
    _Rm10010mpMesrclientNetTxTempPortn_Type()
)
rm10010mpMesrclientNetTxTempPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrclientNetTxTempPortn.setStatus("current")
_Rm10010mpMesrclientNetTxBiasTable_Object = MibTable
rm10010mpMesrclientNetTxBiasTable = _Rm10010mpMesrclientNetTxBiasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 2, 32)
)
if mibBuilder.loadTexts:
    rm10010mpMesrclientNetTxBiasTable.setStatus("current")
_Rm10010mpMesrclientNetTxBiasEntry_Object = MibTableRow
rm10010mpMesrclientNetTxBiasEntry = _Rm10010mpMesrclientNetTxBiasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 2, 32, 1)
)
rm10010mpMesrclientNetTxBiasEntry.setIndexNames(
    (0, "EKINOPS-Rm10010mp-MIB", "rm10010mpMesrclientNetTxBiasIndex"),
)
if mibBuilder.loadTexts:
    rm10010mpMesrclientNetTxBiasEntry.setStatus("current")


class _Rm10010mpMesrclientNetTxBiasIndex_Type(Integer32):
    """Custom type rm10010mpMesrclientNetTxBiasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010mpMesrclientNetTxBiasIndex_Type.__name__ = "Integer32"
_Rm10010mpMesrclientNetTxBiasIndex_Object = MibTableColumn
rm10010mpMesrclientNetTxBiasIndex = _Rm10010mpMesrclientNetTxBiasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 2, 32, 1, 1),
    _Rm10010mpMesrclientNetTxBiasIndex_Type()
)
rm10010mpMesrclientNetTxBiasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrclientNetTxBiasIndex.setStatus("current")


class _Rm10010mpMesrclientNetTxBiasPortn_Type(Integer32):
    """Custom type rm10010mpMesrclientNetTxBiasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010mpMesrclientNetTxBiasPortn_Type.__name__ = "Integer32"
_Rm10010mpMesrclientNetTxBiasPortn_Object = MibTableColumn
rm10010mpMesrclientNetTxBiasPortn = _Rm10010mpMesrclientNetTxBiasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 2, 32, 1, 2),
    _Rm10010mpMesrclientNetTxBiasPortn_Type()
)
rm10010mpMesrclientNetTxBiasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrclientNetTxBiasPortn.setStatus("current")
_Rm10010mpMesrclientNetTxPwrTable_Object = MibTable
rm10010mpMesrclientNetTxPwrTable = _Rm10010mpMesrclientNetTxPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 2, 48)
)
if mibBuilder.loadTexts:
    rm10010mpMesrclientNetTxPwrTable.setStatus("current")
_Rm10010mpMesrclientNetTxPwrEntry_Object = MibTableRow
rm10010mpMesrclientNetTxPwrEntry = _Rm10010mpMesrclientNetTxPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 2, 48, 1)
)
rm10010mpMesrclientNetTxPwrEntry.setIndexNames(
    (0, "EKINOPS-Rm10010mp-MIB", "rm10010mpMesrclientNetTxPwrIndex"),
)
if mibBuilder.loadTexts:
    rm10010mpMesrclientNetTxPwrEntry.setStatus("current")


class _Rm10010mpMesrclientNetTxPwrIndex_Type(Integer32):
    """Custom type rm10010mpMesrclientNetTxPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010mpMesrclientNetTxPwrIndex_Type.__name__ = "Integer32"
_Rm10010mpMesrclientNetTxPwrIndex_Object = MibTableColumn
rm10010mpMesrclientNetTxPwrIndex = _Rm10010mpMesrclientNetTxPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 2, 48, 1, 1),
    _Rm10010mpMesrclientNetTxPwrIndex_Type()
)
rm10010mpMesrclientNetTxPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrclientNetTxPwrIndex.setStatus("current")


class _Rm10010mpMesrclientNetTxPwrPortn_Type(Integer32):
    """Custom type rm10010mpMesrclientNetTxPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010mpMesrclientNetTxPwrPortn_Type.__name__ = "Integer32"
_Rm10010mpMesrclientNetTxPwrPortn_Object = MibTableColumn
rm10010mpMesrclientNetTxPwrPortn = _Rm10010mpMesrclientNetTxPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 2, 48, 1, 2),
    _Rm10010mpMesrclientNetTxPwrPortn_Type()
)
rm10010mpMesrclientNetTxPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrclientNetTxPwrPortn.setStatus("current")
_Rm10010mpMesrclientNetRxPwrTable_Object = MibTable
rm10010mpMesrclientNetRxPwrTable = _Rm10010mpMesrclientNetRxPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 2, 64)
)
if mibBuilder.loadTexts:
    rm10010mpMesrclientNetRxPwrTable.setStatus("current")
_Rm10010mpMesrclientNetRxPwrEntry_Object = MibTableRow
rm10010mpMesrclientNetRxPwrEntry = _Rm10010mpMesrclientNetRxPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 2, 64, 1)
)
rm10010mpMesrclientNetRxPwrEntry.setIndexNames(
    (0, "EKINOPS-Rm10010mp-MIB", "rm10010mpMesrclientNetRxPwrIndex"),
)
if mibBuilder.loadTexts:
    rm10010mpMesrclientNetRxPwrEntry.setStatus("current")


class _Rm10010mpMesrclientNetRxPwrIndex_Type(Integer32):
    """Custom type rm10010mpMesrclientNetRxPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010mpMesrclientNetRxPwrIndex_Type.__name__ = "Integer32"
_Rm10010mpMesrclientNetRxPwrIndex_Object = MibTableColumn
rm10010mpMesrclientNetRxPwrIndex = _Rm10010mpMesrclientNetRxPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 2, 64, 1, 1),
    _Rm10010mpMesrclientNetRxPwrIndex_Type()
)
rm10010mpMesrclientNetRxPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrclientNetRxPwrIndex.setStatus("current")


class _Rm10010mpMesrclientNetRxPwrPortn_Type(Integer32):
    """Custom type rm10010mpMesrclientNetRxPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010mpMesrclientNetRxPwrPortn_Type.__name__ = "Integer32"
_Rm10010mpMesrclientNetRxPwrPortn_Object = MibTableColumn
rm10010mpMesrclientNetRxPwrPortn = _Rm10010mpMesrclientNetRxPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 2, 64, 1, 2),
    _Rm10010mpMesrclientNetRxPwrPortn_Type()
)
rm10010mpMesrclientNetRxPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrclientNetRxPwrPortn.setStatus("current")
_Rm10010mpMesrLine_ObjectIdentity = ObjectIdentity
rm10010mpMesrLine = _Rm10010mpMesrLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 3)
)


class _Rm10010mpMesrlineMsaTemp_Type(Unsigned32):
    """Custom type rm10010mpMesrlineMsaTemp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010mpMesrlineMsaTemp_Type.__name__ = "Unsigned32"
_Rm10010mpMesrlineMsaTemp_Object = MibScalar
rm10010mpMesrlineMsaTemp = _Rm10010mpMesrlineMsaTemp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 3, 12),
    _Rm10010mpMesrlineMsaTemp_Type()
)
rm10010mpMesrlineMsaTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrlineMsaTemp.setStatus("current")


class _Rm10010mpMesrlineMsa3v3Voltage_Type(Unsigned32):
    """Custom type rm10010mpMesrlineMsa3v3Voltage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010mpMesrlineMsa3v3Voltage_Type.__name__ = "Unsigned32"
_Rm10010mpMesrlineMsa3v3Voltage_Object = MibScalar
rm10010mpMesrlineMsa3v3Voltage = _Rm10010mpMesrlineMsa3v3Voltage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 3, 13),
    _Rm10010mpMesrlineMsa3v3Voltage_Type()
)
rm10010mpMesrlineMsa3v3Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrlineMsa3v3Voltage.setStatus("current")


class _Rm10010mpMesrlineSoaBiasCurrent_Type(Unsigned32):
    """Custom type rm10010mpMesrlineSoaBiasCurrent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010mpMesrlineSoaBiasCurrent_Type.__name__ = "Unsigned32"
_Rm10010mpMesrlineSoaBiasCurrent_Object = MibScalar
rm10010mpMesrlineSoaBiasCurrent = _Rm10010mpMesrlineSoaBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 3, 14),
    _Rm10010mpMesrlineSoaBiasCurrent_Type()
)
rm10010mpMesrlineSoaBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrlineSoaBiasCurrent.setStatus("current")
_Rm10010mpMesrlineNetTxLaserOutputPwrTable_Object = MibTable
rm10010mpMesrlineNetTxLaserOutputPwrTable = _Rm10010mpMesrlineNetTxLaserOutputPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 3, 80)
)
if mibBuilder.loadTexts:
    rm10010mpMesrlineNetTxLaserOutputPwrTable.setStatus("current")
_Rm10010mpMesrlineNetTxLaserOutputPwrEntry_Object = MibTableRow
rm10010mpMesrlineNetTxLaserOutputPwrEntry = _Rm10010mpMesrlineNetTxLaserOutputPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 3, 80, 1)
)
rm10010mpMesrlineNetTxLaserOutputPwrEntry.setIndexNames(
    (0, "EKINOPS-Rm10010mp-MIB", "rm10010mpMesrlineNetTxLaserOutputPwrIndex"),
)
if mibBuilder.loadTexts:
    rm10010mpMesrlineNetTxLaserOutputPwrEntry.setStatus("current")


class _Rm10010mpMesrlineNetTxLaserOutputPwrIndex_Type(Integer32):
    """Custom type rm10010mpMesrlineNetTxLaserOutputPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010mpMesrlineNetTxLaserOutputPwrIndex_Type.__name__ = "Integer32"
_Rm10010mpMesrlineNetTxLaserOutputPwrIndex_Object = MibTableColumn
rm10010mpMesrlineNetTxLaserOutputPwrIndex = _Rm10010mpMesrlineNetTxLaserOutputPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 3, 80, 1, 1),
    _Rm10010mpMesrlineNetTxLaserOutputPwrIndex_Type()
)
rm10010mpMesrlineNetTxLaserOutputPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrlineNetTxLaserOutputPwrIndex.setStatus("current")


class _Rm10010mpMesrlineNetTxLaserOutputPwrPortn_Type(Integer32):
    """Custom type rm10010mpMesrlineNetTxLaserOutputPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010mpMesrlineNetTxLaserOutputPwrPortn_Type.__name__ = "Integer32"
_Rm10010mpMesrlineNetTxLaserOutputPwrPortn_Object = MibTableColumn
rm10010mpMesrlineNetTxLaserOutputPwrPortn = _Rm10010mpMesrlineNetTxLaserOutputPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 3, 80, 1, 2),
    _Rm10010mpMesrlineNetTxLaserOutputPwrPortn_Type()
)
rm10010mpMesrlineNetTxLaserOutputPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrlineNetTxLaserOutputPwrPortn.setStatus("current")
_Rm10010mpMesrlineNetTxLaserTempTable_Object = MibTable
rm10010mpMesrlineNetTxLaserTempTable = _Rm10010mpMesrlineNetTxLaserTempTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 3, 96)
)
if mibBuilder.loadTexts:
    rm10010mpMesrlineNetTxLaserTempTable.setStatus("current")
_Rm10010mpMesrlineNetTxLaserTempEntry_Object = MibTableRow
rm10010mpMesrlineNetTxLaserTempEntry = _Rm10010mpMesrlineNetTxLaserTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 3, 96, 1)
)
rm10010mpMesrlineNetTxLaserTempEntry.setIndexNames(
    (0, "EKINOPS-Rm10010mp-MIB", "rm10010mpMesrlineNetTxLaserTempIndex"),
)
if mibBuilder.loadTexts:
    rm10010mpMesrlineNetTxLaserTempEntry.setStatus("current")


class _Rm10010mpMesrlineNetTxLaserTempIndex_Type(Integer32):
    """Custom type rm10010mpMesrlineNetTxLaserTempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010mpMesrlineNetTxLaserTempIndex_Type.__name__ = "Integer32"
_Rm10010mpMesrlineNetTxLaserTempIndex_Object = MibTableColumn
rm10010mpMesrlineNetTxLaserTempIndex = _Rm10010mpMesrlineNetTxLaserTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 3, 96, 1, 1),
    _Rm10010mpMesrlineNetTxLaserTempIndex_Type()
)
rm10010mpMesrlineNetTxLaserTempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrlineNetTxLaserTempIndex.setStatus("current")


class _Rm10010mpMesrlineNetTxLaserTempPortn_Type(Integer32):
    """Custom type rm10010mpMesrlineNetTxLaserTempPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010mpMesrlineNetTxLaserTempPortn_Type.__name__ = "Integer32"
_Rm10010mpMesrlineNetTxLaserTempPortn_Object = MibTableColumn
rm10010mpMesrlineNetTxLaserTempPortn = _Rm10010mpMesrlineNetTxLaserTempPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 3, 96, 1, 2),
    _Rm10010mpMesrlineNetTxLaserTempPortn_Type()
)
rm10010mpMesrlineNetTxLaserTempPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrlineNetTxLaserTempPortn.setStatus("current")
_Rm10010mpMesrlineNetTxBiasCurrentTable_Object = MibTable
rm10010mpMesrlineNetTxBiasCurrentTable = _Rm10010mpMesrlineNetTxBiasCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 3, 112)
)
if mibBuilder.loadTexts:
    rm10010mpMesrlineNetTxBiasCurrentTable.setStatus("current")
_Rm10010mpMesrlineNetTxBiasCurrentEntry_Object = MibTableRow
rm10010mpMesrlineNetTxBiasCurrentEntry = _Rm10010mpMesrlineNetTxBiasCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 3, 112, 1)
)
rm10010mpMesrlineNetTxBiasCurrentEntry.setIndexNames(
    (0, "EKINOPS-Rm10010mp-MIB", "rm10010mpMesrlineNetTxBiasCurrentIndex"),
)
if mibBuilder.loadTexts:
    rm10010mpMesrlineNetTxBiasCurrentEntry.setStatus("current")


class _Rm10010mpMesrlineNetTxBiasCurrentIndex_Type(Integer32):
    """Custom type rm10010mpMesrlineNetTxBiasCurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010mpMesrlineNetTxBiasCurrentIndex_Type.__name__ = "Integer32"
_Rm10010mpMesrlineNetTxBiasCurrentIndex_Object = MibTableColumn
rm10010mpMesrlineNetTxBiasCurrentIndex = _Rm10010mpMesrlineNetTxBiasCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 3, 112, 1, 1),
    _Rm10010mpMesrlineNetTxBiasCurrentIndex_Type()
)
rm10010mpMesrlineNetTxBiasCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrlineNetTxBiasCurrentIndex.setStatus("current")


class _Rm10010mpMesrlineNetTxBiasCurrentPortn_Type(Integer32):
    """Custom type rm10010mpMesrlineNetTxBiasCurrentPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010mpMesrlineNetTxBiasCurrentPortn_Type.__name__ = "Integer32"
_Rm10010mpMesrlineNetTxBiasCurrentPortn_Object = MibTableColumn
rm10010mpMesrlineNetTxBiasCurrentPortn = _Rm10010mpMesrlineNetTxBiasCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 3, 112, 1, 2),
    _Rm10010mpMesrlineNetTxBiasCurrentPortn_Type()
)
rm10010mpMesrlineNetTxBiasCurrentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrlineNetTxBiasCurrentPortn.setStatus("current")
_Rm10010mpMesrlineNetRxInputPwrTable_Object = MibTable
rm10010mpMesrlineNetRxInputPwrTable = _Rm10010mpMesrlineNetRxInputPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 3, 128)
)
if mibBuilder.loadTexts:
    rm10010mpMesrlineNetRxInputPwrTable.setStatus("current")
_Rm10010mpMesrlineNetRxInputPwrEntry_Object = MibTableRow
rm10010mpMesrlineNetRxInputPwrEntry = _Rm10010mpMesrlineNetRxInputPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 3, 128, 1)
)
rm10010mpMesrlineNetRxInputPwrEntry.setIndexNames(
    (0, "EKINOPS-Rm10010mp-MIB", "rm10010mpMesrlineNetRxInputPwrIndex"),
)
if mibBuilder.loadTexts:
    rm10010mpMesrlineNetRxInputPwrEntry.setStatus("current")


class _Rm10010mpMesrlineNetRxInputPwrIndex_Type(Integer32):
    """Custom type rm10010mpMesrlineNetRxInputPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010mpMesrlineNetRxInputPwrIndex_Type.__name__ = "Integer32"
_Rm10010mpMesrlineNetRxInputPwrIndex_Object = MibTableColumn
rm10010mpMesrlineNetRxInputPwrIndex = _Rm10010mpMesrlineNetRxInputPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 3, 128, 1, 1),
    _Rm10010mpMesrlineNetRxInputPwrIndex_Type()
)
rm10010mpMesrlineNetRxInputPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrlineNetRxInputPwrIndex.setStatus("current")


class _Rm10010mpMesrlineNetRxInputPwrPortn_Type(Integer32):
    """Custom type rm10010mpMesrlineNetRxInputPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010mpMesrlineNetRxInputPwrPortn_Type.__name__ = "Integer32"
_Rm10010mpMesrlineNetRxInputPwrPortn_Object = MibTableColumn
rm10010mpMesrlineNetRxInputPwrPortn = _Rm10010mpMesrlineNetRxInputPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 3, 128, 1, 2),
    _Rm10010mpMesrlineNetRxInputPwrPortn_Type()
)
rm10010mpMesrlineNetRxInputPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrlineNetRxInputPwrPortn.setStatus("current")
_Rm10010mpMesrlineResidualChromaticDispTable_Object = MibTable
rm10010mpMesrlineResidualChromaticDispTable = _Rm10010mpMesrlineResidualChromaticDispTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 3, 144)
)
if mibBuilder.loadTexts:
    rm10010mpMesrlineResidualChromaticDispTable.setStatus("current")
_Rm10010mpMesrlineResidualChromaticDispEntry_Object = MibTableRow
rm10010mpMesrlineResidualChromaticDispEntry = _Rm10010mpMesrlineResidualChromaticDispEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 3, 144, 1)
)
rm10010mpMesrlineResidualChromaticDispEntry.setIndexNames(
    (0, "EKINOPS-Rm10010mp-MIB", "rm10010mpMesrlineResidualChromaticDispIndex"),
)
if mibBuilder.loadTexts:
    rm10010mpMesrlineResidualChromaticDispEntry.setStatus("current")


class _Rm10010mpMesrlineResidualChromaticDispIndex_Type(Integer32):
    """Custom type rm10010mpMesrlineResidualChromaticDispIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010mpMesrlineResidualChromaticDispIndex_Type.__name__ = "Integer32"
_Rm10010mpMesrlineResidualChromaticDispIndex_Object = MibTableColumn
rm10010mpMesrlineResidualChromaticDispIndex = _Rm10010mpMesrlineResidualChromaticDispIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 3, 144, 1, 1),
    _Rm10010mpMesrlineResidualChromaticDispIndex_Type()
)
rm10010mpMesrlineResidualChromaticDispIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrlineResidualChromaticDispIndex.setStatus("current")


class _Rm10010mpMesrlineResidualChromaticDispPortn_Type(Integer32):
    """Custom type rm10010mpMesrlineResidualChromaticDispPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010mpMesrlineResidualChromaticDispPortn_Type.__name__ = "Integer32"
_Rm10010mpMesrlineResidualChromaticDispPortn_Object = MibTableColumn
rm10010mpMesrlineResidualChromaticDispPortn = _Rm10010mpMesrlineResidualChromaticDispPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 3, 144, 1, 2),
    _Rm10010mpMesrlineResidualChromaticDispPortn_Type()
)
rm10010mpMesrlineResidualChromaticDispPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrlineResidualChromaticDispPortn.setStatus("current")
_Rm10010mpMesrlineDiffGroupDelayTable_Object = MibTable
rm10010mpMesrlineDiffGroupDelayTable = _Rm10010mpMesrlineDiffGroupDelayTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 3, 148)
)
if mibBuilder.loadTexts:
    rm10010mpMesrlineDiffGroupDelayTable.setStatus("current")
_Rm10010mpMesrlineDiffGroupDelayEntry_Object = MibTableRow
rm10010mpMesrlineDiffGroupDelayEntry = _Rm10010mpMesrlineDiffGroupDelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 3, 148, 1)
)
rm10010mpMesrlineDiffGroupDelayEntry.setIndexNames(
    (0, "EKINOPS-Rm10010mp-MIB", "rm10010mpMesrlineDiffGroupDelayIndex"),
)
if mibBuilder.loadTexts:
    rm10010mpMesrlineDiffGroupDelayEntry.setStatus("current")


class _Rm10010mpMesrlineDiffGroupDelayIndex_Type(Integer32):
    """Custom type rm10010mpMesrlineDiffGroupDelayIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010mpMesrlineDiffGroupDelayIndex_Type.__name__ = "Integer32"
_Rm10010mpMesrlineDiffGroupDelayIndex_Object = MibTableColumn
rm10010mpMesrlineDiffGroupDelayIndex = _Rm10010mpMesrlineDiffGroupDelayIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 3, 148, 1, 1),
    _Rm10010mpMesrlineDiffGroupDelayIndex_Type()
)
rm10010mpMesrlineDiffGroupDelayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrlineDiffGroupDelayIndex.setStatus("current")


class _Rm10010mpMesrlineDiffGroupDelayPortn_Type(Integer32):
    """Custom type rm10010mpMesrlineDiffGroupDelayPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010mpMesrlineDiffGroupDelayPortn_Type.__name__ = "Integer32"
_Rm10010mpMesrlineDiffGroupDelayPortn_Object = MibTableColumn
rm10010mpMesrlineDiffGroupDelayPortn = _Rm10010mpMesrlineDiffGroupDelayPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 3, 148, 1, 2),
    _Rm10010mpMesrlineDiffGroupDelayPortn_Type()
)
rm10010mpMesrlineDiffGroupDelayPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrlineDiffGroupDelayPortn.setStatus("current")
_Rm10010mpMesrlineQFactorTable_Object = MibTable
rm10010mpMesrlineQFactorTable = _Rm10010mpMesrlineQFactorTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 3, 152)
)
if mibBuilder.loadTexts:
    rm10010mpMesrlineQFactorTable.setStatus("current")
_Rm10010mpMesrlineQFactorEntry_Object = MibTableRow
rm10010mpMesrlineQFactorEntry = _Rm10010mpMesrlineQFactorEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 3, 152, 1)
)
rm10010mpMesrlineQFactorEntry.setIndexNames(
    (0, "EKINOPS-Rm10010mp-MIB", "rm10010mpMesrlineQFactorIndex"),
)
if mibBuilder.loadTexts:
    rm10010mpMesrlineQFactorEntry.setStatus("current")


class _Rm10010mpMesrlineQFactorIndex_Type(Integer32):
    """Custom type rm10010mpMesrlineQFactorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010mpMesrlineQFactorIndex_Type.__name__ = "Integer32"
_Rm10010mpMesrlineQFactorIndex_Object = MibTableColumn
rm10010mpMesrlineQFactorIndex = _Rm10010mpMesrlineQFactorIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 3, 152, 1, 1),
    _Rm10010mpMesrlineQFactorIndex_Type()
)
rm10010mpMesrlineQFactorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrlineQFactorIndex.setStatus("current")


class _Rm10010mpMesrlineQFactorPortn_Type(Integer32):
    """Custom type rm10010mpMesrlineQFactorPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010mpMesrlineQFactorPortn_Type.__name__ = "Integer32"
_Rm10010mpMesrlineQFactorPortn_Object = MibTableColumn
rm10010mpMesrlineQFactorPortn = _Rm10010mpMesrlineQFactorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 3, 152, 1, 2),
    _Rm10010mpMesrlineQFactorPortn_Type()
)
rm10010mpMesrlineQFactorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrlineQFactorPortn.setStatus("current")
_Rm10010mpMesrlineCarrierFreqOffsetTable_Object = MibTable
rm10010mpMesrlineCarrierFreqOffsetTable = _Rm10010mpMesrlineCarrierFreqOffsetTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 3, 156)
)
if mibBuilder.loadTexts:
    rm10010mpMesrlineCarrierFreqOffsetTable.setStatus("current")
_Rm10010mpMesrlineCarrierFreqOffsetEntry_Object = MibTableRow
rm10010mpMesrlineCarrierFreqOffsetEntry = _Rm10010mpMesrlineCarrierFreqOffsetEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 3, 156, 1)
)
rm10010mpMesrlineCarrierFreqOffsetEntry.setIndexNames(
    (0, "EKINOPS-Rm10010mp-MIB", "rm10010mpMesrlineCarrierFreqOffsetIndex"),
)
if mibBuilder.loadTexts:
    rm10010mpMesrlineCarrierFreqOffsetEntry.setStatus("current")


class _Rm10010mpMesrlineCarrierFreqOffsetIndex_Type(Integer32):
    """Custom type rm10010mpMesrlineCarrierFreqOffsetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010mpMesrlineCarrierFreqOffsetIndex_Type.__name__ = "Integer32"
_Rm10010mpMesrlineCarrierFreqOffsetIndex_Object = MibTableColumn
rm10010mpMesrlineCarrierFreqOffsetIndex = _Rm10010mpMesrlineCarrierFreqOffsetIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 3, 156, 1, 1),
    _Rm10010mpMesrlineCarrierFreqOffsetIndex_Type()
)
rm10010mpMesrlineCarrierFreqOffsetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrlineCarrierFreqOffsetIndex.setStatus("current")


class _Rm10010mpMesrlineCarrierFreqOffsetPortn_Type(Integer32):
    """Custom type rm10010mpMesrlineCarrierFreqOffsetPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010mpMesrlineCarrierFreqOffsetPortn_Type.__name__ = "Integer32"
_Rm10010mpMesrlineCarrierFreqOffsetPortn_Object = MibTableColumn
rm10010mpMesrlineCarrierFreqOffsetPortn = _Rm10010mpMesrlineCarrierFreqOffsetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 3, 156, 1, 2),
    _Rm10010mpMesrlineCarrierFreqOffsetPortn_Type()
)
rm10010mpMesrlineCarrierFreqOffsetPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrlineCarrierFreqOffsetPortn.setStatus("current")
_Rm10010mpMesrlineOsnrTable_Object = MibTable
rm10010mpMesrlineOsnrTable = _Rm10010mpMesrlineOsnrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 3, 160)
)
if mibBuilder.loadTexts:
    rm10010mpMesrlineOsnrTable.setStatus("current")
_Rm10010mpMesrlineOsnrEntry_Object = MibTableRow
rm10010mpMesrlineOsnrEntry = _Rm10010mpMesrlineOsnrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 3, 160, 1)
)
rm10010mpMesrlineOsnrEntry.setIndexNames(
    (0, "EKINOPS-Rm10010mp-MIB", "rm10010mpMesrlineOsnrIndex"),
)
if mibBuilder.loadTexts:
    rm10010mpMesrlineOsnrEntry.setStatus("current")


class _Rm10010mpMesrlineOsnrIndex_Type(Integer32):
    """Custom type rm10010mpMesrlineOsnrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010mpMesrlineOsnrIndex_Type.__name__ = "Integer32"
_Rm10010mpMesrlineOsnrIndex_Object = MibTableColumn
rm10010mpMesrlineOsnrIndex = _Rm10010mpMesrlineOsnrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 3, 160, 1, 1),
    _Rm10010mpMesrlineOsnrIndex_Type()
)
rm10010mpMesrlineOsnrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrlineOsnrIndex.setStatus("current")


class _Rm10010mpMesrlineOsnrPortn_Type(Integer32):
    """Custom type rm10010mpMesrlineOsnrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rm10010mpMesrlineOsnrPortn_Type.__name__ = "Integer32"
_Rm10010mpMesrlineOsnrPortn_Object = MibTableColumn
rm10010mpMesrlineOsnrPortn = _Rm10010mpMesrlineOsnrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 3, 3, 160, 1, 2),
    _Rm10010mpMesrlineOsnrPortn_Type()
)
rm10010mpMesrlineOsnrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMesrlineOsnrPortn.setStatus("current")
_Rm10010mpcounters_ObjectIdentity = ObjectIdentity
rm10010mpcounters = _Rm10010mpcounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4)
)
_Rm10010mpCntOther_ObjectIdentity = ObjectIdentity
rm10010mpCntOther = _Rm10010mpCntOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4, 1)
)
_Rm10010mpCntClient_ObjectIdentity = ObjectIdentity
rm10010mpCntClient = _Rm10010mpCntClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4, 2)
)
_Rm10010mpCntclientInputErrorCounterLaneOneTable_Object = MibTable
rm10010mpCntclientInputErrorCounterLaneOneTable = _Rm10010mpCntclientInputErrorCounterLaneOneTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4, 2, 16)
)
if mibBuilder.loadTexts:
    rm10010mpCntclientInputErrorCounterLaneOneTable.setStatus("current")
_Rm10010mpCntclientInputErrorCounterLaneOneEntry_Object = MibTableRow
rm10010mpCntclientInputErrorCounterLaneOneEntry = _Rm10010mpCntclientInputErrorCounterLaneOneEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4, 2, 16, 1)
)
rm10010mpCntclientInputErrorCounterLaneOneEntry.setIndexNames(
    (0, "EKINOPS-Rm10010mp-MIB", "rm10010mpCntclientInputErrorCounterLaneOneIndex"),
)
if mibBuilder.loadTexts:
    rm10010mpCntclientInputErrorCounterLaneOneEntry.setStatus("current")


class _Rm10010mpCntclientInputErrorCounterLaneOneIndex_Type(Integer32):
    """Custom type rm10010mpCntclientInputErrorCounterLaneOneIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010mpCntclientInputErrorCounterLaneOneIndex_Type.__name__ = "Integer32"
_Rm10010mpCntclientInputErrorCounterLaneOneIndex_Object = MibTableColumn
rm10010mpCntclientInputErrorCounterLaneOneIndex = _Rm10010mpCntclientInputErrorCounterLaneOneIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4, 2, 16, 1, 1),
    _Rm10010mpCntclientInputErrorCounterLaneOneIndex_Type()
)
rm10010mpCntclientInputErrorCounterLaneOneIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCntclientInputErrorCounterLaneOneIndex.setStatus("current")
_Rm10010mpCntclientInputErrorCounterLaneOneValuePortn_Type = Counter32
_Rm10010mpCntclientInputErrorCounterLaneOneValuePortn_Object = MibTableColumn
rm10010mpCntclientInputErrorCounterLaneOneValuePortn = _Rm10010mpCntclientInputErrorCounterLaneOneValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4, 2, 16, 1, 2),
    _Rm10010mpCntclientInputErrorCounterLaneOneValuePortn_Type()
)
rm10010mpCntclientInputErrorCounterLaneOneValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCntclientInputErrorCounterLaneOneValuePortn.setStatus("current")
_Rm10010mpCntclientInputErrorCounterLaneOneErrorPortn_Type = EkiOnOff
_Rm10010mpCntclientInputErrorCounterLaneOneErrorPortn_Object = MibTableColumn
rm10010mpCntclientInputErrorCounterLaneOneErrorPortn = _Rm10010mpCntclientInputErrorCounterLaneOneErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4, 2, 16, 1, 3),
    _Rm10010mpCntclientInputErrorCounterLaneOneErrorPortn_Type()
)
rm10010mpCntclientInputErrorCounterLaneOneErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCntclientInputErrorCounterLaneOneErrorPortn.setStatus("current")
_Rm10010mpCntclientInputErrorCounterLaneOneOverloadPortn_Type = EkiOnOff
_Rm10010mpCntclientInputErrorCounterLaneOneOverloadPortn_Object = MibTableColumn
rm10010mpCntclientInputErrorCounterLaneOneOverloadPortn = _Rm10010mpCntclientInputErrorCounterLaneOneOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4, 2, 16, 1, 4),
    _Rm10010mpCntclientInputErrorCounterLaneOneOverloadPortn_Type()
)
rm10010mpCntclientInputErrorCounterLaneOneOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCntclientInputErrorCounterLaneOneOverloadPortn.setStatus("current")
_Rm10010mpCntclientInputErrorCounterLaneTwoTable_Object = MibTable
rm10010mpCntclientInputErrorCounterLaneTwoTable = _Rm10010mpCntclientInputErrorCounterLaneTwoTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4, 2, 32)
)
if mibBuilder.loadTexts:
    rm10010mpCntclientInputErrorCounterLaneTwoTable.setStatus("current")
_Rm10010mpCntclientInputErrorCounterLaneTwoEntry_Object = MibTableRow
rm10010mpCntclientInputErrorCounterLaneTwoEntry = _Rm10010mpCntclientInputErrorCounterLaneTwoEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4, 2, 32, 1)
)
rm10010mpCntclientInputErrorCounterLaneTwoEntry.setIndexNames(
    (0, "EKINOPS-Rm10010mp-MIB", "rm10010mpCntclientInputErrorCounterLaneTwoIndex"),
)
if mibBuilder.loadTexts:
    rm10010mpCntclientInputErrorCounterLaneTwoEntry.setStatus("current")


class _Rm10010mpCntclientInputErrorCounterLaneTwoIndex_Type(Integer32):
    """Custom type rm10010mpCntclientInputErrorCounterLaneTwoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010mpCntclientInputErrorCounterLaneTwoIndex_Type.__name__ = "Integer32"
_Rm10010mpCntclientInputErrorCounterLaneTwoIndex_Object = MibTableColumn
rm10010mpCntclientInputErrorCounterLaneTwoIndex = _Rm10010mpCntclientInputErrorCounterLaneTwoIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4, 2, 32, 1, 1),
    _Rm10010mpCntclientInputErrorCounterLaneTwoIndex_Type()
)
rm10010mpCntclientInputErrorCounterLaneTwoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCntclientInputErrorCounterLaneTwoIndex.setStatus("current")
_Rm10010mpCntclientInputErrorCounterLaneTwoValuePortn_Type = Counter32
_Rm10010mpCntclientInputErrorCounterLaneTwoValuePortn_Object = MibTableColumn
rm10010mpCntclientInputErrorCounterLaneTwoValuePortn = _Rm10010mpCntclientInputErrorCounterLaneTwoValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4, 2, 32, 1, 2),
    _Rm10010mpCntclientInputErrorCounterLaneTwoValuePortn_Type()
)
rm10010mpCntclientInputErrorCounterLaneTwoValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCntclientInputErrorCounterLaneTwoValuePortn.setStatus("current")
_Rm10010mpCntclientInputErrorCounterLaneTwoErrorPortn_Type = EkiOnOff
_Rm10010mpCntclientInputErrorCounterLaneTwoErrorPortn_Object = MibTableColumn
rm10010mpCntclientInputErrorCounterLaneTwoErrorPortn = _Rm10010mpCntclientInputErrorCounterLaneTwoErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4, 2, 32, 1, 3),
    _Rm10010mpCntclientInputErrorCounterLaneTwoErrorPortn_Type()
)
rm10010mpCntclientInputErrorCounterLaneTwoErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCntclientInputErrorCounterLaneTwoErrorPortn.setStatus("current")
_Rm10010mpCntclientInputErrorCounterLaneTwoOverloadPortn_Type = EkiOnOff
_Rm10010mpCntclientInputErrorCounterLaneTwoOverloadPortn_Object = MibTableColumn
rm10010mpCntclientInputErrorCounterLaneTwoOverloadPortn = _Rm10010mpCntclientInputErrorCounterLaneTwoOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4, 2, 32, 1, 4),
    _Rm10010mpCntclientInputErrorCounterLaneTwoOverloadPortn_Type()
)
rm10010mpCntclientInputErrorCounterLaneTwoOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCntclientInputErrorCounterLaneTwoOverloadPortn.setStatus("current")
_Rm10010mpCntclientInputErrorCounterTable_Object = MibTable
rm10010mpCntclientInputErrorCounterTable = _Rm10010mpCntclientInputErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4, 2, 80)
)
if mibBuilder.loadTexts:
    rm10010mpCntclientInputErrorCounterTable.setStatus("current")
_Rm10010mpCntclientInputErrorCounterEntry_Object = MibTableRow
rm10010mpCntclientInputErrorCounterEntry = _Rm10010mpCntclientInputErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4, 2, 80, 1)
)
rm10010mpCntclientInputErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Rm10010mp-MIB", "rm10010mpCntclientInputErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    rm10010mpCntclientInputErrorCounterEntry.setStatus("current")


class _Rm10010mpCntclientInputErrorCounterIndex_Type(Integer32):
    """Custom type rm10010mpCntclientInputErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010mpCntclientInputErrorCounterIndex_Type.__name__ = "Integer32"
_Rm10010mpCntclientInputErrorCounterIndex_Object = MibTableColumn
rm10010mpCntclientInputErrorCounterIndex = _Rm10010mpCntclientInputErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4, 2, 80, 1, 1),
    _Rm10010mpCntclientInputErrorCounterIndex_Type()
)
rm10010mpCntclientInputErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCntclientInputErrorCounterIndex.setStatus("current")
_Rm10010mpCntclientInputErrorCounterValuePortn_Type = Counter32
_Rm10010mpCntclientInputErrorCounterValuePortn_Object = MibTableColumn
rm10010mpCntclientInputErrorCounterValuePortn = _Rm10010mpCntclientInputErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4, 2, 80, 1, 2),
    _Rm10010mpCntclientInputErrorCounterValuePortn_Type()
)
rm10010mpCntclientInputErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCntclientInputErrorCounterValuePortn.setStatus("current")
_Rm10010mpCntclientInputErrorCounterErrorPortn_Type = EkiOnOff
_Rm10010mpCntclientInputErrorCounterErrorPortn_Object = MibTableColumn
rm10010mpCntclientInputErrorCounterErrorPortn = _Rm10010mpCntclientInputErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4, 2, 80, 1, 3),
    _Rm10010mpCntclientInputErrorCounterErrorPortn_Type()
)
rm10010mpCntclientInputErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCntclientInputErrorCounterErrorPortn.setStatus("current")
_Rm10010mpCntclientInputErrorCounterOverloadPortn_Type = EkiOnOff
_Rm10010mpCntclientInputErrorCounterOverloadPortn_Object = MibTableColumn
rm10010mpCntclientInputErrorCounterOverloadPortn = _Rm10010mpCntclientInputErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4, 2, 80, 1, 4),
    _Rm10010mpCntclientInputErrorCounterOverloadPortn_Type()
)
rm10010mpCntclientInputErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCntclientInputErrorCounterOverloadPortn.setStatus("current")
_Rm10010mpCntclientCbipCounterTable_Object = MibTable
rm10010mpCntclientCbipCounterTable = _Rm10010mpCntclientCbipCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4, 2, 96)
)
if mibBuilder.loadTexts:
    rm10010mpCntclientCbipCounterTable.setStatus("current")
_Rm10010mpCntclientCbipCounterEntry_Object = MibTableRow
rm10010mpCntclientCbipCounterEntry = _Rm10010mpCntclientCbipCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4, 2, 96, 1)
)
rm10010mpCntclientCbipCounterEntry.setIndexNames(
    (0, "EKINOPS-Rm10010mp-MIB", "rm10010mpCntclientCbipCounterIndex"),
)
if mibBuilder.loadTexts:
    rm10010mpCntclientCbipCounterEntry.setStatus("current")


class _Rm10010mpCntclientCbipCounterIndex_Type(Integer32):
    """Custom type rm10010mpCntclientCbipCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010mpCntclientCbipCounterIndex_Type.__name__ = "Integer32"
_Rm10010mpCntclientCbipCounterIndex_Object = MibTableColumn
rm10010mpCntclientCbipCounterIndex = _Rm10010mpCntclientCbipCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4, 2, 96, 1, 1),
    _Rm10010mpCntclientCbipCounterIndex_Type()
)
rm10010mpCntclientCbipCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCntclientCbipCounterIndex.setStatus("current")
_Rm10010mpCntclientCbipCounterValuePortn_Type = Counter32
_Rm10010mpCntclientCbipCounterValuePortn_Object = MibTableColumn
rm10010mpCntclientCbipCounterValuePortn = _Rm10010mpCntclientCbipCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4, 2, 96, 1, 2),
    _Rm10010mpCntclientCbipCounterValuePortn_Type()
)
rm10010mpCntclientCbipCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCntclientCbipCounterValuePortn.setStatus("current")
_Rm10010mpCntclientCbipCounterErrorPortn_Type = EkiOnOff
_Rm10010mpCntclientCbipCounterErrorPortn_Object = MibTableColumn
rm10010mpCntclientCbipCounterErrorPortn = _Rm10010mpCntclientCbipCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4, 2, 96, 1, 3),
    _Rm10010mpCntclientCbipCounterErrorPortn_Type()
)
rm10010mpCntclientCbipCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCntclientCbipCounterErrorPortn.setStatus("current")
_Rm10010mpCntclientCbipCounterOverloadPortn_Type = EkiOnOff
_Rm10010mpCntclientCbipCounterOverloadPortn_Object = MibTableColumn
rm10010mpCntclientCbipCounterOverloadPortn = _Rm10010mpCntclientCbipCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4, 2, 96, 1, 4),
    _Rm10010mpCntclientCbipCounterOverloadPortn_Type()
)
rm10010mpCntclientCbipCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCntclientCbipCounterOverloadPortn.setStatus("current")
_Rm10010mpCntLine_ObjectIdentity = ObjectIdentity
rm10010mpCntLine = _Rm10010mpCntLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4, 3)
)
_Rm10010mpCntlocalLineSmBip8ErrorCounterTable_Object = MibTable
rm10010mpCntlocalLineSmBip8ErrorCounterTable = _Rm10010mpCntlocalLineSmBip8ErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4, 3, 192)
)
if mibBuilder.loadTexts:
    rm10010mpCntlocalLineSmBip8ErrorCounterTable.setStatus("current")
_Rm10010mpCntlocalLineSmBip8ErrorCounterEntry_Object = MibTableRow
rm10010mpCntlocalLineSmBip8ErrorCounterEntry = _Rm10010mpCntlocalLineSmBip8ErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4, 3, 192, 1)
)
rm10010mpCntlocalLineSmBip8ErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Rm10010mp-MIB", "rm10010mpCntlocalLineSmBip8ErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    rm10010mpCntlocalLineSmBip8ErrorCounterEntry.setStatus("current")


class _Rm10010mpCntlocalLineSmBip8ErrorCounterIndex_Type(Integer32):
    """Custom type rm10010mpCntlocalLineSmBip8ErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010mpCntlocalLineSmBip8ErrorCounterIndex_Type.__name__ = "Integer32"
_Rm10010mpCntlocalLineSmBip8ErrorCounterIndex_Object = MibTableColumn
rm10010mpCntlocalLineSmBip8ErrorCounterIndex = _Rm10010mpCntlocalLineSmBip8ErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4, 3, 192, 1, 1),
    _Rm10010mpCntlocalLineSmBip8ErrorCounterIndex_Type()
)
rm10010mpCntlocalLineSmBip8ErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCntlocalLineSmBip8ErrorCounterIndex.setStatus("current")
_Rm10010mpCntlocalLineSmBip8ErrorCounterValuePortn_Type = Counter64
_Rm10010mpCntlocalLineSmBip8ErrorCounterValuePortn_Object = MibTableColumn
rm10010mpCntlocalLineSmBip8ErrorCounterValuePortn = _Rm10010mpCntlocalLineSmBip8ErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4, 3, 192, 1, 2),
    _Rm10010mpCntlocalLineSmBip8ErrorCounterValuePortn_Type()
)
rm10010mpCntlocalLineSmBip8ErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCntlocalLineSmBip8ErrorCounterValuePortn.setStatus("current")
_Rm10010mpCntlocalLineSmBip8ErrorCounterErrorPortn_Type = EkiOnOff
_Rm10010mpCntlocalLineSmBip8ErrorCounterErrorPortn_Object = MibTableColumn
rm10010mpCntlocalLineSmBip8ErrorCounterErrorPortn = _Rm10010mpCntlocalLineSmBip8ErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4, 3, 192, 1, 3),
    _Rm10010mpCntlocalLineSmBip8ErrorCounterErrorPortn_Type()
)
rm10010mpCntlocalLineSmBip8ErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCntlocalLineSmBip8ErrorCounterErrorPortn.setStatus("current")
_Rm10010mpCntlocalLineSmBip8ErrorCounterOverloadPortn_Type = EkiOnOff
_Rm10010mpCntlocalLineSmBip8ErrorCounterOverloadPortn_Object = MibTableColumn
rm10010mpCntlocalLineSmBip8ErrorCounterOverloadPortn = _Rm10010mpCntlocalLineSmBip8ErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4, 3, 192, 1, 4),
    _Rm10010mpCntlocalLineSmBip8ErrorCounterOverloadPortn_Type()
)
rm10010mpCntlocalLineSmBip8ErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCntlocalLineSmBip8ErrorCounterOverloadPortn.setStatus("current")
_Rm10010mpCntlocalLineFecCorrectedErrorsCounterTable_Object = MibTable
rm10010mpCntlocalLineFecCorrectedErrorsCounterTable = _Rm10010mpCntlocalLineFecCorrectedErrorsCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4, 3, 193)
)
if mibBuilder.loadTexts:
    rm10010mpCntlocalLineFecCorrectedErrorsCounterTable.setStatus("current")
_Rm10010mpCntlocalLineFecCorrectedErrorsCounterEntry_Object = MibTableRow
rm10010mpCntlocalLineFecCorrectedErrorsCounterEntry = _Rm10010mpCntlocalLineFecCorrectedErrorsCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4, 3, 193, 1)
)
rm10010mpCntlocalLineFecCorrectedErrorsCounterEntry.setIndexNames(
    (0, "EKINOPS-Rm10010mp-MIB", "rm10010mpCntlocalLineFecCorrectedErrorsCounterIndex"),
)
if mibBuilder.loadTexts:
    rm10010mpCntlocalLineFecCorrectedErrorsCounterEntry.setStatus("current")


class _Rm10010mpCntlocalLineFecCorrectedErrorsCounterIndex_Type(Integer32):
    """Custom type rm10010mpCntlocalLineFecCorrectedErrorsCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010mpCntlocalLineFecCorrectedErrorsCounterIndex_Type.__name__ = "Integer32"
_Rm10010mpCntlocalLineFecCorrectedErrorsCounterIndex_Object = MibTableColumn
rm10010mpCntlocalLineFecCorrectedErrorsCounterIndex = _Rm10010mpCntlocalLineFecCorrectedErrorsCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4, 3, 193, 1, 1),
    _Rm10010mpCntlocalLineFecCorrectedErrorsCounterIndex_Type()
)
rm10010mpCntlocalLineFecCorrectedErrorsCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCntlocalLineFecCorrectedErrorsCounterIndex.setStatus("current")
_Rm10010mpCntlocalLineFecCorrectedErrorsCounterValuePortn_Type = Counter64
_Rm10010mpCntlocalLineFecCorrectedErrorsCounterValuePortn_Object = MibTableColumn
rm10010mpCntlocalLineFecCorrectedErrorsCounterValuePortn = _Rm10010mpCntlocalLineFecCorrectedErrorsCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4, 3, 193, 1, 2),
    _Rm10010mpCntlocalLineFecCorrectedErrorsCounterValuePortn_Type()
)
rm10010mpCntlocalLineFecCorrectedErrorsCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCntlocalLineFecCorrectedErrorsCounterValuePortn.setStatus("current")
_Rm10010mpCntlocalLineFecCorrectedErrorsCounterErrorPortn_Type = EkiOnOff
_Rm10010mpCntlocalLineFecCorrectedErrorsCounterErrorPortn_Object = MibTableColumn
rm10010mpCntlocalLineFecCorrectedErrorsCounterErrorPortn = _Rm10010mpCntlocalLineFecCorrectedErrorsCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4, 3, 193, 1, 3),
    _Rm10010mpCntlocalLineFecCorrectedErrorsCounterErrorPortn_Type()
)
rm10010mpCntlocalLineFecCorrectedErrorsCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCntlocalLineFecCorrectedErrorsCounterErrorPortn.setStatus("current")
_Rm10010mpCntlocalLineFecCorrectedErrorsCounterOverloadPortn_Type = EkiOnOff
_Rm10010mpCntlocalLineFecCorrectedErrorsCounterOverloadPortn_Object = MibTableColumn
rm10010mpCntlocalLineFecCorrectedErrorsCounterOverloadPortn = _Rm10010mpCntlocalLineFecCorrectedErrorsCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4, 3, 193, 1, 4),
    _Rm10010mpCntlocalLineFecCorrectedErrorsCounterOverloadPortn_Type()
)
rm10010mpCntlocalLineFecCorrectedErrorsCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCntlocalLineFecCorrectedErrorsCounterOverloadPortn.setStatus("current")
_Rm10010mpCntremoteLineSmBip8ErrorCounterTable_Object = MibTable
rm10010mpCntremoteLineSmBip8ErrorCounterTable = _Rm10010mpCntremoteLineSmBip8ErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4, 3, 194)
)
if mibBuilder.loadTexts:
    rm10010mpCntremoteLineSmBip8ErrorCounterTable.setStatus("current")
_Rm10010mpCntremoteLineSmBip8ErrorCounterEntry_Object = MibTableRow
rm10010mpCntremoteLineSmBip8ErrorCounterEntry = _Rm10010mpCntremoteLineSmBip8ErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4, 3, 194, 1)
)
rm10010mpCntremoteLineSmBip8ErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Rm10010mp-MIB", "rm10010mpCntremoteLineSmBip8ErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    rm10010mpCntremoteLineSmBip8ErrorCounterEntry.setStatus("current")


class _Rm10010mpCntremoteLineSmBip8ErrorCounterIndex_Type(Integer32):
    """Custom type rm10010mpCntremoteLineSmBip8ErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010mpCntremoteLineSmBip8ErrorCounterIndex_Type.__name__ = "Integer32"
_Rm10010mpCntremoteLineSmBip8ErrorCounterIndex_Object = MibTableColumn
rm10010mpCntremoteLineSmBip8ErrorCounterIndex = _Rm10010mpCntremoteLineSmBip8ErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4, 3, 194, 1, 1),
    _Rm10010mpCntremoteLineSmBip8ErrorCounterIndex_Type()
)
rm10010mpCntremoteLineSmBip8ErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCntremoteLineSmBip8ErrorCounterIndex.setStatus("current")
_Rm10010mpCntremoteLineSmBip8ErrorCounterValuePortn_Type = Counter64
_Rm10010mpCntremoteLineSmBip8ErrorCounterValuePortn_Object = MibTableColumn
rm10010mpCntremoteLineSmBip8ErrorCounterValuePortn = _Rm10010mpCntremoteLineSmBip8ErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4, 3, 194, 1, 2),
    _Rm10010mpCntremoteLineSmBip8ErrorCounterValuePortn_Type()
)
rm10010mpCntremoteLineSmBip8ErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCntremoteLineSmBip8ErrorCounterValuePortn.setStatus("current")
_Rm10010mpCntremoteLineSmBip8ErrorCounterErrorPortn_Type = EkiOnOff
_Rm10010mpCntremoteLineSmBip8ErrorCounterErrorPortn_Object = MibTableColumn
rm10010mpCntremoteLineSmBip8ErrorCounterErrorPortn = _Rm10010mpCntremoteLineSmBip8ErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4, 3, 194, 1, 3),
    _Rm10010mpCntremoteLineSmBip8ErrorCounterErrorPortn_Type()
)
rm10010mpCntremoteLineSmBip8ErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCntremoteLineSmBip8ErrorCounterErrorPortn.setStatus("current")
_Rm10010mpCntremoteLineSmBip8ErrorCounterOverloadPortn_Type = EkiOnOff
_Rm10010mpCntremoteLineSmBip8ErrorCounterOverloadPortn_Object = MibTableColumn
rm10010mpCntremoteLineSmBip8ErrorCounterOverloadPortn = _Rm10010mpCntremoteLineSmBip8ErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4, 3, 194, 1, 4),
    _Rm10010mpCntremoteLineSmBip8ErrorCounterOverloadPortn_Type()
)
rm10010mpCntremoteLineSmBip8ErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCntremoteLineSmBip8ErrorCounterOverloadPortn.setStatus("current")
_Rm10010mpCntlineDfrmTimCntTable_Object = MibTable
rm10010mpCntlineDfrmTimCntTable = _Rm10010mpCntlineDfrmTimCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4, 3, 195)
)
if mibBuilder.loadTexts:
    rm10010mpCntlineDfrmTimCntTable.setStatus("current")
_Rm10010mpCntlineDfrmTimCntEntry_Object = MibTableRow
rm10010mpCntlineDfrmTimCntEntry = _Rm10010mpCntlineDfrmTimCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4, 3, 195, 1)
)
rm10010mpCntlineDfrmTimCntEntry.setIndexNames(
    (0, "EKINOPS-Rm10010mp-MIB", "rm10010mpCntlineDfrmTimCntIndex"),
)
if mibBuilder.loadTexts:
    rm10010mpCntlineDfrmTimCntEntry.setStatus("current")


class _Rm10010mpCntlineDfrmTimCntIndex_Type(Integer32):
    """Custom type rm10010mpCntlineDfrmTimCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010mpCntlineDfrmTimCntIndex_Type.__name__ = "Integer32"
_Rm10010mpCntlineDfrmTimCntIndex_Object = MibTableColumn
rm10010mpCntlineDfrmTimCntIndex = _Rm10010mpCntlineDfrmTimCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4, 3, 195, 1, 1),
    _Rm10010mpCntlineDfrmTimCntIndex_Type()
)
rm10010mpCntlineDfrmTimCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCntlineDfrmTimCntIndex.setStatus("current")
_Rm10010mpCntlineDfrmTimCntValuePortn_Type = Counter64
_Rm10010mpCntlineDfrmTimCntValuePortn_Object = MibTableColumn
rm10010mpCntlineDfrmTimCntValuePortn = _Rm10010mpCntlineDfrmTimCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4, 3, 195, 1, 2),
    _Rm10010mpCntlineDfrmTimCntValuePortn_Type()
)
rm10010mpCntlineDfrmTimCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCntlineDfrmTimCntValuePortn.setStatus("current")
_Rm10010mpCntlineDfrmTimCntErrorPortn_Type = EkiOnOff
_Rm10010mpCntlineDfrmTimCntErrorPortn_Object = MibTableColumn
rm10010mpCntlineDfrmTimCntErrorPortn = _Rm10010mpCntlineDfrmTimCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4, 3, 195, 1, 3),
    _Rm10010mpCntlineDfrmTimCntErrorPortn_Type()
)
rm10010mpCntlineDfrmTimCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCntlineDfrmTimCntErrorPortn.setStatus("current")
_Rm10010mpCntlineDfrmTimCntOverloadPortn_Type = EkiOnOff
_Rm10010mpCntlineDfrmTimCntOverloadPortn_Object = MibTableColumn
rm10010mpCntlineDfrmTimCntOverloadPortn = _Rm10010mpCntlineDfrmTimCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4, 3, 195, 1, 4),
    _Rm10010mpCntlineDfrmTimCntOverloadPortn_Type()
)
rm10010mpCntlineDfrmTimCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCntlineDfrmTimCntOverloadPortn.setStatus("current")
_Rm10010mpCntlocalLineTrscvFecCorrectedErrorCounterTable_Object = MibTable
rm10010mpCntlocalLineTrscvFecCorrectedErrorCounterTable = _Rm10010mpCntlocalLineTrscvFecCorrectedErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4, 3, 196)
)
if mibBuilder.loadTexts:
    rm10010mpCntlocalLineTrscvFecCorrectedErrorCounterTable.setStatus("current")
_Rm10010mpCntlocalLineTrscvFecCorrectedErrorCounterEntry_Object = MibTableRow
rm10010mpCntlocalLineTrscvFecCorrectedErrorCounterEntry = _Rm10010mpCntlocalLineTrscvFecCorrectedErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4, 3, 196, 1)
)
rm10010mpCntlocalLineTrscvFecCorrectedErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Rm10010mp-MIB", "rm10010mpCntlocalLineTrscvFecCorrectedErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    rm10010mpCntlocalLineTrscvFecCorrectedErrorCounterEntry.setStatus("current")


class _Rm10010mpCntlocalLineTrscvFecCorrectedErrorCounterIndex_Type(Integer32):
    """Custom type rm10010mpCntlocalLineTrscvFecCorrectedErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010mpCntlocalLineTrscvFecCorrectedErrorCounterIndex_Type.__name__ = "Integer32"
_Rm10010mpCntlocalLineTrscvFecCorrectedErrorCounterIndex_Object = MibTableColumn
rm10010mpCntlocalLineTrscvFecCorrectedErrorCounterIndex = _Rm10010mpCntlocalLineTrscvFecCorrectedErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4, 3, 196, 1, 1),
    _Rm10010mpCntlocalLineTrscvFecCorrectedErrorCounterIndex_Type()
)
rm10010mpCntlocalLineTrscvFecCorrectedErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCntlocalLineTrscvFecCorrectedErrorCounterIndex.setStatus("current")
_Rm10010mpCntlocalLineTrscvFecCorrectedErrorCounterValuePortn_Type = Counter64
_Rm10010mpCntlocalLineTrscvFecCorrectedErrorCounterValuePortn_Object = MibTableColumn
rm10010mpCntlocalLineTrscvFecCorrectedErrorCounterValuePortn = _Rm10010mpCntlocalLineTrscvFecCorrectedErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4, 3, 196, 1, 2),
    _Rm10010mpCntlocalLineTrscvFecCorrectedErrorCounterValuePortn_Type()
)
rm10010mpCntlocalLineTrscvFecCorrectedErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCntlocalLineTrscvFecCorrectedErrorCounterValuePortn.setStatus("current")
_Rm10010mpCntlocalLineTrscvFecCorrectedErrorCounterErrorPortn_Type = EkiOnOff
_Rm10010mpCntlocalLineTrscvFecCorrectedErrorCounterErrorPortn_Object = MibTableColumn
rm10010mpCntlocalLineTrscvFecCorrectedErrorCounterErrorPortn = _Rm10010mpCntlocalLineTrscvFecCorrectedErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4, 3, 196, 1, 3),
    _Rm10010mpCntlocalLineTrscvFecCorrectedErrorCounterErrorPortn_Type()
)
rm10010mpCntlocalLineTrscvFecCorrectedErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCntlocalLineTrscvFecCorrectedErrorCounterErrorPortn.setStatus("current")
_Rm10010mpCntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn_Type = EkiOnOff
_Rm10010mpCntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn_Object = MibTableColumn
rm10010mpCntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn = _Rm10010mpCntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4, 3, 196, 1, 4),
    _Rm10010mpCntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn_Type()
)
rm10010mpCntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn.setStatus("current")
_Rm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterTable_Object = MibTable
rm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterTable = _Rm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4, 3, 197)
)
if mibBuilder.loadTexts:
    rm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterTable.setStatus("current")
_Rm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterEntry_Object = MibTableRow
rm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterEntry = _Rm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4, 3, 197, 1)
)
rm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Rm10010mp-MIB", "rm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    rm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterEntry.setStatus("current")


class _Rm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterIndex_Type(Integer32):
    """Custom type rm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterIndex_Type.__name__ = "Integer32"
_Rm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterIndex_Object = MibTableColumn
rm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterIndex = _Rm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4, 3, 197, 1, 1),
    _Rm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterIndex_Type()
)
rm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterIndex.setStatus("current")
_Rm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterValuePortn_Type = Counter64
_Rm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterValuePortn_Object = MibTableColumn
rm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterValuePortn = _Rm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4, 3, 197, 1, 2),
    _Rm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterValuePortn_Type()
)
rm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterValuePortn.setStatus("current")
_Rm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn_Type = EkiOnOff
_Rm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn_Object = MibTableColumn
rm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn = _Rm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4, 3, 197, 1, 3),
    _Rm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn_Type()
)
rm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn.setStatus("current")
_Rm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn_Type = EkiOnOff
_Rm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn_Object = MibTableColumn
rm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn = _Rm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 4, 3, 197, 1, 4),
    _Rm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn_Type()
)
rm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn.setStatus("current")
_Rm10010mpcontrolsWrite_ObjectIdentity = ObjectIdentity
rm10010mpcontrolsWrite = _Rm10010mpcontrolsWrite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6)
)
_Rm10010mpCtrlOther_ObjectIdentity = ObjectIdentity
rm10010mpCtrlOther = _Rm10010mpCtrlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 1)
)
_Rm10010mpCtrlconfMgnt1_ObjectIdentity = ObjectIdentity
rm10010mpCtrlconfMgnt1 = _Rm10010mpCtrlconfMgnt1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 1, 1)
)
_Rm10010mpCtrlConf1Load1_Type = EkiOnOff
_Rm10010mpCtrlConf1Load1_Object = MibScalar
rm10010mpCtrlConf1Load1 = _Rm10010mpCtrlConf1Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 1, 1, 1),
    _Rm10010mpCtrlConf1Load1_Type()
)
rm10010mpCtrlConf1Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010mpCtrlConf1Load1.setStatus("current")
_Rm10010mpCtrlConf2Load1_Type = EkiOnOff
_Rm10010mpCtrlConf2Load1_Object = MibScalar
rm10010mpCtrlConf2Load1 = _Rm10010mpCtrlConf2Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 1, 1, 2),
    _Rm10010mpCtrlConf2Load1_Type()
)
rm10010mpCtrlConf2Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010mpCtrlConf2Load1.setStatus("current")
_Rm10010mpCtrlConf2Flash1_Type = EkiOnOff
_Rm10010mpCtrlConf2Flash1_Object = MibScalar
rm10010mpCtrlConf2Flash1 = _Rm10010mpCtrlConf2Flash1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 1, 1, 10),
    _Rm10010mpCtrlConf2Flash1_Type()
)
rm10010mpCtrlConf2Flash1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010mpCtrlConf2Flash1.setStatus("current")
_Rm10010mpCtrlConf2Clear1_Type = EkiOnOff
_Rm10010mpCtrlConf2Clear1_Object = MibScalar
rm10010mpCtrlConf2Clear1 = _Rm10010mpCtrlConf2Clear1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 1, 1, 14),
    _Rm10010mpCtrlConf2Clear1_Type()
)
rm10010mpCtrlConf2Clear1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010mpCtrlConf2Clear1.setStatus("current")
_Rm10010mpCtrlsynth4_ObjectIdentity = ObjectIdentity
rm10010mpCtrlsynth4 = _Rm10010mpCtrlsynth4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 1, 4)
)
_Rm10010mpCtrlCorrelatOn_Type = EkiOnOff
_Rm10010mpCtrlCorrelatOn_Object = MibScalar
rm10010mpCtrlCorrelatOn = _Rm10010mpCtrlCorrelatOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 1, 4, 1),
    _Rm10010mpCtrlCorrelatOn_Type()
)
rm10010mpCtrlCorrelatOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010mpCtrlCorrelatOn.setStatus("current")
_Rm10010mpCtrlCorrelatOff_Type = EkiOnOff
_Rm10010mpCtrlCorrelatOff_Object = MibScalar
rm10010mpCtrlCorrelatOff = _Rm10010mpCtrlCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 1, 4, 2),
    _Rm10010mpCtrlCorrelatOff_Type()
)
rm10010mpCtrlCorrelatOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010mpCtrlCorrelatOff.setStatus("current")
_Rm10010mpCtrlswMgnt_ObjectIdentity = ObjectIdentity
rm10010mpCtrlswMgnt = _Rm10010mpCtrlswMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 1, 5)
)
_Rm10010mpCtrlColdReset_Type = EkiOnOff
_Rm10010mpCtrlColdReset_Object = MibScalar
rm10010mpCtrlColdReset = _Rm10010mpCtrlColdReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 1, 5, 2),
    _Rm10010mpCtrlColdReset_Type()
)
rm10010mpCtrlColdReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010mpCtrlColdReset.setStatus("current")
_Rm10010mpCtrlWarmReset_Type = EkiOnOff
_Rm10010mpCtrlWarmReset_Object = MibScalar
rm10010mpCtrlWarmReset = _Rm10010mpCtrlWarmReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 1, 5, 3),
    _Rm10010mpCtrlWarmReset_Type()
)
rm10010mpCtrlWarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010mpCtrlWarmReset.setStatus("current")
_Rm10010mpCtrlLoadSwBank1_Type = EkiOnOff
_Rm10010mpCtrlLoadSwBank1_Object = MibScalar
rm10010mpCtrlLoadSwBank1 = _Rm10010mpCtrlLoadSwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 1, 5, 5),
    _Rm10010mpCtrlLoadSwBank1_Type()
)
rm10010mpCtrlLoadSwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010mpCtrlLoadSwBank1.setStatus("current")
_Rm10010mpCtrlLoadSwBank2_Type = EkiOnOff
_Rm10010mpCtrlLoadSwBank2_Object = MibScalar
rm10010mpCtrlLoadSwBank2 = _Rm10010mpCtrlLoadSwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 1, 5, 6),
    _Rm10010mpCtrlLoadSwBank2_Type()
)
rm10010mpCtrlLoadSwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010mpCtrlLoadSwBank2.setStatus("current")
_Rm10010mpCtrlgwMgnt_ObjectIdentity = ObjectIdentity
rm10010mpCtrlgwMgnt = _Rm10010mpCtrlgwMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 1, 6)
)
_Rm10010mpCtrlCurrentGwReset_Type = EkiOnOff
_Rm10010mpCtrlCurrentGwReset_Object = MibScalar
rm10010mpCtrlCurrentGwReset = _Rm10010mpCtrlCurrentGwReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 1, 6, 1),
    _Rm10010mpCtrlCurrentGwReset_Type()
)
rm10010mpCtrlCurrentGwReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010mpCtrlCurrentGwReset.setStatus("current")
_Rm10010mpCtrlLoadGwBank1_Type = EkiOnOff
_Rm10010mpCtrlLoadGwBank1_Object = MibScalar
rm10010mpCtrlLoadGwBank1 = _Rm10010mpCtrlLoadGwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 1, 6, 5),
    _Rm10010mpCtrlLoadGwBank1_Type()
)
rm10010mpCtrlLoadGwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010mpCtrlLoadGwBank1.setStatus("current")
_Rm10010mpCtrlLoadGwBank2_Type = EkiOnOff
_Rm10010mpCtrlLoadGwBank2_Object = MibScalar
rm10010mpCtrlLoadGwBank2 = _Rm10010mpCtrlLoadGwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 1, 6, 6),
    _Rm10010mpCtrlLoadGwBank2_Type()
)
rm10010mpCtrlLoadGwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010mpCtrlLoadGwBank2.setStatus("current")
_Rm10010mpCtrlLoadGwBank3_Type = EkiOnOff
_Rm10010mpCtrlLoadGwBank3_Object = MibScalar
rm10010mpCtrlLoadGwBank3 = _Rm10010mpCtrlLoadGwBank3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 1, 6, 7),
    _Rm10010mpCtrlLoadGwBank3_Type()
)
rm10010mpCtrlLoadGwBank3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010mpCtrlLoadGwBank3.setStatus("current")
_Rm10010mpCtrlLoadGwBank4_Type = EkiOnOff
_Rm10010mpCtrlLoadGwBank4_Object = MibScalar
rm10010mpCtrlLoadGwBank4 = _Rm10010mpCtrlLoadGwBank4_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 1, 6, 8),
    _Rm10010mpCtrlLoadGwBank4_Type()
)
rm10010mpCtrlLoadGwBank4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010mpCtrlLoadGwBank4.setStatus("current")
_Rm10010mpCtrlledTest_ObjectIdentity = ObjectIdentity
rm10010mpCtrlledTest = _Rm10010mpCtrlledTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 1, 192)
)
_Rm10010mpCtrlGreenLed_Type = EkiOnOff
_Rm10010mpCtrlGreenLed_Object = MibScalar
rm10010mpCtrlGreenLed = _Rm10010mpCtrlGreenLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 1, 192, 1),
    _Rm10010mpCtrlGreenLed_Type()
)
rm10010mpCtrlGreenLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010mpCtrlGreenLed.setStatus("current")
_Rm10010mpCtrlRedLed_Type = EkiOnOff
_Rm10010mpCtrlRedLed_Object = MibScalar
rm10010mpCtrlRedLed = _Rm10010mpCtrlRedLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 1, 192, 2),
    _Rm10010mpCtrlRedLed_Type()
)
rm10010mpCtrlRedLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010mpCtrlRedLed.setStatus("current")
_Rm10010mpCtrlLedOff_Type = EkiOnOff
_Rm10010mpCtrlLedOff_Object = MibScalar
rm10010mpCtrlLedOff = _Rm10010mpCtrlLedOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 1, 192, 3),
    _Rm10010mpCtrlLedOff_Type()
)
rm10010mpCtrlLedOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010mpCtrlLedOff.setStatus("current")
_Rm10010mpCtrlinitSwitchMarvell_ObjectIdentity = ObjectIdentity
rm10010mpCtrlinitSwitchMarvell = _Rm10010mpCtrlinitSwitchMarvell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 1, 201)
)
_Rm10010mpCtrlInitSwitchMarvell_Type = EkiOnOff
_Rm10010mpCtrlInitSwitchMarvell_Object = MibScalar
rm10010mpCtrlInitSwitchMarvell = _Rm10010mpCtrlInitSwitchMarvell_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 1, 201, 1),
    _Rm10010mpCtrlInitSwitchMarvell_Type()
)
rm10010mpCtrlInitSwitchMarvell.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010mpCtrlInitSwitchMarvell.setStatus("current")
_Rm10010mpCtrlresetCount_ObjectIdentity = ObjectIdentity
rm10010mpCtrlresetCount = _Rm10010mpCtrlresetCount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 1, 259)
)
_Rm10010mpCtrlResetcount_Type = EkiOnOff
_Rm10010mpCtrlResetcount_Object = MibScalar
rm10010mpCtrlResetcount = _Rm10010mpCtrlResetcount_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 1, 259, 1),
    _Rm10010mpCtrlResetcount_Type()
)
rm10010mpCtrlResetcount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010mpCtrlResetcount.setStatus("current")
_Rm10010mpCtrlresetRmon_ObjectIdentity = ObjectIdentity
rm10010mpCtrlresetRmon = _Rm10010mpCtrlresetRmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 1, 260)
)
_Rm10010mpCtrlResetrmon_Type = EkiOnOff
_Rm10010mpCtrlResetrmon_Object = MibScalar
rm10010mpCtrlResetrmon = _Rm10010mpCtrlResetrmon_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 1, 260, 1),
    _Rm10010mpCtrlResetrmon_Type()
)
rm10010mpCtrlResetrmon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010mpCtrlResetrmon.setStatus("current")
_Rm10010mpCtrlresetMeasurements_ObjectIdentity = ObjectIdentity
rm10010mpCtrlresetMeasurements = _Rm10010mpCtrlresetMeasurements_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 1, 261)
)
_Rm10010mpCtrlResetmeasurements_Type = EkiOnOff
_Rm10010mpCtrlResetmeasurements_Object = MibScalar
rm10010mpCtrlResetmeasurements = _Rm10010mpCtrlResetmeasurements_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 1, 261, 1),
    _Rm10010mpCtrlResetmeasurements_Type()
)
rm10010mpCtrlResetmeasurements.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010mpCtrlResetmeasurements.setStatus("current")
_Rm10010mpCtrlClient_ObjectIdentity = ObjectIdentity
rm10010mpCtrlClient = _Rm10010mpCtrlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 2)
)
_Rm10010mpCtrlaccessLoopTable_Object = MibTable
rm10010mpCtrlaccessLoopTable = _Rm10010mpCtrlaccessLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 2, 16)
)
if mibBuilder.loadTexts:
    rm10010mpCtrlaccessLoopTable.setStatus("current")
_Rm10010mpCtrlaccessLoopEntry_Object = MibTableRow
rm10010mpCtrlaccessLoopEntry = _Rm10010mpCtrlaccessLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 2, 16, 1)
)
rm10010mpCtrlaccessLoopEntry.setIndexNames(
    (0, "EKINOPS-Rm10010mp-MIB", "rm10010mpCtrlaccessLoopIndex"),
)
if mibBuilder.loadTexts:
    rm10010mpCtrlaccessLoopEntry.setStatus("current")


class _Rm10010mpCtrlaccessLoopIndex_Type(Integer32):
    """Custom type rm10010mpCtrlaccessLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010mpCtrlaccessLoopIndex_Type.__name__ = "Integer32"
_Rm10010mpCtrlaccessLoopIndex_Object = MibTableColumn
rm10010mpCtrlaccessLoopIndex = _Rm10010mpCtrlaccessLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 2, 16, 1, 1),
    _Rm10010mpCtrlaccessLoopIndex_Type()
)
rm10010mpCtrlaccessLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCtrlaccessLoopIndex.setStatus("current")
_Rm10010mpCtrlaccessLoopPortn_Type = EkiState
_Rm10010mpCtrlaccessLoopPortn_Object = MibTableColumn
rm10010mpCtrlaccessLoopPortn = _Rm10010mpCtrlaccessLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 2, 16, 1, 2),
    _Rm10010mpCtrlaccessLoopPortn_Type()
)
rm10010mpCtrlaccessLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010mpCtrlaccessLoopPortn.setStatus("current")
_Rm10010mpCtrlclientLoopToLineTable_Object = MibTable
rm10010mpCtrlclientLoopToLineTable = _Rm10010mpCtrlclientLoopToLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 2, 17)
)
if mibBuilder.loadTexts:
    rm10010mpCtrlclientLoopToLineTable.setStatus("current")
_Rm10010mpCtrlclientLoopToLineEntry_Object = MibTableRow
rm10010mpCtrlclientLoopToLineEntry = _Rm10010mpCtrlclientLoopToLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 2, 17, 1)
)
rm10010mpCtrlclientLoopToLineEntry.setIndexNames(
    (0, "EKINOPS-Rm10010mp-MIB", "rm10010mpCtrlclientLoopToLineIndex"),
)
if mibBuilder.loadTexts:
    rm10010mpCtrlclientLoopToLineEntry.setStatus("current")


class _Rm10010mpCtrlclientLoopToLineIndex_Type(Integer32):
    """Custom type rm10010mpCtrlclientLoopToLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010mpCtrlclientLoopToLineIndex_Type.__name__ = "Integer32"
_Rm10010mpCtrlclientLoopToLineIndex_Object = MibTableColumn
rm10010mpCtrlclientLoopToLineIndex = _Rm10010mpCtrlclientLoopToLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 2, 17, 1, 1),
    _Rm10010mpCtrlclientLoopToLineIndex_Type()
)
rm10010mpCtrlclientLoopToLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCtrlclientLoopToLineIndex.setStatus("current")
_Rm10010mpCtrlclientLoopToLinePortn_Type = EkiState
_Rm10010mpCtrlclientLoopToLinePortn_Object = MibTableColumn
rm10010mpCtrlclientLoopToLinePortn = _Rm10010mpCtrlclientLoopToLinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 2, 17, 1, 2),
    _Rm10010mpCtrlclientLoopToLinePortn_Type()
)
rm10010mpCtrlclientLoopToLinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010mpCtrlclientLoopToLinePortn.setStatus("current")
_Rm10010mpCtrlcsfUpInsTable_Object = MibTable
rm10010mpCtrlcsfUpInsTable = _Rm10010mpCtrlcsfUpInsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 2, 21)
)
if mibBuilder.loadTexts:
    rm10010mpCtrlcsfUpInsTable.setStatus("current")
_Rm10010mpCtrlcsfUpInsEntry_Object = MibTableRow
rm10010mpCtrlcsfUpInsEntry = _Rm10010mpCtrlcsfUpInsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 2, 21, 1)
)
rm10010mpCtrlcsfUpInsEntry.setIndexNames(
    (0, "EKINOPS-Rm10010mp-MIB", "rm10010mpCtrlcsfUpInsIndex"),
)
if mibBuilder.loadTexts:
    rm10010mpCtrlcsfUpInsEntry.setStatus("current")


class _Rm10010mpCtrlcsfUpInsIndex_Type(Integer32):
    """Custom type rm10010mpCtrlcsfUpInsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010mpCtrlcsfUpInsIndex_Type.__name__ = "Integer32"
_Rm10010mpCtrlcsfUpInsIndex_Object = MibTableColumn
rm10010mpCtrlcsfUpInsIndex = _Rm10010mpCtrlcsfUpInsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 2, 21, 1, 1),
    _Rm10010mpCtrlcsfUpInsIndex_Type()
)
rm10010mpCtrlcsfUpInsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCtrlcsfUpInsIndex.setStatus("current")
_Rm10010mpCtrlcsfUpInsPortn_Type = EkiState
_Rm10010mpCtrlcsfUpInsPortn_Object = MibTableColumn
rm10010mpCtrlcsfUpInsPortn = _Rm10010mpCtrlcsfUpInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 2, 21, 1, 2),
    _Rm10010mpCtrlcsfUpInsPortn_Type()
)
rm10010mpCtrlcsfUpInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010mpCtrlcsfUpInsPortn.setStatus("current")
_Rm10010mpCtrlcaisDwInsTable_Object = MibTable
rm10010mpCtrlcaisDwInsTable = _Rm10010mpCtrlcaisDwInsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 2, 22)
)
if mibBuilder.loadTexts:
    rm10010mpCtrlcaisDwInsTable.setStatus("current")
_Rm10010mpCtrlcaisDwInsEntry_Object = MibTableRow
rm10010mpCtrlcaisDwInsEntry = _Rm10010mpCtrlcaisDwInsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 2, 22, 1)
)
rm10010mpCtrlcaisDwInsEntry.setIndexNames(
    (0, "EKINOPS-Rm10010mp-MIB", "rm10010mpCtrlcaisDwInsIndex"),
)
if mibBuilder.loadTexts:
    rm10010mpCtrlcaisDwInsEntry.setStatus("current")


class _Rm10010mpCtrlcaisDwInsIndex_Type(Integer32):
    """Custom type rm10010mpCtrlcaisDwInsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010mpCtrlcaisDwInsIndex_Type.__name__ = "Integer32"
_Rm10010mpCtrlcaisDwInsIndex_Object = MibTableColumn
rm10010mpCtrlcaisDwInsIndex = _Rm10010mpCtrlcaisDwInsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 2, 22, 1, 1),
    _Rm10010mpCtrlcaisDwInsIndex_Type()
)
rm10010mpCtrlcaisDwInsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCtrlcaisDwInsIndex.setStatus("current")
_Rm10010mpCtrlcaisDwInsPortn_Type = EkiState
_Rm10010mpCtrlcaisDwInsPortn_Object = MibTableColumn
rm10010mpCtrlcaisDwInsPortn = _Rm10010mpCtrlcaisDwInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 2, 22, 1, 2),
    _Rm10010mpCtrlcaisDwInsPortn_Type()
)
rm10010mpCtrlcaisDwInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010mpCtrlcaisDwInsPortn.setStatus("current")
_Rm10010mpCtrlLine_ObjectIdentity = ObjectIdentity
rm10010mpCtrlLine = _Rm10010mpCtrlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 3)
)
_Rm10010mpCtrlcommAccessLoopTable_Object = MibTable
rm10010mpCtrlcommAccessLoopTable = _Rm10010mpCtrlcommAccessLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 3, 64)
)
if mibBuilder.loadTexts:
    rm10010mpCtrlcommAccessLoopTable.setStatus("current")
_Rm10010mpCtrlcommAccessLoopEntry_Object = MibTableRow
rm10010mpCtrlcommAccessLoopEntry = _Rm10010mpCtrlcommAccessLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 3, 64, 1)
)
rm10010mpCtrlcommAccessLoopEntry.setIndexNames(
    (0, "EKINOPS-Rm10010mp-MIB", "rm10010mpCtrlcommAccessLoopIndex"),
)
if mibBuilder.loadTexts:
    rm10010mpCtrlcommAccessLoopEntry.setStatus("current")


class _Rm10010mpCtrlcommAccessLoopIndex_Type(Integer32):
    """Custom type rm10010mpCtrlcommAccessLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010mpCtrlcommAccessLoopIndex_Type.__name__ = "Integer32"
_Rm10010mpCtrlcommAccessLoopIndex_Object = MibTableColumn
rm10010mpCtrlcommAccessLoopIndex = _Rm10010mpCtrlcommAccessLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 3, 64, 1, 1),
    _Rm10010mpCtrlcommAccessLoopIndex_Type()
)
rm10010mpCtrlcommAccessLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCtrlcommAccessLoopIndex.setStatus("current")
_Rm10010mpCtrlcommAccessLoopPortn_Type = EkiState
_Rm10010mpCtrlcommAccessLoopPortn_Object = MibTableColumn
rm10010mpCtrlcommAccessLoopPortn = _Rm10010mpCtrlcommAccessLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 3, 64, 1, 2),
    _Rm10010mpCtrlcommAccessLoopPortn_Type()
)
rm10010mpCtrlcommAccessLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010mpCtrlcommAccessLoopPortn.setStatus("current")
_Rm10010mpCtrllineLoopTable_Object = MibTable
rm10010mpCtrllineLoopTable = _Rm10010mpCtrllineLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 3, 66)
)
if mibBuilder.loadTexts:
    rm10010mpCtrllineLoopTable.setStatus("current")
_Rm10010mpCtrllineLoopEntry_Object = MibTableRow
rm10010mpCtrllineLoopEntry = _Rm10010mpCtrllineLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 3, 66, 1)
)
rm10010mpCtrllineLoopEntry.setIndexNames(
    (0, "EKINOPS-Rm10010mp-MIB", "rm10010mpCtrllineLoopIndex"),
)
if mibBuilder.loadTexts:
    rm10010mpCtrllineLoopEntry.setStatus("current")


class _Rm10010mpCtrllineLoopIndex_Type(Integer32):
    """Custom type rm10010mpCtrllineLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010mpCtrllineLoopIndex_Type.__name__ = "Integer32"
_Rm10010mpCtrllineLoopIndex_Object = MibTableColumn
rm10010mpCtrllineLoopIndex = _Rm10010mpCtrllineLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 3, 66, 1, 1),
    _Rm10010mpCtrllineLoopIndex_Type()
)
rm10010mpCtrllineLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCtrllineLoopIndex.setStatus("current")
_Rm10010mpCtrllineLoopPortn_Type = EkiState
_Rm10010mpCtrllineLoopPortn_Object = MibTableColumn
rm10010mpCtrllineLoopPortn = _Rm10010mpCtrllineLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 3, 66, 1, 2),
    _Rm10010mpCtrllineLoopPortn_Type()
)
rm10010mpCtrllineLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010mpCtrllineLoopPortn.setStatus("current")
_Rm10010mpCtrlfecDisableTable_Object = MibTable
rm10010mpCtrlfecDisableTable = _Rm10010mpCtrlfecDisableTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 3, 69)
)
if mibBuilder.loadTexts:
    rm10010mpCtrlfecDisableTable.setStatus("current")
_Rm10010mpCtrlfecDisableEntry_Object = MibTableRow
rm10010mpCtrlfecDisableEntry = _Rm10010mpCtrlfecDisableEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 3, 69, 1)
)
rm10010mpCtrlfecDisableEntry.setIndexNames(
    (0, "EKINOPS-Rm10010mp-MIB", "rm10010mpCtrlfecDisableIndex"),
)
if mibBuilder.loadTexts:
    rm10010mpCtrlfecDisableEntry.setStatus("current")


class _Rm10010mpCtrlfecDisableIndex_Type(Integer32):
    """Custom type rm10010mpCtrlfecDisableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010mpCtrlfecDisableIndex_Type.__name__ = "Integer32"
_Rm10010mpCtrlfecDisableIndex_Object = MibTableColumn
rm10010mpCtrlfecDisableIndex = _Rm10010mpCtrlfecDisableIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 3, 69, 1, 1),
    _Rm10010mpCtrlfecDisableIndex_Type()
)
rm10010mpCtrlfecDisableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCtrlfecDisableIndex.setStatus("current")
_Rm10010mpCtrlfecDisablePortn_Type = EkiState
_Rm10010mpCtrlfecDisablePortn_Object = MibTableColumn
rm10010mpCtrlfecDisablePortn = _Rm10010mpCtrlfecDisablePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 3, 69, 1, 2),
    _Rm10010mpCtrlfecDisablePortn_Type()
)
rm10010mpCtrlfecDisablePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010mpCtrlfecDisablePortn.setStatus("current")
_Rm10010mpCtrlmsaLineLoopTable_Object = MibTable
rm10010mpCtrlmsaLineLoopTable = _Rm10010mpCtrlmsaLineLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 3, 209)
)
if mibBuilder.loadTexts:
    rm10010mpCtrlmsaLineLoopTable.setStatus("current")
_Rm10010mpCtrlmsaLineLoopEntry_Object = MibTableRow
rm10010mpCtrlmsaLineLoopEntry = _Rm10010mpCtrlmsaLineLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 3, 209, 1)
)
rm10010mpCtrlmsaLineLoopEntry.setIndexNames(
    (0, "EKINOPS-Rm10010mp-MIB", "rm10010mpCtrlmsaLineLoopIndex"),
)
if mibBuilder.loadTexts:
    rm10010mpCtrlmsaLineLoopEntry.setStatus("current")


class _Rm10010mpCtrlmsaLineLoopIndex_Type(Integer32):
    """Custom type rm10010mpCtrlmsaLineLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010mpCtrlmsaLineLoopIndex_Type.__name__ = "Integer32"
_Rm10010mpCtrlmsaLineLoopIndex_Object = MibTableColumn
rm10010mpCtrlmsaLineLoopIndex = _Rm10010mpCtrlmsaLineLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 3, 209, 1, 1),
    _Rm10010mpCtrlmsaLineLoopIndex_Type()
)
rm10010mpCtrlmsaLineLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCtrlmsaLineLoopIndex.setStatus("current")
_Rm10010mpCtrlmsaLineLoopPortn_Type = EkiState
_Rm10010mpCtrlmsaLineLoopPortn_Object = MibTableColumn
rm10010mpCtrlmsaLineLoopPortn = _Rm10010mpCtrlmsaLineLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 3, 209, 1, 2),
    _Rm10010mpCtrlmsaLineLoopPortn_Type()
)
rm10010mpCtrlmsaLineLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010mpCtrlmsaLineLoopPortn.setStatus("current")
_Rm10010mpCtrlmsaTxResetTable_Object = MibTable
rm10010mpCtrlmsaTxResetTable = _Rm10010mpCtrlmsaTxResetTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 3, 210)
)
if mibBuilder.loadTexts:
    rm10010mpCtrlmsaTxResetTable.setStatus("current")
_Rm10010mpCtrlmsaTxResetEntry_Object = MibTableRow
rm10010mpCtrlmsaTxResetEntry = _Rm10010mpCtrlmsaTxResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 3, 210, 1)
)
rm10010mpCtrlmsaTxResetEntry.setIndexNames(
    (0, "EKINOPS-Rm10010mp-MIB", "rm10010mpCtrlmsaTxResetIndex"),
)
if mibBuilder.loadTexts:
    rm10010mpCtrlmsaTxResetEntry.setStatus("current")


class _Rm10010mpCtrlmsaTxResetIndex_Type(Integer32):
    """Custom type rm10010mpCtrlmsaTxResetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010mpCtrlmsaTxResetIndex_Type.__name__ = "Integer32"
_Rm10010mpCtrlmsaTxResetIndex_Object = MibTableColumn
rm10010mpCtrlmsaTxResetIndex = _Rm10010mpCtrlmsaTxResetIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 3, 210, 1, 1),
    _Rm10010mpCtrlmsaTxResetIndex_Type()
)
rm10010mpCtrlmsaTxResetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCtrlmsaTxResetIndex.setStatus("current")
_Rm10010mpCtrlmsaTxResetPortn_Type = EkiState
_Rm10010mpCtrlmsaTxResetPortn_Object = MibTableColumn
rm10010mpCtrlmsaTxResetPortn = _Rm10010mpCtrlmsaTxResetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 3, 210, 1, 2),
    _Rm10010mpCtrlmsaTxResetPortn_Type()
)
rm10010mpCtrlmsaTxResetPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010mpCtrlmsaTxResetPortn.setStatus("current")
_Rm10010mpCtrlmsaRxResetTable_Object = MibTable
rm10010mpCtrlmsaRxResetTable = _Rm10010mpCtrlmsaRxResetTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 3, 211)
)
if mibBuilder.loadTexts:
    rm10010mpCtrlmsaRxResetTable.setStatus("current")
_Rm10010mpCtrlmsaRxResetEntry_Object = MibTableRow
rm10010mpCtrlmsaRxResetEntry = _Rm10010mpCtrlmsaRxResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 3, 211, 1)
)
rm10010mpCtrlmsaRxResetEntry.setIndexNames(
    (0, "EKINOPS-Rm10010mp-MIB", "rm10010mpCtrlmsaRxResetIndex"),
)
if mibBuilder.loadTexts:
    rm10010mpCtrlmsaRxResetEntry.setStatus("current")


class _Rm10010mpCtrlmsaRxResetIndex_Type(Integer32):
    """Custom type rm10010mpCtrlmsaRxResetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010mpCtrlmsaRxResetIndex_Type.__name__ = "Integer32"
_Rm10010mpCtrlmsaRxResetIndex_Object = MibTableColumn
rm10010mpCtrlmsaRxResetIndex = _Rm10010mpCtrlmsaRxResetIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 3, 211, 1, 1),
    _Rm10010mpCtrlmsaRxResetIndex_Type()
)
rm10010mpCtrlmsaRxResetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCtrlmsaRxResetIndex.setStatus("current")
_Rm10010mpCtrlmsaRxResetPortn_Type = EkiState
_Rm10010mpCtrlmsaRxResetPortn_Object = MibTableColumn
rm10010mpCtrlmsaRxResetPortn = _Rm10010mpCtrlmsaRxResetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 3, 211, 1, 2),
    _Rm10010mpCtrlmsaRxResetPortn_Type()
)
rm10010mpCtrlmsaRxResetPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010mpCtrlmsaRxResetPortn.setStatus("current")
_Rm10010mpCtrlmsaShutdownTable_Object = MibTable
rm10010mpCtrlmsaShutdownTable = _Rm10010mpCtrlmsaShutdownTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 3, 212)
)
if mibBuilder.loadTexts:
    rm10010mpCtrlmsaShutdownTable.setStatus("current")
_Rm10010mpCtrlmsaShutdownEntry_Object = MibTableRow
rm10010mpCtrlmsaShutdownEntry = _Rm10010mpCtrlmsaShutdownEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 3, 212, 1)
)
rm10010mpCtrlmsaShutdownEntry.setIndexNames(
    (0, "EKINOPS-Rm10010mp-MIB", "rm10010mpCtrlmsaShutdownIndex"),
)
if mibBuilder.loadTexts:
    rm10010mpCtrlmsaShutdownEntry.setStatus("current")


class _Rm10010mpCtrlmsaShutdownIndex_Type(Integer32):
    """Custom type rm10010mpCtrlmsaShutdownIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010mpCtrlmsaShutdownIndex_Type.__name__ = "Integer32"
_Rm10010mpCtrlmsaShutdownIndex_Object = MibTableColumn
rm10010mpCtrlmsaShutdownIndex = _Rm10010mpCtrlmsaShutdownIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 3, 212, 1, 1),
    _Rm10010mpCtrlmsaShutdownIndex_Type()
)
rm10010mpCtrlmsaShutdownIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCtrlmsaShutdownIndex.setStatus("current")
_Rm10010mpCtrlmsaShutdownPortn_Type = EkiState
_Rm10010mpCtrlmsaShutdownPortn_Object = MibTableColumn
rm10010mpCtrlmsaShutdownPortn = _Rm10010mpCtrlmsaShutdownPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 6, 3, 212, 1, 2),
    _Rm10010mpCtrlmsaShutdownPortn_Type()
)
rm10010mpCtrlmsaShutdownPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010mpCtrlmsaShutdownPortn.setStatus("current")
_Rm10010mpri_ObjectIdentity = ObjectIdentity
rm10010mpri = _Rm10010mpri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 7)
)
_Rm10010mpriTable_ObjectIdentity = ObjectIdentity
rm10010mpriTable = _Rm10010mpriTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 7, 1)
)
_Rm10010mpRinvSfpTable_Object = MibTable
rm10010mpRinvSfpTable = _Rm10010mpRinvSfpTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 7, 1, 1)
)
if mibBuilder.loadTexts:
    rm10010mpRinvSfpTable.setStatus("current")
_Rm10010mpRinvSfpEntry_Object = MibTableRow
rm10010mpRinvSfpEntry = _Rm10010mpRinvSfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 7, 1, 1, 1)
)
rm10010mpRinvSfpEntry.setIndexNames(
    (0, "EKINOPS-Rm10010mp-MIB", "rm10010mpRinvSfpIndex"),
)
if mibBuilder.loadTexts:
    rm10010mpRinvSfpEntry.setStatus("current")


class _Rm10010mpRinvSfpIndex_Type(Integer32):
    """Custom type rm10010mpRinvSfpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Rm10010mpRinvSfpIndex_Type.__name__ = "Integer32"
_Rm10010mpRinvSfpIndex_Object = MibTableColumn
rm10010mpRinvSfpIndex = _Rm10010mpRinvSfpIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 7, 1, 1, 1, 1),
    _Rm10010mpRinvSfpIndex_Type()
)
rm10010mpRinvSfpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpRinvSfpIndex.setStatus("current")
_Rm10010mpRinvsfp_Type = DisplayString
_Rm10010mpRinvsfp_Object = MibTableColumn
rm10010mpRinvsfp = _Rm10010mpRinvsfp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 7, 1, 1, 1, 2),
    _Rm10010mpRinvsfp_Type()
)
rm10010mpRinvsfp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpRinvsfp.setStatus("current")
_Rm10010mpRinvLineTable_Object = MibTable
rm10010mpRinvLineTable = _Rm10010mpRinvLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 7, 1, 2)
)
if mibBuilder.loadTexts:
    rm10010mpRinvLineTable.setStatus("current")
_Rm10010mpRinvLineEntry_Object = MibTableRow
rm10010mpRinvLineEntry = _Rm10010mpRinvLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 7, 1, 2, 1)
)
rm10010mpRinvLineEntry.setIndexNames(
    (0, "EKINOPS-Rm10010mp-MIB", "rm10010mpRinvLineIndex"),
)
if mibBuilder.loadTexts:
    rm10010mpRinvLineEntry.setStatus("current")


class _Rm10010mpRinvLineIndex_Type(Integer32):
    """Custom type rm10010mpRinvLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Rm10010mpRinvLineIndex_Type.__name__ = "Integer32"
_Rm10010mpRinvLineIndex_Object = MibTableColumn
rm10010mpRinvLineIndex = _Rm10010mpRinvLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 7, 1, 2, 1, 1),
    _Rm10010mpRinvLineIndex_Type()
)
rm10010mpRinvLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpRinvLineIndex.setStatus("current")
_Rm10010mpRinvxfpLine_Type = DisplayString
_Rm10010mpRinvxfpLine_Object = MibTableColumn
rm10010mpRinvxfpLine = _Rm10010mpRinvxfpLine_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 7, 1, 2, 1, 2),
    _Rm10010mpRinvxfpLine_Type()
)
rm10010mpRinvxfpLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpRinvxfpLine.setStatus("current")
_Rm10010mpRinvReloadInventory_Type = EkiOnOff
_Rm10010mpRinvReloadInventory_Object = MibScalar
rm10010mpRinvReloadInventory = _Rm10010mpRinvReloadInventory_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 7, 2),
    _Rm10010mpRinvReloadInventory_Type()
)
rm10010mpRinvReloadInventory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010mpRinvReloadInventory.setStatus("current")
_Rm10010mpRinvHwPlatform_Type = DisplayString
_Rm10010mpRinvHwPlatform_Object = MibScalar
rm10010mpRinvHwPlatform = _Rm10010mpRinvHwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 7, 3),
    _Rm10010mpRinvHwPlatform_Type()
)
rm10010mpRinvHwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpRinvHwPlatform.setStatus("current")
_Rm10010mpRinvModulePlatform_Type = DisplayString
_Rm10010mpRinvModulePlatform_Object = MibScalar
rm10010mpRinvModulePlatform = _Rm10010mpRinvModulePlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 7, 4),
    _Rm10010mpRinvModulePlatform_Type()
)
rm10010mpRinvModulePlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpRinvModulePlatform.setStatus("current")
_Rm10010mpRinvSwPlatform_Type = DisplayString
_Rm10010mpRinvSwPlatform_Object = MibScalar
rm10010mpRinvSwPlatform = _Rm10010mpRinvSwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 7, 5),
    _Rm10010mpRinvSwPlatform_Type()
)
rm10010mpRinvSwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpRinvSwPlatform.setStatus("current")
_Rm10010mpRinvGwPlatform_Type = DisplayString
_Rm10010mpRinvGwPlatform_Object = MibScalar
rm10010mpRinvGwPlatform = _Rm10010mpRinvGwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 7, 6),
    _Rm10010mpRinvGwPlatform_Type()
)
rm10010mpRinvGwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpRinvGwPlatform.setStatus("current")
_Rm10010mpdownload_ObjectIdentity = ObjectIdentity
rm10010mpdownload = _Rm10010mpdownload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 8)
)
_Rm10010mpDwlOther_ObjectIdentity = ObjectIdentity
rm10010mpDwlOther = _Rm10010mpDwlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 8, 1)
)
_Rm10010mpDwlrestartProcess_ObjectIdentity = ObjectIdentity
rm10010mpDwlrestartProcess = _Rm10010mpDwlrestartProcess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 8, 1, 0)
)
_Rm10010mpDwlWarmRestartProcessed_Type = EkiOnOff
_Rm10010mpDwlWarmRestartProcessed_Object = MibScalar
rm10010mpDwlWarmRestartProcessed = _Rm10010mpDwlWarmRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 8, 1, 0, 1),
    _Rm10010mpDwlWarmRestartProcessed_Type()
)
rm10010mpDwlWarmRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpDwlWarmRestartProcessed.setStatus("current")
_Rm10010mpDwlColdRestartProcessed_Type = EkiOnOff
_Rm10010mpDwlColdRestartProcessed_Object = MibScalar
rm10010mpDwlColdRestartProcessed = _Rm10010mpDwlColdRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 8, 1, 0, 2),
    _Rm10010mpDwlColdRestartProcessed_Type()
)
rm10010mpDwlColdRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpDwlColdRestartProcessed.setStatus("current")
_Rm10010mpDwlswBanksUsed_ObjectIdentity = ObjectIdentity
rm10010mpDwlswBanksUsed = _Rm10010mpDwlswBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 8, 1, 1)
)
_Rm10010mpDwlSwBank1Used_Type = EkiOnOff
_Rm10010mpDwlSwBank1Used_Object = MibScalar
rm10010mpDwlSwBank1Used = _Rm10010mpDwlSwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 8, 1, 1, 1),
    _Rm10010mpDwlSwBank1Used_Type()
)
rm10010mpDwlSwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpDwlSwBank1Used.setStatus("current")
_Rm10010mpDwlSwBank2Used_Type = EkiOnOff
_Rm10010mpDwlSwBank2Used_Object = MibScalar
rm10010mpDwlSwBank2Used = _Rm10010mpDwlSwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 8, 1, 1, 2),
    _Rm10010mpDwlSwBank2Used_Type()
)
rm10010mpDwlSwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpDwlSwBank2Used.setStatus("current")
_Rm10010mpDwlSwBank1Notempty_Type = EkiOnOff
_Rm10010mpDwlSwBank1Notempty_Object = MibScalar
rm10010mpDwlSwBank1Notempty = _Rm10010mpDwlSwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 8, 1, 1, 5),
    _Rm10010mpDwlSwBank1Notempty_Type()
)
rm10010mpDwlSwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpDwlSwBank1Notempty.setStatus("current")
_Rm10010mpDwlSwBank2Notempty_Type = EkiOnOff
_Rm10010mpDwlSwBank2Notempty_Object = MibScalar
rm10010mpDwlSwBank2Notempty = _Rm10010mpDwlSwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 8, 1, 1, 6),
    _Rm10010mpDwlSwBank2Notempty_Type()
)
rm10010mpDwlSwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpDwlSwBank2Notempty.setStatus("current")
_Rm10010mpDwlgwBanksUsed_ObjectIdentity = ObjectIdentity
rm10010mpDwlgwBanksUsed = _Rm10010mpDwlgwBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 8, 1, 2)
)
_Rm10010mpDwlGwBank1Used_Type = EkiOnOff
_Rm10010mpDwlGwBank1Used_Object = MibScalar
rm10010mpDwlGwBank1Used = _Rm10010mpDwlGwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 8, 1, 2, 1),
    _Rm10010mpDwlGwBank1Used_Type()
)
rm10010mpDwlGwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpDwlGwBank1Used.setStatus("current")
_Rm10010mpDwlGwBank2Used_Type = EkiOnOff
_Rm10010mpDwlGwBank2Used_Object = MibScalar
rm10010mpDwlGwBank2Used = _Rm10010mpDwlGwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 8, 1, 2, 2),
    _Rm10010mpDwlGwBank2Used_Type()
)
rm10010mpDwlGwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpDwlGwBank2Used.setStatus("current")
_Rm10010mpDwlGwBank3Used_Type = EkiOnOff
_Rm10010mpDwlGwBank3Used_Object = MibScalar
rm10010mpDwlGwBank3Used = _Rm10010mpDwlGwBank3Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 8, 1, 2, 3),
    _Rm10010mpDwlGwBank3Used_Type()
)
rm10010mpDwlGwBank3Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpDwlGwBank3Used.setStatus("current")
_Rm10010mpDwlGwBank4Used_Type = EkiOnOff
_Rm10010mpDwlGwBank4Used_Object = MibScalar
rm10010mpDwlGwBank4Used = _Rm10010mpDwlGwBank4Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 8, 1, 2, 4),
    _Rm10010mpDwlGwBank4Used_Type()
)
rm10010mpDwlGwBank4Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpDwlGwBank4Used.setStatus("current")
_Rm10010mpDwlGwBank1Notempty_Type = EkiOnOff
_Rm10010mpDwlGwBank1Notempty_Object = MibScalar
rm10010mpDwlGwBank1Notempty = _Rm10010mpDwlGwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 8, 1, 2, 5),
    _Rm10010mpDwlGwBank1Notempty_Type()
)
rm10010mpDwlGwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpDwlGwBank1Notempty.setStatus("current")
_Rm10010mpDwlGwBank2Notempty_Type = EkiOnOff
_Rm10010mpDwlGwBank2Notempty_Object = MibScalar
rm10010mpDwlGwBank2Notempty = _Rm10010mpDwlGwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 8, 1, 2, 6),
    _Rm10010mpDwlGwBank2Notempty_Type()
)
rm10010mpDwlGwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpDwlGwBank2Notempty.setStatus("current")
_Rm10010mpDwlGwBank3Notempty_Type = EkiOnOff
_Rm10010mpDwlGwBank3Notempty_Object = MibScalar
rm10010mpDwlGwBank3Notempty = _Rm10010mpDwlGwBank3Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 8, 1, 2, 7),
    _Rm10010mpDwlGwBank3Notempty_Type()
)
rm10010mpDwlGwBank3Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpDwlGwBank3Notempty.setStatus("current")
_Rm10010mpDwlGwBank4Notempty_Type = EkiOnOff
_Rm10010mpDwlGwBank4Notempty_Object = MibScalar
rm10010mpDwlGwBank4Notempty = _Rm10010mpDwlGwBank4Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 8, 1, 2, 8),
    _Rm10010mpDwlGwBank4Notempty_Type()
)
rm10010mpDwlGwBank4Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpDwlGwBank4Notempty.setStatus("current")
_Rm10010mpDwlClient_ObjectIdentity = ObjectIdentity
rm10010mpDwlClient = _Rm10010mpDwlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 8, 2)
)
_Rm10010mpDwlLine_ObjectIdentity = ObjectIdentity
rm10010mpDwlLine = _Rm10010mpDwlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 8, 3)
)
_Rm10010mpConfig_ObjectIdentity = ObjectIdentity
rm10010mpConfig = _Rm10010mpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 9)
)
_Rm10010mpCfgAccessCAisCsf_ObjectIdentity = ObjectIdentity
rm10010mpCfgAccessCAisCsf = _Rm10010mpCfgAccessCAisCsf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 9, 1)
)
_Rm10010mpCfgClientcaiscsfTable_Object = MibTable
rm10010mpCfgClientcaiscsfTable = _Rm10010mpCfgClientcaiscsfTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 9, 1, 1)
)
if mibBuilder.loadTexts:
    rm10010mpCfgClientcaiscsfTable.setStatus("current")
_Rm10010mpCfgClientcaiscsfEntry_Object = MibTableRow
rm10010mpCfgClientcaiscsfEntry = _Rm10010mpCfgClientcaiscsfEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 9, 1, 1, 1)
)
rm10010mpCfgClientcaiscsfEntry.setIndexNames(
    (0, "EKINOPS-Rm10010mp-MIB", "rm10010mpCfgClientcaiscsfIndex"),
)
if mibBuilder.loadTexts:
    rm10010mpCfgClientcaiscsfEntry.setStatus("current")


class _Rm10010mpCfgClientcaiscsfIndex_Type(Integer32):
    """Custom type rm10010mpCfgClientcaiscsfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010mpCfgClientcaiscsfIndex_Type.__name__ = "Integer32"
_Rm10010mpCfgClientcaiscsfIndex_Object = MibTableColumn
rm10010mpCfgClientcaiscsfIndex = _Rm10010mpCfgClientcaiscsfIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 9, 1, 1, 1, 1),
    _Rm10010mpCfgClientcaiscsfIndex_Type()
)
rm10010mpCfgClientcaiscsfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCfgClientcaiscsfIndex.setStatus("current")


class _Rm10010mpCfgReservePortn_Type(Unsigned32):
    """Custom type rm10010mpCfgReservePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010mpCfgReservePortn_Type.__name__ = "Unsigned32"
_Rm10010mpCfgReservePortn_Object = MibTableColumn
rm10010mpCfgReservePortn = _Rm10010mpCfgReservePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 9, 1, 1, 1, 3),
    _Rm10010mpCfgReservePortn_Type()
)
rm10010mpCfgReservePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010mpCfgReservePortn.setStatus("current")
_Rm10010mpCfgStartup_ObjectIdentity = ObjectIdentity
rm10010mpCfgStartup = _Rm10010mpCfgStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 9, 2)
)
_Rm10010mpCfgClientStartupTable_Object = MibTable
rm10010mpCfgClientStartupTable = _Rm10010mpCfgClientStartupTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 9, 2, 1)
)
if mibBuilder.loadTexts:
    rm10010mpCfgClientStartupTable.setStatus("current")
_Rm10010mpCfgClientStartupEntry_Object = MibTableRow
rm10010mpCfgClientStartupEntry = _Rm10010mpCfgClientStartupEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 9, 2, 1, 1)
)
rm10010mpCfgClientStartupEntry.setIndexNames(
    (0, "EKINOPS-Rm10010mp-MIB", "rm10010mpCfgClientStartupIndex"),
)
if mibBuilder.loadTexts:
    rm10010mpCfgClientStartupEntry.setStatus("current")


class _Rm10010mpCfgClientStartupIndex_Type(Integer32):
    """Custom type rm10010mpCfgClientStartupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010mpCfgClientStartupIndex_Type.__name__ = "Integer32"
_Rm10010mpCfgClientStartupIndex_Object = MibTableColumn
rm10010mpCfgClientStartupIndex = _Rm10010mpCfgClientStartupIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 9, 2, 1, 1, 1),
    _Rm10010mpCfgClientStartupIndex_Type()
)
rm10010mpCfgClientStartupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCfgClientStartupIndex.setStatus("current")


class _Rm10010mpCfgSystConfPortPortn_Type(Unsigned32):
    """Custom type rm10010mpCfgSystConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010mpCfgSystConfPortPortn_Type.__name__ = "Unsigned32"
_Rm10010mpCfgSystConfPortPortn_Object = MibTableColumn
rm10010mpCfgSystConfPortPortn = _Rm10010mpCfgSystConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 9, 2, 1, 1, 3),
    _Rm10010mpCfgSystConfPortPortn_Type()
)
rm10010mpCfgSystConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010mpCfgSystConfPortPortn.setStatus("current")


class _Rm10010mpCfgNetConfPortPortn_Type(Unsigned32):
    """Custom type rm10010mpCfgNetConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010mpCfgNetConfPortPortn_Type.__name__ = "Unsigned32"
_Rm10010mpCfgNetConfPortPortn_Object = MibTableColumn
rm10010mpCfgNetConfPortPortn = _Rm10010mpCfgNetConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 9, 2, 1, 1, 4),
    _Rm10010mpCfgNetConfPortPortn_Type()
)
rm10010mpCfgNetConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010mpCfgNetConfPortPortn.setStatus("current")


class _Rm10010mpCfgOptionsPortPortn_Type(Unsigned32):
    """Custom type rm10010mpCfgOptionsPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010mpCfgOptionsPortPortn_Type.__name__ = "Unsigned32"
_Rm10010mpCfgOptionsPortPortn_Object = MibTableColumn
rm10010mpCfgOptionsPortPortn = _Rm10010mpCfgOptionsPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 9, 2, 1, 1, 14),
    _Rm10010mpCfgOptionsPortPortn_Type()
)
rm10010mpCfgOptionsPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010mpCfgOptionsPortPortn.setStatus("current")
_Rm10010mpCfgLineStartupTable_Object = MibTable
rm10010mpCfgLineStartupTable = _Rm10010mpCfgLineStartupTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 9, 2, 2)
)
if mibBuilder.loadTexts:
    rm10010mpCfgLineStartupTable.setStatus("current")
_Rm10010mpCfgLineStartupEntry_Object = MibTableRow
rm10010mpCfgLineStartupEntry = _Rm10010mpCfgLineStartupEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 9, 2, 2, 1)
)
rm10010mpCfgLineStartupEntry.setIndexNames(
    (0, "EKINOPS-Rm10010mp-MIB", "rm10010mpCfgLineStartupIndex"),
)
if mibBuilder.loadTexts:
    rm10010mpCfgLineStartupEntry.setStatus("current")


class _Rm10010mpCfgLineStartupIndex_Type(Integer32):
    """Custom type rm10010mpCfgLineStartupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010mpCfgLineStartupIndex_Type.__name__ = "Integer32"
_Rm10010mpCfgLineStartupIndex_Object = MibTableColumn
rm10010mpCfgLineStartupIndex = _Rm10010mpCfgLineStartupIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 9, 2, 2, 1, 1),
    _Rm10010mpCfgLineStartupIndex_Type()
)
rm10010mpCfgLineStartupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCfgLineStartupIndex.setStatus("current")


class _Rm10010mpCfgSystConfLinePortn_Type(Unsigned32):
    """Custom type rm10010mpCfgSystConfLinePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010mpCfgSystConfLinePortn_Type.__name__ = "Unsigned32"
_Rm10010mpCfgSystConfLinePortn_Object = MibTableColumn
rm10010mpCfgSystConfLinePortn = _Rm10010mpCfgSystConfLinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 9, 2, 2, 1, 3),
    _Rm10010mpCfgSystConfLinePortn_Type()
)
rm10010mpCfgSystConfLinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010mpCfgSystConfLinePortn.setStatus("current")


class _Rm10010mpCfgOptionsLinePortn_Type(Unsigned32):
    """Custom type rm10010mpCfgOptionsLinePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010mpCfgOptionsLinePortn_Type.__name__ = "Unsigned32"
_Rm10010mpCfgOptionsLinePortn_Object = MibTableColumn
rm10010mpCfgOptionsLinePortn = _Rm10010mpCfgOptionsLinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 9, 2, 2, 1, 14),
    _Rm10010mpCfgOptionsLinePortn_Type()
)
rm10010mpCfgOptionsLinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010mpCfgOptionsLinePortn.setStatus("current")
_Rm10010mpCfgXfpTable_Object = MibTable
rm10010mpCfgXfpTable = _Rm10010mpCfgXfpTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 9, 2, 3)
)
if mibBuilder.loadTexts:
    rm10010mpCfgXfpTable.setStatus("current")
_Rm10010mpCfgXfpEntry_Object = MibTableRow
rm10010mpCfgXfpEntry = _Rm10010mpCfgXfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 9, 2, 3, 1)
)
rm10010mpCfgXfpEntry.setIndexNames(
    (0, "EKINOPS-Rm10010mp-MIB", "rm10010mpCfgXfpIndex"),
)
if mibBuilder.loadTexts:
    rm10010mpCfgXfpEntry.setStatus("current")


class _Rm10010mpCfgXfpIndex_Type(Integer32):
    """Custom type rm10010mpCfgXfpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010mpCfgXfpIndex_Type.__name__ = "Integer32"
_Rm10010mpCfgXfpIndex_Object = MibTableColumn
rm10010mpCfgXfpIndex = _Rm10010mpCfgXfpIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 9, 2, 3, 1, 1),
    _Rm10010mpCfgXfpIndex_Type()
)
rm10010mpCfgXfpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCfgXfpIndex.setStatus("current")


class _Rm10010mpCfgSystConfMsaLinePortn_Type(Unsigned32):
    """Custom type rm10010mpCfgSystConfMsaLinePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010mpCfgSystConfMsaLinePortn_Type.__name__ = "Unsigned32"
_Rm10010mpCfgSystConfMsaLinePortn_Object = MibTableColumn
rm10010mpCfgSystConfMsaLinePortn = _Rm10010mpCfgSystConfMsaLinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 9, 2, 3, 1, 3),
    _Rm10010mpCfgSystConfMsaLinePortn_Type()
)
rm10010mpCfgSystConfMsaLinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010mpCfgSystConfMsaLinePortn.setStatus("current")
_Rm10010mpCfgLabels_ObjectIdentity = ObjectIdentity
rm10010mpCfgLabels = _Rm10010mpCfgLabels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 9, 3)
)
_Rm10010mpCfgLabelclientTable_Object = MibTable
rm10010mpCfgLabelclientTable = _Rm10010mpCfgLabelclientTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 9, 3, 1)
)
if mibBuilder.loadTexts:
    rm10010mpCfgLabelclientTable.setStatus("current")
_Rm10010mpCfgLabelclientEntry_Object = MibTableRow
rm10010mpCfgLabelclientEntry = _Rm10010mpCfgLabelclientEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 9, 3, 1, 1)
)
rm10010mpCfgLabelclientEntry.setIndexNames(
    (0, "EKINOPS-Rm10010mp-MIB", "rm10010mpCfgLabelclientIndex"),
)
if mibBuilder.loadTexts:
    rm10010mpCfgLabelclientEntry.setStatus("current")


class _Rm10010mpCfgLabelclientIndex_Type(Integer32):
    """Custom type rm10010mpCfgLabelclientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010mpCfgLabelclientIndex_Type.__name__ = "Integer32"
_Rm10010mpCfgLabelclientIndex_Object = MibTableColumn
rm10010mpCfgLabelclientIndex = _Rm10010mpCfgLabelclientIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 9, 3, 1, 1, 1),
    _Rm10010mpCfgLabelclientIndex_Type()
)
rm10010mpCfgLabelclientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCfgLabelclientIndex.setStatus("current")


class _Rm10010mpCfgLabelclientPortn_Type(DisplayString):
    """Custom type rm10010mpCfgLabelclientPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Rm10010mpCfgLabelclientPortn_Type.__name__ = "DisplayString"
_Rm10010mpCfgLabelclientPortn_Object = MibTableColumn
rm10010mpCfgLabelclientPortn = _Rm10010mpCfgLabelclientPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 9, 3, 1, 1, 3),
    _Rm10010mpCfgLabelclientPortn_Type()
)
rm10010mpCfgLabelclientPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010mpCfgLabelclientPortn.setStatus("current")
_Rm10010mpCfgLabellineTable_Object = MibTable
rm10010mpCfgLabellineTable = _Rm10010mpCfgLabellineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 9, 3, 2)
)
if mibBuilder.loadTexts:
    rm10010mpCfgLabellineTable.setStatus("current")
_Rm10010mpCfgLabellineEntry_Object = MibTableRow
rm10010mpCfgLabellineEntry = _Rm10010mpCfgLabellineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 9, 3, 2, 1)
)
rm10010mpCfgLabellineEntry.setIndexNames(
    (0, "EKINOPS-Rm10010mp-MIB", "rm10010mpCfgLabellineIndex"),
)
if mibBuilder.loadTexts:
    rm10010mpCfgLabellineEntry.setStatus("current")


class _Rm10010mpCfgLabellineIndex_Type(Integer32):
    """Custom type rm10010mpCfgLabellineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010mpCfgLabellineIndex_Type.__name__ = "Integer32"
_Rm10010mpCfgLabellineIndex_Object = MibTableColumn
rm10010mpCfgLabellineIndex = _Rm10010mpCfgLabellineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 9, 3, 2, 1, 1),
    _Rm10010mpCfgLabellineIndex_Type()
)
rm10010mpCfgLabellineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCfgLabellineIndex.setStatus("current")


class _Rm10010mpCfgLabellinePortn_Type(DisplayString):
    """Custom type rm10010mpCfgLabellinePortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Rm10010mpCfgLabellinePortn_Type.__name__ = "DisplayString"
_Rm10010mpCfgLabellinePortn_Object = MibTableColumn
rm10010mpCfgLabellinePortn = _Rm10010mpCfgLabellinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 9, 3, 2, 1, 3),
    _Rm10010mpCfgLabellinePortn_Type()
)
rm10010mpCfgLabellinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010mpCfgLabellinePortn.setStatus("current")
_Rm10010mpCfgStartuptlh_ObjectIdentity = ObjectIdentity
rm10010mpCfgStartuptlh = _Rm10010mpCfgStartuptlh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 9, 4)
)
_Rm10010mpCfgOtxtlhTable_Object = MibTable
rm10010mpCfgOtxtlhTable = _Rm10010mpCfgOtxtlhTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 9, 4, 1)
)
if mibBuilder.loadTexts:
    rm10010mpCfgOtxtlhTable.setStatus("current")
_Rm10010mpCfgOtxtlhEntry_Object = MibTableRow
rm10010mpCfgOtxtlhEntry = _Rm10010mpCfgOtxtlhEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 9, 4, 1, 1)
)
rm10010mpCfgOtxtlhEntry.setIndexNames(
    (0, "EKINOPS-Rm10010mp-MIB", "rm10010mpCfgOtxtlhIndex"),
)
if mibBuilder.loadTexts:
    rm10010mpCfgOtxtlhEntry.setStatus("current")


class _Rm10010mpCfgOtxtlhIndex_Type(Integer32):
    """Custom type rm10010mpCfgOtxtlhIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010mpCfgOtxtlhIndex_Type.__name__ = "Integer32"
_Rm10010mpCfgOtxtlhIndex_Object = MibTableColumn
rm10010mpCfgOtxtlhIndex = _Rm10010mpCfgOtxtlhIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 9, 4, 1, 1, 1),
    _Rm10010mpCfgOtxtlhIndex_Type()
)
rm10010mpCfgOtxtlhIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCfgOtxtlhIndex.setStatus("current")


class _Rm10010mpCfgLinePwrLaserPortn_Type(Unsigned32):
    """Custom type rm10010mpCfgLinePwrLaserPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010mpCfgLinePwrLaserPortn_Type.__name__ = "Unsigned32"
_Rm10010mpCfgLinePwrLaserPortn_Object = MibTableColumn
rm10010mpCfgLinePwrLaserPortn = _Rm10010mpCfgLinePwrLaserPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 9, 4, 1, 1, 6),
    _Rm10010mpCfgLinePwrLaserPortn_Type()
)
rm10010mpCfgLinePwrLaserPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010mpCfgLinePwrLaserPortn.setStatus("current")


class _Rm10010mpCfgLineFCurrentPortn_Type(Unsigned32):
    """Custom type rm10010mpCfgLineFCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010mpCfgLineFCurrentPortn_Type.__name__ = "Unsigned32"
_Rm10010mpCfgLineFCurrentPortn_Object = MibTableColumn
rm10010mpCfgLineFCurrentPortn = _Rm10010mpCfgLineFCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 9, 4, 1, 1, 7),
    _Rm10010mpCfgLineFCurrentPortn_Type()
)
rm10010mpCfgLineFCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010mpCfgLineFCurrentPortn.setStatus("current")


class _Rm10010mpCfgLineGridCurrentPortn_Type(Unsigned32):
    """Custom type rm10010mpCfgLineGridCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010mpCfgLineGridCurrentPortn_Type.__name__ = "Unsigned32"
_Rm10010mpCfgLineGridCurrentPortn_Object = MibTableColumn
rm10010mpCfgLineGridCurrentPortn = _Rm10010mpCfgLineGridCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 9, 4, 1, 1, 8),
    _Rm10010mpCfgLineGridCurrentPortn_Type()
)
rm10010mpCfgLineGridCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010mpCfgLineGridCurrentPortn.setStatus("current")


class _Rm10010mpCfgFPortn_Type(Unsigned32):
    """Custom type rm10010mpCfgFPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010mpCfgFPortn_Type.__name__ = "Unsigned32"
_Rm10010mpCfgFPortn_Object = MibTableColumn
rm10010mpCfgFPortn = _Rm10010mpCfgFPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 9, 4, 1, 1, 9),
    _Rm10010mpCfgFPortn_Type()
)
rm10010mpCfgFPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010mpCfgFPortn.setStatus("current")


class _Rm10010mpCfgRxLineFCurrentPortn_Type(Unsigned32):
    """Custom type rm10010mpCfgRxLineFCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010mpCfgRxLineFCurrentPortn_Type.__name__ = "Unsigned32"
_Rm10010mpCfgRxLineFCurrentPortn_Object = MibTableColumn
rm10010mpCfgRxLineFCurrentPortn = _Rm10010mpCfgRxLineFCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 9, 4, 1, 1, 10),
    _Rm10010mpCfgRxLineFCurrentPortn_Type()
)
rm10010mpCfgRxLineFCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010mpCfgRxLineFCurrentPortn.setStatus("current")
_Rm10010mpCfgOther_ObjectIdentity = ObjectIdentity
rm10010mpCfgOther = _Rm10010mpCfgOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 9, 5)
)
_Rm10010mptablemoduleOther_ObjectIdentity = ObjectIdentity
rm10010mptablemoduleOther = _Rm10010mptablemoduleOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 9, 5, 1)
)


class _Rm10010mpCfgmode_Type(Unsigned32):
    """Custom type rm10010mpCfgmode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010mpCfgmode_Type.__name__ = "Unsigned32"
_Rm10010mpCfgmode_Object = MibScalar
rm10010mpCfgmode = _Rm10010mpCfgmode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 9, 5, 1, 2),
    _Rm10010mpCfgmode_Type()
)
rm10010mpCfgmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010mpCfgmode.setStatus("current")


class _Rm10010mpCfgfanLowSpeedThreshold_Type(Unsigned32):
    """Custom type rm10010mpCfgfanLowSpeedThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010mpCfgfanLowSpeedThreshold_Type.__name__ = "Unsigned32"
_Rm10010mpCfgfanLowSpeedThreshold_Object = MibScalar
rm10010mpCfgfanLowSpeedThreshold = _Rm10010mpCfgfanLowSpeedThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 9, 5, 1, 3),
    _Rm10010mpCfgfanLowSpeedThreshold_Type()
)
rm10010mpCfgfanLowSpeedThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010mpCfgfanLowSpeedThreshold.setStatus("current")


class _Rm10010mpCfgfanHighSpeedThreshold_Type(Unsigned32):
    """Custom type rm10010mpCfgfanHighSpeedThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010mpCfgfanHighSpeedThreshold_Type.__name__ = "Unsigned32"
_Rm10010mpCfgfanHighSpeedThreshold_Object = MibScalar
rm10010mpCfgfanHighSpeedThreshold = _Rm10010mpCfgfanHighSpeedThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 9, 5, 1, 4),
    _Rm10010mpCfgfanHighSpeedThreshold_Type()
)
rm10010mpCfgfanHighSpeedThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010mpCfgfanHighSpeedThreshold.setStatus("current")
_Rm10010mpCfgStartuptablefive_ObjectIdentity = ObjectIdentity
rm10010mpCfgStartuptablefive = _Rm10010mpCfgStartuptablefive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 9, 6)
)
_Rm10010mpCfgOtxtlhcapabilitiesTable_Object = MibTable
rm10010mpCfgOtxtlhcapabilitiesTable = _Rm10010mpCfgOtxtlhcapabilitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 9, 6, 1)
)
if mibBuilder.loadTexts:
    rm10010mpCfgOtxtlhcapabilitiesTable.setStatus("current")
_Rm10010mpCfgOtxtlhcapabilitiesEntry_Object = MibTableRow
rm10010mpCfgOtxtlhcapabilitiesEntry = _Rm10010mpCfgOtxtlhcapabilitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 9, 6, 1, 1)
)
rm10010mpCfgOtxtlhcapabilitiesEntry.setIndexNames(
    (0, "EKINOPS-Rm10010mp-MIB", "rm10010mpCfgOtxtlhcapabilitiesIndex"),
)
if mibBuilder.loadTexts:
    rm10010mpCfgOtxtlhcapabilitiesEntry.setStatus("current")


class _Rm10010mpCfgOtxtlhcapabilitiesIndex_Type(Integer32):
    """Custom type rm10010mpCfgOtxtlhcapabilitiesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010mpCfgOtxtlhcapabilitiesIndex_Type.__name__ = "Integer32"
_Rm10010mpCfgOtxtlhcapabilitiesIndex_Object = MibTableColumn
rm10010mpCfgOtxtlhcapabilitiesIndex = _Rm10010mpCfgOtxtlhcapabilitiesIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 9, 6, 1, 1, 1),
    _Rm10010mpCfgOtxtlhcapabilitiesIndex_Type()
)
rm10010mpCfgOtxtlhcapabilitiesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCfgOtxtlhcapabilitiesIndex.setStatus("current")


class _Rm10010mpCfgComponentTypePortn_Type(Unsigned32):
    """Custom type rm10010mpCfgComponentTypePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010mpCfgComponentTypePortn_Type.__name__ = "Unsigned32"
_Rm10010mpCfgComponentTypePortn_Object = MibTableColumn
rm10010mpCfgComponentTypePortn = _Rm10010mpCfgComponentTypePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 9, 6, 1, 1, 3),
    _Rm10010mpCfgComponentTypePortn_Type()
)
rm10010mpCfgComponentTypePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCfgComponentTypePortn.setStatus("current")


class _Rm10010mpCfgMiscellaneousPortn_Type(Unsigned32):
    """Custom type rm10010mpCfgMiscellaneousPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010mpCfgMiscellaneousPortn_Type.__name__ = "Unsigned32"
_Rm10010mpCfgMiscellaneousPortn_Object = MibTableColumn
rm10010mpCfgMiscellaneousPortn = _Rm10010mpCfgMiscellaneousPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 9, 6, 1, 1, 4),
    _Rm10010mpCfgMiscellaneousPortn_Type()
)
rm10010mpCfgMiscellaneousPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCfgMiscellaneousPortn.setStatus("current")


class _Rm10010mpCfgFirstChannelPortn_Type(Unsigned32):
    """Custom type rm10010mpCfgFirstChannelPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010mpCfgFirstChannelPortn_Type.__name__ = "Unsigned32"
_Rm10010mpCfgFirstChannelPortn_Object = MibTableColumn
rm10010mpCfgFirstChannelPortn = _Rm10010mpCfgFirstChannelPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 9, 6, 1, 1, 5),
    _Rm10010mpCfgFirstChannelPortn_Type()
)
rm10010mpCfgFirstChannelPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCfgFirstChannelPortn.setStatus("current")


class _Rm10010mpCfgLastChannelPortn_Type(Unsigned32):
    """Custom type rm10010mpCfgLastChannelPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010mpCfgLastChannelPortn_Type.__name__ = "Unsigned32"
_Rm10010mpCfgLastChannelPortn_Object = MibTableColumn
rm10010mpCfgLastChannelPortn = _Rm10010mpCfgLastChannelPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 9, 6, 1, 1, 6),
    _Rm10010mpCfgLastChannelPortn_Type()
)
rm10010mpCfgLastChannelPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCfgLastChannelPortn.setStatus("current")


class _Rm10010mpCfgGridPortn_Type(Unsigned32):
    """Custom type rm10010mpCfgGridPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Rm10010mpCfgGridPortn_Type.__name__ = "Unsigned32"
_Rm10010mpCfgGridPortn_Object = MibTableColumn
rm10010mpCfgGridPortn = _Rm10010mpCfgGridPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 9, 6, 1, 1, 7),
    _Rm10010mpCfgGridPortn_Type()
)
rm10010mpCfgGridPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpCfgGridPortn.setStatus("current")
_Rm10010mpCfgWriteConfiguration_Type = EkiOnOff
_Rm10010mpCfgWriteConfiguration_Object = MibScalar
rm10010mpCfgWriteConfiguration = _Rm10010mpCfgWriteConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 9, 257),
    _Rm10010mpCfgWriteConfiguration_Type()
)
rm10010mpCfgWriteConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rm10010mpCfgWriteConfiguration.setStatus("current")
_Rm10010mptraps_ObjectIdentity = ObjectIdentity
rm10010mptraps = _Rm10010mptraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 10)
)


class _Rm10010mptrapPortNumber_Type(Integer32):
    """Custom type rm10010mptrapPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Rm10010mptrapPortNumber_Type.__name__ = "Integer32"
_Rm10010mptrapPortNumber_Object = MibScalar
rm10010mptrapPortNumber = _Rm10010mptrapPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 10, 2),
    _Rm10010mptrapPortNumber_Type()
)
rm10010mptrapPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mptrapPortNumber.setStatus("current")


class _Rm10010mptrapLineNumber_Type(Integer32):
    """Custom type rm10010mptrapLineNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Rm10010mptrapLineNumber_Type.__name__ = "Integer32"
_Rm10010mptrapLineNumber_Object = MibScalar
rm10010mptrapLineNumber = _Rm10010mptrapLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 10, 3),
    _Rm10010mptrapLineNumber_Type()
)
rm10010mptrapLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mptrapLineNumber.setStatus("current")


class _Rm10010mptrapBoardNumber_Type(Integer32):
    """Custom type rm10010mptrapBoardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Rm10010mptrapBoardNumber_Type.__name__ = "Integer32"
_Rm10010mptrapBoardNumber_Object = MibScalar
rm10010mptrapBoardNumber = _Rm10010mptrapBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 10, 4),
    _Rm10010mptrapBoardNumber_Type()
)
rm10010mptrapBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mptrapBoardNumber.setStatus("current")
_Rm10010mpMonitoring_ObjectIdentity = ObjectIdentity
rm10010mpMonitoring = _Rm10010mpMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 11)
)
_Rm10010mpMonOther_ObjectIdentity = ObjectIdentity
rm10010mpMonOther = _Rm10010mpMonOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 11, 1)
)
_Rm10010mpMonRmon_ObjectIdentity = ObjectIdentity
rm10010mpMonRmon = _Rm10010mpMonRmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 11, 1, 3)
)
_Rm10010mpMonClient_ObjectIdentity = ObjectIdentity
rm10010mpMonClient = _Rm10010mpMonClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 11, 2)
)
_Rm10010mpMonClientRmonCounter_ObjectIdentity = ObjectIdentity
rm10010mpMonClientRmonCounter = _Rm10010mpMonClientRmonCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 54, 11, 2, 4)
)
_Rm10010mpMonupRmonBytesCounterClientInputTable_Object = MibTable
rm10010mpMonupRmonBytesCounterClientInputTable = _Rm10010mpMonupRmonBytesCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 11, 2, 4, 16)
)
if mibBuilder.loadTexts:
    rm10010mpMonupRmonBytesCounterClientInputTable.setStatus("current")
_Rm10010mpMonupRmonBytesCounterClientInputEntry_Object = MibTableRow
rm10010mpMonupRmonBytesCounterClientInputEntry = _Rm10010mpMonupRmonBytesCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 11, 2, 4, 16, 1)
)
rm10010mpMonupRmonBytesCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Rm10010mp-MIB", "rm10010mpMonupRmonBytesCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    rm10010mpMonupRmonBytesCounterClientInputEntry.setStatus("current")


class _Rm10010mpMonupRmonBytesCounterClientInputIndex_Type(Integer32):
    """Custom type rm10010mpMonupRmonBytesCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010mpMonupRmonBytesCounterClientInputIndex_Type.__name__ = "Integer32"
_Rm10010mpMonupRmonBytesCounterClientInputIndex_Object = MibTableColumn
rm10010mpMonupRmonBytesCounterClientInputIndex = _Rm10010mpMonupRmonBytesCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 11, 2, 4, 16, 1, 1),
    _Rm10010mpMonupRmonBytesCounterClientInputIndex_Type()
)
rm10010mpMonupRmonBytesCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMonupRmonBytesCounterClientInputIndex.setStatus("current")
_Rm10010mpMonupRmonBytesCounterClientInputValuePortn_Type = Counter64
_Rm10010mpMonupRmonBytesCounterClientInputValuePortn_Object = MibTableColumn
rm10010mpMonupRmonBytesCounterClientInputValuePortn = _Rm10010mpMonupRmonBytesCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 11, 2, 4, 16, 1, 2),
    _Rm10010mpMonupRmonBytesCounterClientInputValuePortn_Type()
)
rm10010mpMonupRmonBytesCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMonupRmonBytesCounterClientInputValuePortn.setStatus("current")
_Rm10010mpMonupRmonBytesCounterClientInputErrorPortn_Type = EkiOnOff
_Rm10010mpMonupRmonBytesCounterClientInputErrorPortn_Object = MibTableColumn
rm10010mpMonupRmonBytesCounterClientInputErrorPortn = _Rm10010mpMonupRmonBytesCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 11, 2, 4, 16, 1, 3),
    _Rm10010mpMonupRmonBytesCounterClientInputErrorPortn_Type()
)
rm10010mpMonupRmonBytesCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMonupRmonBytesCounterClientInputErrorPortn.setStatus("current")
_Rm10010mpMonupRmonBytesCounterClientInputOverloadPortn_Type = EkiOnOff
_Rm10010mpMonupRmonBytesCounterClientInputOverloadPortn_Object = MibTableColumn
rm10010mpMonupRmonBytesCounterClientInputOverloadPortn = _Rm10010mpMonupRmonBytesCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 11, 2, 4, 16, 1, 4),
    _Rm10010mpMonupRmonBytesCounterClientInputOverloadPortn_Type()
)
rm10010mpMonupRmonBytesCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMonupRmonBytesCounterClientInputOverloadPortn.setStatus("current")
_Rm10010mpMonupRmonCrcErrorsCounterClientInputTable_Object = MibTable
rm10010mpMonupRmonCrcErrorsCounterClientInputTable = _Rm10010mpMonupRmonCrcErrorsCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 11, 2, 4, 32)
)
if mibBuilder.loadTexts:
    rm10010mpMonupRmonCrcErrorsCounterClientInputTable.setStatus("current")
_Rm10010mpMonupRmonCrcErrorsCounterClientInputEntry_Object = MibTableRow
rm10010mpMonupRmonCrcErrorsCounterClientInputEntry = _Rm10010mpMonupRmonCrcErrorsCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 11, 2, 4, 32, 1)
)
rm10010mpMonupRmonCrcErrorsCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Rm10010mp-MIB", "rm10010mpMonupRmonCrcErrorsCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    rm10010mpMonupRmonCrcErrorsCounterClientInputEntry.setStatus("current")


class _Rm10010mpMonupRmonCrcErrorsCounterClientInputIndex_Type(Integer32):
    """Custom type rm10010mpMonupRmonCrcErrorsCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010mpMonupRmonCrcErrorsCounterClientInputIndex_Type.__name__ = "Integer32"
_Rm10010mpMonupRmonCrcErrorsCounterClientInputIndex_Object = MibTableColumn
rm10010mpMonupRmonCrcErrorsCounterClientInputIndex = _Rm10010mpMonupRmonCrcErrorsCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 11, 2, 4, 32, 1, 1),
    _Rm10010mpMonupRmonCrcErrorsCounterClientInputIndex_Type()
)
rm10010mpMonupRmonCrcErrorsCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMonupRmonCrcErrorsCounterClientInputIndex.setStatus("current")
_Rm10010mpMonupRmonCrcErrorsCounterClientInputValuePortn_Type = Counter64
_Rm10010mpMonupRmonCrcErrorsCounterClientInputValuePortn_Object = MibTableColumn
rm10010mpMonupRmonCrcErrorsCounterClientInputValuePortn = _Rm10010mpMonupRmonCrcErrorsCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 11, 2, 4, 32, 1, 2),
    _Rm10010mpMonupRmonCrcErrorsCounterClientInputValuePortn_Type()
)
rm10010mpMonupRmonCrcErrorsCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMonupRmonCrcErrorsCounterClientInputValuePortn.setStatus("current")
_Rm10010mpMonupRmonCrcErrorsCounterClientInputErrorPortn_Type = EkiOnOff
_Rm10010mpMonupRmonCrcErrorsCounterClientInputErrorPortn_Object = MibTableColumn
rm10010mpMonupRmonCrcErrorsCounterClientInputErrorPortn = _Rm10010mpMonupRmonCrcErrorsCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 11, 2, 4, 32, 1, 3),
    _Rm10010mpMonupRmonCrcErrorsCounterClientInputErrorPortn_Type()
)
rm10010mpMonupRmonCrcErrorsCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMonupRmonCrcErrorsCounterClientInputErrorPortn.setStatus("current")
_Rm10010mpMonupRmonCrcErrorsCounterClientInputOverloadPortn_Type = EkiOnOff
_Rm10010mpMonupRmonCrcErrorsCounterClientInputOverloadPortn_Object = MibTableColumn
rm10010mpMonupRmonCrcErrorsCounterClientInputOverloadPortn = _Rm10010mpMonupRmonCrcErrorsCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 11, 2, 4, 32, 1, 4),
    _Rm10010mpMonupRmonCrcErrorsCounterClientInputOverloadPortn_Type()
)
rm10010mpMonupRmonCrcErrorsCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMonupRmonCrcErrorsCounterClientInputOverloadPortn.setStatus("current")
_Rm10010mpMonupRmonPacketsCounterClientInputTable_Object = MibTable
rm10010mpMonupRmonPacketsCounterClientInputTable = _Rm10010mpMonupRmonPacketsCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 11, 2, 4, 48)
)
if mibBuilder.loadTexts:
    rm10010mpMonupRmonPacketsCounterClientInputTable.setStatus("current")
_Rm10010mpMonupRmonPacketsCounterClientInputEntry_Object = MibTableRow
rm10010mpMonupRmonPacketsCounterClientInputEntry = _Rm10010mpMonupRmonPacketsCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 11, 2, 4, 48, 1)
)
rm10010mpMonupRmonPacketsCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Rm10010mp-MIB", "rm10010mpMonupRmonPacketsCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    rm10010mpMonupRmonPacketsCounterClientInputEntry.setStatus("current")


class _Rm10010mpMonupRmonPacketsCounterClientInputIndex_Type(Integer32):
    """Custom type rm10010mpMonupRmonPacketsCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010mpMonupRmonPacketsCounterClientInputIndex_Type.__name__ = "Integer32"
_Rm10010mpMonupRmonPacketsCounterClientInputIndex_Object = MibTableColumn
rm10010mpMonupRmonPacketsCounterClientInputIndex = _Rm10010mpMonupRmonPacketsCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 11, 2, 4, 48, 1, 1),
    _Rm10010mpMonupRmonPacketsCounterClientInputIndex_Type()
)
rm10010mpMonupRmonPacketsCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMonupRmonPacketsCounterClientInputIndex.setStatus("current")
_Rm10010mpMonupRmonPacketsCounterClientInputValuePortn_Type = Counter64
_Rm10010mpMonupRmonPacketsCounterClientInputValuePortn_Object = MibTableColumn
rm10010mpMonupRmonPacketsCounterClientInputValuePortn = _Rm10010mpMonupRmonPacketsCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 11, 2, 4, 48, 1, 2),
    _Rm10010mpMonupRmonPacketsCounterClientInputValuePortn_Type()
)
rm10010mpMonupRmonPacketsCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMonupRmonPacketsCounterClientInputValuePortn.setStatus("current")
_Rm10010mpMonupRmonPacketsCounterClientInputErrorPortn_Type = EkiOnOff
_Rm10010mpMonupRmonPacketsCounterClientInputErrorPortn_Object = MibTableColumn
rm10010mpMonupRmonPacketsCounterClientInputErrorPortn = _Rm10010mpMonupRmonPacketsCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 11, 2, 4, 48, 1, 3),
    _Rm10010mpMonupRmonPacketsCounterClientInputErrorPortn_Type()
)
rm10010mpMonupRmonPacketsCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMonupRmonPacketsCounterClientInputErrorPortn.setStatus("current")
_Rm10010mpMonupRmonPacketsCounterClientInputOverloadPortn_Type = EkiOnOff
_Rm10010mpMonupRmonPacketsCounterClientInputOverloadPortn_Object = MibTableColumn
rm10010mpMonupRmonPacketsCounterClientInputOverloadPortn = _Rm10010mpMonupRmonPacketsCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 11, 2, 4, 48, 1, 4),
    _Rm10010mpMonupRmonPacketsCounterClientInputOverloadPortn_Type()
)
rm10010mpMonupRmonPacketsCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMonupRmonPacketsCounterClientInputOverloadPortn.setStatus("current")
_Rm10010mpMonupRmonBroadcastCounterClientInputTable_Object = MibTable
rm10010mpMonupRmonBroadcastCounterClientInputTable = _Rm10010mpMonupRmonBroadcastCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 11, 2, 4, 64)
)
if mibBuilder.loadTexts:
    rm10010mpMonupRmonBroadcastCounterClientInputTable.setStatus("current")
_Rm10010mpMonupRmonBroadcastCounterClientInputEntry_Object = MibTableRow
rm10010mpMonupRmonBroadcastCounterClientInputEntry = _Rm10010mpMonupRmonBroadcastCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 11, 2, 4, 64, 1)
)
rm10010mpMonupRmonBroadcastCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Rm10010mp-MIB", "rm10010mpMonupRmonBroadcastCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    rm10010mpMonupRmonBroadcastCounterClientInputEntry.setStatus("current")


class _Rm10010mpMonupRmonBroadcastCounterClientInputIndex_Type(Integer32):
    """Custom type rm10010mpMonupRmonBroadcastCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010mpMonupRmonBroadcastCounterClientInputIndex_Type.__name__ = "Integer32"
_Rm10010mpMonupRmonBroadcastCounterClientInputIndex_Object = MibTableColumn
rm10010mpMonupRmonBroadcastCounterClientInputIndex = _Rm10010mpMonupRmonBroadcastCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 11, 2, 4, 64, 1, 1),
    _Rm10010mpMonupRmonBroadcastCounterClientInputIndex_Type()
)
rm10010mpMonupRmonBroadcastCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMonupRmonBroadcastCounterClientInputIndex.setStatus("current")
_Rm10010mpMonupRmonBroadcastCounterClientInputValuePortn_Type = Counter64
_Rm10010mpMonupRmonBroadcastCounterClientInputValuePortn_Object = MibTableColumn
rm10010mpMonupRmonBroadcastCounterClientInputValuePortn = _Rm10010mpMonupRmonBroadcastCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 11, 2, 4, 64, 1, 2),
    _Rm10010mpMonupRmonBroadcastCounterClientInputValuePortn_Type()
)
rm10010mpMonupRmonBroadcastCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMonupRmonBroadcastCounterClientInputValuePortn.setStatus("current")
_Rm10010mpMonupRmonBroadcastCounterClientInputErrorPortn_Type = EkiOnOff
_Rm10010mpMonupRmonBroadcastCounterClientInputErrorPortn_Object = MibTableColumn
rm10010mpMonupRmonBroadcastCounterClientInputErrorPortn = _Rm10010mpMonupRmonBroadcastCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 11, 2, 4, 64, 1, 3),
    _Rm10010mpMonupRmonBroadcastCounterClientInputErrorPortn_Type()
)
rm10010mpMonupRmonBroadcastCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMonupRmonBroadcastCounterClientInputErrorPortn.setStatus("current")
_Rm10010mpMonupRmonBroadcastCounterClientInputOverloadPortn_Type = EkiOnOff
_Rm10010mpMonupRmonBroadcastCounterClientInputOverloadPortn_Object = MibTableColumn
rm10010mpMonupRmonBroadcastCounterClientInputOverloadPortn = _Rm10010mpMonupRmonBroadcastCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 11, 2, 4, 64, 1, 4),
    _Rm10010mpMonupRmonBroadcastCounterClientInputOverloadPortn_Type()
)
rm10010mpMonupRmonBroadcastCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMonupRmonBroadcastCounterClientInputOverloadPortn.setStatus("current")
_Rm10010mpMonupRmonMulticastCounterClientInputTable_Object = MibTable
rm10010mpMonupRmonMulticastCounterClientInputTable = _Rm10010mpMonupRmonMulticastCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 11, 2, 4, 80)
)
if mibBuilder.loadTexts:
    rm10010mpMonupRmonMulticastCounterClientInputTable.setStatus("current")
_Rm10010mpMonupRmonMulticastCounterClientInputEntry_Object = MibTableRow
rm10010mpMonupRmonMulticastCounterClientInputEntry = _Rm10010mpMonupRmonMulticastCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 11, 2, 4, 80, 1)
)
rm10010mpMonupRmonMulticastCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Rm10010mp-MIB", "rm10010mpMonupRmonMulticastCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    rm10010mpMonupRmonMulticastCounterClientInputEntry.setStatus("current")


class _Rm10010mpMonupRmonMulticastCounterClientInputIndex_Type(Integer32):
    """Custom type rm10010mpMonupRmonMulticastCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010mpMonupRmonMulticastCounterClientInputIndex_Type.__name__ = "Integer32"
_Rm10010mpMonupRmonMulticastCounterClientInputIndex_Object = MibTableColumn
rm10010mpMonupRmonMulticastCounterClientInputIndex = _Rm10010mpMonupRmonMulticastCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 11, 2, 4, 80, 1, 1),
    _Rm10010mpMonupRmonMulticastCounterClientInputIndex_Type()
)
rm10010mpMonupRmonMulticastCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMonupRmonMulticastCounterClientInputIndex.setStatus("current")
_Rm10010mpMonupRmonMulticastCounterClientInputValuePortn_Type = Counter64
_Rm10010mpMonupRmonMulticastCounterClientInputValuePortn_Object = MibTableColumn
rm10010mpMonupRmonMulticastCounterClientInputValuePortn = _Rm10010mpMonupRmonMulticastCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 11, 2, 4, 80, 1, 2),
    _Rm10010mpMonupRmonMulticastCounterClientInputValuePortn_Type()
)
rm10010mpMonupRmonMulticastCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMonupRmonMulticastCounterClientInputValuePortn.setStatus("current")
_Rm10010mpMonupRmonMulticastCounterClientInputErrorPortn_Type = EkiOnOff
_Rm10010mpMonupRmonMulticastCounterClientInputErrorPortn_Object = MibTableColumn
rm10010mpMonupRmonMulticastCounterClientInputErrorPortn = _Rm10010mpMonupRmonMulticastCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 11, 2, 4, 80, 1, 3),
    _Rm10010mpMonupRmonMulticastCounterClientInputErrorPortn_Type()
)
rm10010mpMonupRmonMulticastCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMonupRmonMulticastCounterClientInputErrorPortn.setStatus("current")
_Rm10010mpMonupRmonMulticastCounterClientInputOverloadPortn_Type = EkiOnOff
_Rm10010mpMonupRmonMulticastCounterClientInputOverloadPortn_Object = MibTableColumn
rm10010mpMonupRmonMulticastCounterClientInputOverloadPortn = _Rm10010mpMonupRmonMulticastCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 11, 2, 4, 80, 1, 4),
    _Rm10010mpMonupRmonMulticastCounterClientInputOverloadPortn_Type()
)
rm10010mpMonupRmonMulticastCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMonupRmonMulticastCounterClientInputOverloadPortn.setStatus("current")
_Rm10010mpMonupRmonPauseFrameCounterClientInputTable_Object = MibTable
rm10010mpMonupRmonPauseFrameCounterClientInputTable = _Rm10010mpMonupRmonPauseFrameCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 11, 2, 4, 96)
)
if mibBuilder.loadTexts:
    rm10010mpMonupRmonPauseFrameCounterClientInputTable.setStatus("current")
_Rm10010mpMonupRmonPauseFrameCounterClientInputEntry_Object = MibTableRow
rm10010mpMonupRmonPauseFrameCounterClientInputEntry = _Rm10010mpMonupRmonPauseFrameCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 11, 2, 4, 96, 1)
)
rm10010mpMonupRmonPauseFrameCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Rm10010mp-MIB", "rm10010mpMonupRmonPauseFrameCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    rm10010mpMonupRmonPauseFrameCounterClientInputEntry.setStatus("current")


class _Rm10010mpMonupRmonPauseFrameCounterClientInputIndex_Type(Integer32):
    """Custom type rm10010mpMonupRmonPauseFrameCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Rm10010mpMonupRmonPauseFrameCounterClientInputIndex_Type.__name__ = "Integer32"
_Rm10010mpMonupRmonPauseFrameCounterClientInputIndex_Object = MibTableColumn
rm10010mpMonupRmonPauseFrameCounterClientInputIndex = _Rm10010mpMonupRmonPauseFrameCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 11, 2, 4, 96, 1, 1),
    _Rm10010mpMonupRmonPauseFrameCounterClientInputIndex_Type()
)
rm10010mpMonupRmonPauseFrameCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMonupRmonPauseFrameCounterClientInputIndex.setStatus("current")
_Rm10010mpMonupRmonPauseFrameCounterClientInputValuePortn_Type = Counter64
_Rm10010mpMonupRmonPauseFrameCounterClientInputValuePortn_Object = MibTableColumn
rm10010mpMonupRmonPauseFrameCounterClientInputValuePortn = _Rm10010mpMonupRmonPauseFrameCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 11, 2, 4, 96, 1, 2),
    _Rm10010mpMonupRmonPauseFrameCounterClientInputValuePortn_Type()
)
rm10010mpMonupRmonPauseFrameCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMonupRmonPauseFrameCounterClientInputValuePortn.setStatus("current")
_Rm10010mpMonupRmonPauseFrameCounterClientInputErrorPortn_Type = EkiOnOff
_Rm10010mpMonupRmonPauseFrameCounterClientInputErrorPortn_Object = MibTableColumn
rm10010mpMonupRmonPauseFrameCounterClientInputErrorPortn = _Rm10010mpMonupRmonPauseFrameCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 11, 2, 4, 96, 1, 3),
    _Rm10010mpMonupRmonPauseFrameCounterClientInputErrorPortn_Type()
)
rm10010mpMonupRmonPauseFrameCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMonupRmonPauseFrameCounterClientInputErrorPortn.setStatus("current")
_Rm10010mpMonupRmonPauseFrameCounterClientInputOverloadPortn_Type = EkiOnOff
_Rm10010mpMonupRmonPauseFrameCounterClientInputOverloadPortn_Object = MibTableColumn
rm10010mpMonupRmonPauseFrameCounterClientInputOverloadPortn = _Rm10010mpMonupRmonPauseFrameCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 54, 11, 2, 4, 96, 1, 4),
    _Rm10010mpMonupRmonPauseFrameCounterClientInputOverloadPortn_Type()
)
rm10010mpMonupRmonPauseFrameCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010mpMonupRmonPauseFrameCounterClientInputOverloadPortn.setStatus("current")

# Managed Objects groups


# Notification objects

rm10010mpLineTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 54, 10, 30)
)
rm10010mpLineTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Rm10010mp-MIB", "rm10010mpAlmLineDdmWarningPortn"),
        ("EKINOPS-Rm10010mp-MIB", "rm10010mptrapLineNumber"),
        ("EKINOPS-Rm10010mp-MIB", "rm10010mptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    rm10010mpLineTrapNotUrgentGoesOn.setStatus(
        "current"
    )

rm10010mpLineTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 54, 10, 31)
)
rm10010mpLineTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Rm10010mp-MIB", "rm10010mpAlmLineDdmWarningPortn"),
        ("EKINOPS-Rm10010mp-MIB", "rm10010mptrapLineNumber"),
        ("EKINOPS-Rm10010mp-MIB", "rm10010mptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    rm10010mpLineTrapNotUrgentGoesOff.setStatus(
        "current"
    )

rm10010mpLineTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 54, 10, 32)
)
rm10010mpLineTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Rm10010mp-MIB", "rm10010mpAlmLineDdmAlmPortn"),
        ("EKINOPS-Rm10010mp-MIB", "rm10010mptrapLineNumber"),
        ("EKINOPS-Rm10010mp-MIB", "rm10010mptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    rm10010mpLineTrapUrgentGoesOn.setStatus(
        "current"
    )

rm10010mpLineTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 54, 10, 33)
)
rm10010mpLineTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Rm10010mp-MIB", "rm10010mpAlmLineDdmAlmPortn"),
        ("EKINOPS-Rm10010mp-MIB", "rm10010mptrapLineNumber"),
        ("EKINOPS-Rm10010mp-MIB", "rm10010mptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    rm10010mpLineTrapUrgentGoesOff.setStatus(
        "current"
    )

rm10010mpLineTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 54, 10, 34)
)
rm10010mpLineTrapCritGoesOn.setObjects(
      *(("EKINOPS-Rm10010mp-MIB", "rm10010mpAlmLineFailPortn"),
        ("EKINOPS-Rm10010mp-MIB", "rm10010mpAlmLineHwFailPortn"),
        ("EKINOPS-Rm10010mp-MIB", "rm10010mptrapLineNumber"),
        ("EKINOPS-Rm10010mp-MIB", "rm10010mptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    rm10010mpLineTrapCritGoesOn.setStatus(
        "current"
    )

rm10010mpLineTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 54, 10, 35)
)
rm10010mpLineTrapCritGoesOff.setObjects(
      *(("EKINOPS-Rm10010mp-MIB", "rm10010mpAlmLineFailPortn"),
        ("EKINOPS-Rm10010mp-MIB", "rm10010mpAlmLineHwFailPortn"),
        ("EKINOPS-Rm10010mp-MIB", "rm10010mptrapLineNumber"),
        ("EKINOPS-Rm10010mp-MIB", "rm10010mptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    rm10010mpLineTrapCritGoesOff.setStatus(
        "current"
    )

rm10010mpClientTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 54, 10, 40)
)
rm10010mpClientTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Rm10010mp-MIB", "rm10010mpAlmSfpDdmWarningPortn"),
        ("EKINOPS-Rm10010mp-MIB", "rm10010mptrapPortNumber"),
        ("EKINOPS-Rm10010mp-MIB", "rm10010mptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    rm10010mpClientTrapNotUrgentGoesOn.setStatus(
        "current"
    )

rm10010mpClientTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 54, 10, 41)
)
rm10010mpClientTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Rm10010mp-MIB", "rm10010mpAlmSfpDdmWarningPortn"),
        ("EKINOPS-Rm10010mp-MIB", "rm10010mptrapPortNumber"),
        ("EKINOPS-Rm10010mp-MIB", "rm10010mptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    rm10010mpClientTrapNotUrgentGoesOff.setStatus(
        "current"
    )

rm10010mpClientTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 54, 10, 42)
)
rm10010mpClientTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Rm10010mp-MIB", "rm10010mpAlmSfpDdmAlmPortn"),
        ("EKINOPS-Rm10010mp-MIB", "rm10010mptrapPortNumber"),
        ("EKINOPS-Rm10010mp-MIB", "rm10010mptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    rm10010mpClientTrapUrgentGoesOn.setStatus(
        "current"
    )

rm10010mpClientTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 54, 10, 43)
)
rm10010mpClientTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Rm10010mp-MIB", "rm10010mpAlmSfpDdmAlmPortn"),
        ("EKINOPS-Rm10010mp-MIB", "rm10010mptrapPortNumber"),
        ("EKINOPS-Rm10010mp-MIB", "rm10010mptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    rm10010mpClientTrapUrgentGoesOff.setStatus(
        "current"
    )

rm10010mpClientTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 54, 10, 44)
)
rm10010mpClientTrapCritGoesOn.setObjects(
      *(("EKINOPS-Rm10010mp-MIB", "rm10010mpAlmFailAccPortn"),
        ("EKINOPS-Rm10010mp-MIB", "rm10010mpAlmHwFailAccPortn"),
        ("EKINOPS-Rm10010mp-MIB", "rm10010mptrapPortNumber"),
        ("EKINOPS-Rm10010mp-MIB", "rm10010mptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    rm10010mpClientTrapCritGoesOn.setStatus(
        "current"
    )

rm10010mpClientTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 54, 10, 45)
)
rm10010mpClientTrapCritGoesOff.setObjects(
      *(("EKINOPS-Rm10010mp-MIB", "rm10010mpAlmFailAccPortn"),
        ("EKINOPS-Rm10010mp-MIB", "rm10010mpAlmHwFailAccPortn"),
        ("EKINOPS-Rm10010mp-MIB", "rm10010mptrapPortNumber"),
        ("EKINOPS-Rm10010mp-MIB", "rm10010mptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    rm10010mpClientTrapCritGoesOff.setStatus(
        "current"
    )

rm10010mpPowerTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 54, 10, 50)
)
rm10010mpPowerTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Rm10010mp-MIB", "rm10010mpAlmDefFuseB"),
        ("EKINOPS-Rm10010mp-MIB", "rm10010mpAlmDefFuseA"),
        ("EKINOPS-Rm10010mp-MIB", "rm10010mptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    rm10010mpPowerTrapUrgentGoesOn.setStatus(
        "current"
    )

rm10010mpPowerTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 54, 10, 51)
)
rm10010mpPowerTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Rm10010mp-MIB", "rm10010mpAlmDefFuseB"),
        ("EKINOPS-Rm10010mp-MIB", "rm10010mpAlmDefFuseA"),
        ("EKINOPS-Rm10010mp-MIB", "rm10010mptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    rm10010mpPowerTrapUrgentGoesOff.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EKINOPS-Rm10010mp-MIB",
    **{"Rm10010mpMultiRate": Rm10010mpMultiRate,
       "Rm10010mpOtxMode": Rm10010mpOtxMode,
       "Rm10010mpOtxGrid": Rm10010mpOtxGrid,
       "Rm10010mpAdjustValue": Rm10010mpAdjustValue,
       "Rm10010mpClientProtocol": Rm10010mpClientProtocol,
       "Rm10010mpProtocolMode": Rm10010mpProtocolMode,
       "Rm10010mpOtxChannel": Rm10010mpOtxChannel,
       "Rm10010mpOrxChannel": Rm10010mpOrxChannel,
       "moduleRm10010mp": moduleRm10010mp,
       "rm10010mpalarms": rm10010mpalarms,
       "rm10010mpAlmOther": rm10010mpAlmOther,
       "rm10010mpAlmOtherNurg": rm10010mpAlmOtherNurg,
       "rm10010mpAlmsynthAlm2": rm10010mpAlmsynthAlm2,
       "rm10010mpAlmConfTableSave": rm10010mpAlmConfTableSave,
       "rm10010mpAlmInvUpload": rm10010mpAlmInvUpload,
       "rm10010mpAlmConfTableLoad": rm10010mpAlmConfTableLoad,
       "rm10010mpAlmCorrelatOff": rm10010mpAlmCorrelatOff,
       "rm10010mpAlmMaintenanceOn": rm10010mpAlmMaintenanceOn,
       "rm10010mpAlmOtherUrg": rm10010mpAlmOtherUrg,
       "rm10010mpAlmmodFanFail": rm10010mpAlmmodFanFail,
       "rm10010mpAlmFanModuleAbsent": rm10010mpAlmFanModuleAbsent,
       "rm10010mpAlmFansFail": rm10010mpAlmFansFail,
       "rm10010mpAlmFan1Fail": rm10010mpAlmFan1Fail,
       "rm10010mpAlmFan2Fail": rm10010mpAlmFan2Fail,
       "rm10010mpAlmFan3Fail": rm10010mpAlmFan3Fail,
       "rm10010mpAlmFan4Fail": rm10010mpAlmFan4Fail,
       "rm10010mpAlmOtherCrit": rm10010mpAlmOtherCrit,
       "rm10010mpAlmsynthAlm0": rm10010mpAlmsynthAlm0,
       "rm10010mpAlmFailFan": rm10010mpAlmFailFan,
       "rm10010mpAlmModGlobFail": rm10010mpAlmModGlobFail,
       "rm10010mpAlmDefFuseA": rm10010mpAlmDefFuseA,
       "rm10010mpAlmDefFuseB": rm10010mpAlmDefFuseB,
       "rm10010mpAlmclientModuleState": rm10010mpAlmclientModuleState,
       "rm10010mpAlmCfpInitialize": rm10010mpAlmCfpInitialize,
       "rm10010mpAlmCfpLowPower": rm10010mpAlmCfpLowPower,
       "rm10010mpAlmCfpHighPowerUp": rm10010mpAlmCfpHighPowerUp,
       "rm10010mpAlmCfpTxOff": rm10010mpAlmCfpTxOff,
       "rm10010mpAlmCfpTxTurnOn": rm10010mpAlmCfpTxTurnOn,
       "rm10010mpAlmCfpReady": rm10010mpAlmCfpReady,
       "rm10010mpAlmCfpFault": rm10010mpAlmCfpFault,
       "rm10010mpAlmCfpTxTurnOff": rm10010mpAlmCfpTxTurnOff,
       "rm10010mpAlmCfpHighPowerDown": rm10010mpAlmCfpHighPowerDown,
       "rm10010mpAlmclientModuleGeneralStatus": rm10010mpAlmclientModuleGeneralStatus,
       "rm10010mpAlmCfpOutOfAlignment": rm10010mpAlmCfpOutOfAlignment,
       "rm10010mpAlmCfpRxNetworkLol": rm10010mpAlmCfpRxNetworkLol,
       "rm10010mpAlmCfpRxLos": rm10010mpAlmCfpRxLos,
       "rm10010mpAlmCfpTxHostLol": rm10010mpAlmCfpTxHostLol,
       "rm10010mpAlmCfpTxLosf": rm10010mpAlmCfpTxLosf,
       "rm10010mpAlmCfpTxCmuLol": rm10010mpAlmCfpTxCmuLol,
       "rm10010mpAlmCfpTxJitterPllLol": rm10010mpAlmCfpTxJitterPllLol,
       "rm10010mpAlmCfpLossOfRefclk": rm10010mpAlmCfpLossOfRefclk,
       "rm10010mpAlmCfpHwInterlock": rm10010mpAlmCfpHwInterlock,
       "rm10010mpAlmclientGlobalAlarmSummary": rm10010mpAlmclientGlobalAlarmSummary,
       "rm10010mpAlmCfpSoftGlobAlarmTest": rm10010mpAlmCfpSoftGlobAlarmTest,
       "rm10010mpAlmCfpNetworkLaneAlarmWarning2": rm10010mpAlmCfpNetworkLaneAlarmWarning2,
       "rm10010mpAlmCfpModuleState": rm10010mpAlmCfpModuleState,
       "rm10010mpAlmCfpModuleGeneralStatus": rm10010mpAlmCfpModuleGeneralStatus,
       "rm10010mpAlmCfpModuleFault": rm10010mpAlmCfpModuleFault,
       "rm10010mpAlmCfpModuleAlarmWarning1": rm10010mpAlmCfpModuleAlarmWarning1,
       "rm10010mpAlmCfpModuleAlarmWarning2": rm10010mpAlmCfpModuleAlarmWarning2,
       "rm10010mpAlmCfpNetworkLaneAlarmWarning1": rm10010mpAlmCfpNetworkLaneAlarmWarning1,
       "rm10010mpAlmCfpNetworkLaneFaultStatus": rm10010mpAlmCfpNetworkLaneFaultStatus,
       "rm10010mpAlmCfpHostLaneFaultStatus": rm10010mpAlmCfpHostLaneFaultStatus,
       "rm10010mpAlmCfpGlobAlarmAssertion": rm10010mpAlmCfpGlobAlarmAssertion,
       "rm10010mpAlmmsaModuleState": rm10010mpAlmmsaModuleState,
       "rm10010mpAlmMsaInitialize": rm10010mpAlmMsaInitialize,
       "rm10010mpAlmMsaLowPower": rm10010mpAlmMsaLowPower,
       "rm10010mpAlmMsaHighPowerUp": rm10010mpAlmMsaHighPowerUp,
       "rm10010mpAlmMsaTxOff": rm10010mpAlmMsaTxOff,
       "rm10010mpAlmMsaTxTurnOn": rm10010mpAlmMsaTxTurnOn,
       "rm10010mpAlmMsaReady": rm10010mpAlmMsaReady,
       "rm10010mpAlmMsaFault": rm10010mpAlmMsaFault,
       "rm10010mpAlmMsaTxTurnOff": rm10010mpAlmMsaTxTurnOff,
       "rm10010mpAlmMsaHighPowerDown": rm10010mpAlmMsaHighPowerDown,
       "rm10010mpAlmmsaModuleGeneralStatus": rm10010mpAlmmsaModuleGeneralStatus,
       "rm10010mpAlmMsaOutOfAlignment": rm10010mpAlmMsaOutOfAlignment,
       "rm10010mpAlmMsaRxNetworkLol": rm10010mpAlmMsaRxNetworkLol,
       "rm10010mpAlmMsaRxLos": rm10010mpAlmMsaRxLos,
       "rm10010mpAlmMsaTxHostLol": rm10010mpAlmMsaTxHostLol,
       "rm10010mpAlmMsaTxLosf": rm10010mpAlmMsaTxLosf,
       "rm10010mpAlmMsaTxCmuLol": rm10010mpAlmMsaTxCmuLol,
       "rm10010mpAlmMsaTxJitterPllLol": rm10010mpAlmMsaTxJitterPllLol,
       "rm10010mpAlmMsaLossOfRefclk": rm10010mpAlmMsaLossOfRefclk,
       "rm10010mpAlmMsaHwInterlock": rm10010mpAlmMsaHwInterlock,
       "rm10010mpAlmmsaGlobalAlarmSummary": rm10010mpAlmmsaGlobalAlarmSummary,
       "rm10010mpAlmMsaSoftGlobAlarmTest": rm10010mpAlmMsaSoftGlobAlarmTest,
       "rm10010mpAlmMsaNetworkHostAlarmStatus": rm10010mpAlmMsaNetworkHostAlarmStatus,
       "rm10010mpAlmMsaNetworkLaneAlarmWarning2": rm10010mpAlmMsaNetworkLaneAlarmWarning2,
       "rm10010mpAlmMsaModuleState": rm10010mpAlmMsaModuleState,
       "rm10010mpAlmMsaModuleGeneralStatus": rm10010mpAlmMsaModuleGeneralStatus,
       "rm10010mpAlmModuleFault": rm10010mpAlmModuleFault,
       "rm10010mpAlmMsaModuleAlarmWarning1": rm10010mpAlmMsaModuleAlarmWarning1,
       "rm10010mpAlmMsaModuleAlarmWarning2": rm10010mpAlmMsaModuleAlarmWarning2,
       "rm10010mpAlmMsaNetworkLaneAlarmWarning1": rm10010mpAlmMsaNetworkLaneAlarmWarning1,
       "rm10010mpAlmMsaNetworkLaneFaultStatus": rm10010mpAlmMsaNetworkLaneFaultStatus,
       "rm10010mpAlmMsaHostLaneFaultStatus": rm10010mpAlmMsaHostLaneFaultStatus,
       "rm10010mpAlmMsaGlobAlarmAssertion": rm10010mpAlmMsaGlobAlarmAssertion,
       "rm10010mpAlmmsaNetworkTxAlignment": rm10010mpAlmmsaNetworkTxAlignment,
       "rm10010mpAlmNetTxTimingFault": rm10010mpAlmNetTxTimingFault,
       "rm10010mpAlmNetTxReferenceClockFault": rm10010mpAlmNetTxReferenceClockFault,
       "rm10010mpAlmNetTxCmuLockFault": rm10010mpAlmNetTxCmuLockFault,
       "rm10010mpAlmNetTxOutOfAlignment": rm10010mpAlmNetTxOutOfAlignment,
       "rm10010mpAlmNetTxLossOfAlignment": rm10010mpAlmNetTxLossOfAlignment,
       "rm10010mpAlmmsaNetworkRxAlignment": rm10010mpAlmmsaNetworkRxAlignment,
       "rm10010mpAlmNetRxTimingFault": rm10010mpAlmNetRxTimingFault,
       "rm10010mpAlmNetRxOutOfAlignment": rm10010mpAlmNetRxOutOfAlignment,
       "rm10010mpAlmNetRxLossOfAlignment": rm10010mpAlmNetRxLossOfAlignment,
       "rm10010mpAlmNetRxModemLockFault": rm10010mpAlmNetRxModemLockFault,
       "rm10010mpAlmNetRxModemSyncDetectFault": rm10010mpAlmNetRxModemSyncDetectFault,
       "rm10010mpAlmmsaNetworkHostNetworkAlarmSummary": rm10010mpAlmmsaNetworkHostNetworkAlarmSummary,
       "rm10010mpAlmNetworkTxAlignment": rm10010mpAlmNetworkTxAlignment,
       "rm10010mpAlmNetworkRxAlignment": rm10010mpAlmNetworkRxAlignment,
       "rm10010mpAlmNetworkRxOtn": rm10010mpAlmNetworkRxOtn,
       "rm10010mpAlmHostRxAlignment": rm10010mpAlmHostRxAlignment,
       "rm10010mpAlmHostTxAlignment": rm10010mpAlmHostTxAlignment,
       "rm10010mpAlmHostTxOtnStatus": rm10010mpAlmHostTxOtnStatus,
       "rm10010mpAlmmsaHostTxAlignment": rm10010mpAlmmsaHostTxAlignment,
       "rm10010mpAlmHostTxDeskewLockFault": rm10010mpAlmHostTxDeskewLockFault,
       "rm10010mpAlmHostTxOutOfAlignment": rm10010mpAlmHostTxOutOfAlignment,
       "rm10010mpAlmHostTxLossOfAlignment": rm10010mpAlmHostTxLossOfAlignment,
       "rm10010mpAlmHostTxCdrLockFault": rm10010mpAlmHostTxCdrLockFault,
       "rm10010mpAlmmsaHostRxAlignment": rm10010mpAlmmsaHostRxAlignment,
       "rm10010mpAlmHostRxCmuLockFault": rm10010mpAlmHostRxCmuLockFault,
       "rm10010mpAlmHostRxOutOfAlignment": rm10010mpAlmHostRxOutOfAlignment,
       "rm10010mpAlmHostRxLossOfAlignment": rm10010mpAlmHostRxLossOfAlignment,
       "rm10010mpAlmClient": rm10010mpAlmClient,
       "rm10010mpAlmClientNurg": rm10010mpAlmClientNurg,
       "rm10010mpAlmclientNetworkLaneAlarmWarningTable": rm10010mpAlmclientNetworkLaneAlarmWarningTable,
       "rm10010mpAlmclientNetworkLaneAlarmWarningEntry": rm10010mpAlmclientNetworkLaneAlarmWarningEntry,
       "rm10010mpAlmclientNetworkLaneAlarmWarningIndex": rm10010mpAlmclientNetworkLaneAlarmWarningIndex,
       "rm10010mpAlmClientRxPowerLowAlarmPortn": rm10010mpAlmClientRxPowerLowAlarmPortn,
       "rm10010mpAlmClientRxPowerLowWarningPortn": rm10010mpAlmClientRxPowerLowWarningPortn,
       "rm10010mpAlmClientRxPowerHighWarningPortn": rm10010mpAlmClientRxPowerHighWarningPortn,
       "rm10010mpAlmClientRxPowerHighAlarmPortn": rm10010mpAlmClientRxPowerHighAlarmPortn,
       "rm10010mpAlmLaserTempLowAlarmPortn": rm10010mpAlmLaserTempLowAlarmPortn,
       "rm10010mpAlmClientLaserTempLowWarningPortn": rm10010mpAlmClientLaserTempLowWarningPortn,
       "rm10010mpAlmClientLaserTempHighWarningPortn": rm10010mpAlmClientLaserTempHighWarningPortn,
       "rm10010mpAlmClientLaserTempHighAlarmPortn": rm10010mpAlmClientLaserTempHighAlarmPortn,
       "rm10010mpAlmClientTxPowerLowAlarmPortn": rm10010mpAlmClientTxPowerLowAlarmPortn,
       "rm10010mpAlmClientTxPowerLowWarningPortn": rm10010mpAlmClientTxPowerLowWarningPortn,
       "rm10010mpAlmClientTxPowerHighWarningPortn": rm10010mpAlmClientTxPowerHighWarningPortn,
       "rm10010mpAlmClientTxPowerHighAlarmPortn": rm10010mpAlmClientTxPowerHighAlarmPortn,
       "rm10010mpAlmClientBiasLowAlarmPortn": rm10010mpAlmClientBiasLowAlarmPortn,
       "rm10010mpAlmClientBiasLowWarningPortn": rm10010mpAlmClientBiasLowWarningPortn,
       "rm10010mpAlmClientBiasHighWarningPortn": rm10010mpAlmClientBiasHighWarningPortn,
       "rm10010mpAlmClientBiasHighAlarmPortn": rm10010mpAlmClientBiasHighAlarmPortn,
       "rm10010mpAlmclientSfpWarnDdmTable": rm10010mpAlmclientSfpWarnDdmTable,
       "rm10010mpAlmclientSfpWarnDdmEntry": rm10010mpAlmclientSfpWarnDdmEntry,
       "rm10010mpAlmclientSfpWarnDdmIndex": rm10010mpAlmclientSfpWarnDdmIndex,
       "rm10010mpAlmTxPwLowWngPortn": rm10010mpAlmTxPwLowWngPortn,
       "rm10010mpAlmTxPwrHighWngPortn": rm10010mpAlmTxPwrHighWngPortn,
       "rm10010mpAlmTxBiasLowWngPortn": rm10010mpAlmTxBiasLowWngPortn,
       "rm10010mpAlmTxBiasHighWngPortn": rm10010mpAlmTxBiasHighWngPortn,
       "rm10010mpAlmVccLowWngPortn": rm10010mpAlmVccLowWngPortn,
       "rm10010mpAlmVccHighWngPortn": rm10010mpAlmVccHighWngPortn,
       "rm10010mpAlmTempLowWngPortn": rm10010mpAlmTempLowWngPortn,
       "rm10010mpAlmTempHighWngPortn": rm10010mpAlmTempHighWngPortn,
       "rm10010mpAlmRxPwrLowWngPortn": rm10010mpAlmRxPwrLowWngPortn,
       "rm10010mpAlmRxPwrHighWngPortn": rm10010mpAlmRxPwrHighWngPortn,
       "rm10010mpAlmClientUrg": rm10010mpAlmClientUrg,
       "rm10010mpAlmclientNetworkLaneFaultTable": rm10010mpAlmclientNetworkLaneFaultTable,
       "rm10010mpAlmclientNetworkLaneFaultEntry": rm10010mpAlmclientNetworkLaneFaultEntry,
       "rm10010mpAlmclientNetworkLaneFaultIndex": rm10010mpAlmclientNetworkLaneFaultIndex,
       "rm10010mpAlmClientLaneRxFifoErrorPortn": rm10010mpAlmClientLaneRxFifoErrorPortn,
       "rm10010mpAlmClientLaneRxLolPortn": rm10010mpAlmClientLaneRxLolPortn,
       "rm10010mpAlmClientLaneRxLosPortn": rm10010mpAlmClientLaneRxLosPortn,
       "rm10010mpAlmClientLaneTxLolPortn": rm10010mpAlmClientLaneTxLolPortn,
       "rm10010mpAlmClientLaneTxLosfPortn": rm10010mpAlmClientLaneTxLosfPortn,
       "rm10010mpAlmClientLaneApdPowerSupplyPortn": rm10010mpAlmClientLaneApdPowerSupplyPortn,
       "rm10010mpAlmClientLaneWavelengthUnlockedPortn": rm10010mpAlmClientLaneWavelengthUnlockedPortn,
       "rm10010mpAlmClientLaneTecFaultPortn": rm10010mpAlmClientLaneTecFaultPortn,
       "rm10010mpAlmclientHostLaneFaultTable": rm10010mpAlmclientHostLaneFaultTable,
       "rm10010mpAlmclientHostLaneFaultEntry": rm10010mpAlmclientHostLaneFaultEntry,
       "rm10010mpAlmclientHostLaneFaultIndex": rm10010mpAlmclientHostLaneFaultIndex,
       "rm10010mpAlmClientLossOfSyncPortn": rm10010mpAlmClientLossOfSyncPortn,
       "rm10010mpAlmClientInputLossOfSigPortn": rm10010mpAlmClientInputLossOfSigPortn,
       "rm10010mpAlmClientLanesMarkerUnlockPortn": rm10010mpAlmClientLanesMarkerUnlockPortn,
       "rm10010mpAlmClientLanes6466UnlockPortn": rm10010mpAlmClientLanes6466UnlockPortn,
       "rm10010mpAlmClientLanesNotAlignedPortn": rm10010mpAlmClientLanesNotAlignedPortn,
       "rm10010mpAlmClientCsfDetectedPortn": rm10010mpAlmClientCsfDetectedPortn,
       "rm10010mpAlmClientTxHostLolPortn": rm10010mpAlmClientTxHostLolPortn,
       "rm10010mpAlmClientLaneTxFifoErrorPortn": rm10010mpAlmClientLaneTxFifoErrorPortn,
       "rm10010mpAlmclientSfpAlmDdmTable": rm10010mpAlmclientSfpAlmDdmTable,
       "rm10010mpAlmclientSfpAlmDdmEntry": rm10010mpAlmclientSfpAlmDdmEntry,
       "rm10010mpAlmclientSfpAlmDdmIndex": rm10010mpAlmclientSfpAlmDdmIndex,
       "rm10010mpAlmTxPwrLowAlaPortn": rm10010mpAlmTxPwrLowAlaPortn,
       "rm10010mpAlmTxPwrHighAlaPortn": rm10010mpAlmTxPwrHighAlaPortn,
       "rm10010mpAlmTxBiasLowAlaPortn": rm10010mpAlmTxBiasLowAlaPortn,
       "rm10010mpAlmTxBiasHighAlaPortn": rm10010mpAlmTxBiasHighAlaPortn,
       "rm10010mpAlmVccLowAlaPortn": rm10010mpAlmVccLowAlaPortn,
       "rm10010mpAlmVccHighAlaPortn": rm10010mpAlmVccHighAlaPortn,
       "rm10010mpAlmTempLowAlaPortn": rm10010mpAlmTempLowAlaPortn,
       "rm10010mpAlmTempHighAlaPortn": rm10010mpAlmTempHighAlaPortn,
       "rm10010mpAlmRxPwrLowAlaPortn": rm10010mpAlmRxPwrLowAlaPortn,
       "rm10010mpAlmRxPwrHighAlaPortn": rm10010mpAlmRxPwrHighAlaPortn,
       "rm10010mpAlmClientCrit": rm10010mpAlmClientCrit,
       "rm10010mpAlmsynthAlmPortTable": rm10010mpAlmsynthAlmPortTable,
       "rm10010mpAlmsynthAlmPortEntry": rm10010mpAlmsynthAlmPortEntry,
       "rm10010mpAlmsynthAlmPortIndex": rm10010mpAlmsynthAlmPortIndex,
       "rm10010mpAlmSfpAbsentPortn": rm10010mpAlmSfpAbsentPortn,
       "rm10010mpAlmDdmAbsentPortn": rm10010mpAlmDdmAbsentPortn,
       "rm10010mpAlmHwFailAccPortn": rm10010mpAlmHwFailAccPortn,
       "rm10010mpAlmDwLsdPortn": rm10010mpAlmDwLsdPortn,
       "rm10010mpAlmClientLocalOosPortn": rm10010mpAlmClientLocalOosPortn,
       "rm10010mpAlmClientRemoteOosPortn": rm10010mpAlmClientRemoteOosPortn,
       "rm10010mpAlmDwCaisPortn": rm10010mpAlmDwCaisPortn,
       "rm10010mpAlmSfpDdmWarningPortn": rm10010mpAlmSfpDdmWarningPortn,
       "rm10010mpAlmSfpDdmAlmPortn": rm10010mpAlmSfpDdmAlmPortn,
       "rm10010mpAlmFailAccPortn": rm10010mpAlmFailAccPortn,
       "rm10010mpAlmUpCsfPortn": rm10010mpAlmUpCsfPortn,
       "rm10010mpAlmLine": rm10010mpAlmLine,
       "rm10010mpAlmLineNurg": rm10010mpAlmLineNurg,
       "rm10010mpAlmlineNetworkLaneAlarmWarning1Table": rm10010mpAlmlineNetworkLaneAlarmWarning1Table,
       "rm10010mpAlmlineNetworkLaneAlarmWarning1Entry": rm10010mpAlmlineNetworkLaneAlarmWarning1Entry,
       "rm10010mpAlmlineNetworkLaneAlarmWarning1Index": rm10010mpAlmlineNetworkLaneAlarmWarning1Index,
       "rm10010mpAlmLineRxPowerLowAlarmPortn": rm10010mpAlmLineRxPowerLowAlarmPortn,
       "rm10010mpAlmLineRxPowerLowWarningPortn": rm10010mpAlmLineRxPowerLowWarningPortn,
       "rm10010mpAlmLineRxPowerHighWarningPortn": rm10010mpAlmLineRxPowerHighWarningPortn,
       "rm10010mpAlmLineRxPowerHighAlarmPortn": rm10010mpAlmLineRxPowerHighAlarmPortn,
       "rm10010mpAlmLineLaserTempLowAlarmPortn": rm10010mpAlmLineLaserTempLowAlarmPortn,
       "rm10010mpAlmLineLaserTempLowWarningPortn": rm10010mpAlmLineLaserTempLowWarningPortn,
       "rm10010mpAlmLineLaserTempHighWarningPortn": rm10010mpAlmLineLaserTempHighWarningPortn,
       "rm10010mpAlmLineLaserTempHighAlarmPortn": rm10010mpAlmLineLaserTempHighAlarmPortn,
       "rm10010mpAlmLineTxPowerLowAlarmPortn": rm10010mpAlmLineTxPowerLowAlarmPortn,
       "rm10010mpAlmLineTxPowerLowWarningPortn": rm10010mpAlmLineTxPowerLowWarningPortn,
       "rm10010mpAlmLineTxPowerHighWarningPortn": rm10010mpAlmLineTxPowerHighWarningPortn,
       "rm10010mpAlmLineTxPowerHighAlarmPortn": rm10010mpAlmLineTxPowerHighAlarmPortn,
       "rm10010mpAlmLineBiasLowAlarmPortn": rm10010mpAlmLineBiasLowAlarmPortn,
       "rm10010mpAlmLineBiasLowWarningPortn": rm10010mpAlmLineBiasLowWarningPortn,
       "rm10010mpAlmLineBiasHighWarningPortn": rm10010mpAlmLineBiasHighWarningPortn,
       "rm10010mpAlmLineBiasHighAlarmPortn": rm10010mpAlmLineBiasHighAlarmPortn,
       "rm10010mpAlmlineNetworkLaneAlarmWarning2Table": rm10010mpAlmlineNetworkLaneAlarmWarning2Table,
       "rm10010mpAlmlineNetworkLaneAlarmWarning2Entry": rm10010mpAlmlineNetworkLaneAlarmWarning2Entry,
       "rm10010mpAlmlineNetworkLaneAlarmWarning2Index": rm10010mpAlmlineNetworkLaneAlarmWarning2Index,
       "rm10010mpAlmTxModulatorBiasLowAlarmPortn": rm10010mpAlmTxModulatorBiasLowAlarmPortn,
       "rm10010mpAlmTxModulatorBiasLowWarningPortn": rm10010mpAlmTxModulatorBiasLowWarningPortn,
       "rm10010mpAlmTxModulatorBiasHighWarningPortn": rm10010mpAlmTxModulatorBiasHighWarningPortn,
       "rm10010mpAlmTxModulatorBiasHighAlarmPortn": rm10010mpAlmTxModulatorBiasHighAlarmPortn,
       "rm10010mpAlmRxLaserTempLowAlarmPortn": rm10010mpAlmRxLaserTempLowAlarmPortn,
       "rm10010mpAlmRxLaserTempLowWarningPortn": rm10010mpAlmRxLaserTempLowWarningPortn,
       "rm10010mpAlmRxLaserTempHighWarningPortn": rm10010mpAlmRxLaserTempHighWarningPortn,
       "rm10010mpAlmRxLaserTempHighAlarmPortn": rm10010mpAlmRxLaserTempHighAlarmPortn,
       "rm10010mpAlmRxLaserOutputLowAlarmPortn": rm10010mpAlmRxLaserOutputLowAlarmPortn,
       "rm10010mpAlmRxLaserOutputLowWarningPortn": rm10010mpAlmRxLaserOutputLowWarningPortn,
       "rm10010mpAlmRxLaserOutputHighWarningPortn": rm10010mpAlmRxLaserOutputHighWarningPortn,
       "rm10010mpAlmRxLaserOutputHighAlarmPortn": rm10010mpAlmRxLaserOutputHighAlarmPortn,
       "rm10010mpAlmRxLaserBiasLowAlarmPortn": rm10010mpAlmRxLaserBiasLowAlarmPortn,
       "rm10010mpAlmRxLaserBiasLowWarningPortn": rm10010mpAlmRxLaserBiasLowWarningPortn,
       "rm10010mpAlmRxLaserBiasHighWarningPortn": rm10010mpAlmRxLaserBiasHighWarningPortn,
       "rm10010mpAlmRxLaserBiasHighAlarmPortn": rm10010mpAlmRxLaserBiasHighAlarmPortn,
       "rm10010mpAlmLineUrg": rm10010mpAlmLineUrg,
       "rm10010mpAlmlineNetworkLaneFaultTable": rm10010mpAlmlineNetworkLaneFaultTable,
       "rm10010mpAlmlineNetworkLaneFaultEntry": rm10010mpAlmlineNetworkLaneFaultEntry,
       "rm10010mpAlmlineNetworkLaneFaultIndex": rm10010mpAlmlineNetworkLaneFaultIndex,
       "rm10010mpAlmLineLaneRxTecFaultPortn": rm10010mpAlmLineLaneRxTecFaultPortn,
       "rm10010mpAlmLineLaneRxFifoErrorPortn": rm10010mpAlmLineLaneRxFifoErrorPortn,
       "rm10010mpAlmLineLaneRxLolPortn": rm10010mpAlmLineLaneRxLolPortn,
       "rm10010mpAlmLineLaneRxLosPortn": rm10010mpAlmLineLaneRxLosPortn,
       "rm10010mpAlmLineLaneTxLolPortn": rm10010mpAlmLineLaneTxLolPortn,
       "rm10010mpAlmLineLaneTxLosfPortn": rm10010mpAlmLineLaneTxLosfPortn,
       "rm10010mpAlmLineLaneApdPowerSupplyPortn": rm10010mpAlmLineLaneApdPowerSupplyPortn,
       "rm10010mpAlmLineLaneWavelengthUnlockedPortn": rm10010mpAlmLineLaneWavelengthUnlockedPortn,
       "rm10010mpAlmLineLaneTecFaultPortn": rm10010mpAlmLineLaneTecFaultPortn,
       "rm10010mpAlmlineHostLaneFaultTable": rm10010mpAlmlineHostLaneFaultTable,
       "rm10010mpAlmlineHostLaneFaultEntry": rm10010mpAlmlineHostLaneFaultEntry,
       "rm10010mpAlmlineHostLaneFaultIndex": rm10010mpAlmlineHostLaneFaultIndex,
       "rm10010mpAlmLineInputLossOfSignalPortn": rm10010mpAlmLineInputLossOfSignalPortn,
       "rm10010mpAlmLineLossOfFramePortn": rm10010mpAlmLineLossOfFramePortn,
       "rm10010mpAlmLineSmBdiInsertedPortn": rm10010mpAlmLineSmBdiInsertedPortn,
       "rm10010mpAlmLineSmBdiDetectedPortn": rm10010mpAlmLineSmBdiDetectedPortn,
       "rm10010mpAlmLineSmIaeInsertedPortn": rm10010mpAlmLineSmIaeInsertedPortn,
       "rm10010mpAlmLineSmIaeDetectedPortn": rm10010mpAlmLineSmIaeDetectedPortn,
       "rm10010mpAlmLineTxHostLolPortn": rm10010mpAlmLineTxHostLolPortn,
       "rm10010mpAlmLineLaneTxFifoErrorPortn": rm10010mpAlmLineLaneTxFifoErrorPortn,
       "rm10010mpAlmlineNetworkLaneRxOtnTable": rm10010mpAlmlineNetworkLaneRxOtnTable,
       "rm10010mpAlmlineNetworkLaneRxOtnEntry": rm10010mpAlmlineNetworkLaneRxOtnEntry,
       "rm10010mpAlmlineNetworkLaneRxOtnIndex": rm10010mpAlmlineNetworkLaneRxOtnIndex,
       "rm10010mpAlmLineRxOtnOduAisPortn": rm10010mpAlmLineRxOtnOduAisPortn,
       "rm10010mpAlmLineRxOtnOtuAisPortn": rm10010mpAlmLineRxOtnOtuAisPortn,
       "rm10010mpAlmLineRxSmBdiPortn": rm10010mpAlmLineRxSmBdiPortn,
       "rm10010mpAlmLineRxOtnIaePortn": rm10010mpAlmLineRxOtnIaePortn,
       "rm10010mpAlmLineRxOtnOomPortn": rm10010mpAlmLineRxOtnOomPortn,
       "rm10010mpAlmLineRxOtnLomPortn": rm10010mpAlmLineRxOtnLomPortn,
       "rm10010mpAlmLineRxOtnOofPortn": rm10010mpAlmLineRxOtnOofPortn,
       "rm10010mpAlmLineRxOtnLofPortn": rm10010mpAlmLineRxOtnLofPortn,
       "rm10010mpAlmlineHostLaneTxOtnTable": rm10010mpAlmlineHostLaneTxOtnTable,
       "rm10010mpAlmlineHostLaneTxOtnEntry": rm10010mpAlmlineHostLaneTxOtnEntry,
       "rm10010mpAlmlineHostLaneTxOtnIndex": rm10010mpAlmlineHostLaneTxOtnIndex,
       "rm10010mpAlmLineTxOtnOduAisPortn": rm10010mpAlmLineTxOtnOduAisPortn,
       "rm10010mpAlmLineTxOtnOtuAisPortn": rm10010mpAlmLineTxOtnOtuAisPortn,
       "rm10010mpAlmLineTxSmBdiPortn": rm10010mpAlmLineTxSmBdiPortn,
       "rm10010mpAlmLineTxOtnIaePortn": rm10010mpAlmLineTxOtnIaePortn,
       "rm10010mpAlmLineTxOtnOomPortn": rm10010mpAlmLineTxOtnOomPortn,
       "rm10010mpAlmLineTxOtnLomPortn": rm10010mpAlmLineTxOtnLomPortn,
       "rm10010mpAlmLineTxOtnOofPortn": rm10010mpAlmLineTxOtnOofPortn,
       "rm10010mpAlmLineTxOtnLofPortn": rm10010mpAlmLineTxOtnLofPortn,
       "rm10010mpAlmLineCrit": rm10010mpAlmLineCrit,
       "rm10010mpAlmsynthAlmLineTable": rm10010mpAlmsynthAlmLineTable,
       "rm10010mpAlmsynthAlmLineEntry": rm10010mpAlmsynthAlmLineEntry,
       "rm10010mpAlmsynthAlmLineIndex": rm10010mpAlmsynthAlmLineIndex,
       "rm10010mpAlmXfpAbsentPortn": rm10010mpAlmXfpAbsentPortn,
       "rm10010mpAlmXfpInitNotComplPortn": rm10010mpAlmXfpInitNotComplPortn,
       "rm10010mpAlmLineHwFailPortn": rm10010mpAlmLineHwFailPortn,
       "rm10010mpAlmXfpTxOffPortn": rm10010mpAlmXfpTxOffPortn,
       "rm10010mpAlmLineLocalOosPortn": rm10010mpAlmLineLocalOosPortn,
       "rm10010mpAlmUpRdiInsPortn": rm10010mpAlmUpRdiInsPortn,
       "rm10010mpAlmLineDdmWarningPortn": rm10010mpAlmLineDdmWarningPortn,
       "rm10010mpAlmLineDdmAlmPortn": rm10010mpAlmLineDdmAlmPortn,
       "rm10010mpAlmLineFailPortn": rm10010mpAlmLineFailPortn,
       "rm10010mpAlmLineActivePortn": rm10010mpAlmLineActivePortn,
       "rm10010mpmeasures": rm10010mpmeasures,
       "rm10010mpMesrOther": rm10010mpMesrOther,
       "rm10010mpMesrsynth0": rm10010mpMesrsynth0,
       "rm10010mpMesrsynth1": rm10010mpMesrsynth1,
       "rm10010mpMesrpmIntervalNumber": rm10010mpMesrpmIntervalNumber,
       "rm10010mpMesrlineNetTxLaserOutputPwrAverage": rm10010mpMesrlineNetTxLaserOutputPwrAverage,
       "rm10010mpMesrlineNetTxLaserTempAverage": rm10010mpMesrlineNetTxLaserTempAverage,
       "rm10010mpMesrlineNetTxBiasCurrentAverage": rm10010mpMesrlineNetTxBiasCurrentAverage,
       "rm10010mpMesrlineNetRxInputPwrAverage": rm10010mpMesrlineNetRxInputPwrAverage,
       "rm10010mpMesrlineResidualChromaticDispAverage": rm10010mpMesrlineResidualChromaticDispAverage,
       "rm10010mpMesrlineDiffGroupDelayAverage": rm10010mpMesrlineDiffGroupDelayAverage,
       "rm10010mpMesrlineQFactorAverage": rm10010mpMesrlineQFactorAverage,
       "rm10010mpMesrlineCarrierFreqOffsetAverage": rm10010mpMesrlineCarrierFreqOffsetAverage,
       "rm10010mpMesrlineOsnrAverage": rm10010mpMesrlineOsnrAverage,
       "rm10010mpMesrclientNetTxTempMin": rm10010mpMesrclientNetTxTempMin,
       "rm10010mpMesrclientNetTxBiasMin": rm10010mpMesrclientNetTxBiasMin,
       "rm10010mpMesrclientNetTxPwrMin": rm10010mpMesrclientNetTxPwrMin,
       "rm10010mpMesrclientNetRxPwrMin": rm10010mpMesrclientNetRxPwrMin,
       "rm10010mpMesrlineNetTxLaserOutputPwrMin": rm10010mpMesrlineNetTxLaserOutputPwrMin,
       "rm10010mpMesrlineNetTxLaserTempMin": rm10010mpMesrlineNetTxLaserTempMin,
       "rm10010mpMesrlineNetTxBiasCurrentMin": rm10010mpMesrlineNetTxBiasCurrentMin,
       "rm10010mpMesrlineNetRxInputPwrMin": rm10010mpMesrlineNetRxInputPwrMin,
       "rm10010mpMesrlineResidualChromaticDispMin": rm10010mpMesrlineResidualChromaticDispMin,
       "rm10010mpMesrlineDiffGroupDelayMin": rm10010mpMesrlineDiffGroupDelayMin,
       "rm10010mpMesrlineQFactorMin": rm10010mpMesrlineQFactorMin,
       "rm10010mpMesrlineCarrierFreqOffsetMin": rm10010mpMesrlineCarrierFreqOffsetMin,
       "rm10010mpMesrlineOsnrMin": rm10010mpMesrlineOsnrMin,
       "rm10010mpMesrclientNetTxTempMax": rm10010mpMesrclientNetTxTempMax,
       "rm10010mpMesrclientNetTxBiasMax": rm10010mpMesrclientNetTxBiasMax,
       "rm10010mpMesrclientNetTxPwrMax": rm10010mpMesrclientNetTxPwrMax,
       "rm10010mpMesrclientNetRxPwrMax": rm10010mpMesrclientNetRxPwrMax,
       "rm10010mpMesrlineNetTxLaserOutputPwrMax": rm10010mpMesrlineNetTxLaserOutputPwrMax,
       "rm10010mpMesrlineNetTxLaserTempMax": rm10010mpMesrlineNetTxLaserTempMax,
       "rm10010mpMesrlineNetTxBiasCurrentMax": rm10010mpMesrlineNetTxBiasCurrentMax,
       "rm10010mpMesrlineNetRxInputPwrMax": rm10010mpMesrlineNetRxInputPwrMax,
       "rm10010mpMesrlineResidualChromaticDispMax": rm10010mpMesrlineResidualChromaticDispMax,
       "rm10010mpMesrlineDiffGroupDelayMax": rm10010mpMesrlineDiffGroupDelayMax,
       "rm10010mpMesrlineQFactorMax": rm10010mpMesrlineQFactorMax,
       "rm10010mpMesrlineCarrierFreqOffsetMax": rm10010mpMesrlineCarrierFreqOffsetMax,
       "rm10010mpMesrlineOsnrMax": rm10010mpMesrlineOsnrMax,
       "rm10010mpMesrClient": rm10010mpMesrClient,
       "rm10010mpMesrclientCfpTemp": rm10010mpMesrclientCfpTemp,
       "rm10010mpMesrclientCfp3v3Voltage": rm10010mpMesrclientCfp3v3Voltage,
       "rm10010mpMesrclientSoaBiasCurrent": rm10010mpMesrclientSoaBiasCurrent,
       "rm10010mpMesrclientNetTxTempTable": rm10010mpMesrclientNetTxTempTable,
       "rm10010mpMesrclientNetTxTempEntry": rm10010mpMesrclientNetTxTempEntry,
       "rm10010mpMesrclientNetTxTempIndex": rm10010mpMesrclientNetTxTempIndex,
       "rm10010mpMesrclientNetTxTempPortn": rm10010mpMesrclientNetTxTempPortn,
       "rm10010mpMesrclientNetTxBiasTable": rm10010mpMesrclientNetTxBiasTable,
       "rm10010mpMesrclientNetTxBiasEntry": rm10010mpMesrclientNetTxBiasEntry,
       "rm10010mpMesrclientNetTxBiasIndex": rm10010mpMesrclientNetTxBiasIndex,
       "rm10010mpMesrclientNetTxBiasPortn": rm10010mpMesrclientNetTxBiasPortn,
       "rm10010mpMesrclientNetTxPwrTable": rm10010mpMesrclientNetTxPwrTable,
       "rm10010mpMesrclientNetTxPwrEntry": rm10010mpMesrclientNetTxPwrEntry,
       "rm10010mpMesrclientNetTxPwrIndex": rm10010mpMesrclientNetTxPwrIndex,
       "rm10010mpMesrclientNetTxPwrPortn": rm10010mpMesrclientNetTxPwrPortn,
       "rm10010mpMesrclientNetRxPwrTable": rm10010mpMesrclientNetRxPwrTable,
       "rm10010mpMesrclientNetRxPwrEntry": rm10010mpMesrclientNetRxPwrEntry,
       "rm10010mpMesrclientNetRxPwrIndex": rm10010mpMesrclientNetRxPwrIndex,
       "rm10010mpMesrclientNetRxPwrPortn": rm10010mpMesrclientNetRxPwrPortn,
       "rm10010mpMesrLine": rm10010mpMesrLine,
       "rm10010mpMesrlineMsaTemp": rm10010mpMesrlineMsaTemp,
       "rm10010mpMesrlineMsa3v3Voltage": rm10010mpMesrlineMsa3v3Voltage,
       "rm10010mpMesrlineSoaBiasCurrent": rm10010mpMesrlineSoaBiasCurrent,
       "rm10010mpMesrlineNetTxLaserOutputPwrTable": rm10010mpMesrlineNetTxLaserOutputPwrTable,
       "rm10010mpMesrlineNetTxLaserOutputPwrEntry": rm10010mpMesrlineNetTxLaserOutputPwrEntry,
       "rm10010mpMesrlineNetTxLaserOutputPwrIndex": rm10010mpMesrlineNetTxLaserOutputPwrIndex,
       "rm10010mpMesrlineNetTxLaserOutputPwrPortn": rm10010mpMesrlineNetTxLaserOutputPwrPortn,
       "rm10010mpMesrlineNetTxLaserTempTable": rm10010mpMesrlineNetTxLaserTempTable,
       "rm10010mpMesrlineNetTxLaserTempEntry": rm10010mpMesrlineNetTxLaserTempEntry,
       "rm10010mpMesrlineNetTxLaserTempIndex": rm10010mpMesrlineNetTxLaserTempIndex,
       "rm10010mpMesrlineNetTxLaserTempPortn": rm10010mpMesrlineNetTxLaserTempPortn,
       "rm10010mpMesrlineNetTxBiasCurrentTable": rm10010mpMesrlineNetTxBiasCurrentTable,
       "rm10010mpMesrlineNetTxBiasCurrentEntry": rm10010mpMesrlineNetTxBiasCurrentEntry,
       "rm10010mpMesrlineNetTxBiasCurrentIndex": rm10010mpMesrlineNetTxBiasCurrentIndex,
       "rm10010mpMesrlineNetTxBiasCurrentPortn": rm10010mpMesrlineNetTxBiasCurrentPortn,
       "rm10010mpMesrlineNetRxInputPwrTable": rm10010mpMesrlineNetRxInputPwrTable,
       "rm10010mpMesrlineNetRxInputPwrEntry": rm10010mpMesrlineNetRxInputPwrEntry,
       "rm10010mpMesrlineNetRxInputPwrIndex": rm10010mpMesrlineNetRxInputPwrIndex,
       "rm10010mpMesrlineNetRxInputPwrPortn": rm10010mpMesrlineNetRxInputPwrPortn,
       "rm10010mpMesrlineResidualChromaticDispTable": rm10010mpMesrlineResidualChromaticDispTable,
       "rm10010mpMesrlineResidualChromaticDispEntry": rm10010mpMesrlineResidualChromaticDispEntry,
       "rm10010mpMesrlineResidualChromaticDispIndex": rm10010mpMesrlineResidualChromaticDispIndex,
       "rm10010mpMesrlineResidualChromaticDispPortn": rm10010mpMesrlineResidualChromaticDispPortn,
       "rm10010mpMesrlineDiffGroupDelayTable": rm10010mpMesrlineDiffGroupDelayTable,
       "rm10010mpMesrlineDiffGroupDelayEntry": rm10010mpMesrlineDiffGroupDelayEntry,
       "rm10010mpMesrlineDiffGroupDelayIndex": rm10010mpMesrlineDiffGroupDelayIndex,
       "rm10010mpMesrlineDiffGroupDelayPortn": rm10010mpMesrlineDiffGroupDelayPortn,
       "rm10010mpMesrlineQFactorTable": rm10010mpMesrlineQFactorTable,
       "rm10010mpMesrlineQFactorEntry": rm10010mpMesrlineQFactorEntry,
       "rm10010mpMesrlineQFactorIndex": rm10010mpMesrlineQFactorIndex,
       "rm10010mpMesrlineQFactorPortn": rm10010mpMesrlineQFactorPortn,
       "rm10010mpMesrlineCarrierFreqOffsetTable": rm10010mpMesrlineCarrierFreqOffsetTable,
       "rm10010mpMesrlineCarrierFreqOffsetEntry": rm10010mpMesrlineCarrierFreqOffsetEntry,
       "rm10010mpMesrlineCarrierFreqOffsetIndex": rm10010mpMesrlineCarrierFreqOffsetIndex,
       "rm10010mpMesrlineCarrierFreqOffsetPortn": rm10010mpMesrlineCarrierFreqOffsetPortn,
       "rm10010mpMesrlineOsnrTable": rm10010mpMesrlineOsnrTable,
       "rm10010mpMesrlineOsnrEntry": rm10010mpMesrlineOsnrEntry,
       "rm10010mpMesrlineOsnrIndex": rm10010mpMesrlineOsnrIndex,
       "rm10010mpMesrlineOsnrPortn": rm10010mpMesrlineOsnrPortn,
       "rm10010mpcounters": rm10010mpcounters,
       "rm10010mpCntOther": rm10010mpCntOther,
       "rm10010mpCntClient": rm10010mpCntClient,
       "rm10010mpCntclientInputErrorCounterLaneOneTable": rm10010mpCntclientInputErrorCounterLaneOneTable,
       "rm10010mpCntclientInputErrorCounterLaneOneEntry": rm10010mpCntclientInputErrorCounterLaneOneEntry,
       "rm10010mpCntclientInputErrorCounterLaneOneIndex": rm10010mpCntclientInputErrorCounterLaneOneIndex,
       "rm10010mpCntclientInputErrorCounterLaneOneValuePortn": rm10010mpCntclientInputErrorCounterLaneOneValuePortn,
       "rm10010mpCntclientInputErrorCounterLaneOneErrorPortn": rm10010mpCntclientInputErrorCounterLaneOneErrorPortn,
       "rm10010mpCntclientInputErrorCounterLaneOneOverloadPortn": rm10010mpCntclientInputErrorCounterLaneOneOverloadPortn,
       "rm10010mpCntclientInputErrorCounterLaneTwoTable": rm10010mpCntclientInputErrorCounterLaneTwoTable,
       "rm10010mpCntclientInputErrorCounterLaneTwoEntry": rm10010mpCntclientInputErrorCounterLaneTwoEntry,
       "rm10010mpCntclientInputErrorCounterLaneTwoIndex": rm10010mpCntclientInputErrorCounterLaneTwoIndex,
       "rm10010mpCntclientInputErrorCounterLaneTwoValuePortn": rm10010mpCntclientInputErrorCounterLaneTwoValuePortn,
       "rm10010mpCntclientInputErrorCounterLaneTwoErrorPortn": rm10010mpCntclientInputErrorCounterLaneTwoErrorPortn,
       "rm10010mpCntclientInputErrorCounterLaneTwoOverloadPortn": rm10010mpCntclientInputErrorCounterLaneTwoOverloadPortn,
       "rm10010mpCntclientInputErrorCounterTable": rm10010mpCntclientInputErrorCounterTable,
       "rm10010mpCntclientInputErrorCounterEntry": rm10010mpCntclientInputErrorCounterEntry,
       "rm10010mpCntclientInputErrorCounterIndex": rm10010mpCntclientInputErrorCounterIndex,
       "rm10010mpCntclientInputErrorCounterValuePortn": rm10010mpCntclientInputErrorCounterValuePortn,
       "rm10010mpCntclientInputErrorCounterErrorPortn": rm10010mpCntclientInputErrorCounterErrorPortn,
       "rm10010mpCntclientInputErrorCounterOverloadPortn": rm10010mpCntclientInputErrorCounterOverloadPortn,
       "rm10010mpCntclientCbipCounterTable": rm10010mpCntclientCbipCounterTable,
       "rm10010mpCntclientCbipCounterEntry": rm10010mpCntclientCbipCounterEntry,
       "rm10010mpCntclientCbipCounterIndex": rm10010mpCntclientCbipCounterIndex,
       "rm10010mpCntclientCbipCounterValuePortn": rm10010mpCntclientCbipCounterValuePortn,
       "rm10010mpCntclientCbipCounterErrorPortn": rm10010mpCntclientCbipCounterErrorPortn,
       "rm10010mpCntclientCbipCounterOverloadPortn": rm10010mpCntclientCbipCounterOverloadPortn,
       "rm10010mpCntLine": rm10010mpCntLine,
       "rm10010mpCntlocalLineSmBip8ErrorCounterTable": rm10010mpCntlocalLineSmBip8ErrorCounterTable,
       "rm10010mpCntlocalLineSmBip8ErrorCounterEntry": rm10010mpCntlocalLineSmBip8ErrorCounterEntry,
       "rm10010mpCntlocalLineSmBip8ErrorCounterIndex": rm10010mpCntlocalLineSmBip8ErrorCounterIndex,
       "rm10010mpCntlocalLineSmBip8ErrorCounterValuePortn": rm10010mpCntlocalLineSmBip8ErrorCounterValuePortn,
       "rm10010mpCntlocalLineSmBip8ErrorCounterErrorPortn": rm10010mpCntlocalLineSmBip8ErrorCounterErrorPortn,
       "rm10010mpCntlocalLineSmBip8ErrorCounterOverloadPortn": rm10010mpCntlocalLineSmBip8ErrorCounterOverloadPortn,
       "rm10010mpCntlocalLineFecCorrectedErrorsCounterTable": rm10010mpCntlocalLineFecCorrectedErrorsCounterTable,
       "rm10010mpCntlocalLineFecCorrectedErrorsCounterEntry": rm10010mpCntlocalLineFecCorrectedErrorsCounterEntry,
       "rm10010mpCntlocalLineFecCorrectedErrorsCounterIndex": rm10010mpCntlocalLineFecCorrectedErrorsCounterIndex,
       "rm10010mpCntlocalLineFecCorrectedErrorsCounterValuePortn": rm10010mpCntlocalLineFecCorrectedErrorsCounterValuePortn,
       "rm10010mpCntlocalLineFecCorrectedErrorsCounterErrorPortn": rm10010mpCntlocalLineFecCorrectedErrorsCounterErrorPortn,
       "rm10010mpCntlocalLineFecCorrectedErrorsCounterOverloadPortn": rm10010mpCntlocalLineFecCorrectedErrorsCounterOverloadPortn,
       "rm10010mpCntremoteLineSmBip8ErrorCounterTable": rm10010mpCntremoteLineSmBip8ErrorCounterTable,
       "rm10010mpCntremoteLineSmBip8ErrorCounterEntry": rm10010mpCntremoteLineSmBip8ErrorCounterEntry,
       "rm10010mpCntremoteLineSmBip8ErrorCounterIndex": rm10010mpCntremoteLineSmBip8ErrorCounterIndex,
       "rm10010mpCntremoteLineSmBip8ErrorCounterValuePortn": rm10010mpCntremoteLineSmBip8ErrorCounterValuePortn,
       "rm10010mpCntremoteLineSmBip8ErrorCounterErrorPortn": rm10010mpCntremoteLineSmBip8ErrorCounterErrorPortn,
       "rm10010mpCntremoteLineSmBip8ErrorCounterOverloadPortn": rm10010mpCntremoteLineSmBip8ErrorCounterOverloadPortn,
       "rm10010mpCntlineDfrmTimCntTable": rm10010mpCntlineDfrmTimCntTable,
       "rm10010mpCntlineDfrmTimCntEntry": rm10010mpCntlineDfrmTimCntEntry,
       "rm10010mpCntlineDfrmTimCntIndex": rm10010mpCntlineDfrmTimCntIndex,
       "rm10010mpCntlineDfrmTimCntValuePortn": rm10010mpCntlineDfrmTimCntValuePortn,
       "rm10010mpCntlineDfrmTimCntErrorPortn": rm10010mpCntlineDfrmTimCntErrorPortn,
       "rm10010mpCntlineDfrmTimCntOverloadPortn": rm10010mpCntlineDfrmTimCntOverloadPortn,
       "rm10010mpCntlocalLineTrscvFecCorrectedErrorCounterTable": rm10010mpCntlocalLineTrscvFecCorrectedErrorCounterTable,
       "rm10010mpCntlocalLineTrscvFecCorrectedErrorCounterEntry": rm10010mpCntlocalLineTrscvFecCorrectedErrorCounterEntry,
       "rm10010mpCntlocalLineTrscvFecCorrectedErrorCounterIndex": rm10010mpCntlocalLineTrscvFecCorrectedErrorCounterIndex,
       "rm10010mpCntlocalLineTrscvFecCorrectedErrorCounterValuePortn": rm10010mpCntlocalLineTrscvFecCorrectedErrorCounterValuePortn,
       "rm10010mpCntlocalLineTrscvFecCorrectedErrorCounterErrorPortn": rm10010mpCntlocalLineTrscvFecCorrectedErrorCounterErrorPortn,
       "rm10010mpCntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn": rm10010mpCntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn,
       "rm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterTable": rm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterTable,
       "rm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterEntry": rm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterEntry,
       "rm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterIndex": rm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterIndex,
       "rm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterValuePortn": rm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterValuePortn,
       "rm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn": rm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn,
       "rm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn": rm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn,
       "rm10010mpcontrolsWrite": rm10010mpcontrolsWrite,
       "rm10010mpCtrlOther": rm10010mpCtrlOther,
       "rm10010mpCtrlconfMgnt1": rm10010mpCtrlconfMgnt1,
       "rm10010mpCtrlConf1Load1": rm10010mpCtrlConf1Load1,
       "rm10010mpCtrlConf2Load1": rm10010mpCtrlConf2Load1,
       "rm10010mpCtrlConf2Flash1": rm10010mpCtrlConf2Flash1,
       "rm10010mpCtrlConf2Clear1": rm10010mpCtrlConf2Clear1,
       "rm10010mpCtrlsynth4": rm10010mpCtrlsynth4,
       "rm10010mpCtrlCorrelatOn": rm10010mpCtrlCorrelatOn,
       "rm10010mpCtrlCorrelatOff": rm10010mpCtrlCorrelatOff,
       "rm10010mpCtrlswMgnt": rm10010mpCtrlswMgnt,
       "rm10010mpCtrlColdReset": rm10010mpCtrlColdReset,
       "rm10010mpCtrlWarmReset": rm10010mpCtrlWarmReset,
       "rm10010mpCtrlLoadSwBank1": rm10010mpCtrlLoadSwBank1,
       "rm10010mpCtrlLoadSwBank2": rm10010mpCtrlLoadSwBank2,
       "rm10010mpCtrlgwMgnt": rm10010mpCtrlgwMgnt,
       "rm10010mpCtrlCurrentGwReset": rm10010mpCtrlCurrentGwReset,
       "rm10010mpCtrlLoadGwBank1": rm10010mpCtrlLoadGwBank1,
       "rm10010mpCtrlLoadGwBank2": rm10010mpCtrlLoadGwBank2,
       "rm10010mpCtrlLoadGwBank3": rm10010mpCtrlLoadGwBank3,
       "rm10010mpCtrlLoadGwBank4": rm10010mpCtrlLoadGwBank4,
       "rm10010mpCtrlledTest": rm10010mpCtrlledTest,
       "rm10010mpCtrlGreenLed": rm10010mpCtrlGreenLed,
       "rm10010mpCtrlRedLed": rm10010mpCtrlRedLed,
       "rm10010mpCtrlLedOff": rm10010mpCtrlLedOff,
       "rm10010mpCtrlinitSwitchMarvell": rm10010mpCtrlinitSwitchMarvell,
       "rm10010mpCtrlInitSwitchMarvell": rm10010mpCtrlInitSwitchMarvell,
       "rm10010mpCtrlresetCount": rm10010mpCtrlresetCount,
       "rm10010mpCtrlResetcount": rm10010mpCtrlResetcount,
       "rm10010mpCtrlresetRmon": rm10010mpCtrlresetRmon,
       "rm10010mpCtrlResetrmon": rm10010mpCtrlResetrmon,
       "rm10010mpCtrlresetMeasurements": rm10010mpCtrlresetMeasurements,
       "rm10010mpCtrlResetmeasurements": rm10010mpCtrlResetmeasurements,
       "rm10010mpCtrlClient": rm10010mpCtrlClient,
       "rm10010mpCtrlaccessLoopTable": rm10010mpCtrlaccessLoopTable,
       "rm10010mpCtrlaccessLoopEntry": rm10010mpCtrlaccessLoopEntry,
       "rm10010mpCtrlaccessLoopIndex": rm10010mpCtrlaccessLoopIndex,
       "rm10010mpCtrlaccessLoopPortn": rm10010mpCtrlaccessLoopPortn,
       "rm10010mpCtrlclientLoopToLineTable": rm10010mpCtrlclientLoopToLineTable,
       "rm10010mpCtrlclientLoopToLineEntry": rm10010mpCtrlclientLoopToLineEntry,
       "rm10010mpCtrlclientLoopToLineIndex": rm10010mpCtrlclientLoopToLineIndex,
       "rm10010mpCtrlclientLoopToLinePortn": rm10010mpCtrlclientLoopToLinePortn,
       "rm10010mpCtrlcsfUpInsTable": rm10010mpCtrlcsfUpInsTable,
       "rm10010mpCtrlcsfUpInsEntry": rm10010mpCtrlcsfUpInsEntry,
       "rm10010mpCtrlcsfUpInsIndex": rm10010mpCtrlcsfUpInsIndex,
       "rm10010mpCtrlcsfUpInsPortn": rm10010mpCtrlcsfUpInsPortn,
       "rm10010mpCtrlcaisDwInsTable": rm10010mpCtrlcaisDwInsTable,
       "rm10010mpCtrlcaisDwInsEntry": rm10010mpCtrlcaisDwInsEntry,
       "rm10010mpCtrlcaisDwInsIndex": rm10010mpCtrlcaisDwInsIndex,
       "rm10010mpCtrlcaisDwInsPortn": rm10010mpCtrlcaisDwInsPortn,
       "rm10010mpCtrlLine": rm10010mpCtrlLine,
       "rm10010mpCtrlcommAccessLoopTable": rm10010mpCtrlcommAccessLoopTable,
       "rm10010mpCtrlcommAccessLoopEntry": rm10010mpCtrlcommAccessLoopEntry,
       "rm10010mpCtrlcommAccessLoopIndex": rm10010mpCtrlcommAccessLoopIndex,
       "rm10010mpCtrlcommAccessLoopPortn": rm10010mpCtrlcommAccessLoopPortn,
       "rm10010mpCtrllineLoopTable": rm10010mpCtrllineLoopTable,
       "rm10010mpCtrllineLoopEntry": rm10010mpCtrllineLoopEntry,
       "rm10010mpCtrllineLoopIndex": rm10010mpCtrllineLoopIndex,
       "rm10010mpCtrllineLoopPortn": rm10010mpCtrllineLoopPortn,
       "rm10010mpCtrlfecDisableTable": rm10010mpCtrlfecDisableTable,
       "rm10010mpCtrlfecDisableEntry": rm10010mpCtrlfecDisableEntry,
       "rm10010mpCtrlfecDisableIndex": rm10010mpCtrlfecDisableIndex,
       "rm10010mpCtrlfecDisablePortn": rm10010mpCtrlfecDisablePortn,
       "rm10010mpCtrlmsaLineLoopTable": rm10010mpCtrlmsaLineLoopTable,
       "rm10010mpCtrlmsaLineLoopEntry": rm10010mpCtrlmsaLineLoopEntry,
       "rm10010mpCtrlmsaLineLoopIndex": rm10010mpCtrlmsaLineLoopIndex,
       "rm10010mpCtrlmsaLineLoopPortn": rm10010mpCtrlmsaLineLoopPortn,
       "rm10010mpCtrlmsaTxResetTable": rm10010mpCtrlmsaTxResetTable,
       "rm10010mpCtrlmsaTxResetEntry": rm10010mpCtrlmsaTxResetEntry,
       "rm10010mpCtrlmsaTxResetIndex": rm10010mpCtrlmsaTxResetIndex,
       "rm10010mpCtrlmsaTxResetPortn": rm10010mpCtrlmsaTxResetPortn,
       "rm10010mpCtrlmsaRxResetTable": rm10010mpCtrlmsaRxResetTable,
       "rm10010mpCtrlmsaRxResetEntry": rm10010mpCtrlmsaRxResetEntry,
       "rm10010mpCtrlmsaRxResetIndex": rm10010mpCtrlmsaRxResetIndex,
       "rm10010mpCtrlmsaRxResetPortn": rm10010mpCtrlmsaRxResetPortn,
       "rm10010mpCtrlmsaShutdownTable": rm10010mpCtrlmsaShutdownTable,
       "rm10010mpCtrlmsaShutdownEntry": rm10010mpCtrlmsaShutdownEntry,
       "rm10010mpCtrlmsaShutdownIndex": rm10010mpCtrlmsaShutdownIndex,
       "rm10010mpCtrlmsaShutdownPortn": rm10010mpCtrlmsaShutdownPortn,
       "rm10010mpri": rm10010mpri,
       "rm10010mpriTable": rm10010mpriTable,
       "rm10010mpRinvSfpTable": rm10010mpRinvSfpTable,
       "rm10010mpRinvSfpEntry": rm10010mpRinvSfpEntry,
       "rm10010mpRinvSfpIndex": rm10010mpRinvSfpIndex,
       "rm10010mpRinvsfp": rm10010mpRinvsfp,
       "rm10010mpRinvLineTable": rm10010mpRinvLineTable,
       "rm10010mpRinvLineEntry": rm10010mpRinvLineEntry,
       "rm10010mpRinvLineIndex": rm10010mpRinvLineIndex,
       "rm10010mpRinvxfpLine": rm10010mpRinvxfpLine,
       "rm10010mpRinvReloadInventory": rm10010mpRinvReloadInventory,
       "rm10010mpRinvHwPlatform": rm10010mpRinvHwPlatform,
       "rm10010mpRinvModulePlatform": rm10010mpRinvModulePlatform,
       "rm10010mpRinvSwPlatform": rm10010mpRinvSwPlatform,
       "rm10010mpRinvGwPlatform": rm10010mpRinvGwPlatform,
       "rm10010mpdownload": rm10010mpdownload,
       "rm10010mpDwlOther": rm10010mpDwlOther,
       "rm10010mpDwlrestartProcess": rm10010mpDwlrestartProcess,
       "rm10010mpDwlWarmRestartProcessed": rm10010mpDwlWarmRestartProcessed,
       "rm10010mpDwlColdRestartProcessed": rm10010mpDwlColdRestartProcessed,
       "rm10010mpDwlswBanksUsed": rm10010mpDwlswBanksUsed,
       "rm10010mpDwlSwBank1Used": rm10010mpDwlSwBank1Used,
       "rm10010mpDwlSwBank2Used": rm10010mpDwlSwBank2Used,
       "rm10010mpDwlSwBank1Notempty": rm10010mpDwlSwBank1Notempty,
       "rm10010mpDwlSwBank2Notempty": rm10010mpDwlSwBank2Notempty,
       "rm10010mpDwlgwBanksUsed": rm10010mpDwlgwBanksUsed,
       "rm10010mpDwlGwBank1Used": rm10010mpDwlGwBank1Used,
       "rm10010mpDwlGwBank2Used": rm10010mpDwlGwBank2Used,
       "rm10010mpDwlGwBank3Used": rm10010mpDwlGwBank3Used,
       "rm10010mpDwlGwBank4Used": rm10010mpDwlGwBank4Used,
       "rm10010mpDwlGwBank1Notempty": rm10010mpDwlGwBank1Notempty,
       "rm10010mpDwlGwBank2Notempty": rm10010mpDwlGwBank2Notempty,
       "rm10010mpDwlGwBank3Notempty": rm10010mpDwlGwBank3Notempty,
       "rm10010mpDwlGwBank4Notempty": rm10010mpDwlGwBank4Notempty,
       "rm10010mpDwlClient": rm10010mpDwlClient,
       "rm10010mpDwlLine": rm10010mpDwlLine,
       "rm10010mpConfig": rm10010mpConfig,
       "rm10010mpCfgAccessCAisCsf": rm10010mpCfgAccessCAisCsf,
       "rm10010mpCfgClientcaiscsfTable": rm10010mpCfgClientcaiscsfTable,
       "rm10010mpCfgClientcaiscsfEntry": rm10010mpCfgClientcaiscsfEntry,
       "rm10010mpCfgClientcaiscsfIndex": rm10010mpCfgClientcaiscsfIndex,
       "rm10010mpCfgReservePortn": rm10010mpCfgReservePortn,
       "rm10010mpCfgStartup": rm10010mpCfgStartup,
       "rm10010mpCfgClientStartupTable": rm10010mpCfgClientStartupTable,
       "rm10010mpCfgClientStartupEntry": rm10010mpCfgClientStartupEntry,
       "rm10010mpCfgClientStartupIndex": rm10010mpCfgClientStartupIndex,
       "rm10010mpCfgSystConfPortPortn": rm10010mpCfgSystConfPortPortn,
       "rm10010mpCfgNetConfPortPortn": rm10010mpCfgNetConfPortPortn,
       "rm10010mpCfgOptionsPortPortn": rm10010mpCfgOptionsPortPortn,
       "rm10010mpCfgLineStartupTable": rm10010mpCfgLineStartupTable,
       "rm10010mpCfgLineStartupEntry": rm10010mpCfgLineStartupEntry,
       "rm10010mpCfgLineStartupIndex": rm10010mpCfgLineStartupIndex,
       "rm10010mpCfgSystConfLinePortn": rm10010mpCfgSystConfLinePortn,
       "rm10010mpCfgOptionsLinePortn": rm10010mpCfgOptionsLinePortn,
       "rm10010mpCfgXfpTable": rm10010mpCfgXfpTable,
       "rm10010mpCfgXfpEntry": rm10010mpCfgXfpEntry,
       "rm10010mpCfgXfpIndex": rm10010mpCfgXfpIndex,
       "rm10010mpCfgSystConfMsaLinePortn": rm10010mpCfgSystConfMsaLinePortn,
       "rm10010mpCfgLabels": rm10010mpCfgLabels,
       "rm10010mpCfgLabelclientTable": rm10010mpCfgLabelclientTable,
       "rm10010mpCfgLabelclientEntry": rm10010mpCfgLabelclientEntry,
       "rm10010mpCfgLabelclientIndex": rm10010mpCfgLabelclientIndex,
       "rm10010mpCfgLabelclientPortn": rm10010mpCfgLabelclientPortn,
       "rm10010mpCfgLabellineTable": rm10010mpCfgLabellineTable,
       "rm10010mpCfgLabellineEntry": rm10010mpCfgLabellineEntry,
       "rm10010mpCfgLabellineIndex": rm10010mpCfgLabellineIndex,
       "rm10010mpCfgLabellinePortn": rm10010mpCfgLabellinePortn,
       "rm10010mpCfgStartuptlh": rm10010mpCfgStartuptlh,
       "rm10010mpCfgOtxtlhTable": rm10010mpCfgOtxtlhTable,
       "rm10010mpCfgOtxtlhEntry": rm10010mpCfgOtxtlhEntry,
       "rm10010mpCfgOtxtlhIndex": rm10010mpCfgOtxtlhIndex,
       "rm10010mpCfgLinePwrLaserPortn": rm10010mpCfgLinePwrLaserPortn,
       "rm10010mpCfgLineFCurrentPortn": rm10010mpCfgLineFCurrentPortn,
       "rm10010mpCfgLineGridCurrentPortn": rm10010mpCfgLineGridCurrentPortn,
       "rm10010mpCfgFPortn": rm10010mpCfgFPortn,
       "rm10010mpCfgRxLineFCurrentPortn": rm10010mpCfgRxLineFCurrentPortn,
       "rm10010mpCfgOther": rm10010mpCfgOther,
       "rm10010mptablemoduleOther": rm10010mptablemoduleOther,
       "rm10010mpCfgmode": rm10010mpCfgmode,
       "rm10010mpCfgfanLowSpeedThreshold": rm10010mpCfgfanLowSpeedThreshold,
       "rm10010mpCfgfanHighSpeedThreshold": rm10010mpCfgfanHighSpeedThreshold,
       "rm10010mpCfgStartuptablefive": rm10010mpCfgStartuptablefive,
       "rm10010mpCfgOtxtlhcapabilitiesTable": rm10010mpCfgOtxtlhcapabilitiesTable,
       "rm10010mpCfgOtxtlhcapabilitiesEntry": rm10010mpCfgOtxtlhcapabilitiesEntry,
       "rm10010mpCfgOtxtlhcapabilitiesIndex": rm10010mpCfgOtxtlhcapabilitiesIndex,
       "rm10010mpCfgComponentTypePortn": rm10010mpCfgComponentTypePortn,
       "rm10010mpCfgMiscellaneousPortn": rm10010mpCfgMiscellaneousPortn,
       "rm10010mpCfgFirstChannelPortn": rm10010mpCfgFirstChannelPortn,
       "rm10010mpCfgLastChannelPortn": rm10010mpCfgLastChannelPortn,
       "rm10010mpCfgGridPortn": rm10010mpCfgGridPortn,
       "rm10010mpCfgWriteConfiguration": rm10010mpCfgWriteConfiguration,
       "rm10010mptraps": rm10010mptraps,
       "rm10010mptrapPortNumber": rm10010mptrapPortNumber,
       "rm10010mptrapLineNumber": rm10010mptrapLineNumber,
       "rm10010mptrapBoardNumber": rm10010mptrapBoardNumber,
       "rm10010mpLineTrapNotUrgentGoesOn": rm10010mpLineTrapNotUrgentGoesOn,
       "rm10010mpLineTrapNotUrgentGoesOff": rm10010mpLineTrapNotUrgentGoesOff,
       "rm10010mpLineTrapUrgentGoesOn": rm10010mpLineTrapUrgentGoesOn,
       "rm10010mpLineTrapUrgentGoesOff": rm10010mpLineTrapUrgentGoesOff,
       "rm10010mpLineTrapCritGoesOn": rm10010mpLineTrapCritGoesOn,
       "rm10010mpLineTrapCritGoesOff": rm10010mpLineTrapCritGoesOff,
       "rm10010mpClientTrapNotUrgentGoesOn": rm10010mpClientTrapNotUrgentGoesOn,
       "rm10010mpClientTrapNotUrgentGoesOff": rm10010mpClientTrapNotUrgentGoesOff,
       "rm10010mpClientTrapUrgentGoesOn": rm10010mpClientTrapUrgentGoesOn,
       "rm10010mpClientTrapUrgentGoesOff": rm10010mpClientTrapUrgentGoesOff,
       "rm10010mpClientTrapCritGoesOn": rm10010mpClientTrapCritGoesOn,
       "rm10010mpClientTrapCritGoesOff": rm10010mpClientTrapCritGoesOff,
       "rm10010mpPowerTrapUrgentGoesOn": rm10010mpPowerTrapUrgentGoesOn,
       "rm10010mpPowerTrapUrgentGoesOff": rm10010mpPowerTrapUrgentGoesOff,
       "rm10010mpMonitoring": rm10010mpMonitoring,
       "rm10010mpMonOther": rm10010mpMonOther,
       "rm10010mpMonRmon": rm10010mpMonRmon,
       "rm10010mpMonClient": rm10010mpMonClient,
       "rm10010mpMonClientRmonCounter": rm10010mpMonClientRmonCounter,
       "rm10010mpMonupRmonBytesCounterClientInputTable": rm10010mpMonupRmonBytesCounterClientInputTable,
       "rm10010mpMonupRmonBytesCounterClientInputEntry": rm10010mpMonupRmonBytesCounterClientInputEntry,
       "rm10010mpMonupRmonBytesCounterClientInputIndex": rm10010mpMonupRmonBytesCounterClientInputIndex,
       "rm10010mpMonupRmonBytesCounterClientInputValuePortn": rm10010mpMonupRmonBytesCounterClientInputValuePortn,
       "rm10010mpMonupRmonBytesCounterClientInputErrorPortn": rm10010mpMonupRmonBytesCounterClientInputErrorPortn,
       "rm10010mpMonupRmonBytesCounterClientInputOverloadPortn": rm10010mpMonupRmonBytesCounterClientInputOverloadPortn,
       "rm10010mpMonupRmonCrcErrorsCounterClientInputTable": rm10010mpMonupRmonCrcErrorsCounterClientInputTable,
       "rm10010mpMonupRmonCrcErrorsCounterClientInputEntry": rm10010mpMonupRmonCrcErrorsCounterClientInputEntry,
       "rm10010mpMonupRmonCrcErrorsCounterClientInputIndex": rm10010mpMonupRmonCrcErrorsCounterClientInputIndex,
       "rm10010mpMonupRmonCrcErrorsCounterClientInputValuePortn": rm10010mpMonupRmonCrcErrorsCounterClientInputValuePortn,
       "rm10010mpMonupRmonCrcErrorsCounterClientInputErrorPortn": rm10010mpMonupRmonCrcErrorsCounterClientInputErrorPortn,
       "rm10010mpMonupRmonCrcErrorsCounterClientInputOverloadPortn": rm10010mpMonupRmonCrcErrorsCounterClientInputOverloadPortn,
       "rm10010mpMonupRmonPacketsCounterClientInputTable": rm10010mpMonupRmonPacketsCounterClientInputTable,
       "rm10010mpMonupRmonPacketsCounterClientInputEntry": rm10010mpMonupRmonPacketsCounterClientInputEntry,
       "rm10010mpMonupRmonPacketsCounterClientInputIndex": rm10010mpMonupRmonPacketsCounterClientInputIndex,
       "rm10010mpMonupRmonPacketsCounterClientInputValuePortn": rm10010mpMonupRmonPacketsCounterClientInputValuePortn,
       "rm10010mpMonupRmonPacketsCounterClientInputErrorPortn": rm10010mpMonupRmonPacketsCounterClientInputErrorPortn,
       "rm10010mpMonupRmonPacketsCounterClientInputOverloadPortn": rm10010mpMonupRmonPacketsCounterClientInputOverloadPortn,
       "rm10010mpMonupRmonBroadcastCounterClientInputTable": rm10010mpMonupRmonBroadcastCounterClientInputTable,
       "rm10010mpMonupRmonBroadcastCounterClientInputEntry": rm10010mpMonupRmonBroadcastCounterClientInputEntry,
       "rm10010mpMonupRmonBroadcastCounterClientInputIndex": rm10010mpMonupRmonBroadcastCounterClientInputIndex,
       "rm10010mpMonupRmonBroadcastCounterClientInputValuePortn": rm10010mpMonupRmonBroadcastCounterClientInputValuePortn,
       "rm10010mpMonupRmonBroadcastCounterClientInputErrorPortn": rm10010mpMonupRmonBroadcastCounterClientInputErrorPortn,
       "rm10010mpMonupRmonBroadcastCounterClientInputOverloadPortn": rm10010mpMonupRmonBroadcastCounterClientInputOverloadPortn,
       "rm10010mpMonupRmonMulticastCounterClientInputTable": rm10010mpMonupRmonMulticastCounterClientInputTable,
       "rm10010mpMonupRmonMulticastCounterClientInputEntry": rm10010mpMonupRmonMulticastCounterClientInputEntry,
       "rm10010mpMonupRmonMulticastCounterClientInputIndex": rm10010mpMonupRmonMulticastCounterClientInputIndex,
       "rm10010mpMonupRmonMulticastCounterClientInputValuePortn": rm10010mpMonupRmonMulticastCounterClientInputValuePortn,
       "rm10010mpMonupRmonMulticastCounterClientInputErrorPortn": rm10010mpMonupRmonMulticastCounterClientInputErrorPortn,
       "rm10010mpMonupRmonMulticastCounterClientInputOverloadPortn": rm10010mpMonupRmonMulticastCounterClientInputOverloadPortn,
       "rm10010mpMonupRmonPauseFrameCounterClientInputTable": rm10010mpMonupRmonPauseFrameCounterClientInputTable,
       "rm10010mpMonupRmonPauseFrameCounterClientInputEntry": rm10010mpMonupRmonPauseFrameCounterClientInputEntry,
       "rm10010mpMonupRmonPauseFrameCounterClientInputIndex": rm10010mpMonupRmonPauseFrameCounterClientInputIndex,
       "rm10010mpMonupRmonPauseFrameCounterClientInputValuePortn": rm10010mpMonupRmonPauseFrameCounterClientInputValuePortn,
       "rm10010mpMonupRmonPauseFrameCounterClientInputErrorPortn": rm10010mpMonupRmonPauseFrameCounterClientInputErrorPortn,
       "rm10010mpMonupRmonPauseFrameCounterClientInputOverloadPortn": rm10010mpMonupRmonPauseFrameCounterClientInputOverloadPortn}
)
