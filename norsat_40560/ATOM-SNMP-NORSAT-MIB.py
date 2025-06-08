# SNMP MIB module (ATOM-SNMP-NORSAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/norsat_40560/ATOM-SNMP-NORSAT-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 19:08:38 2025
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

(InetAddressType,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressType")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

norsat = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 40560)
)
if mibBuilder.loadTexts:
    norsat.setRevisions(
        ("2016-07-28 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Boolean(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )



# MIB Managed Objects in the order of their OIDs

_LinkControl_ObjectIdentity = ObjectIdentity
linkControl = _LinkControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40560, 1)
)
_AtomControl_ObjectIdentity = ObjectIdentity
atomControl = _AtomControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40560, 2)
)
_DeviceInfo_ObjectIdentity = ObjectIdentity
deviceInfo = _DeviceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40560, 2, 1)
)
_ProductType_Type = OctetString
_ProductType_Object = MibScalar
productType = _ProductType_Object(
    (1, 3, 6, 1, 4, 1, 40560, 2, 1, 1),
    _ProductType_Type()
)
productType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productType.setStatus("current")
_SerialNumber_Type = OctetString
_SerialNumber_Object = MibScalar
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 40560, 2, 1, 2),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("current")
_DeviceType_Type = OctetString
_DeviceType_Object = MibScalar
deviceType = _DeviceType_Object(
    (1, 3, 6, 1, 4, 1, 40560, 2, 1, 3),
    _DeviceType_Type()
)
deviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceType.setStatus("current")
_Firmware_Type = OctetString
_Firmware_Object = MibScalar
firmware = _Firmware_Object(
    (1, 3, 6, 1, 4, 1, 40560, 2, 1, 4),
    _Firmware_Type()
)
firmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmware.setStatus("current")
_Syntheziser_ObjectIdentity = ObjectIdentity
syntheziser = _Syntheziser_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40560, 2, 1, 5)
)
_SynthModel_Type = OctetString
_SynthModel_Object = MibScalar
synthModel = _SynthModel_Object(
    (1, 3, 6, 1, 4, 1, 40560, 2, 1, 5, 1),
    _SynthModel_Type()
)
synthModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    synthModel.setStatus("current")
_SynthHardware_Type = OctetString
_SynthHardware_Object = MibScalar
synthHardware = _SynthHardware_Object(
    (1, 3, 6, 1, 4, 1, 40560, 2, 1, 5, 2),
    _SynthHardware_Type()
)
synthHardware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    synthHardware.setStatus("current")
_SynthSoftware_Type = OctetString
_SynthSoftware_Object = MibScalar
synthSoftware = _SynthSoftware_Object(
    (1, 3, 6, 1, 4, 1, 40560, 2, 1, 5, 3),
    _SynthSoftware_Type()
)
synthSoftware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    synthSoftware.setStatus("current")
_Communications_ObjectIdentity = ObjectIdentity
communications = _Communications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40560, 2, 1, 6)
)
_SerialComms_Type = OctetString
_SerialComms_Object = MibScalar
serialComms = _SerialComms_Object(
    (1, 3, 6, 1, 4, 1, 40560, 2, 1, 6, 1),
    _SerialComms_Type()
)
serialComms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialComms.setStatus("current")
_IpAddr_Type = InetAddressType
_IpAddr_Object = MibScalar
ipAddr = _IpAddr_Object(
    (1, 3, 6, 1, 4, 1, 40560, 2, 1, 6, 2),
    _IpAddr_Type()
)
ipAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAddr.setStatus("current")
_NetMask_Type = InetAddressType
_NetMask_Object = MibScalar
netMask = _NetMask_Object(
    (1, 3, 6, 1, 4, 1, 40560, 2, 1, 6, 3),
    _NetMask_Type()
)
netMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMask.setStatus("current")
_Operation_ObjectIdentity = ObjectIdentity
operation = _Operation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40560, 2, 4)
)
_ForwardPower_Type = OctetString
_ForwardPower_Object = MibScalar
forwardPower = _ForwardPower_Object(
    (1, 3, 6, 1, 4, 1, 40560, 2, 4, 1),
    _ForwardPower_Type()
)
forwardPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forwardPower.setStatus("current")
_Temperatures_ObjectIdentity = ObjectIdentity
temperatures = _Temperatures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40560, 2, 4, 2)
)
_Tmp1_Type = OctetString
_Tmp1_Object = MibScalar
tmp1 = _Tmp1_Object(
    (1, 3, 6, 1, 4, 1, 40560, 2, 4, 2, 1),
    _Tmp1_Type()
)
tmp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmp1.setStatus("current")
_Tmp2_Type = OctetString
_Tmp2_Object = MibScalar
tmp2 = _Tmp2_Object(
    (1, 3, 6, 1, 4, 1, 40560, 2, 4, 2, 2),
    _Tmp2_Type()
)
tmp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmp2.setStatus("current")
_Tmp3_Type = OctetString
_Tmp3_Object = MibScalar
tmp3 = _Tmp3_Object(
    (1, 3, 6, 1, 4, 1, 40560, 2, 4, 2, 3),
    _Tmp3_Type()
)
tmp3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmp3.setStatus("current")
_Tmp4_Type = OctetString
_Tmp4_Object = MibScalar
tmp4 = _Tmp4_Object(
    (1, 3, 6, 1, 4, 1, 40560, 2, 4, 2, 4),
    _Tmp4_Type()
)
tmp4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmp4.setStatus("current")
_Tmp5_Type = OctetString
_Tmp5_Object = MibScalar
tmp5 = _Tmp5_Object(
    (1, 3, 6, 1, 4, 1, 40560, 2, 4, 2, 5),
    _Tmp5_Type()
)
tmp5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmp5.setStatus("current")
_Tmp6_Type = OctetString
_Tmp6_Object = MibScalar
tmp6 = _Tmp6_Object(
    (1, 3, 6, 1, 4, 1, 40560, 2, 4, 2, 6),
    _Tmp6_Type()
)
tmp6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmp6.setStatus("current")
_Tmp7_Type = OctetString
_Tmp7_Object = MibScalar
tmp7 = _Tmp7_Object(
    (1, 3, 6, 1, 4, 1, 40560, 2, 4, 2, 7),
    _Tmp7_Type()
)
tmp7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmp7.setStatus("current")
_Tmp8_Type = OctetString
_Tmp8_Object = MibScalar
tmp8 = _Tmp8_Object(
    (1, 3, 6, 1, 4, 1, 40560, 2, 4, 2, 8),
    _Tmp8_Type()
)
tmp8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmp8.setStatus("current")
_Tmp9_Type = OctetString
_Tmp9_Object = MibScalar
tmp9 = _Tmp9_Object(
    (1, 3, 6, 1, 4, 1, 40560, 2, 4, 2, 9),
    _Tmp9_Type()
)
tmp9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmp9.setStatus("current")
_Tmp10_Type = OctetString
_Tmp10_Object = MibScalar
tmp10 = _Tmp10_Object(
    (1, 3, 6, 1, 4, 1, 40560, 2, 4, 2, 10),
    _Tmp10_Type()
)
tmp10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmp10.setStatus("current")
_Tmp11_Type = OctetString
_Tmp11_Object = MibScalar
tmp11 = _Tmp11_Object(
    (1, 3, 6, 1, 4, 1, 40560, 2, 4, 2, 11),
    _Tmp11_Type()
)
tmp11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmp11.setStatus("current")
_Tmp12_Type = OctetString
_Tmp12_Object = MibScalar
tmp12 = _Tmp12_Object(
    (1, 3, 6, 1, 4, 1, 40560, 2, 4, 2, 12),
    _Tmp12_Type()
)
tmp12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmp12.setStatus("current")
_Faults_ObjectIdentity = ObjectIdentity
faults = _Faults_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40560, 2, 4, 3)
)
_TrapActivated_Type = Boolean
_TrapActivated_Object = MibScalar
trapActivated = _TrapActivated_Object(
    (1, 3, 6, 1, 4, 1, 40560, 2, 4, 3, 1),
    _TrapActivated_Type()
)
trapActivated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapActivated.setStatus("current")
_TrapCycles_Type = Integer32
_TrapCycles_Object = MibScalar
trapCycles = _TrapCycles_Object(
    (1, 3, 6, 1, 4, 1, 40560, 2, 4, 3, 2),
    _TrapCycles_Type()
)
trapCycles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapCycles.setStatus("current")
_OvertemperatureFault_Type = Boolean
_OvertemperatureFault_Object = MibScalar
overtemperatureFault = _OvertemperatureFault_Object(
    (1, 3, 6, 1, 4, 1, 40560, 2, 4, 3, 3),
    _OvertemperatureFault_Type()
)
overtemperatureFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    overtemperatureFault.setStatus("current")
_PowerFault_Type = Boolean
_PowerFault_Object = MibScalar
powerFault = _PowerFault_Object(
    (1, 3, 6, 1, 4, 1, 40560, 2, 4, 3, 4),
    _PowerFault_Type()
)
powerFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerFault.setStatus("current")
_PllFault_Type = Boolean
_PllFault_Object = MibScalar
pllFault = _PllFault_Object(
    (1, 3, 6, 1, 4, 1, 40560, 2, 4, 3, 5),
    _PllFault_Type()
)
pllFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pllFault.setStatus("current")
_Muted_Type = Boolean
_Muted_Object = MibScalar
muted = _Muted_Object(
    (1, 3, 6, 1, 4, 1, 40560, 2, 4, 3, 6),
    _Muted_Type()
)
muted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muted.setStatus("current")
_Mute_ObjectIdentity = ObjectIdentity
mute = _Mute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40560, 2, 4, 4)
)
_MuteStatus_Type = Boolean
_MuteStatus_Object = MibScalar
muteStatus = _MuteStatus_Object(
    (1, 3, 6, 1, 4, 1, 40560, 2, 4, 4, 1),
    _MuteStatus_Type()
)
muteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muteStatus.setStatus("current")
_MuteInvert_Type = Boolean
_MuteInvert_Object = MibScalar
muteInvert = _MuteInvert_Object(
    (1, 3, 6, 1, 4, 1, 40560, 2, 4, 4, 2),
    _MuteInvert_Type()
)
muteInvert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muteInvert.setStatus("current")
_MuteBias_Type = Boolean
_MuteBias_Object = MibScalar
muteBias = _MuteBias_Object(
    (1, 3, 6, 1, 4, 1, 40560, 2, 4, 4, 3),
    _MuteBias_Type()
)
muteBias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muteBias.setStatus("current")
_MuteCommand_Type = Boolean
_MuteCommand_Object = MibScalar
muteCommand = _MuteCommand_Object(
    (1, 3, 6, 1, 4, 1, 40560, 2, 4, 4, 4),
    _MuteCommand_Type()
)
muteCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muteCommand.setStatus("current")
_MuteOvrd_Type = Boolean
_MuteOvrd_Object = MibScalar
muteOvrd = _MuteOvrd_Object(
    (1, 3, 6, 1, 4, 1, 40560, 2, 4, 4, 5),
    _MuteOvrd_Type()
)
muteOvrd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muteOvrd.setStatus("current")
_MuteFault_Type = Boolean
_MuteFault_Object = MibScalar
muteFault = _MuteFault_Object(
    (1, 3, 6, 1, 4, 1, 40560, 2, 4, 4, 6),
    _MuteFault_Type()
)
muteFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muteFault.setStatus("current")
_MuteOnFault_Type = Boolean
_MuteOnFault_Object = MibScalar
muteOnFault = _MuteOnFault_Object(
    (1, 3, 6, 1, 4, 1, 40560, 2, 4, 4, 7),
    _MuteOnFault_Type()
)
muteOnFault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muteOnFault.setStatus("current")
_MuteOnPowerFault_Type = Integer32
_MuteOnPowerFault_Object = MibScalar
muteOnPowerFault = _MuteOnPowerFault_Object(
    (1, 3, 6, 1, 4, 1, 40560, 2, 4, 4, 8),
    _MuteOnPowerFault_Type()
)
muteOnPowerFault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muteOnPowerFault.setStatus("current")
_MuteOnPllFault_Type = Integer32
_MuteOnPllFault_Object = MibScalar
muteOnPllFault = _MuteOnPllFault_Object(
    (1, 3, 6, 1, 4, 1, 40560, 2, 4, 4, 9),
    _MuteOnPllFault_Type()
)
muteOnPllFault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muteOnPllFault.setStatus("current")
_MuteOnOvertemperatureFault_Type = Integer32
_MuteOnOvertemperatureFault_Object = MibScalar
muteOnOvertemperatureFault = _MuteOnOvertemperatureFault_Object(
    (1, 3, 6, 1, 4, 1, 40560, 2, 4, 4, 10),
    _MuteOnOvertemperatureFault_Type()
)
muteOnOvertemperatureFault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muteOnOvertemperatureFault.setStatus("current")
_Attenuation_Type = OctetString
_Attenuation_Object = MibScalar
attenuation = _Attenuation_Object(
    (1, 3, 6, 1, 4, 1, 40560, 2, 4, 5),
    _Attenuation_Type()
)
attenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    attenuation.setStatus("current")
_BandSwitching_Type = OctetString
_BandSwitching_Object = MibScalar
bandSwitching = _BandSwitching_Object(
    (1, 3, 6, 1, 4, 1, 40560, 2, 4, 6),
    _BandSwitching_Type()
)
bandSwitching.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandSwitching.setStatus("current")
_NorsatGroups_ObjectIdentity = ObjectIdentity
norsatGroups = _NorsatGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40560, 3)
)

# Managed Objects groups

deviceInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 40560, 3, 1)
)
deviceInfoGroup.setObjects(
      *(("ATOM-SNMP-NORSAT-MIB", "productType"),
        ("ATOM-SNMP-NORSAT-MIB", "serialNumber"),
        ("ATOM-SNMP-NORSAT-MIB", "deviceType"),
        ("ATOM-SNMP-NORSAT-MIB", "firmware"),
        ("ATOM-SNMP-NORSAT-MIB", "synthModel"),
        ("ATOM-SNMP-NORSAT-MIB", "synthHardware"),
        ("ATOM-SNMP-NORSAT-MIB", "synthSoftware"),
        ("ATOM-SNMP-NORSAT-MIB", "serialComms"),
        ("ATOM-SNMP-NORSAT-MIB", "ipAddr"),
        ("ATOM-SNMP-NORSAT-MIB", "netMask"))
)
if mibBuilder.loadTexts:
    deviceInfoGroup.setStatus("current")

deviceStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 40560, 3, 2)
)
deviceStatusGroup.setObjects(
      *(("ATOM-SNMP-NORSAT-MIB", "forwardPower"),
        ("ATOM-SNMP-NORSAT-MIB", "attenuation"),
        ("ATOM-SNMP-NORSAT-MIB", "bandSwitching"))
)
if mibBuilder.loadTexts:
    deviceStatusGroup.setStatus("current")

temperatureGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 40560, 3, 3)
)
temperatureGroup.setObjects(
      *(("ATOM-SNMP-NORSAT-MIB", "tmp1"),
        ("ATOM-SNMP-NORSAT-MIB", "tmp2"),
        ("ATOM-SNMP-NORSAT-MIB", "tmp3"),
        ("ATOM-SNMP-NORSAT-MIB", "tmp4"),
        ("ATOM-SNMP-NORSAT-MIB", "tmp5"),
        ("ATOM-SNMP-NORSAT-MIB", "tmp6"),
        ("ATOM-SNMP-NORSAT-MIB", "tmp7"),
        ("ATOM-SNMP-NORSAT-MIB", "tmp8"),
        ("ATOM-SNMP-NORSAT-MIB", "tmp9"),
        ("ATOM-SNMP-NORSAT-MIB", "tmp10"),
        ("ATOM-SNMP-NORSAT-MIB", "tmp11"),
        ("ATOM-SNMP-NORSAT-MIB", "tmp12"))
)
if mibBuilder.loadTexts:
    temperatureGroup.setStatus("current")

faultGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 40560, 3, 4)
)
faultGroup.setObjects(
      *(("ATOM-SNMP-NORSAT-MIB", "trapActivated"),
        ("ATOM-SNMP-NORSAT-MIB", "trapCycles"),
        ("ATOM-SNMP-NORSAT-MIB", "overtemperatureFault"),
        ("ATOM-SNMP-NORSAT-MIB", "powerFault"),
        ("ATOM-SNMP-NORSAT-MIB", "pllFault"),
        ("ATOM-SNMP-NORSAT-MIB", "muted"))
)
if mibBuilder.loadTexts:
    faultGroup.setStatus("current")

muteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 40560, 3, 5)
)
muteGroup.setObjects(
      *(("ATOM-SNMP-NORSAT-MIB", "muteStatus"),
        ("ATOM-SNMP-NORSAT-MIB", "muteInvert"),
        ("ATOM-SNMP-NORSAT-MIB", "muteBias"),
        ("ATOM-SNMP-NORSAT-MIB", "muteCommand"),
        ("ATOM-SNMP-NORSAT-MIB", "muteOvrd"),
        ("ATOM-SNMP-NORSAT-MIB", "muteFault"),
        ("ATOM-SNMP-NORSAT-MIB", "muteOnFault"),
        ("ATOM-SNMP-NORSAT-MIB", "muteOnPowerFault"),
        ("ATOM-SNMP-NORSAT-MIB", "muteOnPllFault"),
        ("ATOM-SNMP-NORSAT-MIB", "muteOnOvertemperatureFault"))
)
if mibBuilder.loadTexts:
    muteGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ATOM-SNMP-NORSAT-MIB",
    **{"Boolean": Boolean,
       "norsat": norsat,
       "linkControl": linkControl,
       "atomControl": atomControl,
       "deviceInfo": deviceInfo,
       "productType": productType,
       "serialNumber": serialNumber,
       "deviceType": deviceType,
       "firmware": firmware,
       "syntheziser": syntheziser,
       "synthModel": synthModel,
       "synthHardware": synthHardware,
       "synthSoftware": synthSoftware,
       "communications": communications,
       "serialComms": serialComms,
       "ipAddr": ipAddr,
       "netMask": netMask,
       "operation": operation,
       "forwardPower": forwardPower,
       "temperatures": temperatures,
       "tmp1": tmp1,
       "tmp2": tmp2,
       "tmp3": tmp3,
       "tmp4": tmp4,
       "tmp5": tmp5,
       "tmp6": tmp6,
       "tmp7": tmp7,
       "tmp8": tmp8,
       "tmp9": tmp9,
       "tmp10": tmp10,
       "tmp11": tmp11,
       "tmp12": tmp12,
       "faults": faults,
       "trapActivated": trapActivated,
       "trapCycles": trapCycles,
       "overtemperatureFault": overtemperatureFault,
       "powerFault": powerFault,
       "pllFault": pllFault,
       "muted": muted,
       "mute": mute,
       "muteStatus": muteStatus,
       "muteInvert": muteInvert,
       "muteBias": muteBias,
       "muteCommand": muteCommand,
       "muteOvrd": muteOvrd,
       "muteFault": muteFault,
       "muteOnFault": muteOnFault,
       "muteOnPowerFault": muteOnPowerFault,
       "muteOnPllFault": muteOnPllFault,
       "muteOnOvertemperatureFault": muteOnOvertemperatureFault,
       "attenuation": attenuation,
       "bandSwitching": bandSwitching,
       "norsatGroups": norsatGroups,
       "deviceInfoGroup": deviceInfoGroup,
       "deviceStatusGroup": deviceStatusGroup,
       "temperatureGroup": temperatureGroup,
       "faultGroup": faultGroup,
       "muteGroup": muteGroup}
)
