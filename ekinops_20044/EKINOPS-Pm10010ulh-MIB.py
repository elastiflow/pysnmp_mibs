# SNMP MIB module (EKINOPS-Pm10010ulh-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ekinops_20044/EKINOPS-Pm10010ulh-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 12:01:47 2025
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

modulePm10010ulh = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80)
)
if mibBuilder.loadTexts:
    modulePm10010ulh.setRevisions(
        ("2016-10-10 00:00",
         "2017-03-31 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Pm10010ulhMultiRate(TextualConvention, Integer32):
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



class Pm10010ulhOtxMode(TextualConvention, Integer32):
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



class Pm10010ulhOtxGrid(TextualConvention, Integer32):
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



class Pm10010ulhAdjustValue(TextualConvention, Integer32):
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



class Pm10010ulhClientProtocol(TextualConvention, Integer32):
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



class Pm10010ulhProtocolMode(TextualConvention, Integer32):
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



class Pm10010ulhOtxChannel(TextualConvention, Integer32):
    status = "current"


class Pm10010ulhOrxChannel(TextualConvention, Integer32):
    status = "current"


class Pm10010ulhDccMode(TextualConvention, Integer32):
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
        *(("dccNo", 0),
          ("dccLine1", 1),
          ("dccLine2", 2))
    )



class Pm10010ulhModuleMode(TextualConvention, Integer32):
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
        *(("unusedmode", 0),
          ("mode200gma", 1),
          ("mode200gmr", 2),
          ("mode100gulh", 3))
    )



# MIB Managed Objects in the order of their OIDs

_Pm10010ulhalarms_ObjectIdentity = ObjectIdentity
pm10010ulhalarms = _Pm10010ulhalarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2)
)
_Pm10010ulhAlmOther_ObjectIdentity = ObjectIdentity
pm10010ulhAlmOther = _Pm10010ulhAlmOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1)
)
_Pm10010ulhAlmOtherNurg_ObjectIdentity = ObjectIdentity
pm10010ulhAlmOtherNurg = _Pm10010ulhAlmOtherNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 1)
)
_Pm10010ulhAlmsynthAlm2_ObjectIdentity = ObjectIdentity
pm10010ulhAlmsynthAlm2 = _Pm10010ulhAlmsynthAlm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 1, 2)
)
_Pm10010ulhAlmConfTableSave_Type = EkiOnOff
_Pm10010ulhAlmConfTableSave_Object = MibScalar
pm10010ulhAlmConfTableSave = _Pm10010ulhAlmConfTableSave_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 1, 2, 1),
    _Pm10010ulhAlmConfTableSave_Type()
)
pm10010ulhAlmConfTableSave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmConfTableSave.setStatus("current")
_Pm10010ulhAlmInvUpload_Type = EkiOnOff
_Pm10010ulhAlmInvUpload_Object = MibScalar
pm10010ulhAlmInvUpload = _Pm10010ulhAlmInvUpload_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 1, 2, 2),
    _Pm10010ulhAlmInvUpload_Type()
)
pm10010ulhAlmInvUpload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmInvUpload.setStatus("current")
_Pm10010ulhAlmConfTableLoad_Type = EkiOnOff
_Pm10010ulhAlmConfTableLoad_Object = MibScalar
pm10010ulhAlmConfTableLoad = _Pm10010ulhAlmConfTableLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 1, 2, 3),
    _Pm10010ulhAlmConfTableLoad_Type()
)
pm10010ulhAlmConfTableLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmConfTableLoad.setStatus("current")
_Pm10010ulhAlmCorrelatOff_Type = EkiOnOff
_Pm10010ulhAlmCorrelatOff_Object = MibScalar
pm10010ulhAlmCorrelatOff = _Pm10010ulhAlmCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 1, 2, 4),
    _Pm10010ulhAlmCorrelatOff_Type()
)
pm10010ulhAlmCorrelatOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmCorrelatOff.setStatus("current")
_Pm10010ulhAlmMaintenanceOn_Type = EkiOnOff
_Pm10010ulhAlmMaintenanceOn_Object = MibScalar
pm10010ulhAlmMaintenanceOn = _Pm10010ulhAlmMaintenanceOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 1, 2, 5),
    _Pm10010ulhAlmMaintenanceOn_Type()
)
pm10010ulhAlmMaintenanceOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmMaintenanceOn.setStatus("current")
_Pm10010ulhAlmOtherUrg_ObjectIdentity = ObjectIdentity
pm10010ulhAlmOtherUrg = _Pm10010ulhAlmOtherUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 2)
)
_Pm10010ulhAlmmodFanFail_ObjectIdentity = ObjectIdentity
pm10010ulhAlmmodFanFail = _Pm10010ulhAlmmodFanFail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 2, 336)
)
_Pm10010ulhAlmFanFail_Type = EkiOnOff
_Pm10010ulhAlmFanFail_Object = MibScalar
pm10010ulhAlmFanFail = _Pm10010ulhAlmFanFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 2, 336, 1),
    _Pm10010ulhAlmFanFail_Type()
)
pm10010ulhAlmFanFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmFanFail.setStatus("current")
_Pm10010ulhAlmFanHighSpeed_Type = EkiOnOff
_Pm10010ulhAlmFanHighSpeed_Object = MibScalar
pm10010ulhAlmFanHighSpeed = _Pm10010ulhAlmFanHighSpeed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 2, 336, 2),
    _Pm10010ulhAlmFanHighSpeed_Type()
)
pm10010ulhAlmFanHighSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmFanHighSpeed.setStatus("current")
_Pm10010ulhAlmOtherCrit_ObjectIdentity = ObjectIdentity
pm10010ulhAlmOtherCrit = _Pm10010ulhAlmOtherCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3)
)
_Pm10010ulhAlmsynthAlm0_ObjectIdentity = ObjectIdentity
pm10010ulhAlmsynthAlm0 = _Pm10010ulhAlmsynthAlm0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 0)
)
_Pm10010ulhAlmFailFan_Type = EkiOnOff
_Pm10010ulhAlmFailFan_Object = MibScalar
pm10010ulhAlmFailFan = _Pm10010ulhAlmFailFan_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 0, 2),
    _Pm10010ulhAlmFailFan_Type()
)
pm10010ulhAlmFailFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmFailFan.setStatus("current")
_Pm10010ulhAlmModGlobFail_Type = EkiOnOff
_Pm10010ulhAlmModGlobFail_Object = MibScalar
pm10010ulhAlmModGlobFail = _Pm10010ulhAlmModGlobFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 0, 9),
    _Pm10010ulhAlmModGlobFail_Type()
)
pm10010ulhAlmModGlobFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmModGlobFail.setStatus("current")
_Pm10010ulhAlmDefFuseA_Type = EkiOnOff
_Pm10010ulhAlmDefFuseA_Object = MibScalar
pm10010ulhAlmDefFuseA = _Pm10010ulhAlmDefFuseA_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 0, 15),
    _Pm10010ulhAlmDefFuseA_Type()
)
pm10010ulhAlmDefFuseA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmDefFuseA.setStatus("current")
_Pm10010ulhAlmDefFuseB_Type = EkiOnOff
_Pm10010ulhAlmDefFuseB_Object = MibScalar
pm10010ulhAlmDefFuseB = _Pm10010ulhAlmDefFuseB_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 0, 16),
    _Pm10010ulhAlmDefFuseB_Type()
)
pm10010ulhAlmDefFuseB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmDefFuseB.setStatus("current")
_Pm10010ulhAlmclientModuleState_ObjectIdentity = ObjectIdentity
pm10010ulhAlmclientModuleState = _Pm10010ulhAlmclientModuleState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 72)
)
_Pm10010ulhAlmCfpInitialize_Type = EkiOnOff
_Pm10010ulhAlmCfpInitialize_Object = MibScalar
pm10010ulhAlmCfpInitialize = _Pm10010ulhAlmCfpInitialize_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 72, 1),
    _Pm10010ulhAlmCfpInitialize_Type()
)
pm10010ulhAlmCfpInitialize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmCfpInitialize.setStatus("current")
_Pm10010ulhAlmCfpLowPower_Type = EkiOnOff
_Pm10010ulhAlmCfpLowPower_Object = MibScalar
pm10010ulhAlmCfpLowPower = _Pm10010ulhAlmCfpLowPower_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 72, 2),
    _Pm10010ulhAlmCfpLowPower_Type()
)
pm10010ulhAlmCfpLowPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmCfpLowPower.setStatus("current")
_Pm10010ulhAlmCfpHighPowerUp_Type = EkiOnOff
_Pm10010ulhAlmCfpHighPowerUp_Object = MibScalar
pm10010ulhAlmCfpHighPowerUp = _Pm10010ulhAlmCfpHighPowerUp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 72, 3),
    _Pm10010ulhAlmCfpHighPowerUp_Type()
)
pm10010ulhAlmCfpHighPowerUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmCfpHighPowerUp.setStatus("current")
_Pm10010ulhAlmCfpTxOff_Type = EkiOnOff
_Pm10010ulhAlmCfpTxOff_Object = MibScalar
pm10010ulhAlmCfpTxOff = _Pm10010ulhAlmCfpTxOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 72, 4),
    _Pm10010ulhAlmCfpTxOff_Type()
)
pm10010ulhAlmCfpTxOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmCfpTxOff.setStatus("current")
_Pm10010ulhAlmCfpTxTurnOn_Type = EkiOnOff
_Pm10010ulhAlmCfpTxTurnOn_Object = MibScalar
pm10010ulhAlmCfpTxTurnOn = _Pm10010ulhAlmCfpTxTurnOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 72, 5),
    _Pm10010ulhAlmCfpTxTurnOn_Type()
)
pm10010ulhAlmCfpTxTurnOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmCfpTxTurnOn.setStatus("current")
_Pm10010ulhAlmCfpReady_Type = EkiOnOff
_Pm10010ulhAlmCfpReady_Object = MibScalar
pm10010ulhAlmCfpReady = _Pm10010ulhAlmCfpReady_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 72, 6),
    _Pm10010ulhAlmCfpReady_Type()
)
pm10010ulhAlmCfpReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmCfpReady.setStatus("current")
_Pm10010ulhAlmCfpFault_Type = EkiOnOff
_Pm10010ulhAlmCfpFault_Object = MibScalar
pm10010ulhAlmCfpFault = _Pm10010ulhAlmCfpFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 72, 7),
    _Pm10010ulhAlmCfpFault_Type()
)
pm10010ulhAlmCfpFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmCfpFault.setStatus("current")
_Pm10010ulhAlmCfpTxTurnOff_Type = EkiOnOff
_Pm10010ulhAlmCfpTxTurnOff_Object = MibScalar
pm10010ulhAlmCfpTxTurnOff = _Pm10010ulhAlmCfpTxTurnOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 72, 8),
    _Pm10010ulhAlmCfpTxTurnOff_Type()
)
pm10010ulhAlmCfpTxTurnOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmCfpTxTurnOff.setStatus("current")
_Pm10010ulhAlmCfpHighPowerDown_Type = EkiOnOff
_Pm10010ulhAlmCfpHighPowerDown_Object = MibScalar
pm10010ulhAlmCfpHighPowerDown = _Pm10010ulhAlmCfpHighPowerDown_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 72, 9),
    _Pm10010ulhAlmCfpHighPowerDown_Type()
)
pm10010ulhAlmCfpHighPowerDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmCfpHighPowerDown.setStatus("current")
_Pm10010ulhAlmclientModuleGeneralStatus_ObjectIdentity = ObjectIdentity
pm10010ulhAlmclientModuleGeneralStatus = _Pm10010ulhAlmclientModuleGeneralStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 73)
)
_Pm10010ulhAlmCfpOutOfAlignment_Type = EkiOnOff
_Pm10010ulhAlmCfpOutOfAlignment_Object = MibScalar
pm10010ulhAlmCfpOutOfAlignment = _Pm10010ulhAlmCfpOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 73, 4),
    _Pm10010ulhAlmCfpOutOfAlignment_Type()
)
pm10010ulhAlmCfpOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmCfpOutOfAlignment.setStatus("current")
_Pm10010ulhAlmCfpRxNetworkLol_Type = EkiOnOff
_Pm10010ulhAlmCfpRxNetworkLol_Object = MibScalar
pm10010ulhAlmCfpRxNetworkLol = _Pm10010ulhAlmCfpRxNetworkLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 73, 5),
    _Pm10010ulhAlmCfpRxNetworkLol_Type()
)
pm10010ulhAlmCfpRxNetworkLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmCfpRxNetworkLol.setStatus("current")
_Pm10010ulhAlmCfpRxLos_Type = EkiOnOff
_Pm10010ulhAlmCfpRxLos_Object = MibScalar
pm10010ulhAlmCfpRxLos = _Pm10010ulhAlmCfpRxLos_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 73, 6),
    _Pm10010ulhAlmCfpRxLos_Type()
)
pm10010ulhAlmCfpRxLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmCfpRxLos.setStatus("current")
_Pm10010ulhAlmCfpTxHostLol_Type = EkiOnOff
_Pm10010ulhAlmCfpTxHostLol_Object = MibScalar
pm10010ulhAlmCfpTxHostLol = _Pm10010ulhAlmCfpTxHostLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 73, 7),
    _Pm10010ulhAlmCfpTxHostLol_Type()
)
pm10010ulhAlmCfpTxHostLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmCfpTxHostLol.setStatus("current")
_Pm10010ulhAlmCfpTxLosf_Type = EkiOnOff
_Pm10010ulhAlmCfpTxLosf_Object = MibScalar
pm10010ulhAlmCfpTxLosf = _Pm10010ulhAlmCfpTxLosf_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 73, 8),
    _Pm10010ulhAlmCfpTxLosf_Type()
)
pm10010ulhAlmCfpTxLosf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmCfpTxLosf.setStatus("current")
_Pm10010ulhAlmCfpTxCmuLol_Type = EkiOnOff
_Pm10010ulhAlmCfpTxCmuLol_Object = MibScalar
pm10010ulhAlmCfpTxCmuLol = _Pm10010ulhAlmCfpTxCmuLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 73, 9),
    _Pm10010ulhAlmCfpTxCmuLol_Type()
)
pm10010ulhAlmCfpTxCmuLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmCfpTxCmuLol.setStatus("current")
_Pm10010ulhAlmCfpTxJitterPllLol_Type = EkiOnOff
_Pm10010ulhAlmCfpTxJitterPllLol_Object = MibScalar
pm10010ulhAlmCfpTxJitterPllLol = _Pm10010ulhAlmCfpTxJitterPllLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 73, 10),
    _Pm10010ulhAlmCfpTxJitterPllLol_Type()
)
pm10010ulhAlmCfpTxJitterPllLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmCfpTxJitterPllLol.setStatus("current")
_Pm10010ulhAlmCfpLossOfRefclk_Type = EkiOnOff
_Pm10010ulhAlmCfpLossOfRefclk_Object = MibScalar
pm10010ulhAlmCfpLossOfRefclk = _Pm10010ulhAlmCfpLossOfRefclk_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 73, 11),
    _Pm10010ulhAlmCfpLossOfRefclk_Type()
)
pm10010ulhAlmCfpLossOfRefclk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmCfpLossOfRefclk.setStatus("current")
_Pm10010ulhAlmCfpHwInterlock_Type = EkiOnOff
_Pm10010ulhAlmCfpHwInterlock_Object = MibScalar
pm10010ulhAlmCfpHwInterlock = _Pm10010ulhAlmCfpHwInterlock_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 73, 14),
    _Pm10010ulhAlmCfpHwInterlock_Type()
)
pm10010ulhAlmCfpHwInterlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmCfpHwInterlock.setStatus("current")
_Pm10010ulhAlmclientGlobalAlarmSummary_ObjectIdentity = ObjectIdentity
pm10010ulhAlmclientGlobalAlarmSummary = _Pm10010ulhAlmclientGlobalAlarmSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 74)
)
_Pm10010ulhAlmCfpSoftGlobAlarmTest_Type = EkiOnOff
_Pm10010ulhAlmCfpSoftGlobAlarmTest_Object = MibScalar
pm10010ulhAlmCfpSoftGlobAlarmTest = _Pm10010ulhAlmCfpSoftGlobAlarmTest_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 74, 1),
    _Pm10010ulhAlmCfpSoftGlobAlarmTest_Type()
)
pm10010ulhAlmCfpSoftGlobAlarmTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmCfpSoftGlobAlarmTest.setStatus("current")
_Pm10010ulhAlmCfpNetworkLaneAlarmWarning2_Type = EkiOnOff
_Pm10010ulhAlmCfpNetworkLaneAlarmWarning2_Object = MibScalar
pm10010ulhAlmCfpNetworkLaneAlarmWarning2 = _Pm10010ulhAlmCfpNetworkLaneAlarmWarning2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 74, 7),
    _Pm10010ulhAlmCfpNetworkLaneAlarmWarning2_Type()
)
pm10010ulhAlmCfpNetworkLaneAlarmWarning2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmCfpNetworkLaneAlarmWarning2.setStatus("current")
_Pm10010ulhAlmCfpModuleState_Type = EkiOnOff
_Pm10010ulhAlmCfpModuleState_Object = MibScalar
pm10010ulhAlmCfpModuleState = _Pm10010ulhAlmCfpModuleState_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 74, 8),
    _Pm10010ulhAlmCfpModuleState_Type()
)
pm10010ulhAlmCfpModuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmCfpModuleState.setStatus("current")
_Pm10010ulhAlmCfpModuleGeneralStatus_Type = EkiOnOff
_Pm10010ulhAlmCfpModuleGeneralStatus_Object = MibScalar
pm10010ulhAlmCfpModuleGeneralStatus = _Pm10010ulhAlmCfpModuleGeneralStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 74, 9),
    _Pm10010ulhAlmCfpModuleGeneralStatus_Type()
)
pm10010ulhAlmCfpModuleGeneralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmCfpModuleGeneralStatus.setStatus("current")
_Pm10010ulhAlmCfpModuleFault_Type = EkiOnOff
_Pm10010ulhAlmCfpModuleFault_Object = MibScalar
pm10010ulhAlmCfpModuleFault = _Pm10010ulhAlmCfpModuleFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 74, 10),
    _Pm10010ulhAlmCfpModuleFault_Type()
)
pm10010ulhAlmCfpModuleFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmCfpModuleFault.setStatus("current")
_Pm10010ulhAlmCfpModuleAlarmWarning1_Type = EkiOnOff
_Pm10010ulhAlmCfpModuleAlarmWarning1_Object = MibScalar
pm10010ulhAlmCfpModuleAlarmWarning1 = _Pm10010ulhAlmCfpModuleAlarmWarning1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 74, 11),
    _Pm10010ulhAlmCfpModuleAlarmWarning1_Type()
)
pm10010ulhAlmCfpModuleAlarmWarning1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmCfpModuleAlarmWarning1.setStatus("current")
_Pm10010ulhAlmCfpModuleAlarmWarning2_Type = EkiOnOff
_Pm10010ulhAlmCfpModuleAlarmWarning2_Object = MibScalar
pm10010ulhAlmCfpModuleAlarmWarning2 = _Pm10010ulhAlmCfpModuleAlarmWarning2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 74, 12),
    _Pm10010ulhAlmCfpModuleAlarmWarning2_Type()
)
pm10010ulhAlmCfpModuleAlarmWarning2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmCfpModuleAlarmWarning2.setStatus("current")
_Pm10010ulhAlmCfpNetworkLaneAlarmWarning1_Type = EkiOnOff
_Pm10010ulhAlmCfpNetworkLaneAlarmWarning1_Object = MibScalar
pm10010ulhAlmCfpNetworkLaneAlarmWarning1 = _Pm10010ulhAlmCfpNetworkLaneAlarmWarning1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 74, 13),
    _Pm10010ulhAlmCfpNetworkLaneAlarmWarning1_Type()
)
pm10010ulhAlmCfpNetworkLaneAlarmWarning1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmCfpNetworkLaneAlarmWarning1.setStatus("current")
_Pm10010ulhAlmCfpNetworkLaneFaultStatus_Type = EkiOnOff
_Pm10010ulhAlmCfpNetworkLaneFaultStatus_Object = MibScalar
pm10010ulhAlmCfpNetworkLaneFaultStatus = _Pm10010ulhAlmCfpNetworkLaneFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 74, 14),
    _Pm10010ulhAlmCfpNetworkLaneFaultStatus_Type()
)
pm10010ulhAlmCfpNetworkLaneFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmCfpNetworkLaneFaultStatus.setStatus("current")
_Pm10010ulhAlmCfpHostLaneFaultStatus_Type = EkiOnOff
_Pm10010ulhAlmCfpHostLaneFaultStatus_Object = MibScalar
pm10010ulhAlmCfpHostLaneFaultStatus = _Pm10010ulhAlmCfpHostLaneFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 74, 15),
    _Pm10010ulhAlmCfpHostLaneFaultStatus_Type()
)
pm10010ulhAlmCfpHostLaneFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmCfpHostLaneFaultStatus.setStatus("current")
_Pm10010ulhAlmCfpGlobAlarmAssertion_Type = EkiOnOff
_Pm10010ulhAlmCfpGlobAlarmAssertion_Object = MibScalar
pm10010ulhAlmCfpGlobAlarmAssertion = _Pm10010ulhAlmCfpGlobAlarmAssertion_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 74, 16),
    _Pm10010ulhAlmCfpGlobAlarmAssertion_Type()
)
pm10010ulhAlmCfpGlobAlarmAssertion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmCfpGlobAlarmAssertion.setStatus("current")
_Pm10010ulhAlmmsaModuleState_ObjectIdentity = ObjectIdentity
pm10010ulhAlmmsaModuleState = _Pm10010ulhAlmmsaModuleState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 78)
)
_Pm10010ulhAlmMsaInitialize_Type = EkiOnOff
_Pm10010ulhAlmMsaInitialize_Object = MibScalar
pm10010ulhAlmMsaInitialize = _Pm10010ulhAlmMsaInitialize_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 78, 1),
    _Pm10010ulhAlmMsaInitialize_Type()
)
pm10010ulhAlmMsaInitialize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmMsaInitialize.setStatus("current")
_Pm10010ulhAlmMsaLowPower_Type = EkiOnOff
_Pm10010ulhAlmMsaLowPower_Object = MibScalar
pm10010ulhAlmMsaLowPower = _Pm10010ulhAlmMsaLowPower_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 78, 2),
    _Pm10010ulhAlmMsaLowPower_Type()
)
pm10010ulhAlmMsaLowPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmMsaLowPower.setStatus("current")
_Pm10010ulhAlmMsaHighPowerUp_Type = EkiOnOff
_Pm10010ulhAlmMsaHighPowerUp_Object = MibScalar
pm10010ulhAlmMsaHighPowerUp = _Pm10010ulhAlmMsaHighPowerUp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 78, 3),
    _Pm10010ulhAlmMsaHighPowerUp_Type()
)
pm10010ulhAlmMsaHighPowerUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmMsaHighPowerUp.setStatus("current")
_Pm10010ulhAlmMsaTxOff_Type = EkiOnOff
_Pm10010ulhAlmMsaTxOff_Object = MibScalar
pm10010ulhAlmMsaTxOff = _Pm10010ulhAlmMsaTxOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 78, 4),
    _Pm10010ulhAlmMsaTxOff_Type()
)
pm10010ulhAlmMsaTxOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmMsaTxOff.setStatus("current")
_Pm10010ulhAlmMsaTxTurnOn_Type = EkiOnOff
_Pm10010ulhAlmMsaTxTurnOn_Object = MibScalar
pm10010ulhAlmMsaTxTurnOn = _Pm10010ulhAlmMsaTxTurnOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 78, 5),
    _Pm10010ulhAlmMsaTxTurnOn_Type()
)
pm10010ulhAlmMsaTxTurnOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmMsaTxTurnOn.setStatus("current")
_Pm10010ulhAlmMsaReady_Type = EkiOnOff
_Pm10010ulhAlmMsaReady_Object = MibScalar
pm10010ulhAlmMsaReady = _Pm10010ulhAlmMsaReady_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 78, 6),
    _Pm10010ulhAlmMsaReady_Type()
)
pm10010ulhAlmMsaReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmMsaReady.setStatus("current")
_Pm10010ulhAlmMsaFault_Type = EkiOnOff
_Pm10010ulhAlmMsaFault_Object = MibScalar
pm10010ulhAlmMsaFault = _Pm10010ulhAlmMsaFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 78, 7),
    _Pm10010ulhAlmMsaFault_Type()
)
pm10010ulhAlmMsaFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmMsaFault.setStatus("current")
_Pm10010ulhAlmMsaTxTurnOff_Type = EkiOnOff
_Pm10010ulhAlmMsaTxTurnOff_Object = MibScalar
pm10010ulhAlmMsaTxTurnOff = _Pm10010ulhAlmMsaTxTurnOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 78, 8),
    _Pm10010ulhAlmMsaTxTurnOff_Type()
)
pm10010ulhAlmMsaTxTurnOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmMsaTxTurnOff.setStatus("current")
_Pm10010ulhAlmMsaHighPowerDown_Type = EkiOnOff
_Pm10010ulhAlmMsaHighPowerDown_Object = MibScalar
pm10010ulhAlmMsaHighPowerDown = _Pm10010ulhAlmMsaHighPowerDown_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 78, 9),
    _Pm10010ulhAlmMsaHighPowerDown_Type()
)
pm10010ulhAlmMsaHighPowerDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmMsaHighPowerDown.setStatus("current")
_Pm10010ulhAlmmsaModuleGeneralStatus_ObjectIdentity = ObjectIdentity
pm10010ulhAlmmsaModuleGeneralStatus = _Pm10010ulhAlmmsaModuleGeneralStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 79)
)
_Pm10010ulhAlmMsaOutOfAlignment_Type = EkiOnOff
_Pm10010ulhAlmMsaOutOfAlignment_Object = MibScalar
pm10010ulhAlmMsaOutOfAlignment = _Pm10010ulhAlmMsaOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 79, 4),
    _Pm10010ulhAlmMsaOutOfAlignment_Type()
)
pm10010ulhAlmMsaOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmMsaOutOfAlignment.setStatus("current")
_Pm10010ulhAlmMsaRxNetworkLol_Type = EkiOnOff
_Pm10010ulhAlmMsaRxNetworkLol_Object = MibScalar
pm10010ulhAlmMsaRxNetworkLol = _Pm10010ulhAlmMsaRxNetworkLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 79, 5),
    _Pm10010ulhAlmMsaRxNetworkLol_Type()
)
pm10010ulhAlmMsaRxNetworkLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmMsaRxNetworkLol.setStatus("current")
_Pm10010ulhAlmMsaRxLos_Type = EkiOnOff
_Pm10010ulhAlmMsaRxLos_Object = MibScalar
pm10010ulhAlmMsaRxLos = _Pm10010ulhAlmMsaRxLos_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 79, 6),
    _Pm10010ulhAlmMsaRxLos_Type()
)
pm10010ulhAlmMsaRxLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmMsaRxLos.setStatus("current")
_Pm10010ulhAlmMsaTxHostLol_Type = EkiOnOff
_Pm10010ulhAlmMsaTxHostLol_Object = MibScalar
pm10010ulhAlmMsaTxHostLol = _Pm10010ulhAlmMsaTxHostLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 79, 7),
    _Pm10010ulhAlmMsaTxHostLol_Type()
)
pm10010ulhAlmMsaTxHostLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmMsaTxHostLol.setStatus("current")
_Pm10010ulhAlmMsaTxLosf_Type = EkiOnOff
_Pm10010ulhAlmMsaTxLosf_Object = MibScalar
pm10010ulhAlmMsaTxLosf = _Pm10010ulhAlmMsaTxLosf_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 79, 8),
    _Pm10010ulhAlmMsaTxLosf_Type()
)
pm10010ulhAlmMsaTxLosf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmMsaTxLosf.setStatus("current")
_Pm10010ulhAlmMsaTxCmuLol_Type = EkiOnOff
_Pm10010ulhAlmMsaTxCmuLol_Object = MibScalar
pm10010ulhAlmMsaTxCmuLol = _Pm10010ulhAlmMsaTxCmuLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 79, 9),
    _Pm10010ulhAlmMsaTxCmuLol_Type()
)
pm10010ulhAlmMsaTxCmuLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmMsaTxCmuLol.setStatus("current")
_Pm10010ulhAlmMsaTxJitterPllLol_Type = EkiOnOff
_Pm10010ulhAlmMsaTxJitterPllLol_Object = MibScalar
pm10010ulhAlmMsaTxJitterPllLol = _Pm10010ulhAlmMsaTxJitterPllLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 79, 10),
    _Pm10010ulhAlmMsaTxJitterPllLol_Type()
)
pm10010ulhAlmMsaTxJitterPllLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmMsaTxJitterPllLol.setStatus("current")
_Pm10010ulhAlmMsaLossOfRefclk_Type = EkiOnOff
_Pm10010ulhAlmMsaLossOfRefclk_Object = MibScalar
pm10010ulhAlmMsaLossOfRefclk = _Pm10010ulhAlmMsaLossOfRefclk_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 79, 11),
    _Pm10010ulhAlmMsaLossOfRefclk_Type()
)
pm10010ulhAlmMsaLossOfRefclk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmMsaLossOfRefclk.setStatus("current")
_Pm10010ulhAlmMsaHwInterlock_Type = EkiOnOff
_Pm10010ulhAlmMsaHwInterlock_Object = MibScalar
pm10010ulhAlmMsaHwInterlock = _Pm10010ulhAlmMsaHwInterlock_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 79, 14),
    _Pm10010ulhAlmMsaHwInterlock_Type()
)
pm10010ulhAlmMsaHwInterlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmMsaHwInterlock.setStatus("current")
_Pm10010ulhAlmmsaGlobalAlarmSummary_ObjectIdentity = ObjectIdentity
pm10010ulhAlmmsaGlobalAlarmSummary = _Pm10010ulhAlmmsaGlobalAlarmSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 80)
)
_Pm10010ulhAlmMsaSoftGlobAlarmTest_Type = EkiOnOff
_Pm10010ulhAlmMsaSoftGlobAlarmTest_Object = MibScalar
pm10010ulhAlmMsaSoftGlobAlarmTest = _Pm10010ulhAlmMsaSoftGlobAlarmTest_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 80, 1),
    _Pm10010ulhAlmMsaSoftGlobAlarmTest_Type()
)
pm10010ulhAlmMsaSoftGlobAlarmTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmMsaSoftGlobAlarmTest.setStatus("current")
_Pm10010ulhAlmMsaNetworkHostAlarmStatus_Type = EkiOnOff
_Pm10010ulhAlmMsaNetworkHostAlarmStatus_Object = MibScalar
pm10010ulhAlmMsaNetworkHostAlarmStatus = _Pm10010ulhAlmMsaNetworkHostAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 80, 6),
    _Pm10010ulhAlmMsaNetworkHostAlarmStatus_Type()
)
pm10010ulhAlmMsaNetworkHostAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmMsaNetworkHostAlarmStatus.setStatus("current")
_Pm10010ulhAlmMsaNetworkLaneAlarmWarning2_Type = EkiOnOff
_Pm10010ulhAlmMsaNetworkLaneAlarmWarning2_Object = MibScalar
pm10010ulhAlmMsaNetworkLaneAlarmWarning2 = _Pm10010ulhAlmMsaNetworkLaneAlarmWarning2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 80, 7),
    _Pm10010ulhAlmMsaNetworkLaneAlarmWarning2_Type()
)
pm10010ulhAlmMsaNetworkLaneAlarmWarning2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmMsaNetworkLaneAlarmWarning2.setStatus("current")
_Pm10010ulhAlmMsaModuleState_Type = EkiOnOff
_Pm10010ulhAlmMsaModuleState_Object = MibScalar
pm10010ulhAlmMsaModuleState = _Pm10010ulhAlmMsaModuleState_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 80, 8),
    _Pm10010ulhAlmMsaModuleState_Type()
)
pm10010ulhAlmMsaModuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmMsaModuleState.setStatus("current")
_Pm10010ulhAlmMsaModuleGeneralStatus_Type = EkiOnOff
_Pm10010ulhAlmMsaModuleGeneralStatus_Object = MibScalar
pm10010ulhAlmMsaModuleGeneralStatus = _Pm10010ulhAlmMsaModuleGeneralStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 80, 9),
    _Pm10010ulhAlmMsaModuleGeneralStatus_Type()
)
pm10010ulhAlmMsaModuleGeneralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmMsaModuleGeneralStatus.setStatus("current")
_Pm10010ulhAlmModuleFault_Type = EkiOnOff
_Pm10010ulhAlmModuleFault_Object = MibScalar
pm10010ulhAlmModuleFault = _Pm10010ulhAlmModuleFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 80, 10),
    _Pm10010ulhAlmModuleFault_Type()
)
pm10010ulhAlmModuleFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmModuleFault.setStatus("current")
_Pm10010ulhAlmMsaModuleAlarmWarning1_Type = EkiOnOff
_Pm10010ulhAlmMsaModuleAlarmWarning1_Object = MibScalar
pm10010ulhAlmMsaModuleAlarmWarning1 = _Pm10010ulhAlmMsaModuleAlarmWarning1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 80, 11),
    _Pm10010ulhAlmMsaModuleAlarmWarning1_Type()
)
pm10010ulhAlmMsaModuleAlarmWarning1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmMsaModuleAlarmWarning1.setStatus("current")
_Pm10010ulhAlmMsaModuleAlarmWarning2_Type = EkiOnOff
_Pm10010ulhAlmMsaModuleAlarmWarning2_Object = MibScalar
pm10010ulhAlmMsaModuleAlarmWarning2 = _Pm10010ulhAlmMsaModuleAlarmWarning2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 80, 12),
    _Pm10010ulhAlmMsaModuleAlarmWarning2_Type()
)
pm10010ulhAlmMsaModuleAlarmWarning2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmMsaModuleAlarmWarning2.setStatus("current")
_Pm10010ulhAlmMsaNetworkLaneAlarmWarning1_Type = EkiOnOff
_Pm10010ulhAlmMsaNetworkLaneAlarmWarning1_Object = MibScalar
pm10010ulhAlmMsaNetworkLaneAlarmWarning1 = _Pm10010ulhAlmMsaNetworkLaneAlarmWarning1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 80, 13),
    _Pm10010ulhAlmMsaNetworkLaneAlarmWarning1_Type()
)
pm10010ulhAlmMsaNetworkLaneAlarmWarning1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmMsaNetworkLaneAlarmWarning1.setStatus("current")
_Pm10010ulhAlmMsaNetworkLaneFaultStatus_Type = EkiOnOff
_Pm10010ulhAlmMsaNetworkLaneFaultStatus_Object = MibScalar
pm10010ulhAlmMsaNetworkLaneFaultStatus = _Pm10010ulhAlmMsaNetworkLaneFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 80, 14),
    _Pm10010ulhAlmMsaNetworkLaneFaultStatus_Type()
)
pm10010ulhAlmMsaNetworkLaneFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmMsaNetworkLaneFaultStatus.setStatus("current")
_Pm10010ulhAlmMsaHostLaneFaultStatus_Type = EkiOnOff
_Pm10010ulhAlmMsaHostLaneFaultStatus_Object = MibScalar
pm10010ulhAlmMsaHostLaneFaultStatus = _Pm10010ulhAlmMsaHostLaneFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 80, 15),
    _Pm10010ulhAlmMsaHostLaneFaultStatus_Type()
)
pm10010ulhAlmMsaHostLaneFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmMsaHostLaneFaultStatus.setStatus("current")
_Pm10010ulhAlmMsaGlobAlarmAssertion_Type = EkiOnOff
_Pm10010ulhAlmMsaGlobAlarmAssertion_Object = MibScalar
pm10010ulhAlmMsaGlobAlarmAssertion = _Pm10010ulhAlmMsaGlobAlarmAssertion_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 80, 16),
    _Pm10010ulhAlmMsaGlobAlarmAssertion_Type()
)
pm10010ulhAlmMsaGlobAlarmAssertion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmMsaGlobAlarmAssertion.setStatus("current")
_Pm10010ulhAlmmsaNetworkTxAlignment_ObjectIdentity = ObjectIdentity
pm10010ulhAlmmsaNetworkTxAlignment = _Pm10010ulhAlmmsaNetworkTxAlignment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 81)
)
_Pm10010ulhAlmNetTxTimingFault_Type = EkiOnOff
_Pm10010ulhAlmNetTxTimingFault_Object = MibScalar
pm10010ulhAlmNetTxTimingFault = _Pm10010ulhAlmNetTxTimingFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 81, 12),
    _Pm10010ulhAlmNetTxTimingFault_Type()
)
pm10010ulhAlmNetTxTimingFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmNetTxTimingFault.setStatus("current")
_Pm10010ulhAlmNetTxReferenceClockFault_Type = EkiOnOff
_Pm10010ulhAlmNetTxReferenceClockFault_Object = MibScalar
pm10010ulhAlmNetTxReferenceClockFault = _Pm10010ulhAlmNetTxReferenceClockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 81, 13),
    _Pm10010ulhAlmNetTxReferenceClockFault_Type()
)
pm10010ulhAlmNetTxReferenceClockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmNetTxReferenceClockFault.setStatus("current")
_Pm10010ulhAlmNetTxCmuLockFault_Type = EkiOnOff
_Pm10010ulhAlmNetTxCmuLockFault_Object = MibScalar
pm10010ulhAlmNetTxCmuLockFault = _Pm10010ulhAlmNetTxCmuLockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 81, 14),
    _Pm10010ulhAlmNetTxCmuLockFault_Type()
)
pm10010ulhAlmNetTxCmuLockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmNetTxCmuLockFault.setStatus("current")
_Pm10010ulhAlmNetTxOutOfAlignment_Type = EkiOnOff
_Pm10010ulhAlmNetTxOutOfAlignment_Object = MibScalar
pm10010ulhAlmNetTxOutOfAlignment = _Pm10010ulhAlmNetTxOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 81, 15),
    _Pm10010ulhAlmNetTxOutOfAlignment_Type()
)
pm10010ulhAlmNetTxOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmNetTxOutOfAlignment.setStatus("current")
_Pm10010ulhAlmNetTxLossOfAlignment_Type = EkiOnOff
_Pm10010ulhAlmNetTxLossOfAlignment_Object = MibScalar
pm10010ulhAlmNetTxLossOfAlignment = _Pm10010ulhAlmNetTxLossOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 81, 16),
    _Pm10010ulhAlmNetTxLossOfAlignment_Type()
)
pm10010ulhAlmNetTxLossOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmNetTxLossOfAlignment.setStatus("current")
_Pm10010ulhAlmmsaNetworkRxAlignment_ObjectIdentity = ObjectIdentity
pm10010ulhAlmmsaNetworkRxAlignment = _Pm10010ulhAlmmsaNetworkRxAlignment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 82)
)
_Pm10010ulhAlmNetRxTimingFault_Type = EkiOnOff
_Pm10010ulhAlmNetRxTimingFault_Object = MibScalar
pm10010ulhAlmNetRxTimingFault = _Pm10010ulhAlmNetRxTimingFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 82, 12),
    _Pm10010ulhAlmNetRxTimingFault_Type()
)
pm10010ulhAlmNetRxTimingFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmNetRxTimingFault.setStatus("current")
_Pm10010ulhAlmNetRxOutOfAlignment_Type = EkiOnOff
_Pm10010ulhAlmNetRxOutOfAlignment_Object = MibScalar
pm10010ulhAlmNetRxOutOfAlignment = _Pm10010ulhAlmNetRxOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 82, 13),
    _Pm10010ulhAlmNetRxOutOfAlignment_Type()
)
pm10010ulhAlmNetRxOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmNetRxOutOfAlignment.setStatus("current")
_Pm10010ulhAlmNetRxLossOfAlignment_Type = EkiOnOff
_Pm10010ulhAlmNetRxLossOfAlignment_Object = MibScalar
pm10010ulhAlmNetRxLossOfAlignment = _Pm10010ulhAlmNetRxLossOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 82, 14),
    _Pm10010ulhAlmNetRxLossOfAlignment_Type()
)
pm10010ulhAlmNetRxLossOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmNetRxLossOfAlignment.setStatus("current")
_Pm10010ulhAlmNetRxModemLockFault_Type = EkiOnOff
_Pm10010ulhAlmNetRxModemLockFault_Object = MibScalar
pm10010ulhAlmNetRxModemLockFault = _Pm10010ulhAlmNetRxModemLockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 82, 15),
    _Pm10010ulhAlmNetRxModemLockFault_Type()
)
pm10010ulhAlmNetRxModemLockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmNetRxModemLockFault.setStatus("current")
_Pm10010ulhAlmNetRxModemSyncDetectFault_Type = EkiOnOff
_Pm10010ulhAlmNetRxModemSyncDetectFault_Object = MibScalar
pm10010ulhAlmNetRxModemSyncDetectFault = _Pm10010ulhAlmNetRxModemSyncDetectFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 82, 16),
    _Pm10010ulhAlmNetRxModemSyncDetectFault_Type()
)
pm10010ulhAlmNetRxModemSyncDetectFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmNetRxModemSyncDetectFault.setStatus("current")
_Pm10010ulhAlmmsaNetworkHostNetworkAlarmSummary_ObjectIdentity = ObjectIdentity
pm10010ulhAlmmsaNetworkHostNetworkAlarmSummary = _Pm10010ulhAlmmsaNetworkHostNetworkAlarmSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 83)
)
_Pm10010ulhAlmNetworkTxAlignment_Type = EkiOnOff
_Pm10010ulhAlmNetworkTxAlignment_Object = MibScalar
pm10010ulhAlmNetworkTxAlignment = _Pm10010ulhAlmNetworkTxAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 83, 11),
    _Pm10010ulhAlmNetworkTxAlignment_Type()
)
pm10010ulhAlmNetworkTxAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmNetworkTxAlignment.setStatus("current")
_Pm10010ulhAlmNetworkRxAlignment_Type = EkiOnOff
_Pm10010ulhAlmNetworkRxAlignment_Object = MibScalar
pm10010ulhAlmNetworkRxAlignment = _Pm10010ulhAlmNetworkRxAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 83, 12),
    _Pm10010ulhAlmNetworkRxAlignment_Type()
)
pm10010ulhAlmNetworkRxAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmNetworkRxAlignment.setStatus("current")
_Pm10010ulhAlmNetworkRxOtn_Type = EkiOnOff
_Pm10010ulhAlmNetworkRxOtn_Object = MibScalar
pm10010ulhAlmNetworkRxOtn = _Pm10010ulhAlmNetworkRxOtn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 83, 13),
    _Pm10010ulhAlmNetworkRxOtn_Type()
)
pm10010ulhAlmNetworkRxOtn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmNetworkRxOtn.setStatus("current")
_Pm10010ulhAlmHostRxAlignment_Type = EkiOnOff
_Pm10010ulhAlmHostRxAlignment_Object = MibScalar
pm10010ulhAlmHostRxAlignment = _Pm10010ulhAlmHostRxAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 83, 14),
    _Pm10010ulhAlmHostRxAlignment_Type()
)
pm10010ulhAlmHostRxAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmHostRxAlignment.setStatus("current")
_Pm10010ulhAlmHostTxAlignment_Type = EkiOnOff
_Pm10010ulhAlmHostTxAlignment_Object = MibScalar
pm10010ulhAlmHostTxAlignment = _Pm10010ulhAlmHostTxAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 83, 15),
    _Pm10010ulhAlmHostTxAlignment_Type()
)
pm10010ulhAlmHostTxAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmHostTxAlignment.setStatus("current")
_Pm10010ulhAlmHostTxOtnStatus_Type = EkiOnOff
_Pm10010ulhAlmHostTxOtnStatus_Object = MibScalar
pm10010ulhAlmHostTxOtnStatus = _Pm10010ulhAlmHostTxOtnStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 83, 16),
    _Pm10010ulhAlmHostTxOtnStatus_Type()
)
pm10010ulhAlmHostTxOtnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmHostTxOtnStatus.setStatus("current")
_Pm10010ulhAlmmsaHostTxAlignment_ObjectIdentity = ObjectIdentity
pm10010ulhAlmmsaHostTxAlignment = _Pm10010ulhAlmmsaHostTxAlignment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 84)
)
_Pm10010ulhAlmHostTxDeskewLockFault_Type = EkiOnOff
_Pm10010ulhAlmHostTxDeskewLockFault_Object = MibScalar
pm10010ulhAlmHostTxDeskewLockFault = _Pm10010ulhAlmHostTxDeskewLockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 84, 13),
    _Pm10010ulhAlmHostTxDeskewLockFault_Type()
)
pm10010ulhAlmHostTxDeskewLockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmHostTxDeskewLockFault.setStatus("current")
_Pm10010ulhAlmHostTxOutOfAlignment_Type = EkiOnOff
_Pm10010ulhAlmHostTxOutOfAlignment_Object = MibScalar
pm10010ulhAlmHostTxOutOfAlignment = _Pm10010ulhAlmHostTxOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 84, 14),
    _Pm10010ulhAlmHostTxOutOfAlignment_Type()
)
pm10010ulhAlmHostTxOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmHostTxOutOfAlignment.setStatus("current")
_Pm10010ulhAlmHostTxLossOfAlignment_Type = EkiOnOff
_Pm10010ulhAlmHostTxLossOfAlignment_Object = MibScalar
pm10010ulhAlmHostTxLossOfAlignment = _Pm10010ulhAlmHostTxLossOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 84, 15),
    _Pm10010ulhAlmHostTxLossOfAlignment_Type()
)
pm10010ulhAlmHostTxLossOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmHostTxLossOfAlignment.setStatus("current")
_Pm10010ulhAlmHostTxCdrLockFault_Type = EkiOnOff
_Pm10010ulhAlmHostTxCdrLockFault_Object = MibScalar
pm10010ulhAlmHostTxCdrLockFault = _Pm10010ulhAlmHostTxCdrLockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 84, 16),
    _Pm10010ulhAlmHostTxCdrLockFault_Type()
)
pm10010ulhAlmHostTxCdrLockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmHostTxCdrLockFault.setStatus("current")
_Pm10010ulhAlmmsaHostRxAlignment_ObjectIdentity = ObjectIdentity
pm10010ulhAlmmsaHostRxAlignment = _Pm10010ulhAlmmsaHostRxAlignment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 85)
)
_Pm10010ulhAlmHostRxCmuLockFault_Type = EkiOnOff
_Pm10010ulhAlmHostRxCmuLockFault_Object = MibScalar
pm10010ulhAlmHostRxCmuLockFault = _Pm10010ulhAlmHostRxCmuLockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 85, 14),
    _Pm10010ulhAlmHostRxCmuLockFault_Type()
)
pm10010ulhAlmHostRxCmuLockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmHostRxCmuLockFault.setStatus("current")
_Pm10010ulhAlmHostRxOutOfAlignment_Type = EkiOnOff
_Pm10010ulhAlmHostRxOutOfAlignment_Object = MibScalar
pm10010ulhAlmHostRxOutOfAlignment = _Pm10010ulhAlmHostRxOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 85, 15),
    _Pm10010ulhAlmHostRxOutOfAlignment_Type()
)
pm10010ulhAlmHostRxOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmHostRxOutOfAlignment.setStatus("current")
_Pm10010ulhAlmHostRxLossOfAlignment_Type = EkiOnOff
_Pm10010ulhAlmHostRxLossOfAlignment_Object = MibScalar
pm10010ulhAlmHostRxLossOfAlignment = _Pm10010ulhAlmHostRxLossOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 1, 3, 85, 16),
    _Pm10010ulhAlmHostRxLossOfAlignment_Type()
)
pm10010ulhAlmHostRxLossOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmHostRxLossOfAlignment.setStatus("current")
_Pm10010ulhAlmClient_ObjectIdentity = ObjectIdentity
pm10010ulhAlmClient = _Pm10010ulhAlmClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2)
)
_Pm10010ulhAlmClientNurg_ObjectIdentity = ObjectIdentity
pm10010ulhAlmClientNurg = _Pm10010ulhAlmClientNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 1)
)
_Pm10010ulhAlmclientNetworkLaneAlarmWarningTable_Object = MibTable
pm10010ulhAlmclientNetworkLaneAlarmWarningTable = _Pm10010ulhAlmclientNetworkLaneAlarmWarningTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 1, 88)
)
if mibBuilder.loadTexts:
    pm10010ulhAlmclientNetworkLaneAlarmWarningTable.setStatus("current")
_Pm10010ulhAlmclientNetworkLaneAlarmWarningEntry_Object = MibTableRow
pm10010ulhAlmclientNetworkLaneAlarmWarningEntry = _Pm10010ulhAlmclientNetworkLaneAlarmWarningEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 1, 88, 1)
)
pm10010ulhAlmclientNetworkLaneAlarmWarningEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhAlmclientNetworkLaneAlarmWarningIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhAlmclientNetworkLaneAlarmWarningEntry.setStatus("current")


class _Pm10010ulhAlmclientNetworkLaneAlarmWarningIndex_Type(Integer32):
    """Custom type pm10010ulhAlmclientNetworkLaneAlarmWarningIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhAlmclientNetworkLaneAlarmWarningIndex_Type.__name__ = "Integer32"
_Pm10010ulhAlmclientNetworkLaneAlarmWarningIndex_Object = MibTableColumn
pm10010ulhAlmclientNetworkLaneAlarmWarningIndex = _Pm10010ulhAlmclientNetworkLaneAlarmWarningIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 1, 88, 1, 1),
    _Pm10010ulhAlmclientNetworkLaneAlarmWarningIndex_Type()
)
pm10010ulhAlmclientNetworkLaneAlarmWarningIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmclientNetworkLaneAlarmWarningIndex.setStatus("current")
_Pm10010ulhAlmClientRxPowerLowAlarmPortn_Type = EkiOnOff
_Pm10010ulhAlmClientRxPowerLowAlarmPortn_Object = MibTableColumn
pm10010ulhAlmClientRxPowerLowAlarmPortn = _Pm10010ulhAlmClientRxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 1, 88, 1, 2),
    _Pm10010ulhAlmClientRxPowerLowAlarmPortn_Type()
)
pm10010ulhAlmClientRxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmClientRxPowerLowAlarmPortn.setStatus("current")
_Pm10010ulhAlmClientRxPowerLowWarningPortn_Type = EkiOnOff
_Pm10010ulhAlmClientRxPowerLowWarningPortn_Object = MibTableColumn
pm10010ulhAlmClientRxPowerLowWarningPortn = _Pm10010ulhAlmClientRxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 1, 88, 1, 3),
    _Pm10010ulhAlmClientRxPowerLowWarningPortn_Type()
)
pm10010ulhAlmClientRxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmClientRxPowerLowWarningPortn.setStatus("current")
_Pm10010ulhAlmClientRxPowerHighWarningPortn_Type = EkiOnOff
_Pm10010ulhAlmClientRxPowerHighWarningPortn_Object = MibTableColumn
pm10010ulhAlmClientRxPowerHighWarningPortn = _Pm10010ulhAlmClientRxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 1, 88, 1, 4),
    _Pm10010ulhAlmClientRxPowerHighWarningPortn_Type()
)
pm10010ulhAlmClientRxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmClientRxPowerHighWarningPortn.setStatus("current")
_Pm10010ulhAlmClientRxPowerHighAlarmPortn_Type = EkiOnOff
_Pm10010ulhAlmClientRxPowerHighAlarmPortn_Object = MibTableColumn
pm10010ulhAlmClientRxPowerHighAlarmPortn = _Pm10010ulhAlmClientRxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 1, 88, 1, 5),
    _Pm10010ulhAlmClientRxPowerHighAlarmPortn_Type()
)
pm10010ulhAlmClientRxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmClientRxPowerHighAlarmPortn.setStatus("current")
_Pm10010ulhAlmLaserTempLowAlarmPortn_Type = EkiOnOff
_Pm10010ulhAlmLaserTempLowAlarmPortn_Object = MibTableColumn
pm10010ulhAlmLaserTempLowAlarmPortn = _Pm10010ulhAlmLaserTempLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 1, 88, 1, 6),
    _Pm10010ulhAlmLaserTempLowAlarmPortn_Type()
)
pm10010ulhAlmLaserTempLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmLaserTempLowAlarmPortn.setStatus("current")
_Pm10010ulhAlmClientLaserTempLowWarningPortn_Type = EkiOnOff
_Pm10010ulhAlmClientLaserTempLowWarningPortn_Object = MibTableColumn
pm10010ulhAlmClientLaserTempLowWarningPortn = _Pm10010ulhAlmClientLaserTempLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 1, 88, 1, 7),
    _Pm10010ulhAlmClientLaserTempLowWarningPortn_Type()
)
pm10010ulhAlmClientLaserTempLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmClientLaserTempLowWarningPortn.setStatus("current")
_Pm10010ulhAlmClientLaserTempHighWarningPortn_Type = EkiOnOff
_Pm10010ulhAlmClientLaserTempHighWarningPortn_Object = MibTableColumn
pm10010ulhAlmClientLaserTempHighWarningPortn = _Pm10010ulhAlmClientLaserTempHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 1, 88, 1, 8),
    _Pm10010ulhAlmClientLaserTempHighWarningPortn_Type()
)
pm10010ulhAlmClientLaserTempHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmClientLaserTempHighWarningPortn.setStatus("current")
_Pm10010ulhAlmClientLaserTempHighAlarmPortn_Type = EkiOnOff
_Pm10010ulhAlmClientLaserTempHighAlarmPortn_Object = MibTableColumn
pm10010ulhAlmClientLaserTempHighAlarmPortn = _Pm10010ulhAlmClientLaserTempHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 1, 88, 1, 9),
    _Pm10010ulhAlmClientLaserTempHighAlarmPortn_Type()
)
pm10010ulhAlmClientLaserTempHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmClientLaserTempHighAlarmPortn.setStatus("current")
_Pm10010ulhAlmClientTxPowerLowAlarmPortn_Type = EkiOnOff
_Pm10010ulhAlmClientTxPowerLowAlarmPortn_Object = MibTableColumn
pm10010ulhAlmClientTxPowerLowAlarmPortn = _Pm10010ulhAlmClientTxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 1, 88, 1, 10),
    _Pm10010ulhAlmClientTxPowerLowAlarmPortn_Type()
)
pm10010ulhAlmClientTxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmClientTxPowerLowAlarmPortn.setStatus("current")
_Pm10010ulhAlmClientTxPowerLowWarningPortn_Type = EkiOnOff
_Pm10010ulhAlmClientTxPowerLowWarningPortn_Object = MibTableColumn
pm10010ulhAlmClientTxPowerLowWarningPortn = _Pm10010ulhAlmClientTxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 1, 88, 1, 11),
    _Pm10010ulhAlmClientTxPowerLowWarningPortn_Type()
)
pm10010ulhAlmClientTxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmClientTxPowerLowWarningPortn.setStatus("current")
_Pm10010ulhAlmClientTxPowerHighWarningPortn_Type = EkiOnOff
_Pm10010ulhAlmClientTxPowerHighWarningPortn_Object = MibTableColumn
pm10010ulhAlmClientTxPowerHighWarningPortn = _Pm10010ulhAlmClientTxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 1, 88, 1, 12),
    _Pm10010ulhAlmClientTxPowerHighWarningPortn_Type()
)
pm10010ulhAlmClientTxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmClientTxPowerHighWarningPortn.setStatus("current")
_Pm10010ulhAlmClientTxPowerHighAlarmPortn_Type = EkiOnOff
_Pm10010ulhAlmClientTxPowerHighAlarmPortn_Object = MibTableColumn
pm10010ulhAlmClientTxPowerHighAlarmPortn = _Pm10010ulhAlmClientTxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 1, 88, 1, 13),
    _Pm10010ulhAlmClientTxPowerHighAlarmPortn_Type()
)
pm10010ulhAlmClientTxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmClientTxPowerHighAlarmPortn.setStatus("current")
_Pm10010ulhAlmClientBiasLowAlarmPortn_Type = EkiOnOff
_Pm10010ulhAlmClientBiasLowAlarmPortn_Object = MibTableColumn
pm10010ulhAlmClientBiasLowAlarmPortn = _Pm10010ulhAlmClientBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 1, 88, 1, 14),
    _Pm10010ulhAlmClientBiasLowAlarmPortn_Type()
)
pm10010ulhAlmClientBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmClientBiasLowAlarmPortn.setStatus("current")
_Pm10010ulhAlmClientBiasLowWarningPortn_Type = EkiOnOff
_Pm10010ulhAlmClientBiasLowWarningPortn_Object = MibTableColumn
pm10010ulhAlmClientBiasLowWarningPortn = _Pm10010ulhAlmClientBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 1, 88, 1, 15),
    _Pm10010ulhAlmClientBiasLowWarningPortn_Type()
)
pm10010ulhAlmClientBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmClientBiasLowWarningPortn.setStatus("current")
_Pm10010ulhAlmClientBiasHighWarningPortn_Type = EkiOnOff
_Pm10010ulhAlmClientBiasHighWarningPortn_Object = MibTableColumn
pm10010ulhAlmClientBiasHighWarningPortn = _Pm10010ulhAlmClientBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 1, 88, 1, 16),
    _Pm10010ulhAlmClientBiasHighWarningPortn_Type()
)
pm10010ulhAlmClientBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmClientBiasHighWarningPortn.setStatus("current")
_Pm10010ulhAlmClientBiasHighAlarmPortn_Type = EkiOnOff
_Pm10010ulhAlmClientBiasHighAlarmPortn_Object = MibTableColumn
pm10010ulhAlmClientBiasHighAlarmPortn = _Pm10010ulhAlmClientBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 1, 88, 1, 17),
    _Pm10010ulhAlmClientBiasHighAlarmPortn_Type()
)
pm10010ulhAlmClientBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmClientBiasHighAlarmPortn.setStatus("current")
_Pm10010ulhAlmclientSfpWarnDdmTable_Object = MibTable
pm10010ulhAlmclientSfpWarnDdmTable = _Pm10010ulhAlmclientSfpWarnDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 1, 272)
)
if mibBuilder.loadTexts:
    pm10010ulhAlmclientSfpWarnDdmTable.setStatus("current")
_Pm10010ulhAlmclientSfpWarnDdmEntry_Object = MibTableRow
pm10010ulhAlmclientSfpWarnDdmEntry = _Pm10010ulhAlmclientSfpWarnDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 1, 272, 1)
)
pm10010ulhAlmclientSfpWarnDdmEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhAlmclientSfpWarnDdmIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhAlmclientSfpWarnDdmEntry.setStatus("current")


class _Pm10010ulhAlmclientSfpWarnDdmIndex_Type(Integer32):
    """Custom type pm10010ulhAlmclientSfpWarnDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhAlmclientSfpWarnDdmIndex_Type.__name__ = "Integer32"
_Pm10010ulhAlmclientSfpWarnDdmIndex_Object = MibTableColumn
pm10010ulhAlmclientSfpWarnDdmIndex = _Pm10010ulhAlmclientSfpWarnDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 1, 272, 1, 1),
    _Pm10010ulhAlmclientSfpWarnDdmIndex_Type()
)
pm10010ulhAlmclientSfpWarnDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmclientSfpWarnDdmIndex.setStatus("current")
_Pm10010ulhAlmTxPwLowWngPortn_Type = EkiOnOff
_Pm10010ulhAlmTxPwLowWngPortn_Object = MibTableColumn
pm10010ulhAlmTxPwLowWngPortn = _Pm10010ulhAlmTxPwLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 1, 272, 1, 2),
    _Pm10010ulhAlmTxPwLowWngPortn_Type()
)
pm10010ulhAlmTxPwLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmTxPwLowWngPortn.setStatus("current")
_Pm10010ulhAlmTxPwrHighWngPortn_Type = EkiOnOff
_Pm10010ulhAlmTxPwrHighWngPortn_Object = MibTableColumn
pm10010ulhAlmTxPwrHighWngPortn = _Pm10010ulhAlmTxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 1, 272, 1, 3),
    _Pm10010ulhAlmTxPwrHighWngPortn_Type()
)
pm10010ulhAlmTxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmTxPwrHighWngPortn.setStatus("current")
_Pm10010ulhAlmTxBiasLowWngPortn_Type = EkiOnOff
_Pm10010ulhAlmTxBiasLowWngPortn_Object = MibTableColumn
pm10010ulhAlmTxBiasLowWngPortn = _Pm10010ulhAlmTxBiasLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 1, 272, 1, 4),
    _Pm10010ulhAlmTxBiasLowWngPortn_Type()
)
pm10010ulhAlmTxBiasLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmTxBiasLowWngPortn.setStatus("current")
_Pm10010ulhAlmTxBiasHighWngPortn_Type = EkiOnOff
_Pm10010ulhAlmTxBiasHighWngPortn_Object = MibTableColumn
pm10010ulhAlmTxBiasHighWngPortn = _Pm10010ulhAlmTxBiasHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 1, 272, 1, 5),
    _Pm10010ulhAlmTxBiasHighWngPortn_Type()
)
pm10010ulhAlmTxBiasHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmTxBiasHighWngPortn.setStatus("current")
_Pm10010ulhAlmVccLowWngPortn_Type = EkiOnOff
_Pm10010ulhAlmVccLowWngPortn_Object = MibTableColumn
pm10010ulhAlmVccLowWngPortn = _Pm10010ulhAlmVccLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 1, 272, 1, 6),
    _Pm10010ulhAlmVccLowWngPortn_Type()
)
pm10010ulhAlmVccLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmVccLowWngPortn.setStatus("current")
_Pm10010ulhAlmVccHighWngPortn_Type = EkiOnOff
_Pm10010ulhAlmVccHighWngPortn_Object = MibTableColumn
pm10010ulhAlmVccHighWngPortn = _Pm10010ulhAlmVccHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 1, 272, 1, 7),
    _Pm10010ulhAlmVccHighWngPortn_Type()
)
pm10010ulhAlmVccHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmVccHighWngPortn.setStatus("current")
_Pm10010ulhAlmTempLowWngPortn_Type = EkiOnOff
_Pm10010ulhAlmTempLowWngPortn_Object = MibTableColumn
pm10010ulhAlmTempLowWngPortn = _Pm10010ulhAlmTempLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 1, 272, 1, 8),
    _Pm10010ulhAlmTempLowWngPortn_Type()
)
pm10010ulhAlmTempLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmTempLowWngPortn.setStatus("current")
_Pm10010ulhAlmTempHighWngPortn_Type = EkiOnOff
_Pm10010ulhAlmTempHighWngPortn_Object = MibTableColumn
pm10010ulhAlmTempHighWngPortn = _Pm10010ulhAlmTempHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 1, 272, 1, 9),
    _Pm10010ulhAlmTempHighWngPortn_Type()
)
pm10010ulhAlmTempHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmTempHighWngPortn.setStatus("current")
_Pm10010ulhAlmRxPwrLowWngPortn_Type = EkiOnOff
_Pm10010ulhAlmRxPwrLowWngPortn_Object = MibTableColumn
pm10010ulhAlmRxPwrLowWngPortn = _Pm10010ulhAlmRxPwrLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 1, 272, 1, 16),
    _Pm10010ulhAlmRxPwrLowWngPortn_Type()
)
pm10010ulhAlmRxPwrLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmRxPwrLowWngPortn.setStatus("current")
_Pm10010ulhAlmRxPwrHighWngPortn_Type = EkiOnOff
_Pm10010ulhAlmRxPwrHighWngPortn_Object = MibTableColumn
pm10010ulhAlmRxPwrHighWngPortn = _Pm10010ulhAlmRxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 1, 272, 1, 17),
    _Pm10010ulhAlmRxPwrHighWngPortn_Type()
)
pm10010ulhAlmRxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmRxPwrHighWngPortn.setStatus("current")
_Pm10010ulhAlmClientUrg_ObjectIdentity = ObjectIdentity
pm10010ulhAlmClientUrg = _Pm10010ulhAlmClientUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 2)
)
_Pm10010ulhAlmclientNetworkLaneFaultTable_Object = MibTable
pm10010ulhAlmclientNetworkLaneFaultTable = _Pm10010ulhAlmclientNetworkLaneFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 2, 120)
)
if mibBuilder.loadTexts:
    pm10010ulhAlmclientNetworkLaneFaultTable.setStatus("current")
_Pm10010ulhAlmclientNetworkLaneFaultEntry_Object = MibTableRow
pm10010ulhAlmclientNetworkLaneFaultEntry = _Pm10010ulhAlmclientNetworkLaneFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 2, 120, 1)
)
pm10010ulhAlmclientNetworkLaneFaultEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhAlmclientNetworkLaneFaultIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhAlmclientNetworkLaneFaultEntry.setStatus("current")


class _Pm10010ulhAlmclientNetworkLaneFaultIndex_Type(Integer32):
    """Custom type pm10010ulhAlmclientNetworkLaneFaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhAlmclientNetworkLaneFaultIndex_Type.__name__ = "Integer32"
_Pm10010ulhAlmclientNetworkLaneFaultIndex_Object = MibTableColumn
pm10010ulhAlmclientNetworkLaneFaultIndex = _Pm10010ulhAlmclientNetworkLaneFaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 2, 120, 1, 1),
    _Pm10010ulhAlmclientNetworkLaneFaultIndex_Type()
)
pm10010ulhAlmclientNetworkLaneFaultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmclientNetworkLaneFaultIndex.setStatus("current")
_Pm10010ulhAlmClientLaneRxFifoErrorPortn_Type = EkiOnOff
_Pm10010ulhAlmClientLaneRxFifoErrorPortn_Object = MibTableColumn
pm10010ulhAlmClientLaneRxFifoErrorPortn = _Pm10010ulhAlmClientLaneRxFifoErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 2, 120, 1, 4),
    _Pm10010ulhAlmClientLaneRxFifoErrorPortn_Type()
)
pm10010ulhAlmClientLaneRxFifoErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmClientLaneRxFifoErrorPortn.setStatus("current")
_Pm10010ulhAlmClientLaneRxLolPortn_Type = EkiOnOff
_Pm10010ulhAlmClientLaneRxLolPortn_Object = MibTableColumn
pm10010ulhAlmClientLaneRxLolPortn = _Pm10010ulhAlmClientLaneRxLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 2, 120, 1, 5),
    _Pm10010ulhAlmClientLaneRxLolPortn_Type()
)
pm10010ulhAlmClientLaneRxLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmClientLaneRxLolPortn.setStatus("current")
_Pm10010ulhAlmClientLaneRxLosPortn_Type = EkiOnOff
_Pm10010ulhAlmClientLaneRxLosPortn_Object = MibTableColumn
pm10010ulhAlmClientLaneRxLosPortn = _Pm10010ulhAlmClientLaneRxLosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 2, 120, 1, 6),
    _Pm10010ulhAlmClientLaneRxLosPortn_Type()
)
pm10010ulhAlmClientLaneRxLosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmClientLaneRxLosPortn.setStatus("current")
_Pm10010ulhAlmClientLaneTxLolPortn_Type = EkiOnOff
_Pm10010ulhAlmClientLaneTxLolPortn_Object = MibTableColumn
pm10010ulhAlmClientLaneTxLolPortn = _Pm10010ulhAlmClientLaneTxLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 2, 120, 1, 8),
    _Pm10010ulhAlmClientLaneTxLolPortn_Type()
)
pm10010ulhAlmClientLaneTxLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmClientLaneTxLolPortn.setStatus("current")
_Pm10010ulhAlmClientLaneTxLosfPortn_Type = EkiOnOff
_Pm10010ulhAlmClientLaneTxLosfPortn_Object = MibTableColumn
pm10010ulhAlmClientLaneTxLosfPortn = _Pm10010ulhAlmClientLaneTxLosfPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 2, 120, 1, 9),
    _Pm10010ulhAlmClientLaneTxLosfPortn_Type()
)
pm10010ulhAlmClientLaneTxLosfPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmClientLaneTxLosfPortn.setStatus("current")
_Pm10010ulhAlmClientLaneApdPowerSupplyPortn_Type = EkiOnOff
_Pm10010ulhAlmClientLaneApdPowerSupplyPortn_Object = MibTableColumn
pm10010ulhAlmClientLaneApdPowerSupplyPortn = _Pm10010ulhAlmClientLaneApdPowerSupplyPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 2, 120, 1, 15),
    _Pm10010ulhAlmClientLaneApdPowerSupplyPortn_Type()
)
pm10010ulhAlmClientLaneApdPowerSupplyPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmClientLaneApdPowerSupplyPortn.setStatus("current")
_Pm10010ulhAlmClientLaneWavelengthUnlockedPortn_Type = EkiOnOff
_Pm10010ulhAlmClientLaneWavelengthUnlockedPortn_Object = MibTableColumn
pm10010ulhAlmClientLaneWavelengthUnlockedPortn = _Pm10010ulhAlmClientLaneWavelengthUnlockedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 2, 120, 1, 16),
    _Pm10010ulhAlmClientLaneWavelengthUnlockedPortn_Type()
)
pm10010ulhAlmClientLaneWavelengthUnlockedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmClientLaneWavelengthUnlockedPortn.setStatus("current")
_Pm10010ulhAlmClientLaneTecFaultPortn_Type = EkiOnOff
_Pm10010ulhAlmClientLaneTecFaultPortn_Object = MibTableColumn
pm10010ulhAlmClientLaneTecFaultPortn = _Pm10010ulhAlmClientLaneTecFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 2, 120, 1, 17),
    _Pm10010ulhAlmClientLaneTecFaultPortn_Type()
)
pm10010ulhAlmClientLaneTecFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmClientLaneTecFaultPortn.setStatus("current")
_Pm10010ulhAlmclientHostLaneFaultTable_Object = MibTable
pm10010ulhAlmclientHostLaneFaultTable = _Pm10010ulhAlmclientHostLaneFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 2, 152)
)
if mibBuilder.loadTexts:
    pm10010ulhAlmclientHostLaneFaultTable.setStatus("current")
_Pm10010ulhAlmclientHostLaneFaultEntry_Object = MibTableRow
pm10010ulhAlmclientHostLaneFaultEntry = _Pm10010ulhAlmclientHostLaneFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 2, 152, 1)
)
pm10010ulhAlmclientHostLaneFaultEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhAlmclientHostLaneFaultIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhAlmclientHostLaneFaultEntry.setStatus("current")


class _Pm10010ulhAlmclientHostLaneFaultIndex_Type(Integer32):
    """Custom type pm10010ulhAlmclientHostLaneFaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhAlmclientHostLaneFaultIndex_Type.__name__ = "Integer32"
_Pm10010ulhAlmclientHostLaneFaultIndex_Object = MibTableColumn
pm10010ulhAlmclientHostLaneFaultIndex = _Pm10010ulhAlmclientHostLaneFaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 2, 152, 1, 1),
    _Pm10010ulhAlmclientHostLaneFaultIndex_Type()
)
pm10010ulhAlmclientHostLaneFaultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmclientHostLaneFaultIndex.setStatus("current")
_Pm10010ulhAlmClientLossOfSyncPortn_Type = EkiOnOff
_Pm10010ulhAlmClientLossOfSyncPortn_Object = MibTableColumn
pm10010ulhAlmClientLossOfSyncPortn = _Pm10010ulhAlmClientLossOfSyncPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 2, 152, 1, 2),
    _Pm10010ulhAlmClientLossOfSyncPortn_Type()
)
pm10010ulhAlmClientLossOfSyncPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmClientLossOfSyncPortn.setStatus("current")
_Pm10010ulhAlmClientInputLossOfSigPortn_Type = EkiOnOff
_Pm10010ulhAlmClientInputLossOfSigPortn_Object = MibTableColumn
pm10010ulhAlmClientInputLossOfSigPortn = _Pm10010ulhAlmClientInputLossOfSigPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 2, 152, 1, 3),
    _Pm10010ulhAlmClientInputLossOfSigPortn_Type()
)
pm10010ulhAlmClientInputLossOfSigPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmClientInputLossOfSigPortn.setStatus("current")
_Pm10010ulhAlmClientLanesMarkerUnlockPortn_Type = EkiOnOff
_Pm10010ulhAlmClientLanesMarkerUnlockPortn_Object = MibTableColumn
pm10010ulhAlmClientLanesMarkerUnlockPortn = _Pm10010ulhAlmClientLanesMarkerUnlockPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 2, 152, 1, 4),
    _Pm10010ulhAlmClientLanesMarkerUnlockPortn_Type()
)
pm10010ulhAlmClientLanesMarkerUnlockPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmClientLanesMarkerUnlockPortn.setStatus("current")
_Pm10010ulhAlmClientLanes6466UnlockPortn_Type = EkiOnOff
_Pm10010ulhAlmClientLanes6466UnlockPortn_Object = MibTableColumn
pm10010ulhAlmClientLanes6466UnlockPortn = _Pm10010ulhAlmClientLanes6466UnlockPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 2, 152, 1, 5),
    _Pm10010ulhAlmClientLanes6466UnlockPortn_Type()
)
pm10010ulhAlmClientLanes6466UnlockPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmClientLanes6466UnlockPortn.setStatus("current")
_Pm10010ulhAlmClientLanesNotAlignedPortn_Type = EkiOnOff
_Pm10010ulhAlmClientLanesNotAlignedPortn_Object = MibTableColumn
pm10010ulhAlmClientLanesNotAlignedPortn = _Pm10010ulhAlmClientLanesNotAlignedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 2, 152, 1, 6),
    _Pm10010ulhAlmClientLanesNotAlignedPortn_Type()
)
pm10010ulhAlmClientLanesNotAlignedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmClientLanesNotAlignedPortn.setStatus("current")
_Pm10010ulhAlmClientCsfDetectedPortn_Type = EkiOnOff
_Pm10010ulhAlmClientCsfDetectedPortn_Object = MibTableColumn
pm10010ulhAlmClientCsfDetectedPortn = _Pm10010ulhAlmClientCsfDetectedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 2, 152, 1, 7),
    _Pm10010ulhAlmClientCsfDetectedPortn_Type()
)
pm10010ulhAlmClientCsfDetectedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmClientCsfDetectedPortn.setStatus("current")
_Pm10010ulhAlmClientTxHostLolPortn_Type = EkiOnOff
_Pm10010ulhAlmClientTxHostLolPortn_Object = MibTableColumn
pm10010ulhAlmClientTxHostLolPortn = _Pm10010ulhAlmClientTxHostLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 2, 152, 1, 10),
    _Pm10010ulhAlmClientTxHostLolPortn_Type()
)
pm10010ulhAlmClientTxHostLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmClientTxHostLolPortn.setStatus("current")
_Pm10010ulhAlmClientLaneTxFifoErrorPortn_Type = EkiOnOff
_Pm10010ulhAlmClientLaneTxFifoErrorPortn_Object = MibTableColumn
pm10010ulhAlmClientLaneTxFifoErrorPortn = _Pm10010ulhAlmClientLaneTxFifoErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 2, 152, 1, 11),
    _Pm10010ulhAlmClientLaneTxFifoErrorPortn_Type()
)
pm10010ulhAlmClientLaneTxFifoErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmClientLaneTxFifoErrorPortn.setStatus("current")
_Pm10010ulhAlmclientSfpAlmDdmTable_Object = MibTable
pm10010ulhAlmclientSfpAlmDdmTable = _Pm10010ulhAlmclientSfpAlmDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 2, 240)
)
if mibBuilder.loadTexts:
    pm10010ulhAlmclientSfpAlmDdmTable.setStatus("current")
_Pm10010ulhAlmclientSfpAlmDdmEntry_Object = MibTableRow
pm10010ulhAlmclientSfpAlmDdmEntry = _Pm10010ulhAlmclientSfpAlmDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 2, 240, 1)
)
pm10010ulhAlmclientSfpAlmDdmEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhAlmclientSfpAlmDdmIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhAlmclientSfpAlmDdmEntry.setStatus("current")


class _Pm10010ulhAlmclientSfpAlmDdmIndex_Type(Integer32):
    """Custom type pm10010ulhAlmclientSfpAlmDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhAlmclientSfpAlmDdmIndex_Type.__name__ = "Integer32"
_Pm10010ulhAlmclientSfpAlmDdmIndex_Object = MibTableColumn
pm10010ulhAlmclientSfpAlmDdmIndex = _Pm10010ulhAlmclientSfpAlmDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 2, 240, 1, 1),
    _Pm10010ulhAlmclientSfpAlmDdmIndex_Type()
)
pm10010ulhAlmclientSfpAlmDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmclientSfpAlmDdmIndex.setStatus("current")
_Pm10010ulhAlmTxPwrLowAlaPortn_Type = EkiOnOff
_Pm10010ulhAlmTxPwrLowAlaPortn_Object = MibTableColumn
pm10010ulhAlmTxPwrLowAlaPortn = _Pm10010ulhAlmTxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 2, 240, 1, 2),
    _Pm10010ulhAlmTxPwrLowAlaPortn_Type()
)
pm10010ulhAlmTxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmTxPwrLowAlaPortn.setStatus("current")
_Pm10010ulhAlmTxPwrHighAlaPortn_Type = EkiOnOff
_Pm10010ulhAlmTxPwrHighAlaPortn_Object = MibTableColumn
pm10010ulhAlmTxPwrHighAlaPortn = _Pm10010ulhAlmTxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 2, 240, 1, 3),
    _Pm10010ulhAlmTxPwrHighAlaPortn_Type()
)
pm10010ulhAlmTxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmTxPwrHighAlaPortn.setStatus("current")
_Pm10010ulhAlmTxBiasLowAlaPortn_Type = EkiOnOff
_Pm10010ulhAlmTxBiasLowAlaPortn_Object = MibTableColumn
pm10010ulhAlmTxBiasLowAlaPortn = _Pm10010ulhAlmTxBiasLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 2, 240, 1, 4),
    _Pm10010ulhAlmTxBiasLowAlaPortn_Type()
)
pm10010ulhAlmTxBiasLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmTxBiasLowAlaPortn.setStatus("current")
_Pm10010ulhAlmTxBiasHighAlaPortn_Type = EkiOnOff
_Pm10010ulhAlmTxBiasHighAlaPortn_Object = MibTableColumn
pm10010ulhAlmTxBiasHighAlaPortn = _Pm10010ulhAlmTxBiasHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 2, 240, 1, 5),
    _Pm10010ulhAlmTxBiasHighAlaPortn_Type()
)
pm10010ulhAlmTxBiasHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmTxBiasHighAlaPortn.setStatus("current")
_Pm10010ulhAlmVccLowAlaPortn_Type = EkiOnOff
_Pm10010ulhAlmVccLowAlaPortn_Object = MibTableColumn
pm10010ulhAlmVccLowAlaPortn = _Pm10010ulhAlmVccLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 2, 240, 1, 6),
    _Pm10010ulhAlmVccLowAlaPortn_Type()
)
pm10010ulhAlmVccLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmVccLowAlaPortn.setStatus("current")
_Pm10010ulhAlmVccHighAlaPortn_Type = EkiOnOff
_Pm10010ulhAlmVccHighAlaPortn_Object = MibTableColumn
pm10010ulhAlmVccHighAlaPortn = _Pm10010ulhAlmVccHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 2, 240, 1, 7),
    _Pm10010ulhAlmVccHighAlaPortn_Type()
)
pm10010ulhAlmVccHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmVccHighAlaPortn.setStatus("current")
_Pm10010ulhAlmTempLowAlaPortn_Type = EkiOnOff
_Pm10010ulhAlmTempLowAlaPortn_Object = MibTableColumn
pm10010ulhAlmTempLowAlaPortn = _Pm10010ulhAlmTempLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 2, 240, 1, 8),
    _Pm10010ulhAlmTempLowAlaPortn_Type()
)
pm10010ulhAlmTempLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmTempLowAlaPortn.setStatus("current")
_Pm10010ulhAlmTempHighAlaPortn_Type = EkiOnOff
_Pm10010ulhAlmTempHighAlaPortn_Object = MibTableColumn
pm10010ulhAlmTempHighAlaPortn = _Pm10010ulhAlmTempHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 2, 240, 1, 9),
    _Pm10010ulhAlmTempHighAlaPortn_Type()
)
pm10010ulhAlmTempHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmTempHighAlaPortn.setStatus("current")
_Pm10010ulhAlmRxPwrLowAlaPortn_Type = EkiOnOff
_Pm10010ulhAlmRxPwrLowAlaPortn_Object = MibTableColumn
pm10010ulhAlmRxPwrLowAlaPortn = _Pm10010ulhAlmRxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 2, 240, 1, 16),
    _Pm10010ulhAlmRxPwrLowAlaPortn_Type()
)
pm10010ulhAlmRxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmRxPwrLowAlaPortn.setStatus("current")
_Pm10010ulhAlmRxPwrHighAlaPortn_Type = EkiOnOff
_Pm10010ulhAlmRxPwrHighAlaPortn_Object = MibTableColumn
pm10010ulhAlmRxPwrHighAlaPortn = _Pm10010ulhAlmRxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 2, 240, 1, 17),
    _Pm10010ulhAlmRxPwrHighAlaPortn_Type()
)
pm10010ulhAlmRxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmRxPwrHighAlaPortn.setStatus("current")
_Pm10010ulhAlmClientCrit_ObjectIdentity = ObjectIdentity
pm10010ulhAlmClientCrit = _Pm10010ulhAlmClientCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 3)
)
_Pm10010ulhAlmsynthAlmPortTable_Object = MibTable
pm10010ulhAlmsynthAlmPortTable = _Pm10010ulhAlmsynthAlmPortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 3, 8)
)
if mibBuilder.loadTexts:
    pm10010ulhAlmsynthAlmPortTable.setStatus("current")
_Pm10010ulhAlmsynthAlmPortEntry_Object = MibTableRow
pm10010ulhAlmsynthAlmPortEntry = _Pm10010ulhAlmsynthAlmPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 3, 8, 1)
)
pm10010ulhAlmsynthAlmPortEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhAlmsynthAlmPortIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhAlmsynthAlmPortEntry.setStatus("current")


class _Pm10010ulhAlmsynthAlmPortIndex_Type(Integer32):
    """Custom type pm10010ulhAlmsynthAlmPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhAlmsynthAlmPortIndex_Type.__name__ = "Integer32"
_Pm10010ulhAlmsynthAlmPortIndex_Object = MibTableColumn
pm10010ulhAlmsynthAlmPortIndex = _Pm10010ulhAlmsynthAlmPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 3, 8, 1, 1),
    _Pm10010ulhAlmsynthAlmPortIndex_Type()
)
pm10010ulhAlmsynthAlmPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmsynthAlmPortIndex.setStatus("current")
_Pm10010ulhAlmSfpAbsentPortn_Type = EkiOnOff
_Pm10010ulhAlmSfpAbsentPortn_Object = MibTableColumn
pm10010ulhAlmSfpAbsentPortn = _Pm10010ulhAlmSfpAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 3, 8, 1, 2),
    _Pm10010ulhAlmSfpAbsentPortn_Type()
)
pm10010ulhAlmSfpAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmSfpAbsentPortn.setStatus("current")
_Pm10010ulhAlmDdmAbsentPortn_Type = EkiOnOff
_Pm10010ulhAlmDdmAbsentPortn_Object = MibTableColumn
pm10010ulhAlmDdmAbsentPortn = _Pm10010ulhAlmDdmAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 3, 8, 1, 3),
    _Pm10010ulhAlmDdmAbsentPortn_Type()
)
pm10010ulhAlmDdmAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmDdmAbsentPortn.setStatus("current")
_Pm10010ulhAlmHwFailAccPortn_Type = EkiOnOff
_Pm10010ulhAlmHwFailAccPortn_Object = MibTableColumn
pm10010ulhAlmHwFailAccPortn = _Pm10010ulhAlmHwFailAccPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 3, 8, 1, 5),
    _Pm10010ulhAlmHwFailAccPortn_Type()
)
pm10010ulhAlmHwFailAccPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmHwFailAccPortn.setStatus("current")
_Pm10010ulhAlmDwLsdPortn_Type = EkiOnOff
_Pm10010ulhAlmDwLsdPortn_Object = MibTableColumn
pm10010ulhAlmDwLsdPortn = _Pm10010ulhAlmDwLsdPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 3, 8, 1, 6),
    _Pm10010ulhAlmDwLsdPortn_Type()
)
pm10010ulhAlmDwLsdPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmDwLsdPortn.setStatus("current")
_Pm10010ulhAlmClientLocalOosPortn_Type = EkiOnOff
_Pm10010ulhAlmClientLocalOosPortn_Object = MibTableColumn
pm10010ulhAlmClientLocalOosPortn = _Pm10010ulhAlmClientLocalOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 3, 8, 1, 7),
    _Pm10010ulhAlmClientLocalOosPortn_Type()
)
pm10010ulhAlmClientLocalOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmClientLocalOosPortn.setStatus("current")
_Pm10010ulhAlmClientRemoteOosPortn_Type = EkiOnOff
_Pm10010ulhAlmClientRemoteOosPortn_Object = MibTableColumn
pm10010ulhAlmClientRemoteOosPortn = _Pm10010ulhAlmClientRemoteOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 3, 8, 1, 8),
    _Pm10010ulhAlmClientRemoteOosPortn_Type()
)
pm10010ulhAlmClientRemoteOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmClientRemoteOosPortn.setStatus("current")
_Pm10010ulhAlmDwCaisPortn_Type = EkiOnOff
_Pm10010ulhAlmDwCaisPortn_Object = MibTableColumn
pm10010ulhAlmDwCaisPortn = _Pm10010ulhAlmDwCaisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 3, 8, 1, 9),
    _Pm10010ulhAlmDwCaisPortn_Type()
)
pm10010ulhAlmDwCaisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmDwCaisPortn.setStatus("current")
_Pm10010ulhAlmSfpDdmWarningPortn_Type = EkiOnOff
_Pm10010ulhAlmSfpDdmWarningPortn_Object = MibTableColumn
pm10010ulhAlmSfpDdmWarningPortn = _Pm10010ulhAlmSfpDdmWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 3, 8, 1, 10),
    _Pm10010ulhAlmSfpDdmWarningPortn_Type()
)
pm10010ulhAlmSfpDdmWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmSfpDdmWarningPortn.setStatus("current")
_Pm10010ulhAlmSfpDdmAlmPortn_Type = EkiOnOff
_Pm10010ulhAlmSfpDdmAlmPortn_Object = MibTableColumn
pm10010ulhAlmSfpDdmAlmPortn = _Pm10010ulhAlmSfpDdmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 3, 8, 1, 11),
    _Pm10010ulhAlmSfpDdmAlmPortn_Type()
)
pm10010ulhAlmSfpDdmAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmSfpDdmAlmPortn.setStatus("current")
_Pm10010ulhAlmFailAccPortn_Type = EkiOnOff
_Pm10010ulhAlmFailAccPortn_Object = MibTableColumn
pm10010ulhAlmFailAccPortn = _Pm10010ulhAlmFailAccPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 3, 8, 1, 13),
    _Pm10010ulhAlmFailAccPortn_Type()
)
pm10010ulhAlmFailAccPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmFailAccPortn.setStatus("current")
_Pm10010ulhAlmUpCsfPortn_Type = EkiOnOff
_Pm10010ulhAlmUpCsfPortn_Object = MibTableColumn
pm10010ulhAlmUpCsfPortn = _Pm10010ulhAlmUpCsfPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 2, 3, 8, 1, 17),
    _Pm10010ulhAlmUpCsfPortn_Type()
)
pm10010ulhAlmUpCsfPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmUpCsfPortn.setStatus("current")
_Pm10010ulhAlmLine_ObjectIdentity = ObjectIdentity
pm10010ulhAlmLine = _Pm10010ulhAlmLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3)
)
_Pm10010ulhAlmLineNurg_ObjectIdentity = ObjectIdentity
pm10010ulhAlmLineNurg = _Pm10010ulhAlmLineNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 1)
)
_Pm10010ulhAlmlineNetworkLaneAlarmWarning1Table_Object = MibTable
pm10010ulhAlmlineNetworkLaneAlarmWarning1Table = _Pm10010ulhAlmlineNetworkLaneAlarmWarning1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 1, 184)
)
if mibBuilder.loadTexts:
    pm10010ulhAlmlineNetworkLaneAlarmWarning1Table.setStatus("current")
_Pm10010ulhAlmlineNetworkLaneAlarmWarning1Entry_Object = MibTableRow
pm10010ulhAlmlineNetworkLaneAlarmWarning1Entry = _Pm10010ulhAlmlineNetworkLaneAlarmWarning1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 1, 184, 1)
)
pm10010ulhAlmlineNetworkLaneAlarmWarning1Entry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhAlmlineNetworkLaneAlarmWarning1Index"),
)
if mibBuilder.loadTexts:
    pm10010ulhAlmlineNetworkLaneAlarmWarning1Entry.setStatus("current")


class _Pm10010ulhAlmlineNetworkLaneAlarmWarning1Index_Type(Integer32):
    """Custom type pm10010ulhAlmlineNetworkLaneAlarmWarning1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhAlmlineNetworkLaneAlarmWarning1Index_Type.__name__ = "Integer32"
_Pm10010ulhAlmlineNetworkLaneAlarmWarning1Index_Object = MibTableColumn
pm10010ulhAlmlineNetworkLaneAlarmWarning1Index = _Pm10010ulhAlmlineNetworkLaneAlarmWarning1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 1, 184, 1, 1),
    _Pm10010ulhAlmlineNetworkLaneAlarmWarning1Index_Type()
)
pm10010ulhAlmlineNetworkLaneAlarmWarning1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmlineNetworkLaneAlarmWarning1Index.setStatus("current")
_Pm10010ulhAlmLineRxPowerLowAlarmPortn_Type = EkiOnOff
_Pm10010ulhAlmLineRxPowerLowAlarmPortn_Object = MibTableColumn
pm10010ulhAlmLineRxPowerLowAlarmPortn = _Pm10010ulhAlmLineRxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 1, 184, 1, 2),
    _Pm10010ulhAlmLineRxPowerLowAlarmPortn_Type()
)
pm10010ulhAlmLineRxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmLineRxPowerLowAlarmPortn.setStatus("current")
_Pm10010ulhAlmLineRxPowerLowWarningPortn_Type = EkiOnOff
_Pm10010ulhAlmLineRxPowerLowWarningPortn_Object = MibTableColumn
pm10010ulhAlmLineRxPowerLowWarningPortn = _Pm10010ulhAlmLineRxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 1, 184, 1, 3),
    _Pm10010ulhAlmLineRxPowerLowWarningPortn_Type()
)
pm10010ulhAlmLineRxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmLineRxPowerLowWarningPortn.setStatus("current")
_Pm10010ulhAlmLineRxPowerHighWarningPortn_Type = EkiOnOff
_Pm10010ulhAlmLineRxPowerHighWarningPortn_Object = MibTableColumn
pm10010ulhAlmLineRxPowerHighWarningPortn = _Pm10010ulhAlmLineRxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 1, 184, 1, 4),
    _Pm10010ulhAlmLineRxPowerHighWarningPortn_Type()
)
pm10010ulhAlmLineRxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmLineRxPowerHighWarningPortn.setStatus("current")
_Pm10010ulhAlmLineRxPowerHighAlarmPortn_Type = EkiOnOff
_Pm10010ulhAlmLineRxPowerHighAlarmPortn_Object = MibTableColumn
pm10010ulhAlmLineRxPowerHighAlarmPortn = _Pm10010ulhAlmLineRxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 1, 184, 1, 5),
    _Pm10010ulhAlmLineRxPowerHighAlarmPortn_Type()
)
pm10010ulhAlmLineRxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmLineRxPowerHighAlarmPortn.setStatus("current")
_Pm10010ulhAlmLineLaserTempLowAlarmPortn_Type = EkiOnOff
_Pm10010ulhAlmLineLaserTempLowAlarmPortn_Object = MibTableColumn
pm10010ulhAlmLineLaserTempLowAlarmPortn = _Pm10010ulhAlmLineLaserTempLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 1, 184, 1, 6),
    _Pm10010ulhAlmLineLaserTempLowAlarmPortn_Type()
)
pm10010ulhAlmLineLaserTempLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmLineLaserTempLowAlarmPortn.setStatus("current")
_Pm10010ulhAlmLineLaserTempLowWarningPortn_Type = EkiOnOff
_Pm10010ulhAlmLineLaserTempLowWarningPortn_Object = MibTableColumn
pm10010ulhAlmLineLaserTempLowWarningPortn = _Pm10010ulhAlmLineLaserTempLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 1, 184, 1, 7),
    _Pm10010ulhAlmLineLaserTempLowWarningPortn_Type()
)
pm10010ulhAlmLineLaserTempLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmLineLaserTempLowWarningPortn.setStatus("current")
_Pm10010ulhAlmLineLaserTempHighWarningPortn_Type = EkiOnOff
_Pm10010ulhAlmLineLaserTempHighWarningPortn_Object = MibTableColumn
pm10010ulhAlmLineLaserTempHighWarningPortn = _Pm10010ulhAlmLineLaserTempHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 1, 184, 1, 8),
    _Pm10010ulhAlmLineLaserTempHighWarningPortn_Type()
)
pm10010ulhAlmLineLaserTempHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmLineLaserTempHighWarningPortn.setStatus("current")
_Pm10010ulhAlmLineLaserTempHighAlarmPortn_Type = EkiOnOff
_Pm10010ulhAlmLineLaserTempHighAlarmPortn_Object = MibTableColumn
pm10010ulhAlmLineLaserTempHighAlarmPortn = _Pm10010ulhAlmLineLaserTempHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 1, 184, 1, 9),
    _Pm10010ulhAlmLineLaserTempHighAlarmPortn_Type()
)
pm10010ulhAlmLineLaserTempHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmLineLaserTempHighAlarmPortn.setStatus("current")
_Pm10010ulhAlmLineTxPowerLowAlarmPortn_Type = EkiOnOff
_Pm10010ulhAlmLineTxPowerLowAlarmPortn_Object = MibTableColumn
pm10010ulhAlmLineTxPowerLowAlarmPortn = _Pm10010ulhAlmLineTxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 1, 184, 1, 10),
    _Pm10010ulhAlmLineTxPowerLowAlarmPortn_Type()
)
pm10010ulhAlmLineTxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmLineTxPowerLowAlarmPortn.setStatus("current")
_Pm10010ulhAlmLineTxPowerLowWarningPortn_Type = EkiOnOff
_Pm10010ulhAlmLineTxPowerLowWarningPortn_Object = MibTableColumn
pm10010ulhAlmLineTxPowerLowWarningPortn = _Pm10010ulhAlmLineTxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 1, 184, 1, 11),
    _Pm10010ulhAlmLineTxPowerLowWarningPortn_Type()
)
pm10010ulhAlmLineTxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmLineTxPowerLowWarningPortn.setStatus("current")
_Pm10010ulhAlmLineTxPowerHighWarningPortn_Type = EkiOnOff
_Pm10010ulhAlmLineTxPowerHighWarningPortn_Object = MibTableColumn
pm10010ulhAlmLineTxPowerHighWarningPortn = _Pm10010ulhAlmLineTxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 1, 184, 1, 12),
    _Pm10010ulhAlmLineTxPowerHighWarningPortn_Type()
)
pm10010ulhAlmLineTxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmLineTxPowerHighWarningPortn.setStatus("current")
_Pm10010ulhAlmLineTxPowerHighAlarmPortn_Type = EkiOnOff
_Pm10010ulhAlmLineTxPowerHighAlarmPortn_Object = MibTableColumn
pm10010ulhAlmLineTxPowerHighAlarmPortn = _Pm10010ulhAlmLineTxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 1, 184, 1, 13),
    _Pm10010ulhAlmLineTxPowerHighAlarmPortn_Type()
)
pm10010ulhAlmLineTxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmLineTxPowerHighAlarmPortn.setStatus("current")
_Pm10010ulhAlmLineBiasLowAlarmPortn_Type = EkiOnOff
_Pm10010ulhAlmLineBiasLowAlarmPortn_Object = MibTableColumn
pm10010ulhAlmLineBiasLowAlarmPortn = _Pm10010ulhAlmLineBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 1, 184, 1, 14),
    _Pm10010ulhAlmLineBiasLowAlarmPortn_Type()
)
pm10010ulhAlmLineBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmLineBiasLowAlarmPortn.setStatus("current")
_Pm10010ulhAlmLineBiasLowWarningPortn_Type = EkiOnOff
_Pm10010ulhAlmLineBiasLowWarningPortn_Object = MibTableColumn
pm10010ulhAlmLineBiasLowWarningPortn = _Pm10010ulhAlmLineBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 1, 184, 1, 15),
    _Pm10010ulhAlmLineBiasLowWarningPortn_Type()
)
pm10010ulhAlmLineBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmLineBiasLowWarningPortn.setStatus("current")
_Pm10010ulhAlmLineBiasHighWarningPortn_Type = EkiOnOff
_Pm10010ulhAlmLineBiasHighWarningPortn_Object = MibTableColumn
pm10010ulhAlmLineBiasHighWarningPortn = _Pm10010ulhAlmLineBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 1, 184, 1, 16),
    _Pm10010ulhAlmLineBiasHighWarningPortn_Type()
)
pm10010ulhAlmLineBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmLineBiasHighWarningPortn.setStatus("current")
_Pm10010ulhAlmLineBiasHighAlarmPortn_Type = EkiOnOff
_Pm10010ulhAlmLineBiasHighAlarmPortn_Object = MibTableColumn
pm10010ulhAlmLineBiasHighAlarmPortn = _Pm10010ulhAlmLineBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 1, 184, 1, 17),
    _Pm10010ulhAlmLineBiasHighAlarmPortn_Type()
)
pm10010ulhAlmLineBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmLineBiasHighAlarmPortn.setStatus("current")
_Pm10010ulhAlmlineNetworkLaneAlarmWarning2Table_Object = MibTable
pm10010ulhAlmlineNetworkLaneAlarmWarning2Table = _Pm10010ulhAlmlineNetworkLaneAlarmWarning2Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 1, 188)
)
if mibBuilder.loadTexts:
    pm10010ulhAlmlineNetworkLaneAlarmWarning2Table.setStatus("current")
_Pm10010ulhAlmlineNetworkLaneAlarmWarning2Entry_Object = MibTableRow
pm10010ulhAlmlineNetworkLaneAlarmWarning2Entry = _Pm10010ulhAlmlineNetworkLaneAlarmWarning2Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 1, 188, 1)
)
pm10010ulhAlmlineNetworkLaneAlarmWarning2Entry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhAlmlineNetworkLaneAlarmWarning2Index"),
)
if mibBuilder.loadTexts:
    pm10010ulhAlmlineNetworkLaneAlarmWarning2Entry.setStatus("current")


class _Pm10010ulhAlmlineNetworkLaneAlarmWarning2Index_Type(Integer32):
    """Custom type pm10010ulhAlmlineNetworkLaneAlarmWarning2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhAlmlineNetworkLaneAlarmWarning2Index_Type.__name__ = "Integer32"
_Pm10010ulhAlmlineNetworkLaneAlarmWarning2Index_Object = MibTableColumn
pm10010ulhAlmlineNetworkLaneAlarmWarning2Index = _Pm10010ulhAlmlineNetworkLaneAlarmWarning2Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 1, 188, 1, 1),
    _Pm10010ulhAlmlineNetworkLaneAlarmWarning2Index_Type()
)
pm10010ulhAlmlineNetworkLaneAlarmWarning2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmlineNetworkLaneAlarmWarning2Index.setStatus("current")
_Pm10010ulhAlmTxModulatorBiasLowAlarmPortn_Type = EkiOnOff
_Pm10010ulhAlmTxModulatorBiasLowAlarmPortn_Object = MibTableColumn
pm10010ulhAlmTxModulatorBiasLowAlarmPortn = _Pm10010ulhAlmTxModulatorBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 1, 188, 1, 2),
    _Pm10010ulhAlmTxModulatorBiasLowAlarmPortn_Type()
)
pm10010ulhAlmTxModulatorBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmTxModulatorBiasLowAlarmPortn.setStatus("current")
_Pm10010ulhAlmTxModulatorBiasLowWarningPortn_Type = EkiOnOff
_Pm10010ulhAlmTxModulatorBiasLowWarningPortn_Object = MibTableColumn
pm10010ulhAlmTxModulatorBiasLowWarningPortn = _Pm10010ulhAlmTxModulatorBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 1, 188, 1, 3),
    _Pm10010ulhAlmTxModulatorBiasLowWarningPortn_Type()
)
pm10010ulhAlmTxModulatorBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmTxModulatorBiasLowWarningPortn.setStatus("current")
_Pm10010ulhAlmTxModulatorBiasHighWarningPortn_Type = EkiOnOff
_Pm10010ulhAlmTxModulatorBiasHighWarningPortn_Object = MibTableColumn
pm10010ulhAlmTxModulatorBiasHighWarningPortn = _Pm10010ulhAlmTxModulatorBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 1, 188, 1, 4),
    _Pm10010ulhAlmTxModulatorBiasHighWarningPortn_Type()
)
pm10010ulhAlmTxModulatorBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmTxModulatorBiasHighWarningPortn.setStatus("current")
_Pm10010ulhAlmTxModulatorBiasHighAlarmPortn_Type = EkiOnOff
_Pm10010ulhAlmTxModulatorBiasHighAlarmPortn_Object = MibTableColumn
pm10010ulhAlmTxModulatorBiasHighAlarmPortn = _Pm10010ulhAlmTxModulatorBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 1, 188, 1, 5),
    _Pm10010ulhAlmTxModulatorBiasHighAlarmPortn_Type()
)
pm10010ulhAlmTxModulatorBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmTxModulatorBiasHighAlarmPortn.setStatus("current")
_Pm10010ulhAlmRxLaserTempLowAlarmPortn_Type = EkiOnOff
_Pm10010ulhAlmRxLaserTempLowAlarmPortn_Object = MibTableColumn
pm10010ulhAlmRxLaserTempLowAlarmPortn = _Pm10010ulhAlmRxLaserTempLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 1, 188, 1, 6),
    _Pm10010ulhAlmRxLaserTempLowAlarmPortn_Type()
)
pm10010ulhAlmRxLaserTempLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmRxLaserTempLowAlarmPortn.setStatus("current")
_Pm10010ulhAlmRxLaserTempLowWarningPortn_Type = EkiOnOff
_Pm10010ulhAlmRxLaserTempLowWarningPortn_Object = MibTableColumn
pm10010ulhAlmRxLaserTempLowWarningPortn = _Pm10010ulhAlmRxLaserTempLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 1, 188, 1, 7),
    _Pm10010ulhAlmRxLaserTempLowWarningPortn_Type()
)
pm10010ulhAlmRxLaserTempLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmRxLaserTempLowWarningPortn.setStatus("current")
_Pm10010ulhAlmRxLaserTempHighWarningPortn_Type = EkiOnOff
_Pm10010ulhAlmRxLaserTempHighWarningPortn_Object = MibTableColumn
pm10010ulhAlmRxLaserTempHighWarningPortn = _Pm10010ulhAlmRxLaserTempHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 1, 188, 1, 8),
    _Pm10010ulhAlmRxLaserTempHighWarningPortn_Type()
)
pm10010ulhAlmRxLaserTempHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmRxLaserTempHighWarningPortn.setStatus("current")
_Pm10010ulhAlmRxLaserTempHighAlarmPortn_Type = EkiOnOff
_Pm10010ulhAlmRxLaserTempHighAlarmPortn_Object = MibTableColumn
pm10010ulhAlmRxLaserTempHighAlarmPortn = _Pm10010ulhAlmRxLaserTempHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 1, 188, 1, 9),
    _Pm10010ulhAlmRxLaserTempHighAlarmPortn_Type()
)
pm10010ulhAlmRxLaserTempHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmRxLaserTempHighAlarmPortn.setStatus("current")
_Pm10010ulhAlmRxLaserOutputLowAlarmPortn_Type = EkiOnOff
_Pm10010ulhAlmRxLaserOutputLowAlarmPortn_Object = MibTableColumn
pm10010ulhAlmRxLaserOutputLowAlarmPortn = _Pm10010ulhAlmRxLaserOutputLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 1, 188, 1, 10),
    _Pm10010ulhAlmRxLaserOutputLowAlarmPortn_Type()
)
pm10010ulhAlmRxLaserOutputLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmRxLaserOutputLowAlarmPortn.setStatus("current")
_Pm10010ulhAlmRxLaserOutputLowWarningPortn_Type = EkiOnOff
_Pm10010ulhAlmRxLaserOutputLowWarningPortn_Object = MibTableColumn
pm10010ulhAlmRxLaserOutputLowWarningPortn = _Pm10010ulhAlmRxLaserOutputLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 1, 188, 1, 11),
    _Pm10010ulhAlmRxLaserOutputLowWarningPortn_Type()
)
pm10010ulhAlmRxLaserOutputLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmRxLaserOutputLowWarningPortn.setStatus("current")
_Pm10010ulhAlmRxLaserOutputHighWarningPortn_Type = EkiOnOff
_Pm10010ulhAlmRxLaserOutputHighWarningPortn_Object = MibTableColumn
pm10010ulhAlmRxLaserOutputHighWarningPortn = _Pm10010ulhAlmRxLaserOutputHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 1, 188, 1, 12),
    _Pm10010ulhAlmRxLaserOutputHighWarningPortn_Type()
)
pm10010ulhAlmRxLaserOutputHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmRxLaserOutputHighWarningPortn.setStatus("current")
_Pm10010ulhAlmRxLaserOutputHighAlarmPortn_Type = EkiOnOff
_Pm10010ulhAlmRxLaserOutputHighAlarmPortn_Object = MibTableColumn
pm10010ulhAlmRxLaserOutputHighAlarmPortn = _Pm10010ulhAlmRxLaserOutputHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 1, 188, 1, 13),
    _Pm10010ulhAlmRxLaserOutputHighAlarmPortn_Type()
)
pm10010ulhAlmRxLaserOutputHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmRxLaserOutputHighAlarmPortn.setStatus("current")
_Pm10010ulhAlmRxLaserBiasLowAlarmPortn_Type = EkiOnOff
_Pm10010ulhAlmRxLaserBiasLowAlarmPortn_Object = MibTableColumn
pm10010ulhAlmRxLaserBiasLowAlarmPortn = _Pm10010ulhAlmRxLaserBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 1, 188, 1, 14),
    _Pm10010ulhAlmRxLaserBiasLowAlarmPortn_Type()
)
pm10010ulhAlmRxLaserBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmRxLaserBiasLowAlarmPortn.setStatus("current")
_Pm10010ulhAlmRxLaserBiasLowWarningPortn_Type = EkiOnOff
_Pm10010ulhAlmRxLaserBiasLowWarningPortn_Object = MibTableColumn
pm10010ulhAlmRxLaserBiasLowWarningPortn = _Pm10010ulhAlmRxLaserBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 1, 188, 1, 15),
    _Pm10010ulhAlmRxLaserBiasLowWarningPortn_Type()
)
pm10010ulhAlmRxLaserBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmRxLaserBiasLowWarningPortn.setStatus("current")
_Pm10010ulhAlmRxLaserBiasHighWarningPortn_Type = EkiOnOff
_Pm10010ulhAlmRxLaserBiasHighWarningPortn_Object = MibTableColumn
pm10010ulhAlmRxLaserBiasHighWarningPortn = _Pm10010ulhAlmRxLaserBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 1, 188, 1, 16),
    _Pm10010ulhAlmRxLaserBiasHighWarningPortn_Type()
)
pm10010ulhAlmRxLaserBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmRxLaserBiasHighWarningPortn.setStatus("current")
_Pm10010ulhAlmRxLaserBiasHighAlarmPortn_Type = EkiOnOff
_Pm10010ulhAlmRxLaserBiasHighAlarmPortn_Object = MibTableColumn
pm10010ulhAlmRxLaserBiasHighAlarmPortn = _Pm10010ulhAlmRxLaserBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 1, 188, 1, 17),
    _Pm10010ulhAlmRxLaserBiasHighAlarmPortn_Type()
)
pm10010ulhAlmRxLaserBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmRxLaserBiasHighAlarmPortn.setStatus("current")
_Pm10010ulhAlmLineUrg_ObjectIdentity = ObjectIdentity
pm10010ulhAlmLineUrg = _Pm10010ulhAlmLineUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 2)
)
_Pm10010ulhAlmlineNetworkLaneFaultTable_Object = MibTable
pm10010ulhAlmlineNetworkLaneFaultTable = _Pm10010ulhAlmlineNetworkLaneFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 2, 192)
)
if mibBuilder.loadTexts:
    pm10010ulhAlmlineNetworkLaneFaultTable.setStatus("current")
_Pm10010ulhAlmlineNetworkLaneFaultEntry_Object = MibTableRow
pm10010ulhAlmlineNetworkLaneFaultEntry = _Pm10010ulhAlmlineNetworkLaneFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 2, 192, 1)
)
pm10010ulhAlmlineNetworkLaneFaultEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhAlmlineNetworkLaneFaultIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhAlmlineNetworkLaneFaultEntry.setStatus("current")


class _Pm10010ulhAlmlineNetworkLaneFaultIndex_Type(Integer32):
    """Custom type pm10010ulhAlmlineNetworkLaneFaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhAlmlineNetworkLaneFaultIndex_Type.__name__ = "Integer32"
_Pm10010ulhAlmlineNetworkLaneFaultIndex_Object = MibTableColumn
pm10010ulhAlmlineNetworkLaneFaultIndex = _Pm10010ulhAlmlineNetworkLaneFaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 2, 192, 1, 1),
    _Pm10010ulhAlmlineNetworkLaneFaultIndex_Type()
)
pm10010ulhAlmlineNetworkLaneFaultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmlineNetworkLaneFaultIndex.setStatus("current")
_Pm10010ulhAlmLineLaneRxTecFaultPortn_Type = EkiOnOff
_Pm10010ulhAlmLineLaneRxTecFaultPortn_Object = MibTableColumn
pm10010ulhAlmLineLaneRxTecFaultPortn = _Pm10010ulhAlmLineLaneRxTecFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 2, 192, 1, 3),
    _Pm10010ulhAlmLineLaneRxTecFaultPortn_Type()
)
pm10010ulhAlmLineLaneRxTecFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmLineLaneRxTecFaultPortn.setStatus("current")
_Pm10010ulhAlmLineLaneRxFifoErrorPortn_Type = EkiOnOff
_Pm10010ulhAlmLineLaneRxFifoErrorPortn_Object = MibTableColumn
pm10010ulhAlmLineLaneRxFifoErrorPortn = _Pm10010ulhAlmLineLaneRxFifoErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 2, 192, 1, 4),
    _Pm10010ulhAlmLineLaneRxFifoErrorPortn_Type()
)
pm10010ulhAlmLineLaneRxFifoErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmLineLaneRxFifoErrorPortn.setStatus("current")
_Pm10010ulhAlmLineLaneRxLolPortn_Type = EkiOnOff
_Pm10010ulhAlmLineLaneRxLolPortn_Object = MibTableColumn
pm10010ulhAlmLineLaneRxLolPortn = _Pm10010ulhAlmLineLaneRxLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 2, 192, 1, 5),
    _Pm10010ulhAlmLineLaneRxLolPortn_Type()
)
pm10010ulhAlmLineLaneRxLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmLineLaneRxLolPortn.setStatus("current")
_Pm10010ulhAlmLineLaneRxLosPortn_Type = EkiOnOff
_Pm10010ulhAlmLineLaneRxLosPortn_Object = MibTableColumn
pm10010ulhAlmLineLaneRxLosPortn = _Pm10010ulhAlmLineLaneRxLosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 2, 192, 1, 6),
    _Pm10010ulhAlmLineLaneRxLosPortn_Type()
)
pm10010ulhAlmLineLaneRxLosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmLineLaneRxLosPortn.setStatus("current")
_Pm10010ulhAlmLineLaneTxLolPortn_Type = EkiOnOff
_Pm10010ulhAlmLineLaneTxLolPortn_Object = MibTableColumn
pm10010ulhAlmLineLaneTxLolPortn = _Pm10010ulhAlmLineLaneTxLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 2, 192, 1, 8),
    _Pm10010ulhAlmLineLaneTxLolPortn_Type()
)
pm10010ulhAlmLineLaneTxLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmLineLaneTxLolPortn.setStatus("current")
_Pm10010ulhAlmLineLaneTxLosfPortn_Type = EkiOnOff
_Pm10010ulhAlmLineLaneTxLosfPortn_Object = MibTableColumn
pm10010ulhAlmLineLaneTxLosfPortn = _Pm10010ulhAlmLineLaneTxLosfPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 2, 192, 1, 9),
    _Pm10010ulhAlmLineLaneTxLosfPortn_Type()
)
pm10010ulhAlmLineLaneTxLosfPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmLineLaneTxLosfPortn.setStatus("current")
_Pm10010ulhAlmLineLaneApdPowerSupplyPortn_Type = EkiOnOff
_Pm10010ulhAlmLineLaneApdPowerSupplyPortn_Object = MibTableColumn
pm10010ulhAlmLineLaneApdPowerSupplyPortn = _Pm10010ulhAlmLineLaneApdPowerSupplyPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 2, 192, 1, 15),
    _Pm10010ulhAlmLineLaneApdPowerSupplyPortn_Type()
)
pm10010ulhAlmLineLaneApdPowerSupplyPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmLineLaneApdPowerSupplyPortn.setStatus("current")
_Pm10010ulhAlmLineLaneWavelengthUnlockedPortn_Type = EkiOnOff
_Pm10010ulhAlmLineLaneWavelengthUnlockedPortn_Object = MibTableColumn
pm10010ulhAlmLineLaneWavelengthUnlockedPortn = _Pm10010ulhAlmLineLaneWavelengthUnlockedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 2, 192, 1, 16),
    _Pm10010ulhAlmLineLaneWavelengthUnlockedPortn_Type()
)
pm10010ulhAlmLineLaneWavelengthUnlockedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmLineLaneWavelengthUnlockedPortn.setStatus("current")
_Pm10010ulhAlmLineLaneTecFaultPortn_Type = EkiOnOff
_Pm10010ulhAlmLineLaneTecFaultPortn_Object = MibTableColumn
pm10010ulhAlmLineLaneTecFaultPortn = _Pm10010ulhAlmLineLaneTecFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 2, 192, 1, 17),
    _Pm10010ulhAlmLineLaneTecFaultPortn_Type()
)
pm10010ulhAlmLineLaneTecFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmLineLaneTecFaultPortn.setStatus("current")
_Pm10010ulhAlmlineHostLaneFaultTable_Object = MibTable
pm10010ulhAlmlineHostLaneFaultTable = _Pm10010ulhAlmlineHostLaneFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 2, 196)
)
if mibBuilder.loadTexts:
    pm10010ulhAlmlineHostLaneFaultTable.setStatus("current")
_Pm10010ulhAlmlineHostLaneFaultEntry_Object = MibTableRow
pm10010ulhAlmlineHostLaneFaultEntry = _Pm10010ulhAlmlineHostLaneFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 2, 196, 1)
)
pm10010ulhAlmlineHostLaneFaultEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhAlmlineHostLaneFaultIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhAlmlineHostLaneFaultEntry.setStatus("current")


class _Pm10010ulhAlmlineHostLaneFaultIndex_Type(Integer32):
    """Custom type pm10010ulhAlmlineHostLaneFaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhAlmlineHostLaneFaultIndex_Type.__name__ = "Integer32"
_Pm10010ulhAlmlineHostLaneFaultIndex_Object = MibTableColumn
pm10010ulhAlmlineHostLaneFaultIndex = _Pm10010ulhAlmlineHostLaneFaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 2, 196, 1, 1),
    _Pm10010ulhAlmlineHostLaneFaultIndex_Type()
)
pm10010ulhAlmlineHostLaneFaultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmlineHostLaneFaultIndex.setStatus("current")
_Pm10010ulhAlmLineInputLossOfSignalPortn_Type = EkiOnOff
_Pm10010ulhAlmLineInputLossOfSignalPortn_Object = MibTableColumn
pm10010ulhAlmLineInputLossOfSignalPortn = _Pm10010ulhAlmLineInputLossOfSignalPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 2, 196, 1, 2),
    _Pm10010ulhAlmLineInputLossOfSignalPortn_Type()
)
pm10010ulhAlmLineInputLossOfSignalPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmLineInputLossOfSignalPortn.setStatus("current")
_Pm10010ulhAlmLineLossOfFramePortn_Type = EkiOnOff
_Pm10010ulhAlmLineLossOfFramePortn_Object = MibTableColumn
pm10010ulhAlmLineLossOfFramePortn = _Pm10010ulhAlmLineLossOfFramePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 2, 196, 1, 3),
    _Pm10010ulhAlmLineLossOfFramePortn_Type()
)
pm10010ulhAlmLineLossOfFramePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmLineLossOfFramePortn.setStatus("current")
_Pm10010ulhAlmLineSmBdiInsertedPortn_Type = EkiOnOff
_Pm10010ulhAlmLineSmBdiInsertedPortn_Object = MibTableColumn
pm10010ulhAlmLineSmBdiInsertedPortn = _Pm10010ulhAlmLineSmBdiInsertedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 2, 196, 1, 4),
    _Pm10010ulhAlmLineSmBdiInsertedPortn_Type()
)
pm10010ulhAlmLineSmBdiInsertedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmLineSmBdiInsertedPortn.setStatus("current")
_Pm10010ulhAlmLineSmBdiDetectedPortn_Type = EkiOnOff
_Pm10010ulhAlmLineSmBdiDetectedPortn_Object = MibTableColumn
pm10010ulhAlmLineSmBdiDetectedPortn = _Pm10010ulhAlmLineSmBdiDetectedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 2, 196, 1, 5),
    _Pm10010ulhAlmLineSmBdiDetectedPortn_Type()
)
pm10010ulhAlmLineSmBdiDetectedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmLineSmBdiDetectedPortn.setStatus("current")
_Pm10010ulhAlmLineSmIaeInsertedPortn_Type = EkiOnOff
_Pm10010ulhAlmLineSmIaeInsertedPortn_Object = MibTableColumn
pm10010ulhAlmLineSmIaeInsertedPortn = _Pm10010ulhAlmLineSmIaeInsertedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 2, 196, 1, 6),
    _Pm10010ulhAlmLineSmIaeInsertedPortn_Type()
)
pm10010ulhAlmLineSmIaeInsertedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmLineSmIaeInsertedPortn.setStatus("current")
_Pm10010ulhAlmLineSmIaeDetectedPortn_Type = EkiOnOff
_Pm10010ulhAlmLineSmIaeDetectedPortn_Object = MibTableColumn
pm10010ulhAlmLineSmIaeDetectedPortn = _Pm10010ulhAlmLineSmIaeDetectedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 2, 196, 1, 7),
    _Pm10010ulhAlmLineSmIaeDetectedPortn_Type()
)
pm10010ulhAlmLineSmIaeDetectedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmLineSmIaeDetectedPortn.setStatus("current")
_Pm10010ulhAlmLineTxHostLolPortn_Type = EkiOnOff
_Pm10010ulhAlmLineTxHostLolPortn_Object = MibTableColumn
pm10010ulhAlmLineTxHostLolPortn = _Pm10010ulhAlmLineTxHostLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 2, 196, 1, 10),
    _Pm10010ulhAlmLineTxHostLolPortn_Type()
)
pm10010ulhAlmLineTxHostLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmLineTxHostLolPortn.setStatus("current")
_Pm10010ulhAlmLineLaneTxFifoErrorPortn_Type = EkiOnOff
_Pm10010ulhAlmLineLaneTxFifoErrorPortn_Object = MibTableColumn
pm10010ulhAlmLineLaneTxFifoErrorPortn = _Pm10010ulhAlmLineLaneTxFifoErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 2, 196, 1, 11),
    _Pm10010ulhAlmLineLaneTxFifoErrorPortn_Type()
)
pm10010ulhAlmLineLaneTxFifoErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmLineLaneTxFifoErrorPortn.setStatus("current")
_Pm10010ulhAlmlineNetworkLaneRxOtnTable_Object = MibTable
pm10010ulhAlmlineNetworkLaneRxOtnTable = _Pm10010ulhAlmlineNetworkLaneRxOtnTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 2, 200)
)
if mibBuilder.loadTexts:
    pm10010ulhAlmlineNetworkLaneRxOtnTable.setStatus("current")
_Pm10010ulhAlmlineNetworkLaneRxOtnEntry_Object = MibTableRow
pm10010ulhAlmlineNetworkLaneRxOtnEntry = _Pm10010ulhAlmlineNetworkLaneRxOtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 2, 200, 1)
)
pm10010ulhAlmlineNetworkLaneRxOtnEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhAlmlineNetworkLaneRxOtnIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhAlmlineNetworkLaneRxOtnEntry.setStatus("current")


class _Pm10010ulhAlmlineNetworkLaneRxOtnIndex_Type(Integer32):
    """Custom type pm10010ulhAlmlineNetworkLaneRxOtnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhAlmlineNetworkLaneRxOtnIndex_Type.__name__ = "Integer32"
_Pm10010ulhAlmlineNetworkLaneRxOtnIndex_Object = MibTableColumn
pm10010ulhAlmlineNetworkLaneRxOtnIndex = _Pm10010ulhAlmlineNetworkLaneRxOtnIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 2, 200, 1, 1),
    _Pm10010ulhAlmlineNetworkLaneRxOtnIndex_Type()
)
pm10010ulhAlmlineNetworkLaneRxOtnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmlineNetworkLaneRxOtnIndex.setStatus("current")
_Pm10010ulhAlmLineRxOtnOduAisPortn_Type = EkiOnOff
_Pm10010ulhAlmLineRxOtnOduAisPortn_Object = MibTableColumn
pm10010ulhAlmLineRxOtnOduAisPortn = _Pm10010ulhAlmLineRxOtnOduAisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 2, 200, 1, 10),
    _Pm10010ulhAlmLineRxOtnOduAisPortn_Type()
)
pm10010ulhAlmLineRxOtnOduAisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmLineRxOtnOduAisPortn.setStatus("current")
_Pm10010ulhAlmLineRxOtnOtuAisPortn_Type = EkiOnOff
_Pm10010ulhAlmLineRxOtnOtuAisPortn_Object = MibTableColumn
pm10010ulhAlmLineRxOtnOtuAisPortn = _Pm10010ulhAlmLineRxOtnOtuAisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 2, 200, 1, 11),
    _Pm10010ulhAlmLineRxOtnOtuAisPortn_Type()
)
pm10010ulhAlmLineRxOtnOtuAisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmLineRxOtnOtuAisPortn.setStatus("current")
_Pm10010ulhAlmLineRxSmBdiPortn_Type = EkiOnOff
_Pm10010ulhAlmLineRxSmBdiPortn_Object = MibTableColumn
pm10010ulhAlmLineRxSmBdiPortn = _Pm10010ulhAlmLineRxSmBdiPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 2, 200, 1, 12),
    _Pm10010ulhAlmLineRxSmBdiPortn_Type()
)
pm10010ulhAlmLineRxSmBdiPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmLineRxSmBdiPortn.setStatus("current")
_Pm10010ulhAlmLineRxOtnIaePortn_Type = EkiOnOff
_Pm10010ulhAlmLineRxOtnIaePortn_Object = MibTableColumn
pm10010ulhAlmLineRxOtnIaePortn = _Pm10010ulhAlmLineRxOtnIaePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 2, 200, 1, 13),
    _Pm10010ulhAlmLineRxOtnIaePortn_Type()
)
pm10010ulhAlmLineRxOtnIaePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmLineRxOtnIaePortn.setStatus("current")
_Pm10010ulhAlmLineRxOtnOomPortn_Type = EkiOnOff
_Pm10010ulhAlmLineRxOtnOomPortn_Object = MibTableColumn
pm10010ulhAlmLineRxOtnOomPortn = _Pm10010ulhAlmLineRxOtnOomPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 2, 200, 1, 14),
    _Pm10010ulhAlmLineRxOtnOomPortn_Type()
)
pm10010ulhAlmLineRxOtnOomPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmLineRxOtnOomPortn.setStatus("current")
_Pm10010ulhAlmLineRxOtnLomPortn_Type = EkiOnOff
_Pm10010ulhAlmLineRxOtnLomPortn_Object = MibTableColumn
pm10010ulhAlmLineRxOtnLomPortn = _Pm10010ulhAlmLineRxOtnLomPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 2, 200, 1, 15),
    _Pm10010ulhAlmLineRxOtnLomPortn_Type()
)
pm10010ulhAlmLineRxOtnLomPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmLineRxOtnLomPortn.setStatus("current")
_Pm10010ulhAlmLineRxOtnOofPortn_Type = EkiOnOff
_Pm10010ulhAlmLineRxOtnOofPortn_Object = MibTableColumn
pm10010ulhAlmLineRxOtnOofPortn = _Pm10010ulhAlmLineRxOtnOofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 2, 200, 1, 16),
    _Pm10010ulhAlmLineRxOtnOofPortn_Type()
)
pm10010ulhAlmLineRxOtnOofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmLineRxOtnOofPortn.setStatus("current")
_Pm10010ulhAlmLineRxOtnLofPortn_Type = EkiOnOff
_Pm10010ulhAlmLineRxOtnLofPortn_Object = MibTableColumn
pm10010ulhAlmLineRxOtnLofPortn = _Pm10010ulhAlmLineRxOtnLofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 2, 200, 1, 17),
    _Pm10010ulhAlmLineRxOtnLofPortn_Type()
)
pm10010ulhAlmLineRxOtnLofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmLineRxOtnLofPortn.setStatus("current")
_Pm10010ulhAlmlineHostLaneTxOtnTable_Object = MibTable
pm10010ulhAlmlineHostLaneTxOtnTable = _Pm10010ulhAlmlineHostLaneTxOtnTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 2, 204)
)
if mibBuilder.loadTexts:
    pm10010ulhAlmlineHostLaneTxOtnTable.setStatus("current")
_Pm10010ulhAlmlineHostLaneTxOtnEntry_Object = MibTableRow
pm10010ulhAlmlineHostLaneTxOtnEntry = _Pm10010ulhAlmlineHostLaneTxOtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 2, 204, 1)
)
pm10010ulhAlmlineHostLaneTxOtnEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhAlmlineHostLaneTxOtnIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhAlmlineHostLaneTxOtnEntry.setStatus("current")


class _Pm10010ulhAlmlineHostLaneTxOtnIndex_Type(Integer32):
    """Custom type pm10010ulhAlmlineHostLaneTxOtnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhAlmlineHostLaneTxOtnIndex_Type.__name__ = "Integer32"
_Pm10010ulhAlmlineHostLaneTxOtnIndex_Object = MibTableColumn
pm10010ulhAlmlineHostLaneTxOtnIndex = _Pm10010ulhAlmlineHostLaneTxOtnIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 2, 204, 1, 1),
    _Pm10010ulhAlmlineHostLaneTxOtnIndex_Type()
)
pm10010ulhAlmlineHostLaneTxOtnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmlineHostLaneTxOtnIndex.setStatus("current")
_Pm10010ulhAlmLineTxOtnOduAisPortn_Type = EkiOnOff
_Pm10010ulhAlmLineTxOtnOduAisPortn_Object = MibTableColumn
pm10010ulhAlmLineTxOtnOduAisPortn = _Pm10010ulhAlmLineTxOtnOduAisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 2, 204, 1, 10),
    _Pm10010ulhAlmLineTxOtnOduAisPortn_Type()
)
pm10010ulhAlmLineTxOtnOduAisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmLineTxOtnOduAisPortn.setStatus("current")
_Pm10010ulhAlmLineTxOtnOtuAisPortn_Type = EkiOnOff
_Pm10010ulhAlmLineTxOtnOtuAisPortn_Object = MibTableColumn
pm10010ulhAlmLineTxOtnOtuAisPortn = _Pm10010ulhAlmLineTxOtnOtuAisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 2, 204, 1, 11),
    _Pm10010ulhAlmLineTxOtnOtuAisPortn_Type()
)
pm10010ulhAlmLineTxOtnOtuAisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmLineTxOtnOtuAisPortn.setStatus("current")
_Pm10010ulhAlmLineTxSmBdiPortn_Type = EkiOnOff
_Pm10010ulhAlmLineTxSmBdiPortn_Object = MibTableColumn
pm10010ulhAlmLineTxSmBdiPortn = _Pm10010ulhAlmLineTxSmBdiPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 2, 204, 1, 12),
    _Pm10010ulhAlmLineTxSmBdiPortn_Type()
)
pm10010ulhAlmLineTxSmBdiPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmLineTxSmBdiPortn.setStatus("current")
_Pm10010ulhAlmLineTxOtnIaePortn_Type = EkiOnOff
_Pm10010ulhAlmLineTxOtnIaePortn_Object = MibTableColumn
pm10010ulhAlmLineTxOtnIaePortn = _Pm10010ulhAlmLineTxOtnIaePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 2, 204, 1, 13),
    _Pm10010ulhAlmLineTxOtnIaePortn_Type()
)
pm10010ulhAlmLineTxOtnIaePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmLineTxOtnIaePortn.setStatus("current")
_Pm10010ulhAlmLineTxOtnOomPortn_Type = EkiOnOff
_Pm10010ulhAlmLineTxOtnOomPortn_Object = MibTableColumn
pm10010ulhAlmLineTxOtnOomPortn = _Pm10010ulhAlmLineTxOtnOomPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 2, 204, 1, 14),
    _Pm10010ulhAlmLineTxOtnOomPortn_Type()
)
pm10010ulhAlmLineTxOtnOomPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmLineTxOtnOomPortn.setStatus("current")
_Pm10010ulhAlmLineTxOtnLomPortn_Type = EkiOnOff
_Pm10010ulhAlmLineTxOtnLomPortn_Object = MibTableColumn
pm10010ulhAlmLineTxOtnLomPortn = _Pm10010ulhAlmLineTxOtnLomPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 2, 204, 1, 15),
    _Pm10010ulhAlmLineTxOtnLomPortn_Type()
)
pm10010ulhAlmLineTxOtnLomPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmLineTxOtnLomPortn.setStatus("current")
_Pm10010ulhAlmLineTxOtnOofPortn_Type = EkiOnOff
_Pm10010ulhAlmLineTxOtnOofPortn_Object = MibTableColumn
pm10010ulhAlmLineTxOtnOofPortn = _Pm10010ulhAlmLineTxOtnOofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 2, 204, 1, 16),
    _Pm10010ulhAlmLineTxOtnOofPortn_Type()
)
pm10010ulhAlmLineTxOtnOofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmLineTxOtnOofPortn.setStatus("current")
_Pm10010ulhAlmLineTxOtnLofPortn_Type = EkiOnOff
_Pm10010ulhAlmLineTxOtnLofPortn_Object = MibTableColumn
pm10010ulhAlmLineTxOtnLofPortn = _Pm10010ulhAlmLineTxOtnLofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 2, 204, 1, 17),
    _Pm10010ulhAlmLineTxOtnLofPortn_Type()
)
pm10010ulhAlmLineTxOtnLofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmLineTxOtnLofPortn.setStatus("current")
_Pm10010ulhAlmLineCrit_ObjectIdentity = ObjectIdentity
pm10010ulhAlmLineCrit = _Pm10010ulhAlmLineCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 3)
)
_Pm10010ulhAlmsynthAlmLineTable_Object = MibTable
pm10010ulhAlmsynthAlmLineTable = _Pm10010ulhAlmsynthAlmLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 3, 40)
)
if mibBuilder.loadTexts:
    pm10010ulhAlmsynthAlmLineTable.setStatus("current")
_Pm10010ulhAlmsynthAlmLineEntry_Object = MibTableRow
pm10010ulhAlmsynthAlmLineEntry = _Pm10010ulhAlmsynthAlmLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 3, 40, 1)
)
pm10010ulhAlmsynthAlmLineEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhAlmsynthAlmLineIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhAlmsynthAlmLineEntry.setStatus("current")


class _Pm10010ulhAlmsynthAlmLineIndex_Type(Integer32):
    """Custom type pm10010ulhAlmsynthAlmLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhAlmsynthAlmLineIndex_Type.__name__ = "Integer32"
_Pm10010ulhAlmsynthAlmLineIndex_Object = MibTableColumn
pm10010ulhAlmsynthAlmLineIndex = _Pm10010ulhAlmsynthAlmLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 3, 40, 1, 1),
    _Pm10010ulhAlmsynthAlmLineIndex_Type()
)
pm10010ulhAlmsynthAlmLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmsynthAlmLineIndex.setStatus("current")
_Pm10010ulhAlmXfpAbsentPortn_Type = EkiOnOff
_Pm10010ulhAlmXfpAbsentPortn_Object = MibTableColumn
pm10010ulhAlmXfpAbsentPortn = _Pm10010ulhAlmXfpAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 3, 40, 1, 2),
    _Pm10010ulhAlmXfpAbsentPortn_Type()
)
pm10010ulhAlmXfpAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmXfpAbsentPortn.setStatus("current")
_Pm10010ulhAlmXfpInitNotComplPortn_Type = EkiOnOff
_Pm10010ulhAlmXfpInitNotComplPortn_Object = MibTableColumn
pm10010ulhAlmXfpInitNotComplPortn = _Pm10010ulhAlmXfpInitNotComplPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 3, 40, 1, 3),
    _Pm10010ulhAlmXfpInitNotComplPortn_Type()
)
pm10010ulhAlmXfpInitNotComplPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmXfpInitNotComplPortn.setStatus("current")
_Pm10010ulhAlmLineHwFailPortn_Type = EkiOnOff
_Pm10010ulhAlmLineHwFailPortn_Object = MibTableColumn
pm10010ulhAlmLineHwFailPortn = _Pm10010ulhAlmLineHwFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 3, 40, 1, 5),
    _Pm10010ulhAlmLineHwFailPortn_Type()
)
pm10010ulhAlmLineHwFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmLineHwFailPortn.setStatus("current")
_Pm10010ulhAlmXfpTxOffPortn_Type = EkiOnOff
_Pm10010ulhAlmXfpTxOffPortn_Object = MibTableColumn
pm10010ulhAlmXfpTxOffPortn = _Pm10010ulhAlmXfpTxOffPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 3, 40, 1, 6),
    _Pm10010ulhAlmXfpTxOffPortn_Type()
)
pm10010ulhAlmXfpTxOffPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmXfpTxOffPortn.setStatus("current")
_Pm10010ulhAlmLineLocalOosPortn_Type = EkiOnOff
_Pm10010ulhAlmLineLocalOosPortn_Object = MibTableColumn
pm10010ulhAlmLineLocalOosPortn = _Pm10010ulhAlmLineLocalOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 3, 40, 1, 7),
    _Pm10010ulhAlmLineLocalOosPortn_Type()
)
pm10010ulhAlmLineLocalOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmLineLocalOosPortn.setStatus("current")
_Pm10010ulhAlmUpRdiInsPortn_Type = EkiOnOff
_Pm10010ulhAlmUpRdiInsPortn_Object = MibTableColumn
pm10010ulhAlmUpRdiInsPortn = _Pm10010ulhAlmUpRdiInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 3, 40, 1, 9),
    _Pm10010ulhAlmUpRdiInsPortn_Type()
)
pm10010ulhAlmUpRdiInsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmUpRdiInsPortn.setStatus("current")
_Pm10010ulhAlmLineDdmWarningPortn_Type = EkiOnOff
_Pm10010ulhAlmLineDdmWarningPortn_Object = MibTableColumn
pm10010ulhAlmLineDdmWarningPortn = _Pm10010ulhAlmLineDdmWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 3, 40, 1, 10),
    _Pm10010ulhAlmLineDdmWarningPortn_Type()
)
pm10010ulhAlmLineDdmWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmLineDdmWarningPortn.setStatus("current")
_Pm10010ulhAlmLineDdmAlmPortn_Type = EkiOnOff
_Pm10010ulhAlmLineDdmAlmPortn_Object = MibTableColumn
pm10010ulhAlmLineDdmAlmPortn = _Pm10010ulhAlmLineDdmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 3, 40, 1, 11),
    _Pm10010ulhAlmLineDdmAlmPortn_Type()
)
pm10010ulhAlmLineDdmAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmLineDdmAlmPortn.setStatus("current")
_Pm10010ulhAlmLineFailPortn_Type = EkiOnOff
_Pm10010ulhAlmLineFailPortn_Object = MibTableColumn
pm10010ulhAlmLineFailPortn = _Pm10010ulhAlmLineFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 3, 40, 1, 13),
    _Pm10010ulhAlmLineFailPortn_Type()
)
pm10010ulhAlmLineFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmLineFailPortn.setStatus("current")
_Pm10010ulhAlmLineActivePortn_Type = EkiOnOff
_Pm10010ulhAlmLineActivePortn_Object = MibTableColumn
pm10010ulhAlmLineActivePortn = _Pm10010ulhAlmLineActivePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 2, 3, 3, 40, 1, 17),
    _Pm10010ulhAlmLineActivePortn_Type()
)
pm10010ulhAlmLineActivePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhAlmLineActivePortn.setStatus("current")
_Pm10010ulhmeasures_ObjectIdentity = ObjectIdentity
pm10010ulhmeasures = _Pm10010ulhmeasures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3)
)
_Pm10010ulhMesrOther_ObjectIdentity = ObjectIdentity
pm10010ulhMesrOther = _Pm10010ulhMesrOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 1)
)
_Pm10010ulhMesrsynth0_Type = EkiMeasureType
_Pm10010ulhMesrsynth0_Object = MibScalar
pm10010ulhMesrsynth0 = _Pm10010ulhMesrsynth0_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 1, 0),
    _Pm10010ulhMesrsynth0_Type()
)
pm10010ulhMesrsynth0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrsynth0.setStatus("deprecated")
_Pm10010ulhMesrsynth1_Type = EkiMeasureType
_Pm10010ulhMesrsynth1_Object = MibScalar
pm10010ulhMesrsynth1 = _Pm10010ulhMesrsynth1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 1, 1),
    _Pm10010ulhMesrsynth1_Type()
)
pm10010ulhMesrsynth1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrsynth1.setStatus("deprecated")


class _Pm10010ulhMesrpmIntervalNumber_Type(Unsigned32):
    """Custom type pm10010ulhMesrpmIntervalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010ulhMesrpmIntervalNumber_Type.__name__ = "Unsigned32"
_Pm10010ulhMesrpmIntervalNumber_Object = MibScalar
pm10010ulhMesrpmIntervalNumber = _Pm10010ulhMesrpmIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 1, 7),
    _Pm10010ulhMesrpmIntervalNumber_Type()
)
pm10010ulhMesrpmIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrpmIntervalNumber.setStatus("current")


class _Pm10010ulhMesrlineNetTxLaserOutputPwrAverage_Type(Unsigned32):
    """Custom type pm10010ulhMesrlineNetTxLaserOutputPwrAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010ulhMesrlineNetTxLaserOutputPwrAverage_Type.__name__ = "Unsigned32"
_Pm10010ulhMesrlineNetTxLaserOutputPwrAverage_Object = MibScalar
pm10010ulhMesrlineNetTxLaserOutputPwrAverage = _Pm10010ulhMesrlineNetTxLaserOutputPwrAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 1, 196),
    _Pm10010ulhMesrlineNetTxLaserOutputPwrAverage_Type()
)
pm10010ulhMesrlineNetTxLaserOutputPwrAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrlineNetTxLaserOutputPwrAverage.setStatus("current")


class _Pm10010ulhMesrlineNetTxLaserTempAverage_Type(Unsigned32):
    """Custom type pm10010ulhMesrlineNetTxLaserTempAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010ulhMesrlineNetTxLaserTempAverage_Type.__name__ = "Unsigned32"
_Pm10010ulhMesrlineNetTxLaserTempAverage_Object = MibScalar
pm10010ulhMesrlineNetTxLaserTempAverage = _Pm10010ulhMesrlineNetTxLaserTempAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 1, 197),
    _Pm10010ulhMesrlineNetTxLaserTempAverage_Type()
)
pm10010ulhMesrlineNetTxLaserTempAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrlineNetTxLaserTempAverage.setStatus("current")


class _Pm10010ulhMesrlineNetTxBiasCurrentAverage_Type(Unsigned32):
    """Custom type pm10010ulhMesrlineNetTxBiasCurrentAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010ulhMesrlineNetTxBiasCurrentAverage_Type.__name__ = "Unsigned32"
_Pm10010ulhMesrlineNetTxBiasCurrentAverage_Object = MibScalar
pm10010ulhMesrlineNetTxBiasCurrentAverage = _Pm10010ulhMesrlineNetTxBiasCurrentAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 1, 198),
    _Pm10010ulhMesrlineNetTxBiasCurrentAverage_Type()
)
pm10010ulhMesrlineNetTxBiasCurrentAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrlineNetTxBiasCurrentAverage.setStatus("current")


class _Pm10010ulhMesrlineNetRxInputPwrAverage_Type(Unsigned32):
    """Custom type pm10010ulhMesrlineNetRxInputPwrAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010ulhMesrlineNetRxInputPwrAverage_Type.__name__ = "Unsigned32"
_Pm10010ulhMesrlineNetRxInputPwrAverage_Object = MibScalar
pm10010ulhMesrlineNetRxInputPwrAverage = _Pm10010ulhMesrlineNetRxInputPwrAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 1, 199),
    _Pm10010ulhMesrlineNetRxInputPwrAverage_Type()
)
pm10010ulhMesrlineNetRxInputPwrAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrlineNetRxInputPwrAverage.setStatus("current")


class _Pm10010ulhMesrlineResidualChromaticDispAverage_Type(Unsigned32):
    """Custom type pm10010ulhMesrlineResidualChromaticDispAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010ulhMesrlineResidualChromaticDispAverage_Type.__name__ = "Unsigned32"
_Pm10010ulhMesrlineResidualChromaticDispAverage_Object = MibScalar
pm10010ulhMesrlineResidualChromaticDispAverage = _Pm10010ulhMesrlineResidualChromaticDispAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 1, 200),
    _Pm10010ulhMesrlineResidualChromaticDispAverage_Type()
)
pm10010ulhMesrlineResidualChromaticDispAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrlineResidualChromaticDispAverage.setStatus("current")


class _Pm10010ulhMesrlineDiffGroupDelayAverage_Type(Unsigned32):
    """Custom type pm10010ulhMesrlineDiffGroupDelayAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010ulhMesrlineDiffGroupDelayAverage_Type.__name__ = "Unsigned32"
_Pm10010ulhMesrlineDiffGroupDelayAverage_Object = MibScalar
pm10010ulhMesrlineDiffGroupDelayAverage = _Pm10010ulhMesrlineDiffGroupDelayAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 1, 201),
    _Pm10010ulhMesrlineDiffGroupDelayAverage_Type()
)
pm10010ulhMesrlineDiffGroupDelayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrlineDiffGroupDelayAverage.setStatus("current")


class _Pm10010ulhMesrlineQFactorAverage_Type(Unsigned32):
    """Custom type pm10010ulhMesrlineQFactorAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010ulhMesrlineQFactorAverage_Type.__name__ = "Unsigned32"
_Pm10010ulhMesrlineQFactorAverage_Object = MibScalar
pm10010ulhMesrlineQFactorAverage = _Pm10010ulhMesrlineQFactorAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 1, 202),
    _Pm10010ulhMesrlineQFactorAverage_Type()
)
pm10010ulhMesrlineQFactorAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrlineQFactorAverage.setStatus("current")


class _Pm10010ulhMesrlineCarrierFreqOffsetAverage_Type(Unsigned32):
    """Custom type pm10010ulhMesrlineCarrierFreqOffsetAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010ulhMesrlineCarrierFreqOffsetAverage_Type.__name__ = "Unsigned32"
_Pm10010ulhMesrlineCarrierFreqOffsetAverage_Object = MibScalar
pm10010ulhMesrlineCarrierFreqOffsetAverage = _Pm10010ulhMesrlineCarrierFreqOffsetAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 1, 203),
    _Pm10010ulhMesrlineCarrierFreqOffsetAverage_Type()
)
pm10010ulhMesrlineCarrierFreqOffsetAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrlineCarrierFreqOffsetAverage.setStatus("current")


class _Pm10010ulhMesrlineOsnrAverage_Type(Unsigned32):
    """Custom type pm10010ulhMesrlineOsnrAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010ulhMesrlineOsnrAverage_Type.__name__ = "Unsigned32"
_Pm10010ulhMesrlineOsnrAverage_Object = MibScalar
pm10010ulhMesrlineOsnrAverage = _Pm10010ulhMesrlineOsnrAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 1, 204),
    _Pm10010ulhMesrlineOsnrAverage_Type()
)
pm10010ulhMesrlineOsnrAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrlineOsnrAverage.setStatus("current")


class _Pm10010ulhMesrclientNetTxTempMin_Type(Unsigned32):
    """Custom type pm10010ulhMesrclientNetTxTempMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010ulhMesrclientNetTxTempMin_Type.__name__ = "Unsigned32"
_Pm10010ulhMesrclientNetTxTempMin_Object = MibScalar
pm10010ulhMesrclientNetTxTempMin = _Pm10010ulhMesrclientNetTxTempMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 1, 208),
    _Pm10010ulhMesrclientNetTxTempMin_Type()
)
pm10010ulhMesrclientNetTxTempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrclientNetTxTempMin.setStatus("current")


class _Pm10010ulhMesrclientNetTxBiasMin_Type(Unsigned32):
    """Custom type pm10010ulhMesrclientNetTxBiasMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010ulhMesrclientNetTxBiasMin_Type.__name__ = "Unsigned32"
_Pm10010ulhMesrclientNetTxBiasMin_Object = MibScalar
pm10010ulhMesrclientNetTxBiasMin = _Pm10010ulhMesrclientNetTxBiasMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 1, 209),
    _Pm10010ulhMesrclientNetTxBiasMin_Type()
)
pm10010ulhMesrclientNetTxBiasMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrclientNetTxBiasMin.setStatus("current")


class _Pm10010ulhMesrclientNetTxPwrMin_Type(Unsigned32):
    """Custom type pm10010ulhMesrclientNetTxPwrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010ulhMesrclientNetTxPwrMin_Type.__name__ = "Unsigned32"
_Pm10010ulhMesrclientNetTxPwrMin_Object = MibScalar
pm10010ulhMesrclientNetTxPwrMin = _Pm10010ulhMesrclientNetTxPwrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 1, 210),
    _Pm10010ulhMesrclientNetTxPwrMin_Type()
)
pm10010ulhMesrclientNetTxPwrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrclientNetTxPwrMin.setStatus("current")


class _Pm10010ulhMesrclientNetRxPwrMin_Type(Unsigned32):
    """Custom type pm10010ulhMesrclientNetRxPwrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010ulhMesrclientNetRxPwrMin_Type.__name__ = "Unsigned32"
_Pm10010ulhMesrclientNetRxPwrMin_Object = MibScalar
pm10010ulhMesrclientNetRxPwrMin = _Pm10010ulhMesrclientNetRxPwrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 1, 211),
    _Pm10010ulhMesrclientNetRxPwrMin_Type()
)
pm10010ulhMesrclientNetRxPwrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrclientNetRxPwrMin.setStatus("current")


class _Pm10010ulhMesrlineNetTxLaserOutputPwrMin_Type(Unsigned32):
    """Custom type pm10010ulhMesrlineNetTxLaserOutputPwrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010ulhMesrlineNetTxLaserOutputPwrMin_Type.__name__ = "Unsigned32"
_Pm10010ulhMesrlineNetTxLaserOutputPwrMin_Object = MibScalar
pm10010ulhMesrlineNetTxLaserOutputPwrMin = _Pm10010ulhMesrlineNetTxLaserOutputPwrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 1, 212),
    _Pm10010ulhMesrlineNetTxLaserOutputPwrMin_Type()
)
pm10010ulhMesrlineNetTxLaserOutputPwrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrlineNetTxLaserOutputPwrMin.setStatus("current")


class _Pm10010ulhMesrlineNetTxLaserTempMin_Type(Unsigned32):
    """Custom type pm10010ulhMesrlineNetTxLaserTempMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010ulhMesrlineNetTxLaserTempMin_Type.__name__ = "Unsigned32"
_Pm10010ulhMesrlineNetTxLaserTempMin_Object = MibScalar
pm10010ulhMesrlineNetTxLaserTempMin = _Pm10010ulhMesrlineNetTxLaserTempMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 1, 213),
    _Pm10010ulhMesrlineNetTxLaserTempMin_Type()
)
pm10010ulhMesrlineNetTxLaserTempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrlineNetTxLaserTempMin.setStatus("current")


class _Pm10010ulhMesrlineNetTxBiasCurrentMin_Type(Unsigned32):
    """Custom type pm10010ulhMesrlineNetTxBiasCurrentMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010ulhMesrlineNetTxBiasCurrentMin_Type.__name__ = "Unsigned32"
_Pm10010ulhMesrlineNetTxBiasCurrentMin_Object = MibScalar
pm10010ulhMesrlineNetTxBiasCurrentMin = _Pm10010ulhMesrlineNetTxBiasCurrentMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 1, 214),
    _Pm10010ulhMesrlineNetTxBiasCurrentMin_Type()
)
pm10010ulhMesrlineNetTxBiasCurrentMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrlineNetTxBiasCurrentMin.setStatus("current")


class _Pm10010ulhMesrlineNetRxInputPwrMin_Type(Unsigned32):
    """Custom type pm10010ulhMesrlineNetRxInputPwrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010ulhMesrlineNetRxInputPwrMin_Type.__name__ = "Unsigned32"
_Pm10010ulhMesrlineNetRxInputPwrMin_Object = MibScalar
pm10010ulhMesrlineNetRxInputPwrMin = _Pm10010ulhMesrlineNetRxInputPwrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 1, 215),
    _Pm10010ulhMesrlineNetRxInputPwrMin_Type()
)
pm10010ulhMesrlineNetRxInputPwrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrlineNetRxInputPwrMin.setStatus("current")


class _Pm10010ulhMesrlineResidualChromaticDispMin_Type(Unsigned32):
    """Custom type pm10010ulhMesrlineResidualChromaticDispMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010ulhMesrlineResidualChromaticDispMin_Type.__name__ = "Unsigned32"
_Pm10010ulhMesrlineResidualChromaticDispMin_Object = MibScalar
pm10010ulhMesrlineResidualChromaticDispMin = _Pm10010ulhMesrlineResidualChromaticDispMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 1, 216),
    _Pm10010ulhMesrlineResidualChromaticDispMin_Type()
)
pm10010ulhMesrlineResidualChromaticDispMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrlineResidualChromaticDispMin.setStatus("current")


class _Pm10010ulhMesrlineDiffGroupDelayMin_Type(Unsigned32):
    """Custom type pm10010ulhMesrlineDiffGroupDelayMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010ulhMesrlineDiffGroupDelayMin_Type.__name__ = "Unsigned32"
_Pm10010ulhMesrlineDiffGroupDelayMin_Object = MibScalar
pm10010ulhMesrlineDiffGroupDelayMin = _Pm10010ulhMesrlineDiffGroupDelayMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 1, 217),
    _Pm10010ulhMesrlineDiffGroupDelayMin_Type()
)
pm10010ulhMesrlineDiffGroupDelayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrlineDiffGroupDelayMin.setStatus("current")


class _Pm10010ulhMesrlineQFactorMin_Type(Unsigned32):
    """Custom type pm10010ulhMesrlineQFactorMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010ulhMesrlineQFactorMin_Type.__name__ = "Unsigned32"
_Pm10010ulhMesrlineQFactorMin_Object = MibScalar
pm10010ulhMesrlineQFactorMin = _Pm10010ulhMesrlineQFactorMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 1, 218),
    _Pm10010ulhMesrlineQFactorMin_Type()
)
pm10010ulhMesrlineQFactorMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrlineQFactorMin.setStatus("current")


class _Pm10010ulhMesrlineCarrierFreqOffsetMin_Type(Unsigned32):
    """Custom type pm10010ulhMesrlineCarrierFreqOffsetMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010ulhMesrlineCarrierFreqOffsetMin_Type.__name__ = "Unsigned32"
_Pm10010ulhMesrlineCarrierFreqOffsetMin_Object = MibScalar
pm10010ulhMesrlineCarrierFreqOffsetMin = _Pm10010ulhMesrlineCarrierFreqOffsetMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 1, 219),
    _Pm10010ulhMesrlineCarrierFreqOffsetMin_Type()
)
pm10010ulhMesrlineCarrierFreqOffsetMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrlineCarrierFreqOffsetMin.setStatus("current")


class _Pm10010ulhMesrlineOsnrMin_Type(Unsigned32):
    """Custom type pm10010ulhMesrlineOsnrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010ulhMesrlineOsnrMin_Type.__name__ = "Unsigned32"
_Pm10010ulhMesrlineOsnrMin_Object = MibScalar
pm10010ulhMesrlineOsnrMin = _Pm10010ulhMesrlineOsnrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 1, 220),
    _Pm10010ulhMesrlineOsnrMin_Type()
)
pm10010ulhMesrlineOsnrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrlineOsnrMin.setStatus("current")


class _Pm10010ulhMesrclientNetTxTempMax_Type(Unsigned32):
    """Custom type pm10010ulhMesrclientNetTxTempMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010ulhMesrclientNetTxTempMax_Type.__name__ = "Unsigned32"
_Pm10010ulhMesrclientNetTxTempMax_Object = MibScalar
pm10010ulhMesrclientNetTxTempMax = _Pm10010ulhMesrclientNetTxTempMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 1, 224),
    _Pm10010ulhMesrclientNetTxTempMax_Type()
)
pm10010ulhMesrclientNetTxTempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrclientNetTxTempMax.setStatus("current")


class _Pm10010ulhMesrclientNetTxBiasMax_Type(Unsigned32):
    """Custom type pm10010ulhMesrclientNetTxBiasMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010ulhMesrclientNetTxBiasMax_Type.__name__ = "Unsigned32"
_Pm10010ulhMesrclientNetTxBiasMax_Object = MibScalar
pm10010ulhMesrclientNetTxBiasMax = _Pm10010ulhMesrclientNetTxBiasMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 1, 225),
    _Pm10010ulhMesrclientNetTxBiasMax_Type()
)
pm10010ulhMesrclientNetTxBiasMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrclientNetTxBiasMax.setStatus("current")


class _Pm10010ulhMesrclientNetTxPwrMax_Type(Unsigned32):
    """Custom type pm10010ulhMesrclientNetTxPwrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010ulhMesrclientNetTxPwrMax_Type.__name__ = "Unsigned32"
_Pm10010ulhMesrclientNetTxPwrMax_Object = MibScalar
pm10010ulhMesrclientNetTxPwrMax = _Pm10010ulhMesrclientNetTxPwrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 1, 226),
    _Pm10010ulhMesrclientNetTxPwrMax_Type()
)
pm10010ulhMesrclientNetTxPwrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrclientNetTxPwrMax.setStatus("current")


class _Pm10010ulhMesrclientNetRxPwrMax_Type(Unsigned32):
    """Custom type pm10010ulhMesrclientNetRxPwrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010ulhMesrclientNetRxPwrMax_Type.__name__ = "Unsigned32"
_Pm10010ulhMesrclientNetRxPwrMax_Object = MibScalar
pm10010ulhMesrclientNetRxPwrMax = _Pm10010ulhMesrclientNetRxPwrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 1, 227),
    _Pm10010ulhMesrclientNetRxPwrMax_Type()
)
pm10010ulhMesrclientNetRxPwrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrclientNetRxPwrMax.setStatus("current")


class _Pm10010ulhMesrlineNetTxLaserOutputPwrMax_Type(Unsigned32):
    """Custom type pm10010ulhMesrlineNetTxLaserOutputPwrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010ulhMesrlineNetTxLaserOutputPwrMax_Type.__name__ = "Unsigned32"
_Pm10010ulhMesrlineNetTxLaserOutputPwrMax_Object = MibScalar
pm10010ulhMesrlineNetTxLaserOutputPwrMax = _Pm10010ulhMesrlineNetTxLaserOutputPwrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 1, 228),
    _Pm10010ulhMesrlineNetTxLaserOutputPwrMax_Type()
)
pm10010ulhMesrlineNetTxLaserOutputPwrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrlineNetTxLaserOutputPwrMax.setStatus("current")


class _Pm10010ulhMesrlineNetTxLaserTempMax_Type(Unsigned32):
    """Custom type pm10010ulhMesrlineNetTxLaserTempMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010ulhMesrlineNetTxLaserTempMax_Type.__name__ = "Unsigned32"
_Pm10010ulhMesrlineNetTxLaserTempMax_Object = MibScalar
pm10010ulhMesrlineNetTxLaserTempMax = _Pm10010ulhMesrlineNetTxLaserTempMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 1, 229),
    _Pm10010ulhMesrlineNetTxLaserTempMax_Type()
)
pm10010ulhMesrlineNetTxLaserTempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrlineNetTxLaserTempMax.setStatus("current")


class _Pm10010ulhMesrlineNetTxBiasCurrentMax_Type(Unsigned32):
    """Custom type pm10010ulhMesrlineNetTxBiasCurrentMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010ulhMesrlineNetTxBiasCurrentMax_Type.__name__ = "Unsigned32"
_Pm10010ulhMesrlineNetTxBiasCurrentMax_Object = MibScalar
pm10010ulhMesrlineNetTxBiasCurrentMax = _Pm10010ulhMesrlineNetTxBiasCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 1, 230),
    _Pm10010ulhMesrlineNetTxBiasCurrentMax_Type()
)
pm10010ulhMesrlineNetTxBiasCurrentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrlineNetTxBiasCurrentMax.setStatus("current")


class _Pm10010ulhMesrlineNetRxInputPwrMax_Type(Unsigned32):
    """Custom type pm10010ulhMesrlineNetRxInputPwrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010ulhMesrlineNetRxInputPwrMax_Type.__name__ = "Unsigned32"
_Pm10010ulhMesrlineNetRxInputPwrMax_Object = MibScalar
pm10010ulhMesrlineNetRxInputPwrMax = _Pm10010ulhMesrlineNetRxInputPwrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 1, 231),
    _Pm10010ulhMesrlineNetRxInputPwrMax_Type()
)
pm10010ulhMesrlineNetRxInputPwrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrlineNetRxInputPwrMax.setStatus("current")


class _Pm10010ulhMesrlineResidualChromaticDispMax_Type(Unsigned32):
    """Custom type pm10010ulhMesrlineResidualChromaticDispMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010ulhMesrlineResidualChromaticDispMax_Type.__name__ = "Unsigned32"
_Pm10010ulhMesrlineResidualChromaticDispMax_Object = MibScalar
pm10010ulhMesrlineResidualChromaticDispMax = _Pm10010ulhMesrlineResidualChromaticDispMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 1, 232),
    _Pm10010ulhMesrlineResidualChromaticDispMax_Type()
)
pm10010ulhMesrlineResidualChromaticDispMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrlineResidualChromaticDispMax.setStatus("current")


class _Pm10010ulhMesrlineDiffGroupDelayMax_Type(Unsigned32):
    """Custom type pm10010ulhMesrlineDiffGroupDelayMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010ulhMesrlineDiffGroupDelayMax_Type.__name__ = "Unsigned32"
_Pm10010ulhMesrlineDiffGroupDelayMax_Object = MibScalar
pm10010ulhMesrlineDiffGroupDelayMax = _Pm10010ulhMesrlineDiffGroupDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 1, 233),
    _Pm10010ulhMesrlineDiffGroupDelayMax_Type()
)
pm10010ulhMesrlineDiffGroupDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrlineDiffGroupDelayMax.setStatus("current")


class _Pm10010ulhMesrlineQFactorMax_Type(Unsigned32):
    """Custom type pm10010ulhMesrlineQFactorMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010ulhMesrlineQFactorMax_Type.__name__ = "Unsigned32"
_Pm10010ulhMesrlineQFactorMax_Object = MibScalar
pm10010ulhMesrlineQFactorMax = _Pm10010ulhMesrlineQFactorMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 1, 234),
    _Pm10010ulhMesrlineQFactorMax_Type()
)
pm10010ulhMesrlineQFactorMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrlineQFactorMax.setStatus("current")


class _Pm10010ulhMesrlineCarrierFreqOffsetMax_Type(Unsigned32):
    """Custom type pm10010ulhMesrlineCarrierFreqOffsetMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010ulhMesrlineCarrierFreqOffsetMax_Type.__name__ = "Unsigned32"
_Pm10010ulhMesrlineCarrierFreqOffsetMax_Object = MibScalar
pm10010ulhMesrlineCarrierFreqOffsetMax = _Pm10010ulhMesrlineCarrierFreqOffsetMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 1, 235),
    _Pm10010ulhMesrlineCarrierFreqOffsetMax_Type()
)
pm10010ulhMesrlineCarrierFreqOffsetMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrlineCarrierFreqOffsetMax.setStatus("current")


class _Pm10010ulhMesrlineOsnrMax_Type(Unsigned32):
    """Custom type pm10010ulhMesrlineOsnrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010ulhMesrlineOsnrMax_Type.__name__ = "Unsigned32"
_Pm10010ulhMesrlineOsnrMax_Object = MibScalar
pm10010ulhMesrlineOsnrMax = _Pm10010ulhMesrlineOsnrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 1, 236),
    _Pm10010ulhMesrlineOsnrMax_Type()
)
pm10010ulhMesrlineOsnrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrlineOsnrMax.setStatus("current")
_Pm10010ulhMesrClient_ObjectIdentity = ObjectIdentity
pm10010ulhMesrClient = _Pm10010ulhMesrClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 2)
)


class _Pm10010ulhMesrclientCfpTemp_Type(Unsigned32):
    """Custom type pm10010ulhMesrclientCfpTemp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010ulhMesrclientCfpTemp_Type.__name__ = "Unsigned32"
_Pm10010ulhMesrclientCfpTemp_Object = MibScalar
pm10010ulhMesrclientCfpTemp = _Pm10010ulhMesrclientCfpTemp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 2, 8),
    _Pm10010ulhMesrclientCfpTemp_Type()
)
pm10010ulhMesrclientCfpTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrclientCfpTemp.setStatus("current")


class _Pm10010ulhMesrclientCfp3v3Voltage_Type(Unsigned32):
    """Custom type pm10010ulhMesrclientCfp3v3Voltage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010ulhMesrclientCfp3v3Voltage_Type.__name__ = "Unsigned32"
_Pm10010ulhMesrclientCfp3v3Voltage_Object = MibScalar
pm10010ulhMesrclientCfp3v3Voltage = _Pm10010ulhMesrclientCfp3v3Voltage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 2, 9),
    _Pm10010ulhMesrclientCfp3v3Voltage_Type()
)
pm10010ulhMesrclientCfp3v3Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrclientCfp3v3Voltage.setStatus("current")


class _Pm10010ulhMesrclientSoaBiasCurrent_Type(Unsigned32):
    """Custom type pm10010ulhMesrclientSoaBiasCurrent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010ulhMesrclientSoaBiasCurrent_Type.__name__ = "Unsigned32"
_Pm10010ulhMesrclientSoaBiasCurrent_Object = MibScalar
pm10010ulhMesrclientSoaBiasCurrent = _Pm10010ulhMesrclientSoaBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 2, 10),
    _Pm10010ulhMesrclientSoaBiasCurrent_Type()
)
pm10010ulhMesrclientSoaBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrclientSoaBiasCurrent.setStatus("current")
_Pm10010ulhMesrclientNetTxTempTable_Object = MibTable
pm10010ulhMesrclientNetTxTempTable = _Pm10010ulhMesrclientNetTxTempTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 2, 16)
)
if mibBuilder.loadTexts:
    pm10010ulhMesrclientNetTxTempTable.setStatus("current")
_Pm10010ulhMesrclientNetTxTempEntry_Object = MibTableRow
pm10010ulhMesrclientNetTxTempEntry = _Pm10010ulhMesrclientNetTxTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 2, 16, 1)
)
pm10010ulhMesrclientNetTxTempEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhMesrclientNetTxTempIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhMesrclientNetTxTempEntry.setStatus("current")


class _Pm10010ulhMesrclientNetTxTempIndex_Type(Integer32):
    """Custom type pm10010ulhMesrclientNetTxTempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhMesrclientNetTxTempIndex_Type.__name__ = "Integer32"
_Pm10010ulhMesrclientNetTxTempIndex_Object = MibTableColumn
pm10010ulhMesrclientNetTxTempIndex = _Pm10010ulhMesrclientNetTxTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 2, 16, 1, 1),
    _Pm10010ulhMesrclientNetTxTempIndex_Type()
)
pm10010ulhMesrclientNetTxTempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrclientNetTxTempIndex.setStatus("current")


class _Pm10010ulhMesrclientNetTxTempPortn_Type(Integer32):
    """Custom type pm10010ulhMesrclientNetTxTempPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010ulhMesrclientNetTxTempPortn_Type.__name__ = "Integer32"
_Pm10010ulhMesrclientNetTxTempPortn_Object = MibTableColumn
pm10010ulhMesrclientNetTxTempPortn = _Pm10010ulhMesrclientNetTxTempPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 2, 16, 1, 2),
    _Pm10010ulhMesrclientNetTxTempPortn_Type()
)
pm10010ulhMesrclientNetTxTempPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrclientNetTxTempPortn.setStatus("current")
_Pm10010ulhMesrclientNetTxBiasTable_Object = MibTable
pm10010ulhMesrclientNetTxBiasTable = _Pm10010ulhMesrclientNetTxBiasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 2, 48)
)
if mibBuilder.loadTexts:
    pm10010ulhMesrclientNetTxBiasTable.setStatus("current")
_Pm10010ulhMesrclientNetTxBiasEntry_Object = MibTableRow
pm10010ulhMesrclientNetTxBiasEntry = _Pm10010ulhMesrclientNetTxBiasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 2, 48, 1)
)
pm10010ulhMesrclientNetTxBiasEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhMesrclientNetTxBiasIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhMesrclientNetTxBiasEntry.setStatus("current")


class _Pm10010ulhMesrclientNetTxBiasIndex_Type(Integer32):
    """Custom type pm10010ulhMesrclientNetTxBiasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhMesrclientNetTxBiasIndex_Type.__name__ = "Integer32"
_Pm10010ulhMesrclientNetTxBiasIndex_Object = MibTableColumn
pm10010ulhMesrclientNetTxBiasIndex = _Pm10010ulhMesrclientNetTxBiasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 2, 48, 1, 1),
    _Pm10010ulhMesrclientNetTxBiasIndex_Type()
)
pm10010ulhMesrclientNetTxBiasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrclientNetTxBiasIndex.setStatus("current")


class _Pm10010ulhMesrclientNetTxBiasPortn_Type(Integer32):
    """Custom type pm10010ulhMesrclientNetTxBiasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010ulhMesrclientNetTxBiasPortn_Type.__name__ = "Integer32"
_Pm10010ulhMesrclientNetTxBiasPortn_Object = MibTableColumn
pm10010ulhMesrclientNetTxBiasPortn = _Pm10010ulhMesrclientNetTxBiasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 2, 48, 1, 2),
    _Pm10010ulhMesrclientNetTxBiasPortn_Type()
)
pm10010ulhMesrclientNetTxBiasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrclientNetTxBiasPortn.setStatus("current")
_Pm10010ulhMesrclientNetTxPwrTable_Object = MibTable
pm10010ulhMesrclientNetTxPwrTable = _Pm10010ulhMesrclientNetTxPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 2, 80)
)
if mibBuilder.loadTexts:
    pm10010ulhMesrclientNetTxPwrTable.setStatus("current")
_Pm10010ulhMesrclientNetTxPwrEntry_Object = MibTableRow
pm10010ulhMesrclientNetTxPwrEntry = _Pm10010ulhMesrclientNetTxPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 2, 80, 1)
)
pm10010ulhMesrclientNetTxPwrEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhMesrclientNetTxPwrIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhMesrclientNetTxPwrEntry.setStatus("current")


class _Pm10010ulhMesrclientNetTxPwrIndex_Type(Integer32):
    """Custom type pm10010ulhMesrclientNetTxPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhMesrclientNetTxPwrIndex_Type.__name__ = "Integer32"
_Pm10010ulhMesrclientNetTxPwrIndex_Object = MibTableColumn
pm10010ulhMesrclientNetTxPwrIndex = _Pm10010ulhMesrclientNetTxPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 2, 80, 1, 1),
    _Pm10010ulhMesrclientNetTxPwrIndex_Type()
)
pm10010ulhMesrclientNetTxPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrclientNetTxPwrIndex.setStatus("current")


class _Pm10010ulhMesrclientNetTxPwrPortn_Type(Integer32):
    """Custom type pm10010ulhMesrclientNetTxPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010ulhMesrclientNetTxPwrPortn_Type.__name__ = "Integer32"
_Pm10010ulhMesrclientNetTxPwrPortn_Object = MibTableColumn
pm10010ulhMesrclientNetTxPwrPortn = _Pm10010ulhMesrclientNetTxPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 2, 80, 1, 2),
    _Pm10010ulhMesrclientNetTxPwrPortn_Type()
)
pm10010ulhMesrclientNetTxPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrclientNetTxPwrPortn.setStatus("current")
_Pm10010ulhMesrclientNetRxPwrTable_Object = MibTable
pm10010ulhMesrclientNetRxPwrTable = _Pm10010ulhMesrclientNetRxPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 2, 112)
)
if mibBuilder.loadTexts:
    pm10010ulhMesrclientNetRxPwrTable.setStatus("current")
_Pm10010ulhMesrclientNetRxPwrEntry_Object = MibTableRow
pm10010ulhMesrclientNetRxPwrEntry = _Pm10010ulhMesrclientNetRxPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 2, 112, 1)
)
pm10010ulhMesrclientNetRxPwrEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhMesrclientNetRxPwrIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhMesrclientNetRxPwrEntry.setStatus("current")


class _Pm10010ulhMesrclientNetRxPwrIndex_Type(Integer32):
    """Custom type pm10010ulhMesrclientNetRxPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhMesrclientNetRxPwrIndex_Type.__name__ = "Integer32"
_Pm10010ulhMesrclientNetRxPwrIndex_Object = MibTableColumn
pm10010ulhMesrclientNetRxPwrIndex = _Pm10010ulhMesrclientNetRxPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 2, 112, 1, 1),
    _Pm10010ulhMesrclientNetRxPwrIndex_Type()
)
pm10010ulhMesrclientNetRxPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrclientNetRxPwrIndex.setStatus("current")


class _Pm10010ulhMesrclientNetRxPwrPortn_Type(Integer32):
    """Custom type pm10010ulhMesrclientNetRxPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010ulhMesrclientNetRxPwrPortn_Type.__name__ = "Integer32"
_Pm10010ulhMesrclientNetRxPwrPortn_Object = MibTableColumn
pm10010ulhMesrclientNetRxPwrPortn = _Pm10010ulhMesrclientNetRxPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 2, 112, 1, 2),
    _Pm10010ulhMesrclientNetRxPwrPortn_Type()
)
pm10010ulhMesrclientNetRxPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrclientNetRxPwrPortn.setStatus("current")
_Pm10010ulhMesrLine_ObjectIdentity = ObjectIdentity
pm10010ulhMesrLine = _Pm10010ulhMesrLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 3)
)


class _Pm10010ulhMesrlineMsaTemp_Type(Unsigned32):
    """Custom type pm10010ulhMesrlineMsaTemp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010ulhMesrlineMsaTemp_Type.__name__ = "Unsigned32"
_Pm10010ulhMesrlineMsaTemp_Object = MibScalar
pm10010ulhMesrlineMsaTemp = _Pm10010ulhMesrlineMsaTemp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 3, 12),
    _Pm10010ulhMesrlineMsaTemp_Type()
)
pm10010ulhMesrlineMsaTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrlineMsaTemp.setStatus("current")


class _Pm10010ulhMesrlineMsa3v3Voltage_Type(Unsigned32):
    """Custom type pm10010ulhMesrlineMsa3v3Voltage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010ulhMesrlineMsa3v3Voltage_Type.__name__ = "Unsigned32"
_Pm10010ulhMesrlineMsa3v3Voltage_Object = MibScalar
pm10010ulhMesrlineMsa3v3Voltage = _Pm10010ulhMesrlineMsa3v3Voltage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 3, 13),
    _Pm10010ulhMesrlineMsa3v3Voltage_Type()
)
pm10010ulhMesrlineMsa3v3Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrlineMsa3v3Voltage.setStatus("current")


class _Pm10010ulhMesrlineSoaBiasCurrent_Type(Unsigned32):
    """Custom type pm10010ulhMesrlineSoaBiasCurrent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010ulhMesrlineSoaBiasCurrent_Type.__name__ = "Unsigned32"
_Pm10010ulhMesrlineSoaBiasCurrent_Object = MibScalar
pm10010ulhMesrlineSoaBiasCurrent = _Pm10010ulhMesrlineSoaBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 3, 14),
    _Pm10010ulhMesrlineSoaBiasCurrent_Type()
)
pm10010ulhMesrlineSoaBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrlineSoaBiasCurrent.setStatus("current")
_Pm10010ulhMesrlineNetTxLaserOutputPwrTable_Object = MibTable
pm10010ulhMesrlineNetTxLaserOutputPwrTable = _Pm10010ulhMesrlineNetTxLaserOutputPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 3, 144)
)
if mibBuilder.loadTexts:
    pm10010ulhMesrlineNetTxLaserOutputPwrTable.setStatus("current")
_Pm10010ulhMesrlineNetTxLaserOutputPwrEntry_Object = MibTableRow
pm10010ulhMesrlineNetTxLaserOutputPwrEntry = _Pm10010ulhMesrlineNetTxLaserOutputPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 3, 144, 1)
)
pm10010ulhMesrlineNetTxLaserOutputPwrEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhMesrlineNetTxLaserOutputPwrIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhMesrlineNetTxLaserOutputPwrEntry.setStatus("current")


class _Pm10010ulhMesrlineNetTxLaserOutputPwrIndex_Type(Integer32):
    """Custom type pm10010ulhMesrlineNetTxLaserOutputPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhMesrlineNetTxLaserOutputPwrIndex_Type.__name__ = "Integer32"
_Pm10010ulhMesrlineNetTxLaserOutputPwrIndex_Object = MibTableColumn
pm10010ulhMesrlineNetTxLaserOutputPwrIndex = _Pm10010ulhMesrlineNetTxLaserOutputPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 3, 144, 1, 1),
    _Pm10010ulhMesrlineNetTxLaserOutputPwrIndex_Type()
)
pm10010ulhMesrlineNetTxLaserOutputPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrlineNetTxLaserOutputPwrIndex.setStatus("current")


class _Pm10010ulhMesrlineNetTxLaserOutputPwrPortn_Type(Integer32):
    """Custom type pm10010ulhMesrlineNetTxLaserOutputPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010ulhMesrlineNetTxLaserOutputPwrPortn_Type.__name__ = "Integer32"
_Pm10010ulhMesrlineNetTxLaserOutputPwrPortn_Object = MibTableColumn
pm10010ulhMesrlineNetTxLaserOutputPwrPortn = _Pm10010ulhMesrlineNetTxLaserOutputPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 3, 144, 1, 2),
    _Pm10010ulhMesrlineNetTxLaserOutputPwrPortn_Type()
)
pm10010ulhMesrlineNetTxLaserOutputPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrlineNetTxLaserOutputPwrPortn.setStatus("current")
_Pm10010ulhMesrlineNetTxLaserTempTable_Object = MibTable
pm10010ulhMesrlineNetTxLaserTempTable = _Pm10010ulhMesrlineNetTxLaserTempTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 3, 148)
)
if mibBuilder.loadTexts:
    pm10010ulhMesrlineNetTxLaserTempTable.setStatus("current")
_Pm10010ulhMesrlineNetTxLaserTempEntry_Object = MibTableRow
pm10010ulhMesrlineNetTxLaserTempEntry = _Pm10010ulhMesrlineNetTxLaserTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 3, 148, 1)
)
pm10010ulhMesrlineNetTxLaserTempEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhMesrlineNetTxLaserTempIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhMesrlineNetTxLaserTempEntry.setStatus("current")


class _Pm10010ulhMesrlineNetTxLaserTempIndex_Type(Integer32):
    """Custom type pm10010ulhMesrlineNetTxLaserTempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhMesrlineNetTxLaserTempIndex_Type.__name__ = "Integer32"
_Pm10010ulhMesrlineNetTxLaserTempIndex_Object = MibTableColumn
pm10010ulhMesrlineNetTxLaserTempIndex = _Pm10010ulhMesrlineNetTxLaserTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 3, 148, 1, 1),
    _Pm10010ulhMesrlineNetTxLaserTempIndex_Type()
)
pm10010ulhMesrlineNetTxLaserTempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrlineNetTxLaserTempIndex.setStatus("current")


class _Pm10010ulhMesrlineNetTxLaserTempPortn_Type(Integer32):
    """Custom type pm10010ulhMesrlineNetTxLaserTempPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010ulhMesrlineNetTxLaserTempPortn_Type.__name__ = "Integer32"
_Pm10010ulhMesrlineNetTxLaserTempPortn_Object = MibTableColumn
pm10010ulhMesrlineNetTxLaserTempPortn = _Pm10010ulhMesrlineNetTxLaserTempPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 3, 148, 1, 2),
    _Pm10010ulhMesrlineNetTxLaserTempPortn_Type()
)
pm10010ulhMesrlineNetTxLaserTempPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrlineNetTxLaserTempPortn.setStatus("current")
_Pm10010ulhMesrlineNetTxBiasCurrentTable_Object = MibTable
pm10010ulhMesrlineNetTxBiasCurrentTable = _Pm10010ulhMesrlineNetTxBiasCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 3, 152)
)
if mibBuilder.loadTexts:
    pm10010ulhMesrlineNetTxBiasCurrentTable.setStatus("current")
_Pm10010ulhMesrlineNetTxBiasCurrentEntry_Object = MibTableRow
pm10010ulhMesrlineNetTxBiasCurrentEntry = _Pm10010ulhMesrlineNetTxBiasCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 3, 152, 1)
)
pm10010ulhMesrlineNetTxBiasCurrentEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhMesrlineNetTxBiasCurrentIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhMesrlineNetTxBiasCurrentEntry.setStatus("current")


class _Pm10010ulhMesrlineNetTxBiasCurrentIndex_Type(Integer32):
    """Custom type pm10010ulhMesrlineNetTxBiasCurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhMesrlineNetTxBiasCurrentIndex_Type.__name__ = "Integer32"
_Pm10010ulhMesrlineNetTxBiasCurrentIndex_Object = MibTableColumn
pm10010ulhMesrlineNetTxBiasCurrentIndex = _Pm10010ulhMesrlineNetTxBiasCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 3, 152, 1, 1),
    _Pm10010ulhMesrlineNetTxBiasCurrentIndex_Type()
)
pm10010ulhMesrlineNetTxBiasCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrlineNetTxBiasCurrentIndex.setStatus("current")


class _Pm10010ulhMesrlineNetTxBiasCurrentPortn_Type(Integer32):
    """Custom type pm10010ulhMesrlineNetTxBiasCurrentPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010ulhMesrlineNetTxBiasCurrentPortn_Type.__name__ = "Integer32"
_Pm10010ulhMesrlineNetTxBiasCurrentPortn_Object = MibTableColumn
pm10010ulhMesrlineNetTxBiasCurrentPortn = _Pm10010ulhMesrlineNetTxBiasCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 3, 152, 1, 2),
    _Pm10010ulhMesrlineNetTxBiasCurrentPortn_Type()
)
pm10010ulhMesrlineNetTxBiasCurrentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrlineNetTxBiasCurrentPortn.setStatus("current")
_Pm10010ulhMesrlineNetRxInputPwrTable_Object = MibTable
pm10010ulhMesrlineNetRxInputPwrTable = _Pm10010ulhMesrlineNetRxInputPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 3, 156)
)
if mibBuilder.loadTexts:
    pm10010ulhMesrlineNetRxInputPwrTable.setStatus("current")
_Pm10010ulhMesrlineNetRxInputPwrEntry_Object = MibTableRow
pm10010ulhMesrlineNetRxInputPwrEntry = _Pm10010ulhMesrlineNetRxInputPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 3, 156, 1)
)
pm10010ulhMesrlineNetRxInputPwrEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhMesrlineNetRxInputPwrIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhMesrlineNetRxInputPwrEntry.setStatus("current")


class _Pm10010ulhMesrlineNetRxInputPwrIndex_Type(Integer32):
    """Custom type pm10010ulhMesrlineNetRxInputPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhMesrlineNetRxInputPwrIndex_Type.__name__ = "Integer32"
_Pm10010ulhMesrlineNetRxInputPwrIndex_Object = MibTableColumn
pm10010ulhMesrlineNetRxInputPwrIndex = _Pm10010ulhMesrlineNetRxInputPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 3, 156, 1, 1),
    _Pm10010ulhMesrlineNetRxInputPwrIndex_Type()
)
pm10010ulhMesrlineNetRxInputPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrlineNetRxInputPwrIndex.setStatus("current")


class _Pm10010ulhMesrlineNetRxInputPwrPortn_Type(Integer32):
    """Custom type pm10010ulhMesrlineNetRxInputPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010ulhMesrlineNetRxInputPwrPortn_Type.__name__ = "Integer32"
_Pm10010ulhMesrlineNetRxInputPwrPortn_Object = MibTableColumn
pm10010ulhMesrlineNetRxInputPwrPortn = _Pm10010ulhMesrlineNetRxInputPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 3, 156, 1, 2),
    _Pm10010ulhMesrlineNetRxInputPwrPortn_Type()
)
pm10010ulhMesrlineNetRxInputPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrlineNetRxInputPwrPortn.setStatus("current")
_Pm10010ulhMesrlineResidualChromaticDispTable_Object = MibTable
pm10010ulhMesrlineResidualChromaticDispTable = _Pm10010ulhMesrlineResidualChromaticDispTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 3, 160)
)
if mibBuilder.loadTexts:
    pm10010ulhMesrlineResidualChromaticDispTable.setStatus("current")
_Pm10010ulhMesrlineResidualChromaticDispEntry_Object = MibTableRow
pm10010ulhMesrlineResidualChromaticDispEntry = _Pm10010ulhMesrlineResidualChromaticDispEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 3, 160, 1)
)
pm10010ulhMesrlineResidualChromaticDispEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhMesrlineResidualChromaticDispIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhMesrlineResidualChromaticDispEntry.setStatus("current")


class _Pm10010ulhMesrlineResidualChromaticDispIndex_Type(Integer32):
    """Custom type pm10010ulhMesrlineResidualChromaticDispIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhMesrlineResidualChromaticDispIndex_Type.__name__ = "Integer32"
_Pm10010ulhMesrlineResidualChromaticDispIndex_Object = MibTableColumn
pm10010ulhMesrlineResidualChromaticDispIndex = _Pm10010ulhMesrlineResidualChromaticDispIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 3, 160, 1, 1),
    _Pm10010ulhMesrlineResidualChromaticDispIndex_Type()
)
pm10010ulhMesrlineResidualChromaticDispIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrlineResidualChromaticDispIndex.setStatus("current")


class _Pm10010ulhMesrlineResidualChromaticDispPortn_Type(Integer32):
    """Custom type pm10010ulhMesrlineResidualChromaticDispPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010ulhMesrlineResidualChromaticDispPortn_Type.__name__ = "Integer32"
_Pm10010ulhMesrlineResidualChromaticDispPortn_Object = MibTableColumn
pm10010ulhMesrlineResidualChromaticDispPortn = _Pm10010ulhMesrlineResidualChromaticDispPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 3, 160, 1, 2),
    _Pm10010ulhMesrlineResidualChromaticDispPortn_Type()
)
pm10010ulhMesrlineResidualChromaticDispPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrlineResidualChromaticDispPortn.setStatus("current")
_Pm10010ulhMesrlineDiffGroupDelayTable_Object = MibTable
pm10010ulhMesrlineDiffGroupDelayTable = _Pm10010ulhMesrlineDiffGroupDelayTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 3, 164)
)
if mibBuilder.loadTexts:
    pm10010ulhMesrlineDiffGroupDelayTable.setStatus("current")
_Pm10010ulhMesrlineDiffGroupDelayEntry_Object = MibTableRow
pm10010ulhMesrlineDiffGroupDelayEntry = _Pm10010ulhMesrlineDiffGroupDelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 3, 164, 1)
)
pm10010ulhMesrlineDiffGroupDelayEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhMesrlineDiffGroupDelayIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhMesrlineDiffGroupDelayEntry.setStatus("current")


class _Pm10010ulhMesrlineDiffGroupDelayIndex_Type(Integer32):
    """Custom type pm10010ulhMesrlineDiffGroupDelayIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhMesrlineDiffGroupDelayIndex_Type.__name__ = "Integer32"
_Pm10010ulhMesrlineDiffGroupDelayIndex_Object = MibTableColumn
pm10010ulhMesrlineDiffGroupDelayIndex = _Pm10010ulhMesrlineDiffGroupDelayIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 3, 164, 1, 1),
    _Pm10010ulhMesrlineDiffGroupDelayIndex_Type()
)
pm10010ulhMesrlineDiffGroupDelayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrlineDiffGroupDelayIndex.setStatus("current")


class _Pm10010ulhMesrlineDiffGroupDelayPortn_Type(Integer32):
    """Custom type pm10010ulhMesrlineDiffGroupDelayPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010ulhMesrlineDiffGroupDelayPortn_Type.__name__ = "Integer32"
_Pm10010ulhMesrlineDiffGroupDelayPortn_Object = MibTableColumn
pm10010ulhMesrlineDiffGroupDelayPortn = _Pm10010ulhMesrlineDiffGroupDelayPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 3, 164, 1, 2),
    _Pm10010ulhMesrlineDiffGroupDelayPortn_Type()
)
pm10010ulhMesrlineDiffGroupDelayPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrlineDiffGroupDelayPortn.setStatus("current")
_Pm10010ulhMesrlineQFactorTable_Object = MibTable
pm10010ulhMesrlineQFactorTable = _Pm10010ulhMesrlineQFactorTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 3, 168)
)
if mibBuilder.loadTexts:
    pm10010ulhMesrlineQFactorTable.setStatus("current")
_Pm10010ulhMesrlineQFactorEntry_Object = MibTableRow
pm10010ulhMesrlineQFactorEntry = _Pm10010ulhMesrlineQFactorEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 3, 168, 1)
)
pm10010ulhMesrlineQFactorEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhMesrlineQFactorIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhMesrlineQFactorEntry.setStatus("current")


class _Pm10010ulhMesrlineQFactorIndex_Type(Integer32):
    """Custom type pm10010ulhMesrlineQFactorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhMesrlineQFactorIndex_Type.__name__ = "Integer32"
_Pm10010ulhMesrlineQFactorIndex_Object = MibTableColumn
pm10010ulhMesrlineQFactorIndex = _Pm10010ulhMesrlineQFactorIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 3, 168, 1, 1),
    _Pm10010ulhMesrlineQFactorIndex_Type()
)
pm10010ulhMesrlineQFactorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrlineQFactorIndex.setStatus("current")


class _Pm10010ulhMesrlineQFactorPortn_Type(Integer32):
    """Custom type pm10010ulhMesrlineQFactorPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010ulhMesrlineQFactorPortn_Type.__name__ = "Integer32"
_Pm10010ulhMesrlineQFactorPortn_Object = MibTableColumn
pm10010ulhMesrlineQFactorPortn = _Pm10010ulhMesrlineQFactorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 3, 168, 1, 2),
    _Pm10010ulhMesrlineQFactorPortn_Type()
)
pm10010ulhMesrlineQFactorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrlineQFactorPortn.setStatus("current")
_Pm10010ulhMesrlineCarrierFreqOffsetTable_Object = MibTable
pm10010ulhMesrlineCarrierFreqOffsetTable = _Pm10010ulhMesrlineCarrierFreqOffsetTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 3, 172)
)
if mibBuilder.loadTexts:
    pm10010ulhMesrlineCarrierFreqOffsetTable.setStatus("current")
_Pm10010ulhMesrlineCarrierFreqOffsetEntry_Object = MibTableRow
pm10010ulhMesrlineCarrierFreqOffsetEntry = _Pm10010ulhMesrlineCarrierFreqOffsetEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 3, 172, 1)
)
pm10010ulhMesrlineCarrierFreqOffsetEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhMesrlineCarrierFreqOffsetIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhMesrlineCarrierFreqOffsetEntry.setStatus("current")


class _Pm10010ulhMesrlineCarrierFreqOffsetIndex_Type(Integer32):
    """Custom type pm10010ulhMesrlineCarrierFreqOffsetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhMesrlineCarrierFreqOffsetIndex_Type.__name__ = "Integer32"
_Pm10010ulhMesrlineCarrierFreqOffsetIndex_Object = MibTableColumn
pm10010ulhMesrlineCarrierFreqOffsetIndex = _Pm10010ulhMesrlineCarrierFreqOffsetIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 3, 172, 1, 1),
    _Pm10010ulhMesrlineCarrierFreqOffsetIndex_Type()
)
pm10010ulhMesrlineCarrierFreqOffsetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrlineCarrierFreqOffsetIndex.setStatus("current")


class _Pm10010ulhMesrlineCarrierFreqOffsetPortn_Type(Integer32):
    """Custom type pm10010ulhMesrlineCarrierFreqOffsetPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010ulhMesrlineCarrierFreqOffsetPortn_Type.__name__ = "Integer32"
_Pm10010ulhMesrlineCarrierFreqOffsetPortn_Object = MibTableColumn
pm10010ulhMesrlineCarrierFreqOffsetPortn = _Pm10010ulhMesrlineCarrierFreqOffsetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 3, 172, 1, 2),
    _Pm10010ulhMesrlineCarrierFreqOffsetPortn_Type()
)
pm10010ulhMesrlineCarrierFreqOffsetPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrlineCarrierFreqOffsetPortn.setStatus("current")
_Pm10010ulhMesrlineOsnrTable_Object = MibTable
pm10010ulhMesrlineOsnrTable = _Pm10010ulhMesrlineOsnrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 3, 176)
)
if mibBuilder.loadTexts:
    pm10010ulhMesrlineOsnrTable.setStatus("current")
_Pm10010ulhMesrlineOsnrEntry_Object = MibTableRow
pm10010ulhMesrlineOsnrEntry = _Pm10010ulhMesrlineOsnrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 3, 176, 1)
)
pm10010ulhMesrlineOsnrEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhMesrlineOsnrIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhMesrlineOsnrEntry.setStatus("current")


class _Pm10010ulhMesrlineOsnrIndex_Type(Integer32):
    """Custom type pm10010ulhMesrlineOsnrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhMesrlineOsnrIndex_Type.__name__ = "Integer32"
_Pm10010ulhMesrlineOsnrIndex_Object = MibTableColumn
pm10010ulhMesrlineOsnrIndex = _Pm10010ulhMesrlineOsnrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 3, 176, 1, 1),
    _Pm10010ulhMesrlineOsnrIndex_Type()
)
pm10010ulhMesrlineOsnrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrlineOsnrIndex.setStatus("current")


class _Pm10010ulhMesrlineOsnrPortn_Type(Integer32):
    """Custom type pm10010ulhMesrlineOsnrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010ulhMesrlineOsnrPortn_Type.__name__ = "Integer32"
_Pm10010ulhMesrlineOsnrPortn_Object = MibTableColumn
pm10010ulhMesrlineOsnrPortn = _Pm10010ulhMesrlineOsnrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 3, 3, 176, 1, 2),
    _Pm10010ulhMesrlineOsnrPortn_Type()
)
pm10010ulhMesrlineOsnrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMesrlineOsnrPortn.setStatus("current")
_Pm10010ulhcounters_ObjectIdentity = ObjectIdentity
pm10010ulhcounters = _Pm10010ulhcounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4)
)
_Pm10010ulhCntOther_ObjectIdentity = ObjectIdentity
pm10010ulhCntOther = _Pm10010ulhCntOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4, 1)
)
_Pm10010ulhCntClient_ObjectIdentity = ObjectIdentity
pm10010ulhCntClient = _Pm10010ulhCntClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4, 2)
)
_Pm10010ulhCntclientInputErrorCounterTable_Object = MibTable
pm10010ulhCntclientInputErrorCounterTable = _Pm10010ulhCntclientInputErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4, 2, 112)
)
if mibBuilder.loadTexts:
    pm10010ulhCntclientInputErrorCounterTable.setStatus("current")
_Pm10010ulhCntclientInputErrorCounterEntry_Object = MibTableRow
pm10010ulhCntclientInputErrorCounterEntry = _Pm10010ulhCntclientInputErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4, 2, 112, 1)
)
pm10010ulhCntclientInputErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhCntclientInputErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhCntclientInputErrorCounterEntry.setStatus("current")


class _Pm10010ulhCntclientInputErrorCounterIndex_Type(Integer32):
    """Custom type pm10010ulhCntclientInputErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhCntclientInputErrorCounterIndex_Type.__name__ = "Integer32"
_Pm10010ulhCntclientInputErrorCounterIndex_Object = MibTableColumn
pm10010ulhCntclientInputErrorCounterIndex = _Pm10010ulhCntclientInputErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4, 2, 112, 1, 1),
    _Pm10010ulhCntclientInputErrorCounterIndex_Type()
)
pm10010ulhCntclientInputErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCntclientInputErrorCounterIndex.setStatus("current")
_Pm10010ulhCntclientInputErrorCounterValuePortn_Type = Counter32
_Pm10010ulhCntclientInputErrorCounterValuePortn_Object = MibTableColumn
pm10010ulhCntclientInputErrorCounterValuePortn = _Pm10010ulhCntclientInputErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4, 2, 112, 1, 2),
    _Pm10010ulhCntclientInputErrorCounterValuePortn_Type()
)
pm10010ulhCntclientInputErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCntclientInputErrorCounterValuePortn.setStatus("current")
_Pm10010ulhCntclientInputErrorCounterErrorPortn_Type = EkiOnOff
_Pm10010ulhCntclientInputErrorCounterErrorPortn_Object = MibTableColumn
pm10010ulhCntclientInputErrorCounterErrorPortn = _Pm10010ulhCntclientInputErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4, 2, 112, 1, 3),
    _Pm10010ulhCntclientInputErrorCounterErrorPortn_Type()
)
pm10010ulhCntclientInputErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCntclientInputErrorCounterErrorPortn.setStatus("current")
_Pm10010ulhCntclientInputErrorCounterOverloadPortn_Type = EkiOnOff
_Pm10010ulhCntclientInputErrorCounterOverloadPortn_Object = MibTableColumn
pm10010ulhCntclientInputErrorCounterOverloadPortn = _Pm10010ulhCntclientInputErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4, 2, 112, 1, 4),
    _Pm10010ulhCntclientInputErrorCounterOverloadPortn_Type()
)
pm10010ulhCntclientInputErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCntclientInputErrorCounterOverloadPortn.setStatus("current")
_Pm10010ulhCntclientCbipCounterTable_Object = MibTable
pm10010ulhCntclientCbipCounterTable = _Pm10010ulhCntclientCbipCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4, 2, 144)
)
if mibBuilder.loadTexts:
    pm10010ulhCntclientCbipCounterTable.setStatus("current")
_Pm10010ulhCntclientCbipCounterEntry_Object = MibTableRow
pm10010ulhCntclientCbipCounterEntry = _Pm10010ulhCntclientCbipCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4, 2, 144, 1)
)
pm10010ulhCntclientCbipCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhCntclientCbipCounterIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhCntclientCbipCounterEntry.setStatus("current")


class _Pm10010ulhCntclientCbipCounterIndex_Type(Integer32):
    """Custom type pm10010ulhCntclientCbipCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhCntclientCbipCounterIndex_Type.__name__ = "Integer32"
_Pm10010ulhCntclientCbipCounterIndex_Object = MibTableColumn
pm10010ulhCntclientCbipCounterIndex = _Pm10010ulhCntclientCbipCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4, 2, 144, 1, 1),
    _Pm10010ulhCntclientCbipCounterIndex_Type()
)
pm10010ulhCntclientCbipCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCntclientCbipCounterIndex.setStatus("current")
_Pm10010ulhCntclientCbipCounterValuePortn_Type = Counter32
_Pm10010ulhCntclientCbipCounterValuePortn_Object = MibTableColumn
pm10010ulhCntclientCbipCounterValuePortn = _Pm10010ulhCntclientCbipCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4, 2, 144, 1, 2),
    _Pm10010ulhCntclientCbipCounterValuePortn_Type()
)
pm10010ulhCntclientCbipCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCntclientCbipCounterValuePortn.setStatus("current")
_Pm10010ulhCntclientCbipCounterErrorPortn_Type = EkiOnOff
_Pm10010ulhCntclientCbipCounterErrorPortn_Object = MibTableColumn
pm10010ulhCntclientCbipCounterErrorPortn = _Pm10010ulhCntclientCbipCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4, 2, 144, 1, 3),
    _Pm10010ulhCntclientCbipCounterErrorPortn_Type()
)
pm10010ulhCntclientCbipCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCntclientCbipCounterErrorPortn.setStatus("current")
_Pm10010ulhCntclientCbipCounterOverloadPortn_Type = EkiOnOff
_Pm10010ulhCntclientCbipCounterOverloadPortn_Object = MibTableColumn
pm10010ulhCntclientCbipCounterOverloadPortn = _Pm10010ulhCntclientCbipCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4, 2, 144, 1, 4),
    _Pm10010ulhCntclientCbipCounterOverloadPortn_Type()
)
pm10010ulhCntclientCbipCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCntclientCbipCounterOverloadPortn.setStatus("current")
_Pm10010ulhCntLine_ObjectIdentity = ObjectIdentity
pm10010ulhCntLine = _Pm10010ulhCntLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4, 3)
)
_Pm10010ulhCntlocalLineSmBip8ErrorCounterTable_Object = MibTable
pm10010ulhCntlocalLineSmBip8ErrorCounterTable = _Pm10010ulhCntlocalLineSmBip8ErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4, 3, 192)
)
if mibBuilder.loadTexts:
    pm10010ulhCntlocalLineSmBip8ErrorCounterTable.setStatus("current")
_Pm10010ulhCntlocalLineSmBip8ErrorCounterEntry_Object = MibTableRow
pm10010ulhCntlocalLineSmBip8ErrorCounterEntry = _Pm10010ulhCntlocalLineSmBip8ErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4, 3, 192, 1)
)
pm10010ulhCntlocalLineSmBip8ErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhCntlocalLineSmBip8ErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhCntlocalLineSmBip8ErrorCounterEntry.setStatus("current")


class _Pm10010ulhCntlocalLineSmBip8ErrorCounterIndex_Type(Integer32):
    """Custom type pm10010ulhCntlocalLineSmBip8ErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhCntlocalLineSmBip8ErrorCounterIndex_Type.__name__ = "Integer32"
_Pm10010ulhCntlocalLineSmBip8ErrorCounterIndex_Object = MibTableColumn
pm10010ulhCntlocalLineSmBip8ErrorCounterIndex = _Pm10010ulhCntlocalLineSmBip8ErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4, 3, 192, 1, 1),
    _Pm10010ulhCntlocalLineSmBip8ErrorCounterIndex_Type()
)
pm10010ulhCntlocalLineSmBip8ErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCntlocalLineSmBip8ErrorCounterIndex.setStatus("current")
_Pm10010ulhCntlocalLineSmBip8ErrorCounterValuePortn_Type = Counter64
_Pm10010ulhCntlocalLineSmBip8ErrorCounterValuePortn_Object = MibTableColumn
pm10010ulhCntlocalLineSmBip8ErrorCounterValuePortn = _Pm10010ulhCntlocalLineSmBip8ErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4, 3, 192, 1, 2),
    _Pm10010ulhCntlocalLineSmBip8ErrorCounterValuePortn_Type()
)
pm10010ulhCntlocalLineSmBip8ErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCntlocalLineSmBip8ErrorCounterValuePortn.setStatus("current")
_Pm10010ulhCntlocalLineSmBip8ErrorCounterErrorPortn_Type = EkiOnOff
_Pm10010ulhCntlocalLineSmBip8ErrorCounterErrorPortn_Object = MibTableColumn
pm10010ulhCntlocalLineSmBip8ErrorCounterErrorPortn = _Pm10010ulhCntlocalLineSmBip8ErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4, 3, 192, 1, 3),
    _Pm10010ulhCntlocalLineSmBip8ErrorCounterErrorPortn_Type()
)
pm10010ulhCntlocalLineSmBip8ErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCntlocalLineSmBip8ErrorCounterErrorPortn.setStatus("current")
_Pm10010ulhCntlocalLineSmBip8ErrorCounterOverloadPortn_Type = EkiOnOff
_Pm10010ulhCntlocalLineSmBip8ErrorCounterOverloadPortn_Object = MibTableColumn
pm10010ulhCntlocalLineSmBip8ErrorCounterOverloadPortn = _Pm10010ulhCntlocalLineSmBip8ErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4, 3, 192, 1, 4),
    _Pm10010ulhCntlocalLineSmBip8ErrorCounterOverloadPortn_Type()
)
pm10010ulhCntlocalLineSmBip8ErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCntlocalLineSmBip8ErrorCounterOverloadPortn.setStatus("current")
_Pm10010ulhCntlocalLineFecCorrectedErrorsCounterTable_Object = MibTable
pm10010ulhCntlocalLineFecCorrectedErrorsCounterTable = _Pm10010ulhCntlocalLineFecCorrectedErrorsCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4, 3, 193)
)
if mibBuilder.loadTexts:
    pm10010ulhCntlocalLineFecCorrectedErrorsCounterTable.setStatus("current")
_Pm10010ulhCntlocalLineFecCorrectedErrorsCounterEntry_Object = MibTableRow
pm10010ulhCntlocalLineFecCorrectedErrorsCounterEntry = _Pm10010ulhCntlocalLineFecCorrectedErrorsCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4, 3, 193, 1)
)
pm10010ulhCntlocalLineFecCorrectedErrorsCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhCntlocalLineFecCorrectedErrorsCounterIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhCntlocalLineFecCorrectedErrorsCounterEntry.setStatus("current")


class _Pm10010ulhCntlocalLineFecCorrectedErrorsCounterIndex_Type(Integer32):
    """Custom type pm10010ulhCntlocalLineFecCorrectedErrorsCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhCntlocalLineFecCorrectedErrorsCounterIndex_Type.__name__ = "Integer32"
_Pm10010ulhCntlocalLineFecCorrectedErrorsCounterIndex_Object = MibTableColumn
pm10010ulhCntlocalLineFecCorrectedErrorsCounterIndex = _Pm10010ulhCntlocalLineFecCorrectedErrorsCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4, 3, 193, 1, 1),
    _Pm10010ulhCntlocalLineFecCorrectedErrorsCounterIndex_Type()
)
pm10010ulhCntlocalLineFecCorrectedErrorsCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCntlocalLineFecCorrectedErrorsCounterIndex.setStatus("current")
_Pm10010ulhCntlocalLineFecCorrectedErrorsCounterValuePortn_Type = Counter64
_Pm10010ulhCntlocalLineFecCorrectedErrorsCounterValuePortn_Object = MibTableColumn
pm10010ulhCntlocalLineFecCorrectedErrorsCounterValuePortn = _Pm10010ulhCntlocalLineFecCorrectedErrorsCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4, 3, 193, 1, 2),
    _Pm10010ulhCntlocalLineFecCorrectedErrorsCounterValuePortn_Type()
)
pm10010ulhCntlocalLineFecCorrectedErrorsCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCntlocalLineFecCorrectedErrorsCounterValuePortn.setStatus("current")
_Pm10010ulhCntlocalLineFecCorrectedErrorsCounterErrorPortn_Type = EkiOnOff
_Pm10010ulhCntlocalLineFecCorrectedErrorsCounterErrorPortn_Object = MibTableColumn
pm10010ulhCntlocalLineFecCorrectedErrorsCounterErrorPortn = _Pm10010ulhCntlocalLineFecCorrectedErrorsCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4, 3, 193, 1, 3),
    _Pm10010ulhCntlocalLineFecCorrectedErrorsCounterErrorPortn_Type()
)
pm10010ulhCntlocalLineFecCorrectedErrorsCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCntlocalLineFecCorrectedErrorsCounterErrorPortn.setStatus("current")
_Pm10010ulhCntlocalLineFecCorrectedErrorsCounterOverloadPortn_Type = EkiOnOff
_Pm10010ulhCntlocalLineFecCorrectedErrorsCounterOverloadPortn_Object = MibTableColumn
pm10010ulhCntlocalLineFecCorrectedErrorsCounterOverloadPortn = _Pm10010ulhCntlocalLineFecCorrectedErrorsCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4, 3, 193, 1, 4),
    _Pm10010ulhCntlocalLineFecCorrectedErrorsCounterOverloadPortn_Type()
)
pm10010ulhCntlocalLineFecCorrectedErrorsCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCntlocalLineFecCorrectedErrorsCounterOverloadPortn.setStatus("current")
_Pm10010ulhCntremoteLineSmBip8ErrorCounterTable_Object = MibTable
pm10010ulhCntremoteLineSmBip8ErrorCounterTable = _Pm10010ulhCntremoteLineSmBip8ErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4, 3, 194)
)
if mibBuilder.loadTexts:
    pm10010ulhCntremoteLineSmBip8ErrorCounterTable.setStatus("current")
_Pm10010ulhCntremoteLineSmBip8ErrorCounterEntry_Object = MibTableRow
pm10010ulhCntremoteLineSmBip8ErrorCounterEntry = _Pm10010ulhCntremoteLineSmBip8ErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4, 3, 194, 1)
)
pm10010ulhCntremoteLineSmBip8ErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhCntremoteLineSmBip8ErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhCntremoteLineSmBip8ErrorCounterEntry.setStatus("current")


class _Pm10010ulhCntremoteLineSmBip8ErrorCounterIndex_Type(Integer32):
    """Custom type pm10010ulhCntremoteLineSmBip8ErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhCntremoteLineSmBip8ErrorCounterIndex_Type.__name__ = "Integer32"
_Pm10010ulhCntremoteLineSmBip8ErrorCounterIndex_Object = MibTableColumn
pm10010ulhCntremoteLineSmBip8ErrorCounterIndex = _Pm10010ulhCntremoteLineSmBip8ErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4, 3, 194, 1, 1),
    _Pm10010ulhCntremoteLineSmBip8ErrorCounterIndex_Type()
)
pm10010ulhCntremoteLineSmBip8ErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCntremoteLineSmBip8ErrorCounterIndex.setStatus("current")
_Pm10010ulhCntremoteLineSmBip8ErrorCounterValuePortn_Type = Counter64
_Pm10010ulhCntremoteLineSmBip8ErrorCounterValuePortn_Object = MibTableColumn
pm10010ulhCntremoteLineSmBip8ErrorCounterValuePortn = _Pm10010ulhCntremoteLineSmBip8ErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4, 3, 194, 1, 2),
    _Pm10010ulhCntremoteLineSmBip8ErrorCounterValuePortn_Type()
)
pm10010ulhCntremoteLineSmBip8ErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCntremoteLineSmBip8ErrorCounterValuePortn.setStatus("current")
_Pm10010ulhCntremoteLineSmBip8ErrorCounterErrorPortn_Type = EkiOnOff
_Pm10010ulhCntremoteLineSmBip8ErrorCounterErrorPortn_Object = MibTableColumn
pm10010ulhCntremoteLineSmBip8ErrorCounterErrorPortn = _Pm10010ulhCntremoteLineSmBip8ErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4, 3, 194, 1, 3),
    _Pm10010ulhCntremoteLineSmBip8ErrorCounterErrorPortn_Type()
)
pm10010ulhCntremoteLineSmBip8ErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCntremoteLineSmBip8ErrorCounterErrorPortn.setStatus("current")
_Pm10010ulhCntremoteLineSmBip8ErrorCounterOverloadPortn_Type = EkiOnOff
_Pm10010ulhCntremoteLineSmBip8ErrorCounterOverloadPortn_Object = MibTableColumn
pm10010ulhCntremoteLineSmBip8ErrorCounterOverloadPortn = _Pm10010ulhCntremoteLineSmBip8ErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4, 3, 194, 1, 4),
    _Pm10010ulhCntremoteLineSmBip8ErrorCounterOverloadPortn_Type()
)
pm10010ulhCntremoteLineSmBip8ErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCntremoteLineSmBip8ErrorCounterOverloadPortn.setStatus("current")
_Pm10010ulhCntlineDfrmTimCntTable_Object = MibTable
pm10010ulhCntlineDfrmTimCntTable = _Pm10010ulhCntlineDfrmTimCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4, 3, 195)
)
if mibBuilder.loadTexts:
    pm10010ulhCntlineDfrmTimCntTable.setStatus("current")
_Pm10010ulhCntlineDfrmTimCntEntry_Object = MibTableRow
pm10010ulhCntlineDfrmTimCntEntry = _Pm10010ulhCntlineDfrmTimCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4, 3, 195, 1)
)
pm10010ulhCntlineDfrmTimCntEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhCntlineDfrmTimCntIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhCntlineDfrmTimCntEntry.setStatus("current")


class _Pm10010ulhCntlineDfrmTimCntIndex_Type(Integer32):
    """Custom type pm10010ulhCntlineDfrmTimCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhCntlineDfrmTimCntIndex_Type.__name__ = "Integer32"
_Pm10010ulhCntlineDfrmTimCntIndex_Object = MibTableColumn
pm10010ulhCntlineDfrmTimCntIndex = _Pm10010ulhCntlineDfrmTimCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4, 3, 195, 1, 1),
    _Pm10010ulhCntlineDfrmTimCntIndex_Type()
)
pm10010ulhCntlineDfrmTimCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCntlineDfrmTimCntIndex.setStatus("current")
_Pm10010ulhCntlineDfrmTimCntValuePortn_Type = Counter64
_Pm10010ulhCntlineDfrmTimCntValuePortn_Object = MibTableColumn
pm10010ulhCntlineDfrmTimCntValuePortn = _Pm10010ulhCntlineDfrmTimCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4, 3, 195, 1, 2),
    _Pm10010ulhCntlineDfrmTimCntValuePortn_Type()
)
pm10010ulhCntlineDfrmTimCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCntlineDfrmTimCntValuePortn.setStatus("current")
_Pm10010ulhCntlineDfrmTimCntErrorPortn_Type = EkiOnOff
_Pm10010ulhCntlineDfrmTimCntErrorPortn_Object = MibTableColumn
pm10010ulhCntlineDfrmTimCntErrorPortn = _Pm10010ulhCntlineDfrmTimCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4, 3, 195, 1, 3),
    _Pm10010ulhCntlineDfrmTimCntErrorPortn_Type()
)
pm10010ulhCntlineDfrmTimCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCntlineDfrmTimCntErrorPortn.setStatus("current")
_Pm10010ulhCntlineDfrmTimCntOverloadPortn_Type = EkiOnOff
_Pm10010ulhCntlineDfrmTimCntOverloadPortn_Object = MibTableColumn
pm10010ulhCntlineDfrmTimCntOverloadPortn = _Pm10010ulhCntlineDfrmTimCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4, 3, 195, 1, 4),
    _Pm10010ulhCntlineDfrmTimCntOverloadPortn_Type()
)
pm10010ulhCntlineDfrmTimCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCntlineDfrmTimCntOverloadPortn.setStatus("current")
_Pm10010ulhCntlocalLineTrscvPreSdFecErrorCounterTable_Object = MibTable
pm10010ulhCntlocalLineTrscvPreSdFecErrorCounterTable = _Pm10010ulhCntlocalLineTrscvPreSdFecErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4, 3, 196)
)
if mibBuilder.loadTexts:
    pm10010ulhCntlocalLineTrscvPreSdFecErrorCounterTable.setStatus("current")
_Pm10010ulhCntlocalLineTrscvPreSdFecErrorCounterEntry_Object = MibTableRow
pm10010ulhCntlocalLineTrscvPreSdFecErrorCounterEntry = _Pm10010ulhCntlocalLineTrscvPreSdFecErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4, 3, 196, 1)
)
pm10010ulhCntlocalLineTrscvPreSdFecErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhCntlocalLineTrscvPreSdFecErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhCntlocalLineTrscvPreSdFecErrorCounterEntry.setStatus("current")


class _Pm10010ulhCntlocalLineTrscvPreSdFecErrorCounterIndex_Type(Integer32):
    """Custom type pm10010ulhCntlocalLineTrscvPreSdFecErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhCntlocalLineTrscvPreSdFecErrorCounterIndex_Type.__name__ = "Integer32"
_Pm10010ulhCntlocalLineTrscvPreSdFecErrorCounterIndex_Object = MibTableColumn
pm10010ulhCntlocalLineTrscvPreSdFecErrorCounterIndex = _Pm10010ulhCntlocalLineTrscvPreSdFecErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4, 3, 196, 1, 1),
    _Pm10010ulhCntlocalLineTrscvPreSdFecErrorCounterIndex_Type()
)
pm10010ulhCntlocalLineTrscvPreSdFecErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCntlocalLineTrscvPreSdFecErrorCounterIndex.setStatus("current")
_Pm10010ulhCntlocalLineTrscvPreSdFecErrorCounterValuePortn_Type = Counter64
_Pm10010ulhCntlocalLineTrscvPreSdFecErrorCounterValuePortn_Object = MibTableColumn
pm10010ulhCntlocalLineTrscvPreSdFecErrorCounterValuePortn = _Pm10010ulhCntlocalLineTrscvPreSdFecErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4, 3, 196, 1, 2),
    _Pm10010ulhCntlocalLineTrscvPreSdFecErrorCounterValuePortn_Type()
)
pm10010ulhCntlocalLineTrscvPreSdFecErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCntlocalLineTrscvPreSdFecErrorCounterValuePortn.setStatus("current")
_Pm10010ulhCntlocalLineTrscvPreSdFecErrorCounterErrorPortn_Type = EkiOnOff
_Pm10010ulhCntlocalLineTrscvPreSdFecErrorCounterErrorPortn_Object = MibTableColumn
pm10010ulhCntlocalLineTrscvPreSdFecErrorCounterErrorPortn = _Pm10010ulhCntlocalLineTrscvPreSdFecErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4, 3, 196, 1, 3),
    _Pm10010ulhCntlocalLineTrscvPreSdFecErrorCounterErrorPortn_Type()
)
pm10010ulhCntlocalLineTrscvPreSdFecErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCntlocalLineTrscvPreSdFecErrorCounterErrorPortn.setStatus("current")
_Pm10010ulhCntlocalLineTrscvPreSdFecErrorCounterOverloadPortn_Type = EkiOnOff
_Pm10010ulhCntlocalLineTrscvPreSdFecErrorCounterOverloadPortn_Object = MibTableColumn
pm10010ulhCntlocalLineTrscvPreSdFecErrorCounterOverloadPortn = _Pm10010ulhCntlocalLineTrscvPreSdFecErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4, 3, 196, 1, 4),
    _Pm10010ulhCntlocalLineTrscvPreSdFecErrorCounterOverloadPortn_Type()
)
pm10010ulhCntlocalLineTrscvPreSdFecErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCntlocalLineTrscvPreSdFecErrorCounterOverloadPortn.setStatus("current")
_Pm10010ulhCntlocalLineTrscvUncorrectedSdFecErrorCounterTable_Object = MibTable
pm10010ulhCntlocalLineTrscvUncorrectedSdFecErrorCounterTable = _Pm10010ulhCntlocalLineTrscvUncorrectedSdFecErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4, 3, 197)
)
if mibBuilder.loadTexts:
    pm10010ulhCntlocalLineTrscvUncorrectedSdFecErrorCounterTable.setStatus("current")
_Pm10010ulhCntlocalLineTrscvUncorrectedSdFecErrorCounterEntry_Object = MibTableRow
pm10010ulhCntlocalLineTrscvUncorrectedSdFecErrorCounterEntry = _Pm10010ulhCntlocalLineTrscvUncorrectedSdFecErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4, 3, 197, 1)
)
pm10010ulhCntlocalLineTrscvUncorrectedSdFecErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhCntlocalLineTrscvUncorrectedSdFecErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhCntlocalLineTrscvUncorrectedSdFecErrorCounterEntry.setStatus("current")


class _Pm10010ulhCntlocalLineTrscvUncorrectedSdFecErrorCounterIndex_Type(Integer32):
    """Custom type pm10010ulhCntlocalLineTrscvUncorrectedSdFecErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhCntlocalLineTrscvUncorrectedSdFecErrorCounterIndex_Type.__name__ = "Integer32"
_Pm10010ulhCntlocalLineTrscvUncorrectedSdFecErrorCounterIndex_Object = MibTableColumn
pm10010ulhCntlocalLineTrscvUncorrectedSdFecErrorCounterIndex = _Pm10010ulhCntlocalLineTrscvUncorrectedSdFecErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4, 3, 197, 1, 1),
    _Pm10010ulhCntlocalLineTrscvUncorrectedSdFecErrorCounterIndex_Type()
)
pm10010ulhCntlocalLineTrscvUncorrectedSdFecErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCntlocalLineTrscvUncorrectedSdFecErrorCounterIndex.setStatus("current")
_Pm10010ulhCntlocalLineTrscvUncorrectedSdFecErrorCounterValuePortn_Type = Counter64
_Pm10010ulhCntlocalLineTrscvUncorrectedSdFecErrorCounterValuePortn_Object = MibTableColumn
pm10010ulhCntlocalLineTrscvUncorrectedSdFecErrorCounterValuePortn = _Pm10010ulhCntlocalLineTrscvUncorrectedSdFecErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4, 3, 197, 1, 2),
    _Pm10010ulhCntlocalLineTrscvUncorrectedSdFecErrorCounterValuePortn_Type()
)
pm10010ulhCntlocalLineTrscvUncorrectedSdFecErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCntlocalLineTrscvUncorrectedSdFecErrorCounterValuePortn.setStatus("current")
_Pm10010ulhCntlocalLineTrscvUncorrectedSdFecErrorCounterErrorPortn_Type = EkiOnOff
_Pm10010ulhCntlocalLineTrscvUncorrectedSdFecErrorCounterErrorPortn_Object = MibTableColumn
pm10010ulhCntlocalLineTrscvUncorrectedSdFecErrorCounterErrorPortn = _Pm10010ulhCntlocalLineTrscvUncorrectedSdFecErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4, 3, 197, 1, 3),
    _Pm10010ulhCntlocalLineTrscvUncorrectedSdFecErrorCounterErrorPortn_Type()
)
pm10010ulhCntlocalLineTrscvUncorrectedSdFecErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCntlocalLineTrscvUncorrectedSdFecErrorCounterErrorPortn.setStatus("current")
_Pm10010ulhCntlocalLineTrscvUncorrectedSdFecErrorCounterOverloadPortn_Type = EkiOnOff
_Pm10010ulhCntlocalLineTrscvUncorrectedSdFecErrorCounterOverloadPortn_Object = MibTableColumn
pm10010ulhCntlocalLineTrscvUncorrectedSdFecErrorCounterOverloadPortn = _Pm10010ulhCntlocalLineTrscvUncorrectedSdFecErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4, 3, 197, 1, 4),
    _Pm10010ulhCntlocalLineTrscvUncorrectedSdFecErrorCounterOverloadPortn_Type()
)
pm10010ulhCntlocalLineTrscvUncorrectedSdFecErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCntlocalLineTrscvUncorrectedSdFecErrorCounterOverloadPortn.setStatus("current")
_Pm10010ulhCntlocalLineTrscvPreSdFecBitCounterTable_Object = MibTable
pm10010ulhCntlocalLineTrscvPreSdFecBitCounterTable = _Pm10010ulhCntlocalLineTrscvPreSdFecBitCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4, 3, 198)
)
if mibBuilder.loadTexts:
    pm10010ulhCntlocalLineTrscvPreSdFecBitCounterTable.setStatus("current")
_Pm10010ulhCntlocalLineTrscvPreSdFecBitCounterEntry_Object = MibTableRow
pm10010ulhCntlocalLineTrscvPreSdFecBitCounterEntry = _Pm10010ulhCntlocalLineTrscvPreSdFecBitCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4, 3, 198, 1)
)
pm10010ulhCntlocalLineTrscvPreSdFecBitCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhCntlocalLineTrscvPreSdFecBitCounterIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhCntlocalLineTrscvPreSdFecBitCounterEntry.setStatus("current")


class _Pm10010ulhCntlocalLineTrscvPreSdFecBitCounterIndex_Type(Integer32):
    """Custom type pm10010ulhCntlocalLineTrscvPreSdFecBitCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhCntlocalLineTrscvPreSdFecBitCounterIndex_Type.__name__ = "Integer32"
_Pm10010ulhCntlocalLineTrscvPreSdFecBitCounterIndex_Object = MibTableColumn
pm10010ulhCntlocalLineTrscvPreSdFecBitCounterIndex = _Pm10010ulhCntlocalLineTrscvPreSdFecBitCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4, 3, 198, 1, 1),
    _Pm10010ulhCntlocalLineTrscvPreSdFecBitCounterIndex_Type()
)
pm10010ulhCntlocalLineTrscvPreSdFecBitCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCntlocalLineTrscvPreSdFecBitCounterIndex.setStatus("current")
_Pm10010ulhCntlocalLineTrscvPreSdFecBitCounterValuePortn_Type = Counter64
_Pm10010ulhCntlocalLineTrscvPreSdFecBitCounterValuePortn_Object = MibTableColumn
pm10010ulhCntlocalLineTrscvPreSdFecBitCounterValuePortn = _Pm10010ulhCntlocalLineTrscvPreSdFecBitCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4, 3, 198, 1, 2),
    _Pm10010ulhCntlocalLineTrscvPreSdFecBitCounterValuePortn_Type()
)
pm10010ulhCntlocalLineTrscvPreSdFecBitCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCntlocalLineTrscvPreSdFecBitCounterValuePortn.setStatus("current")
_Pm10010ulhCntlocalLineTrscvPreSdFecBitCounterErrorPortn_Type = EkiOnOff
_Pm10010ulhCntlocalLineTrscvPreSdFecBitCounterErrorPortn_Object = MibTableColumn
pm10010ulhCntlocalLineTrscvPreSdFecBitCounterErrorPortn = _Pm10010ulhCntlocalLineTrscvPreSdFecBitCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4, 3, 198, 1, 3),
    _Pm10010ulhCntlocalLineTrscvPreSdFecBitCounterErrorPortn_Type()
)
pm10010ulhCntlocalLineTrscvPreSdFecBitCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCntlocalLineTrscvPreSdFecBitCounterErrorPortn.setStatus("current")
_Pm10010ulhCntlocalLineTrscvPreSdFecBitCounterOverloadPortn_Type = EkiOnOff
_Pm10010ulhCntlocalLineTrscvPreSdFecBitCounterOverloadPortn_Object = MibTableColumn
pm10010ulhCntlocalLineTrscvPreSdFecBitCounterOverloadPortn = _Pm10010ulhCntlocalLineTrscvPreSdFecBitCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4, 3, 198, 1, 4),
    _Pm10010ulhCntlocalLineTrscvPreSdFecBitCounterOverloadPortn_Type()
)
pm10010ulhCntlocalLineTrscvPreSdFecBitCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCntlocalLineTrscvPreSdFecBitCounterOverloadPortn.setStatus("current")
_Pm10010ulhCntlocalLineTrscvUncorrectedSdFecBitCounterTable_Object = MibTable
pm10010ulhCntlocalLineTrscvUncorrectedSdFecBitCounterTable = _Pm10010ulhCntlocalLineTrscvUncorrectedSdFecBitCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4, 3, 199)
)
if mibBuilder.loadTexts:
    pm10010ulhCntlocalLineTrscvUncorrectedSdFecBitCounterTable.setStatus("current")
_Pm10010ulhCntlocalLineTrscvUncorrectedSdFecBitCounterEntry_Object = MibTableRow
pm10010ulhCntlocalLineTrscvUncorrectedSdFecBitCounterEntry = _Pm10010ulhCntlocalLineTrscvUncorrectedSdFecBitCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4, 3, 199, 1)
)
pm10010ulhCntlocalLineTrscvUncorrectedSdFecBitCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhCntlocalLineTrscvUncorrectedSdFecBitCounterIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhCntlocalLineTrscvUncorrectedSdFecBitCounterEntry.setStatus("current")


class _Pm10010ulhCntlocalLineTrscvUncorrectedSdFecBitCounterIndex_Type(Integer32):
    """Custom type pm10010ulhCntlocalLineTrscvUncorrectedSdFecBitCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhCntlocalLineTrscvUncorrectedSdFecBitCounterIndex_Type.__name__ = "Integer32"
_Pm10010ulhCntlocalLineTrscvUncorrectedSdFecBitCounterIndex_Object = MibTableColumn
pm10010ulhCntlocalLineTrscvUncorrectedSdFecBitCounterIndex = _Pm10010ulhCntlocalLineTrscvUncorrectedSdFecBitCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4, 3, 199, 1, 1),
    _Pm10010ulhCntlocalLineTrscvUncorrectedSdFecBitCounterIndex_Type()
)
pm10010ulhCntlocalLineTrscvUncorrectedSdFecBitCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCntlocalLineTrscvUncorrectedSdFecBitCounterIndex.setStatus("current")
_Pm10010ulhCntlocalLineTrscvUncorrectedSdFecBitCounterValuePortn_Type = Counter64
_Pm10010ulhCntlocalLineTrscvUncorrectedSdFecBitCounterValuePortn_Object = MibTableColumn
pm10010ulhCntlocalLineTrscvUncorrectedSdFecBitCounterValuePortn = _Pm10010ulhCntlocalLineTrscvUncorrectedSdFecBitCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4, 3, 199, 1, 2),
    _Pm10010ulhCntlocalLineTrscvUncorrectedSdFecBitCounterValuePortn_Type()
)
pm10010ulhCntlocalLineTrscvUncorrectedSdFecBitCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCntlocalLineTrscvUncorrectedSdFecBitCounterValuePortn.setStatus("current")
_Pm10010ulhCntlocalLineTrscvUncorrectedSdFecBitCounterErrorPortn_Type = EkiOnOff
_Pm10010ulhCntlocalLineTrscvUncorrectedSdFecBitCounterErrorPortn_Object = MibTableColumn
pm10010ulhCntlocalLineTrscvUncorrectedSdFecBitCounterErrorPortn = _Pm10010ulhCntlocalLineTrscvUncorrectedSdFecBitCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4, 3, 199, 1, 3),
    _Pm10010ulhCntlocalLineTrscvUncorrectedSdFecBitCounterErrorPortn_Type()
)
pm10010ulhCntlocalLineTrscvUncorrectedSdFecBitCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCntlocalLineTrscvUncorrectedSdFecBitCounterErrorPortn.setStatus("current")
_Pm10010ulhCntlocalLineTrscvUncorrectedSdFecBitCounterOverloadPortn_Type = EkiOnOff
_Pm10010ulhCntlocalLineTrscvUncorrectedSdFecBitCounterOverloadPortn_Object = MibTableColumn
pm10010ulhCntlocalLineTrscvUncorrectedSdFecBitCounterOverloadPortn = _Pm10010ulhCntlocalLineTrscvUncorrectedSdFecBitCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 4, 3, 199, 1, 4),
    _Pm10010ulhCntlocalLineTrscvUncorrectedSdFecBitCounterOverloadPortn_Type()
)
pm10010ulhCntlocalLineTrscvUncorrectedSdFecBitCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCntlocalLineTrscvUncorrectedSdFecBitCounterOverloadPortn.setStatus("current")
_Pm10010ulhcontrolsWrite_ObjectIdentity = ObjectIdentity
pm10010ulhcontrolsWrite = _Pm10010ulhcontrolsWrite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6)
)
_Pm10010ulhCtrlOther_ObjectIdentity = ObjectIdentity
pm10010ulhCtrlOther = _Pm10010ulhCtrlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 1)
)
_Pm10010ulhCtrlconfMgnt1_ObjectIdentity = ObjectIdentity
pm10010ulhCtrlconfMgnt1 = _Pm10010ulhCtrlconfMgnt1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 1, 1)
)
_Pm10010ulhCtrlConf1Load1_Type = EkiOnOff
_Pm10010ulhCtrlConf1Load1_Object = MibScalar
pm10010ulhCtrlConf1Load1 = _Pm10010ulhCtrlConf1Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 1, 1, 1),
    _Pm10010ulhCtrlConf1Load1_Type()
)
pm10010ulhCtrlConf1Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010ulhCtrlConf1Load1.setStatus("current")
_Pm10010ulhCtrlConf2Load1_Type = EkiOnOff
_Pm10010ulhCtrlConf2Load1_Object = MibScalar
pm10010ulhCtrlConf2Load1 = _Pm10010ulhCtrlConf2Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 1, 1, 2),
    _Pm10010ulhCtrlConf2Load1_Type()
)
pm10010ulhCtrlConf2Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010ulhCtrlConf2Load1.setStatus("current")
_Pm10010ulhCtrlConf2Flash1_Type = EkiOnOff
_Pm10010ulhCtrlConf2Flash1_Object = MibScalar
pm10010ulhCtrlConf2Flash1 = _Pm10010ulhCtrlConf2Flash1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 1, 1, 10),
    _Pm10010ulhCtrlConf2Flash1_Type()
)
pm10010ulhCtrlConf2Flash1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010ulhCtrlConf2Flash1.setStatus("current")
_Pm10010ulhCtrlConf2Clear1_Type = EkiOnOff
_Pm10010ulhCtrlConf2Clear1_Object = MibScalar
pm10010ulhCtrlConf2Clear1 = _Pm10010ulhCtrlConf2Clear1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 1, 1, 14),
    _Pm10010ulhCtrlConf2Clear1_Type()
)
pm10010ulhCtrlConf2Clear1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010ulhCtrlConf2Clear1.setStatus("current")
_Pm10010ulhCtrlsynth4_ObjectIdentity = ObjectIdentity
pm10010ulhCtrlsynth4 = _Pm10010ulhCtrlsynth4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 1, 4)
)
_Pm10010ulhCtrlCorrelatOn_Type = EkiOnOff
_Pm10010ulhCtrlCorrelatOn_Object = MibScalar
pm10010ulhCtrlCorrelatOn = _Pm10010ulhCtrlCorrelatOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 1, 4, 1),
    _Pm10010ulhCtrlCorrelatOn_Type()
)
pm10010ulhCtrlCorrelatOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010ulhCtrlCorrelatOn.setStatus("current")
_Pm10010ulhCtrlCorrelatOff_Type = EkiOnOff
_Pm10010ulhCtrlCorrelatOff_Object = MibScalar
pm10010ulhCtrlCorrelatOff = _Pm10010ulhCtrlCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 1, 4, 2),
    _Pm10010ulhCtrlCorrelatOff_Type()
)
pm10010ulhCtrlCorrelatOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010ulhCtrlCorrelatOff.setStatus("current")
_Pm10010ulhCtrlswMgnt_ObjectIdentity = ObjectIdentity
pm10010ulhCtrlswMgnt = _Pm10010ulhCtrlswMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 1, 5)
)
_Pm10010ulhCtrlColdReset_Type = EkiOnOff
_Pm10010ulhCtrlColdReset_Object = MibScalar
pm10010ulhCtrlColdReset = _Pm10010ulhCtrlColdReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 1, 5, 2),
    _Pm10010ulhCtrlColdReset_Type()
)
pm10010ulhCtrlColdReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010ulhCtrlColdReset.setStatus("current")
_Pm10010ulhCtrlWarmReset_Type = EkiOnOff
_Pm10010ulhCtrlWarmReset_Object = MibScalar
pm10010ulhCtrlWarmReset = _Pm10010ulhCtrlWarmReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 1, 5, 3),
    _Pm10010ulhCtrlWarmReset_Type()
)
pm10010ulhCtrlWarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010ulhCtrlWarmReset.setStatus("current")
_Pm10010ulhCtrlLoadSwBank1_Type = EkiOnOff
_Pm10010ulhCtrlLoadSwBank1_Object = MibScalar
pm10010ulhCtrlLoadSwBank1 = _Pm10010ulhCtrlLoadSwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 1, 5, 5),
    _Pm10010ulhCtrlLoadSwBank1_Type()
)
pm10010ulhCtrlLoadSwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010ulhCtrlLoadSwBank1.setStatus("current")
_Pm10010ulhCtrlLoadSwBank2_Type = EkiOnOff
_Pm10010ulhCtrlLoadSwBank2_Object = MibScalar
pm10010ulhCtrlLoadSwBank2 = _Pm10010ulhCtrlLoadSwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 1, 5, 6),
    _Pm10010ulhCtrlLoadSwBank2_Type()
)
pm10010ulhCtrlLoadSwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010ulhCtrlLoadSwBank2.setStatus("current")
_Pm10010ulhCtrlgwMgnt_ObjectIdentity = ObjectIdentity
pm10010ulhCtrlgwMgnt = _Pm10010ulhCtrlgwMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 1, 6)
)
_Pm10010ulhCtrlCurrentGwReset_Type = EkiOnOff
_Pm10010ulhCtrlCurrentGwReset_Object = MibScalar
pm10010ulhCtrlCurrentGwReset = _Pm10010ulhCtrlCurrentGwReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 1, 6, 1),
    _Pm10010ulhCtrlCurrentGwReset_Type()
)
pm10010ulhCtrlCurrentGwReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010ulhCtrlCurrentGwReset.setStatus("current")
_Pm10010ulhCtrlLoadGwBank1_Type = EkiOnOff
_Pm10010ulhCtrlLoadGwBank1_Object = MibScalar
pm10010ulhCtrlLoadGwBank1 = _Pm10010ulhCtrlLoadGwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 1, 6, 5),
    _Pm10010ulhCtrlLoadGwBank1_Type()
)
pm10010ulhCtrlLoadGwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010ulhCtrlLoadGwBank1.setStatus("current")
_Pm10010ulhCtrlLoadGwBank2_Type = EkiOnOff
_Pm10010ulhCtrlLoadGwBank2_Object = MibScalar
pm10010ulhCtrlLoadGwBank2 = _Pm10010ulhCtrlLoadGwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 1, 6, 6),
    _Pm10010ulhCtrlLoadGwBank2_Type()
)
pm10010ulhCtrlLoadGwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010ulhCtrlLoadGwBank2.setStatus("current")
_Pm10010ulhCtrlLoadGwBank3_Type = EkiOnOff
_Pm10010ulhCtrlLoadGwBank3_Object = MibScalar
pm10010ulhCtrlLoadGwBank3 = _Pm10010ulhCtrlLoadGwBank3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 1, 6, 7),
    _Pm10010ulhCtrlLoadGwBank3_Type()
)
pm10010ulhCtrlLoadGwBank3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010ulhCtrlLoadGwBank3.setStatus("current")
_Pm10010ulhCtrlLoadGwBank4_Type = EkiOnOff
_Pm10010ulhCtrlLoadGwBank4_Object = MibScalar
pm10010ulhCtrlLoadGwBank4 = _Pm10010ulhCtrlLoadGwBank4_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 1, 6, 8),
    _Pm10010ulhCtrlLoadGwBank4_Type()
)
pm10010ulhCtrlLoadGwBank4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010ulhCtrlLoadGwBank4.setStatus("current")
_Pm10010ulhCtrlledTest_ObjectIdentity = ObjectIdentity
pm10010ulhCtrlledTest = _Pm10010ulhCtrlledTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 1, 192)
)
_Pm10010ulhCtrlGreenLed_Type = EkiOnOff
_Pm10010ulhCtrlGreenLed_Object = MibScalar
pm10010ulhCtrlGreenLed = _Pm10010ulhCtrlGreenLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 1, 192, 1),
    _Pm10010ulhCtrlGreenLed_Type()
)
pm10010ulhCtrlGreenLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010ulhCtrlGreenLed.setStatus("current")
_Pm10010ulhCtrlRedLed_Type = EkiOnOff
_Pm10010ulhCtrlRedLed_Object = MibScalar
pm10010ulhCtrlRedLed = _Pm10010ulhCtrlRedLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 1, 192, 2),
    _Pm10010ulhCtrlRedLed_Type()
)
pm10010ulhCtrlRedLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010ulhCtrlRedLed.setStatus("current")
_Pm10010ulhCtrlLedOff_Type = EkiOnOff
_Pm10010ulhCtrlLedOff_Object = MibScalar
pm10010ulhCtrlLedOff = _Pm10010ulhCtrlLedOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 1, 192, 3),
    _Pm10010ulhCtrlLedOff_Type()
)
pm10010ulhCtrlLedOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010ulhCtrlLedOff.setStatus("current")
_Pm10010ulhCtrlinitSwitchMarvell_ObjectIdentity = ObjectIdentity
pm10010ulhCtrlinitSwitchMarvell = _Pm10010ulhCtrlinitSwitchMarvell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 1, 201)
)
_Pm10010ulhCtrlInitSwitchMarvell_Type = EkiOnOff
_Pm10010ulhCtrlInitSwitchMarvell_Object = MibScalar
pm10010ulhCtrlInitSwitchMarvell = _Pm10010ulhCtrlInitSwitchMarvell_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 1, 201, 1),
    _Pm10010ulhCtrlInitSwitchMarvell_Type()
)
pm10010ulhCtrlInitSwitchMarvell.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010ulhCtrlInitSwitchMarvell.setStatus("current")
_Pm10010ulhCtrlresetCount_ObjectIdentity = ObjectIdentity
pm10010ulhCtrlresetCount = _Pm10010ulhCtrlresetCount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 1, 259)
)
_Pm10010ulhCtrlResetcount_Type = EkiOnOff
_Pm10010ulhCtrlResetcount_Object = MibScalar
pm10010ulhCtrlResetcount = _Pm10010ulhCtrlResetcount_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 1, 259, 1),
    _Pm10010ulhCtrlResetcount_Type()
)
pm10010ulhCtrlResetcount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010ulhCtrlResetcount.setStatus("current")
_Pm10010ulhCtrlresetRmon_ObjectIdentity = ObjectIdentity
pm10010ulhCtrlresetRmon = _Pm10010ulhCtrlresetRmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 1, 260)
)
_Pm10010ulhCtrlResetrmon_Type = EkiOnOff
_Pm10010ulhCtrlResetrmon_Object = MibScalar
pm10010ulhCtrlResetrmon = _Pm10010ulhCtrlResetrmon_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 1, 260, 1),
    _Pm10010ulhCtrlResetrmon_Type()
)
pm10010ulhCtrlResetrmon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010ulhCtrlResetrmon.setStatus("current")
_Pm10010ulhCtrlresetMeasurements_ObjectIdentity = ObjectIdentity
pm10010ulhCtrlresetMeasurements = _Pm10010ulhCtrlresetMeasurements_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 1, 261)
)
_Pm10010ulhCtrlResetmeasurements_Type = EkiOnOff
_Pm10010ulhCtrlResetmeasurements_Object = MibScalar
pm10010ulhCtrlResetmeasurements = _Pm10010ulhCtrlResetmeasurements_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 1, 261, 1),
    _Pm10010ulhCtrlResetmeasurements_Type()
)
pm10010ulhCtrlResetmeasurements.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010ulhCtrlResetmeasurements.setStatus("current")
_Pm10010ulhCtrlClient_ObjectIdentity = ObjectIdentity
pm10010ulhCtrlClient = _Pm10010ulhCtrlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 2)
)
_Pm10010ulhCtrlaccessLoopTable_Object = MibTable
pm10010ulhCtrlaccessLoopTable = _Pm10010ulhCtrlaccessLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 2, 16)
)
if mibBuilder.loadTexts:
    pm10010ulhCtrlaccessLoopTable.setStatus("current")
_Pm10010ulhCtrlaccessLoopEntry_Object = MibTableRow
pm10010ulhCtrlaccessLoopEntry = _Pm10010ulhCtrlaccessLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 2, 16, 1)
)
pm10010ulhCtrlaccessLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhCtrlaccessLoopIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhCtrlaccessLoopEntry.setStatus("current")


class _Pm10010ulhCtrlaccessLoopIndex_Type(Integer32):
    """Custom type pm10010ulhCtrlaccessLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhCtrlaccessLoopIndex_Type.__name__ = "Integer32"
_Pm10010ulhCtrlaccessLoopIndex_Object = MibTableColumn
pm10010ulhCtrlaccessLoopIndex = _Pm10010ulhCtrlaccessLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 2, 16, 1, 1),
    _Pm10010ulhCtrlaccessLoopIndex_Type()
)
pm10010ulhCtrlaccessLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCtrlaccessLoopIndex.setStatus("current")
_Pm10010ulhCtrlaccessLoopPortn_Type = EkiState
_Pm10010ulhCtrlaccessLoopPortn_Object = MibTableColumn
pm10010ulhCtrlaccessLoopPortn = _Pm10010ulhCtrlaccessLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 2, 16, 1, 2),
    _Pm10010ulhCtrlaccessLoopPortn_Type()
)
pm10010ulhCtrlaccessLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010ulhCtrlaccessLoopPortn.setStatus("current")
_Pm10010ulhCtrlclientLoopToLineTable_Object = MibTable
pm10010ulhCtrlclientLoopToLineTable = _Pm10010ulhCtrlclientLoopToLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 2, 17)
)
if mibBuilder.loadTexts:
    pm10010ulhCtrlclientLoopToLineTable.setStatus("current")
_Pm10010ulhCtrlclientLoopToLineEntry_Object = MibTableRow
pm10010ulhCtrlclientLoopToLineEntry = _Pm10010ulhCtrlclientLoopToLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 2, 17, 1)
)
pm10010ulhCtrlclientLoopToLineEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhCtrlclientLoopToLineIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhCtrlclientLoopToLineEntry.setStatus("current")


class _Pm10010ulhCtrlclientLoopToLineIndex_Type(Integer32):
    """Custom type pm10010ulhCtrlclientLoopToLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhCtrlclientLoopToLineIndex_Type.__name__ = "Integer32"
_Pm10010ulhCtrlclientLoopToLineIndex_Object = MibTableColumn
pm10010ulhCtrlclientLoopToLineIndex = _Pm10010ulhCtrlclientLoopToLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 2, 17, 1, 1),
    _Pm10010ulhCtrlclientLoopToLineIndex_Type()
)
pm10010ulhCtrlclientLoopToLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCtrlclientLoopToLineIndex.setStatus("current")
_Pm10010ulhCtrlclientLoopToLinePortn_Type = EkiState
_Pm10010ulhCtrlclientLoopToLinePortn_Object = MibTableColumn
pm10010ulhCtrlclientLoopToLinePortn = _Pm10010ulhCtrlclientLoopToLinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 2, 17, 1, 2),
    _Pm10010ulhCtrlclientLoopToLinePortn_Type()
)
pm10010ulhCtrlclientLoopToLinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010ulhCtrlclientLoopToLinePortn.setStatus("current")
_Pm10010ulhCtrlcsfUpInsTable_Object = MibTable
pm10010ulhCtrlcsfUpInsTable = _Pm10010ulhCtrlcsfUpInsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 2, 21)
)
if mibBuilder.loadTexts:
    pm10010ulhCtrlcsfUpInsTable.setStatus("current")
_Pm10010ulhCtrlcsfUpInsEntry_Object = MibTableRow
pm10010ulhCtrlcsfUpInsEntry = _Pm10010ulhCtrlcsfUpInsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 2, 21, 1)
)
pm10010ulhCtrlcsfUpInsEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhCtrlcsfUpInsIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhCtrlcsfUpInsEntry.setStatus("current")


class _Pm10010ulhCtrlcsfUpInsIndex_Type(Integer32):
    """Custom type pm10010ulhCtrlcsfUpInsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhCtrlcsfUpInsIndex_Type.__name__ = "Integer32"
_Pm10010ulhCtrlcsfUpInsIndex_Object = MibTableColumn
pm10010ulhCtrlcsfUpInsIndex = _Pm10010ulhCtrlcsfUpInsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 2, 21, 1, 1),
    _Pm10010ulhCtrlcsfUpInsIndex_Type()
)
pm10010ulhCtrlcsfUpInsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCtrlcsfUpInsIndex.setStatus("current")
_Pm10010ulhCtrlcsfUpInsPortn_Type = EkiState
_Pm10010ulhCtrlcsfUpInsPortn_Object = MibTableColumn
pm10010ulhCtrlcsfUpInsPortn = _Pm10010ulhCtrlcsfUpInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 2, 21, 1, 2),
    _Pm10010ulhCtrlcsfUpInsPortn_Type()
)
pm10010ulhCtrlcsfUpInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010ulhCtrlcsfUpInsPortn.setStatus("current")
_Pm10010ulhCtrlcaisDwInsTable_Object = MibTable
pm10010ulhCtrlcaisDwInsTable = _Pm10010ulhCtrlcaisDwInsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 2, 22)
)
if mibBuilder.loadTexts:
    pm10010ulhCtrlcaisDwInsTable.setStatus("current")
_Pm10010ulhCtrlcaisDwInsEntry_Object = MibTableRow
pm10010ulhCtrlcaisDwInsEntry = _Pm10010ulhCtrlcaisDwInsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 2, 22, 1)
)
pm10010ulhCtrlcaisDwInsEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhCtrlcaisDwInsIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhCtrlcaisDwInsEntry.setStatus("current")


class _Pm10010ulhCtrlcaisDwInsIndex_Type(Integer32):
    """Custom type pm10010ulhCtrlcaisDwInsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhCtrlcaisDwInsIndex_Type.__name__ = "Integer32"
_Pm10010ulhCtrlcaisDwInsIndex_Object = MibTableColumn
pm10010ulhCtrlcaisDwInsIndex = _Pm10010ulhCtrlcaisDwInsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 2, 22, 1, 1),
    _Pm10010ulhCtrlcaisDwInsIndex_Type()
)
pm10010ulhCtrlcaisDwInsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCtrlcaisDwInsIndex.setStatus("current")
_Pm10010ulhCtrlcaisDwInsPortn_Type = EkiState
_Pm10010ulhCtrlcaisDwInsPortn_Object = MibTableColumn
pm10010ulhCtrlcaisDwInsPortn = _Pm10010ulhCtrlcaisDwInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 2, 22, 1, 2),
    _Pm10010ulhCtrlcaisDwInsPortn_Type()
)
pm10010ulhCtrlcaisDwInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010ulhCtrlcaisDwInsPortn.setStatus("current")
_Pm10010ulhCtrlclientResetAllCountTable_Object = MibTable
pm10010ulhCtrlclientResetAllCountTable = _Pm10010ulhCtrlclientResetAllCountTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 2, 262)
)
if mibBuilder.loadTexts:
    pm10010ulhCtrlclientResetAllCountTable.setStatus("current")
_Pm10010ulhCtrlclientResetAllCountEntry_Object = MibTableRow
pm10010ulhCtrlclientResetAllCountEntry = _Pm10010ulhCtrlclientResetAllCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 2, 262, 1)
)
pm10010ulhCtrlclientResetAllCountEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhCtrlclientResetAllCountIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhCtrlclientResetAllCountEntry.setStatus("current")


class _Pm10010ulhCtrlclientResetAllCountIndex_Type(Integer32):
    """Custom type pm10010ulhCtrlclientResetAllCountIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhCtrlclientResetAllCountIndex_Type.__name__ = "Integer32"
_Pm10010ulhCtrlclientResetAllCountIndex_Object = MibTableColumn
pm10010ulhCtrlclientResetAllCountIndex = _Pm10010ulhCtrlclientResetAllCountIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 2, 262, 1, 1),
    _Pm10010ulhCtrlclientResetAllCountIndex_Type()
)
pm10010ulhCtrlclientResetAllCountIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCtrlclientResetAllCountIndex.setStatus("current")
_Pm10010ulhCtrlclientResetAllCountsPortn_Type = EkiState
_Pm10010ulhCtrlclientResetAllCountsPortn_Object = MibTableColumn
pm10010ulhCtrlclientResetAllCountsPortn = _Pm10010ulhCtrlclientResetAllCountsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 2, 262, 1, 2),
    _Pm10010ulhCtrlclientResetAllCountsPortn_Type()
)
pm10010ulhCtrlclientResetAllCountsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010ulhCtrlclientResetAllCountsPortn.setStatus("current")
_Pm10010ulhCtrlLine_ObjectIdentity = ObjectIdentity
pm10010ulhCtrlLine = _Pm10010ulhCtrlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 3)
)
_Pm10010ulhCtrlcommAccessLoopTable_Object = MibTable
pm10010ulhCtrlcommAccessLoopTable = _Pm10010ulhCtrlcommAccessLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 3, 64)
)
if mibBuilder.loadTexts:
    pm10010ulhCtrlcommAccessLoopTable.setStatus("current")
_Pm10010ulhCtrlcommAccessLoopEntry_Object = MibTableRow
pm10010ulhCtrlcommAccessLoopEntry = _Pm10010ulhCtrlcommAccessLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 3, 64, 1)
)
pm10010ulhCtrlcommAccessLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhCtrlcommAccessLoopIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhCtrlcommAccessLoopEntry.setStatus("current")


class _Pm10010ulhCtrlcommAccessLoopIndex_Type(Integer32):
    """Custom type pm10010ulhCtrlcommAccessLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhCtrlcommAccessLoopIndex_Type.__name__ = "Integer32"
_Pm10010ulhCtrlcommAccessLoopIndex_Object = MibTableColumn
pm10010ulhCtrlcommAccessLoopIndex = _Pm10010ulhCtrlcommAccessLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 3, 64, 1, 1),
    _Pm10010ulhCtrlcommAccessLoopIndex_Type()
)
pm10010ulhCtrlcommAccessLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCtrlcommAccessLoopIndex.setStatus("current")
_Pm10010ulhCtrlcommAccessLoopPortn_Type = EkiState
_Pm10010ulhCtrlcommAccessLoopPortn_Object = MibTableColumn
pm10010ulhCtrlcommAccessLoopPortn = _Pm10010ulhCtrlcommAccessLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 3, 64, 1, 2),
    _Pm10010ulhCtrlcommAccessLoopPortn_Type()
)
pm10010ulhCtrlcommAccessLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010ulhCtrlcommAccessLoopPortn.setStatus("current")
_Pm10010ulhCtrllineLoopTable_Object = MibTable
pm10010ulhCtrllineLoopTable = _Pm10010ulhCtrllineLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 3, 66)
)
if mibBuilder.loadTexts:
    pm10010ulhCtrllineLoopTable.setStatus("current")
_Pm10010ulhCtrllineLoopEntry_Object = MibTableRow
pm10010ulhCtrllineLoopEntry = _Pm10010ulhCtrllineLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 3, 66, 1)
)
pm10010ulhCtrllineLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhCtrllineLoopIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhCtrllineLoopEntry.setStatus("current")


class _Pm10010ulhCtrllineLoopIndex_Type(Integer32):
    """Custom type pm10010ulhCtrllineLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhCtrllineLoopIndex_Type.__name__ = "Integer32"
_Pm10010ulhCtrllineLoopIndex_Object = MibTableColumn
pm10010ulhCtrllineLoopIndex = _Pm10010ulhCtrllineLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 3, 66, 1, 1),
    _Pm10010ulhCtrllineLoopIndex_Type()
)
pm10010ulhCtrllineLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCtrllineLoopIndex.setStatus("current")
_Pm10010ulhCtrllineLoopPortn_Type = EkiState
_Pm10010ulhCtrllineLoopPortn_Object = MibTableColumn
pm10010ulhCtrllineLoopPortn = _Pm10010ulhCtrllineLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 3, 66, 1, 2),
    _Pm10010ulhCtrllineLoopPortn_Type()
)
pm10010ulhCtrllineLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010ulhCtrllineLoopPortn.setStatus("current")
_Pm10010ulhCtrlfecDisableTable_Object = MibTable
pm10010ulhCtrlfecDisableTable = _Pm10010ulhCtrlfecDisableTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 3, 69)
)
if mibBuilder.loadTexts:
    pm10010ulhCtrlfecDisableTable.setStatus("current")
_Pm10010ulhCtrlfecDisableEntry_Object = MibTableRow
pm10010ulhCtrlfecDisableEntry = _Pm10010ulhCtrlfecDisableEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 3, 69, 1)
)
pm10010ulhCtrlfecDisableEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhCtrlfecDisableIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhCtrlfecDisableEntry.setStatus("current")


class _Pm10010ulhCtrlfecDisableIndex_Type(Integer32):
    """Custom type pm10010ulhCtrlfecDisableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhCtrlfecDisableIndex_Type.__name__ = "Integer32"
_Pm10010ulhCtrlfecDisableIndex_Object = MibTableColumn
pm10010ulhCtrlfecDisableIndex = _Pm10010ulhCtrlfecDisableIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 3, 69, 1, 1),
    _Pm10010ulhCtrlfecDisableIndex_Type()
)
pm10010ulhCtrlfecDisableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCtrlfecDisableIndex.setStatus("current")
_Pm10010ulhCtrlfecDisablePortn_Type = EkiState
_Pm10010ulhCtrlfecDisablePortn_Object = MibTableColumn
pm10010ulhCtrlfecDisablePortn = _Pm10010ulhCtrlfecDisablePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 3, 69, 1, 2),
    _Pm10010ulhCtrlfecDisablePortn_Type()
)
pm10010ulhCtrlfecDisablePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010ulhCtrlfecDisablePortn.setStatus("current")
_Pm10010ulhCtrlmsaLineLoopTable_Object = MibTable
pm10010ulhCtrlmsaLineLoopTable = _Pm10010ulhCtrlmsaLineLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 3, 209)
)
if mibBuilder.loadTexts:
    pm10010ulhCtrlmsaLineLoopTable.setStatus("current")
_Pm10010ulhCtrlmsaLineLoopEntry_Object = MibTableRow
pm10010ulhCtrlmsaLineLoopEntry = _Pm10010ulhCtrlmsaLineLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 3, 209, 1)
)
pm10010ulhCtrlmsaLineLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhCtrlmsaLineLoopIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhCtrlmsaLineLoopEntry.setStatus("current")


class _Pm10010ulhCtrlmsaLineLoopIndex_Type(Integer32):
    """Custom type pm10010ulhCtrlmsaLineLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhCtrlmsaLineLoopIndex_Type.__name__ = "Integer32"
_Pm10010ulhCtrlmsaLineLoopIndex_Object = MibTableColumn
pm10010ulhCtrlmsaLineLoopIndex = _Pm10010ulhCtrlmsaLineLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 3, 209, 1, 1),
    _Pm10010ulhCtrlmsaLineLoopIndex_Type()
)
pm10010ulhCtrlmsaLineLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCtrlmsaLineLoopIndex.setStatus("current")
_Pm10010ulhCtrlmsaLineLoopPortn_Type = EkiState
_Pm10010ulhCtrlmsaLineLoopPortn_Object = MibTableColumn
pm10010ulhCtrlmsaLineLoopPortn = _Pm10010ulhCtrlmsaLineLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 3, 209, 1, 2),
    _Pm10010ulhCtrlmsaLineLoopPortn_Type()
)
pm10010ulhCtrlmsaLineLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010ulhCtrlmsaLineLoopPortn.setStatus("current")
_Pm10010ulhCtrlmsaTxResetTable_Object = MibTable
pm10010ulhCtrlmsaTxResetTable = _Pm10010ulhCtrlmsaTxResetTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 3, 210)
)
if mibBuilder.loadTexts:
    pm10010ulhCtrlmsaTxResetTable.setStatus("current")
_Pm10010ulhCtrlmsaTxResetEntry_Object = MibTableRow
pm10010ulhCtrlmsaTxResetEntry = _Pm10010ulhCtrlmsaTxResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 3, 210, 1)
)
pm10010ulhCtrlmsaTxResetEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhCtrlmsaTxResetIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhCtrlmsaTxResetEntry.setStatus("current")


class _Pm10010ulhCtrlmsaTxResetIndex_Type(Integer32):
    """Custom type pm10010ulhCtrlmsaTxResetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhCtrlmsaTxResetIndex_Type.__name__ = "Integer32"
_Pm10010ulhCtrlmsaTxResetIndex_Object = MibTableColumn
pm10010ulhCtrlmsaTxResetIndex = _Pm10010ulhCtrlmsaTxResetIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 3, 210, 1, 1),
    _Pm10010ulhCtrlmsaTxResetIndex_Type()
)
pm10010ulhCtrlmsaTxResetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCtrlmsaTxResetIndex.setStatus("current")
_Pm10010ulhCtrlmsaTxResetPortn_Type = EkiState
_Pm10010ulhCtrlmsaTxResetPortn_Object = MibTableColumn
pm10010ulhCtrlmsaTxResetPortn = _Pm10010ulhCtrlmsaTxResetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 3, 210, 1, 2),
    _Pm10010ulhCtrlmsaTxResetPortn_Type()
)
pm10010ulhCtrlmsaTxResetPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010ulhCtrlmsaTxResetPortn.setStatus("current")
_Pm10010ulhCtrlmsaRxResetTable_Object = MibTable
pm10010ulhCtrlmsaRxResetTable = _Pm10010ulhCtrlmsaRxResetTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 3, 211)
)
if mibBuilder.loadTexts:
    pm10010ulhCtrlmsaRxResetTable.setStatus("current")
_Pm10010ulhCtrlmsaRxResetEntry_Object = MibTableRow
pm10010ulhCtrlmsaRxResetEntry = _Pm10010ulhCtrlmsaRxResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 3, 211, 1)
)
pm10010ulhCtrlmsaRxResetEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhCtrlmsaRxResetIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhCtrlmsaRxResetEntry.setStatus("current")


class _Pm10010ulhCtrlmsaRxResetIndex_Type(Integer32):
    """Custom type pm10010ulhCtrlmsaRxResetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhCtrlmsaRxResetIndex_Type.__name__ = "Integer32"
_Pm10010ulhCtrlmsaRxResetIndex_Object = MibTableColumn
pm10010ulhCtrlmsaRxResetIndex = _Pm10010ulhCtrlmsaRxResetIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 3, 211, 1, 1),
    _Pm10010ulhCtrlmsaRxResetIndex_Type()
)
pm10010ulhCtrlmsaRxResetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCtrlmsaRxResetIndex.setStatus("current")
_Pm10010ulhCtrlmsaRxResetPortn_Type = EkiState
_Pm10010ulhCtrlmsaRxResetPortn_Object = MibTableColumn
pm10010ulhCtrlmsaRxResetPortn = _Pm10010ulhCtrlmsaRxResetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 3, 211, 1, 2),
    _Pm10010ulhCtrlmsaRxResetPortn_Type()
)
pm10010ulhCtrlmsaRxResetPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010ulhCtrlmsaRxResetPortn.setStatus("current")
_Pm10010ulhCtrlmsaShutdownTable_Object = MibTable
pm10010ulhCtrlmsaShutdownTable = _Pm10010ulhCtrlmsaShutdownTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 3, 212)
)
if mibBuilder.loadTexts:
    pm10010ulhCtrlmsaShutdownTable.setStatus("current")
_Pm10010ulhCtrlmsaShutdownEntry_Object = MibTableRow
pm10010ulhCtrlmsaShutdownEntry = _Pm10010ulhCtrlmsaShutdownEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 3, 212, 1)
)
pm10010ulhCtrlmsaShutdownEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhCtrlmsaShutdownIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhCtrlmsaShutdownEntry.setStatus("current")


class _Pm10010ulhCtrlmsaShutdownIndex_Type(Integer32):
    """Custom type pm10010ulhCtrlmsaShutdownIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhCtrlmsaShutdownIndex_Type.__name__ = "Integer32"
_Pm10010ulhCtrlmsaShutdownIndex_Object = MibTableColumn
pm10010ulhCtrlmsaShutdownIndex = _Pm10010ulhCtrlmsaShutdownIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 3, 212, 1, 1),
    _Pm10010ulhCtrlmsaShutdownIndex_Type()
)
pm10010ulhCtrlmsaShutdownIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCtrlmsaShutdownIndex.setStatus("current")
_Pm10010ulhCtrlmsaShutdownPortn_Type = EkiState
_Pm10010ulhCtrlmsaShutdownPortn_Object = MibTableColumn
pm10010ulhCtrlmsaShutdownPortn = _Pm10010ulhCtrlmsaShutdownPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 3, 212, 1, 2),
    _Pm10010ulhCtrlmsaShutdownPortn_Type()
)
pm10010ulhCtrlmsaShutdownPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010ulhCtrlmsaShutdownPortn.setStatus("current")
_Pm10010ulhCtrllineResetAllCountTable_Object = MibTable
pm10010ulhCtrllineResetAllCountTable = _Pm10010ulhCtrllineResetAllCountTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 3, 263)
)
if mibBuilder.loadTexts:
    pm10010ulhCtrllineResetAllCountTable.setStatus("current")
_Pm10010ulhCtrllineResetAllCountEntry_Object = MibTableRow
pm10010ulhCtrllineResetAllCountEntry = _Pm10010ulhCtrllineResetAllCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 3, 263, 1)
)
pm10010ulhCtrllineResetAllCountEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhCtrllineResetAllCountIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhCtrllineResetAllCountEntry.setStatus("current")


class _Pm10010ulhCtrllineResetAllCountIndex_Type(Integer32):
    """Custom type pm10010ulhCtrllineResetAllCountIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhCtrllineResetAllCountIndex_Type.__name__ = "Integer32"
_Pm10010ulhCtrllineResetAllCountIndex_Object = MibTableColumn
pm10010ulhCtrllineResetAllCountIndex = _Pm10010ulhCtrllineResetAllCountIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 3, 263, 1, 1),
    _Pm10010ulhCtrllineResetAllCountIndex_Type()
)
pm10010ulhCtrllineResetAllCountIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCtrllineResetAllCountIndex.setStatus("current")
_Pm10010ulhCtrllineResetAllCountsPortn_Type = EkiState
_Pm10010ulhCtrllineResetAllCountsPortn_Object = MibTableColumn
pm10010ulhCtrllineResetAllCountsPortn = _Pm10010ulhCtrllineResetAllCountsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 6, 3, 263, 1, 2),
    _Pm10010ulhCtrllineResetAllCountsPortn_Type()
)
pm10010ulhCtrllineResetAllCountsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010ulhCtrllineResetAllCountsPortn.setStatus("current")
_Pm10010ulhri_ObjectIdentity = ObjectIdentity
pm10010ulhri = _Pm10010ulhri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 7)
)
_Pm10010ulhriTable_ObjectIdentity = ObjectIdentity
pm10010ulhriTable = _Pm10010ulhriTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 7, 1)
)
_Pm10010ulhRinvSfpTable_Object = MibTable
pm10010ulhRinvSfpTable = _Pm10010ulhRinvSfpTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 7, 1, 1)
)
if mibBuilder.loadTexts:
    pm10010ulhRinvSfpTable.setStatus("current")
_Pm10010ulhRinvSfpEntry_Object = MibTableRow
pm10010ulhRinvSfpEntry = _Pm10010ulhRinvSfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 7, 1, 1, 1)
)
pm10010ulhRinvSfpEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhRinvSfpIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhRinvSfpEntry.setStatus("current")


class _Pm10010ulhRinvSfpIndex_Type(Integer32):
    """Custom type pm10010ulhRinvSfpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pm10010ulhRinvSfpIndex_Type.__name__ = "Integer32"
_Pm10010ulhRinvSfpIndex_Object = MibTableColumn
pm10010ulhRinvSfpIndex = _Pm10010ulhRinvSfpIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 7, 1, 1, 1, 1),
    _Pm10010ulhRinvSfpIndex_Type()
)
pm10010ulhRinvSfpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhRinvSfpIndex.setStatus("current")
_Pm10010ulhRinvsfp_Type = DisplayString
_Pm10010ulhRinvsfp_Object = MibTableColumn
pm10010ulhRinvsfp = _Pm10010ulhRinvsfp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 7, 1, 1, 1, 2),
    _Pm10010ulhRinvsfp_Type()
)
pm10010ulhRinvsfp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhRinvsfp.setStatus("current")
_Pm10010ulhRinvLineTable_Object = MibTable
pm10010ulhRinvLineTable = _Pm10010ulhRinvLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 7, 1, 2)
)
if mibBuilder.loadTexts:
    pm10010ulhRinvLineTable.setStatus("current")
_Pm10010ulhRinvLineEntry_Object = MibTableRow
pm10010ulhRinvLineEntry = _Pm10010ulhRinvLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 7, 1, 2, 1)
)
pm10010ulhRinvLineEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhRinvLineIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhRinvLineEntry.setStatus("current")


class _Pm10010ulhRinvLineIndex_Type(Integer32):
    """Custom type pm10010ulhRinvLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pm10010ulhRinvLineIndex_Type.__name__ = "Integer32"
_Pm10010ulhRinvLineIndex_Object = MibTableColumn
pm10010ulhRinvLineIndex = _Pm10010ulhRinvLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 7, 1, 2, 1, 1),
    _Pm10010ulhRinvLineIndex_Type()
)
pm10010ulhRinvLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhRinvLineIndex.setStatus("current")
_Pm10010ulhRinvxfpLine_Type = DisplayString
_Pm10010ulhRinvxfpLine_Object = MibTableColumn
pm10010ulhRinvxfpLine = _Pm10010ulhRinvxfpLine_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 7, 1, 2, 1, 2),
    _Pm10010ulhRinvxfpLine_Type()
)
pm10010ulhRinvxfpLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhRinvxfpLine.setStatus("current")
_Pm10010ulhRinvReloadInventory_Type = EkiOnOff
_Pm10010ulhRinvReloadInventory_Object = MibScalar
pm10010ulhRinvReloadInventory = _Pm10010ulhRinvReloadInventory_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 7, 2),
    _Pm10010ulhRinvReloadInventory_Type()
)
pm10010ulhRinvReloadInventory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010ulhRinvReloadInventory.setStatus("current")
_Pm10010ulhRinvHwPlatform_Type = DisplayString
_Pm10010ulhRinvHwPlatform_Object = MibScalar
pm10010ulhRinvHwPlatform = _Pm10010ulhRinvHwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 7, 3),
    _Pm10010ulhRinvHwPlatform_Type()
)
pm10010ulhRinvHwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhRinvHwPlatform.setStatus("current")
_Pm10010ulhRinvModulePlatform_Type = DisplayString
_Pm10010ulhRinvModulePlatform_Object = MibScalar
pm10010ulhRinvModulePlatform = _Pm10010ulhRinvModulePlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 7, 4),
    _Pm10010ulhRinvModulePlatform_Type()
)
pm10010ulhRinvModulePlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhRinvModulePlatform.setStatus("current")
_Pm10010ulhRinvSwPlatform_Type = DisplayString
_Pm10010ulhRinvSwPlatform_Object = MibScalar
pm10010ulhRinvSwPlatform = _Pm10010ulhRinvSwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 7, 5),
    _Pm10010ulhRinvSwPlatform_Type()
)
pm10010ulhRinvSwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhRinvSwPlatform.setStatus("current")
_Pm10010ulhRinvGwPlatform_Type = DisplayString
_Pm10010ulhRinvGwPlatform_Object = MibScalar
pm10010ulhRinvGwPlatform = _Pm10010ulhRinvGwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 7, 6),
    _Pm10010ulhRinvGwPlatform_Type()
)
pm10010ulhRinvGwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhRinvGwPlatform.setStatus("current")
_Pm10010ulhdownload_ObjectIdentity = ObjectIdentity
pm10010ulhdownload = _Pm10010ulhdownload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 8)
)
_Pm10010ulhDwlOther_ObjectIdentity = ObjectIdentity
pm10010ulhDwlOther = _Pm10010ulhDwlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 8, 1)
)
_Pm10010ulhDwlrestartProcess_ObjectIdentity = ObjectIdentity
pm10010ulhDwlrestartProcess = _Pm10010ulhDwlrestartProcess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 8, 1, 0)
)
_Pm10010ulhDwlWarmRestartProcessed_Type = EkiOnOff
_Pm10010ulhDwlWarmRestartProcessed_Object = MibScalar
pm10010ulhDwlWarmRestartProcessed = _Pm10010ulhDwlWarmRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 8, 1, 0, 1),
    _Pm10010ulhDwlWarmRestartProcessed_Type()
)
pm10010ulhDwlWarmRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhDwlWarmRestartProcessed.setStatus("current")
_Pm10010ulhDwlColdRestartProcessed_Type = EkiOnOff
_Pm10010ulhDwlColdRestartProcessed_Object = MibScalar
pm10010ulhDwlColdRestartProcessed = _Pm10010ulhDwlColdRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 8, 1, 0, 2),
    _Pm10010ulhDwlColdRestartProcessed_Type()
)
pm10010ulhDwlColdRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhDwlColdRestartProcessed.setStatus("current")
_Pm10010ulhDwlswBanksUsed_ObjectIdentity = ObjectIdentity
pm10010ulhDwlswBanksUsed = _Pm10010ulhDwlswBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 8, 1, 1)
)
_Pm10010ulhDwlSwBank1Used_Type = EkiOnOff
_Pm10010ulhDwlSwBank1Used_Object = MibScalar
pm10010ulhDwlSwBank1Used = _Pm10010ulhDwlSwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 8, 1, 1, 1),
    _Pm10010ulhDwlSwBank1Used_Type()
)
pm10010ulhDwlSwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhDwlSwBank1Used.setStatus("current")
_Pm10010ulhDwlSwBank2Used_Type = EkiOnOff
_Pm10010ulhDwlSwBank2Used_Object = MibScalar
pm10010ulhDwlSwBank2Used = _Pm10010ulhDwlSwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 8, 1, 1, 2),
    _Pm10010ulhDwlSwBank2Used_Type()
)
pm10010ulhDwlSwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhDwlSwBank2Used.setStatus("current")
_Pm10010ulhDwlSwBank1Notempty_Type = EkiOnOff
_Pm10010ulhDwlSwBank1Notempty_Object = MibScalar
pm10010ulhDwlSwBank1Notempty = _Pm10010ulhDwlSwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 8, 1, 1, 5),
    _Pm10010ulhDwlSwBank1Notempty_Type()
)
pm10010ulhDwlSwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhDwlSwBank1Notempty.setStatus("current")
_Pm10010ulhDwlSwBank2Notempty_Type = EkiOnOff
_Pm10010ulhDwlSwBank2Notempty_Object = MibScalar
pm10010ulhDwlSwBank2Notempty = _Pm10010ulhDwlSwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 8, 1, 1, 6),
    _Pm10010ulhDwlSwBank2Notempty_Type()
)
pm10010ulhDwlSwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhDwlSwBank2Notempty.setStatus("current")
_Pm10010ulhDwlgwBanksUsed_ObjectIdentity = ObjectIdentity
pm10010ulhDwlgwBanksUsed = _Pm10010ulhDwlgwBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 8, 1, 2)
)
_Pm10010ulhDwlGwBank1Used_Type = EkiOnOff
_Pm10010ulhDwlGwBank1Used_Object = MibScalar
pm10010ulhDwlGwBank1Used = _Pm10010ulhDwlGwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 8, 1, 2, 1),
    _Pm10010ulhDwlGwBank1Used_Type()
)
pm10010ulhDwlGwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhDwlGwBank1Used.setStatus("current")
_Pm10010ulhDwlGwBank2Used_Type = EkiOnOff
_Pm10010ulhDwlGwBank2Used_Object = MibScalar
pm10010ulhDwlGwBank2Used = _Pm10010ulhDwlGwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 8, 1, 2, 2),
    _Pm10010ulhDwlGwBank2Used_Type()
)
pm10010ulhDwlGwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhDwlGwBank2Used.setStatus("current")
_Pm10010ulhDwlGwBank3Used_Type = EkiOnOff
_Pm10010ulhDwlGwBank3Used_Object = MibScalar
pm10010ulhDwlGwBank3Used = _Pm10010ulhDwlGwBank3Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 8, 1, 2, 3),
    _Pm10010ulhDwlGwBank3Used_Type()
)
pm10010ulhDwlGwBank3Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhDwlGwBank3Used.setStatus("current")
_Pm10010ulhDwlGwBank4Used_Type = EkiOnOff
_Pm10010ulhDwlGwBank4Used_Object = MibScalar
pm10010ulhDwlGwBank4Used = _Pm10010ulhDwlGwBank4Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 8, 1, 2, 4),
    _Pm10010ulhDwlGwBank4Used_Type()
)
pm10010ulhDwlGwBank4Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhDwlGwBank4Used.setStatus("current")
_Pm10010ulhDwlGwBank1Notempty_Type = EkiOnOff
_Pm10010ulhDwlGwBank1Notempty_Object = MibScalar
pm10010ulhDwlGwBank1Notempty = _Pm10010ulhDwlGwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 8, 1, 2, 5),
    _Pm10010ulhDwlGwBank1Notempty_Type()
)
pm10010ulhDwlGwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhDwlGwBank1Notempty.setStatus("current")
_Pm10010ulhDwlGwBank2Notempty_Type = EkiOnOff
_Pm10010ulhDwlGwBank2Notempty_Object = MibScalar
pm10010ulhDwlGwBank2Notempty = _Pm10010ulhDwlGwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 8, 1, 2, 6),
    _Pm10010ulhDwlGwBank2Notempty_Type()
)
pm10010ulhDwlGwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhDwlGwBank2Notempty.setStatus("current")
_Pm10010ulhDwlGwBank3Notempty_Type = EkiOnOff
_Pm10010ulhDwlGwBank3Notempty_Object = MibScalar
pm10010ulhDwlGwBank3Notempty = _Pm10010ulhDwlGwBank3Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 8, 1, 2, 7),
    _Pm10010ulhDwlGwBank3Notempty_Type()
)
pm10010ulhDwlGwBank3Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhDwlGwBank3Notempty.setStatus("current")
_Pm10010ulhDwlGwBank4Notempty_Type = EkiOnOff
_Pm10010ulhDwlGwBank4Notempty_Object = MibScalar
pm10010ulhDwlGwBank4Notempty = _Pm10010ulhDwlGwBank4Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 8, 1, 2, 8),
    _Pm10010ulhDwlGwBank4Notempty_Type()
)
pm10010ulhDwlGwBank4Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhDwlGwBank4Notempty.setStatus("current")
_Pm10010ulhDwlClient_ObjectIdentity = ObjectIdentity
pm10010ulhDwlClient = _Pm10010ulhDwlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 8, 2)
)
_Pm10010ulhDwlLine_ObjectIdentity = ObjectIdentity
pm10010ulhDwlLine = _Pm10010ulhDwlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 8, 3)
)
_Pm10010ulhConfig_ObjectIdentity = ObjectIdentity
pm10010ulhConfig = _Pm10010ulhConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 9)
)
_Pm10010ulhCfgAccessCAisCsf_ObjectIdentity = ObjectIdentity
pm10010ulhCfgAccessCAisCsf = _Pm10010ulhCfgAccessCAisCsf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 9, 1)
)
_Pm10010ulhCfgClientcaiscsfTable_Object = MibTable
pm10010ulhCfgClientcaiscsfTable = _Pm10010ulhCfgClientcaiscsfTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 9, 1, 1)
)
if mibBuilder.loadTexts:
    pm10010ulhCfgClientcaiscsfTable.setStatus("current")
_Pm10010ulhCfgClientcaiscsfEntry_Object = MibTableRow
pm10010ulhCfgClientcaiscsfEntry = _Pm10010ulhCfgClientcaiscsfEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 9, 1, 1, 1)
)
pm10010ulhCfgClientcaiscsfEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhCfgClientcaiscsfIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhCfgClientcaiscsfEntry.setStatus("current")


class _Pm10010ulhCfgClientcaiscsfIndex_Type(Integer32):
    """Custom type pm10010ulhCfgClientcaiscsfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhCfgClientcaiscsfIndex_Type.__name__ = "Integer32"
_Pm10010ulhCfgClientcaiscsfIndex_Object = MibTableColumn
pm10010ulhCfgClientcaiscsfIndex = _Pm10010ulhCfgClientcaiscsfIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 9, 1, 1, 1, 1),
    _Pm10010ulhCfgClientcaiscsfIndex_Type()
)
pm10010ulhCfgClientcaiscsfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCfgClientcaiscsfIndex.setStatus("current")


class _Pm10010ulhCfgReservePortn_Type(Unsigned32):
    """Custom type pm10010ulhCfgReservePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010ulhCfgReservePortn_Type.__name__ = "Unsigned32"
_Pm10010ulhCfgReservePortn_Object = MibTableColumn
pm10010ulhCfgReservePortn = _Pm10010ulhCfgReservePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 9, 1, 1, 1, 3),
    _Pm10010ulhCfgReservePortn_Type()
)
pm10010ulhCfgReservePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010ulhCfgReservePortn.setStatus("current")
_Pm10010ulhCfgStartup_ObjectIdentity = ObjectIdentity
pm10010ulhCfgStartup = _Pm10010ulhCfgStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 9, 2)
)
_Pm10010ulhCfgClientStartupTable_Object = MibTable
pm10010ulhCfgClientStartupTable = _Pm10010ulhCfgClientStartupTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 9, 2, 1)
)
if mibBuilder.loadTexts:
    pm10010ulhCfgClientStartupTable.setStatus("current")
_Pm10010ulhCfgClientStartupEntry_Object = MibTableRow
pm10010ulhCfgClientStartupEntry = _Pm10010ulhCfgClientStartupEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 9, 2, 1, 1)
)
pm10010ulhCfgClientStartupEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhCfgClientStartupIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhCfgClientStartupEntry.setStatus("current")


class _Pm10010ulhCfgClientStartupIndex_Type(Integer32):
    """Custom type pm10010ulhCfgClientStartupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhCfgClientStartupIndex_Type.__name__ = "Integer32"
_Pm10010ulhCfgClientStartupIndex_Object = MibTableColumn
pm10010ulhCfgClientStartupIndex = _Pm10010ulhCfgClientStartupIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 9, 2, 1, 1, 1),
    _Pm10010ulhCfgClientStartupIndex_Type()
)
pm10010ulhCfgClientStartupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCfgClientStartupIndex.setStatus("current")


class _Pm10010ulhCfgSystConfPortPortn_Type(Unsigned32):
    """Custom type pm10010ulhCfgSystConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010ulhCfgSystConfPortPortn_Type.__name__ = "Unsigned32"
_Pm10010ulhCfgSystConfPortPortn_Object = MibTableColumn
pm10010ulhCfgSystConfPortPortn = _Pm10010ulhCfgSystConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 9, 2, 1, 1, 3),
    _Pm10010ulhCfgSystConfPortPortn_Type()
)
pm10010ulhCfgSystConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010ulhCfgSystConfPortPortn.setStatus("current")


class _Pm10010ulhCfgNetConfPortPortn_Type(Unsigned32):
    """Custom type pm10010ulhCfgNetConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010ulhCfgNetConfPortPortn_Type.__name__ = "Unsigned32"
_Pm10010ulhCfgNetConfPortPortn_Object = MibTableColumn
pm10010ulhCfgNetConfPortPortn = _Pm10010ulhCfgNetConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 9, 2, 1, 1, 4),
    _Pm10010ulhCfgNetConfPortPortn_Type()
)
pm10010ulhCfgNetConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010ulhCfgNetConfPortPortn.setStatus("current")


class _Pm10010ulhCfgOptionsPortPortn_Type(Unsigned32):
    """Custom type pm10010ulhCfgOptionsPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010ulhCfgOptionsPortPortn_Type.__name__ = "Unsigned32"
_Pm10010ulhCfgOptionsPortPortn_Object = MibTableColumn
pm10010ulhCfgOptionsPortPortn = _Pm10010ulhCfgOptionsPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 9, 2, 1, 1, 14),
    _Pm10010ulhCfgOptionsPortPortn_Type()
)
pm10010ulhCfgOptionsPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010ulhCfgOptionsPortPortn.setStatus("current")
_Pm10010ulhCfgLineStartupTable_Object = MibTable
pm10010ulhCfgLineStartupTable = _Pm10010ulhCfgLineStartupTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 9, 2, 2)
)
if mibBuilder.loadTexts:
    pm10010ulhCfgLineStartupTable.setStatus("current")
_Pm10010ulhCfgLineStartupEntry_Object = MibTableRow
pm10010ulhCfgLineStartupEntry = _Pm10010ulhCfgLineStartupEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 9, 2, 2, 1)
)
pm10010ulhCfgLineStartupEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhCfgLineStartupIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhCfgLineStartupEntry.setStatus("current")


class _Pm10010ulhCfgLineStartupIndex_Type(Integer32):
    """Custom type pm10010ulhCfgLineStartupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhCfgLineStartupIndex_Type.__name__ = "Integer32"
_Pm10010ulhCfgLineStartupIndex_Object = MibTableColumn
pm10010ulhCfgLineStartupIndex = _Pm10010ulhCfgLineStartupIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 9, 2, 2, 1, 1),
    _Pm10010ulhCfgLineStartupIndex_Type()
)
pm10010ulhCfgLineStartupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCfgLineStartupIndex.setStatus("current")


class _Pm10010ulhCfgSystConfLinePortn_Type(Unsigned32):
    """Custom type pm10010ulhCfgSystConfLinePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010ulhCfgSystConfLinePortn_Type.__name__ = "Unsigned32"
_Pm10010ulhCfgSystConfLinePortn_Object = MibTableColumn
pm10010ulhCfgSystConfLinePortn = _Pm10010ulhCfgSystConfLinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 9, 2, 2, 1, 3),
    _Pm10010ulhCfgSystConfLinePortn_Type()
)
pm10010ulhCfgSystConfLinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010ulhCfgSystConfLinePortn.setStatus("current")


class _Pm10010ulhCfgOptionsLinePortn_Type(Unsigned32):
    """Custom type pm10010ulhCfgOptionsLinePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010ulhCfgOptionsLinePortn_Type.__name__ = "Unsigned32"
_Pm10010ulhCfgOptionsLinePortn_Object = MibTableColumn
pm10010ulhCfgOptionsLinePortn = _Pm10010ulhCfgOptionsLinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 9, 2, 2, 1, 14),
    _Pm10010ulhCfgOptionsLinePortn_Type()
)
pm10010ulhCfgOptionsLinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010ulhCfgOptionsLinePortn.setStatus("current")
_Pm10010ulhCfgXfpTable_Object = MibTable
pm10010ulhCfgXfpTable = _Pm10010ulhCfgXfpTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 9, 2, 3)
)
if mibBuilder.loadTexts:
    pm10010ulhCfgXfpTable.setStatus("current")
_Pm10010ulhCfgXfpEntry_Object = MibTableRow
pm10010ulhCfgXfpEntry = _Pm10010ulhCfgXfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 9, 2, 3, 1)
)
pm10010ulhCfgXfpEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhCfgXfpIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhCfgXfpEntry.setStatus("current")


class _Pm10010ulhCfgXfpIndex_Type(Integer32):
    """Custom type pm10010ulhCfgXfpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhCfgXfpIndex_Type.__name__ = "Integer32"
_Pm10010ulhCfgXfpIndex_Object = MibTableColumn
pm10010ulhCfgXfpIndex = _Pm10010ulhCfgXfpIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 9, 2, 3, 1, 1),
    _Pm10010ulhCfgXfpIndex_Type()
)
pm10010ulhCfgXfpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCfgXfpIndex.setStatus("current")


class _Pm10010ulhCfgSystConfMsaLinePortn_Type(Unsigned32):
    """Custom type pm10010ulhCfgSystConfMsaLinePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010ulhCfgSystConfMsaLinePortn_Type.__name__ = "Unsigned32"
_Pm10010ulhCfgSystConfMsaLinePortn_Object = MibTableColumn
pm10010ulhCfgSystConfMsaLinePortn = _Pm10010ulhCfgSystConfMsaLinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 9, 2, 3, 1, 3),
    _Pm10010ulhCfgSystConfMsaLinePortn_Type()
)
pm10010ulhCfgSystConfMsaLinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010ulhCfgSystConfMsaLinePortn.setStatus("current")
_Pm10010ulhCfgLabels_ObjectIdentity = ObjectIdentity
pm10010ulhCfgLabels = _Pm10010ulhCfgLabels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 9, 3)
)
_Pm10010ulhCfgLabelclientTable_Object = MibTable
pm10010ulhCfgLabelclientTable = _Pm10010ulhCfgLabelclientTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 9, 3, 1)
)
if mibBuilder.loadTexts:
    pm10010ulhCfgLabelclientTable.setStatus("current")
_Pm10010ulhCfgLabelclientEntry_Object = MibTableRow
pm10010ulhCfgLabelclientEntry = _Pm10010ulhCfgLabelclientEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 9, 3, 1, 1)
)
pm10010ulhCfgLabelclientEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhCfgLabelclientIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhCfgLabelclientEntry.setStatus("current")


class _Pm10010ulhCfgLabelclientIndex_Type(Integer32):
    """Custom type pm10010ulhCfgLabelclientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhCfgLabelclientIndex_Type.__name__ = "Integer32"
_Pm10010ulhCfgLabelclientIndex_Object = MibTableColumn
pm10010ulhCfgLabelclientIndex = _Pm10010ulhCfgLabelclientIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 9, 3, 1, 1, 1),
    _Pm10010ulhCfgLabelclientIndex_Type()
)
pm10010ulhCfgLabelclientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCfgLabelclientIndex.setStatus("current")


class _Pm10010ulhCfgLabelclientPortn_Type(DisplayString):
    """Custom type pm10010ulhCfgLabelclientPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pm10010ulhCfgLabelclientPortn_Type.__name__ = "DisplayString"
_Pm10010ulhCfgLabelclientPortn_Object = MibTableColumn
pm10010ulhCfgLabelclientPortn = _Pm10010ulhCfgLabelclientPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 9, 3, 1, 1, 3),
    _Pm10010ulhCfgLabelclientPortn_Type()
)
pm10010ulhCfgLabelclientPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010ulhCfgLabelclientPortn.setStatus("current")
_Pm10010ulhCfgLabellineTable_Object = MibTable
pm10010ulhCfgLabellineTable = _Pm10010ulhCfgLabellineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 9, 3, 2)
)
if mibBuilder.loadTexts:
    pm10010ulhCfgLabellineTable.setStatus("current")
_Pm10010ulhCfgLabellineEntry_Object = MibTableRow
pm10010ulhCfgLabellineEntry = _Pm10010ulhCfgLabellineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 9, 3, 2, 1)
)
pm10010ulhCfgLabellineEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhCfgLabellineIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhCfgLabellineEntry.setStatus("current")


class _Pm10010ulhCfgLabellineIndex_Type(Integer32):
    """Custom type pm10010ulhCfgLabellineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhCfgLabellineIndex_Type.__name__ = "Integer32"
_Pm10010ulhCfgLabellineIndex_Object = MibTableColumn
pm10010ulhCfgLabellineIndex = _Pm10010ulhCfgLabellineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 9, 3, 2, 1, 1),
    _Pm10010ulhCfgLabellineIndex_Type()
)
pm10010ulhCfgLabellineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCfgLabellineIndex.setStatus("current")


class _Pm10010ulhCfgLabellinePortn_Type(DisplayString):
    """Custom type pm10010ulhCfgLabellinePortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pm10010ulhCfgLabellinePortn_Type.__name__ = "DisplayString"
_Pm10010ulhCfgLabellinePortn_Object = MibTableColumn
pm10010ulhCfgLabellinePortn = _Pm10010ulhCfgLabellinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 9, 3, 2, 1, 3),
    _Pm10010ulhCfgLabellinePortn_Type()
)
pm10010ulhCfgLabellinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010ulhCfgLabellinePortn.setStatus("current")
_Pm10010ulhCfgStartuptlh_ObjectIdentity = ObjectIdentity
pm10010ulhCfgStartuptlh = _Pm10010ulhCfgStartuptlh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 9, 4)
)
_Pm10010ulhCfgOtxtlhTable_Object = MibTable
pm10010ulhCfgOtxtlhTable = _Pm10010ulhCfgOtxtlhTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 9, 4, 1)
)
if mibBuilder.loadTexts:
    pm10010ulhCfgOtxtlhTable.setStatus("current")
_Pm10010ulhCfgOtxtlhEntry_Object = MibTableRow
pm10010ulhCfgOtxtlhEntry = _Pm10010ulhCfgOtxtlhEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 9, 4, 1, 1)
)
pm10010ulhCfgOtxtlhEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhCfgOtxtlhIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhCfgOtxtlhEntry.setStatus("current")


class _Pm10010ulhCfgOtxtlhIndex_Type(Integer32):
    """Custom type pm10010ulhCfgOtxtlhIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhCfgOtxtlhIndex_Type.__name__ = "Integer32"
_Pm10010ulhCfgOtxtlhIndex_Object = MibTableColumn
pm10010ulhCfgOtxtlhIndex = _Pm10010ulhCfgOtxtlhIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 9, 4, 1, 1, 1),
    _Pm10010ulhCfgOtxtlhIndex_Type()
)
pm10010ulhCfgOtxtlhIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCfgOtxtlhIndex.setStatus("current")


class _Pm10010ulhCfgLinePwrLaserPortn_Type(Unsigned32):
    """Custom type pm10010ulhCfgLinePwrLaserPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010ulhCfgLinePwrLaserPortn_Type.__name__ = "Unsigned32"
_Pm10010ulhCfgLinePwrLaserPortn_Object = MibTableColumn
pm10010ulhCfgLinePwrLaserPortn = _Pm10010ulhCfgLinePwrLaserPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 9, 4, 1, 1, 6),
    _Pm10010ulhCfgLinePwrLaserPortn_Type()
)
pm10010ulhCfgLinePwrLaserPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010ulhCfgLinePwrLaserPortn.setStatus("current")


class _Pm10010ulhCfgLineFCurrentPortn_Type(Unsigned32):
    """Custom type pm10010ulhCfgLineFCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010ulhCfgLineFCurrentPortn_Type.__name__ = "Unsigned32"
_Pm10010ulhCfgLineFCurrentPortn_Object = MibTableColumn
pm10010ulhCfgLineFCurrentPortn = _Pm10010ulhCfgLineFCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 9, 4, 1, 1, 7),
    _Pm10010ulhCfgLineFCurrentPortn_Type()
)
pm10010ulhCfgLineFCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010ulhCfgLineFCurrentPortn.setStatus("current")


class _Pm10010ulhCfgLineGridCurrentPortn_Type(Unsigned32):
    """Custom type pm10010ulhCfgLineGridCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010ulhCfgLineGridCurrentPortn_Type.__name__ = "Unsigned32"
_Pm10010ulhCfgLineGridCurrentPortn_Object = MibTableColumn
pm10010ulhCfgLineGridCurrentPortn = _Pm10010ulhCfgLineGridCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 9, 4, 1, 1, 8),
    _Pm10010ulhCfgLineGridCurrentPortn_Type()
)
pm10010ulhCfgLineGridCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010ulhCfgLineGridCurrentPortn.setStatus("current")


class _Pm10010ulhCfgFPortn_Type(Unsigned32):
    """Custom type pm10010ulhCfgFPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010ulhCfgFPortn_Type.__name__ = "Unsigned32"
_Pm10010ulhCfgFPortn_Object = MibTableColumn
pm10010ulhCfgFPortn = _Pm10010ulhCfgFPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 9, 4, 1, 1, 9),
    _Pm10010ulhCfgFPortn_Type()
)
pm10010ulhCfgFPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010ulhCfgFPortn.setStatus("current")


class _Pm10010ulhCfgRxLineFCurrentPortn_Type(Unsigned32):
    """Custom type pm10010ulhCfgRxLineFCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010ulhCfgRxLineFCurrentPortn_Type.__name__ = "Unsigned32"
_Pm10010ulhCfgRxLineFCurrentPortn_Object = MibTableColumn
pm10010ulhCfgRxLineFCurrentPortn = _Pm10010ulhCfgRxLineFCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 9, 4, 1, 1, 10),
    _Pm10010ulhCfgRxLineFCurrentPortn_Type()
)
pm10010ulhCfgRxLineFCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010ulhCfgRxLineFCurrentPortn.setStatus("current")
_Pm10010ulhCfgOther_ObjectIdentity = ObjectIdentity
pm10010ulhCfgOther = _Pm10010ulhCfgOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 9, 5)
)
_Pm10010ulhtablemoduleOther_ObjectIdentity = ObjectIdentity
pm10010ulhtablemoduleOther = _Pm10010ulhtablemoduleOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 9, 5, 1)
)


class _Pm10010ulhCfgmode_Type(Unsigned32):
    """Custom type pm10010ulhCfgmode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010ulhCfgmode_Type.__name__ = "Unsigned32"
_Pm10010ulhCfgmode_Object = MibScalar
pm10010ulhCfgmode = _Pm10010ulhCfgmode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 9, 5, 1, 2),
    _Pm10010ulhCfgmode_Type()
)
pm10010ulhCfgmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010ulhCfgmode.setStatus("current")


class _Pm10010ulhCfgfanLowSpeedThreshold_Type(Unsigned32):
    """Custom type pm10010ulhCfgfanLowSpeedThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010ulhCfgfanLowSpeedThreshold_Type.__name__ = "Unsigned32"
_Pm10010ulhCfgfanLowSpeedThreshold_Object = MibScalar
pm10010ulhCfgfanLowSpeedThreshold = _Pm10010ulhCfgfanLowSpeedThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 9, 5, 1, 3),
    _Pm10010ulhCfgfanLowSpeedThreshold_Type()
)
pm10010ulhCfgfanLowSpeedThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010ulhCfgfanLowSpeedThreshold.setStatus("current")


class _Pm10010ulhCfgfanHighSpeedThreshold_Type(Unsigned32):
    """Custom type pm10010ulhCfgfanHighSpeedThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010ulhCfgfanHighSpeedThreshold_Type.__name__ = "Unsigned32"
_Pm10010ulhCfgfanHighSpeedThreshold_Object = MibScalar
pm10010ulhCfgfanHighSpeedThreshold = _Pm10010ulhCfgfanHighSpeedThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 9, 5, 1, 4),
    _Pm10010ulhCfgfanHighSpeedThreshold_Type()
)
pm10010ulhCfgfanHighSpeedThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010ulhCfgfanHighSpeedThreshold.setStatus("current")
_Pm10010ulhCfgStartuptablefive_ObjectIdentity = ObjectIdentity
pm10010ulhCfgStartuptablefive = _Pm10010ulhCfgStartuptablefive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 9, 6)
)
_Pm10010ulhCfgOtxtlhcapabilitiesTable_Object = MibTable
pm10010ulhCfgOtxtlhcapabilitiesTable = _Pm10010ulhCfgOtxtlhcapabilitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 9, 6, 1)
)
if mibBuilder.loadTexts:
    pm10010ulhCfgOtxtlhcapabilitiesTable.setStatus("current")
_Pm10010ulhCfgOtxtlhcapabilitiesEntry_Object = MibTableRow
pm10010ulhCfgOtxtlhcapabilitiesEntry = _Pm10010ulhCfgOtxtlhcapabilitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 9, 6, 1, 1)
)
pm10010ulhCfgOtxtlhcapabilitiesEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhCfgOtxtlhcapabilitiesIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhCfgOtxtlhcapabilitiesEntry.setStatus("current")


class _Pm10010ulhCfgOtxtlhcapabilitiesIndex_Type(Integer32):
    """Custom type pm10010ulhCfgOtxtlhcapabilitiesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhCfgOtxtlhcapabilitiesIndex_Type.__name__ = "Integer32"
_Pm10010ulhCfgOtxtlhcapabilitiesIndex_Object = MibTableColumn
pm10010ulhCfgOtxtlhcapabilitiesIndex = _Pm10010ulhCfgOtxtlhcapabilitiesIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 9, 6, 1, 1, 1),
    _Pm10010ulhCfgOtxtlhcapabilitiesIndex_Type()
)
pm10010ulhCfgOtxtlhcapabilitiesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCfgOtxtlhcapabilitiesIndex.setStatus("current")


class _Pm10010ulhCfgComponentTypePortn_Type(Unsigned32):
    """Custom type pm10010ulhCfgComponentTypePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010ulhCfgComponentTypePortn_Type.__name__ = "Unsigned32"
_Pm10010ulhCfgComponentTypePortn_Object = MibTableColumn
pm10010ulhCfgComponentTypePortn = _Pm10010ulhCfgComponentTypePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 9, 6, 1, 1, 3),
    _Pm10010ulhCfgComponentTypePortn_Type()
)
pm10010ulhCfgComponentTypePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCfgComponentTypePortn.setStatus("current")


class _Pm10010ulhCfgMiscellaneousPortn_Type(Unsigned32):
    """Custom type pm10010ulhCfgMiscellaneousPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010ulhCfgMiscellaneousPortn_Type.__name__ = "Unsigned32"
_Pm10010ulhCfgMiscellaneousPortn_Object = MibTableColumn
pm10010ulhCfgMiscellaneousPortn = _Pm10010ulhCfgMiscellaneousPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 9, 6, 1, 1, 4),
    _Pm10010ulhCfgMiscellaneousPortn_Type()
)
pm10010ulhCfgMiscellaneousPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCfgMiscellaneousPortn.setStatus("current")


class _Pm10010ulhCfgFirstChannelPortn_Type(Unsigned32):
    """Custom type pm10010ulhCfgFirstChannelPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010ulhCfgFirstChannelPortn_Type.__name__ = "Unsigned32"
_Pm10010ulhCfgFirstChannelPortn_Object = MibTableColumn
pm10010ulhCfgFirstChannelPortn = _Pm10010ulhCfgFirstChannelPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 9, 6, 1, 1, 5),
    _Pm10010ulhCfgFirstChannelPortn_Type()
)
pm10010ulhCfgFirstChannelPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCfgFirstChannelPortn.setStatus("current")


class _Pm10010ulhCfgLastChannelPortn_Type(Unsigned32):
    """Custom type pm10010ulhCfgLastChannelPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010ulhCfgLastChannelPortn_Type.__name__ = "Unsigned32"
_Pm10010ulhCfgLastChannelPortn_Object = MibTableColumn
pm10010ulhCfgLastChannelPortn = _Pm10010ulhCfgLastChannelPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 9, 6, 1, 1, 6),
    _Pm10010ulhCfgLastChannelPortn_Type()
)
pm10010ulhCfgLastChannelPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCfgLastChannelPortn.setStatus("current")


class _Pm10010ulhCfgGridPortn_Type(Unsigned32):
    """Custom type pm10010ulhCfgGridPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010ulhCfgGridPortn_Type.__name__ = "Unsigned32"
_Pm10010ulhCfgGridPortn_Object = MibTableColumn
pm10010ulhCfgGridPortn = _Pm10010ulhCfgGridPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 9, 6, 1, 1, 7),
    _Pm10010ulhCfgGridPortn_Type()
)
pm10010ulhCfgGridPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhCfgGridPortn.setStatus("current")
_Pm10010ulhCfgWriteConfiguration_Type = EkiOnOff
_Pm10010ulhCfgWriteConfiguration_Object = MibScalar
pm10010ulhCfgWriteConfiguration = _Pm10010ulhCfgWriteConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 9, 257),
    _Pm10010ulhCfgWriteConfiguration_Type()
)
pm10010ulhCfgWriteConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010ulhCfgWriteConfiguration.setStatus("current")
_Pm10010ulhtraps_ObjectIdentity = ObjectIdentity
pm10010ulhtraps = _Pm10010ulhtraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 10)
)


class _Pm10010ulhtrapPortNumber_Type(Integer32):
    """Custom type pm10010ulhtrapPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm10010ulhtrapPortNumber_Type.__name__ = "Integer32"
_Pm10010ulhtrapPortNumber_Object = MibScalar
pm10010ulhtrapPortNumber = _Pm10010ulhtrapPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 10, 2),
    _Pm10010ulhtrapPortNumber_Type()
)
pm10010ulhtrapPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhtrapPortNumber.setStatus("current")


class _Pm10010ulhtrapLineNumber_Type(Integer32):
    """Custom type pm10010ulhtrapLineNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm10010ulhtrapLineNumber_Type.__name__ = "Integer32"
_Pm10010ulhtrapLineNumber_Object = MibScalar
pm10010ulhtrapLineNumber = _Pm10010ulhtrapLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 10, 3),
    _Pm10010ulhtrapLineNumber_Type()
)
pm10010ulhtrapLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhtrapLineNumber.setStatus("current")


class _Pm10010ulhtrapBoardNumber_Type(Integer32):
    """Custom type pm10010ulhtrapBoardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm10010ulhtrapBoardNumber_Type.__name__ = "Integer32"
_Pm10010ulhtrapBoardNumber_Object = MibScalar
pm10010ulhtrapBoardNumber = _Pm10010ulhtrapBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 10, 4),
    _Pm10010ulhtrapBoardNumber_Type()
)
pm10010ulhtrapBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhtrapBoardNumber.setStatus("current")
_Pm10010ulhMonitoring_ObjectIdentity = ObjectIdentity
pm10010ulhMonitoring = _Pm10010ulhMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11)
)
_Pm10010ulhMonOther_ObjectIdentity = ObjectIdentity
pm10010ulhMonOther = _Pm10010ulhMonOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 1)
)
_Pm10010ulhMonRmon_ObjectIdentity = ObjectIdentity
pm10010ulhMonRmon = _Pm10010ulhMonRmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 1, 3)
)
_Pm10010ulhMonClient_ObjectIdentity = ObjectIdentity
pm10010ulhMonClient = _Pm10010ulhMonClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2)
)
_Pm10010ulhMonClientRmonCounter_ObjectIdentity = ObjectIdentity
pm10010ulhMonClientRmonCounter = _Pm10010ulhMonClientRmonCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4)
)
_Pm10010ulhMonupRmonBytesCounterClientInputTable_Object = MibTable
pm10010ulhMonupRmonBytesCounterClientInputTable = _Pm10010ulhMonupRmonBytesCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 16)
)
if mibBuilder.loadTexts:
    pm10010ulhMonupRmonBytesCounterClientInputTable.setStatus("current")
_Pm10010ulhMonupRmonBytesCounterClientInputEntry_Object = MibTableRow
pm10010ulhMonupRmonBytesCounterClientInputEntry = _Pm10010ulhMonupRmonBytesCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 16, 1)
)
pm10010ulhMonupRmonBytesCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhMonupRmonBytesCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhMonupRmonBytesCounterClientInputEntry.setStatus("current")


class _Pm10010ulhMonupRmonBytesCounterClientInputIndex_Type(Integer32):
    """Custom type pm10010ulhMonupRmonBytesCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhMonupRmonBytesCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm10010ulhMonupRmonBytesCounterClientInputIndex_Object = MibTableColumn
pm10010ulhMonupRmonBytesCounterClientInputIndex = _Pm10010ulhMonupRmonBytesCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 16, 1, 1),
    _Pm10010ulhMonupRmonBytesCounterClientInputIndex_Type()
)
pm10010ulhMonupRmonBytesCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMonupRmonBytesCounterClientInputIndex.setStatus("current")
_Pm10010ulhMonupRmonBytesCounterClientInputValuePortn_Type = Counter64
_Pm10010ulhMonupRmonBytesCounterClientInputValuePortn_Object = MibTableColumn
pm10010ulhMonupRmonBytesCounterClientInputValuePortn = _Pm10010ulhMonupRmonBytesCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 16, 1, 2),
    _Pm10010ulhMonupRmonBytesCounterClientInputValuePortn_Type()
)
pm10010ulhMonupRmonBytesCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMonupRmonBytesCounterClientInputValuePortn.setStatus("current")
_Pm10010ulhMonupRmonBytesCounterClientInputErrorPortn_Type = EkiOnOff
_Pm10010ulhMonupRmonBytesCounterClientInputErrorPortn_Object = MibTableColumn
pm10010ulhMonupRmonBytesCounterClientInputErrorPortn = _Pm10010ulhMonupRmonBytesCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 16, 1, 3),
    _Pm10010ulhMonupRmonBytesCounterClientInputErrorPortn_Type()
)
pm10010ulhMonupRmonBytesCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMonupRmonBytesCounterClientInputErrorPortn.setStatus("current")
_Pm10010ulhMonupRmonBytesCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm10010ulhMonupRmonBytesCounterClientInputOverloadPortn_Object = MibTableColumn
pm10010ulhMonupRmonBytesCounterClientInputOverloadPortn = _Pm10010ulhMonupRmonBytesCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 16, 1, 4),
    _Pm10010ulhMonupRmonBytesCounterClientInputOverloadPortn_Type()
)
pm10010ulhMonupRmonBytesCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMonupRmonBytesCounterClientInputOverloadPortn.setStatus("current")
_Pm10010ulhMonupRmonCrcErrorsCounterClientInputTable_Object = MibTable
pm10010ulhMonupRmonCrcErrorsCounterClientInputTable = _Pm10010ulhMonupRmonCrcErrorsCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 48)
)
if mibBuilder.loadTexts:
    pm10010ulhMonupRmonCrcErrorsCounterClientInputTable.setStatus("current")
_Pm10010ulhMonupRmonCrcErrorsCounterClientInputEntry_Object = MibTableRow
pm10010ulhMonupRmonCrcErrorsCounterClientInputEntry = _Pm10010ulhMonupRmonCrcErrorsCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 48, 1)
)
pm10010ulhMonupRmonCrcErrorsCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhMonupRmonCrcErrorsCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhMonupRmonCrcErrorsCounterClientInputEntry.setStatus("current")


class _Pm10010ulhMonupRmonCrcErrorsCounterClientInputIndex_Type(Integer32):
    """Custom type pm10010ulhMonupRmonCrcErrorsCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhMonupRmonCrcErrorsCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm10010ulhMonupRmonCrcErrorsCounterClientInputIndex_Object = MibTableColumn
pm10010ulhMonupRmonCrcErrorsCounterClientInputIndex = _Pm10010ulhMonupRmonCrcErrorsCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 48, 1, 1),
    _Pm10010ulhMonupRmonCrcErrorsCounterClientInputIndex_Type()
)
pm10010ulhMonupRmonCrcErrorsCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMonupRmonCrcErrorsCounterClientInputIndex.setStatus("current")
_Pm10010ulhMonupRmonCrcErrorsCounterClientInputValuePortn_Type = Counter64
_Pm10010ulhMonupRmonCrcErrorsCounterClientInputValuePortn_Object = MibTableColumn
pm10010ulhMonupRmonCrcErrorsCounterClientInputValuePortn = _Pm10010ulhMonupRmonCrcErrorsCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 48, 1, 2),
    _Pm10010ulhMonupRmonCrcErrorsCounterClientInputValuePortn_Type()
)
pm10010ulhMonupRmonCrcErrorsCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMonupRmonCrcErrorsCounterClientInputValuePortn.setStatus("current")
_Pm10010ulhMonupRmonCrcErrorsCounterClientInputErrorPortn_Type = EkiOnOff
_Pm10010ulhMonupRmonCrcErrorsCounterClientInputErrorPortn_Object = MibTableColumn
pm10010ulhMonupRmonCrcErrorsCounterClientInputErrorPortn = _Pm10010ulhMonupRmonCrcErrorsCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 48, 1, 3),
    _Pm10010ulhMonupRmonCrcErrorsCounterClientInputErrorPortn_Type()
)
pm10010ulhMonupRmonCrcErrorsCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMonupRmonCrcErrorsCounterClientInputErrorPortn.setStatus("current")
_Pm10010ulhMonupRmonCrcErrorsCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm10010ulhMonupRmonCrcErrorsCounterClientInputOverloadPortn_Object = MibTableColumn
pm10010ulhMonupRmonCrcErrorsCounterClientInputOverloadPortn = _Pm10010ulhMonupRmonCrcErrorsCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 48, 1, 4),
    _Pm10010ulhMonupRmonCrcErrorsCounterClientInputOverloadPortn_Type()
)
pm10010ulhMonupRmonCrcErrorsCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMonupRmonCrcErrorsCounterClientInputOverloadPortn.setStatus("current")
_Pm10010ulhMonupRmonPacketsCounterClientInputTable_Object = MibTable
pm10010ulhMonupRmonPacketsCounterClientInputTable = _Pm10010ulhMonupRmonPacketsCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 80)
)
if mibBuilder.loadTexts:
    pm10010ulhMonupRmonPacketsCounterClientInputTable.setStatus("current")
_Pm10010ulhMonupRmonPacketsCounterClientInputEntry_Object = MibTableRow
pm10010ulhMonupRmonPacketsCounterClientInputEntry = _Pm10010ulhMonupRmonPacketsCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 80, 1)
)
pm10010ulhMonupRmonPacketsCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhMonupRmonPacketsCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhMonupRmonPacketsCounterClientInputEntry.setStatus("current")


class _Pm10010ulhMonupRmonPacketsCounterClientInputIndex_Type(Integer32):
    """Custom type pm10010ulhMonupRmonPacketsCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhMonupRmonPacketsCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm10010ulhMonupRmonPacketsCounterClientInputIndex_Object = MibTableColumn
pm10010ulhMonupRmonPacketsCounterClientInputIndex = _Pm10010ulhMonupRmonPacketsCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 80, 1, 1),
    _Pm10010ulhMonupRmonPacketsCounterClientInputIndex_Type()
)
pm10010ulhMonupRmonPacketsCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMonupRmonPacketsCounterClientInputIndex.setStatus("current")
_Pm10010ulhMonupRmonPacketsCounterClientInputValuePortn_Type = Counter64
_Pm10010ulhMonupRmonPacketsCounterClientInputValuePortn_Object = MibTableColumn
pm10010ulhMonupRmonPacketsCounterClientInputValuePortn = _Pm10010ulhMonupRmonPacketsCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 80, 1, 2),
    _Pm10010ulhMonupRmonPacketsCounterClientInputValuePortn_Type()
)
pm10010ulhMonupRmonPacketsCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMonupRmonPacketsCounterClientInputValuePortn.setStatus("current")
_Pm10010ulhMonupRmonPacketsCounterClientInputErrorPortn_Type = EkiOnOff
_Pm10010ulhMonupRmonPacketsCounterClientInputErrorPortn_Object = MibTableColumn
pm10010ulhMonupRmonPacketsCounterClientInputErrorPortn = _Pm10010ulhMonupRmonPacketsCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 80, 1, 3),
    _Pm10010ulhMonupRmonPacketsCounterClientInputErrorPortn_Type()
)
pm10010ulhMonupRmonPacketsCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMonupRmonPacketsCounterClientInputErrorPortn.setStatus("current")
_Pm10010ulhMonupRmonPacketsCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm10010ulhMonupRmonPacketsCounterClientInputOverloadPortn_Object = MibTableColumn
pm10010ulhMonupRmonPacketsCounterClientInputOverloadPortn = _Pm10010ulhMonupRmonPacketsCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 80, 1, 4),
    _Pm10010ulhMonupRmonPacketsCounterClientInputOverloadPortn_Type()
)
pm10010ulhMonupRmonPacketsCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMonupRmonPacketsCounterClientInputOverloadPortn.setStatus("current")
_Pm10010ulhMonupRmonBroadcastCounterClientInputTable_Object = MibTable
pm10010ulhMonupRmonBroadcastCounterClientInputTable = _Pm10010ulhMonupRmonBroadcastCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 112)
)
if mibBuilder.loadTexts:
    pm10010ulhMonupRmonBroadcastCounterClientInputTable.setStatus("current")
_Pm10010ulhMonupRmonBroadcastCounterClientInputEntry_Object = MibTableRow
pm10010ulhMonupRmonBroadcastCounterClientInputEntry = _Pm10010ulhMonupRmonBroadcastCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 112, 1)
)
pm10010ulhMonupRmonBroadcastCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhMonupRmonBroadcastCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhMonupRmonBroadcastCounterClientInputEntry.setStatus("current")


class _Pm10010ulhMonupRmonBroadcastCounterClientInputIndex_Type(Integer32):
    """Custom type pm10010ulhMonupRmonBroadcastCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhMonupRmonBroadcastCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm10010ulhMonupRmonBroadcastCounterClientInputIndex_Object = MibTableColumn
pm10010ulhMonupRmonBroadcastCounterClientInputIndex = _Pm10010ulhMonupRmonBroadcastCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 112, 1, 1),
    _Pm10010ulhMonupRmonBroadcastCounterClientInputIndex_Type()
)
pm10010ulhMonupRmonBroadcastCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMonupRmonBroadcastCounterClientInputIndex.setStatus("current")
_Pm10010ulhMonupRmonBroadcastCounterClientInputValuePortn_Type = Counter64
_Pm10010ulhMonupRmonBroadcastCounterClientInputValuePortn_Object = MibTableColumn
pm10010ulhMonupRmonBroadcastCounterClientInputValuePortn = _Pm10010ulhMonupRmonBroadcastCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 112, 1, 2),
    _Pm10010ulhMonupRmonBroadcastCounterClientInputValuePortn_Type()
)
pm10010ulhMonupRmonBroadcastCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMonupRmonBroadcastCounterClientInputValuePortn.setStatus("current")
_Pm10010ulhMonupRmonBroadcastCounterClientInputErrorPortn_Type = EkiOnOff
_Pm10010ulhMonupRmonBroadcastCounterClientInputErrorPortn_Object = MibTableColumn
pm10010ulhMonupRmonBroadcastCounterClientInputErrorPortn = _Pm10010ulhMonupRmonBroadcastCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 112, 1, 3),
    _Pm10010ulhMonupRmonBroadcastCounterClientInputErrorPortn_Type()
)
pm10010ulhMonupRmonBroadcastCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMonupRmonBroadcastCounterClientInputErrorPortn.setStatus("current")
_Pm10010ulhMonupRmonBroadcastCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm10010ulhMonupRmonBroadcastCounterClientInputOverloadPortn_Object = MibTableColumn
pm10010ulhMonupRmonBroadcastCounterClientInputOverloadPortn = _Pm10010ulhMonupRmonBroadcastCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 112, 1, 4),
    _Pm10010ulhMonupRmonBroadcastCounterClientInputOverloadPortn_Type()
)
pm10010ulhMonupRmonBroadcastCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMonupRmonBroadcastCounterClientInputOverloadPortn.setStatus("current")
_Pm10010ulhMonupRmonMulticastCounterClientInputTable_Object = MibTable
pm10010ulhMonupRmonMulticastCounterClientInputTable = _Pm10010ulhMonupRmonMulticastCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 144)
)
if mibBuilder.loadTexts:
    pm10010ulhMonupRmonMulticastCounterClientInputTable.setStatus("current")
_Pm10010ulhMonupRmonMulticastCounterClientInputEntry_Object = MibTableRow
pm10010ulhMonupRmonMulticastCounterClientInputEntry = _Pm10010ulhMonupRmonMulticastCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 144, 1)
)
pm10010ulhMonupRmonMulticastCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhMonupRmonMulticastCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhMonupRmonMulticastCounterClientInputEntry.setStatus("current")


class _Pm10010ulhMonupRmonMulticastCounterClientInputIndex_Type(Integer32):
    """Custom type pm10010ulhMonupRmonMulticastCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhMonupRmonMulticastCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm10010ulhMonupRmonMulticastCounterClientInputIndex_Object = MibTableColumn
pm10010ulhMonupRmonMulticastCounterClientInputIndex = _Pm10010ulhMonupRmonMulticastCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 144, 1, 1),
    _Pm10010ulhMonupRmonMulticastCounterClientInputIndex_Type()
)
pm10010ulhMonupRmonMulticastCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMonupRmonMulticastCounterClientInputIndex.setStatus("current")
_Pm10010ulhMonupRmonMulticastCounterClientInputValuePortn_Type = Counter64
_Pm10010ulhMonupRmonMulticastCounterClientInputValuePortn_Object = MibTableColumn
pm10010ulhMonupRmonMulticastCounterClientInputValuePortn = _Pm10010ulhMonupRmonMulticastCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 144, 1, 2),
    _Pm10010ulhMonupRmonMulticastCounterClientInputValuePortn_Type()
)
pm10010ulhMonupRmonMulticastCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMonupRmonMulticastCounterClientInputValuePortn.setStatus("current")
_Pm10010ulhMonupRmonMulticastCounterClientInputErrorPortn_Type = EkiOnOff
_Pm10010ulhMonupRmonMulticastCounterClientInputErrorPortn_Object = MibTableColumn
pm10010ulhMonupRmonMulticastCounterClientInputErrorPortn = _Pm10010ulhMonupRmonMulticastCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 144, 1, 3),
    _Pm10010ulhMonupRmonMulticastCounterClientInputErrorPortn_Type()
)
pm10010ulhMonupRmonMulticastCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMonupRmonMulticastCounterClientInputErrorPortn.setStatus("current")
_Pm10010ulhMonupRmonMulticastCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm10010ulhMonupRmonMulticastCounterClientInputOverloadPortn_Object = MibTableColumn
pm10010ulhMonupRmonMulticastCounterClientInputOverloadPortn = _Pm10010ulhMonupRmonMulticastCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 144, 1, 4),
    _Pm10010ulhMonupRmonMulticastCounterClientInputOverloadPortn_Type()
)
pm10010ulhMonupRmonMulticastCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMonupRmonMulticastCounterClientInputOverloadPortn.setStatus("current")
_Pm10010ulhMonupRmonPauseFrameCounterClientInputTable_Object = MibTable
pm10010ulhMonupRmonPauseFrameCounterClientInputTable = _Pm10010ulhMonupRmonPauseFrameCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 176)
)
if mibBuilder.loadTexts:
    pm10010ulhMonupRmonPauseFrameCounterClientInputTable.setStatus("current")
_Pm10010ulhMonupRmonPauseFrameCounterClientInputEntry_Object = MibTableRow
pm10010ulhMonupRmonPauseFrameCounterClientInputEntry = _Pm10010ulhMonupRmonPauseFrameCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 176, 1)
)
pm10010ulhMonupRmonPauseFrameCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhMonupRmonPauseFrameCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhMonupRmonPauseFrameCounterClientInputEntry.setStatus("current")


class _Pm10010ulhMonupRmonPauseFrameCounterClientInputIndex_Type(Integer32):
    """Custom type pm10010ulhMonupRmonPauseFrameCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhMonupRmonPauseFrameCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm10010ulhMonupRmonPauseFrameCounterClientInputIndex_Object = MibTableColumn
pm10010ulhMonupRmonPauseFrameCounterClientInputIndex = _Pm10010ulhMonupRmonPauseFrameCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 176, 1, 1),
    _Pm10010ulhMonupRmonPauseFrameCounterClientInputIndex_Type()
)
pm10010ulhMonupRmonPauseFrameCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMonupRmonPauseFrameCounterClientInputIndex.setStatus("current")
_Pm10010ulhMonupRmonPauseFrameCounterClientInputValuePortn_Type = Counter64
_Pm10010ulhMonupRmonPauseFrameCounterClientInputValuePortn_Object = MibTableColumn
pm10010ulhMonupRmonPauseFrameCounterClientInputValuePortn = _Pm10010ulhMonupRmonPauseFrameCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 176, 1, 2),
    _Pm10010ulhMonupRmonPauseFrameCounterClientInputValuePortn_Type()
)
pm10010ulhMonupRmonPauseFrameCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMonupRmonPauseFrameCounterClientInputValuePortn.setStatus("current")
_Pm10010ulhMonupRmonPauseFrameCounterClientInputErrorPortn_Type = EkiOnOff
_Pm10010ulhMonupRmonPauseFrameCounterClientInputErrorPortn_Object = MibTableColumn
pm10010ulhMonupRmonPauseFrameCounterClientInputErrorPortn = _Pm10010ulhMonupRmonPauseFrameCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 176, 1, 3),
    _Pm10010ulhMonupRmonPauseFrameCounterClientInputErrorPortn_Type()
)
pm10010ulhMonupRmonPauseFrameCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMonupRmonPauseFrameCounterClientInputErrorPortn.setStatus("current")
_Pm10010ulhMonupRmonPauseFrameCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm10010ulhMonupRmonPauseFrameCounterClientInputOverloadPortn_Object = MibTableColumn
pm10010ulhMonupRmonPauseFrameCounterClientInputOverloadPortn = _Pm10010ulhMonupRmonPauseFrameCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 176, 1, 4),
    _Pm10010ulhMonupRmonPauseFrameCounterClientInputOverloadPortn_Type()
)
pm10010ulhMonupRmonPauseFrameCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMonupRmonPauseFrameCounterClientInputOverloadPortn.setStatus("current")
_Pm10010ulhMonupRmonUnicastCounterClientInputTable_Object = MibTable
pm10010ulhMonupRmonUnicastCounterClientInputTable = _Pm10010ulhMonupRmonUnicastCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 304)
)
if mibBuilder.loadTexts:
    pm10010ulhMonupRmonUnicastCounterClientInputTable.setStatus("current")
_Pm10010ulhMonupRmonUnicastCounterClientInputEntry_Object = MibTableRow
pm10010ulhMonupRmonUnicastCounterClientInputEntry = _Pm10010ulhMonupRmonUnicastCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 304, 1)
)
pm10010ulhMonupRmonUnicastCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhMonupRmonUnicastCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhMonupRmonUnicastCounterClientInputEntry.setStatus("current")


class _Pm10010ulhMonupRmonUnicastCounterClientInputIndex_Type(Integer32):
    """Custom type pm10010ulhMonupRmonUnicastCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhMonupRmonUnicastCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm10010ulhMonupRmonUnicastCounterClientInputIndex_Object = MibTableColumn
pm10010ulhMonupRmonUnicastCounterClientInputIndex = _Pm10010ulhMonupRmonUnicastCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 304, 1, 1),
    _Pm10010ulhMonupRmonUnicastCounterClientInputIndex_Type()
)
pm10010ulhMonupRmonUnicastCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMonupRmonUnicastCounterClientInputIndex.setStatus("current")
_Pm10010ulhMonupRmonUnicastCounterClientInputValuePortn_Type = Counter64
_Pm10010ulhMonupRmonUnicastCounterClientInputValuePortn_Object = MibTableColumn
pm10010ulhMonupRmonUnicastCounterClientInputValuePortn = _Pm10010ulhMonupRmonUnicastCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 304, 1, 2),
    _Pm10010ulhMonupRmonUnicastCounterClientInputValuePortn_Type()
)
pm10010ulhMonupRmonUnicastCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMonupRmonUnicastCounterClientInputValuePortn.setStatus("current")
_Pm10010ulhMonupRmonUnicastCounterClientInputErrorPortn_Type = EkiOnOff
_Pm10010ulhMonupRmonUnicastCounterClientInputErrorPortn_Object = MibTableColumn
pm10010ulhMonupRmonUnicastCounterClientInputErrorPortn = _Pm10010ulhMonupRmonUnicastCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 304, 1, 3),
    _Pm10010ulhMonupRmonUnicastCounterClientInputErrorPortn_Type()
)
pm10010ulhMonupRmonUnicastCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMonupRmonUnicastCounterClientInputErrorPortn.setStatus("current")
_Pm10010ulhMonupRmonUnicastCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm10010ulhMonupRmonUnicastCounterClientInputOverloadPortn_Object = MibTableColumn
pm10010ulhMonupRmonUnicastCounterClientInputOverloadPortn = _Pm10010ulhMonupRmonUnicastCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 304, 1, 4),
    _Pm10010ulhMonupRmonUnicastCounterClientInputOverloadPortn_Type()
)
pm10010ulhMonupRmonUnicastCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMonupRmonUnicastCounterClientInputOverloadPortn.setStatus("current")
_Pm10010ulhMonupRmonNonunicastCounterClientInputTable_Object = MibTable
pm10010ulhMonupRmonNonunicastCounterClientInputTable = _Pm10010ulhMonupRmonNonunicastCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 336)
)
if mibBuilder.loadTexts:
    pm10010ulhMonupRmonNonunicastCounterClientInputTable.setStatus("current")
_Pm10010ulhMonupRmonNonunicastCounterClientInputEntry_Object = MibTableRow
pm10010ulhMonupRmonNonunicastCounterClientInputEntry = _Pm10010ulhMonupRmonNonunicastCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 336, 1)
)
pm10010ulhMonupRmonNonunicastCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhMonupRmonNonunicastCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhMonupRmonNonunicastCounterClientInputEntry.setStatus("current")


class _Pm10010ulhMonupRmonNonunicastCounterClientInputIndex_Type(Integer32):
    """Custom type pm10010ulhMonupRmonNonunicastCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhMonupRmonNonunicastCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm10010ulhMonupRmonNonunicastCounterClientInputIndex_Object = MibTableColumn
pm10010ulhMonupRmonNonunicastCounterClientInputIndex = _Pm10010ulhMonupRmonNonunicastCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 336, 1, 1),
    _Pm10010ulhMonupRmonNonunicastCounterClientInputIndex_Type()
)
pm10010ulhMonupRmonNonunicastCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMonupRmonNonunicastCounterClientInputIndex.setStatus("current")
_Pm10010ulhMonupRmonNonunicastCounterClientInputValuePortn_Type = Counter64
_Pm10010ulhMonupRmonNonunicastCounterClientInputValuePortn_Object = MibTableColumn
pm10010ulhMonupRmonNonunicastCounterClientInputValuePortn = _Pm10010ulhMonupRmonNonunicastCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 336, 1, 2),
    _Pm10010ulhMonupRmonNonunicastCounterClientInputValuePortn_Type()
)
pm10010ulhMonupRmonNonunicastCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMonupRmonNonunicastCounterClientInputValuePortn.setStatus("current")
_Pm10010ulhMonupRmonNonunicastCounterClientInputErrorPortn_Type = EkiOnOff
_Pm10010ulhMonupRmonNonunicastCounterClientInputErrorPortn_Object = MibTableColumn
pm10010ulhMonupRmonNonunicastCounterClientInputErrorPortn = _Pm10010ulhMonupRmonNonunicastCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 336, 1, 3),
    _Pm10010ulhMonupRmonNonunicastCounterClientInputErrorPortn_Type()
)
pm10010ulhMonupRmonNonunicastCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMonupRmonNonunicastCounterClientInputErrorPortn.setStatus("current")
_Pm10010ulhMonupRmonNonunicastCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm10010ulhMonupRmonNonunicastCounterClientInputOverloadPortn_Object = MibTableColumn
pm10010ulhMonupRmonNonunicastCounterClientInputOverloadPortn = _Pm10010ulhMonupRmonNonunicastCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 336, 1, 4),
    _Pm10010ulhMonupRmonNonunicastCounterClientInputOverloadPortn_Type()
)
pm10010ulhMonupRmonNonunicastCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMonupRmonNonunicastCounterClientInputOverloadPortn.setStatus("current")
_Pm10010ulhMondownRmonBytesCounterClientOutputTable_Object = MibTable
pm10010ulhMondownRmonBytesCounterClientOutputTable = _Pm10010ulhMondownRmonBytesCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 400)
)
if mibBuilder.loadTexts:
    pm10010ulhMondownRmonBytesCounterClientOutputTable.setStatus("current")
_Pm10010ulhMondownRmonBytesCounterClientOutputEntry_Object = MibTableRow
pm10010ulhMondownRmonBytesCounterClientOutputEntry = _Pm10010ulhMondownRmonBytesCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 400, 1)
)
pm10010ulhMondownRmonBytesCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhMondownRmonBytesCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhMondownRmonBytesCounterClientOutputEntry.setStatus("current")


class _Pm10010ulhMondownRmonBytesCounterClientOutputIndex_Type(Integer32):
    """Custom type pm10010ulhMondownRmonBytesCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhMondownRmonBytesCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pm10010ulhMondownRmonBytesCounterClientOutputIndex_Object = MibTableColumn
pm10010ulhMondownRmonBytesCounterClientOutputIndex = _Pm10010ulhMondownRmonBytesCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 400, 1, 1),
    _Pm10010ulhMondownRmonBytesCounterClientOutputIndex_Type()
)
pm10010ulhMondownRmonBytesCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMondownRmonBytesCounterClientOutputIndex.setStatus("current")
_Pm10010ulhMondownRmonBytesCounterClientOutputValuePortn_Type = Counter64
_Pm10010ulhMondownRmonBytesCounterClientOutputValuePortn_Object = MibTableColumn
pm10010ulhMondownRmonBytesCounterClientOutputValuePortn = _Pm10010ulhMondownRmonBytesCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 400, 1, 2),
    _Pm10010ulhMondownRmonBytesCounterClientOutputValuePortn_Type()
)
pm10010ulhMondownRmonBytesCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMondownRmonBytesCounterClientOutputValuePortn.setStatus("current")
_Pm10010ulhMondownRmonBytesCounterClientOutputErrorPortn_Type = EkiOnOff
_Pm10010ulhMondownRmonBytesCounterClientOutputErrorPortn_Object = MibTableColumn
pm10010ulhMondownRmonBytesCounterClientOutputErrorPortn = _Pm10010ulhMondownRmonBytesCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 400, 1, 3),
    _Pm10010ulhMondownRmonBytesCounterClientOutputErrorPortn_Type()
)
pm10010ulhMondownRmonBytesCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMondownRmonBytesCounterClientOutputErrorPortn.setStatus("current")
_Pm10010ulhMondownRmonBytesCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pm10010ulhMondownRmonBytesCounterClientOutputOverloadPortn_Object = MibTableColumn
pm10010ulhMondownRmonBytesCounterClientOutputOverloadPortn = _Pm10010ulhMondownRmonBytesCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 400, 1, 4),
    _Pm10010ulhMondownRmonBytesCounterClientOutputOverloadPortn_Type()
)
pm10010ulhMondownRmonBytesCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMondownRmonBytesCounterClientOutputOverloadPortn.setStatus("current")
_Pm10010ulhMondownRmonCrcErrorsCounterClientOutputTable_Object = MibTable
pm10010ulhMondownRmonCrcErrorsCounterClientOutputTable = _Pm10010ulhMondownRmonCrcErrorsCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 432)
)
if mibBuilder.loadTexts:
    pm10010ulhMondownRmonCrcErrorsCounterClientOutputTable.setStatus("current")
_Pm10010ulhMondownRmonCrcErrorsCounterClientOutputEntry_Object = MibTableRow
pm10010ulhMondownRmonCrcErrorsCounterClientOutputEntry = _Pm10010ulhMondownRmonCrcErrorsCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 432, 1)
)
pm10010ulhMondownRmonCrcErrorsCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhMondownRmonCrcErrorsCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhMondownRmonCrcErrorsCounterClientOutputEntry.setStatus("current")


class _Pm10010ulhMondownRmonCrcErrorsCounterClientOutputIndex_Type(Integer32):
    """Custom type pm10010ulhMondownRmonCrcErrorsCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhMondownRmonCrcErrorsCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pm10010ulhMondownRmonCrcErrorsCounterClientOutputIndex_Object = MibTableColumn
pm10010ulhMondownRmonCrcErrorsCounterClientOutputIndex = _Pm10010ulhMondownRmonCrcErrorsCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 432, 1, 1),
    _Pm10010ulhMondownRmonCrcErrorsCounterClientOutputIndex_Type()
)
pm10010ulhMondownRmonCrcErrorsCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMondownRmonCrcErrorsCounterClientOutputIndex.setStatus("current")
_Pm10010ulhMondownRmonCrcErrorsCounterClientOutputValuePortn_Type = Counter64
_Pm10010ulhMondownRmonCrcErrorsCounterClientOutputValuePortn_Object = MibTableColumn
pm10010ulhMondownRmonCrcErrorsCounterClientOutputValuePortn = _Pm10010ulhMondownRmonCrcErrorsCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 432, 1, 2),
    _Pm10010ulhMondownRmonCrcErrorsCounterClientOutputValuePortn_Type()
)
pm10010ulhMondownRmonCrcErrorsCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMondownRmonCrcErrorsCounterClientOutputValuePortn.setStatus("current")
_Pm10010ulhMondownRmonCrcErrorsCounterClientOutputErrorPortn_Type = EkiOnOff
_Pm10010ulhMondownRmonCrcErrorsCounterClientOutputErrorPortn_Object = MibTableColumn
pm10010ulhMondownRmonCrcErrorsCounterClientOutputErrorPortn = _Pm10010ulhMondownRmonCrcErrorsCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 432, 1, 3),
    _Pm10010ulhMondownRmonCrcErrorsCounterClientOutputErrorPortn_Type()
)
pm10010ulhMondownRmonCrcErrorsCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMondownRmonCrcErrorsCounterClientOutputErrorPortn.setStatus("current")
_Pm10010ulhMondownRmonCrcErrorsCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pm10010ulhMondownRmonCrcErrorsCounterClientOutputOverloadPortn_Object = MibTableColumn
pm10010ulhMondownRmonCrcErrorsCounterClientOutputOverloadPortn = _Pm10010ulhMondownRmonCrcErrorsCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 432, 1, 4),
    _Pm10010ulhMondownRmonCrcErrorsCounterClientOutputOverloadPortn_Type()
)
pm10010ulhMondownRmonCrcErrorsCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMondownRmonCrcErrorsCounterClientOutputOverloadPortn.setStatus("current")
_Pm10010ulhMondownRmonPacketsCounterClientOutputTable_Object = MibTable
pm10010ulhMondownRmonPacketsCounterClientOutputTable = _Pm10010ulhMondownRmonPacketsCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 464)
)
if mibBuilder.loadTexts:
    pm10010ulhMondownRmonPacketsCounterClientOutputTable.setStatus("current")
_Pm10010ulhMondownRmonPacketsCounterClientOutputEntry_Object = MibTableRow
pm10010ulhMondownRmonPacketsCounterClientOutputEntry = _Pm10010ulhMondownRmonPacketsCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 464, 1)
)
pm10010ulhMondownRmonPacketsCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhMondownRmonPacketsCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhMondownRmonPacketsCounterClientOutputEntry.setStatus("current")


class _Pm10010ulhMondownRmonPacketsCounterClientOutputIndex_Type(Integer32):
    """Custom type pm10010ulhMondownRmonPacketsCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhMondownRmonPacketsCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pm10010ulhMondownRmonPacketsCounterClientOutputIndex_Object = MibTableColumn
pm10010ulhMondownRmonPacketsCounterClientOutputIndex = _Pm10010ulhMondownRmonPacketsCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 464, 1, 1),
    _Pm10010ulhMondownRmonPacketsCounterClientOutputIndex_Type()
)
pm10010ulhMondownRmonPacketsCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMondownRmonPacketsCounterClientOutputIndex.setStatus("current")
_Pm10010ulhMondownRmonPacketsCounterClientOutputValuePortn_Type = Counter64
_Pm10010ulhMondownRmonPacketsCounterClientOutputValuePortn_Object = MibTableColumn
pm10010ulhMondownRmonPacketsCounterClientOutputValuePortn = _Pm10010ulhMondownRmonPacketsCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 464, 1, 2),
    _Pm10010ulhMondownRmonPacketsCounterClientOutputValuePortn_Type()
)
pm10010ulhMondownRmonPacketsCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMondownRmonPacketsCounterClientOutputValuePortn.setStatus("current")
_Pm10010ulhMondownRmonPacketsCounterClientOutputErrorPortn_Type = EkiOnOff
_Pm10010ulhMondownRmonPacketsCounterClientOutputErrorPortn_Object = MibTableColumn
pm10010ulhMondownRmonPacketsCounterClientOutputErrorPortn = _Pm10010ulhMondownRmonPacketsCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 464, 1, 3),
    _Pm10010ulhMondownRmonPacketsCounterClientOutputErrorPortn_Type()
)
pm10010ulhMondownRmonPacketsCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMondownRmonPacketsCounterClientOutputErrorPortn.setStatus("current")
_Pm10010ulhMondownRmonPacketsCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pm10010ulhMondownRmonPacketsCounterClientOutputOverloadPortn_Object = MibTableColumn
pm10010ulhMondownRmonPacketsCounterClientOutputOverloadPortn = _Pm10010ulhMondownRmonPacketsCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 464, 1, 4),
    _Pm10010ulhMondownRmonPacketsCounterClientOutputOverloadPortn_Type()
)
pm10010ulhMondownRmonPacketsCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMondownRmonPacketsCounterClientOutputOverloadPortn.setStatus("current")
_Pm10010ulhMondownRmonBroadcastCounterClientOutputTable_Object = MibTable
pm10010ulhMondownRmonBroadcastCounterClientOutputTable = _Pm10010ulhMondownRmonBroadcastCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 496)
)
if mibBuilder.loadTexts:
    pm10010ulhMondownRmonBroadcastCounterClientOutputTable.setStatus("current")
_Pm10010ulhMondownRmonBroadcastCounterClientOutputEntry_Object = MibTableRow
pm10010ulhMondownRmonBroadcastCounterClientOutputEntry = _Pm10010ulhMondownRmonBroadcastCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 496, 1)
)
pm10010ulhMondownRmonBroadcastCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhMondownRmonBroadcastCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhMondownRmonBroadcastCounterClientOutputEntry.setStatus("current")


class _Pm10010ulhMondownRmonBroadcastCounterClientOutputIndex_Type(Integer32):
    """Custom type pm10010ulhMondownRmonBroadcastCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhMondownRmonBroadcastCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pm10010ulhMondownRmonBroadcastCounterClientOutputIndex_Object = MibTableColumn
pm10010ulhMondownRmonBroadcastCounterClientOutputIndex = _Pm10010ulhMondownRmonBroadcastCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 496, 1, 1),
    _Pm10010ulhMondownRmonBroadcastCounterClientOutputIndex_Type()
)
pm10010ulhMondownRmonBroadcastCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMondownRmonBroadcastCounterClientOutputIndex.setStatus("current")
_Pm10010ulhMondownRmonBroadcastCounterClientOutputValuePortn_Type = Counter64
_Pm10010ulhMondownRmonBroadcastCounterClientOutputValuePortn_Object = MibTableColumn
pm10010ulhMondownRmonBroadcastCounterClientOutputValuePortn = _Pm10010ulhMondownRmonBroadcastCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 496, 1, 2),
    _Pm10010ulhMondownRmonBroadcastCounterClientOutputValuePortn_Type()
)
pm10010ulhMondownRmonBroadcastCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMondownRmonBroadcastCounterClientOutputValuePortn.setStatus("current")
_Pm10010ulhMondownRmonBroadcastCounterClientOutputErrorPortn_Type = EkiOnOff
_Pm10010ulhMondownRmonBroadcastCounterClientOutputErrorPortn_Object = MibTableColumn
pm10010ulhMondownRmonBroadcastCounterClientOutputErrorPortn = _Pm10010ulhMondownRmonBroadcastCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 496, 1, 3),
    _Pm10010ulhMondownRmonBroadcastCounterClientOutputErrorPortn_Type()
)
pm10010ulhMondownRmonBroadcastCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMondownRmonBroadcastCounterClientOutputErrorPortn.setStatus("current")
_Pm10010ulhMondownRmonBroadcastCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pm10010ulhMondownRmonBroadcastCounterClientOutputOverloadPortn_Object = MibTableColumn
pm10010ulhMondownRmonBroadcastCounterClientOutputOverloadPortn = _Pm10010ulhMondownRmonBroadcastCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 496, 1, 4),
    _Pm10010ulhMondownRmonBroadcastCounterClientOutputOverloadPortn_Type()
)
pm10010ulhMondownRmonBroadcastCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMondownRmonBroadcastCounterClientOutputOverloadPortn.setStatus("current")
_Pm10010ulhMondownRmonMulticastCounterClientOutputTable_Object = MibTable
pm10010ulhMondownRmonMulticastCounterClientOutputTable = _Pm10010ulhMondownRmonMulticastCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 528)
)
if mibBuilder.loadTexts:
    pm10010ulhMondownRmonMulticastCounterClientOutputTable.setStatus("current")
_Pm10010ulhMondownRmonMulticastCounterClientOutputEntry_Object = MibTableRow
pm10010ulhMondownRmonMulticastCounterClientOutputEntry = _Pm10010ulhMondownRmonMulticastCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 528, 1)
)
pm10010ulhMondownRmonMulticastCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhMondownRmonMulticastCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhMondownRmonMulticastCounterClientOutputEntry.setStatus("current")


class _Pm10010ulhMondownRmonMulticastCounterClientOutputIndex_Type(Integer32):
    """Custom type pm10010ulhMondownRmonMulticastCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhMondownRmonMulticastCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pm10010ulhMondownRmonMulticastCounterClientOutputIndex_Object = MibTableColumn
pm10010ulhMondownRmonMulticastCounterClientOutputIndex = _Pm10010ulhMondownRmonMulticastCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 528, 1, 1),
    _Pm10010ulhMondownRmonMulticastCounterClientOutputIndex_Type()
)
pm10010ulhMondownRmonMulticastCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMondownRmonMulticastCounterClientOutputIndex.setStatus("current")
_Pm10010ulhMondownRmonMulticastCounterClientOutputValuePortn_Type = Counter64
_Pm10010ulhMondownRmonMulticastCounterClientOutputValuePortn_Object = MibTableColumn
pm10010ulhMondownRmonMulticastCounterClientOutputValuePortn = _Pm10010ulhMondownRmonMulticastCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 528, 1, 2),
    _Pm10010ulhMondownRmonMulticastCounterClientOutputValuePortn_Type()
)
pm10010ulhMondownRmonMulticastCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMondownRmonMulticastCounterClientOutputValuePortn.setStatus("current")
_Pm10010ulhMondownRmonMulticastCounterClientOutputErrorPortn_Type = EkiOnOff
_Pm10010ulhMondownRmonMulticastCounterClientOutputErrorPortn_Object = MibTableColumn
pm10010ulhMondownRmonMulticastCounterClientOutputErrorPortn = _Pm10010ulhMondownRmonMulticastCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 528, 1, 3),
    _Pm10010ulhMondownRmonMulticastCounterClientOutputErrorPortn_Type()
)
pm10010ulhMondownRmonMulticastCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMondownRmonMulticastCounterClientOutputErrorPortn.setStatus("current")
_Pm10010ulhMondownRmonMulticastCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pm10010ulhMondownRmonMulticastCounterClientOutputOverloadPortn_Object = MibTableColumn
pm10010ulhMondownRmonMulticastCounterClientOutputOverloadPortn = _Pm10010ulhMondownRmonMulticastCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 528, 1, 4),
    _Pm10010ulhMondownRmonMulticastCounterClientOutputOverloadPortn_Type()
)
pm10010ulhMondownRmonMulticastCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMondownRmonMulticastCounterClientOutputOverloadPortn.setStatus("current")
_Pm10010ulhMondownRmonPauseFrameCounterClientOutputTable_Object = MibTable
pm10010ulhMondownRmonPauseFrameCounterClientOutputTable = _Pm10010ulhMondownRmonPauseFrameCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 560)
)
if mibBuilder.loadTexts:
    pm10010ulhMondownRmonPauseFrameCounterClientOutputTable.setStatus("current")
_Pm10010ulhMondownRmonPauseFrameCounterClientOutputEntry_Object = MibTableRow
pm10010ulhMondownRmonPauseFrameCounterClientOutputEntry = _Pm10010ulhMondownRmonPauseFrameCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 560, 1)
)
pm10010ulhMondownRmonPauseFrameCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhMondownRmonPauseFrameCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhMondownRmonPauseFrameCounterClientOutputEntry.setStatus("current")


class _Pm10010ulhMondownRmonPauseFrameCounterClientOutputIndex_Type(Integer32):
    """Custom type pm10010ulhMondownRmonPauseFrameCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhMondownRmonPauseFrameCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pm10010ulhMondownRmonPauseFrameCounterClientOutputIndex_Object = MibTableColumn
pm10010ulhMondownRmonPauseFrameCounterClientOutputIndex = _Pm10010ulhMondownRmonPauseFrameCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 560, 1, 1),
    _Pm10010ulhMondownRmonPauseFrameCounterClientOutputIndex_Type()
)
pm10010ulhMondownRmonPauseFrameCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMondownRmonPauseFrameCounterClientOutputIndex.setStatus("current")
_Pm10010ulhMondownRmonPauseFrameCounterClientOutputValuePortn_Type = Counter64
_Pm10010ulhMondownRmonPauseFrameCounterClientOutputValuePortn_Object = MibTableColumn
pm10010ulhMondownRmonPauseFrameCounterClientOutputValuePortn = _Pm10010ulhMondownRmonPauseFrameCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 560, 1, 2),
    _Pm10010ulhMondownRmonPauseFrameCounterClientOutputValuePortn_Type()
)
pm10010ulhMondownRmonPauseFrameCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMondownRmonPauseFrameCounterClientOutputValuePortn.setStatus("current")
_Pm10010ulhMondownRmonPauseFrameCounterClientOutputErrorPortn_Type = EkiOnOff
_Pm10010ulhMondownRmonPauseFrameCounterClientOutputErrorPortn_Object = MibTableColumn
pm10010ulhMondownRmonPauseFrameCounterClientOutputErrorPortn = _Pm10010ulhMondownRmonPauseFrameCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 560, 1, 3),
    _Pm10010ulhMondownRmonPauseFrameCounterClientOutputErrorPortn_Type()
)
pm10010ulhMondownRmonPauseFrameCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMondownRmonPauseFrameCounterClientOutputErrorPortn.setStatus("current")
_Pm10010ulhMondownRmonPauseFrameCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pm10010ulhMondownRmonPauseFrameCounterClientOutputOverloadPortn_Object = MibTableColumn
pm10010ulhMondownRmonPauseFrameCounterClientOutputOverloadPortn = _Pm10010ulhMondownRmonPauseFrameCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 560, 1, 4),
    _Pm10010ulhMondownRmonPauseFrameCounterClientOutputOverloadPortn_Type()
)
pm10010ulhMondownRmonPauseFrameCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMondownRmonPauseFrameCounterClientOutputOverloadPortn.setStatus("current")
_Pm10010ulhMondownRmonUnicastCounterClientOutputTable_Object = MibTable
pm10010ulhMondownRmonUnicastCounterClientOutputTable = _Pm10010ulhMondownRmonUnicastCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 688)
)
if mibBuilder.loadTexts:
    pm10010ulhMondownRmonUnicastCounterClientOutputTable.setStatus("current")
_Pm10010ulhMondownRmonUnicastCounterClientOutputEntry_Object = MibTableRow
pm10010ulhMondownRmonUnicastCounterClientOutputEntry = _Pm10010ulhMondownRmonUnicastCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 688, 1)
)
pm10010ulhMondownRmonUnicastCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhMondownRmonUnicastCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhMondownRmonUnicastCounterClientOutputEntry.setStatus("current")


class _Pm10010ulhMondownRmonUnicastCounterClientOutputIndex_Type(Integer32):
    """Custom type pm10010ulhMondownRmonUnicastCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhMondownRmonUnicastCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pm10010ulhMondownRmonUnicastCounterClientOutputIndex_Object = MibTableColumn
pm10010ulhMondownRmonUnicastCounterClientOutputIndex = _Pm10010ulhMondownRmonUnicastCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 688, 1, 1),
    _Pm10010ulhMondownRmonUnicastCounterClientOutputIndex_Type()
)
pm10010ulhMondownRmonUnicastCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMondownRmonUnicastCounterClientOutputIndex.setStatus("current")
_Pm10010ulhMondownRmonUnicastCounterClientOutputValuePortn_Type = Counter64
_Pm10010ulhMondownRmonUnicastCounterClientOutputValuePortn_Object = MibTableColumn
pm10010ulhMondownRmonUnicastCounterClientOutputValuePortn = _Pm10010ulhMondownRmonUnicastCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 688, 1, 2),
    _Pm10010ulhMondownRmonUnicastCounterClientOutputValuePortn_Type()
)
pm10010ulhMondownRmonUnicastCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMondownRmonUnicastCounterClientOutputValuePortn.setStatus("current")
_Pm10010ulhMondownRmonUnicastCounterClientOutputErrorPortn_Type = EkiOnOff
_Pm10010ulhMondownRmonUnicastCounterClientOutputErrorPortn_Object = MibTableColumn
pm10010ulhMondownRmonUnicastCounterClientOutputErrorPortn = _Pm10010ulhMondownRmonUnicastCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 688, 1, 3),
    _Pm10010ulhMondownRmonUnicastCounterClientOutputErrorPortn_Type()
)
pm10010ulhMondownRmonUnicastCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMondownRmonUnicastCounterClientOutputErrorPortn.setStatus("current")
_Pm10010ulhMondownRmonUnicastCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pm10010ulhMondownRmonUnicastCounterClientOutputOverloadPortn_Object = MibTableColumn
pm10010ulhMondownRmonUnicastCounterClientOutputOverloadPortn = _Pm10010ulhMondownRmonUnicastCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 688, 1, 4),
    _Pm10010ulhMondownRmonUnicastCounterClientOutputOverloadPortn_Type()
)
pm10010ulhMondownRmonUnicastCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMondownRmonUnicastCounterClientOutputOverloadPortn.setStatus("current")
_Pm10010ulhMondownRmonNonunicastCounterClientOutputTable_Object = MibTable
pm10010ulhMondownRmonNonunicastCounterClientOutputTable = _Pm10010ulhMondownRmonNonunicastCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 720)
)
if mibBuilder.loadTexts:
    pm10010ulhMondownRmonNonunicastCounterClientOutputTable.setStatus("current")
_Pm10010ulhMondownRmonNonunicastCounterClientOutputEntry_Object = MibTableRow
pm10010ulhMondownRmonNonunicastCounterClientOutputEntry = _Pm10010ulhMondownRmonNonunicastCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 720, 1)
)
pm10010ulhMondownRmonNonunicastCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhMondownRmonNonunicastCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhMondownRmonNonunicastCounterClientOutputEntry.setStatus("current")


class _Pm10010ulhMondownRmonNonunicastCounterClientOutputIndex_Type(Integer32):
    """Custom type pm10010ulhMondownRmonNonunicastCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhMondownRmonNonunicastCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pm10010ulhMondownRmonNonunicastCounterClientOutputIndex_Object = MibTableColumn
pm10010ulhMondownRmonNonunicastCounterClientOutputIndex = _Pm10010ulhMondownRmonNonunicastCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 720, 1, 1),
    _Pm10010ulhMondownRmonNonunicastCounterClientOutputIndex_Type()
)
pm10010ulhMondownRmonNonunicastCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMondownRmonNonunicastCounterClientOutputIndex.setStatus("current")
_Pm10010ulhMondownRmonNonunicastCounterClientOutputValuePortn_Type = Counter64
_Pm10010ulhMondownRmonNonunicastCounterClientOutputValuePortn_Object = MibTableColumn
pm10010ulhMondownRmonNonunicastCounterClientOutputValuePortn = _Pm10010ulhMondownRmonNonunicastCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 720, 1, 2),
    _Pm10010ulhMondownRmonNonunicastCounterClientOutputValuePortn_Type()
)
pm10010ulhMondownRmonNonunicastCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMondownRmonNonunicastCounterClientOutputValuePortn.setStatus("current")
_Pm10010ulhMondownRmonNonunicastCounterClientOutputErrorPortn_Type = EkiOnOff
_Pm10010ulhMondownRmonNonunicastCounterClientOutputErrorPortn_Object = MibTableColumn
pm10010ulhMondownRmonNonunicastCounterClientOutputErrorPortn = _Pm10010ulhMondownRmonNonunicastCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 720, 1, 3),
    _Pm10010ulhMondownRmonNonunicastCounterClientOutputErrorPortn_Type()
)
pm10010ulhMondownRmonNonunicastCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMondownRmonNonunicastCounterClientOutputErrorPortn.setStatus("current")
_Pm10010ulhMondownRmonNonunicastCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pm10010ulhMondownRmonNonunicastCounterClientOutputOverloadPortn_Object = MibTableColumn
pm10010ulhMondownRmonNonunicastCounterClientOutputOverloadPortn = _Pm10010ulhMondownRmonNonunicastCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 2, 4, 720, 1, 4),
    _Pm10010ulhMondownRmonNonunicastCounterClientOutputOverloadPortn_Type()
)
pm10010ulhMondownRmonNonunicastCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhMondownRmonNonunicastCounterClientOutputOverloadPortn.setStatus("current")
_Pm10010ulhMonPerfOther_ObjectIdentity = ObjectIdentity
pm10010ulhMonPerfOther = _Pm10010ulhMonPerfOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 5)
)
_Pm10010ulhMonPerfSync_ObjectIdentity = ObjectIdentity
pm10010ulhMonPerfSync = _Pm10010ulhMonPerfSync_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 5, 1)
)
_Pm10010ulhPerfEnable_Type = EkiOnOff
_Pm10010ulhPerfEnable_Object = MibScalar
pm10010ulhPerfEnable = _Pm10010ulhPerfEnable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 5, 1, 257),
    _Pm10010ulhPerfEnable_Type()
)
pm10010ulhPerfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010ulhPerfEnable.setStatus("current")
_Pm10010ulhPerf15minSync_Type = EkiOnOff
_Pm10010ulhPerf15minSync_Object = MibScalar
pm10010ulhPerf15minSync = _Pm10010ulhPerf15minSync_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 5, 1, 259),
    _Pm10010ulhPerf15minSync_Type()
)
pm10010ulhPerf15minSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010ulhPerf15minSync.setStatus("current")
_Pm10010ulhPerf24hSync_Type = EkiOnOff
_Pm10010ulhPerf24hSync_Object = MibScalar
pm10010ulhPerf24hSync = _Pm10010ulhPerf24hSync_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 5, 1, 260),
    _Pm10010ulhPerf24hSync_Type()
)
pm10010ulhPerf24hSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010ulhPerf24hSync.setStatus("current")
_Pm10010ulhMonPerfTimeStamp_ObjectIdentity = ObjectIdentity
pm10010ulhMonPerfTimeStamp = _Pm10010ulhMonPerfTimeStamp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 5, 2)
)
_Pm10010ulhPerf15MinShort_Type = EkiOnOff
_Pm10010ulhPerf15MinShort_Object = MibScalar
pm10010ulhPerf15MinShort = _Pm10010ulhPerf15MinShort_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 5, 2, 1),
    _Pm10010ulhPerf15MinShort_Type()
)
pm10010ulhPerf15MinShort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010ulhPerf15MinShort.setStatus("current")
_Pm10010ulhPerf15MinLong_Type = EkiOnOff
_Pm10010ulhPerf15MinLong_Object = MibScalar
pm10010ulhPerf15MinLong = _Pm10010ulhPerf15MinLong_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 5, 2, 2),
    _Pm10010ulhPerf15MinLong_Type()
)
pm10010ulhPerf15MinLong.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010ulhPerf15MinLong.setStatus("current")
_Pm10010ulhPerf24HoursShort_Type = Counter32
_Pm10010ulhPerf24HoursShort_Object = MibScalar
pm10010ulhPerf24HoursShort = _Pm10010ulhPerf24HoursShort_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 5, 2, 5),
    _Pm10010ulhPerf24HoursShort_Type()
)
pm10010ulhPerf24HoursShort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010ulhPerf24HoursShort.setStatus("current")
_Pm10010ulhPerf24HoursLong_Type = Counter32
_Pm10010ulhPerf24HoursLong_Object = MibScalar
pm10010ulhPerf24HoursLong = _Pm10010ulhPerf24HoursLong_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 5, 2, 6),
    _Pm10010ulhPerf24HoursLong_Type()
)
pm10010ulhPerf24HoursLong.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010ulhPerf24HoursLong.setStatus("current")
_Pm10010ulhPerfCurrent15MinElapsedTime_Type = Counter32
_Pm10010ulhPerfCurrent15MinElapsedTime_Object = MibScalar
pm10010ulhPerfCurrent15MinElapsedTime = _Pm10010ulhPerfCurrent15MinElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 5, 2, 7),
    _Pm10010ulhPerfCurrent15MinElapsedTime_Type()
)
pm10010ulhPerfCurrent15MinElapsedTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010ulhPerfCurrent15MinElapsedTime.setStatus("current")
_Pm10010ulhPerfCurrent24HoursElapsedTime_Type = Counter32
_Pm10010ulhPerfCurrent24HoursElapsedTime_Object = MibScalar
pm10010ulhPerfCurrent24HoursElapsedTime = _Pm10010ulhPerfCurrent24HoursElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 5, 2, 8),
    _Pm10010ulhPerfCurrent24HoursElapsedTime_Type()
)
pm10010ulhPerfCurrent24HoursElapsedTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010ulhPerfCurrent24HoursElapsedTime.setStatus("current")
_Pm10010ulhMonPerfClient_ObjectIdentity = ObjectIdentity
pm10010ulhMonPerfClient = _Pm10010ulhMonPerfClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6)
)
_Pm10010ulhPerfTelecomInputClientCurrent15StatTable_Object = MibTable
pm10010ulhPerfTelecomInputClientCurrent15StatTable = _Pm10010ulhPerfTelecomInputClientCurrent15StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 16)
)
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomInputClientCurrent15StatTable.setStatus("current")
_Pm10010ulhPerfTelecomInputClientCurrent15StatEntry_Object = MibTableRow
pm10010ulhPerfTelecomInputClientCurrent15StatEntry = _Pm10010ulhPerfTelecomInputClientCurrent15StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 16, 1)
)
pm10010ulhPerfTelecomInputClientCurrent15StatEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhPerfTelecomInputClientCurrent15StatIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomInputClientCurrent15StatEntry.setStatus("current")


class _Pm10010ulhPerfTelecomInputClientCurrent15StatIndex_Type(Integer32):
    """Custom type pm10010ulhPerfTelecomInputClientCurrent15StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhPerfTelecomInputClientCurrent15StatIndex_Type.__name__ = "Integer32"
_Pm10010ulhPerfTelecomInputClientCurrent15StatIndex_Object = MibTableColumn
pm10010ulhPerfTelecomInputClientCurrent15StatIndex = _Pm10010ulhPerfTelecomInputClientCurrent15StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 16, 1, 1),
    _Pm10010ulhPerfTelecomInputClientCurrent15StatIndex_Type()
)
pm10010ulhPerfTelecomInputClientCurrent15StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomInputClientCurrent15StatIndex.setStatus("current")
_Pm10010ulhPerfTelecomInputClientCurrent15StatInvCvPortn_Type = EkiOnOff
_Pm10010ulhPerfTelecomInputClientCurrent15StatInvCvPortn_Object = MibTableColumn
pm10010ulhPerfTelecomInputClientCurrent15StatInvCvPortn = _Pm10010ulhPerfTelecomInputClientCurrent15StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 16, 1, 2),
    _Pm10010ulhPerfTelecomInputClientCurrent15StatInvCvPortn_Type()
)
pm10010ulhPerfTelecomInputClientCurrent15StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomInputClientCurrent15StatInvCvPortn.setStatus("current")
_Pm10010ulhPerfTelecomInputClientCurrent15StatCvValuePortn_Type = Unsigned32
_Pm10010ulhPerfTelecomInputClientCurrent15StatCvValuePortn_Object = MibTableColumn
pm10010ulhPerfTelecomInputClientCurrent15StatCvValuePortn = _Pm10010ulhPerfTelecomInputClientCurrent15StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 16, 1, 3),
    _Pm10010ulhPerfTelecomInputClientCurrent15StatCvValuePortn_Type()
)
pm10010ulhPerfTelecomInputClientCurrent15StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomInputClientCurrent15StatCvValuePortn.setStatus("current")
_Pm10010ulhPerfTelecomInputClientCurrent15StatInvEsPortn_Type = EkiOnOff
_Pm10010ulhPerfTelecomInputClientCurrent15StatInvEsPortn_Object = MibTableColumn
pm10010ulhPerfTelecomInputClientCurrent15StatInvEsPortn = _Pm10010ulhPerfTelecomInputClientCurrent15StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 16, 1, 4),
    _Pm10010ulhPerfTelecomInputClientCurrent15StatInvEsPortn_Type()
)
pm10010ulhPerfTelecomInputClientCurrent15StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomInputClientCurrent15StatInvEsPortn.setStatus("current")
_Pm10010ulhPerfTelecomInputClientCurrent15StatEsValuePortn_Type = Unsigned32
_Pm10010ulhPerfTelecomInputClientCurrent15StatEsValuePortn_Object = MibTableColumn
pm10010ulhPerfTelecomInputClientCurrent15StatEsValuePortn = _Pm10010ulhPerfTelecomInputClientCurrent15StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 16, 1, 5),
    _Pm10010ulhPerfTelecomInputClientCurrent15StatEsValuePortn_Type()
)
pm10010ulhPerfTelecomInputClientCurrent15StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomInputClientCurrent15StatEsValuePortn.setStatus("current")
_Pm10010ulhPerfTelecomInputClientCurrent15StatInvSesPortn_Type = EkiOnOff
_Pm10010ulhPerfTelecomInputClientCurrent15StatInvSesPortn_Object = MibTableColumn
pm10010ulhPerfTelecomInputClientCurrent15StatInvSesPortn = _Pm10010ulhPerfTelecomInputClientCurrent15StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 16, 1, 6),
    _Pm10010ulhPerfTelecomInputClientCurrent15StatInvSesPortn_Type()
)
pm10010ulhPerfTelecomInputClientCurrent15StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomInputClientCurrent15StatInvSesPortn.setStatus("current")
_Pm10010ulhPerfTelecomInputClientCurrent15StatSesValuePortn_Type = Unsigned32
_Pm10010ulhPerfTelecomInputClientCurrent15StatSesValuePortn_Object = MibTableColumn
pm10010ulhPerfTelecomInputClientCurrent15StatSesValuePortn = _Pm10010ulhPerfTelecomInputClientCurrent15StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 16, 1, 7),
    _Pm10010ulhPerfTelecomInputClientCurrent15StatSesValuePortn_Type()
)
pm10010ulhPerfTelecomInputClientCurrent15StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomInputClientCurrent15StatSesValuePortn.setStatus("current")
_Pm10010ulhPerfTelecomInputClientCurrent15StatInvSefsPortn_Type = EkiOnOff
_Pm10010ulhPerfTelecomInputClientCurrent15StatInvSefsPortn_Object = MibTableColumn
pm10010ulhPerfTelecomInputClientCurrent15StatInvSefsPortn = _Pm10010ulhPerfTelecomInputClientCurrent15StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 16, 1, 8),
    _Pm10010ulhPerfTelecomInputClientCurrent15StatInvSefsPortn_Type()
)
pm10010ulhPerfTelecomInputClientCurrent15StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomInputClientCurrent15StatInvSefsPortn.setStatus("current")
_Pm10010ulhPerfTelecomInputClientCurrent15StatSefsValuePortn_Type = Unsigned32
_Pm10010ulhPerfTelecomInputClientCurrent15StatSefsValuePortn_Object = MibTableColumn
pm10010ulhPerfTelecomInputClientCurrent15StatSefsValuePortn = _Pm10010ulhPerfTelecomInputClientCurrent15StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 16, 1, 9),
    _Pm10010ulhPerfTelecomInputClientCurrent15StatSefsValuePortn_Type()
)
pm10010ulhPerfTelecomInputClientCurrent15StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomInputClientCurrent15StatSefsValuePortn.setStatus("current")
_Pm10010ulhPerfTelecomInputClientCurrent15StatInvUasPortn_Type = EkiOnOff
_Pm10010ulhPerfTelecomInputClientCurrent15StatInvUasPortn_Object = MibTableColumn
pm10010ulhPerfTelecomInputClientCurrent15StatInvUasPortn = _Pm10010ulhPerfTelecomInputClientCurrent15StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 16, 1, 10),
    _Pm10010ulhPerfTelecomInputClientCurrent15StatInvUasPortn_Type()
)
pm10010ulhPerfTelecomInputClientCurrent15StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomInputClientCurrent15StatInvUasPortn.setStatus("current")
_Pm10010ulhPerfTelecomInputClientCurrent15StatUasValuePortn_Type = Unsigned32
_Pm10010ulhPerfTelecomInputClientCurrent15StatUasValuePortn_Object = MibTableColumn
pm10010ulhPerfTelecomInputClientCurrent15StatUasValuePortn = _Pm10010ulhPerfTelecomInputClientCurrent15StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 16, 1, 11),
    _Pm10010ulhPerfTelecomInputClientCurrent15StatUasValuePortn_Type()
)
pm10010ulhPerfTelecomInputClientCurrent15StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomInputClientCurrent15StatUasValuePortn.setStatus("current")
_Pm10010ulhPerfTelecomInputClientPast15StatHistoryPort1Table_Object = MibTable
pm10010ulhPerfTelecomInputClientPast15StatHistoryPort1Table = _Pm10010ulhPerfTelecomInputClientPast15StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 48)
)
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomInputClientPast15StatHistoryPort1Table.setStatus("current")
_Pm10010ulhPerfTelecomInputClientPast15StatHistoryPort1Entry_Object = MibTableRow
pm10010ulhPerfTelecomInputClientPast15StatHistoryPort1Entry = _Pm10010ulhPerfTelecomInputClientPast15StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 48, 1)
)
pm10010ulhPerfTelecomInputClientPast15StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhPerfTelecomInputClientPast15StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomInputClientPast15StatHistoryPort1Entry.setStatus("current")


class _Pm10010ulhPerfTelecomInputClientPast15StatHistoryPort1Index_Type(Integer32):
    """Custom type pm10010ulhPerfTelecomInputClientPast15StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhPerfTelecomInputClientPast15StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm10010ulhPerfTelecomInputClientPast15StatHistoryPort1Index_Object = MibTableColumn
pm10010ulhPerfTelecomInputClientPast15StatHistoryPort1Index = _Pm10010ulhPerfTelecomInputClientPast15StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 48, 1, 1),
    _Pm10010ulhPerfTelecomInputClientPast15StatHistoryPort1Index_Type()
)
pm10010ulhPerfTelecomInputClientPast15StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomInputClientPast15StatHistoryPort1Index.setStatus("current")
_Pm10010ulhPerfTelecomInputClientPast15StatHistoryInvCvPort1_Type = EkiOnOff
_Pm10010ulhPerfTelecomInputClientPast15StatHistoryInvCvPort1_Object = MibTableColumn
pm10010ulhPerfTelecomInputClientPast15StatHistoryInvCvPort1 = _Pm10010ulhPerfTelecomInputClientPast15StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 48, 1, 2),
    _Pm10010ulhPerfTelecomInputClientPast15StatHistoryInvCvPort1_Type()
)
pm10010ulhPerfTelecomInputClientPast15StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomInputClientPast15StatHistoryInvCvPort1.setStatus("current")
_Pm10010ulhPerfTelecomInputClientPast15StatHistoryCvValuePort1_Type = Unsigned32
_Pm10010ulhPerfTelecomInputClientPast15StatHistoryCvValuePort1_Object = MibTableColumn
pm10010ulhPerfTelecomInputClientPast15StatHistoryCvValuePort1 = _Pm10010ulhPerfTelecomInputClientPast15StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 48, 1, 3),
    _Pm10010ulhPerfTelecomInputClientPast15StatHistoryCvValuePort1_Type()
)
pm10010ulhPerfTelecomInputClientPast15StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomInputClientPast15StatHistoryCvValuePort1.setStatus("current")
_Pm10010ulhPerfTelecomInputClientPast15StatHistoryInvEsPort1_Type = EkiOnOff
_Pm10010ulhPerfTelecomInputClientPast15StatHistoryInvEsPort1_Object = MibTableColumn
pm10010ulhPerfTelecomInputClientPast15StatHistoryInvEsPort1 = _Pm10010ulhPerfTelecomInputClientPast15StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 48, 1, 4),
    _Pm10010ulhPerfTelecomInputClientPast15StatHistoryInvEsPort1_Type()
)
pm10010ulhPerfTelecomInputClientPast15StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomInputClientPast15StatHistoryInvEsPort1.setStatus("current")
_Pm10010ulhPerfTelecomInputClientPast15StatHistoryEsValuePort1_Type = Unsigned32
_Pm10010ulhPerfTelecomInputClientPast15StatHistoryEsValuePort1_Object = MibTableColumn
pm10010ulhPerfTelecomInputClientPast15StatHistoryEsValuePort1 = _Pm10010ulhPerfTelecomInputClientPast15StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 48, 1, 5),
    _Pm10010ulhPerfTelecomInputClientPast15StatHistoryEsValuePort1_Type()
)
pm10010ulhPerfTelecomInputClientPast15StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomInputClientPast15StatHistoryEsValuePort1.setStatus("current")
_Pm10010ulhPerfTelecomInputClientPast15StatHistoryInvSesPort1_Type = EkiOnOff
_Pm10010ulhPerfTelecomInputClientPast15StatHistoryInvSesPort1_Object = MibTableColumn
pm10010ulhPerfTelecomInputClientPast15StatHistoryInvSesPort1 = _Pm10010ulhPerfTelecomInputClientPast15StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 48, 1, 6),
    _Pm10010ulhPerfTelecomInputClientPast15StatHistoryInvSesPort1_Type()
)
pm10010ulhPerfTelecomInputClientPast15StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomInputClientPast15StatHistoryInvSesPort1.setStatus("current")
_Pm10010ulhPerfTelecomInputClientPast15StatHistorySesValuePort1_Type = Unsigned32
_Pm10010ulhPerfTelecomInputClientPast15StatHistorySesValuePort1_Object = MibTableColumn
pm10010ulhPerfTelecomInputClientPast15StatHistorySesValuePort1 = _Pm10010ulhPerfTelecomInputClientPast15StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 48, 1, 7),
    _Pm10010ulhPerfTelecomInputClientPast15StatHistorySesValuePort1_Type()
)
pm10010ulhPerfTelecomInputClientPast15StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomInputClientPast15StatHistorySesValuePort1.setStatus("current")
_Pm10010ulhPerfTelecomInputClientPast15StatHistoryInvSefsPort1_Type = EkiOnOff
_Pm10010ulhPerfTelecomInputClientPast15StatHistoryInvSefsPort1_Object = MibTableColumn
pm10010ulhPerfTelecomInputClientPast15StatHistoryInvSefsPort1 = _Pm10010ulhPerfTelecomInputClientPast15StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 48, 1, 8),
    _Pm10010ulhPerfTelecomInputClientPast15StatHistoryInvSefsPort1_Type()
)
pm10010ulhPerfTelecomInputClientPast15StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomInputClientPast15StatHistoryInvSefsPort1.setStatus("current")
_Pm10010ulhPerfTelecomInputClientPast15StatHistorySefsValuePort1_Type = Unsigned32
_Pm10010ulhPerfTelecomInputClientPast15StatHistorySefsValuePort1_Object = MibTableColumn
pm10010ulhPerfTelecomInputClientPast15StatHistorySefsValuePort1 = _Pm10010ulhPerfTelecomInputClientPast15StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 48, 1, 9),
    _Pm10010ulhPerfTelecomInputClientPast15StatHistorySefsValuePort1_Type()
)
pm10010ulhPerfTelecomInputClientPast15StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomInputClientPast15StatHistorySefsValuePort1.setStatus("current")
_Pm10010ulhPerfTelecomInputClientPast15StatHistoryInvUasPort1_Type = EkiOnOff
_Pm10010ulhPerfTelecomInputClientPast15StatHistoryInvUasPort1_Object = MibTableColumn
pm10010ulhPerfTelecomInputClientPast15StatHistoryInvUasPort1 = _Pm10010ulhPerfTelecomInputClientPast15StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 48, 1, 10),
    _Pm10010ulhPerfTelecomInputClientPast15StatHistoryInvUasPort1_Type()
)
pm10010ulhPerfTelecomInputClientPast15StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomInputClientPast15StatHistoryInvUasPort1.setStatus("current")
_Pm10010ulhPerfTelecomInputClientPast15StatHistoryUasValuePort1_Type = Unsigned32
_Pm10010ulhPerfTelecomInputClientPast15StatHistoryUasValuePort1_Object = MibTableColumn
pm10010ulhPerfTelecomInputClientPast15StatHistoryUasValuePort1 = _Pm10010ulhPerfTelecomInputClientPast15StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 48, 1, 11),
    _Pm10010ulhPerfTelecomInputClientPast15StatHistoryUasValuePort1_Type()
)
pm10010ulhPerfTelecomInputClientPast15StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomInputClientPast15StatHistoryUasValuePort1.setStatus("current")
_Pm10010ulhPerfTelecomInputClientCurrent24StatTable_Object = MibTable
pm10010ulhPerfTelecomInputClientCurrent24StatTable = _Pm10010ulhPerfTelecomInputClientCurrent24StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 80)
)
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomInputClientCurrent24StatTable.setStatus("current")
_Pm10010ulhPerfTelecomInputClientCurrent24StatEntry_Object = MibTableRow
pm10010ulhPerfTelecomInputClientCurrent24StatEntry = _Pm10010ulhPerfTelecomInputClientCurrent24StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 80, 1)
)
pm10010ulhPerfTelecomInputClientCurrent24StatEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhPerfTelecomInputClientCurrent24StatIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomInputClientCurrent24StatEntry.setStatus("current")


class _Pm10010ulhPerfTelecomInputClientCurrent24StatIndex_Type(Integer32):
    """Custom type pm10010ulhPerfTelecomInputClientCurrent24StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhPerfTelecomInputClientCurrent24StatIndex_Type.__name__ = "Integer32"
_Pm10010ulhPerfTelecomInputClientCurrent24StatIndex_Object = MibTableColumn
pm10010ulhPerfTelecomInputClientCurrent24StatIndex = _Pm10010ulhPerfTelecomInputClientCurrent24StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 80, 1, 1),
    _Pm10010ulhPerfTelecomInputClientCurrent24StatIndex_Type()
)
pm10010ulhPerfTelecomInputClientCurrent24StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomInputClientCurrent24StatIndex.setStatus("current")
_Pm10010ulhPerfTelecomInputClientCurrent24StatInvCvPortn_Type = EkiOnOff
_Pm10010ulhPerfTelecomInputClientCurrent24StatInvCvPortn_Object = MibTableColumn
pm10010ulhPerfTelecomInputClientCurrent24StatInvCvPortn = _Pm10010ulhPerfTelecomInputClientCurrent24StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 80, 1, 2),
    _Pm10010ulhPerfTelecomInputClientCurrent24StatInvCvPortn_Type()
)
pm10010ulhPerfTelecomInputClientCurrent24StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomInputClientCurrent24StatInvCvPortn.setStatus("current")
_Pm10010ulhPerfTelecomInputClientCurrent24StatCvValuePortn_Type = Unsigned32
_Pm10010ulhPerfTelecomInputClientCurrent24StatCvValuePortn_Object = MibTableColumn
pm10010ulhPerfTelecomInputClientCurrent24StatCvValuePortn = _Pm10010ulhPerfTelecomInputClientCurrent24StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 80, 1, 3),
    _Pm10010ulhPerfTelecomInputClientCurrent24StatCvValuePortn_Type()
)
pm10010ulhPerfTelecomInputClientCurrent24StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomInputClientCurrent24StatCvValuePortn.setStatus("current")
_Pm10010ulhPerfTelecomInputClientCurrent24StatInvEsPortn_Type = EkiOnOff
_Pm10010ulhPerfTelecomInputClientCurrent24StatInvEsPortn_Object = MibTableColumn
pm10010ulhPerfTelecomInputClientCurrent24StatInvEsPortn = _Pm10010ulhPerfTelecomInputClientCurrent24StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 80, 1, 4),
    _Pm10010ulhPerfTelecomInputClientCurrent24StatInvEsPortn_Type()
)
pm10010ulhPerfTelecomInputClientCurrent24StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomInputClientCurrent24StatInvEsPortn.setStatus("current")
_Pm10010ulhPerfTelecomInputClientCurrent24StatEsValuePortn_Type = Unsigned32
_Pm10010ulhPerfTelecomInputClientCurrent24StatEsValuePortn_Object = MibTableColumn
pm10010ulhPerfTelecomInputClientCurrent24StatEsValuePortn = _Pm10010ulhPerfTelecomInputClientCurrent24StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 80, 1, 5),
    _Pm10010ulhPerfTelecomInputClientCurrent24StatEsValuePortn_Type()
)
pm10010ulhPerfTelecomInputClientCurrent24StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomInputClientCurrent24StatEsValuePortn.setStatus("current")
_Pm10010ulhPerfTelecomInputClientCurrent24StatInvSesPortn_Type = EkiOnOff
_Pm10010ulhPerfTelecomInputClientCurrent24StatInvSesPortn_Object = MibTableColumn
pm10010ulhPerfTelecomInputClientCurrent24StatInvSesPortn = _Pm10010ulhPerfTelecomInputClientCurrent24StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 80, 1, 6),
    _Pm10010ulhPerfTelecomInputClientCurrent24StatInvSesPortn_Type()
)
pm10010ulhPerfTelecomInputClientCurrent24StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomInputClientCurrent24StatInvSesPortn.setStatus("current")
_Pm10010ulhPerfTelecomInputClientCurrent24StatSesValuePortn_Type = Unsigned32
_Pm10010ulhPerfTelecomInputClientCurrent24StatSesValuePortn_Object = MibTableColumn
pm10010ulhPerfTelecomInputClientCurrent24StatSesValuePortn = _Pm10010ulhPerfTelecomInputClientCurrent24StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 80, 1, 7),
    _Pm10010ulhPerfTelecomInputClientCurrent24StatSesValuePortn_Type()
)
pm10010ulhPerfTelecomInputClientCurrent24StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomInputClientCurrent24StatSesValuePortn.setStatus("current")
_Pm10010ulhPerfTelecomInputClientCurrent24StatInvSefsPortn_Type = EkiOnOff
_Pm10010ulhPerfTelecomInputClientCurrent24StatInvSefsPortn_Object = MibTableColumn
pm10010ulhPerfTelecomInputClientCurrent24StatInvSefsPortn = _Pm10010ulhPerfTelecomInputClientCurrent24StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 80, 1, 8),
    _Pm10010ulhPerfTelecomInputClientCurrent24StatInvSefsPortn_Type()
)
pm10010ulhPerfTelecomInputClientCurrent24StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomInputClientCurrent24StatInvSefsPortn.setStatus("current")
_Pm10010ulhPerfTelecomInputClientCurrent24StatSefsValuePortn_Type = Unsigned32
_Pm10010ulhPerfTelecomInputClientCurrent24StatSefsValuePortn_Object = MibTableColumn
pm10010ulhPerfTelecomInputClientCurrent24StatSefsValuePortn = _Pm10010ulhPerfTelecomInputClientCurrent24StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 80, 1, 9),
    _Pm10010ulhPerfTelecomInputClientCurrent24StatSefsValuePortn_Type()
)
pm10010ulhPerfTelecomInputClientCurrent24StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomInputClientCurrent24StatSefsValuePortn.setStatus("current")
_Pm10010ulhPerfTelecomInputClientCurrent24StatInvUasPortn_Type = EkiOnOff
_Pm10010ulhPerfTelecomInputClientCurrent24StatInvUasPortn_Object = MibTableColumn
pm10010ulhPerfTelecomInputClientCurrent24StatInvUasPortn = _Pm10010ulhPerfTelecomInputClientCurrent24StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 80, 1, 10),
    _Pm10010ulhPerfTelecomInputClientCurrent24StatInvUasPortn_Type()
)
pm10010ulhPerfTelecomInputClientCurrent24StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomInputClientCurrent24StatInvUasPortn.setStatus("current")
_Pm10010ulhPerfTelecomInputClientCurrent24StatUasValuePortn_Type = Unsigned32
_Pm10010ulhPerfTelecomInputClientCurrent24StatUasValuePortn_Object = MibTableColumn
pm10010ulhPerfTelecomInputClientCurrent24StatUasValuePortn = _Pm10010ulhPerfTelecomInputClientCurrent24StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 80, 1, 11),
    _Pm10010ulhPerfTelecomInputClientCurrent24StatUasValuePortn_Type()
)
pm10010ulhPerfTelecomInputClientCurrent24StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomInputClientCurrent24StatUasValuePortn.setStatus("current")
_Pm10010ulhPerfTelecomInputClientPast24StatHistoryPort1Table_Object = MibTable
pm10010ulhPerfTelecomInputClientPast24StatHistoryPort1Table = _Pm10010ulhPerfTelecomInputClientPast24StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 112)
)
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomInputClientPast24StatHistoryPort1Table.setStatus("current")
_Pm10010ulhPerfTelecomInputClientPast24StatHistoryPort1Entry_Object = MibTableRow
pm10010ulhPerfTelecomInputClientPast24StatHistoryPort1Entry = _Pm10010ulhPerfTelecomInputClientPast24StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 112, 1)
)
pm10010ulhPerfTelecomInputClientPast24StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhPerfTelecomInputClientPast24StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomInputClientPast24StatHistoryPort1Entry.setStatus("current")


class _Pm10010ulhPerfTelecomInputClientPast24StatHistoryPort1Index_Type(Integer32):
    """Custom type pm10010ulhPerfTelecomInputClientPast24StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhPerfTelecomInputClientPast24StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm10010ulhPerfTelecomInputClientPast24StatHistoryPort1Index_Object = MibTableColumn
pm10010ulhPerfTelecomInputClientPast24StatHistoryPort1Index = _Pm10010ulhPerfTelecomInputClientPast24StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 112, 1, 1),
    _Pm10010ulhPerfTelecomInputClientPast24StatHistoryPort1Index_Type()
)
pm10010ulhPerfTelecomInputClientPast24StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomInputClientPast24StatHistoryPort1Index.setStatus("current")
_Pm10010ulhPerfTelecomInputClientPast24StatHistoryInvCvPort1_Type = EkiOnOff
_Pm10010ulhPerfTelecomInputClientPast24StatHistoryInvCvPort1_Object = MibTableColumn
pm10010ulhPerfTelecomInputClientPast24StatHistoryInvCvPort1 = _Pm10010ulhPerfTelecomInputClientPast24StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 112, 1, 2),
    _Pm10010ulhPerfTelecomInputClientPast24StatHistoryInvCvPort1_Type()
)
pm10010ulhPerfTelecomInputClientPast24StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomInputClientPast24StatHistoryInvCvPort1.setStatus("current")
_Pm10010ulhPerfTelecomInputClientPast24StatHistoryCvValuePort1_Type = Unsigned32
_Pm10010ulhPerfTelecomInputClientPast24StatHistoryCvValuePort1_Object = MibTableColumn
pm10010ulhPerfTelecomInputClientPast24StatHistoryCvValuePort1 = _Pm10010ulhPerfTelecomInputClientPast24StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 112, 1, 3),
    _Pm10010ulhPerfTelecomInputClientPast24StatHistoryCvValuePort1_Type()
)
pm10010ulhPerfTelecomInputClientPast24StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomInputClientPast24StatHistoryCvValuePort1.setStatus("current")
_Pm10010ulhPerfTelecomInputClientPast24StatHistoryInvEsPort1_Type = EkiOnOff
_Pm10010ulhPerfTelecomInputClientPast24StatHistoryInvEsPort1_Object = MibTableColumn
pm10010ulhPerfTelecomInputClientPast24StatHistoryInvEsPort1 = _Pm10010ulhPerfTelecomInputClientPast24StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 112, 1, 4),
    _Pm10010ulhPerfTelecomInputClientPast24StatHistoryInvEsPort1_Type()
)
pm10010ulhPerfTelecomInputClientPast24StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomInputClientPast24StatHistoryInvEsPort1.setStatus("current")
_Pm10010ulhPerfTelecomInputClientPast24StatHistoryEsValuePort1_Type = Unsigned32
_Pm10010ulhPerfTelecomInputClientPast24StatHistoryEsValuePort1_Object = MibTableColumn
pm10010ulhPerfTelecomInputClientPast24StatHistoryEsValuePort1 = _Pm10010ulhPerfTelecomInputClientPast24StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 112, 1, 5),
    _Pm10010ulhPerfTelecomInputClientPast24StatHistoryEsValuePort1_Type()
)
pm10010ulhPerfTelecomInputClientPast24StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomInputClientPast24StatHistoryEsValuePort1.setStatus("current")
_Pm10010ulhPerfTelecomInputClientPast24StatHistoryInvSesPort1_Type = EkiOnOff
_Pm10010ulhPerfTelecomInputClientPast24StatHistoryInvSesPort1_Object = MibTableColumn
pm10010ulhPerfTelecomInputClientPast24StatHistoryInvSesPort1 = _Pm10010ulhPerfTelecomInputClientPast24StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 112, 1, 6),
    _Pm10010ulhPerfTelecomInputClientPast24StatHistoryInvSesPort1_Type()
)
pm10010ulhPerfTelecomInputClientPast24StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomInputClientPast24StatHistoryInvSesPort1.setStatus("current")
_Pm10010ulhPerfTelecomInputClientPast24StatHistorySesValuePort1_Type = Unsigned32
_Pm10010ulhPerfTelecomInputClientPast24StatHistorySesValuePort1_Object = MibTableColumn
pm10010ulhPerfTelecomInputClientPast24StatHistorySesValuePort1 = _Pm10010ulhPerfTelecomInputClientPast24StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 112, 1, 7),
    _Pm10010ulhPerfTelecomInputClientPast24StatHistorySesValuePort1_Type()
)
pm10010ulhPerfTelecomInputClientPast24StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomInputClientPast24StatHistorySesValuePort1.setStatus("current")
_Pm10010ulhPerfTelecomInputClientPast24StatHistoryInvSefsPort1_Type = EkiOnOff
_Pm10010ulhPerfTelecomInputClientPast24StatHistoryInvSefsPort1_Object = MibTableColumn
pm10010ulhPerfTelecomInputClientPast24StatHistoryInvSefsPort1 = _Pm10010ulhPerfTelecomInputClientPast24StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 112, 1, 8),
    _Pm10010ulhPerfTelecomInputClientPast24StatHistoryInvSefsPort1_Type()
)
pm10010ulhPerfTelecomInputClientPast24StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomInputClientPast24StatHistoryInvSefsPort1.setStatus("current")
_Pm10010ulhPerfTelecomInputClientPast24StatHistorySefsValuePort1_Type = Unsigned32
_Pm10010ulhPerfTelecomInputClientPast24StatHistorySefsValuePort1_Object = MibTableColumn
pm10010ulhPerfTelecomInputClientPast24StatHistorySefsValuePort1 = _Pm10010ulhPerfTelecomInputClientPast24StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 112, 1, 9),
    _Pm10010ulhPerfTelecomInputClientPast24StatHistorySefsValuePort1_Type()
)
pm10010ulhPerfTelecomInputClientPast24StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomInputClientPast24StatHistorySefsValuePort1.setStatus("current")
_Pm10010ulhPerfTelecomInputClientPast24StatHistoryInvUasPort1_Type = EkiOnOff
_Pm10010ulhPerfTelecomInputClientPast24StatHistoryInvUasPort1_Object = MibTableColumn
pm10010ulhPerfTelecomInputClientPast24StatHistoryInvUasPort1 = _Pm10010ulhPerfTelecomInputClientPast24StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 112, 1, 10),
    _Pm10010ulhPerfTelecomInputClientPast24StatHistoryInvUasPort1_Type()
)
pm10010ulhPerfTelecomInputClientPast24StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomInputClientPast24StatHistoryInvUasPort1.setStatus("current")
_Pm10010ulhPerfTelecomInputClientPast24StatHistoryUasValuePort1_Type = Unsigned32
_Pm10010ulhPerfTelecomInputClientPast24StatHistoryUasValuePort1_Object = MibTableColumn
pm10010ulhPerfTelecomInputClientPast24StatHistoryUasValuePort1 = _Pm10010ulhPerfTelecomInputClientPast24StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 112, 1, 11),
    _Pm10010ulhPerfTelecomInputClientPast24StatHistoryUasValuePort1_Type()
)
pm10010ulhPerfTelecomInputClientPast24StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomInputClientPast24StatHistoryUasValuePort1.setStatus("current")
_Pm10010ulhPerfTelecomOutputClientCurrent15StatTable_Object = MibTable
pm10010ulhPerfTelecomOutputClientCurrent15StatTable = _Pm10010ulhPerfTelecomOutputClientCurrent15StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 144)
)
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomOutputClientCurrent15StatTable.setStatus("current")
_Pm10010ulhPerfTelecomOutputClientCurrent15StatEntry_Object = MibTableRow
pm10010ulhPerfTelecomOutputClientCurrent15StatEntry = _Pm10010ulhPerfTelecomOutputClientCurrent15StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 144, 1)
)
pm10010ulhPerfTelecomOutputClientCurrent15StatEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhPerfTelecomOutputClientCurrent15StatIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomOutputClientCurrent15StatEntry.setStatus("current")


class _Pm10010ulhPerfTelecomOutputClientCurrent15StatIndex_Type(Integer32):
    """Custom type pm10010ulhPerfTelecomOutputClientCurrent15StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhPerfTelecomOutputClientCurrent15StatIndex_Type.__name__ = "Integer32"
_Pm10010ulhPerfTelecomOutputClientCurrent15StatIndex_Object = MibTableColumn
pm10010ulhPerfTelecomOutputClientCurrent15StatIndex = _Pm10010ulhPerfTelecomOutputClientCurrent15StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 144, 1, 1),
    _Pm10010ulhPerfTelecomOutputClientCurrent15StatIndex_Type()
)
pm10010ulhPerfTelecomOutputClientCurrent15StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomOutputClientCurrent15StatIndex.setStatus("current")
_Pm10010ulhPerfTelecomOutputClientCurrent15StatInvCvPortn_Type = EkiOnOff
_Pm10010ulhPerfTelecomOutputClientCurrent15StatInvCvPortn_Object = MibTableColumn
pm10010ulhPerfTelecomOutputClientCurrent15StatInvCvPortn = _Pm10010ulhPerfTelecomOutputClientCurrent15StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 144, 1, 2),
    _Pm10010ulhPerfTelecomOutputClientCurrent15StatInvCvPortn_Type()
)
pm10010ulhPerfTelecomOutputClientCurrent15StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomOutputClientCurrent15StatInvCvPortn.setStatus("current")
_Pm10010ulhPerfTelecomOutputClientCurrent15StatCvValuePortn_Type = Unsigned32
_Pm10010ulhPerfTelecomOutputClientCurrent15StatCvValuePortn_Object = MibTableColumn
pm10010ulhPerfTelecomOutputClientCurrent15StatCvValuePortn = _Pm10010ulhPerfTelecomOutputClientCurrent15StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 144, 1, 3),
    _Pm10010ulhPerfTelecomOutputClientCurrent15StatCvValuePortn_Type()
)
pm10010ulhPerfTelecomOutputClientCurrent15StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomOutputClientCurrent15StatCvValuePortn.setStatus("current")
_Pm10010ulhPerfTelecomOutputClientCurrent15StatInvEsPortn_Type = EkiOnOff
_Pm10010ulhPerfTelecomOutputClientCurrent15StatInvEsPortn_Object = MibTableColumn
pm10010ulhPerfTelecomOutputClientCurrent15StatInvEsPortn = _Pm10010ulhPerfTelecomOutputClientCurrent15StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 144, 1, 4),
    _Pm10010ulhPerfTelecomOutputClientCurrent15StatInvEsPortn_Type()
)
pm10010ulhPerfTelecomOutputClientCurrent15StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomOutputClientCurrent15StatInvEsPortn.setStatus("current")
_Pm10010ulhPerfTelecomOutputClientCurrent15StatEsValuePortn_Type = Unsigned32
_Pm10010ulhPerfTelecomOutputClientCurrent15StatEsValuePortn_Object = MibTableColumn
pm10010ulhPerfTelecomOutputClientCurrent15StatEsValuePortn = _Pm10010ulhPerfTelecomOutputClientCurrent15StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 144, 1, 5),
    _Pm10010ulhPerfTelecomOutputClientCurrent15StatEsValuePortn_Type()
)
pm10010ulhPerfTelecomOutputClientCurrent15StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomOutputClientCurrent15StatEsValuePortn.setStatus("current")
_Pm10010ulhPerfTelecomOutputClientCurrent15StatInvSesPortn_Type = EkiOnOff
_Pm10010ulhPerfTelecomOutputClientCurrent15StatInvSesPortn_Object = MibTableColumn
pm10010ulhPerfTelecomOutputClientCurrent15StatInvSesPortn = _Pm10010ulhPerfTelecomOutputClientCurrent15StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 144, 1, 6),
    _Pm10010ulhPerfTelecomOutputClientCurrent15StatInvSesPortn_Type()
)
pm10010ulhPerfTelecomOutputClientCurrent15StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomOutputClientCurrent15StatInvSesPortn.setStatus("current")
_Pm10010ulhPerfTelecomOutputClientCurrent15StatSesValuePortn_Type = Unsigned32
_Pm10010ulhPerfTelecomOutputClientCurrent15StatSesValuePortn_Object = MibTableColumn
pm10010ulhPerfTelecomOutputClientCurrent15StatSesValuePortn = _Pm10010ulhPerfTelecomOutputClientCurrent15StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 144, 1, 7),
    _Pm10010ulhPerfTelecomOutputClientCurrent15StatSesValuePortn_Type()
)
pm10010ulhPerfTelecomOutputClientCurrent15StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomOutputClientCurrent15StatSesValuePortn.setStatus("current")
_Pm10010ulhPerfTelecomOutputClientCurrent15StatInvSefsPortn_Type = EkiOnOff
_Pm10010ulhPerfTelecomOutputClientCurrent15StatInvSefsPortn_Object = MibTableColumn
pm10010ulhPerfTelecomOutputClientCurrent15StatInvSefsPortn = _Pm10010ulhPerfTelecomOutputClientCurrent15StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 144, 1, 8),
    _Pm10010ulhPerfTelecomOutputClientCurrent15StatInvSefsPortn_Type()
)
pm10010ulhPerfTelecomOutputClientCurrent15StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomOutputClientCurrent15StatInvSefsPortn.setStatus("current")
_Pm10010ulhPerfTelecomOutputClientCurrent15StatSefsValuePortn_Type = Unsigned32
_Pm10010ulhPerfTelecomOutputClientCurrent15StatSefsValuePortn_Object = MibTableColumn
pm10010ulhPerfTelecomOutputClientCurrent15StatSefsValuePortn = _Pm10010ulhPerfTelecomOutputClientCurrent15StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 144, 1, 9),
    _Pm10010ulhPerfTelecomOutputClientCurrent15StatSefsValuePortn_Type()
)
pm10010ulhPerfTelecomOutputClientCurrent15StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomOutputClientCurrent15StatSefsValuePortn.setStatus("current")
_Pm10010ulhPerfTelecomOutputClientCurrent15StatInvUasPortn_Type = EkiOnOff
_Pm10010ulhPerfTelecomOutputClientCurrent15StatInvUasPortn_Object = MibTableColumn
pm10010ulhPerfTelecomOutputClientCurrent15StatInvUasPortn = _Pm10010ulhPerfTelecomOutputClientCurrent15StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 144, 1, 10),
    _Pm10010ulhPerfTelecomOutputClientCurrent15StatInvUasPortn_Type()
)
pm10010ulhPerfTelecomOutputClientCurrent15StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomOutputClientCurrent15StatInvUasPortn.setStatus("current")
_Pm10010ulhPerfTelecomOutputClientCurrent15StatUasValuePortn_Type = Unsigned32
_Pm10010ulhPerfTelecomOutputClientCurrent15StatUasValuePortn_Object = MibTableColumn
pm10010ulhPerfTelecomOutputClientCurrent15StatUasValuePortn = _Pm10010ulhPerfTelecomOutputClientCurrent15StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 144, 1, 11),
    _Pm10010ulhPerfTelecomOutputClientCurrent15StatUasValuePortn_Type()
)
pm10010ulhPerfTelecomOutputClientCurrent15StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomOutputClientCurrent15StatUasValuePortn.setStatus("current")
_Pm10010ulhPerfTelecomOutputClientPast15StatHistoryPort1Table_Object = MibTable
pm10010ulhPerfTelecomOutputClientPast15StatHistoryPort1Table = _Pm10010ulhPerfTelecomOutputClientPast15StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 176)
)
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomOutputClientPast15StatHistoryPort1Table.setStatus("current")
_Pm10010ulhPerfTelecomOutputClientPast15StatHistoryPort1Entry_Object = MibTableRow
pm10010ulhPerfTelecomOutputClientPast15StatHistoryPort1Entry = _Pm10010ulhPerfTelecomOutputClientPast15StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 176, 1)
)
pm10010ulhPerfTelecomOutputClientPast15StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhPerfTelecomOutputClientPast15StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomOutputClientPast15StatHistoryPort1Entry.setStatus("current")


class _Pm10010ulhPerfTelecomOutputClientPast15StatHistoryPort1Index_Type(Integer32):
    """Custom type pm10010ulhPerfTelecomOutputClientPast15StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhPerfTelecomOutputClientPast15StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm10010ulhPerfTelecomOutputClientPast15StatHistoryPort1Index_Object = MibTableColumn
pm10010ulhPerfTelecomOutputClientPast15StatHistoryPort1Index = _Pm10010ulhPerfTelecomOutputClientPast15StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 176, 1, 1),
    _Pm10010ulhPerfTelecomOutputClientPast15StatHistoryPort1Index_Type()
)
pm10010ulhPerfTelecomOutputClientPast15StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomOutputClientPast15StatHistoryPort1Index.setStatus("current")
_Pm10010ulhPerfTelecomOutputClientPast15StatHistoryInvCvPort1_Type = EkiOnOff
_Pm10010ulhPerfTelecomOutputClientPast15StatHistoryInvCvPort1_Object = MibTableColumn
pm10010ulhPerfTelecomOutputClientPast15StatHistoryInvCvPort1 = _Pm10010ulhPerfTelecomOutputClientPast15StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 176, 1, 2),
    _Pm10010ulhPerfTelecomOutputClientPast15StatHistoryInvCvPort1_Type()
)
pm10010ulhPerfTelecomOutputClientPast15StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomOutputClientPast15StatHistoryInvCvPort1.setStatus("current")
_Pm10010ulhPerfTelecomOutputClientPast15StatHistoryCvValuePort1_Type = Unsigned32
_Pm10010ulhPerfTelecomOutputClientPast15StatHistoryCvValuePort1_Object = MibTableColumn
pm10010ulhPerfTelecomOutputClientPast15StatHistoryCvValuePort1 = _Pm10010ulhPerfTelecomOutputClientPast15StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 176, 1, 3),
    _Pm10010ulhPerfTelecomOutputClientPast15StatHistoryCvValuePort1_Type()
)
pm10010ulhPerfTelecomOutputClientPast15StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomOutputClientPast15StatHistoryCvValuePort1.setStatus("current")
_Pm10010ulhPerfTelecomOutputClientPast15StatHistoryInvEsPort1_Type = EkiOnOff
_Pm10010ulhPerfTelecomOutputClientPast15StatHistoryInvEsPort1_Object = MibTableColumn
pm10010ulhPerfTelecomOutputClientPast15StatHistoryInvEsPort1 = _Pm10010ulhPerfTelecomOutputClientPast15StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 176, 1, 4),
    _Pm10010ulhPerfTelecomOutputClientPast15StatHistoryInvEsPort1_Type()
)
pm10010ulhPerfTelecomOutputClientPast15StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomOutputClientPast15StatHistoryInvEsPort1.setStatus("current")
_Pm10010ulhPerfTelecomOutputClientPast15StatHistoryEsValuePort1_Type = Unsigned32
_Pm10010ulhPerfTelecomOutputClientPast15StatHistoryEsValuePort1_Object = MibTableColumn
pm10010ulhPerfTelecomOutputClientPast15StatHistoryEsValuePort1 = _Pm10010ulhPerfTelecomOutputClientPast15StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 176, 1, 5),
    _Pm10010ulhPerfTelecomOutputClientPast15StatHistoryEsValuePort1_Type()
)
pm10010ulhPerfTelecomOutputClientPast15StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomOutputClientPast15StatHistoryEsValuePort1.setStatus("current")
_Pm10010ulhPerfTelecomOutputClientPast15StatHistoryInvSesPort1_Type = EkiOnOff
_Pm10010ulhPerfTelecomOutputClientPast15StatHistoryInvSesPort1_Object = MibTableColumn
pm10010ulhPerfTelecomOutputClientPast15StatHistoryInvSesPort1 = _Pm10010ulhPerfTelecomOutputClientPast15StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 176, 1, 6),
    _Pm10010ulhPerfTelecomOutputClientPast15StatHistoryInvSesPort1_Type()
)
pm10010ulhPerfTelecomOutputClientPast15StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomOutputClientPast15StatHistoryInvSesPort1.setStatus("current")
_Pm10010ulhPerfTelecomOutputClientPast15StatHistorySesValuePort1_Type = Unsigned32
_Pm10010ulhPerfTelecomOutputClientPast15StatHistorySesValuePort1_Object = MibTableColumn
pm10010ulhPerfTelecomOutputClientPast15StatHistorySesValuePort1 = _Pm10010ulhPerfTelecomOutputClientPast15StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 176, 1, 7),
    _Pm10010ulhPerfTelecomOutputClientPast15StatHistorySesValuePort1_Type()
)
pm10010ulhPerfTelecomOutputClientPast15StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomOutputClientPast15StatHistorySesValuePort1.setStatus("current")
_Pm10010ulhPerfTelecomOutputClientPast15StatHistoryInvSefsPort1_Type = EkiOnOff
_Pm10010ulhPerfTelecomOutputClientPast15StatHistoryInvSefsPort1_Object = MibTableColumn
pm10010ulhPerfTelecomOutputClientPast15StatHistoryInvSefsPort1 = _Pm10010ulhPerfTelecomOutputClientPast15StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 176, 1, 8),
    _Pm10010ulhPerfTelecomOutputClientPast15StatHistoryInvSefsPort1_Type()
)
pm10010ulhPerfTelecomOutputClientPast15StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomOutputClientPast15StatHistoryInvSefsPort1.setStatus("current")
_Pm10010ulhPerfTelecomOutputClientPast15StatHistorySefsValuePort1_Type = Unsigned32
_Pm10010ulhPerfTelecomOutputClientPast15StatHistorySefsValuePort1_Object = MibTableColumn
pm10010ulhPerfTelecomOutputClientPast15StatHistorySefsValuePort1 = _Pm10010ulhPerfTelecomOutputClientPast15StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 176, 1, 9),
    _Pm10010ulhPerfTelecomOutputClientPast15StatHistorySefsValuePort1_Type()
)
pm10010ulhPerfTelecomOutputClientPast15StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomOutputClientPast15StatHistorySefsValuePort1.setStatus("current")
_Pm10010ulhPerfTelecomOutputClientPast15StatHistoryInvUasPort1_Type = EkiOnOff
_Pm10010ulhPerfTelecomOutputClientPast15StatHistoryInvUasPort1_Object = MibTableColumn
pm10010ulhPerfTelecomOutputClientPast15StatHistoryInvUasPort1 = _Pm10010ulhPerfTelecomOutputClientPast15StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 176, 1, 10),
    _Pm10010ulhPerfTelecomOutputClientPast15StatHistoryInvUasPort1_Type()
)
pm10010ulhPerfTelecomOutputClientPast15StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomOutputClientPast15StatHistoryInvUasPort1.setStatus("current")
_Pm10010ulhPerfTelecomOutputClientPast15StatHistoryUasValuePort1_Type = Unsigned32
_Pm10010ulhPerfTelecomOutputClientPast15StatHistoryUasValuePort1_Object = MibTableColumn
pm10010ulhPerfTelecomOutputClientPast15StatHistoryUasValuePort1 = _Pm10010ulhPerfTelecomOutputClientPast15StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 176, 1, 11),
    _Pm10010ulhPerfTelecomOutputClientPast15StatHistoryUasValuePort1_Type()
)
pm10010ulhPerfTelecomOutputClientPast15StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomOutputClientPast15StatHistoryUasValuePort1.setStatus("current")
_Pm10010ulhPerfTelecomOutputClientCurrent24StatTable_Object = MibTable
pm10010ulhPerfTelecomOutputClientCurrent24StatTable = _Pm10010ulhPerfTelecomOutputClientCurrent24StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 208)
)
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomOutputClientCurrent24StatTable.setStatus("current")
_Pm10010ulhPerfTelecomOutputClientCurrent24StatEntry_Object = MibTableRow
pm10010ulhPerfTelecomOutputClientCurrent24StatEntry = _Pm10010ulhPerfTelecomOutputClientCurrent24StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 208, 1)
)
pm10010ulhPerfTelecomOutputClientCurrent24StatEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhPerfTelecomOutputClientCurrent24StatIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomOutputClientCurrent24StatEntry.setStatus("current")


class _Pm10010ulhPerfTelecomOutputClientCurrent24StatIndex_Type(Integer32):
    """Custom type pm10010ulhPerfTelecomOutputClientCurrent24StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhPerfTelecomOutputClientCurrent24StatIndex_Type.__name__ = "Integer32"
_Pm10010ulhPerfTelecomOutputClientCurrent24StatIndex_Object = MibTableColumn
pm10010ulhPerfTelecomOutputClientCurrent24StatIndex = _Pm10010ulhPerfTelecomOutputClientCurrent24StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 208, 1, 1),
    _Pm10010ulhPerfTelecomOutputClientCurrent24StatIndex_Type()
)
pm10010ulhPerfTelecomOutputClientCurrent24StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomOutputClientCurrent24StatIndex.setStatus("current")
_Pm10010ulhPerfTelecomOutputClientCurrent24StatInvCvPortn_Type = EkiOnOff
_Pm10010ulhPerfTelecomOutputClientCurrent24StatInvCvPortn_Object = MibTableColumn
pm10010ulhPerfTelecomOutputClientCurrent24StatInvCvPortn = _Pm10010ulhPerfTelecomOutputClientCurrent24StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 208, 1, 2),
    _Pm10010ulhPerfTelecomOutputClientCurrent24StatInvCvPortn_Type()
)
pm10010ulhPerfTelecomOutputClientCurrent24StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomOutputClientCurrent24StatInvCvPortn.setStatus("current")
_Pm10010ulhPerfTelecomOutputClientCurrent24StatCvValuePortn_Type = Unsigned32
_Pm10010ulhPerfTelecomOutputClientCurrent24StatCvValuePortn_Object = MibTableColumn
pm10010ulhPerfTelecomOutputClientCurrent24StatCvValuePortn = _Pm10010ulhPerfTelecomOutputClientCurrent24StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 208, 1, 3),
    _Pm10010ulhPerfTelecomOutputClientCurrent24StatCvValuePortn_Type()
)
pm10010ulhPerfTelecomOutputClientCurrent24StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomOutputClientCurrent24StatCvValuePortn.setStatus("current")
_Pm10010ulhPerfTelecomOutputClientCurrent24StatInvEsPortn_Type = EkiOnOff
_Pm10010ulhPerfTelecomOutputClientCurrent24StatInvEsPortn_Object = MibTableColumn
pm10010ulhPerfTelecomOutputClientCurrent24StatInvEsPortn = _Pm10010ulhPerfTelecomOutputClientCurrent24StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 208, 1, 4),
    _Pm10010ulhPerfTelecomOutputClientCurrent24StatInvEsPortn_Type()
)
pm10010ulhPerfTelecomOutputClientCurrent24StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomOutputClientCurrent24StatInvEsPortn.setStatus("current")
_Pm10010ulhPerfTelecomOutputClientCurrent24StatEsValuePortn_Type = Unsigned32
_Pm10010ulhPerfTelecomOutputClientCurrent24StatEsValuePortn_Object = MibTableColumn
pm10010ulhPerfTelecomOutputClientCurrent24StatEsValuePortn = _Pm10010ulhPerfTelecomOutputClientCurrent24StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 208, 1, 5),
    _Pm10010ulhPerfTelecomOutputClientCurrent24StatEsValuePortn_Type()
)
pm10010ulhPerfTelecomOutputClientCurrent24StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomOutputClientCurrent24StatEsValuePortn.setStatus("current")
_Pm10010ulhPerfTelecomOutputClientCurrent24StatInvSesPortn_Type = EkiOnOff
_Pm10010ulhPerfTelecomOutputClientCurrent24StatInvSesPortn_Object = MibTableColumn
pm10010ulhPerfTelecomOutputClientCurrent24StatInvSesPortn = _Pm10010ulhPerfTelecomOutputClientCurrent24StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 208, 1, 6),
    _Pm10010ulhPerfTelecomOutputClientCurrent24StatInvSesPortn_Type()
)
pm10010ulhPerfTelecomOutputClientCurrent24StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomOutputClientCurrent24StatInvSesPortn.setStatus("current")
_Pm10010ulhPerfTelecomOutputClientCurrent24StatSesValuePortn_Type = Unsigned32
_Pm10010ulhPerfTelecomOutputClientCurrent24StatSesValuePortn_Object = MibTableColumn
pm10010ulhPerfTelecomOutputClientCurrent24StatSesValuePortn = _Pm10010ulhPerfTelecomOutputClientCurrent24StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 208, 1, 7),
    _Pm10010ulhPerfTelecomOutputClientCurrent24StatSesValuePortn_Type()
)
pm10010ulhPerfTelecomOutputClientCurrent24StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomOutputClientCurrent24StatSesValuePortn.setStatus("current")
_Pm10010ulhPerfTelecomOutputClientCurrent24StatInvSefsPortn_Type = EkiOnOff
_Pm10010ulhPerfTelecomOutputClientCurrent24StatInvSefsPortn_Object = MibTableColumn
pm10010ulhPerfTelecomOutputClientCurrent24StatInvSefsPortn = _Pm10010ulhPerfTelecomOutputClientCurrent24StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 208, 1, 8),
    _Pm10010ulhPerfTelecomOutputClientCurrent24StatInvSefsPortn_Type()
)
pm10010ulhPerfTelecomOutputClientCurrent24StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomOutputClientCurrent24StatInvSefsPortn.setStatus("current")
_Pm10010ulhPerfTelecomOutputClientCurrent24StatSefsValuePortn_Type = Unsigned32
_Pm10010ulhPerfTelecomOutputClientCurrent24StatSefsValuePortn_Object = MibTableColumn
pm10010ulhPerfTelecomOutputClientCurrent24StatSefsValuePortn = _Pm10010ulhPerfTelecomOutputClientCurrent24StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 208, 1, 9),
    _Pm10010ulhPerfTelecomOutputClientCurrent24StatSefsValuePortn_Type()
)
pm10010ulhPerfTelecomOutputClientCurrent24StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomOutputClientCurrent24StatSefsValuePortn.setStatus("current")
_Pm10010ulhPerfTelecomOutputClientCurrent24StatInvUasPortn_Type = EkiOnOff
_Pm10010ulhPerfTelecomOutputClientCurrent24StatInvUasPortn_Object = MibTableColumn
pm10010ulhPerfTelecomOutputClientCurrent24StatInvUasPortn = _Pm10010ulhPerfTelecomOutputClientCurrent24StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 208, 1, 10),
    _Pm10010ulhPerfTelecomOutputClientCurrent24StatInvUasPortn_Type()
)
pm10010ulhPerfTelecomOutputClientCurrent24StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomOutputClientCurrent24StatInvUasPortn.setStatus("current")
_Pm10010ulhPerfTelecomOutputClientCurrent24StatUasValuePortn_Type = Unsigned32
_Pm10010ulhPerfTelecomOutputClientCurrent24StatUasValuePortn_Object = MibTableColumn
pm10010ulhPerfTelecomOutputClientCurrent24StatUasValuePortn = _Pm10010ulhPerfTelecomOutputClientCurrent24StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 208, 1, 11),
    _Pm10010ulhPerfTelecomOutputClientCurrent24StatUasValuePortn_Type()
)
pm10010ulhPerfTelecomOutputClientCurrent24StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomOutputClientCurrent24StatUasValuePortn.setStatus("current")
_Pm10010ulhPerfTelecomOutputClientPast24StatHistoryPort1Table_Object = MibTable
pm10010ulhPerfTelecomOutputClientPast24StatHistoryPort1Table = _Pm10010ulhPerfTelecomOutputClientPast24StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 240)
)
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomOutputClientPast24StatHistoryPort1Table.setStatus("current")
_Pm10010ulhPerfTelecomOutputClientPast24StatHistoryPort1Entry_Object = MibTableRow
pm10010ulhPerfTelecomOutputClientPast24StatHistoryPort1Entry = _Pm10010ulhPerfTelecomOutputClientPast24StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 240, 1)
)
pm10010ulhPerfTelecomOutputClientPast24StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhPerfTelecomOutputClientPast24StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomOutputClientPast24StatHistoryPort1Entry.setStatus("current")


class _Pm10010ulhPerfTelecomOutputClientPast24StatHistoryPort1Index_Type(Integer32):
    """Custom type pm10010ulhPerfTelecomOutputClientPast24StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhPerfTelecomOutputClientPast24StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm10010ulhPerfTelecomOutputClientPast24StatHistoryPort1Index_Object = MibTableColumn
pm10010ulhPerfTelecomOutputClientPast24StatHistoryPort1Index = _Pm10010ulhPerfTelecomOutputClientPast24StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 240, 1, 1),
    _Pm10010ulhPerfTelecomOutputClientPast24StatHistoryPort1Index_Type()
)
pm10010ulhPerfTelecomOutputClientPast24StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomOutputClientPast24StatHistoryPort1Index.setStatus("current")
_Pm10010ulhPerfTelecomOutputClientPast24StatHistoryInvCvPort1_Type = EkiOnOff
_Pm10010ulhPerfTelecomOutputClientPast24StatHistoryInvCvPort1_Object = MibTableColumn
pm10010ulhPerfTelecomOutputClientPast24StatHistoryInvCvPort1 = _Pm10010ulhPerfTelecomOutputClientPast24StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 240, 1, 2),
    _Pm10010ulhPerfTelecomOutputClientPast24StatHistoryInvCvPort1_Type()
)
pm10010ulhPerfTelecomOutputClientPast24StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomOutputClientPast24StatHistoryInvCvPort1.setStatus("current")
_Pm10010ulhPerfTelecomOutputClientPast24StatHistoryCvValuePort1_Type = Unsigned32
_Pm10010ulhPerfTelecomOutputClientPast24StatHistoryCvValuePort1_Object = MibTableColumn
pm10010ulhPerfTelecomOutputClientPast24StatHistoryCvValuePort1 = _Pm10010ulhPerfTelecomOutputClientPast24StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 240, 1, 3),
    _Pm10010ulhPerfTelecomOutputClientPast24StatHistoryCvValuePort1_Type()
)
pm10010ulhPerfTelecomOutputClientPast24StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomOutputClientPast24StatHistoryCvValuePort1.setStatus("current")
_Pm10010ulhPerfTelecomOutputClientPast24StatHistoryInvEsPort1_Type = EkiOnOff
_Pm10010ulhPerfTelecomOutputClientPast24StatHistoryInvEsPort1_Object = MibTableColumn
pm10010ulhPerfTelecomOutputClientPast24StatHistoryInvEsPort1 = _Pm10010ulhPerfTelecomOutputClientPast24StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 240, 1, 4),
    _Pm10010ulhPerfTelecomOutputClientPast24StatHistoryInvEsPort1_Type()
)
pm10010ulhPerfTelecomOutputClientPast24StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomOutputClientPast24StatHistoryInvEsPort1.setStatus("current")
_Pm10010ulhPerfTelecomOutputClientPast24StatHistoryEsValuePort1_Type = Unsigned32
_Pm10010ulhPerfTelecomOutputClientPast24StatHistoryEsValuePort1_Object = MibTableColumn
pm10010ulhPerfTelecomOutputClientPast24StatHistoryEsValuePort1 = _Pm10010ulhPerfTelecomOutputClientPast24StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 240, 1, 5),
    _Pm10010ulhPerfTelecomOutputClientPast24StatHistoryEsValuePort1_Type()
)
pm10010ulhPerfTelecomOutputClientPast24StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomOutputClientPast24StatHistoryEsValuePort1.setStatus("current")
_Pm10010ulhPerfTelecomOutputClientPast24StatHistoryInvSesPort1_Type = EkiOnOff
_Pm10010ulhPerfTelecomOutputClientPast24StatHistoryInvSesPort1_Object = MibTableColumn
pm10010ulhPerfTelecomOutputClientPast24StatHistoryInvSesPort1 = _Pm10010ulhPerfTelecomOutputClientPast24StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 240, 1, 6),
    _Pm10010ulhPerfTelecomOutputClientPast24StatHistoryInvSesPort1_Type()
)
pm10010ulhPerfTelecomOutputClientPast24StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomOutputClientPast24StatHistoryInvSesPort1.setStatus("current")
_Pm10010ulhPerfTelecomOutputClientPast24StatHistorySesValuePort1_Type = Unsigned32
_Pm10010ulhPerfTelecomOutputClientPast24StatHistorySesValuePort1_Object = MibTableColumn
pm10010ulhPerfTelecomOutputClientPast24StatHistorySesValuePort1 = _Pm10010ulhPerfTelecomOutputClientPast24StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 240, 1, 7),
    _Pm10010ulhPerfTelecomOutputClientPast24StatHistorySesValuePort1_Type()
)
pm10010ulhPerfTelecomOutputClientPast24StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomOutputClientPast24StatHistorySesValuePort1.setStatus("current")
_Pm10010ulhPerfTelecomOutputClientPast24StatHistoryInvSefsPort1_Type = EkiOnOff
_Pm10010ulhPerfTelecomOutputClientPast24StatHistoryInvSefsPort1_Object = MibTableColumn
pm10010ulhPerfTelecomOutputClientPast24StatHistoryInvSefsPort1 = _Pm10010ulhPerfTelecomOutputClientPast24StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 240, 1, 8),
    _Pm10010ulhPerfTelecomOutputClientPast24StatHistoryInvSefsPort1_Type()
)
pm10010ulhPerfTelecomOutputClientPast24StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomOutputClientPast24StatHistoryInvSefsPort1.setStatus("current")
_Pm10010ulhPerfTelecomOutputClientPast24StatHistorySefsValuePort1_Type = Unsigned32
_Pm10010ulhPerfTelecomOutputClientPast24StatHistorySefsValuePort1_Object = MibTableColumn
pm10010ulhPerfTelecomOutputClientPast24StatHistorySefsValuePort1 = _Pm10010ulhPerfTelecomOutputClientPast24StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 240, 1, 9),
    _Pm10010ulhPerfTelecomOutputClientPast24StatHistorySefsValuePort1_Type()
)
pm10010ulhPerfTelecomOutputClientPast24StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomOutputClientPast24StatHistorySefsValuePort1.setStatus("current")
_Pm10010ulhPerfTelecomOutputClientPast24StatHistoryInvUasPort1_Type = EkiOnOff
_Pm10010ulhPerfTelecomOutputClientPast24StatHistoryInvUasPort1_Object = MibTableColumn
pm10010ulhPerfTelecomOutputClientPast24StatHistoryInvUasPort1 = _Pm10010ulhPerfTelecomOutputClientPast24StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 240, 1, 10),
    _Pm10010ulhPerfTelecomOutputClientPast24StatHistoryInvUasPort1_Type()
)
pm10010ulhPerfTelecomOutputClientPast24StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomOutputClientPast24StatHistoryInvUasPort1.setStatus("current")
_Pm10010ulhPerfTelecomOutputClientPast24StatHistoryUasValuePort1_Type = Unsigned32
_Pm10010ulhPerfTelecomOutputClientPast24StatHistoryUasValuePort1_Object = MibTableColumn
pm10010ulhPerfTelecomOutputClientPast24StatHistoryUasValuePort1 = _Pm10010ulhPerfTelecomOutputClientPast24StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 240, 1, 11),
    _Pm10010ulhPerfTelecomOutputClientPast24StatHistoryUasValuePort1_Type()
)
pm10010ulhPerfTelecomOutputClientPast24StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomOutputClientPast24StatHistoryUasValuePort1.setStatus("current")
_Pm10010ulhPerfDatacomClientCurrent15StatTable_Object = MibTable
pm10010ulhPerfDatacomClientCurrent15StatTable = _Pm10010ulhPerfDatacomClientCurrent15StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 848)
)
if mibBuilder.loadTexts:
    pm10010ulhPerfDatacomClientCurrent15StatTable.setStatus("current")
_Pm10010ulhPerfDatacomClientCurrent15StatEntry_Object = MibTableRow
pm10010ulhPerfDatacomClientCurrent15StatEntry = _Pm10010ulhPerfDatacomClientCurrent15StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 848, 1)
)
pm10010ulhPerfDatacomClientCurrent15StatEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhPerfDatacomClientCurrent15StatIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhPerfDatacomClientCurrent15StatEntry.setStatus("current")


class _Pm10010ulhPerfDatacomClientCurrent15StatIndex_Type(Integer32):
    """Custom type pm10010ulhPerfDatacomClientCurrent15StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhPerfDatacomClientCurrent15StatIndex_Type.__name__ = "Integer32"
_Pm10010ulhPerfDatacomClientCurrent15StatIndex_Object = MibTableColumn
pm10010ulhPerfDatacomClientCurrent15StatIndex = _Pm10010ulhPerfDatacomClientCurrent15StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 848, 1, 1),
    _Pm10010ulhPerfDatacomClientCurrent15StatIndex_Type()
)
pm10010ulhPerfDatacomClientCurrent15StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfDatacomClientCurrent15StatIndex.setStatus("current")
_Pm10010ulhperfdatacomclientCurrent15StatInCrcCountInvPortn_Type = EkiOnOff
_Pm10010ulhperfdatacomclientCurrent15StatInCrcCountInvPortn_Object = MibTableColumn
pm10010ulhperfdatacomclientCurrent15StatInCrcCountInvPortn = _Pm10010ulhperfdatacomclientCurrent15StatInCrcCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 848, 1, 4),
    _Pm10010ulhperfdatacomclientCurrent15StatInCrcCountInvPortn_Type()
)
pm10010ulhperfdatacomclientCurrent15StatInCrcCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhperfdatacomclientCurrent15StatInCrcCountInvPortn.setStatus("current")
_Pm10010ulhperfdatacomclientCurrent15StatInCrcCountPortn_Type = Counter64
_Pm10010ulhperfdatacomclientCurrent15StatInCrcCountPortn_Object = MibTableColumn
pm10010ulhperfdatacomclientCurrent15StatInCrcCountPortn = _Pm10010ulhperfdatacomclientCurrent15StatInCrcCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 848, 1, 5),
    _Pm10010ulhperfdatacomclientCurrent15StatInCrcCountPortn_Type()
)
pm10010ulhperfdatacomclientCurrent15StatInCrcCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhperfdatacomclientCurrent15StatInCrcCountPortn.setStatus("current")
_Pm10010ulhperfdatacomclientCurrent15StatInPacketCountInvPortn_Type = EkiOnOff
_Pm10010ulhperfdatacomclientCurrent15StatInPacketCountInvPortn_Object = MibTableColumn
pm10010ulhperfdatacomclientCurrent15StatInPacketCountInvPortn = _Pm10010ulhperfdatacomclientCurrent15StatInPacketCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 848, 1, 6),
    _Pm10010ulhperfdatacomclientCurrent15StatInPacketCountInvPortn_Type()
)
pm10010ulhperfdatacomclientCurrent15StatInPacketCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhperfdatacomclientCurrent15StatInPacketCountInvPortn.setStatus("current")
_Pm10010ulhperfdatacomclientCurrent15StatInPacketCountPortn_Type = Counter64
_Pm10010ulhperfdatacomclientCurrent15StatInPacketCountPortn_Object = MibTableColumn
pm10010ulhperfdatacomclientCurrent15StatInPacketCountPortn = _Pm10010ulhperfdatacomclientCurrent15StatInPacketCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 848, 1, 7),
    _Pm10010ulhperfdatacomclientCurrent15StatInPacketCountPortn_Type()
)
pm10010ulhperfdatacomclientCurrent15StatInPacketCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhperfdatacomclientCurrent15StatInPacketCountPortn.setStatus("current")
_Pm10010ulhperfdatacomclientCurrent15StatOutCrcCountInvPortn_Type = EkiOnOff
_Pm10010ulhperfdatacomclientCurrent15StatOutCrcCountInvPortn_Object = MibTableColumn
pm10010ulhperfdatacomclientCurrent15StatOutCrcCountInvPortn = _Pm10010ulhperfdatacomclientCurrent15StatOutCrcCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 848, 1, 28),
    _Pm10010ulhperfdatacomclientCurrent15StatOutCrcCountInvPortn_Type()
)
pm10010ulhperfdatacomclientCurrent15StatOutCrcCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhperfdatacomclientCurrent15StatOutCrcCountInvPortn.setStatus("current")
_Pm10010ulhperfdatacomclientCurrent15StatOutCrcCountPortn_Type = Counter64
_Pm10010ulhperfdatacomclientCurrent15StatOutCrcCountPortn_Object = MibTableColumn
pm10010ulhperfdatacomclientCurrent15StatOutCrcCountPortn = _Pm10010ulhperfdatacomclientCurrent15StatOutCrcCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 848, 1, 29),
    _Pm10010ulhperfdatacomclientCurrent15StatOutCrcCountPortn_Type()
)
pm10010ulhperfdatacomclientCurrent15StatOutCrcCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhperfdatacomclientCurrent15StatOutCrcCountPortn.setStatus("current")
_Pm10010ulhperfdatacomclientCurrent15StatOutPacketCountInvPortn_Type = EkiOnOff
_Pm10010ulhperfdatacomclientCurrent15StatOutPacketCountInvPortn_Object = MibTableColumn
pm10010ulhperfdatacomclientCurrent15StatOutPacketCountInvPortn = _Pm10010ulhperfdatacomclientCurrent15StatOutPacketCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 848, 1, 30),
    _Pm10010ulhperfdatacomclientCurrent15StatOutPacketCountInvPortn_Type()
)
pm10010ulhperfdatacomclientCurrent15StatOutPacketCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhperfdatacomclientCurrent15StatOutPacketCountInvPortn.setStatus("current")
_Pm10010ulhperfdatacomclientCurrent15StatOutPacketCountPortn_Type = Counter64
_Pm10010ulhperfdatacomclientCurrent15StatOutPacketCountPortn_Object = MibTableColumn
pm10010ulhperfdatacomclientCurrent15StatOutPacketCountPortn = _Pm10010ulhperfdatacomclientCurrent15StatOutPacketCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 848, 1, 31),
    _Pm10010ulhperfdatacomclientCurrent15StatOutPacketCountPortn_Type()
)
pm10010ulhperfdatacomclientCurrent15StatOutPacketCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhperfdatacomclientCurrent15StatOutPacketCountPortn.setStatus("current")
_Pm10010ulhPerfDatacomClientPast15StatHistoryPort1Table_Object = MibTable
pm10010ulhPerfDatacomClientPast15StatHistoryPort1Table = _Pm10010ulhPerfDatacomClientPast15StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 880)
)
if mibBuilder.loadTexts:
    pm10010ulhPerfDatacomClientPast15StatHistoryPort1Table.setStatus("current")
_Pm10010ulhPerfDatacomClientPast15StatHistoryPort1Entry_Object = MibTableRow
pm10010ulhPerfDatacomClientPast15StatHistoryPort1Entry = _Pm10010ulhPerfDatacomClientPast15StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 880, 1)
)
pm10010ulhPerfDatacomClientPast15StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhPerfDatacomClientPast15StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm10010ulhPerfDatacomClientPast15StatHistoryPort1Entry.setStatus("current")


class _Pm10010ulhPerfDatacomClientPast15StatHistoryPort1Index_Type(Integer32):
    """Custom type pm10010ulhPerfDatacomClientPast15StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhPerfDatacomClientPast15StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm10010ulhPerfDatacomClientPast15StatHistoryPort1Index_Object = MibTableColumn
pm10010ulhPerfDatacomClientPast15StatHistoryPort1Index = _Pm10010ulhPerfDatacomClientPast15StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 880, 1, 1),
    _Pm10010ulhPerfDatacomClientPast15StatHistoryPort1Index_Type()
)
pm10010ulhPerfDatacomClientPast15StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfDatacomClientPast15StatHistoryPort1Index.setStatus("current")
_Pm10010ulhperfdatacomclientPast15StatInCrcCountInvPort1_Type = EkiOnOff
_Pm10010ulhperfdatacomclientPast15StatInCrcCountInvPort1_Object = MibTableColumn
pm10010ulhperfdatacomclientPast15StatInCrcCountInvPort1 = _Pm10010ulhperfdatacomclientPast15StatInCrcCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 880, 1, 4),
    _Pm10010ulhperfdatacomclientPast15StatInCrcCountInvPort1_Type()
)
pm10010ulhperfdatacomclientPast15StatInCrcCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhperfdatacomclientPast15StatInCrcCountInvPort1.setStatus("current")
_Pm10010ulhperfdatacomclientPast15StatInCrcCountPort1_Type = Counter64
_Pm10010ulhperfdatacomclientPast15StatInCrcCountPort1_Object = MibTableColumn
pm10010ulhperfdatacomclientPast15StatInCrcCountPort1 = _Pm10010ulhperfdatacomclientPast15StatInCrcCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 880, 1, 5),
    _Pm10010ulhperfdatacomclientPast15StatInCrcCountPort1_Type()
)
pm10010ulhperfdatacomclientPast15StatInCrcCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhperfdatacomclientPast15StatInCrcCountPort1.setStatus("current")
_Pm10010ulhperfdatacomclientPast15StatInPacketCountInvPort1_Type = EkiOnOff
_Pm10010ulhperfdatacomclientPast15StatInPacketCountInvPort1_Object = MibTableColumn
pm10010ulhperfdatacomclientPast15StatInPacketCountInvPort1 = _Pm10010ulhperfdatacomclientPast15StatInPacketCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 880, 1, 6),
    _Pm10010ulhperfdatacomclientPast15StatInPacketCountInvPort1_Type()
)
pm10010ulhperfdatacomclientPast15StatInPacketCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhperfdatacomclientPast15StatInPacketCountInvPort1.setStatus("current")
_Pm10010ulhperfdatacomclientPast15StatInPacketCountPort1_Type = Counter64
_Pm10010ulhperfdatacomclientPast15StatInPacketCountPort1_Object = MibTableColumn
pm10010ulhperfdatacomclientPast15StatInPacketCountPort1 = _Pm10010ulhperfdatacomclientPast15StatInPacketCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 880, 1, 7),
    _Pm10010ulhperfdatacomclientPast15StatInPacketCountPort1_Type()
)
pm10010ulhperfdatacomclientPast15StatInPacketCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhperfdatacomclientPast15StatInPacketCountPort1.setStatus("current")
_Pm10010ulhperfdatacomclientPast15StatOutCrcCountInvPort1_Type = EkiOnOff
_Pm10010ulhperfdatacomclientPast15StatOutCrcCountInvPort1_Object = MibTableColumn
pm10010ulhperfdatacomclientPast15StatOutCrcCountInvPort1 = _Pm10010ulhperfdatacomclientPast15StatOutCrcCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 880, 1, 28),
    _Pm10010ulhperfdatacomclientPast15StatOutCrcCountInvPort1_Type()
)
pm10010ulhperfdatacomclientPast15StatOutCrcCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhperfdatacomclientPast15StatOutCrcCountInvPort1.setStatus("current")
_Pm10010ulhperfdatacomclientPast15StatOutCrcCountPort1_Type = Counter64
_Pm10010ulhperfdatacomclientPast15StatOutCrcCountPort1_Object = MibTableColumn
pm10010ulhperfdatacomclientPast15StatOutCrcCountPort1 = _Pm10010ulhperfdatacomclientPast15StatOutCrcCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 880, 1, 29),
    _Pm10010ulhperfdatacomclientPast15StatOutCrcCountPort1_Type()
)
pm10010ulhperfdatacomclientPast15StatOutCrcCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhperfdatacomclientPast15StatOutCrcCountPort1.setStatus("current")
_Pm10010ulhperfdatacomclientPast15StatOutPacketCountInvPort1_Type = EkiOnOff
_Pm10010ulhperfdatacomclientPast15StatOutPacketCountInvPort1_Object = MibTableColumn
pm10010ulhperfdatacomclientPast15StatOutPacketCountInvPort1 = _Pm10010ulhperfdatacomclientPast15StatOutPacketCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 880, 1, 30),
    _Pm10010ulhperfdatacomclientPast15StatOutPacketCountInvPort1_Type()
)
pm10010ulhperfdatacomclientPast15StatOutPacketCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhperfdatacomclientPast15StatOutPacketCountInvPort1.setStatus("current")
_Pm10010ulhperfdatacomclientPast15StatOutPacketCountPort1_Type = Counter64
_Pm10010ulhperfdatacomclientPast15StatOutPacketCountPort1_Object = MibTableColumn
pm10010ulhperfdatacomclientPast15StatOutPacketCountPort1 = _Pm10010ulhperfdatacomclientPast15StatOutPacketCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 880, 1, 31),
    _Pm10010ulhperfdatacomclientPast15StatOutPacketCountPort1_Type()
)
pm10010ulhperfdatacomclientPast15StatOutPacketCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhperfdatacomclientPast15StatOutPacketCountPort1.setStatus("current")
_Pm10010ulhPerfDatacomClientCurrent24StatTable_Object = MibTable
pm10010ulhPerfDatacomClientCurrent24StatTable = _Pm10010ulhPerfDatacomClientCurrent24StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 912)
)
if mibBuilder.loadTexts:
    pm10010ulhPerfDatacomClientCurrent24StatTable.setStatus("current")
_Pm10010ulhPerfDatacomClientCurrent24StatEntry_Object = MibTableRow
pm10010ulhPerfDatacomClientCurrent24StatEntry = _Pm10010ulhPerfDatacomClientCurrent24StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 912, 1)
)
pm10010ulhPerfDatacomClientCurrent24StatEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhPerfDatacomClientCurrent24StatIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhPerfDatacomClientCurrent24StatEntry.setStatus("current")


class _Pm10010ulhPerfDatacomClientCurrent24StatIndex_Type(Integer32):
    """Custom type pm10010ulhPerfDatacomClientCurrent24StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhPerfDatacomClientCurrent24StatIndex_Type.__name__ = "Integer32"
_Pm10010ulhPerfDatacomClientCurrent24StatIndex_Object = MibTableColumn
pm10010ulhPerfDatacomClientCurrent24StatIndex = _Pm10010ulhPerfDatacomClientCurrent24StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 912, 1, 1),
    _Pm10010ulhPerfDatacomClientCurrent24StatIndex_Type()
)
pm10010ulhPerfDatacomClientCurrent24StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfDatacomClientCurrent24StatIndex.setStatus("current")
_Pm10010ulhperfdatacomclientCurrent24StatInCrcCountInvPortn_Type = EkiOnOff
_Pm10010ulhperfdatacomclientCurrent24StatInCrcCountInvPortn_Object = MibTableColumn
pm10010ulhperfdatacomclientCurrent24StatInCrcCountInvPortn = _Pm10010ulhperfdatacomclientCurrent24StatInCrcCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 912, 1, 4),
    _Pm10010ulhperfdatacomclientCurrent24StatInCrcCountInvPortn_Type()
)
pm10010ulhperfdatacomclientCurrent24StatInCrcCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhperfdatacomclientCurrent24StatInCrcCountInvPortn.setStatus("current")
_Pm10010ulhperfdatacomclientCurrent24StatInCrcCountPortn_Type = Counter64
_Pm10010ulhperfdatacomclientCurrent24StatInCrcCountPortn_Object = MibTableColumn
pm10010ulhperfdatacomclientCurrent24StatInCrcCountPortn = _Pm10010ulhperfdatacomclientCurrent24StatInCrcCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 912, 1, 5),
    _Pm10010ulhperfdatacomclientCurrent24StatInCrcCountPortn_Type()
)
pm10010ulhperfdatacomclientCurrent24StatInCrcCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhperfdatacomclientCurrent24StatInCrcCountPortn.setStatus("current")
_Pm10010ulhperfdatacomclientCurrent24StatInPacketCountInvPortn_Type = EkiOnOff
_Pm10010ulhperfdatacomclientCurrent24StatInPacketCountInvPortn_Object = MibTableColumn
pm10010ulhperfdatacomclientCurrent24StatInPacketCountInvPortn = _Pm10010ulhperfdatacomclientCurrent24StatInPacketCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 912, 1, 6),
    _Pm10010ulhperfdatacomclientCurrent24StatInPacketCountInvPortn_Type()
)
pm10010ulhperfdatacomclientCurrent24StatInPacketCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhperfdatacomclientCurrent24StatInPacketCountInvPortn.setStatus("current")
_Pm10010ulhperfdatacomclientCurrent24StatInPacketCountPortn_Type = Counter64
_Pm10010ulhperfdatacomclientCurrent24StatInPacketCountPortn_Object = MibTableColumn
pm10010ulhperfdatacomclientCurrent24StatInPacketCountPortn = _Pm10010ulhperfdatacomclientCurrent24StatInPacketCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 912, 1, 7),
    _Pm10010ulhperfdatacomclientCurrent24StatInPacketCountPortn_Type()
)
pm10010ulhperfdatacomclientCurrent24StatInPacketCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhperfdatacomclientCurrent24StatInPacketCountPortn.setStatus("current")
_Pm10010ulhperfdatacomclientCurrent24StatOutCrcCountInvPortn_Type = EkiOnOff
_Pm10010ulhperfdatacomclientCurrent24StatOutCrcCountInvPortn_Object = MibTableColumn
pm10010ulhperfdatacomclientCurrent24StatOutCrcCountInvPortn = _Pm10010ulhperfdatacomclientCurrent24StatOutCrcCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 912, 1, 28),
    _Pm10010ulhperfdatacomclientCurrent24StatOutCrcCountInvPortn_Type()
)
pm10010ulhperfdatacomclientCurrent24StatOutCrcCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhperfdatacomclientCurrent24StatOutCrcCountInvPortn.setStatus("current")
_Pm10010ulhperfdatacomclientCurrent24StatOutCrcCountPortn_Type = Counter64
_Pm10010ulhperfdatacomclientCurrent24StatOutCrcCountPortn_Object = MibTableColumn
pm10010ulhperfdatacomclientCurrent24StatOutCrcCountPortn = _Pm10010ulhperfdatacomclientCurrent24StatOutCrcCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 912, 1, 29),
    _Pm10010ulhperfdatacomclientCurrent24StatOutCrcCountPortn_Type()
)
pm10010ulhperfdatacomclientCurrent24StatOutCrcCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhperfdatacomclientCurrent24StatOutCrcCountPortn.setStatus("current")
_Pm10010ulhperfdatacomclientCurrent24StatOutPacketCountInvPortn_Type = EkiOnOff
_Pm10010ulhperfdatacomclientCurrent24StatOutPacketCountInvPortn_Object = MibTableColumn
pm10010ulhperfdatacomclientCurrent24StatOutPacketCountInvPortn = _Pm10010ulhperfdatacomclientCurrent24StatOutPacketCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 912, 1, 30),
    _Pm10010ulhperfdatacomclientCurrent24StatOutPacketCountInvPortn_Type()
)
pm10010ulhperfdatacomclientCurrent24StatOutPacketCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhperfdatacomclientCurrent24StatOutPacketCountInvPortn.setStatus("current")
_Pm10010ulhperfdatacomclientCurrent24StatOutPacketCountPortn_Type = Counter64
_Pm10010ulhperfdatacomclientCurrent24StatOutPacketCountPortn_Object = MibTableColumn
pm10010ulhperfdatacomclientCurrent24StatOutPacketCountPortn = _Pm10010ulhperfdatacomclientCurrent24StatOutPacketCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 912, 1, 31),
    _Pm10010ulhperfdatacomclientCurrent24StatOutPacketCountPortn_Type()
)
pm10010ulhperfdatacomclientCurrent24StatOutPacketCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhperfdatacomclientCurrent24StatOutPacketCountPortn.setStatus("current")
_Pm10010ulhPerfDatacomClientPast24StatHistoryPort1Table_Object = MibTable
pm10010ulhPerfDatacomClientPast24StatHistoryPort1Table = _Pm10010ulhPerfDatacomClientPast24StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 944)
)
if mibBuilder.loadTexts:
    pm10010ulhPerfDatacomClientPast24StatHistoryPort1Table.setStatus("current")
_Pm10010ulhPerfDatacomClientPast24StatHistoryPort1Entry_Object = MibTableRow
pm10010ulhPerfDatacomClientPast24StatHistoryPort1Entry = _Pm10010ulhPerfDatacomClientPast24StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 944, 1)
)
pm10010ulhPerfDatacomClientPast24StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhPerfDatacomClientPast24StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm10010ulhPerfDatacomClientPast24StatHistoryPort1Entry.setStatus("current")


class _Pm10010ulhPerfDatacomClientPast24StatHistoryPort1Index_Type(Integer32):
    """Custom type pm10010ulhPerfDatacomClientPast24StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhPerfDatacomClientPast24StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm10010ulhPerfDatacomClientPast24StatHistoryPort1Index_Object = MibTableColumn
pm10010ulhPerfDatacomClientPast24StatHistoryPort1Index = _Pm10010ulhPerfDatacomClientPast24StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 944, 1, 1),
    _Pm10010ulhPerfDatacomClientPast24StatHistoryPort1Index_Type()
)
pm10010ulhPerfDatacomClientPast24StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfDatacomClientPast24StatHistoryPort1Index.setStatus("current")
_Pm10010ulhperfdatacomclientPast24StatInCrcCountInvPort1_Type = EkiOnOff
_Pm10010ulhperfdatacomclientPast24StatInCrcCountInvPort1_Object = MibTableColumn
pm10010ulhperfdatacomclientPast24StatInCrcCountInvPort1 = _Pm10010ulhperfdatacomclientPast24StatInCrcCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 944, 1, 4),
    _Pm10010ulhperfdatacomclientPast24StatInCrcCountInvPort1_Type()
)
pm10010ulhperfdatacomclientPast24StatInCrcCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhperfdatacomclientPast24StatInCrcCountInvPort1.setStatus("current")
_Pm10010ulhperfdatacomclientPast24StatInCrcCountPort1_Type = Counter64
_Pm10010ulhperfdatacomclientPast24StatInCrcCountPort1_Object = MibTableColumn
pm10010ulhperfdatacomclientPast24StatInCrcCountPort1 = _Pm10010ulhperfdatacomclientPast24StatInCrcCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 944, 1, 5),
    _Pm10010ulhperfdatacomclientPast24StatInCrcCountPort1_Type()
)
pm10010ulhperfdatacomclientPast24StatInCrcCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhperfdatacomclientPast24StatInCrcCountPort1.setStatus("current")
_Pm10010ulhperfdatacomclientPast24StatInPacketCountInvPort1_Type = EkiOnOff
_Pm10010ulhperfdatacomclientPast24StatInPacketCountInvPort1_Object = MibTableColumn
pm10010ulhperfdatacomclientPast24StatInPacketCountInvPort1 = _Pm10010ulhperfdatacomclientPast24StatInPacketCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 944, 1, 6),
    _Pm10010ulhperfdatacomclientPast24StatInPacketCountInvPort1_Type()
)
pm10010ulhperfdatacomclientPast24StatInPacketCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhperfdatacomclientPast24StatInPacketCountInvPort1.setStatus("current")
_Pm10010ulhperfdatacomclientPast24StatInPacketCountPort1_Type = Counter64
_Pm10010ulhperfdatacomclientPast24StatInPacketCountPort1_Object = MibTableColumn
pm10010ulhperfdatacomclientPast24StatInPacketCountPort1 = _Pm10010ulhperfdatacomclientPast24StatInPacketCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 944, 1, 7),
    _Pm10010ulhperfdatacomclientPast24StatInPacketCountPort1_Type()
)
pm10010ulhperfdatacomclientPast24StatInPacketCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhperfdatacomclientPast24StatInPacketCountPort1.setStatus("current")
_Pm10010ulhperfdatacomclientPast24StatOutCrcCountInvPort1_Type = EkiOnOff
_Pm10010ulhperfdatacomclientPast24StatOutCrcCountInvPort1_Object = MibTableColumn
pm10010ulhperfdatacomclientPast24StatOutCrcCountInvPort1 = _Pm10010ulhperfdatacomclientPast24StatOutCrcCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 944, 1, 28),
    _Pm10010ulhperfdatacomclientPast24StatOutCrcCountInvPort1_Type()
)
pm10010ulhperfdatacomclientPast24StatOutCrcCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhperfdatacomclientPast24StatOutCrcCountInvPort1.setStatus("current")
_Pm10010ulhperfdatacomclientPast24StatOutCrcCountPort1_Type = Counter64
_Pm10010ulhperfdatacomclientPast24StatOutCrcCountPort1_Object = MibTableColumn
pm10010ulhperfdatacomclientPast24StatOutCrcCountPort1 = _Pm10010ulhperfdatacomclientPast24StatOutCrcCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 944, 1, 29),
    _Pm10010ulhperfdatacomclientPast24StatOutCrcCountPort1_Type()
)
pm10010ulhperfdatacomclientPast24StatOutCrcCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhperfdatacomclientPast24StatOutCrcCountPort1.setStatus("current")
_Pm10010ulhperfdatacomclientPast24StatOutPacketCountInvPort1_Type = EkiOnOff
_Pm10010ulhperfdatacomclientPast24StatOutPacketCountInvPort1_Object = MibTableColumn
pm10010ulhperfdatacomclientPast24StatOutPacketCountInvPort1 = _Pm10010ulhperfdatacomclientPast24StatOutPacketCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 944, 1, 30),
    _Pm10010ulhperfdatacomclientPast24StatOutPacketCountInvPort1_Type()
)
pm10010ulhperfdatacomclientPast24StatOutPacketCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhperfdatacomclientPast24StatOutPacketCountInvPort1.setStatus("current")
_Pm10010ulhperfdatacomclientPast24StatOutPacketCountPort1_Type = Counter64
_Pm10010ulhperfdatacomclientPast24StatOutPacketCountPort1_Object = MibTableColumn
pm10010ulhperfdatacomclientPast24StatOutPacketCountPort1 = _Pm10010ulhperfdatacomclientPast24StatOutPacketCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 6, 944, 1, 31),
    _Pm10010ulhperfdatacomclientPast24StatOutPacketCountPort1_Type()
)
pm10010ulhperfdatacomclientPast24StatOutPacketCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhperfdatacomclientPast24StatOutPacketCountPort1.setStatus("current")
_Pm10010ulhMonPerfLine_ObjectIdentity = ObjectIdentity
pm10010ulhMonPerfLine = _Pm10010ulhMonPerfLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7)
)
_Pm10010ulhPerfTelecomLinePostFecCurrent15StatTable_Object = MibTable
pm10010ulhPerfTelecomLinePostFecCurrent15StatTable = _Pm10010ulhPerfTelecomLinePostFecCurrent15StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 336)
)
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomLinePostFecCurrent15StatTable.setStatus("current")
_Pm10010ulhPerfTelecomLinePostFecCurrent15StatEntry_Object = MibTableRow
pm10010ulhPerfTelecomLinePostFecCurrent15StatEntry = _Pm10010ulhPerfTelecomLinePostFecCurrent15StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 336, 1)
)
pm10010ulhPerfTelecomLinePostFecCurrent15StatEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhPerfTelecomLinePostFecCurrent15StatIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomLinePostFecCurrent15StatEntry.setStatus("current")


class _Pm10010ulhPerfTelecomLinePostFecCurrent15StatIndex_Type(Integer32):
    """Custom type pm10010ulhPerfTelecomLinePostFecCurrent15StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhPerfTelecomLinePostFecCurrent15StatIndex_Type.__name__ = "Integer32"
_Pm10010ulhPerfTelecomLinePostFecCurrent15StatIndex_Object = MibTableColumn
pm10010ulhPerfTelecomLinePostFecCurrent15StatIndex = _Pm10010ulhPerfTelecomLinePostFecCurrent15StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 336, 1, 1),
    _Pm10010ulhPerfTelecomLinePostFecCurrent15StatIndex_Type()
)
pm10010ulhPerfTelecomLinePostFecCurrent15StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomLinePostFecCurrent15StatIndex.setStatus("current")
_Pm10010ulhPerfTelecomLinePostFecCurrent15StatInvCvPortn_Type = EkiOnOff
_Pm10010ulhPerfTelecomLinePostFecCurrent15StatInvCvPortn_Object = MibTableColumn
pm10010ulhPerfTelecomLinePostFecCurrent15StatInvCvPortn = _Pm10010ulhPerfTelecomLinePostFecCurrent15StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 336, 1, 2),
    _Pm10010ulhPerfTelecomLinePostFecCurrent15StatInvCvPortn_Type()
)
pm10010ulhPerfTelecomLinePostFecCurrent15StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomLinePostFecCurrent15StatInvCvPortn.setStatus("current")
_Pm10010ulhPerfTelecomLinePostFecCurrent15StatCvValuePortn_Type = Unsigned32
_Pm10010ulhPerfTelecomLinePostFecCurrent15StatCvValuePortn_Object = MibTableColumn
pm10010ulhPerfTelecomLinePostFecCurrent15StatCvValuePortn = _Pm10010ulhPerfTelecomLinePostFecCurrent15StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 336, 1, 3),
    _Pm10010ulhPerfTelecomLinePostFecCurrent15StatCvValuePortn_Type()
)
pm10010ulhPerfTelecomLinePostFecCurrent15StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomLinePostFecCurrent15StatCvValuePortn.setStatus("current")
_Pm10010ulhPerfTelecomLinePostFecCurrent15StatInvEsPortn_Type = EkiOnOff
_Pm10010ulhPerfTelecomLinePostFecCurrent15StatInvEsPortn_Object = MibTableColumn
pm10010ulhPerfTelecomLinePostFecCurrent15StatInvEsPortn = _Pm10010ulhPerfTelecomLinePostFecCurrent15StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 336, 1, 4),
    _Pm10010ulhPerfTelecomLinePostFecCurrent15StatInvEsPortn_Type()
)
pm10010ulhPerfTelecomLinePostFecCurrent15StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomLinePostFecCurrent15StatInvEsPortn.setStatus("current")
_Pm10010ulhPerfTelecomLinePostFecCurrent15StatEsValuePortn_Type = Unsigned32
_Pm10010ulhPerfTelecomLinePostFecCurrent15StatEsValuePortn_Object = MibTableColumn
pm10010ulhPerfTelecomLinePostFecCurrent15StatEsValuePortn = _Pm10010ulhPerfTelecomLinePostFecCurrent15StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 336, 1, 5),
    _Pm10010ulhPerfTelecomLinePostFecCurrent15StatEsValuePortn_Type()
)
pm10010ulhPerfTelecomLinePostFecCurrent15StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomLinePostFecCurrent15StatEsValuePortn.setStatus("current")
_Pm10010ulhPerfTelecomLinePostFecCurrent15StatInvSesPortn_Type = EkiOnOff
_Pm10010ulhPerfTelecomLinePostFecCurrent15StatInvSesPortn_Object = MibTableColumn
pm10010ulhPerfTelecomLinePostFecCurrent15StatInvSesPortn = _Pm10010ulhPerfTelecomLinePostFecCurrent15StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 336, 1, 6),
    _Pm10010ulhPerfTelecomLinePostFecCurrent15StatInvSesPortn_Type()
)
pm10010ulhPerfTelecomLinePostFecCurrent15StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomLinePostFecCurrent15StatInvSesPortn.setStatus("current")
_Pm10010ulhPerfTelecomLinePostFecCurrent15StatSesValuePortn_Type = Unsigned32
_Pm10010ulhPerfTelecomLinePostFecCurrent15StatSesValuePortn_Object = MibTableColumn
pm10010ulhPerfTelecomLinePostFecCurrent15StatSesValuePortn = _Pm10010ulhPerfTelecomLinePostFecCurrent15StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 336, 1, 7),
    _Pm10010ulhPerfTelecomLinePostFecCurrent15StatSesValuePortn_Type()
)
pm10010ulhPerfTelecomLinePostFecCurrent15StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomLinePostFecCurrent15StatSesValuePortn.setStatus("current")
_Pm10010ulhPerfTelecomLinePostFecCurrent15StatInvSefsPortn_Type = EkiOnOff
_Pm10010ulhPerfTelecomLinePostFecCurrent15StatInvSefsPortn_Object = MibTableColumn
pm10010ulhPerfTelecomLinePostFecCurrent15StatInvSefsPortn = _Pm10010ulhPerfTelecomLinePostFecCurrent15StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 336, 1, 8),
    _Pm10010ulhPerfTelecomLinePostFecCurrent15StatInvSefsPortn_Type()
)
pm10010ulhPerfTelecomLinePostFecCurrent15StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomLinePostFecCurrent15StatInvSefsPortn.setStatus("current")
_Pm10010ulhPerfTelecomLinePostFecCurrent15StatSefsValuePortn_Type = Unsigned32
_Pm10010ulhPerfTelecomLinePostFecCurrent15StatSefsValuePortn_Object = MibTableColumn
pm10010ulhPerfTelecomLinePostFecCurrent15StatSefsValuePortn = _Pm10010ulhPerfTelecomLinePostFecCurrent15StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 336, 1, 9),
    _Pm10010ulhPerfTelecomLinePostFecCurrent15StatSefsValuePortn_Type()
)
pm10010ulhPerfTelecomLinePostFecCurrent15StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomLinePostFecCurrent15StatSefsValuePortn.setStatus("current")
_Pm10010ulhPerfTelecomLinePostFecCurrent15StatInvUasPortn_Type = EkiOnOff
_Pm10010ulhPerfTelecomLinePostFecCurrent15StatInvUasPortn_Object = MibTableColumn
pm10010ulhPerfTelecomLinePostFecCurrent15StatInvUasPortn = _Pm10010ulhPerfTelecomLinePostFecCurrent15StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 336, 1, 10),
    _Pm10010ulhPerfTelecomLinePostFecCurrent15StatInvUasPortn_Type()
)
pm10010ulhPerfTelecomLinePostFecCurrent15StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomLinePostFecCurrent15StatInvUasPortn.setStatus("current")
_Pm10010ulhPerfTelecomLinePostFecCurrent15StatUasValuePortn_Type = Unsigned32
_Pm10010ulhPerfTelecomLinePostFecCurrent15StatUasValuePortn_Object = MibTableColumn
pm10010ulhPerfTelecomLinePostFecCurrent15StatUasValuePortn = _Pm10010ulhPerfTelecomLinePostFecCurrent15StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 336, 1, 11),
    _Pm10010ulhPerfTelecomLinePostFecCurrent15StatUasValuePortn_Type()
)
pm10010ulhPerfTelecomLinePostFecCurrent15StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomLinePostFecCurrent15StatUasValuePortn.setStatus("current")
_Pm10010ulhPerfTelecomLinePostFecPast15StatHistoryPort1Table_Object = MibTable
pm10010ulhPerfTelecomLinePostFecPast15StatHistoryPort1Table = _Pm10010ulhPerfTelecomLinePostFecPast15StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 337)
)
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomLinePostFecPast15StatHistoryPort1Table.setStatus("current")
_Pm10010ulhPerfTelecomLinePostFecPast15StatHistoryPort1Entry_Object = MibTableRow
pm10010ulhPerfTelecomLinePostFecPast15StatHistoryPort1Entry = _Pm10010ulhPerfTelecomLinePostFecPast15StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 337, 1)
)
pm10010ulhPerfTelecomLinePostFecPast15StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhPerfTelecomLinePostFecPast15StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomLinePostFecPast15StatHistoryPort1Entry.setStatus("current")


class _Pm10010ulhPerfTelecomLinePostFecPast15StatHistoryPort1Index_Type(Integer32):
    """Custom type pm10010ulhPerfTelecomLinePostFecPast15StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhPerfTelecomLinePostFecPast15StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm10010ulhPerfTelecomLinePostFecPast15StatHistoryPort1Index_Object = MibTableColumn
pm10010ulhPerfTelecomLinePostFecPast15StatHistoryPort1Index = _Pm10010ulhPerfTelecomLinePostFecPast15StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 337, 1, 1),
    _Pm10010ulhPerfTelecomLinePostFecPast15StatHistoryPort1Index_Type()
)
pm10010ulhPerfTelecomLinePostFecPast15StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomLinePostFecPast15StatHistoryPort1Index.setStatus("current")
_Pm10010ulhPerfTelecomLinePostFecPast15StatHistoryInvCvPort1_Type = EkiOnOff
_Pm10010ulhPerfTelecomLinePostFecPast15StatHistoryInvCvPort1_Object = MibTableColumn
pm10010ulhPerfTelecomLinePostFecPast15StatHistoryInvCvPort1 = _Pm10010ulhPerfTelecomLinePostFecPast15StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 337, 1, 2),
    _Pm10010ulhPerfTelecomLinePostFecPast15StatHistoryInvCvPort1_Type()
)
pm10010ulhPerfTelecomLinePostFecPast15StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomLinePostFecPast15StatHistoryInvCvPort1.setStatus("current")
_Pm10010ulhPerfTelecomLinePostFecPast15StatHistoryCvValuePort1_Type = Unsigned32
_Pm10010ulhPerfTelecomLinePostFecPast15StatHistoryCvValuePort1_Object = MibTableColumn
pm10010ulhPerfTelecomLinePostFecPast15StatHistoryCvValuePort1 = _Pm10010ulhPerfTelecomLinePostFecPast15StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 337, 1, 3),
    _Pm10010ulhPerfTelecomLinePostFecPast15StatHistoryCvValuePort1_Type()
)
pm10010ulhPerfTelecomLinePostFecPast15StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomLinePostFecPast15StatHistoryCvValuePort1.setStatus("current")
_Pm10010ulhPerfTelecomLinePostFecPast15StatHistoryInvEsPort1_Type = EkiOnOff
_Pm10010ulhPerfTelecomLinePostFecPast15StatHistoryInvEsPort1_Object = MibTableColumn
pm10010ulhPerfTelecomLinePostFecPast15StatHistoryInvEsPort1 = _Pm10010ulhPerfTelecomLinePostFecPast15StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 337, 1, 4),
    _Pm10010ulhPerfTelecomLinePostFecPast15StatHistoryInvEsPort1_Type()
)
pm10010ulhPerfTelecomLinePostFecPast15StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomLinePostFecPast15StatHistoryInvEsPort1.setStatus("current")
_Pm10010ulhPerfTelecomLinePostFecPast15StatHistoryEsValuePort1_Type = Unsigned32
_Pm10010ulhPerfTelecomLinePostFecPast15StatHistoryEsValuePort1_Object = MibTableColumn
pm10010ulhPerfTelecomLinePostFecPast15StatHistoryEsValuePort1 = _Pm10010ulhPerfTelecomLinePostFecPast15StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 337, 1, 5),
    _Pm10010ulhPerfTelecomLinePostFecPast15StatHistoryEsValuePort1_Type()
)
pm10010ulhPerfTelecomLinePostFecPast15StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomLinePostFecPast15StatHistoryEsValuePort1.setStatus("current")
_Pm10010ulhPerfTelecomLinePostFecPast15StatHistoryInvSesPort1_Type = EkiOnOff
_Pm10010ulhPerfTelecomLinePostFecPast15StatHistoryInvSesPort1_Object = MibTableColumn
pm10010ulhPerfTelecomLinePostFecPast15StatHistoryInvSesPort1 = _Pm10010ulhPerfTelecomLinePostFecPast15StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 337, 1, 6),
    _Pm10010ulhPerfTelecomLinePostFecPast15StatHistoryInvSesPort1_Type()
)
pm10010ulhPerfTelecomLinePostFecPast15StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomLinePostFecPast15StatHistoryInvSesPort1.setStatus("current")
_Pm10010ulhPerfTelecomLinePostFecPast15StatHistorySesValuePort1_Type = Unsigned32
_Pm10010ulhPerfTelecomLinePostFecPast15StatHistorySesValuePort1_Object = MibTableColumn
pm10010ulhPerfTelecomLinePostFecPast15StatHistorySesValuePort1 = _Pm10010ulhPerfTelecomLinePostFecPast15StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 337, 1, 7),
    _Pm10010ulhPerfTelecomLinePostFecPast15StatHistorySesValuePort1_Type()
)
pm10010ulhPerfTelecomLinePostFecPast15StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomLinePostFecPast15StatHistorySesValuePort1.setStatus("current")
_Pm10010ulhPerfTelecomLinePostFecPast15StatHistoryInvSefsPort1_Type = EkiOnOff
_Pm10010ulhPerfTelecomLinePostFecPast15StatHistoryInvSefsPort1_Object = MibTableColumn
pm10010ulhPerfTelecomLinePostFecPast15StatHistoryInvSefsPort1 = _Pm10010ulhPerfTelecomLinePostFecPast15StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 337, 1, 8),
    _Pm10010ulhPerfTelecomLinePostFecPast15StatHistoryInvSefsPort1_Type()
)
pm10010ulhPerfTelecomLinePostFecPast15StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomLinePostFecPast15StatHistoryInvSefsPort1.setStatus("current")
_Pm10010ulhPerfTelecomLinePostFecPast15StatHistorySefsValuePort1_Type = Unsigned32
_Pm10010ulhPerfTelecomLinePostFecPast15StatHistorySefsValuePort1_Object = MibTableColumn
pm10010ulhPerfTelecomLinePostFecPast15StatHistorySefsValuePort1 = _Pm10010ulhPerfTelecomLinePostFecPast15StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 337, 1, 9),
    _Pm10010ulhPerfTelecomLinePostFecPast15StatHistorySefsValuePort1_Type()
)
pm10010ulhPerfTelecomLinePostFecPast15StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomLinePostFecPast15StatHistorySefsValuePort1.setStatus("current")
_Pm10010ulhPerfTelecomLinePostFecPast15StatHistoryInvUasPort1_Type = EkiOnOff
_Pm10010ulhPerfTelecomLinePostFecPast15StatHistoryInvUasPort1_Object = MibTableColumn
pm10010ulhPerfTelecomLinePostFecPast15StatHistoryInvUasPort1 = _Pm10010ulhPerfTelecomLinePostFecPast15StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 337, 1, 10),
    _Pm10010ulhPerfTelecomLinePostFecPast15StatHistoryInvUasPort1_Type()
)
pm10010ulhPerfTelecomLinePostFecPast15StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomLinePostFecPast15StatHistoryInvUasPort1.setStatus("current")
_Pm10010ulhPerfTelecomLinePostFecPast15StatHistoryUasValuePort1_Type = Unsigned32
_Pm10010ulhPerfTelecomLinePostFecPast15StatHistoryUasValuePort1_Object = MibTableColumn
pm10010ulhPerfTelecomLinePostFecPast15StatHistoryUasValuePort1 = _Pm10010ulhPerfTelecomLinePostFecPast15StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 337, 1, 11),
    _Pm10010ulhPerfTelecomLinePostFecPast15StatHistoryUasValuePort1_Type()
)
pm10010ulhPerfTelecomLinePostFecPast15StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomLinePostFecPast15StatHistoryUasValuePort1.setStatus("current")
_Pm10010ulhPerfTelecomLinePostFecCurrent24StatTable_Object = MibTable
pm10010ulhPerfTelecomLinePostFecCurrent24StatTable = _Pm10010ulhPerfTelecomLinePostFecCurrent24StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 338)
)
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomLinePostFecCurrent24StatTable.setStatus("current")
_Pm10010ulhPerfTelecomLinePostFecCurrent24StatEntry_Object = MibTableRow
pm10010ulhPerfTelecomLinePostFecCurrent24StatEntry = _Pm10010ulhPerfTelecomLinePostFecCurrent24StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 338, 1)
)
pm10010ulhPerfTelecomLinePostFecCurrent24StatEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhPerfTelecomLinePostFecCurrent24StatIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomLinePostFecCurrent24StatEntry.setStatus("current")


class _Pm10010ulhPerfTelecomLinePostFecCurrent24StatIndex_Type(Integer32):
    """Custom type pm10010ulhPerfTelecomLinePostFecCurrent24StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhPerfTelecomLinePostFecCurrent24StatIndex_Type.__name__ = "Integer32"
_Pm10010ulhPerfTelecomLinePostFecCurrent24StatIndex_Object = MibTableColumn
pm10010ulhPerfTelecomLinePostFecCurrent24StatIndex = _Pm10010ulhPerfTelecomLinePostFecCurrent24StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 338, 1, 1),
    _Pm10010ulhPerfTelecomLinePostFecCurrent24StatIndex_Type()
)
pm10010ulhPerfTelecomLinePostFecCurrent24StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomLinePostFecCurrent24StatIndex.setStatus("current")
_Pm10010ulhPerfTelecomLinePostFecCurrent24StatInvCvPortn_Type = EkiOnOff
_Pm10010ulhPerfTelecomLinePostFecCurrent24StatInvCvPortn_Object = MibTableColumn
pm10010ulhPerfTelecomLinePostFecCurrent24StatInvCvPortn = _Pm10010ulhPerfTelecomLinePostFecCurrent24StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 338, 1, 2),
    _Pm10010ulhPerfTelecomLinePostFecCurrent24StatInvCvPortn_Type()
)
pm10010ulhPerfTelecomLinePostFecCurrent24StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomLinePostFecCurrent24StatInvCvPortn.setStatus("current")
_Pm10010ulhPerfTelecomLinePostFecCurrent24StatCvValuePortn_Type = Unsigned32
_Pm10010ulhPerfTelecomLinePostFecCurrent24StatCvValuePortn_Object = MibTableColumn
pm10010ulhPerfTelecomLinePostFecCurrent24StatCvValuePortn = _Pm10010ulhPerfTelecomLinePostFecCurrent24StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 338, 1, 3),
    _Pm10010ulhPerfTelecomLinePostFecCurrent24StatCvValuePortn_Type()
)
pm10010ulhPerfTelecomLinePostFecCurrent24StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomLinePostFecCurrent24StatCvValuePortn.setStatus("current")
_Pm10010ulhPerfTelecomLinePostFecCurrent24StatInvEsPortn_Type = EkiOnOff
_Pm10010ulhPerfTelecomLinePostFecCurrent24StatInvEsPortn_Object = MibTableColumn
pm10010ulhPerfTelecomLinePostFecCurrent24StatInvEsPortn = _Pm10010ulhPerfTelecomLinePostFecCurrent24StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 338, 1, 4),
    _Pm10010ulhPerfTelecomLinePostFecCurrent24StatInvEsPortn_Type()
)
pm10010ulhPerfTelecomLinePostFecCurrent24StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomLinePostFecCurrent24StatInvEsPortn.setStatus("current")
_Pm10010ulhPerfTelecomLinePostFecCurrent24StatEsValuePortn_Type = Unsigned32
_Pm10010ulhPerfTelecomLinePostFecCurrent24StatEsValuePortn_Object = MibTableColumn
pm10010ulhPerfTelecomLinePostFecCurrent24StatEsValuePortn = _Pm10010ulhPerfTelecomLinePostFecCurrent24StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 338, 1, 5),
    _Pm10010ulhPerfTelecomLinePostFecCurrent24StatEsValuePortn_Type()
)
pm10010ulhPerfTelecomLinePostFecCurrent24StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomLinePostFecCurrent24StatEsValuePortn.setStatus("current")
_Pm10010ulhPerfTelecomLinePostFecCurrent24StatInvSesPortn_Type = EkiOnOff
_Pm10010ulhPerfTelecomLinePostFecCurrent24StatInvSesPortn_Object = MibTableColumn
pm10010ulhPerfTelecomLinePostFecCurrent24StatInvSesPortn = _Pm10010ulhPerfTelecomLinePostFecCurrent24StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 338, 1, 6),
    _Pm10010ulhPerfTelecomLinePostFecCurrent24StatInvSesPortn_Type()
)
pm10010ulhPerfTelecomLinePostFecCurrent24StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomLinePostFecCurrent24StatInvSesPortn.setStatus("current")
_Pm10010ulhPerfTelecomLinePostFecCurrent24StatSesValuePortn_Type = Unsigned32
_Pm10010ulhPerfTelecomLinePostFecCurrent24StatSesValuePortn_Object = MibTableColumn
pm10010ulhPerfTelecomLinePostFecCurrent24StatSesValuePortn = _Pm10010ulhPerfTelecomLinePostFecCurrent24StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 338, 1, 7),
    _Pm10010ulhPerfTelecomLinePostFecCurrent24StatSesValuePortn_Type()
)
pm10010ulhPerfTelecomLinePostFecCurrent24StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomLinePostFecCurrent24StatSesValuePortn.setStatus("current")
_Pm10010ulhPerfTelecomLinePostFecCurrent24StatInvSefsPortn_Type = EkiOnOff
_Pm10010ulhPerfTelecomLinePostFecCurrent24StatInvSefsPortn_Object = MibTableColumn
pm10010ulhPerfTelecomLinePostFecCurrent24StatInvSefsPortn = _Pm10010ulhPerfTelecomLinePostFecCurrent24StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 338, 1, 8),
    _Pm10010ulhPerfTelecomLinePostFecCurrent24StatInvSefsPortn_Type()
)
pm10010ulhPerfTelecomLinePostFecCurrent24StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomLinePostFecCurrent24StatInvSefsPortn.setStatus("current")
_Pm10010ulhPerfTelecomLinePostFecCurrent24StatSefsValuePortn_Type = Unsigned32
_Pm10010ulhPerfTelecomLinePostFecCurrent24StatSefsValuePortn_Object = MibTableColumn
pm10010ulhPerfTelecomLinePostFecCurrent24StatSefsValuePortn = _Pm10010ulhPerfTelecomLinePostFecCurrent24StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 338, 1, 9),
    _Pm10010ulhPerfTelecomLinePostFecCurrent24StatSefsValuePortn_Type()
)
pm10010ulhPerfTelecomLinePostFecCurrent24StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomLinePostFecCurrent24StatSefsValuePortn.setStatus("current")
_Pm10010ulhPerfTelecomLinePostFecCurrent24StatInvUasPortn_Type = EkiOnOff
_Pm10010ulhPerfTelecomLinePostFecCurrent24StatInvUasPortn_Object = MibTableColumn
pm10010ulhPerfTelecomLinePostFecCurrent24StatInvUasPortn = _Pm10010ulhPerfTelecomLinePostFecCurrent24StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 338, 1, 10),
    _Pm10010ulhPerfTelecomLinePostFecCurrent24StatInvUasPortn_Type()
)
pm10010ulhPerfTelecomLinePostFecCurrent24StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomLinePostFecCurrent24StatInvUasPortn.setStatus("current")
_Pm10010ulhPerfTelecomLinePostFecCurrent24StatUasValuePortn_Type = Unsigned32
_Pm10010ulhPerfTelecomLinePostFecCurrent24StatUasValuePortn_Object = MibTableColumn
pm10010ulhPerfTelecomLinePostFecCurrent24StatUasValuePortn = _Pm10010ulhPerfTelecomLinePostFecCurrent24StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 338, 1, 11),
    _Pm10010ulhPerfTelecomLinePostFecCurrent24StatUasValuePortn_Type()
)
pm10010ulhPerfTelecomLinePostFecCurrent24StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomLinePostFecCurrent24StatUasValuePortn.setStatus("current")
_Pm10010ulhPerfTelecomLinePostFecPast24StatHistoryPort1Table_Object = MibTable
pm10010ulhPerfTelecomLinePostFecPast24StatHistoryPort1Table = _Pm10010ulhPerfTelecomLinePostFecPast24StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 339)
)
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomLinePostFecPast24StatHistoryPort1Table.setStatus("current")
_Pm10010ulhPerfTelecomLinePostFecPast24StatHistoryPort1Entry_Object = MibTableRow
pm10010ulhPerfTelecomLinePostFecPast24StatHistoryPort1Entry = _Pm10010ulhPerfTelecomLinePostFecPast24StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 339, 1)
)
pm10010ulhPerfTelecomLinePostFecPast24StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhPerfTelecomLinePostFecPast24StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomLinePostFecPast24StatHistoryPort1Entry.setStatus("current")


class _Pm10010ulhPerfTelecomLinePostFecPast24StatHistoryPort1Index_Type(Integer32):
    """Custom type pm10010ulhPerfTelecomLinePostFecPast24StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhPerfTelecomLinePostFecPast24StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm10010ulhPerfTelecomLinePostFecPast24StatHistoryPort1Index_Object = MibTableColumn
pm10010ulhPerfTelecomLinePostFecPast24StatHistoryPort1Index = _Pm10010ulhPerfTelecomLinePostFecPast24StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 339, 1, 1),
    _Pm10010ulhPerfTelecomLinePostFecPast24StatHistoryPort1Index_Type()
)
pm10010ulhPerfTelecomLinePostFecPast24StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomLinePostFecPast24StatHistoryPort1Index.setStatus("current")
_Pm10010ulhPerfTelecomLinePostFecPast24StatHistoryInvCvPort1_Type = EkiOnOff
_Pm10010ulhPerfTelecomLinePostFecPast24StatHistoryInvCvPort1_Object = MibTableColumn
pm10010ulhPerfTelecomLinePostFecPast24StatHistoryInvCvPort1 = _Pm10010ulhPerfTelecomLinePostFecPast24StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 339, 1, 2),
    _Pm10010ulhPerfTelecomLinePostFecPast24StatHistoryInvCvPort1_Type()
)
pm10010ulhPerfTelecomLinePostFecPast24StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomLinePostFecPast24StatHistoryInvCvPort1.setStatus("current")
_Pm10010ulhPerfTelecomLinePostFecPast24StatHistoryCvValuePort1_Type = Unsigned32
_Pm10010ulhPerfTelecomLinePostFecPast24StatHistoryCvValuePort1_Object = MibTableColumn
pm10010ulhPerfTelecomLinePostFecPast24StatHistoryCvValuePort1 = _Pm10010ulhPerfTelecomLinePostFecPast24StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 339, 1, 3),
    _Pm10010ulhPerfTelecomLinePostFecPast24StatHistoryCvValuePort1_Type()
)
pm10010ulhPerfTelecomLinePostFecPast24StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomLinePostFecPast24StatHistoryCvValuePort1.setStatus("current")
_Pm10010ulhPerfTelecomLinePostFecPast24StatHistoryInvEsPort1_Type = EkiOnOff
_Pm10010ulhPerfTelecomLinePostFecPast24StatHistoryInvEsPort1_Object = MibTableColumn
pm10010ulhPerfTelecomLinePostFecPast24StatHistoryInvEsPort1 = _Pm10010ulhPerfTelecomLinePostFecPast24StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 339, 1, 4),
    _Pm10010ulhPerfTelecomLinePostFecPast24StatHistoryInvEsPort1_Type()
)
pm10010ulhPerfTelecomLinePostFecPast24StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomLinePostFecPast24StatHistoryInvEsPort1.setStatus("current")
_Pm10010ulhPerfTelecomLinePostFecPast24StatHistoryEsValuePort1_Type = Unsigned32
_Pm10010ulhPerfTelecomLinePostFecPast24StatHistoryEsValuePort1_Object = MibTableColumn
pm10010ulhPerfTelecomLinePostFecPast24StatHistoryEsValuePort1 = _Pm10010ulhPerfTelecomLinePostFecPast24StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 339, 1, 5),
    _Pm10010ulhPerfTelecomLinePostFecPast24StatHistoryEsValuePort1_Type()
)
pm10010ulhPerfTelecomLinePostFecPast24StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomLinePostFecPast24StatHistoryEsValuePort1.setStatus("current")
_Pm10010ulhPerfTelecomLinePostFecPast24StatHistoryInvSesPort1_Type = EkiOnOff
_Pm10010ulhPerfTelecomLinePostFecPast24StatHistoryInvSesPort1_Object = MibTableColumn
pm10010ulhPerfTelecomLinePostFecPast24StatHistoryInvSesPort1 = _Pm10010ulhPerfTelecomLinePostFecPast24StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 339, 1, 6),
    _Pm10010ulhPerfTelecomLinePostFecPast24StatHistoryInvSesPort1_Type()
)
pm10010ulhPerfTelecomLinePostFecPast24StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomLinePostFecPast24StatHistoryInvSesPort1.setStatus("current")
_Pm10010ulhPerfTelecomLinePostFecPast24StatHistorySesValuePort1_Type = Unsigned32
_Pm10010ulhPerfTelecomLinePostFecPast24StatHistorySesValuePort1_Object = MibTableColumn
pm10010ulhPerfTelecomLinePostFecPast24StatHistorySesValuePort1 = _Pm10010ulhPerfTelecomLinePostFecPast24StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 339, 1, 7),
    _Pm10010ulhPerfTelecomLinePostFecPast24StatHistorySesValuePort1_Type()
)
pm10010ulhPerfTelecomLinePostFecPast24StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomLinePostFecPast24StatHistorySesValuePort1.setStatus("current")
_Pm10010ulhPerfTelecomLinePostFecPast24StatHistoryInvSefsPort1_Type = EkiOnOff
_Pm10010ulhPerfTelecomLinePostFecPast24StatHistoryInvSefsPort1_Object = MibTableColumn
pm10010ulhPerfTelecomLinePostFecPast24StatHistoryInvSefsPort1 = _Pm10010ulhPerfTelecomLinePostFecPast24StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 339, 1, 8),
    _Pm10010ulhPerfTelecomLinePostFecPast24StatHistoryInvSefsPort1_Type()
)
pm10010ulhPerfTelecomLinePostFecPast24StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomLinePostFecPast24StatHistoryInvSefsPort1.setStatus("current")
_Pm10010ulhPerfTelecomLinePostFecPast24StatHistorySefsValuePort1_Type = Unsigned32
_Pm10010ulhPerfTelecomLinePostFecPast24StatHistorySefsValuePort1_Object = MibTableColumn
pm10010ulhPerfTelecomLinePostFecPast24StatHistorySefsValuePort1 = _Pm10010ulhPerfTelecomLinePostFecPast24StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 339, 1, 9),
    _Pm10010ulhPerfTelecomLinePostFecPast24StatHistorySefsValuePort1_Type()
)
pm10010ulhPerfTelecomLinePostFecPast24StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomLinePostFecPast24StatHistorySefsValuePort1.setStatus("current")
_Pm10010ulhPerfTelecomLinePostFecPast24StatHistoryInvUasPort1_Type = EkiOnOff
_Pm10010ulhPerfTelecomLinePostFecPast24StatHistoryInvUasPort1_Object = MibTableColumn
pm10010ulhPerfTelecomLinePostFecPast24StatHistoryInvUasPort1 = _Pm10010ulhPerfTelecomLinePostFecPast24StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 339, 1, 10),
    _Pm10010ulhPerfTelecomLinePostFecPast24StatHistoryInvUasPort1_Type()
)
pm10010ulhPerfTelecomLinePostFecPast24StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomLinePostFecPast24StatHistoryInvUasPort1.setStatus("current")
_Pm10010ulhPerfTelecomLinePostFecPast24StatHistoryUasValuePort1_Type = Unsigned32
_Pm10010ulhPerfTelecomLinePostFecPast24StatHistoryUasValuePort1_Object = MibTableColumn
pm10010ulhPerfTelecomLinePostFecPast24StatHistoryUasValuePort1 = _Pm10010ulhPerfTelecomLinePostFecPast24StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 339, 1, 11),
    _Pm10010ulhPerfTelecomLinePostFecPast24StatHistoryUasValuePort1_Type()
)
pm10010ulhPerfTelecomLinePostFecPast24StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomLinePostFecPast24StatHistoryUasValuePort1.setStatus("current")
_Pm10010ulhPerfTelecomBerLinePreFecCurrent15StatTable_Object = MibTable
pm10010ulhPerfTelecomBerLinePreFecCurrent15StatTable = _Pm10010ulhPerfTelecomBerLinePreFecCurrent15StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 352)
)
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomBerLinePreFecCurrent15StatTable.setStatus("current")
_Pm10010ulhPerfTelecomBerLinePreFecCurrent15StatEntry_Object = MibTableRow
pm10010ulhPerfTelecomBerLinePreFecCurrent15StatEntry = _Pm10010ulhPerfTelecomBerLinePreFecCurrent15StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 352, 1)
)
pm10010ulhPerfTelecomBerLinePreFecCurrent15StatEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhPerfTelecomBerLinePreFecCurrent15StatIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomBerLinePreFecCurrent15StatEntry.setStatus("current")


class _Pm10010ulhPerfTelecomBerLinePreFecCurrent15StatIndex_Type(Integer32):
    """Custom type pm10010ulhPerfTelecomBerLinePreFecCurrent15StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhPerfTelecomBerLinePreFecCurrent15StatIndex_Type.__name__ = "Integer32"
_Pm10010ulhPerfTelecomBerLinePreFecCurrent15StatIndex_Object = MibTableColumn
pm10010ulhPerfTelecomBerLinePreFecCurrent15StatIndex = _Pm10010ulhPerfTelecomBerLinePreFecCurrent15StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 352, 1, 1),
    _Pm10010ulhPerfTelecomBerLinePreFecCurrent15StatIndex_Type()
)
pm10010ulhPerfTelecomBerLinePreFecCurrent15StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomBerLinePreFecCurrent15StatIndex.setStatus("current")
_Pm10010ulhPerfTelecomBerLinePreFecCurrent15StatInvBerPortn_Type = EkiOnOff
_Pm10010ulhPerfTelecomBerLinePreFecCurrent15StatInvBerPortn_Object = MibTableColumn
pm10010ulhPerfTelecomBerLinePreFecCurrent15StatInvBerPortn = _Pm10010ulhPerfTelecomBerLinePreFecCurrent15StatInvBerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 352, 1, 2),
    _Pm10010ulhPerfTelecomBerLinePreFecCurrent15StatInvBerPortn_Type()
)
pm10010ulhPerfTelecomBerLinePreFecCurrent15StatInvBerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomBerLinePreFecCurrent15StatInvBerPortn.setStatus("current")
_Pm10010ulhPerfTelecomBerLinePreFecCurrent15StatBerValuePortn_Type = Unsigned32
_Pm10010ulhPerfTelecomBerLinePreFecCurrent15StatBerValuePortn_Object = MibTableColumn
pm10010ulhPerfTelecomBerLinePreFecCurrent15StatBerValuePortn = _Pm10010ulhPerfTelecomBerLinePreFecCurrent15StatBerValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 352, 1, 3),
    _Pm10010ulhPerfTelecomBerLinePreFecCurrent15StatBerValuePortn_Type()
)
pm10010ulhPerfTelecomBerLinePreFecCurrent15StatBerValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomBerLinePreFecCurrent15StatBerValuePortn.setStatus("current")
_Pm10010ulhPerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn_Type = EkiOnOff
_Pm10010ulhPerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn_Object = MibTableColumn
pm10010ulhPerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn = _Pm10010ulhPerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 352, 1, 4),
    _Pm10010ulhPerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn_Type()
)
pm10010ulhPerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn.setStatus("current")
_Pm10010ulhPerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn_Type = Unsigned32
_Pm10010ulhPerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn_Object = MibTableColumn
pm10010ulhPerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn = _Pm10010ulhPerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 352, 1, 5),
    _Pm10010ulhPerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn_Type()
)
pm10010ulhPerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn.setStatus("current")
_Pm10010ulhPerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn_Type = EkiOnOff
_Pm10010ulhPerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn_Object = MibTableColumn
pm10010ulhPerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn = _Pm10010ulhPerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 352, 1, 6),
    _Pm10010ulhPerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn_Type()
)
pm10010ulhPerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn.setStatus("current")
_Pm10010ulhPerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn_Type = Unsigned32
_Pm10010ulhPerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn_Object = MibTableColumn
pm10010ulhPerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn = _Pm10010ulhPerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 352, 1, 7),
    _Pm10010ulhPerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn_Type()
)
pm10010ulhPerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn.setStatus("current")
_Pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryPort1Table_Object = MibTable
pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryPort1Table = _Pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 353)
)
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryPort1Table.setStatus("current")
_Pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryPort1Entry_Object = MibTableRow
pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryPort1Entry = _Pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 353, 1)
)
pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryPort1Entry.setStatus("current")


class _Pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryPort1Index_Type(Integer32):
    """Custom type pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryPort1Index_Object = MibTableColumn
pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryPort1Index = _Pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 353, 1, 1),
    _Pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryPort1Index_Type()
)
pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryPort1Index.setStatus("current")
_Pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1_Type = EkiOnOff
_Pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1_Object = MibTableColumn
pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1 = _Pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 353, 1, 2),
    _Pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1_Type()
)
pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1.setStatus("current")
_Pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1_Type = Unsigned32
_Pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1_Object = MibTableColumn
pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1 = _Pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 353, 1, 3),
    _Pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1_Type()
)
pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1.setStatus("current")
_Pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1_Type = EkiOnOff
_Pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1_Object = MibTableColumn
pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1 = _Pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 353, 1, 4),
    _Pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1_Type()
)
pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1.setStatus("current")
_Pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1_Type = Unsigned32
_Pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1_Object = MibTableColumn
pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1 = _Pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 353, 1, 5),
    _Pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1_Type()
)
pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1.setStatus("current")
_Pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1_Type = EkiOnOff
_Pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1_Object = MibTableColumn
pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1 = _Pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 353, 1, 6),
    _Pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1_Type()
)
pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1.setStatus("current")
_Pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1_Type = Unsigned32
_Pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1_Object = MibTableColumn
pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1 = _Pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 353, 1, 7),
    _Pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1_Type()
)
pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1.setStatus("current")
_Pm10010ulhPerfTelecomBerLinePreFecCurrent24StatTable_Object = MibTable
pm10010ulhPerfTelecomBerLinePreFecCurrent24StatTable = _Pm10010ulhPerfTelecomBerLinePreFecCurrent24StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 354)
)
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomBerLinePreFecCurrent24StatTable.setStatus("current")
_Pm10010ulhPerfTelecomBerLinePreFecCurrent24StatEntry_Object = MibTableRow
pm10010ulhPerfTelecomBerLinePreFecCurrent24StatEntry = _Pm10010ulhPerfTelecomBerLinePreFecCurrent24StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 354, 1)
)
pm10010ulhPerfTelecomBerLinePreFecCurrent24StatEntry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhPerfTelecomBerLinePreFecCurrent24StatIndex"),
)
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomBerLinePreFecCurrent24StatEntry.setStatus("current")


class _Pm10010ulhPerfTelecomBerLinePreFecCurrent24StatIndex_Type(Integer32):
    """Custom type pm10010ulhPerfTelecomBerLinePreFecCurrent24StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhPerfTelecomBerLinePreFecCurrent24StatIndex_Type.__name__ = "Integer32"
_Pm10010ulhPerfTelecomBerLinePreFecCurrent24StatIndex_Object = MibTableColumn
pm10010ulhPerfTelecomBerLinePreFecCurrent24StatIndex = _Pm10010ulhPerfTelecomBerLinePreFecCurrent24StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 354, 1, 1),
    _Pm10010ulhPerfTelecomBerLinePreFecCurrent24StatIndex_Type()
)
pm10010ulhPerfTelecomBerLinePreFecCurrent24StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomBerLinePreFecCurrent24StatIndex.setStatus("current")
_Pm10010ulhPerfTelecomBerLinePreFecCurrent24StatInvBerPortn_Type = EkiOnOff
_Pm10010ulhPerfTelecomBerLinePreFecCurrent24StatInvBerPortn_Object = MibTableColumn
pm10010ulhPerfTelecomBerLinePreFecCurrent24StatInvBerPortn = _Pm10010ulhPerfTelecomBerLinePreFecCurrent24StatInvBerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 354, 1, 2),
    _Pm10010ulhPerfTelecomBerLinePreFecCurrent24StatInvBerPortn_Type()
)
pm10010ulhPerfTelecomBerLinePreFecCurrent24StatInvBerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomBerLinePreFecCurrent24StatInvBerPortn.setStatus("current")
_Pm10010ulhPerfTelecomBerLinePreFecCurrent24StatBerValuePortn_Type = Unsigned32
_Pm10010ulhPerfTelecomBerLinePreFecCurrent24StatBerValuePortn_Object = MibTableColumn
pm10010ulhPerfTelecomBerLinePreFecCurrent24StatBerValuePortn = _Pm10010ulhPerfTelecomBerLinePreFecCurrent24StatBerValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 354, 1, 3),
    _Pm10010ulhPerfTelecomBerLinePreFecCurrent24StatBerValuePortn_Type()
)
pm10010ulhPerfTelecomBerLinePreFecCurrent24StatBerValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomBerLinePreFecCurrent24StatBerValuePortn.setStatus("current")
_Pm10010ulhPerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn_Type = EkiOnOff
_Pm10010ulhPerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn_Object = MibTableColumn
pm10010ulhPerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn = _Pm10010ulhPerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 354, 1, 4),
    _Pm10010ulhPerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn_Type()
)
pm10010ulhPerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn.setStatus("current")
_Pm10010ulhPerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn_Type = Unsigned32
_Pm10010ulhPerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn_Object = MibTableColumn
pm10010ulhPerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn = _Pm10010ulhPerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 354, 1, 5),
    _Pm10010ulhPerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn_Type()
)
pm10010ulhPerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn.setStatus("current")
_Pm10010ulhPerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn_Type = EkiOnOff
_Pm10010ulhPerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn_Object = MibTableColumn
pm10010ulhPerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn = _Pm10010ulhPerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 354, 1, 6),
    _Pm10010ulhPerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn_Type()
)
pm10010ulhPerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn.setStatus("current")
_Pm10010ulhPerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn_Type = Unsigned32
_Pm10010ulhPerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn_Object = MibTableColumn
pm10010ulhPerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn = _Pm10010ulhPerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 354, 1, 7),
    _Pm10010ulhPerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn_Type()
)
pm10010ulhPerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn.setStatus("current")
_Pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryPort1Table_Object = MibTable
pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryPort1Table = _Pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 355)
)
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryPort1Table.setStatus("current")
_Pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryPort1Entry_Object = MibTableRow
pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryPort1Entry = _Pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 355, 1)
)
pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm10010ulh-MIB", "pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryPort1Entry.setStatus("current")


class _Pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryPort1Index_Type(Integer32):
    """Custom type pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryPort1Index_Object = MibTableColumn
pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryPort1Index = _Pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 355, 1, 1),
    _Pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryPort1Index_Type()
)
pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryPort1Index.setStatus("current")
_Pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1_Type = EkiOnOff
_Pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1_Object = MibTableColumn
pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1 = _Pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 355, 1, 2),
    _Pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1_Type()
)
pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1.setStatus("current")
_Pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1_Type = Unsigned32
_Pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1_Object = MibTableColumn
pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1 = _Pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 355, 1, 3),
    _Pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1_Type()
)
pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1.setStatus("current")
_Pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1_Type = EkiOnOff
_Pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1_Object = MibTableColumn
pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1 = _Pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 355, 1, 4),
    _Pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1_Type()
)
pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1.setStatus("current")
_Pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1_Type = Unsigned32
_Pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1_Object = MibTableColumn
pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1 = _Pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 355, 1, 5),
    _Pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1_Type()
)
pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1.setStatus("current")
_Pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1_Type = EkiOnOff
_Pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1_Object = MibTableColumn
pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1 = _Pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 355, 1, 6),
    _Pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1_Type()
)
pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1.setStatus("current")
_Pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1_Type = Unsigned32
_Pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1_Object = MibTableColumn
pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1 = _Pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 80, 11, 7, 355, 1, 7),
    _Pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1_Type()
)
pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1.setStatus("current")

# Managed Objects groups


# Notification objects

pm10010ulhLineTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 80, 10, 30)
)
pm10010ulhLineTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm10010ulh-MIB", "pm10010ulhAlmLineDdmWarningPortn"),
        ("EKINOPS-Pm10010ulh-MIB", "pm10010ulhtrapLineNumber"),
        ("EKINOPS-Pm10010ulh-MIB", "pm10010ulhtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10010ulhLineTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pm10010ulhLineTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 80, 10, 31)
)
pm10010ulhLineTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm10010ulh-MIB", "pm10010ulhAlmLineDdmWarningPortn"),
        ("EKINOPS-Pm10010ulh-MIB", "pm10010ulhtrapLineNumber"),
        ("EKINOPS-Pm10010ulh-MIB", "pm10010ulhtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10010ulhLineTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pm10010ulhLineTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 80, 10, 32)
)
pm10010ulhLineTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm10010ulh-MIB", "pm10010ulhAlmLineDdmAlmPortn"),
        ("EKINOPS-Pm10010ulh-MIB", "pm10010ulhtrapLineNumber"),
        ("EKINOPS-Pm10010ulh-MIB", "pm10010ulhtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10010ulhLineTrapUrgentGoesOn.setStatus(
        "current"
    )

pm10010ulhLineTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 80, 10, 33)
)
pm10010ulhLineTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm10010ulh-MIB", "pm10010ulhAlmLineDdmAlmPortn"),
        ("EKINOPS-Pm10010ulh-MIB", "pm10010ulhtrapLineNumber"),
        ("EKINOPS-Pm10010ulh-MIB", "pm10010ulhtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10010ulhLineTrapUrgentGoesOff.setStatus(
        "current"
    )

pm10010ulhLineTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 80, 10, 34)
)
pm10010ulhLineTrapCritGoesOn.setObjects(
      *(("EKINOPS-Pm10010ulh-MIB", "pm10010ulhAlmLineFailPortn"),
        ("EKINOPS-Pm10010ulh-MIB", "pm10010ulhAlmLineHwFailPortn"),
        ("EKINOPS-Pm10010ulh-MIB", "pm10010ulhtrapLineNumber"),
        ("EKINOPS-Pm10010ulh-MIB", "pm10010ulhtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10010ulhLineTrapCritGoesOn.setStatus(
        "current"
    )

pm10010ulhLineTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 80, 10, 35)
)
pm10010ulhLineTrapCritGoesOff.setObjects(
      *(("EKINOPS-Pm10010ulh-MIB", "pm10010ulhAlmLineFailPortn"),
        ("EKINOPS-Pm10010ulh-MIB", "pm10010ulhAlmLineHwFailPortn"),
        ("EKINOPS-Pm10010ulh-MIB", "pm10010ulhtrapLineNumber"),
        ("EKINOPS-Pm10010ulh-MIB", "pm10010ulhtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10010ulhLineTrapCritGoesOff.setStatus(
        "current"
    )

pm10010ulhClientTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 80, 10, 40)
)
pm10010ulhClientTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm10010ulh-MIB", "pm10010ulhAlmSfpDdmWarningPortn"),
        ("EKINOPS-Pm10010ulh-MIB", "pm10010ulhtrapPortNumber"),
        ("EKINOPS-Pm10010ulh-MIB", "pm10010ulhtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10010ulhClientTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pm10010ulhClientTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 80, 10, 41)
)
pm10010ulhClientTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm10010ulh-MIB", "pm10010ulhAlmSfpDdmWarningPortn"),
        ("EKINOPS-Pm10010ulh-MIB", "pm10010ulhtrapPortNumber"),
        ("EKINOPS-Pm10010ulh-MIB", "pm10010ulhtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10010ulhClientTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pm10010ulhClientTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 80, 10, 42)
)
pm10010ulhClientTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm10010ulh-MIB", "pm10010ulhAlmSfpDdmAlmPortn"),
        ("EKINOPS-Pm10010ulh-MIB", "pm10010ulhtrapPortNumber"),
        ("EKINOPS-Pm10010ulh-MIB", "pm10010ulhtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10010ulhClientTrapUrgentGoesOn.setStatus(
        "current"
    )

pm10010ulhClientTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 80, 10, 43)
)
pm10010ulhClientTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm10010ulh-MIB", "pm10010ulhAlmSfpDdmAlmPortn"),
        ("EKINOPS-Pm10010ulh-MIB", "pm10010ulhtrapPortNumber"),
        ("EKINOPS-Pm10010ulh-MIB", "pm10010ulhtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10010ulhClientTrapUrgentGoesOff.setStatus(
        "current"
    )

pm10010ulhClientTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 80, 10, 44)
)
pm10010ulhClientTrapCritGoesOn.setObjects(
      *(("EKINOPS-Pm10010ulh-MIB", "pm10010ulhAlmFailAccPortn"),
        ("EKINOPS-Pm10010ulh-MIB", "pm10010ulhAlmHwFailAccPortn"),
        ("EKINOPS-Pm10010ulh-MIB", "pm10010ulhtrapPortNumber"),
        ("EKINOPS-Pm10010ulh-MIB", "pm10010ulhtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10010ulhClientTrapCritGoesOn.setStatus(
        "current"
    )

pm10010ulhClientTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 80, 10, 45)
)
pm10010ulhClientTrapCritGoesOff.setObjects(
      *(("EKINOPS-Pm10010ulh-MIB", "pm10010ulhAlmFailAccPortn"),
        ("EKINOPS-Pm10010ulh-MIB", "pm10010ulhAlmHwFailAccPortn"),
        ("EKINOPS-Pm10010ulh-MIB", "pm10010ulhtrapPortNumber"),
        ("EKINOPS-Pm10010ulh-MIB", "pm10010ulhtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10010ulhClientTrapCritGoesOff.setStatus(
        "current"
    )

pm10010ulhPowerTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 80, 10, 50)
)
pm10010ulhPowerTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm10010ulh-MIB", "pm10010ulhAlmDefFuseB"),
        ("EKINOPS-Pm10010ulh-MIB", "pm10010ulhAlmDefFuseA"),
        ("EKINOPS-Pm10010ulh-MIB", "pm10010ulhtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10010ulhPowerTrapUrgentGoesOn.setStatus(
        "current"
    )

pm10010ulhPowerTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 80, 10, 51)
)
pm10010ulhPowerTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm10010ulh-MIB", "pm10010ulhAlmDefFuseB"),
        ("EKINOPS-Pm10010ulh-MIB", "pm10010ulhAlmDefFuseA"),
        ("EKINOPS-Pm10010ulh-MIB", "pm10010ulhtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10010ulhPowerTrapUrgentGoesOff.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EKINOPS-Pm10010ulh-MIB",
    **{"Pm10010ulhMultiRate": Pm10010ulhMultiRate,
       "Pm10010ulhOtxMode": Pm10010ulhOtxMode,
       "Pm10010ulhOtxGrid": Pm10010ulhOtxGrid,
       "Pm10010ulhAdjustValue": Pm10010ulhAdjustValue,
       "Pm10010ulhClientProtocol": Pm10010ulhClientProtocol,
       "Pm10010ulhProtocolMode": Pm10010ulhProtocolMode,
       "Pm10010ulhOtxChannel": Pm10010ulhOtxChannel,
       "Pm10010ulhOrxChannel": Pm10010ulhOrxChannel,
       "Pm10010ulhDccMode": Pm10010ulhDccMode,
       "Pm10010ulhModuleMode": Pm10010ulhModuleMode,
       "modulePm10010ulh": modulePm10010ulh,
       "pm10010ulhalarms": pm10010ulhalarms,
       "pm10010ulhAlmOther": pm10010ulhAlmOther,
       "pm10010ulhAlmOtherNurg": pm10010ulhAlmOtherNurg,
       "pm10010ulhAlmsynthAlm2": pm10010ulhAlmsynthAlm2,
       "pm10010ulhAlmConfTableSave": pm10010ulhAlmConfTableSave,
       "pm10010ulhAlmInvUpload": pm10010ulhAlmInvUpload,
       "pm10010ulhAlmConfTableLoad": pm10010ulhAlmConfTableLoad,
       "pm10010ulhAlmCorrelatOff": pm10010ulhAlmCorrelatOff,
       "pm10010ulhAlmMaintenanceOn": pm10010ulhAlmMaintenanceOn,
       "pm10010ulhAlmOtherUrg": pm10010ulhAlmOtherUrg,
       "pm10010ulhAlmmodFanFail": pm10010ulhAlmmodFanFail,
       "pm10010ulhAlmFanFail": pm10010ulhAlmFanFail,
       "pm10010ulhAlmFanHighSpeed": pm10010ulhAlmFanHighSpeed,
       "pm10010ulhAlmOtherCrit": pm10010ulhAlmOtherCrit,
       "pm10010ulhAlmsynthAlm0": pm10010ulhAlmsynthAlm0,
       "pm10010ulhAlmFailFan": pm10010ulhAlmFailFan,
       "pm10010ulhAlmModGlobFail": pm10010ulhAlmModGlobFail,
       "pm10010ulhAlmDefFuseA": pm10010ulhAlmDefFuseA,
       "pm10010ulhAlmDefFuseB": pm10010ulhAlmDefFuseB,
       "pm10010ulhAlmclientModuleState": pm10010ulhAlmclientModuleState,
       "pm10010ulhAlmCfpInitialize": pm10010ulhAlmCfpInitialize,
       "pm10010ulhAlmCfpLowPower": pm10010ulhAlmCfpLowPower,
       "pm10010ulhAlmCfpHighPowerUp": pm10010ulhAlmCfpHighPowerUp,
       "pm10010ulhAlmCfpTxOff": pm10010ulhAlmCfpTxOff,
       "pm10010ulhAlmCfpTxTurnOn": pm10010ulhAlmCfpTxTurnOn,
       "pm10010ulhAlmCfpReady": pm10010ulhAlmCfpReady,
       "pm10010ulhAlmCfpFault": pm10010ulhAlmCfpFault,
       "pm10010ulhAlmCfpTxTurnOff": pm10010ulhAlmCfpTxTurnOff,
       "pm10010ulhAlmCfpHighPowerDown": pm10010ulhAlmCfpHighPowerDown,
       "pm10010ulhAlmclientModuleGeneralStatus": pm10010ulhAlmclientModuleGeneralStatus,
       "pm10010ulhAlmCfpOutOfAlignment": pm10010ulhAlmCfpOutOfAlignment,
       "pm10010ulhAlmCfpRxNetworkLol": pm10010ulhAlmCfpRxNetworkLol,
       "pm10010ulhAlmCfpRxLos": pm10010ulhAlmCfpRxLos,
       "pm10010ulhAlmCfpTxHostLol": pm10010ulhAlmCfpTxHostLol,
       "pm10010ulhAlmCfpTxLosf": pm10010ulhAlmCfpTxLosf,
       "pm10010ulhAlmCfpTxCmuLol": pm10010ulhAlmCfpTxCmuLol,
       "pm10010ulhAlmCfpTxJitterPllLol": pm10010ulhAlmCfpTxJitterPllLol,
       "pm10010ulhAlmCfpLossOfRefclk": pm10010ulhAlmCfpLossOfRefclk,
       "pm10010ulhAlmCfpHwInterlock": pm10010ulhAlmCfpHwInterlock,
       "pm10010ulhAlmclientGlobalAlarmSummary": pm10010ulhAlmclientGlobalAlarmSummary,
       "pm10010ulhAlmCfpSoftGlobAlarmTest": pm10010ulhAlmCfpSoftGlobAlarmTest,
       "pm10010ulhAlmCfpNetworkLaneAlarmWarning2": pm10010ulhAlmCfpNetworkLaneAlarmWarning2,
       "pm10010ulhAlmCfpModuleState": pm10010ulhAlmCfpModuleState,
       "pm10010ulhAlmCfpModuleGeneralStatus": pm10010ulhAlmCfpModuleGeneralStatus,
       "pm10010ulhAlmCfpModuleFault": pm10010ulhAlmCfpModuleFault,
       "pm10010ulhAlmCfpModuleAlarmWarning1": pm10010ulhAlmCfpModuleAlarmWarning1,
       "pm10010ulhAlmCfpModuleAlarmWarning2": pm10010ulhAlmCfpModuleAlarmWarning2,
       "pm10010ulhAlmCfpNetworkLaneAlarmWarning1": pm10010ulhAlmCfpNetworkLaneAlarmWarning1,
       "pm10010ulhAlmCfpNetworkLaneFaultStatus": pm10010ulhAlmCfpNetworkLaneFaultStatus,
       "pm10010ulhAlmCfpHostLaneFaultStatus": pm10010ulhAlmCfpHostLaneFaultStatus,
       "pm10010ulhAlmCfpGlobAlarmAssertion": pm10010ulhAlmCfpGlobAlarmAssertion,
       "pm10010ulhAlmmsaModuleState": pm10010ulhAlmmsaModuleState,
       "pm10010ulhAlmMsaInitialize": pm10010ulhAlmMsaInitialize,
       "pm10010ulhAlmMsaLowPower": pm10010ulhAlmMsaLowPower,
       "pm10010ulhAlmMsaHighPowerUp": pm10010ulhAlmMsaHighPowerUp,
       "pm10010ulhAlmMsaTxOff": pm10010ulhAlmMsaTxOff,
       "pm10010ulhAlmMsaTxTurnOn": pm10010ulhAlmMsaTxTurnOn,
       "pm10010ulhAlmMsaReady": pm10010ulhAlmMsaReady,
       "pm10010ulhAlmMsaFault": pm10010ulhAlmMsaFault,
       "pm10010ulhAlmMsaTxTurnOff": pm10010ulhAlmMsaTxTurnOff,
       "pm10010ulhAlmMsaHighPowerDown": pm10010ulhAlmMsaHighPowerDown,
       "pm10010ulhAlmmsaModuleGeneralStatus": pm10010ulhAlmmsaModuleGeneralStatus,
       "pm10010ulhAlmMsaOutOfAlignment": pm10010ulhAlmMsaOutOfAlignment,
       "pm10010ulhAlmMsaRxNetworkLol": pm10010ulhAlmMsaRxNetworkLol,
       "pm10010ulhAlmMsaRxLos": pm10010ulhAlmMsaRxLos,
       "pm10010ulhAlmMsaTxHostLol": pm10010ulhAlmMsaTxHostLol,
       "pm10010ulhAlmMsaTxLosf": pm10010ulhAlmMsaTxLosf,
       "pm10010ulhAlmMsaTxCmuLol": pm10010ulhAlmMsaTxCmuLol,
       "pm10010ulhAlmMsaTxJitterPllLol": pm10010ulhAlmMsaTxJitterPllLol,
       "pm10010ulhAlmMsaLossOfRefclk": pm10010ulhAlmMsaLossOfRefclk,
       "pm10010ulhAlmMsaHwInterlock": pm10010ulhAlmMsaHwInterlock,
       "pm10010ulhAlmmsaGlobalAlarmSummary": pm10010ulhAlmmsaGlobalAlarmSummary,
       "pm10010ulhAlmMsaSoftGlobAlarmTest": pm10010ulhAlmMsaSoftGlobAlarmTest,
       "pm10010ulhAlmMsaNetworkHostAlarmStatus": pm10010ulhAlmMsaNetworkHostAlarmStatus,
       "pm10010ulhAlmMsaNetworkLaneAlarmWarning2": pm10010ulhAlmMsaNetworkLaneAlarmWarning2,
       "pm10010ulhAlmMsaModuleState": pm10010ulhAlmMsaModuleState,
       "pm10010ulhAlmMsaModuleGeneralStatus": pm10010ulhAlmMsaModuleGeneralStatus,
       "pm10010ulhAlmModuleFault": pm10010ulhAlmModuleFault,
       "pm10010ulhAlmMsaModuleAlarmWarning1": pm10010ulhAlmMsaModuleAlarmWarning1,
       "pm10010ulhAlmMsaModuleAlarmWarning2": pm10010ulhAlmMsaModuleAlarmWarning2,
       "pm10010ulhAlmMsaNetworkLaneAlarmWarning1": pm10010ulhAlmMsaNetworkLaneAlarmWarning1,
       "pm10010ulhAlmMsaNetworkLaneFaultStatus": pm10010ulhAlmMsaNetworkLaneFaultStatus,
       "pm10010ulhAlmMsaHostLaneFaultStatus": pm10010ulhAlmMsaHostLaneFaultStatus,
       "pm10010ulhAlmMsaGlobAlarmAssertion": pm10010ulhAlmMsaGlobAlarmAssertion,
       "pm10010ulhAlmmsaNetworkTxAlignment": pm10010ulhAlmmsaNetworkTxAlignment,
       "pm10010ulhAlmNetTxTimingFault": pm10010ulhAlmNetTxTimingFault,
       "pm10010ulhAlmNetTxReferenceClockFault": pm10010ulhAlmNetTxReferenceClockFault,
       "pm10010ulhAlmNetTxCmuLockFault": pm10010ulhAlmNetTxCmuLockFault,
       "pm10010ulhAlmNetTxOutOfAlignment": pm10010ulhAlmNetTxOutOfAlignment,
       "pm10010ulhAlmNetTxLossOfAlignment": pm10010ulhAlmNetTxLossOfAlignment,
       "pm10010ulhAlmmsaNetworkRxAlignment": pm10010ulhAlmmsaNetworkRxAlignment,
       "pm10010ulhAlmNetRxTimingFault": pm10010ulhAlmNetRxTimingFault,
       "pm10010ulhAlmNetRxOutOfAlignment": pm10010ulhAlmNetRxOutOfAlignment,
       "pm10010ulhAlmNetRxLossOfAlignment": pm10010ulhAlmNetRxLossOfAlignment,
       "pm10010ulhAlmNetRxModemLockFault": pm10010ulhAlmNetRxModemLockFault,
       "pm10010ulhAlmNetRxModemSyncDetectFault": pm10010ulhAlmNetRxModemSyncDetectFault,
       "pm10010ulhAlmmsaNetworkHostNetworkAlarmSummary": pm10010ulhAlmmsaNetworkHostNetworkAlarmSummary,
       "pm10010ulhAlmNetworkTxAlignment": pm10010ulhAlmNetworkTxAlignment,
       "pm10010ulhAlmNetworkRxAlignment": pm10010ulhAlmNetworkRxAlignment,
       "pm10010ulhAlmNetworkRxOtn": pm10010ulhAlmNetworkRxOtn,
       "pm10010ulhAlmHostRxAlignment": pm10010ulhAlmHostRxAlignment,
       "pm10010ulhAlmHostTxAlignment": pm10010ulhAlmHostTxAlignment,
       "pm10010ulhAlmHostTxOtnStatus": pm10010ulhAlmHostTxOtnStatus,
       "pm10010ulhAlmmsaHostTxAlignment": pm10010ulhAlmmsaHostTxAlignment,
       "pm10010ulhAlmHostTxDeskewLockFault": pm10010ulhAlmHostTxDeskewLockFault,
       "pm10010ulhAlmHostTxOutOfAlignment": pm10010ulhAlmHostTxOutOfAlignment,
       "pm10010ulhAlmHostTxLossOfAlignment": pm10010ulhAlmHostTxLossOfAlignment,
       "pm10010ulhAlmHostTxCdrLockFault": pm10010ulhAlmHostTxCdrLockFault,
       "pm10010ulhAlmmsaHostRxAlignment": pm10010ulhAlmmsaHostRxAlignment,
       "pm10010ulhAlmHostRxCmuLockFault": pm10010ulhAlmHostRxCmuLockFault,
       "pm10010ulhAlmHostRxOutOfAlignment": pm10010ulhAlmHostRxOutOfAlignment,
       "pm10010ulhAlmHostRxLossOfAlignment": pm10010ulhAlmHostRxLossOfAlignment,
       "pm10010ulhAlmClient": pm10010ulhAlmClient,
       "pm10010ulhAlmClientNurg": pm10010ulhAlmClientNurg,
       "pm10010ulhAlmclientNetworkLaneAlarmWarningTable": pm10010ulhAlmclientNetworkLaneAlarmWarningTable,
       "pm10010ulhAlmclientNetworkLaneAlarmWarningEntry": pm10010ulhAlmclientNetworkLaneAlarmWarningEntry,
       "pm10010ulhAlmclientNetworkLaneAlarmWarningIndex": pm10010ulhAlmclientNetworkLaneAlarmWarningIndex,
       "pm10010ulhAlmClientRxPowerLowAlarmPortn": pm10010ulhAlmClientRxPowerLowAlarmPortn,
       "pm10010ulhAlmClientRxPowerLowWarningPortn": pm10010ulhAlmClientRxPowerLowWarningPortn,
       "pm10010ulhAlmClientRxPowerHighWarningPortn": pm10010ulhAlmClientRxPowerHighWarningPortn,
       "pm10010ulhAlmClientRxPowerHighAlarmPortn": pm10010ulhAlmClientRxPowerHighAlarmPortn,
       "pm10010ulhAlmLaserTempLowAlarmPortn": pm10010ulhAlmLaserTempLowAlarmPortn,
       "pm10010ulhAlmClientLaserTempLowWarningPortn": pm10010ulhAlmClientLaserTempLowWarningPortn,
       "pm10010ulhAlmClientLaserTempHighWarningPortn": pm10010ulhAlmClientLaserTempHighWarningPortn,
       "pm10010ulhAlmClientLaserTempHighAlarmPortn": pm10010ulhAlmClientLaserTempHighAlarmPortn,
       "pm10010ulhAlmClientTxPowerLowAlarmPortn": pm10010ulhAlmClientTxPowerLowAlarmPortn,
       "pm10010ulhAlmClientTxPowerLowWarningPortn": pm10010ulhAlmClientTxPowerLowWarningPortn,
       "pm10010ulhAlmClientTxPowerHighWarningPortn": pm10010ulhAlmClientTxPowerHighWarningPortn,
       "pm10010ulhAlmClientTxPowerHighAlarmPortn": pm10010ulhAlmClientTxPowerHighAlarmPortn,
       "pm10010ulhAlmClientBiasLowAlarmPortn": pm10010ulhAlmClientBiasLowAlarmPortn,
       "pm10010ulhAlmClientBiasLowWarningPortn": pm10010ulhAlmClientBiasLowWarningPortn,
       "pm10010ulhAlmClientBiasHighWarningPortn": pm10010ulhAlmClientBiasHighWarningPortn,
       "pm10010ulhAlmClientBiasHighAlarmPortn": pm10010ulhAlmClientBiasHighAlarmPortn,
       "pm10010ulhAlmclientSfpWarnDdmTable": pm10010ulhAlmclientSfpWarnDdmTable,
       "pm10010ulhAlmclientSfpWarnDdmEntry": pm10010ulhAlmclientSfpWarnDdmEntry,
       "pm10010ulhAlmclientSfpWarnDdmIndex": pm10010ulhAlmclientSfpWarnDdmIndex,
       "pm10010ulhAlmTxPwLowWngPortn": pm10010ulhAlmTxPwLowWngPortn,
       "pm10010ulhAlmTxPwrHighWngPortn": pm10010ulhAlmTxPwrHighWngPortn,
       "pm10010ulhAlmTxBiasLowWngPortn": pm10010ulhAlmTxBiasLowWngPortn,
       "pm10010ulhAlmTxBiasHighWngPortn": pm10010ulhAlmTxBiasHighWngPortn,
       "pm10010ulhAlmVccLowWngPortn": pm10010ulhAlmVccLowWngPortn,
       "pm10010ulhAlmVccHighWngPortn": pm10010ulhAlmVccHighWngPortn,
       "pm10010ulhAlmTempLowWngPortn": pm10010ulhAlmTempLowWngPortn,
       "pm10010ulhAlmTempHighWngPortn": pm10010ulhAlmTempHighWngPortn,
       "pm10010ulhAlmRxPwrLowWngPortn": pm10010ulhAlmRxPwrLowWngPortn,
       "pm10010ulhAlmRxPwrHighWngPortn": pm10010ulhAlmRxPwrHighWngPortn,
       "pm10010ulhAlmClientUrg": pm10010ulhAlmClientUrg,
       "pm10010ulhAlmclientNetworkLaneFaultTable": pm10010ulhAlmclientNetworkLaneFaultTable,
       "pm10010ulhAlmclientNetworkLaneFaultEntry": pm10010ulhAlmclientNetworkLaneFaultEntry,
       "pm10010ulhAlmclientNetworkLaneFaultIndex": pm10010ulhAlmclientNetworkLaneFaultIndex,
       "pm10010ulhAlmClientLaneRxFifoErrorPortn": pm10010ulhAlmClientLaneRxFifoErrorPortn,
       "pm10010ulhAlmClientLaneRxLolPortn": pm10010ulhAlmClientLaneRxLolPortn,
       "pm10010ulhAlmClientLaneRxLosPortn": pm10010ulhAlmClientLaneRxLosPortn,
       "pm10010ulhAlmClientLaneTxLolPortn": pm10010ulhAlmClientLaneTxLolPortn,
       "pm10010ulhAlmClientLaneTxLosfPortn": pm10010ulhAlmClientLaneTxLosfPortn,
       "pm10010ulhAlmClientLaneApdPowerSupplyPortn": pm10010ulhAlmClientLaneApdPowerSupplyPortn,
       "pm10010ulhAlmClientLaneWavelengthUnlockedPortn": pm10010ulhAlmClientLaneWavelengthUnlockedPortn,
       "pm10010ulhAlmClientLaneTecFaultPortn": pm10010ulhAlmClientLaneTecFaultPortn,
       "pm10010ulhAlmclientHostLaneFaultTable": pm10010ulhAlmclientHostLaneFaultTable,
       "pm10010ulhAlmclientHostLaneFaultEntry": pm10010ulhAlmclientHostLaneFaultEntry,
       "pm10010ulhAlmclientHostLaneFaultIndex": pm10010ulhAlmclientHostLaneFaultIndex,
       "pm10010ulhAlmClientLossOfSyncPortn": pm10010ulhAlmClientLossOfSyncPortn,
       "pm10010ulhAlmClientInputLossOfSigPortn": pm10010ulhAlmClientInputLossOfSigPortn,
       "pm10010ulhAlmClientLanesMarkerUnlockPortn": pm10010ulhAlmClientLanesMarkerUnlockPortn,
       "pm10010ulhAlmClientLanes6466UnlockPortn": pm10010ulhAlmClientLanes6466UnlockPortn,
       "pm10010ulhAlmClientLanesNotAlignedPortn": pm10010ulhAlmClientLanesNotAlignedPortn,
       "pm10010ulhAlmClientCsfDetectedPortn": pm10010ulhAlmClientCsfDetectedPortn,
       "pm10010ulhAlmClientTxHostLolPortn": pm10010ulhAlmClientTxHostLolPortn,
       "pm10010ulhAlmClientLaneTxFifoErrorPortn": pm10010ulhAlmClientLaneTxFifoErrorPortn,
       "pm10010ulhAlmclientSfpAlmDdmTable": pm10010ulhAlmclientSfpAlmDdmTable,
       "pm10010ulhAlmclientSfpAlmDdmEntry": pm10010ulhAlmclientSfpAlmDdmEntry,
       "pm10010ulhAlmclientSfpAlmDdmIndex": pm10010ulhAlmclientSfpAlmDdmIndex,
       "pm10010ulhAlmTxPwrLowAlaPortn": pm10010ulhAlmTxPwrLowAlaPortn,
       "pm10010ulhAlmTxPwrHighAlaPortn": pm10010ulhAlmTxPwrHighAlaPortn,
       "pm10010ulhAlmTxBiasLowAlaPortn": pm10010ulhAlmTxBiasLowAlaPortn,
       "pm10010ulhAlmTxBiasHighAlaPortn": pm10010ulhAlmTxBiasHighAlaPortn,
       "pm10010ulhAlmVccLowAlaPortn": pm10010ulhAlmVccLowAlaPortn,
       "pm10010ulhAlmVccHighAlaPortn": pm10010ulhAlmVccHighAlaPortn,
       "pm10010ulhAlmTempLowAlaPortn": pm10010ulhAlmTempLowAlaPortn,
       "pm10010ulhAlmTempHighAlaPortn": pm10010ulhAlmTempHighAlaPortn,
       "pm10010ulhAlmRxPwrLowAlaPortn": pm10010ulhAlmRxPwrLowAlaPortn,
       "pm10010ulhAlmRxPwrHighAlaPortn": pm10010ulhAlmRxPwrHighAlaPortn,
       "pm10010ulhAlmClientCrit": pm10010ulhAlmClientCrit,
       "pm10010ulhAlmsynthAlmPortTable": pm10010ulhAlmsynthAlmPortTable,
       "pm10010ulhAlmsynthAlmPortEntry": pm10010ulhAlmsynthAlmPortEntry,
       "pm10010ulhAlmsynthAlmPortIndex": pm10010ulhAlmsynthAlmPortIndex,
       "pm10010ulhAlmSfpAbsentPortn": pm10010ulhAlmSfpAbsentPortn,
       "pm10010ulhAlmDdmAbsentPortn": pm10010ulhAlmDdmAbsentPortn,
       "pm10010ulhAlmHwFailAccPortn": pm10010ulhAlmHwFailAccPortn,
       "pm10010ulhAlmDwLsdPortn": pm10010ulhAlmDwLsdPortn,
       "pm10010ulhAlmClientLocalOosPortn": pm10010ulhAlmClientLocalOosPortn,
       "pm10010ulhAlmClientRemoteOosPortn": pm10010ulhAlmClientRemoteOosPortn,
       "pm10010ulhAlmDwCaisPortn": pm10010ulhAlmDwCaisPortn,
       "pm10010ulhAlmSfpDdmWarningPortn": pm10010ulhAlmSfpDdmWarningPortn,
       "pm10010ulhAlmSfpDdmAlmPortn": pm10010ulhAlmSfpDdmAlmPortn,
       "pm10010ulhAlmFailAccPortn": pm10010ulhAlmFailAccPortn,
       "pm10010ulhAlmUpCsfPortn": pm10010ulhAlmUpCsfPortn,
       "pm10010ulhAlmLine": pm10010ulhAlmLine,
       "pm10010ulhAlmLineNurg": pm10010ulhAlmLineNurg,
       "pm10010ulhAlmlineNetworkLaneAlarmWarning1Table": pm10010ulhAlmlineNetworkLaneAlarmWarning1Table,
       "pm10010ulhAlmlineNetworkLaneAlarmWarning1Entry": pm10010ulhAlmlineNetworkLaneAlarmWarning1Entry,
       "pm10010ulhAlmlineNetworkLaneAlarmWarning1Index": pm10010ulhAlmlineNetworkLaneAlarmWarning1Index,
       "pm10010ulhAlmLineRxPowerLowAlarmPortn": pm10010ulhAlmLineRxPowerLowAlarmPortn,
       "pm10010ulhAlmLineRxPowerLowWarningPortn": pm10010ulhAlmLineRxPowerLowWarningPortn,
       "pm10010ulhAlmLineRxPowerHighWarningPortn": pm10010ulhAlmLineRxPowerHighWarningPortn,
       "pm10010ulhAlmLineRxPowerHighAlarmPortn": pm10010ulhAlmLineRxPowerHighAlarmPortn,
       "pm10010ulhAlmLineLaserTempLowAlarmPortn": pm10010ulhAlmLineLaserTempLowAlarmPortn,
       "pm10010ulhAlmLineLaserTempLowWarningPortn": pm10010ulhAlmLineLaserTempLowWarningPortn,
       "pm10010ulhAlmLineLaserTempHighWarningPortn": pm10010ulhAlmLineLaserTempHighWarningPortn,
       "pm10010ulhAlmLineLaserTempHighAlarmPortn": pm10010ulhAlmLineLaserTempHighAlarmPortn,
       "pm10010ulhAlmLineTxPowerLowAlarmPortn": pm10010ulhAlmLineTxPowerLowAlarmPortn,
       "pm10010ulhAlmLineTxPowerLowWarningPortn": pm10010ulhAlmLineTxPowerLowWarningPortn,
       "pm10010ulhAlmLineTxPowerHighWarningPortn": pm10010ulhAlmLineTxPowerHighWarningPortn,
       "pm10010ulhAlmLineTxPowerHighAlarmPortn": pm10010ulhAlmLineTxPowerHighAlarmPortn,
       "pm10010ulhAlmLineBiasLowAlarmPortn": pm10010ulhAlmLineBiasLowAlarmPortn,
       "pm10010ulhAlmLineBiasLowWarningPortn": pm10010ulhAlmLineBiasLowWarningPortn,
       "pm10010ulhAlmLineBiasHighWarningPortn": pm10010ulhAlmLineBiasHighWarningPortn,
       "pm10010ulhAlmLineBiasHighAlarmPortn": pm10010ulhAlmLineBiasHighAlarmPortn,
       "pm10010ulhAlmlineNetworkLaneAlarmWarning2Table": pm10010ulhAlmlineNetworkLaneAlarmWarning2Table,
       "pm10010ulhAlmlineNetworkLaneAlarmWarning2Entry": pm10010ulhAlmlineNetworkLaneAlarmWarning2Entry,
       "pm10010ulhAlmlineNetworkLaneAlarmWarning2Index": pm10010ulhAlmlineNetworkLaneAlarmWarning2Index,
       "pm10010ulhAlmTxModulatorBiasLowAlarmPortn": pm10010ulhAlmTxModulatorBiasLowAlarmPortn,
       "pm10010ulhAlmTxModulatorBiasLowWarningPortn": pm10010ulhAlmTxModulatorBiasLowWarningPortn,
       "pm10010ulhAlmTxModulatorBiasHighWarningPortn": pm10010ulhAlmTxModulatorBiasHighWarningPortn,
       "pm10010ulhAlmTxModulatorBiasHighAlarmPortn": pm10010ulhAlmTxModulatorBiasHighAlarmPortn,
       "pm10010ulhAlmRxLaserTempLowAlarmPortn": pm10010ulhAlmRxLaserTempLowAlarmPortn,
       "pm10010ulhAlmRxLaserTempLowWarningPortn": pm10010ulhAlmRxLaserTempLowWarningPortn,
       "pm10010ulhAlmRxLaserTempHighWarningPortn": pm10010ulhAlmRxLaserTempHighWarningPortn,
       "pm10010ulhAlmRxLaserTempHighAlarmPortn": pm10010ulhAlmRxLaserTempHighAlarmPortn,
       "pm10010ulhAlmRxLaserOutputLowAlarmPortn": pm10010ulhAlmRxLaserOutputLowAlarmPortn,
       "pm10010ulhAlmRxLaserOutputLowWarningPortn": pm10010ulhAlmRxLaserOutputLowWarningPortn,
       "pm10010ulhAlmRxLaserOutputHighWarningPortn": pm10010ulhAlmRxLaserOutputHighWarningPortn,
       "pm10010ulhAlmRxLaserOutputHighAlarmPortn": pm10010ulhAlmRxLaserOutputHighAlarmPortn,
       "pm10010ulhAlmRxLaserBiasLowAlarmPortn": pm10010ulhAlmRxLaserBiasLowAlarmPortn,
       "pm10010ulhAlmRxLaserBiasLowWarningPortn": pm10010ulhAlmRxLaserBiasLowWarningPortn,
       "pm10010ulhAlmRxLaserBiasHighWarningPortn": pm10010ulhAlmRxLaserBiasHighWarningPortn,
       "pm10010ulhAlmRxLaserBiasHighAlarmPortn": pm10010ulhAlmRxLaserBiasHighAlarmPortn,
       "pm10010ulhAlmLineUrg": pm10010ulhAlmLineUrg,
       "pm10010ulhAlmlineNetworkLaneFaultTable": pm10010ulhAlmlineNetworkLaneFaultTable,
       "pm10010ulhAlmlineNetworkLaneFaultEntry": pm10010ulhAlmlineNetworkLaneFaultEntry,
       "pm10010ulhAlmlineNetworkLaneFaultIndex": pm10010ulhAlmlineNetworkLaneFaultIndex,
       "pm10010ulhAlmLineLaneRxTecFaultPortn": pm10010ulhAlmLineLaneRxTecFaultPortn,
       "pm10010ulhAlmLineLaneRxFifoErrorPortn": pm10010ulhAlmLineLaneRxFifoErrorPortn,
       "pm10010ulhAlmLineLaneRxLolPortn": pm10010ulhAlmLineLaneRxLolPortn,
       "pm10010ulhAlmLineLaneRxLosPortn": pm10010ulhAlmLineLaneRxLosPortn,
       "pm10010ulhAlmLineLaneTxLolPortn": pm10010ulhAlmLineLaneTxLolPortn,
       "pm10010ulhAlmLineLaneTxLosfPortn": pm10010ulhAlmLineLaneTxLosfPortn,
       "pm10010ulhAlmLineLaneApdPowerSupplyPortn": pm10010ulhAlmLineLaneApdPowerSupplyPortn,
       "pm10010ulhAlmLineLaneWavelengthUnlockedPortn": pm10010ulhAlmLineLaneWavelengthUnlockedPortn,
       "pm10010ulhAlmLineLaneTecFaultPortn": pm10010ulhAlmLineLaneTecFaultPortn,
       "pm10010ulhAlmlineHostLaneFaultTable": pm10010ulhAlmlineHostLaneFaultTable,
       "pm10010ulhAlmlineHostLaneFaultEntry": pm10010ulhAlmlineHostLaneFaultEntry,
       "pm10010ulhAlmlineHostLaneFaultIndex": pm10010ulhAlmlineHostLaneFaultIndex,
       "pm10010ulhAlmLineInputLossOfSignalPortn": pm10010ulhAlmLineInputLossOfSignalPortn,
       "pm10010ulhAlmLineLossOfFramePortn": pm10010ulhAlmLineLossOfFramePortn,
       "pm10010ulhAlmLineSmBdiInsertedPortn": pm10010ulhAlmLineSmBdiInsertedPortn,
       "pm10010ulhAlmLineSmBdiDetectedPortn": pm10010ulhAlmLineSmBdiDetectedPortn,
       "pm10010ulhAlmLineSmIaeInsertedPortn": pm10010ulhAlmLineSmIaeInsertedPortn,
       "pm10010ulhAlmLineSmIaeDetectedPortn": pm10010ulhAlmLineSmIaeDetectedPortn,
       "pm10010ulhAlmLineTxHostLolPortn": pm10010ulhAlmLineTxHostLolPortn,
       "pm10010ulhAlmLineLaneTxFifoErrorPortn": pm10010ulhAlmLineLaneTxFifoErrorPortn,
       "pm10010ulhAlmlineNetworkLaneRxOtnTable": pm10010ulhAlmlineNetworkLaneRxOtnTable,
       "pm10010ulhAlmlineNetworkLaneRxOtnEntry": pm10010ulhAlmlineNetworkLaneRxOtnEntry,
       "pm10010ulhAlmlineNetworkLaneRxOtnIndex": pm10010ulhAlmlineNetworkLaneRxOtnIndex,
       "pm10010ulhAlmLineRxOtnOduAisPortn": pm10010ulhAlmLineRxOtnOduAisPortn,
       "pm10010ulhAlmLineRxOtnOtuAisPortn": pm10010ulhAlmLineRxOtnOtuAisPortn,
       "pm10010ulhAlmLineRxSmBdiPortn": pm10010ulhAlmLineRxSmBdiPortn,
       "pm10010ulhAlmLineRxOtnIaePortn": pm10010ulhAlmLineRxOtnIaePortn,
       "pm10010ulhAlmLineRxOtnOomPortn": pm10010ulhAlmLineRxOtnOomPortn,
       "pm10010ulhAlmLineRxOtnLomPortn": pm10010ulhAlmLineRxOtnLomPortn,
       "pm10010ulhAlmLineRxOtnOofPortn": pm10010ulhAlmLineRxOtnOofPortn,
       "pm10010ulhAlmLineRxOtnLofPortn": pm10010ulhAlmLineRxOtnLofPortn,
       "pm10010ulhAlmlineHostLaneTxOtnTable": pm10010ulhAlmlineHostLaneTxOtnTable,
       "pm10010ulhAlmlineHostLaneTxOtnEntry": pm10010ulhAlmlineHostLaneTxOtnEntry,
       "pm10010ulhAlmlineHostLaneTxOtnIndex": pm10010ulhAlmlineHostLaneTxOtnIndex,
       "pm10010ulhAlmLineTxOtnOduAisPortn": pm10010ulhAlmLineTxOtnOduAisPortn,
       "pm10010ulhAlmLineTxOtnOtuAisPortn": pm10010ulhAlmLineTxOtnOtuAisPortn,
       "pm10010ulhAlmLineTxSmBdiPortn": pm10010ulhAlmLineTxSmBdiPortn,
       "pm10010ulhAlmLineTxOtnIaePortn": pm10010ulhAlmLineTxOtnIaePortn,
       "pm10010ulhAlmLineTxOtnOomPortn": pm10010ulhAlmLineTxOtnOomPortn,
       "pm10010ulhAlmLineTxOtnLomPortn": pm10010ulhAlmLineTxOtnLomPortn,
       "pm10010ulhAlmLineTxOtnOofPortn": pm10010ulhAlmLineTxOtnOofPortn,
       "pm10010ulhAlmLineTxOtnLofPortn": pm10010ulhAlmLineTxOtnLofPortn,
       "pm10010ulhAlmLineCrit": pm10010ulhAlmLineCrit,
       "pm10010ulhAlmsynthAlmLineTable": pm10010ulhAlmsynthAlmLineTable,
       "pm10010ulhAlmsynthAlmLineEntry": pm10010ulhAlmsynthAlmLineEntry,
       "pm10010ulhAlmsynthAlmLineIndex": pm10010ulhAlmsynthAlmLineIndex,
       "pm10010ulhAlmXfpAbsentPortn": pm10010ulhAlmXfpAbsentPortn,
       "pm10010ulhAlmXfpInitNotComplPortn": pm10010ulhAlmXfpInitNotComplPortn,
       "pm10010ulhAlmLineHwFailPortn": pm10010ulhAlmLineHwFailPortn,
       "pm10010ulhAlmXfpTxOffPortn": pm10010ulhAlmXfpTxOffPortn,
       "pm10010ulhAlmLineLocalOosPortn": pm10010ulhAlmLineLocalOosPortn,
       "pm10010ulhAlmUpRdiInsPortn": pm10010ulhAlmUpRdiInsPortn,
       "pm10010ulhAlmLineDdmWarningPortn": pm10010ulhAlmLineDdmWarningPortn,
       "pm10010ulhAlmLineDdmAlmPortn": pm10010ulhAlmLineDdmAlmPortn,
       "pm10010ulhAlmLineFailPortn": pm10010ulhAlmLineFailPortn,
       "pm10010ulhAlmLineActivePortn": pm10010ulhAlmLineActivePortn,
       "pm10010ulhmeasures": pm10010ulhmeasures,
       "pm10010ulhMesrOther": pm10010ulhMesrOther,
       "pm10010ulhMesrsynth0": pm10010ulhMesrsynth0,
       "pm10010ulhMesrsynth1": pm10010ulhMesrsynth1,
       "pm10010ulhMesrpmIntervalNumber": pm10010ulhMesrpmIntervalNumber,
       "pm10010ulhMesrlineNetTxLaserOutputPwrAverage": pm10010ulhMesrlineNetTxLaserOutputPwrAverage,
       "pm10010ulhMesrlineNetTxLaserTempAverage": pm10010ulhMesrlineNetTxLaserTempAverage,
       "pm10010ulhMesrlineNetTxBiasCurrentAverage": pm10010ulhMesrlineNetTxBiasCurrentAverage,
       "pm10010ulhMesrlineNetRxInputPwrAverage": pm10010ulhMesrlineNetRxInputPwrAverage,
       "pm10010ulhMesrlineResidualChromaticDispAverage": pm10010ulhMesrlineResidualChromaticDispAverage,
       "pm10010ulhMesrlineDiffGroupDelayAverage": pm10010ulhMesrlineDiffGroupDelayAverage,
       "pm10010ulhMesrlineQFactorAverage": pm10010ulhMesrlineQFactorAverage,
       "pm10010ulhMesrlineCarrierFreqOffsetAverage": pm10010ulhMesrlineCarrierFreqOffsetAverage,
       "pm10010ulhMesrlineOsnrAverage": pm10010ulhMesrlineOsnrAverage,
       "pm10010ulhMesrclientNetTxTempMin": pm10010ulhMesrclientNetTxTempMin,
       "pm10010ulhMesrclientNetTxBiasMin": pm10010ulhMesrclientNetTxBiasMin,
       "pm10010ulhMesrclientNetTxPwrMin": pm10010ulhMesrclientNetTxPwrMin,
       "pm10010ulhMesrclientNetRxPwrMin": pm10010ulhMesrclientNetRxPwrMin,
       "pm10010ulhMesrlineNetTxLaserOutputPwrMin": pm10010ulhMesrlineNetTxLaserOutputPwrMin,
       "pm10010ulhMesrlineNetTxLaserTempMin": pm10010ulhMesrlineNetTxLaserTempMin,
       "pm10010ulhMesrlineNetTxBiasCurrentMin": pm10010ulhMesrlineNetTxBiasCurrentMin,
       "pm10010ulhMesrlineNetRxInputPwrMin": pm10010ulhMesrlineNetRxInputPwrMin,
       "pm10010ulhMesrlineResidualChromaticDispMin": pm10010ulhMesrlineResidualChromaticDispMin,
       "pm10010ulhMesrlineDiffGroupDelayMin": pm10010ulhMesrlineDiffGroupDelayMin,
       "pm10010ulhMesrlineQFactorMin": pm10010ulhMesrlineQFactorMin,
       "pm10010ulhMesrlineCarrierFreqOffsetMin": pm10010ulhMesrlineCarrierFreqOffsetMin,
       "pm10010ulhMesrlineOsnrMin": pm10010ulhMesrlineOsnrMin,
       "pm10010ulhMesrclientNetTxTempMax": pm10010ulhMesrclientNetTxTempMax,
       "pm10010ulhMesrclientNetTxBiasMax": pm10010ulhMesrclientNetTxBiasMax,
       "pm10010ulhMesrclientNetTxPwrMax": pm10010ulhMesrclientNetTxPwrMax,
       "pm10010ulhMesrclientNetRxPwrMax": pm10010ulhMesrclientNetRxPwrMax,
       "pm10010ulhMesrlineNetTxLaserOutputPwrMax": pm10010ulhMesrlineNetTxLaserOutputPwrMax,
       "pm10010ulhMesrlineNetTxLaserTempMax": pm10010ulhMesrlineNetTxLaserTempMax,
       "pm10010ulhMesrlineNetTxBiasCurrentMax": pm10010ulhMesrlineNetTxBiasCurrentMax,
       "pm10010ulhMesrlineNetRxInputPwrMax": pm10010ulhMesrlineNetRxInputPwrMax,
       "pm10010ulhMesrlineResidualChromaticDispMax": pm10010ulhMesrlineResidualChromaticDispMax,
       "pm10010ulhMesrlineDiffGroupDelayMax": pm10010ulhMesrlineDiffGroupDelayMax,
       "pm10010ulhMesrlineQFactorMax": pm10010ulhMesrlineQFactorMax,
       "pm10010ulhMesrlineCarrierFreqOffsetMax": pm10010ulhMesrlineCarrierFreqOffsetMax,
       "pm10010ulhMesrlineOsnrMax": pm10010ulhMesrlineOsnrMax,
       "pm10010ulhMesrClient": pm10010ulhMesrClient,
       "pm10010ulhMesrclientCfpTemp": pm10010ulhMesrclientCfpTemp,
       "pm10010ulhMesrclientCfp3v3Voltage": pm10010ulhMesrclientCfp3v3Voltage,
       "pm10010ulhMesrclientSoaBiasCurrent": pm10010ulhMesrclientSoaBiasCurrent,
       "pm10010ulhMesrclientNetTxTempTable": pm10010ulhMesrclientNetTxTempTable,
       "pm10010ulhMesrclientNetTxTempEntry": pm10010ulhMesrclientNetTxTempEntry,
       "pm10010ulhMesrclientNetTxTempIndex": pm10010ulhMesrclientNetTxTempIndex,
       "pm10010ulhMesrclientNetTxTempPortn": pm10010ulhMesrclientNetTxTempPortn,
       "pm10010ulhMesrclientNetTxBiasTable": pm10010ulhMesrclientNetTxBiasTable,
       "pm10010ulhMesrclientNetTxBiasEntry": pm10010ulhMesrclientNetTxBiasEntry,
       "pm10010ulhMesrclientNetTxBiasIndex": pm10010ulhMesrclientNetTxBiasIndex,
       "pm10010ulhMesrclientNetTxBiasPortn": pm10010ulhMesrclientNetTxBiasPortn,
       "pm10010ulhMesrclientNetTxPwrTable": pm10010ulhMesrclientNetTxPwrTable,
       "pm10010ulhMesrclientNetTxPwrEntry": pm10010ulhMesrclientNetTxPwrEntry,
       "pm10010ulhMesrclientNetTxPwrIndex": pm10010ulhMesrclientNetTxPwrIndex,
       "pm10010ulhMesrclientNetTxPwrPortn": pm10010ulhMesrclientNetTxPwrPortn,
       "pm10010ulhMesrclientNetRxPwrTable": pm10010ulhMesrclientNetRxPwrTable,
       "pm10010ulhMesrclientNetRxPwrEntry": pm10010ulhMesrclientNetRxPwrEntry,
       "pm10010ulhMesrclientNetRxPwrIndex": pm10010ulhMesrclientNetRxPwrIndex,
       "pm10010ulhMesrclientNetRxPwrPortn": pm10010ulhMesrclientNetRxPwrPortn,
       "pm10010ulhMesrLine": pm10010ulhMesrLine,
       "pm10010ulhMesrlineMsaTemp": pm10010ulhMesrlineMsaTemp,
       "pm10010ulhMesrlineMsa3v3Voltage": pm10010ulhMesrlineMsa3v3Voltage,
       "pm10010ulhMesrlineSoaBiasCurrent": pm10010ulhMesrlineSoaBiasCurrent,
       "pm10010ulhMesrlineNetTxLaserOutputPwrTable": pm10010ulhMesrlineNetTxLaserOutputPwrTable,
       "pm10010ulhMesrlineNetTxLaserOutputPwrEntry": pm10010ulhMesrlineNetTxLaserOutputPwrEntry,
       "pm10010ulhMesrlineNetTxLaserOutputPwrIndex": pm10010ulhMesrlineNetTxLaserOutputPwrIndex,
       "pm10010ulhMesrlineNetTxLaserOutputPwrPortn": pm10010ulhMesrlineNetTxLaserOutputPwrPortn,
       "pm10010ulhMesrlineNetTxLaserTempTable": pm10010ulhMesrlineNetTxLaserTempTable,
       "pm10010ulhMesrlineNetTxLaserTempEntry": pm10010ulhMesrlineNetTxLaserTempEntry,
       "pm10010ulhMesrlineNetTxLaserTempIndex": pm10010ulhMesrlineNetTxLaserTempIndex,
       "pm10010ulhMesrlineNetTxLaserTempPortn": pm10010ulhMesrlineNetTxLaserTempPortn,
       "pm10010ulhMesrlineNetTxBiasCurrentTable": pm10010ulhMesrlineNetTxBiasCurrentTable,
       "pm10010ulhMesrlineNetTxBiasCurrentEntry": pm10010ulhMesrlineNetTxBiasCurrentEntry,
       "pm10010ulhMesrlineNetTxBiasCurrentIndex": pm10010ulhMesrlineNetTxBiasCurrentIndex,
       "pm10010ulhMesrlineNetTxBiasCurrentPortn": pm10010ulhMesrlineNetTxBiasCurrentPortn,
       "pm10010ulhMesrlineNetRxInputPwrTable": pm10010ulhMesrlineNetRxInputPwrTable,
       "pm10010ulhMesrlineNetRxInputPwrEntry": pm10010ulhMesrlineNetRxInputPwrEntry,
       "pm10010ulhMesrlineNetRxInputPwrIndex": pm10010ulhMesrlineNetRxInputPwrIndex,
       "pm10010ulhMesrlineNetRxInputPwrPortn": pm10010ulhMesrlineNetRxInputPwrPortn,
       "pm10010ulhMesrlineResidualChromaticDispTable": pm10010ulhMesrlineResidualChromaticDispTable,
       "pm10010ulhMesrlineResidualChromaticDispEntry": pm10010ulhMesrlineResidualChromaticDispEntry,
       "pm10010ulhMesrlineResidualChromaticDispIndex": pm10010ulhMesrlineResidualChromaticDispIndex,
       "pm10010ulhMesrlineResidualChromaticDispPortn": pm10010ulhMesrlineResidualChromaticDispPortn,
       "pm10010ulhMesrlineDiffGroupDelayTable": pm10010ulhMesrlineDiffGroupDelayTable,
       "pm10010ulhMesrlineDiffGroupDelayEntry": pm10010ulhMesrlineDiffGroupDelayEntry,
       "pm10010ulhMesrlineDiffGroupDelayIndex": pm10010ulhMesrlineDiffGroupDelayIndex,
       "pm10010ulhMesrlineDiffGroupDelayPortn": pm10010ulhMesrlineDiffGroupDelayPortn,
       "pm10010ulhMesrlineQFactorTable": pm10010ulhMesrlineQFactorTable,
       "pm10010ulhMesrlineQFactorEntry": pm10010ulhMesrlineQFactorEntry,
       "pm10010ulhMesrlineQFactorIndex": pm10010ulhMesrlineQFactorIndex,
       "pm10010ulhMesrlineQFactorPortn": pm10010ulhMesrlineQFactorPortn,
       "pm10010ulhMesrlineCarrierFreqOffsetTable": pm10010ulhMesrlineCarrierFreqOffsetTable,
       "pm10010ulhMesrlineCarrierFreqOffsetEntry": pm10010ulhMesrlineCarrierFreqOffsetEntry,
       "pm10010ulhMesrlineCarrierFreqOffsetIndex": pm10010ulhMesrlineCarrierFreqOffsetIndex,
       "pm10010ulhMesrlineCarrierFreqOffsetPortn": pm10010ulhMesrlineCarrierFreqOffsetPortn,
       "pm10010ulhMesrlineOsnrTable": pm10010ulhMesrlineOsnrTable,
       "pm10010ulhMesrlineOsnrEntry": pm10010ulhMesrlineOsnrEntry,
       "pm10010ulhMesrlineOsnrIndex": pm10010ulhMesrlineOsnrIndex,
       "pm10010ulhMesrlineOsnrPortn": pm10010ulhMesrlineOsnrPortn,
       "pm10010ulhcounters": pm10010ulhcounters,
       "pm10010ulhCntOther": pm10010ulhCntOther,
       "pm10010ulhCntClient": pm10010ulhCntClient,
       "pm10010ulhCntclientInputErrorCounterTable": pm10010ulhCntclientInputErrorCounterTable,
       "pm10010ulhCntclientInputErrorCounterEntry": pm10010ulhCntclientInputErrorCounterEntry,
       "pm10010ulhCntclientInputErrorCounterIndex": pm10010ulhCntclientInputErrorCounterIndex,
       "pm10010ulhCntclientInputErrorCounterValuePortn": pm10010ulhCntclientInputErrorCounterValuePortn,
       "pm10010ulhCntclientInputErrorCounterErrorPortn": pm10010ulhCntclientInputErrorCounterErrorPortn,
       "pm10010ulhCntclientInputErrorCounterOverloadPortn": pm10010ulhCntclientInputErrorCounterOverloadPortn,
       "pm10010ulhCntclientCbipCounterTable": pm10010ulhCntclientCbipCounterTable,
       "pm10010ulhCntclientCbipCounterEntry": pm10010ulhCntclientCbipCounterEntry,
       "pm10010ulhCntclientCbipCounterIndex": pm10010ulhCntclientCbipCounterIndex,
       "pm10010ulhCntclientCbipCounterValuePortn": pm10010ulhCntclientCbipCounterValuePortn,
       "pm10010ulhCntclientCbipCounterErrorPortn": pm10010ulhCntclientCbipCounterErrorPortn,
       "pm10010ulhCntclientCbipCounterOverloadPortn": pm10010ulhCntclientCbipCounterOverloadPortn,
       "pm10010ulhCntLine": pm10010ulhCntLine,
       "pm10010ulhCntlocalLineSmBip8ErrorCounterTable": pm10010ulhCntlocalLineSmBip8ErrorCounterTable,
       "pm10010ulhCntlocalLineSmBip8ErrorCounterEntry": pm10010ulhCntlocalLineSmBip8ErrorCounterEntry,
       "pm10010ulhCntlocalLineSmBip8ErrorCounterIndex": pm10010ulhCntlocalLineSmBip8ErrorCounterIndex,
       "pm10010ulhCntlocalLineSmBip8ErrorCounterValuePortn": pm10010ulhCntlocalLineSmBip8ErrorCounterValuePortn,
       "pm10010ulhCntlocalLineSmBip8ErrorCounterErrorPortn": pm10010ulhCntlocalLineSmBip8ErrorCounterErrorPortn,
       "pm10010ulhCntlocalLineSmBip8ErrorCounterOverloadPortn": pm10010ulhCntlocalLineSmBip8ErrorCounterOverloadPortn,
       "pm10010ulhCntlocalLineFecCorrectedErrorsCounterTable": pm10010ulhCntlocalLineFecCorrectedErrorsCounterTable,
       "pm10010ulhCntlocalLineFecCorrectedErrorsCounterEntry": pm10010ulhCntlocalLineFecCorrectedErrorsCounterEntry,
       "pm10010ulhCntlocalLineFecCorrectedErrorsCounterIndex": pm10010ulhCntlocalLineFecCorrectedErrorsCounterIndex,
       "pm10010ulhCntlocalLineFecCorrectedErrorsCounterValuePortn": pm10010ulhCntlocalLineFecCorrectedErrorsCounterValuePortn,
       "pm10010ulhCntlocalLineFecCorrectedErrorsCounterErrorPortn": pm10010ulhCntlocalLineFecCorrectedErrorsCounterErrorPortn,
       "pm10010ulhCntlocalLineFecCorrectedErrorsCounterOverloadPortn": pm10010ulhCntlocalLineFecCorrectedErrorsCounterOverloadPortn,
       "pm10010ulhCntremoteLineSmBip8ErrorCounterTable": pm10010ulhCntremoteLineSmBip8ErrorCounterTable,
       "pm10010ulhCntremoteLineSmBip8ErrorCounterEntry": pm10010ulhCntremoteLineSmBip8ErrorCounterEntry,
       "pm10010ulhCntremoteLineSmBip8ErrorCounterIndex": pm10010ulhCntremoteLineSmBip8ErrorCounterIndex,
       "pm10010ulhCntremoteLineSmBip8ErrorCounterValuePortn": pm10010ulhCntremoteLineSmBip8ErrorCounterValuePortn,
       "pm10010ulhCntremoteLineSmBip8ErrorCounterErrorPortn": pm10010ulhCntremoteLineSmBip8ErrorCounterErrorPortn,
       "pm10010ulhCntremoteLineSmBip8ErrorCounterOverloadPortn": pm10010ulhCntremoteLineSmBip8ErrorCounterOverloadPortn,
       "pm10010ulhCntlineDfrmTimCntTable": pm10010ulhCntlineDfrmTimCntTable,
       "pm10010ulhCntlineDfrmTimCntEntry": pm10010ulhCntlineDfrmTimCntEntry,
       "pm10010ulhCntlineDfrmTimCntIndex": pm10010ulhCntlineDfrmTimCntIndex,
       "pm10010ulhCntlineDfrmTimCntValuePortn": pm10010ulhCntlineDfrmTimCntValuePortn,
       "pm10010ulhCntlineDfrmTimCntErrorPortn": pm10010ulhCntlineDfrmTimCntErrorPortn,
       "pm10010ulhCntlineDfrmTimCntOverloadPortn": pm10010ulhCntlineDfrmTimCntOverloadPortn,
       "pm10010ulhCntlocalLineTrscvPreSdFecErrorCounterTable": pm10010ulhCntlocalLineTrscvPreSdFecErrorCounterTable,
       "pm10010ulhCntlocalLineTrscvPreSdFecErrorCounterEntry": pm10010ulhCntlocalLineTrscvPreSdFecErrorCounterEntry,
       "pm10010ulhCntlocalLineTrscvPreSdFecErrorCounterIndex": pm10010ulhCntlocalLineTrscvPreSdFecErrorCounterIndex,
       "pm10010ulhCntlocalLineTrscvPreSdFecErrorCounterValuePortn": pm10010ulhCntlocalLineTrscvPreSdFecErrorCounterValuePortn,
       "pm10010ulhCntlocalLineTrscvPreSdFecErrorCounterErrorPortn": pm10010ulhCntlocalLineTrscvPreSdFecErrorCounterErrorPortn,
       "pm10010ulhCntlocalLineTrscvPreSdFecErrorCounterOverloadPortn": pm10010ulhCntlocalLineTrscvPreSdFecErrorCounterOverloadPortn,
       "pm10010ulhCntlocalLineTrscvUncorrectedSdFecErrorCounterTable": pm10010ulhCntlocalLineTrscvUncorrectedSdFecErrorCounterTable,
       "pm10010ulhCntlocalLineTrscvUncorrectedSdFecErrorCounterEntry": pm10010ulhCntlocalLineTrscvUncorrectedSdFecErrorCounterEntry,
       "pm10010ulhCntlocalLineTrscvUncorrectedSdFecErrorCounterIndex": pm10010ulhCntlocalLineTrscvUncorrectedSdFecErrorCounterIndex,
       "pm10010ulhCntlocalLineTrscvUncorrectedSdFecErrorCounterValuePortn": pm10010ulhCntlocalLineTrscvUncorrectedSdFecErrorCounterValuePortn,
       "pm10010ulhCntlocalLineTrscvUncorrectedSdFecErrorCounterErrorPortn": pm10010ulhCntlocalLineTrscvUncorrectedSdFecErrorCounterErrorPortn,
       "pm10010ulhCntlocalLineTrscvUncorrectedSdFecErrorCounterOverloadPortn": pm10010ulhCntlocalLineTrscvUncorrectedSdFecErrorCounterOverloadPortn,
       "pm10010ulhCntlocalLineTrscvPreSdFecBitCounterTable": pm10010ulhCntlocalLineTrscvPreSdFecBitCounterTable,
       "pm10010ulhCntlocalLineTrscvPreSdFecBitCounterEntry": pm10010ulhCntlocalLineTrscvPreSdFecBitCounterEntry,
       "pm10010ulhCntlocalLineTrscvPreSdFecBitCounterIndex": pm10010ulhCntlocalLineTrscvPreSdFecBitCounterIndex,
       "pm10010ulhCntlocalLineTrscvPreSdFecBitCounterValuePortn": pm10010ulhCntlocalLineTrscvPreSdFecBitCounterValuePortn,
       "pm10010ulhCntlocalLineTrscvPreSdFecBitCounterErrorPortn": pm10010ulhCntlocalLineTrscvPreSdFecBitCounterErrorPortn,
       "pm10010ulhCntlocalLineTrscvPreSdFecBitCounterOverloadPortn": pm10010ulhCntlocalLineTrscvPreSdFecBitCounterOverloadPortn,
       "pm10010ulhCntlocalLineTrscvUncorrectedSdFecBitCounterTable": pm10010ulhCntlocalLineTrscvUncorrectedSdFecBitCounterTable,
       "pm10010ulhCntlocalLineTrscvUncorrectedSdFecBitCounterEntry": pm10010ulhCntlocalLineTrscvUncorrectedSdFecBitCounterEntry,
       "pm10010ulhCntlocalLineTrscvUncorrectedSdFecBitCounterIndex": pm10010ulhCntlocalLineTrscvUncorrectedSdFecBitCounterIndex,
       "pm10010ulhCntlocalLineTrscvUncorrectedSdFecBitCounterValuePortn": pm10010ulhCntlocalLineTrscvUncorrectedSdFecBitCounterValuePortn,
       "pm10010ulhCntlocalLineTrscvUncorrectedSdFecBitCounterErrorPortn": pm10010ulhCntlocalLineTrscvUncorrectedSdFecBitCounterErrorPortn,
       "pm10010ulhCntlocalLineTrscvUncorrectedSdFecBitCounterOverloadPortn": pm10010ulhCntlocalLineTrscvUncorrectedSdFecBitCounterOverloadPortn,
       "pm10010ulhcontrolsWrite": pm10010ulhcontrolsWrite,
       "pm10010ulhCtrlOther": pm10010ulhCtrlOther,
       "pm10010ulhCtrlconfMgnt1": pm10010ulhCtrlconfMgnt1,
       "pm10010ulhCtrlConf1Load1": pm10010ulhCtrlConf1Load1,
       "pm10010ulhCtrlConf2Load1": pm10010ulhCtrlConf2Load1,
       "pm10010ulhCtrlConf2Flash1": pm10010ulhCtrlConf2Flash1,
       "pm10010ulhCtrlConf2Clear1": pm10010ulhCtrlConf2Clear1,
       "pm10010ulhCtrlsynth4": pm10010ulhCtrlsynth4,
       "pm10010ulhCtrlCorrelatOn": pm10010ulhCtrlCorrelatOn,
       "pm10010ulhCtrlCorrelatOff": pm10010ulhCtrlCorrelatOff,
       "pm10010ulhCtrlswMgnt": pm10010ulhCtrlswMgnt,
       "pm10010ulhCtrlColdReset": pm10010ulhCtrlColdReset,
       "pm10010ulhCtrlWarmReset": pm10010ulhCtrlWarmReset,
       "pm10010ulhCtrlLoadSwBank1": pm10010ulhCtrlLoadSwBank1,
       "pm10010ulhCtrlLoadSwBank2": pm10010ulhCtrlLoadSwBank2,
       "pm10010ulhCtrlgwMgnt": pm10010ulhCtrlgwMgnt,
       "pm10010ulhCtrlCurrentGwReset": pm10010ulhCtrlCurrentGwReset,
       "pm10010ulhCtrlLoadGwBank1": pm10010ulhCtrlLoadGwBank1,
       "pm10010ulhCtrlLoadGwBank2": pm10010ulhCtrlLoadGwBank2,
       "pm10010ulhCtrlLoadGwBank3": pm10010ulhCtrlLoadGwBank3,
       "pm10010ulhCtrlLoadGwBank4": pm10010ulhCtrlLoadGwBank4,
       "pm10010ulhCtrlledTest": pm10010ulhCtrlledTest,
       "pm10010ulhCtrlGreenLed": pm10010ulhCtrlGreenLed,
       "pm10010ulhCtrlRedLed": pm10010ulhCtrlRedLed,
       "pm10010ulhCtrlLedOff": pm10010ulhCtrlLedOff,
       "pm10010ulhCtrlinitSwitchMarvell": pm10010ulhCtrlinitSwitchMarvell,
       "pm10010ulhCtrlInitSwitchMarvell": pm10010ulhCtrlInitSwitchMarvell,
       "pm10010ulhCtrlresetCount": pm10010ulhCtrlresetCount,
       "pm10010ulhCtrlResetcount": pm10010ulhCtrlResetcount,
       "pm10010ulhCtrlresetRmon": pm10010ulhCtrlresetRmon,
       "pm10010ulhCtrlResetrmon": pm10010ulhCtrlResetrmon,
       "pm10010ulhCtrlresetMeasurements": pm10010ulhCtrlresetMeasurements,
       "pm10010ulhCtrlResetmeasurements": pm10010ulhCtrlResetmeasurements,
       "pm10010ulhCtrlClient": pm10010ulhCtrlClient,
       "pm10010ulhCtrlaccessLoopTable": pm10010ulhCtrlaccessLoopTable,
       "pm10010ulhCtrlaccessLoopEntry": pm10010ulhCtrlaccessLoopEntry,
       "pm10010ulhCtrlaccessLoopIndex": pm10010ulhCtrlaccessLoopIndex,
       "pm10010ulhCtrlaccessLoopPortn": pm10010ulhCtrlaccessLoopPortn,
       "pm10010ulhCtrlclientLoopToLineTable": pm10010ulhCtrlclientLoopToLineTable,
       "pm10010ulhCtrlclientLoopToLineEntry": pm10010ulhCtrlclientLoopToLineEntry,
       "pm10010ulhCtrlclientLoopToLineIndex": pm10010ulhCtrlclientLoopToLineIndex,
       "pm10010ulhCtrlclientLoopToLinePortn": pm10010ulhCtrlclientLoopToLinePortn,
       "pm10010ulhCtrlcsfUpInsTable": pm10010ulhCtrlcsfUpInsTable,
       "pm10010ulhCtrlcsfUpInsEntry": pm10010ulhCtrlcsfUpInsEntry,
       "pm10010ulhCtrlcsfUpInsIndex": pm10010ulhCtrlcsfUpInsIndex,
       "pm10010ulhCtrlcsfUpInsPortn": pm10010ulhCtrlcsfUpInsPortn,
       "pm10010ulhCtrlcaisDwInsTable": pm10010ulhCtrlcaisDwInsTable,
       "pm10010ulhCtrlcaisDwInsEntry": pm10010ulhCtrlcaisDwInsEntry,
       "pm10010ulhCtrlcaisDwInsIndex": pm10010ulhCtrlcaisDwInsIndex,
       "pm10010ulhCtrlcaisDwInsPortn": pm10010ulhCtrlcaisDwInsPortn,
       "pm10010ulhCtrlclientResetAllCountTable": pm10010ulhCtrlclientResetAllCountTable,
       "pm10010ulhCtrlclientResetAllCountEntry": pm10010ulhCtrlclientResetAllCountEntry,
       "pm10010ulhCtrlclientResetAllCountIndex": pm10010ulhCtrlclientResetAllCountIndex,
       "pm10010ulhCtrlclientResetAllCountsPortn": pm10010ulhCtrlclientResetAllCountsPortn,
       "pm10010ulhCtrlLine": pm10010ulhCtrlLine,
       "pm10010ulhCtrlcommAccessLoopTable": pm10010ulhCtrlcommAccessLoopTable,
       "pm10010ulhCtrlcommAccessLoopEntry": pm10010ulhCtrlcommAccessLoopEntry,
       "pm10010ulhCtrlcommAccessLoopIndex": pm10010ulhCtrlcommAccessLoopIndex,
       "pm10010ulhCtrlcommAccessLoopPortn": pm10010ulhCtrlcommAccessLoopPortn,
       "pm10010ulhCtrllineLoopTable": pm10010ulhCtrllineLoopTable,
       "pm10010ulhCtrllineLoopEntry": pm10010ulhCtrllineLoopEntry,
       "pm10010ulhCtrllineLoopIndex": pm10010ulhCtrllineLoopIndex,
       "pm10010ulhCtrllineLoopPortn": pm10010ulhCtrllineLoopPortn,
       "pm10010ulhCtrlfecDisableTable": pm10010ulhCtrlfecDisableTable,
       "pm10010ulhCtrlfecDisableEntry": pm10010ulhCtrlfecDisableEntry,
       "pm10010ulhCtrlfecDisableIndex": pm10010ulhCtrlfecDisableIndex,
       "pm10010ulhCtrlfecDisablePortn": pm10010ulhCtrlfecDisablePortn,
       "pm10010ulhCtrlmsaLineLoopTable": pm10010ulhCtrlmsaLineLoopTable,
       "pm10010ulhCtrlmsaLineLoopEntry": pm10010ulhCtrlmsaLineLoopEntry,
       "pm10010ulhCtrlmsaLineLoopIndex": pm10010ulhCtrlmsaLineLoopIndex,
       "pm10010ulhCtrlmsaLineLoopPortn": pm10010ulhCtrlmsaLineLoopPortn,
       "pm10010ulhCtrlmsaTxResetTable": pm10010ulhCtrlmsaTxResetTable,
       "pm10010ulhCtrlmsaTxResetEntry": pm10010ulhCtrlmsaTxResetEntry,
       "pm10010ulhCtrlmsaTxResetIndex": pm10010ulhCtrlmsaTxResetIndex,
       "pm10010ulhCtrlmsaTxResetPortn": pm10010ulhCtrlmsaTxResetPortn,
       "pm10010ulhCtrlmsaRxResetTable": pm10010ulhCtrlmsaRxResetTable,
       "pm10010ulhCtrlmsaRxResetEntry": pm10010ulhCtrlmsaRxResetEntry,
       "pm10010ulhCtrlmsaRxResetIndex": pm10010ulhCtrlmsaRxResetIndex,
       "pm10010ulhCtrlmsaRxResetPortn": pm10010ulhCtrlmsaRxResetPortn,
       "pm10010ulhCtrlmsaShutdownTable": pm10010ulhCtrlmsaShutdownTable,
       "pm10010ulhCtrlmsaShutdownEntry": pm10010ulhCtrlmsaShutdownEntry,
       "pm10010ulhCtrlmsaShutdownIndex": pm10010ulhCtrlmsaShutdownIndex,
       "pm10010ulhCtrlmsaShutdownPortn": pm10010ulhCtrlmsaShutdownPortn,
       "pm10010ulhCtrllineResetAllCountTable": pm10010ulhCtrllineResetAllCountTable,
       "pm10010ulhCtrllineResetAllCountEntry": pm10010ulhCtrllineResetAllCountEntry,
       "pm10010ulhCtrllineResetAllCountIndex": pm10010ulhCtrllineResetAllCountIndex,
       "pm10010ulhCtrllineResetAllCountsPortn": pm10010ulhCtrllineResetAllCountsPortn,
       "pm10010ulhri": pm10010ulhri,
       "pm10010ulhriTable": pm10010ulhriTable,
       "pm10010ulhRinvSfpTable": pm10010ulhRinvSfpTable,
       "pm10010ulhRinvSfpEntry": pm10010ulhRinvSfpEntry,
       "pm10010ulhRinvSfpIndex": pm10010ulhRinvSfpIndex,
       "pm10010ulhRinvsfp": pm10010ulhRinvsfp,
       "pm10010ulhRinvLineTable": pm10010ulhRinvLineTable,
       "pm10010ulhRinvLineEntry": pm10010ulhRinvLineEntry,
       "pm10010ulhRinvLineIndex": pm10010ulhRinvLineIndex,
       "pm10010ulhRinvxfpLine": pm10010ulhRinvxfpLine,
       "pm10010ulhRinvReloadInventory": pm10010ulhRinvReloadInventory,
       "pm10010ulhRinvHwPlatform": pm10010ulhRinvHwPlatform,
       "pm10010ulhRinvModulePlatform": pm10010ulhRinvModulePlatform,
       "pm10010ulhRinvSwPlatform": pm10010ulhRinvSwPlatform,
       "pm10010ulhRinvGwPlatform": pm10010ulhRinvGwPlatform,
       "pm10010ulhdownload": pm10010ulhdownload,
       "pm10010ulhDwlOther": pm10010ulhDwlOther,
       "pm10010ulhDwlrestartProcess": pm10010ulhDwlrestartProcess,
       "pm10010ulhDwlWarmRestartProcessed": pm10010ulhDwlWarmRestartProcessed,
       "pm10010ulhDwlColdRestartProcessed": pm10010ulhDwlColdRestartProcessed,
       "pm10010ulhDwlswBanksUsed": pm10010ulhDwlswBanksUsed,
       "pm10010ulhDwlSwBank1Used": pm10010ulhDwlSwBank1Used,
       "pm10010ulhDwlSwBank2Used": pm10010ulhDwlSwBank2Used,
       "pm10010ulhDwlSwBank1Notempty": pm10010ulhDwlSwBank1Notempty,
       "pm10010ulhDwlSwBank2Notempty": pm10010ulhDwlSwBank2Notempty,
       "pm10010ulhDwlgwBanksUsed": pm10010ulhDwlgwBanksUsed,
       "pm10010ulhDwlGwBank1Used": pm10010ulhDwlGwBank1Used,
       "pm10010ulhDwlGwBank2Used": pm10010ulhDwlGwBank2Used,
       "pm10010ulhDwlGwBank3Used": pm10010ulhDwlGwBank3Used,
       "pm10010ulhDwlGwBank4Used": pm10010ulhDwlGwBank4Used,
       "pm10010ulhDwlGwBank1Notempty": pm10010ulhDwlGwBank1Notempty,
       "pm10010ulhDwlGwBank2Notempty": pm10010ulhDwlGwBank2Notempty,
       "pm10010ulhDwlGwBank3Notempty": pm10010ulhDwlGwBank3Notempty,
       "pm10010ulhDwlGwBank4Notempty": pm10010ulhDwlGwBank4Notempty,
       "pm10010ulhDwlClient": pm10010ulhDwlClient,
       "pm10010ulhDwlLine": pm10010ulhDwlLine,
       "pm10010ulhConfig": pm10010ulhConfig,
       "pm10010ulhCfgAccessCAisCsf": pm10010ulhCfgAccessCAisCsf,
       "pm10010ulhCfgClientcaiscsfTable": pm10010ulhCfgClientcaiscsfTable,
       "pm10010ulhCfgClientcaiscsfEntry": pm10010ulhCfgClientcaiscsfEntry,
       "pm10010ulhCfgClientcaiscsfIndex": pm10010ulhCfgClientcaiscsfIndex,
       "pm10010ulhCfgReservePortn": pm10010ulhCfgReservePortn,
       "pm10010ulhCfgStartup": pm10010ulhCfgStartup,
       "pm10010ulhCfgClientStartupTable": pm10010ulhCfgClientStartupTable,
       "pm10010ulhCfgClientStartupEntry": pm10010ulhCfgClientStartupEntry,
       "pm10010ulhCfgClientStartupIndex": pm10010ulhCfgClientStartupIndex,
       "pm10010ulhCfgSystConfPortPortn": pm10010ulhCfgSystConfPortPortn,
       "pm10010ulhCfgNetConfPortPortn": pm10010ulhCfgNetConfPortPortn,
       "pm10010ulhCfgOptionsPortPortn": pm10010ulhCfgOptionsPortPortn,
       "pm10010ulhCfgLineStartupTable": pm10010ulhCfgLineStartupTable,
       "pm10010ulhCfgLineStartupEntry": pm10010ulhCfgLineStartupEntry,
       "pm10010ulhCfgLineStartupIndex": pm10010ulhCfgLineStartupIndex,
       "pm10010ulhCfgSystConfLinePortn": pm10010ulhCfgSystConfLinePortn,
       "pm10010ulhCfgOptionsLinePortn": pm10010ulhCfgOptionsLinePortn,
       "pm10010ulhCfgXfpTable": pm10010ulhCfgXfpTable,
       "pm10010ulhCfgXfpEntry": pm10010ulhCfgXfpEntry,
       "pm10010ulhCfgXfpIndex": pm10010ulhCfgXfpIndex,
       "pm10010ulhCfgSystConfMsaLinePortn": pm10010ulhCfgSystConfMsaLinePortn,
       "pm10010ulhCfgLabels": pm10010ulhCfgLabels,
       "pm10010ulhCfgLabelclientTable": pm10010ulhCfgLabelclientTable,
       "pm10010ulhCfgLabelclientEntry": pm10010ulhCfgLabelclientEntry,
       "pm10010ulhCfgLabelclientIndex": pm10010ulhCfgLabelclientIndex,
       "pm10010ulhCfgLabelclientPortn": pm10010ulhCfgLabelclientPortn,
       "pm10010ulhCfgLabellineTable": pm10010ulhCfgLabellineTable,
       "pm10010ulhCfgLabellineEntry": pm10010ulhCfgLabellineEntry,
       "pm10010ulhCfgLabellineIndex": pm10010ulhCfgLabellineIndex,
       "pm10010ulhCfgLabellinePortn": pm10010ulhCfgLabellinePortn,
       "pm10010ulhCfgStartuptlh": pm10010ulhCfgStartuptlh,
       "pm10010ulhCfgOtxtlhTable": pm10010ulhCfgOtxtlhTable,
       "pm10010ulhCfgOtxtlhEntry": pm10010ulhCfgOtxtlhEntry,
       "pm10010ulhCfgOtxtlhIndex": pm10010ulhCfgOtxtlhIndex,
       "pm10010ulhCfgLinePwrLaserPortn": pm10010ulhCfgLinePwrLaserPortn,
       "pm10010ulhCfgLineFCurrentPortn": pm10010ulhCfgLineFCurrentPortn,
       "pm10010ulhCfgLineGridCurrentPortn": pm10010ulhCfgLineGridCurrentPortn,
       "pm10010ulhCfgFPortn": pm10010ulhCfgFPortn,
       "pm10010ulhCfgRxLineFCurrentPortn": pm10010ulhCfgRxLineFCurrentPortn,
       "pm10010ulhCfgOther": pm10010ulhCfgOther,
       "pm10010ulhtablemoduleOther": pm10010ulhtablemoduleOther,
       "pm10010ulhCfgmode": pm10010ulhCfgmode,
       "pm10010ulhCfgfanLowSpeedThreshold": pm10010ulhCfgfanLowSpeedThreshold,
       "pm10010ulhCfgfanHighSpeedThreshold": pm10010ulhCfgfanHighSpeedThreshold,
       "pm10010ulhCfgStartuptablefive": pm10010ulhCfgStartuptablefive,
       "pm10010ulhCfgOtxtlhcapabilitiesTable": pm10010ulhCfgOtxtlhcapabilitiesTable,
       "pm10010ulhCfgOtxtlhcapabilitiesEntry": pm10010ulhCfgOtxtlhcapabilitiesEntry,
       "pm10010ulhCfgOtxtlhcapabilitiesIndex": pm10010ulhCfgOtxtlhcapabilitiesIndex,
       "pm10010ulhCfgComponentTypePortn": pm10010ulhCfgComponentTypePortn,
       "pm10010ulhCfgMiscellaneousPortn": pm10010ulhCfgMiscellaneousPortn,
       "pm10010ulhCfgFirstChannelPortn": pm10010ulhCfgFirstChannelPortn,
       "pm10010ulhCfgLastChannelPortn": pm10010ulhCfgLastChannelPortn,
       "pm10010ulhCfgGridPortn": pm10010ulhCfgGridPortn,
       "pm10010ulhCfgWriteConfiguration": pm10010ulhCfgWriteConfiguration,
       "pm10010ulhtraps": pm10010ulhtraps,
       "pm10010ulhtrapPortNumber": pm10010ulhtrapPortNumber,
       "pm10010ulhtrapLineNumber": pm10010ulhtrapLineNumber,
       "pm10010ulhtrapBoardNumber": pm10010ulhtrapBoardNumber,
       "pm10010ulhLineTrapNotUrgentGoesOn": pm10010ulhLineTrapNotUrgentGoesOn,
       "pm10010ulhLineTrapNotUrgentGoesOff": pm10010ulhLineTrapNotUrgentGoesOff,
       "pm10010ulhLineTrapUrgentGoesOn": pm10010ulhLineTrapUrgentGoesOn,
       "pm10010ulhLineTrapUrgentGoesOff": pm10010ulhLineTrapUrgentGoesOff,
       "pm10010ulhLineTrapCritGoesOn": pm10010ulhLineTrapCritGoesOn,
       "pm10010ulhLineTrapCritGoesOff": pm10010ulhLineTrapCritGoesOff,
       "pm10010ulhClientTrapNotUrgentGoesOn": pm10010ulhClientTrapNotUrgentGoesOn,
       "pm10010ulhClientTrapNotUrgentGoesOff": pm10010ulhClientTrapNotUrgentGoesOff,
       "pm10010ulhClientTrapUrgentGoesOn": pm10010ulhClientTrapUrgentGoesOn,
       "pm10010ulhClientTrapUrgentGoesOff": pm10010ulhClientTrapUrgentGoesOff,
       "pm10010ulhClientTrapCritGoesOn": pm10010ulhClientTrapCritGoesOn,
       "pm10010ulhClientTrapCritGoesOff": pm10010ulhClientTrapCritGoesOff,
       "pm10010ulhPowerTrapUrgentGoesOn": pm10010ulhPowerTrapUrgentGoesOn,
       "pm10010ulhPowerTrapUrgentGoesOff": pm10010ulhPowerTrapUrgentGoesOff,
       "pm10010ulhMonitoring": pm10010ulhMonitoring,
       "pm10010ulhMonOther": pm10010ulhMonOther,
       "pm10010ulhMonRmon": pm10010ulhMonRmon,
       "pm10010ulhMonClient": pm10010ulhMonClient,
       "pm10010ulhMonClientRmonCounter": pm10010ulhMonClientRmonCounter,
       "pm10010ulhMonupRmonBytesCounterClientInputTable": pm10010ulhMonupRmonBytesCounterClientInputTable,
       "pm10010ulhMonupRmonBytesCounterClientInputEntry": pm10010ulhMonupRmonBytesCounterClientInputEntry,
       "pm10010ulhMonupRmonBytesCounterClientInputIndex": pm10010ulhMonupRmonBytesCounterClientInputIndex,
       "pm10010ulhMonupRmonBytesCounterClientInputValuePortn": pm10010ulhMonupRmonBytesCounterClientInputValuePortn,
       "pm10010ulhMonupRmonBytesCounterClientInputErrorPortn": pm10010ulhMonupRmonBytesCounterClientInputErrorPortn,
       "pm10010ulhMonupRmonBytesCounterClientInputOverloadPortn": pm10010ulhMonupRmonBytesCounterClientInputOverloadPortn,
       "pm10010ulhMonupRmonCrcErrorsCounterClientInputTable": pm10010ulhMonupRmonCrcErrorsCounterClientInputTable,
       "pm10010ulhMonupRmonCrcErrorsCounterClientInputEntry": pm10010ulhMonupRmonCrcErrorsCounterClientInputEntry,
       "pm10010ulhMonupRmonCrcErrorsCounterClientInputIndex": pm10010ulhMonupRmonCrcErrorsCounterClientInputIndex,
       "pm10010ulhMonupRmonCrcErrorsCounterClientInputValuePortn": pm10010ulhMonupRmonCrcErrorsCounterClientInputValuePortn,
       "pm10010ulhMonupRmonCrcErrorsCounterClientInputErrorPortn": pm10010ulhMonupRmonCrcErrorsCounterClientInputErrorPortn,
       "pm10010ulhMonupRmonCrcErrorsCounterClientInputOverloadPortn": pm10010ulhMonupRmonCrcErrorsCounterClientInputOverloadPortn,
       "pm10010ulhMonupRmonPacketsCounterClientInputTable": pm10010ulhMonupRmonPacketsCounterClientInputTable,
       "pm10010ulhMonupRmonPacketsCounterClientInputEntry": pm10010ulhMonupRmonPacketsCounterClientInputEntry,
       "pm10010ulhMonupRmonPacketsCounterClientInputIndex": pm10010ulhMonupRmonPacketsCounterClientInputIndex,
       "pm10010ulhMonupRmonPacketsCounterClientInputValuePortn": pm10010ulhMonupRmonPacketsCounterClientInputValuePortn,
       "pm10010ulhMonupRmonPacketsCounterClientInputErrorPortn": pm10010ulhMonupRmonPacketsCounterClientInputErrorPortn,
       "pm10010ulhMonupRmonPacketsCounterClientInputOverloadPortn": pm10010ulhMonupRmonPacketsCounterClientInputOverloadPortn,
       "pm10010ulhMonupRmonBroadcastCounterClientInputTable": pm10010ulhMonupRmonBroadcastCounterClientInputTable,
       "pm10010ulhMonupRmonBroadcastCounterClientInputEntry": pm10010ulhMonupRmonBroadcastCounterClientInputEntry,
       "pm10010ulhMonupRmonBroadcastCounterClientInputIndex": pm10010ulhMonupRmonBroadcastCounterClientInputIndex,
       "pm10010ulhMonupRmonBroadcastCounterClientInputValuePortn": pm10010ulhMonupRmonBroadcastCounterClientInputValuePortn,
       "pm10010ulhMonupRmonBroadcastCounterClientInputErrorPortn": pm10010ulhMonupRmonBroadcastCounterClientInputErrorPortn,
       "pm10010ulhMonupRmonBroadcastCounterClientInputOverloadPortn": pm10010ulhMonupRmonBroadcastCounterClientInputOverloadPortn,
       "pm10010ulhMonupRmonMulticastCounterClientInputTable": pm10010ulhMonupRmonMulticastCounterClientInputTable,
       "pm10010ulhMonupRmonMulticastCounterClientInputEntry": pm10010ulhMonupRmonMulticastCounterClientInputEntry,
       "pm10010ulhMonupRmonMulticastCounterClientInputIndex": pm10010ulhMonupRmonMulticastCounterClientInputIndex,
       "pm10010ulhMonupRmonMulticastCounterClientInputValuePortn": pm10010ulhMonupRmonMulticastCounterClientInputValuePortn,
       "pm10010ulhMonupRmonMulticastCounterClientInputErrorPortn": pm10010ulhMonupRmonMulticastCounterClientInputErrorPortn,
       "pm10010ulhMonupRmonMulticastCounterClientInputOverloadPortn": pm10010ulhMonupRmonMulticastCounterClientInputOverloadPortn,
       "pm10010ulhMonupRmonPauseFrameCounterClientInputTable": pm10010ulhMonupRmonPauseFrameCounterClientInputTable,
       "pm10010ulhMonupRmonPauseFrameCounterClientInputEntry": pm10010ulhMonupRmonPauseFrameCounterClientInputEntry,
       "pm10010ulhMonupRmonPauseFrameCounterClientInputIndex": pm10010ulhMonupRmonPauseFrameCounterClientInputIndex,
       "pm10010ulhMonupRmonPauseFrameCounterClientInputValuePortn": pm10010ulhMonupRmonPauseFrameCounterClientInputValuePortn,
       "pm10010ulhMonupRmonPauseFrameCounterClientInputErrorPortn": pm10010ulhMonupRmonPauseFrameCounterClientInputErrorPortn,
       "pm10010ulhMonupRmonPauseFrameCounterClientInputOverloadPortn": pm10010ulhMonupRmonPauseFrameCounterClientInputOverloadPortn,
       "pm10010ulhMonupRmonUnicastCounterClientInputTable": pm10010ulhMonupRmonUnicastCounterClientInputTable,
       "pm10010ulhMonupRmonUnicastCounterClientInputEntry": pm10010ulhMonupRmonUnicastCounterClientInputEntry,
       "pm10010ulhMonupRmonUnicastCounterClientInputIndex": pm10010ulhMonupRmonUnicastCounterClientInputIndex,
       "pm10010ulhMonupRmonUnicastCounterClientInputValuePortn": pm10010ulhMonupRmonUnicastCounterClientInputValuePortn,
       "pm10010ulhMonupRmonUnicastCounterClientInputErrorPortn": pm10010ulhMonupRmonUnicastCounterClientInputErrorPortn,
       "pm10010ulhMonupRmonUnicastCounterClientInputOverloadPortn": pm10010ulhMonupRmonUnicastCounterClientInputOverloadPortn,
       "pm10010ulhMonupRmonNonunicastCounterClientInputTable": pm10010ulhMonupRmonNonunicastCounterClientInputTable,
       "pm10010ulhMonupRmonNonunicastCounterClientInputEntry": pm10010ulhMonupRmonNonunicastCounterClientInputEntry,
       "pm10010ulhMonupRmonNonunicastCounterClientInputIndex": pm10010ulhMonupRmonNonunicastCounterClientInputIndex,
       "pm10010ulhMonupRmonNonunicastCounterClientInputValuePortn": pm10010ulhMonupRmonNonunicastCounterClientInputValuePortn,
       "pm10010ulhMonupRmonNonunicastCounterClientInputErrorPortn": pm10010ulhMonupRmonNonunicastCounterClientInputErrorPortn,
       "pm10010ulhMonupRmonNonunicastCounterClientInputOverloadPortn": pm10010ulhMonupRmonNonunicastCounterClientInputOverloadPortn,
       "pm10010ulhMondownRmonBytesCounterClientOutputTable": pm10010ulhMondownRmonBytesCounterClientOutputTable,
       "pm10010ulhMondownRmonBytesCounterClientOutputEntry": pm10010ulhMondownRmonBytesCounterClientOutputEntry,
       "pm10010ulhMondownRmonBytesCounterClientOutputIndex": pm10010ulhMondownRmonBytesCounterClientOutputIndex,
       "pm10010ulhMondownRmonBytesCounterClientOutputValuePortn": pm10010ulhMondownRmonBytesCounterClientOutputValuePortn,
       "pm10010ulhMondownRmonBytesCounterClientOutputErrorPortn": pm10010ulhMondownRmonBytesCounterClientOutputErrorPortn,
       "pm10010ulhMondownRmonBytesCounterClientOutputOverloadPortn": pm10010ulhMondownRmonBytesCounterClientOutputOverloadPortn,
       "pm10010ulhMondownRmonCrcErrorsCounterClientOutputTable": pm10010ulhMondownRmonCrcErrorsCounterClientOutputTable,
       "pm10010ulhMondownRmonCrcErrorsCounterClientOutputEntry": pm10010ulhMondownRmonCrcErrorsCounterClientOutputEntry,
       "pm10010ulhMondownRmonCrcErrorsCounterClientOutputIndex": pm10010ulhMondownRmonCrcErrorsCounterClientOutputIndex,
       "pm10010ulhMondownRmonCrcErrorsCounterClientOutputValuePortn": pm10010ulhMondownRmonCrcErrorsCounterClientOutputValuePortn,
       "pm10010ulhMondownRmonCrcErrorsCounterClientOutputErrorPortn": pm10010ulhMondownRmonCrcErrorsCounterClientOutputErrorPortn,
       "pm10010ulhMondownRmonCrcErrorsCounterClientOutputOverloadPortn": pm10010ulhMondownRmonCrcErrorsCounterClientOutputOverloadPortn,
       "pm10010ulhMondownRmonPacketsCounterClientOutputTable": pm10010ulhMondownRmonPacketsCounterClientOutputTable,
       "pm10010ulhMondownRmonPacketsCounterClientOutputEntry": pm10010ulhMondownRmonPacketsCounterClientOutputEntry,
       "pm10010ulhMondownRmonPacketsCounterClientOutputIndex": pm10010ulhMondownRmonPacketsCounterClientOutputIndex,
       "pm10010ulhMondownRmonPacketsCounterClientOutputValuePortn": pm10010ulhMondownRmonPacketsCounterClientOutputValuePortn,
       "pm10010ulhMondownRmonPacketsCounterClientOutputErrorPortn": pm10010ulhMondownRmonPacketsCounterClientOutputErrorPortn,
       "pm10010ulhMondownRmonPacketsCounterClientOutputOverloadPortn": pm10010ulhMondownRmonPacketsCounterClientOutputOverloadPortn,
       "pm10010ulhMondownRmonBroadcastCounterClientOutputTable": pm10010ulhMondownRmonBroadcastCounterClientOutputTable,
       "pm10010ulhMondownRmonBroadcastCounterClientOutputEntry": pm10010ulhMondownRmonBroadcastCounterClientOutputEntry,
       "pm10010ulhMondownRmonBroadcastCounterClientOutputIndex": pm10010ulhMondownRmonBroadcastCounterClientOutputIndex,
       "pm10010ulhMondownRmonBroadcastCounterClientOutputValuePortn": pm10010ulhMondownRmonBroadcastCounterClientOutputValuePortn,
       "pm10010ulhMondownRmonBroadcastCounterClientOutputErrorPortn": pm10010ulhMondownRmonBroadcastCounterClientOutputErrorPortn,
       "pm10010ulhMondownRmonBroadcastCounterClientOutputOverloadPortn": pm10010ulhMondownRmonBroadcastCounterClientOutputOverloadPortn,
       "pm10010ulhMondownRmonMulticastCounterClientOutputTable": pm10010ulhMondownRmonMulticastCounterClientOutputTable,
       "pm10010ulhMondownRmonMulticastCounterClientOutputEntry": pm10010ulhMondownRmonMulticastCounterClientOutputEntry,
       "pm10010ulhMondownRmonMulticastCounterClientOutputIndex": pm10010ulhMondownRmonMulticastCounterClientOutputIndex,
       "pm10010ulhMondownRmonMulticastCounterClientOutputValuePortn": pm10010ulhMondownRmonMulticastCounterClientOutputValuePortn,
       "pm10010ulhMondownRmonMulticastCounterClientOutputErrorPortn": pm10010ulhMondownRmonMulticastCounterClientOutputErrorPortn,
       "pm10010ulhMondownRmonMulticastCounterClientOutputOverloadPortn": pm10010ulhMondownRmonMulticastCounterClientOutputOverloadPortn,
       "pm10010ulhMondownRmonPauseFrameCounterClientOutputTable": pm10010ulhMondownRmonPauseFrameCounterClientOutputTable,
       "pm10010ulhMondownRmonPauseFrameCounterClientOutputEntry": pm10010ulhMondownRmonPauseFrameCounterClientOutputEntry,
       "pm10010ulhMondownRmonPauseFrameCounterClientOutputIndex": pm10010ulhMondownRmonPauseFrameCounterClientOutputIndex,
       "pm10010ulhMondownRmonPauseFrameCounterClientOutputValuePortn": pm10010ulhMondownRmonPauseFrameCounterClientOutputValuePortn,
       "pm10010ulhMondownRmonPauseFrameCounterClientOutputErrorPortn": pm10010ulhMondownRmonPauseFrameCounterClientOutputErrorPortn,
       "pm10010ulhMondownRmonPauseFrameCounterClientOutputOverloadPortn": pm10010ulhMondownRmonPauseFrameCounterClientOutputOverloadPortn,
       "pm10010ulhMondownRmonUnicastCounterClientOutputTable": pm10010ulhMondownRmonUnicastCounterClientOutputTable,
       "pm10010ulhMondownRmonUnicastCounterClientOutputEntry": pm10010ulhMondownRmonUnicastCounterClientOutputEntry,
       "pm10010ulhMondownRmonUnicastCounterClientOutputIndex": pm10010ulhMondownRmonUnicastCounterClientOutputIndex,
       "pm10010ulhMondownRmonUnicastCounterClientOutputValuePortn": pm10010ulhMondownRmonUnicastCounterClientOutputValuePortn,
       "pm10010ulhMondownRmonUnicastCounterClientOutputErrorPortn": pm10010ulhMondownRmonUnicastCounterClientOutputErrorPortn,
       "pm10010ulhMondownRmonUnicastCounterClientOutputOverloadPortn": pm10010ulhMondownRmonUnicastCounterClientOutputOverloadPortn,
       "pm10010ulhMondownRmonNonunicastCounterClientOutputTable": pm10010ulhMondownRmonNonunicastCounterClientOutputTable,
       "pm10010ulhMondownRmonNonunicastCounterClientOutputEntry": pm10010ulhMondownRmonNonunicastCounterClientOutputEntry,
       "pm10010ulhMondownRmonNonunicastCounterClientOutputIndex": pm10010ulhMondownRmonNonunicastCounterClientOutputIndex,
       "pm10010ulhMondownRmonNonunicastCounterClientOutputValuePortn": pm10010ulhMondownRmonNonunicastCounterClientOutputValuePortn,
       "pm10010ulhMondownRmonNonunicastCounterClientOutputErrorPortn": pm10010ulhMondownRmonNonunicastCounterClientOutputErrorPortn,
       "pm10010ulhMondownRmonNonunicastCounterClientOutputOverloadPortn": pm10010ulhMondownRmonNonunicastCounterClientOutputOverloadPortn,
       "pm10010ulhMonPerfOther": pm10010ulhMonPerfOther,
       "pm10010ulhMonPerfSync": pm10010ulhMonPerfSync,
       "pm10010ulhPerfEnable": pm10010ulhPerfEnable,
       "pm10010ulhPerf15minSync": pm10010ulhPerf15minSync,
       "pm10010ulhPerf24hSync": pm10010ulhPerf24hSync,
       "pm10010ulhMonPerfTimeStamp": pm10010ulhMonPerfTimeStamp,
       "pm10010ulhPerf15MinShort": pm10010ulhPerf15MinShort,
       "pm10010ulhPerf15MinLong": pm10010ulhPerf15MinLong,
       "pm10010ulhPerf24HoursShort": pm10010ulhPerf24HoursShort,
       "pm10010ulhPerf24HoursLong": pm10010ulhPerf24HoursLong,
       "pm10010ulhPerfCurrent15MinElapsedTime": pm10010ulhPerfCurrent15MinElapsedTime,
       "pm10010ulhPerfCurrent24HoursElapsedTime": pm10010ulhPerfCurrent24HoursElapsedTime,
       "pm10010ulhMonPerfClient": pm10010ulhMonPerfClient,
       "pm10010ulhPerfTelecomInputClientCurrent15StatTable": pm10010ulhPerfTelecomInputClientCurrent15StatTable,
       "pm10010ulhPerfTelecomInputClientCurrent15StatEntry": pm10010ulhPerfTelecomInputClientCurrent15StatEntry,
       "pm10010ulhPerfTelecomInputClientCurrent15StatIndex": pm10010ulhPerfTelecomInputClientCurrent15StatIndex,
       "pm10010ulhPerfTelecomInputClientCurrent15StatInvCvPortn": pm10010ulhPerfTelecomInputClientCurrent15StatInvCvPortn,
       "pm10010ulhPerfTelecomInputClientCurrent15StatCvValuePortn": pm10010ulhPerfTelecomInputClientCurrent15StatCvValuePortn,
       "pm10010ulhPerfTelecomInputClientCurrent15StatInvEsPortn": pm10010ulhPerfTelecomInputClientCurrent15StatInvEsPortn,
       "pm10010ulhPerfTelecomInputClientCurrent15StatEsValuePortn": pm10010ulhPerfTelecomInputClientCurrent15StatEsValuePortn,
       "pm10010ulhPerfTelecomInputClientCurrent15StatInvSesPortn": pm10010ulhPerfTelecomInputClientCurrent15StatInvSesPortn,
       "pm10010ulhPerfTelecomInputClientCurrent15StatSesValuePortn": pm10010ulhPerfTelecomInputClientCurrent15StatSesValuePortn,
       "pm10010ulhPerfTelecomInputClientCurrent15StatInvSefsPortn": pm10010ulhPerfTelecomInputClientCurrent15StatInvSefsPortn,
       "pm10010ulhPerfTelecomInputClientCurrent15StatSefsValuePortn": pm10010ulhPerfTelecomInputClientCurrent15StatSefsValuePortn,
       "pm10010ulhPerfTelecomInputClientCurrent15StatInvUasPortn": pm10010ulhPerfTelecomInputClientCurrent15StatInvUasPortn,
       "pm10010ulhPerfTelecomInputClientCurrent15StatUasValuePortn": pm10010ulhPerfTelecomInputClientCurrent15StatUasValuePortn,
       "pm10010ulhPerfTelecomInputClientPast15StatHistoryPort1Table": pm10010ulhPerfTelecomInputClientPast15StatHistoryPort1Table,
       "pm10010ulhPerfTelecomInputClientPast15StatHistoryPort1Entry": pm10010ulhPerfTelecomInputClientPast15StatHistoryPort1Entry,
       "pm10010ulhPerfTelecomInputClientPast15StatHistoryPort1Index": pm10010ulhPerfTelecomInputClientPast15StatHistoryPort1Index,
       "pm10010ulhPerfTelecomInputClientPast15StatHistoryInvCvPort1": pm10010ulhPerfTelecomInputClientPast15StatHistoryInvCvPort1,
       "pm10010ulhPerfTelecomInputClientPast15StatHistoryCvValuePort1": pm10010ulhPerfTelecomInputClientPast15StatHistoryCvValuePort1,
       "pm10010ulhPerfTelecomInputClientPast15StatHistoryInvEsPort1": pm10010ulhPerfTelecomInputClientPast15StatHistoryInvEsPort1,
       "pm10010ulhPerfTelecomInputClientPast15StatHistoryEsValuePort1": pm10010ulhPerfTelecomInputClientPast15StatHistoryEsValuePort1,
       "pm10010ulhPerfTelecomInputClientPast15StatHistoryInvSesPort1": pm10010ulhPerfTelecomInputClientPast15StatHistoryInvSesPort1,
       "pm10010ulhPerfTelecomInputClientPast15StatHistorySesValuePort1": pm10010ulhPerfTelecomInputClientPast15StatHistorySesValuePort1,
       "pm10010ulhPerfTelecomInputClientPast15StatHistoryInvSefsPort1": pm10010ulhPerfTelecomInputClientPast15StatHistoryInvSefsPort1,
       "pm10010ulhPerfTelecomInputClientPast15StatHistorySefsValuePort1": pm10010ulhPerfTelecomInputClientPast15StatHistorySefsValuePort1,
       "pm10010ulhPerfTelecomInputClientPast15StatHistoryInvUasPort1": pm10010ulhPerfTelecomInputClientPast15StatHistoryInvUasPort1,
       "pm10010ulhPerfTelecomInputClientPast15StatHistoryUasValuePort1": pm10010ulhPerfTelecomInputClientPast15StatHistoryUasValuePort1,
       "pm10010ulhPerfTelecomInputClientCurrent24StatTable": pm10010ulhPerfTelecomInputClientCurrent24StatTable,
       "pm10010ulhPerfTelecomInputClientCurrent24StatEntry": pm10010ulhPerfTelecomInputClientCurrent24StatEntry,
       "pm10010ulhPerfTelecomInputClientCurrent24StatIndex": pm10010ulhPerfTelecomInputClientCurrent24StatIndex,
       "pm10010ulhPerfTelecomInputClientCurrent24StatInvCvPortn": pm10010ulhPerfTelecomInputClientCurrent24StatInvCvPortn,
       "pm10010ulhPerfTelecomInputClientCurrent24StatCvValuePortn": pm10010ulhPerfTelecomInputClientCurrent24StatCvValuePortn,
       "pm10010ulhPerfTelecomInputClientCurrent24StatInvEsPortn": pm10010ulhPerfTelecomInputClientCurrent24StatInvEsPortn,
       "pm10010ulhPerfTelecomInputClientCurrent24StatEsValuePortn": pm10010ulhPerfTelecomInputClientCurrent24StatEsValuePortn,
       "pm10010ulhPerfTelecomInputClientCurrent24StatInvSesPortn": pm10010ulhPerfTelecomInputClientCurrent24StatInvSesPortn,
       "pm10010ulhPerfTelecomInputClientCurrent24StatSesValuePortn": pm10010ulhPerfTelecomInputClientCurrent24StatSesValuePortn,
       "pm10010ulhPerfTelecomInputClientCurrent24StatInvSefsPortn": pm10010ulhPerfTelecomInputClientCurrent24StatInvSefsPortn,
       "pm10010ulhPerfTelecomInputClientCurrent24StatSefsValuePortn": pm10010ulhPerfTelecomInputClientCurrent24StatSefsValuePortn,
       "pm10010ulhPerfTelecomInputClientCurrent24StatInvUasPortn": pm10010ulhPerfTelecomInputClientCurrent24StatInvUasPortn,
       "pm10010ulhPerfTelecomInputClientCurrent24StatUasValuePortn": pm10010ulhPerfTelecomInputClientCurrent24StatUasValuePortn,
       "pm10010ulhPerfTelecomInputClientPast24StatHistoryPort1Table": pm10010ulhPerfTelecomInputClientPast24StatHistoryPort1Table,
       "pm10010ulhPerfTelecomInputClientPast24StatHistoryPort1Entry": pm10010ulhPerfTelecomInputClientPast24StatHistoryPort1Entry,
       "pm10010ulhPerfTelecomInputClientPast24StatHistoryPort1Index": pm10010ulhPerfTelecomInputClientPast24StatHistoryPort1Index,
       "pm10010ulhPerfTelecomInputClientPast24StatHistoryInvCvPort1": pm10010ulhPerfTelecomInputClientPast24StatHistoryInvCvPort1,
       "pm10010ulhPerfTelecomInputClientPast24StatHistoryCvValuePort1": pm10010ulhPerfTelecomInputClientPast24StatHistoryCvValuePort1,
       "pm10010ulhPerfTelecomInputClientPast24StatHistoryInvEsPort1": pm10010ulhPerfTelecomInputClientPast24StatHistoryInvEsPort1,
       "pm10010ulhPerfTelecomInputClientPast24StatHistoryEsValuePort1": pm10010ulhPerfTelecomInputClientPast24StatHistoryEsValuePort1,
       "pm10010ulhPerfTelecomInputClientPast24StatHistoryInvSesPort1": pm10010ulhPerfTelecomInputClientPast24StatHistoryInvSesPort1,
       "pm10010ulhPerfTelecomInputClientPast24StatHistorySesValuePort1": pm10010ulhPerfTelecomInputClientPast24StatHistorySesValuePort1,
       "pm10010ulhPerfTelecomInputClientPast24StatHistoryInvSefsPort1": pm10010ulhPerfTelecomInputClientPast24StatHistoryInvSefsPort1,
       "pm10010ulhPerfTelecomInputClientPast24StatHistorySefsValuePort1": pm10010ulhPerfTelecomInputClientPast24StatHistorySefsValuePort1,
       "pm10010ulhPerfTelecomInputClientPast24StatHistoryInvUasPort1": pm10010ulhPerfTelecomInputClientPast24StatHistoryInvUasPort1,
       "pm10010ulhPerfTelecomInputClientPast24StatHistoryUasValuePort1": pm10010ulhPerfTelecomInputClientPast24StatHistoryUasValuePort1,
       "pm10010ulhPerfTelecomOutputClientCurrent15StatTable": pm10010ulhPerfTelecomOutputClientCurrent15StatTable,
       "pm10010ulhPerfTelecomOutputClientCurrent15StatEntry": pm10010ulhPerfTelecomOutputClientCurrent15StatEntry,
       "pm10010ulhPerfTelecomOutputClientCurrent15StatIndex": pm10010ulhPerfTelecomOutputClientCurrent15StatIndex,
       "pm10010ulhPerfTelecomOutputClientCurrent15StatInvCvPortn": pm10010ulhPerfTelecomOutputClientCurrent15StatInvCvPortn,
       "pm10010ulhPerfTelecomOutputClientCurrent15StatCvValuePortn": pm10010ulhPerfTelecomOutputClientCurrent15StatCvValuePortn,
       "pm10010ulhPerfTelecomOutputClientCurrent15StatInvEsPortn": pm10010ulhPerfTelecomOutputClientCurrent15StatInvEsPortn,
       "pm10010ulhPerfTelecomOutputClientCurrent15StatEsValuePortn": pm10010ulhPerfTelecomOutputClientCurrent15StatEsValuePortn,
       "pm10010ulhPerfTelecomOutputClientCurrent15StatInvSesPortn": pm10010ulhPerfTelecomOutputClientCurrent15StatInvSesPortn,
       "pm10010ulhPerfTelecomOutputClientCurrent15StatSesValuePortn": pm10010ulhPerfTelecomOutputClientCurrent15StatSesValuePortn,
       "pm10010ulhPerfTelecomOutputClientCurrent15StatInvSefsPortn": pm10010ulhPerfTelecomOutputClientCurrent15StatInvSefsPortn,
       "pm10010ulhPerfTelecomOutputClientCurrent15StatSefsValuePortn": pm10010ulhPerfTelecomOutputClientCurrent15StatSefsValuePortn,
       "pm10010ulhPerfTelecomOutputClientCurrent15StatInvUasPortn": pm10010ulhPerfTelecomOutputClientCurrent15StatInvUasPortn,
       "pm10010ulhPerfTelecomOutputClientCurrent15StatUasValuePortn": pm10010ulhPerfTelecomOutputClientCurrent15StatUasValuePortn,
       "pm10010ulhPerfTelecomOutputClientPast15StatHistoryPort1Table": pm10010ulhPerfTelecomOutputClientPast15StatHistoryPort1Table,
       "pm10010ulhPerfTelecomOutputClientPast15StatHistoryPort1Entry": pm10010ulhPerfTelecomOutputClientPast15StatHistoryPort1Entry,
       "pm10010ulhPerfTelecomOutputClientPast15StatHistoryPort1Index": pm10010ulhPerfTelecomOutputClientPast15StatHistoryPort1Index,
       "pm10010ulhPerfTelecomOutputClientPast15StatHistoryInvCvPort1": pm10010ulhPerfTelecomOutputClientPast15StatHistoryInvCvPort1,
       "pm10010ulhPerfTelecomOutputClientPast15StatHistoryCvValuePort1": pm10010ulhPerfTelecomOutputClientPast15StatHistoryCvValuePort1,
       "pm10010ulhPerfTelecomOutputClientPast15StatHistoryInvEsPort1": pm10010ulhPerfTelecomOutputClientPast15StatHistoryInvEsPort1,
       "pm10010ulhPerfTelecomOutputClientPast15StatHistoryEsValuePort1": pm10010ulhPerfTelecomOutputClientPast15StatHistoryEsValuePort1,
       "pm10010ulhPerfTelecomOutputClientPast15StatHistoryInvSesPort1": pm10010ulhPerfTelecomOutputClientPast15StatHistoryInvSesPort1,
       "pm10010ulhPerfTelecomOutputClientPast15StatHistorySesValuePort1": pm10010ulhPerfTelecomOutputClientPast15StatHistorySesValuePort1,
       "pm10010ulhPerfTelecomOutputClientPast15StatHistoryInvSefsPort1": pm10010ulhPerfTelecomOutputClientPast15StatHistoryInvSefsPort1,
       "pm10010ulhPerfTelecomOutputClientPast15StatHistorySefsValuePort1": pm10010ulhPerfTelecomOutputClientPast15StatHistorySefsValuePort1,
       "pm10010ulhPerfTelecomOutputClientPast15StatHistoryInvUasPort1": pm10010ulhPerfTelecomOutputClientPast15StatHistoryInvUasPort1,
       "pm10010ulhPerfTelecomOutputClientPast15StatHistoryUasValuePort1": pm10010ulhPerfTelecomOutputClientPast15StatHistoryUasValuePort1,
       "pm10010ulhPerfTelecomOutputClientCurrent24StatTable": pm10010ulhPerfTelecomOutputClientCurrent24StatTable,
       "pm10010ulhPerfTelecomOutputClientCurrent24StatEntry": pm10010ulhPerfTelecomOutputClientCurrent24StatEntry,
       "pm10010ulhPerfTelecomOutputClientCurrent24StatIndex": pm10010ulhPerfTelecomOutputClientCurrent24StatIndex,
       "pm10010ulhPerfTelecomOutputClientCurrent24StatInvCvPortn": pm10010ulhPerfTelecomOutputClientCurrent24StatInvCvPortn,
       "pm10010ulhPerfTelecomOutputClientCurrent24StatCvValuePortn": pm10010ulhPerfTelecomOutputClientCurrent24StatCvValuePortn,
       "pm10010ulhPerfTelecomOutputClientCurrent24StatInvEsPortn": pm10010ulhPerfTelecomOutputClientCurrent24StatInvEsPortn,
       "pm10010ulhPerfTelecomOutputClientCurrent24StatEsValuePortn": pm10010ulhPerfTelecomOutputClientCurrent24StatEsValuePortn,
       "pm10010ulhPerfTelecomOutputClientCurrent24StatInvSesPortn": pm10010ulhPerfTelecomOutputClientCurrent24StatInvSesPortn,
       "pm10010ulhPerfTelecomOutputClientCurrent24StatSesValuePortn": pm10010ulhPerfTelecomOutputClientCurrent24StatSesValuePortn,
       "pm10010ulhPerfTelecomOutputClientCurrent24StatInvSefsPortn": pm10010ulhPerfTelecomOutputClientCurrent24StatInvSefsPortn,
       "pm10010ulhPerfTelecomOutputClientCurrent24StatSefsValuePortn": pm10010ulhPerfTelecomOutputClientCurrent24StatSefsValuePortn,
       "pm10010ulhPerfTelecomOutputClientCurrent24StatInvUasPortn": pm10010ulhPerfTelecomOutputClientCurrent24StatInvUasPortn,
       "pm10010ulhPerfTelecomOutputClientCurrent24StatUasValuePortn": pm10010ulhPerfTelecomOutputClientCurrent24StatUasValuePortn,
       "pm10010ulhPerfTelecomOutputClientPast24StatHistoryPort1Table": pm10010ulhPerfTelecomOutputClientPast24StatHistoryPort1Table,
       "pm10010ulhPerfTelecomOutputClientPast24StatHistoryPort1Entry": pm10010ulhPerfTelecomOutputClientPast24StatHistoryPort1Entry,
       "pm10010ulhPerfTelecomOutputClientPast24StatHistoryPort1Index": pm10010ulhPerfTelecomOutputClientPast24StatHistoryPort1Index,
       "pm10010ulhPerfTelecomOutputClientPast24StatHistoryInvCvPort1": pm10010ulhPerfTelecomOutputClientPast24StatHistoryInvCvPort1,
       "pm10010ulhPerfTelecomOutputClientPast24StatHistoryCvValuePort1": pm10010ulhPerfTelecomOutputClientPast24StatHistoryCvValuePort1,
       "pm10010ulhPerfTelecomOutputClientPast24StatHistoryInvEsPort1": pm10010ulhPerfTelecomOutputClientPast24StatHistoryInvEsPort1,
       "pm10010ulhPerfTelecomOutputClientPast24StatHistoryEsValuePort1": pm10010ulhPerfTelecomOutputClientPast24StatHistoryEsValuePort1,
       "pm10010ulhPerfTelecomOutputClientPast24StatHistoryInvSesPort1": pm10010ulhPerfTelecomOutputClientPast24StatHistoryInvSesPort1,
       "pm10010ulhPerfTelecomOutputClientPast24StatHistorySesValuePort1": pm10010ulhPerfTelecomOutputClientPast24StatHistorySesValuePort1,
       "pm10010ulhPerfTelecomOutputClientPast24StatHistoryInvSefsPort1": pm10010ulhPerfTelecomOutputClientPast24StatHistoryInvSefsPort1,
       "pm10010ulhPerfTelecomOutputClientPast24StatHistorySefsValuePort1": pm10010ulhPerfTelecomOutputClientPast24StatHistorySefsValuePort1,
       "pm10010ulhPerfTelecomOutputClientPast24StatHistoryInvUasPort1": pm10010ulhPerfTelecomOutputClientPast24StatHistoryInvUasPort1,
       "pm10010ulhPerfTelecomOutputClientPast24StatHistoryUasValuePort1": pm10010ulhPerfTelecomOutputClientPast24StatHistoryUasValuePort1,
       "pm10010ulhPerfDatacomClientCurrent15StatTable": pm10010ulhPerfDatacomClientCurrent15StatTable,
       "pm10010ulhPerfDatacomClientCurrent15StatEntry": pm10010ulhPerfDatacomClientCurrent15StatEntry,
       "pm10010ulhPerfDatacomClientCurrent15StatIndex": pm10010ulhPerfDatacomClientCurrent15StatIndex,
       "pm10010ulhperfdatacomclientCurrent15StatInCrcCountInvPortn": pm10010ulhperfdatacomclientCurrent15StatInCrcCountInvPortn,
       "pm10010ulhperfdatacomclientCurrent15StatInCrcCountPortn": pm10010ulhperfdatacomclientCurrent15StatInCrcCountPortn,
       "pm10010ulhperfdatacomclientCurrent15StatInPacketCountInvPortn": pm10010ulhperfdatacomclientCurrent15StatInPacketCountInvPortn,
       "pm10010ulhperfdatacomclientCurrent15StatInPacketCountPortn": pm10010ulhperfdatacomclientCurrent15StatInPacketCountPortn,
       "pm10010ulhperfdatacomclientCurrent15StatOutCrcCountInvPortn": pm10010ulhperfdatacomclientCurrent15StatOutCrcCountInvPortn,
       "pm10010ulhperfdatacomclientCurrent15StatOutCrcCountPortn": pm10010ulhperfdatacomclientCurrent15StatOutCrcCountPortn,
       "pm10010ulhperfdatacomclientCurrent15StatOutPacketCountInvPortn": pm10010ulhperfdatacomclientCurrent15StatOutPacketCountInvPortn,
       "pm10010ulhperfdatacomclientCurrent15StatOutPacketCountPortn": pm10010ulhperfdatacomclientCurrent15StatOutPacketCountPortn,
       "pm10010ulhPerfDatacomClientPast15StatHistoryPort1Table": pm10010ulhPerfDatacomClientPast15StatHistoryPort1Table,
       "pm10010ulhPerfDatacomClientPast15StatHistoryPort1Entry": pm10010ulhPerfDatacomClientPast15StatHistoryPort1Entry,
       "pm10010ulhPerfDatacomClientPast15StatHistoryPort1Index": pm10010ulhPerfDatacomClientPast15StatHistoryPort1Index,
       "pm10010ulhperfdatacomclientPast15StatInCrcCountInvPort1": pm10010ulhperfdatacomclientPast15StatInCrcCountInvPort1,
       "pm10010ulhperfdatacomclientPast15StatInCrcCountPort1": pm10010ulhperfdatacomclientPast15StatInCrcCountPort1,
       "pm10010ulhperfdatacomclientPast15StatInPacketCountInvPort1": pm10010ulhperfdatacomclientPast15StatInPacketCountInvPort1,
       "pm10010ulhperfdatacomclientPast15StatInPacketCountPort1": pm10010ulhperfdatacomclientPast15StatInPacketCountPort1,
       "pm10010ulhperfdatacomclientPast15StatOutCrcCountInvPort1": pm10010ulhperfdatacomclientPast15StatOutCrcCountInvPort1,
       "pm10010ulhperfdatacomclientPast15StatOutCrcCountPort1": pm10010ulhperfdatacomclientPast15StatOutCrcCountPort1,
       "pm10010ulhperfdatacomclientPast15StatOutPacketCountInvPort1": pm10010ulhperfdatacomclientPast15StatOutPacketCountInvPort1,
       "pm10010ulhperfdatacomclientPast15StatOutPacketCountPort1": pm10010ulhperfdatacomclientPast15StatOutPacketCountPort1,
       "pm10010ulhPerfDatacomClientCurrent24StatTable": pm10010ulhPerfDatacomClientCurrent24StatTable,
       "pm10010ulhPerfDatacomClientCurrent24StatEntry": pm10010ulhPerfDatacomClientCurrent24StatEntry,
       "pm10010ulhPerfDatacomClientCurrent24StatIndex": pm10010ulhPerfDatacomClientCurrent24StatIndex,
       "pm10010ulhperfdatacomclientCurrent24StatInCrcCountInvPortn": pm10010ulhperfdatacomclientCurrent24StatInCrcCountInvPortn,
       "pm10010ulhperfdatacomclientCurrent24StatInCrcCountPortn": pm10010ulhperfdatacomclientCurrent24StatInCrcCountPortn,
       "pm10010ulhperfdatacomclientCurrent24StatInPacketCountInvPortn": pm10010ulhperfdatacomclientCurrent24StatInPacketCountInvPortn,
       "pm10010ulhperfdatacomclientCurrent24StatInPacketCountPortn": pm10010ulhperfdatacomclientCurrent24StatInPacketCountPortn,
       "pm10010ulhperfdatacomclientCurrent24StatOutCrcCountInvPortn": pm10010ulhperfdatacomclientCurrent24StatOutCrcCountInvPortn,
       "pm10010ulhperfdatacomclientCurrent24StatOutCrcCountPortn": pm10010ulhperfdatacomclientCurrent24StatOutCrcCountPortn,
       "pm10010ulhperfdatacomclientCurrent24StatOutPacketCountInvPortn": pm10010ulhperfdatacomclientCurrent24StatOutPacketCountInvPortn,
       "pm10010ulhperfdatacomclientCurrent24StatOutPacketCountPortn": pm10010ulhperfdatacomclientCurrent24StatOutPacketCountPortn,
       "pm10010ulhPerfDatacomClientPast24StatHistoryPort1Table": pm10010ulhPerfDatacomClientPast24StatHistoryPort1Table,
       "pm10010ulhPerfDatacomClientPast24StatHistoryPort1Entry": pm10010ulhPerfDatacomClientPast24StatHistoryPort1Entry,
       "pm10010ulhPerfDatacomClientPast24StatHistoryPort1Index": pm10010ulhPerfDatacomClientPast24StatHistoryPort1Index,
       "pm10010ulhperfdatacomclientPast24StatInCrcCountInvPort1": pm10010ulhperfdatacomclientPast24StatInCrcCountInvPort1,
       "pm10010ulhperfdatacomclientPast24StatInCrcCountPort1": pm10010ulhperfdatacomclientPast24StatInCrcCountPort1,
       "pm10010ulhperfdatacomclientPast24StatInPacketCountInvPort1": pm10010ulhperfdatacomclientPast24StatInPacketCountInvPort1,
       "pm10010ulhperfdatacomclientPast24StatInPacketCountPort1": pm10010ulhperfdatacomclientPast24StatInPacketCountPort1,
       "pm10010ulhperfdatacomclientPast24StatOutCrcCountInvPort1": pm10010ulhperfdatacomclientPast24StatOutCrcCountInvPort1,
       "pm10010ulhperfdatacomclientPast24StatOutCrcCountPort1": pm10010ulhperfdatacomclientPast24StatOutCrcCountPort1,
       "pm10010ulhperfdatacomclientPast24StatOutPacketCountInvPort1": pm10010ulhperfdatacomclientPast24StatOutPacketCountInvPort1,
       "pm10010ulhperfdatacomclientPast24StatOutPacketCountPort1": pm10010ulhperfdatacomclientPast24StatOutPacketCountPort1,
       "pm10010ulhMonPerfLine": pm10010ulhMonPerfLine,
       "pm10010ulhPerfTelecomLinePostFecCurrent15StatTable": pm10010ulhPerfTelecomLinePostFecCurrent15StatTable,
       "pm10010ulhPerfTelecomLinePostFecCurrent15StatEntry": pm10010ulhPerfTelecomLinePostFecCurrent15StatEntry,
       "pm10010ulhPerfTelecomLinePostFecCurrent15StatIndex": pm10010ulhPerfTelecomLinePostFecCurrent15StatIndex,
       "pm10010ulhPerfTelecomLinePostFecCurrent15StatInvCvPortn": pm10010ulhPerfTelecomLinePostFecCurrent15StatInvCvPortn,
       "pm10010ulhPerfTelecomLinePostFecCurrent15StatCvValuePortn": pm10010ulhPerfTelecomLinePostFecCurrent15StatCvValuePortn,
       "pm10010ulhPerfTelecomLinePostFecCurrent15StatInvEsPortn": pm10010ulhPerfTelecomLinePostFecCurrent15StatInvEsPortn,
       "pm10010ulhPerfTelecomLinePostFecCurrent15StatEsValuePortn": pm10010ulhPerfTelecomLinePostFecCurrent15StatEsValuePortn,
       "pm10010ulhPerfTelecomLinePostFecCurrent15StatInvSesPortn": pm10010ulhPerfTelecomLinePostFecCurrent15StatInvSesPortn,
       "pm10010ulhPerfTelecomLinePostFecCurrent15StatSesValuePortn": pm10010ulhPerfTelecomLinePostFecCurrent15StatSesValuePortn,
       "pm10010ulhPerfTelecomLinePostFecCurrent15StatInvSefsPortn": pm10010ulhPerfTelecomLinePostFecCurrent15StatInvSefsPortn,
       "pm10010ulhPerfTelecomLinePostFecCurrent15StatSefsValuePortn": pm10010ulhPerfTelecomLinePostFecCurrent15StatSefsValuePortn,
       "pm10010ulhPerfTelecomLinePostFecCurrent15StatInvUasPortn": pm10010ulhPerfTelecomLinePostFecCurrent15StatInvUasPortn,
       "pm10010ulhPerfTelecomLinePostFecCurrent15StatUasValuePortn": pm10010ulhPerfTelecomLinePostFecCurrent15StatUasValuePortn,
       "pm10010ulhPerfTelecomLinePostFecPast15StatHistoryPort1Table": pm10010ulhPerfTelecomLinePostFecPast15StatHistoryPort1Table,
       "pm10010ulhPerfTelecomLinePostFecPast15StatHistoryPort1Entry": pm10010ulhPerfTelecomLinePostFecPast15StatHistoryPort1Entry,
       "pm10010ulhPerfTelecomLinePostFecPast15StatHistoryPort1Index": pm10010ulhPerfTelecomLinePostFecPast15StatHistoryPort1Index,
       "pm10010ulhPerfTelecomLinePostFecPast15StatHistoryInvCvPort1": pm10010ulhPerfTelecomLinePostFecPast15StatHistoryInvCvPort1,
       "pm10010ulhPerfTelecomLinePostFecPast15StatHistoryCvValuePort1": pm10010ulhPerfTelecomLinePostFecPast15StatHistoryCvValuePort1,
       "pm10010ulhPerfTelecomLinePostFecPast15StatHistoryInvEsPort1": pm10010ulhPerfTelecomLinePostFecPast15StatHistoryInvEsPort1,
       "pm10010ulhPerfTelecomLinePostFecPast15StatHistoryEsValuePort1": pm10010ulhPerfTelecomLinePostFecPast15StatHistoryEsValuePort1,
       "pm10010ulhPerfTelecomLinePostFecPast15StatHistoryInvSesPort1": pm10010ulhPerfTelecomLinePostFecPast15StatHistoryInvSesPort1,
       "pm10010ulhPerfTelecomLinePostFecPast15StatHistorySesValuePort1": pm10010ulhPerfTelecomLinePostFecPast15StatHistorySesValuePort1,
       "pm10010ulhPerfTelecomLinePostFecPast15StatHistoryInvSefsPort1": pm10010ulhPerfTelecomLinePostFecPast15StatHistoryInvSefsPort1,
       "pm10010ulhPerfTelecomLinePostFecPast15StatHistorySefsValuePort1": pm10010ulhPerfTelecomLinePostFecPast15StatHistorySefsValuePort1,
       "pm10010ulhPerfTelecomLinePostFecPast15StatHistoryInvUasPort1": pm10010ulhPerfTelecomLinePostFecPast15StatHistoryInvUasPort1,
       "pm10010ulhPerfTelecomLinePostFecPast15StatHistoryUasValuePort1": pm10010ulhPerfTelecomLinePostFecPast15StatHistoryUasValuePort1,
       "pm10010ulhPerfTelecomLinePostFecCurrent24StatTable": pm10010ulhPerfTelecomLinePostFecCurrent24StatTable,
       "pm10010ulhPerfTelecomLinePostFecCurrent24StatEntry": pm10010ulhPerfTelecomLinePostFecCurrent24StatEntry,
       "pm10010ulhPerfTelecomLinePostFecCurrent24StatIndex": pm10010ulhPerfTelecomLinePostFecCurrent24StatIndex,
       "pm10010ulhPerfTelecomLinePostFecCurrent24StatInvCvPortn": pm10010ulhPerfTelecomLinePostFecCurrent24StatInvCvPortn,
       "pm10010ulhPerfTelecomLinePostFecCurrent24StatCvValuePortn": pm10010ulhPerfTelecomLinePostFecCurrent24StatCvValuePortn,
       "pm10010ulhPerfTelecomLinePostFecCurrent24StatInvEsPortn": pm10010ulhPerfTelecomLinePostFecCurrent24StatInvEsPortn,
       "pm10010ulhPerfTelecomLinePostFecCurrent24StatEsValuePortn": pm10010ulhPerfTelecomLinePostFecCurrent24StatEsValuePortn,
       "pm10010ulhPerfTelecomLinePostFecCurrent24StatInvSesPortn": pm10010ulhPerfTelecomLinePostFecCurrent24StatInvSesPortn,
       "pm10010ulhPerfTelecomLinePostFecCurrent24StatSesValuePortn": pm10010ulhPerfTelecomLinePostFecCurrent24StatSesValuePortn,
       "pm10010ulhPerfTelecomLinePostFecCurrent24StatInvSefsPortn": pm10010ulhPerfTelecomLinePostFecCurrent24StatInvSefsPortn,
       "pm10010ulhPerfTelecomLinePostFecCurrent24StatSefsValuePortn": pm10010ulhPerfTelecomLinePostFecCurrent24StatSefsValuePortn,
       "pm10010ulhPerfTelecomLinePostFecCurrent24StatInvUasPortn": pm10010ulhPerfTelecomLinePostFecCurrent24StatInvUasPortn,
       "pm10010ulhPerfTelecomLinePostFecCurrent24StatUasValuePortn": pm10010ulhPerfTelecomLinePostFecCurrent24StatUasValuePortn,
       "pm10010ulhPerfTelecomLinePostFecPast24StatHistoryPort1Table": pm10010ulhPerfTelecomLinePostFecPast24StatHistoryPort1Table,
       "pm10010ulhPerfTelecomLinePostFecPast24StatHistoryPort1Entry": pm10010ulhPerfTelecomLinePostFecPast24StatHistoryPort1Entry,
       "pm10010ulhPerfTelecomLinePostFecPast24StatHistoryPort1Index": pm10010ulhPerfTelecomLinePostFecPast24StatHistoryPort1Index,
       "pm10010ulhPerfTelecomLinePostFecPast24StatHistoryInvCvPort1": pm10010ulhPerfTelecomLinePostFecPast24StatHistoryInvCvPort1,
       "pm10010ulhPerfTelecomLinePostFecPast24StatHistoryCvValuePort1": pm10010ulhPerfTelecomLinePostFecPast24StatHistoryCvValuePort1,
       "pm10010ulhPerfTelecomLinePostFecPast24StatHistoryInvEsPort1": pm10010ulhPerfTelecomLinePostFecPast24StatHistoryInvEsPort1,
       "pm10010ulhPerfTelecomLinePostFecPast24StatHistoryEsValuePort1": pm10010ulhPerfTelecomLinePostFecPast24StatHistoryEsValuePort1,
       "pm10010ulhPerfTelecomLinePostFecPast24StatHistoryInvSesPort1": pm10010ulhPerfTelecomLinePostFecPast24StatHistoryInvSesPort1,
       "pm10010ulhPerfTelecomLinePostFecPast24StatHistorySesValuePort1": pm10010ulhPerfTelecomLinePostFecPast24StatHistorySesValuePort1,
       "pm10010ulhPerfTelecomLinePostFecPast24StatHistoryInvSefsPort1": pm10010ulhPerfTelecomLinePostFecPast24StatHistoryInvSefsPort1,
       "pm10010ulhPerfTelecomLinePostFecPast24StatHistorySefsValuePort1": pm10010ulhPerfTelecomLinePostFecPast24StatHistorySefsValuePort1,
       "pm10010ulhPerfTelecomLinePostFecPast24StatHistoryInvUasPort1": pm10010ulhPerfTelecomLinePostFecPast24StatHistoryInvUasPort1,
       "pm10010ulhPerfTelecomLinePostFecPast24StatHistoryUasValuePort1": pm10010ulhPerfTelecomLinePostFecPast24StatHistoryUasValuePort1,
       "pm10010ulhPerfTelecomBerLinePreFecCurrent15StatTable": pm10010ulhPerfTelecomBerLinePreFecCurrent15StatTable,
       "pm10010ulhPerfTelecomBerLinePreFecCurrent15StatEntry": pm10010ulhPerfTelecomBerLinePreFecCurrent15StatEntry,
       "pm10010ulhPerfTelecomBerLinePreFecCurrent15StatIndex": pm10010ulhPerfTelecomBerLinePreFecCurrent15StatIndex,
       "pm10010ulhPerfTelecomBerLinePreFecCurrent15StatInvBerPortn": pm10010ulhPerfTelecomBerLinePreFecCurrent15StatInvBerPortn,
       "pm10010ulhPerfTelecomBerLinePreFecCurrent15StatBerValuePortn": pm10010ulhPerfTelecomBerLinePreFecCurrent15StatBerValuePortn,
       "pm10010ulhPerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn": pm10010ulhPerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn,
       "pm10010ulhPerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn": pm10010ulhPerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn,
       "pm10010ulhPerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn": pm10010ulhPerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn,
       "pm10010ulhPerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn": pm10010ulhPerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn,
       "pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryPort1Table": pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryPort1Table,
       "pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryPort1Entry": pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryPort1Entry,
       "pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryPort1Index": pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryPort1Index,
       "pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1": pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1,
       "pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1": pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1,
       "pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1": pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1,
       "pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1": pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1,
       "pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1": pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1,
       "pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1": pm10010ulhPerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1,
       "pm10010ulhPerfTelecomBerLinePreFecCurrent24StatTable": pm10010ulhPerfTelecomBerLinePreFecCurrent24StatTable,
       "pm10010ulhPerfTelecomBerLinePreFecCurrent24StatEntry": pm10010ulhPerfTelecomBerLinePreFecCurrent24StatEntry,
       "pm10010ulhPerfTelecomBerLinePreFecCurrent24StatIndex": pm10010ulhPerfTelecomBerLinePreFecCurrent24StatIndex,
       "pm10010ulhPerfTelecomBerLinePreFecCurrent24StatInvBerPortn": pm10010ulhPerfTelecomBerLinePreFecCurrent24StatInvBerPortn,
       "pm10010ulhPerfTelecomBerLinePreFecCurrent24StatBerValuePortn": pm10010ulhPerfTelecomBerLinePreFecCurrent24StatBerValuePortn,
       "pm10010ulhPerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn": pm10010ulhPerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn,
       "pm10010ulhPerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn": pm10010ulhPerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn,
       "pm10010ulhPerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn": pm10010ulhPerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn,
       "pm10010ulhPerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn": pm10010ulhPerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn,
       "pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryPort1Table": pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryPort1Table,
       "pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryPort1Entry": pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryPort1Entry,
       "pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryPort1Index": pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryPort1Index,
       "pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1": pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1,
       "pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1": pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1,
       "pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1": pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1,
       "pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1": pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1,
       "pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1": pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1,
       "pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1": pm10010ulhPerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1}
)
