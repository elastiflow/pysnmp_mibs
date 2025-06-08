# SNMP MIB module (KHOMP-UMG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/khomp_32624/KHOMP-UMG-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 10:59:33 2025
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

(KhompOperStatus,
 app) = mibBuilder.importSymbols(
    "KHOMP-MIB",
    "KhompOperStatus",
    "app")

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

umg = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 32624, 3, 4)
)
if mibBuilder.loadTexts:
    umg.setRevisions(
        ("2021-06-30 13:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class UmgNapType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("sip", 0),
          ("trunk", 1),
          ("gsm", 2),
          ("fxo", 3),
          ("fxs", 4))
    )



class UmgSipNapRegisterState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("noRegister", 0),
          ("registerSent", 1),
          ("unregisterSent", 2),
          ("registered", 3),
          ("registerError", 4))
    )



class UmgSipNapKeepAliveState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("keepAliveDisabled", 0),
          ("keepAliveSent", 1),
          ("keepAliveSuccess", 2),
          ("keepAliveFail", 3),
          ("keepAliveRetry", 4))
    )



# MIB Managed Objects in the order of their OIDs

_UmgMIBObjects_ObjectIdentity = ObjectIdentity
umgMIBObjects = _UmgMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32624, 3, 4, 1)
)
_UmgNap_ObjectIdentity = ObjectIdentity
umgNap = _UmgNap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32624, 3, 4, 1, 1)
)
_UmgNapCount_Type = Gauge32
_UmgNapCount_Object = MibScalar
umgNapCount = _UmgNapCount_Object(
    (1, 3, 6, 1, 4, 1, 32624, 3, 4, 1, 1, 1),
    _UmgNapCount_Type()
)
umgNapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umgNapCount.setStatus("current")
_UmgNapTable_Object = MibTable
umgNapTable = _UmgNapTable_Object(
    (1, 3, 6, 1, 4, 1, 32624, 3, 4, 1, 1, 2)
)
if mibBuilder.loadTexts:
    umgNapTable.setStatus("current")
_UmgNapEntry_Object = MibTableRow
umgNapEntry = _UmgNapEntry_Object(
    (1, 3, 6, 1, 4, 1, 32624, 3, 4, 1, 1, 2, 1)
)
umgNapEntry.setIndexNames(
    (0, "KHOMP-UMG-MIB", "umgNapIndex"),
)
if mibBuilder.loadTexts:
    umgNapEntry.setStatus("current")
_UmgNapIndex_Type = Unsigned32
_UmgNapIndex_Object = MibTableColumn
umgNapIndex = _UmgNapIndex_Object(
    (1, 3, 6, 1, 4, 1, 32624, 3, 4, 1, 1, 2, 1, 1),
    _UmgNapIndex_Type()
)
umgNapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    umgNapIndex.setStatus("current")
_UmgNapName_Type = DisplayString
_UmgNapName_Object = MibTableColumn
umgNapName = _UmgNapName_Object(
    (1, 3, 6, 1, 4, 1, 32624, 3, 4, 1, 1, 2, 1, 2),
    _UmgNapName_Type()
)
umgNapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umgNapName.setStatus("current")
_UmgNapType_Type = UmgNapType
_UmgNapType_Object = MibTableColumn
umgNapType = _UmgNapType_Object(
    (1, 3, 6, 1, 4, 1, 32624, 3, 4, 1, 1, 2, 1, 3),
    _UmgNapType_Type()
)
umgNapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umgNapType.setStatus("current")
_UmgNapOperStatus_Type = KhompOperStatus
_UmgNapOperStatus_Object = MibTableColumn
umgNapOperStatus = _UmgNapOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 32624, 3, 4, 1, 1, 2, 1, 4),
    _UmgNapOperStatus_Type()
)
umgNapOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umgNapOperStatus.setStatus("current")
_UmgNapChannelFailCount_Type = Gauge32
_UmgNapChannelFailCount_Object = MibTableColumn
umgNapChannelFailCount = _UmgNapChannelFailCount_Object(
    (1, 3, 6, 1, 4, 1, 32624, 3, 4, 1, 1, 2, 1, 5),
    _UmgNapChannelFailCount_Type()
)
umgNapChannelFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umgNapChannelFailCount.setStatus("current")
_UmgNapChannelIdleCount_Type = Gauge32
_UmgNapChannelIdleCount_Object = MibTableColumn
umgNapChannelIdleCount = _UmgNapChannelIdleCount_Object(
    (1, 3, 6, 1, 4, 1, 32624, 3, 4, 1, 1, 2, 1, 6),
    _UmgNapChannelIdleCount_Type()
)
umgNapChannelIdleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umgNapChannelIdleCount.setStatus("current")
_UmgNapChannelBusyCount_Type = Gauge32
_UmgNapChannelBusyCount_Object = MibTableColumn
umgNapChannelBusyCount = _UmgNapChannelBusyCount_Object(
    (1, 3, 6, 1, 4, 1, 32624, 3, 4, 1, 1, 2, 1, 7),
    _UmgNapChannelBusyCount_Type()
)
umgNapChannelBusyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umgNapChannelBusyCount.setStatus("current")
_UmgSipNap_ObjectIdentity = ObjectIdentity
umgSipNap = _UmgSipNap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32624, 3, 4, 1, 1, 3)
)
_UmgSipNapCount_Type = Gauge32
_UmgSipNapCount_Object = MibScalar
umgSipNapCount = _UmgSipNapCount_Object(
    (1, 3, 6, 1, 4, 1, 32624, 3, 4, 1, 1, 3, 1),
    _UmgSipNapCount_Type()
)
umgSipNapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umgSipNapCount.setStatus("current")
_UmgSipNapTable_Object = MibTable
umgSipNapTable = _UmgSipNapTable_Object(
    (1, 3, 6, 1, 4, 1, 32624, 3, 4, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    umgSipNapTable.setStatus("current")
_UmgSipNapEntry_Object = MibTableRow
umgSipNapEntry = _UmgSipNapEntry_Object(
    (1, 3, 6, 1, 4, 1, 32624, 3, 4, 1, 1, 3, 2, 1)
)
umgSipNapEntry.setIndexNames(
    (0, "KHOMP-UMG-MIB", "umgSipNapIndex"),
)
if mibBuilder.loadTexts:
    umgSipNapEntry.setStatus("current")
_UmgSipNapIndex_Type = Unsigned32
_UmgSipNapIndex_Object = MibTableColumn
umgSipNapIndex = _UmgSipNapIndex_Object(
    (1, 3, 6, 1, 4, 1, 32624, 3, 4, 1, 1, 3, 2, 1, 1),
    _UmgSipNapIndex_Type()
)
umgSipNapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    umgSipNapIndex.setStatus("current")
_UmgSipNapName_Type = DisplayString
_UmgSipNapName_Object = MibTableColumn
umgSipNapName = _UmgSipNapName_Object(
    (1, 3, 6, 1, 4, 1, 32624, 3, 4, 1, 1, 3, 2, 1, 2),
    _UmgSipNapName_Type()
)
umgSipNapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umgSipNapName.setStatus("current")
_UmgSipNapOperStatus_Type = KhompOperStatus
_UmgSipNapOperStatus_Object = MibTableColumn
umgSipNapOperStatus = _UmgSipNapOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 32624, 3, 4, 1, 1, 3, 2, 1, 3),
    _UmgSipNapOperStatus_Type()
)
umgSipNapOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umgSipNapOperStatus.setStatus("current")
_UmgSipNapRegister_Type = UmgSipNapRegisterState
_UmgSipNapRegister_Object = MibTableColumn
umgSipNapRegister = _UmgSipNapRegister_Object(
    (1, 3, 6, 1, 4, 1, 32624, 3, 4, 1, 1, 3, 2, 1, 4),
    _UmgSipNapRegister_Type()
)
umgSipNapRegister.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umgSipNapRegister.setStatus("current")
_UmgSipNapKeepAlive_Type = UmgSipNapKeepAliveState
_UmgSipNapKeepAlive_Object = MibTableColumn
umgSipNapKeepAlive = _UmgSipNapKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 32624, 3, 4, 1, 1, 3, 2, 1, 5),
    _UmgSipNapKeepAlive_Type()
)
umgSipNapKeepAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umgSipNapKeepAlive.setStatus("current")
_UmgMIBConformance_ObjectIdentity = ObjectIdentity
umgMIBConformance = _UmgMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32624, 3, 4, 2)
)
_UmgMIBCompliances_ObjectIdentity = ObjectIdentity
umgMIBCompliances = _UmgMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32624, 3, 4, 2, 1)
)
_UmgMIBGroups_ObjectIdentity = ObjectIdentity
umgMIBGroups = _UmgMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32624, 3, 4, 2, 2)
)
_UmgNapGroups_ObjectIdentity = ObjectIdentity
umgNapGroups = _UmgNapGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32624, 3, 4, 2, 2, 1)
)
_UmgSipNapGroups_ObjectIdentity = ObjectIdentity
umgSipNapGroups = _UmgSipNapGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32624, 3, 4, 2, 2, 1, 2)
)

# Managed Objects groups

umgNapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 32624, 3, 4, 2, 2, 1, 1)
)
umgNapGroup.setObjects(
      *(("KHOMP-UMG-MIB", "umgNapCount"),
        ("KHOMP-UMG-MIB", "umgNapName"),
        ("KHOMP-UMG-MIB", "umgNapType"),
        ("KHOMP-UMG-MIB", "umgNapOperStatus"),
        ("KHOMP-UMG-MIB", "umgNapChannelFailCount"),
        ("KHOMP-UMG-MIB", "umgNapChannelIdleCount"),
        ("KHOMP-UMG-MIB", "umgNapChannelBusyCount"))
)
if mibBuilder.loadTexts:
    umgNapGroup.setStatus("current")

umgSipNapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 32624, 3, 4, 2, 2, 1, 2, 1)
)
umgSipNapGroup.setObjects(
      *(("KHOMP-UMG-MIB", "umgSipNapCount"),
        ("KHOMP-UMG-MIB", "umgSipNapName"),
        ("KHOMP-UMG-MIB", "umgSipNapOperStatus"),
        ("KHOMP-UMG-MIB", "umgSipNapRegister"),
        ("KHOMP-UMG-MIB", "umgSipNapKeepAlive"))
)
if mibBuilder.loadTexts:
    umgSipNapGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

umgMIBFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 32624, 3, 4, 2, 1, 1)
)
umgMIBFullCompliance.setObjects(
    ("KHOMP-UMG-MIB", "umgNapGroup")
)
if mibBuilder.loadTexts:
    umgMIBFullCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "KHOMP-UMG-MIB",
    **{"UmgNapType": UmgNapType,
       "UmgSipNapRegisterState": UmgSipNapRegisterState,
       "UmgSipNapKeepAliveState": UmgSipNapKeepAliveState,
       "umg": umg,
       "umgMIBObjects": umgMIBObjects,
       "umgNap": umgNap,
       "umgNapCount": umgNapCount,
       "umgNapTable": umgNapTable,
       "umgNapEntry": umgNapEntry,
       "umgNapIndex": umgNapIndex,
       "umgNapName": umgNapName,
       "umgNapType": umgNapType,
       "umgNapOperStatus": umgNapOperStatus,
       "umgNapChannelFailCount": umgNapChannelFailCount,
       "umgNapChannelIdleCount": umgNapChannelIdleCount,
       "umgNapChannelBusyCount": umgNapChannelBusyCount,
       "umgSipNap": umgSipNap,
       "umgSipNapCount": umgSipNapCount,
       "umgSipNapTable": umgSipNapTable,
       "umgSipNapEntry": umgSipNapEntry,
       "umgSipNapIndex": umgSipNapIndex,
       "umgSipNapName": umgSipNapName,
       "umgSipNapOperStatus": umgSipNapOperStatus,
       "umgSipNapRegister": umgSipNapRegister,
       "umgSipNapKeepAlive": umgSipNapKeepAlive,
       "umgMIBConformance": umgMIBConformance,
       "umgMIBCompliances": umgMIBCompliances,
       "umgMIBFullCompliance": umgMIBFullCompliance,
       "umgMIBGroups": umgMIBGroups,
       "umgNapGroups": umgNapGroups,
       "umgNapGroup": umgNapGroup,
       "umgSipNapGroups": umgSipNapGroups,
       "umgSipNapGroup": umgSipNapGroup}
)
