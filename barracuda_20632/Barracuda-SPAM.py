# SNMP MIB module (Barracuda-SPAM) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/barracuda_20632/Barracuda-SPAM.mib
# Produced by pysmi-1.5.11 at Fri May 30 16:37:18 2025
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

(barracuda,) = mibBuilder.importSymbols(
    "Barracuda-REF",
    "barracuda")

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

bspam = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20632, 2)
)


# Types definitions



class Boolean(Integer32):
    """Custom type Boolean based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Bspamtraps_ObjectIdentity = ObjectIdentity
bspamtraps = _Bspamtraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20632, 2, 1)
)
_InQueueSize_Type = Integer32
_InQueueSize_Object = MibScalar
inQueueSize = _InQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 20632, 2, 2),
    _InQueueSize_Type()
)
inQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inQueueSize.setStatus("current")
_OutQueueSize_Type = Integer32
_OutQueueSize_Object = MibScalar
outQueueSize = _OutQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 20632, 2, 3),
    _OutQueueSize_Type()
)
outQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outQueueSize.setStatus("current")
_DeferredQueueSize_Type = Integer32
_DeferredQueueSize_Object = MibScalar
deferredQueueSize = _DeferredQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 20632, 2, 4),
    _DeferredQueueSize_Type()
)
deferredQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deferredQueueSize.setStatus("current")
_AvgEmailLatency_Type = Integer32
_AvgEmailLatency_Object = MibScalar
avgEmailLatency = _AvgEmailLatency_Object(
    (1, 3, 6, 1, 4, 1, 20632, 2, 5),
    _AvgEmailLatency_Type()
)
avgEmailLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avgEmailLatency.setStatus("current")
_NotifyQueueSize_Type = Integer32
_NotifyQueueSize_Object = MibScalar
notifyQueueSize = _NotifyQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 20632, 2, 8),
    _NotifyQueueSize_Type()
)
notifyQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notifyQueueSize.setStatus("current")
_EncryptionEnabled_Type = Boolean
_EncryptionEnabled_Object = MibScalar
encryptionEnabled = _EncryptionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 20632, 2, 9),
    _EncryptionEnabled_Type()
)
encryptionEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encryptionEnabled.setStatus("current")
_HybridEnabled_Type = Boolean
_HybridEnabled_Object = MibScalar
hybridEnabled = _HybridEnabled_Object(
    (1, 3, 6, 1, 4, 1, 20632, 2, 10),
    _HybridEnabled_Type()
)
hybridEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hybridEnabled.setStatus("current")
_LastMessageDelivery_Type = Integer32
_LastMessageDelivery_Object = MibScalar
lastMessageDelivery = _LastMessageDelivery_Object(
    (1, 3, 6, 1, 4, 1, 20632, 2, 11),
    _LastMessageDelivery_Type()
)
lastMessageDelivery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastMessageDelivery.setStatus("current")
_UniqueRecipients_Type = Integer32
_UniqueRecipients_Object = MibScalar
uniqueRecipients = _UniqueRecipients_Object(
    (1, 3, 6, 1, 4, 1, 20632, 2, 12),
    _UniqueRecipients_Type()
)
uniqueRecipients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uniqueRecipients.setStatus("current")
_SystemLoad_Type = Integer32
_SystemLoad_Object = MibScalar
systemLoad = _SystemLoad_Object(
    (1, 3, 6, 1, 4, 1, 20632, 2, 13),
    _SystemLoad_Type()
)
systemLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemLoad.setStatus("current")
_SysFanSpeed_Type = Integer32
_SysFanSpeed_Object = MibScalar
sysFanSpeed = _SysFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 20632, 2, 14),
    _SysFanSpeed_Type()
)
sysFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFanSpeed.setStatus("current")
_CpuFanSpeed_Type = Integer32
_CpuFanSpeed_Object = MibScalar
cpuFanSpeed = _CpuFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 20632, 2, 15),
    _CpuFanSpeed_Type()
)
cpuFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuFanSpeed.setStatus("current")
_CpuTemperature_Type = OctetString
_CpuTemperature_Object = MibScalar
cpuTemperature = _CpuTemperature_Object(
    (1, 3, 6, 1, 4, 1, 20632, 2, 16),
    _CpuTemperature_Type()
)
cpuTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTemperature.setStatus("current")
_FirmwareStorage_Type = Integer32
_FirmwareStorage_Object = MibScalar
firmwareStorage = _FirmwareStorage_Object(
    (1, 3, 6, 1, 4, 1, 20632, 2, 17),
    _FirmwareStorage_Type()
)
firmwareStorage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareStorage.setStatus("current")
_MaillogStorage_Type = Integer32
_MaillogStorage_Object = MibScalar
maillogStorage = _MaillogStorage_Object(
    (1, 3, 6, 1, 4, 1, 20632, 2, 18),
    _MaillogStorage_Type()
)
maillogStorage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maillogStorage.setStatus("current")
_RaidStatus_Type = OctetString
_RaidStatus_Object = MibScalar
raidStatus = _RaidStatus_Object(
    (1, 3, 6, 1, 4, 1, 20632, 2, 19),
    _RaidStatus_Type()
)
raidStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidStatus.setStatus("current")
_TotalInboundBlocked_Type = Integer32
_TotalInboundBlocked_Object = MibScalar
totalInboundBlocked = _TotalInboundBlocked_Object(
    (1, 3, 6, 1, 4, 1, 20632, 2, 20),
    _TotalInboundBlocked_Type()
)
totalInboundBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalInboundBlocked.setStatus("current")
_DailyInboundBlocked_Type = Integer32
_DailyInboundBlocked_Object = MibScalar
dailyInboundBlocked = _DailyInboundBlocked_Object(
    (1, 3, 6, 1, 4, 1, 20632, 2, 21),
    _DailyInboundBlocked_Type()
)
dailyInboundBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dailyInboundBlocked.setStatus("current")
_HourlyInboundBlocked_Type = Integer32
_HourlyInboundBlocked_Object = MibScalar
hourlyInboundBlocked = _HourlyInboundBlocked_Object(
    (1, 3, 6, 1, 4, 1, 20632, 2, 22),
    _HourlyInboundBlocked_Type()
)
hourlyInboundBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hourlyInboundBlocked.setStatus("current")
_TotalInboundVirusBlocked_Type = Integer32
_TotalInboundVirusBlocked_Object = MibScalar
totalInboundVirusBlocked = _TotalInboundVirusBlocked_Object(
    (1, 3, 6, 1, 4, 1, 20632, 2, 23),
    _TotalInboundVirusBlocked_Type()
)
totalInboundVirusBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalInboundVirusBlocked.setStatus("current")
_DailyInboundVirusBlocked_Type = Integer32
_DailyInboundVirusBlocked_Object = MibScalar
dailyInboundVirusBlocked = _DailyInboundVirusBlocked_Object(
    (1, 3, 6, 1, 4, 1, 20632, 2, 24),
    _DailyInboundVirusBlocked_Type()
)
dailyInboundVirusBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dailyInboundVirusBlocked.setStatus("current")
_HourlyInboundVirusBlocked_Type = Integer32
_HourlyInboundVirusBlocked_Object = MibScalar
hourlyInboundVirusBlocked = _HourlyInboundVirusBlocked_Object(
    (1, 3, 6, 1, 4, 1, 20632, 2, 25),
    _HourlyInboundVirusBlocked_Type()
)
hourlyInboundVirusBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hourlyInboundVirusBlocked.setStatus("current")
_TotalInboundRateControlled_Type = Integer32
_TotalInboundRateControlled_Object = MibScalar
totalInboundRateControlled = _TotalInboundRateControlled_Object(
    (1, 3, 6, 1, 4, 1, 20632, 2, 26),
    _TotalInboundRateControlled_Type()
)
totalInboundRateControlled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalInboundRateControlled.setStatus("current")
_DailyInboundRateControlled_Type = Integer32
_DailyInboundRateControlled_Object = MibScalar
dailyInboundRateControlled = _DailyInboundRateControlled_Object(
    (1, 3, 6, 1, 4, 1, 20632, 2, 27),
    _DailyInboundRateControlled_Type()
)
dailyInboundRateControlled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dailyInboundRateControlled.setStatus("current")
_HourlyInboundRateControlled_Type = Integer32
_HourlyInboundRateControlled_Object = MibScalar
hourlyInboundRateControlled = _HourlyInboundRateControlled_Object(
    (1, 3, 6, 1, 4, 1, 20632, 2, 28),
    _HourlyInboundRateControlled_Type()
)
hourlyInboundRateControlled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hourlyInboundRateControlled.setStatus("current")
_TotalInboundQuarantined_Type = Integer32
_TotalInboundQuarantined_Object = MibScalar
totalInboundQuarantined = _TotalInboundQuarantined_Object(
    (1, 3, 6, 1, 4, 1, 20632, 2, 29),
    _TotalInboundQuarantined_Type()
)
totalInboundQuarantined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalInboundQuarantined.setStatus("current")
_DailyInboundQuarantined_Type = Integer32
_DailyInboundQuarantined_Object = MibScalar
dailyInboundQuarantined = _DailyInboundQuarantined_Object(
    (1, 3, 6, 1, 4, 1, 20632, 2, 30),
    _DailyInboundQuarantined_Type()
)
dailyInboundQuarantined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dailyInboundQuarantined.setStatus("current")
_HourlyInboundQuarantined_Type = Integer32
_HourlyInboundQuarantined_Object = MibScalar
hourlyInboundQuarantined = _HourlyInboundQuarantined_Object(
    (1, 3, 6, 1, 4, 1, 20632, 2, 31),
    _HourlyInboundQuarantined_Type()
)
hourlyInboundQuarantined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hourlyInboundQuarantined.setStatus("current")
_TotalInboundTagged_Type = Integer32
_TotalInboundTagged_Object = MibScalar
totalInboundTagged = _TotalInboundTagged_Object(
    (1, 3, 6, 1, 4, 1, 20632, 2, 32),
    _TotalInboundTagged_Type()
)
totalInboundTagged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalInboundTagged.setStatus("current")
_DailyInboundTagged_Type = Integer32
_DailyInboundTagged_Object = MibScalar
dailyInboundTagged = _DailyInboundTagged_Object(
    (1, 3, 6, 1, 4, 1, 20632, 2, 33),
    _DailyInboundTagged_Type()
)
dailyInboundTagged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dailyInboundTagged.setStatus("current")
_HourlyInboundTagged_Type = Integer32
_HourlyInboundTagged_Object = MibScalar
hourlyInboundTagged = _HourlyInboundTagged_Object(
    (1, 3, 6, 1, 4, 1, 20632, 2, 34),
    _HourlyInboundTagged_Type()
)
hourlyInboundTagged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hourlyInboundTagged.setStatus("current")
_TotalAllowed_Type = Integer32
_TotalAllowed_Object = MibScalar
totalAllowed = _TotalAllowed_Object(
    (1, 3, 6, 1, 4, 1, 20632, 2, 35),
    _TotalAllowed_Type()
)
totalAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalAllowed.setStatus("current")
_DailyAllowed_Type = Integer32
_DailyAllowed_Object = MibScalar
dailyAllowed = _DailyAllowed_Object(
    (1, 3, 6, 1, 4, 1, 20632, 2, 36),
    _DailyAllowed_Type()
)
dailyAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dailyAllowed.setStatus("current")
_HourlyAllowed_Type = Integer32
_HourlyAllowed_Object = MibScalar
hourlyAllowed = _HourlyAllowed_Object(
    (1, 3, 6, 1, 4, 1, 20632, 2, 37),
    _HourlyAllowed_Type()
)
hourlyAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hourlyAllowed.setStatus("current")
_TotalOutboundPolicyBlocked_Type = Integer32
_TotalOutboundPolicyBlocked_Object = MibScalar
totalOutboundPolicyBlocked = _TotalOutboundPolicyBlocked_Object(
    (1, 3, 6, 1, 4, 1, 20632, 2, 38),
    _TotalOutboundPolicyBlocked_Type()
)
totalOutboundPolicyBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalOutboundPolicyBlocked.setStatus("current")
_DailyOutboundPolicyBlocked_Type = Integer32
_DailyOutboundPolicyBlocked_Object = MibScalar
dailyOutboundPolicyBlocked = _DailyOutboundPolicyBlocked_Object(
    (1, 3, 6, 1, 4, 1, 20632, 2, 39),
    _DailyOutboundPolicyBlocked_Type()
)
dailyOutboundPolicyBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dailyOutboundPolicyBlocked.setStatus("current")
_HourlyOutboundPolicyBlocked_Type = Integer32
_HourlyOutboundPolicyBlocked_Object = MibScalar
hourlyOutboundPolicyBlocked = _HourlyOutboundPolicyBlocked_Object(
    (1, 3, 6, 1, 4, 1, 20632, 2, 40),
    _HourlyOutboundPolicyBlocked_Type()
)
hourlyOutboundPolicyBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hourlyOutboundPolicyBlocked.setStatus("current")
_TotalOutboundSpamBlocked_Type = Integer32
_TotalOutboundSpamBlocked_Object = MibScalar
totalOutboundSpamBlocked = _TotalOutboundSpamBlocked_Object(
    (1, 3, 6, 1, 4, 1, 20632, 2, 41),
    _TotalOutboundSpamBlocked_Type()
)
totalOutboundSpamBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalOutboundSpamBlocked.setStatus("current")
_DailyOutboundSpamBlocked_Type = Integer32
_DailyOutboundSpamBlocked_Object = MibScalar
dailyOutboundSpamBlocked = _DailyOutboundSpamBlocked_Object(
    (1, 3, 6, 1, 4, 1, 20632, 2, 42),
    _DailyOutboundSpamBlocked_Type()
)
dailyOutboundSpamBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dailyOutboundSpamBlocked.setStatus("current")
_HourlyOutboundSpamBlocked_Type = Integer32
_HourlyOutboundSpamBlocked_Object = MibScalar
hourlyOutboundSpamBlocked = _HourlyOutboundSpamBlocked_Object(
    (1, 3, 6, 1, 4, 1, 20632, 2, 43),
    _HourlyOutboundSpamBlocked_Type()
)
hourlyOutboundSpamBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hourlyOutboundSpamBlocked.setStatus("current")
_TotalOutboundVirusBlocked_Type = Integer32
_TotalOutboundVirusBlocked_Object = MibScalar
totalOutboundVirusBlocked = _TotalOutboundVirusBlocked_Object(
    (1, 3, 6, 1, 4, 1, 20632, 2, 44),
    _TotalOutboundVirusBlocked_Type()
)
totalOutboundVirusBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalOutboundVirusBlocked.setStatus("current")
_DailyOutboundVirusBlocked_Type = Integer32
_DailyOutboundVirusBlocked_Object = MibScalar
dailyOutboundVirusBlocked = _DailyOutboundVirusBlocked_Object(
    (1, 3, 6, 1, 4, 1, 20632, 2, 45),
    _DailyOutboundVirusBlocked_Type()
)
dailyOutboundVirusBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dailyOutboundVirusBlocked.setStatus("current")
_HourlyOutboundVirusBlocked_Type = Integer32
_HourlyOutboundVirusBlocked_Object = MibScalar
hourlyOutboundVirusBlocked = _HourlyOutboundVirusBlocked_Object(
    (1, 3, 6, 1, 4, 1, 20632, 2, 46),
    _HourlyOutboundVirusBlocked_Type()
)
hourlyOutboundVirusBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hourlyOutboundVirusBlocked.setStatus("current")
_TotalOutboundRateControlled_Type = Integer32
_TotalOutboundRateControlled_Object = MibScalar
totalOutboundRateControlled = _TotalOutboundRateControlled_Object(
    (1, 3, 6, 1, 4, 1, 20632, 2, 47),
    _TotalOutboundRateControlled_Type()
)
totalOutboundRateControlled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalOutboundRateControlled.setStatus("current")
_DailyOutboundRateControlled_Type = Integer32
_DailyOutboundRateControlled_Object = MibScalar
dailyOutboundRateControlled = _DailyOutboundRateControlled_Object(
    (1, 3, 6, 1, 4, 1, 20632, 2, 48),
    _DailyOutboundRateControlled_Type()
)
dailyOutboundRateControlled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dailyOutboundRateControlled.setStatus("current")
_HourlyOutboundRateControlled_Type = Integer32
_HourlyOutboundRateControlled_Object = MibScalar
hourlyOutboundRateControlled = _HourlyOutboundRateControlled_Object(
    (1, 3, 6, 1, 4, 1, 20632, 2, 49),
    _HourlyOutboundRateControlled_Type()
)
hourlyOutboundRateControlled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hourlyOutboundRateControlled.setStatus("current")
_TotalOutboundQuarantined_Type = Integer32
_TotalOutboundQuarantined_Object = MibScalar
totalOutboundQuarantined = _TotalOutboundQuarantined_Object(
    (1, 3, 6, 1, 4, 1, 20632, 2, 50),
    _TotalOutboundQuarantined_Type()
)
totalOutboundQuarantined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalOutboundQuarantined.setStatus("current")
_DailyOutboundQuarantined_Type = Integer32
_DailyOutboundQuarantined_Object = MibScalar
dailyOutboundQuarantined = _DailyOutboundQuarantined_Object(
    (1, 3, 6, 1, 4, 1, 20632, 2, 51),
    _DailyOutboundQuarantined_Type()
)
dailyOutboundQuarantined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dailyOutboundQuarantined.setStatus("current")
_HourlyOutboundQuarantined_Type = Integer32
_HourlyOutboundQuarantined_Object = MibScalar
hourlyOutboundQuarantined = _HourlyOutboundQuarantined_Object(
    (1, 3, 6, 1, 4, 1, 20632, 2, 52),
    _HourlyOutboundQuarantined_Type()
)
hourlyOutboundQuarantined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hourlyOutboundQuarantined.setStatus("current")
_TotalEncrypted_Type = Integer32
_TotalEncrypted_Object = MibScalar
totalEncrypted = _TotalEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 20632, 2, 53),
    _TotalEncrypted_Type()
)
totalEncrypted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalEncrypted.setStatus("current")
_DailyEncrypted_Type = Integer32
_DailyEncrypted_Object = MibScalar
dailyEncrypted = _DailyEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 20632, 2, 54),
    _DailyEncrypted_Type()
)
dailyEncrypted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dailyEncrypted.setStatus("current")
_HourlyEncrypted_Type = Integer32
_HourlyEncrypted_Object = MibScalar
hourlyEncrypted = _HourlyEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 20632, 2, 55),
    _HourlyEncrypted_Type()
)
hourlyEncrypted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hourlyEncrypted.setStatus("current")
_TotalRedirected_Type = Integer32
_TotalRedirected_Object = MibScalar
totalRedirected = _TotalRedirected_Object(
    (1, 3, 6, 1, 4, 1, 20632, 2, 56),
    _TotalRedirected_Type()
)
totalRedirected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalRedirected.setStatus("current")
_DailyRedirected_Type = Integer32
_DailyRedirected_Object = MibScalar
dailyRedirected = _DailyRedirected_Object(
    (1, 3, 6, 1, 4, 1, 20632, 2, 57),
    _DailyRedirected_Type()
)
dailyRedirected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dailyRedirected.setStatus("current")
_HourlyRedirected_Type = Integer32
_HourlyRedirected_Object = MibScalar
hourlyRedirected = _HourlyRedirected_Object(
    (1, 3, 6, 1, 4, 1, 20632, 2, 58),
    _HourlyRedirected_Type()
)
hourlyRedirected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hourlyRedirected.setStatus("current")
_TotalSent_Type = Integer32
_TotalSent_Object = MibScalar
totalSent = _TotalSent_Object(
    (1, 3, 6, 1, 4, 1, 20632, 2, 59),
    _TotalSent_Type()
)
totalSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalSent.setStatus("current")
_DailySent_Type = Integer32
_DailySent_Object = MibScalar
dailySent = _DailySent_Object(
    (1, 3, 6, 1, 4, 1, 20632, 2, 60),
    _DailySent_Type()
)
dailySent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dailySent.setStatus("current")
_HourlySent_Type = Integer32
_HourlySent_Object = MibScalar
hourlySent = _HourlySent_Object(
    (1, 3, 6, 1, 4, 1, 20632, 2, 61),
    _HourlySent_Type()
)
hourlySent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hourlySent.setStatus("current")
_DomainCount_Type = Integer32
_DomainCount_Object = MibScalar
domainCount = _DomainCount_Object(
    (1, 3, 6, 1, 4, 1, 20632, 2, 62),
    _DomainCount_Type()
)
domainCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    domainCount.setStatus("current")

# Managed Objects groups


# Notification objects

cpuFanDead = NotificationType(
    (1, 3, 6, 1, 4, 1, 20632, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cpuFanDead.setStatus(
        "current"
    )

sysFanDead = NotificationType(
    (1, 3, 6, 1, 4, 1, 20632, 2, 1, 3)
)
if mibBuilder.loadTexts:
    sysFanDead.setStatus(
        "current"
    )

cpuTempHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 20632, 2, 1, 4)
)
if mibBuilder.loadTexts:
    cpuTempHigh.setStatus(
        "current"
    )

firmwareStorageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 20632, 2, 1, 5)
)
if mibBuilder.loadTexts:
    firmwareStorageHigh.setStatus(
        "current"
    )

mailStorageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 20632, 2, 1, 6)
)
if mibBuilder.loadTexts:
    mailStorageHigh.setStatus(
        "current"
    )

raidDegrading = NotificationType(
    (1, 3, 6, 1, 4, 1, 20632, 2, 1, 7)
)
if mibBuilder.loadTexts:
    raidDegrading.setStatus(
        "current"
    )

inQueueHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 20632, 2, 1, 8)
)
inQueueHigh.setObjects(
    ("Barracuda-SPAM", "inQueueSize")
)
if mibBuilder.loadTexts:
    inQueueHigh.setStatus(
        "current"
    )

outQueueHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 20632, 2, 1, 9)
)
outQueueHigh.setObjects(
    ("Barracuda-SPAM", "outQueueSize")
)
if mibBuilder.loadTexts:
    outQueueHigh.setStatus(
        "current"
    )

deferredQueueHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 20632, 2, 1, 10)
)
deferredQueueHigh.setObjects(
    ("Barracuda-SPAM", "deferredQueueSize")
)
if mibBuilder.loadTexts:
    deferredQueueHigh.setStatus(
        "current"
    )

latencyHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 20632, 2, 1, 11)
)
latencyHigh.setObjects(
    ("Barracuda-SPAM", "avgEmailLatency")
)
if mibBuilder.loadTexts:
    latencyHigh.setStatus(
        "current"
    )

noMail = NotificationType(
    (1, 3, 6, 1, 4, 1, 20632, 2, 1, 12)
)
if mibBuilder.loadTexts:
    noMail.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Barracuda-SPAM",
    **{"Boolean": Boolean,
       "bspam": bspam,
       "bspamtraps": bspamtraps,
       "cpuFanDead": cpuFanDead,
       "sysFanDead": sysFanDead,
       "cpuTempHigh": cpuTempHigh,
       "firmwareStorageHigh": firmwareStorageHigh,
       "mailStorageHigh": mailStorageHigh,
       "raidDegrading": raidDegrading,
       "inQueueHigh": inQueueHigh,
       "outQueueHigh": outQueueHigh,
       "deferredQueueHigh": deferredQueueHigh,
       "latencyHigh": latencyHigh,
       "noMail": noMail,
       "inQueueSize": inQueueSize,
       "outQueueSize": outQueueSize,
       "deferredQueueSize": deferredQueueSize,
       "avgEmailLatency": avgEmailLatency,
       "notifyQueueSize": notifyQueueSize,
       "encryptionEnabled": encryptionEnabled,
       "hybridEnabled": hybridEnabled,
       "lastMessageDelivery": lastMessageDelivery,
       "uniqueRecipients": uniqueRecipients,
       "systemLoad": systemLoad,
       "sysFanSpeed": sysFanSpeed,
       "cpuFanSpeed": cpuFanSpeed,
       "cpuTemperature": cpuTemperature,
       "firmwareStorage": firmwareStorage,
       "maillogStorage": maillogStorage,
       "raidStatus": raidStatus,
       "totalInboundBlocked": totalInboundBlocked,
       "dailyInboundBlocked": dailyInboundBlocked,
       "hourlyInboundBlocked": hourlyInboundBlocked,
       "totalInboundVirusBlocked": totalInboundVirusBlocked,
       "dailyInboundVirusBlocked": dailyInboundVirusBlocked,
       "hourlyInboundVirusBlocked": hourlyInboundVirusBlocked,
       "totalInboundRateControlled": totalInboundRateControlled,
       "dailyInboundRateControlled": dailyInboundRateControlled,
       "hourlyInboundRateControlled": hourlyInboundRateControlled,
       "totalInboundQuarantined": totalInboundQuarantined,
       "dailyInboundQuarantined": dailyInboundQuarantined,
       "hourlyInboundQuarantined": hourlyInboundQuarantined,
       "totalInboundTagged": totalInboundTagged,
       "dailyInboundTagged": dailyInboundTagged,
       "hourlyInboundTagged": hourlyInboundTagged,
       "totalAllowed": totalAllowed,
       "dailyAllowed": dailyAllowed,
       "hourlyAllowed": hourlyAllowed,
       "totalOutboundPolicyBlocked": totalOutboundPolicyBlocked,
       "dailyOutboundPolicyBlocked": dailyOutboundPolicyBlocked,
       "hourlyOutboundPolicyBlocked": hourlyOutboundPolicyBlocked,
       "totalOutboundSpamBlocked": totalOutboundSpamBlocked,
       "dailyOutboundSpamBlocked": dailyOutboundSpamBlocked,
       "hourlyOutboundSpamBlocked": hourlyOutboundSpamBlocked,
       "totalOutboundVirusBlocked": totalOutboundVirusBlocked,
       "dailyOutboundVirusBlocked": dailyOutboundVirusBlocked,
       "hourlyOutboundVirusBlocked": hourlyOutboundVirusBlocked,
       "totalOutboundRateControlled": totalOutboundRateControlled,
       "dailyOutboundRateControlled": dailyOutboundRateControlled,
       "hourlyOutboundRateControlled": hourlyOutboundRateControlled,
       "totalOutboundQuarantined": totalOutboundQuarantined,
       "dailyOutboundQuarantined": dailyOutboundQuarantined,
       "hourlyOutboundQuarantined": hourlyOutboundQuarantined,
       "totalEncrypted": totalEncrypted,
       "dailyEncrypted": dailyEncrypted,
       "hourlyEncrypted": hourlyEncrypted,
       "totalRedirected": totalRedirected,
       "dailyRedirected": dailyRedirected,
       "hourlyRedirected": hourlyRedirected,
       "totalSent": totalSent,
       "dailySent": dailySent,
       "hourlySent": hourlySent,
       "domainCount": domainCount}
)
