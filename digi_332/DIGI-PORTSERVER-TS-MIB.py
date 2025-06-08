# SNMP MIB module (DIGI-PORTSERVER-TS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/digi_332/DIGI-PORTSERVER-TS-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 11:54:30 2025
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

(digiPortServerTS,) = mibBuilder.importSymbols(
    "DIGI-SMI",
    "digiPortServerTS")

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


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""




class PhysAddress(OctetString):
    """Custom type PhysAddress based on OctetString"""




class Switch(Integer32):
    """Custom type Switch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )





class Action(Integer32):
    """Custom type Action based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ready", 1),
          ("execute", 2))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_General_ObjectIdentity = ObjectIdentity
general = _General_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 20)
)
_GeneralModel_Type = DisplayString
_GeneralModel_Object = MibScalar
generalModel = _GeneralModel_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 20, 11),
    _GeneralModel_Type()
)
generalModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generalModel.setStatus("mandatory")
_GeneralType_Type = DisplayString
_GeneralType_Object = MibScalar
generalType = _GeneralType_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 20, 12),
    _GeneralType_Type()
)
generalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generalType.setStatus("mandatory")
_GeneralFirmwareVersion_Type = DisplayString
_GeneralFirmwareVersion_Object = MibScalar
generalFirmwareVersion = _GeneralFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 20, 13),
    _GeneralFirmwareVersion_Type()
)
generalFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generalFirmwareVersion.setStatus("mandatory")
_GeneralIPAddress_Type = IpAddress
_GeneralIPAddress_Object = MibScalar
generalIPAddress = _GeneralIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 20, 14),
    _GeneralIPAddress_Type()
)
generalIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generalIPAddress.setStatus("mandatory")
_GeneralGateway_Type = IpAddress
_GeneralGateway_Object = MibScalar
generalGateway = _GeneralGateway_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 20, 15),
    _GeneralGateway_Type()
)
generalGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generalGateway.setStatus("mandatory")
_GeneralNameServer_Type = IpAddress
_GeneralNameServer_Object = MibScalar
generalNameServer = _GeneralNameServer_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 20, 16),
    _GeneralNameServer_Type()
)
generalNameServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generalNameServer.setStatus("mandatory")
_GeneralSubMask_Type = IpAddress
_GeneralSubMask_Object = MibScalar
generalSubMask = _GeneralSubMask_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 20, 17),
    _GeneralSubMask_Type()
)
generalSubMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generalSubMask.setStatus("mandatory")
_GeneralEtherAddress_Type = PhysAddress
_GeneralEtherAddress_Object = MibScalar
generalEtherAddress = _GeneralEtherAddress_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 20, 18),
    _GeneralEtherAddress_Type()
)
generalEtherAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generalEtherAddress.setStatus("mandatory")
_GeneralPortServerName_Type = DisplayString
_GeneralPortServerName_Object = MibScalar
generalPortServerName = _GeneralPortServerName_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 20, 19),
    _GeneralPortServerName_Type()
)
generalPortServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generalPortServerName.setStatus("mandatory")
_GeneralDomain_Type = DisplayString
_GeneralDomain_Object = MibScalar
generalDomain = _GeneralDomain_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 20, 20),
    _GeneralDomain_Type()
)
generalDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generalDomain.setStatus("mandatory")
_GeneralRealPortNumber_Type = Integer32
_GeneralRealPortNumber_Object = MibScalar
generalRealPortNumber = _GeneralRealPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 20, 21),
    _GeneralRealPortNumber_Type()
)
generalRealPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generalRealPortNumber.setStatus("mandatory")
_GeneralBaseSocket_Type = Integer32
_GeneralBaseSocket_Object = MibScalar
generalBaseSocket = _GeneralBaseSocket_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 20, 22),
    _GeneralBaseSocket_Type()
)
generalBaseSocket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generalBaseSocket.setStatus("mandatory")


class _GeneralTBreak_Type(Integer32):
    """Custom type generalTBreak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("standard", 1),
          ("none", 2),
          ("any", 3))
    )


_GeneralTBreak_Type.__name__ = "Integer32"
_GeneralTBreak_Object = MibScalar
generalTBreak = _GeneralTBreak_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 20, 23),
    _GeneralTBreak_Type()
)
generalTBreak.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generalTBreak.setStatus("mandatory")
_GeneralClearStatistics_Type = Action
_GeneralClearStatistics_Object = MibScalar
generalClearStatistics = _GeneralClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 20, 24),
    _GeneralClearStatistics_Type()
)
generalClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generalClearStatistics.setStatus("mandatory")


class _GeneralOptimize_Type(Integer32):
    """Custom type generalOptimize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("throughput", 1),
          ("latency", 2))
    )


_GeneralOptimize_Type.__name__ = "Integer32"
_GeneralOptimize_Object = MibScalar
generalOptimize = _GeneralOptimize_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 20, 25),
    _GeneralOptimize_Type()
)
generalOptimize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generalOptimize.setStatus("mandatory")
_GeneralDhcpClientIdentifier_Type = DisplayString
_GeneralDhcpClientIdentifier_Object = MibScalar
generalDhcpClientIdentifier = _GeneralDhcpClientIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 20, 26),
    _GeneralDhcpClientIdentifier_Type()
)
generalDhcpClientIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generalDhcpClientIdentifier.setStatus("mandatory")


class _GeneralDhcpClientIdentifierType_Type(Integer32):
    """Custom type generalDhcpClientIdentifierType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_GeneralDhcpClientIdentifierType_Type.__name__ = "Integer32"
_GeneralDhcpClientIdentifierType_Object = MibScalar
generalDhcpClientIdentifierType = _GeneralDhcpClientIdentifierType_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 20, 27),
    _GeneralDhcpClientIdentifierType_Type()
)
generalDhcpClientIdentifierType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generalDhcpClientIdentifierType.setStatus("mandatory")


class _GeneralEthernetSpeed_Type(Integer32):
    """Custom type generalEthernetSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("mbit10", 2),
          ("mbit100", 3))
    )


_GeneralEthernetSpeed_Type.__name__ = "Integer32"
_GeneralEthernetSpeed_Object = MibScalar
generalEthernetSpeed = _GeneralEthernetSpeed_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 20, 28),
    _GeneralEthernetSpeed_Type()
)
generalEthernetSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generalEthernetSpeed.setStatus("mandatory")


class _GeneralEthernetDuplex_Type(Integer32):
    """Custom type generalEthernetDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("halfduplex", 2),
          ("fullduplex", 3))
    )


_GeneralEthernetDuplex_Type.__name__ = "Integer32"
_GeneralEthernetDuplex_Object = MibScalar
generalEthernetDuplex = _GeneralEthernetDuplex_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 20, 29),
    _GeneralEthernetDuplex_Type()
)
generalEthernetDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generalEthernetDuplex.setStatus("mandatory")
_GeneralDhcpIgnoreKeepalive_Type = Switch
_GeneralDhcpIgnoreKeepalive_Object = MibScalar
generalDhcpIgnoreKeepalive = _GeneralDhcpIgnoreKeepalive_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 20, 30),
    _GeneralDhcpIgnoreKeepalive_Type()
)
generalDhcpIgnoreKeepalive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generalDhcpIgnoreKeepalive.setStatus("mandatory")
_GeneralSecureRealPortNumber_Type = Integer32
_GeneralSecureRealPortNumber_Object = MibScalar
generalSecureRealPortNumber = _GeneralSecureRealPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 20, 31),
    _GeneralSecureRealPortNumber_Type()
)
generalSecureRealPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generalSecureRealPortNumber.setStatus("mandatory")
_GeneralDhcpClientFqdnOption_Type = Switch
_GeneralDhcpClientFqdnOption_Object = MibScalar
generalDhcpClientFqdnOption = _GeneralDhcpClientFqdnOption_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 20, 32),
    _GeneralDhcpClientFqdnOption_Type()
)
generalDhcpClientFqdnOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generalDhcpClientFqdnOption.setStatus("mandatory")
_Processor_ObjectIdentity = ObjectIdentity
processor = _Processor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 21)
)


class _ProcessorCurrentUtilization_Type(Integer32):
    """Custom type processorCurrentUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ProcessorCurrentUtilization_Type.__name__ = "Integer32"
_ProcessorCurrentUtilization_Object = MibScalar
processorCurrentUtilization = _ProcessorCurrentUtilization_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 21, 11),
    _ProcessorCurrentUtilization_Type()
)
processorCurrentUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorCurrentUtilization.setStatus("mandatory")
_Memory_ObjectIdentity = ObjectIdentity
memory = _Memory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 22)
)
_MemoryTotalMemory_Type = Integer32
_MemoryTotalMemory_Object = MibScalar
memoryTotalMemory = _MemoryTotalMemory_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 22, 11),
    _MemoryTotalMemory_Type()
)
memoryTotalMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryTotalMemory.setStatus("mandatory")
_MemoryAvailable_Type = Integer32
_MemoryAvailable_Object = MibScalar
memoryAvailable = _MemoryAvailable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 22, 12),
    _MemoryAvailable_Type()
)
memoryAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryAvailable.setStatus("mandatory")
_MemoryLargestBlockAvailable_Type = Integer32
_MemoryLargestBlockAvailable_Object = MibScalar
memoryLargestBlockAvailable = _MemoryLargestBlockAvailable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 22, 13),
    _MemoryLargestBlockAvailable_Type()
)
memoryLargestBlockAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryLargestBlockAvailable.setStatus("mandatory")
_MemorySuccessfulAllocates_Type = Integer32
_MemorySuccessfulAllocates_Object = MibScalar
memorySuccessfulAllocates = _MemorySuccessfulAllocates_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 22, 14),
    _MemorySuccessfulAllocates_Type()
)
memorySuccessfulAllocates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memorySuccessfulAllocates.setStatus("mandatory")
_MemoryFailedAllocates_Type = Integer32
_MemoryFailedAllocates_Object = MibScalar
memoryFailedAllocates = _MemoryFailedAllocates_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 22, 15),
    _MemoryFailedAllocates_Type()
)
memoryFailedAllocates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryFailedAllocates.setStatus("mandatory")
_Time_ObjectIdentity = ObjectIdentity
time = _Time_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 23)
)


class _TimeSystemCurrent_Type(DisplayString):
    """Custom type timeSystemCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_TimeSystemCurrent_Type.__name__ = "DisplayString"
_TimeSystemCurrent_Object = MibScalar
timeSystemCurrent = _TimeSystemCurrent_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 23, 11),
    _TimeSystemCurrent_Type()
)
timeSystemCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeSystemCurrent.setStatus("mandatory")
_Boot_ObjectIdentity = ObjectIdentity
boot = _Boot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 24)
)
_BootReboot_Type = Action
_BootReboot_Object = MibScalar
bootReboot = _BootReboot_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 24, 11),
    _BootReboot_Type()
)
bootReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootReboot.setStatus("mandatory")
_BootDHCPBoot_Type = Switch
_BootDHCPBoot_Object = MibScalar
bootDHCPBoot = _BootDHCPBoot_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 24, 12),
    _BootDHCPBoot_Type()
)
bootDHCPBoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootDHCPBoot.setStatus("mandatory")
_Port_ObjectIdentity = ObjectIdentity
port = _Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 25)
)
_AuthTable_Object = MibTable
authTable = _AuthTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 25, 11)
)
if mibBuilder.loadTexts:
    authTable.setStatus("mandatory")
_AuthEntry_Object = MibTableRow
authEntry = _AuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 25, 11, 1)
)
authEntry.setIndexNames(
    (0, "DIGI-PORTSERVER-TS-MIB", "authIndex"),
)
if mibBuilder.loadTexts:
    authEntry.setStatus("mandatory")


class _AuthIndex_Type(Integer32):
    """Custom type authIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AuthIndex_Type.__name__ = "Integer32"
_AuthIndex_Object = MibTableColumn
authIndex = _AuthIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 25, 11, 1, 11),
    _AuthIndex_Type()
)
authIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authIndex.setStatus("mandatory")
_AuthIp_Type = IpAddress
_AuthIp_Object = MibTableColumn
authIp = _AuthIp_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 25, 11, 1, 12),
    _AuthIp_Type()
)
authIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authIp.setStatus("mandatory")
_AuthMask_Type = IpAddress
_AuthMask_Object = MibTableColumn
authMask = _AuthMask_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 25, 11, 1, 13),
    _AuthMask_Type()
)
authMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authMask.setStatus("mandatory")
_AuthRealPort_Type = DisplayString
_AuthRealPort_Object = MibTableColumn
authRealPort = _AuthRealPort_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 25, 11, 1, 14),
    _AuthRealPort_Type()
)
authRealPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authRealPort.setStatus("mandatory")
_AuthLogin_Type = DisplayString
_AuthLogin_Object = MibTableColumn
authLogin = _AuthLogin_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 25, 11, 1, 15),
    _AuthLogin_Type()
)
authLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authLogin.setStatus("mandatory")
_AuthUnrestricted_Type = DisplayString
_AuthUnrestricted_Object = MibTableColumn
authUnrestricted = _AuthUnrestricted_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 25, 11, 1, 16),
    _AuthUnrestricted_Type()
)
authUnrestricted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authUnrestricted.setStatus("mandatory")
_LineTable_Object = MibTable
lineTable = _LineTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 25, 12)
)
if mibBuilder.loadTexts:
    lineTable.setStatus("mandatory")
_LineEntry_Object = MibTableRow
lineEntry = _LineEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 25, 12, 1)
)
lineEntry.setIndexNames(
    (0, "DIGI-PORTSERVER-TS-MIB", "lineIndex"),
)
if mibBuilder.loadTexts:
    lineEntry.setStatus("mandatory")


class _LineIndex_Type(Integer32):
    """Custom type lineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_LineIndex_Type.__name__ = "Integer32"
_LineIndex_Object = MibTableColumn
lineIndex = _LineIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 25, 12, 1, 11),
    _LineIndex_Type()
)
lineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineIndex.setStatus("mandatory")


class _LineResetSettings_Type(Integer32):
    """Custom type lineResetSettings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ready", 1),
          ("factory", 2),
          ("nvram", 3))
    )


_LineResetSettings_Type.__name__ = "Integer32"
_LineResetSettings_Object = MibTableColumn
lineResetSettings = _LineResetSettings_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 25, 12, 1, 12),
    _LineResetSettings_Type()
)
lineResetSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineResetSettings.setStatus("mandatory")


class _LineBreak_Type(Integer32):
    """Custom type lineBreak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("send", 2),
          ("escape", 3))
    )


_LineBreak_Type.__name__ = "Integer32"
_LineBreak_Object = MibTableColumn
lineBreak = _LineBreak_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 25, 12, 1, 13),
    _LineBreak_Type()
)
lineBreak.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineBreak.setStatus("mandatory")


class _LineError_Type(Integer32):
    """Custom type lineError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("null", 2),
          ("dos", 3),
          ("parMk", 4))
    )


_LineError_Type.__name__ = "Integer32"
_LineError_Object = MibTableColumn
lineError = _LineError_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 25, 12, 1, 14),
    _LineError_Type()
)
lineError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineError.setStatus("mandatory")
_LineInPCK_Type = Switch
_LineInPCK_Object = MibTableColumn
lineInPCK = _LineInPCK_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 25, 12, 1, 15),
    _LineInPCK_Type()
)
lineInPCK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineInPCK.setStatus("mandatory")
_LineIStrip_Type = Switch
_LineIStrip_Object = MibTableColumn
lineIStrip = _LineIStrip_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 25, 12, 1, 16),
    _LineIStrip_Type()
)
lineIStrip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineIStrip.setStatus("mandatory")
_LineOnLCR_Type = Switch
_LineOnLCR_Object = MibTableColumn
lineOnLCR = _LineOnLCR_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 25, 12, 1, 17),
    _LineOnLCR_Type()
)
lineOnLCR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineOnLCR.setStatus("mandatory")
_LineOTab_Type = Switch
_LineOTab_Object = MibTableColumn
lineOTab = _LineOTab_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 25, 12, 1, 18),
    _LineOTab_Type()
)
lineOTab.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineOTab.setStatus("mandatory")
_PortsTable_Object = MibTable
portsTable = _PortsTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 25, 13)
)
if mibBuilder.loadTexts:
    portsTable.setStatus("mandatory")
_PortsEntry_Object = MibTableRow
portsEntry = _PortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 25, 13, 1)
)
portsEntry.setIndexNames(
    (0, "DIGI-PORTSERVER-TS-MIB", "portsIndex"),
)
if mibBuilder.loadTexts:
    portsEntry.setStatus("mandatory")


class _PortsIndex_Type(Integer32):
    """Custom type portsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_PortsIndex_Type.__name__ = "Integer32"
_PortsIndex_Object = MibTableColumn
portsIndex = _PortsIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 25, 13, 1, 11),
    _PortsIndex_Type()
)
portsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portsIndex.setStatus("mandatory")


class _PortsResetSettings_Type(Integer32):
    """Custom type portsResetSettings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ready", 1),
          ("factory", 2),
          ("nvram", 3))
    )


_PortsResetSettings_Type.__name__ = "Integer32"
_PortsResetSettings_Object = MibTableColumn
portsResetSettings = _PortsResetSettings_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 25, 13, 1, 12),
    _PortsResetSettings_Type()
)
portsResetSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portsResetSettings.setStatus("mandatory")
_PortsAutoConnect_Type = Switch
_PortsAutoConnect_Object = MibTableColumn
portsAutoConnect = _PortsAutoConnect_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 25, 13, 1, 13),
    _PortsAutoConnect_Type()
)
portsAutoConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portsAutoConnect.setStatus("mandatory")
_PortsBinaryMode_Type = Switch
_PortsBinaryMode_Object = MibTableColumn
portsBinaryMode = _PortsBinaryMode_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 25, 13, 1, 14),
    _PortsBinaryMode_Type()
)
portsBinaryMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portsBinaryMode.setStatus("mandatory")


class _PortsDevice_Type(Integer32):
    """Custom type portsDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("term", 1),
          ("prn", 2),
          ("min", 3),
          ("mout", 4),
          ("mio", 5),
          ("host", 6),
          ("hdial", 7),
          ("hio", 8),
          ("rp", 9),
          ("ia", 10),
          ("power", 11),
          ("pmodem", 12),
          ("trane", 13))
    )


_PortsDevice_Type.__name__ = "Integer32"
_PortsDevice_Object = MibTableColumn
portsDevice = _PortsDevice_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 25, 13, 1, 15),
    _PortsDevice_Type()
)
portsDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portsDevice.setStatus("mandatory")
_PortsDPort_Type = Integer32
_PortsDPort_Object = MibTableColumn
portsDPort = _PortsDPort_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 25, 13, 1, 16),
    _PortsDPort_Type()
)
portsDPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portsDPort.setStatus("mandatory")
_PortsEDelay_Type = Integer32
_PortsEDelay_Object = MibTableColumn
portsEDelay = _PortsEDelay_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 25, 13, 1, 17),
    _PortsEDelay_Type()
)
portsEDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portsEDelay.setStatus("mandatory")
_PortsGroup_Type = Integer32
_PortsGroup_Object = MibTableColumn
portsGroup = _PortsGroup_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 25, 13, 1, 18),
    _PortsGroup_Type()
)
portsGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portsGroup.setStatus("mandatory")


class _PortsSession_Type(Integer32):
    """Custom type portsSession based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_PortsSession_Type.__name__ = "Integer32"
_PortsSession_Object = MibTableColumn
portsSession = _PortsSession_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 25, 13, 1, 19),
    _PortsSession_Type()
)
portsSession.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portsSession.setStatus("mandatory")
_PortsTermType_Type = DisplayString
_PortsTermType_Object = MibTableColumn
portsTermType = _PortsTermType_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 25, 13, 1, 20),
    _PortsTermType_Type()
)
portsTermType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portsTermType.setStatus("mandatory")
_PortsUID_Type = Integer32
_PortsUID_Object = MibTableColumn
portsUID = _PortsUID_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 25, 13, 1, 21),
    _PortsUID_Type()
)
portsUID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portsUID.setStatus("mandatory")
_PortsDestIP_Type = IpAddress
_PortsDestIP_Object = MibTableColumn
portsDestIP = _PortsDestIP_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 25, 13, 1, 22),
    _PortsDestIP_Type()
)
portsDestIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portsDestIP.setStatus("deprecated")
_PortsAltIP_Type = IpAddress
_PortsAltIP_Object = MibTableColumn
portsAltIP = _PortsAltIP_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 25, 13, 1, 23),
    _PortsAltIP_Type()
)
portsAltIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portsAltIP.setStatus("mandatory")
_PortsKeepalive_Type = Switch
_PortsKeepalive_Object = MibTableColumn
portsKeepalive = _PortsKeepalive_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 25, 13, 1, 24),
    _PortsKeepalive_Type()
)
portsKeepalive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portsKeepalive.setStatus("mandatory")


class _PortsFlushStChar_Type(Integer32):
    """Custom type portsFlushStChar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("on", 2),
          ("off", 3))
    )


_PortsFlushStChar_Type.__name__ = "Integer32"
_PortsFlushStChar_Object = MibTableColumn
portsFlushStChar = _PortsFlushStChar_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 25, 13, 1, 25),
    _PortsFlushStChar_Type()
)
portsFlushStChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portsFlushStChar.setStatus("mandatory")


class _PortsAutoService_Type(Integer32):
    """Custom type portsAutoService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("raw", 2),
          ("rlogin", 3),
          ("telnet", 4),
          ("ssl", 5))
    )


_PortsAutoService_Type.__name__ = "Integer32"
_PortsAutoService_Object = MibTableColumn
portsAutoService = _PortsAutoService_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 25, 13, 1, 26),
    _PortsAutoService_Type()
)
portsAutoService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portsAutoService.setStatus("mandatory")


class _PortsResetSerialSettings_Type(Integer32):
    """Custom type portsResetSerialSettings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ready", 1),
          ("factory", 2),
          ("nvram", 3))
    )


_PortsResetSerialSettings_Type.__name__ = "Integer32"
_PortsResetSerialSettings_Object = MibTableColumn
portsResetSerialSettings = _PortsResetSerialSettings_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 25, 13, 1, 27),
    _PortsResetSerialSettings_Type()
)
portsResetSerialSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portsResetSerialSettings.setStatus("mandatory")
_PortsAutoDest_Type = DisplayString
_PortsAutoDest_Object = MibTableColumn
portsAutoDest = _PortsAutoDest_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 25, 13, 1, 28),
    _PortsAutoDest_Type()
)
portsAutoDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portsAutoDest.setStatus("mandatory")
_PortsName_Type = DisplayString
_PortsName_Object = MibTableColumn
portsName = _PortsName_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 25, 13, 1, 29),
    _PortsName_Type()
)
portsName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portsName.setStatus("mandatory")
_FlowTable_Object = MibTable
flowTable = _FlowTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 25, 14)
)
if mibBuilder.loadTexts:
    flowTable.setStatus("mandatory")
_FlowEntry_Object = MibTableRow
flowEntry = _FlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 25, 14, 1)
)
flowEntry.setIndexNames(
    (0, "DIGI-PORTSERVER-TS-MIB", "portsIndex"),
)
if mibBuilder.loadTexts:
    flowEntry.setStatus("mandatory")


class _FlowIndex_Type(Integer32):
    """Custom type flowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_FlowIndex_Type.__name__ = "Integer32"
_FlowIndex_Object = MibTableColumn
flowIndex = _FlowIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 25, 14, 1, 11),
    _FlowIndex_Type()
)
flowIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowIndex.setStatus("mandatory")


class _FlowResetSettings_Type(Integer32):
    """Custom type flowResetSettings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ready", 1),
          ("factory", 2),
          ("nvram", 3))
    )


_FlowResetSettings_Type.__name__ = "Integer32"
_FlowResetSettings_Object = MibTableColumn
flowResetSettings = _FlowResetSettings_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 25, 14, 1, 12),
    _FlowResetSettings_Type()
)
flowResetSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowResetSettings.setStatus("mandatory")
_FlowAltPin_Type = Switch
_FlowAltPin_Object = MibTableColumn
flowAltPin = _FlowAltPin_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 25, 14, 1, 13),
    _FlowAltPin_Type()
)
flowAltPin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowAltPin.setStatus("mandatory")
_FlowForceDCD_Type = Switch
_FlowForceDCD_Object = MibTableColumn
flowForceDCD = _FlowForceDCD_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 25, 14, 1, 14),
    _FlowForceDCD_Type()
)
flowForceDCD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowForceDCD.setStatus("mandatory")


class _FlowRts_Type(Integer32):
    """Custom type flowRts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("toggle", 3))
    )


_FlowRts_Type.__name__ = "Integer32"
_FlowRts_Object = MibTableColumn
flowRts = _FlowRts_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 25, 14, 1, 15),
    _FlowRts_Type()
)
flowRts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowRts.setStatus("mandatory")


class _FlowRtsPreDelay_Type(Integer32):
    """Custom type flowRtsPreDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_FlowRtsPreDelay_Type.__name__ = "Integer32"
_FlowRtsPreDelay_Object = MibTableColumn
flowRtsPreDelay = _FlowRtsPreDelay_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 25, 14, 1, 16),
    _FlowRtsPreDelay_Type()
)
flowRtsPreDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowRtsPreDelay.setStatus("mandatory")


class _FlowRtsPostDelay_Type(Integer32):
    """Custom type flowRtsPostDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_FlowRtsPostDelay_Type.__name__ = "Integer32"
_FlowRtsPostDelay_Object = MibTableColumn
flowRtsPostDelay = _FlowRtsPostDelay_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 25, 14, 1, 17),
    _FlowRtsPostDelay_Type()
)
flowRtsPostDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowRtsPostDelay.setStatus("mandatory")
_Network_ObjectIdentity = ObjectIdentity
network = _Network_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 26)
)
_TcpOther_ObjectIdentity = ObjectIdentity
tcpOther = _TcpOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 26, 11)
)


class _TcpOtherRetransTimeout_Type(Integer32):
    """Custom type tcpOtherRetransTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 240),
    )


_TcpOtherRetransTimeout_Type.__name__ = "Integer32"
_TcpOtherRetransTimeout_Object = MibScalar
tcpOtherRetransTimeout = _TcpOtherRetransTimeout_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 26, 11, 11),
    _TcpOtherRetransTimeout_Type()
)
tcpOtherRetransTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpOtherRetransTimeout.setStatus("mandatory")
_TcpOtherKeepAliveActive_Type = Switch
_TcpOtherKeepAliveActive_Object = MibScalar
tcpOtherKeepAliveActive = _TcpOtherKeepAliveActive_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 26, 11, 12),
    _TcpOtherKeepAliveActive_Type()
)
tcpOtherKeepAliveActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpOtherKeepAliveActive.setStatus("mandatory")


class _TcpOtherKeepAliveIdle_Type(Integer32):
    """Custom type tcpOtherKeepAliveIdle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 86400),
    )


_TcpOtherKeepAliveIdle_Type.__name__ = "Integer32"
_TcpOtherKeepAliveIdle_Object = MibScalar
tcpOtherKeepAliveIdle = _TcpOtherKeepAliveIdle_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 26, 11, 13),
    _TcpOtherKeepAliveIdle_Type()
)
tcpOtherKeepAliveIdle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpOtherKeepAliveIdle.setStatus("mandatory")
_TcpOtherKeepAliveGarbage_Type = Switch
_TcpOtherKeepAliveGarbage_Object = MibScalar
tcpOtherKeepAliveGarbage = _TcpOtherKeepAliveGarbage_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 26, 11, 14),
    _TcpOtherKeepAliveGarbage_Type()
)
tcpOtherKeepAliveGarbage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpOtherKeepAliveGarbage.setStatus("mandatory")


class _TcpOtherProbeCounter_Type(Integer32):
    """Custom type tcpOtherProbeCounter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_TcpOtherProbeCounter_Type.__name__ = "Integer32"
_TcpOtherProbeCounter_Object = MibScalar
tcpOtherProbeCounter = _TcpOtherProbeCounter_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 26, 11, 15),
    _TcpOtherProbeCounter_Type()
)
tcpOtherProbeCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpOtherProbeCounter.setStatus("mandatory")


class _TcpOtherProbeInterval_Type(Integer32):
    """Custom type tcpOtherProbeInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 75),
    )


_TcpOtherProbeInterval_Type.__name__ = "Integer32"
_TcpOtherProbeInterval_Object = MibScalar
tcpOtherProbeInterval = _TcpOtherProbeInterval_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 26, 11, 16),
    _TcpOtherProbeInterval_Type()
)
tcpOtherProbeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpOtherProbeInterval.setStatus("mandatory")
_Forwarding_ObjectIdentity = ObjectIdentity
forwarding = _Forwarding_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 26, 12)
)
_ForwardingAdvertise_Type = Integer32
_ForwardingAdvertise_Object = MibScalar
forwardingAdvertise = _ForwardingAdvertise_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 26, 12, 11),
    _ForwardingAdvertise_Type()
)
forwardingAdvertise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    forwardingAdvertise.setStatus("mandatory")
_ForwardingICMPDiscovery_Type = Switch
_ForwardingICMPDiscovery_Object = MibScalar
forwardingICMPDiscovery = _ForwardingICMPDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 26, 12, 12),
    _ForwardingICMPDiscovery_Type()
)
forwardingICMPDiscovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    forwardingICMPDiscovery.setStatus("mandatory")
_ForwardingICMPSendRedirects_Type = Switch
_ForwardingICMPSendRedirects_Object = MibScalar
forwardingICMPSendRedirects = _ForwardingICMPSendRedirects_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 26, 12, 13),
    _ForwardingICMPSendRedirects_Type()
)
forwardingICMPSendRedirects.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    forwardingICMPSendRedirects.setStatus("mandatory")
_ForwardingICMPMaskServer_Type = Switch
_ForwardingICMPMaskServer_Object = MibScalar
forwardingICMPMaskServer = _ForwardingICMPMaskServer_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 26, 12, 14),
    _ForwardingICMPMaskServer_Type()
)
forwardingICMPMaskServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    forwardingICMPMaskServer.setStatus("mandatory")
_ForwardingIGMP_Type = Switch
_ForwardingIGMP_Object = MibScalar
forwardingIGMP = _ForwardingIGMP_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 26, 12, 15),
    _ForwardingIGMP_Type()
)
forwardingIGMP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    forwardingIGMP.setStatus("mandatory")
_ForwardingPoisonReverse_Type = Switch
_ForwardingPoisonReverse_Object = MibScalar
forwardingPoisonReverse = _ForwardingPoisonReverse_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 26, 12, 16),
    _ForwardingPoisonReverse_Type()
)
forwardingPoisonReverse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    forwardingPoisonReverse.setStatus("mandatory")
_ForwardingProxyArp_Type = Switch
_ForwardingProxyArp_Object = MibScalar
forwardingProxyArp = _ForwardingProxyArp_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 26, 12, 17),
    _ForwardingProxyArp_Type()
)
forwardingProxyArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    forwardingProxyArp.setStatus("mandatory")


class _ForwardingState_Type(Integer32):
    """Custom type forwardingState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("passive", 2),
          ("active", 3))
    )


_ForwardingState_Type.__name__ = "Integer32"
_ForwardingState_Object = MibScalar
forwardingState = _ForwardingState_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 26, 12, 18),
    _ForwardingState_Type()
)
forwardingState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    forwardingState.setStatus("mandatory")
_ForwardingSplitHorizon_Type = Switch
_ForwardingSplitHorizon_Object = MibScalar
forwardingSplitHorizon = _ForwardingSplitHorizon_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 26, 12, 19),
    _ForwardingSplitHorizon_Type()
)
forwardingSplitHorizon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    forwardingSplitHorizon.setStatus("mandatory")


class _ForwardingTimeout_Type(Integer32):
    """Custom type forwardingTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 1080),
    )


_ForwardingTimeout_Type.__name__ = "Integer32"
_ForwardingTimeout_Object = MibScalar
forwardingTimeout = _ForwardingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 26, 12, 20),
    _ForwardingTimeout_Type()
)
forwardingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    forwardingTimeout.setStatus("mandatory")
_HostnameTable_Object = MibTable
hostnameTable = _HostnameTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 26, 13)
)
if mibBuilder.loadTexts:
    hostnameTable.setStatus("mandatory")
_HostnameEntry_Object = MibTableRow
hostnameEntry = _HostnameEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 26, 13, 1)
)
hostnameEntry.setIndexNames(
    (0, "DIGI-PORTSERVER-TS-MIB", "hostIndex"),
)
if mibBuilder.loadTexts:
    hostnameEntry.setStatus("mandatory")


class _HostIndex_Type(Integer32):
    """Custom type hostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_HostIndex_Type.__name__ = "Integer32"
_HostIndex_Object = MibTableColumn
hostIndex = _HostIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 26, 13, 1, 11),
    _HostIndex_Type()
)
hostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostIndex.setStatus("mandatory")
_HostIP_Type = IpAddress
_HostIP_Object = MibTableColumn
hostIP = _HostIP_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 26, 13, 1, 12),
    _HostIP_Type()
)
hostIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostIP.setStatus("mandatory")
_HostName_Type = DisplayString
_HostName_Object = MibTableColumn
hostName = _HostName_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 26, 13, 1, 13),
    _HostName_Type()
)
hostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostName.setStatus("mandatory")
_Trace_ObjectIdentity = ObjectIdentity
trace = _Trace_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 26, 14)
)
_TraceState_Type = Switch
_TraceState_Object = MibScalar
traceState = _TraceState_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 26, 14, 11),
    _TraceState_Type()
)
traceState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceState.setStatus("mandatory")


class _TraceMode_Type(Integer32):
    """Custom type traceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("historical", 1),
          ("concurrent", 2))
    )


_TraceMode_Type.__name__ = "Integer32"
_TraceMode_Object = MibScalar
traceMode = _TraceMode_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 26, 14, 12),
    _TraceMode_Type()
)
traceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceMode.setStatus("mandatory")
_TraceSysLogState_Type = Switch
_TraceSysLogState_Object = MibScalar
traceSysLogState = _TraceSysLogState_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 26, 14, 13),
    _TraceSysLogState_Type()
)
traceSysLogState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceSysLogState.setStatus("mandatory")
_TraceLogHost_Type = IpAddress
_TraceLogHost_Object = MibScalar
traceLogHost = _TraceLogHost_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 26, 14, 14),
    _TraceLogHost_Type()
)
traceLogHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceLogHost.setStatus("mandatory")
_TraceTable_Object = MibTable
traceTable = _TraceTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 26, 14, 15)
)
if mibBuilder.loadTexts:
    traceTable.setStatus("mandatory")
_TraceEntry_Object = MibTableRow
traceEntry = _TraceEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 26, 14, 15, 1)
)
traceEntry.setIndexNames(
    (0, "DIGI-PORTSERVER-TS-MIB", "traceIndex"),
)
if mibBuilder.loadTexts:
    traceEntry.setStatus("mandatory")


class _TraceIndex_Type(Integer32):
    """Custom type traceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 17),
    )


_TraceIndex_Type.__name__ = "Integer32"
_TraceIndex_Object = MibTableColumn
traceIndex = _TraceIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 26, 14, 15, 1, 11),
    _TraceIndex_Type()
)
traceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceIndex.setStatus("mandatory")


class _TraceType_Type(Integer32):
    """Custom type traceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32)
        )
    )
    namedValues = NamedValues(
        *(("arp", 1),
          ("cache", 2),
          ("connect", 3),
          ("dialer", 4),
          ("dhcp", 5),
          ("dns", 6),
          ("esc", 7),
          ("ether", 8),
          ("frame", 9),
          ("forwarding", 10),
          ("icmp", 11),
          ("inetd", 12),
          ("ip", 13),
          ("lpd", 14),
          ("lpdA", 15),
          ("lpdH", 16),
          ("netd", 17),
          ("portsw", 18),
          ("ppp", 19),
          ("radius", 20),
          ("realp", 21),
          ("rlogin", 22),
          ("routed", 23),
          ("serial", 24),
          ("snmp", 25),
          ("stream", 26),
          ("tcp", 27),
          ("telnet", 28),
          ("udp", 29),
          ("user", 30),
          ("vj", 31),
          ("wan", 32))
    )


_TraceType_Type.__name__ = "Integer32"
_TraceType_Object = MibTableColumn
traceType = _TraceType_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 26, 14, 15, 1, 12),
    _TraceType_Type()
)
traceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceType.setStatus("mandatory")


class _TraceSeverity_Type(Integer32):
    """Custom type traceSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("warning", 2),
          ("info", 3),
          ("debug", 4),
          ("ignore", 5))
    )


_TraceSeverity_Type.__name__ = "Integer32"
_TraceSeverity_Object = MibTableColumn
traceSeverity = _TraceSeverity_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 26, 14, 15, 1, 13),
    _TraceSeverity_Type()
)
traceSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceSeverity.setStatus("mandatory")
_AltIpTable_Object = MibTable
altIpTable = _AltIpTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 26, 15)
)
if mibBuilder.loadTexts:
    altIpTable.setStatus("mandatory")
_AltIpEntry_Object = MibTableRow
altIpEntry = _AltIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 26, 15, 1)
)
altIpEntry.setIndexNames(
    (0, "DIGI-PORTSERVER-TS-MIB", "altIpIndex"),
)
if mibBuilder.loadTexts:
    altIpEntry.setStatus("mandatory")
_AltIpIndex_Type = Integer32
_AltIpIndex_Object = MibTableColumn
altIpIndex = _AltIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 26, 15, 1, 11),
    _AltIpIndex_Type()
)
altIpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    altIpIndex.setStatus("mandatory")
_AltIpIp_Type = IpAddress
_AltIpIp_Object = MibTableColumn
altIpIp = _AltIpIp_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 26, 15, 1, 12),
    _AltIpIp_Type()
)
altIpIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    altIpIp.setStatus("mandatory")
_AltIpGroup_Type = Integer32
_AltIpGroup_Object = MibTableColumn
altIpGroup = _AltIpGroup_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 26, 15, 1, 13),
    _AltIpGroup_Type()
)
altIpGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    altIpGroup.setStatus("mandatory")
_SnmpOther_ObjectIdentity = ObjectIdentity
snmpOther = _SnmpOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 26, 16)
)
_SnmpTrapDest_Type = IpAddress
_SnmpTrapDest_Object = MibScalar
snmpTrapDest = _SnmpTrapDest_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 26, 16, 11),
    _SnmpTrapDest_Type()
)
snmpTrapDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapDest.setStatus("mandatory")
_SnmpLoginTraps_Type = Switch
_SnmpLoginTraps_Object = MibScalar
snmpLoginTraps = _SnmpLoginTraps_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 26, 16, 12),
    _SnmpLoginTraps_Type()
)
snmpLoginTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpLoginTraps.setStatus("mandatory")
_SnmpLinkUpTraps_Type = Switch
_SnmpLinkUpTraps_Object = MibScalar
snmpLinkUpTraps = _SnmpLinkUpTraps_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 26, 16, 13),
    _SnmpLinkUpTraps_Type()
)
snmpLinkUpTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpLinkUpTraps.setStatus("mandatory")
_SnmpColdStartTraps_Type = Switch
_SnmpColdStartTraps_Object = MibScalar
snmpColdStartTraps = _SnmpColdStartTraps_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 26, 16, 14),
    _SnmpColdStartTraps_Type()
)
snmpColdStartTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpColdStartTraps.setStatus("mandatory")
_Interface_ObjectIdentity = ObjectIdentity
interface = _Interface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27)
)
_KeyMapTable_Object = MibTable
keyMapTable = _KeyMapTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 11)
)
if mibBuilder.loadTexts:
    keyMapTable.setStatus("mandatory")
_KeyMapEntry_Object = MibTableRow
keyMapEntry = _KeyMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 11, 1)
)
keyMapEntry.setIndexNames(
    (0, "DIGI-PORTSERVER-TS-MIB", "keyMapIndex"),
)
if mibBuilder.loadTexts:
    keyMapEntry.setStatus("mandatory")


class _KeyMapIndex_Type(Integer32):
    """Custom type keyMapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_KeyMapIndex_Type.__name__ = "Integer32"
_KeyMapIndex_Object = MibTableColumn
keyMapIndex = _KeyMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 11, 1, 11),
    _KeyMapIndex_Type()
)
keyMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keyMapIndex.setStatus("mandatory")
_KeyMapEOF_Type = DisplayString
_KeyMapEOF_Object = MibTableColumn
keyMapEOF = _KeyMapEOF_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 11, 1, 12),
    _KeyMapEOF_Type()
)
keyMapEOF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keyMapEOF.setStatus("mandatory")
_KeyMapErase_Type = DisplayString
_KeyMapErase_Object = MibTableColumn
keyMapErase = _KeyMapErase_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 11, 1, 13),
    _KeyMapErase_Type()
)
keyMapErase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keyMapErase.setStatus("mandatory")
_KeyMapInterrupt_Type = DisplayString
_KeyMapInterrupt_Object = MibTableColumn
keyMapInterrupt = _KeyMapInterrupt_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 11, 1, 14),
    _KeyMapInterrupt_Type()
)
keyMapInterrupt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keyMapInterrupt.setStatus("mandatory")
_KeyMapKill_Type = DisplayString
_KeyMapKill_Object = MibTableColumn
keyMapKill = _KeyMapKill_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 11, 1, 15),
    _KeyMapKill_Type()
)
keyMapKill.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keyMapKill.setStatus("mandatory")
_KeyMapTelnetEscape_Type = DisplayString
_KeyMapTelnetEscape_Object = MibTableColumn
keyMapTelnetEscape = _KeyMapTelnetEscape_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 11, 1, 16),
    _KeyMapTelnetEscape_Type()
)
keyMapTelnetEscape.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keyMapTelnetEscape.setStatus("mandatory")
_KeyMapXON_Type = DisplayString
_KeyMapXON_Object = MibTableColumn
keyMapXON = _KeyMapXON_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 11, 1, 17),
    _KeyMapXON_Type()
)
keyMapXON.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keyMapXON.setStatus("mandatory")
_KeyMapXOFF_Type = DisplayString
_KeyMapXOFF_Object = MibTableColumn
keyMapXOFF = _KeyMapXOFF_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 11, 1, 18),
    _KeyMapXOFF_Type()
)
keyMapXOFF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keyMapXOFF.setStatus("mandatory")
_KeyMapXONAlternate_Type = DisplayString
_KeyMapXONAlternate_Object = MibTableColumn
keyMapXONAlternate = _KeyMapXONAlternate_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 11, 1, 19),
    _KeyMapXONAlternate_Type()
)
keyMapXONAlternate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keyMapXONAlternate.setStatus("mandatory")
_KeyMapXOFFAlternate_Type = DisplayString
_KeyMapXOFFAlternate_Object = MibTableColumn
keyMapXOFFAlternate = _KeyMapXOFFAlternate_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 11, 1, 20),
    _KeyMapXOFFAlternate_Type()
)
keyMapXOFFAlternate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keyMapXOFFAlternate.setStatus("mandatory")
_LoginsTable_Object = MibTable
loginsTable = _LoginsTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 12)
)
if mibBuilder.loadTexts:
    loginsTable.setStatus("mandatory")
_LoginsEntry_Object = MibTableRow
loginsEntry = _LoginsEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 12, 1)
)
loginsEntry.setIndexNames(
    (0, "DIGI-PORTSERVER-TS-MIB", "loginsIndex"),
)
if mibBuilder.loadTexts:
    loginsEntry.setStatus("mandatory")


class _LoginsIndex_Type(Integer32):
    """Custom type loginsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_LoginsIndex_Type.__name__ = "Integer32"
_LoginsIndex_Object = MibTableColumn
loginsIndex = _LoginsIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 12, 1, 11),
    _LoginsIndex_Type()
)
loginsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loginsIndex.setStatus("mandatory")
_LoginPrompt_Type = DisplayString
_LoginPrompt_Object = MibTableColumn
loginPrompt = _LoginPrompt_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 12, 1, 12),
    _LoginPrompt_Type()
)
loginPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loginPrompt.setStatus("mandatory")
_LoginsAllowed_Type = Switch
_LoginsAllowed_Object = MibTableColumn
loginsAllowed = _LoginsAllowed_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 12, 1, 13),
    _LoginsAllowed_Type()
)
loginsAllowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loginsAllowed.setStatus("mandatory")
_LoginsPasswordPrompt_Type = DisplayString
_LoginsPasswordPrompt_Object = MibTableColumn
loginsPasswordPrompt = _LoginsPasswordPrompt_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 12, 1, 14),
    _LoginsPasswordPrompt_Type()
)
loginsPasswordPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loginsPasswordPrompt.setStatus("mandatory")
_LoginsPasswordRequired_Type = Switch
_LoginsPasswordRequired_Object = MibTableColumn
loginsPasswordRequired = _LoginsPasswordRequired_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 12, 1, 15),
    _LoginsPasswordRequired_Type()
)
loginsPasswordRequired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loginsPasswordRequired.setStatus("mandatory")
_LoginsVerboseLogins_Type = Switch
_LoginsVerboseLogins_Object = MibTableColumn
loginsVerboseLogins = _LoginsVerboseLogins_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 12, 1, 16),
    _LoginsVerboseLogins_Type()
)
loginsVerboseLogins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loginsVerboseLogins.setStatus("mandatory")
_LoginsCommandPrompt_Type = DisplayString
_LoginsCommandPrompt_Object = MibTableColumn
loginsCommandPrompt = _LoginsCommandPrompt_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 12, 1, 17),
    _LoginsCommandPrompt_Type()
)
loginsCommandPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loginsCommandPrompt.setStatus("mandatory")
_LoginsWriteEnabled_Type = Switch
_LoginsWriteEnabled_Object = MibTableColumn
loginsWriteEnabled = _LoginsWriteEnabled_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 12, 1, 18),
    _LoginsWriteEnabled_Type()
)
loginsWriteEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loginsWriteEnabled.setStatus("mandatory")
_LoginsRootPrompt_Type = DisplayString
_LoginsRootPrompt_Object = MibTableColumn
loginsRootPrompt = _LoginsRootPrompt_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 12, 1, 19),
    _LoginsRootPrompt_Type()
)
loginsRootPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loginsRootPrompt.setStatus("mandatory")
_MenuTable_Object = MibTable
menuTable = _MenuTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 13)
)
if mibBuilder.loadTexts:
    menuTable.setStatus("mandatory")
_MenuEntry_Object = MibTableRow
menuEntry = _MenuEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 13, 1)
)
menuEntry.setIndexNames(
    (0, "DIGI-PORTSERVER-TS-MIB", "menuIndex"),
)
if mibBuilder.loadTexts:
    menuEntry.setStatus("mandatory")


class _MenuIndex_Type(Integer32):
    """Custom type menuIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MenuIndex_Type.__name__ = "Integer32"
_MenuIndex_Object = MibTableColumn
menuIndex = _MenuIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 13, 1, 11),
    _MenuIndex_Type()
)
menuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    menuIndex.setStatus("mandatory")
_MenuName_Type = DisplayString
_MenuName_Object = MibTableColumn
menuName = _MenuName_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 13, 1, 12),
    _MenuName_Type()
)
menuName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    menuName.setStatus("mandatory")
_MenuTitleLine1_Type = DisplayString
_MenuTitleLine1_Object = MibTableColumn
menuTitleLine1 = _MenuTitleLine1_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 13, 1, 13),
    _MenuTitleLine1_Type()
)
menuTitleLine1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    menuTitleLine1.setStatus("mandatory")
_MenuTitleLine2_Type = DisplayString
_MenuTitleLine2_Object = MibTableColumn
menuTitleLine2 = _MenuTitleLine2_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 13, 1, 14),
    _MenuTitleLine2_Type()
)
menuTitleLine2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    menuTitleLine2.setStatus("mandatory")
_MenuText1_Type = DisplayString
_MenuText1_Object = MibTableColumn
menuText1 = _MenuText1_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 13, 1, 101),
    _MenuText1_Type()
)
menuText1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    menuText1.setStatus("mandatory")
_MenuText2_Type = DisplayString
_MenuText2_Object = MibTableColumn
menuText2 = _MenuText2_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 13, 1, 102),
    _MenuText2_Type()
)
menuText2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    menuText2.setStatus("mandatory")
_MenuText3_Type = DisplayString
_MenuText3_Object = MibTableColumn
menuText3 = _MenuText3_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 13, 1, 103),
    _MenuText3_Type()
)
menuText3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    menuText3.setStatus("mandatory")
_MenuText4_Type = DisplayString
_MenuText4_Object = MibTableColumn
menuText4 = _MenuText4_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 13, 1, 104),
    _MenuText4_Type()
)
menuText4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    menuText4.setStatus("mandatory")
_MenuText5_Type = DisplayString
_MenuText5_Object = MibTableColumn
menuText5 = _MenuText5_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 13, 1, 105),
    _MenuText5_Type()
)
menuText5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    menuText5.setStatus("mandatory")
_MenuText6_Type = DisplayString
_MenuText6_Object = MibTableColumn
menuText6 = _MenuText6_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 13, 1, 106),
    _MenuText6_Type()
)
menuText6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    menuText6.setStatus("mandatory")
_MenuText7_Type = DisplayString
_MenuText7_Object = MibTableColumn
menuText7 = _MenuText7_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 13, 1, 107),
    _MenuText7_Type()
)
menuText7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    menuText7.setStatus("mandatory")
_MenuText8_Type = DisplayString
_MenuText8_Object = MibTableColumn
menuText8 = _MenuText8_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 13, 1, 108),
    _MenuText8_Type()
)
menuText8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    menuText8.setStatus("mandatory")
_MenuText9_Type = DisplayString
_MenuText9_Object = MibTableColumn
menuText9 = _MenuText9_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 13, 1, 109),
    _MenuText9_Type()
)
menuText9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    menuText9.setStatus("mandatory")
_MenuText10_Type = DisplayString
_MenuText10_Object = MibTableColumn
menuText10 = _MenuText10_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 13, 1, 110),
    _MenuText10_Type()
)
menuText10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    menuText10.setStatus("mandatory")
_MenuText11_Type = DisplayString
_MenuText11_Object = MibTableColumn
menuText11 = _MenuText11_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 13, 1, 111),
    _MenuText11_Type()
)
menuText11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    menuText11.setStatus("mandatory")
_MenuText12_Type = DisplayString
_MenuText12_Object = MibTableColumn
menuText12 = _MenuText12_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 13, 1, 112),
    _MenuText12_Type()
)
menuText12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    menuText12.setStatus("mandatory")
_MenuText13_Type = DisplayString
_MenuText13_Object = MibTableColumn
menuText13 = _MenuText13_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 13, 1, 113),
    _MenuText13_Type()
)
menuText13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    menuText13.setStatus("mandatory")
_MenuText14_Type = DisplayString
_MenuText14_Object = MibTableColumn
menuText14 = _MenuText14_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 13, 1, 114),
    _MenuText14_Type()
)
menuText14.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    menuText14.setStatus("mandatory")
_MenuText15_Type = DisplayString
_MenuText15_Object = MibTableColumn
menuText15 = _MenuText15_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 13, 1, 115),
    _MenuText15_Type()
)
menuText15.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    menuText15.setStatus("mandatory")
_MenuText16_Type = DisplayString
_MenuText16_Object = MibTableColumn
menuText16 = _MenuText16_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 13, 1, 116),
    _MenuText16_Type()
)
menuText16.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    menuText16.setStatus("mandatory")
_MenuText17_Type = DisplayString
_MenuText17_Object = MibTableColumn
menuText17 = _MenuText17_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 13, 1, 117),
    _MenuText17_Type()
)
menuText17.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    menuText17.setStatus("mandatory")
_MenuText18_Type = DisplayString
_MenuText18_Object = MibTableColumn
menuText18 = _MenuText18_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 13, 1, 118),
    _MenuText18_Type()
)
menuText18.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    menuText18.setStatus("mandatory")
_MenuText19_Type = DisplayString
_MenuText19_Object = MibTableColumn
menuText19 = _MenuText19_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 13, 1, 119),
    _MenuText19_Type()
)
menuText19.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    menuText19.setStatus("mandatory")
_MenuText20_Type = DisplayString
_MenuText20_Object = MibTableColumn
menuText20 = _MenuText20_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 13, 1, 120),
    _MenuText20_Type()
)
menuText20.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    menuText20.setStatus("mandatory")
_MenuCommand1_Type = DisplayString
_MenuCommand1_Object = MibTableColumn
menuCommand1 = _MenuCommand1_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 13, 1, 201),
    _MenuCommand1_Type()
)
menuCommand1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    menuCommand1.setStatus("mandatory")
_MenuCommand2_Type = DisplayString
_MenuCommand2_Object = MibTableColumn
menuCommand2 = _MenuCommand2_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 13, 1, 202),
    _MenuCommand2_Type()
)
menuCommand2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    menuCommand2.setStatus("mandatory")
_MenuCommand3_Type = DisplayString
_MenuCommand3_Object = MibTableColumn
menuCommand3 = _MenuCommand3_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 13, 1, 203),
    _MenuCommand3_Type()
)
menuCommand3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    menuCommand3.setStatus("mandatory")
_MenuCommand4_Type = DisplayString
_MenuCommand4_Object = MibTableColumn
menuCommand4 = _MenuCommand4_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 13, 1, 204),
    _MenuCommand4_Type()
)
menuCommand4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    menuCommand4.setStatus("mandatory")
_MenuCommand5_Type = DisplayString
_MenuCommand5_Object = MibTableColumn
menuCommand5 = _MenuCommand5_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 13, 1, 205),
    _MenuCommand5_Type()
)
menuCommand5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    menuCommand5.setStatus("mandatory")
_MenuCommand6_Type = DisplayString
_MenuCommand6_Object = MibTableColumn
menuCommand6 = _MenuCommand6_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 13, 1, 206),
    _MenuCommand6_Type()
)
menuCommand6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    menuCommand6.setStatus("mandatory")
_MenuCommand7_Type = DisplayString
_MenuCommand7_Object = MibTableColumn
menuCommand7 = _MenuCommand7_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 13, 1, 207),
    _MenuCommand7_Type()
)
menuCommand7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    menuCommand7.setStatus("mandatory")
_MenuCommand8_Type = DisplayString
_MenuCommand8_Object = MibTableColumn
menuCommand8 = _MenuCommand8_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 13, 1, 208),
    _MenuCommand8_Type()
)
menuCommand8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    menuCommand8.setStatus("mandatory")
_MenuCommand9_Type = DisplayString
_MenuCommand9_Object = MibTableColumn
menuCommand9 = _MenuCommand9_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 13, 1, 209),
    _MenuCommand9_Type()
)
menuCommand9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    menuCommand9.setStatus("mandatory")
_MenuCommand10_Type = DisplayString
_MenuCommand10_Object = MibTableColumn
menuCommand10 = _MenuCommand10_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 13, 1, 210),
    _MenuCommand10_Type()
)
menuCommand10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    menuCommand10.setStatus("mandatory")
_MenuCommand11_Type = DisplayString
_MenuCommand11_Object = MibTableColumn
menuCommand11 = _MenuCommand11_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 13, 1, 211),
    _MenuCommand11_Type()
)
menuCommand11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    menuCommand11.setStatus("mandatory")
_MenuCommand12_Type = DisplayString
_MenuCommand12_Object = MibTableColumn
menuCommand12 = _MenuCommand12_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 13, 1, 212),
    _MenuCommand12_Type()
)
menuCommand12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    menuCommand12.setStatus("mandatory")
_MenuCommand13_Type = DisplayString
_MenuCommand13_Object = MibTableColumn
menuCommand13 = _MenuCommand13_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 13, 1, 213),
    _MenuCommand13_Type()
)
menuCommand13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    menuCommand13.setStatus("mandatory")
_MenuCommand14_Type = DisplayString
_MenuCommand14_Object = MibTableColumn
menuCommand14 = _MenuCommand14_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 13, 1, 214),
    _MenuCommand14_Type()
)
menuCommand14.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    menuCommand14.setStatus("mandatory")
_MenuCommand15_Type = DisplayString
_MenuCommand15_Object = MibTableColumn
menuCommand15 = _MenuCommand15_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 13, 1, 215),
    _MenuCommand15_Type()
)
menuCommand15.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    menuCommand15.setStatus("mandatory")
_MenuCommand16_Type = DisplayString
_MenuCommand16_Object = MibTableColumn
menuCommand16 = _MenuCommand16_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 13, 1, 216),
    _MenuCommand16_Type()
)
menuCommand16.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    menuCommand16.setStatus("mandatory")
_MenuCommand17_Type = DisplayString
_MenuCommand17_Object = MibTableColumn
menuCommand17 = _MenuCommand17_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 13, 1, 217),
    _MenuCommand17_Type()
)
menuCommand17.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    menuCommand17.setStatus("mandatory")
_MenuCommand18_Type = DisplayString
_MenuCommand18_Object = MibTableColumn
menuCommand18 = _MenuCommand18_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 13, 1, 218),
    _MenuCommand18_Type()
)
menuCommand18.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    menuCommand18.setStatus("mandatory")
_MenuCommand19_Type = DisplayString
_MenuCommand19_Object = MibTableColumn
menuCommand19 = _MenuCommand19_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 13, 1, 219),
    _MenuCommand19_Type()
)
menuCommand19.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    menuCommand19.setStatus("mandatory")
_MenuCommand20_Type = DisplayString
_MenuCommand20_Object = MibTableColumn
menuCommand20 = _MenuCommand20_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 13, 1, 220),
    _MenuCommand20_Type()
)
menuCommand20.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    menuCommand20.setStatus("mandatory")
_TerminalTable_Object = MibTable
terminalTable = _TerminalTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 14)
)
if mibBuilder.loadTexts:
    terminalTable.setStatus("mandatory")
_TerminalEntry_Object = MibTableRow
terminalEntry = _TerminalEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 14, 1)
)
terminalEntry.setIndexNames(
    (0, "DIGI-PORTSERVER-TS-MIB", "terminalIndex"),
)
if mibBuilder.loadTexts:
    terminalEntry.setStatus("mandatory")


class _TerminalIndex_Type(Integer32):
    """Custom type terminalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_TerminalIndex_Type.__name__ = "Integer32"
_TerminalIndex_Object = MibTableColumn
terminalIndex = _TerminalIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 14, 1, 11),
    _TerminalIndex_Type()
)
terminalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    terminalIndex.setStatus("mandatory")
_TerminalType_Type = DisplayString
_TerminalType_Object = MibTableColumn
terminalType = _TerminalType_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 14, 1, 12),
    _TerminalType_Type()
)
terminalType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminalType.setStatus("mandatory")
_TerminalNumberofPages_Type = Integer32
_TerminalNumberofPages_Object = MibTableColumn
terminalNumberofPages = _TerminalNumberofPages_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 14, 1, 13),
    _TerminalNumberofPages_Type()
)
terminalNumberofPages.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminalNumberofPages.setStatus("mandatory")
_TerminalClearSequence_Type = DisplayString
_TerminalClearSequence_Object = MibTableColumn
terminalClearSequence = _TerminalClearSequence_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 14, 1, 14),
    _TerminalClearSequence_Type()
)
terminalClearSequence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminalClearSequence.setStatus("mandatory")
_TerminalSessionSequence1_Type = DisplayString
_TerminalSessionSequence1_Object = MibTableColumn
terminalSessionSequence1 = _TerminalSessionSequence1_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 14, 1, 21),
    _TerminalSessionSequence1_Type()
)
terminalSessionSequence1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminalSessionSequence1.setStatus("mandatory")
_TerminalSessionSequence2_Type = DisplayString
_TerminalSessionSequence2_Object = MibTableColumn
terminalSessionSequence2 = _TerminalSessionSequence2_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 14, 1, 22),
    _TerminalSessionSequence2_Type()
)
terminalSessionSequence2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminalSessionSequence2.setStatus("mandatory")
_TerminalSessionSequence3_Type = DisplayString
_TerminalSessionSequence3_Object = MibTableColumn
terminalSessionSequence3 = _TerminalSessionSequence3_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 14, 1, 23),
    _TerminalSessionSequence3_Type()
)
terminalSessionSequence3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminalSessionSequence3.setStatus("mandatory")
_TerminalSessionSequence4_Type = DisplayString
_TerminalSessionSequence4_Object = MibTableColumn
terminalSessionSequence4 = _TerminalSessionSequence4_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 14, 1, 24),
    _TerminalSessionSequence4_Type()
)
terminalSessionSequence4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminalSessionSequence4.setStatus("mandatory")
_TerminalSessionSequence5_Type = DisplayString
_TerminalSessionSequence5_Object = MibTableColumn
terminalSessionSequence5 = _TerminalSessionSequence5_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 14, 1, 25),
    _TerminalSessionSequence5_Type()
)
terminalSessionSequence5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminalSessionSequence5.setStatus("mandatory")
_TerminalSessionSequence6_Type = DisplayString
_TerminalSessionSequence6_Object = MibTableColumn
terminalSessionSequence6 = _TerminalSessionSequence6_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 14, 1, 26),
    _TerminalSessionSequence6_Type()
)
terminalSessionSequence6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminalSessionSequence6.setStatus("mandatory")
_TerminalSessionSequence7_Type = DisplayString
_TerminalSessionSequence7_Object = MibTableColumn
terminalSessionSequence7 = _TerminalSessionSequence7_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 14, 1, 27),
    _TerminalSessionSequence7_Type()
)
terminalSessionSequence7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminalSessionSequence7.setStatus("mandatory")
_TerminalSessionSequence8_Type = DisplayString
_TerminalSessionSequence8_Object = MibTableColumn
terminalSessionSequence8 = _TerminalSessionSequence8_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 14, 1, 28),
    _TerminalSessionSequence8_Type()
)
terminalSessionSequence8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminalSessionSequence8.setStatus("mandatory")
_TerminalSessionSequence9_Type = DisplayString
_TerminalSessionSequence9_Object = MibTableColumn
terminalSessionSequence9 = _TerminalSessionSequence9_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 14, 1, 29),
    _TerminalSessionSequence9_Type()
)
terminalSessionSequence9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminalSessionSequence9.setStatus("mandatory")
_NetLogins_ObjectIdentity = ObjectIdentity
netLogins = _NetLogins_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 15)
)
_NetLoginPrompt_Type = DisplayString
_NetLoginPrompt_Object = MibScalar
netLoginPrompt = _NetLoginPrompt_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 15, 12),
    _NetLoginPrompt_Type()
)
netLoginPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netLoginPrompt.setStatus("mandatory")
_NetLoginsPasswordPrompt_Type = DisplayString
_NetLoginsPasswordPrompt_Object = MibScalar
netLoginsPasswordPrompt = _NetLoginsPasswordPrompt_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 15, 14),
    _NetLoginsPasswordPrompt_Type()
)
netLoginsPasswordPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netLoginsPasswordPrompt.setStatus("mandatory")
_NetLoginsCommandPrompt_Type = DisplayString
_NetLoginsCommandPrompt_Object = MibScalar
netLoginsCommandPrompt = _NetLoginsCommandPrompt_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 15, 17),
    _NetLoginsCommandPrompt_Type()
)
netLoginsCommandPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netLoginsCommandPrompt.setStatus("mandatory")
_NetLoginsRootPrompt_Type = DisplayString
_NetLoginsRootPrompt_Object = MibScalar
netLoginsRootPrompt = _NetLoginsRootPrompt_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 27, 15, 19),
    _NetLoginsRootPrompt_Type()
)
netLoginsRootPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netLoginsRootPrompt.setStatus("mandatory")
_Authentication_ObjectIdentity = ObjectIdentity
authentication = _Authentication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 28)
)
_Radius_ObjectIdentity = ObjectIdentity
radius = _Radius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 28, 11)
)
_RadiusRun_Type = Switch
_RadiusRun_Object = MibScalar
radiusRun = _RadiusRun_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 28, 11, 11),
    _RadiusRun_Type()
)
radiusRun.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusRun.setStatus("mandatory")
_RadiusIgnoreBad_Type = Switch
_RadiusIgnoreBad_Object = MibScalar
radiusIgnoreBad = _RadiusIgnoreBad_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 28, 11, 12),
    _RadiusIgnoreBad_Type()
)
radiusIgnoreBad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusIgnoreBad.setStatus("mandatory")
_RadiusPrimaryIPAddress_Type = IpAddress
_RadiusPrimaryIPAddress_Object = MibScalar
radiusPrimaryIPAddress = _RadiusPrimaryIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 28, 11, 13),
    _RadiusPrimaryIPAddress_Type()
)
radiusPrimaryIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusPrimaryIPAddress.setStatus("mandatory")
_RadiusSecondaryIPAddress_Type = IpAddress
_RadiusSecondaryIPAddress_Object = MibScalar
radiusSecondaryIPAddress = _RadiusSecondaryIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 28, 11, 14),
    _RadiusSecondaryIPAddress_Type()
)
radiusSecondaryIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusSecondaryIPAddress.setStatus("mandatory")
_RadiusPrimarySecret_Type = DisplayString
_RadiusPrimarySecret_Object = MibScalar
radiusPrimarySecret = _RadiusPrimarySecret_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 28, 11, 15),
    _RadiusPrimarySecret_Type()
)
radiusPrimarySecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusPrimarySecret.setStatus("mandatory")
_RadiusSecondarySecret_Type = DisplayString
_RadiusSecondarySecret_Object = MibScalar
radiusSecondarySecret = _RadiusSecondarySecret_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 28, 11, 16),
    _RadiusSecondarySecret_Type()
)
radiusSecondarySecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusSecondarySecret.setStatus("mandatory")
_RadiusPrimaryAuthSocket_Type = Integer32
_RadiusPrimaryAuthSocket_Object = MibScalar
radiusPrimaryAuthSocket = _RadiusPrimaryAuthSocket_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 28, 11, 17),
    _RadiusPrimaryAuthSocket_Type()
)
radiusPrimaryAuthSocket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusPrimaryAuthSocket.setStatus("mandatory")
_RadiusSecondaryAuthSocket_Type = Integer32
_RadiusSecondaryAuthSocket_Object = MibScalar
radiusSecondaryAuthSocket = _RadiusSecondaryAuthSocket_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 28, 11, 18),
    _RadiusSecondaryAuthSocket_Type()
)
radiusSecondaryAuthSocket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusSecondaryAuthSocket.setStatus("mandatory")
_RadiusPrimaryAccountingSocket_Type = Integer32
_RadiusPrimaryAccountingSocket_Object = MibScalar
radiusPrimaryAccountingSocket = _RadiusPrimaryAccountingSocket_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 28, 11, 19),
    _RadiusPrimaryAccountingSocket_Type()
)
radiusPrimaryAccountingSocket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusPrimaryAccountingSocket.setStatus("mandatory")
_RadiusSecondaryAccountingSocket_Type = Integer32
_RadiusSecondaryAccountingSocket_Object = MibScalar
radiusSecondaryAccountingSocket = _RadiusSecondaryAccountingSocket_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 28, 11, 20),
    _RadiusSecondaryAccountingSocket_Type()
)
radiusSecondaryAccountingSocket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusSecondaryAccountingSocket.setStatus("mandatory")
_User_ObjectIdentity = ObjectIdentity
user = _User_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 29)
)
_UserTable_Object = MibTable
userTable = _UserTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 29, 11)
)
if mibBuilder.loadTexts:
    userTable.setStatus("mandatory")
_UserEntry_Object = MibTableRow
userEntry = _UserEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 29, 11, 1)
)
userEntry.setIndexNames(
    (0, "DIGI-PORTSERVER-TS-MIB", "userIndex"),
)
if mibBuilder.loadTexts:
    userEntry.setStatus("mandatory")


class _UserIndex_Type(Integer32):
    """Custom type userIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_UserIndex_Type.__name__ = "Integer32"
_UserIndex_Object = MibTableColumn
userIndex = _UserIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 29, 11, 1, 11),
    _UserIndex_Type()
)
userIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userIndex.setStatus("mandatory")
_UserName_Type = DisplayString
_UserName_Object = MibTableColumn
userName = _UserName_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 29, 11, 1, 12),
    _UserName_Type()
)
userName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userName.setStatus("mandatory")
_UserPassword_Type = DisplayString
_UserPassword_Object = MibTableColumn
userPassword = _UserPassword_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 29, 11, 1, 13),
    _UserPassword_Type()
)
userPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userPassword.setStatus("mandatory")
_UserPasswordRequired_Type = Switch
_UserPasswordRequired_Object = MibTableColumn
userPasswordRequired = _UserPasswordRequired_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 29, 11, 1, 14),
    _UserPasswordRequired_Type()
)
userPasswordRequired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userPasswordRequired.setStatus("mandatory")


class _UserDefaultAccess_Type(Integer32):
    """Custom type userDefaultAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("commandLine", 1),
          ("autoconnect", 2),
          ("netService", 3),
          ("menu", 4),
          ("outgoing", 5))
    )


_UserDefaultAccess_Type.__name__ = "Integer32"
_UserDefaultAccess_Object = MibTableColumn
userDefaultAccess = _UserDefaultAccess_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 29, 11, 1, 15),
    _UserDefaultAccess_Type()
)
userDefaultAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userDefaultAccess.setStatus("mandatory")
_UserCommandLine_Type = Switch
_UserCommandLine_Object = MibTableColumn
userCommandLine = _UserCommandLine_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 29, 11, 1, 16),
    _UserCommandLine_Type()
)
userCommandLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userCommandLine.setStatus("mandatory")
_UserMenu_Type = Integer32
_UserMenu_Object = MibTableColumn
userMenu = _UserMenu_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 29, 11, 1, 17),
    _UserMenu_Type()
)
userMenu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userMenu.setStatus("mandatory")
_UserAccessTime_Type = DisplayString
_UserAccessTime_Object = MibTableColumn
userAccessTime = _UserAccessTime_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 29, 11, 1, 18),
    _UserAccessTime_Type()
)
userAccessTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userAccessTime.setStatus("mandatory")
_UserAutoConnect_Type = Switch
_UserAutoConnect_Object = MibTableColumn
userAutoConnect = _UserAutoConnect_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 29, 11, 1, 19),
    _UserAutoConnect_Type()
)
userAutoConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userAutoConnect.setStatus("mandatory")
_UserAutoHostIP_Type = IpAddress
_UserAutoHostIP_Object = MibTableColumn
userAutoHostIP = _UserAutoHostIP_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 29, 11, 1, 20),
    _UserAutoHostIP_Type()
)
userAutoHostIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userAutoHostIP.setStatus("deprecated")


class _UserAutoService_Type(Integer32):
    """Custom type userAutoService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("raw", 2),
          ("rlogin", 3),
          ("telnet", 4))
    )


_UserAutoService_Type.__name__ = "Integer32"
_UserAutoService_Object = MibTableColumn
userAutoService = _UserAutoService_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 29, 11, 1, 21),
    _UserAutoService_Type()
)
userAutoService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userAutoService.setStatus("mandatory")
_UserAutoPort_Type = Integer32
_UserAutoPort_Object = MibTableColumn
userAutoPort = _UserAutoPort_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 29, 11, 1, 22),
    _UserAutoPort_Type()
)
userAutoPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userAutoPort.setStatus("mandatory")
_UserSessionTimeout_Type = Integer32
_UserSessionTimeout_Object = MibTableColumn
userSessionTimeout = _UserSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 29, 11, 1, 23),
    _UserSessionTimeout_Type()
)
userSessionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userSessionTimeout.setStatus("mandatory")
_UserIdleTimeout_Type = Integer32
_UserIdleTimeout_Object = MibTableColumn
userIdleTimeout = _UserIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 29, 11, 1, 24),
    _UserIdleTimeout_Type()
)
userIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userIdleTimeout.setStatus("mandatory")
_UserMaxPort_Type = Integer32
_UserMaxPort_Object = MibTableColumn
userMaxPort = _UserMaxPort_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 29, 11, 1, 25),
    _UserMaxPort_Type()
)
userMaxPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userMaxPort.setStatus("mandatory")
_UserPorts_Type = DisplayString
_UserPorts_Object = MibTableColumn
userPorts = _UserPorts_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 29, 11, 1, 26),
    _UserPorts_Type()
)
userPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userPorts.setStatus("mandatory")
_UserConnectEscape_Type = DisplayString
_UserConnectEscape_Object = MibTableColumn
userConnectEscape = _UserConnectEscape_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 29, 11, 1, 27),
    _UserConnectEscape_Type()
)
userConnectEscape.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userConnectEscape.setStatus("mandatory")
_UserTelnetEscape_Type = DisplayString
_UserTelnetEscape_Object = MibTableColumn
userTelnetEscape = _UserTelnetEscape_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 29, 11, 1, 28),
    _UserTelnetEscape_Type()
)
userTelnetEscape.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userTelnetEscape.setStatus("mandatory")
_UserRloginEscape_Type = DisplayString
_UserRloginEscape_Object = MibTableColumn
userRloginEscape = _UserRloginEscape_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 29, 11, 1, 29),
    _UserRloginEscape_Type()
)
userRloginEscape.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userRloginEscape.setStatus("mandatory")
_UserKillEscape_Type = DisplayString
_UserKillEscape_Object = MibTableColumn
userKillEscape = _UserKillEscape_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 29, 11, 1, 30),
    _UserKillEscape_Type()
)
userKillEscape.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userKillEscape.setStatus("mandatory")
_UserOutgoing_Type = Switch
_UserOutgoing_Object = MibTableColumn
userOutgoing = _UserOutgoing_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 29, 11, 1, 31),
    _UserOutgoing_Type()
)
userOutgoing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userOutgoing.setStatus("mandatory")
_UserRemoteIP_Type = IpAddress
_UserRemoteIP_Object = MibTableColumn
userRemoteIP = _UserRemoteIP_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 29, 11, 1, 32),
    _UserRemoteIP_Type()
)
userRemoteIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userRemoteIP.setStatus("mandatory")
_UserIpMask_Type = IpAddress
_UserIpMask_Object = MibTableColumn
userIpMask = _UserIpMask_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 29, 11, 1, 33),
    _UserIpMask_Type()
)
userIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userIpMask.setStatus("mandatory")
_UserLocalIP_Type = IpAddress
_UserLocalIP_Object = MibTableColumn
userLocalIP = _UserLocalIP_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 29, 11, 1, 34),
    _UserLocalIP_Type()
)
userLocalIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userLocalIP.setStatus("mandatory")


class _UserPPPAuth_Type(Integer32):
    """Custom type userPPPAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("chap", 2),
          ("pap", 3),
          ("both", 4))
    )


_UserPPPAuth_Type.__name__ = "Integer32"
_UserPPPAuth_Object = MibTableColumn
userPPPAuth = _UserPPPAuth_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 29, 11, 1, 35),
    _UserPPPAuth_Type()
)
userPPPAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userPPPAuth.setStatus("mandatory")
_UserChapId_Type = DisplayString
_UserChapId_Object = MibTableColumn
userChapId = _UserChapId_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 29, 11, 1, 36),
    _UserChapId_Type()
)
userChapId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userChapId.setStatus("mandatory")
_UserChapKey_Type = DisplayString
_UserChapKey_Object = MibTableColumn
userChapKey = _UserChapKey_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 29, 11, 1, 37),
    _UserChapKey_Type()
)
userChapKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userChapKey.setStatus("mandatory")
_UserPapId_Type = DisplayString
_UserPapId_Object = MibTableColumn
userPapId = _UserPapId_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 29, 11, 1, 38),
    _UserPapId_Type()
)
userPapId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userPapId.setStatus("mandatory")
_UserPapKey_Type = DisplayString
_UserPapKey_Object = MibTableColumn
userPapKey = _UserPapKey_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 29, 11, 1, 39),
    _UserPapKey_Type()
)
userPapKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userPapKey.setStatus("mandatory")


class _UserCompression_Type(Integer32):
    """Custom type userCompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("vj", 2))
    )


_UserCompression_Type.__name__ = "Integer32"
_UserCompression_Object = MibTableColumn
userCompression = _UserCompression_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 29, 11, 1, 40),
    _UserCompression_Type()
)
userCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userCompression.setStatus("mandatory")
_UserAddrCompress_Type = Switch
_UserAddrCompress_Object = MibTableColumn
userAddrCompress = _UserAddrCompress_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 29, 11, 1, 41),
    _UserAddrCompress_Type()
)
userAddrCompress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userAddrCompress.setStatus("mandatory")
_UserVJSlots_Type = Integer32
_UserVJSlots_Object = MibTableColumn
userVJSlots = _UserVJSlots_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 29, 11, 1, 42),
    _UserVJSlots_Type()
)
userVJSlots.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userVJSlots.setStatus("mandatory")
_UserProtoCompress_Type = Switch
_UserProtoCompress_Object = MibTableColumn
userProtoCompress = _UserProtoCompress_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 29, 11, 1, 43),
    _UserProtoCompress_Type()
)
userProtoCompress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userProtoCompress.setStatus("mandatory")
_UserDeviceIndex_Type = Integer32
_UserDeviceIndex_Object = MibTableColumn
userDeviceIndex = _UserDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 29, 11, 1, 44),
    _UserDeviceIndex_Type()
)
userDeviceIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userDeviceIndex.setStatus("mandatory")
_UserLoginScriptIndex_Type = Integer32
_UserLoginScriptIndex_Object = MibTableColumn
userLoginScriptIndex = _UserLoginScriptIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 29, 11, 1, 45),
    _UserLoginScriptIndex_Type()
)
userLoginScriptIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userLoginScriptIndex.setStatus("mandatory")
_UserPhoneNumber_Type = DisplayString
_UserPhoneNumber_Object = MibTableColumn
userPhoneNumber = _UserPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 29, 11, 1, 46),
    _UserPhoneNumber_Type()
)
userPhoneNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userPhoneNumber.setStatus("mandatory")
_UserDialout_Type = Switch
_UserDialout_Object = MibTableColumn
userDialout = _UserDialout_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 29, 11, 1, 47),
    _UserDialout_Type()
)
userDialout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userDialout.setStatus("mandatory")
_UserWanStatus_Type = DisplayString
_UserWanStatus_Object = MibTableColumn
userWanStatus = _UserWanStatus_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 29, 11, 1, 48),
    _UserWanStatus_Type()
)
userWanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userWanStatus.setStatus("mandatory")
_UserFirstParam_Type = DisplayString
_UserFirstParam_Object = MibTableColumn
userFirstParam = _UserFirstParam_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 29, 11, 1, 49),
    _UserFirstParam_Type()
)
userFirstParam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userFirstParam.setStatus("mandatory")
_UserSecondParam_Type = DisplayString
_UserSecondParam_Object = MibTableColumn
userSecondParam = _UserSecondParam_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 29, 11, 1, 50),
    _UserSecondParam_Type()
)
userSecondParam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userSecondParam.setStatus("mandatory")
_UserKeepalive_Type = Switch
_UserKeepalive_Object = MibTableColumn
userKeepalive = _UserKeepalive_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 29, 11, 1, 51),
    _UserKeepalive_Type()
)
userKeepalive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userKeepalive.setStatus("mandatory")


class _UserFlushStChar_Type(Integer32):
    """Custom type userFlushStChar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("on", 2),
          ("off", 3))
    )


_UserFlushStChar_Type.__name__ = "Integer32"
_UserFlushStChar_Object = MibTableColumn
userFlushStChar = _UserFlushStChar_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 29, 11, 1, 52),
    _UserFlushStChar_Type()
)
userFlushStChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userFlushStChar.setStatus("mandatory")
_UserAutoHost_Type = DisplayString
_UserAutoHost_Object = MibTableColumn
userAutoHost = _UserAutoHost_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 29, 11, 1, 53),
    _UserAutoHost_Type()
)
userAutoHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userAutoHost.setStatus("mandatory")
_UserSSLClientEscape_Type = DisplayString
_UserSSLClientEscape_Object = MibTableColumn
userSSLClientEscape = _UserSSLClientEscape_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 29, 11, 1, 54),
    _UserSSLClientEscape_Type()
)
userSSLClientEscape.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userSSLClientEscape.setStatus("mandatory")
_WhoTable_Object = MibTable
whoTable = _WhoTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 30)
)
if mibBuilder.loadTexts:
    whoTable.setStatus("mandatory")
_WhoEntry_Object = MibTableRow
whoEntry = _WhoEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 30, 1)
)
whoEntry.setIndexNames(
    (0, "DIGI-PORTSERVER-TS-MIB", "whoIndex"),
)
if mibBuilder.loadTexts:
    whoEntry.setStatus("mandatory")
_WhoIndex_Type = Integer32
_WhoIndex_Object = MibTableColumn
whoIndex = _WhoIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 30, 1, 11),
    _WhoIndex_Type()
)
whoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whoIndex.setStatus("mandatory")
_WhoUser_Type = DisplayString
_WhoUser_Object = MibTableColumn
whoUser = _WhoUser_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 30, 1, 12),
    _WhoUser_Type()
)
whoUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whoUser.setStatus("mandatory")
_WhoTTY_Type = DisplayString
_WhoTTY_Object = MibTableColumn
whoTTY = _WhoTTY_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 30, 1, 13),
    _WhoTTY_Type()
)
whoTTY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whoTTY.setStatus("mandatory")
_WhoFrom_Type = DisplayString
_WhoFrom_Object = MibTableColumn
whoFrom = _WhoFrom_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 30, 1, 14),
    _WhoFrom_Type()
)
whoFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whoFrom.setStatus("mandatory")
_WhoTo_Type = DisplayString
_WhoTo_Object = MibTableColumn
whoTo = _WhoTo_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 30, 1, 15),
    _WhoTo_Type()
)
whoTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whoTo.setStatus("mandatory")
_WhoSessions_Type = Integer32
_WhoSessions_Object = MibTableColumn
whoSessions = _WhoSessions_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 30, 1, 16),
    _WhoSessions_Type()
)
whoSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whoSessions.setStatus("mandatory")
_DeviceTable_Object = MibTable
deviceTable = _DeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 31)
)
if mibBuilder.loadTexts:
    deviceTable.setStatus("mandatory")
_DeviceEntry_Object = MibTableRow
deviceEntry = _DeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 31, 1)
)
deviceEntry.setIndexNames(
    (0, "DIGI-PORTSERVER-TS-MIB", "deviceIndex"),
)
if mibBuilder.loadTexts:
    deviceEntry.setStatus("mandatory")
_DeviceIndex_Type = Integer32
_DeviceIndex_Object = MibTableColumn
deviceIndex = _DeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 31, 1, 11),
    _DeviceIndex_Type()
)
deviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceIndex.setStatus("mandatory")
_DeviceName_Type = DisplayString
_DeviceName_Object = MibTableColumn
deviceName = _DeviceName_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 31, 1, 12),
    _DeviceName_Type()
)
deviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceName.setStatus("mandatory")
_DeviceBaud_Type = Integer32
_DeviceBaud_Object = MibTableColumn
deviceBaud = _DeviceBaud_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 31, 1, 13),
    _DeviceBaud_Type()
)
deviceBaud.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceBaud.setStatus("mandatory")
_DevicePorts_Type = DisplayString
_DevicePorts_Object = MibTableColumn
devicePorts = _DevicePorts_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 31, 1, 14),
    _DevicePorts_Type()
)
devicePorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devicePorts.setStatus("mandatory")
_DeviceDialer_Type = Integer32
_DeviceDialer_Object = MibTableColumn
deviceDialer = _DeviceDialer_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 31, 1, 15),
    _DeviceDialer_Type()
)
deviceDialer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceDialer.setStatus("mandatory")
_ScriptTable_Object = MibTable
scriptTable = _ScriptTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 32)
)
if mibBuilder.loadTexts:
    scriptTable.setStatus("mandatory")
_ScriptEntry_Object = MibTableRow
scriptEntry = _ScriptEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 32, 1)
)
scriptEntry.setIndexNames(
    (0, "DIGI-PORTSERVER-TS-MIB", "scriptIndex"),
)
if mibBuilder.loadTexts:
    scriptEntry.setStatus("mandatory")
_ScriptIndex_Type = Integer32
_ScriptIndex_Object = MibTableColumn
scriptIndex = _ScriptIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 32, 1, 11),
    _ScriptIndex_Type()
)
scriptIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scriptIndex.setStatus("mandatory")
_ScriptName_Type = DisplayString
_ScriptName_Object = MibTableColumn
scriptName = _ScriptName_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 32, 1, 12),
    _ScriptName_Type()
)
scriptName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scriptName.setStatus("mandatory")
_SerialPowerOutTable_Object = MibTable
serialPowerOutTable = _SerialPowerOutTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 33)
)
if mibBuilder.loadTexts:
    serialPowerOutTable.setStatus("mandatory")
_SerialPowerOutEntry_Object = MibTableRow
serialPowerOutEntry = _SerialPowerOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 33, 1)
)
serialPowerOutEntry.setIndexNames(
    (0, "DIGI-PORTSERVER-TS-MIB", "serialPowerOutIndex"),
)
if mibBuilder.loadTexts:
    serialPowerOutEntry.setStatus("mandatory")
_SerialPowerOutIndex_Type = Integer32
_SerialPowerOutIndex_Object = MibTableColumn
serialPowerOutIndex = _SerialPowerOutIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 33, 1, 11),
    _SerialPowerOutIndex_Type()
)
serialPowerOutIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialPowerOutIndex.setStatus("mandatory")


class _SerialPowerOutRI_Type(Integer32):
    """Custom type serialPowerOutRI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("unavailable", 3))
    )


_SerialPowerOutRI_Type.__name__ = "Integer32"
_SerialPowerOutRI_Object = MibTableColumn
serialPowerOutRI = _SerialPowerOutRI_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 33, 1, 12),
    _SerialPowerOutRI_Type()
)
serialPowerOutRI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialPowerOutRI.setStatus("mandatory")


class _SerialPowerOutDTR_Type(Integer32):
    """Custom type serialPowerOutDTR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("unavailable", 3))
    )


_SerialPowerOutDTR_Type.__name__ = "Integer32"
_SerialPowerOutDTR_Object = MibTableColumn
serialPowerOutDTR = _SerialPowerOutDTR_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3, 33, 1, 13),
    _SerialPowerOutDTR_Type()
)
serialPowerOutDTR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialPowerOutDTR.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DIGI-PORTSERVER-TS-MIB",
    **{"DisplayString": DisplayString,
       "PhysAddress": PhysAddress,
       "Switch": Switch,
       "Action": Action,
       "general": general,
       "generalModel": generalModel,
       "generalType": generalType,
       "generalFirmwareVersion": generalFirmwareVersion,
       "generalIPAddress": generalIPAddress,
       "generalGateway": generalGateway,
       "generalNameServer": generalNameServer,
       "generalSubMask": generalSubMask,
       "generalEtherAddress": generalEtherAddress,
       "generalPortServerName": generalPortServerName,
       "generalDomain": generalDomain,
       "generalRealPortNumber": generalRealPortNumber,
       "generalBaseSocket": generalBaseSocket,
       "generalTBreak": generalTBreak,
       "generalClearStatistics": generalClearStatistics,
       "generalOptimize": generalOptimize,
       "generalDhcpClientIdentifier": generalDhcpClientIdentifier,
       "generalDhcpClientIdentifierType": generalDhcpClientIdentifierType,
       "generalEthernetSpeed": generalEthernetSpeed,
       "generalEthernetDuplex": generalEthernetDuplex,
       "generalDhcpIgnoreKeepalive": generalDhcpIgnoreKeepalive,
       "generalSecureRealPortNumber": generalSecureRealPortNumber,
       "generalDhcpClientFqdnOption": generalDhcpClientFqdnOption,
       "processor": processor,
       "processorCurrentUtilization": processorCurrentUtilization,
       "memory": memory,
       "memoryTotalMemory": memoryTotalMemory,
       "memoryAvailable": memoryAvailable,
       "memoryLargestBlockAvailable": memoryLargestBlockAvailable,
       "memorySuccessfulAllocates": memorySuccessfulAllocates,
       "memoryFailedAllocates": memoryFailedAllocates,
       "time": time,
       "timeSystemCurrent": timeSystemCurrent,
       "boot": boot,
       "bootReboot": bootReboot,
       "bootDHCPBoot": bootDHCPBoot,
       "port": port,
       "authTable": authTable,
       "authEntry": authEntry,
       "authIndex": authIndex,
       "authIp": authIp,
       "authMask": authMask,
       "authRealPort": authRealPort,
       "authLogin": authLogin,
       "authUnrestricted": authUnrestricted,
       "lineTable": lineTable,
       "lineEntry": lineEntry,
       "lineIndex": lineIndex,
       "lineResetSettings": lineResetSettings,
       "lineBreak": lineBreak,
       "lineError": lineError,
       "lineInPCK": lineInPCK,
       "lineIStrip": lineIStrip,
       "lineOnLCR": lineOnLCR,
       "lineOTab": lineOTab,
       "portsTable": portsTable,
       "portsEntry": portsEntry,
       "portsIndex": portsIndex,
       "portsResetSettings": portsResetSettings,
       "portsAutoConnect": portsAutoConnect,
       "portsBinaryMode": portsBinaryMode,
       "portsDevice": portsDevice,
       "portsDPort": portsDPort,
       "portsEDelay": portsEDelay,
       "portsGroup": portsGroup,
       "portsSession": portsSession,
       "portsTermType": portsTermType,
       "portsUID": portsUID,
       "portsDestIP": portsDestIP,
       "portsAltIP": portsAltIP,
       "portsKeepalive": portsKeepalive,
       "portsFlushStChar": portsFlushStChar,
       "portsAutoService": portsAutoService,
       "portsResetSerialSettings": portsResetSerialSettings,
       "portsAutoDest": portsAutoDest,
       "portsName": portsName,
       "flowTable": flowTable,
       "flowEntry": flowEntry,
       "flowIndex": flowIndex,
       "flowResetSettings": flowResetSettings,
       "flowAltPin": flowAltPin,
       "flowForceDCD": flowForceDCD,
       "flowRts": flowRts,
       "flowRtsPreDelay": flowRtsPreDelay,
       "flowRtsPostDelay": flowRtsPostDelay,
       "network": network,
       "tcpOther": tcpOther,
       "tcpOtherRetransTimeout": tcpOtherRetransTimeout,
       "tcpOtherKeepAliveActive": tcpOtherKeepAliveActive,
       "tcpOtherKeepAliveIdle": tcpOtherKeepAliveIdle,
       "tcpOtherKeepAliveGarbage": tcpOtherKeepAliveGarbage,
       "tcpOtherProbeCounter": tcpOtherProbeCounter,
       "tcpOtherProbeInterval": tcpOtherProbeInterval,
       "forwarding": forwarding,
       "forwardingAdvertise": forwardingAdvertise,
       "forwardingICMPDiscovery": forwardingICMPDiscovery,
       "forwardingICMPSendRedirects": forwardingICMPSendRedirects,
       "forwardingICMPMaskServer": forwardingICMPMaskServer,
       "forwardingIGMP": forwardingIGMP,
       "forwardingPoisonReverse": forwardingPoisonReverse,
       "forwardingProxyArp": forwardingProxyArp,
       "forwardingState": forwardingState,
       "forwardingSplitHorizon": forwardingSplitHorizon,
       "forwardingTimeout": forwardingTimeout,
       "hostnameTable": hostnameTable,
       "hostnameEntry": hostnameEntry,
       "hostIndex": hostIndex,
       "hostIP": hostIP,
       "hostName": hostName,
       "trace": trace,
       "traceState": traceState,
       "traceMode": traceMode,
       "traceSysLogState": traceSysLogState,
       "traceLogHost": traceLogHost,
       "traceTable": traceTable,
       "traceEntry": traceEntry,
       "traceIndex": traceIndex,
       "traceType": traceType,
       "traceSeverity": traceSeverity,
       "altIpTable": altIpTable,
       "altIpEntry": altIpEntry,
       "altIpIndex": altIpIndex,
       "altIpIp": altIpIp,
       "altIpGroup": altIpGroup,
       "snmpOther": snmpOther,
       "snmpTrapDest": snmpTrapDest,
       "snmpLoginTraps": snmpLoginTraps,
       "snmpLinkUpTraps": snmpLinkUpTraps,
       "snmpColdStartTraps": snmpColdStartTraps,
       "interface": interface,
       "keyMapTable": keyMapTable,
       "keyMapEntry": keyMapEntry,
       "keyMapIndex": keyMapIndex,
       "keyMapEOF": keyMapEOF,
       "keyMapErase": keyMapErase,
       "keyMapInterrupt": keyMapInterrupt,
       "keyMapKill": keyMapKill,
       "keyMapTelnetEscape": keyMapTelnetEscape,
       "keyMapXON": keyMapXON,
       "keyMapXOFF": keyMapXOFF,
       "keyMapXONAlternate": keyMapXONAlternate,
       "keyMapXOFFAlternate": keyMapXOFFAlternate,
       "loginsTable": loginsTable,
       "loginsEntry": loginsEntry,
       "loginsIndex": loginsIndex,
       "loginPrompt": loginPrompt,
       "loginsAllowed": loginsAllowed,
       "loginsPasswordPrompt": loginsPasswordPrompt,
       "loginsPasswordRequired": loginsPasswordRequired,
       "loginsVerboseLogins": loginsVerboseLogins,
       "loginsCommandPrompt": loginsCommandPrompt,
       "loginsWriteEnabled": loginsWriteEnabled,
       "loginsRootPrompt": loginsRootPrompt,
       "menuTable": menuTable,
       "menuEntry": menuEntry,
       "menuIndex": menuIndex,
       "menuName": menuName,
       "menuTitleLine1": menuTitleLine1,
       "menuTitleLine2": menuTitleLine2,
       "menuText1": menuText1,
       "menuText2": menuText2,
       "menuText3": menuText3,
       "menuText4": menuText4,
       "menuText5": menuText5,
       "menuText6": menuText6,
       "menuText7": menuText7,
       "menuText8": menuText8,
       "menuText9": menuText9,
       "menuText10": menuText10,
       "menuText11": menuText11,
       "menuText12": menuText12,
       "menuText13": menuText13,
       "menuText14": menuText14,
       "menuText15": menuText15,
       "menuText16": menuText16,
       "menuText17": menuText17,
       "menuText18": menuText18,
       "menuText19": menuText19,
       "menuText20": menuText20,
       "menuCommand1": menuCommand1,
       "menuCommand2": menuCommand2,
       "menuCommand3": menuCommand3,
       "menuCommand4": menuCommand4,
       "menuCommand5": menuCommand5,
       "menuCommand6": menuCommand6,
       "menuCommand7": menuCommand7,
       "menuCommand8": menuCommand8,
       "menuCommand9": menuCommand9,
       "menuCommand10": menuCommand10,
       "menuCommand11": menuCommand11,
       "menuCommand12": menuCommand12,
       "menuCommand13": menuCommand13,
       "menuCommand14": menuCommand14,
       "menuCommand15": menuCommand15,
       "menuCommand16": menuCommand16,
       "menuCommand17": menuCommand17,
       "menuCommand18": menuCommand18,
       "menuCommand19": menuCommand19,
       "menuCommand20": menuCommand20,
       "terminalTable": terminalTable,
       "terminalEntry": terminalEntry,
       "terminalIndex": terminalIndex,
       "terminalType": terminalType,
       "terminalNumberofPages": terminalNumberofPages,
       "terminalClearSequence": terminalClearSequence,
       "terminalSessionSequence1": terminalSessionSequence1,
       "terminalSessionSequence2": terminalSessionSequence2,
       "terminalSessionSequence3": terminalSessionSequence3,
       "terminalSessionSequence4": terminalSessionSequence4,
       "terminalSessionSequence5": terminalSessionSequence5,
       "terminalSessionSequence6": terminalSessionSequence6,
       "terminalSessionSequence7": terminalSessionSequence7,
       "terminalSessionSequence8": terminalSessionSequence8,
       "terminalSessionSequence9": terminalSessionSequence9,
       "netLogins": netLogins,
       "netLoginPrompt": netLoginPrompt,
       "netLoginsPasswordPrompt": netLoginsPasswordPrompt,
       "netLoginsCommandPrompt": netLoginsCommandPrompt,
       "netLoginsRootPrompt": netLoginsRootPrompt,
       "authentication": authentication,
       "radius": radius,
       "radiusRun": radiusRun,
       "radiusIgnoreBad": radiusIgnoreBad,
       "radiusPrimaryIPAddress": radiusPrimaryIPAddress,
       "radiusSecondaryIPAddress": radiusSecondaryIPAddress,
       "radiusPrimarySecret": radiusPrimarySecret,
       "radiusSecondarySecret": radiusSecondarySecret,
       "radiusPrimaryAuthSocket": radiusPrimaryAuthSocket,
       "radiusSecondaryAuthSocket": radiusSecondaryAuthSocket,
       "radiusPrimaryAccountingSocket": radiusPrimaryAccountingSocket,
       "radiusSecondaryAccountingSocket": radiusSecondaryAccountingSocket,
       "user": user,
       "userTable": userTable,
       "userEntry": userEntry,
       "userIndex": userIndex,
       "userName": userName,
       "userPassword": userPassword,
       "userPasswordRequired": userPasswordRequired,
       "userDefaultAccess": userDefaultAccess,
       "userCommandLine": userCommandLine,
       "userMenu": userMenu,
       "userAccessTime": userAccessTime,
       "userAutoConnect": userAutoConnect,
       "userAutoHostIP": userAutoHostIP,
       "userAutoService": userAutoService,
       "userAutoPort": userAutoPort,
       "userSessionTimeout": userSessionTimeout,
       "userIdleTimeout": userIdleTimeout,
       "userMaxPort": userMaxPort,
       "userPorts": userPorts,
       "userConnectEscape": userConnectEscape,
       "userTelnetEscape": userTelnetEscape,
       "userRloginEscape": userRloginEscape,
       "userKillEscape": userKillEscape,
       "userOutgoing": userOutgoing,
       "userRemoteIP": userRemoteIP,
       "userIpMask": userIpMask,
       "userLocalIP": userLocalIP,
       "userPPPAuth": userPPPAuth,
       "userChapId": userChapId,
       "userChapKey": userChapKey,
       "userPapId": userPapId,
       "userPapKey": userPapKey,
       "userCompression": userCompression,
       "userAddrCompress": userAddrCompress,
       "userVJSlots": userVJSlots,
       "userProtoCompress": userProtoCompress,
       "userDeviceIndex": userDeviceIndex,
       "userLoginScriptIndex": userLoginScriptIndex,
       "userPhoneNumber": userPhoneNumber,
       "userDialout": userDialout,
       "userWanStatus": userWanStatus,
       "userFirstParam": userFirstParam,
       "userSecondParam": userSecondParam,
       "userKeepalive": userKeepalive,
       "userFlushStChar": userFlushStChar,
       "userAutoHost": userAutoHost,
       "userSSLClientEscape": userSSLClientEscape,
       "whoTable": whoTable,
       "whoEntry": whoEntry,
       "whoIndex": whoIndex,
       "whoUser": whoUser,
       "whoTTY": whoTTY,
       "whoFrom": whoFrom,
       "whoTo": whoTo,
       "whoSessions": whoSessions,
       "deviceTable": deviceTable,
       "deviceEntry": deviceEntry,
       "deviceIndex": deviceIndex,
       "deviceName": deviceName,
       "deviceBaud": deviceBaud,
       "devicePorts": devicePorts,
       "deviceDialer": deviceDialer,
       "scriptTable": scriptTable,
       "scriptEntry": scriptEntry,
       "scriptIndex": scriptIndex,
       "scriptName": scriptName,
       "serialPowerOutTable": serialPowerOutTable,
       "serialPowerOutEntry": serialPowerOutEntry,
       "serialPowerOutIndex": serialPowerOutIndex,
       "serialPowerOutRI": serialPowerOutRI,
       "serialPowerOutDTR": serialPowerOutDTR}
)
