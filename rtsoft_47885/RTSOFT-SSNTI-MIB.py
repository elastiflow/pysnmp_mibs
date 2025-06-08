# SNMP MIB module (RTSOFT-SSNTI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/rtsoft_47885/RTSOFT-SSNTI-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:56:06 2025
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

rtsoft = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 47885)
)
if mibBuilder.loadTexts:
    rtsoft.setRevisions(
        ("2016-05-24 00:01",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Software_ObjectIdentity = ObjectIdentity
software = _Software_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47885, 1)
)
_Ssnti_ObjectIdentity = ObjectIdentity
ssnti = _Ssnti_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47885, 1, 1)
)
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47885, 1, 1, 2)
)
_TrapNotif_ObjectIdentity = ObjectIdentity
trapNotif = _TrapNotif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47885, 1, 1, 2, 0)
)
_TrapState_ObjectIdentity = ObjectIdentity
trapState = _TrapState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47885, 1, 1, 2, 1)
)
_ErrorCode_Type = Integer32
_ErrorCode_Object = MibScalar
errorCode = _ErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 47885, 1, 1, 2, 1, 1),
    _ErrorCode_Type()
)
errorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorCode.setStatus("current")
_ErrorMessage_Type = OctetString
_ErrorMessage_Object = MibScalar
errorMessage = _ErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 47885, 1, 1, 2, 1, 2),
    _ErrorMessage_Type()
)
errorMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorMessage.setStatus("current")
_SystemName_Type = OctetString
_SystemName_Object = MibScalar
systemName = _SystemName_Object(
    (1, 3, 6, 1, 4, 1, 47885, 1, 1, 2, 1, 3),
    _SystemName_Type()
)
systemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemName.setStatus("current")
_SystemAddress_Type = OctetString
_SystemAddress_Object = MibScalar
systemAddress = _SystemAddress_Object(
    (1, 3, 6, 1, 4, 1, 47885, 1, 1, 2, 1, 4),
    _SystemAddress_Type()
)
systemAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemAddress.setStatus("current")
_ChannelType_Type = OctetString
_ChannelType_Object = MibScalar
channelType = _ChannelType_Object(
    (1, 3, 6, 1, 4, 1, 47885, 1, 1, 2, 1, 5),
    _ChannelType_Type()
)
channelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelType.setStatus("current")

# Managed Objects groups

objGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47885, 1, 1, 2, 2)
)
objGroup.setObjects(
      *(("RTSOFT-SSNTI-MIB", "errorCode"),
        ("RTSOFT-SSNTI-MIB", "errorMessage"),
        ("RTSOFT-SSNTI-MIB", "systemName"),
        ("RTSOFT-SSNTI-MIB", "systemAddress"),
        ("RTSOFT-SSNTI-MIB", "channelType"))
)
if mibBuilder.loadTexts:
    objGroup.setStatus("current")


# Notification objects

sysConnectError = NotificationType(
    (1, 3, 6, 1, 4, 1, 47885, 1, 1, 2, 0, 6)
)
sysConnectError.setObjects(
      *(("RTSOFT-SSNTI-MIB", "errorCode"),
        ("RTSOFT-SSNTI-MIB", "errorMessage"),
        ("RTSOFT-SSNTI-MIB", "systemName"),
        ("RTSOFT-SSNTI-MIB", "systemAddress"),
        ("RTSOFT-SSNTI-MIB", "channelType"))
)
if mibBuilder.loadTexts:
    sysConnectError.setStatus(
        "current"
    )

sysConnectOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 47885, 1, 1, 2, 0, 7)
)
sysConnectOk.setObjects(
      *(("RTSOFT-SSNTI-MIB", "errorCode"),
        ("RTSOFT-SSNTI-MIB", "errorMessage"),
        ("RTSOFT-SSNTI-MIB", "systemName"),
        ("RTSOFT-SSNTI-MIB", "systemAddress"),
        ("RTSOFT-SSNTI-MIB", "channelType"))
)
if mibBuilder.loadTexts:
    sysConnectOk.setStatus(
        "current"
    )

dbConnectError = NotificationType(
    (1, 3, 6, 1, 4, 1, 47885, 1, 1, 2, 0, 8)
)
dbConnectError.setObjects(
      *(("RTSOFT-SSNTI-MIB", "errorCode"),
        ("RTSOFT-SSNTI-MIB", "errorMessage"),
        ("RTSOFT-SSNTI-MIB", "systemName"),
        ("RTSOFT-SSNTI-MIB", "systemAddress"),
        ("RTSOFT-SSNTI-MIB", "channelType"))
)
if mibBuilder.loadTexts:
    dbConnectError.setStatus(
        "current"
    )

dbConnectOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 47885, 1, 1, 2, 0, 9)
)
dbConnectOk.setObjects(
      *(("RTSOFT-SSNTI-MIB", "errorCode"),
        ("RTSOFT-SSNTI-MIB", "errorMessage"),
        ("RTSOFT-SSNTI-MIB", "systemName"),
        ("RTSOFT-SSNTI-MIB", "systemAddress"),
        ("RTSOFT-SSNTI-MIB", "channelType"))
)
if mibBuilder.loadTexts:
    dbConnectOk.setStatus(
        "current"
    )


# Notifications groups

trapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 47885, 1, 1, 2, 3)
)
trapsGroup.setObjects(
      *(("RTSOFT-SSNTI-MIB", "sysConnectError"),
        ("RTSOFT-SSNTI-MIB", "sysConnectOk"),
        ("RTSOFT-SSNTI-MIB", "dbConnectError"),
        ("RTSOFT-SSNTI-MIB", "dbConnectOk"))
)
if mibBuilder.loadTexts:
    trapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ssntiCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 47885, 1, 1, 3)
)
ssntiCompliance.setObjects(
      *(("RTSOFT-SSNTI-MIB", "objGroup"),
        ("RTSOFT-SSNTI-MIB", "trapsGroup"))
)
if mibBuilder.loadTexts:
    ssntiCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RTSOFT-SSNTI-MIB",
    **{"rtsoft": rtsoft,
       "software": software,
       "ssnti": ssnti,
       "traps": traps,
       "trapNotif": trapNotif,
       "sysConnectError": sysConnectError,
       "sysConnectOk": sysConnectOk,
       "dbConnectError": dbConnectError,
       "dbConnectOk": dbConnectOk,
       "trapState": trapState,
       "errorCode": errorCode,
       "errorMessage": errorMessage,
       "systemName": systemName,
       "systemAddress": systemAddress,
       "channelType": channelType,
       "objGroup": objGroup,
       "trapsGroup": trapsGroup,
       "ssntiCompliance": ssntiCompliance}
)
