# SNMP MIB module (AGARI-DATA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/agari_50625/AGARI-DATA-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 12:47:15 2025
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

agariData = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 50625)
)
if mibBuilder.loadTexts:
    agariData.setRevisions(
        ("2017-09-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AgariSensor_ObjectIdentity = ObjectIdentity
agariSensor = _AgariSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50625, 1)
)
_SensorRates_ObjectIdentity = ObjectIdentity
sensorRates = _SensorRates_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50625, 1, 1)
)
_MessagesReceivedRate_Type = Integer32
_MessagesReceivedRate_Object = MibScalar
messagesReceivedRate = _MessagesReceivedRate_Object(
    (1, 3, 6, 1, 4, 1, 50625, 1, 1, 1),
    _MessagesReceivedRate_Type()
)
messagesReceivedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    messagesReceivedRate.setStatus("current")
_MessagesScoredRate_Type = Integer32
_MessagesScoredRate_Object = MibScalar
messagesScoredRate = _MessagesScoredRate_Object(
    (1, 3, 6, 1, 4, 1, 50625, 1, 1, 2),
    _MessagesScoredRate_Type()
)
messagesScoredRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    messagesScoredRate.setStatus("current")
_MessagesDeliveredRate_Type = Integer32
_MessagesDeliveredRate_Object = MibScalar
messagesDeliveredRate = _MessagesDeliveredRate_Object(
    (1, 3, 6, 1, 4, 1, 50625, 1, 1, 3),
    _MessagesDeliveredRate_Type()
)
messagesDeliveredRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    messagesDeliveredRate.setStatus("current")
_MessagesTimedOutRate_Type = Integer32
_MessagesTimedOutRate_Object = MibScalar
messagesTimedOutRate = _MessagesTimedOutRate_Object(
    (1, 3, 6, 1, 4, 1, 50625, 1, 1, 4),
    _MessagesTimedOutRate_Type()
)
messagesTimedOutRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    messagesTimedOutRate.setStatus("current")
_SensorQueues_ObjectIdentity = ObjectIdentity
sensorQueues = _SensorQueues_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50625, 1, 2)
)
_ScoringQueueDepth_Type = Integer32
_ScoringQueueDepth_Object = MibScalar
scoringQueueDepth = _ScoringQueueDepth_Object(
    (1, 3, 6, 1, 4, 1, 50625, 1, 2, 1),
    _ScoringQueueDepth_Type()
)
scoringQueueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scoringQueueDepth.setStatus("current")
_DeliveryQueueDepth_Type = Integer32
_DeliveryQueueDepth_Object = MibScalar
deliveryQueueDepth = _DeliveryQueueDepth_Object(
    (1, 3, 6, 1, 4, 1, 50625, 1, 2, 2),
    _DeliveryQueueDepth_Type()
)
deliveryQueueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deliveryQueueDepth.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AGARI-DATA-MIB",
    **{"agariData": agariData,
       "agariSensor": agariSensor,
       "sensorRates": sensorRates,
       "messagesReceivedRate": messagesReceivedRate,
       "messagesScoredRate": messagesScoredRate,
       "messagesDeliveredRate": messagesDeliveredRate,
       "messagesTimedOutRate": messagesTimedOutRate,
       "sensorQueues": sensorQueues,
       "scoringQueueDepth": scoringQueueDepth,
       "deliveryQueueDepth": deliveryQueueDepth}
)
