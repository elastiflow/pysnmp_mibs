# SNMP MIB module (NDS-DTH3-HEALTH) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/news_digital_1855/NDS-DTH3-HEALTH.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:44:39 2025
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

ndsDTH3Encoder = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1855, 1, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HealthEnc_ObjectIdentity = ObjectIdentity
healthEnc = _HealthEnc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6)
)
_EncSystemHealth_ObjectIdentity = ObjectIdentity
encSystemHealth = _EncSystemHealth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 1)
)


class _SystemHealth_Type(OctetString):
    """Custom type systemHealth based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_SystemHealth_Type.__name__ = "OctetString"
_SystemHealth_Object = MibScalar
systemHealth = _SystemHealth_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 1, 1),
    _SystemHealth_Type()
)
systemHealth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemHealth.setStatus("current")
_EncMuxHealth_ObjectIdentity = ObjectIdentity
encMuxHealth = _EncMuxHealth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 2)
)


class _MuxHealth_Type(OctetString):
    """Custom type muxHealth based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_MuxHealth_Type.__name__ = "OctetString"
_MuxHealth_Object = MibScalar
muxHealth = _MuxHealth_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 2, 1),
    _MuxHealth_Type()
)
muxHealth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxHealth.setStatus("current")
_EncPreProcessorHealth_ObjectIdentity = ObjectIdentity
encPreProcessorHealth = _EncPreProcessorHealth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 3)
)


class _PreProcessorHealth1_Type(OctetString):
    """Custom type preProcessorHealth1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_PreProcessorHealth1_Type.__name__ = "OctetString"
_PreProcessorHealth1_Object = MibScalar
preProcessorHealth1 = _PreProcessorHealth1_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 3, 1),
    _PreProcessorHealth1_Type()
)
preProcessorHealth1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    preProcessorHealth1.setStatus("current")


class _PreProcessorHealth2_Type(OctetString):
    """Custom type preProcessorHealth2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_PreProcessorHealth2_Type.__name__ = "OctetString"
_PreProcessorHealth2_Object = MibScalar
preProcessorHealth2 = _PreProcessorHealth2_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 3, 2),
    _PreProcessorHealth2_Type()
)
preProcessorHealth2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    preProcessorHealth2.setStatus("current")
_EncVidinHealth_ObjectIdentity = ObjectIdentity
encVidinHealth = _EncVidinHealth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 4)
)


class _VidinHealth_Type(OctetString):
    """Custom type vidinHealth based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_VidinHealth_Type.__name__ = "OctetString"
_VidinHealth_Object = MibScalar
vidinHealth = _VidinHealth_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 4, 1),
    _VidinHealth_Type()
)
vidinHealth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vidinHealth.setStatus("current")
_EncVCMHealth_ObjectIdentity = ObjectIdentity
encVCMHealth = _EncVCMHealth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 5)
)


class _VCMHealth_Type(OctetString):
    """Custom type vCMHealth based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_VCMHealth_Type.__name__ = "OctetString"
_VCMHealth_Object = MibScalar
vCMHealth = _VCMHealth_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 5, 1),
    _VCMHealth_Type()
)
vCMHealth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vCMHealth.setStatus("current")
_EncAudioHealth_ObjectIdentity = ObjectIdentity
encAudioHealth = _EncAudioHealth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 7)
)
_AudioHealthTable_Object = MibTable
audioHealthTable = _AudioHealthTable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 7, 1)
)
if mibBuilder.loadTexts:
    audioHealthTable.setStatus("current")
_AudioHealthEntry_Object = MibTableRow
audioHealthEntry = _AudioHealthEntry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 7, 1, 1)
)
audioHealthEntry.setIndexNames(
    (0, "NDS-DTH3-HEALTH", "audioModuleIndex"),
    (0, "NDS-DTH3-HEALTH", "audioChannelIndex"),
)
if mibBuilder.loadTexts:
    audioHealthEntry.setStatus("current")


class _AudioModuleIndex_Type(Integer32):
    """Custom type audioModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AudioModuleIndex_Type.__name__ = "Integer32"
_AudioModuleIndex_Object = MibTableColumn
audioModuleIndex = _AudioModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 7, 1, 1, 1),
    _AudioModuleIndex_Type()
)
audioModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioModuleIndex.setStatus("current")


class _AudioChannelIndex_Type(Integer32):
    """Custom type audioChannelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("a", 1),
          ("b", 2))
    )


_AudioChannelIndex_Type.__name__ = "Integer32"
_AudioChannelIndex_Object = MibTableColumn
audioChannelIndex = _AudioChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 7, 1, 1, 2),
    _AudioChannelIndex_Type()
)
audioChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioChannelIndex.setStatus("current")


class _AudioHealth_Type(OctetString):
    """Custom type audioHealth based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_AudioHealth_Type.__name__ = "OctetString"
_AudioHealth_Object = MibTableColumn
audioHealth = _AudioHealth_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 7, 1, 1, 3),
    _AudioHealth_Type()
)
audioHealth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioHealth.setStatus("current")
_EncRS232Health_ObjectIdentity = ObjectIdentity
encRS232Health = _EncRS232Health_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 8)
)
_Rs232HealthTable_Object = MibTable
rs232HealthTable = _Rs232HealthTable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 8, 1)
)
if mibBuilder.loadTexts:
    rs232HealthTable.setStatus("current")
_Rs232HealthEntry_Object = MibTableRow
rs232HealthEntry = _Rs232HealthEntry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 8, 1, 1)
)
rs232HealthEntry.setIndexNames(
    (0, "NDS-DTH3-HEALTH", "rs232HealthModuleIndex"),
)
if mibBuilder.loadTexts:
    rs232HealthEntry.setStatus("current")


class _Rs232HealthModuleIndex_Type(Integer32):
    """Custom type rs232HealthModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 3),
    )


_Rs232HealthModuleIndex_Type.__name__ = "Integer32"
_Rs232HealthModuleIndex_Object = MibTableColumn
rs232HealthModuleIndex = _Rs232HealthModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 8, 1, 1, 1),
    _Rs232HealthModuleIndex_Type()
)
rs232HealthModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232HealthModuleIndex.setStatus("current")


class _Rs232Health_Type(OctetString):
    """Custom type rs232Health based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_Rs232Health_Type.__name__ = "OctetString"
_Rs232Health_Object = MibTableColumn
rs232Health = _Rs232Health_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 8, 1, 1, 3),
    _Rs232Health_Type()
)
rs232Health.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rs232Health.setStatus("current")
_EncModulatorHealth_ObjectIdentity = ObjectIdentity
encModulatorHealth = _EncModulatorHealth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 9)
)


class _ModulatorHealth_Type(OctetString):
    """Custom type modulatorHealth based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_ModulatorHealth_Type.__name__ = "OctetString"
_ModulatorHealth_Object = MibScalar
modulatorHealth = _ModulatorHealth_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 9, 1),
    _ModulatorHealth_Type()
)
modulatorHealth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modulatorHealth.setStatus("current")
_EncRS422Health_ObjectIdentity = ObjectIdentity
encRS422Health = _EncRS422Health_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 11)
)
_Rs422HealthTable_Object = MibTable
rs422HealthTable = _Rs422HealthTable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 11, 1)
)
if mibBuilder.loadTexts:
    rs422HealthTable.setStatus("current")
_Rs422HealthEntry_Object = MibTableRow
rs422HealthEntry = _Rs422HealthEntry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 11, 1, 1)
)
rs422HealthEntry.setIndexNames(
    (0, "NDS-DTH3-HEALTH", "rs422HealthModuleIndex"),
)
if mibBuilder.loadTexts:
    rs422HealthEntry.setStatus("current")


class _Rs422HealthModuleIndex_Type(Integer32):
    """Custom type rs422HealthModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 3),
    )


_Rs422HealthModuleIndex_Type.__name__ = "Integer32"
_Rs422HealthModuleIndex_Object = MibTableColumn
rs422HealthModuleIndex = _Rs422HealthModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 11, 1, 1, 1),
    _Rs422HealthModuleIndex_Type()
)
rs422HealthModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs422HealthModuleIndex.setStatus("current")


class _Rs422Health_Type(OctetString):
    """Custom type rs422Health based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_Rs422Health_Type.__name__ = "OctetString"
_Rs422Health_Object = MibTableColumn
rs422Health = _Rs422Health_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 11, 1, 1, 3),
    _Rs422Health_Type()
)
rs422Health.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rs422Health.setStatus("current")
_EncIRDHealth_ObjectIdentity = ObjectIdentity
encIRDHealth = _EncIRDHealth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 12)
)


class _IRDHealth_Type(OctetString):
    """Custom type iRDHealth based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_IRDHealth_Type.__name__ = "OctetString"
_IRDHealth_Object = MibScalar
iRDHealth = _IRDHealth_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 12, 1),
    _IRDHealth_Type()
)
iRDHealth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iRDHealth.setStatus("current")
_EncOFDMHealth_ObjectIdentity = ObjectIdentity
encOFDMHealth = _EncOFDMHealth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 15)
)


class _OFDMHealth_Type(OctetString):
    """Custom type oFDMHealth based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_OFDMHealth_Type.__name__ = "OctetString"
_OFDMHealth_Object = MibScalar
oFDMHealth = _OFDMHealth_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 15, 1),
    _OFDMHealth_Type()
)
oFDMHealth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oFDMHealth.setStatus("current")
_EncRemuxE5700Health_ObjectIdentity = ObjectIdentity
encRemuxE5700Health = _EncRemuxE5700Health_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 16)
)


class _RemuxE5700Health_Type(OctetString):
    """Custom type remuxE5700Health based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_RemuxE5700Health_Type.__name__ = "OctetString"
_RemuxE5700Health_Object = MibScalar
remuxE5700Health = _RemuxE5700Health_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 16, 1),
    _RemuxE5700Health_Type()
)
remuxE5700Health.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remuxE5700Health.setStatus("current")
_EncAudioXlrHealth_ObjectIdentity = ObjectIdentity
encAudioXlrHealth = _EncAudioXlrHealth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 18)
)


class _AudioXlrHealth_Type(OctetString):
    """Custom type audioXlrHealth based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_AudioXlrHealth_Type.__name__ = "OctetString"
_AudioXlrHealth_Object = MibScalar
audioXlrHealth = _AudioXlrHealth_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 18, 1),
    _AudioXlrHealth_Type()
)
audioXlrHealth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioXlrHealth.setStatus("current")
_EncIpStreamerHealth_ObjectIdentity = ObjectIdentity
encIpStreamerHealth = _EncIpStreamerHealth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 20)
)
_IpStreamerHealthTable_Object = MibTable
ipStreamerHealthTable = _IpStreamerHealthTable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 20, 1)
)
if mibBuilder.loadTexts:
    ipStreamerHealthTable.setStatus("current")
_IpStreamerHealthEntry_Object = MibTableRow
ipStreamerHealthEntry = _IpStreamerHealthEntry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 20, 1, 1)
)
ipStreamerHealthEntry.setIndexNames(
    (0, "NDS-DTH3-HEALTH", "ipStreamerModuleIndex"),
)
if mibBuilder.loadTexts:
    ipStreamerHealthEntry.setStatus("current")


class _IpStreamerModuleIndex_Type(Integer32):
    """Custom type ipStreamerModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_IpStreamerModuleIndex_Type.__name__ = "Integer32"
_IpStreamerModuleIndex_Object = MibTableColumn
ipStreamerModuleIndex = _IpStreamerModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 20, 1, 1, 1),
    _IpStreamerModuleIndex_Type()
)
ipStreamerModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipStreamerModuleIndex.setStatus("current")


class _IpStreamerHealth_Type(OctetString):
    """Custom type ipStreamerHealth based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_IpStreamerHealth_Type.__name__ = "OctetString"
_IpStreamerHealth_Object = MibTableColumn
ipStreamerHealth = _IpStreamerHealth_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 20, 1, 1, 2),
    _IpStreamerHealth_Type()
)
ipStreamerHealth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipStreamerHealth.setStatus("current")
_EncG703Health_ObjectIdentity = ObjectIdentity
encG703Health = _EncG703Health_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 21)
)
_G703HealthTable_Object = MibTable
g703HealthTable = _G703HealthTable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 21, 1)
)
if mibBuilder.loadTexts:
    g703HealthTable.setStatus("current")
_G703HealthEntry_Object = MibTableRow
g703HealthEntry = _G703HealthEntry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 21, 1, 1)
)
g703HealthEntry.setIndexNames(
    (0, "NDS-DTH3-HEALTH", "g703ModuleIndex"),
)
if mibBuilder.loadTexts:
    g703HealthEntry.setStatus("current")


class _G703ModuleIndex_Type(Integer32):
    """Custom type g703ModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_G703ModuleIndex_Type.__name__ = "Integer32"
_G703ModuleIndex_Object = MibTableColumn
g703ModuleIndex = _G703ModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 21, 1, 1, 1),
    _G703ModuleIndex_Type()
)
g703ModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g703ModuleIndex.setStatus("current")


class _G703Health_Type(OctetString):
    """Custom type g703Health based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_G703Health_Type.__name__ = "OctetString"
_G703Health_Object = MibTableColumn
g703Health = _G703Health_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 21, 1, 1, 2),
    _G703Health_Type()
)
g703Health.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    g703Health.setStatus("current")
_EncWM9Health_ObjectIdentity = ObjectIdentity
encWM9Health = _EncWM9Health_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 22)
)


class _WM9Health_Type(OctetString):
    """Custom type wM9Health based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WM9Health_Type.__name__ = "OctetString"
_WM9Health_Object = MibScalar
wM9Health = _WM9Health_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 22, 1),
    _WM9Health_Type()
)
wM9Health.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wM9Health.setStatus("current")
_EncAlarmHealth_ObjectIdentity = ObjectIdentity
encAlarmHealth = _EncAlarmHealth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 240)
)


class _AlarmHealth_Type(Integer32):
    """Custom type alarmHealth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("alarm", 1))
    )


_AlarmHealth_Type.__name__ = "Integer32"
_AlarmHealth_Object = MibScalar
alarmHealth = _AlarmHealth_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 240, 1),
    _AlarmHealth_Type()
)
alarmHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmHealth.setStatus("current")
_EncFailHealth_ObjectIdentity = ObjectIdentity
encFailHealth = _EncFailHealth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 241)
)


class _FailHealth_Type(Integer32):
    """Custom type failHealth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("fail", 1))
    )


_FailHealth_Type.__name__ = "Integer32"
_FailHealth_Object = MibScalar
failHealth = _FailHealth_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 241, 1),
    _FailHealth_Type()
)
failHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    failHealth.setStatus("current")
_EncLoggingList_ObjectIdentity = ObjectIdentity
encLoggingList = _EncLoggingList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 253)
)
_LogTable_Object = MibTable
logTable = _LogTable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 253, 1)
)
if mibBuilder.loadTexts:
    logTable.setStatus("current")
_LogEntry_Object = MibTableRow
logEntry = _LogEntry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 253, 1, 1)
)
logEntry.setIndexNames(
    (0, "NDS-DTH3-HEALTH", "logIndex"),
)
if mibBuilder.loadTexts:
    logEntry.setStatus("current")


class _LogIndex_Type(Integer32):
    """Custom type logIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_LogIndex_Type.__name__ = "Integer32"
_LogIndex_Object = MibTableColumn
logIndex = _LogIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 253, 1, 1, 1),
    _LogIndex_Type()
)
logIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logIndex.setStatus("current")


class _LogMessage_Type(DisplayString):
    """Custom type logMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LogMessage_Type.__name__ = "DisplayString"
_LogMessage_Object = MibTableColumn
logMessage = _LogMessage_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 253, 1, 1, 2),
    _LogMessage_Type()
)
logMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logMessage.setStatus("current")
_EncLatchErrorList_ObjectIdentity = ObjectIdentity
encLatchErrorList = _EncLatchErrorList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 254)
)
_LatchErrorTable_Object = MibTable
latchErrorTable = _LatchErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 254, 1)
)
if mibBuilder.loadTexts:
    latchErrorTable.setStatus("current")
_LatchErrorEntry_Object = MibTableRow
latchErrorEntry = _LatchErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 254, 1, 1)
)
latchErrorEntry.setIndexNames(
    (0, "NDS-DTH3-HEALTH", "latchErrorIndex"),
)
if mibBuilder.loadTexts:
    latchErrorEntry.setStatus("current")


class _LatchErrorIndex_Type(Integer32):
    """Custom type latchErrorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_LatchErrorIndex_Type.__name__ = "Integer32"
_LatchErrorIndex_Object = MibTableColumn
latchErrorIndex = _LatchErrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 254, 1, 1, 1),
    _LatchErrorIndex_Type()
)
latchErrorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latchErrorIndex.setStatus("current")


class _LatchError_Type(DisplayString):
    """Custom type latchError based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LatchError_Type.__name__ = "DisplayString"
_LatchError_Object = MibTableColumn
latchError = _LatchError_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 254, 1, 1, 2),
    _LatchError_Type()
)
latchError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latchError.setStatus("current")
_EncActiveErrorList_ObjectIdentity = ObjectIdentity
encActiveErrorList = _EncActiveErrorList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 255)
)
_ActiveErrorTable_Object = MibTable
activeErrorTable = _ActiveErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 255, 1)
)
if mibBuilder.loadTexts:
    activeErrorTable.setStatus("current")
_ActiveErrorEntry_Object = MibTableRow
activeErrorEntry = _ActiveErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 255, 1, 1)
)
activeErrorEntry.setIndexNames(
    (0, "NDS-DTH3-HEALTH", "activeErrorIndex"),
)
if mibBuilder.loadTexts:
    activeErrorEntry.setStatus("current")


class _ActiveErrorIndex_Type(Integer32):
    """Custom type activeErrorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_ActiveErrorIndex_Type.__name__ = "Integer32"
_ActiveErrorIndex_Object = MibTableColumn
activeErrorIndex = _ActiveErrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 255, 1, 1, 1),
    _ActiveErrorIndex_Type()
)
activeErrorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeErrorIndex.setStatus("current")


class _ActiveError_Type(DisplayString):
    """Custom type activeError based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ActiveError_Type.__name__ = "DisplayString"
_ActiveError_Object = MibTableColumn
activeError = _ActiveError_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 6, 255, 1, 1, 2),
    _ActiveError_Type()
)
activeError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeError.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NDS-DTH3-HEALTH",
    **{"ndsDTH3Encoder": ndsDTH3Encoder,
       "healthEnc": healthEnc,
       "encSystemHealth": encSystemHealth,
       "systemHealth": systemHealth,
       "encMuxHealth": encMuxHealth,
       "muxHealth": muxHealth,
       "encPreProcessorHealth": encPreProcessorHealth,
       "preProcessorHealth1": preProcessorHealth1,
       "preProcessorHealth2": preProcessorHealth2,
       "encVidinHealth": encVidinHealth,
       "vidinHealth": vidinHealth,
       "encVCMHealth": encVCMHealth,
       "vCMHealth": vCMHealth,
       "encAudioHealth": encAudioHealth,
       "audioHealthTable": audioHealthTable,
       "audioHealthEntry": audioHealthEntry,
       "audioModuleIndex": audioModuleIndex,
       "audioChannelIndex": audioChannelIndex,
       "audioHealth": audioHealth,
       "encRS232Health": encRS232Health,
       "rs232HealthTable": rs232HealthTable,
       "rs232HealthEntry": rs232HealthEntry,
       "rs232HealthModuleIndex": rs232HealthModuleIndex,
       "rs232Health": rs232Health,
       "encModulatorHealth": encModulatorHealth,
       "modulatorHealth": modulatorHealth,
       "encRS422Health": encRS422Health,
       "rs422HealthTable": rs422HealthTable,
       "rs422HealthEntry": rs422HealthEntry,
       "rs422HealthModuleIndex": rs422HealthModuleIndex,
       "rs422Health": rs422Health,
       "encIRDHealth": encIRDHealth,
       "iRDHealth": iRDHealth,
       "encOFDMHealth": encOFDMHealth,
       "oFDMHealth": oFDMHealth,
       "encRemuxE5700Health": encRemuxE5700Health,
       "remuxE5700Health": remuxE5700Health,
       "encAudioXlrHealth": encAudioXlrHealth,
       "audioXlrHealth": audioXlrHealth,
       "encIpStreamerHealth": encIpStreamerHealth,
       "ipStreamerHealthTable": ipStreamerHealthTable,
       "ipStreamerHealthEntry": ipStreamerHealthEntry,
       "ipStreamerModuleIndex": ipStreamerModuleIndex,
       "ipStreamerHealth": ipStreamerHealth,
       "encG703Health": encG703Health,
       "g703HealthTable": g703HealthTable,
       "g703HealthEntry": g703HealthEntry,
       "g703ModuleIndex": g703ModuleIndex,
       "g703Health": g703Health,
       "encWM9Health": encWM9Health,
       "wM9Health": wM9Health,
       "encAlarmHealth": encAlarmHealth,
       "alarmHealth": alarmHealth,
       "encFailHealth": encFailHealth,
       "failHealth": failHealth,
       "encLoggingList": encLoggingList,
       "logTable": logTable,
       "logEntry": logEntry,
       "logIndex": logIndex,
       "logMessage": logMessage,
       "encLatchErrorList": encLatchErrorList,
       "latchErrorTable": latchErrorTable,
       "latchErrorEntry": latchErrorEntry,
       "latchErrorIndex": latchErrorIndex,
       "latchError": latchError,
       "encActiveErrorList": encActiveErrorList,
       "activeErrorTable": activeErrorTable,
       "activeErrorEntry": activeErrorEntry,
       "activeErrorIndex": activeErrorIndex,
       "activeError": activeError}
)
