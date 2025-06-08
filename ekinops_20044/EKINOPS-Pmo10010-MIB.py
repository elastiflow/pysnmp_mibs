# SNMP MIB module (EKINOPS-Pmo10010-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ekinops_20044/EKINOPS-Pmo10010-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 12:01:48 2025
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

modulePmo10010 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76)
)
if mibBuilder.loadTexts:
    modulePmo10010.setRevisions(
        ("2016-01-12 00:00",
         "2016-05-20 00:00",
         "2016-06-02 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Pmo10010MultiRate(TextualConvention, Integer32):
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



class Pmo10010OtxMode(TextualConvention, Integer32):
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



class Pmo10010OtxGrid(TextualConvention, Integer32):
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



class Pmo10010AdjustValue(TextualConvention, Integer32):
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



class Pmo10010ClientProtocol(TextualConvention, Integer32):
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



class Pmo10010ProtocolMode(TextualConvention, Integer32):
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



class Pmo10010OtxChannel(TextualConvention, Integer32):
    status = "current"


class Pmo10010OrxChannel(TextualConvention, Integer32):
    status = "current"


class Pmo10010Odu2SapiMode(TextualConvention, Integer32):
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
        *(("off", 0),
          ("sapi", 1),
          ("dapi", 2),
          ("sapidapi", 3))
    )



class Pmo10010Otu4SapiMode(TextualConvention, Integer32):
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
        *(("off", 0),
          ("sapi", 1),
          ("dapi", 2),
          ("sapidapi", 3))
    )



# MIB Managed Objects in the order of their OIDs

_Pmo10010alarms_ObjectIdentity = ObjectIdentity
pmo10010alarms = _Pmo10010alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2)
)
_Pmo10010AlmOther_ObjectIdentity = ObjectIdentity
pmo10010AlmOther = _Pmo10010AlmOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1)
)
_Pmo10010AlmOtherNurg_ObjectIdentity = ObjectIdentity
pmo10010AlmOtherNurg = _Pmo10010AlmOtherNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 1)
)
_Pmo10010AlmsynthAlm2_ObjectIdentity = ObjectIdentity
pmo10010AlmsynthAlm2 = _Pmo10010AlmsynthAlm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 1, 2)
)
_Pmo10010AlmConfTableSave_Type = EkiOnOff
_Pmo10010AlmConfTableSave_Object = MibScalar
pmo10010AlmConfTableSave = _Pmo10010AlmConfTableSave_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 1, 2, 1),
    _Pmo10010AlmConfTableSave_Type()
)
pmo10010AlmConfTableSave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmConfTableSave.setStatus("current")
_Pmo10010AlmInvUpload_Type = EkiOnOff
_Pmo10010AlmInvUpload_Object = MibScalar
pmo10010AlmInvUpload = _Pmo10010AlmInvUpload_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 1, 2, 2),
    _Pmo10010AlmInvUpload_Type()
)
pmo10010AlmInvUpload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmInvUpload.setStatus("current")
_Pmo10010AlmConfTableLoad_Type = EkiOnOff
_Pmo10010AlmConfTableLoad_Object = MibScalar
pmo10010AlmConfTableLoad = _Pmo10010AlmConfTableLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 1, 2, 3),
    _Pmo10010AlmConfTableLoad_Type()
)
pmo10010AlmConfTableLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmConfTableLoad.setStatus("current")
_Pmo10010AlmCorrelatOff_Type = EkiOnOff
_Pmo10010AlmCorrelatOff_Object = MibScalar
pmo10010AlmCorrelatOff = _Pmo10010AlmCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 1, 2, 4),
    _Pmo10010AlmCorrelatOff_Type()
)
pmo10010AlmCorrelatOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmCorrelatOff.setStatus("current")
_Pmo10010AlmMaintenanceOn_Type = EkiOnOff
_Pmo10010AlmMaintenanceOn_Object = MibScalar
pmo10010AlmMaintenanceOn = _Pmo10010AlmMaintenanceOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 1, 2, 5),
    _Pmo10010AlmMaintenanceOn_Type()
)
pmo10010AlmMaintenanceOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmMaintenanceOn.setStatus("current")
_Pmo10010AlmOtherUrg_ObjectIdentity = ObjectIdentity
pmo10010AlmOtherUrg = _Pmo10010AlmOtherUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 2)
)
_Pmo10010AlmOtherCrit_ObjectIdentity = ObjectIdentity
pmo10010AlmOtherCrit = _Pmo10010AlmOtherCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3)
)
_Pmo10010AlmsynthAlm0_ObjectIdentity = ObjectIdentity
pmo10010AlmsynthAlm0 = _Pmo10010AlmsynthAlm0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 0)
)
_Pmo10010AlmFailFan_Type = EkiOnOff
_Pmo10010AlmFailFan_Object = MibScalar
pmo10010AlmFailFan = _Pmo10010AlmFailFan_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 0, 2),
    _Pmo10010AlmFailFan_Type()
)
pmo10010AlmFailFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmFailFan.setStatus("current")
_Pmo10010AlmModGlobFail_Type = EkiOnOff
_Pmo10010AlmModGlobFail_Object = MibScalar
pmo10010AlmModGlobFail = _Pmo10010AlmModGlobFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 0, 9),
    _Pmo10010AlmModGlobFail_Type()
)
pmo10010AlmModGlobFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmModGlobFail.setStatus("current")
_Pmo10010AlmDefFuseA_Type = EkiOnOff
_Pmo10010AlmDefFuseA_Object = MibScalar
pmo10010AlmDefFuseA = _Pmo10010AlmDefFuseA_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 0, 15),
    _Pmo10010AlmDefFuseA_Type()
)
pmo10010AlmDefFuseA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmDefFuseA.setStatus("current")
_Pmo10010AlmDefFuseB_Type = EkiOnOff
_Pmo10010AlmDefFuseB_Object = MibScalar
pmo10010AlmDefFuseB = _Pmo10010AlmDefFuseB_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 0, 16),
    _Pmo10010AlmDefFuseB_Type()
)
pmo10010AlmDefFuseB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmDefFuseB.setStatus("current")
_Pmo10010AlmclientModuleState_ObjectIdentity = ObjectIdentity
pmo10010AlmclientModuleState = _Pmo10010AlmclientModuleState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 40)
)
_Pmo10010AlmCfpInitialize_Type = EkiOnOff
_Pmo10010AlmCfpInitialize_Object = MibScalar
pmo10010AlmCfpInitialize = _Pmo10010AlmCfpInitialize_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 40, 1),
    _Pmo10010AlmCfpInitialize_Type()
)
pmo10010AlmCfpInitialize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmCfpInitialize.setStatus("current")
_Pmo10010AlmCfpLowPower_Type = EkiOnOff
_Pmo10010AlmCfpLowPower_Object = MibScalar
pmo10010AlmCfpLowPower = _Pmo10010AlmCfpLowPower_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 40, 2),
    _Pmo10010AlmCfpLowPower_Type()
)
pmo10010AlmCfpLowPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmCfpLowPower.setStatus("current")
_Pmo10010AlmCfpHighPowerUp_Type = EkiOnOff
_Pmo10010AlmCfpHighPowerUp_Object = MibScalar
pmo10010AlmCfpHighPowerUp = _Pmo10010AlmCfpHighPowerUp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 40, 3),
    _Pmo10010AlmCfpHighPowerUp_Type()
)
pmo10010AlmCfpHighPowerUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmCfpHighPowerUp.setStatus("current")
_Pmo10010AlmCfpTxOff_Type = EkiOnOff
_Pmo10010AlmCfpTxOff_Object = MibScalar
pmo10010AlmCfpTxOff = _Pmo10010AlmCfpTxOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 40, 4),
    _Pmo10010AlmCfpTxOff_Type()
)
pmo10010AlmCfpTxOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmCfpTxOff.setStatus("current")
_Pmo10010AlmCfpTxTurnOn_Type = EkiOnOff
_Pmo10010AlmCfpTxTurnOn_Object = MibScalar
pmo10010AlmCfpTxTurnOn = _Pmo10010AlmCfpTxTurnOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 40, 5),
    _Pmo10010AlmCfpTxTurnOn_Type()
)
pmo10010AlmCfpTxTurnOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmCfpTxTurnOn.setStatus("current")
_Pmo10010AlmCfpReady_Type = EkiOnOff
_Pmo10010AlmCfpReady_Object = MibScalar
pmo10010AlmCfpReady = _Pmo10010AlmCfpReady_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 40, 6),
    _Pmo10010AlmCfpReady_Type()
)
pmo10010AlmCfpReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmCfpReady.setStatus("current")
_Pmo10010AlmCfpFault_Type = EkiOnOff
_Pmo10010AlmCfpFault_Object = MibScalar
pmo10010AlmCfpFault = _Pmo10010AlmCfpFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 40, 7),
    _Pmo10010AlmCfpFault_Type()
)
pmo10010AlmCfpFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmCfpFault.setStatus("current")
_Pmo10010AlmCfpTxTurnOff_Type = EkiOnOff
_Pmo10010AlmCfpTxTurnOff_Object = MibScalar
pmo10010AlmCfpTxTurnOff = _Pmo10010AlmCfpTxTurnOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 40, 8),
    _Pmo10010AlmCfpTxTurnOff_Type()
)
pmo10010AlmCfpTxTurnOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmCfpTxTurnOff.setStatus("current")
_Pmo10010AlmCfpHighPowerDown_Type = EkiOnOff
_Pmo10010AlmCfpHighPowerDown_Object = MibScalar
pmo10010AlmCfpHighPowerDown = _Pmo10010AlmCfpHighPowerDown_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 40, 9),
    _Pmo10010AlmCfpHighPowerDown_Type()
)
pmo10010AlmCfpHighPowerDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmCfpHighPowerDown.setStatus("current")
_Pmo10010AlmclientModuleGeneralStatus_ObjectIdentity = ObjectIdentity
pmo10010AlmclientModuleGeneralStatus = _Pmo10010AlmclientModuleGeneralStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 41)
)
_Pmo10010AlmCfpOutOfAlignment_Type = EkiOnOff
_Pmo10010AlmCfpOutOfAlignment_Object = MibScalar
pmo10010AlmCfpOutOfAlignment = _Pmo10010AlmCfpOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 41, 4),
    _Pmo10010AlmCfpOutOfAlignment_Type()
)
pmo10010AlmCfpOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmCfpOutOfAlignment.setStatus("current")
_Pmo10010AlmCfpRxNetworkLol_Type = EkiOnOff
_Pmo10010AlmCfpRxNetworkLol_Object = MibScalar
pmo10010AlmCfpRxNetworkLol = _Pmo10010AlmCfpRxNetworkLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 41, 5),
    _Pmo10010AlmCfpRxNetworkLol_Type()
)
pmo10010AlmCfpRxNetworkLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmCfpRxNetworkLol.setStatus("current")
_Pmo10010AlmCfpRxLos_Type = EkiOnOff
_Pmo10010AlmCfpRxLos_Object = MibScalar
pmo10010AlmCfpRxLos = _Pmo10010AlmCfpRxLos_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 41, 6),
    _Pmo10010AlmCfpRxLos_Type()
)
pmo10010AlmCfpRxLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmCfpRxLos.setStatus("current")
_Pmo10010AlmCfpTxHostLol_Type = EkiOnOff
_Pmo10010AlmCfpTxHostLol_Object = MibScalar
pmo10010AlmCfpTxHostLol = _Pmo10010AlmCfpTxHostLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 41, 7),
    _Pmo10010AlmCfpTxHostLol_Type()
)
pmo10010AlmCfpTxHostLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmCfpTxHostLol.setStatus("current")
_Pmo10010AlmCfpTxLosf_Type = EkiOnOff
_Pmo10010AlmCfpTxLosf_Object = MibScalar
pmo10010AlmCfpTxLosf = _Pmo10010AlmCfpTxLosf_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 41, 8),
    _Pmo10010AlmCfpTxLosf_Type()
)
pmo10010AlmCfpTxLosf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmCfpTxLosf.setStatus("current")
_Pmo10010AlmCfpTxCmuLol_Type = EkiOnOff
_Pmo10010AlmCfpTxCmuLol_Object = MibScalar
pmo10010AlmCfpTxCmuLol = _Pmo10010AlmCfpTxCmuLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 41, 9),
    _Pmo10010AlmCfpTxCmuLol_Type()
)
pmo10010AlmCfpTxCmuLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmCfpTxCmuLol.setStatus("current")
_Pmo10010AlmCfpTxJitterPllLol_Type = EkiOnOff
_Pmo10010AlmCfpTxJitterPllLol_Object = MibScalar
pmo10010AlmCfpTxJitterPllLol = _Pmo10010AlmCfpTxJitterPllLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 41, 10),
    _Pmo10010AlmCfpTxJitterPllLol_Type()
)
pmo10010AlmCfpTxJitterPllLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmCfpTxJitterPllLol.setStatus("current")
_Pmo10010AlmCfpLossOfRefclk_Type = EkiOnOff
_Pmo10010AlmCfpLossOfRefclk_Object = MibScalar
pmo10010AlmCfpLossOfRefclk = _Pmo10010AlmCfpLossOfRefclk_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 41, 11),
    _Pmo10010AlmCfpLossOfRefclk_Type()
)
pmo10010AlmCfpLossOfRefclk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmCfpLossOfRefclk.setStatus("current")
_Pmo10010AlmCfpHwInterlock_Type = EkiOnOff
_Pmo10010AlmCfpHwInterlock_Object = MibScalar
pmo10010AlmCfpHwInterlock = _Pmo10010AlmCfpHwInterlock_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 41, 14),
    _Pmo10010AlmCfpHwInterlock_Type()
)
pmo10010AlmCfpHwInterlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmCfpHwInterlock.setStatus("current")
_Pmo10010AlmclientGlobalAlarmSummary_ObjectIdentity = ObjectIdentity
pmo10010AlmclientGlobalAlarmSummary = _Pmo10010AlmclientGlobalAlarmSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 42)
)
_Pmo10010AlmCfpSoftGlobAlarmTest_Type = EkiOnOff
_Pmo10010AlmCfpSoftGlobAlarmTest_Object = MibScalar
pmo10010AlmCfpSoftGlobAlarmTest = _Pmo10010AlmCfpSoftGlobAlarmTest_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 42, 1),
    _Pmo10010AlmCfpSoftGlobAlarmTest_Type()
)
pmo10010AlmCfpSoftGlobAlarmTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmCfpSoftGlobAlarmTest.setStatus("current")
_Pmo10010AlmCfpNetworkLaneAlarmWarning2_Type = EkiOnOff
_Pmo10010AlmCfpNetworkLaneAlarmWarning2_Object = MibScalar
pmo10010AlmCfpNetworkLaneAlarmWarning2 = _Pmo10010AlmCfpNetworkLaneAlarmWarning2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 42, 7),
    _Pmo10010AlmCfpNetworkLaneAlarmWarning2_Type()
)
pmo10010AlmCfpNetworkLaneAlarmWarning2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmCfpNetworkLaneAlarmWarning2.setStatus("current")
_Pmo10010AlmCfpModuleState_Type = EkiOnOff
_Pmo10010AlmCfpModuleState_Object = MibScalar
pmo10010AlmCfpModuleState = _Pmo10010AlmCfpModuleState_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 42, 8),
    _Pmo10010AlmCfpModuleState_Type()
)
pmo10010AlmCfpModuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmCfpModuleState.setStatus("current")
_Pmo10010AlmCfpModuleGeneralStatus_Type = EkiOnOff
_Pmo10010AlmCfpModuleGeneralStatus_Object = MibScalar
pmo10010AlmCfpModuleGeneralStatus = _Pmo10010AlmCfpModuleGeneralStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 42, 9),
    _Pmo10010AlmCfpModuleGeneralStatus_Type()
)
pmo10010AlmCfpModuleGeneralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmCfpModuleGeneralStatus.setStatus("current")
_Pmo10010AlmCfpModuleFault_Type = EkiOnOff
_Pmo10010AlmCfpModuleFault_Object = MibScalar
pmo10010AlmCfpModuleFault = _Pmo10010AlmCfpModuleFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 42, 10),
    _Pmo10010AlmCfpModuleFault_Type()
)
pmo10010AlmCfpModuleFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmCfpModuleFault.setStatus("current")
_Pmo10010AlmCfpModuleAlarmWarning1_Type = EkiOnOff
_Pmo10010AlmCfpModuleAlarmWarning1_Object = MibScalar
pmo10010AlmCfpModuleAlarmWarning1 = _Pmo10010AlmCfpModuleAlarmWarning1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 42, 11),
    _Pmo10010AlmCfpModuleAlarmWarning1_Type()
)
pmo10010AlmCfpModuleAlarmWarning1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmCfpModuleAlarmWarning1.setStatus("current")
_Pmo10010AlmCfpModuleAlarmWarning2_Type = EkiOnOff
_Pmo10010AlmCfpModuleAlarmWarning2_Object = MibScalar
pmo10010AlmCfpModuleAlarmWarning2 = _Pmo10010AlmCfpModuleAlarmWarning2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 42, 12),
    _Pmo10010AlmCfpModuleAlarmWarning2_Type()
)
pmo10010AlmCfpModuleAlarmWarning2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmCfpModuleAlarmWarning2.setStatus("current")
_Pmo10010AlmCfpNetworkLaneAlarmWarning1_Type = EkiOnOff
_Pmo10010AlmCfpNetworkLaneAlarmWarning1_Object = MibScalar
pmo10010AlmCfpNetworkLaneAlarmWarning1 = _Pmo10010AlmCfpNetworkLaneAlarmWarning1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 42, 13),
    _Pmo10010AlmCfpNetworkLaneAlarmWarning1_Type()
)
pmo10010AlmCfpNetworkLaneAlarmWarning1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmCfpNetworkLaneAlarmWarning1.setStatus("current")
_Pmo10010AlmCfpNetworkLaneFaultStatus_Type = EkiOnOff
_Pmo10010AlmCfpNetworkLaneFaultStatus_Object = MibScalar
pmo10010AlmCfpNetworkLaneFaultStatus = _Pmo10010AlmCfpNetworkLaneFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 42, 14),
    _Pmo10010AlmCfpNetworkLaneFaultStatus_Type()
)
pmo10010AlmCfpNetworkLaneFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmCfpNetworkLaneFaultStatus.setStatus("current")
_Pmo10010AlmCfpHostLaneFaultStatus_Type = EkiOnOff
_Pmo10010AlmCfpHostLaneFaultStatus_Object = MibScalar
pmo10010AlmCfpHostLaneFaultStatus = _Pmo10010AlmCfpHostLaneFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 42, 15),
    _Pmo10010AlmCfpHostLaneFaultStatus_Type()
)
pmo10010AlmCfpHostLaneFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmCfpHostLaneFaultStatus.setStatus("current")
_Pmo10010AlmCfpGlobAlarmAssertion_Type = EkiOnOff
_Pmo10010AlmCfpGlobAlarmAssertion_Object = MibScalar
pmo10010AlmCfpGlobAlarmAssertion = _Pmo10010AlmCfpGlobAlarmAssertion_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 42, 16),
    _Pmo10010AlmCfpGlobAlarmAssertion_Type()
)
pmo10010AlmCfpGlobAlarmAssertion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmCfpGlobAlarmAssertion.setStatus("current")
_Pmo10010AlmmsaModuleState_ObjectIdentity = ObjectIdentity
pmo10010AlmmsaModuleState = _Pmo10010AlmmsaModuleState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 46)
)
_Pmo10010AlmMsaInitialize_Type = EkiOnOff
_Pmo10010AlmMsaInitialize_Object = MibScalar
pmo10010AlmMsaInitialize = _Pmo10010AlmMsaInitialize_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 46, 1),
    _Pmo10010AlmMsaInitialize_Type()
)
pmo10010AlmMsaInitialize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmMsaInitialize.setStatus("current")
_Pmo10010AlmMsaLowPower_Type = EkiOnOff
_Pmo10010AlmMsaLowPower_Object = MibScalar
pmo10010AlmMsaLowPower = _Pmo10010AlmMsaLowPower_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 46, 2),
    _Pmo10010AlmMsaLowPower_Type()
)
pmo10010AlmMsaLowPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmMsaLowPower.setStatus("current")
_Pmo10010AlmMsaHighPowerUp_Type = EkiOnOff
_Pmo10010AlmMsaHighPowerUp_Object = MibScalar
pmo10010AlmMsaHighPowerUp = _Pmo10010AlmMsaHighPowerUp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 46, 3),
    _Pmo10010AlmMsaHighPowerUp_Type()
)
pmo10010AlmMsaHighPowerUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmMsaHighPowerUp.setStatus("current")
_Pmo10010AlmMsaTxOff_Type = EkiOnOff
_Pmo10010AlmMsaTxOff_Object = MibScalar
pmo10010AlmMsaTxOff = _Pmo10010AlmMsaTxOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 46, 4),
    _Pmo10010AlmMsaTxOff_Type()
)
pmo10010AlmMsaTxOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmMsaTxOff.setStatus("current")
_Pmo10010AlmMsaTxTurnOn_Type = EkiOnOff
_Pmo10010AlmMsaTxTurnOn_Object = MibScalar
pmo10010AlmMsaTxTurnOn = _Pmo10010AlmMsaTxTurnOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 46, 5),
    _Pmo10010AlmMsaTxTurnOn_Type()
)
pmo10010AlmMsaTxTurnOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmMsaTxTurnOn.setStatus("current")
_Pmo10010AlmMsaReady_Type = EkiOnOff
_Pmo10010AlmMsaReady_Object = MibScalar
pmo10010AlmMsaReady = _Pmo10010AlmMsaReady_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 46, 6),
    _Pmo10010AlmMsaReady_Type()
)
pmo10010AlmMsaReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmMsaReady.setStatus("current")
_Pmo10010AlmMsaFault_Type = EkiOnOff
_Pmo10010AlmMsaFault_Object = MibScalar
pmo10010AlmMsaFault = _Pmo10010AlmMsaFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 46, 7),
    _Pmo10010AlmMsaFault_Type()
)
pmo10010AlmMsaFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmMsaFault.setStatus("current")
_Pmo10010AlmMsaTxTurnOff_Type = EkiOnOff
_Pmo10010AlmMsaTxTurnOff_Object = MibScalar
pmo10010AlmMsaTxTurnOff = _Pmo10010AlmMsaTxTurnOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 46, 8),
    _Pmo10010AlmMsaTxTurnOff_Type()
)
pmo10010AlmMsaTxTurnOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmMsaTxTurnOff.setStatus("current")
_Pmo10010AlmMsaHighPowerDown_Type = EkiOnOff
_Pmo10010AlmMsaHighPowerDown_Object = MibScalar
pmo10010AlmMsaHighPowerDown = _Pmo10010AlmMsaHighPowerDown_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 46, 9),
    _Pmo10010AlmMsaHighPowerDown_Type()
)
pmo10010AlmMsaHighPowerDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmMsaHighPowerDown.setStatus("current")
_Pmo10010AlmmsaModuleGeneralStatus_ObjectIdentity = ObjectIdentity
pmo10010AlmmsaModuleGeneralStatus = _Pmo10010AlmmsaModuleGeneralStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 47)
)
_Pmo10010AlmMsaOutOfAlignment_Type = EkiOnOff
_Pmo10010AlmMsaOutOfAlignment_Object = MibScalar
pmo10010AlmMsaOutOfAlignment = _Pmo10010AlmMsaOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 47, 4),
    _Pmo10010AlmMsaOutOfAlignment_Type()
)
pmo10010AlmMsaOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmMsaOutOfAlignment.setStatus("current")
_Pmo10010AlmMsaRxNetworkLol_Type = EkiOnOff
_Pmo10010AlmMsaRxNetworkLol_Object = MibScalar
pmo10010AlmMsaRxNetworkLol = _Pmo10010AlmMsaRxNetworkLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 47, 5),
    _Pmo10010AlmMsaRxNetworkLol_Type()
)
pmo10010AlmMsaRxNetworkLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmMsaRxNetworkLol.setStatus("current")
_Pmo10010AlmMsaRxLos_Type = EkiOnOff
_Pmo10010AlmMsaRxLos_Object = MibScalar
pmo10010AlmMsaRxLos = _Pmo10010AlmMsaRxLos_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 47, 6),
    _Pmo10010AlmMsaRxLos_Type()
)
pmo10010AlmMsaRxLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmMsaRxLos.setStatus("current")
_Pmo10010AlmMsaTxHostLol_Type = EkiOnOff
_Pmo10010AlmMsaTxHostLol_Object = MibScalar
pmo10010AlmMsaTxHostLol = _Pmo10010AlmMsaTxHostLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 47, 7),
    _Pmo10010AlmMsaTxHostLol_Type()
)
pmo10010AlmMsaTxHostLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmMsaTxHostLol.setStatus("current")
_Pmo10010AlmMsaTxLosf_Type = EkiOnOff
_Pmo10010AlmMsaTxLosf_Object = MibScalar
pmo10010AlmMsaTxLosf = _Pmo10010AlmMsaTxLosf_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 47, 8),
    _Pmo10010AlmMsaTxLosf_Type()
)
pmo10010AlmMsaTxLosf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmMsaTxLosf.setStatus("current")
_Pmo10010AlmMsaTxCmuLol_Type = EkiOnOff
_Pmo10010AlmMsaTxCmuLol_Object = MibScalar
pmo10010AlmMsaTxCmuLol = _Pmo10010AlmMsaTxCmuLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 47, 9),
    _Pmo10010AlmMsaTxCmuLol_Type()
)
pmo10010AlmMsaTxCmuLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmMsaTxCmuLol.setStatus("current")
_Pmo10010AlmMsaTxJitterPllLol_Type = EkiOnOff
_Pmo10010AlmMsaTxJitterPllLol_Object = MibScalar
pmo10010AlmMsaTxJitterPllLol = _Pmo10010AlmMsaTxJitterPllLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 47, 10),
    _Pmo10010AlmMsaTxJitterPllLol_Type()
)
pmo10010AlmMsaTxJitterPllLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmMsaTxJitterPllLol.setStatus("current")
_Pmo10010AlmMsaLossOfRefclk_Type = EkiOnOff
_Pmo10010AlmMsaLossOfRefclk_Object = MibScalar
pmo10010AlmMsaLossOfRefclk = _Pmo10010AlmMsaLossOfRefclk_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 47, 11),
    _Pmo10010AlmMsaLossOfRefclk_Type()
)
pmo10010AlmMsaLossOfRefclk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmMsaLossOfRefclk.setStatus("current")
_Pmo10010AlmMsaHwInterlock_Type = EkiOnOff
_Pmo10010AlmMsaHwInterlock_Object = MibScalar
pmo10010AlmMsaHwInterlock = _Pmo10010AlmMsaHwInterlock_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 47, 14),
    _Pmo10010AlmMsaHwInterlock_Type()
)
pmo10010AlmMsaHwInterlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmMsaHwInterlock.setStatus("current")
_Pmo10010AlmmsaGlobalAlarmSummary_ObjectIdentity = ObjectIdentity
pmo10010AlmmsaGlobalAlarmSummary = _Pmo10010AlmmsaGlobalAlarmSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 48)
)
_Pmo10010AlmMsaSoftGlobAlarmTest_Type = EkiOnOff
_Pmo10010AlmMsaSoftGlobAlarmTest_Object = MibScalar
pmo10010AlmMsaSoftGlobAlarmTest = _Pmo10010AlmMsaSoftGlobAlarmTest_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 48, 1),
    _Pmo10010AlmMsaSoftGlobAlarmTest_Type()
)
pmo10010AlmMsaSoftGlobAlarmTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmMsaSoftGlobAlarmTest.setStatus("current")
_Pmo10010AlmMsaNetworkHostAlarmStatus_Type = EkiOnOff
_Pmo10010AlmMsaNetworkHostAlarmStatus_Object = MibScalar
pmo10010AlmMsaNetworkHostAlarmStatus = _Pmo10010AlmMsaNetworkHostAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 48, 6),
    _Pmo10010AlmMsaNetworkHostAlarmStatus_Type()
)
pmo10010AlmMsaNetworkHostAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmMsaNetworkHostAlarmStatus.setStatus("current")
_Pmo10010AlmMsaNetworkLaneAlarmWarning2_Type = EkiOnOff
_Pmo10010AlmMsaNetworkLaneAlarmWarning2_Object = MibScalar
pmo10010AlmMsaNetworkLaneAlarmWarning2 = _Pmo10010AlmMsaNetworkLaneAlarmWarning2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 48, 7),
    _Pmo10010AlmMsaNetworkLaneAlarmWarning2_Type()
)
pmo10010AlmMsaNetworkLaneAlarmWarning2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmMsaNetworkLaneAlarmWarning2.setStatus("current")
_Pmo10010AlmMsaModuleState_Type = EkiOnOff
_Pmo10010AlmMsaModuleState_Object = MibScalar
pmo10010AlmMsaModuleState = _Pmo10010AlmMsaModuleState_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 48, 8),
    _Pmo10010AlmMsaModuleState_Type()
)
pmo10010AlmMsaModuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmMsaModuleState.setStatus("current")
_Pmo10010AlmMsaModuleGeneralStatus_Type = EkiOnOff
_Pmo10010AlmMsaModuleGeneralStatus_Object = MibScalar
pmo10010AlmMsaModuleGeneralStatus = _Pmo10010AlmMsaModuleGeneralStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 48, 9),
    _Pmo10010AlmMsaModuleGeneralStatus_Type()
)
pmo10010AlmMsaModuleGeneralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmMsaModuleGeneralStatus.setStatus("current")
_Pmo10010AlmModuleFault_Type = EkiOnOff
_Pmo10010AlmModuleFault_Object = MibScalar
pmo10010AlmModuleFault = _Pmo10010AlmModuleFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 48, 10),
    _Pmo10010AlmModuleFault_Type()
)
pmo10010AlmModuleFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmModuleFault.setStatus("current")
_Pmo10010AlmMsaModuleAlarmWarning1_Type = EkiOnOff
_Pmo10010AlmMsaModuleAlarmWarning1_Object = MibScalar
pmo10010AlmMsaModuleAlarmWarning1 = _Pmo10010AlmMsaModuleAlarmWarning1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 48, 11),
    _Pmo10010AlmMsaModuleAlarmWarning1_Type()
)
pmo10010AlmMsaModuleAlarmWarning1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmMsaModuleAlarmWarning1.setStatus("current")
_Pmo10010AlmMsaModuleAlarmWarning2_Type = EkiOnOff
_Pmo10010AlmMsaModuleAlarmWarning2_Object = MibScalar
pmo10010AlmMsaModuleAlarmWarning2 = _Pmo10010AlmMsaModuleAlarmWarning2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 48, 12),
    _Pmo10010AlmMsaModuleAlarmWarning2_Type()
)
pmo10010AlmMsaModuleAlarmWarning2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmMsaModuleAlarmWarning2.setStatus("current")
_Pmo10010AlmMsaNetworkLaneAlarmWarning1_Type = EkiOnOff
_Pmo10010AlmMsaNetworkLaneAlarmWarning1_Object = MibScalar
pmo10010AlmMsaNetworkLaneAlarmWarning1 = _Pmo10010AlmMsaNetworkLaneAlarmWarning1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 48, 13),
    _Pmo10010AlmMsaNetworkLaneAlarmWarning1_Type()
)
pmo10010AlmMsaNetworkLaneAlarmWarning1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmMsaNetworkLaneAlarmWarning1.setStatus("current")
_Pmo10010AlmMsaNetworkLaneFaultStatus_Type = EkiOnOff
_Pmo10010AlmMsaNetworkLaneFaultStatus_Object = MibScalar
pmo10010AlmMsaNetworkLaneFaultStatus = _Pmo10010AlmMsaNetworkLaneFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 48, 14),
    _Pmo10010AlmMsaNetworkLaneFaultStatus_Type()
)
pmo10010AlmMsaNetworkLaneFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmMsaNetworkLaneFaultStatus.setStatus("current")
_Pmo10010AlmMsaHostLaneFaultStatus_Type = EkiOnOff
_Pmo10010AlmMsaHostLaneFaultStatus_Object = MibScalar
pmo10010AlmMsaHostLaneFaultStatus = _Pmo10010AlmMsaHostLaneFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 48, 15),
    _Pmo10010AlmMsaHostLaneFaultStatus_Type()
)
pmo10010AlmMsaHostLaneFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmMsaHostLaneFaultStatus.setStatus("current")
_Pmo10010AlmMsaGlobAlarmAssertion_Type = EkiOnOff
_Pmo10010AlmMsaGlobAlarmAssertion_Object = MibScalar
pmo10010AlmMsaGlobAlarmAssertion = _Pmo10010AlmMsaGlobAlarmAssertion_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 48, 16),
    _Pmo10010AlmMsaGlobAlarmAssertion_Type()
)
pmo10010AlmMsaGlobAlarmAssertion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmMsaGlobAlarmAssertion.setStatus("current")
_Pmo10010AlmmsaNetworkTxAlignment_ObjectIdentity = ObjectIdentity
pmo10010AlmmsaNetworkTxAlignment = _Pmo10010AlmmsaNetworkTxAlignment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 49)
)
_Pmo10010AlmNetTxTimingFault_Type = EkiOnOff
_Pmo10010AlmNetTxTimingFault_Object = MibScalar
pmo10010AlmNetTxTimingFault = _Pmo10010AlmNetTxTimingFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 49, 12),
    _Pmo10010AlmNetTxTimingFault_Type()
)
pmo10010AlmNetTxTimingFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmNetTxTimingFault.setStatus("current")
_Pmo10010AlmNetTxReferenceClockFault_Type = EkiOnOff
_Pmo10010AlmNetTxReferenceClockFault_Object = MibScalar
pmo10010AlmNetTxReferenceClockFault = _Pmo10010AlmNetTxReferenceClockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 49, 13),
    _Pmo10010AlmNetTxReferenceClockFault_Type()
)
pmo10010AlmNetTxReferenceClockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmNetTxReferenceClockFault.setStatus("current")
_Pmo10010AlmNetTxCmuLockFault_Type = EkiOnOff
_Pmo10010AlmNetTxCmuLockFault_Object = MibScalar
pmo10010AlmNetTxCmuLockFault = _Pmo10010AlmNetTxCmuLockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 49, 14),
    _Pmo10010AlmNetTxCmuLockFault_Type()
)
pmo10010AlmNetTxCmuLockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmNetTxCmuLockFault.setStatus("current")
_Pmo10010AlmNetTxOutOfAlignment_Type = EkiOnOff
_Pmo10010AlmNetTxOutOfAlignment_Object = MibScalar
pmo10010AlmNetTxOutOfAlignment = _Pmo10010AlmNetTxOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 49, 15),
    _Pmo10010AlmNetTxOutOfAlignment_Type()
)
pmo10010AlmNetTxOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmNetTxOutOfAlignment.setStatus("current")
_Pmo10010AlmNetTxLossOfAlignment_Type = EkiOnOff
_Pmo10010AlmNetTxLossOfAlignment_Object = MibScalar
pmo10010AlmNetTxLossOfAlignment = _Pmo10010AlmNetTxLossOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 49, 16),
    _Pmo10010AlmNetTxLossOfAlignment_Type()
)
pmo10010AlmNetTxLossOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmNetTxLossOfAlignment.setStatus("current")
_Pmo10010AlmmsaNetworkRxAlignment_ObjectIdentity = ObjectIdentity
pmo10010AlmmsaNetworkRxAlignment = _Pmo10010AlmmsaNetworkRxAlignment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 50)
)
_Pmo10010AlmNetRxTimingFault_Type = EkiOnOff
_Pmo10010AlmNetRxTimingFault_Object = MibScalar
pmo10010AlmNetRxTimingFault = _Pmo10010AlmNetRxTimingFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 50, 12),
    _Pmo10010AlmNetRxTimingFault_Type()
)
pmo10010AlmNetRxTimingFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmNetRxTimingFault.setStatus("current")
_Pmo10010AlmNetRxOutOfAlignment_Type = EkiOnOff
_Pmo10010AlmNetRxOutOfAlignment_Object = MibScalar
pmo10010AlmNetRxOutOfAlignment = _Pmo10010AlmNetRxOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 50, 13),
    _Pmo10010AlmNetRxOutOfAlignment_Type()
)
pmo10010AlmNetRxOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmNetRxOutOfAlignment.setStatus("current")
_Pmo10010AlmNetRxLossOfAlignment_Type = EkiOnOff
_Pmo10010AlmNetRxLossOfAlignment_Object = MibScalar
pmo10010AlmNetRxLossOfAlignment = _Pmo10010AlmNetRxLossOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 50, 14),
    _Pmo10010AlmNetRxLossOfAlignment_Type()
)
pmo10010AlmNetRxLossOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmNetRxLossOfAlignment.setStatus("current")
_Pmo10010AlmNetRxModemLockFault_Type = EkiOnOff
_Pmo10010AlmNetRxModemLockFault_Object = MibScalar
pmo10010AlmNetRxModemLockFault = _Pmo10010AlmNetRxModemLockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 50, 15),
    _Pmo10010AlmNetRxModemLockFault_Type()
)
pmo10010AlmNetRxModemLockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmNetRxModemLockFault.setStatus("current")
_Pmo10010AlmNetRxModemSyncDetectFault_Type = EkiOnOff
_Pmo10010AlmNetRxModemSyncDetectFault_Object = MibScalar
pmo10010AlmNetRxModemSyncDetectFault = _Pmo10010AlmNetRxModemSyncDetectFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 50, 16),
    _Pmo10010AlmNetRxModemSyncDetectFault_Type()
)
pmo10010AlmNetRxModemSyncDetectFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmNetRxModemSyncDetectFault.setStatus("current")
_Pmo10010AlmmsaNetworkHostNetworkAlarmSummary_ObjectIdentity = ObjectIdentity
pmo10010AlmmsaNetworkHostNetworkAlarmSummary = _Pmo10010AlmmsaNetworkHostNetworkAlarmSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 51)
)
_Pmo10010AlmNetworkTxAlignment_Type = EkiOnOff
_Pmo10010AlmNetworkTxAlignment_Object = MibScalar
pmo10010AlmNetworkTxAlignment = _Pmo10010AlmNetworkTxAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 51, 11),
    _Pmo10010AlmNetworkTxAlignment_Type()
)
pmo10010AlmNetworkTxAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmNetworkTxAlignment.setStatus("current")
_Pmo10010AlmNetworkRxAlignment_Type = EkiOnOff
_Pmo10010AlmNetworkRxAlignment_Object = MibScalar
pmo10010AlmNetworkRxAlignment = _Pmo10010AlmNetworkRxAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 51, 12),
    _Pmo10010AlmNetworkRxAlignment_Type()
)
pmo10010AlmNetworkRxAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmNetworkRxAlignment.setStatus("current")
_Pmo10010AlmNetworkRxOtn_Type = EkiOnOff
_Pmo10010AlmNetworkRxOtn_Object = MibScalar
pmo10010AlmNetworkRxOtn = _Pmo10010AlmNetworkRxOtn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 51, 13),
    _Pmo10010AlmNetworkRxOtn_Type()
)
pmo10010AlmNetworkRxOtn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmNetworkRxOtn.setStatus("current")
_Pmo10010AlmHostRxAlignment_Type = EkiOnOff
_Pmo10010AlmHostRxAlignment_Object = MibScalar
pmo10010AlmHostRxAlignment = _Pmo10010AlmHostRxAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 51, 14),
    _Pmo10010AlmHostRxAlignment_Type()
)
pmo10010AlmHostRxAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmHostRxAlignment.setStatus("current")
_Pmo10010AlmHostTxAlignment_Type = EkiOnOff
_Pmo10010AlmHostTxAlignment_Object = MibScalar
pmo10010AlmHostTxAlignment = _Pmo10010AlmHostTxAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 51, 15),
    _Pmo10010AlmHostTxAlignment_Type()
)
pmo10010AlmHostTxAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmHostTxAlignment.setStatus("current")
_Pmo10010AlmHostTxOtnStatus_Type = EkiOnOff
_Pmo10010AlmHostTxOtnStatus_Object = MibScalar
pmo10010AlmHostTxOtnStatus = _Pmo10010AlmHostTxOtnStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 51, 16),
    _Pmo10010AlmHostTxOtnStatus_Type()
)
pmo10010AlmHostTxOtnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmHostTxOtnStatus.setStatus("current")
_Pmo10010AlmmsaHostTxAlignment_ObjectIdentity = ObjectIdentity
pmo10010AlmmsaHostTxAlignment = _Pmo10010AlmmsaHostTxAlignment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 52)
)
_Pmo10010AlmHostTxDeskewLockFault_Type = EkiOnOff
_Pmo10010AlmHostTxDeskewLockFault_Object = MibScalar
pmo10010AlmHostTxDeskewLockFault = _Pmo10010AlmHostTxDeskewLockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 52, 13),
    _Pmo10010AlmHostTxDeskewLockFault_Type()
)
pmo10010AlmHostTxDeskewLockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmHostTxDeskewLockFault.setStatus("current")
_Pmo10010AlmHostTxOutOfAlignment_Type = EkiOnOff
_Pmo10010AlmHostTxOutOfAlignment_Object = MibScalar
pmo10010AlmHostTxOutOfAlignment = _Pmo10010AlmHostTxOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 52, 14),
    _Pmo10010AlmHostTxOutOfAlignment_Type()
)
pmo10010AlmHostTxOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmHostTxOutOfAlignment.setStatus("current")
_Pmo10010AlmHostTxLossOfAlignment_Type = EkiOnOff
_Pmo10010AlmHostTxLossOfAlignment_Object = MibScalar
pmo10010AlmHostTxLossOfAlignment = _Pmo10010AlmHostTxLossOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 52, 15),
    _Pmo10010AlmHostTxLossOfAlignment_Type()
)
pmo10010AlmHostTxLossOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmHostTxLossOfAlignment.setStatus("current")
_Pmo10010AlmHostTxCdrLockFault_Type = EkiOnOff
_Pmo10010AlmHostTxCdrLockFault_Object = MibScalar
pmo10010AlmHostTxCdrLockFault = _Pmo10010AlmHostTxCdrLockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 52, 16),
    _Pmo10010AlmHostTxCdrLockFault_Type()
)
pmo10010AlmHostTxCdrLockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmHostTxCdrLockFault.setStatus("current")
_Pmo10010AlmmsaHostRxAlignment_ObjectIdentity = ObjectIdentity
pmo10010AlmmsaHostRxAlignment = _Pmo10010AlmmsaHostRxAlignment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 53)
)
_Pmo10010AlmHostRxCmuLockFault_Type = EkiOnOff
_Pmo10010AlmHostRxCmuLockFault_Object = MibScalar
pmo10010AlmHostRxCmuLockFault = _Pmo10010AlmHostRxCmuLockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 53, 14),
    _Pmo10010AlmHostRxCmuLockFault_Type()
)
pmo10010AlmHostRxCmuLockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmHostRxCmuLockFault.setStatus("current")
_Pmo10010AlmHostRxOutOfAlignment_Type = EkiOnOff
_Pmo10010AlmHostRxOutOfAlignment_Object = MibScalar
pmo10010AlmHostRxOutOfAlignment = _Pmo10010AlmHostRxOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 53, 15),
    _Pmo10010AlmHostRxOutOfAlignment_Type()
)
pmo10010AlmHostRxOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmHostRxOutOfAlignment.setStatus("current")
_Pmo10010AlmHostRxLossOfAlignment_Type = EkiOnOff
_Pmo10010AlmHostRxLossOfAlignment_Object = MibScalar
pmo10010AlmHostRxLossOfAlignment = _Pmo10010AlmHostRxLossOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 1, 3, 53, 16),
    _Pmo10010AlmHostRxLossOfAlignment_Type()
)
pmo10010AlmHostRxLossOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmHostRxLossOfAlignment.setStatus("current")
_Pmo10010AlmClient_ObjectIdentity = ObjectIdentity
pmo10010AlmClient = _Pmo10010AlmClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2)
)
_Pmo10010AlmClientNurg_ObjectIdentity = ObjectIdentity
pmo10010AlmClientNurg = _Pmo10010AlmClientNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 1)
)
_Pmo10010AlmclientNetworkLaneAlarmWarningTable_Object = MibTable
pmo10010AlmclientNetworkLaneAlarmWarningTable = _Pmo10010AlmclientNetworkLaneAlarmWarningTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 1, 56)
)
if mibBuilder.loadTexts:
    pmo10010AlmclientNetworkLaneAlarmWarningTable.setStatus("current")
_Pmo10010AlmclientNetworkLaneAlarmWarningEntry_Object = MibTableRow
pmo10010AlmclientNetworkLaneAlarmWarningEntry = _Pmo10010AlmclientNetworkLaneAlarmWarningEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 1, 56, 1)
)
pmo10010AlmclientNetworkLaneAlarmWarningEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010AlmclientNetworkLaneAlarmWarningIndex"),
)
if mibBuilder.loadTexts:
    pmo10010AlmclientNetworkLaneAlarmWarningEntry.setStatus("current")


class _Pmo10010AlmclientNetworkLaneAlarmWarningIndex_Type(Integer32):
    """Custom type pmo10010AlmclientNetworkLaneAlarmWarningIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010AlmclientNetworkLaneAlarmWarningIndex_Type.__name__ = "Integer32"
_Pmo10010AlmclientNetworkLaneAlarmWarningIndex_Object = MibTableColumn
pmo10010AlmclientNetworkLaneAlarmWarningIndex = _Pmo10010AlmclientNetworkLaneAlarmWarningIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 1, 56, 1, 1),
    _Pmo10010AlmclientNetworkLaneAlarmWarningIndex_Type()
)
pmo10010AlmclientNetworkLaneAlarmWarningIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmclientNetworkLaneAlarmWarningIndex.setStatus("current")
_Pmo10010AlmClientRxPowerLowAlarmPortn_Type = EkiOnOff
_Pmo10010AlmClientRxPowerLowAlarmPortn_Object = MibTableColumn
pmo10010AlmClientRxPowerLowAlarmPortn = _Pmo10010AlmClientRxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 1, 56, 1, 2),
    _Pmo10010AlmClientRxPowerLowAlarmPortn_Type()
)
pmo10010AlmClientRxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmClientRxPowerLowAlarmPortn.setStatus("current")
_Pmo10010AlmClientRxPowerLowWarningPortn_Type = EkiOnOff
_Pmo10010AlmClientRxPowerLowWarningPortn_Object = MibTableColumn
pmo10010AlmClientRxPowerLowWarningPortn = _Pmo10010AlmClientRxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 1, 56, 1, 3),
    _Pmo10010AlmClientRxPowerLowWarningPortn_Type()
)
pmo10010AlmClientRxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmClientRxPowerLowWarningPortn.setStatus("current")
_Pmo10010AlmClientRxPowerHighWarningPortn_Type = EkiOnOff
_Pmo10010AlmClientRxPowerHighWarningPortn_Object = MibTableColumn
pmo10010AlmClientRxPowerHighWarningPortn = _Pmo10010AlmClientRxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 1, 56, 1, 4),
    _Pmo10010AlmClientRxPowerHighWarningPortn_Type()
)
pmo10010AlmClientRxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmClientRxPowerHighWarningPortn.setStatus("current")
_Pmo10010AlmClientRxPowerHighAlarmPortn_Type = EkiOnOff
_Pmo10010AlmClientRxPowerHighAlarmPortn_Object = MibTableColumn
pmo10010AlmClientRxPowerHighAlarmPortn = _Pmo10010AlmClientRxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 1, 56, 1, 5),
    _Pmo10010AlmClientRxPowerHighAlarmPortn_Type()
)
pmo10010AlmClientRxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmClientRxPowerHighAlarmPortn.setStatus("current")
_Pmo10010AlmLaserTempLowAlarmPortn_Type = EkiOnOff
_Pmo10010AlmLaserTempLowAlarmPortn_Object = MibTableColumn
pmo10010AlmLaserTempLowAlarmPortn = _Pmo10010AlmLaserTempLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 1, 56, 1, 6),
    _Pmo10010AlmLaserTempLowAlarmPortn_Type()
)
pmo10010AlmLaserTempLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLaserTempLowAlarmPortn.setStatus("current")
_Pmo10010AlmClientLaserTempLowWarningPortn_Type = EkiOnOff
_Pmo10010AlmClientLaserTempLowWarningPortn_Object = MibTableColumn
pmo10010AlmClientLaserTempLowWarningPortn = _Pmo10010AlmClientLaserTempLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 1, 56, 1, 7),
    _Pmo10010AlmClientLaserTempLowWarningPortn_Type()
)
pmo10010AlmClientLaserTempLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmClientLaserTempLowWarningPortn.setStatus("current")
_Pmo10010AlmClientLaserTempHighWarningPortn_Type = EkiOnOff
_Pmo10010AlmClientLaserTempHighWarningPortn_Object = MibTableColumn
pmo10010AlmClientLaserTempHighWarningPortn = _Pmo10010AlmClientLaserTempHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 1, 56, 1, 8),
    _Pmo10010AlmClientLaserTempHighWarningPortn_Type()
)
pmo10010AlmClientLaserTempHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmClientLaserTempHighWarningPortn.setStatus("current")
_Pmo10010AlmClientLaserTempHighAlarmPortn_Type = EkiOnOff
_Pmo10010AlmClientLaserTempHighAlarmPortn_Object = MibTableColumn
pmo10010AlmClientLaserTempHighAlarmPortn = _Pmo10010AlmClientLaserTempHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 1, 56, 1, 9),
    _Pmo10010AlmClientLaserTempHighAlarmPortn_Type()
)
pmo10010AlmClientLaserTempHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmClientLaserTempHighAlarmPortn.setStatus("current")
_Pmo10010AlmClientTxPowerLowAlarmPortn_Type = EkiOnOff
_Pmo10010AlmClientTxPowerLowAlarmPortn_Object = MibTableColumn
pmo10010AlmClientTxPowerLowAlarmPortn = _Pmo10010AlmClientTxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 1, 56, 1, 10),
    _Pmo10010AlmClientTxPowerLowAlarmPortn_Type()
)
pmo10010AlmClientTxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmClientTxPowerLowAlarmPortn.setStatus("current")
_Pmo10010AlmClientTxPowerLowWarningPortn_Type = EkiOnOff
_Pmo10010AlmClientTxPowerLowWarningPortn_Object = MibTableColumn
pmo10010AlmClientTxPowerLowWarningPortn = _Pmo10010AlmClientTxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 1, 56, 1, 11),
    _Pmo10010AlmClientTxPowerLowWarningPortn_Type()
)
pmo10010AlmClientTxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmClientTxPowerLowWarningPortn.setStatus("current")
_Pmo10010AlmClientTxPowerHighWarningPortn_Type = EkiOnOff
_Pmo10010AlmClientTxPowerHighWarningPortn_Object = MibTableColumn
pmo10010AlmClientTxPowerHighWarningPortn = _Pmo10010AlmClientTxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 1, 56, 1, 12),
    _Pmo10010AlmClientTxPowerHighWarningPortn_Type()
)
pmo10010AlmClientTxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmClientTxPowerHighWarningPortn.setStatus("current")
_Pmo10010AlmClientTxPowerHighAlarmPortn_Type = EkiOnOff
_Pmo10010AlmClientTxPowerHighAlarmPortn_Object = MibTableColumn
pmo10010AlmClientTxPowerHighAlarmPortn = _Pmo10010AlmClientTxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 1, 56, 1, 13),
    _Pmo10010AlmClientTxPowerHighAlarmPortn_Type()
)
pmo10010AlmClientTxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmClientTxPowerHighAlarmPortn.setStatus("current")
_Pmo10010AlmClientBiasLowAlarmPortn_Type = EkiOnOff
_Pmo10010AlmClientBiasLowAlarmPortn_Object = MibTableColumn
pmo10010AlmClientBiasLowAlarmPortn = _Pmo10010AlmClientBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 1, 56, 1, 14),
    _Pmo10010AlmClientBiasLowAlarmPortn_Type()
)
pmo10010AlmClientBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmClientBiasLowAlarmPortn.setStatus("current")
_Pmo10010AlmClientBiasLowWarningPortn_Type = EkiOnOff
_Pmo10010AlmClientBiasLowWarningPortn_Object = MibTableColumn
pmo10010AlmClientBiasLowWarningPortn = _Pmo10010AlmClientBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 1, 56, 1, 15),
    _Pmo10010AlmClientBiasLowWarningPortn_Type()
)
pmo10010AlmClientBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmClientBiasLowWarningPortn.setStatus("current")
_Pmo10010AlmClientBiasHighWarningPortn_Type = EkiOnOff
_Pmo10010AlmClientBiasHighWarningPortn_Object = MibTableColumn
pmo10010AlmClientBiasHighWarningPortn = _Pmo10010AlmClientBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 1, 56, 1, 16),
    _Pmo10010AlmClientBiasHighWarningPortn_Type()
)
pmo10010AlmClientBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmClientBiasHighWarningPortn.setStatus("current")
_Pmo10010AlmClientBiasHighAlarmPortn_Type = EkiOnOff
_Pmo10010AlmClientBiasHighAlarmPortn_Object = MibTableColumn
pmo10010AlmClientBiasHighAlarmPortn = _Pmo10010AlmClientBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 1, 56, 1, 17),
    _Pmo10010AlmClientBiasHighAlarmPortn_Type()
)
pmo10010AlmClientBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmClientBiasHighAlarmPortn.setStatus("current")
_Pmo10010AlmclientSfpWarnDdmTable_Object = MibTable
pmo10010AlmclientSfpWarnDdmTable = _Pmo10010AlmclientSfpWarnDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 1, 232)
)
if mibBuilder.loadTexts:
    pmo10010AlmclientSfpWarnDdmTable.setStatus("current")
_Pmo10010AlmclientSfpWarnDdmEntry_Object = MibTableRow
pmo10010AlmclientSfpWarnDdmEntry = _Pmo10010AlmclientSfpWarnDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 1, 232, 1)
)
pmo10010AlmclientSfpWarnDdmEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010AlmclientSfpWarnDdmIndex"),
)
if mibBuilder.loadTexts:
    pmo10010AlmclientSfpWarnDdmEntry.setStatus("current")


class _Pmo10010AlmclientSfpWarnDdmIndex_Type(Integer32):
    """Custom type pmo10010AlmclientSfpWarnDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010AlmclientSfpWarnDdmIndex_Type.__name__ = "Integer32"
_Pmo10010AlmclientSfpWarnDdmIndex_Object = MibTableColumn
pmo10010AlmclientSfpWarnDdmIndex = _Pmo10010AlmclientSfpWarnDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 1, 232, 1, 1),
    _Pmo10010AlmclientSfpWarnDdmIndex_Type()
)
pmo10010AlmclientSfpWarnDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmclientSfpWarnDdmIndex.setStatus("current")
_Pmo10010AlmTxPwLowWngPortn_Type = EkiOnOff
_Pmo10010AlmTxPwLowWngPortn_Object = MibTableColumn
pmo10010AlmTxPwLowWngPortn = _Pmo10010AlmTxPwLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 1, 232, 1, 2),
    _Pmo10010AlmTxPwLowWngPortn_Type()
)
pmo10010AlmTxPwLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmTxPwLowWngPortn.setStatus("current")
_Pmo10010AlmTxPwrHighWngPortn_Type = EkiOnOff
_Pmo10010AlmTxPwrHighWngPortn_Object = MibTableColumn
pmo10010AlmTxPwrHighWngPortn = _Pmo10010AlmTxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 1, 232, 1, 3),
    _Pmo10010AlmTxPwrHighWngPortn_Type()
)
pmo10010AlmTxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmTxPwrHighWngPortn.setStatus("current")
_Pmo10010AlmTxBiasLowWngPortn_Type = EkiOnOff
_Pmo10010AlmTxBiasLowWngPortn_Object = MibTableColumn
pmo10010AlmTxBiasLowWngPortn = _Pmo10010AlmTxBiasLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 1, 232, 1, 4),
    _Pmo10010AlmTxBiasLowWngPortn_Type()
)
pmo10010AlmTxBiasLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmTxBiasLowWngPortn.setStatus("current")
_Pmo10010AlmTxBiasHighWngPortn_Type = EkiOnOff
_Pmo10010AlmTxBiasHighWngPortn_Object = MibTableColumn
pmo10010AlmTxBiasHighWngPortn = _Pmo10010AlmTxBiasHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 1, 232, 1, 5),
    _Pmo10010AlmTxBiasHighWngPortn_Type()
)
pmo10010AlmTxBiasHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmTxBiasHighWngPortn.setStatus("current")
_Pmo10010AlmVccLowWngPortn_Type = EkiOnOff
_Pmo10010AlmVccLowWngPortn_Object = MibTableColumn
pmo10010AlmVccLowWngPortn = _Pmo10010AlmVccLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 1, 232, 1, 6),
    _Pmo10010AlmVccLowWngPortn_Type()
)
pmo10010AlmVccLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmVccLowWngPortn.setStatus("current")
_Pmo10010AlmVccHighWngPortn_Type = EkiOnOff
_Pmo10010AlmVccHighWngPortn_Object = MibTableColumn
pmo10010AlmVccHighWngPortn = _Pmo10010AlmVccHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 1, 232, 1, 7),
    _Pmo10010AlmVccHighWngPortn_Type()
)
pmo10010AlmVccHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmVccHighWngPortn.setStatus("current")
_Pmo10010AlmTempLowWngPortn_Type = EkiOnOff
_Pmo10010AlmTempLowWngPortn_Object = MibTableColumn
pmo10010AlmTempLowWngPortn = _Pmo10010AlmTempLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 1, 232, 1, 8),
    _Pmo10010AlmTempLowWngPortn_Type()
)
pmo10010AlmTempLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmTempLowWngPortn.setStatus("current")
_Pmo10010AlmTempHighWngPortn_Type = EkiOnOff
_Pmo10010AlmTempHighWngPortn_Object = MibTableColumn
pmo10010AlmTempHighWngPortn = _Pmo10010AlmTempHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 1, 232, 1, 9),
    _Pmo10010AlmTempHighWngPortn_Type()
)
pmo10010AlmTempHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmTempHighWngPortn.setStatus("current")
_Pmo10010AlmRxPwrLowWngPortn_Type = EkiOnOff
_Pmo10010AlmRxPwrLowWngPortn_Object = MibTableColumn
pmo10010AlmRxPwrLowWngPortn = _Pmo10010AlmRxPwrLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 1, 232, 1, 16),
    _Pmo10010AlmRxPwrLowWngPortn_Type()
)
pmo10010AlmRxPwrLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmRxPwrLowWngPortn.setStatus("current")
_Pmo10010AlmRxPwrHighWngPortn_Type = EkiOnOff
_Pmo10010AlmRxPwrHighWngPortn_Object = MibTableColumn
pmo10010AlmRxPwrHighWngPortn = _Pmo10010AlmRxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 1, 232, 1, 17),
    _Pmo10010AlmRxPwrHighWngPortn_Type()
)
pmo10010AlmRxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmRxPwrHighWngPortn.setStatus("current")
_Pmo10010AlmClientUrg_ObjectIdentity = ObjectIdentity
pmo10010AlmClientUrg = _Pmo10010AlmClientUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 2)
)
_Pmo10010AlmclientNetworkLaneFaultTable_Object = MibTable
pmo10010AlmclientNetworkLaneFaultTable = _Pmo10010AlmclientNetworkLaneFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 2, 72)
)
if mibBuilder.loadTexts:
    pmo10010AlmclientNetworkLaneFaultTable.setStatus("current")
_Pmo10010AlmclientNetworkLaneFaultEntry_Object = MibTableRow
pmo10010AlmclientNetworkLaneFaultEntry = _Pmo10010AlmclientNetworkLaneFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 2, 72, 1)
)
pmo10010AlmclientNetworkLaneFaultEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010AlmclientNetworkLaneFaultIndex"),
)
if mibBuilder.loadTexts:
    pmo10010AlmclientNetworkLaneFaultEntry.setStatus("current")


class _Pmo10010AlmclientNetworkLaneFaultIndex_Type(Integer32):
    """Custom type pmo10010AlmclientNetworkLaneFaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010AlmclientNetworkLaneFaultIndex_Type.__name__ = "Integer32"
_Pmo10010AlmclientNetworkLaneFaultIndex_Object = MibTableColumn
pmo10010AlmclientNetworkLaneFaultIndex = _Pmo10010AlmclientNetworkLaneFaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 2, 72, 1, 1),
    _Pmo10010AlmclientNetworkLaneFaultIndex_Type()
)
pmo10010AlmclientNetworkLaneFaultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmclientNetworkLaneFaultIndex.setStatus("current")
_Pmo10010AlmClientLaneRxFifoErrorPortn_Type = EkiOnOff
_Pmo10010AlmClientLaneRxFifoErrorPortn_Object = MibTableColumn
pmo10010AlmClientLaneRxFifoErrorPortn = _Pmo10010AlmClientLaneRxFifoErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 2, 72, 1, 4),
    _Pmo10010AlmClientLaneRxFifoErrorPortn_Type()
)
pmo10010AlmClientLaneRxFifoErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmClientLaneRxFifoErrorPortn.setStatus("current")
_Pmo10010AlmClientLaneRxLolPortn_Type = EkiOnOff
_Pmo10010AlmClientLaneRxLolPortn_Object = MibTableColumn
pmo10010AlmClientLaneRxLolPortn = _Pmo10010AlmClientLaneRxLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 2, 72, 1, 5),
    _Pmo10010AlmClientLaneRxLolPortn_Type()
)
pmo10010AlmClientLaneRxLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmClientLaneRxLolPortn.setStatus("current")
_Pmo10010AlmClientLaneRxLosPortn_Type = EkiOnOff
_Pmo10010AlmClientLaneRxLosPortn_Object = MibTableColumn
pmo10010AlmClientLaneRxLosPortn = _Pmo10010AlmClientLaneRxLosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 2, 72, 1, 6),
    _Pmo10010AlmClientLaneRxLosPortn_Type()
)
pmo10010AlmClientLaneRxLosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmClientLaneRxLosPortn.setStatus("current")
_Pmo10010AlmClientLaneTxLolPortn_Type = EkiOnOff
_Pmo10010AlmClientLaneTxLolPortn_Object = MibTableColumn
pmo10010AlmClientLaneTxLolPortn = _Pmo10010AlmClientLaneTxLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 2, 72, 1, 8),
    _Pmo10010AlmClientLaneTxLolPortn_Type()
)
pmo10010AlmClientLaneTxLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmClientLaneTxLolPortn.setStatus("current")
_Pmo10010AlmClientLaneTxLosfPortn_Type = EkiOnOff
_Pmo10010AlmClientLaneTxLosfPortn_Object = MibTableColumn
pmo10010AlmClientLaneTxLosfPortn = _Pmo10010AlmClientLaneTxLosfPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 2, 72, 1, 9),
    _Pmo10010AlmClientLaneTxLosfPortn_Type()
)
pmo10010AlmClientLaneTxLosfPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmClientLaneTxLosfPortn.setStatus("current")
_Pmo10010AlmClientLaneApdPowerSupplyPortn_Type = EkiOnOff
_Pmo10010AlmClientLaneApdPowerSupplyPortn_Object = MibTableColumn
pmo10010AlmClientLaneApdPowerSupplyPortn = _Pmo10010AlmClientLaneApdPowerSupplyPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 2, 72, 1, 15),
    _Pmo10010AlmClientLaneApdPowerSupplyPortn_Type()
)
pmo10010AlmClientLaneApdPowerSupplyPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmClientLaneApdPowerSupplyPortn.setStatus("current")
_Pmo10010AlmClientLaneWavelengthUnlockedPortn_Type = EkiOnOff
_Pmo10010AlmClientLaneWavelengthUnlockedPortn_Object = MibTableColumn
pmo10010AlmClientLaneWavelengthUnlockedPortn = _Pmo10010AlmClientLaneWavelengthUnlockedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 2, 72, 1, 16),
    _Pmo10010AlmClientLaneWavelengthUnlockedPortn_Type()
)
pmo10010AlmClientLaneWavelengthUnlockedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmClientLaneWavelengthUnlockedPortn.setStatus("current")
_Pmo10010AlmClientLaneTecFaultPortn_Type = EkiOnOff
_Pmo10010AlmClientLaneTecFaultPortn_Object = MibTableColumn
pmo10010AlmClientLaneTecFaultPortn = _Pmo10010AlmClientLaneTecFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 2, 72, 1, 17),
    _Pmo10010AlmClientLaneTecFaultPortn_Type()
)
pmo10010AlmClientLaneTecFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmClientLaneTecFaultPortn.setStatus("current")
_Pmo10010AlmclientHostLaneFaultTable_Object = MibTable
pmo10010AlmclientHostLaneFaultTable = _Pmo10010AlmclientHostLaneFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 2, 88)
)
if mibBuilder.loadTexts:
    pmo10010AlmclientHostLaneFaultTable.setStatus("current")
_Pmo10010AlmclientHostLaneFaultEntry_Object = MibTableRow
pmo10010AlmclientHostLaneFaultEntry = _Pmo10010AlmclientHostLaneFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 2, 88, 1)
)
pmo10010AlmclientHostLaneFaultEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010AlmclientHostLaneFaultIndex"),
)
if mibBuilder.loadTexts:
    pmo10010AlmclientHostLaneFaultEntry.setStatus("current")


class _Pmo10010AlmclientHostLaneFaultIndex_Type(Integer32):
    """Custom type pmo10010AlmclientHostLaneFaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010AlmclientHostLaneFaultIndex_Type.__name__ = "Integer32"
_Pmo10010AlmclientHostLaneFaultIndex_Object = MibTableColumn
pmo10010AlmclientHostLaneFaultIndex = _Pmo10010AlmclientHostLaneFaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 2, 88, 1, 1),
    _Pmo10010AlmclientHostLaneFaultIndex_Type()
)
pmo10010AlmclientHostLaneFaultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmclientHostLaneFaultIndex.setStatus("current")
_Pmo10010AlmClientRxLossOfSyncPortn_Type = EkiOnOff
_Pmo10010AlmClientRxLossOfSyncPortn_Object = MibTableColumn
pmo10010AlmClientRxLossOfSyncPortn = _Pmo10010AlmClientRxLossOfSyncPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 2, 88, 1, 2),
    _Pmo10010AlmClientRxLossOfSyncPortn_Type()
)
pmo10010AlmClientRxLossOfSyncPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmClientRxLossOfSyncPortn.setStatus("current")
_Pmo10010AlmClientInputLossOfSigPortn_Type = EkiOnOff
_Pmo10010AlmClientInputLossOfSigPortn_Object = MibTableColumn
pmo10010AlmClientInputLossOfSigPortn = _Pmo10010AlmClientInputLossOfSigPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 2, 88, 1, 3),
    _Pmo10010AlmClientInputLossOfSigPortn_Type()
)
pmo10010AlmClientInputLossOfSigPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmClientInputLossOfSigPortn.setStatus("current")
_Pmo10010AlmClientLanesMarkerUnlockPortn_Type = EkiOnOff
_Pmo10010AlmClientLanesMarkerUnlockPortn_Object = MibTableColumn
pmo10010AlmClientLanesMarkerUnlockPortn = _Pmo10010AlmClientLanesMarkerUnlockPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 2, 88, 1, 4),
    _Pmo10010AlmClientLanesMarkerUnlockPortn_Type()
)
pmo10010AlmClientLanesMarkerUnlockPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmClientLanesMarkerUnlockPortn.setStatus("current")
_Pmo10010AlmClientLanes6466UnlockPortn_Type = EkiOnOff
_Pmo10010AlmClientLanes6466UnlockPortn_Object = MibTableColumn
pmo10010AlmClientLanes6466UnlockPortn = _Pmo10010AlmClientLanes6466UnlockPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 2, 88, 1, 5),
    _Pmo10010AlmClientLanes6466UnlockPortn_Type()
)
pmo10010AlmClientLanes6466UnlockPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmClientLanes6466UnlockPortn.setStatus("current")
_Pmo10010AlmClientLanesNotAlignedPortn_Type = EkiOnOff
_Pmo10010AlmClientLanesNotAlignedPortn_Object = MibTableColumn
pmo10010AlmClientLanesNotAlignedPortn = _Pmo10010AlmClientLanesNotAlignedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 2, 88, 1, 6),
    _Pmo10010AlmClientLanesNotAlignedPortn_Type()
)
pmo10010AlmClientLanesNotAlignedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmClientLanesNotAlignedPortn.setStatus("current")
_Pmo10010AlmClientCsfDetectedPortn_Type = EkiOnOff
_Pmo10010AlmClientCsfDetectedPortn_Object = MibTableColumn
pmo10010AlmClientCsfDetectedPortn = _Pmo10010AlmClientCsfDetectedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 2, 88, 1, 7),
    _Pmo10010AlmClientCsfDetectedPortn_Type()
)
pmo10010AlmClientCsfDetectedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmClientCsfDetectedPortn.setStatus("current")
_Pmo10010AlmClientTxHostLolPortn_Type = EkiOnOff
_Pmo10010AlmClientTxHostLolPortn_Object = MibTableColumn
pmo10010AlmClientTxHostLolPortn = _Pmo10010AlmClientTxHostLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 2, 88, 1, 10),
    _Pmo10010AlmClientTxHostLolPortn_Type()
)
pmo10010AlmClientTxHostLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmClientTxHostLolPortn.setStatus("current")
_Pmo10010AlmClientLaneTxFifoErrorPortn_Type = EkiOnOff
_Pmo10010AlmClientLaneTxFifoErrorPortn_Object = MibTableColumn
pmo10010AlmClientLaneTxFifoErrorPortn = _Pmo10010AlmClientLaneTxFifoErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 2, 88, 1, 11),
    _Pmo10010AlmClientLaneTxFifoErrorPortn_Type()
)
pmo10010AlmClientLaneTxFifoErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmClientLaneTxFifoErrorPortn.setStatus("current")
_Pmo10010AlmRxLocalFaultDetectedPortn_Type = EkiOnOff
_Pmo10010AlmRxLocalFaultDetectedPortn_Object = MibTableColumn
pmo10010AlmRxLocalFaultDetectedPortn = _Pmo10010AlmRxLocalFaultDetectedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 2, 88, 1, 12),
    _Pmo10010AlmRxLocalFaultDetectedPortn_Type()
)
pmo10010AlmRxLocalFaultDetectedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmRxLocalFaultDetectedPortn.setStatus("current")
_Pmo10010AlmRxRemoteFaultDetectedPortn_Type = EkiOnOff
_Pmo10010AlmRxRemoteFaultDetectedPortn_Object = MibTableColumn
pmo10010AlmRxRemoteFaultDetectedPortn = _Pmo10010AlmRxRemoteFaultDetectedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 2, 88, 1, 13),
    _Pmo10010AlmRxRemoteFaultDetectedPortn_Type()
)
pmo10010AlmRxRemoteFaultDetectedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmRxRemoteFaultDetectedPortn.setStatus("current")
_Pmo10010AlmTxLocalFaultDetectedPortn_Type = EkiOnOff
_Pmo10010AlmTxLocalFaultDetectedPortn_Object = MibTableColumn
pmo10010AlmTxLocalFaultDetectedPortn = _Pmo10010AlmTxLocalFaultDetectedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 2, 88, 1, 14),
    _Pmo10010AlmTxLocalFaultDetectedPortn_Type()
)
pmo10010AlmTxLocalFaultDetectedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmTxLocalFaultDetectedPortn.setStatus("current")
_Pmo10010AlmTxRemoteFaultDetectedPortn_Type = EkiOnOff
_Pmo10010AlmTxRemoteFaultDetectedPortn_Object = MibTableColumn
pmo10010AlmTxRemoteFaultDetectedPortn = _Pmo10010AlmTxRemoteFaultDetectedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 2, 88, 1, 15),
    _Pmo10010AlmTxRemoteFaultDetectedPortn_Type()
)
pmo10010AlmTxRemoteFaultDetectedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmTxRemoteFaultDetectedPortn.setStatus("current")
_Pmo10010AlmClientTxLossOfSyncPortn_Type = EkiOnOff
_Pmo10010AlmClientTxLossOfSyncPortn_Object = MibTableColumn
pmo10010AlmClientTxLossOfSyncPortn = _Pmo10010AlmClientTxLossOfSyncPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 2, 88, 1, 16),
    _Pmo10010AlmClientTxLossOfSyncPortn_Type()
)
pmo10010AlmClientTxLossOfSyncPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmClientTxLossOfSyncPortn.setStatus("current")
_Pmo10010AlmclientOtnAlmTable_Object = MibTable
pmo10010AlmclientOtnAlmTable = _Pmo10010AlmclientOtnAlmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 2, 200)
)
if mibBuilder.loadTexts:
    pmo10010AlmclientOtnAlmTable.setStatus("current")
_Pmo10010AlmclientOtnAlmEntry_Object = MibTableRow
pmo10010AlmclientOtnAlmEntry = _Pmo10010AlmclientOtnAlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 2, 200, 1)
)
pmo10010AlmclientOtnAlmEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010AlmclientOtnAlmIndex"),
)
if mibBuilder.loadTexts:
    pmo10010AlmclientOtnAlmEntry.setStatus("current")


class _Pmo10010AlmclientOtnAlmIndex_Type(Integer32):
    """Custom type pmo10010AlmclientOtnAlmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010AlmclientOtnAlmIndex_Type.__name__ = "Integer32"
_Pmo10010AlmclientOtnAlmIndex_Object = MibTableColumn
pmo10010AlmclientOtnAlmIndex = _Pmo10010AlmclientOtnAlmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 2, 200, 1, 1),
    _Pmo10010AlmclientOtnAlmIndex_Type()
)
pmo10010AlmclientOtnAlmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmclientOtnAlmIndex.setStatus("current")
_Pmo10010AlmClientOtu2eDlomPortn_Type = EkiOnOff
_Pmo10010AlmClientOtu2eDlomPortn_Object = MibTableColumn
pmo10010AlmClientOtu2eDlomPortn = _Pmo10010AlmClientOtu2eDlomPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 2, 200, 1, 2),
    _Pmo10010AlmClientOtu2eDlomPortn_Type()
)
pmo10010AlmClientOtu2eDlomPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmClientOtu2eDlomPortn.setStatus("current")
_Pmo10010AlmClientOtu2eDlofPortn_Type = EkiOnOff
_Pmo10010AlmClientOtu2eDlofPortn_Object = MibTableColumn
pmo10010AlmClientOtu2eDlofPortn = _Pmo10010AlmClientOtu2eDlofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 2, 200, 1, 3),
    _Pmo10010AlmClientOtu2eDlofPortn_Type()
)
pmo10010AlmClientOtu2eDlofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmClientOtu2eDlofPortn.setStatus("current")
_Pmo10010AlmClientOdu2eDplmPortn_Type = EkiOnOff
_Pmo10010AlmClientOdu2eDplmPortn_Object = MibTableColumn
pmo10010AlmClientOdu2eDplmPortn = _Pmo10010AlmClientOdu2eDplmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 2, 200, 1, 4),
    _Pmo10010AlmClientOdu2eDplmPortn_Type()
)
pmo10010AlmClientOdu2eDplmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmClientOdu2eDplmPortn.setStatus("current")
_Pmo10010AlmClientOdu2eDdegPortn_Type = EkiOnOff
_Pmo10010AlmClientOdu2eDdegPortn_Object = MibTableColumn
pmo10010AlmClientOdu2eDdegPortn = _Pmo10010AlmClientOdu2eDdegPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 2, 200, 1, 6),
    _Pmo10010AlmClientOdu2eDdegPortn_Type()
)
pmo10010AlmClientOdu2eDdegPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmClientOdu2eDdegPortn.setStatus("current")
_Pmo10010AlmClientCsfDetectedOtnPortn_Type = EkiOnOff
_Pmo10010AlmClientCsfDetectedOtnPortn_Object = MibTableColumn
pmo10010AlmClientCsfDetectedOtnPortn = _Pmo10010AlmClientCsfDetectedOtnPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 2, 200, 1, 7),
    _Pmo10010AlmClientCsfDetectedOtnPortn_Type()
)
pmo10010AlmClientCsfDetectedOtnPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmClientCsfDetectedOtnPortn.setStatus("current")
_Pmo10010AlmClientOdu2eIaisPortn_Type = EkiOnOff
_Pmo10010AlmClientOdu2eIaisPortn_Object = MibTableColumn
pmo10010AlmClientOdu2eIaisPortn = _Pmo10010AlmClientOdu2eIaisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 2, 200, 1, 8),
    _Pmo10010AlmClientOdu2eIaisPortn_Type()
)
pmo10010AlmClientOdu2eIaisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmClientOdu2eIaisPortn.setStatus("current")
_Pmo10010AlmClientOdu2eDtimPortn_Type = EkiOnOff
_Pmo10010AlmClientOdu2eDtimPortn_Object = MibTableColumn
pmo10010AlmClientOdu2eDtimPortn = _Pmo10010AlmClientOdu2eDtimPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 2, 200, 1, 9),
    _Pmo10010AlmClientOdu2eDtimPortn_Type()
)
pmo10010AlmClientOdu2eDtimPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmClientOdu2eDtimPortn.setStatus("current")
_Pmo10010AlmClientOdu2eDaisPortn_Type = EkiOnOff
_Pmo10010AlmClientOdu2eDaisPortn_Object = MibTableColumn
pmo10010AlmClientOdu2eDaisPortn = _Pmo10010AlmClientOdu2eDaisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 2, 200, 1, 10),
    _Pmo10010AlmClientOdu2eDaisPortn_Type()
)
pmo10010AlmClientOdu2eDaisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmClientOdu2eDaisPortn.setStatus("current")
_Pmo10010AlmClientOdu2eIociPortn_Type = EkiOnOff
_Pmo10010AlmClientOdu2eIociPortn_Object = MibTableColumn
pmo10010AlmClientOdu2eIociPortn = _Pmo10010AlmClientOdu2eIociPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 2, 200, 1, 12),
    _Pmo10010AlmClientOdu2eIociPortn_Type()
)
pmo10010AlmClientOdu2eIociPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmClientOdu2eIociPortn.setStatus("current")
_Pmo10010AlmClientOdu2eDociPortn_Type = EkiOnOff
_Pmo10010AlmClientOdu2eDociPortn_Object = MibTableColumn
pmo10010AlmClientOdu2eDociPortn = _Pmo10010AlmClientOdu2eDociPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 2, 200, 1, 13),
    _Pmo10010AlmClientOdu2eDociPortn_Type()
)
pmo10010AlmClientOdu2eDociPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmClientOdu2eDociPortn.setStatus("current")
_Pmo10010AlmClientOdu2eIbdiPortn_Type = EkiOnOff
_Pmo10010AlmClientOdu2eIbdiPortn_Object = MibTableColumn
pmo10010AlmClientOdu2eIbdiPortn = _Pmo10010AlmClientOdu2eIbdiPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 2, 200, 1, 14),
    _Pmo10010AlmClientOdu2eIbdiPortn_Type()
)
pmo10010AlmClientOdu2eIbdiPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmClientOdu2eIbdiPortn.setStatus("current")
_Pmo10010AlmClientOdu2eDbdiPortn_Type = EkiOnOff
_Pmo10010AlmClientOdu2eDbdiPortn_Object = MibTableColumn
pmo10010AlmClientOdu2eDbdiPortn = _Pmo10010AlmClientOdu2eDbdiPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 2, 200, 1, 15),
    _Pmo10010AlmClientOdu2eDbdiPortn_Type()
)
pmo10010AlmClientOdu2eDbdiPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmClientOdu2eDbdiPortn.setStatus("current")
_Pmo10010AlmClientOdu2eIlckPortn_Type = EkiOnOff
_Pmo10010AlmClientOdu2eIlckPortn_Object = MibTableColumn
pmo10010AlmClientOdu2eIlckPortn = _Pmo10010AlmClientOdu2eIlckPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 2, 200, 1, 16),
    _Pmo10010AlmClientOdu2eIlckPortn_Type()
)
pmo10010AlmClientOdu2eIlckPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmClientOdu2eIlckPortn.setStatus("current")
_Pmo10010AlmClientOdu2eDlckPortn_Type = EkiOnOff
_Pmo10010AlmClientOdu2eDlckPortn_Object = MibTableColumn
pmo10010AlmClientOdu2eDlckPortn = _Pmo10010AlmClientOdu2eDlckPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 2, 200, 1, 17),
    _Pmo10010AlmClientOdu2eDlckPortn_Type()
)
pmo10010AlmClientOdu2eDlckPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmClientOdu2eDlckPortn.setStatus("current")
_Pmo10010AlmclientSfpAlmDdmTable_Object = MibTable
pmo10010AlmclientSfpAlmDdmTable = _Pmo10010AlmclientSfpAlmDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 2, 216)
)
if mibBuilder.loadTexts:
    pmo10010AlmclientSfpAlmDdmTable.setStatus("current")
_Pmo10010AlmclientSfpAlmDdmEntry_Object = MibTableRow
pmo10010AlmclientSfpAlmDdmEntry = _Pmo10010AlmclientSfpAlmDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 2, 216, 1)
)
pmo10010AlmclientSfpAlmDdmEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010AlmclientSfpAlmDdmIndex"),
)
if mibBuilder.loadTexts:
    pmo10010AlmclientSfpAlmDdmEntry.setStatus("current")


class _Pmo10010AlmclientSfpAlmDdmIndex_Type(Integer32):
    """Custom type pmo10010AlmclientSfpAlmDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010AlmclientSfpAlmDdmIndex_Type.__name__ = "Integer32"
_Pmo10010AlmclientSfpAlmDdmIndex_Object = MibTableColumn
pmo10010AlmclientSfpAlmDdmIndex = _Pmo10010AlmclientSfpAlmDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 2, 216, 1, 1),
    _Pmo10010AlmclientSfpAlmDdmIndex_Type()
)
pmo10010AlmclientSfpAlmDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmclientSfpAlmDdmIndex.setStatus("current")
_Pmo10010AlmTxPwrLowAlaPortn_Type = EkiOnOff
_Pmo10010AlmTxPwrLowAlaPortn_Object = MibTableColumn
pmo10010AlmTxPwrLowAlaPortn = _Pmo10010AlmTxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 2, 216, 1, 2),
    _Pmo10010AlmTxPwrLowAlaPortn_Type()
)
pmo10010AlmTxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmTxPwrLowAlaPortn.setStatus("current")
_Pmo10010AlmTxPwrHighAlaPortn_Type = EkiOnOff
_Pmo10010AlmTxPwrHighAlaPortn_Object = MibTableColumn
pmo10010AlmTxPwrHighAlaPortn = _Pmo10010AlmTxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 2, 216, 1, 3),
    _Pmo10010AlmTxPwrHighAlaPortn_Type()
)
pmo10010AlmTxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmTxPwrHighAlaPortn.setStatus("current")
_Pmo10010AlmTxBiasLowAlaPortn_Type = EkiOnOff
_Pmo10010AlmTxBiasLowAlaPortn_Object = MibTableColumn
pmo10010AlmTxBiasLowAlaPortn = _Pmo10010AlmTxBiasLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 2, 216, 1, 4),
    _Pmo10010AlmTxBiasLowAlaPortn_Type()
)
pmo10010AlmTxBiasLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmTxBiasLowAlaPortn.setStatus("current")
_Pmo10010AlmTxBiasHighAlaPortn_Type = EkiOnOff
_Pmo10010AlmTxBiasHighAlaPortn_Object = MibTableColumn
pmo10010AlmTxBiasHighAlaPortn = _Pmo10010AlmTxBiasHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 2, 216, 1, 5),
    _Pmo10010AlmTxBiasHighAlaPortn_Type()
)
pmo10010AlmTxBiasHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmTxBiasHighAlaPortn.setStatus("current")
_Pmo10010AlmVccLowAlaPortn_Type = EkiOnOff
_Pmo10010AlmVccLowAlaPortn_Object = MibTableColumn
pmo10010AlmVccLowAlaPortn = _Pmo10010AlmVccLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 2, 216, 1, 6),
    _Pmo10010AlmVccLowAlaPortn_Type()
)
pmo10010AlmVccLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmVccLowAlaPortn.setStatus("current")
_Pmo10010AlmVccHighAlaPortn_Type = EkiOnOff
_Pmo10010AlmVccHighAlaPortn_Object = MibTableColumn
pmo10010AlmVccHighAlaPortn = _Pmo10010AlmVccHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 2, 216, 1, 7),
    _Pmo10010AlmVccHighAlaPortn_Type()
)
pmo10010AlmVccHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmVccHighAlaPortn.setStatus("current")
_Pmo10010AlmTempLowAlaPortn_Type = EkiOnOff
_Pmo10010AlmTempLowAlaPortn_Object = MibTableColumn
pmo10010AlmTempLowAlaPortn = _Pmo10010AlmTempLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 2, 216, 1, 8),
    _Pmo10010AlmTempLowAlaPortn_Type()
)
pmo10010AlmTempLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmTempLowAlaPortn.setStatus("current")
_Pmo10010AlmTempHighAlaPortn_Type = EkiOnOff
_Pmo10010AlmTempHighAlaPortn_Object = MibTableColumn
pmo10010AlmTempHighAlaPortn = _Pmo10010AlmTempHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 2, 216, 1, 9),
    _Pmo10010AlmTempHighAlaPortn_Type()
)
pmo10010AlmTempHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmTempHighAlaPortn.setStatus("current")
_Pmo10010AlmRxPwrLowAlaPortn_Type = EkiOnOff
_Pmo10010AlmRxPwrLowAlaPortn_Object = MibTableColumn
pmo10010AlmRxPwrLowAlaPortn = _Pmo10010AlmRxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 2, 216, 1, 16),
    _Pmo10010AlmRxPwrLowAlaPortn_Type()
)
pmo10010AlmRxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmRxPwrLowAlaPortn.setStatus("current")
_Pmo10010AlmRxPwrHighAlaPortn_Type = EkiOnOff
_Pmo10010AlmRxPwrHighAlaPortn_Object = MibTableColumn
pmo10010AlmRxPwrHighAlaPortn = _Pmo10010AlmRxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 2, 216, 1, 17),
    _Pmo10010AlmRxPwrHighAlaPortn_Type()
)
pmo10010AlmRxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmRxPwrHighAlaPortn.setStatus("current")
_Pmo10010AlmClientCrit_ObjectIdentity = ObjectIdentity
pmo10010AlmClientCrit = _Pmo10010AlmClientCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 3)
)
_Pmo10010AlmsynthAlmPortTable_Object = MibTable
pmo10010AlmsynthAlmPortTable = _Pmo10010AlmsynthAlmPortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 3, 8)
)
if mibBuilder.loadTexts:
    pmo10010AlmsynthAlmPortTable.setStatus("current")
_Pmo10010AlmsynthAlmPortEntry_Object = MibTableRow
pmo10010AlmsynthAlmPortEntry = _Pmo10010AlmsynthAlmPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 3, 8, 1)
)
pmo10010AlmsynthAlmPortEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010AlmsynthAlmPortIndex"),
)
if mibBuilder.loadTexts:
    pmo10010AlmsynthAlmPortEntry.setStatus("current")


class _Pmo10010AlmsynthAlmPortIndex_Type(Integer32):
    """Custom type pmo10010AlmsynthAlmPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010AlmsynthAlmPortIndex_Type.__name__ = "Integer32"
_Pmo10010AlmsynthAlmPortIndex_Object = MibTableColumn
pmo10010AlmsynthAlmPortIndex = _Pmo10010AlmsynthAlmPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 3, 8, 1, 1),
    _Pmo10010AlmsynthAlmPortIndex_Type()
)
pmo10010AlmsynthAlmPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmsynthAlmPortIndex.setStatus("current")
_Pmo10010AlmSfpAbsentPortn_Type = EkiOnOff
_Pmo10010AlmSfpAbsentPortn_Object = MibTableColumn
pmo10010AlmSfpAbsentPortn = _Pmo10010AlmSfpAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 3, 8, 1, 2),
    _Pmo10010AlmSfpAbsentPortn_Type()
)
pmo10010AlmSfpAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmSfpAbsentPortn.setStatus("current")
_Pmo10010AlmDdmAbsentPortn_Type = EkiOnOff
_Pmo10010AlmDdmAbsentPortn_Object = MibTableColumn
pmo10010AlmDdmAbsentPortn = _Pmo10010AlmDdmAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 3, 8, 1, 3),
    _Pmo10010AlmDdmAbsentPortn_Type()
)
pmo10010AlmDdmAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmDdmAbsentPortn.setStatus("current")
_Pmo10010AlmHwFailAccPortn_Type = EkiOnOff
_Pmo10010AlmHwFailAccPortn_Object = MibTableColumn
pmo10010AlmHwFailAccPortn = _Pmo10010AlmHwFailAccPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 3, 8, 1, 5),
    _Pmo10010AlmHwFailAccPortn_Type()
)
pmo10010AlmHwFailAccPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmHwFailAccPortn.setStatus("current")
_Pmo10010AlmDwLsdPortn_Type = EkiOnOff
_Pmo10010AlmDwLsdPortn_Object = MibTableColumn
pmo10010AlmDwLsdPortn = _Pmo10010AlmDwLsdPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 3, 8, 1, 6),
    _Pmo10010AlmDwLsdPortn_Type()
)
pmo10010AlmDwLsdPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmDwLsdPortn.setStatus("current")
_Pmo10010AlmClientLocalOosPortn_Type = EkiOnOff
_Pmo10010AlmClientLocalOosPortn_Object = MibTableColumn
pmo10010AlmClientLocalOosPortn = _Pmo10010AlmClientLocalOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 3, 8, 1, 7),
    _Pmo10010AlmClientLocalOosPortn_Type()
)
pmo10010AlmClientLocalOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmClientLocalOosPortn.setStatus("current")
_Pmo10010AlmClientRemoteOosPortn_Type = EkiOnOff
_Pmo10010AlmClientRemoteOosPortn_Object = MibTableColumn
pmo10010AlmClientRemoteOosPortn = _Pmo10010AlmClientRemoteOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 3, 8, 1, 8),
    _Pmo10010AlmClientRemoteOosPortn_Type()
)
pmo10010AlmClientRemoteOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmClientRemoteOosPortn.setStatus("current")
_Pmo10010AlmDwCaisPortn_Type = EkiOnOff
_Pmo10010AlmDwCaisPortn_Object = MibTableColumn
pmo10010AlmDwCaisPortn = _Pmo10010AlmDwCaisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 3, 8, 1, 9),
    _Pmo10010AlmDwCaisPortn_Type()
)
pmo10010AlmDwCaisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmDwCaisPortn.setStatus("current")
_Pmo10010AlmSfpDdmWarningPortn_Type = EkiOnOff
_Pmo10010AlmSfpDdmWarningPortn_Object = MibTableColumn
pmo10010AlmSfpDdmWarningPortn = _Pmo10010AlmSfpDdmWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 3, 8, 1, 10),
    _Pmo10010AlmSfpDdmWarningPortn_Type()
)
pmo10010AlmSfpDdmWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmSfpDdmWarningPortn.setStatus("current")
_Pmo10010AlmSfpDdmAlmPortn_Type = EkiOnOff
_Pmo10010AlmSfpDdmAlmPortn_Object = MibTableColumn
pmo10010AlmSfpDdmAlmPortn = _Pmo10010AlmSfpDdmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 3, 8, 1, 11),
    _Pmo10010AlmSfpDdmAlmPortn_Type()
)
pmo10010AlmSfpDdmAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmSfpDdmAlmPortn.setStatus("current")
_Pmo10010AlmFailAccPortn_Type = EkiOnOff
_Pmo10010AlmFailAccPortn_Object = MibTableColumn
pmo10010AlmFailAccPortn = _Pmo10010AlmFailAccPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 3, 8, 1, 13),
    _Pmo10010AlmFailAccPortn_Type()
)
pmo10010AlmFailAccPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmFailAccPortn.setStatus("current")
_Pmo10010AlmUpCsfPortn_Type = EkiOnOff
_Pmo10010AlmUpCsfPortn_Object = MibTableColumn
pmo10010AlmUpCsfPortn = _Pmo10010AlmUpCsfPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 2, 3, 8, 1, 17),
    _Pmo10010AlmUpCsfPortn_Type()
)
pmo10010AlmUpCsfPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmUpCsfPortn.setStatus("current")
_Pmo10010AlmLine_ObjectIdentity = ObjectIdentity
pmo10010AlmLine = _Pmo10010AlmLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3)
)
_Pmo10010AlmLineNurg_ObjectIdentity = ObjectIdentity
pmo10010AlmLineNurg = _Pmo10010AlmLineNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 1)
)
_Pmo10010AlmlineNetworkLaneAlarmWarning1Table_Object = MibTable
pmo10010AlmlineNetworkLaneAlarmWarning1Table = _Pmo10010AlmlineNetworkLaneAlarmWarning1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 1, 104)
)
if mibBuilder.loadTexts:
    pmo10010AlmlineNetworkLaneAlarmWarning1Table.setStatus("current")
_Pmo10010AlmlineNetworkLaneAlarmWarning1Entry_Object = MibTableRow
pmo10010AlmlineNetworkLaneAlarmWarning1Entry = _Pmo10010AlmlineNetworkLaneAlarmWarning1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 1, 104, 1)
)
pmo10010AlmlineNetworkLaneAlarmWarning1Entry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010AlmlineNetworkLaneAlarmWarning1Index"),
)
if mibBuilder.loadTexts:
    pmo10010AlmlineNetworkLaneAlarmWarning1Entry.setStatus("current")


class _Pmo10010AlmlineNetworkLaneAlarmWarning1Index_Type(Integer32):
    """Custom type pmo10010AlmlineNetworkLaneAlarmWarning1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010AlmlineNetworkLaneAlarmWarning1Index_Type.__name__ = "Integer32"
_Pmo10010AlmlineNetworkLaneAlarmWarning1Index_Object = MibTableColumn
pmo10010AlmlineNetworkLaneAlarmWarning1Index = _Pmo10010AlmlineNetworkLaneAlarmWarning1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 1, 104, 1, 1),
    _Pmo10010AlmlineNetworkLaneAlarmWarning1Index_Type()
)
pmo10010AlmlineNetworkLaneAlarmWarning1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmlineNetworkLaneAlarmWarning1Index.setStatus("current")
_Pmo10010AlmLineRxPowerLowAlarmPortn_Type = EkiOnOff
_Pmo10010AlmLineRxPowerLowAlarmPortn_Object = MibTableColumn
pmo10010AlmLineRxPowerLowAlarmPortn = _Pmo10010AlmLineRxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 1, 104, 1, 2),
    _Pmo10010AlmLineRxPowerLowAlarmPortn_Type()
)
pmo10010AlmLineRxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineRxPowerLowAlarmPortn.setStatus("current")
_Pmo10010AlmLineRxPowerLowWarningPortn_Type = EkiOnOff
_Pmo10010AlmLineRxPowerLowWarningPortn_Object = MibTableColumn
pmo10010AlmLineRxPowerLowWarningPortn = _Pmo10010AlmLineRxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 1, 104, 1, 3),
    _Pmo10010AlmLineRxPowerLowWarningPortn_Type()
)
pmo10010AlmLineRxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineRxPowerLowWarningPortn.setStatus("current")
_Pmo10010AlmLineRxPowerHighWarningPortn_Type = EkiOnOff
_Pmo10010AlmLineRxPowerHighWarningPortn_Object = MibTableColumn
pmo10010AlmLineRxPowerHighWarningPortn = _Pmo10010AlmLineRxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 1, 104, 1, 4),
    _Pmo10010AlmLineRxPowerHighWarningPortn_Type()
)
pmo10010AlmLineRxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineRxPowerHighWarningPortn.setStatus("current")
_Pmo10010AlmLineRxPowerHighAlarmPortn_Type = EkiOnOff
_Pmo10010AlmLineRxPowerHighAlarmPortn_Object = MibTableColumn
pmo10010AlmLineRxPowerHighAlarmPortn = _Pmo10010AlmLineRxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 1, 104, 1, 5),
    _Pmo10010AlmLineRxPowerHighAlarmPortn_Type()
)
pmo10010AlmLineRxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineRxPowerHighAlarmPortn.setStatus("current")
_Pmo10010AlmLineLaserTempLowAlarmPortn_Type = EkiOnOff
_Pmo10010AlmLineLaserTempLowAlarmPortn_Object = MibTableColumn
pmo10010AlmLineLaserTempLowAlarmPortn = _Pmo10010AlmLineLaserTempLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 1, 104, 1, 6),
    _Pmo10010AlmLineLaserTempLowAlarmPortn_Type()
)
pmo10010AlmLineLaserTempLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineLaserTempLowAlarmPortn.setStatus("current")
_Pmo10010AlmLineLaserTempLowWarningPortn_Type = EkiOnOff
_Pmo10010AlmLineLaserTempLowWarningPortn_Object = MibTableColumn
pmo10010AlmLineLaserTempLowWarningPortn = _Pmo10010AlmLineLaserTempLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 1, 104, 1, 7),
    _Pmo10010AlmLineLaserTempLowWarningPortn_Type()
)
pmo10010AlmLineLaserTempLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineLaserTempLowWarningPortn.setStatus("current")
_Pmo10010AlmLineLaserTempHighWarningPortn_Type = EkiOnOff
_Pmo10010AlmLineLaserTempHighWarningPortn_Object = MibTableColumn
pmo10010AlmLineLaserTempHighWarningPortn = _Pmo10010AlmLineLaserTempHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 1, 104, 1, 8),
    _Pmo10010AlmLineLaserTempHighWarningPortn_Type()
)
pmo10010AlmLineLaserTempHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineLaserTempHighWarningPortn.setStatus("current")
_Pmo10010AlmLineLaserTempHighAlarmPortn_Type = EkiOnOff
_Pmo10010AlmLineLaserTempHighAlarmPortn_Object = MibTableColumn
pmo10010AlmLineLaserTempHighAlarmPortn = _Pmo10010AlmLineLaserTempHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 1, 104, 1, 9),
    _Pmo10010AlmLineLaserTempHighAlarmPortn_Type()
)
pmo10010AlmLineLaserTempHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineLaserTempHighAlarmPortn.setStatus("current")
_Pmo10010AlmLineTxPowerLowAlarmPortn_Type = EkiOnOff
_Pmo10010AlmLineTxPowerLowAlarmPortn_Object = MibTableColumn
pmo10010AlmLineTxPowerLowAlarmPortn = _Pmo10010AlmLineTxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 1, 104, 1, 10),
    _Pmo10010AlmLineTxPowerLowAlarmPortn_Type()
)
pmo10010AlmLineTxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineTxPowerLowAlarmPortn.setStatus("current")
_Pmo10010AlmLineTxPowerLowWarningPortn_Type = EkiOnOff
_Pmo10010AlmLineTxPowerLowWarningPortn_Object = MibTableColumn
pmo10010AlmLineTxPowerLowWarningPortn = _Pmo10010AlmLineTxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 1, 104, 1, 11),
    _Pmo10010AlmLineTxPowerLowWarningPortn_Type()
)
pmo10010AlmLineTxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineTxPowerLowWarningPortn.setStatus("current")
_Pmo10010AlmLineTxPowerHighWarningPortn_Type = EkiOnOff
_Pmo10010AlmLineTxPowerHighWarningPortn_Object = MibTableColumn
pmo10010AlmLineTxPowerHighWarningPortn = _Pmo10010AlmLineTxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 1, 104, 1, 12),
    _Pmo10010AlmLineTxPowerHighWarningPortn_Type()
)
pmo10010AlmLineTxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineTxPowerHighWarningPortn.setStatus("current")
_Pmo10010AlmLineTxPowerHighAlarmPortn_Type = EkiOnOff
_Pmo10010AlmLineTxPowerHighAlarmPortn_Object = MibTableColumn
pmo10010AlmLineTxPowerHighAlarmPortn = _Pmo10010AlmLineTxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 1, 104, 1, 13),
    _Pmo10010AlmLineTxPowerHighAlarmPortn_Type()
)
pmo10010AlmLineTxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineTxPowerHighAlarmPortn.setStatus("current")
_Pmo10010AlmLineBiasLowAlarmPortn_Type = EkiOnOff
_Pmo10010AlmLineBiasLowAlarmPortn_Object = MibTableColumn
pmo10010AlmLineBiasLowAlarmPortn = _Pmo10010AlmLineBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 1, 104, 1, 14),
    _Pmo10010AlmLineBiasLowAlarmPortn_Type()
)
pmo10010AlmLineBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineBiasLowAlarmPortn.setStatus("current")
_Pmo10010AlmLineBiasLowWarningPortn_Type = EkiOnOff
_Pmo10010AlmLineBiasLowWarningPortn_Object = MibTableColumn
pmo10010AlmLineBiasLowWarningPortn = _Pmo10010AlmLineBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 1, 104, 1, 15),
    _Pmo10010AlmLineBiasLowWarningPortn_Type()
)
pmo10010AlmLineBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineBiasLowWarningPortn.setStatus("current")
_Pmo10010AlmLineBiasHighWarningPortn_Type = EkiOnOff
_Pmo10010AlmLineBiasHighWarningPortn_Object = MibTableColumn
pmo10010AlmLineBiasHighWarningPortn = _Pmo10010AlmLineBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 1, 104, 1, 16),
    _Pmo10010AlmLineBiasHighWarningPortn_Type()
)
pmo10010AlmLineBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineBiasHighWarningPortn.setStatus("current")
_Pmo10010AlmLineBiasHighAlarmPortn_Type = EkiOnOff
_Pmo10010AlmLineBiasHighAlarmPortn_Object = MibTableColumn
pmo10010AlmLineBiasHighAlarmPortn = _Pmo10010AlmLineBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 1, 104, 1, 17),
    _Pmo10010AlmLineBiasHighAlarmPortn_Type()
)
pmo10010AlmLineBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineBiasHighAlarmPortn.setStatus("current")
_Pmo10010AlmlineNetworkLaneAlarmWarning2Table_Object = MibTable
pmo10010AlmlineNetworkLaneAlarmWarning2Table = _Pmo10010AlmlineNetworkLaneAlarmWarning2Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 1, 120)
)
if mibBuilder.loadTexts:
    pmo10010AlmlineNetworkLaneAlarmWarning2Table.setStatus("current")
_Pmo10010AlmlineNetworkLaneAlarmWarning2Entry_Object = MibTableRow
pmo10010AlmlineNetworkLaneAlarmWarning2Entry = _Pmo10010AlmlineNetworkLaneAlarmWarning2Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 1, 120, 1)
)
pmo10010AlmlineNetworkLaneAlarmWarning2Entry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010AlmlineNetworkLaneAlarmWarning2Index"),
)
if mibBuilder.loadTexts:
    pmo10010AlmlineNetworkLaneAlarmWarning2Entry.setStatus("current")


class _Pmo10010AlmlineNetworkLaneAlarmWarning2Index_Type(Integer32):
    """Custom type pmo10010AlmlineNetworkLaneAlarmWarning2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010AlmlineNetworkLaneAlarmWarning2Index_Type.__name__ = "Integer32"
_Pmo10010AlmlineNetworkLaneAlarmWarning2Index_Object = MibTableColumn
pmo10010AlmlineNetworkLaneAlarmWarning2Index = _Pmo10010AlmlineNetworkLaneAlarmWarning2Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 1, 120, 1, 1),
    _Pmo10010AlmlineNetworkLaneAlarmWarning2Index_Type()
)
pmo10010AlmlineNetworkLaneAlarmWarning2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmlineNetworkLaneAlarmWarning2Index.setStatus("current")
_Pmo10010AlmTxModulatorBiasLowAlarmPortn_Type = EkiOnOff
_Pmo10010AlmTxModulatorBiasLowAlarmPortn_Object = MibTableColumn
pmo10010AlmTxModulatorBiasLowAlarmPortn = _Pmo10010AlmTxModulatorBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 1, 120, 1, 2),
    _Pmo10010AlmTxModulatorBiasLowAlarmPortn_Type()
)
pmo10010AlmTxModulatorBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmTxModulatorBiasLowAlarmPortn.setStatus("current")
_Pmo10010AlmTxModulatorBiasLowWarningPortn_Type = EkiOnOff
_Pmo10010AlmTxModulatorBiasLowWarningPortn_Object = MibTableColumn
pmo10010AlmTxModulatorBiasLowWarningPortn = _Pmo10010AlmTxModulatorBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 1, 120, 1, 3),
    _Pmo10010AlmTxModulatorBiasLowWarningPortn_Type()
)
pmo10010AlmTxModulatorBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmTxModulatorBiasLowWarningPortn.setStatus("current")
_Pmo10010AlmTxModulatorBiasHighWarningPortn_Type = EkiOnOff
_Pmo10010AlmTxModulatorBiasHighWarningPortn_Object = MibTableColumn
pmo10010AlmTxModulatorBiasHighWarningPortn = _Pmo10010AlmTxModulatorBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 1, 120, 1, 4),
    _Pmo10010AlmTxModulatorBiasHighWarningPortn_Type()
)
pmo10010AlmTxModulatorBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmTxModulatorBiasHighWarningPortn.setStatus("current")
_Pmo10010AlmTxModulatorBiasHighAlarmPortn_Type = EkiOnOff
_Pmo10010AlmTxModulatorBiasHighAlarmPortn_Object = MibTableColumn
pmo10010AlmTxModulatorBiasHighAlarmPortn = _Pmo10010AlmTxModulatorBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 1, 120, 1, 5),
    _Pmo10010AlmTxModulatorBiasHighAlarmPortn_Type()
)
pmo10010AlmTxModulatorBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmTxModulatorBiasHighAlarmPortn.setStatus("current")
_Pmo10010AlmRxLaserTempLowAlarmPortn_Type = EkiOnOff
_Pmo10010AlmRxLaserTempLowAlarmPortn_Object = MibTableColumn
pmo10010AlmRxLaserTempLowAlarmPortn = _Pmo10010AlmRxLaserTempLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 1, 120, 1, 6),
    _Pmo10010AlmRxLaserTempLowAlarmPortn_Type()
)
pmo10010AlmRxLaserTempLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmRxLaserTempLowAlarmPortn.setStatus("current")
_Pmo10010AlmRxLaserTempLowWarningPortn_Type = EkiOnOff
_Pmo10010AlmRxLaserTempLowWarningPortn_Object = MibTableColumn
pmo10010AlmRxLaserTempLowWarningPortn = _Pmo10010AlmRxLaserTempLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 1, 120, 1, 7),
    _Pmo10010AlmRxLaserTempLowWarningPortn_Type()
)
pmo10010AlmRxLaserTempLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmRxLaserTempLowWarningPortn.setStatus("current")
_Pmo10010AlmRxLaserTempHighWarningPortn_Type = EkiOnOff
_Pmo10010AlmRxLaserTempHighWarningPortn_Object = MibTableColumn
pmo10010AlmRxLaserTempHighWarningPortn = _Pmo10010AlmRxLaserTempHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 1, 120, 1, 8),
    _Pmo10010AlmRxLaserTempHighWarningPortn_Type()
)
pmo10010AlmRxLaserTempHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmRxLaserTempHighWarningPortn.setStatus("current")
_Pmo10010AlmRxLaserTempHighAlarmPortn_Type = EkiOnOff
_Pmo10010AlmRxLaserTempHighAlarmPortn_Object = MibTableColumn
pmo10010AlmRxLaserTempHighAlarmPortn = _Pmo10010AlmRxLaserTempHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 1, 120, 1, 9),
    _Pmo10010AlmRxLaserTempHighAlarmPortn_Type()
)
pmo10010AlmRxLaserTempHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmRxLaserTempHighAlarmPortn.setStatus("current")
_Pmo10010AlmRxLaserOutputLowAlarmPortn_Type = EkiOnOff
_Pmo10010AlmRxLaserOutputLowAlarmPortn_Object = MibTableColumn
pmo10010AlmRxLaserOutputLowAlarmPortn = _Pmo10010AlmRxLaserOutputLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 1, 120, 1, 10),
    _Pmo10010AlmRxLaserOutputLowAlarmPortn_Type()
)
pmo10010AlmRxLaserOutputLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmRxLaserOutputLowAlarmPortn.setStatus("current")
_Pmo10010AlmRxLaserOutputLowWarningPortn_Type = EkiOnOff
_Pmo10010AlmRxLaserOutputLowWarningPortn_Object = MibTableColumn
pmo10010AlmRxLaserOutputLowWarningPortn = _Pmo10010AlmRxLaserOutputLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 1, 120, 1, 11),
    _Pmo10010AlmRxLaserOutputLowWarningPortn_Type()
)
pmo10010AlmRxLaserOutputLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmRxLaserOutputLowWarningPortn.setStatus("current")
_Pmo10010AlmRxLaserOutputHighWarningPortn_Type = EkiOnOff
_Pmo10010AlmRxLaserOutputHighWarningPortn_Object = MibTableColumn
pmo10010AlmRxLaserOutputHighWarningPortn = _Pmo10010AlmRxLaserOutputHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 1, 120, 1, 12),
    _Pmo10010AlmRxLaserOutputHighWarningPortn_Type()
)
pmo10010AlmRxLaserOutputHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmRxLaserOutputHighWarningPortn.setStatus("current")
_Pmo10010AlmRxLaserOutputHighAlarmPortn_Type = EkiOnOff
_Pmo10010AlmRxLaserOutputHighAlarmPortn_Object = MibTableColumn
pmo10010AlmRxLaserOutputHighAlarmPortn = _Pmo10010AlmRxLaserOutputHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 1, 120, 1, 13),
    _Pmo10010AlmRxLaserOutputHighAlarmPortn_Type()
)
pmo10010AlmRxLaserOutputHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmRxLaserOutputHighAlarmPortn.setStatus("current")
_Pmo10010AlmRxLaserBiasLowAlarmPortn_Type = EkiOnOff
_Pmo10010AlmRxLaserBiasLowAlarmPortn_Object = MibTableColumn
pmo10010AlmRxLaserBiasLowAlarmPortn = _Pmo10010AlmRxLaserBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 1, 120, 1, 14),
    _Pmo10010AlmRxLaserBiasLowAlarmPortn_Type()
)
pmo10010AlmRxLaserBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmRxLaserBiasLowAlarmPortn.setStatus("current")
_Pmo10010AlmRxLaserBiasLowWarningPortn_Type = EkiOnOff
_Pmo10010AlmRxLaserBiasLowWarningPortn_Object = MibTableColumn
pmo10010AlmRxLaserBiasLowWarningPortn = _Pmo10010AlmRxLaserBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 1, 120, 1, 15),
    _Pmo10010AlmRxLaserBiasLowWarningPortn_Type()
)
pmo10010AlmRxLaserBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmRxLaserBiasLowWarningPortn.setStatus("current")
_Pmo10010AlmRxLaserBiasHighWarningPortn_Type = EkiOnOff
_Pmo10010AlmRxLaserBiasHighWarningPortn_Object = MibTableColumn
pmo10010AlmRxLaserBiasHighWarningPortn = _Pmo10010AlmRxLaserBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 1, 120, 1, 16),
    _Pmo10010AlmRxLaserBiasHighWarningPortn_Type()
)
pmo10010AlmRxLaserBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmRxLaserBiasHighWarningPortn.setStatus("current")
_Pmo10010AlmRxLaserBiasHighAlarmPortn_Type = EkiOnOff
_Pmo10010AlmRxLaserBiasHighAlarmPortn_Object = MibTableColumn
pmo10010AlmRxLaserBiasHighAlarmPortn = _Pmo10010AlmRxLaserBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 1, 120, 1, 17),
    _Pmo10010AlmRxLaserBiasHighAlarmPortn_Type()
)
pmo10010AlmRxLaserBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmRxLaserBiasHighAlarmPortn.setStatus("current")
_Pmo10010AlmLineUrg_ObjectIdentity = ObjectIdentity
pmo10010AlmLineUrg = _Pmo10010AlmLineUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2)
)
_Pmo10010AlmlineNetworkLaneFaultTable_Object = MibTable
pmo10010AlmlineNetworkLaneFaultTable = _Pmo10010AlmlineNetworkLaneFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 136)
)
if mibBuilder.loadTexts:
    pmo10010AlmlineNetworkLaneFaultTable.setStatus("current")
_Pmo10010AlmlineNetworkLaneFaultEntry_Object = MibTableRow
pmo10010AlmlineNetworkLaneFaultEntry = _Pmo10010AlmlineNetworkLaneFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 136, 1)
)
pmo10010AlmlineNetworkLaneFaultEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010AlmlineNetworkLaneFaultIndex"),
)
if mibBuilder.loadTexts:
    pmo10010AlmlineNetworkLaneFaultEntry.setStatus("current")


class _Pmo10010AlmlineNetworkLaneFaultIndex_Type(Integer32):
    """Custom type pmo10010AlmlineNetworkLaneFaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010AlmlineNetworkLaneFaultIndex_Type.__name__ = "Integer32"
_Pmo10010AlmlineNetworkLaneFaultIndex_Object = MibTableColumn
pmo10010AlmlineNetworkLaneFaultIndex = _Pmo10010AlmlineNetworkLaneFaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 136, 1, 1),
    _Pmo10010AlmlineNetworkLaneFaultIndex_Type()
)
pmo10010AlmlineNetworkLaneFaultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmlineNetworkLaneFaultIndex.setStatus("current")
_Pmo10010AlmLineLaneRxTecFaultPortn_Type = EkiOnOff
_Pmo10010AlmLineLaneRxTecFaultPortn_Object = MibTableColumn
pmo10010AlmLineLaneRxTecFaultPortn = _Pmo10010AlmLineLaneRxTecFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 136, 1, 3),
    _Pmo10010AlmLineLaneRxTecFaultPortn_Type()
)
pmo10010AlmLineLaneRxTecFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineLaneRxTecFaultPortn.setStatus("current")
_Pmo10010AlmLineLaneRxFifoErrorPortn_Type = EkiOnOff
_Pmo10010AlmLineLaneRxFifoErrorPortn_Object = MibTableColumn
pmo10010AlmLineLaneRxFifoErrorPortn = _Pmo10010AlmLineLaneRxFifoErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 136, 1, 4),
    _Pmo10010AlmLineLaneRxFifoErrorPortn_Type()
)
pmo10010AlmLineLaneRxFifoErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineLaneRxFifoErrorPortn.setStatus("current")
_Pmo10010AlmLineLaneRxLolPortn_Type = EkiOnOff
_Pmo10010AlmLineLaneRxLolPortn_Object = MibTableColumn
pmo10010AlmLineLaneRxLolPortn = _Pmo10010AlmLineLaneRxLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 136, 1, 5),
    _Pmo10010AlmLineLaneRxLolPortn_Type()
)
pmo10010AlmLineLaneRxLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineLaneRxLolPortn.setStatus("current")
_Pmo10010AlmLineLaneRxLosPortn_Type = EkiOnOff
_Pmo10010AlmLineLaneRxLosPortn_Object = MibTableColumn
pmo10010AlmLineLaneRxLosPortn = _Pmo10010AlmLineLaneRxLosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 136, 1, 6),
    _Pmo10010AlmLineLaneRxLosPortn_Type()
)
pmo10010AlmLineLaneRxLosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineLaneRxLosPortn.setStatus("current")
_Pmo10010AlmLineLaneTxLolPortn_Type = EkiOnOff
_Pmo10010AlmLineLaneTxLolPortn_Object = MibTableColumn
pmo10010AlmLineLaneTxLolPortn = _Pmo10010AlmLineLaneTxLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 136, 1, 8),
    _Pmo10010AlmLineLaneTxLolPortn_Type()
)
pmo10010AlmLineLaneTxLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineLaneTxLolPortn.setStatus("current")
_Pmo10010AlmLineLaneTxLosfPortn_Type = EkiOnOff
_Pmo10010AlmLineLaneTxLosfPortn_Object = MibTableColumn
pmo10010AlmLineLaneTxLosfPortn = _Pmo10010AlmLineLaneTxLosfPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 136, 1, 9),
    _Pmo10010AlmLineLaneTxLosfPortn_Type()
)
pmo10010AlmLineLaneTxLosfPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineLaneTxLosfPortn.setStatus("current")
_Pmo10010AlmLineLaneApdPowerSupplyPortn_Type = EkiOnOff
_Pmo10010AlmLineLaneApdPowerSupplyPortn_Object = MibTableColumn
pmo10010AlmLineLaneApdPowerSupplyPortn = _Pmo10010AlmLineLaneApdPowerSupplyPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 136, 1, 15),
    _Pmo10010AlmLineLaneApdPowerSupplyPortn_Type()
)
pmo10010AlmLineLaneApdPowerSupplyPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineLaneApdPowerSupplyPortn.setStatus("current")
_Pmo10010AlmLineLaneWavelengthUnlockedPortn_Type = EkiOnOff
_Pmo10010AlmLineLaneWavelengthUnlockedPortn_Object = MibTableColumn
pmo10010AlmLineLaneWavelengthUnlockedPortn = _Pmo10010AlmLineLaneWavelengthUnlockedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 136, 1, 16),
    _Pmo10010AlmLineLaneWavelengthUnlockedPortn_Type()
)
pmo10010AlmLineLaneWavelengthUnlockedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineLaneWavelengthUnlockedPortn.setStatus("current")
_Pmo10010AlmLineLaneTecFaultPortn_Type = EkiOnOff
_Pmo10010AlmLineLaneTecFaultPortn_Object = MibTableColumn
pmo10010AlmLineLaneTecFaultPortn = _Pmo10010AlmLineLaneTecFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 136, 1, 17),
    _Pmo10010AlmLineLaneTecFaultPortn_Type()
)
pmo10010AlmLineLaneTecFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineLaneTecFaultPortn.setStatus("current")
_Pmo10010AlmlineOtu4AlarmTable_Object = MibTable
pmo10010AlmlineOtu4AlarmTable = _Pmo10010AlmlineOtu4AlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 152)
)
if mibBuilder.loadTexts:
    pmo10010AlmlineOtu4AlarmTable.setStatus("current")
_Pmo10010AlmlineOtu4AlarmEntry_Object = MibTableRow
pmo10010AlmlineOtu4AlarmEntry = _Pmo10010AlmlineOtu4AlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 152, 1)
)
pmo10010AlmlineOtu4AlarmEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010AlmlineOtu4AlarmIndex"),
)
if mibBuilder.loadTexts:
    pmo10010AlmlineOtu4AlarmEntry.setStatus("current")


class _Pmo10010AlmlineOtu4AlarmIndex_Type(Integer32):
    """Custom type pmo10010AlmlineOtu4AlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010AlmlineOtu4AlarmIndex_Type.__name__ = "Integer32"
_Pmo10010AlmlineOtu4AlarmIndex_Object = MibTableColumn
pmo10010AlmlineOtu4AlarmIndex = _Pmo10010AlmlineOtu4AlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 152, 1, 1),
    _Pmo10010AlmlineOtu4AlarmIndex_Type()
)
pmo10010AlmlineOtu4AlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmlineOtu4AlarmIndex.setStatus("current")
_Pmo10010AlmLineInputLossOfSignalPortn_Type = EkiOnOff
_Pmo10010AlmLineInputLossOfSignalPortn_Object = MibTableColumn
pmo10010AlmLineInputLossOfSignalPortn = _Pmo10010AlmLineInputLossOfSignalPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 152, 1, 2),
    _Pmo10010AlmLineInputLossOfSignalPortn_Type()
)
pmo10010AlmLineInputLossOfSignalPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineInputLossOfSignalPortn.setStatus("current")
_Pmo10010AlmLineLossOfFramePortn_Type = EkiOnOff
_Pmo10010AlmLineLossOfFramePortn_Object = MibTableColumn
pmo10010AlmLineLossOfFramePortn = _Pmo10010AlmLineLossOfFramePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 152, 1, 3),
    _Pmo10010AlmLineLossOfFramePortn_Type()
)
pmo10010AlmLineLossOfFramePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineLossOfFramePortn.setStatus("current")
_Pmo10010AlmLineSmBdiInsertedPortn_Type = EkiOnOff
_Pmo10010AlmLineSmBdiInsertedPortn_Object = MibTableColumn
pmo10010AlmLineSmBdiInsertedPortn = _Pmo10010AlmLineSmBdiInsertedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 152, 1, 4),
    _Pmo10010AlmLineSmBdiInsertedPortn_Type()
)
pmo10010AlmLineSmBdiInsertedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineSmBdiInsertedPortn.setStatus("current")
_Pmo10010AlmLineSmBdiDetectedPortn_Type = EkiOnOff
_Pmo10010AlmLineSmBdiDetectedPortn_Object = MibTableColumn
pmo10010AlmLineSmBdiDetectedPortn = _Pmo10010AlmLineSmBdiDetectedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 152, 1, 5),
    _Pmo10010AlmLineSmBdiDetectedPortn_Type()
)
pmo10010AlmLineSmBdiDetectedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineSmBdiDetectedPortn.setStatus("current")
_Pmo10010AlmLineSmIaeInsertedPortn_Type = EkiOnOff
_Pmo10010AlmLineSmIaeInsertedPortn_Object = MibTableColumn
pmo10010AlmLineSmIaeInsertedPortn = _Pmo10010AlmLineSmIaeInsertedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 152, 1, 6),
    _Pmo10010AlmLineSmIaeInsertedPortn_Type()
)
pmo10010AlmLineSmIaeInsertedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineSmIaeInsertedPortn.setStatus("current")
_Pmo10010AlmLineSmIaeDetectedPortn_Type = EkiOnOff
_Pmo10010AlmLineSmIaeDetectedPortn_Object = MibTableColumn
pmo10010AlmLineSmIaeDetectedPortn = _Pmo10010AlmLineSmIaeDetectedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 152, 1, 7),
    _Pmo10010AlmLineSmIaeDetectedPortn_Type()
)
pmo10010AlmLineSmIaeDetectedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineSmIaeDetectedPortn.setStatus("current")
_Pmo10010AlmOtu4DdegPortn_Type = EkiOnOff
_Pmo10010AlmOtu4DdegPortn_Object = MibTableColumn
pmo10010AlmOtu4DdegPortn = _Pmo10010AlmOtu4DdegPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 152, 1, 8),
    _Pmo10010AlmOtu4DdegPortn_Type()
)
pmo10010AlmOtu4DdegPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmOtu4DdegPortn.setStatus("current")
_Pmo10010AlmClientOtu4DtimPortn_Type = EkiOnOff
_Pmo10010AlmClientOtu4DtimPortn_Object = MibTableColumn
pmo10010AlmClientOtu4DtimPortn = _Pmo10010AlmClientOtu4DtimPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 152, 1, 9),
    _Pmo10010AlmClientOtu4DtimPortn_Type()
)
pmo10010AlmClientOtu4DtimPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmClientOtu4DtimPortn.setStatus("current")
_Pmo10010AlmLineTxHostLolPortn_Type = EkiOnOff
_Pmo10010AlmLineTxHostLolPortn_Object = MibTableColumn
pmo10010AlmLineTxHostLolPortn = _Pmo10010AlmLineTxHostLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 152, 1, 10),
    _Pmo10010AlmLineTxHostLolPortn_Type()
)
pmo10010AlmLineTxHostLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineTxHostLolPortn.setStatus("current")
_Pmo10010AlmLineLaneTxFifoErrorPortn_Type = EkiOnOff
_Pmo10010AlmLineLaneTxFifoErrorPortn_Object = MibTableColumn
pmo10010AlmLineLaneTxFifoErrorPortn = _Pmo10010AlmLineLaneTxFifoErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 152, 1, 11),
    _Pmo10010AlmLineLaneTxFifoErrorPortn_Type()
)
pmo10010AlmLineLaneTxFifoErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineLaneTxFifoErrorPortn.setStatus("current")
_Pmo10010AlmLineOchr4DlosPPortn_Type = EkiOnOff
_Pmo10010AlmLineOchr4DlosPPortn_Object = MibTableColumn
pmo10010AlmLineOchr4DlosPPortn = _Pmo10010AlmLineOchr4DlosPPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 152, 1, 12),
    _Pmo10010AlmLineOchr4DlosPPortn_Type()
)
pmo10010AlmLineOchr4DlosPPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineOchr4DlosPPortn.setStatus("current")
_Pmo10010AlmLineOtu4DssfPortn_Type = EkiOnOff
_Pmo10010AlmLineOtu4DssfPortn_Object = MibTableColumn
pmo10010AlmLineOtu4DssfPortn = _Pmo10010AlmLineOtu4DssfPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 152, 1, 16),
    _Pmo10010AlmLineOtu4DssfPortn_Type()
)
pmo10010AlmLineOtu4DssfPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineOtu4DssfPortn.setStatus("current")
_Pmo10010AlmLineOtu4DlomPortn_Type = EkiOnOff
_Pmo10010AlmLineOtu4DlomPortn_Object = MibTableColumn
pmo10010AlmLineOtu4DlomPortn = _Pmo10010AlmLineOtu4DlomPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 152, 1, 17),
    _Pmo10010AlmLineOtu4DlomPortn_Type()
)
pmo10010AlmLineOtu4DlomPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineOtu4DlomPortn.setStatus("current")
_Pmo10010AlmlineNetworkLaneRxOtnTable_Object = MibTable
pmo10010AlmlineNetworkLaneRxOtnTable = _Pmo10010AlmlineNetworkLaneRxOtnTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 168)
)
if mibBuilder.loadTexts:
    pmo10010AlmlineNetworkLaneRxOtnTable.setStatus("current")
_Pmo10010AlmlineNetworkLaneRxOtnEntry_Object = MibTableRow
pmo10010AlmlineNetworkLaneRxOtnEntry = _Pmo10010AlmlineNetworkLaneRxOtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 168, 1)
)
pmo10010AlmlineNetworkLaneRxOtnEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010AlmlineNetworkLaneRxOtnIndex"),
)
if mibBuilder.loadTexts:
    pmo10010AlmlineNetworkLaneRxOtnEntry.setStatus("current")


class _Pmo10010AlmlineNetworkLaneRxOtnIndex_Type(Integer32):
    """Custom type pmo10010AlmlineNetworkLaneRxOtnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010AlmlineNetworkLaneRxOtnIndex_Type.__name__ = "Integer32"
_Pmo10010AlmlineNetworkLaneRxOtnIndex_Object = MibTableColumn
pmo10010AlmlineNetworkLaneRxOtnIndex = _Pmo10010AlmlineNetworkLaneRxOtnIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 168, 1, 1),
    _Pmo10010AlmlineNetworkLaneRxOtnIndex_Type()
)
pmo10010AlmlineNetworkLaneRxOtnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmlineNetworkLaneRxOtnIndex.setStatus("current")
_Pmo10010AlmLineRxOtnOduAisPortn_Type = EkiOnOff
_Pmo10010AlmLineRxOtnOduAisPortn_Object = MibTableColumn
pmo10010AlmLineRxOtnOduAisPortn = _Pmo10010AlmLineRxOtnOduAisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 168, 1, 10),
    _Pmo10010AlmLineRxOtnOduAisPortn_Type()
)
pmo10010AlmLineRxOtnOduAisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineRxOtnOduAisPortn.setStatus("current")
_Pmo10010AlmLineRxOtnOtuAisPortn_Type = EkiOnOff
_Pmo10010AlmLineRxOtnOtuAisPortn_Object = MibTableColumn
pmo10010AlmLineRxOtnOtuAisPortn = _Pmo10010AlmLineRxOtnOtuAisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 168, 1, 11),
    _Pmo10010AlmLineRxOtnOtuAisPortn_Type()
)
pmo10010AlmLineRxOtnOtuAisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineRxOtnOtuAisPortn.setStatus("current")
_Pmo10010AlmLineRxSmBdiPortn_Type = EkiOnOff
_Pmo10010AlmLineRxSmBdiPortn_Object = MibTableColumn
pmo10010AlmLineRxSmBdiPortn = _Pmo10010AlmLineRxSmBdiPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 168, 1, 12),
    _Pmo10010AlmLineRxSmBdiPortn_Type()
)
pmo10010AlmLineRxSmBdiPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineRxSmBdiPortn.setStatus("current")
_Pmo10010AlmLineRxOtnIaePortn_Type = EkiOnOff
_Pmo10010AlmLineRxOtnIaePortn_Object = MibTableColumn
pmo10010AlmLineRxOtnIaePortn = _Pmo10010AlmLineRxOtnIaePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 168, 1, 13),
    _Pmo10010AlmLineRxOtnIaePortn_Type()
)
pmo10010AlmLineRxOtnIaePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineRxOtnIaePortn.setStatus("current")
_Pmo10010AlmLineRxOtnOomPortn_Type = EkiOnOff
_Pmo10010AlmLineRxOtnOomPortn_Object = MibTableColumn
pmo10010AlmLineRxOtnOomPortn = _Pmo10010AlmLineRxOtnOomPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 168, 1, 14),
    _Pmo10010AlmLineRxOtnOomPortn_Type()
)
pmo10010AlmLineRxOtnOomPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineRxOtnOomPortn.setStatus("current")
_Pmo10010AlmLineRxOtnLomPortn_Type = EkiOnOff
_Pmo10010AlmLineRxOtnLomPortn_Object = MibTableColumn
pmo10010AlmLineRxOtnLomPortn = _Pmo10010AlmLineRxOtnLomPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 168, 1, 15),
    _Pmo10010AlmLineRxOtnLomPortn_Type()
)
pmo10010AlmLineRxOtnLomPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineRxOtnLomPortn.setStatus("current")
_Pmo10010AlmLineRxOtnOofPortn_Type = EkiOnOff
_Pmo10010AlmLineRxOtnOofPortn_Object = MibTableColumn
pmo10010AlmLineRxOtnOofPortn = _Pmo10010AlmLineRxOtnOofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 168, 1, 16),
    _Pmo10010AlmLineRxOtnOofPortn_Type()
)
pmo10010AlmLineRxOtnOofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineRxOtnOofPortn.setStatus("current")
_Pmo10010AlmLineRxOtnLofPortn_Type = EkiOnOff
_Pmo10010AlmLineRxOtnLofPortn_Object = MibTableColumn
pmo10010AlmLineRxOtnLofPortn = _Pmo10010AlmLineRxOtnLofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 168, 1, 17),
    _Pmo10010AlmLineRxOtnLofPortn_Type()
)
pmo10010AlmLineRxOtnLofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineRxOtnLofPortn.setStatus("current")
_Pmo10010AlmlineHostLaneTxOtnTable_Object = MibTable
pmo10010AlmlineHostLaneTxOtnTable = _Pmo10010AlmlineHostLaneTxOtnTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 184)
)
if mibBuilder.loadTexts:
    pmo10010AlmlineHostLaneTxOtnTable.setStatus("current")
_Pmo10010AlmlineHostLaneTxOtnEntry_Object = MibTableRow
pmo10010AlmlineHostLaneTxOtnEntry = _Pmo10010AlmlineHostLaneTxOtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 184, 1)
)
pmo10010AlmlineHostLaneTxOtnEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010AlmlineHostLaneTxOtnIndex"),
)
if mibBuilder.loadTexts:
    pmo10010AlmlineHostLaneTxOtnEntry.setStatus("current")


class _Pmo10010AlmlineHostLaneTxOtnIndex_Type(Integer32):
    """Custom type pmo10010AlmlineHostLaneTxOtnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010AlmlineHostLaneTxOtnIndex_Type.__name__ = "Integer32"
_Pmo10010AlmlineHostLaneTxOtnIndex_Object = MibTableColumn
pmo10010AlmlineHostLaneTxOtnIndex = _Pmo10010AlmlineHostLaneTxOtnIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 184, 1, 1),
    _Pmo10010AlmlineHostLaneTxOtnIndex_Type()
)
pmo10010AlmlineHostLaneTxOtnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmlineHostLaneTxOtnIndex.setStatus("current")
_Pmo10010AlmLineTxOtnOduAisPortn_Type = EkiOnOff
_Pmo10010AlmLineTxOtnOduAisPortn_Object = MibTableColumn
pmo10010AlmLineTxOtnOduAisPortn = _Pmo10010AlmLineTxOtnOduAisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 184, 1, 10),
    _Pmo10010AlmLineTxOtnOduAisPortn_Type()
)
pmo10010AlmLineTxOtnOduAisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineTxOtnOduAisPortn.setStatus("current")
_Pmo10010AlmLineTxOtnOtuAisPortn_Type = EkiOnOff
_Pmo10010AlmLineTxOtnOtuAisPortn_Object = MibTableColumn
pmo10010AlmLineTxOtnOtuAisPortn = _Pmo10010AlmLineTxOtnOtuAisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 184, 1, 11),
    _Pmo10010AlmLineTxOtnOtuAisPortn_Type()
)
pmo10010AlmLineTxOtnOtuAisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineTxOtnOtuAisPortn.setStatus("current")
_Pmo10010AlmLineTxSmBdiPortn_Type = EkiOnOff
_Pmo10010AlmLineTxSmBdiPortn_Object = MibTableColumn
pmo10010AlmLineTxSmBdiPortn = _Pmo10010AlmLineTxSmBdiPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 184, 1, 12),
    _Pmo10010AlmLineTxSmBdiPortn_Type()
)
pmo10010AlmLineTxSmBdiPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineTxSmBdiPortn.setStatus("current")
_Pmo10010AlmLineTxOtnIaePortn_Type = EkiOnOff
_Pmo10010AlmLineTxOtnIaePortn_Object = MibTableColumn
pmo10010AlmLineTxOtnIaePortn = _Pmo10010AlmLineTxOtnIaePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 184, 1, 13),
    _Pmo10010AlmLineTxOtnIaePortn_Type()
)
pmo10010AlmLineTxOtnIaePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineTxOtnIaePortn.setStatus("current")
_Pmo10010AlmLineTxOtnOomPortn_Type = EkiOnOff
_Pmo10010AlmLineTxOtnOomPortn_Object = MibTableColumn
pmo10010AlmLineTxOtnOomPortn = _Pmo10010AlmLineTxOtnOomPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 184, 1, 14),
    _Pmo10010AlmLineTxOtnOomPortn_Type()
)
pmo10010AlmLineTxOtnOomPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineTxOtnOomPortn.setStatus("current")
_Pmo10010AlmLineTxOtnLomPortn_Type = EkiOnOff
_Pmo10010AlmLineTxOtnLomPortn_Object = MibTableColumn
pmo10010AlmLineTxOtnLomPortn = _Pmo10010AlmLineTxOtnLomPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 184, 1, 15),
    _Pmo10010AlmLineTxOtnLomPortn_Type()
)
pmo10010AlmLineTxOtnLomPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineTxOtnLomPortn.setStatus("current")
_Pmo10010AlmLineTxOtnOofPortn_Type = EkiOnOff
_Pmo10010AlmLineTxOtnOofPortn_Object = MibTableColumn
pmo10010AlmLineTxOtnOofPortn = _Pmo10010AlmLineTxOtnOofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 184, 1, 16),
    _Pmo10010AlmLineTxOtnOofPortn_Type()
)
pmo10010AlmLineTxOtnOofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineTxOtnOofPortn.setStatus("current")
_Pmo10010AlmLineTxOtnLofPortn_Type = EkiOnOff
_Pmo10010AlmLineTxOtnLofPortn_Object = MibTableColumn
pmo10010AlmLineTxOtnLofPortn = _Pmo10010AlmLineTxOtnLofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 184, 1, 17),
    _Pmo10010AlmLineTxOtnLofPortn_Type()
)
pmo10010AlmLineTxOtnLofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineTxOtnLofPortn.setStatus("current")
_Pmo10010AlmlineOdu4AlmTable_Object = MibTable
pmo10010AlmlineOdu4AlmTable = _Pmo10010AlmlineOdu4AlmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 256)
)
if mibBuilder.loadTexts:
    pmo10010AlmlineOdu4AlmTable.setStatus("current")
_Pmo10010AlmlineOdu4AlmEntry_Object = MibTableRow
pmo10010AlmlineOdu4AlmEntry = _Pmo10010AlmlineOdu4AlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 256, 1)
)
pmo10010AlmlineOdu4AlmEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010AlmlineOdu4AlmIndex"),
)
if mibBuilder.loadTexts:
    pmo10010AlmlineOdu4AlmEntry.setStatus("current")


class _Pmo10010AlmlineOdu4AlmIndex_Type(Integer32):
    """Custom type pmo10010AlmlineOdu4AlmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010AlmlineOdu4AlmIndex_Type.__name__ = "Integer32"
_Pmo10010AlmlineOdu4AlmIndex_Object = MibTableColumn
pmo10010AlmlineOdu4AlmIndex = _Pmo10010AlmlineOdu4AlmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 256, 1, 1),
    _Pmo10010AlmlineOdu4AlmIndex_Type()
)
pmo10010AlmlineOdu4AlmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmlineOdu4AlmIndex.setStatus("current")
_Pmo10010AlmLineOdu4DplmPortn_Type = EkiOnOff
_Pmo10010AlmLineOdu4DplmPortn_Object = MibTableColumn
pmo10010AlmLineOdu4DplmPortn = _Pmo10010AlmLineOdu4DplmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 256, 1, 4),
    _Pmo10010AlmLineOdu4DplmPortn_Type()
)
pmo10010AlmLineOdu4DplmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineOdu4DplmPortn.setStatus("current")
_Pmo10010AlmLineOdu4DdegPortn_Type = EkiOnOff
_Pmo10010AlmLineOdu4DdegPortn_Object = MibTableColumn
pmo10010AlmLineOdu4DdegPortn = _Pmo10010AlmLineOdu4DdegPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 256, 1, 6),
    _Pmo10010AlmLineOdu4DdegPortn_Type()
)
pmo10010AlmLineOdu4DdegPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineOdu4DdegPortn.setStatus("current")
_Pmo10010AlmLineOdu4IaisPortn_Type = EkiOnOff
_Pmo10010AlmLineOdu4IaisPortn_Object = MibTableColumn
pmo10010AlmLineOdu4IaisPortn = _Pmo10010AlmLineOdu4IaisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 256, 1, 8),
    _Pmo10010AlmLineOdu4IaisPortn_Type()
)
pmo10010AlmLineOdu4IaisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineOdu4IaisPortn.setStatus("current")
_Pmo10010AlmLineOdu4DtimPortn_Type = EkiOnOff
_Pmo10010AlmLineOdu4DtimPortn_Object = MibTableColumn
pmo10010AlmLineOdu4DtimPortn = _Pmo10010AlmLineOdu4DtimPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 256, 1, 9),
    _Pmo10010AlmLineOdu4DtimPortn_Type()
)
pmo10010AlmLineOdu4DtimPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineOdu4DtimPortn.setStatus("current")
_Pmo10010AlmLineOdu4DaisPortn_Type = EkiOnOff
_Pmo10010AlmLineOdu4DaisPortn_Object = MibTableColumn
pmo10010AlmLineOdu4DaisPortn = _Pmo10010AlmLineOdu4DaisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 256, 1, 10),
    _Pmo10010AlmLineOdu4DaisPortn_Type()
)
pmo10010AlmLineOdu4DaisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineOdu4DaisPortn.setStatus("current")
_Pmo10010AlmLineOdu4IociPortn_Type = EkiOnOff
_Pmo10010AlmLineOdu4IociPortn_Object = MibTableColumn
pmo10010AlmLineOdu4IociPortn = _Pmo10010AlmLineOdu4IociPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 256, 1, 12),
    _Pmo10010AlmLineOdu4IociPortn_Type()
)
pmo10010AlmLineOdu4IociPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineOdu4IociPortn.setStatus("current")
_Pmo10010AlmLineOdu4DociPortn_Type = EkiOnOff
_Pmo10010AlmLineOdu4DociPortn_Object = MibTableColumn
pmo10010AlmLineOdu4DociPortn = _Pmo10010AlmLineOdu4DociPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 256, 1, 13),
    _Pmo10010AlmLineOdu4DociPortn_Type()
)
pmo10010AlmLineOdu4DociPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineOdu4DociPortn.setStatus("current")
_Pmo10010AlmLineOdu4IbdiPortn_Type = EkiOnOff
_Pmo10010AlmLineOdu4IbdiPortn_Object = MibTableColumn
pmo10010AlmLineOdu4IbdiPortn = _Pmo10010AlmLineOdu4IbdiPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 256, 1, 14),
    _Pmo10010AlmLineOdu4IbdiPortn_Type()
)
pmo10010AlmLineOdu4IbdiPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineOdu4IbdiPortn.setStatus("current")
_Pmo10010AlmLineOdu4DbdiPortn_Type = EkiOnOff
_Pmo10010AlmLineOdu4DbdiPortn_Object = MibTableColumn
pmo10010AlmLineOdu4DbdiPortn = _Pmo10010AlmLineOdu4DbdiPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 256, 1, 15),
    _Pmo10010AlmLineOdu4DbdiPortn_Type()
)
pmo10010AlmLineOdu4DbdiPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineOdu4DbdiPortn.setStatus("current")
_Pmo10010AlmLineOdu4IlckPortn_Type = EkiOnOff
_Pmo10010AlmLineOdu4IlckPortn_Object = MibTableColumn
pmo10010AlmLineOdu4IlckPortn = _Pmo10010AlmLineOdu4IlckPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 256, 1, 16),
    _Pmo10010AlmLineOdu4IlckPortn_Type()
)
pmo10010AlmLineOdu4IlckPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineOdu4IlckPortn.setStatus("current")
_Pmo10010AlmLineOdu4DlckPortn_Type = EkiOnOff
_Pmo10010AlmLineOdu4DlckPortn_Object = MibTableColumn
pmo10010AlmLineOdu4DlckPortn = _Pmo10010AlmLineOdu4DlckPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 2, 256, 1, 17),
    _Pmo10010AlmLineOdu4DlckPortn_Type()
)
pmo10010AlmLineOdu4DlckPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineOdu4DlckPortn.setStatus("current")
_Pmo10010AlmLineCrit_ObjectIdentity = ObjectIdentity
pmo10010AlmLineCrit = _Pmo10010AlmLineCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 3)
)
_Pmo10010AlmsynthAlmLineTable_Object = MibTable
pmo10010AlmsynthAlmLineTable = _Pmo10010AlmsynthAlmLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 3, 24)
)
if mibBuilder.loadTexts:
    pmo10010AlmsynthAlmLineTable.setStatus("current")
_Pmo10010AlmsynthAlmLineEntry_Object = MibTableRow
pmo10010AlmsynthAlmLineEntry = _Pmo10010AlmsynthAlmLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 3, 24, 1)
)
pmo10010AlmsynthAlmLineEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010AlmsynthAlmLineIndex"),
)
if mibBuilder.loadTexts:
    pmo10010AlmsynthAlmLineEntry.setStatus("current")


class _Pmo10010AlmsynthAlmLineIndex_Type(Integer32):
    """Custom type pmo10010AlmsynthAlmLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010AlmsynthAlmLineIndex_Type.__name__ = "Integer32"
_Pmo10010AlmsynthAlmLineIndex_Object = MibTableColumn
pmo10010AlmsynthAlmLineIndex = _Pmo10010AlmsynthAlmLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 3, 24, 1, 1),
    _Pmo10010AlmsynthAlmLineIndex_Type()
)
pmo10010AlmsynthAlmLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmsynthAlmLineIndex.setStatus("current")
_Pmo10010AlmXfpAbsentPortn_Type = EkiOnOff
_Pmo10010AlmXfpAbsentPortn_Object = MibTableColumn
pmo10010AlmXfpAbsentPortn = _Pmo10010AlmXfpAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 3, 24, 1, 2),
    _Pmo10010AlmXfpAbsentPortn_Type()
)
pmo10010AlmXfpAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmXfpAbsentPortn.setStatus("current")
_Pmo10010AlmXfpInitNotComplPortn_Type = EkiOnOff
_Pmo10010AlmXfpInitNotComplPortn_Object = MibTableColumn
pmo10010AlmXfpInitNotComplPortn = _Pmo10010AlmXfpInitNotComplPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 3, 24, 1, 3),
    _Pmo10010AlmXfpInitNotComplPortn_Type()
)
pmo10010AlmXfpInitNotComplPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmXfpInitNotComplPortn.setStatus("current")
_Pmo10010AlmLineHwFailPortn_Type = EkiOnOff
_Pmo10010AlmLineHwFailPortn_Object = MibTableColumn
pmo10010AlmLineHwFailPortn = _Pmo10010AlmLineHwFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 3, 24, 1, 5),
    _Pmo10010AlmLineHwFailPortn_Type()
)
pmo10010AlmLineHwFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineHwFailPortn.setStatus("current")
_Pmo10010AlmXfpTxOffPortn_Type = EkiOnOff
_Pmo10010AlmXfpTxOffPortn_Object = MibTableColumn
pmo10010AlmXfpTxOffPortn = _Pmo10010AlmXfpTxOffPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 3, 24, 1, 6),
    _Pmo10010AlmXfpTxOffPortn_Type()
)
pmo10010AlmXfpTxOffPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmXfpTxOffPortn.setStatus("current")
_Pmo10010AlmLineLocalOosPortn_Type = EkiOnOff
_Pmo10010AlmLineLocalOosPortn_Object = MibTableColumn
pmo10010AlmLineLocalOosPortn = _Pmo10010AlmLineLocalOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 3, 24, 1, 7),
    _Pmo10010AlmLineLocalOosPortn_Type()
)
pmo10010AlmLineLocalOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineLocalOosPortn.setStatus("current")
_Pmo10010AlmUpRdiInsPortn_Type = EkiOnOff
_Pmo10010AlmUpRdiInsPortn_Object = MibTableColumn
pmo10010AlmUpRdiInsPortn = _Pmo10010AlmUpRdiInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 3, 24, 1, 9),
    _Pmo10010AlmUpRdiInsPortn_Type()
)
pmo10010AlmUpRdiInsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmUpRdiInsPortn.setStatus("current")
_Pmo10010AlmLineDdmWarningPortn_Type = EkiOnOff
_Pmo10010AlmLineDdmWarningPortn_Object = MibTableColumn
pmo10010AlmLineDdmWarningPortn = _Pmo10010AlmLineDdmWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 3, 24, 1, 10),
    _Pmo10010AlmLineDdmWarningPortn_Type()
)
pmo10010AlmLineDdmWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineDdmWarningPortn.setStatus("current")
_Pmo10010AlmLineDdmAlmPortn_Type = EkiOnOff
_Pmo10010AlmLineDdmAlmPortn_Object = MibTableColumn
pmo10010AlmLineDdmAlmPortn = _Pmo10010AlmLineDdmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 3, 24, 1, 11),
    _Pmo10010AlmLineDdmAlmPortn_Type()
)
pmo10010AlmLineDdmAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineDdmAlmPortn.setStatus("current")
_Pmo10010AlmLineFailPortn_Type = EkiOnOff
_Pmo10010AlmLineFailPortn_Object = MibTableColumn
pmo10010AlmLineFailPortn = _Pmo10010AlmLineFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 3, 24, 1, 13),
    _Pmo10010AlmLineFailPortn_Type()
)
pmo10010AlmLineFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineFailPortn.setStatus("current")
_Pmo10010AlmLineActivePortn_Type = EkiOnOff
_Pmo10010AlmLineActivePortn_Object = MibTableColumn
pmo10010AlmLineActivePortn = _Pmo10010AlmLineActivePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 2, 3, 3, 24, 1, 17),
    _Pmo10010AlmLineActivePortn_Type()
)
pmo10010AlmLineActivePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010AlmLineActivePortn.setStatus("current")
_Pmo10010measures_ObjectIdentity = ObjectIdentity
pmo10010measures = _Pmo10010measures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3)
)
_Pmo10010MesrOther_ObjectIdentity = ObjectIdentity
pmo10010MesrOther = _Pmo10010MesrOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 1)
)
_Pmo10010Mesrsynth0_Type = EkiMeasureType
_Pmo10010Mesrsynth0_Object = MibScalar
pmo10010Mesrsynth0 = _Pmo10010Mesrsynth0_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 1, 0),
    _Pmo10010Mesrsynth0_Type()
)
pmo10010Mesrsynth0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010Mesrsynth0.setStatus("deprecated")
_Pmo10010Mesrsynth1_Type = EkiMeasureType
_Pmo10010Mesrsynth1_Object = MibScalar
pmo10010Mesrsynth1 = _Pmo10010Mesrsynth1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 1, 1),
    _Pmo10010Mesrsynth1_Type()
)
pmo10010Mesrsynth1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010Mesrsynth1.setStatus("deprecated")


class _Pmo10010MesrpmIntervalNumber_Type(Unsigned32):
    """Custom type pmo10010MesrpmIntervalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmo10010MesrpmIntervalNumber_Type.__name__ = "Unsigned32"
_Pmo10010MesrpmIntervalNumber_Object = MibScalar
pmo10010MesrpmIntervalNumber = _Pmo10010MesrpmIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 1, 7),
    _Pmo10010MesrpmIntervalNumber_Type()
)
pmo10010MesrpmIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrpmIntervalNumber.setStatus("current")


class _Pmo10010MesrlineNetTxLaserOutputPwrAverage_Type(Unsigned32):
    """Custom type pmo10010MesrlineNetTxLaserOutputPwrAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmo10010MesrlineNetTxLaserOutputPwrAverage_Type.__name__ = "Unsigned32"
_Pmo10010MesrlineNetTxLaserOutputPwrAverage_Object = MibScalar
pmo10010MesrlineNetTxLaserOutputPwrAverage = _Pmo10010MesrlineNetTxLaserOutputPwrAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 1, 180),
    _Pmo10010MesrlineNetTxLaserOutputPwrAverage_Type()
)
pmo10010MesrlineNetTxLaserOutputPwrAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrlineNetTxLaserOutputPwrAverage.setStatus("current")


class _Pmo10010MesrlineNetTxLaserTempAverage_Type(Unsigned32):
    """Custom type pmo10010MesrlineNetTxLaserTempAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmo10010MesrlineNetTxLaserTempAverage_Type.__name__ = "Unsigned32"
_Pmo10010MesrlineNetTxLaserTempAverage_Object = MibScalar
pmo10010MesrlineNetTxLaserTempAverage = _Pmo10010MesrlineNetTxLaserTempAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 1, 181),
    _Pmo10010MesrlineNetTxLaserTempAverage_Type()
)
pmo10010MesrlineNetTxLaserTempAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrlineNetTxLaserTempAverage.setStatus("current")


class _Pmo10010MesrlineNetTxBiasCurrentAverage_Type(Unsigned32):
    """Custom type pmo10010MesrlineNetTxBiasCurrentAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmo10010MesrlineNetTxBiasCurrentAverage_Type.__name__ = "Unsigned32"
_Pmo10010MesrlineNetTxBiasCurrentAverage_Object = MibScalar
pmo10010MesrlineNetTxBiasCurrentAverage = _Pmo10010MesrlineNetTxBiasCurrentAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 1, 182),
    _Pmo10010MesrlineNetTxBiasCurrentAverage_Type()
)
pmo10010MesrlineNetTxBiasCurrentAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrlineNetTxBiasCurrentAverage.setStatus("current")


class _Pmo10010MesrlineNetRxInputPwrAverage_Type(Unsigned32):
    """Custom type pmo10010MesrlineNetRxInputPwrAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmo10010MesrlineNetRxInputPwrAverage_Type.__name__ = "Unsigned32"
_Pmo10010MesrlineNetRxInputPwrAverage_Object = MibScalar
pmo10010MesrlineNetRxInputPwrAverage = _Pmo10010MesrlineNetRxInputPwrAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 1, 183),
    _Pmo10010MesrlineNetRxInputPwrAverage_Type()
)
pmo10010MesrlineNetRxInputPwrAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrlineNetRxInputPwrAverage.setStatus("current")


class _Pmo10010MesrlineResidualChromaticDispAverage_Type(Unsigned32):
    """Custom type pmo10010MesrlineResidualChromaticDispAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmo10010MesrlineResidualChromaticDispAverage_Type.__name__ = "Unsigned32"
_Pmo10010MesrlineResidualChromaticDispAverage_Object = MibScalar
pmo10010MesrlineResidualChromaticDispAverage = _Pmo10010MesrlineResidualChromaticDispAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 1, 184),
    _Pmo10010MesrlineResidualChromaticDispAverage_Type()
)
pmo10010MesrlineResidualChromaticDispAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrlineResidualChromaticDispAverage.setStatus("current")


class _Pmo10010MesrlineDiffGroupDelayAverage_Type(Unsigned32):
    """Custom type pmo10010MesrlineDiffGroupDelayAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmo10010MesrlineDiffGroupDelayAverage_Type.__name__ = "Unsigned32"
_Pmo10010MesrlineDiffGroupDelayAverage_Object = MibScalar
pmo10010MesrlineDiffGroupDelayAverage = _Pmo10010MesrlineDiffGroupDelayAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 1, 185),
    _Pmo10010MesrlineDiffGroupDelayAverage_Type()
)
pmo10010MesrlineDiffGroupDelayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrlineDiffGroupDelayAverage.setStatus("current")


class _Pmo10010MesrlineQFactorAverage_Type(Unsigned32):
    """Custom type pmo10010MesrlineQFactorAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmo10010MesrlineQFactorAverage_Type.__name__ = "Unsigned32"
_Pmo10010MesrlineQFactorAverage_Object = MibScalar
pmo10010MesrlineQFactorAverage = _Pmo10010MesrlineQFactorAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 1, 186),
    _Pmo10010MesrlineQFactorAverage_Type()
)
pmo10010MesrlineQFactorAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrlineQFactorAverage.setStatus("current")


class _Pmo10010MesrlineCarrierFreqOffsetAverage_Type(Unsigned32):
    """Custom type pmo10010MesrlineCarrierFreqOffsetAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmo10010MesrlineCarrierFreqOffsetAverage_Type.__name__ = "Unsigned32"
_Pmo10010MesrlineCarrierFreqOffsetAverage_Object = MibScalar
pmo10010MesrlineCarrierFreqOffsetAverage = _Pmo10010MesrlineCarrierFreqOffsetAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 1, 187),
    _Pmo10010MesrlineCarrierFreqOffsetAverage_Type()
)
pmo10010MesrlineCarrierFreqOffsetAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrlineCarrierFreqOffsetAverage.setStatus("current")


class _Pmo10010MesrlineOsnrAverage_Type(Unsigned32):
    """Custom type pmo10010MesrlineOsnrAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmo10010MesrlineOsnrAverage_Type.__name__ = "Unsigned32"
_Pmo10010MesrlineOsnrAverage_Object = MibScalar
pmo10010MesrlineOsnrAverage = _Pmo10010MesrlineOsnrAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 1, 188),
    _Pmo10010MesrlineOsnrAverage_Type()
)
pmo10010MesrlineOsnrAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrlineOsnrAverage.setStatus("current")


class _Pmo10010MesrclientNetTxTempMin_Type(Unsigned32):
    """Custom type pmo10010MesrclientNetTxTempMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmo10010MesrclientNetTxTempMin_Type.__name__ = "Unsigned32"
_Pmo10010MesrclientNetTxTempMin_Object = MibScalar
pmo10010MesrclientNetTxTempMin = _Pmo10010MesrclientNetTxTempMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 1, 192),
    _Pmo10010MesrclientNetTxTempMin_Type()
)
pmo10010MesrclientNetTxTempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrclientNetTxTempMin.setStatus("current")


class _Pmo10010MesrclientNetTxBiasMin_Type(Unsigned32):
    """Custom type pmo10010MesrclientNetTxBiasMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmo10010MesrclientNetTxBiasMin_Type.__name__ = "Unsigned32"
_Pmo10010MesrclientNetTxBiasMin_Object = MibScalar
pmo10010MesrclientNetTxBiasMin = _Pmo10010MesrclientNetTxBiasMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 1, 193),
    _Pmo10010MesrclientNetTxBiasMin_Type()
)
pmo10010MesrclientNetTxBiasMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrclientNetTxBiasMin.setStatus("current")


class _Pmo10010MesrclientNetTxPwrMin_Type(Unsigned32):
    """Custom type pmo10010MesrclientNetTxPwrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmo10010MesrclientNetTxPwrMin_Type.__name__ = "Unsigned32"
_Pmo10010MesrclientNetTxPwrMin_Object = MibScalar
pmo10010MesrclientNetTxPwrMin = _Pmo10010MesrclientNetTxPwrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 1, 194),
    _Pmo10010MesrclientNetTxPwrMin_Type()
)
pmo10010MesrclientNetTxPwrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrclientNetTxPwrMin.setStatus("current")


class _Pmo10010MesrclientNetRxPwrMin_Type(Unsigned32):
    """Custom type pmo10010MesrclientNetRxPwrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmo10010MesrclientNetRxPwrMin_Type.__name__ = "Unsigned32"
_Pmo10010MesrclientNetRxPwrMin_Object = MibScalar
pmo10010MesrclientNetRxPwrMin = _Pmo10010MesrclientNetRxPwrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 1, 195),
    _Pmo10010MesrclientNetRxPwrMin_Type()
)
pmo10010MesrclientNetRxPwrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrclientNetRxPwrMin.setStatus("current")


class _Pmo10010MesrlineNetTxLaserOutputPwrMin_Type(Unsigned32):
    """Custom type pmo10010MesrlineNetTxLaserOutputPwrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmo10010MesrlineNetTxLaserOutputPwrMin_Type.__name__ = "Unsigned32"
_Pmo10010MesrlineNetTxLaserOutputPwrMin_Object = MibScalar
pmo10010MesrlineNetTxLaserOutputPwrMin = _Pmo10010MesrlineNetTxLaserOutputPwrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 1, 196),
    _Pmo10010MesrlineNetTxLaserOutputPwrMin_Type()
)
pmo10010MesrlineNetTxLaserOutputPwrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrlineNetTxLaserOutputPwrMin.setStatus("current")


class _Pmo10010MesrlineNetTxLaserTempMin_Type(Unsigned32):
    """Custom type pmo10010MesrlineNetTxLaserTempMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmo10010MesrlineNetTxLaserTempMin_Type.__name__ = "Unsigned32"
_Pmo10010MesrlineNetTxLaserTempMin_Object = MibScalar
pmo10010MesrlineNetTxLaserTempMin = _Pmo10010MesrlineNetTxLaserTempMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 1, 197),
    _Pmo10010MesrlineNetTxLaserTempMin_Type()
)
pmo10010MesrlineNetTxLaserTempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrlineNetTxLaserTempMin.setStatus("current")


class _Pmo10010MesrlineNetTxBiasCurrentMin_Type(Unsigned32):
    """Custom type pmo10010MesrlineNetTxBiasCurrentMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmo10010MesrlineNetTxBiasCurrentMin_Type.__name__ = "Unsigned32"
_Pmo10010MesrlineNetTxBiasCurrentMin_Object = MibScalar
pmo10010MesrlineNetTxBiasCurrentMin = _Pmo10010MesrlineNetTxBiasCurrentMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 1, 198),
    _Pmo10010MesrlineNetTxBiasCurrentMin_Type()
)
pmo10010MesrlineNetTxBiasCurrentMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrlineNetTxBiasCurrentMin.setStatus("current")


class _Pmo10010MesrlineNetRxInputPwrMin_Type(Unsigned32):
    """Custom type pmo10010MesrlineNetRxInputPwrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmo10010MesrlineNetRxInputPwrMin_Type.__name__ = "Unsigned32"
_Pmo10010MesrlineNetRxInputPwrMin_Object = MibScalar
pmo10010MesrlineNetRxInputPwrMin = _Pmo10010MesrlineNetRxInputPwrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 1, 199),
    _Pmo10010MesrlineNetRxInputPwrMin_Type()
)
pmo10010MesrlineNetRxInputPwrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrlineNetRxInputPwrMin.setStatus("current")


class _Pmo10010MesrlineResidualChromaticDispMin_Type(Unsigned32):
    """Custom type pmo10010MesrlineResidualChromaticDispMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmo10010MesrlineResidualChromaticDispMin_Type.__name__ = "Unsigned32"
_Pmo10010MesrlineResidualChromaticDispMin_Object = MibScalar
pmo10010MesrlineResidualChromaticDispMin = _Pmo10010MesrlineResidualChromaticDispMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 1, 200),
    _Pmo10010MesrlineResidualChromaticDispMin_Type()
)
pmo10010MesrlineResidualChromaticDispMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrlineResidualChromaticDispMin.setStatus("current")


class _Pmo10010MesrlineDiffGroupDelayMin_Type(Unsigned32):
    """Custom type pmo10010MesrlineDiffGroupDelayMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmo10010MesrlineDiffGroupDelayMin_Type.__name__ = "Unsigned32"
_Pmo10010MesrlineDiffGroupDelayMin_Object = MibScalar
pmo10010MesrlineDiffGroupDelayMin = _Pmo10010MesrlineDiffGroupDelayMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 1, 201),
    _Pmo10010MesrlineDiffGroupDelayMin_Type()
)
pmo10010MesrlineDiffGroupDelayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrlineDiffGroupDelayMin.setStatus("current")


class _Pmo10010MesrlineQFactorMin_Type(Unsigned32):
    """Custom type pmo10010MesrlineQFactorMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmo10010MesrlineQFactorMin_Type.__name__ = "Unsigned32"
_Pmo10010MesrlineQFactorMin_Object = MibScalar
pmo10010MesrlineQFactorMin = _Pmo10010MesrlineQFactorMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 1, 202),
    _Pmo10010MesrlineQFactorMin_Type()
)
pmo10010MesrlineQFactorMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrlineQFactorMin.setStatus("current")


class _Pmo10010MesrlineCarrierFreqOffsetMin_Type(Unsigned32):
    """Custom type pmo10010MesrlineCarrierFreqOffsetMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmo10010MesrlineCarrierFreqOffsetMin_Type.__name__ = "Unsigned32"
_Pmo10010MesrlineCarrierFreqOffsetMin_Object = MibScalar
pmo10010MesrlineCarrierFreqOffsetMin = _Pmo10010MesrlineCarrierFreqOffsetMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 1, 203),
    _Pmo10010MesrlineCarrierFreqOffsetMin_Type()
)
pmo10010MesrlineCarrierFreqOffsetMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrlineCarrierFreqOffsetMin.setStatus("current")


class _Pmo10010MesrlineOsnrMin_Type(Unsigned32):
    """Custom type pmo10010MesrlineOsnrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmo10010MesrlineOsnrMin_Type.__name__ = "Unsigned32"
_Pmo10010MesrlineOsnrMin_Object = MibScalar
pmo10010MesrlineOsnrMin = _Pmo10010MesrlineOsnrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 1, 204),
    _Pmo10010MesrlineOsnrMin_Type()
)
pmo10010MesrlineOsnrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrlineOsnrMin.setStatus("current")


class _Pmo10010MesrclientNetTxTempMax_Type(Unsigned32):
    """Custom type pmo10010MesrclientNetTxTempMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmo10010MesrclientNetTxTempMax_Type.__name__ = "Unsigned32"
_Pmo10010MesrclientNetTxTempMax_Object = MibScalar
pmo10010MesrclientNetTxTempMax = _Pmo10010MesrclientNetTxTempMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 1, 208),
    _Pmo10010MesrclientNetTxTempMax_Type()
)
pmo10010MesrclientNetTxTempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrclientNetTxTempMax.setStatus("current")


class _Pmo10010MesrclientNetTxBiasMax_Type(Unsigned32):
    """Custom type pmo10010MesrclientNetTxBiasMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmo10010MesrclientNetTxBiasMax_Type.__name__ = "Unsigned32"
_Pmo10010MesrclientNetTxBiasMax_Object = MibScalar
pmo10010MesrclientNetTxBiasMax = _Pmo10010MesrclientNetTxBiasMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 1, 209),
    _Pmo10010MesrclientNetTxBiasMax_Type()
)
pmo10010MesrclientNetTxBiasMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrclientNetTxBiasMax.setStatus("current")


class _Pmo10010MesrclientNetTxPwrMax_Type(Unsigned32):
    """Custom type pmo10010MesrclientNetTxPwrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmo10010MesrclientNetTxPwrMax_Type.__name__ = "Unsigned32"
_Pmo10010MesrclientNetTxPwrMax_Object = MibScalar
pmo10010MesrclientNetTxPwrMax = _Pmo10010MesrclientNetTxPwrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 1, 210),
    _Pmo10010MesrclientNetTxPwrMax_Type()
)
pmo10010MesrclientNetTxPwrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrclientNetTxPwrMax.setStatus("current")


class _Pmo10010MesrclientNetRxPwrMax_Type(Unsigned32):
    """Custom type pmo10010MesrclientNetRxPwrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmo10010MesrclientNetRxPwrMax_Type.__name__ = "Unsigned32"
_Pmo10010MesrclientNetRxPwrMax_Object = MibScalar
pmo10010MesrclientNetRxPwrMax = _Pmo10010MesrclientNetRxPwrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 1, 211),
    _Pmo10010MesrclientNetRxPwrMax_Type()
)
pmo10010MesrclientNetRxPwrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrclientNetRxPwrMax.setStatus("current")


class _Pmo10010MesrlineNetTxLaserOutputPwrMax_Type(Unsigned32):
    """Custom type pmo10010MesrlineNetTxLaserOutputPwrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmo10010MesrlineNetTxLaserOutputPwrMax_Type.__name__ = "Unsigned32"
_Pmo10010MesrlineNetTxLaserOutputPwrMax_Object = MibScalar
pmo10010MesrlineNetTxLaserOutputPwrMax = _Pmo10010MesrlineNetTxLaserOutputPwrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 1, 212),
    _Pmo10010MesrlineNetTxLaserOutputPwrMax_Type()
)
pmo10010MesrlineNetTxLaserOutputPwrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrlineNetTxLaserOutputPwrMax.setStatus("current")


class _Pmo10010MesrlineNetTxLaserTempMax_Type(Unsigned32):
    """Custom type pmo10010MesrlineNetTxLaserTempMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmo10010MesrlineNetTxLaserTempMax_Type.__name__ = "Unsigned32"
_Pmo10010MesrlineNetTxLaserTempMax_Object = MibScalar
pmo10010MesrlineNetTxLaserTempMax = _Pmo10010MesrlineNetTxLaserTempMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 1, 213),
    _Pmo10010MesrlineNetTxLaserTempMax_Type()
)
pmo10010MesrlineNetTxLaserTempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrlineNetTxLaserTempMax.setStatus("current")


class _Pmo10010MesrlineNetTxBiasCurrentMax_Type(Unsigned32):
    """Custom type pmo10010MesrlineNetTxBiasCurrentMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmo10010MesrlineNetTxBiasCurrentMax_Type.__name__ = "Unsigned32"
_Pmo10010MesrlineNetTxBiasCurrentMax_Object = MibScalar
pmo10010MesrlineNetTxBiasCurrentMax = _Pmo10010MesrlineNetTxBiasCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 1, 214),
    _Pmo10010MesrlineNetTxBiasCurrentMax_Type()
)
pmo10010MesrlineNetTxBiasCurrentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrlineNetTxBiasCurrentMax.setStatus("current")


class _Pmo10010MesrlineNetRxInputPwrMax_Type(Unsigned32):
    """Custom type pmo10010MesrlineNetRxInputPwrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmo10010MesrlineNetRxInputPwrMax_Type.__name__ = "Unsigned32"
_Pmo10010MesrlineNetRxInputPwrMax_Object = MibScalar
pmo10010MesrlineNetRxInputPwrMax = _Pmo10010MesrlineNetRxInputPwrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 1, 215),
    _Pmo10010MesrlineNetRxInputPwrMax_Type()
)
pmo10010MesrlineNetRxInputPwrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrlineNetRxInputPwrMax.setStatus("current")


class _Pmo10010MesrlineResidualChromaticDispMax_Type(Unsigned32):
    """Custom type pmo10010MesrlineResidualChromaticDispMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmo10010MesrlineResidualChromaticDispMax_Type.__name__ = "Unsigned32"
_Pmo10010MesrlineResidualChromaticDispMax_Object = MibScalar
pmo10010MesrlineResidualChromaticDispMax = _Pmo10010MesrlineResidualChromaticDispMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 1, 216),
    _Pmo10010MesrlineResidualChromaticDispMax_Type()
)
pmo10010MesrlineResidualChromaticDispMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrlineResidualChromaticDispMax.setStatus("current")


class _Pmo10010MesrlineDiffGroupDelayMax_Type(Unsigned32):
    """Custom type pmo10010MesrlineDiffGroupDelayMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmo10010MesrlineDiffGroupDelayMax_Type.__name__ = "Unsigned32"
_Pmo10010MesrlineDiffGroupDelayMax_Object = MibScalar
pmo10010MesrlineDiffGroupDelayMax = _Pmo10010MesrlineDiffGroupDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 1, 217),
    _Pmo10010MesrlineDiffGroupDelayMax_Type()
)
pmo10010MesrlineDiffGroupDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrlineDiffGroupDelayMax.setStatus("current")


class _Pmo10010MesrlineQFactorMax_Type(Unsigned32):
    """Custom type pmo10010MesrlineQFactorMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmo10010MesrlineQFactorMax_Type.__name__ = "Unsigned32"
_Pmo10010MesrlineQFactorMax_Object = MibScalar
pmo10010MesrlineQFactorMax = _Pmo10010MesrlineQFactorMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 1, 218),
    _Pmo10010MesrlineQFactorMax_Type()
)
pmo10010MesrlineQFactorMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrlineQFactorMax.setStatus("current")


class _Pmo10010MesrlineCarrierFreqOffsetMax_Type(Unsigned32):
    """Custom type pmo10010MesrlineCarrierFreqOffsetMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmo10010MesrlineCarrierFreqOffsetMax_Type.__name__ = "Unsigned32"
_Pmo10010MesrlineCarrierFreqOffsetMax_Object = MibScalar
pmo10010MesrlineCarrierFreqOffsetMax = _Pmo10010MesrlineCarrierFreqOffsetMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 1, 219),
    _Pmo10010MesrlineCarrierFreqOffsetMax_Type()
)
pmo10010MesrlineCarrierFreqOffsetMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrlineCarrierFreqOffsetMax.setStatus("current")


class _Pmo10010MesrlineOsnrMax_Type(Unsigned32):
    """Custom type pmo10010MesrlineOsnrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmo10010MesrlineOsnrMax_Type.__name__ = "Unsigned32"
_Pmo10010MesrlineOsnrMax_Object = MibScalar
pmo10010MesrlineOsnrMax = _Pmo10010MesrlineOsnrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 1, 220),
    _Pmo10010MesrlineOsnrMax_Type()
)
pmo10010MesrlineOsnrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrlineOsnrMax.setStatus("current")
_Pmo10010MesrClient_ObjectIdentity = ObjectIdentity
pmo10010MesrClient = _Pmo10010MesrClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 2)
)


class _Pmo10010MesrclientCfpTemp_Type(Unsigned32):
    """Custom type pmo10010MesrclientCfpTemp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmo10010MesrclientCfpTemp_Type.__name__ = "Unsigned32"
_Pmo10010MesrclientCfpTemp_Object = MibScalar
pmo10010MesrclientCfpTemp = _Pmo10010MesrclientCfpTemp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 2, 8),
    _Pmo10010MesrclientCfpTemp_Type()
)
pmo10010MesrclientCfpTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrclientCfpTemp.setStatus("current")


class _Pmo10010MesrclientCfp3v3Voltage_Type(Unsigned32):
    """Custom type pmo10010MesrclientCfp3v3Voltage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmo10010MesrclientCfp3v3Voltage_Type.__name__ = "Unsigned32"
_Pmo10010MesrclientCfp3v3Voltage_Object = MibScalar
pmo10010MesrclientCfp3v3Voltage = _Pmo10010MesrclientCfp3v3Voltage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 2, 9),
    _Pmo10010MesrclientCfp3v3Voltage_Type()
)
pmo10010MesrclientCfp3v3Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrclientCfp3v3Voltage.setStatus("current")


class _Pmo10010MesrclientSoaBiasCurrent_Type(Unsigned32):
    """Custom type pmo10010MesrclientSoaBiasCurrent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmo10010MesrclientSoaBiasCurrent_Type.__name__ = "Unsigned32"
_Pmo10010MesrclientSoaBiasCurrent_Object = MibScalar
pmo10010MesrclientSoaBiasCurrent = _Pmo10010MesrclientSoaBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 2, 10),
    _Pmo10010MesrclientSoaBiasCurrent_Type()
)
pmo10010MesrclientSoaBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrclientSoaBiasCurrent.setStatus("current")
_Pmo10010MesrclientNetTxTempTable_Object = MibTable
pmo10010MesrclientNetTxTempTable = _Pmo10010MesrclientNetTxTempTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 2, 16)
)
if mibBuilder.loadTexts:
    pmo10010MesrclientNetTxTempTable.setStatus("current")
_Pmo10010MesrclientNetTxTempEntry_Object = MibTableRow
pmo10010MesrclientNetTxTempEntry = _Pmo10010MesrclientNetTxTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 2, 16, 1)
)
pmo10010MesrclientNetTxTempEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010MesrclientNetTxTempIndex"),
)
if mibBuilder.loadTexts:
    pmo10010MesrclientNetTxTempEntry.setStatus("current")


class _Pmo10010MesrclientNetTxTempIndex_Type(Integer32):
    """Custom type pmo10010MesrclientNetTxTempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010MesrclientNetTxTempIndex_Type.__name__ = "Integer32"
_Pmo10010MesrclientNetTxTempIndex_Object = MibTableColumn
pmo10010MesrclientNetTxTempIndex = _Pmo10010MesrclientNetTxTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 2, 16, 1, 1),
    _Pmo10010MesrclientNetTxTempIndex_Type()
)
pmo10010MesrclientNetTxTempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrclientNetTxTempIndex.setStatus("current")


class _Pmo10010MesrclientNetTxTempPortn_Type(Integer32):
    """Custom type pmo10010MesrclientNetTxTempPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmo10010MesrclientNetTxTempPortn_Type.__name__ = "Integer32"
_Pmo10010MesrclientNetTxTempPortn_Object = MibTableColumn
pmo10010MesrclientNetTxTempPortn = _Pmo10010MesrclientNetTxTempPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 2, 16, 1, 2),
    _Pmo10010MesrclientNetTxTempPortn_Type()
)
pmo10010MesrclientNetTxTempPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrclientNetTxTempPortn.setStatus("current")
_Pmo10010MesrclientNetTxBiasTable_Object = MibTable
pmo10010MesrclientNetTxBiasTable = _Pmo10010MesrclientNetTxBiasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 2, 32)
)
if mibBuilder.loadTexts:
    pmo10010MesrclientNetTxBiasTable.setStatus("current")
_Pmo10010MesrclientNetTxBiasEntry_Object = MibTableRow
pmo10010MesrclientNetTxBiasEntry = _Pmo10010MesrclientNetTxBiasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 2, 32, 1)
)
pmo10010MesrclientNetTxBiasEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010MesrclientNetTxBiasIndex"),
)
if mibBuilder.loadTexts:
    pmo10010MesrclientNetTxBiasEntry.setStatus("current")


class _Pmo10010MesrclientNetTxBiasIndex_Type(Integer32):
    """Custom type pmo10010MesrclientNetTxBiasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010MesrclientNetTxBiasIndex_Type.__name__ = "Integer32"
_Pmo10010MesrclientNetTxBiasIndex_Object = MibTableColumn
pmo10010MesrclientNetTxBiasIndex = _Pmo10010MesrclientNetTxBiasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 2, 32, 1, 1),
    _Pmo10010MesrclientNetTxBiasIndex_Type()
)
pmo10010MesrclientNetTxBiasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrclientNetTxBiasIndex.setStatus("current")


class _Pmo10010MesrclientNetTxBiasPortn_Type(Integer32):
    """Custom type pmo10010MesrclientNetTxBiasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmo10010MesrclientNetTxBiasPortn_Type.__name__ = "Integer32"
_Pmo10010MesrclientNetTxBiasPortn_Object = MibTableColumn
pmo10010MesrclientNetTxBiasPortn = _Pmo10010MesrclientNetTxBiasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 2, 32, 1, 2),
    _Pmo10010MesrclientNetTxBiasPortn_Type()
)
pmo10010MesrclientNetTxBiasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrclientNetTxBiasPortn.setStatus("current")
_Pmo10010MesrclientNetTxPwrTable_Object = MibTable
pmo10010MesrclientNetTxPwrTable = _Pmo10010MesrclientNetTxPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 2, 48)
)
if mibBuilder.loadTexts:
    pmo10010MesrclientNetTxPwrTable.setStatus("current")
_Pmo10010MesrclientNetTxPwrEntry_Object = MibTableRow
pmo10010MesrclientNetTxPwrEntry = _Pmo10010MesrclientNetTxPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 2, 48, 1)
)
pmo10010MesrclientNetTxPwrEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010MesrclientNetTxPwrIndex"),
)
if mibBuilder.loadTexts:
    pmo10010MesrclientNetTxPwrEntry.setStatus("current")


class _Pmo10010MesrclientNetTxPwrIndex_Type(Integer32):
    """Custom type pmo10010MesrclientNetTxPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010MesrclientNetTxPwrIndex_Type.__name__ = "Integer32"
_Pmo10010MesrclientNetTxPwrIndex_Object = MibTableColumn
pmo10010MesrclientNetTxPwrIndex = _Pmo10010MesrclientNetTxPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 2, 48, 1, 1),
    _Pmo10010MesrclientNetTxPwrIndex_Type()
)
pmo10010MesrclientNetTxPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrclientNetTxPwrIndex.setStatus("current")


class _Pmo10010MesrclientNetTxPwrPortn_Type(Integer32):
    """Custom type pmo10010MesrclientNetTxPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmo10010MesrclientNetTxPwrPortn_Type.__name__ = "Integer32"
_Pmo10010MesrclientNetTxPwrPortn_Object = MibTableColumn
pmo10010MesrclientNetTxPwrPortn = _Pmo10010MesrclientNetTxPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 2, 48, 1, 2),
    _Pmo10010MesrclientNetTxPwrPortn_Type()
)
pmo10010MesrclientNetTxPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrclientNetTxPwrPortn.setStatus("current")
_Pmo10010MesrclientNetRxPwrTable_Object = MibTable
pmo10010MesrclientNetRxPwrTable = _Pmo10010MesrclientNetRxPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 2, 64)
)
if mibBuilder.loadTexts:
    pmo10010MesrclientNetRxPwrTable.setStatus("current")
_Pmo10010MesrclientNetRxPwrEntry_Object = MibTableRow
pmo10010MesrclientNetRxPwrEntry = _Pmo10010MesrclientNetRxPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 2, 64, 1)
)
pmo10010MesrclientNetRxPwrEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010MesrclientNetRxPwrIndex"),
)
if mibBuilder.loadTexts:
    pmo10010MesrclientNetRxPwrEntry.setStatus("current")


class _Pmo10010MesrclientNetRxPwrIndex_Type(Integer32):
    """Custom type pmo10010MesrclientNetRxPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010MesrclientNetRxPwrIndex_Type.__name__ = "Integer32"
_Pmo10010MesrclientNetRxPwrIndex_Object = MibTableColumn
pmo10010MesrclientNetRxPwrIndex = _Pmo10010MesrclientNetRxPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 2, 64, 1, 1),
    _Pmo10010MesrclientNetRxPwrIndex_Type()
)
pmo10010MesrclientNetRxPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrclientNetRxPwrIndex.setStatus("current")


class _Pmo10010MesrclientNetRxPwrPortn_Type(Integer32):
    """Custom type pmo10010MesrclientNetRxPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmo10010MesrclientNetRxPwrPortn_Type.__name__ = "Integer32"
_Pmo10010MesrclientNetRxPwrPortn_Object = MibTableColumn
pmo10010MesrclientNetRxPwrPortn = _Pmo10010MesrclientNetRxPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 2, 64, 1, 2),
    _Pmo10010MesrclientNetRxPwrPortn_Type()
)
pmo10010MesrclientNetRxPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrclientNetRxPwrPortn.setStatus("current")
_Pmo10010MesrLine_ObjectIdentity = ObjectIdentity
pmo10010MesrLine = _Pmo10010MesrLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 3)
)


class _Pmo10010MesrlineMsaTemp_Type(Unsigned32):
    """Custom type pmo10010MesrlineMsaTemp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmo10010MesrlineMsaTemp_Type.__name__ = "Unsigned32"
_Pmo10010MesrlineMsaTemp_Object = MibScalar
pmo10010MesrlineMsaTemp = _Pmo10010MesrlineMsaTemp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 3, 12),
    _Pmo10010MesrlineMsaTemp_Type()
)
pmo10010MesrlineMsaTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrlineMsaTemp.setStatus("current")


class _Pmo10010MesrlineMsa3v3Voltage_Type(Unsigned32):
    """Custom type pmo10010MesrlineMsa3v3Voltage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmo10010MesrlineMsa3v3Voltage_Type.__name__ = "Unsigned32"
_Pmo10010MesrlineMsa3v3Voltage_Object = MibScalar
pmo10010MesrlineMsa3v3Voltage = _Pmo10010MesrlineMsa3v3Voltage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 3, 13),
    _Pmo10010MesrlineMsa3v3Voltage_Type()
)
pmo10010MesrlineMsa3v3Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrlineMsa3v3Voltage.setStatus("current")


class _Pmo10010MesrlineSoaBiasCurrent_Type(Unsigned32):
    """Custom type pmo10010MesrlineSoaBiasCurrent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmo10010MesrlineSoaBiasCurrent_Type.__name__ = "Unsigned32"
_Pmo10010MesrlineSoaBiasCurrent_Object = MibScalar
pmo10010MesrlineSoaBiasCurrent = _Pmo10010MesrlineSoaBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 3, 14),
    _Pmo10010MesrlineSoaBiasCurrent_Type()
)
pmo10010MesrlineSoaBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrlineSoaBiasCurrent.setStatus("current")
_Pmo10010MesrlineNetTxLaserOutputPwrTable_Object = MibTable
pmo10010MesrlineNetTxLaserOutputPwrTable = _Pmo10010MesrlineNetTxLaserOutputPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 3, 80)
)
if mibBuilder.loadTexts:
    pmo10010MesrlineNetTxLaserOutputPwrTable.setStatus("current")
_Pmo10010MesrlineNetTxLaserOutputPwrEntry_Object = MibTableRow
pmo10010MesrlineNetTxLaserOutputPwrEntry = _Pmo10010MesrlineNetTxLaserOutputPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 3, 80, 1)
)
pmo10010MesrlineNetTxLaserOutputPwrEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010MesrlineNetTxLaserOutputPwrIndex"),
)
if mibBuilder.loadTexts:
    pmo10010MesrlineNetTxLaserOutputPwrEntry.setStatus("current")


class _Pmo10010MesrlineNetTxLaserOutputPwrIndex_Type(Integer32):
    """Custom type pmo10010MesrlineNetTxLaserOutputPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010MesrlineNetTxLaserOutputPwrIndex_Type.__name__ = "Integer32"
_Pmo10010MesrlineNetTxLaserOutputPwrIndex_Object = MibTableColumn
pmo10010MesrlineNetTxLaserOutputPwrIndex = _Pmo10010MesrlineNetTxLaserOutputPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 3, 80, 1, 1),
    _Pmo10010MesrlineNetTxLaserOutputPwrIndex_Type()
)
pmo10010MesrlineNetTxLaserOutputPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrlineNetTxLaserOutputPwrIndex.setStatus("current")


class _Pmo10010MesrlineNetTxLaserOutputPwrPortn_Type(Integer32):
    """Custom type pmo10010MesrlineNetTxLaserOutputPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmo10010MesrlineNetTxLaserOutputPwrPortn_Type.__name__ = "Integer32"
_Pmo10010MesrlineNetTxLaserOutputPwrPortn_Object = MibTableColumn
pmo10010MesrlineNetTxLaserOutputPwrPortn = _Pmo10010MesrlineNetTxLaserOutputPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 3, 80, 1, 2),
    _Pmo10010MesrlineNetTxLaserOutputPwrPortn_Type()
)
pmo10010MesrlineNetTxLaserOutputPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrlineNetTxLaserOutputPwrPortn.setStatus("current")
_Pmo10010MesrlineNetTxLaserTempTable_Object = MibTable
pmo10010MesrlineNetTxLaserTempTable = _Pmo10010MesrlineNetTxLaserTempTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 3, 96)
)
if mibBuilder.loadTexts:
    pmo10010MesrlineNetTxLaserTempTable.setStatus("current")
_Pmo10010MesrlineNetTxLaserTempEntry_Object = MibTableRow
pmo10010MesrlineNetTxLaserTempEntry = _Pmo10010MesrlineNetTxLaserTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 3, 96, 1)
)
pmo10010MesrlineNetTxLaserTempEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010MesrlineNetTxLaserTempIndex"),
)
if mibBuilder.loadTexts:
    pmo10010MesrlineNetTxLaserTempEntry.setStatus("current")


class _Pmo10010MesrlineNetTxLaserTempIndex_Type(Integer32):
    """Custom type pmo10010MesrlineNetTxLaserTempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010MesrlineNetTxLaserTempIndex_Type.__name__ = "Integer32"
_Pmo10010MesrlineNetTxLaserTempIndex_Object = MibTableColumn
pmo10010MesrlineNetTxLaserTempIndex = _Pmo10010MesrlineNetTxLaserTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 3, 96, 1, 1),
    _Pmo10010MesrlineNetTxLaserTempIndex_Type()
)
pmo10010MesrlineNetTxLaserTempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrlineNetTxLaserTempIndex.setStatus("current")


class _Pmo10010MesrlineNetTxLaserTempPortn_Type(Integer32):
    """Custom type pmo10010MesrlineNetTxLaserTempPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmo10010MesrlineNetTxLaserTempPortn_Type.__name__ = "Integer32"
_Pmo10010MesrlineNetTxLaserTempPortn_Object = MibTableColumn
pmo10010MesrlineNetTxLaserTempPortn = _Pmo10010MesrlineNetTxLaserTempPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 3, 96, 1, 2),
    _Pmo10010MesrlineNetTxLaserTempPortn_Type()
)
pmo10010MesrlineNetTxLaserTempPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrlineNetTxLaserTempPortn.setStatus("current")
_Pmo10010MesrlineNetTxBiasCurrentTable_Object = MibTable
pmo10010MesrlineNetTxBiasCurrentTable = _Pmo10010MesrlineNetTxBiasCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 3, 112)
)
if mibBuilder.loadTexts:
    pmo10010MesrlineNetTxBiasCurrentTable.setStatus("current")
_Pmo10010MesrlineNetTxBiasCurrentEntry_Object = MibTableRow
pmo10010MesrlineNetTxBiasCurrentEntry = _Pmo10010MesrlineNetTxBiasCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 3, 112, 1)
)
pmo10010MesrlineNetTxBiasCurrentEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010MesrlineNetTxBiasCurrentIndex"),
)
if mibBuilder.loadTexts:
    pmo10010MesrlineNetTxBiasCurrentEntry.setStatus("current")


class _Pmo10010MesrlineNetTxBiasCurrentIndex_Type(Integer32):
    """Custom type pmo10010MesrlineNetTxBiasCurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010MesrlineNetTxBiasCurrentIndex_Type.__name__ = "Integer32"
_Pmo10010MesrlineNetTxBiasCurrentIndex_Object = MibTableColumn
pmo10010MesrlineNetTxBiasCurrentIndex = _Pmo10010MesrlineNetTxBiasCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 3, 112, 1, 1),
    _Pmo10010MesrlineNetTxBiasCurrentIndex_Type()
)
pmo10010MesrlineNetTxBiasCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrlineNetTxBiasCurrentIndex.setStatus("current")


class _Pmo10010MesrlineNetTxBiasCurrentPortn_Type(Integer32):
    """Custom type pmo10010MesrlineNetTxBiasCurrentPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmo10010MesrlineNetTxBiasCurrentPortn_Type.__name__ = "Integer32"
_Pmo10010MesrlineNetTxBiasCurrentPortn_Object = MibTableColumn
pmo10010MesrlineNetTxBiasCurrentPortn = _Pmo10010MesrlineNetTxBiasCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 3, 112, 1, 2),
    _Pmo10010MesrlineNetTxBiasCurrentPortn_Type()
)
pmo10010MesrlineNetTxBiasCurrentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrlineNetTxBiasCurrentPortn.setStatus("current")
_Pmo10010MesrlineNetRxInputPwrTable_Object = MibTable
pmo10010MesrlineNetRxInputPwrTable = _Pmo10010MesrlineNetRxInputPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 3, 128)
)
if mibBuilder.loadTexts:
    pmo10010MesrlineNetRxInputPwrTable.setStatus("current")
_Pmo10010MesrlineNetRxInputPwrEntry_Object = MibTableRow
pmo10010MesrlineNetRxInputPwrEntry = _Pmo10010MesrlineNetRxInputPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 3, 128, 1)
)
pmo10010MesrlineNetRxInputPwrEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010MesrlineNetRxInputPwrIndex"),
)
if mibBuilder.loadTexts:
    pmo10010MesrlineNetRxInputPwrEntry.setStatus("current")


class _Pmo10010MesrlineNetRxInputPwrIndex_Type(Integer32):
    """Custom type pmo10010MesrlineNetRxInputPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010MesrlineNetRxInputPwrIndex_Type.__name__ = "Integer32"
_Pmo10010MesrlineNetRxInputPwrIndex_Object = MibTableColumn
pmo10010MesrlineNetRxInputPwrIndex = _Pmo10010MesrlineNetRxInputPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 3, 128, 1, 1),
    _Pmo10010MesrlineNetRxInputPwrIndex_Type()
)
pmo10010MesrlineNetRxInputPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrlineNetRxInputPwrIndex.setStatus("current")


class _Pmo10010MesrlineNetRxInputPwrPortn_Type(Integer32):
    """Custom type pmo10010MesrlineNetRxInputPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmo10010MesrlineNetRxInputPwrPortn_Type.__name__ = "Integer32"
_Pmo10010MesrlineNetRxInputPwrPortn_Object = MibTableColumn
pmo10010MesrlineNetRxInputPwrPortn = _Pmo10010MesrlineNetRxInputPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 3, 128, 1, 2),
    _Pmo10010MesrlineNetRxInputPwrPortn_Type()
)
pmo10010MesrlineNetRxInputPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrlineNetRxInputPwrPortn.setStatus("current")
_Pmo10010MesrlineResidualChromaticDispTable_Object = MibTable
pmo10010MesrlineResidualChromaticDispTable = _Pmo10010MesrlineResidualChromaticDispTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 3, 144)
)
if mibBuilder.loadTexts:
    pmo10010MesrlineResidualChromaticDispTable.setStatus("current")
_Pmo10010MesrlineResidualChromaticDispEntry_Object = MibTableRow
pmo10010MesrlineResidualChromaticDispEntry = _Pmo10010MesrlineResidualChromaticDispEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 3, 144, 1)
)
pmo10010MesrlineResidualChromaticDispEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010MesrlineResidualChromaticDispIndex"),
)
if mibBuilder.loadTexts:
    pmo10010MesrlineResidualChromaticDispEntry.setStatus("current")


class _Pmo10010MesrlineResidualChromaticDispIndex_Type(Integer32):
    """Custom type pmo10010MesrlineResidualChromaticDispIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010MesrlineResidualChromaticDispIndex_Type.__name__ = "Integer32"
_Pmo10010MesrlineResidualChromaticDispIndex_Object = MibTableColumn
pmo10010MesrlineResidualChromaticDispIndex = _Pmo10010MesrlineResidualChromaticDispIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 3, 144, 1, 1),
    _Pmo10010MesrlineResidualChromaticDispIndex_Type()
)
pmo10010MesrlineResidualChromaticDispIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrlineResidualChromaticDispIndex.setStatus("current")


class _Pmo10010MesrlineResidualChromaticDispPortn_Type(Integer32):
    """Custom type pmo10010MesrlineResidualChromaticDispPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmo10010MesrlineResidualChromaticDispPortn_Type.__name__ = "Integer32"
_Pmo10010MesrlineResidualChromaticDispPortn_Object = MibTableColumn
pmo10010MesrlineResidualChromaticDispPortn = _Pmo10010MesrlineResidualChromaticDispPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 3, 144, 1, 2),
    _Pmo10010MesrlineResidualChromaticDispPortn_Type()
)
pmo10010MesrlineResidualChromaticDispPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrlineResidualChromaticDispPortn.setStatus("current")
_Pmo10010MesrlineDiffGroupDelayTable_Object = MibTable
pmo10010MesrlineDiffGroupDelayTable = _Pmo10010MesrlineDiffGroupDelayTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 3, 148)
)
if mibBuilder.loadTexts:
    pmo10010MesrlineDiffGroupDelayTable.setStatus("current")
_Pmo10010MesrlineDiffGroupDelayEntry_Object = MibTableRow
pmo10010MesrlineDiffGroupDelayEntry = _Pmo10010MesrlineDiffGroupDelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 3, 148, 1)
)
pmo10010MesrlineDiffGroupDelayEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010MesrlineDiffGroupDelayIndex"),
)
if mibBuilder.loadTexts:
    pmo10010MesrlineDiffGroupDelayEntry.setStatus("current")


class _Pmo10010MesrlineDiffGroupDelayIndex_Type(Integer32):
    """Custom type pmo10010MesrlineDiffGroupDelayIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010MesrlineDiffGroupDelayIndex_Type.__name__ = "Integer32"
_Pmo10010MesrlineDiffGroupDelayIndex_Object = MibTableColumn
pmo10010MesrlineDiffGroupDelayIndex = _Pmo10010MesrlineDiffGroupDelayIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 3, 148, 1, 1),
    _Pmo10010MesrlineDiffGroupDelayIndex_Type()
)
pmo10010MesrlineDiffGroupDelayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrlineDiffGroupDelayIndex.setStatus("current")


class _Pmo10010MesrlineDiffGroupDelayPortn_Type(Integer32):
    """Custom type pmo10010MesrlineDiffGroupDelayPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmo10010MesrlineDiffGroupDelayPortn_Type.__name__ = "Integer32"
_Pmo10010MesrlineDiffGroupDelayPortn_Object = MibTableColumn
pmo10010MesrlineDiffGroupDelayPortn = _Pmo10010MesrlineDiffGroupDelayPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 3, 148, 1, 2),
    _Pmo10010MesrlineDiffGroupDelayPortn_Type()
)
pmo10010MesrlineDiffGroupDelayPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrlineDiffGroupDelayPortn.setStatus("current")
_Pmo10010MesrlineQFactorTable_Object = MibTable
pmo10010MesrlineQFactorTable = _Pmo10010MesrlineQFactorTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 3, 152)
)
if mibBuilder.loadTexts:
    pmo10010MesrlineQFactorTable.setStatus("current")
_Pmo10010MesrlineQFactorEntry_Object = MibTableRow
pmo10010MesrlineQFactorEntry = _Pmo10010MesrlineQFactorEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 3, 152, 1)
)
pmo10010MesrlineQFactorEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010MesrlineQFactorIndex"),
)
if mibBuilder.loadTexts:
    pmo10010MesrlineQFactorEntry.setStatus("current")


class _Pmo10010MesrlineQFactorIndex_Type(Integer32):
    """Custom type pmo10010MesrlineQFactorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010MesrlineQFactorIndex_Type.__name__ = "Integer32"
_Pmo10010MesrlineQFactorIndex_Object = MibTableColumn
pmo10010MesrlineQFactorIndex = _Pmo10010MesrlineQFactorIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 3, 152, 1, 1),
    _Pmo10010MesrlineQFactorIndex_Type()
)
pmo10010MesrlineQFactorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrlineQFactorIndex.setStatus("current")


class _Pmo10010MesrlineQFactorPortn_Type(Integer32):
    """Custom type pmo10010MesrlineQFactorPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmo10010MesrlineQFactorPortn_Type.__name__ = "Integer32"
_Pmo10010MesrlineQFactorPortn_Object = MibTableColumn
pmo10010MesrlineQFactorPortn = _Pmo10010MesrlineQFactorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 3, 152, 1, 2),
    _Pmo10010MesrlineQFactorPortn_Type()
)
pmo10010MesrlineQFactorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrlineQFactorPortn.setStatus("current")
_Pmo10010MesrlineCarrierFreqOffsetTable_Object = MibTable
pmo10010MesrlineCarrierFreqOffsetTable = _Pmo10010MesrlineCarrierFreqOffsetTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 3, 156)
)
if mibBuilder.loadTexts:
    pmo10010MesrlineCarrierFreqOffsetTable.setStatus("current")
_Pmo10010MesrlineCarrierFreqOffsetEntry_Object = MibTableRow
pmo10010MesrlineCarrierFreqOffsetEntry = _Pmo10010MesrlineCarrierFreqOffsetEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 3, 156, 1)
)
pmo10010MesrlineCarrierFreqOffsetEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010MesrlineCarrierFreqOffsetIndex"),
)
if mibBuilder.loadTexts:
    pmo10010MesrlineCarrierFreqOffsetEntry.setStatus("current")


class _Pmo10010MesrlineCarrierFreqOffsetIndex_Type(Integer32):
    """Custom type pmo10010MesrlineCarrierFreqOffsetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010MesrlineCarrierFreqOffsetIndex_Type.__name__ = "Integer32"
_Pmo10010MesrlineCarrierFreqOffsetIndex_Object = MibTableColumn
pmo10010MesrlineCarrierFreqOffsetIndex = _Pmo10010MesrlineCarrierFreqOffsetIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 3, 156, 1, 1),
    _Pmo10010MesrlineCarrierFreqOffsetIndex_Type()
)
pmo10010MesrlineCarrierFreqOffsetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrlineCarrierFreqOffsetIndex.setStatus("current")


class _Pmo10010MesrlineCarrierFreqOffsetPortn_Type(Integer32):
    """Custom type pmo10010MesrlineCarrierFreqOffsetPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmo10010MesrlineCarrierFreqOffsetPortn_Type.__name__ = "Integer32"
_Pmo10010MesrlineCarrierFreqOffsetPortn_Object = MibTableColumn
pmo10010MesrlineCarrierFreqOffsetPortn = _Pmo10010MesrlineCarrierFreqOffsetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 3, 156, 1, 2),
    _Pmo10010MesrlineCarrierFreqOffsetPortn_Type()
)
pmo10010MesrlineCarrierFreqOffsetPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrlineCarrierFreqOffsetPortn.setStatus("current")
_Pmo10010MesrlineOsnrTable_Object = MibTable
pmo10010MesrlineOsnrTable = _Pmo10010MesrlineOsnrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 3, 160)
)
if mibBuilder.loadTexts:
    pmo10010MesrlineOsnrTable.setStatus("current")
_Pmo10010MesrlineOsnrEntry_Object = MibTableRow
pmo10010MesrlineOsnrEntry = _Pmo10010MesrlineOsnrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 3, 160, 1)
)
pmo10010MesrlineOsnrEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010MesrlineOsnrIndex"),
)
if mibBuilder.loadTexts:
    pmo10010MesrlineOsnrEntry.setStatus("current")


class _Pmo10010MesrlineOsnrIndex_Type(Integer32):
    """Custom type pmo10010MesrlineOsnrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010MesrlineOsnrIndex_Type.__name__ = "Integer32"
_Pmo10010MesrlineOsnrIndex_Object = MibTableColumn
pmo10010MesrlineOsnrIndex = _Pmo10010MesrlineOsnrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 3, 160, 1, 1),
    _Pmo10010MesrlineOsnrIndex_Type()
)
pmo10010MesrlineOsnrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrlineOsnrIndex.setStatus("current")


class _Pmo10010MesrlineOsnrPortn_Type(Integer32):
    """Custom type pmo10010MesrlineOsnrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmo10010MesrlineOsnrPortn_Type.__name__ = "Integer32"
_Pmo10010MesrlineOsnrPortn_Object = MibTableColumn
pmo10010MesrlineOsnrPortn = _Pmo10010MesrlineOsnrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 3, 3, 160, 1, 2),
    _Pmo10010MesrlineOsnrPortn_Type()
)
pmo10010MesrlineOsnrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MesrlineOsnrPortn.setStatus("current")
_Pmo10010counters_ObjectIdentity = ObjectIdentity
pmo10010counters = _Pmo10010counters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4)
)
_Pmo10010CntOther_ObjectIdentity = ObjectIdentity
pmo10010CntOther = _Pmo10010CntOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 1)
)
_Pmo10010CntClient_ObjectIdentity = ObjectIdentity
pmo10010CntClient = _Pmo10010CntClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 2)
)
_Pmo10010CntclientInputErrorCounterLaneOneTable_Object = MibTable
pmo10010CntclientInputErrorCounterLaneOneTable = _Pmo10010CntclientInputErrorCounterLaneOneTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 2, 16)
)
if mibBuilder.loadTexts:
    pmo10010CntclientInputErrorCounterLaneOneTable.setStatus("current")
_Pmo10010CntclientInputErrorCounterLaneOneEntry_Object = MibTableRow
pmo10010CntclientInputErrorCounterLaneOneEntry = _Pmo10010CntclientInputErrorCounterLaneOneEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 2, 16, 1)
)
pmo10010CntclientInputErrorCounterLaneOneEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010CntclientInputErrorCounterLaneOneIndex"),
)
if mibBuilder.loadTexts:
    pmo10010CntclientInputErrorCounterLaneOneEntry.setStatus("current")


class _Pmo10010CntclientInputErrorCounterLaneOneIndex_Type(Integer32):
    """Custom type pmo10010CntclientInputErrorCounterLaneOneIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010CntclientInputErrorCounterLaneOneIndex_Type.__name__ = "Integer32"
_Pmo10010CntclientInputErrorCounterLaneOneIndex_Object = MibTableColumn
pmo10010CntclientInputErrorCounterLaneOneIndex = _Pmo10010CntclientInputErrorCounterLaneOneIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 2, 16, 1, 1),
    _Pmo10010CntclientInputErrorCounterLaneOneIndex_Type()
)
pmo10010CntclientInputErrorCounterLaneOneIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CntclientInputErrorCounterLaneOneIndex.setStatus("current")
_Pmo10010CntclientInputErrorCounterLaneOneValuePortn_Type = Counter32
_Pmo10010CntclientInputErrorCounterLaneOneValuePortn_Object = MibTableColumn
pmo10010CntclientInputErrorCounterLaneOneValuePortn = _Pmo10010CntclientInputErrorCounterLaneOneValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 2, 16, 1, 2),
    _Pmo10010CntclientInputErrorCounterLaneOneValuePortn_Type()
)
pmo10010CntclientInputErrorCounterLaneOneValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CntclientInputErrorCounterLaneOneValuePortn.setStatus("current")
_Pmo10010CntclientInputErrorCounterLaneOneErrorPortn_Type = EkiOnOff
_Pmo10010CntclientInputErrorCounterLaneOneErrorPortn_Object = MibTableColumn
pmo10010CntclientInputErrorCounterLaneOneErrorPortn = _Pmo10010CntclientInputErrorCounterLaneOneErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 2, 16, 1, 3),
    _Pmo10010CntclientInputErrorCounterLaneOneErrorPortn_Type()
)
pmo10010CntclientInputErrorCounterLaneOneErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CntclientInputErrorCounterLaneOneErrorPortn.setStatus("current")
_Pmo10010CntclientInputErrorCounterLaneOneOverloadPortn_Type = EkiOnOff
_Pmo10010CntclientInputErrorCounterLaneOneOverloadPortn_Object = MibTableColumn
pmo10010CntclientInputErrorCounterLaneOneOverloadPortn = _Pmo10010CntclientInputErrorCounterLaneOneOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 2, 16, 1, 4),
    _Pmo10010CntclientInputErrorCounterLaneOneOverloadPortn_Type()
)
pmo10010CntclientInputErrorCounterLaneOneOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CntclientInputErrorCounterLaneOneOverloadPortn.setStatus("current")
_Pmo10010CntclientInputErrorCounterLaneTwoTable_Object = MibTable
pmo10010CntclientInputErrorCounterLaneTwoTable = _Pmo10010CntclientInputErrorCounterLaneTwoTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 2, 32)
)
if mibBuilder.loadTexts:
    pmo10010CntclientInputErrorCounterLaneTwoTable.setStatus("current")
_Pmo10010CntclientInputErrorCounterLaneTwoEntry_Object = MibTableRow
pmo10010CntclientInputErrorCounterLaneTwoEntry = _Pmo10010CntclientInputErrorCounterLaneTwoEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 2, 32, 1)
)
pmo10010CntclientInputErrorCounterLaneTwoEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010CntclientInputErrorCounterLaneTwoIndex"),
)
if mibBuilder.loadTexts:
    pmo10010CntclientInputErrorCounterLaneTwoEntry.setStatus("current")


class _Pmo10010CntclientInputErrorCounterLaneTwoIndex_Type(Integer32):
    """Custom type pmo10010CntclientInputErrorCounterLaneTwoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010CntclientInputErrorCounterLaneTwoIndex_Type.__name__ = "Integer32"
_Pmo10010CntclientInputErrorCounterLaneTwoIndex_Object = MibTableColumn
pmo10010CntclientInputErrorCounterLaneTwoIndex = _Pmo10010CntclientInputErrorCounterLaneTwoIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 2, 32, 1, 1),
    _Pmo10010CntclientInputErrorCounterLaneTwoIndex_Type()
)
pmo10010CntclientInputErrorCounterLaneTwoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CntclientInputErrorCounterLaneTwoIndex.setStatus("current")
_Pmo10010CntclientInputErrorCounterLaneTwoValuePortn_Type = Counter32
_Pmo10010CntclientInputErrorCounterLaneTwoValuePortn_Object = MibTableColumn
pmo10010CntclientInputErrorCounterLaneTwoValuePortn = _Pmo10010CntclientInputErrorCounterLaneTwoValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 2, 32, 1, 2),
    _Pmo10010CntclientInputErrorCounterLaneTwoValuePortn_Type()
)
pmo10010CntclientInputErrorCounterLaneTwoValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CntclientInputErrorCounterLaneTwoValuePortn.setStatus("current")
_Pmo10010CntclientInputErrorCounterLaneTwoErrorPortn_Type = EkiOnOff
_Pmo10010CntclientInputErrorCounterLaneTwoErrorPortn_Object = MibTableColumn
pmo10010CntclientInputErrorCounterLaneTwoErrorPortn = _Pmo10010CntclientInputErrorCounterLaneTwoErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 2, 32, 1, 3),
    _Pmo10010CntclientInputErrorCounterLaneTwoErrorPortn_Type()
)
pmo10010CntclientInputErrorCounterLaneTwoErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CntclientInputErrorCounterLaneTwoErrorPortn.setStatus("current")
_Pmo10010CntclientInputErrorCounterLaneTwoOverloadPortn_Type = EkiOnOff
_Pmo10010CntclientInputErrorCounterLaneTwoOverloadPortn_Object = MibTableColumn
pmo10010CntclientInputErrorCounterLaneTwoOverloadPortn = _Pmo10010CntclientInputErrorCounterLaneTwoOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 2, 32, 1, 4),
    _Pmo10010CntclientInputErrorCounterLaneTwoOverloadPortn_Type()
)
pmo10010CntclientInputErrorCounterLaneTwoOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CntclientInputErrorCounterLaneTwoOverloadPortn.setStatus("current")
_Pmo10010CntclientInputErrorCounterTable_Object = MibTable
pmo10010CntclientInputErrorCounterTable = _Pmo10010CntclientInputErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 2, 80)
)
if mibBuilder.loadTexts:
    pmo10010CntclientInputErrorCounterTable.setStatus("current")
_Pmo10010CntclientInputErrorCounterEntry_Object = MibTableRow
pmo10010CntclientInputErrorCounterEntry = _Pmo10010CntclientInputErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 2, 80, 1)
)
pmo10010CntclientInputErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010CntclientInputErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    pmo10010CntclientInputErrorCounterEntry.setStatus("current")


class _Pmo10010CntclientInputErrorCounterIndex_Type(Integer32):
    """Custom type pmo10010CntclientInputErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010CntclientInputErrorCounterIndex_Type.__name__ = "Integer32"
_Pmo10010CntclientInputErrorCounterIndex_Object = MibTableColumn
pmo10010CntclientInputErrorCounterIndex = _Pmo10010CntclientInputErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 2, 80, 1, 1),
    _Pmo10010CntclientInputErrorCounterIndex_Type()
)
pmo10010CntclientInputErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CntclientInputErrorCounterIndex.setStatus("current")
_Pmo10010CntclientInputErrorCounterValuePortn_Type = Counter32
_Pmo10010CntclientInputErrorCounterValuePortn_Object = MibTableColumn
pmo10010CntclientInputErrorCounterValuePortn = _Pmo10010CntclientInputErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 2, 80, 1, 2),
    _Pmo10010CntclientInputErrorCounterValuePortn_Type()
)
pmo10010CntclientInputErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CntclientInputErrorCounterValuePortn.setStatus("current")
_Pmo10010CntclientInputErrorCounterErrorPortn_Type = EkiOnOff
_Pmo10010CntclientInputErrorCounterErrorPortn_Object = MibTableColumn
pmo10010CntclientInputErrorCounterErrorPortn = _Pmo10010CntclientInputErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 2, 80, 1, 3),
    _Pmo10010CntclientInputErrorCounterErrorPortn_Type()
)
pmo10010CntclientInputErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CntclientInputErrorCounterErrorPortn.setStatus("current")
_Pmo10010CntclientInputErrorCounterOverloadPortn_Type = EkiOnOff
_Pmo10010CntclientInputErrorCounterOverloadPortn_Object = MibTableColumn
pmo10010CntclientInputErrorCounterOverloadPortn = _Pmo10010CntclientInputErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 2, 80, 1, 4),
    _Pmo10010CntclientInputErrorCounterOverloadPortn_Type()
)
pmo10010CntclientInputErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CntclientInputErrorCounterOverloadPortn.setStatus("current")
_Pmo10010CntclientOutputErrorCounterTable_Object = MibTable
pmo10010CntclientOutputErrorCounterTable = _Pmo10010CntclientOutputErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 2, 96)
)
if mibBuilder.loadTexts:
    pmo10010CntclientOutputErrorCounterTable.setStatus("current")
_Pmo10010CntclientOutputErrorCounterEntry_Object = MibTableRow
pmo10010CntclientOutputErrorCounterEntry = _Pmo10010CntclientOutputErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 2, 96, 1)
)
pmo10010CntclientOutputErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010CntclientOutputErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    pmo10010CntclientOutputErrorCounterEntry.setStatus("current")


class _Pmo10010CntclientOutputErrorCounterIndex_Type(Integer32):
    """Custom type pmo10010CntclientOutputErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010CntclientOutputErrorCounterIndex_Type.__name__ = "Integer32"
_Pmo10010CntclientOutputErrorCounterIndex_Object = MibTableColumn
pmo10010CntclientOutputErrorCounterIndex = _Pmo10010CntclientOutputErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 2, 96, 1, 1),
    _Pmo10010CntclientOutputErrorCounterIndex_Type()
)
pmo10010CntclientOutputErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CntclientOutputErrorCounterIndex.setStatus("current")
_Pmo10010CntclientOutputErrorCounterValuePortn_Type = Counter32
_Pmo10010CntclientOutputErrorCounterValuePortn_Object = MibTableColumn
pmo10010CntclientOutputErrorCounterValuePortn = _Pmo10010CntclientOutputErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 2, 96, 1, 2),
    _Pmo10010CntclientOutputErrorCounterValuePortn_Type()
)
pmo10010CntclientOutputErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CntclientOutputErrorCounterValuePortn.setStatus("current")
_Pmo10010CntclientOutputErrorCounterErrorPortn_Type = EkiOnOff
_Pmo10010CntclientOutputErrorCounterErrorPortn_Object = MibTableColumn
pmo10010CntclientOutputErrorCounterErrorPortn = _Pmo10010CntclientOutputErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 2, 96, 1, 3),
    _Pmo10010CntclientOutputErrorCounterErrorPortn_Type()
)
pmo10010CntclientOutputErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CntclientOutputErrorCounterErrorPortn.setStatus("current")
_Pmo10010CntclientOutputErrorCounterOverloadPortn_Type = EkiOnOff
_Pmo10010CntclientOutputErrorCounterOverloadPortn_Object = MibTableColumn
pmo10010CntclientOutputErrorCounterOverloadPortn = _Pmo10010CntclientOutputErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 2, 96, 1, 4),
    _Pmo10010CntclientOutputErrorCounterOverloadPortn_Type()
)
pmo10010CntclientOutputErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CntclientOutputErrorCounterOverloadPortn.setStatus("current")
_Pmo10010CntLine_ObjectIdentity = ObjectIdentity
pmo10010CntLine = _Pmo10010CntLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 3)
)
_Pmo10010CntlocalLineSmBlockErrorCounterTable_Object = MibTable
pmo10010CntlocalLineSmBlockErrorCounterTable = _Pmo10010CntlocalLineSmBlockErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 3, 192)
)
if mibBuilder.loadTexts:
    pmo10010CntlocalLineSmBlockErrorCounterTable.setStatus("current")
_Pmo10010CntlocalLineSmBlockErrorCounterEntry_Object = MibTableRow
pmo10010CntlocalLineSmBlockErrorCounterEntry = _Pmo10010CntlocalLineSmBlockErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 3, 192, 1)
)
pmo10010CntlocalLineSmBlockErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010CntlocalLineSmBlockErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    pmo10010CntlocalLineSmBlockErrorCounterEntry.setStatus("current")


class _Pmo10010CntlocalLineSmBlockErrorCounterIndex_Type(Integer32):
    """Custom type pmo10010CntlocalLineSmBlockErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010CntlocalLineSmBlockErrorCounterIndex_Type.__name__ = "Integer32"
_Pmo10010CntlocalLineSmBlockErrorCounterIndex_Object = MibTableColumn
pmo10010CntlocalLineSmBlockErrorCounterIndex = _Pmo10010CntlocalLineSmBlockErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 3, 192, 1, 1),
    _Pmo10010CntlocalLineSmBlockErrorCounterIndex_Type()
)
pmo10010CntlocalLineSmBlockErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CntlocalLineSmBlockErrorCounterIndex.setStatus("current")
_Pmo10010CntlocalLineSmBlockErrorCounterValuePortn_Type = Counter64
_Pmo10010CntlocalLineSmBlockErrorCounterValuePortn_Object = MibTableColumn
pmo10010CntlocalLineSmBlockErrorCounterValuePortn = _Pmo10010CntlocalLineSmBlockErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 3, 192, 1, 2),
    _Pmo10010CntlocalLineSmBlockErrorCounterValuePortn_Type()
)
pmo10010CntlocalLineSmBlockErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CntlocalLineSmBlockErrorCounterValuePortn.setStatus("current")
_Pmo10010CntlocalLineSmBlockErrorCounterErrorPortn_Type = EkiOnOff
_Pmo10010CntlocalLineSmBlockErrorCounterErrorPortn_Object = MibTableColumn
pmo10010CntlocalLineSmBlockErrorCounterErrorPortn = _Pmo10010CntlocalLineSmBlockErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 3, 192, 1, 3),
    _Pmo10010CntlocalLineSmBlockErrorCounterErrorPortn_Type()
)
pmo10010CntlocalLineSmBlockErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CntlocalLineSmBlockErrorCounterErrorPortn.setStatus("current")
_Pmo10010CntlocalLineSmBlockErrorCounterOverloadPortn_Type = EkiOnOff
_Pmo10010CntlocalLineSmBlockErrorCounterOverloadPortn_Object = MibTableColumn
pmo10010CntlocalLineSmBlockErrorCounterOverloadPortn = _Pmo10010CntlocalLineSmBlockErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 3, 192, 1, 4),
    _Pmo10010CntlocalLineSmBlockErrorCounterOverloadPortn_Type()
)
pmo10010CntlocalLineSmBlockErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CntlocalLineSmBlockErrorCounterOverloadPortn.setStatus("current")
_Pmo10010CntlocalLineFecCorrectedErrorsCounterTable_Object = MibTable
pmo10010CntlocalLineFecCorrectedErrorsCounterTable = _Pmo10010CntlocalLineFecCorrectedErrorsCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 3, 193)
)
if mibBuilder.loadTexts:
    pmo10010CntlocalLineFecCorrectedErrorsCounterTable.setStatus("current")
_Pmo10010CntlocalLineFecCorrectedErrorsCounterEntry_Object = MibTableRow
pmo10010CntlocalLineFecCorrectedErrorsCounterEntry = _Pmo10010CntlocalLineFecCorrectedErrorsCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 3, 193, 1)
)
pmo10010CntlocalLineFecCorrectedErrorsCounterEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010CntlocalLineFecCorrectedErrorsCounterIndex"),
)
if mibBuilder.loadTexts:
    pmo10010CntlocalLineFecCorrectedErrorsCounterEntry.setStatus("current")


class _Pmo10010CntlocalLineFecCorrectedErrorsCounterIndex_Type(Integer32):
    """Custom type pmo10010CntlocalLineFecCorrectedErrorsCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010CntlocalLineFecCorrectedErrorsCounterIndex_Type.__name__ = "Integer32"
_Pmo10010CntlocalLineFecCorrectedErrorsCounterIndex_Object = MibTableColumn
pmo10010CntlocalLineFecCorrectedErrorsCounterIndex = _Pmo10010CntlocalLineFecCorrectedErrorsCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 3, 193, 1, 1),
    _Pmo10010CntlocalLineFecCorrectedErrorsCounterIndex_Type()
)
pmo10010CntlocalLineFecCorrectedErrorsCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CntlocalLineFecCorrectedErrorsCounterIndex.setStatus("current")
_Pmo10010CntlocalLineFecCorrectedErrorsCounterValuePortn_Type = Counter64
_Pmo10010CntlocalLineFecCorrectedErrorsCounterValuePortn_Object = MibTableColumn
pmo10010CntlocalLineFecCorrectedErrorsCounterValuePortn = _Pmo10010CntlocalLineFecCorrectedErrorsCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 3, 193, 1, 2),
    _Pmo10010CntlocalLineFecCorrectedErrorsCounterValuePortn_Type()
)
pmo10010CntlocalLineFecCorrectedErrorsCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CntlocalLineFecCorrectedErrorsCounterValuePortn.setStatus("current")
_Pmo10010CntlocalLineFecCorrectedErrorsCounterErrorPortn_Type = EkiOnOff
_Pmo10010CntlocalLineFecCorrectedErrorsCounterErrorPortn_Object = MibTableColumn
pmo10010CntlocalLineFecCorrectedErrorsCounterErrorPortn = _Pmo10010CntlocalLineFecCorrectedErrorsCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 3, 193, 1, 3),
    _Pmo10010CntlocalLineFecCorrectedErrorsCounterErrorPortn_Type()
)
pmo10010CntlocalLineFecCorrectedErrorsCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CntlocalLineFecCorrectedErrorsCounterErrorPortn.setStatus("current")
_Pmo10010CntlocalLineFecCorrectedErrorsCounterOverloadPortn_Type = EkiOnOff
_Pmo10010CntlocalLineFecCorrectedErrorsCounterOverloadPortn_Object = MibTableColumn
pmo10010CntlocalLineFecCorrectedErrorsCounterOverloadPortn = _Pmo10010CntlocalLineFecCorrectedErrorsCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 3, 193, 1, 4),
    _Pmo10010CntlocalLineFecCorrectedErrorsCounterOverloadPortn_Type()
)
pmo10010CntlocalLineFecCorrectedErrorsCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CntlocalLineFecCorrectedErrorsCounterOverloadPortn.setStatus("current")
_Pmo10010CntremoteLineSmBlockErrorCounterTable_Object = MibTable
pmo10010CntremoteLineSmBlockErrorCounterTable = _Pmo10010CntremoteLineSmBlockErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 3, 194)
)
if mibBuilder.loadTexts:
    pmo10010CntremoteLineSmBlockErrorCounterTable.setStatus("current")
_Pmo10010CntremoteLineSmBlockErrorCounterEntry_Object = MibTableRow
pmo10010CntremoteLineSmBlockErrorCounterEntry = _Pmo10010CntremoteLineSmBlockErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 3, 194, 1)
)
pmo10010CntremoteLineSmBlockErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010CntremoteLineSmBlockErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    pmo10010CntremoteLineSmBlockErrorCounterEntry.setStatus("current")


class _Pmo10010CntremoteLineSmBlockErrorCounterIndex_Type(Integer32):
    """Custom type pmo10010CntremoteLineSmBlockErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010CntremoteLineSmBlockErrorCounterIndex_Type.__name__ = "Integer32"
_Pmo10010CntremoteLineSmBlockErrorCounterIndex_Object = MibTableColumn
pmo10010CntremoteLineSmBlockErrorCounterIndex = _Pmo10010CntremoteLineSmBlockErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 3, 194, 1, 1),
    _Pmo10010CntremoteLineSmBlockErrorCounterIndex_Type()
)
pmo10010CntremoteLineSmBlockErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CntremoteLineSmBlockErrorCounterIndex.setStatus("current")
_Pmo10010CntremoteLineSmBlockErrorCounterValuePortn_Type = Counter64
_Pmo10010CntremoteLineSmBlockErrorCounterValuePortn_Object = MibTableColumn
pmo10010CntremoteLineSmBlockErrorCounterValuePortn = _Pmo10010CntremoteLineSmBlockErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 3, 194, 1, 2),
    _Pmo10010CntremoteLineSmBlockErrorCounterValuePortn_Type()
)
pmo10010CntremoteLineSmBlockErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CntremoteLineSmBlockErrorCounterValuePortn.setStatus("current")
_Pmo10010CntremoteLineSmBlockErrorCounterErrorPortn_Type = EkiOnOff
_Pmo10010CntremoteLineSmBlockErrorCounterErrorPortn_Object = MibTableColumn
pmo10010CntremoteLineSmBlockErrorCounterErrorPortn = _Pmo10010CntremoteLineSmBlockErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 3, 194, 1, 3),
    _Pmo10010CntremoteLineSmBlockErrorCounterErrorPortn_Type()
)
pmo10010CntremoteLineSmBlockErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CntremoteLineSmBlockErrorCounterErrorPortn.setStatus("current")
_Pmo10010CntremoteLineSmBlockErrorCounterOverloadPortn_Type = EkiOnOff
_Pmo10010CntremoteLineSmBlockErrorCounterOverloadPortn_Object = MibTableColumn
pmo10010CntremoteLineSmBlockErrorCounterOverloadPortn = _Pmo10010CntremoteLineSmBlockErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 3, 194, 1, 4),
    _Pmo10010CntremoteLineSmBlockErrorCounterOverloadPortn_Type()
)
pmo10010CntremoteLineSmBlockErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CntremoteLineSmBlockErrorCounterOverloadPortn.setStatus("current")
_Pmo10010CntlineDfrmTimCntTable_Object = MibTable
pmo10010CntlineDfrmTimCntTable = _Pmo10010CntlineDfrmTimCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 3, 195)
)
if mibBuilder.loadTexts:
    pmo10010CntlineDfrmTimCntTable.setStatus("current")
_Pmo10010CntlineDfrmTimCntEntry_Object = MibTableRow
pmo10010CntlineDfrmTimCntEntry = _Pmo10010CntlineDfrmTimCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 3, 195, 1)
)
pmo10010CntlineDfrmTimCntEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010CntlineDfrmTimCntIndex"),
)
if mibBuilder.loadTexts:
    pmo10010CntlineDfrmTimCntEntry.setStatus("current")


class _Pmo10010CntlineDfrmTimCntIndex_Type(Integer32):
    """Custom type pmo10010CntlineDfrmTimCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010CntlineDfrmTimCntIndex_Type.__name__ = "Integer32"
_Pmo10010CntlineDfrmTimCntIndex_Object = MibTableColumn
pmo10010CntlineDfrmTimCntIndex = _Pmo10010CntlineDfrmTimCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 3, 195, 1, 1),
    _Pmo10010CntlineDfrmTimCntIndex_Type()
)
pmo10010CntlineDfrmTimCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CntlineDfrmTimCntIndex.setStatus("current")
_Pmo10010CntlineDfrmTimCntValuePortn_Type = Counter64
_Pmo10010CntlineDfrmTimCntValuePortn_Object = MibTableColumn
pmo10010CntlineDfrmTimCntValuePortn = _Pmo10010CntlineDfrmTimCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 3, 195, 1, 2),
    _Pmo10010CntlineDfrmTimCntValuePortn_Type()
)
pmo10010CntlineDfrmTimCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CntlineDfrmTimCntValuePortn.setStatus("current")
_Pmo10010CntlineDfrmTimCntErrorPortn_Type = EkiOnOff
_Pmo10010CntlineDfrmTimCntErrorPortn_Object = MibTableColumn
pmo10010CntlineDfrmTimCntErrorPortn = _Pmo10010CntlineDfrmTimCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 3, 195, 1, 3),
    _Pmo10010CntlineDfrmTimCntErrorPortn_Type()
)
pmo10010CntlineDfrmTimCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CntlineDfrmTimCntErrorPortn.setStatus("current")
_Pmo10010CntlineDfrmTimCntOverloadPortn_Type = EkiOnOff
_Pmo10010CntlineDfrmTimCntOverloadPortn_Object = MibTableColumn
pmo10010CntlineDfrmTimCntOverloadPortn = _Pmo10010CntlineDfrmTimCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 3, 195, 1, 4),
    _Pmo10010CntlineDfrmTimCntOverloadPortn_Type()
)
pmo10010CntlineDfrmTimCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CntlineDfrmTimCntOverloadPortn.setStatus("current")
_Pmo10010CntlocalLineTrscvFecCorrectedErrorCounterTable_Object = MibTable
pmo10010CntlocalLineTrscvFecCorrectedErrorCounterTable = _Pmo10010CntlocalLineTrscvFecCorrectedErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 3, 196)
)
if mibBuilder.loadTexts:
    pmo10010CntlocalLineTrscvFecCorrectedErrorCounterTable.setStatus("current")
_Pmo10010CntlocalLineTrscvFecCorrectedErrorCounterEntry_Object = MibTableRow
pmo10010CntlocalLineTrscvFecCorrectedErrorCounterEntry = _Pmo10010CntlocalLineTrscvFecCorrectedErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 3, 196, 1)
)
pmo10010CntlocalLineTrscvFecCorrectedErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010CntlocalLineTrscvFecCorrectedErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    pmo10010CntlocalLineTrscvFecCorrectedErrorCounterEntry.setStatus("current")


class _Pmo10010CntlocalLineTrscvFecCorrectedErrorCounterIndex_Type(Integer32):
    """Custom type pmo10010CntlocalLineTrscvFecCorrectedErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010CntlocalLineTrscvFecCorrectedErrorCounterIndex_Type.__name__ = "Integer32"
_Pmo10010CntlocalLineTrscvFecCorrectedErrorCounterIndex_Object = MibTableColumn
pmo10010CntlocalLineTrscvFecCorrectedErrorCounterIndex = _Pmo10010CntlocalLineTrscvFecCorrectedErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 3, 196, 1, 1),
    _Pmo10010CntlocalLineTrscvFecCorrectedErrorCounterIndex_Type()
)
pmo10010CntlocalLineTrscvFecCorrectedErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CntlocalLineTrscvFecCorrectedErrorCounterIndex.setStatus("current")
_Pmo10010CntlocalLineTrscvFecCorrectedErrorCounterValuePortn_Type = Counter64
_Pmo10010CntlocalLineTrscvFecCorrectedErrorCounterValuePortn_Object = MibTableColumn
pmo10010CntlocalLineTrscvFecCorrectedErrorCounterValuePortn = _Pmo10010CntlocalLineTrscvFecCorrectedErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 3, 196, 1, 2),
    _Pmo10010CntlocalLineTrscvFecCorrectedErrorCounterValuePortn_Type()
)
pmo10010CntlocalLineTrscvFecCorrectedErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CntlocalLineTrscvFecCorrectedErrorCounterValuePortn.setStatus("current")
_Pmo10010CntlocalLineTrscvFecCorrectedErrorCounterErrorPortn_Type = EkiOnOff
_Pmo10010CntlocalLineTrscvFecCorrectedErrorCounterErrorPortn_Object = MibTableColumn
pmo10010CntlocalLineTrscvFecCorrectedErrorCounterErrorPortn = _Pmo10010CntlocalLineTrscvFecCorrectedErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 3, 196, 1, 3),
    _Pmo10010CntlocalLineTrscvFecCorrectedErrorCounterErrorPortn_Type()
)
pmo10010CntlocalLineTrscvFecCorrectedErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CntlocalLineTrscvFecCorrectedErrorCounterErrorPortn.setStatus("current")
_Pmo10010CntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn_Type = EkiOnOff
_Pmo10010CntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn_Object = MibTableColumn
pmo10010CntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn = _Pmo10010CntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 3, 196, 1, 4),
    _Pmo10010CntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn_Type()
)
pmo10010CntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn.setStatus("current")
_Pmo10010CntlocalLineTrscvFecUncorrectedErrorCounterTable_Object = MibTable
pmo10010CntlocalLineTrscvFecUncorrectedErrorCounterTable = _Pmo10010CntlocalLineTrscvFecUncorrectedErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 3, 197)
)
if mibBuilder.loadTexts:
    pmo10010CntlocalLineTrscvFecUncorrectedErrorCounterTable.setStatus("current")
_Pmo10010CntlocalLineTrscvFecUncorrectedErrorCounterEntry_Object = MibTableRow
pmo10010CntlocalLineTrscvFecUncorrectedErrorCounterEntry = _Pmo10010CntlocalLineTrscvFecUncorrectedErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 3, 197, 1)
)
pmo10010CntlocalLineTrscvFecUncorrectedErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010CntlocalLineTrscvFecUncorrectedErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    pmo10010CntlocalLineTrscvFecUncorrectedErrorCounterEntry.setStatus("current")


class _Pmo10010CntlocalLineTrscvFecUncorrectedErrorCounterIndex_Type(Integer32):
    """Custom type pmo10010CntlocalLineTrscvFecUncorrectedErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010CntlocalLineTrscvFecUncorrectedErrorCounterIndex_Type.__name__ = "Integer32"
_Pmo10010CntlocalLineTrscvFecUncorrectedErrorCounterIndex_Object = MibTableColumn
pmo10010CntlocalLineTrscvFecUncorrectedErrorCounterIndex = _Pmo10010CntlocalLineTrscvFecUncorrectedErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 3, 197, 1, 1),
    _Pmo10010CntlocalLineTrscvFecUncorrectedErrorCounterIndex_Type()
)
pmo10010CntlocalLineTrscvFecUncorrectedErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CntlocalLineTrscvFecUncorrectedErrorCounterIndex.setStatus("current")
_Pmo10010CntlocalLineTrscvFecUncorrectedErrorCounterValuePortn_Type = Counter64
_Pmo10010CntlocalLineTrscvFecUncorrectedErrorCounterValuePortn_Object = MibTableColumn
pmo10010CntlocalLineTrscvFecUncorrectedErrorCounterValuePortn = _Pmo10010CntlocalLineTrscvFecUncorrectedErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 3, 197, 1, 2),
    _Pmo10010CntlocalLineTrscvFecUncorrectedErrorCounterValuePortn_Type()
)
pmo10010CntlocalLineTrscvFecUncorrectedErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CntlocalLineTrscvFecUncorrectedErrorCounterValuePortn.setStatus("current")
_Pmo10010CntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn_Type = EkiOnOff
_Pmo10010CntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn_Object = MibTableColumn
pmo10010CntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn = _Pmo10010CntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 3, 197, 1, 3),
    _Pmo10010CntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn_Type()
)
pmo10010CntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn.setStatus("current")
_Pmo10010CntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn_Type = EkiOnOff
_Pmo10010CntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn_Object = MibTableColumn
pmo10010CntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn = _Pmo10010CntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 3, 197, 1, 4),
    _Pmo10010CntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn_Type()
)
pmo10010CntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn.setStatus("current")
_Pmo10010CntlocalLinePmBlockErrorCounterTable_Object = MibTable
pmo10010CntlocalLinePmBlockErrorCounterTable = _Pmo10010CntlocalLinePmBlockErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 3, 200)
)
if mibBuilder.loadTexts:
    pmo10010CntlocalLinePmBlockErrorCounterTable.setStatus("current")
_Pmo10010CntlocalLinePmBlockErrorCounterEntry_Object = MibTableRow
pmo10010CntlocalLinePmBlockErrorCounterEntry = _Pmo10010CntlocalLinePmBlockErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 3, 200, 1)
)
pmo10010CntlocalLinePmBlockErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010CntlocalLinePmBlockErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    pmo10010CntlocalLinePmBlockErrorCounterEntry.setStatus("current")


class _Pmo10010CntlocalLinePmBlockErrorCounterIndex_Type(Integer32):
    """Custom type pmo10010CntlocalLinePmBlockErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010CntlocalLinePmBlockErrorCounterIndex_Type.__name__ = "Integer32"
_Pmo10010CntlocalLinePmBlockErrorCounterIndex_Object = MibTableColumn
pmo10010CntlocalLinePmBlockErrorCounterIndex = _Pmo10010CntlocalLinePmBlockErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 3, 200, 1, 1),
    _Pmo10010CntlocalLinePmBlockErrorCounterIndex_Type()
)
pmo10010CntlocalLinePmBlockErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CntlocalLinePmBlockErrorCounterIndex.setStatus("current")
_Pmo10010CntlocalLinePmBlockErrorCounterValuePortn_Type = Counter64
_Pmo10010CntlocalLinePmBlockErrorCounterValuePortn_Object = MibTableColumn
pmo10010CntlocalLinePmBlockErrorCounterValuePortn = _Pmo10010CntlocalLinePmBlockErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 3, 200, 1, 2),
    _Pmo10010CntlocalLinePmBlockErrorCounterValuePortn_Type()
)
pmo10010CntlocalLinePmBlockErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CntlocalLinePmBlockErrorCounterValuePortn.setStatus("current")
_Pmo10010CntlocalLinePmBlockErrorCounterErrorPortn_Type = EkiOnOff
_Pmo10010CntlocalLinePmBlockErrorCounterErrorPortn_Object = MibTableColumn
pmo10010CntlocalLinePmBlockErrorCounterErrorPortn = _Pmo10010CntlocalLinePmBlockErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 3, 200, 1, 3),
    _Pmo10010CntlocalLinePmBlockErrorCounterErrorPortn_Type()
)
pmo10010CntlocalLinePmBlockErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CntlocalLinePmBlockErrorCounterErrorPortn.setStatus("current")
_Pmo10010CntlocalLinePmBlockErrorCounterOverloadPortn_Type = EkiOnOff
_Pmo10010CntlocalLinePmBlockErrorCounterOverloadPortn_Object = MibTableColumn
pmo10010CntlocalLinePmBlockErrorCounterOverloadPortn = _Pmo10010CntlocalLinePmBlockErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 3, 200, 1, 4),
    _Pmo10010CntlocalLinePmBlockErrorCounterOverloadPortn_Type()
)
pmo10010CntlocalLinePmBlockErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CntlocalLinePmBlockErrorCounterOverloadPortn.setStatus("current")
_Pmo10010CntremoteLinePmBlockErrorCounterTable_Object = MibTable
pmo10010CntremoteLinePmBlockErrorCounterTable = _Pmo10010CntremoteLinePmBlockErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 3, 201)
)
if mibBuilder.loadTexts:
    pmo10010CntremoteLinePmBlockErrorCounterTable.setStatus("current")
_Pmo10010CntremoteLinePmBlockErrorCounterEntry_Object = MibTableRow
pmo10010CntremoteLinePmBlockErrorCounterEntry = _Pmo10010CntremoteLinePmBlockErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 3, 201, 1)
)
pmo10010CntremoteLinePmBlockErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010CntremoteLinePmBlockErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    pmo10010CntremoteLinePmBlockErrorCounterEntry.setStatus("current")


class _Pmo10010CntremoteLinePmBlockErrorCounterIndex_Type(Integer32):
    """Custom type pmo10010CntremoteLinePmBlockErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010CntremoteLinePmBlockErrorCounterIndex_Type.__name__ = "Integer32"
_Pmo10010CntremoteLinePmBlockErrorCounterIndex_Object = MibTableColumn
pmo10010CntremoteLinePmBlockErrorCounterIndex = _Pmo10010CntremoteLinePmBlockErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 3, 201, 1, 1),
    _Pmo10010CntremoteLinePmBlockErrorCounterIndex_Type()
)
pmo10010CntremoteLinePmBlockErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CntremoteLinePmBlockErrorCounterIndex.setStatus("current")
_Pmo10010CntremoteLinePmBlockErrorCounterValuePortn_Type = Counter64
_Pmo10010CntremoteLinePmBlockErrorCounterValuePortn_Object = MibTableColumn
pmo10010CntremoteLinePmBlockErrorCounterValuePortn = _Pmo10010CntremoteLinePmBlockErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 3, 201, 1, 2),
    _Pmo10010CntremoteLinePmBlockErrorCounterValuePortn_Type()
)
pmo10010CntremoteLinePmBlockErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CntremoteLinePmBlockErrorCounterValuePortn.setStatus("current")
_Pmo10010CntremoteLinePmBlockErrorCounterErrorPortn_Type = EkiOnOff
_Pmo10010CntremoteLinePmBlockErrorCounterErrorPortn_Object = MibTableColumn
pmo10010CntremoteLinePmBlockErrorCounterErrorPortn = _Pmo10010CntremoteLinePmBlockErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 3, 201, 1, 3),
    _Pmo10010CntremoteLinePmBlockErrorCounterErrorPortn_Type()
)
pmo10010CntremoteLinePmBlockErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CntremoteLinePmBlockErrorCounterErrorPortn.setStatus("current")
_Pmo10010CntremoteLinePmBlockErrorCounterOverloadPortn_Type = EkiOnOff
_Pmo10010CntremoteLinePmBlockErrorCounterOverloadPortn_Object = MibTableColumn
pmo10010CntremoteLinePmBlockErrorCounterOverloadPortn = _Pmo10010CntremoteLinePmBlockErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 4, 3, 201, 1, 4),
    _Pmo10010CntremoteLinePmBlockErrorCounterOverloadPortn_Type()
)
pmo10010CntremoteLinePmBlockErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CntremoteLinePmBlockErrorCounterOverloadPortn.setStatus("current")
_Pmo10010controlsWrite_ObjectIdentity = ObjectIdentity
pmo10010controlsWrite = _Pmo10010controlsWrite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6)
)
_Pmo10010CtrlOther_ObjectIdentity = ObjectIdentity
pmo10010CtrlOther = _Pmo10010CtrlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 1)
)
_Pmo10010CtrlconfMgnt1_ObjectIdentity = ObjectIdentity
pmo10010CtrlconfMgnt1 = _Pmo10010CtrlconfMgnt1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 1, 1)
)
_Pmo10010CtrlConf1Load1_Type = EkiOnOff
_Pmo10010CtrlConf1Load1_Object = MibScalar
pmo10010CtrlConf1Load1 = _Pmo10010CtrlConf1Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 1, 1, 1),
    _Pmo10010CtrlConf1Load1_Type()
)
pmo10010CtrlConf1Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CtrlConf1Load1.setStatus("current")
_Pmo10010CtrlConf2Load1_Type = EkiOnOff
_Pmo10010CtrlConf2Load1_Object = MibScalar
pmo10010CtrlConf2Load1 = _Pmo10010CtrlConf2Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 1, 1, 2),
    _Pmo10010CtrlConf2Load1_Type()
)
pmo10010CtrlConf2Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CtrlConf2Load1.setStatus("current")
_Pmo10010CtrlConf2Flash1_Type = EkiOnOff
_Pmo10010CtrlConf2Flash1_Object = MibScalar
pmo10010CtrlConf2Flash1 = _Pmo10010CtrlConf2Flash1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 1, 1, 10),
    _Pmo10010CtrlConf2Flash1_Type()
)
pmo10010CtrlConf2Flash1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CtrlConf2Flash1.setStatus("current")
_Pmo10010CtrlConf2Clear1_Type = EkiOnOff
_Pmo10010CtrlConf2Clear1_Object = MibScalar
pmo10010CtrlConf2Clear1 = _Pmo10010CtrlConf2Clear1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 1, 1, 14),
    _Pmo10010CtrlConf2Clear1_Type()
)
pmo10010CtrlConf2Clear1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CtrlConf2Clear1.setStatus("current")
_Pmo10010Ctrlsynth4_ObjectIdentity = ObjectIdentity
pmo10010Ctrlsynth4 = _Pmo10010Ctrlsynth4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 1, 4)
)
_Pmo10010CtrlCorrelatOn_Type = EkiOnOff
_Pmo10010CtrlCorrelatOn_Object = MibScalar
pmo10010CtrlCorrelatOn = _Pmo10010CtrlCorrelatOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 1, 4, 1),
    _Pmo10010CtrlCorrelatOn_Type()
)
pmo10010CtrlCorrelatOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CtrlCorrelatOn.setStatus("current")
_Pmo10010CtrlCorrelatOff_Type = EkiOnOff
_Pmo10010CtrlCorrelatOff_Object = MibScalar
pmo10010CtrlCorrelatOff = _Pmo10010CtrlCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 1, 4, 2),
    _Pmo10010CtrlCorrelatOff_Type()
)
pmo10010CtrlCorrelatOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CtrlCorrelatOff.setStatus("current")
_Pmo10010CtrlswMgnt_ObjectIdentity = ObjectIdentity
pmo10010CtrlswMgnt = _Pmo10010CtrlswMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 1, 5)
)
_Pmo10010CtrlColdReset_Type = EkiOnOff
_Pmo10010CtrlColdReset_Object = MibScalar
pmo10010CtrlColdReset = _Pmo10010CtrlColdReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 1, 5, 2),
    _Pmo10010CtrlColdReset_Type()
)
pmo10010CtrlColdReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CtrlColdReset.setStatus("current")
_Pmo10010CtrlWarmReset_Type = EkiOnOff
_Pmo10010CtrlWarmReset_Object = MibScalar
pmo10010CtrlWarmReset = _Pmo10010CtrlWarmReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 1, 5, 3),
    _Pmo10010CtrlWarmReset_Type()
)
pmo10010CtrlWarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CtrlWarmReset.setStatus("current")
_Pmo10010CtrlLoadSwBank1_Type = EkiOnOff
_Pmo10010CtrlLoadSwBank1_Object = MibScalar
pmo10010CtrlLoadSwBank1 = _Pmo10010CtrlLoadSwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 1, 5, 5),
    _Pmo10010CtrlLoadSwBank1_Type()
)
pmo10010CtrlLoadSwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CtrlLoadSwBank1.setStatus("current")
_Pmo10010CtrlLoadSwBank2_Type = EkiOnOff
_Pmo10010CtrlLoadSwBank2_Object = MibScalar
pmo10010CtrlLoadSwBank2 = _Pmo10010CtrlLoadSwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 1, 5, 6),
    _Pmo10010CtrlLoadSwBank2_Type()
)
pmo10010CtrlLoadSwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CtrlLoadSwBank2.setStatus("current")
_Pmo10010CtrlgwMgnt_ObjectIdentity = ObjectIdentity
pmo10010CtrlgwMgnt = _Pmo10010CtrlgwMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 1, 6)
)
_Pmo10010CtrlCurrentGwReset_Type = EkiOnOff
_Pmo10010CtrlCurrentGwReset_Object = MibScalar
pmo10010CtrlCurrentGwReset = _Pmo10010CtrlCurrentGwReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 1, 6, 1),
    _Pmo10010CtrlCurrentGwReset_Type()
)
pmo10010CtrlCurrentGwReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CtrlCurrentGwReset.setStatus("current")
_Pmo10010CtrlLoadGwBank1_Type = EkiOnOff
_Pmo10010CtrlLoadGwBank1_Object = MibScalar
pmo10010CtrlLoadGwBank1 = _Pmo10010CtrlLoadGwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 1, 6, 5),
    _Pmo10010CtrlLoadGwBank1_Type()
)
pmo10010CtrlLoadGwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CtrlLoadGwBank1.setStatus("current")
_Pmo10010CtrlLoadGwBank2_Type = EkiOnOff
_Pmo10010CtrlLoadGwBank2_Object = MibScalar
pmo10010CtrlLoadGwBank2 = _Pmo10010CtrlLoadGwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 1, 6, 6),
    _Pmo10010CtrlLoadGwBank2_Type()
)
pmo10010CtrlLoadGwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CtrlLoadGwBank2.setStatus("current")
_Pmo10010CtrlLoadGwBank3_Type = EkiOnOff
_Pmo10010CtrlLoadGwBank3_Object = MibScalar
pmo10010CtrlLoadGwBank3 = _Pmo10010CtrlLoadGwBank3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 1, 6, 7),
    _Pmo10010CtrlLoadGwBank3_Type()
)
pmo10010CtrlLoadGwBank3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CtrlLoadGwBank3.setStatus("current")
_Pmo10010CtrlLoadGwBank4_Type = EkiOnOff
_Pmo10010CtrlLoadGwBank4_Object = MibScalar
pmo10010CtrlLoadGwBank4 = _Pmo10010CtrlLoadGwBank4_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 1, 6, 8),
    _Pmo10010CtrlLoadGwBank4_Type()
)
pmo10010CtrlLoadGwBank4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CtrlLoadGwBank4.setStatus("current")
_Pmo10010CtrlledTest_ObjectIdentity = ObjectIdentity
pmo10010CtrlledTest = _Pmo10010CtrlledTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 1, 192)
)
_Pmo10010CtrlGreenLed_Type = EkiOnOff
_Pmo10010CtrlGreenLed_Object = MibScalar
pmo10010CtrlGreenLed = _Pmo10010CtrlGreenLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 1, 192, 1),
    _Pmo10010CtrlGreenLed_Type()
)
pmo10010CtrlGreenLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CtrlGreenLed.setStatus("current")
_Pmo10010CtrlRedLed_Type = EkiOnOff
_Pmo10010CtrlRedLed_Object = MibScalar
pmo10010CtrlRedLed = _Pmo10010CtrlRedLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 1, 192, 2),
    _Pmo10010CtrlRedLed_Type()
)
pmo10010CtrlRedLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CtrlRedLed.setStatus("current")
_Pmo10010CtrlLedOff_Type = EkiOnOff
_Pmo10010CtrlLedOff_Object = MibScalar
pmo10010CtrlLedOff = _Pmo10010CtrlLedOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 1, 192, 3),
    _Pmo10010CtrlLedOff_Type()
)
pmo10010CtrlLedOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CtrlLedOff.setStatus("current")
_Pmo10010CtrlinitSwitchMarvell_ObjectIdentity = ObjectIdentity
pmo10010CtrlinitSwitchMarvell = _Pmo10010CtrlinitSwitchMarvell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 1, 201)
)
_Pmo10010CtrlInitSwitchMarvell_Type = EkiOnOff
_Pmo10010CtrlInitSwitchMarvell_Object = MibScalar
pmo10010CtrlInitSwitchMarvell = _Pmo10010CtrlInitSwitchMarvell_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 1, 201, 1),
    _Pmo10010CtrlInitSwitchMarvell_Type()
)
pmo10010CtrlInitSwitchMarvell.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CtrlInitSwitchMarvell.setStatus("current")
_Pmo10010CtrlresetCount_ObjectIdentity = ObjectIdentity
pmo10010CtrlresetCount = _Pmo10010CtrlresetCount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 1, 259)
)
_Pmo10010CtrlResetcount_Type = EkiOnOff
_Pmo10010CtrlResetcount_Object = MibScalar
pmo10010CtrlResetcount = _Pmo10010CtrlResetcount_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 1, 259, 1),
    _Pmo10010CtrlResetcount_Type()
)
pmo10010CtrlResetcount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CtrlResetcount.setStatus("current")
_Pmo10010CtrlresetRmon_ObjectIdentity = ObjectIdentity
pmo10010CtrlresetRmon = _Pmo10010CtrlresetRmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 1, 260)
)
_Pmo10010CtrlResetrmon_Type = EkiOnOff
_Pmo10010CtrlResetrmon_Object = MibScalar
pmo10010CtrlResetrmon = _Pmo10010CtrlResetrmon_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 1, 260, 1),
    _Pmo10010CtrlResetrmon_Type()
)
pmo10010CtrlResetrmon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CtrlResetrmon.setStatus("current")
_Pmo10010CtrlresetMeasurements_ObjectIdentity = ObjectIdentity
pmo10010CtrlresetMeasurements = _Pmo10010CtrlresetMeasurements_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 1, 261)
)
_Pmo10010CtrlResetmeasurements_Type = EkiOnOff
_Pmo10010CtrlResetmeasurements_Object = MibScalar
pmo10010CtrlResetmeasurements = _Pmo10010CtrlResetmeasurements_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 1, 261, 1),
    _Pmo10010CtrlResetmeasurements_Type()
)
pmo10010CtrlResetmeasurements.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CtrlResetmeasurements.setStatus("current")
_Pmo10010CtrlClient_ObjectIdentity = ObjectIdentity
pmo10010CtrlClient = _Pmo10010CtrlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 2)
)
_Pmo10010CtrlaccessLoopTable_Object = MibTable
pmo10010CtrlaccessLoopTable = _Pmo10010CtrlaccessLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 2, 16)
)
if mibBuilder.loadTexts:
    pmo10010CtrlaccessLoopTable.setStatus("current")
_Pmo10010CtrlaccessLoopEntry_Object = MibTableRow
pmo10010CtrlaccessLoopEntry = _Pmo10010CtrlaccessLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 2, 16, 1)
)
pmo10010CtrlaccessLoopEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010CtrlaccessLoopIndex"),
)
if mibBuilder.loadTexts:
    pmo10010CtrlaccessLoopEntry.setStatus("current")


class _Pmo10010CtrlaccessLoopIndex_Type(Integer32):
    """Custom type pmo10010CtrlaccessLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010CtrlaccessLoopIndex_Type.__name__ = "Integer32"
_Pmo10010CtrlaccessLoopIndex_Object = MibTableColumn
pmo10010CtrlaccessLoopIndex = _Pmo10010CtrlaccessLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 2, 16, 1, 1),
    _Pmo10010CtrlaccessLoopIndex_Type()
)
pmo10010CtrlaccessLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CtrlaccessLoopIndex.setStatus("current")
_Pmo10010CtrlaccessLoopPortn_Type = EkiState
_Pmo10010CtrlaccessLoopPortn_Object = MibTableColumn
pmo10010CtrlaccessLoopPortn = _Pmo10010CtrlaccessLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 2, 16, 1, 2),
    _Pmo10010CtrlaccessLoopPortn_Type()
)
pmo10010CtrlaccessLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CtrlaccessLoopPortn.setStatus("current")
_Pmo10010CtrlclientLoopToLineTable_Object = MibTable
pmo10010CtrlclientLoopToLineTable = _Pmo10010CtrlclientLoopToLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 2, 17)
)
if mibBuilder.loadTexts:
    pmo10010CtrlclientLoopToLineTable.setStatus("current")
_Pmo10010CtrlclientLoopToLineEntry_Object = MibTableRow
pmo10010CtrlclientLoopToLineEntry = _Pmo10010CtrlclientLoopToLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 2, 17, 1)
)
pmo10010CtrlclientLoopToLineEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010CtrlclientLoopToLineIndex"),
)
if mibBuilder.loadTexts:
    pmo10010CtrlclientLoopToLineEntry.setStatus("current")


class _Pmo10010CtrlclientLoopToLineIndex_Type(Integer32):
    """Custom type pmo10010CtrlclientLoopToLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010CtrlclientLoopToLineIndex_Type.__name__ = "Integer32"
_Pmo10010CtrlclientLoopToLineIndex_Object = MibTableColumn
pmo10010CtrlclientLoopToLineIndex = _Pmo10010CtrlclientLoopToLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 2, 17, 1, 1),
    _Pmo10010CtrlclientLoopToLineIndex_Type()
)
pmo10010CtrlclientLoopToLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CtrlclientLoopToLineIndex.setStatus("current")
_Pmo10010CtrlclientLoopToLinePortn_Type = EkiState
_Pmo10010CtrlclientLoopToLinePortn_Object = MibTableColumn
pmo10010CtrlclientLoopToLinePortn = _Pmo10010CtrlclientLoopToLinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 2, 17, 1, 2),
    _Pmo10010CtrlclientLoopToLinePortn_Type()
)
pmo10010CtrlclientLoopToLinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CtrlclientLoopToLinePortn.setStatus("current")
_Pmo10010CtrlcsfUpInsTable_Object = MibTable
pmo10010CtrlcsfUpInsTable = _Pmo10010CtrlcsfUpInsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 2, 21)
)
if mibBuilder.loadTexts:
    pmo10010CtrlcsfUpInsTable.setStatus("current")
_Pmo10010CtrlcsfUpInsEntry_Object = MibTableRow
pmo10010CtrlcsfUpInsEntry = _Pmo10010CtrlcsfUpInsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 2, 21, 1)
)
pmo10010CtrlcsfUpInsEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010CtrlcsfUpInsIndex"),
)
if mibBuilder.loadTexts:
    pmo10010CtrlcsfUpInsEntry.setStatus("current")


class _Pmo10010CtrlcsfUpInsIndex_Type(Integer32):
    """Custom type pmo10010CtrlcsfUpInsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010CtrlcsfUpInsIndex_Type.__name__ = "Integer32"
_Pmo10010CtrlcsfUpInsIndex_Object = MibTableColumn
pmo10010CtrlcsfUpInsIndex = _Pmo10010CtrlcsfUpInsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 2, 21, 1, 1),
    _Pmo10010CtrlcsfUpInsIndex_Type()
)
pmo10010CtrlcsfUpInsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CtrlcsfUpInsIndex.setStatus("current")
_Pmo10010CtrlcsfUpInsPortn_Type = EkiState
_Pmo10010CtrlcsfUpInsPortn_Object = MibTableColumn
pmo10010CtrlcsfUpInsPortn = _Pmo10010CtrlcsfUpInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 2, 21, 1, 2),
    _Pmo10010CtrlcsfUpInsPortn_Type()
)
pmo10010CtrlcsfUpInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CtrlcsfUpInsPortn.setStatus("current")
_Pmo10010CtrlcaisDwInsTable_Object = MibTable
pmo10010CtrlcaisDwInsTable = _Pmo10010CtrlcaisDwInsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 2, 22)
)
if mibBuilder.loadTexts:
    pmo10010CtrlcaisDwInsTable.setStatus("current")
_Pmo10010CtrlcaisDwInsEntry_Object = MibTableRow
pmo10010CtrlcaisDwInsEntry = _Pmo10010CtrlcaisDwInsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 2, 22, 1)
)
pmo10010CtrlcaisDwInsEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010CtrlcaisDwInsIndex"),
)
if mibBuilder.loadTexts:
    pmo10010CtrlcaisDwInsEntry.setStatus("current")


class _Pmo10010CtrlcaisDwInsIndex_Type(Integer32):
    """Custom type pmo10010CtrlcaisDwInsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010CtrlcaisDwInsIndex_Type.__name__ = "Integer32"
_Pmo10010CtrlcaisDwInsIndex_Object = MibTableColumn
pmo10010CtrlcaisDwInsIndex = _Pmo10010CtrlcaisDwInsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 2, 22, 1, 1),
    _Pmo10010CtrlcaisDwInsIndex_Type()
)
pmo10010CtrlcaisDwInsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CtrlcaisDwInsIndex.setStatus("current")
_Pmo10010CtrlcaisDwInsPortn_Type = EkiState
_Pmo10010CtrlcaisDwInsPortn_Object = MibTableColumn
pmo10010CtrlcaisDwInsPortn = _Pmo10010CtrlcaisDwInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 2, 22, 1, 2),
    _Pmo10010CtrlcaisDwInsPortn_Type()
)
pmo10010CtrlcaisDwInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CtrlcaisDwInsPortn.setStatus("current")
_Pmo10010CtrlLine_ObjectIdentity = ObjectIdentity
pmo10010CtrlLine = _Pmo10010CtrlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 3)
)
_Pmo10010CtrlcommAccessLoopTable_Object = MibTable
pmo10010CtrlcommAccessLoopTable = _Pmo10010CtrlcommAccessLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 3, 64)
)
if mibBuilder.loadTexts:
    pmo10010CtrlcommAccessLoopTable.setStatus("current")
_Pmo10010CtrlcommAccessLoopEntry_Object = MibTableRow
pmo10010CtrlcommAccessLoopEntry = _Pmo10010CtrlcommAccessLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 3, 64, 1)
)
pmo10010CtrlcommAccessLoopEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010CtrlcommAccessLoopIndex"),
)
if mibBuilder.loadTexts:
    pmo10010CtrlcommAccessLoopEntry.setStatus("current")


class _Pmo10010CtrlcommAccessLoopIndex_Type(Integer32):
    """Custom type pmo10010CtrlcommAccessLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010CtrlcommAccessLoopIndex_Type.__name__ = "Integer32"
_Pmo10010CtrlcommAccessLoopIndex_Object = MibTableColumn
pmo10010CtrlcommAccessLoopIndex = _Pmo10010CtrlcommAccessLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 3, 64, 1, 1),
    _Pmo10010CtrlcommAccessLoopIndex_Type()
)
pmo10010CtrlcommAccessLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CtrlcommAccessLoopIndex.setStatus("current")
_Pmo10010CtrlcommAccessLoopPortn_Type = EkiState
_Pmo10010CtrlcommAccessLoopPortn_Object = MibTableColumn
pmo10010CtrlcommAccessLoopPortn = _Pmo10010CtrlcommAccessLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 3, 64, 1, 2),
    _Pmo10010CtrlcommAccessLoopPortn_Type()
)
pmo10010CtrlcommAccessLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CtrlcommAccessLoopPortn.setStatus("current")
_Pmo10010CtrllineLoopTable_Object = MibTable
pmo10010CtrllineLoopTable = _Pmo10010CtrllineLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 3, 66)
)
if mibBuilder.loadTexts:
    pmo10010CtrllineLoopTable.setStatus("current")
_Pmo10010CtrllineLoopEntry_Object = MibTableRow
pmo10010CtrllineLoopEntry = _Pmo10010CtrllineLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 3, 66, 1)
)
pmo10010CtrllineLoopEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010CtrllineLoopIndex"),
)
if mibBuilder.loadTexts:
    pmo10010CtrllineLoopEntry.setStatus("current")


class _Pmo10010CtrllineLoopIndex_Type(Integer32):
    """Custom type pmo10010CtrllineLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010CtrllineLoopIndex_Type.__name__ = "Integer32"
_Pmo10010CtrllineLoopIndex_Object = MibTableColumn
pmo10010CtrllineLoopIndex = _Pmo10010CtrllineLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 3, 66, 1, 1),
    _Pmo10010CtrllineLoopIndex_Type()
)
pmo10010CtrllineLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CtrllineLoopIndex.setStatus("current")
_Pmo10010CtrllineLoopPortn_Type = EkiState
_Pmo10010CtrllineLoopPortn_Object = MibTableColumn
pmo10010CtrllineLoopPortn = _Pmo10010CtrllineLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 3, 66, 1, 2),
    _Pmo10010CtrllineLoopPortn_Type()
)
pmo10010CtrllineLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CtrllineLoopPortn.setStatus("current")
_Pmo10010CtrlfecDisableTable_Object = MibTable
pmo10010CtrlfecDisableTable = _Pmo10010CtrlfecDisableTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 3, 69)
)
if mibBuilder.loadTexts:
    pmo10010CtrlfecDisableTable.setStatus("current")
_Pmo10010CtrlfecDisableEntry_Object = MibTableRow
pmo10010CtrlfecDisableEntry = _Pmo10010CtrlfecDisableEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 3, 69, 1)
)
pmo10010CtrlfecDisableEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010CtrlfecDisableIndex"),
)
if mibBuilder.loadTexts:
    pmo10010CtrlfecDisableEntry.setStatus("current")


class _Pmo10010CtrlfecDisableIndex_Type(Integer32):
    """Custom type pmo10010CtrlfecDisableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010CtrlfecDisableIndex_Type.__name__ = "Integer32"
_Pmo10010CtrlfecDisableIndex_Object = MibTableColumn
pmo10010CtrlfecDisableIndex = _Pmo10010CtrlfecDisableIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 3, 69, 1, 1),
    _Pmo10010CtrlfecDisableIndex_Type()
)
pmo10010CtrlfecDisableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CtrlfecDisableIndex.setStatus("current")
_Pmo10010CtrlfecDisablePortn_Type = EkiState
_Pmo10010CtrlfecDisablePortn_Object = MibTableColumn
pmo10010CtrlfecDisablePortn = _Pmo10010CtrlfecDisablePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 3, 69, 1, 2),
    _Pmo10010CtrlfecDisablePortn_Type()
)
pmo10010CtrlfecDisablePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CtrlfecDisablePortn.setStatus("current")
_Pmo10010CtrlmsaLineLoopTable_Object = MibTable
pmo10010CtrlmsaLineLoopTable = _Pmo10010CtrlmsaLineLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 3, 209)
)
if mibBuilder.loadTexts:
    pmo10010CtrlmsaLineLoopTable.setStatus("current")
_Pmo10010CtrlmsaLineLoopEntry_Object = MibTableRow
pmo10010CtrlmsaLineLoopEntry = _Pmo10010CtrlmsaLineLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 3, 209, 1)
)
pmo10010CtrlmsaLineLoopEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010CtrlmsaLineLoopIndex"),
)
if mibBuilder.loadTexts:
    pmo10010CtrlmsaLineLoopEntry.setStatus("current")


class _Pmo10010CtrlmsaLineLoopIndex_Type(Integer32):
    """Custom type pmo10010CtrlmsaLineLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010CtrlmsaLineLoopIndex_Type.__name__ = "Integer32"
_Pmo10010CtrlmsaLineLoopIndex_Object = MibTableColumn
pmo10010CtrlmsaLineLoopIndex = _Pmo10010CtrlmsaLineLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 3, 209, 1, 1),
    _Pmo10010CtrlmsaLineLoopIndex_Type()
)
pmo10010CtrlmsaLineLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CtrlmsaLineLoopIndex.setStatus("current")
_Pmo10010CtrlmsaLineLoopPortn_Type = EkiState
_Pmo10010CtrlmsaLineLoopPortn_Object = MibTableColumn
pmo10010CtrlmsaLineLoopPortn = _Pmo10010CtrlmsaLineLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 3, 209, 1, 2),
    _Pmo10010CtrlmsaLineLoopPortn_Type()
)
pmo10010CtrlmsaLineLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CtrlmsaLineLoopPortn.setStatus("current")
_Pmo10010CtrlmsaTxResetTable_Object = MibTable
pmo10010CtrlmsaTxResetTable = _Pmo10010CtrlmsaTxResetTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 3, 210)
)
if mibBuilder.loadTexts:
    pmo10010CtrlmsaTxResetTable.setStatus("current")
_Pmo10010CtrlmsaTxResetEntry_Object = MibTableRow
pmo10010CtrlmsaTxResetEntry = _Pmo10010CtrlmsaTxResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 3, 210, 1)
)
pmo10010CtrlmsaTxResetEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010CtrlmsaTxResetIndex"),
)
if mibBuilder.loadTexts:
    pmo10010CtrlmsaTxResetEntry.setStatus("current")


class _Pmo10010CtrlmsaTxResetIndex_Type(Integer32):
    """Custom type pmo10010CtrlmsaTxResetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010CtrlmsaTxResetIndex_Type.__name__ = "Integer32"
_Pmo10010CtrlmsaTxResetIndex_Object = MibTableColumn
pmo10010CtrlmsaTxResetIndex = _Pmo10010CtrlmsaTxResetIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 3, 210, 1, 1),
    _Pmo10010CtrlmsaTxResetIndex_Type()
)
pmo10010CtrlmsaTxResetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CtrlmsaTxResetIndex.setStatus("current")
_Pmo10010CtrlmsaTxResetPortn_Type = EkiState
_Pmo10010CtrlmsaTxResetPortn_Object = MibTableColumn
pmo10010CtrlmsaTxResetPortn = _Pmo10010CtrlmsaTxResetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 3, 210, 1, 2),
    _Pmo10010CtrlmsaTxResetPortn_Type()
)
pmo10010CtrlmsaTxResetPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CtrlmsaTxResetPortn.setStatus("current")
_Pmo10010CtrlmsaRxResetTable_Object = MibTable
pmo10010CtrlmsaRxResetTable = _Pmo10010CtrlmsaRxResetTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 3, 211)
)
if mibBuilder.loadTexts:
    pmo10010CtrlmsaRxResetTable.setStatus("current")
_Pmo10010CtrlmsaRxResetEntry_Object = MibTableRow
pmo10010CtrlmsaRxResetEntry = _Pmo10010CtrlmsaRxResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 3, 211, 1)
)
pmo10010CtrlmsaRxResetEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010CtrlmsaRxResetIndex"),
)
if mibBuilder.loadTexts:
    pmo10010CtrlmsaRxResetEntry.setStatus("current")


class _Pmo10010CtrlmsaRxResetIndex_Type(Integer32):
    """Custom type pmo10010CtrlmsaRxResetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010CtrlmsaRxResetIndex_Type.__name__ = "Integer32"
_Pmo10010CtrlmsaRxResetIndex_Object = MibTableColumn
pmo10010CtrlmsaRxResetIndex = _Pmo10010CtrlmsaRxResetIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 3, 211, 1, 1),
    _Pmo10010CtrlmsaRxResetIndex_Type()
)
pmo10010CtrlmsaRxResetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CtrlmsaRxResetIndex.setStatus("current")
_Pmo10010CtrlmsaRxResetPortn_Type = EkiState
_Pmo10010CtrlmsaRxResetPortn_Object = MibTableColumn
pmo10010CtrlmsaRxResetPortn = _Pmo10010CtrlmsaRxResetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 3, 211, 1, 2),
    _Pmo10010CtrlmsaRxResetPortn_Type()
)
pmo10010CtrlmsaRxResetPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CtrlmsaRxResetPortn.setStatus("current")
_Pmo10010CtrlmsaShutdownTable_Object = MibTable
pmo10010CtrlmsaShutdownTable = _Pmo10010CtrlmsaShutdownTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 3, 212)
)
if mibBuilder.loadTexts:
    pmo10010CtrlmsaShutdownTable.setStatus("current")
_Pmo10010CtrlmsaShutdownEntry_Object = MibTableRow
pmo10010CtrlmsaShutdownEntry = _Pmo10010CtrlmsaShutdownEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 3, 212, 1)
)
pmo10010CtrlmsaShutdownEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010CtrlmsaShutdownIndex"),
)
if mibBuilder.loadTexts:
    pmo10010CtrlmsaShutdownEntry.setStatus("current")


class _Pmo10010CtrlmsaShutdownIndex_Type(Integer32):
    """Custom type pmo10010CtrlmsaShutdownIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010CtrlmsaShutdownIndex_Type.__name__ = "Integer32"
_Pmo10010CtrlmsaShutdownIndex_Object = MibTableColumn
pmo10010CtrlmsaShutdownIndex = _Pmo10010CtrlmsaShutdownIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 3, 212, 1, 1),
    _Pmo10010CtrlmsaShutdownIndex_Type()
)
pmo10010CtrlmsaShutdownIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CtrlmsaShutdownIndex.setStatus("current")
_Pmo10010CtrlmsaShutdownPortn_Type = EkiState
_Pmo10010CtrlmsaShutdownPortn_Object = MibTableColumn
pmo10010CtrlmsaShutdownPortn = _Pmo10010CtrlmsaShutdownPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 6, 3, 212, 1, 2),
    _Pmo10010CtrlmsaShutdownPortn_Type()
)
pmo10010CtrlmsaShutdownPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CtrlmsaShutdownPortn.setStatus("current")
_Pmo10010ri_ObjectIdentity = ObjectIdentity
pmo10010ri = _Pmo10010ri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 7)
)
_Pmo10010riTable_ObjectIdentity = ObjectIdentity
pmo10010riTable = _Pmo10010riTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 7, 1)
)
_Pmo10010RinvSfpTable_Object = MibTable
pmo10010RinvSfpTable = _Pmo10010RinvSfpTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 7, 1, 1)
)
if mibBuilder.loadTexts:
    pmo10010RinvSfpTable.setStatus("current")
_Pmo10010RinvSfpEntry_Object = MibTableRow
pmo10010RinvSfpEntry = _Pmo10010RinvSfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 7, 1, 1, 1)
)
pmo10010RinvSfpEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010RinvSfpIndex"),
)
if mibBuilder.loadTexts:
    pmo10010RinvSfpEntry.setStatus("current")


class _Pmo10010RinvSfpIndex_Type(Integer32):
    """Custom type pmo10010RinvSfpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pmo10010RinvSfpIndex_Type.__name__ = "Integer32"
_Pmo10010RinvSfpIndex_Object = MibTableColumn
pmo10010RinvSfpIndex = _Pmo10010RinvSfpIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 7, 1, 1, 1, 1),
    _Pmo10010RinvSfpIndex_Type()
)
pmo10010RinvSfpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010RinvSfpIndex.setStatus("current")
_Pmo10010Rinvsfp_Type = DisplayString
_Pmo10010Rinvsfp_Object = MibTableColumn
pmo10010Rinvsfp = _Pmo10010Rinvsfp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 7, 1, 1, 1, 2),
    _Pmo10010Rinvsfp_Type()
)
pmo10010Rinvsfp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010Rinvsfp.setStatus("current")
_Pmo10010RinvLineTable_Object = MibTable
pmo10010RinvLineTable = _Pmo10010RinvLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 7, 1, 2)
)
if mibBuilder.loadTexts:
    pmo10010RinvLineTable.setStatus("current")
_Pmo10010RinvLineEntry_Object = MibTableRow
pmo10010RinvLineEntry = _Pmo10010RinvLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 7, 1, 2, 1)
)
pmo10010RinvLineEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010RinvLineIndex"),
)
if mibBuilder.loadTexts:
    pmo10010RinvLineEntry.setStatus("current")


class _Pmo10010RinvLineIndex_Type(Integer32):
    """Custom type pmo10010RinvLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pmo10010RinvLineIndex_Type.__name__ = "Integer32"
_Pmo10010RinvLineIndex_Object = MibTableColumn
pmo10010RinvLineIndex = _Pmo10010RinvLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 7, 1, 2, 1, 1),
    _Pmo10010RinvLineIndex_Type()
)
pmo10010RinvLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010RinvLineIndex.setStatus("current")
_Pmo10010RinvxfpLine_Type = DisplayString
_Pmo10010RinvxfpLine_Object = MibTableColumn
pmo10010RinvxfpLine = _Pmo10010RinvxfpLine_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 7, 1, 2, 1, 2),
    _Pmo10010RinvxfpLine_Type()
)
pmo10010RinvxfpLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010RinvxfpLine.setStatus("current")
_Pmo10010RinvReloadInventory_Type = EkiOnOff
_Pmo10010RinvReloadInventory_Object = MibScalar
pmo10010RinvReloadInventory = _Pmo10010RinvReloadInventory_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 7, 2),
    _Pmo10010RinvReloadInventory_Type()
)
pmo10010RinvReloadInventory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010RinvReloadInventory.setStatus("current")
_Pmo10010RinvHwPlatform_Type = DisplayString
_Pmo10010RinvHwPlatform_Object = MibScalar
pmo10010RinvHwPlatform = _Pmo10010RinvHwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 7, 3),
    _Pmo10010RinvHwPlatform_Type()
)
pmo10010RinvHwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010RinvHwPlatform.setStatus("current")
_Pmo10010RinvModulePlatform_Type = DisplayString
_Pmo10010RinvModulePlatform_Object = MibScalar
pmo10010RinvModulePlatform = _Pmo10010RinvModulePlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 7, 4),
    _Pmo10010RinvModulePlatform_Type()
)
pmo10010RinvModulePlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010RinvModulePlatform.setStatus("current")
_Pmo10010RinvSwPlatform_Type = DisplayString
_Pmo10010RinvSwPlatform_Object = MibScalar
pmo10010RinvSwPlatform = _Pmo10010RinvSwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 7, 5),
    _Pmo10010RinvSwPlatform_Type()
)
pmo10010RinvSwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010RinvSwPlatform.setStatus("current")
_Pmo10010RinvGwPlatform_Type = DisplayString
_Pmo10010RinvGwPlatform_Object = MibScalar
pmo10010RinvGwPlatform = _Pmo10010RinvGwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 7, 6),
    _Pmo10010RinvGwPlatform_Type()
)
pmo10010RinvGwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010RinvGwPlatform.setStatus("current")
_Pmo10010download_ObjectIdentity = ObjectIdentity
pmo10010download = _Pmo10010download_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 8)
)
_Pmo10010DwlOther_ObjectIdentity = ObjectIdentity
pmo10010DwlOther = _Pmo10010DwlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 8, 1)
)
_Pmo10010DwlrestartProcess_ObjectIdentity = ObjectIdentity
pmo10010DwlrestartProcess = _Pmo10010DwlrestartProcess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 8, 1, 0)
)
_Pmo10010DwlWarmRestartProcessed_Type = EkiOnOff
_Pmo10010DwlWarmRestartProcessed_Object = MibScalar
pmo10010DwlWarmRestartProcessed = _Pmo10010DwlWarmRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 8, 1, 0, 1),
    _Pmo10010DwlWarmRestartProcessed_Type()
)
pmo10010DwlWarmRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010DwlWarmRestartProcessed.setStatus("current")
_Pmo10010DwlColdRestartProcessed_Type = EkiOnOff
_Pmo10010DwlColdRestartProcessed_Object = MibScalar
pmo10010DwlColdRestartProcessed = _Pmo10010DwlColdRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 8, 1, 0, 2),
    _Pmo10010DwlColdRestartProcessed_Type()
)
pmo10010DwlColdRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010DwlColdRestartProcessed.setStatus("current")
_Pmo10010DwlswBanksUsed_ObjectIdentity = ObjectIdentity
pmo10010DwlswBanksUsed = _Pmo10010DwlswBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 8, 1, 1)
)
_Pmo10010DwlSwBank1Used_Type = EkiOnOff
_Pmo10010DwlSwBank1Used_Object = MibScalar
pmo10010DwlSwBank1Used = _Pmo10010DwlSwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 8, 1, 1, 1),
    _Pmo10010DwlSwBank1Used_Type()
)
pmo10010DwlSwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010DwlSwBank1Used.setStatus("current")
_Pmo10010DwlSwBank2Used_Type = EkiOnOff
_Pmo10010DwlSwBank2Used_Object = MibScalar
pmo10010DwlSwBank2Used = _Pmo10010DwlSwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 8, 1, 1, 2),
    _Pmo10010DwlSwBank2Used_Type()
)
pmo10010DwlSwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010DwlSwBank2Used.setStatus("current")
_Pmo10010DwlSwBank1Notempty_Type = EkiOnOff
_Pmo10010DwlSwBank1Notempty_Object = MibScalar
pmo10010DwlSwBank1Notempty = _Pmo10010DwlSwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 8, 1, 1, 5),
    _Pmo10010DwlSwBank1Notempty_Type()
)
pmo10010DwlSwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010DwlSwBank1Notempty.setStatus("current")
_Pmo10010DwlSwBank2Notempty_Type = EkiOnOff
_Pmo10010DwlSwBank2Notempty_Object = MibScalar
pmo10010DwlSwBank2Notempty = _Pmo10010DwlSwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 8, 1, 1, 6),
    _Pmo10010DwlSwBank2Notempty_Type()
)
pmo10010DwlSwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010DwlSwBank2Notempty.setStatus("current")
_Pmo10010DwlgwBanksUsed_ObjectIdentity = ObjectIdentity
pmo10010DwlgwBanksUsed = _Pmo10010DwlgwBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 8, 1, 2)
)
_Pmo10010DwlGwBank1Used_Type = EkiOnOff
_Pmo10010DwlGwBank1Used_Object = MibScalar
pmo10010DwlGwBank1Used = _Pmo10010DwlGwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 8, 1, 2, 1),
    _Pmo10010DwlGwBank1Used_Type()
)
pmo10010DwlGwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010DwlGwBank1Used.setStatus("current")
_Pmo10010DwlGwBank2Used_Type = EkiOnOff
_Pmo10010DwlGwBank2Used_Object = MibScalar
pmo10010DwlGwBank2Used = _Pmo10010DwlGwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 8, 1, 2, 2),
    _Pmo10010DwlGwBank2Used_Type()
)
pmo10010DwlGwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010DwlGwBank2Used.setStatus("current")
_Pmo10010DwlGwBank3Used_Type = EkiOnOff
_Pmo10010DwlGwBank3Used_Object = MibScalar
pmo10010DwlGwBank3Used = _Pmo10010DwlGwBank3Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 8, 1, 2, 3),
    _Pmo10010DwlGwBank3Used_Type()
)
pmo10010DwlGwBank3Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010DwlGwBank3Used.setStatus("current")
_Pmo10010DwlGwBank4Used_Type = EkiOnOff
_Pmo10010DwlGwBank4Used_Object = MibScalar
pmo10010DwlGwBank4Used = _Pmo10010DwlGwBank4Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 8, 1, 2, 4),
    _Pmo10010DwlGwBank4Used_Type()
)
pmo10010DwlGwBank4Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010DwlGwBank4Used.setStatus("current")
_Pmo10010DwlGwBank1Notempty_Type = EkiOnOff
_Pmo10010DwlGwBank1Notempty_Object = MibScalar
pmo10010DwlGwBank1Notempty = _Pmo10010DwlGwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 8, 1, 2, 5),
    _Pmo10010DwlGwBank1Notempty_Type()
)
pmo10010DwlGwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010DwlGwBank1Notempty.setStatus("current")
_Pmo10010DwlGwBank2Notempty_Type = EkiOnOff
_Pmo10010DwlGwBank2Notempty_Object = MibScalar
pmo10010DwlGwBank2Notempty = _Pmo10010DwlGwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 8, 1, 2, 6),
    _Pmo10010DwlGwBank2Notempty_Type()
)
pmo10010DwlGwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010DwlGwBank2Notempty.setStatus("current")
_Pmo10010DwlGwBank3Notempty_Type = EkiOnOff
_Pmo10010DwlGwBank3Notempty_Object = MibScalar
pmo10010DwlGwBank3Notempty = _Pmo10010DwlGwBank3Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 8, 1, 2, 7),
    _Pmo10010DwlGwBank3Notempty_Type()
)
pmo10010DwlGwBank3Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010DwlGwBank3Notempty.setStatus("current")
_Pmo10010DwlGwBank4Notempty_Type = EkiOnOff
_Pmo10010DwlGwBank4Notempty_Object = MibScalar
pmo10010DwlGwBank4Notempty = _Pmo10010DwlGwBank4Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 8, 1, 2, 8),
    _Pmo10010DwlGwBank4Notempty_Type()
)
pmo10010DwlGwBank4Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010DwlGwBank4Notempty.setStatus("current")
_Pmo10010DwlClient_ObjectIdentity = ObjectIdentity
pmo10010DwlClient = _Pmo10010DwlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 8, 2)
)
_Pmo10010DwlLine_ObjectIdentity = ObjectIdentity
pmo10010DwlLine = _Pmo10010DwlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 8, 3)
)
_Pmo10010Config_ObjectIdentity = ObjectIdentity
pmo10010Config = _Pmo10010Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9)
)
_Pmo10010CfgAccessCAisCsf_ObjectIdentity = ObjectIdentity
pmo10010CfgAccessCAisCsf = _Pmo10010CfgAccessCAisCsf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 1)
)
_Pmo10010CfgClientcaiscsfTable_Object = MibTable
pmo10010CfgClientcaiscsfTable = _Pmo10010CfgClientcaiscsfTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 1, 1)
)
if mibBuilder.loadTexts:
    pmo10010CfgClientcaiscsfTable.setStatus("current")
_Pmo10010CfgClientcaiscsfEntry_Object = MibTableRow
pmo10010CfgClientcaiscsfEntry = _Pmo10010CfgClientcaiscsfEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 1, 1, 1)
)
pmo10010CfgClientcaiscsfEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010CfgClientcaiscsfIndex"),
)
if mibBuilder.loadTexts:
    pmo10010CfgClientcaiscsfEntry.setStatus("current")


class _Pmo10010CfgClientcaiscsfIndex_Type(Integer32):
    """Custom type pmo10010CfgClientcaiscsfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010CfgClientcaiscsfIndex_Type.__name__ = "Integer32"
_Pmo10010CfgClientcaiscsfIndex_Object = MibTableColumn
pmo10010CfgClientcaiscsfIndex = _Pmo10010CfgClientcaiscsfIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 1, 1, 1, 1),
    _Pmo10010CfgClientcaiscsfIndex_Type()
)
pmo10010CfgClientcaiscsfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CfgClientcaiscsfIndex.setStatus("current")


class _Pmo10010CfgReservePortn_Type(Unsigned32):
    """Custom type pmo10010CfgReservePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmo10010CfgReservePortn_Type.__name__ = "Unsigned32"
_Pmo10010CfgReservePortn_Object = MibTableColumn
pmo10010CfgReservePortn = _Pmo10010CfgReservePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 1, 1, 1, 3),
    _Pmo10010CfgReservePortn_Type()
)
pmo10010CfgReservePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CfgReservePortn.setStatus("current")
_Pmo10010CfgStartup_ObjectIdentity = ObjectIdentity
pmo10010CfgStartup = _Pmo10010CfgStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 2)
)
_Pmo10010CfgClientStartupTable_Object = MibTable
pmo10010CfgClientStartupTable = _Pmo10010CfgClientStartupTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 2, 1)
)
if mibBuilder.loadTexts:
    pmo10010CfgClientStartupTable.setStatus("current")
_Pmo10010CfgClientStartupEntry_Object = MibTableRow
pmo10010CfgClientStartupEntry = _Pmo10010CfgClientStartupEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 2, 1, 1)
)
pmo10010CfgClientStartupEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010CfgClientStartupIndex"),
)
if mibBuilder.loadTexts:
    pmo10010CfgClientStartupEntry.setStatus("current")


class _Pmo10010CfgClientStartupIndex_Type(Integer32):
    """Custom type pmo10010CfgClientStartupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010CfgClientStartupIndex_Type.__name__ = "Integer32"
_Pmo10010CfgClientStartupIndex_Object = MibTableColumn
pmo10010CfgClientStartupIndex = _Pmo10010CfgClientStartupIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 2, 1, 1, 1),
    _Pmo10010CfgClientStartupIndex_Type()
)
pmo10010CfgClientStartupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CfgClientStartupIndex.setStatus("current")


class _Pmo10010CfgSystConfPortPortn_Type(Unsigned32):
    """Custom type pmo10010CfgSystConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmo10010CfgSystConfPortPortn_Type.__name__ = "Unsigned32"
_Pmo10010CfgSystConfPortPortn_Object = MibTableColumn
pmo10010CfgSystConfPortPortn = _Pmo10010CfgSystConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 2, 1, 1, 3),
    _Pmo10010CfgSystConfPortPortn_Type()
)
pmo10010CfgSystConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CfgSystConfPortPortn.setStatus("current")


class _Pmo10010CfgNetConfPortPortn_Type(Unsigned32):
    """Custom type pmo10010CfgNetConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmo10010CfgNetConfPortPortn_Type.__name__ = "Unsigned32"
_Pmo10010CfgNetConfPortPortn_Object = MibTableColumn
pmo10010CfgNetConfPortPortn = _Pmo10010CfgNetConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 2, 1, 1, 4),
    _Pmo10010CfgNetConfPortPortn_Type()
)
pmo10010CfgNetConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CfgNetConfPortPortn.setStatus("current")


class _Pmo10010CfgOptionsPortPortn_Type(Unsigned32):
    """Custom type pmo10010CfgOptionsPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmo10010CfgOptionsPortPortn_Type.__name__ = "Unsigned32"
_Pmo10010CfgOptionsPortPortn_Object = MibTableColumn
pmo10010CfgOptionsPortPortn = _Pmo10010CfgOptionsPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 2, 1, 1, 14),
    _Pmo10010CfgOptionsPortPortn_Type()
)
pmo10010CfgOptionsPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CfgOptionsPortPortn.setStatus("current")
_Pmo10010CfgLineStartupTable_Object = MibTable
pmo10010CfgLineStartupTable = _Pmo10010CfgLineStartupTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 2, 2)
)
if mibBuilder.loadTexts:
    pmo10010CfgLineStartupTable.setStatus("current")
_Pmo10010CfgLineStartupEntry_Object = MibTableRow
pmo10010CfgLineStartupEntry = _Pmo10010CfgLineStartupEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 2, 2, 1)
)
pmo10010CfgLineStartupEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010CfgLineStartupIndex"),
)
if mibBuilder.loadTexts:
    pmo10010CfgLineStartupEntry.setStatus("current")


class _Pmo10010CfgLineStartupIndex_Type(Integer32):
    """Custom type pmo10010CfgLineStartupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010CfgLineStartupIndex_Type.__name__ = "Integer32"
_Pmo10010CfgLineStartupIndex_Object = MibTableColumn
pmo10010CfgLineStartupIndex = _Pmo10010CfgLineStartupIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 2, 2, 1, 1),
    _Pmo10010CfgLineStartupIndex_Type()
)
pmo10010CfgLineStartupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CfgLineStartupIndex.setStatus("current")


class _Pmo10010CfgSystConfLinePortn_Type(Unsigned32):
    """Custom type pmo10010CfgSystConfLinePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmo10010CfgSystConfLinePortn_Type.__name__ = "Unsigned32"
_Pmo10010CfgSystConfLinePortn_Object = MibTableColumn
pmo10010CfgSystConfLinePortn = _Pmo10010CfgSystConfLinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 2, 2, 1, 3),
    _Pmo10010CfgSystConfLinePortn_Type()
)
pmo10010CfgSystConfLinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CfgSystConfLinePortn.setStatus("current")


class _Pmo10010CfgOptionsLinePortn_Type(Unsigned32):
    """Custom type pmo10010CfgOptionsLinePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmo10010CfgOptionsLinePortn_Type.__name__ = "Unsigned32"
_Pmo10010CfgOptionsLinePortn_Object = MibTableColumn
pmo10010CfgOptionsLinePortn = _Pmo10010CfgOptionsLinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 2, 2, 1, 14),
    _Pmo10010CfgOptionsLinePortn_Type()
)
pmo10010CfgOptionsLinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CfgOptionsLinePortn.setStatus("current")
_Pmo10010CfgXfpTable_Object = MibTable
pmo10010CfgXfpTable = _Pmo10010CfgXfpTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 2, 3)
)
if mibBuilder.loadTexts:
    pmo10010CfgXfpTable.setStatus("current")
_Pmo10010CfgXfpEntry_Object = MibTableRow
pmo10010CfgXfpEntry = _Pmo10010CfgXfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 2, 3, 1)
)
pmo10010CfgXfpEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010CfgXfpIndex"),
)
if mibBuilder.loadTexts:
    pmo10010CfgXfpEntry.setStatus("current")


class _Pmo10010CfgXfpIndex_Type(Integer32):
    """Custom type pmo10010CfgXfpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010CfgXfpIndex_Type.__name__ = "Integer32"
_Pmo10010CfgXfpIndex_Object = MibTableColumn
pmo10010CfgXfpIndex = _Pmo10010CfgXfpIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 2, 3, 1, 1),
    _Pmo10010CfgXfpIndex_Type()
)
pmo10010CfgXfpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CfgXfpIndex.setStatus("current")


class _Pmo10010CfgSystConfMsaLinePortn_Type(Unsigned32):
    """Custom type pmo10010CfgSystConfMsaLinePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmo10010CfgSystConfMsaLinePortn_Type.__name__ = "Unsigned32"
_Pmo10010CfgSystConfMsaLinePortn_Object = MibTableColumn
pmo10010CfgSystConfMsaLinePortn = _Pmo10010CfgSystConfMsaLinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 2, 3, 1, 3),
    _Pmo10010CfgSystConfMsaLinePortn_Type()
)
pmo10010CfgSystConfMsaLinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CfgSystConfMsaLinePortn.setStatus("current")
_Pmo10010CfgClientOtxtlhTable_Object = MibTable
pmo10010CfgClientOtxtlhTable = _Pmo10010CfgClientOtxtlhTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 2, 4)
)
if mibBuilder.loadTexts:
    pmo10010CfgClientOtxtlhTable.setStatus("current")
_Pmo10010CfgClientOtxtlhEntry_Object = MibTableRow
pmo10010CfgClientOtxtlhEntry = _Pmo10010CfgClientOtxtlhEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 2, 4, 1)
)
pmo10010CfgClientOtxtlhEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010CfgClientOtxtlhIndex"),
)
if mibBuilder.loadTexts:
    pmo10010CfgClientOtxtlhEntry.setStatus("current")


class _Pmo10010CfgClientOtxtlhIndex_Type(Integer32):
    """Custom type pmo10010CfgClientOtxtlhIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010CfgClientOtxtlhIndex_Type.__name__ = "Integer32"
_Pmo10010CfgClientOtxtlhIndex_Object = MibTableColumn
pmo10010CfgClientOtxtlhIndex = _Pmo10010CfgClientOtxtlhIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 2, 4, 1, 1),
    _Pmo10010CfgClientOtxtlhIndex_Type()
)
pmo10010CfgClientOtxtlhIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CfgClientOtxtlhIndex.setStatus("current")


class _Pmo10010CfgControlsPortn_Type(Unsigned32):
    """Custom type pmo10010CfgControlsPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmo10010CfgControlsPortn_Type.__name__ = "Unsigned32"
_Pmo10010CfgControlsPortn_Object = MibTableColumn
pmo10010CfgControlsPortn = _Pmo10010CfgControlsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 2, 4, 1, 3),
    _Pmo10010CfgControlsPortn_Type()
)
pmo10010CfgControlsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CfgControlsPortn.setStatus("deprecated")


class _Pmo10010CfgClientPwrLaserPortn_Type(Unsigned32):
    """Custom type pmo10010CfgClientPwrLaserPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmo10010CfgClientPwrLaserPortn_Type.__name__ = "Unsigned32"
_Pmo10010CfgClientPwrLaserPortn_Object = MibTableColumn
pmo10010CfgClientPwrLaserPortn = _Pmo10010CfgClientPwrLaserPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 2, 4, 1, 6),
    _Pmo10010CfgClientPwrLaserPortn_Type()
)
pmo10010CfgClientPwrLaserPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CfgClientPwrLaserPortn.setStatus("current")


class _Pmo10010CfgClientFCurrentPortn_Type(Unsigned32):
    """Custom type pmo10010CfgClientFCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmo10010CfgClientFCurrentPortn_Type.__name__ = "Unsigned32"
_Pmo10010CfgClientFCurrentPortn_Object = MibTableColumn
pmo10010CfgClientFCurrentPortn = _Pmo10010CfgClientFCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 2, 4, 1, 7),
    _Pmo10010CfgClientFCurrentPortn_Type()
)
pmo10010CfgClientFCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CfgClientFCurrentPortn.setStatus("current")


class _Pmo10010CfgClientGridCurrentPortn_Type(Unsigned32):
    """Custom type pmo10010CfgClientGridCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmo10010CfgClientGridCurrentPortn_Type.__name__ = "Unsigned32"
_Pmo10010CfgClientGridCurrentPortn_Object = MibTableColumn
pmo10010CfgClientGridCurrentPortn = _Pmo10010CfgClientGridCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 2, 4, 1, 8),
    _Pmo10010CfgClientGridCurrentPortn_Type()
)
pmo10010CfgClientGridCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CfgClientGridCurrentPortn.setStatus("current")


class _Pmo10010CfgClientFoPortn_Type(Unsigned32):
    """Custom type pmo10010CfgClientFoPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmo10010CfgClientFoPortn_Type.__name__ = "Unsigned32"
_Pmo10010CfgClientFoPortn_Object = MibTableColumn
pmo10010CfgClientFoPortn = _Pmo10010CfgClientFoPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 2, 4, 1, 9),
    _Pmo10010CfgClientFoPortn_Type()
)
pmo10010CfgClientFoPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CfgClientFoPortn.setStatus("current")
_Pmo10010CfgLabels_ObjectIdentity = ObjectIdentity
pmo10010CfgLabels = _Pmo10010CfgLabels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 3)
)
_Pmo10010CfgLabelclientTable_Object = MibTable
pmo10010CfgLabelclientTable = _Pmo10010CfgLabelclientTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 3, 1)
)
if mibBuilder.loadTexts:
    pmo10010CfgLabelclientTable.setStatus("current")
_Pmo10010CfgLabelclientEntry_Object = MibTableRow
pmo10010CfgLabelclientEntry = _Pmo10010CfgLabelclientEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 3, 1, 1)
)
pmo10010CfgLabelclientEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010CfgLabelclientIndex"),
)
if mibBuilder.loadTexts:
    pmo10010CfgLabelclientEntry.setStatus("current")


class _Pmo10010CfgLabelclientIndex_Type(Integer32):
    """Custom type pmo10010CfgLabelclientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010CfgLabelclientIndex_Type.__name__ = "Integer32"
_Pmo10010CfgLabelclientIndex_Object = MibTableColumn
pmo10010CfgLabelclientIndex = _Pmo10010CfgLabelclientIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 3, 1, 1, 1),
    _Pmo10010CfgLabelclientIndex_Type()
)
pmo10010CfgLabelclientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CfgLabelclientIndex.setStatus("current")


class _Pmo10010CfgLabelclientPortn_Type(DisplayString):
    """Custom type pmo10010CfgLabelclientPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pmo10010CfgLabelclientPortn_Type.__name__ = "DisplayString"
_Pmo10010CfgLabelclientPortn_Object = MibTableColumn
pmo10010CfgLabelclientPortn = _Pmo10010CfgLabelclientPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 3, 1, 1, 3),
    _Pmo10010CfgLabelclientPortn_Type()
)
pmo10010CfgLabelclientPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CfgLabelclientPortn.setStatus("current")
_Pmo10010CfgLabellineTable_Object = MibTable
pmo10010CfgLabellineTable = _Pmo10010CfgLabellineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 3, 2)
)
if mibBuilder.loadTexts:
    pmo10010CfgLabellineTable.setStatus("current")
_Pmo10010CfgLabellineEntry_Object = MibTableRow
pmo10010CfgLabellineEntry = _Pmo10010CfgLabellineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 3, 2, 1)
)
pmo10010CfgLabellineEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010CfgLabellineIndex"),
)
if mibBuilder.loadTexts:
    pmo10010CfgLabellineEntry.setStatus("current")


class _Pmo10010CfgLabellineIndex_Type(Integer32):
    """Custom type pmo10010CfgLabellineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010CfgLabellineIndex_Type.__name__ = "Integer32"
_Pmo10010CfgLabellineIndex_Object = MibTableColumn
pmo10010CfgLabellineIndex = _Pmo10010CfgLabellineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 3, 2, 1, 1),
    _Pmo10010CfgLabellineIndex_Type()
)
pmo10010CfgLabellineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CfgLabellineIndex.setStatus("current")


class _Pmo10010CfgLabellinePortn_Type(DisplayString):
    """Custom type pmo10010CfgLabellinePortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pmo10010CfgLabellinePortn_Type.__name__ = "DisplayString"
_Pmo10010CfgLabellinePortn_Object = MibTableColumn
pmo10010CfgLabellinePortn = _Pmo10010CfgLabellinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 3, 2, 1, 3),
    _Pmo10010CfgLabellinePortn_Type()
)
pmo10010CfgLabellinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CfgLabellinePortn.setStatus("current")
_Pmo10010CfgStartuptlh_ObjectIdentity = ObjectIdentity
pmo10010CfgStartuptlh = _Pmo10010CfgStartuptlh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 4)
)
_Pmo10010CfgOtxtlhTable_Object = MibTable
pmo10010CfgOtxtlhTable = _Pmo10010CfgOtxtlhTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 4, 1)
)
if mibBuilder.loadTexts:
    pmo10010CfgOtxtlhTable.setStatus("current")
_Pmo10010CfgOtxtlhEntry_Object = MibTableRow
pmo10010CfgOtxtlhEntry = _Pmo10010CfgOtxtlhEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 4, 1, 1)
)
pmo10010CfgOtxtlhEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010CfgOtxtlhIndex"),
)
if mibBuilder.loadTexts:
    pmo10010CfgOtxtlhEntry.setStatus("current")


class _Pmo10010CfgOtxtlhIndex_Type(Integer32):
    """Custom type pmo10010CfgOtxtlhIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010CfgOtxtlhIndex_Type.__name__ = "Integer32"
_Pmo10010CfgOtxtlhIndex_Object = MibTableColumn
pmo10010CfgOtxtlhIndex = _Pmo10010CfgOtxtlhIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 4, 1, 1, 1),
    _Pmo10010CfgOtxtlhIndex_Type()
)
pmo10010CfgOtxtlhIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CfgOtxtlhIndex.setStatus("current")


class _Pmo10010CfgLinePwrLaserPortn_Type(Unsigned32):
    """Custom type pmo10010CfgLinePwrLaserPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmo10010CfgLinePwrLaserPortn_Type.__name__ = "Unsigned32"
_Pmo10010CfgLinePwrLaserPortn_Object = MibTableColumn
pmo10010CfgLinePwrLaserPortn = _Pmo10010CfgLinePwrLaserPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 4, 1, 1, 6),
    _Pmo10010CfgLinePwrLaserPortn_Type()
)
pmo10010CfgLinePwrLaserPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CfgLinePwrLaserPortn.setStatus("current")


class _Pmo10010CfgLineFCurrentPortn_Type(Unsigned32):
    """Custom type pmo10010CfgLineFCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmo10010CfgLineFCurrentPortn_Type.__name__ = "Unsigned32"
_Pmo10010CfgLineFCurrentPortn_Object = MibTableColumn
pmo10010CfgLineFCurrentPortn = _Pmo10010CfgLineFCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 4, 1, 1, 7),
    _Pmo10010CfgLineFCurrentPortn_Type()
)
pmo10010CfgLineFCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CfgLineFCurrentPortn.setStatus("current")


class _Pmo10010CfgLineGridCurrentPortn_Type(Unsigned32):
    """Custom type pmo10010CfgLineGridCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmo10010CfgLineGridCurrentPortn_Type.__name__ = "Unsigned32"
_Pmo10010CfgLineGridCurrentPortn_Object = MibTableColumn
pmo10010CfgLineGridCurrentPortn = _Pmo10010CfgLineGridCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 4, 1, 1, 8),
    _Pmo10010CfgLineGridCurrentPortn_Type()
)
pmo10010CfgLineGridCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CfgLineGridCurrentPortn.setStatus("current")


class _Pmo10010CfgFPortn_Type(Unsigned32):
    """Custom type pmo10010CfgFPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmo10010CfgFPortn_Type.__name__ = "Unsigned32"
_Pmo10010CfgFPortn_Object = MibTableColumn
pmo10010CfgFPortn = _Pmo10010CfgFPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 4, 1, 1, 9),
    _Pmo10010CfgFPortn_Type()
)
pmo10010CfgFPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CfgFPortn.setStatus("current")


class _Pmo10010CfgRxLineFCurrentPortn_Type(Unsigned32):
    """Custom type pmo10010CfgRxLineFCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmo10010CfgRxLineFCurrentPortn_Type.__name__ = "Unsigned32"
_Pmo10010CfgRxLineFCurrentPortn_Object = MibTableColumn
pmo10010CfgRxLineFCurrentPortn = _Pmo10010CfgRxLineFCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 4, 1, 1, 10),
    _Pmo10010CfgRxLineFCurrentPortn_Type()
)
pmo10010CfgRxLineFCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CfgRxLineFCurrentPortn.setStatus("current")
_Pmo10010CfgOther_ObjectIdentity = ObjectIdentity
pmo10010CfgOther = _Pmo10010CfgOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 5)
)
_Pmo10010tablemoduleOther_ObjectIdentity = ObjectIdentity
pmo10010tablemoduleOther = _Pmo10010tablemoduleOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 5, 1)
)


class _Pmo10010Cfgmode_Type(Unsigned32):
    """Custom type pmo10010Cfgmode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmo10010Cfgmode_Type.__name__ = "Unsigned32"
_Pmo10010Cfgmode_Object = MibScalar
pmo10010Cfgmode = _Pmo10010Cfgmode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 5, 1, 2),
    _Pmo10010Cfgmode_Type()
)
pmo10010Cfgmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010Cfgmode.setStatus("current")


class _Pmo10010CfgfanLowSpeedThreshold_Type(Unsigned32):
    """Custom type pmo10010CfgfanLowSpeedThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmo10010CfgfanLowSpeedThreshold_Type.__name__ = "Unsigned32"
_Pmo10010CfgfanLowSpeedThreshold_Object = MibScalar
pmo10010CfgfanLowSpeedThreshold = _Pmo10010CfgfanLowSpeedThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 5, 1, 3),
    _Pmo10010CfgfanLowSpeedThreshold_Type()
)
pmo10010CfgfanLowSpeedThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CfgfanLowSpeedThreshold.setStatus("current")


class _Pmo10010CfgfanHighSpeedThreshold_Type(Unsigned32):
    """Custom type pmo10010CfgfanHighSpeedThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmo10010CfgfanHighSpeedThreshold_Type.__name__ = "Unsigned32"
_Pmo10010CfgfanHighSpeedThreshold_Object = MibScalar
pmo10010CfgfanHighSpeedThreshold = _Pmo10010CfgfanHighSpeedThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 5, 1, 4),
    _Pmo10010CfgfanHighSpeedThreshold_Type()
)
pmo10010CfgfanHighSpeedThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CfgfanHighSpeedThreshold.setStatus("current")
_Pmo10010CfgOdu2Clienta_ObjectIdentity = ObjectIdentity
pmo10010CfgOdu2Clienta = _Pmo10010CfgOdu2Clienta_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 6)
)
_Pmo10010CfgClientStartupOduTable_Object = MibTable
pmo10010CfgClientStartupOduTable = _Pmo10010CfgClientStartupOduTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 6, 1)
)
if mibBuilder.loadTexts:
    pmo10010CfgClientStartupOduTable.setStatus("current")
_Pmo10010CfgClientStartupOduEntry_Object = MibTableRow
pmo10010CfgClientStartupOduEntry = _Pmo10010CfgClientStartupOduEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 6, 1, 1)
)
pmo10010CfgClientStartupOduEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010CfgClientStartupOduIndex"),
)
if mibBuilder.loadTexts:
    pmo10010CfgClientStartupOduEntry.setStatus("current")


class _Pmo10010CfgClientStartupOduIndex_Type(Integer32):
    """Custom type pmo10010CfgClientStartupOduIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010CfgClientStartupOduIndex_Type.__name__ = "Integer32"
_Pmo10010CfgClientStartupOduIndex_Object = MibTableColumn
pmo10010CfgClientStartupOduIndex = _Pmo10010CfgClientStartupOduIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 6, 1, 1, 1),
    _Pmo10010CfgClientStartupOduIndex_Type()
)
pmo10010CfgClientStartupOduIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CfgClientStartupOduIndex.setStatus("current")


class _Pmo10010CfgOdu2ReserveLsbPortn_Type(Unsigned32):
    """Custom type pmo10010CfgOdu2ReserveLsbPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmo10010CfgOdu2ReserveLsbPortn_Type.__name__ = "Unsigned32"
_Pmo10010CfgOdu2ReserveLsbPortn_Object = MibTableColumn
pmo10010CfgOdu2ReserveLsbPortn = _Pmo10010CfgOdu2ReserveLsbPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 6, 1, 1, 3),
    _Pmo10010CfgOdu2ReserveLsbPortn_Type()
)
pmo10010CfgOdu2ReserveLsbPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CfgOdu2ReserveLsbPortn.setStatus("current")


class _Pmo10010CfgOdu2DegthresholdMsbPortn_Type(Unsigned32):
    """Custom type pmo10010CfgOdu2DegthresholdMsbPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmo10010CfgOdu2DegthresholdMsbPortn_Type.__name__ = "Unsigned32"
_Pmo10010CfgOdu2DegthresholdMsbPortn_Object = MibTableColumn
pmo10010CfgOdu2DegthresholdMsbPortn = _Pmo10010CfgOdu2DegthresholdMsbPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 6, 1, 1, 4),
    _Pmo10010CfgOdu2DegthresholdMsbPortn_Type()
)
pmo10010CfgOdu2DegthresholdMsbPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CfgOdu2DegthresholdMsbPortn.setStatus("current")


class _Pmo10010CfgOdu2DegmPortn_Type(Unsigned32):
    """Custom type pmo10010CfgOdu2DegmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmo10010CfgOdu2DegmPortn_Type.__name__ = "Unsigned32"
_Pmo10010CfgOdu2DegmPortn_Object = MibTableColumn
pmo10010CfgOdu2DegmPortn = _Pmo10010CfgOdu2DegmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 6, 1, 1, 5),
    _Pmo10010CfgOdu2DegmPortn_Type()
)
pmo10010CfgOdu2DegmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CfgOdu2DegmPortn.setStatus("current")


class _Pmo10010CfgOdu2SettingsPortn_Type(Unsigned32):
    """Custom type pmo10010CfgOdu2SettingsPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmo10010CfgOdu2SettingsPortn_Type.__name__ = "Unsigned32"
_Pmo10010CfgOdu2SettingsPortn_Object = MibTableColumn
pmo10010CfgOdu2SettingsPortn = _Pmo10010CfgOdu2SettingsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 6, 1, 1, 6),
    _Pmo10010CfgOdu2SettingsPortn_Type()
)
pmo10010CfgOdu2SettingsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CfgOdu2SettingsPortn.setStatus("current")
_Pmo10010CfgOtu4Line_ObjectIdentity = ObjectIdentity
pmo10010CfgOtu4Line = _Pmo10010CfgOtu4Line_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 7)
)
_Pmo10010CfgLinexStartupOtuTable_Object = MibTable
pmo10010CfgLinexStartupOtuTable = _Pmo10010CfgLinexStartupOtuTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 7, 1)
)
if mibBuilder.loadTexts:
    pmo10010CfgLinexStartupOtuTable.setStatus("current")
_Pmo10010CfgLinexStartupOtuEntry_Object = MibTableRow
pmo10010CfgLinexStartupOtuEntry = _Pmo10010CfgLinexStartupOtuEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 7, 1, 1)
)
pmo10010CfgLinexStartupOtuEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010CfgLinexStartupOtuIndex"),
)
if mibBuilder.loadTexts:
    pmo10010CfgLinexStartupOtuEntry.setStatus("current")


class _Pmo10010CfgLinexStartupOtuIndex_Type(Integer32):
    """Custom type pmo10010CfgLinexStartupOtuIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010CfgLinexStartupOtuIndex_Type.__name__ = "Integer32"
_Pmo10010CfgLinexStartupOtuIndex_Object = MibTableColumn
pmo10010CfgLinexStartupOtuIndex = _Pmo10010CfgLinexStartupOtuIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 7, 1, 1, 1),
    _Pmo10010CfgLinexStartupOtuIndex_Type()
)
pmo10010CfgLinexStartupOtuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CfgLinexStartupOtuIndex.setStatus("current")


class _Pmo10010CfgOtu4ReserveLsbPortn_Type(Unsigned32):
    """Custom type pmo10010CfgOtu4ReserveLsbPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmo10010CfgOtu4ReserveLsbPortn_Type.__name__ = "Unsigned32"
_Pmo10010CfgOtu4ReserveLsbPortn_Object = MibTableColumn
pmo10010CfgOtu4ReserveLsbPortn = _Pmo10010CfgOtu4ReserveLsbPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 7, 1, 1, 3),
    _Pmo10010CfgOtu4ReserveLsbPortn_Type()
)
pmo10010CfgOtu4ReserveLsbPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CfgOtu4ReserveLsbPortn.setStatus("current")


class _Pmo10010CfgOtu4DegthresholdMsbPortn_Type(Unsigned32):
    """Custom type pmo10010CfgOtu4DegthresholdMsbPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmo10010CfgOtu4DegthresholdMsbPortn_Type.__name__ = "Unsigned32"
_Pmo10010CfgOtu4DegthresholdMsbPortn_Object = MibTableColumn
pmo10010CfgOtu4DegthresholdMsbPortn = _Pmo10010CfgOtu4DegthresholdMsbPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 7, 1, 1, 4),
    _Pmo10010CfgOtu4DegthresholdMsbPortn_Type()
)
pmo10010CfgOtu4DegthresholdMsbPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CfgOtu4DegthresholdMsbPortn.setStatus("current")


class _Pmo10010CfgOtu4DegmPortn_Type(Unsigned32):
    """Custom type pmo10010CfgOtu4DegmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmo10010CfgOtu4DegmPortn_Type.__name__ = "Unsigned32"
_Pmo10010CfgOtu4DegmPortn_Object = MibTableColumn
pmo10010CfgOtu4DegmPortn = _Pmo10010CfgOtu4DegmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 7, 1, 1, 5),
    _Pmo10010CfgOtu4DegmPortn_Type()
)
pmo10010CfgOtu4DegmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CfgOtu4DegmPortn.setStatus("current")


class _Pmo10010CfgOtu4SettingsPortn_Type(Unsigned32):
    """Custom type pmo10010CfgOtu4SettingsPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmo10010CfgOtu4SettingsPortn_Type.__name__ = "Unsigned32"
_Pmo10010CfgOtu4SettingsPortn_Object = MibTableColumn
pmo10010CfgOtu4SettingsPortn = _Pmo10010CfgOtu4SettingsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 7, 1, 1, 6),
    _Pmo10010CfgOtu4SettingsPortn_Type()
)
pmo10010CfgOtu4SettingsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CfgOtu4SettingsPortn.setStatus("current")
_Pmo10010CfgOdu4Line_ObjectIdentity = ObjectIdentity
pmo10010CfgOdu4Line = _Pmo10010CfgOdu4Line_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 8)
)
_Pmo10010CfgLinexStartupOduTable_Object = MibTable
pmo10010CfgLinexStartupOduTable = _Pmo10010CfgLinexStartupOduTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 8, 1)
)
if mibBuilder.loadTexts:
    pmo10010CfgLinexStartupOduTable.setStatus("current")
_Pmo10010CfgLinexStartupOduEntry_Object = MibTableRow
pmo10010CfgLinexStartupOduEntry = _Pmo10010CfgLinexStartupOduEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 8, 1, 1)
)
pmo10010CfgLinexStartupOduEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010CfgLinexStartupOduIndex"),
)
if mibBuilder.loadTexts:
    pmo10010CfgLinexStartupOduEntry.setStatus("current")


class _Pmo10010CfgLinexStartupOduIndex_Type(Integer32):
    """Custom type pmo10010CfgLinexStartupOduIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010CfgLinexStartupOduIndex_Type.__name__ = "Integer32"
_Pmo10010CfgLinexStartupOduIndex_Object = MibTableColumn
pmo10010CfgLinexStartupOduIndex = _Pmo10010CfgLinexStartupOduIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 8, 1, 1, 1),
    _Pmo10010CfgLinexStartupOduIndex_Type()
)
pmo10010CfgLinexStartupOduIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CfgLinexStartupOduIndex.setStatus("current")


class _Pmo10010CfgOdu4ReserveLsbPortn_Type(Unsigned32):
    """Custom type pmo10010CfgOdu4ReserveLsbPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmo10010CfgOdu4ReserveLsbPortn_Type.__name__ = "Unsigned32"
_Pmo10010CfgOdu4ReserveLsbPortn_Object = MibTableColumn
pmo10010CfgOdu4ReserveLsbPortn = _Pmo10010CfgOdu4ReserveLsbPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 8, 1, 1, 3),
    _Pmo10010CfgOdu4ReserveLsbPortn_Type()
)
pmo10010CfgOdu4ReserveLsbPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CfgOdu4ReserveLsbPortn.setStatus("current")


class _Pmo10010CfgOdu4DegthresholdMsbPortn_Type(Unsigned32):
    """Custom type pmo10010CfgOdu4DegthresholdMsbPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmo10010CfgOdu4DegthresholdMsbPortn_Type.__name__ = "Unsigned32"
_Pmo10010CfgOdu4DegthresholdMsbPortn_Object = MibTableColumn
pmo10010CfgOdu4DegthresholdMsbPortn = _Pmo10010CfgOdu4DegthresholdMsbPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 8, 1, 1, 4),
    _Pmo10010CfgOdu4DegthresholdMsbPortn_Type()
)
pmo10010CfgOdu4DegthresholdMsbPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CfgOdu4DegthresholdMsbPortn.setStatus("current")


class _Pmo10010CfgOdu4DegmPortn_Type(Unsigned32):
    """Custom type pmo10010CfgOdu4DegmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmo10010CfgOdu4DegmPortn_Type.__name__ = "Unsigned32"
_Pmo10010CfgOdu4DegmPortn_Object = MibTableColumn
pmo10010CfgOdu4DegmPortn = _Pmo10010CfgOdu4DegmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 8, 1, 1, 5),
    _Pmo10010CfgOdu4DegmPortn_Type()
)
pmo10010CfgOdu4DegmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CfgOdu4DegmPortn.setStatus("current")


class _Pmo10010CfgOdu4SettingsPortn_Type(Unsigned32):
    """Custom type pmo10010CfgOdu4SettingsPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmo10010CfgOdu4SettingsPortn_Type.__name__ = "Unsigned32"
_Pmo10010CfgOdu4SettingsPortn_Object = MibTableColumn
pmo10010CfgOdu4SettingsPortn = _Pmo10010CfgOdu4SettingsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 8, 1, 1, 6),
    _Pmo10010CfgOdu4SettingsPortn_Type()
)
pmo10010CfgOdu4SettingsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CfgOdu4SettingsPortn.setStatus("current")
_Pmo10010CfgSapiTxClient_ObjectIdentity = ObjectIdentity
pmo10010CfgSapiTxClient = _Pmo10010CfgSapiTxClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 9)
)
_Pmo10010CfgClientSapiTxOduTable_Object = MibTable
pmo10010CfgClientSapiTxOduTable = _Pmo10010CfgClientSapiTxOduTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 9, 1)
)
if mibBuilder.loadTexts:
    pmo10010CfgClientSapiTxOduTable.setStatus("current")
_Pmo10010CfgClientSapiTxOduEntry_Object = MibTableRow
pmo10010CfgClientSapiTxOduEntry = _Pmo10010CfgClientSapiTxOduEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 9, 1, 1)
)
pmo10010CfgClientSapiTxOduEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010CfgClientSapiTxOduIndex"),
)
if mibBuilder.loadTexts:
    pmo10010CfgClientSapiTxOduEntry.setStatus("current")


class _Pmo10010CfgClientSapiTxOduIndex_Type(Integer32):
    """Custom type pmo10010CfgClientSapiTxOduIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010CfgClientSapiTxOduIndex_Type.__name__ = "Integer32"
_Pmo10010CfgClientSapiTxOduIndex_Object = MibTableColumn
pmo10010CfgClientSapiTxOduIndex = _Pmo10010CfgClientSapiTxOduIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 9, 1, 1, 1),
    _Pmo10010CfgClientSapiTxOduIndex_Type()
)
pmo10010CfgClientSapiTxOduIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CfgClientSapiTxOduIndex.setStatus("current")


class _Pmo10010CfgClientSapiTxSetupPortn_Type(DisplayString):
    """Custom type pmo10010CfgClientSapiTxSetupPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pmo10010CfgClientSapiTxSetupPortn_Type.__name__ = "DisplayString"
_Pmo10010CfgClientSapiTxSetupPortn_Object = MibTableColumn
pmo10010CfgClientSapiTxSetupPortn = _Pmo10010CfgClientSapiTxSetupPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 9, 1, 1, 3),
    _Pmo10010CfgClientSapiTxSetupPortn_Type()
)
pmo10010CfgClientSapiTxSetupPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CfgClientSapiTxSetupPortn.setStatus("current")
_Pmo10010CfgSapiExpClient_ObjectIdentity = ObjectIdentity
pmo10010CfgSapiExpClient = _Pmo10010CfgSapiExpClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 10)
)
_Pmo10010CfgClientSapiExpOduTable_Object = MibTable
pmo10010CfgClientSapiExpOduTable = _Pmo10010CfgClientSapiExpOduTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 10, 1)
)
if mibBuilder.loadTexts:
    pmo10010CfgClientSapiExpOduTable.setStatus("current")
_Pmo10010CfgClientSapiExpOduEntry_Object = MibTableRow
pmo10010CfgClientSapiExpOduEntry = _Pmo10010CfgClientSapiExpOduEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 10, 1, 1)
)
pmo10010CfgClientSapiExpOduEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010CfgClientSapiExpOduIndex"),
)
if mibBuilder.loadTexts:
    pmo10010CfgClientSapiExpOduEntry.setStatus("current")


class _Pmo10010CfgClientSapiExpOduIndex_Type(Integer32):
    """Custom type pmo10010CfgClientSapiExpOduIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010CfgClientSapiExpOduIndex_Type.__name__ = "Integer32"
_Pmo10010CfgClientSapiExpOduIndex_Object = MibTableColumn
pmo10010CfgClientSapiExpOduIndex = _Pmo10010CfgClientSapiExpOduIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 10, 1, 1, 1),
    _Pmo10010CfgClientSapiExpOduIndex_Type()
)
pmo10010CfgClientSapiExpOduIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CfgClientSapiExpOduIndex.setStatus("current")


class _Pmo10010CfgClientSapiExpSetupPortn_Type(DisplayString):
    """Custom type pmo10010CfgClientSapiExpSetupPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pmo10010CfgClientSapiExpSetupPortn_Type.__name__ = "DisplayString"
_Pmo10010CfgClientSapiExpSetupPortn_Object = MibTableColumn
pmo10010CfgClientSapiExpSetupPortn = _Pmo10010CfgClientSapiExpSetupPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 10, 1, 1, 3),
    _Pmo10010CfgClientSapiExpSetupPortn_Type()
)
pmo10010CfgClientSapiExpSetupPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CfgClientSapiExpSetupPortn.setStatus("current")
_Pmo10010CfgSapiAccClient_ObjectIdentity = ObjectIdentity
pmo10010CfgSapiAccClient = _Pmo10010CfgSapiAccClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 11)
)
_Pmo10010CfgClientSapiAccOduTable_Object = MibTable
pmo10010CfgClientSapiAccOduTable = _Pmo10010CfgClientSapiAccOduTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 11, 1)
)
if mibBuilder.loadTexts:
    pmo10010CfgClientSapiAccOduTable.setStatus("current")
_Pmo10010CfgClientSapiAccOduEntry_Object = MibTableRow
pmo10010CfgClientSapiAccOduEntry = _Pmo10010CfgClientSapiAccOduEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 11, 1, 1)
)
pmo10010CfgClientSapiAccOduEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010CfgClientSapiAccOduIndex"),
)
if mibBuilder.loadTexts:
    pmo10010CfgClientSapiAccOduEntry.setStatus("current")


class _Pmo10010CfgClientSapiAccOduIndex_Type(Integer32):
    """Custom type pmo10010CfgClientSapiAccOduIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010CfgClientSapiAccOduIndex_Type.__name__ = "Integer32"
_Pmo10010CfgClientSapiAccOduIndex_Object = MibTableColumn
pmo10010CfgClientSapiAccOduIndex = _Pmo10010CfgClientSapiAccOduIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 11, 1, 1, 1),
    _Pmo10010CfgClientSapiAccOduIndex_Type()
)
pmo10010CfgClientSapiAccOduIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CfgClientSapiAccOduIndex.setStatus("current")


class _Pmo10010CfgClientSapiAccSetupPortn_Type(DisplayString):
    """Custom type pmo10010CfgClientSapiAccSetupPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pmo10010CfgClientSapiAccSetupPortn_Type.__name__ = "DisplayString"
_Pmo10010CfgClientSapiAccSetupPortn_Object = MibTableColumn
pmo10010CfgClientSapiAccSetupPortn = _Pmo10010CfgClientSapiAccSetupPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 11, 1, 1, 3),
    _Pmo10010CfgClientSapiAccSetupPortn_Type()
)
pmo10010CfgClientSapiAccSetupPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CfgClientSapiAccSetupPortn.setStatus("deprecated")
_Pmo10010CfgDapiTxClient_ObjectIdentity = ObjectIdentity
pmo10010CfgDapiTxClient = _Pmo10010CfgDapiTxClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 12)
)
_Pmo10010CfgClientDapiTxOduTable_Object = MibTable
pmo10010CfgClientDapiTxOduTable = _Pmo10010CfgClientDapiTxOduTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 12, 1)
)
if mibBuilder.loadTexts:
    pmo10010CfgClientDapiTxOduTable.setStatus("current")
_Pmo10010CfgClientDapiTxOduEntry_Object = MibTableRow
pmo10010CfgClientDapiTxOduEntry = _Pmo10010CfgClientDapiTxOduEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 12, 1, 1)
)
pmo10010CfgClientDapiTxOduEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010CfgClientDapiTxOduIndex"),
)
if mibBuilder.loadTexts:
    pmo10010CfgClientDapiTxOduEntry.setStatus("current")


class _Pmo10010CfgClientDapiTxOduIndex_Type(Integer32):
    """Custom type pmo10010CfgClientDapiTxOduIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010CfgClientDapiTxOduIndex_Type.__name__ = "Integer32"
_Pmo10010CfgClientDapiTxOduIndex_Object = MibTableColumn
pmo10010CfgClientDapiTxOduIndex = _Pmo10010CfgClientDapiTxOduIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 12, 1, 1, 1),
    _Pmo10010CfgClientDapiTxOduIndex_Type()
)
pmo10010CfgClientDapiTxOduIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CfgClientDapiTxOduIndex.setStatus("current")


class _Pmo10010CfgClientDapiTxSetupPortn_Type(DisplayString):
    """Custom type pmo10010CfgClientDapiTxSetupPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pmo10010CfgClientDapiTxSetupPortn_Type.__name__ = "DisplayString"
_Pmo10010CfgClientDapiTxSetupPortn_Object = MibTableColumn
pmo10010CfgClientDapiTxSetupPortn = _Pmo10010CfgClientDapiTxSetupPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 12, 1, 1, 3),
    _Pmo10010CfgClientDapiTxSetupPortn_Type()
)
pmo10010CfgClientDapiTxSetupPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CfgClientDapiTxSetupPortn.setStatus("current")
_Pmo10010CfgDapiExpClient_ObjectIdentity = ObjectIdentity
pmo10010CfgDapiExpClient = _Pmo10010CfgDapiExpClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 13)
)
_Pmo10010CfgClientDapiExpOduTable_Object = MibTable
pmo10010CfgClientDapiExpOduTable = _Pmo10010CfgClientDapiExpOduTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 13, 1)
)
if mibBuilder.loadTexts:
    pmo10010CfgClientDapiExpOduTable.setStatus("current")
_Pmo10010CfgClientDapiExpOduEntry_Object = MibTableRow
pmo10010CfgClientDapiExpOduEntry = _Pmo10010CfgClientDapiExpOduEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 13, 1, 1)
)
pmo10010CfgClientDapiExpOduEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010CfgClientDapiExpOduIndex"),
)
if mibBuilder.loadTexts:
    pmo10010CfgClientDapiExpOduEntry.setStatus("current")


class _Pmo10010CfgClientDapiExpOduIndex_Type(Integer32):
    """Custom type pmo10010CfgClientDapiExpOduIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010CfgClientDapiExpOduIndex_Type.__name__ = "Integer32"
_Pmo10010CfgClientDapiExpOduIndex_Object = MibTableColumn
pmo10010CfgClientDapiExpOduIndex = _Pmo10010CfgClientDapiExpOduIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 13, 1, 1, 1),
    _Pmo10010CfgClientDapiExpOduIndex_Type()
)
pmo10010CfgClientDapiExpOduIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CfgClientDapiExpOduIndex.setStatus("current")


class _Pmo10010CfgClientDapiExpSetupPortn_Type(DisplayString):
    """Custom type pmo10010CfgClientDapiExpSetupPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pmo10010CfgClientDapiExpSetupPortn_Type.__name__ = "DisplayString"
_Pmo10010CfgClientDapiExpSetupPortn_Object = MibTableColumn
pmo10010CfgClientDapiExpSetupPortn = _Pmo10010CfgClientDapiExpSetupPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 13, 1, 1, 3),
    _Pmo10010CfgClientDapiExpSetupPortn_Type()
)
pmo10010CfgClientDapiExpSetupPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CfgClientDapiExpSetupPortn.setStatus("current")
_Pmo10010CfgDapiAccClient_ObjectIdentity = ObjectIdentity
pmo10010CfgDapiAccClient = _Pmo10010CfgDapiAccClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 14)
)
_Pmo10010CfgClientDapiAccOduTable_Object = MibTable
pmo10010CfgClientDapiAccOduTable = _Pmo10010CfgClientDapiAccOduTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 14, 1)
)
if mibBuilder.loadTexts:
    pmo10010CfgClientDapiAccOduTable.setStatus("current")
_Pmo10010CfgClientDapiAccOduEntry_Object = MibTableRow
pmo10010CfgClientDapiAccOduEntry = _Pmo10010CfgClientDapiAccOduEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 14, 1, 1)
)
pmo10010CfgClientDapiAccOduEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010CfgClientDapiAccOduIndex"),
)
if mibBuilder.loadTexts:
    pmo10010CfgClientDapiAccOduEntry.setStatus("current")


class _Pmo10010CfgClientDapiAccOduIndex_Type(Integer32):
    """Custom type pmo10010CfgClientDapiAccOduIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010CfgClientDapiAccOduIndex_Type.__name__ = "Integer32"
_Pmo10010CfgClientDapiAccOduIndex_Object = MibTableColumn
pmo10010CfgClientDapiAccOduIndex = _Pmo10010CfgClientDapiAccOduIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 14, 1, 1, 1),
    _Pmo10010CfgClientDapiAccOduIndex_Type()
)
pmo10010CfgClientDapiAccOduIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CfgClientDapiAccOduIndex.setStatus("current")


class _Pmo10010CfgClientDapiAccSetupPortn_Type(DisplayString):
    """Custom type pmo10010CfgClientDapiAccSetupPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pmo10010CfgClientDapiAccSetupPortn_Type.__name__ = "DisplayString"
_Pmo10010CfgClientDapiAccSetupPortn_Object = MibTableColumn
pmo10010CfgClientDapiAccSetupPortn = _Pmo10010CfgClientDapiAccSetupPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 14, 1, 1, 3),
    _Pmo10010CfgClientDapiAccSetupPortn_Type()
)
pmo10010CfgClientDapiAccSetupPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CfgClientDapiAccSetupPortn.setStatus("deprecated")
_Pmo10010CfgSapiTxLineOtu4_ObjectIdentity = ObjectIdentity
pmo10010CfgSapiTxLineOtu4 = _Pmo10010CfgSapiTxLineOtu4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 15)
)
_Pmo10010CfgLineSapiTxOtuTable_Object = MibTable
pmo10010CfgLineSapiTxOtuTable = _Pmo10010CfgLineSapiTxOtuTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 15, 1)
)
if mibBuilder.loadTexts:
    pmo10010CfgLineSapiTxOtuTable.setStatus("current")
_Pmo10010CfgLineSapiTxOtuEntry_Object = MibTableRow
pmo10010CfgLineSapiTxOtuEntry = _Pmo10010CfgLineSapiTxOtuEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 15, 1, 1)
)
pmo10010CfgLineSapiTxOtuEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010CfgLineSapiTxOtuIndex"),
)
if mibBuilder.loadTexts:
    pmo10010CfgLineSapiTxOtuEntry.setStatus("current")


class _Pmo10010CfgLineSapiTxOtuIndex_Type(Integer32):
    """Custom type pmo10010CfgLineSapiTxOtuIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010CfgLineSapiTxOtuIndex_Type.__name__ = "Integer32"
_Pmo10010CfgLineSapiTxOtuIndex_Object = MibTableColumn
pmo10010CfgLineSapiTxOtuIndex = _Pmo10010CfgLineSapiTxOtuIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 15, 1, 1, 1),
    _Pmo10010CfgLineSapiTxOtuIndex_Type()
)
pmo10010CfgLineSapiTxOtuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CfgLineSapiTxOtuIndex.setStatus("current")


class _Pmo10010CfgLineSapiTxSetupOtuPortn_Type(DisplayString):
    """Custom type pmo10010CfgLineSapiTxSetupOtuPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pmo10010CfgLineSapiTxSetupOtuPortn_Type.__name__ = "DisplayString"
_Pmo10010CfgLineSapiTxSetupOtuPortn_Object = MibTableColumn
pmo10010CfgLineSapiTxSetupOtuPortn = _Pmo10010CfgLineSapiTxSetupOtuPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 15, 1, 1, 3),
    _Pmo10010CfgLineSapiTxSetupOtuPortn_Type()
)
pmo10010CfgLineSapiTxSetupOtuPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CfgLineSapiTxSetupOtuPortn.setStatus("current")
_Pmo10010CfgSapiExpLineOtu4_ObjectIdentity = ObjectIdentity
pmo10010CfgSapiExpLineOtu4 = _Pmo10010CfgSapiExpLineOtu4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 16)
)
_Pmo10010CfgLineSapiExpOtuTable_Object = MibTable
pmo10010CfgLineSapiExpOtuTable = _Pmo10010CfgLineSapiExpOtuTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 16, 1)
)
if mibBuilder.loadTexts:
    pmo10010CfgLineSapiExpOtuTable.setStatus("current")
_Pmo10010CfgLineSapiExpOtuEntry_Object = MibTableRow
pmo10010CfgLineSapiExpOtuEntry = _Pmo10010CfgLineSapiExpOtuEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 16, 1, 1)
)
pmo10010CfgLineSapiExpOtuEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010CfgLineSapiExpOtuIndex"),
)
if mibBuilder.loadTexts:
    pmo10010CfgLineSapiExpOtuEntry.setStatus("current")


class _Pmo10010CfgLineSapiExpOtuIndex_Type(Integer32):
    """Custom type pmo10010CfgLineSapiExpOtuIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010CfgLineSapiExpOtuIndex_Type.__name__ = "Integer32"
_Pmo10010CfgLineSapiExpOtuIndex_Object = MibTableColumn
pmo10010CfgLineSapiExpOtuIndex = _Pmo10010CfgLineSapiExpOtuIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 16, 1, 1, 1),
    _Pmo10010CfgLineSapiExpOtuIndex_Type()
)
pmo10010CfgLineSapiExpOtuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CfgLineSapiExpOtuIndex.setStatus("current")


class _Pmo10010CfgLineSapiExpSetupOtuPortn_Type(DisplayString):
    """Custom type pmo10010CfgLineSapiExpSetupOtuPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pmo10010CfgLineSapiExpSetupOtuPortn_Type.__name__ = "DisplayString"
_Pmo10010CfgLineSapiExpSetupOtuPortn_Object = MibTableColumn
pmo10010CfgLineSapiExpSetupOtuPortn = _Pmo10010CfgLineSapiExpSetupOtuPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 16, 1, 1, 3),
    _Pmo10010CfgLineSapiExpSetupOtuPortn_Type()
)
pmo10010CfgLineSapiExpSetupOtuPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CfgLineSapiExpSetupOtuPortn.setStatus("current")
_Pmo10010CfgSapiAccLineOtu4_ObjectIdentity = ObjectIdentity
pmo10010CfgSapiAccLineOtu4 = _Pmo10010CfgSapiAccLineOtu4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 17)
)
_Pmo10010CfgLineSapiAccOtuTable_Object = MibTable
pmo10010CfgLineSapiAccOtuTable = _Pmo10010CfgLineSapiAccOtuTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 17, 1)
)
if mibBuilder.loadTexts:
    pmo10010CfgLineSapiAccOtuTable.setStatus("current")
_Pmo10010CfgLineSapiAccOtuEntry_Object = MibTableRow
pmo10010CfgLineSapiAccOtuEntry = _Pmo10010CfgLineSapiAccOtuEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 17, 1, 1)
)
pmo10010CfgLineSapiAccOtuEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010CfgLineSapiAccOtuIndex"),
)
if mibBuilder.loadTexts:
    pmo10010CfgLineSapiAccOtuEntry.setStatus("current")


class _Pmo10010CfgLineSapiAccOtuIndex_Type(Integer32):
    """Custom type pmo10010CfgLineSapiAccOtuIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010CfgLineSapiAccOtuIndex_Type.__name__ = "Integer32"
_Pmo10010CfgLineSapiAccOtuIndex_Object = MibTableColumn
pmo10010CfgLineSapiAccOtuIndex = _Pmo10010CfgLineSapiAccOtuIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 17, 1, 1, 1),
    _Pmo10010CfgLineSapiAccOtuIndex_Type()
)
pmo10010CfgLineSapiAccOtuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CfgLineSapiAccOtuIndex.setStatus("current")


class _Pmo10010CfgLineSapiAccSetupOtuPortn_Type(DisplayString):
    """Custom type pmo10010CfgLineSapiAccSetupOtuPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pmo10010CfgLineSapiAccSetupOtuPortn_Type.__name__ = "DisplayString"
_Pmo10010CfgLineSapiAccSetupOtuPortn_Object = MibTableColumn
pmo10010CfgLineSapiAccSetupOtuPortn = _Pmo10010CfgLineSapiAccSetupOtuPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 17, 1, 1, 3),
    _Pmo10010CfgLineSapiAccSetupOtuPortn_Type()
)
pmo10010CfgLineSapiAccSetupOtuPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CfgLineSapiAccSetupOtuPortn.setStatus("deprecated")
_Pmo10010CfgDapiTxLineOtu4_ObjectIdentity = ObjectIdentity
pmo10010CfgDapiTxLineOtu4 = _Pmo10010CfgDapiTxLineOtu4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 18)
)
_Pmo10010CfgLineDapiTxOtuTable_Object = MibTable
pmo10010CfgLineDapiTxOtuTable = _Pmo10010CfgLineDapiTxOtuTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 18, 1)
)
if mibBuilder.loadTexts:
    pmo10010CfgLineDapiTxOtuTable.setStatus("current")
_Pmo10010CfgLineDapiTxOtuEntry_Object = MibTableRow
pmo10010CfgLineDapiTxOtuEntry = _Pmo10010CfgLineDapiTxOtuEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 18, 1, 1)
)
pmo10010CfgLineDapiTxOtuEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010CfgLineDapiTxOtuIndex"),
)
if mibBuilder.loadTexts:
    pmo10010CfgLineDapiTxOtuEntry.setStatus("current")


class _Pmo10010CfgLineDapiTxOtuIndex_Type(Integer32):
    """Custom type pmo10010CfgLineDapiTxOtuIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010CfgLineDapiTxOtuIndex_Type.__name__ = "Integer32"
_Pmo10010CfgLineDapiTxOtuIndex_Object = MibTableColumn
pmo10010CfgLineDapiTxOtuIndex = _Pmo10010CfgLineDapiTxOtuIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 18, 1, 1, 1),
    _Pmo10010CfgLineDapiTxOtuIndex_Type()
)
pmo10010CfgLineDapiTxOtuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CfgLineDapiTxOtuIndex.setStatus("current")


class _Pmo10010CfgLineDapiTxSetupOtuPortn_Type(DisplayString):
    """Custom type pmo10010CfgLineDapiTxSetupOtuPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pmo10010CfgLineDapiTxSetupOtuPortn_Type.__name__ = "DisplayString"
_Pmo10010CfgLineDapiTxSetupOtuPortn_Object = MibTableColumn
pmo10010CfgLineDapiTxSetupOtuPortn = _Pmo10010CfgLineDapiTxSetupOtuPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 18, 1, 1, 3),
    _Pmo10010CfgLineDapiTxSetupOtuPortn_Type()
)
pmo10010CfgLineDapiTxSetupOtuPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CfgLineDapiTxSetupOtuPortn.setStatus("current")
_Pmo10010CfgDapiExpLineOtu4_ObjectIdentity = ObjectIdentity
pmo10010CfgDapiExpLineOtu4 = _Pmo10010CfgDapiExpLineOtu4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 19)
)
_Pmo10010CfgLineDapiExpOtuTable_Object = MibTable
pmo10010CfgLineDapiExpOtuTable = _Pmo10010CfgLineDapiExpOtuTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 19, 1)
)
if mibBuilder.loadTexts:
    pmo10010CfgLineDapiExpOtuTable.setStatus("current")
_Pmo10010CfgLineDapiExpOtuEntry_Object = MibTableRow
pmo10010CfgLineDapiExpOtuEntry = _Pmo10010CfgLineDapiExpOtuEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 19, 1, 1)
)
pmo10010CfgLineDapiExpOtuEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010CfgLineDapiExpOtuIndex"),
)
if mibBuilder.loadTexts:
    pmo10010CfgLineDapiExpOtuEntry.setStatus("current")


class _Pmo10010CfgLineDapiExpOtuIndex_Type(Integer32):
    """Custom type pmo10010CfgLineDapiExpOtuIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010CfgLineDapiExpOtuIndex_Type.__name__ = "Integer32"
_Pmo10010CfgLineDapiExpOtuIndex_Object = MibTableColumn
pmo10010CfgLineDapiExpOtuIndex = _Pmo10010CfgLineDapiExpOtuIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 19, 1, 1, 1),
    _Pmo10010CfgLineDapiExpOtuIndex_Type()
)
pmo10010CfgLineDapiExpOtuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CfgLineDapiExpOtuIndex.setStatus("current")


class _Pmo10010CfgLineDapiExpSetupOtuPortn_Type(DisplayString):
    """Custom type pmo10010CfgLineDapiExpSetupOtuPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pmo10010CfgLineDapiExpSetupOtuPortn_Type.__name__ = "DisplayString"
_Pmo10010CfgLineDapiExpSetupOtuPortn_Object = MibTableColumn
pmo10010CfgLineDapiExpSetupOtuPortn = _Pmo10010CfgLineDapiExpSetupOtuPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 19, 1, 1, 3),
    _Pmo10010CfgLineDapiExpSetupOtuPortn_Type()
)
pmo10010CfgLineDapiExpSetupOtuPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CfgLineDapiExpSetupOtuPortn.setStatus("current")
_Pmo10010CfgDapiAccLineOtu4_ObjectIdentity = ObjectIdentity
pmo10010CfgDapiAccLineOtu4 = _Pmo10010CfgDapiAccLineOtu4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 20)
)
_Pmo10010CfgLineDapiAccOtuTable_Object = MibTable
pmo10010CfgLineDapiAccOtuTable = _Pmo10010CfgLineDapiAccOtuTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 20, 1)
)
if mibBuilder.loadTexts:
    pmo10010CfgLineDapiAccOtuTable.setStatus("current")
_Pmo10010CfgLineDapiAccOtuEntry_Object = MibTableRow
pmo10010CfgLineDapiAccOtuEntry = _Pmo10010CfgLineDapiAccOtuEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 20, 1, 1)
)
pmo10010CfgLineDapiAccOtuEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010CfgLineDapiAccOtuIndex"),
)
if mibBuilder.loadTexts:
    pmo10010CfgLineDapiAccOtuEntry.setStatus("current")


class _Pmo10010CfgLineDapiAccOtuIndex_Type(Integer32):
    """Custom type pmo10010CfgLineDapiAccOtuIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010CfgLineDapiAccOtuIndex_Type.__name__ = "Integer32"
_Pmo10010CfgLineDapiAccOtuIndex_Object = MibTableColumn
pmo10010CfgLineDapiAccOtuIndex = _Pmo10010CfgLineDapiAccOtuIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 20, 1, 1, 1),
    _Pmo10010CfgLineDapiAccOtuIndex_Type()
)
pmo10010CfgLineDapiAccOtuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CfgLineDapiAccOtuIndex.setStatus("current")


class _Pmo10010CfgLineDapiAccSetupOtuPortn_Type(DisplayString):
    """Custom type pmo10010CfgLineDapiAccSetupOtuPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pmo10010CfgLineDapiAccSetupOtuPortn_Type.__name__ = "DisplayString"
_Pmo10010CfgLineDapiAccSetupOtuPortn_Object = MibTableColumn
pmo10010CfgLineDapiAccSetupOtuPortn = _Pmo10010CfgLineDapiAccSetupOtuPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 20, 1, 1, 3),
    _Pmo10010CfgLineDapiAccSetupOtuPortn_Type()
)
pmo10010CfgLineDapiAccSetupOtuPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CfgLineDapiAccSetupOtuPortn.setStatus("deprecated")
_Pmo10010CfgSapiTxLineOdu4_ObjectIdentity = ObjectIdentity
pmo10010CfgSapiTxLineOdu4 = _Pmo10010CfgSapiTxLineOdu4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 21)
)
_Pmo10010CfgLineSapiTxOduTable_Object = MibTable
pmo10010CfgLineSapiTxOduTable = _Pmo10010CfgLineSapiTxOduTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 21, 1)
)
if mibBuilder.loadTexts:
    pmo10010CfgLineSapiTxOduTable.setStatus("current")
_Pmo10010CfgLineSapiTxOduEntry_Object = MibTableRow
pmo10010CfgLineSapiTxOduEntry = _Pmo10010CfgLineSapiTxOduEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 21, 1, 1)
)
pmo10010CfgLineSapiTxOduEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010CfgLineSapiTxOduIndex"),
)
if mibBuilder.loadTexts:
    pmo10010CfgLineSapiTxOduEntry.setStatus("current")


class _Pmo10010CfgLineSapiTxOduIndex_Type(Integer32):
    """Custom type pmo10010CfgLineSapiTxOduIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010CfgLineSapiTxOduIndex_Type.__name__ = "Integer32"
_Pmo10010CfgLineSapiTxOduIndex_Object = MibTableColumn
pmo10010CfgLineSapiTxOduIndex = _Pmo10010CfgLineSapiTxOduIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 21, 1, 1, 1),
    _Pmo10010CfgLineSapiTxOduIndex_Type()
)
pmo10010CfgLineSapiTxOduIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CfgLineSapiTxOduIndex.setStatus("current")


class _Pmo10010CfgLineSapiTxSetupOduPortn_Type(DisplayString):
    """Custom type pmo10010CfgLineSapiTxSetupOduPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pmo10010CfgLineSapiTxSetupOduPortn_Type.__name__ = "DisplayString"
_Pmo10010CfgLineSapiTxSetupOduPortn_Object = MibTableColumn
pmo10010CfgLineSapiTxSetupOduPortn = _Pmo10010CfgLineSapiTxSetupOduPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 21, 1, 1, 3),
    _Pmo10010CfgLineSapiTxSetupOduPortn_Type()
)
pmo10010CfgLineSapiTxSetupOduPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CfgLineSapiTxSetupOduPortn.setStatus("current")
_Pmo10010CfgSapiExpLineOdu4_ObjectIdentity = ObjectIdentity
pmo10010CfgSapiExpLineOdu4 = _Pmo10010CfgSapiExpLineOdu4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 22)
)
_Pmo10010CfgLineSapiExpOduTable_Object = MibTable
pmo10010CfgLineSapiExpOduTable = _Pmo10010CfgLineSapiExpOduTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 22, 1)
)
if mibBuilder.loadTexts:
    pmo10010CfgLineSapiExpOduTable.setStatus("current")
_Pmo10010CfgLineSapiExpOduEntry_Object = MibTableRow
pmo10010CfgLineSapiExpOduEntry = _Pmo10010CfgLineSapiExpOduEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 22, 1, 1)
)
pmo10010CfgLineSapiExpOduEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010CfgLineSapiExpOduIndex"),
)
if mibBuilder.loadTexts:
    pmo10010CfgLineSapiExpOduEntry.setStatus("current")


class _Pmo10010CfgLineSapiExpOduIndex_Type(Integer32):
    """Custom type pmo10010CfgLineSapiExpOduIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010CfgLineSapiExpOduIndex_Type.__name__ = "Integer32"
_Pmo10010CfgLineSapiExpOduIndex_Object = MibTableColumn
pmo10010CfgLineSapiExpOduIndex = _Pmo10010CfgLineSapiExpOduIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 22, 1, 1, 1),
    _Pmo10010CfgLineSapiExpOduIndex_Type()
)
pmo10010CfgLineSapiExpOduIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CfgLineSapiExpOduIndex.setStatus("current")


class _Pmo10010CfgLineSapiExpSetupOduPortn_Type(DisplayString):
    """Custom type pmo10010CfgLineSapiExpSetupOduPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pmo10010CfgLineSapiExpSetupOduPortn_Type.__name__ = "DisplayString"
_Pmo10010CfgLineSapiExpSetupOduPortn_Object = MibTableColumn
pmo10010CfgLineSapiExpSetupOduPortn = _Pmo10010CfgLineSapiExpSetupOduPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 22, 1, 1, 3),
    _Pmo10010CfgLineSapiExpSetupOduPortn_Type()
)
pmo10010CfgLineSapiExpSetupOduPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CfgLineSapiExpSetupOduPortn.setStatus("current")
_Pmo10010CfgSapiAccLineOdu4_ObjectIdentity = ObjectIdentity
pmo10010CfgSapiAccLineOdu4 = _Pmo10010CfgSapiAccLineOdu4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 23)
)
_Pmo10010CfgLineSapiAccOduTable_Object = MibTable
pmo10010CfgLineSapiAccOduTable = _Pmo10010CfgLineSapiAccOduTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 23, 1)
)
if mibBuilder.loadTexts:
    pmo10010CfgLineSapiAccOduTable.setStatus("current")
_Pmo10010CfgLineSapiAccOduEntry_Object = MibTableRow
pmo10010CfgLineSapiAccOduEntry = _Pmo10010CfgLineSapiAccOduEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 23, 1, 1)
)
pmo10010CfgLineSapiAccOduEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010CfgLineSapiAccOduIndex"),
)
if mibBuilder.loadTexts:
    pmo10010CfgLineSapiAccOduEntry.setStatus("current")


class _Pmo10010CfgLineSapiAccOduIndex_Type(Integer32):
    """Custom type pmo10010CfgLineSapiAccOduIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010CfgLineSapiAccOduIndex_Type.__name__ = "Integer32"
_Pmo10010CfgLineSapiAccOduIndex_Object = MibTableColumn
pmo10010CfgLineSapiAccOduIndex = _Pmo10010CfgLineSapiAccOduIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 23, 1, 1, 1),
    _Pmo10010CfgLineSapiAccOduIndex_Type()
)
pmo10010CfgLineSapiAccOduIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CfgLineSapiAccOduIndex.setStatus("current")


class _Pmo10010CfgLineSapiAccSetupOduPortn_Type(DisplayString):
    """Custom type pmo10010CfgLineSapiAccSetupOduPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pmo10010CfgLineSapiAccSetupOduPortn_Type.__name__ = "DisplayString"
_Pmo10010CfgLineSapiAccSetupOduPortn_Object = MibTableColumn
pmo10010CfgLineSapiAccSetupOduPortn = _Pmo10010CfgLineSapiAccSetupOduPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 23, 1, 1, 3),
    _Pmo10010CfgLineSapiAccSetupOduPortn_Type()
)
pmo10010CfgLineSapiAccSetupOduPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CfgLineSapiAccSetupOduPortn.setStatus("deprecated")
_Pmo10010CfgDapiTxLineOdu4_ObjectIdentity = ObjectIdentity
pmo10010CfgDapiTxLineOdu4 = _Pmo10010CfgDapiTxLineOdu4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 24)
)
_Pmo10010CfgLineDapiTxOduTable_Object = MibTable
pmo10010CfgLineDapiTxOduTable = _Pmo10010CfgLineDapiTxOduTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 24, 1)
)
if mibBuilder.loadTexts:
    pmo10010CfgLineDapiTxOduTable.setStatus("current")
_Pmo10010CfgLineDapiTxOduEntry_Object = MibTableRow
pmo10010CfgLineDapiTxOduEntry = _Pmo10010CfgLineDapiTxOduEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 24, 1, 1)
)
pmo10010CfgLineDapiTxOduEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010CfgLineDapiTxOduIndex"),
)
if mibBuilder.loadTexts:
    pmo10010CfgLineDapiTxOduEntry.setStatus("current")


class _Pmo10010CfgLineDapiTxOduIndex_Type(Integer32):
    """Custom type pmo10010CfgLineDapiTxOduIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010CfgLineDapiTxOduIndex_Type.__name__ = "Integer32"
_Pmo10010CfgLineDapiTxOduIndex_Object = MibTableColumn
pmo10010CfgLineDapiTxOduIndex = _Pmo10010CfgLineDapiTxOduIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 24, 1, 1, 1),
    _Pmo10010CfgLineDapiTxOduIndex_Type()
)
pmo10010CfgLineDapiTxOduIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CfgLineDapiTxOduIndex.setStatus("current")


class _Pmo10010CfgLineDapiTxSetupOduPortn_Type(DisplayString):
    """Custom type pmo10010CfgLineDapiTxSetupOduPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pmo10010CfgLineDapiTxSetupOduPortn_Type.__name__ = "DisplayString"
_Pmo10010CfgLineDapiTxSetupOduPortn_Object = MibTableColumn
pmo10010CfgLineDapiTxSetupOduPortn = _Pmo10010CfgLineDapiTxSetupOduPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 24, 1, 1, 3),
    _Pmo10010CfgLineDapiTxSetupOduPortn_Type()
)
pmo10010CfgLineDapiTxSetupOduPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CfgLineDapiTxSetupOduPortn.setStatus("current")
_Pmo10010CfgDapiExpLineOdu4_ObjectIdentity = ObjectIdentity
pmo10010CfgDapiExpLineOdu4 = _Pmo10010CfgDapiExpLineOdu4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 25)
)
_Pmo10010CfgLineDapiExpOduTable_Object = MibTable
pmo10010CfgLineDapiExpOduTable = _Pmo10010CfgLineDapiExpOduTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 25, 1)
)
if mibBuilder.loadTexts:
    pmo10010CfgLineDapiExpOduTable.setStatus("current")
_Pmo10010CfgLineDapiExpOduEntry_Object = MibTableRow
pmo10010CfgLineDapiExpOduEntry = _Pmo10010CfgLineDapiExpOduEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 25, 1, 1)
)
pmo10010CfgLineDapiExpOduEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010CfgLineDapiExpOduIndex"),
)
if mibBuilder.loadTexts:
    pmo10010CfgLineDapiExpOduEntry.setStatus("current")


class _Pmo10010CfgLineDapiExpOduIndex_Type(Integer32):
    """Custom type pmo10010CfgLineDapiExpOduIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010CfgLineDapiExpOduIndex_Type.__name__ = "Integer32"
_Pmo10010CfgLineDapiExpOduIndex_Object = MibTableColumn
pmo10010CfgLineDapiExpOduIndex = _Pmo10010CfgLineDapiExpOduIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 25, 1, 1, 1),
    _Pmo10010CfgLineDapiExpOduIndex_Type()
)
pmo10010CfgLineDapiExpOduIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CfgLineDapiExpOduIndex.setStatus("current")


class _Pmo10010CfgLineDapiExpSetupOduPortn_Type(DisplayString):
    """Custom type pmo10010CfgLineDapiExpSetupOduPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pmo10010CfgLineDapiExpSetupOduPortn_Type.__name__ = "DisplayString"
_Pmo10010CfgLineDapiExpSetupOduPortn_Object = MibTableColumn
pmo10010CfgLineDapiExpSetupOduPortn = _Pmo10010CfgLineDapiExpSetupOduPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 25, 1, 1, 3),
    _Pmo10010CfgLineDapiExpSetupOduPortn_Type()
)
pmo10010CfgLineDapiExpSetupOduPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CfgLineDapiExpSetupOduPortn.setStatus("current")
_Pmo10010CfgDapiAccLineOdu4_ObjectIdentity = ObjectIdentity
pmo10010CfgDapiAccLineOdu4 = _Pmo10010CfgDapiAccLineOdu4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 26)
)
_Pmo10010CfgLineDapiAccOduTable_Object = MibTable
pmo10010CfgLineDapiAccOduTable = _Pmo10010CfgLineDapiAccOduTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 26, 1)
)
if mibBuilder.loadTexts:
    pmo10010CfgLineDapiAccOduTable.setStatus("current")
_Pmo10010CfgLineDapiAccOduEntry_Object = MibTableRow
pmo10010CfgLineDapiAccOduEntry = _Pmo10010CfgLineDapiAccOduEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 26, 1, 1)
)
pmo10010CfgLineDapiAccOduEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010CfgLineDapiAccOduIndex"),
)
if mibBuilder.loadTexts:
    pmo10010CfgLineDapiAccOduEntry.setStatus("current")


class _Pmo10010CfgLineDapiAccOduIndex_Type(Integer32):
    """Custom type pmo10010CfgLineDapiAccOduIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010CfgLineDapiAccOduIndex_Type.__name__ = "Integer32"
_Pmo10010CfgLineDapiAccOduIndex_Object = MibTableColumn
pmo10010CfgLineDapiAccOduIndex = _Pmo10010CfgLineDapiAccOduIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 26, 1, 1, 1),
    _Pmo10010CfgLineDapiAccOduIndex_Type()
)
pmo10010CfgLineDapiAccOduIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CfgLineDapiAccOduIndex.setStatus("current")


class _Pmo10010CfgLineDapiAccSetupOduPortn_Type(DisplayString):
    """Custom type pmo10010CfgLineDapiAccSetupOduPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pmo10010CfgLineDapiAccSetupOduPortn_Type.__name__ = "DisplayString"
_Pmo10010CfgLineDapiAccSetupOduPortn_Object = MibTableColumn
pmo10010CfgLineDapiAccSetupOduPortn = _Pmo10010CfgLineDapiAccSetupOduPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 26, 1, 1, 3),
    _Pmo10010CfgLineDapiAccSetupOduPortn_Type()
)
pmo10010CfgLineDapiAccSetupOduPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CfgLineDapiAccSetupOduPortn.setStatus("deprecated")
_Pmo10010CfgStartuptablefive_ObjectIdentity = ObjectIdentity
pmo10010CfgStartuptablefive = _Pmo10010CfgStartuptablefive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 27)
)
_Pmo10010CfgOtxtlhcapabilitiesTable_Object = MibTable
pmo10010CfgOtxtlhcapabilitiesTable = _Pmo10010CfgOtxtlhcapabilitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 27, 1)
)
if mibBuilder.loadTexts:
    pmo10010CfgOtxtlhcapabilitiesTable.setStatus("current")
_Pmo10010CfgOtxtlhcapabilitiesEntry_Object = MibTableRow
pmo10010CfgOtxtlhcapabilitiesEntry = _Pmo10010CfgOtxtlhcapabilitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 27, 1, 1)
)
pmo10010CfgOtxtlhcapabilitiesEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010CfgOtxtlhcapabilitiesIndex"),
)
if mibBuilder.loadTexts:
    pmo10010CfgOtxtlhcapabilitiesEntry.setStatus("current")


class _Pmo10010CfgOtxtlhcapabilitiesIndex_Type(Integer32):
    """Custom type pmo10010CfgOtxtlhcapabilitiesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010CfgOtxtlhcapabilitiesIndex_Type.__name__ = "Integer32"
_Pmo10010CfgOtxtlhcapabilitiesIndex_Object = MibTableColumn
pmo10010CfgOtxtlhcapabilitiesIndex = _Pmo10010CfgOtxtlhcapabilitiesIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 27, 1, 1, 1),
    _Pmo10010CfgOtxtlhcapabilitiesIndex_Type()
)
pmo10010CfgOtxtlhcapabilitiesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CfgOtxtlhcapabilitiesIndex.setStatus("current")


class _Pmo10010CfgComponentTypePortn_Type(Unsigned32):
    """Custom type pmo10010CfgComponentTypePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmo10010CfgComponentTypePortn_Type.__name__ = "Unsigned32"
_Pmo10010CfgComponentTypePortn_Object = MibTableColumn
pmo10010CfgComponentTypePortn = _Pmo10010CfgComponentTypePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 27, 1, 1, 3),
    _Pmo10010CfgComponentTypePortn_Type()
)
pmo10010CfgComponentTypePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CfgComponentTypePortn.setStatus("current")


class _Pmo10010CfgMiscellaneousPortn_Type(Unsigned32):
    """Custom type pmo10010CfgMiscellaneousPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmo10010CfgMiscellaneousPortn_Type.__name__ = "Unsigned32"
_Pmo10010CfgMiscellaneousPortn_Object = MibTableColumn
pmo10010CfgMiscellaneousPortn = _Pmo10010CfgMiscellaneousPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 27, 1, 1, 4),
    _Pmo10010CfgMiscellaneousPortn_Type()
)
pmo10010CfgMiscellaneousPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CfgMiscellaneousPortn.setStatus("current")


class _Pmo10010CfgFirstChannelPortn_Type(Unsigned32):
    """Custom type pmo10010CfgFirstChannelPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmo10010CfgFirstChannelPortn_Type.__name__ = "Unsigned32"
_Pmo10010CfgFirstChannelPortn_Object = MibTableColumn
pmo10010CfgFirstChannelPortn = _Pmo10010CfgFirstChannelPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 27, 1, 1, 5),
    _Pmo10010CfgFirstChannelPortn_Type()
)
pmo10010CfgFirstChannelPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CfgFirstChannelPortn.setStatus("current")


class _Pmo10010CfgLastChannelPortn_Type(Unsigned32):
    """Custom type pmo10010CfgLastChannelPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmo10010CfgLastChannelPortn_Type.__name__ = "Unsigned32"
_Pmo10010CfgLastChannelPortn_Object = MibTableColumn
pmo10010CfgLastChannelPortn = _Pmo10010CfgLastChannelPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 27, 1, 1, 6),
    _Pmo10010CfgLastChannelPortn_Type()
)
pmo10010CfgLastChannelPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CfgLastChannelPortn.setStatus("current")


class _Pmo10010CfgGridPortn_Type(Unsigned32):
    """Custom type pmo10010CfgGridPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmo10010CfgGridPortn_Type.__name__ = "Unsigned32"
_Pmo10010CfgGridPortn_Object = MibTableColumn
pmo10010CfgGridPortn = _Pmo10010CfgGridPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 27, 1, 1, 7),
    _Pmo10010CfgGridPortn_Type()
)
pmo10010CfgGridPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010CfgGridPortn.setStatus("current")
_Pmo10010CfgWriteConfiguration_Type = EkiOnOff
_Pmo10010CfgWriteConfiguration_Object = MibScalar
pmo10010CfgWriteConfiguration = _Pmo10010CfgWriteConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 9, 257),
    _Pmo10010CfgWriteConfiguration_Type()
)
pmo10010CfgWriteConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmo10010CfgWriteConfiguration.setStatus("current")
_Pmo10010traps_ObjectIdentity = ObjectIdentity
pmo10010traps = _Pmo10010traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 10)
)


class _Pmo10010trapPortNumber_Type(Integer32):
    """Custom type pmo10010trapPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pmo10010trapPortNumber_Type.__name__ = "Integer32"
_Pmo10010trapPortNumber_Object = MibScalar
pmo10010trapPortNumber = _Pmo10010trapPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 10, 2),
    _Pmo10010trapPortNumber_Type()
)
pmo10010trapPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010trapPortNumber.setStatus("current")


class _Pmo10010trapLineNumber_Type(Integer32):
    """Custom type pmo10010trapLineNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pmo10010trapLineNumber_Type.__name__ = "Integer32"
_Pmo10010trapLineNumber_Object = MibScalar
pmo10010trapLineNumber = _Pmo10010trapLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 10, 3),
    _Pmo10010trapLineNumber_Type()
)
pmo10010trapLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010trapLineNumber.setStatus("current")


class _Pmo10010trapBoardNumber_Type(Integer32):
    """Custom type pmo10010trapBoardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pmo10010trapBoardNumber_Type.__name__ = "Integer32"
_Pmo10010trapBoardNumber_Object = MibScalar
pmo10010trapBoardNumber = _Pmo10010trapBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 10, 4),
    _Pmo10010trapBoardNumber_Type()
)
pmo10010trapBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010trapBoardNumber.setStatus("current")
_Pmo10010Monitoring_ObjectIdentity = ObjectIdentity
pmo10010Monitoring = _Pmo10010Monitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11)
)
_Pmo10010MonOther_ObjectIdentity = ObjectIdentity
pmo10010MonOther = _Pmo10010MonOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 1)
)
_Pmo10010MonRmon_ObjectIdentity = ObjectIdentity
pmo10010MonRmon = _Pmo10010MonRmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 1, 3)
)
_Pmo10010MonClient_ObjectIdentity = ObjectIdentity
pmo10010MonClient = _Pmo10010MonClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2)
)
_Pmo10010MonClientRmonCounter_ObjectIdentity = ObjectIdentity
pmo10010MonClientRmonCounter = _Pmo10010MonClientRmonCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4)
)
_Pmo10010MonupRmonBytesCounterClientInputTable_Object = MibTable
pmo10010MonupRmonBytesCounterClientInputTable = _Pmo10010MonupRmonBytesCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 16)
)
if mibBuilder.loadTexts:
    pmo10010MonupRmonBytesCounterClientInputTable.setStatus("current")
_Pmo10010MonupRmonBytesCounterClientInputEntry_Object = MibTableRow
pmo10010MonupRmonBytesCounterClientInputEntry = _Pmo10010MonupRmonBytesCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 16, 1)
)
pmo10010MonupRmonBytesCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010MonupRmonBytesCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pmo10010MonupRmonBytesCounterClientInputEntry.setStatus("current")


class _Pmo10010MonupRmonBytesCounterClientInputIndex_Type(Integer32):
    """Custom type pmo10010MonupRmonBytesCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010MonupRmonBytesCounterClientInputIndex_Type.__name__ = "Integer32"
_Pmo10010MonupRmonBytesCounterClientInputIndex_Object = MibTableColumn
pmo10010MonupRmonBytesCounterClientInputIndex = _Pmo10010MonupRmonBytesCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 16, 1, 1),
    _Pmo10010MonupRmonBytesCounterClientInputIndex_Type()
)
pmo10010MonupRmonBytesCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MonupRmonBytesCounterClientInputIndex.setStatus("current")
_Pmo10010MonupRmonBytesCounterClientInputValuePortn_Type = Counter64
_Pmo10010MonupRmonBytesCounterClientInputValuePortn_Object = MibTableColumn
pmo10010MonupRmonBytesCounterClientInputValuePortn = _Pmo10010MonupRmonBytesCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 16, 1, 2),
    _Pmo10010MonupRmonBytesCounterClientInputValuePortn_Type()
)
pmo10010MonupRmonBytesCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MonupRmonBytesCounterClientInputValuePortn.setStatus("current")
_Pmo10010MonupRmonBytesCounterClientInputErrorPortn_Type = EkiOnOff
_Pmo10010MonupRmonBytesCounterClientInputErrorPortn_Object = MibTableColumn
pmo10010MonupRmonBytesCounterClientInputErrorPortn = _Pmo10010MonupRmonBytesCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 16, 1, 3),
    _Pmo10010MonupRmonBytesCounterClientInputErrorPortn_Type()
)
pmo10010MonupRmonBytesCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MonupRmonBytesCounterClientInputErrorPortn.setStatus("current")
_Pmo10010MonupRmonBytesCounterClientInputOverloadPortn_Type = EkiOnOff
_Pmo10010MonupRmonBytesCounterClientInputOverloadPortn_Object = MibTableColumn
pmo10010MonupRmonBytesCounterClientInputOverloadPortn = _Pmo10010MonupRmonBytesCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 16, 1, 4),
    _Pmo10010MonupRmonBytesCounterClientInputOverloadPortn_Type()
)
pmo10010MonupRmonBytesCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MonupRmonBytesCounterClientInputOverloadPortn.setStatus("current")
_Pmo10010MonupRmonFcsErrorsCounterClientInputTable_Object = MibTable
pmo10010MonupRmonFcsErrorsCounterClientInputTable = _Pmo10010MonupRmonFcsErrorsCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 32)
)
if mibBuilder.loadTexts:
    pmo10010MonupRmonFcsErrorsCounterClientInputTable.setStatus("current")
_Pmo10010MonupRmonFcsErrorsCounterClientInputEntry_Object = MibTableRow
pmo10010MonupRmonFcsErrorsCounterClientInputEntry = _Pmo10010MonupRmonFcsErrorsCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 32, 1)
)
pmo10010MonupRmonFcsErrorsCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010MonupRmonFcsErrorsCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pmo10010MonupRmonFcsErrorsCounterClientInputEntry.setStatus("current")


class _Pmo10010MonupRmonFcsErrorsCounterClientInputIndex_Type(Integer32):
    """Custom type pmo10010MonupRmonFcsErrorsCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010MonupRmonFcsErrorsCounterClientInputIndex_Type.__name__ = "Integer32"
_Pmo10010MonupRmonFcsErrorsCounterClientInputIndex_Object = MibTableColumn
pmo10010MonupRmonFcsErrorsCounterClientInputIndex = _Pmo10010MonupRmonFcsErrorsCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 32, 1, 1),
    _Pmo10010MonupRmonFcsErrorsCounterClientInputIndex_Type()
)
pmo10010MonupRmonFcsErrorsCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MonupRmonFcsErrorsCounterClientInputIndex.setStatus("current")
_Pmo10010MonupRmonFcsErrorsCounterClientInputValuePortn_Type = Counter64
_Pmo10010MonupRmonFcsErrorsCounterClientInputValuePortn_Object = MibTableColumn
pmo10010MonupRmonFcsErrorsCounterClientInputValuePortn = _Pmo10010MonupRmonFcsErrorsCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 32, 1, 2),
    _Pmo10010MonupRmonFcsErrorsCounterClientInputValuePortn_Type()
)
pmo10010MonupRmonFcsErrorsCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MonupRmonFcsErrorsCounterClientInputValuePortn.setStatus("current")
_Pmo10010MonupRmonFcsErrorsCounterClientInputErrorPortn_Type = EkiOnOff
_Pmo10010MonupRmonFcsErrorsCounterClientInputErrorPortn_Object = MibTableColumn
pmo10010MonupRmonFcsErrorsCounterClientInputErrorPortn = _Pmo10010MonupRmonFcsErrorsCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 32, 1, 3),
    _Pmo10010MonupRmonFcsErrorsCounterClientInputErrorPortn_Type()
)
pmo10010MonupRmonFcsErrorsCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MonupRmonFcsErrorsCounterClientInputErrorPortn.setStatus("current")
_Pmo10010MonupRmonFcsErrorsCounterClientInputOverloadPortn_Type = EkiOnOff
_Pmo10010MonupRmonFcsErrorsCounterClientInputOverloadPortn_Object = MibTableColumn
pmo10010MonupRmonFcsErrorsCounterClientInputOverloadPortn = _Pmo10010MonupRmonFcsErrorsCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 32, 1, 4),
    _Pmo10010MonupRmonFcsErrorsCounterClientInputOverloadPortn_Type()
)
pmo10010MonupRmonFcsErrorsCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MonupRmonFcsErrorsCounterClientInputOverloadPortn.setStatus("current")
_Pmo10010MonupRmonPacketsCounterClientInputTable_Object = MibTable
pmo10010MonupRmonPacketsCounterClientInputTable = _Pmo10010MonupRmonPacketsCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 48)
)
if mibBuilder.loadTexts:
    pmo10010MonupRmonPacketsCounterClientInputTable.setStatus("current")
_Pmo10010MonupRmonPacketsCounterClientInputEntry_Object = MibTableRow
pmo10010MonupRmonPacketsCounterClientInputEntry = _Pmo10010MonupRmonPacketsCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 48, 1)
)
pmo10010MonupRmonPacketsCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010MonupRmonPacketsCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pmo10010MonupRmonPacketsCounterClientInputEntry.setStatus("current")


class _Pmo10010MonupRmonPacketsCounterClientInputIndex_Type(Integer32):
    """Custom type pmo10010MonupRmonPacketsCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010MonupRmonPacketsCounterClientInputIndex_Type.__name__ = "Integer32"
_Pmo10010MonupRmonPacketsCounterClientInputIndex_Object = MibTableColumn
pmo10010MonupRmonPacketsCounterClientInputIndex = _Pmo10010MonupRmonPacketsCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 48, 1, 1),
    _Pmo10010MonupRmonPacketsCounterClientInputIndex_Type()
)
pmo10010MonupRmonPacketsCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MonupRmonPacketsCounterClientInputIndex.setStatus("current")
_Pmo10010MonupRmonPacketsCounterClientInputValuePortn_Type = Counter64
_Pmo10010MonupRmonPacketsCounterClientInputValuePortn_Object = MibTableColumn
pmo10010MonupRmonPacketsCounterClientInputValuePortn = _Pmo10010MonupRmonPacketsCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 48, 1, 2),
    _Pmo10010MonupRmonPacketsCounterClientInputValuePortn_Type()
)
pmo10010MonupRmonPacketsCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MonupRmonPacketsCounterClientInputValuePortn.setStatus("current")
_Pmo10010MonupRmonPacketsCounterClientInputErrorPortn_Type = EkiOnOff
_Pmo10010MonupRmonPacketsCounterClientInputErrorPortn_Object = MibTableColumn
pmo10010MonupRmonPacketsCounterClientInputErrorPortn = _Pmo10010MonupRmonPacketsCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 48, 1, 3),
    _Pmo10010MonupRmonPacketsCounterClientInputErrorPortn_Type()
)
pmo10010MonupRmonPacketsCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MonupRmonPacketsCounterClientInputErrorPortn.setStatus("current")
_Pmo10010MonupRmonPacketsCounterClientInputOverloadPortn_Type = EkiOnOff
_Pmo10010MonupRmonPacketsCounterClientInputOverloadPortn_Object = MibTableColumn
pmo10010MonupRmonPacketsCounterClientInputOverloadPortn = _Pmo10010MonupRmonPacketsCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 48, 1, 4),
    _Pmo10010MonupRmonPacketsCounterClientInputOverloadPortn_Type()
)
pmo10010MonupRmonPacketsCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MonupRmonPacketsCounterClientInputOverloadPortn.setStatus("current")
_Pmo10010MonupRmonBroadcastCounterClientInputTable_Object = MibTable
pmo10010MonupRmonBroadcastCounterClientInputTable = _Pmo10010MonupRmonBroadcastCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 64)
)
if mibBuilder.loadTexts:
    pmo10010MonupRmonBroadcastCounterClientInputTable.setStatus("current")
_Pmo10010MonupRmonBroadcastCounterClientInputEntry_Object = MibTableRow
pmo10010MonupRmonBroadcastCounterClientInputEntry = _Pmo10010MonupRmonBroadcastCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 64, 1)
)
pmo10010MonupRmonBroadcastCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010MonupRmonBroadcastCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pmo10010MonupRmonBroadcastCounterClientInputEntry.setStatus("current")


class _Pmo10010MonupRmonBroadcastCounterClientInputIndex_Type(Integer32):
    """Custom type pmo10010MonupRmonBroadcastCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010MonupRmonBroadcastCounterClientInputIndex_Type.__name__ = "Integer32"
_Pmo10010MonupRmonBroadcastCounterClientInputIndex_Object = MibTableColumn
pmo10010MonupRmonBroadcastCounterClientInputIndex = _Pmo10010MonupRmonBroadcastCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 64, 1, 1),
    _Pmo10010MonupRmonBroadcastCounterClientInputIndex_Type()
)
pmo10010MonupRmonBroadcastCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MonupRmonBroadcastCounterClientInputIndex.setStatus("current")
_Pmo10010MonupRmonBroadcastCounterClientInputValuePortn_Type = Counter64
_Pmo10010MonupRmonBroadcastCounterClientInputValuePortn_Object = MibTableColumn
pmo10010MonupRmonBroadcastCounterClientInputValuePortn = _Pmo10010MonupRmonBroadcastCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 64, 1, 2),
    _Pmo10010MonupRmonBroadcastCounterClientInputValuePortn_Type()
)
pmo10010MonupRmonBroadcastCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MonupRmonBroadcastCounterClientInputValuePortn.setStatus("current")
_Pmo10010MonupRmonBroadcastCounterClientInputErrorPortn_Type = EkiOnOff
_Pmo10010MonupRmonBroadcastCounterClientInputErrorPortn_Object = MibTableColumn
pmo10010MonupRmonBroadcastCounterClientInputErrorPortn = _Pmo10010MonupRmonBroadcastCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 64, 1, 3),
    _Pmo10010MonupRmonBroadcastCounterClientInputErrorPortn_Type()
)
pmo10010MonupRmonBroadcastCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MonupRmonBroadcastCounterClientInputErrorPortn.setStatus("current")
_Pmo10010MonupRmonBroadcastCounterClientInputOverloadPortn_Type = EkiOnOff
_Pmo10010MonupRmonBroadcastCounterClientInputOverloadPortn_Object = MibTableColumn
pmo10010MonupRmonBroadcastCounterClientInputOverloadPortn = _Pmo10010MonupRmonBroadcastCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 64, 1, 4),
    _Pmo10010MonupRmonBroadcastCounterClientInputOverloadPortn_Type()
)
pmo10010MonupRmonBroadcastCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MonupRmonBroadcastCounterClientInputOverloadPortn.setStatus("current")
_Pmo10010MonupRmonMulticastCounterClientInputTable_Object = MibTable
pmo10010MonupRmonMulticastCounterClientInputTable = _Pmo10010MonupRmonMulticastCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 80)
)
if mibBuilder.loadTexts:
    pmo10010MonupRmonMulticastCounterClientInputTable.setStatus("current")
_Pmo10010MonupRmonMulticastCounterClientInputEntry_Object = MibTableRow
pmo10010MonupRmonMulticastCounterClientInputEntry = _Pmo10010MonupRmonMulticastCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 80, 1)
)
pmo10010MonupRmonMulticastCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010MonupRmonMulticastCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pmo10010MonupRmonMulticastCounterClientInputEntry.setStatus("current")


class _Pmo10010MonupRmonMulticastCounterClientInputIndex_Type(Integer32):
    """Custom type pmo10010MonupRmonMulticastCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010MonupRmonMulticastCounterClientInputIndex_Type.__name__ = "Integer32"
_Pmo10010MonupRmonMulticastCounterClientInputIndex_Object = MibTableColumn
pmo10010MonupRmonMulticastCounterClientInputIndex = _Pmo10010MonupRmonMulticastCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 80, 1, 1),
    _Pmo10010MonupRmonMulticastCounterClientInputIndex_Type()
)
pmo10010MonupRmonMulticastCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MonupRmonMulticastCounterClientInputIndex.setStatus("current")
_Pmo10010MonupRmonMulticastCounterClientInputValuePortn_Type = Counter64
_Pmo10010MonupRmonMulticastCounterClientInputValuePortn_Object = MibTableColumn
pmo10010MonupRmonMulticastCounterClientInputValuePortn = _Pmo10010MonupRmonMulticastCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 80, 1, 2),
    _Pmo10010MonupRmonMulticastCounterClientInputValuePortn_Type()
)
pmo10010MonupRmonMulticastCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MonupRmonMulticastCounterClientInputValuePortn.setStatus("current")
_Pmo10010MonupRmonMulticastCounterClientInputErrorPortn_Type = EkiOnOff
_Pmo10010MonupRmonMulticastCounterClientInputErrorPortn_Object = MibTableColumn
pmo10010MonupRmonMulticastCounterClientInputErrorPortn = _Pmo10010MonupRmonMulticastCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 80, 1, 3),
    _Pmo10010MonupRmonMulticastCounterClientInputErrorPortn_Type()
)
pmo10010MonupRmonMulticastCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MonupRmonMulticastCounterClientInputErrorPortn.setStatus("current")
_Pmo10010MonupRmonMulticastCounterClientInputOverloadPortn_Type = EkiOnOff
_Pmo10010MonupRmonMulticastCounterClientInputOverloadPortn_Object = MibTableColumn
pmo10010MonupRmonMulticastCounterClientInputOverloadPortn = _Pmo10010MonupRmonMulticastCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 80, 1, 4),
    _Pmo10010MonupRmonMulticastCounterClientInputOverloadPortn_Type()
)
pmo10010MonupRmonMulticastCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MonupRmonMulticastCounterClientInputOverloadPortn.setStatus("current")
_Pmo10010MonupRmonPauseFrameCounterClientInputTable_Object = MibTable
pmo10010MonupRmonPauseFrameCounterClientInputTable = _Pmo10010MonupRmonPauseFrameCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 96)
)
if mibBuilder.loadTexts:
    pmo10010MonupRmonPauseFrameCounterClientInputTable.setStatus("current")
_Pmo10010MonupRmonPauseFrameCounterClientInputEntry_Object = MibTableRow
pmo10010MonupRmonPauseFrameCounterClientInputEntry = _Pmo10010MonupRmonPauseFrameCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 96, 1)
)
pmo10010MonupRmonPauseFrameCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010MonupRmonPauseFrameCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pmo10010MonupRmonPauseFrameCounterClientInputEntry.setStatus("current")


class _Pmo10010MonupRmonPauseFrameCounterClientInputIndex_Type(Integer32):
    """Custom type pmo10010MonupRmonPauseFrameCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010MonupRmonPauseFrameCounterClientInputIndex_Type.__name__ = "Integer32"
_Pmo10010MonupRmonPauseFrameCounterClientInputIndex_Object = MibTableColumn
pmo10010MonupRmonPauseFrameCounterClientInputIndex = _Pmo10010MonupRmonPauseFrameCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 96, 1, 1),
    _Pmo10010MonupRmonPauseFrameCounterClientInputIndex_Type()
)
pmo10010MonupRmonPauseFrameCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MonupRmonPauseFrameCounterClientInputIndex.setStatus("current")
_Pmo10010MonupRmonPauseFrameCounterClientInputValuePortn_Type = Counter64
_Pmo10010MonupRmonPauseFrameCounterClientInputValuePortn_Object = MibTableColumn
pmo10010MonupRmonPauseFrameCounterClientInputValuePortn = _Pmo10010MonupRmonPauseFrameCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 96, 1, 2),
    _Pmo10010MonupRmonPauseFrameCounterClientInputValuePortn_Type()
)
pmo10010MonupRmonPauseFrameCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MonupRmonPauseFrameCounterClientInputValuePortn.setStatus("current")
_Pmo10010MonupRmonPauseFrameCounterClientInputErrorPortn_Type = EkiOnOff
_Pmo10010MonupRmonPauseFrameCounterClientInputErrorPortn_Object = MibTableColumn
pmo10010MonupRmonPauseFrameCounterClientInputErrorPortn = _Pmo10010MonupRmonPauseFrameCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 96, 1, 3),
    _Pmo10010MonupRmonPauseFrameCounterClientInputErrorPortn_Type()
)
pmo10010MonupRmonPauseFrameCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MonupRmonPauseFrameCounterClientInputErrorPortn.setStatus("current")
_Pmo10010MonupRmonPauseFrameCounterClientInputOverloadPortn_Type = EkiOnOff
_Pmo10010MonupRmonPauseFrameCounterClientInputOverloadPortn_Object = MibTableColumn
pmo10010MonupRmonPauseFrameCounterClientInputOverloadPortn = _Pmo10010MonupRmonPauseFrameCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 96, 1, 4),
    _Pmo10010MonupRmonPauseFrameCounterClientInputOverloadPortn_Type()
)
pmo10010MonupRmonPauseFrameCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MonupRmonPauseFrameCounterClientInputOverloadPortn.setStatus("current")
_Pmo10010MonupRmonUnicastCounterClientInputTable_Object = MibTable
pmo10010MonupRmonUnicastCounterClientInputTable = _Pmo10010MonupRmonUnicastCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 160)
)
if mibBuilder.loadTexts:
    pmo10010MonupRmonUnicastCounterClientInputTable.setStatus("current")
_Pmo10010MonupRmonUnicastCounterClientInputEntry_Object = MibTableRow
pmo10010MonupRmonUnicastCounterClientInputEntry = _Pmo10010MonupRmonUnicastCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 160, 1)
)
pmo10010MonupRmonUnicastCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010MonupRmonUnicastCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pmo10010MonupRmonUnicastCounterClientInputEntry.setStatus("current")


class _Pmo10010MonupRmonUnicastCounterClientInputIndex_Type(Integer32):
    """Custom type pmo10010MonupRmonUnicastCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010MonupRmonUnicastCounterClientInputIndex_Type.__name__ = "Integer32"
_Pmo10010MonupRmonUnicastCounterClientInputIndex_Object = MibTableColumn
pmo10010MonupRmonUnicastCounterClientInputIndex = _Pmo10010MonupRmonUnicastCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 160, 1, 1),
    _Pmo10010MonupRmonUnicastCounterClientInputIndex_Type()
)
pmo10010MonupRmonUnicastCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MonupRmonUnicastCounterClientInputIndex.setStatus("current")
_Pmo10010MonupRmonUnicastCounterClientInputValuePortn_Type = Counter64
_Pmo10010MonupRmonUnicastCounterClientInputValuePortn_Object = MibTableColumn
pmo10010MonupRmonUnicastCounterClientInputValuePortn = _Pmo10010MonupRmonUnicastCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 160, 1, 2),
    _Pmo10010MonupRmonUnicastCounterClientInputValuePortn_Type()
)
pmo10010MonupRmonUnicastCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MonupRmonUnicastCounterClientInputValuePortn.setStatus("current")
_Pmo10010MonupRmonUnicastCounterClientInputErrorPortn_Type = EkiOnOff
_Pmo10010MonupRmonUnicastCounterClientInputErrorPortn_Object = MibTableColumn
pmo10010MonupRmonUnicastCounterClientInputErrorPortn = _Pmo10010MonupRmonUnicastCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 160, 1, 3),
    _Pmo10010MonupRmonUnicastCounterClientInputErrorPortn_Type()
)
pmo10010MonupRmonUnicastCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MonupRmonUnicastCounterClientInputErrorPortn.setStatus("current")
_Pmo10010MonupRmonUnicastCounterClientInputOverloadPortn_Type = EkiOnOff
_Pmo10010MonupRmonUnicastCounterClientInputOverloadPortn_Object = MibTableColumn
pmo10010MonupRmonUnicastCounterClientInputOverloadPortn = _Pmo10010MonupRmonUnicastCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 160, 1, 4),
    _Pmo10010MonupRmonUnicastCounterClientInputOverloadPortn_Type()
)
pmo10010MonupRmonUnicastCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MonupRmonUnicastCounterClientInputOverloadPortn.setStatus("current")
_Pmo10010MonupRmonNonunicastCounterClientInputTable_Object = MibTable
pmo10010MonupRmonNonunicastCounterClientInputTable = _Pmo10010MonupRmonNonunicastCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 176)
)
if mibBuilder.loadTexts:
    pmo10010MonupRmonNonunicastCounterClientInputTable.setStatus("current")
_Pmo10010MonupRmonNonunicastCounterClientInputEntry_Object = MibTableRow
pmo10010MonupRmonNonunicastCounterClientInputEntry = _Pmo10010MonupRmonNonunicastCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 176, 1)
)
pmo10010MonupRmonNonunicastCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010MonupRmonNonunicastCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pmo10010MonupRmonNonunicastCounterClientInputEntry.setStatus("current")


class _Pmo10010MonupRmonNonunicastCounterClientInputIndex_Type(Integer32):
    """Custom type pmo10010MonupRmonNonunicastCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010MonupRmonNonunicastCounterClientInputIndex_Type.__name__ = "Integer32"
_Pmo10010MonupRmonNonunicastCounterClientInputIndex_Object = MibTableColumn
pmo10010MonupRmonNonunicastCounterClientInputIndex = _Pmo10010MonupRmonNonunicastCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 176, 1, 1),
    _Pmo10010MonupRmonNonunicastCounterClientInputIndex_Type()
)
pmo10010MonupRmonNonunicastCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MonupRmonNonunicastCounterClientInputIndex.setStatus("current")
_Pmo10010MonupRmonNonunicastCounterClientInputValuePortn_Type = Counter64
_Pmo10010MonupRmonNonunicastCounterClientInputValuePortn_Object = MibTableColumn
pmo10010MonupRmonNonunicastCounterClientInputValuePortn = _Pmo10010MonupRmonNonunicastCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 176, 1, 2),
    _Pmo10010MonupRmonNonunicastCounterClientInputValuePortn_Type()
)
pmo10010MonupRmonNonunicastCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MonupRmonNonunicastCounterClientInputValuePortn.setStatus("current")
_Pmo10010MonupRmonNonunicastCounterClientInputErrorPortn_Type = EkiOnOff
_Pmo10010MonupRmonNonunicastCounterClientInputErrorPortn_Object = MibTableColumn
pmo10010MonupRmonNonunicastCounterClientInputErrorPortn = _Pmo10010MonupRmonNonunicastCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 176, 1, 3),
    _Pmo10010MonupRmonNonunicastCounterClientInputErrorPortn_Type()
)
pmo10010MonupRmonNonunicastCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MonupRmonNonunicastCounterClientInputErrorPortn.setStatus("current")
_Pmo10010MonupRmonNonunicastCounterClientInputOverloadPortn_Type = EkiOnOff
_Pmo10010MonupRmonNonunicastCounterClientInputOverloadPortn_Object = MibTableColumn
pmo10010MonupRmonNonunicastCounterClientInputOverloadPortn = _Pmo10010MonupRmonNonunicastCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 176, 1, 4),
    _Pmo10010MonupRmonNonunicastCounterClientInputOverloadPortn_Type()
)
pmo10010MonupRmonNonunicastCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MonupRmonNonunicastCounterClientInputOverloadPortn.setStatus("current")
_Pmo10010MondownRmonBytesCounterClientOutputTable_Object = MibTable
pmo10010MondownRmonBytesCounterClientOutputTable = _Pmo10010MondownRmonBytesCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 208)
)
if mibBuilder.loadTexts:
    pmo10010MondownRmonBytesCounterClientOutputTable.setStatus("current")
_Pmo10010MondownRmonBytesCounterClientOutputEntry_Object = MibTableRow
pmo10010MondownRmonBytesCounterClientOutputEntry = _Pmo10010MondownRmonBytesCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 208, 1)
)
pmo10010MondownRmonBytesCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010MondownRmonBytesCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pmo10010MondownRmonBytesCounterClientOutputEntry.setStatus("current")


class _Pmo10010MondownRmonBytesCounterClientOutputIndex_Type(Integer32):
    """Custom type pmo10010MondownRmonBytesCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010MondownRmonBytesCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pmo10010MondownRmonBytesCounterClientOutputIndex_Object = MibTableColumn
pmo10010MondownRmonBytesCounterClientOutputIndex = _Pmo10010MondownRmonBytesCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 208, 1, 1),
    _Pmo10010MondownRmonBytesCounterClientOutputIndex_Type()
)
pmo10010MondownRmonBytesCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MondownRmonBytesCounterClientOutputIndex.setStatus("current")
_Pmo10010MondownRmonBytesCounterClientOutputValuePortn_Type = Counter64
_Pmo10010MondownRmonBytesCounterClientOutputValuePortn_Object = MibTableColumn
pmo10010MondownRmonBytesCounterClientOutputValuePortn = _Pmo10010MondownRmonBytesCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 208, 1, 2),
    _Pmo10010MondownRmonBytesCounterClientOutputValuePortn_Type()
)
pmo10010MondownRmonBytesCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MondownRmonBytesCounterClientOutputValuePortn.setStatus("current")
_Pmo10010MondownRmonBytesCounterClientOutputErrorPortn_Type = EkiOnOff
_Pmo10010MondownRmonBytesCounterClientOutputErrorPortn_Object = MibTableColumn
pmo10010MondownRmonBytesCounterClientOutputErrorPortn = _Pmo10010MondownRmonBytesCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 208, 1, 3),
    _Pmo10010MondownRmonBytesCounterClientOutputErrorPortn_Type()
)
pmo10010MondownRmonBytesCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MondownRmonBytesCounterClientOutputErrorPortn.setStatus("current")
_Pmo10010MondownRmonBytesCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pmo10010MondownRmonBytesCounterClientOutputOverloadPortn_Object = MibTableColumn
pmo10010MondownRmonBytesCounterClientOutputOverloadPortn = _Pmo10010MondownRmonBytesCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 208, 1, 4),
    _Pmo10010MondownRmonBytesCounterClientOutputOverloadPortn_Type()
)
pmo10010MondownRmonBytesCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MondownRmonBytesCounterClientOutputOverloadPortn.setStatus("current")
_Pmo10010MondownRmonFcsErrorsCounterClientOutputTable_Object = MibTable
pmo10010MondownRmonFcsErrorsCounterClientOutputTable = _Pmo10010MondownRmonFcsErrorsCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 224)
)
if mibBuilder.loadTexts:
    pmo10010MondownRmonFcsErrorsCounterClientOutputTable.setStatus("current")
_Pmo10010MondownRmonFcsErrorsCounterClientOutputEntry_Object = MibTableRow
pmo10010MondownRmonFcsErrorsCounterClientOutputEntry = _Pmo10010MondownRmonFcsErrorsCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 224, 1)
)
pmo10010MondownRmonFcsErrorsCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010MondownRmonFcsErrorsCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pmo10010MondownRmonFcsErrorsCounterClientOutputEntry.setStatus("current")


class _Pmo10010MondownRmonFcsErrorsCounterClientOutputIndex_Type(Integer32):
    """Custom type pmo10010MondownRmonFcsErrorsCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010MondownRmonFcsErrorsCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pmo10010MondownRmonFcsErrorsCounterClientOutputIndex_Object = MibTableColumn
pmo10010MondownRmonFcsErrorsCounterClientOutputIndex = _Pmo10010MondownRmonFcsErrorsCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 224, 1, 1),
    _Pmo10010MondownRmonFcsErrorsCounterClientOutputIndex_Type()
)
pmo10010MondownRmonFcsErrorsCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MondownRmonFcsErrorsCounterClientOutputIndex.setStatus("current")
_Pmo10010MondownRmonFcsErrorsCounterClientOutputValuePortn_Type = Counter64
_Pmo10010MondownRmonFcsErrorsCounterClientOutputValuePortn_Object = MibTableColumn
pmo10010MondownRmonFcsErrorsCounterClientOutputValuePortn = _Pmo10010MondownRmonFcsErrorsCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 224, 1, 2),
    _Pmo10010MondownRmonFcsErrorsCounterClientOutputValuePortn_Type()
)
pmo10010MondownRmonFcsErrorsCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MondownRmonFcsErrorsCounterClientOutputValuePortn.setStatus("current")
_Pmo10010MondownRmonFcsErrorsCounterClientOutputErrorPortn_Type = EkiOnOff
_Pmo10010MondownRmonFcsErrorsCounterClientOutputErrorPortn_Object = MibTableColumn
pmo10010MondownRmonFcsErrorsCounterClientOutputErrorPortn = _Pmo10010MondownRmonFcsErrorsCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 224, 1, 3),
    _Pmo10010MondownRmonFcsErrorsCounterClientOutputErrorPortn_Type()
)
pmo10010MondownRmonFcsErrorsCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MondownRmonFcsErrorsCounterClientOutputErrorPortn.setStatus("current")
_Pmo10010MondownRmonFcsErrorsCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pmo10010MondownRmonFcsErrorsCounterClientOutputOverloadPortn_Object = MibTableColumn
pmo10010MondownRmonFcsErrorsCounterClientOutputOverloadPortn = _Pmo10010MondownRmonFcsErrorsCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 224, 1, 4),
    _Pmo10010MondownRmonFcsErrorsCounterClientOutputOverloadPortn_Type()
)
pmo10010MondownRmonFcsErrorsCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MondownRmonFcsErrorsCounterClientOutputOverloadPortn.setStatus("current")
_Pmo10010MondownRmonPacketsCounterClientOutputTable_Object = MibTable
pmo10010MondownRmonPacketsCounterClientOutputTable = _Pmo10010MondownRmonPacketsCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 240)
)
if mibBuilder.loadTexts:
    pmo10010MondownRmonPacketsCounterClientOutputTable.setStatus("current")
_Pmo10010MondownRmonPacketsCounterClientOutputEntry_Object = MibTableRow
pmo10010MondownRmonPacketsCounterClientOutputEntry = _Pmo10010MondownRmonPacketsCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 240, 1)
)
pmo10010MondownRmonPacketsCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010MondownRmonPacketsCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pmo10010MondownRmonPacketsCounterClientOutputEntry.setStatus("current")


class _Pmo10010MondownRmonPacketsCounterClientOutputIndex_Type(Integer32):
    """Custom type pmo10010MondownRmonPacketsCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010MondownRmonPacketsCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pmo10010MondownRmonPacketsCounterClientOutputIndex_Object = MibTableColumn
pmo10010MondownRmonPacketsCounterClientOutputIndex = _Pmo10010MondownRmonPacketsCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 240, 1, 1),
    _Pmo10010MondownRmonPacketsCounterClientOutputIndex_Type()
)
pmo10010MondownRmonPacketsCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MondownRmonPacketsCounterClientOutputIndex.setStatus("current")
_Pmo10010MondownRmonPacketsCounterClientOutputValuePortn_Type = Counter64
_Pmo10010MondownRmonPacketsCounterClientOutputValuePortn_Object = MibTableColumn
pmo10010MondownRmonPacketsCounterClientOutputValuePortn = _Pmo10010MondownRmonPacketsCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 240, 1, 2),
    _Pmo10010MondownRmonPacketsCounterClientOutputValuePortn_Type()
)
pmo10010MondownRmonPacketsCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MondownRmonPacketsCounterClientOutputValuePortn.setStatus("current")
_Pmo10010MondownRmonPacketsCounterClientOutputErrorPortn_Type = EkiOnOff
_Pmo10010MondownRmonPacketsCounterClientOutputErrorPortn_Object = MibTableColumn
pmo10010MondownRmonPacketsCounterClientOutputErrorPortn = _Pmo10010MondownRmonPacketsCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 240, 1, 3),
    _Pmo10010MondownRmonPacketsCounterClientOutputErrorPortn_Type()
)
pmo10010MondownRmonPacketsCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MondownRmonPacketsCounterClientOutputErrorPortn.setStatus("current")
_Pmo10010MondownRmonPacketsCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pmo10010MondownRmonPacketsCounterClientOutputOverloadPortn_Object = MibTableColumn
pmo10010MondownRmonPacketsCounterClientOutputOverloadPortn = _Pmo10010MondownRmonPacketsCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 240, 1, 4),
    _Pmo10010MondownRmonPacketsCounterClientOutputOverloadPortn_Type()
)
pmo10010MondownRmonPacketsCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MondownRmonPacketsCounterClientOutputOverloadPortn.setStatus("current")
_Pmo10010MondownRmonBroadcastCounterClientOutputTable_Object = MibTable
pmo10010MondownRmonBroadcastCounterClientOutputTable = _Pmo10010MondownRmonBroadcastCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 256)
)
if mibBuilder.loadTexts:
    pmo10010MondownRmonBroadcastCounterClientOutputTable.setStatus("current")
_Pmo10010MondownRmonBroadcastCounterClientOutputEntry_Object = MibTableRow
pmo10010MondownRmonBroadcastCounterClientOutputEntry = _Pmo10010MondownRmonBroadcastCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 256, 1)
)
pmo10010MondownRmonBroadcastCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010MondownRmonBroadcastCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pmo10010MondownRmonBroadcastCounterClientOutputEntry.setStatus("current")


class _Pmo10010MondownRmonBroadcastCounterClientOutputIndex_Type(Integer32):
    """Custom type pmo10010MondownRmonBroadcastCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010MondownRmonBroadcastCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pmo10010MondownRmonBroadcastCounterClientOutputIndex_Object = MibTableColumn
pmo10010MondownRmonBroadcastCounterClientOutputIndex = _Pmo10010MondownRmonBroadcastCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 256, 1, 1),
    _Pmo10010MondownRmonBroadcastCounterClientOutputIndex_Type()
)
pmo10010MondownRmonBroadcastCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MondownRmonBroadcastCounterClientOutputIndex.setStatus("current")
_Pmo10010MondownRmonBroadcastCounterClientOutputValuePortn_Type = Counter64
_Pmo10010MondownRmonBroadcastCounterClientOutputValuePortn_Object = MibTableColumn
pmo10010MondownRmonBroadcastCounterClientOutputValuePortn = _Pmo10010MondownRmonBroadcastCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 256, 1, 2),
    _Pmo10010MondownRmonBroadcastCounterClientOutputValuePortn_Type()
)
pmo10010MondownRmonBroadcastCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MondownRmonBroadcastCounterClientOutputValuePortn.setStatus("current")
_Pmo10010MondownRmonBroadcastCounterClientOutputErrorPortn_Type = EkiOnOff
_Pmo10010MondownRmonBroadcastCounterClientOutputErrorPortn_Object = MibTableColumn
pmo10010MondownRmonBroadcastCounterClientOutputErrorPortn = _Pmo10010MondownRmonBroadcastCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 256, 1, 3),
    _Pmo10010MondownRmonBroadcastCounterClientOutputErrorPortn_Type()
)
pmo10010MondownRmonBroadcastCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MondownRmonBroadcastCounterClientOutputErrorPortn.setStatus("current")
_Pmo10010MondownRmonBroadcastCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pmo10010MondownRmonBroadcastCounterClientOutputOverloadPortn_Object = MibTableColumn
pmo10010MondownRmonBroadcastCounterClientOutputOverloadPortn = _Pmo10010MondownRmonBroadcastCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 256, 1, 4),
    _Pmo10010MondownRmonBroadcastCounterClientOutputOverloadPortn_Type()
)
pmo10010MondownRmonBroadcastCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MondownRmonBroadcastCounterClientOutputOverloadPortn.setStatus("current")
_Pmo10010MondownRmonMulticastCounterClientOutputTable_Object = MibTable
pmo10010MondownRmonMulticastCounterClientOutputTable = _Pmo10010MondownRmonMulticastCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 272)
)
if mibBuilder.loadTexts:
    pmo10010MondownRmonMulticastCounterClientOutputTable.setStatus("current")
_Pmo10010MondownRmonMulticastCounterClientOutputEntry_Object = MibTableRow
pmo10010MondownRmonMulticastCounterClientOutputEntry = _Pmo10010MondownRmonMulticastCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 272, 1)
)
pmo10010MondownRmonMulticastCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010MondownRmonMulticastCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pmo10010MondownRmonMulticastCounterClientOutputEntry.setStatus("current")


class _Pmo10010MondownRmonMulticastCounterClientOutputIndex_Type(Integer32):
    """Custom type pmo10010MondownRmonMulticastCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010MondownRmonMulticastCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pmo10010MondownRmonMulticastCounterClientOutputIndex_Object = MibTableColumn
pmo10010MondownRmonMulticastCounterClientOutputIndex = _Pmo10010MondownRmonMulticastCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 272, 1, 1),
    _Pmo10010MondownRmonMulticastCounterClientOutputIndex_Type()
)
pmo10010MondownRmonMulticastCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MondownRmonMulticastCounterClientOutputIndex.setStatus("current")
_Pmo10010MondownRmonMulticastCounterClientOutputValuePortn_Type = Counter64
_Pmo10010MondownRmonMulticastCounterClientOutputValuePortn_Object = MibTableColumn
pmo10010MondownRmonMulticastCounterClientOutputValuePortn = _Pmo10010MondownRmonMulticastCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 272, 1, 2),
    _Pmo10010MondownRmonMulticastCounterClientOutputValuePortn_Type()
)
pmo10010MondownRmonMulticastCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MondownRmonMulticastCounterClientOutputValuePortn.setStatus("current")
_Pmo10010MondownRmonMulticastCounterClientOutputErrorPortn_Type = EkiOnOff
_Pmo10010MondownRmonMulticastCounterClientOutputErrorPortn_Object = MibTableColumn
pmo10010MondownRmonMulticastCounterClientOutputErrorPortn = _Pmo10010MondownRmonMulticastCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 272, 1, 3),
    _Pmo10010MondownRmonMulticastCounterClientOutputErrorPortn_Type()
)
pmo10010MondownRmonMulticastCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MondownRmonMulticastCounterClientOutputErrorPortn.setStatus("current")
_Pmo10010MondownRmonMulticastCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pmo10010MondownRmonMulticastCounterClientOutputOverloadPortn_Object = MibTableColumn
pmo10010MondownRmonMulticastCounterClientOutputOverloadPortn = _Pmo10010MondownRmonMulticastCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 272, 1, 4),
    _Pmo10010MondownRmonMulticastCounterClientOutputOverloadPortn_Type()
)
pmo10010MondownRmonMulticastCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MondownRmonMulticastCounterClientOutputOverloadPortn.setStatus("current")
_Pmo10010MondownRmonPauseFrameCounterClientOutputTable_Object = MibTable
pmo10010MondownRmonPauseFrameCounterClientOutputTable = _Pmo10010MondownRmonPauseFrameCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 288)
)
if mibBuilder.loadTexts:
    pmo10010MondownRmonPauseFrameCounterClientOutputTable.setStatus("current")
_Pmo10010MondownRmonPauseFrameCounterClientOutputEntry_Object = MibTableRow
pmo10010MondownRmonPauseFrameCounterClientOutputEntry = _Pmo10010MondownRmonPauseFrameCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 288, 1)
)
pmo10010MondownRmonPauseFrameCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010MondownRmonPauseFrameCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pmo10010MondownRmonPauseFrameCounterClientOutputEntry.setStatus("current")


class _Pmo10010MondownRmonPauseFrameCounterClientOutputIndex_Type(Integer32):
    """Custom type pmo10010MondownRmonPauseFrameCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010MondownRmonPauseFrameCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pmo10010MondownRmonPauseFrameCounterClientOutputIndex_Object = MibTableColumn
pmo10010MondownRmonPauseFrameCounterClientOutputIndex = _Pmo10010MondownRmonPauseFrameCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 288, 1, 1),
    _Pmo10010MondownRmonPauseFrameCounterClientOutputIndex_Type()
)
pmo10010MondownRmonPauseFrameCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MondownRmonPauseFrameCounterClientOutputIndex.setStatus("current")
_Pmo10010MondownRmonPauseFrameCounterClientOutputValuePortn_Type = Counter64
_Pmo10010MondownRmonPauseFrameCounterClientOutputValuePortn_Object = MibTableColumn
pmo10010MondownRmonPauseFrameCounterClientOutputValuePortn = _Pmo10010MondownRmonPauseFrameCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 288, 1, 2),
    _Pmo10010MondownRmonPauseFrameCounterClientOutputValuePortn_Type()
)
pmo10010MondownRmonPauseFrameCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MondownRmonPauseFrameCounterClientOutputValuePortn.setStatus("current")
_Pmo10010MondownRmonPauseFrameCounterClientOutputErrorPortn_Type = EkiOnOff
_Pmo10010MondownRmonPauseFrameCounterClientOutputErrorPortn_Object = MibTableColumn
pmo10010MondownRmonPauseFrameCounterClientOutputErrorPortn = _Pmo10010MondownRmonPauseFrameCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 288, 1, 3),
    _Pmo10010MondownRmonPauseFrameCounterClientOutputErrorPortn_Type()
)
pmo10010MondownRmonPauseFrameCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MondownRmonPauseFrameCounterClientOutputErrorPortn.setStatus("current")
_Pmo10010MondownRmonPauseFrameCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pmo10010MondownRmonPauseFrameCounterClientOutputOverloadPortn_Object = MibTableColumn
pmo10010MondownRmonPauseFrameCounterClientOutputOverloadPortn = _Pmo10010MondownRmonPauseFrameCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 288, 1, 4),
    _Pmo10010MondownRmonPauseFrameCounterClientOutputOverloadPortn_Type()
)
pmo10010MondownRmonPauseFrameCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MondownRmonPauseFrameCounterClientOutputOverloadPortn.setStatus("current")
_Pmo10010MondownRmonUnicastCounterClientOutputTable_Object = MibTable
pmo10010MondownRmonUnicastCounterClientOutputTable = _Pmo10010MondownRmonUnicastCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 352)
)
if mibBuilder.loadTexts:
    pmo10010MondownRmonUnicastCounterClientOutputTable.setStatus("current")
_Pmo10010MondownRmonUnicastCounterClientOutputEntry_Object = MibTableRow
pmo10010MondownRmonUnicastCounterClientOutputEntry = _Pmo10010MondownRmonUnicastCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 352, 1)
)
pmo10010MondownRmonUnicastCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010MondownRmonUnicastCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pmo10010MondownRmonUnicastCounterClientOutputEntry.setStatus("current")


class _Pmo10010MondownRmonUnicastCounterClientOutputIndex_Type(Integer32):
    """Custom type pmo10010MondownRmonUnicastCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010MondownRmonUnicastCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pmo10010MondownRmonUnicastCounterClientOutputIndex_Object = MibTableColumn
pmo10010MondownRmonUnicastCounterClientOutputIndex = _Pmo10010MondownRmonUnicastCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 352, 1, 1),
    _Pmo10010MondownRmonUnicastCounterClientOutputIndex_Type()
)
pmo10010MondownRmonUnicastCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MondownRmonUnicastCounterClientOutputIndex.setStatus("current")
_Pmo10010MondownRmonUnicastCounterClientOutputValuePortn_Type = Counter64
_Pmo10010MondownRmonUnicastCounterClientOutputValuePortn_Object = MibTableColumn
pmo10010MondownRmonUnicastCounterClientOutputValuePortn = _Pmo10010MondownRmonUnicastCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 352, 1, 2),
    _Pmo10010MondownRmonUnicastCounterClientOutputValuePortn_Type()
)
pmo10010MondownRmonUnicastCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MondownRmonUnicastCounterClientOutputValuePortn.setStatus("current")
_Pmo10010MondownRmonUnicastCounterClientOutputErrorPortn_Type = EkiOnOff
_Pmo10010MondownRmonUnicastCounterClientOutputErrorPortn_Object = MibTableColumn
pmo10010MondownRmonUnicastCounterClientOutputErrorPortn = _Pmo10010MondownRmonUnicastCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 352, 1, 3),
    _Pmo10010MondownRmonUnicastCounterClientOutputErrorPortn_Type()
)
pmo10010MondownRmonUnicastCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MondownRmonUnicastCounterClientOutputErrorPortn.setStatus("current")
_Pmo10010MondownRmonUnicastCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pmo10010MondownRmonUnicastCounterClientOutputOverloadPortn_Object = MibTableColumn
pmo10010MondownRmonUnicastCounterClientOutputOverloadPortn = _Pmo10010MondownRmonUnicastCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 352, 1, 4),
    _Pmo10010MondownRmonUnicastCounterClientOutputOverloadPortn_Type()
)
pmo10010MondownRmonUnicastCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MondownRmonUnicastCounterClientOutputOverloadPortn.setStatus("current")
_Pmo10010MondownRmonNonunicastCounterClientOutputTable_Object = MibTable
pmo10010MondownRmonNonunicastCounterClientOutputTable = _Pmo10010MondownRmonNonunicastCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 368)
)
if mibBuilder.loadTexts:
    pmo10010MondownRmonNonunicastCounterClientOutputTable.setStatus("current")
_Pmo10010MondownRmonNonunicastCounterClientOutputEntry_Object = MibTableRow
pmo10010MondownRmonNonunicastCounterClientOutputEntry = _Pmo10010MondownRmonNonunicastCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 368, 1)
)
pmo10010MondownRmonNonunicastCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pmo10010-MIB", "pmo10010MondownRmonNonunicastCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pmo10010MondownRmonNonunicastCounterClientOutputEntry.setStatus("current")


class _Pmo10010MondownRmonNonunicastCounterClientOutputIndex_Type(Integer32):
    """Custom type pmo10010MondownRmonNonunicastCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmo10010MondownRmonNonunicastCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pmo10010MondownRmonNonunicastCounterClientOutputIndex_Object = MibTableColumn
pmo10010MondownRmonNonunicastCounterClientOutputIndex = _Pmo10010MondownRmonNonunicastCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 368, 1, 1),
    _Pmo10010MondownRmonNonunicastCounterClientOutputIndex_Type()
)
pmo10010MondownRmonNonunicastCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MondownRmonNonunicastCounterClientOutputIndex.setStatus("current")
_Pmo10010MondownRmonNonunicastCounterClientOutputValuePortn_Type = Counter64
_Pmo10010MondownRmonNonunicastCounterClientOutputValuePortn_Object = MibTableColumn
pmo10010MondownRmonNonunicastCounterClientOutputValuePortn = _Pmo10010MondownRmonNonunicastCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 368, 1, 2),
    _Pmo10010MondownRmonNonunicastCounterClientOutputValuePortn_Type()
)
pmo10010MondownRmonNonunicastCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MondownRmonNonunicastCounterClientOutputValuePortn.setStatus("current")
_Pmo10010MondownRmonNonunicastCounterClientOutputErrorPortn_Type = EkiOnOff
_Pmo10010MondownRmonNonunicastCounterClientOutputErrorPortn_Object = MibTableColumn
pmo10010MondownRmonNonunicastCounterClientOutputErrorPortn = _Pmo10010MondownRmonNonunicastCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 368, 1, 3),
    _Pmo10010MondownRmonNonunicastCounterClientOutputErrorPortn_Type()
)
pmo10010MondownRmonNonunicastCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MondownRmonNonunicastCounterClientOutputErrorPortn.setStatus("current")
_Pmo10010MondownRmonNonunicastCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pmo10010MondownRmonNonunicastCounterClientOutputOverloadPortn_Object = MibTableColumn
pmo10010MondownRmonNonunicastCounterClientOutputOverloadPortn = _Pmo10010MondownRmonNonunicastCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 76, 11, 2, 4, 368, 1, 4),
    _Pmo10010MondownRmonNonunicastCounterClientOutputOverloadPortn_Type()
)
pmo10010MondownRmonNonunicastCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmo10010MondownRmonNonunicastCounterClientOutputOverloadPortn.setStatus("current")

# Managed Objects groups


# Notification objects

pmo10010LineTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 76, 10, 30)
)
pmo10010LineTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Pmo10010-MIB", "pmo10010AlmLineDdmWarningPortn"),
        ("EKINOPS-Pmo10010-MIB", "pmo10010trapLineNumber"),
        ("EKINOPS-Pmo10010-MIB", "pmo10010trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmo10010LineTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pmo10010LineTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 76, 10, 31)
)
pmo10010LineTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Pmo10010-MIB", "pmo10010AlmLineDdmWarningPortn"),
        ("EKINOPS-Pmo10010-MIB", "pmo10010trapLineNumber"),
        ("EKINOPS-Pmo10010-MIB", "pmo10010trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmo10010LineTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pmo10010LineTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 76, 10, 32)
)
pmo10010LineTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pmo10010-MIB", "pmo10010AlmLineDdmAlmPortn"),
        ("EKINOPS-Pmo10010-MIB", "pmo10010trapLineNumber"),
        ("EKINOPS-Pmo10010-MIB", "pmo10010trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmo10010LineTrapUrgentGoesOn.setStatus(
        "current"
    )

pmo10010LineTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 76, 10, 33)
)
pmo10010LineTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pmo10010-MIB", "pmo10010AlmLineDdmAlmPortn"),
        ("EKINOPS-Pmo10010-MIB", "pmo10010trapLineNumber"),
        ("EKINOPS-Pmo10010-MIB", "pmo10010trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmo10010LineTrapUrgentGoesOff.setStatus(
        "current"
    )

pmo10010LineTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 76, 10, 34)
)
pmo10010LineTrapCritGoesOn.setObjects(
      *(("EKINOPS-Pmo10010-MIB", "pmo10010AlmLineFailPortn"),
        ("EKINOPS-Pmo10010-MIB", "pmo10010AlmLineHwFailPortn"),
        ("EKINOPS-Pmo10010-MIB", "pmo10010trapLineNumber"),
        ("EKINOPS-Pmo10010-MIB", "pmo10010trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmo10010LineTrapCritGoesOn.setStatus(
        "current"
    )

pmo10010LineTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 76, 10, 35)
)
pmo10010LineTrapCritGoesOff.setObjects(
      *(("EKINOPS-Pmo10010-MIB", "pmo10010AlmLineFailPortn"),
        ("EKINOPS-Pmo10010-MIB", "pmo10010AlmLineHwFailPortn"),
        ("EKINOPS-Pmo10010-MIB", "pmo10010trapLineNumber"),
        ("EKINOPS-Pmo10010-MIB", "pmo10010trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmo10010LineTrapCritGoesOff.setStatus(
        "current"
    )

pmo10010ClientTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 76, 10, 40)
)
pmo10010ClientTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Pmo10010-MIB", "pmo10010AlmSfpDdmWarningPortn"),
        ("EKINOPS-Pmo10010-MIB", "pmo10010trapPortNumber"),
        ("EKINOPS-Pmo10010-MIB", "pmo10010trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmo10010ClientTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pmo10010ClientTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 76, 10, 41)
)
pmo10010ClientTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Pmo10010-MIB", "pmo10010AlmSfpDdmWarningPortn"),
        ("EKINOPS-Pmo10010-MIB", "pmo10010trapPortNumber"),
        ("EKINOPS-Pmo10010-MIB", "pmo10010trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmo10010ClientTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pmo10010ClientTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 76, 10, 42)
)
pmo10010ClientTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pmo10010-MIB", "pmo10010AlmSfpDdmAlmPortn"),
        ("EKINOPS-Pmo10010-MIB", "pmo10010trapPortNumber"),
        ("EKINOPS-Pmo10010-MIB", "pmo10010trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmo10010ClientTrapUrgentGoesOn.setStatus(
        "current"
    )

pmo10010ClientTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 76, 10, 43)
)
pmo10010ClientTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pmo10010-MIB", "pmo10010AlmSfpDdmAlmPortn"),
        ("EKINOPS-Pmo10010-MIB", "pmo10010trapPortNumber"),
        ("EKINOPS-Pmo10010-MIB", "pmo10010trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmo10010ClientTrapUrgentGoesOff.setStatus(
        "current"
    )

pmo10010ClientTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 76, 10, 44)
)
pmo10010ClientTrapCritGoesOn.setObjects(
      *(("EKINOPS-Pmo10010-MIB", "pmo10010AlmFailAccPortn"),
        ("EKINOPS-Pmo10010-MIB", "pmo10010AlmHwFailAccPortn"),
        ("EKINOPS-Pmo10010-MIB", "pmo10010trapPortNumber"),
        ("EKINOPS-Pmo10010-MIB", "pmo10010trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmo10010ClientTrapCritGoesOn.setStatus(
        "current"
    )

pmo10010ClientTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 76, 10, 45)
)
pmo10010ClientTrapCritGoesOff.setObjects(
      *(("EKINOPS-Pmo10010-MIB", "pmo10010AlmFailAccPortn"),
        ("EKINOPS-Pmo10010-MIB", "pmo10010AlmHwFailAccPortn"),
        ("EKINOPS-Pmo10010-MIB", "pmo10010trapPortNumber"),
        ("EKINOPS-Pmo10010-MIB", "pmo10010trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmo10010ClientTrapCritGoesOff.setStatus(
        "current"
    )

pmo10010PowerTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 76, 10, 50)
)
pmo10010PowerTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pmo10010-MIB", "pmo10010AlmDefFuseB"),
        ("EKINOPS-Pmo10010-MIB", "pmo10010AlmDefFuseA"),
        ("EKINOPS-Pmo10010-MIB", "pmo10010trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmo10010PowerTrapUrgentGoesOn.setStatus(
        "current"
    )

pmo10010PowerTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 76, 10, 51)
)
pmo10010PowerTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pmo10010-MIB", "pmo10010AlmDefFuseB"),
        ("EKINOPS-Pmo10010-MIB", "pmo10010AlmDefFuseA"),
        ("EKINOPS-Pmo10010-MIB", "pmo10010trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmo10010PowerTrapUrgentGoesOff.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EKINOPS-Pmo10010-MIB",
    **{"Pmo10010MultiRate": Pmo10010MultiRate,
       "Pmo10010OtxMode": Pmo10010OtxMode,
       "Pmo10010OtxGrid": Pmo10010OtxGrid,
       "Pmo10010AdjustValue": Pmo10010AdjustValue,
       "Pmo10010ClientProtocol": Pmo10010ClientProtocol,
       "Pmo10010ProtocolMode": Pmo10010ProtocolMode,
       "Pmo10010OtxChannel": Pmo10010OtxChannel,
       "Pmo10010OrxChannel": Pmo10010OrxChannel,
       "Pmo10010Odu2SapiMode": Pmo10010Odu2SapiMode,
       "Pmo10010Otu4SapiMode": Pmo10010Otu4SapiMode,
       "modulePmo10010": modulePmo10010,
       "pmo10010alarms": pmo10010alarms,
       "pmo10010AlmOther": pmo10010AlmOther,
       "pmo10010AlmOtherNurg": pmo10010AlmOtherNurg,
       "pmo10010AlmsynthAlm2": pmo10010AlmsynthAlm2,
       "pmo10010AlmConfTableSave": pmo10010AlmConfTableSave,
       "pmo10010AlmInvUpload": pmo10010AlmInvUpload,
       "pmo10010AlmConfTableLoad": pmo10010AlmConfTableLoad,
       "pmo10010AlmCorrelatOff": pmo10010AlmCorrelatOff,
       "pmo10010AlmMaintenanceOn": pmo10010AlmMaintenanceOn,
       "pmo10010AlmOtherUrg": pmo10010AlmOtherUrg,
       "pmo10010AlmOtherCrit": pmo10010AlmOtherCrit,
       "pmo10010AlmsynthAlm0": pmo10010AlmsynthAlm0,
       "pmo10010AlmFailFan": pmo10010AlmFailFan,
       "pmo10010AlmModGlobFail": pmo10010AlmModGlobFail,
       "pmo10010AlmDefFuseA": pmo10010AlmDefFuseA,
       "pmo10010AlmDefFuseB": pmo10010AlmDefFuseB,
       "pmo10010AlmclientModuleState": pmo10010AlmclientModuleState,
       "pmo10010AlmCfpInitialize": pmo10010AlmCfpInitialize,
       "pmo10010AlmCfpLowPower": pmo10010AlmCfpLowPower,
       "pmo10010AlmCfpHighPowerUp": pmo10010AlmCfpHighPowerUp,
       "pmo10010AlmCfpTxOff": pmo10010AlmCfpTxOff,
       "pmo10010AlmCfpTxTurnOn": pmo10010AlmCfpTxTurnOn,
       "pmo10010AlmCfpReady": pmo10010AlmCfpReady,
       "pmo10010AlmCfpFault": pmo10010AlmCfpFault,
       "pmo10010AlmCfpTxTurnOff": pmo10010AlmCfpTxTurnOff,
       "pmo10010AlmCfpHighPowerDown": pmo10010AlmCfpHighPowerDown,
       "pmo10010AlmclientModuleGeneralStatus": pmo10010AlmclientModuleGeneralStatus,
       "pmo10010AlmCfpOutOfAlignment": pmo10010AlmCfpOutOfAlignment,
       "pmo10010AlmCfpRxNetworkLol": pmo10010AlmCfpRxNetworkLol,
       "pmo10010AlmCfpRxLos": pmo10010AlmCfpRxLos,
       "pmo10010AlmCfpTxHostLol": pmo10010AlmCfpTxHostLol,
       "pmo10010AlmCfpTxLosf": pmo10010AlmCfpTxLosf,
       "pmo10010AlmCfpTxCmuLol": pmo10010AlmCfpTxCmuLol,
       "pmo10010AlmCfpTxJitterPllLol": pmo10010AlmCfpTxJitterPllLol,
       "pmo10010AlmCfpLossOfRefclk": pmo10010AlmCfpLossOfRefclk,
       "pmo10010AlmCfpHwInterlock": pmo10010AlmCfpHwInterlock,
       "pmo10010AlmclientGlobalAlarmSummary": pmo10010AlmclientGlobalAlarmSummary,
       "pmo10010AlmCfpSoftGlobAlarmTest": pmo10010AlmCfpSoftGlobAlarmTest,
       "pmo10010AlmCfpNetworkLaneAlarmWarning2": pmo10010AlmCfpNetworkLaneAlarmWarning2,
       "pmo10010AlmCfpModuleState": pmo10010AlmCfpModuleState,
       "pmo10010AlmCfpModuleGeneralStatus": pmo10010AlmCfpModuleGeneralStatus,
       "pmo10010AlmCfpModuleFault": pmo10010AlmCfpModuleFault,
       "pmo10010AlmCfpModuleAlarmWarning1": pmo10010AlmCfpModuleAlarmWarning1,
       "pmo10010AlmCfpModuleAlarmWarning2": pmo10010AlmCfpModuleAlarmWarning2,
       "pmo10010AlmCfpNetworkLaneAlarmWarning1": pmo10010AlmCfpNetworkLaneAlarmWarning1,
       "pmo10010AlmCfpNetworkLaneFaultStatus": pmo10010AlmCfpNetworkLaneFaultStatus,
       "pmo10010AlmCfpHostLaneFaultStatus": pmo10010AlmCfpHostLaneFaultStatus,
       "pmo10010AlmCfpGlobAlarmAssertion": pmo10010AlmCfpGlobAlarmAssertion,
       "pmo10010AlmmsaModuleState": pmo10010AlmmsaModuleState,
       "pmo10010AlmMsaInitialize": pmo10010AlmMsaInitialize,
       "pmo10010AlmMsaLowPower": pmo10010AlmMsaLowPower,
       "pmo10010AlmMsaHighPowerUp": pmo10010AlmMsaHighPowerUp,
       "pmo10010AlmMsaTxOff": pmo10010AlmMsaTxOff,
       "pmo10010AlmMsaTxTurnOn": pmo10010AlmMsaTxTurnOn,
       "pmo10010AlmMsaReady": pmo10010AlmMsaReady,
       "pmo10010AlmMsaFault": pmo10010AlmMsaFault,
       "pmo10010AlmMsaTxTurnOff": pmo10010AlmMsaTxTurnOff,
       "pmo10010AlmMsaHighPowerDown": pmo10010AlmMsaHighPowerDown,
       "pmo10010AlmmsaModuleGeneralStatus": pmo10010AlmmsaModuleGeneralStatus,
       "pmo10010AlmMsaOutOfAlignment": pmo10010AlmMsaOutOfAlignment,
       "pmo10010AlmMsaRxNetworkLol": pmo10010AlmMsaRxNetworkLol,
       "pmo10010AlmMsaRxLos": pmo10010AlmMsaRxLos,
       "pmo10010AlmMsaTxHostLol": pmo10010AlmMsaTxHostLol,
       "pmo10010AlmMsaTxLosf": pmo10010AlmMsaTxLosf,
       "pmo10010AlmMsaTxCmuLol": pmo10010AlmMsaTxCmuLol,
       "pmo10010AlmMsaTxJitterPllLol": pmo10010AlmMsaTxJitterPllLol,
       "pmo10010AlmMsaLossOfRefclk": pmo10010AlmMsaLossOfRefclk,
       "pmo10010AlmMsaHwInterlock": pmo10010AlmMsaHwInterlock,
       "pmo10010AlmmsaGlobalAlarmSummary": pmo10010AlmmsaGlobalAlarmSummary,
       "pmo10010AlmMsaSoftGlobAlarmTest": pmo10010AlmMsaSoftGlobAlarmTest,
       "pmo10010AlmMsaNetworkHostAlarmStatus": pmo10010AlmMsaNetworkHostAlarmStatus,
       "pmo10010AlmMsaNetworkLaneAlarmWarning2": pmo10010AlmMsaNetworkLaneAlarmWarning2,
       "pmo10010AlmMsaModuleState": pmo10010AlmMsaModuleState,
       "pmo10010AlmMsaModuleGeneralStatus": pmo10010AlmMsaModuleGeneralStatus,
       "pmo10010AlmModuleFault": pmo10010AlmModuleFault,
       "pmo10010AlmMsaModuleAlarmWarning1": pmo10010AlmMsaModuleAlarmWarning1,
       "pmo10010AlmMsaModuleAlarmWarning2": pmo10010AlmMsaModuleAlarmWarning2,
       "pmo10010AlmMsaNetworkLaneAlarmWarning1": pmo10010AlmMsaNetworkLaneAlarmWarning1,
       "pmo10010AlmMsaNetworkLaneFaultStatus": pmo10010AlmMsaNetworkLaneFaultStatus,
       "pmo10010AlmMsaHostLaneFaultStatus": pmo10010AlmMsaHostLaneFaultStatus,
       "pmo10010AlmMsaGlobAlarmAssertion": pmo10010AlmMsaGlobAlarmAssertion,
       "pmo10010AlmmsaNetworkTxAlignment": pmo10010AlmmsaNetworkTxAlignment,
       "pmo10010AlmNetTxTimingFault": pmo10010AlmNetTxTimingFault,
       "pmo10010AlmNetTxReferenceClockFault": pmo10010AlmNetTxReferenceClockFault,
       "pmo10010AlmNetTxCmuLockFault": pmo10010AlmNetTxCmuLockFault,
       "pmo10010AlmNetTxOutOfAlignment": pmo10010AlmNetTxOutOfAlignment,
       "pmo10010AlmNetTxLossOfAlignment": pmo10010AlmNetTxLossOfAlignment,
       "pmo10010AlmmsaNetworkRxAlignment": pmo10010AlmmsaNetworkRxAlignment,
       "pmo10010AlmNetRxTimingFault": pmo10010AlmNetRxTimingFault,
       "pmo10010AlmNetRxOutOfAlignment": pmo10010AlmNetRxOutOfAlignment,
       "pmo10010AlmNetRxLossOfAlignment": pmo10010AlmNetRxLossOfAlignment,
       "pmo10010AlmNetRxModemLockFault": pmo10010AlmNetRxModemLockFault,
       "pmo10010AlmNetRxModemSyncDetectFault": pmo10010AlmNetRxModemSyncDetectFault,
       "pmo10010AlmmsaNetworkHostNetworkAlarmSummary": pmo10010AlmmsaNetworkHostNetworkAlarmSummary,
       "pmo10010AlmNetworkTxAlignment": pmo10010AlmNetworkTxAlignment,
       "pmo10010AlmNetworkRxAlignment": pmo10010AlmNetworkRxAlignment,
       "pmo10010AlmNetworkRxOtn": pmo10010AlmNetworkRxOtn,
       "pmo10010AlmHostRxAlignment": pmo10010AlmHostRxAlignment,
       "pmo10010AlmHostTxAlignment": pmo10010AlmHostTxAlignment,
       "pmo10010AlmHostTxOtnStatus": pmo10010AlmHostTxOtnStatus,
       "pmo10010AlmmsaHostTxAlignment": pmo10010AlmmsaHostTxAlignment,
       "pmo10010AlmHostTxDeskewLockFault": pmo10010AlmHostTxDeskewLockFault,
       "pmo10010AlmHostTxOutOfAlignment": pmo10010AlmHostTxOutOfAlignment,
       "pmo10010AlmHostTxLossOfAlignment": pmo10010AlmHostTxLossOfAlignment,
       "pmo10010AlmHostTxCdrLockFault": pmo10010AlmHostTxCdrLockFault,
       "pmo10010AlmmsaHostRxAlignment": pmo10010AlmmsaHostRxAlignment,
       "pmo10010AlmHostRxCmuLockFault": pmo10010AlmHostRxCmuLockFault,
       "pmo10010AlmHostRxOutOfAlignment": pmo10010AlmHostRxOutOfAlignment,
       "pmo10010AlmHostRxLossOfAlignment": pmo10010AlmHostRxLossOfAlignment,
       "pmo10010AlmClient": pmo10010AlmClient,
       "pmo10010AlmClientNurg": pmo10010AlmClientNurg,
       "pmo10010AlmclientNetworkLaneAlarmWarningTable": pmo10010AlmclientNetworkLaneAlarmWarningTable,
       "pmo10010AlmclientNetworkLaneAlarmWarningEntry": pmo10010AlmclientNetworkLaneAlarmWarningEntry,
       "pmo10010AlmclientNetworkLaneAlarmWarningIndex": pmo10010AlmclientNetworkLaneAlarmWarningIndex,
       "pmo10010AlmClientRxPowerLowAlarmPortn": pmo10010AlmClientRxPowerLowAlarmPortn,
       "pmo10010AlmClientRxPowerLowWarningPortn": pmo10010AlmClientRxPowerLowWarningPortn,
       "pmo10010AlmClientRxPowerHighWarningPortn": pmo10010AlmClientRxPowerHighWarningPortn,
       "pmo10010AlmClientRxPowerHighAlarmPortn": pmo10010AlmClientRxPowerHighAlarmPortn,
       "pmo10010AlmLaserTempLowAlarmPortn": pmo10010AlmLaserTempLowAlarmPortn,
       "pmo10010AlmClientLaserTempLowWarningPortn": pmo10010AlmClientLaserTempLowWarningPortn,
       "pmo10010AlmClientLaserTempHighWarningPortn": pmo10010AlmClientLaserTempHighWarningPortn,
       "pmo10010AlmClientLaserTempHighAlarmPortn": pmo10010AlmClientLaserTempHighAlarmPortn,
       "pmo10010AlmClientTxPowerLowAlarmPortn": pmo10010AlmClientTxPowerLowAlarmPortn,
       "pmo10010AlmClientTxPowerLowWarningPortn": pmo10010AlmClientTxPowerLowWarningPortn,
       "pmo10010AlmClientTxPowerHighWarningPortn": pmo10010AlmClientTxPowerHighWarningPortn,
       "pmo10010AlmClientTxPowerHighAlarmPortn": pmo10010AlmClientTxPowerHighAlarmPortn,
       "pmo10010AlmClientBiasLowAlarmPortn": pmo10010AlmClientBiasLowAlarmPortn,
       "pmo10010AlmClientBiasLowWarningPortn": pmo10010AlmClientBiasLowWarningPortn,
       "pmo10010AlmClientBiasHighWarningPortn": pmo10010AlmClientBiasHighWarningPortn,
       "pmo10010AlmClientBiasHighAlarmPortn": pmo10010AlmClientBiasHighAlarmPortn,
       "pmo10010AlmclientSfpWarnDdmTable": pmo10010AlmclientSfpWarnDdmTable,
       "pmo10010AlmclientSfpWarnDdmEntry": pmo10010AlmclientSfpWarnDdmEntry,
       "pmo10010AlmclientSfpWarnDdmIndex": pmo10010AlmclientSfpWarnDdmIndex,
       "pmo10010AlmTxPwLowWngPortn": pmo10010AlmTxPwLowWngPortn,
       "pmo10010AlmTxPwrHighWngPortn": pmo10010AlmTxPwrHighWngPortn,
       "pmo10010AlmTxBiasLowWngPortn": pmo10010AlmTxBiasLowWngPortn,
       "pmo10010AlmTxBiasHighWngPortn": pmo10010AlmTxBiasHighWngPortn,
       "pmo10010AlmVccLowWngPortn": pmo10010AlmVccLowWngPortn,
       "pmo10010AlmVccHighWngPortn": pmo10010AlmVccHighWngPortn,
       "pmo10010AlmTempLowWngPortn": pmo10010AlmTempLowWngPortn,
       "pmo10010AlmTempHighWngPortn": pmo10010AlmTempHighWngPortn,
       "pmo10010AlmRxPwrLowWngPortn": pmo10010AlmRxPwrLowWngPortn,
       "pmo10010AlmRxPwrHighWngPortn": pmo10010AlmRxPwrHighWngPortn,
       "pmo10010AlmClientUrg": pmo10010AlmClientUrg,
       "pmo10010AlmclientNetworkLaneFaultTable": pmo10010AlmclientNetworkLaneFaultTable,
       "pmo10010AlmclientNetworkLaneFaultEntry": pmo10010AlmclientNetworkLaneFaultEntry,
       "pmo10010AlmclientNetworkLaneFaultIndex": pmo10010AlmclientNetworkLaneFaultIndex,
       "pmo10010AlmClientLaneRxFifoErrorPortn": pmo10010AlmClientLaneRxFifoErrorPortn,
       "pmo10010AlmClientLaneRxLolPortn": pmo10010AlmClientLaneRxLolPortn,
       "pmo10010AlmClientLaneRxLosPortn": pmo10010AlmClientLaneRxLosPortn,
       "pmo10010AlmClientLaneTxLolPortn": pmo10010AlmClientLaneTxLolPortn,
       "pmo10010AlmClientLaneTxLosfPortn": pmo10010AlmClientLaneTxLosfPortn,
       "pmo10010AlmClientLaneApdPowerSupplyPortn": pmo10010AlmClientLaneApdPowerSupplyPortn,
       "pmo10010AlmClientLaneWavelengthUnlockedPortn": pmo10010AlmClientLaneWavelengthUnlockedPortn,
       "pmo10010AlmClientLaneTecFaultPortn": pmo10010AlmClientLaneTecFaultPortn,
       "pmo10010AlmclientHostLaneFaultTable": pmo10010AlmclientHostLaneFaultTable,
       "pmo10010AlmclientHostLaneFaultEntry": pmo10010AlmclientHostLaneFaultEntry,
       "pmo10010AlmclientHostLaneFaultIndex": pmo10010AlmclientHostLaneFaultIndex,
       "pmo10010AlmClientRxLossOfSyncPortn": pmo10010AlmClientRxLossOfSyncPortn,
       "pmo10010AlmClientInputLossOfSigPortn": pmo10010AlmClientInputLossOfSigPortn,
       "pmo10010AlmClientLanesMarkerUnlockPortn": pmo10010AlmClientLanesMarkerUnlockPortn,
       "pmo10010AlmClientLanes6466UnlockPortn": pmo10010AlmClientLanes6466UnlockPortn,
       "pmo10010AlmClientLanesNotAlignedPortn": pmo10010AlmClientLanesNotAlignedPortn,
       "pmo10010AlmClientCsfDetectedPortn": pmo10010AlmClientCsfDetectedPortn,
       "pmo10010AlmClientTxHostLolPortn": pmo10010AlmClientTxHostLolPortn,
       "pmo10010AlmClientLaneTxFifoErrorPortn": pmo10010AlmClientLaneTxFifoErrorPortn,
       "pmo10010AlmRxLocalFaultDetectedPortn": pmo10010AlmRxLocalFaultDetectedPortn,
       "pmo10010AlmRxRemoteFaultDetectedPortn": pmo10010AlmRxRemoteFaultDetectedPortn,
       "pmo10010AlmTxLocalFaultDetectedPortn": pmo10010AlmTxLocalFaultDetectedPortn,
       "pmo10010AlmTxRemoteFaultDetectedPortn": pmo10010AlmTxRemoteFaultDetectedPortn,
       "pmo10010AlmClientTxLossOfSyncPortn": pmo10010AlmClientTxLossOfSyncPortn,
       "pmo10010AlmclientOtnAlmTable": pmo10010AlmclientOtnAlmTable,
       "pmo10010AlmclientOtnAlmEntry": pmo10010AlmclientOtnAlmEntry,
       "pmo10010AlmclientOtnAlmIndex": pmo10010AlmclientOtnAlmIndex,
       "pmo10010AlmClientOtu2eDlomPortn": pmo10010AlmClientOtu2eDlomPortn,
       "pmo10010AlmClientOtu2eDlofPortn": pmo10010AlmClientOtu2eDlofPortn,
       "pmo10010AlmClientOdu2eDplmPortn": pmo10010AlmClientOdu2eDplmPortn,
       "pmo10010AlmClientOdu2eDdegPortn": pmo10010AlmClientOdu2eDdegPortn,
       "pmo10010AlmClientCsfDetectedOtnPortn": pmo10010AlmClientCsfDetectedOtnPortn,
       "pmo10010AlmClientOdu2eIaisPortn": pmo10010AlmClientOdu2eIaisPortn,
       "pmo10010AlmClientOdu2eDtimPortn": pmo10010AlmClientOdu2eDtimPortn,
       "pmo10010AlmClientOdu2eDaisPortn": pmo10010AlmClientOdu2eDaisPortn,
       "pmo10010AlmClientOdu2eIociPortn": pmo10010AlmClientOdu2eIociPortn,
       "pmo10010AlmClientOdu2eDociPortn": pmo10010AlmClientOdu2eDociPortn,
       "pmo10010AlmClientOdu2eIbdiPortn": pmo10010AlmClientOdu2eIbdiPortn,
       "pmo10010AlmClientOdu2eDbdiPortn": pmo10010AlmClientOdu2eDbdiPortn,
       "pmo10010AlmClientOdu2eIlckPortn": pmo10010AlmClientOdu2eIlckPortn,
       "pmo10010AlmClientOdu2eDlckPortn": pmo10010AlmClientOdu2eDlckPortn,
       "pmo10010AlmclientSfpAlmDdmTable": pmo10010AlmclientSfpAlmDdmTable,
       "pmo10010AlmclientSfpAlmDdmEntry": pmo10010AlmclientSfpAlmDdmEntry,
       "pmo10010AlmclientSfpAlmDdmIndex": pmo10010AlmclientSfpAlmDdmIndex,
       "pmo10010AlmTxPwrLowAlaPortn": pmo10010AlmTxPwrLowAlaPortn,
       "pmo10010AlmTxPwrHighAlaPortn": pmo10010AlmTxPwrHighAlaPortn,
       "pmo10010AlmTxBiasLowAlaPortn": pmo10010AlmTxBiasLowAlaPortn,
       "pmo10010AlmTxBiasHighAlaPortn": pmo10010AlmTxBiasHighAlaPortn,
       "pmo10010AlmVccLowAlaPortn": pmo10010AlmVccLowAlaPortn,
       "pmo10010AlmVccHighAlaPortn": pmo10010AlmVccHighAlaPortn,
       "pmo10010AlmTempLowAlaPortn": pmo10010AlmTempLowAlaPortn,
       "pmo10010AlmTempHighAlaPortn": pmo10010AlmTempHighAlaPortn,
       "pmo10010AlmRxPwrLowAlaPortn": pmo10010AlmRxPwrLowAlaPortn,
       "pmo10010AlmRxPwrHighAlaPortn": pmo10010AlmRxPwrHighAlaPortn,
       "pmo10010AlmClientCrit": pmo10010AlmClientCrit,
       "pmo10010AlmsynthAlmPortTable": pmo10010AlmsynthAlmPortTable,
       "pmo10010AlmsynthAlmPortEntry": pmo10010AlmsynthAlmPortEntry,
       "pmo10010AlmsynthAlmPortIndex": pmo10010AlmsynthAlmPortIndex,
       "pmo10010AlmSfpAbsentPortn": pmo10010AlmSfpAbsentPortn,
       "pmo10010AlmDdmAbsentPortn": pmo10010AlmDdmAbsentPortn,
       "pmo10010AlmHwFailAccPortn": pmo10010AlmHwFailAccPortn,
       "pmo10010AlmDwLsdPortn": pmo10010AlmDwLsdPortn,
       "pmo10010AlmClientLocalOosPortn": pmo10010AlmClientLocalOosPortn,
       "pmo10010AlmClientRemoteOosPortn": pmo10010AlmClientRemoteOosPortn,
       "pmo10010AlmDwCaisPortn": pmo10010AlmDwCaisPortn,
       "pmo10010AlmSfpDdmWarningPortn": pmo10010AlmSfpDdmWarningPortn,
       "pmo10010AlmSfpDdmAlmPortn": pmo10010AlmSfpDdmAlmPortn,
       "pmo10010AlmFailAccPortn": pmo10010AlmFailAccPortn,
       "pmo10010AlmUpCsfPortn": pmo10010AlmUpCsfPortn,
       "pmo10010AlmLine": pmo10010AlmLine,
       "pmo10010AlmLineNurg": pmo10010AlmLineNurg,
       "pmo10010AlmlineNetworkLaneAlarmWarning1Table": pmo10010AlmlineNetworkLaneAlarmWarning1Table,
       "pmo10010AlmlineNetworkLaneAlarmWarning1Entry": pmo10010AlmlineNetworkLaneAlarmWarning1Entry,
       "pmo10010AlmlineNetworkLaneAlarmWarning1Index": pmo10010AlmlineNetworkLaneAlarmWarning1Index,
       "pmo10010AlmLineRxPowerLowAlarmPortn": pmo10010AlmLineRxPowerLowAlarmPortn,
       "pmo10010AlmLineRxPowerLowWarningPortn": pmo10010AlmLineRxPowerLowWarningPortn,
       "pmo10010AlmLineRxPowerHighWarningPortn": pmo10010AlmLineRxPowerHighWarningPortn,
       "pmo10010AlmLineRxPowerHighAlarmPortn": pmo10010AlmLineRxPowerHighAlarmPortn,
       "pmo10010AlmLineLaserTempLowAlarmPortn": pmo10010AlmLineLaserTempLowAlarmPortn,
       "pmo10010AlmLineLaserTempLowWarningPortn": pmo10010AlmLineLaserTempLowWarningPortn,
       "pmo10010AlmLineLaserTempHighWarningPortn": pmo10010AlmLineLaserTempHighWarningPortn,
       "pmo10010AlmLineLaserTempHighAlarmPortn": pmo10010AlmLineLaserTempHighAlarmPortn,
       "pmo10010AlmLineTxPowerLowAlarmPortn": pmo10010AlmLineTxPowerLowAlarmPortn,
       "pmo10010AlmLineTxPowerLowWarningPortn": pmo10010AlmLineTxPowerLowWarningPortn,
       "pmo10010AlmLineTxPowerHighWarningPortn": pmo10010AlmLineTxPowerHighWarningPortn,
       "pmo10010AlmLineTxPowerHighAlarmPortn": pmo10010AlmLineTxPowerHighAlarmPortn,
       "pmo10010AlmLineBiasLowAlarmPortn": pmo10010AlmLineBiasLowAlarmPortn,
       "pmo10010AlmLineBiasLowWarningPortn": pmo10010AlmLineBiasLowWarningPortn,
       "pmo10010AlmLineBiasHighWarningPortn": pmo10010AlmLineBiasHighWarningPortn,
       "pmo10010AlmLineBiasHighAlarmPortn": pmo10010AlmLineBiasHighAlarmPortn,
       "pmo10010AlmlineNetworkLaneAlarmWarning2Table": pmo10010AlmlineNetworkLaneAlarmWarning2Table,
       "pmo10010AlmlineNetworkLaneAlarmWarning2Entry": pmo10010AlmlineNetworkLaneAlarmWarning2Entry,
       "pmo10010AlmlineNetworkLaneAlarmWarning2Index": pmo10010AlmlineNetworkLaneAlarmWarning2Index,
       "pmo10010AlmTxModulatorBiasLowAlarmPortn": pmo10010AlmTxModulatorBiasLowAlarmPortn,
       "pmo10010AlmTxModulatorBiasLowWarningPortn": pmo10010AlmTxModulatorBiasLowWarningPortn,
       "pmo10010AlmTxModulatorBiasHighWarningPortn": pmo10010AlmTxModulatorBiasHighWarningPortn,
       "pmo10010AlmTxModulatorBiasHighAlarmPortn": pmo10010AlmTxModulatorBiasHighAlarmPortn,
       "pmo10010AlmRxLaserTempLowAlarmPortn": pmo10010AlmRxLaserTempLowAlarmPortn,
       "pmo10010AlmRxLaserTempLowWarningPortn": pmo10010AlmRxLaserTempLowWarningPortn,
       "pmo10010AlmRxLaserTempHighWarningPortn": pmo10010AlmRxLaserTempHighWarningPortn,
       "pmo10010AlmRxLaserTempHighAlarmPortn": pmo10010AlmRxLaserTempHighAlarmPortn,
       "pmo10010AlmRxLaserOutputLowAlarmPortn": pmo10010AlmRxLaserOutputLowAlarmPortn,
       "pmo10010AlmRxLaserOutputLowWarningPortn": pmo10010AlmRxLaserOutputLowWarningPortn,
       "pmo10010AlmRxLaserOutputHighWarningPortn": pmo10010AlmRxLaserOutputHighWarningPortn,
       "pmo10010AlmRxLaserOutputHighAlarmPortn": pmo10010AlmRxLaserOutputHighAlarmPortn,
       "pmo10010AlmRxLaserBiasLowAlarmPortn": pmo10010AlmRxLaserBiasLowAlarmPortn,
       "pmo10010AlmRxLaserBiasLowWarningPortn": pmo10010AlmRxLaserBiasLowWarningPortn,
       "pmo10010AlmRxLaserBiasHighWarningPortn": pmo10010AlmRxLaserBiasHighWarningPortn,
       "pmo10010AlmRxLaserBiasHighAlarmPortn": pmo10010AlmRxLaserBiasHighAlarmPortn,
       "pmo10010AlmLineUrg": pmo10010AlmLineUrg,
       "pmo10010AlmlineNetworkLaneFaultTable": pmo10010AlmlineNetworkLaneFaultTable,
       "pmo10010AlmlineNetworkLaneFaultEntry": pmo10010AlmlineNetworkLaneFaultEntry,
       "pmo10010AlmlineNetworkLaneFaultIndex": pmo10010AlmlineNetworkLaneFaultIndex,
       "pmo10010AlmLineLaneRxTecFaultPortn": pmo10010AlmLineLaneRxTecFaultPortn,
       "pmo10010AlmLineLaneRxFifoErrorPortn": pmo10010AlmLineLaneRxFifoErrorPortn,
       "pmo10010AlmLineLaneRxLolPortn": pmo10010AlmLineLaneRxLolPortn,
       "pmo10010AlmLineLaneRxLosPortn": pmo10010AlmLineLaneRxLosPortn,
       "pmo10010AlmLineLaneTxLolPortn": pmo10010AlmLineLaneTxLolPortn,
       "pmo10010AlmLineLaneTxLosfPortn": pmo10010AlmLineLaneTxLosfPortn,
       "pmo10010AlmLineLaneApdPowerSupplyPortn": pmo10010AlmLineLaneApdPowerSupplyPortn,
       "pmo10010AlmLineLaneWavelengthUnlockedPortn": pmo10010AlmLineLaneWavelengthUnlockedPortn,
       "pmo10010AlmLineLaneTecFaultPortn": pmo10010AlmLineLaneTecFaultPortn,
       "pmo10010AlmlineOtu4AlarmTable": pmo10010AlmlineOtu4AlarmTable,
       "pmo10010AlmlineOtu4AlarmEntry": pmo10010AlmlineOtu4AlarmEntry,
       "pmo10010AlmlineOtu4AlarmIndex": pmo10010AlmlineOtu4AlarmIndex,
       "pmo10010AlmLineInputLossOfSignalPortn": pmo10010AlmLineInputLossOfSignalPortn,
       "pmo10010AlmLineLossOfFramePortn": pmo10010AlmLineLossOfFramePortn,
       "pmo10010AlmLineSmBdiInsertedPortn": pmo10010AlmLineSmBdiInsertedPortn,
       "pmo10010AlmLineSmBdiDetectedPortn": pmo10010AlmLineSmBdiDetectedPortn,
       "pmo10010AlmLineSmIaeInsertedPortn": pmo10010AlmLineSmIaeInsertedPortn,
       "pmo10010AlmLineSmIaeDetectedPortn": pmo10010AlmLineSmIaeDetectedPortn,
       "pmo10010AlmOtu4DdegPortn": pmo10010AlmOtu4DdegPortn,
       "pmo10010AlmClientOtu4DtimPortn": pmo10010AlmClientOtu4DtimPortn,
       "pmo10010AlmLineTxHostLolPortn": pmo10010AlmLineTxHostLolPortn,
       "pmo10010AlmLineLaneTxFifoErrorPortn": pmo10010AlmLineLaneTxFifoErrorPortn,
       "pmo10010AlmLineOchr4DlosPPortn": pmo10010AlmLineOchr4DlosPPortn,
       "pmo10010AlmLineOtu4DssfPortn": pmo10010AlmLineOtu4DssfPortn,
       "pmo10010AlmLineOtu4DlomPortn": pmo10010AlmLineOtu4DlomPortn,
       "pmo10010AlmlineNetworkLaneRxOtnTable": pmo10010AlmlineNetworkLaneRxOtnTable,
       "pmo10010AlmlineNetworkLaneRxOtnEntry": pmo10010AlmlineNetworkLaneRxOtnEntry,
       "pmo10010AlmlineNetworkLaneRxOtnIndex": pmo10010AlmlineNetworkLaneRxOtnIndex,
       "pmo10010AlmLineRxOtnOduAisPortn": pmo10010AlmLineRxOtnOduAisPortn,
       "pmo10010AlmLineRxOtnOtuAisPortn": pmo10010AlmLineRxOtnOtuAisPortn,
       "pmo10010AlmLineRxSmBdiPortn": pmo10010AlmLineRxSmBdiPortn,
       "pmo10010AlmLineRxOtnIaePortn": pmo10010AlmLineRxOtnIaePortn,
       "pmo10010AlmLineRxOtnOomPortn": pmo10010AlmLineRxOtnOomPortn,
       "pmo10010AlmLineRxOtnLomPortn": pmo10010AlmLineRxOtnLomPortn,
       "pmo10010AlmLineRxOtnOofPortn": pmo10010AlmLineRxOtnOofPortn,
       "pmo10010AlmLineRxOtnLofPortn": pmo10010AlmLineRxOtnLofPortn,
       "pmo10010AlmlineHostLaneTxOtnTable": pmo10010AlmlineHostLaneTxOtnTable,
       "pmo10010AlmlineHostLaneTxOtnEntry": pmo10010AlmlineHostLaneTxOtnEntry,
       "pmo10010AlmlineHostLaneTxOtnIndex": pmo10010AlmlineHostLaneTxOtnIndex,
       "pmo10010AlmLineTxOtnOduAisPortn": pmo10010AlmLineTxOtnOduAisPortn,
       "pmo10010AlmLineTxOtnOtuAisPortn": pmo10010AlmLineTxOtnOtuAisPortn,
       "pmo10010AlmLineTxSmBdiPortn": pmo10010AlmLineTxSmBdiPortn,
       "pmo10010AlmLineTxOtnIaePortn": pmo10010AlmLineTxOtnIaePortn,
       "pmo10010AlmLineTxOtnOomPortn": pmo10010AlmLineTxOtnOomPortn,
       "pmo10010AlmLineTxOtnLomPortn": pmo10010AlmLineTxOtnLomPortn,
       "pmo10010AlmLineTxOtnOofPortn": pmo10010AlmLineTxOtnOofPortn,
       "pmo10010AlmLineTxOtnLofPortn": pmo10010AlmLineTxOtnLofPortn,
       "pmo10010AlmlineOdu4AlmTable": pmo10010AlmlineOdu4AlmTable,
       "pmo10010AlmlineOdu4AlmEntry": pmo10010AlmlineOdu4AlmEntry,
       "pmo10010AlmlineOdu4AlmIndex": pmo10010AlmlineOdu4AlmIndex,
       "pmo10010AlmLineOdu4DplmPortn": pmo10010AlmLineOdu4DplmPortn,
       "pmo10010AlmLineOdu4DdegPortn": pmo10010AlmLineOdu4DdegPortn,
       "pmo10010AlmLineOdu4IaisPortn": pmo10010AlmLineOdu4IaisPortn,
       "pmo10010AlmLineOdu4DtimPortn": pmo10010AlmLineOdu4DtimPortn,
       "pmo10010AlmLineOdu4DaisPortn": pmo10010AlmLineOdu4DaisPortn,
       "pmo10010AlmLineOdu4IociPortn": pmo10010AlmLineOdu4IociPortn,
       "pmo10010AlmLineOdu4DociPortn": pmo10010AlmLineOdu4DociPortn,
       "pmo10010AlmLineOdu4IbdiPortn": pmo10010AlmLineOdu4IbdiPortn,
       "pmo10010AlmLineOdu4DbdiPortn": pmo10010AlmLineOdu4DbdiPortn,
       "pmo10010AlmLineOdu4IlckPortn": pmo10010AlmLineOdu4IlckPortn,
       "pmo10010AlmLineOdu4DlckPortn": pmo10010AlmLineOdu4DlckPortn,
       "pmo10010AlmLineCrit": pmo10010AlmLineCrit,
       "pmo10010AlmsynthAlmLineTable": pmo10010AlmsynthAlmLineTable,
       "pmo10010AlmsynthAlmLineEntry": pmo10010AlmsynthAlmLineEntry,
       "pmo10010AlmsynthAlmLineIndex": pmo10010AlmsynthAlmLineIndex,
       "pmo10010AlmXfpAbsentPortn": pmo10010AlmXfpAbsentPortn,
       "pmo10010AlmXfpInitNotComplPortn": pmo10010AlmXfpInitNotComplPortn,
       "pmo10010AlmLineHwFailPortn": pmo10010AlmLineHwFailPortn,
       "pmo10010AlmXfpTxOffPortn": pmo10010AlmXfpTxOffPortn,
       "pmo10010AlmLineLocalOosPortn": pmo10010AlmLineLocalOosPortn,
       "pmo10010AlmUpRdiInsPortn": pmo10010AlmUpRdiInsPortn,
       "pmo10010AlmLineDdmWarningPortn": pmo10010AlmLineDdmWarningPortn,
       "pmo10010AlmLineDdmAlmPortn": pmo10010AlmLineDdmAlmPortn,
       "pmo10010AlmLineFailPortn": pmo10010AlmLineFailPortn,
       "pmo10010AlmLineActivePortn": pmo10010AlmLineActivePortn,
       "pmo10010measures": pmo10010measures,
       "pmo10010MesrOther": pmo10010MesrOther,
       "pmo10010Mesrsynth0": pmo10010Mesrsynth0,
       "pmo10010Mesrsynth1": pmo10010Mesrsynth1,
       "pmo10010MesrpmIntervalNumber": pmo10010MesrpmIntervalNumber,
       "pmo10010MesrlineNetTxLaserOutputPwrAverage": pmo10010MesrlineNetTxLaserOutputPwrAverage,
       "pmo10010MesrlineNetTxLaserTempAverage": pmo10010MesrlineNetTxLaserTempAverage,
       "pmo10010MesrlineNetTxBiasCurrentAverage": pmo10010MesrlineNetTxBiasCurrentAverage,
       "pmo10010MesrlineNetRxInputPwrAverage": pmo10010MesrlineNetRxInputPwrAverage,
       "pmo10010MesrlineResidualChromaticDispAverage": pmo10010MesrlineResidualChromaticDispAverage,
       "pmo10010MesrlineDiffGroupDelayAverage": pmo10010MesrlineDiffGroupDelayAverage,
       "pmo10010MesrlineQFactorAverage": pmo10010MesrlineQFactorAverage,
       "pmo10010MesrlineCarrierFreqOffsetAverage": pmo10010MesrlineCarrierFreqOffsetAverage,
       "pmo10010MesrlineOsnrAverage": pmo10010MesrlineOsnrAverage,
       "pmo10010MesrclientNetTxTempMin": pmo10010MesrclientNetTxTempMin,
       "pmo10010MesrclientNetTxBiasMin": pmo10010MesrclientNetTxBiasMin,
       "pmo10010MesrclientNetTxPwrMin": pmo10010MesrclientNetTxPwrMin,
       "pmo10010MesrclientNetRxPwrMin": pmo10010MesrclientNetRxPwrMin,
       "pmo10010MesrlineNetTxLaserOutputPwrMin": pmo10010MesrlineNetTxLaserOutputPwrMin,
       "pmo10010MesrlineNetTxLaserTempMin": pmo10010MesrlineNetTxLaserTempMin,
       "pmo10010MesrlineNetTxBiasCurrentMin": pmo10010MesrlineNetTxBiasCurrentMin,
       "pmo10010MesrlineNetRxInputPwrMin": pmo10010MesrlineNetRxInputPwrMin,
       "pmo10010MesrlineResidualChromaticDispMin": pmo10010MesrlineResidualChromaticDispMin,
       "pmo10010MesrlineDiffGroupDelayMin": pmo10010MesrlineDiffGroupDelayMin,
       "pmo10010MesrlineQFactorMin": pmo10010MesrlineQFactorMin,
       "pmo10010MesrlineCarrierFreqOffsetMin": pmo10010MesrlineCarrierFreqOffsetMin,
       "pmo10010MesrlineOsnrMin": pmo10010MesrlineOsnrMin,
       "pmo10010MesrclientNetTxTempMax": pmo10010MesrclientNetTxTempMax,
       "pmo10010MesrclientNetTxBiasMax": pmo10010MesrclientNetTxBiasMax,
       "pmo10010MesrclientNetTxPwrMax": pmo10010MesrclientNetTxPwrMax,
       "pmo10010MesrclientNetRxPwrMax": pmo10010MesrclientNetRxPwrMax,
       "pmo10010MesrlineNetTxLaserOutputPwrMax": pmo10010MesrlineNetTxLaserOutputPwrMax,
       "pmo10010MesrlineNetTxLaserTempMax": pmo10010MesrlineNetTxLaserTempMax,
       "pmo10010MesrlineNetTxBiasCurrentMax": pmo10010MesrlineNetTxBiasCurrentMax,
       "pmo10010MesrlineNetRxInputPwrMax": pmo10010MesrlineNetRxInputPwrMax,
       "pmo10010MesrlineResidualChromaticDispMax": pmo10010MesrlineResidualChromaticDispMax,
       "pmo10010MesrlineDiffGroupDelayMax": pmo10010MesrlineDiffGroupDelayMax,
       "pmo10010MesrlineQFactorMax": pmo10010MesrlineQFactorMax,
       "pmo10010MesrlineCarrierFreqOffsetMax": pmo10010MesrlineCarrierFreqOffsetMax,
       "pmo10010MesrlineOsnrMax": pmo10010MesrlineOsnrMax,
       "pmo10010MesrClient": pmo10010MesrClient,
       "pmo10010MesrclientCfpTemp": pmo10010MesrclientCfpTemp,
       "pmo10010MesrclientCfp3v3Voltage": pmo10010MesrclientCfp3v3Voltage,
       "pmo10010MesrclientSoaBiasCurrent": pmo10010MesrclientSoaBiasCurrent,
       "pmo10010MesrclientNetTxTempTable": pmo10010MesrclientNetTxTempTable,
       "pmo10010MesrclientNetTxTempEntry": pmo10010MesrclientNetTxTempEntry,
       "pmo10010MesrclientNetTxTempIndex": pmo10010MesrclientNetTxTempIndex,
       "pmo10010MesrclientNetTxTempPortn": pmo10010MesrclientNetTxTempPortn,
       "pmo10010MesrclientNetTxBiasTable": pmo10010MesrclientNetTxBiasTable,
       "pmo10010MesrclientNetTxBiasEntry": pmo10010MesrclientNetTxBiasEntry,
       "pmo10010MesrclientNetTxBiasIndex": pmo10010MesrclientNetTxBiasIndex,
       "pmo10010MesrclientNetTxBiasPortn": pmo10010MesrclientNetTxBiasPortn,
       "pmo10010MesrclientNetTxPwrTable": pmo10010MesrclientNetTxPwrTable,
       "pmo10010MesrclientNetTxPwrEntry": pmo10010MesrclientNetTxPwrEntry,
       "pmo10010MesrclientNetTxPwrIndex": pmo10010MesrclientNetTxPwrIndex,
       "pmo10010MesrclientNetTxPwrPortn": pmo10010MesrclientNetTxPwrPortn,
       "pmo10010MesrclientNetRxPwrTable": pmo10010MesrclientNetRxPwrTable,
       "pmo10010MesrclientNetRxPwrEntry": pmo10010MesrclientNetRxPwrEntry,
       "pmo10010MesrclientNetRxPwrIndex": pmo10010MesrclientNetRxPwrIndex,
       "pmo10010MesrclientNetRxPwrPortn": pmo10010MesrclientNetRxPwrPortn,
       "pmo10010MesrLine": pmo10010MesrLine,
       "pmo10010MesrlineMsaTemp": pmo10010MesrlineMsaTemp,
       "pmo10010MesrlineMsa3v3Voltage": pmo10010MesrlineMsa3v3Voltage,
       "pmo10010MesrlineSoaBiasCurrent": pmo10010MesrlineSoaBiasCurrent,
       "pmo10010MesrlineNetTxLaserOutputPwrTable": pmo10010MesrlineNetTxLaserOutputPwrTable,
       "pmo10010MesrlineNetTxLaserOutputPwrEntry": pmo10010MesrlineNetTxLaserOutputPwrEntry,
       "pmo10010MesrlineNetTxLaserOutputPwrIndex": pmo10010MesrlineNetTxLaserOutputPwrIndex,
       "pmo10010MesrlineNetTxLaserOutputPwrPortn": pmo10010MesrlineNetTxLaserOutputPwrPortn,
       "pmo10010MesrlineNetTxLaserTempTable": pmo10010MesrlineNetTxLaserTempTable,
       "pmo10010MesrlineNetTxLaserTempEntry": pmo10010MesrlineNetTxLaserTempEntry,
       "pmo10010MesrlineNetTxLaserTempIndex": pmo10010MesrlineNetTxLaserTempIndex,
       "pmo10010MesrlineNetTxLaserTempPortn": pmo10010MesrlineNetTxLaserTempPortn,
       "pmo10010MesrlineNetTxBiasCurrentTable": pmo10010MesrlineNetTxBiasCurrentTable,
       "pmo10010MesrlineNetTxBiasCurrentEntry": pmo10010MesrlineNetTxBiasCurrentEntry,
       "pmo10010MesrlineNetTxBiasCurrentIndex": pmo10010MesrlineNetTxBiasCurrentIndex,
       "pmo10010MesrlineNetTxBiasCurrentPortn": pmo10010MesrlineNetTxBiasCurrentPortn,
       "pmo10010MesrlineNetRxInputPwrTable": pmo10010MesrlineNetRxInputPwrTable,
       "pmo10010MesrlineNetRxInputPwrEntry": pmo10010MesrlineNetRxInputPwrEntry,
       "pmo10010MesrlineNetRxInputPwrIndex": pmo10010MesrlineNetRxInputPwrIndex,
       "pmo10010MesrlineNetRxInputPwrPortn": pmo10010MesrlineNetRxInputPwrPortn,
       "pmo10010MesrlineResidualChromaticDispTable": pmo10010MesrlineResidualChromaticDispTable,
       "pmo10010MesrlineResidualChromaticDispEntry": pmo10010MesrlineResidualChromaticDispEntry,
       "pmo10010MesrlineResidualChromaticDispIndex": pmo10010MesrlineResidualChromaticDispIndex,
       "pmo10010MesrlineResidualChromaticDispPortn": pmo10010MesrlineResidualChromaticDispPortn,
       "pmo10010MesrlineDiffGroupDelayTable": pmo10010MesrlineDiffGroupDelayTable,
       "pmo10010MesrlineDiffGroupDelayEntry": pmo10010MesrlineDiffGroupDelayEntry,
       "pmo10010MesrlineDiffGroupDelayIndex": pmo10010MesrlineDiffGroupDelayIndex,
       "pmo10010MesrlineDiffGroupDelayPortn": pmo10010MesrlineDiffGroupDelayPortn,
       "pmo10010MesrlineQFactorTable": pmo10010MesrlineQFactorTable,
       "pmo10010MesrlineQFactorEntry": pmo10010MesrlineQFactorEntry,
       "pmo10010MesrlineQFactorIndex": pmo10010MesrlineQFactorIndex,
       "pmo10010MesrlineQFactorPortn": pmo10010MesrlineQFactorPortn,
       "pmo10010MesrlineCarrierFreqOffsetTable": pmo10010MesrlineCarrierFreqOffsetTable,
       "pmo10010MesrlineCarrierFreqOffsetEntry": pmo10010MesrlineCarrierFreqOffsetEntry,
       "pmo10010MesrlineCarrierFreqOffsetIndex": pmo10010MesrlineCarrierFreqOffsetIndex,
       "pmo10010MesrlineCarrierFreqOffsetPortn": pmo10010MesrlineCarrierFreqOffsetPortn,
       "pmo10010MesrlineOsnrTable": pmo10010MesrlineOsnrTable,
       "pmo10010MesrlineOsnrEntry": pmo10010MesrlineOsnrEntry,
       "pmo10010MesrlineOsnrIndex": pmo10010MesrlineOsnrIndex,
       "pmo10010MesrlineOsnrPortn": pmo10010MesrlineOsnrPortn,
       "pmo10010counters": pmo10010counters,
       "pmo10010CntOther": pmo10010CntOther,
       "pmo10010CntClient": pmo10010CntClient,
       "pmo10010CntclientInputErrorCounterLaneOneTable": pmo10010CntclientInputErrorCounterLaneOneTable,
       "pmo10010CntclientInputErrorCounterLaneOneEntry": pmo10010CntclientInputErrorCounterLaneOneEntry,
       "pmo10010CntclientInputErrorCounterLaneOneIndex": pmo10010CntclientInputErrorCounterLaneOneIndex,
       "pmo10010CntclientInputErrorCounterLaneOneValuePortn": pmo10010CntclientInputErrorCounterLaneOneValuePortn,
       "pmo10010CntclientInputErrorCounterLaneOneErrorPortn": pmo10010CntclientInputErrorCounterLaneOneErrorPortn,
       "pmo10010CntclientInputErrorCounterLaneOneOverloadPortn": pmo10010CntclientInputErrorCounterLaneOneOverloadPortn,
       "pmo10010CntclientInputErrorCounterLaneTwoTable": pmo10010CntclientInputErrorCounterLaneTwoTable,
       "pmo10010CntclientInputErrorCounterLaneTwoEntry": pmo10010CntclientInputErrorCounterLaneTwoEntry,
       "pmo10010CntclientInputErrorCounterLaneTwoIndex": pmo10010CntclientInputErrorCounterLaneTwoIndex,
       "pmo10010CntclientInputErrorCounterLaneTwoValuePortn": pmo10010CntclientInputErrorCounterLaneTwoValuePortn,
       "pmo10010CntclientInputErrorCounterLaneTwoErrorPortn": pmo10010CntclientInputErrorCounterLaneTwoErrorPortn,
       "pmo10010CntclientInputErrorCounterLaneTwoOverloadPortn": pmo10010CntclientInputErrorCounterLaneTwoOverloadPortn,
       "pmo10010CntclientInputErrorCounterTable": pmo10010CntclientInputErrorCounterTable,
       "pmo10010CntclientInputErrorCounterEntry": pmo10010CntclientInputErrorCounterEntry,
       "pmo10010CntclientInputErrorCounterIndex": pmo10010CntclientInputErrorCounterIndex,
       "pmo10010CntclientInputErrorCounterValuePortn": pmo10010CntclientInputErrorCounterValuePortn,
       "pmo10010CntclientInputErrorCounterErrorPortn": pmo10010CntclientInputErrorCounterErrorPortn,
       "pmo10010CntclientInputErrorCounterOverloadPortn": pmo10010CntclientInputErrorCounterOverloadPortn,
       "pmo10010CntclientOutputErrorCounterTable": pmo10010CntclientOutputErrorCounterTable,
       "pmo10010CntclientOutputErrorCounterEntry": pmo10010CntclientOutputErrorCounterEntry,
       "pmo10010CntclientOutputErrorCounterIndex": pmo10010CntclientOutputErrorCounterIndex,
       "pmo10010CntclientOutputErrorCounterValuePortn": pmo10010CntclientOutputErrorCounterValuePortn,
       "pmo10010CntclientOutputErrorCounterErrorPortn": pmo10010CntclientOutputErrorCounterErrorPortn,
       "pmo10010CntclientOutputErrorCounterOverloadPortn": pmo10010CntclientOutputErrorCounterOverloadPortn,
       "pmo10010CntLine": pmo10010CntLine,
       "pmo10010CntlocalLineSmBlockErrorCounterTable": pmo10010CntlocalLineSmBlockErrorCounterTable,
       "pmo10010CntlocalLineSmBlockErrorCounterEntry": pmo10010CntlocalLineSmBlockErrorCounterEntry,
       "pmo10010CntlocalLineSmBlockErrorCounterIndex": pmo10010CntlocalLineSmBlockErrorCounterIndex,
       "pmo10010CntlocalLineSmBlockErrorCounterValuePortn": pmo10010CntlocalLineSmBlockErrorCounterValuePortn,
       "pmo10010CntlocalLineSmBlockErrorCounterErrorPortn": pmo10010CntlocalLineSmBlockErrorCounterErrorPortn,
       "pmo10010CntlocalLineSmBlockErrorCounterOverloadPortn": pmo10010CntlocalLineSmBlockErrorCounterOverloadPortn,
       "pmo10010CntlocalLineFecCorrectedErrorsCounterTable": pmo10010CntlocalLineFecCorrectedErrorsCounterTable,
       "pmo10010CntlocalLineFecCorrectedErrorsCounterEntry": pmo10010CntlocalLineFecCorrectedErrorsCounterEntry,
       "pmo10010CntlocalLineFecCorrectedErrorsCounterIndex": pmo10010CntlocalLineFecCorrectedErrorsCounterIndex,
       "pmo10010CntlocalLineFecCorrectedErrorsCounterValuePortn": pmo10010CntlocalLineFecCorrectedErrorsCounterValuePortn,
       "pmo10010CntlocalLineFecCorrectedErrorsCounterErrorPortn": pmo10010CntlocalLineFecCorrectedErrorsCounterErrorPortn,
       "pmo10010CntlocalLineFecCorrectedErrorsCounterOverloadPortn": pmo10010CntlocalLineFecCorrectedErrorsCounterOverloadPortn,
       "pmo10010CntremoteLineSmBlockErrorCounterTable": pmo10010CntremoteLineSmBlockErrorCounterTable,
       "pmo10010CntremoteLineSmBlockErrorCounterEntry": pmo10010CntremoteLineSmBlockErrorCounterEntry,
       "pmo10010CntremoteLineSmBlockErrorCounterIndex": pmo10010CntremoteLineSmBlockErrorCounterIndex,
       "pmo10010CntremoteLineSmBlockErrorCounterValuePortn": pmo10010CntremoteLineSmBlockErrorCounterValuePortn,
       "pmo10010CntremoteLineSmBlockErrorCounterErrorPortn": pmo10010CntremoteLineSmBlockErrorCounterErrorPortn,
       "pmo10010CntremoteLineSmBlockErrorCounterOverloadPortn": pmo10010CntremoteLineSmBlockErrorCounterOverloadPortn,
       "pmo10010CntlineDfrmTimCntTable": pmo10010CntlineDfrmTimCntTable,
       "pmo10010CntlineDfrmTimCntEntry": pmo10010CntlineDfrmTimCntEntry,
       "pmo10010CntlineDfrmTimCntIndex": pmo10010CntlineDfrmTimCntIndex,
       "pmo10010CntlineDfrmTimCntValuePortn": pmo10010CntlineDfrmTimCntValuePortn,
       "pmo10010CntlineDfrmTimCntErrorPortn": pmo10010CntlineDfrmTimCntErrorPortn,
       "pmo10010CntlineDfrmTimCntOverloadPortn": pmo10010CntlineDfrmTimCntOverloadPortn,
       "pmo10010CntlocalLineTrscvFecCorrectedErrorCounterTable": pmo10010CntlocalLineTrscvFecCorrectedErrorCounterTable,
       "pmo10010CntlocalLineTrscvFecCorrectedErrorCounterEntry": pmo10010CntlocalLineTrscvFecCorrectedErrorCounterEntry,
       "pmo10010CntlocalLineTrscvFecCorrectedErrorCounterIndex": pmo10010CntlocalLineTrscvFecCorrectedErrorCounterIndex,
       "pmo10010CntlocalLineTrscvFecCorrectedErrorCounterValuePortn": pmo10010CntlocalLineTrscvFecCorrectedErrorCounterValuePortn,
       "pmo10010CntlocalLineTrscvFecCorrectedErrorCounterErrorPortn": pmo10010CntlocalLineTrscvFecCorrectedErrorCounterErrorPortn,
       "pmo10010CntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn": pmo10010CntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn,
       "pmo10010CntlocalLineTrscvFecUncorrectedErrorCounterTable": pmo10010CntlocalLineTrscvFecUncorrectedErrorCounterTable,
       "pmo10010CntlocalLineTrscvFecUncorrectedErrorCounterEntry": pmo10010CntlocalLineTrscvFecUncorrectedErrorCounterEntry,
       "pmo10010CntlocalLineTrscvFecUncorrectedErrorCounterIndex": pmo10010CntlocalLineTrscvFecUncorrectedErrorCounterIndex,
       "pmo10010CntlocalLineTrscvFecUncorrectedErrorCounterValuePortn": pmo10010CntlocalLineTrscvFecUncorrectedErrorCounterValuePortn,
       "pmo10010CntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn": pmo10010CntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn,
       "pmo10010CntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn": pmo10010CntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn,
       "pmo10010CntlocalLinePmBlockErrorCounterTable": pmo10010CntlocalLinePmBlockErrorCounterTable,
       "pmo10010CntlocalLinePmBlockErrorCounterEntry": pmo10010CntlocalLinePmBlockErrorCounterEntry,
       "pmo10010CntlocalLinePmBlockErrorCounterIndex": pmo10010CntlocalLinePmBlockErrorCounterIndex,
       "pmo10010CntlocalLinePmBlockErrorCounterValuePortn": pmo10010CntlocalLinePmBlockErrorCounterValuePortn,
       "pmo10010CntlocalLinePmBlockErrorCounterErrorPortn": pmo10010CntlocalLinePmBlockErrorCounterErrorPortn,
       "pmo10010CntlocalLinePmBlockErrorCounterOverloadPortn": pmo10010CntlocalLinePmBlockErrorCounterOverloadPortn,
       "pmo10010CntremoteLinePmBlockErrorCounterTable": pmo10010CntremoteLinePmBlockErrorCounterTable,
       "pmo10010CntremoteLinePmBlockErrorCounterEntry": pmo10010CntremoteLinePmBlockErrorCounterEntry,
       "pmo10010CntremoteLinePmBlockErrorCounterIndex": pmo10010CntremoteLinePmBlockErrorCounterIndex,
       "pmo10010CntremoteLinePmBlockErrorCounterValuePortn": pmo10010CntremoteLinePmBlockErrorCounterValuePortn,
       "pmo10010CntremoteLinePmBlockErrorCounterErrorPortn": pmo10010CntremoteLinePmBlockErrorCounterErrorPortn,
       "pmo10010CntremoteLinePmBlockErrorCounterOverloadPortn": pmo10010CntremoteLinePmBlockErrorCounterOverloadPortn,
       "pmo10010controlsWrite": pmo10010controlsWrite,
       "pmo10010CtrlOther": pmo10010CtrlOther,
       "pmo10010CtrlconfMgnt1": pmo10010CtrlconfMgnt1,
       "pmo10010CtrlConf1Load1": pmo10010CtrlConf1Load1,
       "pmo10010CtrlConf2Load1": pmo10010CtrlConf2Load1,
       "pmo10010CtrlConf2Flash1": pmo10010CtrlConf2Flash1,
       "pmo10010CtrlConf2Clear1": pmo10010CtrlConf2Clear1,
       "pmo10010Ctrlsynth4": pmo10010Ctrlsynth4,
       "pmo10010CtrlCorrelatOn": pmo10010CtrlCorrelatOn,
       "pmo10010CtrlCorrelatOff": pmo10010CtrlCorrelatOff,
       "pmo10010CtrlswMgnt": pmo10010CtrlswMgnt,
       "pmo10010CtrlColdReset": pmo10010CtrlColdReset,
       "pmo10010CtrlWarmReset": pmo10010CtrlWarmReset,
       "pmo10010CtrlLoadSwBank1": pmo10010CtrlLoadSwBank1,
       "pmo10010CtrlLoadSwBank2": pmo10010CtrlLoadSwBank2,
       "pmo10010CtrlgwMgnt": pmo10010CtrlgwMgnt,
       "pmo10010CtrlCurrentGwReset": pmo10010CtrlCurrentGwReset,
       "pmo10010CtrlLoadGwBank1": pmo10010CtrlLoadGwBank1,
       "pmo10010CtrlLoadGwBank2": pmo10010CtrlLoadGwBank2,
       "pmo10010CtrlLoadGwBank3": pmo10010CtrlLoadGwBank3,
       "pmo10010CtrlLoadGwBank4": pmo10010CtrlLoadGwBank4,
       "pmo10010CtrlledTest": pmo10010CtrlledTest,
       "pmo10010CtrlGreenLed": pmo10010CtrlGreenLed,
       "pmo10010CtrlRedLed": pmo10010CtrlRedLed,
       "pmo10010CtrlLedOff": pmo10010CtrlLedOff,
       "pmo10010CtrlinitSwitchMarvell": pmo10010CtrlinitSwitchMarvell,
       "pmo10010CtrlInitSwitchMarvell": pmo10010CtrlInitSwitchMarvell,
       "pmo10010CtrlresetCount": pmo10010CtrlresetCount,
       "pmo10010CtrlResetcount": pmo10010CtrlResetcount,
       "pmo10010CtrlresetRmon": pmo10010CtrlresetRmon,
       "pmo10010CtrlResetrmon": pmo10010CtrlResetrmon,
       "pmo10010CtrlresetMeasurements": pmo10010CtrlresetMeasurements,
       "pmo10010CtrlResetmeasurements": pmo10010CtrlResetmeasurements,
       "pmo10010CtrlClient": pmo10010CtrlClient,
       "pmo10010CtrlaccessLoopTable": pmo10010CtrlaccessLoopTable,
       "pmo10010CtrlaccessLoopEntry": pmo10010CtrlaccessLoopEntry,
       "pmo10010CtrlaccessLoopIndex": pmo10010CtrlaccessLoopIndex,
       "pmo10010CtrlaccessLoopPortn": pmo10010CtrlaccessLoopPortn,
       "pmo10010CtrlclientLoopToLineTable": pmo10010CtrlclientLoopToLineTable,
       "pmo10010CtrlclientLoopToLineEntry": pmo10010CtrlclientLoopToLineEntry,
       "pmo10010CtrlclientLoopToLineIndex": pmo10010CtrlclientLoopToLineIndex,
       "pmo10010CtrlclientLoopToLinePortn": pmo10010CtrlclientLoopToLinePortn,
       "pmo10010CtrlcsfUpInsTable": pmo10010CtrlcsfUpInsTable,
       "pmo10010CtrlcsfUpInsEntry": pmo10010CtrlcsfUpInsEntry,
       "pmo10010CtrlcsfUpInsIndex": pmo10010CtrlcsfUpInsIndex,
       "pmo10010CtrlcsfUpInsPortn": pmo10010CtrlcsfUpInsPortn,
       "pmo10010CtrlcaisDwInsTable": pmo10010CtrlcaisDwInsTable,
       "pmo10010CtrlcaisDwInsEntry": pmo10010CtrlcaisDwInsEntry,
       "pmo10010CtrlcaisDwInsIndex": pmo10010CtrlcaisDwInsIndex,
       "pmo10010CtrlcaisDwInsPortn": pmo10010CtrlcaisDwInsPortn,
       "pmo10010CtrlLine": pmo10010CtrlLine,
       "pmo10010CtrlcommAccessLoopTable": pmo10010CtrlcommAccessLoopTable,
       "pmo10010CtrlcommAccessLoopEntry": pmo10010CtrlcommAccessLoopEntry,
       "pmo10010CtrlcommAccessLoopIndex": pmo10010CtrlcommAccessLoopIndex,
       "pmo10010CtrlcommAccessLoopPortn": pmo10010CtrlcommAccessLoopPortn,
       "pmo10010CtrllineLoopTable": pmo10010CtrllineLoopTable,
       "pmo10010CtrllineLoopEntry": pmo10010CtrllineLoopEntry,
       "pmo10010CtrllineLoopIndex": pmo10010CtrllineLoopIndex,
       "pmo10010CtrllineLoopPortn": pmo10010CtrllineLoopPortn,
       "pmo10010CtrlfecDisableTable": pmo10010CtrlfecDisableTable,
       "pmo10010CtrlfecDisableEntry": pmo10010CtrlfecDisableEntry,
       "pmo10010CtrlfecDisableIndex": pmo10010CtrlfecDisableIndex,
       "pmo10010CtrlfecDisablePortn": pmo10010CtrlfecDisablePortn,
       "pmo10010CtrlmsaLineLoopTable": pmo10010CtrlmsaLineLoopTable,
       "pmo10010CtrlmsaLineLoopEntry": pmo10010CtrlmsaLineLoopEntry,
       "pmo10010CtrlmsaLineLoopIndex": pmo10010CtrlmsaLineLoopIndex,
       "pmo10010CtrlmsaLineLoopPortn": pmo10010CtrlmsaLineLoopPortn,
       "pmo10010CtrlmsaTxResetTable": pmo10010CtrlmsaTxResetTable,
       "pmo10010CtrlmsaTxResetEntry": pmo10010CtrlmsaTxResetEntry,
       "pmo10010CtrlmsaTxResetIndex": pmo10010CtrlmsaTxResetIndex,
       "pmo10010CtrlmsaTxResetPortn": pmo10010CtrlmsaTxResetPortn,
       "pmo10010CtrlmsaRxResetTable": pmo10010CtrlmsaRxResetTable,
       "pmo10010CtrlmsaRxResetEntry": pmo10010CtrlmsaRxResetEntry,
       "pmo10010CtrlmsaRxResetIndex": pmo10010CtrlmsaRxResetIndex,
       "pmo10010CtrlmsaRxResetPortn": pmo10010CtrlmsaRxResetPortn,
       "pmo10010CtrlmsaShutdownTable": pmo10010CtrlmsaShutdownTable,
       "pmo10010CtrlmsaShutdownEntry": pmo10010CtrlmsaShutdownEntry,
       "pmo10010CtrlmsaShutdownIndex": pmo10010CtrlmsaShutdownIndex,
       "pmo10010CtrlmsaShutdownPortn": pmo10010CtrlmsaShutdownPortn,
       "pmo10010ri": pmo10010ri,
       "pmo10010riTable": pmo10010riTable,
       "pmo10010RinvSfpTable": pmo10010RinvSfpTable,
       "pmo10010RinvSfpEntry": pmo10010RinvSfpEntry,
       "pmo10010RinvSfpIndex": pmo10010RinvSfpIndex,
       "pmo10010Rinvsfp": pmo10010Rinvsfp,
       "pmo10010RinvLineTable": pmo10010RinvLineTable,
       "pmo10010RinvLineEntry": pmo10010RinvLineEntry,
       "pmo10010RinvLineIndex": pmo10010RinvLineIndex,
       "pmo10010RinvxfpLine": pmo10010RinvxfpLine,
       "pmo10010RinvReloadInventory": pmo10010RinvReloadInventory,
       "pmo10010RinvHwPlatform": pmo10010RinvHwPlatform,
       "pmo10010RinvModulePlatform": pmo10010RinvModulePlatform,
       "pmo10010RinvSwPlatform": pmo10010RinvSwPlatform,
       "pmo10010RinvGwPlatform": pmo10010RinvGwPlatform,
       "pmo10010download": pmo10010download,
       "pmo10010DwlOther": pmo10010DwlOther,
       "pmo10010DwlrestartProcess": pmo10010DwlrestartProcess,
       "pmo10010DwlWarmRestartProcessed": pmo10010DwlWarmRestartProcessed,
       "pmo10010DwlColdRestartProcessed": pmo10010DwlColdRestartProcessed,
       "pmo10010DwlswBanksUsed": pmo10010DwlswBanksUsed,
       "pmo10010DwlSwBank1Used": pmo10010DwlSwBank1Used,
       "pmo10010DwlSwBank2Used": pmo10010DwlSwBank2Used,
       "pmo10010DwlSwBank1Notempty": pmo10010DwlSwBank1Notempty,
       "pmo10010DwlSwBank2Notempty": pmo10010DwlSwBank2Notempty,
       "pmo10010DwlgwBanksUsed": pmo10010DwlgwBanksUsed,
       "pmo10010DwlGwBank1Used": pmo10010DwlGwBank1Used,
       "pmo10010DwlGwBank2Used": pmo10010DwlGwBank2Used,
       "pmo10010DwlGwBank3Used": pmo10010DwlGwBank3Used,
       "pmo10010DwlGwBank4Used": pmo10010DwlGwBank4Used,
       "pmo10010DwlGwBank1Notempty": pmo10010DwlGwBank1Notempty,
       "pmo10010DwlGwBank2Notempty": pmo10010DwlGwBank2Notempty,
       "pmo10010DwlGwBank3Notempty": pmo10010DwlGwBank3Notempty,
       "pmo10010DwlGwBank4Notempty": pmo10010DwlGwBank4Notempty,
       "pmo10010DwlClient": pmo10010DwlClient,
       "pmo10010DwlLine": pmo10010DwlLine,
       "pmo10010Config": pmo10010Config,
       "pmo10010CfgAccessCAisCsf": pmo10010CfgAccessCAisCsf,
       "pmo10010CfgClientcaiscsfTable": pmo10010CfgClientcaiscsfTable,
       "pmo10010CfgClientcaiscsfEntry": pmo10010CfgClientcaiscsfEntry,
       "pmo10010CfgClientcaiscsfIndex": pmo10010CfgClientcaiscsfIndex,
       "pmo10010CfgReservePortn": pmo10010CfgReservePortn,
       "pmo10010CfgStartup": pmo10010CfgStartup,
       "pmo10010CfgClientStartupTable": pmo10010CfgClientStartupTable,
       "pmo10010CfgClientStartupEntry": pmo10010CfgClientStartupEntry,
       "pmo10010CfgClientStartupIndex": pmo10010CfgClientStartupIndex,
       "pmo10010CfgSystConfPortPortn": pmo10010CfgSystConfPortPortn,
       "pmo10010CfgNetConfPortPortn": pmo10010CfgNetConfPortPortn,
       "pmo10010CfgOptionsPortPortn": pmo10010CfgOptionsPortPortn,
       "pmo10010CfgLineStartupTable": pmo10010CfgLineStartupTable,
       "pmo10010CfgLineStartupEntry": pmo10010CfgLineStartupEntry,
       "pmo10010CfgLineStartupIndex": pmo10010CfgLineStartupIndex,
       "pmo10010CfgSystConfLinePortn": pmo10010CfgSystConfLinePortn,
       "pmo10010CfgOptionsLinePortn": pmo10010CfgOptionsLinePortn,
       "pmo10010CfgXfpTable": pmo10010CfgXfpTable,
       "pmo10010CfgXfpEntry": pmo10010CfgXfpEntry,
       "pmo10010CfgXfpIndex": pmo10010CfgXfpIndex,
       "pmo10010CfgSystConfMsaLinePortn": pmo10010CfgSystConfMsaLinePortn,
       "pmo10010CfgClientOtxtlhTable": pmo10010CfgClientOtxtlhTable,
       "pmo10010CfgClientOtxtlhEntry": pmo10010CfgClientOtxtlhEntry,
       "pmo10010CfgClientOtxtlhIndex": pmo10010CfgClientOtxtlhIndex,
       "pmo10010CfgControlsPortn": pmo10010CfgControlsPortn,
       "pmo10010CfgClientPwrLaserPortn": pmo10010CfgClientPwrLaserPortn,
       "pmo10010CfgClientFCurrentPortn": pmo10010CfgClientFCurrentPortn,
       "pmo10010CfgClientGridCurrentPortn": pmo10010CfgClientGridCurrentPortn,
       "pmo10010CfgClientFoPortn": pmo10010CfgClientFoPortn,
       "pmo10010CfgLabels": pmo10010CfgLabels,
       "pmo10010CfgLabelclientTable": pmo10010CfgLabelclientTable,
       "pmo10010CfgLabelclientEntry": pmo10010CfgLabelclientEntry,
       "pmo10010CfgLabelclientIndex": pmo10010CfgLabelclientIndex,
       "pmo10010CfgLabelclientPortn": pmo10010CfgLabelclientPortn,
       "pmo10010CfgLabellineTable": pmo10010CfgLabellineTable,
       "pmo10010CfgLabellineEntry": pmo10010CfgLabellineEntry,
       "pmo10010CfgLabellineIndex": pmo10010CfgLabellineIndex,
       "pmo10010CfgLabellinePortn": pmo10010CfgLabellinePortn,
       "pmo10010CfgStartuptlh": pmo10010CfgStartuptlh,
       "pmo10010CfgOtxtlhTable": pmo10010CfgOtxtlhTable,
       "pmo10010CfgOtxtlhEntry": pmo10010CfgOtxtlhEntry,
       "pmo10010CfgOtxtlhIndex": pmo10010CfgOtxtlhIndex,
       "pmo10010CfgLinePwrLaserPortn": pmo10010CfgLinePwrLaserPortn,
       "pmo10010CfgLineFCurrentPortn": pmo10010CfgLineFCurrentPortn,
       "pmo10010CfgLineGridCurrentPortn": pmo10010CfgLineGridCurrentPortn,
       "pmo10010CfgFPortn": pmo10010CfgFPortn,
       "pmo10010CfgRxLineFCurrentPortn": pmo10010CfgRxLineFCurrentPortn,
       "pmo10010CfgOther": pmo10010CfgOther,
       "pmo10010tablemoduleOther": pmo10010tablemoduleOther,
       "pmo10010Cfgmode": pmo10010Cfgmode,
       "pmo10010CfgfanLowSpeedThreshold": pmo10010CfgfanLowSpeedThreshold,
       "pmo10010CfgfanHighSpeedThreshold": pmo10010CfgfanHighSpeedThreshold,
       "pmo10010CfgOdu2Clienta": pmo10010CfgOdu2Clienta,
       "pmo10010CfgClientStartupOduTable": pmo10010CfgClientStartupOduTable,
       "pmo10010CfgClientStartupOduEntry": pmo10010CfgClientStartupOduEntry,
       "pmo10010CfgClientStartupOduIndex": pmo10010CfgClientStartupOduIndex,
       "pmo10010CfgOdu2ReserveLsbPortn": pmo10010CfgOdu2ReserveLsbPortn,
       "pmo10010CfgOdu2DegthresholdMsbPortn": pmo10010CfgOdu2DegthresholdMsbPortn,
       "pmo10010CfgOdu2DegmPortn": pmo10010CfgOdu2DegmPortn,
       "pmo10010CfgOdu2SettingsPortn": pmo10010CfgOdu2SettingsPortn,
       "pmo10010CfgOtu4Line": pmo10010CfgOtu4Line,
       "pmo10010CfgLinexStartupOtuTable": pmo10010CfgLinexStartupOtuTable,
       "pmo10010CfgLinexStartupOtuEntry": pmo10010CfgLinexStartupOtuEntry,
       "pmo10010CfgLinexStartupOtuIndex": pmo10010CfgLinexStartupOtuIndex,
       "pmo10010CfgOtu4ReserveLsbPortn": pmo10010CfgOtu4ReserveLsbPortn,
       "pmo10010CfgOtu4DegthresholdMsbPortn": pmo10010CfgOtu4DegthresholdMsbPortn,
       "pmo10010CfgOtu4DegmPortn": pmo10010CfgOtu4DegmPortn,
       "pmo10010CfgOtu4SettingsPortn": pmo10010CfgOtu4SettingsPortn,
       "pmo10010CfgOdu4Line": pmo10010CfgOdu4Line,
       "pmo10010CfgLinexStartupOduTable": pmo10010CfgLinexStartupOduTable,
       "pmo10010CfgLinexStartupOduEntry": pmo10010CfgLinexStartupOduEntry,
       "pmo10010CfgLinexStartupOduIndex": pmo10010CfgLinexStartupOduIndex,
       "pmo10010CfgOdu4ReserveLsbPortn": pmo10010CfgOdu4ReserveLsbPortn,
       "pmo10010CfgOdu4DegthresholdMsbPortn": pmo10010CfgOdu4DegthresholdMsbPortn,
       "pmo10010CfgOdu4DegmPortn": pmo10010CfgOdu4DegmPortn,
       "pmo10010CfgOdu4SettingsPortn": pmo10010CfgOdu4SettingsPortn,
       "pmo10010CfgSapiTxClient": pmo10010CfgSapiTxClient,
       "pmo10010CfgClientSapiTxOduTable": pmo10010CfgClientSapiTxOduTable,
       "pmo10010CfgClientSapiTxOduEntry": pmo10010CfgClientSapiTxOduEntry,
       "pmo10010CfgClientSapiTxOduIndex": pmo10010CfgClientSapiTxOduIndex,
       "pmo10010CfgClientSapiTxSetupPortn": pmo10010CfgClientSapiTxSetupPortn,
       "pmo10010CfgSapiExpClient": pmo10010CfgSapiExpClient,
       "pmo10010CfgClientSapiExpOduTable": pmo10010CfgClientSapiExpOduTable,
       "pmo10010CfgClientSapiExpOduEntry": pmo10010CfgClientSapiExpOduEntry,
       "pmo10010CfgClientSapiExpOduIndex": pmo10010CfgClientSapiExpOduIndex,
       "pmo10010CfgClientSapiExpSetupPortn": pmo10010CfgClientSapiExpSetupPortn,
       "pmo10010CfgSapiAccClient": pmo10010CfgSapiAccClient,
       "pmo10010CfgClientSapiAccOduTable": pmo10010CfgClientSapiAccOduTable,
       "pmo10010CfgClientSapiAccOduEntry": pmo10010CfgClientSapiAccOduEntry,
       "pmo10010CfgClientSapiAccOduIndex": pmo10010CfgClientSapiAccOduIndex,
       "pmo10010CfgClientSapiAccSetupPortn": pmo10010CfgClientSapiAccSetupPortn,
       "pmo10010CfgDapiTxClient": pmo10010CfgDapiTxClient,
       "pmo10010CfgClientDapiTxOduTable": pmo10010CfgClientDapiTxOduTable,
       "pmo10010CfgClientDapiTxOduEntry": pmo10010CfgClientDapiTxOduEntry,
       "pmo10010CfgClientDapiTxOduIndex": pmo10010CfgClientDapiTxOduIndex,
       "pmo10010CfgClientDapiTxSetupPortn": pmo10010CfgClientDapiTxSetupPortn,
       "pmo10010CfgDapiExpClient": pmo10010CfgDapiExpClient,
       "pmo10010CfgClientDapiExpOduTable": pmo10010CfgClientDapiExpOduTable,
       "pmo10010CfgClientDapiExpOduEntry": pmo10010CfgClientDapiExpOduEntry,
       "pmo10010CfgClientDapiExpOduIndex": pmo10010CfgClientDapiExpOduIndex,
       "pmo10010CfgClientDapiExpSetupPortn": pmo10010CfgClientDapiExpSetupPortn,
       "pmo10010CfgDapiAccClient": pmo10010CfgDapiAccClient,
       "pmo10010CfgClientDapiAccOduTable": pmo10010CfgClientDapiAccOduTable,
       "pmo10010CfgClientDapiAccOduEntry": pmo10010CfgClientDapiAccOduEntry,
       "pmo10010CfgClientDapiAccOduIndex": pmo10010CfgClientDapiAccOduIndex,
       "pmo10010CfgClientDapiAccSetupPortn": pmo10010CfgClientDapiAccSetupPortn,
       "pmo10010CfgSapiTxLineOtu4": pmo10010CfgSapiTxLineOtu4,
       "pmo10010CfgLineSapiTxOtuTable": pmo10010CfgLineSapiTxOtuTable,
       "pmo10010CfgLineSapiTxOtuEntry": pmo10010CfgLineSapiTxOtuEntry,
       "pmo10010CfgLineSapiTxOtuIndex": pmo10010CfgLineSapiTxOtuIndex,
       "pmo10010CfgLineSapiTxSetupOtuPortn": pmo10010CfgLineSapiTxSetupOtuPortn,
       "pmo10010CfgSapiExpLineOtu4": pmo10010CfgSapiExpLineOtu4,
       "pmo10010CfgLineSapiExpOtuTable": pmo10010CfgLineSapiExpOtuTable,
       "pmo10010CfgLineSapiExpOtuEntry": pmo10010CfgLineSapiExpOtuEntry,
       "pmo10010CfgLineSapiExpOtuIndex": pmo10010CfgLineSapiExpOtuIndex,
       "pmo10010CfgLineSapiExpSetupOtuPortn": pmo10010CfgLineSapiExpSetupOtuPortn,
       "pmo10010CfgSapiAccLineOtu4": pmo10010CfgSapiAccLineOtu4,
       "pmo10010CfgLineSapiAccOtuTable": pmo10010CfgLineSapiAccOtuTable,
       "pmo10010CfgLineSapiAccOtuEntry": pmo10010CfgLineSapiAccOtuEntry,
       "pmo10010CfgLineSapiAccOtuIndex": pmo10010CfgLineSapiAccOtuIndex,
       "pmo10010CfgLineSapiAccSetupOtuPortn": pmo10010CfgLineSapiAccSetupOtuPortn,
       "pmo10010CfgDapiTxLineOtu4": pmo10010CfgDapiTxLineOtu4,
       "pmo10010CfgLineDapiTxOtuTable": pmo10010CfgLineDapiTxOtuTable,
       "pmo10010CfgLineDapiTxOtuEntry": pmo10010CfgLineDapiTxOtuEntry,
       "pmo10010CfgLineDapiTxOtuIndex": pmo10010CfgLineDapiTxOtuIndex,
       "pmo10010CfgLineDapiTxSetupOtuPortn": pmo10010CfgLineDapiTxSetupOtuPortn,
       "pmo10010CfgDapiExpLineOtu4": pmo10010CfgDapiExpLineOtu4,
       "pmo10010CfgLineDapiExpOtuTable": pmo10010CfgLineDapiExpOtuTable,
       "pmo10010CfgLineDapiExpOtuEntry": pmo10010CfgLineDapiExpOtuEntry,
       "pmo10010CfgLineDapiExpOtuIndex": pmo10010CfgLineDapiExpOtuIndex,
       "pmo10010CfgLineDapiExpSetupOtuPortn": pmo10010CfgLineDapiExpSetupOtuPortn,
       "pmo10010CfgDapiAccLineOtu4": pmo10010CfgDapiAccLineOtu4,
       "pmo10010CfgLineDapiAccOtuTable": pmo10010CfgLineDapiAccOtuTable,
       "pmo10010CfgLineDapiAccOtuEntry": pmo10010CfgLineDapiAccOtuEntry,
       "pmo10010CfgLineDapiAccOtuIndex": pmo10010CfgLineDapiAccOtuIndex,
       "pmo10010CfgLineDapiAccSetupOtuPortn": pmo10010CfgLineDapiAccSetupOtuPortn,
       "pmo10010CfgSapiTxLineOdu4": pmo10010CfgSapiTxLineOdu4,
       "pmo10010CfgLineSapiTxOduTable": pmo10010CfgLineSapiTxOduTable,
       "pmo10010CfgLineSapiTxOduEntry": pmo10010CfgLineSapiTxOduEntry,
       "pmo10010CfgLineSapiTxOduIndex": pmo10010CfgLineSapiTxOduIndex,
       "pmo10010CfgLineSapiTxSetupOduPortn": pmo10010CfgLineSapiTxSetupOduPortn,
       "pmo10010CfgSapiExpLineOdu4": pmo10010CfgSapiExpLineOdu4,
       "pmo10010CfgLineSapiExpOduTable": pmo10010CfgLineSapiExpOduTable,
       "pmo10010CfgLineSapiExpOduEntry": pmo10010CfgLineSapiExpOduEntry,
       "pmo10010CfgLineSapiExpOduIndex": pmo10010CfgLineSapiExpOduIndex,
       "pmo10010CfgLineSapiExpSetupOduPortn": pmo10010CfgLineSapiExpSetupOduPortn,
       "pmo10010CfgSapiAccLineOdu4": pmo10010CfgSapiAccLineOdu4,
       "pmo10010CfgLineSapiAccOduTable": pmo10010CfgLineSapiAccOduTable,
       "pmo10010CfgLineSapiAccOduEntry": pmo10010CfgLineSapiAccOduEntry,
       "pmo10010CfgLineSapiAccOduIndex": pmo10010CfgLineSapiAccOduIndex,
       "pmo10010CfgLineSapiAccSetupOduPortn": pmo10010CfgLineSapiAccSetupOduPortn,
       "pmo10010CfgDapiTxLineOdu4": pmo10010CfgDapiTxLineOdu4,
       "pmo10010CfgLineDapiTxOduTable": pmo10010CfgLineDapiTxOduTable,
       "pmo10010CfgLineDapiTxOduEntry": pmo10010CfgLineDapiTxOduEntry,
       "pmo10010CfgLineDapiTxOduIndex": pmo10010CfgLineDapiTxOduIndex,
       "pmo10010CfgLineDapiTxSetupOduPortn": pmo10010CfgLineDapiTxSetupOduPortn,
       "pmo10010CfgDapiExpLineOdu4": pmo10010CfgDapiExpLineOdu4,
       "pmo10010CfgLineDapiExpOduTable": pmo10010CfgLineDapiExpOduTable,
       "pmo10010CfgLineDapiExpOduEntry": pmo10010CfgLineDapiExpOduEntry,
       "pmo10010CfgLineDapiExpOduIndex": pmo10010CfgLineDapiExpOduIndex,
       "pmo10010CfgLineDapiExpSetupOduPortn": pmo10010CfgLineDapiExpSetupOduPortn,
       "pmo10010CfgDapiAccLineOdu4": pmo10010CfgDapiAccLineOdu4,
       "pmo10010CfgLineDapiAccOduTable": pmo10010CfgLineDapiAccOduTable,
       "pmo10010CfgLineDapiAccOduEntry": pmo10010CfgLineDapiAccOduEntry,
       "pmo10010CfgLineDapiAccOduIndex": pmo10010CfgLineDapiAccOduIndex,
       "pmo10010CfgLineDapiAccSetupOduPortn": pmo10010CfgLineDapiAccSetupOduPortn,
       "pmo10010CfgStartuptablefive": pmo10010CfgStartuptablefive,
       "pmo10010CfgOtxtlhcapabilitiesTable": pmo10010CfgOtxtlhcapabilitiesTable,
       "pmo10010CfgOtxtlhcapabilitiesEntry": pmo10010CfgOtxtlhcapabilitiesEntry,
       "pmo10010CfgOtxtlhcapabilitiesIndex": pmo10010CfgOtxtlhcapabilitiesIndex,
       "pmo10010CfgComponentTypePortn": pmo10010CfgComponentTypePortn,
       "pmo10010CfgMiscellaneousPortn": pmo10010CfgMiscellaneousPortn,
       "pmo10010CfgFirstChannelPortn": pmo10010CfgFirstChannelPortn,
       "pmo10010CfgLastChannelPortn": pmo10010CfgLastChannelPortn,
       "pmo10010CfgGridPortn": pmo10010CfgGridPortn,
       "pmo10010CfgWriteConfiguration": pmo10010CfgWriteConfiguration,
       "pmo10010traps": pmo10010traps,
       "pmo10010trapPortNumber": pmo10010trapPortNumber,
       "pmo10010trapLineNumber": pmo10010trapLineNumber,
       "pmo10010trapBoardNumber": pmo10010trapBoardNumber,
       "pmo10010LineTrapNotUrgentGoesOn": pmo10010LineTrapNotUrgentGoesOn,
       "pmo10010LineTrapNotUrgentGoesOff": pmo10010LineTrapNotUrgentGoesOff,
       "pmo10010LineTrapUrgentGoesOn": pmo10010LineTrapUrgentGoesOn,
       "pmo10010LineTrapUrgentGoesOff": pmo10010LineTrapUrgentGoesOff,
       "pmo10010LineTrapCritGoesOn": pmo10010LineTrapCritGoesOn,
       "pmo10010LineTrapCritGoesOff": pmo10010LineTrapCritGoesOff,
       "pmo10010ClientTrapNotUrgentGoesOn": pmo10010ClientTrapNotUrgentGoesOn,
       "pmo10010ClientTrapNotUrgentGoesOff": pmo10010ClientTrapNotUrgentGoesOff,
       "pmo10010ClientTrapUrgentGoesOn": pmo10010ClientTrapUrgentGoesOn,
       "pmo10010ClientTrapUrgentGoesOff": pmo10010ClientTrapUrgentGoesOff,
       "pmo10010ClientTrapCritGoesOn": pmo10010ClientTrapCritGoesOn,
       "pmo10010ClientTrapCritGoesOff": pmo10010ClientTrapCritGoesOff,
       "pmo10010PowerTrapUrgentGoesOn": pmo10010PowerTrapUrgentGoesOn,
       "pmo10010PowerTrapUrgentGoesOff": pmo10010PowerTrapUrgentGoesOff,
       "pmo10010Monitoring": pmo10010Monitoring,
       "pmo10010MonOther": pmo10010MonOther,
       "pmo10010MonRmon": pmo10010MonRmon,
       "pmo10010MonClient": pmo10010MonClient,
       "pmo10010MonClientRmonCounter": pmo10010MonClientRmonCounter,
       "pmo10010MonupRmonBytesCounterClientInputTable": pmo10010MonupRmonBytesCounterClientInputTable,
       "pmo10010MonupRmonBytesCounterClientInputEntry": pmo10010MonupRmonBytesCounterClientInputEntry,
       "pmo10010MonupRmonBytesCounterClientInputIndex": pmo10010MonupRmonBytesCounterClientInputIndex,
       "pmo10010MonupRmonBytesCounterClientInputValuePortn": pmo10010MonupRmonBytesCounterClientInputValuePortn,
       "pmo10010MonupRmonBytesCounterClientInputErrorPortn": pmo10010MonupRmonBytesCounterClientInputErrorPortn,
       "pmo10010MonupRmonBytesCounterClientInputOverloadPortn": pmo10010MonupRmonBytesCounterClientInputOverloadPortn,
       "pmo10010MonupRmonFcsErrorsCounterClientInputTable": pmo10010MonupRmonFcsErrorsCounterClientInputTable,
       "pmo10010MonupRmonFcsErrorsCounterClientInputEntry": pmo10010MonupRmonFcsErrorsCounterClientInputEntry,
       "pmo10010MonupRmonFcsErrorsCounterClientInputIndex": pmo10010MonupRmonFcsErrorsCounterClientInputIndex,
       "pmo10010MonupRmonFcsErrorsCounterClientInputValuePortn": pmo10010MonupRmonFcsErrorsCounterClientInputValuePortn,
       "pmo10010MonupRmonFcsErrorsCounterClientInputErrorPortn": pmo10010MonupRmonFcsErrorsCounterClientInputErrorPortn,
       "pmo10010MonupRmonFcsErrorsCounterClientInputOverloadPortn": pmo10010MonupRmonFcsErrorsCounterClientInputOverloadPortn,
       "pmo10010MonupRmonPacketsCounterClientInputTable": pmo10010MonupRmonPacketsCounterClientInputTable,
       "pmo10010MonupRmonPacketsCounterClientInputEntry": pmo10010MonupRmonPacketsCounterClientInputEntry,
       "pmo10010MonupRmonPacketsCounterClientInputIndex": pmo10010MonupRmonPacketsCounterClientInputIndex,
       "pmo10010MonupRmonPacketsCounterClientInputValuePortn": pmo10010MonupRmonPacketsCounterClientInputValuePortn,
       "pmo10010MonupRmonPacketsCounterClientInputErrorPortn": pmo10010MonupRmonPacketsCounterClientInputErrorPortn,
       "pmo10010MonupRmonPacketsCounterClientInputOverloadPortn": pmo10010MonupRmonPacketsCounterClientInputOverloadPortn,
       "pmo10010MonupRmonBroadcastCounterClientInputTable": pmo10010MonupRmonBroadcastCounterClientInputTable,
       "pmo10010MonupRmonBroadcastCounterClientInputEntry": pmo10010MonupRmonBroadcastCounterClientInputEntry,
       "pmo10010MonupRmonBroadcastCounterClientInputIndex": pmo10010MonupRmonBroadcastCounterClientInputIndex,
       "pmo10010MonupRmonBroadcastCounterClientInputValuePortn": pmo10010MonupRmonBroadcastCounterClientInputValuePortn,
       "pmo10010MonupRmonBroadcastCounterClientInputErrorPortn": pmo10010MonupRmonBroadcastCounterClientInputErrorPortn,
       "pmo10010MonupRmonBroadcastCounterClientInputOverloadPortn": pmo10010MonupRmonBroadcastCounterClientInputOverloadPortn,
       "pmo10010MonupRmonMulticastCounterClientInputTable": pmo10010MonupRmonMulticastCounterClientInputTable,
       "pmo10010MonupRmonMulticastCounterClientInputEntry": pmo10010MonupRmonMulticastCounterClientInputEntry,
       "pmo10010MonupRmonMulticastCounterClientInputIndex": pmo10010MonupRmonMulticastCounterClientInputIndex,
       "pmo10010MonupRmonMulticastCounterClientInputValuePortn": pmo10010MonupRmonMulticastCounterClientInputValuePortn,
       "pmo10010MonupRmonMulticastCounterClientInputErrorPortn": pmo10010MonupRmonMulticastCounterClientInputErrorPortn,
       "pmo10010MonupRmonMulticastCounterClientInputOverloadPortn": pmo10010MonupRmonMulticastCounterClientInputOverloadPortn,
       "pmo10010MonupRmonPauseFrameCounterClientInputTable": pmo10010MonupRmonPauseFrameCounterClientInputTable,
       "pmo10010MonupRmonPauseFrameCounterClientInputEntry": pmo10010MonupRmonPauseFrameCounterClientInputEntry,
       "pmo10010MonupRmonPauseFrameCounterClientInputIndex": pmo10010MonupRmonPauseFrameCounterClientInputIndex,
       "pmo10010MonupRmonPauseFrameCounterClientInputValuePortn": pmo10010MonupRmonPauseFrameCounterClientInputValuePortn,
       "pmo10010MonupRmonPauseFrameCounterClientInputErrorPortn": pmo10010MonupRmonPauseFrameCounterClientInputErrorPortn,
       "pmo10010MonupRmonPauseFrameCounterClientInputOverloadPortn": pmo10010MonupRmonPauseFrameCounterClientInputOverloadPortn,
       "pmo10010MonupRmonUnicastCounterClientInputTable": pmo10010MonupRmonUnicastCounterClientInputTable,
       "pmo10010MonupRmonUnicastCounterClientInputEntry": pmo10010MonupRmonUnicastCounterClientInputEntry,
       "pmo10010MonupRmonUnicastCounterClientInputIndex": pmo10010MonupRmonUnicastCounterClientInputIndex,
       "pmo10010MonupRmonUnicastCounterClientInputValuePortn": pmo10010MonupRmonUnicastCounterClientInputValuePortn,
       "pmo10010MonupRmonUnicastCounterClientInputErrorPortn": pmo10010MonupRmonUnicastCounterClientInputErrorPortn,
       "pmo10010MonupRmonUnicastCounterClientInputOverloadPortn": pmo10010MonupRmonUnicastCounterClientInputOverloadPortn,
       "pmo10010MonupRmonNonunicastCounterClientInputTable": pmo10010MonupRmonNonunicastCounterClientInputTable,
       "pmo10010MonupRmonNonunicastCounterClientInputEntry": pmo10010MonupRmonNonunicastCounterClientInputEntry,
       "pmo10010MonupRmonNonunicastCounterClientInputIndex": pmo10010MonupRmonNonunicastCounterClientInputIndex,
       "pmo10010MonupRmonNonunicastCounterClientInputValuePortn": pmo10010MonupRmonNonunicastCounterClientInputValuePortn,
       "pmo10010MonupRmonNonunicastCounterClientInputErrorPortn": pmo10010MonupRmonNonunicastCounterClientInputErrorPortn,
       "pmo10010MonupRmonNonunicastCounterClientInputOverloadPortn": pmo10010MonupRmonNonunicastCounterClientInputOverloadPortn,
       "pmo10010MondownRmonBytesCounterClientOutputTable": pmo10010MondownRmonBytesCounterClientOutputTable,
       "pmo10010MondownRmonBytesCounterClientOutputEntry": pmo10010MondownRmonBytesCounterClientOutputEntry,
       "pmo10010MondownRmonBytesCounterClientOutputIndex": pmo10010MondownRmonBytesCounterClientOutputIndex,
       "pmo10010MondownRmonBytesCounterClientOutputValuePortn": pmo10010MondownRmonBytesCounterClientOutputValuePortn,
       "pmo10010MondownRmonBytesCounterClientOutputErrorPortn": pmo10010MondownRmonBytesCounterClientOutputErrorPortn,
       "pmo10010MondownRmonBytesCounterClientOutputOverloadPortn": pmo10010MondownRmonBytesCounterClientOutputOverloadPortn,
       "pmo10010MondownRmonFcsErrorsCounterClientOutputTable": pmo10010MondownRmonFcsErrorsCounterClientOutputTable,
       "pmo10010MondownRmonFcsErrorsCounterClientOutputEntry": pmo10010MondownRmonFcsErrorsCounterClientOutputEntry,
       "pmo10010MondownRmonFcsErrorsCounterClientOutputIndex": pmo10010MondownRmonFcsErrorsCounterClientOutputIndex,
       "pmo10010MondownRmonFcsErrorsCounterClientOutputValuePortn": pmo10010MondownRmonFcsErrorsCounterClientOutputValuePortn,
       "pmo10010MondownRmonFcsErrorsCounterClientOutputErrorPortn": pmo10010MondownRmonFcsErrorsCounterClientOutputErrorPortn,
       "pmo10010MondownRmonFcsErrorsCounterClientOutputOverloadPortn": pmo10010MondownRmonFcsErrorsCounterClientOutputOverloadPortn,
       "pmo10010MondownRmonPacketsCounterClientOutputTable": pmo10010MondownRmonPacketsCounterClientOutputTable,
       "pmo10010MondownRmonPacketsCounterClientOutputEntry": pmo10010MondownRmonPacketsCounterClientOutputEntry,
       "pmo10010MondownRmonPacketsCounterClientOutputIndex": pmo10010MondownRmonPacketsCounterClientOutputIndex,
       "pmo10010MondownRmonPacketsCounterClientOutputValuePortn": pmo10010MondownRmonPacketsCounterClientOutputValuePortn,
       "pmo10010MondownRmonPacketsCounterClientOutputErrorPortn": pmo10010MondownRmonPacketsCounterClientOutputErrorPortn,
       "pmo10010MondownRmonPacketsCounterClientOutputOverloadPortn": pmo10010MondownRmonPacketsCounterClientOutputOverloadPortn,
       "pmo10010MondownRmonBroadcastCounterClientOutputTable": pmo10010MondownRmonBroadcastCounterClientOutputTable,
       "pmo10010MondownRmonBroadcastCounterClientOutputEntry": pmo10010MondownRmonBroadcastCounterClientOutputEntry,
       "pmo10010MondownRmonBroadcastCounterClientOutputIndex": pmo10010MondownRmonBroadcastCounterClientOutputIndex,
       "pmo10010MondownRmonBroadcastCounterClientOutputValuePortn": pmo10010MondownRmonBroadcastCounterClientOutputValuePortn,
       "pmo10010MondownRmonBroadcastCounterClientOutputErrorPortn": pmo10010MondownRmonBroadcastCounterClientOutputErrorPortn,
       "pmo10010MondownRmonBroadcastCounterClientOutputOverloadPortn": pmo10010MondownRmonBroadcastCounterClientOutputOverloadPortn,
       "pmo10010MondownRmonMulticastCounterClientOutputTable": pmo10010MondownRmonMulticastCounterClientOutputTable,
       "pmo10010MondownRmonMulticastCounterClientOutputEntry": pmo10010MondownRmonMulticastCounterClientOutputEntry,
       "pmo10010MondownRmonMulticastCounterClientOutputIndex": pmo10010MondownRmonMulticastCounterClientOutputIndex,
       "pmo10010MondownRmonMulticastCounterClientOutputValuePortn": pmo10010MondownRmonMulticastCounterClientOutputValuePortn,
       "pmo10010MondownRmonMulticastCounterClientOutputErrorPortn": pmo10010MondownRmonMulticastCounterClientOutputErrorPortn,
       "pmo10010MondownRmonMulticastCounterClientOutputOverloadPortn": pmo10010MondownRmonMulticastCounterClientOutputOverloadPortn,
       "pmo10010MondownRmonPauseFrameCounterClientOutputTable": pmo10010MondownRmonPauseFrameCounterClientOutputTable,
       "pmo10010MondownRmonPauseFrameCounterClientOutputEntry": pmo10010MondownRmonPauseFrameCounterClientOutputEntry,
       "pmo10010MondownRmonPauseFrameCounterClientOutputIndex": pmo10010MondownRmonPauseFrameCounterClientOutputIndex,
       "pmo10010MondownRmonPauseFrameCounterClientOutputValuePortn": pmo10010MondownRmonPauseFrameCounterClientOutputValuePortn,
       "pmo10010MondownRmonPauseFrameCounterClientOutputErrorPortn": pmo10010MondownRmonPauseFrameCounterClientOutputErrorPortn,
       "pmo10010MondownRmonPauseFrameCounterClientOutputOverloadPortn": pmo10010MondownRmonPauseFrameCounterClientOutputOverloadPortn,
       "pmo10010MondownRmonUnicastCounterClientOutputTable": pmo10010MondownRmonUnicastCounterClientOutputTable,
       "pmo10010MondownRmonUnicastCounterClientOutputEntry": pmo10010MondownRmonUnicastCounterClientOutputEntry,
       "pmo10010MondownRmonUnicastCounterClientOutputIndex": pmo10010MondownRmonUnicastCounterClientOutputIndex,
       "pmo10010MondownRmonUnicastCounterClientOutputValuePortn": pmo10010MondownRmonUnicastCounterClientOutputValuePortn,
       "pmo10010MondownRmonUnicastCounterClientOutputErrorPortn": pmo10010MondownRmonUnicastCounterClientOutputErrorPortn,
       "pmo10010MondownRmonUnicastCounterClientOutputOverloadPortn": pmo10010MondownRmonUnicastCounterClientOutputOverloadPortn,
       "pmo10010MondownRmonNonunicastCounterClientOutputTable": pmo10010MondownRmonNonunicastCounterClientOutputTable,
       "pmo10010MondownRmonNonunicastCounterClientOutputEntry": pmo10010MondownRmonNonunicastCounterClientOutputEntry,
       "pmo10010MondownRmonNonunicastCounterClientOutputIndex": pmo10010MondownRmonNonunicastCounterClientOutputIndex,
       "pmo10010MondownRmonNonunicastCounterClientOutputValuePortn": pmo10010MondownRmonNonunicastCounterClientOutputValuePortn,
       "pmo10010MondownRmonNonunicastCounterClientOutputErrorPortn": pmo10010MondownRmonNonunicastCounterClientOutputErrorPortn,
       "pmo10010MondownRmonNonunicastCounterClientOutputOverloadPortn": pmo10010MondownRmonNonunicastCounterClientOutputOverloadPortn}
)
