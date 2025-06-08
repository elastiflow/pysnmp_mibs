# SNMP MIB module (SNMPSERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/tecnair_53332/SNMPSERVER-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 12:04:33 2025
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
 dod,
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "dod",
    "iso",
    "mib-2")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Mgmt_ObjectIdentity = ObjectIdentity
mgmt = _Mgmt_ObjectIdentity(
    (1, 3, 6, 1, 2)
)
_Mib_2_ObjectIdentity = ObjectIdentity
mib_2 = _Mib_2_ObjectIdentity(
    (1, 3, 6, 1, 2, 1)
)
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 1)
)
_SysDescr_Type = DisplayString
_SysDescr_Object = MibScalar
sysDescr = _SysDescr_Object(
    (1, 3, 6, 1, 2, 1, 1, 1),
    _SysDescr_Type()
)
sysDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDescr.setStatus("current")
_SysObjectID_Type = ObjectIdentifier
_SysObjectID_Object = MibScalar
sysObjectID = _SysObjectID_Object(
    (1, 3, 6, 1, 2, 1, 1, 2),
    _SysObjectID_Type()
)
sysObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysObjectID.setStatus("current")
_SysUpTime_Type = TimeTicks
_SysUpTime_Object = MibScalar
sysUpTime = _SysUpTime_Object(
    (1, 3, 6, 1, 2, 1, 1, 3),
    _SysUpTime_Type()
)
sysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysUpTime.setStatus("current")
_SysContact_Type = DisplayString
_SysContact_Object = MibScalar
sysContact = _SysContact_Object(
    (1, 3, 6, 1, 2, 1, 1, 4),
    _SysContact_Type()
)
sysContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysContact.setStatus("current")
_SysName_Type = DisplayString
_SysName_Object = MibScalar
sysName = _SysName_Object(
    (1, 3, 6, 1, 2, 1, 1, 5),
    _SysName_Type()
)
sysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysName.setStatus("current")
_SysLocation_Type = DisplayString
_SysLocation_Object = MibScalar
sysLocation = _SysLocation_Object(
    (1, 3, 6, 1, 2, 1, 1, 6),
    _SysLocation_Type()
)
sysLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLocation.setStatus("current")
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Tecnairlv_ObjectIdentity = ObjectIdentity
tecnairlv = _Tecnairlv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 53332)
)
_Node1_ObjectIdentity = ObjectIdentity
node1 = _Node1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 53332, 1)
)
_Traps1_ObjectIdentity = ObjectIdentity
traps1 = _Traps1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0)
)
_BinaryObjects1_ObjectIdentity = ObjectIdentity
binaryObjects1 = _BinaryObjects1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1)
)
_DamperStatusDI_1_Type = Integer32
_DamperStatusDI_1_Object = MibScalar
damperStatusDI_1 = _DamperStatusDI_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 1),
    _DamperStatusDI_1_Type()
)
damperStatusDI_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    damperStatusDI_1.setStatus("current")
_DirtyFilterDI_1_Type = Integer32
_DirtyFilterDI_1_Object = MibScalar
dirtyFilterDI_1 = _DirtyFilterDI_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 2),
    _DirtyFilterDI_1_Type()
)
dirtyFilterDI_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dirtyFilterDI_1.setStatus("current")
_RemoteOffDI_1_Type = Integer32
_RemoteOffDI_1_Object = MibScalar
remoteOffDI_1 = _RemoteOffDI_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 3),
    _RemoteOffDI_1_Type()
)
remoteOffDI_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteOffDI_1.setStatus("current")
_ElHeaterAlarmDI_1_Type = Integer32
_ElHeaterAlarmDI_1_Object = MibScalar
elHeaterAlarmDI_1 = _ElHeaterAlarmDI_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 4),
    _ElHeaterAlarmDI_1_Type()
)
elHeaterAlarmDI_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elHeaterAlarmDI_1.setStatus("current")
_CondPumpAlarmDI_1_Type = Integer32
_CondPumpAlarmDI_1_Object = MibScalar
condPumpAlarmDI_1 = _CondPumpAlarmDI_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 5),
    _CondPumpAlarmDI_1_Type()
)
condPumpAlarmDI_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    condPumpAlarmDI_1.setStatus("current")
_ConfigurableDI1_1_Type = Integer32
_ConfigurableDI1_1_Object = MibScalar
configurableDI1_1 = _ConfigurableDI1_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 6),
    _ConfigurableDI1_1_Type()
)
configurableDI1_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configurableDI1_1.setStatus("current")
_ConfigurableDI2_1_Type = Integer32
_ConfigurableDI2_1_Object = MibScalar
configurableDI2_1 = _ConfigurableDI2_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 7),
    _ConfigurableDI2_1_Type()
)
configurableDI2_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configurableDI2_1.setStatus("current")
_ConfigurableDI3_1_Type = Integer32
_ConfigurableDI3_1_Object = MibScalar
configurableDI3_1 = _ConfigurableDI3_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 8),
    _ConfigurableDI3_1_Type()
)
configurableDI3_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configurableDI3_1.setStatus("current")
_ConfigurableDI4_1_Type = Integer32
_ConfigurableDI4_1_Object = MibScalar
configurableDI4_1 = _ConfigurableDI4_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 9),
    _ConfigurableDI4_1_Type()
)
configurableDI4_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configurableDI4_1.setStatus("current")
_ConfigurableDI5_1_Type = Integer32
_ConfigurableDI5_1_Object = MibScalar
configurableDI5_1 = _ConfigurableDI5_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 10),
    _ConfigurableDI5_1_Type()
)
configurableDI5_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configurableDI5_1.setStatus("current")
_C1ThermAlarmDI_1_Type = Integer32
_C1ThermAlarmDI_1_Object = MibScalar
c1ThermAlarmDI_1 = _C1ThermAlarmDI_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 11),
    _C1ThermAlarmDI_1_Type()
)
c1ThermAlarmDI_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c1ThermAlarmDI_1.setStatus("current")
_C1HPAlarmDI_1_Type = Integer32
_C1HPAlarmDI_1_Object = MibScalar
c1HPAlarmDI_1 = _C1HPAlarmDI_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 12),
    _C1HPAlarmDI_1_Type()
)
c1HPAlarmDI_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c1HPAlarmDI_1.setStatus("current")
_C1LPAlarmDI_1_Type = Integer32
_C1LPAlarmDI_1_Object = MibScalar
c1LPAlarmDI_1 = _C1LPAlarmDI_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 13),
    _C1LPAlarmDI_1_Type()
)
c1LPAlarmDI_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c1LPAlarmDI_1.setStatus("current")
_C2ThermAlarmDI_1_Type = Integer32
_C2ThermAlarmDI_1_Object = MibScalar
c2ThermAlarmDI_1 = _C2ThermAlarmDI_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 14),
    _C2ThermAlarmDI_1_Type()
)
c2ThermAlarmDI_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2ThermAlarmDI_1.setStatus("current")
_C2HPAlarmDI_1_Type = Integer32
_C2HPAlarmDI_1_Object = MibScalar
c2HPAlarmDI_1 = _C2HPAlarmDI_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 15),
    _C2HPAlarmDI_1_Type()
)
c2HPAlarmDI_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2HPAlarmDI_1.setStatus("current")
_C2LPAlarmDI_1_Type = Integer32
_C2LPAlarmDI_1_Object = MibScalar
c2LPAlarmDI_1 = _C2LPAlarmDI_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 16),
    _C2LPAlarmDI_1_Type()
)
c2LPAlarmDI_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2LPAlarmDI_1.setStatus("current")
_FansDO_1_Type = Integer32
_FansDO_1_Object = MibScalar
fansDO_1 = _FansDO_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 17),
    _FansDO_1_Type()
)
fansDO_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fansDO_1.setStatus("current")
_DamperDO_1_Type = Integer32
_DamperDO_1_Object = MibScalar
damperDO_1 = _DamperDO_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 18),
    _DamperDO_1_Type()
)
damperDO_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    damperDO_1.setStatus("current")
_ConfigurableDO1_1_Type = Integer32
_ConfigurableDO1_1_Object = MibScalar
configurableDO1_1 = _ConfigurableDO1_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 19),
    _ConfigurableDO1_1_Type()
)
configurableDO1_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configurableDO1_1.setStatus("current")
_ConfigurableDO2_1_Type = Integer32
_ConfigurableDO2_1_Object = MibScalar
configurableDO2_1 = _ConfigurableDO2_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 20),
    _ConfigurableDO2_1_Type()
)
configurableDO2_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configurableDO2_1.setStatus("current")
_ConfigurableDO3_1_Type = Integer32
_ConfigurableDO3_1_Object = MibScalar
configurableDO3_1 = _ConfigurableDO3_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 21),
    _ConfigurableDO3_1_Type()
)
configurableDO3_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configurableDO3_1.setStatus("current")
_ConfigurableDO4_1_Type = Integer32
_ConfigurableDO4_1_Object = MibScalar
configurableDO4_1 = _ConfigurableDO4_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 22),
    _ConfigurableDO4_1_Type()
)
configurableDO4_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configurableDO4_1.setStatus("current")
_ConfigurableDO5_1_Type = Integer32
_ConfigurableDO5_1_Object = MibScalar
configurableDO5_1 = _ConfigurableDO5_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 23),
    _ConfigurableDO5_1_Type()
)
configurableDO5_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configurableDO5_1.setStatus("current")
_EHeaterStage1DO_1_Type = Integer32
_EHeaterStage1DO_1_Object = MibScalar
eHeaterStage1DO_1 = _EHeaterStage1DO_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 24),
    _EHeaterStage1DO_1_Type()
)
eHeaterStage1DO_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eHeaterStage1DO_1.setStatus("current")
_EHeaterStage2DO_1_Type = Integer32
_EHeaterStage2DO_1_Object = MibScalar
eHeaterStage2DO_1 = _EHeaterStage2DO_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 25),
    _EHeaterStage2DO_1_Type()
)
eHeaterStage2DO_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eHeaterStage2DO_1.setStatus("current")
_Compressor1DO_1_Type = Integer32
_Compressor1DO_1_Object = MibScalar
compressor1DO_1 = _Compressor1DO_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 26),
    _Compressor1DO_1_Type()
)
compressor1DO_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compressor1DO_1.setStatus("current")
_Compressor2DO_1_Type = Integer32
_Compressor2DO_1_Object = MibScalar
compressor2DO_1 = _Compressor2DO_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 27),
    _Compressor2DO_1_Type()
)
compressor2DO_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compressor2DO_1.setStatus("current")
_HumPowerDO_1_Type = Integer32
_HumPowerDO_1_Object = MibScalar
humPowerDO_1 = _HumPowerDO_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 28),
    _HumPowerDO_1_Type()
)
humPowerDO_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humPowerDO_1.setStatus("current")
_HumDrainValveDO_1_Type = Integer32
_HumDrainValveDO_1_Object = MibScalar
humDrainValveDO_1 = _HumDrainValveDO_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 29),
    _HumDrainValveDO_1_Type()
)
humDrainValveDO_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humDrainValveDO_1.setStatus("current")
_HumFillValveDO_1_Type = Integer32
_HumFillValveDO_1_Object = MibScalar
humFillValveDO_1 = _HumFillValveDO_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 30),
    _HumFillValveDO_1_Type()
)
humFillValveDO_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humFillValveDO_1.setStatus("current")
_HumWaterLevel_1_Type = Integer32
_HumWaterLevel_1_Object = MibScalar
humWaterLevel_1 = _HumWaterLevel_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 31),
    _HumWaterLevel_1_Type()
)
humWaterLevel_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humWaterLevel_1.setStatus("current")
_SupervOFF_1_Type = Integer32
_SupervOFF_1_Object = MibScalar
supervOFF_1 = _SupervOFF_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 32),
    _SupervOFF_1_Type()
)
supervOFF_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    supervOFF_1.setStatus("current")
_EnableHumid_1_Type = Integer32
_EnableHumid_1_Object = MibScalar
enableHumid_1 = _EnableHumid_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 33),
    _EnableHumid_1_Type()
)
enableHumid_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableHumid_1.setStatus("current")
_HumManualDrain_1_Type = Integer32
_HumManualDrain_1_Object = MibScalar
humManualDrain_1 = _HumManualDrain_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 34),
    _HumManualDrain_1_Type()
)
humManualDrain_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humManualDrain_1.setStatus("current")
_HumCylWashing_1_Type = Integer32
_HumCylWashing_1_Object = MibScalar
humCylWashing_1 = _HumCylWashing_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 35),
    _HumCylWashing_1_Type()
)
humCylWashing_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humCylWashing_1.setStatus("current")
_TSManExchange_1_Type = Integer32
_TSManExchange_1_Object = MibScalar
tSManExchange_1 = _TSManExchange_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 36),
    _TSManExchange_1_Type()
)
tSManExchange_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tSManExchange_1.setStatus("current")
_TSTempExchEnab_1_Type = Integer32
_TSTempExchEnab_1_Object = MibScalar
tSTempExchEnab_1 = _TSTempExchEnab_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 37),
    _TSTempExchEnab_1_Type()
)
tSTempExchEnab_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tSTempExchEnab_1.setStatus("current")
_DamperAlRes_1_Type = Integer32
_DamperAlRes_1_Object = MibScalar
damperAlRes_1 = _DamperAlRes_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 38),
    _DamperAlRes_1_Type()
)
damperAlRes_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    damperAlRes_1.setStatus("current")
_FireSmokeAlRes_1_Type = Integer32
_FireSmokeAlRes_1_Object = MibScalar
fireSmokeAlRes_1 = _FireSmokeAlRes_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 39),
    _FireSmokeAlRes_1_Type()
)
fireSmokeAlRes_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fireSmokeAlRes_1.setStatus("current")
_GenSerAlRes_1_Type = Integer32
_GenSerAlRes_1_Object = MibScalar
genSerAlRes_1 = _GenSerAlRes_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 40),
    _GenSerAlRes_1_Type()
)
genSerAlRes_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genSerAlRes_1.setStatus("current")
_FansGenAlRes_1_Type = Integer32
_FansGenAlRes_1_Object = MibScalar
fansGenAlRes_1 = _FansGenAlRes_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 41),
    _FansGenAlRes_1_Type()
)
fansGenAlRes_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fansGenAlRes_1.setStatus("current")
_F1InvAlRes_1_Type = Integer32
_F1InvAlRes_1_Object = MibScalar
f1InvAlRes_1 = _F1InvAlRes_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 42),
    _F1InvAlRes_1_Type()
)
f1InvAlRes_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f1InvAlRes_1.setStatus("current")
_F2InvAlRes_1_Type = Integer32
_F2InvAlRes_1_Object = MibScalar
f2InvAlRes_1 = _F2InvAlRes_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 43),
    _F2InvAlRes_1_Type()
)
f2InvAlRes_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f2InvAlRes_1.setStatus("current")
_F3InvAlRes_1_Type = Integer32
_F3InvAlRes_1_Object = MibScalar
f3InvAlRes_1 = _F3InvAlRes_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 44),
    _F3InvAlRes_1_Type()
)
f3InvAlRes_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3InvAlRes_1.setStatus("current")
_F4InvAlRes_1_Type = Integer32
_F4InvAlRes_1_Object = MibScalar
f4InvAlRes_1 = _F4InvAlRes_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 45),
    _F4InvAlRes_1_Type()
)
f4InvAlRes_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f4InvAlRes_1.setStatus("current")
_F5InvAlRes_1_Type = Integer32
_F5InvAlRes_1_Object = MibScalar
f5InvAlRes_1 = _F5InvAlRes_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 46),
    _F5InvAlRes_1_Type()
)
f5InvAlRes_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f5InvAlRes_1.setStatus("current")
_F6InvAlRes_1_Type = Integer32
_F6InvAlRes_1_Object = MibScalar
f6InvAlRes_1 = _F6InvAlRes_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 47),
    _F6InvAlRes_1_Type()
)
f6InvAlRes_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f6InvAlRes_1.setStatus("current")
_F7InvAlRes_1_Type = Integer32
_F7InvAlRes_1_Object = MibScalar
f7InvAlRes_1 = _F7InvAlRes_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 48),
    _F7InvAlRes_1_Type()
)
f7InvAlRes_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f7InvAlRes_1.setStatus("current")
_F8InvAlRes_1_Type = Integer32
_F8InvAlRes_1_Object = MibScalar
f8InvAlRes_1 = _F8InvAlRes_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 49),
    _F8InvAlRes_1_Type()
)
f8InvAlRes_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f8InvAlRes_1.setStatus("current")
_F9InvAlRes_1_Type = Integer32
_F9InvAlRes_1_Object = MibScalar
f9InvAlRes_1 = _F9InvAlRes_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 50),
    _F9InvAlRes_1_Type()
)
f9InvAlRes_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f9InvAlRes_1.setStatus("current")
_F10InvAlRes_1_Type = Integer32
_F10InvAlRes_1_Object = MibScalar
f10InvAlRes_1 = _F10InvAlRes_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 51),
    _F10InvAlRes_1_Type()
)
f10InvAlRes_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f10InvAlRes_1.setStatus("current")
_InvCompAlRes_1_Type = Integer32
_InvCompAlRes_1_Object = MibScalar
invCompAlRes_1 = _InvCompAlRes_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 52),
    _InvCompAlRes_1_Type()
)
invCompAlRes_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    invCompAlRes_1.setStatus("current")
_C1ThermAlRes_1_Type = Integer32
_C1ThermAlRes_1_Object = MibScalar
c1ThermAlRes_1 = _C1ThermAlRes_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 53),
    _C1ThermAlRes_1_Type()
)
c1ThermAlRes_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c1ThermAlRes_1.setStatus("current")
_C1HighPresAlRes_1_Type = Integer32
_C1HighPresAlRes_1_Object = MibScalar
c1HighPresAlRes_1 = _C1HighPresAlRes_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 54),
    _C1HighPresAlRes_1_Type()
)
c1HighPresAlRes_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c1HighPresAlRes_1.setStatus("current")
_C1LowPresAlRes_1_Type = Integer32
_C1LowPresAlRes_1_Object = MibScalar
c1LowPresAlRes_1 = _C1LowPresAlRes_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 55),
    _C1LowPresAlRes_1_Type()
)
c1LowPresAlRes_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c1LowPresAlRes_1.setStatus("current")
_C1HighDisTAlRes_1_Type = Integer32
_C1HighDisTAlRes_1_Object = MibScalar
c1HighDisTAlRes_1 = _C1HighDisTAlRes_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 56),
    _C1HighDisTAlRes_1_Type()
)
c1HighDisTAlRes_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c1HighDisTAlRes_1.setStatus("current")
_C1LCompRatAlRes_1_Type = Integer32
_C1LCompRatAlRes_1_Object = MibScalar
c1LCompRatAlRes_1 = _C1LCompRatAlRes_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 57),
    _C1LCompRatAlRes_1_Type()
)
c1LCompRatAlRes_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c1LCompRatAlRes_1.setStatus("current")
_Condenser1AlRes_1_Type = Integer32
_Condenser1AlRes_1_Object = MibScalar
condenser1AlRes_1 = _Condenser1AlRes_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 58),
    _Condenser1AlRes_1_Type()
)
condenser1AlRes_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    condenser1AlRes_1.setStatus("current")
_EEV1AlRes_1_Type = Integer32
_EEV1AlRes_1_Object = MibScalar
eEV1AlRes_1 = _EEV1AlRes_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 59),
    _EEV1AlRes_1_Type()
)
eEV1AlRes_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eEV1AlRes_1.setStatus("current")
_C2ThermAlRes_1_Type = Integer32
_C2ThermAlRes_1_Object = MibScalar
c2ThermAlRes_1 = _C2ThermAlRes_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 60),
    _C2ThermAlRes_1_Type()
)
c2ThermAlRes_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c2ThermAlRes_1.setStatus("current")
_C2HighPresAlRes_1_Type = Integer32
_C2HighPresAlRes_1_Object = MibScalar
c2HighPresAlRes_1 = _C2HighPresAlRes_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 61),
    _C2HighPresAlRes_1_Type()
)
c2HighPresAlRes_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c2HighPresAlRes_1.setStatus("current")
_C2LowPresAlRes_1_Type = Integer32
_C2LowPresAlRes_1_Object = MibScalar
c2LowPresAlRes_1 = _C2LowPresAlRes_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 62),
    _C2LowPresAlRes_1_Type()
)
c2LowPresAlRes_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c2LowPresAlRes_1.setStatus("current")
_C2HighDisTAlRes_1_Type = Integer32
_C2HighDisTAlRes_1_Object = MibScalar
c2HighDisTAlRes_1 = _C2HighDisTAlRes_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 63),
    _C2HighDisTAlRes_1_Type()
)
c2HighDisTAlRes_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c2HighDisTAlRes_1.setStatus("current")
_C2LComRatAlRes_1_Type = Integer32
_C2LComRatAlRes_1_Object = MibScalar
c2LComRatAlRes_1 = _C2LComRatAlRes_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 64),
    _C2LComRatAlRes_1_Type()
)
c2LComRatAlRes_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c2LComRatAlRes_1.setStatus("current")
_Condenser2AlRes_1_Type = Integer32
_Condenser2AlRes_1_Object = MibScalar
condenser2AlRes_1 = _Condenser2AlRes_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 65),
    _Condenser2AlRes_1_Type()
)
condenser2AlRes_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    condenser2AlRes_1.setStatus("current")
_EEV2AlRes_1_Type = Integer32
_EEV2AlRes_1_Object = MibScalar
eEV2AlRes_1 = _EEV2AlRes_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 66),
    _EEV2AlRes_1_Type()
)
eEV2AlRes_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eEV2AlRes_1.setStatus("current")
_IntHumidifAlRes_1_Type = Integer32
_IntHumidifAlRes_1_Object = MibScalar
intHumidifAlRes_1 = _IntHumidifAlRes_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 67),
    _IntHumidifAlRes_1_Type()
)
intHumidifAlRes_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intHumidifAlRes_1.setStatus("current")
_WatPresAlRes_1_Type = Integer32
_WatPresAlRes_1_Object = MibScalar
watPresAlRes_1 = _WatPresAlRes_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 68),
    _WatPresAlRes_1_Type()
)
watPresAlRes_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    watPresAlRes_1.setStatus("current")
_DrainPumpAlRes_1_Type = Integer32
_DrainPumpAlRes_1_Object = MibScalar
drainPumpAlRes_1 = _DrainPumpAlRes_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 69),
    _DrainPumpAlRes_1_Type()
)
drainPumpAlRes_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drainPumpAlRes_1.setStatus("current")
_ElHeatAlRes_1_Type = Integer32
_ElHeatAlRes_1_Object = MibScalar
elHeatAlRes_1 = _ElHeatAlRes_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 70),
    _ElHeatAlRes_1_Type()
)
elHeatAlRes_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elHeatAlRes_1.setStatus("current")
_FilterAlRes_1_Type = Integer32
_FilterAlRes_1_Object = MibScalar
filterAlRes_1 = _FilterAlRes_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 71),
    _FilterAlRes_1_Type()
)
filterAlRes_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterAlRes_1.setStatus("current")
_DryCoolerAlRes_1_Type = Integer32
_DryCoolerAlRes_1_Object = MibScalar
dryCoolerAlRes_1 = _DryCoolerAlRes_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 72),
    _DryCoolerAlRes_1_Type()
)
dryCoolerAlRes_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dryCoolerAlRes_1.setStatus("current")
_ExtHumidifAlRes_1_Type = Integer32
_ExtHumidifAlRes_1_Object = MibScalar
extHumidifAlRes_1 = _ExtHumidifAlRes_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 73),
    _ExtHumidifAlRes_1_Type()
)
extHumidifAlRes_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extHumidifAlRes_1.setStatus("current")
_WaterPumpAlRes_1_Type = Integer32
_WaterPumpAlRes_1_Object = MibScalar
waterPumpAlRes_1 = _WaterPumpAlRes_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 74),
    _WaterPumpAlRes_1_Type()
)
waterPumpAlRes_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    waterPumpAlRes_1.setStatus("current")
_CondUnitGAlRes_1_Type = Integer32
_CondUnitGAlRes_1_Object = MibScalar
condUnitGAlRes_1 = _CondUnitGAlRes_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 75),
    _CondUnitGAlRes_1_Type()
)
condUnitGAlRes_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    condUnitGAlRes_1.setStatus("current")
_GasLeakAlRes_1_Type = Integer32
_GasLeakAlRes_1_Object = MibScalar
gasLeakAlRes_1 = _GasLeakAlRes_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 76),
    _GasLeakAlRes_1_Type()
)
gasLeakAlRes_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gasLeakAlRes_1.setStatus("current")
_PowerSupAlRes_1_Type = Integer32
_PowerSupAlRes_1_Object = MibScalar
powerSupAlRes_1 = _PowerSupAlRes_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 77),
    _PowerSupAlRes_1_Type()
)
powerSupAlRes_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerSupAlRes_1.setStatus("current")
_GenSoftAlRes_1_Type = Integer32
_GenSoftAlRes_1_Object = MibScalar
genSoftAlRes_1 = _GenSoftAlRes_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 1, 78),
    _GenSoftAlRes_1_Type()
)
genSoftAlRes_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genSoftAlRes_1.setStatus("current")
_ScalarsObjects1_ObjectIdentity = ObjectIdentity
scalarsObjects1 = _ScalarsObjects1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2)
)
_ConfDI1Combo_1_Type = Integer32
_ConfDI1Combo_1_Object = MibScalar
confDI1Combo_1 = _ConfDI1Combo_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 1),
    _ConfDI1Combo_1_Type()
)
confDI1Combo_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    confDI1Combo_1.setStatus("current")
_ConfDI2Combo_1_Type = Integer32
_ConfDI2Combo_1_Object = MibScalar
confDI2Combo_1 = _ConfDI2Combo_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 2),
    _ConfDI2Combo_1_Type()
)
confDI2Combo_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    confDI2Combo_1.setStatus("current")
_ConfDI3Combo_1_Type = Integer32
_ConfDI3Combo_1_Object = MibScalar
confDI3Combo_1 = _ConfDI3Combo_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 3),
    _ConfDI3Combo_1_Type()
)
confDI3Combo_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    confDI3Combo_1.setStatus("current")
_ConfDI4Combo_1_Type = Integer32
_ConfDI4Combo_1_Object = MibScalar
confDI4Combo_1 = _ConfDI4Combo_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 4),
    _ConfDI4Combo_1_Type()
)
confDI4Combo_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    confDI4Combo_1.setStatus("current")
_ConfDI5Combo_1_Type = Integer32
_ConfDI5Combo_1_Object = MibScalar
confDI5Combo_1 = _ConfDI5Combo_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 5),
    _ConfDI5Combo_1_Type()
)
confDI5Combo_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    confDI5Combo_1.setStatus("current")
_ConfDO1Combo_1_Type = Integer32
_ConfDO1Combo_1_Object = MibScalar
confDO1Combo_1 = _ConfDO1Combo_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 6),
    _ConfDO1Combo_1_Type()
)
confDO1Combo_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    confDO1Combo_1.setStatus("current")
_ConfDO2Combo_1_Type = Integer32
_ConfDO2Combo_1_Object = MibScalar
confDO2Combo_1 = _ConfDO2Combo_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 7),
    _ConfDO2Combo_1_Type()
)
confDO2Combo_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    confDO2Combo_1.setStatus("current")
_ConfDO3Combo_1_Type = Integer32
_ConfDO3Combo_1_Object = MibScalar
confDO3Combo_1 = _ConfDO3Combo_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 8),
    _ConfDO3Combo_1_Type()
)
confDO3Combo_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    confDO3Combo_1.setStatus("current")
_ConfDO4Combo_1_Type = Integer32
_ConfDO4Combo_1_Object = MibScalar
confDO4Combo_1 = _ConfDO4Combo_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 9),
    _ConfDO4Combo_1_Type()
)
confDO4Combo_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    confDO4Combo_1.setStatus("current")
_ConfDO5Combo_1_Type = Integer32
_ConfDO5Combo_1_Object = MibScalar
confDO5Combo_1 = _ConfDO5Combo_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 10),
    _ConfDO5Combo_1_Type()
)
confDO5Combo_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    confDO5Combo_1.setStatus("current")
_ReturnTemp_1_Type = Integer32
_ReturnTemp_1_Object = MibScalar
returnTemp_1 = _ReturnTemp_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 11),
    _ReturnTemp_1_Type()
)
returnTemp_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    returnTemp_1.setStatus("current")
_ReturnTAvg_1_Type = Integer32
_ReturnTAvg_1_Object = MibScalar
returnTAvg_1 = _ReturnTAvg_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 12),
    _ReturnTAvg_1_Type()
)
returnTAvg_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    returnTAvg_1.setStatus("current")
_SupplyTemp_1_Type = Integer32
_SupplyTemp_1_Object = MibScalar
supplyTemp_1 = _SupplyTemp_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 13),
    _SupplyTemp_1_Type()
)
supplyTemp_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supplyTemp_1.setStatus("current")
_SupplyTAvg_1_Type = Integer32
_SupplyTAvg_1_Object = MibScalar
supplyTAvg_1 = _SupplyTAvg_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 14),
    _SupplyTAvg_1_Type()
)
supplyTAvg_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supplyTAvg_1.setStatus("current")
_TempDelta_1_Type = Integer32
_TempDelta_1_Object = MibScalar
tempDelta_1 = _TempDelta_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 15),
    _TempDelta_1_Type()
)
tempDelta_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempDelta_1.setStatus("current")
_ReturnHumidity_1_Type = Integer32
_ReturnHumidity_1_Object = MibScalar
returnHumidity_1 = _ReturnHumidity_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 16),
    _ReturnHumidity_1_Type()
)
returnHumidity_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    returnHumidity_1.setStatus("current")
_ReturnHumAvg_1_Type = Integer32
_ReturnHumAvg_1_Object = MibScalar
returnHumAvg_1 = _ReturnHumAvg_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 17),
    _ReturnHumAvg_1_Type()
)
returnHumAvg_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    returnHumAvg_1.setStatus("current")
_SupplyHumidity_1_Type = Integer32
_SupplyHumidity_1_Object = MibScalar
supplyHumidity_1 = _SupplyHumidity_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 18),
    _SupplyHumidity_1_Type()
)
supplyHumidity_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supplyHumidity_1.setStatus("current")
_SupplyHumAvg_1_Type = Integer32
_SupplyHumAvg_1_Object = MibScalar
supplyHumAvg_1 = _SupplyHumAvg_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 19),
    _SupplyHumAvg_1_Type()
)
supplyHumAvg_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supplyHumAvg_1.setStatus("current")
_AirFlow_1_Type = Integer32
_AirFlow_1_Object = MibScalar
airFlow_1 = _AirFlow_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 20),
    _AirFlow_1_Type()
)
airFlow_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airFlow_1.setStatus("current")
_AirPressure_1_Type = Integer32
_AirPressure_1_Object = MibScalar
airPressure_1 = _AirPressure_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 22),
    _AirPressure_1_Type()
)
airPressure_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airPressure_1.setStatus("current")
_AirPressureAvg_1_Type = Integer32
_AirPressureAvg_1_Object = MibScalar
airPressureAvg_1 = _AirPressureAvg_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 23),
    _AirPressureAvg_1_Type()
)
airPressureAvg_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airPressureAvg_1.setStatus("current")
_NetMod1Combo1_1_Type = Integer32
_NetMod1Combo1_1_Object = MibScalar
netMod1Combo1_1 = _NetMod1Combo1_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 24),
    _NetMod1Combo1_1_Type()
)
netMod1Combo1_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod1Combo1_1.setStatus("current")
_NetMod1Probe1_1_Type = Integer32
_NetMod1Probe1_1_Object = MibScalar
netMod1Probe1_1 = _NetMod1Probe1_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 25),
    _NetMod1Probe1_1_Type()
)
netMod1Probe1_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod1Probe1_1.setStatus("current")
_NetMod1Combo2_1_Type = Integer32
_NetMod1Combo2_1_Object = MibScalar
netMod1Combo2_1 = _NetMod1Combo2_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 26),
    _NetMod1Combo2_1_Type()
)
netMod1Combo2_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod1Combo2_1.setStatus("current")
_NetMod1Probe2_1_Type = Integer32
_NetMod1Probe2_1_Object = MibScalar
netMod1Probe2_1 = _NetMod1Probe2_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 27),
    _NetMod1Probe2_1_Type()
)
netMod1Probe2_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod1Probe2_1.setStatus("current")
_NetMod1Combo3_1_Type = Integer32
_NetMod1Combo3_1_Object = MibScalar
netMod1Combo3_1 = _NetMod1Combo3_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 28),
    _NetMod1Combo3_1_Type()
)
netMod1Combo3_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod1Combo3_1.setStatus("current")
_NetMod1Probe3_1_Type = Integer32
_NetMod1Probe3_1_Object = MibScalar
netMod1Probe3_1 = _NetMod1Probe3_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 29),
    _NetMod1Probe3_1_Type()
)
netMod1Probe3_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod1Probe3_1.setStatus("current")
_NetMod1Combo4_1_Type = Integer32
_NetMod1Combo4_1_Object = MibScalar
netMod1Combo4_1 = _NetMod1Combo4_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 30),
    _NetMod1Combo4_1_Type()
)
netMod1Combo4_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod1Combo4_1.setStatus("current")
_NetMod1Probe4_1_Type = Integer32
_NetMod1Probe4_1_Object = MibScalar
netMod1Probe4_1 = _NetMod1Probe4_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 31),
    _NetMod1Probe4_1_Type()
)
netMod1Probe4_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod1Probe4_1.setStatus("current")
_NetMod1Combo5_1_Type = Integer32
_NetMod1Combo5_1_Object = MibScalar
netMod1Combo5_1 = _NetMod1Combo5_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 32),
    _NetMod1Combo5_1_Type()
)
netMod1Combo5_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod1Combo5_1.setStatus("current")
_NetMod1Probe5_1_Type = Integer32
_NetMod1Probe5_1_Object = MibScalar
netMod1Probe5_1 = _NetMod1Probe5_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 33),
    _NetMod1Probe5_1_Type()
)
netMod1Probe5_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod1Probe5_1.setStatus("current")
_NetMod1Combo6_1_Type = Integer32
_NetMod1Combo6_1_Object = MibScalar
netMod1Combo6_1 = _NetMod1Combo6_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 34),
    _NetMod1Combo6_1_Type()
)
netMod1Combo6_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod1Combo6_1.setStatus("current")
_NetMod1Probe6_1_Type = Integer32
_NetMod1Probe6_1_Object = MibScalar
netMod1Probe6_1 = _NetMod1Probe6_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 35),
    _NetMod1Probe6_1_Type()
)
netMod1Probe6_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod1Probe6_1.setStatus("current")
_NetMod2Combo1_1_Type = Integer32
_NetMod2Combo1_1_Object = MibScalar
netMod2Combo1_1 = _NetMod2Combo1_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 36),
    _NetMod2Combo1_1_Type()
)
netMod2Combo1_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod2Combo1_1.setStatus("current")
_NetMod2Probe1_1_Type = Integer32
_NetMod2Probe1_1_Object = MibScalar
netMod2Probe1_1 = _NetMod2Probe1_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 37),
    _NetMod2Probe1_1_Type()
)
netMod2Probe1_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod2Probe1_1.setStatus("current")
_NetMod2Combo2_1_Type = Integer32
_NetMod2Combo2_1_Object = MibScalar
netMod2Combo2_1 = _NetMod2Combo2_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 38),
    _NetMod2Combo2_1_Type()
)
netMod2Combo2_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod2Combo2_1.setStatus("current")
_NetMod2Probe2_1_Type = Integer32
_NetMod2Probe2_1_Object = MibScalar
netMod2Probe2_1 = _NetMod2Probe2_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 39),
    _NetMod2Probe2_1_Type()
)
netMod2Probe2_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod2Probe2_1.setStatus("current")
_NetMod2Combo3_1_Type = Integer32
_NetMod2Combo3_1_Object = MibScalar
netMod2Combo3_1 = _NetMod2Combo3_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 40),
    _NetMod2Combo3_1_Type()
)
netMod2Combo3_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod2Combo3_1.setStatus("current")
_NetMod2Probe3_1_Type = Integer32
_NetMod2Probe3_1_Object = MibScalar
netMod2Probe3_1 = _NetMod2Probe3_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 41),
    _NetMod2Probe3_1_Type()
)
netMod2Probe3_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod2Probe3_1.setStatus("current")
_NetMod2Combo4_1_Type = Integer32
_NetMod2Combo4_1_Object = MibScalar
netMod2Combo4_1 = _NetMod2Combo4_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 42),
    _NetMod2Combo4_1_Type()
)
netMod2Combo4_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod2Combo4_1.setStatus("current")
_NetMod2Probe4_1_Type = Integer32
_NetMod2Probe4_1_Object = MibScalar
netMod2Probe4_1 = _NetMod2Probe4_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 43),
    _NetMod2Probe4_1_Type()
)
netMod2Probe4_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod2Probe4_1.setStatus("current")
_NetMod2Combo5_1_Type = Integer32
_NetMod2Combo5_1_Object = MibScalar
netMod2Combo5_1 = _NetMod2Combo5_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 44),
    _NetMod2Combo5_1_Type()
)
netMod2Combo5_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod2Combo5_1.setStatus("current")
_NetMod2Probe5_1_Type = Integer32
_NetMod2Probe5_1_Object = MibScalar
netMod2Probe5_1 = _NetMod2Probe5_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 45),
    _NetMod2Probe5_1_Type()
)
netMod2Probe5_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod2Probe5_1.setStatus("current")
_NetMod2Combo6_1_Type = Integer32
_NetMod2Combo6_1_Object = MibScalar
netMod2Combo6_1 = _NetMod2Combo6_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 46),
    _NetMod2Combo6_1_Type()
)
netMod2Combo6_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod2Combo6_1.setStatus("current")
_NetMod2Probe6_1_Type = Integer32
_NetMod2Probe6_1_Object = MibScalar
netMod2Probe6_1 = _NetMod2Probe6_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 47),
    _NetMod2Probe6_1_Type()
)
netMod2Probe6_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod2Probe6_1.setStatus("current")
_NetMod3Combo1_1_Type = Integer32
_NetMod3Combo1_1_Object = MibScalar
netMod3Combo1_1 = _NetMod3Combo1_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 48),
    _NetMod3Combo1_1_Type()
)
netMod3Combo1_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod3Combo1_1.setStatus("current")
_NetMod3Probe1_1_Type = Integer32
_NetMod3Probe1_1_Object = MibScalar
netMod3Probe1_1 = _NetMod3Probe1_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 49),
    _NetMod3Probe1_1_Type()
)
netMod3Probe1_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod3Probe1_1.setStatus("current")
_NetMod3Combo2_1_Type = Integer32
_NetMod3Combo2_1_Object = MibScalar
netMod3Combo2_1 = _NetMod3Combo2_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 50),
    _NetMod3Combo2_1_Type()
)
netMod3Combo2_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod3Combo2_1.setStatus("current")
_NetMod3Probe2_1_Type = Integer32
_NetMod3Probe2_1_Object = MibScalar
netMod3Probe2_1 = _NetMod3Probe2_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 51),
    _NetMod3Probe2_1_Type()
)
netMod3Probe2_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod3Probe2_1.setStatus("current")
_NetMod3Combo3_1_Type = Integer32
_NetMod3Combo3_1_Object = MibScalar
netMod3Combo3_1 = _NetMod3Combo3_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 52),
    _NetMod3Combo3_1_Type()
)
netMod3Combo3_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod3Combo3_1.setStatus("current")
_NetMod3Probe3_1_Type = Integer32
_NetMod3Probe3_1_Object = MibScalar
netMod3Probe3_1 = _NetMod3Probe3_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 53),
    _NetMod3Probe3_1_Type()
)
netMod3Probe3_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod3Probe3_1.setStatus("current")
_NetMod3Combo4_1_Type = Integer32
_NetMod3Combo4_1_Object = MibScalar
netMod3Combo4_1 = _NetMod3Combo4_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 54),
    _NetMod3Combo4_1_Type()
)
netMod3Combo4_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod3Combo4_1.setStatus("current")
_NetMod3Probe4_1_Type = Integer32
_NetMod3Probe4_1_Object = MibScalar
netMod3Probe4_1 = _NetMod3Probe4_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 55),
    _NetMod3Probe4_1_Type()
)
netMod3Probe4_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod3Probe4_1.setStatus("current")
_NetMod3Combo5_1_Type = Integer32
_NetMod3Combo5_1_Object = MibScalar
netMod3Combo5_1 = _NetMod3Combo5_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 56),
    _NetMod3Combo5_1_Type()
)
netMod3Combo5_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod3Combo5_1.setStatus("current")
_NetMod3Probe5_1_Type = Integer32
_NetMod3Probe5_1_Object = MibScalar
netMod3Probe5_1 = _NetMod3Probe5_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 57),
    _NetMod3Probe5_1_Type()
)
netMod3Probe5_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod3Probe5_1.setStatus("current")
_NetMod3Combo6_1_Type = Integer32
_NetMod3Combo6_1_Object = MibScalar
netMod3Combo6_1 = _NetMod3Combo6_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 58),
    _NetMod3Combo6_1_Type()
)
netMod3Combo6_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod3Combo6_1.setStatus("current")
_NetMod3Probe6_1_Type = Integer32
_NetMod3Probe6_1_Object = MibScalar
netMod3Probe6_1 = _NetMod3Probe6_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 59),
    _NetMod3Probe6_1_Type()
)
netMod3Probe6_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod3Probe6_1.setStatus("current")
_AvgModTemp_1_Type = Integer32
_AvgModTemp_1_Object = MibScalar
avgModTemp_1 = _AvgModTemp_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 60),
    _AvgModTemp_1_Type()
)
avgModTemp_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avgModTemp_1.setStatus("current")
_AvgModHumi_1_Type = Integer32
_AvgModHumi_1_Object = MibScalar
avgModHumi_1 = _AvgModHumi_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 61),
    _AvgModHumi_1_Type()
)
avgModHumi_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avgModHumi_1.setStatus("current")
_AvgModPress_1_Type = Integer32
_AvgModPress_1_Object = MibScalar
avgModPress_1 = _AvgModPress_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 62),
    _AvgModPress_1_Type()
)
avgModPress_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avgModPress_1.setStatus("current")
_DryCoolerAO_1_Type = Integer32
_DryCoolerAO_1_Object = MibScalar
dryCoolerAO_1 = _DryCoolerAO_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 63),
    _DryCoolerAO_1_Type()
)
dryCoolerAO_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dryCoolerAO_1.setStatus("current")
_CoolingAO_1_Type = Integer32
_CoolingAO_1_Object = MibScalar
coolingAO_1 = _CoolingAO_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 64),
    _CoolingAO_1_Type()
)
coolingAO_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingAO_1.setStatus("current")
_HeatingAO_1_Type = Integer32
_HeatingAO_1_Object = MibScalar
heatingAO_1 = _HeatingAO_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 65),
    _HeatingAO_1_Type()
)
heatingAO_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heatingAO_1.setStatus("current")
_TwoSources2AO_1_Type = Integer32
_TwoSources2AO_1_Object = MibScalar
twoSources2AO_1 = _TwoSources2AO_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 66),
    _TwoSources2AO_1_Type()
)
twoSources2AO_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twoSources2AO_1.setStatus("current")
_Condenser1AO_1_Type = Integer32
_Condenser1AO_1_Object = MibScalar
condenser1AO_1 = _Condenser1AO_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 67),
    _Condenser1AO_1_Type()
)
condenser1AO_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    condenser1AO_1.setStatus("current")
_Cond2HumidifAO_1_Type = Integer32
_Cond2HumidifAO_1_Object = MibScalar
cond2HumidifAO_1 = _Cond2HumidifAO_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 68),
    _Cond2HumidifAO_1_Type()
)
cond2HumidifAO_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cond2HumidifAO_1.setStatus("current")
_UnitStatus_1_Type = Integer32
_UnitStatus_1_Object = MibScalar
unitStatus_1 = _UnitStatus_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 69),
    _UnitStatus_1_Type()
)
unitStatus_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitStatus_1.setStatus("current")
_FanSpeed_1_Type = Integer32
_FanSpeed_1_Object = MibScalar
fanSpeed_1 = _FanSpeed_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 70),
    _FanSpeed_1_Type()
)
fanSpeed_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanSpeed_1.setStatus("current")
_Fan1Actspeed_1_Type = Integer32
_Fan1Actspeed_1_Object = MibScalar
fan1Actspeed_1 = _Fan1Actspeed_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 71),
    _Fan1Actspeed_1_Type()
)
fan1Actspeed_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan1Actspeed_1.setStatus("current")
_Fan1ActRPM_1_Type = Integer32
_Fan1ActRPM_1_Object = MibScalar
fan1ActRPM_1 = _Fan1ActRPM_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 72),
    _Fan1ActRPM_1_Type()
)
fan1ActRPM_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan1ActRPM_1.setStatus("current")
_Fan1Cur_1_Type = Integer32
_Fan1Cur_1_Object = MibScalar
fan1Cur_1 = _Fan1Cur_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 73),
    _Fan1Cur_1_Type()
)
fan1Cur_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan1Cur_1.setStatus("current")
_Fan1Power_1_Type = Integer32
_Fan1Power_1_Object = MibScalar
fan1Power_1 = _Fan1Power_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 74),
    _Fan1Power_1_Type()
)
fan1Power_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan1Power_1.setStatus("current")
_Fan2Actspeed_1_Type = Integer32
_Fan2Actspeed_1_Object = MibScalar
fan2Actspeed_1 = _Fan2Actspeed_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 75),
    _Fan2Actspeed_1_Type()
)
fan2Actspeed_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan2Actspeed_1.setStatus("current")
_Fan2ActRPM_1_Type = Integer32
_Fan2ActRPM_1_Object = MibScalar
fan2ActRPM_1 = _Fan2ActRPM_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 76),
    _Fan2ActRPM_1_Type()
)
fan2ActRPM_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan2ActRPM_1.setStatus("current")
_Fan2Cur_1_Type = Integer32
_Fan2Cur_1_Object = MibScalar
fan2Cur_1 = _Fan2Cur_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 77),
    _Fan2Cur_1_Type()
)
fan2Cur_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan2Cur_1.setStatus("current")
_Fan2Power_1_Type = Integer32
_Fan2Power_1_Object = MibScalar
fan2Power_1 = _Fan2Power_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 78),
    _Fan2Power_1_Type()
)
fan2Power_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan2Power_1.setStatus("current")
_Fan3Actspeed_1_Type = Integer32
_Fan3Actspeed_1_Object = MibScalar
fan3Actspeed_1 = _Fan3Actspeed_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 79),
    _Fan3Actspeed_1_Type()
)
fan3Actspeed_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan3Actspeed_1.setStatus("current")
_Fan3ActRPM_1_Type = Integer32
_Fan3ActRPM_1_Object = MibScalar
fan3ActRPM_1 = _Fan3ActRPM_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 80),
    _Fan3ActRPM_1_Type()
)
fan3ActRPM_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan3ActRPM_1.setStatus("current")
_Fan3Cur_1_Type = Integer32
_Fan3Cur_1_Object = MibScalar
fan3Cur_1 = _Fan3Cur_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 81),
    _Fan3Cur_1_Type()
)
fan3Cur_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan3Cur_1.setStatus("current")
_Fan3Power_1_Type = Integer32
_Fan3Power_1_Object = MibScalar
fan3Power_1 = _Fan3Power_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 82),
    _Fan3Power_1_Type()
)
fan3Power_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan3Power_1.setStatus("current")
_Fan4Actspeed_1_Type = Integer32
_Fan4Actspeed_1_Object = MibScalar
fan4Actspeed_1 = _Fan4Actspeed_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 83),
    _Fan4Actspeed_1_Type()
)
fan4Actspeed_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan4Actspeed_1.setStatus("current")
_Fan4ActRPM_1_Type = Integer32
_Fan4ActRPM_1_Object = MibScalar
fan4ActRPM_1 = _Fan4ActRPM_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 84),
    _Fan4ActRPM_1_Type()
)
fan4ActRPM_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan4ActRPM_1.setStatus("current")
_Fan4Cur_1_Type = Integer32
_Fan4Cur_1_Object = MibScalar
fan4Cur_1 = _Fan4Cur_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 85),
    _Fan4Cur_1_Type()
)
fan4Cur_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan4Cur_1.setStatus("current")
_Fan4Power_1_Type = Integer32
_Fan4Power_1_Object = MibScalar
fan4Power_1 = _Fan4Power_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 86),
    _Fan4Power_1_Type()
)
fan4Power_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan4Power_1.setStatus("current")
_Fan5Actspeed_1_Type = Integer32
_Fan5Actspeed_1_Object = MibScalar
fan5Actspeed_1 = _Fan5Actspeed_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 87),
    _Fan5Actspeed_1_Type()
)
fan5Actspeed_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan5Actspeed_1.setStatus("current")
_Fan5ActRPM_1_Type = Integer32
_Fan5ActRPM_1_Object = MibScalar
fan5ActRPM_1 = _Fan5ActRPM_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 88),
    _Fan5ActRPM_1_Type()
)
fan5ActRPM_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan5ActRPM_1.setStatus("current")
_Fan5Cur_1_Type = Integer32
_Fan5Cur_1_Object = MibScalar
fan5Cur_1 = _Fan5Cur_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 89),
    _Fan5Cur_1_Type()
)
fan5Cur_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan5Cur_1.setStatus("current")
_Fan5Power_1_Type = Integer32
_Fan5Power_1_Object = MibScalar
fan5Power_1 = _Fan5Power_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 90),
    _Fan5Power_1_Type()
)
fan5Power_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan5Power_1.setStatus("current")
_Fan6Actspeed_1_Type = Integer32
_Fan6Actspeed_1_Object = MibScalar
fan6Actspeed_1 = _Fan6Actspeed_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 91),
    _Fan6Actspeed_1_Type()
)
fan6Actspeed_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan6Actspeed_1.setStatus("current")
_Fan6ActRPM_1_Type = Integer32
_Fan6ActRPM_1_Object = MibScalar
fan6ActRPM_1 = _Fan6ActRPM_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 92),
    _Fan6ActRPM_1_Type()
)
fan6ActRPM_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan6ActRPM_1.setStatus("current")
_Fan6Cur_1_Type = Integer32
_Fan6Cur_1_Object = MibScalar
fan6Cur_1 = _Fan6Cur_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 93),
    _Fan6Cur_1_Type()
)
fan6Cur_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan6Cur_1.setStatus("current")
_Fan6Power_1_Type = Integer32
_Fan6Power_1_Object = MibScalar
fan6Power_1 = _Fan6Power_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 94),
    _Fan6Power_1_Type()
)
fan6Power_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan6Power_1.setStatus("current")
_Fan7Actspeed_1_Type = Integer32
_Fan7Actspeed_1_Object = MibScalar
fan7Actspeed_1 = _Fan7Actspeed_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 95),
    _Fan7Actspeed_1_Type()
)
fan7Actspeed_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan7Actspeed_1.setStatus("current")
_Fan7ActRPM_1_Type = Integer32
_Fan7ActRPM_1_Object = MibScalar
fan7ActRPM_1 = _Fan7ActRPM_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 96),
    _Fan7ActRPM_1_Type()
)
fan7ActRPM_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan7ActRPM_1.setStatus("current")
_Fan7Cur_1_Type = Integer32
_Fan7Cur_1_Object = MibScalar
fan7Cur_1 = _Fan7Cur_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 97),
    _Fan7Cur_1_Type()
)
fan7Cur_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan7Cur_1.setStatus("current")
_Fan7Power_1_Type = Integer32
_Fan7Power_1_Object = MibScalar
fan7Power_1 = _Fan7Power_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 98),
    _Fan7Power_1_Type()
)
fan7Power_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan7Power_1.setStatus("current")
_Fan8Actspeed_1_Type = Integer32
_Fan8Actspeed_1_Object = MibScalar
fan8Actspeed_1 = _Fan8Actspeed_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 99),
    _Fan8Actspeed_1_Type()
)
fan8Actspeed_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan8Actspeed_1.setStatus("current")
_Fan8ActRPM_1_Type = Integer32
_Fan8ActRPM_1_Object = MibScalar
fan8ActRPM_1 = _Fan8ActRPM_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 100),
    _Fan8ActRPM_1_Type()
)
fan8ActRPM_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan8ActRPM_1.setStatus("current")
_Fan8Cur_1_Type = Integer32
_Fan8Cur_1_Object = MibScalar
fan8Cur_1 = _Fan8Cur_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 101),
    _Fan8Cur_1_Type()
)
fan8Cur_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan8Cur_1.setStatus("current")
_Fan8Power_1_Type = Integer32
_Fan8Power_1_Object = MibScalar
fan8Power_1 = _Fan8Power_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 102),
    _Fan8Power_1_Type()
)
fan8Power_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan8Power_1.setStatus("current")
_Fan9Actspeed_1_Type = Integer32
_Fan9Actspeed_1_Object = MibScalar
fan9Actspeed_1 = _Fan9Actspeed_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 103),
    _Fan9Actspeed_1_Type()
)
fan9Actspeed_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan9Actspeed_1.setStatus("current")
_Fan9ActRPM_1_Type = Integer32
_Fan9ActRPM_1_Object = MibScalar
fan9ActRPM_1 = _Fan9ActRPM_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 104),
    _Fan9ActRPM_1_Type()
)
fan9ActRPM_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan9ActRPM_1.setStatus("current")
_Fan9Cur_1_Type = Integer32
_Fan9Cur_1_Object = MibScalar
fan9Cur_1 = _Fan9Cur_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 105),
    _Fan9Cur_1_Type()
)
fan9Cur_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan9Cur_1.setStatus("current")
_Fan9Power_1_Type = Integer32
_Fan9Power_1_Object = MibScalar
fan9Power_1 = _Fan9Power_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 106),
    _Fan9Power_1_Type()
)
fan9Power_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan9Power_1.setStatus("current")
_Fan10Actspeed_1_Type = Integer32
_Fan10Actspeed_1_Object = MibScalar
fan10Actspeed_1 = _Fan10Actspeed_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 107),
    _Fan10Actspeed_1_Type()
)
fan10Actspeed_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan10Actspeed_1.setStatus("current")
_Fan10ActRPM_1_Type = Integer32
_Fan10ActRPM_1_Object = MibScalar
fan10ActRPM_1 = _Fan10ActRPM_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 108),
    _Fan10ActRPM_1_Type()
)
fan10ActRPM_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan10ActRPM_1.setStatus("current")
_Fan10Cur_1_Type = Integer32
_Fan10Cur_1_Object = MibScalar
fan10Cur_1 = _Fan10Cur_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 109),
    _Fan10Cur_1_Type()
)
fan10Cur_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan10Cur_1.setStatus("current")
_Fan10Power_1_Type = Integer32
_Fan10Power_1_Object = MibScalar
fan10Power_1 = _Fan10Power_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 110),
    _Fan10Power_1_Type()
)
fan10Power_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan10Power_1.setStatus("current")
_DiffFilterPres_1_Type = Integer32
_DiffFilterPres_1_Object = MibScalar
diffFilterPres_1 = _DiffFilterPres_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 111),
    _DiffFilterPres_1_Type()
)
diffFilterPres_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffFilterPres_1.setStatus("current")
_CoolingRequest_1_Type = Integer32
_CoolingRequest_1_Object = MibScalar
coolingRequest_1 = _CoolingRequest_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 112),
    _CoolingRequest_1_Type()
)
coolingRequest_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingRequest_1.setStatus("current")
_HeatingRequest_1_Type = Integer32
_HeatingRequest_1_Object = MibScalar
heatingRequest_1 = _HeatingRequest_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 113),
    _HeatingRequest_1_Type()
)
heatingRequest_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heatingRequest_1.setStatus("current")
_DehumidRequest_1_Type = Integer32
_DehumidRequest_1_Object = MibScalar
dehumidRequest_1 = _DehumidRequest_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 114),
    _DehumidRequest_1_Type()
)
dehumidRequest_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dehumidRequest_1.setStatus("current")
_HumidifRequest_1_Type = Integer32
_HumidifRequest_1_Object = MibScalar
humidifRequest_1 = _HumidifRequest_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 115),
    _HumidifRequest_1_Type()
)
humidifRequest_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidifRequest_1.setStatus("current")
_TempFcTs_1_Type = Integer32
_TempFcTs_1_Object = MibScalar
tempFcTs_1 = _TempFcTs_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 116),
    _TempFcTs_1_Type()
)
tempFcTs_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempFcTs_1.setStatus("current")
_FCTSStatus_1_Type = Integer32
_FCTSStatus_1_Object = MibScalar
fCTSStatus_1 = _FCTSStatus_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 117),
    _FCTSStatus_1_Type()
)
fCTSStatus_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fCTSStatus_1.setStatus("current")
_FCRequest_1_Type = Integer32
_FCRequest_1_Object = MibScalar
fCRequest_1 = _FCRequest_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 118),
    _FCRequest_1_Type()
)
fCRequest_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fCRequest_1.setStatus("current")
_ActiveComp_1_Type = Integer32
_ActiveComp_1_Object = MibScalar
activeComp_1 = _ActiveComp_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 119),
    _ActiveComp_1_Type()
)
activeComp_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeComp_1.setStatus("current")
_Comp1Sts_1_Type = Integer32
_Comp1Sts_1_Object = MibScalar
comp1Sts_1 = _Comp1Sts_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 120),
    _Comp1Sts_1_Type()
)
comp1Sts_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comp1Sts_1.setStatus("current")
_Comp2Sts_1_Type = Integer32
_Comp2Sts_1_Object = MibScalar
comp2Sts_1 = _Comp2Sts_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 121),
    _Comp2Sts_1_Type()
)
comp2Sts_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comp2Sts_1.setStatus("current")
_InvComprReq_1_Type = Integer32
_InvComprReq_1_Object = MibScalar
invComprReq_1 = _InvComprReq_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 122),
    _InvComprReq_1_Type()
)
invComprReq_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invComprReq_1.setStatus("current")
_InvCompHz_1_Type = Integer32
_InvCompHz_1_Object = MibScalar
invCompHz_1 = _InvCompHz_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 123),
    _InvCompHz_1_Type()
)
invCompHz_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invCompHz_1.setStatus("current")
_InvCompPower_1_Type = Integer32
_InvCompPower_1_Object = MibScalar
invCompPower_1 = _InvCompPower_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 124),
    _InvCompPower_1_Type()
)
invCompPower_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invCompPower_1.setStatus("current")
_InvCompCurrent_1_Type = Integer32
_InvCompCurrent_1_Object = MibScalar
invCompCurrent_1 = _InvCompCurrent_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 125),
    _InvCompCurrent_1_Type()
)
invCompCurrent_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invCompCurrent_1.setStatus("current")
_C1EvapPres_1_Type = Integer32
_C1EvapPres_1_Object = MibScalar
c1EvapPres_1 = _C1EvapPres_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 126),
    _C1EvapPres_1_Type()
)
c1EvapPres_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c1EvapPres_1.setStatus("current")
_C1EvapTemp_1_Type = Integer32
_C1EvapTemp_1_Object = MibScalar
c1EvapTemp_1 = _C1EvapTemp_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 127),
    _C1EvapTemp_1_Type()
)
c1EvapTemp_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c1EvapTemp_1.setStatus("current")
_C1SuctionTemp_1_Type = Integer32
_C1SuctionTemp_1_Object = MibScalar
c1SuctionTemp_1 = _C1SuctionTemp_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 128),
    _C1SuctionTemp_1_Type()
)
c1SuctionTemp_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c1SuctionTemp_1.setStatus("current")
_C1Superheat_1_Type = Integer32
_C1Superheat_1_Object = MibScalar
c1Superheat_1 = _C1Superheat_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 129),
    _C1Superheat_1_Type()
)
c1Superheat_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c1Superheat_1.setStatus("current")
_C1CompRatio_1_Type = Integer32
_C1CompRatio_1_Object = MibScalar
c1CompRatio_1 = _C1CompRatio_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 130),
    _C1CompRatio_1_Type()
)
c1CompRatio_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c1CompRatio_1.setStatus("current")
_C1DischTemp_1_Type = Integer32
_C1DischTemp_1_Object = MibScalar
c1DischTemp_1 = _C1DischTemp_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 131),
    _C1DischTemp_1_Type()
)
c1DischTemp_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c1DischTemp_1.setStatus("current")
_C1CondPress_1_Type = Integer32
_C1CondPress_1_Object = MibScalar
c1CondPress_1 = _C1CondPress_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 132),
    _C1CondPress_1_Type()
)
c1CondPress_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c1CondPress_1.setStatus("current")
_C1CondTemp_1_Type = Integer32
_C1CondTemp_1_Object = MibScalar
c1CondTemp_1 = _C1CondTemp_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 133),
    _C1CondTemp_1_Type()
)
c1CondTemp_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c1CondTemp_1.setStatus("current")
_C1Desuperheat_1_Type = Integer32
_C1Desuperheat_1_Object = MibScalar
c1Desuperheat_1 = _C1Desuperheat_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 134),
    _C1Desuperheat_1_Type()
)
c1Desuperheat_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c1Desuperheat_1.setStatus("current")
_C1LiquidTemp_1_Type = Integer32
_C1LiquidTemp_1_Object = MibScalar
c1LiquidTemp_1 = _C1LiquidTemp_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 135),
    _C1LiquidTemp_1_Type()
)
c1LiquidTemp_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c1LiquidTemp_1.setStatus("current")
_C1Subcooling_1_Type = Integer32
_C1Subcooling_1_Object = MibScalar
c1Subcooling_1 = _C1Subcooling_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 136),
    _C1Subcooling_1_Type()
)
c1Subcooling_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c1Subcooling_1.setStatus("current")
_EEV1SHSet_1_Type = Integer32
_EEV1SHSet_1_Object = MibScalar
eEV1SHSet_1 = _EEV1SHSet_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 137),
    _EEV1SHSet_1_Type()
)
eEV1SHSet_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eEV1SHSet_1.setStatus("current")
_EEV1Position_1_Type = Integer32
_EEV1Position_1_Object = MibScalar
eEV1Position_1 = _EEV1Position_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 138),
    _EEV1Position_1_Type()
)
eEV1Position_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eEV1Position_1.setStatus("current")
_EEV1Status_1_Type = Integer32
_EEV1Status_1_Object = MibScalar
eEV1Status_1 = _EEV1Status_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 139),
    _EEV1Status_1_Type()
)
eEV1Status_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eEV1Status_1.setStatus("current")
_Cond1ActualSet_1_Type = Integer32
_Cond1ActualSet_1_Object = MibScalar
cond1ActualSet_1 = _Cond1ActualSet_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 140),
    _Cond1ActualSet_1_Type()
)
cond1ActualSet_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cond1ActualSet_1.setStatus("current")
_Cond1Req_1_Type = Integer32
_Cond1Req_1_Object = MibScalar
cond1Req_1 = _Cond1Req_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 141),
    _Cond1Req_1_Type()
)
cond1Req_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cond1Req_1.setStatus("current")
_C2EvapPres_1_Type = Integer32
_C2EvapPres_1_Object = MibScalar
c2EvapPres_1 = _C2EvapPres_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 142),
    _C2EvapPres_1_Type()
)
c2EvapPres_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2EvapPres_1.setStatus("current")
_C2EvapTemp_1_Type = Integer32
_C2EvapTemp_1_Object = MibScalar
c2EvapTemp_1 = _C2EvapTemp_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 143),
    _C2EvapTemp_1_Type()
)
c2EvapTemp_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2EvapTemp_1.setStatus("current")
_C2SuctionTemp_1_Type = Integer32
_C2SuctionTemp_1_Object = MibScalar
c2SuctionTemp_1 = _C2SuctionTemp_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 144),
    _C2SuctionTemp_1_Type()
)
c2SuctionTemp_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2SuctionTemp_1.setStatus("current")
_C2Superheat_1_Type = Integer32
_C2Superheat_1_Object = MibScalar
c2Superheat_1 = _C2Superheat_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 145),
    _C2Superheat_1_Type()
)
c2Superheat_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2Superheat_1.setStatus("current")
_C2CompRatio_1_Type = Integer32
_C2CompRatio_1_Object = MibScalar
c2CompRatio_1 = _C2CompRatio_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 146),
    _C2CompRatio_1_Type()
)
c2CompRatio_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2CompRatio_1.setStatus("current")
_C2DischTemp_1_Type = Integer32
_C2DischTemp_1_Object = MibScalar
c2DischTemp_1 = _C2DischTemp_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 147),
    _C2DischTemp_1_Type()
)
c2DischTemp_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2DischTemp_1.setStatus("current")
_C2CondPress_1_Type = Integer32
_C2CondPress_1_Object = MibScalar
c2CondPress_1 = _C2CondPress_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 148),
    _C2CondPress_1_Type()
)
c2CondPress_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2CondPress_1.setStatus("current")
_C2CondTemp_1_Type = Integer32
_C2CondTemp_1_Object = MibScalar
c2CondTemp_1 = _C2CondTemp_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 149),
    _C2CondTemp_1_Type()
)
c2CondTemp_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2CondTemp_1.setStatus("current")
_C2Desuperheat_1_Type = Integer32
_C2Desuperheat_1_Object = MibScalar
c2Desuperheat_1 = _C2Desuperheat_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 150),
    _C2Desuperheat_1_Type()
)
c2Desuperheat_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2Desuperheat_1.setStatus("current")
_C2LiquidTemp_1_Type = Integer32
_C2LiquidTemp_1_Object = MibScalar
c2LiquidTemp_1 = _C2LiquidTemp_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 151),
    _C2LiquidTemp_1_Type()
)
c2LiquidTemp_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2LiquidTemp_1.setStatus("current")
_C2Subcooling_1_Type = Integer32
_C2Subcooling_1_Object = MibScalar
c2Subcooling_1 = _C2Subcooling_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 152),
    _C2Subcooling_1_Type()
)
c2Subcooling_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2Subcooling_1.setStatus("current")
_EEV2SHSet_1_Type = Integer32
_EEV2SHSet_1_Object = MibScalar
eEV2SHSet_1 = _EEV2SHSet_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 153),
    _EEV2SHSet_1_Type()
)
eEV2SHSet_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eEV2SHSet_1.setStatus("current")
_EEV2Position_1_Type = Integer32
_EEV2Position_1_Object = MibScalar
eEV2Position_1 = _EEV2Position_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 154),
    _EEV2Position_1_Type()
)
eEV2Position_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eEV2Position_1.setStatus("current")
_EEV2Status_1_Type = Integer32
_EEV2Status_1_Object = MibScalar
eEV2Status_1 = _EEV2Status_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 155),
    _EEV2Status_1_Type()
)
eEV2Status_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eEV2Status_1.setStatus("current")
_Cond2ActualSet_1_Type = Integer32
_Cond2ActualSet_1_Object = MibScalar
cond2ActualSet_1 = _Cond2ActualSet_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 156),
    _Cond2ActualSet_1_Type()
)
cond2ActualSet_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cond2ActualSet_1.setStatus("current")
_Cond2Req_1_Type = Integer32
_Cond2Req_1_Object = MibScalar
cond2Req_1 = _Cond2Req_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 157),
    _Cond2Req_1_Type()
)
cond2Req_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cond2Req_1.setStatus("current")
_WaterINTemp1_1_Type = Integer32
_WaterINTemp1_1_Object = MibScalar
waterINTemp1_1 = _WaterINTemp1_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 158),
    _WaterINTemp1_1_Type()
)
waterINTemp1_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    waterINTemp1_1.setStatus("current")
_WaterOUTTemp1_1_Type = Integer32
_WaterOUTTemp1_1_Object = MibScalar
waterOUTTemp1_1 = _WaterOUTTemp1_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 159),
    _WaterOUTTemp1_1_Type()
)
waterOUTTemp1_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    waterOUTTemp1_1.setStatus("current")
_WaterDT1_1_Type = Integer32
_WaterDT1_1_Object = MibScalar
waterDT1_1 = _WaterDT1_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 160),
    _WaterDT1_1_Type()
)
waterDT1_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    waterDT1_1.setStatus("current")
_WaterFlow1_1_Type = Integer32
_WaterFlow1_1_Object = MibScalar
waterFlow1_1 = _WaterFlow1_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 161),
    _WaterFlow1_1_Type()
)
waterFlow1_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    waterFlow1_1.setStatus("current")
_ActWatFlowSet1_1_Type = Integer32
_ActWatFlowSet1_1_Object = MibScalar
actWatFlowSet1_1 = _ActWatFlowSet1_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 162),
    _ActWatFlowSet1_1_Type()
)
actWatFlowSet1_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actWatFlowSet1_1.setStatus("current")
_WaterCoolCap1_1_Type = Integer32
_WaterCoolCap1_1_Object = MibScalar
waterCoolCap1_1 = _WaterCoolCap1_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 163),
    _WaterCoolCap1_1_Type()
)
waterCoolCap1_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    waterCoolCap1_1.setStatus("current")
_EER1_1_Type = Integer32
_EER1_1_Object = MibScalar
eER1_1 = _EER1_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 164),
    _EER1_1_Type()
)
eER1_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eER1_1.setStatus("current")
_Valve1Position_1_Type = Integer32
_Valve1Position_1_Object = MibScalar
valve1Position_1 = _Valve1Position_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 165),
    _Valve1Position_1_Type()
)
valve1Position_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    valve1Position_1.setStatus("current")
_WaterINTemp2_1_Type = Integer32
_WaterINTemp2_1_Object = MibScalar
waterINTemp2_1 = _WaterINTemp2_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 166),
    _WaterINTemp2_1_Type()
)
waterINTemp2_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    waterINTemp2_1.setStatus("current")
_WaterOUTTemp2_1_Type = Integer32
_WaterOUTTemp2_1_Object = MibScalar
waterOUTTemp2_1 = _WaterOUTTemp2_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 167),
    _WaterOUTTemp2_1_Type()
)
waterOUTTemp2_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    waterOUTTemp2_1.setStatus("current")
_WaterDT2_1_Type = Integer32
_WaterDT2_1_Object = MibScalar
waterDT2_1 = _WaterDT2_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 168),
    _WaterDT2_1_Type()
)
waterDT2_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    waterDT2_1.setStatus("current")
_WaterFlow2_1_Type = Integer32
_WaterFlow2_1_Object = MibScalar
waterFlow2_1 = _WaterFlow2_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 169),
    _WaterFlow2_1_Type()
)
waterFlow2_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    waterFlow2_1.setStatus("current")
_ActWatFlowSet2_1_Type = Integer32
_ActWatFlowSet2_1_Object = MibScalar
actWatFlowSet2_1 = _ActWatFlowSet2_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 170),
    _ActWatFlowSet2_1_Type()
)
actWatFlowSet2_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actWatFlowSet2_1.setStatus("current")
_WaterCoolCap2_1_Type = Integer32
_WaterCoolCap2_1_Object = MibScalar
waterCoolCap2_1 = _WaterCoolCap2_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 171),
    _WaterCoolCap2_1_Type()
)
waterCoolCap2_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    waterCoolCap2_1.setStatus("current")
_EER2_1_Type = Integer32
_EER2_1_Object = MibScalar
eER2_1 = _EER2_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 172),
    _EER2_1_Type()
)
eER2_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eER2_1.setStatus("current")
_Valve2Position_1_Type = Integer32
_Valve2Position_1_Object = MibScalar
valve2Position_1 = _Valve2Position_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 173),
    _Valve2Position_1_Type()
)
valve2Position_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    valve2Position_1.setStatus("current")
_HumSteamProd_1_Type = Integer32
_HumSteamProd_1_Object = MibScalar
humSteamProd_1 = _HumSteamProd_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 174),
    _HumSteamProd_1_Type()
)
humSteamProd_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humSteamProd_1.setStatus("current")
_HumWaterConduct_1_Type = Integer32
_HumWaterConduct_1_Object = MibScalar
humWaterConduct_1 = _HumWaterConduct_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 175),
    _HumWaterConduct_1_Type()
)
humWaterConduct_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humWaterConduct_1.setStatus("current")
_HumCurrent_1_Type = Integer32
_HumCurrent_1_Object = MibScalar
humCurrent_1 = _HumCurrent_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 176),
    _HumCurrent_1_Type()
)
humCurrent_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humCurrent_1.setStatus("current")
_HumWorkingMode_1_Type = Integer32
_HumWorkingMode_1_Object = MibScalar
humWorkingMode_1 = _HumWorkingMode_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 177),
    _HumWorkingMode_1_Type()
)
humWorkingMode_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humWorkingMode_1.setStatus("current")
_HumWorkStatus_1_Type = Integer32
_HumWorkStatus_1_Object = MibScalar
humWorkStatus_1 = _HumWorkStatus_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 178),
    _HumWorkStatus_1_Type()
)
humWorkStatus_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humWorkStatus_1.setStatus("current")
_HeaterReq_1_Type = Integer32
_HeaterReq_1_Object = MibScalar
heaterReq_1 = _HeaterReq_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 179),
    _HeaterReq_1_Type()
)
heaterReq_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heaterReq_1.setStatus("current")
_HeaterActiveStg_1_Type = Integer32
_HeaterActiveStg_1_Object = MibScalar
heaterActiveStg_1 = _HeaterActiveStg_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 180),
    _HeaterActiveStg_1_Type()
)
heaterActiveStg_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heaterActiveStg_1.setStatus("current")
_ElHeaterPower_1_Type = Integer32
_ElHeaterPower_1_Object = MibScalar
elHeaterPower_1 = _ElHeaterPower_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 181),
    _ElHeaterPower_1_Type()
)
elHeaterPower_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elHeaterPower_1.setStatus("current")
_HeatValveReq_1_Type = Integer32
_HeatValveReq_1_Object = MibScalar
heatValveReq_1 = _HeatValveReq_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 182),
    _HeatValveReq_1_Type()
)
heatValveReq_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heatValveReq_1.setStatus("current")
_DryCoolerActSet_1_Type = Integer32
_DryCoolerActSet_1_Object = MibScalar
dryCoolerActSet_1 = _DryCoolerActSet_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 183),
    _DryCoolerActSet_1_Type()
)
dryCoolerActSet_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dryCoolerActSet_1.setStatus("current")
_DryCoolerReq_1_Type = Integer32
_DryCoolerReq_1_Object = MibScalar
dryCoolerReq_1 = _DryCoolerReq_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 184),
    _DryCoolerReq_1_Type()
)
dryCoolerReq_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dryCoolerReq_1.setStatus("current")
_UnitWH_1_Type = Integer32
_UnitWH_1_Object = MibScalar
unitWH_1 = _UnitWH_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 185),
    _UnitWH_1_Type()
)
unitWH_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitWH_1.setStatus("current")
_C1WH_1_Type = Integer32
_C1WH_1_Object = MibScalar
c1WH_1 = _C1WH_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 186),
    _C1WH_1_Type()
)
c1WH_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c1WH_1.setStatus("current")
_C1Startup_1_Type = Integer32
_C1Startup_1_Object = MibScalar
c1Startup_1 = _C1Startup_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 187),
    _C1Startup_1_Type()
)
c1Startup_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c1Startup_1.setStatus("current")
_C2WH_1_Type = Integer32
_C2WH_1_Object = MibScalar
c2WH_1 = _C2WH_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 188),
    _C2WH_1_Type()
)
c2WH_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2WH_1.setStatus("current")
_C2Startup_1_Type = Integer32
_C2Startup_1_Object = MibScalar
c2Startup_1 = _C2Startup_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 189),
    _C2Startup_1_Type()
)
c2Startup_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2Startup_1.setStatus("current")
_CoolValveWH_1_Type = Integer32
_CoolValveWH_1_Object = MibScalar
coolValveWH_1 = _CoolValveWH_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 190),
    _CoolValveWH_1_Type()
)
coolValveWH_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolValveWH_1.setStatus("current")
_HeatingWH_1_Type = Integer32
_HeatingWH_1_Object = MibScalar
heatingWH_1 = _HeatingWH_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 191),
    _HeatingWH_1_Type()
)
heatingWH_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heatingWH_1.setStatus("current")
_HumidifWH_1_Type = Integer32
_HumidifWH_1_Object = MibScalar
humidifWH_1 = _HumidifWH_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 192),
    _HumidifWH_1_Type()
)
humidifWH_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidifWH_1.setStatus("current")
_FreeCoolWH_1_Type = Integer32
_FreeCoolWH_1_Object = MibScalar
freeCoolWH_1 = _FreeCoolWH_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 193),
    _FreeCoolWH_1_Type()
)
freeCoolWH_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    freeCoolWH_1.setStatus("current")
_DryCoolerWH_1_Type = Integer32
_DryCoolerWH_1_Object = MibScalar
dryCoolerWH_1 = _DryCoolerWH_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 194),
    _DryCoolerWH_1_Type()
)
dryCoolerWH_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dryCoolerWH_1.setStatus("current")
_Cond1WH_1_Type = Integer32
_Cond1WH_1_Object = MibScalar
cond1WH_1 = _Cond1WH_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 195),
    _Cond1WH_1_Type()
)
cond1WH_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cond1WH_1.setStatus("current")
_Cond2WH_1_Type = Integer32
_Cond2WH_1_Object = MibScalar
cond2WH_1 = _Cond2WH_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 196),
    _Cond2WH_1_Type()
)
cond2WH_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cond2WH_1.setStatus("current")
_TempSetpoint_1_Type = Integer32
_TempSetpoint_1_Object = MibScalar
tempSetpoint_1 = _TempSetpoint_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 197),
    _TempSetpoint_1_Type()
)
tempSetpoint_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempSetpoint_1.setStatus("current")
_HumSetpoint_1_Type = Integer32
_HumSetpoint_1_Object = MibScalar
humSetpoint_1 = _HumSetpoint_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 198),
    _HumSetpoint_1_Type()
)
humSetpoint_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humSetpoint_1.setStatus("current")
_AirFlowSetpoint_1_Type = Integer32
_AirFlowSetpoint_1_Object = MibScalar
airFlowSetpoint_1 = _AirFlowSetpoint_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 199),
    _AirFlowSetpoint_1_Type()
)
airFlowSetpoint_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    airFlowSetpoint_1.setStatus("current")
_AirPresSetpoint_1_Type = Integer32
_AirPresSetpoint_1_Object = MibScalar
airPresSetpoint_1 = _AirPresSetpoint_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 200),
    _AirPresSetpoint_1_Type()
)
airPresSetpoint_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    airPresSetpoint_1.setStatus("current")
_AirDTSetpoint_1_Type = Integer32
_AirDTSetpoint_1_Object = MibScalar
airDTSetpoint_1 = _AirDTSetpoint_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 201),
    _AirDTSetpoint_1_Type()
)
airDTSetpoint_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    airDTSetpoint_1.setStatus("current")
_TempControlSel_1_Type = Integer32
_TempControlSel_1_Object = MibScalar
tempControlSel_1 = _TempControlSel_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 202),
    _TempControlSel_1_Type()
)
tempControlSel_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempControlSel_1.setStatus("current")
_TempControlType_1_Type = Integer32
_TempControlType_1_Object = MibScalar
tempControlType_1 = _TempControlType_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 203),
    _TempControlType_1_Type()
)
tempControlType_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempControlType_1.setStatus("current")
_TPropBand_1_Type = Integer32
_TPropBand_1_Object = MibScalar
tPropBand_1 = _TPropBand_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 204),
    _TPropBand_1_Type()
)
tPropBand_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tPropBand_1.setStatus("current")
_TIntegralTime_1_Type = Integer32
_TIntegralTime_1_Object = MibScalar
tIntegralTime_1 = _TIntegralTime_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 205),
    _TIntegralTime_1_Type()
)
tIntegralTime_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tIntegralTime_1.setStatus("current")
_TDerivativeTime_1_Type = Integer32
_TDerivativeTime_1_Object = MibScalar
tDerivativeTime_1 = _TDerivativeTime_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 206),
    _TDerivativeTime_1_Type()
)
tDerivativeTime_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tDerivativeTime_1.setStatus("current")
_HighTAlOffset_1_Type = Integer32
_HighTAlOffset_1_Object = MibScalar
highTAlOffset_1 = _HighTAlOffset_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 207),
    _HighTAlOffset_1_Type()
)
highTAlOffset_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highTAlOffset_1.setStatus("current")
_LowTAlOffset_1_Type = Integer32
_LowTAlOffset_1_Object = MibScalar
lowTAlOffset_1 = _LowTAlOffset_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 208),
    _LowTAlOffset_1_Type()
)
lowTAlOffset_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowTAlOffset_1.setStatus("current")
_HighLimitTThr_1_Type = Integer32
_HighLimitTThr_1_Object = MibScalar
highLimitTThr_1 = _HighLimitTThr_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 209),
    _HighLimitTThr_1_Type()
)
highLimitTThr_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highLimitTThr_1.setStatus("current")
_HighLimitTMng_1_Type = Integer32
_HighLimitTMng_1_Object = MibScalar
highLimitTMng_1 = _HighLimitTMng_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 210),
    _HighLimitTMng_1_Type()
)
highLimitTMng_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highLimitTMng_1.setStatus("current")
_LowLimitTThr_1_Type = Integer32
_LowLimitTThr_1_Object = MibScalar
lowLimitTThr_1 = _LowLimitTThr_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 211),
    _LowLimitTThr_1_Type()
)
lowLimitTThr_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowLimitTThr_1.setStatus("current")
_LowLimitTMng_1_Type = Integer32
_LowLimitTMng_1_Object = MibScalar
lowLimitTMng_1 = _LowLimitTMng_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 212),
    _LowLimitTMng_1_Type()
)
lowLimitTMng_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowLimitTMng_1.setStatus("current")
_DehumPropBand_1_Type = Integer32
_DehumPropBand_1_Object = MibScalar
dehumPropBand_1 = _DehumPropBand_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 213),
    _DehumPropBand_1_Type()
)
dehumPropBand_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dehumPropBand_1.setStatus("current")
_HumPropBand_1_Type = Integer32
_HumPropBand_1_Object = MibScalar
humPropBand_1 = _HumPropBand_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 214),
    _HumPropBand_1_Type()
)
humPropBand_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humPropBand_1.setStatus("current")
_HRetHAlOffset_1_Type = Integer32
_HRetHAlOffset_1_Object = MibScalar
hRetHAlOffset_1 = _HRetHAlOffset_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 215),
    _HRetHAlOffset_1_Type()
)
hRetHAlOffset_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hRetHAlOffset_1.setStatus("current")
_LRetHAlOffset_1_Type = Integer32
_LRetHAlOffset_1_Object = MibScalar
lRetHAlOffset_1 = _LRetHAlOffset_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 216),
    _LRetHAlOffset_1_Type()
)
lRetHAlOffset_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lRetHAlOffset_1.setStatus("current")
_HighSupHumThr_1_Type = Integer32
_HighSupHumThr_1_Object = MibScalar
highSupHumThr_1 = _HighSupHumThr_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 217),
    _HighSupHumThr_1_Type()
)
highSupHumThr_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highSupHumThr_1.setStatus("current")
_LowSupHumThr_1_Type = Integer32
_LowSupHumThr_1_Object = MibScalar
lowSupHumThr_1 = _LowSupHumThr_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 218),
    _LowSupHumThr_1_Type()
)
lowSupHumThr_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowSupHumThr_1.setStatus("current")
_FCDelta_1_Type = Integer32
_FCDelta_1_Object = MibScalar
fCDelta_1 = _FCDelta_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 219),
    _FCDelta_1_Type()
)
fCDelta_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fCDelta_1.setStatus("current")
_TSWaterSet_1_Type = Integer32
_TSWaterSet_1_Object = MibScalar
tSWaterSet_1 = _TSWaterSet_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 220),
    _TSWaterSet_1_Type()
)
tSWaterSet_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tSWaterSet_1.setStatus("current")
_TSWaterPropBand_1_Type = Integer32
_TSWaterPropBand_1_Object = MibScalar
tSWaterPropBand_1 = _TSWaterPropBand_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 221),
    _TSWaterPropBand_1_Type()
)
tSWaterPropBand_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tSWaterPropBand_1.setStatus("current")
_TSAirTempSet_1_Type = Integer32
_TSAirTempSet_1_Object = MibScalar
tSAirTempSet_1 = _TSAirTempSet_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 222),
    _TSAirTempSet_1_Type()
)
tSAirTempSet_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tSAirTempSet_1.setStatus("current")
_CondSetpoint_1_Type = Integer32
_CondSetpoint_1_Object = MibScalar
condSetpoint_1 = _CondSetpoint_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 223),
    _CondSetpoint_1_Type()
)
condSetpoint_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    condSetpoint_1.setStatus("current")
_CondPropoBand_1_Type = Integer32
_CondPropoBand_1_Object = MibScalar
condPropoBand_1 = _CondPropoBand_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 224),
    _CondPropoBand_1_Type()
)
condPropoBand_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    condPropoBand_1.setStatus("current")
_CondSetIncrease_1_Type = Integer32
_CondSetIncrease_1_Object = MibScalar
condSetIncrease_1 = _CondSetIncrease_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 225),
    _CondSetIncrease_1_Type()
)
condSetIncrease_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    condSetIncrease_1.setStatus("current")
_MaxCondSetpoint_1_Type = Integer32
_MaxCondSetpoint_1_Object = MibScalar
maxCondSetpoint_1 = _MaxCondSetpoint_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 226),
    _MaxCondSetpoint_1_Type()
)
maxCondSetpoint_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxCondSetpoint_1.setStatus("current")
_DryCoolerSet_1_Type = Integer32
_DryCoolerSet_1_Object = MibScalar
dryCoolerSet_1 = _DryCoolerSet_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 227),
    _DryCoolerSet_1_Type()
)
dryCoolerSet_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dryCoolerSet_1.setStatus("current")
_DryCoolPropBand_1_Type = Integer32
_DryCoolPropBand_1_Object = MibScalar
dryCoolPropBand_1 = _DryCoolPropBand_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 228),
    _DryCoolPropBand_1_Type()
)
dryCoolPropBand_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dryCoolPropBand_1.setStatus("current")
_DryCoolSetIncr_1_Type = Integer32
_DryCoolSetIncr_1_Object = MibScalar
dryCoolSetIncr_1 = _DryCoolSetIncr_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 229),
    _DryCoolSetIncr_1_Type()
)
dryCoolSetIncr_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dryCoolSetIncr_1.setStatus("current")
_MaxDryCoolerSet_1_Type = Integer32
_MaxDryCoolerSet_1_Object = MibScalar
maxDryCoolerSet_1 = _MaxDryCoolerSet_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 230),
    _MaxDryCoolerSet_1_Type()
)
maxDryCoolerSet_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxDryCoolerSet_1.setStatus("current")
_DirtyFiltSet_1_Type = Integer32
_DirtyFiltSet_1_Object = MibScalar
dirtyFiltSet_1 = _DirtyFiltSet_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 231),
    _DirtyFiltSet_1_Type()
)
dirtyFiltSet_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dirtyFiltSet_1.setStatus("current")
_DirtyFiltDiff_1_Type = Integer32
_DirtyFiltDiff_1_Object = MibScalar
dirtyFiltDiff_1 = _DirtyFiltDiff_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 232),
    _DirtyFiltDiff_1_Type()
)
dirtyFiltDiff_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dirtyFiltDiff_1.setStatus("current")
_InvCompAlCode1_1_Type = Integer32
_InvCompAlCode1_1_Object = MibScalar
invCompAlCode1_1 = _InvCompAlCode1_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 233),
    _InvCompAlCode1_1_Type()
)
invCompAlCode1_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invCompAlCode1_1.setStatus("current")
_InvCompAlCode2_1_Type = Integer32
_InvCompAlCode2_1_Object = MibScalar
invCompAlCode2_1 = _InvCompAlCode2_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 234),
    _InvCompAlCode2_1_Type()
)
invCompAlCode2_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invCompAlCode2_1.setStatus("current")
_InvCompAlCode3_1_Type = Integer32
_InvCompAlCode3_1_Object = MibScalar
invCompAlCode3_1 = _InvCompAlCode3_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 235),
    _InvCompAlCode3_1_Type()
)
invCompAlCode3_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invCompAlCode3_1.setStatus("current")
_InvCompAlCode4_1_Type = Integer32
_InvCompAlCode4_1_Object = MibScalar
invCompAlCode4_1 = _InvCompAlCode4_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 236),
    _InvCompAlCode4_1_Type()
)
invCompAlCode4_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invCompAlCode4_1.setStatus("current")
_InvCompAlCode5_1_Type = Integer32
_InvCompAlCode5_1_Object = MibScalar
invCompAlCode5_1 = _InvCompAlCode5_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 2, 237),
    _InvCompAlCode5_1_Type()
)
invCompAlCode5_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invCompAlCode5_1.setStatus("current")
_Alarms1_ObjectIdentity = ObjectIdentity
alarms1 = _Alarms1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3)
)
_GeneralAl_1_Type = Integer32
_GeneralAl_1_Object = MibScalar
generalAl_1 = _GeneralAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 1),
    _GeneralAl_1_Type()
)
generalAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generalAl_1.setStatus("current")
_NotCriticAl_1_Type = Integer32
_NotCriticAl_1_Object = MibScalar
notCriticAl_1 = _NotCriticAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 2),
    _NotCriticAl_1_Type()
)
notCriticAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notCriticAl_1.setStatus("current")
_CriticalAl_1_Type = Integer32
_CriticalAl_1_Object = MibScalar
criticalAl_1 = _CriticalAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 3),
    _CriticalAl_1_Type()
)
criticalAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    criticalAl_1.setStatus("current")
_FansAl_1_Type = Integer32
_FansAl_1_Object = MibScalar
fansAl_1 = _FansAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 4),
    _FansAl_1_Type()
)
fansAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fansAl_1.setStatus("current")
_CompAl_1_Type = Integer32
_CompAl_1_Object = MibScalar
compAl_1 = _CompAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 5),
    _CompAl_1_Type()
)
compAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compAl_1.setStatus("current")
_TempAl_1_Type = Integer32
_TempAl_1_Object = MibScalar
tempAl_1 = _TempAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 6),
    _TempAl_1_Type()
)
tempAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempAl_1.setStatus("current")
_HumidityAl_1_Type = Integer32
_HumidityAl_1_Object = MibScalar
humidityAl_1 = _HumidityAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 7),
    _HumidityAl_1_Type()
)
humidityAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidityAl_1.setStatus("current")
_DamperAl_1_Type = Integer32
_DamperAl_1_Object = MibScalar
damperAl_1 = _DamperAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 8),
    _DamperAl_1_Type()
)
damperAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    damperAl_1.setStatus("current")
_FireSmokeAl_1_Type = Integer32
_FireSmokeAl_1_Object = MibScalar
fireSmokeAl_1 = _FireSmokeAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 9),
    _FireSmokeAl_1_Type()
)
fireSmokeAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fireSmokeAl_1.setStatus("current")
_GSeriousAl_1_Type = Integer32
_GSeriousAl_1_Object = MibScalar
gSeriousAl_1 = _GSeriousAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 10),
    _GSeriousAl_1_Type()
)
gSeriousAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gSeriousAl_1.setStatus("current")
_FansGenAl_1_Type = Integer32
_FansGenAl_1_Object = MibScalar
fansGenAl_1 = _FansGenAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 11),
    _FansGenAl_1_Type()
)
fansGenAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fansGenAl_1.setStatus("current")
_F1GeneralAl_1_Type = Integer32
_F1GeneralAl_1_Object = MibScalar
f1GeneralAl_1 = _F1GeneralAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 12),
    _F1GeneralAl_1_Type()
)
f1GeneralAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f1GeneralAl_1.setStatus("current")
_F1PowerAl_1_Type = Integer32
_F1PowerAl_1_Object = MibScalar
f1PowerAl_1 = _F1PowerAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 13),
    _F1PowerAl_1_Type()
)
f1PowerAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f1PowerAl_1.setStatus("current")
_F1CommAl_1_Type = Integer32
_F1CommAl_1_Object = MibScalar
f1CommAl_1 = _F1CommAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 14),
    _F1CommAl_1_Type()
)
f1CommAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f1CommAl_1.setStatus("current")
_F1HiTempAl_1_Type = Integer32
_F1HiTempAl_1_Object = MibScalar
f1HiTempAl_1 = _F1HiTempAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 15),
    _F1HiTempAl_1_Type()
)
f1HiTempAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f1HiTempAl_1.setStatus("current")
_F1NetComAl_1_Type = Integer32
_F1NetComAl_1_Object = MibScalar
f1NetComAl_1 = _F1NetComAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 16),
    _F1NetComAl_1_Type()
)
f1NetComAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f1NetComAl_1.setStatus("current")
_F1InvRegAl_1_Type = Integer32
_F1InvRegAl_1_Object = MibScalar
f1InvRegAl_1 = _F1InvRegAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 17),
    _F1InvRegAl_1_Type()
)
f1InvRegAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f1InvRegAl_1.setStatus("current")
_F1HiMotTAl_1_Type = Integer32
_F1HiMotTAl_1_Object = MibScalar
f1HiMotTAl_1 = _F1HiMotTAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 18),
    _F1HiMotTAl_1_Type()
)
f1HiMotTAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f1HiMotTAl_1.setStatus("current")
_F1HallSenAl_1_Type = Integer32
_F1HallSenAl_1_Object = MibScalar
f1HallSenAl_1 = _F1HallSenAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 19),
    _F1HallSenAl_1_Type()
)
f1HallSenAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f1HallSenAl_1.setStatus("current")
_F1OverlAl_1_Type = Integer32
_F1OverlAl_1_Object = MibScalar
f1OverlAl_1 = _F1OverlAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 20),
    _F1OverlAl_1_Type()
)
f1OverlAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f1OverlAl_1.setStatus("current")
_F1LowDCAl_1_Type = Integer32
_F1LowDCAl_1_Object = MibScalar
f1LowDCAl_1 = _F1LowDCAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 21),
    _F1LowDCAl_1_Type()
)
f1LowDCAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f1LowDCAl_1.setStatus("current")
_F2GeneralAl_1_Type = Integer32
_F2GeneralAl_1_Object = MibScalar
f2GeneralAl_1 = _F2GeneralAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 22),
    _F2GeneralAl_1_Type()
)
f2GeneralAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f2GeneralAl_1.setStatus("current")
_F2PowerAl_1_Type = Integer32
_F2PowerAl_1_Object = MibScalar
f2PowerAl_1 = _F2PowerAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 23),
    _F2PowerAl_1_Type()
)
f2PowerAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f2PowerAl_1.setStatus("current")
_F2CommAl_1_Type = Integer32
_F2CommAl_1_Object = MibScalar
f2CommAl_1 = _F2CommAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 24),
    _F2CommAl_1_Type()
)
f2CommAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f2CommAl_1.setStatus("current")
_F2HiTempAl_1_Type = Integer32
_F2HiTempAl_1_Object = MibScalar
f2HiTempAl_1 = _F2HiTempAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 25),
    _F2HiTempAl_1_Type()
)
f2HiTempAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f2HiTempAl_1.setStatus("current")
_F2NetComAl_1_Type = Integer32
_F2NetComAl_1_Object = MibScalar
f2NetComAl_1 = _F2NetComAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 26),
    _F2NetComAl_1_Type()
)
f2NetComAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f2NetComAl_1.setStatus("current")
_F2InvRegAl_1_Type = Integer32
_F2InvRegAl_1_Object = MibScalar
f2InvRegAl_1 = _F2InvRegAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 27),
    _F2InvRegAl_1_Type()
)
f2InvRegAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f2InvRegAl_1.setStatus("current")
_F2HiMotTAl_1_Type = Integer32
_F2HiMotTAl_1_Object = MibScalar
f2HiMotTAl_1 = _F2HiMotTAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 28),
    _F2HiMotTAl_1_Type()
)
f2HiMotTAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f2HiMotTAl_1.setStatus("current")
_F2HallSenAl_1_Type = Integer32
_F2HallSenAl_1_Object = MibScalar
f2HallSenAl_1 = _F2HallSenAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 29),
    _F2HallSenAl_1_Type()
)
f2HallSenAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f2HallSenAl_1.setStatus("current")
_F2OverlAl_1_Type = Integer32
_F2OverlAl_1_Object = MibScalar
f2OverlAl_1 = _F2OverlAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 30),
    _F2OverlAl_1_Type()
)
f2OverlAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f2OverlAl_1.setStatus("current")
_F2LowDCAl_1_Type = Integer32
_F2LowDCAl_1_Object = MibScalar
f2LowDCAl_1 = _F2LowDCAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 31),
    _F2LowDCAl_1_Type()
)
f2LowDCAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f2LowDCAl_1.setStatus("current")
_F3GeneralAl_1_Type = Integer32
_F3GeneralAl_1_Object = MibScalar
f3GeneralAl_1 = _F3GeneralAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 32),
    _F3GeneralAl_1_Type()
)
f3GeneralAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3GeneralAl_1.setStatus("current")
_F3PowerAl_1_Type = Integer32
_F3PowerAl_1_Object = MibScalar
f3PowerAl_1 = _F3PowerAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 33),
    _F3PowerAl_1_Type()
)
f3PowerAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PowerAl_1.setStatus("current")
_F3CommAl_1_Type = Integer32
_F3CommAl_1_Object = MibScalar
f3CommAl_1 = _F3CommAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 34),
    _F3CommAl_1_Type()
)
f3CommAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3CommAl_1.setStatus("current")
_F3HiTempAl_1_Type = Integer32
_F3HiTempAl_1_Object = MibScalar
f3HiTempAl_1 = _F3HiTempAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 35),
    _F3HiTempAl_1_Type()
)
f3HiTempAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3HiTempAl_1.setStatus("current")
_F3NetComAl_1_Type = Integer32
_F3NetComAl_1_Object = MibScalar
f3NetComAl_1 = _F3NetComAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 36),
    _F3NetComAl_1_Type()
)
f3NetComAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetComAl_1.setStatus("current")
_F3InvRegAl_1_Type = Integer32
_F3InvRegAl_1_Object = MibScalar
f3InvRegAl_1 = _F3InvRegAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 37),
    _F3InvRegAl_1_Type()
)
f3InvRegAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3InvRegAl_1.setStatus("current")
_F3HiMotTAl_1_Type = Integer32
_F3HiMotTAl_1_Object = MibScalar
f3HiMotTAl_1 = _F3HiMotTAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 38),
    _F3HiMotTAl_1_Type()
)
f3HiMotTAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3HiMotTAl_1.setStatus("current")
_F3HallSenAl_1_Type = Integer32
_F3HallSenAl_1_Object = MibScalar
f3HallSenAl_1 = _F3HallSenAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 39),
    _F3HallSenAl_1_Type()
)
f3HallSenAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3HallSenAl_1.setStatus("current")
_F3OverlAl_1_Type = Integer32
_F3OverlAl_1_Object = MibScalar
f3OverlAl_1 = _F3OverlAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 40),
    _F3OverlAl_1_Type()
)
f3OverlAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3OverlAl_1.setStatus("current")
_F3LowDCAl_1_Type = Integer32
_F3LowDCAl_1_Object = MibScalar
f3LowDCAl_1 = _F3LowDCAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 41),
    _F3LowDCAl_1_Type()
)
f3LowDCAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3LowDCAl_1.setStatus("current")
_F4GeneralAl_1_Type = Integer32
_F4GeneralAl_1_Object = MibScalar
f4GeneralAl_1 = _F4GeneralAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 42),
    _F4GeneralAl_1_Type()
)
f4GeneralAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f4GeneralAl_1.setStatus("current")
_F4PowerAl_1_Type = Integer32
_F4PowerAl_1_Object = MibScalar
f4PowerAl_1 = _F4PowerAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 43),
    _F4PowerAl_1_Type()
)
f4PowerAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f4PowerAl_1.setStatus("current")
_F4CommAl_1_Type = Integer32
_F4CommAl_1_Object = MibScalar
f4CommAl_1 = _F4CommAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 44),
    _F4CommAl_1_Type()
)
f4CommAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f4CommAl_1.setStatus("current")
_F4HiTempAl_1_Type = Integer32
_F4HiTempAl_1_Object = MibScalar
f4HiTempAl_1 = _F4HiTempAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 45),
    _F4HiTempAl_1_Type()
)
f4HiTempAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f4HiTempAl_1.setStatus("current")
_F4NetComAl_1_Type = Integer32
_F4NetComAl_1_Object = MibScalar
f4NetComAl_1 = _F4NetComAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 46),
    _F4NetComAl_1_Type()
)
f4NetComAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f4NetComAl_1.setStatus("current")
_F4InvRegAl_1_Type = Integer32
_F4InvRegAl_1_Object = MibScalar
f4InvRegAl_1 = _F4InvRegAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 47),
    _F4InvRegAl_1_Type()
)
f4InvRegAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f4InvRegAl_1.setStatus("current")
_F4HiMotTAl_1_Type = Integer32
_F4HiMotTAl_1_Object = MibScalar
f4HiMotTAl_1 = _F4HiMotTAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 48),
    _F4HiMotTAl_1_Type()
)
f4HiMotTAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f4HiMotTAl_1.setStatus("current")
_F4HallSenAl_1_Type = Integer32
_F4HallSenAl_1_Object = MibScalar
f4HallSenAl_1 = _F4HallSenAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 49),
    _F4HallSenAl_1_Type()
)
f4HallSenAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f4HallSenAl_1.setStatus("current")
_F4OverlAl_1_Type = Integer32
_F4OverlAl_1_Object = MibScalar
f4OverlAl_1 = _F4OverlAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 50),
    _F4OverlAl_1_Type()
)
f4OverlAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f4OverlAl_1.setStatus("current")
_F4LowDCAl_1_Type = Integer32
_F4LowDCAl_1_Object = MibScalar
f4LowDCAl_1 = _F4LowDCAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 51),
    _F4LowDCAl_1_Type()
)
f4LowDCAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f4LowDCAl_1.setStatus("current")
_F5GeneralAl_1_Type = Integer32
_F5GeneralAl_1_Object = MibScalar
f5GeneralAl_1 = _F5GeneralAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 52),
    _F5GeneralAl_1_Type()
)
f5GeneralAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f5GeneralAl_1.setStatus("current")
_F5PowerAl_1_Type = Integer32
_F5PowerAl_1_Object = MibScalar
f5PowerAl_1 = _F5PowerAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 53),
    _F5PowerAl_1_Type()
)
f5PowerAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f5PowerAl_1.setStatus("current")
_F5CommAl_1_Type = Integer32
_F5CommAl_1_Object = MibScalar
f5CommAl_1 = _F5CommAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 54),
    _F5CommAl_1_Type()
)
f5CommAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f5CommAl_1.setStatus("current")
_F5HiTempAl_1_Type = Integer32
_F5HiTempAl_1_Object = MibScalar
f5HiTempAl_1 = _F5HiTempAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 55),
    _F5HiTempAl_1_Type()
)
f5HiTempAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f5HiTempAl_1.setStatus("current")
_F5NetComAl_1_Type = Integer32
_F5NetComAl_1_Object = MibScalar
f5NetComAl_1 = _F5NetComAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 56),
    _F5NetComAl_1_Type()
)
f5NetComAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f5NetComAl_1.setStatus("current")
_F5InvRegAl_1_Type = Integer32
_F5InvRegAl_1_Object = MibScalar
f5InvRegAl_1 = _F5InvRegAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 57),
    _F5InvRegAl_1_Type()
)
f5InvRegAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f5InvRegAl_1.setStatus("current")
_F5HiMotTAl_1_Type = Integer32
_F5HiMotTAl_1_Object = MibScalar
f5HiMotTAl_1 = _F5HiMotTAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 58),
    _F5HiMotTAl_1_Type()
)
f5HiMotTAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f5HiMotTAl_1.setStatus("current")
_F5HallSenAl_1_Type = Integer32
_F5HallSenAl_1_Object = MibScalar
f5HallSenAl_1 = _F5HallSenAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 59),
    _F5HallSenAl_1_Type()
)
f5HallSenAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f5HallSenAl_1.setStatus("current")
_F5OverlAl_1_Type = Integer32
_F5OverlAl_1_Object = MibScalar
f5OverlAl_1 = _F5OverlAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 60),
    _F5OverlAl_1_Type()
)
f5OverlAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f5OverlAl_1.setStatus("current")
_F5LowDCAl_1_Type = Integer32
_F5LowDCAl_1_Object = MibScalar
f5LowDCAl_1 = _F5LowDCAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 61),
    _F5LowDCAl_1_Type()
)
f5LowDCAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f5LowDCAl_1.setStatus("current")
_F6GeneralAl_1_Type = Integer32
_F6GeneralAl_1_Object = MibScalar
f6GeneralAl_1 = _F6GeneralAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 62),
    _F6GeneralAl_1_Type()
)
f6GeneralAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f6GeneralAl_1.setStatus("current")
_F6PowerAl_1_Type = Integer32
_F6PowerAl_1_Object = MibScalar
f6PowerAl_1 = _F6PowerAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 63),
    _F6PowerAl_1_Type()
)
f6PowerAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f6PowerAl_1.setStatus("current")
_F6CommAl_1_Type = Integer32
_F6CommAl_1_Object = MibScalar
f6CommAl_1 = _F6CommAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 64),
    _F6CommAl_1_Type()
)
f6CommAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f6CommAl_1.setStatus("current")
_F6HiTempAl_1_Type = Integer32
_F6HiTempAl_1_Object = MibScalar
f6HiTempAl_1 = _F6HiTempAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 65),
    _F6HiTempAl_1_Type()
)
f6HiTempAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f6HiTempAl_1.setStatus("current")
_F6NetComAl_1_Type = Integer32
_F6NetComAl_1_Object = MibScalar
f6NetComAl_1 = _F6NetComAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 66),
    _F6NetComAl_1_Type()
)
f6NetComAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f6NetComAl_1.setStatus("current")
_F6InvRegAl_1_Type = Integer32
_F6InvRegAl_1_Object = MibScalar
f6InvRegAl_1 = _F6InvRegAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 67),
    _F6InvRegAl_1_Type()
)
f6InvRegAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f6InvRegAl_1.setStatus("current")
_F6HiMotTAl_1_Type = Integer32
_F6HiMotTAl_1_Object = MibScalar
f6HiMotTAl_1 = _F6HiMotTAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 68),
    _F6HiMotTAl_1_Type()
)
f6HiMotTAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f6HiMotTAl_1.setStatus("current")
_F6HallSenAl_1_Type = Integer32
_F6HallSenAl_1_Object = MibScalar
f6HallSenAl_1 = _F6HallSenAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 69),
    _F6HallSenAl_1_Type()
)
f6HallSenAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f6HallSenAl_1.setStatus("current")
_F6OverlAl_1_Type = Integer32
_F6OverlAl_1_Object = MibScalar
f6OverlAl_1 = _F6OverlAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 70),
    _F6OverlAl_1_Type()
)
f6OverlAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f6OverlAl_1.setStatus("current")
_F6LowDCAl_1_Type = Integer32
_F6LowDCAl_1_Object = MibScalar
f6LowDCAl_1 = _F6LowDCAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 71),
    _F6LowDCAl_1_Type()
)
f6LowDCAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f6LowDCAl_1.setStatus("current")
_F7GeneralAl_1_Type = Integer32
_F7GeneralAl_1_Object = MibScalar
f7GeneralAl_1 = _F7GeneralAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 72),
    _F7GeneralAl_1_Type()
)
f7GeneralAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f7GeneralAl_1.setStatus("current")
_F7PowerAl_1_Type = Integer32
_F7PowerAl_1_Object = MibScalar
f7PowerAl_1 = _F7PowerAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 73),
    _F7PowerAl_1_Type()
)
f7PowerAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f7PowerAl_1.setStatus("current")
_F7CommAl_1_Type = Integer32
_F7CommAl_1_Object = MibScalar
f7CommAl_1 = _F7CommAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 74),
    _F7CommAl_1_Type()
)
f7CommAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f7CommAl_1.setStatus("current")
_F7HiTempAl_1_Type = Integer32
_F7HiTempAl_1_Object = MibScalar
f7HiTempAl_1 = _F7HiTempAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 75),
    _F7HiTempAl_1_Type()
)
f7HiTempAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f7HiTempAl_1.setStatus("current")
_F7NetComAl_1_Type = Integer32
_F7NetComAl_1_Object = MibScalar
f7NetComAl_1 = _F7NetComAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 76),
    _F7NetComAl_1_Type()
)
f7NetComAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f7NetComAl_1.setStatus("current")
_F7InvRegAl_1_Type = Integer32
_F7InvRegAl_1_Object = MibScalar
f7InvRegAl_1 = _F7InvRegAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 77),
    _F7InvRegAl_1_Type()
)
f7InvRegAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f7InvRegAl_1.setStatus("current")
_F7HiMotTAl_1_Type = Integer32
_F7HiMotTAl_1_Object = MibScalar
f7HiMotTAl_1 = _F7HiMotTAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 78),
    _F7HiMotTAl_1_Type()
)
f7HiMotTAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f7HiMotTAl_1.setStatus("current")
_F7HallSenAl_1_Type = Integer32
_F7HallSenAl_1_Object = MibScalar
f7HallSenAl_1 = _F7HallSenAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 79),
    _F7HallSenAl_1_Type()
)
f7HallSenAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f7HallSenAl_1.setStatus("current")
_F7OverlAl_1_Type = Integer32
_F7OverlAl_1_Object = MibScalar
f7OverlAl_1 = _F7OverlAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 80),
    _F7OverlAl_1_Type()
)
f7OverlAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f7OverlAl_1.setStatus("current")
_F7LowDCAl_1_Type = Integer32
_F7LowDCAl_1_Object = MibScalar
f7LowDCAl_1 = _F7LowDCAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 81),
    _F7LowDCAl_1_Type()
)
f7LowDCAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f7LowDCAl_1.setStatus("current")
_F8GeneralAl_1_Type = Integer32
_F8GeneralAl_1_Object = MibScalar
f8GeneralAl_1 = _F8GeneralAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 82),
    _F8GeneralAl_1_Type()
)
f8GeneralAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f8GeneralAl_1.setStatus("current")
_F8PowerAl_1_Type = Integer32
_F8PowerAl_1_Object = MibScalar
f8PowerAl_1 = _F8PowerAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 83),
    _F8PowerAl_1_Type()
)
f8PowerAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f8PowerAl_1.setStatus("current")
_F8CommAl_1_Type = Integer32
_F8CommAl_1_Object = MibScalar
f8CommAl_1 = _F8CommAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 84),
    _F8CommAl_1_Type()
)
f8CommAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f8CommAl_1.setStatus("current")
_F8HiTempAl_1_Type = Integer32
_F8HiTempAl_1_Object = MibScalar
f8HiTempAl_1 = _F8HiTempAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 85),
    _F8HiTempAl_1_Type()
)
f8HiTempAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f8HiTempAl_1.setStatus("current")
_F8NetComAl_1_Type = Integer32
_F8NetComAl_1_Object = MibScalar
f8NetComAl_1 = _F8NetComAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 86),
    _F8NetComAl_1_Type()
)
f8NetComAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f8NetComAl_1.setStatus("current")
_F8InvRegAl_1_Type = Integer32
_F8InvRegAl_1_Object = MibScalar
f8InvRegAl_1 = _F8InvRegAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 87),
    _F8InvRegAl_1_Type()
)
f8InvRegAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f8InvRegAl_1.setStatus("current")
_F8HiMotTAl_1_Type = Integer32
_F8HiMotTAl_1_Object = MibScalar
f8HiMotTAl_1 = _F8HiMotTAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 88),
    _F8HiMotTAl_1_Type()
)
f8HiMotTAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f8HiMotTAl_1.setStatus("current")
_F8HallSenAl_1_Type = Integer32
_F8HallSenAl_1_Object = MibScalar
f8HallSenAl_1 = _F8HallSenAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 89),
    _F8HallSenAl_1_Type()
)
f8HallSenAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f8HallSenAl_1.setStatus("current")
_F8OverlAl_1_Type = Integer32
_F8OverlAl_1_Object = MibScalar
f8OverlAl_1 = _F8OverlAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 90),
    _F8OverlAl_1_Type()
)
f8OverlAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f8OverlAl_1.setStatus("current")
_F8LowDCAl_1_Type = Integer32
_F8LowDCAl_1_Object = MibScalar
f8LowDCAl_1 = _F8LowDCAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 91),
    _F8LowDCAl_1_Type()
)
f8LowDCAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f8LowDCAl_1.setStatus("current")
_F9GeneralAl_1_Type = Integer32
_F9GeneralAl_1_Object = MibScalar
f9GeneralAl_1 = _F9GeneralAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 92),
    _F9GeneralAl_1_Type()
)
f9GeneralAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f9GeneralAl_1.setStatus("current")
_F9PowerAl_1_Type = Integer32
_F9PowerAl_1_Object = MibScalar
f9PowerAl_1 = _F9PowerAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 93),
    _F9PowerAl_1_Type()
)
f9PowerAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f9PowerAl_1.setStatus("current")
_F9CommAl_1_Type = Integer32
_F9CommAl_1_Object = MibScalar
f9CommAl_1 = _F9CommAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 94),
    _F9CommAl_1_Type()
)
f9CommAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f9CommAl_1.setStatus("current")
_F9HiTempAl_1_Type = Integer32
_F9HiTempAl_1_Object = MibScalar
f9HiTempAl_1 = _F9HiTempAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 95),
    _F9HiTempAl_1_Type()
)
f9HiTempAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f9HiTempAl_1.setStatus("current")
_F9NetComAl_1_Type = Integer32
_F9NetComAl_1_Object = MibScalar
f9NetComAl_1 = _F9NetComAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 96),
    _F9NetComAl_1_Type()
)
f9NetComAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f9NetComAl_1.setStatus("current")
_F9InvRegAl_1_Type = Integer32
_F9InvRegAl_1_Object = MibScalar
f9InvRegAl_1 = _F9InvRegAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 97),
    _F9InvRegAl_1_Type()
)
f9InvRegAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f9InvRegAl_1.setStatus("current")
_F9HiMotTAl_1_Type = Integer32
_F9HiMotTAl_1_Object = MibScalar
f9HiMotTAl_1 = _F9HiMotTAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 98),
    _F9HiMotTAl_1_Type()
)
f9HiMotTAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f9HiMotTAl_1.setStatus("current")
_F9HallSenAl_1_Type = Integer32
_F9HallSenAl_1_Object = MibScalar
f9HallSenAl_1 = _F9HallSenAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 99),
    _F9HallSenAl_1_Type()
)
f9HallSenAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f9HallSenAl_1.setStatus("current")
_F9OverlAl_1_Type = Integer32
_F9OverlAl_1_Object = MibScalar
f9OverlAl_1 = _F9OverlAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 100),
    _F9OverlAl_1_Type()
)
f9OverlAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f9OverlAl_1.setStatus("current")
_F9LowDCAl_1_Type = Integer32
_F9LowDCAl_1_Object = MibScalar
f9LowDCAl_1 = _F9LowDCAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 101),
    _F9LowDCAl_1_Type()
)
f9LowDCAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f9LowDCAl_1.setStatus("current")
_F10GenlAl_1_Type = Integer32
_F10GenlAl_1_Object = MibScalar
f10GenlAl_1 = _F10GenlAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 102),
    _F10GenlAl_1_Type()
)
f10GenlAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10GenlAl_1.setStatus("current")
_F10PowerAl_1_Type = Integer32
_F10PowerAl_1_Object = MibScalar
f10PowerAl_1 = _F10PowerAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 103),
    _F10PowerAl_1_Type()
)
f10PowerAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10PowerAl_1.setStatus("current")
_F10CommAl_1_Type = Integer32
_F10CommAl_1_Object = MibScalar
f10CommAl_1 = _F10CommAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 104),
    _F10CommAl_1_Type()
)
f10CommAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10CommAl_1.setStatus("current")
_F10HiTempAl_1_Type = Integer32
_F10HiTempAl_1_Object = MibScalar
f10HiTempAl_1 = _F10HiTempAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 105),
    _F10HiTempAl_1_Type()
)
f10HiTempAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10HiTempAl_1.setStatus("current")
_F10NetComAl_1_Type = Integer32
_F10NetComAl_1_Object = MibScalar
f10NetComAl_1 = _F10NetComAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 106),
    _F10NetComAl_1_Type()
)
f10NetComAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10NetComAl_1.setStatus("current")
_F10InvRegAl_1_Type = Integer32
_F10InvRegAl_1_Object = MibScalar
f10InvRegAl_1 = _F10InvRegAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 107),
    _F10InvRegAl_1_Type()
)
f10InvRegAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10InvRegAl_1.setStatus("current")
_F10HiMotTAl_1_Type = Integer32
_F10HiMotTAl_1_Object = MibScalar
f10HiMotTAl_1 = _F10HiMotTAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 108),
    _F10HiMotTAl_1_Type()
)
f10HiMotTAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10HiMotTAl_1.setStatus("current")
_F10HallSAl_1_Type = Integer32
_F10HallSAl_1_Object = MibScalar
f10HallSAl_1 = _F10HallSAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 109),
    _F10HallSAl_1_Type()
)
f10HallSAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10HallSAl_1.setStatus("current")
_F10OverlAl_1_Type = Integer32
_F10OverlAl_1_Object = MibScalar
f10OverlAl_1 = _F10OverlAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 110),
    _F10OverlAl_1_Type()
)
f10OverlAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10OverlAl_1.setStatus("current")
_F10LowDCAl_1_Type = Integer32
_F10LowDCAl_1_Object = MibScalar
f10LowDCAl_1 = _F10LowDCAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 111),
    _F10LowDCAl_1_Type()
)
f10LowDCAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10LowDCAl_1.setStatus("current")
_RetTempPbAl_1_Type = Integer32
_RetTempPbAl_1_Object = MibScalar
retTempPbAl_1 = _RetTempPbAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 112),
    _RetTempPbAl_1_Type()
)
retTempPbAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    retTempPbAl_1.setStatus("current")
_SupTempPrAl_1_Type = Integer32
_SupTempPrAl_1_Object = MibScalar
supTempPrAl_1 = _SupTempPrAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 113),
    _SupTempPrAl_1_Type()
)
supTempPrAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supTempPrAl_1.setStatus("current")
_RetHumPrAl_1_Type = Integer32
_RetHumPrAl_1_Object = MibScalar
retHumPrAl_1 = _RetHumPrAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 114),
    _RetHumPrAl_1_Type()
)
retHumPrAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    retHumPrAl_1.setStatus("current")
_SupHumPrAl_1_Type = Integer32
_SupHumPrAl_1_Object = MibScalar
supHumPrAl_1 = _SupHumPrAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 115),
    _SupHumPrAl_1_Type()
)
supHumPrAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supHumPrAl_1.setStatus("current")
_AirPrSensAl_1_Type = Integer32
_AirPrSensAl_1_Object = MibScalar
airPrSensAl_1 = _AirPrSensAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 116),
    _AirPrSensAl_1_Type()
)
airPrSensAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airPrSensAl_1.setStatus("current")
_WatIN1PrAl_1_Type = Integer32
_WatIN1PrAl_1_Object = MibScalar
watIN1PrAl_1 = _WatIN1PrAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 117),
    _WatIN1PrAl_1_Type()
)
watIN1PrAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    watIN1PrAl_1.setStatus("current")
_WatOUT1PrAl_1_Type = Integer32
_WatOUT1PrAl_1_Object = MibScalar
watOUT1PrAl_1 = _WatOUT1PrAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 118),
    _WatOUT1PrAl_1_Type()
)
watOUT1PrAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    watOUT1PrAl_1.setStatus("current")
_WatIN2PrAl_1_Type = Integer32
_WatIN2PrAl_1_Object = MibScalar
watIN2PrAl_1 = _WatIN2PrAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 119),
    _WatIN2PrAl_1_Type()
)
watIN2PrAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    watIN2PrAl_1.setStatus("current")
_WatOUT2PrAl_1_Type = Integer32
_WatOUT2PrAl_1_Object = MibScalar
watOUT2PrAl_1 = _WatOUT2PrAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 120),
    _WatOUT2PrAl_1_Type()
)
watOUT2PrAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    watOUT2PrAl_1.setStatus("current")
_WatFlw1PrAl_1_Type = Integer32
_WatFlw1PrAl_1_Object = MibScalar
watFlw1PrAl_1 = _WatFlw1PrAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 121),
    _WatFlw1PrAl_1_Type()
)
watFlw1PrAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    watFlw1PrAl_1.setStatus("current")
_WatFlw2PrAl_1_Type = Integer32
_WatFlw2PrAl_1_Object = MibScalar
watFlw2PrAl_1 = _WatFlw2PrAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 122),
    _WatFlw2PrAl_1_Type()
)
watFlw2PrAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    watFlw2PrAl_1.setStatus("current")
_DFPSGenAl_1_Type = Integer32
_DFPSGenAl_1_Object = MibScalar
dFPSGenAl_1 = _DFPSGenAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 123),
    _DFPSGenAl_1_Type()
)
dFPSGenAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dFPSGenAl_1.setStatus("current")
_DFPSBrokAl_1_Type = Integer32
_DFPSBrokAl_1_Object = MibScalar
dFPSBrokAl_1 = _DFPSBrokAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 124),
    _DFPSBrokAl_1_Type()
)
dFPSBrokAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dFPSBrokAl_1.setStatus("current")
_DFPSCablAl_1_Type = Integer32
_DFPSCablAl_1_Object = MibScalar
dFPSCablAl_1 = _DFPSCablAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 125),
    _DFPSCablAl_1_Type()
)
dFPSCablAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dFPSCablAl_1.setStatus("current")
_DFPSRangeAl_1_Type = Integer32
_DFPSRangeAl_1_Object = MibScalar
dFPSRangeAl_1 = _DFPSRangeAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 126),
    _DFPSRangeAl_1_Type()
)
dFPSRangeAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dFPSRangeAl_1.setStatus("current")
_DFPSADCAl_1_Type = Integer32
_DFPSADCAl_1_Object = MibScalar
dFPSADCAl_1 = _DFPSADCAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 127),
    _DFPSADCAl_1_Type()
)
dFPSADCAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dFPSADCAl_1.setStatus("current")
_DFPSSetAl_1_Type = Integer32
_DFPSSetAl_1_Object = MibScalar
dFPSSetAl_1 = _DFPSSetAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 128),
    _DFPSSetAl_1_Type()
)
dFPSSetAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dFPSSetAl_1.setStatus("current")
_DFPSDCOAl_1_Type = Integer32
_DFPSDCOAl_1_Object = MibScalar
dFPSDCOAl_1 = _DFPSDCOAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 129),
    _DFPSDCOAl_1_Type()
)
dFPSDCOAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dFPSDCOAl_1.setStatus("current")
_DFPSWatdAl_1_Type = Integer32
_DFPSWatdAl_1_Object = MibScalar
dFPSWatdAl_1 = _DFPSWatdAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 130),
    _DFPSWatdAl_1_Type()
)
dFPSWatdAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dFPSWatdAl_1.setStatus("current")
_DFPSCommAl_1_Type = Integer32
_DFPSCommAl_1_Object = MibScalar
dFPSCommAl_1 = _DFPSCommAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 131),
    _DFPSCommAl_1_Type()
)
dFPSCommAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dFPSCommAl_1.setStatus("current")
_InvC1GenAl_1_Type = Integer32
_InvC1GenAl_1_Object = MibScalar
invC1GenAl_1 = _InvC1GenAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 132),
    _InvC1GenAl_1_Type()
)
invC1GenAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invC1GenAl_1.setStatus("current")
_InvC1CommAl_1_Type = Integer32
_InvC1CommAl_1_Object = MibScalar
invC1CommAl_1 = _InvC1CommAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 133),
    _InvC1CommAl_1_Type()
)
invC1CommAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invC1CommAl_1.setStatus("current")
_C1ThermAl_1_Type = Integer32
_C1ThermAl_1_Object = MibScalar
c1ThermAl_1 = _C1ThermAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 134),
    _C1ThermAl_1_Type()
)
c1ThermAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c1ThermAl_1.setStatus("current")
_C1HighPresAl_1_Type = Integer32
_C1HighPresAl_1_Object = MibScalar
c1HighPresAl_1 = _C1HighPresAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 135),
    _C1HighPresAl_1_Type()
)
c1HighPresAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c1HighPresAl_1.setStatus("current")
_C1LowPresAl_1_Type = Integer32
_C1LowPresAl_1_Object = MibScalar
c1LowPresAl_1 = _C1LowPresAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 136),
    _C1LowPresAl_1_Type()
)
c1LowPresAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c1LowPresAl_1.setStatus("current")
_C1HighDiscAl_1_Type = Integer32
_C1HighDiscAl_1_Object = MibScalar
c1HighDiscAl_1 = _C1HighDiscAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 137),
    _C1HighDiscAl_1_Type()
)
c1HighDiscAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c1HighDiscAl_1.setStatus("current")
_C1LCompRatAl_1_Type = Integer32
_C1LCompRatAl_1_Object = MibScalar
c1LCompRatAl_1 = _C1LCompRatAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 138),
    _C1LCompRatAl_1_Type()
)
c1LCompRatAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c1LCompRatAl_1.setStatus("current")
_Condenser1Al_1_Type = Integer32
_Condenser1Al_1_Object = MibScalar
condenser1Al_1 = _Condenser1Al_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 139),
    _Condenser1Al_1_Type()
)
condenser1Al_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    condenser1Al_1.setStatus("current")
_C1WatFlowAl_1_Type = Integer32
_C1WatFlowAl_1_Object = MibScalar
c1WatFlowAl_1 = _C1WatFlowAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 140),
    _C1WatFlowAl_1_Type()
)
c1WatFlowAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c1WatFlowAl_1.setStatus("current")
_EEV1GenAl_1_Type = Integer32
_EEV1GenAl_1_Object = MibScalar
eEV1GenAl_1 = _EEV1GenAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 141),
    _EEV1GenAl_1_Type()
)
eEV1GenAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eEV1GenAl_1.setStatus("current")
_EEV1CommAl_1_Type = Integer32
_EEV1CommAl_1_Object = MibScalar
eEV1CommAl_1 = _EEV1CommAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 142),
    _EEV1CommAl_1_Type()
)
eEV1CommAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eEV1CommAl_1.setStatus("current")
_EEV1SuctPrAl_1_Type = Integer32
_EEV1SuctPrAl_1_Object = MibScalar
eEV1SuctPrAl_1 = _EEV1SuctPrAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 143),
    _EEV1SuctPrAl_1_Type()
)
eEV1SuctPrAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eEV1SuctPrAl_1.setStatus("current")
_EEV1EvapPrAl_1_Type = Integer32
_EEV1EvapPrAl_1_Object = MibScalar
eEV1EvapPrAl_1 = _EEV1EvapPrAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 144),
    _EEV1EvapPrAl_1_Type()
)
eEV1EvapPrAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eEV1EvapPrAl_1.setStatus("current")
_EEV1CondPrAl_1_Type = Integer32
_EEV1CondPrAl_1_Object = MibScalar
eEV1CondPrAl_1 = _EEV1CondPrAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 145),
    _EEV1CondPrAl_1_Type()
)
eEV1CondPrAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eEV1CondPrAl_1.setStatus("current")
_EEV1DiscPrAl_1_Type = Integer32
_EEV1DiscPrAl_1_Object = MibScalar
eEV1DiscPrAl_1 = _EEV1DiscPrAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 146),
    _EEV1DiscPrAl_1_Type()
)
eEV1DiscPrAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eEV1DiscPrAl_1.setStatus("current")
_C2ThermAl_1_Type = Integer32
_C2ThermAl_1_Object = MibScalar
c2ThermAl_1 = _C2ThermAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 147),
    _C2ThermAl_1_Type()
)
c2ThermAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2ThermAl_1.setStatus("current")
_C2HighPresAl_1_Type = Integer32
_C2HighPresAl_1_Object = MibScalar
c2HighPresAl_1 = _C2HighPresAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 148),
    _C2HighPresAl_1_Type()
)
c2HighPresAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2HighPresAl_1.setStatus("current")
_C2LowPresAl_1_Type = Integer32
_C2LowPresAl_1_Object = MibScalar
c2LowPresAl_1 = _C2LowPresAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 149),
    _C2LowPresAl_1_Type()
)
c2LowPresAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2LowPresAl_1.setStatus("current")
_C2HighDiscAl_1_Type = Integer32
_C2HighDiscAl_1_Object = MibScalar
c2HighDiscAl_1 = _C2HighDiscAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 150),
    _C2HighDiscAl_1_Type()
)
c2HighDiscAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2HighDiscAl_1.setStatus("current")
_C2LCompRatAl_1_Type = Integer32
_C2LCompRatAl_1_Object = MibScalar
c2LCompRatAl_1 = _C2LCompRatAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 151),
    _C2LCompRatAl_1_Type()
)
c2LCompRatAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2LCompRatAl_1.setStatus("current")
_Condenser2Al_1_Type = Integer32
_Condenser2Al_1_Object = MibScalar
condenser2Al_1 = _Condenser2Al_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 152),
    _Condenser2Al_1_Type()
)
condenser2Al_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    condenser2Al_1.setStatus("current")
_C2WatFlowAl_1_Type = Integer32
_C2WatFlowAl_1_Object = MibScalar
c2WatFlowAl_1 = _C2WatFlowAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 153),
    _C2WatFlowAl_1_Type()
)
c2WatFlowAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2WatFlowAl_1.setStatus("current")
_EEV2GenAl_1_Type = Integer32
_EEV2GenAl_1_Object = MibScalar
eEV2GenAl_1 = _EEV2GenAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 154),
    _EEV2GenAl_1_Type()
)
eEV2GenAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eEV2GenAl_1.setStatus("current")
_EEV2CommAl_1_Type = Integer32
_EEV2CommAl_1_Object = MibScalar
eEV2CommAl_1 = _EEV2CommAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 155),
    _EEV2CommAl_1_Type()
)
eEV2CommAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eEV2CommAl_1.setStatus("current")
_EEV2SuctPrAl_1_Type = Integer32
_EEV2SuctPrAl_1_Object = MibScalar
eEV2SuctPrAl_1 = _EEV2SuctPrAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 156),
    _EEV2SuctPrAl_1_Type()
)
eEV2SuctPrAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eEV2SuctPrAl_1.setStatus("current")
_EEV2EvapPrAl_1_Type = Integer32
_EEV2EvapPrAl_1_Object = MibScalar
eEV2EvapPrAl_1 = _EEV2EvapPrAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 157),
    _EEV2EvapPrAl_1_Type()
)
eEV2EvapPrAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eEV2EvapPrAl_1.setStatus("current")
_EEV2CondPrAl_1_Type = Integer32
_EEV2CondPrAl_1_Object = MibScalar
eEV2CondPrAl_1 = _EEV2CondPrAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 158),
    _EEV2CondPrAl_1_Type()
)
eEV2CondPrAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eEV2CondPrAl_1.setStatus("current")
_EEV2DiscPrAl_1_Type = Integer32
_EEV2DiscPrAl_1_Object = MibScalar
eEV2DiscPrAl_1 = _EEV2DiscPrAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 159),
    _EEV2DiscPrAl_1_Type()
)
eEV2DiscPrAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eEV2DiscPrAl_1.setStatus("current")
_IntHumGenAl_1_Type = Integer32
_IntHumGenAl_1_Object = MibScalar
intHumGenAl_1 = _IntHumGenAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 160),
    _IntHumGenAl_1_Type()
)
intHumGenAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intHumGenAl_1.setStatus("current")
_CPYCommAl_1_Type = Integer32
_CPYCommAl_1_Object = MibScalar
cPYCommAl_1 = _CPYCommAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 161),
    _CPYCommAl_1_Type()
)
cPYCommAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPYCommAl_1.setStatus("current")
_CPYMemoryAl_1_Type = Integer32
_CPYMemoryAl_1_Object = MibScalar
cPYMemoryAl_1 = _CPYMemoryAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 162),
    _CPYMemoryAl_1_Type()
)
cPYMemoryAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPYMemoryAl_1.setStatus("current")
_CPYParamAl_1_Type = Integer32
_CPYParamAl_1_Object = MibScalar
cPYParamAl_1 = _CPYParamAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 163),
    _CPYParamAl_1_Type()
)
cPYParamAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPYParamAl_1.setStatus("current")
_CPYHighCurAl_1_Type = Integer32
_CPYHighCurAl_1_Object = MibScalar
cPYHighCurAl_1 = _CPYHighCurAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 164),
    _CPYHighCurAl_1_Type()
)
cPYHighCurAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPYHighCurAl_1.setStatus("current")
_CPYLoSteamAl_1_Type = Integer32
_CPYLoSteamAl_1_Object = MibScalar
cPYLoSteamAl_1 = _CPYLoSteamAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 165),
    _CPYLoSteamAl_1_Type()
)
cPYLoSteamAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPYLoSteamAl_1.setStatus("current")
_CPYDrainAl_1_Type = Integer32
_CPYDrainAl_1_Object = MibScalar
cPYDrainAl_1 = _CPYDrainAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 166),
    _CPYDrainAl_1_Type()
)
cPYDrainAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPYDrainAl_1.setStatus("current")
_CPYMaintAl_1_Type = Integer32
_CPYMaintAl_1_Object = MibScalar
cPYMaintAl_1 = _CPYMaintAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 167),
    _CPYMaintAl_1_Type()
)
cPYMaintAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPYMaintAl_1.setStatus("current")
_CPYNoWaterAl_1_Type = Integer32
_CPYNoWaterAl_1_Object = MibScalar
cPYNoWaterAl_1 = _CPYNoWaterAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 168),
    _CPYNoWaterAl_1_Type()
)
cPYNoWaterAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPYNoWaterAl_1.setStatus("current")
_CPYCylMainAl_1_Type = Integer32
_CPYCylMainAl_1_Object = MibScalar
cPYCylMainAl_1 = _CPYCylMainAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 169),
    _CPYCylMainAl_1_Type()
)
cPYCylMainAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPYCylMainAl_1.setStatus("current")
_CPYDirtCylAl_1_Type = Integer32
_CPYDirtCylAl_1_Object = MibScalar
cPYDirtCylAl_1 = _CPYDirtCylAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 170),
    _CPYDirtCylAl_1_Type()
)
cPYDirtCylAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPYDirtCylAl_1.setStatus("current")
_CPYFoamAl_1_Type = Integer32
_CPYFoamAl_1_Object = MibScalar
cPYFoamAl_1 = _CPYFoamAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 171),
    _CPYFoamAl_1_Type()
)
cPYFoamAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPYFoamAl_1.setStatus("current")
_CPYLifeTimAl_1_Type = Integer32
_CPYLifeTimAl_1_Object = MibScalar
cPYLifeTimAl_1 = _CPYLifeTimAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 172),
    _CPYLifeTimAl_1_Type()
)
cPYLifeTimAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPYLifeTimAl_1.setStatus("current")
_CPYHiWLevAl_1_Type = Integer32
_CPYHiWLevAl_1_Object = MibScalar
cPYHiWLevAl_1 = _CPYHiWLevAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 173),
    _CPYHiWLevAl_1_Type()
)
cPYHiWLevAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPYHiWLevAl_1.setStatus("current")
_CPYHWatConAl_1_Type = Integer32
_CPYHWatConAl_1_Object = MibScalar
cPYHWatConAl_1 = _CPYHWatConAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 174),
    _CPYHWatConAl_1_Type()
)
cPYHWatConAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPYHWatConAl_1.setStatus("current")
_CPYConnAl_1_Type = Integer32
_CPYConnAl_1_Object = MibScalar
cPYConnAl_1 = _CPYConnAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 175),
    _CPYConnAl_1_Type()
)
cPYConnAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPYConnAl_1.setStatus("current")
_WatPresAl_1_Type = Integer32
_WatPresAl_1_Object = MibScalar
watPresAl_1 = _WatPresAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 176),
    _WatPresAl_1_Type()
)
watPresAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    watPresAl_1.setStatus("current")
_DrainPumpAl_1_Type = Integer32
_DrainPumpAl_1_Object = MibScalar
drainPumpAl_1 = _DrainPumpAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 177),
    _DrainPumpAl_1_Type()
)
drainPumpAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drainPumpAl_1.setStatus("current")
_ElHeatAl_1_Type = Integer32
_ElHeatAl_1_Object = MibScalar
elHeatAl_1 = _ElHeatAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 178),
    _ElHeatAl_1_Type()
)
elHeatAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elHeatAl_1.setStatus("current")
_FilterAl_1_Type = Integer32
_FilterAl_1_Object = MibScalar
filterAl_1 = _FilterAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 179),
    _FilterAl_1_Type()
)
filterAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterAl_1.setStatus("current")
_DryCoolerAl_1_Type = Integer32
_DryCoolerAl_1_Object = MibScalar
dryCoolerAl_1 = _DryCoolerAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 180),
    _DryCoolerAl_1_Type()
)
dryCoolerAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dryCoolerAl_1.setStatus("current")
_ExtHumidAl_1_Type = Integer32
_ExtHumidAl_1_Object = MibScalar
extHumidAl_1 = _ExtHumidAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 181),
    _ExtHumidAl_1_Type()
)
extHumidAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extHumidAl_1.setStatus("current")
_WaterPumpAl_1_Type = Integer32
_WaterPumpAl_1_Object = MibScalar
waterPumpAl_1 = _WaterPumpAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 182),
    _WaterPumpAl_1_Type()
)
waterPumpAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    waterPumpAl_1.setStatus("current")
_CondUnitGAl_1_Type = Integer32
_CondUnitGAl_1_Object = MibScalar
condUnitGAl_1 = _CondUnitGAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 183),
    _CondUnitGAl_1_Type()
)
condUnitGAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    condUnitGAl_1.setStatus("current")
_GasLeakAl_1_Type = Integer32
_GasLeakAl_1_Object = MibScalar
gasLeakAl_1 = _GasLeakAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 184),
    _GasLeakAl_1_Type()
)
gasLeakAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gasLeakAl_1.setStatus("current")
_PowerSuppAl_1_Type = Integer32
_PowerSuppAl_1_Object = MibScalar
powerSuppAl_1 = _PowerSuppAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 185),
    _PowerSuppAl_1_Type()
)
powerSuppAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSuppAl_1.setStatus("current")
_GenSoftAl_1_Type = Integer32
_GenSoftAl_1_Object = MibScalar
genSoftAl_1 = _GenSoftAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 186),
    _GenSoftAl_1_Type()
)
genSoftAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genSoftAl_1.setStatus("current")
_LocalNetAl_1_Type = Integer32
_LocalNetAl_1_Object = MibScalar
localNetAl_1 = _LocalNetAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 187),
    _LocalNetAl_1_Type()
)
localNetAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localNetAl_1.setStatus("current")
_RegHiTempAl_1_Type = Integer32
_RegHiTempAl_1_Object = MibScalar
regHiTempAl_1 = _RegHiTempAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 188),
    _RegHiTempAl_1_Type()
)
regHiTempAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regHiTempAl_1.setStatus("current")
_RegLowTempAl_1_Type = Integer32
_RegLowTempAl_1_Object = MibScalar
regLowTempAl_1 = _RegLowTempAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 189),
    _RegLowTempAl_1_Type()
)
regLowTempAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLowTempAl_1.setStatus("current")
_HiLimTempAl_1_Type = Integer32
_HiLimTempAl_1_Object = MibScalar
hiLimTempAl_1 = _HiLimTempAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 190),
    _HiLimTempAl_1_Type()
)
hiLimTempAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hiLimTempAl_1.setStatus("current")
_LowLimTempAl_1_Type = Integer32
_LowLimTempAl_1_Object = MibScalar
lowLimTempAl_1 = _LowLimTempAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 191),
    _LowLimTempAl_1_Type()
)
lowLimTempAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowLimTempAl_1.setStatus("current")
_RetHiHumiAl_1_Type = Integer32
_RetHiHumiAl_1_Object = MibScalar
retHiHumiAl_1 = _RetHiHumiAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 192),
    _RetHiHumiAl_1_Type()
)
retHiHumiAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    retHiHumiAl_1.setStatus("current")
_RetLowHumiAl_1_Type = Integer32
_RetLowHumiAl_1_Object = MibScalar
retLowHumiAl_1 = _RetLowHumiAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 193),
    _RetLowHumiAl_1_Type()
)
retLowHumiAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    retLowHumiAl_1.setStatus("current")
_SupHiHumiAl_1_Type = Integer32
_SupHiHumiAl_1_Object = MibScalar
supHiHumiAl_1 = _SupHiHumiAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 194),
    _SupHiHumiAl_1_Type()
)
supHiHumiAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supHiHumiAl_1.setStatus("current")
_SupLowHumiAl_1_Type = Integer32
_SupLowHumiAl_1_Object = MibScalar
supLowHumiAl_1 = _SupLowHumiAl_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 195),
    _SupLowHumiAl_1_Type()
)
supLowHumiAl_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supLowHumiAl_1.setStatus("current")
_ProbeMod1COM_1_Type = Integer32
_ProbeMod1COM_1_Object = MibScalar
probeMod1COM_1 = _ProbeMod1COM_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 196),
    _ProbeMod1COM_1_Type()
)
probeMod1COM_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probeMod1COM_1.setStatus("current")
_PrMod1err1_1_Type = Integer32
_PrMod1err1_1_Object = MibScalar
prMod1err1_1 = _PrMod1err1_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 197),
    _PrMod1err1_1_Type()
)
prMod1err1_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prMod1err1_1.setStatus("current")
_PrMod1err2_1_Type = Integer32
_PrMod1err2_1_Object = MibScalar
prMod1err2_1 = _PrMod1err2_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 198),
    _PrMod1err2_1_Type()
)
prMod1err2_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prMod1err2_1.setStatus("current")
_PrMod1err3_1_Type = Integer32
_PrMod1err3_1_Object = MibScalar
prMod1err3_1 = _PrMod1err3_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 199),
    _PrMod1err3_1_Type()
)
prMod1err3_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prMod1err3_1.setStatus("current")
_PrMod1err4_1_Type = Integer32
_PrMod1err4_1_Object = MibScalar
prMod1err4_1 = _PrMod1err4_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 200),
    _PrMod1err4_1_Type()
)
prMod1err4_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prMod1err4_1.setStatus("current")
_PrMod1err5_1_Type = Integer32
_PrMod1err5_1_Object = MibScalar
prMod1err5_1 = _PrMod1err5_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 201),
    _PrMod1err5_1_Type()
)
prMod1err5_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prMod1err5_1.setStatus("current")
_PrMod1err6_1_Type = Integer32
_PrMod1err6_1_Object = MibScalar
prMod1err6_1 = _PrMod1err6_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 202),
    _PrMod1err6_1_Type()
)
prMod1err6_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prMod1err6_1.setStatus("current")
_ProbeMod2COM_1_Type = Integer32
_ProbeMod2COM_1_Object = MibScalar
probeMod2COM_1 = _ProbeMod2COM_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 203),
    _ProbeMod2COM_1_Type()
)
probeMod2COM_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probeMod2COM_1.setStatus("current")
_PrMod2err1_1_Type = Integer32
_PrMod2err1_1_Object = MibScalar
prMod2err1_1 = _PrMod2err1_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 204),
    _PrMod2err1_1_Type()
)
prMod2err1_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prMod2err1_1.setStatus("current")
_PrMod2err2_1_Type = Integer32
_PrMod2err2_1_Object = MibScalar
prMod2err2_1 = _PrMod2err2_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 205),
    _PrMod2err2_1_Type()
)
prMod2err2_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prMod2err2_1.setStatus("current")
_PrMod2err3_1_Type = Integer32
_PrMod2err3_1_Object = MibScalar
prMod2err3_1 = _PrMod2err3_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 206),
    _PrMod2err3_1_Type()
)
prMod2err3_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prMod2err3_1.setStatus("current")
_PrMod2err4_1_Type = Integer32
_PrMod2err4_1_Object = MibScalar
prMod2err4_1 = _PrMod2err4_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 207),
    _PrMod2err4_1_Type()
)
prMod2err4_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prMod2err4_1.setStatus("current")
_PrMod2err5_1_Type = Integer32
_PrMod2err5_1_Object = MibScalar
prMod2err5_1 = _PrMod2err5_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 208),
    _PrMod2err5_1_Type()
)
prMod2err5_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prMod2err5_1.setStatus("current")
_PrMod2err6_1_Type = Integer32
_PrMod2err6_1_Object = MibScalar
prMod2err6_1 = _PrMod2err6_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 209),
    _PrMod2err6_1_Type()
)
prMod2err6_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prMod2err6_1.setStatus("current")
_ProbeMod3COM_1_Type = Integer32
_ProbeMod3COM_1_Object = MibScalar
probeMod3COM_1 = _ProbeMod3COM_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 210),
    _ProbeMod3COM_1_Type()
)
probeMod3COM_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probeMod3COM_1.setStatus("current")
_PrMod3err1_1_Type = Integer32
_PrMod3err1_1_Object = MibScalar
prMod3err1_1 = _PrMod3err1_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 211),
    _PrMod3err1_1_Type()
)
prMod3err1_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prMod3err1_1.setStatus("current")
_PrMod3err2_1_Type = Integer32
_PrMod3err2_1_Object = MibScalar
prMod3err2_1 = _PrMod3err2_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 212),
    _PrMod3err2_1_Type()
)
prMod3err2_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prMod3err2_1.setStatus("current")
_PrMod3err3_1_Type = Integer32
_PrMod3err3_1_Object = MibScalar
prMod3err3_1 = _PrMod3err3_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 213),
    _PrMod3err3_1_Type()
)
prMod3err3_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prMod3err3_1.setStatus("current")
_PrMod3err4_1_Type = Integer32
_PrMod3err4_1_Object = MibScalar
prMod3err4_1 = _PrMod3err4_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 214),
    _PrMod3err4_1_Type()
)
prMod3err4_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prMod3err4_1.setStatus("current")
_PrMod3err5_1_Type = Integer32
_PrMod3err5_1_Object = MibScalar
prMod3err5_1 = _PrMod3err5_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 215),
    _PrMod3err5_1_Type()
)
prMod3err5_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prMod3err5_1.setStatus("current")
_PrMod3err6_1_Type = Integer32
_PrMod3err6_1_Object = MibScalar
prMod3err6_1 = _PrMod3err6_1_Object(
    (1, 3, 6, 1, 4, 1, 53332, 1, 3, 216),
    _PrMod3err6_1_Type()
)
prMod3err6_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prMod3err6_1.setStatus("current")
_Node2_ObjectIdentity = ObjectIdentity
node2 = _Node2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 53332, 2)
)
_Traps2_ObjectIdentity = ObjectIdentity
traps2 = _Traps2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0)
)
_BinaryObjects2_ObjectIdentity = ObjectIdentity
binaryObjects2 = _BinaryObjects2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1)
)
_DamperStatusDI_2_Type = Integer32
_DamperStatusDI_2_Object = MibScalar
damperStatusDI_2 = _DamperStatusDI_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 1),
    _DamperStatusDI_2_Type()
)
damperStatusDI_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    damperStatusDI_2.setStatus("current")
_DirtyFilterDI_2_Type = Integer32
_DirtyFilterDI_2_Object = MibScalar
dirtyFilterDI_2 = _DirtyFilterDI_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 2),
    _DirtyFilterDI_2_Type()
)
dirtyFilterDI_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dirtyFilterDI_2.setStatus("current")
_RemoteOffDI_2_Type = Integer32
_RemoteOffDI_2_Object = MibScalar
remoteOffDI_2 = _RemoteOffDI_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 3),
    _RemoteOffDI_2_Type()
)
remoteOffDI_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteOffDI_2.setStatus("current")
_ElHeaterAlarmDI_2_Type = Integer32
_ElHeaterAlarmDI_2_Object = MibScalar
elHeaterAlarmDI_2 = _ElHeaterAlarmDI_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 4),
    _ElHeaterAlarmDI_2_Type()
)
elHeaterAlarmDI_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elHeaterAlarmDI_2.setStatus("current")
_CondPumpAlarmDI_2_Type = Integer32
_CondPumpAlarmDI_2_Object = MibScalar
condPumpAlarmDI_2 = _CondPumpAlarmDI_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 5),
    _CondPumpAlarmDI_2_Type()
)
condPumpAlarmDI_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    condPumpAlarmDI_2.setStatus("current")
_ConfigurableDI1_2_Type = Integer32
_ConfigurableDI1_2_Object = MibScalar
configurableDI1_2 = _ConfigurableDI1_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 6),
    _ConfigurableDI1_2_Type()
)
configurableDI1_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configurableDI1_2.setStatus("current")
_ConfigurableDI2_2_Type = Integer32
_ConfigurableDI2_2_Object = MibScalar
configurableDI2_2 = _ConfigurableDI2_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 7),
    _ConfigurableDI2_2_Type()
)
configurableDI2_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configurableDI2_2.setStatus("current")
_ConfigurableDI3_2_Type = Integer32
_ConfigurableDI3_2_Object = MibScalar
configurableDI3_2 = _ConfigurableDI3_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 8),
    _ConfigurableDI3_2_Type()
)
configurableDI3_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configurableDI3_2.setStatus("current")
_ConfigurableDI4_2_Type = Integer32
_ConfigurableDI4_2_Object = MibScalar
configurableDI4_2 = _ConfigurableDI4_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 9),
    _ConfigurableDI4_2_Type()
)
configurableDI4_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configurableDI4_2.setStatus("current")
_ConfigurableDI5_2_Type = Integer32
_ConfigurableDI5_2_Object = MibScalar
configurableDI5_2 = _ConfigurableDI5_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 10),
    _ConfigurableDI5_2_Type()
)
configurableDI5_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configurableDI5_2.setStatus("current")
_C1ThermAlarmDI_2_Type = Integer32
_C1ThermAlarmDI_2_Object = MibScalar
c1ThermAlarmDI_2 = _C1ThermAlarmDI_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 11),
    _C1ThermAlarmDI_2_Type()
)
c1ThermAlarmDI_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c1ThermAlarmDI_2.setStatus("current")
_C1HPAlarmDI_2_Type = Integer32
_C1HPAlarmDI_2_Object = MibScalar
c1HPAlarmDI_2 = _C1HPAlarmDI_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 12),
    _C1HPAlarmDI_2_Type()
)
c1HPAlarmDI_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c1HPAlarmDI_2.setStatus("current")
_C1LPAlarmDI_2_Type = Integer32
_C1LPAlarmDI_2_Object = MibScalar
c1LPAlarmDI_2 = _C1LPAlarmDI_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 13),
    _C1LPAlarmDI_2_Type()
)
c1LPAlarmDI_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c1LPAlarmDI_2.setStatus("current")
_C2ThermAlarmDI_2_Type = Integer32
_C2ThermAlarmDI_2_Object = MibScalar
c2ThermAlarmDI_2 = _C2ThermAlarmDI_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 14),
    _C2ThermAlarmDI_2_Type()
)
c2ThermAlarmDI_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2ThermAlarmDI_2.setStatus("current")
_C2HPAlarmDI_2_Type = Integer32
_C2HPAlarmDI_2_Object = MibScalar
c2HPAlarmDI_2 = _C2HPAlarmDI_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 15),
    _C2HPAlarmDI_2_Type()
)
c2HPAlarmDI_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2HPAlarmDI_2.setStatus("current")
_C2LPAlarmDI_2_Type = Integer32
_C2LPAlarmDI_2_Object = MibScalar
c2LPAlarmDI_2 = _C2LPAlarmDI_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 16),
    _C2LPAlarmDI_2_Type()
)
c2LPAlarmDI_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2LPAlarmDI_2.setStatus("current")
_FansDO_2_Type = Integer32
_FansDO_2_Object = MibScalar
fansDO_2 = _FansDO_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 17),
    _FansDO_2_Type()
)
fansDO_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fansDO_2.setStatus("current")
_DamperDO_2_Type = Integer32
_DamperDO_2_Object = MibScalar
damperDO_2 = _DamperDO_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 18),
    _DamperDO_2_Type()
)
damperDO_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    damperDO_2.setStatus("current")
_ConfigurableDO1_2_Type = Integer32
_ConfigurableDO1_2_Object = MibScalar
configurableDO1_2 = _ConfigurableDO1_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 19),
    _ConfigurableDO1_2_Type()
)
configurableDO1_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configurableDO1_2.setStatus("current")
_ConfigurableDO2_2_Type = Integer32
_ConfigurableDO2_2_Object = MibScalar
configurableDO2_2 = _ConfigurableDO2_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 20),
    _ConfigurableDO2_2_Type()
)
configurableDO2_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configurableDO2_2.setStatus("current")
_ConfigurableDO3_2_Type = Integer32
_ConfigurableDO3_2_Object = MibScalar
configurableDO3_2 = _ConfigurableDO3_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 21),
    _ConfigurableDO3_2_Type()
)
configurableDO3_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configurableDO3_2.setStatus("current")
_ConfigurableDO4_2_Type = Integer32
_ConfigurableDO4_2_Object = MibScalar
configurableDO4_2 = _ConfigurableDO4_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 22),
    _ConfigurableDO4_2_Type()
)
configurableDO4_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configurableDO4_2.setStatus("current")
_ConfigurableDO5_2_Type = Integer32
_ConfigurableDO5_2_Object = MibScalar
configurableDO5_2 = _ConfigurableDO5_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 23),
    _ConfigurableDO5_2_Type()
)
configurableDO5_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configurableDO5_2.setStatus("current")
_EHeaterStage1DO_2_Type = Integer32
_EHeaterStage1DO_2_Object = MibScalar
eHeaterStage1DO_2 = _EHeaterStage1DO_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 24),
    _EHeaterStage1DO_2_Type()
)
eHeaterStage1DO_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eHeaterStage1DO_2.setStatus("current")
_EHeaterStage2DO_2_Type = Integer32
_EHeaterStage2DO_2_Object = MibScalar
eHeaterStage2DO_2 = _EHeaterStage2DO_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 25),
    _EHeaterStage2DO_2_Type()
)
eHeaterStage2DO_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eHeaterStage2DO_2.setStatus("current")
_Compressor1DO_2_Type = Integer32
_Compressor1DO_2_Object = MibScalar
compressor1DO_2 = _Compressor1DO_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 26),
    _Compressor1DO_2_Type()
)
compressor1DO_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compressor1DO_2.setStatus("current")
_Compressor2DO_2_Type = Integer32
_Compressor2DO_2_Object = MibScalar
compressor2DO_2 = _Compressor2DO_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 27),
    _Compressor2DO_2_Type()
)
compressor2DO_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compressor2DO_2.setStatus("current")
_HumPowerDO_2_Type = Integer32
_HumPowerDO_2_Object = MibScalar
humPowerDO_2 = _HumPowerDO_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 28),
    _HumPowerDO_2_Type()
)
humPowerDO_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humPowerDO_2.setStatus("current")
_HumDrainValveDO_2_Type = Integer32
_HumDrainValveDO_2_Object = MibScalar
humDrainValveDO_2 = _HumDrainValveDO_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 29),
    _HumDrainValveDO_2_Type()
)
humDrainValveDO_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humDrainValveDO_2.setStatus("current")
_HumFillValveDO_2_Type = Integer32
_HumFillValveDO_2_Object = MibScalar
humFillValveDO_2 = _HumFillValveDO_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 30),
    _HumFillValveDO_2_Type()
)
humFillValveDO_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humFillValveDO_2.setStatus("current")
_HumWaterLevel_2_Type = Integer32
_HumWaterLevel_2_Object = MibScalar
humWaterLevel_2 = _HumWaterLevel_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 31),
    _HumWaterLevel_2_Type()
)
humWaterLevel_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humWaterLevel_2.setStatus("current")
_SupervOFF_2_Type = Integer32
_SupervOFF_2_Object = MibScalar
supervOFF_2 = _SupervOFF_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 32),
    _SupervOFF_2_Type()
)
supervOFF_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    supervOFF_2.setStatus("current")
_EnableHumid_2_Type = Integer32
_EnableHumid_2_Object = MibScalar
enableHumid_2 = _EnableHumid_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 33),
    _EnableHumid_2_Type()
)
enableHumid_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableHumid_2.setStatus("current")
_HumManualDrain_2_Type = Integer32
_HumManualDrain_2_Object = MibScalar
humManualDrain_2 = _HumManualDrain_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 34),
    _HumManualDrain_2_Type()
)
humManualDrain_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humManualDrain_2.setStatus("current")
_HumCylWashing_2_Type = Integer32
_HumCylWashing_2_Object = MibScalar
humCylWashing_2 = _HumCylWashing_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 35),
    _HumCylWashing_2_Type()
)
humCylWashing_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humCylWashing_2.setStatus("current")
_TSManExchange_2_Type = Integer32
_TSManExchange_2_Object = MibScalar
tSManExchange_2 = _TSManExchange_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 36),
    _TSManExchange_2_Type()
)
tSManExchange_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tSManExchange_2.setStatus("current")
_TSTempExchEnab_2_Type = Integer32
_TSTempExchEnab_2_Object = MibScalar
tSTempExchEnab_2 = _TSTempExchEnab_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 37),
    _TSTempExchEnab_2_Type()
)
tSTempExchEnab_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tSTempExchEnab_2.setStatus("current")
_DamperAlRes_2_Type = Integer32
_DamperAlRes_2_Object = MibScalar
damperAlRes_2 = _DamperAlRes_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 38),
    _DamperAlRes_2_Type()
)
damperAlRes_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    damperAlRes_2.setStatus("current")
_FireSmokeAlRes_2_Type = Integer32
_FireSmokeAlRes_2_Object = MibScalar
fireSmokeAlRes_2 = _FireSmokeAlRes_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 39),
    _FireSmokeAlRes_2_Type()
)
fireSmokeAlRes_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fireSmokeAlRes_2.setStatus("current")
_GenSerAlRes_2_Type = Integer32
_GenSerAlRes_2_Object = MibScalar
genSerAlRes_2 = _GenSerAlRes_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 40),
    _GenSerAlRes_2_Type()
)
genSerAlRes_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genSerAlRes_2.setStatus("current")
_FansGenAlRes_2_Type = Integer32
_FansGenAlRes_2_Object = MibScalar
fansGenAlRes_2 = _FansGenAlRes_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 41),
    _FansGenAlRes_2_Type()
)
fansGenAlRes_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fansGenAlRes_2.setStatus("current")
_F1InvAlRes_2_Type = Integer32
_F1InvAlRes_2_Object = MibScalar
f1InvAlRes_2 = _F1InvAlRes_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 42),
    _F1InvAlRes_2_Type()
)
f1InvAlRes_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f1InvAlRes_2.setStatus("current")
_F2InvAlRes_2_Type = Integer32
_F2InvAlRes_2_Object = MibScalar
f2InvAlRes_2 = _F2InvAlRes_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 43),
    _F2InvAlRes_2_Type()
)
f2InvAlRes_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f2InvAlRes_2.setStatus("current")
_F3InvAlRes_2_Type = Integer32
_F3InvAlRes_2_Object = MibScalar
f3InvAlRes_2 = _F3InvAlRes_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 44),
    _F3InvAlRes_2_Type()
)
f3InvAlRes_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3InvAlRes_2.setStatus("current")
_F4InvAlRes_2_Type = Integer32
_F4InvAlRes_2_Object = MibScalar
f4InvAlRes_2 = _F4InvAlRes_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 45),
    _F4InvAlRes_2_Type()
)
f4InvAlRes_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f4InvAlRes_2.setStatus("current")
_F5InvAlRes_2_Type = Integer32
_F5InvAlRes_2_Object = MibScalar
f5InvAlRes_2 = _F5InvAlRes_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 46),
    _F5InvAlRes_2_Type()
)
f5InvAlRes_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f5InvAlRes_2.setStatus("current")
_F6InvAlRes_2_Type = Integer32
_F6InvAlRes_2_Object = MibScalar
f6InvAlRes_2 = _F6InvAlRes_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 47),
    _F6InvAlRes_2_Type()
)
f6InvAlRes_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f6InvAlRes_2.setStatus("current")
_F7InvAlRes_2_Type = Integer32
_F7InvAlRes_2_Object = MibScalar
f7InvAlRes_2 = _F7InvAlRes_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 48),
    _F7InvAlRes_2_Type()
)
f7InvAlRes_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f7InvAlRes_2.setStatus("current")
_F8InvAlRes_2_Type = Integer32
_F8InvAlRes_2_Object = MibScalar
f8InvAlRes_2 = _F8InvAlRes_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 49),
    _F8InvAlRes_2_Type()
)
f8InvAlRes_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f8InvAlRes_2.setStatus("current")
_F9InvAlRes_2_Type = Integer32
_F9InvAlRes_2_Object = MibScalar
f9InvAlRes_2 = _F9InvAlRes_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 50),
    _F9InvAlRes_2_Type()
)
f9InvAlRes_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f9InvAlRes_2.setStatus("current")
_F10InvAlRes_2_Type = Integer32
_F10InvAlRes_2_Object = MibScalar
f10InvAlRes_2 = _F10InvAlRes_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 51),
    _F10InvAlRes_2_Type()
)
f10InvAlRes_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f10InvAlRes_2.setStatus("current")
_InvCompAlRes_2_Type = Integer32
_InvCompAlRes_2_Object = MibScalar
invCompAlRes_2 = _InvCompAlRes_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 52),
    _InvCompAlRes_2_Type()
)
invCompAlRes_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    invCompAlRes_2.setStatus("current")
_C1ThermAlRes_2_Type = Integer32
_C1ThermAlRes_2_Object = MibScalar
c1ThermAlRes_2 = _C1ThermAlRes_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 53),
    _C1ThermAlRes_2_Type()
)
c1ThermAlRes_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c1ThermAlRes_2.setStatus("current")
_C1HighPresAlRes_2_Type = Integer32
_C1HighPresAlRes_2_Object = MibScalar
c1HighPresAlRes_2 = _C1HighPresAlRes_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 54),
    _C1HighPresAlRes_2_Type()
)
c1HighPresAlRes_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c1HighPresAlRes_2.setStatus("current")
_C1LowPresAlRes_2_Type = Integer32
_C1LowPresAlRes_2_Object = MibScalar
c1LowPresAlRes_2 = _C1LowPresAlRes_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 55),
    _C1LowPresAlRes_2_Type()
)
c1LowPresAlRes_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c1LowPresAlRes_2.setStatus("current")
_C1HighDisTAlRes_2_Type = Integer32
_C1HighDisTAlRes_2_Object = MibScalar
c1HighDisTAlRes_2 = _C1HighDisTAlRes_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 56),
    _C1HighDisTAlRes_2_Type()
)
c1HighDisTAlRes_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c1HighDisTAlRes_2.setStatus("current")
_C1LCompRatAlRes_2_Type = Integer32
_C1LCompRatAlRes_2_Object = MibScalar
c1LCompRatAlRes_2 = _C1LCompRatAlRes_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 57),
    _C1LCompRatAlRes_2_Type()
)
c1LCompRatAlRes_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c1LCompRatAlRes_2.setStatus("current")
_Condenser1AlRes_2_Type = Integer32
_Condenser1AlRes_2_Object = MibScalar
condenser1AlRes_2 = _Condenser1AlRes_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 58),
    _Condenser1AlRes_2_Type()
)
condenser1AlRes_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    condenser1AlRes_2.setStatus("current")
_EEV1AlRes_2_Type = Integer32
_EEV1AlRes_2_Object = MibScalar
eEV1AlRes_2 = _EEV1AlRes_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 59),
    _EEV1AlRes_2_Type()
)
eEV1AlRes_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eEV1AlRes_2.setStatus("current")
_C2ThermAlRes_2_Type = Integer32
_C2ThermAlRes_2_Object = MibScalar
c2ThermAlRes_2 = _C2ThermAlRes_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 60),
    _C2ThermAlRes_2_Type()
)
c2ThermAlRes_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c2ThermAlRes_2.setStatus("current")
_C2HighPresAlRes_2_Type = Integer32
_C2HighPresAlRes_2_Object = MibScalar
c2HighPresAlRes_2 = _C2HighPresAlRes_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 61),
    _C2HighPresAlRes_2_Type()
)
c2HighPresAlRes_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c2HighPresAlRes_2.setStatus("current")
_C2LowPresAlRes_2_Type = Integer32
_C2LowPresAlRes_2_Object = MibScalar
c2LowPresAlRes_2 = _C2LowPresAlRes_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 62),
    _C2LowPresAlRes_2_Type()
)
c2LowPresAlRes_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c2LowPresAlRes_2.setStatus("current")
_C2HighDisTAlRes_2_Type = Integer32
_C2HighDisTAlRes_2_Object = MibScalar
c2HighDisTAlRes_2 = _C2HighDisTAlRes_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 63),
    _C2HighDisTAlRes_2_Type()
)
c2HighDisTAlRes_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c2HighDisTAlRes_2.setStatus("current")
_C2LComRatAlRes_2_Type = Integer32
_C2LComRatAlRes_2_Object = MibScalar
c2LComRatAlRes_2 = _C2LComRatAlRes_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 64),
    _C2LComRatAlRes_2_Type()
)
c2LComRatAlRes_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c2LComRatAlRes_2.setStatus("current")
_Condenser2AlRes_2_Type = Integer32
_Condenser2AlRes_2_Object = MibScalar
condenser2AlRes_2 = _Condenser2AlRes_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 65),
    _Condenser2AlRes_2_Type()
)
condenser2AlRes_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    condenser2AlRes_2.setStatus("current")
_EEV2AlRes_2_Type = Integer32
_EEV2AlRes_2_Object = MibScalar
eEV2AlRes_2 = _EEV2AlRes_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 66),
    _EEV2AlRes_2_Type()
)
eEV2AlRes_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eEV2AlRes_2.setStatus("current")
_IntHumidifAlRes_2_Type = Integer32
_IntHumidifAlRes_2_Object = MibScalar
intHumidifAlRes_2 = _IntHumidifAlRes_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 67),
    _IntHumidifAlRes_2_Type()
)
intHumidifAlRes_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intHumidifAlRes_2.setStatus("current")
_WatPresAlRes_2_Type = Integer32
_WatPresAlRes_2_Object = MibScalar
watPresAlRes_2 = _WatPresAlRes_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 68),
    _WatPresAlRes_2_Type()
)
watPresAlRes_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    watPresAlRes_2.setStatus("current")
_DrainPumpAlRes_2_Type = Integer32
_DrainPumpAlRes_2_Object = MibScalar
drainPumpAlRes_2 = _DrainPumpAlRes_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 69),
    _DrainPumpAlRes_2_Type()
)
drainPumpAlRes_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drainPumpAlRes_2.setStatus("current")
_ElHeatAlRes_2_Type = Integer32
_ElHeatAlRes_2_Object = MibScalar
elHeatAlRes_2 = _ElHeatAlRes_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 70),
    _ElHeatAlRes_2_Type()
)
elHeatAlRes_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elHeatAlRes_2.setStatus("current")
_FilterAlRes_2_Type = Integer32
_FilterAlRes_2_Object = MibScalar
filterAlRes_2 = _FilterAlRes_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 71),
    _FilterAlRes_2_Type()
)
filterAlRes_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterAlRes_2.setStatus("current")
_DryCoolerAlRes_2_Type = Integer32
_DryCoolerAlRes_2_Object = MibScalar
dryCoolerAlRes_2 = _DryCoolerAlRes_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 72),
    _DryCoolerAlRes_2_Type()
)
dryCoolerAlRes_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dryCoolerAlRes_2.setStatus("current")
_ExtHumidifAlRes_2_Type = Integer32
_ExtHumidifAlRes_2_Object = MibScalar
extHumidifAlRes_2 = _ExtHumidifAlRes_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 73),
    _ExtHumidifAlRes_2_Type()
)
extHumidifAlRes_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extHumidifAlRes_2.setStatus("current")
_WaterPumpAlRes_2_Type = Integer32
_WaterPumpAlRes_2_Object = MibScalar
waterPumpAlRes_2 = _WaterPumpAlRes_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 74),
    _WaterPumpAlRes_2_Type()
)
waterPumpAlRes_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    waterPumpAlRes_2.setStatus("current")
_CondUnitGAlRes_2_Type = Integer32
_CondUnitGAlRes_2_Object = MibScalar
condUnitGAlRes_2 = _CondUnitGAlRes_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 75),
    _CondUnitGAlRes_2_Type()
)
condUnitGAlRes_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    condUnitGAlRes_2.setStatus("current")
_GasLeakAlRes_2_Type = Integer32
_GasLeakAlRes_2_Object = MibScalar
gasLeakAlRes_2 = _GasLeakAlRes_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 76),
    _GasLeakAlRes_2_Type()
)
gasLeakAlRes_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gasLeakAlRes_2.setStatus("current")
_PowerSupAlRes_2_Type = Integer32
_PowerSupAlRes_2_Object = MibScalar
powerSupAlRes_2 = _PowerSupAlRes_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 77),
    _PowerSupAlRes_2_Type()
)
powerSupAlRes_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerSupAlRes_2.setStatus("current")
_GenSoftAlRes_2_Type = Integer32
_GenSoftAlRes_2_Object = MibScalar
genSoftAlRes_2 = _GenSoftAlRes_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 1, 78),
    _GenSoftAlRes_2_Type()
)
genSoftAlRes_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genSoftAlRes_2.setStatus("current")
_ScalarsObjects2_ObjectIdentity = ObjectIdentity
scalarsObjects2 = _ScalarsObjects2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2)
)
_ConfDI1Combo_2_Type = Integer32
_ConfDI1Combo_2_Object = MibScalar
confDI1Combo_2 = _ConfDI1Combo_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 1),
    _ConfDI1Combo_2_Type()
)
confDI1Combo_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    confDI1Combo_2.setStatus("current")
_ConfDI2Combo_2_Type = Integer32
_ConfDI2Combo_2_Object = MibScalar
confDI2Combo_2 = _ConfDI2Combo_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 2),
    _ConfDI2Combo_2_Type()
)
confDI2Combo_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    confDI2Combo_2.setStatus("current")
_ConfDI3Combo_2_Type = Integer32
_ConfDI3Combo_2_Object = MibScalar
confDI3Combo_2 = _ConfDI3Combo_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 3),
    _ConfDI3Combo_2_Type()
)
confDI3Combo_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    confDI3Combo_2.setStatus("current")
_ConfDI4Combo_2_Type = Integer32
_ConfDI4Combo_2_Object = MibScalar
confDI4Combo_2 = _ConfDI4Combo_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 4),
    _ConfDI4Combo_2_Type()
)
confDI4Combo_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    confDI4Combo_2.setStatus("current")
_ConfDI5Combo_2_Type = Integer32
_ConfDI5Combo_2_Object = MibScalar
confDI5Combo_2 = _ConfDI5Combo_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 5),
    _ConfDI5Combo_2_Type()
)
confDI5Combo_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    confDI5Combo_2.setStatus("current")
_ConfDO1Combo_2_Type = Integer32
_ConfDO1Combo_2_Object = MibScalar
confDO1Combo_2 = _ConfDO1Combo_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 6),
    _ConfDO1Combo_2_Type()
)
confDO1Combo_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    confDO1Combo_2.setStatus("current")
_ConfDO2Combo_2_Type = Integer32
_ConfDO2Combo_2_Object = MibScalar
confDO2Combo_2 = _ConfDO2Combo_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 7),
    _ConfDO2Combo_2_Type()
)
confDO2Combo_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    confDO2Combo_2.setStatus("current")
_ConfDO3Combo_2_Type = Integer32
_ConfDO3Combo_2_Object = MibScalar
confDO3Combo_2 = _ConfDO3Combo_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 8),
    _ConfDO3Combo_2_Type()
)
confDO3Combo_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    confDO3Combo_2.setStatus("current")
_ConfDO4Combo_2_Type = Integer32
_ConfDO4Combo_2_Object = MibScalar
confDO4Combo_2 = _ConfDO4Combo_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 9),
    _ConfDO4Combo_2_Type()
)
confDO4Combo_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    confDO4Combo_2.setStatus("current")
_ConfDO5Combo_2_Type = Integer32
_ConfDO5Combo_2_Object = MibScalar
confDO5Combo_2 = _ConfDO5Combo_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 10),
    _ConfDO5Combo_2_Type()
)
confDO5Combo_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    confDO5Combo_2.setStatus("current")
_ReturnTemp_2_Type = Integer32
_ReturnTemp_2_Object = MibScalar
returnTemp_2 = _ReturnTemp_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 11),
    _ReturnTemp_2_Type()
)
returnTemp_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    returnTemp_2.setStatus("current")
_ReturnTAvg_2_Type = Integer32
_ReturnTAvg_2_Object = MibScalar
returnTAvg_2 = _ReturnTAvg_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 12),
    _ReturnTAvg_2_Type()
)
returnTAvg_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    returnTAvg_2.setStatus("current")
_SupplyTemp_2_Type = Integer32
_SupplyTemp_2_Object = MibScalar
supplyTemp_2 = _SupplyTemp_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 13),
    _SupplyTemp_2_Type()
)
supplyTemp_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supplyTemp_2.setStatus("current")
_SupplyTAvg_2_Type = Integer32
_SupplyTAvg_2_Object = MibScalar
supplyTAvg_2 = _SupplyTAvg_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 14),
    _SupplyTAvg_2_Type()
)
supplyTAvg_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supplyTAvg_2.setStatus("current")
_TempDelta_2_Type = Integer32
_TempDelta_2_Object = MibScalar
tempDelta_2 = _TempDelta_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 15),
    _TempDelta_2_Type()
)
tempDelta_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempDelta_2.setStatus("current")
_ReturnHumidity_2_Type = Integer32
_ReturnHumidity_2_Object = MibScalar
returnHumidity_2 = _ReturnHumidity_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 16),
    _ReturnHumidity_2_Type()
)
returnHumidity_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    returnHumidity_2.setStatus("current")
_ReturnHumAvg_2_Type = Integer32
_ReturnHumAvg_2_Object = MibScalar
returnHumAvg_2 = _ReturnHumAvg_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 17),
    _ReturnHumAvg_2_Type()
)
returnHumAvg_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    returnHumAvg_2.setStatus("current")
_SupplyHumidity_2_Type = Integer32
_SupplyHumidity_2_Object = MibScalar
supplyHumidity_2 = _SupplyHumidity_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 18),
    _SupplyHumidity_2_Type()
)
supplyHumidity_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supplyHumidity_2.setStatus("current")
_SupplyHumAvg_2_Type = Integer32
_SupplyHumAvg_2_Object = MibScalar
supplyHumAvg_2 = _SupplyHumAvg_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 19),
    _SupplyHumAvg_2_Type()
)
supplyHumAvg_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supplyHumAvg_2.setStatus("current")
_AirFlow_2_Type = Integer32
_AirFlow_2_Object = MibScalar
airFlow_2 = _AirFlow_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 20),
    _AirFlow_2_Type()
)
airFlow_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airFlow_2.setStatus("current")
_AirPressure_2_Type = Integer32
_AirPressure_2_Object = MibScalar
airPressure_2 = _AirPressure_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 22),
    _AirPressure_2_Type()
)
airPressure_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airPressure_2.setStatus("current")
_AirPressureAvg_2_Type = Integer32
_AirPressureAvg_2_Object = MibScalar
airPressureAvg_2 = _AirPressureAvg_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 23),
    _AirPressureAvg_2_Type()
)
airPressureAvg_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airPressureAvg_2.setStatus("current")
_NetMod1Combo1_2_Type = Integer32
_NetMod1Combo1_2_Object = MibScalar
netMod1Combo1_2 = _NetMod1Combo1_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 24),
    _NetMod1Combo1_2_Type()
)
netMod1Combo1_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod1Combo1_2.setStatus("current")
_NetMod1Probe1_2_Type = Integer32
_NetMod1Probe1_2_Object = MibScalar
netMod1Probe1_2 = _NetMod1Probe1_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 25),
    _NetMod1Probe1_2_Type()
)
netMod1Probe1_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod1Probe1_2.setStatus("current")
_NetMod1Combo2_2_Type = Integer32
_NetMod1Combo2_2_Object = MibScalar
netMod1Combo2_2 = _NetMod1Combo2_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 26),
    _NetMod1Combo2_2_Type()
)
netMod1Combo2_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod1Combo2_2.setStatus("current")
_NetMod1Probe2_2_Type = Integer32
_NetMod1Probe2_2_Object = MibScalar
netMod1Probe2_2 = _NetMod1Probe2_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 27),
    _NetMod1Probe2_2_Type()
)
netMod1Probe2_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod1Probe2_2.setStatus("current")
_NetMod1Combo3_2_Type = Integer32
_NetMod1Combo3_2_Object = MibScalar
netMod1Combo3_2 = _NetMod1Combo3_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 28),
    _NetMod1Combo3_2_Type()
)
netMod1Combo3_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod1Combo3_2.setStatus("current")
_NetMod1Probe3_2_Type = Integer32
_NetMod1Probe3_2_Object = MibScalar
netMod1Probe3_2 = _NetMod1Probe3_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 29),
    _NetMod1Probe3_2_Type()
)
netMod1Probe3_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod1Probe3_2.setStatus("current")
_NetMod1Combo4_2_Type = Integer32
_NetMod1Combo4_2_Object = MibScalar
netMod1Combo4_2 = _NetMod1Combo4_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 30),
    _NetMod1Combo4_2_Type()
)
netMod1Combo4_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod1Combo4_2.setStatus("current")
_NetMod1Probe4_2_Type = Integer32
_NetMod1Probe4_2_Object = MibScalar
netMod1Probe4_2 = _NetMod1Probe4_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 31),
    _NetMod1Probe4_2_Type()
)
netMod1Probe4_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod1Probe4_2.setStatus("current")
_NetMod1Combo5_2_Type = Integer32
_NetMod1Combo5_2_Object = MibScalar
netMod1Combo5_2 = _NetMod1Combo5_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 32),
    _NetMod1Combo5_2_Type()
)
netMod1Combo5_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod1Combo5_2.setStatus("current")
_NetMod1Probe5_2_Type = Integer32
_NetMod1Probe5_2_Object = MibScalar
netMod1Probe5_2 = _NetMod1Probe5_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 33),
    _NetMod1Probe5_2_Type()
)
netMod1Probe5_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod1Probe5_2.setStatus("current")
_NetMod1Combo6_2_Type = Integer32
_NetMod1Combo6_2_Object = MibScalar
netMod1Combo6_2 = _NetMod1Combo6_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 34),
    _NetMod1Combo6_2_Type()
)
netMod1Combo6_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod1Combo6_2.setStatus("current")
_NetMod1Probe6_2_Type = Integer32
_NetMod1Probe6_2_Object = MibScalar
netMod1Probe6_2 = _NetMod1Probe6_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 35),
    _NetMod1Probe6_2_Type()
)
netMod1Probe6_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod1Probe6_2.setStatus("current")
_NetMod2Combo1_2_Type = Integer32
_NetMod2Combo1_2_Object = MibScalar
netMod2Combo1_2 = _NetMod2Combo1_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 36),
    _NetMod2Combo1_2_Type()
)
netMod2Combo1_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod2Combo1_2.setStatus("current")
_NetMod2Probe1_2_Type = Integer32
_NetMod2Probe1_2_Object = MibScalar
netMod2Probe1_2 = _NetMod2Probe1_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 37),
    _NetMod2Probe1_2_Type()
)
netMod2Probe1_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod2Probe1_2.setStatus("current")
_NetMod2Combo2_2_Type = Integer32
_NetMod2Combo2_2_Object = MibScalar
netMod2Combo2_2 = _NetMod2Combo2_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 38),
    _NetMod2Combo2_2_Type()
)
netMod2Combo2_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod2Combo2_2.setStatus("current")
_NetMod2Probe2_2_Type = Integer32
_NetMod2Probe2_2_Object = MibScalar
netMod2Probe2_2 = _NetMod2Probe2_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 39),
    _NetMod2Probe2_2_Type()
)
netMod2Probe2_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod2Probe2_2.setStatus("current")
_NetMod2Combo3_2_Type = Integer32
_NetMod2Combo3_2_Object = MibScalar
netMod2Combo3_2 = _NetMod2Combo3_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 40),
    _NetMod2Combo3_2_Type()
)
netMod2Combo3_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod2Combo3_2.setStatus("current")
_NetMod2Probe3_2_Type = Integer32
_NetMod2Probe3_2_Object = MibScalar
netMod2Probe3_2 = _NetMod2Probe3_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 41),
    _NetMod2Probe3_2_Type()
)
netMod2Probe3_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod2Probe3_2.setStatus("current")
_NetMod2Combo4_2_Type = Integer32
_NetMod2Combo4_2_Object = MibScalar
netMod2Combo4_2 = _NetMod2Combo4_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 42),
    _NetMod2Combo4_2_Type()
)
netMod2Combo4_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod2Combo4_2.setStatus("current")
_NetMod2Probe4_2_Type = Integer32
_NetMod2Probe4_2_Object = MibScalar
netMod2Probe4_2 = _NetMod2Probe4_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 43),
    _NetMod2Probe4_2_Type()
)
netMod2Probe4_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod2Probe4_2.setStatus("current")
_NetMod2Combo5_2_Type = Integer32
_NetMod2Combo5_2_Object = MibScalar
netMod2Combo5_2 = _NetMod2Combo5_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 44),
    _NetMod2Combo5_2_Type()
)
netMod2Combo5_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod2Combo5_2.setStatus("current")
_NetMod2Probe5_2_Type = Integer32
_NetMod2Probe5_2_Object = MibScalar
netMod2Probe5_2 = _NetMod2Probe5_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 45),
    _NetMod2Probe5_2_Type()
)
netMod2Probe5_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod2Probe5_2.setStatus("current")
_NetMod2Combo6_2_Type = Integer32
_NetMod2Combo6_2_Object = MibScalar
netMod2Combo6_2 = _NetMod2Combo6_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 46),
    _NetMod2Combo6_2_Type()
)
netMod2Combo6_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod2Combo6_2.setStatus("current")
_NetMod2Probe6_2_Type = Integer32
_NetMod2Probe6_2_Object = MibScalar
netMod2Probe6_2 = _NetMod2Probe6_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 47),
    _NetMod2Probe6_2_Type()
)
netMod2Probe6_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod2Probe6_2.setStatus("current")
_NetMod3Combo1_2_Type = Integer32
_NetMod3Combo1_2_Object = MibScalar
netMod3Combo1_2 = _NetMod3Combo1_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 48),
    _NetMod3Combo1_2_Type()
)
netMod3Combo1_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod3Combo1_2.setStatus("current")
_NetMod3Probe1_2_Type = Integer32
_NetMod3Probe1_2_Object = MibScalar
netMod3Probe1_2 = _NetMod3Probe1_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 49),
    _NetMod3Probe1_2_Type()
)
netMod3Probe1_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod3Probe1_2.setStatus("current")
_NetMod3Combo2_2_Type = Integer32
_NetMod3Combo2_2_Object = MibScalar
netMod3Combo2_2 = _NetMod3Combo2_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 50),
    _NetMod3Combo2_2_Type()
)
netMod3Combo2_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod3Combo2_2.setStatus("current")
_NetMod3Probe2_2_Type = Integer32
_NetMod3Probe2_2_Object = MibScalar
netMod3Probe2_2 = _NetMod3Probe2_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 51),
    _NetMod3Probe2_2_Type()
)
netMod3Probe2_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod3Probe2_2.setStatus("current")
_NetMod3Combo3_2_Type = Integer32
_NetMod3Combo3_2_Object = MibScalar
netMod3Combo3_2 = _NetMod3Combo3_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 52),
    _NetMod3Combo3_2_Type()
)
netMod3Combo3_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod3Combo3_2.setStatus("current")
_NetMod3Probe3_2_Type = Integer32
_NetMod3Probe3_2_Object = MibScalar
netMod3Probe3_2 = _NetMod3Probe3_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 53),
    _NetMod3Probe3_2_Type()
)
netMod3Probe3_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod3Probe3_2.setStatus("current")
_NetMod3Combo4_2_Type = Integer32
_NetMod3Combo4_2_Object = MibScalar
netMod3Combo4_2 = _NetMod3Combo4_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 54),
    _NetMod3Combo4_2_Type()
)
netMod3Combo4_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod3Combo4_2.setStatus("current")
_NetMod3Probe4_2_Type = Integer32
_NetMod3Probe4_2_Object = MibScalar
netMod3Probe4_2 = _NetMod3Probe4_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 55),
    _NetMod3Probe4_2_Type()
)
netMod3Probe4_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod3Probe4_2.setStatus("current")
_NetMod3Combo5_2_Type = Integer32
_NetMod3Combo5_2_Object = MibScalar
netMod3Combo5_2 = _NetMod3Combo5_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 56),
    _NetMod3Combo5_2_Type()
)
netMod3Combo5_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod3Combo5_2.setStatus("current")
_NetMod3Probe5_2_Type = Integer32
_NetMod3Probe5_2_Object = MibScalar
netMod3Probe5_2 = _NetMod3Probe5_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 57),
    _NetMod3Probe5_2_Type()
)
netMod3Probe5_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod3Probe5_2.setStatus("current")
_NetMod3Combo6_2_Type = Integer32
_NetMod3Combo6_2_Object = MibScalar
netMod3Combo6_2 = _NetMod3Combo6_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 58),
    _NetMod3Combo6_2_Type()
)
netMod3Combo6_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod3Combo6_2.setStatus("current")
_NetMod3Probe6_2_Type = Integer32
_NetMod3Probe6_2_Object = MibScalar
netMod3Probe6_2 = _NetMod3Probe6_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 59),
    _NetMod3Probe6_2_Type()
)
netMod3Probe6_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMod3Probe6_2.setStatus("current")
_AvgModTemp_2_Type = Integer32
_AvgModTemp_2_Object = MibScalar
avgModTemp_2 = _AvgModTemp_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 60),
    _AvgModTemp_2_Type()
)
avgModTemp_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avgModTemp_2.setStatus("current")
_AvgModHumi_2_Type = Integer32
_AvgModHumi_2_Object = MibScalar
avgModHumi_2 = _AvgModHumi_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 61),
    _AvgModHumi_2_Type()
)
avgModHumi_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avgModHumi_2.setStatus("current")
_AvgModPress_2_Type = Integer32
_AvgModPress_2_Object = MibScalar
avgModPress_2 = _AvgModPress_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 62),
    _AvgModPress_2_Type()
)
avgModPress_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avgModPress_2.setStatus("current")
_DryCoolerAO_2_Type = Integer32
_DryCoolerAO_2_Object = MibScalar
dryCoolerAO_2 = _DryCoolerAO_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 63),
    _DryCoolerAO_2_Type()
)
dryCoolerAO_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dryCoolerAO_2.setStatus("current")
_CoolingAO_2_Type = Integer32
_CoolingAO_2_Object = MibScalar
coolingAO_2 = _CoolingAO_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 64),
    _CoolingAO_2_Type()
)
coolingAO_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingAO_2.setStatus("current")
_HeatingAO_2_Type = Integer32
_HeatingAO_2_Object = MibScalar
heatingAO_2 = _HeatingAO_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 65),
    _HeatingAO_2_Type()
)
heatingAO_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heatingAO_2.setStatus("current")
_TwoSources2AO_2_Type = Integer32
_TwoSources2AO_2_Object = MibScalar
twoSources2AO_2 = _TwoSources2AO_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 66),
    _TwoSources2AO_2_Type()
)
twoSources2AO_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twoSources2AO_2.setStatus("current")
_Condenser1AO_2_Type = Integer32
_Condenser1AO_2_Object = MibScalar
condenser1AO_2 = _Condenser1AO_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 67),
    _Condenser1AO_2_Type()
)
condenser1AO_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    condenser1AO_2.setStatus("current")
_Cond2HumidifAO_2_Type = Integer32
_Cond2HumidifAO_2_Object = MibScalar
cond2HumidifAO_2 = _Cond2HumidifAO_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 68),
    _Cond2HumidifAO_2_Type()
)
cond2HumidifAO_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cond2HumidifAO_2.setStatus("current")
_UnitStatus_2_Type = Integer32
_UnitStatus_2_Object = MibScalar
unitStatus_2 = _UnitStatus_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 69),
    _UnitStatus_2_Type()
)
unitStatus_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitStatus_2.setStatus("current")
_FanSpeed_2_Type = Integer32
_FanSpeed_2_Object = MibScalar
fanSpeed_2 = _FanSpeed_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 70),
    _FanSpeed_2_Type()
)
fanSpeed_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanSpeed_2.setStatus("current")
_Fan1Actspeed_2_Type = Integer32
_Fan1Actspeed_2_Object = MibScalar
fan1Actspeed_2 = _Fan1Actspeed_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 71),
    _Fan1Actspeed_2_Type()
)
fan1Actspeed_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan1Actspeed_2.setStatus("current")
_Fan1ActRPM_2_Type = Integer32
_Fan1ActRPM_2_Object = MibScalar
fan1ActRPM_2 = _Fan1ActRPM_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 72),
    _Fan1ActRPM_2_Type()
)
fan1ActRPM_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan1ActRPM_2.setStatus("current")
_Fan1Cur_2_Type = Integer32
_Fan1Cur_2_Object = MibScalar
fan1Cur_2 = _Fan1Cur_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 73),
    _Fan1Cur_2_Type()
)
fan1Cur_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan1Cur_2.setStatus("current")
_Fan1Power_2_Type = Integer32
_Fan1Power_2_Object = MibScalar
fan1Power_2 = _Fan1Power_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 74),
    _Fan1Power_2_Type()
)
fan1Power_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan1Power_2.setStatus("current")
_Fan2Actspeed_2_Type = Integer32
_Fan2Actspeed_2_Object = MibScalar
fan2Actspeed_2 = _Fan2Actspeed_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 75),
    _Fan2Actspeed_2_Type()
)
fan2Actspeed_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan2Actspeed_2.setStatus("current")
_Fan2ActRPM_2_Type = Integer32
_Fan2ActRPM_2_Object = MibScalar
fan2ActRPM_2 = _Fan2ActRPM_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 76),
    _Fan2ActRPM_2_Type()
)
fan2ActRPM_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan2ActRPM_2.setStatus("current")
_Fan2Cur_2_Type = Integer32
_Fan2Cur_2_Object = MibScalar
fan2Cur_2 = _Fan2Cur_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 77),
    _Fan2Cur_2_Type()
)
fan2Cur_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan2Cur_2.setStatus("current")
_Fan2Power_2_Type = Integer32
_Fan2Power_2_Object = MibScalar
fan2Power_2 = _Fan2Power_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 78),
    _Fan2Power_2_Type()
)
fan2Power_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan2Power_2.setStatus("current")
_Fan3Actspeed_2_Type = Integer32
_Fan3Actspeed_2_Object = MibScalar
fan3Actspeed_2 = _Fan3Actspeed_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 79),
    _Fan3Actspeed_2_Type()
)
fan3Actspeed_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan3Actspeed_2.setStatus("current")
_Fan3ActRPM_2_Type = Integer32
_Fan3ActRPM_2_Object = MibScalar
fan3ActRPM_2 = _Fan3ActRPM_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 80),
    _Fan3ActRPM_2_Type()
)
fan3ActRPM_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan3ActRPM_2.setStatus("current")
_Fan3Cur_2_Type = Integer32
_Fan3Cur_2_Object = MibScalar
fan3Cur_2 = _Fan3Cur_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 81),
    _Fan3Cur_2_Type()
)
fan3Cur_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan3Cur_2.setStatus("current")
_Fan3Power_2_Type = Integer32
_Fan3Power_2_Object = MibScalar
fan3Power_2 = _Fan3Power_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 82),
    _Fan3Power_2_Type()
)
fan3Power_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan3Power_2.setStatus("current")
_Fan4Actspeed_2_Type = Integer32
_Fan4Actspeed_2_Object = MibScalar
fan4Actspeed_2 = _Fan4Actspeed_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 83),
    _Fan4Actspeed_2_Type()
)
fan4Actspeed_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan4Actspeed_2.setStatus("current")
_Fan4ActRPM_2_Type = Integer32
_Fan4ActRPM_2_Object = MibScalar
fan4ActRPM_2 = _Fan4ActRPM_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 84),
    _Fan4ActRPM_2_Type()
)
fan4ActRPM_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan4ActRPM_2.setStatus("current")
_Fan4Cur_2_Type = Integer32
_Fan4Cur_2_Object = MibScalar
fan4Cur_2 = _Fan4Cur_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 85),
    _Fan4Cur_2_Type()
)
fan4Cur_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan4Cur_2.setStatus("current")
_Fan4Power_2_Type = Integer32
_Fan4Power_2_Object = MibScalar
fan4Power_2 = _Fan4Power_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 86),
    _Fan4Power_2_Type()
)
fan4Power_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan4Power_2.setStatus("current")
_Fan5Actspeed_2_Type = Integer32
_Fan5Actspeed_2_Object = MibScalar
fan5Actspeed_2 = _Fan5Actspeed_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 87),
    _Fan5Actspeed_2_Type()
)
fan5Actspeed_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan5Actspeed_2.setStatus("current")
_Fan5ActRPM_2_Type = Integer32
_Fan5ActRPM_2_Object = MibScalar
fan5ActRPM_2 = _Fan5ActRPM_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 88),
    _Fan5ActRPM_2_Type()
)
fan5ActRPM_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan5ActRPM_2.setStatus("current")
_Fan5Cur_2_Type = Integer32
_Fan5Cur_2_Object = MibScalar
fan5Cur_2 = _Fan5Cur_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 89),
    _Fan5Cur_2_Type()
)
fan5Cur_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan5Cur_2.setStatus("current")
_Fan5Power_2_Type = Integer32
_Fan5Power_2_Object = MibScalar
fan5Power_2 = _Fan5Power_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 90),
    _Fan5Power_2_Type()
)
fan5Power_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan5Power_2.setStatus("current")
_Fan6Actspeed_2_Type = Integer32
_Fan6Actspeed_2_Object = MibScalar
fan6Actspeed_2 = _Fan6Actspeed_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 91),
    _Fan6Actspeed_2_Type()
)
fan6Actspeed_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan6Actspeed_2.setStatus("current")
_Fan6ActRPM_2_Type = Integer32
_Fan6ActRPM_2_Object = MibScalar
fan6ActRPM_2 = _Fan6ActRPM_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 92),
    _Fan6ActRPM_2_Type()
)
fan6ActRPM_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan6ActRPM_2.setStatus("current")
_Fan6Cur_2_Type = Integer32
_Fan6Cur_2_Object = MibScalar
fan6Cur_2 = _Fan6Cur_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 93),
    _Fan6Cur_2_Type()
)
fan6Cur_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan6Cur_2.setStatus("current")
_Fan6Power_2_Type = Integer32
_Fan6Power_2_Object = MibScalar
fan6Power_2 = _Fan6Power_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 94),
    _Fan6Power_2_Type()
)
fan6Power_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan6Power_2.setStatus("current")
_Fan7Actspeed_2_Type = Integer32
_Fan7Actspeed_2_Object = MibScalar
fan7Actspeed_2 = _Fan7Actspeed_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 95),
    _Fan7Actspeed_2_Type()
)
fan7Actspeed_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan7Actspeed_2.setStatus("current")
_Fan7ActRPM_2_Type = Integer32
_Fan7ActRPM_2_Object = MibScalar
fan7ActRPM_2 = _Fan7ActRPM_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 96),
    _Fan7ActRPM_2_Type()
)
fan7ActRPM_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan7ActRPM_2.setStatus("current")
_Fan7Cur_2_Type = Integer32
_Fan7Cur_2_Object = MibScalar
fan7Cur_2 = _Fan7Cur_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 97),
    _Fan7Cur_2_Type()
)
fan7Cur_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan7Cur_2.setStatus("current")
_Fan7Power_2_Type = Integer32
_Fan7Power_2_Object = MibScalar
fan7Power_2 = _Fan7Power_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 98),
    _Fan7Power_2_Type()
)
fan7Power_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan7Power_2.setStatus("current")
_Fan8Actspeed_2_Type = Integer32
_Fan8Actspeed_2_Object = MibScalar
fan8Actspeed_2 = _Fan8Actspeed_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 99),
    _Fan8Actspeed_2_Type()
)
fan8Actspeed_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan8Actspeed_2.setStatus("current")
_Fan8ActRPM_2_Type = Integer32
_Fan8ActRPM_2_Object = MibScalar
fan8ActRPM_2 = _Fan8ActRPM_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 100),
    _Fan8ActRPM_2_Type()
)
fan8ActRPM_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan8ActRPM_2.setStatus("current")
_Fan8Cur_2_Type = Integer32
_Fan8Cur_2_Object = MibScalar
fan8Cur_2 = _Fan8Cur_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 101),
    _Fan8Cur_2_Type()
)
fan8Cur_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan8Cur_2.setStatus("current")
_Fan8Power_2_Type = Integer32
_Fan8Power_2_Object = MibScalar
fan8Power_2 = _Fan8Power_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 102),
    _Fan8Power_2_Type()
)
fan8Power_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan8Power_2.setStatus("current")
_Fan9Actspeed_2_Type = Integer32
_Fan9Actspeed_2_Object = MibScalar
fan9Actspeed_2 = _Fan9Actspeed_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 103),
    _Fan9Actspeed_2_Type()
)
fan9Actspeed_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan9Actspeed_2.setStatus("current")
_Fan9ActRPM_2_Type = Integer32
_Fan9ActRPM_2_Object = MibScalar
fan9ActRPM_2 = _Fan9ActRPM_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 104),
    _Fan9ActRPM_2_Type()
)
fan9ActRPM_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan9ActRPM_2.setStatus("current")
_Fan9Cur_2_Type = Integer32
_Fan9Cur_2_Object = MibScalar
fan9Cur_2 = _Fan9Cur_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 105),
    _Fan9Cur_2_Type()
)
fan9Cur_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan9Cur_2.setStatus("current")
_Fan9Power_2_Type = Integer32
_Fan9Power_2_Object = MibScalar
fan9Power_2 = _Fan9Power_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 106),
    _Fan9Power_2_Type()
)
fan9Power_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan9Power_2.setStatus("current")
_Fan10Actspeed_2_Type = Integer32
_Fan10Actspeed_2_Object = MibScalar
fan10Actspeed_2 = _Fan10Actspeed_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 107),
    _Fan10Actspeed_2_Type()
)
fan10Actspeed_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan10Actspeed_2.setStatus("current")
_Fan10ActRPM_2_Type = Integer32
_Fan10ActRPM_2_Object = MibScalar
fan10ActRPM_2 = _Fan10ActRPM_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 108),
    _Fan10ActRPM_2_Type()
)
fan10ActRPM_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan10ActRPM_2.setStatus("current")
_Fan10Cur_2_Type = Integer32
_Fan10Cur_2_Object = MibScalar
fan10Cur_2 = _Fan10Cur_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 109),
    _Fan10Cur_2_Type()
)
fan10Cur_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan10Cur_2.setStatus("current")
_Fan10Power_2_Type = Integer32
_Fan10Power_2_Object = MibScalar
fan10Power_2 = _Fan10Power_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 110),
    _Fan10Power_2_Type()
)
fan10Power_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan10Power_2.setStatus("current")
_DiffFilterPres_2_Type = Integer32
_DiffFilterPres_2_Object = MibScalar
diffFilterPres_2 = _DiffFilterPres_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 111),
    _DiffFilterPres_2_Type()
)
diffFilterPres_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffFilterPres_2.setStatus("current")
_CoolingRequest_2_Type = Integer32
_CoolingRequest_2_Object = MibScalar
coolingRequest_2 = _CoolingRequest_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 112),
    _CoolingRequest_2_Type()
)
coolingRequest_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingRequest_2.setStatus("current")
_HeatingRequest_2_Type = Integer32
_HeatingRequest_2_Object = MibScalar
heatingRequest_2 = _HeatingRequest_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 113),
    _HeatingRequest_2_Type()
)
heatingRequest_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heatingRequest_2.setStatus("current")
_DehumidRequest_2_Type = Integer32
_DehumidRequest_2_Object = MibScalar
dehumidRequest_2 = _DehumidRequest_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 114),
    _DehumidRequest_2_Type()
)
dehumidRequest_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dehumidRequest_2.setStatus("current")
_HumidifRequest_2_Type = Integer32
_HumidifRequest_2_Object = MibScalar
humidifRequest_2 = _HumidifRequest_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 115),
    _HumidifRequest_2_Type()
)
humidifRequest_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidifRequest_2.setStatus("current")
_TempFcTs_2_Type = Integer32
_TempFcTs_2_Object = MibScalar
tempFcTs_2 = _TempFcTs_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 116),
    _TempFcTs_2_Type()
)
tempFcTs_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempFcTs_2.setStatus("current")
_FCTSStatus_2_Type = Integer32
_FCTSStatus_2_Object = MibScalar
fCTSStatus_2 = _FCTSStatus_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 117),
    _FCTSStatus_2_Type()
)
fCTSStatus_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fCTSStatus_2.setStatus("current")
_FCRequest_2_Type = Integer32
_FCRequest_2_Object = MibScalar
fCRequest_2 = _FCRequest_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 118),
    _FCRequest_2_Type()
)
fCRequest_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fCRequest_2.setStatus("current")
_ActiveComp_2_Type = Integer32
_ActiveComp_2_Object = MibScalar
activeComp_2 = _ActiveComp_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 119),
    _ActiveComp_2_Type()
)
activeComp_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeComp_2.setStatus("current")
_Comp1Sts_2_Type = Integer32
_Comp1Sts_2_Object = MibScalar
comp1Sts_2 = _Comp1Sts_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 120),
    _Comp1Sts_2_Type()
)
comp1Sts_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comp1Sts_2.setStatus("current")
_Comp2Sts_2_Type = Integer32
_Comp2Sts_2_Object = MibScalar
comp2Sts_2 = _Comp2Sts_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 121),
    _Comp2Sts_2_Type()
)
comp2Sts_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comp2Sts_2.setStatus("current")
_InvComprReq_2_Type = Integer32
_InvComprReq_2_Object = MibScalar
invComprReq_2 = _InvComprReq_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 122),
    _InvComprReq_2_Type()
)
invComprReq_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invComprReq_2.setStatus("current")
_InvCompHz_2_Type = Integer32
_InvCompHz_2_Object = MibScalar
invCompHz_2 = _InvCompHz_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 123),
    _InvCompHz_2_Type()
)
invCompHz_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invCompHz_2.setStatus("current")
_InvCompPower_2_Type = Integer32
_InvCompPower_2_Object = MibScalar
invCompPower_2 = _InvCompPower_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 124),
    _InvCompPower_2_Type()
)
invCompPower_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invCompPower_2.setStatus("current")
_InvCompCurrent_2_Type = Integer32
_InvCompCurrent_2_Object = MibScalar
invCompCurrent_2 = _InvCompCurrent_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 125),
    _InvCompCurrent_2_Type()
)
invCompCurrent_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invCompCurrent_2.setStatus("current")
_C1EvapPres_2_Type = Integer32
_C1EvapPres_2_Object = MibScalar
c1EvapPres_2 = _C1EvapPres_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 126),
    _C1EvapPres_2_Type()
)
c1EvapPres_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c1EvapPres_2.setStatus("current")
_C1EvapTemp_2_Type = Integer32
_C1EvapTemp_2_Object = MibScalar
c1EvapTemp_2 = _C1EvapTemp_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 127),
    _C1EvapTemp_2_Type()
)
c1EvapTemp_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c1EvapTemp_2.setStatus("current")
_C1SuctionTemp_2_Type = Integer32
_C1SuctionTemp_2_Object = MibScalar
c1SuctionTemp_2 = _C1SuctionTemp_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 128),
    _C1SuctionTemp_2_Type()
)
c1SuctionTemp_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c1SuctionTemp_2.setStatus("current")
_C1Superheat_2_Type = Integer32
_C1Superheat_2_Object = MibScalar
c1Superheat_2 = _C1Superheat_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 129),
    _C1Superheat_2_Type()
)
c1Superheat_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c1Superheat_2.setStatus("current")
_C1CompRatio_2_Type = Integer32
_C1CompRatio_2_Object = MibScalar
c1CompRatio_2 = _C1CompRatio_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 130),
    _C1CompRatio_2_Type()
)
c1CompRatio_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c1CompRatio_2.setStatus("current")
_C1DischTemp_2_Type = Integer32
_C1DischTemp_2_Object = MibScalar
c1DischTemp_2 = _C1DischTemp_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 131),
    _C1DischTemp_2_Type()
)
c1DischTemp_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c1DischTemp_2.setStatus("current")
_C1CondPress_2_Type = Integer32
_C1CondPress_2_Object = MibScalar
c1CondPress_2 = _C1CondPress_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 132),
    _C1CondPress_2_Type()
)
c1CondPress_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c1CondPress_2.setStatus("current")
_C1CondTemp_2_Type = Integer32
_C1CondTemp_2_Object = MibScalar
c1CondTemp_2 = _C1CondTemp_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 133),
    _C1CondTemp_2_Type()
)
c1CondTemp_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c1CondTemp_2.setStatus("current")
_C1Desuperheat_2_Type = Integer32
_C1Desuperheat_2_Object = MibScalar
c1Desuperheat_2 = _C1Desuperheat_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 134),
    _C1Desuperheat_2_Type()
)
c1Desuperheat_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c1Desuperheat_2.setStatus("current")
_C1LiquidTemp_2_Type = Integer32
_C1LiquidTemp_2_Object = MibScalar
c1LiquidTemp_2 = _C1LiquidTemp_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 135),
    _C1LiquidTemp_2_Type()
)
c1LiquidTemp_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c1LiquidTemp_2.setStatus("current")
_C1Subcooling_2_Type = Integer32
_C1Subcooling_2_Object = MibScalar
c1Subcooling_2 = _C1Subcooling_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 136),
    _C1Subcooling_2_Type()
)
c1Subcooling_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c1Subcooling_2.setStatus("current")
_EEV1SHSet_2_Type = Integer32
_EEV1SHSet_2_Object = MibScalar
eEV1SHSet_2 = _EEV1SHSet_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 137),
    _EEV1SHSet_2_Type()
)
eEV1SHSet_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eEV1SHSet_2.setStatus("current")
_EEV1Position_2_Type = Integer32
_EEV1Position_2_Object = MibScalar
eEV1Position_2 = _EEV1Position_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 138),
    _EEV1Position_2_Type()
)
eEV1Position_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eEV1Position_2.setStatus("current")
_EEV1Status_2_Type = Integer32
_EEV1Status_2_Object = MibScalar
eEV1Status_2 = _EEV1Status_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 139),
    _EEV1Status_2_Type()
)
eEV1Status_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eEV1Status_2.setStatus("current")
_Cond1ActualSet_2_Type = Integer32
_Cond1ActualSet_2_Object = MibScalar
cond1ActualSet_2 = _Cond1ActualSet_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 140),
    _Cond1ActualSet_2_Type()
)
cond1ActualSet_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cond1ActualSet_2.setStatus("current")
_Cond1Req_2_Type = Integer32
_Cond1Req_2_Object = MibScalar
cond1Req_2 = _Cond1Req_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 141),
    _Cond1Req_2_Type()
)
cond1Req_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cond1Req_2.setStatus("current")
_C2EvapPres_2_Type = Integer32
_C2EvapPres_2_Object = MibScalar
c2EvapPres_2 = _C2EvapPres_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 142),
    _C2EvapPres_2_Type()
)
c2EvapPres_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2EvapPres_2.setStatus("current")
_C2EvapTemp_2_Type = Integer32
_C2EvapTemp_2_Object = MibScalar
c2EvapTemp_2 = _C2EvapTemp_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 143),
    _C2EvapTemp_2_Type()
)
c2EvapTemp_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2EvapTemp_2.setStatus("current")
_C2SuctionTemp_2_Type = Integer32
_C2SuctionTemp_2_Object = MibScalar
c2SuctionTemp_2 = _C2SuctionTemp_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 144),
    _C2SuctionTemp_2_Type()
)
c2SuctionTemp_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2SuctionTemp_2.setStatus("current")
_C2Superheat_2_Type = Integer32
_C2Superheat_2_Object = MibScalar
c2Superheat_2 = _C2Superheat_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 145),
    _C2Superheat_2_Type()
)
c2Superheat_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2Superheat_2.setStatus("current")
_C2CompRatio_2_Type = Integer32
_C2CompRatio_2_Object = MibScalar
c2CompRatio_2 = _C2CompRatio_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 146),
    _C2CompRatio_2_Type()
)
c2CompRatio_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2CompRatio_2.setStatus("current")
_C2DischTemp_2_Type = Integer32
_C2DischTemp_2_Object = MibScalar
c2DischTemp_2 = _C2DischTemp_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 147),
    _C2DischTemp_2_Type()
)
c2DischTemp_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2DischTemp_2.setStatus("current")
_C2CondPress_2_Type = Integer32
_C2CondPress_2_Object = MibScalar
c2CondPress_2 = _C2CondPress_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 148),
    _C2CondPress_2_Type()
)
c2CondPress_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2CondPress_2.setStatus("current")
_C2CondTemp_2_Type = Integer32
_C2CondTemp_2_Object = MibScalar
c2CondTemp_2 = _C2CondTemp_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 149),
    _C2CondTemp_2_Type()
)
c2CondTemp_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2CondTemp_2.setStatus("current")
_C2Desuperheat_2_Type = Integer32
_C2Desuperheat_2_Object = MibScalar
c2Desuperheat_2 = _C2Desuperheat_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 150),
    _C2Desuperheat_2_Type()
)
c2Desuperheat_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2Desuperheat_2.setStatus("current")
_C2LiquidTemp_2_Type = Integer32
_C2LiquidTemp_2_Object = MibScalar
c2LiquidTemp_2 = _C2LiquidTemp_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 151),
    _C2LiquidTemp_2_Type()
)
c2LiquidTemp_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2LiquidTemp_2.setStatus("current")
_C2Subcooling_2_Type = Integer32
_C2Subcooling_2_Object = MibScalar
c2Subcooling_2 = _C2Subcooling_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 152),
    _C2Subcooling_2_Type()
)
c2Subcooling_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2Subcooling_2.setStatus("current")
_EEV2SHSet_2_Type = Integer32
_EEV2SHSet_2_Object = MibScalar
eEV2SHSet_2 = _EEV2SHSet_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 153),
    _EEV2SHSet_2_Type()
)
eEV2SHSet_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eEV2SHSet_2.setStatus("current")
_EEV2Position_2_Type = Integer32
_EEV2Position_2_Object = MibScalar
eEV2Position_2 = _EEV2Position_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 154),
    _EEV2Position_2_Type()
)
eEV2Position_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eEV2Position_2.setStatus("current")
_EEV2Status_2_Type = Integer32
_EEV2Status_2_Object = MibScalar
eEV2Status_2 = _EEV2Status_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 155),
    _EEV2Status_2_Type()
)
eEV2Status_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eEV2Status_2.setStatus("current")
_Cond2ActualSet_2_Type = Integer32
_Cond2ActualSet_2_Object = MibScalar
cond2ActualSet_2 = _Cond2ActualSet_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 156),
    _Cond2ActualSet_2_Type()
)
cond2ActualSet_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cond2ActualSet_2.setStatus("current")
_Cond2Req_2_Type = Integer32
_Cond2Req_2_Object = MibScalar
cond2Req_2 = _Cond2Req_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 157),
    _Cond2Req_2_Type()
)
cond2Req_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cond2Req_2.setStatus("current")
_WaterINTemp1_2_Type = Integer32
_WaterINTemp1_2_Object = MibScalar
waterINTemp1_2 = _WaterINTemp1_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 158),
    _WaterINTemp1_2_Type()
)
waterINTemp1_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    waterINTemp1_2.setStatus("current")
_WaterOUTTemp1_2_Type = Integer32
_WaterOUTTemp1_2_Object = MibScalar
waterOUTTemp1_2 = _WaterOUTTemp1_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 159),
    _WaterOUTTemp1_2_Type()
)
waterOUTTemp1_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    waterOUTTemp1_2.setStatus("current")
_WaterDT1_2_Type = Integer32
_WaterDT1_2_Object = MibScalar
waterDT1_2 = _WaterDT1_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 160),
    _WaterDT1_2_Type()
)
waterDT1_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    waterDT1_2.setStatus("current")
_WaterFlow1_2_Type = Integer32
_WaterFlow1_2_Object = MibScalar
waterFlow1_2 = _WaterFlow1_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 161),
    _WaterFlow1_2_Type()
)
waterFlow1_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    waterFlow1_2.setStatus("current")
_ActWatFlowSet1_2_Type = Integer32
_ActWatFlowSet1_2_Object = MibScalar
actWatFlowSet1_2 = _ActWatFlowSet1_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 162),
    _ActWatFlowSet1_2_Type()
)
actWatFlowSet1_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actWatFlowSet1_2.setStatus("current")
_WaterCoolCap1_2_Type = Integer32
_WaterCoolCap1_2_Object = MibScalar
waterCoolCap1_2 = _WaterCoolCap1_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 163),
    _WaterCoolCap1_2_Type()
)
waterCoolCap1_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    waterCoolCap1_2.setStatus("current")
_EER1_2_Type = Integer32
_EER1_2_Object = MibScalar
eER1_2 = _EER1_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 164),
    _EER1_2_Type()
)
eER1_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eER1_2.setStatus("current")
_Valve1Position_2_Type = Integer32
_Valve1Position_2_Object = MibScalar
valve1Position_2 = _Valve1Position_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 165),
    _Valve1Position_2_Type()
)
valve1Position_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    valve1Position_2.setStatus("current")
_WaterINTemp2_2_Type = Integer32
_WaterINTemp2_2_Object = MibScalar
waterINTemp2_2 = _WaterINTemp2_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 166),
    _WaterINTemp2_2_Type()
)
waterINTemp2_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    waterINTemp2_2.setStatus("current")
_WaterOUTTemp2_2_Type = Integer32
_WaterOUTTemp2_2_Object = MibScalar
waterOUTTemp2_2 = _WaterOUTTemp2_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 167),
    _WaterOUTTemp2_2_Type()
)
waterOUTTemp2_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    waterOUTTemp2_2.setStatus("current")
_WaterDT2_2_Type = Integer32
_WaterDT2_2_Object = MibScalar
waterDT2_2 = _WaterDT2_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 168),
    _WaterDT2_2_Type()
)
waterDT2_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    waterDT2_2.setStatus("current")
_WaterFlow2_2_Type = Integer32
_WaterFlow2_2_Object = MibScalar
waterFlow2_2 = _WaterFlow2_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 169),
    _WaterFlow2_2_Type()
)
waterFlow2_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    waterFlow2_2.setStatus("current")
_ActWatFlowSet2_2_Type = Integer32
_ActWatFlowSet2_2_Object = MibScalar
actWatFlowSet2_2 = _ActWatFlowSet2_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 170),
    _ActWatFlowSet2_2_Type()
)
actWatFlowSet2_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actWatFlowSet2_2.setStatus("current")
_WaterCoolCap2_2_Type = Integer32
_WaterCoolCap2_2_Object = MibScalar
waterCoolCap2_2 = _WaterCoolCap2_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 171),
    _WaterCoolCap2_2_Type()
)
waterCoolCap2_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    waterCoolCap2_2.setStatus("current")
_EER2_2_Type = Integer32
_EER2_2_Object = MibScalar
eER2_2 = _EER2_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 172),
    _EER2_2_Type()
)
eER2_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eER2_2.setStatus("current")
_Valve2Position_2_Type = Integer32
_Valve2Position_2_Object = MibScalar
valve2Position_2 = _Valve2Position_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 173),
    _Valve2Position_2_Type()
)
valve2Position_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    valve2Position_2.setStatus("current")
_HumSteamProd_2_Type = Integer32
_HumSteamProd_2_Object = MibScalar
humSteamProd_2 = _HumSteamProd_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 174),
    _HumSteamProd_2_Type()
)
humSteamProd_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humSteamProd_2.setStatus("current")
_HumWaterConduct_2_Type = Integer32
_HumWaterConduct_2_Object = MibScalar
humWaterConduct_2 = _HumWaterConduct_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 175),
    _HumWaterConduct_2_Type()
)
humWaterConduct_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humWaterConduct_2.setStatus("current")
_HumCurrent_2_Type = Integer32
_HumCurrent_2_Object = MibScalar
humCurrent_2 = _HumCurrent_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 176),
    _HumCurrent_2_Type()
)
humCurrent_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humCurrent_2.setStatus("current")
_HumWorkingMode_2_Type = Integer32
_HumWorkingMode_2_Object = MibScalar
humWorkingMode_2 = _HumWorkingMode_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 177),
    _HumWorkingMode_2_Type()
)
humWorkingMode_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humWorkingMode_2.setStatus("current")
_HumWorkStatus_2_Type = Integer32
_HumWorkStatus_2_Object = MibScalar
humWorkStatus_2 = _HumWorkStatus_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 178),
    _HumWorkStatus_2_Type()
)
humWorkStatus_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humWorkStatus_2.setStatus("current")
_HeaterReq_2_Type = Integer32
_HeaterReq_2_Object = MibScalar
heaterReq_2 = _HeaterReq_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 179),
    _HeaterReq_2_Type()
)
heaterReq_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heaterReq_2.setStatus("current")
_HeaterActiveStg_2_Type = Integer32
_HeaterActiveStg_2_Object = MibScalar
heaterActiveStg_2 = _HeaterActiveStg_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 180),
    _HeaterActiveStg_2_Type()
)
heaterActiveStg_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heaterActiveStg_2.setStatus("current")
_ElHeaterPower_2_Type = Integer32
_ElHeaterPower_2_Object = MibScalar
elHeaterPower_2 = _ElHeaterPower_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 181),
    _ElHeaterPower_2_Type()
)
elHeaterPower_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elHeaterPower_2.setStatus("current")
_HeatValveReq_2_Type = Integer32
_HeatValveReq_2_Object = MibScalar
heatValveReq_2 = _HeatValveReq_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 182),
    _HeatValveReq_2_Type()
)
heatValveReq_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heatValveReq_2.setStatus("current")
_DryCoolerActSet_2_Type = Integer32
_DryCoolerActSet_2_Object = MibScalar
dryCoolerActSet_2 = _DryCoolerActSet_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 183),
    _DryCoolerActSet_2_Type()
)
dryCoolerActSet_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dryCoolerActSet_2.setStatus("current")
_DryCoolerReq_2_Type = Integer32
_DryCoolerReq_2_Object = MibScalar
dryCoolerReq_2 = _DryCoolerReq_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 184),
    _DryCoolerReq_2_Type()
)
dryCoolerReq_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dryCoolerReq_2.setStatus("current")
_UnitWH_2_Type = Integer32
_UnitWH_2_Object = MibScalar
unitWH_2 = _UnitWH_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 185),
    _UnitWH_2_Type()
)
unitWH_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitWH_2.setStatus("current")
_C1WH_2_Type = Integer32
_C1WH_2_Object = MibScalar
c1WH_2 = _C1WH_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 186),
    _C1WH_2_Type()
)
c1WH_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c1WH_2.setStatus("current")
_C1Startup_2_Type = Integer32
_C1Startup_2_Object = MibScalar
c1Startup_2 = _C1Startup_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 187),
    _C1Startup_2_Type()
)
c1Startup_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c1Startup_2.setStatus("current")
_C2WH_2_Type = Integer32
_C2WH_2_Object = MibScalar
c2WH_2 = _C2WH_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 188),
    _C2WH_2_Type()
)
c2WH_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2WH_2.setStatus("current")
_C2Startup_2_Type = Integer32
_C2Startup_2_Object = MibScalar
c2Startup_2 = _C2Startup_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 189),
    _C2Startup_2_Type()
)
c2Startup_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2Startup_2.setStatus("current")
_CoolValveWH_2_Type = Integer32
_CoolValveWH_2_Object = MibScalar
coolValveWH_2 = _CoolValveWH_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 190),
    _CoolValveWH_2_Type()
)
coolValveWH_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolValveWH_2.setStatus("current")
_HeatingWH_2_Type = Integer32
_HeatingWH_2_Object = MibScalar
heatingWH_2 = _HeatingWH_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 191),
    _HeatingWH_2_Type()
)
heatingWH_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heatingWH_2.setStatus("current")
_HumidifWH_2_Type = Integer32
_HumidifWH_2_Object = MibScalar
humidifWH_2 = _HumidifWH_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 192),
    _HumidifWH_2_Type()
)
humidifWH_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidifWH_2.setStatus("current")
_FreeCoolWH_2_Type = Integer32
_FreeCoolWH_2_Object = MibScalar
freeCoolWH_2 = _FreeCoolWH_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 193),
    _FreeCoolWH_2_Type()
)
freeCoolWH_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    freeCoolWH_2.setStatus("current")
_DryCoolerWH_2_Type = Integer32
_DryCoolerWH_2_Object = MibScalar
dryCoolerWH_2 = _DryCoolerWH_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 194),
    _DryCoolerWH_2_Type()
)
dryCoolerWH_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dryCoolerWH_2.setStatus("current")
_Cond1WH_2_Type = Integer32
_Cond1WH_2_Object = MibScalar
cond1WH_2 = _Cond1WH_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 195),
    _Cond1WH_2_Type()
)
cond1WH_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cond1WH_2.setStatus("current")
_Cond2WH_2_Type = Integer32
_Cond2WH_2_Object = MibScalar
cond2WH_2 = _Cond2WH_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 196),
    _Cond2WH_2_Type()
)
cond2WH_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cond2WH_2.setStatus("current")
_TempSetpoint_2_Type = Integer32
_TempSetpoint_2_Object = MibScalar
tempSetpoint_2 = _TempSetpoint_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 197),
    _TempSetpoint_2_Type()
)
tempSetpoint_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempSetpoint_2.setStatus("current")
_HumSetpoint_2_Type = Integer32
_HumSetpoint_2_Object = MibScalar
humSetpoint_2 = _HumSetpoint_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 198),
    _HumSetpoint_2_Type()
)
humSetpoint_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humSetpoint_2.setStatus("current")
_AirFlowSetpoint_2_Type = Integer32
_AirFlowSetpoint_2_Object = MibScalar
airFlowSetpoint_2 = _AirFlowSetpoint_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 199),
    _AirFlowSetpoint_2_Type()
)
airFlowSetpoint_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    airFlowSetpoint_2.setStatus("current")
_AirPresSetpoint_2_Type = Integer32
_AirPresSetpoint_2_Object = MibScalar
airPresSetpoint_2 = _AirPresSetpoint_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 200),
    _AirPresSetpoint_2_Type()
)
airPresSetpoint_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    airPresSetpoint_2.setStatus("current")
_AirDTSetpoint_2_Type = Integer32
_AirDTSetpoint_2_Object = MibScalar
airDTSetpoint_2 = _AirDTSetpoint_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 201),
    _AirDTSetpoint_2_Type()
)
airDTSetpoint_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    airDTSetpoint_2.setStatus("current")
_TempControlSel_2_Type = Integer32
_TempControlSel_2_Object = MibScalar
tempControlSel_2 = _TempControlSel_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 202),
    _TempControlSel_2_Type()
)
tempControlSel_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempControlSel_2.setStatus("current")
_TempControlType_2_Type = Integer32
_TempControlType_2_Object = MibScalar
tempControlType_2 = _TempControlType_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 203),
    _TempControlType_2_Type()
)
tempControlType_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempControlType_2.setStatus("current")
_TPropBand_2_Type = Integer32
_TPropBand_2_Object = MibScalar
tPropBand_2 = _TPropBand_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 204),
    _TPropBand_2_Type()
)
tPropBand_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tPropBand_2.setStatus("current")
_TIntegralTime_2_Type = Integer32
_TIntegralTime_2_Object = MibScalar
tIntegralTime_2 = _TIntegralTime_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 205),
    _TIntegralTime_2_Type()
)
tIntegralTime_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tIntegralTime_2.setStatus("current")
_TDerivativeTime_2_Type = Integer32
_TDerivativeTime_2_Object = MibScalar
tDerivativeTime_2 = _TDerivativeTime_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 206),
    _TDerivativeTime_2_Type()
)
tDerivativeTime_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tDerivativeTime_2.setStatus("current")
_HighTAlOffset_2_Type = Integer32
_HighTAlOffset_2_Object = MibScalar
highTAlOffset_2 = _HighTAlOffset_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 207),
    _HighTAlOffset_2_Type()
)
highTAlOffset_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highTAlOffset_2.setStatus("current")
_LowTAlOffset_2_Type = Integer32
_LowTAlOffset_2_Object = MibScalar
lowTAlOffset_2 = _LowTAlOffset_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 208),
    _LowTAlOffset_2_Type()
)
lowTAlOffset_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowTAlOffset_2.setStatus("current")
_HighLimitTThr_2_Type = Integer32
_HighLimitTThr_2_Object = MibScalar
highLimitTThr_2 = _HighLimitTThr_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 209),
    _HighLimitTThr_2_Type()
)
highLimitTThr_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highLimitTThr_2.setStatus("current")
_HighLimitTMng_2_Type = Integer32
_HighLimitTMng_2_Object = MibScalar
highLimitTMng_2 = _HighLimitTMng_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 210),
    _HighLimitTMng_2_Type()
)
highLimitTMng_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highLimitTMng_2.setStatus("current")
_LowLimitTThr_2_Type = Integer32
_LowLimitTThr_2_Object = MibScalar
lowLimitTThr_2 = _LowLimitTThr_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 211),
    _LowLimitTThr_2_Type()
)
lowLimitTThr_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowLimitTThr_2.setStatus("current")
_LowLimitTMng_2_Type = Integer32
_LowLimitTMng_2_Object = MibScalar
lowLimitTMng_2 = _LowLimitTMng_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 212),
    _LowLimitTMng_2_Type()
)
lowLimitTMng_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowLimitTMng_2.setStatus("current")
_DehumPropBand_2_Type = Integer32
_DehumPropBand_2_Object = MibScalar
dehumPropBand_2 = _DehumPropBand_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 213),
    _DehumPropBand_2_Type()
)
dehumPropBand_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dehumPropBand_2.setStatus("current")
_HumPropBand_2_Type = Integer32
_HumPropBand_2_Object = MibScalar
humPropBand_2 = _HumPropBand_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 214),
    _HumPropBand_2_Type()
)
humPropBand_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humPropBand_2.setStatus("current")
_HRetHAlOffset_2_Type = Integer32
_HRetHAlOffset_2_Object = MibScalar
hRetHAlOffset_2 = _HRetHAlOffset_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 215),
    _HRetHAlOffset_2_Type()
)
hRetHAlOffset_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hRetHAlOffset_2.setStatus("current")
_LRetHAlOffset_2_Type = Integer32
_LRetHAlOffset_2_Object = MibScalar
lRetHAlOffset_2 = _LRetHAlOffset_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 216),
    _LRetHAlOffset_2_Type()
)
lRetHAlOffset_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lRetHAlOffset_2.setStatus("current")
_HighSupHumThr_2_Type = Integer32
_HighSupHumThr_2_Object = MibScalar
highSupHumThr_2 = _HighSupHumThr_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 217),
    _HighSupHumThr_2_Type()
)
highSupHumThr_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highSupHumThr_2.setStatus("current")
_LowSupHumThr_2_Type = Integer32
_LowSupHumThr_2_Object = MibScalar
lowSupHumThr_2 = _LowSupHumThr_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 218),
    _LowSupHumThr_2_Type()
)
lowSupHumThr_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowSupHumThr_2.setStatus("current")
_FCDelta_2_Type = Integer32
_FCDelta_2_Object = MibScalar
fCDelta_2 = _FCDelta_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 219),
    _FCDelta_2_Type()
)
fCDelta_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fCDelta_2.setStatus("current")
_TSWaterSet_2_Type = Integer32
_TSWaterSet_2_Object = MibScalar
tSWaterSet_2 = _TSWaterSet_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 220),
    _TSWaterSet_2_Type()
)
tSWaterSet_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tSWaterSet_2.setStatus("current")
_TSWaterPropBand_2_Type = Integer32
_TSWaterPropBand_2_Object = MibScalar
tSWaterPropBand_2 = _TSWaterPropBand_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 221),
    _TSWaterPropBand_2_Type()
)
tSWaterPropBand_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tSWaterPropBand_2.setStatus("current")
_TSAirTempSet_2_Type = Integer32
_TSAirTempSet_2_Object = MibScalar
tSAirTempSet_2 = _TSAirTempSet_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 222),
    _TSAirTempSet_2_Type()
)
tSAirTempSet_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tSAirTempSet_2.setStatus("current")
_CondSetpoint_2_Type = Integer32
_CondSetpoint_2_Object = MibScalar
condSetpoint_2 = _CondSetpoint_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 223),
    _CondSetpoint_2_Type()
)
condSetpoint_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    condSetpoint_2.setStatus("current")
_CondPropoBand_2_Type = Integer32
_CondPropoBand_2_Object = MibScalar
condPropoBand_2 = _CondPropoBand_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 224),
    _CondPropoBand_2_Type()
)
condPropoBand_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    condPropoBand_2.setStatus("current")
_CondSetIncrease_2_Type = Integer32
_CondSetIncrease_2_Object = MibScalar
condSetIncrease_2 = _CondSetIncrease_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 225),
    _CondSetIncrease_2_Type()
)
condSetIncrease_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    condSetIncrease_2.setStatus("current")
_MaxCondSetpoint_2_Type = Integer32
_MaxCondSetpoint_2_Object = MibScalar
maxCondSetpoint_2 = _MaxCondSetpoint_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 226),
    _MaxCondSetpoint_2_Type()
)
maxCondSetpoint_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxCondSetpoint_2.setStatus("current")
_DryCoolerSet_2_Type = Integer32
_DryCoolerSet_2_Object = MibScalar
dryCoolerSet_2 = _DryCoolerSet_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 227),
    _DryCoolerSet_2_Type()
)
dryCoolerSet_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dryCoolerSet_2.setStatus("current")
_DryCoolPropBand_2_Type = Integer32
_DryCoolPropBand_2_Object = MibScalar
dryCoolPropBand_2 = _DryCoolPropBand_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 228),
    _DryCoolPropBand_2_Type()
)
dryCoolPropBand_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dryCoolPropBand_2.setStatus("current")
_DryCoolSetIncr_2_Type = Integer32
_DryCoolSetIncr_2_Object = MibScalar
dryCoolSetIncr_2 = _DryCoolSetIncr_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 229),
    _DryCoolSetIncr_2_Type()
)
dryCoolSetIncr_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dryCoolSetIncr_2.setStatus("current")
_MaxDryCoolerSet_2_Type = Integer32
_MaxDryCoolerSet_2_Object = MibScalar
maxDryCoolerSet_2 = _MaxDryCoolerSet_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 230),
    _MaxDryCoolerSet_2_Type()
)
maxDryCoolerSet_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxDryCoolerSet_2.setStatus("current")
_DirtyFiltSet_2_Type = Integer32
_DirtyFiltSet_2_Object = MibScalar
dirtyFiltSet_2 = _DirtyFiltSet_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 231),
    _DirtyFiltSet_2_Type()
)
dirtyFiltSet_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dirtyFiltSet_2.setStatus("current")
_DirtyFiltDiff_2_Type = Integer32
_DirtyFiltDiff_2_Object = MibScalar
dirtyFiltDiff_2 = _DirtyFiltDiff_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 232),
    _DirtyFiltDiff_2_Type()
)
dirtyFiltDiff_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dirtyFiltDiff_2.setStatus("current")
_InvCompAlCode1_2_Type = Integer32
_InvCompAlCode1_2_Object = MibScalar
invCompAlCode1_2 = _InvCompAlCode1_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 233),
    _InvCompAlCode1_2_Type()
)
invCompAlCode1_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invCompAlCode1_2.setStatus("current")
_InvCompAlCode2_2_Type = Integer32
_InvCompAlCode2_2_Object = MibScalar
invCompAlCode2_2 = _InvCompAlCode2_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 234),
    _InvCompAlCode2_2_Type()
)
invCompAlCode2_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invCompAlCode2_2.setStatus("current")
_InvCompAlCode3_2_Type = Integer32
_InvCompAlCode3_2_Object = MibScalar
invCompAlCode3_2 = _InvCompAlCode3_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 235),
    _InvCompAlCode3_2_Type()
)
invCompAlCode3_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invCompAlCode3_2.setStatus("current")
_InvCompAlCode4_2_Type = Integer32
_InvCompAlCode4_2_Object = MibScalar
invCompAlCode4_2 = _InvCompAlCode4_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 236),
    _InvCompAlCode4_2_Type()
)
invCompAlCode4_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invCompAlCode4_2.setStatus("current")
_InvCompAlCode5_2_Type = Integer32
_InvCompAlCode5_2_Object = MibScalar
invCompAlCode5_2 = _InvCompAlCode5_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 2, 237),
    _InvCompAlCode5_2_Type()
)
invCompAlCode5_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invCompAlCode5_2.setStatus("current")
_Alarms2_ObjectIdentity = ObjectIdentity
alarms2 = _Alarms2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3)
)
_GeneralAl_2_Type = Integer32
_GeneralAl_2_Object = MibScalar
generalAl_2 = _GeneralAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 1),
    _GeneralAl_2_Type()
)
generalAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generalAl_2.setStatus("current")
_NotCriticAl_2_Type = Integer32
_NotCriticAl_2_Object = MibScalar
notCriticAl_2 = _NotCriticAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 2),
    _NotCriticAl_2_Type()
)
notCriticAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notCriticAl_2.setStatus("current")
_CriticalAl_2_Type = Integer32
_CriticalAl_2_Object = MibScalar
criticalAl_2 = _CriticalAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 3),
    _CriticalAl_2_Type()
)
criticalAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    criticalAl_2.setStatus("current")
_FansAl_2_Type = Integer32
_FansAl_2_Object = MibScalar
fansAl_2 = _FansAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 4),
    _FansAl_2_Type()
)
fansAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fansAl_2.setStatus("current")
_CompAl_2_Type = Integer32
_CompAl_2_Object = MibScalar
compAl_2 = _CompAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 5),
    _CompAl_2_Type()
)
compAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compAl_2.setStatus("current")
_TempAl_2_Type = Integer32
_TempAl_2_Object = MibScalar
tempAl_2 = _TempAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 6),
    _TempAl_2_Type()
)
tempAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempAl_2.setStatus("current")
_HumidityAl_2_Type = Integer32
_HumidityAl_2_Object = MibScalar
humidityAl_2 = _HumidityAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 7),
    _HumidityAl_2_Type()
)
humidityAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidityAl_2.setStatus("current")
_DamperAl_2_Type = Integer32
_DamperAl_2_Object = MibScalar
damperAl_2 = _DamperAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 8),
    _DamperAl_2_Type()
)
damperAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    damperAl_2.setStatus("current")
_FireSmokeAl_2_Type = Integer32
_FireSmokeAl_2_Object = MibScalar
fireSmokeAl_2 = _FireSmokeAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 9),
    _FireSmokeAl_2_Type()
)
fireSmokeAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fireSmokeAl_2.setStatus("current")
_GSeriousAl_2_Type = Integer32
_GSeriousAl_2_Object = MibScalar
gSeriousAl_2 = _GSeriousAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 10),
    _GSeriousAl_2_Type()
)
gSeriousAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gSeriousAl_2.setStatus("current")
_FansGenAl_2_Type = Integer32
_FansGenAl_2_Object = MibScalar
fansGenAl_2 = _FansGenAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 11),
    _FansGenAl_2_Type()
)
fansGenAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fansGenAl_2.setStatus("current")
_F1GeneralAl_2_Type = Integer32
_F1GeneralAl_2_Object = MibScalar
f1GeneralAl_2 = _F1GeneralAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 12),
    _F1GeneralAl_2_Type()
)
f1GeneralAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f1GeneralAl_2.setStatus("current")
_F1PowerAl_2_Type = Integer32
_F1PowerAl_2_Object = MibScalar
f1PowerAl_2 = _F1PowerAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 13),
    _F1PowerAl_2_Type()
)
f1PowerAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f1PowerAl_2.setStatus("current")
_F1CommAl_2_Type = Integer32
_F1CommAl_2_Object = MibScalar
f1CommAl_2 = _F1CommAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 14),
    _F1CommAl_2_Type()
)
f1CommAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f1CommAl_2.setStatus("current")
_F1HiTempAl_2_Type = Integer32
_F1HiTempAl_2_Object = MibScalar
f1HiTempAl_2 = _F1HiTempAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 15),
    _F1HiTempAl_2_Type()
)
f1HiTempAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f1HiTempAl_2.setStatus("current")
_F1NetComAl_2_Type = Integer32
_F1NetComAl_2_Object = MibScalar
f1NetComAl_2 = _F1NetComAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 16),
    _F1NetComAl_2_Type()
)
f1NetComAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f1NetComAl_2.setStatus("current")
_F1InvRegAl_2_Type = Integer32
_F1InvRegAl_2_Object = MibScalar
f1InvRegAl_2 = _F1InvRegAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 17),
    _F1InvRegAl_2_Type()
)
f1InvRegAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f1InvRegAl_2.setStatus("current")
_F1HiMotTAl_2_Type = Integer32
_F1HiMotTAl_2_Object = MibScalar
f1HiMotTAl_2 = _F1HiMotTAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 18),
    _F1HiMotTAl_2_Type()
)
f1HiMotTAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f1HiMotTAl_2.setStatus("current")
_F1HallSenAl_2_Type = Integer32
_F1HallSenAl_2_Object = MibScalar
f1HallSenAl_2 = _F1HallSenAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 19),
    _F1HallSenAl_2_Type()
)
f1HallSenAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f1HallSenAl_2.setStatus("current")
_F1OverlAl_2_Type = Integer32
_F1OverlAl_2_Object = MibScalar
f1OverlAl_2 = _F1OverlAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 20),
    _F1OverlAl_2_Type()
)
f1OverlAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f1OverlAl_2.setStatus("current")
_F1LowDCAl_2_Type = Integer32
_F1LowDCAl_2_Object = MibScalar
f1LowDCAl_2 = _F1LowDCAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 21),
    _F1LowDCAl_2_Type()
)
f1LowDCAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f1LowDCAl_2.setStatus("current")
_F2GeneralAl_2_Type = Integer32
_F2GeneralAl_2_Object = MibScalar
f2GeneralAl_2 = _F2GeneralAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 22),
    _F2GeneralAl_2_Type()
)
f2GeneralAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f2GeneralAl_2.setStatus("current")
_F2PowerAl_2_Type = Integer32
_F2PowerAl_2_Object = MibScalar
f2PowerAl_2 = _F2PowerAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 23),
    _F2PowerAl_2_Type()
)
f2PowerAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f2PowerAl_2.setStatus("current")
_F2CommAl_2_Type = Integer32
_F2CommAl_2_Object = MibScalar
f2CommAl_2 = _F2CommAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 24),
    _F2CommAl_2_Type()
)
f2CommAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f2CommAl_2.setStatus("current")
_F2HiTempAl_2_Type = Integer32
_F2HiTempAl_2_Object = MibScalar
f2HiTempAl_2 = _F2HiTempAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 25),
    _F2HiTempAl_2_Type()
)
f2HiTempAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f2HiTempAl_2.setStatus("current")
_F2NetComAl_2_Type = Integer32
_F2NetComAl_2_Object = MibScalar
f2NetComAl_2 = _F2NetComAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 26),
    _F2NetComAl_2_Type()
)
f2NetComAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f2NetComAl_2.setStatus("current")
_F2InvRegAl_2_Type = Integer32
_F2InvRegAl_2_Object = MibScalar
f2InvRegAl_2 = _F2InvRegAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 27),
    _F2InvRegAl_2_Type()
)
f2InvRegAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f2InvRegAl_2.setStatus("current")
_F2HiMotTAl_2_Type = Integer32
_F2HiMotTAl_2_Object = MibScalar
f2HiMotTAl_2 = _F2HiMotTAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 28),
    _F2HiMotTAl_2_Type()
)
f2HiMotTAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f2HiMotTAl_2.setStatus("current")
_F2HallSenAl_2_Type = Integer32
_F2HallSenAl_2_Object = MibScalar
f2HallSenAl_2 = _F2HallSenAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 29),
    _F2HallSenAl_2_Type()
)
f2HallSenAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f2HallSenAl_2.setStatus("current")
_F2OverlAl_2_Type = Integer32
_F2OverlAl_2_Object = MibScalar
f2OverlAl_2 = _F2OverlAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 30),
    _F2OverlAl_2_Type()
)
f2OverlAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f2OverlAl_2.setStatus("current")
_F2LowDCAl_2_Type = Integer32
_F2LowDCAl_2_Object = MibScalar
f2LowDCAl_2 = _F2LowDCAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 31),
    _F2LowDCAl_2_Type()
)
f2LowDCAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f2LowDCAl_2.setStatus("current")
_F3GeneralAl_2_Type = Integer32
_F3GeneralAl_2_Object = MibScalar
f3GeneralAl_2 = _F3GeneralAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 32),
    _F3GeneralAl_2_Type()
)
f3GeneralAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3GeneralAl_2.setStatus("current")
_F3PowerAl_2_Type = Integer32
_F3PowerAl_2_Object = MibScalar
f3PowerAl_2 = _F3PowerAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 33),
    _F3PowerAl_2_Type()
)
f3PowerAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PowerAl_2.setStatus("current")
_F3CommAl_2_Type = Integer32
_F3CommAl_2_Object = MibScalar
f3CommAl_2 = _F3CommAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 34),
    _F3CommAl_2_Type()
)
f3CommAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3CommAl_2.setStatus("current")
_F3HiTempAl_2_Type = Integer32
_F3HiTempAl_2_Object = MibScalar
f3HiTempAl_2 = _F3HiTempAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 35),
    _F3HiTempAl_2_Type()
)
f3HiTempAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3HiTempAl_2.setStatus("current")
_F3NetComAl_2_Type = Integer32
_F3NetComAl_2_Object = MibScalar
f3NetComAl_2 = _F3NetComAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 36),
    _F3NetComAl_2_Type()
)
f3NetComAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetComAl_2.setStatus("current")
_F3InvRegAl_2_Type = Integer32
_F3InvRegAl_2_Object = MibScalar
f3InvRegAl_2 = _F3InvRegAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 37),
    _F3InvRegAl_2_Type()
)
f3InvRegAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3InvRegAl_2.setStatus("current")
_F3HiMotTAl_2_Type = Integer32
_F3HiMotTAl_2_Object = MibScalar
f3HiMotTAl_2 = _F3HiMotTAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 38),
    _F3HiMotTAl_2_Type()
)
f3HiMotTAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3HiMotTAl_2.setStatus("current")
_F3HallSenAl_2_Type = Integer32
_F3HallSenAl_2_Object = MibScalar
f3HallSenAl_2 = _F3HallSenAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 39),
    _F3HallSenAl_2_Type()
)
f3HallSenAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3HallSenAl_2.setStatus("current")
_F3OverlAl_2_Type = Integer32
_F3OverlAl_2_Object = MibScalar
f3OverlAl_2 = _F3OverlAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 40),
    _F3OverlAl_2_Type()
)
f3OverlAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3OverlAl_2.setStatus("current")
_F3LowDCAl_2_Type = Integer32
_F3LowDCAl_2_Object = MibScalar
f3LowDCAl_2 = _F3LowDCAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 41),
    _F3LowDCAl_2_Type()
)
f3LowDCAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3LowDCAl_2.setStatus("current")
_F4GeneralAl_2_Type = Integer32
_F4GeneralAl_2_Object = MibScalar
f4GeneralAl_2 = _F4GeneralAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 42),
    _F4GeneralAl_2_Type()
)
f4GeneralAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f4GeneralAl_2.setStatus("current")
_F4PowerAl_2_Type = Integer32
_F4PowerAl_2_Object = MibScalar
f4PowerAl_2 = _F4PowerAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 43),
    _F4PowerAl_2_Type()
)
f4PowerAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f4PowerAl_2.setStatus("current")
_F4CommAl_2_Type = Integer32
_F4CommAl_2_Object = MibScalar
f4CommAl_2 = _F4CommAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 44),
    _F4CommAl_2_Type()
)
f4CommAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f4CommAl_2.setStatus("current")
_F4HiTempAl_2_Type = Integer32
_F4HiTempAl_2_Object = MibScalar
f4HiTempAl_2 = _F4HiTempAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 45),
    _F4HiTempAl_2_Type()
)
f4HiTempAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f4HiTempAl_2.setStatus("current")
_F4NetComAl_2_Type = Integer32
_F4NetComAl_2_Object = MibScalar
f4NetComAl_2 = _F4NetComAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 46),
    _F4NetComAl_2_Type()
)
f4NetComAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f4NetComAl_2.setStatus("current")
_F4InvRegAl_2_Type = Integer32
_F4InvRegAl_2_Object = MibScalar
f4InvRegAl_2 = _F4InvRegAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 47),
    _F4InvRegAl_2_Type()
)
f4InvRegAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f4InvRegAl_2.setStatus("current")
_F4HiMotTAl_2_Type = Integer32
_F4HiMotTAl_2_Object = MibScalar
f4HiMotTAl_2 = _F4HiMotTAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 48),
    _F4HiMotTAl_2_Type()
)
f4HiMotTAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f4HiMotTAl_2.setStatus("current")
_F4HallSenAl_2_Type = Integer32
_F4HallSenAl_2_Object = MibScalar
f4HallSenAl_2 = _F4HallSenAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 49),
    _F4HallSenAl_2_Type()
)
f4HallSenAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f4HallSenAl_2.setStatus("current")
_F4OverlAl_2_Type = Integer32
_F4OverlAl_2_Object = MibScalar
f4OverlAl_2 = _F4OverlAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 50),
    _F4OverlAl_2_Type()
)
f4OverlAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f4OverlAl_2.setStatus("current")
_F4LowDCAl_2_Type = Integer32
_F4LowDCAl_2_Object = MibScalar
f4LowDCAl_2 = _F4LowDCAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 51),
    _F4LowDCAl_2_Type()
)
f4LowDCAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f4LowDCAl_2.setStatus("current")
_F5GeneralAl_2_Type = Integer32
_F5GeneralAl_2_Object = MibScalar
f5GeneralAl_2 = _F5GeneralAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 52),
    _F5GeneralAl_2_Type()
)
f5GeneralAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f5GeneralAl_2.setStatus("current")
_F5PowerAl_2_Type = Integer32
_F5PowerAl_2_Object = MibScalar
f5PowerAl_2 = _F5PowerAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 53),
    _F5PowerAl_2_Type()
)
f5PowerAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f5PowerAl_2.setStatus("current")
_F5CommAl_2_Type = Integer32
_F5CommAl_2_Object = MibScalar
f5CommAl_2 = _F5CommAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 54),
    _F5CommAl_2_Type()
)
f5CommAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f5CommAl_2.setStatus("current")
_F5HiTempAl_2_Type = Integer32
_F5HiTempAl_2_Object = MibScalar
f5HiTempAl_2 = _F5HiTempAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 55),
    _F5HiTempAl_2_Type()
)
f5HiTempAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f5HiTempAl_2.setStatus("current")
_F5NetComAl_2_Type = Integer32
_F5NetComAl_2_Object = MibScalar
f5NetComAl_2 = _F5NetComAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 56),
    _F5NetComAl_2_Type()
)
f5NetComAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f5NetComAl_2.setStatus("current")
_F5InvRegAl_2_Type = Integer32
_F5InvRegAl_2_Object = MibScalar
f5InvRegAl_2 = _F5InvRegAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 57),
    _F5InvRegAl_2_Type()
)
f5InvRegAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f5InvRegAl_2.setStatus("current")
_F5HiMotTAl_2_Type = Integer32
_F5HiMotTAl_2_Object = MibScalar
f5HiMotTAl_2 = _F5HiMotTAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 58),
    _F5HiMotTAl_2_Type()
)
f5HiMotTAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f5HiMotTAl_2.setStatus("current")
_F5HallSenAl_2_Type = Integer32
_F5HallSenAl_2_Object = MibScalar
f5HallSenAl_2 = _F5HallSenAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 59),
    _F5HallSenAl_2_Type()
)
f5HallSenAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f5HallSenAl_2.setStatus("current")
_F5OverlAl_2_Type = Integer32
_F5OverlAl_2_Object = MibScalar
f5OverlAl_2 = _F5OverlAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 60),
    _F5OverlAl_2_Type()
)
f5OverlAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f5OverlAl_2.setStatus("current")
_F5LowDCAl_2_Type = Integer32
_F5LowDCAl_2_Object = MibScalar
f5LowDCAl_2 = _F5LowDCAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 61),
    _F5LowDCAl_2_Type()
)
f5LowDCAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f5LowDCAl_2.setStatus("current")
_F6GeneralAl_2_Type = Integer32
_F6GeneralAl_2_Object = MibScalar
f6GeneralAl_2 = _F6GeneralAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 62),
    _F6GeneralAl_2_Type()
)
f6GeneralAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f6GeneralAl_2.setStatus("current")
_F6PowerAl_2_Type = Integer32
_F6PowerAl_2_Object = MibScalar
f6PowerAl_2 = _F6PowerAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 63),
    _F6PowerAl_2_Type()
)
f6PowerAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f6PowerAl_2.setStatus("current")
_F6CommAl_2_Type = Integer32
_F6CommAl_2_Object = MibScalar
f6CommAl_2 = _F6CommAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 64),
    _F6CommAl_2_Type()
)
f6CommAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f6CommAl_2.setStatus("current")
_F6HiTempAl_2_Type = Integer32
_F6HiTempAl_2_Object = MibScalar
f6HiTempAl_2 = _F6HiTempAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 65),
    _F6HiTempAl_2_Type()
)
f6HiTempAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f6HiTempAl_2.setStatus("current")
_F6NetComAl_2_Type = Integer32
_F6NetComAl_2_Object = MibScalar
f6NetComAl_2 = _F6NetComAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 66),
    _F6NetComAl_2_Type()
)
f6NetComAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f6NetComAl_2.setStatus("current")
_F6InvRegAl_2_Type = Integer32
_F6InvRegAl_2_Object = MibScalar
f6InvRegAl_2 = _F6InvRegAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 67),
    _F6InvRegAl_2_Type()
)
f6InvRegAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f6InvRegAl_2.setStatus("current")
_F6HiMotTAl_2_Type = Integer32
_F6HiMotTAl_2_Object = MibScalar
f6HiMotTAl_2 = _F6HiMotTAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 68),
    _F6HiMotTAl_2_Type()
)
f6HiMotTAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f6HiMotTAl_2.setStatus("current")
_F6HallSenAl_2_Type = Integer32
_F6HallSenAl_2_Object = MibScalar
f6HallSenAl_2 = _F6HallSenAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 69),
    _F6HallSenAl_2_Type()
)
f6HallSenAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f6HallSenAl_2.setStatus("current")
_F6OverlAl_2_Type = Integer32
_F6OverlAl_2_Object = MibScalar
f6OverlAl_2 = _F6OverlAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 70),
    _F6OverlAl_2_Type()
)
f6OverlAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f6OverlAl_2.setStatus("current")
_F6LowDCAl_2_Type = Integer32
_F6LowDCAl_2_Object = MibScalar
f6LowDCAl_2 = _F6LowDCAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 71),
    _F6LowDCAl_2_Type()
)
f6LowDCAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f6LowDCAl_2.setStatus("current")
_F7GeneralAl_2_Type = Integer32
_F7GeneralAl_2_Object = MibScalar
f7GeneralAl_2 = _F7GeneralAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 72),
    _F7GeneralAl_2_Type()
)
f7GeneralAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f7GeneralAl_2.setStatus("current")
_F7PowerAl_2_Type = Integer32
_F7PowerAl_2_Object = MibScalar
f7PowerAl_2 = _F7PowerAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 73),
    _F7PowerAl_2_Type()
)
f7PowerAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f7PowerAl_2.setStatus("current")
_F7CommAl_2_Type = Integer32
_F7CommAl_2_Object = MibScalar
f7CommAl_2 = _F7CommAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 74),
    _F7CommAl_2_Type()
)
f7CommAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f7CommAl_2.setStatus("current")
_F7HiTempAl_2_Type = Integer32
_F7HiTempAl_2_Object = MibScalar
f7HiTempAl_2 = _F7HiTempAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 75),
    _F7HiTempAl_2_Type()
)
f7HiTempAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f7HiTempAl_2.setStatus("current")
_F7NetComAl_2_Type = Integer32
_F7NetComAl_2_Object = MibScalar
f7NetComAl_2 = _F7NetComAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 76),
    _F7NetComAl_2_Type()
)
f7NetComAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f7NetComAl_2.setStatus("current")
_F7InvRegAl_2_Type = Integer32
_F7InvRegAl_2_Object = MibScalar
f7InvRegAl_2 = _F7InvRegAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 77),
    _F7InvRegAl_2_Type()
)
f7InvRegAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f7InvRegAl_2.setStatus("current")
_F7HiMotTAl_2_Type = Integer32
_F7HiMotTAl_2_Object = MibScalar
f7HiMotTAl_2 = _F7HiMotTAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 78),
    _F7HiMotTAl_2_Type()
)
f7HiMotTAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f7HiMotTAl_2.setStatus("current")
_F7HallSenAl_2_Type = Integer32
_F7HallSenAl_2_Object = MibScalar
f7HallSenAl_2 = _F7HallSenAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 79),
    _F7HallSenAl_2_Type()
)
f7HallSenAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f7HallSenAl_2.setStatus("current")
_F7OverlAl_2_Type = Integer32
_F7OverlAl_2_Object = MibScalar
f7OverlAl_2 = _F7OverlAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 80),
    _F7OverlAl_2_Type()
)
f7OverlAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f7OverlAl_2.setStatus("current")
_F7LowDCAl_2_Type = Integer32
_F7LowDCAl_2_Object = MibScalar
f7LowDCAl_2 = _F7LowDCAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 81),
    _F7LowDCAl_2_Type()
)
f7LowDCAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f7LowDCAl_2.setStatus("current")
_F8GeneralAl_2_Type = Integer32
_F8GeneralAl_2_Object = MibScalar
f8GeneralAl_2 = _F8GeneralAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 82),
    _F8GeneralAl_2_Type()
)
f8GeneralAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f8GeneralAl_2.setStatus("current")
_F8PowerAl_2_Type = Integer32
_F8PowerAl_2_Object = MibScalar
f8PowerAl_2 = _F8PowerAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 83),
    _F8PowerAl_2_Type()
)
f8PowerAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f8PowerAl_2.setStatus("current")
_F8CommAl_2_Type = Integer32
_F8CommAl_2_Object = MibScalar
f8CommAl_2 = _F8CommAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 84),
    _F8CommAl_2_Type()
)
f8CommAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f8CommAl_2.setStatus("current")
_F8HiTempAl_2_Type = Integer32
_F8HiTempAl_2_Object = MibScalar
f8HiTempAl_2 = _F8HiTempAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 85),
    _F8HiTempAl_2_Type()
)
f8HiTempAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f8HiTempAl_2.setStatus("current")
_F8NetComAl_2_Type = Integer32
_F8NetComAl_2_Object = MibScalar
f8NetComAl_2 = _F8NetComAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 86),
    _F8NetComAl_2_Type()
)
f8NetComAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f8NetComAl_2.setStatus("current")
_F8InvRegAl_2_Type = Integer32
_F8InvRegAl_2_Object = MibScalar
f8InvRegAl_2 = _F8InvRegAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 87),
    _F8InvRegAl_2_Type()
)
f8InvRegAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f8InvRegAl_2.setStatus("current")
_F8HiMotTAl_2_Type = Integer32
_F8HiMotTAl_2_Object = MibScalar
f8HiMotTAl_2 = _F8HiMotTAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 88),
    _F8HiMotTAl_2_Type()
)
f8HiMotTAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f8HiMotTAl_2.setStatus("current")
_F8HallSenAl_2_Type = Integer32
_F8HallSenAl_2_Object = MibScalar
f8HallSenAl_2 = _F8HallSenAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 89),
    _F8HallSenAl_2_Type()
)
f8HallSenAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f8HallSenAl_2.setStatus("current")
_F8OverlAl_2_Type = Integer32
_F8OverlAl_2_Object = MibScalar
f8OverlAl_2 = _F8OverlAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 90),
    _F8OverlAl_2_Type()
)
f8OverlAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f8OverlAl_2.setStatus("current")
_F8LowDCAl_2_Type = Integer32
_F8LowDCAl_2_Object = MibScalar
f8LowDCAl_2 = _F8LowDCAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 91),
    _F8LowDCAl_2_Type()
)
f8LowDCAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f8LowDCAl_2.setStatus("current")
_F9GeneralAl_2_Type = Integer32
_F9GeneralAl_2_Object = MibScalar
f9GeneralAl_2 = _F9GeneralAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 92),
    _F9GeneralAl_2_Type()
)
f9GeneralAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f9GeneralAl_2.setStatus("current")
_F9PowerAl_2_Type = Integer32
_F9PowerAl_2_Object = MibScalar
f9PowerAl_2 = _F9PowerAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 93),
    _F9PowerAl_2_Type()
)
f9PowerAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f9PowerAl_2.setStatus("current")
_F9CommAl_2_Type = Integer32
_F9CommAl_2_Object = MibScalar
f9CommAl_2 = _F9CommAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 94),
    _F9CommAl_2_Type()
)
f9CommAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f9CommAl_2.setStatus("current")
_F9HiTempAl_2_Type = Integer32
_F9HiTempAl_2_Object = MibScalar
f9HiTempAl_2 = _F9HiTempAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 95),
    _F9HiTempAl_2_Type()
)
f9HiTempAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f9HiTempAl_2.setStatus("current")
_F9NetComAl_2_Type = Integer32
_F9NetComAl_2_Object = MibScalar
f9NetComAl_2 = _F9NetComAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 96),
    _F9NetComAl_2_Type()
)
f9NetComAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f9NetComAl_2.setStatus("current")
_F9InvRegAl_2_Type = Integer32
_F9InvRegAl_2_Object = MibScalar
f9InvRegAl_2 = _F9InvRegAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 97),
    _F9InvRegAl_2_Type()
)
f9InvRegAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f9InvRegAl_2.setStatus("current")
_F9HiMotTAl_2_Type = Integer32
_F9HiMotTAl_2_Object = MibScalar
f9HiMotTAl_2 = _F9HiMotTAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 98),
    _F9HiMotTAl_2_Type()
)
f9HiMotTAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f9HiMotTAl_2.setStatus("current")
_F9HallSenAl_2_Type = Integer32
_F9HallSenAl_2_Object = MibScalar
f9HallSenAl_2 = _F9HallSenAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 99),
    _F9HallSenAl_2_Type()
)
f9HallSenAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f9HallSenAl_2.setStatus("current")
_F9OverlAl_2_Type = Integer32
_F9OverlAl_2_Object = MibScalar
f9OverlAl_2 = _F9OverlAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 100),
    _F9OverlAl_2_Type()
)
f9OverlAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f9OverlAl_2.setStatus("current")
_F9LowDCAl_2_Type = Integer32
_F9LowDCAl_2_Object = MibScalar
f9LowDCAl_2 = _F9LowDCAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 101),
    _F9LowDCAl_2_Type()
)
f9LowDCAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f9LowDCAl_2.setStatus("current")
_F10GenlAl_2_Type = Integer32
_F10GenlAl_2_Object = MibScalar
f10GenlAl_2 = _F10GenlAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 102),
    _F10GenlAl_2_Type()
)
f10GenlAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10GenlAl_2.setStatus("current")
_F10PowerAl_2_Type = Integer32
_F10PowerAl_2_Object = MibScalar
f10PowerAl_2 = _F10PowerAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 103),
    _F10PowerAl_2_Type()
)
f10PowerAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10PowerAl_2.setStatus("current")
_F10CommAl_2_Type = Integer32
_F10CommAl_2_Object = MibScalar
f10CommAl_2 = _F10CommAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 104),
    _F10CommAl_2_Type()
)
f10CommAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10CommAl_2.setStatus("current")
_F10HiTempAl_2_Type = Integer32
_F10HiTempAl_2_Object = MibScalar
f10HiTempAl_2 = _F10HiTempAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 105),
    _F10HiTempAl_2_Type()
)
f10HiTempAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10HiTempAl_2.setStatus("current")
_F10NetComAl_2_Type = Integer32
_F10NetComAl_2_Object = MibScalar
f10NetComAl_2 = _F10NetComAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 106),
    _F10NetComAl_2_Type()
)
f10NetComAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10NetComAl_2.setStatus("current")
_F10InvRegAl_2_Type = Integer32
_F10InvRegAl_2_Object = MibScalar
f10InvRegAl_2 = _F10InvRegAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 107),
    _F10InvRegAl_2_Type()
)
f10InvRegAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10InvRegAl_2.setStatus("current")
_F10HiMotTAl_2_Type = Integer32
_F10HiMotTAl_2_Object = MibScalar
f10HiMotTAl_2 = _F10HiMotTAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 108),
    _F10HiMotTAl_2_Type()
)
f10HiMotTAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10HiMotTAl_2.setStatus("current")
_F10HallSAl_2_Type = Integer32
_F10HallSAl_2_Object = MibScalar
f10HallSAl_2 = _F10HallSAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 109),
    _F10HallSAl_2_Type()
)
f10HallSAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10HallSAl_2.setStatus("current")
_F10OverlAl_2_Type = Integer32
_F10OverlAl_2_Object = MibScalar
f10OverlAl_2 = _F10OverlAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 110),
    _F10OverlAl_2_Type()
)
f10OverlAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10OverlAl_2.setStatus("current")
_F10LowDCAl_2_Type = Integer32
_F10LowDCAl_2_Object = MibScalar
f10LowDCAl_2 = _F10LowDCAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 111),
    _F10LowDCAl_2_Type()
)
f10LowDCAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10LowDCAl_2.setStatus("current")
_RetTempPbAl_2_Type = Integer32
_RetTempPbAl_2_Object = MibScalar
retTempPbAl_2 = _RetTempPbAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 112),
    _RetTempPbAl_2_Type()
)
retTempPbAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    retTempPbAl_2.setStatus("current")
_SupTempPrAl_2_Type = Integer32
_SupTempPrAl_2_Object = MibScalar
supTempPrAl_2 = _SupTempPrAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 113),
    _SupTempPrAl_2_Type()
)
supTempPrAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supTempPrAl_2.setStatus("current")
_RetHumPrAl_2_Type = Integer32
_RetHumPrAl_2_Object = MibScalar
retHumPrAl_2 = _RetHumPrAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 114),
    _RetHumPrAl_2_Type()
)
retHumPrAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    retHumPrAl_2.setStatus("current")
_SupHumPrAl_2_Type = Integer32
_SupHumPrAl_2_Object = MibScalar
supHumPrAl_2 = _SupHumPrAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 115),
    _SupHumPrAl_2_Type()
)
supHumPrAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supHumPrAl_2.setStatus("current")
_AirPrSensAl_2_Type = Integer32
_AirPrSensAl_2_Object = MibScalar
airPrSensAl_2 = _AirPrSensAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 116),
    _AirPrSensAl_2_Type()
)
airPrSensAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airPrSensAl_2.setStatus("current")
_WatIN1PrAl_2_Type = Integer32
_WatIN1PrAl_2_Object = MibScalar
watIN1PrAl_2 = _WatIN1PrAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 117),
    _WatIN1PrAl_2_Type()
)
watIN1PrAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    watIN1PrAl_2.setStatus("current")
_WatOUT1PrAl_2_Type = Integer32
_WatOUT1PrAl_2_Object = MibScalar
watOUT1PrAl_2 = _WatOUT1PrAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 118),
    _WatOUT1PrAl_2_Type()
)
watOUT1PrAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    watOUT1PrAl_2.setStatus("current")
_WatIN2PrAl_2_Type = Integer32
_WatIN2PrAl_2_Object = MibScalar
watIN2PrAl_2 = _WatIN2PrAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 119),
    _WatIN2PrAl_2_Type()
)
watIN2PrAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    watIN2PrAl_2.setStatus("current")
_WatOUT2PrAl_2_Type = Integer32
_WatOUT2PrAl_2_Object = MibScalar
watOUT2PrAl_2 = _WatOUT2PrAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 120),
    _WatOUT2PrAl_2_Type()
)
watOUT2PrAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    watOUT2PrAl_2.setStatus("current")
_WatFlw1PrAl_2_Type = Integer32
_WatFlw1PrAl_2_Object = MibScalar
watFlw1PrAl_2 = _WatFlw1PrAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 121),
    _WatFlw1PrAl_2_Type()
)
watFlw1PrAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    watFlw1PrAl_2.setStatus("current")
_WatFlw2PrAl_2_Type = Integer32
_WatFlw2PrAl_2_Object = MibScalar
watFlw2PrAl_2 = _WatFlw2PrAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 122),
    _WatFlw2PrAl_2_Type()
)
watFlw2PrAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    watFlw2PrAl_2.setStatus("current")
_DFPSGenAl_2_Type = Integer32
_DFPSGenAl_2_Object = MibScalar
dFPSGenAl_2 = _DFPSGenAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 123),
    _DFPSGenAl_2_Type()
)
dFPSGenAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dFPSGenAl_2.setStatus("current")
_DFPSBrokAl_2_Type = Integer32
_DFPSBrokAl_2_Object = MibScalar
dFPSBrokAl_2 = _DFPSBrokAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 124),
    _DFPSBrokAl_2_Type()
)
dFPSBrokAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dFPSBrokAl_2.setStatus("current")
_DFPSCablAl_2_Type = Integer32
_DFPSCablAl_2_Object = MibScalar
dFPSCablAl_2 = _DFPSCablAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 125),
    _DFPSCablAl_2_Type()
)
dFPSCablAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dFPSCablAl_2.setStatus("current")
_DFPSRangeAl_2_Type = Integer32
_DFPSRangeAl_2_Object = MibScalar
dFPSRangeAl_2 = _DFPSRangeAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 126),
    _DFPSRangeAl_2_Type()
)
dFPSRangeAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dFPSRangeAl_2.setStatus("current")
_DFPSADCAl_2_Type = Integer32
_DFPSADCAl_2_Object = MibScalar
dFPSADCAl_2 = _DFPSADCAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 127),
    _DFPSADCAl_2_Type()
)
dFPSADCAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dFPSADCAl_2.setStatus("current")
_DFPSSetAl_2_Type = Integer32
_DFPSSetAl_2_Object = MibScalar
dFPSSetAl_2 = _DFPSSetAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 128),
    _DFPSSetAl_2_Type()
)
dFPSSetAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dFPSSetAl_2.setStatus("current")
_DFPSDCOAl_2_Type = Integer32
_DFPSDCOAl_2_Object = MibScalar
dFPSDCOAl_2 = _DFPSDCOAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 129),
    _DFPSDCOAl_2_Type()
)
dFPSDCOAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dFPSDCOAl_2.setStatus("current")
_DFPSWatdAl_2_Type = Integer32
_DFPSWatdAl_2_Object = MibScalar
dFPSWatdAl_2 = _DFPSWatdAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 130),
    _DFPSWatdAl_2_Type()
)
dFPSWatdAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dFPSWatdAl_2.setStatus("current")
_DFPSCommAl_2_Type = Integer32
_DFPSCommAl_2_Object = MibScalar
dFPSCommAl_2 = _DFPSCommAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 131),
    _DFPSCommAl_2_Type()
)
dFPSCommAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dFPSCommAl_2.setStatus("current")
_InvC1GenAl_2_Type = Integer32
_InvC1GenAl_2_Object = MibScalar
invC1GenAl_2 = _InvC1GenAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 132),
    _InvC1GenAl_2_Type()
)
invC1GenAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invC1GenAl_2.setStatus("current")
_InvC1CommAl_2_Type = Integer32
_InvC1CommAl_2_Object = MibScalar
invC1CommAl_2 = _InvC1CommAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 133),
    _InvC1CommAl_2_Type()
)
invC1CommAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invC1CommAl_2.setStatus("current")
_C1ThermAl_2_Type = Integer32
_C1ThermAl_2_Object = MibScalar
c1ThermAl_2 = _C1ThermAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 134),
    _C1ThermAl_2_Type()
)
c1ThermAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c1ThermAl_2.setStatus("current")
_C1HighPresAl_2_Type = Integer32
_C1HighPresAl_2_Object = MibScalar
c1HighPresAl_2 = _C1HighPresAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 135),
    _C1HighPresAl_2_Type()
)
c1HighPresAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c1HighPresAl_2.setStatus("current")
_C1LowPresAl_2_Type = Integer32
_C1LowPresAl_2_Object = MibScalar
c1LowPresAl_2 = _C1LowPresAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 136),
    _C1LowPresAl_2_Type()
)
c1LowPresAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c1LowPresAl_2.setStatus("current")
_C1HighDiscAl_2_Type = Integer32
_C1HighDiscAl_2_Object = MibScalar
c1HighDiscAl_2 = _C1HighDiscAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 137),
    _C1HighDiscAl_2_Type()
)
c1HighDiscAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c1HighDiscAl_2.setStatus("current")
_C1LCompRatAl_2_Type = Integer32
_C1LCompRatAl_2_Object = MibScalar
c1LCompRatAl_2 = _C1LCompRatAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 138),
    _C1LCompRatAl_2_Type()
)
c1LCompRatAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c1LCompRatAl_2.setStatus("current")
_Condenser1Al_2_Type = Integer32
_Condenser1Al_2_Object = MibScalar
condenser1Al_2 = _Condenser1Al_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 139),
    _Condenser1Al_2_Type()
)
condenser1Al_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    condenser1Al_2.setStatus("current")
_C1WatFlowAl_2_Type = Integer32
_C1WatFlowAl_2_Object = MibScalar
c1WatFlowAl_2 = _C1WatFlowAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 140),
    _C1WatFlowAl_2_Type()
)
c1WatFlowAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c1WatFlowAl_2.setStatus("current")
_EEV1GenAl_2_Type = Integer32
_EEV1GenAl_2_Object = MibScalar
eEV1GenAl_2 = _EEV1GenAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 141),
    _EEV1GenAl_2_Type()
)
eEV1GenAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eEV1GenAl_2.setStatus("current")
_EEV1CommAl_2_Type = Integer32
_EEV1CommAl_2_Object = MibScalar
eEV1CommAl_2 = _EEV1CommAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 142),
    _EEV1CommAl_2_Type()
)
eEV1CommAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eEV1CommAl_2.setStatus("current")
_EEV1SuctPrAl_2_Type = Integer32
_EEV1SuctPrAl_2_Object = MibScalar
eEV1SuctPrAl_2 = _EEV1SuctPrAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 143),
    _EEV1SuctPrAl_2_Type()
)
eEV1SuctPrAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eEV1SuctPrAl_2.setStatus("current")
_EEV1EvapPrAl_2_Type = Integer32
_EEV1EvapPrAl_2_Object = MibScalar
eEV1EvapPrAl_2 = _EEV1EvapPrAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 144),
    _EEV1EvapPrAl_2_Type()
)
eEV1EvapPrAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eEV1EvapPrAl_2.setStatus("current")
_EEV1CondPrAl_2_Type = Integer32
_EEV1CondPrAl_2_Object = MibScalar
eEV1CondPrAl_2 = _EEV1CondPrAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 145),
    _EEV1CondPrAl_2_Type()
)
eEV1CondPrAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eEV1CondPrAl_2.setStatus("current")
_EEV1DiscPrAl_2_Type = Integer32
_EEV1DiscPrAl_2_Object = MibScalar
eEV1DiscPrAl_2 = _EEV1DiscPrAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 146),
    _EEV1DiscPrAl_2_Type()
)
eEV1DiscPrAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eEV1DiscPrAl_2.setStatus("current")
_C2ThermAl_2_Type = Integer32
_C2ThermAl_2_Object = MibScalar
c2ThermAl_2 = _C2ThermAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 147),
    _C2ThermAl_2_Type()
)
c2ThermAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2ThermAl_2.setStatus("current")
_C2HighPresAl_2_Type = Integer32
_C2HighPresAl_2_Object = MibScalar
c2HighPresAl_2 = _C2HighPresAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 148),
    _C2HighPresAl_2_Type()
)
c2HighPresAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2HighPresAl_2.setStatus("current")
_C2LowPresAl_2_Type = Integer32
_C2LowPresAl_2_Object = MibScalar
c2LowPresAl_2 = _C2LowPresAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 149),
    _C2LowPresAl_2_Type()
)
c2LowPresAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2LowPresAl_2.setStatus("current")
_C2HighDiscAl_2_Type = Integer32
_C2HighDiscAl_2_Object = MibScalar
c2HighDiscAl_2 = _C2HighDiscAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 150),
    _C2HighDiscAl_2_Type()
)
c2HighDiscAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2HighDiscAl_2.setStatus("current")
_C2LCompRatAl_2_Type = Integer32
_C2LCompRatAl_2_Object = MibScalar
c2LCompRatAl_2 = _C2LCompRatAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 151),
    _C2LCompRatAl_2_Type()
)
c2LCompRatAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2LCompRatAl_2.setStatus("current")
_Condenser2Al_2_Type = Integer32
_Condenser2Al_2_Object = MibScalar
condenser2Al_2 = _Condenser2Al_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 152),
    _Condenser2Al_2_Type()
)
condenser2Al_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    condenser2Al_2.setStatus("current")
_C2WatFlowAl_2_Type = Integer32
_C2WatFlowAl_2_Object = MibScalar
c2WatFlowAl_2 = _C2WatFlowAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 153),
    _C2WatFlowAl_2_Type()
)
c2WatFlowAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2WatFlowAl_2.setStatus("current")
_EEV2GenAl_2_Type = Integer32
_EEV2GenAl_2_Object = MibScalar
eEV2GenAl_2 = _EEV2GenAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 154),
    _EEV2GenAl_2_Type()
)
eEV2GenAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eEV2GenAl_2.setStatus("current")
_EEV2CommAl_2_Type = Integer32
_EEV2CommAl_2_Object = MibScalar
eEV2CommAl_2 = _EEV2CommAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 155),
    _EEV2CommAl_2_Type()
)
eEV2CommAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eEV2CommAl_2.setStatus("current")
_EEV2SuctPrAl_2_Type = Integer32
_EEV2SuctPrAl_2_Object = MibScalar
eEV2SuctPrAl_2 = _EEV2SuctPrAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 156),
    _EEV2SuctPrAl_2_Type()
)
eEV2SuctPrAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eEV2SuctPrAl_2.setStatus("current")
_EEV2EvapPrAl_2_Type = Integer32
_EEV2EvapPrAl_2_Object = MibScalar
eEV2EvapPrAl_2 = _EEV2EvapPrAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 157),
    _EEV2EvapPrAl_2_Type()
)
eEV2EvapPrAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eEV2EvapPrAl_2.setStatus("current")
_EEV2CondPrAl_2_Type = Integer32
_EEV2CondPrAl_2_Object = MibScalar
eEV2CondPrAl_2 = _EEV2CondPrAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 158),
    _EEV2CondPrAl_2_Type()
)
eEV2CondPrAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eEV2CondPrAl_2.setStatus("current")
_EEV2DiscPrAl_2_Type = Integer32
_EEV2DiscPrAl_2_Object = MibScalar
eEV2DiscPrAl_2 = _EEV2DiscPrAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 159),
    _EEV2DiscPrAl_2_Type()
)
eEV2DiscPrAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eEV2DiscPrAl_2.setStatus("current")
_IntHumGenAl_2_Type = Integer32
_IntHumGenAl_2_Object = MibScalar
intHumGenAl_2 = _IntHumGenAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 160),
    _IntHumGenAl_2_Type()
)
intHumGenAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intHumGenAl_2.setStatus("current")
_CPYCommAl_2_Type = Integer32
_CPYCommAl_2_Object = MibScalar
cPYCommAl_2 = _CPYCommAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 161),
    _CPYCommAl_2_Type()
)
cPYCommAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPYCommAl_2.setStatus("current")
_CPYMemoryAl_2_Type = Integer32
_CPYMemoryAl_2_Object = MibScalar
cPYMemoryAl_2 = _CPYMemoryAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 162),
    _CPYMemoryAl_2_Type()
)
cPYMemoryAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPYMemoryAl_2.setStatus("current")
_CPYParamAl_2_Type = Integer32
_CPYParamAl_2_Object = MibScalar
cPYParamAl_2 = _CPYParamAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 163),
    _CPYParamAl_2_Type()
)
cPYParamAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPYParamAl_2.setStatus("current")
_CPYHighCurAl_2_Type = Integer32
_CPYHighCurAl_2_Object = MibScalar
cPYHighCurAl_2 = _CPYHighCurAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 164),
    _CPYHighCurAl_2_Type()
)
cPYHighCurAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPYHighCurAl_2.setStatus("current")
_CPYLoSteamAl_2_Type = Integer32
_CPYLoSteamAl_2_Object = MibScalar
cPYLoSteamAl_2 = _CPYLoSteamAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 165),
    _CPYLoSteamAl_2_Type()
)
cPYLoSteamAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPYLoSteamAl_2.setStatus("current")
_CPYDrainAl_2_Type = Integer32
_CPYDrainAl_2_Object = MibScalar
cPYDrainAl_2 = _CPYDrainAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 166),
    _CPYDrainAl_2_Type()
)
cPYDrainAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPYDrainAl_2.setStatus("current")
_CPYMaintAl_2_Type = Integer32
_CPYMaintAl_2_Object = MibScalar
cPYMaintAl_2 = _CPYMaintAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 167),
    _CPYMaintAl_2_Type()
)
cPYMaintAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPYMaintAl_2.setStatus("current")
_CPYNoWaterAl_2_Type = Integer32
_CPYNoWaterAl_2_Object = MibScalar
cPYNoWaterAl_2 = _CPYNoWaterAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 168),
    _CPYNoWaterAl_2_Type()
)
cPYNoWaterAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPYNoWaterAl_2.setStatus("current")
_CPYCylMainAl_2_Type = Integer32
_CPYCylMainAl_2_Object = MibScalar
cPYCylMainAl_2 = _CPYCylMainAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 169),
    _CPYCylMainAl_2_Type()
)
cPYCylMainAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPYCylMainAl_2.setStatus("current")
_CPYDirtCylAl_2_Type = Integer32
_CPYDirtCylAl_2_Object = MibScalar
cPYDirtCylAl_2 = _CPYDirtCylAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 170),
    _CPYDirtCylAl_2_Type()
)
cPYDirtCylAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPYDirtCylAl_2.setStatus("current")
_CPYFoamAl_2_Type = Integer32
_CPYFoamAl_2_Object = MibScalar
cPYFoamAl_2 = _CPYFoamAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 171),
    _CPYFoamAl_2_Type()
)
cPYFoamAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPYFoamAl_2.setStatus("current")
_CPYLifeTimAl_2_Type = Integer32
_CPYLifeTimAl_2_Object = MibScalar
cPYLifeTimAl_2 = _CPYLifeTimAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 172),
    _CPYLifeTimAl_2_Type()
)
cPYLifeTimAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPYLifeTimAl_2.setStatus("current")
_CPYHiWLevAl_2_Type = Integer32
_CPYHiWLevAl_2_Object = MibScalar
cPYHiWLevAl_2 = _CPYHiWLevAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 173),
    _CPYHiWLevAl_2_Type()
)
cPYHiWLevAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPYHiWLevAl_2.setStatus("current")
_CPYHWatConAl_2_Type = Integer32
_CPYHWatConAl_2_Object = MibScalar
cPYHWatConAl_2 = _CPYHWatConAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 174),
    _CPYHWatConAl_2_Type()
)
cPYHWatConAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPYHWatConAl_2.setStatus("current")
_CPYConnAl_2_Type = Integer32
_CPYConnAl_2_Object = MibScalar
cPYConnAl_2 = _CPYConnAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 175),
    _CPYConnAl_2_Type()
)
cPYConnAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPYConnAl_2.setStatus("current")
_WatPresAl_2_Type = Integer32
_WatPresAl_2_Object = MibScalar
watPresAl_2 = _WatPresAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 176),
    _WatPresAl_2_Type()
)
watPresAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    watPresAl_2.setStatus("current")
_DrainPumpAl_2_Type = Integer32
_DrainPumpAl_2_Object = MibScalar
drainPumpAl_2 = _DrainPumpAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 177),
    _DrainPumpAl_2_Type()
)
drainPumpAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drainPumpAl_2.setStatus("current")
_ElHeatAl_2_Type = Integer32
_ElHeatAl_2_Object = MibScalar
elHeatAl_2 = _ElHeatAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 178),
    _ElHeatAl_2_Type()
)
elHeatAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elHeatAl_2.setStatus("current")
_FilterAl_2_Type = Integer32
_FilterAl_2_Object = MibScalar
filterAl_2 = _FilterAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 179),
    _FilterAl_2_Type()
)
filterAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterAl_2.setStatus("current")
_DryCoolerAl_2_Type = Integer32
_DryCoolerAl_2_Object = MibScalar
dryCoolerAl_2 = _DryCoolerAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 180),
    _DryCoolerAl_2_Type()
)
dryCoolerAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dryCoolerAl_2.setStatus("current")
_ExtHumidAl_2_Type = Integer32
_ExtHumidAl_2_Object = MibScalar
extHumidAl_2 = _ExtHumidAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 181),
    _ExtHumidAl_2_Type()
)
extHumidAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extHumidAl_2.setStatus("current")
_WaterPumpAl_2_Type = Integer32
_WaterPumpAl_2_Object = MibScalar
waterPumpAl_2 = _WaterPumpAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 182),
    _WaterPumpAl_2_Type()
)
waterPumpAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    waterPumpAl_2.setStatus("current")
_CondUnitGAl_2_Type = Integer32
_CondUnitGAl_2_Object = MibScalar
condUnitGAl_2 = _CondUnitGAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 183),
    _CondUnitGAl_2_Type()
)
condUnitGAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    condUnitGAl_2.setStatus("current")
_GasLeakAl_2_Type = Integer32
_GasLeakAl_2_Object = MibScalar
gasLeakAl_2 = _GasLeakAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 184),
    _GasLeakAl_2_Type()
)
gasLeakAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gasLeakAl_2.setStatus("current")
_PowerSuppAl_2_Type = Integer32
_PowerSuppAl_2_Object = MibScalar
powerSuppAl_2 = _PowerSuppAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 185),
    _PowerSuppAl_2_Type()
)
powerSuppAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSuppAl_2.setStatus("current")
_GenSoftAl_2_Type = Integer32
_GenSoftAl_2_Object = MibScalar
genSoftAl_2 = _GenSoftAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 186),
    _GenSoftAl_2_Type()
)
genSoftAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genSoftAl_2.setStatus("current")
_LocalNetAl_2_Type = Integer32
_LocalNetAl_2_Object = MibScalar
localNetAl_2 = _LocalNetAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 187),
    _LocalNetAl_2_Type()
)
localNetAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localNetAl_2.setStatus("current")
_RegHiTempAl_2_Type = Integer32
_RegHiTempAl_2_Object = MibScalar
regHiTempAl_2 = _RegHiTempAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 188),
    _RegHiTempAl_2_Type()
)
regHiTempAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regHiTempAl_2.setStatus("current")
_RegLowTempAl_2_Type = Integer32
_RegLowTempAl_2_Object = MibScalar
regLowTempAl_2 = _RegLowTempAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 189),
    _RegLowTempAl_2_Type()
)
regLowTempAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regLowTempAl_2.setStatus("current")
_HiLimTempAl_2_Type = Integer32
_HiLimTempAl_2_Object = MibScalar
hiLimTempAl_2 = _HiLimTempAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 190),
    _HiLimTempAl_2_Type()
)
hiLimTempAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hiLimTempAl_2.setStatus("current")
_LowLimTempAl_2_Type = Integer32
_LowLimTempAl_2_Object = MibScalar
lowLimTempAl_2 = _LowLimTempAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 191),
    _LowLimTempAl_2_Type()
)
lowLimTempAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowLimTempAl_2.setStatus("current")
_RetHiHumiAl_2_Type = Integer32
_RetHiHumiAl_2_Object = MibScalar
retHiHumiAl_2 = _RetHiHumiAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 192),
    _RetHiHumiAl_2_Type()
)
retHiHumiAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    retHiHumiAl_2.setStatus("current")
_RetLowHumiAl_2_Type = Integer32
_RetLowHumiAl_2_Object = MibScalar
retLowHumiAl_2 = _RetLowHumiAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 193),
    _RetLowHumiAl_2_Type()
)
retLowHumiAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    retLowHumiAl_2.setStatus("current")
_SupHiHumiAl_2_Type = Integer32
_SupHiHumiAl_2_Object = MibScalar
supHiHumiAl_2 = _SupHiHumiAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 194),
    _SupHiHumiAl_2_Type()
)
supHiHumiAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supHiHumiAl_2.setStatus("current")
_SupLowHumiAl_2_Type = Integer32
_SupLowHumiAl_2_Object = MibScalar
supLowHumiAl_2 = _SupLowHumiAl_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 195),
    _SupLowHumiAl_2_Type()
)
supLowHumiAl_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supLowHumiAl_2.setStatus("current")
_ProbeMod1COM_2_Type = Integer32
_ProbeMod1COM_2_Object = MibScalar
probeMod1COM_2 = _ProbeMod1COM_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 196),
    _ProbeMod1COM_2_Type()
)
probeMod1COM_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probeMod1COM_2.setStatus("current")
_PrMod1err1_2_Type = Integer32
_PrMod1err1_2_Object = MibScalar
prMod1err1_2 = _PrMod1err1_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 197),
    _PrMod1err1_2_Type()
)
prMod1err1_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prMod1err1_2.setStatus("current")
_PrMod1err2_2_Type = Integer32
_PrMod1err2_2_Object = MibScalar
prMod1err2_2 = _PrMod1err2_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 198),
    _PrMod1err2_2_Type()
)
prMod1err2_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prMod1err2_2.setStatus("current")
_PrMod1err3_2_Type = Integer32
_PrMod1err3_2_Object = MibScalar
prMod1err3_2 = _PrMod1err3_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 199),
    _PrMod1err3_2_Type()
)
prMod1err3_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prMod1err3_2.setStatus("current")
_PrMod1err4_2_Type = Integer32
_PrMod1err4_2_Object = MibScalar
prMod1err4_2 = _PrMod1err4_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 200),
    _PrMod1err4_2_Type()
)
prMod1err4_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prMod1err4_2.setStatus("current")
_PrMod1err5_2_Type = Integer32
_PrMod1err5_2_Object = MibScalar
prMod1err5_2 = _PrMod1err5_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 201),
    _PrMod1err5_2_Type()
)
prMod1err5_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prMod1err5_2.setStatus("current")
_PrMod1err6_2_Type = Integer32
_PrMod1err6_2_Object = MibScalar
prMod1err6_2 = _PrMod1err6_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 202),
    _PrMod1err6_2_Type()
)
prMod1err6_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prMod1err6_2.setStatus("current")
_ProbeMod2COM_2_Type = Integer32
_ProbeMod2COM_2_Object = MibScalar
probeMod2COM_2 = _ProbeMod2COM_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 203),
    _ProbeMod2COM_2_Type()
)
probeMod2COM_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probeMod2COM_2.setStatus("current")
_PrMod2err1_2_Type = Integer32
_PrMod2err1_2_Object = MibScalar
prMod2err1_2 = _PrMod2err1_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 204),
    _PrMod2err1_2_Type()
)
prMod2err1_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prMod2err1_2.setStatus("current")
_PrMod2err2_2_Type = Integer32
_PrMod2err2_2_Object = MibScalar
prMod2err2_2 = _PrMod2err2_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 205),
    _PrMod2err2_2_Type()
)
prMod2err2_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prMod2err2_2.setStatus("current")
_PrMod2err3_2_Type = Integer32
_PrMod2err3_2_Object = MibScalar
prMod2err3_2 = _PrMod2err3_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 206),
    _PrMod2err3_2_Type()
)
prMod2err3_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prMod2err3_2.setStatus("current")
_PrMod2err4_2_Type = Integer32
_PrMod2err4_2_Object = MibScalar
prMod2err4_2 = _PrMod2err4_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 207),
    _PrMod2err4_2_Type()
)
prMod2err4_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prMod2err4_2.setStatus("current")
_PrMod2err5_2_Type = Integer32
_PrMod2err5_2_Object = MibScalar
prMod2err5_2 = _PrMod2err5_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 208),
    _PrMod2err5_2_Type()
)
prMod2err5_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prMod2err5_2.setStatus("current")
_PrMod2err6_2_Type = Integer32
_PrMod2err6_2_Object = MibScalar
prMod2err6_2 = _PrMod2err6_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 209),
    _PrMod2err6_2_Type()
)
prMod2err6_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prMod2err6_2.setStatus("current")
_ProbeMod3COM_2_Type = Integer32
_ProbeMod3COM_2_Object = MibScalar
probeMod3COM_2 = _ProbeMod3COM_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 210),
    _ProbeMod3COM_2_Type()
)
probeMod3COM_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probeMod3COM_2.setStatus("current")
_PrMod3err1_2_Type = Integer32
_PrMod3err1_2_Object = MibScalar
prMod3err1_2 = _PrMod3err1_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 211),
    _PrMod3err1_2_Type()
)
prMod3err1_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prMod3err1_2.setStatus("current")
_PrMod3err2_2_Type = Integer32
_PrMod3err2_2_Object = MibScalar
prMod3err2_2 = _PrMod3err2_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 212),
    _PrMod3err2_2_Type()
)
prMod3err2_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prMod3err2_2.setStatus("current")
_PrMod3err3_2_Type = Integer32
_PrMod3err3_2_Object = MibScalar
prMod3err3_2 = _PrMod3err3_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 213),
    _PrMod3err3_2_Type()
)
prMod3err3_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prMod3err3_2.setStatus("current")
_PrMod3err4_2_Type = Integer32
_PrMod3err4_2_Object = MibScalar
prMod3err4_2 = _PrMod3err4_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 214),
    _PrMod3err4_2_Type()
)
prMod3err4_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prMod3err4_2.setStatus("current")
_PrMod3err5_2_Type = Integer32
_PrMod3err5_2_Object = MibScalar
prMod3err5_2 = _PrMod3err5_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 215),
    _PrMod3err5_2_Type()
)
prMod3err5_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prMod3err5_2.setStatus("current")
_PrMod3err6_2_Type = Integer32
_PrMod3err6_2_Object = MibScalar
prMod3err6_2 = _PrMod3err6_2_Object(
    (1, 3, 6, 1, 4, 1, 53332, 2, 3, 216),
    _PrMod3err6_2_Type()
)
prMod3err6_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prMod3err6_2.setStatus("current")

# Managed Objects groups


# Notification objects

generalAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 1)
)
generalAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "generalAl_1")
)
if mibBuilder.loadTexts:
    generalAlTrap_1.setStatus(
        "current"
    )

notCriticalAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 2)
)
notCriticalAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "notCriticalAl_1")
)
if mibBuilder.loadTexts:
    notCriticalAlTrap_1.setStatus(
        "current"
    )

criticalAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 3)
)
criticalAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "criticalAl_1")
)
if mibBuilder.loadTexts:
    criticalAlTrap_1.setStatus(
        "current"
    )

fansAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 4)
)
fansAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "fansAl_1")
)
if mibBuilder.loadTexts:
    fansAlTrap_1.setStatus(
        "current"
    )

compAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 5)
)
compAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "compAl_1")
)
if mibBuilder.loadTexts:
    compAlTrap_1.setStatus(
        "current"
    )

temperatureAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 6)
)
temperatureAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "temperatureAl_1")
)
if mibBuilder.loadTexts:
    temperatureAlTrap_1.setStatus(
        "current"
    )

humidityAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 7)
)
humidityAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "humidityAl_1")
)
if mibBuilder.loadTexts:
    humidityAlTrap_1.setStatus(
        "current"
    )

damperAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 8)
)
damperAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "damperAl_1")
)
if mibBuilder.loadTexts:
    damperAlTrap_1.setStatus(
        "current"
    )

fireSmokeAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 9)
)
fireSmokeAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "fireSmokeAl_1")
)
if mibBuilder.loadTexts:
    fireSmokeAlTrap_1.setStatus(
        "current"
    )

genSeriousAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 10)
)
genSeriousAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "genSeriousAl_1")
)
if mibBuilder.loadTexts:
    genSeriousAlTrap_1.setStatus(
        "current"
    )

fansGenAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 11)
)
fansGenAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "fansGenAl_1")
)
if mibBuilder.loadTexts:
    fansGenAlTrap_1.setStatus(
        "current"
    )

f1GeneralAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 12)
)
f1GeneralAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f1GeneralAl_1")
)
if mibBuilder.loadTexts:
    f1GeneralAlTrap_1.setStatus(
        "current"
    )

f1PowerAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 13)
)
f1PowerAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f1PowerAl_1")
)
if mibBuilder.loadTexts:
    f1PowerAlTrap_1.setStatus(
        "current"
    )

f1CommAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 14)
)
f1CommAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f1CommAl_1")
)
if mibBuilder.loadTexts:
    f1CommAlTrap_1.setStatus(
        "current"
    )

f1HighTempAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 15)
)
f1HighTempAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f1HighTempAl_1")
)
if mibBuilder.loadTexts:
    f1HighTempAlTrap_1.setStatus(
        "current"
    )

f1NetComAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 16)
)
f1NetComAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f1NetComAl_1")
)
if mibBuilder.loadTexts:
    f1NetComAlTrap_1.setStatus(
        "current"
    )

f1InvRegAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 17)
)
f1InvRegAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f1InvRegAl_1")
)
if mibBuilder.loadTexts:
    f1InvRegAlTrap_1.setStatus(
        "current"
    )

f1HighMotTempAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 18)
)
f1HighMotTempAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f1HighMotTempAl_1")
)
if mibBuilder.loadTexts:
    f1HighMotTempAlTrap_1.setStatus(
        "current"
    )

f1HallSensAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 19)
)
f1HallSensAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f1HallSensAl_1")
)
if mibBuilder.loadTexts:
    f1HallSensAlTrap_1.setStatus(
        "current"
    )

f1OverloadAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 20)
)
f1OverloadAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f1OverloadAl_1")
)
if mibBuilder.loadTexts:
    f1OverloadAlTrap_1.setStatus(
        "current"
    )

f1LowDCAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 21)
)
f1LowDCAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f1LowDCAl_1")
)
if mibBuilder.loadTexts:
    f1LowDCAlTrap_1.setStatus(
        "current"
    )

f2GeneralAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 22)
)
f2GeneralAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f2GeneralAl_1")
)
if mibBuilder.loadTexts:
    f2GeneralAlTrap_1.setStatus(
        "current"
    )

f2PowerAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 23)
)
f2PowerAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f2PowerAl_1")
)
if mibBuilder.loadTexts:
    f2PowerAlTrap_1.setStatus(
        "current"
    )

f2CommAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 24)
)
f2CommAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f2CommAl_1")
)
if mibBuilder.loadTexts:
    f2CommAlTrap_1.setStatus(
        "current"
    )

f2HighTempAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 25)
)
f2HighTempAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f2HighTempAl_1")
)
if mibBuilder.loadTexts:
    f2HighTempAlTrap_1.setStatus(
        "current"
    )

f2NetComAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 26)
)
f2NetComAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f2NetComAl_1")
)
if mibBuilder.loadTexts:
    f2NetComAlTrap_1.setStatus(
        "current"
    )

f2InvRegAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 27)
)
f2InvRegAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f2InvRegAl_1")
)
if mibBuilder.loadTexts:
    f2InvRegAlTrap_1.setStatus(
        "current"
    )

f2HighMotTempAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 28)
)
f2HighMotTempAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f2HighMotTempAl_1")
)
if mibBuilder.loadTexts:
    f2HighMotTempAlTrap_1.setStatus(
        "current"
    )

f2HallSensAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 29)
)
f2HallSensAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f2HallSensAl_1")
)
if mibBuilder.loadTexts:
    f2HallSensAlTrap_1.setStatus(
        "current"
    )

f2OverloadAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 30)
)
f2OverloadAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f2OverloadAl_1")
)
if mibBuilder.loadTexts:
    f2OverloadAlTrap_1.setStatus(
        "current"
    )

f2LowDCAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 31)
)
f2LowDCAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f2LowDCAl_1")
)
if mibBuilder.loadTexts:
    f2LowDCAlTrap_1.setStatus(
        "current"
    )

f3GeneralAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 32)
)
f3GeneralAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f3GeneralAl_1")
)
if mibBuilder.loadTexts:
    f3GeneralAlTrap_1.setStatus(
        "current"
    )

f3PowerAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 33)
)
f3PowerAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f3PowerAl_1")
)
if mibBuilder.loadTexts:
    f3PowerAlTrap_1.setStatus(
        "current"
    )

f3CommAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 34)
)
f3CommAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f3CommAl_1")
)
if mibBuilder.loadTexts:
    f3CommAlTrap_1.setStatus(
        "current"
    )

f3HighTempAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 35)
)
f3HighTempAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f3HighTempAl_1")
)
if mibBuilder.loadTexts:
    f3HighTempAlTrap_1.setStatus(
        "current"
    )

f3NetComAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 36)
)
f3NetComAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f3NetComAl_1")
)
if mibBuilder.loadTexts:
    f3NetComAlTrap_1.setStatus(
        "current"
    )

f3InvRegAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 37)
)
f3InvRegAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f3InvRegAl_1")
)
if mibBuilder.loadTexts:
    f3InvRegAlTrap_1.setStatus(
        "current"
    )

f3HighMotTempAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 38)
)
f3HighMotTempAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f3HighMotTempAl_1")
)
if mibBuilder.loadTexts:
    f3HighMotTempAlTrap_1.setStatus(
        "current"
    )

f3HallSensAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 39)
)
f3HallSensAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f3HallSensAl_1")
)
if mibBuilder.loadTexts:
    f3HallSensAlTrap_1.setStatus(
        "current"
    )

f3OverloadAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 40)
)
f3OverloadAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f3OverloadAl_1")
)
if mibBuilder.loadTexts:
    f3OverloadAlTrap_1.setStatus(
        "current"
    )

f3LowDCAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 41)
)
f3LowDCAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f3LowDCAl_1")
)
if mibBuilder.loadTexts:
    f3LowDCAlTrap_1.setStatus(
        "current"
    )

f4GeneralAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 42)
)
f4GeneralAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f4GeneralAl_1")
)
if mibBuilder.loadTexts:
    f4GeneralAlTrap_1.setStatus(
        "current"
    )

f4PowerAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 43)
)
f4PowerAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f4PowerAl_1")
)
if mibBuilder.loadTexts:
    f4PowerAlTrap_1.setStatus(
        "current"
    )

f4CommAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 44)
)
f4CommAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f4CommAl_1")
)
if mibBuilder.loadTexts:
    f4CommAlTrap_1.setStatus(
        "current"
    )

f4HighTempAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 45)
)
f4HighTempAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f4HighTempAl_1")
)
if mibBuilder.loadTexts:
    f4HighTempAlTrap_1.setStatus(
        "current"
    )

f4NetComAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 46)
)
f4NetComAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f4NetComAl_1")
)
if mibBuilder.loadTexts:
    f4NetComAlTrap_1.setStatus(
        "current"
    )

f4InvRegAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 47)
)
f4InvRegAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f4InvRegAl_1")
)
if mibBuilder.loadTexts:
    f4InvRegAlTrap_1.setStatus(
        "current"
    )

f4HighMotTempAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 48)
)
f4HighMotTempAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f4HighMotTempAl_1")
)
if mibBuilder.loadTexts:
    f4HighMotTempAlTrap_1.setStatus(
        "current"
    )

f4HallSensAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 49)
)
f4HallSensAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f4HallSensAl_1")
)
if mibBuilder.loadTexts:
    f4HallSensAlTrap_1.setStatus(
        "current"
    )

f4OverloadAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 50)
)
f4OverloadAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f4OverloadAl_1")
)
if mibBuilder.loadTexts:
    f4OverloadAlTrap_1.setStatus(
        "current"
    )

f4LowDCAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 51)
)
f4LowDCAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f4LowDCAl_1")
)
if mibBuilder.loadTexts:
    f4LowDCAlTrap_1.setStatus(
        "current"
    )

f5GeneralAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 52)
)
f5GeneralAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f5GeneralAl_1")
)
if mibBuilder.loadTexts:
    f5GeneralAlTrap_1.setStatus(
        "current"
    )

f5PowerAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 53)
)
f5PowerAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f5PowerAl_1")
)
if mibBuilder.loadTexts:
    f5PowerAlTrap_1.setStatus(
        "current"
    )

f5CommAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 54)
)
f5CommAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f5CommAl_1")
)
if mibBuilder.loadTexts:
    f5CommAlTrap_1.setStatus(
        "current"
    )

f5HighTempAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 55)
)
f5HighTempAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f5HighTempAl_1")
)
if mibBuilder.loadTexts:
    f5HighTempAlTrap_1.setStatus(
        "current"
    )

f5NetComAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 56)
)
f5NetComAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f5NetComAl_1")
)
if mibBuilder.loadTexts:
    f5NetComAlTrap_1.setStatus(
        "current"
    )

f5InvRegAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 57)
)
f5InvRegAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f5InvRegAl_1")
)
if mibBuilder.loadTexts:
    f5InvRegAlTrap_1.setStatus(
        "current"
    )

f5HighMotTempAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 58)
)
f5HighMotTempAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f5HighMotTempAl_1")
)
if mibBuilder.loadTexts:
    f5HighMotTempAlTrap_1.setStatus(
        "current"
    )

f5HallSensAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 59)
)
f5HallSensAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f5HallSensAl_1")
)
if mibBuilder.loadTexts:
    f5HallSensAlTrap_1.setStatus(
        "current"
    )

f5OverloadAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 60)
)
f5OverloadAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f5OverloadAl_1")
)
if mibBuilder.loadTexts:
    f5OverloadAlTrap_1.setStatus(
        "current"
    )

f5LowDCAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 61)
)
f5LowDCAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f5LowDCAl_1")
)
if mibBuilder.loadTexts:
    f5LowDCAlTrap_1.setStatus(
        "current"
    )

f6GeneralAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 62)
)
f6GeneralAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f6GeneralAl_1")
)
if mibBuilder.loadTexts:
    f6GeneralAlTrap_1.setStatus(
        "current"
    )

f6PowerAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 63)
)
f6PowerAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f6PowerAl_1")
)
if mibBuilder.loadTexts:
    f6PowerAlTrap_1.setStatus(
        "current"
    )

f6CommAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 64)
)
f6CommAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f6CommAl_1")
)
if mibBuilder.loadTexts:
    f6CommAlTrap_1.setStatus(
        "current"
    )

f6HighTempAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 65)
)
f6HighTempAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f6HighTempAl_1")
)
if mibBuilder.loadTexts:
    f6HighTempAlTrap_1.setStatus(
        "current"
    )

f6NetComAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 66)
)
f6NetComAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f6NetComAl_1")
)
if mibBuilder.loadTexts:
    f6NetComAlTrap_1.setStatus(
        "current"
    )

f6InvRegAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 67)
)
f6InvRegAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f6InvRegAl_1")
)
if mibBuilder.loadTexts:
    f6InvRegAlTrap_1.setStatus(
        "current"
    )

f6HighMotTempAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 68)
)
f6HighMotTempAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f6HighMotTempAl_1")
)
if mibBuilder.loadTexts:
    f6HighMotTempAlTrap_1.setStatus(
        "current"
    )

f6HallSensAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 69)
)
f6HallSensAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f6HallSensAl_1")
)
if mibBuilder.loadTexts:
    f6HallSensAlTrap_1.setStatus(
        "current"
    )

f6OverloadAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 70)
)
f6OverloadAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f6OverloadAl_1")
)
if mibBuilder.loadTexts:
    f6OverloadAlTrap_1.setStatus(
        "current"
    )

f6LowDCAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 71)
)
f6LowDCAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f6LowDCAl_1")
)
if mibBuilder.loadTexts:
    f6LowDCAlTrap_1.setStatus(
        "current"
    )

f7GeneralAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 72)
)
f7GeneralAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f7GeneralAl_1")
)
if mibBuilder.loadTexts:
    f7GeneralAlTrap_1.setStatus(
        "current"
    )

f7PowerAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 73)
)
f7PowerAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f7PowerAl_1")
)
if mibBuilder.loadTexts:
    f7PowerAlTrap_1.setStatus(
        "current"
    )

f7CommAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 74)
)
f7CommAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f7CommAl_1")
)
if mibBuilder.loadTexts:
    f7CommAlTrap_1.setStatus(
        "current"
    )

f7HighTempAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 75)
)
f7HighTempAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f7HighTempAl_1")
)
if mibBuilder.loadTexts:
    f7HighTempAlTrap_1.setStatus(
        "current"
    )

f7NetComAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 76)
)
f7NetComAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f7NetComAl_1")
)
if mibBuilder.loadTexts:
    f7NetComAlTrap_1.setStatus(
        "current"
    )

f7InvRegAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 77)
)
f7InvRegAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f7InvRegAl_1")
)
if mibBuilder.loadTexts:
    f7InvRegAlTrap_1.setStatus(
        "current"
    )

f7HighMotTempAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 78)
)
f7HighMotTempAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f7HighMotTempAl_1")
)
if mibBuilder.loadTexts:
    f7HighMotTempAlTrap_1.setStatus(
        "current"
    )

f7HallSensAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 79)
)
f7HallSensAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f7HallSensAl_1")
)
if mibBuilder.loadTexts:
    f7HallSensAlTrap_1.setStatus(
        "current"
    )

f7OverloadAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 80)
)
f7OverloadAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f7OverloadAl_1")
)
if mibBuilder.loadTexts:
    f7OverloadAlTrap_1.setStatus(
        "current"
    )

f7LowDCAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 81)
)
f7LowDCAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f7LowDCAl_1")
)
if mibBuilder.loadTexts:
    f7LowDCAlTrap_1.setStatus(
        "current"
    )

f8GeneralAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 82)
)
f8GeneralAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f8GeneralAl_1")
)
if mibBuilder.loadTexts:
    f8GeneralAlTrap_1.setStatus(
        "current"
    )

f8PowerAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 83)
)
f8PowerAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f8PowerAl_1")
)
if mibBuilder.loadTexts:
    f8PowerAlTrap_1.setStatus(
        "current"
    )

f8CommAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 84)
)
f8CommAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f8CommAl_1")
)
if mibBuilder.loadTexts:
    f8CommAlTrap_1.setStatus(
        "current"
    )

f8HighTempAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 85)
)
f8HighTempAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f8HighTempAl_1")
)
if mibBuilder.loadTexts:
    f8HighTempAlTrap_1.setStatus(
        "current"
    )

f8NetComAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 86)
)
f8NetComAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f8NetComAl_1")
)
if mibBuilder.loadTexts:
    f8NetComAlTrap_1.setStatus(
        "current"
    )

f8InvRegAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 87)
)
f8InvRegAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f8InvRegAl_1")
)
if mibBuilder.loadTexts:
    f8InvRegAlTrap_1.setStatus(
        "current"
    )

f8HighMotTempAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 88)
)
f8HighMotTempAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f8HighMotTempAl_1")
)
if mibBuilder.loadTexts:
    f8HighMotTempAlTrap_1.setStatus(
        "current"
    )

f8HallSensAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 89)
)
f8HallSensAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f8HallSensAl_1")
)
if mibBuilder.loadTexts:
    f8HallSensAlTrap_1.setStatus(
        "current"
    )

f8OverloadAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 90)
)
f8OverloadAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f8OverloadAl_1")
)
if mibBuilder.loadTexts:
    f8OverloadAlTrap_1.setStatus(
        "current"
    )

f8LowDCAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 91)
)
f8LowDCAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f8LowDCAl_1")
)
if mibBuilder.loadTexts:
    f8LowDCAlTrap_1.setStatus(
        "current"
    )

f9InverterAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 92)
)
f9InverterAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f9InverterAl_1")
)
if mibBuilder.loadTexts:
    f9InverterAlTrap_1.setStatus(
        "current"
    )

f9PowerAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 93)
)
f9PowerAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f9PowerAl_1")
)
if mibBuilder.loadTexts:
    f9PowerAlTrap_1.setStatus(
        "current"
    )

f9CommAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 94)
)
f9CommAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f9CommAl_1")
)
if mibBuilder.loadTexts:
    f9CommAlTrap_1.setStatus(
        "current"
    )

f9HighTempAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 95)
)
f9HighTempAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f9HighTempAl_1")
)
if mibBuilder.loadTexts:
    f9HighTempAlTrap_1.setStatus(
        "current"
    )

f9NetComAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 96)
)
f9NetComAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f9NetComAl_1")
)
if mibBuilder.loadTexts:
    f9NetComAlTrap_1.setStatus(
        "current"
    )

f9InvRegAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 97)
)
f9InvRegAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f9InvRegAl_1")
)
if mibBuilder.loadTexts:
    f9InvRegAlTrap_1.setStatus(
        "current"
    )

f9HighMotTempAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 98)
)
f9HighMotTempAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f9HighMotTempAl_1")
)
if mibBuilder.loadTexts:
    f9HighMotTempAlTrap_1.setStatus(
        "current"
    )

f9HallSensAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 99)
)
f9HallSensAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f9HallSensAl_1")
)
if mibBuilder.loadTexts:
    f9HallSensAlTrap_1.setStatus(
        "current"
    )

f9OverloadAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 100)
)
f9OverloadAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f9OverloadAl_1")
)
if mibBuilder.loadTexts:
    f9OverloadAlTrap_1.setStatus(
        "current"
    )

f9LowDCAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 101)
)
f9LowDCAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f9LowDCAl_1")
)
if mibBuilder.loadTexts:
    f9LowDCAlTrap_1.setStatus(
        "current"
    )

f10GeneralAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 102)
)
f10GeneralAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f10GeneralAl_1")
)
if mibBuilder.loadTexts:
    f10GeneralAlTrap_1.setStatus(
        "current"
    )

f10PowerAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 103)
)
f10PowerAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f10PowerAl_1")
)
if mibBuilder.loadTexts:
    f10PowerAlTrap_1.setStatus(
        "current"
    )

f10CommAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 104)
)
f10CommAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f10CommAl_1")
)
if mibBuilder.loadTexts:
    f10CommAlTrap_1.setStatus(
        "current"
    )

f10HighTempAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 105)
)
f10HighTempAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f10HighTempAl_1")
)
if mibBuilder.loadTexts:
    f10HighTempAlTrap_1.setStatus(
        "current"
    )

f10NetComAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 106)
)
f10NetComAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f10NetComAl_1")
)
if mibBuilder.loadTexts:
    f10NetComAlTrap_1.setStatus(
        "current"
    )

f10InvRegAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 107)
)
f10InvRegAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f10InvRegAl_1")
)
if mibBuilder.loadTexts:
    f10InvRegAlTrap_1.setStatus(
        "current"
    )

f10HighMotTAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 108)
)
f10HighMotTAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f10HighMotTAl_1")
)
if mibBuilder.loadTexts:
    f10HighMotTAlTrap_1.setStatus(
        "current"
    )

f10HallSensAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 109)
)
f10HallSensAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f10HallSensAl_1")
)
if mibBuilder.loadTexts:
    f10HallSensAlTrap_1.setStatus(
        "current"
    )

f10OverloadAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 110)
)
f10OverloadAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f10OverloadAl_1")
)
if mibBuilder.loadTexts:
    f10OverloadAlTrap_1.setStatus(
        "current"
    )

f10LowDCAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 111)
)
f10LowDCAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "f10LowDCAl_1")
)
if mibBuilder.loadTexts:
    f10LowDCAlTrap_1.setStatus(
        "current"
    )

retTempProbAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 112)
)
retTempProbAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "retTempProbAl_1")
)
if mibBuilder.loadTexts:
    retTempProbAlTrap_1.setStatus(
        "current"
    )

supTempProbAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 113)
)
supTempProbAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "supTempProbAl_1")
)
if mibBuilder.loadTexts:
    supTempProbAlTrap_1.setStatus(
        "current"
    )

retHumProbAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 114)
)
retHumProbAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "retHumProbAl_1")
)
if mibBuilder.loadTexts:
    retHumProbAlTrap_1.setStatus(
        "current"
    )

supHumProbAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 115)
)
supHumProbAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "supHumProbAl_1")
)
if mibBuilder.loadTexts:
    supHumProbAlTrap_1.setStatus(
        "current"
    )

airPrSensorAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 116)
)
airPrSensorAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "airPrSensorAl_1")
)
if mibBuilder.loadTexts:
    airPrSensorAlTrap_1.setStatus(
        "current"
    )

watIN1ProbAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 117)
)
watIN1ProbAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "watIN1ProbAl_1")
)
if mibBuilder.loadTexts:
    watIN1ProbAlTrap_1.setStatus(
        "current"
    )

watOUT1ProbAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 118)
)
watOUT1ProbAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "watOUT1ProbAl_1")
)
if mibBuilder.loadTexts:
    watOUT1ProbAlTrap_1.setStatus(
        "current"
    )

watIN2ProbAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 119)
)
watIN2ProbAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "watIN2ProbAl_1")
)
if mibBuilder.loadTexts:
    watIN2ProbAlTrap_1.setStatus(
        "current"
    )

watOUT2ProbAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 120)
)
watOUT2ProbAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "watOUT2ProbAl_1")
)
if mibBuilder.loadTexts:
    watOUT2ProbAlTrap_1.setStatus(
        "current"
    )

watFlw1ProbAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 121)
)
watFlw1ProbAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "watFlw1ProbAl_1")
)
if mibBuilder.loadTexts:
    watFlw1ProbAlTrap_1.setStatus(
        "current"
    )

watFlw2ProbAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 122)
)
watFlw2ProbAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "watFlw2ProbAl_1")
)
if mibBuilder.loadTexts:
    watFlw2ProbAlTrap_1.setStatus(
        "current"
    )

dFPSGenAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 123)
)
dFPSGenAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "dFPSGenAl_1")
)
if mibBuilder.loadTexts:
    dFPSGenAlTrap_1.setStatus(
        "current"
    )

dFPSBrokenAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 124)
)
dFPSBrokenAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "dFPSBrokenAl_1")
)
if mibBuilder.loadTexts:
    dFPSBrokenAlTrap_1.setStatus(
        "current"
    )

dFPSCablingAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 125)
)
dFPSCablingAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "dFPSCablingAl_1")
)
if mibBuilder.loadTexts:
    dFPSCablingAlTrap_1.setStatus(
        "current"
    )

dFPSRangeAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 126)
)
dFPSRangeAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "dFPSRangeAl_1")
)
if mibBuilder.loadTexts:
    dFPSRangeAlTrap_1.setStatus(
        "current"
    )

dFPSADCAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 127)
)
dFPSADCAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "dFPSADCAl_1")
)
if mibBuilder.loadTexts:
    dFPSADCAlTrap_1.setStatus(
        "current"
    )

dFPSSettingAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 128)
)
dFPSSettingAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "dFPSSettingAl_1")
)
if mibBuilder.loadTexts:
    dFPSSettingAlTrap_1.setStatus(
        "current"
    )

dFPSDCOAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 129)
)
dFPSDCOAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "dFPSDCOAl_1")
)
if mibBuilder.loadTexts:
    dFPSDCOAlTrap_1.setStatus(
        "current"
    )

dFPSWatchdogAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 130)
)
dFPSWatchdogAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "dFPSWatchdogAl_1")
)
if mibBuilder.loadTexts:
    dFPSWatchdogAlTrap_1.setStatus(
        "current"
    )

dFPSCommAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 131)
)
dFPSCommAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "dFPSCommAl_1")
)
if mibBuilder.loadTexts:
    dFPSCommAlTrap_1.setStatus(
        "current"
    )

invCompGenAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 132)
)
invCompGenAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "invCompGenAl_1")
)
if mibBuilder.loadTexts:
    invCompGenAlTrap_1.setStatus(
        "current"
    )

invCompCommAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 133)
)
invCompCommAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "invCompCommAl_1")
)
if mibBuilder.loadTexts:
    invCompCommAlTrap_1.setStatus(
        "current"
    )

invCompAlCode1Trap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 134)
)
invCompAlCode1Trap_1.setObjects(
    ("SNMPSERVER-MIB", "invCompAlCode1_1")
)
if mibBuilder.loadTexts:
    invCompAlCode1Trap_1.setStatus(
        "current"
    )

invCompAlCode2Trap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 135)
)
invCompAlCode2Trap_1.setObjects(
    ("SNMPSERVER-MIB", "invCompAlCode2_1")
)
if mibBuilder.loadTexts:
    invCompAlCode2Trap_1.setStatus(
        "current"
    )

invCompAlCode3Trap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 136)
)
invCompAlCode3Trap_1.setObjects(
    ("SNMPSERVER-MIB", "invCompAlCode3_1")
)
if mibBuilder.loadTexts:
    invCompAlCode3Trap_1.setStatus(
        "current"
    )

invCompAlCode4Trap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 137)
)
invCompAlCode4Trap_1.setObjects(
    ("SNMPSERVER-MIB", "invCompAlCode4_1")
)
if mibBuilder.loadTexts:
    invCompAlCode4Trap_1.setStatus(
        "current"
    )

invCompAlCode5Trap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 138)
)
invCompAlCode5Trap_1.setObjects(
    ("SNMPSERVER-MIB", "invCompAlCode5_1")
)
if mibBuilder.loadTexts:
    invCompAlCode5Trap_1.setStatus(
        "current"
    )

c1ThermAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 139)
)
c1ThermAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "c1ThermAl_1")
)
if mibBuilder.loadTexts:
    c1ThermAlTrap_1.setStatus(
        "current"
    )

c1HighPresAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 140)
)
c1HighPresAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "c1HighPresAl_1")
)
if mibBuilder.loadTexts:
    c1HighPresAlTrap_1.setStatus(
        "current"
    )

c1LowPresAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 141)
)
c1LowPresAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "c1LowPresAl_1")
)
if mibBuilder.loadTexts:
    c1LowPresAlTrap_1.setStatus(
        "current"
    )

c1HighDischAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 142)
)
c1HighDischAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "c1HighDischAl_1")
)
if mibBuilder.loadTexts:
    c1HighDischAlTrap_1.setStatus(
        "current"
    )

c1LCompRatAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 143)
)
c1LCompRatAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "c1LCompRatAl_1")
)
if mibBuilder.loadTexts:
    c1LCompRatAlTrap_1.setStatus(
        "current"
    )

condenser1AlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 144)
)
condenser1AlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "condenser1Al_1")
)
if mibBuilder.loadTexts:
    condenser1AlTrap_1.setStatus(
        "current"
    )

c1WatFlowAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 145)
)
c1WatFlowAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "c1WatFlowAl_1")
)
if mibBuilder.loadTexts:
    c1WatFlowAlTrap_1.setStatus(
        "current"
    )

eEV1GenAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 146)
)
eEV1GenAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "eEV1GenAl_1")
)
if mibBuilder.loadTexts:
    eEV1GenAlTrap_1.setStatus(
        "current"
    )

eEV1CommAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 147)
)
eEV1CommAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "eEV1CommAl_1")
)
if mibBuilder.loadTexts:
    eEV1CommAlTrap_1.setStatus(
        "current"
    )

eEV1SuctProbAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 148)
)
eEV1SuctProbAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "eEV1SuctProbAl_1")
)
if mibBuilder.loadTexts:
    eEV1SuctProbAlTrap_1.setStatus(
        "current"
    )

eEV1EvapProbAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 149)
)
eEV1EvapProbAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "eEV1EvapProbAl_1")
)
if mibBuilder.loadTexts:
    eEV1EvapProbAlTrap_1.setStatus(
        "current"
    )

eEV1CondProbAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 150)
)
eEV1CondProbAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "eEV1CondProbAl_1")
)
if mibBuilder.loadTexts:
    eEV1CondProbAlTrap_1.setStatus(
        "current"
    )

eEV1DischProbAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 151)
)
eEV1DischProbAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "eEV1DischProbAl_1")
)
if mibBuilder.loadTexts:
    eEV1DischProbAlTrap_1.setStatus(
        "current"
    )

c2ThermAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 152)
)
c2ThermAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "c2ThermAl_1")
)
if mibBuilder.loadTexts:
    c2ThermAlTrap_1.setStatus(
        "current"
    )

c2HighPresAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 153)
)
c2HighPresAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "c2HighPresAl_1")
)
if mibBuilder.loadTexts:
    c2HighPresAlTrap_1.setStatus(
        "current"
    )

c2LowPresAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 154)
)
c2LowPresAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "c2LowPresAl_1")
)
if mibBuilder.loadTexts:
    c2LowPresAlTrap_1.setStatus(
        "current"
    )

c2HighDischAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 155)
)
c2HighDischAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "c2HighDischAl_1")
)
if mibBuilder.loadTexts:
    c2HighDischAlTrap_1.setStatus(
        "current"
    )

c2LCompRatAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 156)
)
c2LCompRatAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "c2LCompRatAl_1")
)
if mibBuilder.loadTexts:
    c2LCompRatAlTrap_1.setStatus(
        "current"
    )

condenser2AlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 157)
)
condenser2AlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "condenser2Al_1")
)
if mibBuilder.loadTexts:
    condenser2AlTrap_1.setStatus(
        "current"
    )

c2WatFlowAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 158)
)
c2WatFlowAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "c2WatFlowAl_1")
)
if mibBuilder.loadTexts:
    c2WatFlowAlTrap_1.setStatus(
        "current"
    )

eEV2GenAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 159)
)
eEV2GenAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "eEV2GenAl_1")
)
if mibBuilder.loadTexts:
    eEV2GenAlTrap_1.setStatus(
        "current"
    )

eEV2CommAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 160)
)
eEV2CommAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "eEV2CommAl_1")
)
if mibBuilder.loadTexts:
    eEV2CommAlTrap_1.setStatus(
        "current"
    )

eEV2SuctProbAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 161)
)
eEV2SuctProbAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "eEV2SuctProbAl_1")
)
if mibBuilder.loadTexts:
    eEV2SuctProbAlTrap_1.setStatus(
        "current"
    )

eEV2EvapProbAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 162)
)
eEV2EvapProbAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "eEV2EvapProbAl_1")
)
if mibBuilder.loadTexts:
    eEV2EvapProbAlTrap_1.setStatus(
        "current"
    )

eEV2CondProbAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 163)
)
eEV2CondProbAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "eEV2CondProbAl_1")
)
if mibBuilder.loadTexts:
    eEV2CondProbAlTrap_1.setStatus(
        "current"
    )

eEV2DischProbAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 164)
)
eEV2DischProbAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "eEV2DischProbAl_1")
)
if mibBuilder.loadTexts:
    eEV2DischProbAlTrap_1.setStatus(
        "current"
    )

intHumidGenAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 165)
)
intHumidGenAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "intHumidGenAl_1")
)
if mibBuilder.loadTexts:
    intHumidGenAlTrap_1.setStatus(
        "current"
    )

cPYCommAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 166)
)
cPYCommAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "cPYCommAl_1")
)
if mibBuilder.loadTexts:
    cPYCommAlTrap_1.setStatus(
        "current"
    )

cPYMemoryAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 167)
)
cPYMemoryAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "cPYMemoryAl_1")
)
if mibBuilder.loadTexts:
    cPYMemoryAlTrap_1.setStatus(
        "current"
    )

cPYParameterAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 168)
)
cPYParameterAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "cPYParameterAl_1")
)
if mibBuilder.loadTexts:
    cPYParameterAlTrap_1.setStatus(
        "current"
    )

cPYHighCurrAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 169)
)
cPYHighCurrAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "cPYHighCurrAl_1")
)
if mibBuilder.loadTexts:
    cPYHighCurrAlTrap_1.setStatus(
        "current"
    )

cPYLowSteamAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 170)
)
cPYLowSteamAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "cPYLowSteamAl_1")
)
if mibBuilder.loadTexts:
    cPYLowSteamAlTrap_1.setStatus(
        "current"
    )

cPYDrainAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 171)
)
cPYDrainAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "cPYDrainAl_1")
)
if mibBuilder.loadTexts:
    cPYDrainAlTrap_1.setStatus(
        "current"
    )

cPYMaintAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 172)
)
cPYMaintAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "cPYMaintAl_1")
)
if mibBuilder.loadTexts:
    cPYMaintAlTrap_1.setStatus(
        "current"
    )

cPYNoWaterAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 173)
)
cPYNoWaterAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "cPYNoWaterAl_1")
)
if mibBuilder.loadTexts:
    cPYNoWaterAlTrap_1.setStatus(
        "current"
    )

cPYCylMaintAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 174)
)
cPYCylMaintAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "cPYCylMaintAl_1")
)
if mibBuilder.loadTexts:
    cPYCylMaintAlTrap_1.setStatus(
        "current"
    )

cPYDirtyCylAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 175)
)
cPYDirtyCylAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "cPYDirtyCylAl_1")
)
if mibBuilder.loadTexts:
    cPYDirtyCylAlTrap_1.setStatus(
        "current"
    )

cPYFoamAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 176)
)
cPYFoamAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "cPYFoamAl_1")
)
if mibBuilder.loadTexts:
    cPYFoamAlTrap_1.setStatus(
        "current"
    )

cPYLifeTimeAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 177)
)
cPYLifeTimeAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "cPYLifeTimeAl_1")
)
if mibBuilder.loadTexts:
    cPYLifeTimeAlTrap_1.setStatus(
        "current"
    )

cPYHighWatLevAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 178)
)
cPYHighWatLevAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "cPYHighWatLevAl_1")
)
if mibBuilder.loadTexts:
    cPYHighWatLevAlTrap_1.setStatus(
        "current"
    )

cPYHWatCondAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 179)
)
cPYHWatCondAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "cPYHWatCondAl_1")
)
if mibBuilder.loadTexts:
    cPYHWatCondAlTrap_1.setStatus(
        "current"
    )

cPYConnectionAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 180)
)
cPYConnectionAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "cPYConnectionAl_1")
)
if mibBuilder.loadTexts:
    cPYConnectionAlTrap_1.setStatus(
        "current"
    )

watPresAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 181)
)
watPresAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "watPresAl_1")
)
if mibBuilder.loadTexts:
    watPresAlTrap_1.setStatus(
        "current"
    )

drainPumpAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 182)
)
drainPumpAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "drainPumpAl_1")
)
if mibBuilder.loadTexts:
    drainPumpAlTrap_1.setStatus(
        "current"
    )

elHeatAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 183)
)
elHeatAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "elHeatAl_1")
)
if mibBuilder.loadTexts:
    elHeatAlTrap_1.setStatus(
        "current"
    )

filterAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 184)
)
filterAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "filterAl_1")
)
if mibBuilder.loadTexts:
    filterAlTrap_1.setStatus(
        "current"
    )

dryCoolerAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 185)
)
dryCoolerAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "dryCoolerAl_1")
)
if mibBuilder.loadTexts:
    dryCoolerAlTrap_1.setStatus(
        "current"
    )

extHumidAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 186)
)
extHumidAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "extHumidAl_1")
)
if mibBuilder.loadTexts:
    extHumidAlTrap_1.setStatus(
        "current"
    )

waterPumpAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 187)
)
waterPumpAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "waterPumpAl_1")
)
if mibBuilder.loadTexts:
    waterPumpAlTrap_1.setStatus(
        "current"
    )

condUnitGenAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 188)
)
condUnitGenAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "condUnitGenAl_1")
)
if mibBuilder.loadTexts:
    condUnitGenAlTrap_1.setStatus(
        "current"
    )

gasLeakAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 189)
)
gasLeakAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "gasLeakAl_1")
)
if mibBuilder.loadTexts:
    gasLeakAlTrap_1.setStatus(
        "current"
    )

powerSupplyAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 190)
)
powerSupplyAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "powerSupplyAl_1")
)
if mibBuilder.loadTexts:
    powerSupplyAlTrap_1.setStatus(
        "current"
    )

genericSoftAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 191)
)
genericSoftAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "genericSoftAl_1")
)
if mibBuilder.loadTexts:
    genericSoftAlTrap_1.setStatus(
        "current"
    )

localNetworkAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 192)
)
localNetworkAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "localNetworkAl_1")
)
if mibBuilder.loadTexts:
    localNetworkAlTrap_1.setStatus(
        "current"
    )

regHighTempAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 193)
)
regHighTempAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "regHighTempAl_1")
)
if mibBuilder.loadTexts:
    regHighTempAlTrap_1.setStatus(
        "current"
    )

regLowTempAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 194)
)
regLowTempAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "regLowTempAl_1")
)
if mibBuilder.loadTexts:
    regLowTempAlTrap_1.setStatus(
        "current"
    )

highLimTempAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 195)
)
highLimTempAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "highLimTempAl_1")
)
if mibBuilder.loadTexts:
    highLimTempAlTrap_1.setStatus(
        "current"
    )

lowLimTempAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 196)
)
lowLimTempAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "lowLimTempAl_1")
)
if mibBuilder.loadTexts:
    lowLimTempAlTrap_1.setStatus(
        "current"
    )

retHighHumiAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 197)
)
retHighHumiAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "retHighHumiAl_1")
)
if mibBuilder.loadTexts:
    retHighHumiAlTrap_1.setStatus(
        "current"
    )

retLowHumiAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 198)
)
retLowHumiAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "retLowHumiAl_1")
)
if mibBuilder.loadTexts:
    retLowHumiAlTrap_1.setStatus(
        "current"
    )

supHighHumiAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 199)
)
supHighHumiAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "supHighHumiAl_1")
)
if mibBuilder.loadTexts:
    supHighHumiAlTrap_1.setStatus(
        "current"
    )

supLowHumiAlTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 200)
)
supLowHumiAlTrap_1.setObjects(
    ("SNMPSERVER-MIB", "supLowHumiAl_1")
)
if mibBuilder.loadTexts:
    supLowHumiAlTrap_1.setStatus(
        "current"
    )

probeMod1COMTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 201)
)
probeMod1COMTrap_1.setObjects(
    ("SNMPSERVER-MIB", "probeMod1COM_1")
)
if mibBuilder.loadTexts:
    probeMod1COMTrap_1.setStatus(
        "current"
    )

probeMod1err1Trap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 202)
)
probeMod1err1Trap_1.setObjects(
    ("SNMPSERVER-MIB", "probeMod1err1_1")
)
if mibBuilder.loadTexts:
    probeMod1err1Trap_1.setStatus(
        "current"
    )

probeMod1err2Trap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 203)
)
probeMod1err2Trap_1.setObjects(
    ("SNMPSERVER-MIB", "probeMod1err2_1")
)
if mibBuilder.loadTexts:
    probeMod1err2Trap_1.setStatus(
        "current"
    )

probeMod1err3Trap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 204)
)
probeMod1err3Trap_1.setObjects(
    ("SNMPSERVER-MIB", "probeMod1err3_1")
)
if mibBuilder.loadTexts:
    probeMod1err3Trap_1.setStatus(
        "current"
    )

probeMod1err4Trap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 205)
)
probeMod1err4Trap_1.setObjects(
    ("SNMPSERVER-MIB", "probeMod1err4_1")
)
if mibBuilder.loadTexts:
    probeMod1err4Trap_1.setStatus(
        "current"
    )

probeMod1err5Trap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 206)
)
probeMod1err5Trap_1.setObjects(
    ("SNMPSERVER-MIB", "probeMod1err5_1")
)
if mibBuilder.loadTexts:
    probeMod1err5Trap_1.setStatus(
        "current"
    )

probeMod1err6Trap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 207)
)
probeMod1err6Trap_1.setObjects(
    ("SNMPSERVER-MIB", "probeMod1err6_1")
)
if mibBuilder.loadTexts:
    probeMod1err6Trap_1.setStatus(
        "current"
    )

probeMod2COMTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 208)
)
probeMod2COMTrap_1.setObjects(
    ("SNMPSERVER-MIB", "probeMod2COM_1")
)
if mibBuilder.loadTexts:
    probeMod2COMTrap_1.setStatus(
        "current"
    )

probeMod2err1Trap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 209)
)
probeMod2err1Trap_1.setObjects(
    ("SNMPSERVER-MIB", "probeMod2err1_1")
)
if mibBuilder.loadTexts:
    probeMod2err1Trap_1.setStatus(
        "current"
    )

probeMod2err2Trap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 210)
)
probeMod2err2Trap_1.setObjects(
    ("SNMPSERVER-MIB", "probeMod2err2_1")
)
if mibBuilder.loadTexts:
    probeMod2err2Trap_1.setStatus(
        "current"
    )

probeMod2err3Trap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 211)
)
probeMod2err3Trap_1.setObjects(
    ("SNMPSERVER-MIB", "probeMod2err3_1")
)
if mibBuilder.loadTexts:
    probeMod2err3Trap_1.setStatus(
        "current"
    )

probeMod2err4Trap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 212)
)
probeMod2err4Trap_1.setObjects(
    ("SNMPSERVER-MIB", "probeMod2err4_1")
)
if mibBuilder.loadTexts:
    probeMod2err4Trap_1.setStatus(
        "current"
    )

probeMod2err5Trap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 213)
)
probeMod2err5Trap_1.setObjects(
    ("SNMPSERVER-MIB", "probeMod2err5_1")
)
if mibBuilder.loadTexts:
    probeMod2err5Trap_1.setStatus(
        "current"
    )

probeMod2err6Trap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 214)
)
probeMod2err6Trap_1.setObjects(
    ("SNMPSERVER-MIB", "probeMod2err6_1")
)
if mibBuilder.loadTexts:
    probeMod2err6Trap_1.setStatus(
        "current"
    )

probeMod3COMTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 215)
)
probeMod3COMTrap_1.setObjects(
    ("SNMPSERVER-MIB", "probeMod3COM_1")
)
if mibBuilder.loadTexts:
    probeMod3COMTrap_1.setStatus(
        "current"
    )

probeMod3err1Trap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 216)
)
probeMod3err1Trap_1.setObjects(
    ("SNMPSERVER-MIB", "probeMod3err1_1")
)
if mibBuilder.loadTexts:
    probeMod3err1Trap_1.setStatus(
        "current"
    )

probeMod3err2Trap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 217)
)
probeMod3err2Trap_1.setObjects(
    ("SNMPSERVER-MIB", "probeMod3err2_1")
)
if mibBuilder.loadTexts:
    probeMod3err2Trap_1.setStatus(
        "current"
    )

probeMod3err3Trap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 218)
)
probeMod3err3Trap_1.setObjects(
    ("SNMPSERVER-MIB", "probeMod3err3_1")
)
if mibBuilder.loadTexts:
    probeMod3err3Trap_1.setStatus(
        "current"
    )

probeMod3err4Trap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 219)
)
probeMod3err4Trap_1.setObjects(
    ("SNMPSERVER-MIB", "probeMod3err4_1")
)
if mibBuilder.loadTexts:
    probeMod3err4Trap_1.setStatus(
        "current"
    )

probeMod3err5Trap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 220)
)
probeMod3err5Trap_1.setObjects(
    ("SNMPSERVER-MIB", "probeMod3err5_1")
)
if mibBuilder.loadTexts:
    probeMod3err5Trap_1.setStatus(
        "current"
    )

probeMod3err6Trap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 1, 0, 221)
)
probeMod3err6Trap_1.setObjects(
    ("SNMPSERVER-MIB", "probeMod3err6_1")
)
if mibBuilder.loadTexts:
    probeMod3err6Trap_1.setStatus(
        "current"
    )

generalAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 1)
)
generalAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "generalAl_2")
)
if mibBuilder.loadTexts:
    generalAlTrap_2.setStatus(
        "current"
    )

notCriticalAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 2)
)
notCriticalAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "notCriticalAl_2")
)
if mibBuilder.loadTexts:
    notCriticalAlTrap_2.setStatus(
        "current"
    )

criticalAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 3)
)
criticalAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "criticalAl_2")
)
if mibBuilder.loadTexts:
    criticalAlTrap_2.setStatus(
        "current"
    )

fansAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 4)
)
fansAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "fansAl_2")
)
if mibBuilder.loadTexts:
    fansAlTrap_2.setStatus(
        "current"
    )

compAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 5)
)
compAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "compAl_2")
)
if mibBuilder.loadTexts:
    compAlTrap_2.setStatus(
        "current"
    )

temperatureAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 6)
)
temperatureAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "temperatureAl_2")
)
if mibBuilder.loadTexts:
    temperatureAlTrap_2.setStatus(
        "current"
    )

humidityAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 7)
)
humidityAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "humidityAl_2")
)
if mibBuilder.loadTexts:
    humidityAlTrap_2.setStatus(
        "current"
    )

damperAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 8)
)
damperAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "damperAl_2")
)
if mibBuilder.loadTexts:
    damperAlTrap_2.setStatus(
        "current"
    )

fireSmokeAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 9)
)
fireSmokeAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "fireSmokeAl_2")
)
if mibBuilder.loadTexts:
    fireSmokeAlTrap_2.setStatus(
        "current"
    )

genSeriousAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 10)
)
genSeriousAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "genSeriousAl_2")
)
if mibBuilder.loadTexts:
    genSeriousAlTrap_2.setStatus(
        "current"
    )

fansGenAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 11)
)
fansGenAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "fansGenAl_2")
)
if mibBuilder.loadTexts:
    fansGenAlTrap_2.setStatus(
        "current"
    )

f1GeneralAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 12)
)
f1GeneralAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f1GeneralAl_2")
)
if mibBuilder.loadTexts:
    f1GeneralAlTrap_2.setStatus(
        "current"
    )

f1PowerAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 13)
)
f1PowerAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f1PowerAl_2")
)
if mibBuilder.loadTexts:
    f1PowerAlTrap_2.setStatus(
        "current"
    )

f1CommAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 14)
)
f1CommAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f1CommAl_2")
)
if mibBuilder.loadTexts:
    f1CommAlTrap_2.setStatus(
        "current"
    )

f1HighTempAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 15)
)
f1HighTempAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f1HighTempAl_2")
)
if mibBuilder.loadTexts:
    f1HighTempAlTrap_2.setStatus(
        "current"
    )

f1NetComAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 16)
)
f1NetComAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f1NetComAl_2")
)
if mibBuilder.loadTexts:
    f1NetComAlTrap_2.setStatus(
        "current"
    )

f1InvRegAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 17)
)
f1InvRegAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f1InvRegAl_2")
)
if mibBuilder.loadTexts:
    f1InvRegAlTrap_2.setStatus(
        "current"
    )

f1HighMotTempAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 18)
)
f1HighMotTempAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f1HighMotTempAl_2")
)
if mibBuilder.loadTexts:
    f1HighMotTempAlTrap_2.setStatus(
        "current"
    )

f1HallSensAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 19)
)
f1HallSensAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f1HallSensAl_2")
)
if mibBuilder.loadTexts:
    f1HallSensAlTrap_2.setStatus(
        "current"
    )

f1OverloadAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 20)
)
f1OverloadAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f1OverloadAl_2")
)
if mibBuilder.loadTexts:
    f1OverloadAlTrap_2.setStatus(
        "current"
    )

f1LowDCAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 21)
)
f1LowDCAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f1LowDCAl_2")
)
if mibBuilder.loadTexts:
    f1LowDCAlTrap_2.setStatus(
        "current"
    )

f2GeneralAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 22)
)
f2GeneralAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f2GeneralAl_2")
)
if mibBuilder.loadTexts:
    f2GeneralAlTrap_2.setStatus(
        "current"
    )

f2PowerAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 23)
)
f2PowerAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f2PowerAl_2")
)
if mibBuilder.loadTexts:
    f2PowerAlTrap_2.setStatus(
        "current"
    )

f2CommAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 24)
)
f2CommAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f2CommAl_2")
)
if mibBuilder.loadTexts:
    f2CommAlTrap_2.setStatus(
        "current"
    )

f2HighTempAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 25)
)
f2HighTempAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f2HighTempAl_2")
)
if mibBuilder.loadTexts:
    f2HighTempAlTrap_2.setStatus(
        "current"
    )

f2NetComAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 26)
)
f2NetComAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f2NetComAl_2")
)
if mibBuilder.loadTexts:
    f2NetComAlTrap_2.setStatus(
        "current"
    )

f2InvRegAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 27)
)
f2InvRegAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f2InvRegAl_2")
)
if mibBuilder.loadTexts:
    f2InvRegAlTrap_2.setStatus(
        "current"
    )

f2HighMotTempAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 28)
)
f2HighMotTempAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f2HighMotTempAl_2")
)
if mibBuilder.loadTexts:
    f2HighMotTempAlTrap_2.setStatus(
        "current"
    )

f2HallSensAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 29)
)
f2HallSensAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f2HallSensAl_2")
)
if mibBuilder.loadTexts:
    f2HallSensAlTrap_2.setStatus(
        "current"
    )

f2OverloadAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 30)
)
f2OverloadAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f2OverloadAl_2")
)
if mibBuilder.loadTexts:
    f2OverloadAlTrap_2.setStatus(
        "current"
    )

f2LowDCAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 31)
)
f2LowDCAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f2LowDCAl_2")
)
if mibBuilder.loadTexts:
    f2LowDCAlTrap_2.setStatus(
        "current"
    )

f3GeneralAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 32)
)
f3GeneralAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f3GeneralAl_2")
)
if mibBuilder.loadTexts:
    f3GeneralAlTrap_2.setStatus(
        "current"
    )

f3PowerAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 33)
)
f3PowerAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f3PowerAl_2")
)
if mibBuilder.loadTexts:
    f3PowerAlTrap_2.setStatus(
        "current"
    )

f3CommAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 34)
)
f3CommAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f3CommAl_2")
)
if mibBuilder.loadTexts:
    f3CommAlTrap_2.setStatus(
        "current"
    )

f3HighTempAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 35)
)
f3HighTempAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f3HighTempAl_2")
)
if mibBuilder.loadTexts:
    f3HighTempAlTrap_2.setStatus(
        "current"
    )

f3NetComAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 36)
)
f3NetComAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f3NetComAl_2")
)
if mibBuilder.loadTexts:
    f3NetComAlTrap_2.setStatus(
        "current"
    )

f3InvRegAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 37)
)
f3InvRegAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f3InvRegAl_2")
)
if mibBuilder.loadTexts:
    f3InvRegAlTrap_2.setStatus(
        "current"
    )

f3HighMotTempAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 38)
)
f3HighMotTempAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f3HighMotTempAl_2")
)
if mibBuilder.loadTexts:
    f3HighMotTempAlTrap_2.setStatus(
        "current"
    )

f3HallSensAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 39)
)
f3HallSensAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f3HallSensAl_2")
)
if mibBuilder.loadTexts:
    f3HallSensAlTrap_2.setStatus(
        "current"
    )

f3OverloadAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 40)
)
f3OverloadAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f3OverloadAl_2")
)
if mibBuilder.loadTexts:
    f3OverloadAlTrap_2.setStatus(
        "current"
    )

f3LowDCAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 41)
)
f3LowDCAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f3LowDCAl_2")
)
if mibBuilder.loadTexts:
    f3LowDCAlTrap_2.setStatus(
        "current"
    )

f4GeneralAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 42)
)
f4GeneralAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f4GeneralAl_2")
)
if mibBuilder.loadTexts:
    f4GeneralAlTrap_2.setStatus(
        "current"
    )

f4PowerAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 43)
)
f4PowerAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f4PowerAl_2")
)
if mibBuilder.loadTexts:
    f4PowerAlTrap_2.setStatus(
        "current"
    )

f4CommAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 44)
)
f4CommAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f4CommAl_2")
)
if mibBuilder.loadTexts:
    f4CommAlTrap_2.setStatus(
        "current"
    )

f4HighTempAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 45)
)
f4HighTempAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f4HighTempAl_2")
)
if mibBuilder.loadTexts:
    f4HighTempAlTrap_2.setStatus(
        "current"
    )

f4NetComAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 46)
)
f4NetComAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f4NetComAl_2")
)
if mibBuilder.loadTexts:
    f4NetComAlTrap_2.setStatus(
        "current"
    )

f4InvRegAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 47)
)
f4InvRegAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f4InvRegAl_2")
)
if mibBuilder.loadTexts:
    f4InvRegAlTrap_2.setStatus(
        "current"
    )

f4HighMotTempAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 48)
)
f4HighMotTempAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f4HighMotTempAl_2")
)
if mibBuilder.loadTexts:
    f4HighMotTempAlTrap_2.setStatus(
        "current"
    )

f4HallSensAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 49)
)
f4HallSensAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f4HallSensAl_2")
)
if mibBuilder.loadTexts:
    f4HallSensAlTrap_2.setStatus(
        "current"
    )

f4OverloadAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 50)
)
f4OverloadAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f4OverloadAl_2")
)
if mibBuilder.loadTexts:
    f4OverloadAlTrap_2.setStatus(
        "current"
    )

f4LowDCAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 51)
)
f4LowDCAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f4LowDCAl_2")
)
if mibBuilder.loadTexts:
    f4LowDCAlTrap_2.setStatus(
        "current"
    )

f5GeneralAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 52)
)
f5GeneralAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f5GeneralAl_2")
)
if mibBuilder.loadTexts:
    f5GeneralAlTrap_2.setStatus(
        "current"
    )

f5PowerAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 53)
)
f5PowerAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f5PowerAl_2")
)
if mibBuilder.loadTexts:
    f5PowerAlTrap_2.setStatus(
        "current"
    )

f5CommAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 54)
)
f5CommAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f5CommAl_2")
)
if mibBuilder.loadTexts:
    f5CommAlTrap_2.setStatus(
        "current"
    )

f5HighTempAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 55)
)
f5HighTempAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f5HighTempAl_2")
)
if mibBuilder.loadTexts:
    f5HighTempAlTrap_2.setStatus(
        "current"
    )

f5NetComAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 56)
)
f5NetComAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f5NetComAl_2")
)
if mibBuilder.loadTexts:
    f5NetComAlTrap_2.setStatus(
        "current"
    )

f5InvRegAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 57)
)
f5InvRegAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f5InvRegAl_2")
)
if mibBuilder.loadTexts:
    f5InvRegAlTrap_2.setStatus(
        "current"
    )

f5HighMotTempAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 58)
)
f5HighMotTempAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f5HighMotTempAl_2")
)
if mibBuilder.loadTexts:
    f5HighMotTempAlTrap_2.setStatus(
        "current"
    )

f5HallSensAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 59)
)
f5HallSensAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f5HallSensAl_2")
)
if mibBuilder.loadTexts:
    f5HallSensAlTrap_2.setStatus(
        "current"
    )

f5OverloadAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 60)
)
f5OverloadAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f5OverloadAl_2")
)
if mibBuilder.loadTexts:
    f5OverloadAlTrap_2.setStatus(
        "current"
    )

f5LowDCAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 61)
)
f5LowDCAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f5LowDCAl_2")
)
if mibBuilder.loadTexts:
    f5LowDCAlTrap_2.setStatus(
        "current"
    )

f6GeneralAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 62)
)
f6GeneralAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f6GeneralAl_2")
)
if mibBuilder.loadTexts:
    f6GeneralAlTrap_2.setStatus(
        "current"
    )

f6PowerAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 63)
)
f6PowerAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f6PowerAl_2")
)
if mibBuilder.loadTexts:
    f6PowerAlTrap_2.setStatus(
        "current"
    )

f6CommAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 64)
)
f6CommAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f6CommAl_2")
)
if mibBuilder.loadTexts:
    f6CommAlTrap_2.setStatus(
        "current"
    )

f6HighTempAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 65)
)
f6HighTempAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f6HighTempAl_2")
)
if mibBuilder.loadTexts:
    f6HighTempAlTrap_2.setStatus(
        "current"
    )

f6NetComAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 66)
)
f6NetComAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f6NetComAl_2")
)
if mibBuilder.loadTexts:
    f6NetComAlTrap_2.setStatus(
        "current"
    )

f6InvRegAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 67)
)
f6InvRegAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f6InvRegAl_2")
)
if mibBuilder.loadTexts:
    f6InvRegAlTrap_2.setStatus(
        "current"
    )

f6HighMotTempAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 68)
)
f6HighMotTempAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f6HighMotTempAl_2")
)
if mibBuilder.loadTexts:
    f6HighMotTempAlTrap_2.setStatus(
        "current"
    )

f6HallSensAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 69)
)
f6HallSensAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f6HallSensAl_2")
)
if mibBuilder.loadTexts:
    f6HallSensAlTrap_2.setStatus(
        "current"
    )

f6OverloadAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 70)
)
f6OverloadAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f6OverloadAl_2")
)
if mibBuilder.loadTexts:
    f6OverloadAlTrap_2.setStatus(
        "current"
    )

f6LowDCAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 71)
)
f6LowDCAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f6LowDCAl_2")
)
if mibBuilder.loadTexts:
    f6LowDCAlTrap_2.setStatus(
        "current"
    )

f7GeneralAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 72)
)
f7GeneralAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f7GeneralAl_2")
)
if mibBuilder.loadTexts:
    f7GeneralAlTrap_2.setStatus(
        "current"
    )

f7PowerAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 73)
)
f7PowerAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f7PowerAl_2")
)
if mibBuilder.loadTexts:
    f7PowerAlTrap_2.setStatus(
        "current"
    )

f7CommAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 74)
)
f7CommAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f7CommAl_2")
)
if mibBuilder.loadTexts:
    f7CommAlTrap_2.setStatus(
        "current"
    )

f7HighTempAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 75)
)
f7HighTempAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f7HighTempAl_2")
)
if mibBuilder.loadTexts:
    f7HighTempAlTrap_2.setStatus(
        "current"
    )

f7NetComAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 76)
)
f7NetComAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f7NetComAl_2")
)
if mibBuilder.loadTexts:
    f7NetComAlTrap_2.setStatus(
        "current"
    )

f7InvRegAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 77)
)
f7InvRegAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f7InvRegAl_2")
)
if mibBuilder.loadTexts:
    f7InvRegAlTrap_2.setStatus(
        "current"
    )

f7HighMotTempAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 78)
)
f7HighMotTempAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f7HighMotTempAl_2")
)
if mibBuilder.loadTexts:
    f7HighMotTempAlTrap_2.setStatus(
        "current"
    )

f7HallSensAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 79)
)
f7HallSensAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f7HallSensAl_2")
)
if mibBuilder.loadTexts:
    f7HallSensAlTrap_2.setStatus(
        "current"
    )

f7OverloadAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 80)
)
f7OverloadAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f7OverloadAl_2")
)
if mibBuilder.loadTexts:
    f7OverloadAlTrap_2.setStatus(
        "current"
    )

f7LowDCAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 81)
)
f7LowDCAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f7LowDCAl_2")
)
if mibBuilder.loadTexts:
    f7LowDCAlTrap_2.setStatus(
        "current"
    )

f8GeneralAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 82)
)
f8GeneralAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f8GeneralAl_2")
)
if mibBuilder.loadTexts:
    f8GeneralAlTrap_2.setStatus(
        "current"
    )

f8PowerAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 83)
)
f8PowerAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f8PowerAl_2")
)
if mibBuilder.loadTexts:
    f8PowerAlTrap_2.setStatus(
        "current"
    )

f8CommAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 84)
)
f8CommAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f8CommAl_2")
)
if mibBuilder.loadTexts:
    f8CommAlTrap_2.setStatus(
        "current"
    )

f8HighTempAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 85)
)
f8HighTempAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f8HighTempAl_2")
)
if mibBuilder.loadTexts:
    f8HighTempAlTrap_2.setStatus(
        "current"
    )

f8NetComAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 86)
)
f8NetComAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f8NetComAl_2")
)
if mibBuilder.loadTexts:
    f8NetComAlTrap_2.setStatus(
        "current"
    )

f8InvRegAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 87)
)
f8InvRegAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f8InvRegAl_2")
)
if mibBuilder.loadTexts:
    f8InvRegAlTrap_2.setStatus(
        "current"
    )

f8HighMotTempAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 88)
)
f8HighMotTempAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f8HighMotTempAl_2")
)
if mibBuilder.loadTexts:
    f8HighMotTempAlTrap_2.setStatus(
        "current"
    )

f8HallSensAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 89)
)
f8HallSensAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f8HallSensAl_2")
)
if mibBuilder.loadTexts:
    f8HallSensAlTrap_2.setStatus(
        "current"
    )

f8OverloadAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 90)
)
f8OverloadAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f8OverloadAl_2")
)
if mibBuilder.loadTexts:
    f8OverloadAlTrap_2.setStatus(
        "current"
    )

f8LowDCAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 91)
)
f8LowDCAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f8LowDCAl_2")
)
if mibBuilder.loadTexts:
    f8LowDCAlTrap_2.setStatus(
        "current"
    )

f9InverterAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 92)
)
f9InverterAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f9InverterAl_2")
)
if mibBuilder.loadTexts:
    f9InverterAlTrap_2.setStatus(
        "current"
    )

f9PowerAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 93)
)
f9PowerAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f9PowerAl_2")
)
if mibBuilder.loadTexts:
    f9PowerAlTrap_2.setStatus(
        "current"
    )

f9CommAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 94)
)
f9CommAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f9CommAl_2")
)
if mibBuilder.loadTexts:
    f9CommAlTrap_2.setStatus(
        "current"
    )

f9HighTempAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 95)
)
f9HighTempAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f9HighTempAl_2")
)
if mibBuilder.loadTexts:
    f9HighTempAlTrap_2.setStatus(
        "current"
    )

f9NetComAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 96)
)
f9NetComAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f9NetComAl_2")
)
if mibBuilder.loadTexts:
    f9NetComAlTrap_2.setStatus(
        "current"
    )

f9InvRegAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 97)
)
f9InvRegAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f9InvRegAl_2")
)
if mibBuilder.loadTexts:
    f9InvRegAlTrap_2.setStatus(
        "current"
    )

f9HighMotTempAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 98)
)
f9HighMotTempAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f9HighMotTempAl_2")
)
if mibBuilder.loadTexts:
    f9HighMotTempAlTrap_2.setStatus(
        "current"
    )

f9HallSensAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 99)
)
f9HallSensAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f9HallSensAl_2")
)
if mibBuilder.loadTexts:
    f9HallSensAlTrap_2.setStatus(
        "current"
    )

f9OverloadAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 100)
)
f9OverloadAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f9OverloadAl_2")
)
if mibBuilder.loadTexts:
    f9OverloadAlTrap_2.setStatus(
        "current"
    )

f9LowDCAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 101)
)
f9LowDCAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f9LowDCAl_2")
)
if mibBuilder.loadTexts:
    f9LowDCAlTrap_2.setStatus(
        "current"
    )

f10GeneralAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 102)
)
f10GeneralAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f10GeneralAl_2")
)
if mibBuilder.loadTexts:
    f10GeneralAlTrap_2.setStatus(
        "current"
    )

f10PowerAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 103)
)
f10PowerAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f10PowerAl_2")
)
if mibBuilder.loadTexts:
    f10PowerAlTrap_2.setStatus(
        "current"
    )

f10CommAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 104)
)
f10CommAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f10CommAl_2")
)
if mibBuilder.loadTexts:
    f10CommAlTrap_2.setStatus(
        "current"
    )

f10HighTempAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 105)
)
f10HighTempAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f10HighTempAl_2")
)
if mibBuilder.loadTexts:
    f10HighTempAlTrap_2.setStatus(
        "current"
    )

f10NetComAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 106)
)
f10NetComAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f10NetComAl_2")
)
if mibBuilder.loadTexts:
    f10NetComAlTrap_2.setStatus(
        "current"
    )

f10InvRegAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 107)
)
f10InvRegAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f10InvRegAl_2")
)
if mibBuilder.loadTexts:
    f10InvRegAlTrap_2.setStatus(
        "current"
    )

f10HighMotTAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 108)
)
f10HighMotTAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f10HighMotTAl_2")
)
if mibBuilder.loadTexts:
    f10HighMotTAlTrap_2.setStatus(
        "current"
    )

f10HallSensAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 109)
)
f10HallSensAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f10HallSensAl_2")
)
if mibBuilder.loadTexts:
    f10HallSensAlTrap_2.setStatus(
        "current"
    )

f10OverloadAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 110)
)
f10OverloadAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f10OverloadAl_2")
)
if mibBuilder.loadTexts:
    f10OverloadAlTrap_2.setStatus(
        "current"
    )

f10LowDCAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 111)
)
f10LowDCAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "f10LowDCAl_2")
)
if mibBuilder.loadTexts:
    f10LowDCAlTrap_2.setStatus(
        "current"
    )

retTempProbAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 112)
)
retTempProbAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "retTempProbAl_2")
)
if mibBuilder.loadTexts:
    retTempProbAlTrap_2.setStatus(
        "current"
    )

supTempProbAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 113)
)
supTempProbAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "supTempProbAl_2")
)
if mibBuilder.loadTexts:
    supTempProbAlTrap_2.setStatus(
        "current"
    )

retHumProbAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 114)
)
retHumProbAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "retHumProbAl_2")
)
if mibBuilder.loadTexts:
    retHumProbAlTrap_2.setStatus(
        "current"
    )

supHumProbAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 115)
)
supHumProbAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "supHumProbAl_2")
)
if mibBuilder.loadTexts:
    supHumProbAlTrap_2.setStatus(
        "current"
    )

airPrSensorAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 116)
)
airPrSensorAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "airPrSensorAl_2")
)
if mibBuilder.loadTexts:
    airPrSensorAlTrap_2.setStatus(
        "current"
    )

watIN1ProbAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 117)
)
watIN1ProbAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "watIN1ProbAl_2")
)
if mibBuilder.loadTexts:
    watIN1ProbAlTrap_2.setStatus(
        "current"
    )

watOUT1ProbAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 118)
)
watOUT1ProbAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "watOUT1ProbAl_2")
)
if mibBuilder.loadTexts:
    watOUT1ProbAlTrap_2.setStatus(
        "current"
    )

watIN2ProbAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 119)
)
watIN2ProbAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "watIN2ProbAl_2")
)
if mibBuilder.loadTexts:
    watIN2ProbAlTrap_2.setStatus(
        "current"
    )

watOUT2ProbAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 120)
)
watOUT2ProbAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "watOUT2ProbAl_2")
)
if mibBuilder.loadTexts:
    watOUT2ProbAlTrap_2.setStatus(
        "current"
    )

watFlw1ProbAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 121)
)
watFlw1ProbAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "watFlw1ProbAl_2")
)
if mibBuilder.loadTexts:
    watFlw1ProbAlTrap_2.setStatus(
        "current"
    )

watFlw2ProbAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 122)
)
watFlw2ProbAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "watFlw2ProbAl_2")
)
if mibBuilder.loadTexts:
    watFlw2ProbAlTrap_2.setStatus(
        "current"
    )

dFPSGenAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 123)
)
dFPSGenAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "dFPSGenAl_2")
)
if mibBuilder.loadTexts:
    dFPSGenAlTrap_2.setStatus(
        "current"
    )

dFPSBrokenAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 124)
)
dFPSBrokenAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "dFPSBrokenAl_2")
)
if mibBuilder.loadTexts:
    dFPSBrokenAlTrap_2.setStatus(
        "current"
    )

dFPSCablingAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 125)
)
dFPSCablingAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "dFPSCablingAl_2")
)
if mibBuilder.loadTexts:
    dFPSCablingAlTrap_2.setStatus(
        "current"
    )

dFPSRangeAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 126)
)
dFPSRangeAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "dFPSRangeAl_2")
)
if mibBuilder.loadTexts:
    dFPSRangeAlTrap_2.setStatus(
        "current"
    )

dFPSADCAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 127)
)
dFPSADCAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "dFPSADCAl_2")
)
if mibBuilder.loadTexts:
    dFPSADCAlTrap_2.setStatus(
        "current"
    )

dFPSSettingAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 128)
)
dFPSSettingAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "dFPSSettingAl_2")
)
if mibBuilder.loadTexts:
    dFPSSettingAlTrap_2.setStatus(
        "current"
    )

dFPSDCOAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 129)
)
dFPSDCOAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "dFPSDCOAl_2")
)
if mibBuilder.loadTexts:
    dFPSDCOAlTrap_2.setStatus(
        "current"
    )

dFPSWatchdogAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 130)
)
dFPSWatchdogAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "dFPSWatchdogAl_2")
)
if mibBuilder.loadTexts:
    dFPSWatchdogAlTrap_2.setStatus(
        "current"
    )

dFPSCommAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 131)
)
dFPSCommAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "dFPSCommAl_2")
)
if mibBuilder.loadTexts:
    dFPSCommAlTrap_2.setStatus(
        "current"
    )

invCompGenAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 132)
)
invCompGenAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "invCompGenAl_2")
)
if mibBuilder.loadTexts:
    invCompGenAlTrap_2.setStatus(
        "current"
    )

invCompCommAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 133)
)
invCompCommAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "invCompCommAl_2")
)
if mibBuilder.loadTexts:
    invCompCommAlTrap_2.setStatus(
        "current"
    )

invCompAlCode1Trap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 134)
)
invCompAlCode1Trap_2.setObjects(
    ("SNMPSERVER-MIB", "invCompAlCode1_2")
)
if mibBuilder.loadTexts:
    invCompAlCode1Trap_2.setStatus(
        "current"
    )

invCompAlCode2Trap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 135)
)
invCompAlCode2Trap_2.setObjects(
    ("SNMPSERVER-MIB", "invCompAlCode2_2")
)
if mibBuilder.loadTexts:
    invCompAlCode2Trap_2.setStatus(
        "current"
    )

invCompAlCode3Trap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 136)
)
invCompAlCode3Trap_2.setObjects(
    ("SNMPSERVER-MIB", "invCompAlCode3_2")
)
if mibBuilder.loadTexts:
    invCompAlCode3Trap_2.setStatus(
        "current"
    )

invCompAlCode4Trap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 137)
)
invCompAlCode4Trap_2.setObjects(
    ("SNMPSERVER-MIB", "invCompAlCode4_2")
)
if mibBuilder.loadTexts:
    invCompAlCode4Trap_2.setStatus(
        "current"
    )

invCompAlCode5Trap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 138)
)
invCompAlCode5Trap_2.setObjects(
    ("SNMPSERVER-MIB", "invCompAlCode5_2")
)
if mibBuilder.loadTexts:
    invCompAlCode5Trap_2.setStatus(
        "current"
    )

c1ThermAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 139)
)
c1ThermAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "c1ThermAl_2")
)
if mibBuilder.loadTexts:
    c1ThermAlTrap_2.setStatus(
        "current"
    )

c1HighPresAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 140)
)
c1HighPresAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "c1HighPresAl_2")
)
if mibBuilder.loadTexts:
    c1HighPresAlTrap_2.setStatus(
        "current"
    )

c1LowPresAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 141)
)
c1LowPresAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "c1LowPresAl_2")
)
if mibBuilder.loadTexts:
    c1LowPresAlTrap_2.setStatus(
        "current"
    )

c1HighDischAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 142)
)
c1HighDischAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "c1HighDischAl_2")
)
if mibBuilder.loadTexts:
    c1HighDischAlTrap_2.setStatus(
        "current"
    )

c1LCompRatAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 143)
)
c1LCompRatAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "c1LCompRatAl_2")
)
if mibBuilder.loadTexts:
    c1LCompRatAlTrap_2.setStatus(
        "current"
    )

condenser1AlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 144)
)
condenser1AlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "condenser1Al_2")
)
if mibBuilder.loadTexts:
    condenser1AlTrap_2.setStatus(
        "current"
    )

c1WatFlowAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 145)
)
c1WatFlowAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "c1WatFlowAl_2")
)
if mibBuilder.loadTexts:
    c1WatFlowAlTrap_2.setStatus(
        "current"
    )

eEV1GenAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 146)
)
eEV1GenAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "eEV1GenAl_2")
)
if mibBuilder.loadTexts:
    eEV1GenAlTrap_2.setStatus(
        "current"
    )

eEV1CommAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 147)
)
eEV1CommAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "eEV1CommAl_2")
)
if mibBuilder.loadTexts:
    eEV1CommAlTrap_2.setStatus(
        "current"
    )

eEV1SuctProbAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 148)
)
eEV1SuctProbAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "eEV1SuctProbAl_2")
)
if mibBuilder.loadTexts:
    eEV1SuctProbAlTrap_2.setStatus(
        "current"
    )

eEV1EvapProbAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 149)
)
eEV1EvapProbAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "eEV1EvapProbAl_2")
)
if mibBuilder.loadTexts:
    eEV1EvapProbAlTrap_2.setStatus(
        "current"
    )

eEV1CondProbAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 150)
)
eEV1CondProbAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "eEV1CondProbAl_2")
)
if mibBuilder.loadTexts:
    eEV1CondProbAlTrap_2.setStatus(
        "current"
    )

eEV1DischProbAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 151)
)
eEV1DischProbAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "eEV1DischProbAl_2")
)
if mibBuilder.loadTexts:
    eEV1DischProbAlTrap_2.setStatus(
        "current"
    )

c2ThermAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 152)
)
c2ThermAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "c2ThermAl_2")
)
if mibBuilder.loadTexts:
    c2ThermAlTrap_2.setStatus(
        "current"
    )

c2HighPresAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 153)
)
c2HighPresAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "c2HighPresAl_2")
)
if mibBuilder.loadTexts:
    c2HighPresAlTrap_2.setStatus(
        "current"
    )

c2LowPresAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 154)
)
c2LowPresAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "c2LowPresAl_2")
)
if mibBuilder.loadTexts:
    c2LowPresAlTrap_2.setStatus(
        "current"
    )

c2HighDischAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 155)
)
c2HighDischAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "c2HighDischAl_2")
)
if mibBuilder.loadTexts:
    c2HighDischAlTrap_2.setStatus(
        "current"
    )

c2LCompRatAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 156)
)
c2LCompRatAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "c2LCompRatAl_2")
)
if mibBuilder.loadTexts:
    c2LCompRatAlTrap_2.setStatus(
        "current"
    )

condenser2AlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 157)
)
condenser2AlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "condenser2Al_2")
)
if mibBuilder.loadTexts:
    condenser2AlTrap_2.setStatus(
        "current"
    )

c2WatFlowAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 158)
)
c2WatFlowAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "c2WatFlowAl_2")
)
if mibBuilder.loadTexts:
    c2WatFlowAlTrap_2.setStatus(
        "current"
    )

eEV2GenAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 159)
)
eEV2GenAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "eEV2GenAl_2")
)
if mibBuilder.loadTexts:
    eEV2GenAlTrap_2.setStatus(
        "current"
    )

eEV2CommAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 160)
)
eEV2CommAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "eEV2CommAl_2")
)
if mibBuilder.loadTexts:
    eEV2CommAlTrap_2.setStatus(
        "current"
    )

eEV2SuctProbAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 161)
)
eEV2SuctProbAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "eEV2SuctProbAl_2")
)
if mibBuilder.loadTexts:
    eEV2SuctProbAlTrap_2.setStatus(
        "current"
    )

eEV2EvapProbAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 162)
)
eEV2EvapProbAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "eEV2EvapProbAl_2")
)
if mibBuilder.loadTexts:
    eEV2EvapProbAlTrap_2.setStatus(
        "current"
    )

eEV2CondProbAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 163)
)
eEV2CondProbAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "eEV2CondProbAl_2")
)
if mibBuilder.loadTexts:
    eEV2CondProbAlTrap_2.setStatus(
        "current"
    )

eEV2DischProbAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 164)
)
eEV2DischProbAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "eEV2DischProbAl_2")
)
if mibBuilder.loadTexts:
    eEV2DischProbAlTrap_2.setStatus(
        "current"
    )

intHumidGenAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 165)
)
intHumidGenAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "intHumidGenAl_2")
)
if mibBuilder.loadTexts:
    intHumidGenAlTrap_2.setStatus(
        "current"
    )

cPYCommAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 166)
)
cPYCommAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "cPYCommAl_2")
)
if mibBuilder.loadTexts:
    cPYCommAlTrap_2.setStatus(
        "current"
    )

cPYMemoryAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 167)
)
cPYMemoryAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "cPYMemoryAl_2")
)
if mibBuilder.loadTexts:
    cPYMemoryAlTrap_2.setStatus(
        "current"
    )

cPYParameterAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 168)
)
cPYParameterAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "cPYParameterAl_2")
)
if mibBuilder.loadTexts:
    cPYParameterAlTrap_2.setStatus(
        "current"
    )

cPYHighCurrAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 169)
)
cPYHighCurrAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "cPYHighCurrAl_2")
)
if mibBuilder.loadTexts:
    cPYHighCurrAlTrap_2.setStatus(
        "current"
    )

cPYLowSteamAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 170)
)
cPYLowSteamAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "cPYLowSteamAl_2")
)
if mibBuilder.loadTexts:
    cPYLowSteamAlTrap_2.setStatus(
        "current"
    )

cPYDrainAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 171)
)
cPYDrainAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "cPYDrainAl_2")
)
if mibBuilder.loadTexts:
    cPYDrainAlTrap_2.setStatus(
        "current"
    )

cPYMaintAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 172)
)
cPYMaintAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "cPYMaintAl_2")
)
if mibBuilder.loadTexts:
    cPYMaintAlTrap_2.setStatus(
        "current"
    )

cPYNoWaterAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 173)
)
cPYNoWaterAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "cPYNoWaterAl_2")
)
if mibBuilder.loadTexts:
    cPYNoWaterAlTrap_2.setStatus(
        "current"
    )

cPYCylMaintAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 174)
)
cPYCylMaintAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "cPYCylMaintAl_2")
)
if mibBuilder.loadTexts:
    cPYCylMaintAlTrap_2.setStatus(
        "current"
    )

cPYDirtyCylAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 175)
)
cPYDirtyCylAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "cPYDirtyCylAl_2")
)
if mibBuilder.loadTexts:
    cPYDirtyCylAlTrap_2.setStatus(
        "current"
    )

cPYFoamAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 176)
)
cPYFoamAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "cPYFoamAl_2")
)
if mibBuilder.loadTexts:
    cPYFoamAlTrap_2.setStatus(
        "current"
    )

cPYLifeTimeAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 177)
)
cPYLifeTimeAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "cPYLifeTimeAl_2")
)
if mibBuilder.loadTexts:
    cPYLifeTimeAlTrap_2.setStatus(
        "current"
    )

cPYHighWatLevAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 178)
)
cPYHighWatLevAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "cPYHighWatLevAl_2")
)
if mibBuilder.loadTexts:
    cPYHighWatLevAlTrap_2.setStatus(
        "current"
    )

cPYHWatCondAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 179)
)
cPYHWatCondAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "cPYHWatCondAl_2")
)
if mibBuilder.loadTexts:
    cPYHWatCondAlTrap_2.setStatus(
        "current"
    )

cPYConnectionAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 180)
)
cPYConnectionAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "cPYConnectionAl_2")
)
if mibBuilder.loadTexts:
    cPYConnectionAlTrap_2.setStatus(
        "current"
    )

watPresAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 181)
)
watPresAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "watPresAl_2")
)
if mibBuilder.loadTexts:
    watPresAlTrap_2.setStatus(
        "current"
    )

drainPumpAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 182)
)
drainPumpAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "drainPumpAl_2")
)
if mibBuilder.loadTexts:
    drainPumpAlTrap_2.setStatus(
        "current"
    )

elHeatAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 183)
)
elHeatAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "elHeatAl_2")
)
if mibBuilder.loadTexts:
    elHeatAlTrap_2.setStatus(
        "current"
    )

filterAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 184)
)
filterAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "filterAl_2")
)
if mibBuilder.loadTexts:
    filterAlTrap_2.setStatus(
        "current"
    )

dryCoolerAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 185)
)
dryCoolerAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "dryCoolerAl_2")
)
if mibBuilder.loadTexts:
    dryCoolerAlTrap_2.setStatus(
        "current"
    )

extHumidAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 186)
)
extHumidAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "extHumidAl_2")
)
if mibBuilder.loadTexts:
    extHumidAlTrap_2.setStatus(
        "current"
    )

waterPumpAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 187)
)
waterPumpAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "waterPumpAl_2")
)
if mibBuilder.loadTexts:
    waterPumpAlTrap_2.setStatus(
        "current"
    )

condUnitGenAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 188)
)
condUnitGenAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "condUnitGenAl_2")
)
if mibBuilder.loadTexts:
    condUnitGenAlTrap_2.setStatus(
        "current"
    )

gasLeakAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 189)
)
gasLeakAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "gasLeakAl_2")
)
if mibBuilder.loadTexts:
    gasLeakAlTrap_2.setStatus(
        "current"
    )

powerSupplyAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 190)
)
powerSupplyAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "powerSupplyAl_2")
)
if mibBuilder.loadTexts:
    powerSupplyAlTrap_2.setStatus(
        "current"
    )

genericSoftAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 191)
)
genericSoftAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "genericSoftAl_2")
)
if mibBuilder.loadTexts:
    genericSoftAlTrap_2.setStatus(
        "current"
    )

localNetworkAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 192)
)
localNetworkAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "localNetworkAl_2")
)
if mibBuilder.loadTexts:
    localNetworkAlTrap_2.setStatus(
        "current"
    )

regHighTempAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 193)
)
regHighTempAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "regHighTempAl_2")
)
if mibBuilder.loadTexts:
    regHighTempAlTrap_2.setStatus(
        "current"
    )

regLowTempAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 194)
)
regLowTempAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "regLowTempAl_2")
)
if mibBuilder.loadTexts:
    regLowTempAlTrap_2.setStatus(
        "current"
    )

highLimTempAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 195)
)
highLimTempAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "highLimTempAl_2")
)
if mibBuilder.loadTexts:
    highLimTempAlTrap_2.setStatus(
        "current"
    )

lowLimTempAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 196)
)
lowLimTempAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "lowLimTempAl_2")
)
if mibBuilder.loadTexts:
    lowLimTempAlTrap_2.setStatus(
        "current"
    )

retHighHumiAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 197)
)
retHighHumiAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "retHighHumiAl_2")
)
if mibBuilder.loadTexts:
    retHighHumiAlTrap_2.setStatus(
        "current"
    )

retLowHumiAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 198)
)
retLowHumiAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "retLowHumiAl_2")
)
if mibBuilder.loadTexts:
    retLowHumiAlTrap_2.setStatus(
        "current"
    )

supHighHumiAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 199)
)
supHighHumiAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "supHighHumiAl_2")
)
if mibBuilder.loadTexts:
    supHighHumiAlTrap_2.setStatus(
        "current"
    )

supLowHumiAlTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 200)
)
supLowHumiAlTrap_2.setObjects(
    ("SNMPSERVER-MIB", "supLowHumiAl_2")
)
if mibBuilder.loadTexts:
    supLowHumiAlTrap_2.setStatus(
        "current"
    )

probeMod1COMTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 201)
)
probeMod1COMTrap_2.setObjects(
    ("SNMPSERVER-MIB", "probeMod1COM_2")
)
if mibBuilder.loadTexts:
    probeMod1COMTrap_2.setStatus(
        "current"
    )

probeMod1err1Trap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 202)
)
probeMod1err1Trap_2.setObjects(
    ("SNMPSERVER-MIB", "probeMod1err1_2")
)
if mibBuilder.loadTexts:
    probeMod1err1Trap_2.setStatus(
        "current"
    )

probeMod1err2Trap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 203)
)
probeMod1err2Trap_2.setObjects(
    ("SNMPSERVER-MIB", "probeMod1err2_2")
)
if mibBuilder.loadTexts:
    probeMod1err2Trap_2.setStatus(
        "current"
    )

probeMod1err3Trap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 204)
)
probeMod1err3Trap_2.setObjects(
    ("SNMPSERVER-MIB", "probeMod1err3_2")
)
if mibBuilder.loadTexts:
    probeMod1err3Trap_2.setStatus(
        "current"
    )

probeMod1err4Trap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 205)
)
probeMod1err4Trap_2.setObjects(
    ("SNMPSERVER-MIB", "probeMod1err4_2")
)
if mibBuilder.loadTexts:
    probeMod1err4Trap_2.setStatus(
        "current"
    )

probeMod1err5Trap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 206)
)
probeMod1err5Trap_2.setObjects(
    ("SNMPSERVER-MIB", "probeMod1err5_2")
)
if mibBuilder.loadTexts:
    probeMod1err5Trap_2.setStatus(
        "current"
    )

probeMod1err6Trap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 207)
)
probeMod1err6Trap_2.setObjects(
    ("SNMPSERVER-MIB", "probeMod1err6_2")
)
if mibBuilder.loadTexts:
    probeMod1err6Trap_2.setStatus(
        "current"
    )

probeMod2COMTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 208)
)
probeMod2COMTrap_2.setObjects(
    ("SNMPSERVER-MIB", "probeMod2COM_2")
)
if mibBuilder.loadTexts:
    probeMod2COMTrap_2.setStatus(
        "current"
    )

probeMod2err1Trap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 209)
)
probeMod2err1Trap_2.setObjects(
    ("SNMPSERVER-MIB", "probeMod2err1_2")
)
if mibBuilder.loadTexts:
    probeMod2err1Trap_2.setStatus(
        "current"
    )

probeMod2err2Trap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 210)
)
probeMod2err2Trap_2.setObjects(
    ("SNMPSERVER-MIB", "probeMod2err2_2")
)
if mibBuilder.loadTexts:
    probeMod2err2Trap_2.setStatus(
        "current"
    )

probeMod2err3Trap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 211)
)
probeMod2err3Trap_2.setObjects(
    ("SNMPSERVER-MIB", "probeMod2err3_2")
)
if mibBuilder.loadTexts:
    probeMod2err3Trap_2.setStatus(
        "current"
    )

probeMod2err4Trap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 212)
)
probeMod2err4Trap_2.setObjects(
    ("SNMPSERVER-MIB", "probeMod2err4_2")
)
if mibBuilder.loadTexts:
    probeMod2err4Trap_2.setStatus(
        "current"
    )

probeMod2err5Trap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 213)
)
probeMod2err5Trap_2.setObjects(
    ("SNMPSERVER-MIB", "probeMod2err5_2")
)
if mibBuilder.loadTexts:
    probeMod2err5Trap_2.setStatus(
        "current"
    )

probeMod2err6Trap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 214)
)
probeMod2err6Trap_2.setObjects(
    ("SNMPSERVER-MIB", "probeMod2err6_2")
)
if mibBuilder.loadTexts:
    probeMod2err6Trap_2.setStatus(
        "current"
    )

probeMod3COMTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 215)
)
probeMod3COMTrap_2.setObjects(
    ("SNMPSERVER-MIB", "probeMod3COM_2")
)
if mibBuilder.loadTexts:
    probeMod3COMTrap_2.setStatus(
        "current"
    )

probeMod3err1Trap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 216)
)
probeMod3err1Trap_2.setObjects(
    ("SNMPSERVER-MIB", "probeMod3err1_2")
)
if mibBuilder.loadTexts:
    probeMod3err1Trap_2.setStatus(
        "current"
    )

probeMod3err2Trap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 217)
)
probeMod3err2Trap_2.setObjects(
    ("SNMPSERVER-MIB", "probeMod3err2_2")
)
if mibBuilder.loadTexts:
    probeMod3err2Trap_2.setStatus(
        "current"
    )

probeMod3err3Trap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 218)
)
probeMod3err3Trap_2.setObjects(
    ("SNMPSERVER-MIB", "probeMod3err3_2")
)
if mibBuilder.loadTexts:
    probeMod3err3Trap_2.setStatus(
        "current"
    )

probeMod3err4Trap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 219)
)
probeMod3err4Trap_2.setObjects(
    ("SNMPSERVER-MIB", "probeMod3err4_2")
)
if mibBuilder.loadTexts:
    probeMod3err4Trap_2.setStatus(
        "current"
    )

probeMod3err5Trap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 220)
)
probeMod3err5Trap_2.setObjects(
    ("SNMPSERVER-MIB", "probeMod3err5_2")
)
if mibBuilder.loadTexts:
    probeMod3err5Trap_2.setStatus(
        "current"
    )

probeMod3err6Trap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 53332, 2, 0, 221)
)
probeMod3err6Trap_2.setObjects(
    ("SNMPSERVER-MIB", "probeMod3err6_2")
)
if mibBuilder.loadTexts:
    probeMod3err6Trap_2.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SNMPSERVER-MIB",
    **{"internet": internet,
       "mgmt": mgmt,
       "mib-2": mib_2,
       "system": system,
       "sysDescr": sysDescr,
       "sysObjectID": sysObjectID,
       "sysUpTime": sysUpTime,
       "sysContact": sysContact,
       "sysName": sysName,
       "sysLocation": sysLocation,
       "private": private,
       "enterprises": enterprises,
       "tecnairlv": tecnairlv,
       "node1": node1,
       "traps1": traps1,
       "generalAlTrap_1": generalAlTrap_1,
       "notCriticalAlTrap_1": notCriticalAlTrap_1,
       "criticalAlTrap_1": criticalAlTrap_1,
       "fansAlTrap_1": fansAlTrap_1,
       "compAlTrap_1": compAlTrap_1,
       "temperatureAlTrap_1": temperatureAlTrap_1,
       "humidityAlTrap_1": humidityAlTrap_1,
       "damperAlTrap_1": damperAlTrap_1,
       "fireSmokeAlTrap_1": fireSmokeAlTrap_1,
       "genSeriousAlTrap_1": genSeriousAlTrap_1,
       "fansGenAlTrap_1": fansGenAlTrap_1,
       "f1GeneralAlTrap_1": f1GeneralAlTrap_1,
       "f1PowerAlTrap_1": f1PowerAlTrap_1,
       "f1CommAlTrap_1": f1CommAlTrap_1,
       "f1HighTempAlTrap_1": f1HighTempAlTrap_1,
       "f1NetComAlTrap_1": f1NetComAlTrap_1,
       "f1InvRegAlTrap_1": f1InvRegAlTrap_1,
       "f1HighMotTempAlTrap_1": f1HighMotTempAlTrap_1,
       "f1HallSensAlTrap_1": f1HallSensAlTrap_1,
       "f1OverloadAlTrap_1": f1OverloadAlTrap_1,
       "f1LowDCAlTrap_1": f1LowDCAlTrap_1,
       "f2GeneralAlTrap_1": f2GeneralAlTrap_1,
       "f2PowerAlTrap_1": f2PowerAlTrap_1,
       "f2CommAlTrap_1": f2CommAlTrap_1,
       "f2HighTempAlTrap_1": f2HighTempAlTrap_1,
       "f2NetComAlTrap_1": f2NetComAlTrap_1,
       "f2InvRegAlTrap_1": f2InvRegAlTrap_1,
       "f2HighMotTempAlTrap_1": f2HighMotTempAlTrap_1,
       "f2HallSensAlTrap_1": f2HallSensAlTrap_1,
       "f2OverloadAlTrap_1": f2OverloadAlTrap_1,
       "f2LowDCAlTrap_1": f2LowDCAlTrap_1,
       "f3GeneralAlTrap_1": f3GeneralAlTrap_1,
       "f3PowerAlTrap_1": f3PowerAlTrap_1,
       "f3CommAlTrap_1": f3CommAlTrap_1,
       "f3HighTempAlTrap_1": f3HighTempAlTrap_1,
       "f3NetComAlTrap_1": f3NetComAlTrap_1,
       "f3InvRegAlTrap_1": f3InvRegAlTrap_1,
       "f3HighMotTempAlTrap_1": f3HighMotTempAlTrap_1,
       "f3HallSensAlTrap_1": f3HallSensAlTrap_1,
       "f3OverloadAlTrap_1": f3OverloadAlTrap_1,
       "f3LowDCAlTrap_1": f3LowDCAlTrap_1,
       "f4GeneralAlTrap_1": f4GeneralAlTrap_1,
       "f4PowerAlTrap_1": f4PowerAlTrap_1,
       "f4CommAlTrap_1": f4CommAlTrap_1,
       "f4HighTempAlTrap_1": f4HighTempAlTrap_1,
       "f4NetComAlTrap_1": f4NetComAlTrap_1,
       "f4InvRegAlTrap_1": f4InvRegAlTrap_1,
       "f4HighMotTempAlTrap_1": f4HighMotTempAlTrap_1,
       "f4HallSensAlTrap_1": f4HallSensAlTrap_1,
       "f4OverloadAlTrap_1": f4OverloadAlTrap_1,
       "f4LowDCAlTrap_1": f4LowDCAlTrap_1,
       "f5GeneralAlTrap_1": f5GeneralAlTrap_1,
       "f5PowerAlTrap_1": f5PowerAlTrap_1,
       "f5CommAlTrap_1": f5CommAlTrap_1,
       "f5HighTempAlTrap_1": f5HighTempAlTrap_1,
       "f5NetComAlTrap_1": f5NetComAlTrap_1,
       "f5InvRegAlTrap_1": f5InvRegAlTrap_1,
       "f5HighMotTempAlTrap_1": f5HighMotTempAlTrap_1,
       "f5HallSensAlTrap_1": f5HallSensAlTrap_1,
       "f5OverloadAlTrap_1": f5OverloadAlTrap_1,
       "f5LowDCAlTrap_1": f5LowDCAlTrap_1,
       "f6GeneralAlTrap_1": f6GeneralAlTrap_1,
       "f6PowerAlTrap_1": f6PowerAlTrap_1,
       "f6CommAlTrap_1": f6CommAlTrap_1,
       "f6HighTempAlTrap_1": f6HighTempAlTrap_1,
       "f6NetComAlTrap_1": f6NetComAlTrap_1,
       "f6InvRegAlTrap_1": f6InvRegAlTrap_1,
       "f6HighMotTempAlTrap_1": f6HighMotTempAlTrap_1,
       "f6HallSensAlTrap_1": f6HallSensAlTrap_1,
       "f6OverloadAlTrap_1": f6OverloadAlTrap_1,
       "f6LowDCAlTrap_1": f6LowDCAlTrap_1,
       "f7GeneralAlTrap_1": f7GeneralAlTrap_1,
       "f7PowerAlTrap_1": f7PowerAlTrap_1,
       "f7CommAlTrap_1": f7CommAlTrap_1,
       "f7HighTempAlTrap_1": f7HighTempAlTrap_1,
       "f7NetComAlTrap_1": f7NetComAlTrap_1,
       "f7InvRegAlTrap_1": f7InvRegAlTrap_1,
       "f7HighMotTempAlTrap_1": f7HighMotTempAlTrap_1,
       "f7HallSensAlTrap_1": f7HallSensAlTrap_1,
       "f7OverloadAlTrap_1": f7OverloadAlTrap_1,
       "f7LowDCAlTrap_1": f7LowDCAlTrap_1,
       "f8GeneralAlTrap_1": f8GeneralAlTrap_1,
       "f8PowerAlTrap_1": f8PowerAlTrap_1,
       "f8CommAlTrap_1": f8CommAlTrap_1,
       "f8HighTempAlTrap_1": f8HighTempAlTrap_1,
       "f8NetComAlTrap_1": f8NetComAlTrap_1,
       "f8InvRegAlTrap_1": f8InvRegAlTrap_1,
       "f8HighMotTempAlTrap_1": f8HighMotTempAlTrap_1,
       "f8HallSensAlTrap_1": f8HallSensAlTrap_1,
       "f8OverloadAlTrap_1": f8OverloadAlTrap_1,
       "f8LowDCAlTrap_1": f8LowDCAlTrap_1,
       "f9InverterAlTrap_1": f9InverterAlTrap_1,
       "f9PowerAlTrap_1": f9PowerAlTrap_1,
       "f9CommAlTrap_1": f9CommAlTrap_1,
       "f9HighTempAlTrap_1": f9HighTempAlTrap_1,
       "f9NetComAlTrap_1": f9NetComAlTrap_1,
       "f9InvRegAlTrap_1": f9InvRegAlTrap_1,
       "f9HighMotTempAlTrap_1": f9HighMotTempAlTrap_1,
       "f9HallSensAlTrap_1": f9HallSensAlTrap_1,
       "f9OverloadAlTrap_1": f9OverloadAlTrap_1,
       "f9LowDCAlTrap_1": f9LowDCAlTrap_1,
       "f10GeneralAlTrap_1": f10GeneralAlTrap_1,
       "f10PowerAlTrap_1": f10PowerAlTrap_1,
       "f10CommAlTrap_1": f10CommAlTrap_1,
       "f10HighTempAlTrap_1": f10HighTempAlTrap_1,
       "f10NetComAlTrap_1": f10NetComAlTrap_1,
       "f10InvRegAlTrap_1": f10InvRegAlTrap_1,
       "f10HighMotTAlTrap_1": f10HighMotTAlTrap_1,
       "f10HallSensAlTrap_1": f10HallSensAlTrap_1,
       "f10OverloadAlTrap_1": f10OverloadAlTrap_1,
       "f10LowDCAlTrap_1": f10LowDCAlTrap_1,
       "retTempProbAlTrap_1": retTempProbAlTrap_1,
       "supTempProbAlTrap_1": supTempProbAlTrap_1,
       "retHumProbAlTrap_1": retHumProbAlTrap_1,
       "supHumProbAlTrap_1": supHumProbAlTrap_1,
       "airPrSensorAlTrap_1": airPrSensorAlTrap_1,
       "watIN1ProbAlTrap_1": watIN1ProbAlTrap_1,
       "watOUT1ProbAlTrap_1": watOUT1ProbAlTrap_1,
       "watIN2ProbAlTrap_1": watIN2ProbAlTrap_1,
       "watOUT2ProbAlTrap_1": watOUT2ProbAlTrap_1,
       "watFlw1ProbAlTrap_1": watFlw1ProbAlTrap_1,
       "watFlw2ProbAlTrap_1": watFlw2ProbAlTrap_1,
       "dFPSGenAlTrap_1": dFPSGenAlTrap_1,
       "dFPSBrokenAlTrap_1": dFPSBrokenAlTrap_1,
       "dFPSCablingAlTrap_1": dFPSCablingAlTrap_1,
       "dFPSRangeAlTrap_1": dFPSRangeAlTrap_1,
       "dFPSADCAlTrap_1": dFPSADCAlTrap_1,
       "dFPSSettingAlTrap_1": dFPSSettingAlTrap_1,
       "dFPSDCOAlTrap_1": dFPSDCOAlTrap_1,
       "dFPSWatchdogAlTrap_1": dFPSWatchdogAlTrap_1,
       "dFPSCommAlTrap_1": dFPSCommAlTrap_1,
       "invCompGenAlTrap_1": invCompGenAlTrap_1,
       "invCompCommAlTrap_1": invCompCommAlTrap_1,
       "invCompAlCode1Trap_1": invCompAlCode1Trap_1,
       "invCompAlCode2Trap_1": invCompAlCode2Trap_1,
       "invCompAlCode3Trap_1": invCompAlCode3Trap_1,
       "invCompAlCode4Trap_1": invCompAlCode4Trap_1,
       "invCompAlCode5Trap_1": invCompAlCode5Trap_1,
       "c1ThermAlTrap_1": c1ThermAlTrap_1,
       "c1HighPresAlTrap_1": c1HighPresAlTrap_1,
       "c1LowPresAlTrap_1": c1LowPresAlTrap_1,
       "c1HighDischAlTrap_1": c1HighDischAlTrap_1,
       "c1LCompRatAlTrap_1": c1LCompRatAlTrap_1,
       "condenser1AlTrap_1": condenser1AlTrap_1,
       "c1WatFlowAlTrap_1": c1WatFlowAlTrap_1,
       "eEV1GenAlTrap_1": eEV1GenAlTrap_1,
       "eEV1CommAlTrap_1": eEV1CommAlTrap_1,
       "eEV1SuctProbAlTrap_1": eEV1SuctProbAlTrap_1,
       "eEV1EvapProbAlTrap_1": eEV1EvapProbAlTrap_1,
       "eEV1CondProbAlTrap_1": eEV1CondProbAlTrap_1,
       "eEV1DischProbAlTrap_1": eEV1DischProbAlTrap_1,
       "c2ThermAlTrap_1": c2ThermAlTrap_1,
       "c2HighPresAlTrap_1": c2HighPresAlTrap_1,
       "c2LowPresAlTrap_1": c2LowPresAlTrap_1,
       "c2HighDischAlTrap_1": c2HighDischAlTrap_1,
       "c2LCompRatAlTrap_1": c2LCompRatAlTrap_1,
       "condenser2AlTrap_1": condenser2AlTrap_1,
       "c2WatFlowAlTrap_1": c2WatFlowAlTrap_1,
       "eEV2GenAlTrap_1": eEV2GenAlTrap_1,
       "eEV2CommAlTrap_1": eEV2CommAlTrap_1,
       "eEV2SuctProbAlTrap_1": eEV2SuctProbAlTrap_1,
       "eEV2EvapProbAlTrap_1": eEV2EvapProbAlTrap_1,
       "eEV2CondProbAlTrap_1": eEV2CondProbAlTrap_1,
       "eEV2DischProbAlTrap_1": eEV2DischProbAlTrap_1,
       "intHumidGenAlTrap_1": intHumidGenAlTrap_1,
       "cPYCommAlTrap_1": cPYCommAlTrap_1,
       "cPYMemoryAlTrap_1": cPYMemoryAlTrap_1,
       "cPYParameterAlTrap_1": cPYParameterAlTrap_1,
       "cPYHighCurrAlTrap_1": cPYHighCurrAlTrap_1,
       "cPYLowSteamAlTrap_1": cPYLowSteamAlTrap_1,
       "cPYDrainAlTrap_1": cPYDrainAlTrap_1,
       "cPYMaintAlTrap_1": cPYMaintAlTrap_1,
       "cPYNoWaterAlTrap_1": cPYNoWaterAlTrap_1,
       "cPYCylMaintAlTrap_1": cPYCylMaintAlTrap_1,
       "cPYDirtyCylAlTrap_1": cPYDirtyCylAlTrap_1,
       "cPYFoamAlTrap_1": cPYFoamAlTrap_1,
       "cPYLifeTimeAlTrap_1": cPYLifeTimeAlTrap_1,
       "cPYHighWatLevAlTrap_1": cPYHighWatLevAlTrap_1,
       "cPYHWatCondAlTrap_1": cPYHWatCondAlTrap_1,
       "cPYConnectionAlTrap_1": cPYConnectionAlTrap_1,
       "watPresAlTrap_1": watPresAlTrap_1,
       "drainPumpAlTrap_1": drainPumpAlTrap_1,
       "elHeatAlTrap_1": elHeatAlTrap_1,
       "filterAlTrap_1": filterAlTrap_1,
       "dryCoolerAlTrap_1": dryCoolerAlTrap_1,
       "extHumidAlTrap_1": extHumidAlTrap_1,
       "waterPumpAlTrap_1": waterPumpAlTrap_1,
       "condUnitGenAlTrap_1": condUnitGenAlTrap_1,
       "gasLeakAlTrap_1": gasLeakAlTrap_1,
       "powerSupplyAlTrap_1": powerSupplyAlTrap_1,
       "genericSoftAlTrap_1": genericSoftAlTrap_1,
       "localNetworkAlTrap_1": localNetworkAlTrap_1,
       "regHighTempAlTrap_1": regHighTempAlTrap_1,
       "regLowTempAlTrap_1": regLowTempAlTrap_1,
       "highLimTempAlTrap_1": highLimTempAlTrap_1,
       "lowLimTempAlTrap_1": lowLimTempAlTrap_1,
       "retHighHumiAlTrap_1": retHighHumiAlTrap_1,
       "retLowHumiAlTrap_1": retLowHumiAlTrap_1,
       "supHighHumiAlTrap_1": supHighHumiAlTrap_1,
       "supLowHumiAlTrap_1": supLowHumiAlTrap_1,
       "probeMod1COMTrap_1": probeMod1COMTrap_1,
       "probeMod1err1Trap_1": probeMod1err1Trap_1,
       "probeMod1err2Trap_1": probeMod1err2Trap_1,
       "probeMod1err3Trap_1": probeMod1err3Trap_1,
       "probeMod1err4Trap_1": probeMod1err4Trap_1,
       "probeMod1err5Trap_1": probeMod1err5Trap_1,
       "probeMod1err6Trap_1": probeMod1err6Trap_1,
       "probeMod2COMTrap_1": probeMod2COMTrap_1,
       "probeMod2err1Trap_1": probeMod2err1Trap_1,
       "probeMod2err2Trap_1": probeMod2err2Trap_1,
       "probeMod2err3Trap_1": probeMod2err3Trap_1,
       "probeMod2err4Trap_1": probeMod2err4Trap_1,
       "probeMod2err5Trap_1": probeMod2err5Trap_1,
       "probeMod2err6Trap_1": probeMod2err6Trap_1,
       "probeMod3COMTrap_1": probeMod3COMTrap_1,
       "probeMod3err1Trap_1": probeMod3err1Trap_1,
       "probeMod3err2Trap_1": probeMod3err2Trap_1,
       "probeMod3err3Trap_1": probeMod3err3Trap_1,
       "probeMod3err4Trap_1": probeMod3err4Trap_1,
       "probeMod3err5Trap_1": probeMod3err5Trap_1,
       "probeMod3err6Trap_1": probeMod3err6Trap_1,
       "binaryObjects1": binaryObjects1,
       "damperStatusDI_1": damperStatusDI_1,
       "dirtyFilterDI_1": dirtyFilterDI_1,
       "remoteOffDI_1": remoteOffDI_1,
       "elHeaterAlarmDI_1": elHeaterAlarmDI_1,
       "condPumpAlarmDI_1": condPumpAlarmDI_1,
       "configurableDI1_1": configurableDI1_1,
       "configurableDI2_1": configurableDI2_1,
       "configurableDI3_1": configurableDI3_1,
       "configurableDI4_1": configurableDI4_1,
       "configurableDI5_1": configurableDI5_1,
       "c1ThermAlarmDI_1": c1ThermAlarmDI_1,
       "c1HPAlarmDI_1": c1HPAlarmDI_1,
       "c1LPAlarmDI_1": c1LPAlarmDI_1,
       "c2ThermAlarmDI_1": c2ThermAlarmDI_1,
       "c2HPAlarmDI_1": c2HPAlarmDI_1,
       "c2LPAlarmDI_1": c2LPAlarmDI_1,
       "fansDO_1": fansDO_1,
       "damperDO_1": damperDO_1,
       "configurableDO1_1": configurableDO1_1,
       "configurableDO2_1": configurableDO2_1,
       "configurableDO3_1": configurableDO3_1,
       "configurableDO4_1": configurableDO4_1,
       "configurableDO5_1": configurableDO5_1,
       "eHeaterStage1DO_1": eHeaterStage1DO_1,
       "eHeaterStage2DO_1": eHeaterStage2DO_1,
       "compressor1DO_1": compressor1DO_1,
       "compressor2DO_1": compressor2DO_1,
       "humPowerDO_1": humPowerDO_1,
       "humDrainValveDO_1": humDrainValveDO_1,
       "humFillValveDO_1": humFillValveDO_1,
       "humWaterLevel_1": humWaterLevel_1,
       "supervOFF_1": supervOFF_1,
       "enableHumid_1": enableHumid_1,
       "humManualDrain_1": humManualDrain_1,
       "humCylWashing_1": humCylWashing_1,
       "tSManExchange_1": tSManExchange_1,
       "tSTempExchEnab_1": tSTempExchEnab_1,
       "damperAlRes_1": damperAlRes_1,
       "fireSmokeAlRes_1": fireSmokeAlRes_1,
       "genSerAlRes_1": genSerAlRes_1,
       "fansGenAlRes_1": fansGenAlRes_1,
       "f1InvAlRes_1": f1InvAlRes_1,
       "f2InvAlRes_1": f2InvAlRes_1,
       "f3InvAlRes_1": f3InvAlRes_1,
       "f4InvAlRes_1": f4InvAlRes_1,
       "f5InvAlRes_1": f5InvAlRes_1,
       "f6InvAlRes_1": f6InvAlRes_1,
       "f7InvAlRes_1": f7InvAlRes_1,
       "f8InvAlRes_1": f8InvAlRes_1,
       "f9InvAlRes_1": f9InvAlRes_1,
       "f10InvAlRes_1": f10InvAlRes_1,
       "invCompAlRes_1": invCompAlRes_1,
       "c1ThermAlRes_1": c1ThermAlRes_1,
       "c1HighPresAlRes_1": c1HighPresAlRes_1,
       "c1LowPresAlRes_1": c1LowPresAlRes_1,
       "c1HighDisTAlRes_1": c1HighDisTAlRes_1,
       "c1LCompRatAlRes_1": c1LCompRatAlRes_1,
       "condenser1AlRes_1": condenser1AlRes_1,
       "eEV1AlRes_1": eEV1AlRes_1,
       "c2ThermAlRes_1": c2ThermAlRes_1,
       "c2HighPresAlRes_1": c2HighPresAlRes_1,
       "c2LowPresAlRes_1": c2LowPresAlRes_1,
       "c2HighDisTAlRes_1": c2HighDisTAlRes_1,
       "c2LComRatAlRes_1": c2LComRatAlRes_1,
       "condenser2AlRes_1": condenser2AlRes_1,
       "eEV2AlRes_1": eEV2AlRes_1,
       "intHumidifAlRes_1": intHumidifAlRes_1,
       "watPresAlRes_1": watPresAlRes_1,
       "drainPumpAlRes_1": drainPumpAlRes_1,
       "elHeatAlRes_1": elHeatAlRes_1,
       "filterAlRes_1": filterAlRes_1,
       "dryCoolerAlRes_1": dryCoolerAlRes_1,
       "extHumidifAlRes_1": extHumidifAlRes_1,
       "waterPumpAlRes_1": waterPumpAlRes_1,
       "condUnitGAlRes_1": condUnitGAlRes_1,
       "gasLeakAlRes_1": gasLeakAlRes_1,
       "powerSupAlRes_1": powerSupAlRes_1,
       "genSoftAlRes_1": genSoftAlRes_1,
       "scalarsObjects1": scalarsObjects1,
       "confDI1Combo_1": confDI1Combo_1,
       "confDI2Combo_1": confDI2Combo_1,
       "confDI3Combo_1": confDI3Combo_1,
       "confDI4Combo_1": confDI4Combo_1,
       "confDI5Combo_1": confDI5Combo_1,
       "confDO1Combo_1": confDO1Combo_1,
       "confDO2Combo_1": confDO2Combo_1,
       "confDO3Combo_1": confDO3Combo_1,
       "confDO4Combo_1": confDO4Combo_1,
       "confDO5Combo_1": confDO5Combo_1,
       "returnTemp_1": returnTemp_1,
       "returnTAvg_1": returnTAvg_1,
       "supplyTemp_1": supplyTemp_1,
       "supplyTAvg_1": supplyTAvg_1,
       "tempDelta_1": tempDelta_1,
       "returnHumidity_1": returnHumidity_1,
       "returnHumAvg_1": returnHumAvg_1,
       "supplyHumidity_1": supplyHumidity_1,
       "supplyHumAvg_1": supplyHumAvg_1,
       "airFlow_1": airFlow_1,
       "airPressure_1": airPressure_1,
       "airPressureAvg_1": airPressureAvg_1,
       "netMod1Combo1_1": netMod1Combo1_1,
       "netMod1Probe1_1": netMod1Probe1_1,
       "netMod1Combo2_1": netMod1Combo2_1,
       "netMod1Probe2_1": netMod1Probe2_1,
       "netMod1Combo3_1": netMod1Combo3_1,
       "netMod1Probe3_1": netMod1Probe3_1,
       "netMod1Combo4_1": netMod1Combo4_1,
       "netMod1Probe4_1": netMod1Probe4_1,
       "netMod1Combo5_1": netMod1Combo5_1,
       "netMod1Probe5_1": netMod1Probe5_1,
       "netMod1Combo6_1": netMod1Combo6_1,
       "netMod1Probe6_1": netMod1Probe6_1,
       "netMod2Combo1_1": netMod2Combo1_1,
       "netMod2Probe1_1": netMod2Probe1_1,
       "netMod2Combo2_1": netMod2Combo2_1,
       "netMod2Probe2_1": netMod2Probe2_1,
       "netMod2Combo3_1": netMod2Combo3_1,
       "netMod2Probe3_1": netMod2Probe3_1,
       "netMod2Combo4_1": netMod2Combo4_1,
       "netMod2Probe4_1": netMod2Probe4_1,
       "netMod2Combo5_1": netMod2Combo5_1,
       "netMod2Probe5_1": netMod2Probe5_1,
       "netMod2Combo6_1": netMod2Combo6_1,
       "netMod2Probe6_1": netMod2Probe6_1,
       "netMod3Combo1_1": netMod3Combo1_1,
       "netMod3Probe1_1": netMod3Probe1_1,
       "netMod3Combo2_1": netMod3Combo2_1,
       "netMod3Probe2_1": netMod3Probe2_1,
       "netMod3Combo3_1": netMod3Combo3_1,
       "netMod3Probe3_1": netMod3Probe3_1,
       "netMod3Combo4_1": netMod3Combo4_1,
       "netMod3Probe4_1": netMod3Probe4_1,
       "netMod3Combo5_1": netMod3Combo5_1,
       "netMod3Probe5_1": netMod3Probe5_1,
       "netMod3Combo6_1": netMod3Combo6_1,
       "netMod3Probe6_1": netMod3Probe6_1,
       "avgModTemp_1": avgModTemp_1,
       "avgModHumi_1": avgModHumi_1,
       "avgModPress_1": avgModPress_1,
       "dryCoolerAO_1": dryCoolerAO_1,
       "coolingAO_1": coolingAO_1,
       "heatingAO_1": heatingAO_1,
       "twoSources2AO_1": twoSources2AO_1,
       "condenser1AO_1": condenser1AO_1,
       "cond2HumidifAO_1": cond2HumidifAO_1,
       "unitStatus_1": unitStatus_1,
       "fanSpeed_1": fanSpeed_1,
       "fan1Actspeed_1": fan1Actspeed_1,
       "fan1ActRPM_1": fan1ActRPM_1,
       "fan1Cur_1": fan1Cur_1,
       "fan1Power_1": fan1Power_1,
       "fan2Actspeed_1": fan2Actspeed_1,
       "fan2ActRPM_1": fan2ActRPM_1,
       "fan2Cur_1": fan2Cur_1,
       "fan2Power_1": fan2Power_1,
       "fan3Actspeed_1": fan3Actspeed_1,
       "fan3ActRPM_1": fan3ActRPM_1,
       "fan3Cur_1": fan3Cur_1,
       "fan3Power_1": fan3Power_1,
       "fan4Actspeed_1": fan4Actspeed_1,
       "fan4ActRPM_1": fan4ActRPM_1,
       "fan4Cur_1": fan4Cur_1,
       "fan4Power_1": fan4Power_1,
       "fan5Actspeed_1": fan5Actspeed_1,
       "fan5ActRPM_1": fan5ActRPM_1,
       "fan5Cur_1": fan5Cur_1,
       "fan5Power_1": fan5Power_1,
       "fan6Actspeed_1": fan6Actspeed_1,
       "fan6ActRPM_1": fan6ActRPM_1,
       "fan6Cur_1": fan6Cur_1,
       "fan6Power_1": fan6Power_1,
       "fan7Actspeed_1": fan7Actspeed_1,
       "fan7ActRPM_1": fan7ActRPM_1,
       "fan7Cur_1": fan7Cur_1,
       "fan7Power_1": fan7Power_1,
       "fan8Actspeed_1": fan8Actspeed_1,
       "fan8ActRPM_1": fan8ActRPM_1,
       "fan8Cur_1": fan8Cur_1,
       "fan8Power_1": fan8Power_1,
       "fan9Actspeed_1": fan9Actspeed_1,
       "fan9ActRPM_1": fan9ActRPM_1,
       "fan9Cur_1": fan9Cur_1,
       "fan9Power_1": fan9Power_1,
       "fan10Actspeed_1": fan10Actspeed_1,
       "fan10ActRPM_1": fan10ActRPM_1,
       "fan10Cur_1": fan10Cur_1,
       "fan10Power_1": fan10Power_1,
       "diffFilterPres_1": diffFilterPres_1,
       "coolingRequest_1": coolingRequest_1,
       "heatingRequest_1": heatingRequest_1,
       "dehumidRequest_1": dehumidRequest_1,
       "humidifRequest_1": humidifRequest_1,
       "tempFcTs_1": tempFcTs_1,
       "fCTSStatus_1": fCTSStatus_1,
       "fCRequest_1": fCRequest_1,
       "activeComp_1": activeComp_1,
       "comp1Sts_1": comp1Sts_1,
       "comp2Sts_1": comp2Sts_1,
       "invComprReq_1": invComprReq_1,
       "invCompHz_1": invCompHz_1,
       "invCompPower_1": invCompPower_1,
       "invCompCurrent_1": invCompCurrent_1,
       "c1EvapPres_1": c1EvapPres_1,
       "c1EvapTemp_1": c1EvapTemp_1,
       "c1SuctionTemp_1": c1SuctionTemp_1,
       "c1Superheat_1": c1Superheat_1,
       "c1CompRatio_1": c1CompRatio_1,
       "c1DischTemp_1": c1DischTemp_1,
       "c1CondPress_1": c1CondPress_1,
       "c1CondTemp_1": c1CondTemp_1,
       "c1Desuperheat_1": c1Desuperheat_1,
       "c1LiquidTemp_1": c1LiquidTemp_1,
       "c1Subcooling_1": c1Subcooling_1,
       "eEV1SHSet_1": eEV1SHSet_1,
       "eEV1Position_1": eEV1Position_1,
       "eEV1Status_1": eEV1Status_1,
       "cond1ActualSet_1": cond1ActualSet_1,
       "cond1Req_1": cond1Req_1,
       "c2EvapPres_1": c2EvapPres_1,
       "c2EvapTemp_1": c2EvapTemp_1,
       "c2SuctionTemp_1": c2SuctionTemp_1,
       "c2Superheat_1": c2Superheat_1,
       "c2CompRatio_1": c2CompRatio_1,
       "c2DischTemp_1": c2DischTemp_1,
       "c2CondPress_1": c2CondPress_1,
       "c2CondTemp_1": c2CondTemp_1,
       "c2Desuperheat_1": c2Desuperheat_1,
       "c2LiquidTemp_1": c2LiquidTemp_1,
       "c2Subcooling_1": c2Subcooling_1,
       "eEV2SHSet_1": eEV2SHSet_1,
       "eEV2Position_1": eEV2Position_1,
       "eEV2Status_1": eEV2Status_1,
       "cond2ActualSet_1": cond2ActualSet_1,
       "cond2Req_1": cond2Req_1,
       "waterINTemp1_1": waterINTemp1_1,
       "waterOUTTemp1_1": waterOUTTemp1_1,
       "waterDT1_1": waterDT1_1,
       "waterFlow1_1": waterFlow1_1,
       "actWatFlowSet1_1": actWatFlowSet1_1,
       "waterCoolCap1_1": waterCoolCap1_1,
       "eER1_1": eER1_1,
       "valve1Position_1": valve1Position_1,
       "waterINTemp2_1": waterINTemp2_1,
       "waterOUTTemp2_1": waterOUTTemp2_1,
       "waterDT2_1": waterDT2_1,
       "waterFlow2_1": waterFlow2_1,
       "actWatFlowSet2_1": actWatFlowSet2_1,
       "waterCoolCap2_1": waterCoolCap2_1,
       "eER2_1": eER2_1,
       "valve2Position_1": valve2Position_1,
       "humSteamProd_1": humSteamProd_1,
       "humWaterConduct_1": humWaterConduct_1,
       "humCurrent_1": humCurrent_1,
       "humWorkingMode_1": humWorkingMode_1,
       "humWorkStatus_1": humWorkStatus_1,
       "heaterReq_1": heaterReq_1,
       "heaterActiveStg_1": heaterActiveStg_1,
       "elHeaterPower_1": elHeaterPower_1,
       "heatValveReq_1": heatValveReq_1,
       "dryCoolerActSet_1": dryCoolerActSet_1,
       "dryCoolerReq_1": dryCoolerReq_1,
       "unitWH_1": unitWH_1,
       "c1WH_1": c1WH_1,
       "c1Startup_1": c1Startup_1,
       "c2WH_1": c2WH_1,
       "c2Startup_1": c2Startup_1,
       "coolValveWH_1": coolValveWH_1,
       "heatingWH_1": heatingWH_1,
       "humidifWH_1": humidifWH_1,
       "freeCoolWH_1": freeCoolWH_1,
       "dryCoolerWH_1": dryCoolerWH_1,
       "cond1WH_1": cond1WH_1,
       "cond2WH_1": cond2WH_1,
       "tempSetpoint_1": tempSetpoint_1,
       "humSetpoint_1": humSetpoint_1,
       "airFlowSetpoint_1": airFlowSetpoint_1,
       "airPresSetpoint_1": airPresSetpoint_1,
       "airDTSetpoint_1": airDTSetpoint_1,
       "tempControlSel_1": tempControlSel_1,
       "tempControlType_1": tempControlType_1,
       "tPropBand_1": tPropBand_1,
       "tIntegralTime_1": tIntegralTime_1,
       "tDerivativeTime_1": tDerivativeTime_1,
       "highTAlOffset_1": highTAlOffset_1,
       "lowTAlOffset_1": lowTAlOffset_1,
       "highLimitTThr_1": highLimitTThr_1,
       "highLimitTMng_1": highLimitTMng_1,
       "lowLimitTThr_1": lowLimitTThr_1,
       "lowLimitTMng_1": lowLimitTMng_1,
       "dehumPropBand_1": dehumPropBand_1,
       "humPropBand_1": humPropBand_1,
       "hRetHAlOffset_1": hRetHAlOffset_1,
       "lRetHAlOffset_1": lRetHAlOffset_1,
       "highSupHumThr_1": highSupHumThr_1,
       "lowSupHumThr_1": lowSupHumThr_1,
       "fCDelta_1": fCDelta_1,
       "tSWaterSet_1": tSWaterSet_1,
       "tSWaterPropBand_1": tSWaterPropBand_1,
       "tSAirTempSet_1": tSAirTempSet_1,
       "condSetpoint_1": condSetpoint_1,
       "condPropoBand_1": condPropoBand_1,
       "condSetIncrease_1": condSetIncrease_1,
       "maxCondSetpoint_1": maxCondSetpoint_1,
       "dryCoolerSet_1": dryCoolerSet_1,
       "dryCoolPropBand_1": dryCoolPropBand_1,
       "dryCoolSetIncr_1": dryCoolSetIncr_1,
       "maxDryCoolerSet_1": maxDryCoolerSet_1,
       "dirtyFiltSet_1": dirtyFiltSet_1,
       "dirtyFiltDiff_1": dirtyFiltDiff_1,
       "invCompAlCode1_1": invCompAlCode1_1,
       "invCompAlCode2_1": invCompAlCode2_1,
       "invCompAlCode3_1": invCompAlCode3_1,
       "invCompAlCode4_1": invCompAlCode4_1,
       "invCompAlCode5_1": invCompAlCode5_1,
       "alarms1": alarms1,
       "generalAl_1": generalAl_1,
       "notCriticAl_1": notCriticAl_1,
       "criticalAl_1": criticalAl_1,
       "fansAl_1": fansAl_1,
       "compAl_1": compAl_1,
       "tempAl_1": tempAl_1,
       "humidityAl_1": humidityAl_1,
       "damperAl_1": damperAl_1,
       "fireSmokeAl_1": fireSmokeAl_1,
       "gSeriousAl_1": gSeriousAl_1,
       "fansGenAl_1": fansGenAl_1,
       "f1GeneralAl_1": f1GeneralAl_1,
       "f1PowerAl_1": f1PowerAl_1,
       "f1CommAl_1": f1CommAl_1,
       "f1HiTempAl_1": f1HiTempAl_1,
       "f1NetComAl_1": f1NetComAl_1,
       "f1InvRegAl_1": f1InvRegAl_1,
       "f1HiMotTAl_1": f1HiMotTAl_1,
       "f1HallSenAl_1": f1HallSenAl_1,
       "f1OverlAl_1": f1OverlAl_1,
       "f1LowDCAl_1": f1LowDCAl_1,
       "f2GeneralAl_1": f2GeneralAl_1,
       "f2PowerAl_1": f2PowerAl_1,
       "f2CommAl_1": f2CommAl_1,
       "f2HiTempAl_1": f2HiTempAl_1,
       "f2NetComAl_1": f2NetComAl_1,
       "f2InvRegAl_1": f2InvRegAl_1,
       "f2HiMotTAl_1": f2HiMotTAl_1,
       "f2HallSenAl_1": f2HallSenAl_1,
       "f2OverlAl_1": f2OverlAl_1,
       "f2LowDCAl_1": f2LowDCAl_1,
       "f3GeneralAl_1": f3GeneralAl_1,
       "f3PowerAl_1": f3PowerAl_1,
       "f3CommAl_1": f3CommAl_1,
       "f3HiTempAl_1": f3HiTempAl_1,
       "f3NetComAl_1": f3NetComAl_1,
       "f3InvRegAl_1": f3InvRegAl_1,
       "f3HiMotTAl_1": f3HiMotTAl_1,
       "f3HallSenAl_1": f3HallSenAl_1,
       "f3OverlAl_1": f3OverlAl_1,
       "f3LowDCAl_1": f3LowDCAl_1,
       "f4GeneralAl_1": f4GeneralAl_1,
       "f4PowerAl_1": f4PowerAl_1,
       "f4CommAl_1": f4CommAl_1,
       "f4HiTempAl_1": f4HiTempAl_1,
       "f4NetComAl_1": f4NetComAl_1,
       "f4InvRegAl_1": f4InvRegAl_1,
       "f4HiMotTAl_1": f4HiMotTAl_1,
       "f4HallSenAl_1": f4HallSenAl_1,
       "f4OverlAl_1": f4OverlAl_1,
       "f4LowDCAl_1": f4LowDCAl_1,
       "f5GeneralAl_1": f5GeneralAl_1,
       "f5PowerAl_1": f5PowerAl_1,
       "f5CommAl_1": f5CommAl_1,
       "f5HiTempAl_1": f5HiTempAl_1,
       "f5NetComAl_1": f5NetComAl_1,
       "f5InvRegAl_1": f5InvRegAl_1,
       "f5HiMotTAl_1": f5HiMotTAl_1,
       "f5HallSenAl_1": f5HallSenAl_1,
       "f5OverlAl_1": f5OverlAl_1,
       "f5LowDCAl_1": f5LowDCAl_1,
       "f6GeneralAl_1": f6GeneralAl_1,
       "f6PowerAl_1": f6PowerAl_1,
       "f6CommAl_1": f6CommAl_1,
       "f6HiTempAl_1": f6HiTempAl_1,
       "f6NetComAl_1": f6NetComAl_1,
       "f6InvRegAl_1": f6InvRegAl_1,
       "f6HiMotTAl_1": f6HiMotTAl_1,
       "f6HallSenAl_1": f6HallSenAl_1,
       "f6OverlAl_1": f6OverlAl_1,
       "f6LowDCAl_1": f6LowDCAl_1,
       "f7GeneralAl_1": f7GeneralAl_1,
       "f7PowerAl_1": f7PowerAl_1,
       "f7CommAl_1": f7CommAl_1,
       "f7HiTempAl_1": f7HiTempAl_1,
       "f7NetComAl_1": f7NetComAl_1,
       "f7InvRegAl_1": f7InvRegAl_1,
       "f7HiMotTAl_1": f7HiMotTAl_1,
       "f7HallSenAl_1": f7HallSenAl_1,
       "f7OverlAl_1": f7OverlAl_1,
       "f7LowDCAl_1": f7LowDCAl_1,
       "f8GeneralAl_1": f8GeneralAl_1,
       "f8PowerAl_1": f8PowerAl_1,
       "f8CommAl_1": f8CommAl_1,
       "f8HiTempAl_1": f8HiTempAl_1,
       "f8NetComAl_1": f8NetComAl_1,
       "f8InvRegAl_1": f8InvRegAl_1,
       "f8HiMotTAl_1": f8HiMotTAl_1,
       "f8HallSenAl_1": f8HallSenAl_1,
       "f8OverlAl_1": f8OverlAl_1,
       "f8LowDCAl_1": f8LowDCAl_1,
       "f9GeneralAl_1": f9GeneralAl_1,
       "f9PowerAl_1": f9PowerAl_1,
       "f9CommAl_1": f9CommAl_1,
       "f9HiTempAl_1": f9HiTempAl_1,
       "f9NetComAl_1": f9NetComAl_1,
       "f9InvRegAl_1": f9InvRegAl_1,
       "f9HiMotTAl_1": f9HiMotTAl_1,
       "f9HallSenAl_1": f9HallSenAl_1,
       "f9OverlAl_1": f9OverlAl_1,
       "f9LowDCAl_1": f9LowDCAl_1,
       "f10GenlAl_1": f10GenlAl_1,
       "f10PowerAl_1": f10PowerAl_1,
       "f10CommAl_1": f10CommAl_1,
       "f10HiTempAl_1": f10HiTempAl_1,
       "f10NetComAl_1": f10NetComAl_1,
       "f10InvRegAl_1": f10InvRegAl_1,
       "f10HiMotTAl_1": f10HiMotTAl_1,
       "f10HallSAl_1": f10HallSAl_1,
       "f10OverlAl_1": f10OverlAl_1,
       "f10LowDCAl_1": f10LowDCAl_1,
       "retTempPbAl_1": retTempPbAl_1,
       "supTempPrAl_1": supTempPrAl_1,
       "retHumPrAl_1": retHumPrAl_1,
       "supHumPrAl_1": supHumPrAl_1,
       "airPrSensAl_1": airPrSensAl_1,
       "watIN1PrAl_1": watIN1PrAl_1,
       "watOUT1PrAl_1": watOUT1PrAl_1,
       "watIN2PrAl_1": watIN2PrAl_1,
       "watOUT2PrAl_1": watOUT2PrAl_1,
       "watFlw1PrAl_1": watFlw1PrAl_1,
       "watFlw2PrAl_1": watFlw2PrAl_1,
       "dFPSGenAl_1": dFPSGenAl_1,
       "dFPSBrokAl_1": dFPSBrokAl_1,
       "dFPSCablAl_1": dFPSCablAl_1,
       "dFPSRangeAl_1": dFPSRangeAl_1,
       "dFPSADCAl_1": dFPSADCAl_1,
       "dFPSSetAl_1": dFPSSetAl_1,
       "dFPSDCOAl_1": dFPSDCOAl_1,
       "dFPSWatdAl_1": dFPSWatdAl_1,
       "dFPSCommAl_1": dFPSCommAl_1,
       "invC1GenAl_1": invC1GenAl_1,
       "invC1CommAl_1": invC1CommAl_1,
       "c1ThermAl_1": c1ThermAl_1,
       "c1HighPresAl_1": c1HighPresAl_1,
       "c1LowPresAl_1": c1LowPresAl_1,
       "c1HighDiscAl_1": c1HighDiscAl_1,
       "c1LCompRatAl_1": c1LCompRatAl_1,
       "condenser1Al_1": condenser1Al_1,
       "c1WatFlowAl_1": c1WatFlowAl_1,
       "eEV1GenAl_1": eEV1GenAl_1,
       "eEV1CommAl_1": eEV1CommAl_1,
       "eEV1SuctPrAl_1": eEV1SuctPrAl_1,
       "eEV1EvapPrAl_1": eEV1EvapPrAl_1,
       "eEV1CondPrAl_1": eEV1CondPrAl_1,
       "eEV1DiscPrAl_1": eEV1DiscPrAl_1,
       "c2ThermAl_1": c2ThermAl_1,
       "c2HighPresAl_1": c2HighPresAl_1,
       "c2LowPresAl_1": c2LowPresAl_1,
       "c2HighDiscAl_1": c2HighDiscAl_1,
       "c2LCompRatAl_1": c2LCompRatAl_1,
       "condenser2Al_1": condenser2Al_1,
       "c2WatFlowAl_1": c2WatFlowAl_1,
       "eEV2GenAl_1": eEV2GenAl_1,
       "eEV2CommAl_1": eEV2CommAl_1,
       "eEV2SuctPrAl_1": eEV2SuctPrAl_1,
       "eEV2EvapPrAl_1": eEV2EvapPrAl_1,
       "eEV2CondPrAl_1": eEV2CondPrAl_1,
       "eEV2DiscPrAl_1": eEV2DiscPrAl_1,
       "intHumGenAl_1": intHumGenAl_1,
       "cPYCommAl_1": cPYCommAl_1,
       "cPYMemoryAl_1": cPYMemoryAl_1,
       "cPYParamAl_1": cPYParamAl_1,
       "cPYHighCurAl_1": cPYHighCurAl_1,
       "cPYLoSteamAl_1": cPYLoSteamAl_1,
       "cPYDrainAl_1": cPYDrainAl_1,
       "cPYMaintAl_1": cPYMaintAl_1,
       "cPYNoWaterAl_1": cPYNoWaterAl_1,
       "cPYCylMainAl_1": cPYCylMainAl_1,
       "cPYDirtCylAl_1": cPYDirtCylAl_1,
       "cPYFoamAl_1": cPYFoamAl_1,
       "cPYLifeTimAl_1": cPYLifeTimAl_1,
       "cPYHiWLevAl_1": cPYHiWLevAl_1,
       "cPYHWatConAl_1": cPYHWatConAl_1,
       "cPYConnAl_1": cPYConnAl_1,
       "watPresAl_1": watPresAl_1,
       "drainPumpAl_1": drainPumpAl_1,
       "elHeatAl_1": elHeatAl_1,
       "filterAl_1": filterAl_1,
       "dryCoolerAl_1": dryCoolerAl_1,
       "extHumidAl_1": extHumidAl_1,
       "waterPumpAl_1": waterPumpAl_1,
       "condUnitGAl_1": condUnitGAl_1,
       "gasLeakAl_1": gasLeakAl_1,
       "powerSuppAl_1": powerSuppAl_1,
       "genSoftAl_1": genSoftAl_1,
       "localNetAl_1": localNetAl_1,
       "regHiTempAl_1": regHiTempAl_1,
       "regLowTempAl_1": regLowTempAl_1,
       "hiLimTempAl_1": hiLimTempAl_1,
       "lowLimTempAl_1": lowLimTempAl_1,
       "retHiHumiAl_1": retHiHumiAl_1,
       "retLowHumiAl_1": retLowHumiAl_1,
       "supHiHumiAl_1": supHiHumiAl_1,
       "supLowHumiAl_1": supLowHumiAl_1,
       "probeMod1COM_1": probeMod1COM_1,
       "prMod1err1_1": prMod1err1_1,
       "prMod1err2_1": prMod1err2_1,
       "prMod1err3_1": prMod1err3_1,
       "prMod1err4_1": prMod1err4_1,
       "prMod1err5_1": prMod1err5_1,
       "prMod1err6_1": prMod1err6_1,
       "probeMod2COM_1": probeMod2COM_1,
       "prMod2err1_1": prMod2err1_1,
       "prMod2err2_1": prMod2err2_1,
       "prMod2err3_1": prMod2err3_1,
       "prMod2err4_1": prMod2err4_1,
       "prMod2err5_1": prMod2err5_1,
       "prMod2err6_1": prMod2err6_1,
       "probeMod3COM_1": probeMod3COM_1,
       "prMod3err1_1": prMod3err1_1,
       "prMod3err2_1": prMod3err2_1,
       "prMod3err3_1": prMod3err3_1,
       "prMod3err4_1": prMod3err4_1,
       "prMod3err5_1": prMod3err5_1,
       "prMod3err6_1": prMod3err6_1,
       "node2": node2,
       "traps2": traps2,
       "generalAlTrap_2": generalAlTrap_2,
       "notCriticalAlTrap_2": notCriticalAlTrap_2,
       "criticalAlTrap_2": criticalAlTrap_2,
       "fansAlTrap_2": fansAlTrap_2,
       "compAlTrap_2": compAlTrap_2,
       "temperatureAlTrap_2": temperatureAlTrap_2,
       "humidityAlTrap_2": humidityAlTrap_2,
       "damperAlTrap_2": damperAlTrap_2,
       "fireSmokeAlTrap_2": fireSmokeAlTrap_2,
       "genSeriousAlTrap_2": genSeriousAlTrap_2,
       "fansGenAlTrap_2": fansGenAlTrap_2,
       "f1GeneralAlTrap_2": f1GeneralAlTrap_2,
       "f1PowerAlTrap_2": f1PowerAlTrap_2,
       "f1CommAlTrap_2": f1CommAlTrap_2,
       "f1HighTempAlTrap_2": f1HighTempAlTrap_2,
       "f1NetComAlTrap_2": f1NetComAlTrap_2,
       "f1InvRegAlTrap_2": f1InvRegAlTrap_2,
       "f1HighMotTempAlTrap_2": f1HighMotTempAlTrap_2,
       "f1HallSensAlTrap_2": f1HallSensAlTrap_2,
       "f1OverloadAlTrap_2": f1OverloadAlTrap_2,
       "f1LowDCAlTrap_2": f1LowDCAlTrap_2,
       "f2GeneralAlTrap_2": f2GeneralAlTrap_2,
       "f2PowerAlTrap_2": f2PowerAlTrap_2,
       "f2CommAlTrap_2": f2CommAlTrap_2,
       "f2HighTempAlTrap_2": f2HighTempAlTrap_2,
       "f2NetComAlTrap_2": f2NetComAlTrap_2,
       "f2InvRegAlTrap_2": f2InvRegAlTrap_2,
       "f2HighMotTempAlTrap_2": f2HighMotTempAlTrap_2,
       "f2HallSensAlTrap_2": f2HallSensAlTrap_2,
       "f2OverloadAlTrap_2": f2OverloadAlTrap_2,
       "f2LowDCAlTrap_2": f2LowDCAlTrap_2,
       "f3GeneralAlTrap_2": f3GeneralAlTrap_2,
       "f3PowerAlTrap_2": f3PowerAlTrap_2,
       "f3CommAlTrap_2": f3CommAlTrap_2,
       "f3HighTempAlTrap_2": f3HighTempAlTrap_2,
       "f3NetComAlTrap_2": f3NetComAlTrap_2,
       "f3InvRegAlTrap_2": f3InvRegAlTrap_2,
       "f3HighMotTempAlTrap_2": f3HighMotTempAlTrap_2,
       "f3HallSensAlTrap_2": f3HallSensAlTrap_2,
       "f3OverloadAlTrap_2": f3OverloadAlTrap_2,
       "f3LowDCAlTrap_2": f3LowDCAlTrap_2,
       "f4GeneralAlTrap_2": f4GeneralAlTrap_2,
       "f4PowerAlTrap_2": f4PowerAlTrap_2,
       "f4CommAlTrap_2": f4CommAlTrap_2,
       "f4HighTempAlTrap_2": f4HighTempAlTrap_2,
       "f4NetComAlTrap_2": f4NetComAlTrap_2,
       "f4InvRegAlTrap_2": f4InvRegAlTrap_2,
       "f4HighMotTempAlTrap_2": f4HighMotTempAlTrap_2,
       "f4HallSensAlTrap_2": f4HallSensAlTrap_2,
       "f4OverloadAlTrap_2": f4OverloadAlTrap_2,
       "f4LowDCAlTrap_2": f4LowDCAlTrap_2,
       "f5GeneralAlTrap_2": f5GeneralAlTrap_2,
       "f5PowerAlTrap_2": f5PowerAlTrap_2,
       "f5CommAlTrap_2": f5CommAlTrap_2,
       "f5HighTempAlTrap_2": f5HighTempAlTrap_2,
       "f5NetComAlTrap_2": f5NetComAlTrap_2,
       "f5InvRegAlTrap_2": f5InvRegAlTrap_2,
       "f5HighMotTempAlTrap_2": f5HighMotTempAlTrap_2,
       "f5HallSensAlTrap_2": f5HallSensAlTrap_2,
       "f5OverloadAlTrap_2": f5OverloadAlTrap_2,
       "f5LowDCAlTrap_2": f5LowDCAlTrap_2,
       "f6GeneralAlTrap_2": f6GeneralAlTrap_2,
       "f6PowerAlTrap_2": f6PowerAlTrap_2,
       "f6CommAlTrap_2": f6CommAlTrap_2,
       "f6HighTempAlTrap_2": f6HighTempAlTrap_2,
       "f6NetComAlTrap_2": f6NetComAlTrap_2,
       "f6InvRegAlTrap_2": f6InvRegAlTrap_2,
       "f6HighMotTempAlTrap_2": f6HighMotTempAlTrap_2,
       "f6HallSensAlTrap_2": f6HallSensAlTrap_2,
       "f6OverloadAlTrap_2": f6OverloadAlTrap_2,
       "f6LowDCAlTrap_2": f6LowDCAlTrap_2,
       "f7GeneralAlTrap_2": f7GeneralAlTrap_2,
       "f7PowerAlTrap_2": f7PowerAlTrap_2,
       "f7CommAlTrap_2": f7CommAlTrap_2,
       "f7HighTempAlTrap_2": f7HighTempAlTrap_2,
       "f7NetComAlTrap_2": f7NetComAlTrap_2,
       "f7InvRegAlTrap_2": f7InvRegAlTrap_2,
       "f7HighMotTempAlTrap_2": f7HighMotTempAlTrap_2,
       "f7HallSensAlTrap_2": f7HallSensAlTrap_2,
       "f7OverloadAlTrap_2": f7OverloadAlTrap_2,
       "f7LowDCAlTrap_2": f7LowDCAlTrap_2,
       "f8GeneralAlTrap_2": f8GeneralAlTrap_2,
       "f8PowerAlTrap_2": f8PowerAlTrap_2,
       "f8CommAlTrap_2": f8CommAlTrap_2,
       "f8HighTempAlTrap_2": f8HighTempAlTrap_2,
       "f8NetComAlTrap_2": f8NetComAlTrap_2,
       "f8InvRegAlTrap_2": f8InvRegAlTrap_2,
       "f8HighMotTempAlTrap_2": f8HighMotTempAlTrap_2,
       "f8HallSensAlTrap_2": f8HallSensAlTrap_2,
       "f8OverloadAlTrap_2": f8OverloadAlTrap_2,
       "f8LowDCAlTrap_2": f8LowDCAlTrap_2,
       "f9InverterAlTrap_2": f9InverterAlTrap_2,
       "f9PowerAlTrap_2": f9PowerAlTrap_2,
       "f9CommAlTrap_2": f9CommAlTrap_2,
       "f9HighTempAlTrap_2": f9HighTempAlTrap_2,
       "f9NetComAlTrap_2": f9NetComAlTrap_2,
       "f9InvRegAlTrap_2": f9InvRegAlTrap_2,
       "f9HighMotTempAlTrap_2": f9HighMotTempAlTrap_2,
       "f9HallSensAlTrap_2": f9HallSensAlTrap_2,
       "f9OverloadAlTrap_2": f9OverloadAlTrap_2,
       "f9LowDCAlTrap_2": f9LowDCAlTrap_2,
       "f10GeneralAlTrap_2": f10GeneralAlTrap_2,
       "f10PowerAlTrap_2": f10PowerAlTrap_2,
       "f10CommAlTrap_2": f10CommAlTrap_2,
       "f10HighTempAlTrap_2": f10HighTempAlTrap_2,
       "f10NetComAlTrap_2": f10NetComAlTrap_2,
       "f10InvRegAlTrap_2": f10InvRegAlTrap_2,
       "f10HighMotTAlTrap_2": f10HighMotTAlTrap_2,
       "f10HallSensAlTrap_2": f10HallSensAlTrap_2,
       "f10OverloadAlTrap_2": f10OverloadAlTrap_2,
       "f10LowDCAlTrap_2": f10LowDCAlTrap_2,
       "retTempProbAlTrap_2": retTempProbAlTrap_2,
       "supTempProbAlTrap_2": supTempProbAlTrap_2,
       "retHumProbAlTrap_2": retHumProbAlTrap_2,
       "supHumProbAlTrap_2": supHumProbAlTrap_2,
       "airPrSensorAlTrap_2": airPrSensorAlTrap_2,
       "watIN1ProbAlTrap_2": watIN1ProbAlTrap_2,
       "watOUT1ProbAlTrap_2": watOUT1ProbAlTrap_2,
       "watIN2ProbAlTrap_2": watIN2ProbAlTrap_2,
       "watOUT2ProbAlTrap_2": watOUT2ProbAlTrap_2,
       "watFlw1ProbAlTrap_2": watFlw1ProbAlTrap_2,
       "watFlw2ProbAlTrap_2": watFlw2ProbAlTrap_2,
       "dFPSGenAlTrap_2": dFPSGenAlTrap_2,
       "dFPSBrokenAlTrap_2": dFPSBrokenAlTrap_2,
       "dFPSCablingAlTrap_2": dFPSCablingAlTrap_2,
       "dFPSRangeAlTrap_2": dFPSRangeAlTrap_2,
       "dFPSADCAlTrap_2": dFPSADCAlTrap_2,
       "dFPSSettingAlTrap_2": dFPSSettingAlTrap_2,
       "dFPSDCOAlTrap_2": dFPSDCOAlTrap_2,
       "dFPSWatchdogAlTrap_2": dFPSWatchdogAlTrap_2,
       "dFPSCommAlTrap_2": dFPSCommAlTrap_2,
       "invCompGenAlTrap_2": invCompGenAlTrap_2,
       "invCompCommAlTrap_2": invCompCommAlTrap_2,
       "invCompAlCode1Trap_2": invCompAlCode1Trap_2,
       "invCompAlCode2Trap_2": invCompAlCode2Trap_2,
       "invCompAlCode3Trap_2": invCompAlCode3Trap_2,
       "invCompAlCode4Trap_2": invCompAlCode4Trap_2,
       "invCompAlCode5Trap_2": invCompAlCode5Trap_2,
       "c1ThermAlTrap_2": c1ThermAlTrap_2,
       "c1HighPresAlTrap_2": c1HighPresAlTrap_2,
       "c1LowPresAlTrap_2": c1LowPresAlTrap_2,
       "c1HighDischAlTrap_2": c1HighDischAlTrap_2,
       "c1LCompRatAlTrap_2": c1LCompRatAlTrap_2,
       "condenser1AlTrap_2": condenser1AlTrap_2,
       "c1WatFlowAlTrap_2": c1WatFlowAlTrap_2,
       "eEV1GenAlTrap_2": eEV1GenAlTrap_2,
       "eEV1CommAlTrap_2": eEV1CommAlTrap_2,
       "eEV1SuctProbAlTrap_2": eEV1SuctProbAlTrap_2,
       "eEV1EvapProbAlTrap_2": eEV1EvapProbAlTrap_2,
       "eEV1CondProbAlTrap_2": eEV1CondProbAlTrap_2,
       "eEV1DischProbAlTrap_2": eEV1DischProbAlTrap_2,
       "c2ThermAlTrap_2": c2ThermAlTrap_2,
       "c2HighPresAlTrap_2": c2HighPresAlTrap_2,
       "c2LowPresAlTrap_2": c2LowPresAlTrap_2,
       "c2HighDischAlTrap_2": c2HighDischAlTrap_2,
       "c2LCompRatAlTrap_2": c2LCompRatAlTrap_2,
       "condenser2AlTrap_2": condenser2AlTrap_2,
       "c2WatFlowAlTrap_2": c2WatFlowAlTrap_2,
       "eEV2GenAlTrap_2": eEV2GenAlTrap_2,
       "eEV2CommAlTrap_2": eEV2CommAlTrap_2,
       "eEV2SuctProbAlTrap_2": eEV2SuctProbAlTrap_2,
       "eEV2EvapProbAlTrap_2": eEV2EvapProbAlTrap_2,
       "eEV2CondProbAlTrap_2": eEV2CondProbAlTrap_2,
       "eEV2DischProbAlTrap_2": eEV2DischProbAlTrap_2,
       "intHumidGenAlTrap_2": intHumidGenAlTrap_2,
       "cPYCommAlTrap_2": cPYCommAlTrap_2,
       "cPYMemoryAlTrap_2": cPYMemoryAlTrap_2,
       "cPYParameterAlTrap_2": cPYParameterAlTrap_2,
       "cPYHighCurrAlTrap_2": cPYHighCurrAlTrap_2,
       "cPYLowSteamAlTrap_2": cPYLowSteamAlTrap_2,
       "cPYDrainAlTrap_2": cPYDrainAlTrap_2,
       "cPYMaintAlTrap_2": cPYMaintAlTrap_2,
       "cPYNoWaterAlTrap_2": cPYNoWaterAlTrap_2,
       "cPYCylMaintAlTrap_2": cPYCylMaintAlTrap_2,
       "cPYDirtyCylAlTrap_2": cPYDirtyCylAlTrap_2,
       "cPYFoamAlTrap_2": cPYFoamAlTrap_2,
       "cPYLifeTimeAlTrap_2": cPYLifeTimeAlTrap_2,
       "cPYHighWatLevAlTrap_2": cPYHighWatLevAlTrap_2,
       "cPYHWatCondAlTrap_2": cPYHWatCondAlTrap_2,
       "cPYConnectionAlTrap_2": cPYConnectionAlTrap_2,
       "watPresAlTrap_2": watPresAlTrap_2,
       "drainPumpAlTrap_2": drainPumpAlTrap_2,
       "elHeatAlTrap_2": elHeatAlTrap_2,
       "filterAlTrap_2": filterAlTrap_2,
       "dryCoolerAlTrap_2": dryCoolerAlTrap_2,
       "extHumidAlTrap_2": extHumidAlTrap_2,
       "waterPumpAlTrap_2": waterPumpAlTrap_2,
       "condUnitGenAlTrap_2": condUnitGenAlTrap_2,
       "gasLeakAlTrap_2": gasLeakAlTrap_2,
       "powerSupplyAlTrap_2": powerSupplyAlTrap_2,
       "genericSoftAlTrap_2": genericSoftAlTrap_2,
       "localNetworkAlTrap_2": localNetworkAlTrap_2,
       "regHighTempAlTrap_2": regHighTempAlTrap_2,
       "regLowTempAlTrap_2": regLowTempAlTrap_2,
       "highLimTempAlTrap_2": highLimTempAlTrap_2,
       "lowLimTempAlTrap_2": lowLimTempAlTrap_2,
       "retHighHumiAlTrap_2": retHighHumiAlTrap_2,
       "retLowHumiAlTrap_2": retLowHumiAlTrap_2,
       "supHighHumiAlTrap_2": supHighHumiAlTrap_2,
       "supLowHumiAlTrap_2": supLowHumiAlTrap_2,
       "probeMod1COMTrap_2": probeMod1COMTrap_2,
       "probeMod1err1Trap_2": probeMod1err1Trap_2,
       "probeMod1err2Trap_2": probeMod1err2Trap_2,
       "probeMod1err3Trap_2": probeMod1err3Trap_2,
       "probeMod1err4Trap_2": probeMod1err4Trap_2,
       "probeMod1err5Trap_2": probeMod1err5Trap_2,
       "probeMod1err6Trap_2": probeMod1err6Trap_2,
       "probeMod2COMTrap_2": probeMod2COMTrap_2,
       "probeMod2err1Trap_2": probeMod2err1Trap_2,
       "probeMod2err2Trap_2": probeMod2err2Trap_2,
       "probeMod2err3Trap_2": probeMod2err3Trap_2,
       "probeMod2err4Trap_2": probeMod2err4Trap_2,
       "probeMod2err5Trap_2": probeMod2err5Trap_2,
       "probeMod2err6Trap_2": probeMod2err6Trap_2,
       "probeMod3COMTrap_2": probeMod3COMTrap_2,
       "probeMod3err1Trap_2": probeMod3err1Trap_2,
       "probeMod3err2Trap_2": probeMod3err2Trap_2,
       "probeMod3err3Trap_2": probeMod3err3Trap_2,
       "probeMod3err4Trap_2": probeMod3err4Trap_2,
       "probeMod3err5Trap_2": probeMod3err5Trap_2,
       "probeMod3err6Trap_2": probeMod3err6Trap_2,
       "binaryObjects2": binaryObjects2,
       "damperStatusDI_2": damperStatusDI_2,
       "dirtyFilterDI_2": dirtyFilterDI_2,
       "remoteOffDI_2": remoteOffDI_2,
       "elHeaterAlarmDI_2": elHeaterAlarmDI_2,
       "condPumpAlarmDI_2": condPumpAlarmDI_2,
       "configurableDI1_2": configurableDI1_2,
       "configurableDI2_2": configurableDI2_2,
       "configurableDI3_2": configurableDI3_2,
       "configurableDI4_2": configurableDI4_2,
       "configurableDI5_2": configurableDI5_2,
       "c1ThermAlarmDI_2": c1ThermAlarmDI_2,
       "c1HPAlarmDI_2": c1HPAlarmDI_2,
       "c1LPAlarmDI_2": c1LPAlarmDI_2,
       "c2ThermAlarmDI_2": c2ThermAlarmDI_2,
       "c2HPAlarmDI_2": c2HPAlarmDI_2,
       "c2LPAlarmDI_2": c2LPAlarmDI_2,
       "fansDO_2": fansDO_2,
       "damperDO_2": damperDO_2,
       "configurableDO1_2": configurableDO1_2,
       "configurableDO2_2": configurableDO2_2,
       "configurableDO3_2": configurableDO3_2,
       "configurableDO4_2": configurableDO4_2,
       "configurableDO5_2": configurableDO5_2,
       "eHeaterStage1DO_2": eHeaterStage1DO_2,
       "eHeaterStage2DO_2": eHeaterStage2DO_2,
       "compressor1DO_2": compressor1DO_2,
       "compressor2DO_2": compressor2DO_2,
       "humPowerDO_2": humPowerDO_2,
       "humDrainValveDO_2": humDrainValveDO_2,
       "humFillValveDO_2": humFillValveDO_2,
       "humWaterLevel_2": humWaterLevel_2,
       "supervOFF_2": supervOFF_2,
       "enableHumid_2": enableHumid_2,
       "humManualDrain_2": humManualDrain_2,
       "humCylWashing_2": humCylWashing_2,
       "tSManExchange_2": tSManExchange_2,
       "tSTempExchEnab_2": tSTempExchEnab_2,
       "damperAlRes_2": damperAlRes_2,
       "fireSmokeAlRes_2": fireSmokeAlRes_2,
       "genSerAlRes_2": genSerAlRes_2,
       "fansGenAlRes_2": fansGenAlRes_2,
       "f1InvAlRes_2": f1InvAlRes_2,
       "f2InvAlRes_2": f2InvAlRes_2,
       "f3InvAlRes_2": f3InvAlRes_2,
       "f4InvAlRes_2": f4InvAlRes_2,
       "f5InvAlRes_2": f5InvAlRes_2,
       "f6InvAlRes_2": f6InvAlRes_2,
       "f7InvAlRes_2": f7InvAlRes_2,
       "f8InvAlRes_2": f8InvAlRes_2,
       "f9InvAlRes_2": f9InvAlRes_2,
       "f10InvAlRes_2": f10InvAlRes_2,
       "invCompAlRes_2": invCompAlRes_2,
       "c1ThermAlRes_2": c1ThermAlRes_2,
       "c1HighPresAlRes_2": c1HighPresAlRes_2,
       "c1LowPresAlRes_2": c1LowPresAlRes_2,
       "c1HighDisTAlRes_2": c1HighDisTAlRes_2,
       "c1LCompRatAlRes_2": c1LCompRatAlRes_2,
       "condenser1AlRes_2": condenser1AlRes_2,
       "eEV1AlRes_2": eEV1AlRes_2,
       "c2ThermAlRes_2": c2ThermAlRes_2,
       "c2HighPresAlRes_2": c2HighPresAlRes_2,
       "c2LowPresAlRes_2": c2LowPresAlRes_2,
       "c2HighDisTAlRes_2": c2HighDisTAlRes_2,
       "c2LComRatAlRes_2": c2LComRatAlRes_2,
       "condenser2AlRes_2": condenser2AlRes_2,
       "eEV2AlRes_2": eEV2AlRes_2,
       "intHumidifAlRes_2": intHumidifAlRes_2,
       "watPresAlRes_2": watPresAlRes_2,
       "drainPumpAlRes_2": drainPumpAlRes_2,
       "elHeatAlRes_2": elHeatAlRes_2,
       "filterAlRes_2": filterAlRes_2,
       "dryCoolerAlRes_2": dryCoolerAlRes_2,
       "extHumidifAlRes_2": extHumidifAlRes_2,
       "waterPumpAlRes_2": waterPumpAlRes_2,
       "condUnitGAlRes_2": condUnitGAlRes_2,
       "gasLeakAlRes_2": gasLeakAlRes_2,
       "powerSupAlRes_2": powerSupAlRes_2,
       "genSoftAlRes_2": genSoftAlRes_2,
       "scalarsObjects2": scalarsObjects2,
       "confDI1Combo_2": confDI1Combo_2,
       "confDI2Combo_2": confDI2Combo_2,
       "confDI3Combo_2": confDI3Combo_2,
       "confDI4Combo_2": confDI4Combo_2,
       "confDI5Combo_2": confDI5Combo_2,
       "confDO1Combo_2": confDO1Combo_2,
       "confDO2Combo_2": confDO2Combo_2,
       "confDO3Combo_2": confDO3Combo_2,
       "confDO4Combo_2": confDO4Combo_2,
       "confDO5Combo_2": confDO5Combo_2,
       "returnTemp_2": returnTemp_2,
       "returnTAvg_2": returnTAvg_2,
       "supplyTemp_2": supplyTemp_2,
       "supplyTAvg_2": supplyTAvg_2,
       "tempDelta_2": tempDelta_2,
       "returnHumidity_2": returnHumidity_2,
       "returnHumAvg_2": returnHumAvg_2,
       "supplyHumidity_2": supplyHumidity_2,
       "supplyHumAvg_2": supplyHumAvg_2,
       "airFlow_2": airFlow_2,
       "airPressure_2": airPressure_2,
       "airPressureAvg_2": airPressureAvg_2,
       "netMod1Combo1_2": netMod1Combo1_2,
       "netMod1Probe1_2": netMod1Probe1_2,
       "netMod1Combo2_2": netMod1Combo2_2,
       "netMod1Probe2_2": netMod1Probe2_2,
       "netMod1Combo3_2": netMod1Combo3_2,
       "netMod1Probe3_2": netMod1Probe3_2,
       "netMod1Combo4_2": netMod1Combo4_2,
       "netMod1Probe4_2": netMod1Probe4_2,
       "netMod1Combo5_2": netMod1Combo5_2,
       "netMod1Probe5_2": netMod1Probe5_2,
       "netMod1Combo6_2": netMod1Combo6_2,
       "netMod1Probe6_2": netMod1Probe6_2,
       "netMod2Combo1_2": netMod2Combo1_2,
       "netMod2Probe1_2": netMod2Probe1_2,
       "netMod2Combo2_2": netMod2Combo2_2,
       "netMod2Probe2_2": netMod2Probe2_2,
       "netMod2Combo3_2": netMod2Combo3_2,
       "netMod2Probe3_2": netMod2Probe3_2,
       "netMod2Combo4_2": netMod2Combo4_2,
       "netMod2Probe4_2": netMod2Probe4_2,
       "netMod2Combo5_2": netMod2Combo5_2,
       "netMod2Probe5_2": netMod2Probe5_2,
       "netMod2Combo6_2": netMod2Combo6_2,
       "netMod2Probe6_2": netMod2Probe6_2,
       "netMod3Combo1_2": netMod3Combo1_2,
       "netMod3Probe1_2": netMod3Probe1_2,
       "netMod3Combo2_2": netMod3Combo2_2,
       "netMod3Probe2_2": netMod3Probe2_2,
       "netMod3Combo3_2": netMod3Combo3_2,
       "netMod3Probe3_2": netMod3Probe3_2,
       "netMod3Combo4_2": netMod3Combo4_2,
       "netMod3Probe4_2": netMod3Probe4_2,
       "netMod3Combo5_2": netMod3Combo5_2,
       "netMod3Probe5_2": netMod3Probe5_2,
       "netMod3Combo6_2": netMod3Combo6_2,
       "netMod3Probe6_2": netMod3Probe6_2,
       "avgModTemp_2": avgModTemp_2,
       "avgModHumi_2": avgModHumi_2,
       "avgModPress_2": avgModPress_2,
       "dryCoolerAO_2": dryCoolerAO_2,
       "coolingAO_2": coolingAO_2,
       "heatingAO_2": heatingAO_2,
       "twoSources2AO_2": twoSources2AO_2,
       "condenser1AO_2": condenser1AO_2,
       "cond2HumidifAO_2": cond2HumidifAO_2,
       "unitStatus_2": unitStatus_2,
       "fanSpeed_2": fanSpeed_2,
       "fan1Actspeed_2": fan1Actspeed_2,
       "fan1ActRPM_2": fan1ActRPM_2,
       "fan1Cur_2": fan1Cur_2,
       "fan1Power_2": fan1Power_2,
       "fan2Actspeed_2": fan2Actspeed_2,
       "fan2ActRPM_2": fan2ActRPM_2,
       "fan2Cur_2": fan2Cur_2,
       "fan2Power_2": fan2Power_2,
       "fan3Actspeed_2": fan3Actspeed_2,
       "fan3ActRPM_2": fan3ActRPM_2,
       "fan3Cur_2": fan3Cur_2,
       "fan3Power_2": fan3Power_2,
       "fan4Actspeed_2": fan4Actspeed_2,
       "fan4ActRPM_2": fan4ActRPM_2,
       "fan4Cur_2": fan4Cur_2,
       "fan4Power_2": fan4Power_2,
       "fan5Actspeed_2": fan5Actspeed_2,
       "fan5ActRPM_2": fan5ActRPM_2,
       "fan5Cur_2": fan5Cur_2,
       "fan5Power_2": fan5Power_2,
       "fan6Actspeed_2": fan6Actspeed_2,
       "fan6ActRPM_2": fan6ActRPM_2,
       "fan6Cur_2": fan6Cur_2,
       "fan6Power_2": fan6Power_2,
       "fan7Actspeed_2": fan7Actspeed_2,
       "fan7ActRPM_2": fan7ActRPM_2,
       "fan7Cur_2": fan7Cur_2,
       "fan7Power_2": fan7Power_2,
       "fan8Actspeed_2": fan8Actspeed_2,
       "fan8ActRPM_2": fan8ActRPM_2,
       "fan8Cur_2": fan8Cur_2,
       "fan8Power_2": fan8Power_2,
       "fan9Actspeed_2": fan9Actspeed_2,
       "fan9ActRPM_2": fan9ActRPM_2,
       "fan9Cur_2": fan9Cur_2,
       "fan9Power_2": fan9Power_2,
       "fan10Actspeed_2": fan10Actspeed_2,
       "fan10ActRPM_2": fan10ActRPM_2,
       "fan10Cur_2": fan10Cur_2,
       "fan10Power_2": fan10Power_2,
       "diffFilterPres_2": diffFilterPres_2,
       "coolingRequest_2": coolingRequest_2,
       "heatingRequest_2": heatingRequest_2,
       "dehumidRequest_2": dehumidRequest_2,
       "humidifRequest_2": humidifRequest_2,
       "tempFcTs_2": tempFcTs_2,
       "fCTSStatus_2": fCTSStatus_2,
       "fCRequest_2": fCRequest_2,
       "activeComp_2": activeComp_2,
       "comp1Sts_2": comp1Sts_2,
       "comp2Sts_2": comp2Sts_2,
       "invComprReq_2": invComprReq_2,
       "invCompHz_2": invCompHz_2,
       "invCompPower_2": invCompPower_2,
       "invCompCurrent_2": invCompCurrent_2,
       "c1EvapPres_2": c1EvapPres_2,
       "c1EvapTemp_2": c1EvapTemp_2,
       "c1SuctionTemp_2": c1SuctionTemp_2,
       "c1Superheat_2": c1Superheat_2,
       "c1CompRatio_2": c1CompRatio_2,
       "c1DischTemp_2": c1DischTemp_2,
       "c1CondPress_2": c1CondPress_2,
       "c1CondTemp_2": c1CondTemp_2,
       "c1Desuperheat_2": c1Desuperheat_2,
       "c1LiquidTemp_2": c1LiquidTemp_2,
       "c1Subcooling_2": c1Subcooling_2,
       "eEV1SHSet_2": eEV1SHSet_2,
       "eEV1Position_2": eEV1Position_2,
       "eEV1Status_2": eEV1Status_2,
       "cond1ActualSet_2": cond1ActualSet_2,
       "cond1Req_2": cond1Req_2,
       "c2EvapPres_2": c2EvapPres_2,
       "c2EvapTemp_2": c2EvapTemp_2,
       "c2SuctionTemp_2": c2SuctionTemp_2,
       "c2Superheat_2": c2Superheat_2,
       "c2CompRatio_2": c2CompRatio_2,
       "c2DischTemp_2": c2DischTemp_2,
       "c2CondPress_2": c2CondPress_2,
       "c2CondTemp_2": c2CondTemp_2,
       "c2Desuperheat_2": c2Desuperheat_2,
       "c2LiquidTemp_2": c2LiquidTemp_2,
       "c2Subcooling_2": c2Subcooling_2,
       "eEV2SHSet_2": eEV2SHSet_2,
       "eEV2Position_2": eEV2Position_2,
       "eEV2Status_2": eEV2Status_2,
       "cond2ActualSet_2": cond2ActualSet_2,
       "cond2Req_2": cond2Req_2,
       "waterINTemp1_2": waterINTemp1_2,
       "waterOUTTemp1_2": waterOUTTemp1_2,
       "waterDT1_2": waterDT1_2,
       "waterFlow1_2": waterFlow1_2,
       "actWatFlowSet1_2": actWatFlowSet1_2,
       "waterCoolCap1_2": waterCoolCap1_2,
       "eER1_2": eER1_2,
       "valve1Position_2": valve1Position_2,
       "waterINTemp2_2": waterINTemp2_2,
       "waterOUTTemp2_2": waterOUTTemp2_2,
       "waterDT2_2": waterDT2_2,
       "waterFlow2_2": waterFlow2_2,
       "actWatFlowSet2_2": actWatFlowSet2_2,
       "waterCoolCap2_2": waterCoolCap2_2,
       "eER2_2": eER2_2,
       "valve2Position_2": valve2Position_2,
       "humSteamProd_2": humSteamProd_2,
       "humWaterConduct_2": humWaterConduct_2,
       "humCurrent_2": humCurrent_2,
       "humWorkingMode_2": humWorkingMode_2,
       "humWorkStatus_2": humWorkStatus_2,
       "heaterReq_2": heaterReq_2,
       "heaterActiveStg_2": heaterActiveStg_2,
       "elHeaterPower_2": elHeaterPower_2,
       "heatValveReq_2": heatValveReq_2,
       "dryCoolerActSet_2": dryCoolerActSet_2,
       "dryCoolerReq_2": dryCoolerReq_2,
       "unitWH_2": unitWH_2,
       "c1WH_2": c1WH_2,
       "c1Startup_2": c1Startup_2,
       "c2WH_2": c2WH_2,
       "c2Startup_2": c2Startup_2,
       "coolValveWH_2": coolValveWH_2,
       "heatingWH_2": heatingWH_2,
       "humidifWH_2": humidifWH_2,
       "freeCoolWH_2": freeCoolWH_2,
       "dryCoolerWH_2": dryCoolerWH_2,
       "cond1WH_2": cond1WH_2,
       "cond2WH_2": cond2WH_2,
       "tempSetpoint_2": tempSetpoint_2,
       "humSetpoint_2": humSetpoint_2,
       "airFlowSetpoint_2": airFlowSetpoint_2,
       "airPresSetpoint_2": airPresSetpoint_2,
       "airDTSetpoint_2": airDTSetpoint_2,
       "tempControlSel_2": tempControlSel_2,
       "tempControlType_2": tempControlType_2,
       "tPropBand_2": tPropBand_2,
       "tIntegralTime_2": tIntegralTime_2,
       "tDerivativeTime_2": tDerivativeTime_2,
       "highTAlOffset_2": highTAlOffset_2,
       "lowTAlOffset_2": lowTAlOffset_2,
       "highLimitTThr_2": highLimitTThr_2,
       "highLimitTMng_2": highLimitTMng_2,
       "lowLimitTThr_2": lowLimitTThr_2,
       "lowLimitTMng_2": lowLimitTMng_2,
       "dehumPropBand_2": dehumPropBand_2,
       "humPropBand_2": humPropBand_2,
       "hRetHAlOffset_2": hRetHAlOffset_2,
       "lRetHAlOffset_2": lRetHAlOffset_2,
       "highSupHumThr_2": highSupHumThr_2,
       "lowSupHumThr_2": lowSupHumThr_2,
       "fCDelta_2": fCDelta_2,
       "tSWaterSet_2": tSWaterSet_2,
       "tSWaterPropBand_2": tSWaterPropBand_2,
       "tSAirTempSet_2": tSAirTempSet_2,
       "condSetpoint_2": condSetpoint_2,
       "condPropoBand_2": condPropoBand_2,
       "condSetIncrease_2": condSetIncrease_2,
       "maxCondSetpoint_2": maxCondSetpoint_2,
       "dryCoolerSet_2": dryCoolerSet_2,
       "dryCoolPropBand_2": dryCoolPropBand_2,
       "dryCoolSetIncr_2": dryCoolSetIncr_2,
       "maxDryCoolerSet_2": maxDryCoolerSet_2,
       "dirtyFiltSet_2": dirtyFiltSet_2,
       "dirtyFiltDiff_2": dirtyFiltDiff_2,
       "invCompAlCode1_2": invCompAlCode1_2,
       "invCompAlCode2_2": invCompAlCode2_2,
       "invCompAlCode3_2": invCompAlCode3_2,
       "invCompAlCode4_2": invCompAlCode4_2,
       "invCompAlCode5_2": invCompAlCode5_2,
       "alarms2": alarms2,
       "generalAl_2": generalAl_2,
       "notCriticAl_2": notCriticAl_2,
       "criticalAl_2": criticalAl_2,
       "fansAl_2": fansAl_2,
       "compAl_2": compAl_2,
       "tempAl_2": tempAl_2,
       "humidityAl_2": humidityAl_2,
       "damperAl_2": damperAl_2,
       "fireSmokeAl_2": fireSmokeAl_2,
       "gSeriousAl_2": gSeriousAl_2,
       "fansGenAl_2": fansGenAl_2,
       "f1GeneralAl_2": f1GeneralAl_2,
       "f1PowerAl_2": f1PowerAl_2,
       "f1CommAl_2": f1CommAl_2,
       "f1HiTempAl_2": f1HiTempAl_2,
       "f1NetComAl_2": f1NetComAl_2,
       "f1InvRegAl_2": f1InvRegAl_2,
       "f1HiMotTAl_2": f1HiMotTAl_2,
       "f1HallSenAl_2": f1HallSenAl_2,
       "f1OverlAl_2": f1OverlAl_2,
       "f1LowDCAl_2": f1LowDCAl_2,
       "f2GeneralAl_2": f2GeneralAl_2,
       "f2PowerAl_2": f2PowerAl_2,
       "f2CommAl_2": f2CommAl_2,
       "f2HiTempAl_2": f2HiTempAl_2,
       "f2NetComAl_2": f2NetComAl_2,
       "f2InvRegAl_2": f2InvRegAl_2,
       "f2HiMotTAl_2": f2HiMotTAl_2,
       "f2HallSenAl_2": f2HallSenAl_2,
       "f2OverlAl_2": f2OverlAl_2,
       "f2LowDCAl_2": f2LowDCAl_2,
       "f3GeneralAl_2": f3GeneralAl_2,
       "f3PowerAl_2": f3PowerAl_2,
       "f3CommAl_2": f3CommAl_2,
       "f3HiTempAl_2": f3HiTempAl_2,
       "f3NetComAl_2": f3NetComAl_2,
       "f3InvRegAl_2": f3InvRegAl_2,
       "f3HiMotTAl_2": f3HiMotTAl_2,
       "f3HallSenAl_2": f3HallSenAl_2,
       "f3OverlAl_2": f3OverlAl_2,
       "f3LowDCAl_2": f3LowDCAl_2,
       "f4GeneralAl_2": f4GeneralAl_2,
       "f4PowerAl_2": f4PowerAl_2,
       "f4CommAl_2": f4CommAl_2,
       "f4HiTempAl_2": f4HiTempAl_2,
       "f4NetComAl_2": f4NetComAl_2,
       "f4InvRegAl_2": f4InvRegAl_2,
       "f4HiMotTAl_2": f4HiMotTAl_2,
       "f4HallSenAl_2": f4HallSenAl_2,
       "f4OverlAl_2": f4OverlAl_2,
       "f4LowDCAl_2": f4LowDCAl_2,
       "f5GeneralAl_2": f5GeneralAl_2,
       "f5PowerAl_2": f5PowerAl_2,
       "f5CommAl_2": f5CommAl_2,
       "f5HiTempAl_2": f5HiTempAl_2,
       "f5NetComAl_2": f5NetComAl_2,
       "f5InvRegAl_2": f5InvRegAl_2,
       "f5HiMotTAl_2": f5HiMotTAl_2,
       "f5HallSenAl_2": f5HallSenAl_2,
       "f5OverlAl_2": f5OverlAl_2,
       "f5LowDCAl_2": f5LowDCAl_2,
       "f6GeneralAl_2": f6GeneralAl_2,
       "f6PowerAl_2": f6PowerAl_2,
       "f6CommAl_2": f6CommAl_2,
       "f6HiTempAl_2": f6HiTempAl_2,
       "f6NetComAl_2": f6NetComAl_2,
       "f6InvRegAl_2": f6InvRegAl_2,
       "f6HiMotTAl_2": f6HiMotTAl_2,
       "f6HallSenAl_2": f6HallSenAl_2,
       "f6OverlAl_2": f6OverlAl_2,
       "f6LowDCAl_2": f6LowDCAl_2,
       "f7GeneralAl_2": f7GeneralAl_2,
       "f7PowerAl_2": f7PowerAl_2,
       "f7CommAl_2": f7CommAl_2,
       "f7HiTempAl_2": f7HiTempAl_2,
       "f7NetComAl_2": f7NetComAl_2,
       "f7InvRegAl_2": f7InvRegAl_2,
       "f7HiMotTAl_2": f7HiMotTAl_2,
       "f7HallSenAl_2": f7HallSenAl_2,
       "f7OverlAl_2": f7OverlAl_2,
       "f7LowDCAl_2": f7LowDCAl_2,
       "f8GeneralAl_2": f8GeneralAl_2,
       "f8PowerAl_2": f8PowerAl_2,
       "f8CommAl_2": f8CommAl_2,
       "f8HiTempAl_2": f8HiTempAl_2,
       "f8NetComAl_2": f8NetComAl_2,
       "f8InvRegAl_2": f8InvRegAl_2,
       "f8HiMotTAl_2": f8HiMotTAl_2,
       "f8HallSenAl_2": f8HallSenAl_2,
       "f8OverlAl_2": f8OverlAl_2,
       "f8LowDCAl_2": f8LowDCAl_2,
       "f9GeneralAl_2": f9GeneralAl_2,
       "f9PowerAl_2": f9PowerAl_2,
       "f9CommAl_2": f9CommAl_2,
       "f9HiTempAl_2": f9HiTempAl_2,
       "f9NetComAl_2": f9NetComAl_2,
       "f9InvRegAl_2": f9InvRegAl_2,
       "f9HiMotTAl_2": f9HiMotTAl_2,
       "f9HallSenAl_2": f9HallSenAl_2,
       "f9OverlAl_2": f9OverlAl_2,
       "f9LowDCAl_2": f9LowDCAl_2,
       "f10GenlAl_2": f10GenlAl_2,
       "f10PowerAl_2": f10PowerAl_2,
       "f10CommAl_2": f10CommAl_2,
       "f10HiTempAl_2": f10HiTempAl_2,
       "f10NetComAl_2": f10NetComAl_2,
       "f10InvRegAl_2": f10InvRegAl_2,
       "f10HiMotTAl_2": f10HiMotTAl_2,
       "f10HallSAl_2": f10HallSAl_2,
       "f10OverlAl_2": f10OverlAl_2,
       "f10LowDCAl_2": f10LowDCAl_2,
       "retTempPbAl_2": retTempPbAl_2,
       "supTempPrAl_2": supTempPrAl_2,
       "retHumPrAl_2": retHumPrAl_2,
       "supHumPrAl_2": supHumPrAl_2,
       "airPrSensAl_2": airPrSensAl_2,
       "watIN1PrAl_2": watIN1PrAl_2,
       "watOUT1PrAl_2": watOUT1PrAl_2,
       "watIN2PrAl_2": watIN2PrAl_2,
       "watOUT2PrAl_2": watOUT2PrAl_2,
       "watFlw1PrAl_2": watFlw1PrAl_2,
       "watFlw2PrAl_2": watFlw2PrAl_2,
       "dFPSGenAl_2": dFPSGenAl_2,
       "dFPSBrokAl_2": dFPSBrokAl_2,
       "dFPSCablAl_2": dFPSCablAl_2,
       "dFPSRangeAl_2": dFPSRangeAl_2,
       "dFPSADCAl_2": dFPSADCAl_2,
       "dFPSSetAl_2": dFPSSetAl_2,
       "dFPSDCOAl_2": dFPSDCOAl_2,
       "dFPSWatdAl_2": dFPSWatdAl_2,
       "dFPSCommAl_2": dFPSCommAl_2,
       "invC1GenAl_2": invC1GenAl_2,
       "invC1CommAl_2": invC1CommAl_2,
       "c1ThermAl_2": c1ThermAl_2,
       "c1HighPresAl_2": c1HighPresAl_2,
       "c1LowPresAl_2": c1LowPresAl_2,
       "c1HighDiscAl_2": c1HighDiscAl_2,
       "c1LCompRatAl_2": c1LCompRatAl_2,
       "condenser1Al_2": condenser1Al_2,
       "c1WatFlowAl_2": c1WatFlowAl_2,
       "eEV1GenAl_2": eEV1GenAl_2,
       "eEV1CommAl_2": eEV1CommAl_2,
       "eEV1SuctPrAl_2": eEV1SuctPrAl_2,
       "eEV1EvapPrAl_2": eEV1EvapPrAl_2,
       "eEV1CondPrAl_2": eEV1CondPrAl_2,
       "eEV1DiscPrAl_2": eEV1DiscPrAl_2,
       "c2ThermAl_2": c2ThermAl_2,
       "c2HighPresAl_2": c2HighPresAl_2,
       "c2LowPresAl_2": c2LowPresAl_2,
       "c2HighDiscAl_2": c2HighDiscAl_2,
       "c2LCompRatAl_2": c2LCompRatAl_2,
       "condenser2Al_2": condenser2Al_2,
       "c2WatFlowAl_2": c2WatFlowAl_2,
       "eEV2GenAl_2": eEV2GenAl_2,
       "eEV2CommAl_2": eEV2CommAl_2,
       "eEV2SuctPrAl_2": eEV2SuctPrAl_2,
       "eEV2EvapPrAl_2": eEV2EvapPrAl_2,
       "eEV2CondPrAl_2": eEV2CondPrAl_2,
       "eEV2DiscPrAl_2": eEV2DiscPrAl_2,
       "intHumGenAl_2": intHumGenAl_2,
       "cPYCommAl_2": cPYCommAl_2,
       "cPYMemoryAl_2": cPYMemoryAl_2,
       "cPYParamAl_2": cPYParamAl_2,
       "cPYHighCurAl_2": cPYHighCurAl_2,
       "cPYLoSteamAl_2": cPYLoSteamAl_2,
       "cPYDrainAl_2": cPYDrainAl_2,
       "cPYMaintAl_2": cPYMaintAl_2,
       "cPYNoWaterAl_2": cPYNoWaterAl_2,
       "cPYCylMainAl_2": cPYCylMainAl_2,
       "cPYDirtCylAl_2": cPYDirtCylAl_2,
       "cPYFoamAl_2": cPYFoamAl_2,
       "cPYLifeTimAl_2": cPYLifeTimAl_2,
       "cPYHiWLevAl_2": cPYHiWLevAl_2,
       "cPYHWatConAl_2": cPYHWatConAl_2,
       "cPYConnAl_2": cPYConnAl_2,
       "watPresAl_2": watPresAl_2,
       "drainPumpAl_2": drainPumpAl_2,
       "elHeatAl_2": elHeatAl_2,
       "filterAl_2": filterAl_2,
       "dryCoolerAl_2": dryCoolerAl_2,
       "extHumidAl_2": extHumidAl_2,
       "waterPumpAl_2": waterPumpAl_2,
       "condUnitGAl_2": condUnitGAl_2,
       "gasLeakAl_2": gasLeakAl_2,
       "powerSuppAl_2": powerSuppAl_2,
       "genSoftAl_2": genSoftAl_2,
       "localNetAl_2": localNetAl_2,
       "regHiTempAl_2": regHiTempAl_2,
       "regLowTempAl_2": regLowTempAl_2,
       "hiLimTempAl_2": hiLimTempAl_2,
       "lowLimTempAl_2": lowLimTempAl_2,
       "retHiHumiAl_2": retHiHumiAl_2,
       "retLowHumiAl_2": retLowHumiAl_2,
       "supHiHumiAl_2": supHiHumiAl_2,
       "supLowHumiAl_2": supLowHumiAl_2,
       "probeMod1COM_2": probeMod1COM_2,
       "prMod1err1_2": prMod1err1_2,
       "prMod1err2_2": prMod1err2_2,
       "prMod1err3_2": prMod1err3_2,
       "prMod1err4_2": prMod1err4_2,
       "prMod1err5_2": prMod1err5_2,
       "prMod1err6_2": prMod1err6_2,
       "probeMod2COM_2": probeMod2COM_2,
       "prMod2err1_2": prMod2err1_2,
       "prMod2err2_2": prMod2err2_2,
       "prMod2err3_2": prMod2err3_2,
       "prMod2err4_2": prMod2err4_2,
       "prMod2err5_2": prMod2err5_2,
       "prMod2err6_2": prMod2err6_2,
       "probeMod3COM_2": probeMod3COM_2,
       "prMod3err1_2": prMod3err1_2,
       "prMod3err2_2": prMod3err2_2,
       "prMod3err3_2": prMod3err3_2,
       "prMod3err4_2": prMod3err4_2,
       "prMod3err5_2": prMod3err5_2,
       "prMod3err6_2": prMod3err6_2}
)
