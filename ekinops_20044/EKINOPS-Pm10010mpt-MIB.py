# SNMP MIB module (EKINOPS-Pm10010mpt-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ekinops_20044/EKINOPS-Pm10010mpt-MIB.mib
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

modulePm10010mpt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60)
)
if mibBuilder.loadTexts:
    modulePm10010mpt.setRevisions(
        ("2014-02-19 00:00",
         "2014-04-01 00:00",
         "2014-04-03 00:00",
         "2014-10-14 00:00",
         "2015-01-23 00:00",
         "2015-07-30 00:00",
         "2015-10-12 00:00",
         "2015-10-21 00:00",
         "2016-05-02 00:00",
         "2016-05-20 00:00",
         "2016-06-02 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Pm10010mptMultiRate(TextualConvention, Integer32):
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



class Pm10010mptOtxMode(TextualConvention, Integer32):
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



class Pm10010mptOtxGrid(TextualConvention, Integer32):
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



class Pm10010mptAdjustValue(TextualConvention, Integer32):
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



class Pm10010mptClientProtocol(TextualConvention, Integer32):
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



class Pm10010mptProtocolMode(TextualConvention, Integer32):
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



class Pm10010mptOtxChannel(TextualConvention, Integer32):
    status = "current"


class Pm10010mptOrxChannel(TextualConvention, Integer32):
    status = "current"


class Rm10010ClientIgnoreTimer(TextualConvention, Integer32):
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
        *(("ignoretimerclientvalue0", 0),
          ("ignoretimerclientvalue1", 1),
          ("ignoretimerclientvalue2", 2),
          ("ignoretimerclientvalue3", 3),
          ("ignoretimerclientvalue4", 4),
          ("ignoretimerclientvalue5", 5),
          ("ignoretimerclientvalue6", 6),
          ("ignoretimerclientvalue7", 7),
          ("ignoretimerclientvalue8", 8),
          ("ignoretimerclientvalue9", 9),
          ("ignoretimerclientvalue10", 10))
    )



# MIB Managed Objects in the order of their OIDs

_Pm10010mptalarms_ObjectIdentity = ObjectIdentity
pm10010mptalarms = _Pm10010mptalarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2)
)
_Pm10010mptAlmOther_ObjectIdentity = ObjectIdentity
pm10010mptAlmOther = _Pm10010mptAlmOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1)
)
_Pm10010mptAlmOtherNurg_ObjectIdentity = ObjectIdentity
pm10010mptAlmOtherNurg = _Pm10010mptAlmOtherNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 1)
)
_Pm10010mptAlmsynthAlm2_ObjectIdentity = ObjectIdentity
pm10010mptAlmsynthAlm2 = _Pm10010mptAlmsynthAlm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 1, 2)
)
_Pm10010mptAlmConfTableSave_Type = EkiOnOff
_Pm10010mptAlmConfTableSave_Object = MibScalar
pm10010mptAlmConfTableSave = _Pm10010mptAlmConfTableSave_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 1, 2, 1),
    _Pm10010mptAlmConfTableSave_Type()
)
pm10010mptAlmConfTableSave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmConfTableSave.setStatus("current")
_Pm10010mptAlmInvUpload_Type = EkiOnOff
_Pm10010mptAlmInvUpload_Object = MibScalar
pm10010mptAlmInvUpload = _Pm10010mptAlmInvUpload_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 1, 2, 2),
    _Pm10010mptAlmInvUpload_Type()
)
pm10010mptAlmInvUpload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmInvUpload.setStatus("current")
_Pm10010mptAlmConfTableLoad_Type = EkiOnOff
_Pm10010mptAlmConfTableLoad_Object = MibScalar
pm10010mptAlmConfTableLoad = _Pm10010mptAlmConfTableLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 1, 2, 3),
    _Pm10010mptAlmConfTableLoad_Type()
)
pm10010mptAlmConfTableLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmConfTableLoad.setStatus("current")
_Pm10010mptAlmCorrelatOff_Type = EkiOnOff
_Pm10010mptAlmCorrelatOff_Object = MibScalar
pm10010mptAlmCorrelatOff = _Pm10010mptAlmCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 1, 2, 4),
    _Pm10010mptAlmCorrelatOff_Type()
)
pm10010mptAlmCorrelatOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmCorrelatOff.setStatus("current")
_Pm10010mptAlmMaintenanceOn_Type = EkiOnOff
_Pm10010mptAlmMaintenanceOn_Object = MibScalar
pm10010mptAlmMaintenanceOn = _Pm10010mptAlmMaintenanceOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 1, 2, 5),
    _Pm10010mptAlmMaintenanceOn_Type()
)
pm10010mptAlmMaintenanceOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmMaintenanceOn.setStatus("current")
_Pm10010mptAlmOtherUrg_ObjectIdentity = ObjectIdentity
pm10010mptAlmOtherUrg = _Pm10010mptAlmOtherUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 2)
)
_Pm10010mptAlmOtherCrit_ObjectIdentity = ObjectIdentity
pm10010mptAlmOtherCrit = _Pm10010mptAlmOtherCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3)
)
_Pm10010mptAlmsynthAlm0_ObjectIdentity = ObjectIdentity
pm10010mptAlmsynthAlm0 = _Pm10010mptAlmsynthAlm0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 0)
)
_Pm10010mptAlmFailFan_Type = EkiOnOff
_Pm10010mptAlmFailFan_Object = MibScalar
pm10010mptAlmFailFan = _Pm10010mptAlmFailFan_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 0, 2),
    _Pm10010mptAlmFailFan_Type()
)
pm10010mptAlmFailFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmFailFan.setStatus("current")
_Pm10010mptAlmModGlobFail_Type = EkiOnOff
_Pm10010mptAlmModGlobFail_Object = MibScalar
pm10010mptAlmModGlobFail = _Pm10010mptAlmModGlobFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 0, 9),
    _Pm10010mptAlmModGlobFail_Type()
)
pm10010mptAlmModGlobFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmModGlobFail.setStatus("current")
_Pm10010mptAlmDefFuseA_Type = EkiOnOff
_Pm10010mptAlmDefFuseA_Object = MibScalar
pm10010mptAlmDefFuseA = _Pm10010mptAlmDefFuseA_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 0, 15),
    _Pm10010mptAlmDefFuseA_Type()
)
pm10010mptAlmDefFuseA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmDefFuseA.setStatus("current")
_Pm10010mptAlmDefFuseB_Type = EkiOnOff
_Pm10010mptAlmDefFuseB_Object = MibScalar
pm10010mptAlmDefFuseB = _Pm10010mptAlmDefFuseB_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 0, 16),
    _Pm10010mptAlmDefFuseB_Type()
)
pm10010mptAlmDefFuseB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmDefFuseB.setStatus("current")
_Pm10010mptAlmclientModuleState_ObjectIdentity = ObjectIdentity
pm10010mptAlmclientModuleState = _Pm10010mptAlmclientModuleState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 40)
)
_Pm10010mptAlmCfpInitialize_Type = EkiOnOff
_Pm10010mptAlmCfpInitialize_Object = MibScalar
pm10010mptAlmCfpInitialize = _Pm10010mptAlmCfpInitialize_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 40, 1),
    _Pm10010mptAlmCfpInitialize_Type()
)
pm10010mptAlmCfpInitialize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmCfpInitialize.setStatus("current")
_Pm10010mptAlmCfpLowPower_Type = EkiOnOff
_Pm10010mptAlmCfpLowPower_Object = MibScalar
pm10010mptAlmCfpLowPower = _Pm10010mptAlmCfpLowPower_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 40, 2),
    _Pm10010mptAlmCfpLowPower_Type()
)
pm10010mptAlmCfpLowPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmCfpLowPower.setStatus("current")
_Pm10010mptAlmCfpHighPowerUp_Type = EkiOnOff
_Pm10010mptAlmCfpHighPowerUp_Object = MibScalar
pm10010mptAlmCfpHighPowerUp = _Pm10010mptAlmCfpHighPowerUp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 40, 3),
    _Pm10010mptAlmCfpHighPowerUp_Type()
)
pm10010mptAlmCfpHighPowerUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmCfpHighPowerUp.setStatus("current")
_Pm10010mptAlmCfpTxOff_Type = EkiOnOff
_Pm10010mptAlmCfpTxOff_Object = MibScalar
pm10010mptAlmCfpTxOff = _Pm10010mptAlmCfpTxOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 40, 4),
    _Pm10010mptAlmCfpTxOff_Type()
)
pm10010mptAlmCfpTxOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmCfpTxOff.setStatus("current")
_Pm10010mptAlmCfpTxTurnOn_Type = EkiOnOff
_Pm10010mptAlmCfpTxTurnOn_Object = MibScalar
pm10010mptAlmCfpTxTurnOn = _Pm10010mptAlmCfpTxTurnOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 40, 5),
    _Pm10010mptAlmCfpTxTurnOn_Type()
)
pm10010mptAlmCfpTxTurnOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmCfpTxTurnOn.setStatus("current")
_Pm10010mptAlmCfpReady_Type = EkiOnOff
_Pm10010mptAlmCfpReady_Object = MibScalar
pm10010mptAlmCfpReady = _Pm10010mptAlmCfpReady_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 40, 6),
    _Pm10010mptAlmCfpReady_Type()
)
pm10010mptAlmCfpReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmCfpReady.setStatus("current")
_Pm10010mptAlmCfpFault_Type = EkiOnOff
_Pm10010mptAlmCfpFault_Object = MibScalar
pm10010mptAlmCfpFault = _Pm10010mptAlmCfpFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 40, 7),
    _Pm10010mptAlmCfpFault_Type()
)
pm10010mptAlmCfpFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmCfpFault.setStatus("current")
_Pm10010mptAlmCfpTxTurnOff_Type = EkiOnOff
_Pm10010mptAlmCfpTxTurnOff_Object = MibScalar
pm10010mptAlmCfpTxTurnOff = _Pm10010mptAlmCfpTxTurnOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 40, 8),
    _Pm10010mptAlmCfpTxTurnOff_Type()
)
pm10010mptAlmCfpTxTurnOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmCfpTxTurnOff.setStatus("current")
_Pm10010mptAlmCfpHighPowerDown_Type = EkiOnOff
_Pm10010mptAlmCfpHighPowerDown_Object = MibScalar
pm10010mptAlmCfpHighPowerDown = _Pm10010mptAlmCfpHighPowerDown_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 40, 9),
    _Pm10010mptAlmCfpHighPowerDown_Type()
)
pm10010mptAlmCfpHighPowerDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmCfpHighPowerDown.setStatus("current")
_Pm10010mptAlmclientModuleGeneralStatus_ObjectIdentity = ObjectIdentity
pm10010mptAlmclientModuleGeneralStatus = _Pm10010mptAlmclientModuleGeneralStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 41)
)
_Pm10010mptAlmCfpOutOfAlignment_Type = EkiOnOff
_Pm10010mptAlmCfpOutOfAlignment_Object = MibScalar
pm10010mptAlmCfpOutOfAlignment = _Pm10010mptAlmCfpOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 41, 4),
    _Pm10010mptAlmCfpOutOfAlignment_Type()
)
pm10010mptAlmCfpOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmCfpOutOfAlignment.setStatus("current")
_Pm10010mptAlmCfpRxNetworkLol_Type = EkiOnOff
_Pm10010mptAlmCfpRxNetworkLol_Object = MibScalar
pm10010mptAlmCfpRxNetworkLol = _Pm10010mptAlmCfpRxNetworkLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 41, 5),
    _Pm10010mptAlmCfpRxNetworkLol_Type()
)
pm10010mptAlmCfpRxNetworkLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmCfpRxNetworkLol.setStatus("current")
_Pm10010mptAlmCfpRxLos_Type = EkiOnOff
_Pm10010mptAlmCfpRxLos_Object = MibScalar
pm10010mptAlmCfpRxLos = _Pm10010mptAlmCfpRxLos_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 41, 6),
    _Pm10010mptAlmCfpRxLos_Type()
)
pm10010mptAlmCfpRxLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmCfpRxLos.setStatus("current")
_Pm10010mptAlmCfpTxHostLol_Type = EkiOnOff
_Pm10010mptAlmCfpTxHostLol_Object = MibScalar
pm10010mptAlmCfpTxHostLol = _Pm10010mptAlmCfpTxHostLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 41, 7),
    _Pm10010mptAlmCfpTxHostLol_Type()
)
pm10010mptAlmCfpTxHostLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmCfpTxHostLol.setStatus("current")
_Pm10010mptAlmCfpTxLosf_Type = EkiOnOff
_Pm10010mptAlmCfpTxLosf_Object = MibScalar
pm10010mptAlmCfpTxLosf = _Pm10010mptAlmCfpTxLosf_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 41, 8),
    _Pm10010mptAlmCfpTxLosf_Type()
)
pm10010mptAlmCfpTxLosf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmCfpTxLosf.setStatus("current")
_Pm10010mptAlmCfpTxCmuLol_Type = EkiOnOff
_Pm10010mptAlmCfpTxCmuLol_Object = MibScalar
pm10010mptAlmCfpTxCmuLol = _Pm10010mptAlmCfpTxCmuLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 41, 9),
    _Pm10010mptAlmCfpTxCmuLol_Type()
)
pm10010mptAlmCfpTxCmuLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmCfpTxCmuLol.setStatus("current")
_Pm10010mptAlmCfpTxJitterPllLol_Type = EkiOnOff
_Pm10010mptAlmCfpTxJitterPllLol_Object = MibScalar
pm10010mptAlmCfpTxJitterPllLol = _Pm10010mptAlmCfpTxJitterPllLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 41, 10),
    _Pm10010mptAlmCfpTxJitterPllLol_Type()
)
pm10010mptAlmCfpTxJitterPllLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmCfpTxJitterPllLol.setStatus("current")
_Pm10010mptAlmCfpLossOfRefclk_Type = EkiOnOff
_Pm10010mptAlmCfpLossOfRefclk_Object = MibScalar
pm10010mptAlmCfpLossOfRefclk = _Pm10010mptAlmCfpLossOfRefclk_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 41, 11),
    _Pm10010mptAlmCfpLossOfRefclk_Type()
)
pm10010mptAlmCfpLossOfRefclk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmCfpLossOfRefclk.setStatus("current")
_Pm10010mptAlmCfpHwInterlock_Type = EkiOnOff
_Pm10010mptAlmCfpHwInterlock_Object = MibScalar
pm10010mptAlmCfpHwInterlock = _Pm10010mptAlmCfpHwInterlock_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 41, 14),
    _Pm10010mptAlmCfpHwInterlock_Type()
)
pm10010mptAlmCfpHwInterlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmCfpHwInterlock.setStatus("current")
_Pm10010mptAlmclientGlobalAlarmSummary_ObjectIdentity = ObjectIdentity
pm10010mptAlmclientGlobalAlarmSummary = _Pm10010mptAlmclientGlobalAlarmSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 42)
)
_Pm10010mptAlmCfpSoftGlobAlarmTest_Type = EkiOnOff
_Pm10010mptAlmCfpSoftGlobAlarmTest_Object = MibScalar
pm10010mptAlmCfpSoftGlobAlarmTest = _Pm10010mptAlmCfpSoftGlobAlarmTest_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 42, 1),
    _Pm10010mptAlmCfpSoftGlobAlarmTest_Type()
)
pm10010mptAlmCfpSoftGlobAlarmTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmCfpSoftGlobAlarmTest.setStatus("current")
_Pm10010mptAlmCfpNetworkLaneAlarmWarning2_Type = EkiOnOff
_Pm10010mptAlmCfpNetworkLaneAlarmWarning2_Object = MibScalar
pm10010mptAlmCfpNetworkLaneAlarmWarning2 = _Pm10010mptAlmCfpNetworkLaneAlarmWarning2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 42, 7),
    _Pm10010mptAlmCfpNetworkLaneAlarmWarning2_Type()
)
pm10010mptAlmCfpNetworkLaneAlarmWarning2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmCfpNetworkLaneAlarmWarning2.setStatus("current")
_Pm10010mptAlmCfpModuleState_Type = EkiOnOff
_Pm10010mptAlmCfpModuleState_Object = MibScalar
pm10010mptAlmCfpModuleState = _Pm10010mptAlmCfpModuleState_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 42, 8),
    _Pm10010mptAlmCfpModuleState_Type()
)
pm10010mptAlmCfpModuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmCfpModuleState.setStatus("current")
_Pm10010mptAlmCfpModuleGeneralStatus_Type = EkiOnOff
_Pm10010mptAlmCfpModuleGeneralStatus_Object = MibScalar
pm10010mptAlmCfpModuleGeneralStatus = _Pm10010mptAlmCfpModuleGeneralStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 42, 9),
    _Pm10010mptAlmCfpModuleGeneralStatus_Type()
)
pm10010mptAlmCfpModuleGeneralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmCfpModuleGeneralStatus.setStatus("current")
_Pm10010mptAlmCfpModuleFault_Type = EkiOnOff
_Pm10010mptAlmCfpModuleFault_Object = MibScalar
pm10010mptAlmCfpModuleFault = _Pm10010mptAlmCfpModuleFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 42, 10),
    _Pm10010mptAlmCfpModuleFault_Type()
)
pm10010mptAlmCfpModuleFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmCfpModuleFault.setStatus("current")
_Pm10010mptAlmCfpModuleAlarmWarning1_Type = EkiOnOff
_Pm10010mptAlmCfpModuleAlarmWarning1_Object = MibScalar
pm10010mptAlmCfpModuleAlarmWarning1 = _Pm10010mptAlmCfpModuleAlarmWarning1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 42, 11),
    _Pm10010mptAlmCfpModuleAlarmWarning1_Type()
)
pm10010mptAlmCfpModuleAlarmWarning1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmCfpModuleAlarmWarning1.setStatus("current")
_Pm10010mptAlmCfpModuleAlarmWarning2_Type = EkiOnOff
_Pm10010mptAlmCfpModuleAlarmWarning2_Object = MibScalar
pm10010mptAlmCfpModuleAlarmWarning2 = _Pm10010mptAlmCfpModuleAlarmWarning2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 42, 12),
    _Pm10010mptAlmCfpModuleAlarmWarning2_Type()
)
pm10010mptAlmCfpModuleAlarmWarning2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmCfpModuleAlarmWarning2.setStatus("current")
_Pm10010mptAlmCfpNetworkLaneAlarmWarning1_Type = EkiOnOff
_Pm10010mptAlmCfpNetworkLaneAlarmWarning1_Object = MibScalar
pm10010mptAlmCfpNetworkLaneAlarmWarning1 = _Pm10010mptAlmCfpNetworkLaneAlarmWarning1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 42, 13),
    _Pm10010mptAlmCfpNetworkLaneAlarmWarning1_Type()
)
pm10010mptAlmCfpNetworkLaneAlarmWarning1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmCfpNetworkLaneAlarmWarning1.setStatus("current")
_Pm10010mptAlmCfpNetworkLaneFaultStatus_Type = EkiOnOff
_Pm10010mptAlmCfpNetworkLaneFaultStatus_Object = MibScalar
pm10010mptAlmCfpNetworkLaneFaultStatus = _Pm10010mptAlmCfpNetworkLaneFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 42, 14),
    _Pm10010mptAlmCfpNetworkLaneFaultStatus_Type()
)
pm10010mptAlmCfpNetworkLaneFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmCfpNetworkLaneFaultStatus.setStatus("current")
_Pm10010mptAlmCfpHostLaneFaultStatus_Type = EkiOnOff
_Pm10010mptAlmCfpHostLaneFaultStatus_Object = MibScalar
pm10010mptAlmCfpHostLaneFaultStatus = _Pm10010mptAlmCfpHostLaneFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 42, 15),
    _Pm10010mptAlmCfpHostLaneFaultStatus_Type()
)
pm10010mptAlmCfpHostLaneFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmCfpHostLaneFaultStatus.setStatus("current")
_Pm10010mptAlmCfpGlobAlarmAssertion_Type = EkiOnOff
_Pm10010mptAlmCfpGlobAlarmAssertion_Object = MibScalar
pm10010mptAlmCfpGlobAlarmAssertion = _Pm10010mptAlmCfpGlobAlarmAssertion_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 42, 16),
    _Pm10010mptAlmCfpGlobAlarmAssertion_Type()
)
pm10010mptAlmCfpGlobAlarmAssertion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmCfpGlobAlarmAssertion.setStatus("current")
_Pm10010mptAlmmsaModuleState_ObjectIdentity = ObjectIdentity
pm10010mptAlmmsaModuleState = _Pm10010mptAlmmsaModuleState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 46)
)
_Pm10010mptAlmMsaInitialize_Type = EkiOnOff
_Pm10010mptAlmMsaInitialize_Object = MibScalar
pm10010mptAlmMsaInitialize = _Pm10010mptAlmMsaInitialize_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 46, 1),
    _Pm10010mptAlmMsaInitialize_Type()
)
pm10010mptAlmMsaInitialize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmMsaInitialize.setStatus("current")
_Pm10010mptAlmMsaLowPower_Type = EkiOnOff
_Pm10010mptAlmMsaLowPower_Object = MibScalar
pm10010mptAlmMsaLowPower = _Pm10010mptAlmMsaLowPower_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 46, 2),
    _Pm10010mptAlmMsaLowPower_Type()
)
pm10010mptAlmMsaLowPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmMsaLowPower.setStatus("current")
_Pm10010mptAlmMsaHighPowerUp_Type = EkiOnOff
_Pm10010mptAlmMsaHighPowerUp_Object = MibScalar
pm10010mptAlmMsaHighPowerUp = _Pm10010mptAlmMsaHighPowerUp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 46, 3),
    _Pm10010mptAlmMsaHighPowerUp_Type()
)
pm10010mptAlmMsaHighPowerUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmMsaHighPowerUp.setStatus("current")
_Pm10010mptAlmMsaTxOff_Type = EkiOnOff
_Pm10010mptAlmMsaTxOff_Object = MibScalar
pm10010mptAlmMsaTxOff = _Pm10010mptAlmMsaTxOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 46, 4),
    _Pm10010mptAlmMsaTxOff_Type()
)
pm10010mptAlmMsaTxOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmMsaTxOff.setStatus("current")
_Pm10010mptAlmMsaTxTurnOn_Type = EkiOnOff
_Pm10010mptAlmMsaTxTurnOn_Object = MibScalar
pm10010mptAlmMsaTxTurnOn = _Pm10010mptAlmMsaTxTurnOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 46, 5),
    _Pm10010mptAlmMsaTxTurnOn_Type()
)
pm10010mptAlmMsaTxTurnOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmMsaTxTurnOn.setStatus("current")
_Pm10010mptAlmMsaReady_Type = EkiOnOff
_Pm10010mptAlmMsaReady_Object = MibScalar
pm10010mptAlmMsaReady = _Pm10010mptAlmMsaReady_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 46, 6),
    _Pm10010mptAlmMsaReady_Type()
)
pm10010mptAlmMsaReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmMsaReady.setStatus("current")
_Pm10010mptAlmMsaFault_Type = EkiOnOff
_Pm10010mptAlmMsaFault_Object = MibScalar
pm10010mptAlmMsaFault = _Pm10010mptAlmMsaFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 46, 7),
    _Pm10010mptAlmMsaFault_Type()
)
pm10010mptAlmMsaFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmMsaFault.setStatus("current")
_Pm10010mptAlmMsaTxTurnOff_Type = EkiOnOff
_Pm10010mptAlmMsaTxTurnOff_Object = MibScalar
pm10010mptAlmMsaTxTurnOff = _Pm10010mptAlmMsaTxTurnOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 46, 8),
    _Pm10010mptAlmMsaTxTurnOff_Type()
)
pm10010mptAlmMsaTxTurnOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmMsaTxTurnOff.setStatus("current")
_Pm10010mptAlmMsaHighPowerDown_Type = EkiOnOff
_Pm10010mptAlmMsaHighPowerDown_Object = MibScalar
pm10010mptAlmMsaHighPowerDown = _Pm10010mptAlmMsaHighPowerDown_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 46, 9),
    _Pm10010mptAlmMsaHighPowerDown_Type()
)
pm10010mptAlmMsaHighPowerDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmMsaHighPowerDown.setStatus("current")
_Pm10010mptAlmmsaModuleGeneralStatus_ObjectIdentity = ObjectIdentity
pm10010mptAlmmsaModuleGeneralStatus = _Pm10010mptAlmmsaModuleGeneralStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 47)
)
_Pm10010mptAlmMsaOutOfAlignment_Type = EkiOnOff
_Pm10010mptAlmMsaOutOfAlignment_Object = MibScalar
pm10010mptAlmMsaOutOfAlignment = _Pm10010mptAlmMsaOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 47, 4),
    _Pm10010mptAlmMsaOutOfAlignment_Type()
)
pm10010mptAlmMsaOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmMsaOutOfAlignment.setStatus("current")
_Pm10010mptAlmMsaRxNetworkLol_Type = EkiOnOff
_Pm10010mptAlmMsaRxNetworkLol_Object = MibScalar
pm10010mptAlmMsaRxNetworkLol = _Pm10010mptAlmMsaRxNetworkLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 47, 5),
    _Pm10010mptAlmMsaRxNetworkLol_Type()
)
pm10010mptAlmMsaRxNetworkLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmMsaRxNetworkLol.setStatus("current")
_Pm10010mptAlmMsaRxLos_Type = EkiOnOff
_Pm10010mptAlmMsaRxLos_Object = MibScalar
pm10010mptAlmMsaRxLos = _Pm10010mptAlmMsaRxLos_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 47, 6),
    _Pm10010mptAlmMsaRxLos_Type()
)
pm10010mptAlmMsaRxLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmMsaRxLos.setStatus("current")
_Pm10010mptAlmMsaTxHostLol_Type = EkiOnOff
_Pm10010mptAlmMsaTxHostLol_Object = MibScalar
pm10010mptAlmMsaTxHostLol = _Pm10010mptAlmMsaTxHostLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 47, 7),
    _Pm10010mptAlmMsaTxHostLol_Type()
)
pm10010mptAlmMsaTxHostLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmMsaTxHostLol.setStatus("current")
_Pm10010mptAlmMsaTxLosf_Type = EkiOnOff
_Pm10010mptAlmMsaTxLosf_Object = MibScalar
pm10010mptAlmMsaTxLosf = _Pm10010mptAlmMsaTxLosf_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 47, 8),
    _Pm10010mptAlmMsaTxLosf_Type()
)
pm10010mptAlmMsaTxLosf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmMsaTxLosf.setStatus("current")
_Pm10010mptAlmMsaTxCmuLol_Type = EkiOnOff
_Pm10010mptAlmMsaTxCmuLol_Object = MibScalar
pm10010mptAlmMsaTxCmuLol = _Pm10010mptAlmMsaTxCmuLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 47, 9),
    _Pm10010mptAlmMsaTxCmuLol_Type()
)
pm10010mptAlmMsaTxCmuLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmMsaTxCmuLol.setStatus("current")
_Pm10010mptAlmMsaTxJitterPllLol_Type = EkiOnOff
_Pm10010mptAlmMsaTxJitterPllLol_Object = MibScalar
pm10010mptAlmMsaTxJitterPllLol = _Pm10010mptAlmMsaTxJitterPllLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 47, 10),
    _Pm10010mptAlmMsaTxJitterPllLol_Type()
)
pm10010mptAlmMsaTxJitterPllLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmMsaTxJitterPllLol.setStatus("current")
_Pm10010mptAlmMsaLossOfRefclk_Type = EkiOnOff
_Pm10010mptAlmMsaLossOfRefclk_Object = MibScalar
pm10010mptAlmMsaLossOfRefclk = _Pm10010mptAlmMsaLossOfRefclk_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 47, 11),
    _Pm10010mptAlmMsaLossOfRefclk_Type()
)
pm10010mptAlmMsaLossOfRefclk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmMsaLossOfRefclk.setStatus("current")
_Pm10010mptAlmMsaHwInterlock_Type = EkiOnOff
_Pm10010mptAlmMsaHwInterlock_Object = MibScalar
pm10010mptAlmMsaHwInterlock = _Pm10010mptAlmMsaHwInterlock_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 47, 14),
    _Pm10010mptAlmMsaHwInterlock_Type()
)
pm10010mptAlmMsaHwInterlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmMsaHwInterlock.setStatus("current")
_Pm10010mptAlmmsaGlobalAlarmSummary_ObjectIdentity = ObjectIdentity
pm10010mptAlmmsaGlobalAlarmSummary = _Pm10010mptAlmmsaGlobalAlarmSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 48)
)
_Pm10010mptAlmMsaSoftGlobAlarmTest_Type = EkiOnOff
_Pm10010mptAlmMsaSoftGlobAlarmTest_Object = MibScalar
pm10010mptAlmMsaSoftGlobAlarmTest = _Pm10010mptAlmMsaSoftGlobAlarmTest_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 48, 1),
    _Pm10010mptAlmMsaSoftGlobAlarmTest_Type()
)
pm10010mptAlmMsaSoftGlobAlarmTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmMsaSoftGlobAlarmTest.setStatus("current")
_Pm10010mptAlmMsaNetworkHostAlarmStatus_Type = EkiOnOff
_Pm10010mptAlmMsaNetworkHostAlarmStatus_Object = MibScalar
pm10010mptAlmMsaNetworkHostAlarmStatus = _Pm10010mptAlmMsaNetworkHostAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 48, 6),
    _Pm10010mptAlmMsaNetworkHostAlarmStatus_Type()
)
pm10010mptAlmMsaNetworkHostAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmMsaNetworkHostAlarmStatus.setStatus("current")
_Pm10010mptAlmMsaNetworkLaneAlarmWarning2_Type = EkiOnOff
_Pm10010mptAlmMsaNetworkLaneAlarmWarning2_Object = MibScalar
pm10010mptAlmMsaNetworkLaneAlarmWarning2 = _Pm10010mptAlmMsaNetworkLaneAlarmWarning2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 48, 7),
    _Pm10010mptAlmMsaNetworkLaneAlarmWarning2_Type()
)
pm10010mptAlmMsaNetworkLaneAlarmWarning2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmMsaNetworkLaneAlarmWarning2.setStatus("current")
_Pm10010mptAlmMsaModuleState_Type = EkiOnOff
_Pm10010mptAlmMsaModuleState_Object = MibScalar
pm10010mptAlmMsaModuleState = _Pm10010mptAlmMsaModuleState_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 48, 8),
    _Pm10010mptAlmMsaModuleState_Type()
)
pm10010mptAlmMsaModuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmMsaModuleState.setStatus("current")
_Pm10010mptAlmMsaModuleGeneralStatus_Type = EkiOnOff
_Pm10010mptAlmMsaModuleGeneralStatus_Object = MibScalar
pm10010mptAlmMsaModuleGeneralStatus = _Pm10010mptAlmMsaModuleGeneralStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 48, 9),
    _Pm10010mptAlmMsaModuleGeneralStatus_Type()
)
pm10010mptAlmMsaModuleGeneralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmMsaModuleGeneralStatus.setStatus("current")
_Pm10010mptAlmModuleFault_Type = EkiOnOff
_Pm10010mptAlmModuleFault_Object = MibScalar
pm10010mptAlmModuleFault = _Pm10010mptAlmModuleFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 48, 10),
    _Pm10010mptAlmModuleFault_Type()
)
pm10010mptAlmModuleFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmModuleFault.setStatus("current")
_Pm10010mptAlmMsaModuleAlarmWarning1_Type = EkiOnOff
_Pm10010mptAlmMsaModuleAlarmWarning1_Object = MibScalar
pm10010mptAlmMsaModuleAlarmWarning1 = _Pm10010mptAlmMsaModuleAlarmWarning1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 48, 11),
    _Pm10010mptAlmMsaModuleAlarmWarning1_Type()
)
pm10010mptAlmMsaModuleAlarmWarning1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmMsaModuleAlarmWarning1.setStatus("current")
_Pm10010mptAlmMsaModuleAlarmWarning2_Type = EkiOnOff
_Pm10010mptAlmMsaModuleAlarmWarning2_Object = MibScalar
pm10010mptAlmMsaModuleAlarmWarning2 = _Pm10010mptAlmMsaModuleAlarmWarning2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 48, 12),
    _Pm10010mptAlmMsaModuleAlarmWarning2_Type()
)
pm10010mptAlmMsaModuleAlarmWarning2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmMsaModuleAlarmWarning2.setStatus("current")
_Pm10010mptAlmMsaNetworkLaneAlarmWarning1_Type = EkiOnOff
_Pm10010mptAlmMsaNetworkLaneAlarmWarning1_Object = MibScalar
pm10010mptAlmMsaNetworkLaneAlarmWarning1 = _Pm10010mptAlmMsaNetworkLaneAlarmWarning1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 48, 13),
    _Pm10010mptAlmMsaNetworkLaneAlarmWarning1_Type()
)
pm10010mptAlmMsaNetworkLaneAlarmWarning1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmMsaNetworkLaneAlarmWarning1.setStatus("current")
_Pm10010mptAlmMsaNetworkLaneFaultStatus_Type = EkiOnOff
_Pm10010mptAlmMsaNetworkLaneFaultStatus_Object = MibScalar
pm10010mptAlmMsaNetworkLaneFaultStatus = _Pm10010mptAlmMsaNetworkLaneFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 48, 14),
    _Pm10010mptAlmMsaNetworkLaneFaultStatus_Type()
)
pm10010mptAlmMsaNetworkLaneFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmMsaNetworkLaneFaultStatus.setStatus("current")
_Pm10010mptAlmMsaHostLaneFaultStatus_Type = EkiOnOff
_Pm10010mptAlmMsaHostLaneFaultStatus_Object = MibScalar
pm10010mptAlmMsaHostLaneFaultStatus = _Pm10010mptAlmMsaHostLaneFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 48, 15),
    _Pm10010mptAlmMsaHostLaneFaultStatus_Type()
)
pm10010mptAlmMsaHostLaneFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmMsaHostLaneFaultStatus.setStatus("current")
_Pm10010mptAlmMsaGlobAlarmAssertion_Type = EkiOnOff
_Pm10010mptAlmMsaGlobAlarmAssertion_Object = MibScalar
pm10010mptAlmMsaGlobAlarmAssertion = _Pm10010mptAlmMsaGlobAlarmAssertion_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 48, 16),
    _Pm10010mptAlmMsaGlobAlarmAssertion_Type()
)
pm10010mptAlmMsaGlobAlarmAssertion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmMsaGlobAlarmAssertion.setStatus("current")
_Pm10010mptAlmmsaNetworkTxAlignment_ObjectIdentity = ObjectIdentity
pm10010mptAlmmsaNetworkTxAlignment = _Pm10010mptAlmmsaNetworkTxAlignment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 49)
)
_Pm10010mptAlmNetTxTimingFault_Type = EkiOnOff
_Pm10010mptAlmNetTxTimingFault_Object = MibScalar
pm10010mptAlmNetTxTimingFault = _Pm10010mptAlmNetTxTimingFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 49, 12),
    _Pm10010mptAlmNetTxTimingFault_Type()
)
pm10010mptAlmNetTxTimingFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmNetTxTimingFault.setStatus("current")
_Pm10010mptAlmNetTxReferenceClockFault_Type = EkiOnOff
_Pm10010mptAlmNetTxReferenceClockFault_Object = MibScalar
pm10010mptAlmNetTxReferenceClockFault = _Pm10010mptAlmNetTxReferenceClockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 49, 13),
    _Pm10010mptAlmNetTxReferenceClockFault_Type()
)
pm10010mptAlmNetTxReferenceClockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmNetTxReferenceClockFault.setStatus("current")
_Pm10010mptAlmNetTxCmuLockFault_Type = EkiOnOff
_Pm10010mptAlmNetTxCmuLockFault_Object = MibScalar
pm10010mptAlmNetTxCmuLockFault = _Pm10010mptAlmNetTxCmuLockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 49, 14),
    _Pm10010mptAlmNetTxCmuLockFault_Type()
)
pm10010mptAlmNetTxCmuLockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmNetTxCmuLockFault.setStatus("current")
_Pm10010mptAlmNetTxOutOfAlignment_Type = EkiOnOff
_Pm10010mptAlmNetTxOutOfAlignment_Object = MibScalar
pm10010mptAlmNetTxOutOfAlignment = _Pm10010mptAlmNetTxOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 49, 15),
    _Pm10010mptAlmNetTxOutOfAlignment_Type()
)
pm10010mptAlmNetTxOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmNetTxOutOfAlignment.setStatus("current")
_Pm10010mptAlmNetTxLossOfAlignment_Type = EkiOnOff
_Pm10010mptAlmNetTxLossOfAlignment_Object = MibScalar
pm10010mptAlmNetTxLossOfAlignment = _Pm10010mptAlmNetTxLossOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 49, 16),
    _Pm10010mptAlmNetTxLossOfAlignment_Type()
)
pm10010mptAlmNetTxLossOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmNetTxLossOfAlignment.setStatus("current")
_Pm10010mptAlmmsaNetworkRxAlignment_ObjectIdentity = ObjectIdentity
pm10010mptAlmmsaNetworkRxAlignment = _Pm10010mptAlmmsaNetworkRxAlignment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 50)
)
_Pm10010mptAlmNetRxTimingFault_Type = EkiOnOff
_Pm10010mptAlmNetRxTimingFault_Object = MibScalar
pm10010mptAlmNetRxTimingFault = _Pm10010mptAlmNetRxTimingFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 50, 12),
    _Pm10010mptAlmNetRxTimingFault_Type()
)
pm10010mptAlmNetRxTimingFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmNetRxTimingFault.setStatus("current")
_Pm10010mptAlmNetRxOutOfAlignment_Type = EkiOnOff
_Pm10010mptAlmNetRxOutOfAlignment_Object = MibScalar
pm10010mptAlmNetRxOutOfAlignment = _Pm10010mptAlmNetRxOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 50, 13),
    _Pm10010mptAlmNetRxOutOfAlignment_Type()
)
pm10010mptAlmNetRxOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmNetRxOutOfAlignment.setStatus("current")
_Pm10010mptAlmNetRxLossOfAlignment_Type = EkiOnOff
_Pm10010mptAlmNetRxLossOfAlignment_Object = MibScalar
pm10010mptAlmNetRxLossOfAlignment = _Pm10010mptAlmNetRxLossOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 50, 14),
    _Pm10010mptAlmNetRxLossOfAlignment_Type()
)
pm10010mptAlmNetRxLossOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmNetRxLossOfAlignment.setStatus("current")
_Pm10010mptAlmNetRxModemLockFault_Type = EkiOnOff
_Pm10010mptAlmNetRxModemLockFault_Object = MibScalar
pm10010mptAlmNetRxModemLockFault = _Pm10010mptAlmNetRxModemLockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 50, 15),
    _Pm10010mptAlmNetRxModemLockFault_Type()
)
pm10010mptAlmNetRxModemLockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmNetRxModemLockFault.setStatus("current")
_Pm10010mptAlmNetRxModemSyncDetectFault_Type = EkiOnOff
_Pm10010mptAlmNetRxModemSyncDetectFault_Object = MibScalar
pm10010mptAlmNetRxModemSyncDetectFault = _Pm10010mptAlmNetRxModemSyncDetectFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 50, 16),
    _Pm10010mptAlmNetRxModemSyncDetectFault_Type()
)
pm10010mptAlmNetRxModemSyncDetectFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmNetRxModemSyncDetectFault.setStatus("current")
_Pm10010mptAlmmsaNetworkHostNetworkAlarmSummary_ObjectIdentity = ObjectIdentity
pm10010mptAlmmsaNetworkHostNetworkAlarmSummary = _Pm10010mptAlmmsaNetworkHostNetworkAlarmSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 51)
)
_Pm10010mptAlmNetworkTxAlignment_Type = EkiOnOff
_Pm10010mptAlmNetworkTxAlignment_Object = MibScalar
pm10010mptAlmNetworkTxAlignment = _Pm10010mptAlmNetworkTxAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 51, 11),
    _Pm10010mptAlmNetworkTxAlignment_Type()
)
pm10010mptAlmNetworkTxAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmNetworkTxAlignment.setStatus("current")
_Pm10010mptAlmNetworkRxAlignment_Type = EkiOnOff
_Pm10010mptAlmNetworkRxAlignment_Object = MibScalar
pm10010mptAlmNetworkRxAlignment = _Pm10010mptAlmNetworkRxAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 51, 12),
    _Pm10010mptAlmNetworkRxAlignment_Type()
)
pm10010mptAlmNetworkRxAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmNetworkRxAlignment.setStatus("current")
_Pm10010mptAlmNetworkRxOtn_Type = EkiOnOff
_Pm10010mptAlmNetworkRxOtn_Object = MibScalar
pm10010mptAlmNetworkRxOtn = _Pm10010mptAlmNetworkRxOtn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 51, 13),
    _Pm10010mptAlmNetworkRxOtn_Type()
)
pm10010mptAlmNetworkRxOtn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmNetworkRxOtn.setStatus("current")
_Pm10010mptAlmHostRxAlignment_Type = EkiOnOff
_Pm10010mptAlmHostRxAlignment_Object = MibScalar
pm10010mptAlmHostRxAlignment = _Pm10010mptAlmHostRxAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 51, 14),
    _Pm10010mptAlmHostRxAlignment_Type()
)
pm10010mptAlmHostRxAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmHostRxAlignment.setStatus("current")
_Pm10010mptAlmHostTxAlignment_Type = EkiOnOff
_Pm10010mptAlmHostTxAlignment_Object = MibScalar
pm10010mptAlmHostTxAlignment = _Pm10010mptAlmHostTxAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 51, 15),
    _Pm10010mptAlmHostTxAlignment_Type()
)
pm10010mptAlmHostTxAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmHostTxAlignment.setStatus("current")
_Pm10010mptAlmHostTxOtnStatus_Type = EkiOnOff
_Pm10010mptAlmHostTxOtnStatus_Object = MibScalar
pm10010mptAlmHostTxOtnStatus = _Pm10010mptAlmHostTxOtnStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 51, 16),
    _Pm10010mptAlmHostTxOtnStatus_Type()
)
pm10010mptAlmHostTxOtnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmHostTxOtnStatus.setStatus("current")
_Pm10010mptAlmmsaHostTxAlignment_ObjectIdentity = ObjectIdentity
pm10010mptAlmmsaHostTxAlignment = _Pm10010mptAlmmsaHostTxAlignment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 52)
)
_Pm10010mptAlmHostTxDeskewLockFault_Type = EkiOnOff
_Pm10010mptAlmHostTxDeskewLockFault_Object = MibScalar
pm10010mptAlmHostTxDeskewLockFault = _Pm10010mptAlmHostTxDeskewLockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 52, 13),
    _Pm10010mptAlmHostTxDeskewLockFault_Type()
)
pm10010mptAlmHostTxDeskewLockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmHostTxDeskewLockFault.setStatus("current")
_Pm10010mptAlmHostTxOutOfAlignment_Type = EkiOnOff
_Pm10010mptAlmHostTxOutOfAlignment_Object = MibScalar
pm10010mptAlmHostTxOutOfAlignment = _Pm10010mptAlmHostTxOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 52, 14),
    _Pm10010mptAlmHostTxOutOfAlignment_Type()
)
pm10010mptAlmHostTxOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmHostTxOutOfAlignment.setStatus("current")
_Pm10010mptAlmHostTxLossOfAlignment_Type = EkiOnOff
_Pm10010mptAlmHostTxLossOfAlignment_Object = MibScalar
pm10010mptAlmHostTxLossOfAlignment = _Pm10010mptAlmHostTxLossOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 52, 15),
    _Pm10010mptAlmHostTxLossOfAlignment_Type()
)
pm10010mptAlmHostTxLossOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmHostTxLossOfAlignment.setStatus("current")
_Pm10010mptAlmHostTxCdrLockFault_Type = EkiOnOff
_Pm10010mptAlmHostTxCdrLockFault_Object = MibScalar
pm10010mptAlmHostTxCdrLockFault = _Pm10010mptAlmHostTxCdrLockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 52, 16),
    _Pm10010mptAlmHostTxCdrLockFault_Type()
)
pm10010mptAlmHostTxCdrLockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmHostTxCdrLockFault.setStatus("current")
_Pm10010mptAlmmsaHostRxAlignment_ObjectIdentity = ObjectIdentity
pm10010mptAlmmsaHostRxAlignment = _Pm10010mptAlmmsaHostRxAlignment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 53)
)
_Pm10010mptAlmHostRxCmuLockFault_Type = EkiOnOff
_Pm10010mptAlmHostRxCmuLockFault_Object = MibScalar
pm10010mptAlmHostRxCmuLockFault = _Pm10010mptAlmHostRxCmuLockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 53, 14),
    _Pm10010mptAlmHostRxCmuLockFault_Type()
)
pm10010mptAlmHostRxCmuLockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmHostRxCmuLockFault.setStatus("current")
_Pm10010mptAlmHostRxOutOfAlignment_Type = EkiOnOff
_Pm10010mptAlmHostRxOutOfAlignment_Object = MibScalar
pm10010mptAlmHostRxOutOfAlignment = _Pm10010mptAlmHostRxOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 53, 15),
    _Pm10010mptAlmHostRxOutOfAlignment_Type()
)
pm10010mptAlmHostRxOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmHostRxOutOfAlignment.setStatus("current")
_Pm10010mptAlmHostRxLossOfAlignment_Type = EkiOnOff
_Pm10010mptAlmHostRxLossOfAlignment_Object = MibScalar
pm10010mptAlmHostRxLossOfAlignment = _Pm10010mptAlmHostRxLossOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 1, 3, 53, 16),
    _Pm10010mptAlmHostRxLossOfAlignment_Type()
)
pm10010mptAlmHostRxLossOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmHostRxLossOfAlignment.setStatus("current")
_Pm10010mptAlmClient_ObjectIdentity = ObjectIdentity
pm10010mptAlmClient = _Pm10010mptAlmClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2)
)
_Pm10010mptAlmClientNurg_ObjectIdentity = ObjectIdentity
pm10010mptAlmClientNurg = _Pm10010mptAlmClientNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 1)
)
_Pm10010mptAlmclientNetworkLaneAlarmWarningTable_Object = MibTable
pm10010mptAlmclientNetworkLaneAlarmWarningTable = _Pm10010mptAlmclientNetworkLaneAlarmWarningTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 1, 56)
)
if mibBuilder.loadTexts:
    pm10010mptAlmclientNetworkLaneAlarmWarningTable.setStatus("current")
_Pm10010mptAlmclientNetworkLaneAlarmWarningEntry_Object = MibTableRow
pm10010mptAlmclientNetworkLaneAlarmWarningEntry = _Pm10010mptAlmclientNetworkLaneAlarmWarningEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 1, 56, 1)
)
pm10010mptAlmclientNetworkLaneAlarmWarningEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptAlmclientNetworkLaneAlarmWarningIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptAlmclientNetworkLaneAlarmWarningEntry.setStatus("current")


class _Pm10010mptAlmclientNetworkLaneAlarmWarningIndex_Type(Integer32):
    """Custom type pm10010mptAlmclientNetworkLaneAlarmWarningIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptAlmclientNetworkLaneAlarmWarningIndex_Type.__name__ = "Integer32"
_Pm10010mptAlmclientNetworkLaneAlarmWarningIndex_Object = MibTableColumn
pm10010mptAlmclientNetworkLaneAlarmWarningIndex = _Pm10010mptAlmclientNetworkLaneAlarmWarningIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 1, 56, 1, 1),
    _Pm10010mptAlmclientNetworkLaneAlarmWarningIndex_Type()
)
pm10010mptAlmclientNetworkLaneAlarmWarningIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmclientNetworkLaneAlarmWarningIndex.setStatus("current")
_Pm10010mptAlmClientRxPowerLowAlarmPortn_Type = EkiOnOff
_Pm10010mptAlmClientRxPowerLowAlarmPortn_Object = MibTableColumn
pm10010mptAlmClientRxPowerLowAlarmPortn = _Pm10010mptAlmClientRxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 1, 56, 1, 2),
    _Pm10010mptAlmClientRxPowerLowAlarmPortn_Type()
)
pm10010mptAlmClientRxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmClientRxPowerLowAlarmPortn.setStatus("current")
_Pm10010mptAlmClientRxPowerLowWarningPortn_Type = EkiOnOff
_Pm10010mptAlmClientRxPowerLowWarningPortn_Object = MibTableColumn
pm10010mptAlmClientRxPowerLowWarningPortn = _Pm10010mptAlmClientRxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 1, 56, 1, 3),
    _Pm10010mptAlmClientRxPowerLowWarningPortn_Type()
)
pm10010mptAlmClientRxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmClientRxPowerLowWarningPortn.setStatus("current")
_Pm10010mptAlmClientRxPowerHighWarningPortn_Type = EkiOnOff
_Pm10010mptAlmClientRxPowerHighWarningPortn_Object = MibTableColumn
pm10010mptAlmClientRxPowerHighWarningPortn = _Pm10010mptAlmClientRxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 1, 56, 1, 4),
    _Pm10010mptAlmClientRxPowerHighWarningPortn_Type()
)
pm10010mptAlmClientRxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmClientRxPowerHighWarningPortn.setStatus("current")
_Pm10010mptAlmClientRxPowerHighAlarmPortn_Type = EkiOnOff
_Pm10010mptAlmClientRxPowerHighAlarmPortn_Object = MibTableColumn
pm10010mptAlmClientRxPowerHighAlarmPortn = _Pm10010mptAlmClientRxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 1, 56, 1, 5),
    _Pm10010mptAlmClientRxPowerHighAlarmPortn_Type()
)
pm10010mptAlmClientRxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmClientRxPowerHighAlarmPortn.setStatus("current")
_Pm10010mptAlmLaserTempLowAlarmPortn_Type = EkiOnOff
_Pm10010mptAlmLaserTempLowAlarmPortn_Object = MibTableColumn
pm10010mptAlmLaserTempLowAlarmPortn = _Pm10010mptAlmLaserTempLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 1, 56, 1, 6),
    _Pm10010mptAlmLaserTempLowAlarmPortn_Type()
)
pm10010mptAlmLaserTempLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmLaserTempLowAlarmPortn.setStatus("current")
_Pm10010mptAlmClientLaserTempLowWarningPortn_Type = EkiOnOff
_Pm10010mptAlmClientLaserTempLowWarningPortn_Object = MibTableColumn
pm10010mptAlmClientLaserTempLowWarningPortn = _Pm10010mptAlmClientLaserTempLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 1, 56, 1, 7),
    _Pm10010mptAlmClientLaserTempLowWarningPortn_Type()
)
pm10010mptAlmClientLaserTempLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmClientLaserTempLowWarningPortn.setStatus("current")
_Pm10010mptAlmClientLaserTempHighWarningPortn_Type = EkiOnOff
_Pm10010mptAlmClientLaserTempHighWarningPortn_Object = MibTableColumn
pm10010mptAlmClientLaserTempHighWarningPortn = _Pm10010mptAlmClientLaserTempHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 1, 56, 1, 8),
    _Pm10010mptAlmClientLaserTempHighWarningPortn_Type()
)
pm10010mptAlmClientLaserTempHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmClientLaserTempHighWarningPortn.setStatus("current")
_Pm10010mptAlmClientLaserTempHighAlarmPortn_Type = EkiOnOff
_Pm10010mptAlmClientLaserTempHighAlarmPortn_Object = MibTableColumn
pm10010mptAlmClientLaserTempHighAlarmPortn = _Pm10010mptAlmClientLaserTempHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 1, 56, 1, 9),
    _Pm10010mptAlmClientLaserTempHighAlarmPortn_Type()
)
pm10010mptAlmClientLaserTempHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmClientLaserTempHighAlarmPortn.setStatus("current")
_Pm10010mptAlmClientTxPowerLowAlarmPortn_Type = EkiOnOff
_Pm10010mptAlmClientTxPowerLowAlarmPortn_Object = MibTableColumn
pm10010mptAlmClientTxPowerLowAlarmPortn = _Pm10010mptAlmClientTxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 1, 56, 1, 10),
    _Pm10010mptAlmClientTxPowerLowAlarmPortn_Type()
)
pm10010mptAlmClientTxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmClientTxPowerLowAlarmPortn.setStatus("current")
_Pm10010mptAlmClientTxPowerLowWarningPortn_Type = EkiOnOff
_Pm10010mptAlmClientTxPowerLowWarningPortn_Object = MibTableColumn
pm10010mptAlmClientTxPowerLowWarningPortn = _Pm10010mptAlmClientTxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 1, 56, 1, 11),
    _Pm10010mptAlmClientTxPowerLowWarningPortn_Type()
)
pm10010mptAlmClientTxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmClientTxPowerLowWarningPortn.setStatus("current")
_Pm10010mptAlmClientTxPowerHighWarningPortn_Type = EkiOnOff
_Pm10010mptAlmClientTxPowerHighWarningPortn_Object = MibTableColumn
pm10010mptAlmClientTxPowerHighWarningPortn = _Pm10010mptAlmClientTxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 1, 56, 1, 12),
    _Pm10010mptAlmClientTxPowerHighWarningPortn_Type()
)
pm10010mptAlmClientTxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmClientTxPowerHighWarningPortn.setStatus("current")
_Pm10010mptAlmClientTxPowerHighAlarmPortn_Type = EkiOnOff
_Pm10010mptAlmClientTxPowerHighAlarmPortn_Object = MibTableColumn
pm10010mptAlmClientTxPowerHighAlarmPortn = _Pm10010mptAlmClientTxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 1, 56, 1, 13),
    _Pm10010mptAlmClientTxPowerHighAlarmPortn_Type()
)
pm10010mptAlmClientTxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmClientTxPowerHighAlarmPortn.setStatus("current")
_Pm10010mptAlmClientBiasLowAlarmPortn_Type = EkiOnOff
_Pm10010mptAlmClientBiasLowAlarmPortn_Object = MibTableColumn
pm10010mptAlmClientBiasLowAlarmPortn = _Pm10010mptAlmClientBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 1, 56, 1, 14),
    _Pm10010mptAlmClientBiasLowAlarmPortn_Type()
)
pm10010mptAlmClientBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmClientBiasLowAlarmPortn.setStatus("current")
_Pm10010mptAlmClientBiasLowWarningPortn_Type = EkiOnOff
_Pm10010mptAlmClientBiasLowWarningPortn_Object = MibTableColumn
pm10010mptAlmClientBiasLowWarningPortn = _Pm10010mptAlmClientBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 1, 56, 1, 15),
    _Pm10010mptAlmClientBiasLowWarningPortn_Type()
)
pm10010mptAlmClientBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmClientBiasLowWarningPortn.setStatus("current")
_Pm10010mptAlmClientBiasHighWarningPortn_Type = EkiOnOff
_Pm10010mptAlmClientBiasHighWarningPortn_Object = MibTableColumn
pm10010mptAlmClientBiasHighWarningPortn = _Pm10010mptAlmClientBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 1, 56, 1, 16),
    _Pm10010mptAlmClientBiasHighWarningPortn_Type()
)
pm10010mptAlmClientBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmClientBiasHighWarningPortn.setStatus("current")
_Pm10010mptAlmClientBiasHighAlarmPortn_Type = EkiOnOff
_Pm10010mptAlmClientBiasHighAlarmPortn_Object = MibTableColumn
pm10010mptAlmClientBiasHighAlarmPortn = _Pm10010mptAlmClientBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 1, 56, 1, 17),
    _Pm10010mptAlmClientBiasHighAlarmPortn_Type()
)
pm10010mptAlmClientBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmClientBiasHighAlarmPortn.setStatus("current")
_Pm10010mptAlmclientSfpWarnDdmTable_Object = MibTable
pm10010mptAlmclientSfpWarnDdmTable = _Pm10010mptAlmclientSfpWarnDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 1, 232)
)
if mibBuilder.loadTexts:
    pm10010mptAlmclientSfpWarnDdmTable.setStatus("current")
_Pm10010mptAlmclientSfpWarnDdmEntry_Object = MibTableRow
pm10010mptAlmclientSfpWarnDdmEntry = _Pm10010mptAlmclientSfpWarnDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 1, 232, 1)
)
pm10010mptAlmclientSfpWarnDdmEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptAlmclientSfpWarnDdmIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptAlmclientSfpWarnDdmEntry.setStatus("current")


class _Pm10010mptAlmclientSfpWarnDdmIndex_Type(Integer32):
    """Custom type pm10010mptAlmclientSfpWarnDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptAlmclientSfpWarnDdmIndex_Type.__name__ = "Integer32"
_Pm10010mptAlmclientSfpWarnDdmIndex_Object = MibTableColumn
pm10010mptAlmclientSfpWarnDdmIndex = _Pm10010mptAlmclientSfpWarnDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 1, 232, 1, 1),
    _Pm10010mptAlmclientSfpWarnDdmIndex_Type()
)
pm10010mptAlmclientSfpWarnDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmclientSfpWarnDdmIndex.setStatus("current")
_Pm10010mptAlmTxPwLowWngPortn_Type = EkiOnOff
_Pm10010mptAlmTxPwLowWngPortn_Object = MibTableColumn
pm10010mptAlmTxPwLowWngPortn = _Pm10010mptAlmTxPwLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 1, 232, 1, 2),
    _Pm10010mptAlmTxPwLowWngPortn_Type()
)
pm10010mptAlmTxPwLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmTxPwLowWngPortn.setStatus("current")
_Pm10010mptAlmTxPwrHighWngPortn_Type = EkiOnOff
_Pm10010mptAlmTxPwrHighWngPortn_Object = MibTableColumn
pm10010mptAlmTxPwrHighWngPortn = _Pm10010mptAlmTxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 1, 232, 1, 3),
    _Pm10010mptAlmTxPwrHighWngPortn_Type()
)
pm10010mptAlmTxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmTxPwrHighWngPortn.setStatus("current")
_Pm10010mptAlmTxBiasLowWngPortn_Type = EkiOnOff
_Pm10010mptAlmTxBiasLowWngPortn_Object = MibTableColumn
pm10010mptAlmTxBiasLowWngPortn = _Pm10010mptAlmTxBiasLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 1, 232, 1, 4),
    _Pm10010mptAlmTxBiasLowWngPortn_Type()
)
pm10010mptAlmTxBiasLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmTxBiasLowWngPortn.setStatus("current")
_Pm10010mptAlmTxBiasHighWngPortn_Type = EkiOnOff
_Pm10010mptAlmTxBiasHighWngPortn_Object = MibTableColumn
pm10010mptAlmTxBiasHighWngPortn = _Pm10010mptAlmTxBiasHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 1, 232, 1, 5),
    _Pm10010mptAlmTxBiasHighWngPortn_Type()
)
pm10010mptAlmTxBiasHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmTxBiasHighWngPortn.setStatus("current")
_Pm10010mptAlmVccLowWngPortn_Type = EkiOnOff
_Pm10010mptAlmVccLowWngPortn_Object = MibTableColumn
pm10010mptAlmVccLowWngPortn = _Pm10010mptAlmVccLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 1, 232, 1, 6),
    _Pm10010mptAlmVccLowWngPortn_Type()
)
pm10010mptAlmVccLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmVccLowWngPortn.setStatus("current")
_Pm10010mptAlmVccHighWngPortn_Type = EkiOnOff
_Pm10010mptAlmVccHighWngPortn_Object = MibTableColumn
pm10010mptAlmVccHighWngPortn = _Pm10010mptAlmVccHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 1, 232, 1, 7),
    _Pm10010mptAlmVccHighWngPortn_Type()
)
pm10010mptAlmVccHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmVccHighWngPortn.setStatus("current")
_Pm10010mptAlmTempLowWngPortn_Type = EkiOnOff
_Pm10010mptAlmTempLowWngPortn_Object = MibTableColumn
pm10010mptAlmTempLowWngPortn = _Pm10010mptAlmTempLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 1, 232, 1, 8),
    _Pm10010mptAlmTempLowWngPortn_Type()
)
pm10010mptAlmTempLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmTempLowWngPortn.setStatus("current")
_Pm10010mptAlmTempHighWngPortn_Type = EkiOnOff
_Pm10010mptAlmTempHighWngPortn_Object = MibTableColumn
pm10010mptAlmTempHighWngPortn = _Pm10010mptAlmTempHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 1, 232, 1, 9),
    _Pm10010mptAlmTempHighWngPortn_Type()
)
pm10010mptAlmTempHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmTempHighWngPortn.setStatus("current")
_Pm10010mptAlmRxPwrLowWngPortn_Type = EkiOnOff
_Pm10010mptAlmRxPwrLowWngPortn_Object = MibTableColumn
pm10010mptAlmRxPwrLowWngPortn = _Pm10010mptAlmRxPwrLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 1, 232, 1, 16),
    _Pm10010mptAlmRxPwrLowWngPortn_Type()
)
pm10010mptAlmRxPwrLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmRxPwrLowWngPortn.setStatus("current")
_Pm10010mptAlmRxPwrHighWngPortn_Type = EkiOnOff
_Pm10010mptAlmRxPwrHighWngPortn_Object = MibTableColumn
pm10010mptAlmRxPwrHighWngPortn = _Pm10010mptAlmRxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 1, 232, 1, 17),
    _Pm10010mptAlmRxPwrHighWngPortn_Type()
)
pm10010mptAlmRxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmRxPwrHighWngPortn.setStatus("current")
_Pm10010mptAlmClientUrg_ObjectIdentity = ObjectIdentity
pm10010mptAlmClientUrg = _Pm10010mptAlmClientUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 2)
)
_Pm10010mptAlmclientNetworkLaneFaultTable_Object = MibTable
pm10010mptAlmclientNetworkLaneFaultTable = _Pm10010mptAlmclientNetworkLaneFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 2, 72)
)
if mibBuilder.loadTexts:
    pm10010mptAlmclientNetworkLaneFaultTable.setStatus("current")
_Pm10010mptAlmclientNetworkLaneFaultEntry_Object = MibTableRow
pm10010mptAlmclientNetworkLaneFaultEntry = _Pm10010mptAlmclientNetworkLaneFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 2, 72, 1)
)
pm10010mptAlmclientNetworkLaneFaultEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptAlmclientNetworkLaneFaultIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptAlmclientNetworkLaneFaultEntry.setStatus("current")


class _Pm10010mptAlmclientNetworkLaneFaultIndex_Type(Integer32):
    """Custom type pm10010mptAlmclientNetworkLaneFaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptAlmclientNetworkLaneFaultIndex_Type.__name__ = "Integer32"
_Pm10010mptAlmclientNetworkLaneFaultIndex_Object = MibTableColumn
pm10010mptAlmclientNetworkLaneFaultIndex = _Pm10010mptAlmclientNetworkLaneFaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 2, 72, 1, 1),
    _Pm10010mptAlmclientNetworkLaneFaultIndex_Type()
)
pm10010mptAlmclientNetworkLaneFaultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmclientNetworkLaneFaultIndex.setStatus("current")
_Pm10010mptAlmClientLaneRxFifoErrorPortn_Type = EkiOnOff
_Pm10010mptAlmClientLaneRxFifoErrorPortn_Object = MibTableColumn
pm10010mptAlmClientLaneRxFifoErrorPortn = _Pm10010mptAlmClientLaneRxFifoErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 2, 72, 1, 4),
    _Pm10010mptAlmClientLaneRxFifoErrorPortn_Type()
)
pm10010mptAlmClientLaneRxFifoErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmClientLaneRxFifoErrorPortn.setStatus("current")
_Pm10010mptAlmClientLaneRxLolPortn_Type = EkiOnOff
_Pm10010mptAlmClientLaneRxLolPortn_Object = MibTableColumn
pm10010mptAlmClientLaneRxLolPortn = _Pm10010mptAlmClientLaneRxLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 2, 72, 1, 5),
    _Pm10010mptAlmClientLaneRxLolPortn_Type()
)
pm10010mptAlmClientLaneRxLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmClientLaneRxLolPortn.setStatus("current")
_Pm10010mptAlmClientLaneRxLosPortn_Type = EkiOnOff
_Pm10010mptAlmClientLaneRxLosPortn_Object = MibTableColumn
pm10010mptAlmClientLaneRxLosPortn = _Pm10010mptAlmClientLaneRxLosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 2, 72, 1, 6),
    _Pm10010mptAlmClientLaneRxLosPortn_Type()
)
pm10010mptAlmClientLaneRxLosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmClientLaneRxLosPortn.setStatus("current")
_Pm10010mptAlmClientLaneTxLolPortn_Type = EkiOnOff
_Pm10010mptAlmClientLaneTxLolPortn_Object = MibTableColumn
pm10010mptAlmClientLaneTxLolPortn = _Pm10010mptAlmClientLaneTxLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 2, 72, 1, 8),
    _Pm10010mptAlmClientLaneTxLolPortn_Type()
)
pm10010mptAlmClientLaneTxLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmClientLaneTxLolPortn.setStatus("current")
_Pm10010mptAlmClientLaneTxLosfPortn_Type = EkiOnOff
_Pm10010mptAlmClientLaneTxLosfPortn_Object = MibTableColumn
pm10010mptAlmClientLaneTxLosfPortn = _Pm10010mptAlmClientLaneTxLosfPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 2, 72, 1, 9),
    _Pm10010mptAlmClientLaneTxLosfPortn_Type()
)
pm10010mptAlmClientLaneTxLosfPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmClientLaneTxLosfPortn.setStatus("current")
_Pm10010mptAlmClientLaneApdPowerSupplyPortn_Type = EkiOnOff
_Pm10010mptAlmClientLaneApdPowerSupplyPortn_Object = MibTableColumn
pm10010mptAlmClientLaneApdPowerSupplyPortn = _Pm10010mptAlmClientLaneApdPowerSupplyPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 2, 72, 1, 15),
    _Pm10010mptAlmClientLaneApdPowerSupplyPortn_Type()
)
pm10010mptAlmClientLaneApdPowerSupplyPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmClientLaneApdPowerSupplyPortn.setStatus("current")
_Pm10010mptAlmClientLaneWavelengthUnlockedPortn_Type = EkiOnOff
_Pm10010mptAlmClientLaneWavelengthUnlockedPortn_Object = MibTableColumn
pm10010mptAlmClientLaneWavelengthUnlockedPortn = _Pm10010mptAlmClientLaneWavelengthUnlockedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 2, 72, 1, 16),
    _Pm10010mptAlmClientLaneWavelengthUnlockedPortn_Type()
)
pm10010mptAlmClientLaneWavelengthUnlockedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmClientLaneWavelengthUnlockedPortn.setStatus("current")
_Pm10010mptAlmClientLaneTecFaultPortn_Type = EkiOnOff
_Pm10010mptAlmClientLaneTecFaultPortn_Object = MibTableColumn
pm10010mptAlmClientLaneTecFaultPortn = _Pm10010mptAlmClientLaneTecFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 2, 72, 1, 17),
    _Pm10010mptAlmClientLaneTecFaultPortn_Type()
)
pm10010mptAlmClientLaneTecFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmClientLaneTecFaultPortn.setStatus("current")
_Pm10010mptAlmclientHostLaneFaultTable_Object = MibTable
pm10010mptAlmclientHostLaneFaultTable = _Pm10010mptAlmclientHostLaneFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 2, 88)
)
if mibBuilder.loadTexts:
    pm10010mptAlmclientHostLaneFaultTable.setStatus("current")
_Pm10010mptAlmclientHostLaneFaultEntry_Object = MibTableRow
pm10010mptAlmclientHostLaneFaultEntry = _Pm10010mptAlmclientHostLaneFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 2, 88, 1)
)
pm10010mptAlmclientHostLaneFaultEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptAlmclientHostLaneFaultIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptAlmclientHostLaneFaultEntry.setStatus("current")


class _Pm10010mptAlmclientHostLaneFaultIndex_Type(Integer32):
    """Custom type pm10010mptAlmclientHostLaneFaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptAlmclientHostLaneFaultIndex_Type.__name__ = "Integer32"
_Pm10010mptAlmclientHostLaneFaultIndex_Object = MibTableColumn
pm10010mptAlmclientHostLaneFaultIndex = _Pm10010mptAlmclientHostLaneFaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 2, 88, 1, 1),
    _Pm10010mptAlmclientHostLaneFaultIndex_Type()
)
pm10010mptAlmclientHostLaneFaultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmclientHostLaneFaultIndex.setStatus("current")
_Pm10010mptAlmClientLossOfSyncPortn_Type = EkiOnOff
_Pm10010mptAlmClientLossOfSyncPortn_Object = MibTableColumn
pm10010mptAlmClientLossOfSyncPortn = _Pm10010mptAlmClientLossOfSyncPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 2, 88, 1, 2),
    _Pm10010mptAlmClientLossOfSyncPortn_Type()
)
pm10010mptAlmClientLossOfSyncPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmClientLossOfSyncPortn.setStatus("current")
_Pm10010mptAlmClientInputLossOfSigPortn_Type = EkiOnOff
_Pm10010mptAlmClientInputLossOfSigPortn_Object = MibTableColumn
pm10010mptAlmClientInputLossOfSigPortn = _Pm10010mptAlmClientInputLossOfSigPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 2, 88, 1, 3),
    _Pm10010mptAlmClientInputLossOfSigPortn_Type()
)
pm10010mptAlmClientInputLossOfSigPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmClientInputLossOfSigPortn.setStatus("current")
_Pm10010mptAlmClientLanesMarkerUnlockPortn_Type = EkiOnOff
_Pm10010mptAlmClientLanesMarkerUnlockPortn_Object = MibTableColumn
pm10010mptAlmClientLanesMarkerUnlockPortn = _Pm10010mptAlmClientLanesMarkerUnlockPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 2, 88, 1, 4),
    _Pm10010mptAlmClientLanesMarkerUnlockPortn_Type()
)
pm10010mptAlmClientLanesMarkerUnlockPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmClientLanesMarkerUnlockPortn.setStatus("current")
_Pm10010mptAlmClientLanes6466UnlockPortn_Type = EkiOnOff
_Pm10010mptAlmClientLanes6466UnlockPortn_Object = MibTableColumn
pm10010mptAlmClientLanes6466UnlockPortn = _Pm10010mptAlmClientLanes6466UnlockPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 2, 88, 1, 5),
    _Pm10010mptAlmClientLanes6466UnlockPortn_Type()
)
pm10010mptAlmClientLanes6466UnlockPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmClientLanes6466UnlockPortn.setStatus("current")
_Pm10010mptAlmClientLanesNotAlignedPortn_Type = EkiOnOff
_Pm10010mptAlmClientLanesNotAlignedPortn_Object = MibTableColumn
pm10010mptAlmClientLanesNotAlignedPortn = _Pm10010mptAlmClientLanesNotAlignedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 2, 88, 1, 6),
    _Pm10010mptAlmClientLanesNotAlignedPortn_Type()
)
pm10010mptAlmClientLanesNotAlignedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmClientLanesNotAlignedPortn.setStatus("current")
_Pm10010mptAlmClientCsfDetectedPortn_Type = EkiOnOff
_Pm10010mptAlmClientCsfDetectedPortn_Object = MibTableColumn
pm10010mptAlmClientCsfDetectedPortn = _Pm10010mptAlmClientCsfDetectedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 2, 88, 1, 7),
    _Pm10010mptAlmClientCsfDetectedPortn_Type()
)
pm10010mptAlmClientCsfDetectedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmClientCsfDetectedPortn.setStatus("current")
_Pm10010mptAlmClientTxHostLolPortn_Type = EkiOnOff
_Pm10010mptAlmClientTxHostLolPortn_Object = MibTableColumn
pm10010mptAlmClientTxHostLolPortn = _Pm10010mptAlmClientTxHostLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 2, 88, 1, 10),
    _Pm10010mptAlmClientTxHostLolPortn_Type()
)
pm10010mptAlmClientTxHostLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmClientTxHostLolPortn.setStatus("current")
_Pm10010mptAlmClientLaneTxFifoErrorPortn_Type = EkiOnOff
_Pm10010mptAlmClientLaneTxFifoErrorPortn_Object = MibTableColumn
pm10010mptAlmClientLaneTxFifoErrorPortn = _Pm10010mptAlmClientLaneTxFifoErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 2, 88, 1, 11),
    _Pm10010mptAlmClientLaneTxFifoErrorPortn_Type()
)
pm10010mptAlmClientLaneTxFifoErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmClientLaneTxFifoErrorPortn.setStatus("current")
_Pm10010mptAlmLfDetectedPortn_Type = EkiOnOff
_Pm10010mptAlmLfDetectedPortn_Object = MibTableColumn
pm10010mptAlmLfDetectedPortn = _Pm10010mptAlmLfDetectedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 2, 88, 1, 12),
    _Pm10010mptAlmLfDetectedPortn_Type()
)
pm10010mptAlmLfDetectedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmLfDetectedPortn.setStatus("current")
_Pm10010mptAlmRfDetectedPortn_Type = EkiOnOff
_Pm10010mptAlmRfDetectedPortn_Object = MibTableColumn
pm10010mptAlmRfDetectedPortn = _Pm10010mptAlmRfDetectedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 2, 88, 1, 13),
    _Pm10010mptAlmRfDetectedPortn_Type()
)
pm10010mptAlmRfDetectedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmRfDetectedPortn.setStatus("current")
_Pm10010mptAlmclientSfpAlmDdmTable_Object = MibTable
pm10010mptAlmclientSfpAlmDdmTable = _Pm10010mptAlmclientSfpAlmDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 2, 216)
)
if mibBuilder.loadTexts:
    pm10010mptAlmclientSfpAlmDdmTable.setStatus("current")
_Pm10010mptAlmclientSfpAlmDdmEntry_Object = MibTableRow
pm10010mptAlmclientSfpAlmDdmEntry = _Pm10010mptAlmclientSfpAlmDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 2, 216, 1)
)
pm10010mptAlmclientSfpAlmDdmEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptAlmclientSfpAlmDdmIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptAlmclientSfpAlmDdmEntry.setStatus("current")


class _Pm10010mptAlmclientSfpAlmDdmIndex_Type(Integer32):
    """Custom type pm10010mptAlmclientSfpAlmDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptAlmclientSfpAlmDdmIndex_Type.__name__ = "Integer32"
_Pm10010mptAlmclientSfpAlmDdmIndex_Object = MibTableColumn
pm10010mptAlmclientSfpAlmDdmIndex = _Pm10010mptAlmclientSfpAlmDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 2, 216, 1, 1),
    _Pm10010mptAlmclientSfpAlmDdmIndex_Type()
)
pm10010mptAlmclientSfpAlmDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmclientSfpAlmDdmIndex.setStatus("current")
_Pm10010mptAlmTxPwrLowAlaPortn_Type = EkiOnOff
_Pm10010mptAlmTxPwrLowAlaPortn_Object = MibTableColumn
pm10010mptAlmTxPwrLowAlaPortn = _Pm10010mptAlmTxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 2, 216, 1, 2),
    _Pm10010mptAlmTxPwrLowAlaPortn_Type()
)
pm10010mptAlmTxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmTxPwrLowAlaPortn.setStatus("current")
_Pm10010mptAlmTxPwrHighAlaPortn_Type = EkiOnOff
_Pm10010mptAlmTxPwrHighAlaPortn_Object = MibTableColumn
pm10010mptAlmTxPwrHighAlaPortn = _Pm10010mptAlmTxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 2, 216, 1, 3),
    _Pm10010mptAlmTxPwrHighAlaPortn_Type()
)
pm10010mptAlmTxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmTxPwrHighAlaPortn.setStatus("current")
_Pm10010mptAlmTxBiasLowAlaPortn_Type = EkiOnOff
_Pm10010mptAlmTxBiasLowAlaPortn_Object = MibTableColumn
pm10010mptAlmTxBiasLowAlaPortn = _Pm10010mptAlmTxBiasLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 2, 216, 1, 4),
    _Pm10010mptAlmTxBiasLowAlaPortn_Type()
)
pm10010mptAlmTxBiasLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmTxBiasLowAlaPortn.setStatus("current")
_Pm10010mptAlmTxBiasHighAlaPortn_Type = EkiOnOff
_Pm10010mptAlmTxBiasHighAlaPortn_Object = MibTableColumn
pm10010mptAlmTxBiasHighAlaPortn = _Pm10010mptAlmTxBiasHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 2, 216, 1, 5),
    _Pm10010mptAlmTxBiasHighAlaPortn_Type()
)
pm10010mptAlmTxBiasHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmTxBiasHighAlaPortn.setStatus("current")
_Pm10010mptAlmVccLowAlaPortn_Type = EkiOnOff
_Pm10010mptAlmVccLowAlaPortn_Object = MibTableColumn
pm10010mptAlmVccLowAlaPortn = _Pm10010mptAlmVccLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 2, 216, 1, 6),
    _Pm10010mptAlmVccLowAlaPortn_Type()
)
pm10010mptAlmVccLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmVccLowAlaPortn.setStatus("current")
_Pm10010mptAlmVccHighAlaPortn_Type = EkiOnOff
_Pm10010mptAlmVccHighAlaPortn_Object = MibTableColumn
pm10010mptAlmVccHighAlaPortn = _Pm10010mptAlmVccHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 2, 216, 1, 7),
    _Pm10010mptAlmVccHighAlaPortn_Type()
)
pm10010mptAlmVccHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmVccHighAlaPortn.setStatus("current")
_Pm10010mptAlmTempLowAlaPortn_Type = EkiOnOff
_Pm10010mptAlmTempLowAlaPortn_Object = MibTableColumn
pm10010mptAlmTempLowAlaPortn = _Pm10010mptAlmTempLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 2, 216, 1, 8),
    _Pm10010mptAlmTempLowAlaPortn_Type()
)
pm10010mptAlmTempLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmTempLowAlaPortn.setStatus("current")
_Pm10010mptAlmTempHighAlaPortn_Type = EkiOnOff
_Pm10010mptAlmTempHighAlaPortn_Object = MibTableColumn
pm10010mptAlmTempHighAlaPortn = _Pm10010mptAlmTempHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 2, 216, 1, 9),
    _Pm10010mptAlmTempHighAlaPortn_Type()
)
pm10010mptAlmTempHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmTempHighAlaPortn.setStatus("current")
_Pm10010mptAlmRxPwrLowAlaPortn_Type = EkiOnOff
_Pm10010mptAlmRxPwrLowAlaPortn_Object = MibTableColumn
pm10010mptAlmRxPwrLowAlaPortn = _Pm10010mptAlmRxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 2, 216, 1, 16),
    _Pm10010mptAlmRxPwrLowAlaPortn_Type()
)
pm10010mptAlmRxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmRxPwrLowAlaPortn.setStatus("current")
_Pm10010mptAlmRxPwrHighAlaPortn_Type = EkiOnOff
_Pm10010mptAlmRxPwrHighAlaPortn_Object = MibTableColumn
pm10010mptAlmRxPwrHighAlaPortn = _Pm10010mptAlmRxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 2, 216, 1, 17),
    _Pm10010mptAlmRxPwrHighAlaPortn_Type()
)
pm10010mptAlmRxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmRxPwrHighAlaPortn.setStatus("current")
_Pm10010mptAlmClientCrit_ObjectIdentity = ObjectIdentity
pm10010mptAlmClientCrit = _Pm10010mptAlmClientCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 3)
)
_Pm10010mptAlmsynthAlmPortTable_Object = MibTable
pm10010mptAlmsynthAlmPortTable = _Pm10010mptAlmsynthAlmPortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 3, 8)
)
if mibBuilder.loadTexts:
    pm10010mptAlmsynthAlmPortTable.setStatus("current")
_Pm10010mptAlmsynthAlmPortEntry_Object = MibTableRow
pm10010mptAlmsynthAlmPortEntry = _Pm10010mptAlmsynthAlmPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 3, 8, 1)
)
pm10010mptAlmsynthAlmPortEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptAlmsynthAlmPortIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptAlmsynthAlmPortEntry.setStatus("current")


class _Pm10010mptAlmsynthAlmPortIndex_Type(Integer32):
    """Custom type pm10010mptAlmsynthAlmPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptAlmsynthAlmPortIndex_Type.__name__ = "Integer32"
_Pm10010mptAlmsynthAlmPortIndex_Object = MibTableColumn
pm10010mptAlmsynthAlmPortIndex = _Pm10010mptAlmsynthAlmPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 3, 8, 1, 1),
    _Pm10010mptAlmsynthAlmPortIndex_Type()
)
pm10010mptAlmsynthAlmPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmsynthAlmPortIndex.setStatus("current")
_Pm10010mptAlmSfpAbsentPortn_Type = EkiOnOff
_Pm10010mptAlmSfpAbsentPortn_Object = MibTableColumn
pm10010mptAlmSfpAbsentPortn = _Pm10010mptAlmSfpAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 3, 8, 1, 2),
    _Pm10010mptAlmSfpAbsentPortn_Type()
)
pm10010mptAlmSfpAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmSfpAbsentPortn.setStatus("current")
_Pm10010mptAlmDdmAbsentPortn_Type = EkiOnOff
_Pm10010mptAlmDdmAbsentPortn_Object = MibTableColumn
pm10010mptAlmDdmAbsentPortn = _Pm10010mptAlmDdmAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 3, 8, 1, 3),
    _Pm10010mptAlmDdmAbsentPortn_Type()
)
pm10010mptAlmDdmAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmDdmAbsentPortn.setStatus("current")
_Pm10010mptAlmHwFailAccPortn_Type = EkiOnOff
_Pm10010mptAlmHwFailAccPortn_Object = MibTableColumn
pm10010mptAlmHwFailAccPortn = _Pm10010mptAlmHwFailAccPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 3, 8, 1, 5),
    _Pm10010mptAlmHwFailAccPortn_Type()
)
pm10010mptAlmHwFailAccPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmHwFailAccPortn.setStatus("current")
_Pm10010mptAlmDwLsdPortn_Type = EkiOnOff
_Pm10010mptAlmDwLsdPortn_Object = MibTableColumn
pm10010mptAlmDwLsdPortn = _Pm10010mptAlmDwLsdPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 3, 8, 1, 6),
    _Pm10010mptAlmDwLsdPortn_Type()
)
pm10010mptAlmDwLsdPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmDwLsdPortn.setStatus("current")
_Pm10010mptAlmClientLocalOosPortn_Type = EkiOnOff
_Pm10010mptAlmClientLocalOosPortn_Object = MibTableColumn
pm10010mptAlmClientLocalOosPortn = _Pm10010mptAlmClientLocalOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 3, 8, 1, 7),
    _Pm10010mptAlmClientLocalOosPortn_Type()
)
pm10010mptAlmClientLocalOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmClientLocalOosPortn.setStatus("current")
_Pm10010mptAlmClientRemoteOosPortn_Type = EkiOnOff
_Pm10010mptAlmClientRemoteOosPortn_Object = MibTableColumn
pm10010mptAlmClientRemoteOosPortn = _Pm10010mptAlmClientRemoteOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 3, 8, 1, 8),
    _Pm10010mptAlmClientRemoteOosPortn_Type()
)
pm10010mptAlmClientRemoteOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmClientRemoteOosPortn.setStatus("current")
_Pm10010mptAlmDwCaisPortn_Type = EkiOnOff
_Pm10010mptAlmDwCaisPortn_Object = MibTableColumn
pm10010mptAlmDwCaisPortn = _Pm10010mptAlmDwCaisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 3, 8, 1, 9),
    _Pm10010mptAlmDwCaisPortn_Type()
)
pm10010mptAlmDwCaisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmDwCaisPortn.setStatus("current")
_Pm10010mptAlmSfpDdmWarningPortn_Type = EkiOnOff
_Pm10010mptAlmSfpDdmWarningPortn_Object = MibTableColumn
pm10010mptAlmSfpDdmWarningPortn = _Pm10010mptAlmSfpDdmWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 3, 8, 1, 10),
    _Pm10010mptAlmSfpDdmWarningPortn_Type()
)
pm10010mptAlmSfpDdmWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmSfpDdmWarningPortn.setStatus("current")
_Pm10010mptAlmSfpDdmAlmPortn_Type = EkiOnOff
_Pm10010mptAlmSfpDdmAlmPortn_Object = MibTableColumn
pm10010mptAlmSfpDdmAlmPortn = _Pm10010mptAlmSfpDdmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 3, 8, 1, 11),
    _Pm10010mptAlmSfpDdmAlmPortn_Type()
)
pm10010mptAlmSfpDdmAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmSfpDdmAlmPortn.setStatus("current")
_Pm10010mptAlmIdleInsertedPortn_Type = EkiOnOff
_Pm10010mptAlmIdleInsertedPortn_Object = MibTableColumn
pm10010mptAlmIdleInsertedPortn = _Pm10010mptAlmIdleInsertedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 3, 8, 1, 12),
    _Pm10010mptAlmIdleInsertedPortn_Type()
)
pm10010mptAlmIdleInsertedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmIdleInsertedPortn.setStatus("current")
_Pm10010mptAlmFailAccPortn_Type = EkiOnOff
_Pm10010mptAlmFailAccPortn_Object = MibTableColumn
pm10010mptAlmFailAccPortn = _Pm10010mptAlmFailAccPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 3, 8, 1, 13),
    _Pm10010mptAlmFailAccPortn_Type()
)
pm10010mptAlmFailAccPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmFailAccPortn.setStatus("current")
_Pm10010mptAlmUpCsfPortn_Type = EkiOnOff
_Pm10010mptAlmUpCsfPortn_Object = MibTableColumn
pm10010mptAlmUpCsfPortn = _Pm10010mptAlmUpCsfPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 2, 3, 8, 1, 17),
    _Pm10010mptAlmUpCsfPortn_Type()
)
pm10010mptAlmUpCsfPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmUpCsfPortn.setStatus("current")
_Pm10010mptAlmLine_ObjectIdentity = ObjectIdentity
pm10010mptAlmLine = _Pm10010mptAlmLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3)
)
_Pm10010mptAlmLineNurg_ObjectIdentity = ObjectIdentity
pm10010mptAlmLineNurg = _Pm10010mptAlmLineNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 1)
)
_Pm10010mptAlmlineNetworkLaneAlarmWarning1Table_Object = MibTable
pm10010mptAlmlineNetworkLaneAlarmWarning1Table = _Pm10010mptAlmlineNetworkLaneAlarmWarning1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 1, 104)
)
if mibBuilder.loadTexts:
    pm10010mptAlmlineNetworkLaneAlarmWarning1Table.setStatus("current")
_Pm10010mptAlmlineNetworkLaneAlarmWarning1Entry_Object = MibTableRow
pm10010mptAlmlineNetworkLaneAlarmWarning1Entry = _Pm10010mptAlmlineNetworkLaneAlarmWarning1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 1, 104, 1)
)
pm10010mptAlmlineNetworkLaneAlarmWarning1Entry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptAlmlineNetworkLaneAlarmWarning1Index"),
)
if mibBuilder.loadTexts:
    pm10010mptAlmlineNetworkLaneAlarmWarning1Entry.setStatus("current")


class _Pm10010mptAlmlineNetworkLaneAlarmWarning1Index_Type(Integer32):
    """Custom type pm10010mptAlmlineNetworkLaneAlarmWarning1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptAlmlineNetworkLaneAlarmWarning1Index_Type.__name__ = "Integer32"
_Pm10010mptAlmlineNetworkLaneAlarmWarning1Index_Object = MibTableColumn
pm10010mptAlmlineNetworkLaneAlarmWarning1Index = _Pm10010mptAlmlineNetworkLaneAlarmWarning1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 1, 104, 1, 1),
    _Pm10010mptAlmlineNetworkLaneAlarmWarning1Index_Type()
)
pm10010mptAlmlineNetworkLaneAlarmWarning1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmlineNetworkLaneAlarmWarning1Index.setStatus("current")
_Pm10010mptAlmLineRxPowerLowAlarmPortn_Type = EkiOnOff
_Pm10010mptAlmLineRxPowerLowAlarmPortn_Object = MibTableColumn
pm10010mptAlmLineRxPowerLowAlarmPortn = _Pm10010mptAlmLineRxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 1, 104, 1, 2),
    _Pm10010mptAlmLineRxPowerLowAlarmPortn_Type()
)
pm10010mptAlmLineRxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmLineRxPowerLowAlarmPortn.setStatus("current")
_Pm10010mptAlmLineRxPowerLowWarningPortn_Type = EkiOnOff
_Pm10010mptAlmLineRxPowerLowWarningPortn_Object = MibTableColumn
pm10010mptAlmLineRxPowerLowWarningPortn = _Pm10010mptAlmLineRxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 1, 104, 1, 3),
    _Pm10010mptAlmLineRxPowerLowWarningPortn_Type()
)
pm10010mptAlmLineRxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmLineRxPowerLowWarningPortn.setStatus("current")
_Pm10010mptAlmLineRxPowerHighWarningPortn_Type = EkiOnOff
_Pm10010mptAlmLineRxPowerHighWarningPortn_Object = MibTableColumn
pm10010mptAlmLineRxPowerHighWarningPortn = _Pm10010mptAlmLineRxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 1, 104, 1, 4),
    _Pm10010mptAlmLineRxPowerHighWarningPortn_Type()
)
pm10010mptAlmLineRxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmLineRxPowerHighWarningPortn.setStatus("current")
_Pm10010mptAlmLineRxPowerHighAlarmPortn_Type = EkiOnOff
_Pm10010mptAlmLineRxPowerHighAlarmPortn_Object = MibTableColumn
pm10010mptAlmLineRxPowerHighAlarmPortn = _Pm10010mptAlmLineRxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 1, 104, 1, 5),
    _Pm10010mptAlmLineRxPowerHighAlarmPortn_Type()
)
pm10010mptAlmLineRxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmLineRxPowerHighAlarmPortn.setStatus("current")
_Pm10010mptAlmLineLaserTempLowAlarmPortn_Type = EkiOnOff
_Pm10010mptAlmLineLaserTempLowAlarmPortn_Object = MibTableColumn
pm10010mptAlmLineLaserTempLowAlarmPortn = _Pm10010mptAlmLineLaserTempLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 1, 104, 1, 6),
    _Pm10010mptAlmLineLaserTempLowAlarmPortn_Type()
)
pm10010mptAlmLineLaserTempLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmLineLaserTempLowAlarmPortn.setStatus("current")
_Pm10010mptAlmLineLaserTempLowWarningPortn_Type = EkiOnOff
_Pm10010mptAlmLineLaserTempLowWarningPortn_Object = MibTableColumn
pm10010mptAlmLineLaserTempLowWarningPortn = _Pm10010mptAlmLineLaserTempLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 1, 104, 1, 7),
    _Pm10010mptAlmLineLaserTempLowWarningPortn_Type()
)
pm10010mptAlmLineLaserTempLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmLineLaserTempLowWarningPortn.setStatus("current")
_Pm10010mptAlmLineLaserTempHighWarningPortn_Type = EkiOnOff
_Pm10010mptAlmLineLaserTempHighWarningPortn_Object = MibTableColumn
pm10010mptAlmLineLaserTempHighWarningPortn = _Pm10010mptAlmLineLaserTempHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 1, 104, 1, 8),
    _Pm10010mptAlmLineLaserTempHighWarningPortn_Type()
)
pm10010mptAlmLineLaserTempHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmLineLaserTempHighWarningPortn.setStatus("current")
_Pm10010mptAlmLineLaserTempHighAlarmPortn_Type = EkiOnOff
_Pm10010mptAlmLineLaserTempHighAlarmPortn_Object = MibTableColumn
pm10010mptAlmLineLaserTempHighAlarmPortn = _Pm10010mptAlmLineLaserTempHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 1, 104, 1, 9),
    _Pm10010mptAlmLineLaserTempHighAlarmPortn_Type()
)
pm10010mptAlmLineLaserTempHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmLineLaserTempHighAlarmPortn.setStatus("current")
_Pm10010mptAlmLineTxPowerLowAlarmPortn_Type = EkiOnOff
_Pm10010mptAlmLineTxPowerLowAlarmPortn_Object = MibTableColumn
pm10010mptAlmLineTxPowerLowAlarmPortn = _Pm10010mptAlmLineTxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 1, 104, 1, 10),
    _Pm10010mptAlmLineTxPowerLowAlarmPortn_Type()
)
pm10010mptAlmLineTxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmLineTxPowerLowAlarmPortn.setStatus("current")
_Pm10010mptAlmLineTxPowerLowWarningPortn_Type = EkiOnOff
_Pm10010mptAlmLineTxPowerLowWarningPortn_Object = MibTableColumn
pm10010mptAlmLineTxPowerLowWarningPortn = _Pm10010mptAlmLineTxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 1, 104, 1, 11),
    _Pm10010mptAlmLineTxPowerLowWarningPortn_Type()
)
pm10010mptAlmLineTxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmLineTxPowerLowWarningPortn.setStatus("current")
_Pm10010mptAlmLineTxPowerHighWarningPortn_Type = EkiOnOff
_Pm10010mptAlmLineTxPowerHighWarningPortn_Object = MibTableColumn
pm10010mptAlmLineTxPowerHighWarningPortn = _Pm10010mptAlmLineTxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 1, 104, 1, 12),
    _Pm10010mptAlmLineTxPowerHighWarningPortn_Type()
)
pm10010mptAlmLineTxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmLineTxPowerHighWarningPortn.setStatus("current")
_Pm10010mptAlmLineTxPowerHighAlarmPortn_Type = EkiOnOff
_Pm10010mptAlmLineTxPowerHighAlarmPortn_Object = MibTableColumn
pm10010mptAlmLineTxPowerHighAlarmPortn = _Pm10010mptAlmLineTxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 1, 104, 1, 13),
    _Pm10010mptAlmLineTxPowerHighAlarmPortn_Type()
)
pm10010mptAlmLineTxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmLineTxPowerHighAlarmPortn.setStatus("current")
_Pm10010mptAlmLineBiasLowAlarmPortn_Type = EkiOnOff
_Pm10010mptAlmLineBiasLowAlarmPortn_Object = MibTableColumn
pm10010mptAlmLineBiasLowAlarmPortn = _Pm10010mptAlmLineBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 1, 104, 1, 14),
    _Pm10010mptAlmLineBiasLowAlarmPortn_Type()
)
pm10010mptAlmLineBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmLineBiasLowAlarmPortn.setStatus("current")
_Pm10010mptAlmLineBiasLowWarningPortn_Type = EkiOnOff
_Pm10010mptAlmLineBiasLowWarningPortn_Object = MibTableColumn
pm10010mptAlmLineBiasLowWarningPortn = _Pm10010mptAlmLineBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 1, 104, 1, 15),
    _Pm10010mptAlmLineBiasLowWarningPortn_Type()
)
pm10010mptAlmLineBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmLineBiasLowWarningPortn.setStatus("current")
_Pm10010mptAlmLineBiasHighWarningPortn_Type = EkiOnOff
_Pm10010mptAlmLineBiasHighWarningPortn_Object = MibTableColumn
pm10010mptAlmLineBiasHighWarningPortn = _Pm10010mptAlmLineBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 1, 104, 1, 16),
    _Pm10010mptAlmLineBiasHighWarningPortn_Type()
)
pm10010mptAlmLineBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmLineBiasHighWarningPortn.setStatus("current")
_Pm10010mptAlmLineBiasHighAlarmPortn_Type = EkiOnOff
_Pm10010mptAlmLineBiasHighAlarmPortn_Object = MibTableColumn
pm10010mptAlmLineBiasHighAlarmPortn = _Pm10010mptAlmLineBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 1, 104, 1, 17),
    _Pm10010mptAlmLineBiasHighAlarmPortn_Type()
)
pm10010mptAlmLineBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmLineBiasHighAlarmPortn.setStatus("current")
_Pm10010mptAlmlineNetworkLaneAlarmWarning2Table_Object = MibTable
pm10010mptAlmlineNetworkLaneAlarmWarning2Table = _Pm10010mptAlmlineNetworkLaneAlarmWarning2Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 1, 120)
)
if mibBuilder.loadTexts:
    pm10010mptAlmlineNetworkLaneAlarmWarning2Table.setStatus("current")
_Pm10010mptAlmlineNetworkLaneAlarmWarning2Entry_Object = MibTableRow
pm10010mptAlmlineNetworkLaneAlarmWarning2Entry = _Pm10010mptAlmlineNetworkLaneAlarmWarning2Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 1, 120, 1)
)
pm10010mptAlmlineNetworkLaneAlarmWarning2Entry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptAlmlineNetworkLaneAlarmWarning2Index"),
)
if mibBuilder.loadTexts:
    pm10010mptAlmlineNetworkLaneAlarmWarning2Entry.setStatus("current")


class _Pm10010mptAlmlineNetworkLaneAlarmWarning2Index_Type(Integer32):
    """Custom type pm10010mptAlmlineNetworkLaneAlarmWarning2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptAlmlineNetworkLaneAlarmWarning2Index_Type.__name__ = "Integer32"
_Pm10010mptAlmlineNetworkLaneAlarmWarning2Index_Object = MibTableColumn
pm10010mptAlmlineNetworkLaneAlarmWarning2Index = _Pm10010mptAlmlineNetworkLaneAlarmWarning2Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 1, 120, 1, 1),
    _Pm10010mptAlmlineNetworkLaneAlarmWarning2Index_Type()
)
pm10010mptAlmlineNetworkLaneAlarmWarning2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmlineNetworkLaneAlarmWarning2Index.setStatus("current")
_Pm10010mptAlmTxModulatorBiasLowAlarmPortn_Type = EkiOnOff
_Pm10010mptAlmTxModulatorBiasLowAlarmPortn_Object = MibTableColumn
pm10010mptAlmTxModulatorBiasLowAlarmPortn = _Pm10010mptAlmTxModulatorBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 1, 120, 1, 2),
    _Pm10010mptAlmTxModulatorBiasLowAlarmPortn_Type()
)
pm10010mptAlmTxModulatorBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmTxModulatorBiasLowAlarmPortn.setStatus("current")
_Pm10010mptAlmTxModulatorBiasLowWarningPortn_Type = EkiOnOff
_Pm10010mptAlmTxModulatorBiasLowWarningPortn_Object = MibTableColumn
pm10010mptAlmTxModulatorBiasLowWarningPortn = _Pm10010mptAlmTxModulatorBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 1, 120, 1, 3),
    _Pm10010mptAlmTxModulatorBiasLowWarningPortn_Type()
)
pm10010mptAlmTxModulatorBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmTxModulatorBiasLowWarningPortn.setStatus("current")
_Pm10010mptAlmTxModulatorBiasHighWarningPortn_Type = EkiOnOff
_Pm10010mptAlmTxModulatorBiasHighWarningPortn_Object = MibTableColumn
pm10010mptAlmTxModulatorBiasHighWarningPortn = _Pm10010mptAlmTxModulatorBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 1, 120, 1, 4),
    _Pm10010mptAlmTxModulatorBiasHighWarningPortn_Type()
)
pm10010mptAlmTxModulatorBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmTxModulatorBiasHighWarningPortn.setStatus("current")
_Pm10010mptAlmTxModulatorBiasHighAlarmPortn_Type = EkiOnOff
_Pm10010mptAlmTxModulatorBiasHighAlarmPortn_Object = MibTableColumn
pm10010mptAlmTxModulatorBiasHighAlarmPortn = _Pm10010mptAlmTxModulatorBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 1, 120, 1, 5),
    _Pm10010mptAlmTxModulatorBiasHighAlarmPortn_Type()
)
pm10010mptAlmTxModulatorBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmTxModulatorBiasHighAlarmPortn.setStatus("current")
_Pm10010mptAlmRxLaserTempLowAlarmPortn_Type = EkiOnOff
_Pm10010mptAlmRxLaserTempLowAlarmPortn_Object = MibTableColumn
pm10010mptAlmRxLaserTempLowAlarmPortn = _Pm10010mptAlmRxLaserTempLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 1, 120, 1, 6),
    _Pm10010mptAlmRxLaserTempLowAlarmPortn_Type()
)
pm10010mptAlmRxLaserTempLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmRxLaserTempLowAlarmPortn.setStatus("current")
_Pm10010mptAlmRxLaserTempLowWarningPortn_Type = EkiOnOff
_Pm10010mptAlmRxLaserTempLowWarningPortn_Object = MibTableColumn
pm10010mptAlmRxLaserTempLowWarningPortn = _Pm10010mptAlmRxLaserTempLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 1, 120, 1, 7),
    _Pm10010mptAlmRxLaserTempLowWarningPortn_Type()
)
pm10010mptAlmRxLaserTempLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmRxLaserTempLowWarningPortn.setStatus("current")
_Pm10010mptAlmRxLaserTempHighWarningPortn_Type = EkiOnOff
_Pm10010mptAlmRxLaserTempHighWarningPortn_Object = MibTableColumn
pm10010mptAlmRxLaserTempHighWarningPortn = _Pm10010mptAlmRxLaserTempHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 1, 120, 1, 8),
    _Pm10010mptAlmRxLaserTempHighWarningPortn_Type()
)
pm10010mptAlmRxLaserTempHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmRxLaserTempHighWarningPortn.setStatus("current")
_Pm10010mptAlmRxLaserTempHighAlarmPortn_Type = EkiOnOff
_Pm10010mptAlmRxLaserTempHighAlarmPortn_Object = MibTableColumn
pm10010mptAlmRxLaserTempHighAlarmPortn = _Pm10010mptAlmRxLaserTempHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 1, 120, 1, 9),
    _Pm10010mptAlmRxLaserTempHighAlarmPortn_Type()
)
pm10010mptAlmRxLaserTempHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmRxLaserTempHighAlarmPortn.setStatus("current")
_Pm10010mptAlmRxLaserOutputLowAlarmPortn_Type = EkiOnOff
_Pm10010mptAlmRxLaserOutputLowAlarmPortn_Object = MibTableColumn
pm10010mptAlmRxLaserOutputLowAlarmPortn = _Pm10010mptAlmRxLaserOutputLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 1, 120, 1, 10),
    _Pm10010mptAlmRxLaserOutputLowAlarmPortn_Type()
)
pm10010mptAlmRxLaserOutputLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmRxLaserOutputLowAlarmPortn.setStatus("current")
_Pm10010mptAlmRxLaserOutputLowWarningPortn_Type = EkiOnOff
_Pm10010mptAlmRxLaserOutputLowWarningPortn_Object = MibTableColumn
pm10010mptAlmRxLaserOutputLowWarningPortn = _Pm10010mptAlmRxLaserOutputLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 1, 120, 1, 11),
    _Pm10010mptAlmRxLaserOutputLowWarningPortn_Type()
)
pm10010mptAlmRxLaserOutputLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmRxLaserOutputLowWarningPortn.setStatus("current")
_Pm10010mptAlmRxLaserOutputHighWarningPortn_Type = EkiOnOff
_Pm10010mptAlmRxLaserOutputHighWarningPortn_Object = MibTableColumn
pm10010mptAlmRxLaserOutputHighWarningPortn = _Pm10010mptAlmRxLaserOutputHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 1, 120, 1, 12),
    _Pm10010mptAlmRxLaserOutputHighWarningPortn_Type()
)
pm10010mptAlmRxLaserOutputHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmRxLaserOutputHighWarningPortn.setStatus("current")
_Pm10010mptAlmRxLaserOutputHighAlarmPortn_Type = EkiOnOff
_Pm10010mptAlmRxLaserOutputHighAlarmPortn_Object = MibTableColumn
pm10010mptAlmRxLaserOutputHighAlarmPortn = _Pm10010mptAlmRxLaserOutputHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 1, 120, 1, 13),
    _Pm10010mptAlmRxLaserOutputHighAlarmPortn_Type()
)
pm10010mptAlmRxLaserOutputHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmRxLaserOutputHighAlarmPortn.setStatus("current")
_Pm10010mptAlmRxLaserBiasLowAlarmPortn_Type = EkiOnOff
_Pm10010mptAlmRxLaserBiasLowAlarmPortn_Object = MibTableColumn
pm10010mptAlmRxLaserBiasLowAlarmPortn = _Pm10010mptAlmRxLaserBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 1, 120, 1, 14),
    _Pm10010mptAlmRxLaserBiasLowAlarmPortn_Type()
)
pm10010mptAlmRxLaserBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmRxLaserBiasLowAlarmPortn.setStatus("current")
_Pm10010mptAlmRxLaserBiasLowWarningPortn_Type = EkiOnOff
_Pm10010mptAlmRxLaserBiasLowWarningPortn_Object = MibTableColumn
pm10010mptAlmRxLaserBiasLowWarningPortn = _Pm10010mptAlmRxLaserBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 1, 120, 1, 15),
    _Pm10010mptAlmRxLaserBiasLowWarningPortn_Type()
)
pm10010mptAlmRxLaserBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmRxLaserBiasLowWarningPortn.setStatus("current")
_Pm10010mptAlmRxLaserBiasHighWarningPortn_Type = EkiOnOff
_Pm10010mptAlmRxLaserBiasHighWarningPortn_Object = MibTableColumn
pm10010mptAlmRxLaserBiasHighWarningPortn = _Pm10010mptAlmRxLaserBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 1, 120, 1, 16),
    _Pm10010mptAlmRxLaserBiasHighWarningPortn_Type()
)
pm10010mptAlmRxLaserBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmRxLaserBiasHighWarningPortn.setStatus("current")
_Pm10010mptAlmRxLaserBiasHighAlarmPortn_Type = EkiOnOff
_Pm10010mptAlmRxLaserBiasHighAlarmPortn_Object = MibTableColumn
pm10010mptAlmRxLaserBiasHighAlarmPortn = _Pm10010mptAlmRxLaserBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 1, 120, 1, 17),
    _Pm10010mptAlmRxLaserBiasHighAlarmPortn_Type()
)
pm10010mptAlmRxLaserBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmRxLaserBiasHighAlarmPortn.setStatus("current")
_Pm10010mptAlmLineUrg_ObjectIdentity = ObjectIdentity
pm10010mptAlmLineUrg = _Pm10010mptAlmLineUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 2)
)
_Pm10010mptAlmlineNetworkLaneFaultTable_Object = MibTable
pm10010mptAlmlineNetworkLaneFaultTable = _Pm10010mptAlmlineNetworkLaneFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 2, 136)
)
if mibBuilder.loadTexts:
    pm10010mptAlmlineNetworkLaneFaultTable.setStatus("current")
_Pm10010mptAlmlineNetworkLaneFaultEntry_Object = MibTableRow
pm10010mptAlmlineNetworkLaneFaultEntry = _Pm10010mptAlmlineNetworkLaneFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 2, 136, 1)
)
pm10010mptAlmlineNetworkLaneFaultEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptAlmlineNetworkLaneFaultIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptAlmlineNetworkLaneFaultEntry.setStatus("current")


class _Pm10010mptAlmlineNetworkLaneFaultIndex_Type(Integer32):
    """Custom type pm10010mptAlmlineNetworkLaneFaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptAlmlineNetworkLaneFaultIndex_Type.__name__ = "Integer32"
_Pm10010mptAlmlineNetworkLaneFaultIndex_Object = MibTableColumn
pm10010mptAlmlineNetworkLaneFaultIndex = _Pm10010mptAlmlineNetworkLaneFaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 2, 136, 1, 1),
    _Pm10010mptAlmlineNetworkLaneFaultIndex_Type()
)
pm10010mptAlmlineNetworkLaneFaultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmlineNetworkLaneFaultIndex.setStatus("current")
_Pm10010mptAlmLineLaneRxTecFaultPortn_Type = EkiOnOff
_Pm10010mptAlmLineLaneRxTecFaultPortn_Object = MibTableColumn
pm10010mptAlmLineLaneRxTecFaultPortn = _Pm10010mptAlmLineLaneRxTecFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 2, 136, 1, 3),
    _Pm10010mptAlmLineLaneRxTecFaultPortn_Type()
)
pm10010mptAlmLineLaneRxTecFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmLineLaneRxTecFaultPortn.setStatus("current")
_Pm10010mptAlmLineLaneRxFifoErrorPortn_Type = EkiOnOff
_Pm10010mptAlmLineLaneRxFifoErrorPortn_Object = MibTableColumn
pm10010mptAlmLineLaneRxFifoErrorPortn = _Pm10010mptAlmLineLaneRxFifoErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 2, 136, 1, 4),
    _Pm10010mptAlmLineLaneRxFifoErrorPortn_Type()
)
pm10010mptAlmLineLaneRxFifoErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmLineLaneRxFifoErrorPortn.setStatus("current")
_Pm10010mptAlmLineLaneRxLolPortn_Type = EkiOnOff
_Pm10010mptAlmLineLaneRxLolPortn_Object = MibTableColumn
pm10010mptAlmLineLaneRxLolPortn = _Pm10010mptAlmLineLaneRxLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 2, 136, 1, 5),
    _Pm10010mptAlmLineLaneRxLolPortn_Type()
)
pm10010mptAlmLineLaneRxLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmLineLaneRxLolPortn.setStatus("current")
_Pm10010mptAlmLineLaneRxLosPortn_Type = EkiOnOff
_Pm10010mptAlmLineLaneRxLosPortn_Object = MibTableColumn
pm10010mptAlmLineLaneRxLosPortn = _Pm10010mptAlmLineLaneRxLosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 2, 136, 1, 6),
    _Pm10010mptAlmLineLaneRxLosPortn_Type()
)
pm10010mptAlmLineLaneRxLosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmLineLaneRxLosPortn.setStatus("current")
_Pm10010mptAlmLineLaneTxLolPortn_Type = EkiOnOff
_Pm10010mptAlmLineLaneTxLolPortn_Object = MibTableColumn
pm10010mptAlmLineLaneTxLolPortn = _Pm10010mptAlmLineLaneTxLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 2, 136, 1, 8),
    _Pm10010mptAlmLineLaneTxLolPortn_Type()
)
pm10010mptAlmLineLaneTxLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmLineLaneTxLolPortn.setStatus("current")
_Pm10010mptAlmLineLaneTxLosfPortn_Type = EkiOnOff
_Pm10010mptAlmLineLaneTxLosfPortn_Object = MibTableColumn
pm10010mptAlmLineLaneTxLosfPortn = _Pm10010mptAlmLineLaneTxLosfPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 2, 136, 1, 9),
    _Pm10010mptAlmLineLaneTxLosfPortn_Type()
)
pm10010mptAlmLineLaneTxLosfPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmLineLaneTxLosfPortn.setStatus("current")
_Pm10010mptAlmLineLaneApdPowerSupplyPortn_Type = EkiOnOff
_Pm10010mptAlmLineLaneApdPowerSupplyPortn_Object = MibTableColumn
pm10010mptAlmLineLaneApdPowerSupplyPortn = _Pm10010mptAlmLineLaneApdPowerSupplyPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 2, 136, 1, 15),
    _Pm10010mptAlmLineLaneApdPowerSupplyPortn_Type()
)
pm10010mptAlmLineLaneApdPowerSupplyPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmLineLaneApdPowerSupplyPortn.setStatus("current")
_Pm10010mptAlmLineLaneWavelengthUnlockedPortn_Type = EkiOnOff
_Pm10010mptAlmLineLaneWavelengthUnlockedPortn_Object = MibTableColumn
pm10010mptAlmLineLaneWavelengthUnlockedPortn = _Pm10010mptAlmLineLaneWavelengthUnlockedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 2, 136, 1, 16),
    _Pm10010mptAlmLineLaneWavelengthUnlockedPortn_Type()
)
pm10010mptAlmLineLaneWavelengthUnlockedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmLineLaneWavelengthUnlockedPortn.setStatus("current")
_Pm10010mptAlmLineLaneTecFaultPortn_Type = EkiOnOff
_Pm10010mptAlmLineLaneTecFaultPortn_Object = MibTableColumn
pm10010mptAlmLineLaneTecFaultPortn = _Pm10010mptAlmLineLaneTecFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 2, 136, 1, 17),
    _Pm10010mptAlmLineLaneTecFaultPortn_Type()
)
pm10010mptAlmLineLaneTecFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmLineLaneTecFaultPortn.setStatus("current")
_Pm10010mptAlmlineHostLaneFaultTable_Object = MibTable
pm10010mptAlmlineHostLaneFaultTable = _Pm10010mptAlmlineHostLaneFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 2, 152)
)
if mibBuilder.loadTexts:
    pm10010mptAlmlineHostLaneFaultTable.setStatus("current")
_Pm10010mptAlmlineHostLaneFaultEntry_Object = MibTableRow
pm10010mptAlmlineHostLaneFaultEntry = _Pm10010mptAlmlineHostLaneFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 2, 152, 1)
)
pm10010mptAlmlineHostLaneFaultEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptAlmlineHostLaneFaultIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptAlmlineHostLaneFaultEntry.setStatus("current")


class _Pm10010mptAlmlineHostLaneFaultIndex_Type(Integer32):
    """Custom type pm10010mptAlmlineHostLaneFaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptAlmlineHostLaneFaultIndex_Type.__name__ = "Integer32"
_Pm10010mptAlmlineHostLaneFaultIndex_Object = MibTableColumn
pm10010mptAlmlineHostLaneFaultIndex = _Pm10010mptAlmlineHostLaneFaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 2, 152, 1, 1),
    _Pm10010mptAlmlineHostLaneFaultIndex_Type()
)
pm10010mptAlmlineHostLaneFaultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmlineHostLaneFaultIndex.setStatus("current")
_Pm10010mptAlmLineInputLossOfSignalPortn_Type = EkiOnOff
_Pm10010mptAlmLineInputLossOfSignalPortn_Object = MibTableColumn
pm10010mptAlmLineInputLossOfSignalPortn = _Pm10010mptAlmLineInputLossOfSignalPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 2, 152, 1, 2),
    _Pm10010mptAlmLineInputLossOfSignalPortn_Type()
)
pm10010mptAlmLineInputLossOfSignalPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmLineInputLossOfSignalPortn.setStatus("current")
_Pm10010mptAlmLineLossOfFramePortn_Type = EkiOnOff
_Pm10010mptAlmLineLossOfFramePortn_Object = MibTableColumn
pm10010mptAlmLineLossOfFramePortn = _Pm10010mptAlmLineLossOfFramePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 2, 152, 1, 3),
    _Pm10010mptAlmLineLossOfFramePortn_Type()
)
pm10010mptAlmLineLossOfFramePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmLineLossOfFramePortn.setStatus("current")
_Pm10010mptAlmLineSmBdiInsertedPortn_Type = EkiOnOff
_Pm10010mptAlmLineSmBdiInsertedPortn_Object = MibTableColumn
pm10010mptAlmLineSmBdiInsertedPortn = _Pm10010mptAlmLineSmBdiInsertedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 2, 152, 1, 4),
    _Pm10010mptAlmLineSmBdiInsertedPortn_Type()
)
pm10010mptAlmLineSmBdiInsertedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmLineSmBdiInsertedPortn.setStatus("current")
_Pm10010mptAlmLineSmBdiDetectedPortn_Type = EkiOnOff
_Pm10010mptAlmLineSmBdiDetectedPortn_Object = MibTableColumn
pm10010mptAlmLineSmBdiDetectedPortn = _Pm10010mptAlmLineSmBdiDetectedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 2, 152, 1, 5),
    _Pm10010mptAlmLineSmBdiDetectedPortn_Type()
)
pm10010mptAlmLineSmBdiDetectedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmLineSmBdiDetectedPortn.setStatus("current")
_Pm10010mptAlmLineSmIaeInsertedPortn_Type = EkiOnOff
_Pm10010mptAlmLineSmIaeInsertedPortn_Object = MibTableColumn
pm10010mptAlmLineSmIaeInsertedPortn = _Pm10010mptAlmLineSmIaeInsertedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 2, 152, 1, 6),
    _Pm10010mptAlmLineSmIaeInsertedPortn_Type()
)
pm10010mptAlmLineSmIaeInsertedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmLineSmIaeInsertedPortn.setStatus("current")
_Pm10010mptAlmLineSmIaeDetectedPortn_Type = EkiOnOff
_Pm10010mptAlmLineSmIaeDetectedPortn_Object = MibTableColumn
pm10010mptAlmLineSmIaeDetectedPortn = _Pm10010mptAlmLineSmIaeDetectedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 2, 152, 1, 7),
    _Pm10010mptAlmLineSmIaeDetectedPortn_Type()
)
pm10010mptAlmLineSmIaeDetectedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmLineSmIaeDetectedPortn.setStatus("current")
_Pm10010mptAlmLineTxHostLolPortn_Type = EkiOnOff
_Pm10010mptAlmLineTxHostLolPortn_Object = MibTableColumn
pm10010mptAlmLineTxHostLolPortn = _Pm10010mptAlmLineTxHostLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 2, 152, 1, 10),
    _Pm10010mptAlmLineTxHostLolPortn_Type()
)
pm10010mptAlmLineTxHostLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmLineTxHostLolPortn.setStatus("current")
_Pm10010mptAlmLineLaneTxFifoErrorPortn_Type = EkiOnOff
_Pm10010mptAlmLineLaneTxFifoErrorPortn_Object = MibTableColumn
pm10010mptAlmLineLaneTxFifoErrorPortn = _Pm10010mptAlmLineLaneTxFifoErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 2, 152, 1, 11),
    _Pm10010mptAlmLineLaneTxFifoErrorPortn_Type()
)
pm10010mptAlmLineLaneTxFifoErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmLineLaneTxFifoErrorPortn.setStatus("current")
_Pm10010mptAlmLinePowerDegradePortn_Type = EkiOnOff
_Pm10010mptAlmLinePowerDegradePortn_Object = MibTableColumn
pm10010mptAlmLinePowerDegradePortn = _Pm10010mptAlmLinePowerDegradePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 2, 152, 1, 16),
    _Pm10010mptAlmLinePowerDegradePortn_Type()
)
pm10010mptAlmLinePowerDegradePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmLinePowerDegradePortn.setStatus("current")
_Pm10010mptAlmLineTrxOverTempPortn_Type = EkiOnOff
_Pm10010mptAlmLineTrxOverTempPortn_Object = MibTableColumn
pm10010mptAlmLineTrxOverTempPortn = _Pm10010mptAlmLineTrxOverTempPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 2, 152, 1, 17),
    _Pm10010mptAlmLineTrxOverTempPortn_Type()
)
pm10010mptAlmLineTrxOverTempPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmLineTrxOverTempPortn.setStatus("current")
_Pm10010mptAlmlineNetworkLaneRxOtnTable_Object = MibTable
pm10010mptAlmlineNetworkLaneRxOtnTable = _Pm10010mptAlmlineNetworkLaneRxOtnTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 2, 168)
)
if mibBuilder.loadTexts:
    pm10010mptAlmlineNetworkLaneRxOtnTable.setStatus("current")
_Pm10010mptAlmlineNetworkLaneRxOtnEntry_Object = MibTableRow
pm10010mptAlmlineNetworkLaneRxOtnEntry = _Pm10010mptAlmlineNetworkLaneRxOtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 2, 168, 1)
)
pm10010mptAlmlineNetworkLaneRxOtnEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptAlmlineNetworkLaneRxOtnIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptAlmlineNetworkLaneRxOtnEntry.setStatus("current")


class _Pm10010mptAlmlineNetworkLaneRxOtnIndex_Type(Integer32):
    """Custom type pm10010mptAlmlineNetworkLaneRxOtnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptAlmlineNetworkLaneRxOtnIndex_Type.__name__ = "Integer32"
_Pm10010mptAlmlineNetworkLaneRxOtnIndex_Object = MibTableColumn
pm10010mptAlmlineNetworkLaneRxOtnIndex = _Pm10010mptAlmlineNetworkLaneRxOtnIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 2, 168, 1, 1),
    _Pm10010mptAlmlineNetworkLaneRxOtnIndex_Type()
)
pm10010mptAlmlineNetworkLaneRxOtnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmlineNetworkLaneRxOtnIndex.setStatus("current")
_Pm10010mptAlmLineRxOtnOduAisPortn_Type = EkiOnOff
_Pm10010mptAlmLineRxOtnOduAisPortn_Object = MibTableColumn
pm10010mptAlmLineRxOtnOduAisPortn = _Pm10010mptAlmLineRxOtnOduAisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 2, 168, 1, 10),
    _Pm10010mptAlmLineRxOtnOduAisPortn_Type()
)
pm10010mptAlmLineRxOtnOduAisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmLineRxOtnOduAisPortn.setStatus("current")
_Pm10010mptAlmLineRxOtnOtuAisPortn_Type = EkiOnOff
_Pm10010mptAlmLineRxOtnOtuAisPortn_Object = MibTableColumn
pm10010mptAlmLineRxOtnOtuAisPortn = _Pm10010mptAlmLineRxOtnOtuAisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 2, 168, 1, 11),
    _Pm10010mptAlmLineRxOtnOtuAisPortn_Type()
)
pm10010mptAlmLineRxOtnOtuAisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmLineRxOtnOtuAisPortn.setStatus("current")
_Pm10010mptAlmLineRxSmBdiPortn_Type = EkiOnOff
_Pm10010mptAlmLineRxSmBdiPortn_Object = MibTableColumn
pm10010mptAlmLineRxSmBdiPortn = _Pm10010mptAlmLineRxSmBdiPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 2, 168, 1, 12),
    _Pm10010mptAlmLineRxSmBdiPortn_Type()
)
pm10010mptAlmLineRxSmBdiPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmLineRxSmBdiPortn.setStatus("current")
_Pm10010mptAlmLineRxOtnIaePortn_Type = EkiOnOff
_Pm10010mptAlmLineRxOtnIaePortn_Object = MibTableColumn
pm10010mptAlmLineRxOtnIaePortn = _Pm10010mptAlmLineRxOtnIaePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 2, 168, 1, 13),
    _Pm10010mptAlmLineRxOtnIaePortn_Type()
)
pm10010mptAlmLineRxOtnIaePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmLineRxOtnIaePortn.setStatus("current")
_Pm10010mptAlmLineRxOtnOomPortn_Type = EkiOnOff
_Pm10010mptAlmLineRxOtnOomPortn_Object = MibTableColumn
pm10010mptAlmLineRxOtnOomPortn = _Pm10010mptAlmLineRxOtnOomPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 2, 168, 1, 14),
    _Pm10010mptAlmLineRxOtnOomPortn_Type()
)
pm10010mptAlmLineRxOtnOomPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmLineRxOtnOomPortn.setStatus("current")
_Pm10010mptAlmLineRxOtnLomPortn_Type = EkiOnOff
_Pm10010mptAlmLineRxOtnLomPortn_Object = MibTableColumn
pm10010mptAlmLineRxOtnLomPortn = _Pm10010mptAlmLineRxOtnLomPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 2, 168, 1, 15),
    _Pm10010mptAlmLineRxOtnLomPortn_Type()
)
pm10010mptAlmLineRxOtnLomPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmLineRxOtnLomPortn.setStatus("current")
_Pm10010mptAlmLineRxOtnOofPortn_Type = EkiOnOff
_Pm10010mptAlmLineRxOtnOofPortn_Object = MibTableColumn
pm10010mptAlmLineRxOtnOofPortn = _Pm10010mptAlmLineRxOtnOofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 2, 168, 1, 16),
    _Pm10010mptAlmLineRxOtnOofPortn_Type()
)
pm10010mptAlmLineRxOtnOofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmLineRxOtnOofPortn.setStatus("current")
_Pm10010mptAlmLineRxOtnLofPortn_Type = EkiOnOff
_Pm10010mptAlmLineRxOtnLofPortn_Object = MibTableColumn
pm10010mptAlmLineRxOtnLofPortn = _Pm10010mptAlmLineRxOtnLofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 2, 168, 1, 17),
    _Pm10010mptAlmLineRxOtnLofPortn_Type()
)
pm10010mptAlmLineRxOtnLofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmLineRxOtnLofPortn.setStatus("current")
_Pm10010mptAlmlineHostLaneTxOtnTable_Object = MibTable
pm10010mptAlmlineHostLaneTxOtnTable = _Pm10010mptAlmlineHostLaneTxOtnTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 2, 184)
)
if mibBuilder.loadTexts:
    pm10010mptAlmlineHostLaneTxOtnTable.setStatus("current")
_Pm10010mptAlmlineHostLaneTxOtnEntry_Object = MibTableRow
pm10010mptAlmlineHostLaneTxOtnEntry = _Pm10010mptAlmlineHostLaneTxOtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 2, 184, 1)
)
pm10010mptAlmlineHostLaneTxOtnEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptAlmlineHostLaneTxOtnIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptAlmlineHostLaneTxOtnEntry.setStatus("current")


class _Pm10010mptAlmlineHostLaneTxOtnIndex_Type(Integer32):
    """Custom type pm10010mptAlmlineHostLaneTxOtnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptAlmlineHostLaneTxOtnIndex_Type.__name__ = "Integer32"
_Pm10010mptAlmlineHostLaneTxOtnIndex_Object = MibTableColumn
pm10010mptAlmlineHostLaneTxOtnIndex = _Pm10010mptAlmlineHostLaneTxOtnIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 2, 184, 1, 1),
    _Pm10010mptAlmlineHostLaneTxOtnIndex_Type()
)
pm10010mptAlmlineHostLaneTxOtnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmlineHostLaneTxOtnIndex.setStatus("current")
_Pm10010mptAlmLineTxOtnOduAisPortn_Type = EkiOnOff
_Pm10010mptAlmLineTxOtnOduAisPortn_Object = MibTableColumn
pm10010mptAlmLineTxOtnOduAisPortn = _Pm10010mptAlmLineTxOtnOduAisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 2, 184, 1, 10),
    _Pm10010mptAlmLineTxOtnOduAisPortn_Type()
)
pm10010mptAlmLineTxOtnOduAisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmLineTxOtnOduAisPortn.setStatus("current")
_Pm10010mptAlmLineTxOtnOtuAisPortn_Type = EkiOnOff
_Pm10010mptAlmLineTxOtnOtuAisPortn_Object = MibTableColumn
pm10010mptAlmLineTxOtnOtuAisPortn = _Pm10010mptAlmLineTxOtnOtuAisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 2, 184, 1, 11),
    _Pm10010mptAlmLineTxOtnOtuAisPortn_Type()
)
pm10010mptAlmLineTxOtnOtuAisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmLineTxOtnOtuAisPortn.setStatus("current")
_Pm10010mptAlmLineTxSmBdiPortn_Type = EkiOnOff
_Pm10010mptAlmLineTxSmBdiPortn_Object = MibTableColumn
pm10010mptAlmLineTxSmBdiPortn = _Pm10010mptAlmLineTxSmBdiPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 2, 184, 1, 12),
    _Pm10010mptAlmLineTxSmBdiPortn_Type()
)
pm10010mptAlmLineTxSmBdiPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmLineTxSmBdiPortn.setStatus("current")
_Pm10010mptAlmLineTxOtnIaePortn_Type = EkiOnOff
_Pm10010mptAlmLineTxOtnIaePortn_Object = MibTableColumn
pm10010mptAlmLineTxOtnIaePortn = _Pm10010mptAlmLineTxOtnIaePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 2, 184, 1, 13),
    _Pm10010mptAlmLineTxOtnIaePortn_Type()
)
pm10010mptAlmLineTxOtnIaePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmLineTxOtnIaePortn.setStatus("current")
_Pm10010mptAlmLineTxOtnOomPortn_Type = EkiOnOff
_Pm10010mptAlmLineTxOtnOomPortn_Object = MibTableColumn
pm10010mptAlmLineTxOtnOomPortn = _Pm10010mptAlmLineTxOtnOomPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 2, 184, 1, 14),
    _Pm10010mptAlmLineTxOtnOomPortn_Type()
)
pm10010mptAlmLineTxOtnOomPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmLineTxOtnOomPortn.setStatus("current")
_Pm10010mptAlmLineTxOtnLomPortn_Type = EkiOnOff
_Pm10010mptAlmLineTxOtnLomPortn_Object = MibTableColumn
pm10010mptAlmLineTxOtnLomPortn = _Pm10010mptAlmLineTxOtnLomPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 2, 184, 1, 15),
    _Pm10010mptAlmLineTxOtnLomPortn_Type()
)
pm10010mptAlmLineTxOtnLomPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmLineTxOtnLomPortn.setStatus("current")
_Pm10010mptAlmLineTxOtnOofPortn_Type = EkiOnOff
_Pm10010mptAlmLineTxOtnOofPortn_Object = MibTableColumn
pm10010mptAlmLineTxOtnOofPortn = _Pm10010mptAlmLineTxOtnOofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 2, 184, 1, 16),
    _Pm10010mptAlmLineTxOtnOofPortn_Type()
)
pm10010mptAlmLineTxOtnOofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmLineTxOtnOofPortn.setStatus("current")
_Pm10010mptAlmLineTxOtnLofPortn_Type = EkiOnOff
_Pm10010mptAlmLineTxOtnLofPortn_Object = MibTableColumn
pm10010mptAlmLineTxOtnLofPortn = _Pm10010mptAlmLineTxOtnLofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 2, 184, 1, 17),
    _Pm10010mptAlmLineTxOtnLofPortn_Type()
)
pm10010mptAlmLineTxOtnLofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmLineTxOtnLofPortn.setStatus("current")
_Pm10010mptAlmLineCrit_ObjectIdentity = ObjectIdentity
pm10010mptAlmLineCrit = _Pm10010mptAlmLineCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 3)
)
_Pm10010mptAlmsynthAlmLineTable_Object = MibTable
pm10010mptAlmsynthAlmLineTable = _Pm10010mptAlmsynthAlmLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 3, 24)
)
if mibBuilder.loadTexts:
    pm10010mptAlmsynthAlmLineTable.setStatus("current")
_Pm10010mptAlmsynthAlmLineEntry_Object = MibTableRow
pm10010mptAlmsynthAlmLineEntry = _Pm10010mptAlmsynthAlmLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 3, 24, 1)
)
pm10010mptAlmsynthAlmLineEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptAlmsynthAlmLineIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptAlmsynthAlmLineEntry.setStatus("current")


class _Pm10010mptAlmsynthAlmLineIndex_Type(Integer32):
    """Custom type pm10010mptAlmsynthAlmLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptAlmsynthAlmLineIndex_Type.__name__ = "Integer32"
_Pm10010mptAlmsynthAlmLineIndex_Object = MibTableColumn
pm10010mptAlmsynthAlmLineIndex = _Pm10010mptAlmsynthAlmLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 3, 24, 1, 1),
    _Pm10010mptAlmsynthAlmLineIndex_Type()
)
pm10010mptAlmsynthAlmLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmsynthAlmLineIndex.setStatus("current")
_Pm10010mptAlmXfpAbsentPortn_Type = EkiOnOff
_Pm10010mptAlmXfpAbsentPortn_Object = MibTableColumn
pm10010mptAlmXfpAbsentPortn = _Pm10010mptAlmXfpAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 3, 24, 1, 2),
    _Pm10010mptAlmXfpAbsentPortn_Type()
)
pm10010mptAlmXfpAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmXfpAbsentPortn.setStatus("current")
_Pm10010mptAlmXfpInitNotComplPortn_Type = EkiOnOff
_Pm10010mptAlmXfpInitNotComplPortn_Object = MibTableColumn
pm10010mptAlmXfpInitNotComplPortn = _Pm10010mptAlmXfpInitNotComplPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 3, 24, 1, 3),
    _Pm10010mptAlmXfpInitNotComplPortn_Type()
)
pm10010mptAlmXfpInitNotComplPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmXfpInitNotComplPortn.setStatus("current")
_Pm10010mptAlmLineHwFailPortn_Type = EkiOnOff
_Pm10010mptAlmLineHwFailPortn_Object = MibTableColumn
pm10010mptAlmLineHwFailPortn = _Pm10010mptAlmLineHwFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 3, 24, 1, 5),
    _Pm10010mptAlmLineHwFailPortn_Type()
)
pm10010mptAlmLineHwFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmLineHwFailPortn.setStatus("current")
_Pm10010mptAlmXfpTxOffPortn_Type = EkiOnOff
_Pm10010mptAlmXfpTxOffPortn_Object = MibTableColumn
pm10010mptAlmXfpTxOffPortn = _Pm10010mptAlmXfpTxOffPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 3, 24, 1, 6),
    _Pm10010mptAlmXfpTxOffPortn_Type()
)
pm10010mptAlmXfpTxOffPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmXfpTxOffPortn.setStatus("current")
_Pm10010mptAlmLineLocalOosPortn_Type = EkiOnOff
_Pm10010mptAlmLineLocalOosPortn_Object = MibTableColumn
pm10010mptAlmLineLocalOosPortn = _Pm10010mptAlmLineLocalOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 3, 24, 1, 7),
    _Pm10010mptAlmLineLocalOosPortn_Type()
)
pm10010mptAlmLineLocalOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmLineLocalOosPortn.setStatus("current")
_Pm10010mptAlmUpRdiInsPortn_Type = EkiOnOff
_Pm10010mptAlmUpRdiInsPortn_Object = MibTableColumn
pm10010mptAlmUpRdiInsPortn = _Pm10010mptAlmUpRdiInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 3, 24, 1, 9),
    _Pm10010mptAlmUpRdiInsPortn_Type()
)
pm10010mptAlmUpRdiInsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmUpRdiInsPortn.setStatus("current")
_Pm10010mptAlmLineDdmWarningPortn_Type = EkiOnOff
_Pm10010mptAlmLineDdmWarningPortn_Object = MibTableColumn
pm10010mptAlmLineDdmWarningPortn = _Pm10010mptAlmLineDdmWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 3, 24, 1, 10),
    _Pm10010mptAlmLineDdmWarningPortn_Type()
)
pm10010mptAlmLineDdmWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmLineDdmWarningPortn.setStatus("current")
_Pm10010mptAlmLineDdmAlmPortn_Type = EkiOnOff
_Pm10010mptAlmLineDdmAlmPortn_Object = MibTableColumn
pm10010mptAlmLineDdmAlmPortn = _Pm10010mptAlmLineDdmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 3, 24, 1, 11),
    _Pm10010mptAlmLineDdmAlmPortn_Type()
)
pm10010mptAlmLineDdmAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmLineDdmAlmPortn.setStatus("current")
_Pm10010mptAlmLineFailPortn_Type = EkiOnOff
_Pm10010mptAlmLineFailPortn_Object = MibTableColumn
pm10010mptAlmLineFailPortn = _Pm10010mptAlmLineFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 3, 24, 1, 13),
    _Pm10010mptAlmLineFailPortn_Type()
)
pm10010mptAlmLineFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmLineFailPortn.setStatus("current")
_Pm10010mptAlmLineActivePortn_Type = EkiOnOff
_Pm10010mptAlmLineActivePortn_Object = MibTableColumn
pm10010mptAlmLineActivePortn = _Pm10010mptAlmLineActivePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 2, 3, 3, 24, 1, 17),
    _Pm10010mptAlmLineActivePortn_Type()
)
pm10010mptAlmLineActivePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptAlmLineActivePortn.setStatus("current")
_Pm10010mptmeasures_ObjectIdentity = ObjectIdentity
pm10010mptmeasures = _Pm10010mptmeasures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3)
)
_Pm10010mptMesrOther_ObjectIdentity = ObjectIdentity
pm10010mptMesrOther = _Pm10010mptMesrOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 1)
)
_Pm10010mptMesrsynth0_Type = EkiMeasureType
_Pm10010mptMesrsynth0_Object = MibScalar
pm10010mptMesrsynth0 = _Pm10010mptMesrsynth0_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 1, 0),
    _Pm10010mptMesrsynth0_Type()
)
pm10010mptMesrsynth0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrsynth0.setStatus("deprecated")
_Pm10010mptMesrsynth1_Type = EkiMeasureType
_Pm10010mptMesrsynth1_Object = MibScalar
pm10010mptMesrsynth1 = _Pm10010mptMesrsynth1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 1, 1),
    _Pm10010mptMesrsynth1_Type()
)
pm10010mptMesrsynth1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrsynth1.setStatus("deprecated")


class _Pm10010mptMesrpmIntervalNumber_Type(Unsigned32):
    """Custom type pm10010mptMesrpmIntervalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mptMesrpmIntervalNumber_Type.__name__ = "Unsigned32"
_Pm10010mptMesrpmIntervalNumber_Object = MibScalar
pm10010mptMesrpmIntervalNumber = _Pm10010mptMesrpmIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 1, 7),
    _Pm10010mptMesrpmIntervalNumber_Type()
)
pm10010mptMesrpmIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrpmIntervalNumber.setStatus("current")


class _Pm10010mptMesrlineNetTxLaserOutputPwrAverage_Type(Unsigned32):
    """Custom type pm10010mptMesrlineNetTxLaserOutputPwrAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mptMesrlineNetTxLaserOutputPwrAverage_Type.__name__ = "Unsigned32"
_Pm10010mptMesrlineNetTxLaserOutputPwrAverage_Object = MibScalar
pm10010mptMesrlineNetTxLaserOutputPwrAverage = _Pm10010mptMesrlineNetTxLaserOutputPwrAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 1, 180),
    _Pm10010mptMesrlineNetTxLaserOutputPwrAverage_Type()
)
pm10010mptMesrlineNetTxLaserOutputPwrAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrlineNetTxLaserOutputPwrAverage.setStatus("current")


class _Pm10010mptMesrlineNetTxLaserTempAverage_Type(Unsigned32):
    """Custom type pm10010mptMesrlineNetTxLaserTempAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mptMesrlineNetTxLaserTempAverage_Type.__name__ = "Unsigned32"
_Pm10010mptMesrlineNetTxLaserTempAverage_Object = MibScalar
pm10010mptMesrlineNetTxLaserTempAverage = _Pm10010mptMesrlineNetTxLaserTempAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 1, 181),
    _Pm10010mptMesrlineNetTxLaserTempAverage_Type()
)
pm10010mptMesrlineNetTxLaserTempAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrlineNetTxLaserTempAverage.setStatus("current")


class _Pm10010mptMesrlineNetTxBiasCurrentAverage_Type(Unsigned32):
    """Custom type pm10010mptMesrlineNetTxBiasCurrentAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mptMesrlineNetTxBiasCurrentAverage_Type.__name__ = "Unsigned32"
_Pm10010mptMesrlineNetTxBiasCurrentAverage_Object = MibScalar
pm10010mptMesrlineNetTxBiasCurrentAverage = _Pm10010mptMesrlineNetTxBiasCurrentAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 1, 182),
    _Pm10010mptMesrlineNetTxBiasCurrentAverage_Type()
)
pm10010mptMesrlineNetTxBiasCurrentAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrlineNetTxBiasCurrentAverage.setStatus("current")


class _Pm10010mptMesrlineNetRxInputPwrAverage_Type(Unsigned32):
    """Custom type pm10010mptMesrlineNetRxInputPwrAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mptMesrlineNetRxInputPwrAverage_Type.__name__ = "Unsigned32"
_Pm10010mptMesrlineNetRxInputPwrAverage_Object = MibScalar
pm10010mptMesrlineNetRxInputPwrAverage = _Pm10010mptMesrlineNetRxInputPwrAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 1, 183),
    _Pm10010mptMesrlineNetRxInputPwrAverage_Type()
)
pm10010mptMesrlineNetRxInputPwrAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrlineNetRxInputPwrAverage.setStatus("current")


class _Pm10010mptMesrlineResidualChromaticDispAverage_Type(Unsigned32):
    """Custom type pm10010mptMesrlineResidualChromaticDispAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mptMesrlineResidualChromaticDispAverage_Type.__name__ = "Unsigned32"
_Pm10010mptMesrlineResidualChromaticDispAverage_Object = MibScalar
pm10010mptMesrlineResidualChromaticDispAverage = _Pm10010mptMesrlineResidualChromaticDispAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 1, 184),
    _Pm10010mptMesrlineResidualChromaticDispAverage_Type()
)
pm10010mptMesrlineResidualChromaticDispAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrlineResidualChromaticDispAverage.setStatus("current")


class _Pm10010mptMesrlineDiffGroupDelayAverage_Type(Unsigned32):
    """Custom type pm10010mptMesrlineDiffGroupDelayAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mptMesrlineDiffGroupDelayAverage_Type.__name__ = "Unsigned32"
_Pm10010mptMesrlineDiffGroupDelayAverage_Object = MibScalar
pm10010mptMesrlineDiffGroupDelayAverage = _Pm10010mptMesrlineDiffGroupDelayAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 1, 185),
    _Pm10010mptMesrlineDiffGroupDelayAverage_Type()
)
pm10010mptMesrlineDiffGroupDelayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrlineDiffGroupDelayAverage.setStatus("current")


class _Pm10010mptMesrlineQFactorAverage_Type(Unsigned32):
    """Custom type pm10010mptMesrlineQFactorAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mptMesrlineQFactorAverage_Type.__name__ = "Unsigned32"
_Pm10010mptMesrlineQFactorAverage_Object = MibScalar
pm10010mptMesrlineQFactorAverage = _Pm10010mptMesrlineQFactorAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 1, 186),
    _Pm10010mptMesrlineQFactorAverage_Type()
)
pm10010mptMesrlineQFactorAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrlineQFactorAverage.setStatus("current")


class _Pm10010mptMesrlineCarrierFreqOffsetAverage_Type(Unsigned32):
    """Custom type pm10010mptMesrlineCarrierFreqOffsetAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mptMesrlineCarrierFreqOffsetAverage_Type.__name__ = "Unsigned32"
_Pm10010mptMesrlineCarrierFreqOffsetAverage_Object = MibScalar
pm10010mptMesrlineCarrierFreqOffsetAverage = _Pm10010mptMesrlineCarrierFreqOffsetAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 1, 187),
    _Pm10010mptMesrlineCarrierFreqOffsetAverage_Type()
)
pm10010mptMesrlineCarrierFreqOffsetAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrlineCarrierFreqOffsetAverage.setStatus("current")


class _Pm10010mptMesrlineOsnrAverage_Type(Unsigned32):
    """Custom type pm10010mptMesrlineOsnrAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mptMesrlineOsnrAverage_Type.__name__ = "Unsigned32"
_Pm10010mptMesrlineOsnrAverage_Object = MibScalar
pm10010mptMesrlineOsnrAverage = _Pm10010mptMesrlineOsnrAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 1, 188),
    _Pm10010mptMesrlineOsnrAverage_Type()
)
pm10010mptMesrlineOsnrAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrlineOsnrAverage.setStatus("current")


class _Pm10010mptMesrclientNetTxTempMin_Type(Unsigned32):
    """Custom type pm10010mptMesrclientNetTxTempMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mptMesrclientNetTxTempMin_Type.__name__ = "Unsigned32"
_Pm10010mptMesrclientNetTxTempMin_Object = MibScalar
pm10010mptMesrclientNetTxTempMin = _Pm10010mptMesrclientNetTxTempMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 1, 192),
    _Pm10010mptMesrclientNetTxTempMin_Type()
)
pm10010mptMesrclientNetTxTempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrclientNetTxTempMin.setStatus("current")


class _Pm10010mptMesrclientNetTxBiasMin_Type(Unsigned32):
    """Custom type pm10010mptMesrclientNetTxBiasMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mptMesrclientNetTxBiasMin_Type.__name__ = "Unsigned32"
_Pm10010mptMesrclientNetTxBiasMin_Object = MibScalar
pm10010mptMesrclientNetTxBiasMin = _Pm10010mptMesrclientNetTxBiasMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 1, 193),
    _Pm10010mptMesrclientNetTxBiasMin_Type()
)
pm10010mptMesrclientNetTxBiasMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrclientNetTxBiasMin.setStatus("current")


class _Pm10010mptMesrclientNetTxPwrMin_Type(Unsigned32):
    """Custom type pm10010mptMesrclientNetTxPwrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mptMesrclientNetTxPwrMin_Type.__name__ = "Unsigned32"
_Pm10010mptMesrclientNetTxPwrMin_Object = MibScalar
pm10010mptMesrclientNetTxPwrMin = _Pm10010mptMesrclientNetTxPwrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 1, 194),
    _Pm10010mptMesrclientNetTxPwrMin_Type()
)
pm10010mptMesrclientNetTxPwrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrclientNetTxPwrMin.setStatus("current")


class _Pm10010mptMesrclientNetRxPwrMin_Type(Unsigned32):
    """Custom type pm10010mptMesrclientNetRxPwrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mptMesrclientNetRxPwrMin_Type.__name__ = "Unsigned32"
_Pm10010mptMesrclientNetRxPwrMin_Object = MibScalar
pm10010mptMesrclientNetRxPwrMin = _Pm10010mptMesrclientNetRxPwrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 1, 195),
    _Pm10010mptMesrclientNetRxPwrMin_Type()
)
pm10010mptMesrclientNetRxPwrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrclientNetRxPwrMin.setStatus("current")


class _Pm10010mptMesrlineNetTxLaserOutputPwrMin_Type(Unsigned32):
    """Custom type pm10010mptMesrlineNetTxLaserOutputPwrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mptMesrlineNetTxLaserOutputPwrMin_Type.__name__ = "Unsigned32"
_Pm10010mptMesrlineNetTxLaserOutputPwrMin_Object = MibScalar
pm10010mptMesrlineNetTxLaserOutputPwrMin = _Pm10010mptMesrlineNetTxLaserOutputPwrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 1, 196),
    _Pm10010mptMesrlineNetTxLaserOutputPwrMin_Type()
)
pm10010mptMesrlineNetTxLaserOutputPwrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrlineNetTxLaserOutputPwrMin.setStatus("current")


class _Pm10010mptMesrlineNetTxLaserTempMin_Type(Unsigned32):
    """Custom type pm10010mptMesrlineNetTxLaserTempMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mptMesrlineNetTxLaserTempMin_Type.__name__ = "Unsigned32"
_Pm10010mptMesrlineNetTxLaserTempMin_Object = MibScalar
pm10010mptMesrlineNetTxLaserTempMin = _Pm10010mptMesrlineNetTxLaserTempMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 1, 197),
    _Pm10010mptMesrlineNetTxLaserTempMin_Type()
)
pm10010mptMesrlineNetTxLaserTempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrlineNetTxLaserTempMin.setStatus("current")


class _Pm10010mptMesrlineNetTxBiasCurrentMin_Type(Unsigned32):
    """Custom type pm10010mptMesrlineNetTxBiasCurrentMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mptMesrlineNetTxBiasCurrentMin_Type.__name__ = "Unsigned32"
_Pm10010mptMesrlineNetTxBiasCurrentMin_Object = MibScalar
pm10010mptMesrlineNetTxBiasCurrentMin = _Pm10010mptMesrlineNetTxBiasCurrentMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 1, 198),
    _Pm10010mptMesrlineNetTxBiasCurrentMin_Type()
)
pm10010mptMesrlineNetTxBiasCurrentMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrlineNetTxBiasCurrentMin.setStatus("current")


class _Pm10010mptMesrlineNetRxInputPwrMin_Type(Unsigned32):
    """Custom type pm10010mptMesrlineNetRxInputPwrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mptMesrlineNetRxInputPwrMin_Type.__name__ = "Unsigned32"
_Pm10010mptMesrlineNetRxInputPwrMin_Object = MibScalar
pm10010mptMesrlineNetRxInputPwrMin = _Pm10010mptMesrlineNetRxInputPwrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 1, 199),
    _Pm10010mptMesrlineNetRxInputPwrMin_Type()
)
pm10010mptMesrlineNetRxInputPwrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrlineNetRxInputPwrMin.setStatus("current")


class _Pm10010mptMesrlineResidualChromaticDispMin_Type(Unsigned32):
    """Custom type pm10010mptMesrlineResidualChromaticDispMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mptMesrlineResidualChromaticDispMin_Type.__name__ = "Unsigned32"
_Pm10010mptMesrlineResidualChromaticDispMin_Object = MibScalar
pm10010mptMesrlineResidualChromaticDispMin = _Pm10010mptMesrlineResidualChromaticDispMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 1, 200),
    _Pm10010mptMesrlineResidualChromaticDispMin_Type()
)
pm10010mptMesrlineResidualChromaticDispMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrlineResidualChromaticDispMin.setStatus("current")


class _Pm10010mptMesrlineDiffGroupDelayMin_Type(Unsigned32):
    """Custom type pm10010mptMesrlineDiffGroupDelayMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mptMesrlineDiffGroupDelayMin_Type.__name__ = "Unsigned32"
_Pm10010mptMesrlineDiffGroupDelayMin_Object = MibScalar
pm10010mptMesrlineDiffGroupDelayMin = _Pm10010mptMesrlineDiffGroupDelayMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 1, 201),
    _Pm10010mptMesrlineDiffGroupDelayMin_Type()
)
pm10010mptMesrlineDiffGroupDelayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrlineDiffGroupDelayMin.setStatus("current")


class _Pm10010mptMesrlineQFactorMin_Type(Unsigned32):
    """Custom type pm10010mptMesrlineQFactorMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mptMesrlineQFactorMin_Type.__name__ = "Unsigned32"
_Pm10010mptMesrlineQFactorMin_Object = MibScalar
pm10010mptMesrlineQFactorMin = _Pm10010mptMesrlineQFactorMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 1, 202),
    _Pm10010mptMesrlineQFactorMin_Type()
)
pm10010mptMesrlineQFactorMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrlineQFactorMin.setStatus("current")


class _Pm10010mptMesrlineCarrierFreqOffsetMin_Type(Unsigned32):
    """Custom type pm10010mptMesrlineCarrierFreqOffsetMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mptMesrlineCarrierFreqOffsetMin_Type.__name__ = "Unsigned32"
_Pm10010mptMesrlineCarrierFreqOffsetMin_Object = MibScalar
pm10010mptMesrlineCarrierFreqOffsetMin = _Pm10010mptMesrlineCarrierFreqOffsetMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 1, 203),
    _Pm10010mptMesrlineCarrierFreqOffsetMin_Type()
)
pm10010mptMesrlineCarrierFreqOffsetMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrlineCarrierFreqOffsetMin.setStatus("current")


class _Pm10010mptMesrlineOsnrMin_Type(Unsigned32):
    """Custom type pm10010mptMesrlineOsnrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mptMesrlineOsnrMin_Type.__name__ = "Unsigned32"
_Pm10010mptMesrlineOsnrMin_Object = MibScalar
pm10010mptMesrlineOsnrMin = _Pm10010mptMesrlineOsnrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 1, 204),
    _Pm10010mptMesrlineOsnrMin_Type()
)
pm10010mptMesrlineOsnrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrlineOsnrMin.setStatus("current")


class _Pm10010mptMesrclientNetTxTempMax_Type(Unsigned32):
    """Custom type pm10010mptMesrclientNetTxTempMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mptMesrclientNetTxTempMax_Type.__name__ = "Unsigned32"
_Pm10010mptMesrclientNetTxTempMax_Object = MibScalar
pm10010mptMesrclientNetTxTempMax = _Pm10010mptMesrclientNetTxTempMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 1, 208),
    _Pm10010mptMesrclientNetTxTempMax_Type()
)
pm10010mptMesrclientNetTxTempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrclientNetTxTempMax.setStatus("current")


class _Pm10010mptMesrclientNetTxBiasMax_Type(Unsigned32):
    """Custom type pm10010mptMesrclientNetTxBiasMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mptMesrclientNetTxBiasMax_Type.__name__ = "Unsigned32"
_Pm10010mptMesrclientNetTxBiasMax_Object = MibScalar
pm10010mptMesrclientNetTxBiasMax = _Pm10010mptMesrclientNetTxBiasMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 1, 209),
    _Pm10010mptMesrclientNetTxBiasMax_Type()
)
pm10010mptMesrclientNetTxBiasMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrclientNetTxBiasMax.setStatus("current")


class _Pm10010mptMesrclientNetTxPwrMax_Type(Unsigned32):
    """Custom type pm10010mptMesrclientNetTxPwrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mptMesrclientNetTxPwrMax_Type.__name__ = "Unsigned32"
_Pm10010mptMesrclientNetTxPwrMax_Object = MibScalar
pm10010mptMesrclientNetTxPwrMax = _Pm10010mptMesrclientNetTxPwrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 1, 210),
    _Pm10010mptMesrclientNetTxPwrMax_Type()
)
pm10010mptMesrclientNetTxPwrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrclientNetTxPwrMax.setStatus("current")


class _Pm10010mptMesrclientNetRxPwrMax_Type(Unsigned32):
    """Custom type pm10010mptMesrclientNetRxPwrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mptMesrclientNetRxPwrMax_Type.__name__ = "Unsigned32"
_Pm10010mptMesrclientNetRxPwrMax_Object = MibScalar
pm10010mptMesrclientNetRxPwrMax = _Pm10010mptMesrclientNetRxPwrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 1, 211),
    _Pm10010mptMesrclientNetRxPwrMax_Type()
)
pm10010mptMesrclientNetRxPwrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrclientNetRxPwrMax.setStatus("current")


class _Pm10010mptMesrlineNetTxLaserOutputPwrMax_Type(Unsigned32):
    """Custom type pm10010mptMesrlineNetTxLaserOutputPwrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mptMesrlineNetTxLaserOutputPwrMax_Type.__name__ = "Unsigned32"
_Pm10010mptMesrlineNetTxLaserOutputPwrMax_Object = MibScalar
pm10010mptMesrlineNetTxLaserOutputPwrMax = _Pm10010mptMesrlineNetTxLaserOutputPwrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 1, 212),
    _Pm10010mptMesrlineNetTxLaserOutputPwrMax_Type()
)
pm10010mptMesrlineNetTxLaserOutputPwrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrlineNetTxLaserOutputPwrMax.setStatus("current")


class _Pm10010mptMesrlineNetTxLaserTempMax_Type(Unsigned32):
    """Custom type pm10010mptMesrlineNetTxLaserTempMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mptMesrlineNetTxLaserTempMax_Type.__name__ = "Unsigned32"
_Pm10010mptMesrlineNetTxLaserTempMax_Object = MibScalar
pm10010mptMesrlineNetTxLaserTempMax = _Pm10010mptMesrlineNetTxLaserTempMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 1, 213),
    _Pm10010mptMesrlineNetTxLaserTempMax_Type()
)
pm10010mptMesrlineNetTxLaserTempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrlineNetTxLaserTempMax.setStatus("current")


class _Pm10010mptMesrlineNetTxBiasCurrentMax_Type(Unsigned32):
    """Custom type pm10010mptMesrlineNetTxBiasCurrentMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mptMesrlineNetTxBiasCurrentMax_Type.__name__ = "Unsigned32"
_Pm10010mptMesrlineNetTxBiasCurrentMax_Object = MibScalar
pm10010mptMesrlineNetTxBiasCurrentMax = _Pm10010mptMesrlineNetTxBiasCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 1, 214),
    _Pm10010mptMesrlineNetTxBiasCurrentMax_Type()
)
pm10010mptMesrlineNetTxBiasCurrentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrlineNetTxBiasCurrentMax.setStatus("current")


class _Pm10010mptMesrlineNetRxInputPwrMax_Type(Unsigned32):
    """Custom type pm10010mptMesrlineNetRxInputPwrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mptMesrlineNetRxInputPwrMax_Type.__name__ = "Unsigned32"
_Pm10010mptMesrlineNetRxInputPwrMax_Object = MibScalar
pm10010mptMesrlineNetRxInputPwrMax = _Pm10010mptMesrlineNetRxInputPwrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 1, 215),
    _Pm10010mptMesrlineNetRxInputPwrMax_Type()
)
pm10010mptMesrlineNetRxInputPwrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrlineNetRxInputPwrMax.setStatus("current")


class _Pm10010mptMesrlineResidualChromaticDispMax_Type(Unsigned32):
    """Custom type pm10010mptMesrlineResidualChromaticDispMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mptMesrlineResidualChromaticDispMax_Type.__name__ = "Unsigned32"
_Pm10010mptMesrlineResidualChromaticDispMax_Object = MibScalar
pm10010mptMesrlineResidualChromaticDispMax = _Pm10010mptMesrlineResidualChromaticDispMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 1, 216),
    _Pm10010mptMesrlineResidualChromaticDispMax_Type()
)
pm10010mptMesrlineResidualChromaticDispMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrlineResidualChromaticDispMax.setStatus("current")


class _Pm10010mptMesrlineDiffGroupDelayMax_Type(Unsigned32):
    """Custom type pm10010mptMesrlineDiffGroupDelayMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mptMesrlineDiffGroupDelayMax_Type.__name__ = "Unsigned32"
_Pm10010mptMesrlineDiffGroupDelayMax_Object = MibScalar
pm10010mptMesrlineDiffGroupDelayMax = _Pm10010mptMesrlineDiffGroupDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 1, 217),
    _Pm10010mptMesrlineDiffGroupDelayMax_Type()
)
pm10010mptMesrlineDiffGroupDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrlineDiffGroupDelayMax.setStatus("current")


class _Pm10010mptMesrlineQFactorMax_Type(Unsigned32):
    """Custom type pm10010mptMesrlineQFactorMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mptMesrlineQFactorMax_Type.__name__ = "Unsigned32"
_Pm10010mptMesrlineQFactorMax_Object = MibScalar
pm10010mptMesrlineQFactorMax = _Pm10010mptMesrlineQFactorMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 1, 218),
    _Pm10010mptMesrlineQFactorMax_Type()
)
pm10010mptMesrlineQFactorMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrlineQFactorMax.setStatus("current")


class _Pm10010mptMesrlineCarrierFreqOffsetMax_Type(Unsigned32):
    """Custom type pm10010mptMesrlineCarrierFreqOffsetMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mptMesrlineCarrierFreqOffsetMax_Type.__name__ = "Unsigned32"
_Pm10010mptMesrlineCarrierFreqOffsetMax_Object = MibScalar
pm10010mptMesrlineCarrierFreqOffsetMax = _Pm10010mptMesrlineCarrierFreqOffsetMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 1, 219),
    _Pm10010mptMesrlineCarrierFreqOffsetMax_Type()
)
pm10010mptMesrlineCarrierFreqOffsetMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrlineCarrierFreqOffsetMax.setStatus("current")


class _Pm10010mptMesrlineOsnrMax_Type(Unsigned32):
    """Custom type pm10010mptMesrlineOsnrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mptMesrlineOsnrMax_Type.__name__ = "Unsigned32"
_Pm10010mptMesrlineOsnrMax_Object = MibScalar
pm10010mptMesrlineOsnrMax = _Pm10010mptMesrlineOsnrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 1, 220),
    _Pm10010mptMesrlineOsnrMax_Type()
)
pm10010mptMesrlineOsnrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrlineOsnrMax.setStatus("current")
_Pm10010mptMesrClient_ObjectIdentity = ObjectIdentity
pm10010mptMesrClient = _Pm10010mptMesrClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 2)
)


class _Pm10010mptMesrclientCfpTemp_Type(Unsigned32):
    """Custom type pm10010mptMesrclientCfpTemp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mptMesrclientCfpTemp_Type.__name__ = "Unsigned32"
_Pm10010mptMesrclientCfpTemp_Object = MibScalar
pm10010mptMesrclientCfpTemp = _Pm10010mptMesrclientCfpTemp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 2, 8),
    _Pm10010mptMesrclientCfpTemp_Type()
)
pm10010mptMesrclientCfpTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrclientCfpTemp.setStatus("current")


class _Pm10010mptMesrclientCfp3v3Voltage_Type(Unsigned32):
    """Custom type pm10010mptMesrclientCfp3v3Voltage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mptMesrclientCfp3v3Voltage_Type.__name__ = "Unsigned32"
_Pm10010mptMesrclientCfp3v3Voltage_Object = MibScalar
pm10010mptMesrclientCfp3v3Voltage = _Pm10010mptMesrclientCfp3v3Voltage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 2, 9),
    _Pm10010mptMesrclientCfp3v3Voltage_Type()
)
pm10010mptMesrclientCfp3v3Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrclientCfp3v3Voltage.setStatus("current")


class _Pm10010mptMesrclientSoaBiasCurrent_Type(Unsigned32):
    """Custom type pm10010mptMesrclientSoaBiasCurrent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mptMesrclientSoaBiasCurrent_Type.__name__ = "Unsigned32"
_Pm10010mptMesrclientSoaBiasCurrent_Object = MibScalar
pm10010mptMesrclientSoaBiasCurrent = _Pm10010mptMesrclientSoaBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 2, 10),
    _Pm10010mptMesrclientSoaBiasCurrent_Type()
)
pm10010mptMesrclientSoaBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrclientSoaBiasCurrent.setStatus("current")
_Pm10010mptMesrclientNetTxTempTable_Object = MibTable
pm10010mptMesrclientNetTxTempTable = _Pm10010mptMesrclientNetTxTempTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 2, 16)
)
if mibBuilder.loadTexts:
    pm10010mptMesrclientNetTxTempTable.setStatus("current")
_Pm10010mptMesrclientNetTxTempEntry_Object = MibTableRow
pm10010mptMesrclientNetTxTempEntry = _Pm10010mptMesrclientNetTxTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 2, 16, 1)
)
pm10010mptMesrclientNetTxTempEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptMesrclientNetTxTempIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptMesrclientNetTxTempEntry.setStatus("current")


class _Pm10010mptMesrclientNetTxTempIndex_Type(Integer32):
    """Custom type pm10010mptMesrclientNetTxTempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptMesrclientNetTxTempIndex_Type.__name__ = "Integer32"
_Pm10010mptMesrclientNetTxTempIndex_Object = MibTableColumn
pm10010mptMesrclientNetTxTempIndex = _Pm10010mptMesrclientNetTxTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 2, 16, 1, 1),
    _Pm10010mptMesrclientNetTxTempIndex_Type()
)
pm10010mptMesrclientNetTxTempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrclientNetTxTempIndex.setStatus("current")


class _Pm10010mptMesrclientNetTxTempPortn_Type(Integer32):
    """Custom type pm10010mptMesrclientNetTxTempPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mptMesrclientNetTxTempPortn_Type.__name__ = "Integer32"
_Pm10010mptMesrclientNetTxTempPortn_Object = MibTableColumn
pm10010mptMesrclientNetTxTempPortn = _Pm10010mptMesrclientNetTxTempPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 2, 16, 1, 2),
    _Pm10010mptMesrclientNetTxTempPortn_Type()
)
pm10010mptMesrclientNetTxTempPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrclientNetTxTempPortn.setStatus("current")
_Pm10010mptMesrclientNetTxBiasTable_Object = MibTable
pm10010mptMesrclientNetTxBiasTable = _Pm10010mptMesrclientNetTxBiasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 2, 32)
)
if mibBuilder.loadTexts:
    pm10010mptMesrclientNetTxBiasTable.setStatus("current")
_Pm10010mptMesrclientNetTxBiasEntry_Object = MibTableRow
pm10010mptMesrclientNetTxBiasEntry = _Pm10010mptMesrclientNetTxBiasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 2, 32, 1)
)
pm10010mptMesrclientNetTxBiasEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptMesrclientNetTxBiasIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptMesrclientNetTxBiasEntry.setStatus("current")


class _Pm10010mptMesrclientNetTxBiasIndex_Type(Integer32):
    """Custom type pm10010mptMesrclientNetTxBiasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptMesrclientNetTxBiasIndex_Type.__name__ = "Integer32"
_Pm10010mptMesrclientNetTxBiasIndex_Object = MibTableColumn
pm10010mptMesrclientNetTxBiasIndex = _Pm10010mptMesrclientNetTxBiasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 2, 32, 1, 1),
    _Pm10010mptMesrclientNetTxBiasIndex_Type()
)
pm10010mptMesrclientNetTxBiasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrclientNetTxBiasIndex.setStatus("current")


class _Pm10010mptMesrclientNetTxBiasPortn_Type(Integer32):
    """Custom type pm10010mptMesrclientNetTxBiasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mptMesrclientNetTxBiasPortn_Type.__name__ = "Integer32"
_Pm10010mptMesrclientNetTxBiasPortn_Object = MibTableColumn
pm10010mptMesrclientNetTxBiasPortn = _Pm10010mptMesrclientNetTxBiasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 2, 32, 1, 2),
    _Pm10010mptMesrclientNetTxBiasPortn_Type()
)
pm10010mptMesrclientNetTxBiasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrclientNetTxBiasPortn.setStatus("current")
_Pm10010mptMesrclientNetTxPwrTable_Object = MibTable
pm10010mptMesrclientNetTxPwrTable = _Pm10010mptMesrclientNetTxPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 2, 48)
)
if mibBuilder.loadTexts:
    pm10010mptMesrclientNetTxPwrTable.setStatus("current")
_Pm10010mptMesrclientNetTxPwrEntry_Object = MibTableRow
pm10010mptMesrclientNetTxPwrEntry = _Pm10010mptMesrclientNetTxPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 2, 48, 1)
)
pm10010mptMesrclientNetTxPwrEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptMesrclientNetTxPwrIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptMesrclientNetTxPwrEntry.setStatus("current")


class _Pm10010mptMesrclientNetTxPwrIndex_Type(Integer32):
    """Custom type pm10010mptMesrclientNetTxPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptMesrclientNetTxPwrIndex_Type.__name__ = "Integer32"
_Pm10010mptMesrclientNetTxPwrIndex_Object = MibTableColumn
pm10010mptMesrclientNetTxPwrIndex = _Pm10010mptMesrclientNetTxPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 2, 48, 1, 1),
    _Pm10010mptMesrclientNetTxPwrIndex_Type()
)
pm10010mptMesrclientNetTxPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrclientNetTxPwrIndex.setStatus("current")


class _Pm10010mptMesrclientNetTxPwrPortn_Type(Integer32):
    """Custom type pm10010mptMesrclientNetTxPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mptMesrclientNetTxPwrPortn_Type.__name__ = "Integer32"
_Pm10010mptMesrclientNetTxPwrPortn_Object = MibTableColumn
pm10010mptMesrclientNetTxPwrPortn = _Pm10010mptMesrclientNetTxPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 2, 48, 1, 2),
    _Pm10010mptMesrclientNetTxPwrPortn_Type()
)
pm10010mptMesrclientNetTxPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrclientNetTxPwrPortn.setStatus("current")
_Pm10010mptMesrclientNetRxPwrTable_Object = MibTable
pm10010mptMesrclientNetRxPwrTable = _Pm10010mptMesrclientNetRxPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 2, 64)
)
if mibBuilder.loadTexts:
    pm10010mptMesrclientNetRxPwrTable.setStatus("current")
_Pm10010mptMesrclientNetRxPwrEntry_Object = MibTableRow
pm10010mptMesrclientNetRxPwrEntry = _Pm10010mptMesrclientNetRxPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 2, 64, 1)
)
pm10010mptMesrclientNetRxPwrEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptMesrclientNetRxPwrIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptMesrclientNetRxPwrEntry.setStatus("current")


class _Pm10010mptMesrclientNetRxPwrIndex_Type(Integer32):
    """Custom type pm10010mptMesrclientNetRxPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptMesrclientNetRxPwrIndex_Type.__name__ = "Integer32"
_Pm10010mptMesrclientNetRxPwrIndex_Object = MibTableColumn
pm10010mptMesrclientNetRxPwrIndex = _Pm10010mptMesrclientNetRxPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 2, 64, 1, 1),
    _Pm10010mptMesrclientNetRxPwrIndex_Type()
)
pm10010mptMesrclientNetRxPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrclientNetRxPwrIndex.setStatus("current")


class _Pm10010mptMesrclientNetRxPwrPortn_Type(Integer32):
    """Custom type pm10010mptMesrclientNetRxPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mptMesrclientNetRxPwrPortn_Type.__name__ = "Integer32"
_Pm10010mptMesrclientNetRxPwrPortn_Object = MibTableColumn
pm10010mptMesrclientNetRxPwrPortn = _Pm10010mptMesrclientNetRxPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 2, 64, 1, 2),
    _Pm10010mptMesrclientNetRxPwrPortn_Type()
)
pm10010mptMesrclientNetRxPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrclientNetRxPwrPortn.setStatus("current")
_Pm10010mptMesrLine_ObjectIdentity = ObjectIdentity
pm10010mptMesrLine = _Pm10010mptMesrLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 3)
)


class _Pm10010mptMesrlineMsaTemp_Type(Unsigned32):
    """Custom type pm10010mptMesrlineMsaTemp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mptMesrlineMsaTemp_Type.__name__ = "Unsigned32"
_Pm10010mptMesrlineMsaTemp_Object = MibScalar
pm10010mptMesrlineMsaTemp = _Pm10010mptMesrlineMsaTemp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 3, 12),
    _Pm10010mptMesrlineMsaTemp_Type()
)
pm10010mptMesrlineMsaTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrlineMsaTemp.setStatus("current")


class _Pm10010mptMesrlineMsa3v3Voltage_Type(Unsigned32):
    """Custom type pm10010mptMesrlineMsa3v3Voltage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mptMesrlineMsa3v3Voltage_Type.__name__ = "Unsigned32"
_Pm10010mptMesrlineMsa3v3Voltage_Object = MibScalar
pm10010mptMesrlineMsa3v3Voltage = _Pm10010mptMesrlineMsa3v3Voltage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 3, 13),
    _Pm10010mptMesrlineMsa3v3Voltage_Type()
)
pm10010mptMesrlineMsa3v3Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrlineMsa3v3Voltage.setStatus("current")


class _Pm10010mptMesrlineSoaBiasCurrent_Type(Unsigned32):
    """Custom type pm10010mptMesrlineSoaBiasCurrent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mptMesrlineSoaBiasCurrent_Type.__name__ = "Unsigned32"
_Pm10010mptMesrlineSoaBiasCurrent_Object = MibScalar
pm10010mptMesrlineSoaBiasCurrent = _Pm10010mptMesrlineSoaBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 3, 14),
    _Pm10010mptMesrlineSoaBiasCurrent_Type()
)
pm10010mptMesrlineSoaBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrlineSoaBiasCurrent.setStatus("current")
_Pm10010mptMesrlineNetTxLaserOutputPwrTable_Object = MibTable
pm10010mptMesrlineNetTxLaserOutputPwrTable = _Pm10010mptMesrlineNetTxLaserOutputPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 3, 80)
)
if mibBuilder.loadTexts:
    pm10010mptMesrlineNetTxLaserOutputPwrTable.setStatus("current")
_Pm10010mptMesrlineNetTxLaserOutputPwrEntry_Object = MibTableRow
pm10010mptMesrlineNetTxLaserOutputPwrEntry = _Pm10010mptMesrlineNetTxLaserOutputPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 3, 80, 1)
)
pm10010mptMesrlineNetTxLaserOutputPwrEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptMesrlineNetTxLaserOutputPwrIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptMesrlineNetTxLaserOutputPwrEntry.setStatus("current")


class _Pm10010mptMesrlineNetTxLaserOutputPwrIndex_Type(Integer32):
    """Custom type pm10010mptMesrlineNetTxLaserOutputPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptMesrlineNetTxLaserOutputPwrIndex_Type.__name__ = "Integer32"
_Pm10010mptMesrlineNetTxLaserOutputPwrIndex_Object = MibTableColumn
pm10010mptMesrlineNetTxLaserOutputPwrIndex = _Pm10010mptMesrlineNetTxLaserOutputPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 3, 80, 1, 1),
    _Pm10010mptMesrlineNetTxLaserOutputPwrIndex_Type()
)
pm10010mptMesrlineNetTxLaserOutputPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrlineNetTxLaserOutputPwrIndex.setStatus("current")


class _Pm10010mptMesrlineNetTxLaserOutputPwrPortn_Type(Integer32):
    """Custom type pm10010mptMesrlineNetTxLaserOutputPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mptMesrlineNetTxLaserOutputPwrPortn_Type.__name__ = "Integer32"
_Pm10010mptMesrlineNetTxLaserOutputPwrPortn_Object = MibTableColumn
pm10010mptMesrlineNetTxLaserOutputPwrPortn = _Pm10010mptMesrlineNetTxLaserOutputPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 3, 80, 1, 2),
    _Pm10010mptMesrlineNetTxLaserOutputPwrPortn_Type()
)
pm10010mptMesrlineNetTxLaserOutputPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrlineNetTxLaserOutputPwrPortn.setStatus("current")
_Pm10010mptMesrlineNetTxLaserTempTable_Object = MibTable
pm10010mptMesrlineNetTxLaserTempTable = _Pm10010mptMesrlineNetTxLaserTempTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 3, 96)
)
if mibBuilder.loadTexts:
    pm10010mptMesrlineNetTxLaserTempTable.setStatus("current")
_Pm10010mptMesrlineNetTxLaserTempEntry_Object = MibTableRow
pm10010mptMesrlineNetTxLaserTempEntry = _Pm10010mptMesrlineNetTxLaserTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 3, 96, 1)
)
pm10010mptMesrlineNetTxLaserTempEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptMesrlineNetTxLaserTempIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptMesrlineNetTxLaserTempEntry.setStatus("current")


class _Pm10010mptMesrlineNetTxLaserTempIndex_Type(Integer32):
    """Custom type pm10010mptMesrlineNetTxLaserTempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptMesrlineNetTxLaserTempIndex_Type.__name__ = "Integer32"
_Pm10010mptMesrlineNetTxLaserTempIndex_Object = MibTableColumn
pm10010mptMesrlineNetTxLaserTempIndex = _Pm10010mptMesrlineNetTxLaserTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 3, 96, 1, 1),
    _Pm10010mptMesrlineNetTxLaserTempIndex_Type()
)
pm10010mptMesrlineNetTxLaserTempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrlineNetTxLaserTempIndex.setStatus("current")


class _Pm10010mptMesrlineNetTxLaserTempPortn_Type(Integer32):
    """Custom type pm10010mptMesrlineNetTxLaserTempPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mptMesrlineNetTxLaserTempPortn_Type.__name__ = "Integer32"
_Pm10010mptMesrlineNetTxLaserTempPortn_Object = MibTableColumn
pm10010mptMesrlineNetTxLaserTempPortn = _Pm10010mptMesrlineNetTxLaserTempPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 3, 96, 1, 2),
    _Pm10010mptMesrlineNetTxLaserTempPortn_Type()
)
pm10010mptMesrlineNetTxLaserTempPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrlineNetTxLaserTempPortn.setStatus("current")
_Pm10010mptMesrlineNetTxBiasCurrentTable_Object = MibTable
pm10010mptMesrlineNetTxBiasCurrentTable = _Pm10010mptMesrlineNetTxBiasCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 3, 112)
)
if mibBuilder.loadTexts:
    pm10010mptMesrlineNetTxBiasCurrentTable.setStatus("current")
_Pm10010mptMesrlineNetTxBiasCurrentEntry_Object = MibTableRow
pm10010mptMesrlineNetTxBiasCurrentEntry = _Pm10010mptMesrlineNetTxBiasCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 3, 112, 1)
)
pm10010mptMesrlineNetTxBiasCurrentEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptMesrlineNetTxBiasCurrentIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptMesrlineNetTxBiasCurrentEntry.setStatus("current")


class _Pm10010mptMesrlineNetTxBiasCurrentIndex_Type(Integer32):
    """Custom type pm10010mptMesrlineNetTxBiasCurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptMesrlineNetTxBiasCurrentIndex_Type.__name__ = "Integer32"
_Pm10010mptMesrlineNetTxBiasCurrentIndex_Object = MibTableColumn
pm10010mptMesrlineNetTxBiasCurrentIndex = _Pm10010mptMesrlineNetTxBiasCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 3, 112, 1, 1),
    _Pm10010mptMesrlineNetTxBiasCurrentIndex_Type()
)
pm10010mptMesrlineNetTxBiasCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrlineNetTxBiasCurrentIndex.setStatus("current")


class _Pm10010mptMesrlineNetTxBiasCurrentPortn_Type(Integer32):
    """Custom type pm10010mptMesrlineNetTxBiasCurrentPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mptMesrlineNetTxBiasCurrentPortn_Type.__name__ = "Integer32"
_Pm10010mptMesrlineNetTxBiasCurrentPortn_Object = MibTableColumn
pm10010mptMesrlineNetTxBiasCurrentPortn = _Pm10010mptMesrlineNetTxBiasCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 3, 112, 1, 2),
    _Pm10010mptMesrlineNetTxBiasCurrentPortn_Type()
)
pm10010mptMesrlineNetTxBiasCurrentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrlineNetTxBiasCurrentPortn.setStatus("current")
_Pm10010mptMesrlineNetRxInputPwrTable_Object = MibTable
pm10010mptMesrlineNetRxInputPwrTable = _Pm10010mptMesrlineNetRxInputPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 3, 128)
)
if mibBuilder.loadTexts:
    pm10010mptMesrlineNetRxInputPwrTable.setStatus("current")
_Pm10010mptMesrlineNetRxInputPwrEntry_Object = MibTableRow
pm10010mptMesrlineNetRxInputPwrEntry = _Pm10010mptMesrlineNetRxInputPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 3, 128, 1)
)
pm10010mptMesrlineNetRxInputPwrEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptMesrlineNetRxInputPwrIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptMesrlineNetRxInputPwrEntry.setStatus("current")


class _Pm10010mptMesrlineNetRxInputPwrIndex_Type(Integer32):
    """Custom type pm10010mptMesrlineNetRxInputPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptMesrlineNetRxInputPwrIndex_Type.__name__ = "Integer32"
_Pm10010mptMesrlineNetRxInputPwrIndex_Object = MibTableColumn
pm10010mptMesrlineNetRxInputPwrIndex = _Pm10010mptMesrlineNetRxInputPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 3, 128, 1, 1),
    _Pm10010mptMesrlineNetRxInputPwrIndex_Type()
)
pm10010mptMesrlineNetRxInputPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrlineNetRxInputPwrIndex.setStatus("current")


class _Pm10010mptMesrlineNetRxInputPwrPortn_Type(Integer32):
    """Custom type pm10010mptMesrlineNetRxInputPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mptMesrlineNetRxInputPwrPortn_Type.__name__ = "Integer32"
_Pm10010mptMesrlineNetRxInputPwrPortn_Object = MibTableColumn
pm10010mptMesrlineNetRxInputPwrPortn = _Pm10010mptMesrlineNetRxInputPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 3, 128, 1, 2),
    _Pm10010mptMesrlineNetRxInputPwrPortn_Type()
)
pm10010mptMesrlineNetRxInputPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrlineNetRxInputPwrPortn.setStatus("current")
_Pm10010mptMesrlineResidualChromaticDispTable_Object = MibTable
pm10010mptMesrlineResidualChromaticDispTable = _Pm10010mptMesrlineResidualChromaticDispTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 3, 144)
)
if mibBuilder.loadTexts:
    pm10010mptMesrlineResidualChromaticDispTable.setStatus("current")
_Pm10010mptMesrlineResidualChromaticDispEntry_Object = MibTableRow
pm10010mptMesrlineResidualChromaticDispEntry = _Pm10010mptMesrlineResidualChromaticDispEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 3, 144, 1)
)
pm10010mptMesrlineResidualChromaticDispEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptMesrlineResidualChromaticDispIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptMesrlineResidualChromaticDispEntry.setStatus("current")


class _Pm10010mptMesrlineResidualChromaticDispIndex_Type(Integer32):
    """Custom type pm10010mptMesrlineResidualChromaticDispIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptMesrlineResidualChromaticDispIndex_Type.__name__ = "Integer32"
_Pm10010mptMesrlineResidualChromaticDispIndex_Object = MibTableColumn
pm10010mptMesrlineResidualChromaticDispIndex = _Pm10010mptMesrlineResidualChromaticDispIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 3, 144, 1, 1),
    _Pm10010mptMesrlineResidualChromaticDispIndex_Type()
)
pm10010mptMesrlineResidualChromaticDispIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrlineResidualChromaticDispIndex.setStatus("current")


class _Pm10010mptMesrlineResidualChromaticDispPortn_Type(Integer32):
    """Custom type pm10010mptMesrlineResidualChromaticDispPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mptMesrlineResidualChromaticDispPortn_Type.__name__ = "Integer32"
_Pm10010mptMesrlineResidualChromaticDispPortn_Object = MibTableColumn
pm10010mptMesrlineResidualChromaticDispPortn = _Pm10010mptMesrlineResidualChromaticDispPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 3, 144, 1, 2),
    _Pm10010mptMesrlineResidualChromaticDispPortn_Type()
)
pm10010mptMesrlineResidualChromaticDispPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrlineResidualChromaticDispPortn.setStatus("current")
_Pm10010mptMesrlineDiffGroupDelayTable_Object = MibTable
pm10010mptMesrlineDiffGroupDelayTable = _Pm10010mptMesrlineDiffGroupDelayTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 3, 148)
)
if mibBuilder.loadTexts:
    pm10010mptMesrlineDiffGroupDelayTable.setStatus("current")
_Pm10010mptMesrlineDiffGroupDelayEntry_Object = MibTableRow
pm10010mptMesrlineDiffGroupDelayEntry = _Pm10010mptMesrlineDiffGroupDelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 3, 148, 1)
)
pm10010mptMesrlineDiffGroupDelayEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptMesrlineDiffGroupDelayIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptMesrlineDiffGroupDelayEntry.setStatus("current")


class _Pm10010mptMesrlineDiffGroupDelayIndex_Type(Integer32):
    """Custom type pm10010mptMesrlineDiffGroupDelayIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptMesrlineDiffGroupDelayIndex_Type.__name__ = "Integer32"
_Pm10010mptMesrlineDiffGroupDelayIndex_Object = MibTableColumn
pm10010mptMesrlineDiffGroupDelayIndex = _Pm10010mptMesrlineDiffGroupDelayIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 3, 148, 1, 1),
    _Pm10010mptMesrlineDiffGroupDelayIndex_Type()
)
pm10010mptMesrlineDiffGroupDelayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrlineDiffGroupDelayIndex.setStatus("current")


class _Pm10010mptMesrlineDiffGroupDelayPortn_Type(Integer32):
    """Custom type pm10010mptMesrlineDiffGroupDelayPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mptMesrlineDiffGroupDelayPortn_Type.__name__ = "Integer32"
_Pm10010mptMesrlineDiffGroupDelayPortn_Object = MibTableColumn
pm10010mptMesrlineDiffGroupDelayPortn = _Pm10010mptMesrlineDiffGroupDelayPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 3, 148, 1, 2),
    _Pm10010mptMesrlineDiffGroupDelayPortn_Type()
)
pm10010mptMesrlineDiffGroupDelayPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrlineDiffGroupDelayPortn.setStatus("current")
_Pm10010mptMesrlineQFactorTable_Object = MibTable
pm10010mptMesrlineQFactorTable = _Pm10010mptMesrlineQFactorTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 3, 152)
)
if mibBuilder.loadTexts:
    pm10010mptMesrlineQFactorTable.setStatus("current")
_Pm10010mptMesrlineQFactorEntry_Object = MibTableRow
pm10010mptMesrlineQFactorEntry = _Pm10010mptMesrlineQFactorEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 3, 152, 1)
)
pm10010mptMesrlineQFactorEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptMesrlineQFactorIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptMesrlineQFactorEntry.setStatus("current")


class _Pm10010mptMesrlineQFactorIndex_Type(Integer32):
    """Custom type pm10010mptMesrlineQFactorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptMesrlineQFactorIndex_Type.__name__ = "Integer32"
_Pm10010mptMesrlineQFactorIndex_Object = MibTableColumn
pm10010mptMesrlineQFactorIndex = _Pm10010mptMesrlineQFactorIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 3, 152, 1, 1),
    _Pm10010mptMesrlineQFactorIndex_Type()
)
pm10010mptMesrlineQFactorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrlineQFactorIndex.setStatus("current")


class _Pm10010mptMesrlineQFactorPortn_Type(Integer32):
    """Custom type pm10010mptMesrlineQFactorPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mptMesrlineQFactorPortn_Type.__name__ = "Integer32"
_Pm10010mptMesrlineQFactorPortn_Object = MibTableColumn
pm10010mptMesrlineQFactorPortn = _Pm10010mptMesrlineQFactorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 3, 152, 1, 2),
    _Pm10010mptMesrlineQFactorPortn_Type()
)
pm10010mptMesrlineQFactorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrlineQFactorPortn.setStatus("current")
_Pm10010mptMesrlineCarrierFreqOffsetTable_Object = MibTable
pm10010mptMesrlineCarrierFreqOffsetTable = _Pm10010mptMesrlineCarrierFreqOffsetTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 3, 156)
)
if mibBuilder.loadTexts:
    pm10010mptMesrlineCarrierFreqOffsetTable.setStatus("current")
_Pm10010mptMesrlineCarrierFreqOffsetEntry_Object = MibTableRow
pm10010mptMesrlineCarrierFreqOffsetEntry = _Pm10010mptMesrlineCarrierFreqOffsetEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 3, 156, 1)
)
pm10010mptMesrlineCarrierFreqOffsetEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptMesrlineCarrierFreqOffsetIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptMesrlineCarrierFreqOffsetEntry.setStatus("current")


class _Pm10010mptMesrlineCarrierFreqOffsetIndex_Type(Integer32):
    """Custom type pm10010mptMesrlineCarrierFreqOffsetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptMesrlineCarrierFreqOffsetIndex_Type.__name__ = "Integer32"
_Pm10010mptMesrlineCarrierFreqOffsetIndex_Object = MibTableColumn
pm10010mptMesrlineCarrierFreqOffsetIndex = _Pm10010mptMesrlineCarrierFreqOffsetIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 3, 156, 1, 1),
    _Pm10010mptMesrlineCarrierFreqOffsetIndex_Type()
)
pm10010mptMesrlineCarrierFreqOffsetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrlineCarrierFreqOffsetIndex.setStatus("current")


class _Pm10010mptMesrlineCarrierFreqOffsetPortn_Type(Integer32):
    """Custom type pm10010mptMesrlineCarrierFreqOffsetPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mptMesrlineCarrierFreqOffsetPortn_Type.__name__ = "Integer32"
_Pm10010mptMesrlineCarrierFreqOffsetPortn_Object = MibTableColumn
pm10010mptMesrlineCarrierFreqOffsetPortn = _Pm10010mptMesrlineCarrierFreqOffsetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 3, 156, 1, 2),
    _Pm10010mptMesrlineCarrierFreqOffsetPortn_Type()
)
pm10010mptMesrlineCarrierFreqOffsetPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrlineCarrierFreqOffsetPortn.setStatus("current")
_Pm10010mptMesrlineOsnrTable_Object = MibTable
pm10010mptMesrlineOsnrTable = _Pm10010mptMesrlineOsnrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 3, 160)
)
if mibBuilder.loadTexts:
    pm10010mptMesrlineOsnrTable.setStatus("current")
_Pm10010mptMesrlineOsnrEntry_Object = MibTableRow
pm10010mptMesrlineOsnrEntry = _Pm10010mptMesrlineOsnrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 3, 160, 1)
)
pm10010mptMesrlineOsnrEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptMesrlineOsnrIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptMesrlineOsnrEntry.setStatus("current")


class _Pm10010mptMesrlineOsnrIndex_Type(Integer32):
    """Custom type pm10010mptMesrlineOsnrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptMesrlineOsnrIndex_Type.__name__ = "Integer32"
_Pm10010mptMesrlineOsnrIndex_Object = MibTableColumn
pm10010mptMesrlineOsnrIndex = _Pm10010mptMesrlineOsnrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 3, 160, 1, 1),
    _Pm10010mptMesrlineOsnrIndex_Type()
)
pm10010mptMesrlineOsnrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrlineOsnrIndex.setStatus("current")


class _Pm10010mptMesrlineOsnrPortn_Type(Integer32):
    """Custom type pm10010mptMesrlineOsnrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mptMesrlineOsnrPortn_Type.__name__ = "Integer32"
_Pm10010mptMesrlineOsnrPortn_Object = MibTableColumn
pm10010mptMesrlineOsnrPortn = _Pm10010mptMesrlineOsnrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 3, 3, 160, 1, 2),
    _Pm10010mptMesrlineOsnrPortn_Type()
)
pm10010mptMesrlineOsnrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMesrlineOsnrPortn.setStatus("current")
_Pm10010mptcounters_ObjectIdentity = ObjectIdentity
pm10010mptcounters = _Pm10010mptcounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4)
)
_Pm10010mptCntOther_ObjectIdentity = ObjectIdentity
pm10010mptCntOther = _Pm10010mptCntOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4, 1)
)
_Pm10010mptCntClient_ObjectIdentity = ObjectIdentity
pm10010mptCntClient = _Pm10010mptCntClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4, 2)
)
_Pm10010mptCntclientInputErrorCounterLaneOneTable_Object = MibTable
pm10010mptCntclientInputErrorCounterLaneOneTable = _Pm10010mptCntclientInputErrorCounterLaneOneTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4, 2, 16)
)
if mibBuilder.loadTexts:
    pm10010mptCntclientInputErrorCounterLaneOneTable.setStatus("current")
_Pm10010mptCntclientInputErrorCounterLaneOneEntry_Object = MibTableRow
pm10010mptCntclientInputErrorCounterLaneOneEntry = _Pm10010mptCntclientInputErrorCounterLaneOneEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4, 2, 16, 1)
)
pm10010mptCntclientInputErrorCounterLaneOneEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptCntclientInputErrorCounterLaneOneIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptCntclientInputErrorCounterLaneOneEntry.setStatus("current")


class _Pm10010mptCntclientInputErrorCounterLaneOneIndex_Type(Integer32):
    """Custom type pm10010mptCntclientInputErrorCounterLaneOneIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptCntclientInputErrorCounterLaneOneIndex_Type.__name__ = "Integer32"
_Pm10010mptCntclientInputErrorCounterLaneOneIndex_Object = MibTableColumn
pm10010mptCntclientInputErrorCounterLaneOneIndex = _Pm10010mptCntclientInputErrorCounterLaneOneIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4, 2, 16, 1, 1),
    _Pm10010mptCntclientInputErrorCounterLaneOneIndex_Type()
)
pm10010mptCntclientInputErrorCounterLaneOneIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCntclientInputErrorCounterLaneOneIndex.setStatus("current")
_Pm10010mptCntclientInputErrorCounterLaneOneValuePortn_Type = Counter32
_Pm10010mptCntclientInputErrorCounterLaneOneValuePortn_Object = MibTableColumn
pm10010mptCntclientInputErrorCounterLaneOneValuePortn = _Pm10010mptCntclientInputErrorCounterLaneOneValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4, 2, 16, 1, 2),
    _Pm10010mptCntclientInputErrorCounterLaneOneValuePortn_Type()
)
pm10010mptCntclientInputErrorCounterLaneOneValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCntclientInputErrorCounterLaneOneValuePortn.setStatus("current")
_Pm10010mptCntclientInputErrorCounterLaneOneErrorPortn_Type = EkiOnOff
_Pm10010mptCntclientInputErrorCounterLaneOneErrorPortn_Object = MibTableColumn
pm10010mptCntclientInputErrorCounterLaneOneErrorPortn = _Pm10010mptCntclientInputErrorCounterLaneOneErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4, 2, 16, 1, 3),
    _Pm10010mptCntclientInputErrorCounterLaneOneErrorPortn_Type()
)
pm10010mptCntclientInputErrorCounterLaneOneErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCntclientInputErrorCounterLaneOneErrorPortn.setStatus("current")
_Pm10010mptCntclientInputErrorCounterLaneOneOverloadPortn_Type = EkiOnOff
_Pm10010mptCntclientInputErrorCounterLaneOneOverloadPortn_Object = MibTableColumn
pm10010mptCntclientInputErrorCounterLaneOneOverloadPortn = _Pm10010mptCntclientInputErrorCounterLaneOneOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4, 2, 16, 1, 4),
    _Pm10010mptCntclientInputErrorCounterLaneOneOverloadPortn_Type()
)
pm10010mptCntclientInputErrorCounterLaneOneOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCntclientInputErrorCounterLaneOneOverloadPortn.setStatus("current")
_Pm10010mptCntclientInputErrorCounterLaneTwoTable_Object = MibTable
pm10010mptCntclientInputErrorCounterLaneTwoTable = _Pm10010mptCntclientInputErrorCounterLaneTwoTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4, 2, 32)
)
if mibBuilder.loadTexts:
    pm10010mptCntclientInputErrorCounterLaneTwoTable.setStatus("current")
_Pm10010mptCntclientInputErrorCounterLaneTwoEntry_Object = MibTableRow
pm10010mptCntclientInputErrorCounterLaneTwoEntry = _Pm10010mptCntclientInputErrorCounterLaneTwoEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4, 2, 32, 1)
)
pm10010mptCntclientInputErrorCounterLaneTwoEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptCntclientInputErrorCounterLaneTwoIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptCntclientInputErrorCounterLaneTwoEntry.setStatus("current")


class _Pm10010mptCntclientInputErrorCounterLaneTwoIndex_Type(Integer32):
    """Custom type pm10010mptCntclientInputErrorCounterLaneTwoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptCntclientInputErrorCounterLaneTwoIndex_Type.__name__ = "Integer32"
_Pm10010mptCntclientInputErrorCounterLaneTwoIndex_Object = MibTableColumn
pm10010mptCntclientInputErrorCounterLaneTwoIndex = _Pm10010mptCntclientInputErrorCounterLaneTwoIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4, 2, 32, 1, 1),
    _Pm10010mptCntclientInputErrorCounterLaneTwoIndex_Type()
)
pm10010mptCntclientInputErrorCounterLaneTwoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCntclientInputErrorCounterLaneTwoIndex.setStatus("current")
_Pm10010mptCntclientInputErrorCounterLaneTwoValuePortn_Type = Counter32
_Pm10010mptCntclientInputErrorCounterLaneTwoValuePortn_Object = MibTableColumn
pm10010mptCntclientInputErrorCounterLaneTwoValuePortn = _Pm10010mptCntclientInputErrorCounterLaneTwoValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4, 2, 32, 1, 2),
    _Pm10010mptCntclientInputErrorCounterLaneTwoValuePortn_Type()
)
pm10010mptCntclientInputErrorCounterLaneTwoValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCntclientInputErrorCounterLaneTwoValuePortn.setStatus("current")
_Pm10010mptCntclientInputErrorCounterLaneTwoErrorPortn_Type = EkiOnOff
_Pm10010mptCntclientInputErrorCounterLaneTwoErrorPortn_Object = MibTableColumn
pm10010mptCntclientInputErrorCounterLaneTwoErrorPortn = _Pm10010mptCntclientInputErrorCounterLaneTwoErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4, 2, 32, 1, 3),
    _Pm10010mptCntclientInputErrorCounterLaneTwoErrorPortn_Type()
)
pm10010mptCntclientInputErrorCounterLaneTwoErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCntclientInputErrorCounterLaneTwoErrorPortn.setStatus("current")
_Pm10010mptCntclientInputErrorCounterLaneTwoOverloadPortn_Type = EkiOnOff
_Pm10010mptCntclientInputErrorCounterLaneTwoOverloadPortn_Object = MibTableColumn
pm10010mptCntclientInputErrorCounterLaneTwoOverloadPortn = _Pm10010mptCntclientInputErrorCounterLaneTwoOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4, 2, 32, 1, 4),
    _Pm10010mptCntclientInputErrorCounterLaneTwoOverloadPortn_Type()
)
pm10010mptCntclientInputErrorCounterLaneTwoOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCntclientInputErrorCounterLaneTwoOverloadPortn.setStatus("current")
_Pm10010mptCntclientInputErrorCounterTable_Object = MibTable
pm10010mptCntclientInputErrorCounterTable = _Pm10010mptCntclientInputErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4, 2, 80)
)
if mibBuilder.loadTexts:
    pm10010mptCntclientInputErrorCounterTable.setStatus("current")
_Pm10010mptCntclientInputErrorCounterEntry_Object = MibTableRow
pm10010mptCntclientInputErrorCounterEntry = _Pm10010mptCntclientInputErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4, 2, 80, 1)
)
pm10010mptCntclientInputErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptCntclientInputErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptCntclientInputErrorCounterEntry.setStatus("current")


class _Pm10010mptCntclientInputErrorCounterIndex_Type(Integer32):
    """Custom type pm10010mptCntclientInputErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptCntclientInputErrorCounterIndex_Type.__name__ = "Integer32"
_Pm10010mptCntclientInputErrorCounterIndex_Object = MibTableColumn
pm10010mptCntclientInputErrorCounterIndex = _Pm10010mptCntclientInputErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4, 2, 80, 1, 1),
    _Pm10010mptCntclientInputErrorCounterIndex_Type()
)
pm10010mptCntclientInputErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCntclientInputErrorCounterIndex.setStatus("current")
_Pm10010mptCntclientInputErrorCounterValuePortn_Type = Counter32
_Pm10010mptCntclientInputErrorCounterValuePortn_Object = MibTableColumn
pm10010mptCntclientInputErrorCounterValuePortn = _Pm10010mptCntclientInputErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4, 2, 80, 1, 2),
    _Pm10010mptCntclientInputErrorCounterValuePortn_Type()
)
pm10010mptCntclientInputErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCntclientInputErrorCounterValuePortn.setStatus("current")
_Pm10010mptCntclientInputErrorCounterErrorPortn_Type = EkiOnOff
_Pm10010mptCntclientInputErrorCounterErrorPortn_Object = MibTableColumn
pm10010mptCntclientInputErrorCounterErrorPortn = _Pm10010mptCntclientInputErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4, 2, 80, 1, 3),
    _Pm10010mptCntclientInputErrorCounterErrorPortn_Type()
)
pm10010mptCntclientInputErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCntclientInputErrorCounterErrorPortn.setStatus("current")
_Pm10010mptCntclientInputErrorCounterOverloadPortn_Type = EkiOnOff
_Pm10010mptCntclientInputErrorCounterOverloadPortn_Object = MibTableColumn
pm10010mptCntclientInputErrorCounterOverloadPortn = _Pm10010mptCntclientInputErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4, 2, 80, 1, 4),
    _Pm10010mptCntclientInputErrorCounterOverloadPortn_Type()
)
pm10010mptCntclientInputErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCntclientInputErrorCounterOverloadPortn.setStatus("current")
_Pm10010mptCntclientCbipCounterTable_Object = MibTable
pm10010mptCntclientCbipCounterTable = _Pm10010mptCntclientCbipCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4, 2, 96)
)
if mibBuilder.loadTexts:
    pm10010mptCntclientCbipCounterTable.setStatus("current")
_Pm10010mptCntclientCbipCounterEntry_Object = MibTableRow
pm10010mptCntclientCbipCounterEntry = _Pm10010mptCntclientCbipCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4, 2, 96, 1)
)
pm10010mptCntclientCbipCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptCntclientCbipCounterIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptCntclientCbipCounterEntry.setStatus("current")


class _Pm10010mptCntclientCbipCounterIndex_Type(Integer32):
    """Custom type pm10010mptCntclientCbipCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptCntclientCbipCounterIndex_Type.__name__ = "Integer32"
_Pm10010mptCntclientCbipCounterIndex_Object = MibTableColumn
pm10010mptCntclientCbipCounterIndex = _Pm10010mptCntclientCbipCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4, 2, 96, 1, 1),
    _Pm10010mptCntclientCbipCounterIndex_Type()
)
pm10010mptCntclientCbipCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCntclientCbipCounterIndex.setStatus("current")
_Pm10010mptCntclientCbipCounterValuePortn_Type = Counter32
_Pm10010mptCntclientCbipCounterValuePortn_Object = MibTableColumn
pm10010mptCntclientCbipCounterValuePortn = _Pm10010mptCntclientCbipCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4, 2, 96, 1, 2),
    _Pm10010mptCntclientCbipCounterValuePortn_Type()
)
pm10010mptCntclientCbipCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCntclientCbipCounterValuePortn.setStatus("current")
_Pm10010mptCntclientCbipCounterErrorPortn_Type = EkiOnOff
_Pm10010mptCntclientCbipCounterErrorPortn_Object = MibTableColumn
pm10010mptCntclientCbipCounterErrorPortn = _Pm10010mptCntclientCbipCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4, 2, 96, 1, 3),
    _Pm10010mptCntclientCbipCounterErrorPortn_Type()
)
pm10010mptCntclientCbipCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCntclientCbipCounterErrorPortn.setStatus("current")
_Pm10010mptCntclientCbipCounterOverloadPortn_Type = EkiOnOff
_Pm10010mptCntclientCbipCounterOverloadPortn_Object = MibTableColumn
pm10010mptCntclientCbipCounterOverloadPortn = _Pm10010mptCntclientCbipCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4, 2, 96, 1, 4),
    _Pm10010mptCntclientCbipCounterOverloadPortn_Type()
)
pm10010mptCntclientCbipCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCntclientCbipCounterOverloadPortn.setStatus("current")
_Pm10010mptCntLine_ObjectIdentity = ObjectIdentity
pm10010mptCntLine = _Pm10010mptCntLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4, 3)
)
_Pm10010mptCntlocalLineSmBip8ErrorCounterTable_Object = MibTable
pm10010mptCntlocalLineSmBip8ErrorCounterTable = _Pm10010mptCntlocalLineSmBip8ErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4, 3, 192)
)
if mibBuilder.loadTexts:
    pm10010mptCntlocalLineSmBip8ErrorCounterTable.setStatus("current")
_Pm10010mptCntlocalLineSmBip8ErrorCounterEntry_Object = MibTableRow
pm10010mptCntlocalLineSmBip8ErrorCounterEntry = _Pm10010mptCntlocalLineSmBip8ErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4, 3, 192, 1)
)
pm10010mptCntlocalLineSmBip8ErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptCntlocalLineSmBip8ErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptCntlocalLineSmBip8ErrorCounterEntry.setStatus("current")


class _Pm10010mptCntlocalLineSmBip8ErrorCounterIndex_Type(Integer32):
    """Custom type pm10010mptCntlocalLineSmBip8ErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptCntlocalLineSmBip8ErrorCounterIndex_Type.__name__ = "Integer32"
_Pm10010mptCntlocalLineSmBip8ErrorCounterIndex_Object = MibTableColumn
pm10010mptCntlocalLineSmBip8ErrorCounterIndex = _Pm10010mptCntlocalLineSmBip8ErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4, 3, 192, 1, 1),
    _Pm10010mptCntlocalLineSmBip8ErrorCounterIndex_Type()
)
pm10010mptCntlocalLineSmBip8ErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCntlocalLineSmBip8ErrorCounterIndex.setStatus("current")
_Pm10010mptCntlocalLineSmBip8ErrorCounterValuePortn_Type = Counter64
_Pm10010mptCntlocalLineSmBip8ErrorCounterValuePortn_Object = MibTableColumn
pm10010mptCntlocalLineSmBip8ErrorCounterValuePortn = _Pm10010mptCntlocalLineSmBip8ErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4, 3, 192, 1, 2),
    _Pm10010mptCntlocalLineSmBip8ErrorCounterValuePortn_Type()
)
pm10010mptCntlocalLineSmBip8ErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCntlocalLineSmBip8ErrorCounterValuePortn.setStatus("current")
_Pm10010mptCntlocalLineSmBip8ErrorCounterErrorPortn_Type = EkiOnOff
_Pm10010mptCntlocalLineSmBip8ErrorCounterErrorPortn_Object = MibTableColumn
pm10010mptCntlocalLineSmBip8ErrorCounterErrorPortn = _Pm10010mptCntlocalLineSmBip8ErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4, 3, 192, 1, 3),
    _Pm10010mptCntlocalLineSmBip8ErrorCounterErrorPortn_Type()
)
pm10010mptCntlocalLineSmBip8ErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCntlocalLineSmBip8ErrorCounterErrorPortn.setStatus("current")
_Pm10010mptCntlocalLineSmBip8ErrorCounterOverloadPortn_Type = EkiOnOff
_Pm10010mptCntlocalLineSmBip8ErrorCounterOverloadPortn_Object = MibTableColumn
pm10010mptCntlocalLineSmBip8ErrorCounterOverloadPortn = _Pm10010mptCntlocalLineSmBip8ErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4, 3, 192, 1, 4),
    _Pm10010mptCntlocalLineSmBip8ErrorCounterOverloadPortn_Type()
)
pm10010mptCntlocalLineSmBip8ErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCntlocalLineSmBip8ErrorCounterOverloadPortn.setStatus("current")
_Pm10010mptCntlocalLineFecCorrectedErrorsCounterTable_Object = MibTable
pm10010mptCntlocalLineFecCorrectedErrorsCounterTable = _Pm10010mptCntlocalLineFecCorrectedErrorsCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4, 3, 193)
)
if mibBuilder.loadTexts:
    pm10010mptCntlocalLineFecCorrectedErrorsCounterTable.setStatus("current")
_Pm10010mptCntlocalLineFecCorrectedErrorsCounterEntry_Object = MibTableRow
pm10010mptCntlocalLineFecCorrectedErrorsCounterEntry = _Pm10010mptCntlocalLineFecCorrectedErrorsCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4, 3, 193, 1)
)
pm10010mptCntlocalLineFecCorrectedErrorsCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptCntlocalLineFecCorrectedErrorsCounterIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptCntlocalLineFecCorrectedErrorsCounterEntry.setStatus("current")


class _Pm10010mptCntlocalLineFecCorrectedErrorsCounterIndex_Type(Integer32):
    """Custom type pm10010mptCntlocalLineFecCorrectedErrorsCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptCntlocalLineFecCorrectedErrorsCounterIndex_Type.__name__ = "Integer32"
_Pm10010mptCntlocalLineFecCorrectedErrorsCounterIndex_Object = MibTableColumn
pm10010mptCntlocalLineFecCorrectedErrorsCounterIndex = _Pm10010mptCntlocalLineFecCorrectedErrorsCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4, 3, 193, 1, 1),
    _Pm10010mptCntlocalLineFecCorrectedErrorsCounterIndex_Type()
)
pm10010mptCntlocalLineFecCorrectedErrorsCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCntlocalLineFecCorrectedErrorsCounterIndex.setStatus("current")
_Pm10010mptCntlocalLineFecCorrectedErrorsCounterValuePortn_Type = Counter64
_Pm10010mptCntlocalLineFecCorrectedErrorsCounterValuePortn_Object = MibTableColumn
pm10010mptCntlocalLineFecCorrectedErrorsCounterValuePortn = _Pm10010mptCntlocalLineFecCorrectedErrorsCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4, 3, 193, 1, 2),
    _Pm10010mptCntlocalLineFecCorrectedErrorsCounterValuePortn_Type()
)
pm10010mptCntlocalLineFecCorrectedErrorsCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCntlocalLineFecCorrectedErrorsCounterValuePortn.setStatus("current")
_Pm10010mptCntlocalLineFecCorrectedErrorsCounterErrorPortn_Type = EkiOnOff
_Pm10010mptCntlocalLineFecCorrectedErrorsCounterErrorPortn_Object = MibTableColumn
pm10010mptCntlocalLineFecCorrectedErrorsCounterErrorPortn = _Pm10010mptCntlocalLineFecCorrectedErrorsCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4, 3, 193, 1, 3),
    _Pm10010mptCntlocalLineFecCorrectedErrorsCounterErrorPortn_Type()
)
pm10010mptCntlocalLineFecCorrectedErrorsCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCntlocalLineFecCorrectedErrorsCounterErrorPortn.setStatus("current")
_Pm10010mptCntlocalLineFecCorrectedErrorsCounterOverloadPortn_Type = EkiOnOff
_Pm10010mptCntlocalLineFecCorrectedErrorsCounterOverloadPortn_Object = MibTableColumn
pm10010mptCntlocalLineFecCorrectedErrorsCounterOverloadPortn = _Pm10010mptCntlocalLineFecCorrectedErrorsCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4, 3, 193, 1, 4),
    _Pm10010mptCntlocalLineFecCorrectedErrorsCounterOverloadPortn_Type()
)
pm10010mptCntlocalLineFecCorrectedErrorsCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCntlocalLineFecCorrectedErrorsCounterOverloadPortn.setStatus("current")
_Pm10010mptCntremoteLineSmBip8ErrorCounterTable_Object = MibTable
pm10010mptCntremoteLineSmBip8ErrorCounterTable = _Pm10010mptCntremoteLineSmBip8ErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4, 3, 194)
)
if mibBuilder.loadTexts:
    pm10010mptCntremoteLineSmBip8ErrorCounterTable.setStatus("current")
_Pm10010mptCntremoteLineSmBip8ErrorCounterEntry_Object = MibTableRow
pm10010mptCntremoteLineSmBip8ErrorCounterEntry = _Pm10010mptCntremoteLineSmBip8ErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4, 3, 194, 1)
)
pm10010mptCntremoteLineSmBip8ErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptCntremoteLineSmBip8ErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptCntremoteLineSmBip8ErrorCounterEntry.setStatus("current")


class _Pm10010mptCntremoteLineSmBip8ErrorCounterIndex_Type(Integer32):
    """Custom type pm10010mptCntremoteLineSmBip8ErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptCntremoteLineSmBip8ErrorCounterIndex_Type.__name__ = "Integer32"
_Pm10010mptCntremoteLineSmBip8ErrorCounterIndex_Object = MibTableColumn
pm10010mptCntremoteLineSmBip8ErrorCounterIndex = _Pm10010mptCntremoteLineSmBip8ErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4, 3, 194, 1, 1),
    _Pm10010mptCntremoteLineSmBip8ErrorCounterIndex_Type()
)
pm10010mptCntremoteLineSmBip8ErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCntremoteLineSmBip8ErrorCounterIndex.setStatus("current")
_Pm10010mptCntremoteLineSmBip8ErrorCounterValuePortn_Type = Counter64
_Pm10010mptCntremoteLineSmBip8ErrorCounterValuePortn_Object = MibTableColumn
pm10010mptCntremoteLineSmBip8ErrorCounterValuePortn = _Pm10010mptCntremoteLineSmBip8ErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4, 3, 194, 1, 2),
    _Pm10010mptCntremoteLineSmBip8ErrorCounterValuePortn_Type()
)
pm10010mptCntremoteLineSmBip8ErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCntremoteLineSmBip8ErrorCounterValuePortn.setStatus("current")
_Pm10010mptCntremoteLineSmBip8ErrorCounterErrorPortn_Type = EkiOnOff
_Pm10010mptCntremoteLineSmBip8ErrorCounterErrorPortn_Object = MibTableColumn
pm10010mptCntremoteLineSmBip8ErrorCounterErrorPortn = _Pm10010mptCntremoteLineSmBip8ErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4, 3, 194, 1, 3),
    _Pm10010mptCntremoteLineSmBip8ErrorCounterErrorPortn_Type()
)
pm10010mptCntremoteLineSmBip8ErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCntremoteLineSmBip8ErrorCounterErrorPortn.setStatus("current")
_Pm10010mptCntremoteLineSmBip8ErrorCounterOverloadPortn_Type = EkiOnOff
_Pm10010mptCntremoteLineSmBip8ErrorCounterOverloadPortn_Object = MibTableColumn
pm10010mptCntremoteLineSmBip8ErrorCounterOverloadPortn = _Pm10010mptCntremoteLineSmBip8ErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4, 3, 194, 1, 4),
    _Pm10010mptCntremoteLineSmBip8ErrorCounterOverloadPortn_Type()
)
pm10010mptCntremoteLineSmBip8ErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCntremoteLineSmBip8ErrorCounterOverloadPortn.setStatus("current")
_Pm10010mptCntlineDfrmTimCntTable_Object = MibTable
pm10010mptCntlineDfrmTimCntTable = _Pm10010mptCntlineDfrmTimCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4, 3, 195)
)
if mibBuilder.loadTexts:
    pm10010mptCntlineDfrmTimCntTable.setStatus("current")
_Pm10010mptCntlineDfrmTimCntEntry_Object = MibTableRow
pm10010mptCntlineDfrmTimCntEntry = _Pm10010mptCntlineDfrmTimCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4, 3, 195, 1)
)
pm10010mptCntlineDfrmTimCntEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptCntlineDfrmTimCntIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptCntlineDfrmTimCntEntry.setStatus("current")


class _Pm10010mptCntlineDfrmTimCntIndex_Type(Integer32):
    """Custom type pm10010mptCntlineDfrmTimCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptCntlineDfrmTimCntIndex_Type.__name__ = "Integer32"
_Pm10010mptCntlineDfrmTimCntIndex_Object = MibTableColumn
pm10010mptCntlineDfrmTimCntIndex = _Pm10010mptCntlineDfrmTimCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4, 3, 195, 1, 1),
    _Pm10010mptCntlineDfrmTimCntIndex_Type()
)
pm10010mptCntlineDfrmTimCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCntlineDfrmTimCntIndex.setStatus("current")
_Pm10010mptCntlineDfrmTimCntValuePortn_Type = Counter64
_Pm10010mptCntlineDfrmTimCntValuePortn_Object = MibTableColumn
pm10010mptCntlineDfrmTimCntValuePortn = _Pm10010mptCntlineDfrmTimCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4, 3, 195, 1, 2),
    _Pm10010mptCntlineDfrmTimCntValuePortn_Type()
)
pm10010mptCntlineDfrmTimCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCntlineDfrmTimCntValuePortn.setStatus("current")
_Pm10010mptCntlineDfrmTimCntErrorPortn_Type = EkiOnOff
_Pm10010mptCntlineDfrmTimCntErrorPortn_Object = MibTableColumn
pm10010mptCntlineDfrmTimCntErrorPortn = _Pm10010mptCntlineDfrmTimCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4, 3, 195, 1, 3),
    _Pm10010mptCntlineDfrmTimCntErrorPortn_Type()
)
pm10010mptCntlineDfrmTimCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCntlineDfrmTimCntErrorPortn.setStatus("current")
_Pm10010mptCntlineDfrmTimCntOverloadPortn_Type = EkiOnOff
_Pm10010mptCntlineDfrmTimCntOverloadPortn_Object = MibTableColumn
pm10010mptCntlineDfrmTimCntOverloadPortn = _Pm10010mptCntlineDfrmTimCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4, 3, 195, 1, 4),
    _Pm10010mptCntlineDfrmTimCntOverloadPortn_Type()
)
pm10010mptCntlineDfrmTimCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCntlineDfrmTimCntOverloadPortn.setStatus("current")
_Pm10010mptCntlocalLineTrscvFecCorrectedErrorCounterTable_Object = MibTable
pm10010mptCntlocalLineTrscvFecCorrectedErrorCounterTable = _Pm10010mptCntlocalLineTrscvFecCorrectedErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4, 3, 196)
)
if mibBuilder.loadTexts:
    pm10010mptCntlocalLineTrscvFecCorrectedErrorCounterTable.setStatus("current")
_Pm10010mptCntlocalLineTrscvFecCorrectedErrorCounterEntry_Object = MibTableRow
pm10010mptCntlocalLineTrscvFecCorrectedErrorCounterEntry = _Pm10010mptCntlocalLineTrscvFecCorrectedErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4, 3, 196, 1)
)
pm10010mptCntlocalLineTrscvFecCorrectedErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptCntlocalLineTrscvFecCorrectedErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptCntlocalLineTrscvFecCorrectedErrorCounterEntry.setStatus("current")


class _Pm10010mptCntlocalLineTrscvFecCorrectedErrorCounterIndex_Type(Integer32):
    """Custom type pm10010mptCntlocalLineTrscvFecCorrectedErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptCntlocalLineTrscvFecCorrectedErrorCounterIndex_Type.__name__ = "Integer32"
_Pm10010mptCntlocalLineTrscvFecCorrectedErrorCounterIndex_Object = MibTableColumn
pm10010mptCntlocalLineTrscvFecCorrectedErrorCounterIndex = _Pm10010mptCntlocalLineTrscvFecCorrectedErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4, 3, 196, 1, 1),
    _Pm10010mptCntlocalLineTrscvFecCorrectedErrorCounterIndex_Type()
)
pm10010mptCntlocalLineTrscvFecCorrectedErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCntlocalLineTrscvFecCorrectedErrorCounterIndex.setStatus("current")
_Pm10010mptCntlocalLineTrscvFecCorrectedErrorCounterValuePortn_Type = Counter64
_Pm10010mptCntlocalLineTrscvFecCorrectedErrorCounterValuePortn_Object = MibTableColumn
pm10010mptCntlocalLineTrscvFecCorrectedErrorCounterValuePortn = _Pm10010mptCntlocalLineTrscvFecCorrectedErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4, 3, 196, 1, 2),
    _Pm10010mptCntlocalLineTrscvFecCorrectedErrorCounterValuePortn_Type()
)
pm10010mptCntlocalLineTrscvFecCorrectedErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCntlocalLineTrscvFecCorrectedErrorCounterValuePortn.setStatus("current")
_Pm10010mptCntlocalLineTrscvFecCorrectedErrorCounterErrorPortn_Type = EkiOnOff
_Pm10010mptCntlocalLineTrscvFecCorrectedErrorCounterErrorPortn_Object = MibTableColumn
pm10010mptCntlocalLineTrscvFecCorrectedErrorCounterErrorPortn = _Pm10010mptCntlocalLineTrscvFecCorrectedErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4, 3, 196, 1, 3),
    _Pm10010mptCntlocalLineTrscvFecCorrectedErrorCounterErrorPortn_Type()
)
pm10010mptCntlocalLineTrscvFecCorrectedErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCntlocalLineTrscvFecCorrectedErrorCounterErrorPortn.setStatus("current")
_Pm10010mptCntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn_Type = EkiOnOff
_Pm10010mptCntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn_Object = MibTableColumn
pm10010mptCntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn = _Pm10010mptCntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4, 3, 196, 1, 4),
    _Pm10010mptCntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn_Type()
)
pm10010mptCntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn.setStatus("current")
_Pm10010mptCntlocalLineTrscvFecUncorrectedErrorCounterTable_Object = MibTable
pm10010mptCntlocalLineTrscvFecUncorrectedErrorCounterTable = _Pm10010mptCntlocalLineTrscvFecUncorrectedErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4, 3, 197)
)
if mibBuilder.loadTexts:
    pm10010mptCntlocalLineTrscvFecUncorrectedErrorCounterTable.setStatus("current")
_Pm10010mptCntlocalLineTrscvFecUncorrectedErrorCounterEntry_Object = MibTableRow
pm10010mptCntlocalLineTrscvFecUncorrectedErrorCounterEntry = _Pm10010mptCntlocalLineTrscvFecUncorrectedErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4, 3, 197, 1)
)
pm10010mptCntlocalLineTrscvFecUncorrectedErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptCntlocalLineTrscvFecUncorrectedErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptCntlocalLineTrscvFecUncorrectedErrorCounterEntry.setStatus("current")


class _Pm10010mptCntlocalLineTrscvFecUncorrectedErrorCounterIndex_Type(Integer32):
    """Custom type pm10010mptCntlocalLineTrscvFecUncorrectedErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptCntlocalLineTrscvFecUncorrectedErrorCounterIndex_Type.__name__ = "Integer32"
_Pm10010mptCntlocalLineTrscvFecUncorrectedErrorCounterIndex_Object = MibTableColumn
pm10010mptCntlocalLineTrscvFecUncorrectedErrorCounterIndex = _Pm10010mptCntlocalLineTrscvFecUncorrectedErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4, 3, 197, 1, 1),
    _Pm10010mptCntlocalLineTrscvFecUncorrectedErrorCounterIndex_Type()
)
pm10010mptCntlocalLineTrscvFecUncorrectedErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCntlocalLineTrscvFecUncorrectedErrorCounterIndex.setStatus("current")
_Pm10010mptCntlocalLineTrscvFecUncorrectedErrorCounterValuePortn_Type = Counter64
_Pm10010mptCntlocalLineTrscvFecUncorrectedErrorCounterValuePortn_Object = MibTableColumn
pm10010mptCntlocalLineTrscvFecUncorrectedErrorCounterValuePortn = _Pm10010mptCntlocalLineTrscvFecUncorrectedErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4, 3, 197, 1, 2),
    _Pm10010mptCntlocalLineTrscvFecUncorrectedErrorCounterValuePortn_Type()
)
pm10010mptCntlocalLineTrscvFecUncorrectedErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCntlocalLineTrscvFecUncorrectedErrorCounterValuePortn.setStatus("current")
_Pm10010mptCntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn_Type = EkiOnOff
_Pm10010mptCntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn_Object = MibTableColumn
pm10010mptCntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn = _Pm10010mptCntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4, 3, 197, 1, 3),
    _Pm10010mptCntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn_Type()
)
pm10010mptCntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn.setStatus("current")
_Pm10010mptCntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn_Type = EkiOnOff
_Pm10010mptCntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn_Object = MibTableColumn
pm10010mptCntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn = _Pm10010mptCntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 4, 3, 197, 1, 4),
    _Pm10010mptCntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn_Type()
)
pm10010mptCntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn.setStatus("current")
_Pm10010mptcontrolsWrite_ObjectIdentity = ObjectIdentity
pm10010mptcontrolsWrite = _Pm10010mptcontrolsWrite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6)
)
_Pm10010mptCtrlOther_ObjectIdentity = ObjectIdentity
pm10010mptCtrlOther = _Pm10010mptCtrlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 1)
)
_Pm10010mptCtrlconfMgnt1_ObjectIdentity = ObjectIdentity
pm10010mptCtrlconfMgnt1 = _Pm10010mptCtrlconfMgnt1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 1, 1)
)
_Pm10010mptCtrlConf1Load1_Type = EkiOnOff
_Pm10010mptCtrlConf1Load1_Object = MibScalar
pm10010mptCtrlConf1Load1 = _Pm10010mptCtrlConf1Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 1, 1, 1),
    _Pm10010mptCtrlConf1Load1_Type()
)
pm10010mptCtrlConf1Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptCtrlConf1Load1.setStatus("current")
_Pm10010mptCtrlConf2Load1_Type = EkiOnOff
_Pm10010mptCtrlConf2Load1_Object = MibScalar
pm10010mptCtrlConf2Load1 = _Pm10010mptCtrlConf2Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 1, 1, 2),
    _Pm10010mptCtrlConf2Load1_Type()
)
pm10010mptCtrlConf2Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptCtrlConf2Load1.setStatus("current")
_Pm10010mptCtrlConf2Flash1_Type = EkiOnOff
_Pm10010mptCtrlConf2Flash1_Object = MibScalar
pm10010mptCtrlConf2Flash1 = _Pm10010mptCtrlConf2Flash1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 1, 1, 10),
    _Pm10010mptCtrlConf2Flash1_Type()
)
pm10010mptCtrlConf2Flash1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptCtrlConf2Flash1.setStatus("current")
_Pm10010mptCtrlConf2Clear1_Type = EkiOnOff
_Pm10010mptCtrlConf2Clear1_Object = MibScalar
pm10010mptCtrlConf2Clear1 = _Pm10010mptCtrlConf2Clear1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 1, 1, 14),
    _Pm10010mptCtrlConf2Clear1_Type()
)
pm10010mptCtrlConf2Clear1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptCtrlConf2Clear1.setStatus("current")
_Pm10010mptCtrlsynth4_ObjectIdentity = ObjectIdentity
pm10010mptCtrlsynth4 = _Pm10010mptCtrlsynth4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 1, 4)
)
_Pm10010mptCtrlCorrelatOn_Type = EkiOnOff
_Pm10010mptCtrlCorrelatOn_Object = MibScalar
pm10010mptCtrlCorrelatOn = _Pm10010mptCtrlCorrelatOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 1, 4, 1),
    _Pm10010mptCtrlCorrelatOn_Type()
)
pm10010mptCtrlCorrelatOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptCtrlCorrelatOn.setStatus("current")
_Pm10010mptCtrlCorrelatOff_Type = EkiOnOff
_Pm10010mptCtrlCorrelatOff_Object = MibScalar
pm10010mptCtrlCorrelatOff = _Pm10010mptCtrlCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 1, 4, 2),
    _Pm10010mptCtrlCorrelatOff_Type()
)
pm10010mptCtrlCorrelatOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptCtrlCorrelatOff.setStatus("current")
_Pm10010mptCtrlswMgnt_ObjectIdentity = ObjectIdentity
pm10010mptCtrlswMgnt = _Pm10010mptCtrlswMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 1, 5)
)
_Pm10010mptCtrlColdReset_Type = EkiOnOff
_Pm10010mptCtrlColdReset_Object = MibScalar
pm10010mptCtrlColdReset = _Pm10010mptCtrlColdReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 1, 5, 2),
    _Pm10010mptCtrlColdReset_Type()
)
pm10010mptCtrlColdReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptCtrlColdReset.setStatus("current")
_Pm10010mptCtrlWarmReset_Type = EkiOnOff
_Pm10010mptCtrlWarmReset_Object = MibScalar
pm10010mptCtrlWarmReset = _Pm10010mptCtrlWarmReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 1, 5, 3),
    _Pm10010mptCtrlWarmReset_Type()
)
pm10010mptCtrlWarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptCtrlWarmReset.setStatus("current")
_Pm10010mptCtrlLoadSwBank1_Type = EkiOnOff
_Pm10010mptCtrlLoadSwBank1_Object = MibScalar
pm10010mptCtrlLoadSwBank1 = _Pm10010mptCtrlLoadSwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 1, 5, 5),
    _Pm10010mptCtrlLoadSwBank1_Type()
)
pm10010mptCtrlLoadSwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptCtrlLoadSwBank1.setStatus("current")
_Pm10010mptCtrlLoadSwBank2_Type = EkiOnOff
_Pm10010mptCtrlLoadSwBank2_Object = MibScalar
pm10010mptCtrlLoadSwBank2 = _Pm10010mptCtrlLoadSwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 1, 5, 6),
    _Pm10010mptCtrlLoadSwBank2_Type()
)
pm10010mptCtrlLoadSwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptCtrlLoadSwBank2.setStatus("current")
_Pm10010mptCtrlgwMgnt_ObjectIdentity = ObjectIdentity
pm10010mptCtrlgwMgnt = _Pm10010mptCtrlgwMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 1, 6)
)
_Pm10010mptCtrlCurrentGwReset_Type = EkiOnOff
_Pm10010mptCtrlCurrentGwReset_Object = MibScalar
pm10010mptCtrlCurrentGwReset = _Pm10010mptCtrlCurrentGwReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 1, 6, 1),
    _Pm10010mptCtrlCurrentGwReset_Type()
)
pm10010mptCtrlCurrentGwReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptCtrlCurrentGwReset.setStatus("current")
_Pm10010mptCtrlLoadGwBank1_Type = EkiOnOff
_Pm10010mptCtrlLoadGwBank1_Object = MibScalar
pm10010mptCtrlLoadGwBank1 = _Pm10010mptCtrlLoadGwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 1, 6, 5),
    _Pm10010mptCtrlLoadGwBank1_Type()
)
pm10010mptCtrlLoadGwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptCtrlLoadGwBank1.setStatus("current")
_Pm10010mptCtrlLoadGwBank2_Type = EkiOnOff
_Pm10010mptCtrlLoadGwBank2_Object = MibScalar
pm10010mptCtrlLoadGwBank2 = _Pm10010mptCtrlLoadGwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 1, 6, 6),
    _Pm10010mptCtrlLoadGwBank2_Type()
)
pm10010mptCtrlLoadGwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptCtrlLoadGwBank2.setStatus("current")
_Pm10010mptCtrlLoadGwBank3_Type = EkiOnOff
_Pm10010mptCtrlLoadGwBank3_Object = MibScalar
pm10010mptCtrlLoadGwBank3 = _Pm10010mptCtrlLoadGwBank3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 1, 6, 7),
    _Pm10010mptCtrlLoadGwBank3_Type()
)
pm10010mptCtrlLoadGwBank3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptCtrlLoadGwBank3.setStatus("current")
_Pm10010mptCtrlLoadGwBank4_Type = EkiOnOff
_Pm10010mptCtrlLoadGwBank4_Object = MibScalar
pm10010mptCtrlLoadGwBank4 = _Pm10010mptCtrlLoadGwBank4_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 1, 6, 8),
    _Pm10010mptCtrlLoadGwBank4_Type()
)
pm10010mptCtrlLoadGwBank4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptCtrlLoadGwBank4.setStatus("current")
_Pm10010mptCtrlledTest_ObjectIdentity = ObjectIdentity
pm10010mptCtrlledTest = _Pm10010mptCtrlledTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 1, 192)
)
_Pm10010mptCtrlGreenLed_Type = EkiOnOff
_Pm10010mptCtrlGreenLed_Object = MibScalar
pm10010mptCtrlGreenLed = _Pm10010mptCtrlGreenLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 1, 192, 1),
    _Pm10010mptCtrlGreenLed_Type()
)
pm10010mptCtrlGreenLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptCtrlGreenLed.setStatus("current")
_Pm10010mptCtrlRedLed_Type = EkiOnOff
_Pm10010mptCtrlRedLed_Object = MibScalar
pm10010mptCtrlRedLed = _Pm10010mptCtrlRedLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 1, 192, 2),
    _Pm10010mptCtrlRedLed_Type()
)
pm10010mptCtrlRedLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptCtrlRedLed.setStatus("current")
_Pm10010mptCtrlLedOff_Type = EkiOnOff
_Pm10010mptCtrlLedOff_Object = MibScalar
pm10010mptCtrlLedOff = _Pm10010mptCtrlLedOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 1, 192, 3),
    _Pm10010mptCtrlLedOff_Type()
)
pm10010mptCtrlLedOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptCtrlLedOff.setStatus("current")
_Pm10010mptCtrlinitSwitchMarvell_ObjectIdentity = ObjectIdentity
pm10010mptCtrlinitSwitchMarvell = _Pm10010mptCtrlinitSwitchMarvell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 1, 201)
)
_Pm10010mptCtrlInitSwitchMarvell_Type = EkiOnOff
_Pm10010mptCtrlInitSwitchMarvell_Object = MibScalar
pm10010mptCtrlInitSwitchMarvell = _Pm10010mptCtrlInitSwitchMarvell_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 1, 201, 1),
    _Pm10010mptCtrlInitSwitchMarvell_Type()
)
pm10010mptCtrlInitSwitchMarvell.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptCtrlInitSwitchMarvell.setStatus("current")
_Pm10010mptCtrlresetCount_ObjectIdentity = ObjectIdentity
pm10010mptCtrlresetCount = _Pm10010mptCtrlresetCount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 1, 259)
)
_Pm10010mptCtrlResetcount_Type = EkiOnOff
_Pm10010mptCtrlResetcount_Object = MibScalar
pm10010mptCtrlResetcount = _Pm10010mptCtrlResetcount_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 1, 259, 1),
    _Pm10010mptCtrlResetcount_Type()
)
pm10010mptCtrlResetcount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptCtrlResetcount.setStatus("current")
_Pm10010mptCtrlresetRmon_ObjectIdentity = ObjectIdentity
pm10010mptCtrlresetRmon = _Pm10010mptCtrlresetRmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 1, 260)
)
_Pm10010mptCtrlResetrmon_Type = EkiOnOff
_Pm10010mptCtrlResetrmon_Object = MibScalar
pm10010mptCtrlResetrmon = _Pm10010mptCtrlResetrmon_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 1, 260, 1),
    _Pm10010mptCtrlResetrmon_Type()
)
pm10010mptCtrlResetrmon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptCtrlResetrmon.setStatus("current")
_Pm10010mptCtrlresetMeasurements_ObjectIdentity = ObjectIdentity
pm10010mptCtrlresetMeasurements = _Pm10010mptCtrlresetMeasurements_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 1, 261)
)
_Pm10010mptCtrlResetmeasurements_Type = EkiOnOff
_Pm10010mptCtrlResetmeasurements_Object = MibScalar
pm10010mptCtrlResetmeasurements = _Pm10010mptCtrlResetmeasurements_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 1, 261, 1),
    _Pm10010mptCtrlResetmeasurements_Type()
)
pm10010mptCtrlResetmeasurements.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptCtrlResetmeasurements.setStatus("current")
_Pm10010mptCtrlClient_ObjectIdentity = ObjectIdentity
pm10010mptCtrlClient = _Pm10010mptCtrlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 2)
)
_Pm10010mptCtrlaccessLoopTable_Object = MibTable
pm10010mptCtrlaccessLoopTable = _Pm10010mptCtrlaccessLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 2, 16)
)
if mibBuilder.loadTexts:
    pm10010mptCtrlaccessLoopTable.setStatus("current")
_Pm10010mptCtrlaccessLoopEntry_Object = MibTableRow
pm10010mptCtrlaccessLoopEntry = _Pm10010mptCtrlaccessLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 2, 16, 1)
)
pm10010mptCtrlaccessLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptCtrlaccessLoopIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptCtrlaccessLoopEntry.setStatus("current")


class _Pm10010mptCtrlaccessLoopIndex_Type(Integer32):
    """Custom type pm10010mptCtrlaccessLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptCtrlaccessLoopIndex_Type.__name__ = "Integer32"
_Pm10010mptCtrlaccessLoopIndex_Object = MibTableColumn
pm10010mptCtrlaccessLoopIndex = _Pm10010mptCtrlaccessLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 2, 16, 1, 1),
    _Pm10010mptCtrlaccessLoopIndex_Type()
)
pm10010mptCtrlaccessLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCtrlaccessLoopIndex.setStatus("current")
_Pm10010mptCtrlaccessLoopPortn_Type = EkiState
_Pm10010mptCtrlaccessLoopPortn_Object = MibTableColumn
pm10010mptCtrlaccessLoopPortn = _Pm10010mptCtrlaccessLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 2, 16, 1, 2),
    _Pm10010mptCtrlaccessLoopPortn_Type()
)
pm10010mptCtrlaccessLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptCtrlaccessLoopPortn.setStatus("current")
_Pm10010mptCtrlclientLoopToLineTable_Object = MibTable
pm10010mptCtrlclientLoopToLineTable = _Pm10010mptCtrlclientLoopToLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 2, 17)
)
if mibBuilder.loadTexts:
    pm10010mptCtrlclientLoopToLineTable.setStatus("current")
_Pm10010mptCtrlclientLoopToLineEntry_Object = MibTableRow
pm10010mptCtrlclientLoopToLineEntry = _Pm10010mptCtrlclientLoopToLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 2, 17, 1)
)
pm10010mptCtrlclientLoopToLineEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptCtrlclientLoopToLineIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptCtrlclientLoopToLineEntry.setStatus("current")


class _Pm10010mptCtrlclientLoopToLineIndex_Type(Integer32):
    """Custom type pm10010mptCtrlclientLoopToLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptCtrlclientLoopToLineIndex_Type.__name__ = "Integer32"
_Pm10010mptCtrlclientLoopToLineIndex_Object = MibTableColumn
pm10010mptCtrlclientLoopToLineIndex = _Pm10010mptCtrlclientLoopToLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 2, 17, 1, 1),
    _Pm10010mptCtrlclientLoopToLineIndex_Type()
)
pm10010mptCtrlclientLoopToLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCtrlclientLoopToLineIndex.setStatus("current")
_Pm10010mptCtrlclientLoopToLinePortn_Type = EkiState
_Pm10010mptCtrlclientLoopToLinePortn_Object = MibTableColumn
pm10010mptCtrlclientLoopToLinePortn = _Pm10010mptCtrlclientLoopToLinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 2, 17, 1, 2),
    _Pm10010mptCtrlclientLoopToLinePortn_Type()
)
pm10010mptCtrlclientLoopToLinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptCtrlclientLoopToLinePortn.setStatus("current")
_Pm10010mptCtrlcsfUpInsTable_Object = MibTable
pm10010mptCtrlcsfUpInsTable = _Pm10010mptCtrlcsfUpInsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 2, 21)
)
if mibBuilder.loadTexts:
    pm10010mptCtrlcsfUpInsTable.setStatus("current")
_Pm10010mptCtrlcsfUpInsEntry_Object = MibTableRow
pm10010mptCtrlcsfUpInsEntry = _Pm10010mptCtrlcsfUpInsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 2, 21, 1)
)
pm10010mptCtrlcsfUpInsEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptCtrlcsfUpInsIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptCtrlcsfUpInsEntry.setStatus("current")


class _Pm10010mptCtrlcsfUpInsIndex_Type(Integer32):
    """Custom type pm10010mptCtrlcsfUpInsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptCtrlcsfUpInsIndex_Type.__name__ = "Integer32"
_Pm10010mptCtrlcsfUpInsIndex_Object = MibTableColumn
pm10010mptCtrlcsfUpInsIndex = _Pm10010mptCtrlcsfUpInsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 2, 21, 1, 1),
    _Pm10010mptCtrlcsfUpInsIndex_Type()
)
pm10010mptCtrlcsfUpInsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCtrlcsfUpInsIndex.setStatus("current")
_Pm10010mptCtrlcsfUpInsPortn_Type = EkiState
_Pm10010mptCtrlcsfUpInsPortn_Object = MibTableColumn
pm10010mptCtrlcsfUpInsPortn = _Pm10010mptCtrlcsfUpInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 2, 21, 1, 2),
    _Pm10010mptCtrlcsfUpInsPortn_Type()
)
pm10010mptCtrlcsfUpInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptCtrlcsfUpInsPortn.setStatus("current")
_Pm10010mptCtrlcaisDwInsTable_Object = MibTable
pm10010mptCtrlcaisDwInsTable = _Pm10010mptCtrlcaisDwInsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 2, 22)
)
if mibBuilder.loadTexts:
    pm10010mptCtrlcaisDwInsTable.setStatus("current")
_Pm10010mptCtrlcaisDwInsEntry_Object = MibTableRow
pm10010mptCtrlcaisDwInsEntry = _Pm10010mptCtrlcaisDwInsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 2, 22, 1)
)
pm10010mptCtrlcaisDwInsEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptCtrlcaisDwInsIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptCtrlcaisDwInsEntry.setStatus("current")


class _Pm10010mptCtrlcaisDwInsIndex_Type(Integer32):
    """Custom type pm10010mptCtrlcaisDwInsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptCtrlcaisDwInsIndex_Type.__name__ = "Integer32"
_Pm10010mptCtrlcaisDwInsIndex_Object = MibTableColumn
pm10010mptCtrlcaisDwInsIndex = _Pm10010mptCtrlcaisDwInsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 2, 22, 1, 1),
    _Pm10010mptCtrlcaisDwInsIndex_Type()
)
pm10010mptCtrlcaisDwInsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCtrlcaisDwInsIndex.setStatus("current")
_Pm10010mptCtrlcaisDwInsPortn_Type = EkiState
_Pm10010mptCtrlcaisDwInsPortn_Object = MibTableColumn
pm10010mptCtrlcaisDwInsPortn = _Pm10010mptCtrlcaisDwInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 2, 22, 1, 2),
    _Pm10010mptCtrlcaisDwInsPortn_Type()
)
pm10010mptCtrlcaisDwInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptCtrlcaisDwInsPortn.setStatus("current")
_Pm10010mptCtrlclientResetAllCountTable_Object = MibTable
pm10010mptCtrlclientResetAllCountTable = _Pm10010mptCtrlclientResetAllCountTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 2, 262)
)
if mibBuilder.loadTexts:
    pm10010mptCtrlclientResetAllCountTable.setStatus("current")
_Pm10010mptCtrlclientResetAllCountEntry_Object = MibTableRow
pm10010mptCtrlclientResetAllCountEntry = _Pm10010mptCtrlclientResetAllCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 2, 262, 1)
)
pm10010mptCtrlclientResetAllCountEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptCtrlclientResetAllCountIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptCtrlclientResetAllCountEntry.setStatus("current")


class _Pm10010mptCtrlclientResetAllCountIndex_Type(Integer32):
    """Custom type pm10010mptCtrlclientResetAllCountIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptCtrlclientResetAllCountIndex_Type.__name__ = "Integer32"
_Pm10010mptCtrlclientResetAllCountIndex_Object = MibTableColumn
pm10010mptCtrlclientResetAllCountIndex = _Pm10010mptCtrlclientResetAllCountIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 2, 262, 1, 1),
    _Pm10010mptCtrlclientResetAllCountIndex_Type()
)
pm10010mptCtrlclientResetAllCountIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCtrlclientResetAllCountIndex.setStatus("current")
_Pm10010mptCtrlclientResetAllCountsPortn_Type = EkiState
_Pm10010mptCtrlclientResetAllCountsPortn_Object = MibTableColumn
pm10010mptCtrlclientResetAllCountsPortn = _Pm10010mptCtrlclientResetAllCountsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 2, 262, 1, 2),
    _Pm10010mptCtrlclientResetAllCountsPortn_Type()
)
pm10010mptCtrlclientResetAllCountsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptCtrlclientResetAllCountsPortn.setStatus("current")
_Pm10010mptCtrlLine_ObjectIdentity = ObjectIdentity
pm10010mptCtrlLine = _Pm10010mptCtrlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 3)
)
_Pm10010mptCtrlcommAccessLoopTable_Object = MibTable
pm10010mptCtrlcommAccessLoopTable = _Pm10010mptCtrlcommAccessLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 3, 64)
)
if mibBuilder.loadTexts:
    pm10010mptCtrlcommAccessLoopTable.setStatus("current")
_Pm10010mptCtrlcommAccessLoopEntry_Object = MibTableRow
pm10010mptCtrlcommAccessLoopEntry = _Pm10010mptCtrlcommAccessLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 3, 64, 1)
)
pm10010mptCtrlcommAccessLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptCtrlcommAccessLoopIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptCtrlcommAccessLoopEntry.setStatus("current")


class _Pm10010mptCtrlcommAccessLoopIndex_Type(Integer32):
    """Custom type pm10010mptCtrlcommAccessLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptCtrlcommAccessLoopIndex_Type.__name__ = "Integer32"
_Pm10010mptCtrlcommAccessLoopIndex_Object = MibTableColumn
pm10010mptCtrlcommAccessLoopIndex = _Pm10010mptCtrlcommAccessLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 3, 64, 1, 1),
    _Pm10010mptCtrlcommAccessLoopIndex_Type()
)
pm10010mptCtrlcommAccessLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCtrlcommAccessLoopIndex.setStatus("current")
_Pm10010mptCtrlcommAccessLoopPortn_Type = EkiState
_Pm10010mptCtrlcommAccessLoopPortn_Object = MibTableColumn
pm10010mptCtrlcommAccessLoopPortn = _Pm10010mptCtrlcommAccessLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 3, 64, 1, 2),
    _Pm10010mptCtrlcommAccessLoopPortn_Type()
)
pm10010mptCtrlcommAccessLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptCtrlcommAccessLoopPortn.setStatus("current")
_Pm10010mptCtrllineLoopTable_Object = MibTable
pm10010mptCtrllineLoopTable = _Pm10010mptCtrllineLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 3, 66)
)
if mibBuilder.loadTexts:
    pm10010mptCtrllineLoopTable.setStatus("current")
_Pm10010mptCtrllineLoopEntry_Object = MibTableRow
pm10010mptCtrllineLoopEntry = _Pm10010mptCtrllineLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 3, 66, 1)
)
pm10010mptCtrllineLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptCtrllineLoopIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptCtrllineLoopEntry.setStatus("current")


class _Pm10010mptCtrllineLoopIndex_Type(Integer32):
    """Custom type pm10010mptCtrllineLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptCtrllineLoopIndex_Type.__name__ = "Integer32"
_Pm10010mptCtrllineLoopIndex_Object = MibTableColumn
pm10010mptCtrllineLoopIndex = _Pm10010mptCtrllineLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 3, 66, 1, 1),
    _Pm10010mptCtrllineLoopIndex_Type()
)
pm10010mptCtrllineLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCtrllineLoopIndex.setStatus("current")
_Pm10010mptCtrllineLoopPortn_Type = EkiState
_Pm10010mptCtrllineLoopPortn_Object = MibTableColumn
pm10010mptCtrllineLoopPortn = _Pm10010mptCtrllineLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 3, 66, 1, 2),
    _Pm10010mptCtrllineLoopPortn_Type()
)
pm10010mptCtrllineLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptCtrllineLoopPortn.setStatus("current")
_Pm10010mptCtrlfecDisableTable_Object = MibTable
pm10010mptCtrlfecDisableTable = _Pm10010mptCtrlfecDisableTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 3, 69)
)
if mibBuilder.loadTexts:
    pm10010mptCtrlfecDisableTable.setStatus("current")
_Pm10010mptCtrlfecDisableEntry_Object = MibTableRow
pm10010mptCtrlfecDisableEntry = _Pm10010mptCtrlfecDisableEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 3, 69, 1)
)
pm10010mptCtrlfecDisableEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptCtrlfecDisableIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptCtrlfecDisableEntry.setStatus("current")


class _Pm10010mptCtrlfecDisableIndex_Type(Integer32):
    """Custom type pm10010mptCtrlfecDisableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptCtrlfecDisableIndex_Type.__name__ = "Integer32"
_Pm10010mptCtrlfecDisableIndex_Object = MibTableColumn
pm10010mptCtrlfecDisableIndex = _Pm10010mptCtrlfecDisableIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 3, 69, 1, 1),
    _Pm10010mptCtrlfecDisableIndex_Type()
)
pm10010mptCtrlfecDisableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCtrlfecDisableIndex.setStatus("current")
_Pm10010mptCtrlfecDisablePortn_Type = EkiState
_Pm10010mptCtrlfecDisablePortn_Object = MibTableColumn
pm10010mptCtrlfecDisablePortn = _Pm10010mptCtrlfecDisablePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 3, 69, 1, 2),
    _Pm10010mptCtrlfecDisablePortn_Type()
)
pm10010mptCtrlfecDisablePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptCtrlfecDisablePortn.setStatus("current")
_Pm10010mptCtrlmsaLineLoopTable_Object = MibTable
pm10010mptCtrlmsaLineLoopTable = _Pm10010mptCtrlmsaLineLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 3, 209)
)
if mibBuilder.loadTexts:
    pm10010mptCtrlmsaLineLoopTable.setStatus("current")
_Pm10010mptCtrlmsaLineLoopEntry_Object = MibTableRow
pm10010mptCtrlmsaLineLoopEntry = _Pm10010mptCtrlmsaLineLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 3, 209, 1)
)
pm10010mptCtrlmsaLineLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptCtrlmsaLineLoopIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptCtrlmsaLineLoopEntry.setStatus("current")


class _Pm10010mptCtrlmsaLineLoopIndex_Type(Integer32):
    """Custom type pm10010mptCtrlmsaLineLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptCtrlmsaLineLoopIndex_Type.__name__ = "Integer32"
_Pm10010mptCtrlmsaLineLoopIndex_Object = MibTableColumn
pm10010mptCtrlmsaLineLoopIndex = _Pm10010mptCtrlmsaLineLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 3, 209, 1, 1),
    _Pm10010mptCtrlmsaLineLoopIndex_Type()
)
pm10010mptCtrlmsaLineLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCtrlmsaLineLoopIndex.setStatus("current")
_Pm10010mptCtrlmsaLineLoopPortn_Type = EkiState
_Pm10010mptCtrlmsaLineLoopPortn_Object = MibTableColumn
pm10010mptCtrlmsaLineLoopPortn = _Pm10010mptCtrlmsaLineLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 3, 209, 1, 2),
    _Pm10010mptCtrlmsaLineLoopPortn_Type()
)
pm10010mptCtrlmsaLineLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptCtrlmsaLineLoopPortn.setStatus("current")
_Pm10010mptCtrlmsaTxResetTable_Object = MibTable
pm10010mptCtrlmsaTxResetTable = _Pm10010mptCtrlmsaTxResetTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 3, 210)
)
if mibBuilder.loadTexts:
    pm10010mptCtrlmsaTxResetTable.setStatus("current")
_Pm10010mptCtrlmsaTxResetEntry_Object = MibTableRow
pm10010mptCtrlmsaTxResetEntry = _Pm10010mptCtrlmsaTxResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 3, 210, 1)
)
pm10010mptCtrlmsaTxResetEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptCtrlmsaTxResetIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptCtrlmsaTxResetEntry.setStatus("current")


class _Pm10010mptCtrlmsaTxResetIndex_Type(Integer32):
    """Custom type pm10010mptCtrlmsaTxResetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptCtrlmsaTxResetIndex_Type.__name__ = "Integer32"
_Pm10010mptCtrlmsaTxResetIndex_Object = MibTableColumn
pm10010mptCtrlmsaTxResetIndex = _Pm10010mptCtrlmsaTxResetIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 3, 210, 1, 1),
    _Pm10010mptCtrlmsaTxResetIndex_Type()
)
pm10010mptCtrlmsaTxResetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCtrlmsaTxResetIndex.setStatus("current")
_Pm10010mptCtrlmsaTxResetPortn_Type = EkiState
_Pm10010mptCtrlmsaTxResetPortn_Object = MibTableColumn
pm10010mptCtrlmsaTxResetPortn = _Pm10010mptCtrlmsaTxResetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 3, 210, 1, 2),
    _Pm10010mptCtrlmsaTxResetPortn_Type()
)
pm10010mptCtrlmsaTxResetPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptCtrlmsaTxResetPortn.setStatus("current")
_Pm10010mptCtrlmsaRxResetTable_Object = MibTable
pm10010mptCtrlmsaRxResetTable = _Pm10010mptCtrlmsaRxResetTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 3, 211)
)
if mibBuilder.loadTexts:
    pm10010mptCtrlmsaRxResetTable.setStatus("current")
_Pm10010mptCtrlmsaRxResetEntry_Object = MibTableRow
pm10010mptCtrlmsaRxResetEntry = _Pm10010mptCtrlmsaRxResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 3, 211, 1)
)
pm10010mptCtrlmsaRxResetEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptCtrlmsaRxResetIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptCtrlmsaRxResetEntry.setStatus("current")


class _Pm10010mptCtrlmsaRxResetIndex_Type(Integer32):
    """Custom type pm10010mptCtrlmsaRxResetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptCtrlmsaRxResetIndex_Type.__name__ = "Integer32"
_Pm10010mptCtrlmsaRxResetIndex_Object = MibTableColumn
pm10010mptCtrlmsaRxResetIndex = _Pm10010mptCtrlmsaRxResetIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 3, 211, 1, 1),
    _Pm10010mptCtrlmsaRxResetIndex_Type()
)
pm10010mptCtrlmsaRxResetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCtrlmsaRxResetIndex.setStatus("current")
_Pm10010mptCtrlmsaRxResetPortn_Type = EkiState
_Pm10010mptCtrlmsaRxResetPortn_Object = MibTableColumn
pm10010mptCtrlmsaRxResetPortn = _Pm10010mptCtrlmsaRxResetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 3, 211, 1, 2),
    _Pm10010mptCtrlmsaRxResetPortn_Type()
)
pm10010mptCtrlmsaRxResetPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptCtrlmsaRxResetPortn.setStatus("current")
_Pm10010mptCtrlmsaShutdownTable_Object = MibTable
pm10010mptCtrlmsaShutdownTable = _Pm10010mptCtrlmsaShutdownTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 3, 212)
)
if mibBuilder.loadTexts:
    pm10010mptCtrlmsaShutdownTable.setStatus("current")
_Pm10010mptCtrlmsaShutdownEntry_Object = MibTableRow
pm10010mptCtrlmsaShutdownEntry = _Pm10010mptCtrlmsaShutdownEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 3, 212, 1)
)
pm10010mptCtrlmsaShutdownEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptCtrlmsaShutdownIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptCtrlmsaShutdownEntry.setStatus("current")


class _Pm10010mptCtrlmsaShutdownIndex_Type(Integer32):
    """Custom type pm10010mptCtrlmsaShutdownIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptCtrlmsaShutdownIndex_Type.__name__ = "Integer32"
_Pm10010mptCtrlmsaShutdownIndex_Object = MibTableColumn
pm10010mptCtrlmsaShutdownIndex = _Pm10010mptCtrlmsaShutdownIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 3, 212, 1, 1),
    _Pm10010mptCtrlmsaShutdownIndex_Type()
)
pm10010mptCtrlmsaShutdownIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCtrlmsaShutdownIndex.setStatus("current")
_Pm10010mptCtrlmsaShutdownPortn_Type = EkiState
_Pm10010mptCtrlmsaShutdownPortn_Object = MibTableColumn
pm10010mptCtrlmsaShutdownPortn = _Pm10010mptCtrlmsaShutdownPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 3, 212, 1, 2),
    _Pm10010mptCtrlmsaShutdownPortn_Type()
)
pm10010mptCtrlmsaShutdownPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptCtrlmsaShutdownPortn.setStatus("current")
_Pm10010mptCtrllineResetAllCountTable_Object = MibTable
pm10010mptCtrllineResetAllCountTable = _Pm10010mptCtrllineResetAllCountTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 3, 263)
)
if mibBuilder.loadTexts:
    pm10010mptCtrllineResetAllCountTable.setStatus("current")
_Pm10010mptCtrllineResetAllCountEntry_Object = MibTableRow
pm10010mptCtrllineResetAllCountEntry = _Pm10010mptCtrllineResetAllCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 3, 263, 1)
)
pm10010mptCtrllineResetAllCountEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptCtrllineResetAllCountIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptCtrllineResetAllCountEntry.setStatus("current")


class _Pm10010mptCtrllineResetAllCountIndex_Type(Integer32):
    """Custom type pm10010mptCtrllineResetAllCountIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptCtrllineResetAllCountIndex_Type.__name__ = "Integer32"
_Pm10010mptCtrllineResetAllCountIndex_Object = MibTableColumn
pm10010mptCtrllineResetAllCountIndex = _Pm10010mptCtrllineResetAllCountIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 3, 263, 1, 1),
    _Pm10010mptCtrllineResetAllCountIndex_Type()
)
pm10010mptCtrllineResetAllCountIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCtrllineResetAllCountIndex.setStatus("current")
_Pm10010mptCtrllineResetAllCountsPortn_Type = EkiState
_Pm10010mptCtrllineResetAllCountsPortn_Object = MibTableColumn
pm10010mptCtrllineResetAllCountsPortn = _Pm10010mptCtrllineResetAllCountsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 6, 3, 263, 1, 2),
    _Pm10010mptCtrllineResetAllCountsPortn_Type()
)
pm10010mptCtrllineResetAllCountsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptCtrllineResetAllCountsPortn.setStatus("current")
_Pm10010mptri_ObjectIdentity = ObjectIdentity
pm10010mptri = _Pm10010mptri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 7)
)
_Pm10010mptriTable_ObjectIdentity = ObjectIdentity
pm10010mptriTable = _Pm10010mptriTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 7, 1)
)
_Pm10010mptRinvSfpTable_Object = MibTable
pm10010mptRinvSfpTable = _Pm10010mptRinvSfpTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 7, 1, 1)
)
if mibBuilder.loadTexts:
    pm10010mptRinvSfpTable.setStatus("current")
_Pm10010mptRinvSfpEntry_Object = MibTableRow
pm10010mptRinvSfpEntry = _Pm10010mptRinvSfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 7, 1, 1, 1)
)
pm10010mptRinvSfpEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptRinvSfpIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptRinvSfpEntry.setStatus("current")


class _Pm10010mptRinvSfpIndex_Type(Integer32):
    """Custom type pm10010mptRinvSfpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pm10010mptRinvSfpIndex_Type.__name__ = "Integer32"
_Pm10010mptRinvSfpIndex_Object = MibTableColumn
pm10010mptRinvSfpIndex = _Pm10010mptRinvSfpIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 7, 1, 1, 1, 1),
    _Pm10010mptRinvSfpIndex_Type()
)
pm10010mptRinvSfpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptRinvSfpIndex.setStatus("current")
_Pm10010mptRinvsfp_Type = DisplayString
_Pm10010mptRinvsfp_Object = MibTableColumn
pm10010mptRinvsfp = _Pm10010mptRinvsfp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 7, 1, 1, 1, 2),
    _Pm10010mptRinvsfp_Type()
)
pm10010mptRinvsfp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptRinvsfp.setStatus("current")
_Pm10010mptRinvLineTable_Object = MibTable
pm10010mptRinvLineTable = _Pm10010mptRinvLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 7, 1, 2)
)
if mibBuilder.loadTexts:
    pm10010mptRinvLineTable.setStatus("current")
_Pm10010mptRinvLineEntry_Object = MibTableRow
pm10010mptRinvLineEntry = _Pm10010mptRinvLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 7, 1, 2, 1)
)
pm10010mptRinvLineEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptRinvLineIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptRinvLineEntry.setStatus("current")


class _Pm10010mptRinvLineIndex_Type(Integer32):
    """Custom type pm10010mptRinvLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pm10010mptRinvLineIndex_Type.__name__ = "Integer32"
_Pm10010mptRinvLineIndex_Object = MibTableColumn
pm10010mptRinvLineIndex = _Pm10010mptRinvLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 7, 1, 2, 1, 1),
    _Pm10010mptRinvLineIndex_Type()
)
pm10010mptRinvLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptRinvLineIndex.setStatus("current")
_Pm10010mptRinvxfpLine_Type = DisplayString
_Pm10010mptRinvxfpLine_Object = MibTableColumn
pm10010mptRinvxfpLine = _Pm10010mptRinvxfpLine_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 7, 1, 2, 1, 2),
    _Pm10010mptRinvxfpLine_Type()
)
pm10010mptRinvxfpLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptRinvxfpLine.setStatus("current")
_Pm10010mptRinvReloadInventory_Type = EkiOnOff
_Pm10010mptRinvReloadInventory_Object = MibScalar
pm10010mptRinvReloadInventory = _Pm10010mptRinvReloadInventory_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 7, 2),
    _Pm10010mptRinvReloadInventory_Type()
)
pm10010mptRinvReloadInventory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptRinvReloadInventory.setStatus("current")
_Pm10010mptRinvHwPlatform_Type = DisplayString
_Pm10010mptRinvHwPlatform_Object = MibScalar
pm10010mptRinvHwPlatform = _Pm10010mptRinvHwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 7, 3),
    _Pm10010mptRinvHwPlatform_Type()
)
pm10010mptRinvHwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptRinvHwPlatform.setStatus("current")
_Pm10010mptRinvModulePlatform_Type = DisplayString
_Pm10010mptRinvModulePlatform_Object = MibScalar
pm10010mptRinvModulePlatform = _Pm10010mptRinvModulePlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 7, 4),
    _Pm10010mptRinvModulePlatform_Type()
)
pm10010mptRinvModulePlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptRinvModulePlatform.setStatus("current")
_Pm10010mptRinvSwPlatform_Type = DisplayString
_Pm10010mptRinvSwPlatform_Object = MibScalar
pm10010mptRinvSwPlatform = _Pm10010mptRinvSwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 7, 5),
    _Pm10010mptRinvSwPlatform_Type()
)
pm10010mptRinvSwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptRinvSwPlatform.setStatus("current")
_Pm10010mptRinvGwPlatform_Type = DisplayString
_Pm10010mptRinvGwPlatform_Object = MibScalar
pm10010mptRinvGwPlatform = _Pm10010mptRinvGwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 7, 6),
    _Pm10010mptRinvGwPlatform_Type()
)
pm10010mptRinvGwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptRinvGwPlatform.setStatus("current")
_Pm10010mptdownload_ObjectIdentity = ObjectIdentity
pm10010mptdownload = _Pm10010mptdownload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 8)
)
_Pm10010mptDwlOther_ObjectIdentity = ObjectIdentity
pm10010mptDwlOther = _Pm10010mptDwlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 8, 1)
)
_Pm10010mptDwlrestartProcess_ObjectIdentity = ObjectIdentity
pm10010mptDwlrestartProcess = _Pm10010mptDwlrestartProcess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 8, 1, 0)
)
_Pm10010mptDwlWarmRestartProcessed_Type = EkiOnOff
_Pm10010mptDwlWarmRestartProcessed_Object = MibScalar
pm10010mptDwlWarmRestartProcessed = _Pm10010mptDwlWarmRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 8, 1, 0, 1),
    _Pm10010mptDwlWarmRestartProcessed_Type()
)
pm10010mptDwlWarmRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptDwlWarmRestartProcessed.setStatus("current")
_Pm10010mptDwlColdRestartProcessed_Type = EkiOnOff
_Pm10010mptDwlColdRestartProcessed_Object = MibScalar
pm10010mptDwlColdRestartProcessed = _Pm10010mptDwlColdRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 8, 1, 0, 2),
    _Pm10010mptDwlColdRestartProcessed_Type()
)
pm10010mptDwlColdRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptDwlColdRestartProcessed.setStatus("current")
_Pm10010mptDwlswBanksUsed_ObjectIdentity = ObjectIdentity
pm10010mptDwlswBanksUsed = _Pm10010mptDwlswBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 8, 1, 1)
)
_Pm10010mptDwlSwBank1Used_Type = EkiOnOff
_Pm10010mptDwlSwBank1Used_Object = MibScalar
pm10010mptDwlSwBank1Used = _Pm10010mptDwlSwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 8, 1, 1, 1),
    _Pm10010mptDwlSwBank1Used_Type()
)
pm10010mptDwlSwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptDwlSwBank1Used.setStatus("current")
_Pm10010mptDwlSwBank2Used_Type = EkiOnOff
_Pm10010mptDwlSwBank2Used_Object = MibScalar
pm10010mptDwlSwBank2Used = _Pm10010mptDwlSwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 8, 1, 1, 2),
    _Pm10010mptDwlSwBank2Used_Type()
)
pm10010mptDwlSwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptDwlSwBank2Used.setStatus("current")
_Pm10010mptDwlSwBank1Notempty_Type = EkiOnOff
_Pm10010mptDwlSwBank1Notempty_Object = MibScalar
pm10010mptDwlSwBank1Notempty = _Pm10010mptDwlSwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 8, 1, 1, 5),
    _Pm10010mptDwlSwBank1Notempty_Type()
)
pm10010mptDwlSwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptDwlSwBank1Notempty.setStatus("current")
_Pm10010mptDwlSwBank2Notempty_Type = EkiOnOff
_Pm10010mptDwlSwBank2Notempty_Object = MibScalar
pm10010mptDwlSwBank2Notempty = _Pm10010mptDwlSwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 8, 1, 1, 6),
    _Pm10010mptDwlSwBank2Notempty_Type()
)
pm10010mptDwlSwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptDwlSwBank2Notempty.setStatus("current")
_Pm10010mptDwlgwBanksUsed_ObjectIdentity = ObjectIdentity
pm10010mptDwlgwBanksUsed = _Pm10010mptDwlgwBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 8, 1, 2)
)
_Pm10010mptDwlGwBank1Used_Type = EkiOnOff
_Pm10010mptDwlGwBank1Used_Object = MibScalar
pm10010mptDwlGwBank1Used = _Pm10010mptDwlGwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 8, 1, 2, 1),
    _Pm10010mptDwlGwBank1Used_Type()
)
pm10010mptDwlGwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptDwlGwBank1Used.setStatus("current")
_Pm10010mptDwlGwBank2Used_Type = EkiOnOff
_Pm10010mptDwlGwBank2Used_Object = MibScalar
pm10010mptDwlGwBank2Used = _Pm10010mptDwlGwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 8, 1, 2, 2),
    _Pm10010mptDwlGwBank2Used_Type()
)
pm10010mptDwlGwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptDwlGwBank2Used.setStatus("current")
_Pm10010mptDwlGwBank3Used_Type = EkiOnOff
_Pm10010mptDwlGwBank3Used_Object = MibScalar
pm10010mptDwlGwBank3Used = _Pm10010mptDwlGwBank3Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 8, 1, 2, 3),
    _Pm10010mptDwlGwBank3Used_Type()
)
pm10010mptDwlGwBank3Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptDwlGwBank3Used.setStatus("current")
_Pm10010mptDwlGwBank4Used_Type = EkiOnOff
_Pm10010mptDwlGwBank4Used_Object = MibScalar
pm10010mptDwlGwBank4Used = _Pm10010mptDwlGwBank4Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 8, 1, 2, 4),
    _Pm10010mptDwlGwBank4Used_Type()
)
pm10010mptDwlGwBank4Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptDwlGwBank4Used.setStatus("current")
_Pm10010mptDwlGwBank1Notempty_Type = EkiOnOff
_Pm10010mptDwlGwBank1Notempty_Object = MibScalar
pm10010mptDwlGwBank1Notempty = _Pm10010mptDwlGwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 8, 1, 2, 5),
    _Pm10010mptDwlGwBank1Notempty_Type()
)
pm10010mptDwlGwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptDwlGwBank1Notempty.setStatus("current")
_Pm10010mptDwlGwBank2Notempty_Type = EkiOnOff
_Pm10010mptDwlGwBank2Notempty_Object = MibScalar
pm10010mptDwlGwBank2Notempty = _Pm10010mptDwlGwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 8, 1, 2, 6),
    _Pm10010mptDwlGwBank2Notempty_Type()
)
pm10010mptDwlGwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptDwlGwBank2Notempty.setStatus("current")
_Pm10010mptDwlGwBank3Notempty_Type = EkiOnOff
_Pm10010mptDwlGwBank3Notempty_Object = MibScalar
pm10010mptDwlGwBank3Notempty = _Pm10010mptDwlGwBank3Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 8, 1, 2, 7),
    _Pm10010mptDwlGwBank3Notempty_Type()
)
pm10010mptDwlGwBank3Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptDwlGwBank3Notempty.setStatus("current")
_Pm10010mptDwlGwBank4Notempty_Type = EkiOnOff
_Pm10010mptDwlGwBank4Notempty_Object = MibScalar
pm10010mptDwlGwBank4Notempty = _Pm10010mptDwlGwBank4Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 8, 1, 2, 8),
    _Pm10010mptDwlGwBank4Notempty_Type()
)
pm10010mptDwlGwBank4Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptDwlGwBank4Notempty.setStatus("current")
_Pm10010mptDwlClient_ObjectIdentity = ObjectIdentity
pm10010mptDwlClient = _Pm10010mptDwlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 8, 2)
)
_Pm10010mptDwlLine_ObjectIdentity = ObjectIdentity
pm10010mptDwlLine = _Pm10010mptDwlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 8, 3)
)
_Pm10010mptConfig_ObjectIdentity = ObjectIdentity
pm10010mptConfig = _Pm10010mptConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 9)
)
_Pm10010mptCfgAccessCAisCsf_ObjectIdentity = ObjectIdentity
pm10010mptCfgAccessCAisCsf = _Pm10010mptCfgAccessCAisCsf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 9, 1)
)
_Pm10010mptCfgClientcaiscsfTable_Object = MibTable
pm10010mptCfgClientcaiscsfTable = _Pm10010mptCfgClientcaiscsfTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 9, 1, 1)
)
if mibBuilder.loadTexts:
    pm10010mptCfgClientcaiscsfTable.setStatus("current")
_Pm10010mptCfgClientcaiscsfEntry_Object = MibTableRow
pm10010mptCfgClientcaiscsfEntry = _Pm10010mptCfgClientcaiscsfEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 9, 1, 1, 1)
)
pm10010mptCfgClientcaiscsfEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptCfgClientcaiscsfIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptCfgClientcaiscsfEntry.setStatus("current")


class _Pm10010mptCfgClientcaiscsfIndex_Type(Integer32):
    """Custom type pm10010mptCfgClientcaiscsfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptCfgClientcaiscsfIndex_Type.__name__ = "Integer32"
_Pm10010mptCfgClientcaiscsfIndex_Object = MibTableColumn
pm10010mptCfgClientcaiscsfIndex = _Pm10010mptCfgClientcaiscsfIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 9, 1, 1, 1, 1),
    _Pm10010mptCfgClientcaiscsfIndex_Type()
)
pm10010mptCfgClientcaiscsfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCfgClientcaiscsfIndex.setStatus("current")


class _Pm10010mptCfgReservePortn_Type(Unsigned32):
    """Custom type pm10010mptCfgReservePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mptCfgReservePortn_Type.__name__ = "Unsigned32"
_Pm10010mptCfgReservePortn_Object = MibTableColumn
pm10010mptCfgReservePortn = _Pm10010mptCfgReservePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 9, 1, 1, 1, 3),
    _Pm10010mptCfgReservePortn_Type()
)
pm10010mptCfgReservePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptCfgReservePortn.setStatus("current")
_Pm10010mptCfgStartup_ObjectIdentity = ObjectIdentity
pm10010mptCfgStartup = _Pm10010mptCfgStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 9, 2)
)
_Pm10010mptCfgClientStartupTable_Object = MibTable
pm10010mptCfgClientStartupTable = _Pm10010mptCfgClientStartupTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 9, 2, 1)
)
if mibBuilder.loadTexts:
    pm10010mptCfgClientStartupTable.setStatus("current")
_Pm10010mptCfgClientStartupEntry_Object = MibTableRow
pm10010mptCfgClientStartupEntry = _Pm10010mptCfgClientStartupEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 9, 2, 1, 1)
)
pm10010mptCfgClientStartupEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptCfgClientStartupIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptCfgClientStartupEntry.setStatus("current")


class _Pm10010mptCfgClientStartupIndex_Type(Integer32):
    """Custom type pm10010mptCfgClientStartupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptCfgClientStartupIndex_Type.__name__ = "Integer32"
_Pm10010mptCfgClientStartupIndex_Object = MibTableColumn
pm10010mptCfgClientStartupIndex = _Pm10010mptCfgClientStartupIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 9, 2, 1, 1, 1),
    _Pm10010mptCfgClientStartupIndex_Type()
)
pm10010mptCfgClientStartupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCfgClientStartupIndex.setStatus("current")


class _Pm10010mptCfgSystConfPortPortn_Type(Unsigned32):
    """Custom type pm10010mptCfgSystConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mptCfgSystConfPortPortn_Type.__name__ = "Unsigned32"
_Pm10010mptCfgSystConfPortPortn_Object = MibTableColumn
pm10010mptCfgSystConfPortPortn = _Pm10010mptCfgSystConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 9, 2, 1, 1, 3),
    _Pm10010mptCfgSystConfPortPortn_Type()
)
pm10010mptCfgSystConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptCfgSystConfPortPortn.setStatus("current")


class _Pm10010mptCfgNetConfPortPortn_Type(Unsigned32):
    """Custom type pm10010mptCfgNetConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mptCfgNetConfPortPortn_Type.__name__ = "Unsigned32"
_Pm10010mptCfgNetConfPortPortn_Object = MibTableColumn
pm10010mptCfgNetConfPortPortn = _Pm10010mptCfgNetConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 9, 2, 1, 1, 4),
    _Pm10010mptCfgNetConfPortPortn_Type()
)
pm10010mptCfgNetConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptCfgNetConfPortPortn.setStatus("current")


class _Pm10010mptCfgIgnoreTimePortn_Type(Unsigned32):
    """Custom type pm10010mptCfgIgnoreTimePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mptCfgIgnoreTimePortn_Type.__name__ = "Unsigned32"
_Pm10010mptCfgIgnoreTimePortn_Object = MibTableColumn
pm10010mptCfgIgnoreTimePortn = _Pm10010mptCfgIgnoreTimePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 9, 2, 1, 1, 6),
    _Pm10010mptCfgIgnoreTimePortn_Type()
)
pm10010mptCfgIgnoreTimePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptCfgIgnoreTimePortn.setStatus("current")


class _Pm10010mptCfgOptionsPortPortn_Type(Unsigned32):
    """Custom type pm10010mptCfgOptionsPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mptCfgOptionsPortPortn_Type.__name__ = "Unsigned32"
_Pm10010mptCfgOptionsPortPortn_Object = MibTableColumn
pm10010mptCfgOptionsPortPortn = _Pm10010mptCfgOptionsPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 9, 2, 1, 1, 14),
    _Pm10010mptCfgOptionsPortPortn_Type()
)
pm10010mptCfgOptionsPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptCfgOptionsPortPortn.setStatus("current")
_Pm10010mptCfgLineStartupTable_Object = MibTable
pm10010mptCfgLineStartupTable = _Pm10010mptCfgLineStartupTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 9, 2, 2)
)
if mibBuilder.loadTexts:
    pm10010mptCfgLineStartupTable.setStatus("current")
_Pm10010mptCfgLineStartupEntry_Object = MibTableRow
pm10010mptCfgLineStartupEntry = _Pm10010mptCfgLineStartupEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 9, 2, 2, 1)
)
pm10010mptCfgLineStartupEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptCfgLineStartupIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptCfgLineStartupEntry.setStatus("current")


class _Pm10010mptCfgLineStartupIndex_Type(Integer32):
    """Custom type pm10010mptCfgLineStartupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptCfgLineStartupIndex_Type.__name__ = "Integer32"
_Pm10010mptCfgLineStartupIndex_Object = MibTableColumn
pm10010mptCfgLineStartupIndex = _Pm10010mptCfgLineStartupIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 9, 2, 2, 1, 1),
    _Pm10010mptCfgLineStartupIndex_Type()
)
pm10010mptCfgLineStartupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCfgLineStartupIndex.setStatus("current")


class _Pm10010mptCfgSystConfLinePortn_Type(Unsigned32):
    """Custom type pm10010mptCfgSystConfLinePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mptCfgSystConfLinePortn_Type.__name__ = "Unsigned32"
_Pm10010mptCfgSystConfLinePortn_Object = MibTableColumn
pm10010mptCfgSystConfLinePortn = _Pm10010mptCfgSystConfLinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 9, 2, 2, 1, 3),
    _Pm10010mptCfgSystConfLinePortn_Type()
)
pm10010mptCfgSystConfLinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptCfgSystConfLinePortn.setStatus("current")


class _Pm10010mptCfgOptionsLinePortn_Type(Unsigned32):
    """Custom type pm10010mptCfgOptionsLinePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mptCfgOptionsLinePortn_Type.__name__ = "Unsigned32"
_Pm10010mptCfgOptionsLinePortn_Object = MibTableColumn
pm10010mptCfgOptionsLinePortn = _Pm10010mptCfgOptionsLinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 9, 2, 2, 1, 14),
    _Pm10010mptCfgOptionsLinePortn_Type()
)
pm10010mptCfgOptionsLinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptCfgOptionsLinePortn.setStatus("current")
_Pm10010mptCfgXfpTable_Object = MibTable
pm10010mptCfgXfpTable = _Pm10010mptCfgXfpTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 9, 2, 3)
)
if mibBuilder.loadTexts:
    pm10010mptCfgXfpTable.setStatus("current")
_Pm10010mptCfgXfpEntry_Object = MibTableRow
pm10010mptCfgXfpEntry = _Pm10010mptCfgXfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 9, 2, 3, 1)
)
pm10010mptCfgXfpEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptCfgXfpIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptCfgXfpEntry.setStatus("current")


class _Pm10010mptCfgXfpIndex_Type(Integer32):
    """Custom type pm10010mptCfgXfpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptCfgXfpIndex_Type.__name__ = "Integer32"
_Pm10010mptCfgXfpIndex_Object = MibTableColumn
pm10010mptCfgXfpIndex = _Pm10010mptCfgXfpIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 9, 2, 3, 1, 1),
    _Pm10010mptCfgXfpIndex_Type()
)
pm10010mptCfgXfpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCfgXfpIndex.setStatus("current")


class _Pm10010mptCfgSystConfMsaLinePortn_Type(Unsigned32):
    """Custom type pm10010mptCfgSystConfMsaLinePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mptCfgSystConfMsaLinePortn_Type.__name__ = "Unsigned32"
_Pm10010mptCfgSystConfMsaLinePortn_Object = MibTableColumn
pm10010mptCfgSystConfMsaLinePortn = _Pm10010mptCfgSystConfMsaLinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 9, 2, 3, 1, 3),
    _Pm10010mptCfgSystConfMsaLinePortn_Type()
)
pm10010mptCfgSystConfMsaLinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptCfgSystConfMsaLinePortn.setStatus("current")
_Pm10010mptCfgLabels_ObjectIdentity = ObjectIdentity
pm10010mptCfgLabels = _Pm10010mptCfgLabels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 9, 3)
)
_Pm10010mptCfgLabelclientTable_Object = MibTable
pm10010mptCfgLabelclientTable = _Pm10010mptCfgLabelclientTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 9, 3, 1)
)
if mibBuilder.loadTexts:
    pm10010mptCfgLabelclientTable.setStatus("current")
_Pm10010mptCfgLabelclientEntry_Object = MibTableRow
pm10010mptCfgLabelclientEntry = _Pm10010mptCfgLabelclientEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 9, 3, 1, 1)
)
pm10010mptCfgLabelclientEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptCfgLabelclientIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptCfgLabelclientEntry.setStatus("current")


class _Pm10010mptCfgLabelclientIndex_Type(Integer32):
    """Custom type pm10010mptCfgLabelclientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptCfgLabelclientIndex_Type.__name__ = "Integer32"
_Pm10010mptCfgLabelclientIndex_Object = MibTableColumn
pm10010mptCfgLabelclientIndex = _Pm10010mptCfgLabelclientIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 9, 3, 1, 1, 1),
    _Pm10010mptCfgLabelclientIndex_Type()
)
pm10010mptCfgLabelclientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCfgLabelclientIndex.setStatus("current")


class _Pm10010mptCfgLabelclientPortn_Type(DisplayString):
    """Custom type pm10010mptCfgLabelclientPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pm10010mptCfgLabelclientPortn_Type.__name__ = "DisplayString"
_Pm10010mptCfgLabelclientPortn_Object = MibTableColumn
pm10010mptCfgLabelclientPortn = _Pm10010mptCfgLabelclientPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 9, 3, 1, 1, 3),
    _Pm10010mptCfgLabelclientPortn_Type()
)
pm10010mptCfgLabelclientPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptCfgLabelclientPortn.setStatus("current")
_Pm10010mptCfgLabellineTable_Object = MibTable
pm10010mptCfgLabellineTable = _Pm10010mptCfgLabellineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 9, 3, 2)
)
if mibBuilder.loadTexts:
    pm10010mptCfgLabellineTable.setStatus("current")
_Pm10010mptCfgLabellineEntry_Object = MibTableRow
pm10010mptCfgLabellineEntry = _Pm10010mptCfgLabellineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 9, 3, 2, 1)
)
pm10010mptCfgLabellineEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptCfgLabellineIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptCfgLabellineEntry.setStatus("current")


class _Pm10010mptCfgLabellineIndex_Type(Integer32):
    """Custom type pm10010mptCfgLabellineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptCfgLabellineIndex_Type.__name__ = "Integer32"
_Pm10010mptCfgLabellineIndex_Object = MibTableColumn
pm10010mptCfgLabellineIndex = _Pm10010mptCfgLabellineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 9, 3, 2, 1, 1),
    _Pm10010mptCfgLabellineIndex_Type()
)
pm10010mptCfgLabellineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCfgLabellineIndex.setStatus("current")


class _Pm10010mptCfgLabellinePortn_Type(DisplayString):
    """Custom type pm10010mptCfgLabellinePortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pm10010mptCfgLabellinePortn_Type.__name__ = "DisplayString"
_Pm10010mptCfgLabellinePortn_Object = MibTableColumn
pm10010mptCfgLabellinePortn = _Pm10010mptCfgLabellinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 9, 3, 2, 1, 3),
    _Pm10010mptCfgLabellinePortn_Type()
)
pm10010mptCfgLabellinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptCfgLabellinePortn.setStatus("current")
_Pm10010mptCfgStartuptlh_ObjectIdentity = ObjectIdentity
pm10010mptCfgStartuptlh = _Pm10010mptCfgStartuptlh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 9, 4)
)
_Pm10010mptCfgOtxtlhTable_Object = MibTable
pm10010mptCfgOtxtlhTable = _Pm10010mptCfgOtxtlhTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 9, 4, 1)
)
if mibBuilder.loadTexts:
    pm10010mptCfgOtxtlhTable.setStatus("current")
_Pm10010mptCfgOtxtlhEntry_Object = MibTableRow
pm10010mptCfgOtxtlhEntry = _Pm10010mptCfgOtxtlhEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 9, 4, 1, 1)
)
pm10010mptCfgOtxtlhEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptCfgOtxtlhIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptCfgOtxtlhEntry.setStatus("current")


class _Pm10010mptCfgOtxtlhIndex_Type(Integer32):
    """Custom type pm10010mptCfgOtxtlhIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptCfgOtxtlhIndex_Type.__name__ = "Integer32"
_Pm10010mptCfgOtxtlhIndex_Object = MibTableColumn
pm10010mptCfgOtxtlhIndex = _Pm10010mptCfgOtxtlhIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 9, 4, 1, 1, 1),
    _Pm10010mptCfgOtxtlhIndex_Type()
)
pm10010mptCfgOtxtlhIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCfgOtxtlhIndex.setStatus("current")


class _Pm10010mptCfgLinePwrLaserPortn_Type(Unsigned32):
    """Custom type pm10010mptCfgLinePwrLaserPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mptCfgLinePwrLaserPortn_Type.__name__ = "Unsigned32"
_Pm10010mptCfgLinePwrLaserPortn_Object = MibTableColumn
pm10010mptCfgLinePwrLaserPortn = _Pm10010mptCfgLinePwrLaserPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 9, 4, 1, 1, 6),
    _Pm10010mptCfgLinePwrLaserPortn_Type()
)
pm10010mptCfgLinePwrLaserPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptCfgLinePwrLaserPortn.setStatus("current")


class _Pm10010mptCfgLineFCurrentPortn_Type(Unsigned32):
    """Custom type pm10010mptCfgLineFCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mptCfgLineFCurrentPortn_Type.__name__ = "Unsigned32"
_Pm10010mptCfgLineFCurrentPortn_Object = MibTableColumn
pm10010mptCfgLineFCurrentPortn = _Pm10010mptCfgLineFCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 9, 4, 1, 1, 7),
    _Pm10010mptCfgLineFCurrentPortn_Type()
)
pm10010mptCfgLineFCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptCfgLineFCurrentPortn.setStatus("current")


class _Pm10010mptCfgLineGridCurrentPortn_Type(Unsigned32):
    """Custom type pm10010mptCfgLineGridCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mptCfgLineGridCurrentPortn_Type.__name__ = "Unsigned32"
_Pm10010mptCfgLineGridCurrentPortn_Object = MibTableColumn
pm10010mptCfgLineGridCurrentPortn = _Pm10010mptCfgLineGridCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 9, 4, 1, 1, 8),
    _Pm10010mptCfgLineGridCurrentPortn_Type()
)
pm10010mptCfgLineGridCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptCfgLineGridCurrentPortn.setStatus("current")


class _Pm10010mptCfgFPortn_Type(Unsigned32):
    """Custom type pm10010mptCfgFPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mptCfgFPortn_Type.__name__ = "Unsigned32"
_Pm10010mptCfgFPortn_Object = MibTableColumn
pm10010mptCfgFPortn = _Pm10010mptCfgFPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 9, 4, 1, 1, 9),
    _Pm10010mptCfgFPortn_Type()
)
pm10010mptCfgFPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptCfgFPortn.setStatus("current")


class _Pm10010mptCfgRxLineFCurrentPortn_Type(Unsigned32):
    """Custom type pm10010mptCfgRxLineFCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mptCfgRxLineFCurrentPortn_Type.__name__ = "Unsigned32"
_Pm10010mptCfgRxLineFCurrentPortn_Object = MibTableColumn
pm10010mptCfgRxLineFCurrentPortn = _Pm10010mptCfgRxLineFCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 9, 4, 1, 1, 10),
    _Pm10010mptCfgRxLineFCurrentPortn_Type()
)
pm10010mptCfgRxLineFCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptCfgRxLineFCurrentPortn.setStatus("current")
_Pm10010mptCfgOther_ObjectIdentity = ObjectIdentity
pm10010mptCfgOther = _Pm10010mptCfgOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 9, 5)
)
_Pm10010mpttablemoduleOther_ObjectIdentity = ObjectIdentity
pm10010mpttablemoduleOther = _Pm10010mpttablemoduleOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 9, 5, 1)
)


class _Pm10010mptCfgmode_Type(Unsigned32):
    """Custom type pm10010mptCfgmode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mptCfgmode_Type.__name__ = "Unsigned32"
_Pm10010mptCfgmode_Object = MibScalar
pm10010mptCfgmode = _Pm10010mptCfgmode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 9, 5, 1, 2),
    _Pm10010mptCfgmode_Type()
)
pm10010mptCfgmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptCfgmode.setStatus("current")


class _Pm10010mptCfgfanLowSpeedThreshold_Type(Unsigned32):
    """Custom type pm10010mptCfgfanLowSpeedThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mptCfgfanLowSpeedThreshold_Type.__name__ = "Unsigned32"
_Pm10010mptCfgfanLowSpeedThreshold_Object = MibScalar
pm10010mptCfgfanLowSpeedThreshold = _Pm10010mptCfgfanLowSpeedThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 9, 5, 1, 3),
    _Pm10010mptCfgfanLowSpeedThreshold_Type()
)
pm10010mptCfgfanLowSpeedThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptCfgfanLowSpeedThreshold.setStatus("current")


class _Pm10010mptCfgfanHighSpeedThreshold_Type(Unsigned32):
    """Custom type pm10010mptCfgfanHighSpeedThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mptCfgfanHighSpeedThreshold_Type.__name__ = "Unsigned32"
_Pm10010mptCfgfanHighSpeedThreshold_Object = MibScalar
pm10010mptCfgfanHighSpeedThreshold = _Pm10010mptCfgfanHighSpeedThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 9, 5, 1, 4),
    _Pm10010mptCfgfanHighSpeedThreshold_Type()
)
pm10010mptCfgfanHighSpeedThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptCfgfanHighSpeedThreshold.setStatus("current")
_Pm10010mptCfgStartuptablefive_ObjectIdentity = ObjectIdentity
pm10010mptCfgStartuptablefive = _Pm10010mptCfgStartuptablefive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 9, 6)
)
_Pm10010mptCfgOtxtlhcapabilitiesTable_Object = MibTable
pm10010mptCfgOtxtlhcapabilitiesTable = _Pm10010mptCfgOtxtlhcapabilitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 9, 6, 1)
)
if mibBuilder.loadTexts:
    pm10010mptCfgOtxtlhcapabilitiesTable.setStatus("current")
_Pm10010mptCfgOtxtlhcapabilitiesEntry_Object = MibTableRow
pm10010mptCfgOtxtlhcapabilitiesEntry = _Pm10010mptCfgOtxtlhcapabilitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 9, 6, 1, 1)
)
pm10010mptCfgOtxtlhcapabilitiesEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptCfgOtxtlhcapabilitiesIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptCfgOtxtlhcapabilitiesEntry.setStatus("current")


class _Pm10010mptCfgOtxtlhcapabilitiesIndex_Type(Integer32):
    """Custom type pm10010mptCfgOtxtlhcapabilitiesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptCfgOtxtlhcapabilitiesIndex_Type.__name__ = "Integer32"
_Pm10010mptCfgOtxtlhcapabilitiesIndex_Object = MibTableColumn
pm10010mptCfgOtxtlhcapabilitiesIndex = _Pm10010mptCfgOtxtlhcapabilitiesIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 9, 6, 1, 1, 1),
    _Pm10010mptCfgOtxtlhcapabilitiesIndex_Type()
)
pm10010mptCfgOtxtlhcapabilitiesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCfgOtxtlhcapabilitiesIndex.setStatus("current")


class _Pm10010mptCfgComponentTypePortn_Type(Unsigned32):
    """Custom type pm10010mptCfgComponentTypePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mptCfgComponentTypePortn_Type.__name__ = "Unsigned32"
_Pm10010mptCfgComponentTypePortn_Object = MibTableColumn
pm10010mptCfgComponentTypePortn = _Pm10010mptCfgComponentTypePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 9, 6, 1, 1, 3),
    _Pm10010mptCfgComponentTypePortn_Type()
)
pm10010mptCfgComponentTypePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCfgComponentTypePortn.setStatus("current")


class _Pm10010mptCfgMiscellaneousPortn_Type(Unsigned32):
    """Custom type pm10010mptCfgMiscellaneousPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mptCfgMiscellaneousPortn_Type.__name__ = "Unsigned32"
_Pm10010mptCfgMiscellaneousPortn_Object = MibTableColumn
pm10010mptCfgMiscellaneousPortn = _Pm10010mptCfgMiscellaneousPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 9, 6, 1, 1, 4),
    _Pm10010mptCfgMiscellaneousPortn_Type()
)
pm10010mptCfgMiscellaneousPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCfgMiscellaneousPortn.setStatus("current")


class _Pm10010mptCfgFirstChannelPortn_Type(Unsigned32):
    """Custom type pm10010mptCfgFirstChannelPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mptCfgFirstChannelPortn_Type.__name__ = "Unsigned32"
_Pm10010mptCfgFirstChannelPortn_Object = MibTableColumn
pm10010mptCfgFirstChannelPortn = _Pm10010mptCfgFirstChannelPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 9, 6, 1, 1, 5),
    _Pm10010mptCfgFirstChannelPortn_Type()
)
pm10010mptCfgFirstChannelPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCfgFirstChannelPortn.setStatus("current")


class _Pm10010mptCfgLastChannelPortn_Type(Unsigned32):
    """Custom type pm10010mptCfgLastChannelPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mptCfgLastChannelPortn_Type.__name__ = "Unsigned32"
_Pm10010mptCfgLastChannelPortn_Object = MibTableColumn
pm10010mptCfgLastChannelPortn = _Pm10010mptCfgLastChannelPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 9, 6, 1, 1, 6),
    _Pm10010mptCfgLastChannelPortn_Type()
)
pm10010mptCfgLastChannelPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCfgLastChannelPortn.setStatus("current")


class _Pm10010mptCfgGridPortn_Type(Unsigned32):
    """Custom type pm10010mptCfgGridPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mptCfgGridPortn_Type.__name__ = "Unsigned32"
_Pm10010mptCfgGridPortn_Object = MibTableColumn
pm10010mptCfgGridPortn = _Pm10010mptCfgGridPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 9, 6, 1, 1, 7),
    _Pm10010mptCfgGridPortn_Type()
)
pm10010mptCfgGridPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptCfgGridPortn.setStatus("current")
_Pm10010mptCfgWriteConfiguration_Type = EkiOnOff
_Pm10010mptCfgWriteConfiguration_Object = MibScalar
pm10010mptCfgWriteConfiguration = _Pm10010mptCfgWriteConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 9, 257),
    _Pm10010mptCfgWriteConfiguration_Type()
)
pm10010mptCfgWriteConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptCfgWriteConfiguration.setStatus("current")
_Pm10010mpttraps_ObjectIdentity = ObjectIdentity
pm10010mpttraps = _Pm10010mpttraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 10)
)


class _Pm10010mpttrapPortNumber_Type(Integer32):
    """Custom type pm10010mpttrapPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm10010mpttrapPortNumber_Type.__name__ = "Integer32"
_Pm10010mpttrapPortNumber_Object = MibScalar
pm10010mpttrapPortNumber = _Pm10010mpttrapPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 10, 2),
    _Pm10010mpttrapPortNumber_Type()
)
pm10010mpttrapPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpttrapPortNumber.setStatus("current")


class _Pm10010mpttrapLineNumber_Type(Integer32):
    """Custom type pm10010mpttrapLineNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm10010mpttrapLineNumber_Type.__name__ = "Integer32"
_Pm10010mpttrapLineNumber_Object = MibScalar
pm10010mpttrapLineNumber = _Pm10010mpttrapLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 10, 3),
    _Pm10010mpttrapLineNumber_Type()
)
pm10010mpttrapLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpttrapLineNumber.setStatus("current")


class _Pm10010mpttrapBoardNumber_Type(Integer32):
    """Custom type pm10010mpttrapBoardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm10010mpttrapBoardNumber_Type.__name__ = "Integer32"
_Pm10010mpttrapBoardNumber_Object = MibScalar
pm10010mpttrapBoardNumber = _Pm10010mpttrapBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 10, 4),
    _Pm10010mpttrapBoardNumber_Type()
)
pm10010mpttrapBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpttrapBoardNumber.setStatus("current")
_Pm10010mptMonitoring_ObjectIdentity = ObjectIdentity
pm10010mptMonitoring = _Pm10010mptMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11)
)
_Pm10010mptMonOther_ObjectIdentity = ObjectIdentity
pm10010mptMonOther = _Pm10010mptMonOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 1)
)
_Pm10010mptMonRmon_ObjectIdentity = ObjectIdentity
pm10010mptMonRmon = _Pm10010mptMonRmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 1, 3)
)
_Pm10010mptMonClient_ObjectIdentity = ObjectIdentity
pm10010mptMonClient = _Pm10010mptMonClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2)
)
_Pm10010mptMonClientRmonCounter_ObjectIdentity = ObjectIdentity
pm10010mptMonClientRmonCounter = _Pm10010mptMonClientRmonCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4)
)
_Pm10010mptMonupRmonBytesCounterClientInputTable_Object = MibTable
pm10010mptMonupRmonBytesCounterClientInputTable = _Pm10010mptMonupRmonBytesCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 16)
)
if mibBuilder.loadTexts:
    pm10010mptMonupRmonBytesCounterClientInputTable.setStatus("current")
_Pm10010mptMonupRmonBytesCounterClientInputEntry_Object = MibTableRow
pm10010mptMonupRmonBytesCounterClientInputEntry = _Pm10010mptMonupRmonBytesCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 16, 1)
)
pm10010mptMonupRmonBytesCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptMonupRmonBytesCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptMonupRmonBytesCounterClientInputEntry.setStatus("current")


class _Pm10010mptMonupRmonBytesCounterClientInputIndex_Type(Integer32):
    """Custom type pm10010mptMonupRmonBytesCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptMonupRmonBytesCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm10010mptMonupRmonBytesCounterClientInputIndex_Object = MibTableColumn
pm10010mptMonupRmonBytesCounterClientInputIndex = _Pm10010mptMonupRmonBytesCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 16, 1, 1),
    _Pm10010mptMonupRmonBytesCounterClientInputIndex_Type()
)
pm10010mptMonupRmonBytesCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMonupRmonBytesCounterClientInputIndex.setStatus("current")
_Pm10010mptMonupRmonBytesCounterClientInputValuePortn_Type = Counter64
_Pm10010mptMonupRmonBytesCounterClientInputValuePortn_Object = MibTableColumn
pm10010mptMonupRmonBytesCounterClientInputValuePortn = _Pm10010mptMonupRmonBytesCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 16, 1, 2),
    _Pm10010mptMonupRmonBytesCounterClientInputValuePortn_Type()
)
pm10010mptMonupRmonBytesCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMonupRmonBytesCounterClientInputValuePortn.setStatus("current")
_Pm10010mptMonupRmonBytesCounterClientInputErrorPortn_Type = EkiOnOff
_Pm10010mptMonupRmonBytesCounterClientInputErrorPortn_Object = MibTableColumn
pm10010mptMonupRmonBytesCounterClientInputErrorPortn = _Pm10010mptMonupRmonBytesCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 16, 1, 3),
    _Pm10010mptMonupRmonBytesCounterClientInputErrorPortn_Type()
)
pm10010mptMonupRmonBytesCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMonupRmonBytesCounterClientInputErrorPortn.setStatus("current")
_Pm10010mptMonupRmonBytesCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm10010mptMonupRmonBytesCounterClientInputOverloadPortn_Object = MibTableColumn
pm10010mptMonupRmonBytesCounterClientInputOverloadPortn = _Pm10010mptMonupRmonBytesCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 16, 1, 4),
    _Pm10010mptMonupRmonBytesCounterClientInputOverloadPortn_Type()
)
pm10010mptMonupRmonBytesCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMonupRmonBytesCounterClientInputOverloadPortn.setStatus("current")
_Pm10010mptMonupRmonCrcErrorsCounterClientInputTable_Object = MibTable
pm10010mptMonupRmonCrcErrorsCounterClientInputTable = _Pm10010mptMonupRmonCrcErrorsCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 32)
)
if mibBuilder.loadTexts:
    pm10010mptMonupRmonCrcErrorsCounterClientInputTable.setStatus("current")
_Pm10010mptMonupRmonCrcErrorsCounterClientInputEntry_Object = MibTableRow
pm10010mptMonupRmonCrcErrorsCounterClientInputEntry = _Pm10010mptMonupRmonCrcErrorsCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 32, 1)
)
pm10010mptMonupRmonCrcErrorsCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptMonupRmonCrcErrorsCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptMonupRmonCrcErrorsCounterClientInputEntry.setStatus("current")


class _Pm10010mptMonupRmonCrcErrorsCounterClientInputIndex_Type(Integer32):
    """Custom type pm10010mptMonupRmonCrcErrorsCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptMonupRmonCrcErrorsCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm10010mptMonupRmonCrcErrorsCounterClientInputIndex_Object = MibTableColumn
pm10010mptMonupRmonCrcErrorsCounterClientInputIndex = _Pm10010mptMonupRmonCrcErrorsCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 32, 1, 1),
    _Pm10010mptMonupRmonCrcErrorsCounterClientInputIndex_Type()
)
pm10010mptMonupRmonCrcErrorsCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMonupRmonCrcErrorsCounterClientInputIndex.setStatus("current")
_Pm10010mptMonupRmonCrcErrorsCounterClientInputValuePortn_Type = Counter64
_Pm10010mptMonupRmonCrcErrorsCounterClientInputValuePortn_Object = MibTableColumn
pm10010mptMonupRmonCrcErrorsCounterClientInputValuePortn = _Pm10010mptMonupRmonCrcErrorsCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 32, 1, 2),
    _Pm10010mptMonupRmonCrcErrorsCounterClientInputValuePortn_Type()
)
pm10010mptMonupRmonCrcErrorsCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMonupRmonCrcErrorsCounterClientInputValuePortn.setStatus("current")
_Pm10010mptMonupRmonCrcErrorsCounterClientInputErrorPortn_Type = EkiOnOff
_Pm10010mptMonupRmonCrcErrorsCounterClientInputErrorPortn_Object = MibTableColumn
pm10010mptMonupRmonCrcErrorsCounterClientInputErrorPortn = _Pm10010mptMonupRmonCrcErrorsCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 32, 1, 3),
    _Pm10010mptMonupRmonCrcErrorsCounterClientInputErrorPortn_Type()
)
pm10010mptMonupRmonCrcErrorsCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMonupRmonCrcErrorsCounterClientInputErrorPortn.setStatus("current")
_Pm10010mptMonupRmonCrcErrorsCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm10010mptMonupRmonCrcErrorsCounterClientInputOverloadPortn_Object = MibTableColumn
pm10010mptMonupRmonCrcErrorsCounterClientInputOverloadPortn = _Pm10010mptMonupRmonCrcErrorsCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 32, 1, 4),
    _Pm10010mptMonupRmonCrcErrorsCounterClientInputOverloadPortn_Type()
)
pm10010mptMonupRmonCrcErrorsCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMonupRmonCrcErrorsCounterClientInputOverloadPortn.setStatus("current")
_Pm10010mptMonupRmonPacketsCounterClientInputTable_Object = MibTable
pm10010mptMonupRmonPacketsCounterClientInputTable = _Pm10010mptMonupRmonPacketsCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 48)
)
if mibBuilder.loadTexts:
    pm10010mptMonupRmonPacketsCounterClientInputTable.setStatus("current")
_Pm10010mptMonupRmonPacketsCounterClientInputEntry_Object = MibTableRow
pm10010mptMonupRmonPacketsCounterClientInputEntry = _Pm10010mptMonupRmonPacketsCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 48, 1)
)
pm10010mptMonupRmonPacketsCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptMonupRmonPacketsCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptMonupRmonPacketsCounterClientInputEntry.setStatus("current")


class _Pm10010mptMonupRmonPacketsCounterClientInputIndex_Type(Integer32):
    """Custom type pm10010mptMonupRmonPacketsCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptMonupRmonPacketsCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm10010mptMonupRmonPacketsCounterClientInputIndex_Object = MibTableColumn
pm10010mptMonupRmonPacketsCounterClientInputIndex = _Pm10010mptMonupRmonPacketsCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 48, 1, 1),
    _Pm10010mptMonupRmonPacketsCounterClientInputIndex_Type()
)
pm10010mptMonupRmonPacketsCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMonupRmonPacketsCounterClientInputIndex.setStatus("current")
_Pm10010mptMonupRmonPacketsCounterClientInputValuePortn_Type = Counter64
_Pm10010mptMonupRmonPacketsCounterClientInputValuePortn_Object = MibTableColumn
pm10010mptMonupRmonPacketsCounterClientInputValuePortn = _Pm10010mptMonupRmonPacketsCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 48, 1, 2),
    _Pm10010mptMonupRmonPacketsCounterClientInputValuePortn_Type()
)
pm10010mptMonupRmonPacketsCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMonupRmonPacketsCounterClientInputValuePortn.setStatus("current")
_Pm10010mptMonupRmonPacketsCounterClientInputErrorPortn_Type = EkiOnOff
_Pm10010mptMonupRmonPacketsCounterClientInputErrorPortn_Object = MibTableColumn
pm10010mptMonupRmonPacketsCounterClientInputErrorPortn = _Pm10010mptMonupRmonPacketsCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 48, 1, 3),
    _Pm10010mptMonupRmonPacketsCounterClientInputErrorPortn_Type()
)
pm10010mptMonupRmonPacketsCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMonupRmonPacketsCounterClientInputErrorPortn.setStatus("current")
_Pm10010mptMonupRmonPacketsCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm10010mptMonupRmonPacketsCounterClientInputOverloadPortn_Object = MibTableColumn
pm10010mptMonupRmonPacketsCounterClientInputOverloadPortn = _Pm10010mptMonupRmonPacketsCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 48, 1, 4),
    _Pm10010mptMonupRmonPacketsCounterClientInputOverloadPortn_Type()
)
pm10010mptMonupRmonPacketsCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMonupRmonPacketsCounterClientInputOverloadPortn.setStatus("current")
_Pm10010mptMonupRmonBroadcastCounterClientInputTable_Object = MibTable
pm10010mptMonupRmonBroadcastCounterClientInputTable = _Pm10010mptMonupRmonBroadcastCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 64)
)
if mibBuilder.loadTexts:
    pm10010mptMonupRmonBroadcastCounterClientInputTable.setStatus("current")
_Pm10010mptMonupRmonBroadcastCounterClientInputEntry_Object = MibTableRow
pm10010mptMonupRmonBroadcastCounterClientInputEntry = _Pm10010mptMonupRmonBroadcastCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 64, 1)
)
pm10010mptMonupRmonBroadcastCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptMonupRmonBroadcastCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptMonupRmonBroadcastCounterClientInputEntry.setStatus("current")


class _Pm10010mptMonupRmonBroadcastCounterClientInputIndex_Type(Integer32):
    """Custom type pm10010mptMonupRmonBroadcastCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptMonupRmonBroadcastCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm10010mptMonupRmonBroadcastCounterClientInputIndex_Object = MibTableColumn
pm10010mptMonupRmonBroadcastCounterClientInputIndex = _Pm10010mptMonupRmonBroadcastCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 64, 1, 1),
    _Pm10010mptMonupRmonBroadcastCounterClientInputIndex_Type()
)
pm10010mptMonupRmonBroadcastCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMonupRmonBroadcastCounterClientInputIndex.setStatus("current")
_Pm10010mptMonupRmonBroadcastCounterClientInputValuePortn_Type = Counter64
_Pm10010mptMonupRmonBroadcastCounterClientInputValuePortn_Object = MibTableColumn
pm10010mptMonupRmonBroadcastCounterClientInputValuePortn = _Pm10010mptMonupRmonBroadcastCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 64, 1, 2),
    _Pm10010mptMonupRmonBroadcastCounterClientInputValuePortn_Type()
)
pm10010mptMonupRmonBroadcastCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMonupRmonBroadcastCounterClientInputValuePortn.setStatus("current")
_Pm10010mptMonupRmonBroadcastCounterClientInputErrorPortn_Type = EkiOnOff
_Pm10010mptMonupRmonBroadcastCounterClientInputErrorPortn_Object = MibTableColumn
pm10010mptMonupRmonBroadcastCounterClientInputErrorPortn = _Pm10010mptMonupRmonBroadcastCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 64, 1, 3),
    _Pm10010mptMonupRmonBroadcastCounterClientInputErrorPortn_Type()
)
pm10010mptMonupRmonBroadcastCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMonupRmonBroadcastCounterClientInputErrorPortn.setStatus("current")
_Pm10010mptMonupRmonBroadcastCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm10010mptMonupRmonBroadcastCounterClientInputOverloadPortn_Object = MibTableColumn
pm10010mptMonupRmonBroadcastCounterClientInputOverloadPortn = _Pm10010mptMonupRmonBroadcastCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 64, 1, 4),
    _Pm10010mptMonupRmonBroadcastCounterClientInputOverloadPortn_Type()
)
pm10010mptMonupRmonBroadcastCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMonupRmonBroadcastCounterClientInputOverloadPortn.setStatus("current")
_Pm10010mptMonupRmonMulticastCounterClientInputTable_Object = MibTable
pm10010mptMonupRmonMulticastCounterClientInputTable = _Pm10010mptMonupRmonMulticastCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 80)
)
if mibBuilder.loadTexts:
    pm10010mptMonupRmonMulticastCounterClientInputTable.setStatus("current")
_Pm10010mptMonupRmonMulticastCounterClientInputEntry_Object = MibTableRow
pm10010mptMonupRmonMulticastCounterClientInputEntry = _Pm10010mptMonupRmonMulticastCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 80, 1)
)
pm10010mptMonupRmonMulticastCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptMonupRmonMulticastCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptMonupRmonMulticastCounterClientInputEntry.setStatus("current")


class _Pm10010mptMonupRmonMulticastCounterClientInputIndex_Type(Integer32):
    """Custom type pm10010mptMonupRmonMulticastCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptMonupRmonMulticastCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm10010mptMonupRmonMulticastCounterClientInputIndex_Object = MibTableColumn
pm10010mptMonupRmonMulticastCounterClientInputIndex = _Pm10010mptMonupRmonMulticastCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 80, 1, 1),
    _Pm10010mptMonupRmonMulticastCounterClientInputIndex_Type()
)
pm10010mptMonupRmonMulticastCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMonupRmonMulticastCounterClientInputIndex.setStatus("current")
_Pm10010mptMonupRmonMulticastCounterClientInputValuePortn_Type = Counter64
_Pm10010mptMonupRmonMulticastCounterClientInputValuePortn_Object = MibTableColumn
pm10010mptMonupRmonMulticastCounterClientInputValuePortn = _Pm10010mptMonupRmonMulticastCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 80, 1, 2),
    _Pm10010mptMonupRmonMulticastCounterClientInputValuePortn_Type()
)
pm10010mptMonupRmonMulticastCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMonupRmonMulticastCounterClientInputValuePortn.setStatus("current")
_Pm10010mptMonupRmonMulticastCounterClientInputErrorPortn_Type = EkiOnOff
_Pm10010mptMonupRmonMulticastCounterClientInputErrorPortn_Object = MibTableColumn
pm10010mptMonupRmonMulticastCounterClientInputErrorPortn = _Pm10010mptMonupRmonMulticastCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 80, 1, 3),
    _Pm10010mptMonupRmonMulticastCounterClientInputErrorPortn_Type()
)
pm10010mptMonupRmonMulticastCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMonupRmonMulticastCounterClientInputErrorPortn.setStatus("current")
_Pm10010mptMonupRmonMulticastCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm10010mptMonupRmonMulticastCounterClientInputOverloadPortn_Object = MibTableColumn
pm10010mptMonupRmonMulticastCounterClientInputOverloadPortn = _Pm10010mptMonupRmonMulticastCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 80, 1, 4),
    _Pm10010mptMonupRmonMulticastCounterClientInputOverloadPortn_Type()
)
pm10010mptMonupRmonMulticastCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMonupRmonMulticastCounterClientInputOverloadPortn.setStatus("current")
_Pm10010mptMonupRmonPauseFrameCounterClientInputTable_Object = MibTable
pm10010mptMonupRmonPauseFrameCounterClientInputTable = _Pm10010mptMonupRmonPauseFrameCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 96)
)
if mibBuilder.loadTexts:
    pm10010mptMonupRmonPauseFrameCounterClientInputTable.setStatus("current")
_Pm10010mptMonupRmonPauseFrameCounterClientInputEntry_Object = MibTableRow
pm10010mptMonupRmonPauseFrameCounterClientInputEntry = _Pm10010mptMonupRmonPauseFrameCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 96, 1)
)
pm10010mptMonupRmonPauseFrameCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptMonupRmonPauseFrameCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptMonupRmonPauseFrameCounterClientInputEntry.setStatus("current")


class _Pm10010mptMonupRmonPauseFrameCounterClientInputIndex_Type(Integer32):
    """Custom type pm10010mptMonupRmonPauseFrameCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptMonupRmonPauseFrameCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm10010mptMonupRmonPauseFrameCounterClientInputIndex_Object = MibTableColumn
pm10010mptMonupRmonPauseFrameCounterClientInputIndex = _Pm10010mptMonupRmonPauseFrameCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 96, 1, 1),
    _Pm10010mptMonupRmonPauseFrameCounterClientInputIndex_Type()
)
pm10010mptMonupRmonPauseFrameCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMonupRmonPauseFrameCounterClientInputIndex.setStatus("current")
_Pm10010mptMonupRmonPauseFrameCounterClientInputValuePortn_Type = Counter64
_Pm10010mptMonupRmonPauseFrameCounterClientInputValuePortn_Object = MibTableColumn
pm10010mptMonupRmonPauseFrameCounterClientInputValuePortn = _Pm10010mptMonupRmonPauseFrameCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 96, 1, 2),
    _Pm10010mptMonupRmonPauseFrameCounterClientInputValuePortn_Type()
)
pm10010mptMonupRmonPauseFrameCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMonupRmonPauseFrameCounterClientInputValuePortn.setStatus("current")
_Pm10010mptMonupRmonPauseFrameCounterClientInputErrorPortn_Type = EkiOnOff
_Pm10010mptMonupRmonPauseFrameCounterClientInputErrorPortn_Object = MibTableColumn
pm10010mptMonupRmonPauseFrameCounterClientInputErrorPortn = _Pm10010mptMonupRmonPauseFrameCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 96, 1, 3),
    _Pm10010mptMonupRmonPauseFrameCounterClientInputErrorPortn_Type()
)
pm10010mptMonupRmonPauseFrameCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMonupRmonPauseFrameCounterClientInputErrorPortn.setStatus("current")
_Pm10010mptMonupRmonPauseFrameCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm10010mptMonupRmonPauseFrameCounterClientInputOverloadPortn_Object = MibTableColumn
pm10010mptMonupRmonPauseFrameCounterClientInputOverloadPortn = _Pm10010mptMonupRmonPauseFrameCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 96, 1, 4),
    _Pm10010mptMonupRmonPauseFrameCounterClientInputOverloadPortn_Type()
)
pm10010mptMonupRmonPauseFrameCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMonupRmonPauseFrameCounterClientInputOverloadPortn.setStatus("current")
_Pm10010mptMonupRmonUnicastCounterClientInputTable_Object = MibTable
pm10010mptMonupRmonUnicastCounterClientInputTable = _Pm10010mptMonupRmonUnicastCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 160)
)
if mibBuilder.loadTexts:
    pm10010mptMonupRmonUnicastCounterClientInputTable.setStatus("current")
_Pm10010mptMonupRmonUnicastCounterClientInputEntry_Object = MibTableRow
pm10010mptMonupRmonUnicastCounterClientInputEntry = _Pm10010mptMonupRmonUnicastCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 160, 1)
)
pm10010mptMonupRmonUnicastCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptMonupRmonUnicastCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptMonupRmonUnicastCounterClientInputEntry.setStatus("current")


class _Pm10010mptMonupRmonUnicastCounterClientInputIndex_Type(Integer32):
    """Custom type pm10010mptMonupRmonUnicastCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptMonupRmonUnicastCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm10010mptMonupRmonUnicastCounterClientInputIndex_Object = MibTableColumn
pm10010mptMonupRmonUnicastCounterClientInputIndex = _Pm10010mptMonupRmonUnicastCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 160, 1, 1),
    _Pm10010mptMonupRmonUnicastCounterClientInputIndex_Type()
)
pm10010mptMonupRmonUnicastCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMonupRmonUnicastCounterClientInputIndex.setStatus("current")
_Pm10010mptMonupRmonUnicastCounterClientInputValuePortn_Type = Counter64
_Pm10010mptMonupRmonUnicastCounterClientInputValuePortn_Object = MibTableColumn
pm10010mptMonupRmonUnicastCounterClientInputValuePortn = _Pm10010mptMonupRmonUnicastCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 160, 1, 2),
    _Pm10010mptMonupRmonUnicastCounterClientInputValuePortn_Type()
)
pm10010mptMonupRmonUnicastCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMonupRmonUnicastCounterClientInputValuePortn.setStatus("current")
_Pm10010mptMonupRmonUnicastCounterClientInputErrorPortn_Type = EkiOnOff
_Pm10010mptMonupRmonUnicastCounterClientInputErrorPortn_Object = MibTableColumn
pm10010mptMonupRmonUnicastCounterClientInputErrorPortn = _Pm10010mptMonupRmonUnicastCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 160, 1, 3),
    _Pm10010mptMonupRmonUnicastCounterClientInputErrorPortn_Type()
)
pm10010mptMonupRmonUnicastCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMonupRmonUnicastCounterClientInputErrorPortn.setStatus("current")
_Pm10010mptMonupRmonUnicastCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm10010mptMonupRmonUnicastCounterClientInputOverloadPortn_Object = MibTableColumn
pm10010mptMonupRmonUnicastCounterClientInputOverloadPortn = _Pm10010mptMonupRmonUnicastCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 160, 1, 4),
    _Pm10010mptMonupRmonUnicastCounterClientInputOverloadPortn_Type()
)
pm10010mptMonupRmonUnicastCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMonupRmonUnicastCounterClientInputOverloadPortn.setStatus("current")
_Pm10010mptMonupRmonNonunicastCounterClientInputTable_Object = MibTable
pm10010mptMonupRmonNonunicastCounterClientInputTable = _Pm10010mptMonupRmonNonunicastCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 176)
)
if mibBuilder.loadTexts:
    pm10010mptMonupRmonNonunicastCounterClientInputTable.setStatus("current")
_Pm10010mptMonupRmonNonunicastCounterClientInputEntry_Object = MibTableRow
pm10010mptMonupRmonNonunicastCounterClientInputEntry = _Pm10010mptMonupRmonNonunicastCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 176, 1)
)
pm10010mptMonupRmonNonunicastCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptMonupRmonNonunicastCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptMonupRmonNonunicastCounterClientInputEntry.setStatus("current")


class _Pm10010mptMonupRmonNonunicastCounterClientInputIndex_Type(Integer32):
    """Custom type pm10010mptMonupRmonNonunicastCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptMonupRmonNonunicastCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm10010mptMonupRmonNonunicastCounterClientInputIndex_Object = MibTableColumn
pm10010mptMonupRmonNonunicastCounterClientInputIndex = _Pm10010mptMonupRmonNonunicastCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 176, 1, 1),
    _Pm10010mptMonupRmonNonunicastCounterClientInputIndex_Type()
)
pm10010mptMonupRmonNonunicastCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMonupRmonNonunicastCounterClientInputIndex.setStatus("current")
_Pm10010mptMonupRmonNonunicastCounterClientInputValuePortn_Type = Counter64
_Pm10010mptMonupRmonNonunicastCounterClientInputValuePortn_Object = MibTableColumn
pm10010mptMonupRmonNonunicastCounterClientInputValuePortn = _Pm10010mptMonupRmonNonunicastCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 176, 1, 2),
    _Pm10010mptMonupRmonNonunicastCounterClientInputValuePortn_Type()
)
pm10010mptMonupRmonNonunicastCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMonupRmonNonunicastCounterClientInputValuePortn.setStatus("current")
_Pm10010mptMonupRmonNonunicastCounterClientInputErrorPortn_Type = EkiOnOff
_Pm10010mptMonupRmonNonunicastCounterClientInputErrorPortn_Object = MibTableColumn
pm10010mptMonupRmonNonunicastCounterClientInputErrorPortn = _Pm10010mptMonupRmonNonunicastCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 176, 1, 3),
    _Pm10010mptMonupRmonNonunicastCounterClientInputErrorPortn_Type()
)
pm10010mptMonupRmonNonunicastCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMonupRmonNonunicastCounterClientInputErrorPortn.setStatus("current")
_Pm10010mptMonupRmonNonunicastCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm10010mptMonupRmonNonunicastCounterClientInputOverloadPortn_Object = MibTableColumn
pm10010mptMonupRmonNonunicastCounterClientInputOverloadPortn = _Pm10010mptMonupRmonNonunicastCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 176, 1, 4),
    _Pm10010mptMonupRmonNonunicastCounterClientInputOverloadPortn_Type()
)
pm10010mptMonupRmonNonunicastCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMonupRmonNonunicastCounterClientInputOverloadPortn.setStatus("current")
_Pm10010mptMondownRmonBytesCounterClientOutputTable_Object = MibTable
pm10010mptMondownRmonBytesCounterClientOutputTable = _Pm10010mptMondownRmonBytesCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 208)
)
if mibBuilder.loadTexts:
    pm10010mptMondownRmonBytesCounterClientOutputTable.setStatus("current")
_Pm10010mptMondownRmonBytesCounterClientOutputEntry_Object = MibTableRow
pm10010mptMondownRmonBytesCounterClientOutputEntry = _Pm10010mptMondownRmonBytesCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 208, 1)
)
pm10010mptMondownRmonBytesCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptMondownRmonBytesCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptMondownRmonBytesCounterClientOutputEntry.setStatus("current")


class _Pm10010mptMondownRmonBytesCounterClientOutputIndex_Type(Integer32):
    """Custom type pm10010mptMondownRmonBytesCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptMondownRmonBytesCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pm10010mptMondownRmonBytesCounterClientOutputIndex_Object = MibTableColumn
pm10010mptMondownRmonBytesCounterClientOutputIndex = _Pm10010mptMondownRmonBytesCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 208, 1, 1),
    _Pm10010mptMondownRmonBytesCounterClientOutputIndex_Type()
)
pm10010mptMondownRmonBytesCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMondownRmonBytesCounterClientOutputIndex.setStatus("current")
_Pm10010mptMondownRmonBytesCounterClientOutputValuePortn_Type = Counter64
_Pm10010mptMondownRmonBytesCounterClientOutputValuePortn_Object = MibTableColumn
pm10010mptMondownRmonBytesCounterClientOutputValuePortn = _Pm10010mptMondownRmonBytesCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 208, 1, 2),
    _Pm10010mptMondownRmonBytesCounterClientOutputValuePortn_Type()
)
pm10010mptMondownRmonBytesCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMondownRmonBytesCounterClientOutputValuePortn.setStatus("current")
_Pm10010mptMondownRmonBytesCounterClientOutputErrorPortn_Type = EkiOnOff
_Pm10010mptMondownRmonBytesCounterClientOutputErrorPortn_Object = MibTableColumn
pm10010mptMondownRmonBytesCounterClientOutputErrorPortn = _Pm10010mptMondownRmonBytesCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 208, 1, 3),
    _Pm10010mptMondownRmonBytesCounterClientOutputErrorPortn_Type()
)
pm10010mptMondownRmonBytesCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMondownRmonBytesCounterClientOutputErrorPortn.setStatus("current")
_Pm10010mptMondownRmonBytesCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pm10010mptMondownRmonBytesCounterClientOutputOverloadPortn_Object = MibTableColumn
pm10010mptMondownRmonBytesCounterClientOutputOverloadPortn = _Pm10010mptMondownRmonBytesCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 208, 1, 4),
    _Pm10010mptMondownRmonBytesCounterClientOutputOverloadPortn_Type()
)
pm10010mptMondownRmonBytesCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMondownRmonBytesCounterClientOutputOverloadPortn.setStatus("current")
_Pm10010mptMondownRmonCrcErrorsCounterClientOutputTable_Object = MibTable
pm10010mptMondownRmonCrcErrorsCounterClientOutputTable = _Pm10010mptMondownRmonCrcErrorsCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 224)
)
if mibBuilder.loadTexts:
    pm10010mptMondownRmonCrcErrorsCounterClientOutputTable.setStatus("current")
_Pm10010mptMondownRmonCrcErrorsCounterClientOutputEntry_Object = MibTableRow
pm10010mptMondownRmonCrcErrorsCounterClientOutputEntry = _Pm10010mptMondownRmonCrcErrorsCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 224, 1)
)
pm10010mptMondownRmonCrcErrorsCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptMondownRmonCrcErrorsCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptMondownRmonCrcErrorsCounterClientOutputEntry.setStatus("current")


class _Pm10010mptMondownRmonCrcErrorsCounterClientOutputIndex_Type(Integer32):
    """Custom type pm10010mptMondownRmonCrcErrorsCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptMondownRmonCrcErrorsCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pm10010mptMondownRmonCrcErrorsCounterClientOutputIndex_Object = MibTableColumn
pm10010mptMondownRmonCrcErrorsCounterClientOutputIndex = _Pm10010mptMondownRmonCrcErrorsCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 224, 1, 1),
    _Pm10010mptMondownRmonCrcErrorsCounterClientOutputIndex_Type()
)
pm10010mptMondownRmonCrcErrorsCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMondownRmonCrcErrorsCounterClientOutputIndex.setStatus("current")
_Pm10010mptMondownRmonCrcErrorsCounterClientOutputValuePortn_Type = Counter64
_Pm10010mptMondownRmonCrcErrorsCounterClientOutputValuePortn_Object = MibTableColumn
pm10010mptMondownRmonCrcErrorsCounterClientOutputValuePortn = _Pm10010mptMondownRmonCrcErrorsCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 224, 1, 2),
    _Pm10010mptMondownRmonCrcErrorsCounterClientOutputValuePortn_Type()
)
pm10010mptMondownRmonCrcErrorsCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMondownRmonCrcErrorsCounterClientOutputValuePortn.setStatus("current")
_Pm10010mptMondownRmonCrcErrorsCounterClientOutputErrorPortn_Type = EkiOnOff
_Pm10010mptMondownRmonCrcErrorsCounterClientOutputErrorPortn_Object = MibTableColumn
pm10010mptMondownRmonCrcErrorsCounterClientOutputErrorPortn = _Pm10010mptMondownRmonCrcErrorsCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 224, 1, 3),
    _Pm10010mptMondownRmonCrcErrorsCounterClientOutputErrorPortn_Type()
)
pm10010mptMondownRmonCrcErrorsCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMondownRmonCrcErrorsCounterClientOutputErrorPortn.setStatus("current")
_Pm10010mptMondownRmonCrcErrorsCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pm10010mptMondownRmonCrcErrorsCounterClientOutputOverloadPortn_Object = MibTableColumn
pm10010mptMondownRmonCrcErrorsCounterClientOutputOverloadPortn = _Pm10010mptMondownRmonCrcErrorsCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 224, 1, 4),
    _Pm10010mptMondownRmonCrcErrorsCounterClientOutputOverloadPortn_Type()
)
pm10010mptMondownRmonCrcErrorsCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMondownRmonCrcErrorsCounterClientOutputOverloadPortn.setStatus("current")
_Pm10010mptMondownRmonPacketsCounterClientOutputTable_Object = MibTable
pm10010mptMondownRmonPacketsCounterClientOutputTable = _Pm10010mptMondownRmonPacketsCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 240)
)
if mibBuilder.loadTexts:
    pm10010mptMondownRmonPacketsCounterClientOutputTable.setStatus("current")
_Pm10010mptMondownRmonPacketsCounterClientOutputEntry_Object = MibTableRow
pm10010mptMondownRmonPacketsCounterClientOutputEntry = _Pm10010mptMondownRmonPacketsCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 240, 1)
)
pm10010mptMondownRmonPacketsCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptMondownRmonPacketsCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptMondownRmonPacketsCounterClientOutputEntry.setStatus("current")


class _Pm10010mptMondownRmonPacketsCounterClientOutputIndex_Type(Integer32):
    """Custom type pm10010mptMondownRmonPacketsCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptMondownRmonPacketsCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pm10010mptMondownRmonPacketsCounterClientOutputIndex_Object = MibTableColumn
pm10010mptMondownRmonPacketsCounterClientOutputIndex = _Pm10010mptMondownRmonPacketsCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 240, 1, 1),
    _Pm10010mptMondownRmonPacketsCounterClientOutputIndex_Type()
)
pm10010mptMondownRmonPacketsCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMondownRmonPacketsCounterClientOutputIndex.setStatus("current")
_Pm10010mptMondownRmonPacketsCounterClientOutputValuePortn_Type = Counter64
_Pm10010mptMondownRmonPacketsCounterClientOutputValuePortn_Object = MibTableColumn
pm10010mptMondownRmonPacketsCounterClientOutputValuePortn = _Pm10010mptMondownRmonPacketsCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 240, 1, 2),
    _Pm10010mptMondownRmonPacketsCounterClientOutputValuePortn_Type()
)
pm10010mptMondownRmonPacketsCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMondownRmonPacketsCounterClientOutputValuePortn.setStatus("current")
_Pm10010mptMondownRmonPacketsCounterClientOutputErrorPortn_Type = EkiOnOff
_Pm10010mptMondownRmonPacketsCounterClientOutputErrorPortn_Object = MibTableColumn
pm10010mptMondownRmonPacketsCounterClientOutputErrorPortn = _Pm10010mptMondownRmonPacketsCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 240, 1, 3),
    _Pm10010mptMondownRmonPacketsCounterClientOutputErrorPortn_Type()
)
pm10010mptMondownRmonPacketsCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMondownRmonPacketsCounterClientOutputErrorPortn.setStatus("current")
_Pm10010mptMondownRmonPacketsCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pm10010mptMondownRmonPacketsCounterClientOutputOverloadPortn_Object = MibTableColumn
pm10010mptMondownRmonPacketsCounterClientOutputOverloadPortn = _Pm10010mptMondownRmonPacketsCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 240, 1, 4),
    _Pm10010mptMondownRmonPacketsCounterClientOutputOverloadPortn_Type()
)
pm10010mptMondownRmonPacketsCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMondownRmonPacketsCounterClientOutputOverloadPortn.setStatus("current")
_Pm10010mptMondownRmonBroadcastCounterClientOutputTable_Object = MibTable
pm10010mptMondownRmonBroadcastCounterClientOutputTable = _Pm10010mptMondownRmonBroadcastCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 256)
)
if mibBuilder.loadTexts:
    pm10010mptMondownRmonBroadcastCounterClientOutputTable.setStatus("current")
_Pm10010mptMondownRmonBroadcastCounterClientOutputEntry_Object = MibTableRow
pm10010mptMondownRmonBroadcastCounterClientOutputEntry = _Pm10010mptMondownRmonBroadcastCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 256, 1)
)
pm10010mptMondownRmonBroadcastCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptMondownRmonBroadcastCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptMondownRmonBroadcastCounterClientOutputEntry.setStatus("current")


class _Pm10010mptMondownRmonBroadcastCounterClientOutputIndex_Type(Integer32):
    """Custom type pm10010mptMondownRmonBroadcastCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptMondownRmonBroadcastCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pm10010mptMondownRmonBroadcastCounterClientOutputIndex_Object = MibTableColumn
pm10010mptMondownRmonBroadcastCounterClientOutputIndex = _Pm10010mptMondownRmonBroadcastCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 256, 1, 1),
    _Pm10010mptMondownRmonBroadcastCounterClientOutputIndex_Type()
)
pm10010mptMondownRmonBroadcastCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMondownRmonBroadcastCounterClientOutputIndex.setStatus("current")
_Pm10010mptMondownRmonBroadcastCounterClientOutputValuePortn_Type = Counter64
_Pm10010mptMondownRmonBroadcastCounterClientOutputValuePortn_Object = MibTableColumn
pm10010mptMondownRmonBroadcastCounterClientOutputValuePortn = _Pm10010mptMondownRmonBroadcastCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 256, 1, 2),
    _Pm10010mptMondownRmonBroadcastCounterClientOutputValuePortn_Type()
)
pm10010mptMondownRmonBroadcastCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMondownRmonBroadcastCounterClientOutputValuePortn.setStatus("current")
_Pm10010mptMondownRmonBroadcastCounterClientOutputErrorPortn_Type = EkiOnOff
_Pm10010mptMondownRmonBroadcastCounterClientOutputErrorPortn_Object = MibTableColumn
pm10010mptMondownRmonBroadcastCounterClientOutputErrorPortn = _Pm10010mptMondownRmonBroadcastCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 256, 1, 3),
    _Pm10010mptMondownRmonBroadcastCounterClientOutputErrorPortn_Type()
)
pm10010mptMondownRmonBroadcastCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMondownRmonBroadcastCounterClientOutputErrorPortn.setStatus("current")
_Pm10010mptMondownRmonBroadcastCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pm10010mptMondownRmonBroadcastCounterClientOutputOverloadPortn_Object = MibTableColumn
pm10010mptMondownRmonBroadcastCounterClientOutputOverloadPortn = _Pm10010mptMondownRmonBroadcastCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 256, 1, 4),
    _Pm10010mptMondownRmonBroadcastCounterClientOutputOverloadPortn_Type()
)
pm10010mptMondownRmonBroadcastCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMondownRmonBroadcastCounterClientOutputOverloadPortn.setStatus("current")
_Pm10010mptMondownRmonMulticastCounterClientOutputTable_Object = MibTable
pm10010mptMondownRmonMulticastCounterClientOutputTable = _Pm10010mptMondownRmonMulticastCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 272)
)
if mibBuilder.loadTexts:
    pm10010mptMondownRmonMulticastCounterClientOutputTable.setStatus("current")
_Pm10010mptMondownRmonMulticastCounterClientOutputEntry_Object = MibTableRow
pm10010mptMondownRmonMulticastCounterClientOutputEntry = _Pm10010mptMondownRmonMulticastCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 272, 1)
)
pm10010mptMondownRmonMulticastCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptMondownRmonMulticastCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptMondownRmonMulticastCounterClientOutputEntry.setStatus("current")


class _Pm10010mptMondownRmonMulticastCounterClientOutputIndex_Type(Integer32):
    """Custom type pm10010mptMondownRmonMulticastCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptMondownRmonMulticastCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pm10010mptMondownRmonMulticastCounterClientOutputIndex_Object = MibTableColumn
pm10010mptMondownRmonMulticastCounterClientOutputIndex = _Pm10010mptMondownRmonMulticastCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 272, 1, 1),
    _Pm10010mptMondownRmonMulticastCounterClientOutputIndex_Type()
)
pm10010mptMondownRmonMulticastCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMondownRmonMulticastCounterClientOutputIndex.setStatus("current")
_Pm10010mptMondownRmonMulticastCounterClientOutputValuePortn_Type = Counter64
_Pm10010mptMondownRmonMulticastCounterClientOutputValuePortn_Object = MibTableColumn
pm10010mptMondownRmonMulticastCounterClientOutputValuePortn = _Pm10010mptMondownRmonMulticastCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 272, 1, 2),
    _Pm10010mptMondownRmonMulticastCounterClientOutputValuePortn_Type()
)
pm10010mptMondownRmonMulticastCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMondownRmonMulticastCounterClientOutputValuePortn.setStatus("current")
_Pm10010mptMondownRmonMulticastCounterClientOutputErrorPortn_Type = EkiOnOff
_Pm10010mptMondownRmonMulticastCounterClientOutputErrorPortn_Object = MibTableColumn
pm10010mptMondownRmonMulticastCounterClientOutputErrorPortn = _Pm10010mptMondownRmonMulticastCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 272, 1, 3),
    _Pm10010mptMondownRmonMulticastCounterClientOutputErrorPortn_Type()
)
pm10010mptMondownRmonMulticastCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMondownRmonMulticastCounterClientOutputErrorPortn.setStatus("current")
_Pm10010mptMondownRmonMulticastCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pm10010mptMondownRmonMulticastCounterClientOutputOverloadPortn_Object = MibTableColumn
pm10010mptMondownRmonMulticastCounterClientOutputOverloadPortn = _Pm10010mptMondownRmonMulticastCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 272, 1, 4),
    _Pm10010mptMondownRmonMulticastCounterClientOutputOverloadPortn_Type()
)
pm10010mptMondownRmonMulticastCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMondownRmonMulticastCounterClientOutputOverloadPortn.setStatus("current")
_Pm10010mptMondownRmonPauseFrameCounterClientOutputTable_Object = MibTable
pm10010mptMondownRmonPauseFrameCounterClientOutputTable = _Pm10010mptMondownRmonPauseFrameCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 288)
)
if mibBuilder.loadTexts:
    pm10010mptMondownRmonPauseFrameCounterClientOutputTable.setStatus("current")
_Pm10010mptMondownRmonPauseFrameCounterClientOutputEntry_Object = MibTableRow
pm10010mptMondownRmonPauseFrameCounterClientOutputEntry = _Pm10010mptMondownRmonPauseFrameCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 288, 1)
)
pm10010mptMondownRmonPauseFrameCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptMondownRmonPauseFrameCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptMondownRmonPauseFrameCounterClientOutputEntry.setStatus("current")


class _Pm10010mptMondownRmonPauseFrameCounterClientOutputIndex_Type(Integer32):
    """Custom type pm10010mptMondownRmonPauseFrameCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptMondownRmonPauseFrameCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pm10010mptMondownRmonPauseFrameCounterClientOutputIndex_Object = MibTableColumn
pm10010mptMondownRmonPauseFrameCounterClientOutputIndex = _Pm10010mptMondownRmonPauseFrameCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 288, 1, 1),
    _Pm10010mptMondownRmonPauseFrameCounterClientOutputIndex_Type()
)
pm10010mptMondownRmonPauseFrameCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMondownRmonPauseFrameCounterClientOutputIndex.setStatus("current")
_Pm10010mptMondownRmonPauseFrameCounterClientOutputValuePortn_Type = Counter64
_Pm10010mptMondownRmonPauseFrameCounterClientOutputValuePortn_Object = MibTableColumn
pm10010mptMondownRmonPauseFrameCounterClientOutputValuePortn = _Pm10010mptMondownRmonPauseFrameCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 288, 1, 2),
    _Pm10010mptMondownRmonPauseFrameCounterClientOutputValuePortn_Type()
)
pm10010mptMondownRmonPauseFrameCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMondownRmonPauseFrameCounterClientOutputValuePortn.setStatus("current")
_Pm10010mptMondownRmonPauseFrameCounterClientOutputErrorPortn_Type = EkiOnOff
_Pm10010mptMondownRmonPauseFrameCounterClientOutputErrorPortn_Object = MibTableColumn
pm10010mptMondownRmonPauseFrameCounterClientOutputErrorPortn = _Pm10010mptMondownRmonPauseFrameCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 288, 1, 3),
    _Pm10010mptMondownRmonPauseFrameCounterClientOutputErrorPortn_Type()
)
pm10010mptMondownRmonPauseFrameCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMondownRmonPauseFrameCounterClientOutputErrorPortn.setStatus("current")
_Pm10010mptMondownRmonPauseFrameCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pm10010mptMondownRmonPauseFrameCounterClientOutputOverloadPortn_Object = MibTableColumn
pm10010mptMondownRmonPauseFrameCounterClientOutputOverloadPortn = _Pm10010mptMondownRmonPauseFrameCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 288, 1, 4),
    _Pm10010mptMondownRmonPauseFrameCounterClientOutputOverloadPortn_Type()
)
pm10010mptMondownRmonPauseFrameCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMondownRmonPauseFrameCounterClientOutputOverloadPortn.setStatus("current")
_Pm10010mptMondownRmonUnicastCounterClientOutputTable_Object = MibTable
pm10010mptMondownRmonUnicastCounterClientOutputTable = _Pm10010mptMondownRmonUnicastCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 352)
)
if mibBuilder.loadTexts:
    pm10010mptMondownRmonUnicastCounterClientOutputTable.setStatus("current")
_Pm10010mptMondownRmonUnicastCounterClientOutputEntry_Object = MibTableRow
pm10010mptMondownRmonUnicastCounterClientOutputEntry = _Pm10010mptMondownRmonUnicastCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 352, 1)
)
pm10010mptMondownRmonUnicastCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptMondownRmonUnicastCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptMondownRmonUnicastCounterClientOutputEntry.setStatus("current")


class _Pm10010mptMondownRmonUnicastCounterClientOutputIndex_Type(Integer32):
    """Custom type pm10010mptMondownRmonUnicastCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptMondownRmonUnicastCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pm10010mptMondownRmonUnicastCounterClientOutputIndex_Object = MibTableColumn
pm10010mptMondownRmonUnicastCounterClientOutputIndex = _Pm10010mptMondownRmonUnicastCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 352, 1, 1),
    _Pm10010mptMondownRmonUnicastCounterClientOutputIndex_Type()
)
pm10010mptMondownRmonUnicastCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMondownRmonUnicastCounterClientOutputIndex.setStatus("current")
_Pm10010mptMondownRmonUnicastCounterClientOutputValuePortn_Type = Counter64
_Pm10010mptMondownRmonUnicastCounterClientOutputValuePortn_Object = MibTableColumn
pm10010mptMondownRmonUnicastCounterClientOutputValuePortn = _Pm10010mptMondownRmonUnicastCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 352, 1, 2),
    _Pm10010mptMondownRmonUnicastCounterClientOutputValuePortn_Type()
)
pm10010mptMondownRmonUnicastCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMondownRmonUnicastCounterClientOutputValuePortn.setStatus("current")
_Pm10010mptMondownRmonUnicastCounterClientOutputErrorPortn_Type = EkiOnOff
_Pm10010mptMondownRmonUnicastCounterClientOutputErrorPortn_Object = MibTableColumn
pm10010mptMondownRmonUnicastCounterClientOutputErrorPortn = _Pm10010mptMondownRmonUnicastCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 352, 1, 3),
    _Pm10010mptMondownRmonUnicastCounterClientOutputErrorPortn_Type()
)
pm10010mptMondownRmonUnicastCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMondownRmonUnicastCounterClientOutputErrorPortn.setStatus("current")
_Pm10010mptMondownRmonUnicastCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pm10010mptMondownRmonUnicastCounterClientOutputOverloadPortn_Object = MibTableColumn
pm10010mptMondownRmonUnicastCounterClientOutputOverloadPortn = _Pm10010mptMondownRmonUnicastCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 352, 1, 4),
    _Pm10010mptMondownRmonUnicastCounterClientOutputOverloadPortn_Type()
)
pm10010mptMondownRmonUnicastCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMondownRmonUnicastCounterClientOutputOverloadPortn.setStatus("current")
_Pm10010mptMondownRmonNonunicastCounterClientOutputTable_Object = MibTable
pm10010mptMondownRmonNonunicastCounterClientOutputTable = _Pm10010mptMondownRmonNonunicastCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 368)
)
if mibBuilder.loadTexts:
    pm10010mptMondownRmonNonunicastCounterClientOutputTable.setStatus("current")
_Pm10010mptMondownRmonNonunicastCounterClientOutputEntry_Object = MibTableRow
pm10010mptMondownRmonNonunicastCounterClientOutputEntry = _Pm10010mptMondownRmonNonunicastCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 368, 1)
)
pm10010mptMondownRmonNonunicastCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptMondownRmonNonunicastCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptMondownRmonNonunicastCounterClientOutputEntry.setStatus("current")


class _Pm10010mptMondownRmonNonunicastCounterClientOutputIndex_Type(Integer32):
    """Custom type pm10010mptMondownRmonNonunicastCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptMondownRmonNonunicastCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pm10010mptMondownRmonNonunicastCounterClientOutputIndex_Object = MibTableColumn
pm10010mptMondownRmonNonunicastCounterClientOutputIndex = _Pm10010mptMondownRmonNonunicastCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 368, 1, 1),
    _Pm10010mptMondownRmonNonunicastCounterClientOutputIndex_Type()
)
pm10010mptMondownRmonNonunicastCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMondownRmonNonunicastCounterClientOutputIndex.setStatus("current")
_Pm10010mptMondownRmonNonunicastCounterClientOutputValuePortn_Type = Counter64
_Pm10010mptMondownRmonNonunicastCounterClientOutputValuePortn_Object = MibTableColumn
pm10010mptMondownRmonNonunicastCounterClientOutputValuePortn = _Pm10010mptMondownRmonNonunicastCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 368, 1, 2),
    _Pm10010mptMondownRmonNonunicastCounterClientOutputValuePortn_Type()
)
pm10010mptMondownRmonNonunicastCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMondownRmonNonunicastCounterClientOutputValuePortn.setStatus("current")
_Pm10010mptMondownRmonNonunicastCounterClientOutputErrorPortn_Type = EkiOnOff
_Pm10010mptMondownRmonNonunicastCounterClientOutputErrorPortn_Object = MibTableColumn
pm10010mptMondownRmonNonunicastCounterClientOutputErrorPortn = _Pm10010mptMondownRmonNonunicastCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 368, 1, 3),
    _Pm10010mptMondownRmonNonunicastCounterClientOutputErrorPortn_Type()
)
pm10010mptMondownRmonNonunicastCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMondownRmonNonunicastCounterClientOutputErrorPortn.setStatus("current")
_Pm10010mptMondownRmonNonunicastCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pm10010mptMondownRmonNonunicastCounterClientOutputOverloadPortn_Object = MibTableColumn
pm10010mptMondownRmonNonunicastCounterClientOutputOverloadPortn = _Pm10010mptMondownRmonNonunicastCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 2, 4, 368, 1, 4),
    _Pm10010mptMondownRmonNonunicastCounterClientOutputOverloadPortn_Type()
)
pm10010mptMondownRmonNonunicastCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptMondownRmonNonunicastCounterClientOutputOverloadPortn.setStatus("current")
_Pm10010mptMonPerfOther_ObjectIdentity = ObjectIdentity
pm10010mptMonPerfOther = _Pm10010mptMonPerfOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 5)
)
_Pm10010mptMonPerfSync_ObjectIdentity = ObjectIdentity
pm10010mptMonPerfSync = _Pm10010mptMonPerfSync_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 5, 1)
)
_Pm10010mptPerfEnable_Type = EkiOnOff
_Pm10010mptPerfEnable_Object = MibScalar
pm10010mptPerfEnable = _Pm10010mptPerfEnable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 5, 1, 257),
    _Pm10010mptPerfEnable_Type()
)
pm10010mptPerfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptPerfEnable.setStatus("current")
_Pm10010mptPerf15minSync_Type = EkiOnOff
_Pm10010mptPerf15minSync_Object = MibScalar
pm10010mptPerf15minSync = _Pm10010mptPerf15minSync_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 5, 1, 259),
    _Pm10010mptPerf15minSync_Type()
)
pm10010mptPerf15minSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptPerf15minSync.setStatus("current")
_Pm10010mptPerf24hSync_Type = EkiOnOff
_Pm10010mptPerf24hSync_Object = MibScalar
pm10010mptPerf24hSync = _Pm10010mptPerf24hSync_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 5, 1, 260),
    _Pm10010mptPerf24hSync_Type()
)
pm10010mptPerf24hSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptPerf24hSync.setStatus("current")
_Pm10010mptMonPerfTimeStamp_ObjectIdentity = ObjectIdentity
pm10010mptMonPerfTimeStamp = _Pm10010mptMonPerfTimeStamp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 5, 2)
)
_Pm10010mptPerf15MinShort_Type = EkiOnOff
_Pm10010mptPerf15MinShort_Object = MibScalar
pm10010mptPerf15MinShort = _Pm10010mptPerf15MinShort_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 5, 2, 1),
    _Pm10010mptPerf15MinShort_Type()
)
pm10010mptPerf15MinShort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptPerf15MinShort.setStatus("current")
_Pm10010mptPerf15MinLong_Type = EkiOnOff
_Pm10010mptPerf15MinLong_Object = MibScalar
pm10010mptPerf15MinLong = _Pm10010mptPerf15MinLong_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 5, 2, 2),
    _Pm10010mptPerf15MinLong_Type()
)
pm10010mptPerf15MinLong.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptPerf15MinLong.setStatus("current")
_Pm10010mptPerf24HoursShort_Type = Counter32
_Pm10010mptPerf24HoursShort_Object = MibScalar
pm10010mptPerf24HoursShort = _Pm10010mptPerf24HoursShort_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 5, 2, 5),
    _Pm10010mptPerf24HoursShort_Type()
)
pm10010mptPerf24HoursShort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptPerf24HoursShort.setStatus("current")
_Pm10010mptPerf24HoursLong_Type = Counter32
_Pm10010mptPerf24HoursLong_Object = MibScalar
pm10010mptPerf24HoursLong = _Pm10010mptPerf24HoursLong_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 5, 2, 6),
    _Pm10010mptPerf24HoursLong_Type()
)
pm10010mptPerf24HoursLong.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptPerf24HoursLong.setStatus("current")
_Pm10010mptPerfCurrent15MinElapsedTime_Type = Counter32
_Pm10010mptPerfCurrent15MinElapsedTime_Object = MibScalar
pm10010mptPerfCurrent15MinElapsedTime = _Pm10010mptPerfCurrent15MinElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 5, 2, 7),
    _Pm10010mptPerfCurrent15MinElapsedTime_Type()
)
pm10010mptPerfCurrent15MinElapsedTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptPerfCurrent15MinElapsedTime.setStatus("current")
_Pm10010mptPerfCurrent24HoursElapsedTime_Type = Counter32
_Pm10010mptPerfCurrent24HoursElapsedTime_Object = MibScalar
pm10010mptPerfCurrent24HoursElapsedTime = _Pm10010mptPerfCurrent24HoursElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 5, 2, 8),
    _Pm10010mptPerfCurrent24HoursElapsedTime_Type()
)
pm10010mptPerfCurrent24HoursElapsedTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mptPerfCurrent24HoursElapsedTime.setStatus("current")
_Pm10010mptMonPerfClient_ObjectIdentity = ObjectIdentity
pm10010mptMonPerfClient = _Pm10010mptMonPerfClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6)
)
_Pm10010mptPerfTelecomInputClientCurrent15StatTable_Object = MibTable
pm10010mptPerfTelecomInputClientCurrent15StatTable = _Pm10010mptPerfTelecomInputClientCurrent15StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 16)
)
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomInputClientCurrent15StatTable.setStatus("current")
_Pm10010mptPerfTelecomInputClientCurrent15StatEntry_Object = MibTableRow
pm10010mptPerfTelecomInputClientCurrent15StatEntry = _Pm10010mptPerfTelecomInputClientCurrent15StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 16, 1)
)
pm10010mptPerfTelecomInputClientCurrent15StatEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptPerfTelecomInputClientCurrent15StatIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomInputClientCurrent15StatEntry.setStatus("current")


class _Pm10010mptPerfTelecomInputClientCurrent15StatIndex_Type(Integer32):
    """Custom type pm10010mptPerfTelecomInputClientCurrent15StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptPerfTelecomInputClientCurrent15StatIndex_Type.__name__ = "Integer32"
_Pm10010mptPerfTelecomInputClientCurrent15StatIndex_Object = MibTableColumn
pm10010mptPerfTelecomInputClientCurrent15StatIndex = _Pm10010mptPerfTelecomInputClientCurrent15StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 16, 1, 1),
    _Pm10010mptPerfTelecomInputClientCurrent15StatIndex_Type()
)
pm10010mptPerfTelecomInputClientCurrent15StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomInputClientCurrent15StatIndex.setStatus("current")
_Pm10010mptPerfTelecomInputClientCurrent15StatInvCvPortn_Type = EkiOnOff
_Pm10010mptPerfTelecomInputClientCurrent15StatInvCvPortn_Object = MibTableColumn
pm10010mptPerfTelecomInputClientCurrent15StatInvCvPortn = _Pm10010mptPerfTelecomInputClientCurrent15StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 16, 1, 2),
    _Pm10010mptPerfTelecomInputClientCurrent15StatInvCvPortn_Type()
)
pm10010mptPerfTelecomInputClientCurrent15StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomInputClientCurrent15StatInvCvPortn.setStatus("current")
_Pm10010mptPerfTelecomInputClientCurrent15StatCvValuePortn_Type = Unsigned32
_Pm10010mptPerfTelecomInputClientCurrent15StatCvValuePortn_Object = MibTableColumn
pm10010mptPerfTelecomInputClientCurrent15StatCvValuePortn = _Pm10010mptPerfTelecomInputClientCurrent15StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 16, 1, 3),
    _Pm10010mptPerfTelecomInputClientCurrent15StatCvValuePortn_Type()
)
pm10010mptPerfTelecomInputClientCurrent15StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomInputClientCurrent15StatCvValuePortn.setStatus("current")
_Pm10010mptPerfTelecomInputClientCurrent15StatInvEsPortn_Type = EkiOnOff
_Pm10010mptPerfTelecomInputClientCurrent15StatInvEsPortn_Object = MibTableColumn
pm10010mptPerfTelecomInputClientCurrent15StatInvEsPortn = _Pm10010mptPerfTelecomInputClientCurrent15StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 16, 1, 4),
    _Pm10010mptPerfTelecomInputClientCurrent15StatInvEsPortn_Type()
)
pm10010mptPerfTelecomInputClientCurrent15StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomInputClientCurrent15StatInvEsPortn.setStatus("current")
_Pm10010mptPerfTelecomInputClientCurrent15StatEsValuePortn_Type = Unsigned32
_Pm10010mptPerfTelecomInputClientCurrent15StatEsValuePortn_Object = MibTableColumn
pm10010mptPerfTelecomInputClientCurrent15StatEsValuePortn = _Pm10010mptPerfTelecomInputClientCurrent15StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 16, 1, 5),
    _Pm10010mptPerfTelecomInputClientCurrent15StatEsValuePortn_Type()
)
pm10010mptPerfTelecomInputClientCurrent15StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomInputClientCurrent15StatEsValuePortn.setStatus("current")
_Pm10010mptPerfTelecomInputClientCurrent15StatInvSesPortn_Type = EkiOnOff
_Pm10010mptPerfTelecomInputClientCurrent15StatInvSesPortn_Object = MibTableColumn
pm10010mptPerfTelecomInputClientCurrent15StatInvSesPortn = _Pm10010mptPerfTelecomInputClientCurrent15StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 16, 1, 6),
    _Pm10010mptPerfTelecomInputClientCurrent15StatInvSesPortn_Type()
)
pm10010mptPerfTelecomInputClientCurrent15StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomInputClientCurrent15StatInvSesPortn.setStatus("current")
_Pm10010mptPerfTelecomInputClientCurrent15StatSesValuePortn_Type = Unsigned32
_Pm10010mptPerfTelecomInputClientCurrent15StatSesValuePortn_Object = MibTableColumn
pm10010mptPerfTelecomInputClientCurrent15StatSesValuePortn = _Pm10010mptPerfTelecomInputClientCurrent15StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 16, 1, 7),
    _Pm10010mptPerfTelecomInputClientCurrent15StatSesValuePortn_Type()
)
pm10010mptPerfTelecomInputClientCurrent15StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomInputClientCurrent15StatSesValuePortn.setStatus("current")
_Pm10010mptPerfTelecomInputClientCurrent15StatInvSefsPortn_Type = EkiOnOff
_Pm10010mptPerfTelecomInputClientCurrent15StatInvSefsPortn_Object = MibTableColumn
pm10010mptPerfTelecomInputClientCurrent15StatInvSefsPortn = _Pm10010mptPerfTelecomInputClientCurrent15StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 16, 1, 8),
    _Pm10010mptPerfTelecomInputClientCurrent15StatInvSefsPortn_Type()
)
pm10010mptPerfTelecomInputClientCurrent15StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomInputClientCurrent15StatInvSefsPortn.setStatus("current")
_Pm10010mptPerfTelecomInputClientCurrent15StatSefsValuePortn_Type = Unsigned32
_Pm10010mptPerfTelecomInputClientCurrent15StatSefsValuePortn_Object = MibTableColumn
pm10010mptPerfTelecomInputClientCurrent15StatSefsValuePortn = _Pm10010mptPerfTelecomInputClientCurrent15StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 16, 1, 9),
    _Pm10010mptPerfTelecomInputClientCurrent15StatSefsValuePortn_Type()
)
pm10010mptPerfTelecomInputClientCurrent15StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomInputClientCurrent15StatSefsValuePortn.setStatus("current")
_Pm10010mptPerfTelecomInputClientCurrent15StatInvUasPortn_Type = EkiOnOff
_Pm10010mptPerfTelecomInputClientCurrent15StatInvUasPortn_Object = MibTableColumn
pm10010mptPerfTelecomInputClientCurrent15StatInvUasPortn = _Pm10010mptPerfTelecomInputClientCurrent15StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 16, 1, 10),
    _Pm10010mptPerfTelecomInputClientCurrent15StatInvUasPortn_Type()
)
pm10010mptPerfTelecomInputClientCurrent15StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomInputClientCurrent15StatInvUasPortn.setStatus("current")
_Pm10010mptPerfTelecomInputClientCurrent15StatUasValuePortn_Type = Unsigned32
_Pm10010mptPerfTelecomInputClientCurrent15StatUasValuePortn_Object = MibTableColumn
pm10010mptPerfTelecomInputClientCurrent15StatUasValuePortn = _Pm10010mptPerfTelecomInputClientCurrent15StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 16, 1, 11),
    _Pm10010mptPerfTelecomInputClientCurrent15StatUasValuePortn_Type()
)
pm10010mptPerfTelecomInputClientCurrent15StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomInputClientCurrent15StatUasValuePortn.setStatus("current")
_Pm10010mptPerfTelecomInputClientPast15StatHistoryPort1Table_Object = MibTable
pm10010mptPerfTelecomInputClientPast15StatHistoryPort1Table = _Pm10010mptPerfTelecomInputClientPast15StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 32)
)
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomInputClientPast15StatHistoryPort1Table.setStatus("current")
_Pm10010mptPerfTelecomInputClientPast15StatHistoryPort1Entry_Object = MibTableRow
pm10010mptPerfTelecomInputClientPast15StatHistoryPort1Entry = _Pm10010mptPerfTelecomInputClientPast15StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 32, 1)
)
pm10010mptPerfTelecomInputClientPast15StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptPerfTelecomInputClientPast15StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomInputClientPast15StatHistoryPort1Entry.setStatus("current")


class _Pm10010mptPerfTelecomInputClientPast15StatHistoryPort1Index_Type(Integer32):
    """Custom type pm10010mptPerfTelecomInputClientPast15StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptPerfTelecomInputClientPast15StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm10010mptPerfTelecomInputClientPast15StatHistoryPort1Index_Object = MibTableColumn
pm10010mptPerfTelecomInputClientPast15StatHistoryPort1Index = _Pm10010mptPerfTelecomInputClientPast15StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 32, 1, 1),
    _Pm10010mptPerfTelecomInputClientPast15StatHistoryPort1Index_Type()
)
pm10010mptPerfTelecomInputClientPast15StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomInputClientPast15StatHistoryPort1Index.setStatus("current")
_Pm10010mptPerfTelecomInputClientPast15StatHistoryInvCvPort1_Type = EkiOnOff
_Pm10010mptPerfTelecomInputClientPast15StatHistoryInvCvPort1_Object = MibTableColumn
pm10010mptPerfTelecomInputClientPast15StatHistoryInvCvPort1 = _Pm10010mptPerfTelecomInputClientPast15StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 32, 1, 2),
    _Pm10010mptPerfTelecomInputClientPast15StatHistoryInvCvPort1_Type()
)
pm10010mptPerfTelecomInputClientPast15StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomInputClientPast15StatHistoryInvCvPort1.setStatus("current")
_Pm10010mptPerfTelecomInputClientPast15StatHistoryCvValuePort1_Type = Unsigned32
_Pm10010mptPerfTelecomInputClientPast15StatHistoryCvValuePort1_Object = MibTableColumn
pm10010mptPerfTelecomInputClientPast15StatHistoryCvValuePort1 = _Pm10010mptPerfTelecomInputClientPast15StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 32, 1, 3),
    _Pm10010mptPerfTelecomInputClientPast15StatHistoryCvValuePort1_Type()
)
pm10010mptPerfTelecomInputClientPast15StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomInputClientPast15StatHistoryCvValuePort1.setStatus("current")
_Pm10010mptPerfTelecomInputClientPast15StatHistoryInvEsPort1_Type = EkiOnOff
_Pm10010mptPerfTelecomInputClientPast15StatHistoryInvEsPort1_Object = MibTableColumn
pm10010mptPerfTelecomInputClientPast15StatHistoryInvEsPort1 = _Pm10010mptPerfTelecomInputClientPast15StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 32, 1, 4),
    _Pm10010mptPerfTelecomInputClientPast15StatHistoryInvEsPort1_Type()
)
pm10010mptPerfTelecomInputClientPast15StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomInputClientPast15StatHistoryInvEsPort1.setStatus("current")
_Pm10010mptPerfTelecomInputClientPast15StatHistoryEsValuePort1_Type = Unsigned32
_Pm10010mptPerfTelecomInputClientPast15StatHistoryEsValuePort1_Object = MibTableColumn
pm10010mptPerfTelecomInputClientPast15StatHistoryEsValuePort1 = _Pm10010mptPerfTelecomInputClientPast15StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 32, 1, 5),
    _Pm10010mptPerfTelecomInputClientPast15StatHistoryEsValuePort1_Type()
)
pm10010mptPerfTelecomInputClientPast15StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomInputClientPast15StatHistoryEsValuePort1.setStatus("current")
_Pm10010mptPerfTelecomInputClientPast15StatHistoryInvSesPort1_Type = EkiOnOff
_Pm10010mptPerfTelecomInputClientPast15StatHistoryInvSesPort1_Object = MibTableColumn
pm10010mptPerfTelecomInputClientPast15StatHistoryInvSesPort1 = _Pm10010mptPerfTelecomInputClientPast15StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 32, 1, 6),
    _Pm10010mptPerfTelecomInputClientPast15StatHistoryInvSesPort1_Type()
)
pm10010mptPerfTelecomInputClientPast15StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomInputClientPast15StatHistoryInvSesPort1.setStatus("current")
_Pm10010mptPerfTelecomInputClientPast15StatHistorySesValuePort1_Type = Unsigned32
_Pm10010mptPerfTelecomInputClientPast15StatHistorySesValuePort1_Object = MibTableColumn
pm10010mptPerfTelecomInputClientPast15StatHistorySesValuePort1 = _Pm10010mptPerfTelecomInputClientPast15StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 32, 1, 7),
    _Pm10010mptPerfTelecomInputClientPast15StatHistorySesValuePort1_Type()
)
pm10010mptPerfTelecomInputClientPast15StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomInputClientPast15StatHistorySesValuePort1.setStatus("current")
_Pm10010mptPerfTelecomInputClientPast15StatHistoryInvSefsPort1_Type = EkiOnOff
_Pm10010mptPerfTelecomInputClientPast15StatHistoryInvSefsPort1_Object = MibTableColumn
pm10010mptPerfTelecomInputClientPast15StatHistoryInvSefsPort1 = _Pm10010mptPerfTelecomInputClientPast15StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 32, 1, 8),
    _Pm10010mptPerfTelecomInputClientPast15StatHistoryInvSefsPort1_Type()
)
pm10010mptPerfTelecomInputClientPast15StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomInputClientPast15StatHistoryInvSefsPort1.setStatus("current")
_Pm10010mptPerfTelecomInputClientPast15StatHistorySefsValuePort1_Type = Unsigned32
_Pm10010mptPerfTelecomInputClientPast15StatHistorySefsValuePort1_Object = MibTableColumn
pm10010mptPerfTelecomInputClientPast15StatHistorySefsValuePort1 = _Pm10010mptPerfTelecomInputClientPast15StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 32, 1, 9),
    _Pm10010mptPerfTelecomInputClientPast15StatHistorySefsValuePort1_Type()
)
pm10010mptPerfTelecomInputClientPast15StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomInputClientPast15StatHistorySefsValuePort1.setStatus("current")
_Pm10010mptPerfTelecomInputClientPast15StatHistoryInvUasPort1_Type = EkiOnOff
_Pm10010mptPerfTelecomInputClientPast15StatHistoryInvUasPort1_Object = MibTableColumn
pm10010mptPerfTelecomInputClientPast15StatHistoryInvUasPort1 = _Pm10010mptPerfTelecomInputClientPast15StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 32, 1, 10),
    _Pm10010mptPerfTelecomInputClientPast15StatHistoryInvUasPort1_Type()
)
pm10010mptPerfTelecomInputClientPast15StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomInputClientPast15StatHistoryInvUasPort1.setStatus("current")
_Pm10010mptPerfTelecomInputClientPast15StatHistoryUasValuePort1_Type = Unsigned32
_Pm10010mptPerfTelecomInputClientPast15StatHistoryUasValuePort1_Object = MibTableColumn
pm10010mptPerfTelecomInputClientPast15StatHistoryUasValuePort1 = _Pm10010mptPerfTelecomInputClientPast15StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 32, 1, 11),
    _Pm10010mptPerfTelecomInputClientPast15StatHistoryUasValuePort1_Type()
)
pm10010mptPerfTelecomInputClientPast15StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomInputClientPast15StatHistoryUasValuePort1.setStatus("current")
_Pm10010mptPerfTelecomInputClientCurrent24StatTable_Object = MibTable
pm10010mptPerfTelecomInputClientCurrent24StatTable = _Pm10010mptPerfTelecomInputClientCurrent24StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 48)
)
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomInputClientCurrent24StatTable.setStatus("current")
_Pm10010mptPerfTelecomInputClientCurrent24StatEntry_Object = MibTableRow
pm10010mptPerfTelecomInputClientCurrent24StatEntry = _Pm10010mptPerfTelecomInputClientCurrent24StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 48, 1)
)
pm10010mptPerfTelecomInputClientCurrent24StatEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptPerfTelecomInputClientCurrent24StatIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomInputClientCurrent24StatEntry.setStatus("current")


class _Pm10010mptPerfTelecomInputClientCurrent24StatIndex_Type(Integer32):
    """Custom type pm10010mptPerfTelecomInputClientCurrent24StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptPerfTelecomInputClientCurrent24StatIndex_Type.__name__ = "Integer32"
_Pm10010mptPerfTelecomInputClientCurrent24StatIndex_Object = MibTableColumn
pm10010mptPerfTelecomInputClientCurrent24StatIndex = _Pm10010mptPerfTelecomInputClientCurrent24StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 48, 1, 1),
    _Pm10010mptPerfTelecomInputClientCurrent24StatIndex_Type()
)
pm10010mptPerfTelecomInputClientCurrent24StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomInputClientCurrent24StatIndex.setStatus("current")
_Pm10010mptPerfTelecomInputClientCurrent24StatInvCvPortn_Type = EkiOnOff
_Pm10010mptPerfTelecomInputClientCurrent24StatInvCvPortn_Object = MibTableColumn
pm10010mptPerfTelecomInputClientCurrent24StatInvCvPortn = _Pm10010mptPerfTelecomInputClientCurrent24StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 48, 1, 2),
    _Pm10010mptPerfTelecomInputClientCurrent24StatInvCvPortn_Type()
)
pm10010mptPerfTelecomInputClientCurrent24StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomInputClientCurrent24StatInvCvPortn.setStatus("current")
_Pm10010mptPerfTelecomInputClientCurrent24StatCvValuePortn_Type = Unsigned32
_Pm10010mptPerfTelecomInputClientCurrent24StatCvValuePortn_Object = MibTableColumn
pm10010mptPerfTelecomInputClientCurrent24StatCvValuePortn = _Pm10010mptPerfTelecomInputClientCurrent24StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 48, 1, 3),
    _Pm10010mptPerfTelecomInputClientCurrent24StatCvValuePortn_Type()
)
pm10010mptPerfTelecomInputClientCurrent24StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomInputClientCurrent24StatCvValuePortn.setStatus("current")
_Pm10010mptPerfTelecomInputClientCurrent24StatInvEsPortn_Type = EkiOnOff
_Pm10010mptPerfTelecomInputClientCurrent24StatInvEsPortn_Object = MibTableColumn
pm10010mptPerfTelecomInputClientCurrent24StatInvEsPortn = _Pm10010mptPerfTelecomInputClientCurrent24StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 48, 1, 4),
    _Pm10010mptPerfTelecomInputClientCurrent24StatInvEsPortn_Type()
)
pm10010mptPerfTelecomInputClientCurrent24StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomInputClientCurrent24StatInvEsPortn.setStatus("current")
_Pm10010mptPerfTelecomInputClientCurrent24StatEsValuePortn_Type = Unsigned32
_Pm10010mptPerfTelecomInputClientCurrent24StatEsValuePortn_Object = MibTableColumn
pm10010mptPerfTelecomInputClientCurrent24StatEsValuePortn = _Pm10010mptPerfTelecomInputClientCurrent24StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 48, 1, 5),
    _Pm10010mptPerfTelecomInputClientCurrent24StatEsValuePortn_Type()
)
pm10010mptPerfTelecomInputClientCurrent24StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomInputClientCurrent24StatEsValuePortn.setStatus("current")
_Pm10010mptPerfTelecomInputClientCurrent24StatInvSesPortn_Type = EkiOnOff
_Pm10010mptPerfTelecomInputClientCurrent24StatInvSesPortn_Object = MibTableColumn
pm10010mptPerfTelecomInputClientCurrent24StatInvSesPortn = _Pm10010mptPerfTelecomInputClientCurrent24StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 48, 1, 6),
    _Pm10010mptPerfTelecomInputClientCurrent24StatInvSesPortn_Type()
)
pm10010mptPerfTelecomInputClientCurrent24StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomInputClientCurrent24StatInvSesPortn.setStatus("current")
_Pm10010mptPerfTelecomInputClientCurrent24StatSesValuePortn_Type = Unsigned32
_Pm10010mptPerfTelecomInputClientCurrent24StatSesValuePortn_Object = MibTableColumn
pm10010mptPerfTelecomInputClientCurrent24StatSesValuePortn = _Pm10010mptPerfTelecomInputClientCurrent24StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 48, 1, 7),
    _Pm10010mptPerfTelecomInputClientCurrent24StatSesValuePortn_Type()
)
pm10010mptPerfTelecomInputClientCurrent24StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomInputClientCurrent24StatSesValuePortn.setStatus("current")
_Pm10010mptPerfTelecomInputClientCurrent24StatInvSefsPortn_Type = EkiOnOff
_Pm10010mptPerfTelecomInputClientCurrent24StatInvSefsPortn_Object = MibTableColumn
pm10010mptPerfTelecomInputClientCurrent24StatInvSefsPortn = _Pm10010mptPerfTelecomInputClientCurrent24StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 48, 1, 8),
    _Pm10010mptPerfTelecomInputClientCurrent24StatInvSefsPortn_Type()
)
pm10010mptPerfTelecomInputClientCurrent24StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomInputClientCurrent24StatInvSefsPortn.setStatus("current")
_Pm10010mptPerfTelecomInputClientCurrent24StatSefsValuePortn_Type = Unsigned32
_Pm10010mptPerfTelecomInputClientCurrent24StatSefsValuePortn_Object = MibTableColumn
pm10010mptPerfTelecomInputClientCurrent24StatSefsValuePortn = _Pm10010mptPerfTelecomInputClientCurrent24StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 48, 1, 9),
    _Pm10010mptPerfTelecomInputClientCurrent24StatSefsValuePortn_Type()
)
pm10010mptPerfTelecomInputClientCurrent24StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomInputClientCurrent24StatSefsValuePortn.setStatus("current")
_Pm10010mptPerfTelecomInputClientCurrent24StatInvUasPortn_Type = EkiOnOff
_Pm10010mptPerfTelecomInputClientCurrent24StatInvUasPortn_Object = MibTableColumn
pm10010mptPerfTelecomInputClientCurrent24StatInvUasPortn = _Pm10010mptPerfTelecomInputClientCurrent24StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 48, 1, 10),
    _Pm10010mptPerfTelecomInputClientCurrent24StatInvUasPortn_Type()
)
pm10010mptPerfTelecomInputClientCurrent24StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomInputClientCurrent24StatInvUasPortn.setStatus("current")
_Pm10010mptPerfTelecomInputClientCurrent24StatUasValuePortn_Type = Unsigned32
_Pm10010mptPerfTelecomInputClientCurrent24StatUasValuePortn_Object = MibTableColumn
pm10010mptPerfTelecomInputClientCurrent24StatUasValuePortn = _Pm10010mptPerfTelecomInputClientCurrent24StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 48, 1, 11),
    _Pm10010mptPerfTelecomInputClientCurrent24StatUasValuePortn_Type()
)
pm10010mptPerfTelecomInputClientCurrent24StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomInputClientCurrent24StatUasValuePortn.setStatus("current")
_Pm10010mptPerfTelecomInputClientPast24StatHistoryPort1Table_Object = MibTable
pm10010mptPerfTelecomInputClientPast24StatHistoryPort1Table = _Pm10010mptPerfTelecomInputClientPast24StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 64)
)
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomInputClientPast24StatHistoryPort1Table.setStatus("current")
_Pm10010mptPerfTelecomInputClientPast24StatHistoryPort1Entry_Object = MibTableRow
pm10010mptPerfTelecomInputClientPast24StatHistoryPort1Entry = _Pm10010mptPerfTelecomInputClientPast24StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 64, 1)
)
pm10010mptPerfTelecomInputClientPast24StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptPerfTelecomInputClientPast24StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomInputClientPast24StatHistoryPort1Entry.setStatus("current")


class _Pm10010mptPerfTelecomInputClientPast24StatHistoryPort1Index_Type(Integer32):
    """Custom type pm10010mptPerfTelecomInputClientPast24StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptPerfTelecomInputClientPast24StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm10010mptPerfTelecomInputClientPast24StatHistoryPort1Index_Object = MibTableColumn
pm10010mptPerfTelecomInputClientPast24StatHistoryPort1Index = _Pm10010mptPerfTelecomInputClientPast24StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 64, 1, 1),
    _Pm10010mptPerfTelecomInputClientPast24StatHistoryPort1Index_Type()
)
pm10010mptPerfTelecomInputClientPast24StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomInputClientPast24StatHistoryPort1Index.setStatus("current")
_Pm10010mptPerfTelecomInputClientPast24StatHistoryInvCvPort1_Type = EkiOnOff
_Pm10010mptPerfTelecomInputClientPast24StatHistoryInvCvPort1_Object = MibTableColumn
pm10010mptPerfTelecomInputClientPast24StatHistoryInvCvPort1 = _Pm10010mptPerfTelecomInputClientPast24StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 64, 1, 2),
    _Pm10010mptPerfTelecomInputClientPast24StatHistoryInvCvPort1_Type()
)
pm10010mptPerfTelecomInputClientPast24StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomInputClientPast24StatHistoryInvCvPort1.setStatus("current")
_Pm10010mptPerfTelecomInputClientPast24StatHistoryCvValuePort1_Type = Unsigned32
_Pm10010mptPerfTelecomInputClientPast24StatHistoryCvValuePort1_Object = MibTableColumn
pm10010mptPerfTelecomInputClientPast24StatHistoryCvValuePort1 = _Pm10010mptPerfTelecomInputClientPast24StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 64, 1, 3),
    _Pm10010mptPerfTelecomInputClientPast24StatHistoryCvValuePort1_Type()
)
pm10010mptPerfTelecomInputClientPast24StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomInputClientPast24StatHistoryCvValuePort1.setStatus("current")
_Pm10010mptPerfTelecomInputClientPast24StatHistoryInvEsPort1_Type = EkiOnOff
_Pm10010mptPerfTelecomInputClientPast24StatHistoryInvEsPort1_Object = MibTableColumn
pm10010mptPerfTelecomInputClientPast24StatHistoryInvEsPort1 = _Pm10010mptPerfTelecomInputClientPast24StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 64, 1, 4),
    _Pm10010mptPerfTelecomInputClientPast24StatHistoryInvEsPort1_Type()
)
pm10010mptPerfTelecomInputClientPast24StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomInputClientPast24StatHistoryInvEsPort1.setStatus("current")
_Pm10010mptPerfTelecomInputClientPast24StatHistoryEsValuePort1_Type = Unsigned32
_Pm10010mptPerfTelecomInputClientPast24StatHistoryEsValuePort1_Object = MibTableColumn
pm10010mptPerfTelecomInputClientPast24StatHistoryEsValuePort1 = _Pm10010mptPerfTelecomInputClientPast24StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 64, 1, 5),
    _Pm10010mptPerfTelecomInputClientPast24StatHistoryEsValuePort1_Type()
)
pm10010mptPerfTelecomInputClientPast24StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomInputClientPast24StatHistoryEsValuePort1.setStatus("current")
_Pm10010mptPerfTelecomInputClientPast24StatHistoryInvSesPort1_Type = EkiOnOff
_Pm10010mptPerfTelecomInputClientPast24StatHistoryInvSesPort1_Object = MibTableColumn
pm10010mptPerfTelecomInputClientPast24StatHistoryInvSesPort1 = _Pm10010mptPerfTelecomInputClientPast24StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 64, 1, 6),
    _Pm10010mptPerfTelecomInputClientPast24StatHistoryInvSesPort1_Type()
)
pm10010mptPerfTelecomInputClientPast24StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomInputClientPast24StatHistoryInvSesPort1.setStatus("current")
_Pm10010mptPerfTelecomInputClientPast24StatHistorySesValuePort1_Type = Unsigned32
_Pm10010mptPerfTelecomInputClientPast24StatHistorySesValuePort1_Object = MibTableColumn
pm10010mptPerfTelecomInputClientPast24StatHistorySesValuePort1 = _Pm10010mptPerfTelecomInputClientPast24StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 64, 1, 7),
    _Pm10010mptPerfTelecomInputClientPast24StatHistorySesValuePort1_Type()
)
pm10010mptPerfTelecomInputClientPast24StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomInputClientPast24StatHistorySesValuePort1.setStatus("current")
_Pm10010mptPerfTelecomInputClientPast24StatHistoryInvSefsPort1_Type = EkiOnOff
_Pm10010mptPerfTelecomInputClientPast24StatHistoryInvSefsPort1_Object = MibTableColumn
pm10010mptPerfTelecomInputClientPast24StatHistoryInvSefsPort1 = _Pm10010mptPerfTelecomInputClientPast24StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 64, 1, 8),
    _Pm10010mptPerfTelecomInputClientPast24StatHistoryInvSefsPort1_Type()
)
pm10010mptPerfTelecomInputClientPast24StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomInputClientPast24StatHistoryInvSefsPort1.setStatus("current")
_Pm10010mptPerfTelecomInputClientPast24StatHistorySefsValuePort1_Type = Unsigned32
_Pm10010mptPerfTelecomInputClientPast24StatHistorySefsValuePort1_Object = MibTableColumn
pm10010mptPerfTelecomInputClientPast24StatHistorySefsValuePort1 = _Pm10010mptPerfTelecomInputClientPast24StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 64, 1, 9),
    _Pm10010mptPerfTelecomInputClientPast24StatHistorySefsValuePort1_Type()
)
pm10010mptPerfTelecomInputClientPast24StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomInputClientPast24StatHistorySefsValuePort1.setStatus("current")
_Pm10010mptPerfTelecomInputClientPast24StatHistoryInvUasPort1_Type = EkiOnOff
_Pm10010mptPerfTelecomInputClientPast24StatHistoryInvUasPort1_Object = MibTableColumn
pm10010mptPerfTelecomInputClientPast24StatHistoryInvUasPort1 = _Pm10010mptPerfTelecomInputClientPast24StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 64, 1, 10),
    _Pm10010mptPerfTelecomInputClientPast24StatHistoryInvUasPort1_Type()
)
pm10010mptPerfTelecomInputClientPast24StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomInputClientPast24StatHistoryInvUasPort1.setStatus("current")
_Pm10010mptPerfTelecomInputClientPast24StatHistoryUasValuePort1_Type = Unsigned32
_Pm10010mptPerfTelecomInputClientPast24StatHistoryUasValuePort1_Object = MibTableColumn
pm10010mptPerfTelecomInputClientPast24StatHistoryUasValuePort1 = _Pm10010mptPerfTelecomInputClientPast24StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 64, 1, 11),
    _Pm10010mptPerfTelecomInputClientPast24StatHistoryUasValuePort1_Type()
)
pm10010mptPerfTelecomInputClientPast24StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomInputClientPast24StatHistoryUasValuePort1.setStatus("current")
_Pm10010mptPerfTelecomOutputClientCurrent15StatTable_Object = MibTable
pm10010mptPerfTelecomOutputClientCurrent15StatTable = _Pm10010mptPerfTelecomOutputClientCurrent15StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 80)
)
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomOutputClientCurrent15StatTable.setStatus("current")
_Pm10010mptPerfTelecomOutputClientCurrent15StatEntry_Object = MibTableRow
pm10010mptPerfTelecomOutputClientCurrent15StatEntry = _Pm10010mptPerfTelecomOutputClientCurrent15StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 80, 1)
)
pm10010mptPerfTelecomOutputClientCurrent15StatEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptPerfTelecomOutputClientCurrent15StatIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomOutputClientCurrent15StatEntry.setStatus("current")


class _Pm10010mptPerfTelecomOutputClientCurrent15StatIndex_Type(Integer32):
    """Custom type pm10010mptPerfTelecomOutputClientCurrent15StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptPerfTelecomOutputClientCurrent15StatIndex_Type.__name__ = "Integer32"
_Pm10010mptPerfTelecomOutputClientCurrent15StatIndex_Object = MibTableColumn
pm10010mptPerfTelecomOutputClientCurrent15StatIndex = _Pm10010mptPerfTelecomOutputClientCurrent15StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 80, 1, 1),
    _Pm10010mptPerfTelecomOutputClientCurrent15StatIndex_Type()
)
pm10010mptPerfTelecomOutputClientCurrent15StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomOutputClientCurrent15StatIndex.setStatus("current")
_Pm10010mptPerfTelecomOutputClientCurrent15StatInvCvPortn_Type = EkiOnOff
_Pm10010mptPerfTelecomOutputClientCurrent15StatInvCvPortn_Object = MibTableColumn
pm10010mptPerfTelecomOutputClientCurrent15StatInvCvPortn = _Pm10010mptPerfTelecomOutputClientCurrent15StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 80, 1, 2),
    _Pm10010mptPerfTelecomOutputClientCurrent15StatInvCvPortn_Type()
)
pm10010mptPerfTelecomOutputClientCurrent15StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomOutputClientCurrent15StatInvCvPortn.setStatus("current")
_Pm10010mptPerfTelecomOutputClientCurrent15StatCvValuePortn_Type = Unsigned32
_Pm10010mptPerfTelecomOutputClientCurrent15StatCvValuePortn_Object = MibTableColumn
pm10010mptPerfTelecomOutputClientCurrent15StatCvValuePortn = _Pm10010mptPerfTelecomOutputClientCurrent15StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 80, 1, 3),
    _Pm10010mptPerfTelecomOutputClientCurrent15StatCvValuePortn_Type()
)
pm10010mptPerfTelecomOutputClientCurrent15StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomOutputClientCurrent15StatCvValuePortn.setStatus("current")
_Pm10010mptPerfTelecomOutputClientCurrent15StatInvEsPortn_Type = EkiOnOff
_Pm10010mptPerfTelecomOutputClientCurrent15StatInvEsPortn_Object = MibTableColumn
pm10010mptPerfTelecomOutputClientCurrent15StatInvEsPortn = _Pm10010mptPerfTelecomOutputClientCurrent15StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 80, 1, 4),
    _Pm10010mptPerfTelecomOutputClientCurrent15StatInvEsPortn_Type()
)
pm10010mptPerfTelecomOutputClientCurrent15StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomOutputClientCurrent15StatInvEsPortn.setStatus("current")
_Pm10010mptPerfTelecomOutputClientCurrent15StatEsValuePortn_Type = Unsigned32
_Pm10010mptPerfTelecomOutputClientCurrent15StatEsValuePortn_Object = MibTableColumn
pm10010mptPerfTelecomOutputClientCurrent15StatEsValuePortn = _Pm10010mptPerfTelecomOutputClientCurrent15StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 80, 1, 5),
    _Pm10010mptPerfTelecomOutputClientCurrent15StatEsValuePortn_Type()
)
pm10010mptPerfTelecomOutputClientCurrent15StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomOutputClientCurrent15StatEsValuePortn.setStatus("current")
_Pm10010mptPerfTelecomOutputClientCurrent15StatInvSesPortn_Type = EkiOnOff
_Pm10010mptPerfTelecomOutputClientCurrent15StatInvSesPortn_Object = MibTableColumn
pm10010mptPerfTelecomOutputClientCurrent15StatInvSesPortn = _Pm10010mptPerfTelecomOutputClientCurrent15StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 80, 1, 6),
    _Pm10010mptPerfTelecomOutputClientCurrent15StatInvSesPortn_Type()
)
pm10010mptPerfTelecomOutputClientCurrent15StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomOutputClientCurrent15StatInvSesPortn.setStatus("current")
_Pm10010mptPerfTelecomOutputClientCurrent15StatSesValuePortn_Type = Unsigned32
_Pm10010mptPerfTelecomOutputClientCurrent15StatSesValuePortn_Object = MibTableColumn
pm10010mptPerfTelecomOutputClientCurrent15StatSesValuePortn = _Pm10010mptPerfTelecomOutputClientCurrent15StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 80, 1, 7),
    _Pm10010mptPerfTelecomOutputClientCurrent15StatSesValuePortn_Type()
)
pm10010mptPerfTelecomOutputClientCurrent15StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomOutputClientCurrent15StatSesValuePortn.setStatus("current")
_Pm10010mptPerfTelecomOutputClientCurrent15StatInvSefsPortn_Type = EkiOnOff
_Pm10010mptPerfTelecomOutputClientCurrent15StatInvSefsPortn_Object = MibTableColumn
pm10010mptPerfTelecomOutputClientCurrent15StatInvSefsPortn = _Pm10010mptPerfTelecomOutputClientCurrent15StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 80, 1, 8),
    _Pm10010mptPerfTelecomOutputClientCurrent15StatInvSefsPortn_Type()
)
pm10010mptPerfTelecomOutputClientCurrent15StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomOutputClientCurrent15StatInvSefsPortn.setStatus("current")
_Pm10010mptPerfTelecomOutputClientCurrent15StatSefsValuePortn_Type = Unsigned32
_Pm10010mptPerfTelecomOutputClientCurrent15StatSefsValuePortn_Object = MibTableColumn
pm10010mptPerfTelecomOutputClientCurrent15StatSefsValuePortn = _Pm10010mptPerfTelecomOutputClientCurrent15StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 80, 1, 9),
    _Pm10010mptPerfTelecomOutputClientCurrent15StatSefsValuePortn_Type()
)
pm10010mptPerfTelecomOutputClientCurrent15StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomOutputClientCurrent15StatSefsValuePortn.setStatus("current")
_Pm10010mptPerfTelecomOutputClientCurrent15StatInvUasPortn_Type = EkiOnOff
_Pm10010mptPerfTelecomOutputClientCurrent15StatInvUasPortn_Object = MibTableColumn
pm10010mptPerfTelecomOutputClientCurrent15StatInvUasPortn = _Pm10010mptPerfTelecomOutputClientCurrent15StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 80, 1, 10),
    _Pm10010mptPerfTelecomOutputClientCurrent15StatInvUasPortn_Type()
)
pm10010mptPerfTelecomOutputClientCurrent15StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomOutputClientCurrent15StatInvUasPortn.setStatus("current")
_Pm10010mptPerfTelecomOutputClientCurrent15StatUasValuePortn_Type = Unsigned32
_Pm10010mptPerfTelecomOutputClientCurrent15StatUasValuePortn_Object = MibTableColumn
pm10010mptPerfTelecomOutputClientCurrent15StatUasValuePortn = _Pm10010mptPerfTelecomOutputClientCurrent15StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 80, 1, 11),
    _Pm10010mptPerfTelecomOutputClientCurrent15StatUasValuePortn_Type()
)
pm10010mptPerfTelecomOutputClientCurrent15StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomOutputClientCurrent15StatUasValuePortn.setStatus("current")
_Pm10010mptPerfTelecomOutputClientPast15StatHistoryPort1Table_Object = MibTable
pm10010mptPerfTelecomOutputClientPast15StatHistoryPort1Table = _Pm10010mptPerfTelecomOutputClientPast15StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 96)
)
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomOutputClientPast15StatHistoryPort1Table.setStatus("current")
_Pm10010mptPerfTelecomOutputClientPast15StatHistoryPort1Entry_Object = MibTableRow
pm10010mptPerfTelecomOutputClientPast15StatHistoryPort1Entry = _Pm10010mptPerfTelecomOutputClientPast15StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 96, 1)
)
pm10010mptPerfTelecomOutputClientPast15StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptPerfTelecomOutputClientPast15StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomOutputClientPast15StatHistoryPort1Entry.setStatus("current")


class _Pm10010mptPerfTelecomOutputClientPast15StatHistoryPort1Index_Type(Integer32):
    """Custom type pm10010mptPerfTelecomOutputClientPast15StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptPerfTelecomOutputClientPast15StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm10010mptPerfTelecomOutputClientPast15StatHistoryPort1Index_Object = MibTableColumn
pm10010mptPerfTelecomOutputClientPast15StatHistoryPort1Index = _Pm10010mptPerfTelecomOutputClientPast15StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 96, 1, 1),
    _Pm10010mptPerfTelecomOutputClientPast15StatHistoryPort1Index_Type()
)
pm10010mptPerfTelecomOutputClientPast15StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomOutputClientPast15StatHistoryPort1Index.setStatus("current")
_Pm10010mptPerfTelecomOutputClientPast15StatHistoryInvCvPort1_Type = EkiOnOff
_Pm10010mptPerfTelecomOutputClientPast15StatHistoryInvCvPort1_Object = MibTableColumn
pm10010mptPerfTelecomOutputClientPast15StatHistoryInvCvPort1 = _Pm10010mptPerfTelecomOutputClientPast15StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 96, 1, 2),
    _Pm10010mptPerfTelecomOutputClientPast15StatHistoryInvCvPort1_Type()
)
pm10010mptPerfTelecomOutputClientPast15StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomOutputClientPast15StatHistoryInvCvPort1.setStatus("current")
_Pm10010mptPerfTelecomOutputClientPast15StatHistoryCvValuePort1_Type = Unsigned32
_Pm10010mptPerfTelecomOutputClientPast15StatHistoryCvValuePort1_Object = MibTableColumn
pm10010mptPerfTelecomOutputClientPast15StatHistoryCvValuePort1 = _Pm10010mptPerfTelecomOutputClientPast15StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 96, 1, 3),
    _Pm10010mptPerfTelecomOutputClientPast15StatHistoryCvValuePort1_Type()
)
pm10010mptPerfTelecomOutputClientPast15StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomOutputClientPast15StatHistoryCvValuePort1.setStatus("current")
_Pm10010mptPerfTelecomOutputClientPast15StatHistoryInvEsPort1_Type = EkiOnOff
_Pm10010mptPerfTelecomOutputClientPast15StatHistoryInvEsPort1_Object = MibTableColumn
pm10010mptPerfTelecomOutputClientPast15StatHistoryInvEsPort1 = _Pm10010mptPerfTelecomOutputClientPast15StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 96, 1, 4),
    _Pm10010mptPerfTelecomOutputClientPast15StatHistoryInvEsPort1_Type()
)
pm10010mptPerfTelecomOutputClientPast15StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomOutputClientPast15StatHistoryInvEsPort1.setStatus("current")
_Pm10010mptPerfTelecomOutputClientPast15StatHistoryEsValuePort1_Type = Unsigned32
_Pm10010mptPerfTelecomOutputClientPast15StatHistoryEsValuePort1_Object = MibTableColumn
pm10010mptPerfTelecomOutputClientPast15StatHistoryEsValuePort1 = _Pm10010mptPerfTelecomOutputClientPast15StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 96, 1, 5),
    _Pm10010mptPerfTelecomOutputClientPast15StatHistoryEsValuePort1_Type()
)
pm10010mptPerfTelecomOutputClientPast15StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomOutputClientPast15StatHistoryEsValuePort1.setStatus("current")
_Pm10010mptPerfTelecomOutputClientPast15StatHistoryInvSesPort1_Type = EkiOnOff
_Pm10010mptPerfTelecomOutputClientPast15StatHistoryInvSesPort1_Object = MibTableColumn
pm10010mptPerfTelecomOutputClientPast15StatHistoryInvSesPort1 = _Pm10010mptPerfTelecomOutputClientPast15StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 96, 1, 6),
    _Pm10010mptPerfTelecomOutputClientPast15StatHistoryInvSesPort1_Type()
)
pm10010mptPerfTelecomOutputClientPast15StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomOutputClientPast15StatHistoryInvSesPort1.setStatus("current")
_Pm10010mptPerfTelecomOutputClientPast15StatHistorySesValuePort1_Type = Unsigned32
_Pm10010mptPerfTelecomOutputClientPast15StatHistorySesValuePort1_Object = MibTableColumn
pm10010mptPerfTelecomOutputClientPast15StatHistorySesValuePort1 = _Pm10010mptPerfTelecomOutputClientPast15StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 96, 1, 7),
    _Pm10010mptPerfTelecomOutputClientPast15StatHistorySesValuePort1_Type()
)
pm10010mptPerfTelecomOutputClientPast15StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomOutputClientPast15StatHistorySesValuePort1.setStatus("current")
_Pm10010mptPerfTelecomOutputClientPast15StatHistoryInvSefsPort1_Type = EkiOnOff
_Pm10010mptPerfTelecomOutputClientPast15StatHistoryInvSefsPort1_Object = MibTableColumn
pm10010mptPerfTelecomOutputClientPast15StatHistoryInvSefsPort1 = _Pm10010mptPerfTelecomOutputClientPast15StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 96, 1, 8),
    _Pm10010mptPerfTelecomOutputClientPast15StatHistoryInvSefsPort1_Type()
)
pm10010mptPerfTelecomOutputClientPast15StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomOutputClientPast15StatHistoryInvSefsPort1.setStatus("current")
_Pm10010mptPerfTelecomOutputClientPast15StatHistorySefsValuePort1_Type = Unsigned32
_Pm10010mptPerfTelecomOutputClientPast15StatHistorySefsValuePort1_Object = MibTableColumn
pm10010mptPerfTelecomOutputClientPast15StatHistorySefsValuePort1 = _Pm10010mptPerfTelecomOutputClientPast15StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 96, 1, 9),
    _Pm10010mptPerfTelecomOutputClientPast15StatHistorySefsValuePort1_Type()
)
pm10010mptPerfTelecomOutputClientPast15StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomOutputClientPast15StatHistorySefsValuePort1.setStatus("current")
_Pm10010mptPerfTelecomOutputClientPast15StatHistoryInvUasPort1_Type = EkiOnOff
_Pm10010mptPerfTelecomOutputClientPast15StatHistoryInvUasPort1_Object = MibTableColumn
pm10010mptPerfTelecomOutputClientPast15StatHistoryInvUasPort1 = _Pm10010mptPerfTelecomOutputClientPast15StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 96, 1, 10),
    _Pm10010mptPerfTelecomOutputClientPast15StatHistoryInvUasPort1_Type()
)
pm10010mptPerfTelecomOutputClientPast15StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomOutputClientPast15StatHistoryInvUasPort1.setStatus("current")
_Pm10010mptPerfTelecomOutputClientPast15StatHistoryUasValuePort1_Type = Unsigned32
_Pm10010mptPerfTelecomOutputClientPast15StatHistoryUasValuePort1_Object = MibTableColumn
pm10010mptPerfTelecomOutputClientPast15StatHistoryUasValuePort1 = _Pm10010mptPerfTelecomOutputClientPast15StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 96, 1, 11),
    _Pm10010mptPerfTelecomOutputClientPast15StatHistoryUasValuePort1_Type()
)
pm10010mptPerfTelecomOutputClientPast15StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomOutputClientPast15StatHistoryUasValuePort1.setStatus("current")
_Pm10010mptPerfTelecomOutputClientCurrent24StatTable_Object = MibTable
pm10010mptPerfTelecomOutputClientCurrent24StatTable = _Pm10010mptPerfTelecomOutputClientCurrent24StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 112)
)
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomOutputClientCurrent24StatTable.setStatus("current")
_Pm10010mptPerfTelecomOutputClientCurrent24StatEntry_Object = MibTableRow
pm10010mptPerfTelecomOutputClientCurrent24StatEntry = _Pm10010mptPerfTelecomOutputClientCurrent24StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 112, 1)
)
pm10010mptPerfTelecomOutputClientCurrent24StatEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptPerfTelecomOutputClientCurrent24StatIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomOutputClientCurrent24StatEntry.setStatus("current")


class _Pm10010mptPerfTelecomOutputClientCurrent24StatIndex_Type(Integer32):
    """Custom type pm10010mptPerfTelecomOutputClientCurrent24StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptPerfTelecomOutputClientCurrent24StatIndex_Type.__name__ = "Integer32"
_Pm10010mptPerfTelecomOutputClientCurrent24StatIndex_Object = MibTableColumn
pm10010mptPerfTelecomOutputClientCurrent24StatIndex = _Pm10010mptPerfTelecomOutputClientCurrent24StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 112, 1, 1),
    _Pm10010mptPerfTelecomOutputClientCurrent24StatIndex_Type()
)
pm10010mptPerfTelecomOutputClientCurrent24StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomOutputClientCurrent24StatIndex.setStatus("current")
_Pm10010mptPerfTelecomOutputClientCurrent24StatInvCvPortn_Type = EkiOnOff
_Pm10010mptPerfTelecomOutputClientCurrent24StatInvCvPortn_Object = MibTableColumn
pm10010mptPerfTelecomOutputClientCurrent24StatInvCvPortn = _Pm10010mptPerfTelecomOutputClientCurrent24StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 112, 1, 2),
    _Pm10010mptPerfTelecomOutputClientCurrent24StatInvCvPortn_Type()
)
pm10010mptPerfTelecomOutputClientCurrent24StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomOutputClientCurrent24StatInvCvPortn.setStatus("current")
_Pm10010mptPerfTelecomOutputClientCurrent24StatCvValuePortn_Type = Unsigned32
_Pm10010mptPerfTelecomOutputClientCurrent24StatCvValuePortn_Object = MibTableColumn
pm10010mptPerfTelecomOutputClientCurrent24StatCvValuePortn = _Pm10010mptPerfTelecomOutputClientCurrent24StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 112, 1, 3),
    _Pm10010mptPerfTelecomOutputClientCurrent24StatCvValuePortn_Type()
)
pm10010mptPerfTelecomOutputClientCurrent24StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomOutputClientCurrent24StatCvValuePortn.setStatus("current")
_Pm10010mptPerfTelecomOutputClientCurrent24StatInvEsPortn_Type = EkiOnOff
_Pm10010mptPerfTelecomOutputClientCurrent24StatInvEsPortn_Object = MibTableColumn
pm10010mptPerfTelecomOutputClientCurrent24StatInvEsPortn = _Pm10010mptPerfTelecomOutputClientCurrent24StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 112, 1, 4),
    _Pm10010mptPerfTelecomOutputClientCurrent24StatInvEsPortn_Type()
)
pm10010mptPerfTelecomOutputClientCurrent24StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomOutputClientCurrent24StatInvEsPortn.setStatus("current")
_Pm10010mptPerfTelecomOutputClientCurrent24StatEsValuePortn_Type = Unsigned32
_Pm10010mptPerfTelecomOutputClientCurrent24StatEsValuePortn_Object = MibTableColumn
pm10010mptPerfTelecomOutputClientCurrent24StatEsValuePortn = _Pm10010mptPerfTelecomOutputClientCurrent24StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 112, 1, 5),
    _Pm10010mptPerfTelecomOutputClientCurrent24StatEsValuePortn_Type()
)
pm10010mptPerfTelecomOutputClientCurrent24StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomOutputClientCurrent24StatEsValuePortn.setStatus("current")
_Pm10010mptPerfTelecomOutputClientCurrent24StatInvSesPortn_Type = EkiOnOff
_Pm10010mptPerfTelecomOutputClientCurrent24StatInvSesPortn_Object = MibTableColumn
pm10010mptPerfTelecomOutputClientCurrent24StatInvSesPortn = _Pm10010mptPerfTelecomOutputClientCurrent24StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 112, 1, 6),
    _Pm10010mptPerfTelecomOutputClientCurrent24StatInvSesPortn_Type()
)
pm10010mptPerfTelecomOutputClientCurrent24StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomOutputClientCurrent24StatInvSesPortn.setStatus("current")
_Pm10010mptPerfTelecomOutputClientCurrent24StatSesValuePortn_Type = Unsigned32
_Pm10010mptPerfTelecomOutputClientCurrent24StatSesValuePortn_Object = MibTableColumn
pm10010mptPerfTelecomOutputClientCurrent24StatSesValuePortn = _Pm10010mptPerfTelecomOutputClientCurrent24StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 112, 1, 7),
    _Pm10010mptPerfTelecomOutputClientCurrent24StatSesValuePortn_Type()
)
pm10010mptPerfTelecomOutputClientCurrent24StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomOutputClientCurrent24StatSesValuePortn.setStatus("current")
_Pm10010mptPerfTelecomOutputClientCurrent24StatInvSefsPortn_Type = EkiOnOff
_Pm10010mptPerfTelecomOutputClientCurrent24StatInvSefsPortn_Object = MibTableColumn
pm10010mptPerfTelecomOutputClientCurrent24StatInvSefsPortn = _Pm10010mptPerfTelecomOutputClientCurrent24StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 112, 1, 8),
    _Pm10010mptPerfTelecomOutputClientCurrent24StatInvSefsPortn_Type()
)
pm10010mptPerfTelecomOutputClientCurrent24StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomOutputClientCurrent24StatInvSefsPortn.setStatus("current")
_Pm10010mptPerfTelecomOutputClientCurrent24StatSefsValuePortn_Type = Unsigned32
_Pm10010mptPerfTelecomOutputClientCurrent24StatSefsValuePortn_Object = MibTableColumn
pm10010mptPerfTelecomOutputClientCurrent24StatSefsValuePortn = _Pm10010mptPerfTelecomOutputClientCurrent24StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 112, 1, 9),
    _Pm10010mptPerfTelecomOutputClientCurrent24StatSefsValuePortn_Type()
)
pm10010mptPerfTelecomOutputClientCurrent24StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomOutputClientCurrent24StatSefsValuePortn.setStatus("current")
_Pm10010mptPerfTelecomOutputClientCurrent24StatInvUasPortn_Type = EkiOnOff
_Pm10010mptPerfTelecomOutputClientCurrent24StatInvUasPortn_Object = MibTableColumn
pm10010mptPerfTelecomOutputClientCurrent24StatInvUasPortn = _Pm10010mptPerfTelecomOutputClientCurrent24StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 112, 1, 10),
    _Pm10010mptPerfTelecomOutputClientCurrent24StatInvUasPortn_Type()
)
pm10010mptPerfTelecomOutputClientCurrent24StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomOutputClientCurrent24StatInvUasPortn.setStatus("current")
_Pm10010mptPerfTelecomOutputClientCurrent24StatUasValuePortn_Type = Unsigned32
_Pm10010mptPerfTelecomOutputClientCurrent24StatUasValuePortn_Object = MibTableColumn
pm10010mptPerfTelecomOutputClientCurrent24StatUasValuePortn = _Pm10010mptPerfTelecomOutputClientCurrent24StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 112, 1, 11),
    _Pm10010mptPerfTelecomOutputClientCurrent24StatUasValuePortn_Type()
)
pm10010mptPerfTelecomOutputClientCurrent24StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomOutputClientCurrent24StatUasValuePortn.setStatus("current")
_Pm10010mptPerfTelecomOutputClientPast24StatHistoryPort1Table_Object = MibTable
pm10010mptPerfTelecomOutputClientPast24StatHistoryPort1Table = _Pm10010mptPerfTelecomOutputClientPast24StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 128)
)
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomOutputClientPast24StatHistoryPort1Table.setStatus("current")
_Pm10010mptPerfTelecomOutputClientPast24StatHistoryPort1Entry_Object = MibTableRow
pm10010mptPerfTelecomOutputClientPast24StatHistoryPort1Entry = _Pm10010mptPerfTelecomOutputClientPast24StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 128, 1)
)
pm10010mptPerfTelecomOutputClientPast24StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptPerfTelecomOutputClientPast24StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomOutputClientPast24StatHistoryPort1Entry.setStatus("current")


class _Pm10010mptPerfTelecomOutputClientPast24StatHistoryPort1Index_Type(Integer32):
    """Custom type pm10010mptPerfTelecomOutputClientPast24StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptPerfTelecomOutputClientPast24StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm10010mptPerfTelecomOutputClientPast24StatHistoryPort1Index_Object = MibTableColumn
pm10010mptPerfTelecomOutputClientPast24StatHistoryPort1Index = _Pm10010mptPerfTelecomOutputClientPast24StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 128, 1, 1),
    _Pm10010mptPerfTelecomOutputClientPast24StatHistoryPort1Index_Type()
)
pm10010mptPerfTelecomOutputClientPast24StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomOutputClientPast24StatHistoryPort1Index.setStatus("current")
_Pm10010mptPerfTelecomOutputClientPast24StatHistoryInvCvPort1_Type = EkiOnOff
_Pm10010mptPerfTelecomOutputClientPast24StatHistoryInvCvPort1_Object = MibTableColumn
pm10010mptPerfTelecomOutputClientPast24StatHistoryInvCvPort1 = _Pm10010mptPerfTelecomOutputClientPast24StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 128, 1, 2),
    _Pm10010mptPerfTelecomOutputClientPast24StatHistoryInvCvPort1_Type()
)
pm10010mptPerfTelecomOutputClientPast24StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomOutputClientPast24StatHistoryInvCvPort1.setStatus("current")
_Pm10010mptPerfTelecomOutputClientPast24StatHistoryCvValuePort1_Type = Unsigned32
_Pm10010mptPerfTelecomOutputClientPast24StatHistoryCvValuePort1_Object = MibTableColumn
pm10010mptPerfTelecomOutputClientPast24StatHistoryCvValuePort1 = _Pm10010mptPerfTelecomOutputClientPast24StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 128, 1, 3),
    _Pm10010mptPerfTelecomOutputClientPast24StatHistoryCvValuePort1_Type()
)
pm10010mptPerfTelecomOutputClientPast24StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomOutputClientPast24StatHistoryCvValuePort1.setStatus("current")
_Pm10010mptPerfTelecomOutputClientPast24StatHistoryInvEsPort1_Type = EkiOnOff
_Pm10010mptPerfTelecomOutputClientPast24StatHistoryInvEsPort1_Object = MibTableColumn
pm10010mptPerfTelecomOutputClientPast24StatHistoryInvEsPort1 = _Pm10010mptPerfTelecomOutputClientPast24StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 128, 1, 4),
    _Pm10010mptPerfTelecomOutputClientPast24StatHistoryInvEsPort1_Type()
)
pm10010mptPerfTelecomOutputClientPast24StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomOutputClientPast24StatHistoryInvEsPort1.setStatus("current")
_Pm10010mptPerfTelecomOutputClientPast24StatHistoryEsValuePort1_Type = Unsigned32
_Pm10010mptPerfTelecomOutputClientPast24StatHistoryEsValuePort1_Object = MibTableColumn
pm10010mptPerfTelecomOutputClientPast24StatHistoryEsValuePort1 = _Pm10010mptPerfTelecomOutputClientPast24StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 128, 1, 5),
    _Pm10010mptPerfTelecomOutputClientPast24StatHistoryEsValuePort1_Type()
)
pm10010mptPerfTelecomOutputClientPast24StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomOutputClientPast24StatHistoryEsValuePort1.setStatus("current")
_Pm10010mptPerfTelecomOutputClientPast24StatHistoryInvSesPort1_Type = EkiOnOff
_Pm10010mptPerfTelecomOutputClientPast24StatHistoryInvSesPort1_Object = MibTableColumn
pm10010mptPerfTelecomOutputClientPast24StatHistoryInvSesPort1 = _Pm10010mptPerfTelecomOutputClientPast24StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 128, 1, 6),
    _Pm10010mptPerfTelecomOutputClientPast24StatHistoryInvSesPort1_Type()
)
pm10010mptPerfTelecomOutputClientPast24StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomOutputClientPast24StatHistoryInvSesPort1.setStatus("current")
_Pm10010mptPerfTelecomOutputClientPast24StatHistorySesValuePort1_Type = Unsigned32
_Pm10010mptPerfTelecomOutputClientPast24StatHistorySesValuePort1_Object = MibTableColumn
pm10010mptPerfTelecomOutputClientPast24StatHistorySesValuePort1 = _Pm10010mptPerfTelecomOutputClientPast24StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 128, 1, 7),
    _Pm10010mptPerfTelecomOutputClientPast24StatHistorySesValuePort1_Type()
)
pm10010mptPerfTelecomOutputClientPast24StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomOutputClientPast24StatHistorySesValuePort1.setStatus("current")
_Pm10010mptPerfTelecomOutputClientPast24StatHistoryInvSefsPort1_Type = EkiOnOff
_Pm10010mptPerfTelecomOutputClientPast24StatHistoryInvSefsPort1_Object = MibTableColumn
pm10010mptPerfTelecomOutputClientPast24StatHistoryInvSefsPort1 = _Pm10010mptPerfTelecomOutputClientPast24StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 128, 1, 8),
    _Pm10010mptPerfTelecomOutputClientPast24StatHistoryInvSefsPort1_Type()
)
pm10010mptPerfTelecomOutputClientPast24StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomOutputClientPast24StatHistoryInvSefsPort1.setStatus("current")
_Pm10010mptPerfTelecomOutputClientPast24StatHistorySefsValuePort1_Type = Unsigned32
_Pm10010mptPerfTelecomOutputClientPast24StatHistorySefsValuePort1_Object = MibTableColumn
pm10010mptPerfTelecomOutputClientPast24StatHistorySefsValuePort1 = _Pm10010mptPerfTelecomOutputClientPast24StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 128, 1, 9),
    _Pm10010mptPerfTelecomOutputClientPast24StatHistorySefsValuePort1_Type()
)
pm10010mptPerfTelecomOutputClientPast24StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomOutputClientPast24StatHistorySefsValuePort1.setStatus("current")
_Pm10010mptPerfTelecomOutputClientPast24StatHistoryInvUasPort1_Type = EkiOnOff
_Pm10010mptPerfTelecomOutputClientPast24StatHistoryInvUasPort1_Object = MibTableColumn
pm10010mptPerfTelecomOutputClientPast24StatHistoryInvUasPort1 = _Pm10010mptPerfTelecomOutputClientPast24StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 128, 1, 10),
    _Pm10010mptPerfTelecomOutputClientPast24StatHistoryInvUasPort1_Type()
)
pm10010mptPerfTelecomOutputClientPast24StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomOutputClientPast24StatHistoryInvUasPort1.setStatus("current")
_Pm10010mptPerfTelecomOutputClientPast24StatHistoryUasValuePort1_Type = Unsigned32
_Pm10010mptPerfTelecomOutputClientPast24StatHistoryUasValuePort1_Object = MibTableColumn
pm10010mptPerfTelecomOutputClientPast24StatHistoryUasValuePort1 = _Pm10010mptPerfTelecomOutputClientPast24StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 128, 1, 11),
    _Pm10010mptPerfTelecomOutputClientPast24StatHistoryUasValuePort1_Type()
)
pm10010mptPerfTelecomOutputClientPast24StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomOutputClientPast24StatHistoryUasValuePort1.setStatus("current")
_Pm10010mptPerfDatacomClientCurrent15StatTable_Object = MibTable
pm10010mptPerfDatacomClientCurrent15StatTable = _Pm10010mptPerfDatacomClientCurrent15StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 432)
)
if mibBuilder.loadTexts:
    pm10010mptPerfDatacomClientCurrent15StatTable.setStatus("current")
_Pm10010mptPerfDatacomClientCurrent15StatEntry_Object = MibTableRow
pm10010mptPerfDatacomClientCurrent15StatEntry = _Pm10010mptPerfDatacomClientCurrent15StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 432, 1)
)
pm10010mptPerfDatacomClientCurrent15StatEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptPerfDatacomClientCurrent15StatIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptPerfDatacomClientCurrent15StatEntry.setStatus("current")


class _Pm10010mptPerfDatacomClientCurrent15StatIndex_Type(Integer32):
    """Custom type pm10010mptPerfDatacomClientCurrent15StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptPerfDatacomClientCurrent15StatIndex_Type.__name__ = "Integer32"
_Pm10010mptPerfDatacomClientCurrent15StatIndex_Object = MibTableColumn
pm10010mptPerfDatacomClientCurrent15StatIndex = _Pm10010mptPerfDatacomClientCurrent15StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 432, 1, 1),
    _Pm10010mptPerfDatacomClientCurrent15StatIndex_Type()
)
pm10010mptPerfDatacomClientCurrent15StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfDatacomClientCurrent15StatIndex.setStatus("current")
_Rm10010perfdatacomclientCurrent15StatInCrcCountInvPortn_Type = EkiOnOff
_Rm10010perfdatacomclientCurrent15StatInCrcCountInvPortn_Object = MibTableColumn
rm10010perfdatacomclientCurrent15StatInCrcCountInvPortn = _Rm10010perfdatacomclientCurrent15StatInCrcCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 432, 1, 4),
    _Rm10010perfdatacomclientCurrent15StatInCrcCountInvPortn_Type()
)
rm10010perfdatacomclientCurrent15StatInCrcCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientCurrent15StatInCrcCountInvPortn.setStatus("current")
_Rm10010perfdatacomclientCurrent15StatInCrcCountPortn_Type = Counter64
_Rm10010perfdatacomclientCurrent15StatInCrcCountPortn_Object = MibTableColumn
rm10010perfdatacomclientCurrent15StatInCrcCountPortn = _Rm10010perfdatacomclientCurrent15StatInCrcCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 432, 1, 5),
    _Rm10010perfdatacomclientCurrent15StatInCrcCountPortn_Type()
)
rm10010perfdatacomclientCurrent15StatInCrcCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientCurrent15StatInCrcCountPortn.setStatus("current")
_Rm10010perfdatacomclientCurrent15StatInPacketCountInvPortn_Type = EkiOnOff
_Rm10010perfdatacomclientCurrent15StatInPacketCountInvPortn_Object = MibTableColumn
rm10010perfdatacomclientCurrent15StatInPacketCountInvPortn = _Rm10010perfdatacomclientCurrent15StatInPacketCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 432, 1, 6),
    _Rm10010perfdatacomclientCurrent15StatInPacketCountInvPortn_Type()
)
rm10010perfdatacomclientCurrent15StatInPacketCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientCurrent15StatInPacketCountInvPortn.setStatus("current")
_Rm10010perfdatacomclientCurrent15StatInPacketCountPortn_Type = Counter64
_Rm10010perfdatacomclientCurrent15StatInPacketCountPortn_Object = MibTableColumn
rm10010perfdatacomclientCurrent15StatInPacketCountPortn = _Rm10010perfdatacomclientCurrent15StatInPacketCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 432, 1, 7),
    _Rm10010perfdatacomclientCurrent15StatInPacketCountPortn_Type()
)
rm10010perfdatacomclientCurrent15StatInPacketCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientCurrent15StatInPacketCountPortn.setStatus("current")
_Rm10010perfdatacomclientCurrent15StatOutCrcCountInvPortn_Type = EkiOnOff
_Rm10010perfdatacomclientCurrent15StatOutCrcCountInvPortn_Object = MibTableColumn
rm10010perfdatacomclientCurrent15StatOutCrcCountInvPortn = _Rm10010perfdatacomclientCurrent15StatOutCrcCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 432, 1, 28),
    _Rm10010perfdatacomclientCurrent15StatOutCrcCountInvPortn_Type()
)
rm10010perfdatacomclientCurrent15StatOutCrcCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientCurrent15StatOutCrcCountInvPortn.setStatus("current")
_Rm10010perfdatacomclientCurrent15StatOutCrcCountPortn_Type = Counter64
_Rm10010perfdatacomclientCurrent15StatOutCrcCountPortn_Object = MibTableColumn
rm10010perfdatacomclientCurrent15StatOutCrcCountPortn = _Rm10010perfdatacomclientCurrent15StatOutCrcCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 432, 1, 29),
    _Rm10010perfdatacomclientCurrent15StatOutCrcCountPortn_Type()
)
rm10010perfdatacomclientCurrent15StatOutCrcCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientCurrent15StatOutCrcCountPortn.setStatus("current")
_Rm10010perfdatacomclientCurrent15StatOutPacketCountInvPortn_Type = EkiOnOff
_Rm10010perfdatacomclientCurrent15StatOutPacketCountInvPortn_Object = MibTableColumn
rm10010perfdatacomclientCurrent15StatOutPacketCountInvPortn = _Rm10010perfdatacomclientCurrent15StatOutPacketCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 432, 1, 30),
    _Rm10010perfdatacomclientCurrent15StatOutPacketCountInvPortn_Type()
)
rm10010perfdatacomclientCurrent15StatOutPacketCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientCurrent15StatOutPacketCountInvPortn.setStatus("current")
_Rm10010perfdatacomclientCurrent15StatOutPacketCountPortn_Type = Counter64
_Rm10010perfdatacomclientCurrent15StatOutPacketCountPortn_Object = MibTableColumn
rm10010perfdatacomclientCurrent15StatOutPacketCountPortn = _Rm10010perfdatacomclientCurrent15StatOutPacketCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 432, 1, 31),
    _Rm10010perfdatacomclientCurrent15StatOutPacketCountPortn_Type()
)
rm10010perfdatacomclientCurrent15StatOutPacketCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientCurrent15StatOutPacketCountPortn.setStatus("current")
_Pm10010mptPerfDatacomClientPast15StatHistoryPort1Table_Object = MibTable
pm10010mptPerfDatacomClientPast15StatHistoryPort1Table = _Pm10010mptPerfDatacomClientPast15StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 448)
)
if mibBuilder.loadTexts:
    pm10010mptPerfDatacomClientPast15StatHistoryPort1Table.setStatus("current")
_Pm10010mptPerfDatacomClientPast15StatHistoryPort1Entry_Object = MibTableRow
pm10010mptPerfDatacomClientPast15StatHistoryPort1Entry = _Pm10010mptPerfDatacomClientPast15StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 448, 1)
)
pm10010mptPerfDatacomClientPast15StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptPerfDatacomClientPast15StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm10010mptPerfDatacomClientPast15StatHistoryPort1Entry.setStatus("current")


class _Pm10010mptPerfDatacomClientPast15StatHistoryPort1Index_Type(Integer32):
    """Custom type pm10010mptPerfDatacomClientPast15StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptPerfDatacomClientPast15StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm10010mptPerfDatacomClientPast15StatHistoryPort1Index_Object = MibTableColumn
pm10010mptPerfDatacomClientPast15StatHistoryPort1Index = _Pm10010mptPerfDatacomClientPast15StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 448, 1, 1),
    _Pm10010mptPerfDatacomClientPast15StatHistoryPort1Index_Type()
)
pm10010mptPerfDatacomClientPast15StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfDatacomClientPast15StatHistoryPort1Index.setStatus("current")
_Rm10010perfdatacomclientPast15StatInCrcCountInvPort1_Type = EkiOnOff
_Rm10010perfdatacomclientPast15StatInCrcCountInvPort1_Object = MibTableColumn
rm10010perfdatacomclientPast15StatInCrcCountInvPort1 = _Rm10010perfdatacomclientPast15StatInCrcCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 448, 1, 4),
    _Rm10010perfdatacomclientPast15StatInCrcCountInvPort1_Type()
)
rm10010perfdatacomclientPast15StatInCrcCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientPast15StatInCrcCountInvPort1.setStatus("current")
_Rm10010perfdatacomclientPast15StatInCrcCountPort1_Type = Counter64
_Rm10010perfdatacomclientPast15StatInCrcCountPort1_Object = MibTableColumn
rm10010perfdatacomclientPast15StatInCrcCountPort1 = _Rm10010perfdatacomclientPast15StatInCrcCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 448, 1, 5),
    _Rm10010perfdatacomclientPast15StatInCrcCountPort1_Type()
)
rm10010perfdatacomclientPast15StatInCrcCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientPast15StatInCrcCountPort1.setStatus("current")
_Rm10010perfdatacomclientPast15StatInPacketCountInvPort1_Type = EkiOnOff
_Rm10010perfdatacomclientPast15StatInPacketCountInvPort1_Object = MibTableColumn
rm10010perfdatacomclientPast15StatInPacketCountInvPort1 = _Rm10010perfdatacomclientPast15StatInPacketCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 448, 1, 6),
    _Rm10010perfdatacomclientPast15StatInPacketCountInvPort1_Type()
)
rm10010perfdatacomclientPast15StatInPacketCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientPast15StatInPacketCountInvPort1.setStatus("current")
_Rm10010perfdatacomclientPast15StatInPacketCountPort1_Type = Counter64
_Rm10010perfdatacomclientPast15StatInPacketCountPort1_Object = MibTableColumn
rm10010perfdatacomclientPast15StatInPacketCountPort1 = _Rm10010perfdatacomclientPast15StatInPacketCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 448, 1, 7),
    _Rm10010perfdatacomclientPast15StatInPacketCountPort1_Type()
)
rm10010perfdatacomclientPast15StatInPacketCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientPast15StatInPacketCountPort1.setStatus("current")
_Rm10010perfdatacomclientPast15StatOutCrcCountInvPort1_Type = EkiOnOff
_Rm10010perfdatacomclientPast15StatOutCrcCountInvPort1_Object = MibTableColumn
rm10010perfdatacomclientPast15StatOutCrcCountInvPort1 = _Rm10010perfdatacomclientPast15StatOutCrcCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 448, 1, 28),
    _Rm10010perfdatacomclientPast15StatOutCrcCountInvPort1_Type()
)
rm10010perfdatacomclientPast15StatOutCrcCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientPast15StatOutCrcCountInvPort1.setStatus("current")
_Rm10010perfdatacomclientPast15StatOutCrcCountPort1_Type = Counter64
_Rm10010perfdatacomclientPast15StatOutCrcCountPort1_Object = MibTableColumn
rm10010perfdatacomclientPast15StatOutCrcCountPort1 = _Rm10010perfdatacomclientPast15StatOutCrcCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 448, 1, 29),
    _Rm10010perfdatacomclientPast15StatOutCrcCountPort1_Type()
)
rm10010perfdatacomclientPast15StatOutCrcCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientPast15StatOutCrcCountPort1.setStatus("current")
_Rm10010perfdatacomclientPast15StatOutPacketCountInvPort1_Type = EkiOnOff
_Rm10010perfdatacomclientPast15StatOutPacketCountInvPort1_Object = MibTableColumn
rm10010perfdatacomclientPast15StatOutPacketCountInvPort1 = _Rm10010perfdatacomclientPast15StatOutPacketCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 448, 1, 30),
    _Rm10010perfdatacomclientPast15StatOutPacketCountInvPort1_Type()
)
rm10010perfdatacomclientPast15StatOutPacketCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientPast15StatOutPacketCountInvPort1.setStatus("current")
_Rm10010perfdatacomclientPast15StatOutPacketCountPort1_Type = Counter64
_Rm10010perfdatacomclientPast15StatOutPacketCountPort1_Object = MibTableColumn
rm10010perfdatacomclientPast15StatOutPacketCountPort1 = _Rm10010perfdatacomclientPast15StatOutPacketCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 448, 1, 31),
    _Rm10010perfdatacomclientPast15StatOutPacketCountPort1_Type()
)
rm10010perfdatacomclientPast15StatOutPacketCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientPast15StatOutPacketCountPort1.setStatus("current")
_Pm10010mptPerfDatacomClientCurrent24StatTable_Object = MibTable
pm10010mptPerfDatacomClientCurrent24StatTable = _Pm10010mptPerfDatacomClientCurrent24StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 464)
)
if mibBuilder.loadTexts:
    pm10010mptPerfDatacomClientCurrent24StatTable.setStatus("current")
_Pm10010mptPerfDatacomClientCurrent24StatEntry_Object = MibTableRow
pm10010mptPerfDatacomClientCurrent24StatEntry = _Pm10010mptPerfDatacomClientCurrent24StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 464, 1)
)
pm10010mptPerfDatacomClientCurrent24StatEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptPerfDatacomClientCurrent24StatIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptPerfDatacomClientCurrent24StatEntry.setStatus("current")


class _Pm10010mptPerfDatacomClientCurrent24StatIndex_Type(Integer32):
    """Custom type pm10010mptPerfDatacomClientCurrent24StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptPerfDatacomClientCurrent24StatIndex_Type.__name__ = "Integer32"
_Pm10010mptPerfDatacomClientCurrent24StatIndex_Object = MibTableColumn
pm10010mptPerfDatacomClientCurrent24StatIndex = _Pm10010mptPerfDatacomClientCurrent24StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 464, 1, 1),
    _Pm10010mptPerfDatacomClientCurrent24StatIndex_Type()
)
pm10010mptPerfDatacomClientCurrent24StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfDatacomClientCurrent24StatIndex.setStatus("current")
_Rm10010perfdatacomclientCurrent24StatInCrcCountInvPortn_Type = EkiOnOff
_Rm10010perfdatacomclientCurrent24StatInCrcCountInvPortn_Object = MibTableColumn
rm10010perfdatacomclientCurrent24StatInCrcCountInvPortn = _Rm10010perfdatacomclientCurrent24StatInCrcCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 464, 1, 4),
    _Rm10010perfdatacomclientCurrent24StatInCrcCountInvPortn_Type()
)
rm10010perfdatacomclientCurrent24StatInCrcCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientCurrent24StatInCrcCountInvPortn.setStatus("current")
_Rm10010perfdatacomclientCurrent24StatInCrcCountPortn_Type = Counter64
_Rm10010perfdatacomclientCurrent24StatInCrcCountPortn_Object = MibTableColumn
rm10010perfdatacomclientCurrent24StatInCrcCountPortn = _Rm10010perfdatacomclientCurrent24StatInCrcCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 464, 1, 5),
    _Rm10010perfdatacomclientCurrent24StatInCrcCountPortn_Type()
)
rm10010perfdatacomclientCurrent24StatInCrcCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientCurrent24StatInCrcCountPortn.setStatus("current")
_Rm10010perfdatacomclientCurrent24StatInPacketCountInvPortn_Type = EkiOnOff
_Rm10010perfdatacomclientCurrent24StatInPacketCountInvPortn_Object = MibTableColumn
rm10010perfdatacomclientCurrent24StatInPacketCountInvPortn = _Rm10010perfdatacomclientCurrent24StatInPacketCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 464, 1, 6),
    _Rm10010perfdatacomclientCurrent24StatInPacketCountInvPortn_Type()
)
rm10010perfdatacomclientCurrent24StatInPacketCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientCurrent24StatInPacketCountInvPortn.setStatus("current")
_Rm10010perfdatacomclientCurrent24StatInPacketCountPortn_Type = Counter64
_Rm10010perfdatacomclientCurrent24StatInPacketCountPortn_Object = MibTableColumn
rm10010perfdatacomclientCurrent24StatInPacketCountPortn = _Rm10010perfdatacomclientCurrent24StatInPacketCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 464, 1, 7),
    _Rm10010perfdatacomclientCurrent24StatInPacketCountPortn_Type()
)
rm10010perfdatacomclientCurrent24StatInPacketCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientCurrent24StatInPacketCountPortn.setStatus("current")
_Rm10010perfdatacomclientCurrent24StatOutCrcCountInvPortn_Type = EkiOnOff
_Rm10010perfdatacomclientCurrent24StatOutCrcCountInvPortn_Object = MibTableColumn
rm10010perfdatacomclientCurrent24StatOutCrcCountInvPortn = _Rm10010perfdatacomclientCurrent24StatOutCrcCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 464, 1, 28),
    _Rm10010perfdatacomclientCurrent24StatOutCrcCountInvPortn_Type()
)
rm10010perfdatacomclientCurrent24StatOutCrcCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientCurrent24StatOutCrcCountInvPortn.setStatus("current")
_Rm10010perfdatacomclientCurrent24StatOutCrcCountPortn_Type = Counter64
_Rm10010perfdatacomclientCurrent24StatOutCrcCountPortn_Object = MibTableColumn
rm10010perfdatacomclientCurrent24StatOutCrcCountPortn = _Rm10010perfdatacomclientCurrent24StatOutCrcCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 464, 1, 29),
    _Rm10010perfdatacomclientCurrent24StatOutCrcCountPortn_Type()
)
rm10010perfdatacomclientCurrent24StatOutCrcCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientCurrent24StatOutCrcCountPortn.setStatus("current")
_Rm10010perfdatacomclientCurrent24StatOutPacketCountInvPortn_Type = EkiOnOff
_Rm10010perfdatacomclientCurrent24StatOutPacketCountInvPortn_Object = MibTableColumn
rm10010perfdatacomclientCurrent24StatOutPacketCountInvPortn = _Rm10010perfdatacomclientCurrent24StatOutPacketCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 464, 1, 30),
    _Rm10010perfdatacomclientCurrent24StatOutPacketCountInvPortn_Type()
)
rm10010perfdatacomclientCurrent24StatOutPacketCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientCurrent24StatOutPacketCountInvPortn.setStatus("current")
_Rm10010perfdatacomclientCurrent24StatOutPacketCountPortn_Type = Counter64
_Rm10010perfdatacomclientCurrent24StatOutPacketCountPortn_Object = MibTableColumn
rm10010perfdatacomclientCurrent24StatOutPacketCountPortn = _Rm10010perfdatacomclientCurrent24StatOutPacketCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 464, 1, 31),
    _Rm10010perfdatacomclientCurrent24StatOutPacketCountPortn_Type()
)
rm10010perfdatacomclientCurrent24StatOutPacketCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientCurrent24StatOutPacketCountPortn.setStatus("current")
_Pm10010mptPerfDatacomClientPast24StatHistoryPort1Table_Object = MibTable
pm10010mptPerfDatacomClientPast24StatHistoryPort1Table = _Pm10010mptPerfDatacomClientPast24StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 480)
)
if mibBuilder.loadTexts:
    pm10010mptPerfDatacomClientPast24StatHistoryPort1Table.setStatus("current")
_Pm10010mptPerfDatacomClientPast24StatHistoryPort1Entry_Object = MibTableRow
pm10010mptPerfDatacomClientPast24StatHistoryPort1Entry = _Pm10010mptPerfDatacomClientPast24StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 480, 1)
)
pm10010mptPerfDatacomClientPast24StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptPerfDatacomClientPast24StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm10010mptPerfDatacomClientPast24StatHistoryPort1Entry.setStatus("current")


class _Pm10010mptPerfDatacomClientPast24StatHistoryPort1Index_Type(Integer32):
    """Custom type pm10010mptPerfDatacomClientPast24StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptPerfDatacomClientPast24StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm10010mptPerfDatacomClientPast24StatHistoryPort1Index_Object = MibTableColumn
pm10010mptPerfDatacomClientPast24StatHistoryPort1Index = _Pm10010mptPerfDatacomClientPast24StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 480, 1, 1),
    _Pm10010mptPerfDatacomClientPast24StatHistoryPort1Index_Type()
)
pm10010mptPerfDatacomClientPast24StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfDatacomClientPast24StatHistoryPort1Index.setStatus("current")
_Rm10010perfdatacomclientPast24StatInCrcCountInvPort1_Type = EkiOnOff
_Rm10010perfdatacomclientPast24StatInCrcCountInvPort1_Object = MibTableColumn
rm10010perfdatacomclientPast24StatInCrcCountInvPort1 = _Rm10010perfdatacomclientPast24StatInCrcCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 480, 1, 4),
    _Rm10010perfdatacomclientPast24StatInCrcCountInvPort1_Type()
)
rm10010perfdatacomclientPast24StatInCrcCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientPast24StatInCrcCountInvPort1.setStatus("current")
_Rm10010perfdatacomclientPast24StatInCrcCountPort1_Type = Counter64
_Rm10010perfdatacomclientPast24StatInCrcCountPort1_Object = MibTableColumn
rm10010perfdatacomclientPast24StatInCrcCountPort1 = _Rm10010perfdatacomclientPast24StatInCrcCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 480, 1, 5),
    _Rm10010perfdatacomclientPast24StatInCrcCountPort1_Type()
)
rm10010perfdatacomclientPast24StatInCrcCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientPast24StatInCrcCountPort1.setStatus("current")
_Rm10010perfdatacomclientPast24StatInPacketCountInvPort1_Type = EkiOnOff
_Rm10010perfdatacomclientPast24StatInPacketCountInvPort1_Object = MibTableColumn
rm10010perfdatacomclientPast24StatInPacketCountInvPort1 = _Rm10010perfdatacomclientPast24StatInPacketCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 480, 1, 6),
    _Rm10010perfdatacomclientPast24StatInPacketCountInvPort1_Type()
)
rm10010perfdatacomclientPast24StatInPacketCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientPast24StatInPacketCountInvPort1.setStatus("current")
_Rm10010perfdatacomclientPast24StatInPacketCountPort1_Type = Counter64
_Rm10010perfdatacomclientPast24StatInPacketCountPort1_Object = MibTableColumn
rm10010perfdatacomclientPast24StatInPacketCountPort1 = _Rm10010perfdatacomclientPast24StatInPacketCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 480, 1, 7),
    _Rm10010perfdatacomclientPast24StatInPacketCountPort1_Type()
)
rm10010perfdatacomclientPast24StatInPacketCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientPast24StatInPacketCountPort1.setStatus("current")
_Rm10010perfdatacomclientPast24StatOutCrcCountInvPort1_Type = EkiOnOff
_Rm10010perfdatacomclientPast24StatOutCrcCountInvPort1_Object = MibTableColumn
rm10010perfdatacomclientPast24StatOutCrcCountInvPort1 = _Rm10010perfdatacomclientPast24StatOutCrcCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 480, 1, 28),
    _Rm10010perfdatacomclientPast24StatOutCrcCountInvPort1_Type()
)
rm10010perfdatacomclientPast24StatOutCrcCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientPast24StatOutCrcCountInvPort1.setStatus("current")
_Rm10010perfdatacomclientPast24StatOutCrcCountPort1_Type = Counter64
_Rm10010perfdatacomclientPast24StatOutCrcCountPort1_Object = MibTableColumn
rm10010perfdatacomclientPast24StatOutCrcCountPort1 = _Rm10010perfdatacomclientPast24StatOutCrcCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 480, 1, 29),
    _Rm10010perfdatacomclientPast24StatOutCrcCountPort1_Type()
)
rm10010perfdatacomclientPast24StatOutCrcCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientPast24StatOutCrcCountPort1.setStatus("current")
_Rm10010perfdatacomclientPast24StatOutPacketCountInvPort1_Type = EkiOnOff
_Rm10010perfdatacomclientPast24StatOutPacketCountInvPort1_Object = MibTableColumn
rm10010perfdatacomclientPast24StatOutPacketCountInvPort1 = _Rm10010perfdatacomclientPast24StatOutPacketCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 480, 1, 30),
    _Rm10010perfdatacomclientPast24StatOutPacketCountInvPort1_Type()
)
rm10010perfdatacomclientPast24StatOutPacketCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientPast24StatOutPacketCountInvPort1.setStatus("current")
_Rm10010perfdatacomclientPast24StatOutPacketCountPort1_Type = Counter64
_Rm10010perfdatacomclientPast24StatOutPacketCountPort1_Object = MibTableColumn
rm10010perfdatacomclientPast24StatOutPacketCountPort1 = _Rm10010perfdatacomclientPast24StatOutPacketCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 6, 480, 1, 31),
    _Rm10010perfdatacomclientPast24StatOutPacketCountPort1_Type()
)
rm10010perfdatacomclientPast24StatOutPacketCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientPast24StatOutPacketCountPort1.setStatus("current")
_Pm10010mptMonPerfLine_ObjectIdentity = ObjectIdentity
pm10010mptMonPerfLine = _Pm10010mptMonPerfLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7)
)
_Pm10010mptPerfTelecomLinePostFecCurrent15StatTable_Object = MibTable
pm10010mptPerfTelecomLinePostFecCurrent15StatTable = _Pm10010mptPerfTelecomLinePostFecCurrent15StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 192)
)
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomLinePostFecCurrent15StatTable.setStatus("current")
_Pm10010mptPerfTelecomLinePostFecCurrent15StatEntry_Object = MibTableRow
pm10010mptPerfTelecomLinePostFecCurrent15StatEntry = _Pm10010mptPerfTelecomLinePostFecCurrent15StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 192, 1)
)
pm10010mptPerfTelecomLinePostFecCurrent15StatEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptPerfTelecomLinePostFecCurrent15StatIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomLinePostFecCurrent15StatEntry.setStatus("current")


class _Pm10010mptPerfTelecomLinePostFecCurrent15StatIndex_Type(Integer32):
    """Custom type pm10010mptPerfTelecomLinePostFecCurrent15StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptPerfTelecomLinePostFecCurrent15StatIndex_Type.__name__ = "Integer32"
_Pm10010mptPerfTelecomLinePostFecCurrent15StatIndex_Object = MibTableColumn
pm10010mptPerfTelecomLinePostFecCurrent15StatIndex = _Pm10010mptPerfTelecomLinePostFecCurrent15StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 192, 1, 1),
    _Pm10010mptPerfTelecomLinePostFecCurrent15StatIndex_Type()
)
pm10010mptPerfTelecomLinePostFecCurrent15StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomLinePostFecCurrent15StatIndex.setStatus("current")
_Pm10010mptPerfTelecomLinePostFecCurrent15StatInvCvPortn_Type = EkiOnOff
_Pm10010mptPerfTelecomLinePostFecCurrent15StatInvCvPortn_Object = MibTableColumn
pm10010mptPerfTelecomLinePostFecCurrent15StatInvCvPortn = _Pm10010mptPerfTelecomLinePostFecCurrent15StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 192, 1, 2),
    _Pm10010mptPerfTelecomLinePostFecCurrent15StatInvCvPortn_Type()
)
pm10010mptPerfTelecomLinePostFecCurrent15StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomLinePostFecCurrent15StatInvCvPortn.setStatus("current")
_Pm10010mptPerfTelecomLinePostFecCurrent15StatCvValuePortn_Type = Unsigned32
_Pm10010mptPerfTelecomLinePostFecCurrent15StatCvValuePortn_Object = MibTableColumn
pm10010mptPerfTelecomLinePostFecCurrent15StatCvValuePortn = _Pm10010mptPerfTelecomLinePostFecCurrent15StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 192, 1, 3),
    _Pm10010mptPerfTelecomLinePostFecCurrent15StatCvValuePortn_Type()
)
pm10010mptPerfTelecomLinePostFecCurrent15StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomLinePostFecCurrent15StatCvValuePortn.setStatus("current")
_Pm10010mptPerfTelecomLinePostFecCurrent15StatInvEsPortn_Type = EkiOnOff
_Pm10010mptPerfTelecomLinePostFecCurrent15StatInvEsPortn_Object = MibTableColumn
pm10010mptPerfTelecomLinePostFecCurrent15StatInvEsPortn = _Pm10010mptPerfTelecomLinePostFecCurrent15StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 192, 1, 4),
    _Pm10010mptPerfTelecomLinePostFecCurrent15StatInvEsPortn_Type()
)
pm10010mptPerfTelecomLinePostFecCurrent15StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomLinePostFecCurrent15StatInvEsPortn.setStatus("current")
_Pm10010mptPerfTelecomLinePostFecCurrent15StatEsValuePortn_Type = Unsigned32
_Pm10010mptPerfTelecomLinePostFecCurrent15StatEsValuePortn_Object = MibTableColumn
pm10010mptPerfTelecomLinePostFecCurrent15StatEsValuePortn = _Pm10010mptPerfTelecomLinePostFecCurrent15StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 192, 1, 5),
    _Pm10010mptPerfTelecomLinePostFecCurrent15StatEsValuePortn_Type()
)
pm10010mptPerfTelecomLinePostFecCurrent15StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomLinePostFecCurrent15StatEsValuePortn.setStatus("current")
_Pm10010mptPerfTelecomLinePostFecCurrent15StatInvSesPortn_Type = EkiOnOff
_Pm10010mptPerfTelecomLinePostFecCurrent15StatInvSesPortn_Object = MibTableColumn
pm10010mptPerfTelecomLinePostFecCurrent15StatInvSesPortn = _Pm10010mptPerfTelecomLinePostFecCurrent15StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 192, 1, 6),
    _Pm10010mptPerfTelecomLinePostFecCurrent15StatInvSesPortn_Type()
)
pm10010mptPerfTelecomLinePostFecCurrent15StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomLinePostFecCurrent15StatInvSesPortn.setStatus("current")
_Pm10010mptPerfTelecomLinePostFecCurrent15StatSesValuePortn_Type = Unsigned32
_Pm10010mptPerfTelecomLinePostFecCurrent15StatSesValuePortn_Object = MibTableColumn
pm10010mptPerfTelecomLinePostFecCurrent15StatSesValuePortn = _Pm10010mptPerfTelecomLinePostFecCurrent15StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 192, 1, 7),
    _Pm10010mptPerfTelecomLinePostFecCurrent15StatSesValuePortn_Type()
)
pm10010mptPerfTelecomLinePostFecCurrent15StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomLinePostFecCurrent15StatSesValuePortn.setStatus("current")
_Pm10010mptPerfTelecomLinePostFecCurrent15StatInvSefsPortn_Type = EkiOnOff
_Pm10010mptPerfTelecomLinePostFecCurrent15StatInvSefsPortn_Object = MibTableColumn
pm10010mptPerfTelecomLinePostFecCurrent15StatInvSefsPortn = _Pm10010mptPerfTelecomLinePostFecCurrent15StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 192, 1, 8),
    _Pm10010mptPerfTelecomLinePostFecCurrent15StatInvSefsPortn_Type()
)
pm10010mptPerfTelecomLinePostFecCurrent15StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomLinePostFecCurrent15StatInvSefsPortn.setStatus("current")
_Pm10010mptPerfTelecomLinePostFecCurrent15StatSefsValuePortn_Type = Unsigned32
_Pm10010mptPerfTelecomLinePostFecCurrent15StatSefsValuePortn_Object = MibTableColumn
pm10010mptPerfTelecomLinePostFecCurrent15StatSefsValuePortn = _Pm10010mptPerfTelecomLinePostFecCurrent15StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 192, 1, 9),
    _Pm10010mptPerfTelecomLinePostFecCurrent15StatSefsValuePortn_Type()
)
pm10010mptPerfTelecomLinePostFecCurrent15StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomLinePostFecCurrent15StatSefsValuePortn.setStatus("current")
_Pm10010mptPerfTelecomLinePostFecCurrent15StatInvUasPortn_Type = EkiOnOff
_Pm10010mptPerfTelecomLinePostFecCurrent15StatInvUasPortn_Object = MibTableColumn
pm10010mptPerfTelecomLinePostFecCurrent15StatInvUasPortn = _Pm10010mptPerfTelecomLinePostFecCurrent15StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 192, 1, 10),
    _Pm10010mptPerfTelecomLinePostFecCurrent15StatInvUasPortn_Type()
)
pm10010mptPerfTelecomLinePostFecCurrent15StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomLinePostFecCurrent15StatInvUasPortn.setStatus("current")
_Pm10010mptPerfTelecomLinePostFecCurrent15StatUasValuePortn_Type = Unsigned32
_Pm10010mptPerfTelecomLinePostFecCurrent15StatUasValuePortn_Object = MibTableColumn
pm10010mptPerfTelecomLinePostFecCurrent15StatUasValuePortn = _Pm10010mptPerfTelecomLinePostFecCurrent15StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 192, 1, 11),
    _Pm10010mptPerfTelecomLinePostFecCurrent15StatUasValuePortn_Type()
)
pm10010mptPerfTelecomLinePostFecCurrent15StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomLinePostFecCurrent15StatUasValuePortn.setStatus("current")
_Pm10010mptPerfTelecomLinePostFecPast15StatHistoryPort1Table_Object = MibTable
pm10010mptPerfTelecomLinePostFecPast15StatHistoryPort1Table = _Pm10010mptPerfTelecomLinePostFecPast15StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 193)
)
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomLinePostFecPast15StatHistoryPort1Table.setStatus("current")
_Pm10010mptPerfTelecomLinePostFecPast15StatHistoryPort1Entry_Object = MibTableRow
pm10010mptPerfTelecomLinePostFecPast15StatHistoryPort1Entry = _Pm10010mptPerfTelecomLinePostFecPast15StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 193, 1)
)
pm10010mptPerfTelecomLinePostFecPast15StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptPerfTelecomLinePostFecPast15StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomLinePostFecPast15StatHistoryPort1Entry.setStatus("current")


class _Pm10010mptPerfTelecomLinePostFecPast15StatHistoryPort1Index_Type(Integer32):
    """Custom type pm10010mptPerfTelecomLinePostFecPast15StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptPerfTelecomLinePostFecPast15StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm10010mptPerfTelecomLinePostFecPast15StatHistoryPort1Index_Object = MibTableColumn
pm10010mptPerfTelecomLinePostFecPast15StatHistoryPort1Index = _Pm10010mptPerfTelecomLinePostFecPast15StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 193, 1, 1),
    _Pm10010mptPerfTelecomLinePostFecPast15StatHistoryPort1Index_Type()
)
pm10010mptPerfTelecomLinePostFecPast15StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomLinePostFecPast15StatHistoryPort1Index.setStatus("current")
_Pm10010mptPerfTelecomLinePostFecPast15StatHistoryInvCvPort1_Type = EkiOnOff
_Pm10010mptPerfTelecomLinePostFecPast15StatHistoryInvCvPort1_Object = MibTableColumn
pm10010mptPerfTelecomLinePostFecPast15StatHistoryInvCvPort1 = _Pm10010mptPerfTelecomLinePostFecPast15StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 193, 1, 2),
    _Pm10010mptPerfTelecomLinePostFecPast15StatHistoryInvCvPort1_Type()
)
pm10010mptPerfTelecomLinePostFecPast15StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomLinePostFecPast15StatHistoryInvCvPort1.setStatus("current")
_Pm10010mptPerfTelecomLinePostFecPast15StatHistoryCvValuePort1_Type = Unsigned32
_Pm10010mptPerfTelecomLinePostFecPast15StatHistoryCvValuePort1_Object = MibTableColumn
pm10010mptPerfTelecomLinePostFecPast15StatHistoryCvValuePort1 = _Pm10010mptPerfTelecomLinePostFecPast15StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 193, 1, 3),
    _Pm10010mptPerfTelecomLinePostFecPast15StatHistoryCvValuePort1_Type()
)
pm10010mptPerfTelecomLinePostFecPast15StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomLinePostFecPast15StatHistoryCvValuePort1.setStatus("current")
_Pm10010mptPerfTelecomLinePostFecPast15StatHistoryInvEsPort1_Type = EkiOnOff
_Pm10010mptPerfTelecomLinePostFecPast15StatHistoryInvEsPort1_Object = MibTableColumn
pm10010mptPerfTelecomLinePostFecPast15StatHistoryInvEsPort1 = _Pm10010mptPerfTelecomLinePostFecPast15StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 193, 1, 4),
    _Pm10010mptPerfTelecomLinePostFecPast15StatHistoryInvEsPort1_Type()
)
pm10010mptPerfTelecomLinePostFecPast15StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomLinePostFecPast15StatHistoryInvEsPort1.setStatus("current")
_Pm10010mptPerfTelecomLinePostFecPast15StatHistoryEsValuePort1_Type = Unsigned32
_Pm10010mptPerfTelecomLinePostFecPast15StatHistoryEsValuePort1_Object = MibTableColumn
pm10010mptPerfTelecomLinePostFecPast15StatHistoryEsValuePort1 = _Pm10010mptPerfTelecomLinePostFecPast15StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 193, 1, 5),
    _Pm10010mptPerfTelecomLinePostFecPast15StatHistoryEsValuePort1_Type()
)
pm10010mptPerfTelecomLinePostFecPast15StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomLinePostFecPast15StatHistoryEsValuePort1.setStatus("current")
_Pm10010mptPerfTelecomLinePostFecPast15StatHistoryInvSesPort1_Type = EkiOnOff
_Pm10010mptPerfTelecomLinePostFecPast15StatHistoryInvSesPort1_Object = MibTableColumn
pm10010mptPerfTelecomLinePostFecPast15StatHistoryInvSesPort1 = _Pm10010mptPerfTelecomLinePostFecPast15StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 193, 1, 6),
    _Pm10010mptPerfTelecomLinePostFecPast15StatHistoryInvSesPort1_Type()
)
pm10010mptPerfTelecomLinePostFecPast15StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomLinePostFecPast15StatHistoryInvSesPort1.setStatus("current")
_Pm10010mptPerfTelecomLinePostFecPast15StatHistorySesValuePort1_Type = Unsigned32
_Pm10010mptPerfTelecomLinePostFecPast15StatHistorySesValuePort1_Object = MibTableColumn
pm10010mptPerfTelecomLinePostFecPast15StatHistorySesValuePort1 = _Pm10010mptPerfTelecomLinePostFecPast15StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 193, 1, 7),
    _Pm10010mptPerfTelecomLinePostFecPast15StatHistorySesValuePort1_Type()
)
pm10010mptPerfTelecomLinePostFecPast15StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomLinePostFecPast15StatHistorySesValuePort1.setStatus("current")
_Pm10010mptPerfTelecomLinePostFecPast15StatHistoryInvSefsPort1_Type = EkiOnOff
_Pm10010mptPerfTelecomLinePostFecPast15StatHistoryInvSefsPort1_Object = MibTableColumn
pm10010mptPerfTelecomLinePostFecPast15StatHistoryInvSefsPort1 = _Pm10010mptPerfTelecomLinePostFecPast15StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 193, 1, 8),
    _Pm10010mptPerfTelecomLinePostFecPast15StatHistoryInvSefsPort1_Type()
)
pm10010mptPerfTelecomLinePostFecPast15StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomLinePostFecPast15StatHistoryInvSefsPort1.setStatus("current")
_Pm10010mptPerfTelecomLinePostFecPast15StatHistorySefsValuePort1_Type = Unsigned32
_Pm10010mptPerfTelecomLinePostFecPast15StatHistorySefsValuePort1_Object = MibTableColumn
pm10010mptPerfTelecomLinePostFecPast15StatHistorySefsValuePort1 = _Pm10010mptPerfTelecomLinePostFecPast15StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 193, 1, 9),
    _Pm10010mptPerfTelecomLinePostFecPast15StatHistorySefsValuePort1_Type()
)
pm10010mptPerfTelecomLinePostFecPast15StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomLinePostFecPast15StatHistorySefsValuePort1.setStatus("current")
_Pm10010mptPerfTelecomLinePostFecPast15StatHistoryInvUasPort1_Type = EkiOnOff
_Pm10010mptPerfTelecomLinePostFecPast15StatHistoryInvUasPort1_Object = MibTableColumn
pm10010mptPerfTelecomLinePostFecPast15StatHistoryInvUasPort1 = _Pm10010mptPerfTelecomLinePostFecPast15StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 193, 1, 10),
    _Pm10010mptPerfTelecomLinePostFecPast15StatHistoryInvUasPort1_Type()
)
pm10010mptPerfTelecomLinePostFecPast15StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomLinePostFecPast15StatHistoryInvUasPort1.setStatus("current")
_Pm10010mptPerfTelecomLinePostFecPast15StatHistoryUasValuePort1_Type = Unsigned32
_Pm10010mptPerfTelecomLinePostFecPast15StatHistoryUasValuePort1_Object = MibTableColumn
pm10010mptPerfTelecomLinePostFecPast15StatHistoryUasValuePort1 = _Pm10010mptPerfTelecomLinePostFecPast15StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 193, 1, 11),
    _Pm10010mptPerfTelecomLinePostFecPast15StatHistoryUasValuePort1_Type()
)
pm10010mptPerfTelecomLinePostFecPast15StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomLinePostFecPast15StatHistoryUasValuePort1.setStatus("current")
_Pm10010mptPerfTelecomLinePostFecCurrent24StatTable_Object = MibTable
pm10010mptPerfTelecomLinePostFecCurrent24StatTable = _Pm10010mptPerfTelecomLinePostFecCurrent24StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 194)
)
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomLinePostFecCurrent24StatTable.setStatus("current")
_Pm10010mptPerfTelecomLinePostFecCurrent24StatEntry_Object = MibTableRow
pm10010mptPerfTelecomLinePostFecCurrent24StatEntry = _Pm10010mptPerfTelecomLinePostFecCurrent24StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 194, 1)
)
pm10010mptPerfTelecomLinePostFecCurrent24StatEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptPerfTelecomLinePostFecCurrent24StatIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomLinePostFecCurrent24StatEntry.setStatus("current")


class _Pm10010mptPerfTelecomLinePostFecCurrent24StatIndex_Type(Integer32):
    """Custom type pm10010mptPerfTelecomLinePostFecCurrent24StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptPerfTelecomLinePostFecCurrent24StatIndex_Type.__name__ = "Integer32"
_Pm10010mptPerfTelecomLinePostFecCurrent24StatIndex_Object = MibTableColumn
pm10010mptPerfTelecomLinePostFecCurrent24StatIndex = _Pm10010mptPerfTelecomLinePostFecCurrent24StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 194, 1, 1),
    _Pm10010mptPerfTelecomLinePostFecCurrent24StatIndex_Type()
)
pm10010mptPerfTelecomLinePostFecCurrent24StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomLinePostFecCurrent24StatIndex.setStatus("current")
_Pm10010mptPerfTelecomLinePostFecCurrent24StatInvCvPortn_Type = EkiOnOff
_Pm10010mptPerfTelecomLinePostFecCurrent24StatInvCvPortn_Object = MibTableColumn
pm10010mptPerfTelecomLinePostFecCurrent24StatInvCvPortn = _Pm10010mptPerfTelecomLinePostFecCurrent24StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 194, 1, 2),
    _Pm10010mptPerfTelecomLinePostFecCurrent24StatInvCvPortn_Type()
)
pm10010mptPerfTelecomLinePostFecCurrent24StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomLinePostFecCurrent24StatInvCvPortn.setStatus("current")
_Pm10010mptPerfTelecomLinePostFecCurrent24StatCvValuePortn_Type = Unsigned32
_Pm10010mptPerfTelecomLinePostFecCurrent24StatCvValuePortn_Object = MibTableColumn
pm10010mptPerfTelecomLinePostFecCurrent24StatCvValuePortn = _Pm10010mptPerfTelecomLinePostFecCurrent24StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 194, 1, 3),
    _Pm10010mptPerfTelecomLinePostFecCurrent24StatCvValuePortn_Type()
)
pm10010mptPerfTelecomLinePostFecCurrent24StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomLinePostFecCurrent24StatCvValuePortn.setStatus("current")
_Pm10010mptPerfTelecomLinePostFecCurrent24StatInvEsPortn_Type = EkiOnOff
_Pm10010mptPerfTelecomLinePostFecCurrent24StatInvEsPortn_Object = MibTableColumn
pm10010mptPerfTelecomLinePostFecCurrent24StatInvEsPortn = _Pm10010mptPerfTelecomLinePostFecCurrent24StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 194, 1, 4),
    _Pm10010mptPerfTelecomLinePostFecCurrent24StatInvEsPortn_Type()
)
pm10010mptPerfTelecomLinePostFecCurrent24StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomLinePostFecCurrent24StatInvEsPortn.setStatus("current")
_Pm10010mptPerfTelecomLinePostFecCurrent24StatEsValuePortn_Type = Unsigned32
_Pm10010mptPerfTelecomLinePostFecCurrent24StatEsValuePortn_Object = MibTableColumn
pm10010mptPerfTelecomLinePostFecCurrent24StatEsValuePortn = _Pm10010mptPerfTelecomLinePostFecCurrent24StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 194, 1, 5),
    _Pm10010mptPerfTelecomLinePostFecCurrent24StatEsValuePortn_Type()
)
pm10010mptPerfTelecomLinePostFecCurrent24StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomLinePostFecCurrent24StatEsValuePortn.setStatus("current")
_Pm10010mptPerfTelecomLinePostFecCurrent24StatInvSesPortn_Type = EkiOnOff
_Pm10010mptPerfTelecomLinePostFecCurrent24StatInvSesPortn_Object = MibTableColumn
pm10010mptPerfTelecomLinePostFecCurrent24StatInvSesPortn = _Pm10010mptPerfTelecomLinePostFecCurrent24StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 194, 1, 6),
    _Pm10010mptPerfTelecomLinePostFecCurrent24StatInvSesPortn_Type()
)
pm10010mptPerfTelecomLinePostFecCurrent24StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomLinePostFecCurrent24StatInvSesPortn.setStatus("current")
_Pm10010mptPerfTelecomLinePostFecCurrent24StatSesValuePortn_Type = Unsigned32
_Pm10010mptPerfTelecomLinePostFecCurrent24StatSesValuePortn_Object = MibTableColumn
pm10010mptPerfTelecomLinePostFecCurrent24StatSesValuePortn = _Pm10010mptPerfTelecomLinePostFecCurrent24StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 194, 1, 7),
    _Pm10010mptPerfTelecomLinePostFecCurrent24StatSesValuePortn_Type()
)
pm10010mptPerfTelecomLinePostFecCurrent24StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomLinePostFecCurrent24StatSesValuePortn.setStatus("current")
_Pm10010mptPerfTelecomLinePostFecCurrent24StatInvSefsPortn_Type = EkiOnOff
_Pm10010mptPerfTelecomLinePostFecCurrent24StatInvSefsPortn_Object = MibTableColumn
pm10010mptPerfTelecomLinePostFecCurrent24StatInvSefsPortn = _Pm10010mptPerfTelecomLinePostFecCurrent24StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 194, 1, 8),
    _Pm10010mptPerfTelecomLinePostFecCurrent24StatInvSefsPortn_Type()
)
pm10010mptPerfTelecomLinePostFecCurrent24StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomLinePostFecCurrent24StatInvSefsPortn.setStatus("current")
_Pm10010mptPerfTelecomLinePostFecCurrent24StatSefsValuePortn_Type = Unsigned32
_Pm10010mptPerfTelecomLinePostFecCurrent24StatSefsValuePortn_Object = MibTableColumn
pm10010mptPerfTelecomLinePostFecCurrent24StatSefsValuePortn = _Pm10010mptPerfTelecomLinePostFecCurrent24StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 194, 1, 9),
    _Pm10010mptPerfTelecomLinePostFecCurrent24StatSefsValuePortn_Type()
)
pm10010mptPerfTelecomLinePostFecCurrent24StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomLinePostFecCurrent24StatSefsValuePortn.setStatus("current")
_Pm10010mptPerfTelecomLinePostFecCurrent24StatInvUasPortn_Type = EkiOnOff
_Pm10010mptPerfTelecomLinePostFecCurrent24StatInvUasPortn_Object = MibTableColumn
pm10010mptPerfTelecomLinePostFecCurrent24StatInvUasPortn = _Pm10010mptPerfTelecomLinePostFecCurrent24StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 194, 1, 10),
    _Pm10010mptPerfTelecomLinePostFecCurrent24StatInvUasPortn_Type()
)
pm10010mptPerfTelecomLinePostFecCurrent24StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomLinePostFecCurrent24StatInvUasPortn.setStatus("current")
_Pm10010mptPerfTelecomLinePostFecCurrent24StatUasValuePortn_Type = Unsigned32
_Pm10010mptPerfTelecomLinePostFecCurrent24StatUasValuePortn_Object = MibTableColumn
pm10010mptPerfTelecomLinePostFecCurrent24StatUasValuePortn = _Pm10010mptPerfTelecomLinePostFecCurrent24StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 194, 1, 11),
    _Pm10010mptPerfTelecomLinePostFecCurrent24StatUasValuePortn_Type()
)
pm10010mptPerfTelecomLinePostFecCurrent24StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomLinePostFecCurrent24StatUasValuePortn.setStatus("current")
_Pm10010mptPerfTelecomLinePostFecPast24StatHistoryPort1Table_Object = MibTable
pm10010mptPerfTelecomLinePostFecPast24StatHistoryPort1Table = _Pm10010mptPerfTelecomLinePostFecPast24StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 195)
)
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomLinePostFecPast24StatHistoryPort1Table.setStatus("current")
_Pm10010mptPerfTelecomLinePostFecPast24StatHistoryPort1Entry_Object = MibTableRow
pm10010mptPerfTelecomLinePostFecPast24StatHistoryPort1Entry = _Pm10010mptPerfTelecomLinePostFecPast24StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 195, 1)
)
pm10010mptPerfTelecomLinePostFecPast24StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptPerfTelecomLinePostFecPast24StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomLinePostFecPast24StatHistoryPort1Entry.setStatus("current")


class _Pm10010mptPerfTelecomLinePostFecPast24StatHistoryPort1Index_Type(Integer32):
    """Custom type pm10010mptPerfTelecomLinePostFecPast24StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptPerfTelecomLinePostFecPast24StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm10010mptPerfTelecomLinePostFecPast24StatHistoryPort1Index_Object = MibTableColumn
pm10010mptPerfTelecomLinePostFecPast24StatHistoryPort1Index = _Pm10010mptPerfTelecomLinePostFecPast24StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 195, 1, 1),
    _Pm10010mptPerfTelecomLinePostFecPast24StatHistoryPort1Index_Type()
)
pm10010mptPerfTelecomLinePostFecPast24StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomLinePostFecPast24StatHistoryPort1Index.setStatus("current")
_Pm10010mptPerfTelecomLinePostFecPast24StatHistoryInvCvPort1_Type = EkiOnOff
_Pm10010mptPerfTelecomLinePostFecPast24StatHistoryInvCvPort1_Object = MibTableColumn
pm10010mptPerfTelecomLinePostFecPast24StatHistoryInvCvPort1 = _Pm10010mptPerfTelecomLinePostFecPast24StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 195, 1, 2),
    _Pm10010mptPerfTelecomLinePostFecPast24StatHistoryInvCvPort1_Type()
)
pm10010mptPerfTelecomLinePostFecPast24StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomLinePostFecPast24StatHistoryInvCvPort1.setStatus("current")
_Pm10010mptPerfTelecomLinePostFecPast24StatHistoryCvValuePort1_Type = Unsigned32
_Pm10010mptPerfTelecomLinePostFecPast24StatHistoryCvValuePort1_Object = MibTableColumn
pm10010mptPerfTelecomLinePostFecPast24StatHistoryCvValuePort1 = _Pm10010mptPerfTelecomLinePostFecPast24StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 195, 1, 3),
    _Pm10010mptPerfTelecomLinePostFecPast24StatHistoryCvValuePort1_Type()
)
pm10010mptPerfTelecomLinePostFecPast24StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomLinePostFecPast24StatHistoryCvValuePort1.setStatus("current")
_Pm10010mptPerfTelecomLinePostFecPast24StatHistoryInvEsPort1_Type = EkiOnOff
_Pm10010mptPerfTelecomLinePostFecPast24StatHistoryInvEsPort1_Object = MibTableColumn
pm10010mptPerfTelecomLinePostFecPast24StatHistoryInvEsPort1 = _Pm10010mptPerfTelecomLinePostFecPast24StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 195, 1, 4),
    _Pm10010mptPerfTelecomLinePostFecPast24StatHistoryInvEsPort1_Type()
)
pm10010mptPerfTelecomLinePostFecPast24StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomLinePostFecPast24StatHistoryInvEsPort1.setStatus("current")
_Pm10010mptPerfTelecomLinePostFecPast24StatHistoryEsValuePort1_Type = Unsigned32
_Pm10010mptPerfTelecomLinePostFecPast24StatHistoryEsValuePort1_Object = MibTableColumn
pm10010mptPerfTelecomLinePostFecPast24StatHistoryEsValuePort1 = _Pm10010mptPerfTelecomLinePostFecPast24StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 195, 1, 5),
    _Pm10010mptPerfTelecomLinePostFecPast24StatHistoryEsValuePort1_Type()
)
pm10010mptPerfTelecomLinePostFecPast24StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomLinePostFecPast24StatHistoryEsValuePort1.setStatus("current")
_Pm10010mptPerfTelecomLinePostFecPast24StatHistoryInvSesPort1_Type = EkiOnOff
_Pm10010mptPerfTelecomLinePostFecPast24StatHistoryInvSesPort1_Object = MibTableColumn
pm10010mptPerfTelecomLinePostFecPast24StatHistoryInvSesPort1 = _Pm10010mptPerfTelecomLinePostFecPast24StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 195, 1, 6),
    _Pm10010mptPerfTelecomLinePostFecPast24StatHistoryInvSesPort1_Type()
)
pm10010mptPerfTelecomLinePostFecPast24StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomLinePostFecPast24StatHistoryInvSesPort1.setStatus("current")
_Pm10010mptPerfTelecomLinePostFecPast24StatHistorySesValuePort1_Type = Unsigned32
_Pm10010mptPerfTelecomLinePostFecPast24StatHistorySesValuePort1_Object = MibTableColumn
pm10010mptPerfTelecomLinePostFecPast24StatHistorySesValuePort1 = _Pm10010mptPerfTelecomLinePostFecPast24StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 195, 1, 7),
    _Pm10010mptPerfTelecomLinePostFecPast24StatHistorySesValuePort1_Type()
)
pm10010mptPerfTelecomLinePostFecPast24StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomLinePostFecPast24StatHistorySesValuePort1.setStatus("current")
_Pm10010mptPerfTelecomLinePostFecPast24StatHistoryInvSefsPort1_Type = EkiOnOff
_Pm10010mptPerfTelecomLinePostFecPast24StatHistoryInvSefsPort1_Object = MibTableColumn
pm10010mptPerfTelecomLinePostFecPast24StatHistoryInvSefsPort1 = _Pm10010mptPerfTelecomLinePostFecPast24StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 195, 1, 8),
    _Pm10010mptPerfTelecomLinePostFecPast24StatHistoryInvSefsPort1_Type()
)
pm10010mptPerfTelecomLinePostFecPast24StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomLinePostFecPast24StatHistoryInvSefsPort1.setStatus("current")
_Pm10010mptPerfTelecomLinePostFecPast24StatHistorySefsValuePort1_Type = Unsigned32
_Pm10010mptPerfTelecomLinePostFecPast24StatHistorySefsValuePort1_Object = MibTableColumn
pm10010mptPerfTelecomLinePostFecPast24StatHistorySefsValuePort1 = _Pm10010mptPerfTelecomLinePostFecPast24StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 195, 1, 9),
    _Pm10010mptPerfTelecomLinePostFecPast24StatHistorySefsValuePort1_Type()
)
pm10010mptPerfTelecomLinePostFecPast24StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomLinePostFecPast24StatHistorySefsValuePort1.setStatus("current")
_Pm10010mptPerfTelecomLinePostFecPast24StatHistoryInvUasPort1_Type = EkiOnOff
_Pm10010mptPerfTelecomLinePostFecPast24StatHistoryInvUasPort1_Object = MibTableColumn
pm10010mptPerfTelecomLinePostFecPast24StatHistoryInvUasPort1 = _Pm10010mptPerfTelecomLinePostFecPast24StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 195, 1, 10),
    _Pm10010mptPerfTelecomLinePostFecPast24StatHistoryInvUasPort1_Type()
)
pm10010mptPerfTelecomLinePostFecPast24StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomLinePostFecPast24StatHistoryInvUasPort1.setStatus("current")
_Pm10010mptPerfTelecomLinePostFecPast24StatHistoryUasValuePort1_Type = Unsigned32
_Pm10010mptPerfTelecomLinePostFecPast24StatHistoryUasValuePort1_Object = MibTableColumn
pm10010mptPerfTelecomLinePostFecPast24StatHistoryUasValuePort1 = _Pm10010mptPerfTelecomLinePostFecPast24StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 195, 1, 11),
    _Pm10010mptPerfTelecomLinePostFecPast24StatHistoryUasValuePort1_Type()
)
pm10010mptPerfTelecomLinePostFecPast24StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomLinePostFecPast24StatHistoryUasValuePort1.setStatus("current")
_Pm10010mptPerfTelecomBerLinePreFecCurrent15StatTable_Object = MibTable
pm10010mptPerfTelecomBerLinePreFecCurrent15StatTable = _Pm10010mptPerfTelecomBerLinePreFecCurrent15StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 208)
)
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomBerLinePreFecCurrent15StatTable.setStatus("current")
_Pm10010mptPerfTelecomBerLinePreFecCurrent15StatEntry_Object = MibTableRow
pm10010mptPerfTelecomBerLinePreFecCurrent15StatEntry = _Pm10010mptPerfTelecomBerLinePreFecCurrent15StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 208, 1)
)
pm10010mptPerfTelecomBerLinePreFecCurrent15StatEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptPerfTelecomBerLinePreFecCurrent15StatIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomBerLinePreFecCurrent15StatEntry.setStatus("current")


class _Pm10010mptPerfTelecomBerLinePreFecCurrent15StatIndex_Type(Integer32):
    """Custom type pm10010mptPerfTelecomBerLinePreFecCurrent15StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptPerfTelecomBerLinePreFecCurrent15StatIndex_Type.__name__ = "Integer32"
_Pm10010mptPerfTelecomBerLinePreFecCurrent15StatIndex_Object = MibTableColumn
pm10010mptPerfTelecomBerLinePreFecCurrent15StatIndex = _Pm10010mptPerfTelecomBerLinePreFecCurrent15StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 208, 1, 1),
    _Pm10010mptPerfTelecomBerLinePreFecCurrent15StatIndex_Type()
)
pm10010mptPerfTelecomBerLinePreFecCurrent15StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomBerLinePreFecCurrent15StatIndex.setStatus("current")
_Pm10010mptPerfTelecomBerLinePreFecCurrent15StatInvBerPortn_Type = EkiOnOff
_Pm10010mptPerfTelecomBerLinePreFecCurrent15StatInvBerPortn_Object = MibTableColumn
pm10010mptPerfTelecomBerLinePreFecCurrent15StatInvBerPortn = _Pm10010mptPerfTelecomBerLinePreFecCurrent15StatInvBerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 208, 1, 2),
    _Pm10010mptPerfTelecomBerLinePreFecCurrent15StatInvBerPortn_Type()
)
pm10010mptPerfTelecomBerLinePreFecCurrent15StatInvBerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomBerLinePreFecCurrent15StatInvBerPortn.setStatus("current")
_Pm10010mptPerfTelecomBerLinePreFecCurrent15StatBerValuePortn_Type = Unsigned32
_Pm10010mptPerfTelecomBerLinePreFecCurrent15StatBerValuePortn_Object = MibTableColumn
pm10010mptPerfTelecomBerLinePreFecCurrent15StatBerValuePortn = _Pm10010mptPerfTelecomBerLinePreFecCurrent15StatBerValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 208, 1, 3),
    _Pm10010mptPerfTelecomBerLinePreFecCurrent15StatBerValuePortn_Type()
)
pm10010mptPerfTelecomBerLinePreFecCurrent15StatBerValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomBerLinePreFecCurrent15StatBerValuePortn.setStatus("current")
_Pm10010mptPerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn_Type = EkiOnOff
_Pm10010mptPerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn_Object = MibTableColumn
pm10010mptPerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn = _Pm10010mptPerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 208, 1, 4),
    _Pm10010mptPerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn_Type()
)
pm10010mptPerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn.setStatus("current")
_Pm10010mptPerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn_Type = Unsigned32
_Pm10010mptPerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn_Object = MibTableColumn
pm10010mptPerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn = _Pm10010mptPerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 208, 1, 5),
    _Pm10010mptPerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn_Type()
)
pm10010mptPerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn.setStatus("current")
_Pm10010mptPerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn_Type = EkiOnOff
_Pm10010mptPerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn_Object = MibTableColumn
pm10010mptPerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn = _Pm10010mptPerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 208, 1, 6),
    _Pm10010mptPerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn_Type()
)
pm10010mptPerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn.setStatus("current")
_Pm10010mptPerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn_Type = Unsigned32
_Pm10010mptPerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn_Object = MibTableColumn
pm10010mptPerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn = _Pm10010mptPerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 208, 1, 7),
    _Pm10010mptPerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn_Type()
)
pm10010mptPerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn.setStatus("current")
_Pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryPort1Table_Object = MibTable
pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryPort1Table = _Pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 209)
)
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryPort1Table.setStatus("current")
_Pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryPort1Entry_Object = MibTableRow
pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryPort1Entry = _Pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 209, 1)
)
pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryPort1Entry.setStatus("current")


class _Pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryPort1Index_Type(Integer32):
    """Custom type pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryPort1Index_Object = MibTableColumn
pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryPort1Index = _Pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 209, 1, 1),
    _Pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryPort1Index_Type()
)
pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryPort1Index.setStatus("current")
_Pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1_Type = EkiOnOff
_Pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1_Object = MibTableColumn
pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1 = _Pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 209, 1, 2),
    _Pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1_Type()
)
pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1.setStatus("current")
_Pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1_Type = Unsigned32
_Pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1_Object = MibTableColumn
pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1 = _Pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 209, 1, 3),
    _Pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1_Type()
)
pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1.setStatus("current")
_Pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1_Type = EkiOnOff
_Pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1_Object = MibTableColumn
pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1 = _Pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 209, 1, 4),
    _Pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1_Type()
)
pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1.setStatus("current")
_Pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1_Type = Unsigned32
_Pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1_Object = MibTableColumn
pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1 = _Pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 209, 1, 5),
    _Pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1_Type()
)
pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1.setStatus("current")
_Pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1_Type = EkiOnOff
_Pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1_Object = MibTableColumn
pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1 = _Pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 209, 1, 6),
    _Pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1_Type()
)
pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1.setStatus("current")
_Pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1_Type = Unsigned32
_Pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1_Object = MibTableColumn
pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1 = _Pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 209, 1, 7),
    _Pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1_Type()
)
pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1.setStatus("current")
_Pm10010mptPerfTelecomBerLinePreFecCurrent24StatTable_Object = MibTable
pm10010mptPerfTelecomBerLinePreFecCurrent24StatTable = _Pm10010mptPerfTelecomBerLinePreFecCurrent24StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 210)
)
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomBerLinePreFecCurrent24StatTable.setStatus("current")
_Pm10010mptPerfTelecomBerLinePreFecCurrent24StatEntry_Object = MibTableRow
pm10010mptPerfTelecomBerLinePreFecCurrent24StatEntry = _Pm10010mptPerfTelecomBerLinePreFecCurrent24StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 210, 1)
)
pm10010mptPerfTelecomBerLinePreFecCurrent24StatEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptPerfTelecomBerLinePreFecCurrent24StatIndex"),
)
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomBerLinePreFecCurrent24StatEntry.setStatus("current")


class _Pm10010mptPerfTelecomBerLinePreFecCurrent24StatIndex_Type(Integer32):
    """Custom type pm10010mptPerfTelecomBerLinePreFecCurrent24StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptPerfTelecomBerLinePreFecCurrent24StatIndex_Type.__name__ = "Integer32"
_Pm10010mptPerfTelecomBerLinePreFecCurrent24StatIndex_Object = MibTableColumn
pm10010mptPerfTelecomBerLinePreFecCurrent24StatIndex = _Pm10010mptPerfTelecomBerLinePreFecCurrent24StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 210, 1, 1),
    _Pm10010mptPerfTelecomBerLinePreFecCurrent24StatIndex_Type()
)
pm10010mptPerfTelecomBerLinePreFecCurrent24StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomBerLinePreFecCurrent24StatIndex.setStatus("current")
_Pm10010mptPerfTelecomBerLinePreFecCurrent24StatInvBerPortn_Type = EkiOnOff
_Pm10010mptPerfTelecomBerLinePreFecCurrent24StatInvBerPortn_Object = MibTableColumn
pm10010mptPerfTelecomBerLinePreFecCurrent24StatInvBerPortn = _Pm10010mptPerfTelecomBerLinePreFecCurrent24StatInvBerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 210, 1, 2),
    _Pm10010mptPerfTelecomBerLinePreFecCurrent24StatInvBerPortn_Type()
)
pm10010mptPerfTelecomBerLinePreFecCurrent24StatInvBerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomBerLinePreFecCurrent24StatInvBerPortn.setStatus("current")
_Pm10010mptPerfTelecomBerLinePreFecCurrent24StatBerValuePortn_Type = Unsigned32
_Pm10010mptPerfTelecomBerLinePreFecCurrent24StatBerValuePortn_Object = MibTableColumn
pm10010mptPerfTelecomBerLinePreFecCurrent24StatBerValuePortn = _Pm10010mptPerfTelecomBerLinePreFecCurrent24StatBerValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 210, 1, 3),
    _Pm10010mptPerfTelecomBerLinePreFecCurrent24StatBerValuePortn_Type()
)
pm10010mptPerfTelecomBerLinePreFecCurrent24StatBerValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomBerLinePreFecCurrent24StatBerValuePortn.setStatus("current")
_Pm10010mptPerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn_Type = EkiOnOff
_Pm10010mptPerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn_Object = MibTableColumn
pm10010mptPerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn = _Pm10010mptPerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 210, 1, 4),
    _Pm10010mptPerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn_Type()
)
pm10010mptPerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn.setStatus("current")
_Pm10010mptPerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn_Type = Unsigned32
_Pm10010mptPerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn_Object = MibTableColumn
pm10010mptPerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn = _Pm10010mptPerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 210, 1, 5),
    _Pm10010mptPerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn_Type()
)
pm10010mptPerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn.setStatus("current")
_Pm10010mptPerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn_Type = EkiOnOff
_Pm10010mptPerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn_Object = MibTableColumn
pm10010mptPerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn = _Pm10010mptPerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 210, 1, 6),
    _Pm10010mptPerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn_Type()
)
pm10010mptPerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn.setStatus("current")
_Pm10010mptPerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn_Type = Unsigned32
_Pm10010mptPerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn_Object = MibTableColumn
pm10010mptPerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn = _Pm10010mptPerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 210, 1, 7),
    _Pm10010mptPerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn_Type()
)
pm10010mptPerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn.setStatus("current")
_Pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryPort1Table_Object = MibTable
pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryPort1Table = _Pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 211)
)
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryPort1Table.setStatus("current")
_Pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryPort1Entry_Object = MibTableRow
pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryPort1Entry = _Pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 211, 1)
)
pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm10010mpt-MIB", "pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryPort1Entry.setStatus("current")


class _Pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryPort1Index_Type(Integer32):
    """Custom type pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryPort1Index_Object = MibTableColumn
pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryPort1Index = _Pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 211, 1, 1),
    _Pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryPort1Index_Type()
)
pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryPort1Index.setStatus("current")
_Pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1_Type = EkiOnOff
_Pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1_Object = MibTableColumn
pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1 = _Pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 211, 1, 2),
    _Pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1_Type()
)
pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1.setStatus("current")
_Pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1_Type = Unsigned32
_Pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1_Object = MibTableColumn
pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1 = _Pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 211, 1, 3),
    _Pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1_Type()
)
pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1.setStatus("current")
_Pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1_Type = EkiOnOff
_Pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1_Object = MibTableColumn
pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1 = _Pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 211, 1, 4),
    _Pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1_Type()
)
pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1.setStatus("current")
_Pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1_Type = Unsigned32
_Pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1_Object = MibTableColumn
pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1 = _Pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 211, 1, 5),
    _Pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1_Type()
)
pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1.setStatus("current")
_Pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1_Type = EkiOnOff
_Pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1_Object = MibTableColumn
pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1 = _Pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 211, 1, 6),
    _Pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1_Type()
)
pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1.setStatus("current")
_Pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1_Type = Unsigned32
_Pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1_Object = MibTableColumn
pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1 = _Pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 60, 11, 7, 211, 1, 7),
    _Pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1_Type()
)
pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1.setStatus("current")

# Managed Objects groups


# Notification objects

pm10010mptLineTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 60, 10, 30)
)
pm10010mptLineTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm10010mpt-MIB", "pm10010mptAlmLineDdmWarningPortn"),
        ("EKINOPS-Pm10010mpt-MIB", "pm10010mpttrapLineNumber"),
        ("EKINOPS-Pm10010mpt-MIB", "pm10010mpttrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10010mptLineTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pm10010mptLineTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 60, 10, 31)
)
pm10010mptLineTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm10010mpt-MIB", "pm10010mptAlmLineDdmWarningPortn"),
        ("EKINOPS-Pm10010mpt-MIB", "pm10010mpttrapLineNumber"),
        ("EKINOPS-Pm10010mpt-MIB", "pm10010mpttrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10010mptLineTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pm10010mptLineTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 60, 10, 32)
)
pm10010mptLineTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm10010mpt-MIB", "pm10010mptAlmLineDdmAlmPortn"),
        ("EKINOPS-Pm10010mpt-MIB", "pm10010mpttrapLineNumber"),
        ("EKINOPS-Pm10010mpt-MIB", "pm10010mpttrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10010mptLineTrapUrgentGoesOn.setStatus(
        "current"
    )

pm10010mptLineTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 60, 10, 33)
)
pm10010mptLineTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm10010mpt-MIB", "pm10010mptAlmLineDdmAlmPortn"),
        ("EKINOPS-Pm10010mpt-MIB", "pm10010mpttrapLineNumber"),
        ("EKINOPS-Pm10010mpt-MIB", "pm10010mpttrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10010mptLineTrapUrgentGoesOff.setStatus(
        "current"
    )

pm10010mptLineTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 60, 10, 34)
)
pm10010mptLineTrapCritGoesOn.setObjects(
      *(("EKINOPS-Pm10010mpt-MIB", "pm10010mptAlmLineFailPortn"),
        ("EKINOPS-Pm10010mpt-MIB", "pm10010mptAlmLineHwFailPortn"),
        ("EKINOPS-Pm10010mpt-MIB", "pm10010mpttrapLineNumber"),
        ("EKINOPS-Pm10010mpt-MIB", "pm10010mpttrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10010mptLineTrapCritGoesOn.setStatus(
        "current"
    )

pm10010mptLineTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 60, 10, 35)
)
pm10010mptLineTrapCritGoesOff.setObjects(
      *(("EKINOPS-Pm10010mpt-MIB", "pm10010mptAlmLineFailPortn"),
        ("EKINOPS-Pm10010mpt-MIB", "pm10010mptAlmLineHwFailPortn"),
        ("EKINOPS-Pm10010mpt-MIB", "pm10010mpttrapLineNumber"),
        ("EKINOPS-Pm10010mpt-MIB", "pm10010mpttrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10010mptLineTrapCritGoesOff.setStatus(
        "current"
    )

pm10010mptClientTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 60, 10, 40)
)
pm10010mptClientTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm10010mpt-MIB", "pm10010mptAlmSfpDdmWarningPortn"),
        ("EKINOPS-Pm10010mpt-MIB", "pm10010mpttrapPortNumber"),
        ("EKINOPS-Pm10010mpt-MIB", "pm10010mpttrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10010mptClientTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pm10010mptClientTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 60, 10, 41)
)
pm10010mptClientTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm10010mpt-MIB", "pm10010mptAlmSfpDdmWarningPortn"),
        ("EKINOPS-Pm10010mpt-MIB", "pm10010mpttrapPortNumber"),
        ("EKINOPS-Pm10010mpt-MIB", "pm10010mpttrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10010mptClientTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pm10010mptClientTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 60, 10, 42)
)
pm10010mptClientTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm10010mpt-MIB", "pm10010mptAlmSfpDdmAlmPortn"),
        ("EKINOPS-Pm10010mpt-MIB", "pm10010mpttrapPortNumber"),
        ("EKINOPS-Pm10010mpt-MIB", "pm10010mpttrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10010mptClientTrapUrgentGoesOn.setStatus(
        "current"
    )

pm10010mptClientTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 60, 10, 43)
)
pm10010mptClientTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm10010mpt-MIB", "pm10010mptAlmSfpDdmAlmPortn"),
        ("EKINOPS-Pm10010mpt-MIB", "pm10010mpttrapPortNumber"),
        ("EKINOPS-Pm10010mpt-MIB", "pm10010mpttrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10010mptClientTrapUrgentGoesOff.setStatus(
        "current"
    )

pm10010mptClientTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 60, 10, 44)
)
pm10010mptClientTrapCritGoesOn.setObjects(
      *(("EKINOPS-Pm10010mpt-MIB", "pm10010mptAlmFailAccPortn"),
        ("EKINOPS-Pm10010mpt-MIB", "pm10010mptAlmHwFailAccPortn"),
        ("EKINOPS-Pm10010mpt-MIB", "pm10010mpttrapPortNumber"),
        ("EKINOPS-Pm10010mpt-MIB", "pm10010mpttrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10010mptClientTrapCritGoesOn.setStatus(
        "current"
    )

pm10010mptClientTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 60, 10, 45)
)
pm10010mptClientTrapCritGoesOff.setObjects(
      *(("EKINOPS-Pm10010mpt-MIB", "pm10010mptAlmFailAccPortn"),
        ("EKINOPS-Pm10010mpt-MIB", "pm10010mptAlmHwFailAccPortn"),
        ("EKINOPS-Pm10010mpt-MIB", "pm10010mpttrapPortNumber"),
        ("EKINOPS-Pm10010mpt-MIB", "pm10010mpttrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10010mptClientTrapCritGoesOff.setStatus(
        "current"
    )

pm10010mptPowerTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 60, 10, 50)
)
pm10010mptPowerTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm10010mpt-MIB", "pm10010mptAlmDefFuseB"),
        ("EKINOPS-Pm10010mpt-MIB", "pm10010mptAlmDefFuseA"),
        ("EKINOPS-Pm10010mpt-MIB", "pm10010mpttrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10010mptPowerTrapUrgentGoesOn.setStatus(
        "current"
    )

pm10010mptPowerTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 60, 10, 51)
)
pm10010mptPowerTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm10010mpt-MIB", "pm10010mptAlmDefFuseB"),
        ("EKINOPS-Pm10010mpt-MIB", "pm10010mptAlmDefFuseA"),
        ("EKINOPS-Pm10010mpt-MIB", "pm10010mpttrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10010mptPowerTrapUrgentGoesOff.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EKINOPS-Pm10010mpt-MIB",
    **{"Pm10010mptMultiRate": Pm10010mptMultiRate,
       "Pm10010mptOtxMode": Pm10010mptOtxMode,
       "Pm10010mptOtxGrid": Pm10010mptOtxGrid,
       "Pm10010mptAdjustValue": Pm10010mptAdjustValue,
       "Pm10010mptClientProtocol": Pm10010mptClientProtocol,
       "Pm10010mptProtocolMode": Pm10010mptProtocolMode,
       "Pm10010mptOtxChannel": Pm10010mptOtxChannel,
       "Pm10010mptOrxChannel": Pm10010mptOrxChannel,
       "Rm10010ClientIgnoreTimer": Rm10010ClientIgnoreTimer,
       "modulePm10010mpt": modulePm10010mpt,
       "pm10010mptalarms": pm10010mptalarms,
       "pm10010mptAlmOther": pm10010mptAlmOther,
       "pm10010mptAlmOtherNurg": pm10010mptAlmOtherNurg,
       "pm10010mptAlmsynthAlm2": pm10010mptAlmsynthAlm2,
       "pm10010mptAlmConfTableSave": pm10010mptAlmConfTableSave,
       "pm10010mptAlmInvUpload": pm10010mptAlmInvUpload,
       "pm10010mptAlmConfTableLoad": pm10010mptAlmConfTableLoad,
       "pm10010mptAlmCorrelatOff": pm10010mptAlmCorrelatOff,
       "pm10010mptAlmMaintenanceOn": pm10010mptAlmMaintenanceOn,
       "pm10010mptAlmOtherUrg": pm10010mptAlmOtherUrg,
       "pm10010mptAlmOtherCrit": pm10010mptAlmOtherCrit,
       "pm10010mptAlmsynthAlm0": pm10010mptAlmsynthAlm0,
       "pm10010mptAlmFailFan": pm10010mptAlmFailFan,
       "pm10010mptAlmModGlobFail": pm10010mptAlmModGlobFail,
       "pm10010mptAlmDefFuseA": pm10010mptAlmDefFuseA,
       "pm10010mptAlmDefFuseB": pm10010mptAlmDefFuseB,
       "pm10010mptAlmclientModuleState": pm10010mptAlmclientModuleState,
       "pm10010mptAlmCfpInitialize": pm10010mptAlmCfpInitialize,
       "pm10010mptAlmCfpLowPower": pm10010mptAlmCfpLowPower,
       "pm10010mptAlmCfpHighPowerUp": pm10010mptAlmCfpHighPowerUp,
       "pm10010mptAlmCfpTxOff": pm10010mptAlmCfpTxOff,
       "pm10010mptAlmCfpTxTurnOn": pm10010mptAlmCfpTxTurnOn,
       "pm10010mptAlmCfpReady": pm10010mptAlmCfpReady,
       "pm10010mptAlmCfpFault": pm10010mptAlmCfpFault,
       "pm10010mptAlmCfpTxTurnOff": pm10010mptAlmCfpTxTurnOff,
       "pm10010mptAlmCfpHighPowerDown": pm10010mptAlmCfpHighPowerDown,
       "pm10010mptAlmclientModuleGeneralStatus": pm10010mptAlmclientModuleGeneralStatus,
       "pm10010mptAlmCfpOutOfAlignment": pm10010mptAlmCfpOutOfAlignment,
       "pm10010mptAlmCfpRxNetworkLol": pm10010mptAlmCfpRxNetworkLol,
       "pm10010mptAlmCfpRxLos": pm10010mptAlmCfpRxLos,
       "pm10010mptAlmCfpTxHostLol": pm10010mptAlmCfpTxHostLol,
       "pm10010mptAlmCfpTxLosf": pm10010mptAlmCfpTxLosf,
       "pm10010mptAlmCfpTxCmuLol": pm10010mptAlmCfpTxCmuLol,
       "pm10010mptAlmCfpTxJitterPllLol": pm10010mptAlmCfpTxJitterPllLol,
       "pm10010mptAlmCfpLossOfRefclk": pm10010mptAlmCfpLossOfRefclk,
       "pm10010mptAlmCfpHwInterlock": pm10010mptAlmCfpHwInterlock,
       "pm10010mptAlmclientGlobalAlarmSummary": pm10010mptAlmclientGlobalAlarmSummary,
       "pm10010mptAlmCfpSoftGlobAlarmTest": pm10010mptAlmCfpSoftGlobAlarmTest,
       "pm10010mptAlmCfpNetworkLaneAlarmWarning2": pm10010mptAlmCfpNetworkLaneAlarmWarning2,
       "pm10010mptAlmCfpModuleState": pm10010mptAlmCfpModuleState,
       "pm10010mptAlmCfpModuleGeneralStatus": pm10010mptAlmCfpModuleGeneralStatus,
       "pm10010mptAlmCfpModuleFault": pm10010mptAlmCfpModuleFault,
       "pm10010mptAlmCfpModuleAlarmWarning1": pm10010mptAlmCfpModuleAlarmWarning1,
       "pm10010mptAlmCfpModuleAlarmWarning2": pm10010mptAlmCfpModuleAlarmWarning2,
       "pm10010mptAlmCfpNetworkLaneAlarmWarning1": pm10010mptAlmCfpNetworkLaneAlarmWarning1,
       "pm10010mptAlmCfpNetworkLaneFaultStatus": pm10010mptAlmCfpNetworkLaneFaultStatus,
       "pm10010mptAlmCfpHostLaneFaultStatus": pm10010mptAlmCfpHostLaneFaultStatus,
       "pm10010mptAlmCfpGlobAlarmAssertion": pm10010mptAlmCfpGlobAlarmAssertion,
       "pm10010mptAlmmsaModuleState": pm10010mptAlmmsaModuleState,
       "pm10010mptAlmMsaInitialize": pm10010mptAlmMsaInitialize,
       "pm10010mptAlmMsaLowPower": pm10010mptAlmMsaLowPower,
       "pm10010mptAlmMsaHighPowerUp": pm10010mptAlmMsaHighPowerUp,
       "pm10010mptAlmMsaTxOff": pm10010mptAlmMsaTxOff,
       "pm10010mptAlmMsaTxTurnOn": pm10010mptAlmMsaTxTurnOn,
       "pm10010mptAlmMsaReady": pm10010mptAlmMsaReady,
       "pm10010mptAlmMsaFault": pm10010mptAlmMsaFault,
       "pm10010mptAlmMsaTxTurnOff": pm10010mptAlmMsaTxTurnOff,
       "pm10010mptAlmMsaHighPowerDown": pm10010mptAlmMsaHighPowerDown,
       "pm10010mptAlmmsaModuleGeneralStatus": pm10010mptAlmmsaModuleGeneralStatus,
       "pm10010mptAlmMsaOutOfAlignment": pm10010mptAlmMsaOutOfAlignment,
       "pm10010mptAlmMsaRxNetworkLol": pm10010mptAlmMsaRxNetworkLol,
       "pm10010mptAlmMsaRxLos": pm10010mptAlmMsaRxLos,
       "pm10010mptAlmMsaTxHostLol": pm10010mptAlmMsaTxHostLol,
       "pm10010mptAlmMsaTxLosf": pm10010mptAlmMsaTxLosf,
       "pm10010mptAlmMsaTxCmuLol": pm10010mptAlmMsaTxCmuLol,
       "pm10010mptAlmMsaTxJitterPllLol": pm10010mptAlmMsaTxJitterPllLol,
       "pm10010mptAlmMsaLossOfRefclk": pm10010mptAlmMsaLossOfRefclk,
       "pm10010mptAlmMsaHwInterlock": pm10010mptAlmMsaHwInterlock,
       "pm10010mptAlmmsaGlobalAlarmSummary": pm10010mptAlmmsaGlobalAlarmSummary,
       "pm10010mptAlmMsaSoftGlobAlarmTest": pm10010mptAlmMsaSoftGlobAlarmTest,
       "pm10010mptAlmMsaNetworkHostAlarmStatus": pm10010mptAlmMsaNetworkHostAlarmStatus,
       "pm10010mptAlmMsaNetworkLaneAlarmWarning2": pm10010mptAlmMsaNetworkLaneAlarmWarning2,
       "pm10010mptAlmMsaModuleState": pm10010mptAlmMsaModuleState,
       "pm10010mptAlmMsaModuleGeneralStatus": pm10010mptAlmMsaModuleGeneralStatus,
       "pm10010mptAlmModuleFault": pm10010mptAlmModuleFault,
       "pm10010mptAlmMsaModuleAlarmWarning1": pm10010mptAlmMsaModuleAlarmWarning1,
       "pm10010mptAlmMsaModuleAlarmWarning2": pm10010mptAlmMsaModuleAlarmWarning2,
       "pm10010mptAlmMsaNetworkLaneAlarmWarning1": pm10010mptAlmMsaNetworkLaneAlarmWarning1,
       "pm10010mptAlmMsaNetworkLaneFaultStatus": pm10010mptAlmMsaNetworkLaneFaultStatus,
       "pm10010mptAlmMsaHostLaneFaultStatus": pm10010mptAlmMsaHostLaneFaultStatus,
       "pm10010mptAlmMsaGlobAlarmAssertion": pm10010mptAlmMsaGlobAlarmAssertion,
       "pm10010mptAlmmsaNetworkTxAlignment": pm10010mptAlmmsaNetworkTxAlignment,
       "pm10010mptAlmNetTxTimingFault": pm10010mptAlmNetTxTimingFault,
       "pm10010mptAlmNetTxReferenceClockFault": pm10010mptAlmNetTxReferenceClockFault,
       "pm10010mptAlmNetTxCmuLockFault": pm10010mptAlmNetTxCmuLockFault,
       "pm10010mptAlmNetTxOutOfAlignment": pm10010mptAlmNetTxOutOfAlignment,
       "pm10010mptAlmNetTxLossOfAlignment": pm10010mptAlmNetTxLossOfAlignment,
       "pm10010mptAlmmsaNetworkRxAlignment": pm10010mptAlmmsaNetworkRxAlignment,
       "pm10010mptAlmNetRxTimingFault": pm10010mptAlmNetRxTimingFault,
       "pm10010mptAlmNetRxOutOfAlignment": pm10010mptAlmNetRxOutOfAlignment,
       "pm10010mptAlmNetRxLossOfAlignment": pm10010mptAlmNetRxLossOfAlignment,
       "pm10010mptAlmNetRxModemLockFault": pm10010mptAlmNetRxModemLockFault,
       "pm10010mptAlmNetRxModemSyncDetectFault": pm10010mptAlmNetRxModemSyncDetectFault,
       "pm10010mptAlmmsaNetworkHostNetworkAlarmSummary": pm10010mptAlmmsaNetworkHostNetworkAlarmSummary,
       "pm10010mptAlmNetworkTxAlignment": pm10010mptAlmNetworkTxAlignment,
       "pm10010mptAlmNetworkRxAlignment": pm10010mptAlmNetworkRxAlignment,
       "pm10010mptAlmNetworkRxOtn": pm10010mptAlmNetworkRxOtn,
       "pm10010mptAlmHostRxAlignment": pm10010mptAlmHostRxAlignment,
       "pm10010mptAlmHostTxAlignment": pm10010mptAlmHostTxAlignment,
       "pm10010mptAlmHostTxOtnStatus": pm10010mptAlmHostTxOtnStatus,
       "pm10010mptAlmmsaHostTxAlignment": pm10010mptAlmmsaHostTxAlignment,
       "pm10010mptAlmHostTxDeskewLockFault": pm10010mptAlmHostTxDeskewLockFault,
       "pm10010mptAlmHostTxOutOfAlignment": pm10010mptAlmHostTxOutOfAlignment,
       "pm10010mptAlmHostTxLossOfAlignment": pm10010mptAlmHostTxLossOfAlignment,
       "pm10010mptAlmHostTxCdrLockFault": pm10010mptAlmHostTxCdrLockFault,
       "pm10010mptAlmmsaHostRxAlignment": pm10010mptAlmmsaHostRxAlignment,
       "pm10010mptAlmHostRxCmuLockFault": pm10010mptAlmHostRxCmuLockFault,
       "pm10010mptAlmHostRxOutOfAlignment": pm10010mptAlmHostRxOutOfAlignment,
       "pm10010mptAlmHostRxLossOfAlignment": pm10010mptAlmHostRxLossOfAlignment,
       "pm10010mptAlmClient": pm10010mptAlmClient,
       "pm10010mptAlmClientNurg": pm10010mptAlmClientNurg,
       "pm10010mptAlmclientNetworkLaneAlarmWarningTable": pm10010mptAlmclientNetworkLaneAlarmWarningTable,
       "pm10010mptAlmclientNetworkLaneAlarmWarningEntry": pm10010mptAlmclientNetworkLaneAlarmWarningEntry,
       "pm10010mptAlmclientNetworkLaneAlarmWarningIndex": pm10010mptAlmclientNetworkLaneAlarmWarningIndex,
       "pm10010mptAlmClientRxPowerLowAlarmPortn": pm10010mptAlmClientRxPowerLowAlarmPortn,
       "pm10010mptAlmClientRxPowerLowWarningPortn": pm10010mptAlmClientRxPowerLowWarningPortn,
       "pm10010mptAlmClientRxPowerHighWarningPortn": pm10010mptAlmClientRxPowerHighWarningPortn,
       "pm10010mptAlmClientRxPowerHighAlarmPortn": pm10010mptAlmClientRxPowerHighAlarmPortn,
       "pm10010mptAlmLaserTempLowAlarmPortn": pm10010mptAlmLaserTempLowAlarmPortn,
       "pm10010mptAlmClientLaserTempLowWarningPortn": pm10010mptAlmClientLaserTempLowWarningPortn,
       "pm10010mptAlmClientLaserTempHighWarningPortn": pm10010mptAlmClientLaserTempHighWarningPortn,
       "pm10010mptAlmClientLaserTempHighAlarmPortn": pm10010mptAlmClientLaserTempHighAlarmPortn,
       "pm10010mptAlmClientTxPowerLowAlarmPortn": pm10010mptAlmClientTxPowerLowAlarmPortn,
       "pm10010mptAlmClientTxPowerLowWarningPortn": pm10010mptAlmClientTxPowerLowWarningPortn,
       "pm10010mptAlmClientTxPowerHighWarningPortn": pm10010mptAlmClientTxPowerHighWarningPortn,
       "pm10010mptAlmClientTxPowerHighAlarmPortn": pm10010mptAlmClientTxPowerHighAlarmPortn,
       "pm10010mptAlmClientBiasLowAlarmPortn": pm10010mptAlmClientBiasLowAlarmPortn,
       "pm10010mptAlmClientBiasLowWarningPortn": pm10010mptAlmClientBiasLowWarningPortn,
       "pm10010mptAlmClientBiasHighWarningPortn": pm10010mptAlmClientBiasHighWarningPortn,
       "pm10010mptAlmClientBiasHighAlarmPortn": pm10010mptAlmClientBiasHighAlarmPortn,
       "pm10010mptAlmclientSfpWarnDdmTable": pm10010mptAlmclientSfpWarnDdmTable,
       "pm10010mptAlmclientSfpWarnDdmEntry": pm10010mptAlmclientSfpWarnDdmEntry,
       "pm10010mptAlmclientSfpWarnDdmIndex": pm10010mptAlmclientSfpWarnDdmIndex,
       "pm10010mptAlmTxPwLowWngPortn": pm10010mptAlmTxPwLowWngPortn,
       "pm10010mptAlmTxPwrHighWngPortn": pm10010mptAlmTxPwrHighWngPortn,
       "pm10010mptAlmTxBiasLowWngPortn": pm10010mptAlmTxBiasLowWngPortn,
       "pm10010mptAlmTxBiasHighWngPortn": pm10010mptAlmTxBiasHighWngPortn,
       "pm10010mptAlmVccLowWngPortn": pm10010mptAlmVccLowWngPortn,
       "pm10010mptAlmVccHighWngPortn": pm10010mptAlmVccHighWngPortn,
       "pm10010mptAlmTempLowWngPortn": pm10010mptAlmTempLowWngPortn,
       "pm10010mptAlmTempHighWngPortn": pm10010mptAlmTempHighWngPortn,
       "pm10010mptAlmRxPwrLowWngPortn": pm10010mptAlmRxPwrLowWngPortn,
       "pm10010mptAlmRxPwrHighWngPortn": pm10010mptAlmRxPwrHighWngPortn,
       "pm10010mptAlmClientUrg": pm10010mptAlmClientUrg,
       "pm10010mptAlmclientNetworkLaneFaultTable": pm10010mptAlmclientNetworkLaneFaultTable,
       "pm10010mptAlmclientNetworkLaneFaultEntry": pm10010mptAlmclientNetworkLaneFaultEntry,
       "pm10010mptAlmclientNetworkLaneFaultIndex": pm10010mptAlmclientNetworkLaneFaultIndex,
       "pm10010mptAlmClientLaneRxFifoErrorPortn": pm10010mptAlmClientLaneRxFifoErrorPortn,
       "pm10010mptAlmClientLaneRxLolPortn": pm10010mptAlmClientLaneRxLolPortn,
       "pm10010mptAlmClientLaneRxLosPortn": pm10010mptAlmClientLaneRxLosPortn,
       "pm10010mptAlmClientLaneTxLolPortn": pm10010mptAlmClientLaneTxLolPortn,
       "pm10010mptAlmClientLaneTxLosfPortn": pm10010mptAlmClientLaneTxLosfPortn,
       "pm10010mptAlmClientLaneApdPowerSupplyPortn": pm10010mptAlmClientLaneApdPowerSupplyPortn,
       "pm10010mptAlmClientLaneWavelengthUnlockedPortn": pm10010mptAlmClientLaneWavelengthUnlockedPortn,
       "pm10010mptAlmClientLaneTecFaultPortn": pm10010mptAlmClientLaneTecFaultPortn,
       "pm10010mptAlmclientHostLaneFaultTable": pm10010mptAlmclientHostLaneFaultTable,
       "pm10010mptAlmclientHostLaneFaultEntry": pm10010mptAlmclientHostLaneFaultEntry,
       "pm10010mptAlmclientHostLaneFaultIndex": pm10010mptAlmclientHostLaneFaultIndex,
       "pm10010mptAlmClientLossOfSyncPortn": pm10010mptAlmClientLossOfSyncPortn,
       "pm10010mptAlmClientInputLossOfSigPortn": pm10010mptAlmClientInputLossOfSigPortn,
       "pm10010mptAlmClientLanesMarkerUnlockPortn": pm10010mptAlmClientLanesMarkerUnlockPortn,
       "pm10010mptAlmClientLanes6466UnlockPortn": pm10010mptAlmClientLanes6466UnlockPortn,
       "pm10010mptAlmClientLanesNotAlignedPortn": pm10010mptAlmClientLanesNotAlignedPortn,
       "pm10010mptAlmClientCsfDetectedPortn": pm10010mptAlmClientCsfDetectedPortn,
       "pm10010mptAlmClientTxHostLolPortn": pm10010mptAlmClientTxHostLolPortn,
       "pm10010mptAlmClientLaneTxFifoErrorPortn": pm10010mptAlmClientLaneTxFifoErrorPortn,
       "pm10010mptAlmLfDetectedPortn": pm10010mptAlmLfDetectedPortn,
       "pm10010mptAlmRfDetectedPortn": pm10010mptAlmRfDetectedPortn,
       "pm10010mptAlmclientSfpAlmDdmTable": pm10010mptAlmclientSfpAlmDdmTable,
       "pm10010mptAlmclientSfpAlmDdmEntry": pm10010mptAlmclientSfpAlmDdmEntry,
       "pm10010mptAlmclientSfpAlmDdmIndex": pm10010mptAlmclientSfpAlmDdmIndex,
       "pm10010mptAlmTxPwrLowAlaPortn": pm10010mptAlmTxPwrLowAlaPortn,
       "pm10010mptAlmTxPwrHighAlaPortn": pm10010mptAlmTxPwrHighAlaPortn,
       "pm10010mptAlmTxBiasLowAlaPortn": pm10010mptAlmTxBiasLowAlaPortn,
       "pm10010mptAlmTxBiasHighAlaPortn": pm10010mptAlmTxBiasHighAlaPortn,
       "pm10010mptAlmVccLowAlaPortn": pm10010mptAlmVccLowAlaPortn,
       "pm10010mptAlmVccHighAlaPortn": pm10010mptAlmVccHighAlaPortn,
       "pm10010mptAlmTempLowAlaPortn": pm10010mptAlmTempLowAlaPortn,
       "pm10010mptAlmTempHighAlaPortn": pm10010mptAlmTempHighAlaPortn,
       "pm10010mptAlmRxPwrLowAlaPortn": pm10010mptAlmRxPwrLowAlaPortn,
       "pm10010mptAlmRxPwrHighAlaPortn": pm10010mptAlmRxPwrHighAlaPortn,
       "pm10010mptAlmClientCrit": pm10010mptAlmClientCrit,
       "pm10010mptAlmsynthAlmPortTable": pm10010mptAlmsynthAlmPortTable,
       "pm10010mptAlmsynthAlmPortEntry": pm10010mptAlmsynthAlmPortEntry,
       "pm10010mptAlmsynthAlmPortIndex": pm10010mptAlmsynthAlmPortIndex,
       "pm10010mptAlmSfpAbsentPortn": pm10010mptAlmSfpAbsentPortn,
       "pm10010mptAlmDdmAbsentPortn": pm10010mptAlmDdmAbsentPortn,
       "pm10010mptAlmHwFailAccPortn": pm10010mptAlmHwFailAccPortn,
       "pm10010mptAlmDwLsdPortn": pm10010mptAlmDwLsdPortn,
       "pm10010mptAlmClientLocalOosPortn": pm10010mptAlmClientLocalOosPortn,
       "pm10010mptAlmClientRemoteOosPortn": pm10010mptAlmClientRemoteOosPortn,
       "pm10010mptAlmDwCaisPortn": pm10010mptAlmDwCaisPortn,
       "pm10010mptAlmSfpDdmWarningPortn": pm10010mptAlmSfpDdmWarningPortn,
       "pm10010mptAlmSfpDdmAlmPortn": pm10010mptAlmSfpDdmAlmPortn,
       "pm10010mptAlmIdleInsertedPortn": pm10010mptAlmIdleInsertedPortn,
       "pm10010mptAlmFailAccPortn": pm10010mptAlmFailAccPortn,
       "pm10010mptAlmUpCsfPortn": pm10010mptAlmUpCsfPortn,
       "pm10010mptAlmLine": pm10010mptAlmLine,
       "pm10010mptAlmLineNurg": pm10010mptAlmLineNurg,
       "pm10010mptAlmlineNetworkLaneAlarmWarning1Table": pm10010mptAlmlineNetworkLaneAlarmWarning1Table,
       "pm10010mptAlmlineNetworkLaneAlarmWarning1Entry": pm10010mptAlmlineNetworkLaneAlarmWarning1Entry,
       "pm10010mptAlmlineNetworkLaneAlarmWarning1Index": pm10010mptAlmlineNetworkLaneAlarmWarning1Index,
       "pm10010mptAlmLineRxPowerLowAlarmPortn": pm10010mptAlmLineRxPowerLowAlarmPortn,
       "pm10010mptAlmLineRxPowerLowWarningPortn": pm10010mptAlmLineRxPowerLowWarningPortn,
       "pm10010mptAlmLineRxPowerHighWarningPortn": pm10010mptAlmLineRxPowerHighWarningPortn,
       "pm10010mptAlmLineRxPowerHighAlarmPortn": pm10010mptAlmLineRxPowerHighAlarmPortn,
       "pm10010mptAlmLineLaserTempLowAlarmPortn": pm10010mptAlmLineLaserTempLowAlarmPortn,
       "pm10010mptAlmLineLaserTempLowWarningPortn": pm10010mptAlmLineLaserTempLowWarningPortn,
       "pm10010mptAlmLineLaserTempHighWarningPortn": pm10010mptAlmLineLaserTempHighWarningPortn,
       "pm10010mptAlmLineLaserTempHighAlarmPortn": pm10010mptAlmLineLaserTempHighAlarmPortn,
       "pm10010mptAlmLineTxPowerLowAlarmPortn": pm10010mptAlmLineTxPowerLowAlarmPortn,
       "pm10010mptAlmLineTxPowerLowWarningPortn": pm10010mptAlmLineTxPowerLowWarningPortn,
       "pm10010mptAlmLineTxPowerHighWarningPortn": pm10010mptAlmLineTxPowerHighWarningPortn,
       "pm10010mptAlmLineTxPowerHighAlarmPortn": pm10010mptAlmLineTxPowerHighAlarmPortn,
       "pm10010mptAlmLineBiasLowAlarmPortn": pm10010mptAlmLineBiasLowAlarmPortn,
       "pm10010mptAlmLineBiasLowWarningPortn": pm10010mptAlmLineBiasLowWarningPortn,
       "pm10010mptAlmLineBiasHighWarningPortn": pm10010mptAlmLineBiasHighWarningPortn,
       "pm10010mptAlmLineBiasHighAlarmPortn": pm10010mptAlmLineBiasHighAlarmPortn,
       "pm10010mptAlmlineNetworkLaneAlarmWarning2Table": pm10010mptAlmlineNetworkLaneAlarmWarning2Table,
       "pm10010mptAlmlineNetworkLaneAlarmWarning2Entry": pm10010mptAlmlineNetworkLaneAlarmWarning2Entry,
       "pm10010mptAlmlineNetworkLaneAlarmWarning2Index": pm10010mptAlmlineNetworkLaneAlarmWarning2Index,
       "pm10010mptAlmTxModulatorBiasLowAlarmPortn": pm10010mptAlmTxModulatorBiasLowAlarmPortn,
       "pm10010mptAlmTxModulatorBiasLowWarningPortn": pm10010mptAlmTxModulatorBiasLowWarningPortn,
       "pm10010mptAlmTxModulatorBiasHighWarningPortn": pm10010mptAlmTxModulatorBiasHighWarningPortn,
       "pm10010mptAlmTxModulatorBiasHighAlarmPortn": pm10010mptAlmTxModulatorBiasHighAlarmPortn,
       "pm10010mptAlmRxLaserTempLowAlarmPortn": pm10010mptAlmRxLaserTempLowAlarmPortn,
       "pm10010mptAlmRxLaserTempLowWarningPortn": pm10010mptAlmRxLaserTempLowWarningPortn,
       "pm10010mptAlmRxLaserTempHighWarningPortn": pm10010mptAlmRxLaserTempHighWarningPortn,
       "pm10010mptAlmRxLaserTempHighAlarmPortn": pm10010mptAlmRxLaserTempHighAlarmPortn,
       "pm10010mptAlmRxLaserOutputLowAlarmPortn": pm10010mptAlmRxLaserOutputLowAlarmPortn,
       "pm10010mptAlmRxLaserOutputLowWarningPortn": pm10010mptAlmRxLaserOutputLowWarningPortn,
       "pm10010mptAlmRxLaserOutputHighWarningPortn": pm10010mptAlmRxLaserOutputHighWarningPortn,
       "pm10010mptAlmRxLaserOutputHighAlarmPortn": pm10010mptAlmRxLaserOutputHighAlarmPortn,
       "pm10010mptAlmRxLaserBiasLowAlarmPortn": pm10010mptAlmRxLaserBiasLowAlarmPortn,
       "pm10010mptAlmRxLaserBiasLowWarningPortn": pm10010mptAlmRxLaserBiasLowWarningPortn,
       "pm10010mptAlmRxLaserBiasHighWarningPortn": pm10010mptAlmRxLaserBiasHighWarningPortn,
       "pm10010mptAlmRxLaserBiasHighAlarmPortn": pm10010mptAlmRxLaserBiasHighAlarmPortn,
       "pm10010mptAlmLineUrg": pm10010mptAlmLineUrg,
       "pm10010mptAlmlineNetworkLaneFaultTable": pm10010mptAlmlineNetworkLaneFaultTable,
       "pm10010mptAlmlineNetworkLaneFaultEntry": pm10010mptAlmlineNetworkLaneFaultEntry,
       "pm10010mptAlmlineNetworkLaneFaultIndex": pm10010mptAlmlineNetworkLaneFaultIndex,
       "pm10010mptAlmLineLaneRxTecFaultPortn": pm10010mptAlmLineLaneRxTecFaultPortn,
       "pm10010mptAlmLineLaneRxFifoErrorPortn": pm10010mptAlmLineLaneRxFifoErrorPortn,
       "pm10010mptAlmLineLaneRxLolPortn": pm10010mptAlmLineLaneRxLolPortn,
       "pm10010mptAlmLineLaneRxLosPortn": pm10010mptAlmLineLaneRxLosPortn,
       "pm10010mptAlmLineLaneTxLolPortn": pm10010mptAlmLineLaneTxLolPortn,
       "pm10010mptAlmLineLaneTxLosfPortn": pm10010mptAlmLineLaneTxLosfPortn,
       "pm10010mptAlmLineLaneApdPowerSupplyPortn": pm10010mptAlmLineLaneApdPowerSupplyPortn,
       "pm10010mptAlmLineLaneWavelengthUnlockedPortn": pm10010mptAlmLineLaneWavelengthUnlockedPortn,
       "pm10010mptAlmLineLaneTecFaultPortn": pm10010mptAlmLineLaneTecFaultPortn,
       "pm10010mptAlmlineHostLaneFaultTable": pm10010mptAlmlineHostLaneFaultTable,
       "pm10010mptAlmlineHostLaneFaultEntry": pm10010mptAlmlineHostLaneFaultEntry,
       "pm10010mptAlmlineHostLaneFaultIndex": pm10010mptAlmlineHostLaneFaultIndex,
       "pm10010mptAlmLineInputLossOfSignalPortn": pm10010mptAlmLineInputLossOfSignalPortn,
       "pm10010mptAlmLineLossOfFramePortn": pm10010mptAlmLineLossOfFramePortn,
       "pm10010mptAlmLineSmBdiInsertedPortn": pm10010mptAlmLineSmBdiInsertedPortn,
       "pm10010mptAlmLineSmBdiDetectedPortn": pm10010mptAlmLineSmBdiDetectedPortn,
       "pm10010mptAlmLineSmIaeInsertedPortn": pm10010mptAlmLineSmIaeInsertedPortn,
       "pm10010mptAlmLineSmIaeDetectedPortn": pm10010mptAlmLineSmIaeDetectedPortn,
       "pm10010mptAlmLineTxHostLolPortn": pm10010mptAlmLineTxHostLolPortn,
       "pm10010mptAlmLineLaneTxFifoErrorPortn": pm10010mptAlmLineLaneTxFifoErrorPortn,
       "pm10010mptAlmLinePowerDegradePortn": pm10010mptAlmLinePowerDegradePortn,
       "pm10010mptAlmLineTrxOverTempPortn": pm10010mptAlmLineTrxOverTempPortn,
       "pm10010mptAlmlineNetworkLaneRxOtnTable": pm10010mptAlmlineNetworkLaneRxOtnTable,
       "pm10010mptAlmlineNetworkLaneRxOtnEntry": pm10010mptAlmlineNetworkLaneRxOtnEntry,
       "pm10010mptAlmlineNetworkLaneRxOtnIndex": pm10010mptAlmlineNetworkLaneRxOtnIndex,
       "pm10010mptAlmLineRxOtnOduAisPortn": pm10010mptAlmLineRxOtnOduAisPortn,
       "pm10010mptAlmLineRxOtnOtuAisPortn": pm10010mptAlmLineRxOtnOtuAisPortn,
       "pm10010mptAlmLineRxSmBdiPortn": pm10010mptAlmLineRxSmBdiPortn,
       "pm10010mptAlmLineRxOtnIaePortn": pm10010mptAlmLineRxOtnIaePortn,
       "pm10010mptAlmLineRxOtnOomPortn": pm10010mptAlmLineRxOtnOomPortn,
       "pm10010mptAlmLineRxOtnLomPortn": pm10010mptAlmLineRxOtnLomPortn,
       "pm10010mptAlmLineRxOtnOofPortn": pm10010mptAlmLineRxOtnOofPortn,
       "pm10010mptAlmLineRxOtnLofPortn": pm10010mptAlmLineRxOtnLofPortn,
       "pm10010mptAlmlineHostLaneTxOtnTable": pm10010mptAlmlineHostLaneTxOtnTable,
       "pm10010mptAlmlineHostLaneTxOtnEntry": pm10010mptAlmlineHostLaneTxOtnEntry,
       "pm10010mptAlmlineHostLaneTxOtnIndex": pm10010mptAlmlineHostLaneTxOtnIndex,
       "pm10010mptAlmLineTxOtnOduAisPortn": pm10010mptAlmLineTxOtnOduAisPortn,
       "pm10010mptAlmLineTxOtnOtuAisPortn": pm10010mptAlmLineTxOtnOtuAisPortn,
       "pm10010mptAlmLineTxSmBdiPortn": pm10010mptAlmLineTxSmBdiPortn,
       "pm10010mptAlmLineTxOtnIaePortn": pm10010mptAlmLineTxOtnIaePortn,
       "pm10010mptAlmLineTxOtnOomPortn": pm10010mptAlmLineTxOtnOomPortn,
       "pm10010mptAlmLineTxOtnLomPortn": pm10010mptAlmLineTxOtnLomPortn,
       "pm10010mptAlmLineTxOtnOofPortn": pm10010mptAlmLineTxOtnOofPortn,
       "pm10010mptAlmLineTxOtnLofPortn": pm10010mptAlmLineTxOtnLofPortn,
       "pm10010mptAlmLineCrit": pm10010mptAlmLineCrit,
       "pm10010mptAlmsynthAlmLineTable": pm10010mptAlmsynthAlmLineTable,
       "pm10010mptAlmsynthAlmLineEntry": pm10010mptAlmsynthAlmLineEntry,
       "pm10010mptAlmsynthAlmLineIndex": pm10010mptAlmsynthAlmLineIndex,
       "pm10010mptAlmXfpAbsentPortn": pm10010mptAlmXfpAbsentPortn,
       "pm10010mptAlmXfpInitNotComplPortn": pm10010mptAlmXfpInitNotComplPortn,
       "pm10010mptAlmLineHwFailPortn": pm10010mptAlmLineHwFailPortn,
       "pm10010mptAlmXfpTxOffPortn": pm10010mptAlmXfpTxOffPortn,
       "pm10010mptAlmLineLocalOosPortn": pm10010mptAlmLineLocalOosPortn,
       "pm10010mptAlmUpRdiInsPortn": pm10010mptAlmUpRdiInsPortn,
       "pm10010mptAlmLineDdmWarningPortn": pm10010mptAlmLineDdmWarningPortn,
       "pm10010mptAlmLineDdmAlmPortn": pm10010mptAlmLineDdmAlmPortn,
       "pm10010mptAlmLineFailPortn": pm10010mptAlmLineFailPortn,
       "pm10010mptAlmLineActivePortn": pm10010mptAlmLineActivePortn,
       "pm10010mptmeasures": pm10010mptmeasures,
       "pm10010mptMesrOther": pm10010mptMesrOther,
       "pm10010mptMesrsynth0": pm10010mptMesrsynth0,
       "pm10010mptMesrsynth1": pm10010mptMesrsynth1,
       "pm10010mptMesrpmIntervalNumber": pm10010mptMesrpmIntervalNumber,
       "pm10010mptMesrlineNetTxLaserOutputPwrAverage": pm10010mptMesrlineNetTxLaserOutputPwrAverage,
       "pm10010mptMesrlineNetTxLaserTempAverage": pm10010mptMesrlineNetTxLaserTempAverage,
       "pm10010mptMesrlineNetTxBiasCurrentAverage": pm10010mptMesrlineNetTxBiasCurrentAverage,
       "pm10010mptMesrlineNetRxInputPwrAverage": pm10010mptMesrlineNetRxInputPwrAverage,
       "pm10010mptMesrlineResidualChromaticDispAverage": pm10010mptMesrlineResidualChromaticDispAverage,
       "pm10010mptMesrlineDiffGroupDelayAverage": pm10010mptMesrlineDiffGroupDelayAverage,
       "pm10010mptMesrlineQFactorAverage": pm10010mptMesrlineQFactorAverage,
       "pm10010mptMesrlineCarrierFreqOffsetAverage": pm10010mptMesrlineCarrierFreqOffsetAverage,
       "pm10010mptMesrlineOsnrAverage": pm10010mptMesrlineOsnrAverage,
       "pm10010mptMesrclientNetTxTempMin": pm10010mptMesrclientNetTxTempMin,
       "pm10010mptMesrclientNetTxBiasMin": pm10010mptMesrclientNetTxBiasMin,
       "pm10010mptMesrclientNetTxPwrMin": pm10010mptMesrclientNetTxPwrMin,
       "pm10010mptMesrclientNetRxPwrMin": pm10010mptMesrclientNetRxPwrMin,
       "pm10010mptMesrlineNetTxLaserOutputPwrMin": pm10010mptMesrlineNetTxLaserOutputPwrMin,
       "pm10010mptMesrlineNetTxLaserTempMin": pm10010mptMesrlineNetTxLaserTempMin,
       "pm10010mptMesrlineNetTxBiasCurrentMin": pm10010mptMesrlineNetTxBiasCurrentMin,
       "pm10010mptMesrlineNetRxInputPwrMin": pm10010mptMesrlineNetRxInputPwrMin,
       "pm10010mptMesrlineResidualChromaticDispMin": pm10010mptMesrlineResidualChromaticDispMin,
       "pm10010mptMesrlineDiffGroupDelayMin": pm10010mptMesrlineDiffGroupDelayMin,
       "pm10010mptMesrlineQFactorMin": pm10010mptMesrlineQFactorMin,
       "pm10010mptMesrlineCarrierFreqOffsetMin": pm10010mptMesrlineCarrierFreqOffsetMin,
       "pm10010mptMesrlineOsnrMin": pm10010mptMesrlineOsnrMin,
       "pm10010mptMesrclientNetTxTempMax": pm10010mptMesrclientNetTxTempMax,
       "pm10010mptMesrclientNetTxBiasMax": pm10010mptMesrclientNetTxBiasMax,
       "pm10010mptMesrclientNetTxPwrMax": pm10010mptMesrclientNetTxPwrMax,
       "pm10010mptMesrclientNetRxPwrMax": pm10010mptMesrclientNetRxPwrMax,
       "pm10010mptMesrlineNetTxLaserOutputPwrMax": pm10010mptMesrlineNetTxLaserOutputPwrMax,
       "pm10010mptMesrlineNetTxLaserTempMax": pm10010mptMesrlineNetTxLaserTempMax,
       "pm10010mptMesrlineNetTxBiasCurrentMax": pm10010mptMesrlineNetTxBiasCurrentMax,
       "pm10010mptMesrlineNetRxInputPwrMax": pm10010mptMesrlineNetRxInputPwrMax,
       "pm10010mptMesrlineResidualChromaticDispMax": pm10010mptMesrlineResidualChromaticDispMax,
       "pm10010mptMesrlineDiffGroupDelayMax": pm10010mptMesrlineDiffGroupDelayMax,
       "pm10010mptMesrlineQFactorMax": pm10010mptMesrlineQFactorMax,
       "pm10010mptMesrlineCarrierFreqOffsetMax": pm10010mptMesrlineCarrierFreqOffsetMax,
       "pm10010mptMesrlineOsnrMax": pm10010mptMesrlineOsnrMax,
       "pm10010mptMesrClient": pm10010mptMesrClient,
       "pm10010mptMesrclientCfpTemp": pm10010mptMesrclientCfpTemp,
       "pm10010mptMesrclientCfp3v3Voltage": pm10010mptMesrclientCfp3v3Voltage,
       "pm10010mptMesrclientSoaBiasCurrent": pm10010mptMesrclientSoaBiasCurrent,
       "pm10010mptMesrclientNetTxTempTable": pm10010mptMesrclientNetTxTempTable,
       "pm10010mptMesrclientNetTxTempEntry": pm10010mptMesrclientNetTxTempEntry,
       "pm10010mptMesrclientNetTxTempIndex": pm10010mptMesrclientNetTxTempIndex,
       "pm10010mptMesrclientNetTxTempPortn": pm10010mptMesrclientNetTxTempPortn,
       "pm10010mptMesrclientNetTxBiasTable": pm10010mptMesrclientNetTxBiasTable,
       "pm10010mptMesrclientNetTxBiasEntry": pm10010mptMesrclientNetTxBiasEntry,
       "pm10010mptMesrclientNetTxBiasIndex": pm10010mptMesrclientNetTxBiasIndex,
       "pm10010mptMesrclientNetTxBiasPortn": pm10010mptMesrclientNetTxBiasPortn,
       "pm10010mptMesrclientNetTxPwrTable": pm10010mptMesrclientNetTxPwrTable,
       "pm10010mptMesrclientNetTxPwrEntry": pm10010mptMesrclientNetTxPwrEntry,
       "pm10010mptMesrclientNetTxPwrIndex": pm10010mptMesrclientNetTxPwrIndex,
       "pm10010mptMesrclientNetTxPwrPortn": pm10010mptMesrclientNetTxPwrPortn,
       "pm10010mptMesrclientNetRxPwrTable": pm10010mptMesrclientNetRxPwrTable,
       "pm10010mptMesrclientNetRxPwrEntry": pm10010mptMesrclientNetRxPwrEntry,
       "pm10010mptMesrclientNetRxPwrIndex": pm10010mptMesrclientNetRxPwrIndex,
       "pm10010mptMesrclientNetRxPwrPortn": pm10010mptMesrclientNetRxPwrPortn,
       "pm10010mptMesrLine": pm10010mptMesrLine,
       "pm10010mptMesrlineMsaTemp": pm10010mptMesrlineMsaTemp,
       "pm10010mptMesrlineMsa3v3Voltage": pm10010mptMesrlineMsa3v3Voltage,
       "pm10010mptMesrlineSoaBiasCurrent": pm10010mptMesrlineSoaBiasCurrent,
       "pm10010mptMesrlineNetTxLaserOutputPwrTable": pm10010mptMesrlineNetTxLaserOutputPwrTable,
       "pm10010mptMesrlineNetTxLaserOutputPwrEntry": pm10010mptMesrlineNetTxLaserOutputPwrEntry,
       "pm10010mptMesrlineNetTxLaserOutputPwrIndex": pm10010mptMesrlineNetTxLaserOutputPwrIndex,
       "pm10010mptMesrlineNetTxLaserOutputPwrPortn": pm10010mptMesrlineNetTxLaserOutputPwrPortn,
       "pm10010mptMesrlineNetTxLaserTempTable": pm10010mptMesrlineNetTxLaserTempTable,
       "pm10010mptMesrlineNetTxLaserTempEntry": pm10010mptMesrlineNetTxLaserTempEntry,
       "pm10010mptMesrlineNetTxLaserTempIndex": pm10010mptMesrlineNetTxLaserTempIndex,
       "pm10010mptMesrlineNetTxLaserTempPortn": pm10010mptMesrlineNetTxLaserTempPortn,
       "pm10010mptMesrlineNetTxBiasCurrentTable": pm10010mptMesrlineNetTxBiasCurrentTable,
       "pm10010mptMesrlineNetTxBiasCurrentEntry": pm10010mptMesrlineNetTxBiasCurrentEntry,
       "pm10010mptMesrlineNetTxBiasCurrentIndex": pm10010mptMesrlineNetTxBiasCurrentIndex,
       "pm10010mptMesrlineNetTxBiasCurrentPortn": pm10010mptMesrlineNetTxBiasCurrentPortn,
       "pm10010mptMesrlineNetRxInputPwrTable": pm10010mptMesrlineNetRxInputPwrTable,
       "pm10010mptMesrlineNetRxInputPwrEntry": pm10010mptMesrlineNetRxInputPwrEntry,
       "pm10010mptMesrlineNetRxInputPwrIndex": pm10010mptMesrlineNetRxInputPwrIndex,
       "pm10010mptMesrlineNetRxInputPwrPortn": pm10010mptMesrlineNetRxInputPwrPortn,
       "pm10010mptMesrlineResidualChromaticDispTable": pm10010mptMesrlineResidualChromaticDispTable,
       "pm10010mptMesrlineResidualChromaticDispEntry": pm10010mptMesrlineResidualChromaticDispEntry,
       "pm10010mptMesrlineResidualChromaticDispIndex": pm10010mptMesrlineResidualChromaticDispIndex,
       "pm10010mptMesrlineResidualChromaticDispPortn": pm10010mptMesrlineResidualChromaticDispPortn,
       "pm10010mptMesrlineDiffGroupDelayTable": pm10010mptMesrlineDiffGroupDelayTable,
       "pm10010mptMesrlineDiffGroupDelayEntry": pm10010mptMesrlineDiffGroupDelayEntry,
       "pm10010mptMesrlineDiffGroupDelayIndex": pm10010mptMesrlineDiffGroupDelayIndex,
       "pm10010mptMesrlineDiffGroupDelayPortn": pm10010mptMesrlineDiffGroupDelayPortn,
       "pm10010mptMesrlineQFactorTable": pm10010mptMesrlineQFactorTable,
       "pm10010mptMesrlineQFactorEntry": pm10010mptMesrlineQFactorEntry,
       "pm10010mptMesrlineQFactorIndex": pm10010mptMesrlineQFactorIndex,
       "pm10010mptMesrlineQFactorPortn": pm10010mptMesrlineQFactorPortn,
       "pm10010mptMesrlineCarrierFreqOffsetTable": pm10010mptMesrlineCarrierFreqOffsetTable,
       "pm10010mptMesrlineCarrierFreqOffsetEntry": pm10010mptMesrlineCarrierFreqOffsetEntry,
       "pm10010mptMesrlineCarrierFreqOffsetIndex": pm10010mptMesrlineCarrierFreqOffsetIndex,
       "pm10010mptMesrlineCarrierFreqOffsetPortn": pm10010mptMesrlineCarrierFreqOffsetPortn,
       "pm10010mptMesrlineOsnrTable": pm10010mptMesrlineOsnrTable,
       "pm10010mptMesrlineOsnrEntry": pm10010mptMesrlineOsnrEntry,
       "pm10010mptMesrlineOsnrIndex": pm10010mptMesrlineOsnrIndex,
       "pm10010mptMesrlineOsnrPortn": pm10010mptMesrlineOsnrPortn,
       "pm10010mptcounters": pm10010mptcounters,
       "pm10010mptCntOther": pm10010mptCntOther,
       "pm10010mptCntClient": pm10010mptCntClient,
       "pm10010mptCntclientInputErrorCounterLaneOneTable": pm10010mptCntclientInputErrorCounterLaneOneTable,
       "pm10010mptCntclientInputErrorCounterLaneOneEntry": pm10010mptCntclientInputErrorCounterLaneOneEntry,
       "pm10010mptCntclientInputErrorCounterLaneOneIndex": pm10010mptCntclientInputErrorCounterLaneOneIndex,
       "pm10010mptCntclientInputErrorCounterLaneOneValuePortn": pm10010mptCntclientInputErrorCounterLaneOneValuePortn,
       "pm10010mptCntclientInputErrorCounterLaneOneErrorPortn": pm10010mptCntclientInputErrorCounterLaneOneErrorPortn,
       "pm10010mptCntclientInputErrorCounterLaneOneOverloadPortn": pm10010mptCntclientInputErrorCounterLaneOneOverloadPortn,
       "pm10010mptCntclientInputErrorCounterLaneTwoTable": pm10010mptCntclientInputErrorCounterLaneTwoTable,
       "pm10010mptCntclientInputErrorCounterLaneTwoEntry": pm10010mptCntclientInputErrorCounterLaneTwoEntry,
       "pm10010mptCntclientInputErrorCounterLaneTwoIndex": pm10010mptCntclientInputErrorCounterLaneTwoIndex,
       "pm10010mptCntclientInputErrorCounterLaneTwoValuePortn": pm10010mptCntclientInputErrorCounterLaneTwoValuePortn,
       "pm10010mptCntclientInputErrorCounterLaneTwoErrorPortn": pm10010mptCntclientInputErrorCounterLaneTwoErrorPortn,
       "pm10010mptCntclientInputErrorCounterLaneTwoOverloadPortn": pm10010mptCntclientInputErrorCounterLaneTwoOverloadPortn,
       "pm10010mptCntclientInputErrorCounterTable": pm10010mptCntclientInputErrorCounterTable,
       "pm10010mptCntclientInputErrorCounterEntry": pm10010mptCntclientInputErrorCounterEntry,
       "pm10010mptCntclientInputErrorCounterIndex": pm10010mptCntclientInputErrorCounterIndex,
       "pm10010mptCntclientInputErrorCounterValuePortn": pm10010mptCntclientInputErrorCounterValuePortn,
       "pm10010mptCntclientInputErrorCounterErrorPortn": pm10010mptCntclientInputErrorCounterErrorPortn,
       "pm10010mptCntclientInputErrorCounterOverloadPortn": pm10010mptCntclientInputErrorCounterOverloadPortn,
       "pm10010mptCntclientCbipCounterTable": pm10010mptCntclientCbipCounterTable,
       "pm10010mptCntclientCbipCounterEntry": pm10010mptCntclientCbipCounterEntry,
       "pm10010mptCntclientCbipCounterIndex": pm10010mptCntclientCbipCounterIndex,
       "pm10010mptCntclientCbipCounterValuePortn": pm10010mptCntclientCbipCounterValuePortn,
       "pm10010mptCntclientCbipCounterErrorPortn": pm10010mptCntclientCbipCounterErrorPortn,
       "pm10010mptCntclientCbipCounterOverloadPortn": pm10010mptCntclientCbipCounterOverloadPortn,
       "pm10010mptCntLine": pm10010mptCntLine,
       "pm10010mptCntlocalLineSmBip8ErrorCounterTable": pm10010mptCntlocalLineSmBip8ErrorCounterTable,
       "pm10010mptCntlocalLineSmBip8ErrorCounterEntry": pm10010mptCntlocalLineSmBip8ErrorCounterEntry,
       "pm10010mptCntlocalLineSmBip8ErrorCounterIndex": pm10010mptCntlocalLineSmBip8ErrorCounterIndex,
       "pm10010mptCntlocalLineSmBip8ErrorCounterValuePortn": pm10010mptCntlocalLineSmBip8ErrorCounterValuePortn,
       "pm10010mptCntlocalLineSmBip8ErrorCounterErrorPortn": pm10010mptCntlocalLineSmBip8ErrorCounterErrorPortn,
       "pm10010mptCntlocalLineSmBip8ErrorCounterOverloadPortn": pm10010mptCntlocalLineSmBip8ErrorCounterOverloadPortn,
       "pm10010mptCntlocalLineFecCorrectedErrorsCounterTable": pm10010mptCntlocalLineFecCorrectedErrorsCounterTable,
       "pm10010mptCntlocalLineFecCorrectedErrorsCounterEntry": pm10010mptCntlocalLineFecCorrectedErrorsCounterEntry,
       "pm10010mptCntlocalLineFecCorrectedErrorsCounterIndex": pm10010mptCntlocalLineFecCorrectedErrorsCounterIndex,
       "pm10010mptCntlocalLineFecCorrectedErrorsCounterValuePortn": pm10010mptCntlocalLineFecCorrectedErrorsCounterValuePortn,
       "pm10010mptCntlocalLineFecCorrectedErrorsCounterErrorPortn": pm10010mptCntlocalLineFecCorrectedErrorsCounterErrorPortn,
       "pm10010mptCntlocalLineFecCorrectedErrorsCounterOverloadPortn": pm10010mptCntlocalLineFecCorrectedErrorsCounterOverloadPortn,
       "pm10010mptCntremoteLineSmBip8ErrorCounterTable": pm10010mptCntremoteLineSmBip8ErrorCounterTable,
       "pm10010mptCntremoteLineSmBip8ErrorCounterEntry": pm10010mptCntremoteLineSmBip8ErrorCounterEntry,
       "pm10010mptCntremoteLineSmBip8ErrorCounterIndex": pm10010mptCntremoteLineSmBip8ErrorCounterIndex,
       "pm10010mptCntremoteLineSmBip8ErrorCounterValuePortn": pm10010mptCntremoteLineSmBip8ErrorCounterValuePortn,
       "pm10010mptCntremoteLineSmBip8ErrorCounterErrorPortn": pm10010mptCntremoteLineSmBip8ErrorCounterErrorPortn,
       "pm10010mptCntremoteLineSmBip8ErrorCounterOverloadPortn": pm10010mptCntremoteLineSmBip8ErrorCounterOverloadPortn,
       "pm10010mptCntlineDfrmTimCntTable": pm10010mptCntlineDfrmTimCntTable,
       "pm10010mptCntlineDfrmTimCntEntry": pm10010mptCntlineDfrmTimCntEntry,
       "pm10010mptCntlineDfrmTimCntIndex": pm10010mptCntlineDfrmTimCntIndex,
       "pm10010mptCntlineDfrmTimCntValuePortn": pm10010mptCntlineDfrmTimCntValuePortn,
       "pm10010mptCntlineDfrmTimCntErrorPortn": pm10010mptCntlineDfrmTimCntErrorPortn,
       "pm10010mptCntlineDfrmTimCntOverloadPortn": pm10010mptCntlineDfrmTimCntOverloadPortn,
       "pm10010mptCntlocalLineTrscvFecCorrectedErrorCounterTable": pm10010mptCntlocalLineTrscvFecCorrectedErrorCounterTable,
       "pm10010mptCntlocalLineTrscvFecCorrectedErrorCounterEntry": pm10010mptCntlocalLineTrscvFecCorrectedErrorCounterEntry,
       "pm10010mptCntlocalLineTrscvFecCorrectedErrorCounterIndex": pm10010mptCntlocalLineTrscvFecCorrectedErrorCounterIndex,
       "pm10010mptCntlocalLineTrscvFecCorrectedErrorCounterValuePortn": pm10010mptCntlocalLineTrscvFecCorrectedErrorCounterValuePortn,
       "pm10010mptCntlocalLineTrscvFecCorrectedErrorCounterErrorPortn": pm10010mptCntlocalLineTrscvFecCorrectedErrorCounterErrorPortn,
       "pm10010mptCntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn": pm10010mptCntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn,
       "pm10010mptCntlocalLineTrscvFecUncorrectedErrorCounterTable": pm10010mptCntlocalLineTrscvFecUncorrectedErrorCounterTable,
       "pm10010mptCntlocalLineTrscvFecUncorrectedErrorCounterEntry": pm10010mptCntlocalLineTrscvFecUncorrectedErrorCounterEntry,
       "pm10010mptCntlocalLineTrscvFecUncorrectedErrorCounterIndex": pm10010mptCntlocalLineTrscvFecUncorrectedErrorCounterIndex,
       "pm10010mptCntlocalLineTrscvFecUncorrectedErrorCounterValuePortn": pm10010mptCntlocalLineTrscvFecUncorrectedErrorCounterValuePortn,
       "pm10010mptCntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn": pm10010mptCntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn,
       "pm10010mptCntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn": pm10010mptCntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn,
       "pm10010mptcontrolsWrite": pm10010mptcontrolsWrite,
       "pm10010mptCtrlOther": pm10010mptCtrlOther,
       "pm10010mptCtrlconfMgnt1": pm10010mptCtrlconfMgnt1,
       "pm10010mptCtrlConf1Load1": pm10010mptCtrlConf1Load1,
       "pm10010mptCtrlConf2Load1": pm10010mptCtrlConf2Load1,
       "pm10010mptCtrlConf2Flash1": pm10010mptCtrlConf2Flash1,
       "pm10010mptCtrlConf2Clear1": pm10010mptCtrlConf2Clear1,
       "pm10010mptCtrlsynth4": pm10010mptCtrlsynth4,
       "pm10010mptCtrlCorrelatOn": pm10010mptCtrlCorrelatOn,
       "pm10010mptCtrlCorrelatOff": pm10010mptCtrlCorrelatOff,
       "pm10010mptCtrlswMgnt": pm10010mptCtrlswMgnt,
       "pm10010mptCtrlColdReset": pm10010mptCtrlColdReset,
       "pm10010mptCtrlWarmReset": pm10010mptCtrlWarmReset,
       "pm10010mptCtrlLoadSwBank1": pm10010mptCtrlLoadSwBank1,
       "pm10010mptCtrlLoadSwBank2": pm10010mptCtrlLoadSwBank2,
       "pm10010mptCtrlgwMgnt": pm10010mptCtrlgwMgnt,
       "pm10010mptCtrlCurrentGwReset": pm10010mptCtrlCurrentGwReset,
       "pm10010mptCtrlLoadGwBank1": pm10010mptCtrlLoadGwBank1,
       "pm10010mptCtrlLoadGwBank2": pm10010mptCtrlLoadGwBank2,
       "pm10010mptCtrlLoadGwBank3": pm10010mptCtrlLoadGwBank3,
       "pm10010mptCtrlLoadGwBank4": pm10010mptCtrlLoadGwBank4,
       "pm10010mptCtrlledTest": pm10010mptCtrlledTest,
       "pm10010mptCtrlGreenLed": pm10010mptCtrlGreenLed,
       "pm10010mptCtrlRedLed": pm10010mptCtrlRedLed,
       "pm10010mptCtrlLedOff": pm10010mptCtrlLedOff,
       "pm10010mptCtrlinitSwitchMarvell": pm10010mptCtrlinitSwitchMarvell,
       "pm10010mptCtrlInitSwitchMarvell": pm10010mptCtrlInitSwitchMarvell,
       "pm10010mptCtrlresetCount": pm10010mptCtrlresetCount,
       "pm10010mptCtrlResetcount": pm10010mptCtrlResetcount,
       "pm10010mptCtrlresetRmon": pm10010mptCtrlresetRmon,
       "pm10010mptCtrlResetrmon": pm10010mptCtrlResetrmon,
       "pm10010mptCtrlresetMeasurements": pm10010mptCtrlresetMeasurements,
       "pm10010mptCtrlResetmeasurements": pm10010mptCtrlResetmeasurements,
       "pm10010mptCtrlClient": pm10010mptCtrlClient,
       "pm10010mptCtrlaccessLoopTable": pm10010mptCtrlaccessLoopTable,
       "pm10010mptCtrlaccessLoopEntry": pm10010mptCtrlaccessLoopEntry,
       "pm10010mptCtrlaccessLoopIndex": pm10010mptCtrlaccessLoopIndex,
       "pm10010mptCtrlaccessLoopPortn": pm10010mptCtrlaccessLoopPortn,
       "pm10010mptCtrlclientLoopToLineTable": pm10010mptCtrlclientLoopToLineTable,
       "pm10010mptCtrlclientLoopToLineEntry": pm10010mptCtrlclientLoopToLineEntry,
       "pm10010mptCtrlclientLoopToLineIndex": pm10010mptCtrlclientLoopToLineIndex,
       "pm10010mptCtrlclientLoopToLinePortn": pm10010mptCtrlclientLoopToLinePortn,
       "pm10010mptCtrlcsfUpInsTable": pm10010mptCtrlcsfUpInsTable,
       "pm10010mptCtrlcsfUpInsEntry": pm10010mptCtrlcsfUpInsEntry,
       "pm10010mptCtrlcsfUpInsIndex": pm10010mptCtrlcsfUpInsIndex,
       "pm10010mptCtrlcsfUpInsPortn": pm10010mptCtrlcsfUpInsPortn,
       "pm10010mptCtrlcaisDwInsTable": pm10010mptCtrlcaisDwInsTable,
       "pm10010mptCtrlcaisDwInsEntry": pm10010mptCtrlcaisDwInsEntry,
       "pm10010mptCtrlcaisDwInsIndex": pm10010mptCtrlcaisDwInsIndex,
       "pm10010mptCtrlcaisDwInsPortn": pm10010mptCtrlcaisDwInsPortn,
       "pm10010mptCtrlclientResetAllCountTable": pm10010mptCtrlclientResetAllCountTable,
       "pm10010mptCtrlclientResetAllCountEntry": pm10010mptCtrlclientResetAllCountEntry,
       "pm10010mptCtrlclientResetAllCountIndex": pm10010mptCtrlclientResetAllCountIndex,
       "pm10010mptCtrlclientResetAllCountsPortn": pm10010mptCtrlclientResetAllCountsPortn,
       "pm10010mptCtrlLine": pm10010mptCtrlLine,
       "pm10010mptCtrlcommAccessLoopTable": pm10010mptCtrlcommAccessLoopTable,
       "pm10010mptCtrlcommAccessLoopEntry": pm10010mptCtrlcommAccessLoopEntry,
       "pm10010mptCtrlcommAccessLoopIndex": pm10010mptCtrlcommAccessLoopIndex,
       "pm10010mptCtrlcommAccessLoopPortn": pm10010mptCtrlcommAccessLoopPortn,
       "pm10010mptCtrllineLoopTable": pm10010mptCtrllineLoopTable,
       "pm10010mptCtrllineLoopEntry": pm10010mptCtrllineLoopEntry,
       "pm10010mptCtrllineLoopIndex": pm10010mptCtrllineLoopIndex,
       "pm10010mptCtrllineLoopPortn": pm10010mptCtrllineLoopPortn,
       "pm10010mptCtrlfecDisableTable": pm10010mptCtrlfecDisableTable,
       "pm10010mptCtrlfecDisableEntry": pm10010mptCtrlfecDisableEntry,
       "pm10010mptCtrlfecDisableIndex": pm10010mptCtrlfecDisableIndex,
       "pm10010mptCtrlfecDisablePortn": pm10010mptCtrlfecDisablePortn,
       "pm10010mptCtrlmsaLineLoopTable": pm10010mptCtrlmsaLineLoopTable,
       "pm10010mptCtrlmsaLineLoopEntry": pm10010mptCtrlmsaLineLoopEntry,
       "pm10010mptCtrlmsaLineLoopIndex": pm10010mptCtrlmsaLineLoopIndex,
       "pm10010mptCtrlmsaLineLoopPortn": pm10010mptCtrlmsaLineLoopPortn,
       "pm10010mptCtrlmsaTxResetTable": pm10010mptCtrlmsaTxResetTable,
       "pm10010mptCtrlmsaTxResetEntry": pm10010mptCtrlmsaTxResetEntry,
       "pm10010mptCtrlmsaTxResetIndex": pm10010mptCtrlmsaTxResetIndex,
       "pm10010mptCtrlmsaTxResetPortn": pm10010mptCtrlmsaTxResetPortn,
       "pm10010mptCtrlmsaRxResetTable": pm10010mptCtrlmsaRxResetTable,
       "pm10010mptCtrlmsaRxResetEntry": pm10010mptCtrlmsaRxResetEntry,
       "pm10010mptCtrlmsaRxResetIndex": pm10010mptCtrlmsaRxResetIndex,
       "pm10010mptCtrlmsaRxResetPortn": pm10010mptCtrlmsaRxResetPortn,
       "pm10010mptCtrlmsaShutdownTable": pm10010mptCtrlmsaShutdownTable,
       "pm10010mptCtrlmsaShutdownEntry": pm10010mptCtrlmsaShutdownEntry,
       "pm10010mptCtrlmsaShutdownIndex": pm10010mptCtrlmsaShutdownIndex,
       "pm10010mptCtrlmsaShutdownPortn": pm10010mptCtrlmsaShutdownPortn,
       "pm10010mptCtrllineResetAllCountTable": pm10010mptCtrllineResetAllCountTable,
       "pm10010mptCtrllineResetAllCountEntry": pm10010mptCtrllineResetAllCountEntry,
       "pm10010mptCtrllineResetAllCountIndex": pm10010mptCtrllineResetAllCountIndex,
       "pm10010mptCtrllineResetAllCountsPortn": pm10010mptCtrllineResetAllCountsPortn,
       "pm10010mptri": pm10010mptri,
       "pm10010mptriTable": pm10010mptriTable,
       "pm10010mptRinvSfpTable": pm10010mptRinvSfpTable,
       "pm10010mptRinvSfpEntry": pm10010mptRinvSfpEntry,
       "pm10010mptRinvSfpIndex": pm10010mptRinvSfpIndex,
       "pm10010mptRinvsfp": pm10010mptRinvsfp,
       "pm10010mptRinvLineTable": pm10010mptRinvLineTable,
       "pm10010mptRinvLineEntry": pm10010mptRinvLineEntry,
       "pm10010mptRinvLineIndex": pm10010mptRinvLineIndex,
       "pm10010mptRinvxfpLine": pm10010mptRinvxfpLine,
       "pm10010mptRinvReloadInventory": pm10010mptRinvReloadInventory,
       "pm10010mptRinvHwPlatform": pm10010mptRinvHwPlatform,
       "pm10010mptRinvModulePlatform": pm10010mptRinvModulePlatform,
       "pm10010mptRinvSwPlatform": pm10010mptRinvSwPlatform,
       "pm10010mptRinvGwPlatform": pm10010mptRinvGwPlatform,
       "pm10010mptdownload": pm10010mptdownload,
       "pm10010mptDwlOther": pm10010mptDwlOther,
       "pm10010mptDwlrestartProcess": pm10010mptDwlrestartProcess,
       "pm10010mptDwlWarmRestartProcessed": pm10010mptDwlWarmRestartProcessed,
       "pm10010mptDwlColdRestartProcessed": pm10010mptDwlColdRestartProcessed,
       "pm10010mptDwlswBanksUsed": pm10010mptDwlswBanksUsed,
       "pm10010mptDwlSwBank1Used": pm10010mptDwlSwBank1Used,
       "pm10010mptDwlSwBank2Used": pm10010mptDwlSwBank2Used,
       "pm10010mptDwlSwBank1Notempty": pm10010mptDwlSwBank1Notempty,
       "pm10010mptDwlSwBank2Notempty": pm10010mptDwlSwBank2Notempty,
       "pm10010mptDwlgwBanksUsed": pm10010mptDwlgwBanksUsed,
       "pm10010mptDwlGwBank1Used": pm10010mptDwlGwBank1Used,
       "pm10010mptDwlGwBank2Used": pm10010mptDwlGwBank2Used,
       "pm10010mptDwlGwBank3Used": pm10010mptDwlGwBank3Used,
       "pm10010mptDwlGwBank4Used": pm10010mptDwlGwBank4Used,
       "pm10010mptDwlGwBank1Notempty": pm10010mptDwlGwBank1Notempty,
       "pm10010mptDwlGwBank2Notempty": pm10010mptDwlGwBank2Notempty,
       "pm10010mptDwlGwBank3Notempty": pm10010mptDwlGwBank3Notempty,
       "pm10010mptDwlGwBank4Notempty": pm10010mptDwlGwBank4Notempty,
       "pm10010mptDwlClient": pm10010mptDwlClient,
       "pm10010mptDwlLine": pm10010mptDwlLine,
       "pm10010mptConfig": pm10010mptConfig,
       "pm10010mptCfgAccessCAisCsf": pm10010mptCfgAccessCAisCsf,
       "pm10010mptCfgClientcaiscsfTable": pm10010mptCfgClientcaiscsfTable,
       "pm10010mptCfgClientcaiscsfEntry": pm10010mptCfgClientcaiscsfEntry,
       "pm10010mptCfgClientcaiscsfIndex": pm10010mptCfgClientcaiscsfIndex,
       "pm10010mptCfgReservePortn": pm10010mptCfgReservePortn,
       "pm10010mptCfgStartup": pm10010mptCfgStartup,
       "pm10010mptCfgClientStartupTable": pm10010mptCfgClientStartupTable,
       "pm10010mptCfgClientStartupEntry": pm10010mptCfgClientStartupEntry,
       "pm10010mptCfgClientStartupIndex": pm10010mptCfgClientStartupIndex,
       "pm10010mptCfgSystConfPortPortn": pm10010mptCfgSystConfPortPortn,
       "pm10010mptCfgNetConfPortPortn": pm10010mptCfgNetConfPortPortn,
       "pm10010mptCfgIgnoreTimePortn": pm10010mptCfgIgnoreTimePortn,
       "pm10010mptCfgOptionsPortPortn": pm10010mptCfgOptionsPortPortn,
       "pm10010mptCfgLineStartupTable": pm10010mptCfgLineStartupTable,
       "pm10010mptCfgLineStartupEntry": pm10010mptCfgLineStartupEntry,
       "pm10010mptCfgLineStartupIndex": pm10010mptCfgLineStartupIndex,
       "pm10010mptCfgSystConfLinePortn": pm10010mptCfgSystConfLinePortn,
       "pm10010mptCfgOptionsLinePortn": pm10010mptCfgOptionsLinePortn,
       "pm10010mptCfgXfpTable": pm10010mptCfgXfpTable,
       "pm10010mptCfgXfpEntry": pm10010mptCfgXfpEntry,
       "pm10010mptCfgXfpIndex": pm10010mptCfgXfpIndex,
       "pm10010mptCfgSystConfMsaLinePortn": pm10010mptCfgSystConfMsaLinePortn,
       "pm10010mptCfgLabels": pm10010mptCfgLabels,
       "pm10010mptCfgLabelclientTable": pm10010mptCfgLabelclientTable,
       "pm10010mptCfgLabelclientEntry": pm10010mptCfgLabelclientEntry,
       "pm10010mptCfgLabelclientIndex": pm10010mptCfgLabelclientIndex,
       "pm10010mptCfgLabelclientPortn": pm10010mptCfgLabelclientPortn,
       "pm10010mptCfgLabellineTable": pm10010mptCfgLabellineTable,
       "pm10010mptCfgLabellineEntry": pm10010mptCfgLabellineEntry,
       "pm10010mptCfgLabellineIndex": pm10010mptCfgLabellineIndex,
       "pm10010mptCfgLabellinePortn": pm10010mptCfgLabellinePortn,
       "pm10010mptCfgStartuptlh": pm10010mptCfgStartuptlh,
       "pm10010mptCfgOtxtlhTable": pm10010mptCfgOtxtlhTable,
       "pm10010mptCfgOtxtlhEntry": pm10010mptCfgOtxtlhEntry,
       "pm10010mptCfgOtxtlhIndex": pm10010mptCfgOtxtlhIndex,
       "pm10010mptCfgLinePwrLaserPortn": pm10010mptCfgLinePwrLaserPortn,
       "pm10010mptCfgLineFCurrentPortn": pm10010mptCfgLineFCurrentPortn,
       "pm10010mptCfgLineGridCurrentPortn": pm10010mptCfgLineGridCurrentPortn,
       "pm10010mptCfgFPortn": pm10010mptCfgFPortn,
       "pm10010mptCfgRxLineFCurrentPortn": pm10010mptCfgRxLineFCurrentPortn,
       "pm10010mptCfgOther": pm10010mptCfgOther,
       "pm10010mpttablemoduleOther": pm10010mpttablemoduleOther,
       "pm10010mptCfgmode": pm10010mptCfgmode,
       "pm10010mptCfgfanLowSpeedThreshold": pm10010mptCfgfanLowSpeedThreshold,
       "pm10010mptCfgfanHighSpeedThreshold": pm10010mptCfgfanHighSpeedThreshold,
       "pm10010mptCfgStartuptablefive": pm10010mptCfgStartuptablefive,
       "pm10010mptCfgOtxtlhcapabilitiesTable": pm10010mptCfgOtxtlhcapabilitiesTable,
       "pm10010mptCfgOtxtlhcapabilitiesEntry": pm10010mptCfgOtxtlhcapabilitiesEntry,
       "pm10010mptCfgOtxtlhcapabilitiesIndex": pm10010mptCfgOtxtlhcapabilitiesIndex,
       "pm10010mptCfgComponentTypePortn": pm10010mptCfgComponentTypePortn,
       "pm10010mptCfgMiscellaneousPortn": pm10010mptCfgMiscellaneousPortn,
       "pm10010mptCfgFirstChannelPortn": pm10010mptCfgFirstChannelPortn,
       "pm10010mptCfgLastChannelPortn": pm10010mptCfgLastChannelPortn,
       "pm10010mptCfgGridPortn": pm10010mptCfgGridPortn,
       "pm10010mptCfgWriteConfiguration": pm10010mptCfgWriteConfiguration,
       "pm10010mpttraps": pm10010mpttraps,
       "pm10010mpttrapPortNumber": pm10010mpttrapPortNumber,
       "pm10010mpttrapLineNumber": pm10010mpttrapLineNumber,
       "pm10010mpttrapBoardNumber": pm10010mpttrapBoardNumber,
       "pm10010mptLineTrapNotUrgentGoesOn": pm10010mptLineTrapNotUrgentGoesOn,
       "pm10010mptLineTrapNotUrgentGoesOff": pm10010mptLineTrapNotUrgentGoesOff,
       "pm10010mptLineTrapUrgentGoesOn": pm10010mptLineTrapUrgentGoesOn,
       "pm10010mptLineTrapUrgentGoesOff": pm10010mptLineTrapUrgentGoesOff,
       "pm10010mptLineTrapCritGoesOn": pm10010mptLineTrapCritGoesOn,
       "pm10010mptLineTrapCritGoesOff": pm10010mptLineTrapCritGoesOff,
       "pm10010mptClientTrapNotUrgentGoesOn": pm10010mptClientTrapNotUrgentGoesOn,
       "pm10010mptClientTrapNotUrgentGoesOff": pm10010mptClientTrapNotUrgentGoesOff,
       "pm10010mptClientTrapUrgentGoesOn": pm10010mptClientTrapUrgentGoesOn,
       "pm10010mptClientTrapUrgentGoesOff": pm10010mptClientTrapUrgentGoesOff,
       "pm10010mptClientTrapCritGoesOn": pm10010mptClientTrapCritGoesOn,
       "pm10010mptClientTrapCritGoesOff": pm10010mptClientTrapCritGoesOff,
       "pm10010mptPowerTrapUrgentGoesOn": pm10010mptPowerTrapUrgentGoesOn,
       "pm10010mptPowerTrapUrgentGoesOff": pm10010mptPowerTrapUrgentGoesOff,
       "pm10010mptMonitoring": pm10010mptMonitoring,
       "pm10010mptMonOther": pm10010mptMonOther,
       "pm10010mptMonRmon": pm10010mptMonRmon,
       "pm10010mptMonClient": pm10010mptMonClient,
       "pm10010mptMonClientRmonCounter": pm10010mptMonClientRmonCounter,
       "pm10010mptMonupRmonBytesCounterClientInputTable": pm10010mptMonupRmonBytesCounterClientInputTable,
       "pm10010mptMonupRmonBytesCounterClientInputEntry": pm10010mptMonupRmonBytesCounterClientInputEntry,
       "pm10010mptMonupRmonBytesCounterClientInputIndex": pm10010mptMonupRmonBytesCounterClientInputIndex,
       "pm10010mptMonupRmonBytesCounterClientInputValuePortn": pm10010mptMonupRmonBytesCounterClientInputValuePortn,
       "pm10010mptMonupRmonBytesCounterClientInputErrorPortn": pm10010mptMonupRmonBytesCounterClientInputErrorPortn,
       "pm10010mptMonupRmonBytesCounterClientInputOverloadPortn": pm10010mptMonupRmonBytesCounterClientInputOverloadPortn,
       "pm10010mptMonupRmonCrcErrorsCounterClientInputTable": pm10010mptMonupRmonCrcErrorsCounterClientInputTable,
       "pm10010mptMonupRmonCrcErrorsCounterClientInputEntry": pm10010mptMonupRmonCrcErrorsCounterClientInputEntry,
       "pm10010mptMonupRmonCrcErrorsCounterClientInputIndex": pm10010mptMonupRmonCrcErrorsCounterClientInputIndex,
       "pm10010mptMonupRmonCrcErrorsCounterClientInputValuePortn": pm10010mptMonupRmonCrcErrorsCounterClientInputValuePortn,
       "pm10010mptMonupRmonCrcErrorsCounterClientInputErrorPortn": pm10010mptMonupRmonCrcErrorsCounterClientInputErrorPortn,
       "pm10010mptMonupRmonCrcErrorsCounterClientInputOverloadPortn": pm10010mptMonupRmonCrcErrorsCounterClientInputOverloadPortn,
       "pm10010mptMonupRmonPacketsCounterClientInputTable": pm10010mptMonupRmonPacketsCounterClientInputTable,
       "pm10010mptMonupRmonPacketsCounterClientInputEntry": pm10010mptMonupRmonPacketsCounterClientInputEntry,
       "pm10010mptMonupRmonPacketsCounterClientInputIndex": pm10010mptMonupRmonPacketsCounterClientInputIndex,
       "pm10010mptMonupRmonPacketsCounterClientInputValuePortn": pm10010mptMonupRmonPacketsCounterClientInputValuePortn,
       "pm10010mptMonupRmonPacketsCounterClientInputErrorPortn": pm10010mptMonupRmonPacketsCounterClientInputErrorPortn,
       "pm10010mptMonupRmonPacketsCounterClientInputOverloadPortn": pm10010mptMonupRmonPacketsCounterClientInputOverloadPortn,
       "pm10010mptMonupRmonBroadcastCounterClientInputTable": pm10010mptMonupRmonBroadcastCounterClientInputTable,
       "pm10010mptMonupRmonBroadcastCounterClientInputEntry": pm10010mptMonupRmonBroadcastCounterClientInputEntry,
       "pm10010mptMonupRmonBroadcastCounterClientInputIndex": pm10010mptMonupRmonBroadcastCounterClientInputIndex,
       "pm10010mptMonupRmonBroadcastCounterClientInputValuePortn": pm10010mptMonupRmonBroadcastCounterClientInputValuePortn,
       "pm10010mptMonupRmonBroadcastCounterClientInputErrorPortn": pm10010mptMonupRmonBroadcastCounterClientInputErrorPortn,
       "pm10010mptMonupRmonBroadcastCounterClientInputOverloadPortn": pm10010mptMonupRmonBroadcastCounterClientInputOverloadPortn,
       "pm10010mptMonupRmonMulticastCounterClientInputTable": pm10010mptMonupRmonMulticastCounterClientInputTable,
       "pm10010mptMonupRmonMulticastCounterClientInputEntry": pm10010mptMonupRmonMulticastCounterClientInputEntry,
       "pm10010mptMonupRmonMulticastCounterClientInputIndex": pm10010mptMonupRmonMulticastCounterClientInputIndex,
       "pm10010mptMonupRmonMulticastCounterClientInputValuePortn": pm10010mptMonupRmonMulticastCounterClientInputValuePortn,
       "pm10010mptMonupRmonMulticastCounterClientInputErrorPortn": pm10010mptMonupRmonMulticastCounterClientInputErrorPortn,
       "pm10010mptMonupRmonMulticastCounterClientInputOverloadPortn": pm10010mptMonupRmonMulticastCounterClientInputOverloadPortn,
       "pm10010mptMonupRmonPauseFrameCounterClientInputTable": pm10010mptMonupRmonPauseFrameCounterClientInputTable,
       "pm10010mptMonupRmonPauseFrameCounterClientInputEntry": pm10010mptMonupRmonPauseFrameCounterClientInputEntry,
       "pm10010mptMonupRmonPauseFrameCounterClientInputIndex": pm10010mptMonupRmonPauseFrameCounterClientInputIndex,
       "pm10010mptMonupRmonPauseFrameCounterClientInputValuePortn": pm10010mptMonupRmonPauseFrameCounterClientInputValuePortn,
       "pm10010mptMonupRmonPauseFrameCounterClientInputErrorPortn": pm10010mptMonupRmonPauseFrameCounterClientInputErrorPortn,
       "pm10010mptMonupRmonPauseFrameCounterClientInputOverloadPortn": pm10010mptMonupRmonPauseFrameCounterClientInputOverloadPortn,
       "pm10010mptMonupRmonUnicastCounterClientInputTable": pm10010mptMonupRmonUnicastCounterClientInputTable,
       "pm10010mptMonupRmonUnicastCounterClientInputEntry": pm10010mptMonupRmonUnicastCounterClientInputEntry,
       "pm10010mptMonupRmonUnicastCounterClientInputIndex": pm10010mptMonupRmonUnicastCounterClientInputIndex,
       "pm10010mptMonupRmonUnicastCounterClientInputValuePortn": pm10010mptMonupRmonUnicastCounterClientInputValuePortn,
       "pm10010mptMonupRmonUnicastCounterClientInputErrorPortn": pm10010mptMonupRmonUnicastCounterClientInputErrorPortn,
       "pm10010mptMonupRmonUnicastCounterClientInputOverloadPortn": pm10010mptMonupRmonUnicastCounterClientInputOverloadPortn,
       "pm10010mptMonupRmonNonunicastCounterClientInputTable": pm10010mptMonupRmonNonunicastCounterClientInputTable,
       "pm10010mptMonupRmonNonunicastCounterClientInputEntry": pm10010mptMonupRmonNonunicastCounterClientInputEntry,
       "pm10010mptMonupRmonNonunicastCounterClientInputIndex": pm10010mptMonupRmonNonunicastCounterClientInputIndex,
       "pm10010mptMonupRmonNonunicastCounterClientInputValuePortn": pm10010mptMonupRmonNonunicastCounterClientInputValuePortn,
       "pm10010mptMonupRmonNonunicastCounterClientInputErrorPortn": pm10010mptMonupRmonNonunicastCounterClientInputErrorPortn,
       "pm10010mptMonupRmonNonunicastCounterClientInputOverloadPortn": pm10010mptMonupRmonNonunicastCounterClientInputOverloadPortn,
       "pm10010mptMondownRmonBytesCounterClientOutputTable": pm10010mptMondownRmonBytesCounterClientOutputTable,
       "pm10010mptMondownRmonBytesCounterClientOutputEntry": pm10010mptMondownRmonBytesCounterClientOutputEntry,
       "pm10010mptMondownRmonBytesCounterClientOutputIndex": pm10010mptMondownRmonBytesCounterClientOutputIndex,
       "pm10010mptMondownRmonBytesCounterClientOutputValuePortn": pm10010mptMondownRmonBytesCounterClientOutputValuePortn,
       "pm10010mptMondownRmonBytesCounterClientOutputErrorPortn": pm10010mptMondownRmonBytesCounterClientOutputErrorPortn,
       "pm10010mptMondownRmonBytesCounterClientOutputOverloadPortn": pm10010mptMondownRmonBytesCounterClientOutputOverloadPortn,
       "pm10010mptMondownRmonCrcErrorsCounterClientOutputTable": pm10010mptMondownRmonCrcErrorsCounterClientOutputTable,
       "pm10010mptMondownRmonCrcErrorsCounterClientOutputEntry": pm10010mptMondownRmonCrcErrorsCounterClientOutputEntry,
       "pm10010mptMondownRmonCrcErrorsCounterClientOutputIndex": pm10010mptMondownRmonCrcErrorsCounterClientOutputIndex,
       "pm10010mptMondownRmonCrcErrorsCounterClientOutputValuePortn": pm10010mptMondownRmonCrcErrorsCounterClientOutputValuePortn,
       "pm10010mptMondownRmonCrcErrorsCounterClientOutputErrorPortn": pm10010mptMondownRmonCrcErrorsCounterClientOutputErrorPortn,
       "pm10010mptMondownRmonCrcErrorsCounterClientOutputOverloadPortn": pm10010mptMondownRmonCrcErrorsCounterClientOutputOverloadPortn,
       "pm10010mptMondownRmonPacketsCounterClientOutputTable": pm10010mptMondownRmonPacketsCounterClientOutputTable,
       "pm10010mptMondownRmonPacketsCounterClientOutputEntry": pm10010mptMondownRmonPacketsCounterClientOutputEntry,
       "pm10010mptMondownRmonPacketsCounterClientOutputIndex": pm10010mptMondownRmonPacketsCounterClientOutputIndex,
       "pm10010mptMondownRmonPacketsCounterClientOutputValuePortn": pm10010mptMondownRmonPacketsCounterClientOutputValuePortn,
       "pm10010mptMondownRmonPacketsCounterClientOutputErrorPortn": pm10010mptMondownRmonPacketsCounterClientOutputErrorPortn,
       "pm10010mptMondownRmonPacketsCounterClientOutputOverloadPortn": pm10010mptMondownRmonPacketsCounterClientOutputOverloadPortn,
       "pm10010mptMondownRmonBroadcastCounterClientOutputTable": pm10010mptMondownRmonBroadcastCounterClientOutputTable,
       "pm10010mptMondownRmonBroadcastCounterClientOutputEntry": pm10010mptMondownRmonBroadcastCounterClientOutputEntry,
       "pm10010mptMondownRmonBroadcastCounterClientOutputIndex": pm10010mptMondownRmonBroadcastCounterClientOutputIndex,
       "pm10010mptMondownRmonBroadcastCounterClientOutputValuePortn": pm10010mptMondownRmonBroadcastCounterClientOutputValuePortn,
       "pm10010mptMondownRmonBroadcastCounterClientOutputErrorPortn": pm10010mptMondownRmonBroadcastCounterClientOutputErrorPortn,
       "pm10010mptMondownRmonBroadcastCounterClientOutputOverloadPortn": pm10010mptMondownRmonBroadcastCounterClientOutputOverloadPortn,
       "pm10010mptMondownRmonMulticastCounterClientOutputTable": pm10010mptMondownRmonMulticastCounterClientOutputTable,
       "pm10010mptMondownRmonMulticastCounterClientOutputEntry": pm10010mptMondownRmonMulticastCounterClientOutputEntry,
       "pm10010mptMondownRmonMulticastCounterClientOutputIndex": pm10010mptMondownRmonMulticastCounterClientOutputIndex,
       "pm10010mptMondownRmonMulticastCounterClientOutputValuePortn": pm10010mptMondownRmonMulticastCounterClientOutputValuePortn,
       "pm10010mptMondownRmonMulticastCounterClientOutputErrorPortn": pm10010mptMondownRmonMulticastCounterClientOutputErrorPortn,
       "pm10010mptMondownRmonMulticastCounterClientOutputOverloadPortn": pm10010mptMondownRmonMulticastCounterClientOutputOverloadPortn,
       "pm10010mptMondownRmonPauseFrameCounterClientOutputTable": pm10010mptMondownRmonPauseFrameCounterClientOutputTable,
       "pm10010mptMondownRmonPauseFrameCounterClientOutputEntry": pm10010mptMondownRmonPauseFrameCounterClientOutputEntry,
       "pm10010mptMondownRmonPauseFrameCounterClientOutputIndex": pm10010mptMondownRmonPauseFrameCounterClientOutputIndex,
       "pm10010mptMondownRmonPauseFrameCounterClientOutputValuePortn": pm10010mptMondownRmonPauseFrameCounterClientOutputValuePortn,
       "pm10010mptMondownRmonPauseFrameCounterClientOutputErrorPortn": pm10010mptMondownRmonPauseFrameCounterClientOutputErrorPortn,
       "pm10010mptMondownRmonPauseFrameCounterClientOutputOverloadPortn": pm10010mptMondownRmonPauseFrameCounterClientOutputOverloadPortn,
       "pm10010mptMondownRmonUnicastCounterClientOutputTable": pm10010mptMondownRmonUnicastCounterClientOutputTable,
       "pm10010mptMondownRmonUnicastCounterClientOutputEntry": pm10010mptMondownRmonUnicastCounterClientOutputEntry,
       "pm10010mptMondownRmonUnicastCounterClientOutputIndex": pm10010mptMondownRmonUnicastCounterClientOutputIndex,
       "pm10010mptMondownRmonUnicastCounterClientOutputValuePortn": pm10010mptMondownRmonUnicastCounterClientOutputValuePortn,
       "pm10010mptMondownRmonUnicastCounterClientOutputErrorPortn": pm10010mptMondownRmonUnicastCounterClientOutputErrorPortn,
       "pm10010mptMondownRmonUnicastCounterClientOutputOverloadPortn": pm10010mptMondownRmonUnicastCounterClientOutputOverloadPortn,
       "pm10010mptMondownRmonNonunicastCounterClientOutputTable": pm10010mptMondownRmonNonunicastCounterClientOutputTable,
       "pm10010mptMondownRmonNonunicastCounterClientOutputEntry": pm10010mptMondownRmonNonunicastCounterClientOutputEntry,
       "pm10010mptMondownRmonNonunicastCounterClientOutputIndex": pm10010mptMondownRmonNonunicastCounterClientOutputIndex,
       "pm10010mptMondownRmonNonunicastCounterClientOutputValuePortn": pm10010mptMondownRmonNonunicastCounterClientOutputValuePortn,
       "pm10010mptMondownRmonNonunicastCounterClientOutputErrorPortn": pm10010mptMondownRmonNonunicastCounterClientOutputErrorPortn,
       "pm10010mptMondownRmonNonunicastCounterClientOutputOverloadPortn": pm10010mptMondownRmonNonunicastCounterClientOutputOverloadPortn,
       "pm10010mptMonPerfOther": pm10010mptMonPerfOther,
       "pm10010mptMonPerfSync": pm10010mptMonPerfSync,
       "pm10010mptPerfEnable": pm10010mptPerfEnable,
       "pm10010mptPerf15minSync": pm10010mptPerf15minSync,
       "pm10010mptPerf24hSync": pm10010mptPerf24hSync,
       "pm10010mptMonPerfTimeStamp": pm10010mptMonPerfTimeStamp,
       "pm10010mptPerf15MinShort": pm10010mptPerf15MinShort,
       "pm10010mptPerf15MinLong": pm10010mptPerf15MinLong,
       "pm10010mptPerf24HoursShort": pm10010mptPerf24HoursShort,
       "pm10010mptPerf24HoursLong": pm10010mptPerf24HoursLong,
       "pm10010mptPerfCurrent15MinElapsedTime": pm10010mptPerfCurrent15MinElapsedTime,
       "pm10010mptPerfCurrent24HoursElapsedTime": pm10010mptPerfCurrent24HoursElapsedTime,
       "pm10010mptMonPerfClient": pm10010mptMonPerfClient,
       "pm10010mptPerfTelecomInputClientCurrent15StatTable": pm10010mptPerfTelecomInputClientCurrent15StatTable,
       "pm10010mptPerfTelecomInputClientCurrent15StatEntry": pm10010mptPerfTelecomInputClientCurrent15StatEntry,
       "pm10010mptPerfTelecomInputClientCurrent15StatIndex": pm10010mptPerfTelecomInputClientCurrent15StatIndex,
       "pm10010mptPerfTelecomInputClientCurrent15StatInvCvPortn": pm10010mptPerfTelecomInputClientCurrent15StatInvCvPortn,
       "pm10010mptPerfTelecomInputClientCurrent15StatCvValuePortn": pm10010mptPerfTelecomInputClientCurrent15StatCvValuePortn,
       "pm10010mptPerfTelecomInputClientCurrent15StatInvEsPortn": pm10010mptPerfTelecomInputClientCurrent15StatInvEsPortn,
       "pm10010mptPerfTelecomInputClientCurrent15StatEsValuePortn": pm10010mptPerfTelecomInputClientCurrent15StatEsValuePortn,
       "pm10010mptPerfTelecomInputClientCurrent15StatInvSesPortn": pm10010mptPerfTelecomInputClientCurrent15StatInvSesPortn,
       "pm10010mptPerfTelecomInputClientCurrent15StatSesValuePortn": pm10010mptPerfTelecomInputClientCurrent15StatSesValuePortn,
       "pm10010mptPerfTelecomInputClientCurrent15StatInvSefsPortn": pm10010mptPerfTelecomInputClientCurrent15StatInvSefsPortn,
       "pm10010mptPerfTelecomInputClientCurrent15StatSefsValuePortn": pm10010mptPerfTelecomInputClientCurrent15StatSefsValuePortn,
       "pm10010mptPerfTelecomInputClientCurrent15StatInvUasPortn": pm10010mptPerfTelecomInputClientCurrent15StatInvUasPortn,
       "pm10010mptPerfTelecomInputClientCurrent15StatUasValuePortn": pm10010mptPerfTelecomInputClientCurrent15StatUasValuePortn,
       "pm10010mptPerfTelecomInputClientPast15StatHistoryPort1Table": pm10010mptPerfTelecomInputClientPast15StatHistoryPort1Table,
       "pm10010mptPerfTelecomInputClientPast15StatHistoryPort1Entry": pm10010mptPerfTelecomInputClientPast15StatHistoryPort1Entry,
       "pm10010mptPerfTelecomInputClientPast15StatHistoryPort1Index": pm10010mptPerfTelecomInputClientPast15StatHistoryPort1Index,
       "pm10010mptPerfTelecomInputClientPast15StatHistoryInvCvPort1": pm10010mptPerfTelecomInputClientPast15StatHistoryInvCvPort1,
       "pm10010mptPerfTelecomInputClientPast15StatHistoryCvValuePort1": pm10010mptPerfTelecomInputClientPast15StatHistoryCvValuePort1,
       "pm10010mptPerfTelecomInputClientPast15StatHistoryInvEsPort1": pm10010mptPerfTelecomInputClientPast15StatHistoryInvEsPort1,
       "pm10010mptPerfTelecomInputClientPast15StatHistoryEsValuePort1": pm10010mptPerfTelecomInputClientPast15StatHistoryEsValuePort1,
       "pm10010mptPerfTelecomInputClientPast15StatHistoryInvSesPort1": pm10010mptPerfTelecomInputClientPast15StatHistoryInvSesPort1,
       "pm10010mptPerfTelecomInputClientPast15StatHistorySesValuePort1": pm10010mptPerfTelecomInputClientPast15StatHistorySesValuePort1,
       "pm10010mptPerfTelecomInputClientPast15StatHistoryInvSefsPort1": pm10010mptPerfTelecomInputClientPast15StatHistoryInvSefsPort1,
       "pm10010mptPerfTelecomInputClientPast15StatHistorySefsValuePort1": pm10010mptPerfTelecomInputClientPast15StatHistorySefsValuePort1,
       "pm10010mptPerfTelecomInputClientPast15StatHistoryInvUasPort1": pm10010mptPerfTelecomInputClientPast15StatHistoryInvUasPort1,
       "pm10010mptPerfTelecomInputClientPast15StatHistoryUasValuePort1": pm10010mptPerfTelecomInputClientPast15StatHistoryUasValuePort1,
       "pm10010mptPerfTelecomInputClientCurrent24StatTable": pm10010mptPerfTelecomInputClientCurrent24StatTable,
       "pm10010mptPerfTelecomInputClientCurrent24StatEntry": pm10010mptPerfTelecomInputClientCurrent24StatEntry,
       "pm10010mptPerfTelecomInputClientCurrent24StatIndex": pm10010mptPerfTelecomInputClientCurrent24StatIndex,
       "pm10010mptPerfTelecomInputClientCurrent24StatInvCvPortn": pm10010mptPerfTelecomInputClientCurrent24StatInvCvPortn,
       "pm10010mptPerfTelecomInputClientCurrent24StatCvValuePortn": pm10010mptPerfTelecomInputClientCurrent24StatCvValuePortn,
       "pm10010mptPerfTelecomInputClientCurrent24StatInvEsPortn": pm10010mptPerfTelecomInputClientCurrent24StatInvEsPortn,
       "pm10010mptPerfTelecomInputClientCurrent24StatEsValuePortn": pm10010mptPerfTelecomInputClientCurrent24StatEsValuePortn,
       "pm10010mptPerfTelecomInputClientCurrent24StatInvSesPortn": pm10010mptPerfTelecomInputClientCurrent24StatInvSesPortn,
       "pm10010mptPerfTelecomInputClientCurrent24StatSesValuePortn": pm10010mptPerfTelecomInputClientCurrent24StatSesValuePortn,
       "pm10010mptPerfTelecomInputClientCurrent24StatInvSefsPortn": pm10010mptPerfTelecomInputClientCurrent24StatInvSefsPortn,
       "pm10010mptPerfTelecomInputClientCurrent24StatSefsValuePortn": pm10010mptPerfTelecomInputClientCurrent24StatSefsValuePortn,
       "pm10010mptPerfTelecomInputClientCurrent24StatInvUasPortn": pm10010mptPerfTelecomInputClientCurrent24StatInvUasPortn,
       "pm10010mptPerfTelecomInputClientCurrent24StatUasValuePortn": pm10010mptPerfTelecomInputClientCurrent24StatUasValuePortn,
       "pm10010mptPerfTelecomInputClientPast24StatHistoryPort1Table": pm10010mptPerfTelecomInputClientPast24StatHistoryPort1Table,
       "pm10010mptPerfTelecomInputClientPast24StatHistoryPort1Entry": pm10010mptPerfTelecomInputClientPast24StatHistoryPort1Entry,
       "pm10010mptPerfTelecomInputClientPast24StatHistoryPort1Index": pm10010mptPerfTelecomInputClientPast24StatHistoryPort1Index,
       "pm10010mptPerfTelecomInputClientPast24StatHistoryInvCvPort1": pm10010mptPerfTelecomInputClientPast24StatHistoryInvCvPort1,
       "pm10010mptPerfTelecomInputClientPast24StatHistoryCvValuePort1": pm10010mptPerfTelecomInputClientPast24StatHistoryCvValuePort1,
       "pm10010mptPerfTelecomInputClientPast24StatHistoryInvEsPort1": pm10010mptPerfTelecomInputClientPast24StatHistoryInvEsPort1,
       "pm10010mptPerfTelecomInputClientPast24StatHistoryEsValuePort1": pm10010mptPerfTelecomInputClientPast24StatHistoryEsValuePort1,
       "pm10010mptPerfTelecomInputClientPast24StatHistoryInvSesPort1": pm10010mptPerfTelecomInputClientPast24StatHistoryInvSesPort1,
       "pm10010mptPerfTelecomInputClientPast24StatHistorySesValuePort1": pm10010mptPerfTelecomInputClientPast24StatHistorySesValuePort1,
       "pm10010mptPerfTelecomInputClientPast24StatHistoryInvSefsPort1": pm10010mptPerfTelecomInputClientPast24StatHistoryInvSefsPort1,
       "pm10010mptPerfTelecomInputClientPast24StatHistorySefsValuePort1": pm10010mptPerfTelecomInputClientPast24StatHistorySefsValuePort1,
       "pm10010mptPerfTelecomInputClientPast24StatHistoryInvUasPort1": pm10010mptPerfTelecomInputClientPast24StatHistoryInvUasPort1,
       "pm10010mptPerfTelecomInputClientPast24StatHistoryUasValuePort1": pm10010mptPerfTelecomInputClientPast24StatHistoryUasValuePort1,
       "pm10010mptPerfTelecomOutputClientCurrent15StatTable": pm10010mptPerfTelecomOutputClientCurrent15StatTable,
       "pm10010mptPerfTelecomOutputClientCurrent15StatEntry": pm10010mptPerfTelecomOutputClientCurrent15StatEntry,
       "pm10010mptPerfTelecomOutputClientCurrent15StatIndex": pm10010mptPerfTelecomOutputClientCurrent15StatIndex,
       "pm10010mptPerfTelecomOutputClientCurrent15StatInvCvPortn": pm10010mptPerfTelecomOutputClientCurrent15StatInvCvPortn,
       "pm10010mptPerfTelecomOutputClientCurrent15StatCvValuePortn": pm10010mptPerfTelecomOutputClientCurrent15StatCvValuePortn,
       "pm10010mptPerfTelecomOutputClientCurrent15StatInvEsPortn": pm10010mptPerfTelecomOutputClientCurrent15StatInvEsPortn,
       "pm10010mptPerfTelecomOutputClientCurrent15StatEsValuePortn": pm10010mptPerfTelecomOutputClientCurrent15StatEsValuePortn,
       "pm10010mptPerfTelecomOutputClientCurrent15StatInvSesPortn": pm10010mptPerfTelecomOutputClientCurrent15StatInvSesPortn,
       "pm10010mptPerfTelecomOutputClientCurrent15StatSesValuePortn": pm10010mptPerfTelecomOutputClientCurrent15StatSesValuePortn,
       "pm10010mptPerfTelecomOutputClientCurrent15StatInvSefsPortn": pm10010mptPerfTelecomOutputClientCurrent15StatInvSefsPortn,
       "pm10010mptPerfTelecomOutputClientCurrent15StatSefsValuePortn": pm10010mptPerfTelecomOutputClientCurrent15StatSefsValuePortn,
       "pm10010mptPerfTelecomOutputClientCurrent15StatInvUasPortn": pm10010mptPerfTelecomOutputClientCurrent15StatInvUasPortn,
       "pm10010mptPerfTelecomOutputClientCurrent15StatUasValuePortn": pm10010mptPerfTelecomOutputClientCurrent15StatUasValuePortn,
       "pm10010mptPerfTelecomOutputClientPast15StatHistoryPort1Table": pm10010mptPerfTelecomOutputClientPast15StatHistoryPort1Table,
       "pm10010mptPerfTelecomOutputClientPast15StatHistoryPort1Entry": pm10010mptPerfTelecomOutputClientPast15StatHistoryPort1Entry,
       "pm10010mptPerfTelecomOutputClientPast15StatHistoryPort1Index": pm10010mptPerfTelecomOutputClientPast15StatHistoryPort1Index,
       "pm10010mptPerfTelecomOutputClientPast15StatHistoryInvCvPort1": pm10010mptPerfTelecomOutputClientPast15StatHistoryInvCvPort1,
       "pm10010mptPerfTelecomOutputClientPast15StatHistoryCvValuePort1": pm10010mptPerfTelecomOutputClientPast15StatHistoryCvValuePort1,
       "pm10010mptPerfTelecomOutputClientPast15StatHistoryInvEsPort1": pm10010mptPerfTelecomOutputClientPast15StatHistoryInvEsPort1,
       "pm10010mptPerfTelecomOutputClientPast15StatHistoryEsValuePort1": pm10010mptPerfTelecomOutputClientPast15StatHistoryEsValuePort1,
       "pm10010mptPerfTelecomOutputClientPast15StatHistoryInvSesPort1": pm10010mptPerfTelecomOutputClientPast15StatHistoryInvSesPort1,
       "pm10010mptPerfTelecomOutputClientPast15StatHistorySesValuePort1": pm10010mptPerfTelecomOutputClientPast15StatHistorySesValuePort1,
       "pm10010mptPerfTelecomOutputClientPast15StatHistoryInvSefsPort1": pm10010mptPerfTelecomOutputClientPast15StatHistoryInvSefsPort1,
       "pm10010mptPerfTelecomOutputClientPast15StatHistorySefsValuePort1": pm10010mptPerfTelecomOutputClientPast15StatHistorySefsValuePort1,
       "pm10010mptPerfTelecomOutputClientPast15StatHistoryInvUasPort1": pm10010mptPerfTelecomOutputClientPast15StatHistoryInvUasPort1,
       "pm10010mptPerfTelecomOutputClientPast15StatHistoryUasValuePort1": pm10010mptPerfTelecomOutputClientPast15StatHistoryUasValuePort1,
       "pm10010mptPerfTelecomOutputClientCurrent24StatTable": pm10010mptPerfTelecomOutputClientCurrent24StatTable,
       "pm10010mptPerfTelecomOutputClientCurrent24StatEntry": pm10010mptPerfTelecomOutputClientCurrent24StatEntry,
       "pm10010mptPerfTelecomOutputClientCurrent24StatIndex": pm10010mptPerfTelecomOutputClientCurrent24StatIndex,
       "pm10010mptPerfTelecomOutputClientCurrent24StatInvCvPortn": pm10010mptPerfTelecomOutputClientCurrent24StatInvCvPortn,
       "pm10010mptPerfTelecomOutputClientCurrent24StatCvValuePortn": pm10010mptPerfTelecomOutputClientCurrent24StatCvValuePortn,
       "pm10010mptPerfTelecomOutputClientCurrent24StatInvEsPortn": pm10010mptPerfTelecomOutputClientCurrent24StatInvEsPortn,
       "pm10010mptPerfTelecomOutputClientCurrent24StatEsValuePortn": pm10010mptPerfTelecomOutputClientCurrent24StatEsValuePortn,
       "pm10010mptPerfTelecomOutputClientCurrent24StatInvSesPortn": pm10010mptPerfTelecomOutputClientCurrent24StatInvSesPortn,
       "pm10010mptPerfTelecomOutputClientCurrent24StatSesValuePortn": pm10010mptPerfTelecomOutputClientCurrent24StatSesValuePortn,
       "pm10010mptPerfTelecomOutputClientCurrent24StatInvSefsPortn": pm10010mptPerfTelecomOutputClientCurrent24StatInvSefsPortn,
       "pm10010mptPerfTelecomOutputClientCurrent24StatSefsValuePortn": pm10010mptPerfTelecomOutputClientCurrent24StatSefsValuePortn,
       "pm10010mptPerfTelecomOutputClientCurrent24StatInvUasPortn": pm10010mptPerfTelecomOutputClientCurrent24StatInvUasPortn,
       "pm10010mptPerfTelecomOutputClientCurrent24StatUasValuePortn": pm10010mptPerfTelecomOutputClientCurrent24StatUasValuePortn,
       "pm10010mptPerfTelecomOutputClientPast24StatHistoryPort1Table": pm10010mptPerfTelecomOutputClientPast24StatHistoryPort1Table,
       "pm10010mptPerfTelecomOutputClientPast24StatHistoryPort1Entry": pm10010mptPerfTelecomOutputClientPast24StatHistoryPort1Entry,
       "pm10010mptPerfTelecomOutputClientPast24StatHistoryPort1Index": pm10010mptPerfTelecomOutputClientPast24StatHistoryPort1Index,
       "pm10010mptPerfTelecomOutputClientPast24StatHistoryInvCvPort1": pm10010mptPerfTelecomOutputClientPast24StatHistoryInvCvPort1,
       "pm10010mptPerfTelecomOutputClientPast24StatHistoryCvValuePort1": pm10010mptPerfTelecomOutputClientPast24StatHistoryCvValuePort1,
       "pm10010mptPerfTelecomOutputClientPast24StatHistoryInvEsPort1": pm10010mptPerfTelecomOutputClientPast24StatHistoryInvEsPort1,
       "pm10010mptPerfTelecomOutputClientPast24StatHistoryEsValuePort1": pm10010mptPerfTelecomOutputClientPast24StatHistoryEsValuePort1,
       "pm10010mptPerfTelecomOutputClientPast24StatHistoryInvSesPort1": pm10010mptPerfTelecomOutputClientPast24StatHistoryInvSesPort1,
       "pm10010mptPerfTelecomOutputClientPast24StatHistorySesValuePort1": pm10010mptPerfTelecomOutputClientPast24StatHistorySesValuePort1,
       "pm10010mptPerfTelecomOutputClientPast24StatHistoryInvSefsPort1": pm10010mptPerfTelecomOutputClientPast24StatHistoryInvSefsPort1,
       "pm10010mptPerfTelecomOutputClientPast24StatHistorySefsValuePort1": pm10010mptPerfTelecomOutputClientPast24StatHistorySefsValuePort1,
       "pm10010mptPerfTelecomOutputClientPast24StatHistoryInvUasPort1": pm10010mptPerfTelecomOutputClientPast24StatHistoryInvUasPort1,
       "pm10010mptPerfTelecomOutputClientPast24StatHistoryUasValuePort1": pm10010mptPerfTelecomOutputClientPast24StatHistoryUasValuePort1,
       "pm10010mptPerfDatacomClientCurrent15StatTable": pm10010mptPerfDatacomClientCurrent15StatTable,
       "pm10010mptPerfDatacomClientCurrent15StatEntry": pm10010mptPerfDatacomClientCurrent15StatEntry,
       "pm10010mptPerfDatacomClientCurrent15StatIndex": pm10010mptPerfDatacomClientCurrent15StatIndex,
       "rm10010perfdatacomclientCurrent15StatInCrcCountInvPortn": rm10010perfdatacomclientCurrent15StatInCrcCountInvPortn,
       "rm10010perfdatacomclientCurrent15StatInCrcCountPortn": rm10010perfdatacomclientCurrent15StatInCrcCountPortn,
       "rm10010perfdatacomclientCurrent15StatInPacketCountInvPortn": rm10010perfdatacomclientCurrent15StatInPacketCountInvPortn,
       "rm10010perfdatacomclientCurrent15StatInPacketCountPortn": rm10010perfdatacomclientCurrent15StatInPacketCountPortn,
       "rm10010perfdatacomclientCurrent15StatOutCrcCountInvPortn": rm10010perfdatacomclientCurrent15StatOutCrcCountInvPortn,
       "rm10010perfdatacomclientCurrent15StatOutCrcCountPortn": rm10010perfdatacomclientCurrent15StatOutCrcCountPortn,
       "rm10010perfdatacomclientCurrent15StatOutPacketCountInvPortn": rm10010perfdatacomclientCurrent15StatOutPacketCountInvPortn,
       "rm10010perfdatacomclientCurrent15StatOutPacketCountPortn": rm10010perfdatacomclientCurrent15StatOutPacketCountPortn,
       "pm10010mptPerfDatacomClientPast15StatHistoryPort1Table": pm10010mptPerfDatacomClientPast15StatHistoryPort1Table,
       "pm10010mptPerfDatacomClientPast15StatHistoryPort1Entry": pm10010mptPerfDatacomClientPast15StatHistoryPort1Entry,
       "pm10010mptPerfDatacomClientPast15StatHistoryPort1Index": pm10010mptPerfDatacomClientPast15StatHistoryPort1Index,
       "rm10010perfdatacomclientPast15StatInCrcCountInvPort1": rm10010perfdatacomclientPast15StatInCrcCountInvPort1,
       "rm10010perfdatacomclientPast15StatInCrcCountPort1": rm10010perfdatacomclientPast15StatInCrcCountPort1,
       "rm10010perfdatacomclientPast15StatInPacketCountInvPort1": rm10010perfdatacomclientPast15StatInPacketCountInvPort1,
       "rm10010perfdatacomclientPast15StatInPacketCountPort1": rm10010perfdatacomclientPast15StatInPacketCountPort1,
       "rm10010perfdatacomclientPast15StatOutCrcCountInvPort1": rm10010perfdatacomclientPast15StatOutCrcCountInvPort1,
       "rm10010perfdatacomclientPast15StatOutCrcCountPort1": rm10010perfdatacomclientPast15StatOutCrcCountPort1,
       "rm10010perfdatacomclientPast15StatOutPacketCountInvPort1": rm10010perfdatacomclientPast15StatOutPacketCountInvPort1,
       "rm10010perfdatacomclientPast15StatOutPacketCountPort1": rm10010perfdatacomclientPast15StatOutPacketCountPort1,
       "pm10010mptPerfDatacomClientCurrent24StatTable": pm10010mptPerfDatacomClientCurrent24StatTable,
       "pm10010mptPerfDatacomClientCurrent24StatEntry": pm10010mptPerfDatacomClientCurrent24StatEntry,
       "pm10010mptPerfDatacomClientCurrent24StatIndex": pm10010mptPerfDatacomClientCurrent24StatIndex,
       "rm10010perfdatacomclientCurrent24StatInCrcCountInvPortn": rm10010perfdatacomclientCurrent24StatInCrcCountInvPortn,
       "rm10010perfdatacomclientCurrent24StatInCrcCountPortn": rm10010perfdatacomclientCurrent24StatInCrcCountPortn,
       "rm10010perfdatacomclientCurrent24StatInPacketCountInvPortn": rm10010perfdatacomclientCurrent24StatInPacketCountInvPortn,
       "rm10010perfdatacomclientCurrent24StatInPacketCountPortn": rm10010perfdatacomclientCurrent24StatInPacketCountPortn,
       "rm10010perfdatacomclientCurrent24StatOutCrcCountInvPortn": rm10010perfdatacomclientCurrent24StatOutCrcCountInvPortn,
       "rm10010perfdatacomclientCurrent24StatOutCrcCountPortn": rm10010perfdatacomclientCurrent24StatOutCrcCountPortn,
       "rm10010perfdatacomclientCurrent24StatOutPacketCountInvPortn": rm10010perfdatacomclientCurrent24StatOutPacketCountInvPortn,
       "rm10010perfdatacomclientCurrent24StatOutPacketCountPortn": rm10010perfdatacomclientCurrent24StatOutPacketCountPortn,
       "pm10010mptPerfDatacomClientPast24StatHistoryPort1Table": pm10010mptPerfDatacomClientPast24StatHistoryPort1Table,
       "pm10010mptPerfDatacomClientPast24StatHistoryPort1Entry": pm10010mptPerfDatacomClientPast24StatHistoryPort1Entry,
       "pm10010mptPerfDatacomClientPast24StatHistoryPort1Index": pm10010mptPerfDatacomClientPast24StatHistoryPort1Index,
       "rm10010perfdatacomclientPast24StatInCrcCountInvPort1": rm10010perfdatacomclientPast24StatInCrcCountInvPort1,
       "rm10010perfdatacomclientPast24StatInCrcCountPort1": rm10010perfdatacomclientPast24StatInCrcCountPort1,
       "rm10010perfdatacomclientPast24StatInPacketCountInvPort1": rm10010perfdatacomclientPast24StatInPacketCountInvPort1,
       "rm10010perfdatacomclientPast24StatInPacketCountPort1": rm10010perfdatacomclientPast24StatInPacketCountPort1,
       "rm10010perfdatacomclientPast24StatOutCrcCountInvPort1": rm10010perfdatacomclientPast24StatOutCrcCountInvPort1,
       "rm10010perfdatacomclientPast24StatOutCrcCountPort1": rm10010perfdatacomclientPast24StatOutCrcCountPort1,
       "rm10010perfdatacomclientPast24StatOutPacketCountInvPort1": rm10010perfdatacomclientPast24StatOutPacketCountInvPort1,
       "rm10010perfdatacomclientPast24StatOutPacketCountPort1": rm10010perfdatacomclientPast24StatOutPacketCountPort1,
       "pm10010mptMonPerfLine": pm10010mptMonPerfLine,
       "pm10010mptPerfTelecomLinePostFecCurrent15StatTable": pm10010mptPerfTelecomLinePostFecCurrent15StatTable,
       "pm10010mptPerfTelecomLinePostFecCurrent15StatEntry": pm10010mptPerfTelecomLinePostFecCurrent15StatEntry,
       "pm10010mptPerfTelecomLinePostFecCurrent15StatIndex": pm10010mptPerfTelecomLinePostFecCurrent15StatIndex,
       "pm10010mptPerfTelecomLinePostFecCurrent15StatInvCvPortn": pm10010mptPerfTelecomLinePostFecCurrent15StatInvCvPortn,
       "pm10010mptPerfTelecomLinePostFecCurrent15StatCvValuePortn": pm10010mptPerfTelecomLinePostFecCurrent15StatCvValuePortn,
       "pm10010mptPerfTelecomLinePostFecCurrent15StatInvEsPortn": pm10010mptPerfTelecomLinePostFecCurrent15StatInvEsPortn,
       "pm10010mptPerfTelecomLinePostFecCurrent15StatEsValuePortn": pm10010mptPerfTelecomLinePostFecCurrent15StatEsValuePortn,
       "pm10010mptPerfTelecomLinePostFecCurrent15StatInvSesPortn": pm10010mptPerfTelecomLinePostFecCurrent15StatInvSesPortn,
       "pm10010mptPerfTelecomLinePostFecCurrent15StatSesValuePortn": pm10010mptPerfTelecomLinePostFecCurrent15StatSesValuePortn,
       "pm10010mptPerfTelecomLinePostFecCurrent15StatInvSefsPortn": pm10010mptPerfTelecomLinePostFecCurrent15StatInvSefsPortn,
       "pm10010mptPerfTelecomLinePostFecCurrent15StatSefsValuePortn": pm10010mptPerfTelecomLinePostFecCurrent15StatSefsValuePortn,
       "pm10010mptPerfTelecomLinePostFecCurrent15StatInvUasPortn": pm10010mptPerfTelecomLinePostFecCurrent15StatInvUasPortn,
       "pm10010mptPerfTelecomLinePostFecCurrent15StatUasValuePortn": pm10010mptPerfTelecomLinePostFecCurrent15StatUasValuePortn,
       "pm10010mptPerfTelecomLinePostFecPast15StatHistoryPort1Table": pm10010mptPerfTelecomLinePostFecPast15StatHistoryPort1Table,
       "pm10010mptPerfTelecomLinePostFecPast15StatHistoryPort1Entry": pm10010mptPerfTelecomLinePostFecPast15StatHistoryPort1Entry,
       "pm10010mptPerfTelecomLinePostFecPast15StatHistoryPort1Index": pm10010mptPerfTelecomLinePostFecPast15StatHistoryPort1Index,
       "pm10010mptPerfTelecomLinePostFecPast15StatHistoryInvCvPort1": pm10010mptPerfTelecomLinePostFecPast15StatHistoryInvCvPort1,
       "pm10010mptPerfTelecomLinePostFecPast15StatHistoryCvValuePort1": pm10010mptPerfTelecomLinePostFecPast15StatHistoryCvValuePort1,
       "pm10010mptPerfTelecomLinePostFecPast15StatHistoryInvEsPort1": pm10010mptPerfTelecomLinePostFecPast15StatHistoryInvEsPort1,
       "pm10010mptPerfTelecomLinePostFecPast15StatHistoryEsValuePort1": pm10010mptPerfTelecomLinePostFecPast15StatHistoryEsValuePort1,
       "pm10010mptPerfTelecomLinePostFecPast15StatHistoryInvSesPort1": pm10010mptPerfTelecomLinePostFecPast15StatHistoryInvSesPort1,
       "pm10010mptPerfTelecomLinePostFecPast15StatHistorySesValuePort1": pm10010mptPerfTelecomLinePostFecPast15StatHistorySesValuePort1,
       "pm10010mptPerfTelecomLinePostFecPast15StatHistoryInvSefsPort1": pm10010mptPerfTelecomLinePostFecPast15StatHistoryInvSefsPort1,
       "pm10010mptPerfTelecomLinePostFecPast15StatHistorySefsValuePort1": pm10010mptPerfTelecomLinePostFecPast15StatHistorySefsValuePort1,
       "pm10010mptPerfTelecomLinePostFecPast15StatHistoryInvUasPort1": pm10010mptPerfTelecomLinePostFecPast15StatHistoryInvUasPort1,
       "pm10010mptPerfTelecomLinePostFecPast15StatHistoryUasValuePort1": pm10010mptPerfTelecomLinePostFecPast15StatHistoryUasValuePort1,
       "pm10010mptPerfTelecomLinePostFecCurrent24StatTable": pm10010mptPerfTelecomLinePostFecCurrent24StatTable,
       "pm10010mptPerfTelecomLinePostFecCurrent24StatEntry": pm10010mptPerfTelecomLinePostFecCurrent24StatEntry,
       "pm10010mptPerfTelecomLinePostFecCurrent24StatIndex": pm10010mptPerfTelecomLinePostFecCurrent24StatIndex,
       "pm10010mptPerfTelecomLinePostFecCurrent24StatInvCvPortn": pm10010mptPerfTelecomLinePostFecCurrent24StatInvCvPortn,
       "pm10010mptPerfTelecomLinePostFecCurrent24StatCvValuePortn": pm10010mptPerfTelecomLinePostFecCurrent24StatCvValuePortn,
       "pm10010mptPerfTelecomLinePostFecCurrent24StatInvEsPortn": pm10010mptPerfTelecomLinePostFecCurrent24StatInvEsPortn,
       "pm10010mptPerfTelecomLinePostFecCurrent24StatEsValuePortn": pm10010mptPerfTelecomLinePostFecCurrent24StatEsValuePortn,
       "pm10010mptPerfTelecomLinePostFecCurrent24StatInvSesPortn": pm10010mptPerfTelecomLinePostFecCurrent24StatInvSesPortn,
       "pm10010mptPerfTelecomLinePostFecCurrent24StatSesValuePortn": pm10010mptPerfTelecomLinePostFecCurrent24StatSesValuePortn,
       "pm10010mptPerfTelecomLinePostFecCurrent24StatInvSefsPortn": pm10010mptPerfTelecomLinePostFecCurrent24StatInvSefsPortn,
       "pm10010mptPerfTelecomLinePostFecCurrent24StatSefsValuePortn": pm10010mptPerfTelecomLinePostFecCurrent24StatSefsValuePortn,
       "pm10010mptPerfTelecomLinePostFecCurrent24StatInvUasPortn": pm10010mptPerfTelecomLinePostFecCurrent24StatInvUasPortn,
       "pm10010mptPerfTelecomLinePostFecCurrent24StatUasValuePortn": pm10010mptPerfTelecomLinePostFecCurrent24StatUasValuePortn,
       "pm10010mptPerfTelecomLinePostFecPast24StatHistoryPort1Table": pm10010mptPerfTelecomLinePostFecPast24StatHistoryPort1Table,
       "pm10010mptPerfTelecomLinePostFecPast24StatHistoryPort1Entry": pm10010mptPerfTelecomLinePostFecPast24StatHistoryPort1Entry,
       "pm10010mptPerfTelecomLinePostFecPast24StatHistoryPort1Index": pm10010mptPerfTelecomLinePostFecPast24StatHistoryPort1Index,
       "pm10010mptPerfTelecomLinePostFecPast24StatHistoryInvCvPort1": pm10010mptPerfTelecomLinePostFecPast24StatHistoryInvCvPort1,
       "pm10010mptPerfTelecomLinePostFecPast24StatHistoryCvValuePort1": pm10010mptPerfTelecomLinePostFecPast24StatHistoryCvValuePort1,
       "pm10010mptPerfTelecomLinePostFecPast24StatHistoryInvEsPort1": pm10010mptPerfTelecomLinePostFecPast24StatHistoryInvEsPort1,
       "pm10010mptPerfTelecomLinePostFecPast24StatHistoryEsValuePort1": pm10010mptPerfTelecomLinePostFecPast24StatHistoryEsValuePort1,
       "pm10010mptPerfTelecomLinePostFecPast24StatHistoryInvSesPort1": pm10010mptPerfTelecomLinePostFecPast24StatHistoryInvSesPort1,
       "pm10010mptPerfTelecomLinePostFecPast24StatHistorySesValuePort1": pm10010mptPerfTelecomLinePostFecPast24StatHistorySesValuePort1,
       "pm10010mptPerfTelecomLinePostFecPast24StatHistoryInvSefsPort1": pm10010mptPerfTelecomLinePostFecPast24StatHistoryInvSefsPort1,
       "pm10010mptPerfTelecomLinePostFecPast24StatHistorySefsValuePort1": pm10010mptPerfTelecomLinePostFecPast24StatHistorySefsValuePort1,
       "pm10010mptPerfTelecomLinePostFecPast24StatHistoryInvUasPort1": pm10010mptPerfTelecomLinePostFecPast24StatHistoryInvUasPort1,
       "pm10010mptPerfTelecomLinePostFecPast24StatHistoryUasValuePort1": pm10010mptPerfTelecomLinePostFecPast24StatHistoryUasValuePort1,
       "pm10010mptPerfTelecomBerLinePreFecCurrent15StatTable": pm10010mptPerfTelecomBerLinePreFecCurrent15StatTable,
       "pm10010mptPerfTelecomBerLinePreFecCurrent15StatEntry": pm10010mptPerfTelecomBerLinePreFecCurrent15StatEntry,
       "pm10010mptPerfTelecomBerLinePreFecCurrent15StatIndex": pm10010mptPerfTelecomBerLinePreFecCurrent15StatIndex,
       "pm10010mptPerfTelecomBerLinePreFecCurrent15StatInvBerPortn": pm10010mptPerfTelecomBerLinePreFecCurrent15StatInvBerPortn,
       "pm10010mptPerfTelecomBerLinePreFecCurrent15StatBerValuePortn": pm10010mptPerfTelecomBerLinePreFecCurrent15StatBerValuePortn,
       "pm10010mptPerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn": pm10010mptPerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn,
       "pm10010mptPerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn": pm10010mptPerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn,
       "pm10010mptPerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn": pm10010mptPerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn,
       "pm10010mptPerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn": pm10010mptPerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn,
       "pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryPort1Table": pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryPort1Table,
       "pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryPort1Entry": pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryPort1Entry,
       "pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryPort1Index": pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryPort1Index,
       "pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1": pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1,
       "pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1": pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1,
       "pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1": pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1,
       "pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1": pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1,
       "pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1": pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1,
       "pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1": pm10010mptPerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1,
       "pm10010mptPerfTelecomBerLinePreFecCurrent24StatTable": pm10010mptPerfTelecomBerLinePreFecCurrent24StatTable,
       "pm10010mptPerfTelecomBerLinePreFecCurrent24StatEntry": pm10010mptPerfTelecomBerLinePreFecCurrent24StatEntry,
       "pm10010mptPerfTelecomBerLinePreFecCurrent24StatIndex": pm10010mptPerfTelecomBerLinePreFecCurrent24StatIndex,
       "pm10010mptPerfTelecomBerLinePreFecCurrent24StatInvBerPortn": pm10010mptPerfTelecomBerLinePreFecCurrent24StatInvBerPortn,
       "pm10010mptPerfTelecomBerLinePreFecCurrent24StatBerValuePortn": pm10010mptPerfTelecomBerLinePreFecCurrent24StatBerValuePortn,
       "pm10010mptPerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn": pm10010mptPerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn,
       "pm10010mptPerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn": pm10010mptPerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn,
       "pm10010mptPerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn": pm10010mptPerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn,
       "pm10010mptPerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn": pm10010mptPerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn,
       "pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryPort1Table": pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryPort1Table,
       "pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryPort1Entry": pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryPort1Entry,
       "pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryPort1Index": pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryPort1Index,
       "pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1": pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1,
       "pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1": pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1,
       "pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1": pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1,
       "pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1": pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1,
       "pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1": pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1,
       "pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1": pm10010mptPerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1}
)
